"""
WAVE Living Patterns — Proposal Generator v3 (S1 + S2)
Bilingual EN/PL, token-optimized (two API calls).
Fixed: removed web search (caused empty responses on low-tier API plans).
Model knowledge is sufficient for domain selection.
"""

import os
import sys
import json
import glob
import time
from datetime import datetime, timezone
from pathlib import Path

import anthropic


MODEL = "claude-sonnet-4-20250514"
PATTERNS_DIR = "living-patterns/patterns/official"


def log(msg):
    print(msg, file=sys.stderr)


def get_existing_domains() -> list[str]:
    domains = []
    for pattern in [os.path.join(PATTERNS_DIR, "LP_*_EN.md"),
                    os.path.join(PATTERNS_DIR, "LP_*.md")]:
        for filepath in glob.glob(pattern):
            name = Path(filepath).stem
            domain = name.replace("LP_", "").rsplit("_v", 1)[0].replace("_EN", "").replace("_PL", "")
            domains.append(domain)
    return list(set(domains))


def get_past_proposals() -> list[str]:
    log_path = Path("living-patterns/scripts/.proposal_history")
    if log_path.exists():
        return [line.strip() for line in log_path.read_text().splitlines() if line.strip()]
    return []


def save_proposal_to_history(domain: str):
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
- Pick SPECIFIC domains (not "business" but "supply chain logistics")
- Domain must help PRACTITIONERS (doctors, lawyers, engineers, teachers)
- Use your knowledge of current AI adoption trends (2024-2026)

## STEP 2 (S2) — Identify problem and solution

For selected domain:

1. Identify 2-3 COMMON DAILY problems practitioners face. Real, widespread, not exotic.

2. Score each on: work efficiency impact + human empowerment potential. Pick highest.

3. Propose 2 realistic AI solutions. Pick ONE based on: feasibility (medium-to-large corporate budget), practicality (existing AI capabilities), WAVE alignment (human leads, AI amplifies).

CRITICAL: Solution must be credible. Would a senior practitioner take this seriously?

## OUTPUT — Respond with ONLY a JSON object. No markdown, no backticks, no explanation before or after:

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

PROMPT_TRANSLATE = """Translate all fields below to natural, professional Polish.
Respond with ONLY a JSON object. No markdown, no backticks, no explanation:

{{
  "lp_title_pl": "translate: {lp_title}",
  "objective_function_pl": "translate: {objective_function}",
  "selected_problem_pl": "translate: {selected_problem}",
  "selected_solution_pl": "translate: {selected_solution}",
  "problems_pl": {problems_json},
  "solutions_pl": {solutions_json}
}}

For problems_pl: translate each problem description string in the array.
For solutions_pl: translate each solution description string in the array.
Keep the arrays in the same order as input.
"""


def call_api(client: anthropic.Anthropic, prompt: str, max_tokens: int) -> str:
    """Single API call, no tools. Returns text response."""
    log(f"  Calling API (max_tokens={max_tokens})...")

    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )

    log(f"  Response: stop_reason={response.stop_reason}, blocks={len(response.content)}")

    texts = []
    for block in response.content:
        if block.type == "text":
            texts.append(block.text)

    result = "\n".join(texts).strip()
    log(f"  Extracted {len(result)} chars of text")

    if not result:
        log(f"  WARNING: Empty response. Block types: {[b.type for b in response.content]}")

    return result


def parse_json(text: str) -> dict:
    """Parse JSON from API response."""
    if not text:
        raise json.JSONDecodeError("Empty response from API", "", 0)
    clean = text.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    if not clean.startswith("{"):
        start = clean.find("{")
        if start >= 0:
            depth = 0
            for i, c in enumerate(clean[start:], start):
                if c == "{": depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        clean = clean[start:i+1]
                        break
    return json.loads(clean)


def generate_proposal(client: anthropic.Anthropic, excluded: list[str]) -> dict:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded_str = ", ".join(excluded) if excluded else "none yet"

    # Call 1: S1+S2 analysis
    log("CALL 1: S1+S2 analysis...")
    prompt = PROMPT_S1_S2.format(excluded=excluded_str, today=today)
    text = call_api(client, prompt, max_tokens=3000)
    data = parse_json(text)
    log(f"  Domain: {data.get('domain', '?')}")

    # Rate limit pause
    log("  Waiting 65s for rate limit...")
    time.sleep(65)

    # Call 2: Translate
    log("CALL 2: Translation...")
    problems_list = [p.get("problem", "") for p in data.get("problems_considered", [])]
    solutions_list = [s.get("solution", "") for s in data.get("solutions_considered", [])]
    translate_prompt = PROMPT_TRANSLATE.format(
        lp_title=data.get("lp_title", ""),
        objective_function=data.get("objective_function", ""),
        selected_problem=data.get("selected_problem", ""),
        selected_solution=data.get("selected_solution", ""),
        problems_json=json.dumps(problems_list, ensure_ascii=False),
        solutions_json=json.dumps(solutions_list, ensure_ascii=False),
    )
    pl_text = call_api(client, translate_prompt, max_tokens=1500)
    pl_data = parse_json(pl_text)

    data.update(pl_data)
    return data


def format_issue(data: dict) -> dict:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    title_en = data.get("lp_title", "Unknown")
    title_pl = data.get("lp_title_pl", title_en)
    obj_en = data.get("objective_function", "")
    obj_pl = data.get("objective_function_pl", obj_en)
    problem_en = data.get("selected_problem", "")
    problem_pl = data.get("selected_problem_pl", problem_en)
    solution_en = data.get("selected_solution", "")
    solution_pl = data.get("selected_solution_pl", solution_en)
    problems_pl = data.get("problems_pl", [])
    solutions_pl = data.get("solutions_pl", [])

    title = f"📋 LP Proposal: {title_en}"

    # Build problems table with PL translations
    problems_rows = ""
    for i, p in enumerate(data.get("problems_considered", [])):
        sel = "✅" if p["problem"] == problem_en else ""
        p_en = p['problem'][:80] + ('...' if len(p['problem']) > 80 else '')
        p_pl = problems_pl[i][:80] + ('...' if len(problems_pl[i]) > 80 else '') if i < len(problems_pl) else p_en
        problems_rows += f"| {p_en} | {p_pl} | {p['efficiency_score']}/10 | {p['empowerment_score']}/10 | {sel} |\n"

    # Build solutions table with PL translations
    solutions_rows = ""
    for i, s in enumerate(data.get("solutions_considered", [])):
        sel = "✅" if s["solution"] == solution_en else ""
        s_en = s['solution'][:70] + ('...' if len(s['solution']) > 70 else '')
        s_pl = solutions_pl[i][:70] + ('...' if len(solutions_pl[i]) > 70 else '') if i < len(solutions_pl) else s_en
        solutions_rows += f"| {s_en} | {s_pl} | {s['feasibility']}/10 | {s['practicality']}/10 | {s['wave_alignment']}/10 | {sel} |\n"

    body = f"""## Propozycja Living Pattern — Wygenerowana automatycznie {today}
## Living Pattern Proposal — Auto-Generated {today}

---

### Wybrana domena / Selected Domain: **{data['domain']}**

**Wynik ważony / Weighted score:** {data['domain_score']['weighted_total']}/10
- Potencjał AI / AI augmentation potential: {data['domain_score']['ai_potential']}/10 (waga/weight: 40%)
- Akceptacja społeczna AI / Social acceptance of AI: {data['domain_score']['social_acceptance']}/10 (waga/weight: 30%)
- Istniejące rozwiązania AI / Existing AI solutions: {data['domain_score']['existing_solutions']}/10 (waga/weight: 30%)

**Domeny drugie w kolejności / Runner-up domains:** {', '.join(f"{d['name']} ({d['weighted_total']})" for d in data.get('runner_up_domains', []))}

---

### Rozpatrywane problemy / Problems Considered

| Problem (EN) | Problem (PL) | Wydajność / Efficiency | Wzmocnienie / Empowerment | Wybrano / Selected |
|--------------|-------------|:----------------------:|:-------------------------:|:------------------:|
{problems_rows}
**Wybrany problem / Selected problem (EN):** {problem_en}
**Wybrany problem / Selected problem (PL):** {problem_pl}

---

### Rozpatrywane rozwiązania / Solutions Considered

| Rozwiązanie / Solution (EN) | Rozwiązanie / Solution (PL) | Wykonalność / Feasibility | Praktyczność / Practicality | WAVE | Wybrano / Selected |
|-----------------------------|----------------------------|:-------------------------:|:---------------------------:|:----:|:------------------:|
{solutions_rows}
**Wybrane rozwiązanie / Selected solution (EN):** {solution_en}
**Wybrane rozwiązanie / Selected solution (PL):** {solution_pl}

---

### Proponowany Living Pattern / Proposed Living Pattern

| | English | Polski |
|---|---------|--------|
| **Tytuł / Title** | {title_en} | {title_pl} |
| **Cel / Objective** | {obj_en} | {obj_pl} |

**Kluczowe źródła / Key sources:** {', '.join(data.get('key_sources', []))}

---

### Parametry PULSE / PULSE Parameters

**English:**
```
[AREA]: {data['domain']}
[OBJECTIVE FUNCTION]: {obj_en}
[SOLUTION CONTEXT]: {solution_en}
[INTERNAL MATERIALS]: none (new domain)
[CONSTRAINTS]: Feasible within medium-to-large corporate project budget
```

**Polski:**
```
[OBSZAR]: {data['domain']}
[FUNKCJA CELU]: {obj_pl}
[KONTEKST ROZWIĄZANIA]: {solution_pl}
[MATERIAŁY WEWNĘTRZNE]: brak (nowa dziedzina)
[OGRANICZENIA]: Wykonalne w budżecie średnich lub dużych projektów korporacyjnych
```

---

### Pliki wyjściowe / Output files

- `LP_{data['domain'].replace(' ', '_')}_v1_EN.md`
- `LP_{data['domain'].replace(' ', '_')}_v1_PL.md`

---

### Co zrobić / What to do

- 👍 **Zatwierdź / Approve** — Uruchom SCAN + PULSE / Run SCAN + PULSE
- 👎 **Odrzuć / Reject** — Zamknij z komentarzem / Close with comment
- 💬 **Dyskusja / Discuss** — Zaproponuj zmiany / Suggest modifications

*Wygenerowano automatycznie przez WAVE Living Patterns (S1+S2). AI proponuje, człowiek decyduje.*
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

    log(f"Excluded domains: {excluded}")

    client = anthropic.Anthropic(api_key=api_key)

    try:
        data = generate_proposal(client, excluded)
        result = format_issue(data)
        save_proposal_to_history(data.get("domain", "unknown"))
        print(json.dumps(result, ensure_ascii=False))
    except json.JSONDecodeError as e:
        log(f"FATAL: JSON parse error: {e}")
        print(json.dumps({"status": "error", "message": f"JSON parse error: {e}"}))
        sys.exit(1)
    except anthropic.APIError as e:
        log(f"FATAL: API error: {e}")
        print(json.dumps({"status": "error", "message": f"API error: {e}"}))
        sys.exit(1)
    except Exception as e:
        log(f"FATAL: {type(e).__name__}: {e}")
        print(json.dumps({"status": "error", "message": f"Error: {e}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
