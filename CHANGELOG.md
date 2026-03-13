# Changelog

All notable changes to WAVE Methodology will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.0.0] — 2026-03-12

### Added — New Concepts
- **DooR** (Definition of Operational Readiness) — category of readiness standards for transitions between work phases
- **AANP** (Aktor, Akcja, Narzędzie, Produkt / Actor, Action, Tool, Product) — completeness test for any process in WAVE
- **Product Profiles**: Discovery / Build / Scale — intensity slider matching WAVE to project type
- **FALA** (From Architecture to Live Application) — three-session pipeline from document to working code
- **RtS** (Requisite-to-Start) — 11-layer technical blueprint standard for software engineering
- **70/30 as gravity** — the preparation/execution ratio is a center of gravity, not a rigid rule (~60/40 in Discovery, ~70/30 in Build, ~50/50 in large Scale)
- **Cross-Session Merge** — new auto-improvement variant: two PULSE sessions with different angles > one session with Round 4 (DEC-039)
- **LP Pipeline** — semi-automated pipeline on GitHub Actions: Proposal Generator (daily) → SCAN → 3 PULSE rounds → Publisher, ~$1/LP (DEC-041)
- **SCAN v2** — two-stage selection: 8-10 candidates → scoring (Impact × Risk × Knowledge) → top 5-6 (DEC-048)
- **Currents and Tensions / Prądy i Napięcia** — navigation meta-axiom: every H-AI session plays out on a field of competing attributes; emergence is born at their intersection; reserve is a first-class value, not waste. Validated by Carl Benedikt Frey's thousand-year analysis of civilizational progress

### Added — New Documents
- WAVE Metodyka v2.0 PL — complete rewrite of the main methodology document
- WAVE Methodology v2.0 EN — English version of the main document
- Dokument Referencyjny Software Engineering v1.2 PL — first domain application with AI productivity paradox data
- WAVE SE Reference v1.2 EN — English version of SE reference
- Profile Produktu v1.2 PL — Discovery/Build/Scale with hourly breakdowns
- FALA: Procedura Kodowania v1, Blueprint Walidacja v3, Szablon Blueprint v1

### Added — Infrastructure
- GitHub Actions workflows: `lp-propose.yml` (daily proposals), `lp-pipeline.yml` (SCAN → PULSE → Publisher)
- Pipeline scripts: `lp_common.py`, `propose_lp.py`, `run_scan.py`, `run_pulse.py`, `publish_lp.py`
- Label-based approval gates between pipeline stages (human approves, AI executes)
- Bilingual EN+PL output at every pipeline stage (DEC-045)
- Domain category prefix in LP file names (DEC-046)
- Post-processing markdown repair (tables + orphan dots) (DEC-043)

### Validated
- **Repeatability test passed** — two independent PULSE sessions produced identical foundations: 18 principles, ~25 errors, same target metrics (DEC-038)
- **Cross-Session Merge confirmed** — scoring: session 1 = 7.4, session 2 = 8.0, merged = >9.0 (DEC-039)
- **Prompt philosophy validated** — "create freely, fill completely" (1 rule) outperformed 12 strict rules: 18 vs 12 principles, 7 vs 4 tables (DEC-042)

### Changed
- Three-layer architecture: Philosophy → Components → Practices (previously DataPrep/P2D/P2P was the entire methodology description)
- Living Patterns Ecosystem updated to v3.0 with auto-improvement cycle
- README completely rewritten with Quick Start, document map, and reader's path

### Archived
- v1.0 papers moved to `/archive/v1.0/` — preserved for reference

---

## [1.0.0] — 2026-02-15

### Added
- Initial release of WAVE Methodology
- WAVE Methodology v1.0 EN — generic methodology document
- FALA Metodyka v1.0 PL — Polish version
- Living Patterns ecosystem: SCAN-Prompt, SCAN-HowTo, PULSE-Prompt, PULSE-HowTo, Ecosystem document
- CITATION.cff, CONTRIBUTING.md, LICENSE (CC BY-SA 4.0)
