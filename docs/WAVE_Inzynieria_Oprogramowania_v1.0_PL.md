# WAVE w wytwarzaniu oprogramowania

## Workflow Amplification via Vectored Expertise — zastosowanie w software development

### Pierwsze i najgłębsze studium przypadku

**Wersja:** 1.0  
**Data:** 15 lutego 2026  
**Autor:** Przemysław Zieliński  
**Współtwórca dokumentacji:** Claude (Anthropic)  
**Licencja:** CC BY-SA 4.0  
**Wymaga znajomości:** [Metodyka WAVE/FALA (rdzeń generyczny)](FALA_Metodyka_v1.0_PL.md)

---

## Spis treści

1. [Dlaczego oprogramowanie jako pierwsze](#1-dlaczego-oprogramowanie-jako-pierwsze)
2. [Problem znany każdemu programiście](#2-problem-znany-każdemu-programiście)
3. [Trzy warstwy w kodzie](#3-trzy-warstwy-w-kodzie)
4. [Model operacyjny — narzędzia, silniki, rytm dnia](#4-model-operacyjny)
5. [Przed i po — konkretne przykłady](#5-przed-i-po)
6. [Mierniki z pola walki](#6-mierniki-z-pola-walki)
7. [Czym WAVE różni się od istniejących podejść](#7-czym-wave-różni-się-od-istniejących-podejść)
8. [Jak zacząć — dla programistów](#8-jak-zacząć)
9. [Typowe pułapki](#9-typowe-pułapki)
10. [Kierunki rozwoju](#10-kierunki-rozwoju)

---

## 1. Dlaczego oprogramowanie jako pierwsze

Wytwarzanie oprogramowania to naturalny poligon doświadczalny dla metodyki współpracy człowiek-AI. Programiści byli jednymi z pierwszych, którzy przyjęli AI jako codzienne narzędzie — przez generatory kodu, asystentów programowania w parach i agentyczne środowiska kodowania. Pętle zwrotne są szybkie: piszesz prompt, dostajesz kod, uruchamiasz go i natychmiast wiesz czy działa.

To czyni oprogramowanie idealną dziedziną do walidacji rdzenia WAVE:

- Że 70% przygotowania i 30% realizacji bije chaotyczne promptowanie.
- Że trzy warstwy (DataPrep, Prompt2Data, Prompt2Prompt) tworzą samodoskonalący się system.
- Że mierniki jak PSR i TFCO da się śledzić i poprawiać.

Wszystko w tym dokumencie zostało przetestowane podczas realnej budowy złożonej platformy webowej (IDareU V2) przez jednego programistę pracującego z AI. Liczby, przykłady i przepływy pracy poniżej pochodzą z tego doświadczenia.

Jeśli nie czytałeś jeszcze generycznego rdzenia WAVE — zacznij tam. Tamten dokument wyjaśnia filozofię, zasady i zastosowania w wielu branżach. Ten dokument zakłada znajomość trzech warstw i skupia się na ich przełożeniu na kod, prompty, szablony i codzienną praktykę.

---

## 2. Problem znany każdemu programiście

Siadasz do budowy funkcjonalności. Otwierasz asystenta AI i piszesz:

```
„Zbuduj mi system autentykacji użytkowników z email/hasło, 
OAuth i obsługą 2FA"
```

AI generuje kod. Uruchamiasz. Połowy funkcji brakuje. Konwencje nazewnicze nie pasują do projektu. Obsługa błędów jest niespójna. Typy są źle dobrane.

Poprawiasz. AI regeneruje. Lepiej, ale zarządzanie sesją koliduje z istniejącą konfiguracją JWT. Tłumaczysz konflikt. AI naprawia jedno, psuje drugie. Trzy godziny i dziesięć iteracji później masz kod, który działa — ale jest kruchy, niespójny z resztą projektu i nieudokumentowany.

To nie jest porażka zdolności AI. Współczesne modele AI potrafią pisać znakomity kod. Porażka leży w schemacie współpracy: **programista nie dał AI tego, czego potrzebowało żeby trafić za pierwszym razem.**

WAVE rozwiązuje to odwracając proporcje czasu. Zamiast 10% myślenia i 90% iterowania, poświęcasz 70% na przygotowanie i 30% na realizację. Efekt: skuteczność pierwszej próby powyżej 80%, współczynnik rewizji poniżej 1,5 i czas wytworzenia krótszy o 25-33%.

---

## 3. Trzy warstwy w kodzie

### Warstwa 1: DataPrep dla oprogramowania

W software DataPrep to hierarchia dokumentów opisujących projekt od wizji po specyfikacje pojedynczych funkcji. Każdy dokument generuje następny.

```
Poziom 1.1: Wizja produktu
  „Platforma gamifikowanego uczenia — trójstronny rynek"
    ↓ generuje
Poziom 1.2: Wymagania biznesowe
  „Autentykacja, tworzenie wyzwań, upload video, 
   płatności, system gamifikacji..."
    ↓ generuje
Poziom 1.3: Architektura
  „Next.js + TypeScript + Tailwind + Supabase, 
   monorepo, API routes, RLS..."
    ↓ generuje
Poziom 1.4: Specyfikacje komponentów
  „AuthService: email/hasło + OAuth + 2FA
   ChallengeService: CRUD + video + ocenianie
   PaymentService: model podziału IdUShare..."
    ↓ generuje
Poziom 1.5: Specyfikacje na poziomie funkcji
  „validateEmail(): wejście string, wyjście ValidationResult,
   zgodność z RFC 5322, sprawdzenie domen jednorazowych..."
```

**Kluczowa zasada:** kompletność na każdym poziomie ma większe znaczenie niż głębokość na jednym poziomie. AI potrafi wygenerować kompletną funkcję z kompletnej specyfikacji komponentu. Nie potrafi wygenerować kompletnego komponentu z fragmentu architektury.

**Co wchodzi w skład DataPrep dla oprogramowania:**

| Dokument                 | Zawartość                                                    | Tworzy podstawę dla           |
| ------------------------ | ------------------------------------------------------------ | ----------------------------- |
| Wizja produktu           | Misja, wartość, docelowi użytkownicy                         | Wymagania biznesowe           |
| Wymagania biznesowe      | Wymagania funkcjonalne i niefunkcjonalne, priorytetyzacja (MoSCoW) | Decyzje architektoniczne      |
| Dokument architektury    | Stack, diagram systemu, przepływ danych, model bezpieczeństwa | Specyfikacje komponentów      |
| Specyfikacje komponentów | Każdy moduł: wejścia, wyjścia, interfejsy, zależności        | Specyfikacje funkcji, prompty |
| Przewodnik stylu         | Konwencje nazewnicze, wzorce obsługi błędów, organizacja kodu | Każdy prompt                  |
| Model danych             | Relacje encji, typy pól, indeksy, ograniczenia               | Prompty backendowe            |
| Kontrakty API            | Endpointy, formaty żądań/odpowiedzi, wymagania autoryzacji   | Prompty front i back          |
| Strategia testów         | Cele pokrycia, typy testów, kategorie przypadków brzegowych  | Prompty testowe               |

**Rada praktyczna:** Nie potrzebujesz tego wszystkiego pierwszego dnia. Zacznij od Wizji + Architektury + Przewodnika stylu. Te trzy dokumenty same drastycznie poprawią skuteczność Twoich promptów, bo dają AI trzy rzeczy, których najbardziej potrzebuje: co budujesz, jak to jest zorganizowane i jakie konwencje obowiązują.

### Warstwa 2: Prompt2Data dla oprogramowania

Prompt WAVE do generowania kodu nie jest prośbą — to kontrakt. Mówi AI dokładnie co zbudować, z jakimi ograniczeniami, w jakim formacie i jak ocenimy sukces.

**Anatomia promptu WAVE do generowania kodu:**

```markdown
## Kontekst (z DataPrep)
Projekt: IDareU V2 — platforma gamifikowanego uczenia
Stack: Next.js 14, TypeScript strict, Tailwind CSS, Supabase
Lokalizacja: /lib/services/auth/emailAuth.ts
Powiązane: specyfikacja komponentu AuthService [link]

## Zadanie
Wygeneruj klasę EmailAuthProvider implementującą autentykację 
email/hasło z haszowaniem bcrypt i zarządzaniem sesją JWT.

## Ograniczenia
- TypeScript strict, żadnych typów `any`
- Bez zewnętrznych bibliotek auth (Supabase obsługuje OAuth osobno)
- Komunikaty błędów jako kody i18n, nie hardkodowane stringi
- Wszystkie operacje async z try/catch
- Logowanie przez Winston (już skonfigurowany)

## Dane wejściowe
- Schemat tabeli User: [z modelu danych]
- Konfiguracja JWT: sekret z env, wygaśnięcie 24h, refresh token 7d
- Limitowanie prób: 5 na 15 minut na IP
- Polityka haseł: min 8 znaków, 1 wielka litera, 1 cyfra

## Oczekiwany wynik
- Kompletna klasa TypeScript ze wszystkimi metodami
- Metody: register(), login(), resetPassword(), verifyEmail()
- Każda metoda zwraca typowany Result<T, AuthError>
- Metody prywatne z prefiksem _

## Kryteria sukcesu
- Kompiluje się z zerem błędów TypeScript
- Stosuje konwencje nazewnicze projektu
- Obsługuje wszystkie przypadki brzegowe poniżej
- Gotowy do testów jednostkowych (wstrzykiwanie zależności Supabase)

## Przypadki brzegowe
- Email już zarejestrowany → błąd DUPLICATE_EMAIL
- Nieprawidłowy format hasła → PASSWORD_POLICY_VIOLATION
- Konto zablokowane po 5 nieudanych próbach → ACCOUNT_LOCKED
- Wygasły token weryfikacji → TOKEN_EXPIRED
- Awaria połączenia z bazą → łagodna degradacja
```

**Wynik:** AI generuje kompletną, poprawną, testowalną klasę za pierwszym razem — bo ma wszystko czego potrzebuje.

### Warstwa 3: Prompt2Prompt dla oprogramowania

Meta-prompty to szablony definiujące jak tworzyć prompty dla powtarzalnych typów zadań. W oprogramowaniu najczęstsze typy to:

- **Meta-prompt generowania kodu** — do pisania nowych funkcji, komponentów i serwisów
- **Meta-prompt przeglądu kodu** — do żądania przeglądów architektonicznych i jakościowych
- **Meta-prompt badania błędów** — do analizy awarii z pełnym kontekstem
- **Meta-prompt refaktoryzacji** — do restrukturyzacji istniejącego kodu
- **Meta-prompt pisania testów** — do generowania zestawów testów ze specyfikacji
- **Meta-prompt dokumentacji** — do generowania dokumentacji technicznej z kodu
- **Meta-prompt analizy architektury** — do oceny decyzji projektowych

Każdy meta-prompt zawiera: kiedy go użyć, jakie dokumenty DataPrep dołączyć, strukturę promptu, listę kontrolną jakości i typowe pułapki.

**Siła meta-promptingu:** gdy szablon jest sprawdzony przez 10-20 użyć, każde nowe zadanie tego typu staje się uzupełnianiem pól. Myślenie zostało wykonane. Jakość jest wbudowana. Realizacja jest szybka i spójna.

Meta-prompty ewoluują. Po 50 użyciach dodajesz sekcję „Typowe pułapki" na podstawie zaobserwowanych wzorców. Po 100 użyciach przebudowujesz szablon od nowa. To rekurencyjne doskonalenie WAVE w działaniu.

---

## 4. Model operacyjny

WAVE w oprogramowaniu to nie tylko trzy warstwy na papierze. Obejmuje konkretny model operacyjny — które narzędzia AI używać, kiedy i jak zorganizować dzień pracy.

### Macierz doboru narzędzi

| Co robisz                                       | Silnik AI               | Interfejs            | Dlaczego                                       |
| ----------------------------------------------- | ----------------------- | -------------------- | ---------------------------------------------- |
| Architektura, strategia, synteza                | Najpotężniejszy model   | Chat                 | Głębokie rozumowanie, widzi całość             |
| Codzienne kodowanie (komponenty, moduły)        | Szybki niezawodny model | Agent kodujący       | Szybkość, spójność, oszczędność zasobów        |
| Złożone kodowanie (scaffolding, refaktoryzacja) | Najpotężniejszy model   | Agent kodujący       | Mniej iteracji, lepszy pierwszy strzał         |
| Przetwarzanie plików, audyty, raporty           | Najpotężniejszy model   | Agent autonomiczny   | Praca wieloplikowa bez ręcznego sterowania     |
| Szukanie w sieci, trendy                        | Szybki model            | Chat z wyszukiwaniem | Wyszukiwanie nie wymaga głębokiego rozumowania |

### Trzy reguły kciuka

**Reguła 1: „Myśli czy robi?"**
Jeśli zadanie wymaga myślenia (analiza, architektura, decyzje) → najpotężniejszy model. Jeśli wymaga robienia (implementacja wg specyfikacji, formatowanie, rutynowy kod) → szybki model.

**Reguła 2: „Ile plików naraz?"**
1-3 pliki, proste przetwarzanie → szybki model. 5+ plików, synteza → potężny model. Cały folder → potężny model, agent autonomiczny.

**Reguła 3: „Pierwszy raz czy powtórka?"**
Robisz coś po raz pierwszy (nowa architektura, nowy moduł) → najpotężniejszy model. Powtarzasz sprawdzony wzorzec → szybki model.

**Reguła bonusowa:** Jeśli spodziewasz się więcej niż dwóch iteracji „popraw to" — zacznij od najpotężniejszego. Trzy iteracje na szybkim modelu zużyją więcej zasobów niż jeden strzał z potężnego.

### Rytm dnia

**Rano — strategia (potężny model, Chat, 2-3 godziny)**
Przegląd wczorajszych postępów. Planowanie dzisiejszych zadań. Rozwiązywanie problemów architektonicznych. Tworzenie lub aktualizacja DataPrep. To jest 70% — przygotowanie, które sprawia, że popołudnie jest produktywne.

**Popołudnie — realizacja (szybki model, agent kodujący, 4-6 godzin)**
Implementacja funkcjonalności ze specyfikacji porannych. Użycie szablonów meta-promptów. Przekazanie ustrukturyzowanych promptów AI. Przegląd wyniku, merge, następne zadanie. To jest 30% — szybkie, skupione, mało stresujące.

**Wieczór — refleksja (potężny model, Chat, 30-60 minut)**
Podsumowanie dnia. Aktualizacja meta-promptów na podstawie tego co zadziałało a co nie. Przygotowanie DataPrep na jutro. Śledzenie mierników.

**Efekt:** 5-6 godzin wysoce produktywnej pracy zamiast 8-10 godzin chaotycznego kodowania. Niższe obciążenie poznawcze. Wyższa jakość kodu. Lepsza dokumentacja — bo dokumentacja jest produktem ubocznym DataPrep, nie dopiskiemppo fakcie.

---

## 5. Przed i po

### Przykład: System autentykacji

**Bez WAVE:**

```
Programista: „Zbuduj system auth z email, OAuth i 2FA"
AI generuje → brak obsługi błędów
Programista: „Dodaj obsługę błędów"  
AI regeneruje → złe konwencje nazewnicze
Programista: „Użyj camelCase, trzymaj się naszego stylu"
AI poprawia → konfiguracja JWT koliduje z istniejącą
...8-10 iteracji, 4+ godziny...
```

**Z WAVE:**

```
Krok 1: DataPrep (przygotowany w porannej sesji strategicznej)
Krok 2: Prompt (zbudowany z meta-promptu generowania kodu)
Krok 3: Realizacja — AI generuje kompletną klasę
Krok 4: Przegląd i merge — drobna korekta formatu komunikatów

Wynik: 1 iteracja, 45 minut, spójny kod, testowalny, udokumentowany.
```

### Przykład: Serwis flag funkcjonalnych

**Bez WAVE:** „Napisz serwis flag" → 6 iteracji, 3 godziny.

**Z WAVE:** Prompt z pełnym DataPrep, specyfikacją metod, ograniczeniami, przypadkami brzegowymi. Czas przygotowania promptu: 15 minut. Realizacja AI: 2 minuty. Przegląd: 10 minut. **Łącznie: 27 minut.**

---

## 6. Mierniki z pola walki

Dane z realnego projektu — budowy złożonej platformy webowej przez sześć tygodni.

### Główne wyniki

| Wskaźnik                          | Bez WAVE              | Z WAVE           | Zmiana |
| --------------------------------- | --------------------- | ---------------- | ------ |
| Czas wytworzenia (MVP)            | 8+ tygodni (szacunek) | 6 tygodni (fakt) | -25%   |
| Skuteczność pierwszej próby (PSR) | ~30%                  | ~80% (tydzień 4) | +167%  |
| Poprawki na zadanie               | 3-5 średnio           | 0,8 średnio      | -78%   |
| Gęstość błędów                    | ~2,5 bugs/KLOC        | ~0,8 bugs/KLOC   | -68%   |
| Czas przeglądów kodu              | ~15% czasu dev        | ~5% czasu dev    | -67%   |
| Pokrycie dokumentacją             | ~40%                  | ~95%             | +138%  |
| Obciążenie poznawcze (1-10)       | 7-8                   | 3-4              | -50%   |

### Poprawa w czasie

| Tydzień | PSR  | Pokrycie DataPrep | Średni czas zadania | Uwagi                        |
| ------- | ---- | ----------------- | ------------------- | ---------------------------- |
| 1       | 60%  | 35%               | 3,5h                | Nauka metodyki               |
| 2       | 70%  | 50%               | 2,5h                | Meta-prompty ustalone        |
| 4       | 82%  | 65%               | 1,5h                | Szablony działają dobrze     |
| 6       | 88%  | 78%               | 1,0h                | Niemal automatyczny przepływ |

### Zwrot z inwestycji

Dla solo developera budującego MVP:

- Zaoszczędzony czas: 2-4 tygodnie × koszt alternatywny (~2000 €/tydzień) = **4000-8000 €**
- Mniej błędów: mniej napraw po uruchomieniu = **~3000-5000 € oszczędności**
- Dokumentacja: brak osobnego sprintu dokumentacyjnego = **~2000 € oszczędności**
- Gotowość na skalowanie: nowy programista wdraża się w 1 tydzień zamiast 3

**Szacunkowa łączna wartość dla pierwszego projektu: 10 000-15 000 €.**

---

## 7. Czym WAVE różni się od istniejących podejść

| Podejście                            | Na czym się skupia                      | Co WAVE dodaje                                               |
| ------------------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| **Recursive Meta Prompting (MIT)**   | Samodoskonalące się prompty             | Warstwa DataPrep, praktyczny przepływ, rytm dnia, struktura na poziomie projektu |
| **Documentation-Driven Development** | Dokumentacja przed kodem                | Rekurencyjność (nie liniowość), AI jako aktywny współpracownik, warstwa meta-promptów |
| **AI-DLC**                           | Fazy cyklu życia AI                     | Konkretne techniki przygotowania, mierniki, model operacyjny z doborem narzędzi |
| **Podejście Addy Osmani**            | Praktyczne wskazówki AI-assisted coding | Systematyczna trójwarstwowa struktura, szablony wielokrotnego użytku, samodoskonalące się mierniki |
| **Kursy prompt engineering**         | Pisanie lepszych promptów               | Kontekst na poziomie projektu (DataPrep), szablony (Prompt2Prompt), ciągłe doskonalenie |
| **„Vibe coding"**                    | Intuicyjne kodowanie z AI               | Struktura, powtarzalność, mierzalność, skalowalność zespołowa |

---

## 8. Jak zacząć — dla programistów

### Dzień 1: Trzy kluczowe dokumenty

Zanim napiszesz linijkę kodu, stwórz:

**1. Przegląd architektury (1-2 strony)** — stack z wersjami, struktura projektu, diagram przepływu danych, kluczowe decyzje architektoniczne z uzasadnieniem.

**2. Przewodnik stylu (1 strona)** — konwencje nazewnicze, wzorzec obsługi błędów, organizacja importów, polityka komentarzy.

**3. Model danych (w miarę potrzeb)** — lista encji z kluczowymi polami, relacje, ograniczenia i indeksy.

Te trzy dokumenty same odmienią Twoje interakcje z AI. Dołączaj je (lub istotne fragmenty) do każdego promptu.

### Dzień 2-3: Pierwszy meta-prompt

Wybierz zadanie, które robisz najczęściej — pewnie generowanie kodu. Stwórz szablon meta-promptu. Użyj go do następnych 5-10 zadań. Obserwuj PSR. Dopracuj szablon.

### Dzień 4-7: Ustal rytm

- Rano: aktualizacja DataPrep, planowanie, rozwiązywanie pytań (potężny model, Chat)
- Popołudnie: realizacja ze specyfikacji (szybki model, agent kodujący)
- Wieczór: aktualizacja meta-promptów, śledzenie mierników (potężny model, Chat)

### Tydzień 2+: Rozszerzaj i mierz

- Twórz meta-prompty dla kolejnych typów zadań (przegląd, refaktoryzacja, testy)
- Śledź PSR co tydzień — powinien rosnąć
- Rozszerzaj pokrycie DataPrep w miarę budowania nowych modułów

---

## 9. Typowe pułapki

**Pułapka 1: „Nie mam czasu na DataPrep"** — Najczęstszy błąd i najdroższy. Pominięcie DataPrep „żeby iść szybciej" prowadzi do 3-5x więcej iteracji, niespójnego kodu i długu technicznego. Inwestycja 70% w przygotowanie nie jest luksusem — jest mechanizmem.

**Pułapka 2: Przesadne dokumentowanie** — Odwrotność: dokumentowanie każdego możliwego detalu przed napisaniem kodu. DataPrep ma malejące zyski. Punkt optymalny to 70-85% pokrycia.

**Pułapka 3: Statyczne meta-prompty** — Stworzenie meta-promptów raz i nigdy ich nie aktualizowanie. Powinny ewoluować co 10-20 użyć. Przeznacz 10 minut dziennie na dopracowanie.

**Pułapka 4: Ignorowanie porażek** — Gdy prompt zawiedzie, odruch każe ręcznie naprawić wynik i iść dalej. W WAVE nieudany prompt to sygnał: albo DataPrep jest niekompletny, albo meta-prompt wadliwy. Naprawiaj przyczynę, nie objaw.

**Pułapka 5: Za duże prompty** — Proszenie AI o zbudowanie całego modułu w jednym prompcie. Prompty WAVE są precyzyjne i pojedyncze — jedna funkcja, jeden komponent, jeden serwis.

**Pułapka 6: Brak pomiarów** — „Czuję że jest szybciej" to nie miernik. Śledź PSR, TFCO i współczynnik rewizji — choćby nieformalnie.

---

## 10. Kierunki rozwoju

### WAVE 2.0 dla oprogramowania (2027-2028)

- **Autonomiczne utrzymanie DataPrep** — AI monitorujące zmiany w kodzie i automatycznie aktualizujące dokumenty architektury.
- **Inteligentna ewolucja meta-promptów** — AI śledzące które meta-prompty dają najwyższe PSR i sugerujące ulepszenia.
- **Wieloagentowy WAVE** — wiele agentów AI pracujących równolegle, wszystkie czerpiące z tego samego DataPrep.
- **Integracja z IDE** — wtyczki WAVE dla VS Code, Cursor i innych edytorów.

### Specjalizacje

- **WAVE dla mobile** — meta-prompty specyficzne dla iOS/Android
- **WAVE dla inżynierii danych** — meta-prompty do budowy pipeline'ów
- **WAVE dla DevOps** — meta-prompty dla infrastructure-as-code

---

## Relacja z rdzeniem generycznym

Ten dokument opisuje **jedno zastosowanie** WAVE — pierwsze i najgłębsze. Generyczny rdzeń ([Metodyka WAVE/FALA](FALA_Metodyka_v1.0_PL.md)) opisuje uniwersalne zasady obowiązujące we wszystkich dziedzinach.

Wytwarzanie oprogramowania waliduje twierdzenia WAVE twardymi miernikami i konkretnymi przykładami. Ale trzy warstwy, zasada 70/30 i dwukierunkowy przepływ nie dotyczą kodu. Dotyczą relacji między ludzką ekspertyzą a zdolnościami AI — relacji identycznej niezależnie od tego, czy piszesz oprogramowanie, diagnozujesz pacjentów, czy projektujesz mosty.

---

*WAVE w wytwarzaniu oprogramowania v1.0 — Opublikowany w lutym 2026*  
*Stworzony przez Przemysława Zielińskiego z Claude (Anthropic)*  
*„70% przygotowania. 30% realizacji. 10x wynik."*
