# Mapa projektu Framer

> Snapshot: 2026-11-14 (gałąź `main`). ID węzłów pozwalają Claude od razu trafić w
> właściwe miejsce bez przeszukiwania całego drzewa. Aktualizuj po zmianach struktury.

## Strony

| Strona | ID | Ścieżka | Status | Layout Template |
|---|---|---|---|---|
| Home | `OQp6lSols` | `/` | opublikowana w projekcie | brak |
| Home (stara kopia) | `PkrJvvJdu` | `/home` | **draft** | brak |

Design page (brudnopis): **Robocze** `juyxNVARq` — wersje robocze stopki, About,
„work-grid — B Index”, sticky-icon, read-more.

CMS: **brak kolekcji.** Layout Templates: **brak.**

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
   │             i2N136b3V Państwo Gąbczakowie · cry8ujNyS Herd (= „Dziki”, slug `dziki`)
   │    F9wbx7YX3 wszechkarmicielka-video (Video)
   └─ WsnqpbDjZ  footer-reveal-wrap
        ├─ vJjOZlmbG About  #about — jOjY0LRDG „My Journey”, WofT2fgDc cytat,
        │     Practice: jmcxRpJ7U / xcfzwDUar / tGNhInyzO / Mi6naZeIe,
        │     DJOzTCWGP „Read more” + Dn5XeEUW7 Read More Underline
        └─ stopka: XX1mW0A7e „Get in touch”, mTqFRSUk0 e-mail,
              kolumny Menu / Contact / Legal, xCRqk8oKn Back to top (href „/”)
```

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
- Metadane strony głównej: **domyślne** („My Framer Site” / „Made with Framer”) — backlog P0.
- Publikacja: status „ready”, cel: production, brak URL produkcyjnego, staging wyłączony.
