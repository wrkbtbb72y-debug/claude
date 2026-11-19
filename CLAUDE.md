# Projekty — baza wiedzy

To repozytorium trzyma **wiele projektów** (głównie strony we Framerze). Każdy projekt ma
własny folder w `projects/<nazwa>/` z własnym `CLAUDE.md`, dokumentacją i ewentualnie
skillami. Ten plik zawiera tylko spis projektów i zasady wspólne dla wszystkich.

**Język rozmowy z Claude:** polski.

## Na start każdej sesji

1. Ustal, nad którym projektem pracujemy (z wiadomości użytkownika). Jeśli nie wiadomo —
   **zapytaj**, nie zgaduj.
2. Przeczytaj `projects/<nazwa>/CLAUDE.md` i trzymaj się go. Ścieżki w dokumentach projektu
   są względem jego folderu.
3. Nie mieszaj projektów: nie czytaj ani nie zmieniaj plików innych projektów, a we Framerze
   otwieraj tylko projekt podany w `CLAUDE.md` danego folderu.

## Spis projektów

| Folder | Klient / projekt | Framer | Status |
|---|---|---|---|
| `projects/ewa-dabrowska/` | Ewa Dąbrowska — oficjalna strona artystki | [projekt](https://framer.com/projects/Ewa-D-browska-Official--gMKkn1ektXgFZXROgJCy-a6APP) | w toku |
| `projects/kronika/` | Kronika | [projekt](https://framer.com/projects/Kronika--0h5pA6cwUCiyjVB0qFni-1oD05) | w toku — brief do uzupełnienia |
| `projects/wnetrze-3d/` | NUMINO / Wnętrze 3D („Kubatura”) — interaktywne wnętrze z linii | [projekt](https://framer.com/projects/Bashful-Career--TrZY6V7hpIyWsOmfEYfW-dBvqu) | w toku |
| `projects/si2pem/` | SI2PEM — serwis o PEM (projekt tylko w Figmie) | [Figma](https://www.figma.com/design/kiuBZ1fA0OMqFDdPuhmnHy/SI2PEM) | w toku |

**Nowy projekt:** skopiuj `projects/_template/` do `projects/<nazwa>/`, uzupełnij jego
`CLAUDE.md` i dopisz wiersz do tabeli powyżej. Krótkiemu projektowi wystarczy sam `CLAUDE.md`
(brief, link do Framera, notatki) — folder `docs/` dodaj dopiero, gdy będzie potrzebny.
Zakończony projekt: status „zakończony” (folder zostaje jako archiwum).

## Jak pracować z Framerem (MCP `mcp__Framer__*`)

1. `open_project` z linkiem z `CLAUDE.md` projektu → dostajesz `session`; wszystkie dalsze
   wywołania przez `exec`.
2. **Najpierw czytaj, potem zmieniaj.** Pierwszy program zawsze tylko-do-odczytu (sitemap,
   serialize, screenshot). Użytkownik edytuje canvas ręcznie między sesjami — nigdy nie
   nadpisuj jego zmian copy z pamięci; czytaj aktualny stan węzła.
3. **Szanuj system.** Używaj istniejących presetów tekstu, tokenów i komponentów (opisanych
   w `design-system.md` projektu, jeśli istnieje). Nie modyfikuj presetów/komponentów
   „przy okazji” — tylko na wyraźną prośbę. Nowy styl = nowy preset, dopisany do dokumentacji.
4. **Każda zmiana → screenshot wszystkich breakpointów** (zwykle Desktop 1200 / Tablet 810 /
   Phone 390) i obejrzenie go.
5. **Branche:** jeśli plan Framera je obejmuje, pierwsza edycja AI tworzy branch — podaj link do niego
   w podsumowaniu. Jeśli nie obejmuje (sprawdź w `CLAUDE.md` projektu), zmiany idą od razu do głównej
   wersji: powiedz to wprost. **Nigdy nie merguj i nie publikuj** bez wyraźnego polecenia.
6. ID węzłów w replikach (Tablet/Phone) to ID złożone `<breakpoint><węzeł>` — nie
   wstawiaj nic do replik, tylko patchuj.

## Zasady treści (wspólne)

- Typograficzne cudzysłowy i apostrofy („ ” ’ “ ”), półpauza w zakresach lat (2019–2021).
- Każde nowe zdjęcie ma alt-text.
- Nie wymyślaj faktów o klientach (dat, nagród, danych kontaktowych). Brak danych → `TODO`
  i pytanie do użytkownika.

## Definition of done dla zmiany na stronie

- [ ] Zmiana obejrzana na screenshotach wszystkich breakpointów
- [ ] Brak diagnostyk/ostrzeżeń z `exec`
- [ ] Nowe obrazy mają alt-text, nowe linki mają `href` i `linkStylePreset`
- [ ] Mapa projektu (`framer-map.md`) zaktualizowana, jeśli zmieniła się struktura/ID
- [ ] Istotna decyzja dopisana do `decisions.md` projektu (data, decyzja, powód)
- [ ] Zamknięte/nowe punkty odhaczone w `backlog.md` projektu

## Utrzymanie tej wiedzy

Po każdej sesji, w której coś ustaliliśmy, **zaktualizuj odpowiedni plik w folderze
projektu** (w opisie commita podaj nazwę projektu, np. `ewa-dabrowska: …`).
Ten plik trzymaj krótki — szczegóły idą do folderów projektów.

## Zapisywanie zmian w repo — automatycznie, bez pytania

Użytkownik nie jest techniczny i **nie chce o tym pamiętać** (stała zgoda, 2026-11-14).
Zawsze, gdy w sesji zmieniły się pliki w repo, na koniec pracy (zanim oddasz głos) **sam**:

1. zrób commit i push na branch roboczy sesji;
2. otwórz pull request do domyślnego brancha repo (`claude/eloquent-cray-h16cwt`) i od razu
   go **scal** (merge) — bez pytania o zgodę;
3. jeśli przy scalaniu jest konflikt (np. równoległa sesja zmieniła te same pliki), rozwiąż go,
   zachowując zmiany obu stron; pytaj użytkownika tylko, gdy treści naprawdę sobie przeczą;
4. w podsumowaniu napisz jednym zdaniem, że zmiany są zapisane i widoczne dla kolejnych sesji.

To dotyczy **tylko notatek w tym repozytorium**. Zasada z sekcji o Framerze bez zmian:
**brancha we Framerze nigdy nie scalaj i strony nie publikuj** bez wyraźnego polecenia.
