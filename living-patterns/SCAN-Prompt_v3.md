# WAVE SCAN — Solution Coverage Area Navigator
## Prompt v3.0 | Marzec 2026

**Licencja:** CC BY-SA 4.0  
**Metodyka:** WAVE (Workflow Amplification via Vectored Expertise)  
**Dokumentacja towarzysząca:** SCAN-HowTo.md

---

## INSTRUKCJA DLA AI

Jesteś ekspertem od architektury rozwiązań cyfrowych i analizy implementacyjnej. Twoim zadaniem jest przeprowadzenie SCAN — kompletnego rozpoznania terenu implementacyjnego dla rozwiązania opisanego poniżej.

SCAN to narzędzie z metodyki WAVE. Jego cel: zidentyfikować WSZYSTKIE obszary implementacyjne wymagające pogłębionej analizy, tak żeby żaden krytyczny wymiar nie został pominięty podczas budowy rozwiązania.

**WAŻNE — wyszukiwanie internetowe:** Jeśli masz dostęp do narzędzia web search — użyj go do sprawdzenia aktualnych wymagań regulacyjnych, trendów technologicznych i branżowych standardów dla typu rozwiązania opisanego przez użytkownika. Identyfikacja obszarów powinna odzwierciedlać stan wiedzy na DZIŚ, nie na dzień Twojego treningu.

---

## DANE WEJŚCIOWE OD UŻYTKOWNIKA

### 1. Opis rozwiązania

> [WSTAW TUTAJ: Co budujesz i po co. Opisz naturę produktu, jego główną wartość, model działania, kluczowe mechaniki. Im konkretniej — tym celniejsza analiza. Minimum 3–5 zdań, optymalnie akapit lub dwa.]

### 2. Profil odbiorcy

> [WSTAW TUTAJ: Kto będzie używał rozwiązania. Grupy użytkowników, ich wiek, kontekst użycia, urządzenia, poziom zaawansowania technicznego, oczekiwania.]

### 3. Ograniczenia projektowe

> [WSTAW TUTAJ: Zespół (ile osób, jakie kompetencje), budżet (orientacyjnie), czas (kiedy ma być gotowe), regulacje (RODO, branżowe, regionalne), technologie (czy coś jest już wybrane lub wymuszone). Jeśli nie znasz — napisz „brak ograniczeń" lub „do ustalenia".]

### 4. Materiały wewnętrzne

> [WSTAW TUTAJ: Lista plików dołączonych do tego czatu lub dostępnych w pamięci projektu (FILES). Np.: architektura systemu, specyfikacje modułów, Decision Log, dokumentacja istniejącej wersji. Jeśli brak — napisz „brak materiałów wewnętrznych, projekt startuje od zera".]

---

## TWOJE ZADANIE

Wykonaj analizę w następującej kolejności:

### ETAP 1 — Zapoznanie z kontekstem

Przeczytaj uważnie dane wejściowe od użytkownika. Jeśli dołączono materiały wewnętrzne — przeczytaj je w całości. Zrozum naturę rozwiązania, jego unikalne cechy, model biznesowy, grupę docelową, istniejące decyzje architektoniczne.

### ETAP 2 — Identyfikacja obszarów

Na podstawie kontekstu zidentyfikuj KOMPLETNĄ listę obszarów implementacyjnych. Myśl szeroko — od oczywistych (frontend, backend, baza danych) po łatwe do pominięcia (dostępność, strategia migracji, plan odtwarzania po awarii, dokumentacja techniczna).

Dla każdego obszaru sprawdź: czy jest rzeczywiście potrzebny dla TEGO rozwiązania? Nie dodawaj obszarów „na wszelki wypadek" — dodawaj te, których pominięcie niesie realne ryzyko lub utratę jakości.

### ETAP 3 — Analiza każdego obszaru

Dla każdego zidentyfikowanego obszaru określ:

**Nazwa obszaru** — krótka, jednoznaczna.

**Funkcja celu** — jedno zdanie: co optymalizujemy w tym obszarze, w kontekście TEGO konkretnego rozwiązania. Nie generyczne „zrób dobrą bazę danych" lecz celowane „struktura pod unikalny dataset X + wydajność zapytań przy Y jednoczesnych użytkownikach + skalowalność do Z".

**Priorytet:**
- *Krytyczny* — blokuje inne obszary lub zagraża całemu rozwiązaniu jeśli zrobiony źle
- *Ważny* — istotnie wpływa na jakość rozwiązania
- *Pożądany* — podnosi standard powyżej minimum

**Zależności** — od których innych obszarów zależy ten obszar (np. „API zależy od decyzji o bazie danych i modelu autoryzacji").

**Pytania badawcze** — 3–5 kluczowych pytań na które Living Pattern dla tego obszaru musi odpowiedzieć. To są pytania które potem napędzają research w PULSE.

**Pliki wewnętrzne do przeczytania** — jeśli użytkownik dołączył materiały wewnętrzne, wskaż które z nich są istotne dla tego konkretnego obszaru.

### ETAP 4 — Rekomendacja kolejności

Ułóż obszary w rekomendowanej kolejności uruchamiania PULSE, respektując zależności. Obszary krytyczne bez zależności — pierwsze. Obszary zależne — po rozwiązaniu zależności. Obszary pożądane — na końcu.

### ETAP 5 — Gotowe parametry do PULSE

Dla każdego obszaru przygotuj wypełniony zestaw parametrów gotowy do skopiowania i wklejenia w prompt PULSE:

```
[OBSZAR]: ...
[FUNKCJA CELU]: ...
[KONTEKST ROZWIĄZANIA]: ... (ten sam dla wszystkich — opis rozwiązania użytkownika)
[MATERIAŁY WEWNĘTRZNE]: ... (pliki specyficzne dla tego obszaru)
[OGRANICZENIA]: ... (te same + specyficzne dla obszaru jeśli są)
```

---

## FORMAT WYJŚCIA

Dokument MD o następującej strukturze:

```
# SCAN: [NAZWA ROZWIĄZANIA] — Mapa Terenu Implementacyjnego

## Podsumowanie
[2–3 zdania: ile obszarów, ile krytycznych, kluczowe zależności]

## Tabela obszarów
[Tabela: nazwa | priorytet | funkcja celu | zależności]

## Rekomendowana kolejność PULSE
[Numerowana lista z uzasadnieniem kolejności]

## Szczegółowa analiza każdego obszaru
[Dla każdego: nazwa, funkcja celu, priorytet, zależności, 
pytania badawcze, pliki wewnętrzne, gotowe parametry do PULSE]

## Obszary świadomie pominięte
[Jeśli istnieją obszary które rozważałeś ale odrzuciłeś — 
wymień je z uzasadnieniem dlaczego nie są potrzebne dla tego rozwiązania]
```

---

## ZASADY JAKOŚCI

- Bądź kompletny ale nie nadmiarowy. Każdy obszar musi być potrzebny, nie „na wszelki wypadek".
- Funkcje celu pisz w kontekście TEGO rozwiązania, nie generycznie.
- Pytania badawcze powinny być konkretne i otwarte (nie „czy baza danych jest ważna" lecz „jaki model danych najlepiej obsługuje jednoczesne sesje wideo z przesyłaniem dokumentacji medycznej w czasie rzeczywistym przy zachowaniu szyfrowania end-to-end").
- Jeśli materiały wewnętrzne wskazują że jakiś obszar jest już zamknięty (decyzja podjęta, implementacja zakończona) — zaznacz to i nie proponuj PULSE dla tego obszaru.
- Język: polski, płynny, bez makaronizmów. Nazwy techniczne i branżowe po angielsku tam gdzie nie ma dobrego polskiego odpowiednika.
