# Metodyka WAVE / FALA
## Workflow Amplification via Vectored Expertise
## Formuła Amplifikacji Ludzkiej Aktywności
### Metodyka współpracy człowiek-AI

**Wersja:** 2.0  
**Data:** Marzec 2026  
**Autor:** Przemysław Zieliński  
**Współtwórca dokumentacji:** Claude (Anthropic)  
**Licencja:** CC BY-SA 4.0  
**Repozytorium:** github.com/przemek-zielinski/WAVE-Methodology

---

## Spis treści

— Szybki Start — zacznij tutaj
0. W jednym zdaniu, w jednym akapicie, w jedną minutę
1. Problem
2. Filozofia — pięć aksjomatów i trzy poziomy współpracy H-AI
3. Architektura — trzy warstwy WAVE
4. DooR — drzwi między etapami
5. Komponenty — otwarta mapa narzędzi
6. Test kompletności — czwórka AANP
7. Profile Produktu — WAVE dla każdej skali
8. Co i jak mierzyć
9. WAVE poza oprogramowaniem — sześć kierunków
10. WAVE a istniejące podejścia
11. Jak zacząć
12. Najczęstsze pytania
13. Geneza
14. Cytowanie i licencja

### Mapa WAVE — architektura w jednym spojrzeniu

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║   WAVE — Workflow Amplification via Vectored Expertise                 ║
║   Metodyka Współpracy Człowiek-AI                                     ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 1: FILOZOFIA (zamknięta — 5 aksjomatów)              │   ║
║   │                                                                │   ║
║   │  70/30 • Człowiek kieruje • Buduj kompletnie • Droga=wartość  │   ║
║   │  • Porażki uczą                                                │   ║
║   │                                                                │   ║
║   │  Meta-aksjomat: Prądy i Napięcia (nawigacja, nie optymalizacja)│   ║
║   │  Trzy poziomy H-AI: DataPrep → Prompt2Data → Prompt2Prompt    │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 2: KOMPONENTY (otwarte — zbiór rośnie)               │   ║
║   │                                                                │   ║
║   │  DooR — Definition of Operational Readiness                   │   ║
║   │  Living Patterns (SCAN, PULSE) • FALA • Decision Log          │   ║
║   │  [+ przyszłe komponenty → zbiór otwarty]                      │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  WARSTWA 3: PRAKTYKI (otwarte — nawyki narastają)             │   ║
║   │                                                                │   ║
║   │  Checkpointy • Krótsze sesje • Wersjonowanie • Imperatyw      │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║   ┌────────────────────────────────────────────────────────────────┐   ║
║   │  TEST KOMPLETNOŚCI: AANP (zamknięty)                          │   ║
║   │  Każdy proces = Aktor + Akcja + Narzędzie + Produkt           │   ║
║   └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Uwaga terminologiczna

WAVE to **metodyka** — zbiór zasad dotyczących sposobów wykonywania pracy. Nie „metodologia" (nauka o metodach), nie „metoda" (pojedynczy sposób), nie „model" (uproszczone odwzorowanie). Scrum, PRINCE2, Extreme Programming — to metodyki. WAVE dołącza do tej kategorii, adresując pytanie, którego żadna z nich nie pokrywa: jak współpracować z AI.

---

## Szybki Start — zacznij tutaj

Nie chcesz czytać czternastu rozdziałów zanim zaczniesz? Oto minimum.

**Co to jest:** Metodyka współpracy człowiek-AI. Mówi jak przygotować kontekst, prowadzić sesję i budować wiedzę, żeby AI pracował na najlepszych założeniach — nie na zgadywaniu.

**Jak zacząć w trzech krokach:**

```
  KROK 1 — Wybierz profil produktu
  ─────────────────────────────────
  □ Prototyp / POC?        → Profil DISCOVERY (1-5 dni)
  □ MVP / pilot?           → Profil BUILD (4-8 tygodni)
  □ Produkt docelowy?      → Profil SCALE (miesiące)

  Nie wiesz? Zacznij od DISCOVERY. Zawsze możesz przesunąć wyżej.

  KROK 2 — Uruchom SCAN
  ──────────────────────
  Otwórz czat z AI. Wklej prompt SCAN z opisem swojego rozwiązania.
  Dostaniesz listę obszarów do zbadania z gotowymi parametrami.

  KROK 3 — Uruchom PULSE dla pierwszego obszaru
  ───────────────────────────────────────────────
  Weź najważniejszy obszar z listy SCAN. Wklej prompt PULSE
  z parametrami. Przeprowadź Rundę 1. Oceń wynik. Masz pierwszy
  Living Pattern — żywy dokument wiedzy. Powtórz dla kolejnych.
```

**Czego potrzebujesz:** Dostęp do AI z wyszukiwaniem internetowym (Claude, ChatGPT, Gemini z web search). Opis swojego rozwiązania. Opcjonalnie: istniejąca dokumentacja projektu.

**Pliki do pobrania z repozytorium:**

| Plik | Co robi | Kiedy użyć |
|---|---|---|
| `SCAN-Prompt.md` | Identyfikuje obszary do zbadania | Na początku — raz |
| `SCAN-HowTo.md` | Instrukcja użycia SCAN | Przed pierwszym SCAN |
| `PULSE-Prompt.md` | Buduje Living Pattern w 3 rundach | Per obszar z listy SCAN |
| `PULSE-HowTo.md` | Instrukcja użycia PULSE | Przed pierwszym PULSE |

Reszta dokumentu wyjaśnia DLACZEGO to działa, JAK jest zbudowane i CO możesz osiągnąć na większą skalę.

---

## 0. W jednym zdaniu, w jednym akapicie, w jedną minutę

### Jedno zdanie

WAVE to metodyka współpracy człowiek-AI — mówi jak przygotować kontekst, prowadzić sesję i budować wiedzę, żeby AI pracował na najlepszych możliwych założeniach, a nie na zgadywaniu.

### Jeden akapit

Każdy kto pracuje z AI zna ten moment — AI daje coś średniego, poprawiasz, poprawiasz, po godzinie masz coś używalnego. Następnego dnia zaczynasz od zera. WAVE odwraca tę proporcję: większość czasu inwestujesz w przygotowanie kontekstu i wiedzy, mniejszość w egzekucję — i ta egzekucja jest celna od pierwszego strzału. WAVE daje konkretne narzędzia: SCAN rozpoznaje co musisz wiedzieć, PULSE buduje tę wiedzę w trzech rundach, Living Pattern utrzymuje ją aktualną. Rezultat: AI przestaje zgadywać i zaczyna działać jak partner, który naprawdę rozumie twój projekt.

### Jedna minuta

Mamy problem, którego nikt nie nazwał. Miliony ludzi codziennie pracują z AI — piszą kod, projektują produkty, analizują dane, tworzą dokumenty. I większość z nich robi to tak samo: wrzucam prompt, patrzę co wyjdzie, poprawiam, poprawiam, poprawiam. To jest jak budowanie domu bez projektu — stawiasz ścianę, burzysz, stawiasz inaczej. Działa, ale marnujesz ogromną część potencjału.

WAVE mówi: odwróć proporcję. Zanim zaczniesz budować — przygotuj kontekst. Zbierz wiedzę. Zdefiniuj co optymalizujesz. Daj AI pełny obraz, a nie strzęp informacji. Przygotowanie dominuje nad egzekucją. I ta egzekucja jest celna, bo AI nie zgaduje — wie.

WAVE nie jest kolejnym frameworkiem zarządzania projektami. Nie konkuruje ze Scrumem ani z Lean. WAVE działa na poziomie, którego żadna istniejąca metodyka nie adresuje — na poziomie sesji roboczej, w której człowiek i AI razem tworzą coś konkretnego. Jest open-source, jest darmowa, i każdy może zacząć ją stosować dziś — od jednego narzędzia, od jednej sesji.

---

## 1. Problem

W 2026 roku każda organizacja na świecie ma dostęp do sztucznej inteligencji. Szpitale używają jej do diagnostyki. Kancelarie prawne do analizy precedensów. Szkoły do personalizacji nauczania. Inżynierowie do optymalizacji projektów. Zespoły programistyczne do generowania kodu.

I niemal wszystkie robią to tak samo: chaotycznie.

Typowa interakcja wygląda tak: specjalista zadaje AI pytanie, dostaje wynik, stwierdza że nie o to chodziło, pyta ponownie innymi słowami, dostaje trochę inny wynik, poprawia, pyta jeszcze raz. Dziesięć iteracji później wynik jest znośny, ale daleki od tego, co było możliwe.

```
  BEZ METODYKI                              Z WAVE
  ─────────────────────────────              ─────────────────────────────

  😐 → [prompt] → 🤖 → wynik 4/10          😐 → [kontekst + wiedza + cel]
  😐 → [poprawka] → 🤖 → wynik 5/10               ↓
  😐 → [poprawka] → 🤖 → wynik 6/10          🤖 → wynik 9/10 ✅
  😐 → [poprawka] → 🤖 → wynik 7/10
  😐 → [poprawka] → 🤖 → wynik 8/10 ✅      czas: ~1h
                                              (przygotowanie + egzekucja)
  czas: 3h+ (zero przygotowania,
  wszystko w poprawkach)
```

To nie jest porażka sztucznej inteligencji. To porażka współpracy. Problem nie leży w AI — AI jest potężne. Problem nie leży w człowieku — człowiek ma ekspertyzę. Problem leży w **przestrzeni między nimi** — w sposobie, w jaki ludzka wiedza i intencja trafia do AI.

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

Narzędzia istnieją. Brakuje **metodyki** — uporządkowanego, warstwowego, mierzalnego systemu współpracy z AI, który stawia w centrum jedną zasadę: **człowiek prowadzi, AI wzmacnia**.

To, co dziś uchodzi za podejście do współpracy z AI, nie wypełnia tej luki:

| Podejście | Czym jest | Czego mu brakuje |
|---|---|---|
| **Prompt engineering** | Techniki pisania lepszych zapytań | Brak struktury projektowej, mierników, warstwy przygotowania |
| **„Agile AI"** | Agile z dopiskiem „z AI" | Brak przemyślenia relacji człowiek-AI |
| **Wytyczne odpowiedzialnego AI** | Polityki etyczne | To nie przepływ pracy — mówi czego unikać, nie jak pracować |
| **Kursy narzędziowe** | Instrukcje obsługi produktów | Specyficzne dla produktu, nie są metodyką |

WAVE wypełnia tę lukę.

---

## 2. Filozofia — pięć aksjomatów i trzy poziomy współpracy H-AI

### Pięć aksjomatów

Filozofia WAVE to zbiór zamknięty — pięć przekonań, które nie podlegają negocjacji. Wszystko inne w WAVE może się zmieniać, rosnąć, ewoluować. Te pięć — nie. Są jak prawa termodynamiki: możesz budować dowolną maszynę, ale te prawa zawsze obowiązują.

| # | Aksjomat | Esencja | Analogia |
|:---:|---|---|---|
| 1 | **Przygotowanie dominuje** | Większość czasu na przygotowanie, reszta na egzekucję | Gepard: 16h obserwacji → 12s pościgu |
| 2 | **Człowiek kieruje, AI wzmacnia** | AI to wzmacniacz ekspertyzy, nie zamiennik | Teleskop nie zastępuje oka astronoma |
| 3 | **Buduj kompletnie, aktywuj progresywnie** | Pełna architektura od dnia 1, aktywacja stopniowa | Drzewo: sadzisz kompletne, owoce za 2 lata |
| 4 | **Proces i droga = wartość** | Odkrycia rodzą się między zadaniami | Serendypia: Kolumb → Ameryka |
| 5 | **Porażki uczą więcej niż sukcesy** | Cudze błędy z liczbami > cudze sukcesy bez kontekstu | Sukces usypia, porażka wyostrza |

**Aksjomat 1 — Przygotowanie dominuje nad egzekucją.** WAVE stoi na kontraintuicyjnej regule: poświęć większość czasu na przygotowanie, a mniejszość na wykonanie z AI. To jest grawitacja, nie nakaz — punkt ciążenia zależy od skali projektu. W małym prototypie proporcja ciągnie ku 60/40 (bo produkt jest za prosty żeby przygotowanie potrzebowało dominacji). W średnim projekcie ląduje na 70/30 (tu aksjomat oddycha najpełniej). W dużym produkcie ciągnie ku 50/50 (bo egzekucja rośnie liniowo z każdym modułem). Ale we WSZYSTKICH przypadkach przygotowanie to co najmniej połowa pracy — co jest radykalną odwrotnością chaotycznego promptowania, gdzie przygotowanie równa się zeru.

Analogia to **mise en place** — zasada kucharska, w której szef kuchni przygotowuje wszystkie składniki przed serwisem. Podczas serwisu realizacja jest szybka i precyzyjna. Inwestycja w przygotowanie sprawia, że doskonałość pod presją staje się możliwa.

**Aksjomat 2 — Człowiek kieruje, AI wzmacnia.** AI jest wzmacniaczem ekspertyzy — nie jej zamiennikiem. Jak wzmacniacz nie zastępuje gitary, tylko pozwala jej brzmieć na stadion. To człowiek definiuje funkcję celu, człowiek ocenia wynik, człowiek podejmuje decyzję. AI przetwarza, syntetyzuje, generuje — na skali niedostępnej dla człowieka. Ale kierunek zawsze należy do człowieka. AI bez kierunku ludzkiego produkuje treść poprawną ale generyczną — jak orkiestra bez dyrygenta.

**Aksjomat 3 — Buduj kompletnie, aktywuj progresywnie.** Nie buduj połowy i „dopiszesz resztę później." Buduj całość — ale włączaj ją kawałek po kawałku, w miarę jak dojrzewają warunki. Projektuj pełną architekturę od pierwszego dnia, ale aktywuj przez przełączniki, w miarę jak zbierasz dane i potwierdzasz założenia.

**Aksjomat 4 — Proces i droga mają wartość.** Najcenniejsze odkrycia pojawiają się między zadaniami — w dygresjach, w próbach, w momentach gdy AI odpowiada coś nieoczekiwanego i człowiek mówi: „chwila, to jest ciekawe." WAVE nie jest linią prostą od A do B. Jest rzeką, która płynie w kierunku morza, ale po drodze tworzy meandry i delty — i w tych zakrętach mieszka wartość.

**Aksjomat 5 — Porażki uczą więcej niż sukcesy.** Sukces usypia zmysły. Porażka wyostrza. Dlatego w WAVE każde narzędzie badawcze (PULSE) celowo szuka porażek w jednej z rund — bo cudze błędy z liczbami są cenniejsze niż cudze sukcesy bez kontekstu. Potwierdzenie empiryczne: test powtarzalności WAVE (marzec 2026) pokazał, że dwie niezależne sesje PULSE dla tego samego obszaru doszły do identycznej liczby zasad (18), zbliżonej liczby błędów (25 vs 26) i tych samych fundamentów — ale z różnymi profilami. Sesja nastawiona na porażki dała inny kąt niż sesja nastawiona na przyszłość. Obie potrzebne, żadna niekompletna sama.

### Prądy i Napięcia — meta-aksjomat nawigacji

Pięć aksjomatów mówi CO jest ważne. Prądy i Napięcia mówi JAK te wartości rywalizują ze sobą w każdej konkretnej decyzji — i że rolą operatora jest nawigacja tej rywalizacji, nie jej eliminacja.

Jak prądy oceaniczne — nieustannie płyną obok siebie, czasem zgodnie, czasem przeciwnie. Żeglarz nie walczy z prądami. Czyta je i wybiera optymalną ścieżkę dla aktualnych warunków. Nie próbuje płynąć ze wszystkimi naraz, bo to fizycznie niemożliwe. I zawsze zostawia rezerwę na nieprzewidywalny prąd za rogiem.

```
  POLE NAPIĘĆ — każda decyzja rozgrywa się na przecięciu osi

  Jakość wyniku ◄─────────────────────────────────► Prostota algorytmu
  Stabilność    ◄─────────────────────────────────► Bogactwo funkcji
  Głębokość     ◄─────────────────────────────────► Koszt i czas
  Spójność      ◄─────────────────────────────────► Elastyczność
  Rozwiązanie   ◄─────────────────────────────────► Zapas pojemności
  Kontrola      ◄─────────────────────────────────► Swoboda twórcza

  Operator nie optymalizuje jednej osi.
  Operator nawiguje MIĘDZY osiami — czytając
  która konfiguracja jest krytyczna TERAZ.
```

**Trzy obserwacje fundamentalne.**

Pierwsza: napięcia nie znikają. Nie można ich „rozwiązać" — można je tylko nawigować. Każda poprawa na jednej osi kosztuje coś na innej. Próba optymalizacji wszystkich naraz prowadzi do paraliżu albo do systemu, który jest „trochę dobry we wszystkim" ale doskonały w niczym.

Druga: konfiguracja napięć zmienia się w czasie. Na początku projektu dominuje napięcie jakość↔prostota. W środku — stabilność↔funkcje. Pod koniec — koszt↔głębokość. Operator który czyta aktualną konfigurację podejmuje lepsze decyzje niż operator ze stałymi regułami bez względu na fazę.

Trzecia — i najważniejsza: **zapas jest wartością pierwszej klasy, nie marnotrawstwem.** W myśleniu optymalizacyjnym zapas wygląda jak zmarnowany potencjał — niewykorzystana pojemność, nierozwiązany problem. W myśleniu nawigacyjnym zapas jest rezerwą strategiczną na problem, którego jeszcze nie widzisz. Lean mówi „eliminuj marnotrawstwo." Prądy i Napięcia mówi: „zapas pojemności — budżetowy, architektoniczny, mentalny — to nie jest marnotrawstwo. To jest rezerwa, która decyduje o zdolności systemu do przetrwania."

**Emergencja rodzi się na przecięciu napięć.** To jest rdzeń odkrycia. Prądy i Napięcia to nie tylko opis trade-offów — to opis warunków, w których emergencja zachodzi. Gdy operator świadomie nawiguje napięcia zamiast optymalizować jeden atrybut, otwiera przestrzeń na odkrycia, których nie zaplanował. Cofnięcie czterech iteracji naprawy tabeli nie było porażką — było momentem emergencji, z którego wyłonił się aksjomat warty więcej niż poprawiona tabela.

Carl Benedikt Frey w „How Progress Ends" (Princeton University Press, 2025) potwierdza tę obserwację na skali tysiąca lat historii cywilizacji: innowacja umiera zawsze z tego samego powodu — gdy systemy przestają nawigować napięcie między eksploracją a eksploatacją i zamrażają się w jednym trybie. Chiny dynastii Song zamroziły się w centralizacji. Dolina Krzemowa zamraża się w koncentracji. Korporacje zamrażają się po skalowaniu. WAVE przenosi tę obserwację z poziomu cywilizacji na poziom sesji roboczej — i daje operatorowi narzędzia do świadomej nawigacji.

**Formuła nawigacyjna — trzy pytania przed każdą decyzją:**

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │  1. KTÓRY PRĄD TERAZ DOMINUJE?                         │
  │     (Jakość? Stabilność? Koszt? Zapas? Swoboda?)       │
  │                                                         │
  │  2. CO ZYSKUJĘ, CO TRACĘ?                              │
  │     (Każda poprawa na jednej osi ma cenę na innej)     │
  │                                                         │
  │  3. CZY ZOSTAWIAM WYSTARCZAJĄCY ZAPAS?                 │
  │     (Jeśli za rogiem czeka problem którego nie widzę    │
  │      — czy mam z czego zaczerpnąć?)                    │
  │                                                         │
  │  Trzy pytania. Kilka sekund refleksji.                 │
  │  Nie spowalnia pracy — przyspiesza ją,                 │
  │  bo eliminuje iteracje w ślepe zaułki.                 │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

**Rola operatora.** AI nie widzi pola napięć samodzielnie. AI optymalizuje to co mu zlecisz — jeśli zlecisz naprawę tabeli, będzie naprawiać tabelę przez cztery iteracje, każda bardziej złożona, aż operator powie „stop, cofamy." Człowiek w WAVE prowadzi nie dlatego że jest mądrzejszy od AI w danej dziedzinie. Prowadzi dlatego że widzi pole napięć jako całość — wszystkie osie jednocześnie — i podejmuje decyzje, których AI nie jest w stanie podjąć: „cofamy, bo zapas jest ważniejszy niż perfekcja."

To jest operacyjne rozszerzenie aksjomatu „człowiek prowadzi, AI wzmacnia": człowiek prowadzi **nawigację przez napięcia**, AI wzmacnia **wykonanie w wybranym kierunku**.

### Trzy poziomy współpracy H-AI

Pod aksjomatami żyje model opisujący JAK przebiega każda interakcja człowiek-AI w WAVE. Trzy poziomy, zawsze w tej samej kolejności — jak wdech, puls i wydech.

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║                                                                   ║
  ║  Poziom 1: DataPrep                                    WDECH     ║
  ║  ─────────────────                                               ║
  ║  Człowiek porządkuje wiedzę dziedzinową                          ║
  ║  Zbiera kontekst, definiuje cel, strukturyzuje                   ║
  ║  ● Kto: CZŁOWIEK (głównie)                                      ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Poziom 2: Prompt2Data                                 PULS      ║
  ║  ────────────────────                                            ║
  ║  Precyzyjne zadanie z pełnym kontekstem                          ║
  ║  AI nie zgaduje intencji — intencja jest jawna                   ║
  ║  ● Kto: CZŁOWIEK → AI                                           ║
  ║                                                                   ║
  ║                          ↓                                        ║
  ║                                                                   ║
  ║  Poziom 3: Prompt2Prompt                               WYDECH   ║
  ║  ──────────────────────                                          ║
  ║  Meta-sterowanie: ocena wyniku, korekta, iteracja                ║
  ║  Człowiek kształtuje kierunek, nie pisze treści                  ║
  ║  ● Kto: CZŁOWIEK (ocenia) ← AI (proponuje)                     ║
  ║                                                                   ║
  ║                          ↻ (cykl się powtarza)                   ║
  ║                                                                   ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

**DataPrep** — uporządkowanie wiedzy dziedzinowej przed pracą z AI. Gdy architekt projektuje wieżowiec, nie zaczyna od rysowania cegieł. Zaczyna od wizji, potem wymagań, potem architektury, potem specyfikacji. Każdy dokument rodzi następny. DataPrep działa tak samo — w każdej dziedzinie.

**Prompt2Data** — precyzyjne zadanie dla AI z pełnym kontekstem. Nie „zrób coś słodkiego" lecz „na podstawie tego menu, tych składników, tych ograniczeń — stwórz przepis spełniający wszystkie warunki." Zero zgadywania. Jeden precyzyjny wynik.

**Prompt2Prompt** — meta-sterowanie współpracą. Ocena wyniku, korekta kierunku, iteracja. Człowiek patrzy na to co AI wyprodukował i mówi: „to jest dobre, ale poszukaj z drugiej strony" albo „tu brakuje aspektu bezpieczeństwa." To jest poziom, na którym człowiek naprawdę kieruje.

### Przepływ dwukierunkowy

AI nie dostarcza gotowych wyników. Człowiek weryfikuje, koryguje i odsyła. To nie jest usterka AI — to projekt współpracy.

```
  LUDZKA EKSPERTYZA                  AI JAKO WZMOCNIENIE
  ┌──────────────────────────┐       ┌──────────────────────────┐
  │ Wiedza dziedzinowa        │       │ Przetwarzanie danych     │
  │ Kontekst sytuacyjny       │──────▶│ Rozpoznawanie wzorców    │
  │ Doświadczenie             │       │ Generowanie wariantów    │
  │ Osąd i intuicja           │◀──────│ Skalowanie powtarzalnych │
  │ Odpowiedzialność          │       │   operacji               │
  └──────────────────────────┘       └──────────────────────────┘
            ↕ PRZEPŁYW DWUKIERUNKOWY ↕
```

Każda korekta aktualizuje przygotowanie. Jeśli AI źle zrozumiało wymaganie — to wymaganie było prawdopodobnie niejasne. Napraw je w DataPrep, nie tylko w wyniku.

---

## 3. Architektura — trzy warstwy WAVE

WAVE jako metodyka składa się z trzech warstw różnej natury. Filozofia jest zamknięta — pięć aksjomatów, niezmiennych. Komponenty są otwarte — nowe narzędzia mogą powstawać, społeczność może je dodawać. Praktyki narastają z doświadczeniem.

To jak ekosystem leśny — zamknięte są warunki jakości (gleba, woda, światło), otwarta jest lista gatunków. Las rośnie. Nowe gatunki pojawiają się. Stare ewoluują. WAVE żyje w ten sam sposób.

```
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓                                                              ▓
  ▓  ZAMKNIĘTE (nie podlegają negocjacji):                       ▓
  ▓  • 5 aksjomatów filozofii                                   ▓
  ▓  • Prądy i Napięcia (meta-aksjomat nawigacji)               ▓
  ▓  • Test AANP (4 elementy procesu)                            ▓
  ▓  • Zasada DooR (przejście = kompletność artefaktu)           ▓
  ▓                                                              ▓
  ▓  ┌──────────────────────────────────────────────────────┐    ▓
  ▓  │                                                      │    ▓
  ▓  │  OTWARTE (rosną z doświadczeniem i społecznością):   │    ▓
  ▓  │                                                      │    ▓
  ▓  │  • Nowe narzędzia                                    │    ▓
  ▓  │  • Nowe Living Patterns (per branża, per obszar)     │    ▓
  ▓  │  • Nowe praktyki                                     │    ▓
  ▓  │  • Nowe procedury                                    │    ▓
  ▓  │  • Nowe standardy DooR (per etap, per branża)        │    ▓
  ▓  │                                                      │    ▓
  ▓  └──────────────────────────────────────────────────────┘    ▓
  ▓                                                              ▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

### Trzy warstwy — tabela

| Warstwa | Natura | Co zawiera | Czy się zmienia? |
|---|---|---|---|
| **1. Filozofia** | Zamknięta | 5 aksjomatów + Prądy i Napięcia + 3 poziomy H-AI | Nie — aksjomaty obowiązują zawsze |
| **2. Komponenty** | Otwarta | Narzędzia, standardy, procedury | Tak — zbiór rośnie |
| **3. Praktyki** | Otwarta | Nawyki pracy | Tak — narastają z doświadczeniem |

---

## 4. DooR — drzwi między etapami

### Definition of Operational Readiness

Wyobraź sobie rakietę na platformie startowej. Inżynierowie nie pytają „czy czujemy się gotowi do startu?" Pytają: „czy każdy system przeszedł weryfikację? czy paliwo jest na poziomie? czy telemetria działa?" Lista jest zamknięta, mierzalna, binarna. Albo wszystko jest na zielono, albo start nie następuje.

DooR w WAVE działa na tej samej zasadzie. Zanim przejdziesz do następnego etapu — sprawdź czy warunki operacyjne są spełnione. Nie „czy czujesz się gotowy" — lecz „czy istnieje to, co wymagane."

```
                    ╭─── DooR ───╮
                    │             │
  ETAP N            │  Standard   │           ETAP N+1
  ─────────         │  gotowości  │           ──────────
                    │             │
  Wynik pracy  ───▶ │  ✅ ✅ ✅   │ ───▶  Następny krok
  dotychczasowej    │  ✅ ✅ ✅   │        (z pewnością
                    │             │         że wsad jest
                    │             │         kompletny)
                    ╰─────────────╯
                          │
                    Jedno ❌ = STOP
                    Wróć i uzupełnij
```

DooR to kategoria nadrzędna dla wszystkich standardów gotowości w WAVE. Każde narzędzie, które definiuje „kiedy możesz przejść dalej" — należy do rodziny DooR.

### Standardy DooR w obecnym ekosystemie

| Standard | Etap | Co sprawdza | Przykład testu |
|---|---|---|---|
| **Living Pattern** | Gotowość WIEDZY | Czy mam najlepszą dostępną wiedzę? | 3 rundy PULSE ukończone, struktura kompletna |
| **RtS** (w SE) | Gotowość KODU | Czy specyfikacja jest kompletna? | Test na artefakcie — zero „to zależy" |
| **DoD** (w SE) | ZAMKNIĘCIE etapu | Czy wynik = specyfikacja? | Checklista weryfikacyjna |

Rodzina DooR jest otwarta. Nowe standardy gotowości mogą powstawać — dla nowych etapów, dla nowych branż. Zamknięta jest zasada: **każde przejście ma swoje drzwi, i drzwi otwiera kompletność.**

---

## 5. Komponenty — otwarta mapa narzędzi

### Living Patterns — ekosystem żywej wiedzy

Living Patterns odpowiadają na pytanie, które każdy zespół zadaje sobie w ciszy: **„Czy działamy na najlepszych możliwych założeniach?"**

Zwykle odpowiedź brzmi jedno z trzech: „nie wiemy, bo nie mieliśmy czasu sprawdzić", „sprawdziliśmy, ale to było pół roku temu", „każdy z nas sprawdził coś innego." Living Patterns rozwiązują te trzy problemy jednocześnie.

```
  ┌──────────┐     ┌─────────────┐     ┌──────────────┐
  │  SCAN    │────▶│   PULSE     │────▶│ Living       │
  │  (raz)   │     │   × N       │     │ Pattern v3   │
  │          │     │  obszarów   │     │              │
  │ Mapa     │     │ 3 rundy     │     │ ↻ auto-      │
  │ terenu   │     │ per obszar  │     │  doskonalenie │
  └──────────┘     └─────────────┘     └──────────────┘
```

**SCAN — Solution Coverage Area Navigator.** Radar skanujący horyzont. Na podstawie opisu rozwiązania identyfikuje WSZYSTKIE obszary wymagające pogłębionej analizy — od oczywistych po łatwe do pominięcia. Uruchamia się raz — na początku projektu.

**PULSE — Pattern Universal Living Standard Engine.** Puls — rytmiczny cykl trzech uderzeń. Dla jednego obszaru przeprowadza trzy rundy badawczo-syntetyczne. Runda 1 buduje fundament (~60% wiedzy). Runda 2 weryfikuje z drugiej strony — szuka porażek zamiast sukcesów (~25%). Runda 3 szuka w peryferyjnych kierunkach (~12%). Między rundami decyduje człowiek.

```
  Wartość
  dodana
    │
100%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·····97%
    │                                    ·
    │                          ·  ·  ·         RUNDA 3: +12%
 85%├─ ─ ─ ─ ─ ─ ─ ─ · ─ ─ ─ ─              peryferyjne
    │              ·
    │           ·         RUNDA 2: +25%
 60%├─ ─ ─ · ─ ─ ─      porażki, kontrowersje
    │    ·
    │  ·     RUNDA 1: +60%
    │·       fundament: nauka, branża, praktyka
    ├──────────┬──────────┬──────────┬──────────▶
    0          1          2          3         (4) +3%
```

**Living Pattern — żywy dokument wiedzy.** Produkt PULSE — kompletny wzorzec dla jednego obszaru. Ustandaryzowana struktura: stan wiedzy, zasady i standardy, matryca błędów, matryca decyzji, metryki sukcesu, źródła. Podlega cyklicznemu auto-doskonaleniu — jak organizm, który oddycha. Wdech to nowa wiedza. Wydech to aktualizacja dokumentu.

**Auto-doskonalenie i Cross-Session Merge.** Living Pattern po trzech rundach PULSE jest kompletny — ale nie zamknięty. Dwa mechanizmy utrzymują go przy życiu. Pierwszy to cykliczne auto-doskonalenie: ponowne przeszukanie źródeł co kwartał i porównanie ze stanem dokumentu. Drugi — odkryty empirycznie — to **Cross-Session Merge**: uruchomienie nowej sesji PULSE z celowo innym kątem ataku (np. porażki zamiast sukcesów, perspektywa trzech lat zamiast stanu bieżącego), a następnie scalenie znalezisk z istniejącym Living Pattern. Wynik: dokument silniejszy niż którakolwiek sesja osobno. Test na żywym projekcie: scoring 7.4 (sesja 1) + 8.0 (sesja 2) = >9.0 (scalenie). Runda 4 w tej samej sesji daje ~3% przyrostu. Cross-Session Merge z innym kątem daje 15–25% nowej wartości.

**LP Pipeline — infrastruktura automatyzacji.** Living Patterns mają działający półautomatyczny pipeline na GitHub Actions. Proposal Generator codziennie proponuje nowe dziedziny do zbadania. Człowiek zatwierdza — pipeline uruchamia SCAN, trzy rundy PULSE i Publisher, który tworzy gotowy plik. Koszt jednego Living Pattern: poniżej dolara. Między każdym krokiem bramka decyzyjna — AI proponuje, człowiek zatwierdza. Filozofia WAVE w infrastrukturze.

### FALA — From Architecture to Live Application

FALA to procedura transformująca dokumentację koncepcyjną w działający kod (lub inny artefakt końcowy). Trzy sesje, z wyraźnym kryterium przejścia między każdą.

```
  Sesja 1 ──▶ Sesja 2 ──▶ Sesja 3
  AUDYT       BLUEPRINT    REALIZACJA

  Zmierz      Wypełnij     Wykonaj
  dystans     specyfikację z kompletnego
  (co mam     (co brakuje  kontekstu
  vs co       → uzupełnij)
  potrzebuję)
```

W software engineering FALA obejmuje pipeline RtS (Requisite-to-Start) z jedenastoma warstwami specyfikacji technicznej i autotest trzema pytaniami. W innych branżach FALA adaptuje się — sesje mają tę samą logikę (audyt → specyfikacja → realizacja), ale warstwy specyfikacji są inne.

Pełna dokumentacja FALA dla software engineering: osobny dokument w repozytorium.

### Decision Log

Centralny rejestr decyzji projektu. Każda zatwierdzona decyzja: data, kontekst, treść, uzasadnienie, odrzucone alternatywy, wpływ. Nie jest notatnikiem — jest kręgosłupem projektu. Gdy za trzy miesiące ktoś zapyta „dlaczego wybraliśmy tę drogę?" — odpowiedź jest w logu, nie w czyjejś pamięci.

### Praktyki

Nawyki pracy, które narastają z doświadczeniem. Zbiór otwarty.

**Checkpointy.** Po dwóch godzinach intensywnej pracy — zatrzymaj się. Wygeneruj log sesji: co zrobiliśmy, jakie decyzje padły, co odrzuciliśmy. Pamięć projektu, która przetrwa zamknięcie czatu.

**Krótsze sesje tematyczne.** Jeden temat na sesję. Nie maratony po sto wiadomości — krótkie, celowane interakcje. AI działa lepiej ze świeżym kontekstem niż z przeciążonym oknem.

**Wersjonowanie dokumentów.** Każdy dokument ma wersję, datę, dziennik zmian. Nie „plik_final_v2_NAPRAWDĘ_final." Struktura czytelna i przewidywalna.

**Imperatyw współpracy.** Rozpoznawaj momenty przełomu i celebruj je. Proces i droga mają wartość — nie tylko cel.

---

## 6. Test kompletności — czwórka AANP

W mechanice są cztery siły fundamentalne — grawitacja, elektromagnetyzm, silna i słaba. Każde zjawisko fizyczne jest wynikiem ich współdziałania. Jeśli zignorujesz jedną — twój model nie opisuje rzeczywistości.

W WAVE każdy proces ma cztery elementy fundamentalne. Jeśli brakuje jednego — proces jest dziurawy, z wysokim ryzykiem że nie da oczekiwanego efektu.

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │              KOMPLETNY PROCES WAVE                          │
  │                                                             │
  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
  │   │  AKTOR   │→ │  AKCJA   │→ │ NARZĘDZIE│→ │ PRODUKT  │    │
  │   │  KTO     │  │  CO      │  │  CZYM    │  │  WYNIK   │    │
  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
  │                                                             │
  │   Cztery z czterech = proces wykonalny ✅                   │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

| Element | Pytanie | Jeśli brakuje |
|---|---|---|
| **Aktor** | KTO to robi? Człowiek, AI, obaj? | Zadanie wisi — nikt nie odpowiada |
| **Akcja** | CO robi krok po kroku? | Ludzie mają narzędzia, nie wiedzą jak użyć |
| **Narzędzie** | CZYM? Prompt, szablon, checklista? | Każda sesja = improwizacja |
| **Produkt** | CO masz w ręku gdy skończysz? | Robią, robią, nie wiadomo kiedy koniec |

AANP nie mówi JAKIE procesy budować — mówi JAK SPRAWDZIĆ czy to co zbudowałeś jest kompletne. WAVE jest zbiorem otwartym procesów. AANP jest zamkniętym testem dla każdego z nich.

---

## 7. Profile Produktu — WAVE dla każdej skali

WAVE to jedna metodyka z trzema profilami intensywności — dopasowanymi do rodzaju budowanego rozwiązania. Filozofia ta sama, skala komponentów inna.

```
  DISCOVERY ──────────── BUILD ──────────── SCALE
  (POC/prototyp)          (MVP/pilot)        (Produkt)
  │                       │                  │
  │  Cel: zwalidować      │  Cel: dostarczyć │  Cel: skalować
  │  pomysł               │  wartość         │  i utrzymać
  │                       │                  │
  │  Przygotowanie:       │  Przygotowanie:  │  Przygotowanie:
  │  2-4h                 │  41-73h          │  163-385h
  │                       │                  │
  │  Proporcja P/E:       │  Proporcja P/E:  │  Proporcja P/E:
  │  ~60/40               │  ~70/30          │  50-70/30-50
  └───────────────────────┴──────────────────┘
```

| Wymiar | DISCOVERY (POC) | BUILD (MVP) | SCALE (Produkt) |
|---|---|---|---|
| **Cel** | Zwalidować pomysł | Dostarczyć wartość | Skalować i utrzymać |
| **Czas** | 1–5 dni | 4–8 tygodni | Miesiące → lata |
| **SCAN** | 3-5 kluczowych pytań | 6-8 obszarów | 10-15 z zależnościami |
| **PULSE** | 1 runda, 1-2 obszary | 2 rundy, 3-5 obszarów | 3 rundy, 8-15 obszarów |
| **Proporcja P/E** | ~60/40 | ~70/30 | 50-70 / 30-50 |
| **Rozbudowalność** | Do MVP bez przebudowy | Do produktu bez przebudowy | Do platformy enterprise |

Profile są ewolucyjne — Discovery przesuwa się do Build, Build do Scale. Kod, dokumentacja i decyzje rosną z tobą. Nie wyrzucasz niczego.

Pełny opis profili z rozkładem godzinowym, tabelami porównawczymi i drzewem decyzyjnym: **WAVE Profile Produktu** (dokument towarzyszący w repozytorium).

---

## 8. Co i jak mierzyć

Metodyka bez mierników to filozofia. WAVE definiuje konkretne wskaźniki jakości współpracy H-AI.

### Wskaźniki główne

| Wskaźnik | Definicja | Początek | Biegłość | Mistrzostwo |
|---|---|:---:|:---:|:---:|
| **PSR** (Prompt Success Rate) | % promptów z dobrym wynikiem za 1. razem | ~60% | >80% | >90% |
| **DPC** (Data Preparation Coverage) | % wiedzy ustrukturyzowanej w DataPrep | ~40% | >70% | >85% |
| **TFCO** (Time to First Correct Output) | Czas do pierwszego poprawnego wyniku | 2-4h | 30-60 min | 15-30 min |
| **RR** (Revision Rate) | Średnia liczba poprawek na zadanie | 3-5 | 1-2 | ~0 |

### Trajektoria samodoskonalenia

```
  PSR
  (sukces
  1. próby)
    │
 90%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · ·  mistrzostwo
    │                                      · · ·
 80%├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ · · · ·
    │                        · · ·                        biegłość
 70%├─ ─ ─ ─ ─ ─ ─ ─ · · · ·
    │            · · ·
 60%├─ ─ · · · ·                                          początek
    │  · ·
    │ ·
    ├──────────┬──────────┬──────────┬──────────▶ Tygodnie
    0          4          8          12
```

Poprawa nie wynika z tego, że AI staje się mądrzejsze. Wynika z tego, że Twój DataPrep się pogłębia, a szablony dojrzewają. Schemat jest stały niezależnie od branży.

---

## 9. WAVE poza oprogramowaniem — sześć kierunków

Trzy warstwy WAVE — uporządkowanie wiedzy dziedzinowej, precyzyjne zadanie dla AI, meta-sterowanie współpracą — nie zawierają niczego specyficznego dla żadnej branży. Opisują uniwersalny wzorzec współpracy człowiek-AI.

Poniżej sześć dziedzin, w których WAVE ma bezpośrednie zastosowanie. To są szkice, nie pełne wdrożenia — zaproszenia dla praktyków do testowania i informowania o wynikach.

| Dziedzina | DataPrep | Prompt2Data | Prompt2Prompt |
|---|---|---|---|
| **Farmacja** | Dane o cząsteczce, interakcje, wyniki prób | AI modeluje wiązania molekularne | Iteracyjne doprecyzowanie prognoz |
| **Medycyna** | Historia choroby, wyniki, kontekst genetyczny | AI analizuje wzorce diagnostyczne | Lekarz weryfikuje z osądem klinicznym |
| **Edukacja** | Wyniki uczniów, style uczenia, wzorce zachowań | AI proponuje ścieżki nauczania | Nauczyciel koryguje o dynamikę klasy |
| **Prawo** | Stan faktyczny, przepisy, orzecznictwo | AI analizuje precedensy, identyfikuje ryzyka | Prawnik weryfikuje strategię procesową |
| **NGO** | Dane o społeczności, dotychczasowe interwencje | AI identyfikuje wzorce skuteczności | Zespół koryguje o wiedzę terenową |
| **Inżynieria** | Specyfikacje, ograniczenia materiałowe, normy | AI generuje warianty projektowe | Inżynier weryfikuje z doświadczeniem |

### Wspólny wzorzec

W każdym przypadku schemat jest identyczny:

```
  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
  │                 │     │                 │     │                 │
  │  CZŁOWIEK       │     │  AI             │     │  CZŁOWIEK       │
  │  porządkuje     │────▶│  przetwarza     │────▶│  weryfikuje     │
  │  ekspertyzę     │     │  na skali       │     │  z osądem       │
  │                 │     │  niedostępnej   │     │  i decyduje     │
  │  (DataPrep)     │     │  (Prompt2Data)  │     │  (Prompt2Prompt)│
  │                 │     │                 │     │                 │
  └─────────────────┘     └─────────────────┘     └─────────────────┘
```

Różnica jest w treści — dane farmaceuty wyglądają inaczej niż dane prawnika. Ale struktura współpracy jest ta sama. Tak jak Lean wyszedł z fabryk Toyoty i trafił do szpitali — WAVE wyszła z wytwarzania oprogramowania, ale trzy warstwy mówią o ekspertyzie, nie o kodzie.

---

## 10. WAVE a istniejące podejścia

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
              │  Sprinty, backlog, standupy                 │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 2    ┌─────────────────────────────────────────────┐
  ZASADY      │  Lean / Kaizen                              │
              │  Eliminuj marnotrawstwo                     │
              └─────────────────────────────────────────────┘
                                    │
  PIĘTRO 1    ╔═════════════════════════════════════════════╗
  SESJA H-AI  ║  WAVE                                       ║
              ║  Jak współpracować z AI w konkretnej sesji  ║
              ╚═════════════════════════════════════════════╝
```

WAVE nie konkuruje z tradycyjnymi metodykami — działa na poziomie, którego żadna z nich nie pokrywa. Możesz prowadzić projekt w PRINCE2, organizować pracę w Scrumie, stosować Lean — i jednocześnie używać WAVE do każdej sesji z AI.

| Aspekt | Tradycyjne metodyki | WAVE | Relacja |
|---|---|---|---|
| Przygotowanie | Dokumentacja dla ludzi | Dokumentacja jako PALIWO dla AI | Wspólna wartość, inna motywacja |
| Iteracyjność | Scrum: sprinty | PULSE: 3 rundy per obszar | Wspólna zasada, inny rytm |
| Eliminacja marnotrawstwa | Lean: optymalizuj przepływ | Przygotowanie eliminuje przeróbki | Wspólny cel, inny mechanizm |
| **AI jako partner** | **Brak — nie istniało** | **Rdzeń metodyki** | **Unikalne dla WAVE** |
| **DooR** | **Brak odpowiednika** | **Standardy gotowości** | **Unikalne** |
| **Living Patterns** | **Brak odpowiednika** | **Żywa baza wiedzy** | **Unikalne** |

Najbliższy historyczny precedens pochodzi z przemysłu. **Lean** zaczął jako Toyota Production System, skupiony na produkcji samochodów. Z czasem jego zasady okazały się uniwersalne. WAVE odpowiada na fundamentalnie inny i pilniejszy problem: **jak człowiek powinien współpracować z AI, żeby AI go wzmacniało zamiast zastępować.**

---

## 11. Jak zacząć

### Ścieżka szybka — od dziś

Wybierz jedno zadanie, które regularnie wykonujesz z AI. Zanim zaczniesz następne podejście:

1. Zapisz wszystko, co wiesz o tym zadaniu — kontekst, ograniczenia, jak wygląda dobry wynik, jakich błędów unikać.
2. Uporządkuj to w prosty dokument: Wizja → Wymagania → Kontekst → Kryteria sukcesu.
3. Użyj tego dokumentu jako podstawy następnej interakcji z AI.

Obserwuj różnicę. Jeśli skuteczność pierwszej próby się poprawi — właśnie doświadczyłeś rdzenia WAVE.

### Ścieżka pełna — tydzień po tygodniu

| Tydzień | Co robisz | Efekt |
|:---:|---|---|
| 1 | DataPrep dla jednego zadania — zapisz kontekst, uporządkuj | PSR rośnie z ~60% do ~70% |
| 2 | Ustrukturyzowane prompty (7 elementów z Prompt2Data) | Mniej iteracji, lepsze wyniki |
| 3 | Szablony meta-promptów dla powtarzalnych typów zadań | Nowe zadania = wypełnianie pól, nie pisanie od zera |
| 4 | Uruchom SCAN dla swojego projektu | Mapa terenu — wiesz co zbadać |
| 5-6 | PULSE dla najważniejszych obszarów | Pierwsze Living Patterns |
| 7-8 | Mierz PSR, DPC, TFCO. Doskonal DataPrep i szablony | Metodyka zaczyna się samodoskonalić |

### Ścieżka zespołowa

W zespole DataPrep staje się wspólną bazą wiedzy, meta-prompty standardami zespołowymi, a mierniki miarami jakości współpracy. Living Patterns są referencjami, które każdy członek zespołu otwiera przed podjęciem decyzji w swoim obszarze. Decision Log jest kręgosłupem — nie w głowach trzech osób, lecz w jednym miejscu.

---

## 12. Najczęstsze pytania

**Czy WAVE działa tylko w wytwarzaniu oprogramowania?**

Nie. WAVE powstała w środowisku programistycznym i tam ma najgłębsze studium przypadku. Ale aksjomaty, trzy poziomy H-AI, DooR, AANP i Living Patterns nie zawierają niczego specyficznego dla żadnej branży. Rozdział 9 zarysowuje sześć dalszych dziedzin.

**Czy muszę być osobą techniczną?**

Nie. DataPrep polega na porządkowaniu Twojej ekspertyzy — jakiejkolwiek ekspertyzy. DataPrep nauczyciela wygląda inaczej niż inżyniera, ale zasada jest ta sama.

**Czym WAVE różni się od „pisania dobrych promptów"?**

Prompt engineering to technika — jak umiejętność posługiwania się młotkiem. WAVE to metodyka — jak plan budowy. Dobre prompty są częścią WAVE (Prompt2Data), ale osadzone w większym systemie przygotowania (DataPrep), meta-sterowania (Prompt2Prompt), standardów gotowości (DooR), testu kompletności (AANP) i profili produktu (Discovery/Build/Scale).

**Z jakimi narzędziami AI działa WAVE?**

WAVE jest niezależna od narzędzi. Działa z każdym AI przyjmującym ustrukturyzowane dane wejściowe — Claude, ChatGPT, Gemini, Copilot, modele dziedzinowe czy przyszłe narzędzia, które jeszcze nie istnieją.

**Jak szybko zobaczę wyniki?**

Większość praktyków zauważa poprawę skuteczności pierwszej próby już w pierwszym tygodniu zdyscyplinowanego DataPrep. Znacząca poprawa ogólnej efektywności pojawia się między czwartym a ósmym tygodniem, gdy szablony dojrzewają i pokrycie DataPrep się pogłębia.

**Czy WAVE może używać zespół?**

Tak. W zespole DataPrep staje się wspólną bazą wiedzy, meta-prompty standardami zespołowymi, Living Patterns referencjami decyzyjnymi, a mierniki miarami jakości współpracy. Zasady się skalują.

**Co nowego w v2.0 wobec v1.0?**

V2.0 dodaje: trójwarstwową architekturę (filozofia → komponenty → praktyki), DooR (standardy gotowości), Living Patterns (SCAN, PULSE — narzędzia do budowania wiedzy), FALA (procedura od koncepcji do realizacji), AANP (test kompletności procesów), Profile Produktu (Discovery/Build/Scale), grawitacyjną interpretację zasady 70/30, Szybki Start. V1.0 pozostaje dostępny w repozytorium jako punkt wejścia.

**Czy WAVE jest darmowa?**

Tak. CC BY-SA 4.0 — możesz używać, adaptować, uczyć i rozbudowywać, pod warunkiem przypisania autorstwa i udostępnienia adaptacji na tej samej licencji.

---

## 13. Geneza

WAVE powstała 17 stycznia 2026 roku, podczas sesji roboczej Przemysława Zielińskiego z Claude (Anthropic). Zieliński — współzałożyciel i CEO IDareU, platformy gamifikowanego uczenia się opartej na wyzwaniach wideo z mentoringiem — potrzebował ustrukturyzowanego podejścia do budowy złożonej aplikacji webowej ze wsparciem AI.

Trójwarstwowa struktura — DataPrep, Prompt2Data, Prompt2Prompt — wyłoniła się z praktycznej konieczności: odkrycia, że większość wartości we współpracy z AI pochodzi z tego, co człowiek przygotuje ZANIM AI zostanie zaangażowane.

W lutym 2026 WAVE została opublikowana jako open-source (v1.0) z generycznym pozycjonowaniem od pierwszego dnia — ucząc się na kosztownym błędzie Lean, który zaczął z etykietą „Manufacturing" i dekadami się z niej wyzwalał.

Między lutym a marcem 2026, w praktyce budowania IDareU Gen2, wyłoniły się koncepty które fundamentalnie rozszerzyły architekturę WAVE: DooR (standardy gotowości), Living Patterns (ekosystem żywej wiedzy z narzędziami SCAN i PULSE), FALA (pipeline od koncepcji do kodu), RtS (11 warstw specyfikacji technicznej), AANP (test kompletności procesów), Profile Produktu (Discovery/Build/Scale). V2.0 to efekt tej ewolucji — z luźnej kolekcji zasad do ustrukturyzowanej metodyki z trzema warstwami architektury.

Polska nazwa FALA — **Formuła Amplifikacji Ludzkiej Aktywności** — stawia człowieka w centrum już w samej nazwie: to ludzka aktywność jest wzmacniana, nie zastępowana.

W marcu 2026 metoda WAVE Living Patterns przeszła test powtarzalności — dwie niezależne sesje doszły do tych samych fundamentów z różnymi profilami. Z testu wyłonił się Cross-Session Merge jako nowy wariant auto-doskonalenia, a półautomatyczny pipeline na GitHub Actions potwierdził skalowalność podejścia — koszt jednego Living Pattern spadł poniżej dolara, z bramkami zatwierdzenia między każdym krokiem.

Tego samego miesiąca, z nocnej sesji nad pipeline'em Living Patterns, wyłonił się meta-aksjomat **Prądy i Napięcia** — obserwacja że każda sesja współpracy człowiek-AI rozgrywa się na polu rywalizujących atrybutów, a emergencja rodzi się na ich przecięciu. Cofnięcie czterech iteracji naprawy tabeli na rzecz prostoty i zapasu pojemności okazało się momentem, w którym z nawigacji napięcia wyłoniło się odkrycie warte więcej niż poprawiona tabela. Carl Benedikt Frey z Oxfordu potwierdził tę obserwację na skali tysiąca lat historii: postęp umiera gdy systemy zamrażają się w jednym trybie zamiast nawigować napięcia.

---

## 14. Cytowanie i licencja

### Licencja

WAVE jest opublikowana na licencji **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

### Cytowanie

```
Zieliński, P. (2026). WAVE: Workflow Amplification via Vectored Expertise — 
Metodyka współpracy człowiek-AI (v2.0). 
https://github.com/przemek-zielinski/WAVE-Methodology
```

### Współtworzenie

WAVE to wersja 2.0 — urodzona w wytwarzaniu oprogramowania, zaprojektowana dla każdej dziedziny. Rośnie dzięki praktykom, którzy ją testują, łamią i udoskonalają.

Studia przypadków, szablony, tłumaczenia, krytyka — zobacz [CONTRIBUTING.md](../CONTRIBUTING.md).

Szukamy **współprowadzących (co-maintainers)**, którzy są pasjonatami współpracy człowiek-AI i chcą pomóc tej metodyce osiągnąć jej potencjał.

---

*Metodyka WAVE / FALA v2.0 — Opublikowana w marcu 2026*  
*Stworzona przez Przemysława Zielińskiego z Claude (Anthropic)*  
*„Człowiek prowadzi. AI wzmacnia."*
