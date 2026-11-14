---
name: add-work
description: Add or update an artwork of Ewa Dąbrowska in content/works.csv (and in the Framer CMS "Works" collection once it exists) — collects facts, writes PL/EN copy and alt text, never invents data. Use when the user wants to add a new work/project/realizacja, update a work's details, or prepare works for the CMS.
---

# Dodanie / aktualizacja pracy

1. Przeczytaj `content/README.md` (schemat) i `docs/content-guidelines.md` (ton, alt, slug).
2. Zbierz od użytkownika fakty: tytuł oryginalny, rok, kategoria (jedna z 4), materiały,
   wymiary, miejsce, kontekst/opis, zdjęcia (dostępne URL-e). **Niczego nie zgaduj** —
   brakujące pola zostaw jako `TODO` i wypisz je na końcu.
3. Zredaguj `description_pl` / `description_en` (2–5 zdań, ton z guidelines) i alt-tekst
   okładki. Pokaż użytkownikowi do akceptacji.
4. Dopisz/zaktualizuj wiersz w `content/works.csv` (poprawne escapowanie CSV: pola z
   przecinkami w cudzysłowach). Ustaw `status`: `draft` lub `ready`.
5. Jeśli istnieje kolekcja CMS „Works” (sprawdź w `docs/framer-map.md`, potem w Framerze):
   po akceptacji użytkownika utwórz/zaktualizuj item przez `mcp__Framer__exec`
   (najpierw `api.skills.load("cms")`), ustaw `status` na `live`. Nie publikuj strony.
6. Zaproponuj commit z opisem zmiany.
