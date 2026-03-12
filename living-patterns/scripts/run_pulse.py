#!/usr/bin/env python3
"""
WAVE Living Patterns Pipeline — PULSE Runner
Executes PULSE rounds (R1/R2/R3) via Anthropic API. Each round reads previous
results from Issue comments and posts its output as a new comment.
Triggered by 'scan-approved', 'r1-approved', 'r2-approved' labels.
"""

import os
import sys
import argparse

sys.path.insert(0, os.path.dirname(__file__))
from lp_common import *

# ---------------------------------------------------------------------------
# PULSE Prompt Templates
# ---------------------------------------------------------------------------

PULSE_R1 = """You are an expert in {area}. Your task is to build Round 1 (Foundation) of a Living Pattern — a comprehensive knowledge document for this implementation area.

A Living Pattern is a tool from the WAVE methodology. It captures the best available scientific, industry, and practical knowledge for a specific area, synthesized under a clear objective function.

**IMPORTANT — Web search:** USE your web search tool actively in this round. Search for:
- Scientific research: peer-reviewed papers, systematic reviews, empirical data
- Industry reports: analyst reports, technical documentation, benchmarks
- Practical knowledge: case studies, post-mortems, lessons learned from real implementations
- Current trends: what's changing in 2025-2026, emerging approaches
- Regulatory landscape: compliance requirements, standards, certifications

Search at least 3-5 different queries to build comprehensive coverage. Do NOT rely only on training data.

---

## PARAMETERS

**Area:** {area}
**Objective function:** {objective_function}
**Context:** {context}
**Constraints:** {constraints}

## SCAN ANALYSIS (for reference)
{scan_result}

---

## YOUR TASK — ROUND 1: BUILD FOUNDATION

### Step 1 — Multi-layer Research
Search the web across three layers:
- **Scientific layer:** Academic research, empirical data, theoretical foundations
- **Industry layer:** Reports, documentation, case studies from leading organizations
- **Practice layer:** Real-world experiences, common mistakes, measurable consequences

**Filter:** Every finding must answer: "How does this impact implementation toward the objective function?" If irrelevant — skip.

### Step 2 — Synthesize into Living Pattern

Write the Living Pattern in this exact structure:

```markdown
# Living Pattern: {area}
## Version 1.0 | Round 1 (Foundation)

**Objective function:** {objective_function}
**Context:** {context}
**Status:** Round 1 — awaiting verification

---

## PART I — STATE OF KNOWLEDGE
[Current state of the field. What science says. What industry does. Key numbers and data.
Organized by themes, not by sources. Every claim backed by source.]

## PART II — PRINCIPLES AND STANDARDS
[Numbered list of design/implementation principles derived from research.
Each principle: name + explanation + rationale + what happens if violated.
Minimum 10 principles.]

## PART III — ERROR MATRIX
[Table of common/critical mistakes in this area.
Columns: Error | Severity (critical/serious/subtle) | Consequence | Prevention
Minimum 15 entries across three severity levels.]

## PART IV — DECISION MATRIX
[Key implementation decisions that teams face in this area.
For each: decision description | options | recommended option | rationale]

## PART V — SUCCESS METRICS
[Measurable indicators that the implementation is on track.
Split into: Leading metrics (predict success) | Lagging metrics (confirm success) | Technical metrics]

## PART VI — SOURCES
[Organized by: Scientific | Industry | Case Studies | Regulatory]
```

## QUALITY RULES
- Be specific to THIS solution context, not generic
- Every principle must have a rationale grounded in research or practice
- Error matrix must include real-world examples where possible
- Metrics must be measurable (numbers, percentages, thresholds)
- Write in English, professional but accessible tone
- Aim for comprehensive coverage — this is the foundation that R2 and R3 will refine
"""

PULSE_R2 = """You are a critical reviewer specializing in {area}. Your task is Round 2 (Verification) of a Living Pattern — to challenge, verify, and strengthen the foundation built in Round 1.

**IMPORTANT — Web search:** USE your web search tool. Search from DIFFERENT angles than Round 1:
- Contrarian views and critiques of mainstream approaches
- Failure cases and post-mortems that Round 1 might have missed
- Adjacent fields that might offer unexpected insights
- Very recent developments (last 6 months) that could change recommendations
- Regional/regulatory differences that weren't covered

Search at least 3 new queries that Round 1 wouldn't have used.

---

## PARAMETERS

**Area:** {area}
**Objective function:** {objective_function}
**Context:** {context}

## ROUND 1 RESULT (to verify)
{r1_result}

---

## YOUR TASK — ROUND 2: VERIFY AND STRENGTHEN

Attack the Round 1 document from a different angle. Specifically:

1. **Find gaps:** What did R1 miss? What areas are suspiciously absent?
2. **Challenge assumptions:** Which principles seem weak or poorly supported?
3. **Check currency:** Is any information outdated or superseded by newer research?
4. **Test completeness:** Are there errors in the matrix that should be there but aren't?
5. **Validate metrics:** Are the success metrics actually measurable and useful?
6. **Cross-check sources:** Are there better or more authoritative sources?

## OUTPUT FORMAT

Write as a DELTA document — only what's new or changed. Do NOT reproduce Round 1 content.

```markdown
# Living Pattern: {area}
## Round 2 — Verification Delta

### GAPS FOUND
[What was missing from R1. For each gap: description + why it matters + content to add]

### CHALLENGED ASSUMPTIONS
[Which R1 claims are weak. For each: the claim + the counter-evidence + recommendation]

### UPDATED INFORMATION
[What changed since R1's sources. New data, new regulations, new tools]

### NEW ERROR MATRIX ENTRIES
[Errors that R1 missed. Same format: Error | Severity | Consequence | Prevention]

### NEW OR REVISED PRINCIPLES
[Principles to add or modify. For modifications: original + revised + why]

### METRICS ADJUSTMENTS
[New metrics to add or existing ones to revise]

### NEW SOURCES
[Sources found in R2 that strengthen or update the pattern]

### ASSESSMENT
[Overall quality of R1: what percentage was solid, what needed correction.
Estimate: how much did R2 add? (expect ~15-25% new value)]
```
"""

PULSE_R3 = """You are a master synthesizer specializing in {area}. Your task is Round 3 (Finalization) — to search peripheral directions, integrate all findings, and compose the definitive Living Pattern.

**IMPORTANT — Web search:** In this final round, search in PERIPHERAL directions:
- Adjacent disciplines that might offer unexpected insights
- Analogies from completely different fields that solved similar problems
- Cutting-edge research that hasn't yet entered mainstream practice
- Ethical and social implications that technical analysis often misses
- Future trajectories: where is this field heading in 2-3 years?

Search at least 2-3 peripheral queries. Think creatively.

---

## PARAMETERS

**Area:** {area}
**Objective function:** {objective_function}
**Context:** {context}

## ROUND 1 RESULT
{r1_result}

## ROUND 2 DELTA
{r2_result}

---

## YOUR TASK — ROUND 3: FINALIZE

1. **Peripheral search:** Look in unexpected places for insights R1 and R2 missed
2. **Integrate:** Merge R1 foundation + R2 corrections + R3 peripheral insights
3. **Compose:** Write the COMPLETE, FINAL Living Pattern

The output is the definitive document. It must be self-contained — a reader should need nothing else to understand the state of knowledge in this area.

## OUTPUT FORMAT

Write the COMPLETE Living Pattern (not a delta). Include everything from R1, corrected by R2, enriched by R3.

```markdown
# Living Pattern: {area}
## Version 1.0 | {today}

**Objective function:** {objective_function}
**Context:** {context}
**Status:** Complete — 3 rounds of PULSE analysis
**Methodology:** WAVE Living Patterns (github.com/przemek-zielinski/WAVE-Methodology)

---

## PART I — STATE OF KNOWLEDGE
[Comprehensive, current, synthesized from 3 rounds]

## PART II — PRINCIPLES AND STANDARDS
[Final numbered list — R1 principles + R2 corrections + R3 additions]

## PART III — ERROR MATRIX
[Complete matrix from all 3 rounds]

## PART IV — DECISION MATRIX
[Key decisions with recommendations]

## PART V — SUCCESS METRICS
[Leading | Lagging | Technical — validated across 3 rounds]

## PART VI — SOURCES
[All sources from 3 rounds, organized by type]

---

## CHANGELOG
- **R1 (Foundation):** Built initial knowledge base from [N] sources
- **R2 (Verification):** Found [N] gaps, corrected [N] assumptions, added [N] sources
- **R3 (Finalization):** Added peripheral insights from [fields], composed final version
```

Write comprehensively. This is the final product. Quality over brevity.
"""

TRANSLATE_PROMPT = """Translate the following Living Pattern document from English to Polish.

RULES:
- Natural, fluent Polish — NOT machine translation
- Technical terms that have no good Polish equivalent stay in English (API, framework, compliance, etc.)
- Metric names and section headers in Polish
- Maintain all Markdown formatting exactly
- Keep source references in original language
- The tone should be professional but accessible — as if a Polish expert wrote it originally

DOCUMENT TO TRANSLATE:
{document}
"""

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="PULSE Runner")
    parser.add_argument("--round", type=int, required=True, choices=[1, 2, 3])
    parser.add_argument("--issue", type=int, required=True)
    args = parser.parse_args()

    issue_number = args.issue
    round_num = args.round

    log(f"{'='*60}")
    log(f"PULSE RUNNER — Round {round_num}, Issue #{issue_number}")
    log(f"{'='*60}")

    # 1. Read Issue and comments
    issue = get_issue(issue_number)
    title = issue["title"]
    domain, area_from_title = parse_domain_from_title(title)
    comments = get_issue_comments(issue_number)
    log(f"Title: {title}")
    log(f"Comments: {len(comments)}")

    # 2. Get SCAN result (required for all rounds)
    scan_comment = find_comment(comments, "scan")
    if not scan_comment:
        log("ERROR: No SCAN result found in comments. Run SCAN first.")
        sys.exit(1)
    scan_result = extract_lp_content(scan_comment, "scan")

    # 3. Extract PULSE parameters from SCAN
    area, objective_function, context, constraints = extract_pulse_params(scan_result, domain, area_from_title)
    log(f"Area: {area}")
    log(f"Objective: {objective_function[:80]}...")

    client = get_anthropic_client()
    from datetime import date
    today = date.today().isoformat()

    # 4. Execute appropriate round
    if round_num == 1:
        run_r1(client, issue_number, comments, area, objective_function, context, constraints, scan_result, today)
    elif round_num == 2:
        run_r2(client, issue_number, comments, area, objective_function, context, today)
    elif round_num == 3:
        run_r3(client, issue_number, comments, area, objective_function, context, today)

    log(f"PULSE ROUND {round_num} DONE.")


def extract_pulse_params(scan_result, domain, area_from_title):
    """Extract PULSE parameters from SCAN result."""
    area = area_from_title or domain
    objective_function = ""
    context = ""
    constraints = "Public knowledge only. Focus on current state of art (2025-2026)."

    # Try to find PULSE Parameters block in SCAN
    lines = scan_result.split("\n")
    in_params = False
    for line in lines:
        stripped = line.strip()
        if "PULSE Parameters" in line or "PULSE parameters" in line:
            in_params = True
            continue
        if in_params:
            if stripped.startswith("```"):
                if in_params and any(k in stripped for k in ["AREA", "OBJECTIVE"]):
                    continue
                in_params = not in_params
                continue
            if stripped.upper().startswith("AREA:"):
                area = stripped.split(":", 1)[1].strip()
            elif stripped.upper().startswith("OBJECTIVE_FUNCTION:") or stripped.upper().startswith("OBJECTIVE FUNCTION:"):
                objective_function = stripped.split(":", 1)[1].strip()
            elif stripped.upper().startswith("CONTEXT:"):
                context = stripped.split(":", 1)[1].strip()
            elif stripped.upper().startswith("CONSTRAINTS:"):
                constraints = stripped.split(":", 1)[1].strip()
            elif stripped.startswith("#") or stripped.startswith("##"):
                in_params = False

    # Fallbacks
    if not objective_function:
        # Try to find from "Objective function:" anywhere in SCAN
        for line in lines:
            if "objective function" in line.lower() and ":" in line:
                objective_function = line.split(":", 1)[1].strip().strip("*").strip()
                if objective_function:
                    break
    if not objective_function:
        objective_function = f"Comprehensive implementation knowledge for {area} in {domain}"
    if not context:
        context = f"AI-powered solution in {domain} domain"

    return area, objective_function, context, constraints


def run_r1(client, issue_number, comments, area, objective_function, context, constraints, scan_result, today):
    """Execute PULSE Round 1 — Build Foundation."""
    log("--- ROUND 1: Build Foundation ---")

    # Check for corrections from previous R1 attempt
    corrections = find_corrections(comments, "r1") if find_comment(comments, "r1") else []
    correction_text = ""
    if corrections:
        log(f"Found {len(corrections)} correction(s)")
        correction_text = "\n\n## CORRECTIONS FROM REVIEWER\n" + "\n".join(corrections)

    prompt = PULSE_R1.format(
        area=area,
        objective_function=objective_function,
        context=context,
        constraints=constraints,
        scan_result=scan_result[:6000],
    ) + correction_text

    result = call_api(client, prompt, model=SONNET, max_tokens=8000, use_web_search=True)
    log(f"R1 result: {len(result)} chars")

    marker = MARKERS["r1"]
    comment_body = f"""{marker}
## 🫀 PULSE Round 1 — Foundation

{result}

---
*Generated by WAVE Living Patterns Pipeline — PULSE R1 | {today}*
*Next: review above. Add label `r1-approved` to proceed to Round 2.*
*To skip R2/R3 and publish: add label `publish`.*
*To request corrections: comment with "## Correction" then add label `redo-r1`.*
"""

    add_comment(issue_number, comment_body)
    add_label(issue_number, "r1-ready")
    log("R1 posted. Label 'r1-ready' added.")


def run_r2(client, issue_number, comments, area, objective_function, context, today):
    """Execute PULSE Round 2 — Verification."""
    log("--- ROUND 2: Verify and Strengthen ---")

    r1_comment = find_comment(comments, "r1")
    if not r1_comment:
        log("ERROR: No R1 result found. Run R1 first.")
        sys.exit(1)
    r1_result = extract_lp_content(r1_comment, "r1")

    corrections = find_corrections(comments, "r2") if find_comment(comments, "r2") else []
    correction_text = ""
    if corrections:
        correction_text = "\n\n## CORRECTIONS FROM REVIEWER\n" + "\n".join(corrections)

    prompt = PULSE_R2.format(
        area=area,
        objective_function=objective_function,
        context=context,
        r1_result=r1_result[:12000],
    ) + correction_text

    log("Calling API for R2 (with web search)...")
    result = call_api(client, prompt, model=SONNET, max_tokens=5000, use_web_search=True)
    log(f"R2 result: {len(result)} chars")

    marker = MARKERS["r2"]
    comment_body = f"""{marker}
## 🫀 PULSE Round 2 — Verification Delta

{result}

---
*Generated by WAVE Living Patterns Pipeline — PULSE R2 | {today}*
*Next: review above. Add label `r2-approved` to proceed to Round 3 (Final).*
*To skip R3 and publish R1+R2: add label `publish`.*
*To request corrections: comment with "## Correction" then add label `redo-r2`.*
"""

    add_comment(issue_number, comment_body)
    add_label(issue_number, "r2-ready")
    log("R2 posted. Label 'r2-ready' added.")


def run_r3(client, issue_number, comments, area, objective_function, context, today):
    """Execute PULSE Round 3 — Finalization + Translation."""
    log("--- ROUND 3: Finalize and Compose ---")

    r1_comment = find_comment(comments, "r1")
    r2_comment = find_comment(comments, "r2")

    if not r1_comment:
        log("ERROR: No R1 result found.")
        sys.exit(1)

    r1_result = extract_lp_content(r1_comment, "r1")
    r2_result = ""
    if r2_comment:
        r2_result = extract_lp_content(r2_comment, "r2")
    else:
        log("WARNING: No R2 result found. R3 will work with R1 only.")
        r2_result = "(Round 2 was skipped)"

    corrections = find_corrections(comments, "r3_en") if find_comment(comments, "r3_en") else []
    correction_text = ""
    if corrections:
        correction_text = "\n\n## CORRECTIONS FROM REVIEWER\n" + "\n".join(corrections)

    # --- R3 English ---
    prompt = PULSE_R3.format(
        area=area,
        objective_function=objective_function,
        context=context,
        r1_result=r1_result[:12000],
        r2_result=r2_result[:6000],
        today=today,
    ) + correction_text

    log("Calling API for R3 — English (with web search)...")
    result_en = call_api(client, prompt, model=SONNET, max_tokens=16000, use_web_search=True)
    log(f"R3 EN: {len(result_en)} chars")

    # Post EN version
    marker_en = MARKERS["r3_en"]
    comment_en = f"""{marker_en}
## 🫀 PULSE Round 3 — Final Living Pattern (English)

{result_en}

---
*Generated by WAVE Living Patterns Pipeline — PULSE R3 EN | {today}*
"""
    add_comment(issue_number, comment_en)
    log("R3 EN posted.")

    # --- Pause for rate limit ---
    log(f"Pausing {RATE_LIMIT_PAUSE}s before translation...")
    import time
    time.sleep(RATE_LIMIT_PAUSE)

    # --- Translation to Polish (chunked for long documents) ---
    CHUNK_THRESHOLD = 12000  # chars — above this, split into two API calls

    if len(result_en) <= CHUNK_THRESHOLD:
        # Short document — single pass
        log(f"Translation: single pass ({len(result_en)} chars)")
        translate_prompt = TRANSLATE_PROMPT.format(document=result_en)
        result_pl = call_api(client, translate_prompt, model=SONNET, max_tokens=16000, use_web_search=False)
    else:
        # Long document — split at a PART boundary near the middle
        log(f"Translation: chunked mode ({len(result_en)} chars, threshold={CHUNK_THRESHOLD})")
        midpoint = len(result_en) // 2
        # Find nearest "## PART" or "## CZĘŚĆ" boundary around midpoint
        split_pos = -1
        for marker_text in ["## PART ", "## CZĘŚĆ ", "## CHANGELOG", "## DZIENNIK"]:
            # Search backward from midpoint+3000 to find a good split
            search_zone = result_en[midpoint - 2000 : midpoint + 4000]
            idx = search_zone.rfind(marker_text)
            if idx >= 0:
                split_pos = midpoint - 2000 + idx
                break

        if split_pos < 0:
            # Fallback: split at double newline nearest to midpoint
            search_zone = result_en[midpoint - 1000 : midpoint + 1000]
            idx = search_zone.rfind("\n\n")
            split_pos = midpoint - 1000 + idx if idx >= 0 else midpoint

        chunk1 = result_en[:split_pos].strip()
        chunk2 = result_en[split_pos:].strip()
        log(f"  Chunk 1: {len(chunk1)} chars, Chunk 2: {len(chunk2)} chars")

        # Translate chunk 1
        prompt1 = TRANSLATE_PROMPT.format(document=chunk1) + "\n\nIMPORTANT: This is PART 1 of a larger document. Translate completely — the rest follows in a separate request."
        log("  Translating chunk 1...")
        pl_chunk1 = call_api(client, prompt1, model=SONNET, max_tokens=16000, use_web_search=False)
        log(f"  Chunk 1 PL: {len(pl_chunk1)} chars")

        # Pause between chunks
        log(f"  Pausing {RATE_LIMIT_PAUSE}s between chunks...")
        time.sleep(RATE_LIMIT_PAUSE)

        # Translate chunk 2
        prompt2 = TRANSLATE_PROMPT.format(document=chunk2) + "\n\nIMPORTANT: This is PART 2 of a larger document, continuing from a previous section. Translate completely. Maintain consistent terminology with the first part."
        log("  Translating chunk 2...")
        pl_chunk2 = call_api(client, prompt2, model=SONNET, max_tokens=16000, use_web_search=False)
        log(f"  Chunk 2 PL: {len(pl_chunk2)} chars")

        result_pl = pl_chunk1.rstrip() + "\n\n" + pl_chunk2.lstrip()

    log(f"R3 PL total: {len(result_pl)} chars (EN was {len(result_en)} chars, ratio: {len(result_pl)/max(len(result_en),1):.2f})")

    marker_pl = MARKERS["r3_pl"]
    comment_pl = f"""{marker_pl}
## 🫀 PULSE Runda 3 — Finalny Living Pattern (Polski)

{result_pl}

---
*Wygenerowano przez WAVE Living Patterns Pipeline — PULSE R3 PL | {today}*
*Następny krok: przejrzyj obie wersje. Dodaj label `publish` żeby opublikować jako PR.*
*Korekty: napisz komentarz "## Korekta" i dodaj label `redo-r3`.*
"""
    add_comment(issue_number, comment_pl)
    add_label(issue_number, "r3-ready")
    log("R3 PL posted. Label 'r3-ready' added.")


if __name__ == "__main__":
    main()
