# RtS — Requisite-to-Start
## Jedenaście warstw informacji, które WAVE musi wyprodukować zanim AI siada do pisania kodu

**Element metodyki WAVE** | **Wersja:** 3.0 | **Data:** 1 marca 2026  
**Charakter:** Generyczny — działa dla dowolnego modułu. Przykłady ilustracyjne z HIVE.

---

## RtS w ekosystemie WAVE

W Scrumie istnieje **DoD — Definition of Done**: checklista zamykająca etap, odpowiadająca na pytanie *„kiedy możesz powiedzieć, że skończyłeś?"*

WAVE wprowadza symetryczny koncept na początku: **RtS — Requisite-to-Start**. Nie „czy jesteśmy gotowi?" (stan umysłu) — ale **„czy istnieje to, co wymagane?"** (artefakt, dokument, dane). AI nie ma stanu umysłu — ma okno kontekstowe. Albo widzi jedenaście warstw, albo zgaduje.

```
 ┌──────────────────────────────────────────────────────────┐
 │                    ETAP W WAVE                           │
 │                                                          │
 │  ✅ RtS                    Sesja kodowania          DoD  │
 │  (Requisite-to-Start)      AI pisze kod         (Done)   │
 │  „Czy blueprint            strumieniowo,        „Czy     │
 │   ma 11 warstw,            bez zatrzymywania    moduł    │
 │   każda kompletna?"        się"                 przeszedł│
 │                                                 testy?"  │
 │  ◄── OTWIERA ──────────── TRWA ──────── ZAMYKA ──►       │
 └──────────────────────────────────────────────────────────┘
```

**RtS to nie jest dokument planistyczny.** To jest specyfikacja techniczna — blueprint, który AI czyta i zamienia w kod. Każda warstwa odpowiada na jedno pytanie, na które AI nie powinno odpowiadać sobie samo.

**Dlaczego „Requisite" a nie „Prerequisite"?** „Pre-" i „to-Start" mówią to samo: *przed*. Jak „PIN number" — P już znaczy Personal. „Requisite-to-Start" mówi czysto: *to co jest wymagane żeby wystartować*. Trzy litery — RtS — symetryczne z DoD. Łatwo zapamiętać, łatwo powiedzieć.

**Dlaczego nie DoR (Definition of Ready)?** DoR w Scrumie jest miękkie — checklista na karteczce „czy zadanie jest jasne". RtS jest twarde — jedenaście warstw z precyzją do typu pola w bazie danych. To nie jest pytanie o gotowość zespołu. To jest pytanie o kompletność wsadu. AI nie trzeba pytać „czy rozumiesz?" — trzeba mu dać kompletny kontekst.

---

## Jedenaście warstw RtS — widok ogólny

> **Kolejność warstw nie jest przypadkowa.** Każda następna zależy od poprzedniej. Warstwa 2 (API) opisuje co system robi z danymi z Warstwy 1. Warstwa 3 (logika) opisuje jak system przetwarza to co API przyjmuje. Warstwa 9 (bezpieczeństwo) mówi czego NIE robić z tym co opisały warstwy 1–8. Zmiana kolejności = luki w definicji.

| # | Warstwa | AI wie... | Pytanie kontrolne |
|:---:|---|---|---|
| ✅ 1 | **Dane** — schematy tabel | **NA CZYM operuje** | Każde pole ma typ, ograniczenia i opis? |
| ✅ 2 | **API** — endpointy | **CO system robi na zewnątrz** | Każdy endpoint ma sygnaturę z typami i kodami błędów? |
| ✅ 3 | **Logika** — algorytmy | **JAK system myśli** | Każdy wzór ma parametry, zakresy i edge case'y? |
| ✅ 4 | **Stany** — flagi, crony, eventy | **KIEDY system reaguje** | Flagi, crony i eventy mają warunki i fallbacki? |
| ✅ 5 | **Integracje** — zależności | **Z CZYM system rozmawia** | Import/eksport do innych modułów jest jasny? |
| ✅ 6 | **UI** — komponenty | **CO użytkownik widzi** | Każdy komponent ma dane, akcje i stany? |
| ✅ 7 | **Testy** — seedy, scenariusze | **JAK zweryfikować** | Są testy z konkretnymi liczbami? |
| ✅ 8 | **Meta** — stos, konwencje | **W CZYM pisać** | Stos, konwencje i struktura plików ustalone? |
| ✅ 9 | **Bezpieczeństwo** — walidacja | **CZEGO NIE ROBIĆ** | Reguły sanityzacji i ścieżki ataku zamknięte? |
| ✅ 10 | **Odporność** — obsługa błędów | **CO GDY COŚ PÓJDZIE ŹLE** | Format błędów, retry i fallbacki jednolite? |
| ✅ 11 | **Obserwowalność** — logi, metryki | **CO SYSTEM MÓWI O SOBIE** | Wiadomo co logować, mierzyć i kiedy alarmować? |
| ✅ — | **Próbka kodu** *(załącznik do 8)* | **STYL zamiast zgadywania** | AI widzi realny plik z istniejącego modułu? |

> **Zasada RtS:** Jeśli na pytanie o jakikolwiek element blueprintu możesz odpowiedzieć „to zależy" — blueprint nie jest gotowy. Wróć do warstwy, w której pojawia się „to zależy", i uzupełnij.

---

## Struktura każdej warstwy

Każda z jedenastu warstw ma tę samą budowę:

```
  DEFINICJA (generyczna)
    Co to jest          — jedno zdanie
    Dlaczego krytyczne  — co się stanie bez tego
    Format wymagany     — jak blueprint musi to opisać
    Checklist           — lista do odhaczenia

  PRZYKŁAD → [NAZWA MODUŁU]
    Konkretna ilustracja na wybranym module
    (w tym dokumencie: HIVE — ale przy blueprincie innego
    modułu zastąp własnymi danymi)
```

Czytelnik powinien potrafić wyciąć sekcję „Przykład" i użyć samej definicji do dowolnego modułu.


---

## Warstwy szczegółowo

---

## 1. WARSTWA DANYCH — Schematy tabel z typami i ograniczeniami

### Definicja

**Co to jest:** Dokładna definicja każdej tabeli, każdego pola, każdego typu, każdego ograniczenia. Nie „encja ma score" — ale precyzyjny typ z zakresem, ograniczeniami i wartością domyślną.

**Dlaczego krytyczne:** AI które widzi „tabela z polami" pisze `CREATE TABLE x (id INT, content TEXT)` i potem trzeba dodawać pola, typy, indeksy, relacje. AI które widzi kompletny schemat pisze go raz, dobrze.

**Format wymagany — dla każdej tabeli:**

```
TABELA: [nazwa_tabeli]

  POLE          TYP                  OGRANICZENIA                    OPIS
  ──────────────────────────────────────────────────────────────────────────
  [pole_1]      [typ z precyzją]     [NOT NULL/NULLABLE, DEFAULT,    [co przechowuje]
                                      CHECK, FK, INDEX...]

  INDEKSY:
    [nazwa]    ([pola])              ← [które zapytanie go używa]

  RELACJE:
    [pole]     → [tabela.pole]       ([krotność: ONE-TO-MANY, etc.])
```

**Checklist gotowości:**

- [ ] Każde pole ma typ z precyzją (VARCHAR(100), nie VARCHAR)
- [ ] Każde pole ma ograniczenia (NOT NULL / NULLABLE / DEFAULT / CHECK)
- [ ] Każda relacja ma jawny FK z kierunkiem i krotnością
- [ ] Każdy indeks ma uzasadnienie (które zapytanie go używa)
- [ ] Każdy ENUM ma zamkniętą listę wartości
- [ ] Podane są seedowane dane startowe (jeśli moduł wymaga danych na start)

**Sygnał niekompletności:** ❌ „Encja ma pole score" → AI nie wie: INT? FLOAT? DECIMAL? Zakres? Default?

### Przykład → HIVE

```
TABELA: hint_repository

  POLE                  TYP                    OGRANICZENIA                          OPIS
  ─────────────────────────────────────────────────────────────────────────────────────────
  id                    UUID                   PK, auto-generated                    -
  discipline            VARCHAR(100)           NOT NULL, INDEX                       klucz dyscypliny
  screen_type           VARCHAR(50)            NOT NULL, INDEX                       typ ekranu
  hint_content          TEXT                   NOT NULL, MIN 10 chars                treść podpowiedzi
  hint_type             ENUM                   ('suggestion','warning','anti_pattern') DEFAULT 'suggestion'
  source                ENUM                   ('manual','crowd','ai','ai_edited','transfer') NOT NULL
  author_id             UUID                   FK → users.id, NULLABLE              kto dodał
  usage_count           INT                    DEFAULT 0, >= 0                       ile razy użyty
  modification_count    INT                    DEFAULT 0, >= 0                       ile razy zmodyfikowany
  dismiss_count         INT                    DEFAULT 0, >= 0                       ile razy odrzucony
  confidence_score      DECIMAL(5,4)           DEFAULT 0.0, CHECK(0.0–1.0)          obliczany dynamicznie
  parent_hint_id        UUID                   FK → hint_repository.id, NULLABLE     drzewo wariantów
  last_used_at          TIMESTAMP              NULLABLE                              do temporal decay
  archived_at           TIMESTAMP              NULLABLE                              NULL = aktywny
  created_at            TIMESTAMP              NOT NULL, DEFAULT NOW()               -
  updated_at            TIMESTAMP              NOT NULL, auto-update                 -

  INDEKSY:
    idx_discipline_screen    (discipline, screen_type)       ← główne zapytanie getHints
    idx_confidence           (confidence_score DESC)          ← sortowanie wyników
    idx_author               (author_id)                      ← diversity guard
    idx_archived             (archived_at)                    ← filtrowanie aktywnych

  RELACJE:
    author_id    → users.id (MANY-TO-ONE)
    parent_hint  → hint_repository.id (SELF-REFERENCING, NULLABLE)
```

---

## 2. WARSTWA API — Endpointy z sygnaturami, typami i kodami błędów

### Definicja

**Co to jest:** Kompletna definicja każdego endpointu: ścieżka, metoda HTTP, parametry wejściowe z typami, obiekt odpowiedzi z typami, kody błędów, reguły autoryzacji i reguły biznesowe.

**Dlaczego krytyczne:** Endpoint bez precyzyjnej sygnatury to zaproszenie do niespójności. AI napisze siedem endpointów — każdy z innym formatem odpowiedzi, inną konwencją nazewnictwa parametrów. Wszystkie „poprawne" — żaden spójny z pozostałymi.

**Format wymagany — dla każdego endpointu:**

```
ENDPOINT: [nazwa]

  ŚCIEŻKA:      [METHOD] [path]
  AUTORYZACJA:   [kto ma dostęp]
  RATE LIMIT:    [limit per user/rola]

  PARAMETRY WEJŚCIOWE:
    [param]      [TYP]    [REQUIRED/OPTIONAL]    [opis, DEFAULT jeśli optional]

  ODPOWIEDŹ (200 OK):
    { [pełna struktura z typami dla każdego pola, w tym zagnieżdżonych] }

  KODY BŁĘDÓW:
    [kod]  [kiedy]

  REGUŁY BIZNESOWE:
    [lista reguł specyficznych dla tego endpointu — sortowanie, filtrowanie, fallback]
```

**Checklist gotowości:**

- [ ] Każdy parametr ma typ, opcjonalność i domyślną wartość
- [ ] Każdy obiekt odpowiedzi ma typy dla wszystkich pól (w tym zagnieżdżonych)
- [ ] Kody błędów pokrywają: walidacja, autoryzacja, brak danych, rate limit, serwer
- [ ] Reguły biznesowe wylistowane TU, nie w osobnym dokumencie
- [ ] Jasne co się dzieje z parametrami opcjonalnymi gdy nie podane
- [ ] Jasne co się dzieje na pustym zbiorze (404? pusta lista? fallback?)

### Przykład → HIVE

```
ENDPOINT: getHints

  ŚCIEŻKA:     GET /api/v1/hive/hints
  AUTORYZACJA:  Bearer token, rola: mentor | admin
  RATE LIMIT:   100 req/min per user

  PARAMETRY WEJŚCIOWE (query):
    discipline        STRING    REQUIRED    "bieganie", "skateboarding"...
    screen_type       STRING    REQUIRED    "challenge_feedback", "entry_form"...
    context           JSON      OPTIONAL    {challenge_id, challenge_type}
    learner_context   JSON      OPTIONAL    {skill_level: ENUM, attempt_number: INT,
                                             previous_feedback: STRING[],
                                             mastery_score: FLOAT (0.0–1.0)}
    limit             INT       OPTIONAL    DEFAULT 5, MAX 20

  ODPOWIEDŹ (200 OK):
    {
      hints: [{
        id: UUID, content: STRING, hint_type: ENUM, source: ENUM,
        confidence: FLOAT, parent_hint_id: UUID|null, transfer_source: STRING|null
      }],
      meta: {
        total_available: INT,
        discipline_maturity: ENUM("cold"|"warming"|"mature"|"saturated"),
        dominant_layer: ENUM("manual"|"crowd"|"ai"|"transfer")
      }
    }

  KODY BŁĘDÓW:
    400  Invalid discipline or screen_type
    401  Unauthorized
    403  Role not permitted
    429  Rate limit exceeded
    500  Internal server error

  REGUŁY BIZNESOWE:
    1. Sortowanie: weighted_confidence DESC
    2. Filtrowanie: archived_at IS NULL
    3. Flaga DIVERSITY_GUARD ON: top 3 confidence + 2 najnowsze
    4. Flaga CONTEXT_AWARE ON + learner_context: filtruj po skill_level
    5. Fallback: 0 crowd → Warstwa 1 → 0 Warstwa 1 → Warstwa 3 (AI generate + cache)
```

---

## 3. WARSTWA LOGIKI — Wzory, algorytmy i reguły z parametrami

### Definicja

**Co to jest:** Każdy obliczany wynik opisany jako wzór z konkretnymi parametrami, zakresami i edge case'ami. Nie „oblicz score na podstawie użyć" — ale wzór z parametrami prowadzący do jednej implementacji.

**Dlaczego krytyczne:** „Oblicz trafność na podstawie interakcji" to jedno zdanie prowadzące do dziesięciu różnych implementacji. Wzór z parametrami prowadzi do jednej.

**Format wymagany — dla każdego algorytmu:**

```
ALGORYTM: [nazwa]

  WZÓR:           [formuła matematyczna z nazwanymi zmiennymi]
  ZMIENNE:        [każda zmienna: typ, zakres min–max, źródło]
  MODYFIKATORY:   [opcjonalne mnożniki/modyfikatory z warunkami włączenia]
  EDGE CASES:     [co gdy NULL, zero, pierwszy rekord, jeden element]
  KIEDY LICZYĆ:   [per-request / cron / event-driven]
  GDY FLAGA OFF:  [co się dzieje — pomijany? domyślna wartość?]
  TEST:           [konkretne liczby: INPUT → EXPECTED OUTPUT]
```

**Checklist gotowości:**

- [ ] Każdy wzór ma jawne zmienne z typami i zakresami
- [ ] Każdy edge case opisany (NULL, zero, pierwsze użycie, jeden rekord)
- [ ] Jasne kiedy przeliczać (per-request, cron, event-driven)
- [ ] Podany min. jeden test weryfikacyjny z konkretnymi liczbami
- [ ] Jasne co się dzieje gdy flaga wyłączona

### Przykład → HIVE

```
ALGORYTM: Kalkulacja weighted_confidence

  WZÓR BAZOWY:
    base = (usage × 1.0 + modification × 0.5) / (usage + modification + dismiss + 1)

  MODYFIKATOR: Temporal Decay (flaga: HIVE_TEMPORAL_DECAY)
    temporal_factor = 0.5 ^ (days_since_last_use / half_life)
    half_life: DEFAULT 180, konfigurowalny per dyscyplina

  MODYFIKATOR: Mentor Weight (flaga: HIVE_MENTOR_WEIGHT)
    mentor_factor = mentor_weights[author_id].weight
    Zakres: 0.5–2.0, DEFAULT 1.0

  EDGE CASES:
    last_used_at IS NULL → temporal_factor = 1.0
    author_id IS NULL    → mentor_factor = 1.0

  WYNIK: weighted_confidence = base × temporal_factor × mentor_factor

  TEST: usage=20, dismiss=0, mod=0, 30 dni, half_life=180, mentor=1.5:
    base=0.952, temporal=0.891, weighted=0.952 × 0.891 × 1.5 = 1.272
```

---

## 4. WARSTWA STANÓW I PRZEJŚĆ — Feature flags, crony, eventy

### Definicja

**Co to jest:** Wszystkie stany systemu, warunki przejść, zadania cykliczne i zdarzenia wyzwalające akcje. „System nerwowy" modułu — bez niego AI nie wie kiedy co się odpala.

**Format wymagany:**

```
FEATURE FLAGS:
  [nazwa]    [domyślnie]    [typ]    [warunek włączenia]
  MECHANIKA: przechowywanie, odczyt (cache?), zmiana (kto, jak), audyt

CRON JOBS:
  [nazwa]    [częstotliwość]    [flaga]    [co robi]
  DLA KAŻDEGO: warunek, co gdy OFF, co gdy brak danych, timeout, retry

EVENTS:
  [zdarzenie]    [wyzwalacz]    [akcja]    [warunek flagi]
```

**Checklist gotowości:**

- [ ] Każda flaga: nazwa, typ, domyślna, warunek włączenia, mechanika przechowywania
- [ ] Każdy cron: częstotliwość, warunek, co robi, timeout, retry
- [ ] Każdy event: wyzwalacz, akcja, warunek flagi
- [ ] Jasne jak flagi odczytywane (per-request? cache? odświeżanie co ile?)
- [ ] Zmiany flag audytowane (kto, kiedy, co)

### Przykład → HIVE

```
FLAGS:
  HIVE_PASSIVE_SIGNALS      ON     boolean    od dnia pierwszego
  HIVE_TEMPORAL_DECAY       OFF    boolean    > 50 hintów w dyscyplinie
  HIVE_ANTI_PATTERNS        OFF    boolean    > 100 feedbacków łącznie
  HIVE_GARBAGE_COLLECTION   OFF    boolean    po 6 miesiącach
  HIVE_DIVERSITY_GUARD      OFF    boolean    > 20 mentorów w dyscyplinie
  HIVE_MENTOR_WEIGHT        OFF    boolean    > 20 mentorów
  HIVE_CONTEXT_AWARE        OFF    boolean    z User Mastery
  HIVE_LEARNER_FEEDBACK     OFF    boolean    z AI, Faza 1
  HIVE_CROSS_DISCIPLINE     OFF    boolean    > 10 dyscyplin
  HIVE_PATH_HINTS           OFF    boolean    z danymi o ścieżkach, Faza 2
  HIVE_REPLAY               OFF    boolean    > 50 feedbacków eksperta
  HIVE_DRIFT_DETECTION      OFF    boolean    ustalona norma
  HIVE_SEASONS              OFF    boolean    po 6 miesiącach

  Przechowywanie: tabela hive_config → JSON. Cache w pamięci, odświeżanie co 60s.
  Zmiana: PUT /api/v1/admin/hive/flags/{name}. Rola: admin. Audyt: audit_log.

CRON JOBS:
  recalc_mentor_weights     co 24h (3:00)    MENTOR_WEIGHT         przelicza wagi
  garbage_collection        co 7 dni (ndz)   GARBAGE_COLLECTION    archiwizuje martwe hinty
  anti_pattern_detect       co 24h (4:00)    ANTI_PATTERNS         konwertuje odrzucane
  season_report             co 90 dni        SEASONS               raport kwartalny
  Timeout: 5 min. Retry: 1× po 10 min. Flaga OFF → skip + log.

EVENTS:
  hint_used        → usage_count++, last_used_at = NOW()
  hint_modified    → modification_count++, twórz child hint
  hint_dismissed   → dismiss_count++
  hint_custom      → nowy rekord, source='crowd'
```

---

## 5. WARSTWA INTEGRACJI — Zależności od innych modułów i serwisów

### Definicja

**Co to jest:** Mapa tego, co moduł importuje (potrzebuje od reszty) i co eksportuje (udostępnia innym). Bez tego AI pisze moduł w izolacji i potem nie pasuje do reszty.

**Format wymagany:**

```
IMPORT (co moduł potrzebuje):
  [źródło]    [co pobiera]    [jak uzyskuje]    [co gdy niedostępne]

EKSPORT (co moduł udostępnia):
  [odbiorca]    [co udostępnia]    [przez jaki interfejs]

SERWISY ZEWNĘTRZNE:
  [serwis]    [co robi]    [URL, auth, timeout, retry, fallback]
  [prompt template jeśli LLM — dosłownie, nie opis]
```

**Checklist gotowości:**

- [ ] Każda zależność wejściowa: źródło, co pobiera, format, jak
- [ ] Każda zależność wyjściowa: odbiorca, co udostępnia, interfejs
- [ ] Serwisy zewnętrzne: URL, auth, timeout, retry, fallback
- [ ] Prompt templates dla AI podane dosłownie
- [ ] Jasne co gdy zależność niedostępna (fallback? error? graceful degradation?)

### Przykład → HIVE

```
IMPORT:
  users (auth)       → user_id, role              JWT token w headerze
  challenges         → challenge_id, discipline    query param w context
  user_mastery       → skill_level, mastery_score  query param w learner_context
  LLM API            → generowanie hintów W3       POST, timeout 10s, retry 1×

EKSPORT:
  ekran feedbacku    → getHints + recordAction     REST API
  ekran formularza   → getHints + recordAction     REST API
  panel admina       → flagi, diagnostyka           REST API (admin)
  TACIT (przyszły)   → pary hint→korekta           event bus / polling
  LEARNIEE (przyszły)→ wzorce cross-discipline      event bus / polling

LLM API: fallback jeśli timeout → Warstwa 1 (predefiniowane)
```

---

## 6. WARSTWA UI — Mapa komponentów z danymi i akcjami

### Definicja

**Co to jest:** Specyfikacja tego, co użytkownik widzi i co może zrobić. Nie mockup — ale lista komponentów z danymi wejściowymi, akcjami i stanami.

**Format wymagany — dla każdego komponentu:**

```
KOMPONENT: [Nazwa]

  GDZIE UŻYWANY:    [ekrany / konteksty]
  DANE WEJŚCIOWE:   [props z typami]
  STANY WEWNĘTRZNE: [zmienne stanu]
  WYŚWIETLANIE:     [co widać — warunkowe warianty, stany: pusty/loading/error]
  AKCJE → API:      [co użytkownik klika → jaki endpoint → jaki feedback]
  RESPONSYWNOŚĆ:    [desktop vs mobile]
```

**Checklist gotowości:**

- [ ] Każdy komponent: nazwa, gdzie używany, dane wejściowe z typami
- [ ] Stany wewnętrzne komponentu opisane
- [ ] Każda akcja: co widzi → co klika → jakie API → jaki feedback
- [ ] Stany pustych danych, ładowania i błędów opisane
- [ ] Wygląd warunkowy (typ → wygląd) opisany
- [ ] Responsywność: co się zmienia na mobile

### Przykład → HIVE

```
KOMPONENT: HintDisplay

  GDZIE: ekran feedbacku, ekran formularza, plan tygodniowy
  PROPS: hints: Hint[], loading: boolean, error: string|null
  STANY: expandedHintId, hoveredHintId, hoverStartTime

  WYŚWIETLANIE:
    suggestion → biała karta, szary tekst
    warning → żółta karta, ikona
    anti_pattern → czerwona karta, "Unikaj tego"
    transfer → notatka "Na podstawie wzorców z [dyscyplina]"
    Pusty: "Brak podpowiedzi — pisz od siebie!"
    Loading: skeleton loader (3 karty)
    Error: komunikat + "Spróbuj ponownie"

  AKCJE → API:
    "Użyj"          → recordAction(used)
    "Edytuj" + zapis → recordAction(modified, {final_text})
    "Odrzuć"         → recordAction(dismissed)
    Nowy od zera     → recordAction(custom_added, {content})
    Hover > 2s       → zbierz hover_time (pasywne)

  RESPONSYWNOŚĆ: Desktop: max-width 600px. Mobile: full-width, swipe.
```

---

## 7. WARSTWA TESTÓW — Dane startowe i scenariusze weryfikacyjne

### Definicja

**Co to jest:** Jakie dane istnieją na starcie (seedy) i jak zweryfikować że kod działa (testy z oczekiwanymi wynikami).

**Format wymagany:**

```
SEEDS (dane startowe):
  [zbiór]    [ile rekordów]    [format: JSON/SQL]    [opis]

TESTY JEDNOSTKOWE (min. 5 per algorytm):
  TEST [N]: [nazwa scenariusza]
    INPUT:   [konkretne wartości]
    FLAGS:   [które ON, które OFF]
    EXPECT:  [dokładny wynik liczbowy]

TESTY E2E (min. 2 per główny flow):
  TEST E2E-[N]: [opis flow]
    KROK 1:  [request] → [expected response]
    KROK 2:  [request] → [expected response]
    ...
```

**Checklist gotowości:**

- [ ] Seedy gotowe w formacie importowalnym (JSON/SQL)
- [ ] Konfiguracja domyślna: flagi, parametry
- [ ] Min. 5 testów jednostkowych per algorytm (w tym edge cases)
- [ ] Min. 2 testy E2E per główny flow
- [ ] Każdy test: INPUT + FLAGS + EXPECTED OUTPUT z liczbami
- [ ] Testy pokrywają: happy path, edge cases, flagi ON/OFF, puste dane

### Przykład → HIVE

```
SEEDS:
  Predefiniowane hinty    ~50–60 rekordów    JSON    10–12 dyscyplin × 4–5 ekranów
  Klastry dyscyplin       ~8 klastrów        JSON    endurance, board, combat...
  Konfiguracja domyślna   1 rekord           JSON    flagi, half_life: 180

TESTY:
  TEST 1: Nowy hint, zero interakcji
    INPUT: usage=0, mod=0, dismiss=0, last_used=NULL | FLAGS: wszystkie OFF
    EXPECT: weighted=0.0

  TEST 2: Popularny, aktywny, ważny mentor
    INPUT: usage=20, mod=2, dismiss=1, last_used=wczoraj, mentor.weight=1.5
    FLAGS: TEMPORAL_DECAY=ON, MENTOR_WEIGHT=ON
    EXPECT: weighted=1.364

  TEST 3: Stary, porzucony
    INPUT: usage=5, dismiss=15, last_used=365 dni | FLAGS: TEMPORAL_DECAY=ON
    EXPECT: weighted=0.056

  TEST E2E-1: Pełny flow mentor→hint→edycja→zapis
  TEST E2E-2: Admin zmienia flagę → efekt natychmiastowy
```

---

## 8. WARSTWA META — Stos, konwencje, struktura plików

### Definicja

**Co to jest:** Decyzje techniczne wpływające na cały moduł. Bez tego AI pisze w Pythonie gdy reszta jest w TypeScript albo używa snake_case gdy reszta jest w camelCase.

**Format wymagany:**

```
STOS:         [backend, baza, frontend, API format, auth, hosting]
KONWENCJE:    [tabele, kolumny, endpointy, komponenty, pliki, zmienne]
STRUKTURA:    [drzewo plików modułu — przed pisaniem, nie po]
```

**Checklist gotowości:**

- [ ] Stos technologiczny zdefiniowany
- [ ] Konwencje nazewnictwa — jedno źródło prawdy
- [ ] Struktura plików modułu ustalona
- [ ] Format API (REST/GraphQL) ustalony
- [ ] Mechanizm autentykacji ustalony

### Załącznik 8A: Próbka kodu

AI pisze dramatycznie lepiej gdy widzi **realny plik z istniejącego modułu** — nie opis konwencji, ale żywy kod. Dołącz do blueprintu:

```
  □ Jeden kompletny kontroler z istniejącego modułu
  □ Jeden kompletny serwis
  □ Jeden model
  □ Jeden middleware
  □ Jeden plik testowy
  □ Konfiguracja bazy danych / ORM
  □ Lista istniejących helperów (żeby AI nie duplikowało)
```

Jeśli moduł jest jednym z pierwszych w projekcie — AI powinno NAJPIERW wygenerować wzorcowy moduł-referencję z prostym endpointem, a potem pisać właściwy moduł w tym samym stylu. 30 minut inwestycji = godziny oszczędności na spójności.


---

## 9. WARSTWA BEZPIECZEŃSTWA — Walidacja, sanityzacja, zamknięte ścieżki

### Definicja

**Co to jest:** Jawna lista reguł mówiących AI czego NIE robić: jakie dane są niebezpieczne, jak je sanityzować, jakie ścieżki ataku zamknąć, co nigdy nie wychodzi w odpowiedzi.

**Dlaczego krytyczne:** AI domyślnie pisze „happy path" — zakłada prawidłowe dane, uczciwego użytkownika, brak ataku. Bez jawnych reguł AI nie doda sanityzacji, nie obetnie nierozsądnych wartości, nie zamknie ścieżek bocznych. To nie jest rozszerzenie Warstwy 2 — dotyczy KAŻDEGO endpointu, KAŻDEGO pola, KAŻDEGO flow jednocześnie.

**Format wymagany:**

```
WALIDACJA WEJŚCIA:
  [pole/param]    [reguła: whitelist/zakres/typ/max length]    [co jeśli złamana]

AUTORYZACJA:
  [reguła]    [implementacja]
  [idempotentność: podwójne kliknięcie → jedna akcja]
  [wygasły token przy zapisie → nie gubić danych]

DANE UKRYTE (nigdy nie wychodzą w API):
  [pole]    [widoczne dla]    [ukryte przed]
```

**Checklist gotowości:**

- [ ] Każde pole wejściowe ma regułę walidacji (whitelist, zakres, typ, max length)
- [ ] Jasne co z nieprawidłowym wejściem (odrzuć? clamp? sanityzuj?)
- [ ] Autoryzacja per rola per endpoint (kto co widzi, kto co zmienia)
- [ ] Lista danych ukrytych w odpowiedzi (per rola)
- [ ] Obsługa wygasłego tokenu przy zapisie
- [ ] Idempotentność endpointów zapisu
- [ ] Sanityzacja HTML/skryptów w polach tekstowych
- [ ] Rate limiting per endpoint per rola

**Sygnał niekompletności:** ❌ „Discipline jako string od usera" → AI przyjmie dowolny string, w tym `"; DROP TABLE hints;--`

### Przykład → HIVE

```
WALIDACJA:
  discipline         whitelist z tabeli disciplines (nie dowolny string!)     400
  screen_type        whitelist: ["challenge_feedback","entry_form",...]       400
  hint_content       strip HTML, max 2000 chars, min 10, UTF-8 only          obcięcie
  hover_time         INT, >= 0, max 300 (5 min)                              clamp
  time_to_edit       INT, >= 0, max 3600 (1h)                                clamp
  limit              INT, 1–20                                                clamp
  context (JSON)     max 5KB, walidacja schematu                              400

AUTORYZACJA:
  Mentor widzi hinty TYLKO dla swoich dyscyplin
  Mentor NIE modyfikuje hintów innego mentora
  Uczeń NIE ma dostępu do endpointów HIVE (403)
  Podwójne "Użyj" → deduplikacja po hint_id + user_id + timestamp ± 5s

DANE UKRYTE:
  author_id (UUID)       widoczny: admin        ukryty: mentor, user
  usage/dismiss_count    widoczny: admin        ukryty: mentor, user
  passive_data surowe    widoczny: admin        ukryty: mentor, user
  confidence_score       widoczny: admin        ukryty: mentor (widzi ranking)
```

---

## 10. WARSTWA ODPORNOŚCI — Obsługa błędów, retry, fallbacki

### Definicja

**Co to jest:** Globalny wzorzec zachowania gdy coś pójdzie nie tak. Nie per-endpoint (to jest w Warstwie 2), ale systemowy: jeden format błędów, jedna strategia retry, jedna filozofia fallbacków.

**Dlaczego krytyczne:** Bez globalnego wzorca AI napisze obsługę błędów na siedem różnych sposobów. W jednym `{error: "not found"}`, w drugim `{message: "404"}`, w trzecim wyjątek bez catch. Razem — bałagan którego nie chcesz debugować o trzeciej w nocy.

**Format wymagany:**

```
FORMAT BŁĘDU (globalny, nie per moduł):
  Sukces: { data: {...}, meta: {...} }
  Błąd:   { error: { code: STRING (maszynowy), message: STRING (ludzki),
                      details: OBJECT|null } }
  ZASADY: bez stack trace w produkcji, bez surowych komunikatów bazy,
          HTTP status + error.code spójne

STRATEGIA RETRY:
  [scenariusz awarii]    [ile retry]    [po ile sekund]    [fallback gdy wyczerpane]

CIRCUIT BREAKER (dla zależności zewnętrznych):
  [serwis]    [próg otwarcia]    [czas otwarcia]    [warunek powrotu]

ZASADA OGÓLNA: Degraduj łagodnie, nie crashuj.
```

**Checklist gotowości:**

- [ ] Globalny format odpowiedzi (sukces + błąd) z przykładami
- [ ] Kody błędów maszynowe (frontend parsuje po kodzie, nie po message)
- [ ] Strategia retry per typ zależności
- [ ] Strategia fallback per scenariusz awarii
- [ ] Circuit breaker dla zależności zewnętrznych
- [ ] Jasne co frontend pokazuje użytkownikowi w każdym scenariuszu awarii

### Przykład → HIVE

```
FORMAT:
  Sukces: { data: { hints: [...] }, meta: { total: INT } }
  Błąd:   { error: { code: "INVALID_DISCIPLINE", message: "Nieznana dyscyplina",
                      details: { received: "surfing123" } } }

RETRY:
  LLM timeout          → retry 1× po 3s → fallback Warstwa 1 (predefiniowane)
  Baza timeout          → retry 1× po 1s → 503 SERVICE_TEMPORARILY_UNAVAILABLE
  Cache nie odświeżony  → użyj ostatniej wartości (stale > missing)
  Cron nie wykonany     → log WARNING, retry na następny cykl
  Frontend bez odp.     → timeout 10s → skeleton → "Spróbuj ponownie"

CIRCUIT BREAKER — LLM API:
  CLOSED (normalny): requesty idą do LLM
  3 błędy w 60s → OPEN: fallback na Warstwę 1
  60s → HALF-OPEN: 1 request testowy
  2 udane z rzędu → CLOSED
```

---

## 11. WARSTWA OBSERWOWALNOŚCI — Logi, metryki, alerty

### Definicja

**Co to jest:** Co system mówi o sobie w produkcji. Bez tego moduł jest czarną skrzynką — działa albo nie, ale nie wiesz dlaczego ani kiedy przestanie.

**Dlaczego krytyczne:** AI bez instrukcji albo loguje wszystko (szum — tysiące linii na minutę), albo nic (cisza — dowiadujesz się o problemie od użytkownika). Obserwowalność to decyzja: co logować, na jakim poziomie, w jakim formacie, co mierzyć, kiedy alarmować.

**Format wymagany:**

```
LOGI:
  FORMAT: [JSON strukturalny — pola wspólne dla każdego logu]
  INFO:   [co logować — normalne operacje]
  WARN:   [co logować — degradacja, fallbacki, anomalie]
  ERROR:  [co logować — awarie wymagające uwagi]
  NIE LOGOWAĆ: [dane osobowe, tokeny, treści wrażliwe]

METRYKI:
  [nazwa]    [typ: counter/gauge/histogram]    [agregacja]    [dashboard]

ALERTY:
  [warunek]    [poziom: WARNING/CRITICAL]    [akcja: Slack/SMS/log]
```

**Checklist gotowości:**

- [ ] Format logów ustalony (JSON, nie tekst swobodny)
- [ ] Co logować na każdym poziomie (INFO, WARN, ERROR)
- [ ] Co NIE logować (dane osobowe, tokeny, treści)
- [ ] Metryki z typami (counter, gauge, histogram) i agregacjami
- [ ] Alerty z warunkami, poziomami i akcjami
- [ ] Logowanie synchroniczne czy asynchroniczne (nie blokuj request na log)

### Przykład → HIVE

```
LOGI (format JSON, pola wspólne: timestamp, level, module, action, user_id, duration_ms):
  INFO:  każde getHints (discipline, hint_count, dominant_layer, ms)
         każde recordAction (action_type, hint_id, has_passive_data)
         każda zmiana flagi (flag, old→new, changed_by)
  WARN:  fallback na Warstwę 1 lub 3, cron pominięty, response > 1s, circuit breaker zmiana
  ERROR: LLM timeout, baza timeout, cron failed po retry
  NIE:   treści hintów, tokeny JWT, surowe passive_data

METRYKI:
  hive.hints.requests            counter      req/min       operacyjny
  hive.hints.response_time_ms    histogram    p50/p95/p99   operacyjny
  hive.hints.fallback_rate       gauge        % per 5min    operacyjny
  hive.actions.count             counter      per type      analityczny
  hive.llm.circuit_breaker       gauge        OPEN/CLOSED   operacyjny

ALERTY:
  p95 > 2s (5 min)            WARNING     Slack
  p95 > 5s (5 min)            CRITICAL    Slack + SMS
  fallback > 50% (15 min)     CRITICAL    Slack + SMS
  LLM breaker OPEN > 10 min   CRITICAL    Slack + SMS
  0 req / 30 min (w godzinach) WARNING    Slack
```


---

## 12. TRZY NARZĘDZIA PROCEDURALNE — Jak używać RtS przy challengowaniu

RtS opisuje **stan docelowy**: 11 warstw, każda kompletna. Ale dokumentacja modułu jest zazwyczaj na poziomie koncepcyjnym — pitchowym, strategicznym. Challenge polega na zmierzeniu **dystansu** między tym co jest a tym co potrzeba. Do tego służą trzy narzędzia.

---

### 12.1. Gap Map — Mapa luk

**Co to jest:** Tabela porównująca istniejącą dokumentację modułu z 11 warstwami RtS. Dla każdej warstwy kategoryzuje: co jest zdefiniowane, co wymaga doprecyzowania, czego brakuje całkowicie.

**Kiedy używać:** Na początku challenge'u — zanim zaczniesz pytać o szczegóły.

**Format:**

```
GAP MAP — [NAZWA MODUŁU]
Źródło: [nazwa dokumentu koncepcyjnego]
Data audytu: [data]

  Warstwa          Status    Co jest                     Czego brakuje / pytania
  ──────────────────────────────────────────────────────────────────────────────────
  1. Dane          ⚠️        Opisane koncepcyjnie        Brak typów pól, indeksów, FK
  2. API           ❌        Nie opisane                  Potrzebna pełna specyfikacja
  3. Logika        ✅        Wzór confidence podany       Brak edge case dla NULL
  4. Stany         ⚠️        Flagi wymienione             Brak mechaniki przechowywania
  5. Integracje    ⚠️        Wiadomo co potrzebuje        Brak timeout/fallback
  6. UI            ❌        Nie opisane                  Potrzebna mapa komponentów
  7. Testy         ❌        Brak                         Potrzebne seedy + scenariusze
  8. Meta          ⚠️        Stos opisany ogólnie         Brak konwencji, struktury plików
  9. Bezpieczeństwo ❌       Nie opisane                  Potrzebna walidacja, autoryzacja
  10. Odporność    ❌        Nie opisane                  Potrzebny format błędów, retry
  11. Obserwowalność ❌      Nie opisane                  Potrzebne logi, metryki, alerty

  PODSUMOWANIE:
    ✅ Gotowe:              [N] warstw
    ⚠️ Do doprecyzowania:   [N] warstw — [lista konkretnych pytań]
    ❌ Brakuje:             [N] warstw — [do stworzenia od zera]
```

**Legenda:**
- ✅ **Zdefiniowane** — informacja istnieje z wystarczającą precyzją do napisania kodu
- ⚠️ **Do doprecyzowania** — informacja istnieje koncepcyjnie, ale brakuje detali (typów, zakresów, edge case'ów). Wymaga pytań do właściciela produktu.
- ❌ **Brakuje** — informacja nie istnieje w żadnej formie. Do stworzenia od zera.

**Kluczowe:** Wynikiem Gap Map jest **lista konkretnych pytań** — nie „uzupełnij Warstwę 10" ale „jaki timeout dla LLM API? 5s? 10s? ile retry? co widzi mentor gdy LLM nie odpowiada?"

---

### 12.2. Graf zależności implementacyjnych

**Co to jest:** Mapa pokazująca który moduł musi być gotowy (albo przynajmniej mieć ustalone interfejsy) PRZED którym. Nie harmonogram — mapa „co blokuje co".

**Kiedy używać:** Przed wyborem kolejności implementacji modułów.

**Format:**

```
GRAF ZALEŻNOŚCI — [NAZWA PROJEKTU]

  [Moduł A]
    ↓ wymaga interfejsu: [co dokładnie — np. "user_id + role z JWT"]
  [Moduł B]
    ↓ wymaga interfejsu: [co dokładnie]
  [Moduł C]

  LEGENDA:
    ● Gotowy (kod istnieje, interfejsy ustalone)
    ◐ Interfejs ustalony (moduł nie napisany, ale kontrakt API zdefiniowany)
    ○ Nie ustalony (trzeba zdefiniować przed implementacją zależnego modułu)
```

**Zasada:** Nie musisz mieć gotowego kodu modułu-zależności — wystarczy **ustalony interfejs** (Warstwa 2 + Warstwa 5 tego modułu). AI piszące HIVE nie potrzebuje gotowego kodu auth — potrzebuje wiedzieć że JWT zawiera `user_id: UUID` i `role: ENUM("mentor"|"admin"|"user")`.

**Przykład → IDareU Gen2:**

```
  Auth ●─────────────────────┐
    ↓ JWT: user_id + role    │
  Users ◐                    │
    ↓ user_id, disciplines[] │
  Challenges ◐               │
    ↓ challenge_id, type,    │
    ↓ discipline             │
  HIVE ○ ◄──────────────────┘
    ↓ getHints, recordAction
  Ekran feedbacku ○
  Panel admina ○
```

---

### 12.3. Wskaźnik głębokości RtS

**Co to jest:** Definicja które warstwy RtS są wymagane dla danej fazy implementacji, a które mogą być placeholderem.

**Kiedy używać:** Przy planowaniu konkretnej sesji kodowania — żeby challenge był proporcjonalny do tego co kodujemy, nie do docelowej wizji.

**Format:**

```
GŁĘBOKOŚĆ RtS — [MODUŁ] — [FAZA]

  Warstwa              Wymagana?    Uzasadnienie
  ──────────────────────────────────────────────────────────────
  1. Dane              PEŁNA        Schemat bazy budujemy raz
  2. API               PEŁNA        Endpointy muszą być stabilne
  3. Logika            PEŁNA        Algorytmy w kodzie
  4. Stany             CZĘŚCIOWA    Tylko flagi aktywne w tej fazie
  5. Integracje        PEŁNA        Interfejsy muszą być jasne
  6. UI                PEŁNA        Komponenty w kodzie
  7. Testy             PEŁNA        Testy piszemy od razu
  8. Meta              PEŁNA        Stos i konwencje raz na zawsze
  9. Bezpieczeństwo    PEŁNA        Bezpieczeństwo od dnia pierwszego
  10. Odporność        CZĘŚCIOWA    Format błędów tak, circuit breaker placeholder
  11. Obserwowalność   PODSTAWOWA   Logi INFO tak, alerty placeholder
```

**Trzy poziomy głębokości:**

- **PEŁNA** — warstwa musi być kompletna według checklisty z definicji
- **CZĘŚCIOWA** — warstwa opisana dla elementów aktywnych w tej fazie, reszta jawnie oznaczona jako „placeholder — do uzupełnienia przed Fazą [N]"
- **PODSTAWOWA** — minimum funkcjonalne (np. logi INFO bez alertów), z jasnym planem rozszerzenia

**Zasada:** Schemat bazy (Warstwa 1) i bezpieczeństwo (Warstwa 9) są ZAWSZE pełne — niezależnie od fazy. Źle zaprojektowany schemat to migracje. Brak bezpieczeństwa to wystawienie danych.

**Przykład → HIVE Faza 0:**

```
GŁĘBOKOŚĆ RtS — HIVE — FAZA 0

  1. Dane             PEŁNA       pełny schemat z polami na przyszłe flagi
  2. API              PEŁNA       getHints + recordAction + admin endpoints
  3. Logika           CZĘŚCIOWA   base confidence (bez temporal, bez mentor weight)
  4. Stany            CZĘŚCIOWA   tylko PASSIVE_SIGNALS=ON, reszta flag OFF
  5. Integracje       PEŁNA       auth + challenges
  6. UI               PEŁNA       HintDisplay + HiveAdminPanel (zakładki 1–2)
  7. Testy            PEŁNA       testy dla aktywnej logiki
  8. Meta             PEŁNA       stos + konwencje
  9. Bezpieczeństwo   PEŁNA       walidacja, autoryzacja, sanityzacja
  10. Odporność       CZĘŚCIOWA   format błędów pełny, circuit breaker placeholder
  11. Obserwowalność  PODSTAWOWA  logi INFO, metryki bazowe, alerty placeholder
```


---

## 13. PROCES — Jak AI czyta blueprint i pisze kod

### Kolejność budowania modułu

AI nie czyta blueprintu od góry do dołu i potem pisze wszystko naraz. Optymalna kolejność:

```
KROK 1:  Modele i migracje bazy danych              (Warstwa 1)
KROK 2:  Middleware walidacji i bezpieczeństwa        (Warstwa 9)
KROK 3:  Serwis z logiką biznesową                   (Warstwa 3 + 4)
KROK 4:  Obsługa błędów i circuit breaker            (Warstwa 10)
KROK 5:  Endpointy API                               (Warstwa 2)
KROK 6:  Logowanie i metryki                         (Warstwa 11)
KROK 7:  Crony i eventy                              (Warstwa 4)
KROK 8:  Komponenty frontendowe                      (Warstwa 6)
KROK 9:  Seeds i testy E2E                           (Warstwa 7)
KROK 10: Integracja z resztą systemu                 (Warstwa 5)
```

Każdy krok ma walidację: AI pisze fragment → uruchamia testy → dopiero przechodzi dalej. Nie pisze 10 000 linii kodu i testuje na końcu.

### Jak podać blueprint AI

Jeden dokument. Nie jedenaście plików. AI pracuje najlepiej gdy cały kontekst jest w jednym oknie. Blueprint modułu — wszystkie warstwy w głębokości wymaganej przez fazę — to ~20–30 stron. Mieści się w kontekście Claude Code.

Na górze dokumentu — jedno zdanie: *„Zaimplementuj moduł [NAZWA] zgodnie z poniższą specyfikacją. Każdy element jest zdefiniowany precyzyjnie — nie zgaduj, nie dodawaj, nie upraszczaj."*

---

## 14. RtS — PEŁNA CHECKLISTA

Generyczna — działa dla dowolnego modułu.

### Czy blueprint jest gotowy do sesji kodowania?

| # | Warstwa | Pytanie kontrolne | ✅ |
|:---:|---|---|:---:|
| 1 | **Dane** | Każde pole ma typ z precyzją, ograniczenia, indeksy z uzasadnieniem? | |
| 2 | **API** | Każdy endpoint ma sygnaturę z typami wejścia/wyjścia, kody błędów, reguły? | |
| 3 | **Logika** | Każdy algorytm ma wzór z parametrami, zakresami, edge case'ami, testem? | |
| 4 | **Stany** | Flagi mają mechanikę, crony częstotliwość i timeout, eventy wyzwalacz i akcję? | |
| 5 | **Integracje** | Import/eksport jasny: co, skąd, jak, co gdy niedostępne? | |
| 6 | **UI** | Każdy komponent ma dane, akcje, stany (pusty/loading/error), responsywność? | |
| 7 | **Testy** | Seedy gotowe, min. 5 testów per algorytm, min. 2 E2E, z liczbami? | |
| 8 | **Meta** | Stos, konwencje, struktura plików, próbka kodu? | |
| 9 | **Bezpieczeństwo** | Walidacja, sanityzacja, autoryzacja per rola, dane ukryte, idempotentność? | |
| 10 | **Odporność** | Format błędów, retry/fallback, circuit breaker, łagodna degradacja? | |
| 11 | **Obserwowalność** | Format logów, co logować/nie, metryki z typami, alerty z warunkami? | |

### Test gotowości — trzy pytania

**Pytanie 1 — dane:** Weź dowolne pole z dowolnej tabeli. Jaki typ? Jakie ograniczenie? Kto zapisuje? Kto czyta? Jak wyświetlane? Co gdy NULL?

**Pytanie 2 — awaria:** Weź dowolną zależność zewnętrzną. Co gdy nie odpowie w 10 sekund? Co zobaczy użytkownik? Co w logach? Kiedy dostaniesz alert?

**Pytanie 3 — bezpieczeństwo:** Weź dowolny parametr wejściowy. Jak walidowany? Co gdy wartość spoza zakresu? Co gdy ten sam request dwa razy?

Trzy „tak" bez wahania → RtS spełniony. Jedno „to zależy" → wróć do odpowiedniej warstwy.

---

## 15. RtS ↔ DoD — Symetria w WAVE

Każda warstwa RtS ma swój odpowiednik w DoD. To nie jest przypadkowe — DoD weryfikuje, czy kod realizuje to, co RtS zdefiniował.

```
 ┌─────────────────────────────────────────────────────────────────┐
 │                                                                 │
 │  RtS                                                    DoD     │
 │  Requisite-to-Start                          Definition-of-Done │
 │                                                                 │
 │  11 warstw blueprintu                  Kryteria zamknięcia      │
 │  ───────────────────                   ────────────────────      │
 │  ✅ Dane zdefiniowane                  ✅ Migracje wykonane     │
 │  ✅ API wyspecyfikowane                ✅ Endpointy odpowiadają │
 │  ✅ Logika ze wzorami                  ✅ Testy jednostkowe OK  │
 │  ✅ Stany i przejścia                  ✅ Flagi przełączalne    │
 │  ✅ Integracje zmapowane               ✅ Moduły połączone      │
 │  ✅ UI opisane                         ✅ Komponenty renderują   │
 │  ✅ Testy przygotowane                 ✅ Testy E2E przechodzą  │
 │  ✅ Meta ustalone                      ✅ Konwencje zachowane    │
 │  ✅ Bezpieczeństwo zamknięte           ✅ Pen-test bazowy OK    │
 │  ✅ Odporność zaplanowana              ✅ Scenariusze awarii OK │
 │  ✅ Obserwowalność zdefiniowana        ✅ Logi i metryki żywe   │
 │                                                                 │
 │  „Czy istnieje to,                    „Czy moduł robi to,      │
 │   co wymagane?"                        co blueprint opisuje?"   │
 │                                                                 │
 │  ◄── OTWIERA ETAP ──── KODOWANIE ──── ZAMYKA ETAP ──►         │
 │                                                                 │
 └─────────────────────────────────────────────────────────────────┘
```

---

## 16. MIEJSCE RtS W PIRAMIDZIE WAVE

```
                        ┌──────────┐
                        │  WIZJA   │  ← Pitch, Common Wise
                        │ (DLACZEGO)│     "Co chcemy osiągnąć?"
                        └─────┬────┘
                              │
                     ┌────────┴────────┐
                     │   WYMAGANIA     │  ← Dokumenty 01–11, Decision Log
                     │     (CO)        │     "Co system ma robić?"
                     └────────┬────────┘
                              │
              ┌───────────────┴───────────────┐
              │   RtS — BLUEPRINT TECHNICZNY   │  ← TEN DOKUMENT definiuje format
              │       (JAK DOKŁADNIE)          │     Konkretny blueprint modułu
              │                                │     to osobny dokument
              │  11 warstw + 3 narzędzia       │     wypełniający ten format.
              │  proceduralne                  │
              └───────────────┬───────────────┘
                              │
                     ┌────────┴────────┐
                     │   KODOWANIE     │  ← Claude Code / sesja implementacji
                     │   (REALIZACJA)  │     AI pisze kod strumieniowo
                     └────────┬────────┘
                              │
                        ┌─────┴────┐
                        │   DoD    │  ← Testy, review, integracja
                        │ (GOTOWE?) │     "Czy moduł spełnia blueprint?"
                        └──────────┘
```

RtS żyje na styku wymagań i kodowania. Tłumaczy „co system ma robić" na „jak dokładnie to zbudować" — z precyzją wystarczającą, żeby AI nie musiało interpretować ani zgadywać.

---

## 17. CZEGO BLUEPRINT NIE ZAWIERA

Blueprint techniczny to nie jest „cała dokumentacja". To jest jedno konkretne narzędzie z jednym celem: żeby AI pisało kod bez zatrzymywania się.

**Blueprint NIE zawiera:**
- Uzasadnień biznesowych *(Common Wise, pitch decki)*
- Historii decyzji *(Decision Log)*
- Analizy konkurencji *(analizy rynkowe)*
- Strategii wdrożenia *(harmonogram)*
- Dokumentacji użytkownika *(powstaje PO kodzie)*

**Blueprint ZAWIERA wyłącznie:**
- Na czym system operuje *(tabele, typy, relacje)*
- Co system robi na zewnątrz *(endpointy, odpowiedzi)*
- Jak system myśli *(algorytmy, wzory, edge case'y)*
- Kiedy system reaguje *(flagi, crony, eventy)*
- Z czym system rozmawia *(integracje, zależności)*
- Co użytkownik widzi *(komponenty, stany, akcje)*
- Jak zweryfikować *(testy z liczbami)*
- W czym pisać *(stos, konwencje, próbka kodu)*
- Czego nie robić *(walidacja, sanityzacja, dane ukryte)*
- Co gdy coś nie działa *(retry, fallback, circuit breaker)*
- Co system mówi o sobie *(logi, metryki, alerty)*

---

## 18. WORKFLOW CHALLENGE'U — Jak używać RtS do audytu dokumentacji

Krok po kroku, jak przejść od dokumentu koncepcyjnego do gotowego blueprintu:

```
KROK 1: ZBIERZ DOKUMENTY ŹRÓDŁOWE
         Dla modułu X weź: Common Wise, dokumenty Core (01–11),
         Decision Log — wszystko co opisuje X.

KROK 2: STWÓRZ GAP MAP
         Warstwa po warstwie: ✅ / ⚠️ / ❌.
         Wynik: lista pytań do właściciela produktu.

KROK 3: OKREŚL GRAF ZALEŻNOŚCI
         Które moduły muszą mieć ustalone interfejsy PRZED X?
         Wynik: lista interfejsów do ustalenia lub potwierdzenia.

KROK 4: USTAW GŁĘBOKOŚĆ RtS
         Dla danej fazy: które warstwy PEŁNE, CZĘŚCIOWE, PODSTAWOWE?
         Wynik: zakres blueprintu proporcjonalny do sesji kodowania.

KROK 5: UZUPEŁNIJ LUKI
         Warstwa po warstwie, w kolejności 1→11.
         Każda odpowiedź właściciela produktu → od razu do blueprintu.

KROK 6: WERYFIKACJA — TRZY PYTANIA
         Pytanie o dane, pytanie o awarię, pytanie o bezpieczeństwo.
         Jeśli „to zależy" → wróć do KROK 5.

KROK 7: SESJA KODOWANIA
         Blueprint gotowy → Claude Code → kod strumieniowy.
```

---

*RtS — Requisite-to-Start. Element metodyki WAVE. Jedenaście warstw zamyka przestrzeń wymagań: od danych (NA CZYM) przez logikę (JAK) i bezpieczeństwo (CZEGO NIE) po obserwowalność (CO SYSTEM MÓWI O SOBIE). Trzy narzędzia proceduralne (Gap Map, Graf zależności, Wskaźnik głębokości) zamieniają RtS z dokumentu referencyjnego w narzędzie robocze. Generyczny — działa dla dowolnego modułu. Jeśli AI musi zgadywać — RtS nie jest spełniony.*
