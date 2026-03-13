# WAVE — Metodyka Współpracy Człowiek-AI
## Dokument Referencyjny: Software Engineering v1.2 | Marzec 2026

**Autor koncepcji:** Przemek Zieliński  
**Opracowanie:** Claude Opus 4.6  
**Licencja:** CC BY-SA 4.0  
**Repozytorium:** github.com/przemek-zielinski/WAVE-Methodology  
**Pierwsza dziedzina zastosowania:** Software Engineering (inżynieria oprogramowania)

---

## Spis treści

— Szybki Start — zacznij tutaj

0. W jednym zdaniu, w jednym akapicie, w jedną minutę
1. Problem — paradoks produktywności AI
2. Filozofia — pięć aksjomatów i trzy poziomy współpracy
3. Siedem problemów i siedem odpowiedzi WAVE
4. DooR — drzwi między etapami
5. Komponenty — otwarta mapa narzędzi
6. Test kompletności — czwórka AANP
7. WAVE a istniejące metodyki — inne pytanie, inny poziom
8. Przykład zastosowania — IDareU Gen2
9. Słownik pojęć

---

## Szybki Start — zacznij tutaj

Nie chcesz czytać dziesięciu rozdziałów zanim zaczniesz? Oto minimum.

**Co to jest:** Metodyka współpracy człowiek-AI. Mówi jak przygotować kontekst, prowadzić sesję i budować wiedzę, żeby AI pracował na najlepszych założeniach — nie na zgadywaniu.

**Jak zacząć w trzech krokach:**

```
  KROK 1 — Wybierz profil produktu
  ─────────────────────────────────
  □ POC / prototyp?        → Profil DISCOVERY (1-5 dni)
  □ MVP / pilot?           → Profil BUILD (4-8 tygodni)
  □ Produkt docelowy?      → Profil SCALE (miesiące)
  
  Nie wiesz? Zacznij od DISCOVERY. Zawsze możesz przesunąć wyżej.

  KROK 2 — Uruchom SCAN
  ──────────────────────
  Otwórz czat z AI. Wklej prompt SCAN-Prompt.md z opisem
  swojego rozwiązania. Dostaniesz listę obszarów do zbadania
  z gotowymi parametrami do następnego kroku.

  KROK 3 — Uruchom PULSE dla pierwszego obszaru
  ───────────────────────────────────────────────
  Weź najważniejszy obszar z listy SCAN.
  Wklej prompt PULSE-Prompt.md z parametrami.
  Przeprowadź Rundę 1. Oceń wynik.
  Masz pierwszy Living Pattern — żywy dokument wiedzy.
  Powtórz dla kolejnych obszarów.
```

**Czego potrzebujesz:** Dostęp do AI z wyszukiwaniem internetowym (Claude, ChatGPT, Gemini z web search). Opis swojego rozwiązania. Opcjonalnie: istniejąca dokumentacja projektu.

**Pliki do pobrania:**

| Plik | Co robi | Kiedy użyć |
|---|---|---|
| `SCAN-Prompt.md` | Identyfikuje obszary do zbadania | Na początku — raz |
| `SCAN-HowTo.md` | Instrukcja użycia SCAN | Przed pierwszym SCAN |
| `PULSE-Prompt.md` | Buduje Living Pattern w 3 rundach | Per obszar z listy SCAN |
| `PULSE-HowTo.md` | Instrukcja użycia PULSE | Przed pierwszym PULSE |
| `WAVE_Profile_Produktu.md` | Jak dobrać skalę WAVE do projektu | Gdy nie wiesz ile WAVE potrzebujesz |

Reszta dokumentu wyjaśnia DLACZEGO to działa, JAK jest zbudowane i CO możesz osiągnąć na większą skalę.

### Mapa WAVE — architektura metodyki w jednym spojrzeniu

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║   WAVE — Workflow Amplification via Vectored Expertise                 ║
║   Metodyka Współpracy Człowiek-AI                                     ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 1: FILOZOFIA (zamknięta — 5 aksjomatów + meta-aksjomat) │   ║
║   │                                                                │   ║
║   │  70/30 • Człowiek kieruje • Buduj kompletnie • Droga=wartość  │   ║
║   │  • Porażki uczą                                                │   ║
║   │  Meta-aksjomat: Prądy i Napięcia (nawigacja, nie optymalizacja)│   ║
║   │                                                                │   ║
║   │  Trzy poziomy H-AI: DataPrep → Prompt2Data → Prompt2Prompt    │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 2: KOMPONENTY (otwarte — zbiór rośnie)               │   ║
║   │                                                                │   ║
║   │  DooR — Definition of Operational Readiness                   │   ║
║   │  ┌──────────────────────┐  ┌──────────────────────────────┐   │   ║
║   │  │  Living Patterns     │  │  FALA                        │   │   ║
║   │  │  (gotowość WIEDZY)   │  │  (od koncepcji do KODU)      │   │   ║
║   │  │                      │  │                              │   │   ║
║   │  │  SCAN → PULSE →      │  │  Audyt → Blueprint → Kod    │   │   ║
║   │  │  Living Pattern      │  │  RtS (11 warstw) → DoD      │   │   ║
║   │  └──────────────────────┘  └──────────────────────────────┘   │   ║
║   │                                                                │   ║
║   │  Decision Log • [przyszłe komponenty → zbiór otwarty]         │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 3: PRAKTYKI (otwarte — nawyki narastają)             │   ║
║   │                                                                │   ║
║   │  Checkpointy • Krótsze czaty • Wersjonowanie • Imperatyw      │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  TEST KOMPLETNOŚCI: AANP (zamknięty)                          │   ║
║   │                                                                │   ║
║   │  Każdy proces = Aktor + Akcja + Narzędzie + Produkt           │   ║
║   │  Brak jednego = proces dziurawy                               │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Profile Produktu — WAVE dla każdej skali

WAVE to jedna metodyka z trzema profilami intensywności — dopasowanymi do rodzaju budowanego rozwiązania. Budujesz POC w jeden dzień? Profil DISCOVERY. MVP w kilka tygodni? Profil BUILD. Produkt docelowy? Profil SCALE. Filozofia ta sama, skala komponentów inna.

| Profil | Cel | Czas | Proporcja P/E | SCAN | PULSE | RtS |
|---|---|---|:---:|---|---|---|
| **DISCOVERY** (POC) | Zwalidować pomysł | 1-5 dni | ~60/40 | 3-5 pytań | 1 runda | 4 warstwy |
| **BUILD** (MVP) | Dostarczyć wartość | 2-8 tyg. | ~70/30 | 6-8 obszarów | 2 rundy | 8 warstw |
| **SCALE** (Produkt) | Skalować i utrzymać | Miesiące | 50-70/30-50 | 10-15 obszarów | 3 rundy | 11 warstw |

Pełny opis: **WAVE Profile Produktu v1.0** (dokument towarzyszący).

---

## 0. W jednym zdaniu, w jednym akapicie, w jedną minutę

### Jedno zdanie

WAVE to metodyka współpracy człowiek-AI — mówi jak przygotować kontekst, prowadzić sesję i budować wiedzę, żeby AI pracował na najlepszych możliwych założeniach, a nie na zgadywaniu.

### Jeden akapit

Każdy kto pracuje z AI zna ten moment — AI daje coś średniego, poprawiasz, poprawiasz, po godzinie masz coś używalnego. Następnego dnia zaczynasz od zera. WAVE odwraca tę proporcję: siedemdziesiąt procent czasu inwestujesz w przygotowanie kontekstu i wiedzy, trzydzieści procent w egzekucję — i ta egzekucja jest celna od pierwszego strzału. WAVE daje konkretne narzędzia: SCAN rozpoznaje co musisz wiedzieć, PULSE buduje tę wiedzę w trzech rundach, Living Pattern utrzymuje ją aktualną, RtS definiuje kiedy kontekst jest kompletny. Rezultat: AI przestaje zgadywać i zaczyna działać jak partner, który naprawdę rozumie twój projekt.

### Jedna minuta

Mamy problem, którego nikt nie nazwał. Miliony ludzi codziennie pracują z AI — piszą kod, projektują produkty, tworzą dokumenty. I większość z nich robi to tak samo: wrzucam prompt, patrzę co wyjdzie, poprawiam, poprawiam, poprawiam. To jest jak budowanie domu bez projektu — stawiasz ścianę, burzysz, stawiasz inaczej. Działa, ale marnujesz osiemdziesiąt procent potencjału.

WAVE mówi: odwróć proporcję. Zanim zaczniesz budować — przygotuj kontekst. Zbierz wiedzę. Zdefiniuj co optymalizujesz. Daj AI pełny obraz, a nie strzęp informacji. Siedemdziesiąt procent przygotowanie, trzydzieści procent egzekucja. I ta egzekucja jest celna, bo AI nie zgaduje — wie.

WAVE nie jest kolejnym frameworkiem zarządzania projektami. Nie konkuruje ze Scrumem ani z Lean. WAVE działa na poziomie, którego żadna istniejąca metodyka nie adresuje — na poziomie sesji roboczej, w której człowiek i AI razem tworzą coś konkretnego. Jest open-source, jest darmowa, i każdy może zacząć ją stosować dziś — od jednego narzędzia, od jednej sesji.

---

## 1. Problem — paradoks produktywności AI

### Percepcja vs rzeczywistość

Ponad 80% programistów korzysta dziś z narzędzi AI do kodowania. Niemal wszyscy deklarują, że pracują szybciej. Tymczasem dane mówią coś zaskakującego.

```
  PERCEPCJA PROGRAMISTÓW          DANE Z BADAŃ
  ═══════════════════════         ═══════════════════════

  „AI przyspiesza                 Doświadczeni programiści
   moją pracę o 20%"             są 19% WOLNIEJSI z AI
                                  (METR, 2025)
          ▲                             ▲
          │         39 punktów          │
          │◄────── przepaści ──────────►│
          │        percepcji            │
          │                             │

  +20% (odczucie)               -19% (pomiar)
```

Ta trzydziestodziewięciopunktowa przepaść percepcji to nie ciekawostka — to sygnał ostrzegawczy. Jak ujął to profesor MIT Armando Solar-Lezama: AI to nowa karta kredytowa pozwalająca zaciągać dług techniczny w tempie, jakiego nigdy wcześniej nie znaliśmy.

### Skala problemu — twarde liczby

| Źródło | Rok | Odkrycie | Skala |
|---|:---:|---|---|
| **METR** | 2025 | Doświadczeni programiści wolniejsi z AI o 19% | Kontrolowane badanie |
| **Faros AI** | 2025 | Czas code review wydłużył się o 91% | 10 000 programistów, 1255 zespołów |
| **GitClear** | 2024 | Duplikacja kodu wzrosła 4× | 211 mln zmienionych linii kodu |
| **CodeRabbit** | 2025 | Kod z AI: 1,7× więcej poważnych błędów | 470 pull requestów |
| **Apiiro** | 2025 | Luki bezpieczeństwa: z 1000 do 10 000/mies. | Firmy Fortune 50 |
| **NBER** | 2026 | Brak mierzalnego wpływu AI na produktywność firm | 6000 dyrektorów |
| **MIT Media Lab** | 2026 | 95% organizacji nie widzi mierzalnego zwrotu z AI | Badanie przekrojowe |
| **Stack Overflow** | 2025 | Zaufanie do AI kodującego spadło z 43% do 29% | Społeczność globalna |
| **Fed San Francisco** | 2026 | Makro-statystyki nie wykazują efektu AI na produktywność | Przemówienie 17.02.2026 |

### Wizualizacja — co się stało z obietnicą AI

```
  Obietnica                              Rzeczywistość
  ────────                               ────────────

  Programista                            Programista
  + AI                                   + AI
  = 10× szybszy                          = więcej kodu
                                           + więcej błędów
  ┌────────────┐                           + dłuższe review
  │ ██████████ │ 10×                       + więcej długu
  │ ██████████ │                           + mniej zrozumienia
  │ ██████████ │                         
  │ ██████████ │                         ┌────────────┐
  │ ██████████ │                         │ ████       │ 1,2×
  └────────────┘                         │            │ (netto)
                                         └────────────┘
       MIT                                   Faros AI
  „przyszłość"                          „stan na dziś"
```

### Gdzie leży problem — mapa

Problem nie leży w AI. Problem nie leży w człowieku. Problem leży w **przestrzeni między nimi** — w sposobie, w jaki ludzka wiedza i intencja trafia do okna kontekstowego AI.

```
  ┌─────────────┐          ╔═══════════════════╗          ┌─────────────┐
  │             │          ║                   ║          │             │
  │  CZŁOWIEK   │          ║   PRZESTRZEŃ      ║          │     AI      │
  │             │          ║   MIĘDZY          ║          │             │
  │  • wiedza   │ ──??──▶  ║                   ║  ──??──▶ │  • moc      │
  │  • kontekst │          ║   niezagospoda-   ║          │  • skala    │
  │  • intencja │          ║   rowana          ║          │  • szybkość │
  │  • cel      │          ║                   ║          │  • synteza  │
  │             │          ║   ◀── WAVE ──▶    ║          │             │
  └─────────────┘          ╚═══════════════════╝          └─────────────┘
```

WAVE zagospodarowuje tę przestrzeń. Nie przez zmianę AI — AI jest wystarczająco dobre. Przez zmianę tego, co AI dostaje na wejściu.

---

## 2. Filozofia — pięć aksjomatów i trzy poziomy współpracy

### Pięć aksjomatów

Filozofia WAVE to zbiór zamknięty — pięć aksjomatów i jeden meta-aksjomat, które nie podlegają negocjacji. Wszystko inne w WAVE może się zmieniać, rosnąć, ewoluować. Filozofia — nie. Jest jak prawa termodynamiki: możesz budować dowolną maszynę, ale te prawa zawsze obowiązują.

### Pięć aksjomatów — przegląd

| # | Aksjomat | Esencja | Analogia |
|:---:|---|---|---|
| 1 | **70 / 30** | Przygotowanie dominuje — jak grawitacja, nie nakaz | Gepard: 16h obserwacji → 12s pościgu |
| 2 | **Człowiek kieruje, AI wzmacnia** | AI to wzmacniacz ekspertyzy, nie zamiennik | Teleskop nie zastępuje oka astronoma |
| 3 | **Buduj kompletnie, aktywuj progresywnie** | Pełna architektura od dnia 1, aktywacja stopniowa | Drzewo owocowe: sadzisz kompletne, owoce za 2 lata |
| 4 | **Proces i droga = wartość** | Odkrycia rodzą się między zadaniami | Serendypia: Kolumb → Ameryka, Fleming → penicylina |
| 5 | **Porażki uczą więcej niż sukcesy** | Cudze błędy z liczbami > cudze sukcesy bez kontekstu | Sukces usypia zmysły, porażka wyostrza |

**Aksjomat 1 — Siedemdziesiąt na trzydzieści.** Przygotowanie dominuje nad egzekucją. Nie jako nakaz — jako grawitacja. Ciało zawsze spada ku ziemi, ale trajektoria zależy od tego, co budujesz.

W przyrodzie ta proporcja pojawia się wszędzie. Gepard — najszybsze zwierzę lądowe — biega maksymalnie dwanaście sekund. Reszta jego dnia to obserwacja, pozycjonowanie, oczekiwanie na właściwy moment. Z AI jest tak samo: godzina przygotowania kontekstu i piętnaście minut egzekucji, która trafia za pierwszym razem. Albo: zero przygotowania i trzy godziny poprawiania.

70/30 to punkt ciążenia, nie żelazna reguła. W lekkim prototypie (profil Discovery) proporcja naturalnie ciągnie ku 60/40 — bo produkt jest za prosty, żeby przygotowanie potrzebowało dominacji. W dużym produkcie z dwudziestoma modułami ciągnie ku 50/50 — bo egzekucja rośnie liniowo z każdym modułem, a przygotowanie się reużywa. W MVP (profil Build) ląduje dokładnie na 70/30 — i tu aksjomat oddycha najpełniej.

Ale we WSZYSTKICH przypadkach przygotowanie to co najmniej połowa pracy — co jest radykalną odwrotnością vibe codingu, gdzie przygotowanie równa się zeru.

**Aksjomat 2 — Człowiek kieruje, AI wzmacnia.** AI jest wzmacniaczem ekspertyzy — nie jej zamiennikiem. To człowiek definiuje funkcję celu, człowiek ocenia wynik, człowiek podejmuje decyzję. AI przetwarza, syntetyzuje, generuje — na skali niedostępnej dla człowieka. Ale kierunek zawsze należy do człowieka. AI bez kierunku ludzkiego produkuje treść poprawną ale generyczną — jak orkiestra bez dyrygenta.

**Aksjomat 3 — Buduj kompletnie, aktywuj progresywnie.** Projektuj pełną architekturę od pierwszego dnia, ale aktywuj funkcje przez przełączniki, w miarę jak zbierasz dane i potwierdzasz założenia. Nie buduj „wersji tymczasowej, którą potem wyrzucisz." Buduj wersję docelową, którą potem odkrywasz.

**Aksjomat 4 — Proces i droga mają wartość.** Najcenniejsze odkrycia pojawiają się między zadaniami. WAVE nie jest linią prostą od punktu A do punktu B. Jest rzeką, która płynie w kierunku morza, ale po drodze tworzy meandry, rozlewiska i delty — i w tych zakrętach mieszka wartość, której plan liniowy nigdy by nie znalazł.

**Aksjomat 5 — Porażki uczą więcej niż sukcesy.** Dlatego w WAVE każde narzędzie badawcze (PULSE) celowo szuka porażek w Rundzie 2 — nie dlatego, że jest pesymistyczne, lecz dlatego, że cudze błędy z liczbami są cenniejsze niż cudze sukcesy bez kontekstu.

**Meta-aksjomat: Prądy i Napięcia.** Pięć aksjomatów mówi CO jest ważne. Prądy i Napięcia mówi JAK te wartości rywalizują ze sobą w każdej konkretnej decyzji. Każda sesja współpracy człowiek-AI rozgrywa się na polu napięć — jakość↔prostota, stabilność↔bogactwo funkcji, koszt↔głębokość — a emergencja rodzi się na ich przecięciu. Rolą operatora jest nawigacja tej rywalizacji, nie eliminacja jej. Zapas pojemności jest wartością pierwszej klasy, nie marnotrawstwem. Pełny opis: dokument główny WAVE v2.0, rozdział 2.

### Trzy poziomy współpracy H-AI

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║                                                                   ║
  ║  Poziom 1: DataPrep                                    WDECH     ║
  ║  ─────────────────                                               ║
  ║  Człowiek porządkuje wiedzę dziedzinową                          ║
  ║  Zbiera kontekst, definiuje cel, strukturyzuje                   ║
  ║  ● Kto: CZŁOWIEK (głównie)                                      ║
  ║  ● W SE: architektura, specyfikacje, model danych, Decision Log  ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Poziom 2: Prompt2Data                                 PULS      ║
  ║  ────────────────────                                            ║
  ║  Precyzyjne zadanie z pełnym kontekstem                          ║
  ║  AI nie zgaduje intencji — intencja jest jawna                   ║
  ║  ● Kto: CZŁOWIEK → AI                                           ║
  ║  ● W SE: blueprint z 11 warstwami, prompt z parametrami         ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Poziom 3: Prompt2Prompt                               WYDECH   ║
  ║  ──────────────────────                                          ║
  ║  Meta-sterowanie: ocena wyniku, korekta, iteracja                ║
  ║  Człowiek kształtuje kierunek, nie pisze treści                  ║
  ║  ● Kto: CZŁOWIEK (ocenia) ← AI (proponuje)                     ║
  ║  ● W SE: autotest 3 pytań RtS, code review, korekta blueprintu  ║
  ║                                                                   ║
  ║                          ↻ (cykl się powtarza)                   ║
  ║                                                                   ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

### Jak trzy poziomy przenikają narzędzia WAVE

| Narzędzie | DataPrep | Prompt2Data | Prompt2Prompt |
|---|---|---|---|
| **PULSE** | Zbierz materiały, wypełnij 5 parametrów | Prompt badawczy z funkcją celu | Ocena rundy, zmiana kąta ataku |
| **FALA** | Zbierz dokumentację koncepcyjną | AI audytuje / wypełnia blueprint | Autotest 3 pytań, korekta luk |
| **SCAN** | Opisz rozwiązanie, profil, ograniczenia | AI identyfikuje obszary | Przegląd mapy, dodanie/usunięcie |
| **Decision Log** | Zbierz kontekst decyzji | AI formatuje wpis | Weryfikacja i zatwierdzenie |

---

## 3. Siedem problemów i siedem odpowiedzi WAVE

Paradoks produktywności AI to nie jedno zjawisko — to splot siedmiu wzajemnie wzmacniających się problemów. Każdy z nich osobno jest do opanowania. Razem tworzą systemową pułapkę, w którą wpada większość zespołów pracujących z AI bez świadomej metodyki.

### Mapa siedmiu problemów — przegląd

```
  PROBLEMY H-AI BEZ METODYKI                  ODPOWIEDZI WAVE
  ══════════════════════════                   ═══════════════

  1. Dryf architektoniczny ─────────────────── DataPrep + Living Patterns
     „lokalnie mądrze, globalnie chaotycznie"   („konstytucja projektu")

  2. Eksplozja długu technicznego ──────────── Kaskadowy kontekst 3 poziomów
     „szybka karta kredytowa"                   („spójność z góry")

  3. Zator na recenzji kodu ────────────────── RtS + jakość 1. przejścia
     „prawo Amdahla w praktyce"                 („mniej kodu do poprawki")

  4. Degradacja kontekstu ──────────────────── FILES + krótkie sesje
     „fałszywe wspomnienia agenta"              („pamięć zewnętrzna")

  5. Erozja umiejętności ───────────────────── Zasada 70/30
     „kac po vibe codingu"                      („rozumiesz, co budujesz")

  6. Dolina „prawie dobrze" ────────────────── Precyzyjne specyfikacje
     „kod wygląda OK, ale nie jest"             („mniej miejsca na odchylenia")

  7. Luka indywidualna vs organizacyjna ────── Kompletny cykl WAVE
     „szybciej piszę, wolniej dostarczam"       („system, nie narzędzie")
```

---

### Problem 1: Dryf architektoniczny

**Diagnoza:** Agent kodujący nie zna niepisanych konwencji zespołu, wcześniejszych decyzji architektonicznych ani tego, że trzy pliki dalej istnieje funkcja robiąca to samo. Ox Security: dziesięć anty-wzorców w 80-100% kodu generowanego przez AI. Kod jest „wysoce funkcjonalny, ale systematycznie pozbawiony osądu architektonicznego."

```
  BEZ WAVE                               Z WAVE
  ────────                                ──────

  AI widzi:                               AI widzi:
  ┌──────────────────┐                    ┌──────────────────┐
  │ Bieżący plik     │                    │ Blueprint RtS    │
  │ + fragment kodu   │                    │ + Decision Log   │
  │ + ogólny prompt   │                    │ + Living Pattern │
  │                   │                    │ + próbka kodu    │
  │ (strzęp kontekstu)│                    │ + 11 warstw      │
  └──────────────────┘                    │                   │
                                          │ (pełna mapa)     │
  Rezultat:                               └──────────────────┘
  10 anty-wzorców                         
  w 80-100% kodu                          Rezultat:
  (Ox Security)                           Spójność wymuszona
                                          kontekstem, nie nadzieją
```

**Odpowiedź WAVE:** DataPrep tworzy kompletną dokumentację PRZED pierwszą linią kodu. Living Patterns dostarczają najlepszą wiedzę branżową. RtS z 11 warstwami wymusza, że AI widzi pełną architekturę — nie fragment. Branża dochodzi do tego samego (pliki CLAUDE.md, AGENTS.md, Spec-Driven Development) — WAVE ujmuje to w kompletny system.

---

### Problem 2: Eksplozja długu technicznego

**Diagnoza:** GitClear (211 mln linii kodu): duplikacja 4×, refaktoryzacja -60%, code churn 2×. CodeRabbit: kod z AI ma 1,7× więcej poważnych błędów. Apiiro: luki bezpieczeństwa z 1000 do 10 000 miesięcznie w Fortune 50.

```
  WZROST DŁUGU TECHNICZNEGO Z AI (GitClear, 2020-2024)
  
  Duplikacja kodu    ████████████████████████████████  4× wzrost
  Code churn         ████████████████                  2× wzrost
  Błędy logiczne     ████████████████████████          1,7× (CodeRabbit)
  Luki bezpieczeństwa████████████████████████████████████████ 10× (Apiiro)
  Refaktoryzacja     ██████                            -60% spadek
                     ─────────────────────────────────────────────▶
                     2020              2022              2024
```

**Odpowiedź WAVE:** Trzy poziomy (DataPrep → Prompt2Data → Prompt2Prompt) tworzą kaskadę, w której żaden agent nie działa w próżni. Kontekst architektoniczny dostarczany PRZED kodowaniem eliminuje główny mechanizm narastania długu — kod generowany bez świadomości istniejących wzorców.

---

### Problem 3: Zator na recenzji kodu

**Diagnoza:** Faros AI: 98% wzrost scalanych pull requestów + 91% wydłużenie czasu recenzji. Prawo Amdahla: przyspieszasz jedną maszynę na linii montażowej, reszta pracuje w tym samym tempie. Powstaje korek.

```
  PRAWO AMDAHLA W PRAKTYCE

  BEZ WAVE:
  Kodowanie:  ██░░░░░░░░░░░░░░░░░░░░░░   szybkie (AI)
  Review:     ░░░░░░██████████████████████ wolne (człowiek) ← ZATOR
  Testy:      ░░░░░░░░░░░░░░░░░░░░████████ czekają
  Deploy:     ░░░░░░░░░░░░░░░░░░░░░░░░░██ czeka
              ──────────────────────────────────────────▶ czas

  Z WAVE:
  Kodowanie:  ████░░░░░░░░░░░░░░░░░░░░░░  celne (>80% bez poprawek)
  Review:     ░░░░████░░░░░░░░░░░░░░░░░░░ krótsze (mniej błędów)
  Testy:      ░░░░░░░░████░░░░░░░░░░░░░░░ przechodzą
  Deploy:     ░░░░░░░░░░░░████░░░░░░░░░░░ płynnie
              ──────────────────────────────────────────▶ czas
```

**Odpowiedź WAVE:** Metryka „jakość pierwszego przejścia" (cel: >80% komponentów bez poprawek). Kod z pełnym kontekstem RtS wymaga mniej poprawek — kolejka recenzji nie puchnie. Limit 50 promptów na najdłuższą sesję zapobiega degradacji jakości.

---

### Problem 4: Degradacja kontekstu

**Diagnoza:** Przy długich sesjach (>50 wymian) agenci twierdzą, że istnieją funkcje których nie ma, odwołują się do plików które nie zostały zmodyfikowane, „pamiętają" ustalenia które nigdy nie padły. Badania Chroma: modele radzą sobie GORZEJ gdy kontekst zachowuje logiczny przepływ — „idą z prądem" zamiast analizować.

| Długość sesji | Ryzyko halucynacji | Jakość kodu | Zalecenie WAVE |
|:---:|:---:|:---:|---|
| 1-20 wymian | Niskie | Wysoka | Norma — pracuj swobodnie |
| 20-50 wymian | Rosnące | Malejąca | Checkpoint — zapisz stan |
| 50-100 wymian | Wysokie | Niska | Zamknij sesję, otwórz nową |
| 100+ wymian | Krytyczne | Nieprzewidywalna | Zakaz — maraton = chaos |

**Odpowiedź WAVE:** Hierarchiczna struktura FILES (dokumentacja w projekcie Claude) to pamięć zewnętrzna — AI nie musi „pamiętać", ma gdzie sprawdzić. Praktyka krótszych czatów tematycznych wymusza świeży kontekst na początku każdej sesji. Checkpointy co 2 godziny zapisują stan, zanim kontekst się zdegraduje.

---

### Problem 5: Erozja umiejętności

**Diagnoza:** Vibe coding — Słowo Roku 2025 (Collins Dictionary). Programista opisuje naturalnym językiem co chce, AI generuje kod, programista akceptuje bez zrozumienia. Stanford: 20% spadek zatrudnienia juniorów (22-25 lat) między 2022-2025. 54% liderów planuje zatrudniać mniej juniorów. Problem: junior to przyszły architekt w trakcie szkolenia — eliminacja „walki z kodem" eliminuje naukę.

```
  CYKL EROZJI UMIEJĘTNOŚCI

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ AI pisze │────▶│ Człowiek │────▶│ Umiejętn.│────▶│ Większa  │
  │ za mnie  │     │ nie ćwiczy│     │ zanikają │     │ zależność│
  └──────────┘     └──────────┘     └──────────┘     │ od AI    │
       ▲                                              └─────┬────┘
       │                                                    │
       └────────────────────────────────────────────────────┘
                    pętla degradacji

  WAVE PRZERYWA PĘTLĘ:

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ Człowiek │────▶│ Człowiek │────▶│ AI       │────▶│ Człowiek │
  │ ROZUMIE  │     │ SPECYFI- │     │ REALIZUJE│     │ WERYFIKUJE│
  │ archit.  │     │ KUJE     │     │ z kontekst│    │ i UCZY SIĘ│
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
       70% przygotowania                   30% egzekucji
```

**Odpowiedź WAVE:** Zasada 70/30 oznacza, że programista MUSI dogłębnie rozumieć architekturę, model danych, logikę biznesową ZANIM AI napisze pierwszą linię kodu. Simon Willison postawił granicę: „jeśli przejrzałeś, przetestowałeś i zrozumiałeś — to nie vibe coding." WAVE z definicji stawia rozumienie przed wykonaniem.

---

### Problem 6: Dolina „prawie dobrze"

**Diagnoza:** Stack Overflow 2025: 45% programistów — główna frustracja to kod AI który jest „prawie dobrze, ale nie całkiem." Zaufanie spadło z 43% do 29%, ale użycie wzrosło do 84% — programiści korzystają z narzędzi którym coraz mniej ufają. 67% spędza WIĘCEJ czasu na debugowaniu kodu AI niż pisanego ręcznie.

| Metryka | Wartość | Trend |
|---|:---:|:---:|
| Programiści używający AI do kodowania | 84% | ↑ rośnie |
| Zaufanie do kodu AI | 29% | ↓ spada (było 43%) |
| Wysokie zaufanie do kodu AI | 3% | ↓↓ minimalne |
| Odmawiających merge bez review | 71% | ↑ rośnie |
| Regularnie poprawiających kod AI | 66% | ↑ rośnie |
| Więcej czasu na debugowanie AI kodu | 67% | ↑ rośnie |

**Odpowiedź WAVE:** Pełne specyfikacje z DataPrep i RtS drastycznie zmniejszają przestrzeń, w której AI może „prawie trafić." CodeScene (2026) potwierdza: AI zwiększa ryzyko defektów o 30% w projektach ze słabą dokumentacją — ale w projektach z jasną architekturą wzrost jest znacznie mniejszy.

---

### Problem 7: Luka indywidualna vs organizacyjna

**Diagnoza:** Faros AI: programiści w zespołach z wysoką adopcją AI kończą 21% więcej zadań i scalają 98% więcej PRów. Ale zyski indywidualne neutralizowane przez zatykające się recenzje, niestabilne testy i powolne wydawanie. Fed San Francisco (02.2026): makro-statystyki nie wykazują efektu AI na produktywność.

```
  LUKA PRODUKTYWNOŚCI

  Indywidualna produktywność:
  ████████████████████████████████████████  +21% zadań  ↑
  ████████████████████████████████████████████████████████  +98% PRów  ↑

  Organizacyjna produktywność:
  ████████████████████  ~0% zmiana netto  →

  Dlaczego? Bo:
  Review:    ████████████████████████████████████████████  +91% czasu  ↑
  Bugi:      ████████████████████████████  +1,7× więcej  ↑
  Bezpiecz.: ████████████████████████████████████████████████████  +10× luk  ↑
  Dług tech: ████████████████████████████████████████  +4× duplikacji  ↑
```

**Odpowiedź WAVE:** WAVE to nie przyspieszenie jednego ogniwa — to optymalizacja całego łańcucha. Od pomysłu (SCAN) przez wiedzę (PULSE) i specyfikację (FALA) po kod (Claude Code) i weryfikację (DoD). Metryki WAVE mierzą nie „ile kodu powstało" ale „ile komponentów przeszło bez poprawek" i „stosunek godzin planowanych do rzeczywistych."

### Podsumowanie siedmiu problemów — tabela zbiorcza

| # | Problem | Kluczowa dana | Mechanizm WAVE | Komponent |
|:---:|---|---|---|---|
| 1 | Dryf architektoniczny | 80-100% AI kodu ma anty-wzorce | Pełny kontekst przed kodowaniem | Living Patterns + RtS |
| 2 | Eksplozja długu | 4× duplikacja, -60% refaktor | Kaskadowy kontekst 3 poziomów | DataPrep → P2D → P2P |
| 3 | Zator na review | +91% czas recenzji | Jakość 1. przejścia >80% | RtS + limit sesji |
| 4 | Degradacja kontekstu | Halucynacje po 50+ wymianach | FILES + krótkie sesje | Checkpointy |
| 5 | Erozja umiejętności | -20% zatrudnienie juniorów | 70% = człowiek rozumie | Zasada 70/30 |
| 6 | Dolina „prawie dobrze" | 67% więcej debugowania | Precyzyjne specyfikacje | RtS (11 warstw) |
| 7 | Luka ind. vs org. | +21% ind., ~0% org. | Cały cykl, nie jedno ogniwo | WAVE kompletne |

---

## 4. DooR — drzwi między etapami

### Definition of Operational Readiness

Wyobraź sobie rakietę na platformie startowej. Inżynierowie nie pytają „czy czujemy się gotowi do startu?" Pytają: „czy każdy system przeszedł weryfikację? czy paliwo jest na poziomie? czy telemetria działa?" Lista jest zamknięta, mierzalna, binarna. Albo wszystko jest na zielono, albo start nie następuje.

DooR w WAVE działa na tej samej zasadzie. Zanim przejdziesz do następnego etapu — sprawdź czy warunki operacyjne są spełnione. Nie „czy czujesz się gotowy" — lecz „czy istnieje to, co wymagane."

### DooR — mechanizm przejścia

```
                    ╭─── DooR ───╮
                    │             │
  ETAP N            │  Standard   │           ETAP N+1
  ─────────         │  gotowości  │           ──────────
                    │             │
  Wynik pracy  ───▶ │  ✅ ✅ ✅   │ ───▶  Następny krok
  dotychczasowej    │  ✅ ✅ ✅   │        (z pewnością
                    │  ✅ ✅ ✅   │         że wsad jest
                    │             │         kompletny)
                    ╰─────────────╯
                          │
                    Jedno ❌ = STOP
                    Wróć i uzupełnij
```

### DooR vs DoR ze Scruma

| Cecha | DoR (Scrum) | DooR (WAVE) |
|---|---|---|
| Pytanie | „Czy zespół rozumie zadanie?" | „Czy artefakt jest kompletny?" |
| Natura | Stan umysłu (subiektywny) | Stan dokumentu (weryfikowalny) |
| Sprawdzenie | Rozmowa z zespołem | Test na artefakcie (3 pytania RtS) |
| Szczegółowość | Ogólny — „czy jasne?" | Atomowy — „jaki typ pola? co gdy NULL?" |
| Dla kogo | Ludzi w zespole | AI w oknie kontekstowym |

### Standardy gotowości w WAVE

| Standard | Etap | Co sprawdza | Test |
|---|---|---|---|
| **Living Pattern** | Gotowość WIEDZY | Najlepsza dostępna wiedza? | 3 rundy PULSE ukończone |
| **RtS** | Gotowość KODU | Blueprint 11 warstw kompletny? | 3 pytania: dane / awaria / bezpieczeństwo |
| **DoD** | ZAMKNIĘCIE etapu | Kod = blueprint? | Checklista: migracje, testy, flagi |

### Symetria RtS ↔ DoD

```
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  ✅ RtS                  SESJA KODOWANIA              DoD ✅ │
  │                                                              │
  │  ◄── OTWIERA ──────────── TRWA ──────────── ZAMYKA ──►      │
  │                                                              │
  │  11 warstw wejściowych         11 kryteriów zamknięcia       │
  │  ─────────────────────         ────────────────────────      │
  │  Dane zdefiniowane       ──▶   Migracje wykonane             │
  │  API wyspecyfikowane     ──▶   Endpointy odpowiadają         │
  │  Logika ze wzorami       ──▶   Testy jednostkowe OK          │
  │  Stany i przejścia       ──▶   Flagi przełączalne            │
  │  Integracje zmapowane    ──▶   Moduły połączone              │
  │  UI opisane              ──▶   Komponenty renderują          │
  │  Testy przygotowane      ──▶   Testy E2E przechodzą          │
  │  Meta ustalone           ──▶   Konwencje zachowane           │
  │  Bezpieczeństwo zamknięte──▶   Pen-test bazowy OK            │
  │  Odporność zaplanowana   ──▶   Scenariusze awarii OK         │
  │  Obserwowalność zdef.    ──▶   Logi i metryki żywe          │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
```

---

## 5. Komponenty — otwarta mapa narzędzi

Zestaw komponentów WAVE jest celowo otwarty. Jak ekosystem leśny — zamknięte są warunki jakości (gleba, woda, światło), otwarta jest lista gatunków.

### Living Patterns — ekosystem żywej wiedzy

Living Patterns odpowiadają na pytanie: **„Czy działamy na najlepszych możliwych założeniach?"**

### Living Patterns — przepływ

```
  ┌──────────┐     ┌─────────────┐     ┌──────────────┐
  │  SCAN    │────▶│   PULSE     │────▶│ Living       │
  │  (raz)   │     │   × N       │     │ Pattern v3   │
  │          │     │  obszarów   │     │              │
  │ Mapa     │     │ 3 rundy     │     │ ↻ auto-      │
  │ terenu   │     │ per obszar  │     │  doskonalenie │
  └──────────┘     └─────────────┘     └──────────────┘
```

### PULSE — krzywa malejących przyrostów

```
  Wartość
  dodana
    │
100%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·····97%
    │                                    ·
    │                          ·  ·  ·         RUNDA 3: +12%
 85%├─ ─ ─ ─ ─ ─ ─ ─ · ─ ─ ─ ─              prawo, edge cases
    │              ·
    │           ·         RUNDA 2: +25%
 60%├─ ─ ─ · ─ ─ ─      porażki, kontrowersje
    │    ·
    │  ·     RUNDA 1: +60%
    │·       fundament: nauka, branża, praktyka
    ├──────────┬──────────┬──────────┬──────────▶
    0          1          2          3         (4) +3%
```

### Struktura Living Pattern

```
  LIVING PATTERN: [NAZWA OBSZARU]
  │
  ├── I. STAN WIEDZY
  │   ├── Co wiemy na pewno
  │   ├── Co jest dyskusyjne
  │   └── Co się zmienia
  ├── II. ZASADY I STANDARDY
  │   ├── Zasady projektowe (reguła + miara + implikacja)
  │   ├── Standardy (tabele cel/alarm)
  │   └── Implikacje dla ekosystemu
  ├── III. MATRYCA BŁĘDÓW (krytyczne → poważne → subtelne)
  ├── IV. MATRYCA DECYZJI (warianty + rekomendacja)
  ├── V. METRYKI SUKCESU (wiodące + opóźnione)
  ├── VI. ŹRÓDŁA (badania + raporty + case studies)
  └── DZIENNIK ZMIAN (v1 → v2 → v3 → auto-doskonalenie)
```

### Auto-doskonalenie i Cross-Session Merge

Living Pattern po trzech rundach PULSE jest kompletny — ale nie zamknięty. Dwa mechanizmy utrzymują go przy życiu.

Pierwszy to cykliczne auto-doskonalenie: ponowne przeszukanie źródeł co kwartał i porównanie ze stanem dokumentu. Czy coś się zmieniło? Czy nowe badania podważają istniejące zasady?

Drugi — odkryty empirycznie — to **Cross-Session Merge**: uruchomienie nowej sesji PULSE z celowo innym kątem ataku (np. porażki zamiast sukcesów, perspektywa trzech lat zamiast stanu bieżącego), a następnie scalenie znalezisk z istniejącym Living Pattern. Wynik: dokument silniejszy niż którakolwiek sesja osobno. Test na żywym projekcie: scoring 7.4 (sesja 1) + 8.0 (sesja 2) = >9.0 (scalenie). Runda 4 w tej samej sesji daje ~3% przyrostu. Cross-Session Merge z innym kątem daje 15–25% nowej wartości.

### LP Pipeline — infrastruktura automatyzacji

Living Patterns mają działający półautomatyczny pipeline na GitHub Actions. Proposal Generator codziennie proponuje nowe dziedziny do zbadania. Człowiek zatwierdza — pipeline uruchamia SCAN, trzy rundy PULSE i Publisher, który tworzy gotowy plik. Koszt jednego Living Pattern: poniżej dolara. Między każdym krokiem bramka decyzyjna — AI proponuje, człowiek zatwierdza. Filozofia WAVE w infrastrukturze.

Metoda potwierdzona jako **stabilna i powtarzalna**: dwie niezależne sesje PULSE dla tego samego obszaru doszły do identycznych fundamentów (18 zasad, ~25 błędów, te same metryki docelowe) z różnymi profilami — bo kąt ataku był inny.

### FALA — From Architecture to Live Application

```
  WEJŚCIE                    SESJA                      WYJŚCIE
  ═══════════════════════════════════════════════════════════════

  Dokumenty koncepcyjne   ┌──────────────┐
  + RtS Walidacja       ──▶│  SESJA 1     │──▶  Audyt RtS
  + Decision Log          │  AUDYT       │     Gap Map ✅⚠️❌
                          └──────┬───────┘
                                 │ Właściciel odpowiada
  Audyt + odpowiedzi       ┌──────────────┐
  + Szablon Blueprint    ──▶│  SESJA 2     │──▶  Blueprint
                            │  BLUEPRINT   │     11 warstw + 3×PASS
                            └──────┬───────┘
                                   │ Autotest RtS
  Blueprint modułu          ┌──────────────┐
  + Próbka kodu           ──▶│  SESJA 3     │──▶  Kod + testy + DoD ✅
                             │  KODOWANIE   │
                             └──────────────┘
```

### 11 warstw RtS — co AI musi widzieć

| # | Warstwa | AI wie... | Bez tego AI... |
|:---:|---|---|---|
| 1 | **Dane** | NA CZYM operuje | pisze `content TEXT` zamiast typów |
| 2 | **API** | CO robi na zewnątrz | wymyśla ścieżki i formaty |
| 3 | **Logika** | JAK myśli | upraszcza, pomija edge cases |
| 4 | **Stany** | KIEDY reaguje | ignoruje przejścia stanów |
| 5 | **Integracje** | Z CZYM rozmawia | łamie kontrakty |
| 6 | **UI** | CO użytkownik widzi | zgaduje layout i stany |
| 7 | **Testy** | JAK zweryfikować | pisze testy bez danych |
| 8 | **Meta** | W CZYM pisać | miesza style i konwencje |
| 9 | **Bezpieczeństwo** | CZEGO NIE ROBIĆ | pisze happy path |
| 10 | **Odporność** | CO GDY AWARIA | 7 endpointów = 7 formatów |
| 11 | **Obserwowalność** | CO MÓWI O SOBIE | loguje wszystko lub nic |

### Decision Log

Centralny rejestr decyzji projektu. Każda decyzja: data, kontekst, treść, uzasadnienie, odrzucone alternatywy, wpływ, źródło. Kręgosłup projektu — gdy za trzy miesiące ktoś zapyta „dlaczego wariant D?" odpowiedź jest w logu, nie w czyjejś pamięci.

### Praktyki

Nawyki pracy — zbiór otwarty. Checkpointy co 2h. Krótsze czaty tematyczne (jeden temat = jeden czat). Wersjonowanie dokumentów (_v1, _v2, _v3_revised). Imperatyw współpracy — celebracja przełomów, wartość drogi.

---

## 6. Test kompletności — czwórka AANP

W mechanice są cztery siły fundamentalne. W WAVE każdy proces ma cztery elementy fundamentalne. Brak jednego — proces dziurawy, z wysokim ryzykiem że nie da oczekiwanego efektu.

### AANP — cztery elementy i cztery patologie

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │              KOMPLETNY PROCES WAVE                          │
  │                                                             │
  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
  │   │  AKTOR   │→ │  AKCJA   │→ │ NARZĘDZIE│→ │ PRODUKT  │  │
  │   │  KTO     │  │  CO      │  │  CZYM    │  │  WYNIK   │  │
  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
  │                                                             │
  │   Cztery z czterech = proces wykonalny ✅                   │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  CO SIĘ DZIEJE GDY BRAKUJE JEDNEGO:

  ❌ Aktor     → Zadanie wisi. Nikt nie odpowiada.
  ❌ Akcja     → Ludzie mają narzędzia, nie wiedzą jak użyć.
  ❌ Narzędzie → Każda sesja = improwizacja. Zero powtarzalności.
  ❌ Produkt   → Robią, robią, nie wiadomo kiedy koniec.
```

### Test AANP — diagnostyka procesu

| Element | Pytanie | Jeśli brakuje |
|---|---|---|
| **Aktor** | Kto to robi? W jakiej konfiguracji H-AI? | Zadanie bez adresata |
| **Akcja** | Co robi krok po kroku? Jak wie kiedy dalej? | Narzędzia bez instrukcji |
| **Narzędzie** | Jakim instrumentem? Prompt, szablon, checklista? | Improwizacja zamiast systemu |
| **Produkt** | Co masz w ręku gdy skończysz? W jakim formacie? | Praca bez mierzalnego efektu |

### AANP w praktyce — weryfikacja procesów WAVE

| Proces | Aktor | Akcja | Narzędzie | Produkt | Status |
|---|---|---|---|---|:---:|
| **PULSE** | Człowiek + AI | 3 rundy z decyzją | PULSE-Prompt, HowTo | Living Pattern v3 | ✅ |
| **FALA Sesja 2** | Właściciel + AI | Wypełnij 11 warstw → autotest | Szablon, RtS, Autotest | Blueprint modułu | ✅ |
| **SCAN** | Człowiek + AI | 5 etapów analizy | SCAN-Prompt, HowTo | Mapa terenu | ✅ |
| **Checkpoint** | Człowiek + AI | Zatrzymaj → log | ??? | Plik MD (nieformalny) | ⚠️ |

Checkpoint wymaga sformalizowania narzędzia i produktu — AANP natychmiast to pokazuje.

### AANP nie jest zamkniętą listą procesów

AANP nie mówi JAKIE procesy budować — mówi JAK SPRAWDZIĆ czy to co zbudowałeś jest kompletne. WAVE jest zbiorem otwartym. Nowe procesy mogą powstawać. AANP jest testem zamkniętym.

```
  ZAMKNIĘTE RAMY                    OTWARTY ŚRODEK
  ═══════════════                   ═══════════════

  • 5 aksjomatów                    • Nowe narzędzia
  • Test AANP                       • Nowe Living Patterns
  • Zasada DooR                     • Nowe praktyki
                                    • Nowe procedury
  Jak rama okna:                    • Nowe standardy DooR
  sztywna, żeby trzymać
                                    Jak widok za oknem:
                                    zmienia się, rośnie, żyje
```

---

## 7. WAVE a istniejące metodyki — inne pytanie, inny poziom

### Piętra budynku — gdzie siedzi każda metodyka

```
  PIĘTRO 5    ┌─────────────────────────────────────────────┐
  STRATEGIA   │  Strategia firmy, wizja produktu            │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 4    ┌─────────────────────────────────────────────┐
  ZARZĄDZANIE │  PRINCE2 / PMBOK                            │
              │  Harmonogram, budżet, raportowanie          │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 3    ┌─────────────────────────────────────────────┐
  ORGANIZACJA │  Scrum / Kanban / XP                        │
              │  Sprinty, backlog, standupy                  │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 2    ┌─────────────────────────────────────────────┐
  ZASADY      │  Lean / Kaizen                              │
              │  Eliminuj marnotrawstwo                     │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 1    ╔═════════════════════════════════════════════╗
  SESJA H-AI  ║  WAVE                                      ║
              ║  Jak współpracować z AI w konkretnej sesji  ║
              ╚═════════════════════════════════════════════╝
```

Nie ma konfliktu. Możesz prowadzić projekt w PRINCE2, organizować pracę w Scrumie, stosować Lean — i jednocześnie używać WAVE do każdej sesji z AI.

### WAVE na mapie nowych podejść 2026

| Podejście | Główny obszar | Siła | Ograniczenie |
|---|---|---|---|
| **WAVE** | Kompletny cykl: wiedza → specyfikacja → kod → weryfikacja | Cały przepływ, głęboki kontekst, potwierdzone w praktyce | Wymaga adaptacji do innych kontekstów |
| **SDD** (Spec-Driven Dev) | Specyfikacje jako źródło prawdy | Wsparcie branży (GitHub, Amazon) | Ryzyko „waterfall w markdownie" |
| **Context Engineering** | Zarządzanie oknem kontekstu AI | Praktyczne techniki promptingowe | Brak pełnego cyklu dostarczania |
| **Thread-Based Eng.** | AI jako nadzorowany contributor | Structured review, jasne role | Słaba warstwa przygotowania |
| **Structured Vibes** | Prototypuj vibem, buduj z rygorem | Pragmatyczne, fazowe | Słaba warstwa kontekstu |

### Co WAVE dzieli z tradycyjnymi, co jest unikalne

| Aspekt | Tradycyjne | WAVE | Relacja |
|---|---|---|---|
| Przygotowanie | PRINCE2: dokumentacja dla ludzi | Dokumentacja jako PALIWO dla AI | Wspólna wartość, inna motywacja |
| Iteracyjność | Scrum: sprinty | PULSE: 3 rundy per obszar | Wspólna zasada, inny rytm |
| Eliminacja marnotrawstwa | Lean: optymalizuj przepływ | 70/30: inwestuj w przygotowanie | Wspólny cel, inny mechanizm |
| **AI jako partner** | **Brak** | **Rdzeń metodyki** | **Unikalne** |
| **DooR** | **Brak odpowiednika** | **Standardy gotowości dla AI** | **Unikalne** |
| **Living Patterns** | **Brak odpowiednika** | **Żywa baza wiedzy** | **Unikalne** |

### Dlaczego WAVE zyskuje na znaczeniu — trzy trendy 2026

```
  TREND 1: Rosnąca moc narzędzi = rosnące ryzyko bez ram
  ─────────────────────────────────────────────────────
  Cursor 2.0+ z 8 agentami • Claude 1M tokenów • Background Agents
  → Potężniejsze narzędzie bez metodyki = potężniejszy generator chaosu

  TREND 2: Branża zmierza ku Spec-Driven Development
  ─────────────────────────────────────────────────────
  Amazon Kiro • GitHub Spec-Kit • arXiv papers • Thoughtworks
  → Specyfikacje jako główny artefakt — WAVE było tam pierwsze

  TREND 3: Nadchodzi „reckoning" 2026-2027
  ─────────────────────────────────────────────────────
  Dług z 2023-2025 osiągnie masę krytyczną • „Spaghetti Point"
  → Kto budował z metodyką — w pozycji siły. Reszta — naprawia.
```

---

## 8. Przykład zastosowania — IDareU Gen2

### Kontekst

IDareU Gen2 to trójstronny marketplace łączący mentorów, użytkowników i marki, z mechanizmem wyzwań wideo, feedbackiem eksperckim, gamifikacją i innowacyjnym modelem podziału przychodów (IdUShare). Stack: Next.js 15, Supabase, Tailwind CSS, shadcn/ui. Zespół: CEO, COO, AI jako główny partner technologiczny.

WAVE jest metodyką wytwórczą IDareU Gen2 od pierwszego dnia.

### Przepływ WAVE w IDareU

```
  ┌─────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────┐
  │  SCAN   │────▶│   PULSE     │────▶│ Projektow.   │────▶│   FALA   │
  │  1 sesja│     │   × 10      │     │ 20 dok. core │     │  × moduł │
  │         │     │  obszarów   │     │ Decision Log │     │ 3 sesje  │
  └─────────┘     └─────────────┘     └──────────────┘     └──────────┘
       ▼                ▼                    ▼                   ▼
   Mapa terenu    Living Patterns     31+ decyzji          Kod + DoD ✅
```

### IDareU Gen2 w liczbach

| Metryka | Wartość | Znaczenie |
|---|:---:|---|
| Decyzje w Decision Log | 31+ | Każda z kontekstem i odrzuconymi alternatywami |
| Dokumenty serii core | 20 | Pełna specyfikacja platformy |
| Linie dokumentacji | ~7000+ | Kompletny kontekst — zero zgadywania |
| Warstwy inteligencji AI | 3 | HIVE + TACIT + AGAPE = Triada Logos |
| Przepływy krzyżowe Triady | 6 | Każdy filar wzbogaca pozostałe |
| Warstwy emergencji | 5 | System uczy się tego, czego projektant nie przewidział |
| Living Interface — warstwy | 5 | Adaptacyjny UI behawioralny od dnia 0 |
| Zespół | 2 + AI | CEO, COO, Claude jako partner technologiczny |

### Pełny cykl życia WAVE — od pomysłu do żywego produktu

```
  FAZA PRZYGOTOWAWCZA (70%)                    FAZA EGZEKUCYJNA (30%)
  ═══════════════════════════                   ═══════════════════════

  SCAN ──▶ Mapa terenu
       │
  PULSE × N ──▶ Living Patterns
       │                              DooR: Living Pattern ✅
  Projektowanie ──▶ Specyfikacje
       │                              DooR: RtS ✅
  FALA Sesja 1 ──▶ Audyt
       │
  FALA Sesja 2 ──▶ Blueprint ──▶ FALA Sesja 3 ──▶ Kod + DoD ✅
       │
  ŻYCIE ──▶ Auto-doskonalenie LP, Decision Log, Checkpointy
            Wiedza kumuluje się, nie rozprasza
```

---

## 9. Słownik pojęć

| Termin | Definicja |
|---|---|
| **WAVE** | Workflow Amplification via Vectored Expertise. Metodyka współpracy człowiek-AI. |
| **H-AI** | Human-AI. Para człowiek-AI jako jednostka współpracy. |
| **DooR** | Definition of Operational Readiness. Kategoria standardów gotowości w WAVE. |
| **Living Pattern** | Żywy dokument wiedzy implementacyjnej, podlegający cyklicznej weryfikacji. |
| **SCAN** | Solution Coverage Area Navigator. Narzędzie identyfikujące obszary implementacyjne. |
| **PULSE** | Pattern Universal Living Standard Engine. Buduje Living Pattern w 3 rundach. |
| **FALA** | From Architecture to Live Application. Procedura: dokument koncepcyjny → kod. |
| **RtS** | Requisite-to-Start. 11 warstw blueprintu technicznego. Element DooR. |
| **DoD** | Definition of Done. Standard zamknięcia etapu. Element DooR. |
| **AANP** | Aktor, Akcja, Narzędzie, Produkt. Test kompletności procesu. |
| **DataPrep** | Poziom 1 H-AI. Uporządkowanie wiedzy dziedzinowej. |
| **Prompt2Data** | Poziom 2 H-AI. Precyzyjne zadanie z pełnym kontekstem. |
| **Prompt2Prompt** | Poziom 3 H-AI. Meta-sterowanie: ocena, korekta, iteracja. |
| **Gap Map** | Narzędzie RtS. Porównanie dokumentacji z 11 warstwami: ✅ / ⚠️ / ❌ |
| **Funkcja celu** | Jedno zdanie definiujące co optymalizujemy. Kompas procesu. |
| **Auto-doskonalenie** | Cykliczna weryfikacja aktualności Living Pattern. |
| **Cross-Session Merge** | Wariant auto-doskonalenia: dwie sesje PULSE z różnymi kątami, scalenie w silniejszy LP. |
| **LP Pipeline** | Półautomatyczny pipeline na GitHub Actions: Proposal → SCAN → PULSE × 3 → Publisher. |
| **Paradoks produktywności** | Zjawisko: AI przyspiesza kodowanie ale nie poprawia dostarczania. |

---

*Dokument opracowany: 11 marca 2026*  
*Wersja: Software Engineering v1.2*  
*Autor koncepcji: Przemek Zieliński*  
*Opracowanie: Claude Opus 4.6*  
*Licencja: CC BY-SA 4.0*  
*Repozytorium: github.com/przemek-zielinski/WAVE-Methodology*  
*Pierwsza dziedzina zastosowania: Software Engineering*  
*Źródła danych: METR, Faros AI, GitClear, CodeRabbit, Apiiro, NBER, MIT Media Lab, Stack Overflow, Fed San Francisco (luty 2026)*
