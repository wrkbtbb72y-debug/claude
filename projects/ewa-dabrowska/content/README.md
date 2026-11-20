# Treści i dane

## Skąd są dane

- **Google Drive projektu** (portfolio, zdjęcia Ewy, zdjęcia prac):
  https://drive.google.com/drive/folders/1ODdjKarffSbNv4YrUwelKkm0PLBD317T
  - `zdjęcia/portfolio_Ewa_Dąbrowska.pdf` — portfolio z 09.2026 → przepisane do `sources/portfolio-2026-09.md`
  - `zdjęcia/WhatsApp Image 2026-10-03 …` (2 pliki) — zdjęcia Ewy (portret) — _do potwierdzenia, które na About_
  - `zdjęcia/images/<praca>/` — 13 folderów ze zdjęciami prac (72 pliki, stan 2026-11-14)
- `sources/` — przepisane materiały źródłowe (słowa artystki). Nie edytujemy ich; redakcje idą do `works.csv` / `bio.md`.

## `works.csv` — baza prac

Jeden wiersz = jedna praca (31 wierszy, stan 2026-11-14). Schemat odpowiada planowanej kolekcji
CMS „Works” we Framerze. Wypełnione wyłącznie faktami z portfolio i z nazw plików na Dysku.

| Kolumna | Typ w CMS | Opis |
|---|---|---|
| `order` | number | ręczna kolejność na Work (1 = pierwsza). Ustalone: 1 „Słoneczny Stwór”, 2 „Tancerz”, 3 „Herd” (Dziki); reszta wg wyczucia projektanta |
| `slug` | slug | z tytułu oryginalnego, bez polskich znaków, kebab-case |
| `title_pl` / `title_en` | string | tytuł oryginalny (nadrzędny) / angielski |
| `year` | string | rok lub zakres `2020–2023` |
| `category` | enum | `Land Art & Happenings` · `Sculpture` · `Drawing & stop-motion` · `Sound` — **przypisane przez Claude jako propozycja, do weryfikacji** |
| `materials` | string | materiały / technika |
| `dimensions` | string | wymiary lub opis skali |
| `location` / `country` | string | miejsce realizacji / wystawy; kraj (do mapy i filtrów) |
| `context` | string | festiwal, rezydencja, wystawa, zamówienie, stypendium |
| `collaborators` | string | współautorzy (np. Jan Sajdak) |
| `can_visit` | enum | `yes` · `gone` (efemeryczna, nie istnieje) · `private` — **czeka na artystkę** |
| `maps_url` | link | link z Map Google — do mapy prac (Exhibitions) |
| `video_url` | link | film (YouTube) — także do podstrony Film / Performance |
| `photos_drive` | link | folder ze zdjęciami na Dysku |
| `photo_credit` | string | autor zdjęć — **obowiązkowo podawać na stronie** |
| `description_pl` | richtext | `portfolio` = tekst artystki jest w `sources/portfolio-2026-09.md`; `—` = portfolio nie ma opisu; `TODO` = brak |
| `description_en` | richtext | tłumaczenie/redakcja (strona powstaje najpierw po angielsku) |
| `featured` | boolean | na stronie głównej |
| `on_site` | — | gdzie praca jest teraz użyta na stronie (pomocnicze, nie do CMS) |
| `status` | — | `draft` / `ready` (komplet, zaakceptowane) / `live` (w CMS) |
| `notes` | — | pytania i rozbieżności do wyjaśnienia (nie do CMS) |

Wymagane do `ready`: `slug`, `title_pl`, `title_en`, `year`, `category`, zdjęcia, `photo_credit`,
`description_en`, alt-tekst okładki.

## Zdjęcia — przygotowanie do Framera

Część plików z aparatu ma 10–31 MB (folder „słoneczny stwór”, „taniec deszczu”, „kłos”). Przed
wgraniem do Framera: eksport do JPG ok. 2400 px dłuższego boku, < 1 MB. Nazwa pliku: `<slug>-01.jpg`.

## Pozostałe pliki

- `bio.md` — biogram i CV.
- `awards-press.md` — nagrody, stypendia, wystawy, realizacje, filmy, prasa.
