# Ewa Dąbrowska — oficjalna strona artystki

Ten folder (`projects/ewa-dabrowska/`) jest **bazą wiedzy projektu** strony Ewy Dąbrowskiej
(land-art, rzeźba, rysunek i stop-motion, dźwięk). Sama strona (wygląd, layout, CMS) żyje we
**Framerze** — tutaj trzymamy wszystko, czego Framer nie pamięta: brief, ustalenia, system
projektowy, mapę projektu, treści, bazę prac i backlog.

Zasady wspólne dla wszystkich projektów (praca z Framerem, definition of done, utrzymanie
wiedzy) są w głównym `CLAUDE.md` repozytorium. **Ścieżki w tym pliku i w `docs/` / `content/`
są względem tego folderu** (np. `docs/brief.md` = `projects/ewa-dabrowska/docs/brief.md`).

- **Framer:** https://framer.com/projects/Ewa-D-browska-Official--gMKkn1ektXgFZXROgJCy-a6APP
  (project ID `gMKkn1ektXgFZXROgJCy`)
- **Produkcja:** jeszcze nieopublikowana — domena: _TODO_
- **Materiały od artystki (Google Drive):** portfolio PDF, zdjęcia Ewy, zdjęcia prac —
  https://drive.google.com/drive/folders/1ODdjKarffSbNv4YrUwelKkm0PLBD317T
- **Język rozmowy z Claude:** polski. **Język treści na stronie:** patrz `docs/content-guidelines.md`.

## Mapa folderu

| Plik | Po co | Kiedy czytać |
|---|---|---|
| `docs/brief.md` | Kim jest artystka, cel strony, odbiorcy, ton | Przed każdą zmianą treści lub nową sekcją |
| `docs/design-system.md` | Kolory, typografia (ID presetów), komponenty, ruch | Przed każdą zmianą wizualną |
| `docs/framer-map.md` | Strony, sekcje, ID węzłów, kotwice, triggery scrolla | Przed edycją we Framerze |
| `docs/content-guidelines.md` | Język PL/EN, ton, alt-teksty, nazewnictwo prac | Przy pisaniu copy |
| `docs/decisions.md` | Log decyzji (co, dlaczego, kiedy) | Gdy coś wydaje się „dziwne” — może było celowe |
| `docs/ustalenia/` | Dokument ustaleń z klientką (HTML → PDF, najnowsza wersja = najwyższy numer) | Gdy trzeba wysłać artystce aktualny stan ustaleń |
| `docs/backlog.md` | Znane problemy i plan prac z priorytetami | Na start sesji roboczej |
| `docs/zaliczenie-klika.md` | **Wymagania zaliczenia kursu KLIKA** (21 punktów) ze statusami ✅ / 🟡 / ⬜ / ❓ | Gdy Piotr pyta, co zostało do zaliczenia; przy planowaniu prac; po każdej zmianie we Framerze, która spełnia punkt |
| `content/works.csv` | Baza prac — źródło prawdy dla przyszłego CMS „Works” | Przy dodawaniu/edycji prac |
| `content/bio.md`, `content/awards-press.md` | Biogram/CV; wystawy, nagrody, filmy, kandydaci na logotypy | Przy About / Exhibitions / Film / Press |
| `content/sources/` | Przepisane materiały źródłowe (portfolio) — słowa artystki, nie edytować | Gdy potrzebny opis pracy lub fakt |

Skille projektu (`.claude/skills/` w tym folderze): **`/framer-audit`** — audyt przed
publikacją, **`/add-work`** — dodanie nowej pracy do bazy (i do CMS, gdy powstanie).

## Specyfika Framera w tym projekcie

- Strona Home ma rozbudowane triggery scrolla — po każdej zmianie sprawdź, czy kotwice
  z `docs/framer-map.md` nadal istnieją.
- **Plan Framera nie obejmuje branchy** — każda zmiana trafia od razu do głównej wersji projektu.
  Strona nie jest opublikowana; przed zmianą istniejących elementów zrób screenshot „przed”, po zmianie
  „po”, i powiedz Piotrowi, że cofnięcie jest w historii wersji Framera.
- CMS: kolekcje **Works** (31 prac) i **Exhibitions** (18 wystaw) — ID pól w `docs/framer-map.md`.
  Prace na Home są nadal wpięte ręcznie na canvasie (nie z CMS).
- Skill Framera **`ewa-brand`** trzyma zasady marki dla AI we Framerze — aktualizuj go razem z design-system.md.

## Kluczowe fakty (skrót — szczegóły w docs/)

- **Projekt zaliczeniowy kursu KLIKA** — strona musi spełnić wszystkie wymagania z
  `docs/zaliczenie-klika.md` (m.in. min. 1 zalinkowana podstrona, Layout Template, favicon + Social
  Image, znaczniki HTML, aria-label). Po zmianie we Framerze, która spełnia punkt, **zaktualizuj jego status**.
- **Klimat:** ciemny, galeryjny, dużo powietrza; czerń `#000` + biel, akcent przez zdjęcia,
  nie przez kolor. Duża szeryfowa typografia (Instrument Serif) + techniczny grotesk
  (ABC Diatype) do UI.
- **Struktura Home:** Hero „Land-Art & Sculpture” → pasek „Explore projects” (sticky) →
  Projects (rozsypane zdjęcia z efektami scrolla) → My Journey / About (cytat, portret,
  Practice 01–04) → footer reveal (kontakt, e-mail).
- **Practice (4 obszary = kategorie prac):** Land Art & Happenings · Sculpture ·
  Drawing & stop-motion · Sound.
- **Zewnętrzne moduły:** Lenis (smooth scroll), Video, override `withLinksAfterSection`.
- **Ustalenia z artystką (v3, 2026-11-14)** — `docs/ustalenia/ustalenia-strony-v3.pdf`, streszczone
  w `docs/brief.md` i `docs/decisions.md`: najpierw EN (PL później), CTA „Zobacz realizacje” +
  „Kontakt” (+ „Gdzie zobaczyć moje prace”), docelowe menu Work · Where to see · Exhibitions ·
  Film / Performance · Publications / Press · About · Contact. **Obecna strona jeszcze tego nie
  odzwierciedla** (stare menu Works / Info / Awards). W nawigacji musi się zmieścić
  **przełącznik języków EN / PL**.
- **E-mail na stronie (`e.dabrowska@mail.com`) jest przykładowy** — prawdziwy poda artystka.
- **Brak CMS** — plan: kolekcja „Works” zgodna ze schematem `content/works.csv` (patrz backlog).

## Zasady treści (specyficzne dla tego projektu)

- Każde zdjęcie pracy ma **alt-text** (tytuł + materiał + co widać) — zob. content-guidelines.
- Tytuły prac: oryginalny polski tytuł jest nadrzędny; angielski jako tłumaczenie.
- Nie wymyślaj faktów o artystce (dat, nagród, wystaw, materiałów). Brak danych → `TODO`
  i pytanie do użytkownika.
