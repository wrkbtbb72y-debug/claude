# Biblioteka inspiracji

Wspólny zbiór elementów wizualnych ze stron internetowych (screen + link + opis), posegregowany
na kategorie, z wizualną mapą. **Nie jest projektem klienta** — można z niej korzystać w każdej
sesji (np. „pokaż nawigacje z biblioteki, przydadzą się dla Ewy Dąbrowskiej”).
Ścieżki w tym pliku są względem folderu `inspiracje/`.

- **Mapa (Artifact, do oglądania):** _TODO — link pojawi się po pierwszej publikacji_
- **Mapa w repo:** `MAPA.md` (widoczna na GitHubie) i `mapa.html` (pełna wersja z filtrami)

## Co gdzie leży

| Ścieżka | Co to jest |
|---|---|
| `katalog.json` | **Jedyne źródło prawdy**: lista kategorii i wpisów. |
| `obrazy/<kategoria>/<id>.jpg` | Screeny (zmniejszone do 1600 px szer., JPEG). |
| `_skrzynka/` | Skrzynka odbiorcza: tu użytkownik może wrzucać screeny przez GitHub. |
| `MAPA.md`, `mapa.html` | Generowane skryptem — **nie edytuj ręcznie**. |
| `narzedzia/inspiracje.py` | Skrypt: `dodaj`, `zbuduj`, `artefakt`, `sprawdz`. |
| `narzedzia/szablon.html` | Wygląd mapy (wspólny dla `mapa.html` i Artifactu). |

## Jak użytkownik dodaje inspiracje

1. **W czacie** — screen + link + jedno zdanie, co się podoba (np. „fajne menu, minimalistyczne”).
   Jeśli załączony obraz nie jest dostępny jako plik na dysku (sam podgląd w rozmowie nie
   wystarczy, bo trzeba zapisać plik), poproś o sposób 2.
2. **Skrzynka na GitHubie** — w repo wejść w `inspiracje/_skrzynka/` → *Add file* → *Upload files*,
   wrzucić screeny i zatwierdzić (*Commit changes*). Linki i komentarze podać w czacie albo w
   nazwie pliku. Potem napisać Claude’owi: „przejrzyj skrzynkę inspiracji”.
3. **Sam link** (bez screena) — Claude robi screen sam, **o ile** sieć środowiska wpuszcza daną
   stronę. Obecnie środowisko blokuje strony zewnętrzne (sprawdzone 2026-11-20); wtedy poproś
   o screen albo zaproponuj zmianę dostępu do sieci w ustawieniach środowiska.

## Procedura dla Claude’a (każdy nowy element)

1. Zdobądź plik obrazu (czat / `_skrzynka/` / własny screen). Jeden element = jeden wpis;
   jeśli screen pokazuje kilka ciekawych rzeczy — zapytaj, o który chodzi, albo zrób kilka wpisów.
2. Obejrzyj obraz i ustal:
   - **kategoria** — jedna z tabeli niżej; wybieraj sam, pytaj tylko przy prawdziwej wątpliwości;
   - **tytuł** — krótko, po polsku, *co to za element i czym się wyróżnia*
     (np. „Menu pełnoekranowe z ogromną typografią”), bez nazwy strony;
   - **tagi** — 2–5, małymi literami, ze słownika niżej (nowy tag tylko, gdy żaden nie pasuje);
   - **notatka** — słowa użytkownika (co mu się podoba); bez zmyślania;
   - **projekt** — folder projektu, jeśli użytkownik wskazał, do czego to (np. `ewa-dabrowska`).
3. Dodaj wpis (z katalogu głównego repo):
   ```
   python3 inspiracje/narzedzia/inspiracje.py dodaj --obraz <plik> --url <link> \
     --kategoria <slug> --tytul "…" --tagi a,b --notatka "…" [--projekt …] [--strona "Nazwa"]
   ```
   Skrypt zapisuje obraz, dopisuje wpis do `katalog.json` i przebudowuje `MAPA.md` + `mapa.html`.
   Brak linku → pomiń `--url` i zapytaj użytkownika (nie zgaduj adresu).
4. Plik ze `_skrzynki/` po dodaniu **usuń** (`git rm`) — skrzynka ma być pusta.
5. `python3 inspiracje/narzedzia/inspiracje.py sprawdz` — musi być „OK”.
6. Odśwież Artifact: `… inspiracje.py artefakt --wyjscie <scratchpad>/atlas-inspiracji.html`
   i opublikuj ten plik **pod ten sam adres** (link na górze tego pliku; przy pierwszej publikacji
   wpisz link tutaj). Artifact jest prywatny — udostępnia go tylko użytkownik.
7. Zapisz zmiany w repo zgodnie z głównym `CLAUDE.md` (commit `inspiracje: …`, PR, merge).
8. W odpowiedzi: co dodano, do jakiej kategorii, z jakimi tagami + link do mapy.

## Kategorie

| slug | Nazwa | Co tu trafia |
|---|---|---|
| `nawigacja` | Nawigacja i menu | paski nawigacji, menu mobilne, nagłówki |
| `hero` | Hero i otwarcia | pierwsze ekrany, intro, ekrany ładowania |
| `typografia` | Typografia | kroje, zestawienia, duże napisy, detale składu |
| `uklad` | Układ i siatka | kompozycja, asymetria, siatki, rytm sekcji |
| `galerie` | Galerie i portfolio | siatki prac, karuzele, listy projektów, strona pracy |
| `obraz-i-wideo` | Zdjęcia i wideo | kadrowanie, maski, wideo w tle, obraz + tekst |
| `kolor` | Kolor i tekstury | palety, tła, gradienty, ziarno |
| `interakcje` | Animacje i interakcje | hover, scroll, kursor, przejścia |
| `komponenty` | Komponenty UI | przyciski, karty, formularze, zakładki, akordeony |
| `stopki` | Stopki i kontakt | stopki, sekcje kontaktowe, końcowe CTA |
| `inne` | Inne | tymczasowo — przy porządkach przenieść |

Animacji nie widać na screenie — w notatce opisz, co się dzieje (np. „zdjęcie powiększa się
przy przewijaniu”). **Nowa kategoria** dopiero, gdy w `inne` zbiorą się ≥3 podobne wpisy:
dopisz ją w `katalog.json` (`kategorie`) i w tabeli wyżej. Zmiana kategorii wpisu = zmiana pola
`kategoria` + przeniesienie pliku do nowego podfolderu + aktualizacja pola `obraz`, potem `zbuduj`.

## Słownik tagów

Trzymaj się istniejących tagów, żeby filtry działały (sprawdź też tagi już użyte w `katalog.json`).

- **Styl:** minimalizm, editorial, brutalizm, retro, luksusowy, zabawowy, techniczny
- **Kolor:** czarno-białe, monochromatyczne, pastelowe, kontrastowe, ciemny-motyw
- **Typografia:** szeryfowa, groteska, wielkie-litery, ogromny-tekst
- **Technika:** hover, scroll, kursor, wideo, 3d, siatka, asymetria, pełny-ekran, poziomy-scroll
- **Kontekst:** portfolio, sztuka, sklep, agencja, mobile
