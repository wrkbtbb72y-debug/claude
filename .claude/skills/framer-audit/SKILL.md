---
name: framer-audit
description: Read-only audit of the Ewa Dąbrowska Framer site before publishing or at the start of a work session — checks SEO metadata, alt texts, links, drafts, font licensing, design-system drift and scroll anchors, then updates docs/backlog.md. Use when the user asks for an audit, a pre-publish check, "co jest do poprawy", or a status of the site.
---

# Audyt strony Framer (tylko odczyt)

Nie wprowadzaj żadnych zmian we Framerze w trakcie audytu.

1. Przeczytaj `docs/backlog.md`, `docs/framer-map.md`, `docs/design-system.md`.
2. `mcp__Framer__open_project` z linkiem z `CLAUDE.md`. W **jednym** programie `exec`
   (read-only) zbierz:
   - sitemap (`WebPageNode`: path, draft, metadata.title/description), metadane `tree.root`;
   - obrazy bez `altText` (węzły z `fill` będącym asset reference) — liczba per strona;
   - węzły tekstowe/przyciski wyglądające na linki bez `link.href` (nav, stopka);
   - fonty presetów (`TextStylePresetNode.fontName`) zawierające „Trial” lub „Unlicensed”;
   - kolory użyte bez tokenów (surowe `fill`/`textColor`) vs `ColorStyleTokenNode`;
   - czy wszystkie `elementId` z tabeli kotwic w `docs/framer-map.md` nadal istnieją;
   - komponenty / presety, których nie ma w `docs/design-system.md` (drift dokumentacji);
   - `api.publishing.status()` — błędy i ostrzeżenia.
3. Zrób screenshoty Home na 3 breakpointach i obejrzyj je (ucięty tekst, nakładanie,
   puste sekcje).
4. Raport dla użytkownika po polsku: **co się zmieniło od ostatniego audytu**, nowe
   problemy, rozwiązane problemy. Krótko, z priorytetami P0/P1/P2.
5. Zaktualizuj `docs/backlog.md` (odhacz rozwiązane z datą, dopisz nowe) oraz
   `docs/framer-map.md` / `docs/design-system.md`, jeśli wykryto drift. Zaproponuj commit.
