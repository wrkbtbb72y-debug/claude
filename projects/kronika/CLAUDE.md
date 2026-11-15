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
  „Otwarte zasoby nauki i kultury” + licznik „19mln zgromadzonych obiektów”, nad
  „Instytucje Partnerskie”.
- Presety tekstu są responsywne (sloty `medium` ≥1024, `small` ≥768): np. „Nazwy sekcji”
  `onFkvs54B` 28→26 px, „Body 1 - tekst długi L” `qho9AhWr_` 20→18 px na tablecie.

## Ustalenia i decyzje

- 2026-11-15 — Sekcja „O Portalu‑section 4” na Tablecie ma wyglądać jak na Desktop Primary:
  zresetowano wszystkie nadpisania tabletu w tej sekcji (szerokość bloku licznika 527→468 px,
  kolor tytułu, wariant przycisku „Czytaj więcej”, padding pod tytułem 12→9 px, overflow).
  Presetów tekstu nie ruszano (różnica rozmiaru fontu 28/26 i 20/18 px zostaje) — na prośbę
  użytkownika. Uwaga: zmiana trafiła bezpośrednio do `main` we Framerze (nie utworzył się
  branch), strona nieopublikowana.

## Do zrobienia

- [ ] Zdecydować, czy na tablecie tytuł sekcji i podpis licznika mają mieć te same rozmiary
      fontu co na Desktop Primary (wymaga zmiany presetów — wpływa na całą stronę).
- [ ] Uzupełnić brief (pola TODO powyżej).
