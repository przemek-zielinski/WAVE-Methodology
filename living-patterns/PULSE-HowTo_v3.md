# WAVE PULSE — Instrukcja Użycia (How-To)
## Wersja 3.0 | Marzec 2026

**Dotyczy:** PULSE-Prompt.md v3.0  
**Licencja:** CC BY-SA 4.0  
**Metodyka:** WAVE (Workflow Amplification via Vectored Expertise)

---

## 1. Cel użycia PULSE

PULSE odpowiada na pytanie: **„Jaka jest najlepsza dostępna wiedza dla tego obszaru implementacyjnego i jak ją zastosować w moim projekcie?"**

Efektem PULSE jest Living Pattern — żyjący dokument który zawiera zsyntezowaną wiedzę naukową, branżową i praktyczną, celowaną pod konkretną funkcję celu. Living Pattern nie jest teorią — jest narzędziem decyzyjnym. Projektant otwiera go przed rysowaniem ekranów. Programista przed projektowaniem schematów. Product owner przed definiowaniem metryk.

PULSE buduje Living Pattern w trzech rundach, z których każda celowo szuka z innego kąta. Mechanizm malejących przyrostów gwarantuje, że trzy rundy pokrywają ~97% dostępnej wiedzy.

---

## 2. Logika budowy promptu

Prompt PULSE składa się z pięciu warstw:

**Warstwa roli** — AI wie że jest ekspertem w danym obszarze i że buduje dokument referencyjny, nie odpowiedź na pytanie.

**Warstwa parametrów** — pięć pól definiujących kontekst: obszar, funkcja celu, kontekst rozwiązania, materiały wewnętrzne, ograniczenia. Parametry zamieniają generyczny research w celowany.

**Warstwa Rundy 1** — trzy kroki: przeczytaj materiały wewnętrzne → przeprowadź research wielowarstwowy (nauka → branża → praktyka) → zsyntezuj w ustandaryzowaną strukturę Living Pattern.

**Warstwa Rund 2 i 3** — zdefiniowane w tym samym prompcie, ale uruchamiane ODDZIELNIE przez użytkownika w kolejnych poleceniach. Runda 2 zmienia kąt ataku (porażki zamiast sukcesów). Runda 3 szuka w peryferyjnych kierunkach (prawo, dostępność, edge case'y).

**Warstwa jakości** — zasady obowiązujące we wszystkich rundach: konkretność, źródła, celowość, język, praktyczność.

---

## 3. Model działania

### Trzy rundy — mechanika i uzasadnienie

```
RUNDA 1 — BUDOWA (~60% wartości)
│  Kąt ataku: najlepsze praktyki, konsensus, sukcesy
│  Research: nauka + branża + praktyka
│  Efekt: Living Pattern v1.0 — solidny rdzeń
│
│  ← DECYZJA UŻYTKOWNIKA: ocena, uwagi, kierunek →
│
RUNDA 2 — OPTYMALIZACJA (~25% wartości)
│  Kąt ataku: porażki, kontrowersje, alternatywy
│  Research: z innej strony niż Runda 1
│  Efekt: Living Pattern v2.0 — rdzeń + luki wypełnione
│
│  ← DECYZJA UŻYTKOWNIKA: ocena, uwagi, kierunek →
│
RUNDA 3 — FINALIZACJA (~12% wartości)
│  Kąt ataku: prawo, dostępność, wydajność, edge case'y, przyszłość
│  Research: peryferyjne kierunki
│  Efekt: Living Pattern v3.0 — kompletny fundament
│
│  ← WERDYKT: kompletny czy potrzebna Runda 4 (zwykle nie) →
```

### Dlaczego trzy oddzielne, nie jedna z trzema podpunktami

**Jakość:** Oddzielne rundy wymuszają pełny wysiłek w każdej. W jednorazowym podejściu AI „rezerwuje" materiał na później.

**Zmiana kontekstu:** Między rundami AI wraca z nową wiedzą która zmienia perspektywę. Runda 3 jest celniejsza dzięki temu co znalazła Runda 2.

**Decyzyjność człowieka:** Między rundami użytkownik ocenia efekt i może zmienić kierunek. Ta elastyczność jest niemożliwa w jednorazowym podejściu.

### Krzywa malejących przyrostów

Cztery rundy dałyby ~99%, ale czwarta dodaje tylko ~3% wartości — pojedyncze, niszowe optymalizacje. Trzy rundy to naturalny punkt nasycenia, w którym stosunek wartości do czasu jest optymalny.

---

## 4. Przypadek użycia — jak poprawnie sparametryzować prompt

### Parametr [OBSZAR]

**Co wpisać:** Nazwa obszaru implementacyjnego — krótka i jednoznaczna.

**Dobre przykłady:** „UX/UI i User Journey", „Baza danych i model danych", „Architektura API i integracje", „Bezpieczeństwo i ochrona danych", „Frontend techstack", „Backend techstack", „DevOps i CI/CD", „Strategia testowania", „SEO i ASO", „Analityka i metryki produktowe".

**Jak dobrać zakres:** Obszar powinien być na tyle wąski żeby Living Pattern był konkretny (nie „cała technologia"), ale na tyle szeroki żeby obejmował spójną dziedzinę (nie „walidacja jednego formularza"). Zasada kciuka: jeśli ekspert w tym obszarze mógłby napisać książkę — zakres jest dobry. Jeśli mógłby napisać rozdział — może za wąsko. Jeśli musiałby napisać encyklopedię — za szeroko.

### Parametr [FUNKCJA CELU]

**Co wpisać:** Jedno zdanie definiujące co optymalizujemy. To jest NAJWAŻNIEJSZY parametr — decyduje o celowości całego Living Pattern.

**Dobre przykłady:**

Dla UX/UI: „Maksymalizacja efektu WOW na użytkowniku, retencji D30 powyżej 20%, i aktywacji (pierwsza przesłana próba) powyżej 40% w ciągu 24h od rejestracji."

Dla bazy danych: „Integralność transakcji trójstronnych (mentor-user-marka) + wydajność przy 100k jednoczesnych użytkowników + struktura pod przechwytywanie par próba→feedback→korekta→postęp jako dataset do trenowania modeli AI."

Dla bezpieczeństwa: „Ochrona danych osobowych (RODO) + zabezpieczenie treści UGC przed nadużyciem + odporność na ataki typowe dla platform z transakcjami finansowymi i treściami wideo."

Dla DevOps: „Zero-downtime deployment + automatyzacja testów + monitoring z alertami + koszt infrastruktury poniżej X€/miesiąc przy Y użytkownikach."

**Zła funkcja celu:** „Zrób dobrą bazę danych." — Nie mówi CO jest „dobre" w kontekście tego rozwiązania.

**Skąd wziąć funkcję celu:** Jeśli używałeś SCAN — funkcja celu jest już gotowa w wyniku SCAN dla tego obszaru. Jeśli nie używałeś SCAN — zastanów się: „Gdybym mógł zmierzyć JEDNO kryterium sukcesu dla tego obszaru, co by to było?" I rozbuduj to zdanie o 2–3 dodatkowe kryteria.

### Parametr [KONTEKST ROZWIĄZANIA]

**Co wpisać:** Ten sam opis co w SCAN, ewentualnie uzupełniony o wiedzę zdobytą od czasu SCAN.

**Wskazówka:** Jeśli robisz PULSE dla kilku obszarów — [KONTEKST ROZWIĄZANIA] jest taki sam we wszystkich. Kopiuj między promptami.

### Parametr [MATERIAŁY WEWNĘTRZNE]

**Co wpisać:** Lista plików SPECYFICZNYCH dla tego obszaru. Nie wszystkie pliki projektu — tylko te które dają AI kontekst do celowanego researchu.

**Przykład dla bazy danych:** Specyfikacja TACIT (model danych), specyfikacja IdUShare (transakcje), Decision Log (podjęte decyzje o architekturze), specyfikacja HIVE (wzorce zbierania danych behawioralnych).

**Przykład dla bezpieczeństwa:** Specyfikacja ogólna (co chronimy), specyfikacja modułu płatności, specyfikacja moderacji, polityka prywatności (jeśli istnieje).

### Parametr [OGRANICZENIA]

**Co wpisać:** Twarde fakty ograniczające pole rozwiązań. Szczególnie: wybrane technologie (np. Supabase = PostgreSQL, więc nie szukaj rozwiązań dla MongoDB), regulacje (RODO, EAA), zespół (jeśli jeden programista — nie rekomenduj rozwiązań wymagających zespołu DevOps).

---

## 5. Krok po kroku — jak przeprowadzić sesję PULSE

### Przed sesją (15–30 minut)

Wypełnij pięć parametrów. Jeśli masz wynik SCAN — większość parametrów jest gotowa.

Zbierz materiały wewnętrzne. Jeśli pracujesz w projekcie Claude z FILES — wystarczy wymienić nazwy plików. Jeśli nie — dołącz pliki do czatu.

**Sprawdź czy AI ma włączone wyszukiwanie internetowe.** To jest warunek konieczny dla pełnej wartości PULSE. W Claude: web search jest domyślnie dostępny. W ChatGPT: włącz „Browse with Bing." W Gemini: włącz wyszukiwanie. Bez web search PULSE będzie opierać się wyłącznie na wiedzy treningowej — która może być nieaktualna o miesiące.

### Runda 1 (sesja z AI)

Otwórz nowy czat z AI. Wklej prompt PULSE z wypełnionymi parametrami. AI przeczyta materiały, przeprowadzi research, zsyntezuje Living Pattern v1.0.

Otrzymujesz dokument + werdykt Rundy 1 (co jest pokryte dobrze, gdzie mogą być luki).

**Twoja praca:** Przeczytaj dokument. Oceń: czy rdzeń wiedzy jest sensowny? Czy czegoś oczywistego brakuje? Masz uwagi? Przekaż je AI zanim uruchomisz Rundę 2.

### Runda 2 (w tym samym czacie)

Napisz polecenie uruchamiające Rundę 2. Może być tak proste jak:

> „Uruchom Rundę 2 weryfikacji."

Lub z kierunkiem:

> „Uruchom Rundę 2. Szczególnie chcę sprawdzić czy nasza decyzja o PostgreSQL wytrzyma skalę 100k użytkowników i czy są pułapki przy przechowywaniu danych wideo."

AI zmienia kąt ataku, robi nowy research, dodaje znaleziska do dokumentu.

**Twoja praca:** Przeczytaj uzupełnienia [NOWE v2]. Czy weryfikacja znalazła istotne luki? Masz dodatkowe kierunki do Rundy 3?

### Runda 3 (w tym samym czacie)

Napisz polecenie:

> „Uruchom Rundę 3 — peryferyjne kierunki."

Lub z kierunkiem:

> „Runda 3. Interesują mnie szczególnie aspekty RODO przy przechowywaniu wideo, strategia backup/recovery i co się zmieni w PostgreSQL w ciągu 2 lat."

AI szuka w peryferyjnych kierunkach, dodaje ostatnie elementy.

**Twoja praca:** Przeczytaj werdykt końcowy. Jeśli AI mówi „kompletny" — Living Pattern jest gotowy. Jeśli AI identyfikuje otwarte pytanie — zdecyduj czy je zamknąć (dodatkowy research) czy zostawić (świadoma decyzja).

### Po sesji

Zapisz Living Pattern v3.0 jako plik MD. Dodaj do repozytorium projektu. Ustal rytm auto-doskonalenia (patrz: WAVE Living Patterns Ecosystem, sekcja 9).

---

## 6. Wskazówki zaawansowane

### Jak oceniać jakość Living Pattern

Dobry Living Pattern spełnia pięć kryteriów:

**Celowość** — każdy element wiąże się z funkcją celu. Nie ma „encyklopedycznych" fragmentów dodanych „bo to interesujące."

**Mierzalność** — zasady i standardy mają konkretne liczby: „poniżej 2,5 sekundy", „minimum 44×44 pikseli", „powyżej 40% aktywacji." Nie „szybko", „wystarczająco duży", „wysoka aktywacja."

**Praktyczność** — dla każdego ustalenia jest jasne CO zrobić w implementacji. Nie tylko „cognitive load jest ważny" ale „maksymalnie 3–4 nowe elementy na ekranie, test 5-sekundowy na każdym widoku."

**Sprzeczności rozwiązane** — jeśli branża się nie zgadza, Living Pattern przedstawia obie strony z argumentami i daje rekomendację z uzasadnieniem. Nie udaje że konsensus istnieje gdy go nie ma.

**Aktualność** — źródła z ostatnich 2–3 lat. Fundamenty naukowe mogą być starsze (Kahneman 1993 jest wciąż aktualny), ale dane rynkowe i trendy muszą być świeże.

### Kiedy Living Pattern wymaga przebudowy (nie aktualizacji)

Trzy sytuacje:

Fundamentalna zmiana funkcji celu — np. zmiana z „platforma mobilna" na „platforma desktop-first." Cały wzorzec UX/UI traci ważność.

Przełom technologiczny — np. pojawienie się nowego paradygmatu baz danych który zmienia rachunek kosztów i możliwości.

Zmiana regulacyjna zmieniająca zasady gry — np. nowa dyrektywa UE fundamentalnie zmieniająca wymagania bezpieczeństwa.

W tych sytuacjach auto-doskonalenie nie wystarczy. Trzeba uruchomić PULSE od nowa z nowymi parametrami.

### Ile Living Patterns dla jednego projektu

Typowy projekt cyfrowy potrzebuje 6–12 Living Patterns (odpowiednio do złożoności). Mały projekt (MVP, jeden deweloper) może wystarczyć z 3–5. Duży (enterprise, wiele zespołów) może potrzebować 15–20.

Zasada kciuka: jeśli dwa obszary mają RÓŻNE funkcje celu — to dwa oddzielne Living Patterns. Jeśli mają tę samą — rozważ połączenie.

---

*Dokument opracowany: 9 marca 2026*
*Wersja: 3.0*
*Licencja: CC BY-SA 4.0*
