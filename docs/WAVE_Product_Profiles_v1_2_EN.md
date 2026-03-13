# WAVE — Product Profiles
## How to Scale WAVE to the Type of Solution You're Building
### Companion Document to WAVE SE Reference v1.2 | March 2026

**Concept author:** Przemek Zieliński  
**Written by:** Claude Opus 4.6  
**License:** CC BY-SA 4.0  
**Parent document:** WAVE Software Engineering Reference v1.2

---

## Table of Contents

— Quick Start — choose your profile in 60 seconds
1. The idea — one methodology, three profiles
2. Three product profiles — overview
3. DISCOVERY profile (POC / Spike / Proof of Concept)
4. BUILD profile (MVP / Pilot / Beta)
5. SCALE profile (Product / Platform / Enterprise)
6. Profile evolution — from Discovery to Scale
7. Side-by-side comparison — time, scope, cost, quality
8. Which profile when — decision tree
9. Axioms don't scale — what's indivisible

---

## Quick Start — choose your profile in 60 seconds

Don't want to read nine chapters? Answer one question:

```
  What are you building?
  │
  ├── "I want to check if the idea makes sense"
  │    → DISCOVERY — 1 to 5 days, 2-4h preparation, 1.5-3h coding
  │    → Go to chapter 3
  │
  ├── "I have a validated idea, building the first version"
  │    → BUILD — 4 to 8 weeks, ~70h preparation, ~25h coding
  │    → Go to chapter 4
  │
  └── "I have a working MVP, scaling to a product"
       → SCALE — months, hundreds of hours of preparation and coding
       → Go to chapter 5
```

**Key principle:** Profiles are evolutionary. Discovery shifts to Build. Build to Scale. Code, documentation, and decisions grow with you — you throw nothing away.

**Not sure what to choose?** Start with DISCOVERY. Always. Even if you "feel" you need more — it's better to validate in 3 days than build for 3 months in the wrong direction.

---

## 1. The idea — one methodology, three profiles

WAVE is one methodology. There's no "WAVE Light" and "WAVE Full" — just as there's no "Lean Light" and "Lean Full." There are principles that you apply proportionally to what you're building.

A camera has one lens and one physics of light. But sometimes you're shooting a billboard — tripod, studio lighting, full resolution. And sometimes you're shooting for Instagram — phone, natural light, two seconds. The physics is the same. The scale changes.

```
  WAVE — ONE METHODOLOGY, THREE PRODUCT PROFILES

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  PHILOSOPHY (5 axioms)             ← always the same        │
  │  AANP (completeness test)          ← always applies         │
  │  DooR (transition principle)       ← always applies         │
  │  Three H-AI levels                 ← always the same rhythm │
  │                                                             │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
  │  │DISCOVERY │  │  BUILD   │  │  SCALE   │  ← scale changes │
  │  │  (POC)   │  │  (MVP)   │  │(Product) │    philosophy    │
  │  │          │  │          │  │          │    — doesn't      │
  │  └──────────┘  └──────────┘  └──────────┘                  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

Key principle: **the profile determines the scale of components, not their presence.** Every profile has SCAN, has context preparation, has verification. What differs is depth — not existence.

---

## 2. Three product profiles — overview

### Comparison table — bird's-eye view

| Dimension | DISCOVERY (POC) | BUILD (MVP) | SCALE (Product) |
|---|---|---|---|
| **Goal** | Validate idea | Deliver value | Scale and maintain |
| **Question** | "Does this make sense?" | "Do people want this?" | "Will this withstand scale?" |
| **Total time** | 1–5 days | 4–8 weeks | Months → years |
| **H-AI team** | 1 person + AI | 1–3 people + AI | Team + AI |
| **Budget** | Own time + AI subscription | Thousands € | Tens–hundreds of thousands € |
| **Code quality** | Works and demostrable | Works, secure, testable | Production, scalable, monitored |
| **Risk without WAVE** | POC can't be expanded | MVP = debt from day 1 | Spaghetti Point after 3 months |
| **P/E ratio** | ~60/40 | ~70/30 | 50-70 / 30-50 |

### The 70/30 rule as gravity

The 70/30 axiom is gravity, not command. A body always falls toward earth, but the trajectory depends on what you're building. But in ALL profiles, preparation is at least half the work — which is a radical inversion of vibe coding, where preparation equals zero.

```
  PREPARATION / EXECUTION RATIO (from hourly calculations)

  DISCOVERY:  ████████████████████████░░░░░░░░░░░░░░░░░░░  ~57/43
  BUILD:      ████████████████████████████████░░░░░░░░░░░░  ~70/30
  SCALE (small)███████████████████████████████░░░░░░░░░░░░  ~70/30
  SCALE (large)█████████████████████████░░░░░░░░░░░░░░░░░░  ~50/50
  Vibe coding:░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0/100

              ├── preparation ──┤├── execution ──┤
```

### Hourly breakdown — what makes up preparation and execution

| Activity | Discovery | Build | Scale (small) | Scale (large) |
|---|:---:|:---:|:---:|:---:|
| **PREPARATION:** | | | | |
| SCAN | 15-30 min | 2-3h | 3-5h | 3-5h |
| PULSE | 1-2h | 15-25h | 60-80h | 60-120h |
| Specifications / design | — | 10-15h | 40-60h | 40-80h |
| Decision Log | — | 3-5h | 10-15h | 10-20h |
| FALA Session 1 (audit) | — | 5-10h | 10-20h | 10-40h |
| FALA Session 2 (blueprint) | 30 min-1h | 6-15h | 30-50h | 30-100h |
| LP self-improvement | — | — | 10-15h | 10-20h |
| Context gathering | 15-30 min | included | included | included |
| **Preparation total** | **2-4h** | **41-73h** | **163-245h** | **163-385h** |
| **EXECUTION:** | | | | |
| Coding with AI | 1-2h | 9-25h | 50-100h | 50-300h |
| Tests, DoD, integration | 30 min-1h | 5-10h | 20-40h | 20-80h |
| **Execution total** | **1.5-3h** | **14-35h** | **70-140h** | **70-380h** |
| | | | | |
| **GRAND TOTAL** | **3.5-7h** | **55-108h** | **233-385h** | **233-765h** |
| **P/E RATIO** | **~57/43** | **~70/30** | **~70/30** | **~50/50** |

### Ratio visualization — time

```
  DISCOVERY        BUILD              SCALE
  ─────────        ─────              ─────

  Preparation:     Preparation:       Preparation:
  ██████░░░░       ██████████░░░░     ████████████████████░░░░░░░░░░
  2-4h             41-73h             163-385h

  Execution:       Execution:         Execution:
  ████░░░░░░       ████░░░░░░░░░░     ██████████████████████████████
  1.5-3h           14-35h             70-380h

  Documentation:   Documentation:     Documentation:
  █░░░░░░░░░       ████░░░░░░░░░░    ██████████████████████████░░░░
  1-3 files        10-20 files        50+ files

  ─────────────────────────────────────────────────────────▶
  1-5 days         4-8 weeks          months → years
```

---

## 3. DISCOVERY profile — POC / Spike / Proof of Concept

### When to use

You have an idea and want to check if it makes sense — technically, commercially, or operationally. You're not building a product. You're building proof that it's WORTH building a product. A client (internal or external) wants to see "does this even work" before investing.

### WAVE in the DISCOVERY profile

```
  DISCOVERY — flow

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  Mini-SCAN   │────▶│  PULSE lite  │────▶│  Quick code  │
  │  15 min      │     │  1 round     │     │  with context│
  │  3-5 questions│    │  1-2 areas   │     │  2-8h        │
  └──────────────┘     └──────────────┘     └──────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
   "What do I            "What pitfalls        Working
    need to know?"        in this area?"       prototype
```

### WAVE components in the DISCOVERY profile

| Component | Scale in Discovery | What you actually do |
|---|---|---|
| **SCAN** | 15 min, 3-5 areas | Answer: "what could kill this POC?" — not a full map, just the mines |
| **PULSE** | 1 round, 1-2 critical areas | Quick research: has anyone tried this? what pitfalls? |
| **Living Pattern** | v1 — core, 1-2 pages | Most important principles and critical errors — nothing more |
| **RtS** | 4 layers FULL | Data (schema), API (endpoints), Logic (algorithm), UI (screens) |
| **RtS placeholders** | 7 layers PLACEHOLDER | Security, resilience, observability — explicitly deferred |
| **FALA** | 1 session (quick blueprint → code) | No formal audit — straight to code with a mini-blueprint |
| **DoD** | 3 questions | Does it work? Can it be demoed? Can it be expanded? |
| **Decision Log** | 3-5 key decisions | Technology, architecture, scope — no more |

### What you DON'T do in Discovery

```
  ✅ YOU DO                          ❌ YOU DON'T
  ─────────                          ─────────────
  Mini-SCAN (15 min)                 Full map of 15 areas
  1 PULSE round                      3 rounds + self-improvement
  4 RtS layers                       Full 11 layers
  3 DoD questions                    Full 11-point checklist
  Quick blueprint (1-2 pages)        30+ page blueprint
  Decision Log (3-5 decisions)       Complete log with history

  BUT YOU ALWAYS DO:
  ✅ 70/30 (even if 70% = 15 minutes)
  ✅ Human understands what they're building (no vibe coding)
  ✅ Explicit placeholders (you know WHAT you're deferring)
  ✅ Structure that can be expanded (not a one-off hack)
```

### DISCOVERY with WAVE vs without WAVE

| Dimension | Without WAVE (vibe coding) | With WAVE Discovery |
|---|---|---|
| Build time | 3-8h | 3-8h (same) |
| Preparation time | 0 min | 15-30 min |
| Code quality | Works "somehow" | Works with foundations |
| Expandability | Throw away and rewrite | Expand to MVP |
| Documented decisions | 0 | 3-5 key ones |
| Known pitfalls | Discovered live | Identified upfront |
| Cost to transition to MVP | Rewrite 80% of code | Extend existing |

### The key value of DISCOVERY with WAVE

A POC without WAVE is a one-off shot. It works for the demo — and goes in the bin when it's time for the MVP. A POC with WAVE Discovery is a foundation on which you build the next floor. Those fifteen minutes of preparation save weeks of rebuilding.

---

## 4. BUILD profile — MVP / Pilot / Beta

### When to use

The idea is validated. A client (or market) said "I want this." You're building the first version that delivers real value — not a demo, not a mockup, but a working product that people actually use. You're not scaling yet — you're testing with a limited group.

### WAVE in the BUILD profile

```
  BUILD — flow

  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────┐
  │  SCAN    │──▶│  PULSE       │──▶│  Design      │──▶│  FALA    │
  │  1h      │   │  2 rounds    │   │ Specifications│  │ 2 sessions│
  │  6-8     │   │  3-5 areas   │   │ Decision Log │   │ per module│
  │ areas    │   │              │   │              │   │          │
  └──────────┘   └──────────────┘   └──────────────┘   └──────────┘
       │               │                   │                 │
       ▼               ▼                   ▼                 ▼
  Map with        Living Patterns     10-15 decisions    Code + tests
  priorities      v2 (core+verif.)    documented         + basic DoD
```

### WAVE components in the BUILD profile

| Component | Scale in Build | What you actually do |
|---|---|---|
| **SCAN** | 1h, 6-8 areas | Fuller map — include security, testing, infrastructure |
| **PULSE** | 2 rounds, 3-5 areas | Core + failure verification (Round 2) |
| **Living Pattern** | v2 — core + verification | Principles + error matrix + key metrics |
| **RtS** | 8 layers FULL | Data, API, Logic, States, Integrations, UI, Tests, Meta |
| **RtS placeholders** | 3 layers PLACEHOLDER | Basic security, resilience and observability — simplified |
| **FALA** | 2 sessions (audit + code) | Light audit (Gap Map without full graph) + coding |
| **DoD** | 7 points | + Basic tests + Minimal security + Deployment |
| **Decision Log** | 10-15 decisions | Architecture, stack, data model, key trade-offs |

### Financial comparison — BUILD with WAVE vs without WAVE

```
  MVP BUILD COST (rough estimates, 1-3 people + AI)
  ═══════════════════════════════════════════════════

  WITHOUT WAVE:
  Week 1-2:   Coding                      ██████████████
  Week 3-4:   Debugging                   ████████████████████
  Week 5-6:   Rebuilding (bad foundations) ██████████████████████████
  Week 7-8:   Recoding                    ██████████████
  Week 9+:    Testing and fixing          ████████████████████
                                           ─────────────────────▶
              Total cost: 8-12 weeks       Tech debt: HIGH

  WITH WAVE BUILD:
  Week 1:     SCAN + PULSE + specs        ████████████████
  Week 2-3:   FALA (audit + blueprint)    ████████████
  Week 4-6:   Coding with context         ██████████████████████
  Week 7:     Tests + DoD                 ████████
                                           ─────────────────────▶
              Total cost: 6-8 weeks        Tech debt: LOW
```

| Metric | Without WAVE | With WAVE Build | Difference |
|---|:---:|:---:|:---:|
| Time to MVP | 8-12 weeks | 6-8 weeks | -30% time |
| Components without fixes | ~40% | ~70% | +30pp quality |
| Technical debt | High (rebuild) | Low (foundations) | Qualitative shift |
| Readiness to scale | Rewrite 50-80% | Extend existing | Weeks of savings |
| Blind decisions | Many | 0 (Decision Log) | Full transparency |

---

## 5. SCALE profile — Product / Platform / Enterprise

### When to use

The MVP worked. Users are using it. Time to scale — more features, more users, more integrations, production quality. There's no room for shortcuts here — every shortcut comes back with interest.

### WAVE in the SCALE profile

```
  SCALE — full WAVE flow

  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────┐
  │  SCAN    │──▶│  PULSE       │──▶│  Design      │──▶│  FALA    │
  │  2h+     │   │  3 rounds    │   │ Full specs   │   │ 3 sessions│
  │  10-15   │   │  8-15        │   │ Decision Log │   │ per module│
  │ areas    │   │  areas       │   │ 30+ decisions│   │ per phase │
  └──────────┘   └──────────────┘   └──────────────┘   └──────────┘
       │               │                   │                 │
       ▼               ▼                   ▼                 ▼
  Full map +     Living Patterns     Complete             Production code
  sequencing     v3 + self-impr.     documentation        + 11-point DoD
```

### WAVE components in the SCALE profile

| Component | Scale in Scale | What you actually do |
|---|---|---|
| **SCAN** | 2h+, 10-15 areas | Full map with dependencies and sequencing |
| **PULSE** | 3 rounds, 8-15 areas | Complete Living Patterns with self-improvement |
| **Living Pattern** | v3 — complete | All sections: knowledge, principles, errors, decisions, metrics, sources |
| **RtS** | 11 layers FULL | Every field defined, zero "it depends" |
| **FALA** | 3 full sessions per module | Audit → Blueprint → Coding |
| **DoD** | Full 11-point checklist | Migrations, tests, flags, security, logs, metrics |
| **Decision Log** | 30+ decisions with full history | Context, rationale, rejected alternatives |

---

## 6. Profile evolution — from Discovery to Scale

The most important feature of profiles: **they are evolutionary, not replaceable.** Discovery is not a "throwaway trial" — it's the foundation on which you build Build. Build is not a "temporary MVP" — it's the base you extend into Scale.

### Evolution path — what happens to artifacts

```
  DISCOVERY                BUILD                   SCALE
  ═══════════              ═════                    ═════

  Mini-SCAN (3-5) ──────▶  Extended SCAN ──────────▶ Full SCAN
  (add areas)              (6-8 areas)               (10-15 areas)

  LP v1 (core) ──────────▶ LP v2 (+verification) ──▶ LP v3 (+finalization)
  (PULSE adds rounds)      (2 rounds)                (3 rounds + self-impr.)

  RtS 4 layers ──────────▶ RtS 8 layers ───────────▶ RtS 11 layers
  (fill placeholders)      (placeholder → full)       (zero placeholders)

  Blueprint 1-2 pp. ─────▶ Blueprint 5-10 pp. ─────▶ Blueprint 30+ pp.
  (extend, don't           (extend, don't             (complete per module)
   rewrite)                 rewrite)

  Decision Log 3-5 ──────▶ Decision Log 10-15 ────▶ Decision Log 30+
  (grows organically)      (grows organically)       (grows organically)

  POC code ──────────────▶ MVP code ───────────────▶ Production code
  (expand,                 (expand,                   (scale, don't
   don't throw away)        don't throw away)          rewrite)
```

### Cost of evolution vs cost from scratch

```
  SCENARIO A: Three separate builds (without evolution)

  POC:     █████████████████             (thrown away)
  MVP:     ████████████████████████████  (thrown away)
  Product: ████████████████████████████████████████████████
           ─────────────────────────────────────────────▶
           Total cost: 3× full build
           Total waste: ~60% (two discarded POC/MVP)

  SCENARIO B: WAVE profile evolution

  Discovery: ████████
  Build:     ────────████████████████
  Scale:     ────────────────────────████████████████████████
             ─────────────────────────────────────────────▶
             Total cost: 1× build with extensions
             Waste: ~5% (only explicit placeholders to fill)
```

| Scenario | Total time | Waste | Foundation quality |
|---|:---:|:---:|:---:|
| A: Three separate builds | 3× | ~60% discarded code | Each build from scratch |
| B: WAVE evolution | 1.4× | ~5% placeholders | Foundations from day 1 |
| **Savings B vs A** | **~55% time** | **~55pp waste** | **Architecture continuity** |

---

## 7. Side-by-side comparison — time, scope, cost, quality

### Master table — all dimensions

| Dimension | DISCOVERY | BUILD | SCALE |
|---|---|---|---|
| **Preparation time** | 2-4h | 41-73h (~1-2 weeks) | 163-385h (months) |
| **Execution time** | 1.5-3h | 14-35h (~1 week) | 70-380h (months) |
| **Total time** | 3.5-7h (1-5 days) | 55-108h (4-8 weeks) | 233-765h (3-12 months) |
| **P/E ratio** | ~57/43 | ~70/30 | 50-70 / 30-50 |
| **Budget (time + AI)** | ~0 (own time) | 5-20K € | 50-500K € |
| **First-pass quality** | ~50% without fixes | ~70% without fixes | ~85% without fixes |
| **Test coverage** | None / manual | Basic (happy path) | Full (unit + E2E) |
| **Security** | Placeholder | Basic (auth + validation) | Full (pen-test, GDPR) |
| **Documentation** | 1-3 files | 10-20 files | 50+ files |
| **Decision Log** | 3-5 decisions | 10-15 decisions | 30+ decisions |
| **Living Patterns** | 1-2 × v1 | 3-5 × v2 | 8-15 × v3 |
| **RtS** | 4 full layers | 8 full layers | 11 full layers |
| **DoD** | 3 questions | 7 points | 11 points |
| **Expandability** | To MVP without rebuild | To product without rebuild | To enterprise platform |
| **Technical debt** | Explicit (placeholders) | Low | Minimal |

### Diagram — quality over time

```
  Code
  quality
    │
 95%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·  SCALE with WAVE
    │                                            · ·
 85%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · ·
    │                              · · ·
 70%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · · ·                       BUILD with WAVE
    │                · · ·
 50%├─ ─ ─ ─ · · · ·                                     DISCOVERY with WAVE
    │    · · ·
    │  · ·
    │ · ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─          Without WAVE
 30%├ ·     · · · · · · · · ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · ·   (plateau + decline)
    │              ↑ "Spaghetti Point"           · ·
 20%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·
    │
    ├──────────┬──────────┬──────────┬──────────┬─────▶ Time
    0       1 month    3 months   6 months   12 months
```

---

## 8. Which profile when — decision tree

```
  START: You have an idea for a solution
  │
  ├── Do you know if the idea makes sense technically?
  │   │
  │   ├── NO ──────────────▶ DISCOVERY
  │   │                       "Build proof in 1-5 days"
  │   │
  │   └── YES
  │       │
  │       ├── Do you have users / clients ready to test?
  │       │   │
  │       │   ├── NO ──────▶ DISCOVERY
  │       │   │               "Validate with the market, not in your head"
  │       │   │
  │       │   └── YES
  │       │       │
  │       │       ├── Does the solution need to serve >100 users?
  │       │       │   │
  │       │       │   ├── NO ──▶ BUILD
  │       │       │   │           "MVP for a limited group"
  │       │       │   │
  │       │       │   └── YES
  │       │       │       │
  │       │       │       ├── Do you have budget and time for months of work?
  │       │       │       │   │
  │       │       │       │   ├── NO ──▶ BUILD (then SCALE)
  │       │       │       │   │           "Start with MVP, evolve"
  │       │       │       │   │
  │       │       │       │   └── YES ──▶ SCALE
  │       │       │       │               "Build the target product"
```

### Three rules for choosing a profile

| Rule | Description |
|---|---|
| **Validate before you build** | If you don't know if the idea makes sense — DISCOVERY. Always. Even if you "feel" it does. |
| **Evolve instead of rewriting** | Start with Discovery, shift to Build when the idea confirms, then Scale. Don't build Scale from day one. |
| **A profile isn't a sentence** | You can change profile mid-stream. Discovery turned out bigger than expected? Shift to Build. Build doesn't need Scale? Stay in Build. |

---

## 9. Axioms don't scale — what's indivisible

The profile changes the scale of components. But there's a set of elements that NEVER change — regardless of profile. They are indivisible, like an atom (in the original sense of the word).

### What stays constant across all profiles

```
  INDIVISIBLE (identical in Discovery, Build, and Scale):
  ════════════════════════════════════════════════════════

  ✅ The 70/30 rule as GRAVITY
     The ratio gravitates toward 70/30 — in Discovery it lands at ~60/40,
     in Build at ~70/30, in large Scale at ~50/50.
     But ALWAYS preparation ≥ 50%. Zero "vibe coding."

  ✅ Human leads, AI amplifies
     Even in a POC — you understand what you're building, no vibe coding

  ✅ Build completely, activate progressively
     Even a POC has structure that can be expanded

  ✅ Explicit placeholders
     You know WHAT you're deferring (not "we forgot," but "consciously later")

  ✅ AANP test
     Every process has an Actor, Action, Tool, Product

  ✅ DooR principle
     Transition between stages = artifact completeness
     (even if the artifact is a 2-page blueprint)

  ✅ Decision Log
     Even 3 decisions are a Decision Log, not "I remember in my head"

  ✅ Three H-AI levels
     DataPrep → Prompt2Data → Prompt2Prompt
     Even in Discovery: gather context → give task → evaluate result
```

### What scales

| Element | Discovery | Build | Scale |
|---|:---:|:---:|:---:|
| Number of SCAN areas | 3-5 | 6-8 | 10-15 |
| PULSE rounds | 1 | 2 | 3 |
| Living Pattern version | v1 | v2 | v3 |
| Full RtS layers | 4 | 8 | 11 |
| FALA sessions | 1 | 2 | 3 |
| DoD points | 3 | 7 | 11 |
| Decision Log entries | 3-5 | 10-15 | 30+ |
| Documentation depth | Minimal | Moderate | Complete |

---

*Document created: March 11, 2026*  
*Version: 1.2*  
*Concept author: Przemek Zieliński*  
*Written by: Claude Opus 4.6*  
*License: CC BY-SA 4.0*  
*Companion document to: WAVE Software Engineering Reference v1.2*
