# WAVE FALA — Procedura RtS: Od dokumentu koncepcyjnego do gotowego kodu
## Trzy sesje, trzy prompty, powtarzalny pipeline dla każdego modułu

**Element metodyki WAVE** | **Wersja:** 1.0 | **Data:** 1 marca 2026  
**Charakter:** Proceduralny — opisuje JAK używać RtS w praktyce

---

## Czym jest ten dokument

Ten dokument opisuje **powtarzalną procedurę** przekształcania dokumentacji koncepcyjnej modułu (Common Wise, dokumenty Core 01–11, Decision Log) w działający kod. Procedura składa się z trzech sesji, każda z jasnym promptem, załącznikami i outputem.

```
  DOKUMENTY KONCEPCYJNE              RtS + SZABLON
  (to co mamy — pitchowe,           (generyczne, raz napisane,
   biznesowe, strategiczne)           wielokrotnie użyte)
        │                                   │
        └──────────────┬────────────────────┘
                       ▼
              ┌─────────────────┐
              │  SESJA 1: AUDYT │  → Gap Map + pytania
              └────────┬────────┘
                       │ Właściciel produktu odpowiada
                       ▼
              ┌─────────────────┐
              │ SESJA 2: BLUEPRINT │  → wypełniony blueprint
              └────────┬────────┘
                       │ Autotest 3 pytań RtS
                       ▼
              ┌─────────────────┐
              │  SESJA 3: KOD   │  → działający moduł
              └────────┬────────┘
                       │
                       ▼
                    ✅ DoD
```

**Zasada nadrzędna:** Każda sesja produkuje artefakt, który jest wejściem do następnej. Nie przeskakuj sesji. Sesja 3 bez Sesji 2 = AI zgaduje. Sesja 2 bez Sesji 1 = blueprint z lukami.

---

## Ekosystem dokumentów WAVE FALA

Cztery dokumenty — dwa generyczne (raz napisane), dwa produkowane per moduł:

| # | Dokument | Typ | Rola |
|:---:|---|---|---|
| 01 | **Procedura RtS** *(ten dokument)* | Generyczny | JAK przeprowadzić pipeline |
| 02 | **RtS Blueprint Walidacja** | Generyczny | CO musi być w blueprincie (11 warstw) |
| 03 | **Szablon Blueprint** | Generyczny | GDZIE to wpisać (puste pola do wypełnienia) |
| — | `[NN]_Audyt_RtS_[MODUŁ].md` | Per moduł | Wynik Sesji 1: Gap Map + graf + głębokość |
| — | `[NN]_Blueprint_[MODUŁ]_Faza[N].md` | Per moduł | Wynik Sesji 2: gotowy do kodowania |

```
  01 Procedura        → mówi KTO robi CO W JAKIEJ KOLEJNOŚCI
  02 RtS Walidacja    → mówi CO musi być i DLACZEGO (definicje, przykłady)
  03 Szablon          → mówi GDZIE to wpisać (puste tabele, [UZUPEŁNIJ])
```

---

## Przed startem — co muszę mieć

### Dokumenty generyczne (raz na projekt)

```
  □ 01_WAVE_FALA_RtS_Procedura_Kodowania_v1.md     ← ten dokument
  □ 02_WAVE_FALA_RtS_Blueprint_Walidacja_v3.md      ← definicja 11 warstw
  □ 03_WAVE_FALA_RtS_Szablon_Blueprint_v1.md         ← pusty szablon
```

### Dokumenty per moduł (zbierasz przed Sesją 1)

```
  □ Dokumenty koncepcyjne modułu
    — Common Wise (jeśli istnieje — np. 01_IDareU_HIVE_Common_Wise_v3.md)
    — Dokument z serii Core (np. 10_IDareU_HIVE_v3_revised.md)
    — Powiązane dokumenty Core (np. 11_Challange_Logic, 07_AI_Feature)
  □ Decision Log (IDareU_Decision_Log.md)
  □ Blueprinty zależnych modułów (jeśli istnieją)
  □ Próbka kodu z istniejącego modułu (jeśli istnieje — kontroler, serwis, model)
```

---

## SESJA 1: AUDYT RtS

### Cel

Zmierzyć dystans między dokumentacją koncepcyjną a tym co potrzebne do kodowania. Wyprodukować mapę luk z konkretnymi pytaniami do właściciela produktu.

### Kiedy

Przed rozpoczęciem pracy nad blueprintem modułu. Sesja 1 to pierwszy krok po decyzji „następny implementujemy moduł X".

### Kto

Właściciel produktu + AI (Claude w projekcie IDareU).

### Czas

~1–2 godziny. Prosty moduł (3–4 endpointy, bez AI) → 1h. Złożony moduł (HIVE, grupy treningowe) → 2h.

### Prompt

```
Przeprowadź audyt RtS dla modułu [NAZWA MODUŁU] w fazie [FAZA].

W załączeniu:
1. Dokument RtS: 02_WAVE_FALA_RtS_Blueprint_Walidacja_v3.md
2. Dokumenty koncepcyjne modułu: [LISTA PLIKÓW]
3. Decision Log: IDareU_Decision_Log.md
4. [opcjonalnie] Blueprinty zależnych modułów: [LISTA PLIKÓW]

Wyprodukuj trzy rzeczy:

A. GAP MAP — dla każdej z 11 warstw RtS:
   ✅ Zdefiniowane (jest precyzyjnie, gotowe do blueprintu)
   ⚠️ Do doprecyzowania (jest koncepcyjnie, brakuje detali — wymień JAKICH)
   ❌ Brakuje (nie istnieje w żadnej formie)
   Dla każdego ⚠️ i ❌ napisz KONKRETNE pytanie do mnie — nie "uzupełnij
   Warstwę 3" ale "jaki timeout dla LLM API? 5s? 10s? ile retry?"

B. GRAF ZALEŻNOŚCI — które moduły muszą mieć ustalony interfejs
   PRZED [NAZWA MODUŁU]:
   ● Gotowy (kod istnieje)
   ◐ Interfejs ustalony (kontrakt API zdefiniowany, kod nie napisany)
   ○ Nie ustalony (trzeba zdefiniować)
   Dla każdego ○ napisz CO DOKŁADNIE trzeba ustalić.

C. WSKAŹNIK GŁĘBOKOŚCI — dla fazy [FAZA], która warstwa:
   PEŁNA / CZĘŚCIOWA / PODSTAWOWA
   Z uzasadnieniem dlaczego nie pełna (jeśli dotyczy).

Nie zgaduj odpowiedzi na pytania merytoryczne — jeśli nie wiesz, wpisz
pytanie do mnie. Twój output to mapa luk i pytania, nie wypełniony blueprint.

Format outputu: plik Markdown o nazwie [NN]_Audyt_RtS_[MODUŁ].md
```

### Załączniki

| # | Plik | Wymagany? |
|:---:|---|:---:|
| 1 | `02_WAVE_FALA_RtS_Blueprint_Walidacja_v3.md` | ✅ Zawsze |
| 2 | Dokumenty koncepcyjne modułu | ✅ Zawsze |
| 3 | `IDareU_Decision_Log.md` | ✅ Zawsze |
| 4 | Blueprinty zależnych modułów | Jeśli istnieją |

### Output

Plik: `[NN]_Audyt_RtS_[MODUŁ].md`

Zawiera:
- Gap Map (11 wierszy — warstwa po warstwie)
- Lista pytań do właściciela produktu (pogrupowana per warstwa)
- Graf zależności z oznaczeniami ● / ◐ / ○
- Wskaźnik głębokości per warstwa per faza

### Co dalej

Właściciel produktu przegląda pytania z Gap Map i odpowiada. Odpowiedzi mogą padać w tej samej konwersacji (AI dopisuje do audytu) lub w osobnym dokumencie. Gdy wszystkie pytania mają odpowiedzi → przejście do Sesji 2.

**Kryterium przejścia do Sesji 2:** Każde ⚠️ z Gap Map stało się ✅ (odpowiedź uzyskana) lub świadomie oznaczone jako placeholder (z jawną notatką „uzupełnić przed Fazą [N]").


---

## SESJA 2: WYPEŁNIENIE BLUEPRINTU

### Cel

Wypełnić szablon blueprintu technicznego na podstawie odpowiedzi z Sesji 1. Wyprodukować kompletny dokument gotowy do przekazania Claude Code.

### Kiedy

Po zakończeniu Sesji 1 — gdy wszystkie pytania z Gap Map mają odpowiedzi lub świadome placeholdery.

### Kto

Właściciel produktu + AI (Claude w projekcie IDareU). Sesja jest interaktywna — AI wypełnia, właściciel weryfikuje i podejmuje decyzje na bieżąco.

### Czas

~2–5 godzin. Prosty moduł → 2h. Złożony (HIVE, grupy treningowe) → 4–5h. Czas zależy głównie od ilości decyzji do podjęcia w trakcie.

### Prompt

```
Wypełnij blueprint techniczny dla modułu [NAZWA MODUŁU] w fazie [FAZA].

W załączeniu:
1. Szablon: 03_WAVE_FALA_RtS_Szablon_Blueprint_v1.md
2. Audyt RtS z Sesji 1: [NN]_Audyt_RtS_[MODUŁ].md
   (zawiera Gap Map z odpowiedziami, graf zależności, wskaźnik głębokości)
3. Dokumenty koncepcyjne modułu: [LISTA PLIKÓW]
4. Decision Log: IDareU_Decision_Log.md
5. [opcjonalnie] Blueprint zależnego modułu (jako referencja interfejsów)
6. [opcjonalnie] Próbka kodu z istniejącego modułu (dla Warstwy 8)

Wypełnij każdą warstwę szablonu w głębokości ustalonej wskaźnikiem:
  PEŁNA     = każdy element checklisty odhaczony, zero [UZUPEŁNIJ]
  CZĘŚCIOWA = elementy aktywne w tej fazie wypełnione,
              reszta jawnie oznaczona „PLACEHOLDER — Faza [N]"
  PODSTAWOWA = minimum funkcjonalne wypełnione,
               reszta jawnie oznaczona „PLACEHOLDER — Faza [N]"

Zasady:
— Nie zgaduj wartości merytorycznych — pytaj mnie
— Nie pomijaj pól — wypełnij lub oznacz jako placeholder
— Reguły biznesowe wpisuj PRZY endpoincie, nie w osobnej sekcji
— Edge case'y wpisuj PRZY algorytmie, nie w osobnej sekcji
— Po wypełnieniu przeprowadź AUTOTEST trzema pytaniami RtS

Format outputu: plik Markdown o nazwie [NN]_Blueprint_[MODUŁ]_Faza[N].md
```

### Załączniki

| # | Plik | Wymagany? |
|:---:|---|:---:|
| 1 | `03_WAVE_FALA_RtS_Szablon_Blueprint_v1.md` | ✅ Zawsze |
| 2 | Audyt RtS z Sesji 1 | ✅ Zawsze |
| 3 | Dokumenty koncepcyjne modułu | ✅ Zawsze |
| 4 | `IDareU_Decision_Log.md` | ✅ Zawsze |
| 5 | Blueprint zależnego modułu | Jeśli istnieje |
| 6 | Próbka kodu | Jeśli istnieje |

### Output

Plik: `[NN]_Blueprint_[MODUŁ]_Faza[N].md`

Zawiera:
- 11 warstw wypełnionych w ustalonej głębokości
- Raport autotestu (trzy pytania RtS z odpowiedziami PASS / FAIL)
- Lista placeholderów z przypisaniem do przyszłej fazy (jeśli są)

### Autotest — trzy pytania RtS

AI po wypełnieniu blueprintu sam sobie zadaje trzy pytania:

```
PYTANIE 1 — DANE:
  Wybieram losowe pole z losowej tabeli.
  Czy wiem: typ? ograniczenie? kto zapisuje? kto czyta?
  jak wyświetlane? co gdy NULL?
  → PASS / FAIL (jeśli FAIL: wskaż brakujący element)

PYTANIE 2 — AWARIA:
  Wybieram losową zależność zewnętrzną.
  Czy wiem: co gdy timeout? co widzi użytkownik?
  co w logach? kiedy alert?
  → PASS / FAIL (jeśli FAIL: wskaż brakujący element)

PYTANIE 3 — BEZPIECZEŃSTWO:
  Wybieram losowy parametr wejściowy.
  Czy wiem: jak walidowany? co gdy spoza zakresu?
  co gdy podwójny request?
  → PASS / FAIL (jeśli FAIL: wskaż brakujący element)
```

**Kryterium przejścia do Sesji 3:** Trzy PASS. Jeśli choćby jeden FAIL → wróć do warstwy z luką, uzupełnij, powtórz autotest.

---

## SESJA 3: KODOWANIE

### Cel

Zaimplementować moduł w Claude Code na podstawie kompletnego blueprintu. Kod pisany strumieniowo, bez zatrzymywania się na pytania — bo blueprint odpowiada na wszystkie.

### Kiedy

Po zakończeniu Sesji 2 z trzema PASS w autoteście.

### Kto

Właściciel produktu + Claude Code. Rola właściciela: nadzór, review, decyzje w sytuacjach nieoczekiwanych (nie powinno ich być przy dobrym blueprincie).

### Czas

~15–25 godzin dla złożonego modułu. ~5–10 godzin dla prostego. Czas zależy od objętości kodu, nie od ilości decyzji — decyzje zostały podjęte w Sesjach 1–2.

### Prompt

```
Zaimplementuj moduł [NAZWA MODUŁU] zgodnie z poniższym blueprintem.

Każdy element jest zdefiniowany precyzyjnie — nie zgaduj, nie dodawaj,
nie upraszczaj. Jeśli coś jest niejasne — ZATRZYMAJ SIĘ i zapytaj
zamiast domyślać się.

Kolejność implementacji:
  1. Modele i migracje bazy danych              (Warstwa 1)
  2. Middleware walidacji i bezpieczeństwa        (Warstwa 9)
  3. Serwis z logiką biznesową                   (Warstwa 3 + 4)
  4. Obsługa błędów i circuit breaker            (Warstwa 10)
  5. Endpointy API                               (Warstwa 2)
  6. Logowanie i metryki                         (Warstwa 11)
  7. Crony i eventy                              (Warstwa 4)
  8. Komponenty frontendowe                      (Warstwa 6)
  9. Seeds i testy                               (Warstwa 7)
  10. Integracja z resztą systemu                (Warstwa 5)

Po każdym kroku:
  — Uruchom testy z blueprintu zanim przejdziesz dalej
  — Jeśli test nie przechodzi — napraw zanim kontynuujesz
  — Loguj postęp: "KROK [N] DONE — testy: [X/Y passed]"
```

### Załączniki

| # | Plik | Wymagany? |
|:---:|---|:---:|
| 1 | `[NN]_Blueprint_[MODUŁ]_Faza[N].md` | ✅ Zawsze — JEDEN PLIK |
| 2 | Próbka kodu z istniejącego modułu | ✅ Jeśli nie pierwszy moduł |

**Ważne:** Blueprint to JEDEN plik. Nie jedenaście dokumentów. AI pracuje najlepiej gdy cały kontekst jest w jednym oknie. Blueprint modułu — wszystkie warstwy w głębokości ustalonej w Sesji 1 — mieści się w kontekście Claude Code (~20–30 stron).

### Output

- Kod modułu (pliki źródłowe w strukturze z Warstwy 8 blueprintu)
- Wyniki testów jednostkowych
- Wyniki testów E2E
- Log postępu (10 kroków z wynikami)

### Weryfikacja — DoD

Po Sesji 3 weryfikacja przez Definition of Done:

```
  ✅ Migracje wykonane — baza ma tabele z blueprintu
  ✅ Endpointy odpowiadają — każdy zwraca oczekiwany format
  ✅ Testy jednostkowe przechodzą — min. 5 per algorytm
  ✅ Testy E2E przechodzą — min. 2 per główny flow
  ✅ Flagi przełączalne — admin panel zmienia flagi, efekt natychmiastowy
  ✅ Bezpieczeństwo — walidacja, sanityzacja, autoryzacja per rola
  ✅ Odporność — scenariusze awarii działają (timeout → fallback)
  ✅ Logi i metryki — format JSON, metryki zbierane
  ✅ Konwencje — kod zgodny z próbką, nazewnictwo spójne
  ✅ Integracja — moduł podłączony do istniejących ekranów
```

Wszystkie ✅ → moduł gotowy.
Choćby jedno ❌ → napraw, powtórz test, aż DoD spełnione.

---

## Podsumowanie — pełny pipeline

```
  WEJŚCIE                           SESJA                         WYJŚCIE
  ───────────────────────────────────────────────────────────────────────

  Dokumenty koncepcyjne        ┌─────────────┐
  + RtS Walidacja (02)    ───► │ SESJA 1     │ ───► Audyt RtS
  + Decision Log               │ AUDYT       │      (Gap Map + graf
                               └─────────────┘       + głębokość + pytania)
                                      │
                    Właściciel odpowiada na pytania
                                      │
  Audyt RtS + odpowiedzi        ┌─────────────┐
  + Szablon (03)           ───► │ SESJA 2     │ ───► Blueprint modułu
  + Decision Log                │ BLUEPRINT   │      (11 warstw wypełnionych
                                └─────────────┘       + autotest 3×PASS)
                                      │
                        Autotest: 3 pytania RtS
                                      │
  Blueprint modułu              ┌─────────────┐
  + Próbka kodu            ───► │ SESJA 3     │ ───► Kod + testy
                                │ KODOWANIE   │      (10 kroków + DoD)
                                └─────────────┘
```

### Ile razy to powtarzam?

Raz na moduł, raz na fazę. Jeśli moduł HIVE ma Fazę 0 i Fazę 1 — pipeline przechodzisz dwa razy, ale druga iteracja jest szybsza bo:
- Gap Map z Fazy 0 jest punktem wyjścia (większość warstw już ✅)
- Blueprint z Fazy 0 jest rozszerzany, nie pisany od zera
- Kod z Fazy 0 jest próbką kodu dla Fazy 1

### Co jeśli w Sesji 3 AI się zatrzymuje?

Znaczy RtS nie był spełniony — wróć do Sesji 2, uzupełnij blueprint w miejscu gdzie AI miało pytanie, i kontynuuj. Nie naprawiaj w locie w Sesji 3 — decyzje architektoniczne podjęte pod presją kodu są gorsze niż podjęte w spokoju blueprintu.

---

*01_WAVE_FALA_RtS_Procedura_Kodowania. Element metodyki WAVE. Definiuje trzy sesje transformujące dokumentację koncepcyjną w działający kod. Generyczny — działa dla dowolnego modułu IDareU Gen2. Powtarzalny — raz na moduł, raz na fazę.*
