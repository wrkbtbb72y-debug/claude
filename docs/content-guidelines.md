# Zasady treści

## Język

- ✅ **Ustalone (2026-11-14):** projekt powstaje **najpierw po angielsku**; wersja **polska**
  dochodzi pod koniec prac jako druga wersja językowa z przełącznikiem (lokalizacja Framera).
- Na tym etapie piszemy i redagujemy copy po angielsku. Teksty polskie zbieramy w `content/`
  (`description_pl`, `bio.md`), ale nie wstawiamy ich na stronę przed etapem PL.
- Tytuły prac: oryginalny polski tytuł jest nadrzędny (np. „Słoneczny Stwór”); w wersji EN
  pokazujemy tytuł angielski, a polski oryginał jako podtytuł/w opisie — _do potwierdzenia
  w projekcie_.
- Nazwy w menu są robocze, po angielsku: Work · Where to see · Exhibitions · Film / Performance ·
  Publications / Press · About · Contact.

## Ton

- Uważny, poetycki, konkretny. Krótkie zdania. Zero marketingowego żargonu
  („innowacyjny”, „unikalny”, „pasja”).
- Głos artystki w 1. osobie w sekcji About („My Journey”); opisy prac — rzeczowo, w 3. osobie
  lub bezosobowo. _Potwierdzić z artystką._

## Typografia w tekstach

- Cudzysłowy: EN “…” ‘…’, PL „…” ‚…’. Apostrof: ’ (nie ').
- Zakresy lat: półpauza bez spacji — 2019–2021. Myślnik w zdaniu: spacja – spacja (PL) / em dash — (EN).
- Wielkie litery w tytułach EN: Title Case tylko dla nazw sekcji; tytuły prac w oryginalnej pisowni.

## Nazewnictwo prac (spójne z `content/works.csv`)

- `title_pl` — tytuł oryginalny (nadrzędny), `title_en` — tłumaczenie.
- `slug` — z tytułu oryginalnego, bez polskich znaków, kebab-case: `sloneczny-stwor`.
- Kategoria — dokładnie jedna z 4 z sekcji Practice:
  `Land Art & Happenings` · `Sculpture` · `Drawing & stop-motion` · `Sound`.

## Alt-teksty (obowiązkowe)

Wzór: **[Tytuł], [rok] — [co widać / materiał / kontekst].** Max ~125 znaków.

- ✅ „Słoneczny Stwór — postać ze słomy z twarzą słońca na tle drzew”
- ✅ „Herd (Dziki) — rzeźby dzików z patyków ustawione w lesie”
- ❌ „zdjęcie”, „IMG_2034”, „rzeźba”

Zdjęcia czysto dekoracyjne (tekstury, tła) — alt pusty, ale świadomie.

## Fakty

Nie wymyślamy dat, materiałów, wymiarów, miejsc, nagród, wystaw. Brak danych → `TODO`
w `content/` i pytanie do Piotra/artystki.
