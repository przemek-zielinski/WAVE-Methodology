"""
WAVE Living Patterns — Auto-Refinement Script
Checks official Living Patterns against current web sources
and proposes updates when relevant changes are found.

Usage:
  - Automatically via GitHub Actions (see .github/workflows/lp-auto-refine.yml)
  - Manually: ANTHROPIC_API_KEY=sk-... python auto_refine.py

Environment variables:
  ANTHROPIC_API_KEY  — required, Anthropic API key
  DRY_RUN            — optional, "true" to check without modifying files
  PATTERN_PATH       — optional, path to specific LP file (empty = all official)
"""

import os
import sys
import glob
import json
from datetime import datetime, timezone
from pathlib import Path

import anthropic


# --- Configuration ---

PATTERNS_DIR = "living-patterns/patterns/official"
MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 8000

REFINEMENT_PROMPT = """You are performing a WAVE Living Pattern auto-refinement cycle.

I'm giving you an existing Living Pattern document. Your task is to check its freshness against current knowledge.

STEPS:
1. Search the web for CHANGES in this area since the document's last update date.
   Look for: new scientific research, new industry reports, regulatory changes,
   new tools/frameworks, new case studies, changed best practices.

2. Compare findings with existing content in the Living Pattern.

3. Respond in ONE of two formats:

FORMAT A — No significant changes:
Start your response with exactly: STATUS: CURRENT
Then briefly explain what you checked and why no updates are needed.

FORMAT B — Changes found:
Start your response with exactly: STATUS: UPDATES_FOUND
Then for each change provide:
- WHAT changed (new research / new regulation / new tool / trend shift)
- SOURCE with date
- WHICH section of the Living Pattern is affected
- PROPOSED change (addition / update / removal)
- PRIORITY (critical / important / cosmetic)

Finally, provide the COMPLETE updated Living Pattern document with changes integrated.
Mark all changes with [AUTO-REFINED {today's date}].
Update the CHANGELOG table at the bottom.

IMPORTANT: Only propose changes that are SIGNIFICANT — not minor rephrasing or cosmetic edits.
The bar is: would this change affect an implementation decision?

Today's date: {today}
"""


def find_patterns(specific_path: str = "") -> list[Path]:
    """Find LP files to process."""
    if specific_path:
        path = Path(specific_path)
        if path.exists():
            return [path]
        print(f"⚠ Specified path not found: {specific_path}")
        return []

    pattern = os.path.join(PATTERNS_DIR, "LP_*.md")
    files = [Path(f) for f in glob.glob(pattern)]

    if not files:
        print(f"⚠ No Living Patterns found in {PATTERNS_DIR}")

    return sorted(files)


def extract_last_update(content: str) -> str:
    """Try to extract last update date from the document."""
    for line in content.split("\n"):
        if "Version" in line or "version" in line:
            # Look for date patterns like "March 2026", "Mar 9, 2026"
            for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
                if month in line:
                    return line.strip()
    return "Unknown"


def refine_pattern(client: anthropic.Anthropic, filepath: Path, dry_run: bool) -> bool:
    """
    Run auto-refinement on a single Living Pattern.
    Returns True if changes were made.
    """
    print(f"\n{'='*60}")
    print(f"Processing: {filepath.name}")
    print(f"{'='*60}")

    content = filepath.read_text(encoding="utf-8")
    last_update = extract_last_update(content)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"  Last update: {last_update}")
    print(f"  Checking against current sources...")

    prompt = REFINEMENT_PROMPT.format(today=today)

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            tools=[{
                "type": "web_search_20250305",
                "name": "web_search"
            }],
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}\n\n---\n\nLIVING PATTERN DOCUMENT:\n\n{content}"
                }
            ]
        )
    except anthropic.APIError as e:
        print(f"  ❌ API error: {e}")
        return False

    # Extract text from response
    response_text = ""
    for block in response.content:
        if block.type == "text":
            response_text += block.text

    if not response_text:
        print("  ❌ Empty response from API")
        return False

    # Check status
    if "STATUS: CURRENT" in response_text:
        print("  ✅ Pattern is up to date. No changes needed.")
        # Log the check
        summary = response_text.split("STATUS: CURRENT")[-1].strip()[:200]
        print(f"  Summary: {summary}")
        return False

    if "STATUS: UPDATES_FOUND" in response_text:
        print("  🔄 Updates found!")

        # Extract the updated document
        # The full updated LP should be after the analysis
        # Look for the LP header pattern
        updated_content = None
        lines = response_text.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("# Living Pattern:"):
                updated_content = "\n".join(lines[i:])
                break

        if not updated_content:
            print("  ⚠ Could not extract updated document from response.")
            print("  Full response saved to _refinement_log.md for manual review.")
            log_path = filepath.parent / f"_refinement_log_{filepath.stem}_{today}.md"
            log_path.write_text(response_text, encoding="utf-8")
            return False

        if dry_run:
            print("  🏃 DRY RUN — changes detected but not written.")
            # Show what changed
            analysis = response_text.split("# Living Pattern:")[0]
            print(f"\n  Proposed changes:\n{analysis[:500]}...")
            return False

        # Write updated file
        filepath.write_text(updated_content, encoding="utf-8")
        print(f"  ✅ Updated: {filepath.name}")
        return True

    print("  ⚠ Unexpected response format. Saving log for manual review.")
    log_path = filepath.parent / f"_refinement_log_{filepath.stem}_{today}.md"
    log_path.write_text(response_text, encoding="utf-8")
    return False


def main():
    # Check API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    specific_path = os.environ.get("PATTERN_PATH", "")

    print("🌊 WAVE Living Patterns — Auto-Refinement")
    print(f"   Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"   Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"   Target: {specific_path or 'all official patterns'}")

    # Find patterns
    patterns = find_patterns(specific_path)
    if not patterns:
        print("\nNo patterns to process. Exiting.")
        sys.exit(0)

    print(f"\nFound {len(patterns)} pattern(s) to check:")
    for p in patterns:
        print(f"  - {p.name}")

    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # Process each pattern
    changes_made = 0
    for pattern_path in patterns:
        try:
            if refine_pattern(client, pattern_path, dry_run):
                changes_made += 1
        except Exception as e:
            print(f"  ❌ Unexpected error processing {pattern_path.name}: {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Patterns checked: {len(patterns)}")
    print(f"  Changes made: {changes_made}")
    print(f"  Mode: {'DRY RUN' if dry_run else 'LIVE'}")

    if changes_made > 0 and not dry_run:
        print("\n  📝 Changes written to files. GitHub Actions will create a PR.")
    elif changes_made == 0:
        print("\n  ✅ All patterns are current. No PR needed.")


if __name__ == "__main__":
    main()
