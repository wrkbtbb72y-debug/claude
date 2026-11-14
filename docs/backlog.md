# Backlog

> Wyniki audytu z 2026-11-14 + plan rozbudowy. P0 = blokuje publikację, P1 = ważne, P2 = później.
> Odhaczaj `[x]` i dopisuj datę.

## P0 — przed publikacją

- [ ] **Licencje fontów.** ABC Diatype i ABC Arizona Mix Condensed są w wersjach
      *Trial / Unlicensed Trial* — nie wolno ich używać na produkcji. Opcje: kupić licencje
      webowe (Dinamo) albo podmienić na zamienniki (np. grotesk: Inter / Geist; condensed
      serif: Instrument Serif lub Google Fonts). Dotyczy 9 z 13 presetów.
- [ ] **SEO / metadane.** Tytuł strony to „My Framer Site”, opis „Made with Framer”.
      Ustawić tytuł, opis, obraz społecznościowy (OG), favicon.
- [ ] **Alt-teksty:** 0 z 19 obrazów na Home ma alt-text (zob. content-guidelines.md).
- [ ] **Nawigacja i linki:** nie wykryto `href` w Nav Bar (Works / Info / Awards / Contact)
      ani w kolumnach stopki (Menu, Instagram, Facebook, E-mail, Privacy Policy, Site credits).
      Do weryfikacji i podpięcia (kotwice `#work`, `#about`, mailto:, profile social).
- [ ] **E-mail kontaktowy:** `e.dabrowska@mail.com` — potwierdzić, że to prawdziwy adres.
- [ ] **Privacy Policy:** link w stopce, strony brak. Stworzyć lub usunąć link.
- [ ] **Usunąć draft `/home`** (`PkrJvvJdu`) — stara kopia Home, ryzyko pomyłki.
- [ ] Domena i pierwsza publikacja.

## P1 — fundamenty pod rozbudowę

- [ ] **Nowa architektura wg ustaleń z 2026-11-14** (decisions.md): menu Work · Where to see ·
      Exhibitions · Film / Performance · Publications / Press · About · Contact; obecny Nav Bar
      (Works / Info / Awards / Contact) do zmiany.
- [ ] **Mapa „Where to see”:** dodać do `content/works.csv` pola na lokalizację (np. `maps_url`,
      `lat`, `lng`, `visitable`) — po decyzji artystki co z pracami efemerycznymi i prywatnymi.
- [ ] **Home:** dodać sekcję logotypów instytucji + przyciski „Zobacz realizacje” / „Kontakt” /
      „Gdzie zobaczyć moje prace”.
- [ ] **Contact:** podstrona z widocznym e-mailem + formularzem (formularz ⇒ Privacy Policy).
- [ ] **Czekamy na artystkę:** inspiracje, wybór 3–5 projektów na Home i kolejność Work, kierunek
      logo, lokalizacje prac, potwierdzenie e-maila, logotypy instytucji, linki YouTube.

- [ ] **CMS „Works”** wg schematu `content/works.csv` + strona listy `/works` i detail `/works/:slug`.
- [ ] **Layout Template** z Nav Bar i stopką — warunek przed dodaniem kolejnych stron.
- [ ] **Tokeny kolorów** zamiast surowych wartości (Ink / Paper / Line / Muted) — bez zmiany wyglądu.
- [ ] **Strona Publications / Press** (ustalona nazwa; dawniej „Awards”).
- [ ] **About** — osobna podstrona (ustalone 2026-11-14); „Read more” na Home ma do niej prowadzić.
- [x] Decyzja PL/EN — najpierw EN, PL na końcu z przełącznikiem (2026-11-14).
- [ ] Ujednolicić `Copyright`: w stopce są dwa warianty („© 2026 Ewa Dąbrowska” i „… All rights reserved.”).

## P2 — później

- [ ] Press kit do pobrania (bio, zdjęcia hi-res, CV PDF).
- [ ] Analityka (Framer Analytics jest dostępne) — cele: klik w e-mail, wejścia w prace.
- [ ] Dane strukturalne JSON-LD (`Person`, `VisualArtwork`) dla SEO.
- [ ] Wydajność: rozmiary zdjęć i wideo (Bandwidth), `prefers-reduced-motion` dla efektów scrolla.
- [ ] Porządek w design page „Robocze”.
- [ ] Framer project skill (SkillNode) z zasadami marki — żeby AI wewnątrz Framera też ich pilnowało.
