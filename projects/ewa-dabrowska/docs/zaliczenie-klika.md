# Zaliczenie kursu KLIKA — lista wymagań

> Ta strona jest jednocześnie **projektem końcowym kursu KLIKA**. Żeby dostać zaliczenie,
> muszą być spełnione **wszystkie** poniższe punkty („Upewnij się, że projekt końcowy spełnia
> wszystkie poniższe założenia”).
>
> - **Wytyczne (źródło):** https://woolen-bit-4cb.notion.site/Projekt-ko-cowy-1d9dbf94db1080b68090ec7b99369b7a
>   — przepisane dosłownie ze screena strony (2026-11-15). Jeśli wytyczne się zmienią, zaktualizuj ten plik.
> - **Termin i sposób oddania:** _TODO_ — nie ma ich na stronie z wytycznymi; uzupełnić z kursu.

## Jak sprawdzić, co zostało

Napisz do Claude: **„Co mi zostało do zaliczenia KLIKA?”** — Claude przeczyta ten plik,
sprawdzi stan strony we Framerze (tylko odczyt), zaktualizuje statusy i poda listę.
Albo otwórz ten plik — **Podsumowanie** i **Do zrobienia** są na górze.

**Legenda:** ✅ spełnione · 🟡 częściowo / do dokończenia · ⬜ nie zaczęte · ❓ niesprawdzone — trzeba zajrzeć do Framera

## Podsumowanie (stan: 2026-11-15)

| ✅ Spełnione | 🟡 Częściowo | ⬜ Nie zaczęte | ❓ Do sprawdzenia | Razem |
|---|---|---|---|---|
| 8 | 6 | 4 | 3 | 21 |

> ⚠ Statusy z 2026-11-15 są ocenione **na podstawie dokumentacji w repo** (`framer-map.md`,
> `design-system.md`, `backlog.md`), a nie świeżego przeglądu Framera. Przed oddaniem zrób
> pełne sprawdzenie we Framerze.

### Do zrobienia — najważniejsze blokery

1. **Podstrona zalinkowana ze strony głównej** (#4) — dziś jest tylko Home. Podstrony są wstrzymane
   (decyzja z 2026-11-15) — do zaliczenia trzeba zbudować co najmniej jedną, np. **About**
   (link „Read more” z Home już na nią czeka).
2. **Layout Template z top-barem i stopką** (#11) — komponent Nav Bar istnieje, szablonu brak.
3. **Favicon i Social Image** (#17).
4. **aria-label dla linków bez tekstu** (#21) — ikony social, logo, „Back to top”; linki w ogóle
   trzeba najpierw podpiąć.
5. Sprawdzić we Framerze punkty ❓: wrappery z Max Width (#6), hover na przyciskach (#12),
   znaczniki HTML (#19).

## Wymagania

### Temat projektu i zawartość strony

| # | Wymaganie (dosłownie) | Stan | Dowód / gdzie to jest | Co jeszcze zrobić |
|---|---|---|---|---|
| 1 | Wybierz dowolny temat projektu, który ma sens. Może to być działający biznes twój lub twoich znajomych, własne portfolio, lub wymyślony przez ciebie projekt nieistniejącej inicjatywy (jak wszystkie nasze pliki robocze). | ✅ | Prawdziwa klientka — oficjalna strona artystki (`brief.md`) | — |
| 2 | Zgromadź content wizualny. Jeśli takowego nie posiadasz, polecamy korzystać z narzędzi AI – Midjourney bądź ChatGPT 4o. | 🟡 | Zdjęcia prac na Home (13 + portret); Google Drive artystki; CMS Works: 8 z 31 okładek | Zmniejszyć zdjęcia z Dysku i dodać do podstron/CMS (`backlog.md` P1) |
| 3 | Zredaguj teksty do strony. | 🟡 | Teksty Home (hero, About, Practice); fakty w CMS | Teksty podstron (np. About); opisy prac w CMS są puste |
| 4 | Zaprojektuj minimum stronę główną i jedną dodatkową podstronę, którą zalinkuj. (Podstron może być więcej). | ⬜ | Tylko Home (`framer-map.md`); podstrony wstrzymane 2026-11-15 | Zbudować min. 1 podstronę (np. About) i podlinkować z Home i menu |

### Design zgodny z dobrymi praktykami

| # | Wymaganie (dosłownie) | Stan | Dowód / gdzie to jest | Co jeszcze zrobić |
|---|---|---|---|---|
| 5 | Strona oparta jest na strukturze: Header, Main, Section, Footer. | 🟡 | Drzewo Home: nav-bar → Main `GI46d7Pmp` → sekcje Hero / Projects / About → footer-reveal (`framer-map.md`) | Potwierdzić we Framerze; podstrony też muszą mieć tę strukturę |
| 6 | Sekcje zawierają Wrappery z Max Width, które ograniczają skalowanie contentu na szerokim viewporcie. | ❓ | Brak informacji w dokumentacji | Sprawdzić sekcje Home na 1920 px; dodać wrappery, jeśli brak |
| 7 | Strona jest w pełni responsywna, przetestowana na rozdzielczości od 1920px do 390px. | 🟡 | 3 breakpointy; znany błąd: szare paski po bokach About (`backlog.md` P0) | Naprawić paski; przetestować 1920 / 1440 / 1200 / 810 / 390 (screenshoty) |
| 8 | Strona zawiera conajmniej 3 breakpointy. | ✅ | Desktop 1200 · Tablet 810 · Phone 390 (`framer-map.md`) | Nowe podstrony też z 3 breakpointami |
| 9 | Utworzone są responsywne style tekstowe, pod które podpięte są warstwy tekstowe. | 🟡 | 13 presetów z rozmiarami D / T / P (`design-system.md`) | Sprawdzić, czy **wszystkie** teksty mają preset (żadnych „luźnych” stylów) |
| 10 | Utworzone są style kolorystyczne, pod które podpięte są warstwy wykorzystujące kolor. | ✅ | Tokeny Ink / Paper / Line / Muted podpięte w 24 miejscach (2026-11-15) | Pilnować tokenów na nowych podstronach |
| 11 | Projekt musi zawierać komponenty – top-bar i footer, ujęte w Layout template. Więcej komponentów jest mile widziane. | ⬜ | Komponenty Nav Bar i Footer Bar są; **Layout Template brak** | Zrobić Layout Template z Nav Bar i stopką (`backlog.md` P1) |

### Efekty i animacje

| # | Wymaganie (dosłownie) | Stan | Dowód / gdzie to jest | Co jeszcze zrobić |
|---|---|---|---|---|
| 12 | Wszystkie przyciski mają mikrointerakcję na hover. | 🟡 | Linki w menu Nav Bar mają hover (opacity 0,5, 2026-11-20); reszty nie sprawdzono | Sprawdzić Nav Bar button, Contact, CTA w stopce; dodać stan Hover, jeśli brak |
| 13 | Zastosuj przynajmniej jedną animację typu Appear. | ✅ | 14 × Appear na Home Desktop (`framer-map.md`) | — |
| 14 | Zastosuj przynajmniej jedną animację typu Scroll Animate lub Scroll Transform. | ✅ | 14 × Scroll Transform + triggery scrolla na Home | — |
| 15 | Więcej animacji mile widziane. Tylko nie przedawkuj. | ✅ | Efekty scrolla w Projects, nav zmieniający wariant, footer reveal | Opcjonalne — nie dokładać na siłę |

### Ustawienia strony, dostępność i SEO

| # | Wymaganie (dosłownie) | Stan | Dowód / gdzie to jest | Co jeszcze zrobić |
|---|---|---|---|---|
| 16 | Strona ma wypełnione pole Title i Description w Settings. | ✅ | „Ewa Dąbrowska · Land Art & Sculpture” + opis (2026-11-15) | Podstrony: własne title / description |
| 17 | Dodana jest favikona i Social Image. | ⬜ | Brak (`backlog.md` P0) | Wybrać zdjęcie na Social Image i znak na favicon |
| 18 | Warstwy są ponazywane. | 🟡 | Główne warstwy Home mają nazwy (`framer-map.md`) | Przejrzeć wszystkie warstwy (też w komponentach) — bez „Frame”, „Text”, „Image” |
| 19 | Ustawione są znaczniki elementów header, nav, main, section, footer. | 🟡 | `header` na wrapperze paska i `nav` w komponencie Nav Bar (2026-11-20); main / section / footer niesprawdzone | Sprawdzić pole HTML Tag w Framerze dla nav-baru, Main, sekcji i stopki |
| 20 | Wszystkie obrazy mają swój alt-text. | ✅ | 13 zdjęć prac + portret na Home (2026-11-15); 6 grafik dekoracyjnych celowo bez opisu | Każde nowe zdjęcie z alt-textem (`content-guidelines.md`) |
| 21 | Wszystkie elementy linkujące bez etykiety tekstowej mają swój aria-label. | ⬜ | Linki w nav i stopce w większości niepodpięte (`backlog.md` P0) | Podpiąć linki; aria-label dla logo, ikon Instagram / Facebook, „Back to top” |

## Zasady aktualizacji

- Status zmieniaj tylko po **sprawdzeniu** (Framer, pliki w repo), nie z pamięci.
- Przy zmianie statusu dopisz datę w kolumnie „Dowód”, np. „✅ 2026-11-20 — favicon ustawiony”,
  i przelicz **Podsumowanie** (zmień też datę „stan:”).
- Punkty wymagające pracy na stronie są też w `docs/backlog.md` z dopiskiem **[KLIKA]**.
- Zaliczenie ma pierwszeństwo przy planowaniu: punkty ⬜ / 🟡 z tej listy to warunek oddania.
