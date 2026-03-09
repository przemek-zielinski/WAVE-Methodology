"""
WAVE Living Patterns — Auto-Refinement v3
Token-optimized: two-step check (header-first, full doc only if changes found).
Bilingual: detects EN/PL from filename suffix, responds in matching language.

Step 1: Send ONLY header (~200 tokens) → "any changes since [date]?"
  → If no → done (~1500 tokens total)
  → If yes → Step 2
Step 2: Send FULL document → "apply changes" (~12000 tokens)

Saves ~80% tokens in months when nothing changes.
"""

import os
import sys
import glob
import json
from datetime import datetime, timezone
from pathlib import Path

import anthropic


PATTERNS_DIR = "living-patterns/patterns/official"
MODEL = "claude-sonnet-4-20250514"

PROMPT_CHECK = """You are checking whether a Living Pattern document needs updating.

The document covers this area:
- Title: {title}
- Area: {area}
- Objective: {objective}
- Last updated: {last_updated}
- Language: {language}

Search the web for SIGNIFICANT changes in this area since {last_updated}.
Look for: new research, new regulations, new tools, changed best practices, new case studies.

The bar is HIGH: only changes that would affect an implementation decision count.
Minor trends, opinion pieces, or incremental updates do NOT count.

Respond in EXACTLY one of two formats:

If NO significant changes:
STATUS: CURRENT
[1-2 sentences explaining what you checked]

If changes found:
STATUS: UPDATES_FOUND
[For each change: what changed, source with date, which LP section affected, priority (critical/important/cosmetic)]
"""

PROMPT_UPDATE = """You are updating a Living Pattern document with changes you previously identified.

Here are the changes to apply:
{changes}

Here is the FULL document to update:
{document}

Rules:
- Integrate changes naturally into the existing structure
- Mark each change with [AUTO-REFINED {today}]
- Update the CHANGELOG table at the bottom
- Respond in {language} (same language as the document)
- Output the COMPLETE updated document — nothing else, no preamble

IMPORTANT: Output ONLY the markdown document. No commentary before or after.
"""


def find_patterns(specific_path: str = "") -> list[Path]:
    """Find LP files to process."""
    if specific_path:
        path = Path(specific_path)
        if path.exists():
            return [path]
        print(f"⚠ Specified path not found: {specific_path}")
        return []

    files = []
    for suffix in ["_EN.md", "_PL.md"]:
        files.extend(Path(p) for p in glob.glob(os.path.join(PATTERNS_DIR, f"LP_*{suffix}")))

    # Also check old naming without _EN/_PL
    for p in glob.glob(os.path.join(PATTERNS_DIR, "LP_*.md")):
        path = Path(p)
        if not path.stem.endswith("_EN") and not path.stem.endswith("_PL"):
            files.append(path)

    if not files:
        print(f"⚠ No Living Patterns found in {PATTERNS_DIR}")

    return sorted(set(files))


def detect_language(filepath: Path, content: str) -> str:
    """Detect language from filename suffix or content."""
    if filepath.stem.endswith("_PL"):
        return "Polish"
    if filepath.stem.endswith("_EN"):
        return "English"
    # Fallback: check content for Polish characters
    if any(c in content for c in "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"):
        return "Polish"
    return "English"


def extract_header(content: str) -> dict:
    """Extract title, area, objective, last update from LP header."""
    header = {"title": "", "area": "", "objective": "", "last_updated": "Unknown"}

    for line in content.split("\n")[:30]:
        if line.startswith("# Living Pattern:"):
            header["title"] = line.replace("# ", "").strip()
            header["area"] = header["title"].replace("Living Pattern: ", "").split("—")[0].strip()
        if "Objective" in line or "objective" in line or "Funkcja celu" in line:
            header["objective"] = line.split(":", 1)[-1].strip().strip("*")
        if "Version" in line or "version" in line or "Wersja" in line:
            for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
                          "sty", "lut", "mar", "kwi", "maj", "cze",
                          "lip", "sie", "wrz", "paź", "lis", "gru"]:
                if month.lower() in line.lower():
                    header["last_updated"] = line.split("|")[-1].strip() if "|" in line else line.strip()
                    break

    return header


def call_api(client: anthropic.Anthropic, prompt: str, max_tokens: int, use_search: bool = False) -> str:
    """Single API call. Returns text content."""
    kwargs = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }
    if use_search:
        kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]

    response = client.messages.create(**kwargs)

    text = ""
    for block in response.content:
        if block.type == "text":
            text += block.text
    return text.strip()


def refine_pattern(client: anthropic.Anthropic, filepath: Path, dry_run: bool) -> bool:
    """Two-step refinement. Returns True if changes were made."""
    print(f"\n{'='*60}")
    print(f"Processing: {filepath.name}")
    print(f"{'='*60}")

    content = filepath.read_text(encoding="utf-8")
    language = detect_language(filepath, content)
    header = extract_header(content)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"  Language: {language}")
    print(f"  Area: {header['area']}")
    print(f"  Last updated: {header['last_updated']}")

    # --- STEP 1: Lightweight check (header only, ~1500 tokens total) ---
    print(f"  Step 1: Quick check (header only)...")

    check_prompt = PROMPT_CHECK.format(
        title=header["title"],
        area=header["area"],
        objective=header["objective"],
        last_updated=header["last_updated"],
        language=language
    )

    try:
        check_response = call_api(client, check_prompt, max_tokens=1000, use_search=True)
    except anthropic.APIError as e:
        print(f"  ❌ API error in Step 1: {e}")
        return False

    if "STATUS: CURRENT" in check_response:
        summary = check_response.split("STATUS: CURRENT")[-1].strip()[:200]
        print(f"  ✅ Up to date. {summary}")
        return False

    if "STATUS: UPDATES_FOUND" not in check_response:
        print(f"  ⚠ Unexpected response format in Step 1. Skipping.")
        return False

    # --- STEP 2: Full update (send entire document, ~12000 tokens) ---
    changes = check_response.split("STATUS: UPDATES_FOUND")[-1].strip()
    print(f"  Step 2: Changes found — sending full document for update...")
    print(f"  Changes preview: {changes[:200]}...")

    if dry_run:
        print(f"  🏃 DRY RUN — changes detected but not applied.")
        return False

    update_prompt = PROMPT_UPDATE.format(
        changes=changes,
        document=content,
        today=today,
        language=language
    )

    try:
        updated_content = call_api(client, update_prompt, max_tokens=8000, use_search=False)
    except anthropic.APIError as e:
        print(f"  ❌ API error in Step 2: {e}")
        return False

    # Validate output starts with markdown header
    if not updated_content.startswith("#"):
        print(f"  ⚠ Response doesn't look like a document. Saving log for review.")
        log_path = filepath.parent / f"_refinement_log_{filepath.stem}_{today}.md"
        log_path.write_text(f"CHANGES:\n{changes}\n\nRESPONSE:\n{updated_content}", encoding="utf-8")
        return False

    filepath.write_text(updated_content, encoding="utf-8")
    print(f"  ✅ Updated: {filepath.name}")
    return True


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    specific_path = os.environ.get("PATTERN_PATH", "")

    print("🌊 WAVE Living Patterns — Auto-Refinement v3")
    print(f"   Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"   Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"   Target: {specific_path or 'all official patterns'}")

    patterns = find_patterns(specific_path)
    if not patterns:
        print("\nNo patterns to process.")
        sys.exit(0)

    print(f"\nFound {len(patterns)} pattern(s):")
    for p in patterns:
        lang = "PL" if p.stem.endswith("_PL") else "EN" if p.stem.endswith("_EN") else "??"
        print(f"  - {p.name} [{lang}]")

    client = anthropic.Anthropic(api_key=api_key)

    changes_made = 0
    for pattern_path in patterns:
        try:
            if refine_pattern(client, pattern_path, dry_run):
                changes_made += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(patterns)} checked, {changes_made} updated, {'DRY RUN' if dry_run else 'LIVE'}")

    if changes_made > 0 and not dry_run:
        print("📝 Changes written. GitHub Actions will create PR.")
    elif changes_made == 0:
        print("✅ All patterns current.")


if __name__ == "__main__":
    main()
