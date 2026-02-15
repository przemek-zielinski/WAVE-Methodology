# WAVE for Software Engineering

## Workflow Amplification via Vectored Expertise — Applied to Software Development

### The First and Deepest Case Study

**Version:** 1.0  
**Date:** February 15, 2026  
**Author:** Przemysław Zieliński  
**With:** Claude (Anthropic)  
**License:** CC BY-SA 4.0  
**Prerequisite:** [WAVE Methodology (Generic Core)](WAVE_Methodology_v1.0_EN.md)

---

## Contents

1. [Why Software Engineering First](#1-why-software-engineering-first)
2. [The Problem Every Developer Knows](#2-the-problem-every-developer-knows)
3. [Three Layers in Code](#3-three-layers-in-code)
4. [Operational Model — Tools, Engines, Daily Rhythm](#4-operational-model)
5. [Before and After — Concrete Examples](#5-before-and-after)
6. [Metrics From the Field](#6-metrics-from-the-field)
7. [How WAVE Differs From Existing Approaches](#7-how-wave-differs-from-existing-approaches)
8. [Getting Started for Developers](#8-getting-started-for-developers)
9. [Common Pitfalls](#9-common-pitfalls)
10. [Future Directions](#10-future-directions)

---

## 1. Why Software Engineering First

Software engineering is the natural proving ground for a human-AI collaboration methodology. Developers were among the first professionals to adopt AI as a daily tool — through code generators, pair-programming assistants, and agentic coding environments. The feedback loops are fast: you write a prompt, get code, run it, and immediately know if it works.

This makes software the ideal domain for validating WAVE's core claims:

- That 70% preparation and 30% execution outperforms chaotic prompting.
- That three layers (DataPrep, Prompt2Data, Prompt2Prompt) create a self-improving system.
- That metrics like PSR and TFCO can be tracked and improved.

Everything in this document was tested during the real-world construction of a complex web platform (IDareU V2) by a solo developer working with AI. The numbers, examples, and workflows below come from that experience.

If you have not read the generic WAVE core document, start there. It explains the philosophy, principles, and cross-domain applicability. This document assumes you understand the three layers and focuses on how they translate into code, prompts, templates, and daily practice.

---

## 2. The Problem Every Developer Knows

You sit down to build a feature. You open your AI assistant and type:

```
"Build me a user authentication system with email/password, 
OAuth, and 2FA support"
```

AI generates code. You run it. Half the functions are missing. The naming conventions do not match your project. The error handling is inconsistent. The types are wrong.

You correct. AI regenerates. Better, but the session management conflicts with your existing JWT setup. You explain the conflict. AI fixes one thing, breaks another. Three hours and ten iterations later, you have code that works — but is fragile, inconsistent with your codebase, and undocumented.

This is not a failure of AI capability. Modern AI models can write excellent code. The failure is in the collaboration pattern: **the developer did not give AI what it needed to succeed on the first try.**

WAVE solves this by inverting the time allocation. Instead of spending 10% thinking and 90% iterating, you spend 70% preparing and 30% executing. The result: first-attempt success rates above 80%, revision rates below 1.5, and development time reduced by 25-33%.

---

## 3. Three Layers in Code

### Layer 1: DataPrep for Software

In software, DataPrep is the hierarchy of documents that describe your project from vision down to individual function specifications. Each document generates the next.

```
Level 1.1: Product Vision
  "Gamified learning platform — three-sided marketplace"
    ↓ generates
Level 1.2: Business Requirements
  "User authentication, challenge creation, video upload, 
   payment processing, gamification system..."
    ↓ generates
Level 1.3: Architecture
  "Next.js + TypeScript + Tailwind + Supabase, 
   monorepo structure, API routes, RLS policies..."
    ↓ generates
Level 1.4: Component Specifications
  "AuthService: email/password + OAuth + 2FA
   ChallengeService: CRUD + video attachment + scoring
   PaymentService: IdUShare revenue split model..."
    ↓ generates
Level 1.5: Function-Level Specs
  "validateEmail(): input string, output ValidationResult,
   RFC 5322 compliant, disposable domain check..."
```

**Key principle:** completeness at each level matters more than depth at any single level. AI can generate a complete function from a complete component spec. It cannot generate a complete component from a fragment of the architecture.

**What goes into a software DataPrep:**

| Document                 | Contents                                                     | Creates basis for            |
| ------------------------ | ------------------------------------------------------------ | ---------------------------- |
| Product Vision           | Mission, value proposition, target users                     | Business requirements        |
| Business Requirements    | Functional and non-functional requirements, prioritized (MoSCoW) | Architecture decisions       |
| Architecture Document    | Tech stack, system diagram, data flow, security model        | Component specs              |
| Component Specifications | Each module: inputs, outputs, interfaces, dependencies       | Function specs, prompts      |
| Style Guide              | Naming conventions, error handling patterns, code organization | Every prompt                 |
| Data Model               | Entity relationships, field types, indexes, constraints      | Backend prompts              |
| API Contracts            | Endpoints, request/response formats, auth requirements       | Frontend and backend prompts |
| Test Strategy            | Coverage goals, test types, edge case categories             | Test prompts                 |

**Practical advice:** You do not need all of these on day one. Start with Vision + Architecture + Style Guide. These three documents alone will dramatically improve your prompt success rate, because they give AI the three things it needs most: what you are building, how it is structured, and what conventions to follow.

### Layer 2: Prompt2Data for Software

A WAVE prompt for code generation is not a request — it is a contract. It tells AI exactly what to build, with what constraints, in what format, and how success will be judged.

**Anatomy of a WAVE code prompt:**

```markdown
## Context (from DataPrep)
Project: IDareU V2 — gamified learning platform
Stack: Next.js 14, TypeScript strict, Tailwind CSS, Supabase
Location: /lib/services/auth/emailAuth.ts
Related: See AuthService component spec [link]

## Task
Generate the EmailAuthProvider class implementing email/password 
authentication with bcrypt hashing and JWT session management.

## Constraints
- TypeScript strict mode, no `any` types
- No external auth libraries (Supabase handles OAuth separately)
- Error messages as i18n-ready codes, not hardcoded strings
- All async operations with try/catch
- Logging via Winston logger (already configured)

## Input Data
- User table schema: [from Data Model]
- JWT config: secret from env, 24h expiry, refresh token 7d
- Rate limiting: 5 attempts per 15 minutes per IP
- Password policy: min 8 chars, 1 uppercase, 1 number

## Expected Output
- Complete TypeScript class with all methods
- Methods: register(), login(), resetPassword(), verifyEmail()
- Each method returns typed Result<T, AuthError>
- Private helper methods prefixed with _

## Success Criteria
- Compiles with zero TypeScript errors
- Follows project naming conventions
- Handles all edge cases listed below
- Ready for unit testing (dependency injection for Supabase client)

## Edge Cases
- Email already registered → DUPLICATE_EMAIL error
- Invalid password format → PASSWORD_POLICY_VIOLATION
- Account locked after 5 failed attempts → ACCOUNT_LOCKED
- Expired verification token → TOKEN_EXPIRED
- Database connection failure → graceful degradation
```

**Result:** AI generates a complete, correct, testable class on the first attempt — because it has everything it needs. No guessing, no hallucinating method names, no inventing conventions.

### Layer 3: Prompt2Prompt for Software

Meta-prompts are templates that define how to create prompts for recurring types of tasks. In software, the most common types are:

**Code Generation Meta-Prompt** — for writing new functions, components, and services.

**Code Review Meta-Prompt** — for requesting architectural and quality reviews.

**Bug Investigation Meta-Prompt** — for analyzing failures with full context.

**Refactoring Meta-Prompt** — for restructuring existing code.

**Test Writing Meta-Prompt** — for generating test suites from specifications.

**Documentation Meta-Prompt** — for generating technical docs from code.

**Architecture Analysis Meta-Prompt** — for evaluating design decisions.

Each meta-prompt contains:

- **When to use it** (trigger conditions)
- **What DataPrep to include** (which documents from Layer 1)
- **Prompt structure** (sections, order, required fields)
- **Quality checklist** (verify before sending)
- **Common pitfalls** (what usually goes wrong with this task type)

**Example: Code Generation Meta-Prompt (simplified)**

```markdown
# Meta-Prompt: Code Generation

## Trigger: Writing any new function, component, or service

## Required DataPrep:
- [ ] Architecture doc (for stack and patterns)
- [ ] Component spec (for this module)
- [ ] Style guide (for conventions)
- [ ] Data model (if touching database)

## Prompt Structure:
1. Context — project, stack, file location, related modules
2. Task — "Generate [TYPE] that [ACTION] for [PURPOSE]"
3. Constraints — language version, libraries, style rules
4. Input data — types, schemas, configs from DataPrep
5. Expected output — format, methods, return types
6. Success criteria — what "correct" means
7. Edge cases — minimum 3 (happy, boundary, error)

## Quality Check Before Sending:
- [ ] Task is singular and specific (not "build the whole module")
- [ ] All types and interfaces referenced actually exist in DataPrep
- [ ] Constraints do not contradict each other
- [ ] Edge cases cover security-relevant scenarios
- [ ] Expected output is precise enough to verify programmatically

## Common Pitfalls:
- Forgetting to include the style guide → inconsistent naming
- Asking for too much in one prompt → fragmented output
- Not specifying error handling approach → AI invents its own
- Missing dependency injection requirement → untestable code
```

**The power:** once this meta-prompt is validated through 10-20 uses, every new code generation task becomes a fill-in-the-blanks exercise. The thinking has been done. Quality is baked in. Execution is fast and consistent.

Meta-prompts evolve. After 50 uses, you add a "Common Pitfalls" section based on patterns you noticed. After 100 uses, you restructure the template entirely. This is WAVE's recursive improvement in action — the methodology gets better the more you use it.

---

## 4. Operational Model

WAVE for software is not just three layers on paper. It includes a concrete operational model — which AI tools to use, when, and how to organize your workday.

### Tool Selection Matrix

Modern AI platforms offer multiple interfaces. WAVE assigns each to its optimal role:

| What you are doing                        | AI Engine           | Interface          | Why                                               |
| ----------------------------------------- | ------------------- | ------------------ | ------------------------------------------------- |
| Architecture, strategy, synthesis         | Most capable model  | Chat               | Deep reasoning, sees the whole picture            |
| Daily coding (components, modules)        | Fast reliable model | Code agent         | Speed, consistency, does not drain resources      |
| Complex coding (scaffolding, refactoring) | Most capable model  | Code agent         | Fewer iterations, better first attempt            |
| File processing, audits, reports          | Most capable model  | Autonomous agent   | Multi-file work without manual steering           |
| Web research, trends                      | Fast model          | Chat with search   | Search capability does not require deep reasoning |
| Documentation from code                   | Fast model          | Code agent or Chat | Generates from existing code, straightforward     |

### Three Rules of Thumb

**Rule 1: "Thinking or Doing?"**
If the task requires thinking (analysis, architecture, decisions) → use the most capable model. If the task requires doing (implementing a spec, formatting, routine code) → use the fast model.

**Rule 2: "How many files at once?"**
1-3 files, simple processing → fast model, Chat. 5+ files, synthesis or comparison → capable model, Chat or autonomous agent. Entire folder reorganization → capable model, autonomous agent.

**Rule 3: "First time or repeat?"**
Doing something for the first time (new architecture, new module, new pattern) → most capable model. Repeating a validated pattern (another component from template, another test) → fast model.

**Bonus rule for code agents:** If you expect more than two "fix this" iterations — start with the most capable model. Three iterations on the fast model consume more resources than one shot from the capable model.

### Daily Rhythm

A typical WAVE development day has three phases:

**Morning — Strategy (capable model, Chat, 2-3 hours)**
Review yesterday's progress. Plan today's tasks. Resolve architectural questions that emerged. Create or update DataPrep documents. This is the 70% — the preparation that makes the afternoon productive.

**Afternoon — Execution (fast model, Code agent, 4-6 hours)**
Implement features from morning specifications. Use meta-prompt templates. Pass structured prompts to AI. Review output, merge, move to next task. This is the 30% — fast, focused, low-stress.

**Evening — Reflection (capable model, Chat, 30-60 minutes)**
Summarize the day. Update meta-prompts based on what worked and what did not. Prepare DataPrep for tomorrow. Track metrics.

**The effect:** 5-6 hours of highly productive work instead of 8-10 hours of chaotic coding. Lower cognitive load. Higher code quality. Better documentation (because documentation is a byproduct of DataPrep, not an afterthought).

---

## 5. Before and After

### Example: User Authentication System

**Without WAVE (traditional approach):**

```
Developer: "Build a user auth system with email, OAuth, and 2FA"

AI generates code → Missing error handling
Developer: "Add error handling"
AI regenerates → Naming conventions wrong  
Developer: "Use camelCase, follow our style guide"
AI fixes naming → JWT config conflicts with existing setup
Developer: "Here's our JWT config, please adjust"
AI adjusts → 2FA implementation incomplete
Developer: "Complete the 2FA flow"
AI completes → Tests missing
Developer: "Write tests"
AI writes tests → Tests don't match implementation
...

Result: 8-10 iterations, 4+ hours, inconsistent code, 
fragile test suite, no documentation, high stress.
```

**With WAVE:**

```
Step 1: DataPrep (prepared in morning strategy session)
- Architecture doc: stack, patterns, JWT config
- Component spec: AuthService — all methods, types, interfaces
- Style guide: naming, error handling, logging
- Data model: User table schema, session table

Step 2: Prompt (built from Code Generation Meta-Prompt)
- Full context from DataPrep
- Single task: EmailAuthProvider class
- All constraints, edge cases, success criteria

Step 3: Execute
AI generates complete class → compiles, passes lint, 
handles all edge cases, follows conventions.

Step 4: Review & merge
One review pass. Minor adjustment to error message format.
Merge.

Result: 1 iteration, 45 minutes (including DataPrep time), 
consistent code, testable, documented, low stress.
```

### Example: Feature Flag Service

**Without WAVE:**

```
"Write a feature flag service" → 6 iterations, 3 hours
```

**WAVE Prompt (using prepared DataPrep):**

```markdown
## Context
Project: [from Architecture Doc]
Feature flags needed for gradual rollout of gamification 
features in IDareU V2. Flags stored in Supabase with 
Redis cache for performance.

## Task
Generate FeatureFlagService class with methods:
- isEnabled(flagName, userId?): Check if flag is active
- getAllFlags(): Return all flags with usage stats
- createFlag(data): Create new flag
- updateFlag(name, data): Update flag config
- deleteFlag(name): Soft-delete flag

## Constraints
- [Style Guide]: async/await, try/catch, Winston logger
- [Data Model]: feature_flags table schema attached
- Cache strategy: Redis with 5-minute TTL, fail-safe to DB
- [Security]: Admin-only for create/update/delete

## Edge Cases
- Flag does not exist → return false (fail-safe)
- User not authenticated → return default state
- Database error → use cached value or fail-safe
- Redis unavailable → continue without cache (slower)

## Success Criteria
- Complete TypeScript class, all methods typed
- Dependency injection for Supabase and Redis clients
- Ready for unit testing
- Follows existing service patterns in codebase
```

**Result:** Complete, correct service on first attempt. DataPrep time: already done (architecture and data model existed). Prompt creation: 15 minutes (using meta-prompt template). AI execution: 2 minutes. Review: 10 minutes. Total: 27 minutes.

---

## 6. Metrics From the Field

These metrics come from a real project — building a complex web platform using WAVE over a six-week period.

### Primary Results

| Metric                          | Without WAVE                  | With WAVE        | Change |
| ------------------------------- | ----------------------------- | ---------------- | ------ |
| Development time (MVP)          | 8+ weeks (estimated)          | 6 weeks (actual) | -25%   |
| Prompt Success Rate (PSR)       | ~30%                          | ~80% (by week 4) | +167%  |
| Revisions per task              | 3-5 average                   | 0.8 average      | -78%   |
| Bug density                     | ~2.5 bugs/KLOC (industry avg) | ~0.8 bugs/KLOC   | -68%   |
| Code review time                | ~15% of dev time              | ~5% of dev time  | -67%   |
| Documentation coverage          | ~40%                          | ~95%             | +138%  |
| Developer cognitive load (1-10) | 7-8                           | 3-4              | -50%   |

### Improvement Over Time

PSR improved steadily as DataPrep deepened and meta-prompts matured:

| Week | PSR  | DataPrep Coverage | Avg Task Time | Notes                    |
| ---- | ---- | ----------------- | ------------- | ------------------------ |
| 1    | 60%  | 35%               | 3.5h          | Learning the methodology |
| 2    | 70%  | 50%               | 2.5h          | Meta-prompts established |
| 4    | 82%  | 65%               | 1.5h          | Templates working well   |
| 6    | 88%  | 78%               | 1.0h          | Near-automatic workflow  |

### ROI Calculation

For a solo developer building an MVP:

- Time saved: 2-4 weeks × opportunity cost (~€2,000/week) = **€4,000-8,000**
- Bug reduction: fewer post-launch fixes = **~€3,000-5,000 saved**
- Documentation: no separate documentation sprint needed = **€2,000 saved**
- Onboarding readiness: when team grows, new developers ramp up in 1 week instead of 3

**Estimated total value for first project: €10,000-15,000.**

The methodology pays for itself in the first project, and every subsequent project starts with mature meta-prompts and refined workflows.

---

## 7. How WAVE Differs From Existing Approaches

| Approach                                 | Focus                                      | Strength                                     | What WAVE adds                                               |
| ---------------------------------------- | ------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| **Recursive Meta Prompting (MIT, 2024)** | Self-improving prompts via category theory | Theoretical rigor, proven in reasoning tasks | DataPrep layer, practical workflow, daily rhythm, project-level structure |
| **Documentation-Driven Development**     | Docs before code                           | Forces design thinking                       | Recursive (not linear), AI as active collaborator, meta-prompt layer |
| **AI-DLC (2024)**                        | Lifecycle phases for AI development        | Structured phases                            | Specific preparation techniques, metrics, operational model with tool selection |
| **Addy Osmani's approach**               | Practical AI-assisted coding tips          | Accessible, experience-based                 | Systematic three-layer structure, reusable meta-prompts, self-improving metrics |
| **Prompt engineering courses**           | Writing better prompts                     | Technique improvement                        | Project-level context (DataPrep), reusable templates (Prompt2Prompt), continuous improvement |
| **"Vibe coding"**                        | Intuitive AI-assisted development          | Low barrier to entry                         | Structure, reproducibility, measurability, team scalability  |

WAVE does not replace these approaches. It provides the structural layer they lack — the system that connects individual techniques into a coherent, measurable, self-improving workflow.

---

## 8. Getting Started for Developers

### Day 1: Three Essential Documents

Before writing any code, create three documents:

**1. Architecture Overview (1-2 pages)**

- Tech stack with versions
- Project structure (folders, naming)
- Data flow diagram (even a rough one)
- Key architectural decisions with reasoning

**2. Style Guide (1 page)**

- Naming conventions (camelCase, PascalCase, where)
- Error handling pattern (try/catch structure, error types)
- Import organization
- Comment policy (when to comment, when not to)

**3. Data Model (as needed)**

- Entity list with key fields
- Relationships
- Constraints and indexes

These three documents alone will transform your AI interactions. Include them (or relevant excerpts) in every prompt.

### Day 2-3: First Meta-Prompt

Pick the task you do most often — probably code generation. Create a meta-prompt template:

1. What DataPrep sections to include
2. Prompt structure (Context → Task → Constraints → Input → Output → Criteria → Edge Cases)
3. Quality checklist before sending

Use this template for your next 5-10 coding tasks. Observe PSR. Refine the template.

### Day 4-7: Establish Rhythm

- Morning: update DataPrep, plan tasks, resolve questions (capable model, Chat)
- Afternoon: execute from specs using meta-prompt templates (fast model, Code agent)
- Evening: update meta-prompts, track metrics (capable model, Chat)

### Week 2+: Expand and Measure

- Create meta-prompts for other task types (review, refactoring, testing)
- Track PSR weekly — it should trend upward
- Expand DataPrep coverage as new modules are built
- Each new document enriches every future prompt

---

## 9. Common Pitfalls

**Pitfall 1: "I don't have time for DataPrep"**

This is the most common mistake — and the most expensive. Skipping DataPrep to "move faster" leads to 3-5x more iterations, inconsistent code, and technical debt that compounds. The 70% investment in preparation is not a luxury. It is the mechanism that makes the 30% execution work.

**Pitfall 2: Over-engineering DataPrep**

The opposite extreme: documenting every possible detail before writing any code. DataPrep has diminishing returns. The sweet spot is around 70-85% coverage — enough for high PSR, not so much that you are writing documentation instead of building software.

**Pitfall 3: Static meta-prompts**

Creating meta-prompts once and never updating them. Meta-prompts should evolve after every 10-20 uses. Budget 10 minutes per day for refinement. If your PSR is not improving, your meta-prompts are not evolving.

**Pitfall 4: Ignoring failures**

When a prompt fails, the instinct is to manually fix the output and move on. In WAVE, a failed prompt is a signal: either DataPrep is incomplete or the meta-prompt is flawed. Fix the root cause, not the symptom.

**Pitfall 5: Prompts that are too large**

Asking AI to build an entire module in one prompt. WAVE prompts are precise and singular — one function, one component, one service. Larger outputs come from composing smaller, validated pieces.

**Pitfall 6: No measurement**

"It feels faster" is not a metric. Track PSR, TFCO, and revision rate — even informally. You cannot improve what you do not measure.

---

## 10. Future Directions

### WAVE 2.0 for Software (2027-2028)

**Autonomous DataPrep maintenance:** AI that monitors code changes and automatically updates architecture documents, flags inconsistencies, and suggests requirement updates.

**Smart meta-prompt evolution:** AI that tracks which meta-prompts produce the highest PSR and suggests template improvements based on patterns across hundreds of uses.

**Multi-agent WAVE:** Multiple AI agents working in parallel — one on frontend, one on backend, one on tests — all drawing from the same DataPrep and coordinated by meta-prompts.

**IDE integration:** WAVE Assistant plugins for VS Code, Cursor, and other editors — surfacing relevant DataPrep when you open a file, suggesting meta-prompt templates for the task at hand, tracking metrics in real-time.

### Specializations

**WAVE for Mobile Development** — platform-specific meta-prompts for iOS/Android, DataPrep templates for app architectures, patterns for responsive design.

**WAVE for Data Engineering** — meta-prompts for pipeline construction, DataPrep for data schemas and transformation rules, quality metrics adapted for data accuracy.

**WAVE for DevOps** — meta-prompts for infrastructure-as-code, DataPrep for system configurations, runbooks generated from architecture documents.

### Community Growth

WAVE for Software Engineering has the most immediate community — millions of developers working with AI daily. The open-source repository invites contributions: new meta-prompt templates, case studies from different tech stacks, specialized DataPrep patterns for specific architectures.

If you build something with WAVE, tell the community about it. Open an Issue, submit a case study, share your metrics. Every data point makes the methodology stronger.

---

## Relationship to the Generic Core

This document describes **one application** of WAVE — the first and deepest. The generic core document ([WAVE Methodology](WAVE_Methodology_v1.0_EN.md)) describes the universal principles that apply across all domains.

Software engineering validates WAVE's claims with hard metrics and concrete examples. But the three layers, the 70/30 principle, and the bidirectional flow are not about code. They are about the relationship between human expertise and AI capability — a relationship that is the same whether you are writing software, diagnosing patients, or designing bridges.

---

*WAVE for Software Engineering v1.0 — Published February 2026*  
*Created by Przemysław Zieliński with Claude (Anthropic)*  
*"70% preparation. 30% execution. 10x the result."*
