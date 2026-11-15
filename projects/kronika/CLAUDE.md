# Kronika

<!-- Utworzone 2026-11-14 z szablonu. Pola TODO uzupełnić z użytkownikiem — nie zgadywać. -->

Zasady wspólne (praca z Framerem, definition of done) są w głównym `CLAUDE.md` repozytorium.
Ścieżki w tym pliku są względem tego folderu.

- **Framer:** https://framer.com/projects/Kronika--0h5pA6cwUCiyjVB0qFni-1oD05
  (project ID `0h5pA6cwUCiyjVB0qFni`)
- **Produkcja / domena:** _TODO_
- **Materiały od klienta:** _TODO (np. link do Google Drive)_
- **Język treści na stronie:** _TODO (PL / EN / oba)_
- **Termin:** _TODO_

## O projekcie (brief w skrócie)

- **Klient:** kim jest, czym się zajmuje.
- **Cel strony:** _TODO_
- **Odbiorcy:** _TODO_
- **Ton / klimat:** _TODO_

## Struktura strony

- **Home** (`augiA20Il`) — breakpointy: **Desktop Primary** `d0VxK3QJN` (1024, primary,
  1024–1439 px), **Tablet** `hzEqmNBoY` (810, 810–1023 px), **Duzy desktop** `XjMbofAH4`
  (1440, ≥1440 px), **Mobile** `YLBtCSeLh` (390, <810 px). Uwaga: primary to 1024, nie 1200.
- Sekcja „O Portalu‑section 4” (`XQ6Ofe1Rp`, w środku `About_wrapper` `tTtyi3gJx`) —
  „Otwarte zasoby nauki i kultury”, nad „Instytucje Partnerskie”. Desktop Primary, Tablet
  i Duży desktop: ilustracja „tablet i książki” (`XTasEtfqG`) po lewej + tekst „Zapewniamy
  bezpłatny dostęp…” z „Czytaj więcej” (`OJuh71bfJ`) po prawej; „Czytaj więcej” w wierszu
  tytułu (`FXesmdTxZ`) ukryte. Mobile: tytuł z „Czytaj więcej” + licznik „19mln
  zgromadzonych obiektów” (`uXWoz4CPW`, `B22SY_ZNm`) — utrzymane nadpisaniami Mobile.
- Presety tekstu są responsywne (sloty `medium` ≥1024, `small` ≥768): np. „Nazwy sekcji”
  `onFkvs54B` 28→26 px, „Body 1 - tekst długi L” `qho9AhWr_` 20→18 px na tablecie.

## Ustalenia i decyzje

- 2026-11-15 — Sekcja „O Portalu‑section 4” na Tablecie ma wyglądać jak na Desktop Primary:
  zresetowano wszystkie nadpisania tabletu w tej sekcji (szerokość bloku licznika 527→468 px,
  kolor tytułu, wariant przycisku „Czytaj więcej”, padding pod tytułem 12→9 px, overflow).
  Presetów tekstu nie ruszano (różnica rozmiaru fontu 28/26 i 20/18 px zostaje) — zmiana presetów wpłynęłaby na całą stronę, czeka na decyzję
  użytkownika. Uwaga: zmiana trafiła bezpośrednio do `main` we Framerze (nie utworzył się
  branch), strona nieopublikowana.

- 2026-11-15 — Ta sama sekcja na Desktop Primary i Tablecie pokazuje te same elementy co na
  Dużym desktopie (ilustracja + opis zamiast licznika „19mln”) — prośba użytkownika. Zmiana
  na Desktop Primary (dziedziczy Tablet); Mobile celowo bez zmian. Znów bezpośrednio w `main`
  we Framerze, nieopublikowane.

## Do zrobienia

- [ ] Zdecydować, czy na tablecie tytuł sekcji i opis mają mieć te same rozmiary fontu co na
      Desktop Primary (28/20 px zamiast 26/18 px — wymaga zmiany presetów, wpływa na całą stronę).
- [ ] Zdecydować, czy Mobile w sekcji „Otwarte zasoby…” też ma dostać ilustrację + opis.
- [ ] Uzupełnić brief (pola TODO powyżej).
