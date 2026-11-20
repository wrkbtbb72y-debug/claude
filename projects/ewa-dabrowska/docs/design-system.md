# Design system

> Snapshot z Framera: 2026-11-14. Źródło prawdy to Framer — ten plik jest mapą.
> Jeśli dodasz/zmienisz preset, token albo komponent, zaktualizuj ten plik.

## Kierunek wizualny

- **Ciemna galeria:** tło `#000`, tekst biały; sekcja Projects ma jasne tło, na którym
  „pływają” zdjęcia prac w różnych skalach (asymetryczna kompozycja, głębia przez scroll).
- **Akcent = fotografia**, nie kolor. Nie wprowadzamy kolorów akcentowych bez decyzji.
- **Typografia katalogowa:** ogromny szeryf (Instrument Serif 132px, interlinia 80–110%)
  vs. drobny, techniczny grotesk (ABC Diatype 14–15px).
- **Ruch:** płynny scroll (Lenis), efekty scroll-transform i appear (po 14 węzłów na Home),
  stopka typu „reveal”, sticky pasek „Explore projects”. Ruch jest częścią tożsamości —
  zmiany w sekcjach z triggerami robić ostrożnie (zob. framer-map.md).

## Breakpointy

| Nazwa | Szerokość | Zakres |
|---|---|---|
| Desktop Large (primary) | 1200px | ≥ 1200px |
| Tablet | 810px | 810–1199.98px |
| Phone | 390px | ≤ 809.98px |

Kontener nawigacji: 1168px (16px marginesu na 1200). Hero: padding `60px 40px 0 40px`.
Pasek „Explore projects”: wysokość 59px, padding poziomy 100px.

## Kolory

| Token / wartość | Gdzie | Uwagi |
|---|---|---|
| `Black` token — `rgb(31,31,31)` (ID `0397fb76-20a8-4fdc-ba50-854349caca2b`) | tekst na jasnym tle | starszy token |
| **Ink** `dLrIqbBXT` — `#000000` | tło strony, hero, About, logo w wariantach Black | token (2026-11-15) |
| **Paper** `y2ty1fQ3X` — `#FFFFFF` | tekst/elementy na ciemnym, tło Projects | token |
| **Line** `Lgw6mIbcg` — `rgb(196,196,196)` | stopka, linie | token |
| **Muted** `NidFX33fI` — `rgb(122,121,121)` | podpisy (preset Caption) | token |
| `rgba(255,255,255,0.6)` | podtytuł hero | w presecie |
| **Night** `y6um7al0w` — `#1B1B1B` | tło otwartego menu (Nav Bar Open) | token (2026-11-20) |

Nowe elementy: używaj tokenów zamiast surowych wartości. Półprzezroczyste kolory (np. biel 60%) zostają w presetach.

## Typografia — presety tekstu

| Preset | ID | Font | Rozmiar D / T / P | Interlinia | Rola |
|---|---|---|---|---|---|
| Heading 1 Narrow | `j1PLXPFTE` | Instrument Serif 400 | 132 / 100 / 56 | 80% | Hero, linia 1 („Land-Art”) |
| Heading 1 Wide | `p91ikxZED` | Instrument Serif 400 | 132 / 92 / 56 | 110% | Hero, linia 2 („& Sculpture”) |
| Body 2 Instrument | `pHLTmOCkW` | Instrument Serif 400 | 18 / 16 | 140% | Podtytuł hero (biel 60%) |
| Intro Quote | `DNPvqvyeg` | ABC Arizona Mix Condensed 300 | 34 / 30 / 24 | 120% | Intro, cytat w About |
| Practice Title | `oiJIGsspQ` | ABC Arizona Mix Condensed 300 | 24 / 22 | 120% | Pozycje listy Practice |
| Contact Email | `nwEhFmtSs` | Instrument Serif 400 | 56 / 36 / 30 | 1.15em | E-mail w stopce |
| Heading 2 | `OlIghTzTc` | ABC Diatype 400 | 18 / 16 / 15 | 100% | „Get in touch” |
| Heading 3 | `EIxkWzKdw` | ABC Diatype 400 | 15 | 140% | Etykiety sekcji („Explore projects”, „My Journey”) |
| Heading 4 | `ZFoPtf4uS` | ABC Diatype 400 | 14 | 140% | Małe nagłówki („Practice”) |
| Meta | `jlhfHVuRU` | ABC Diatype 400 | 15 | 140% | Metadane |
| Caption | `q8a80OhDX` | ABC Diatype 400 | 14 | 140% | Podpisy pod zdjęciami prac |
| links | `sAkSZeyYk` | ABC Diatype 300 | 14 | 145% | Linki („Read more”, social) |
| footer small | `VPJZTLXqN` | ABC Diatype 300 | 14 / 13 | — | Stopka |
| Nav Primary | `g8gsJNo38` | Instrument Serif 400 | 88 / 72 / 52 | 100% | Nieużywany od 2026-11-20 (zastąpiony przez Nav Primary 2) |
| Nav Secondary | `N3PQzeLo4` | Instrument Serif 400 | 24 / 22 / 20 | 120% | Nieużywany od 2026-11-20 (wcześniej linki secondary) |
| Hero Statement | `QNTM_UWmf` | Instrument Serif 400, wersaliki, odstęp 0,01em | 52 / 44 / 32 | 110% | Hasło w hero (h1), wyśrodkowane |
| Logo Script | `lBfVEdHOq` | Rock Salt 400 (Google Fonts, Apache 2.0) + kontur 0,6 (Paper) dla grubszej kreski | 20,8 / 19,2 / 15,2 | 1.4em |
| Logo Script Dark | `Tz0N5j_mX` | jak wyżej, kolor i kontur Ink | 20,8 / 19,2 / 15,2 | 1.4em | Logo „Ewa Dąbrowska” w pasku (Ink w wariantach Black) |
| Nav Primary 2 | `iESRe_5Uf` | Instrument Serif 400, wersaliki | 80 / 72 / 52 | 100% | Linki w otwartym menu (Work … Publications) — styl Piotra ze szkicu |

Link style: `Contact Email Link` (`JrZOvXHMr`).

**Fonty w użyciu:** Instrument Serif (Google, OK), ABC Diatype **Trial**,
ABC Arizona Mix Condensed **Unlicensed Trial**, Syne, Inter.
⚠ Wersje Trial nie są licencjonowane do produkcji — zob. backlog P0.

## Komponenty

| Komponent | ID | Warianty | Użycie |
|---|---|---|---|
| Nav Bar | `ECLoOCCHr` | Desktop / Tablet / Phone × White, Black, Open | Górny pasek: logo + hamburger; po kliknięciu wariant Open = menu na cały ekran (zob. framer-map.md) |
| Nav Bar button | `RQhfdR2vS` | Variant 1, Black (+ gesty) | Przycisk w nawigacji; zmienna `Title` |
| Nav bar button outlined | `flntBxkgE` | Variant 1 (+ gesty) | Obrysowany przycisk („Contact”) |
| Footer Bar | `CZImlwXQG` | Desktop/Phone × Hidden/Visible | Stały pasek na dole (pojawia się przy scrollu) |
| Intro Subtext | `dLnxv11ux` | 1, 2 | Podmieniany tekst w intro (blend „difference”) |
| Read More Underline | `WMRFPcODi` | Hidden, Drawn | Animowane podkreślenie „Read more” |

Zewnętrzne: **Lenis** (smooth scroll), **Video** (np. „wszechkarmicielka-video”),
override **withLinksAfterSection**.

Ikony: zestaw z ikonami `Copy`, `Arrow Down`, `Facebook`, `Instagram` (+ własne wektory „arrow big”).

## Zasady przy rozbudowie

- Nowe sekcje: tło czarne lub białe, etykieta sekcji presetem **Heading 3** + linia
  pozioma (jak „Explore projects” / „My Journey”).
- Listy numerowane: wzór Practice (numer 01–04 drobnym groteskiem + tytuł **Practice Title**,
  separator linią).
- Podpisy zdjęć: zawsze **Caption**, oryginalny tytuł pracy.
- Brak zaokrągleń, brak cieni — estetyka płaska, drukowa.
- Nawigacja i stopka powinny trafić do **Layout Template** zanim powstaną kolejne strony.
- **Nav Bar musi mieć miejsce na przełącznik języków EN / PL** (desktop i menu mobilne) oraz na
  logotyp „Ewa Dąbrowska” + przyszły znak artystki. Docelowo 6 pozycji menu (zob. brief.md).
- **Menu = wariant komponentu, nie overlay** (2026-11-20). Nowe pozycje menu dodawaj w `nav-menu` wariantu
  primary (Desktop White) — trafią do wszystkich wariantów.
