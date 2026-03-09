# WAVE Living Patterns — Ekosystem Żywej Wiedzy Implementacyjnej

## Wersja 3.0 | Marzec 2026
## Rozszerzenie metodyki WAVE (Workflow Amplification via Vectored Expertise)

**Autor:** Przemek Zieliński  
**Opracowanie:** Claude Opus 4.6  
**Licencja:** CC BY-SA 4.0 (spójna z licencją WAVE Methodology)  
**Repozytorium źródłowe:** github.com/przemek-zielinski/WAVE-Methodology

---

## Spis treści

0. Szybki Start — zacznij tutaj
1. Czym jest ekosystem WAVE Living Patterns
2. Problem który rozwiązujemy
3. Trzy elementy ekosystemu
4. SCAN — rozpoznanie terenu
5. PULSE — budowanie Żywego Wzorca
6. Living Pattern — żyjący dokument wiedzy
7. Cykl życia — od SCAN do auto-doskonalenia
8. Posługiwanie się ekosystemem — przewodnik krok po kroku
9. Auto-doskonalenie — mechanizm cyklicznej aktualizacji
10. Model open source — oficjalne i społecznościowe wzorce
11. Relacja z metodyką WAVE
12. Przykład zastosowania — IDareU Gen2
13. Słownik pojęć

---

## 0. Szybki Start — zacznij tutaj

Nie chcesz czytać 13 sekcji zanim zaczniesz? Oto minimum:

**Co to jest:** Zestaw narzędzi do budowania kompletnej bazy wiedzy dla każdego obszaru Twojego projektu (UX, baza danych, bezpieczeństwo, itd.) — żebyś działał na najlepszych możliwych założeniach, a nie na intuicji.

**Jak to działa w trzech krokach:**

Krok 1: **SCAN** — podajesz opis swojego rozwiązania, dostajesz listę wszystkich obszarów które musisz zbadać. Korzystasz z pliku `SCAN-Prompt.md`.

Krok 2: **PULSE** — dla każdego obszaru z listy uruchamiasz trzy rundy badawcze. Runda 1 buduje rdzeń wiedzy. Runda 2 weryfikuje z innego kąta. Runda 3 szuka w peryferyjnych kierunkach. Korzystasz z pliku `PULSE-Prompt.md`.

Krok 3: **Living Pattern** — efektem jest żywy dokument z zasadami, standardami, matrycą błędów i metrykami dla danego obszaru. Dokument cyklicznie sprawdza swoją aktualność.

**Czego potrzebujesz:** Dostęp do AI z możliwością wyszukiwania internetowego (Claude, ChatGPT, Gemini z włączonym web search). Opis swojego rozwiązania. Opcjonalnie: materiały wewnętrzne projektu.

**Od czego zacząć:** Przeczytaj `SCAN-HowTo.md`, wypełnij prompt `SCAN-Prompt.md`, uruchom w czacie z AI.

Reszta dokumentu wyjaśnia DLACZEGO to działa, JAK jest zbudowane i JAK z tego korzystać zaawansowanie. Czytaj dalej gdy będziesz gotowy.

---

## 1. Czym jest ekosystem WAVE Living Patterns

Ekosystem WAVE Living Patterns to zestaw trzech narzędzi opartych na współpracy człowiek-AI, które razem tworzą zamknięty cykl: rozpoznanie terenu implementacyjnego, zbudowanie kompletnej bazy wiedzy dla każdego obszaru, a następnie utrzymywanie tej wiedzy w stanie aktualnym przez cykliczne auto-doskonalenie.

To nie jest dokumentacja projektu. To nie jest podręcznik. To nie jest Biała Księga która się publikuje i leży na półce.

Living Pattern to **żywy dokument**, który zawiera najlepszą dostępną wiedzę — naukową, branżową i praktyczną — dla konkretnego obszaru implementacyjnego, i który regularnie sprawdza sam siebie pod kątem aktualności. Jak organizm, który oddycha — wdech to nowa wiedza z otoczenia, wydech to aktualizacja dokumentu.

Ekosystem składa się z trzech poziomów:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Poziom 3:   SCAN                                  │
│   Co robi:    Rozpoznaje teren — identyfikuje       │
│               WSZYSTKIE obszary implementacyjne      │
│               dla danego rozwiązania                 │
│   Kiedy:      Raz, na początku projektu             │
│                                                     │
│               ┌──────────────────────┐              │
│               │  Lista obszarów      │              │
│               │  + funkcje celu      │              │
│               │  + parametry         │              │
│               └──────────┬───────────┘              │
│                          ↓                          │
│   Poziom 2:   PULSE                                 │
│   Co robi:    Buduje Living Pattern dla JEDNEGO     │
│               obszaru (3 rundy kreacji)             │
│   Kiedy:      Dla każdego obszaru z listy SCAN      │
│                                                     │
│               ┌──────────────────────┐              │
│               │  Living Pattern v3   │              │
│               │  (kompletny wzorzec) │              │
│               └──────────┬───────────┘              │
│                          ↓                          │
│   Poziom 1:   Living Pattern                        │
│   Co robi:    Żyje — cyklicznie sprawdza            │
│               swoją aktualność i doskonali się      │
│   Kiedy:      Ciągle, w rytmie odpowiednim          │
│               dla danego obszaru                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 2. Problem który rozwiązujemy

Każdy zespół budujący produkt cyfrowy staje przed tym samym pytaniem: **„Czy działamy na najlepszych możliwych założeniach?"**

Zwykle odpowiedź brzmi jedno z trzech:

**„Nie wiemy, bo nie mieliśmy czasu sprawdzić."** Zespół rzuca się w implementację z wiedzą którą ma — z poprzednich projektów, z treningu modelu AI, z intuicji lidera technicznego. Błędy wychodzą miesiące później, kosztowne do naprawy.

**„Sprawdziliśmy, ale to było pół roku temu."** Branżowe najlepsze praktyki się zmieniają. Regulacje się zmieniają. Nowe narzędzia się pojawiają. Wiedza z początku projektu starzeje się szybciej niż projekt postępuje.

**„Każdy z nas sprawdził coś innego."** Programista czytał dokumentację frameworka. Projektant przeglądał trendy UX. Product owner rozmawiał z użytkownikami. Ale nikt nie zsyntezował tego w spójny obraz pod jedną funkcją celu.

Living Patterns rozwiązują te trzy problemy jednocześnie:

Dają **kompletny przegląd** najlepszej dostępnej wiedzy (trzy rundy PULSE eliminują luki). Utrzymują wiedzę **aktualną** (mechanizm auto-doskonalenia). Syntetyzują wiedzę **pod konkretną funkcję celu** (parametryzacja PULSE wymusza celowanie, nie zbieranie wszystkiego).

---

## 3. Trzy elementy ekosystemu

### SCAN — Solution Coverage Area Navigator

**Metafora:** Radar który skanuje horyzont i identyfikuje wszystkie obszary wymagające uwagi.

**Co robi:** Na podstawie opisu rozwiązania (co budujemy, dla kogo, w jakiej skali, z jakimi ograniczeniami) identyfikuje kompletną listę obszarów implementacyjnych. Dla każdego obszaru określa funkcję celu, priorytet, zależności od innych obszarów i parametry potrzebne do uruchomienia PULSE.

**Co daje:** Dokument — mapę terenu implementacyjnego z gotowymi instrukcjami do dalszych prac.

**Kiedy używać:** Raz na początku projektu. Opcjonalnie ponownie przy dużej zmianie zakresu.

### PULSE — Pattern Universal Living Standard Engine

**Metafora:** Puls — rytmiczny cykl trzech uderzeń (rund), z których każde przynosi nową warstwę wiedzy.

**Co robi:** Dla jednego obszaru implementacyjnego przeprowadza trzy rundy badawczo-syntetyczne. Runda 1 buduje fundament. Runda 2 weryfikuje z innego kąta. Runda 3 szuka w peryferyjnych kierunkach. Efektem jest kompletny Living Pattern.

**Co daje:** Żywy Wzorzec (Living Pattern) — gotowy do użycia dokument referencyjny.

**Kiedy używać:** Dla każdego obszaru zidentyfikowanego przez SCAN. Rundy wykonywane oddzielnie, z decyzją człowieka między nimi.

### Living Pattern — Żywy Wzorzec

**Metafora:** Żywy organizm — oddycha (pobiera nową wiedzę), rośnie (rozszerza się o nowe odkrycia), dojrzewa (stabilizuje się w sprawdzonych ustaleniach).

**Co robi:** Przechowuje zsyntezowaną wiedzę implementacyjną dla jednego obszaru. Podlega cyklicznej weryfikacji aktualności.

**Co daje:** Pewność że decyzje implementacyjne opierają się na najlepszej dostępnej wiedzy, nie na wiedzy z dnia tworzenia dokumentu.

**Kiedy używać:** Ciągle — jako referencja przy każdej decyzji w danym obszarze.

---

## 4. SCAN — rozpoznanie terenu

### Co SCAN potrzebuje na wejściu

SCAN wymaga od użytkownika czterech informacji:

**Opis rozwiązania** — co budujemy i po co. Nie musi być długi, ale musi być konkretny. „Budujemy platformę edukacyjną" to za mało. „Budujemy trójstronny marketplace łączący mentorów, użytkowników i marki, z mechanizmem wyzwań, feedbacku wideo i gamifikacją opartą na próbach" — to daje SCAN wystarczający kontekst.

**Profil odbiorcy** — kto będzie używał rozwiązania. Wiek, kontekst, urządzenia, poziom zaawansowania technicznego.

**Ograniczenia projektowe** — zespół (ile osób, jakie kompetencje), budżet (orientacyjnie), czas (kiedy ma być gotowe), regulacje (RODO, EAA, branżowe), technologie (czy coś jest już wybrane lub wymuszone).

**Materiały wewnętrzne** — jeśli istnieją: architektura, specyfikacje, Decision Log, dokumentacja istniejącej wersji. SCAN używa ich żeby nie proponować obszarów które są już zamknięte.

### Co SCAN daje na wyjściu

Dokument zawierający:

**Tabelę obszarów implementacyjnych** — kompletna lista, np.: UX/UI, baza danych, architektura API, techstack frontend, techstack backend, DevOps/CI-CD, bezpieczeństwo, model danych, strategia testowania, strategia migracji, infrastruktura sieciowa, SEO/ASO, analityka, dokumentacja techniczna, plan odtwarzania po awarii.

**Dla każdego obszaru:**

Funkcja celu — jedno zdanie definiujące co optymalizujemy. Przykład dla bazy danych: „Integralność danych + wydajność zapytań przy rosnącej bazie + struktura pod unikalny dataset TACIT." Przykład dla bezpieczeństwa: „Ochrona danych użytkowników i mentorów + zgodność z RODO + odporność na ataki typowe dla platform z UGC."

Priorytet — krytyczny (blokuje resztę), ważny (wpływa na jakość), pożądany (podnosi standard).

Zależności — np. „architektura API zależy od decyzji o bazie danych i techstack backend."

Parametry do PULSE — gotowe wartości do wstawienia w prompt PULSE: nazwa obszaru, funkcja celu, lista plików wewnętrznych do przeczytania, specyficzne pytania badawcze.

**Rekomendowaną kolejność** — w jakiej sekwencji uruchamiać PULSE żeby respektować zależności.

### Jak posługiwać się SCAN

Krok 1: Przygotuj cztery informacje wejściowe (opis, profil, ograniczenia, materiały).

Krok 2: Uruchom prompt SCAN w nowym czacie z AI. Dołącz materiały wewnętrzne jako pliki lub odniesienia.

Krok 3: Otrzymujesz mapę obszarów. Przejrzyj ją. Dodaj obszary które znasz z doświadczenia a których AI mogło nie zidentyfikować. Usuń te, które nie mają zastosowania.

Krok 4: Zatwierdź kolejność i zacznij uruchamiać PULSE dla poszczególnych obszarów.

SCAN uruchamia się raz. Wynik to dokument który służy jako mapa drogowa dla wszystkich późniejszych prac PULSE.

---

## 5. PULSE — budowanie Żywego Wzorca

### Filozofia trzech rund

PULSE nie jest jednorazowym przeszukaniem internetu. To jest trzyetapowy proces, w którym każda runda celowo szuka z INNEGO kąta niż poprzednia. Mechanizm opiera się na obserwacji potwierdzonej praktyką:

**Runda 1 (Budowa)** — daje ~60% wartości. Buduje rdzeń wiedzy: fundamenty naukowe, konsensus branżowy, sprawdzone praktyki, główne case studies.

**Runda 2 (Optymalizacja)** — daje ~25% wartości. Weryfikuje rdzeń z drugiej strony: szuka porażek zamiast sukcesów, kontrowersji zamiast konsensusu, głosów mniejszości zamiast mainstream. Znajduje luki które Runda 1 pominęła.

**Runda 3 (Finalizacja)** — daje ~12% wartości. Szuka w peryferyjnych kierunkach: aspekty prawne, dostępność, edge case'y, perspektywa 2–3 lat do przodu. Znajduje wzmocnienia które podnoszą dokument z „bardzo dobrego" na „doskonały".

Pozostałe ~3% wymagałoby czwartej rundy, która nie jest warta zatrzymania projektu. To jest krzywa malejących przyrostów — naturalny punkt nasycenia.

### Dlaczego trzy ODDZIELNE rundy, nie jedna z trzema podpunktami

Trzy powody wynikające z praktyki:

**Jakość.** Gdy AI wie od początku że będzie trzy rundy, podświadomie „rezerwuje" materiał na później zamiast dać wszystko w pierwszej rundzie. Oddzielne rundy wymuszają za każdym razem pełny wysiłek.

**Zmiana kontekstu.** Między rundami AI wraca z NOWYM kontekstem zdobytym w nowym researchu. To co znajdzie w Rundzie 2 zmienia perspektywę — i trzecia runda jest celniejsza niż byłaby gdyby była zaplanowana od początku.

**Decyzyjność człowieka.** Między rundami człowiek ocenia efekt, może zmienić kierunek, może zatwierdzić fragment i poprosić o pogłębienie innego. Ta elastyczność jest niemożliwa w jednorazowym podejściu.

### Co PULSE potrzebuje na wejściu

Pięć parametrów, z których trzy są obowiązkowe:

**[OBSZAR]** (obowiązkowy) — nazwa obszaru implementacyjnego. Przykład: „Baza danych", „UX/UI interfejsów", „Architektura API", „Strategia testowania".

**[FUNKCJA CELU]** (obowiązkowy) — jedno zdanie definiujące co optymalizujemy w tym obszarze. To jest kompas całego procesu — każda znaleziona wiedza jest oceniana pytaniem „czy to przybliża do funkcji celu?" Przykład: „Maksymalizacja efektu WOW na użytkowniku przy pierwszym i kolejnym kontakcie z serwisem."

**[KONTEKST ROZWIĄZANIA]** (obowiązkowy) — krótki opis budowanego produktu i jego specyfiki. PULSE musi wiedzieć CZY szuka wzorców dla platformy społecznościowej, systemu bankowego czy aplikacji medycznej — bo najlepsze praktyki są różne.

**[MATERIAŁY WEWNĘTRZNE]** (opcjonalny, ale silnie zalecany) — lista plików wewnętrznych projektu które AI powinno przeczytać PRZED researchem zewnętrznym. Znajomość istniejącej architektury i decyzji zamienia generyczny research w celowany.

**[OGRANICZENIA]** (opcjonalny) — budżet, czas, zespół, regulacje, wybrane technologie. Pozwala PULSE filtrować rekomendacje — nie proponować rozwiązań które są poza zasięgiem.

### Co PULSE daje na wyjściu

Living Pattern — dokument MD o ustandaryzowanej strukturze (opisanej w sekcji 6).

### Jak posługiwać się PULSE

**Przygotowanie:** Wypełnij pięć parametrów. Jeśli korzystałeś z SCAN — parametry dla Twojego obszaru są już gotowe w dokumencie wyjściowym SCAN.

**Runda 1 — Budowa:**

Otwórz nowy czat z AI. Podaj prompt PULSE z wypełnionymi parametrami. AI przeczyta materiały wewnętrzne, przeprowadzi wielowarstwowy research (nauka → branża → praktyka), zsyntezuje wyniki w dokument.

Otrzymujesz Living Pattern v1. Przeczytaj go. Oceń: czy rdzeń wiedzy jest sensowny? Czy czegoś oczywistego brakuje? Jeśli masz uwagi — przekaż je przed Rundą 2.

**Runda 2 — Optymalizacja:**

W TYM SAMYM czacie powiedz AI: uruchom Rundę 2 weryfikacji. AI zmienia kąt ataku — szuka tego, czego nie znalazło w Rundzie 1. Szuka porażek, kontrowersji, alternatywnych podejść. Dodaje znaleziska z oznaczeniem [NOWE v2] lub [WZMOCNIONE v2].

Otrzymujesz Living Pattern v2. Przeczytaj uzupełnienia. Oceń: czy weryfikacja znalazła istotne luki? Czy dodane elementy mają praktyczną wartość?

**Runda 3 — Finalizacja:**

W TYM SAMYM czacie powiedz AI: uruchom Rundę 3 — peryferyjne kierunki. AI szuka w obszarach które typowy research pomija: regulacje prawne, dostępność, wydajność, edge case'y, perspektywa przyszłości.

Otrzymujesz Living Pattern v3 + werdykt AI czy fundament jest kompletny. Jeśli tak — Living Pattern jest gotowy do użycia i auto-doskonalenia.

**Ważna zasada:** Między rundami to CZŁOWIEK decyduje czy iść dalej, czy zmienić kierunek, czy zakończyć wcześniej. AI proponuje, człowiek zatwierdza. To jest rdzeń filozofii WAVE.

---

## 6. Living Pattern — żyjący dokument wiedzy

### Ustandaryzowana struktura

Każdy Living Pattern, niezależnie od obszaru, ma tę samą strukturę. Standaryzacja pozwala szybko nawigować między wzorcami z różnych obszarów — szukasz informacji w tym samym miejscu.

```
LIVING PATTERN: [NAZWA OBSZARU]
│
├── NAGŁÓWEK
│   ├── Nazwa obszaru
│   ├── Wersja (v1 / v2 / v3 / v3.1 / ...)
│   ├── Data utworzenia
│   ├── Data ostatniej aktualizacji
│   ├── Funkcja celu
│   ├── Kontekst rozwiązania
│   └── Status (aktywny / zarchiwizowany / wymaga aktualizacji)
│
├── CZĘŚĆ I — STAN WIEDZY
│   ├── Co wiemy na pewno (konsensus naukowy i branżowy)
│   ├── Co jest dyskusyjne (rozbieżne stanowiska, brak konsensusu)
│   └── Co się zmienia (trendy, kierunki rozwoju)
│
├── CZĘŚĆ II — ZASADY I STANDARDY
│   ├── Zasady projektowe (reguły kierunkowe)
│   ├── Standardy i wymagania (mierzalne wymagania)
│   └── Implikacje dla ekosystemu rozwiązania
│
├── CZĘŚĆ III — MATRYCA BŁĘDÓW
│   ├── Błędy krytyczne (zagrażają produktowi)
│   ├── Błędy poważne (obniżają jakość)
│   └── Błędy subtelne (ograniczają doskonałość)
│   Dla każdego: opis → skutek → ochrona
│
├── CZĘŚĆ IV — MATRYCA DECYZJI
│   ├── Kluczowe wybory do podjęcia
│   ├── Warianty dla każdego wyboru
│   └── Kryteria decyzji i rekomendacje
│
├── CZĘŚĆ V — METRYKI SUKCESU
│   ├── Metryki wiodące (leading indicators)
│   ├── Metryki opóźnione (lagging indicators)
│   └── Alarmy (progi wymagające interwencji)
│
├── CZĘŚĆ VI — ŹRÓDŁA I REFERENCJE
│   ├── Badania naukowe (z datami, autorami, wynikami)
│   ├── Raporty branżowe (z nazwami firm i konkretnymi danymi)
│   ├── Case studies (z liczbami i kontekstem)
│   └── Dokumentacja wewnętrzna projektu
│
└── DZIENNIK ZMIAN
    ├── v1 — [data] — Runda 1 (Budowa)
    ├── v2 — [data] — Runda 2 (Optymalizacja) — [X nowych elementów]
    ├── v3 — [data] — Runda 3 (Finalizacja) — [Y nowych elementów]
    └── v3.1 — [data] — Auto-doskonalenie — [co zmieniono i dlaczego]
```

### Cechy charakterystyczne Living Pattern

**Konkretność.** Każda zasada, reguła i rekomendacja ma trzy elementy: uzasadnienie (dlaczego), miarę (jak zmierzyć) i implikację (co to oznacza dla projektu). Nie „bądź szybki" lecz „LCP poniżej 2,5 sekundy na mobile 4G, bo 90% użytkowników odchodzi powyżej 3 sekund (Google Mobile Optimization Report)."

**Źródła.** Każde twierdzenie ma źródło. Nie „badania pokazują" lecz „Lindgaard i in. (2006), replikowane przez Google Research." Źródła pozwalają zespołowi weryfikować ustalenia i pogłębiać wiedzę.

**Celowość.** Każdy element oceniany pytaniem: „Czy to przybliża do funkcji celu?" Jeśli nie — nie trafia do dokumentu. Living Pattern nie jest encyklopedią — jest narzędziem decyzyjnym.

**Wersjonowanie.** Każda zmiana jest oznaczona i datowana. Zespół widzi co się zmieniło i kiedy. Nowe elementy z Rundy 2 oznaczone [NOWE v2], z Rundy 3 oznaczone [NOWE v3], z auto-doskonalenia oznaczone datą i źródłem aktualizacji.

---

## 7. Cykl życia — od SCAN do auto-doskonalenia

Pełny cykl życia ekosystemu Living Patterns wygląda następująco:

### Faza 1 — Rozpoznanie (SCAN)

Użytkownik dostarcza opis rozwiązania. SCAN identyfikuje obszary. Użytkownik zatwierdza listę. Czas: jedna sesja z AI.

### Faza 2 — Budowanie wzorców (PULSE × N)

Dla każdego obszaru z listy SCAN użytkownik uruchamia PULSE. Każdy PULSE to trzy rundy w jednym czacie, rozdzielone decyzją użytkownika. Czas per obszar: jedna sesja z AI (2–4 godziny pracy AI, ~30 minut pracy człowieka na ocenę i decyzje między rundami). Wynik: kolekcja Living Patterns pokrywająca cały teren implementacyjny.

### Faza 3 — Użytkowanie

Zespół używa Living Patterns jako referencji przy każdej decyzji implementacyjnej. Projektant otwiera Living Pattern UX/UI przed rysowaniem ekranów. Programista otwiera Living Pattern Database przed projektowaniem schematów. Product owner otwiera Living Pattern Analityka przed definiowaniem metryk.

### Faza 4 — Auto-doskonalenie

W rytmie odpowiednim dla danego obszaru (patrz sekcja 9), Living Pattern przechodzi cykl weryfikacji aktualności. Efektem jest albo potwierdzenie „wzorzec aktualny" albo aktualizacja z oznaczeniem co się zmieniło i dlaczego.

### Faza 5 — Archiwizacja lub ewolucja

Gdy projekt jest zakończony — Living Patterns przechodzą w archiwum (status: zarchiwizowany). Gdy projekt ewoluuje (nowa wersja, nowa skala) — SCAN uruchamia się ponownie, a istniejące Living Patterns są aktualizowane lub rozszerzane.

---

## 8. Posługiwanie się ekosystemem — przewodnik krok po kroku

### Scenariusz: Zaczynasz nowy projekt

**Krok 1.** Opisz swoje rozwiązanie — co budujesz, dla kogo, z jakimi ograniczeniami.

**Krok 2.** Uruchom SCAN. Otwórz czat z AI, podaj prompt SCAN z opisem rozwiązania i materiałami wewnętrznymi (jeśli masz). Otrzymasz mapę obszarów z parametrami.

**Krok 3.** Przejrzyj mapę. Dodaj brakujące obszary z własnego doświadczenia. Oceń priorytety. Ustal kolejność.

**Krok 4.** Uruchom PULSE dla pierwszego obszaru. Otwórz nowy czat, podaj prompt PULSE z parametrami z mapy SCAN. Przeprowadź trzy rundy. Otrzymaj Living Pattern.

**Krok 5.** Powtórz Krok 4 dla kolejnych obszarów. Każdy PULSE w oddzielnym czacie (świeży kontekst = lepsza jakość).

**Krok 6.** Masz kolekcję Living Patterns. Używaj ich jako referencji w pracy implementacyjnej. Ustaw rytm auto-doskonalenia.

### Scenariusz: Dołączasz do istniejącego projektu

**Krok 1.** Sprawdź czy projekt ma Living Patterns. Jeśli tak — przeczytaj je jako wprowadzenie do stanu wiedzy projektu (szybsze niż rozmowy z zespołem o „dlaczego zdecydowaliśmy się na X").

**Krok 2.** Jeśli Living Patterns nie istnieją — uruchom SCAN i PULSE dla kluczowych obszarów. Nawet post factum, Living Pattern porządkuje wiedzę rozproszoną w głowach członków zespołu.

### Scenariusz: Projekt zmienia kierunek

**Krok 1.** Uruchom SCAN ponownie z nowym opisem rozwiązania. Porównaj nową mapę ze starą — które obszary się zmieniły?

**Krok 2.** Dla zmienionych obszarów uruchom PULSE od nowa (lub Rundę 2–3 weryfikacji istniejącego Living Pattern z nową funkcją celu).

---

## 9. Auto-doskonalenie — mechanizm cyklicznej aktualizacji

### Jak działa auto-doskonalenie

Cykl auto-doskonalenia Living Pattern przebiega w pięciu krokach:

Krok 1: AI otrzymuje istniejący Living Pattern jako kontekst.

Krok 2: AI przeszukuje internet pod kątem zmian w danym obszarze od daty ostatniej aktualizacji. Szuka nowych badań, nowych narzędzi, zmian w regulacjach, nowych case studies, nowych trendów.

Krok 3: AI porównuje znaleziska z istniejącymi ustaleniami w Living Pattern.

Krok 4: Jeśli znaleziska są istotne — AI proponuje konkretne zmiany z uzasadnieniem i źródłem. Jeśli nie — AI potwierdza aktualność wzorca.

Krok 5: Człowiek przegląda propozycje i zatwierdza lub odrzuca. Zatwierdzone zmiany trafiają do Living Pattern z oznaczeniem daty i źródła w Dzienniku zmian.

### Rytm auto-doskonalenia

Nie każdy obszar zmienia się w tym samym tempie. Rytm aktualizacji powinien odpowiadać szybkości zmian:

| Szybkość zmian | Przykłady obszarów | Zalecany rytm |
|---|---|---|
| Szybka (tygodnie) | Trendy UX/UI, frameworki frontend, narzędzia AI | Co miesiąc |
| Umiarkowana (miesiące) | Architektura systemów, bazy danych, bezpieczeństwo | Co kwartał |
| Wolna (lata) | Fundamenty naukowe, psychologia użytkownika, teoria informacji | Co pół roku |
| Regulacyjna (daty wejścia w życie) | RODO, EAA/WCAG, regulacje branżowe | Przy zmianie regulacji |

### Ograniczenia techniczne na dziś (marzec 2026)

Modele AI (w tym Claude) nie mają wbudowanego mechanizmu automatycznego uruchamiania. Cykliczne auto-doskonalenie wymaga obecnie jednej z dwóch metod:

**Metoda ręczna:** Człowiek otwiera czat z AI w ustalonym rytmie, podaje istniejący Living Pattern i prompt auto-doskonalenia. Wymaga dyscypliny, ale jest natychmiast dostępna.

**Metoda półautomatyczna:** Skrypt (np. cron job + Anthropic API) uruchamia prompt auto-doskonalenia w ustalonym harmonogramie. Wynik trafia do repozytorium jako propozycja zmian (Pull Request). Człowiek przegląda i zatwierdza. Wymaga infrastruktury, ale eliminuje zależność od dyscypliny.

W miarę rozwoju narzędzi AI (scheduled tasks, agentowe przepływy pracy) metoda półautomatyczna będzie się upraszczać.

### Prompt auto-doskonalenia — gotowy do użycia

Poniższy prompt wklejasz w czacie z AI razem z istniejącym Living Pattern jako załącznikiem:

```
WAVE Living Pattern — cykl auto-doskonalenia

Dołączam Living Pattern dla obszaru [NAZWA OBSZARU], ostatnia aktualizacja: [DATA].

Twoim zadaniem jest sprawdzenie aktualności tego dokumentu. Wykonaj:

1. Przeszukaj internet pod kątem ZMIAN w tym obszarze od daty ostatniej aktualizacji.
   Szukaj: nowych badań naukowych, nowych raportów branżowych, zmian w regulacjach,
   nowych narzędzi/frameworków, nowych case studies, zmienionych najlepszych praktyk.

2. Porównaj znaleziska z istniejącymi ustaleniami w Living Pattern.

3. Podaj werdykt w jednym z dwóch formatów:

   FORMAT A — Brak istotnych zmian:
   „Living Pattern aktualny na [DATA]. Sprawdzono [X] źródeł. Brak zmian 
   wymagających aktualizacji. Następne sprawdzenie: [DATA + rytm]."

   FORMAT B — Znaleziono zmiany:
   Dla każdej zmiany podaj:
   - Co się zmieniło (nowe badanie / nowa regulacja / nowe narzędzie / zmiana trendu)
   - Źródło z datą
   - Która sekcja Living Pattern jest dotknięta
   - Proponowana zmiana (dodanie / aktualizacja / usunięcie)
   - Priorytet (krytyczny / ważny / kosmetyczny)

Nie zmieniaj dokumentu samodzielnie — PROPONUJ zmiany. Człowiek zatwierdza.
```

---

## 10. Model open source — oficjalne i społecznościowe wzorce

### Dwa poziomy Living Patterns

**Poziom oficjalny** — Living Patterns utrzymywane przez autora/zespół metodyki WAVE. Gwarancja jakości, regularny rytm auto-doskonalenia, zgodność ze standardami. Publikowane w repozytorium WAVE-Living-Patterns pod licencją CC BY-SA 4.0.

**Poziom społecznościowy** — Living Patterns tworzone przez użytkowników metodyki WAVE dla swoich projektów i udostępniane społeczności. Oznaczone jako „community-contributed". Bez gwarancji jakości, ale z systemem ocen (inne zespoły mogą oceniać przydatność). Najlepsze społecznościowe mogą awansować do oficjalnych po przeglądzie.

### Struktura repozytoriów

```
przemek-zielinski/WAVE-Methodology
    └── Istniejące repo z metodyką WAVE

przemek-zielinski/WAVE-SCAN
    ├── SCAN-Prompt.md          ← prompt SCAN
    └── SCAN-HowTo.md           ← instrukcja użycia

przemek-zielinski/WAVE-PULSE
    ├── PULSE-Prompt.md          ← prompt PULSE
    └── PULSE-HowTo.md           ← instrukcja użycia

przemek-zielinski/WAVE-Living-Patterns
    ├── /official                 ← wzorce oficjalne
    │   ├── UX-UI/
    │   │   └── LP_UX_UI_v3.md
    │   ├── Database/
    │   │   └── LP_Database_v3.md
    │   └── ...
    ├── /community                ← wzorce społecznościowe
    │   ├── Healthcare/
    │   ├── FinTech/
    │   └── ...
    └── CONTRIBUTING.md           ← zasady dodawania wzorców
```

### Efekt dla metodyki WAVE

Trzy poziomy wzmocnienia:

**Bariera wejścia drastycznie spada.** Nowy użytkownik WAVE nie zaczyna od zera — otwiera gotowy Living Pattern dla swojego obszaru i ma natychmiastową bazę wiedzy. Różnica między „przeczytaj metodykę i sam zbierz wiedzę" a „oto gotowy, aktualny wzorzec dla Twojego problemu."

**Efekt sieciowy.** Im więcej użytkowników tworzy Living Patterns i udostępnia je społeczności, tym bogatsza baza wiedzy. Każdy nowy wzorzec zwiększa wartość ekosystemu dla wszystkich.

**Samonapędzający się cykl.** Lepsza baza wzorców → więcej użytkowników → więcej wkładów społecznościowych → jeszcze lepsza baza. To jest ten sam mechanizm efektów sieciowych który IDareU ma na poziomie platformy — tyle że tu dotyczy wiedzy implementacyjnej.

---

## 11. Relacja z metodyką WAVE

### Gdzie Living Patterns siedzą w WAVE

Metodyka WAVE opiera się na zasadzie 70/30 — siedemdziesiąt procent przygotowanie, trzydzieści procent egzekucja. Living Patterns są narzędziem fazy przygotowawczej — ale specyficznym rodzajem przygotowania.

W obecnym modelu WAVE przygotowanie oznacza: zbuduj kompletny kontekst (dokumentacja, wymagania, specyfikacje) ZANIM wejdziesz w implementację. Living Patterns dodają do tego: zbuduj kompletną bazę wiedzy kierunkowej ZANIM zaczniesz projektować i specyfikować.

Sekwencja w rozszerzonym WAVE:

```
FAZA PRZYGOTOWAWCZA (70%)
│
├── KROK 1: SCAN — rozpoznaj teren implementacyjny
├── KROK 2: PULSE — zbuduj Living Patterns dla kluczowych obszarów
├── KROK 3: Projektowanie (specyfikacje, architektura, strumienie sterowania)
│           ↑ informowane przez Living Patterns
└── KROK 4: Przygotowanie dokumentacji dla Claude w Cursor
            ↑ informowane przez Living Patterns

FAZA EGZEKUCYJNA (30%)
│
├── KROK 5: Implementacja z Claude w Cursor
│           ↑ Living Patterns jako referencja dla decyzji w trakcie
└── KROK 6: Weryfikacja i testy
            ↑ metryki sukcesu z Living Patterns jako kryteria akceptacji
```

### Filozoficzna spójność

WAVE mówi: „Człowiek kieruje, AI wzmacnia." Living Patterns realizują tę filozofię w czystej formie: SCAN i PULSE to AI które przetwarza wiedzę ze skali niedostępnej dla człowieka (cały internet, wszystkie badania), ale to człowiek decyduje co jest ważne, co zatwierdzić, kiedy zakończyć. AI jest wzmacniaczem ekspertyzy — nie jej zamiennikiem.

WAVE mówi: „Buduj kompletnie, aktywuj progresywnie." Living Patterns realizują to w swoim mechanizmie: trzy rundy PULSE budują kompletny wzorzec, auto-doskonalenie aktywuje go progresywnie w czasie.

---

## 12. Przykład zastosowania — IDareU Gen2

### Kontekst

IDareU Gen2 to trójstronny marketplace łączący mentorów, użytkowników i marki, z mechanizmem wyzwań, feedbacku wideo, gamifikacji i innowacyjnym modelem podziału przychodów (IdUShare). Techstack: Next.js, TypeScript, Tailwind, Supabase. Zespół korzysta z metodyki WAVE i narzędzia Cursor z Claude.

### SCAN — wynik (przykładowy fragment)

SCAN zidentyfikował następujące obszary dla IDareU Gen2:

| Obszar | Priorytet | Funkcja celu |
|---|---|---|
| UX/UI i User Journey | Krytyczny | Efekt WOW na użytkowniku, maksymalizacja retencji |
| Baza danych i model danych | Krytyczny | Struktura pod TACIT dataset + wydajność + skalowalność |
| Architektura API | Krytyczny | Spójność trójstronnego marketplace + real-time feedback |
| Bezpieczeństwo | Krytyczny | RODO + ochrona danych UGC + zabezpieczenie transakcji |
| Frontend techstack | Ważny | Szybkość implementacji WAVE + Living Interface compatibility |
| Backend techstack | Ważny | Wydajność + skalowalność + koszt utrzymania |
| DevOps / CI-CD | Ważny | Szybkość deploymentu + stabilność + monitoring |
| Strategia testowania | Ważny | Pokrycie krytycznych ścieżek + automatyzacja |
| SEO / ASO | Pożądany | Widoczność organiczna + optymalizacja app store |
| Analityka i metryki | Pożądany | Mierzenie Living Patterns KPIs + panel admina |

### PULSE — wynik (zrealizowany)

Pierwszy Living Pattern zrealizowany w praktyce: **LP_UX_UI_v3** — Fundament Projektowy UX/UI IDareU Gen2. Trzy rundy (8–9 marca 2026), osiemnaście zasad projektowych, dwadzieścia pięć pozycji w matrycy błędów, kompletne metryki, integracja z Living Interface i Wise Internet.

Ten Living Pattern posłuży jako wzorzec struktury i jakości dla wszystkich kolejnych Living Patterns w projekcie IDareU Gen2.

---

## 13. Słownik pojęć

**Living Pattern (Żywy Wzorzec)** — dokument zawierający zsyntezowaną, aktualną wiedzę implementacyjną dla jednego obszaru projektu. Podlega cyklicznej weryfikacji i auto-doskonaleniu.

**SCAN (Solution Coverage Area Navigator)** — prompt AI identyfikujący kompletną listę obszarów implementacyjnych dla danego rozwiązania, wraz z funkcjami celu i parametrami dla każdego.

**PULSE (Pattern Universal Living Standard Engine)** — prompt AI budujący Living Pattern w trzech rundach: Budowa → Optymalizacja → Finalizacja.

**Runda** — jeden przebieg badawczo-syntetyczny w ramach PULSE. Każda runda celowo szuka z innego kąta niż poprzednia.

**Funkcja celu** — jedno zdanie definiujące co optymalizujemy w danym obszarze. Kompas całego procesu — każda znaleziona wiedza oceniana pytaniem „czy to przybliża do funkcji celu?"

**Auto-doskonalenie** — cykliczny mechanizm weryfikacji aktualności Living Pattern przez ponowne przeszukanie źródeł i porównanie ze stanem dokumentu.

**Krzywa malejących przyrostów** — obserwacja że kolejne rundy PULSE dają coraz mniej nowej wartości (60% → 25% → 12% → ~3%). Naturalne uzasadnienie dla trzech rund jako optymalnej liczby.

**Zmiana kąta ataku** — celowa zmiana perspektywy badawczej między rundami. Runda 1 szuka sukcesów, Runda 2 szuka porażek, Runda 3 szuka w peryferyjnych kierunkach.

**Materiały wewnętrzne** — istniejąca dokumentacja projektu (architektura, specyfikacje, Decision Log) podawana jako kontekst dla SCAN i PULSE. Zamienia generyczny research w celowany.

**Wzorzec oficjalny** — Living Pattern utrzymywany przez autora/zespół metodyki WAVE, z gwarancją jakości i regularnym auto-doskonaleniem.

**Wzorzec społecznościowy** — Living Pattern stworzony i udostępniony przez użytkownika metodyki WAVE, oznaczony jako „community-contributed".

---

*Dokument opracowany: 9 marca 2026*
*Wersja: 3.0*
*Autor koncepcji: Przemek Zieliński*
*Opracowanie: Claude Opus 4.6*
*Licencja: CC BY-SA 4.0*
*Powiązane: WAVE Methodology (github.com/przemek-zielinski/WAVE-Methodology)*
