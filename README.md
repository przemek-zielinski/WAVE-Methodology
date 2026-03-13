# WAVE — Workflow Amplification via Vectored Expertise
### Metodyka współpracy człowiek-AI | Human-AI Collaboration Methodology

> **WAVE mówi jak przygotować kontekst, prowadzić sesję i budować wiedzę, żeby AI pracował na najlepszych założeniach — nie na zgadywaniu.**
>
> *WAVE teaches how to prepare context, run sessions, and build knowledge so AI works from the best possible assumptions — not from guesswork.*

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)]()

---

## Szybki Start / Quick Start

**PL:** Trzy kroki — od zera do pierwszego Living Pattern w kilka godzin.

**EN:** Three steps — from zero to your first Living Pattern in a few hours.

```
  KROK 1 / STEP 1 — Wybierz profil / Choose your profile
  ─────────────────────────────────────────────────────────
  □ Prototyp / POC?        → DISCOVERY (1-5 dni / days)
  □ MVP / pilot?           → BUILD (4-8 tygodni / weeks)
  □ Produkt docelowy?      → SCALE (miesiące / months)
  
  Nie wiesz? Zacznij od DISCOVERY. / Not sure? Start with DISCOVERY.

  KROK 2 / STEP 2 — Uruchom SCAN / Run SCAN
  ─────────────────────────────────────────────
  Otwórz czat z AI. Wklej prompt z living-patterns/SCAN-Prompt.md
  z opisem swojego rozwiązania. Dostaniesz mapę obszarów do zbadania.
  
  Open a chat with AI. Paste the prompt from living-patterns/SCAN-Prompt.md
  with your solution description. You'll get a map of areas to investigate.

  KROK 3 / STEP 3 — Uruchom PULSE / Run PULSE
  ──────────────────────────────────────────────
  Weź najważniejszy obszar. Wklej living-patterns/PULSE-Prompt.md
  z parametrami. Przeprowadź Rundę 1. Masz pierwszy Living Pattern.
  
  Take the top-priority area. Paste living-patterns/PULSE-Prompt.md
  with parameters. Run Round 1. You have your first Living Pattern.
```

**Czego potrzebujesz / What you need:** Dostęp do AI z wyszukiwaniem (Claude, ChatGPT, Gemini z web search). Opis rozwiązania które budujesz. / Access to AI with web search. Description of what you're building.

---

## Co to jest WAVE / What is WAVE

WAVE to **metodyka** — uporządkowany zbiór zasad współpracy człowiek-AI. Nie narzędzie, nie framework, nie kurs promptów. Metodyka, jak Scrum czy Lean — ale dla zupełnie innego pytania.

Scrum odpowiada na pytanie „jak organizować pracę zespołu." Lean na „jak eliminować marnotrawstwo." **WAVE odpowiada na pytanie „jak współpracować z AI, żeby AI wzmacniało człowieka zamiast go zastępować."**

*WAVE is a methodology for human-AI collaboration. Not a tool, not a framework, not a prompting course. A methodology — like Scrum or Lean — but for a fundamentally different question: how to work with AI so it amplifies you instead of replacing you.*

---

## Co nowego w v2.0

v2.0 to skok pokoleniowy wobec v1.0. Oto kluczowe zmiany:

| Element | v1.0 (luty 2026) | v2.0 (marzec 2026) |
|---|---|---|
| Struktura | Trzy warstwy (DataPrep/P2D/P2P) | Trójwarstwowa architektura: Filozofia → Komponenty → Praktyki |
| Narzędzia | Brak | Living Patterns (SCAN + PULSE), FALA, Decision Log |
| Standardy gotowości | Brak | **DooR** — Definition of Operational Readiness |
| Test kompletności | Brak | **AANP** — Aktor, Akcja, Narzędzie, Produkt |
| Profile produktu | Brak | **Discovery / Build / Scale** — suwak intensywności |
| Zasada 70/30 | Sztywna reguła | Grawitacja — ~60/40 w Discovery, ~70/30 w Build, ~50/50 w dużym Scale |
| Pierwsze zastosowanie | Brak studium przypadku | **Software Engineering** — z danymi o paradoksie produktywności AI |
| Automatyzacja | Brak | **LP Pipeline** — półautomatyczny pipeline na GitHub Actions (SCAN → PULSE → Publisher, ~$1/LP) |
| Auto-doskonalenie | Brak | **Cross-Session Merge** — dwie sesje z różnymi kątami > jedna sesja z Rundą 4 |
| Powtarzalność | Nieprzetestowana | **Potwierdzona** — dwie niezależne sesje → te same fundamenty, różne profile |
| Meta-aksjomat | Brak | **Prądy i Napięcia / Currents and Tensions** — nawigacja rywalizujących atrybutów, emergencja na ich przecięciu |

---

## Mapa dokumentów / Document Map

### Ścieżka czytelnika / Reader's Path

```
  Nowy tutaj?
  │
  └──▶ Dokument główny WAVE v2.0
       Filozofia, DooR, AANP, Living Patterns, Profile
       │
       ├──▶ Chcesz budować wiedzę?
       │    └──▶ Living Patterns (SCAN + PULSE)
       │
       ├──▶ Jesteś programistą / budujesz oprogramowanie?
       │    └──▶ Dokument Referencyjny SE
       │         7 problemów pracy z AI + 7 odpowiedzi WAVE
       │         + Profile Produktu (Discovery / Build / Scale)
       │
       └──▶ Chcesz przejść od dokumentu do kodu?
            └──▶ FALA + RtS (pipeline implementacyjny)
```

### Pełna lista dokumentów

| Dokument | Język | Folder | Co robi |
|---|:---:|---|---|
| **WAVE Metodyka v2.0** | PL | `docs/` | Dokument główny — filozofia, architektura, komponenty |
| **WAVE Methodology v2.0** | EN | `docs/` | Main document — philosophy, architecture, components |
| **Dokument Referencyjny SE v1.2** | PL | `docs/` | Pierwsze zastosowanie dziedzinowe — software engineering |
| **WAVE SE Reference v1.2** | EN | `docs/` | First domain application — software engineering |
| **Profile Produktu v1.2** | PL | `docs/` | Discovery / Build / Scale — jak skalować WAVE |
| **Product Profiles v1.2** | EN | `docs/` | Discovery / Build / Scale — how to scale WAVE |
| **SCAN-Prompt v3** | PL | `living-patterns/` | Prompt do rozpoznania terenu |
| **SCAN-HowTo v3** | PL | `living-patterns/` | Instrukcja użycia SCAN |
| **PULSE-Prompt v3** | PL | `living-patterns/` | Prompt do budowania Living Pattern |
| **PULSE-HowTo v3** | PL | `living-patterns/` | Instrukcja użycia PULSE |
| **Living Patterns Ecosystem v3** | PL | `living-patterns/` | Pełna dokumentacja ekosystemu |
| **FALA RtS Procedura v1** | PL | `fala/` | Pipeline: dokument → kod (SE) |
| **FALA RtS Blueprint v3** | PL | `fala/` | 11 warstw specyfikacji technicznej (SE) |
| **FALA RtS Szablon v1** | PL | `fala/` | Szablon do wypełnienia (SE) |

---

## Architektura WAVE — w jednym spojrzeniu

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   WAVE — Metodyka Współpracy Człowiek-AI                           ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  WARSTWA 1: FILOZOFIA (zamknięta — 5 aksjomatów)            │  ║
║   │                                                              │  ║
║   │  70/30 • Człowiek kieruje • Buduj kompletnie                │  ║
║   │  • Droga = wartość • Porażki uczą                           │  ║
║   │  Meta-aksjomat: Prądy i Napięcia (nawigacja, nie optymalizacja)│ ║
║   │                                                              │  ║
║   │  Trzy poziomy H-AI: DataPrep → Prompt2Data → Prompt2Prompt  │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  WARSTWA 2: KOMPONENTY (otwarte — zbiór rośnie)             │  ║
║   │                                                              │  ║
║   │  DooR — Definition of Operational Readiness                 │  ║
║   │  Living Patterns (SCAN, PULSE) • FALA • Decision Log        │  ║
║   │  [+ przyszłe komponenty → zbiór otwarty]                    │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  WARSTWA 3: PRAKTYKI (otwarte — nawyki narastają)           │  ║
║   │                                                              │  ║
║   │  Checkpointy • Krótsze sesje • Wersjonowanie • Imperatyw    │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │  TEST KOMPLETNOŚCI: AANP (zamknięty)                        │  ║
║   │  Każdy proces = Aktor + Akcja + Narzędzie + Produkt         │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## Dla kogo jest WAVE / Who is WAVE for

**Programista pracujący z AI** — piszesz kod z Cursorem, Copilotem, Claude? WAVE mówi jak przygotować kontekst żeby AI nie zgadywał architektury twojego projektu. Dokument Referencyjny SE pokazuje siedem zmierzonych problemów i siedem odpowiedzi.

**Twórca produktu / założyciel startupu** — budujesz MVP z AI jako głównym partnerem? Profile Produktu mówią jak skalować WAVE od prototypu (3 dni) do produktu (miesiące) bez wyrzucania pracy.

**Każdy kto pracuje z AI** — piszesz dokumenty, analizujesz dane, projektujesz kursy, badasz rynek? Living Patterns (SCAN + PULSE) budują bazę wiedzy dla twojego projektu — żebyś działał na najlepszych założeniach, nie na intuicji.

---

## Studium przypadku / Case Study

WAVE jest metodyką wytwórczą **IDareU Gen2** — trójstronnej platformy edukacyjnej łączącej mentorów, uczniów i marki przez wyzwania wideo z feedbackiem eksperckim.

| Metryka | Wartość |
|---|:---:|
| Zespół | 2 osoby + AI (Claude) |
| Decyzje w Decision Log | 31+ |
| Dokumenty specyfikacji | 20 |
| Linie dokumentacji | ~7 000+ |
| Warstwy inteligencji AI | 3 (HIVE + TACIT + AGAPE) |
| Stack | Next.js 15, Supabase, Tailwind, shadcn/ui |

### LP Pipeline — działająca infrastruktura

WAVE ma działający półautomatyczny pipeline na GitHub Actions. Proposal Generator codziennie proponuje nowe dziedziny do zbadania. Pipeline uruchamia SCAN, trzy rundy PULSE i Publisher — z bramkami decyzyjnymi między krokami. Koszt jednego Living Pattern: poniżej dolara. AI proponuje, człowiek zatwierdza.

Metoda potwierdzona jako stabilna i powtarzalna — dwie niezależne sesje PULSE dla tego samego obszaru doszły do identycznych fundamentów (18 zasad, ~25 błędów, te same metryki) z różnymi profilami.

Pełny opis w Dokumencie Referencyjnym SE, rozdział 8.

---

## Struktura repozytorium / Repository Structure

```
WAVE-Methodology/
├── README.md                              ← ten plik / this file
├── CITATION.cff
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE (CC BY-SA 4.0)
│
├── docs/                                  ← dokumenty główne
│   ├── WAVE_Methodology_v2_0_PL.md
│   ├── WAVE_Methodology_v2_0_EN.md
│   ├── WAVE_SE_Reference_v1_2_PL.md
│   ├── WAVE_SE_Reference_v1_2_EN.md
│   ├── WAVE_Product_Profiles_v1_2_PL.md
│   └── WAVE_Product_Profiles_v1_2_EN.md
│
├── living-patterns/                       ← narzędzia budowania wiedzy
│   ├── SCAN-Prompt.md
│   ├── SCAN-HowTo.md
│   ├── PULSE-Prompt.md
│   ├── PULSE-HowTo.md
│   └── WAVE_Living_Patterns_Ecosystem_v3.md
│
├── fala/                                  ← pipeline implementacyjny (SE)
│   ├── 01_WAVE_FALA_RtS_Procedura_Kodowania_v1.md
│   ├── 02_WAVE_FALA_RtS_Blueprint_Walidacja_v3.md
│   └── 03_WAVE_FALA_RtS_Szablon_Blueprint_v1.md
│
├── .github/workflows/                     ← LP Pipeline (GitHub Actions)
│   ├── lp-propose.yml                     ← Proposal Generator (codziennie)
│   └── lp-pipeline.yml                    ← SCAN → PULSE → Publisher
│
├── scripts/                               ← Skrypty pipeline'u
│   ├── lp_common.py
│   ├── propose_lp.py
│   ├── run_scan.py
│   ├── run_pulse.py
│   └── publish_lp.py
│
├── archive/v1.0/                          ← poprzednia wersja
│   ├── WAVE_Methodology_v1.0_EN.md
│   └── FALA_Metodyka_v1.0_PL.md
│
├── templates/
├── examples/
└── assets/
```

---

## Licencja / License

**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

Możesz używać, adaptować, uczyć i rozbudowywać — pod warunkiem przypisania autorstwa i udostępnienia adaptacji na tej samej licencji.

*You may use, adapt, teach, and build upon — with attribution and share-alike.*

## Cytowanie / Citation

```
Zieliński, P. (2026). WAVE: Workflow Amplification via Vectored Expertise — 
Metodyka współpracy człowiek-AI (v2.0). 
https://github.com/przemek-zielinski/WAVE-Methodology
```

## Współtworzenie / Contributing

WAVE to v2.0 — urodzona w wytwarzaniu oprogramowania, zaprojektowana dla każdej dziedziny. Rośnie dzięki praktykom, którzy ją testują, łamią i udoskonalają.

Studia przypadków, szablony Living Patterns dla nowych branż, tłumaczenia, krytyka — zobacz [CONTRIBUTING.md](CONTRIBUTING.md).

Szukamy **współprowadzących (co-maintainers)**, którzy są pasjonatami współpracy człowiek-AI.

---

## Geneza / Origin

WAVE powstała 17 stycznia 2026 roku, podczas sesji roboczej Przemysława Zielińskiego z Claude (Anthropic). Trójwarstwowa struktura — DataPrep, Prompt2Data, Prompt2Prompt — wyłoniła się z praktycznego odkrycia, że większość wartości we współpracy z AI pochodzi z tego, co człowiek przygotuje ZANIM AI zostanie zaangażowane.

V1.0 opublikowana w lutym 2026. V2.0 — marzec 2026, z DooR, AANP, Living Patterns, FALA, profilami produktu i pierwszym zastosowaniem dziedzinowym w software engineering.

Polska nazwa FALA — **Formuła Amplifikacji Ludzkiej Aktywności** — stawia człowieka w centrum już w samej nazwie.

---

*WAVE v2.0 — Człowiek prowadzi. AI wzmacnia. / The human leads. AI amplifies.*
