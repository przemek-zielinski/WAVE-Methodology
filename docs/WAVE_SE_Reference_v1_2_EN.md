# WAVE — Human-AI Collaboration Methodology
## Reference Document: Software Engineering v1.2 | March 2026

**Concept author:** Przemek Zieliński  
**Written by:** Claude Opus 4.6  
**License:** CC BY-SA 4.0  
**Repository:** github.com/przemek-zielinski/WAVE-Methodology  
**First domain application:** Software Engineering

---

## Table of Contents

— Quick Start — begin here

0. In one sentence, in one paragraph, in one minute
1. The Problem — the AI productivity paradox
2. Philosophy — five axioms and three levels of collaboration
3. Seven problems and seven WAVE answers
4. DooR — the doors between stages
5. Components — an open map of tools
6. The completeness test — the AANP quadruple
7. WAVE and existing methodologies — a different question, a different level
8. Case study — IDareU Gen2
9. Glossary

---

## Quick Start — begin here

Don't want to read ten chapters before you start? Here's the minimum.

**What it is:** A methodology for human-AI collaboration. It tells you how to prepare context, run sessions, and build knowledge so AI works from the best possible assumptions — not from guesswork.

**How to start in three steps:**

```
  STEP 1 — Choose your product profile
  ──────────────────────────────────────
  □ POC / prototype?     → DISCOVERY profile (1-5 days)
  □ MVP / pilot?         → BUILD profile (4-8 weeks)
  □ Target product?      → SCALE profile (months)
  
  Not sure? Start with DISCOVERY. You can always move up.

  STEP 2 — Run SCAN
  ──────────────────
  Open a chat with AI. Paste the prompt from SCAN-Prompt.md
  with a description of your solution. You'll get a list of areas
  to investigate with ready-made parameters for the next step.

  STEP 3 — Run PULSE for the first area
  ───────────────────────────────────────
  Take the highest-priority area from the SCAN list.
  Paste the prompt from PULSE-Prompt.md with parameters.
  Run Round 1. Review the result.
  You now have your first Living Pattern — a living knowledge document.
  Repeat for the remaining areas.
```

**What you need:** Access to AI with web search (Claude, ChatGPT, Gemini with web search enabled). A description of your solution. Optionally: existing project documentation.

**Files to download:**

| File | What it does | When to use |
|---|---|---|
| `SCAN-Prompt.md` | Identifies areas to investigate | At the start — once |
| `SCAN-HowTo.md` | Instructions for using SCAN | Before your first SCAN |
| `PULSE-Prompt.md` | Builds a Living Pattern in 3 rounds | Per area from the SCAN list |
| `PULSE-HowTo.md` | Instructions for using PULSE | Before your first PULSE |
| `WAVE_Product_Profiles.md` | How to match WAVE scale to your project | When unsure how much WAVE you need |

The rest of this document explains WHY this works, HOW it's built, and WHAT you can achieve at larger scale.

### WAVE Architecture — at a glance

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   WAVE — Workflow Amplification via Vectored Expertise               ║
║   Human-AI Collaboration Methodology                                 ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  LAYER 1: PHILOSOPHY (closed — 5 axioms + meta-axiom)        │  ║
║   │                                                              │  ║
║   │  70/30 • Human leads • Build completely • Path = value      │  ║
║   │  • Failures teach                                            │  ║
║   │  Meta-axiom: Currents & Tensions (navigate, don't optimize) │  ║
║   │                                                              │  ║
║   │  Three H-AI levels: DataPrep → Prompt2Data → Prompt2Prompt  │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  LAYER 2: COMPONENTS (open — the set grows)                 │  ║
║   │                                                              │  ║
║   │  DooR — Definition of Operational Readiness                 │  ║
║   │  ┌──────────────────────┐  ┌──────────────────────────────┐ │  ║
║   │  │  Living Patterns     │  │  FALA                        │ │  ║
║   │  │  (KNOWLEDGE ready)   │  │  (from concept to CODE)      │ │  ║
║   │  │                      │  │                              │ │  ║
║   │  │  SCAN → PULSE →      │  │  Audit → Blueprint → Code   │ │  ║
║   │  │  Living Pattern      │  │  RtS (11 layers) → DoD      │ │  ║
║   │  └──────────────────────┘  └──────────────────────────────┘ │  ║
║   │                                                              │  ║
║   │  Decision Log • [future components → open set]              │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  LAYER 3: PRACTICES (open — habits accumulate)              │  ║
║   │                                                              │  ║
║   │  Checkpoints • Shorter chats • Versioning • Imperative      │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  COMPLETENESS TEST: AANP (closed)                           │  ║
║   │                                                              │  ║
║   │  Every process = Actor + Action + Tool + Product             │  ║
║   │  Missing one = broken process                                │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

### Product Profiles — WAVE for every scale

WAVE is one methodology with three intensity profiles — matched to the type of solution you're building. Building a POC in one day? DISCOVERY profile. An MVP in a few weeks? BUILD profile. A target product? SCALE profile. Same philosophy, different component scale.

| Profile | Goal | Time | P/E Ratio | SCAN | PULSE | RtS |
|---|---|---|:---:|---|---|---|
| **DISCOVERY** (POC) | Validate idea | 1-5 days | ~60/40 | 3-5 questions | 1 round | 4 layers |
| **BUILD** (MVP) | Deliver value | 2-8 weeks | ~70/30 | 6-8 areas | 2 rounds | 8 layers |
| **SCALE** (Product) | Scale & maintain | Months | 50-70/30-50 | 10-15 areas | 3 rounds | 11 layers |

Full description: **WAVE Product Profiles v1.0** (companion document).

---

## 0. In one sentence, in one paragraph, in one minute

### One sentence

WAVE is a human-AI collaboration methodology — it tells you how to prepare context, run sessions, and build knowledge so AI works from the best possible assumptions, not from guesswork.

### One paragraph

Everyone who works with AI knows the moment — AI produces something mediocre, you iterate, iterate, iterate, and an hour later you have something passable. The next day you start from scratch because AI doesn't remember what you agreed on. WAVE inverts this ratio: seventy percent of your time goes into preparing context and knowledge, thirty percent into execution — and that execution is accurate on the first shot. WAVE provides concrete tools: SCAN maps what you need to know, PULSE builds that knowledge in three rounds, Living Patterns keep it current, RtS defines when context is complete. The result: AI stops guessing and starts acting like a partner who truly understands your project.

### One minute

We have a problem that nobody has named. Millions of people work with AI daily — writing code, designing products, creating documents. And most of them do it the same way: throw in a prompt, see what comes out, fix, fix, fix. It's like building a house without blueprints — you put up a wall, tear it down, try again. It works, but you waste eighty percent of the potential.

WAVE says: invert the ratio. Before you start building — prepare context. Gather knowledge. Define what you're optimizing. Give AI the full picture, not scraps. Seventy percent preparation, thirty percent execution. And that execution is accurate, because AI isn't guessing — it knows.

WAVE isn't another project management framework. It doesn't compete with Scrum or Lean. WAVE operates at a level no existing methodology addresses — at the level of the working session where a human and AI create something concrete together. It's open-source, it's free, and anyone can start using it today — from one tool, from one session.

---

## 1. The Problem — the AI productivity paradox

### Perception vs reality

Over 80% of developers today use AI coding tools. Nearly all claim they work faster. Meanwhile, the data tells a different story.

```
  DEVELOPER PERCEPTION              RESEARCH DATA
  ═══════════════════════           ═══════════════════════

  "AI speeds up                     Experienced developers
   my work by 20%"                  are 19% SLOWER with AI
                                     (METR, 2025)
          ▲                                ▲
          │        39-point                │
          │◄────── perception ────────────►│
          │        gap                     │
          │                                │

  +20% (feeling)                  -19% (measurement)
```

This thirty-nine-point perception gap isn't a curiosity — it's a warning signal. As MIT professor Armando Solar-Lezama put it: AI is a new credit card that lets you take on technical debt at a pace we've never seen before.

### The scale of the problem — hard numbers

| Source | Year | Finding | Scale |
|---|:---:|---|---|
| **METR** | 2025 | Experienced developers 19% slower with AI | Controlled study |
| **Faros AI** | 2025 | Code review time increased 91% | 10,000 developers, 1,255 teams |
| **GitClear** | 2024 | Code duplication rose 4× | 211M changed lines of code |
| **CodeRabbit** | 2025 | AI code: 1.7× more critical bugs | 470 pull requests |
| **Apiiro** | 2025 | Security vulnerabilities: 1,000 to 10,000/month | Fortune 50 companies |
| **NBER** | 2026 | No measurable AI impact on firm productivity | 6,000 executives |
| **MIT Media Lab** | 2026 | 95% of organizations see no measurable AI ROI | Cross-sectional study |
| **Stack Overflow** | 2025 | Trust in AI-generated code dropped from 43% to 29% | Global community |
| **Fed San Francisco** | 2026 | Macro-statistics show no AI productivity effect | Speech, Feb 17, 2026 |

### Visualization — what happened to the AI promise

```
  The Promise                            The Reality
  ───────────                            ───────────

  Developer                              Developer
  + AI                                   + AI
  = 10× faster                           = more code
                                           + more bugs
  ┌────────────┐                           + longer reviews
  │ ██████████ │ 10×                       + more debt
  │ ██████████ │                           + less understanding
  │ ██████████ │                         
  │ ██████████ │                         ┌────────────┐
  │ ██████████ │                         │ ████       │ 1.2×
  └────────────┘                         │            │ (net)
                                         └────────────┘
       MIT                                   Faros AI
  "the future"                           "the present"
```

### Where the problem lies — a map

The problem isn't in AI. The problem isn't in the human. The problem lies in the **space between them** — in how human knowledge and intent reaches AI's context window.

```
  ┌─────────────┐          ╔═══════════════════╗          ┌─────────────┐
  │             │          ║                   ║          │             │
  │   HUMAN    │          ║    THE SPACE      ║          │     AI      │
  │             │          ║    BETWEEN        ║          │             │
  │  • knowledge│ ──??──▶  ║                   ║  ──??──▶ │  • power    │
  │  • context │          ║   unoccupied      ║          │  • scale    │
  │  • intent  │          ║                   ║          │  • speed    │
  │  • goal    │          ║   ◀── WAVE ──▶    ║          │  • synthesis│
  │             │          ║                   ║          │             │
  └─────────────┘          ╚═══════════════════╝          └─────────────┘
```

WAVE occupies that space. Not by changing AI — AI is powerful enough. By changing what AI receives as input.

---

## 2. Philosophy — five axioms and three levels of collaboration

### Five axioms

WAVE's philosophy is a closed set — five axioms and one meta-axiom that are non-negotiable. Everything else in WAVE can change, grow, evolve. The philosophy cannot. It is like the laws of thermodynamics: you can build any machine, but these laws always apply.

| # | Axiom | Essence | Analogy |
|:---:|---|---|---|
| 1 | **70 / 30** | Preparation dominates — like gravity, not command | Cheetah: 16h observation → 12s chase |
| 2 | **Human leads, AI amplifies** | AI amplifies expertise, doesn't replace it | Telescope doesn't replace the astronomer's eye |
| 3 | **Build completely, activate progressively** | Full architecture from day 1, gradual activation | Fruit tree: you plant it whole, fruit in 2 years |
| 4 | **The path and process = value** | Discoveries emerge between tasks | Serendipity: Columbus → America, Fleming → penicillin |
| 5 | **Failures teach more than successes** | Others' mistakes with numbers > others' successes without context | Success dulls the senses, failure sharpens them |

**Axiom 1 — Seventy thirty.** Preparation dominates execution. Not as a command — as gravity. A body always falls toward earth, but the trajectory depends on what you're building.

In nature, this ratio appears everywhere. The cheetah — the fastest land animal — runs at full speed for twelve seconds at most. The rest of its day is observation, positioning, waiting for the right moment. Working with AI is the same: an hour of context preparation and fifteen minutes of execution that hits the mark on the first try. Or: zero preparation and three hours of fixing.

70/30 is a center of gravity, not an iron rule. In a light prototype (Discovery profile), the ratio naturally gravitates toward 60/40 — the product is too simple for preparation to need dominance. In a large product with twenty modules, it gravitates toward 50/50 — execution grows linearly with each module, while preparation is reusable. In an MVP (Build profile), it lands exactly at 70/30 — and here the axiom breathes most fully.

But in ALL cases, preparation is at least half the work — which is a radical inversion of vibe coding, where preparation equals zero.

**Axiom 2 — The human leads, AI amplifies.** AI is an amplifier of expertise — not a replacement. The human defines the objective function, the human evaluates the result, the human makes the decision. AI processes, synthesizes, generates — at a scale inaccessible to humans. But direction always belongs to the human. AI without human direction produces output that's correct but generic — like an orchestra without a conductor.

**Axiom 3 — Build completely, activate progressively.** Design the full architecture from day one, but activate features through toggles as you gather data and confirm assumptions. Don't build "a temporary version you'll throw away later." Build the target version that you then discover over time.

**Axiom 4 — The path and process have value.** The most valuable discoveries emerge between tasks. WAVE isn't a straight line from A to B. It's a river flowing toward the sea but creating meanders, floodplains, and deltas along the way — and in those bends lives value that a linear plan would never find.

**Axiom 5 — Failures teach more than successes.** That's why every WAVE research tool (PULSE) deliberately searches for failures in Round 2 — not because it's pessimistic, but because others' mistakes with numbers are more valuable than others' successes without context.

**Meta-axiom: Currents and Tensions.** The five axioms say WHAT matters. Currents and Tensions says HOW those values compete with each other in every concrete decision. Every human-AI collaboration session plays out on a field of tensions — quality↔simplicity, stability↔feature richness, cost↔depth — and emergence is born at their intersection. The operator's role is to navigate that competition, not to eliminate it. Capacity reserve is a first-class value, not waste. Full description: WAVE v2.0 main document, chapter 2.

### Three levels of H-AI collaboration

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║                                                                   ║
  ║  Level 1: DataPrep                                    INHALE     ║
  ║  ─────────────────                                               ║
  ║  Human organizes domain knowledge                                ║
  ║  Collects context, defines goals, structures information         ║
  ║  ● Who: HUMAN (primarily)                                       ║
  ║  ● In SE: architecture, specs, data model, Decision Log          ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Level 2: Prompt2Data                                 PULSE      ║
  ║  ────────────────────                                            ║
  ║  Precise task with full context                                  ║
  ║  AI doesn't guess intent — intent is explicit                    ║
  ║  ● Who: HUMAN → AI                                              ║
  ║  ● In SE: "Here are specs, data model, and constraints → code"  ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Level 3: Prompt2Prompt                               EXHALE    ║
  ║  ──────────────────────                                          ║
  ║  Meta-steering: evaluate result, correct, iterate                ║
  ║  Human shapes direction, doesn't write content                   ║
  ║  ● Who: HUMAN (evaluates) ← AI (proposes)                      ║
  ║  ● In SE: "This component needs auth logic from doc 04 → redo" ║
  ║                                                                   ║
  ║                          ↻ (cycle repeats)                       ║
  ║                                                                   ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

---

## 3. Seven problems and seven WAVE answers

### Problem 1: Architectural drift

**Diagnosis:** AI generates code that works in isolation but doesn't fit the larger system. Every AI agent rewrites rather than adapting existing patterns. Ox Security: anti-patterns present in 80-100% of AI-generated code. The code runs. The architecture disintegrates.

```
  WITHOUT WAVE:                          WITH WAVE:
  
  Agent 1 → code A (works)              Full architecture
  Agent 2 → code B (works)              provided BEFORE coding
  Agent 3 → code C (works)              (DataPrep + RtS)
  A + B + C → 💥 (conflicts)                     ↓
                                         Agent 1 → code A (fits) ✅
  Root cause:                            Agent 2 → code B (fits) ✅
  Each agent saw a fragment,             Agent 3 → code C (fits) ✅
  none saw the whole                     A + B + C → coherent ✅
  Anti-patterns in 80-100%
  of code (Ox Security)                  Result: coherence enforced
                                         by context, not hope
```

**WAVE answer:** DataPrep creates complete documentation BEFORE the first line of code. Living Patterns deliver the best available domain knowledge. RtS with 11 layers ensures AI sees the full architecture — not a fragment. The industry is arriving at the same insight (CLAUDE.md files, AGENTS.md, Spec-Driven Development) — WAVE wraps it in a complete system.

---

### Problem 2: Technical debt explosion

**Diagnosis:** GitClear (211M lines of code): duplication 4×, refactoring -60%, code churn 2×. CodeRabbit: AI code has 1.7× more critical bugs. Apiiro: security vulnerabilities from 1,000 to 10,000 per month in Fortune 50 firms.

```
  TECHNICAL DEBT GROWTH WITH AI (GitClear, 2020-2024)
  
  Code duplication      ████████████████████████████████  4× increase
  Code churn            ████████████████                  2× increase
  Logic bugs            ████████████████████████          1.7× (CodeRabbit)
  Security vulns        ████████████████████████████████████████ 10× (Apiiro)
  Refactoring           ██████                            -60% decline
                        ─────────────────────────────────────────────▶
                        2020              2022              2024
```

**WAVE answer:** Three levels (DataPrep → Prompt2Data → Prompt2Prompt) create a cascade where no agent operates in a vacuum. Architectural context delivered BEFORE coding eliminates the main mechanism of debt accumulation — code generated without awareness of existing patterns.

---

### Problem 3: Code review bottleneck

**Diagnosis:** Faros AI: 98% increase in merged pull requests + 91% increase in review time. Amdahl's Law: you accelerate one machine on the assembly line, the rest operate at the same speed. A bottleneck forms.

```
  AMDAHL'S LAW IN PRACTICE

  WITHOUT WAVE:
  Coding:  ██░░░░░░░░░░░░░░░░░░░░░░   fast (AI)
  Review:  ░░░░░░██████████████████████ slow (human) ← BOTTLENECK
  Testing: ░░░░░░░░░░░░░░░░░░░░████████ waiting
  Deploy:  ░░░░░░░░░░░░░░░░░░░░░░░░░██ waiting
           ──────────────────────────────────────────▶ time

  WITH WAVE:
  Coding:  ████░░░░░░░░░░░░░░░░░░░░░░  accurate (>80% clean)
  Review:  ░░░░████░░░░░░░░░░░░░░░░░░░ shorter (fewer bugs)
  Testing: ░░░░░░░░████░░░░░░░░░░░░░░░ passes
  Deploy:  ░░░░░░░░░░░░████░░░░░░░░░░░ smooth
           ──────────────────────────────────────────▶ time
```

**WAVE answer:** The "first-pass quality" metric (target: >80% of components without fixes). Code built from full RtS context requires fewer corrections — the review queue doesn't balloon. A 50-prompt limit on the longest session prevents quality degradation.

---

### Problem 4: Context degradation

**Diagnosis:** In long sessions (>50 exchanges), agents claim functions exist that don't, reference files that weren't modified, "remember" agreements that never happened. Chroma research: models perform WORSE when context maintains logical flow — they "go with the flow" instead of analyzing.

| Session length | Hallucination risk | Code quality | WAVE recommendation |
|:---:|:---:|:---:|---|
| 1-20 exchanges | Low | High | Normal — work freely |
| 20-50 exchanges | Rising | Declining | Checkpoint — save state |
| 50-100 exchanges | High | Low | Close session, open new one |
| 100+ exchanges | Critical | Unpredictable | Prohibited — marathon = chaos |

**WAVE answer:** Hierarchical FILES structure (documentation in Claude project) serves as external memory — AI doesn't need to "remember," it can check. The practice of shorter topical chats forces fresh context at the start of each session. Checkpoints every 2 hours save state before context degrades.

---

### Problem 5: Skill erosion

**Diagnosis:** Vibe coding — 2025 Word of the Year (Collins Dictionary). Developer describes what they want in natural language, AI generates code, developer accepts without understanding. Stanford: 20% decline in junior developer hiring (ages 22-25) between 2022-2025. 54% of leaders plan to hire fewer juniors. The problem: a junior is a future architect in training — eliminating "the struggle with code" eliminates learning.

```
  THE SKILL EROSION CYCLE

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ AI writes│────▶│ Human    │────▶│ Skills   │────▶│ Greater  │
  │ for me   │     │ doesn't  │     │ atrophy  │     │ AI       │
  └──────────┘     │ practice │     └──────────┘     │ dependence│
                   └──────────┘                      └─────┬────┘
       ▲                                                    │
       └────────────────────────────────────────────────────┘
                    degradation loop

  WAVE BREAKS THE LOOP:

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ Human    │────▶│ Human    │────▶│ AI       │────▶│ Human    │
  │ UNDER-   │     │ SPECI-   │     │ EXECUTES │     │ VERIFIES │
  │ STANDS   │     │ FIES     │     │ with full│     │ and LEARNS│
  │ arch.    │     │          │     │ context  │     │          │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
       70% preparation                   30% execution
```

**WAVE answer:** The 70/30 principle means the developer MUST deeply understand architecture, data model, and business logic BEFORE AI writes the first line of code. Simon Willison drew the line: "if you've reviewed, tested, and understood it — it's not vibe coding." WAVE by definition puts understanding before execution.

---

### Problem 6: The "almost right" valley

**Diagnosis:** Stack Overflow 2025: 45% of developers — their main frustration is AI code that's "almost right, but not quite." Trust dropped from 43% to 29%, but usage rose to 84% — developers use tools they increasingly distrust. 67% spend MORE time debugging AI code than hand-written code.

| Metric | Value | Trend |
|---|:---:|:---:|
| Developers using AI for coding | 84% | ↑ rising |
| Trust in AI-generated code | 29% | ↓ falling (was 43%) |
| High trust in AI-generated code | 3% | ↓↓ minimal |
| Refuse to merge without review | 71% | ↑ rising |
| Regularly fix AI code | 66% | ↑ rising |
| More time debugging AI code | 67% | ↑ rising |

**WAVE answer:** Complete specifications from DataPrep and RtS drastically reduce the space where AI can "almost hit." CodeScene (2026) confirms: AI increases defect risk by 30% in projects with poor documentation — but in projects with clear architecture, the increase is significantly smaller.

---

### Problem 7: Individual vs organizational gap

**Diagnosis:** Faros AI: developers in high-AI-adoption teams complete 21% more tasks and merge 98% more PRs. But individual gains are neutralized by clogged reviews, flaky tests, and slow releases. Fed San Francisco (Feb 2026): macro-statistics show no AI effect on productivity.

```
  THE PRODUCTIVITY GAP

  Individual productivity:
  ████████████████████████████████████████  +21% tasks  ↑
  ████████████████████████████████████████████████████████  +98% PRs  ↑

  Organizational productivity:
  ████████████████████  ~0% net change  →

  Why? Because:
  Review:    ████████████████████████████████████████████  +91% time  ↑
  Bugs:      ████████████████████████████  +1.7× more  ↑
  Security:  ████████████████████████████████████████████████████  +10× vulns  ↑
  Tech debt: ████████████████████████████████████████  +4× duplication  ↑
```

**WAVE answer:** WAVE doesn't accelerate one link — it optimizes the entire chain. From idea (SCAN) through knowledge (PULSE) and specification (FALA) to code and verification (DoD). WAVE metrics measure not "how much code was produced" but "how many components passed without fixes" and "ratio of planned to actual hours."

### Seven problems summary — consolidated table

| # | Problem | Key data point | WAVE mechanism | Component |
|:---:|---|---|---|---|
| 1 | Architectural drift | 80-100% AI code has anti-patterns | Full context before coding | Living Patterns + RtS |
| 2 | Debt explosion | 4× duplication, -60% refactoring | Cascading 3-level context | DataPrep → P2D → P2P |
| 3 | Review bottleneck | +91% review time | First-pass quality >80% | RtS + session limits |
| 4 | Context degradation | Hallucinations after 50+ exchanges | FILES + short sessions | Checkpoints |
| 5 | Skill erosion | -20% junior hiring | 70% = human understands | 70/30 principle |
| 6 | "Almost right" valley | 67% more debugging | Precise specifications | RtS (11 layers) |
| 7 | Individual vs org gap | +21% individual, ~0% org | Whole cycle, not one link | Complete WAVE |

---

## 4. DooR — the doors between stages

### Definition of Operational Readiness

Imagine a rocket on the launch pad. Engineers don't ask "do we feel ready to launch?" They ask: "has every system passed verification? is fuel at the required level? is telemetry operational?" The checklist is closed, measurable, binary. Either everything is green, or the launch doesn't happen.

DooR in WAVE works on the same principle. Before you move to the next stage — verify that operational conditions are met. Not "do you feel ready" — but "does the required artifact exist and is it complete?"

### DooR — the transition mechanism

```
                    ╭─── DooR ───╮
                    │             │
  STAGE N           │  Readiness  │           STAGE N+1
  ─────────         │  standard   │           ──────────
                    │             │
  Work output  ───▶ │  ✅ ✅ ✅   │ ───▶  Next step
                    │  ✅ ✅ ✅   │        (certain that
                    │  ✅ ✅ ✅   │         input is
                    │             │         complete)
                    ╰─────────────╯
                          │
                    One ❌ = STOP
                    Go back and complete
```

### DooR vs Scrum's DoR

| Aspect | DoR (Scrum) | DooR (WAVE) |
|---|---|---|
| Question | "Does the team understand the task?" | "Is the artifact complete?" |
| Nature | State of mind (subjective) | State of document (verifiable) |
| Verification | Conversation with team | Test on artifact (3 RtS questions) |
| Granularity | General — "is it clear?" | Atomic — "what field type? what if NULL?" |
| For whom | People on the team | AI in the context window |

### Readiness standards in WAVE

| Standard | Stage | What it checks | Test |
|---|---|---|---|
| **Living Pattern** | KNOWLEDGE readiness | Best available knowledge? | 3 PULSE rounds complete |
| **RtS** | CODE readiness | 11-layer blueprint complete? | 3 questions: data / failure / security |
| **DoD** | Stage CLOSURE | Code matches blueprint? | Checklist: migrations, tests, flags |

### RtS ↔ DoD symmetry

```
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  ✅ RtS                  CODING SESSION              DoD ✅ │
  │                                                              │
  │  ◄── OPENS ──────────── RUNS ──────────── CLOSES ──►        │
  │                                                              │
  │  11 input layers               11 closure criteria           │
  │  ─────────────────             ────────────────────          │
  │  Data defined            ──▶   Migrations executed           │
  │  APIs specified          ──▶   Endpoints responding          │
  │  Logic with patterns     ──▶   Unit tests passing            │
  │  States and transitions  ──▶   Flags togglable               │
  │  Integrations mapped     ──▶   Modules connected             │
  │  UI described            ──▶   Components rendering          │
  │  Tests prepared          ──▶   E2E tests passing             │
  │  Meta established        ──▶   Conventions maintained        │
  │  Security locked         ──▶   Basic pen-test OK             │
  │  Resilience planned      ──▶   Failure scenarios OK          │
  │  Observability defined   ──▶   Logs and metrics live         │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
```

---

## 5. Components — an open map of tools

WAVE's component set is intentionally open. Like a forest ecosystem — the quality conditions are closed (soil, water, light), but the species list is open.

### Living Patterns — the living knowledge ecosystem

Living Patterns answer the question every team silently asks: **"Are we working from the best possible assumptions?"**

### Living Patterns — flow

```
  ┌──────────┐     ┌─────────────┐     ┌──────────────┐
  │  SCAN    │────▶│   PULSE     │────▶│ Living       │
  │  (once)  │     │   × N       │     │ Pattern v3   │
  │          │     │  areas      │     │              │
  │ Terrain  │     │ 3 rounds    │     │ ↻ auto-      │
  │ map      │     │ per area    │     │  improvement  │
  └──────────┘     └─────────────┘     └──────────────┘
```

### PULSE — the curve of diminishing returns

```
  Value
  added
    │
100%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·····97%
    │                                    ·
    │                          ·  ·  ·         ROUND 3: +12%
 85%├─ ─ ─ ─ ─ ─ ─ ─ · ─ ─ ─ ─              law, edge cases
    │              ·
    │           ·         ROUND 2: +25%
 60%├─ ─ ─ · ─ ─ ─      failures, controversies
    │    ·
    │  ·     ROUND 1: +60%
    │·       foundation: science, industry, practice
    ├──────────┬──────────┬──────────┬──────────▶
    0          1          2          3         (4) +3%
```

### Living Pattern structure

```
  LIVING PATTERN: [AREA NAME]
  │
  ├── I. STATE OF KNOWLEDGE
  │   ├── What we know for certain
  │   ├── What is debatable
  │   └── What is changing
  ├── II. PRINCIPLES AND STANDARDS
  │   ├── Design principles (rule + measure + implication)
  │   ├── Standards (target/alarm tables)
  │   └── Ecosystem implications
  ├── III. ERROR MATRIX (critical → major → subtle)
  ├── IV. DECISION MATRIX (variants + recommendation)
  ├── V. SUCCESS METRICS (leading + lagging)
  ├── VI. SOURCES (research + reports + case studies)
  └── CHANGE LOG (v1 → v2 → v3 → auto-improvement)
```

### Auto-improvement and Cross-Session Merge

A Living Pattern after three PULSE rounds is complete — but not closed. Two mechanisms keep it alive.

The first is cyclical auto-improvement: re-searching sources quarterly and comparing with the document's current state.

The second — discovered empirically — is **Cross-Session Merge**: running a new PULSE session with a deliberately different angle of attack (e.g., failures instead of successes, 3-year perspective instead of current state), then merging findings with the existing Living Pattern. Result: a document stronger than either session alone. A live project test yielded scoring of 7.4 (session 1) + 8.0 (session 2) = >9.0 (merged). Round 4 in the same session yields ~3% gain. Cross-Session Merge with a different angle yields 15-25% new value.

### LP Pipeline — automation infrastructure

Living Patterns have a working semi-automated pipeline on GitHub Actions. A Proposal Generator runs daily, suggesting new domains to investigate. The human approves — the pipeline runs SCAN, three PULSE rounds, and a Publisher that creates the final file. Cost per Living Pattern: under one dollar. Between each step, a label-based approval gate — AI proposes, human approves. WAVE philosophy in infrastructure.

The method has been confirmed as **stable and repeatable**: two independent PULSE sessions for the same area produced identical foundations (18 principles, ~25 errors, same target metrics) with different profiles — because the angle of attack was different.

### FALA — From Architecture to Live Application

```
  INPUT                      SESSION                    OUTPUT
  ═══════════════════════════════════════════════════════════════

  Concept documents       ┌──────────────┐
  + RtS Validation      ──▶│  SESSION 1   │──▶  RtS Audit
  + Decision Log          │  AUDIT       │     Gap Map ✅⚠️❌
                          └──────┬───────┘
                                 │ Owner answers questions
  Audit + answers          ┌──────────────┐
  + Blueprint Template   ──▶│  SESSION 2   │──▶  Blueprint
                            │  BLUEPRINT   │     11 layers + 3×PASS
                            └──────┬───────┘
                                   │ RtS Autotest
  Blueprint (verified)       ┌──────────────┐
  + full project context   ──▶│  SESSION 3   │──▶  Working code
                              │  CODE        │     + DoD ✅
                              └──────────────┘
```

### Decision Log

The central register of project decisions. Every approved decision: date, context, content, rationale, rejected alternatives, impact. It's not a notebook — it's the project's spine. When someone asks three months from now "why did we choose this path?" — the answer is in the log, not in someone's memory.

---

## 6. The completeness test — the AANP quadruple

In mechanics there are four fundamental forces — gravity, electromagnetism, strong and weak. Every physical phenomenon results from their interaction. Ignore one — your model doesn't describe reality.

In WAVE, every process has four fundamental elements. If one is missing — the process is leaky, with a high risk of not delivering the expected result.

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │              COMPLETE WAVE PROCESS                          │
  │                                                             │
  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
  │   │  ACTOR   │→ │  ACTION  │→ │   TOOL   │→ │ PRODUCT  │  │
  │   │  WHO     │  │  WHAT    │  │  WITH    │  │  RESULT  │  │
  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
  │                                                             │
  │   Four out of four = executable process ✅                  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

| Element | Question | If missing |
|---|---|---|
| **Actor** | WHO does it? Human, AI, both? | Task floats — nobody owns it |
| **Action** | WHAT do they do step by step? | People have tools, don't know how to use them |
| **Tool** | WITH WHAT? Prompt, template, checklist? | Every session = improvisation |
| **Product** | WHAT do you have when done? | Work continues, nobody knows when it's finished |

AANP doesn't tell you WHICH processes to build — it tells you HOW TO CHECK if what you've built is complete. WAVE is an open set of processes. AANP is a closed test for each of them.

### The open/closed principle

```
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓                                                              ▓
  ▓  CLOSED (non-negotiable):                                   ▓
  ▓  • 5 axioms of philosophy                                   ▓
  ▓  • AANP test (4 process elements)                           ▓
  ▓  • DooR principle (transition = artifact completeness)       ▓
  ▓                                                              ▓
  ▓  ┌──────────────────────────────────────────────────────┐   ▓
  ▓  │                                                      │   ▓
  ▓  │  OPEN (grows with experience and community):        │   ▓
  ▓  │                                                      │   ▓
  ▓  │  • New tools                                        │   ▓
  ▓  │  • New Living Patterns (per domain, per area)       │   ▓
  ▓  │  • New practices                                    │   ▓
  ▓  │  • New procedures                                   │   ▓
  ▓  │  • New DooR standards (per stage, per domain)       │   ▓
  ▓  │                                                      │   ▓
  ▓  └──────────────────────────────────────────────────────┘   ▓
  ▓                                                              ▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

---

## 7. WAVE and existing methodologies — a different question, a different level

### Floors of a building — where each methodology sits

```
  FLOOR 5    ┌─────────────────────────────────────────────┐
  STRATEGY   │  Company strategy, product vision            │
             └─────────────────────────────────────────────┘
                                   │
  FLOOR 4    ┌─────────────────────────────────────────────┐
  MANAGEMENT │  PRINCE2 / PMBOK                             │
             │  Schedule, budget, reporting                  │
             └─────────────────────────────────────────────┘
                                   │
  FLOOR 3    ┌─────────────────────────────────────────────┐
  ORGANIZE   │  Scrum / Kanban / XP                         │
             │  Sprints, backlog, standups                   │
             └─────────────────────────────────────────────┘
                                   │
  FLOOR 2    ┌─────────────────────────────────────────────┐
  PRINCIPLES │  Lean / Kaizen                               │
             │  Eliminate waste                              │
             └─────────────────────────────────────────────┘
                                   │
  FLOOR 1    ╔═════════════════════════════════════════════╗
  H-AI       ║  WAVE                                       ║
  SESSION    ║  How to collaborate with AI in a session     ║
             ╚═════════════════════════════════════════════╝
```

There is no conflict. You can run a project in PRINCE2, organize work in Scrum, apply Lean — and simultaneously use WAVE for every session with AI.

### WAVE on the 2026 landscape

| Approach | Main area | Strength | Limitation |
|---|---|---|---|
| **WAVE** | Complete cycle: knowledge → spec → code → verification | Full flow, deep context, proven in practice | Requires adaptation to other contexts |
| **SDD** (Spec-Driven Dev) | Specifications as source of truth | Industry support (GitHub, Amazon) | Risk of "waterfall in markdown" |
| **Context Engineering** | Managing AI's context window | Practical prompting techniques | No complete delivery cycle |
| **Thread-Based Eng.** | AI as supervised contributor | Structured review, clear roles | Weak preparation layer |
| **Structured Vibes** | Prototype with vibes, build with rigor | Pragmatic, phased | Weak context layer |

### What WAVE shares with traditional approaches, what's unique

| Aspect | Traditional | WAVE | Relationship |
|---|---|---|---|
| Preparation | PRINCE2: documentation for people | Documentation as FUEL for AI | Shared value, different motivation |
| Iterativeness | Scrum: sprints | PULSE: 3 rounds per area | Shared principle, different rhythm |
| Waste elimination | Lean: optimize flow | 70/30: invest in preparation | Shared goal, different mechanism |
| **AI as partner** | **None** | **Core of methodology** | **Unique** |
| **DooR** | **No equivalent** | **Readiness standards for AI** | **Unique** |
| **Living Patterns** | **No equivalent** | **Living knowledge base** | **Unique** |

### Why WAVE is gaining relevance — three 2026 trends

```
  TREND 1: Growing tool power = growing risk without guardrails
  ─────────────────────────────────────────────────────────────
  Cursor 2.0+ with 8 agents • Claude 1M tokens • Background Agents
  → More powerful tools without methodology = more powerful chaos generators

  TREND 2: The industry is moving toward Spec-Driven Development
  ─────────────────────────────────────────────────────────────
  Amazon Kiro • GitHub Spec-Kit • arXiv papers • Thoughtworks
  → Specifications as the main artifact — WAVE was there first

  TREND 3: The 2026-2027 "reckoning" is coming
  ─────────────────────────────────────────────────────────────
  Debt from 2023-2025 will reach critical mass • "Spaghetti Point"
  → Those who built with methodology — in a position of strength. The rest — patching.
```

---

## 8. Case study — IDareU Gen2

### Context

IDareU Gen2 is a three-sided marketplace connecting mentors, users, and brands through video challenges, expert feedback, gamification, and an innovative revenue-sharing model (IdUShare). Stack: Next.js 15, Supabase, Tailwind CSS, shadcn/ui. Team: CEO, COO, AI as the primary technology partner.

WAVE has been IDareU Gen2's development methodology from day one.

### WAVE flow in IDareU

```
  ┌─────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────┐
  │  SCAN   │────▶│   PULSE     │────▶│  Design      │────▶│   FALA   │
  │  1 session│   │   × 10      │     │ 20 core docs │     │  × module│
  │         │     │  areas      │     │ Decision Log │     │ 3 sessions│
  └─────────┘     └─────────────┘     └──────────────┘     └──────────┘
       ▼                ▼                    ▼                   ▼
   Terrain map    Living Patterns     31+ decisions         Code + DoD ✅
```

### IDareU Gen2 in numbers

| Metric | Value | Significance |
|---|:---:|---|
| Decisions in Decision Log | 31+ | Each with context and rejected alternatives |
| Core specification documents | 20 | Complete platform specification |
| Lines of documentation | ~7,000+ | Complete context — zero guessing |
| AI intelligence layers | 3 | HIVE + TACIT + AGAPE = Triada Logos |
| Cross-system flows | 6 | Each pillar enriches the others |
| Emergence layers | 5 | System learns what the designer didn't predict |
| Living Interface layers | 5 | Behavioral adaptive UI from day 0 |
| Team | 2 + AI | CEO, COO, Claude as technology partner |

### Full WAVE lifecycle — from idea to living product

```
  PREPARATION PHASE (70%)                  EXECUTION PHASE (30%)
  ═══════════════════════════              ═══════════════════════

  SCAN ──▶ Terrain map
       │
  PULSE × N ──▶ Living Patterns
       │                              DooR: Living Pattern ✅
  Design ──▶ Specifications
       │                              DooR: RtS ✅
  FALA Session 1 ──▶ Audit
       │
  FALA Session 2 ──▶ Blueprint ──▶ FALA Session 3 ──▶ Code + DoD ✅
       │
  LIFE ──▶ LP auto-improvement, Decision Log, Checkpoints
           Knowledge accumulates, doesn't scatter
```

---

## 9. Glossary

| Term | Definition |
|---|---|
| **WAVE** | Workflow Amplification via Vectored Expertise. Human-AI collaboration methodology. |
| **H-AI** | Human-AI. The human-AI pair as a unit of collaboration. |
| **DooR** | Definition of Operational Readiness. Category of readiness standards in WAVE. |
| **Living Pattern** | A living document of implementation knowledge, subject to cyclical verification. |
| **SCAN** | Solution Coverage Area Navigator. Tool identifying implementation areas. |
| **PULSE** | Pattern Universal Living Standard Engine. Builds a Living Pattern in 3 rounds. |
| **FALA** | From Architecture to Live Application. Procedure: concept document → code. |
| **RtS** | Requisite-to-Start. 11-layer technical blueprint. DooR element. |
| **DoD** | Definition of Done. Stage closure standard. DooR element. |
| **AANP** | Actor, Action, Tool (Narzędzie), Product. Process completeness test. |
| **DataPrep** | H-AI Level 1. Organizing domain knowledge. |
| **Prompt2Data** | H-AI Level 2. Precise task with full context. |
| **Prompt2Prompt** | H-AI Level 3. Meta-steering: evaluate, correct, iterate. |
| **Gap Map** | RtS tool. Comparing documentation against 11 layers: ✅ / ⚠️ / ❌ |
| **Objective function** | One sentence defining what we're optimizing. Process compass. |
| **Auto-improvement** | Cyclical verification of Living Pattern currency. |
| **Cross-Session Merge** | Auto-improvement variant: two PULSE sessions with different angles, merged into one stronger LP. |
| **LP Pipeline** | Semi-automated GitHub Actions pipeline: Proposal → SCAN → PULSE × 3 → Publisher. |
| **Productivity paradox** | Phenomenon: AI accelerates coding but doesn't improve delivery. |

---

*Document created: March 11, 2026*  
*Version: Software Engineering v1.2*  
*Concept author: Przemek Zieliński*  
*Written by: Claude Opus 4.6*  
*License: CC BY-SA 4.0*  
*Repository: github.com/przemek-zielinski/WAVE-Methodology*  
*First domain application: Software Engineering*  
*Data sources: METR, Faros AI, GitClear, CodeRabbit, Apiiro, NBER, MIT Media Lab, Stack Overflow, Fed San Francisco (February 2026)*
