# WAVE PULSE — Pattern Universal Living Standard Engine
## Prompt v3.0 | Marzec 2026

**Licencja:** CC BY-SA 4.0  
**Metodyka:** WAVE (Workflow Amplification via Vectored Expertise)  
**Dokumentacja towarzysząca:** PULSE-HowTo.md

---

## INSTRUKCJA DLA AI

Jesteś ekspertem w obszarze zdefiniowanym poniżej. Twoim zadaniem jest zbudowanie **Living Pattern** (Żywego Wzorca) — kompletnego dokumentu referencyjnego zawierającego najlepszą dostępną wiedzę naukową, branżową i praktyczną dla tego obszaru, zsyntezowaną pod konkretną funkcję celu.

Living Pattern to narzędzie z metodyki WAVE. Nie jest podręcznikiem, nie jest encyklopedią, nie jest Białą Księgą. Jest żywym dokumentem, który uzbrajana zespół implementacyjny w pewność, że działa na najlepszych możliwych założeniach.

Pracujesz w trybie **trzech rund**. Ten prompt uruchamia Rundę 1 (Budowa). Runda 2 (Optymalizacja) i Runda 3 (Finalizacja) zostaną uruchomione przez użytkownika w kolejnych poleceniach w tym samym czacie.

**WAŻNE — wyszukiwanie internetowe:** Research w każdej rundzie WYMAGA aktywnego przeszukiwania internetu za pomocą dostępnych narzędzi wyszukiwania (web search). Nie polegaj wyłącznie na wiedzy treningowej — ona może być nieaktualna. Szukaj aktywnie: nowych badań, aktualnych raportów, świeżych case studies, bieżących trendów. Jeśli narzędzie web search nie jest dostępne — poinformuj użytkownika że wynik będzie oparty wyłącznie na wiedzy treningowej i może nie odzwierciedlać najnowszego stanu wiedzy.

---

## PARAMETRY

### [OBSZAR]

> [WSTAW TUTAJ: Nazwa obszaru implementacyjnego. Np.: „UX/UI i User Journey", „Baza danych i model danych", „Architektura API", „Bezpieczeństwo", „Strategia testowania".]

### [FUNKCJA CELU]

> [WSTAW TUTAJ: Jedno zdanie definiujące co optymalizujemy. To jest kompas całego procesu — każda znaleziona wiedza będzie oceniana pytaniem „czy to przybliża do funkcji celu?" Przykład: „Maksymalizacja zaufania pacjenta od pierwszego kontaktu, retencji D30 powyżej 25%, i aktywacji (pierwsza konsultacja) powyżej 35% w ciągu 48h od rejestracji." Inny przykład: „Integralność dokumentacji medycznej + wydajność przy 5000 jednoczesnych sesji + struktura pod analizę wzorców diagnostycznych jako dataset do AI."]

### [KONTEKST ROZWIĄZANIA]

> [WSTAW TUTAJ: Opis budowanego produktu — co to jest, dla kogo, jak działa, co jest w nim unikalne. Im więcej kontekstu — tym celniejszy research. Minimum 3–5 zdań.]

### [MATERIAŁY WEWNĘTRZNE]

> [WSTAW TUTAJ: Lista plików dołączonych do czatu lub dostępnych w pamięci projektu (FILES). Wskaż które są kluczowe dla TEGO obszaru. Jeśli brak — napisz „brak".]

### [OGRANICZENIA]

> [WSTAW TUTAJ: Budżet, czas, zespół, regulacje, wybrane technologie — wszystko co zawęża pole możliwych rozwiązań. Jeśli brak — napisz „brak znanych ograniczeń".]

---

## RUNDA 1 — BUDOWA

### Krok 0 — Kontekst wewnętrzny

Przeczytaj materiały wewnętrzne wskazane w parametrze [MATERIAŁY WEWNĘTRZNE]. Zrozum architekturę rozwiązania, podjęte decyzje, istniejące specyfikacje. To jest warunek konieczny — bez niego Twój research będzie generyczny zamiast celowany pod TO rozwiązanie.

### Krok 1 — Research wielowarstwowy

Przeprowadź dogłębne badanie internetu w trzech warstwach:

**Warstwa naukowa:** Badania akademickie, przeglądy systematyczne, publikacje w recenzowanych czasopismach. Szukaj fundamentów teoretycznych i danych empirycznych. Nie opinii — faktów z dowodami.

**Warstwa branżowa:** Raporty firm analitycznych (Gartner, McKinsey, Forrester, NN/g i inne stosowne do obszaru), dokumentacje techniczne liderów rynku, case studies platform o profilu zbliżonym do rozwiązania użytkownika.

**Warstwa praktyczna:** Najlepsze praktyki z doświadczeń zespołów implementacyjnych. Błędy które inne firmy popełniły i ich mierzalne konsekwencje. Trendy na bieżący rok i najbliższą przyszłość. Rozwiązania innowacyjne które mogą dać przewagę.

**Filtr:** Każda znaleziona wiedza oceniana pytaniem: „Jak to wpływa na implementację w kontekście [FUNKCJA CELU]?" Jeśli nie wpływa — pomijaj. Jeśli wpływa — opisuj konkretnie jak.

### Krok 2 — Synteza w Living Pattern

Na podstawie materiałów wewnętrznych i researchu zbuduj dokument w następującej strukturze:

---

```markdown
# Living Pattern: [OBSZAR]
## Wersja 1.0 | [DATA]

**Funkcja celu:** [FUNKCJA CELU]
**Kontekst:** [KONTEKST ROZWIĄZANIA — skrócony]
**Status:** Runda 1 (Budowa) — oczekuje na weryfikację

---

## CZĘŚĆ I — STAN WIEDZY

### Co wiemy na pewno
[Konsensus naukowy i branżowy. Fakty z dowodami.]

### Co jest dyskusyjne
[Rozbieżne stanowiska, brak konsensusu, zależność od kontekstu.]

### Co się zmienia
[Trendy, kierunki rozwoju, nadchodzące zmiany.]

---

## CZĘŚĆ II — ZASADY I STANDARDY

### Zasady projektowe
[Reguły kierunkowe. Każda z: uzasadnienie + miara + implikacja.]

### Standardy i wymagania
[Mierzalne wymagania. Tabele z wartościami cel/alarm.]

### Implikacje dla ekosystemu rozwiązania
[Jak ten obszar łączy się z innymi komponentami rozwiązania.]

---

## CZĘŚĆ III — MATRYCA BŁĘDÓW

### Błędy krytyczne
[Zagrażają produktowi. Tabela: błąd | skutek | ochrona.]

### Błędy poważne
[Obniżają jakość.]

### Błędy subtelne
[Ograniczają doskonałość.]

---

## CZĘŚĆ IV — MATRYCA DECYZJI

[Kluczowe wybory do podjęcia w tym obszarze.
Dla każdego: warianty + kryteria + rekomendacja z uzasadnieniem.]

---

## CZĘŚĆ V — METRYKI SUKCESU

### Metryki wiodące (leading indicators)
[Tabela: metryka | definicja | cel | alarm]

### Metryki opóźnione (lagging indicators)
[Tabela: metryka | definicja | cel | alarm]

---

## CZĘŚĆ VI — ŹRÓDŁA I REFERENCJE

### Badania naukowe
[Autor, rok, tytuł, wynik.]

### Raporty branżowe
[Firma, rok, kluczowy wniosek.]

### Case studies
[Firma/produkt, kontekst, liczby.]

### Dokumentacja wewnętrzna
[Pliki z materiałów wewnętrznych użyte jako kontekst.]

---

## DZIENNIK ZMIAN

| Wersja | Data | Runda | Opis |
|--------|------|-------|------|
| v1.0 | [DATA] | Budowa | Fundament — [X] zasad, [Y] błędów, [Z] metryk |
```

**Nazwa pliku wyjściowego:** `LP_[OBSZAR_skrócony]_v[WERSJA].md`  
Przykłady: `LP_UX_UI_v3.md`, `LP_Database_v1.md`, `LP_Security_v2.md`

---

### Krok 3 — Werdykt Rundy 1

Po wygenerowaniu dokumentu podaj krótki werdykt: jakie obszary uważasz za dobrze pokryte, a gdzie czujesz że mogą być luki wymagające weryfikacji w Rundzie 2. To pomaga użytkownikowi podjąć decyzję o kierunku dalszej pracy.

---

## RUNDA 2 — OPTYMALIZACJA

> **Ta sekcja uruchamiana jest przez użytkownika poleceniem w rodzaju: „Uruchom Rundę 2 weryfikacji."**

### Zmiana kąta ataku

W Rundzie 1 szukałeś najlepszych praktyk i sukcesów. W Rundzie 2 celowo zmieniasz perspektywę:

**Szukaj porażek** — jakie błędy popełniły firmy w tym obszarze i jakie były mierzalne konsekwencje?

**Szukaj kontrowersji** — gdzie branża się nie zgadza? Jakie „oczywiste" praktyki mają krytyków?

**Szukaj głosów mniejszości** — co mówią startups vs. korporacje? Co mówią niszowi gracze vs. liderzy rynku?

**Szukaj alternatyw** — czy istnieją podejścia które celowo łamią konwencję i odnoszą sukces?

### Ponowny research

Przeszukaj internet celowo z nowego kąta. Inne zapytania, inne źródła, inne perspektywy niż w Rundzie 1.

### Aktualizacja dokumentu

Dodaj znaleziska do Living Pattern:
- Nowe elementy oznaczaj `[NOWE v2]`
- Wzmocnienia istniejących elementów oznaczaj `[WZMOCNIONE v2]`
- NIE usuwaj niczego z v1 — tylko dodawaj i wzmacniaj

Zaktualizuj wersję na v2.0 i wpis w Dzienniku zmian.

### Werdykt Rundy 2

Podaj ocenę: czy fundament jest kompletny, czy potrzebna Runda 3? Co zyskaliśmy w Rundzie 2? Jakie luki mogą jeszcze istnieć?

---

## RUNDA 3 — FINALIZACJA

> **Ta sekcja uruchamiana jest przez użytkownika poleceniem w rodzaju: „Uruchom Rundę 3 — peryferyjne kierunki."**

### Peryferyjne kierunki

Runda 3 celuje w obszary które typowy research pomija:

**Aspekty prawne i regulacyjne** — jakie przepisy, normy, standardy dotyczą tego obszaru? Co weszło w życie w ostatnim roku? Co się zmieni w najbliższych 2–3 latach?

**Dostępność i inkluzywność** — czy rozwiązania w tym obszarze są dostępne dla osób z niepełnosprawnościami? Czy uwzględniają neurodywersyjność?

**Wydajność i skalowalność** — jakie twarde limity obowiązują? Co się stanie przy 10× lub 100× wzroście skali?

**Edge case'y i sytuacje graniczne** — co się stanie gdy coś się zepsuje? Utrata połączenia? Błąd serwera? Migracja danych? Awaria zewnętrznego dostawcy?

**Perspektywa przyszłości** — co się zmieni w tym obszarze w ciągu 2–3 lat? Jak się przygotować żeby nie musieć przebudowywać?

### Aktualizacja dokumentu

Dodaj znaleziska z oznaczeniem `[NOWE v3]` i `[WZMOCNIONE v3]`. Zaktualizuj wersję na v3.0 i Dziennik zmian.

### Werdykt końcowy

Odpowiedz na pytanie: **Czy Living Pattern jest kompletny na poziomie dostępnej wiedzy?**

Podaj:
- Podsumowanie trzech rund — co znalazła każda
- Listę wszystkich obszarów pokrytych w dokumencie
- Ocenę kompletności (procentowo szacunkowo)
- Rekomendację: czy potrzebna czwarta runda (zwykle nie — uzasadnij)

---

## ZASADY JAKOŚCI (obowiązują we wszystkich rundach)

**Konkretność:** Każda zasada, reguła i rekomendacja ma trzy elementy: uzasadnienie (dlaczego), miarę (jak zmierzyć), implikację (co to oznacza dla tego rozwiązania). Nie „bądź szybki" lecz „LCP poniżej 2,5s na mobile 4G, bo 90% użytkowników odchodzi powyżej 3s (Google)."

**Źródła:** Każde twierdzenie ma źródło. Badania z datami i autorami. Raporty z nazwami firm. Case studies z liczbami. Nie „badania pokazują" — lecz kto, kiedy, jaki wynik.

**Celowość:** Każdy element oceniany pytaniem: „Czy to przybliża do [FUNKCJA CELU]?" Jeśli nie — nie trafia do dokumentu.

**Język:** Polski, płynny, bez makaronizmów i korpo-mowy. Nazwy techniczne i branżowe po angielsku tam gdzie nie ma dobrego polskiego odpowiednika.

**Praktyczność:** Living Pattern to narzędzie decyzyjne, nie akademicki artykuł. Każdy element musi odpowiadać na pytanie: „I co z tego dla mojej implementacji?"

**Format:** Dokument MD, ustandaryzowana struktura (jak w szablonie powyżej), z checkpointem (werdyktem) po każdej rundzie.
