# Blueprint techniczny — [NAZWA MODUŁU]
## Faza [N] | RtS — Requisite-to-Start

**Moduł:** [NAZWA MODUŁU]  
**Faza:** [N — np. 0, 1, 2]  
**Data:** [DATA]  
**Autor blueprintu:** [KTO]  
**Źródło wymagań:** [lista dokumentów koncepcyjnych]  
**Audyt RtS:** [nazwa pliku audytu z Sesji 1]

---

## Wskaźnik głębokości RtS — ten blueprint

> Wypełnij poniższą tabelę na podstawie Sesji 1 (Audyt RtS). Określa ona ile szczegółów wymaga każda warstwa w tej fazie.

| # | Warstwa | Głębokość | Uzasadnienie |
|:---:|---|---|---|
| 1 | Dane | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 2 | API | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 3 | Logika | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 4 | Stany | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 5 | Integracje | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 6 | UI | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 7 | Testy | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 8 | Meta | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 9 | Bezpieczeństwo | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 10 | Odporność | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |
| 11 | Obserwowalność | [PEŁNA / CZĘŚCIOWA / PODSTAWOWA] | [UZUPEŁNIJ] |

> **PEŁNA** = każdy element checklisty odhaczony, zero [UZUPEŁNIJ]  
> **CZĘŚCIOWA** = elementy aktywne w tej fazie + placeholdery na resztę  
> **PODSTAWOWA** = minimum funkcjonalne + plan rozszerzenia

---

## Graf zależności — co musi istnieć PRZED tym modułem

> Wypełnij na podstawie Sesji 1.

```
  [Moduł zależny 1] [●/◐/○]
    ↓ wymaga: [CO DOKŁADNIE — np. "user_id + role z JWT"]
  [Moduł zależny 2] [●/◐/○]
    ↓ wymaga: [CO DOKŁADNIE]
  [TEN MODUŁ] ○
```

> ● Gotowy (kod istnieje) | ◐ Interfejs ustalony (kontrakt API) | ○ Nie ustalony

Interfejsy do ustalenia PRZED kodowaniem:

| Moduł | Co dokładnie trzeba ustalić | Status |
|---|---|:---:|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | ○ |


---

## WARSTWA 1: DANE — Schematy tabel

> Dla każdej tabeli: pełna definicja pól, typów, ograniczeń, indeksów, relacji.  
> Skopiuj blok TABELA tyle razy ile tabel potrzebuje moduł.

### Tabela: [NAZWA_TABELI_1]

| Pole | Typ | Ograniczenia | Opis |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ — z precyzją: VARCHAR(100), nie VARCHAR] | [NOT NULL / NULLABLE / DEFAULT / CHECK / FK / INDEX] | [UZUPEŁNIJ] |
| | | | |
| | | | |
| | | | |
| | | | |

**Indeksy:**

| Nazwa | Pola | Uzasadnienie (które zapytanie) |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | |

**Relacje:**

| Pole | Cel (tabela.pole) | Krotność |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [ONE-TO-MANY / MANY-TO-ONE / SELF-REF] |
| | | |

### Tabela: [NAZWA_TABELI_2]

> Powtórz powyższy blok dla każdej dodatkowej tabeli.

| Pole | Typ | Ograniczenia | Opis |
|---|---|---|---|
| | | | |

### Checklist Warstwy 1

- [ ] Każde pole ma typ z precyzją
- [ ] Każde pole ma ograniczenia (NOT NULL / NULLABLE / DEFAULT / CHECK)
- [ ] Każda relacja ma FK z kierunkiem i krotnością
- [ ] Każdy indeks ma uzasadnienie
- [ ] Każdy ENUM ma zamkniętą listę wartości
- [ ] Dane seedowe zdefiniowane (patrz Warstwa 7)

---

## WARSTWA 2: API — Endpointy

> Dla każdego endpointu: ścieżka, metoda, autoryzacja, parametry z typami, odpowiedź z typami, kody błędów, reguły biznesowe.  
> Skopiuj blok ENDPOINT tyle razy ile endpointów potrzebuje moduł.

### Endpoint: [NAZWA_1]

```
ŚCIEŻKA:      [METHOD] [/api/v1/...]
AUTORYZACJA:   [kto ma dostęp — role]
RATE LIMIT:    [limit per user/rola]
```

**Parametry wejściowe:**

| Parametr | Typ | Wymagany? | Default | Opis |
|---|---|:---:|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | TAK/NIE | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | | | |
| | | | | |

**Odpowiedź (200 OK):**

```json
{
  "data": {
    [UZUPEŁNIJ — pełna struktura z typami dla KAŻDEGO pola, w tym zagnieżdżonych]
  },
  "meta": {
    [UZUPEŁNIJ — jeśli dotyczy: paginacja, statystyki]
  }
}
```

**Kody błędów:**

| Kod | Kiedy |
|:---:|---|
| 400 | [UZUPEŁNIJ] |
| 401 | [UZUPEŁNIJ] |
| 403 | [UZUPEŁNIJ] |
| 429 | [UZUPEŁNIJ] |
| 500 | [UZUPEŁNIJ] |

**Reguły biznesowe tego endpointu:**

1. [UZUPEŁNIJ — sortowanie, filtrowanie, fallback, logika warunkowa]
2. [UZUPEŁNIJ]
3. [UZUPEŁNIJ]

### Endpoint: [NAZWA_2]

> Powtórz powyższy blok dla każdego dodatkowego endpointu.

### Checklist Warstwy 2

- [ ] Każdy parametr ma typ, opcjonalność i default
- [ ] Każda odpowiedź ma typy dla wszystkich pól (w tym zagnieżdżonych)
- [ ] Kody błędów pokrywają: walidacja, auth, brak danych, rate limit, serwer
- [ ] Reguły biznesowe PRZY endpoincie (nie w osobnym dokumencie)
- [ ] Jasne co na pustym zbiorze (404? pusta lista? fallback?)

---

## WARSTWA 3: LOGIKA — Algorytmy i wzory

> Dla każdego obliczanego wyniku: wzór z parametrami, zakresy, edge case'y, test weryfikacyjny.  
> Skopiuj blok ALGORYTM tyle razy ile algorytmów potrzebuje moduł.

### Algorytm: [NAZWA_1]

**Wzór:**

```
[UZUPEŁNIJ — formuła matematyczna z nazwanymi zmiennymi]
```

**Zmienne:**

| Zmienna | Typ | Zakres | Źródło |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [min–max] | [skąd pochodzi] |
| | | | |

**Modyfikatory (opcjonalne):**

| Modyfikator | Flaga | Wzór | Zakres | Kiedy nieaktywny |
|---|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | = [wartość domyślna] |
| | | | | |

**Edge case'y:**

| Sytuacja | Zachowanie |
|---|---|
| [np. pole IS NULL] | [UZUPEŁNIJ] |
| [np. dzielenie przez zero] | [UZUPEŁNIJ] |
| [np. pierwszy rekord] | [UZUPEŁNIJ] |

**Kiedy przeliczać:** [per-request / cron co Xh / event-driven]

**Test weryfikacyjny:**

```
INPUT:  [konkretne wartości]
FLAGS:  [które ON, które OFF]
EXPECT: [dokładny wynik liczbowy z krokami pośrednimi]
```

### Algorytm: [NAZWA_2]

> Powtórz powyższy blok dla każdego dodatkowego algorytmu.

### Checklist Warstwy 3

- [ ] Każdy wzór ma jawne zmienne z typami i zakresami
- [ ] Każdy edge case opisany
- [ ] Jasne kiedy przeliczać
- [ ] Min. 1 test weryfikacyjny z konkretnymi liczbami per algorytm
- [ ] Jasne co gdy flaga wyłączona

---

## WARSTWA 4: STANY — Feature flags, crony, eventy

### Feature flags

| Nazwa | Domyślnie | Typ | Warunek włączenia |
|---|:---:|---|---|
| [UZUPEŁNIJ] | ON/OFF | boolean | [UZUPEŁNIJ] |
| | | | |
| | | | |

**Mechanika flag:**

```
Przechowywanie:  [UZUPEŁNIJ — tabela? plik? env?]
Odczyt:          [UZUPEŁNIJ — per-request? cache? odświeżanie co ile?]
Zmiana:          [UZUPEŁNIJ — endpoint? panel? kto ma uprawnienia?]
Audyt:           [UZUPEŁNIJ — co logować przy zmianie?]
```

### Cron jobs

| Nazwa | Częstotliwość | Flaga | Co robi |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | | |

**Dla każdego crona:**

```
Warunek uruchomienia:  [flaga ON + ...]
Co jeśli flaga OFF:    [UZUPEŁNIJ]
Co jeśli brak danych:  [UZUPEŁNIJ]
Timeout:               [UZUPEŁNIJ]
Retry:                 [UZUPEŁNIJ]
```

### Eventy

| Zdarzenie | Wyzwalacz | Akcja | Warunek flagi |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ lub "zawsze"] |
| | | | |
| | | | |

### Checklist Warstwy 4

- [ ] Każda flaga: nazwa, typ, default, warunek, mechanika
- [ ] Każdy cron: częstotliwość, warunek, timeout, retry
- [ ] Każdy event: wyzwalacz, akcja, warunek flagi
- [ ] Mechanika odczytu flag jasna (cache? odświeżanie?)
- [ ] Zmiany flag audytowane

---

## WARSTWA 5: INTEGRACJE — Zależności

### Import — co ten moduł potrzebuje od reszty

| Źródło | Co pobiera | Jak uzyskuje | Co gdy niedostępne |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [fallback? error? degradacja?] |
| | | | |
| | | | |

### Eksport — co ten moduł udostępnia innym

| Odbiorca | Co udostępnia | Przez jaki interfejs |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [REST API / event bus / polling] |
| | | |
| | | |

### Serwisy zewnętrzne

| Serwis | Co robi | URL | Auth | Timeout | Retry | Fallback |
|---|---|---|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | | | | | |

**Prompt template (jeśli LLM):**

```
[UZUPEŁNIJ — dosłowny prompt, nie opis. Jeśli nie dotyczy — usuń tę sekcję.]
```

### Checklist Warstwy 5

- [ ] Każdy import: źródło, co pobiera, format, co gdy niedostępne
- [ ] Każdy eksport: odbiorca, co udostępnia, interfejs
- [ ] Serwisy zewnętrzne: URL, auth, timeout, retry, fallback
- [ ] Prompt templates dosłownie (jeśli LLM)


---

## WARSTWA 6: UI — Komponenty frontendowe

> Dla każdego komponentu: gdzie używany, dane, stany, wyświetlanie, akcje, responsywność.  
> Skopiuj blok KOMPONENT tyle razy ile komponentów potrzebuje moduł.

### Komponent: [NAZWA_1]

**Gdzie używany:** [UZUPEŁNIJ — ekrany / konteksty]

**Dane wejściowe (props):**

| Prop | Typ | Opis |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | |

**Stany wewnętrzne:**

| Stan | Typ | Wartość początkowa |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | |

**Wyświetlanie warunkowe:**

| Warunek | Co widać |
|---|---|
| [np. typ = "warning"] | [UZUPEŁNIJ — kolor, ikona, tekst] |
| Stan pusty (brak danych) | [UZUPEŁNIJ] |
| Stan ładowania | [UZUPEŁNIJ] |
| Stan błędu | [UZUPEŁNIJ] |

**Akcje użytkownika → API:**

| Co użytkownik robi | Jaki endpoint wywołuje | Jaki feedback dostaje |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| | | |

**Responsywność:**

```
Desktop: [UZUPEŁNIJ]
Mobile:  [UZUPEŁNIJ]
```

### Komponent: [NAZWA_2]

> Powtórz powyższy blok dla każdego dodatkowego komponentu.

### Checklist Warstwy 6

- [ ] Każdy komponent: nazwa, gdzie używany, props z typami
- [ ] Stany wewnętrzne opisane
- [ ] Każda akcja: co widzi → co klika → jakie API → jaki feedback
- [ ] Stany: pusty / loading / error opisane
- [ ] Wygląd warunkowy opisany
- [ ] Responsywność: desktop vs mobile

---

## WARSTWA 7: TESTY — Dane startowe i scenariusze

### Dane seedowe

| Zbiór | Ile rekordów | Format | Opis |
|---|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | JSON/SQL | [UZUPEŁNIJ] |
| | | | |

**Konfiguracja domyślna:**

```
[UZUPEŁNIJ — domyślne wartości flag, parametrów, konfiguracji]
```

### Testy jednostkowe

> Min. 5 testów per algorytm. Skopiuj blok TEST tyle razy ile potrzeba.

```
TEST 1: [NAZWA SCENARIUSZA]
  INPUT:  [konkretne wartości]
  FLAGS:  [które ON, które OFF]
  EXPECT: [dokładny wynik liczbowy]

TEST 2: [NAZWA SCENARIUSZA]
  INPUT:  [konkretne wartości]
  FLAGS:  [które ON, które OFF]
  EXPECT: [dokładny wynik liczbowy]

TEST 3: [EDGE CASE — np. "zerowe dane"]
  INPUT:  [konkretne wartości]
  FLAGS:  [które ON, które OFF]
  EXPECT: [dokładny wynik]

TEST 4: [EDGE CASE — np. "NULL w kluczowym polu"]
  INPUT:  [konkretne wartości]
  FLAGS:  [które ON, które OFF]
  EXPECT: [dokładny wynik]

TEST 5: [EDGE CASE — np. "flagi OFF"]
  INPUT:  [konkretne wartości]
  FLAGS:  wszystkie OFF
  EXPECT: [dokładny wynik]
```

### Testy E2E

> Min. 2 testy per główny flow.

```
TEST E2E-1: [OPIS FLOW]
  KROK 1: [REQUEST]
          → [EXPECTED RESPONSE]
  KROK 2: [REQUEST]
          → [EXPECTED RESPONSE]
  KROK 3: [REQUEST]
          → [EXPECTED RESPONSE — weryfikacja że krok 2 miał efekt]

TEST E2E-2: [OPIS FLOW — np. "scenariusz awarii"]
  KROK 1: [REQUEST]
          → [EXPECTED RESPONSE]
  KROK 2: [SYMULACJA AWARII — np. timeout zależności]
          → [EXPECTED BEHAVIOR — fallback? error?]
```

### Checklist Warstwy 7

- [ ] Seedy gotowe w formacie importowalnym
- [ ] Konfiguracja domyślna zdefiniowana
- [ ] Min. 5 testów jednostkowych per algorytm (w tym edge cases)
- [ ] Min. 2 testy E2E per główny flow
- [ ] Każdy test: INPUT + FLAGS + EXPECTED OUTPUT z liczbami

---

## WARSTWA 8: META — Stos, konwencje, struktura

### Stos technologiczny

```
Backend:       [UZUPEŁNIJ — język, framework, ORM]
Baza danych:   [UZUPEŁNIJ — typ, wersja, hosting]
Frontend:      [UZUPEŁNIJ — framework, state management, styling]
API format:    [REST / GraphQL / mieszany]
Autentykacja:  [UZUPEŁNIJ — JWT, session, etc.]
Hosting:       [UZUPEŁNIJ — provider, architektura]
```

### Konwencje nazewnictwa

```
Tabele:        [UZUPEŁNIJ — np. snake_case, liczba pojedyncza]
Kolumny:       [UZUPEŁNIJ — np. snake_case]
Endpointy:     [UZUPEŁNIJ — np. kebab-case]
Komponenty:    [UZUPEŁNIJ — np. PascalCase]
Pliki:         [UZUPEŁNIJ — np. kebab-case.ts]
Zmienne:       [UZUPEŁNIJ — np. camelCase]
```

### Struktura plików modułu

```
/modules/[nazwa-modułu]/
  /api/
    [UZUPEŁNIJ — lista plików kontrolerów]
  /services/
    [UZUPEŁNIJ — lista plików serwisów]
  /models/
    [UZUPEŁNIJ — lista plików modeli]
  /middleware/
    [UZUPEŁNIJ — lista plików middleware]
  /cron/
    [UZUPEŁNIJ — lista plików cronów]
  /components/
    [UZUPEŁNIJ — lista plików komponentów]
  /seeds/
    [UZUPEŁNIJ — lista plików seedów]
  /tests/
    [UZUPEŁNIJ — lista plików testów]
```

### Próbka kodu (Załącznik 8A)

> Dołącz do blueprintu realne pliki z istniejącego modułu. Jeśli to pierwszy moduł — wygeneruj wzorcowy moduł-referencję.

```
  □ Kontroler:    [UZUPEŁNIJ — nazwa pliku lub "do wygenerowania"]
  □ Serwis:       [UZUPEŁNIJ]
  □ Model:        [UZUPEŁNIJ]
  □ Middleware:    [UZUPEŁNIJ]
  □ Plik testowy: [UZUPEŁNIJ]
  □ Konfiguracja bazy / ORM: [UZUPEŁNIJ]
  □ Lista istniejących helperów: [UZUPEŁNIJ]
```

### Checklist Warstwy 8

- [ ] Stos technologiczny zdefiniowany
- [ ] Konwencje nazewnictwa ustalone
- [ ] Struktura plików modułu ustalona
- [ ] Próbka kodu dołączona lub zaplanowana

---

## WARSTWA 9: BEZPIECZEŃSTWO — Walidacja i sanityzacja

### Walidacja wejścia

| Pole / Parametr | Reguła | Co jeśli złamana |
|---|---|---|
| [UZUPEŁNIJ] | [whitelist / zakres / typ / max length] | [400 / clamp / sanityzuj] |
| | | |
| | | |
| | | |

### Autoryzacja per rola per endpoint

| Reguła | Implementacja |
|---|---|
| [UZUPEŁNIJ — np. "Mentor widzi tylko swoje dane"] | [UZUPEŁNIJ — filtr, check] |
| [UZUPEŁNIJ — idempotentność] | [UZUPEŁNIJ — deduplikacja po czym?] |
| [UZUPEŁNIJ — wygasły token] | [UZUPEŁNIJ — co z niezapisanymi danymi?] |
| | |

### Dane ukryte — co NIGDY nie wychodzi w odpowiedzi API

| Pole | Widoczne dla | Ukryte przed |
|---|---|---|
| [UZUPEŁNIJ] | [UZUPEŁNIJ — role] | [UZUPEŁNIJ — role] |
| | | |
| | | |

### Checklist Warstwy 9

- [ ] Każde pole wejściowe ma regułę walidacji
- [ ] Jasne co z nieprawidłowym wejściem (odrzuć? clamp? sanityzuj?)
- [ ] Autoryzacja per rola per endpoint
- [ ] Lista danych ukrytych per rola
- [ ] Wygasły token przy zapisie obsłużony
- [ ] Idempotentność endpointów zapisu
- [ ] Sanityzacja HTML/skryptów
- [ ] Rate limiting per endpoint per rola

---

## WARSTWA 10: ODPORNOŚĆ — Obsługa błędów i fallbacki

### Globalny format odpowiedzi

```json
// SUKCES:
{
  "data": { ... },
  "meta": { ... }
}

// BŁĄD:
{
  "error": {
    "code": "[UZUPEŁNIJ — kod maszynowy: INVALID_DISCIPLINE, RATE_LIMIT_EXCEEDED]",
    "message": "[UZUPEŁNIJ — tekst ludzki]",
    "details": { ... } // opcjonalne
  }
}
```

**Zasady formatu:**

```
[UZUPEŁNIJ — np. bez stack trace w produkcji, bez surowych komunikatów bazy,
 HTTP status + error.code spójne]
```

### Strategia retry i fallback

| Scenariusz awarii | Retry | Po ile sekund | Fallback gdy wyczerpane |
|---|:---:|:---:|---|
| [UZUPEŁNIJ — np. LLM timeout] | [UZUPEŁNIJ] | [UZUPEŁNIJ] | [UZUPEŁNIJ] |
| [UZUPEŁNIJ — np. baza timeout] | | | |
| [UZUPEŁNIJ — np. cache miss] | | | |
| [UZUPEŁNIJ — np. cron fail] | | | |
| [UZUPEŁNIJ — np. frontend timeout] | | | |

### Circuit breaker (jeśli dotyczy)

```
Serwis:           [UZUPEŁNIJ — np. LLM API]
Stan CLOSED:      [normalne działanie]
Próg otwarcia:    [UZUPEŁNIJ — np. 3 błędy w 60s]
Stan OPEN:        [UZUPEŁNIJ — co zamiast: fallback na...]
Czas otwarcia:    [UZUPEŁNIJ — np. 60s]
Stan HALF-OPEN:   [UZUPEŁNIJ — np. 1 request testowy co 60s]
Powrót do CLOSED: [UZUPEŁNIJ — np. 2 udane z rzędu]
```

### Checklist Warstwy 10

- [ ] Globalny format odpowiedzi (sukces + błąd)
- [ ] Kody błędów maszynowe zdefiniowane
- [ ] Strategia retry per typ zależności
- [ ] Strategia fallback per scenariusz awarii
- [ ] Circuit breaker dla zależności zewnętrznych (jeśli dotyczy)
- [ ] Jasne co frontend pokazuje w każdym scenariuszu awarii

---

## WARSTWA 11: OBSERWOWALNOŚĆ — Logi, metryki, alerty

### Format logów

```
Format:           [UZUPEŁNIJ — np. JSON strukturalny]
Pola wspólne:     [UZUPEŁNIJ — np. timestamp, level, module, action, user_id, duration_ms]
Synchroniczność:  [synchroniczne / asynchroniczne — czy blokuje request?]
```

### Co logować

**INFO (normalne operacje):**

```
[UZUPEŁNIJ — np. "każde wywołanie getX: parametry, count, czas"]
[UZUPEŁNIJ]
[UZUPEŁNIJ]
```

**WARN (degradacja, anomalie):**

```
[UZUPEŁNIJ — np. "fallback na zapasowe źródło"]
[UZUPEŁNIJ]
[UZUPEŁNIJ]
```

**ERROR (awarie):**

```
[UZUPEŁNIJ — np. "timeout zależności zewnętrznej"]
[UZUPEŁNIJ]
[UZUPEŁNIJ]
```

**NIE LOGOWAĆ:**

```
[UZUPEŁNIJ — np. "treści danych osobowych, tokeny, hasła"]
[UZUPEŁNIJ]
```

### Metryki

| Nazwa | Typ | Agregacja | Dashboard |
|---|---|---|---|
| [UZUPEŁNIJ] | counter / gauge / histogram | [UZUPEŁNIJ] | operacyjny / analityczny |
| | | | |
| | | | |
| | | | |

### Alerty

| Warunek | Poziom | Akcja |
|---|---|---|
| [UZUPEŁNIJ — np. "p95 > 2s przez 5 min"] | WARNING / CRITICAL | [Slack / SMS / log] |
| | | |
| | | |
| | | |

### Checklist Warstwy 11

- [ ] Format logów ustalony
- [ ] Co logować na każdym poziomie (INFO, WARN, ERROR)
- [ ] Co NIE logować
- [ ] Metryki z typami i agregacjami
- [ ] Alerty z warunkami, poziomami i akcjami
- [ ] Jasne czy logowanie synchroniczne czy asynchroniczne


---

## AUTOTEST RtS — Trzy pytania

> AI wypełniające blueprint wykonuje ten test SAMODZIELNIE po zakończeniu wypełniania. Wybieram losowo, odpowiadam, i oceniam PASS / FAIL.

### Pytanie 1 — DANE

```
Wybieram pole: [UZUPEŁNIJ — losowe pole z losowej tabeli]

  Typ:              [UZUPEŁNIJ]
  Ograniczenie:     [UZUPEŁNIJ]
  Kto zapisuje:     [UZUPEŁNIJ]
  Kto czyta:        [UZUPEŁNIJ]
  Jak wyświetlane:  [UZUPEŁNIJ]
  Co gdy NULL:      [UZUPEŁNIJ]

  → PASS / FAIL    [jeśli FAIL — czego brakuje: ________________]
```

### Pytanie 2 — AWARIA

```
Wybieram zależność: [UZUPEŁNIJ — losowa zależność zewnętrzna]

  Co gdy timeout:       [UZUPEŁNIJ]
  Co widzi użytkownik:  [UZUPEŁNIJ]
  Co w logach:          [UZUPEŁNIJ]
  Kiedy alert:          [UZUPEŁNIJ]

  → PASS / FAIL    [jeśli FAIL — czego brakuje: ________________]
```

### Pytanie 3 — BEZPIECZEŃSTWO

```
Wybieram parametr: [UZUPEŁNIJ — losowy parametr wejściowy]

  Jak walidowany:          [UZUPEŁNIJ]
  Co gdy spoza zakresu:    [UZUPEŁNIJ]
  Co gdy podwójny request: [UZUPEŁNIJ]

  → PASS / FAIL    [jeśli FAIL — czego brakuje: ________________]
```

### Wynik autotestu

```
  Pytanie 1 (dane):           PASS / FAIL
  Pytanie 2 (awaria):         PASS / FAIL
  Pytanie 3 (bezpieczeństwo): PASS / FAIL

  BLUEPRINT GOTOWY DO KODOWANIA?   TAK / NIE

  [Jeśli NIE — lista elementów do uzupełnienia:]
  1. [________________]
  2. [________________]
  3. [________________]
```

---

## PLACEHOLDERY — Otwarte tematy na przyszłe fazy

> Jeśli wskaźnik głębokości oznaczył warstwę jako CZĘŚCIOWA lub PODSTAWOWA, wpisz tu co zostało pominięte i kiedy uzupełnić.

| Warstwa | Co pominięte | Uzupełnić przed fazą |
|---|---|:---:|
| [UZUPEŁNIJ] | [UZUPEŁNIJ] | Faza [N] |
| | | |
| | | |

---

*Blueprint techniczny modułu [NAZWA MODUŁU], Faza [N]. Wygenerowany zgodnie z procedurą WAVE FALA RtS. Szablon: 03_WAVE_FALA_RtS_Szablon_Blueprint_v1.md. Walidacja: 02_WAVE_FALA_RtS_Blueprint_Walidacja_v3.md.*
