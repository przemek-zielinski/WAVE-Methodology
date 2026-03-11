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
