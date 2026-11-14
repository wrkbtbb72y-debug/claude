# Treści i dane

## `works.csv` — baza prac

Jeden wiersz = jedna praca. Schemat odpowiada planowanej kolekcji CMS „Works” we Framerze.

| Kolumna | Typ w CMS | Opis |
|---|---|---|
| `order` | number | ręczna kolejność na podstronie Work (1 = pierwsza). Ustalone: 1 „Słoneczny Stwór”, 2 „Tancerz”, 3 „Dziki”; reszta wg wyczucia projektanta |
| `slug` | slug | z tytułu oryginalnego, bez polskich znaków, kebab-case |
| `title_pl` | string | tytuł oryginalny (nadrzędny) |
| `title_en` | string | tłumaczenie tytułu |
| `year` | string | rok lub zakres `2019–2021` |
| `category` | enum | `Land Art & Happenings` · `Sculpture` · `Drawing & stop-motion` · `Sound` |
| `materials` | string | np. „słoma, drewno” |
| `dimensions` | string | np. „220 × 90 × 80 cm” lub „site-specific” |
| `location` | string | miejsce realizacji / wystawy (nazwa miejscowości / miejsca) |
| `maps_url` | link | link z Map Google — do mapy „Where to see” i bloku „Gdzie zobaczyć” |
| `can_visit` | enum | `yes` (można zobaczyć na żywo) · `gone` (praca efemeryczna, już nie istnieje) · `private` (prywatny ogród / niedostępne). Sposób pokazywania `gone` i `private` na mapie — **czeka na decyzję artystki** |
| `description_pl` / `description_en` | richtext | 2–5 zdań |
| `images` | array (galeria) | nazwy plików/URL; pierwszy = okładka |
| `featured` | boolean | czy pokazywać na Home |
| `on_site` | — | gdzie praca jest teraz użyta na stronie (pomocnicze, nie do CMS) |
| `status` | — | `draft` (brak danych) / `ready` (komplet, zaakceptowane) / `live` (w CMS) |

Wiersze startowe pochodzą z podpisów na Home (stan 2026-11-14). Wszystko oznaczone `TODO`
wymaga danych od artystki — Claude **nie zgaduje** faktów.

Wymagane do publikacji (`ready`): `slug`, `title_pl`, `title_en`, `year`, `category`,
`images`, alt-tekst dla okładki.

## Pozostałe pliki

- `bio.md` — biogram (krótki/długi, PL/EN), CV.
- `awards-press.md` — nagrody, wystawy, publikacje prasowe.
