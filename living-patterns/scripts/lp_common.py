"""
WAVE Living Patterns — Pipeline Shared Module
Common utilities: Anthropic API (with web search), GitHub API, parsing.
"""

import os
import sys
import time
import json
import re
import requests
from anthropic import Anthropic

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log(msg):
    """Print to stderr so GitHub Actions captures it in logs."""
    print(msg, file=sys.stderr, flush=True)

# ---------------------------------------------------------------------------
# Anthropic API
# ---------------------------------------------------------------------------

SONNET = "claude-sonnet-4-20250514"
OPUS = "claude-sonnet-4-20250514"   # TODO: switch to Opus when testing confirms stability

RATE_LIMIT_PAUSE = 65  # seconds between API calls (Tier 1 safety)


def get_anthropic_client():
    return Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def call_api(client, prompt, model=SONNET, max_tokens=4000, use_web_search=False):
    """
    Call Anthropic API. With web search, response may contain multiple block types.
    Extracts all text blocks. Falls back to no-web-search if text is empty.
    """
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if use_web_search:
        kwargs["tools"] = [
            {"type": "web_search_20250305", "name": "web_search", "max_uses": 5}
        ]

    try:
        log(f"  API call: model={model}, max_tokens={max_tokens}, web_search={use_web_search}")
        response = client.messages.create(**kwargs)

        # Extract text from ALL content blocks (web search adds non-text blocks)
        text_parts = []
        for block in response.content:
            if hasattr(block, "text") and block.text:
                text_parts.append(block.text)

        result = "\n".join(text_parts).strip()

        if not result:
            if use_web_search:
                log("  WARNING: empty text with web search. Retrying without...")
                time.sleep(5)
                return call_api(client, prompt, model, max_tokens, use_web_search=False)
            raise ValueError("API returned empty text content")

        log(f"  API response: {len(result)} chars, stop={response.stop_reason}")
        return result

    except Exception as e:
        error_msg = str(e)
        if "rate_limit" in error_msg.lower() or "429" in error_msg:
            log(f"  Rate limit hit. Waiting {RATE_LIMIT_PAUSE}s...")
            time.sleep(RATE_LIMIT_PAUSE)
            return call_api(client, prompt, model, max_tokens, use_web_search)
        if use_web_search and "tool" in error_msg.lower():
            log(f"  Web search error: {e}. Retrying without web search...")
            time.sleep(5)
            return call_api(client, prompt, model, max_tokens, use_web_search=False)
        log(f"  API ERROR: {e}")
        raise


def call_api_with_pause(client, prompt, **kwargs):
    """Call API then pause for rate limit safety."""
    result = call_api(client, prompt, **kwargs)
    log(f"  Pausing {RATE_LIMIT_PAUSE}s for rate limit...")
    time.sleep(RATE_LIMIT_PAUSE)
    return result

# ---------------------------------------------------------------------------
# GitHub API
# ---------------------------------------------------------------------------

def _gh_headers():
    token = os.environ.get("GITHUB_TOKEN", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _gh_url(endpoint):
    repo = os.environ["GITHUB_REPOSITORY"]
    return f"https://api.github.com/repos/{repo}{endpoint}"


def gh_get(endpoint):
    r = requests.get(_gh_url(endpoint), headers=_gh_headers())
    r.raise_for_status()
    return r.json()


def gh_post(endpoint, data):
    r = requests.post(_gh_url(endpoint), headers=_gh_headers(), json=data)
    r.raise_for_status()
    return r.json() if r.text.strip() else None


def gh_put(endpoint, data):
    r = requests.put(_gh_url(endpoint), headers=_gh_headers(), json=data)
    r.raise_for_status()
    return r.json() if r.text.strip() else None


def gh_patch(endpoint, data):
    r = requests.patch(_gh_url(endpoint), headers=_gh_headers(), json=data)
    r.raise_for_status()
    return r.json() if r.text.strip() else None


def gh_delete(endpoint):
    try:
        requests.delete(_gh_url(endpoint), headers=_gh_headers())
    except Exception:
        pass


# --- Issue helpers ---

def get_issue(number):
    return gh_get(f"/issues/{number}")


def get_issue_comments(number):
    """Get all comments, sorted oldest first."""
    comments = []
    page = 1
    while True:
        batch = gh_get(f"/issues/{number}/comments?per_page=100&page={page}")
        if not batch:
            break
        comments.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return comments


def add_comment(number, body):
    """Add comment to issue. Truncates if over GitHub limit."""
    MAX_LEN = 65000
    if len(body) > MAX_LEN:
        body = body[:MAX_LEN] + "\n\n---\n*[Truncated — exceeded GitHub comment limit]*"
    return gh_post(f"/issues/{number}/comments", {"body": body})


def add_label(number, label):
    return gh_post(f"/issues/{number}/labels", {"labels": [label]})


def remove_label(number, label):
    gh_delete(f"/issues/{number}/labels/{label}")


# --- Comment search helpers ---

MARKERS = {
    "scan":   "<!-- LP_SCAN -->",
    "r1":     "<!-- LP_R1 -->",
    "r2":     "<!-- LP_R2 -->",
    "r3_en":  "<!-- LP_R3_EN -->",
    "r3_pl":  "<!-- LP_R3_PL -->",
}


def find_comment(comments, marker_key):
    """Find the LAST comment containing the specified marker."""
    marker = MARKERS[marker_key]
    for c in reversed(comments):
        if marker in c["body"]:
            return c["body"]
    return None


def extract_lp_content(comment_body, marker_key):
    """Extract Living Pattern content from comment, removing wrapper."""
    marker = MARKERS[marker_key]
    body = comment_body.replace(marker, "").strip()
    # Remove pipeline footer
    footer_idx = body.rfind("---\n*Generated by WAVE")
    if footer_idx > 0:
        body = body[:footer_idx].strip()
    return body


def find_corrections(comments, after_marker_key):
    """Find correction comments posted after the last stage result."""
    marker = MARKERS[after_marker_key]
    # Find timestamp of last stage comment
    stage_idx = -1
    for i, c in enumerate(comments):
        if marker in c["body"]:
            stage_idx = i

    if stage_idx < 0:
        return []

    corrections = []
    for c in comments[stage_idx + 1:]:
        body = c["body"].strip()
        if (body.lower().startswith("## correction") or
            body.lower().startswith("## korekta") or
            body.lower().startswith("correction:") or
            body.lower().startswith("korekta:")):
            corrections.append(body)
    return corrections


# --- Git/PR helpers ---

def get_default_branch():
    repo_info = gh_get("")
    return repo_info.get("default_branch", "main")


def get_branch_sha(branch):
    ref = gh_get(f"/git/ref/heads/{branch}")
    return ref["object"]["sha"]


def create_branch(name, from_sha):
    try:
        gh_post("/git/refs", {"ref": f"refs/heads/{name}", "sha": from_sha})
        log(f"  Created branch: {name}")
    except requests.exceptions.HTTPError as e:
        if "422" in str(e):
            log(f"  Branch {name} already exists, updating...")
            gh_patch(f"/git/refs/heads/{name}", {"sha": from_sha, "force": True})
        else:
            raise


def create_or_update_file(branch, path, content, message):
    """Create or update a file in the repo on the given branch."""
    import base64
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    # Check if file exists
    try:
        existing = gh_get(f"/contents/{path}?ref={branch}")
        sha = existing["sha"]
        gh_put(f"/contents/{path}", {
            "message": message,
            "content": encoded,
            "branch": branch,
            "sha": sha,
        })
    except requests.exceptions.HTTPError:
        gh_put(f"/contents/{path}", {
            "message": message,
            "content": encoded,
            "branch": branch,
        })
    log(f"  File written: {path}")


def create_pull_request(title, body, head_branch, base_branch):
    return gh_post("/pulls", {
        "title": title,
        "body": body,
        "head": head_branch,
        "base": base_branch,
    })


# ---------------------------------------------------------------------------
# Parsing utilities
# ---------------------------------------------------------------------------

def parse_domain_from_title(title):
    """Extract domain name from proposal Issue title."""
    # Format: "📋 LP Proposal: Living Pattern: [Domain] — [Area]"
    m = re.search(r"Living Pattern:\s*(.+?)(?:\s*[—–-]\s*(.+))?$", title)
    if m:
        domain = m.group(1).strip()
        area = (m.group(2) or "").strip()
        return domain, area
    # Fallback: take everything after last colon
    parts = title.split(":")
    if len(parts) > 1:
        return parts[-1].strip(), ""
    return title.strip(), ""


def slugify(text):
    """Convert text to filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "_", text)
    text = re.sub(r"-+", "_", text)
    return text.strip("_")[:60]


# ---------------------------------------------------------------------------
# Markdown table repair
# ---------------------------------------------------------------------------

def repair_markdown_tables(text):
    """
    Fix broken markdown tables where rows are split across multiple lines.
    
    Problem: AI models sometimes break a table row into 2+ lines, which destroys
    markdown rendering. This function detects and merges broken rows.
    
    Rules:
    - A table row is a line that starts and ends with |
    - A separator row matches |---|
    - If we're inside a table and a line doesn't start with |, 
      merge it into the previous row
    - If a line starts with | but the previous table row seems incomplete
      (fewer | than the header), merge it too
    """
    lines = text.split("\n")
    if not lines:
        return text

    repaired = []
    in_table = False
    table_cols = 0  # number of | in header row

    for line in lines:
        stripped = line.strip()

        # Detect table header/separator
        is_table_row = stripped.startswith("|") and stripped.endswith("|")
        is_separator = bool(re.match(r"^\|[\s\-:|]+\|$", stripped))

        if is_separator:
            in_table = True
            repaired.append(line)
            continue

        if is_table_row and not in_table:
            # Might be start of a table (header row) — count columns
            table_cols = stripped.count("|")
            repaired.append(line)
            continue

        if in_table:
            if is_table_row:
                # Normal table row — check if it has enough columns
                col_count = stripped.count("|")
                if col_count >= table_cols - 1:
                    # Complete row
                    repaired.append(line)
                else:
                    # Incomplete row — merge with previous
                    if repaired:
                        prev = repaired[-1].rstrip()
                        if prev.endswith("|"):
                            repaired[-1] = prev + " " + stripped.lstrip("|")
                        else:
                            repaired[-1] = prev + " " + stripped
                    else:
                        repaired.append(line)
            elif stripped == "":
                # Empty line ends the table
                in_table = False
                table_cols = 0
                repaired.append(line)
            elif stripped.startswith("|") or "|" in stripped:
                # Broken continuation with pipes — merge with previous row
                if repaired:
                    prev = repaired[-1].rstrip()
                    if prev.endswith("|"):
                        # Previous row ended with pipe, this continues it
                        repaired[-1] = prev + " " + stripped
                    else:
                        repaired[-1] = prev + " " + stripped
                else:
                    repaired.append(line)
            elif not stripped.startswith("#") and not stripped.startswith("*"):
                # Non-table text while in table context — merge with previous
                if repaired and repaired[-1].strip().startswith("|"):
                    prev = repaired[-1].rstrip()
                    if prev.endswith("|"):
                        # Insert into last cell
                        repaired[-1] = prev[:-1] + " " + stripped + " |"
                    else:
                        repaired[-1] = prev + " " + stripped
                else:
                    # Actually leaving the table
                    in_table = False
                    table_cols = 0
                    repaired.append(line)
            else:
                # Header or other markdown — table ended
                in_table = False
                table_cols = 0
                repaired.append(line)
        else:
            repaired.append(line)

    result = "\n".join(repaired)
    if result != text:
        broken_count = len(lines) - len(repaired)
        log(f"  Table repair: merged {broken_count} broken line(s)")
    return result


def fix_orphan_dots(text):
    """
    Fix orphan dots — periods that end up alone on a new line
    instead of staying at the end of the previous sentence.
    
    Pattern: line of text\n.\n → line of text.\n
    """
    # Fix: line ending without period, followed by line with just a dot
    result = re.sub(r'([^\.\n])\s*\n\s*\.\s*\n', r'\1.\n', text)
    # Fix: line ending without period, followed by line starting with dot and space
    result = re.sub(r'([^\.\n])\s*\n\s*\.\s+', r'\1. ', result)
    # Remove standalone dot lines (just "." on a line by itself)
    result = re.sub(r'\n\s*\.\s*\n', '\n\n', result)
    if result != text:
        log(f"  Orphan dots: fixed")
    return result


def fix_broken_lines(text):
    """
    Fix broken prose lines — where a sentence is split across two lines
    despite having room to continue on the same line.
    
    Problem: AI models sometimes break mid-sentence at citation boundaries:
        "Research reveals a landscape where\n70% of organizations will adopt AI\n, yet..."
    Should be: "Research reveals a landscape where 70% of organizations will adopt AI, yet..."
    
    Rules:
    - Only merge lines that are clearly continuation of prose (not markdown elements)
    - Don't touch: headers (#), lists (- or *), tables (|), blank lines, code blocks (```)
    - Don't touch: lines that start a new paragraph (after blank line)
    - Merge: lines that start with lowercase, digit, comma, period, or opening paren
      and follow a non-blank, non-structural line
    """
    lines = text.split("\n")
    if len(lines) < 2:
        return text
    
    repaired = [lines[0]]
    in_code_block = lines[0].strip().startswith("```")
    
    for i in range(1, len(lines)):
        current = lines[i]
        stripped = current.strip()
        prev_stripped = repaired[-1].strip() if repaired else ""
        
        # Track code blocks — don't touch anything inside
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            repaired.append(current)
            continue
        
        if in_code_block:
            repaired.append(current)
            continue
        
        # Don't merge if current line is a structural markdown element
        if (stripped == "" or                          # blank line
            stripped.startswith("#") or                # header
            stripped.startswith("-") or                # unordered list
            stripped.startswith("*") or                # unordered list / bold start
            stripped.startswith("|") or                # table
            stripped.startswith(">") or                # blockquote
            stripped.startswith("```") or              # code block
            re.match(r"^\d+\.", stripped) or           # ordered list
            stripped.startswith("---") or              # horizontal rule
            stripped.startswith("**") or               # bold line start
            stripped.startswith("AREA:") or            # PULSE params
            stripped.startswith("OBJECTIVE") or        # PULSE params
            stripped.startswith("CONTEXT:") or         # PULSE params
            stripped.startswith("CONSTRAINTS:")):      # PULSE params
            repaired.append(current)
            continue
        
        # Don't merge if previous line is blank or structural
        if (prev_stripped == "" or
            prev_stripped.startswith("#") or
            prev_stripped.startswith("|") or
            prev_stripped.startswith("```") or
            prev_stripped.startswith("---")):
            repaired.append(current)
            continue
        
        # Current line looks like a continuation of prose — merge it
        # (starts with lowercase, digit, comma, period, or is a quoted fragment)
        if (stripped[0].islower() or 
            stripped[0].isdigit() or 
            stripped[0] in ",;.)'" or
            (prev_stripped.endswith(",") or 
             prev_stripped.endswith("(") or
             (prev_stripped[-1:].isalpha() and not prev_stripped.endswith(".")))):
            # Merge with previous line
            repaired[-1] = repaired[-1].rstrip() + " " + stripped
        else:
            repaired.append(current)
    
    result = "\n".join(repaired)
    if result != text:
        merged = len(lines) - len(repaired)
        if merged > 0:
            log(f"  Broken lines: merged {merged} continuation(s)")
    return result


def split_concatenated_table_rows(text):
    """
    Fix tables where the separator row and data rows are all on one line.
    
    Problem: AI model generates:
        | Error | Severity | Consequence | Prevention |
        |---|---|---|---| Row1 data | Critical | Bad things | Fix it | Row2 data | Serious | ...
    
    Should be:
        | Error | Severity | Consequence | Prevention |
        |---|---|---|---|
        | Row1 data | Critical | Bad things | Fix it |
        | Row2 data | Serious | ... |
    
    Simple approach: detect separator with trailing content, split by column count.
    """
    lines = text.split("\n")
    repaired = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect separator with trailing content: |---|---|---| some text...
        sep_match = re.match(r'^(\|[\s\-:|]+\|)(.*\S.*)$', stripped)
        if sep_match:
            separator_part = sep_match.group(1).strip()
            trailing_content = sep_match.group(2).strip()
            
            # Count columns from separator
            num_cols = separator_part.count("|") - 1
            if num_cols < 2:
                repaired.append(line)
                continue
            
            # Add clean separator
            repaired.append(separator_part)
            
            # Split trailing content into table rows
            content = trailing_content.strip("|").strip()
            cells = [c.strip() for c in content.split("|")]
            
            # Group cells into rows of num_cols
            row_cells = []
            for cell in cells:
                row_cells.append(cell)
                if len(row_cells) == num_cols:
                    row_line = "| " + " | ".join(row_cells) + " |"
                    repaired.append(row_line)
                    row_cells = []
            
            # Handle leftover cells
            if row_cells:
                while len(row_cells) < num_cols:
                    row_cells.append("")
                row_line = "| " + " | ".join(row_cells) + " |"
                repaired.append(row_line)
            
            log(f"  Table split: separated concatenated rows ({num_cols} cols)")
        else:
            repaired.append(line)
    
    return "\n".join(repaired)


def fix_orphan_bullets(text):
    """
    Fix orphan bullet points where the bullet marker is on one line
    and the content is on the next line (optionally with a blank line between).
    
    Problem patterns:
        •                           →   • Source text here
        Source text here
        
        •                           →   • Source text here
                                    
        Source text here
        
        - \\n content               →   - content
    """
    # Pattern 1: bullet (• or -) alone on line, blank line, then content
    result = re.sub(
        r'^(\s*[•\-])\s*\n\s*\n(\s*)(\S)',
        r'\1 \3',
        text,
        flags=re.MULTILINE
    )
    
    # Pattern 2: bullet (• or -) alone on line, content on next line (no blank between)
    result = re.sub(
        r'^(\s*[•\-])\s*\n(\s*)([A-ZŻŹĆŁŚĄĘÓŃa-ząćęłńóśźż\d"\'])',
        r'\1 \3',
        result,
        flags=re.MULTILINE
    )
    
    if result != text:
        log(f"  Orphan bullets: fixed")
    return result


def remove_duplicate_headers(text):
    """
    Remove duplicate title blocks that the model sometimes generates.
    
    Problem: Model writes the title twice:
        Living Pattern: Intelligent Demand Sensing
        Round 2 — Verification Delta
        Living Pattern: Intelligent Demand Sensing
        Round 2 — Verification Delta
        GAPS FOUND
    
    Fix: Detect consecutive duplicate header pairs and remove the first occurrence.
    """
    lines = text.split("\n")
    if len(lines) < 4:
        return text
    
    # Find sequences where the same title block appears twice
    i = 0
    cleaned = []
    while i < len(lines):
        # Look ahead: does lines[i:i+k] repeat at lines[i+k:i+2k]?
        found_dup = False
        for block_size in range(1, 5):  # check blocks of 1-4 lines
            if i + 2 * block_size > len(lines):
                break
            block1 = [lines[i + j].strip() for j in range(block_size)]
            block2 = [lines[i + block_size + j].strip() for j in range(block_size)]
            # Check if both blocks are non-empty and identical
            if (block1 == block2 and 
                all(b for b in block1) and
                any(b.startswith("#") or "Living Pattern" in b or "Round" in b or "Runda" in b for b in block1)):
                # Skip first occurrence, keep second
                i += block_size
                found_dup = True
                log(f"  Duplicate header: removed {block_size}-line duplicate")
                break
        if not found_dup:
            cleaned.append(lines[i])
            i += 1
    
    return "\n".join(cleaned)


def fix_malformed_separators(text):
    """
    Fix table separator issues that prevent GitHub rendering:
    1. Separator has fewer columns than header → pad to match
    2. Garbage lines after separator (empty cells + dashes) → remove
    
    Root cause: model generates incomplete separators or junk lines,
    and GitHub requires EXACT column match between header and separator.
    """
    lines = text.split("\n")
    cleaned = []
    
    for line in lines:
        stripped = line.strip()
        
        # Only process lines starting with |
        if not stripped.startswith("|"):
            cleaned.append(line)
            continue
        
        # Parse cells (split by |, skip empty first/last from leading/trailing |)
        parts = stripped.split("|")
        cells = [p.strip() for p in parts[1:]]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        
        # Is this a separator-like line? (cells are only dashes, colons, or empty)
        is_separator = len(cells) > 0 and all(
            re.match(r'^[\-:\s]*$', c) for c in cells
        ) and any("-" in c for c in cells)
        
        # Is this a pure garbage line? (all cells empty or very short dashes)
        is_garbage = len(cells) > 0 and all(
            c == "" or re.match(r'^[\-\s]+$', c) for c in cells
        )
        
        if is_separator or is_garbage:
            # Find the header — last non-separator, non-garbage | line above us
            header_cols = 0
            for prev in reversed(cleaned):
                prev_s = prev.strip()
                if not prev_s.startswith("|"):
                    break
                # Check if this previous line is a real content row (not separator)
                prev_cells = [p.strip() for p in prev_s.split("|")[1:]]
                if prev_cells and prev_cells[-1] == "":
                    prev_cells = prev_cells[:-1]
                prev_has_text = any(c and not re.match(r'^[\-:\s]*$', c) for c in prev_cells)
                if prev_has_text:
                    header_cols = len(prev_cells)
                    break
            
            if is_separator and header_cols >= 2:
                # Skip if previous line is already a valid separator
                if cleaned and re.match(r'^\|[\s\-:|]+\|$', cleaned[-1].strip()):
                    continue
                # Pad separator to match header
                sep = "| " + " | ".join(["---"] * header_cols) + " |"
                cleaned.append(sep)
                continue
            
            if is_garbage:
                # Skip garbage lines entirely (duplicate separators, empty rows)
                if cleaned and re.match(r'^\|[\s\-:|]+\|$', cleaned[-1].strip()):
                    log(f"  Table fix: removed garbage line after separator")
                    continue
                # Garbage not after separator — might be malformed separator itself
                if header_cols >= 2:
                    if not any(re.match(r'^\|[\s\-:|]+\|$', c.strip()) for c in cleaned[-3:] if c.strip().startswith("|")):
                        sep = "| " + " | ".join(["---"] * header_cols) + " |"
                        cleaned.append(sep)
                    continue
                # Can't determine context — keep it
                cleaned.append(line)
                continue
        
        # Normal content row — keep as-is
        cleaned.append(line)
    
    return "\n".join(cleaned)


def cleanup_markdown(text):
    """Combined markdown cleanup: all fixes in optimal order."""
    text = remove_duplicate_headers(text)
    text = fix_malformed_separators(text)
    text = split_concatenated_table_rows(text)
    text = repair_markdown_tables(text)
    text = fix_orphan_dots(text)
    text = fix_broken_lines(text)
    text = fix_orphan_bullets(text)
    return text


# ---------------------------------------------------------------------------
# Translation prompt (shared across all pipeline stages)
# ---------------------------------------------------------------------------

TRANSLATE_PROMPT = """Translate the following document from English to Polish.

RULES:
- Natural, fluent Polish — NOT machine translation. Write as if a Polish expert wrote it originally.
- USE POLISH EQUIVALENTS where they exist naturally in professional Polish:
  compliance → zgodność, best practices → najlepsze praktyki, framework → ramy/struktura,
  data lineage → rodowód danych, traceability → identyfikowalność, emerging → wschodzący/nowy,
  stakeholder → interesariusz, scalability → skalowalność, governance → zarządzanie/nadzór,
  use case → przypadek użycia, workflow → przepływ pracy, bottleneck → wąskie gardło,
  deployment → wdrożenie, drift → dryf/dryfowanie, adversarial → kontradyktoryjny.
- Terms WITHOUT good Polish equivalent stay in English: API, ERP, AI, ROI, GDPR, SOX, SaaS, DevOps, CI/CD.
- Metric names and section headers in Polish
- Maintain all Markdown formatting exactly
- Keep source references (author names, report titles, DOIs) in original language
- The tone should be professional but accessible
- Your output must contain ONLY the translated text — no translator notes, no comments, no instructions.

DOCUMENT TO TRANSLATE:
{document}
"""
