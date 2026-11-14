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

- [ ] **CMS „Works”** wg schematu `content/works.csv` + strona listy `/works` i detail `/works/:slug`.
- [ ] **Layout Template** z Nav Bar i stopką — warunek przed dodaniem kolejnych stron.
- [ ] **Tokeny kolorów** zamiast surowych wartości (Ink / Paper / Line / Muted) — bez zmiany wyglądu.
- [ ] **Strona Awards / Press** (nawigacja już do niej odsyła).
- [ ] **Info / About** — decyzja: osobna strona czy kotwica `#about`; „Read more” musi gdzieś prowadzić.
- [ ] Decyzja PL/EN (decisions.md).
- [ ] Ujednolicić `Copyright`: w stopce są dwa warianty („© 2026 Ewa Dąbrowska” i „… All rights reserved.”).

## P2 — później

- [ ] Press kit do pobrania (bio, zdjęcia hi-res, CV PDF).
- [ ] Analityka (Framer Analytics jest dostępne) — cele: klik w e-mail, wejścia w prace.
- [ ] Dane strukturalne JSON-LD (`Person`, `VisualArtwork`) dla SEO.
- [ ] Wydajność: rozmiary zdjęć i wideo (Bandwidth), `prefers-reduced-motion` dla efektów scrolla.
- [ ] Porządek w design page „Robocze”.
- [ ] Framer project skill (SkillNode) z zasadami marki — żeby AI wewnątrz Framera też ich pilnowało.
