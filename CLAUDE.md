# Ewa Dąbrowska — oficjalna strona artystki

To repozytorium jest **bazą wiedzy projektu** strony Ewy Dąbrowskiej (land-art, rzeźba,
rysunek i stop-motion, dźwięk). Sama strona (wygląd, layout, CMS) żyje we **Framerze** —
tutaj trzymamy wszystko, czego Framer nie pamięta: brief, ustalenia, system projektowy,
mapę projektu, treści, bazę prac i backlog.

- **Framer:** https://framer.com/projects/Ewa-D-browska-Official--gMKkn1ektXgFZXROgJCy-a6APP
  (project ID `gMKkn1ektXgFZXROgJCy`)
- **Produkcja:** jeszcze nieopublikowana — domena: _TODO_
- **Język rozmowy z Claude:** polski. **Język treści na stronie:** patrz `docs/content-guidelines.md`.

## Mapa repozytorium

| Plik | Po co | Kiedy czytać |
|---|---|---|
| `docs/brief.md` | Kim jest artystka, cel strony, odbiorcy, ton | Przed każdą zmianą treści lub nową sekcją |
| `docs/design-system.md` | Kolory, typografia (ID presetów), komponenty, ruch | Przed każdą zmianą wizualną |
| `docs/framer-map.md` | Strony, sekcje, ID węzłów, kotwice, triggery scrolla | Przed edycją we Framerze |
| `docs/content-guidelines.md` | Język PL/EN, ton, alt-teksty, nazewnictwo prac | Przy pisaniu copy |
| `docs/decisions.md` | Log decyzji (co, dlaczego, kiedy) | Gdy coś wydaje się „dziwne” — może było celowe |
| `docs/ustalenia/` | Dokument ustaleń z klientką (HTML → PDF, najnowsza wersja = najwyższy numer) | Gdy trzeba wysłać artystce aktualny stan ustaleń |
| `docs/backlog.md` | Znane problemy i plan prac z priorytetami | Na start sesji roboczej |
| `content/works.csv` | Baza prac — źródło prawdy dla przyszłego CMS „Works” | Przy dodawaniu/edycji prac |
| `content/bio.md`, `content/awards-press.md` | Teksty źródłowe | Przy sekcjach About / Awards / Press |

Skille projektu (`.claude/skills/`): **`/framer-audit`** — audyt przed publikacją,
**`/add-work`** — dodanie nowej pracy do bazy (i do CMS, gdy powstanie).

## Jak pracować z Framerem (MCP `mcp__Framer__*`)

1. `open_project` z linkiem powyżej → dostajesz `session`; wszystkie dalsze wywołania przez `exec`.
2. **Najpierw czytaj, potem zmieniaj.** Pierwszy program zawsze tylko-do-odczytu (sitemap,
   serialize, screenshot). Użytkownik edytuje canvas ręcznie między sesjami — nigdy nie
   nadpisuj jego zmian copy z pamięci; czytaj aktualny stan węzła.
3. **Szanuj system.** Używaj istniejących presetów tekstu, tokenów i komponentów
   (`docs/design-system.md`). Nie modyfikuj presetów/komponentów „przy okazji” — tylko na
   wyraźną prośbę. Nowy styl = nowy preset, dopisany do design-system.md.
4. **Każda zmiana → screenshot wszystkich 3 breakpointów** (Desktop 1200 / Tablet 810 /
   Phone 390) i obejrzenie go. Strona Home ma rozbudowane triggery scrolla — sprawdź, czy
   kotwice z `docs/framer-map.md` nadal istnieją.
5. **Branche:** pierwsza edycja AI tworzy branch we Framerze. **Nigdy nie merguj i nie
   publikuj** bez wyraźnego polecenia. W podsumowaniu zawsze podaj link do brancha.
6. ID węzłów w replikach (Tablet/Phone) to ID złożone `<breakpoint><węzeł>` — nie
   wstawiaj nic do replik, tylko patchuj.

## Kluczowe fakty (skrót — szczegóły w docs/)

- **Klimat:** ciemny, galeryjny, dużo powietrza; czerń `#000` + biel, akcent przez zdjęcia,
  nie przez kolor. Duża szeryfowa typografia (Instrument Serif) + techniczny grotesk
  (ABC Diatype) do UI.
- **Struktura Home:** Hero „Land-Art & Sculpture” → pasek „Explore projects” (sticky) →
  Projects (rozsypane zdjęcia z efektami scrolla) → My Journey / About (cytat, portret,
  Practice 01–04) → footer reveal (kontakt, e-mail).
- **Practice (4 obszary = kategorie prac):** Land Art & Happenings · Sculpture ·
  Drawing & stop-motion · Sound.
- **Zewnętrzne moduły:** Lenis (smooth scroll), Video, override `withLinksAfterSection`.
- **Brak CMS** — prace są wpięte ręcznie na canvasie. Plan: kolekcja „Works” zgodna ze
  schematem `content/works.csv` (patrz backlog).

## Zasady treści (skrót)

- Typograficzne cudzysłowy i apostrofy („ ” ’ “ ”), półpauza w zakresach lat (2019–2021).
- Każde zdjęcie pracy ma **alt-text** (tytuł + materiał + co widać) — zob. content-guidelines.
- Tytuły prac: oryginalny polski tytuł jest nadrzędny; angielski jako tłumaczenie.
- Nie wymyślaj faktów o artystce (dat, nagród, wystaw, materiałów). Brak danych → `TODO`
  i pytanie do użytkownika.

## Definition of done dla zmiany na stronie

- [ ] Zmiana obejrzana na screenshotach Desktop / Tablet / Phone
- [ ] Brak diagnostyk/ostrzeżeń z `exec`
- [ ] Nowe obrazy mają alt-text, nowe linki mają `href` i `linkStylePreset`
- [ ] `docs/framer-map.md` zaktualizowany, jeśli zmieniła się struktura/ID
- [ ] Istotna decyzja dopisana do `docs/decisions.md` (data, decyzja, powód)
- [ ] Zamknięte/nowe punkty odhaczone w `docs/backlog.md`

## Utrzymanie tej wiedzy

Po każdej sesji, w której coś ustaliliśmy, **zaktualizuj odpowiedni plik w `docs/`** i
zaproponuj commit. CLAUDE.md trzymaj krótki — szczegóły idą do `docs/`.
