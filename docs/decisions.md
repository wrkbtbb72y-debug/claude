# Log decyzji

Format: data · decyzja · powód · status. Najnowsze na górze.
Status: ✅ przyjęte · 🟡 propozycja (czeka na akceptację) · ❌ odrzucone.

---

### 2026-11-14 · Przełącznik języków, e-mail, materiały źródłowe — ✅
- **Przełącznik języków EN/PL w pasku nawigacyjnym.** Strona powstaje po angielsku, wersja polska
  dojdzie później — ale miejsce na przełącznik (EN / PL) projektujemy w Nav Bar **od razu**, na
  desktopie i w menu mobilnym, żeby nie przebudowywać nawigacji na końcu.
- **E-mail `e.dabrowska@mail.com` jest przykładowy (placeholder).** Nie traktować jako prawdziwego;
  prawdziwy adres przekaże artystka. Do tego czasu nie podpinać `mailto:` ani formularza do niego.
- **Materiały źródłowe na Google Drive** (portfolio PDF, zdjęcia Ewy, zdjęcia prac):
  https://drive.google.com/drive/folders/1ODdjKarffSbNv4YrUwelKkm0PLBD317T — portfolio przepisane do
  `content/sources/portfolio-2026-09.md`; baza `content/works.csv` zbudowana z portfolio (31 prac).

### 2026-11-14 · Kolejność prac i logo (wiadomości od artystki z 7.10.2026) — ✅
Zapisane w `docs/ustalenia/ustalenia-strony-v3.pdf` (pkt 7 i 8).
- **Kolejność prac (Work):** od najnowszych, ręcznie: 1. „Słoneczny Stwór”, 2. „Tancerz”,
  3. „Dziki” (z patyków); dalej wg wyczucia projektanta. Propozycja na Home: te same trzy
  (+ ew. 1–2 kolejne). ✅ Potwierdzone: „Dziki” = praca podpisana na stronie jako „Herd” (slug `herd`; tytuł w portfolio „Herd”, folder na Dysku „Stado”).
- **Logo:** start z logotypem — imię i nazwisko ładnym fontem (artystce bardzo się podoba).
  Własny znak: artystka spróbuje naszkicować (w podróży, bez terminu) — zostawiamy na niego
  miejsce, potem ewentualnie motyw przewodni strony. Strona nie czeka na znak.

### 2026-11-14 · Ustalenia z klientką (dokument „Ustalenia strony”, v2) — ✅
Źródło: komentarze artystki do v1 dokumentu ustaleń → podsumowanie w `docs/ustalenia/ustalenia-strony-v2.pdf`
(źródło HTML obok; PDF generowany z HTML przez Chromium/Playwright).
- **Cele i odbiorcy:** zaakceptowane wszystkie propozycje (wizytówka dla instytucji, galeria
  pod współprace, marka własna; wspierająco: media, archiwum sztuki efemerycznej, warsztaty).
  Główna persona: osoby decyzyjne z budżetem.
- **CTA:** dwa równorzędne przyciski „Zobacz realizacje” i „Kontakt”. ❌ Kup / Zapytaj o
  współpracę / Napisz do mnie / Zobacz terminy.
- **Nowe (pomysł artystki):** „Gdzie zobaczyć moje prace” — podstrona z mapą prac (PL + Europa),
  pinezka → zdjęcie, tytuł, rok, miejsce + „Otwórz w Mapach Google”; lista miejsc pod mapą;
  blok „Gdzie zobaczyć” na stronie projektu; trzeci, spokojniejszy przycisk na Home.
  🟡 Otwarte: prace efemeryczne (pomijać / oznaczać), lokalizacje prywatne.
- **Kontakt:** widoczny adres e-mail (podstrona Contact + stopka) + formularz jako uzupełnienie.
  ❌ telefon, ❌ newsletter.
- **Home:** wybrane projekty (3–5), krótko o artystce, logotypy instytucji.
  ❌ belka „Nowości” (powód: rzadkie aktualizacje), ❌ sekcja „Featured”.
- **Menu (nazwy robocze):** Work · Where to see · Exhibitions (jedna lista, bez podziału na
  nadchodzące/aktualne/archiwalne) · Film / Performance (YouTube) · Publications / Press · About · Contact.
  ❌ News, ❌ Creative Process.
- **Wciąż otwarte:** strony-inspiracje. (Kolejność projektów i logo — ustalone, wpis wyżej.)

### 2026-11-14 · Język strony — ✅
- **Decyzja:** najpierw wersja EN, wersja PL dodana pod koniec prac (przełącznik języków,
  lokalizacja Framera) — tak zakomunikowano klientce w dokumencie ustaleń.

### 2026-11-14 · Źródło prawdy dla prac: `content/works.csv` → Framer CMS — 🟡
- **Decyzja:** Dane o pracach (tytuły, lata, materiały, opisy) edytujemy najpierw w
  `content/works.csv` w repo; Claude synchronizuje je do kolekcji CMS „Works” we Framerze.
  Zdjęcia żyją we Framerze (asset store), w CSV trzymamy ich nazwy/URL.
- **Powód:** historia zmian w git, możliwość masowych poprawek i generowania tekstów
  (opisy, alt-teksty, PL/EN) przez Claude, jedna kanoniczna lista do wniosków grantowych/CV.
- **Alternatywa:** CMS we Framerze jako jedyne źródło (prościej, jeśli treści będzie
  edytować artystka sama w Framerze) — wtedy CSV tylko jako okresowy eksport.

### 2026-11-14 · Repo jako baza wiedzy, Framer jako źródło prawdy dla wyglądu — ✅
- **Decyzja:** Wygląd, layout i komponenty utrzymujemy wyłącznie we Framerze. Repo zawiera
  wiedzę, ustalenia, treści i dane. `docs/design-system.md` i `docs/framer-map.md` to
  mapy/snapshoty, aktualizowane po zmianach.
- **Powód:** Framer nie ma pamięci kontekstu między sesjami AI; repo daje Claude stały kontekst.

### (wcześniej) · Kierunek wizualny: ciemna galeria + duży szeryf + efekty scrolla — ✅
- Odtworzone ze stanu projektu. Powody/inspiracje: _TODO — dopisać, jeśli były ustalenia_.
