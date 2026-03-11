# WAVE SCAN — Instrukcja Użycia (How-To)
## Wersja 3.0 | Marzec 2026

**Dotyczy:** SCAN-Prompt.md v3.0  
**Licencja:** CC BY-SA 4.0  
**Metodyka:** WAVE (Workflow Amplification via Vectored Expertise)

---

## 1. Cel użycia SCAN

SCAN odpowiada na pytanie: **„Jakie obszary implementacyjne muszę zbadać, zanim zacznę budować?"**

Większość zespołów wchodzi w implementację z listą obszarów opartą na doświadczeniu — „potrzebujemy bazę, frontend, backend, deploy." To pokrywa oczywiste, ale pomija subtelne: dostępność, strategia testowania, plan odtwarzania po awarii, model danych pod przyszłe wykorzystanie AI, zgodność z regulacjami.

SCAN skanuje teren implementacyjny z perspektywy całości rozwiązania i identyfikuje pełną mapę — łącznie z obszarami które zespół mógłby przeoczyć. Dla każdego obszaru SCAN dostarcza gotowe parametry do uruchomienia PULSE (promptu budującego Living Pattern).

**SCAN nie buduje wiedzy.** SCAN mówi GDZIE szukać. Wiedzę buduje PULSE.

---

## 2. Logika budowy promptu

Prompt SCAN składa się z czterech warstw:

**Warstwa kontekstowa** — instrukcja dla AI definiująca rolę (ekspert od architektury rozwiązań) i naturę zadania (kompletne rozpoznanie terenu).

**Warstwa danych wejściowych** — cztery pola parametryzowane przez użytkownika: opis rozwiązania, profil odbiorcy, ograniczenia projektowe, materiały wewnętrzne. Te dane dają AI kontekst do celowanej (nie generycznej) analizy.

**Warstwa zadaniowa** — pięć etapów sekwencyjnych: zapoznanie z kontekstem → identyfikacja obszarów → analiza każdego → rekomendacja kolejności → gotowe parametry do PULSE. Sekwencja wymusza systematyczność — AI nie może przeskoczyć do rekomendacji bez wcześniejszego przeczytania materiałów.

**Warstwa jakości** — zasady filtrujące wynik: kompletność bez nadmiarowości, celowość funkcji celu, konkretność pytań badawczych, szacunek dla istniejących decyzji.

---

## 3. Model działania

SCAN to jednorazowe narzędzie — uruchamia się raz na początku projektu (lub ponownie przy dużej zmianie zakresu). Nie ma rund jak PULSE. Jedna sesja z AI daje kompletny wynik.

Przebieg sesji:

```
Użytkownik przygotowuje dane wejściowe (15–30 min)
         ↓
Użytkownik otwiera nowy czat z AI
         ↓
Użytkownik wkleja prompt SCAN z wypełnionymi polami
         ↓
AI czyta materiały wewnętrzne (jeśli dołączone)
         ↓
AI przeprowadza analizę (5 etapów)
         ↓
AI generuje dokument — mapę terenu implementacyjnego
         ↓
Użytkownik przegląda mapę
         ↓
Użytkownik dodaje brakujące obszary z własnego doświadczenia
         ↓
Użytkownik usuwa nieistotne obszary
         ↓
Użytkownik ustala ostateczną kolejność
         ↓
Mapa zatwierdzona — gotowa do uruchamiania PULSE
```

Czas: około 1–2 godziny (przygotowanie danych + sesja z AI + przegląd wyniku).

**Wymaganie:** AI z włączonym wyszukiwaniem internetowym (web search) da pełniejsze wyniki — może sprawdzić aktualne regulacje i trendy dla typu rozwiązania. Bez web search SCAN zadziała, ale lista obszarów będzie oparta na wiedzy treningowej.

---

## 4. Przypadek użycia — jak poprawnie sparametryzować prompt

### Parametr 1: Opis rozwiązania

**Co wpisać:** Naturę produktu, jego główną wartość, model działania, kluczowe mechaniki. Wyobraź sobie że tłumaczysz swój produkt inteligentnemu inżynierowi który go nigdy nie widział.

**Dobry przykład:**
> Budujemy platformę telemedyczną łączącą lekarzy specjalistów, pacjentów i ubezpieczycieli. Lekarze prowadzą konsultacje wideo, wystawiają e-recepty i monitorują pacjentów zdalnie przez wearables. Pacjenci rezerwują wizyty, przesyłają wyniki badań (zdjęcia, PDF, dane z urządzeń IoT) i otrzymują spersonalizowane plany leczenia. Ubezpieczyciele rozliczają wizyty automatycznie i monitorują jakość świadczeń. Platforma obejmuje system triażu AI (wstępna ocena objawów przed konsultacją), adaptacyjny dashboard lekarza (priorytetyzacja pacjentów na podstawie pilności), szyfrowaną komunikację end-to-end i integrację z systemami szpitalnymi (HL7 FHIR). Model przychodowy: subskrypcja dla lekarzy + prowizja od konsultacji + opłata licencyjna od ubezpieczycieli.

**Zły przykład:**
> Robimy apkę medyczną.

Im więcej kontekstu — tym celniejsza analiza SCAN.

### Parametr 2: Profil odbiorcy

**Co wpisać:** Grupy użytkowników z ich charakterystykami. Jeśli masz wiele grup — opisz każdą krótko.

**Dobry przykład:**
> Trzy grupy: (1) Pacjenci — 25–75 lat, różny poziom zaawansowania technicznego (od cyfrowych natywnych po seniorów z podstawową obsługą smartfona), korzystają głównie z telefonu, oczekują prostoty i szybkiego dostępu do lekarza. (2) Lekarze specjaliści — 30–65 lat, wysokie wymagania co do niezawodności i bezpieczeństwa danych, korzystają z laptopa i tabletu podczas konsultacji, potrzebują integracji z systemami szpitalnymi. (3) Ubezpieczyciele — zespoły IT i operacyjne firm ubezpieczeniowych, potrzebują API do automatycznego rozliczania i raportowania jakości świadczeń.

### Parametr 3: Ograniczenia projektowe

**Co wpisać:** Twarde fakty o zasobach i warunkach brzegowych.

**Dobry przykład:**
> Zespół: CTO (architektura), 3 deweloperów fullstack, 1 UX designer, 1 specjalista ds. regulacji medycznych. Budżet: €200k na MVP + €50k/rok utrzymanie. Czas: MVP w Q3 2026, pełna wersja Q1 2027. Regulacje: RODO, ustawa o wyrobach medycznych (MDR), dyrektywa NIS2 (cyberbezpieczeństwo), wymóg certyfikacji jako wyrób medyczny klasy I (jeśli triaz AI). Technologie wybrane: React Native (mobile cross-platform), Node.js (backend), PostgreSQL (baza), AWS (hosting z certyfikacją HIPAA/ISO 27001). Istniejąca infrastruktura: integracja z 3 systemami szpitalnymi przez HL7 FHIR.

**Jeśli nie wiesz:** Napisz „do ustalenia" przy konkretnym parametrze. SCAN uwzględni to jako otwarte pytanie.

### Parametr 4: Materiały wewnętrzne

**Co wpisać:** Lista plików które dołączasz do czatu lub które są dostępne w projekcie Claude (FILES).

**Dobry przykład:**
> Dołączam / W FILES dostępne: specyfikacja ogólna platformy (MedConnect_Overview_v2.md), Decision Log (MedConnect_Decision_Log.md), specyfikacja modułu triażu AI (Triage_AI_Spec_v1.md), specyfikacja integracji HL7 FHIR (FHIR_Integration_Spec.md), analiza regulacyjna MDR (Regulatory_Analysis_MDR.md), prototyp UX dashboardu lekarza (Doctor_Dashboard_Prototype_v1.html).

**Jeśli nie masz:** Napisz „brak materiałów wewnętrznych, projekt startuje od zera." SCAN zadziała — analiza będzie bardziej generyczna, ale nadal wartościowa.

---

## 5. Wskazówki dodatkowe

### Co robić po otrzymaniu wyniku SCAN

Przeczytaj tabelę obszarów. Zadaj sobie pytanie: „Czy jest coś co ja wiem o swoim projekcie, a czego AI nie mogło wiedzieć?" Dodaj to. Następnie zadaj drugie pytanie: „Czy któryś z obszarów jest zbędny?" Jeśli np. AI zaproponowało „Strategia internacjonalizacji" a Ty celujesz wyłącznie w rynek polski — usuń.

Kolejność PULSE rekomendowana przez SCAN jest sugestią, nie nakazem. Jeśli masz powód żeby zacząć od innego obszaru (np. bariera czasowa, zależność od partnera zewnętrznego) — zmień kolejność.

### Kiedy uruchomić SCAN ponownie

Trzy sytuacje uzasadniają ponowne uruchomienie:

Fundamentalna zmiana zakresu — np. dodanie nowej grupy użytkowników, zmiana modelu biznesowego, wejście na nowy rynek.

Pojawienie się nowego ograniczenia — np. nowe regulacje, zmiana budżetu, zmiana techstack.

Ukończenie wszystkich PULSE — po zbudowaniu wszystkich Living Patterns warto uruchomić SCAN jeszcze raz żeby sprawdzić czy nie pojawiły się nowe obszary wynikające ze zdobytej wiedzy (rzadkie, ale możliwe).

### Czego SCAN nie robi

SCAN nie buduje wiedzy. Nie przeprowadza researchu branżowego ani naukowego. Nie odpowiada na pytania implementacyjne. SCAN IDENTYFIKUJE pytania — odpowiedzi buduje PULSE.

SCAN nie zastępuje doświadczenia. Jeśli masz wiedzę domenową której AI nie ma (np. specyfika lokalnych regulacji telemedycznych w Twoim kraju) — Ty musisz dodać to do wyniku SCAN.

---

*Dokument opracowany: 9 marca 2026*
*Wersja: 3.0*
*Licencja: CC BY-SA 4.0*
