# Mapa projektu Framer

> Snapshot: 2026-11-14 (gałąź `main`). ID węzłów pozwalają Claude od razu trafić w
> właściwe miejsce bez przeszukiwania całego drzewa. Aktualizuj po zmianach struktury.

## Strony

| Strona | ID | Ścieżka | Status | Layout Template |
|---|---|---|---|---|
| Home | `OQp6lSols` | `/` | opublikowana w projekcie | brak |

Design page (brudnopis): **Robocze** `juyxNVARq` — wersje robocze stopki, About,
„work-grid — B Index”, sticky-icon, read-more.

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

## Nav Bar `ECLoOCCHr` (opis z 2026-11-15)

> **Stan odczytany 2026-11-20 (ręczne zmiany na canvasie):** „Where to see” już nie ma — węzeł `kqmsI6XdP`
> ma teraz tytuł **„Awards”**. Exhibitions, Film / Performance i Publications / Press są **ukryte**
> (`visible: false`) we wszystkich 4 wariantach. Widoczne: Work, About, Awards (+ Contact, EN / PL).
> To odbiega od ustalonego menu (6 pozycji, bez Awards) — czeka na decyzję Piotra.


Warianty: Desktop White `PKP79zZJ_`, Mobile White `i2tgDvjkO`, Desktop Black `SdizDLgxu`, Mobile Black `Ii_PrCq2k`.
- Nav-right `TtQqBfySi` (szerokość auto, gap 32px; mobile 20px) → nav-links `lDGdXylue`:
  Work, `YLvlX7Zs1` · ~~Where to see~~ → „Awards” `kqmsI6XdP` (2026-11-20) · Exhibitions, `OToj1MVWj` · Film / Performance,
  `i2IyH4QtE` · Publications / Press, `vOfp1_xvb` · About `UJdoV6Oz2` (instancje Nav Bar button, w
  wariantach Black — wariant „Black”); Contact `LtsS5yjgf`; **EN / PL** `gB3ixSUcy` (EN `ZMOZgDB6s`,
  „/” `QPrvRHUsm`, PL `IcWUDMV8x`); hamburger `OOgm1RAxl` (tylko mobile, nie działa).
- Logo `iyXc2Haid` → link `/`. Pozostałe linki: brak (czekają na podstrony).
- Na Home instancja `xLcWXJD7r` przełącza warianty przy scrollu (hero → White, #work → Black);
  **tablet `YinCLfjHuxLcWXJD7r` używa wariantów Mobile** (jak telefon).

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
   ├─ MbHe0i_sG  Hero            #hero      100vh, padding 60/40/0/40
   │    teksty: fSAxILuDe „Land-Art” · gxakAEnqL „& Sculpture” · RZ0QS_xoY podtytuł
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
