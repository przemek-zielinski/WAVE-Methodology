"""
WAVE Living Patterns — Proposal Generator (S1 + S2)
Identifies a promising domain and problem for a new Living Pattern.
Outputs a JSON with Issue title and body for GitHub.

S1: Selects domain/industry based on three weighted criteria:
    - AI augmentation potential (40%)
    - Social acceptance of AI in domain (30%)
    - Existing AI solutions as proof points (30%)

S2: Identifies 2-3 daily problems in selected domain,
    picks the one with highest impact on work efficiency
    and human empowerment, proposes a realistic AI solution.

Output: JSON { status, title, body } printed to stdout.
"""

import os
import sys
import json
import glob
from datetime import datetime, timezone
from pathlib import Path

import anthropic


MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 4000
PATTERNS_DIR = "living-patterns/patterns/official"


def get_existing_domains() -> list[str]:
    """Read existing LP files to avoid proposing duplicate domains."""
    domains = []
    pattern = os.path.join(PATTERNS_DIR, "LP_*.md")
    for filepath in glob.glob(pattern):
        name = Path(filepath).stem  # e.g. LP_UX_UI_v3
        domain = name.replace("LP_", "").rsplit("_v", 1)[0]
        domains.append(domain)
    return domains


def get_past_proposals() -> list[str]:
    """Read proposal log to avoid repeating recent proposals."""
    log_path = Path("living-patterns/scripts/.proposal_history")
    if log_path.exists():
        return [line.strip() for line in log_path.read_text().splitlines() if line.strip()]
    return []


def save_proposal_to_history(domain: str):
    """Append domain to history file."""
    log_path = Path("living-patterns/scripts/.proposal_history")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(f"{domain}\n")


PROMPT_S1_S2 = """You are a strategic analyst for the WAVE methodology — an open methodology for human-AI collaboration.

Your task: identify a promising domain for a new Living Pattern (a living knowledge standard that helps practitioners in that domain work better with AI).

## STEP 1 (S1) — Select a domain

Evaluate domains using THREE criteria with these weights:

1. **AI augmentation potential (40%)** — How much can AI amplify human work in this domain? Look for: repetitive expert tasks, data-heavy decisions, documentation burden, knowledge transfer gaps. Higher = better.

2. **Social acceptance of AI (30%)** — How ready is this domain to adopt AI tools? Look for: existing positive sentiment, regulatory openness, professional bodies endorsing AI, practitioners already experimenting. Higher = better.

3. **Existing AI solutions as proof (30%)** — Are there already working AI tools in this domain? This validates feasibility and market readiness. Look for: commercial products, research prototypes, pilot programs. More = better.

CONSTRAINTS:
- Do NOT propose these domains (already covered or recently proposed): {excluded}
- Search the web for CURRENT data (2025-2026) on AI adoption across industries
- Pick a domain that is SPECIFIC enough to be actionable (not "business" but "supply chain logistics" or "clinical trials management")
- The domain must be one where a Living Pattern would help PRACTITIONERS (doctors, lawyers, engineers, teachers) — not AI researchers

Score each candidate domain 1-10 on each criterion, apply weights, pick the highest.

## STEP 2 (S2) — Identify the key problem and solution

For the selected domain:

1. Identify 2-3 COMMON DAILY problems that practitioners face. These must be:
   - Real, widespread, recognized by practitioners themselves
   - Related to work efficiency, cognitive burden, process friction, or resource gaps
   - NOT exotic edge cases — everyday pain points

2. Score each problem on two dimensions:
   - Work efficiency impact (how much time/effort is wasted)
   - Human empowerment potential (how much AI could strengthen the human's role, not replace it)
   Pick the highest-scoring problem.

3. Propose 2 realistic AI-augmented solutions for this problem. Then pick ONE based on:
   - Implementation feasibility (fits within medium-to-large corporate project budget)
   - Practicality (uses existing or near-term AI capabilities, not science fiction)
   - Alignment with WAVE philosophy (human leads, AI amplifies)
   
   CRITICAL: The solution must be credible and professional. Avoid anything that could be perceived as naive, abstract, or disconnected from reality. Think: "Would a senior practitioner in this domain take this seriously?"

## OUTPUT FORMAT

Respond with EXACTLY this JSON structure (no markdown, no backticks, no preamble):

{{
  "domain": "name of domain",
  "domain_score": {{
    "ai_potential": 8,
    "social_acceptance": 7,
    "existing_solutions": 6,
    "weighted_total": 7.1
  }},
  "runner_up_domains": [
    {{"name": "domain2", "weighted_total": 6.5}},
    {{"name": "domain3", "weighted_total": 6.2}}
  ],
  "problems_considered": [
    {{"problem": "description", "efficiency_score": 8, "empowerment_score": 7}},
    {{"problem": "description", "efficiency_score": 6, "empowerment_score": 8}},
    {{"problem": "description", "efficiency_score": 7, "empowerment_score": 5}}
  ],
  "selected_problem": "the chosen problem description",
  "solutions_considered": [
    {{"solution": "description", "feasibility": 8, "practicality": 7, "wave_alignment": 9}},
    {{"solution": "description", "feasibility": 6, "practicality": 8, "wave_alignment": 7}}
  ],
  "selected_solution": "the chosen solution description",
  "lp_title": "Living Pattern: [Domain] — [Focus Area]",
  "objective_function": "one sentence defining what this LP would optimize",
  "key_sources": ["source 1 with date", "source 2 with date", "source 3 with date"]
}}

Today's date: {today}
"""


def generate_proposal(client: anthropic.Anthropic, excluded: list[str]) -> dict:
    """Call API to generate S1+S2 proposal."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded_str = ", ".join(excluded) if excluded else "none yet"

    prompt = PROMPT_S1_S2.format(excluded=excluded_str, today=today)

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search"
        }],
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract text
    text = ""
    for block in response.content:
        if block.type == "text":
            text += block.text

    # Clean and parse JSON
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]

    return json.loads(text)


def format_issue(data: dict) -> dict:
    """Format proposal data into GitHub Issue title and body."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    title = f"📋 LP Proposal: {data['lp_title']}"

    body = f"""## Living Pattern Proposal — Auto-Generated {today}

### Selected Domain: **{data['domain']}**

**Weighted score:** {data['domain_score']['weighted_total']}/10
- AI augmentation potential: {data['domain_score']['ai_potential']}/10 (weight: 40%)
- Social acceptance of AI: {data['domain_score']['social_acceptance']}/10 (weight: 30%)
- Existing AI solutions: {data['domain_score']['existing_solutions']}/10 (weight: 30%)

**Runner-up domains:** {', '.join(f"{d['name']} ({d['weighted_total']})" for d in data.get('runner_up_domains', []))}

---

### Problems Considered

| Problem | Efficiency | Empowerment | Selected |
|---------|:----------:|:-----------:|:--------:|
"""
    for p in data.get('problems_considered', []):
        selected = "✅" if p['problem'] == data.get('selected_problem', '') else ""
        body += f"| {p['problem'][:80]}{'...' if len(p['problem']) > 80 else ''} | {p['efficiency_score']}/10 | {p['empowerment_score']}/10 | {selected} |\n"

    body += f"""
**Selected problem:** {data['selected_problem']}

---

### Solutions Considered

| Solution | Feasibility | Practicality | WAVE Alignment | Selected |
|----------|:-----------:|:------------:|:--------------:|:--------:|
"""
    for s in data.get('solutions_considered', []):
        selected = "✅" if s['solution'] == data.get('selected_solution', '') else ""
        body += f"| {s['solution'][:70]}{'...' if len(s['solution']) > 70 else ''} | {s['feasibility']}/10 | {s['practicality']}/10 | {s['wave_alignment']}/10 | {selected} |\n"

    body += f"""
**Selected solution:** {data['selected_solution']}

---

### Proposed Living Pattern

**Title:** {data['lp_title']}

**Objective function:** {data['objective_function']}

**Key sources found:** 
"""
    for src in data.get('key_sources', []):
        body += f"- {src}\n"

    body += f"""
---

### Ready PULSE Parameters

If you approve this proposal, use these parameters with [PULSE-Prompt](../living-patterns/PULSE-Prompt_v3.md):

```
[AREA]: {data['domain']}
[OBJECTIVE FUNCTION]: {data['objective_function']}
[SOLUTION CONTEXT]: {data['selected_solution']}
[INTERNAL MATERIALS]: none (new domain)
[CONSTRAINTS]: Solution must be feasible within medium-to-large corporate project budget
```

---

### What to do

- 👍 **Approve** — React with 👍, then run SCAN + PULSE manually when you have time
- 👎 **Reject** — Close this Issue with a comment why (helps improve future proposals)
- 💬 **Discuss** — Comment with modifications or questions

*Auto-generated by WAVE Living Patterns Proposal Generator (S1+S2). AI proposes, human decides.*
"""

    return {"status": "ok", "title": title, "body": body}


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(json.dumps({"status": "error", "message": "ANTHROPIC_API_KEY not set"}))
        sys.exit(1)

    # Build exclusion list
    existing = get_existing_domains()
    past = get_past_proposals()
    manual_exclude = [
        d.strip() for d in os.environ.get("EXCLUDE_DOMAINS", "").split(",") if d.strip()
    ]
    excluded = list(set(existing + past + manual_exclude))

    client = anthropic.Anthropic(api_key=api_key)

    try:
        data = generate_proposal(client, excluded)
        result = format_issue(data)
        # Save to history to avoid repeats
        save_proposal_to_history(data.get("domain", "unknown"))
        print(json.dumps(result, ensure_ascii=False))
    except json.JSONDecodeError as e:
        print(json.dumps({
            "status": "error",
            "message": f"Failed to parse API response as JSON: {e}"
        }))
        sys.exit(1)
    except anthropic.APIError as e:
        print(json.dumps({
            "status": "error",
            "message": f"Anthropic API error: {e}"
        }))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({
            "status": "error",
            "message": f"Unexpected error: {e}"
        }))
        sys.exit(1)


if __name__ == "__main__":
    main()
