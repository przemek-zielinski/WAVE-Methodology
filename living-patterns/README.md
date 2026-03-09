# 🔧 WAVE Living Patterns

## A tool for systematically building living knowledge standards with AI

---

### Start here — three steps

**Step 1: SCAN** — describe your solution, get a complete list of areas to investigate.
→ [SCAN-Prompt_v3.md](SCAN-Prompt_v3.md) | [How-To](SCAN-HowTo_v3.md)

**Step 2: PULSE** — for each area, run three research rounds. AI builds, verifies from a different angle, searches peripheral directions.
→ [PULSE-Prompt_v3.md](PULSE-Prompt_v3.md) | [How-To](PULSE-HowTo_v3.md)

**Step 3: Living Pattern** — the result is a living document with principles, standards, error matrix, and metrics. It periodically checks its own freshness.
→ [First official pattern: UX/UI](patterns/official/LP_UX_UI_v3.md)

**What you need:** AI with web search enabled (Claude, ChatGPT, Gemini). A description of your solution. Optionally: internal project documentation.

---

### What is a Living Pattern

A Living Pattern is a living document containing the best available knowledge — scientific, industry, and practical — for one implementation area. It is not a textbook that sits on a shelf. It is a decision-making tool that regularly verifies its own freshness.

A designer opens the UX/UI Living Pattern before drawing screens. A developer opens the Database Living Pattern before designing schemas. A lawyer opens the Compliance Living Pattern before writing policies.

### How it works

```
SCAN                          PULSE (×3 rounds)             Living Pattern
identifies areas        →     builds knowledge         →    living document
+ objective functions         from three angles              + auto-refinement
+ PULSE parameters            (build → optimize              on a set rhythm
                               → finalize)
```

Three PULSE rounds cover ~97% of available knowledge. Diminishing returns: Round 1 delivers ~60% of value, Round 2 ~25%, Round 3 ~12%. A natural saturation point — not infinity.

### Who is it for

**AI beginners** — a ready-made workflow instead of chaotic questions. Predictable structure and quality of results.

**Advanced practitioners without a model** — repeatable process, shared language across the team, knowledge that doesn't age in a drawer.

**Teams** — shared area map (SCAN), same document format (Living Pattern), visible progress, new members read the pattern instead of asking "why did we choose X."

### Full documentation

→ [Ecosystem — complete description of the ecosystem, philosophy, lifecycle, auto-refinement, open source model](Ecosystem_v3.md)

### Available patterns

| Pattern                                            | Area                                    | Status         |
| -------------------------------------------------- | --------------------------------------- | -------------- |
| [LP_UX_UI_v3.md](patterns/official/LP_UX_UI_v3.md) | UX/UI & User Journey                    | Official       |
| *LP_Database*                                      | Database & data model                   | In preparation |
| *LP_Security*                                      | Security                                | In preparation |
| *Your pattern?*                                    | → [CONTRIBUTING.md](../CONTRIBUTING.md) | Community      |

---

### Relationship with WAVE

Living Patterns is a **tool** from the [WAVE](../README.md) methodology (Workflow Amplification via Vectored Expertise). You can use Living Patterns standalone — but if you want the full human-AI collaboration methodology, start with the [WAVE core](../docs/).

---

*License: CC BY-SA 4.0 | Concept: Przemek Zieliński | Documentation: Claude (Anthropic)*
