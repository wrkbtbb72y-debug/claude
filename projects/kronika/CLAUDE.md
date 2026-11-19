# Kronika

<!-- Utworzone 2026-11-14 z szablonu. Pola TODO uzupełnić z użytkownikiem — nie zgadywać. -->

Zasady wspólne (praca z Framerem, definition of done) są w głównym `CLAUDE.md` repozytorium.
Ścieżki w tym pliku są względem tego folderu.

- **Framer:** https://framer.com/projects/Kronika--0h5pA6cwUCiyjVB0qFni-1oD05
  (project ID `0h5pA6cwUCiyjVB0qFni`)
- **Figma (projekt graficzny):** https://www.figma.com/design/XvZvAuEpnnShbbxSqZoseo/KRONIKA
  — komponenty robocze na stronie „- KOMPONENTY - nowe (robocze)”, przyciski na stronie „BUTTONS”.
- **Figma (makiety):** https://www.figma.com/design/XvZvAuEpnnShbbxSqZoseo/KRONIKA — strona
  „1. Główna 2.0”, ramka `8867:13877` z 4 makietami Home: 1440 `7373:100781`, Desktop Primary
  1024 `7399:252`, Tablet 810 `7373:101588`, Mobile 390 `7373:102357`.
  Strona „3. Zasoby/Obiekty - TBC”: **„Lista obiektów”** — oficjalna makieta Desktop Large
  (1440): widok kafelków **„Desktop Large - Cards”** `8670:4812`, obok po prawej widok listy
  **„Desktop Large - Lista”** `8970:7119` (x 5639), dalej „audyt”. **Wyniki wyszukiwania** —
  rząd 4 makiet (y −47876): Desktop Large `8949:9184` (x 5639), Desktop Small `9173:12149`,
  Tablet `9173:15859`, Mobile `9173:16891`; pod nim **brak wyników** (y −39090): Desktop Large
  `9015:7886`, Desktop Small `9173:18307`, Tablet `9173:19085`, Mobile `9173:19850`; kopia zapasowa
  sprzed zmian 2026-11-16: „Lista obiektów - kopia zapasowa” `8911:31206` (karty odłączone
  od komponentu). **Nowe komponenty** tych makiet (wzorce) leżą w opisanej ramce
  **„Lista obiektów – nowe komponenty”** `8983:7846` na prawo od makiety wyników
  (x 10777): Przełącznik Obiekty / Kolekcje, Przełącznik widoku, Przycisk Dodaj do kolekcji
  (te trzy jako **kopie** — wzorce przeniesione na stronę BUTTONS do tabeli „Nowe przyciski”,
  sekcja „Strona: Zasoby · Lista obiektów”), Object row (wzorzec) — każdy z nagłówkiem
  i opisem; na dole notka o zmienionych „Object tile”
  i „Category label” (te zostały na swoich miejscach). Wcześniej podane pozycje x/y tych
  komponentów są nieaktualne. Stara wersja przełącznika widoku („– kwadraty (poprzednia
  wersja)” `8951:7085`) nie jest używana i została obok makiety kart.
- **Przyciski w Figmie — zasada (użytkownik, 2026-11-16):** strona „BUTTONS” to oficjalny
  zbiór wszystkich przycisków serwisu. **Każdy nowy przycisk** powstały podczas pracy: jego
  **komponent główny (wzorzec)** umieść w tabeli **„Nowe przyciski”** (`8988:324`, w ramce
  „Buttons Kronika” `8578:129844`, na prawo od tabeli „Przyciski – przegląd” `8347:118328`),
  w sekcji strony, na której się pojawia (wiersz: opis po lewej, wzorzec w „Podglądzie”).
  Na makietach na innych stronach używaj **wyłącznie kopii (instancji)** tych komponentów.
  Styl tabeli = kopia wierszy z „Przyciski – przegląd” (nagłówek „KRONIK@ · …” #9A1C31,
  tytuł 40 px, tło #EFEFEF, wiersz kolumn #F7F8FA, wiersz sekcji 20/500, opis 14/500
  + notka 12/450 #646A74). Nowe wiersze dodawaj, klonując istniejący wiersz tej tabeli.
- **Ikony w Figmie:** wszystkie ikony w przyciskach bierz **wyłącznie** z kolekcji na stronie
  „- ICONS LUCIDE” (`31:782`, ramka „Lucide Icons” `39:784`, nazwy `lucide/<nazwa>`) —
  polecenie użytkownika, 2026-11-16.
- **Produkcja / domena:** _TODO_
- **Materiały od klienta:** _TODO (np. link do Google Drive)_
- **Język treści na stronie:** _TODO (PL / EN / oba)_
- **Termin:** _TODO_
- **Branche we Framerze:** w tym projekcie edycje AI **nie tworzą brancha** (sprawdzone
  2026-11-15, trzy razy) — zmiany idą od razu do głównej wersji (`main`), nieopublikowane.

## O projekcie (brief w skrócie)

- **Klient:** kim jest, czym się zajmuje.
- **Cel strony:** _TODO_
- **Odbiorcy:** _TODO_
- **Ton / klimat:** _TODO_

## Struktura strony

- **Home** (`augiA20Il`) — breakpointy: **Desktop Primary** `d0VxK3QJN` (1024, primary,
  1024–1439 px), **Tablet** `hzEqmNBoY` (810, 810–1023 px), **Duzy desktop** `XjMbofAH4`
  (1440, ≥1440 px), **Mobile** `YLBtCSeLh` (390, <810 px). Uwaga: primary to 1024, nie 1200.
- Sekcja „O Portalu‑section 4” (`XQ6Ofe1Rp`, w środku `About_wrapper` `tTtyi3gJx`) —
  „Otwarte zasoby nauki i kultury”, nad „Instytucje Partnerskie”. Desktop Primary, Tablet
  i Duży desktop: ilustracja „tablet i książki” (`XTasEtfqG`) po lewej + tekst „Zapewniamy
  bezpłatny dostęp…” z „Czytaj więcej” (`OJuh71bfJ`) po prawej; „Czytaj więcej” w wierszu
  tytułu (`FXesmdTxZ`) ukryte. Licznik „19mln zgromadzonych obiektów” (`uXWoz4CPW`,
  `B22SY_ZNm`) ukryty na wszystkich breakpointach. Mobile: układ jak „Aktualności-section”
  (`K4Yhx9QyY`) na Mobile — tytuł + linia, ilustracja na całą szerokość, pod nią tekst
  (odstęp 28 px) i „Czytaj więcej” (gap 20 px, wariant przycisku jak w Aktualnościach),
  odstęp tytuł–treść 32 px.
- Presety tekstu są responsywne (sloty `medium` ≥1024, `small` ≥768): np. „Nazwy sekcji”
  `onFkvs54B` 28→26 px, „Body 1 - tekst długi L” `qho9AhWr_` 20→18 px na tablecie.

## Ustalenia i decyzje

- 2026-11-15 — Sekcja „O Portalu‑section 4” na Tablecie ma wyglądać jak na Desktop Primary:
  zresetowano wszystkie nadpisania tabletu w tej sekcji (szerokość bloku licznika 527→468 px,
  kolor tytułu, wariant przycisku „Czytaj więcej”, padding pod tytułem 12→9 px, overflow).
  Presetów tekstu nie ruszano (różnica rozmiaru fontu 28/26 i 20/18 px zostaje) — zmiana presetów wpłynęłaby na całą stronę, czeka na decyzję
  użytkownika. Uwaga: zmiana trafiła bezpośrednio do `main` we Framerze (nie utworzył się
  branch), strona nieopublikowana.

- 2026-11-15 — Ta sama sekcja na Desktop Primary i Tablecie pokazuje te same elementy co na
  Dużym desktopie (ilustracja + opis zamiast licznika „19mln”) — prośba użytkownika. Zmiana
  na Desktop Primary (dziedziczy Tablet); Mobile celowo bez zmian. Znów bezpośrednio w `main`
  we Framerze, nieopublikowane.

- 2026-11-15 — Mobile tej sekcji zrobiony na wzór sekcji Aktualności na Mobile (prośba
  użytkownika: obie sekcje mają podobny układ, więc na Mobile mają wyglądać podobnie).

- 2026-11-15 — **Figma:** komponent „Section heading” (`3350:38625`, 4 warianty: Dekstop Large /
  Desktop Small / Tablet / Mobile) dostał dwa przełączniki: **„Link tekstowy”** (instancja
  „Zobacz wszystkie” `8867:14967`) i **„Strzałki”** (instancja „arrows navi” `8867:14958`),
  domyślnie wyłączone — dotychczasowe użycia wyglądają bez zmian. Układ wzorowany na roboczych
  frame’ach `8867:14979`: w każdym wariancie nagłówek siedzi w „Heading row” (space-between),
  po prawej kontener „Actions” (gap 24) z „Link wrapper” (link wyrównany do dołu nagłówka)
  i strzałkami (wyśrodkowane w pionie). Oba naraz: link po lewej, strzałki przy krawędzi.
  Na Tablecie/Mobile włączone strzałki (32 px) podnoszą wysokość bloku o 1–3 px.

- 2026-11-15 — Makiety w Figmie zsynchronizowane z Framerem dla sekcji „Otwarte zasoby nauki
  i kultury” (ramki „O Portalu — Integrujemy zasoby” `7636:83155` / `:83162` / `:83169` /
  `:83176`): przebudowane na auto‑layout — tytuł + linia, ilustracja + opis z pogrubionym
  „19 milionów obiektów” + „Czytaj więcej”; licznik „19mln” usunięty. Ilustracja to kopia
  ramki „Ilustracja 07b” (`8833:7645`, wskazana przez użytkownika) ze strony „1. Główna 2.0”,
  przeskalowana do rozmiarów z Framera (652×373 / 468×267 / 361×206 / 358×205).

- 2026-11-15 — **Figma:** na makietach Desktop Small, Tablet i Mobile (strona „1. Główna 2.0”)
  wszystkie tytuły sekcji (ramki tytuł + kreska) zastąpione instancjami „Section heading”
  w wariancie danego breakpointu, jak na Desktop Large. Przełączniki jak na Desktop Large:
  Polecane — „Strzałki”, Wybrane kategorie i Instytucje — „Link tekstowy”, Aktualności
  i Otwarte zasoby — bez dodatków. Teksty tytułów zostały bez zmian (na Mobile „Instytucje”,
  nie „Instytucje Partnerskie”). Instancje mają szerokość „Fill”.

- 2026-11-15 — **Figma:** teksty na 4 makietach Home (poza instancjami komponentów: nawigacja,
  stopka, Section heading itp.) dostały style tekstowe odpowiadające presetom z Framera.
  Mapowanie preset Framera → styl Figmy (grupa breakpointu: „Duży desktop ≥1440” /
  „Desktop 1024–1439” / „Tablet 768–1023” / „Mobile ≤767”, albo „Wszystkie breakpointy”):
  Nazwy sekcji → H2 - Nazwy sekcji; Nagłówki → H4 - Nagłówki; Body 1 - tekst długi L → Body 1;
  Nagłówek stron → H1; Body 4 Thin, Button, Button Thin, Uppercase S → odpowiedniki
  z „Wszystkie breakpointy”. „Czytaj więcej”, „Jak zarejestrować instytucję”, „Wyszukiwanie
  zaawansowane”, „Wszystkie instytucje” → Button (we Framerze to komponenty z presetem Button).
  Pogrubienie „19 milionów obiektów” zostawione jako nadpisanie. Ukryte procenty w kategoriach
  pominięte (we Framerze bez presetu).
  Uwaga: placeholder wyszukiwarki we Framerze ma różne style na breakpointach (Duży desktop:
  Button Thin, Desktop Primary: Body 4 Thin, Tablet: jak Button Thin bez presetu, Mobile: jak
  Button bez presetu) — w Figmie odwzorowane 1:1, do ujednolicenia, jeśli to niezamierzone.

- 2026-11-15 — **Figma, Desktop Large, sekcja Polecane:** 3 karty jak we Framerze (Duży
  desktop). Czwarta karta („Polecane_card 4” `7658:1935`) ukryta, nie usunięta. Karty 1–3
  mają szerokość „Fill” (429 px), obrazki 429×241 (proporcja 1,78 jak we Framerze), karta
  429×358.

- 2026-11-16 — **Figma, „Ilustracja 07b” (`8911:27037`) → „Kompozycja” (`8911:27061`):** tablet
  z efektem 3D (ramka „Tablet – perspektywa” `8911:27095`: perspektywa 500 na ramce + obrót 3D
  tabletu) spłaszczony na prośbę użytkownika — bez żadnego efektu 3D, wygląd 1:1 z wersją 3D.
  Nowa ramka „Tablet (spłaszczony)” (`8936:4629`, x 134 / y 17,75 w „Kompozycja”):
  **„Korpus”** (`8936:4630`) — edytowalny wektor z wypełnieniem (kolor + gradient, cień jak
  w oryginale); **„Ekran – Kronika polska”** (`8936:4631`) — wektor z wypełnieniem obrazem
  (zdjęcie ekranu w perspektywie, PNG 4×); **„Linia”** (`8936:4636`) — białe obrysy jako wektory
  (obrys tabletu, ekranu, przycisku, lewa krawędź; stroke 1,14 px). Oryginał 3D zostawiony
  **ukryty** jako kopia zapasowa („… (oryginał 3D, ukryty)”) — można go usunąć.
  Wcześniejsza wersja (cały tablet jako jedna bitmapa) odrzucona — użytkownik chce wektorów.
  **Jak spłaszczać 3D (lekcje):**
  - `exportAsync`/`screenshot` we wtyczce (use_figma) renderują perspektywę **źle**; prawidłowy
    render daje `get_screenshot` (serwer) — tylko nim porównywać.
  - Wektory: rzutować punkty ścieżek (także punkty kontrolne) modelem CSS: punkt w układzie
    lokalnym węzła − transformOrigin → rotateZ, potem Y, potem X (konwencja CSS) → + origin,
    + translateZ → transformacja 2D węzła do rodzica → perspektywa d/(d − z) względem środka
    ramki ze `scene3d`. Zgodność konturu z renderem serwera: 99,2%.
  - Bitmapy (zdjęcie ekranu): kopia ramki `rescale(4)` (perspektywa, translateZ, transformOrigin
    w px ×4) w tymczasowej ramce → `get_screenshot` → przycięcie do bboxa wektora → `upload_assets`
    z `nodeIds` (wymaga hosta `mcp.figma.com`, dodanego do środowiska 2026-11-16). Przezroczystość
    w renderze serwera: dwa rendery (czarne i białe tło), alfa = 1 − (biały − czarny)/255.

- 2026-11-16 — **Figma, strona „BUTTONS”, tabela przycisków (ramka `8911:29360`):** komponenty
  linków tekstowych „Czytaj więcej” i „Zobacz wszystkie” zamienione na zestawy wariantów
  (`8921:328` i `8921:333`) z właściwością **„Stan”**: `Domyślny` (dotychczasowy komponent,
  ID bez zmian: `8911:29361` / `8867:14967`) i `Hover` (`8921:326` / `8921:331`) — po prawej,
  ten sam styl „Button” + podkreślenie tekstu. Nad wariantami etykiety „Desktop” / „Hover”.
  Zestawy i warianty mają wyłączone przycinanie (inaczej podkreślenie pod 15‑px linią tekstu
  było ucięte). Istniejące instancje (np. w „Section heading”) zostały podpięte i dalej
  pokazują stan domyślny.

- 2026-11-16 — **Figma, sekcja „Polecane” na 4 makietach Home** (`7373:101080` / `7399:581` /
  `7373:101889` / `7373:102651`): warstwy uporządkowane i ujednolicone, wygląd i wymiary bez
  zmian. Wszędzie ta sama struktura, całość na auto‑layoucie:
  `Recommended` → `Section heading` (Fill) + `Cards` → `Card N` (Fill) → `Image` (prostokąt
  ze zdjęciem, Fill × stała wysokość) + `Content` → `Title` + `Meta` → `Author`, `Separator`
  (`Dot`), `Year`. Usunięte zbędne ramki‑pośredniki (ramka wokół zdjęcia, dwie puste ramki
  wokół tekstów — 27 warstw) i ukryta 4. karta na Desktop Large (`7658:1935`). Nazwy proste,
  po angielsku jak reszta pliku, bez kresek, slashy i podkreśleń. Różnice między breakpointami
  zostały tylko w wartościach (odstępy, paddingi, wysokość zdjęcia, liczba kart: 3 / 3 / 2 / 1).
  Odstęp tytuł–podpis w `Content` (gap): 8 px na wszystkich breakpointach (wcześniej 12, na Mobile 10;
  prośba użytkownika). Padding `Content`: góra 24 px, dół 0 na wszystkich breakpointach (wcześniej
  Desktop Large 20/36, pozostałe 16/0; prawy 16 i lewy 0 bez zmian). We Framerze nie zmieniano.

- 2026-11-16 — **Figma, makiety Home (sekcja „Otwarte zasoby nauki i kultury”):** wyeksportowany
  obrazek (prostokąt z JPG) zastąpiony na wszystkich 4 makietach **instancją komponentu
  „Ilustracja 07b”** (`8911:29497`, 630×360, strona „1. Główna 2.0”), przeskalowaną proporcjonalnie
  do szerokości dawnego obrazka: Desktop Large 652 px (`8937:4629`), Desktop Small 468
  (`8937:4689`), Tablet 361 (`8937:4749`), Mobile 358 (`8937:4809`). Wysokości wynikają z proporcji
  komponentu (372,6 / 267,4 / 206,3 / 204,6 — o ułamek px mniej niż stare obrazki). Zmiany
  w komponencie przenoszą się teraz automatycznie na wszystkie makiety.

- 2026-11-16 — **Figma, „Lista obiektów” (Desktop Large `8670:4812`):**
  - **Przełącznik Obiekty / Kolekcje** (dawniej ramka `8701:4842`, teraz instancja
    komponentu — niżej) przeniesiony z hero na górę sekcji listy,
    tuż pod hero (padding sekcji u góry 120 → 24 px; 40 px do tytułu „Lista obiektów”).
    Kolory pod jasne tło: aktywny #121212 + kreska 3 px, nieaktywny #6C6C6C; style tekstu
    Button Active / Button Thin. Hero zostaje 380 px — tytuł „Przeglądaj obiekty”
    z wyszukiwarką wyśrodkowany w pionie między okruszkami a dolną krawędzią hero (prośba
    użytkownika). Sekcja listy ma teraz wysokość „Hug” (wcześniej stała 1777 px).
    **Linia bazowa** (prośba użytkownika): pod oboma opcjami cienka linia 1 px #D6D6D6
    („Linia bazowa”, prostokąt absolutny, rozciągany na szerokość przełącznika, pod opcjami);
    gruba kreska aktywnej opcji (3 px #121212, obrys „Inside”) leży na niej, wyrównana do
    dołu. Obie opcje mają stałą wysokość 32 px (padding 4/4), żeby teksty były w jednej linii.
    To samo w ramce wyników wyszukiwania.
    **Komponent** (prośba użytkownika): „Przełącznik Obiekty / Kolekcje” (`8967:7106`, obok
    makiety, x 3689 / y −28300), warianty **Aktywny=Obiekty** `8967:7099` / **Aktywny=Kolekcje**
    `8967:7100`, właściwości tekstowe „Obiekty” i „Kolekcje”. Obie opcje mają **jednakową
    szerokość podkreślenia** — równą dłuższej etykiecie (61 px dla „Obiekty” / „Kolekcje”
    w pogrubieniu) + **padding 4 px po bokach** (prośba użytkownika), czyli 69 px:
    komponent ma stałą szerokość 158 px, opcje „Fill” (dzielą po równo, odstęp 20), tekst
    wyśrodkowany. Przy dłuższych etykietach poszerza się całą instancję:
    2 × (szersza etykieta + 8) + 20. Instancje: lista `8967:7107` (158 px), wyniki
    wyszukiwania `8967:7113` (240 px, opcje po 110 px, „Obiekty (1 248)” / „Kolekcje (3)”).
    Stare ramki usunięte. **Kreski (zmiana użytkownika):** gruba kreska aktywnej opcji
    (3 px) **stoi na** szarej linii bazowej (1 px) — komponent ma 33 px wysokości, opcje 32 px
    (wyrównane do góry), linia bazowa na samym dole (y 32), ciągła pod obiema opcjami.
  - **Karta „Object tile”** (komponent `8669:3701`): marginesy 16 px ze wszystkich stron
    (ikona „Dodaj do kolekcji” 20 px dosunięta do prawej krawędzi przycisku 32 px, więc
    wizualnie też 16 px), rytm pionowy: zdjęcie –16– kategoria –16– tytuł –4– autor –24–
    kreska –16– muzeum –16– dół karty. Style tekstu: tytuł → H4 - Nagłówki (Duży desktop,
    20/500, wcześniej 18/500 bez stylu), autor i muzeum → Table Thin (14/400). Karta urosła
    383 → 397 px. Zmiana w komponencie — dotyczy też ramki „Obiekty - propozycja”;
    kopia zapasowa zamrożona (instancje odłączone).
    **Przycisk „Dodaj do kolekcji” powiększony** (uwaga użytkownika: „trochę za mały”):
    pole 32 → 40×40 px, ikona lucide/folder-plus 20 → 24 px (natywny rozmiar Lucide, obrys
    1,5 px bez zmian), dosunięta do prawej krawędzi przycisku — dalej 16 px od krawędzi karty.
    Wiersz z kategorią ma teraz 40 px, karta 397 → 405 px.
    **Przycisk w ramce (próba, prośba użytkownika):** nowy komponent „Przycisk Dodaj do
    kolekcji” (`8975:7834`, obok makiety, x 3689 / y −28124) z wariantami **Styl=Bez ramki**
    `8975:7830` (dotychczasowy wygląd: ikona dosunięta do prawej) i **Styl=W ramce**
    `8975:7831` (40×40, białe tło, ramka 1 px #E5E5E5 jak sortowanie i filtry, ikona 24 px
    wyśrodkowana). W „Object tile” i „Object row” wstawiony wariant **W ramce** — powrót do
    poprzedniego wyglądu = przełączenie wariantu w komponentach.
    **Styl wg tabeli stanów** (prośba użytkownika, wzór: strona „BUTTONS”, wiersz „Niebieski”
    `8578:129283`): wariant W ramce ma teraz 36×36, białe tło, ramkę 1 px #193680 / 40 %,
    ikonę folder-plus 18 px z linią 1,5 px #193680. Nowa właściwość **Stan**: Domyślny,
    Hover (tło #193680 / 6 %), Focus (pierścień 2 px #193680 z 2 px odstępu — warstwa
    „Focus ring” 44×44), Wciśnięty (tło #193680, ikona biała), Nieaktywny (krycie 35 %).
    „Bez ramki” ma tylko stan Domyślny. Karta: 405 → 401 px.
    **Porządek warstw i auto layoutu (2026-11-17, prośba użytkownika):** usunięta ramka
    „Top content” (miała stałą wysokość 389 px i przycinała stopkę — dolny padding 16 px był
    niewidoczny, a w kartach z wyższym zdjęciem znikał cały wiersz muzeum) i „Divider wrapper”.
    Struktura teraz: **Object tile** (pionowo, gap 16, padding dół 16, szer. stała, wys. hug) →
    `Cover image` (214, fill) · `Content` (padding boki 16, gap 20: `Meta row`, `Title block`)
    · `Footer` (padding boki 16, gap 16: `Divider` 1 px, `Institution row`). ID warstw bez zmian,
    nadpisania instancji (zdjęcia, teksty, kategorie) zachowane. Wygląd bez zmian poza widocznym
    dołem: karta 321 px ma 405 px. Uwaga: makieta „Mobile – wyniki wyszukiwania” `9173:16891`
    ma stałą wysokość 5010 px i już wcześniej ucinała treść (stopka strony od y 7124).
  - **Etykieta kategorii „Tekst”:** komponent „Category label” (`8675:4398`), wariant
    Kategoria=Tekst (`8675:4388`) — tło zmienione #F4EDDA → **#D6DADF** (polecenie
    użytkownika; wariant nie był wcześniej nigdzie użyty). Karta „Maria Skłodowska-Curie”
    (tytuł poprawiony z „Skłodowskiej”) na obu makietach ma teraz kategorię „Tekst”
    (wcześniej „Sztuki wizualne”) i stoi w 2. rzędzie, 3. miejscu (zamieniona miejscami
    z „Portret Elizy Orzeszkowej”).
    Kolory pozostałych kategorii: Muzealia #EAE4DD, Muzyka #DFEBE2, Sztuki wizualne #F8F6EF,
    Film #D4E4ED.
  - **Przełącznik widoku** — nowy komponent „Przełącznik widoku” (`8949:6740`, warianty
    Widok=Kafelki `8949:6726` / Widok=Lista `8949:6733`): dwa kwadratowe przyciski 48×48
    (wysokość jak sortowanie), ikony lucide/layout-grid i lucide/layout-list, aktywny tło
    #F1F1F1 + ikona #121212, nieaktywny białe + #6C6C6C, ramka #E5E5E5. Instancja na prawo
    od sortowania (`8949:6741`).
  - **Przełącznik widoku — wersja 2** (tego samego dnia, prośba użytkownika: „jak shadcn Tabs
    z ikonami, w stylu Kroniki”): komponent `8949:6740` przebudowany na segmentowany
    przełącznik — szyna #E5E5E5 (padding 4, wysokość 48 jak sortowanie, kąty proste),
    segmenty 40 px z ikoną 20 px + podpisem „Kafelki” / „Lista” (gap 8, padding 16).
    Aktywny: białe tło + cień 0/1/3 rgba(0,0,0,.08), #121212, styl Button Active;
    nieaktywny: bez tła, #6C6C6C, styl Button. Warianty w zestawie ułożone pionowo
    (zestaw stoi obok makiety, x 3689). Wzór w kodzie: shadcn Toggle Group (`type="single"`)
    lub Tabs. Poprzednia wersja (dwa kwadraty 48×48) zachowana bez zmian jako osobny zestaw
    „Przełącznik widoku – kwadraty (poprzednia wersja)” `8951:7085`.
    **Poprawka:** szare tło szyny nie pasowało do stylu strony (uwaga użytkownika) — szyna
    jest teraz biała z ramką 1 px #E5E5E5 (jak przycisk sortowania obok), aktywny segment
    ma tło #F1F1F1 (jak aktywne „20” w „Pokaż na stronie”), bez cienia.
  - **Wyniki wyszukiwania** — propozycja w osobnej ramce `8949:9184`: fraza w wyszukiwarce,
    zakładki z liczbami („Obiekty (1 248)”, „Kolekcje (3)”), tytuł sekcji „Wyniki
    wyszukiwania”, licznik „Znaleziono 1 248 obiektów dla „…””, sortowanie „Trafność”,
    paginacja „z 63”. Czeka na akceptację.
  - Audyt stylów tekstu na makiecie: bez stylu były m.in. przełącznik, filtry (etykiety
    12/600 i wartości 15/500), licznik wyników (15/450), sortowanie oraz teksty kart.
    Przełącznik i karta mają już style; filtry/licznik/sortowanie — do decyzji (etykiety
    filtrów 12/600 nie mają odpowiednika w stylach).
  - **Widok „Lista”** (prośba użytkownika): makieta „Desktop Large - Lista” `8970:7119` —
    kopia widoku kafelków z przełącznikiem widoku na „Lista” i 10 obiektami jeden pod drugim
    (lista pionowa, odstęp 12, pełna szerokość kolumny 1320). Nowy komponent **„Object row”**
    `8970:7103` (stoi nad makietą, y ≈ −30165): po lewej zdjęcie **523,2×348,8** — szerokość
    dwóch boksów filtrów nad listą (2 × 257,6 + odstęp 8; prośba użytkownika), proporcje 3:2
    i kadr jak na karcie; prawa krawędź zdjęcia równo z prawą krawędzią boksu „Instytucja”.
    Po prawej treść z paddingiem 24 (góra/dół) i 24 (boki): u góry grupa „Top” (etykieta
    kategorii + „Dodaj do kolekcji” 40×40, pod nią tytuł H4 + autor Table Thin, odstęp 16),
    na dole instytucja z ikoną. Właściwości tekstowe: Tytuł, Autor, Instytucja; zdjęcie
    i kategoria jako nadpisania w instancji. Wiersz: 1320 × ~349 (Hug), ramka #E5E5E5.
    Makieta listy ma przez to ~5520 px wysokości.
    **Opis obiektu** (prośba użytkownika): między „Top” a „Institution row” tekst „Opis”
    — styl **Body 3** (Duży desktop, 16/350, interlinia 150%), kolor #333333, maks. szerokość
    640 px (2–3 linie), właściwość tekstowa „Opis”. Treść `Content`: wyrównanie do góry,
    odstęp 16; opis wypełnia wolną wysokość, więc instytucja zostaje na dole. Opisy na
    makiecie są **zmyślone** (wypełniacz do makiety) — przed wdrożeniem podmienić na prawdziwe
    z danych KRONIK@.
    „Wycieczka statkiem” ma wariant etykiety **Film** — także na kartach w „Desktop Large -
    Cards” i w wynikach wyszukiwania (wcześniej był tam wariant „Sztuki wizualne” z ręcznie
    zmienionym tekstem „FILM” i kolorem; poprawione, wygląd bez zmian). W kopii zapasowej
    zostało po staremu.
  - **Podpowiedzi wyszukiwania** (prośba użytkownika, wzór: screen z obecnego serwisu):
    na makiecie wyników `8949:9184` między przełącznikiem Obiekty / Kolekcje a tytułem
    „Wyniki wyszukiwania” blok „Podpowiedzi wyszukiwania” (`9002:8224`): „Czy chodziło Ci o?”
    i „Możesz obejrzeć także” (etykiety Body 4 Bold), pod nimi zawijane rzędy podpowiedzi
    (odstęp 8). Treści przykładowe. Na stronie BUTTONS nie było pasującego elementu —
    najbliżej klasa „B · Outline button 1 px (kompaktowy)” (44–46 px, z ikoną), więc
    powstał nowy przycisk **„Podpowiedź wyszukiwania”** (`9002:341`, w tabeli „Nowe
    przyciski”): bez ikony, 36 px, padding 0/14, tekst Button 15/450 #222222, ramka 1 px
    #222222, białe tło; Stan = Domyślny / Hover (#F3F3F3) / Focus (pierścień 2 px);
    długi tekst ucinany wielokropkiem (maks. 640 px); właściwość „Etykieta”.
    Uwaga: odstęp w grupie nad listą to 100 px (zmiana użytkownika) — działa też nad
    i pod blokiem podpowiedzi.
    **Białe tło na całą szerokość** (prośba użytkownika): blok stoi pod przełącznikiem
    Obiekty / Kolekcje; treść w kolumnie 1320, białe tło jak niżej. Ramka-rodzic `8949:9452` ma wyłączone przycinanie. We Framerze zrobić
    to jako osobną sekcję na pełną szerokość z białym tłem i kontenerem o szerokości kolumny.
    (Próba z podpowiedziami bezpośrednio pod hero i przełącznikiem pod nimi — cofnięta na
    prośbę użytkownika.) Przełącznik i podpowiedzi są w ramce „Przełącznik + podpowiedzi”
    (`9009:7886`, gap 24); od niej do tytułu „Wyniki wyszukiwania” zostaje 100 px.
    **Białe tło od krawędzi hero** (próba, prośba użytkownika): absolutny prostokąt
    „Tło – białe, pełna szerokość” (`9010:7888`) w tej ramce — od dolnej krawędzi hero
    (sięga w górny padding sekcji, 24 px) do końca podpowiedzi, 1440 px; obejmuje przełącznik.
    Między przełącznikiem a „Czy chodziło Ci o?” **szara kreska 1 px #E5E5E5 na szerokość
    kolumny** (z bocznymi marginesami 60 px, jak tytuł i filtry; początkowo była na całą
    szerokość — zmiana użytkownika; „Linia – pełna szerokość”, `9010:7887`): 24 px pod przełącznikiem, 40 px nad
    podpowiedziami; pod podpowiedziami 40 px do końca białego pasa (padding bloku 16/40).
  - **Brak wyników** (prośba użytkownika): makieta **„Desktop Large – brak wyników”**
    `9015:7886` (kopia makiety wyników; położenie — patrz góra pliku). Fraza z literówką „Muzeum Wojska Polskeigo”,
    przełącznik „Obiekty (0)” / „Kolekcje (0)”, pierwsza podpowiedź „Czy chodziło Ci o?” =
    poprawna fraza; grupa „Możesz obejrzeć także” usunięta (przy braku wyników tylko
    „Czy chodziło Ci o?” — decyzja użytkownika). Pasek wyników, siatka kart i paginacja usunięte; w ich miejscu blok
    „Brak wyników” (`9015:9141`, wyśrodkowany, padding 120 góra/dół): napis **„Brak wyników”**
    w stylu **H2 - Nazwy sekcji** (Duży desktop, 28/450, czarny — ten sam co tytuł „Wyniki
    wyszukiwania”; decyzja użytkownika, wcześniej H1 38/400) + zdanie pomocy w Body 3
    #333333 (maks. 640 px). Tytuł sekcji i filtry zostają.
  - **Wyniki wyszukiwania — pogrubiona liczba wyników:** w „Znaleziono 336 obiektów” liczba
    w Aspekta 600, reszta zdania bez zmian (15/450).
  - We Framerze nic nie zmieniano.

- 2026-11-17 — **Figma, strona „BUTTONS”, komponent „Pagination”** (`9037:21913`, wariant
  „Desktop Large i Small” `9037:21912`): „Page change” (strzałki + numer strony) jest zawsze
  **wyśrodkowany względem całej szerokości komponentu**, także po rozciągnięciu instancji
  (prośba użytkownika; sprawdzone przy 900 / 1024 / 1320 / 1440 px). Ramka „pagination buttons”
  (`9037:21848`) była stała (740 px, bez auto‑layoutu, dosunięta do prawej) — teraz to poziomy
  auto‑layout na całą szerokość („Fill”) z trzema elementami: pusta „Lewa kolumna (odstęp)”
  (`9071:334`, Fill) · „Page change” (Hug) · „Prawa kolumna” (`9071:335`, Fill, wyrównanie do
  prawej) z „Pokaż na stronie”. Obie boczne kolumny dzielą wolne miejsce po równo, więc środek
  zawsze wypada na środku komponentu. Działa, dopóki „Pokaż na stronie” (246 px) mieści się
  w połowie wolnego miejsca (komponent ≥ ~660 px). We Framerze: ten sam układ (stack poziomy,
  dwie kolumny 1fr po bokach) albo grid 1fr / auto / 1fr. Wariant „Tablet i Mobile” bez zmian
  (tam „Page change” już był wyśrodkowany).

- 2026-11-17 — **Figma, „3. Zasoby/Obiekty”: paginacja = komponent „Pagination”** (`9037:21913`,
  ten sam co na nowych makietach „4. Zasoby/Kolekcje”, ramka `9037:16516`). Odłączone ramki
  „Pagination section” zastąpione instancjami (szerokość „Fill”): wariant „Desktop Large
  i Small” na Desktop Large - Cards (`9074:18271`), Desktop Small - Cards (`9074:18302`),
  Desktop Large - Lista (`9074:18365`) i wynikach wyszukiwania (`9074:18396`, nadpisanie „z 63”);
  wariant „Tablet i Mobile” na Tablet (`9074:18333`) i Mobile (`9074:18349`) — jak w Kolekcjach,
  tam **bez „Pokaż na stronie”** (wcześniej na Mobile było pod numerami stron).
  Kopie zapasowe i starsze propozycje bez zmian.

- 2026-11-17 — **Figma: nowy przycisk „Sortowanie”** (prośba użytkownika) — zestaw komponentów
  `9078:20251` w tabeli „Nowe przyciski” (wiersz „Sortowanie (lista rozwijana)” `9078:20214`,
  sekcja „Strona: Zasoby · Lista obiektów”). Zrobiony z przycisku z makiety (wygląd 1:1:
  48 px, padding 14/20/13/20, białe tło 90 %, ramka 1 px #E5E5E5 60 %); własna strzałka
  zamieniona na **lucide/chevron-down** 16 px (linia 1,5 px #7D7D7D) zgodnie z zasadą ikon.
  Właściwości: **Stan** = Domyślny `9078:20235` / Hover `9078:20238` (tło #F3F3F3) / Focus
  `9078:20244` (pierścień 2 px #222222 z 2 px odstępu — jak „Podpowiedź wyszukiwania”),
  teksty **Etykieta** („Sortuj: ”) i **Wartość**. Teksty nadal bez stylu tekstu (jak było —
  punkt w „Do zrobienia”). Instancje na makietach Obiektów: Desktop Large - Cards, Desktop
  Small, Tablet, Mobile, Lista i wyniki wyszukiwania (tam Wartość = „Trafność”); szerokość
  249 → 250 px. Kopia zapasowa i „Obiekty - propozycja” bez zmian. Kolekcje mają inny, starszy
  przycisk „Sortuj według” — nie ruszany.

- 2026-11-17 — **Figma, „Lista obiektów” — 4 makiety Cards** (ramka `9037:22307`: Desktop Large
  `8670:4812`, Desktop Small `9044:8436`, Tablet `9044:10606`, Mobile `9044:12750`): audyt
  stylów tekstu z wersjami na breakpointy (H1–H4, Body 1–3, Body 4 Thin 2, Metric, Breadcrumbs)
  — prośba użytkownika. Na Desktop Small / Tablecie / Mobile 42 teksty miały style „Duży
  desktop ≥1440” i dostały odpowiedniki swojego breakpointu: tytuł hero „Przeglądaj obiekty”
  (H1: 36 / 34 / 30 px), tytuły kart „Object tile” (H4: 20 → 18 px), „Czynna w dni robocze…”
  w stopce (Body 4 Thin 2: 15 / 14 / 14 px). Wszystkie trzy były **nadpisaniami w instancjach**
  (komponenty „Header Text”, „Footer desktop” i „Object tile” same nie mają tych stylów), więc
  poprawione w instancjach, komponenty bez zmian. Makiety niższe o 12 / 18 / 40 px (tytuły
  kart 18 px). Desktop Large, okruszki i „Lista obiektów” (H2) były już poprawne.
  **Bez stylu tekstu** (poza zakresem — nie mają wersji na breakpointy w systemie): filtry
  (12/600 i 15/500), licznik wyników, „Sortowanie”, część stopki (adres/kontakt 16/15/14 px
  — rozmiar zmienia się z breakpointem, ale bez stylu) i pasek gov.pl.
  Uwaga: „Object tile” nie ma wariantów na breakpointy — styl tytułu na mniejszych
  breakpointach trzyma się na nadpisaniu w instancji (nowe karty wstawiane z komponentu mają H4
  Dużego desktopu; trzeba przełączyć ręcznie albo dodać warianty).

- 2026-11-17 — **Figma: usunięty komponent „Header Text”** (`3380:50356`, strona „- KOMPONENTY -
  nowe (robocze)”; tytuł + podtytuł w hero, warianty D Large Default / D Small / Tablet / Mobile)
  — zbędny i nieaktualny (decyzja użytkownika). Wszystkie **71 kopii odłączono** (decyzja
  użytkownika: „odłączyć i usunąć”) — są teraz zwykłymi ramkami „Header Text” z tym samym tekstem
  i stylem, wygląd makiet bez zmian (m.in. hero na Obiektach, Kolekcjach, Instytucjach,
  O Portalu, Głównej 2.0, Typography, NAWIGACJA I i na stronach „❌ nieaktualne”). Style H1
  na 4 makietach „Lista obiektów – Cards” sprawdzone po odłączeniu (38 / 36 / 34 / 30 px).

- 2026-11-17 — **Figma, pasek wyszukiwarki „Toolbar”** (`9096:32681`, strona BUTTONS),
  wariant **Mobile** (`9096:32682`): wysokość 56 → **52 px** (prośba użytkownika), padding
  góra/dół 5 → 3 (jak z prawej: 3 px odstępu wokół czerwonego przycisku). Czerwony przycisk
  „Search_button” (`9096:32694`) przebudowany na auto‑layout: czerwone tło na samej ramce
  (usunięty czerwony prostokąt‑wektor), ikona lucide/search wyśrodkowana, wysokość „Fill”
  + **zablokowane proporcje 1:1** — przycisk sam dopasowuje się do wysokości paska (52 → 46×46;
  sprawdzone na kopii: 48 → 42, 60 → 54). Kontenery „3” i „Frame 427320017” też „Fill” w pionie.
  Wariant Default (56 px, 16 kopii) bez zmian; wariant Mobile nie miał jeszcze kopii.

- 2026-11-17 — **Figma, strona „BUTTONS”: audyt i ujednolicenie kolorów przycisków**
  (decyzje użytkownika; ramka „nieaktualne” pominięta na jego prośbę):
  - **Jeden zielony przycisków: #15682D, hover #115525.** Było też #1A7936 (hover #14602B)
    w secondary „Publikuj” (Specyfikacja, sekcja 44 px, tabela przeglądu), w hoverze zielonego
    wiersza tabeli stanów i w „Przyciskach dodawania” (`8578:129878`) — poprawione.
    Zmienna **`mode/OK`** (oba tryby) też zmieniona #1A7936 → **#15682D** (wpływa na cały plik).
  - **Ramki w kolorze akcji zawsze z kryciem 80 %** — także przyciski z samą ikoną (były 40 %,
    neutralny 30 %): tabela stanów `8578:129228`, „Same ikony” w Specyfikacji, komponent
    „Przycisk Dodaj do kolekcji” wariant W ramce (`8975:7834`, zmiana idzie do instancji).
  - **Stan nieaktywny = krycie 40 %** (tabela stanów i „Dodaj do kolekcji” miały 35 %).
  - Próbka palety „Kronika Blue Hover” → **#142C69** (odłączona od starego stylu #163F7D);
    „Cofnij publikację” w sekcji 44 px: #4B5563 → czarny secondary (tekst #1A1A1A, ramka
    #333333); nazwy warstw: próbki „Kronika Green” / „Kronika Red”, przycisk „Przycisk/Green”.
  - Zostało (nie ruszane, do decyzji): style kolorów w pliku są nieaktualne („Kronika Blue”
    #1C4F9C, „Kronika Blue Hover” #163F7D), zmienne palety nie zgadzają się z przyciskami
    (`palette/KRONIKA` #134571, `palette/RED KRONIKA` #BF1F39, `Kronika-black` #000000),
    kolory przycisków są wpisane na sztywno; sekcja „Linki” w Specyfikacji to kopia „Disabled”;
    w tabeli ok. 8 różnych prawie-czarnych (#1A1A1A, #121212, #111214, #0A0A0A, #000000…).
  - Ramka „Kolory podstawowe” → „Paleta Kronika”: Blue, Green, Black i Red ułożone w kolumny
    jak w sekcji „Primary” Specyfikacji — kolor podstawowy na górze, hover pod spodem
    (Blue hover #142C69, Green hover #115525, Black hover #333333, Red hover #7E1728;
    kolumny `9126:352` / `9126:353` / `9126:356` / `9126:359`). Podpis „RED #9A1C31” → „Red · #9A1C31”.
    Szarości i biały bez hoveru, w tym samym rzędzie.
    W każdej kolumnie trzecia próbka **hover Secondary** (białe tło + kolor akcji 6 %, ramka
    80 % — czarny #333333 100 %, tekst w kolorze akcji); podpisy „X · hover Primary · #…” /
    „X · hover Secondary · #… 6%”, pod paletą opis obu zasad hoveru (warstwa „Opis hover”).
    **Aktualny układ (prośba użytkownika):** w każdej kolumnie 4 próbki — kolor podstawowy ·
    Primary tło hover · **Secondary ramka 1 px** (białe tło, kolor akcji 80 %, czarny #333333
    100 %) · **Secondary tło hover** (kolor akcji 6 % na bieli; ramka i tekst bez zmian).
    Po lewej kolumna podpisów wierszy „Opis wierszy” (`9132:377`). Opis „Opis hover” pod
    paletą użytkownik usunął — nie przywracać.
    Nazwy kolorów (Blue, Green, Black, Red, Biały) są **nagłówkami kolumn** (12/450 #737373,
    jak hexy w sekcji Primary); w podpisach próbek już bez nazwy koloru (np. „Primary · tło
    hover · #142C69”). Biały w osobnej kolumnie; w kolumnie podpisów wierszy pusty odstęp
    16 px, żeby wiersze się zgadzały. Użytkownik sam przeniósł Dark gray do drugiego rzędu
    („Kolory użyte w niektórych przyciskach”), usunął „Ramkę przycisku” i ramkę z próbek
    „tło hover Secondary”.
  - Usunięte podpisy „domyślny · tło strony #F3F3F3” (3×: dwa wiersze „Pasek wyszukiwarki”,
    „Paginacja”) — tło tych wierszy to w rzeczywistości #F6F6F6; podpięte do stylu
    **Background Gray** (`8378:125152`, `8414:151`, `8347:118795`, `8362:121286`). #F3F3F3 zostaje
    tylko jako tło hover („Anuluj”, „Podpowiedź wyszukiwania”, „Sortowanie”) — do decyzji.
  - **Linki = #193680** (jak Kronika Blue; prośba użytkownika). Na stronie BUTTONS #2248A5 →
    #193680: próbka „Link” w palecie, „Strona instytucji”, „Regulamin”, „Zasady RODO”,
    „Strona obiektu” (+ ikona), „40” / „60” w „Pokaż na stronie” (też w komponencie
    Pagination), ikona wariantu „Bez ramki” przycisku „Dodaj do kolekcji”. Czarne podkreślone
    „Czytaj więcej” / „Zobacz wszystkie” (#1A1A1A) bez zmian.
  - **Czarna ramka przycisków secondary = #1A1A1A z kryciem 80 %** (prośba użytkownika; najpierw
    ustawione 60 %, potem zmienione na 80 % — tak jak ramki kolorowe; było
    #333333 100 %, #333333/80 przy A+ i English, #1A1A1A/80 przy ikonach, #222222 przy
    „Podpowiedzi wyszukiwania”). Zmienione na BUTTONS: wszystkie przyciski outline 44/46 px,
    Anuluj (wszystkie stany), Secondary/Black, Zaloguj się (jasne tło), Zalogowany, strzałki
    ← →, A+ / kontrast / English (stan domyślny), neutralne przyciski z ikoną (tabela stanów,
    „Same ikony”), „Podpowiedź wyszukiwania” (3 stany), ilustracje „Anatomia”, próbki
    w palecie i podpisy/opisy w Specyfikacji. **Nie ruszane:** stany wciśnięte z ramką 2 px
    (A+, kontrast, English), pierścienie focus, przyciski „down” z czarnym tłem.
  - **Szarości:** Dark gray **#656766** (zmienna `palette/Kronika-gray`) = **help text / tekst
    szary** (placeholdery wyszukiwarki, „Wybierz jednostkę”, „Sortuj:”, odpowiedź FAQ) — tak
    podpisany w palecie. **Light gray #8A8A8A usunięty** (decyzja użytkownika): próbka skasowana,
    na stronie BUTTONS zastąpiony #656766 (nagłówki grup w „Przycisku Panel”, podpisy stanów
    w wierszu „Anuluj · Zapisz”). Makiet stron nie sprawdzano — mogą mieć stare kolory.

- 2026-11-17 — **Figma, nowy komponent „Pasek wyszukiwarki”** (`9147:381`, strona BUTTONS,
  tam, gdzie leżały dwie ramki „Toolbar” od użytkownika — pusta ramka‑opakowanie usunięta).
  Zrobiony z tych ramek (prośba użytkownika). Właściwości: **Breakpoint** = Desktop (660×56)
  / Mobile (358×52, czerwony przycisk Fill + proporcje 1:1) i **Stan** = Pusty (placeholder
  #656766, Button Thin) / **Wypełniony** — „po wpisaniu treści”: tekst czarny #0A0A0A
  (przykład „Wypoczynek w czasach PRL”) + ikona **lucide/x** 18 px („Wyczyść”, jak w ramce
  „Po wpisaniu treści” `9096:35460`), 12 px przed przyciskiem szukania. Warianty: Desktop
  Pusty `9147:377` / Wypełniony `9147:378`, Mobile Pusty `9147:379` / Wypełniony `9147:380`.
  Warstwa „Wyczyść” jest we wszystkich wariantach (w Pustym ukryta), pole tekstu „Fill”,
  długi tekst ucinany wielokropkiem. Stary komponent „Toolbar” (`9096:32681`, 16 kopii na
  makietach) **bez zmian** — kopie nie są podmienione (do decyzji użytkownika).

- 2026-11-17 — **Figma: „Przełącznik widoku” — wariant mobilny bez tekstu** (prośba użytkownika).
  Zestaw `8949:6740` (tabela „Nowe przyciski”) ma nową właściwość **Urządzenie = Desktop /
  Mobile**. Mobile: `Widok=Kafelki` `9156:339`, `Widok=Lista` `9156:348` — same ikony
  (layout-grid / layout-list), segmenty 40×40, całość 92×48; ramka, kolory i aktywny segment
  jak w Desktop. Dotychczasowe warianty → `Urządzenie=Desktop`; 8 kopii na stronie „3. Zasoby/
  Obiekty” bez zmian (Desktop). Opis wiersza w tabeli uzupełniony.

- 2026-11-17 — **Figma: „Sortowanie” — wariant mobilny bez etykiety „Sortuj:”** (prośba
  użytkownika). Zestaw `9078:20251` ma nową właściwość **Urządzenie = Desktop / Mobile**.
  Mobile dla każdego stanu: Domyślny `9164:343`, Hover `9164:350`, Focus `9164:357` (pierścień
  focus dopasowany do szerokości) — sama wartość + chevron, szerokość Hug (~201 px), wysokość
  48 px, reszta jak Desktop. Warianty Mobile w drugim rzędzie zestawu. 6 kopii na „3. Zasoby/
  Obiekty” bez zmian (Desktop). Opis wiersza w tabeli uzupełniony.

- 2026-11-17 — **Figma, „Nowe przyciski” (`8988:324`): kolory ujednolicone z systemem przycisków**
  (prośba użytkownika). W komponentach z kolumny „Podgląd”: czarny tekst/kreska/ikony
  #121212 i #222222 → **#1A1A1A**; szary nieaktywny #6C6C6C i strzałka sortowania #7D7D7D →
  **#656766**; tło hover „Podpowiedzi wyszukiwania” i „Sortowania” #F3F3F3 → **białe + #1A1A1A
  6 %** (zasada hover secondary); pierścienie focus #222222 → #1A1A1A; ramka „Sortowania”
  #E5E5E5 60 % → **100 %**, tło białe 90 % → 100 %; linia bazowa przełącznika Obiekty / Kolekcje
  #D6D6D6 → #E5E5E5; usunięta niewidoczna biała ramka 31 % z jego wariantów. Po zmianie
  w podglądach tylko: #193680 (100/80/6 %), #1A1A1A (100/80/6 %), #656766, #E5E5E5,
  #F1F1F1 (aktywny segment), #FFFFFF. „Dodaj do kolekcji” był już zgodny.
  Poza ramką: „Wybierz jednostkę” na BUTTONS nadal ma ramkę #E5E5E5 60 % — do decyzji.

- 2026-11-17 — **Figma, „Wyniki wyszukiwania” i „Brak wyników” — pozostałe 3 breakpointy**
  (prośba użytkownika). Każda nowa makieta to **kopia odpowiedniej makiety „Cards”** (ramka
  `9096:35581`) — nawigacja, hero, filtry, karty, paginacja, stopka, paddingi i style tekstu
  dokładnie jak w Cards danego breakpointu — z elementami wyników przeniesionymi z Desktop Large:
  pasek wyszukiwarki w stanie **Wypełniony** („Muzeum Wojska Polskiego”; Tablet — wariant Desktop
  584 px, Mobile — wariant Mobile, jak w Cards), blok „Przełącznik + podpowiedzi” (białe tło na
  całą szerokość makiety, od dolnej krawędzi hero), tytuł „Wyniki wyszukiwania” (H2 danego
  breakpointu), „Znaleziono **336** obiektów”, sortowanie „Trafność”, paginacja „z 63”; odstępy
  sekcji jak w Desktop Large (wyniki 80/80, brak wyników 120/80). Długa podpowiedź „Katalog
  zbiorów Muzeum Wojska Polskiego…” **usunięta ze wszystkich 8 makiet** (decyzja użytkownika,
  tego samego dnia); białe tło bloku podpowiedzi dopasowane. Uwaga na przyszłość: w komponencie
  „Podpowiedź wyszukiwania” nie da się nadpisać maks. szerokości (640 px) w instancji — na Mobile
  długą etykietę trzeba ograniczać stałą szerokością instancji + tekst „Fill”.
  Brak wyników: blok „Brak wyników” z H2 i Body 3 danego breakpointu.
  Makieta „Desktop Large – brak wyników” **przesunięta niżej** (y −43826 → −39090), bo wysoka
  makieta Mobile wyników zachodziła na jej rząd.
  W nowych makietach „Section heading” ma szerokość „Fill” — w Cards Desktop Small i Tablet ma
  stałe 1320 px (kreska pod „Lista obiektów” wychodzi poza kolumnę) — **w Cards nie poprawiano**.
  Celowo **jak w Cards, nie jak w Desktop Large wyników** (rozbieżności w samych makietach DL,
  do decyzji): kolejność filtrów (Cards: Kategoria, Instytucja, Autor, Data publikacji, Więcej;
  wyniki DL: …Data publikacji, Autor…), odstępy w hero (Cards: gap 28 + 20 px pod paskiem; wyniki
  DL: gap 32, bez dolnego paddingu), sortowanie na Mobile w wariancie Desktop (z „Sortuj:”).
  Uwaga: w „brak wyników” pasek wyszukiwarki pokazuje „Muzeum Wojska Polskiego”, a opis frazę
  z literówką „Polskeigo” — skopiowane 1:1 z Desktop Large, do decyzji.

- 2026-11-17 — **Figma, makieta „Kolekcje” Desktop Large** (`9186:39665`, strona „3. Zasoby/Obiekty
  - TBC”; prośba użytkownika):
  - **Hero = jak w „Desktop Large - Cards”:** wysokość 340 → **380 px** (tło „tło” i ramki w nim
    380, tekstura i grafika „Group 5879S” ustawione jak w Cards). „Header Text Container” jak
    w Cards (Fill × Fill, wyśrodkowany w pionie, gap 28); w nim nowa ramka **„Tytuł i wyszukiwarka”**
    (`9192:17776`, kopia ramki z Cards: gap 28, dół 20) — tytuł „Kolekcje” (dotychczasowy
    „Header Text”) + **instancja „Pasek wyszukiwarki”** Desktop / Pusty (`9192:17780`, placeholder
    jak w Cards: „Wyszukaj z ponad 19 milionów zbiorów”). Opis „Przeglądaj publiczne kolekcje
    obiektów nauki i kultury” **ukryty** (nie usunięty — jak w Cards). Pasek wypada w tym samym
    miejscu co w Cards (132,5 px od góry hero).
  - **Usunięty stary pasek „Toolbar”** (z „Sortuj według”) spod nagłówka „Kolekcje publiczne”.
  - **Siatka kolekcji: 4 w rzędzie** zamiast 3 — kafelki „Collection tile” (wariant Desktop 1440)
    432 → **321 px** (jak „Object tile” w Cards, odstęp 12), 3 rzędy po 4; „Meta row” w kafelkach
    przestawiony na „Fill” (miał stałe 406 px i wychodził poza kafelek).
  - **Okładki = jak w Obiektach: 321×214, skalowanie „Fill” (bez zniekształceń)** — prośba
    użytkownika. Wysokości „Cover image” nie da się nadpisać w instancji, więc w komponencie
    „Collection tile - framer”, wariant Desktop 1440 (`6354:3841`), okładka (`6354:3843`) ma
    **zablokowane proporcje 3:2** (432×288) — wysokość wynika z szerokości. Pozostałe 85 kopii
    tego wariantu (wszystkie 432 px: Obiekty, „4. Zasoby/Kolekcje”, Instytucje) bez zmian
    (sprawdzone: 432×288). **Obrazki podmienione na odpowiedniki z „Desktop Large - Cards”**
    (te same pliki obrazów co „Object tile”, skalowanie Fill): Historia Wojska Polskiego ← Anioł
    przy poległym rycerzu, Jan Stanisławski ← Błonia pod lasem, Spacer po Warszawie ← Centrum
    Warszawy, Wirtualny spacer po muzeach ← Dziewczęce popiersie, Niezbędnik maturzysty ← Kobieta
    w chuście, Eliza Orzeszkowa ← Portret Elizy Orzeszkowej, Dzień dziecka ← Przy furtce ogrodu,
    Mikołaj Kopernik ← Wizerunek Mikołaja Kopernika, WIOSNA ← Wiosna, Wielkanoc ← Wołanie dzwonu,
    Maria Skłodowska-Curie ← Maria Skłodowska-Curie, Wakacje ← Wycieczka statkiem.
  - Makieta niższa: 3678 → 2938 px.
  - **Placeholder paska: „Wyszukaj w kolekcjach”** (decyzja użytkownika) — na wszystkich 4 makietach.
  - **Pozostałe breakpointy** (prośba użytkownika): **kopie** makiet ze strony „4. Zasoby/Kolekcje”
    (`8175:8159` / `8175:9268` / `8175:10363` — oryginały tam **bez zmian**) postawione obok Desktop
    Large na stronie „3. Zasoby/Obiekty - TBC”: **Desktop Small `9197:24055`**, **Tablet
    `9197:24360`**, **Mobile `9197:24671`**. Na każdej: hero = **kopia hero z Cards danego
    breakpointu** (380 px, pasek wyszukiwarki — Desktop na DS i Tablecie, Mobile na Mobile;
    teksty zmienione na „KRONIK@ / Kolekcje / Kolekcje publiczne” i tytuł „Kolekcje”), usunięta
    stara wyszukiwarka spod „Kolekcje publiczne” (DS „Input wrapper”, Tablet „Toolbar”, Mobile
    „Search bar”), **obrazki podmienione** na odpowiedniki z Obiektów (to samo przypisanie co
    w Desktop Large, skalowanie Fill). Liczba kolumn i wymiary okładek były już jak w Cards:
    DS 3 × 309×206, Tablet 2 × 383×255, Mobile 1 × 366×244.
  - **Rząd 4 makiet Kolekcji przesunięty wyżej** (y −60688 → **−64327**, x jak kolumny Cards:
    5909 / 7499 / 8673 / 9633), żeby wysoka makieta Mobile nie nachodziła na „Cards” (y −56855).

- 2026-11-17 — **Figma, strona „3. Zasoby/Obiekty”** (`6885:93257`, nazwa już bez „- TBC”; makiety
  leżą teraz w ramce „Frame 427320022” `9228:96066`): wszystkie **12 nagłówków sekcji z kreską**
  (odłączone ramki „Section heading”: tytuł + kreska 1 px #333) zastąpione **instancjami komponentu
  „Section heading”** (`3350:38625`) w wariancie breakpointu (prośba użytkownika): 4 × Cards
  („Lista obiektów”), 4 × wyniki i 4 × brak wyników („Wyniki wyszukiwania”). Teksty bez zmian,
  przełączniki „Link tekstowy” i „Strzałki” wyłączone (jak było), nazwa warstwy „Section heading”,
  to samo miejsce w „nagłówek i filtry”. Szerokość jak w oryginałach: Desktop Large — stałe 1320 px
  (rodzic „nagłówek i filtry” ma tam szerokość Hug), pozostałe — „Fill”. Wymiary 1:1 z oryginałami,
  nic się nie przesunęło. Pominięty tytuł ramki opisowej „Lista obiektów – nowe komponenty”
  (`8983:7847`) — to nagłówek dokumentacji, nie sekcja makiety.

- 2026-11-17 — **Figma, strona „4. Zasoby/Kolekcje”** (`6335:42234`; prośba użytkownika): to samo.
  Nagłówki „Kolekcje publiczne” były tu instancjami **starej lokalnej kopii** „Section heading”
  (`6415:32201`, warianty z literówką „Dekstop Large”) — ten komponent nie leży już na żadnej
  stronie (osierocony). Wszystkie **14** takich instancji (makiety „Kolekcje publiczne - kafelki”
  Desktop 1444/1445/1446/1024/Tablet/Mobile, stary rząd Desktop Large/Small/Tablet/Mobile
  `8175:…` i nowy rząd `9199:…`) + **1 odłączona ramka** („Wyniki wyszukiwania” w „Desktop Large –
  wyniki wyszukiwania” `9199:34164`) zastąpione instancjami „Section heading” `3350:38625`
  w wariancie breakpointu. Teksty, szerokości (Fill / stałe — jak w oryginałach; Desktop Small
  ma stałe 952 px) i wysokości bez zmian. Nie ruszane: „Wynik wyszukiwania” (H3 w „Heading row /
  Learn more”, bez kreski) — to nie nagłówek sekcji.

- 2026-11-18 — **Figma, strona „tabele - robocze”** (`9258:24783`), makieta „Zmiana hasła - 1441”:
  tabela `9258:25269` (dawniej „Tabela / Użytkownicy”, teraz **„Tabela / Zaproszenia”**)
  przerobiona wg zrzutu od użytkownika (prośba użytkownika). Kolumny: E-mail (Fill) · Data
  utworzenia 190 · Data ważności 190 · Status 170 (wyśrodkowany) · Członek jednostki 180 ·
  Akcje 130 (wyśrodkowane). Ramki tabeli, nagłówka i wierszy (ID, tła, kreski) bez zmian,
  komórki zbudowane od nowa na auto‑layoucie; wiersze min. 88 px. **Style tekstu
  (istniejące):** nagłówki → Table Bold (14/500; wcześniej 14/600 bez stylu), treść → Table
  Thin, status → Uppercase S (Wysłane #FB7321, Zaakceptowane #0F793B), data akceptacji pod
  statusem → Body 6 Footer #737373, członek jednostki → Links #2A307D. Kolory statusów i linku
  wzięte ze zrzutu — w pliku nie ma dla nich stylów kolorów. Akcje (tylko przy „Wysłane”):
  przyciski 44×44 jak wcześniej w tabeli, ikony Lucide `refresh-cw` („Wyślij ponownie”)
  i `square-x` („Anuluj zaproszenie”), 20 px. Paginacja pod tabelą bez zmian (20/40/60;
  na zrzucie 50/75/100 — do decyzji).

- 2026-11-18 — **Figma, strona „3. Zasoby/Obiekty”** (`6885:93257`): nad rzędami makiet stoją
  **zielone etykiety „aktualne”** (tekst Aspekta 500 / 88 px #135530 + zielona belka #088540,
  szerokość 4114 px = rząd 4 makiet). Wszystkie trzy miały skopiowany tekst „Widok przed
  wyszukaniem kolekcji” — poprawione wg tego, co pokazują makiety (prośba użytkownika):
  `9317:45054` (x 5909, nad Cards) → „Widok przed wyszukaniem obiektów”, `9317:45058`
  (x 11158) → „Wyniki wyszukiwania obiektów”, `9317:45061` (x 16382) → „Brak wyników
  wyszukiwania obiektów”. Nazwy warstw tekstu = treść. Rząd pod „brak wyników”
  (`9299:43811`, wyniki z 2 obiektami, y −48074) nie ma etykiety — nie dodawano.

- 2026-11-19 — **Figma, menu boczne po zalogowaniu** (strona „NAWIGACJA I”, makieta „Tablet -
  zwinięte” `9403:42446`, „Drawer 580 (zwinięte)” `9403:43715`; prośba użytkownika):
  - **Nowy przycisk „Przycisk konta (menu boczne)”** — zestaw `9414:389` w tabeli „Nowe przyciski”,
    nowa sekcja **„Nawigacja · Menu boczne (tablet i mobile)”** (`9414:346`, wiersz `9414:348`).
    Właściwości: **Akcja** = Moje konto / Wyloguj się, **Stan** = Domyślny / Hover / Focus.
    64 px wysokości (jak „Zaloguj się lub zarejestruj konto” w menu wylogowanym i „English”),
    padding boki 16, treść wyśrodkowana, ikona 20 px przed tekstem, odstęp 8, tekst styl
    **Button** (15/450). **Moje konto** = Primary czarny (#1A1A1A, hover #333333, tekst i ikona
    białe, ikona **lucide/user**) — w tym samym miejscu co przycisk logowania w stanie
    wylogowanym. **Wyloguj się** = Secondary outline (białe tło, ramka 1 px #1A1A1A 80 %,
    hover + #1A1A1A 6 %, ikona **lucide/log-out**). Focus: pierścień 2 px #1A1A1A z 2 px odstępu.
    Ikony = instancje z kolekcji „Lucide Icons”, przeskalowane 24 → 20 px, linia 1,5.
    Warianty: Moje konto `9414:363` / `9414:367` / `9414:371`, Wyloguj się `9414:376` /
    `9414:380` / `9414:384`.
  - **Blok „Konto”** w menu (`9403:44319`, dawniej „Frame 427320014”): pionowy auto‑layout,
    odstęp **16 px**: „Imię i nazwisko” (`9403:43723`) w stylu **H4 - Nagłówki (Tablet)**
    (18/500, interlinia 130 %, #1A1A1A; wcześniej 15/450 bez stylu, przyklejone do przycisków)
    + „Przyciski konta” (`9403:44320`, poziomo, odstęp 16) z dwoma instancjami, szerokość Fill.
    Odstępy wokół bez zmian: 60 px od logo, 40 px do nawigacji. Literówka „Wylloguj się”
    poprawiona na „Wyloguj się”. We Framerze nic nie zmieniano.
  - **Zmiana użytkownika (później tego dnia):** blok „Konto” ma odstęp 40 px, imię i nazwisko
    („Adrianna Wysoczyńska”) w ramce „Frame 427320016” (`9403:46775`) z ukrytą kreską; obok stoi
    jego kopia makiety `9403:46776` (x −22).
  - **3 warianty stylu imienia i nazwiska do wyboru** (prośba użytkownika: „szlachetnie,
    minimalistycznie”; oryginał `9403:42446` bez zmian) — kopie makiety na prawo, y −1154,
    z podpisem nad każdą (H3 Tablet):
    **Wariant 1** `9420:3856` (x 900) — etykieta „ZALOGOWANO JAKO” (Uppercase S 13/450, #656766)
    + imię i nazwisko H3 Tablet (20/450), odstęp 8; 24 px do przycisków.
    **Wariant 2** `9420:5734` (x 1810) — monogram „AW” w kwadracie 52×52 (ramka 1 px #1A1A1A 80 %,
    jak A+ / kontrast; Aspekta 500 17, ls 4 %) + obok etykieta „ZALOGOWANO JAKO” i imię H4 Tablet
    (18/500), odstęp 16 / 6; 24 px do przycisków.
    **Wariant 3** `9420:7615` (x 2720) — jak wariant 1, ale cały blok konta (etykieta, imię,
    przyciski) to panel na tle **Background Gray** z paddingiem 24.
    **Wersje mobilne wariantów 1 i 3** (prośba użytkownika; baza: instancja komponentu
    „Mobile — zwinięte” `9403:50941` → komponent `9403:50940`, oba bez zmian): kopie odłączone
    od komponentu, stoją pod tabletowymi wariantami (y 304): **Wariant 1 — mobile** `9422:5690`
    (x jak `9420:3856`), **Wariant 3 — mobile** `9422:5922` (x jak `9420:7615`). Przycisk
    „Zaloguj się lub zarejestruj konto” zastąpiony blokiem „Konto” (gap 24): etykieta Uppercase S
    + imię **H3 Mobile** (18/450), przyciski konta obok siebie (Fill, odstęp 16 → ok. 171 px;
    w panelu 151 px). Panel w wariancie 3 na mobile ma padding **20** (na tablecie 24). Odstępy
    jak w bazie: 48 px od logo, 40 px do nawigacji.
    **Etykieta „Zalogowano jako” usunięta** (uwaga użytkownika: „mało zręczna”; jego pomysł:
    ikona po lewej, imię i nazwisko po prawej) — we wszystkich 4 kopiach (warianty 1 i 3,
    tablet i mobile) ramka „Użytkownik” jest teraz pozioma: **lucide/circle-user** 24 px
    (linia 1,5, #1A1A1A; inna niż lucide/user w „Moje konto”) + imię, odstęp 12, wyśrodkowane
    w pionie. Podpisy: „Wariant 1 — ikona + imię i nazwisko”, „Wariant 3 — ikona + imię
    i nazwisko na panelu (Background Gray)”. Wariant 2 (monogram) nadal ma starą etykietę.
    Czeka na wybór
    użytkownika — po wyborze przenieść do makiety głównej i usunąć pozostałe kopie.

- 2026-11-19 — **Figma: „Sortowanie” — ikona zamiast etykiety „Sortuj:”** (prośba użytkownika,
  „na wszystkich breakpointach”). W zestawie `9078:20251` (strona BUTTONS) we **wszystkich
  6 wariantach** (Desktop i Mobile × Domyślny/Hover/Focus) usunięty tekst „Sortuj: ”, a na
  początku ramki „Row” wstawiona ikona **lucide/arrow-up-down** (z kolekcji „Lucide Icons”,
  ogólna ikona sortowania; inne opcje w kolekcji: arrow-down-wide-narrow, arrow-down-a-z)
  **18 px, linia 1,5 px #656766** (jak chevron); odstępy w „Row” 8 px. Właściwość tekstowa
  **Etykieta usunięta** (została Wartość). Szerokość z wartością „Alfabetycznie (A–Z)” 250 → 227 px,
  pierścienie focus dopasowały się same. Desktop i Mobile wyglądają teraz identycznie (właściwość
  Urządzenie zostaje, żeby nie psuć kopii). Zmiana objęła wszystkie kopie: „3. Zasoby/Obiekty”
  (Cards 4 breakpointy, wyniki wyszukiwania), „4. Zasoby/Kolekcje” i „3. Zasoby/Obiekty - OLD”.
  Poprawka w „Mobile – wyniki wyszukiwania” (`9173:17255`): kopia miała nadpisane rozłożenie
  „space-between”, przez co ikona odjechała od tekstu — teraz stała szerokość 201 px, ikona +
  wartość po lewej (wartość „Fill”), chevron przy prawej krawędzi. Opis komponentu i wiersza tabeli
  zaktualizowane (z notką: w kodzie przycisk potrzebuje aria-label „Sortuj: <wartość>”).
  **Tego samego dnia warianty Desktop i Mobile połączone** (prośba użytkownika): usunięte warianty
  Urządzenie=Mobile (`9164:343`, `9164:350`, `9164:357`) i właściwość **Urządzenie**; zestaw ma teraz
  tylko **Stan** = Domyślny `9078:20235` / Hover `9078:20238` / Focus `9078:20244` + tekst Wartość.
  Dwie kopie z wariantu Mobile („Mobile - Cards” `9078:20275`, „Mobile – wyniki wyszukiwania”
  `9173:17255`) przełączone na Stan=Domyślny z zachowaniem wartości i układu (wyniki: nadal 201 px,
  chevron przy prawej krawędzi). Wszystkie 13 kopii w pliku podpięte do nowego zestawu.

- 2026-11-19 — **Figma: podpowiedzi wyszukiwania pod wynikami** (prośba użytkownika) — tylko makieta
  **„Desktop Large – wyniki wyszukiwania” `9439:24776`** (strona „3. Zasoby/Obiekty”; nowsza kopia,
  obok starszej `8949:9184`, której nie ruszano). Ramka „Podpowiedzi wyszukiwania” `9439:25049`
  („Czy chodziło Ci o?” + „Możesz obejrzeć także”) przeniesiona z bloku pod hero na **koniec sekcji
  „Section / Wyniki wyszukiwania”** — pod paginacją (odstęp 80 jak między pozostałymi częściami
  sekcji, padding ramki 16/28 → 0/0, pod nią dolny padding sekcji 140). **Przełącznik Obiekty /
  Kolekcje zostaje na swoim miejscu** (blok „Przełącznik + podpowiedzi” `9439:25046`, nazwa bez
  zmian); białe tło bloku (prostokąt rozciągany) skurczyło się samo do wysokości przełącznika
  (56 px od hero). Pozostałe breakpointy wyników — bez zmian (do decyzji, czy też przenieść).

## Do zrobienia

- [ ] Wyniki / brak wyników — ujednolicić z Cards: kolejność filtrów i odstępy w hero na Desktop
      Large; fraza w pasku „brak wyników” (z literówką czy bez?). („Section heading” w Cards — już instancje z „Fill”, 2026-11-17.)

- [ ] Placeholder wyszukiwarki — ujednolicić styl między breakpointami (Framer i Figma)?

- [ ] Zdecydować, czy na tablecie tytuł sekcji i opis mają mieć te same rozmiary fontu co na
      Desktop Primary (28/20 px zamiast 26/18 px — wymaga zmiany presetów, wpływa na całą stronę).
- [ ] Uzupełnić brief (pola TODO powyżej).
- [ ] „Lista obiektów”: ustalić kolejność filtrów (obecnie Kategoria, Instytucja, Data
      publikacji, Autor, Więcej).
- [ ] „Lista obiektów”: akceptacja makiety Desktop Large i wariantu wyników wyszukiwania;
      potem przycisk „×” do czyszczenia frazy w wyszukiwarce (komponent „Toolbar”).
- [ ] „Lista obiektów”: style tekstu dla filtrów, licznika i sortowania (etykiety 12/600 —
      nowy styl czy Uppercase S 13/450?).
- [ ] „Lista obiektów”: **po akceptacji makiety w Figmie** przenieść projekt strony do Framera
      (nie wcześniej — wymóg użytkownika). Potem pozostałe 3 breakpointy.
- [ ] Wyniki wyszukiwania — do decyzji, czy dodać: opcje wyszukiwania (checkboxy „Szukaj
      z warstwą tekstową OCR”, „Szukaj tylko w tytułach” z ikoną informacji), pasek aktywnych
      filtrów z „×” i „Wyczyść filtry”, wyróżnienie frazy w wynikach.
      (Pogrubiona liczba wyników i makieta „brak wyników” — zrobione 2026-11-16.)
- [ ] „Tabela / Zaproszenia” (`9258:25269`): czy zmienić opcje „Pokaż na stronie” na 50/75/100
      jak na zrzucie? Status pogrubiony jak na zrzucie — nowy styl czy zostaje Uppercase S?
