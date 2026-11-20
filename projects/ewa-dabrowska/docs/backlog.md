# Backlog

> Wyniki audytu z 2026-11-14 + plan rozbudowy. P0 = blokuje publikację, P1 = ważne, P2 = później.
> Odhaczaj `[x]` i dopisuj datę.
>
> **[KLIKA]** = punkt wymagany do zaliczenia kursu KLIKA — pełna lista i statusy: `docs/zaliczenie-klika.md`.

## P0 — przed publikacją

- [ ] **Licencje fontów.** ABC Diatype i ABC Arizona Mix Condensed są w wersjach
      *Trial / Unlicensed Trial* — nie wolno ich używać na produkcji. Opcje: kupić licencje
      webowe (Dinamo) albo podmienić na zamienniki (np. grotesk: Inter / Geist; condensed
      serif: Instrument Serif lub Google Fonts). Dotyczy 9 z 13 presetów.
      ➡ 2026-11-15: próbki darmowych zamienników są we Framerze na design page
      „Fonty — propozycje zamienników” (`IC_Z5ffzI`). **Decyzja Piotra** — style nie zostały zmienione.
- [x] **SEO / metadane** — tytuł „Ewa Dąbrowska · Land Art & Sculpture” i opis ustawione (2026-11-15).
- [ ] **[KLIKA]** **Obraz społecznościowy (OG) i favicon** — do dodania (potrzebny wybór zdjęcia / znak).
- [x] **Alt-teksty** — 13 zdjęć prac i portret na Home mają opisy (2026-11-15); 6 grafik dekoracyjnych
      (ikony, kreski) celowo bez opisu.
- [ ] **[KLIKA]** **Nawigacja i linki:** nie wykryto `href` w Nav Bar (Works / Info / Awards / Contact)
      ani w kolumnach stopki (Menu, Instagram, Facebook, E-mail, Privacy Policy, Site credits).
      Do weryfikacji i podpięcia (kotwice `#work`, `#about`, mailto:, profile social).
      KLIKA: linki bez tekstu (logo, ikony social, „Back to top”) muszą mieć **aria-label**.
      ⚠ Pozycje menu zmienią się wg nowej architektury (P1) — linki podpinać już do docelowych podstron.
      ➡ 2026-11-15: menu ma już docelowe pozycje (Work, Where to see — do usunięcia 2026-11-20, Exhibitions, Film / Performance,
      Publications / Press, About + Contact + EN / PL); logo prowadzi do `/`. **Linki pozycji menu
      czekają na utworzenie podstron** (wstrzymane na prośbę Piotra).
- [ ] **E-mail kontaktowy:** `e.dabrowska@mail.com` to **adres przykładowy** (potwierdzone 2026-11-14) —
      podmienić na prawdziwy, gdy artystka go poda (stopka, Contact, `mailto:`, odbiorca formularza).
- [ ] **Privacy Policy:** link w stopce, strony brak. Ustalono formularz kontaktowy, więc
      podstrona `/privacy` jest **wymagana** (nie usuwamy linku).
- [x] **Usunięto draft `/home`** (`PkrJvvJdu`, 2026-11-15) — w razie potrzeby do odzyskania z historii wersji Framera.
- [ ] Domena i pierwsza publikacja.
- [x] **Footer Bar nie pojawiał się przy stopce** — warianty *Desktop Visible* / *Phone Visible*
      (`CZImlwXQG`) miały opacity 0 jak *Hidden*; ustawiono 1 i przywrócono wysuwanie z góry
      (szczegóły w decisions.md, 2026-11-14).
- [ ] **[KLIKA]** **Szare paski po bokach sekcji About** — prześwituje stopka (`NMyUr1YCD`, z-index 4, sticky
      bottom), bo „About + sticky-scope” (`hVUwmnJJl`) nie ma z-indexu, a jego dzieci zaczynają się
      za paddingiem 60px. Proponowana poprawka: Z Index = 5 na `hVUwmnJJl` (powyżej stopki 4 i
      Projects 2–3).

## P1 — fundamenty pod rozbudowę

- [x] **Przełącznik języków EN / PL w Nav Bar** — dodany wizualnie we wszystkich 4 wariantach (2026-11-15);
      **aktywować** (podpiąć pod lokalizację Framera) na etapie wersji PL.
- [ ] **[KLIKA]** **Podstrony + szablon (Layout Template) z nawigacją i stopką** — Work, Exhibitions (z mapą prac),
      Film / Performance, Publications / Press, About, Contact. **Wstrzymane na prośbę Piotra (2026-11-15).**
      KLIKA wymaga min. 1 zalinkowanej podstrony i Layout Template z top-barem i stopką.
      Gdy ruszą: podpiąć linki w menu, Contact → `/contact`, „Read more” → `/about`.
- [x] **„Where to see” zniknęło z Nav Bar** (2026-11-20, sprawdzone we Framerze — zmienione ręcznie: ten węzeł to teraz „Awards”).
- [ ] **Ustalić widoczne pozycje menu** — na canvasie: Work · About · Awards (Exhibitions, Film / Performance,
      Publications / Press ukryte); ustalone menu: Work · Exhibitions · Film / Performance · Publications / Press ·
      About · Contact. Czy „Awards” wraca do menu? (pytanie do Piotra, 2026-11-20)
- [ ] **Podstrona Exhibitions** — dane gotowe w CMS „Exhibitions” (18 wystaw); zostaje zbudować stronę z listą
      **+ mapa prac i lista miejsc** (dawne „Where to see”, 2026-11-20).
- [x] **Menu (hamburger)** — działa na desktopie, tablecie i telefonie jako wariant Open komponentu Nav Bar
      (2026-11-20, framer-map.md). Do zrobienia: podpiąć `href` linków, gdy powstaną podstrony; URL-e
      Instagram / Facebook (od artystki); link przycisku Contact (`eVB1wQuPY`) — czeka na podstronę Contact; sprawdzić w podglądzie zachowanie przy przewijaniu z otwartym menu.
      Performance nie ma w menu (2026-11-20) — gdy powstanie podstrona, zdecydować, skąd będzie dostępna.
- [ ] **Opisy prac po angielsku** — pole *Description* w CMS „Works” jest puste; źródło: `content/sources/portfolio-2026-09.md`.
- [ ] **Okładki w CMS** — 8 z 31 prac ma okładkę (zdjęcia już będące na stronie); reszta po zmniejszeniu
      zdjęć z Dysku. Pole *Photos source (Drive)* wskazuje folder.
- [ ] **[KLIKA] Sprawdzić we Framerze** (brak danych w dokumentacji): wrappery z Max Width w sekcjach,
      hover na wszystkich przyciskach, znaczniki HTML (header / nav / main / section / footer),
      nazwy wszystkich warstw, presety na wszystkich tekstach, test 1920 → 390 px.
- [ ] **Przycisk Contact w wariantach Black** paska (Desktop/Tablet/Phone Black) jest niewidoczny — biały na białym.
      Od 2026-11-20 Contact jest w pasku na stałe (prawa strona); potrzebny ciemny wariant przycisku `flntBxkgE`.
- [ ] **Pytania do artystki po lekturze portfolio** (szczegóły w kolumnie `notes` w `content/works.csv`):
      „Słoneczny Stwór”, „Kłos”, „Wszechkarmicielka” — brak w portfolio (dane?); czy „Tancerz” =
      „Taniec deszczu”?; „Wszechkarmicielka” — część „Żywiciała”?; rok „Państwa Gąbczaków” i
      „Obsesji” (portfolio 2014, pliki 2015); pisownia „Kroppemaan”; zdjęcia Ewy — które na About.
- [ ] **Zdjęcia:** zmniejszyć pliki z aparatu (10–31 MB) przed Framerem; brakuje folderów zdjęć dla
      części prac z portfolio (lista w `works.csv` → `notes`).
- [ ] **Autorzy zdjęć** (A. Aubry, Kaja Tarłowska, …) — podpisywać na stronach prac; zebrać brakujące.
- [x] Baza prac zbudowana z portfolio (31 pozycji), lista wystaw/nagród/filmów i biogram (2026-11-14).

- [ ] **Nowa architektura wg ustaleń z 2026-11-14** (decisions.md): menu Work ·
      Exhibitions · Film / Performance · Publications / Press · About · Contact; obecny Nav Bar
      (Works / Info / Awards / Contact) do zmiany.
- [ ] **Mapa prac (na podstronie Exhibitions, dawne „Where to see”):** mapa + lista miejsc — po decyzji artystki, co z pracami
      efemerycznymi i prywatnymi (pola w `works.csv` już są).
- [ ] **Home:** dodać sekcję logotypów instytucji + przyciski „Zobacz realizacje” / „Kontakt” /
      „Gdzie zobaczyć moje prace” (ten trzeci — do ustalenia, czy zostaje; prowadziłby do Exhibitions).
- [ ] **Contact:** podstrona z widocznym e-mailem + formularzem (formularz ⇒ Privacy Policy).
- [ ] **Czekamy na artystkę:** inspiracje, lokalizacje prac do mapy, prawdziwy e-mail,
      wybór logotypów instytucji (kandydaci w `content/awards-press.md`), szkic znaku (bez terminu).
      Linki YouTube — 4 są w portfolio (`awards-press.md` → Filmy); zapytać o kolejne (np. „Spójnia”).
- [x] Kolejność prac i kierunek logo ustalone (2026-11-14, decisions.md).
- [ ] **Prace „Tancerz” i „Dziki”** — uzupełnić dane w `content/works.csv` (skill `/add-work`).
      Wiersz „Tancerz” i kolumna `order` już są (2026-11-14). „Dziki” = „Herd” — potwierdzone.
- [x] Kolumny na mapę (`maps_url`, `can_visit`) dodane do `content/works.csv` (2026-11-14);
      współrzędne niepotrzebne, jeśli są linki z Map Google.
- [x] **Logotyp:** font odręczny **Parisienne** (Google Fonts, OFL) — 2026-11-20; do akceptacji artystki.

- [x] **CMS „Works”** (31 prac, 2026-11-15; strony listy i detail — jeszcze nie) wg schematu `content/works.csv` + strona listy `/work` i detail `/work/:slug` (zgodnie z brief.md).
- [ ] **[KLIKA]** **Layout Template** z Nav Bar i stopką — warunek przed dodaniem kolejnych stron.
- [x] **Tokeny kolorów** Ink / Paper / Line / Muted — dodane i podpięte w miejsce identycznych wartości na Home
      i w komponentach (24 miejsca) oraz w presecie Caption (2026-11-15).
- [ ] **Strona Publications / Press** (ustalona nazwa; dawniej „Awards”).
- [ ] **[KLIKA]** **About** — osobna podstrona (ustalone 2026-11-14); „Read more” na Home ma do niej prowadzić.
- [x] Decyzja PL/EN — najpierw EN, PL na końcu z przełącznikiem (2026-11-14).
- [ ] Ujednolicić `Copyright`: w stopce są dwa warianty („© 2026 Ewa Dąbrowska” i „… All rights reserved.”).

## P2 — później

- [ ] Press kit do pobrania (bio, zdjęcia hi-res, CV PDF).
- [ ] Analityka (Framer Analytics jest dostępne) — cele: klik w e-mail, wejścia w prace.
- [ ] Dane strukturalne JSON-LD (`Person`, `VisualArtwork`) dla SEO.
- [ ] Wydajność: rozmiary zdjęć i wideo (Bandwidth), `prefers-reduced-motion` dla efektów scrolla.
- [ ] Porządek w design page „Robocze”.
- [x] Framer project skill **`ewa-brand`** z zasadami marki i listą kotwic scrolla (2026-11-15).
