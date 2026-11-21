# Mapa projektu Framer

> Snapshot: 2026-11-14 (gałąź `main`). ID węzłów pozwalają Claude od razu trafić w
> właściwe miejsce bez przeszukiwania całego drzewa. Aktualizuj po zmianach struktury.

## Strony

| Strona | ID | Ścieżka | Status | Layout Template |
|---|---|---|---|---|
| Home | `OQp6lSols` | `/` | opublikowana w projekcie | brak |

Design page (brudnopis): **Robocze** `juyxNVARq` — wersje robocze stopki, About,
„work-grid — B Index”, sticky-icon, read-more.

Na „Robocze” są też ramki z próbkami fontów do logo (2026-11-20): **Logo — próbki pisma odręcznego**
`G1f2KF0Xw` (18 cienkich) i **Logo — próbki: grubsza kreska** `hX2pKSrmR` (31 pędzelkowych / grubszych), **Logo — próbki: ekspresyjne**
`LvcJ1oVNL` (40 surowych, markerowych, graffiti) oraz **Logo — próbki: pióro / pędzel** `diU0NpTmC` (z pochyleniem i bez).

Design page: **Fonty — propozycje zamienników** `IC_Z5ffzI` — próbki darmowych fontów (2026-11-15).

Layout Templates: **brak** (wstrzymane). Skill Framera: **`ewa-brand`** `QIgqMpnwt` (on-demand).

## CMS (od 2026-11-15)

**Works** `jkOY2Zimh` — 31 prac (z `content/works.csv`, fakty po angielsku). Pola (ID):
Title `WzOlAO5cq` · Slug `QoWpilZnw` · Original title `y44E_IcMd` · Order `GVnHfz3yR` ·
Featured on Home `tG4628spA` · Year `q0COQSAiL` · Category `GLfRDJsQD` (enum: Land Art & Happenings
`ZY2J1ZJuX`, Sculpture `OLOMNw4U6`, Drawing & stop-motion `u7n5Amtxe`, Sound `kqMwgvwz7`) ·
Cover image `DxHd9Q0PN` · Gallery `NYI0ZAt_H` · Description `NM5SrvrVs` (puste) · Materials `iGwXHAKjU` ·
Dimensions `SSPzrvI4E` · Context `c28BHMS4b` · Collaborators `ZUuWu0sXo` · Location `CkNmLthkp` ·
Country `GYOtKiSnZ` · Can visit `bP3XnnkGZ` (puste) · Google Maps `rzQH2k1i0` · Video `Dy1n8eRUL` ·
Photo credit `NoEk5UhCp` · Photos source (Drive) `ICFIO1h2q`.

**Exhibitions** `T6szg68Z3` — 18 wystaw. Pola: Title `rqF5Iwx_r` · Slug `eiaa4zvBL` · Year (number)
`VzrrcKmZt` · Venue `N7AuqP9nD` · City `p75Rs9FWW` · Country `qQ9KgIhrq` · Type `VtyAOyIX1` (Solo,
Group, International, Festival, Open-air) · Link `mM2hTlwr3`.

## Nav Bar `ECLoOCCHr` — menu pełnoekranowe (2026-11-20)

Komponent (bez overlay, bez custom code). Root wariantu = `<nav>`, pionowy stack, padding `0 16px`, overflow clip.
- **Warianty zamknięte:** Desktop White `PKP79zZJ_` (primary), Desktop Black `SdizDLgxu`, Tablet White
  `lOwMG1XiX`, Tablet Black `mCSjiTuhs`, Phone White `i2tgDvjkO`, Phone Black `Ii_PrCq2k` (dawne „Mobile”).
- **Warianty otwarte:** Desktop Open `ie2h56T5S`, Tablet Open `QU72InY3n`, Phone Open `gBUFzCXNV` —
  tło token **Night** `y6um7al0w` (#1B1B1B), `minHeight: 100vh` (Framer nie przyjmuje `height: 100vh` na
  wariancie komponentu), przejście tween 0,6 s.
- Struktura: `UlU0nzIq3` nav-row (linia dolna 0,5 px; od 2026-11-20 trzy części: `DleEx3DjC` nav-row-left 1fr
  z hamburgerem `OOgm1RAxl` · logo `iyXc2Haid` → `/` **na środku** (od 2026-11-20: **12 osobnych liter** + odstęp `pAS1B9MpM`, każda z własnym
  obrotem / przesunięciem / skalą, preset Logo Script, w Black — Logo Script Dark; ramka pochylona −8°;
  stary tekst `kAw3N4j00` usunięty 2026-11-20;
  dawny logotyp SVG był maską ramki: `uSAvd2qsAvbTUDNT5VcSshybTF4.svg`) · `VW7CEorPF` nav-row-right 1fr z przyciskiem
  Contact `eVB1wQuPY` = instancja „Nav bar button outlined” `flntBxkgE`, bez linku) →
  `tHAjPmZye` nav-menu (ukryte w zamkniętych, widoczne w Open; od 2026-11-20 wg szkicu `JfmuN1_YU` na stronie „Robocze”):
  - `TeGGXVBLU` nav-list — wyśrodkowana kolumna (gap 48 / 40 / 28 px): Work `E00Wq41qe`, Exhibitions `YRqINZHOg`,
    About `KOSrIErZS`, Contact `dq03FGQzu`, Publications `m6Fj5zoMG`; tekst presetem **Nav Primary 2** `iESRe_5Uf`
    (wersaliki), pod każdym „bar-line” na całą szerokość (ręcznie rysowana linia — maska SVG jak w Footer Bar).
  - `WQcXBeASU` nav-menu-footer: socials `BwpZKSPeb` (Instagram, Facebook) po lewej, `VZn4ZDpNd`
    „© 2026 Ewa Dąbrowska. All rights reserved.” po prawej (na telefonie pod sobą).
  - W Open ukryte: logo i przycisk Contact w pasku; widoczny EN / PL `iYrl_UOC4` w prawym górnym rogu
    (w `VW7CEorPF`); linia pod paskiem przezroczysta. **Performance usunięte z menu** (decyzja Piotra).
  - Każdy link to ramka z hover (opacity 0,5). **Linki bez `href`**; social bez URL.
- **Zasady budowy paska (2026-11-20, po nagraniu Piotra):** górny wiersz `UlU0nzIq3` ma **ten sam układ we
  wszystkich 9 wariantach** — logo, Contact i EN / PL są zawsze w warstwach, a w wariantach przełącza się tylko
  **opacity** (+ `pointerEvents: none`), nigdy `visible`. Dzięki temu wysokość paska i linia pod nim się nie
  ruszają przy otwieraniu. EN / PL `iYrl_UOC4` leży **absolutnie** na miejscu przycisku Contact (prawa kolumna
  `VW7CEorPF`, piny prawo/góra/dół) — przenika się z Contact zamiast wjeżdżać z boku. Padding wiersza: desktop
  15/20 px, tablet/telefon 11/0 px.
- **Hamburger:** obszar kliknięcia 44×44 px (linie bez zmian, przy lewej krawędzi), `ariaRole: button`, `tabIndex 0`, aria-label „Open menu” / „Close menu”. Klik (`onTap` →
  SET_VARIANT): White/Black → Open danego rozmiaru; Open → White. W Open linie (`ERKAKLz7L`, `kEFBSpbbT`)
  mają translateY ±3,5 px → jedna pozioma kreska.
- Na Home: wrapper `zbBVXvrUI` (`<header>`, absolute, left/right 0, z-index 10), instancja `xLcWXJD7r`
  przełącza przy scrollu White/Black (desktop: Desktop, **tablet: Tablet White/Black**, telefon: Phone).
- W komponencie leży też ramka `GkUviYHV8` „OLD — stara wersja paska (nieużywana)” — kopia Piotra; Framer nie
  pozwala przenieść jej poza komponent. Można ją usunąć, gdy nie będzie potrzebna.

## navi-top `TResx8GqO` — nowy pasek z menu „roletą” (2026-11-21)

Na Home: instancja `OIeRrf3DF` (fixed, z-index 10, szerokość 1200 px). Warianty: **navi-open** `uSok_Ju8O`
(primary, wysokość z rozpórki) i **navi-closed** `lmfEqZApa` (74 px). Oba bez tła, overflow clip.
- `kNqO7Bcte` top-bar-container (absolute, góra, 74 px, z-index 1) — hamburger, logo, Contact / EN-PL, Navi-line.
- `rYB7_toMi` „100vh” — pusta rozpórka (relative, 100vh); bez niej otwarte menu spada do 200 px.
- `OPG86_Pmg` menu-panel (absolute L/R/B, 100vh, Night, z-index 0; navi-closed: Bottom 74 px) →
  `CWJfR8V2e` links-100vh → maski `pp24mHNlQ`, `DAc3ac1EX`, `s5M6MGcR1`, `eIxos2ptA` z linkami
  (work `OtV__FjxS`, nav-primary-button `irKeFJFBu`, `HjwH49EAE`, `N8wcphCcb`) + `NHjiomG5_` footer (absolute, dół).
- Szczegóły animacji: `decisions.md` (2026-11-21, „roleta”).
- ⚠ W komponencie leży luźna stara ramka „Desktop Open” (`o7uYvB9DP`); jej hamburger ma akcję Set Variant do
  nieistniejącego wariantu (błąd w diagnostyce Framera) — do usunięcia razem z ramką.

## Home — breakpointy

| Breakpoint | ID |
|---|---|
| Desktop Large Primary (1200) | `jKwXMbO36` |
| Tablet (810) | `YinCLfjHu` |
| Phone (390) | `dHjtNw9CS` |

Węzły w replikach mają ID złożone, np. Hero na Phone = `dHjtNw9CS` + `MbHe0i_sG`.

## Home — drzewo (Desktop)

```
jKwXMbO36  Desktop Large Primary (fill #000, stack vertical)
├─ nMDvE6f04  lenis (Lenis)
├─ zbBVXvrUI  nav-bar-scroll → xLcWXJD7r nav-bar-scroll-inner (Nav Bar)
├─ O63VKWwFo  footer-bar-fixed (Footer Bar)
└─ GI46d7Pmp  Main
   ├─ MbHe0i_sG  Hero            #hero      100vh, tło token Night (warstwy uporządkowane 2026-11-21)
   │    xFXsEh5DM „Stwór 6” — zdjęcie na całe hero (absolute, piny 0/0/0/0, z-index 1, alt-text)
   │    ycitzB0yn photo-dim — przyciemnienie (Ink; opacity ustawiona przez Piotra), nad zdjęciem, pod tekstem
   │    z2KrpmppH wrapper (z-index 2, max 1200) → PRqOQDz7Q typo:
   │      cpclYQakr eyebrow-group → XWLFp0Xq3 hero-eyebrow „a tender look beyond” (Hero Eyebrow) + ZVLMQ7A1h bar-line
   │      e0N8XfIys heading-01 → fSAxILuDe (h1) „Land art, sculpture, and sound” (Hero Statement, max 960 px)
   │    **Sekwencja wejścia:** hasło 0,3 s (Text Effect linia po linii: fade, 36 px w górę, blur 6 px, 1,1 s,
   │    co 0,15 s) → razem z paskiem nav (1,6 s): eyebrow (fade + 14 px w górę, 1 s) i linia (fade + skala
   │    0,2→1, 1 s). Przy zmianie opóźnienia paska (`xLcWXJD7r`) zmień też te dwa.
   │    B9kXdfngL scroll-arrow · QuXEKed3G socials (qJK7mwyTh Facebook, zztZovkXY Instagram)
   │    Usunięte 2026-11-21 (wyłączone na wszystkich breakpointach): heading-02 „& Sculpture”, stare
   │    „photo wrapper” z wyciętym zdjęciem rzeźby.
   ├─ a4blNq1t9  Projects-pasek sticky (59px) — vd9XkMmi0 „Explore projects”
   ├─ vwdTZARvA  Projects        #work (Scroll runway RPSCNyuOK)
   │    EBDMHlsbW intro „A multidisciplinary art…” · pky5JYXw5 Intro Subtext
   │    podpisy: Oj16NppMH Płaskorzeźba · tZPu6cFZr Słoneczny Stwór ·
   │             i2N136b3V Państwo Gąbczakowie · cry8ujNyS Herd (= „Dziki”, slug `herd`)
   │    F9wbx7YX3 wszechkarmicielka-video (Video)
   └─ WsnqpbDjZ  footer-reveal-wrap
        ├─ vJjOZlmbG About  #about — jOjY0LRDG „My Journey”, WofT2fgDc cytat,
        │     Practice: jmcxRpJ7U / xcfzwDUar / tGNhInyzO / Mi6naZeIe,
        │     DJOzTCWGP „Read more” + Dn5XeEUW7 Read More Underline
        └─ stopka: XX1mW0A7e „Get in touch”, mTqFRSUk0 e-mail,
              kolumny Menu / Contact / Legal, xCRqk8oKn Back to top (href „/”)
```

## Warstwy (z-index) na Home — stan 2026-11-20

Dzieci breakpointu (jeden kontekst nakładania, wszystkie breakpointy bez nadpisań):
`zbBVXvrUI` nav-bar-scroll **10** (absolute, u góry strony) > `O63VKWwFo` footer-bar-fixed **9** (fixed, góra
ekranu, `pointerEvents: none`) > `GI46d7Pmp` Main **8** (relative).
⚠ Footer Bar musi mieć wyższy z-index niż Main — przy równych wartościach Main (późniejszy w kolejności)
przykrywa pasek i ten „nie wysuwa się” (zob. decisions.md 2026-11-20).
Z-indeksy wewnątrz Main (np. sticky pasek About `sHRNN4Tvd` = 11) działają tylko w obrębie Main.

## Kotwice i triggery scrolla (nie usuwać / nie zmieniać `elementId` bez potrzeby!)

| elementId | Węzeł | Rola |
|---|---|---|
| `hero` | `MbHe0i_sG` | sekcja Hero |
| `work` | `RPSCNyuOK` | Scroll runway sekcji Projects |
| `intro-drift-start`, `intro-drift-range` | `T6L4lW1Dn`, `V5E8g6o5q` | dryf tekstu intro |
| `outro-text-start`, `subtext-switch-2`, `outro-text-range` | `ic_jEqNBV`, `inbImJfKA`, `g0NW1oRvX` | podmiana/wysuw subtextu |
| `projects-bar-hide` | `OuREZSX6m` | chowanie sticky paska |
| `depth-entry-range`, `depth-pin-range`, `depth-exit-range` | `c5UF32hjk`, `NTao4VVko`, `hQgWpsbXb` | wejście / przypięcie / wyjście zdjęć |
| `about` | `vJjOZlmbG` | sekcja About |
| `footer-revealed` | `mHZutgMyh` | marker odsłonięcia stopki |

Efekty na Desktop: 14 × appearEffect, 14 × styleTransformEffect.

## Inne ustawienia

- Custom code (plugin API, site-wide, head): `html, body { overscroll-behavior: none; }`
- Metadane strony: tytuł „Ewa Dąbrowska · Land Art & Sculpture” + opis (2026-11-15). Brak OG i favicon.
- Tokeny kolorów: Ink `dLrIqbBXT`, Paper `y2ty1fQ3X`, Line `Lgw6mIbcg`, Muted `NidFX33fI` (+ starszy `Black`).
- Plan Framera **bez branchy** — zmiany od razu w głównej wersji (zob. decisions.md).
- Publikacja: status „ready”, cel: production, brak URL produkcyjnego, staging wyłączony.
