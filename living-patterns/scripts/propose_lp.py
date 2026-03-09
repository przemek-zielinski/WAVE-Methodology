"""
WAVE Living Patterns — Proposal Generator v3 (S1 + S2)
Bilingual EN/PL, token-optimized (two API calls instead of one).

Call 1: S1+S2 analysis in English (clean logic, smaller prompt)
Call 2: Translation of key fields to Polish (cheap, fast, no JSON risk)

Output: JSON { status, title, body } printed to stdout → GitHub Issue.
"""

import os
import sys
import json
import glob
from datetime import datetime, timezone
from pathlib import Path

import anthropic


MODEL = "claude-sonnet-4-20250514"
PATTERNS_DIR = "living-patterns/patterns/official"


def get_existing_domains() -> list[str]:
    """Read existing LP files to avoid proposing duplicate domains."""
    domains = []
    pattern = os.path.join(PATTERNS_DIR, "LP_*_EN.md")
    # Also check old naming convention without _EN
    pattern_old = os.path.join(PATTERNS_DIR, "LP_*.md")
    for filepath in glob.glob(pattern) + glob.glob(pattern_old):
        name = Path(filepath).stem
        domain = name.replace("LP_", "").rsplit("_v", 1)[0].replace("_EN", "").replace("_PL", "")
        domains.append(domain)
    return list(set(domains))


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

Your task: identify a promising domain for a new Living Pattern.

## STEP 1 (S1) — Select a domain

Evaluate domains using THREE weighted criteria:

1. **AI augmentation potential (40%)** — How much can AI amplify human work? Look for: repetitive expert tasks, data-heavy decisions, documentation burden, knowledge transfer gaps.

2. **Social acceptance of AI (30%)** — How ready is this domain? Look for: positive sentiment, regulatory openness, practitioners experimenting.

3. **Existing AI solutions (30%)** — Working AI tools already? Validates feasibility.

CONSTRAINTS:
- Do NOT propose these domains (already covered or recently proposed): {excluded}
- Search the web for CURRENT data (2025-2026) on AI adoption
- Pick SPECIFIC domains (not "business" but "supply chain logistics")
- Domain must help PRACTITIONERS (doctors, lawyers, engineers, teachers)

## STEP 2 (S2) — Identify problem and solution

For selected domain:

1. Identify 2-3 COMMON DAILY problems practitioners face. Real, widespread, not exotic.

2. Score each on: work efficiency impact + human empowerment potential. Pick highest.

3. Propose 2 realistic AI solutions. Pick ONE based on: feasibility (medium-to-large corporate budget), practicality (existing AI capabilities), WAVE alignment (human leads, AI amplifies).

CRITICAL: Solution must be credible. Would a senior practitioner take this seriously?

## OUTPUT — JSON only, no markdown, no backticks:

{{
  "domain": "name",
  "domain_score": {{"ai_potential": 8, "social_acceptance": 7, "existing_solutions": 6, "weighted_total": 7.1}},
  "runner_up_domains": [{{"name": "x", "weighted_total": 6.5}}, {{"name": "y", "weighted_total": 6.2}}],
  "problems_considered": [
    {{"problem": "desc", "efficiency_score": 8, "empowerment_score": 7}},
    {{"problem": "desc", "efficiency_score": 6, "empowerment_score": 8}}
  ],
  "selected_problem": "chosen problem",
  "solutions_considered": [
    {{"solution": "desc", "feasibility": 8, "practicality": 7, "wave_alignment": 9}},
    {{"solution": "desc", "feasibility": 6, "practicality": 8, "wave_alignment": 7}}
  ],
  "selected_solution": "chosen solution",
  "lp_title": "Living Pattern: [Domain] — [Focus]",
  "objective_function": "one sentence",
  "key_sources": ["source 1", "source 2", "source 3"]
}}

Today: {today}
"""

PROMPT_TRANSLATE = """Translate these fields to Polish. Natural, professional Polish — not word-for-word translation. No markdown, no backticks, JSON only:

{{
  "lp_title_pl": "translate: {lp_title}",
  "objective_function_pl": "translate: {objective_function}",
  "selected_problem_pl": "translate: {selected_problem}",
  "selected_solution_pl": "translate: {selected_solution}"
}}
"""


def call_api(client: anthropic.Anthropic, prompt: str, max_tokens: int, use_search: bool = False) -> str:
    """Single API call with optional web search. Returns text response."""
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


def parse_json(text: str) -> dict:
    """Parse JSON from API response, handling common formatting issues."""
    clean = text.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(clean)


def generate_proposal(client: anthropic.Anthropic, excluded: list[str]) -> dict:
    """Two-call strategy: S1+S2 in English, then translate key fields."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded_str = ", ".join(excluded) if excluded else "none yet"

    # Call 1: S1+S2 analysis (with web search, higher token budget)
    prompt = PROMPT_S1_S2.format(excluded=excluded_str, today=today)
    text = call_api(client, prompt, max_tokens=3000, use_search=True)
    data = parse_json(text)

    # Call 2: Translate key fields (no web search, minimal tokens)
    translate_prompt = PROMPT_TRANSLATE.format(
        lp_title=data.get("lp_title", ""),
        objective_function=data.get("objective_function", ""),
        selected_problem=data.get("selected_problem", ""),
        selected_solution=data.get("selected_solution", "")
    )
    pl_text = call_api(client, translate_prompt, max_tokens=500, use_search=False)
    pl_data = parse_json(pl_text)

    # Merge
    data.update(pl_data)
    return data


def format_issue(data: dict) -> dict:
    """Format proposal into bilingual GitHub Issue."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    title_en = data.get("lp_title", "Unknown")
    title_pl = data.get("lp_title_pl", title_en)
    obj_en = data.get("objective_function", "")
    obj_pl = data.get("objective_function_pl", obj_en)
    problem_en = data.get("selected_problem", "")
    problem_pl = data.get("selected_problem_pl", problem_en)
    solution_en = data.get("selected_solution", "")
    solution_pl = data.get("selected_solution_pl", solution_en)

    title = f"📋 LP Proposal: {title_en}"

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
    for p in data.get("problems_considered", []):
        sel = "✅" if p["problem"] == problem_en else ""
        body += f"| {p['problem'][:80]}{'...' if len(p['problem']) > 80 else ''} | {p['efficiency_score']}/10 | {p['empowerment_score']}/10 | {sel} |\n"

    body += f"""
**Selected problem (EN):** {problem_en}
**Wybrany problem (PL):** {problem_pl}

---

### Solutions Considered

| Solution | Feasibility | Practicality | WAVE | Selected |
|----------|:-----------:|:------------:|:----:|:--------:|
"""
    for s in data.get("solutions_considered", []):
        sel = "✅" if s["solution"] == solution_en else ""
        body += f"| {s['solution'][:70]}{'...' if len(s['solution']) > 70 else ''} | {s['feasibility']}/10 | {s['practicality']}/10 | {s['wave_alignment']}/10 | {sel} |\n"

    body += f"""
**Selected solution (EN):** {solution_en}
**Wybrane rozwiązanie (PL):** {solution_pl}

---

### Proposed Living Pattern

| | English | Polski |
|---|---------|--------|
| **Title** | {title_en} | {title_pl} |
| **Objective** | {obj_en} | {obj_pl} |

**Key sources:** {', '.join(data.get('key_sources', []))}

---

### Ready PULSE Parameters — English

```
[AREA]: {data['domain']}
[OBJECTIVE FUNCTION]: {obj_en}
[SOLUTION CONTEXT]: {solution_en}
[INTERNAL MATERIALS]: none (new domain)
[CONSTRAINTS]: Feasible within medium-to-large corporate project budget
```

### Gotowe parametry PULSE — Polski

```
[OBSZAR]: {data['domain']}
[FUNKCJA CELU]: {obj_pl}
[KONTEKST ROZWIĄZANIA]: {solution_pl}
[MATERIAŁY WEWNĘTRZNE]: brak (nowa dziedzina)
[OGRANICZENIA]: Wykonalne w budżecie średnich lub dużych projektów korporacyjnych
```

---

### Output files / Pliki wyjściowe

When building this LP with PULSE, generate two files:
- `LP_{data['domain'].replace(' ', '_')}_v1_EN.md`
- `LP_{data['domain'].replace(' ', '_')}_v1_PL.md`

---

### What to do / Co zrobić

- 👍 **Approve** — Run SCAN + PULSE in both EN and PL when ready
- 👎 **Reject** — Close with comment why
- 💬 **Discuss** — Suggest modifications

*Auto-generated by WAVE Living Patterns (S1+S2). AI proposes, human decides.*
"""

    return {"status": "ok", "title": title, "body": body}


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(json.dumps({"status": "error", "message": "ANTHROPIC_API_KEY not set"}))
        sys.exit(1)

    existing = get_existing_domains()
    past = get_past_proposals()
    manual_exclude = [d.strip() for d in os.environ.get("EXCLUDE_DOMAINS", "").split(",") if d.strip()]
    excluded = list(set(existing + past + manual_exclude))

    client = anthropic.Anthropic(api_key=api_key)

    try:
        data = generate_proposal(client, excluded)
        result = format_issue(data)
        save_proposal_to_history(data.get("domain", "unknown"))
        print(json.dumps(result, ensure_ascii=False))
    except json.JSONDecodeError as e:
        print(json.dumps({"status": "error", "message": f"JSON parse error: {e}"}))
        sys.exit(1)
    except anthropic.APIError as e:
        print(json.dumps({"status": "error", "message": f"API error: {e}"}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"status": "error", "message": f"Error: {e}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
