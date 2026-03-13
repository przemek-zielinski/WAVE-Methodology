# WAVE — Profile Produktu
## Jak skalować WAVE do rodzaju budowanego rozwiązania
### Dokument towarzyszący do WAVE Dokument Referencyjny SE v1.2 | Marzec 2026

**Autor koncepcji:** Przemek Zieliński  
**Opracowanie:** Claude Opus 4.6  
**Licencja:** CC BY-SA 4.0  
**Dokument nadrzędny:** WAVE Dokument Referencyjny Software Engineering v1.2

---

## Spis treści

— Szybki Start — wybierz profil w 60 sekund
1. Idea — jedna metodyka, trzy profile
2. Trzy profile produktu — przegląd
3. Profil DISCOVERY (POC / Spike / Proof of Concept)
4. Profil BUILD (MVP / Pilot / Beta)
5. Profil SCALE (Produkt / Platforma / Enterprise)
6. Ewolucja profili — od Discovery do Scale
7. Porównanie zestawione — czas, zakres, koszt, jakość
8. Kiedy który profil — drzewo decyzyjne
9. Aksjomaty nie skalują się — co jest niepodzielne

---

## Szybki Start — wybierz profil w 60 sekund

Nie chcesz czytać dziewięciu rozdziałów? Odpowiedz na jedno pytanie:

```
  Co budujesz?
  │
  ├── „Chcę sprawdzić czy pomysł ma sens"
  │    → DISCOVERY — 1 do 5 dni, 2-4h przygotowania, 1,5-3h kodowania
  │    → Przejdź do rozdziału 3
  │
  ├── „Mam zwalidowany pomysł, buduję pierwszą wersję"
  │    → BUILD — 4 do 8 tygodni, ~70h przygotowania, ~25h kodowania
  │    → Przejdź do rozdziału 4
  │
  └── „Mam działający MVP, skaluję do produktu"
       → SCALE — miesiące, setki godzin przygotowania i kodowania
       → Przejdź do rozdziału 5
```

**Kluczowa zasada:** Profile są ewolucyjne. Discovery przesuwa się do Build. Build do Scale. Kod, dokumentacja i decyzje rosną z tobą — nie wyrzucasz niczego.

**Nie wiesz co wybrać?** Zacznij od DISCOVERY. Zawsze. Nawet jeśli „czujesz" że potrzebujesz więcej — lepiej zwalidować w 3 dni niż budować 3 miesiące w złym kierunku.

---

## 1. Idea — jedna metodyka, trzy profile

WAVE to jedna metodyka. Nie ma „WAVE Light" i „WAVE Full" — tak jak nie ma „Lean Light" i „Lean Full." Są zasady, które stosujesz proporcjonalnie do tego, co budujesz.

Aparat fotograficzny ma jeden obiektyw i jedną fizykę światła. Ale raz robisz zdjęcie na plakat wielkoformatowy — tripod, oświetlenie studyjne, pełna rozdzielczość. A raz robisz zdjęcie na Instagram — telefon, naturalne światło, dwie sekundy. Fizyka jest ta sama. Zmienia się skala.

```
  WAVE — JEDNA METODYKA, TRZY PROFILE PRODUKTU

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  FILOZOFIA (5 aksjomatów)          ← zawsze ta sama         │
  │  AANP (test kompletności)          ← zawsze obowiązuje      │
  │  DooR (zasada przejść)             ← zawsze obowiązuje      │
  │  Trzy poziomy H-AI                ← zawsze ten sam rytm    │
  │                                                             │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
  │  │DISCOVERY │  │  BUILD   │  │  SCALE   │  ← skala zmienia │
  │  │  (POC)   │  │  (MVP)   │  │(Produkt) │    się, filozofia │
  │  │          │  │          │  │          │    — nie           │
  │  └──────────┘  └──────────┘  └──────────┘                  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

Kluczowa zasada: **profil określa skalę komponentów, nie ich obecność.** Każdy profil ma SCAN, ma przygotowanie kontekstu, ma weryfikację. Różni się głębokość — nie istnienie.

---

## 2. Trzy profile produktu — przegląd

### Tabela porównawcza — widok z lotu ptaka

| Wymiar | DISCOVERY (POC) | BUILD (MVP) | SCALE (Produkt) |
|---|---|---|---|
| **Cel** | Zwalidować pomysł | Dostarczyć wartość | Skalować i utrzymać |
| **Pytanie** | „Czy to ma sens?" | „Czy ludzie tego chcą?" | „Czy to wytrzyma skalę?" |
| **Czas łączny** | 1–5 dni | 4–8 tygodni | Miesiące → lata |
| **Zespół H-AI** | 1 osoba + AI | 1–3 osoby + AI | Zespół + AI |
| **Budżet** | Czas własny + subskrypcja AI | Tysiące € | Dziesiątki–setki tysięcy € |
| **Jakość kodu** | Działa i pokazywalne | Działa, bezpieczne, testowalne | Produkcyjne, skalowalne, monitorowane |
| **Ryzyko bez WAVE** | POC nie do rozbudowy | MVP = dług od dnia 1 | Spaghetti Point po 3 mies. |
| **Proporcja P/E** | ~60/40 | ~70/30 | 50-70 / 30-50 |

### Zasada 70/30 jako grawitacja

Aksjomat 70/30 to grawitacja, nie nakaz. Ciało zawsze spada ku ziemi, ale trajektoria zależy od tego co budujesz. Ale we WSZYSTKICH profilach przygotowanie to co najmniej połowa pracy — co jest radykalną odwrotnością vibe codingu, gdzie przygotowanie równa się zeru.

```
  PROPORCJA PRZYGOTOWANIE / EGZEKUCJA (dane z przeliczenia godzinowego)

  DISCOVERY:  ████████████████████████░░░░░░░░░░░░░░░░░░░  ~57/43
  BUILD:      ████████████████████████████████░░░░░░░░░░░░  ~70/30
  SCALE (mały)████████████████████████████████░░░░░░░░░░░░  ~70/30
  SCALE (duży)██████████████████████████░░░░░░░░░░░░░░░░░░  ~50/50
  Vibe coding:░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0/100

              ├── przygotowanie ──┤├── egzekucja ──┤
```

### Rozkład godzinowy — co składa się na przygotowanie i egzekucję

| Czynność | Discovery | Build | Scale (mały) | Scale (duży) |
|---|:---:|:---:|:---:|:---:|
| **PRZYGOTOWANIE:** | | | | |
| SCAN | 15-30 min | 2-3h | 3-5h | 3-5h |
| PULSE | 1-2h | 15-25h | 60-80h | 60-120h |
| Specyfikacje / projektowanie | — | 10-15h | 40-60h | 40-80h |
| Decision Log | — | 3-5h | 10-15h | 10-20h |
| FALA Sesja 1 (audyt) | — | 5-10h | 10-20h | 10-40h |
| FALA Sesja 2 (blueprint) | 30 min-1h | 6-15h | 30-50h | 30-100h |
| Auto-doskonalenie LP | — | — | 10-15h | 10-20h |
| Zebranie kontekstu | 15-30 min | wliczone | wliczone | wliczone |
| **Suma przygotowania** | **2-4h** | **41-73h** | **163-245h** | **163-385h** |
| **EGZEKUCJA:** | | | | |
| Kodowanie z AI | 1-2h | 9-25h | 50-100h | 50-300h |
| Testy, DoD, integracja | 30 min-1h | 5-10h | 20-40h | 20-80h |
| **Suma egzekucji** | **1,5-3h** | **14-35h** | **70-140h** | **70-380h** |
| | | | | |
| **ŁĄCZNIE** | **3,5-7h** | **55-108h** | **233-385h** | **233-765h** |
| **PROPORCJA P/E** | **~57/43** | **~70/30** | **~70/30** | **~50/50** |

### Wizualizacja proporcji — czas

```
  DISCOVERY        BUILD              SCALE
  ─────────        ─────              ─────

  Przygotowanie:   Przygotowanie:     Przygotowanie:
  ██████░░░░       ██████████░░░░     ████████████████████░░░░░░░░░░
  2-4h             41-73h             163-385h

  Egzekucja:       Egzekucja:         Egzekucja:
  ████░░░░░░       ████░░░░░░░░░░     ██████████████████████████████
  1,5-3h           14-35h             70-380h

  Dokumentacja:    Dokumentacja:      Dokumentacja:
  █░░░░░░░░░       ████░░░░░░░░░░    ██████████████████████████░░░░
  1-3 pliki        10-20 plików       50+ plików

  ─────────────────────────────────────────────────────────▶
  1-5 dni          4-8 tygodni        miesiące → lata
```

---

## 3. Profil DISCOVERY — POC / Spike / Proof of Concept

### Kiedy używać

Masz pomysł i chcesz sprawdzić czy ma sens — technicznie, rynkowo lub operacyjnie. Nie budujesz produktu. Budujesz dowód, że WARTO budować produkt. Klient (wewnętrzny lub zewnętrzny) chce zobaczyć „czy to w ogóle działa" zanim zainwestuje.

### WAVE w profilu DISCOVERY

```
  DISCOVERY — przepływ

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  Mini-SCAN   │────▶│  PULSE lite  │────▶│  Szybki kod  │
  │  15 min      │     │  1 runda     │     │  z kontekstem│
  │  3-5 pytań   │     │  1-2 obszary │     │  2-8h        │
  └──────────────┘     └──────────────┘     └──────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
   „Co muszę            „Jakie pułapki       Działający
    wiedzieć?"           w tym obszarze?"     prototyp
```

### Komponenty WAVE w profilu DISCOVERY

| Komponent | Skala w Discovery | Co konkretnie robisz |
|---|---|---|
| **SCAN** | 15 min, 3-5 obszarów | Odpowiedz na: „co może zabić ten POC?" — nie pełna mapa, tylko miny |
| **PULSE** | 1 runda, 1-2 krytyczne obszary | Szybki research: czy ktoś to próbował? jakie pułapki? |
| **Living Pattern** | v1 — rdzeń, 1-2 strony | Najważniejsze zasady i błędy krytyczne — nic więcej |
| **RtS** | 4 warstwy PEŁNE | Dane (schemat), API (endpointy), Logika (algorytm), UI (ekrany) |
| **RtS placeholdery** | 7 warstw PLACEHOLDER | Bezpieczeństwo, odporność, obserwowalność — jawnie odłożone |
| **FALA** | 1 sesja (szybki blueprint → kod) | Bez formalnego audytu — prosto do kodu z mini-blueprintem |
| **DoD** | 3 pytania | Działa? Pokazywalne? Da się rozbudować? |
| **Decision Log** | 3-5 kluczowych decyzji | Technologia, architektura, zakres — nie więcej |

### Czego NIE robisz w Discovery

```
  ✅ ROBISZ                          ❌ NIE ROBISZ
  ─────────                          ─────────────
  Mini-SCAN (15 min)                 Pełna mapa 15 obszarów
  1 runda PULSE                      3 rundy + auto-doskonalenie
  4 warstwy RtS                      11 warstw pełnych
  3 pytania DoD                      Pełna checklista 11 punktów
  Szybki blueprint (1-2 strony)      Blueprint 30+ stron
  Decision Log (3-5 decyzji)         Kompletny log z historią

  ALE ZAWSZE ROBISZ:
  ✅ 70/30 (nawet jeśli 70% = 15 minut)
  ✅ Człowiek rozumie co buduje (nie vibe coding)
  ✅ Jawne placeholdery (wiesz CO odkładasz)
  ✅ Struktura dająca się rozbudować (nie jednorazowy hack)
```

### Efekt DISCOVERY z WAVE vs bez WAVE

| Wymiar | Bez WAVE (vibe coding) | Z WAVE Discovery |
|---|---|---|
| Czas budowy | 3-8h | 3-8h (tyle samo) |
| Czas przygotowania | 0 min | 15-30 min |
| Jakość kodu | Działa „jakoś" | Działa z fundamentami |
| Rozbudowalność | Wyrzuć i pisz od nowa | Rozbuduj do MVP |
| Decyzje udokumentowane | 0 | 3-5 kluczowych |
| Pułapki znane | Odkrywane na żywo | Zidentyfikowane z góry |
| Koszt przejścia do MVP | Przepisz 80% kodu | Rozszerz istniejący |

### Kluczowa wartość DISCOVERY z WAVE

POC bez WAVE to jednorazowy strzał. Zadziała na demo — i pójdzie do kosza gdy przyjdzie czas na MVP. POC z WAVE Discovery to fundament, na którym stawiasz następne piętro. Te piętnaście minut przygotowania oszczędza tygodnie przebudowy.

---

## 4. Profil BUILD — MVP / Pilot / Beta

### Kiedy używać

Pomysł jest zwalidowany. Klient (lub rynek) powiedział „chcę tego." Budujesz pierwszą wersję, która dostarcza realną wartość — nie demo, nie mockup, ale działający produkt z którego ludzie korzystają. Jeszcze nie skalujesz — testujesz na ograniczonej grupie.

### WAVE w profilu BUILD

```
  BUILD — przepływ

  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────┐
  │  SCAN    │──▶│  PULSE       │──▶│ Projektow.   │──▶│  FALA    │
  │  1h      │   │  2 rundy     │   │ Specyfikacje │   │ 2 sesje  │
  │  6-8     │   │  3-5 obszarów│   │ Decision Log │   │ per moduł│
  │ obszarów │   │              │   │              │   │          │
  └──────────┘   └──────────────┘   └──────────────┘   └──────────┘
       │               │                   │                 │
       ▼               ▼                   ▼                 ▼
  Mapa z          Living Patterns     10-15 decyzji     Kod + testy
  priorytetami    v2 (rdzeń+werf.)    udokumentowanych  + DoD bazowy
```

### Komponenty WAVE w profilu BUILD

| Komponent | Skala w Build | Co konkretnie robisz |
|---|---|---|
| **SCAN** | 1h, 6-8 obszarów | Pełniejsza mapa — włącz bezpieczeństwo, testy, infrastrukturę |
| **PULSE** | 2 rundy, 3-5 obszarów | Rdzeń + weryfikacja porażkami (Runda 2) |
| **Living Pattern** | v2 — rdzeń + weryfikacja | Zasady + matryca błędów + kluczowe metryki |
| **RtS** | 8 warstw PEŁNYCH | Dane, API, Logika, Stany, Integracje, UI, Testy, Meta |
| **RtS placeholdery** | 3 warstwy PLACEHOLDER | Bezpieczeństwo bazowe, odporność i obserwowalność — uproszczone |
| **FALA** | 2 sesje (audyt + kod) | Audyt lekki (Gap Map bez pełnego grafu) + kodowanie |
| **DoD** | 7 punktów | + Testy bazowe + Bezpieczeństwo minimalne + Deployment |
| **Decision Log** | 10-15 decyzji | Architektura, stos, model danych, kluczowe kompromisy |

### Porównanie finansowe — BUILD z WAVE vs bez WAVE

```
  KOSZT BUDOWY MVP (szacunki orientacyjne, 1-3 osoby + AI)
  ═══════════════════════════════════════════════════════════

  BEZ WAVE:
  Tydzień 1-2:  Kodowanie                    ██████████████
  Tydzień 3-4:  Debugowanie                  ████████████████████
  Tydzień 5-6:  Przebudowa (bo fundamenty)   ██████████████████████████
  Tydzień 7-8:  Ponowne kodowanie            ██████████████
  Tydzień 9+:   Testowanie i naprawianie     ████████████████████
                                              ─────────────────────▶
                Łączny koszt: 8-12 tygodni    Dług techniczny: WYSOKI

  Z WAVE BUILD:
  Tydzień 1:    SCAN + PULSE + specyfikacje  ████████████████
  Tydzień 2-3:  FALA (audyt + blueprint)     ████████████
  Tydzień 4-6:  Kodowanie z kontekstem       ██████████████████████
  Tydzień 7:    Testy + DoD                  ████████
                                              ─────────────────────▶
                Łączny koszt: 6-8 tygodni     Dług techniczny: NISKI
```

| Metryka | Bez WAVE | Z WAVE Build | Różnica |
|---|:---:|:---:|:---:|
| Czas do MVP | 8-12 tygodni | 6-8 tygodni | -30% czasu |
| Komponenty bez poprawek | ~40% | ~70% | +30pp jakości |
| Dług techniczny | Wysoki (przebudowa) | Niski (fundamenty) | Jakościowa zmiana |
| Gotowość do skalowania | Przepisanie 50-80% | Rozszerzenie istniejącego | Tygodnie oszczędności |
| Decyzje ślepe | Wiele | 0 (Decision Log) | Pełna przejrzystość |

---

## 5. Profil SCALE — Produkt / Platforma / Enterprise

### Kiedy używać

MVP zadziałał. Użytkownicy korzystają. Czas skalować — więcej funkcji, więcej użytkowników, więcej integracji, produkcyjna jakość. Tu nie ma miejsca na skróty — każdy skrót wraca z odsetkami.

### WAVE w profilu SCALE

```
  SCALE — pełen przepływ WAVE

  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────┐
  │  SCAN    │──▶│  PULSE       │──▶│ Projektow.   │──▶│  FALA    │
  │  2h+     │   │  3 rundy     │   │ Pełne specyf.│   │ 3 sesje  │
  │  10-15   │   │  8-15        │   │ Decision Log │   │ per moduł│
  │ obszarów │   │  obszarów    │   │ 30+ decyzji  │   │ per faza │
  └──────────┘   └──────────────┘   └──────────────┘   └──────────┘
       │               │                   │                 │
       ▼               ▼                   ▼                 ▼
  Pełna mapa     Living Patterns     Kompletna            Kod produkcyjny
  + kolejność    v3 + auto-dosk.     dokumentacja         + 11-punktowe DoD
```

### Komponenty WAVE w profilu SCALE

| Komponent | Skala w Scale | Co konkretnie robisz |
|---|---|---|
| **SCAN** | 2h+, 10-15 obszarów | Pełna mapa z zależnościami i kolejnością |
| **PULSE** | 3 rundy, 8-15 obszarów | Kompletne Living Patterns z auto-doskonaleniem |
| **Living Pattern** | v3 — kompletny | Wszystkie sekcje: wiedza, zasady, błędy, decyzje, metryki, źródła |
| **RtS** | 11 warstw PEŁNYCH | Każde pole zdefiniowane, zero „to zależy" |
| **FALA** | 3 pełne sesje per moduł | Audyt → Blueprint → Kodowanie |
| **DoD** | Pełna checklista 11 punktów | Migracje, testy, flagi, bezpieczeństwo, logi, metryki |
| **Decision Log** | 30+ decyzji z pełną historią | Kontekst, uzasadnienie, odrzucone alternatywy |

---

## 6. Ewolucja profili — od Discovery do Scale

Najważniejsza cecha profili: **są ewolucyjne, nie zastępcze.** Discovery nie jest „wyrzucaną próbą" — jest fundamentem, na którym stawiasz Build. Build nie jest „tymczasowym MVP" — jest bazą, którą rozszerzasz w Scale.

### Ścieżka ewolucji — co się dzieje z artefaktami

```
  DISCOVERY                BUILD                   SCALE
  ═══════════              ═════                    ═════

  Mini-SCAN (3-5) ──────▶  SCAN rozszerzony ──────▶ SCAN pełny
  (dodajesz obszary)       (6-8 obszarów)           (10-15 obszarów)

  LP v1 (rdzeń) ─────────▶ LP v2 (+weryfikacja) ──▶ LP v3 (+finalizacja)
  (PULSE dodaje rundy)     (2 rundy)                (3 rundy + auto-dosk.)

  RtS 4 warstwy ─────────▶ RtS 8 warstw ──────────▶ RtS 11 warstw
  (wypełniasz placeholder) (placeholder → pełne)    (zero placeholderów)

  Blueprint 1-2 str. ────▶ Blueprint 5-10 str. ───▶ Blueprint 30+ str.
  (rozszerzasz, nie        (rozszerzasz, nie        (kompletny per moduł)
   piszesz od nowa)         piszesz od nowa)

  Decision Log 3-5 ──────▶ Decision Log 10-15 ────▶ Decision Log 30+
  (rośnie organicznie)     (rośnie organicznie)     (rośnie organicznie)

  Kod POC ────────────────▶ Kod MVP ───────────────▶ Kod produkcyjny
  (rozbudowujesz,          (rozbudowujesz,          (skalujesz, nie
   nie wyrzucasz)            nie wyrzucasz)            przepisujesz)
```

### Koszt ewolucji vs koszt od zera

```
  SCENARIUSZ A: Trzy oddzielne budowy (bez ewolucji)

  POC:    █████████████████             (wyrzucony)
  MVP:    ████████████████████████████  (wyrzucony)
  Produkt:████████████████████████████████████████████████
          ─────────────────────────────────────────────▶
          Łączny koszt: 3× pełna budowa
          Łączne marnotrawstwo: ~60% (dwa wyrzucone POC/MVP)

  SCENARIUSZ B: Ewolucja profili WAVE

  Discovery: ████████
  Build:     ────────████████████████
  Scale:     ────────────────────────████████████████████████
             ─────────────────────────────────────────────▶
             Łączny koszt: 1× budowa z rozszerzeniami
             Marnotrawstwo: ~5% (tylko jawne placeholdery do wypełnienia)
```

| Scenariusz | Łączny czas | Marnotrawstwo | Jakość fundamentów |
|---|:---:|:---:|:---:|
| A: Trzy oddzielne budowy | 3× | ~60% wyrzuconego kodu | Każda budowa od zera |
| B: Ewolucja WAVE | 1,4× | ~5% placeholderów | Fundamenty od dnia 1 |
| **Oszczędność B vs A** | **~55% czasu** | **~55pp marnotrawstwa** | **Ciągłość architektury** |

---

## 7. Porównanie zestawione — czas, zakres, koszt, jakość

### Tabela główna — wszystkie wymiary

| Wymiar | DISCOVERY | BUILD | SCALE |
|---|---|---|---|
| **Czas przygotowania** | 2-4h | 41-73h (~1-2 tyg.) | 163-385h (miesiące) |
| **Czas egzekucji** | 1,5-3h | 14-35h (~1 tyg.) | 70-380h (miesiące) |
| **Czas łączny** | 3,5-7h (1-5 dni) | 55-108h (4-8 tyg.) | 233-765h (3-12 mies.) |
| **Proporcja P/E** | ~57/43 | ~70/30 | 50-70 / 30-50 |
| **Budżet (czas + AI)** | ~0 (czas własny) | 5-20 tys. € | 50-500 tys. € |
| **Jakość 1. przejścia** | ~50% bez poprawek | ~70% bez poprawek | ~85% bez poprawek |
| **Pokrycie testami** | Brak / manualne | Bazowe (happy path) | Pełne (unit + E2E) |
| **Bezpieczeństwo** | Placeholder | Bazowe (auth + walidacja) | Pełne (pen-test, RODO) |
| **Dokumentacja** | 1-3 pliki | 10-20 plików | 50+ plików |
| **Decision Log** | 3-5 decyzji | 10-15 decyzji | 30+ decyzji |
| **Living Patterns** | 1-2 × v1 | 3-5 × v2 | 8-15 × v3 |
| **RtS** | 4 warstwy pełne | 8 warstw pełnych | 11 warstw pełnych |
| **DoD** | 3 pytania | 7 punktów | 11 punktów |
| **Rozbudowalność** | Do MVP bez przebudowy | Do produktu bez przebudowy | Do platformy enterprise |
| **Dług techniczny** | Jawny (placeholdery) | Niski | Minimalny |

### Diagram — jakość w czasie

```
  Jakość
  kodu
    │
 95%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·  SCALE z WAVE
    │                                            · ·
 85%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · ·
    │                              · · ·
 70%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · · ·                       BUILD z WAVE
    │                · · ·
 50%├─ ─ ─ ─ · · · ·                                     DISCOVERY z WAVE
    │    · · ·
    │  · ·
    │ · ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─          Bez WAVE
 30%├ ·     · · · · · · · · ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · ·   (plateau + spadek)
    │              ↑ „Spaghetti Point"           · ·
 20%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·
    │
    ├──────────┬──────────┬──────────┬──────────┬─────▶ Czas
    0       1 mies.    3 mies.    6 mies.    12 mies.
```

---

## 8. Kiedy który profil — drzewo decyzyjne

```
  START: Masz pomysł na rozwiązanie
  │
  ├── Czy wiesz czy pomysł ma sens technicznie?
  │   │
  │   ├── NIE ──────────────▶ DISCOVERY
  │   │                       „Zbuduj dowód w 1-5 dni"
  │   │
  │   └── TAK
  │       │
  │       ├── Czy masz użytkowników / klientów gotowych testować?
  │       │   │
  │       │   ├── NIE ──────▶ DISCOVERY
  │       │   │               „Zwaliduj z rynkiem, nie w głowie"
  │       │   │
  │       │   └── TAK
  │       │       │
  │       │       ├── Czy rozwiązanie musi obsługiwać >100 użytkowników?
  │       │       │   │
  │       │       │   ├── NIE ──▶ BUILD
  │       │       │   │           „MVP dla ograniczonej grupy"
  │       │       │   │
  │       │       │   └── TAK
  │       │       │       │
  │       │       │       ├── Czy masz budżet i czas na miesiące pracy?
  │       │       │       │   │
  │       │       │       │   ├── NIE ──▶ BUILD (potem SCALE)
  │       │       │       │   │           „Zacznij od MVP, ewoluuj"
  │       │       │       │   │
  │       │       │       │   └── TAK ──▶ SCALE
  │       │       │       │               „Buduj produkt docelowy"
```

### Trzy zasady wyboru profilu

| Zasada | Opis |
|---|---|
| **Waliduj zanim budujesz** | Jeśli nie wiesz czy pomysł ma sens — DISCOVERY. Zawsze. Nawet jeśli „czujesz" że ma. |
| **Ewoluuj zamiast przepisywać** | Zacznij od Discovery, przesuń do Build gdy pomysł się potwierdzi, potem do Scale. Nie buduj Scale od razu. |
| **Profil to nie wyrok** | Możesz zmienić profil w trakcie. Discovery okazało się większe niż myślałeś? Przesuń do Build. Build nie potrzebuje Scale? Zostań w Build. |

---

## 9. Aksjomaty nie skalują się — co jest niepodzielne

Profil zmienia skalę komponentów. Ale jest zestaw elementów, które nie zmieniają się NIGDY — niezależnie od profilu. Są niepodzielne, jak atom (w pierwotnym sensie tego słowa).

### Co jest stałe we wszystkich profilach

```
  NIEPODZIELNE (identyczne w Discovery, Build i Scale):
  ════════════════════════════════════════════════════

  ✅ Zasada 70/30 jako GRAWITACJA
     Proporcja ciąży ku 70/30 — w Discovery ląduje na ~60/40,
     w Build na ~70/30, w dużym Scale na ~50/50.
     Ale ZAWSZE przygotowanie ≥ 50%. Zero „vibe codingu".

  ✅ Człowiek kieruje, AI wzmacnia
     Nawet w POC — rozumiesz co budujesz, nie vibecoding

  ✅ Buduj kompletnie, aktywuj progresywnie
     Nawet POC ma strukturę dającą się rozbudować

  ✅ Jawne placeholdery
     Wiesz CO odkładasz (nie „zapomnieliśmy", lecz „świadomie później")

  ✅ Test AANP
     Każdy proces ma Aktora, Akcję, Narzędzie, Produkt

  ✅ Zasada DooR
     Przejście między etapami = kompletność artefaktu
     (nawet jeśli artefakt to 2-stronicowy blueprint)

  ✅ Decision Log
     Nawet 3 decyzje to Decision Log, nie „pamiętam w głowie"

  ✅ Trzy poziomy H-AI
     DataPrep → Prompt2Data → Prompt2Prompt
     Nawet w Discovery: zbierz kontekst → daj zadanie → oceń wynik
```

### Co się skaluje

| Element | Discovery | Build | Scale |
|---|:---:|:---:|:---:|
| Liczba obszarów SCAN | 3-5 | 6-8 | 10-15 |
| Rundy PULSE | 1 | 2 | 3 |
| Wersja Living Pattern | v1 | v2 | v3 |
| Warstwy RtS pełne | 4 | 8 | 11 |
| Sesje FALA | 1 | 2 | 3 |
| Punkty DoD | 3 | 7 | 11 |
| Wpisy Decision Log | 3-5 | 10-15 | 30+ |
| Głębokość dokumentacji | Minimalna | Umiarkowana | Kompletna |

---

*Dokument opracowany: 11 marca 2026*  
*Wersja: 1.2*  
*Autor koncepcji: Przemek Zieliński*  
*Opracowanie: Claude Opus 4.6*  
*Licencja: CC BY-SA 4.0*  
*Dokument towarzyszący do: WAVE Dokument Referencyjny Software Engineering v1.2*
