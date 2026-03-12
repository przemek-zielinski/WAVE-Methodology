#!/usr/bin/env python3
"""
WAVE Living Patterns Pipeline — Publisher
Reads final LP from Issue comments, creates files in repo, opens Pull Request.
Triggered by 'publish' label on Issue.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from lp_common import *

def main():
    issue_number = int(os.environ["ISSUE_NUMBER"])
    log(f"{'='*60}")
    log(f"PUBLISHER — Issue #{issue_number}")
    log(f"{'='*60}")

    # 1. Read Issue
    issue = get_issue(issue_number)
    title = issue["title"]
    domain, area = parse_domain_from_title(title)
    comments = get_issue_comments(issue_number)
    log(f"Domain: {domain}, Area: {area}")

    # 2. Find best available LP content
    # Priority: R3 > R1 (R2 is delta only, not standalone)
    en_content = None
    pl_content = None
    version_note = ""

    r3_en = find_comment(comments, "r3_en")
    r3_pl = find_comment(comments, "r3_pl")
    r1 = find_comment(comments, "r1")

    if r3_en:
        en_content = extract_lp_content(r3_en, "r3_en")
        version_note = "3 rounds (R1 + R2 + R3)"
        log("Using R3 EN content")
    elif r1:
        en_content = extract_lp_content(r1, "r1")
        version_note = "Round 1 only (R2/R3 skipped)"
        log("Using R1 content (R3 not available)")
    else:
        log("ERROR: No LP content found in comments. Need at least R1.")
        sys.exit(1)

    if r3_pl:
        pl_content = extract_lp_content(r3_pl, "r3_pl")
        log("Using R3 PL content")
    else:
        log("WARNING: No PL translation found. Generating from EN...")
        # Generate PL translation
        client = get_anthropic_client()
        # For long documents, split translation into chunks
        CHUNK_THRESHOLD = 12000
        if len(en_content) <= CHUNK_THRESHOLD:
            translate_prompt = f"""Translate the following Living Pattern document from English to Polish.

RULES:
- Natural, fluent Polish — NOT machine translation
- Technical terms that have no good Polish equivalent stay in English
- Maintain all Markdown formatting exactly
- Professional but accessible tone

DOCUMENT:
{en_content}
"""
            pl_content = call_api(client, translate_prompt, model=SONNET, max_tokens=16000, use_web_search=False)
        else:
            log(f"Long document ({len(en_content)} chars) — chunked translation")
            import time
            midpoint = len(en_content) // 2
            # Find nearest ## PART boundary
            split_pos = -1
            for marker_text in ["## PART ", "## CZĘŚĆ ", "## CHANGELOG"]:
                search_zone = en_content[midpoint - 2000 : midpoint + 4000]
                idx = search_zone.rfind(marker_text)
                if idx >= 0:
                    split_pos = midpoint - 2000 + idx
                    break
            if split_pos < 0:
                search_zone = en_content[midpoint - 1000 : midpoint + 1000]
                idx = search_zone.rfind("\n\n")
                split_pos = midpoint - 1000 + idx if idx >= 0 else midpoint

            chunk1 = en_content[:split_pos].strip()
            chunk2 = en_content[split_pos:].strip()

            p1 = f"""Translate the following Living Pattern document from English to Polish.

RULES:
- Natural, fluent Polish — NOT machine translation
- Technical terms that have no good Polish equivalent stay in English
- Maintain all Markdown formatting exactly
- Professional but accessible tone
- This is PART 1 of a split document. Translate it completely.
- Your output must contain ONLY the translated text — no translator notes, no comments, no instructions.

DOCUMENT TO TRANSLATE:
{chunk1}
"""
            pl1 = call_api(client, p1, model=SONNET, max_tokens=16000, use_web_search=False)
            time.sleep(RATE_LIMIT_PAUSE)

            p2 = f"""Translate the following Living Pattern document from English to Polish.

RULES:
- Natural, fluent Polish — NOT machine translation
- Technical terms that have no good Polish equivalent stay in English
- Maintain all Markdown formatting exactly
- Professional but accessible tone
- This is PART 2 of a split document. Maintain consistent terminology with Part 1.
- Your output must contain ONLY the translated text — no translator notes, no comments, no instructions.

DOCUMENT TO TRANSLATE:
{chunk2}
"""
            pl2 = call_api(client, p2, model=SONNET, max_tokens=16000, use_web_search=False)
            pl_content = pl1.rstrip() + "\n\n" + pl2.lstrip()

        log(f"Translation generated: {len(pl_content)} chars")

    # 3. Classify broad domain category (for file prefix)
    log("Classifying domain category...")
    client = get_anthropic_client()
    classify_prompt = f"""Classify this solution domain into exactly ONE broad category.

Domain: {domain}
Area: {area}

Choose from: healthcare, education, logistics, finance, manufacturing, agriculture, legal, energy, retail, government, technology, science, media, other

Reply with ONLY the category name in lowercase. Nothing else."""

    try:
        category = call_api(client, classify_prompt, model=SONNET, max_tokens=20, use_web_search=False)
        category = category.strip().lower().split()[0].strip(".,")
        # Validate against known categories
        valid = {"healthcare", "education", "logistics", "finance", "manufacturing",
                 "agriculture", "legal", "energy", "retail", "government",
                 "technology", "science", "media", "other"}
        if category not in valid:
            log(f"  Unknown category '{category}', falling back to 'other'")
            category = "other"
    except Exception as e:
        log(f"  Classification failed: {e}, falling back to 'other'")
        category = "other"
    log(f"  Category: {category}")

    # 4. Determine file names
    slug = slugify(f"{domain}_{area}" if area else domain)
    file_en = f"living-patterns/patterns/official/LP_{category}_{slug}_v1_EN.md"
    file_pl = f"living-patterns/patterns/official/LP_{category}_{slug}_v1_PL.md"
    branch_name = f"lp/{slug}"
    log(f"Files: {file_en}, {file_pl}")
    log(f"Branch: {branch_name}")

    # 5. Create branch
    default_branch = get_default_branch()
    base_sha = get_branch_sha(default_branch)
    create_branch(branch_name, base_sha)

    # 6. Create files
    from datetime import date
    today = date.today().isoformat()

    create_or_update_file(
        branch_name, file_en, en_content,
        f"Add Living Pattern: {domain} — {area} (EN)"
    )
    create_or_update_file(
        branch_name, file_pl, pl_content,
        f"Add Living Pattern: {domain} — {area} (PL)"
    )

    # 7. Create Pull Request
    pr_body = f"""## 📋 New Living Pattern: {domain} — {area}

**Category:** {category}
**Source:** Issue #{issue_number}
**Rounds:** {version_note}
**Files:**
- `{file_en}` (English)
- `{file_pl}` (Polski)

**Pipeline:** Proposal → SCAN → PULSE ({version_note}) → Publisher

---
*Generated by WAVE Living Patterns Pipeline | {today}*
*Merge this PR to publish the Living Pattern to the official collection.*
"""

    pr = create_pull_request(
        title=f"📋 LP: {domain} — {area}",
        body=pr_body,
        head_branch=branch_name,
        base_branch=default_branch,
    )
    pr_url = pr.get("html_url", "")
    pr_number = pr.get("number", "?")
    log(f"PR created: #{pr_number} — {pr_url}")

    # 8. Comment on Issue with PR link
    add_comment(issue_number, f"""## ✅ Living Pattern Published as PR

Pull Request: **#{pr_number}** — {pr_url}

**Files created:**
- `{file_en}` (English)
- `{file_pl}` (Polski)

Merge the PR to add this Living Pattern to the official collection.

---
*WAVE Living Patterns Pipeline — Publisher | {today}*
""")

    log("PUBLISHER DONE.")


if __name__ == "__main__":
    main()
