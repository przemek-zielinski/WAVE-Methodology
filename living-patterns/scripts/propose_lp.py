"""
WAVE Living Patterns — Proposal Generator v4 (S0 + S1 + S2)
Three-stage: Web Research → Domain Selection → Problem/Solution.
Bilingual EN/PL, 5 decision factors, web-informed scoring.
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
RATE_LIMIT_PAUSE = 65


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


# ---------------------------------------------------------------------------
# Step 0 — Market Intelligence (with web search)
# ---------------------------------------------------------------------------

PROMPT_STEP0 = """You are a market intelligence analyst researching where AI is making the biggest real-world impact on practitioners' daily work in 2025-2026.

Conduct 5 web searches, one for each axis below. Find the FRESHEST, most CONCRETE data available.

## FIVE RESEARCH AXES

**1. PAIN — Practitioner suffering**
Where do practitioners suffer most? Burnout, attrition, administrative overload, repetitive drudgery. Search for 2025-2026 data on workforce crises, burnout rates, time wasted on non-core tasks. This is about PEOPLE, not technology.

**2. SOLUTIONS — Working AI implementations**
What AI tools have been DEPLOYED (not announced) with MEASURABLE results? Search for case studies, pilot results, production deployments with concrete numbers (time saved, errors reduced, costs cut). Not predictions — real outcomes.

**3. ECONOMIC VALUE — Financial impact of AI**
What is the ROI of AI implementations across domains? Search for: direct savings (cost reduction, revenue increase), indirect value (time optimization, process efficiency, risk mitigation, better resource allocation, error cost elimination). Hard numbers per domain.

**4. REGULATION — Doors opening and closing**
What new AI regulations entered force or were proposed in 2025-2026? Which domains gained regulatory clarity (green light) and which face new restrictions (red light)? Search for FDA, EU AI Act, sector-specific AI rules.

**5. FAILURES — Where AI fell short**
Where did AI deployments fail or disappoint? What lessons emerged? Search for post-mortems, critical analyses, abandoned projects, unintended consequences. This is the counterbalance — domains with hype but no substance.

## OUTPUT

Write a briefing of 400-600 words. For each domain you discover, include:
- What specific practitioner pain AI addresses
- What measurable results have been achieved (numbers, percentages, timeframes)
- What is the economic value (direct and indirect)
- What is the regulatory status
- What are the known risks and failures

Every claim must cite a specific source with date. No generalities.
Cover at minimum 4 different domains. Do NOT cover these domains (already done): {excluded}

Today: {today}
"""


# ---------------------------------------------------------------------------
# Step 1+2 — Domain Selection + Problem/Solution (JSON, no web search)
# ---------------------------------------------------------------------------

PROMPT_S1_S2 = """You are a strategic analyst for the WAVE methodology — an open methodology for human-AI collaboration.

Your task: using the market intelligence below, select the best domain for a new Living Pattern.

## CURRENT MARKET INTELLIGENCE (from web research today)
{market_intelligence}

## STEP 1 (S1) — Select a domain

Evaluate at least 3 candidate domains using FIVE weighted criteria:

1. **Practitioner pain intensity (25%)** — How severely do practitioners suffer without AI? Look for: burnout rates, workforce attrition, time wasted on non-core work, measurable suffering.

2. **AI augmentation potential (25%)** — How effectively can AI amplify human work? Look for: proven implementations with results, not just theoretical potential.

3. **Economic value measurability (20%)** — Can results be measured in hard numbers? Look for: clear before/after metrics, ROI data, cost savings, time savings. Domains with measurable outcomes build stronger Living Patterns.

4. **Social and regulatory readiness (15%)** — Is the domain ready for AI? Look for: practitioner acceptance, regulatory clarity (not restriction), existing experimentation.

5. **Market reach (15%)** — How many practitioners would benefit? Larger impact = more valuable Living Pattern for WAVE methodology.

Score each domain 1-10 on each factor. Weighted total determines selection.

CONSTRAINTS:
- Do NOT propose these domains (already covered or recently proposed): {excluded}
- Pick SPECIFIC domains (not "business" but "supply chain logistics")
- Domain must help PRACTITIONERS (doctors, lawyers, engineers, teachers, managers)
- Base your scores on the market intelligence above, not assumptions

## STEP 2 (S2) — Identify problem and solution

For the selected domain:

1. Identify 2-3 COMMON DAILY problems practitioners face. Real, widespread, not exotic. Use evidence from the market intelligence.

2. Score each on: work efficiency impact (1-10) + human empowerment potential (1-10). Pick highest combined.

3. Propose 2 realistic AI solutions. Pick ONE based on: feasibility (medium-to-large corporate budget), practicality (existing AI capabilities), WAVE alignment (human leads, AI amplifies).

CRITICAL: Solution must be credible. Would a senior practitioner take this seriously?

## OUTPUT — Respond with ONLY a JSON object. No markdown, no backticks, no explanation:

{{
  "domain": "name",
  "domain_scores": {{
    "pain_intensity": 8,
    "ai_potential": 9,
    "measurability": 7,
    "readiness": 8,
    "market_reach": 7,
    "weighted_total": 7.9
  }},
  "runner_up_domains": [
    {{"name": "x", "pain": 7, "ai_pot": 8, "measur": 6, "ready": 7, "reach": 8, "total": 7.2}},
    {{"name": "y", "pain": 8, "ai_pot": 6, "measur": 7, "ready": 6, "reach": 7, "total": 6.8}}
  ],
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


# ---------------------------------------------------------------------------
# Translation prompt
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

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


def call_api_with_search(client: anthropic.Anthropic, prompt: str, max_tokens: int) -> str:
    """API call with web search enabled. Extracts text from mixed response blocks."""
    log(f"  Calling API with web search (max_tokens={max_tokens})...")

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
            tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
        )

        texts = []
        for block in response.content:
            if hasattr(block, "text") and block.text:
                texts.append(block.text)

        result = "\n".join(texts).strip()
        log(f"  Web search response: {len(result)} chars, stop={response.stop_reason}")

        if not result:
            log("  WARNING: Empty text from web search. Falling back to no-search...")
            return call_api(client, prompt, max_tokens)

        return result

    except Exception as e:
        log(f"  Web search error: {e}. Falling back to no-search...")
        return call_api(client, prompt, max_tokens)


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


# ---------------------------------------------------------------------------
# Main generation flow
# ---------------------------------------------------------------------------

def generate_proposal(client: anthropic.Anthropic, excluded: list[str]) -> dict:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded_str = ", ".join(excluded) if excluded else "none yet"

    # Step 0: Market Intelligence (web search)
    log("STEP 0: Market Intelligence (web search)...")
    step0_prompt = PROMPT_STEP0.format(excluded=excluded_str, today=today)
    market_intelligence = call_api_with_search(client, step0_prompt, max_tokens=2000)
    log(f"  Market briefing: {len(market_intelligence)} chars")

    # Rate limit pause
    log(f"  Waiting {RATE_LIMIT_PAUSE}s for rate limit...")
    time.sleep(RATE_LIMIT_PAUSE)

    # Step 1+2: Domain selection + Problem/Solution (JSON, no web search)
    log("STEP 1+2: S1+S2 analysis (with market intelligence)...")
    s1s2_prompt = PROMPT_S1_S2.format(
        market_intelligence=market_intelligence[:4000],
        excluded=excluded_str,
        today=today,
    )
    text = call_api(client, s1s2_prompt, max_tokens=3000)
    data = parse_json(text)
    data["market_intelligence_excerpt"] = market_intelligence[:500]
    log(f"  Domain: {data.get('domain', '?')}")

    # Rate limit pause
    log(f"  Waiting {RATE_LIMIT_PAUSE}s for rate limit...")
    time.sleep(RATE_LIMIT_PAUSE)

    # Step 3: Translate
    log("STEP 3: Translation...")
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

    # Extract scores (handle both old and new format)
    scores = data.get("domain_scores", data.get("domain_score", {}))

    # Build runner-up domains table
    runner_up_rows = ""
    for d in data.get("runner_up_domains", []):
        runner_up_rows += f"| {d.get('name', '?')} | {d.get('pain', '?')} | {d.get('ai_pot', '?')} | {d.get('measur', '?')} | {d.get('ready', '?')} | {d.get('reach', '?')} | {d.get('total', '?')} |\n"

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

**Wynik ważony / Weighted score:** {scores.get('weighted_total', '?')}/10

| Faktor / Factor | Waga / Weight | Wynik / Score |
|-----------------|:------------:|:------------:|
| Intensywność bólu praktyków / Practitioner pain intensity | 25% | {scores.get('pain_intensity', '?')}/10 |
| Potencjał wzmocnienia AI / AI augmentation potential | 25% | {scores.get('ai_potential', '?')}/10 |
| Mierzalność efektu / Economic value measurability | 20% | {scores.get('measurability', '?')}/10 |
| Gotowość społeczna i regulacyjna / Social & regulatory readiness | 15% | {scores.get('readiness', '?')}/10 |
| Zasięg rynku / Market reach | 15% | {scores.get('market_reach', '?')}/10 |

**Domeny drugie w kolejności / Runner-up domains:**

| Domena / Domain | Ból / Pain | AI Pot. | Mierz. / Meas. | Gotow. / Ready | Zasięg / Reach | Suma / Total |
|-----------------|:----------:|:-------:|:--------------:|:--------------:|:--------------:|:------------:|
{runner_up_rows}

---

### Wywiad rynkowy / Market Intelligence (excerpt)

{data.get('market_intelligence_excerpt', 'N/A')}

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

*Wygenerowano automatycznie przez WAVE Living Patterns (S0+S1+S2). AI proponuje, człowiek decyduje.*
*Auto-generated by WAVE Living Patterns (S0+S1+S2). AI proposes, human decides.*
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
