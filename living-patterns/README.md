# WAVE Living Patterns

## Narzędzie do systematycznego budowania żywych wzorców wiedzy z pomocą AI

---

### Zacznij tutaj — trzy kroki

**Krok 1: SCAN** — podaj opis swojego rozwiązania, dostaniesz listę wszystkich obszarów do zbadania.  
→ [SCAN-Prompt_v3.md](SCAN-Prompt_v3.md) | [Instrukcja użycia](SCAN-HowTo_v3.md)

**Krok 2: PULSE** — dla każdego obszaru uruchom trzy rundy badawcze. AI buduje, weryfikuje z innego kąta, szuka w peryferyjnych kierunkach.  
→ [PULSE-Prompt_v3.md](PULSE-Prompt_v3.md) | [Instrukcja użycia](PULSE-HowTo_v3.md)

**Krok 3: Living Pattern** — efektem jest żywy dokument z zasadami, standardami, matrycą błędów i metrykami. Cyklicznie sprawdza swoją aktualność.  
→ [Pierwszy oficjalny wzorzec: UX/UI](patterns/official/LP_UX_UI_v3.md)

**Czego potrzebujesz:** AI z wyszukiwaniem internetowym (Claude, ChatGPT, Gemini). Opis swojego rozwiązania. Opcjonalnie: materiały wewnętrzne projektu.

---

### Czym jest Living Pattern

Living Pattern to żywy dokument zawierający najlepszą dostępną wiedzę — naukową, branżową i praktyczną — dla jednego obszaru implementacyjnego. Nie jest podręcznikiem który leży na półce. Jest narzędziem decyzyjnym które regularnie sprawdza swoją aktualność.

Projektant otwiera Living Pattern UX/UI przed rysowaniem ekranów. Programista otwiera Living Pattern Database przed projektowaniem schematów. Prawnik otwiera Living Pattern Compliance przed pisaniem polityk.

### Jak to działa

```
SCAN                          PULSE (×3 rundy)              Living Pattern
identyfikuje obszary    →     buduje wiedzę            →    żywy dokument
+ funkcje celu                z trzech kątów ataku          + auto-doskonalenie
+ parametry do PULSE          (budowa → optymalizacja       w ustalonym rytmie
                               → finalizacja)
```

Trzy rundy PULSE pokrywają ~97% dostępnej wiedzy. Mechanizm malejących przyrostów: Runda 1 daje ~60% wartości, Runda 2 ~25%, Runda 3 ~12%. Punkt nasycenia — nie nieskończoność.

### Dla kogo

**Początkujący z AI** — gotowy przepływ pracy zamiast chaotycznych pytań. Przewidywalna struktura i jakość wyników.

**Zaawansowani bez modelu** — powtarzalny proces, wspólny język w zespole, wiedza która się nie starzeje w szufladzie.

**Zespoły** — wspólna mapa obszarów (SCAN), ten sam format dokumentów (Living Pattern), widoczny progres, nowy członek czyta wzorzec zamiast pytać „dlaczego wybraliśmy X."

### Pełna dokumentacja

→ [Ecosystem — kompletny opis ekosystemu, filozofia, cykl życia, auto-doskonalenie, model open source](Ecosystem_v3.md)

### Gotowe wzorce

| Wzorzec                                            | Obszar                                  | Status          |
| -------------------------------------------------- | --------------------------------------- | --------------- |
| [LP_UX_UI_v3.md](patterns/official/LP_UX_UI_v3.md) | UX/UI i User Journey                    | Oficjalny       |
| *LP_Database*                                      | Baza danych i model danych              | W przygotowaniu |
| *LP_Security*                                      | Bezpieczeństwo                          | W przygotowaniu |
| *Twój wzorzec?*                                    | → [CONTRIBUTING.md](../CONTRIBUTING.md) | Społecznościowy |

---

### Relacja z WAVE

Living Patterns to **narzędzie** z metodyki [WAVE](../README.md) (Workflow Amplification via Vectored Expertise). Możesz używać Living Patterns samodzielnie — ale jeśli chcesz poznać pełną metodykę współpracy człowiek-AI, zacznij od [rdzenia WAVE](../docs/).

---

*Licencja: CC BY-SA 4.0 | Autor koncepcji: Przemek Zieliński | Opracowanie: Claude (Anthropic)*
