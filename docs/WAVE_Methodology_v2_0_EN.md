# WAVE Methodology
## Workflow Amplification via Vectored Expertise
### A Human-AI Collaboration Methodology

**Version:** 2.0  
**Date:** March 2026  
**Author:** Przemysław Zieliński  
**Documentation co-author:** Claude (Anthropic)  
**License:** CC BY-SA 4.0  
**Repository:** github.com/przemek-zielinski/WAVE-Methodology

---

## Table of Contents

— Quick Start — begin here
0. In one sentence, one paragraph, one minute
1. The Problem
2. Philosophy — five axioms and three levels of H-AI collaboration
3. Architecture — three layers of WAVE
4. DooR — doors between stages
5. Components — an open map of tools
6. Completeness test — the AANP quartet
7. Product Profiles — WAVE at every scale
8. What and how to measure
9. WAVE beyond software — six directions
10. WAVE and existing approaches
11. How to start
12. Frequently asked questions
13. Origin story
14. Citation and license

### WAVE map — architecture at a glance

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║   WAVE — Workflow Amplification via Vectored Expertise                 ║
║   Human-AI Collaboration Methodology                                  ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  LAYER 1: PHILOSOPHY (closed — 5 axioms)                      │   ║
║   │                                                                │   ║
║   │  70/30 • Human leads • Build complete • Journey=value         │   ║
║   │  • Failures teach                                              │   ║
║   │                                                                │   ║
║   │  Meta-axiom: Currents & Tensions (navigate, don't optimize)   │   ║
║   │  Three H-AI levels: DataPrep → Prompt2Data → Prompt2Prompt    │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  LAYER 2: COMPONENTS (open — the set grows)                   │   ║
║   │                                                                │   ║
║   │  DooR — Definition of Operational Readiness                   │   ║
║   │  Living Patterns (SCAN, PULSE) • FALA • Decision Log          │   ║
║   │  [+ future components → open set]                             │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  LAYER 3: PRACTICES (open — habits accumulate)                │   ║
║   │                                                                │   ║
║   │  Checkpoints • Shorter sessions • Versioning • Collaboration  │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  COMPLETENESS TEST: AANP (closed)                             │   ║
║   │  Every process = Actor + Action + iNstrument + Product        │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Terminological note

WAVE is a **methodology** — a structured set of principles for how to do work. Not a "method" (a single technique), not a "model" (a simplified representation), not a "framework" (an overused word that has lost its meaning). Scrum, PRINCE2, Extreme Programming — these are methodologies. WAVE joins this category, addressing a question none of them cover: how to collaborate with AI.

---

## Quick Start — begin here

Don't want to read fourteen chapters before you start? Here's the minimum.

**What it is:** A methodology for human-AI collaboration. It tells you how to prepare context, run sessions, and build knowledge so that AI works from the best possible assumptions — not from guessing.

**How to start in three steps:**

```
  STEP 1 — Choose your product profile
  ──────────────────────────────────────
  □ Prototype / POC?       → DISCOVERY profile (1-5 days)
  □ MVP / pilot?           → BUILD profile (4-8 weeks)
  □ Full product?          → SCALE profile (months)

  Not sure? Start with DISCOVERY. You can always move up.

  STEP 2 — Run SCAN
  ──────────────────
  Open a chat with AI. Paste the SCAN prompt with a description
  of your solution. You'll get a list of areas to investigate
  with ready-made parameters for the next step.

  STEP 3 — Run PULSE for the first area
  ──────────────────────────────────────
  Take the most important area from the SCAN list.
  Paste the PULSE prompt with parameters.
  Run Round 1. Evaluate the result. You now have your first
  Living Pattern — a living knowledge document.
  Repeat for subsequent areas.
```

**What you need:** Access to AI with web search enabled (Claude, ChatGPT, Gemini). A description of your solution. Optionally: existing project documentation.

**Files to download from the repository:**

| File | What it does | When to use |
|---|---|---|
| `SCAN-Prompt.md` | Identifies areas to investigate | At the start — once |
| `SCAN-HowTo.md` | SCAN usage guide | Before your first SCAN |
| `PULSE-Prompt.md` | Builds a Living Pattern in 3 rounds | Per area from the SCAN list |
| `PULSE-HowTo.md` | PULSE usage guide | Before your first PULSE |

The rest of this document explains WHY it works, HOW it's built, and WHAT you can achieve at larger scale.

---

## 0. In one sentence, one paragraph, one minute

### One sentence

WAVE is a human-AI collaboration methodology — it tells you how to prepare context, run sessions, and build knowledge so that AI works from the best possible assumptions, not from guessing.

### One paragraph

Everyone who works with AI knows the feeling — AI produces something mediocre, you refine it, refine again, and after an hour you have something usable. Next day you start from scratch. WAVE inverts this ratio: you spend the majority of your time preparing context and knowledge, the minority on execution — and that execution is accurate on the first shot. WAVE provides concrete tools: SCAN identifies what you need to know, PULSE builds that knowledge in three rounds, Living Pattern keeps it current. Result: AI stops guessing and starts acting like a partner who genuinely understands your project.

### One minute

We have a problem no one has named. Millions of people work with AI every day — writing code, designing products, analysing data, creating documents. And most of them do it the same way: type a prompt, see what comes out, refine, refine, refine. It's like building a house without blueprints — you put up a wall, tear it down, try again. It works, but you waste most of the potential.

WAVE says: invert the ratio. Before you start building — prepare context. Gather knowledge. Define what you're optimising for. Give AI the full picture, not scraps of information. Preparation dominates execution. And that execution is accurate, because AI doesn't guess — it knows.

WAVE is not another project management framework. It doesn't compete with Scrum or Lean. WAVE operates at a level no existing methodology addresses — the level of the working session, where a human and AI create something concrete together. It's open-source, it's free, and anyone can start using it today — from one tool, from one session.

---

## 1. The Problem

In 2026, every organisation in the world has access to artificial intelligence. Hospitals use it for diagnostics. Law firms for precedent analysis. Schools for personalised teaching. Engineers for design optimisation. Development teams for code generation.

And almost all of them do it the same way: chaotically.

The typical interaction looks like this: a specialist asks AI a question, gets a result, realises that's not quite right, rephrases, gets a slightly different result, refines, asks again. Ten iterations later the result is passable, but far from what was possible.

```
  WITHOUT A METHODOLOGY                 WITH WAVE
  ─────────────────────────────          ─────────────────────────────

  😐 → [prompt] → 🤖 → result 4/10     😐 → [context + knowledge + goal]
  😐 → [refine] → 🤖 → result 5/10            ↓
  😐 → [refine] → 🤖 → result 6/10       🤖 → result 9/10 ✅
  😐 → [refine] → 🤖 → result 7/10
  😐 → [refine] → 🤖 → result 8/10 ✅   time: ~1h
                                          (preparation + execution)
  time: 3h+ (zero preparation,
  all spent on refining)
```

This is not a failure of artificial intelligence. It's a failure of collaboration. The problem isn't in AI — AI is powerful. The problem isn't in the human — humans have expertise. The problem lies in **the space between them** — in how human knowledge and intent reaches AI.

```
  ┌─────────────┐          ╔═══════════════════╗          ┌─────────────┐
  │             │          ║                   ║          │             │
  │   HUMAN     │          ║   THE SPACE       ║          │     AI      │
  │             │          ║   BETWEEN         ║          │             │
  │  • knowledge│ ──??──▶  ║                   ║  ──??──▶ │  • power    │
  │  • context  │          ║   unoccupied      ║          │  • scale    │
  │  • intent   │          ║                   ║          │  • speed    │
  │  • goal     │          ║   ◀── WAVE ──▶    ║          │  • synthesis│
  │             │          ╚═══════════════════╝          │             │
  └─────────────┘                                         └─────────────┘
```

Tools exist. What's missing is a **methodology** — a structured, layered, measurable system of collaboration with AI, built around one principle: **the human leads, AI amplifies**.

What currently passes for approaches to AI collaboration doesn't fill this gap:

| Approach | What it is | What it lacks |
|---|---|---|
| **Prompt engineering** | Techniques for writing better queries | No project structure, no metrics, no preparation layer |
| **"Agile AI"** | Agile with "with AI" appended | No rethinking of the human-AI relationship |
| **Responsible AI guidelines** | Ethical policies | Not a workflow — says what to avoid, not how to work |
| **Tool-specific courses** | Product instruction manuals | Product-specific, not a methodology |

WAVE fills this gap.

---

## 2. Philosophy — five axioms and three levels of H-AI collaboration

### Five axioms

WAVE's philosophy is a closed set — five convictions that are non-negotiable. Everything else in WAVE can change, grow, evolve. These five — cannot. They are like the laws of thermodynamics: you can build any machine, but these laws always apply.

| # | Axiom | Essence | Analogy |
|:---:|---|---|---|
| 1 | **Preparation dominates** | Most time on preparation, the rest on execution | Cheetah: 16h observation → 12s chase |
| 2 | **Human leads, AI amplifies** | AI is an amplifier of expertise, not a replacement | Telescope doesn't replace the astronomer's eye |
| 3 | **Build complete, activate progressively** | Full architecture from day 1, gradual activation | Fruit tree: planted complete, fruit in 2 years |
| 4 | **Journey and process = value** | Discoveries emerge between tasks | Serendipity: Columbus → America |
| 5 | **Failures teach more than successes** | Others' mistakes with data > others' wins without context | Success lulls, failure sharpens |

**Axiom 1 — Preparation dominates execution.** WAVE rests on a counterintuitive rule: spend the majority of your time on preparation, the minority on execution with AI. This is gravity, not a mandate — the point of attraction depends on the project's scale. In a small prototype the ratio naturally pulls toward 60/40 (the product is too simple for preparation to need dominance). In a mid-sized project it lands at 70/30 (where the axiom breathes most fully). In a large product it pulls toward 50/50 (execution grows linearly with each module). But in ALL cases, preparation accounts for at least half the work — a radical inversion of chaotic prompting, where preparation equals zero.

The analogy is **mise en place** — the culinary principle where a chef prepares and organises all ingredients before service. During service, execution is fast, precise, and calm. Investment in preparation makes excellence under pressure possible.

**Axiom 2 — Human leads, AI amplifies.** AI is an amplifier of expertise — not its replacement. Like an amplifier doesn't replace a guitar, just lets it fill a stadium. The human defines the objective function, evaluates results, makes decisions. AI processes, synthesises, generates — at a scale unavailable to humans. But direction always belongs to the human. AI without human direction produces output that's correct but generic — like an orchestra without a conductor.

**Axiom 3 — Build complete, activate progressively.** Don't build half and "add the rest later." Build the whole thing — but switch it on piece by piece, as conditions mature. Design the full architecture from day one, but activate through feature flags as you collect data and confirm assumptions.

**Axiom 4 — Journey and process have value.** The most valuable discoveries appear between tasks — in digressions, in experiments, in moments when AI responds with something unexpected and the human says: "wait, this is interesting." WAVE is not a straight line from A to B. It's a river flowing toward the sea, creating meanders and deltas along the way — and in those bends lives value that no linear plan would find.

**Axiom 5 — Failures teach more than successes.** Success lulls the senses. Failure sharpens them. That's why every WAVE research tool (PULSE) deliberately searches for failures in one of its rounds — because others' mistakes with numbers are more valuable than others' successes without context. Empirical confirmation: a WAVE repeatability test (March 2026) showed that two independent PULSE sessions for the same area arrived at an identical number of principles (18), a similar number of errors (25 vs 26), and the same foundations — but with different profiles. A session focused on failures produced a different angle than a session focused on the future. Both needed, neither complete alone.

### Currents and Tensions — the navigation meta-axiom

The five axioms say WHAT matters. Currents and Tensions says HOW those values compete with each other in every concrete decision — and that the operator's role is to navigate that competition, not to eliminate it.

Like ocean currents — they flow alongside each other ceaselessly, sometimes aligned, sometimes opposing. A sailor doesn't fight currents. She reads them and chooses the optimal path for current conditions. She doesn't try to ride all of them at once, because that's physically impossible. And she always keeps a reserve for the unpredictable current around the corner.

```
  THE TENSION FIELD — every decision plays out at the intersection of axes

  Output quality  ◄─────────────────────────────────► Algorithm simplicity
  Stability       ◄─────────────────────────────────► Feature richness
  Depth           ◄─────────────────────────────────► Cost and time
  Consistency     ◄─────────────────────────────────► Flexibility
  Solution now    ◄─────────────────────────────────► Capacity reserve
  Control         ◄─────────────────────────────────► Creative freedom

  The operator doesn't optimize one axis.
  The operator navigates BETWEEN axes — reading
  which configuration is critical RIGHT NOW.
```

**Three fundamental observations.**

First: tensions don't disappear. You can't "solve" them — you can only navigate them. Every improvement on one axis costs something on another. Attempting to optimize all at once leads to paralysis or to a system that's "a little good at everything" but excellent at nothing.

Second: the tension configuration changes over time. Early in a project, quality↔simplicity dominates. In the middle — stability↔features. Near the end — cost↔depth. An operator who reads the current configuration makes better decisions than an operator with fixed rules regardless of phase.

Third — and most important: **reserve is a first-class value, not waste.** In optimization thinking, reserve looks like squandered potential — unused capacity, unsolved problem. In navigation thinking, reserve is a strategic buffer for the problem you don't yet see. Lean says "eliminate waste." Currents and Tensions says: "capacity reserve — budgetary, architectural, mental — is not waste. It is the buffer that determines the system's ability to survive."

**Emergence is born at the intersection of tensions.** This is the core discovery. Currents and Tensions is not merely a description of trade-offs — it describes the conditions under which emergence occurs. When an operator consciously navigates tensions instead of optimizing a single attribute, they open space for discoveries they didn't plan. Rolling back four iterations of table repair wasn't a failure — it was a moment of emergence from which an axiom worth more than the repaired table was born.

Carl Benedikt Frey in "How Progress Ends" (Princeton University Press, 2025) confirms this observation across a thousand years of civilization history: innovation dies for the same reason every time — when systems stop navigating the tension between exploration and exploitation and freeze into one mode. Song Dynasty China froze in centralization. Silicon Valley is freezing in concentration. Corporations freeze after scaling. WAVE transfers this observation from the civilization level to the working session — and gives the operator tools for conscious navigation.

**The navigation formula — three questions before every decision:**

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │  1. WHICH CURRENT DOMINATES RIGHT NOW?                 │
  │     (Quality? Stability? Cost? Reserve? Freedom?)      │
  │                                                         │
  │  2. WHAT DO I GAIN, WHAT DO I LOSE?                    │
  │     (Every improvement on one axis has a price          │
  │      on another)                                        │
  │                                                         │
  │  3. AM I LEAVING SUFFICIENT RESERVE?                   │
  │     (If a problem I can't see waits around the corner  │
  │      — can I absorb it?)                               │
  │                                                         │
  │  Three questions. A few seconds of reflection.         │
  │  Doesn't slow the work — accelerates it,               │
  │  because it eliminates iterations into dead ends.      │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

**The operator's role.** AI doesn't see the tension field on its own. AI optimizes whatever you assign — if you assign table repair, it will repair the table through four iterations, each more complex, until the operator says "stop, we're rolling back." The human in WAVE leads not because they're smarter than AI in a given domain. They lead because they see the tension field as a whole — all axes simultaneously — and make decisions AI cannot make: "we're rolling back, because reserve matters more than perfection."

This is the operational extension of the axiom "the human leads, AI amplifies": the human leads **navigation through tensions**, AI amplifies **execution in the chosen direction**.

### Three levels of H-AI collaboration

Beneath the axioms lives a model describing HOW every human-AI interaction unfolds in WAVE. Three levels, always in the same sequence — like inhale, pulse, and exhale.

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║                                                                   ║
  ║  Level 1: DataPrep                                     INHALE   ║
  ║  ─────────────────                                               ║
  ║  Human organises domain knowledge                                ║
  ║  Gathers context, defines goals, structures information          ║
  ║  ● Who: HUMAN (primarily)                                       ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Level 2: Prompt2Data                                  PULSE    ║
  ║  ────────────────────                                            ║
  ║  Precise task with full context                                  ║
  ║  AI doesn't guess intent — intent is explicit                    ║
  ║  ● Who: HUMAN → AI                                              ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Level 3: Prompt2Prompt                                EXHALE   ║
  ║  ──────────────────────                                          ║
  ║  Meta-steering: evaluate output, correct course, iterate         ║
  ║  Human shapes direction, doesn't write content                   ║
  ║  ● Who: HUMAN (evaluates) ← AI (proposes)                      ║
  ║                                                                   ║
  ║                          ↻ (cycle repeats)                       ║
  ║                                                                   ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

**DataPrep** — organising domain knowledge before working with AI. When an architect designs a skyscraper, they don't start by drawing bricks. They start with vision, then requirements, then architecture, then specifications. Each document gives birth to the next. DataPrep works the same way — in every domain.

**Prompt2Data** — a precise task for AI with full context. Not "make something nice" but "based on this menu, these ingredients, these constraints — create a recipe meeting all conditions." Zero guessing. One precise result.

**Prompt2Prompt** — meta-steering of the collaboration. Evaluating output, correcting course, iterating. The human looks at what AI produced and says: "this is good, but search from the other side" or "the security aspect is missing, expand." This is the level where the human truly leads.

### Bidirectional flow

AI doesn't deliver finished results. The human verifies, corrects, and sends back. This isn't an AI deficiency — it's a collaboration design.

```
  HUMAN EXPERTISE                    AI AS AMPLIFICATION
  ┌──────────────────────────┐       ┌──────────────────────────┐
  │ Domain knowledge         │       │ Data processing          │
  │ Situational context      │──────▶│ Pattern recognition      │
  │ Experience               │       │ Variant generation       │
  │ Judgement and intuition  │◀──────│ Scaling repetitive ops   │
  │ Responsibility           │       │                          │
  └──────────────────────────┘       └──────────────────────────┘
            ↕ BIDIRECTIONAL FLOW ↕
```

Every correction updates the preparation. If AI misunderstood a requirement — that requirement was probably unclear. Fix it in DataPrep, not just in the output.

---

## 3. Architecture — three layers of WAVE

WAVE as a methodology consists of three layers of different natures. Philosophy is closed — five axioms, immutable. Components are open — new tools can emerge, the community can add them. Practices accumulate with experience.

Like a forest ecosystem — the quality conditions are closed (soil, water, light), the species list is open. The forest grows. New species appear. Old ones evolve. WAVE lives the same way.

```
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓                                                            ▓
  ▓  CLOSED (non-negotiable):                                  ▓
  ▓  • 5 axioms of philosophy                                  ▓
  ▓  • Currents and Tensions (navigation meta-axiom)           ▓
  ▓  • AANP test (4 process elements)                          ▓
  ▓  • DooR principle (transition = artefact completeness)     ▓
  ▓                                                            ▓
  ▓  ┌──────────────────────────────────────────────────────┐  ▓
  ▓  │                                                      │  ▓
  ▓  │  OPEN (grows with experience and community):         │  ▓
  ▓  │                                                      │  ▓
  ▓  │  • New tools                                         │  ▓
  ▓  │  • New Living Patterns (per industry, per area)      │  ▓
  ▓  │  • New practices                                     │  ▓
  ▓  │  • New procedures                                    │  ▓
  ▓  │  • New DooR standards (per stage, per industry)      │  ▓
  ▓  │                                                      │  ▓
  ▓  └──────────────────────────────────────────────────────┘  ▓
  ▓                                                            ▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

### Three layers — table

| Layer | Nature | Contains | Does it change? |
|---|---|---|---|
| **1. Philosophy** | Closed | 5 axioms + Currents and Tensions + 3 H-AI levels | No — axioms always apply |
| **2. Components** | Open | Tools, standards, procedures | Yes — the set grows |
| **3. Practices** | Open | Work habits | Yes — they accumulate with experience |

---

## 4. DooR — doors between stages

### Definition of Operational Readiness

Imagine a rocket on the launch pad. Engineers don't ask "do we feel ready for launch?" They ask: "has every system passed verification? Is fuel at level? Is telemetry working?" The list is closed, measurable, binary. Either everything is green, or launch doesn't happen.

DooR in WAVE works on the same principle. Before you move to the next stage — verify that operational conditions are met. Not "do you feel ready" — but "does what's required exist."

```
                    ╭─── DooR ───╮
                    │            │
  STAGE N           │  Readiness │           STAGE N+1
  ─────────         │  standard  │           ──────────
                    │            │
  Work output  ───▶ │  ✅ ✅ ✅ │ ───▶  Next step
                    │  ✅ ✅ ✅ │        (with certainty
                    │            │         that input is
                    │            │         complete)
                    ╰────────────╯
                          │
                    One ❌ = STOP
                    Go back and fill the gap
```

DooR is the umbrella category for all readiness standards in WAVE. Every tool that defines "when you can move forward" belongs to the DooR family.

### DooR standards in the current ecosystem

| Standard | Stage | What it checks | Example test |
|---|---|---|---|
| **Living Pattern** | Knowledge READINESS | Do I have the best available knowledge? | 3 PULSE rounds complete, structure sound |
| **RtS** (in SE) | Code READINESS | Is the specification complete? | Artefact test — zero "it depends" |
| **DoD** (in SE) | Stage CLOSURE | Does output = specification? | Verification checklist |

The DooR family is open. New readiness standards can emerge. The principle is closed: **every transition has its door, and completeness opens it.**

---

## 5. Components — an open map of tools

### Living Patterns — a living knowledge ecosystem

Living Patterns answer the question every team asks in silence: **"Are we working from the best possible assumptions?"**

The usual answer is one of three: "we don't know, we didn't have time to check," "we checked, but that was six months ago," "each of us checked something different." Living Patterns solve all three simultaneously.

```
  ┌──────────┐     ┌─────────────┐     ┌──────────────┐
  │  SCAN    │────▶│   PULSE     │────▶│ Living       │
  │  (once)  │     │   × N       │     │ Pattern v3   │
  │          │     │  areas      │     │              │
  │ Terrain  │     │ 3 rounds    │     │ ↻ self-      │
  │ map      │     │ per area    │     │  improvement │
  └──────────┘     └─────────────┘     └──────────────┘
```

**SCAN — Solution Coverage Area Navigator.** A radar scanning the horizon. Based on a solution description, it identifies ALL areas requiring deeper analysis — from obvious to easy-to-miss. Run once — at the project's start.

**PULSE — Pattern Universal Living Standard Engine.** A pulse — a rhythmic cycle of three beats. For one area, it conducts three research-synthesis rounds. Round 1 builds the foundation (~60% of knowledge). Round 2 verifies from the other side — looking for failures instead of successes (~25%). Round 3 searches peripheral directions (~12%). Between rounds, the human decides.

```
  Value
  added
    │
100%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·····97%
    │                                    ·
    │                          ·  ·  ·         ROUND 3: +12%
 85%├─ ─ ─ ─ ─ ─ ─ ─ · ─ ─ ─ ─              peripheral
    │              ·
    │           ·         ROUND 2: +25%
 60%├─ ─ ─ · ─ ─ ─      failures, controversies
    │    ·
    │  ·     ROUND 1: +60%
    │·       foundation: science, industry, practice
    ├──────────┬──────────┬──────────┬──────────▶
    0          1          2          3         (4) +3%
```

**Living Pattern — a living knowledge document.** The product of PULSE — a complete reference for one area. Standardised structure: state of knowledge, principles and standards, error matrix, decision matrix, success metrics, sources. Subject to cyclical self-improvement — like an organism that breathes. Inhale is new knowledge. Exhale is document update.

**Self-improvement and Cross-Session Merge.** A Living Pattern after three PULSE rounds is complete — but not closed. Two mechanisms keep it alive. The first is cyclical self-improvement: re-searching sources quarterly and comparing with the document's current state. The second — discovered empirically — is **Cross-Session Merge**: running a new PULSE session with a deliberately different angle of attack (e.g. failures instead of successes, three-year perspective instead of current state), then merging findings with the existing Living Pattern. Result: a document stronger than either session alone. A live project test yielded scoring of 7.4 (session 1) + 8.0 (session 2) = >9.0 (merged). Round 4 in the same session yields ~3% gain. Cross-Session Merge with a different angle yields 15–25% new value.

**LP Pipeline — automation infrastructure.** Living Patterns have a working semi-automated pipeline on GitHub Actions. A Proposal Generator runs daily, suggesting new domains to investigate. The human approves — the pipeline runs SCAN, three PULSE rounds, and a Publisher that creates the final file. Cost per Living Pattern: under one dollar. Between each step, a label-based approval gate — AI proposes, human approves. WAVE philosophy in infrastructure.

### FALA — From Architecture to Live Application

FALA is a procedure transforming conceptual documentation into working code (or another end artefact). Three sessions, with clear transition criteria between each.

```
  Session 1 ──▶ Session 2 ──▶ Session 3
  AUDIT         BLUEPRINT      EXECUTION

  Measure       Fill the       Execute from
  distance      specification  complete
  (what I have  (what's        context
  vs what I     missing →
  need)         fill it)
```

In software engineering, FALA includes the RtS pipeline (Requisite-to-Start) with eleven layers of technical specification and a three-question self-test. In other domains, FALA adapts — sessions follow the same logic (audit → specification → execution), but specification layers differ.

Full FALA documentation for software engineering: separate document in the repository.

### Decision Log

Central registry of project decisions. Each approved decision: date, context, content, rationale, rejected alternatives, impact. Not a notebook — a project backbone. When someone asks "why did we choose this path?" three months later — the answer is in the log, not in someone's memory.

### Practices

Work habits that accumulate with experience. An open set.

**Checkpoints.** After two hours of intensive work — stop. Generate a session log: what we did, what decisions were made, what we rejected. Project memory that survives a closed chat.

**Shorter themed sessions.** One topic per session. No hundred-message marathons — short, targeted interactions. AI works better with fresh context than with an overloaded window.

**Document versioning.** Every document has a version, date, changelog. Not "file_final_v2_REALLY_final." A readable, predictable structure.

**Collaboration imperative.** Recognise breakthrough moments and celebrate them. Process and journey have value — not just the destination.

---

## 6. Completeness test — the AANP quartet

In mechanics there are four fundamental forces — gravity, electromagnetism, strong and weak. Every physical phenomenon results from their interplay. Ignore one — your model doesn't describe reality.

In WAVE, every process has four fundamental elements. Missing one — the process is leaky, with high risk that it won't deliver the expected result.

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │              COMPLETE WAVE PROCESS                          │
  │                                                             │
  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
  │   │  ACTOR   │→ │  ACTION  │→ │iNSTRUMENT│→ │ PRODUCT  │    │
  │   │  WHO     │  │  WHAT    │  │  WITH    │  │  RESULT  │    │
  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
  │                                                             │
  │   Four of four = executable process ✅                      │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

| Element | Question | If missing |
|---|---|---|
| **Actor** | WHO does this? Human, AI, both? | Task floats — nobody is responsible |
| **Action** | WHAT do they do step by step? | People have tools, don't know how to use them |
| **iNstrument** | WITH WHAT? Prompt, template, checklist? | Every session = improvisation |
| **Product** | WHAT do you hold when done? | Work, work, never know when it's finished |

AANP doesn't tell you WHICH processes to build — it tells you HOW TO CHECK if what you built is complete. WAVE is an open set of processes. AANP is a closed test for each of them.

---

## 7. Product Profiles — WAVE at every scale

WAVE is one methodology with three intensity profiles — matched to the type of solution being built. Same philosophy, different component scale.

```
  DISCOVERY ──────────── BUILD ──────────── SCALE
  (POC/prototype)         (MVP/pilot)        (Product)
  │                       │                  │
  │  Goal: validate       │  Goal: deliver   │  Goal: scale
  │  the idea             │  value           │  and maintain
  │                       │                  │
  │  Preparation:         │  Preparation:    │  Preparation:
  │  2-4h                 │  41-73h          │  163-385h
  │                       │                  │
  │  P/E ratio:           │  P/E ratio:      │  P/E ratio:
  │  ~60/40               │  ~70/30          │  50-70/30-50
  └───────────────────────┴──────────────────┘
```

| Dimension | DISCOVERY (POC) | BUILD (MVP) | SCALE (Product) |
|---|---|---|---|
| **Goal** | Validate the idea | Deliver value | Scale and maintain |
| **Time** | 1–5 days | 4–8 weeks | Months → years |
| **SCAN** | 3-5 key questions | 6-8 areas | 10-15 with dependencies |
| **PULSE** | 1 round, 1-2 areas | 2 rounds, 3-5 areas | 3 rounds, 8-15 areas |
| **P/E ratio** | ~60/40 | ~70/30 | 50-70 / 30-50 |
| **Expandability** | To MVP without rebuild | To product without rebuild | To enterprise platform |

Profiles are evolutionary — Discovery shifts to Build, Build to Scale. Code, documentation, and decisions grow with you. Nothing is discarded.

Full profile description with hourly breakdown, comparison tables, and decision tree: **WAVE Product Profiles** (companion document in the repository).

---

## 8. What and how to measure

A methodology without metrics is philosophy. WAVE defines concrete indicators of H-AI collaboration quality.

### Core indicators

| Indicator | Definition | Starting | Proficiency | Mastery |
|---|---|:---:|:---:|:---:|
| **PSR** (Prompt Success Rate) | % of prompts yielding good output on 1st try | ~60% | >80% | >90% |
| **DPC** (Data Preparation Coverage) | % of domain knowledge structured in DataPrep | ~40% | >70% | >85% |
| **TFCO** (Time to First Correct Output) | Time to first correct result | 2-4h | 30-60 min | 15-30 min |
| **RR** (Revision Rate) | Average revisions per task | 3-5 | 1-2 | ~0 |

### Self-improvement trajectory

```
  PSR
  (first-try
  success)
    │
 90%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · ·  mastery
    │                                      · · ·
 80%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · · ·
    │                        · · ·                        proficiency
 70%├─ ─ ─ ─ ─ ─ ─ ─ · · · ·
    │            · · ·
 60%├─ ─ · · · ·                                          starting
    │  · ·
    │ ·
    ├──────────┬──────────┬──────────┬──────────▶ Weeks
    0          4          8          12
```

Improvement doesn't come from AI getting smarter. It comes from your DataPrep deepening and your templates maturing. The pattern is consistent regardless of domain.

---

## 9. WAVE beyond software — six directions

WAVE's three layers — organising domain knowledge, precise tasking for AI, meta-steering of the collaboration — contain nothing specific to any industry. They describe a universal pattern of human-AI collaboration.

Below are six domains where WAVE has direct applicability. These are sketches, not full implementations — invitations for practitioners to test and report back.

| Domain | DataPrep | Prompt2Data | Prompt2Prompt |
|---|---|---|---|
| **Pharmaceuticals** | Molecule data, interactions, trial results | AI models molecular bindings | Iterative refinement of predictions |
| **Healthcare** | Medical history, results, genetic context | AI analyses diagnostic patterns | Clinician verifies with clinical judgement |
| **Education** | Student results, learning styles, behaviour | AI proposes learning paths | Teacher corrects for class dynamics |
| **Law** | Facts, legislation, case law | AI analyses precedents, identifies risks | Lawyer verifies litigation strategy |
| **NGO** | Community data, past interventions | AI identifies effectiveness patterns | Team corrects with field knowledge |
| **Engineering** | Specifications, material constraints, norms | AI generates design variants | Engineer verifies from experience |

### The common pattern

In every case, the schema is identical:

```
  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
  │                 │     │                 │     │                 │
  │  HUMAN          │     │  AI             │     │  HUMAN          │
  │  organises      │────▶│  processes at   │────▶│  verifies with  │
  │  expertise      │     │  scale beyond   │     │  judgement      │
  │                 │     │  human reach    │     │  and decides    │
  │  (DataPrep)     │     │  (Prompt2Data)  │     │  (Prompt2Prompt)│
  │                 │     │                 │     │                 │
  └─────────────────┘     └─────────────────┘     └─────────────────┘
```

The difference is in the content — a pharmacist's data looks different from a lawyer's. But the collaboration structure is the same. Just as Lean left Toyota's factories and reached hospitals — WAVE left software engineering, but its three layers speak about expertise, not code.

---

## 10. WAVE and existing approaches

### Floors of a building — where each methodology sits

```
  FLOOR 5   ┌─────────────────────────────────────────────┐
  STRATEGY  │  Company strategy, product vision           │
            └─────────────────────────────────────────────┘
                                    │
  FLOOR 4   ┌─────────────────────────────────────────────┐
  MANAGEMENT│  PRINCE2 / PMBOK                            │
            │  Schedule, budget, reporting                │
            └─────────────────────────────────────────────┘
                                    │
  FLOOR 3   ┌─────────────────────────────────────────────┐
  ORGANISING│  Scrum / Kanban / XP                        │
            │  Sprints, backlog, standups                 │
            └─────────────────────────────────────────────┘
                                    │
  FLOOR 2   ┌─────────────────────────────────────────────┐
  PRINCIPLES│  Lean / Kaizen                              │
            │  Eliminate waste                            │
            └─────────────────────────────────────────────┘
                                    │
  FLOOR 1   ╔═════════════════════════════════════════════╗
  H-AI      ║  WAVE                                       ║
  SESSION   ║  How to collaborate with AI in a session    ║
            ╚═════════════════════════════════════════════╝
```

WAVE doesn't compete with traditional methodologies — it operates at a level none of them cover. You can run a project in PRINCE2, organise work in Scrum, apply Lean — and simultaneously use WAVE for every AI session.

| Aspect | Traditional methodologies | WAVE | Relationship |
|---|---|---|---|
| Preparation | Documentation for humans | Documentation as FUEL for AI | Shared value, different motivation |
| Iteration | Scrum: sprints | PULSE: 3 rounds per area | Shared principle, different rhythm |
| Waste elimination | Lean: optimise flow | Preparation eliminates rework | Shared goal, different mechanism |
| **AI as partner** | **None — didn't exist** | **Core of the methodology** | **Unique to WAVE** |
| **DooR** | **No equivalent** | **Readiness standards** | **Unique** |
| **Living Patterns** | **No equivalent** | **Living knowledge base** | **Unique** |

The closest historical precedent comes from manufacturing. **Lean** started as the Toyota Production System, focused on car production. Over time its principles proved universal. WAVE addresses a fundamentally different and more pressing problem: **how should humans collaborate with AI so that AI amplifies them rather than replaces them.**

---

## 11. How to start

### The fast path — starting today

Choose one task you regularly perform with AI. Before your next attempt:

1. Write down everything you know about this task — context, constraints, what a good result looks like, what mistakes to avoid.
2. Organise it into a simple document: Vision → Requirements → Context → Success criteria.
3. Use this document as the foundation for your next AI interaction.

Observe the difference. If first-try accuracy improves — you've just experienced the core of WAVE.

### The full path — week by week

| Week | What you do | Effect |
|:---:|---|---|
| 1 | DataPrep for one task — write context, organise | PSR rises from ~60% to ~70% |
| 2 | Structured prompts (7 elements from Prompt2Data) | Fewer iterations, better results |
| 3 | Meta-prompt templates for repeating task types | New tasks = filling fields, not writing from scratch |
| 4 | Run SCAN for your project | Terrain map — you know what to investigate |
| 5-6 | PULSE for the most important areas | First Living Patterns |
| 7-8 | Measure PSR, DPC, TFCO. Improve DataPrep and templates | Methodology starts self-improving |

### The team path

In a team, DataPrep becomes a shared knowledge base, meta-prompts become team standards, Living Patterns become decision references that every team member opens before making decisions in their area. The Decision Log is the backbone — not in three people's heads, but in one place.

---

## 12. Frequently asked questions

**Does WAVE only work for software development?**

No. WAVE originated in a software environment and has its deepest case study there. But the axioms, three H-AI levels, DooR, AANP, and Living Patterns contain nothing specific to any industry. Chapter 9 outlines six additional domains.

**Do I need to be technical?**

No. DataPrep is about organising YOUR expertise — whatever that expertise may be. A teacher's DataPrep looks different from an engineer's, but the principle is the same.

**How does WAVE differ from "writing good prompts"?**

Prompt engineering is a technique — like knowing how to use a hammer. WAVE is a methodology — like having a construction plan. Good prompts are part of WAVE (Prompt2Data), but embedded in a larger system of preparation (DataPrep), meta-steering (Prompt2Prompt), readiness standards (DooR), completeness testing (AANP), and product profiles (Discovery/Build/Scale).

**Which AI tools does WAVE work with?**

WAVE is tool-agnostic. It works with any AI that accepts structured input — Claude, ChatGPT, Gemini, Copilot, domain-specific models, or future tools that don't exist yet.

**How quickly will I see results?**

Most practitioners notice improved first-try accuracy within the first week of disciplined DataPrep. Significant overall improvement (3-5x) typically appears between weeks four and eight, as templates mature and DataPrep coverage deepens.

**Can a team use WAVE?**

Yes. In a team, DataPrep becomes shared knowledge, meta-prompts become team standards, Living Patterns become decision references, and metrics become collaboration quality measures. The principles scale.

**What's new in v2.0 compared to v1.0?**

V2.0 adds: three-layer architecture (philosophy → components → practices), DooR (readiness standards), Living Patterns (SCAN, PULSE — knowledge-building tools), FALA (concept-to-execution procedure), AANP (process completeness test), Product Profiles (Discovery/Build/Scale), gravitational interpretation of the 70/30 rule, Quick Start. V1.0 remains available in the repository as an entry point.

**Is WAVE free?**

Yes. CC BY-SA 4.0 — you may use, adapt, teach, and extend it, provided you attribute authorship and share adaptations under the same license.

---

## 13. Origin story

WAVE was born on January 17, 2026, during a working session between Przemysław Zieliński and Claude (Anthropic). Zieliński — co-founder and CEO of IDareU, a gamified learning platform built around video challenges with mentoring — needed a structured approach to building a complex web application with AI support.

The three-layer structure — DataPrep, Prompt2Data, Prompt2Prompt — emerged from practical necessity: the discovery that most value in AI collaboration comes from what the human prepares BEFORE AI is engaged.

In February 2026, WAVE was published as open-source (v1.0) with generic positioning from day one — learning from Lean's costly mistake of starting with the "Manufacturing" label, which took decades to shed.

Between February and March 2026, while building IDareU Gen2 in practice, concepts emerged that fundamentally expanded WAVE's architecture: DooR (readiness standards), Living Patterns (a living knowledge ecosystem with SCAN and PULSE tools), FALA (concept-to-code pipeline), RtS (11 layers of technical specification), AANP (process completeness test), Product Profiles (Discovery/Build/Scale). V2.0 is the result of that evolution — from a loose collection of principles to a structured methodology with three architectural layers.

In March 2026, the WAVE Living Patterns method passed a repeatability test — two independent sessions arrived at the same foundations with different profiles. From that test, Cross-Session Merge emerged as a new self-improvement variant, and a semi-automated pipeline on GitHub Actions confirmed the approach's scalability — the cost of a single Living Pattern dropped below one dollar, with approval gates between every step.

That same month, during a late-night session on the Living Patterns pipeline, the meta-axiom **Currents and Tensions** emerged — the observation that every human-AI collaboration session plays out on a field of competing attributes, and that emergence is born at their intersection. Rolling back four iterations of table repair in favor of simplicity and capacity reserve turned out to be the moment where navigating a tension produced a discovery worth more than the repaired table. Carl Benedikt Frey of Oxford confirmed this observation at the scale of a thousand years of history: progress dies when systems freeze into a single mode instead of navigating tensions.

---

## 14. Citation and license

### License

WAVE is published under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.

### Citation

```
Zieliński, P. (2026). WAVE: Workflow Amplification via Vectored Expertise — 
A Human-AI Collaboration Methodology (v2.0). 
https://github.com/przemek-zielinski/WAVE-Methodology
```

### Contributing

WAVE is version 2.0 — born in software engineering, designed for every domain. It grows through practitioners who test it, break it, and improve it.

Case studies, templates, translations, criticism — see [CONTRIBUTING.md](../CONTRIBUTING.md).

We're looking for **co-maintainers** who are passionate about human-AI collaboration and want to help this methodology reach its potential.

---

*WAVE Methodology v2.0 — Published March 2026*  
*Created by Przemysław Zieliński with Claude (Anthropic)*  
*"The human leads. AI amplifies."*
