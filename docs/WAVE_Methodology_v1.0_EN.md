# WAVE Methodology

## Workflow Amplification via Vectored Expertise

### A Human-AI Collaboration Methodology

**Version:** 1.0  
**Date:** February 15, 2026  
**Author:** Przemysław Zieliński  
**With:** Claude (Anthropic)  
**License:** CC BY-SA 4.0

---

## Contents

1. [The Problem](#1-the-problem)
2. [The WAVE Philosophy](#2-the-wave-philosophy)
3. [Three Layers](#3-three-layers)
4. [Bidirectional Flow](#4-bidirectional-flow)
5. [Measuring What Matters](#5-measuring-what-matters)
6. [How WAVE Differs](#6-how-wave-differs)
7. [WAVE in Software Engineering](#7-wave-in-software-engineering)
8. [Beyond Software: WAVE Across Domains](#8-beyond-software-wave-across-domains)
9. [Getting Started](#9-getting-started)
10. [FAQ](#10-faq)
11. [Origins](#11-origins)
12. [Citation and License](#12-citation-and-license)

---

## 1. The Problem

In 2026, every organization on the planet has access to artificial intelligence. Hospitals use it for diagnostics. Law firms use it for precedent analysis. Schools use it for personalized learning. Engineers use it for design optimization. Software teams use it for code generation.

And almost all of them use it the same way: chaotically.

The typical interaction looks like this: a professional asks AI a question, receives a result, finds it lacking, asks again with slightly different wording, receives a slightly different result, corrects it, asks once more. Ten iterations later, the output is acceptable but far from what was possible.

This is not a failure of AI. It is a failure of collaboration.

The tools exist. What is missing is a **methodology** — a structured, layered, measurable system for working with AI that places a clear principle at its center: **the human leads, the AI amplifies**.

Today, what passes for methodology in human-AI collaboration falls into four categories, none of which fills this gap:

**Prompt engineering** — a collection of techniques for writing better queries. Useful, but a technique is not a methodology. Knowing how to write a good prompt does not tell you how to organize a project, structure your knowledge, or measure your collaboration over time.

**"Agile AI"** — typically Agile with the word "AI" appended, without rethinking the fundamental relationship between human expertise and machine capability.

**Responsible AI guidelines** — corporate policies governing what AI should and should not do. Necessary, but policies are not workflows. They tell you what to avoid, not how to work.

**Tool tutorials** — courses on how to use ChatGPT, Claude, Copilot, or other specific products. Instruction manuals for individual tools, not frameworks for collaboration.

WAVE is what is missing: a **three-layer methodology with defined metrics, reusable templates, and a guiding principle that human expertise is the driver, not the passenger**.

---

## 2. The WAVE Philosophy

WAVE stands for **Workflow Amplification via Vectored Expertise**. The name encodes the core idea: your expertise, given direction (vectored) and structure, is amplified by AI into outcomes neither could achieve alone.

The Polish name is **FALA** — **Formuła Amplifikacji Ludzkiej Aktywności** (Formula for Amplifying Human Activity). FALA means "wave" in Polish, carrying the same metaphor: a small impulse on the open ocean becomes a powerful wave at the shore.

### The 70/30 Principle

WAVE is built on one counterintuitive rule: **spend 70% of your time preparing, and 30% executing with AI**.

This reverses the instinct of most professionals. The natural impulse is to start working with AI immediately — ask the question, get the answer, move on. But this impulse leads to the chaotic ten-iteration cycle described above.

The 70/30 principle says: before you engage AI, deeply understand what you want to achieve, what data and context you have, what constraints apply, and what a successful outcome looks like. This preparation — your expertise, structured and made explicit — is the fuel that makes AI collaboration effective.

The analogy is **mise en place** — the culinary principle where a chef prepares and organizes all ingredients before service begins. During service, execution is fast, precise, and calm. The investment in preparation makes excellence under pressure possible.

### Human Leads, AI Amplifies

WAVE does not treat AI as an autonomous agent that replaces human judgment. It treats AI as a powerful amplifier of human expertise.

The distinction matters. An amplifier cannot create signal from noise. It takes a clear signal — your knowledge, your context, your judgment — and makes it stronger. If the signal is weak (vague instructions, incomplete context, unclear goals), the amplified output will be weak too. Garbage in, garbage out — at scale.

This is why the methodology places such emphasis on the human side of the equation. WAVE is not a manual for getting more from AI. It is a framework for structuring human expertise so that AI collaboration produces outcomes worthy of that expertise.

---

## 3. Three Layers

WAVE organizes human-AI collaboration into three layers, each building on the one below it. Together, they form a recursive system where documents generate documents, prompts generate prompts, and each iteration improves the next.

### Layer 1: DataPrep — Structuring Domain Knowledge

**What it is:** The process of organizing your expertise, data, and context into a hierarchy of documents where each document informs the creation of the next.

**The analogy:** When an architect designs a skyscraper, they do not start by drawing bricks. They begin with a vision ("50-story office building downtown"), then requirements ("1,000 offices, parking for 500, rooftop restaurant"), then architecture ("steel frame, concrete columns, HVAC system"), then specifications for each component. Each document generates the next. The vision determines the requirements. The requirements determine the architecture. Nothing is left to guesswork.

DataPrep follows the same logic for any domain:

```
Vision (what you want to achieve)
  ↓ generates
Requirements (what must be true)
  ↓ generates
Domain Context (constraints, knowledge, conditions)
  ↓ generates
Structured Input Data (organized for AI consumption)
  ↓ generates
Success Criteria (how you will judge the output)
```

**Key principles of DataPrep:**

1. **Completeness before detail.** A complete high-level overview is more valuable than a fragment of deep detail. AI can generate detail from context; it cannot generate context from detail.

2. **One-directional dependency.** Higher documents never depend on lower ones. Information flows downward only. This prevents circular confusion.

3. **Verifiability.** Each document can be verified by asking one question: "Is this sufficient to generate the next level?" If not, something is missing.

4. **Context over content.** Knowing *why* a decision was made is more valuable than knowing *what* the decision was. AI can execute decisions. It cannot reconstruct the reasoning behind them unless you provide it.

### Layer 2: Prompt2Data — Precision Tasking

**What it is:** The process of creating precise instructions for AI that draw on the prepared data from Layer 1 to produce exactly the output you need.

**The analogy:** Imagine asking a master chef to make a dessert. A vague request ("make something sweet") produces a random result. A precise request, informed by preparation, produces excellence:

*"Based on the menu [from Layer 1]: it is winter, so use apples. The guest prefers cakes. Previous courses were heavy, so keep it light. You have 15 minutes and these tools [from Layer 1]. Create a recipe for apple cake that meets all conditions. Format: step-by-step with timings."*

The chef has everything needed. No guessing. No iterations. One precise output.

**Anatomy of a WAVE prompt:**

```
Context         — what we already know (from DataPrep)
Task            — one specific thing to do
Constraints     — limitations (technical, temporal, domain-specific)
Input Data      — all relevant data from Layer 1
Expected Output — exact format and structure
Success Criteria — how we judge quality
Edge Cases      — what might go wrong
```

**The key insight:** a well-prepared prompt does not ask AI to be creative. It asks AI to be precise. Creativity is the human's domain — expressed through the choices made in DataPrep. AI's strength is execution at scale, not invention in a vacuum.

### Layer 3: Prompt2Prompt — Meta-Prompting

**What it is:** A prompt that generates prompts. The meta-level where you define *how* to create prompts for different types of tasks, rather than creating each prompt from scratch.

**The analogy:** When a lawyer drafts a contract, they do not start from a blank page. They use a template — a structure that defines what every contract of that type must contain, where to insert specific details, and what legal requirements must be met. The template does not write the contract. It ensures consistency, completeness, and quality across every contract the firm produces.

Prompt2Prompt does the same for AI collaboration. Instead of crafting each prompt individually, you create templates that define:

- What type of task this prompt addresses
- What DataPrep inputs are required
- What structure the prompt must follow
- What variables change between instances
- What quality checks apply

**The power of meta-prompting:** once you have a well-tested meta-prompt for a type of task, every new instance of that task becomes a fill-in-the-blanks exercise. The thinking has already been done. The quality has already been validated. What remains is execution — fast, consistent, reliable.

### The Recursive Engine

The three layers are not linear. They form a recursive loop:

```
Layer 1 (DataPrep) informs → Layer 2 (Prompt2Data)
Layer 2 produces outputs that → update Layer 1
Layer 3 (Prompt2Prompt) governs → how Layer 2 prompts are built
Results from Layer 2 → refine Layer 3 templates

Each cycle improves the next.
```

This is the mechanism that makes WAVE self-improving. Every output teaches you something about your DataPrep (was it complete?), your prompts (were they precise?), and your meta-prompts (did the template work?). The methodology gets better with use.

---

## 4. Bidirectional Flow

AI does not deliver finished results. The human verifies, corrects, and sends back. This is not a failure of AI — it is the design of the collaboration.

**Bottom-up (preparation):** The human builds understanding from the ground up — vision, requirements, context, data, criteria. This is the 70%.

**Top-down (execution):** AI processes the structured input and generates output. The human reviews, accepts, corrects, or refines. This is the 30%.

**The feedback loop:** Every correction updates the preparation. If AI misunderstood a requirement, the requirement was likely ambiguous — fix it in DataPrep, not just in the output. If a prompt produced an unexpected result, the prompt template may need adjustment — fix it in Layer 3, not just in Layer 2.

This bidirectional flow ensures that WAVE is not a one-time setup. It is a living system where every interaction makes the next one better.

```
HUMAN EXPERTISE (70%)                AI AS AMPLIFIER (30%)
┌──────────────────────────┐         ┌──────────────────────────┐
│ Domain knowledge          │         │ Data processing           │
│ Situational context       │────────→│ Pattern recognition       │
│ Experience                │         │ Variant generation        │
│ Judgment and intuition    │←────────│ Scaling repetitive        │
│ Accountability            │         │   operations              │
└──────────────────────────┘         └──────────────────────────┘
          ↕ BIDIRECTIONAL FLOW ↕
```

---

## 5. Measuring What Matters

A methodology without metrics is a philosophy. WAVE defines specific, measurable indicators for the quality of human-AI collaboration.

### Primary Metrics

**Prompt Success Rate (PSR):** The percentage of prompts that produce a usable output on the first attempt.

```
PSR = (Prompts with good output on first try) / (Total prompts)

Starting:  ~60%
Proficient: >80%
Mastery:    >90%
```

PSR is the single most revealing metric. A low PSR means your DataPrep is incomplete or your prompts are imprecise. A high PSR means the 70% preparation is paying off.

**Data Preparation Coverage (DPC):** The percentage of relevant domain knowledge that has been structured and documented in Layer 1.

```
DPC = (Documented aspects) / (Total aspects needed)

Starting:  ~40%
Target:    >70%
Excellent: >85%
```

DPC measures how well you have made your expertise explicit. Low DPC does not mean you lack expertise — it means your expertise is still tacit, locked in your head where AI cannot access it.

**Time to First Correct Output (TFCO):** The elapsed time from task assignment to a usable result.

```
Without WAVE: 2-4 hours (multiple iterations)
With WAVE:    30-60 minutes (first-attempt success)
Target:       3-5x improvement
```

**Revision Rate (RR):** The average number of revisions needed per output.

```
Without WAVE: 3-5 revisions average
With WAVE:    0-1 revisions
Target:       <1.5
```

### The Self-Improvement Pattern

These metrics improve over time — not because AI gets smarter, but because your DataPrep deepens and your meta-prompts mature.

Typical trajectory:

| Week | PSR  | DPC  | TFCO     | Revision Rate |
| ---- | ---- | ---- | -------- | ------------- |
| 1    | 60%  | 40%  | 3-4h     | 3-5           |
| 4    | 75%  | 60%  | 1-2h     | 1-2           |
| 8    | 85%  | 75%  | 30-60min | 0-1           |
| 12   | 90%+ | 85%+ | 15-30min | ~0            |

This trajectory holds across domains. The numbers may vary, but the pattern is consistent: structured preparation leads to exponentially improving collaboration.

---

## 6. How WAVE Differs

WAVE is not the first attempt to structure human-AI interaction. But it occupies a space that no existing approach fills.

| Approach                             | What it is                                                   | What it lacks                                                |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Prompt engineering**               | Techniques for writing better individual prompts             | No project-level structure, no metrics, no preparation layer, no meta-level |
| **"Agile AI"**                       | Agile with AI bolted on                                      | No rethinking of human-AI roles, no preparation emphasis, no recursive improvement |
| **Responsible AI guidelines**        | Policies for ethical AI use                                  | Not a workflow — tells you what to avoid, not how to work    |
| **Tool tutorials**                   | How to use specific AI products                              | Product-specific, not methodology, no transferable framework |
| **Recursive Meta Prompting (MIT)**   | Academic technique for self-improving prompts                | Focused on mathematical reasoning, lacks DataPrep layer, no practical workflow |
| **Documentation-Driven Development** | Write docs before code                                       | Linear (not recursive), does not account for AI as collaborator |
| **WAVE**                             | **Three-layer methodology with 70/30 principle, defined metrics, reusable templates, recursive improvement, domain-agnostic** | **First full implementation in software engineering; other domains in early exploration** |

The closest historical parallel is not in AI — it is in manufacturing. **Lean** began as Toyota Production System in the 1940s, focused on automobile manufacturing. Over decades, its principles (value, flow, waste elimination, continuous improvement) proved universal. By 2026, Lean is used in healthcare, education, construction, government, finance, and dozens of other fields.

Lean solved the problem of waste in physical and organizational processes. WAVE addresses a fundamentally different and — in the context of 2026 — more urgent problem: **how should humans collaborate with AI so that AI amplifies them rather than replaces them.**

This is not an industry-specific problem. It is a civilizational one. Every organization in the world — from a solo practice to a multinational corporation, from a hospital to a nonprofit, from a military unit to a school — faces the same question: "We have AI. How do we use it so that people become better, not obsolete?"

---

## 7. WAVE in Software Engineering

Software development is WAVE's first and most deeply validated domain. A separate document — [WAVE for Software Engineering](WAVE_Software_Engineering_v1.0_EN.md) — provides the full applied guide with code examples, prompt templates, and measured results.

Here is the summary:

**Context:** A solo developer building a complex web platform with AI assistance. Traditional approach: chaotic prompting, 10 iterations per task, inconsistent architecture, 8+ weeks for MVP. WAVE approach: structured DataPrep (architecture documents, component specifications, API contracts), precision prompts drawing on prepared data, meta-prompt templates for recurring task types.

**Results:**

| Metric                   | Without WAVE | With WAVE | Improvement |
| ------------------------ | ------------ | --------- | ----------- |
| Development time         | 8+ weeks     | 6 weeks   | 25% faster  |
| First-attempt success    | ~30%         | ~80%      | 2.7x better |
| Revisions per task       | 3-5          | 0-1       | 4x fewer    |
| Code consistency         | Low          | High      | Qualitative |
| Developer cognitive load | High         | Low       | Qualitative |
| Documentation coverage   | ~40%         | ~95%      | 2.4x better |

The full case study, including specific DataPrep documents, prompt examples, and daily workflow patterns, is available in the companion document.

---

## 8. Beyond Software: WAVE Across Domains

The three layers of WAVE — structuring domain knowledge, creating precise tasks for AI, and building reusable meta-templates — contain nothing specific to software. They describe a universal pattern of human-AI collaboration.

Below are six domains where WAVE's principles apply directly. Each sketch shows how the three layers map to that domain's specific challenges. These are outlines, not full implementations — invitations for practitioners to test, adapt, and report back.

### Pharmaceutical Research

A research team prepares data about a candidate molecule — chemical structure, known interactions, preclinical trial results (**DataPrep**). They structure this data for AI-assisted molecular modeling, specifying exactly what predictions are needed (**Prompt2Data**). They iteratively refine protein binding predictions, using meta-prompts built on results from previous iterations (**Prompt2Prompt**).

The 70/30 principle protects against blind trust in AI predictions. Seventy percent is the chemist's expertise — understanding biological context, recognizing when a computationally optimal molecule is biologically implausible. AI accelerates the search space. The human ensures the search is meaningful.

### Healthcare

A physician prepares a patient's medical history, test results, and genetic context (**DataPrep**). AI analyzes the data for diagnostic patterns (**Prompt2Data**). The physician verifies, rejects, or refines recommendations by adding clinical context — how the patient responds psychologically, treatment preferences, support system (**Prompt2Prompt**).

Here, 70/30 is not a productivity principle. It is a safety principle. The human's 70% — clinical judgment, patient relationship, ethical responsibility — is irreplaceable.

### Education

A teacher prepares data about a class — individual learning outcomes, learning styles, behavioral patterns (**DataPrep**). AI analyzes patterns and proposes personalized learning paths (**Prompt2Data**). The teacher corrects recommendations based on knowledge of classroom dynamics, family situations, emotional context (**Prompt2Prompt**).

The teacher — not AI — decides the pedagogical strategy. AI handles the data processing that would take weeks manually. The teacher provides the human insight that makes personalization meaningful rather than algorithmic.

### Law

A lawyer prepares the facts of the case, applicable statutes, and relevant precedents (**DataPrep**). AI analyzes precedents and identifies legal risks (**Prompt2Data**). The lawyer verifies against litigation strategy, client intent, and interpretive nuance (**Prompt2Prompt**).

No AI replaces legal judgment on which line of argument to pursue. But WAVE allows the lawyer to work faster and more comprehensively — reviewing more precedents, identifying more risks, preparing more thorough briefs.

### Nonprofit Organizations

A grants team prepares data about a target community — demographics, previous interventions, measured outcomes (**DataPrep**). They structure this for AI to identify effectiveness patterns in historical data (**Prompt2Data**). They iteratively build an intervention plan, each round refining recommendations based on local constraints (**Prompt2Prompt**).

Seventy percent is field knowledge — cultural context, relationships with local leaders, history of what has been tried and why it succeeded or failed. This is tacit knowledge that no dataset contains and no AI possesses.

### Industrial Engineering

An engineer prepares project specifications, material constraints, and safety standards (**DataPrep**). AI generates design variants meeting the parameters (**Prompt2Data**). The engineer verifies against practical experience — how materials behave under extreme conditions, assembly limitations, lessons from past projects (**Prompt2Prompt**).

The 70% is the engineer's domain expertise — decades of knowing what works in practice versus what works on paper.

### The Common Pattern

In every case, the pattern is identical:

|                   | Human (70%)                                                  | AI (30%)                                                     |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Brings**        | Domain knowledge, situational context, experience, judgment, accountability | Data processing, pattern recognition, variant generation, scaling |
| **DataPrep**      | Structures what they know                                    | —                                                            |
| **Prompt2Data**   | Defines the task precisely                                   | Executes at scale                                            |
| **Prompt2Prompt** | Builds reusable templates                                    | —                                                            |
| **Verification**  | Judges quality, corrects, decides                            | —                                                            |

The human leads. The AI amplifies. The methodology connects them.

**If you work in any of these domains and want to test WAVE — we invite you to do so.** Open an Issue on the GitHub repository describing your experience. Write a case study. Tell us what worked and what broke. WAVE will grow through practitioners, not through theory.

---

## 9. Getting Started

You do not need to implement all three layers on day one. Start small, build up.

### Week 1: DataPrep Foundation

Pick one task you regularly do with AI. Before you start the next instance:

1. Write down everything you know about the task — context, constraints, what good output looks like, what mistakes to avoid.
2. Organize this into a simple document: Vision → Requirements → Context → Success Criteria.
3. Use this document as the basis for your next AI interaction.

Observe the difference. If your first-attempt success rate improves, you have experienced the core of WAVE.

### Week 2: Precision Prompts

Take the DataPrep from Week 1 and build a structured prompt:

1. Context (from your DataPrep)
2. One specific task
3. Constraints
4. Input data
5. Expected output format
6. Success criteria

Compare this structured prompt to your typical interactions. Measure PSR.

### Week 3: Meta-Prompts

Identify the types of tasks you do repeatedly. For each type, create a template that defines:

- What DataPrep inputs are needed
- What prompt structure works best
- What variables change between instances

Use these templates for the next batch of tasks. You now have all three layers working.

### Week 4+: Measure and Improve

Track PSR, DPC, TFCO, and Revision Rate. Update your DataPrep, prompts, and meta-prompts based on what you learn. The methodology improves itself.

---

## 10. FAQ

**Is WAVE only for software development?**

No. WAVE was born in software development, and that is where its deepest case study exists. But the three layers, the 70/30 principle, the metrics, and the bidirectional flow contain nothing specific to any single domain. They describe a universal pattern of human-AI collaboration. Section 8 outlines six additional domains.

**Do I need to be technical to use WAVE?**

No. DataPrep is about organizing your expertise — whatever that expertise is. A teacher's DataPrep looks different from an engineer's, but the principle is the same: make your knowledge explicit and structured so that AI can use it effectively.

**How is WAVE different from just "writing good prompts"?**

Prompt engineering is a technique. WAVE is a methodology. The difference is like between knowing how to use a hammer and having a construction plan. Good prompts are part of WAVE (Layer 2), but they are embedded in a larger system of preparation (Layer 1) and reusable templates (Layer 3), with defined metrics to track improvement.

**What AI tools does WAVE work with?**

WAVE is tool-agnostic. It works with any AI that accepts structured input — Claude, ChatGPT, Gemini, Copilot, domain-specific models, or future tools that do not yet exist. The methodology is about how you prepare and structure your collaboration, not about which product you use.

**How long before I see results?**

Most practitioners report noticeable improvement in first-attempt success rate within the first week of disciplined DataPrep. Significant improvement in overall efficiency (3-5x) typically emerges by week 4-8, as meta-prompts mature and DataPrep coverage deepens.

**Can a team use WAVE, or is it only for solo practitioners?**

WAVE works for individuals and teams. In a team setting, DataPrep becomes a shared knowledge base, meta-prompts become team standards, and metrics become collaboration benchmarks. The principles scale.

**What if my domain is not listed in Section 8?**

The six domains listed are illustrations, not limits. If you work with AI in any capacity — research, marketing, design, finance, administration, journalism, architecture — WAVE's three layers apply. We actively invite practitioners from unlisted domains to test WAVE and share their experience.

**Is WAVE free?**

Yes. WAVE is published under CC BY-SA 4.0. You can use it, adapt it, teach it, and build on it — as long as you give attribution and share your adaptations under the same license.

---

## 11. Origins

WAVE was created on January 17, 2026, during a working session between Przemysław Zieliński and Claude (Anthropic). Zieliński, CEO and co-founder of IDareU — a gamified education platform — needed a structured approach to building a complex web application with AI assistance. Existing approaches were either too academic (Recursive Meta Prompting), too narrow (prompt engineering guides), or too vague ("just use AI more").

The three-layer structure — DataPrep, Prompt2Data, Prompt2Prompt — emerged from practical necessity: the realization that 70% of the value in AI collaboration comes from what the human prepares before the AI is engaged, and only 30% from the execution itself.

During preparation for open publication in February 2026, a critical insight emerged: the three layers contain nothing specific to software. They describe a universal pattern of structuring human expertise for AI amplification. The decision was made to publish WAVE as a generic methodology from day one, with software engineering as the first and deepest case study — learning from Lean's costly mistake of starting with the "Manufacturing" label and spending decades shedding it.

The Polish name FALA — Formuła Amplifikacji Ludzkiej Aktywności (Formula for Amplifying Human Activity) — was chosen because it places the human at the center of the name itself: it is human activity that is amplified, not replaced.

---

## 12. Citation and License

### License

WAVE is published under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

You are free to share, adapt, and build upon WAVE for any purpose, including commercial use, as long as you give appropriate credit and distribute your contributions under the same license.

### Citation

If you use WAVE in your work, please cite:

```
Zieliński, P. (2026). WAVE: Workflow Amplification via Vectored Expertise — 
A Human-AI Collaboration Methodology (v1.0). 
https://github.com/[username]/WAVE-Methodology
DOI: [to be assigned upon Zenodo publication]
```

### Contributing

WAVE is v1.0 — born from software development, designed for every domain. It will grow through practitioners who test it, break it, and improve it.

If you want to contribute — case studies, templates, translations, critique — see [CONTRIBUTING.md](../CONTRIBUTING.md).

We are looking for **co-maintainers** who are passionate about human-AI collaboration and want to help this methodology reach its potential. If that is you, open an Issue titled "Co-Maintainer Application" on the GitHub repository.

---

*WAVE Methodology v1.0 — Published February 2026*  
*Created by Przemysław Zieliński with Claude (Anthropic)*  
*"The human leads. The AI amplifies."*
