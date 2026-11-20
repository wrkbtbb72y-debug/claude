---
name: inspiracje
description: Dodawanie elementów wizualnych ze stron internetowych (screen + link) do biblioteki inspiracji w `inspiracje/` — katalogowanie w kategoriach, tagi i odświeżenie wizualnej mapy (Atlas inspiracji). Używaj, gdy użytkownik wysyła screen lub link strony „do inspiracji”, prosi o przejrzenie skrzynki inspiracji, o pokazanie zebranych przykładów (np. nawigacji, galerii) albo o porządki w kategoriach.
---

# Biblioteka inspiracji

1. Przeczytaj `inspiracje/CLAUDE.md` — tam są kategorie, słownik tagów i procedura.
2. **Dodawanie:** dla każdego elementu wykonaj procedurę „Procedura dla Claude’a” (skrypt
   `inspiracje/narzedzia/inspiracje.py dodaj`), potem `sprawdz`, odśwież Artifact pod tym samym
   adresem i zapisz zmiany w repo (commit `inspiracje: …`, PR, merge — wg głównego `CLAUDE.md`).
3. **Przegląd skrzynki:** każdy plik z `inspiracje/_skrzynka/` (poza README.md) skataloguj jak wyżej,
   a potem usuń ze skrzynki. Brakujące linki zbierz w jednym pytaniu do użytkownika.
4. **Wyszukiwanie dla projektu:** czytaj `inspiracje/katalog.json` (kategoria, tagi, notatka)
   i obejrzyj pasujące obrazy z `inspiracje/obrazy/`; podaj tytuły, linki i krótkie uzasadnienie.
5. Nie zmyślaj: brak linku albo niejasne „co się podoba” → zapytaj.
