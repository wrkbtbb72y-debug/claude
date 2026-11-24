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
  **Potwierdzone 2026-11-24 (użytkownik):** każdy przycisk (także dropdown / „Dymek”, pole Select) na makietach
  ma być **instancją komponentu głównego ze strony „Buttons”** - nie zwykłą ramką, nie odłączoną kopią i nie
  instancją usuniętego lub innego komponentu. Po zmianach w komponentach na „Buttons” (np. gdy zestaw dostanie
  nowe ID) sprawdzić, czy instancje na makietach nadal wskazują na „Buttons”, i w razie potrzeby przepiąć je
  (`swapComponent` + ponowne ustawienie właściwości).
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
- **Kolekcje** (`TaU5NR1T7`, `/kolekcje`) — breakpointy: **Desktop Large** `yL7U5Ca6k` (primary, ≥1440),
  **Desktop Small** `wGZ1SNtqa` (1024–1439), **Tablet** `s9pVODhJU` (768–1023), **Mobile** `LPOTrtJ2n` (<768).
  Układ wg makiet Figmy „4. Zasoby/Kolekcje”, rząd aktualny (`9725:19869`, od 2026-11-22): hero (`nhd7zbaRB`,
  okruszki `MD_Oaspc6`, ramka „text” `WEiUJ9hAP` z tytułem `g84TAGEBn` „Przeglądaj kolekcje” i wyszukiwarką
  „search” `gAvqbQX8m`); wiersz pod hero `C3RRpKDkJ` (przełącznik „Obiekty / Kolekcje” `E0XHTw2QL` + ramka
  informacyjna `wa_CqtzF1` z linkiem „Zarejestruj konto” `muxmYNClL` → `/moje-konto`); „main” `zOmqRBR29`
  (nagłówek „Kolekcje publiczne” = instancja „tytuł sekcji”); „Pasek wyników” `LdQyL8mYK` (licznik, „Sortowanie”
  `LktU3No1N`, „Przełącznik widoku” `xrG4ybpUO` krycie 50 %); siatka CMS „Collections grid” `AIctD0gIv`
  (kolekcja `ieFZEvO29`; 4 / 3 / 2 / 1 kolumny, odstęp 16); „Pagination section”. Zmienna strony „Stan
  Wyszukiwania” (`RzifO176z`): 0 = przed wyszukaniem (start), 1 = po wyszukaniu (blok „Wynik wyszukiwania”
  `gX5UFBu0f` i tytuł „Pozostałe”).
- Presety tekstu są responsywne (sloty `medium` ≥1024, `small` ≥768): np. „Nazwy sekcji”
  `onFkvs54B` 28→26 px, „Body 1 - tekst długi L” `qho9AhWr_` 20→18 px na tablecie.

## Stałe zasady projektowe (Figma)

- **Stan Disabled / nieaktywny przycisku = krycie 50 %** całego elementu (bez zmiany kolorów).
  Dotyczy wszystkich przycisków, także przełączników (np. „Przełącznik widoku” Kafelki / Lista).
  Zmiana z 40 % na 50 % — decyzja użytkownika 2026-11-22 (wcześniej 40 %, potwierdzone 2026-11-17 i 2026-11-20).

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
  (56 px od hero). **Potem użytkownik poprawił odstępy na DL** (ręcznie): przełącznik → nagłówek
  „Wyniki wyszukiwania” 80 → **100**; wyniki + podpowiedzi w nowej ramce `9439:26003` z odstępem
  **120** (paginacja → podpowiedzi); między grupami „Czy chodziło Ci o?” / „Możesz obejrzeć także”
  28 → **60**; etykieta → przyciski 8 → **12**.
  **Te same zmiany przeniesione na pozostałe breakpointy wyników** (prośba użytkownika, ten sam dzień):
  Desktop Small `9173:12149`, Tablet `9173:15859`, Mobile `9173:16891` — przełącznik zostaje u góry,
  podpowiedzi pod paginacją, w nowych ramkach **„Wyniki i podpowiedzi”** (DS `9483:10884`, Tablet
  `9483:10885`, Mobile `9483:10886`), odstępy 100 / 120 / 60 / 12 jak na DL (na Mobile też — bez
  skalowania). **Mobile:** ramka makiety miała stałą wysokość 5010 px i ucinała treść (część kart,
  paginację, stopkę) — ustawiona na „Hug”, teraz ok. 8297 px; nic pod nią nie nachodzi.
  Uwaga: rząd wyników to teraz DL `9439:24776` + DS/Tablet/Mobile jak wyżej (x 11158–15272,
  y −56855); druga makieta „Desktop Large – wyniki wyszukiwania” `9299:43811` (x 16382, y −53287,
  pod etykietą „aktualne”) i makiety „brak wyników” — bez zmian.

- 2026-11-20 — **Figma: hover linków „Członek jednostki”** (prośba użytkownika) — strona
  „tabele - robocze”, makieta „Zmiana hasła - 1441” `9258:25170`, tabela „Tabela / Zaproszenia”
  `9258:25269`. Pięć linków z imieniem i strzałką (dotąd luźne ramki „See_more_button”) zamienione
  na kopie nowego zestawu wariantów **„Link z ikoną”** `9520:2026` (leży pod makietą, x 1640, y 120):
  właściwości **Stan** = Domyślny `9520:2021` / Hover `9520:2022` (**podkreślenie tekstu**, kolor bez
  zmian — jak „Czytaj więcej” / „Zobacz wszystkie” na BUTTONS) + tekst **Tekst**. Wariant Domyślny ma
  interakcję prototypu **While hovering → Change to Hover** (Dissolve 150 ms), więc w trybie
  prezentacji linki podkreślają się po najechaniu. Nowe ID kopii w tabeli: `9520:2030`, `9520:2035`,
  `9520:2040`, `9520:2045`, `9520:2050` (warstwa „Link” w ramkach „akcje”). Wygląd tabeli bez zmian.
  Zestaw nie został przeniesiony na stronę BUTTONS — do decyzji.
  **Kursor „łapka”** (prośba użytkownika, ten sam dzień): Figma pokazuje łapkę w prezentacji tylko
  nad elementami z interakcją kliknięcia, więc **oba warianty** dostały **On click → Navigate to
  „Zmiana hasła - 1441”** (ta sama makieta, bez animacji, z zachowaniem przewinięcia — kliknięcie
  praktycznie nic nie robi). Docelowa akcja kliknięcia (profil członka?) — do ustalenia; użyty na
  innej makiecie komponent przeniesie do tej. W kodzie: `cursor: pointer` + podkreślenie na `:hover`.
  **Ciemniejszy kolor w hoverze** (prośba użytkownika, ten sam dzień): w wariancie Hover tekst
  i strzałka #2350BF → najpierw #142C69 (Blue hover z palety) — użytkownik: „trochę za ciemne” →
  **#1C3E94** (środek między #2350BF a #142C69, bez stylu w pliku). Uwaga: kolor domyślny tych
  linków (#2350BF) nie jest systemowym kolorem linku #193680 — do decyzji, czy ujednolicić.

- 2026-11-20 — **Figma: podpowiedzi wyszukiwania na dole — pozostałe makiety strony „3. Zasoby/Obiekty”**
  (prośba użytkownika, wzór: rząd wyników `9439:24776` + DS/Tablet/Mobile z 2026-11-19). Zmienione
  makiety: druga **„Desktop Large – wyniki wyszukiwania” `9299:43811`** (2 obiekty) i cały rząd
  **„brak wyników”**: DL `9015:7886`, DS `9173:18307`, Tablet `9173:19085`, Mobile `9173:19850`.
  W każdej: przełącznik Obiekty / Kolekcje zostaje u góry (blok „Przełącznik + podpowiedzi”, nazwa bez
  zmian), odstęp przełącznik → „Wyniki wyszukiwania” 80 → **100**; „Podpowiedzi wyszukiwania” przeniesione
  do nowej ramki pod treścią: **„Wyniki i podpowiedzi”** `9539:10884` (w `9299:43811`, odstęp 120) oraz
  **„Brak wyników i podpowiedzi”** — DL `9539:10885`, DS `9539:10886` (odstęp 120), Tablet `9539:10887`,
  Mobile `9539:10888` (odstęp 100, jak we wzorcu na tych breakpointach). Podpowiedzi: padding 0, odstęp
  między grupami 40, etykieta → przyciski 12 (jak we wzorcu). Sekcja: odstęp 80 (było 120 w „brak
  wyników”), dolny padding **60** (było 140/140/120/100); blok „Brak wyników” — dolny padding 60 → 0
  (odstęp do podpowiedzi daje ramka). Makiety „brak wyników” są ok. 100 px niższe, `9299:43811` o 12 px
  wyższa — nic nie nachodzi. Uwaga (bez zmian, było wcześniej): w `9299:43811` przełącznik „Obiekty (2) /
  Kolekcje (0)” łamie liczby do drugiej linii.
  **„Pasek wyników” także w „brak wyników”** (prośba użytkownika, ten sam dzień; wzór `9439:25153`):
  kopia paska danego breakpointu (licznik + Sortowanie „Trafność” + Przełącznik widoku; na Mobile układ
  pionowy jak w wynikach) z licznikiem **„Znaleziono 0 obiektów”** (pogrubione „0”). Pasek i blok „Brak
  wyników” w nowej ramce **„Pasek wyników + brak wyników”** (odstęp **80**) na początku ramki „Brak
  wyników i podpowiedzi”: DL `9539:10889` (pasek `9539:10890`), DS `9539:10895` (`9539:10896`), Tablet
  `9539:10901` (`9539:10902`), Mobile `9539:10907` (`9539:10908`). Makiety wyższe o 25 px (Mobile 81 px),
  nic nie nachodzi. Odstęp 80 między paskiem a komunikatem — moja propozycja, do akceptacji.
  **Poprawka (ten sam dzień):** użytkownik zgłosił ucięte od dołu przyciski podpowiedzi w „brak wyników”.
  W 5 zmienionych makietach (`9299:44084`, `9015:8171`, `9173:19063`, `9173:19828`, `9173:20584`
  i ich grupy „Czy chodziło Ci o?” / „Możesz obejrzeć także”) wyłączone przycinanie treści
  i wymuszone ponowne „Hug” wysokości — grupy miały clip, a po zmianie odstępu 8 → 12 przez API
  wysokość u użytkownika się nie przeliczyła (API pokazywało 71 px).

- 2026-11-20 — **Figma: cień na hover kafelka „Object tile”** (prośba użytkownika, wzór: zrzut obecnego
  serwisu — karta z miękkim cieniem). Komponent `8669:3701` (strona „3. Zasoby/Obiekty - OLD”, x 23062 /
  y 17681) zamieniony w **zestaw wariantów „Object tile” `9545:8118`** z właściwością **Stan**:
  **Domyślny** `8669:3701` (bez zmian; to ten sam węzeł, więc wszystkie 122 kopie zostały podpięte
  z nadpisaniami tekstów i zdjęć) i **Hover** `9545:8119` — styl efektu **„hover-shadow”** z pliku
  (cień 0/0, rozmycie 12, rozszerzenie 7, czarny 10 %; ramka 1 px #E5E5E5 zostaje). Wariant Domyślny
  ma interakcję **While hovering → Change to Hover** (Dissolve 150 ms), jak „Link z ikoną”. Opis
  komponentu przeniesiony na zestaw i uzupełniony o stany. Właściwości tekstowe „Nazwa obiektu”
  i „Autor” zostały (nowe sufiksy ID). Kursor „łapka” w prezentacji wymagałby interakcji kliknięcia
  (docelowo: strona obiektu) — nie dodano, do decyzji.

- 2026-11-20 — **Figma: „Pasek wyników” nad listą kolekcji** (prośba użytkownika) — strona „4. Zasoby/
  Kolekcje” (`6335:42234`), makieta **Desktop Large `9199:29821`** (w ramce `9602:42101`, rząd „aktualne”:
  DL / DS `9199:30131` / Tablet `9199:30429` / Mobile `9199:30727`). Kopia paska `9536:33793` z „Desktop
  Large - Cards” tej strony (licznik + Sortowanie „Alfabetycznie (A–Z)” + Przełącznik widoku Kafelki /
  Lista) wstawiona nad siatkę: nowa ramka **„Pasek wyników + lista kolekcji”** `9612:18417` (odstęp 16 jak
  w Cards) w „Section / Kolekcje publiczne” `9199:30099`, w niej pasek `9612:18418` i dotychczasowa lista
  `9199:30102`. Licznik: **„12 kolekcji”** (12 kafelków, paginacja „1 z 1”; bez pogrubienia jak w Cards).
  Makieta wyższa o 64 px, nic nie nachodzi. **Pozostałe 3 breakpointy** (prośba użytkownika, ten sam
  dzień): to samo z kopią paska danego breakpointu z Cards tej strony (DS `9536:34186`, Tablet
  `9536:34579`, Mobile `9536:34972` — na Mobile układ pionowy: licznik nad sortowaniem i przełącznikiem
  widoku). Nowe ramki „Pasek wyników + lista kolekcji” (odstęp 16): DS `9617:18432` (pasek `9617:18433`),
  Tablet `9617:18438` (`9617:18439`), Mobile `9617:18444` (`9617:18445`); licznik „12 kolekcji” (na
  każdej 12 kafelków). Makiety wyższe o 64 px (Mobile 101 px), nic nie nachodzi. Te 3 breakpointy nadal
  nie mają przełącznika Obiekty / Kolekcje (jest tylko na DL). Prośba o dodanie go na DS / Tablet /
  Mobile — przerwana, potem wznowiona i **zrobiona** (wpis niżej).
  **Przełącznik Obiekty / Kolekcje na DS / Tablet / Mobile** (prośba użytkownika, ten sam dzień; wzór:
  DL `9536:33427`, który użytkownik przełączył na **Aktywny = Kolekcje**, i Cards tej strony): w „Section /
  Kolekcje publiczne” nowa ramka **„Przełącznik + nagłówek”** (odstęp **100**, jak w Cards) — instancja
  wariantu **Aktywny = Kolekcje** (`8967:7100`, 150×33, teksty „Obiekty” / „Kolekcje”) nad dotychczasową
  ramką z nagłówkiem. DS `9629:18475` (przełącznik `9629:18476`), Tablet `9629:18482` (`9629:18483`),
  Mobile `9629:18489` (`9629:18490`). Górny padding sekcji 120 / 100 / 80 → **24** (jak w Cards; na DL
  16 + 8 przesunięcia przełącznika = 24). Makiety wyższe o 37 / 57 / 77 px, nic nie nachodzi. Ramka
  informacyjna „Zarejestruj konto i twórz własne kolekcje” (na DL po prawej obok przełącznika) — **nie
  dodana** na pozostałych breakpointach (nie było prośby).
  **Zastąpione tego samego dnia** (prośba użytkownika: „ten design i ta struktura warstw”, wzór DL
  `9536:38176`): moje ramki „Przełącznik + nagłówek” (i w nich przełączniki `9629:…`) usunięte, w ich
  miejsce **kopie ramki DL „Frame 427320023”** (odstęp 100) → „Frame 427320024” (bez auto layoutu:
  przełącznik Aktywny = Kolekcje + ramka „main” z „Zarejestruj konto ↗ i twórz własne kolekcje.”) →
  „Frame 427319994” z **nagłówkiem sekcji danego breakpointu** (przeniesione instancje `9241:13424` /
  `9241:13431` / `9241:13438`; stare ramki „Frame 427319977” usunięte). Górny padding sekcji **16**
  (jak DL). DS `9631:18490` (wiersz `9631:18491`, „main” `9631:18493` przy prawej krawędzi, x 589,
  ograniczenie poziome Right), Tablet `9631:18515` (`9631:18516`, „main” `9631:18518`, x 415, Right),
  **Mobile** `9631:18540` — przełącznik i ramka obok siebie się nie mieszczą (366 px), więc **ramka
  „main” pod przełącznikiem** (odstęp 16, x 0; wiersz `9631:18541` ma 98 px; ramka ma 363 px — Hug,
  nie pełna szerokość). Makiety: DS 3327, Tablet 4427, Mobile 7243 px; nic nie nachodzi. Uwaga: w ramce
  „main” (też na DL) leży ikona **lucide/x** z pozycją absolutną x 1400 — poza ramką, niewidoczna
  (makiety przycinają treść); pewnie przycisk zamknięcia do ustawienia — nie ruszano.

- 2026-11-20 — **Figma: „Przełącznik widoku” Kafelki / Lista wygaszony (stan Disabled, krycie 40 %)**
  (prośba użytkownika) — strona „3. Zasoby/Obiekty” (`6885:93257`), wszystkie **13 kopii w makietach**:
  Cards DL `9439:24731` / DS `9044:8807` / Tablet `9044:10977` / Mobile `9044:13121`; wyniki DL
  `9439:25157`, DL (2 obiekty) `9299:44192`, DS `9173:12514`, Tablet `9173:16224`, Mobile `9173:17256`;
  brak wyników DL `9539:10894`, DS `9539:10900`, Tablet `9539:10906`, Mobile `9539:10912`. Krycie
  ustawione na instancjach (komponent bez zmian). Nie ruszano 2 wzorców w ramce dokumentacji „Lista
  obiektów - komponenty” (`8988:8238`, `8988:8247`) ani przełączników na stronie „4. Zasoby/Kolekcje”. Uwaga (bez zmian): przełącznik w DL `9536:33427` ma aktywne
  „Obiekty”, choć to strona Kolekcji.

- 2026-11-22 — **Figma: okruszki na makietach Kolekcji — „Kolekcje” → „Zasoby”** (prośba użytkownika) —
  strona „4. Zasoby/Kolekcje” (`6335:42234`): we wszystkich **16** okruszkach „KRONIK@ / Kolekcje / Kolekcje
  publiczne” drugi element zmieniony na **„Zasoby”** (teraz „KRONIK@ / Zasoby / Kolekcje publiczne”, jak
  „KRONIK@ / Zasoby / Obiekty” w Obiektach). Makiety: „Kolekcje publiczne - kafelki” Desktop 1445 / 1446 /
  1447 / 1448, ramka „Frame 427320025” `9602:42100` (8 starszych makiet, m.in. rząd `8175:…`) i rząd aktualny
  DL `9199:29821` / DS `9199:30131` / Tablet `9199:30429` / Mobile `9199:30727`. Zmieniony tylko tekst
  (styl bez zmian; okruszek węższy o ok. 10 px). Na stronie „3. Zasoby/Obiekty” nie ma już okruszków
  z „Kolekcje”. Uwaga: na DL w hero leży czerwona strzałka-adnotacja wskazująca ten element — nie ruszana.

- 2026-11-22 — **Figma: padding boczny 16 px na makietach Mobile** (prośba użytkownika) — strona
  „3. Zasoby/Obiekty” (`6885:93257`), 3 makiety Mobile: Cards `9044:12750`, wyniki wyszukiwania
  `9173:16891`, brak wyników `9173:19850`. W „Section / Hero” (`9044:12752` / `9173:16893` / `9173:19852`)
  i sekcji treści („Section / Lista obiektów” `9044:13017`, „Section / Wyniki wyszukiwania” `9173:17159`
  / `9173:20118`) padding lewy/prawy **12 → 16** (kolumna treści 366 → **358 px**; nawigacja i stopka
  miały już 16). Skutki:
  - **„Object tile”** (12 na Cards, 12 na wynikach) miały stałe 366 px — teraz stałe **358** (okładka
    358×239, Fill bez zniekształceń). Nie „Fill”: lista „Objects list” to poziomy układ z zawijaniem,
    „Fill” dzieliłby rząd między kafelki.
  - **Filtry** („Filtry / pasek (wariant 3)”, 5 pól) 179 → **175 px**, żeby nadal stały po dwa w rzędzie
    (175 + 8 + 175 = 358); przy 179 łamały się po jednym.
  - Wysokości: Cards 7775 → 7711, wyniki 8217 → 8153, brak wyników bez zmian (2790).
  - Pasek kategorii („Zakładka / …”) nadal celowo wystaje w prawo (przewijany) — bez zmian.
  - Nie ruszano makiet Mobile na innych stronach (np. „4. Zasoby/Kolekcje” `9199:30727` ma nadal 12).

- 2026-11-22 — **Figma: odstępy między kafelkami 16 px** (prośba użytkownika) — strona „3. Zasoby/Obiekty”
  (`6885:93257`), wszystkie **9** list „Objects list” (poziomy układ z zawijaniem): Cards DL `8670:5146` /
  DS `9044:8822` / Tablet `9044:10992` / Mobile `9044:13136`; wyniki DL `9439:25172`, DL (2 obiekty)
  `9299:44207`, DS `9173:12529`, Tablet `9173:16239`, Mobile `9173:17271`. Odstęp poziomy i pionowy
  **12 → 16**. Szerokość „Object tile” (stała, przeliczona tak, by liczba kolumn została ta sama):
  DL 4 kol. 321 → **318**, DS 3 kol. 309 → **306,666** (952 nie dzieli się równo), Tablet 2 kol.
  383 → **381**, Mobile 1 kol. **358** (bez zmian). Okładki trzymają proporcje 3:2 (318×212, 306,67×204,44,
  381×254, 358×238,67). Wysokość kafelków Hug. Makiety nie nachodzą na sąsiednie. Nie ruszano: kopii
  zapasowej (odłączone karty) ani list kolekcji na stronie „4. Zasoby/Kolekcje” (tam nadal 12).

- 2026-11-22 — **Figma: odstępy między kafelkami 16 px — także w Kolekcjach** (prośba użytkownika) — strona
  „4. Zasoby/Kolekcje” (`6335:42234`), wszystkie **20** list (12 → **16** w poziomie i pionie):
  - **15 list „Collection tile”**: rząd aktualny DL `9199:30116` (4 kol., 321 → **318**), DS `9199:30414`
    (3 kol., 309,33 → **306,666**), Tablet `9199:30712` (2 kol., 383 → **381**), Mobile `9199:31015`
    (pionowa lista, kafelki Fill 366 — tylko odstęp); stary rząd `8175:4930` / `8175:8483` / `8175:9591` /
    `8175:10446`; „Kolekcje publiczne - kafelki” 1444 `6335:42571`, 1446 `9228:100615`, 1024 `6335:43060`,
    Tablet 810 `6335:43439`, Mobile 390 `6335:43672`; ramki „Frame 427319993” `9228:101444` i `9317:45404`
    (2 kafelki). Listy 3-kolumnowe na 1320: 432 → **429,333**.
  - **5 list „Object tile”** (kopie makiet Obiektów na tej stronie): wyniki DL `9199:34562`, Cards DL
    `9536:33812` (318), DS `9536:34205` (306,666), Tablet `9536:34598` (381), Mobile `9536:34991` (366,
    tylko odstęp — kolumna na tej stronie nadal 366, padding Mobile tu 12).
  - Liczba kolumn bez zmian, okładki bez zniekształceń, kafelki Hug w pionie; 20 makiet nie nachodzi na siebie.

- 2026-11-22 — **Figma: „Przełącznik widoku” krycie 40 % na stronie „4. Zasoby/Kolekcje”** (`6335:42234`;
  prośba użytkownika; to samo co 2026-11-20 na Obiektach). Na stronie jest **14** instancji; 6 miało już
  40 % (m.in. nowe makiety użytkownika „Kolekcje publiczne - kafelki - Desktop 1449” `9657:63377`, DS
  `9657:64762`, Tablet `9657:65068`, Mobile `9657:65374`, „Desktop Large – wyniki wyszukiwania” `9657:58553`),
  pozostałe **8** ustawione na 40 %: Desktop 1447 `9317:45390`, rząd aktualny DL `9612:18422` / DS
  `9617:18437` / Tablet `9617:18443` / Mobile `9617:18449`, oraz DS `9657:55650`, Tablet `9657:55956`,
  Mobile `9657:56016`. Krycie na instancjach, komponent bez zmian. Kopie makiet Obiektów (`9536:…`) nie
  leżą już na tej stronie (usunięte przez użytkownika).

- 2026-11-22 — **Framer: strona „Kolekcje” (`TaU5NR1T7`) zaktualizowana wg makiet Figmy** (prośba użytkownika;
  wzór: rząd aktualny na „4. Zasoby/Kolekcje”, ramka `9725:19869`, 4 breakpointy). Zmiany od razu w `main`
  (bez brancha), **strona nieopublikowana**. Co zmieniono:
  - Okruszki „KRONIK@ / **Zasoby** / Kolekcje publiczne” (Tablet i Mobile miały własną kopię tekstu —
    poprawione osobno). Tytuł hero **„Przeglądaj kolekcje”**, opis pod tytułem ukryty.
  - **Wyszukiwarka przeniesiona do hero** pod tytuł (odstęp 24): szerokość 652 / 629 / 584 px / pełna
    (Mobile, wys. 52), placeholder „Wyszukaj w kolekcjach” (#656766), pole „Sortuj według” 203 px, przycisk
    lupy 50 px (Mobile 46, samo „v” bez napisu). Stara siatka „wyszukiwarka + wypełniacz” `SbLNRBp1Y` ukryta.
  - **Pod hero** (wiersz `C3RRpKDkJ`, góra 12): nowy **przełącznik „Obiekty / Kolekcje”** (zwykłe ramki,
    nie komponent: zakładki 69×32, aktywna „Kolekcje” z kreską 3 px #1A1A1A, linia bazowa 1 px #999; presety
    „Button Thin” / „Button Active”; „Obiekty” **bez linku** — brak strony Obiektów we Framerze) + **ramka
    informacyjna** po prawej (Hug, padding 12/16, tło białe 80 %, ramka #E5E5E5, bez zaokrągleń, przycisk „×”
    ukryty jak w makiecie). Komponent „In-body link z strzałką v2” (tekst „Zaloguj się lub zarejestruj”, użyty
    też na „Przyciski – przegląd”) **nie zmieniany** — w ramce ukryty, a w jego miejsce lokalny link
    **„Zarejestruj konto” ↗** (ten sam cel `/moje-konto`). Mobile: przełącznik nad ramką (odstęp 16), ramka
    z paddingiem 12, by tekst zmieścił się w jednej linii.
  - **Pasek wyników** nad siatką (odstęp 16): „12 kolekcji” (statyczny tekst), „Sortowanie” 48 px (ikony Lucide
    Arrow Up Down / Chevron Down, „Alfabetycznie (A–Z)” preset „Body 4 Bold” #1A1A1A), „Przełącznik widoku”
    Kafelki / Lista krycie 40 %. Mobile: przełącznik (same ikony, 40×40) nad sortowaniem, licznik po lewej na dole.
  - **Siatka kolekcji**: Desktop Large **4 kolumny** (było 3), odstępy **16** na wszystkich breakpointach.
  - Odstępy: hero→wiersz 12, wiersz→„Kolekcje publiczne” 100, nagłówek→pasek wyników 80 (Mobile 60),
    lista→stopka 140 / 140 / 120 / 100.
  - **Stan startowy = przed wyszukaniem** (zmienna „Stan Wyszukiwania” 1 → **0**); blok „Wynik wyszukiwania”
    i tytuł „Pozostałe” widoczne tylko przy stanie 1 (wcześniej blok był widoczny zawsze, a „Pozostałe”
    przy stanie 0). Przełączniki stanu leżą w ukrytym „Search row” — prototyp wyszukiwania na widocznej
    stronie nic nie przełącza.
  - Diagnostyki, które **były wcześniej** i nie są ruszane: akcje „Set Variable” w ukrytym „Search row”
    odwołują się do usuniętej zmiennej `RAB75BF1M`; „tytuł sekcji” na Tablecie i Mobile ma wariant „1440”
    (linter sugeruje Tablet / Phone); nakładanie się ramek na canvasie.

- 2026-11-22 — **Przyciski nieaktywne: krycie 40 % → 50 %** w Figmie i we Framerze (prośba użytkownika; zasada
  w „Stałe zasady projektowe” zaktualizowana). Przeszukane wszystkie bieżące strony Figmy (bez stron ❌ i spod
  „NIEAKTUALNE”, bez stron ikon / grafik / e-maili). Zmienione **50** elementów w Figmie:
  - „Buttons” (`5360:39838`): „Button – disabled” ×4, „para” (Anuluj / Zapisz), przykłady w „Specyfikacja
    przycisków” (Edytuj, Dodaj obiekt, Rozmiar czcionki), wzorzec „Przycisk Dodaj do kolekcji” Styl=W ramce,
    Stan=Nieaktywny (`8981:8170`);
  - „linki i tertiary” (`9258:24783`): Usuń / Publikuj / Ukryj (3);
  - „3. Zasoby/Obiekty”: 13 × „Przełącznik widoku” + instancja „Dodaj do kolekcji” w ramce komponentów
    (`8988:8273`, krycie przejęła ze wzorca);
  - „4. Zasoby/Kolekcje”: 12 × „Przełącznik widoku”;
  - „9. Zarządzanie obiektami” (`5239:35351`): Usuń / Publikuj / Ukryj ×4 (12).
  Pominięte: ramka „OLD MOBILE” (`1132:8612`, „7. Moje konto”) — to nie przycisk. Framer: „Przełącznik widoku”
  na stronie „Kolekcje” (`xrG4ybpUO`, wszystkie breakpointy) — jedyny element z kryciem 40 % w projekcie.

- 2026-11-23 — **Figma: propozycje podziału dropdownów w pasku „Subnav”** (prośba użytkownika) — strona
  „NAWIGACJA II” (`6785:11870`), pasek `9767:25074` w „Navi II - Desktop Large” (`9767:24513`; „Edycja treści”,
  „Zarządzanie”, „Pozyskiwanie zasobów”, „Moja instytucja”). **Oryginał bez zmian.** Pod nim ramka
  **„Pasek – propozycje podziału dropdownów (do wyboru)”** `9779:5969` (x −1383, y −10400) z kopiami paska
  (zwykłe ramki): **0** obecnie · **A** pionowe kreski 1×20 px (#1A1A1A 20 %, odstęp 20) · **B** osobne
  ramki Secondary (biel, ramka #1A1A1A 80 %, 46 px, padding 16, odstęp 8) · **C** osobne jasne ramki
  (biel, ramka #E5E5E5, jak pole „Wybierz jednostkę”) · **D** jedna biała grupa #E5E5E5 z przegródkami
  na pełną wysokość (segmenty, jak „Przełącznik widoku”) · **E** ikony Lucide 18 px przed nazwami
  (file-pen-line, settings, folder-input, building-2), odstęp 36. Czeka na wybór użytkownika.
  Użytkownik sam wprowadził wariant **E (ikony)** w pasku — teraz to **Subnav `9767:33573`** (Container `9767:33574`).

- 2026-11-23 — **Figma: „Subnav” — dopracowanie odstępów i stylu** (prośba użytkownika: „spacing niedopracowany”).
  Oryginał `9767:33573` **bez zmian**; na lewo od „Navi II - Desktop Large” ramka **„Subnav — dopracowanie odstępów
  (przed / po)”** `9789:6055` (x −3023, y −10904): „Przed” = kopia obecnego, „Po” = kopia dopracowana `9789:6103`.
  W „Po”: pasek 72 px (padding 12 + kontrolki 48, jak „Sortowanie” / „Przełącznik widoku”); pole „Wybierz jednostkę”
  260 × 48, padding 0/16 wyśrodkowany, biel 100 %, ramka #E5E5E5 100 %, placeholder styl **Button Thin** #656766;
  pozycje — styl **Button**, ikona–tekst 8, tekst–strzałka 4, **między pozycjami 40** (było 28), ikony i strzałki
  #1A1A1A, wszystko wyśrodkowane w pionie (bez paddingu 2 px w „Chevron wrap”), pole klikalne pozycji na pełną
  wysokość 48 (niewidoczne). Prawa krawędź równa z „Anna Sobczak”. Czeka na akceptację.

- 2026-11-23 — **Figma: menu konta „Anna Sobczak” — stan otwarty** (prośba użytkownika) — strona „NAWIGACJA II”,
  instancja **„Navi Kronika”** `9767:33430` (x −1343, y −11662). W tej instancji (override, komponent bez zmian)
  przycisk „Anna Sobczak” (`I9767:33430;7724:24882`) dostał stan otwarty: tło biel + #1A1A1A 6 % (zasada hover
  secondary), strzałka podmieniona na **lucide/chevron-up**. Pod przyciskiem (4 px niżej, wyrównana do jego prawej
  krawędzi) ramka **„Menu konta – rozwinięte (Anna Sobczak)”** `9796:7538` (na stronie, nie w instancji) — styl jak
  „Dymek” z wzorców dropdownów (`9767:33921`): 260 px, biel, ramka #E5E5E5, zaokrąglenie 4, cień 0/0/3 czarny 20 %,
  pozycje 38 px (padding 11/8/12/12, styl **Button**), separatory #E5E5E5 (padding 4/6) na pełną szerokość.
  Kolejność (zmieniona względem listy użytkownika — „Wyloguj się” na końcu, jak zwykle w menu konta):
  Moje konto · Moje zgłoszenia · Moje kolekcje · Moje adnotacje | Rejestracja instytucji | Wyloguj się.
  **Poprawka tego samego dnia** (użytkownik: „odrobinę ściśnięte w pionie”): pozycje 38 → **44 px** (padding
  14/15 zamiast 11/12, cel kliknięcia ≥ 44), separatory padding 4/6 → **8/8**; lista ma teraz 316 px wysokości.
  Uwaga: wzorcowe „Dymki” (`9767:33921`) nadal mają 38 px — do ujednolicenia, jeśli 44 zostaje.
  **Druga poprawka** (użytkownik: 44 „za bardzo, coś pomiędzy”): pozycje **40 px** (padding 12/13), separatory
  **6/6**; lista 284 px. Aktualne wartości = te.
  **Treść (prośba użytkownika):** pierwsza grupa ma nagłówek kategorii **„Moje konto”** (14/500 #656766, bez stylu
  tekstu — jak etykiety grup w „Dymku” mobilnym; ramka „Label Moje konto” `9799:6066`, padding 8/8/4/12), pod nim
  **Ustawienia konta · Zgłoszenia · Kolekcje · Adnotacje**; dalej Rejestracja instytucji | **Wyloguj się na czerwono
  #9A1C31** (Kronika Red). Lista 310 px. Na stronie leży też kopia użytkownika `9767:33963` (stara treść) — nie ruszana.
  **Wersja aktualna = kopia użytkownika `9767:33983`** w „Navi II - Desktop Large” (`9767:24513`), z jego poprawkami
  (kreska pod „Moje konto”, inne paddingi). Na jego prośbę **dwie dolne kreski jak ta pod „Moje konto”**: wcięte
  15 px z obu stron (szer. 228, #E5E5E5) — padding L/P 15 w „Separator” `9767:33995` i `9767:34000`. Moja wersja
  `9796:7538` (przy instancji `9767:33430`) jest starsza i nie ma tych zmian.
  **Nagłówek kategorii „Moje konto” (`9767:33986`) → styl „Uppercase S”** (13/450, wersaliki, tracking 2 %), kolor
  #656766 (prośba użytkownika: ma wyglądać jak nazwa kategorii, nie link). Uwaga: górna nawigacja też ma wersaliki
  (14/450, czarne, klikalne) — od linków odróżnia go mniejszy rozmiar i szary kolor.
  **Kreska pod „Ustawienia konta”** (prośba użytkownika): „Separator” `9805:6066` (kopia dolnego separatora, padding
  6/6, kreska 228 px #E5E5E5 w tym samym miejscu co pozostałe). Lista 342 px. Użytkownik sam dodał kreskę nad
  „MOJE KONTO” (`9767:34014`) — nie ruszana.
  **Porządki w warstwach (prośba użytkownika; treść i układ wg jego wersji — bez nagłówka „MOJE KONTO”, pozycje
  „Moje zgłoszenia / kolekcje / adnotacje”):** jednolity auto‑layout: ramka menu (V, padding 12/8/12/8, gap 0) →
  „Grupa – Konto” / „Grupa – Moje zasoby” / „Grupa – Instytucja” / „Grupa – Wylogowanie” (V, bez paddingu) →
  „Pozycja – <nazwa>” (H, padding 10/8/10/12, wys. 35, bez tła) → tekst (styl Button). Między grupami „Separator”
  (V, padding 2/7/2/7, kreska 228 × 1 #E5E5E5, x 16). Usunięte zbędne ramki („Moje”, „Frame 427320025”,
  „Instytucja”, „Wyloguj”) i białe tła wewnętrznych ramek. **Odstęp tekst–kreska i kreska–tekst = 12 px przy
  każdej kresce** (wcześniej przy ostatniej 12/14); margines góra/dół menu do tekstu 23/23. Menu 260 × 251.

- 2026-11-23 — **Figma: menu boczne Mobile — gdzie dać linki konta** (prośba użytkownika: Moje zgłoszenia, Moje
  kolekcje, Moje adnotacje, Rejestracja instytucji; „Ustawienia konta” = obecny czarny przycisk „Moje konto”).
  Strona „NAWIGACJA II”, ramka **„Menu boczne Mobile — gdzie dać linki konta (propozycje)”** `9816:6120`
  (x −1343, y −8700, pod ramką z makietami Tablet/Mobile `9767:36131`). Kopie „Mobile - zalogowany” (`9767:35466`,
  oryginał bez zmian; w kopiach „Drawer Mobile (zwinięte)” przestawiony z Absolute do układu, ramki wysokie na
  treść, czerwona linia = dół ekranu 844): **Teraz** `9816:6129` · **A** lista „MOJE ZASOBY” (Uppercase S #656766)
  pod przyciskami konta, wiersze jak pod‑lista „O nas” `9816:6201` · **B** rozwijana pozycja „MOJE ZASOBY” jako
  pierwsza w nawigacji (kopia akordeonu „O nas”, stan rozwinięty) `9816:6353` · **C** imię i nazwisko ze strzałką
  rozwija to samo menu co desktop (Ustawienia konta | Moje… ×3 | Rejestracja | Wyloguj się czerwony), przyciski konta
  ukryte, stan rozwinięty `9816:6509`. Rekomendacja Claude: C (spójne z desktopem, zwinięte najkrótsze), alternatywa B.
  Czeka na wybór; potem Tablet (drawer 580).

- 2026-11-23 — **Figma: rozwinięte sekcje paska „Subnav”** (prośba użytkownika, lista pozycji od niego). Wzór:
  „Navi II - Desktop Large” `9767:37402` (x −3501, y −10945; z „Subnav — dopracowany”) — **bez zmian**. Pod nim
  (odstęp 80) **4 kopie 1440 × 700**, w każdej jedna sekcja otwarta (strzałka w górę, lista 4 px pod polem klikalnym,
  kolumna tekstu wyrównana do ikony; ostatnia dosunięta do prawej krawędzi treści 1380):
  „… — Edycja treści (rozwinięte)” `9830:7044` · „… — Zarządzanie” `9830:7444` · „… — Pozyskiwanie zasobów” `9830:7839`
  · „… — Moja instytucja” `9830:8228`. Listy = styl menu konta: 260 px, padding 12/8, biel, ramka #E5E5E5, r 4, cień
  0/0/3 20 %, pozycje 35 px (10/8/10/12, styl Button), separator 2/7/2/7. Pozycje:
  Edycja treści — O portalu, Aktualności, Pomoc, Instytucje, Kontakt | Regulamin, Polityka prywatności i RODO
  (nazwa robocza), Deklaracja dostępności; Zarządzanie — Użytkownicy, Zgłoszenia, Instytucje, Wnioski o rejestrację,
  Słowniki, Kolekcje, Statystyki; Pozyskiwanie zasobów — Obiekty cyfrowe, Źródła danych, Lista migracji, Manager
  plików; Moja instytucja — Dane instytucji, Obiekty instytucji, Migracje, Użytkownicy. Uwagi z listy (do dopytania
  MC, dubel „Instytucje”, znaczenie „Użytkownicy”) jako żółte notatki obok list. Menu konta użytkownika `9767:33983`
  już nie istnieje na stronie — listy zbudowane od zera według jego wymiarów.

- 2026-11-23 — **Figma: drugi pasek „Subnav” — instytucja partnerska** (prośba użytkownika: „drugi pasek dla innego
  usera”). Kopia wzoru `9767:37402` pod czterema makietami rozwiniętych sekcji: **„Navi II - Desktop Large — instytucja
  partnerska — Zarządzanie (rozwinięte)”** `9835:9490` (x −3501, y −7288, 1440 × 457). Sekcje z ikonami Lucide 18 px:
  **Obiekty instytucji** (lucide/images) i **Migracje** (lucide/arrow-right-left) — zwykłe linki, bez strzałki;
  **Zarządzanie** (settings) — jedyny dropdown, pokazany rozwinięty: Dane instytucji, Użytkownicy (lista `9835:9871`,
  ten sam styl co pozostałe, dosunięta do prawej krawędzi 1380). Żółta notatka: wg notatki „DLA PARTNERSKICH” na
  stronie „Zarządzanie” tylko dla administratorów lokalnych; ikony do akceptacji.

- 2026-11-23 — **Figma: stan aktywny (otwarty) pozycji „Subnav”** wg wzoru użytkownika „Makieta” `9767:39134`
  (stary przycisk „Zarządzanie”): tło **#E6E6E6**, ramka **1 px #D4D4D4** (inside), wysokość **34**, 12 px poza
  treść pozycji z każdej strony, bez zaokrągleń. Dodane we **wszystkich 5** makietach rozwiniętych sekcji
  (`9830:7044`, `9830:7444`, `9830:7839`, `9830:8228`, `9835:9490`) jako prostokąt „Tło – aktywny” (Absolute, pod
  treścią pozycji — układ paska bez zmian). Lista przesunięta **4 px pod ramkę** i wyrównana do jej lewej krawędzi
  (przy ostatniej pozycji — do prawej). We wdrożeniu: padding 0/12 na każdej pozycji, tło tylko w stanie otwartym.
  Poprawka: ramka była **ucinana** (przycinanie treści w „Nav2 links”, „Container” i „Subnav — dopracowany”) —
  w tych 5 makietach „Clip content” wyłączone, ramka widoczna w całości.

- 2026-11-23 - Prośba użytkownika: bez długich myślników „—” w tekstach Claude (zasada w głównym `CLAUDE.md`).
  W Figmie (strona „NAWIGACJA II”) w ramkach od Claude zamienione „—” → „-”: 8 tekstów i 19 nazw warstw
  (ramki `9779:5969`, `9830:7044`, `9830:7444`, `9830:7839`, `9830:8228`, `9835:9490`, `9796:7538`). Ramek
  `9789:6055` (Subnav przed/po) i `9816:6120` (menu boczne Mobile - propozycje) już nie ma na stronie.

- 2026-11-23 - **Figma: „Wzór zachowania paska” (MC) zaktualizowany** (prośba użytkownika) - strona „NAWIGACJA II”,
  ramka `9767:39525` (x 1600, y −8170). Kopia zapasowa starej wersji: **„Wzór zachowania paska - stara wersja (kopia
  zapasowa 2026-11-23)”** `9846:9844` (x 6030, y −8170). Instancje komponentu „Subnav” (`8088:5007`, komponent bez
  zmian) zastąpione kopiami „Subnav - dopracowany” (zwykłe ramki, 72 px, przycinanie wyłączone):
  - **Desktop Large 1440** `9846:9919`: jak wzór - 4 sekcje z ikonami (Edycja treści, Zarządzanie, Pozyskiwanie
    zasobów, Moja instytucja), odstęp 40, pole jednostki 260.
  - **Desktop Small 1024** `9846:9960`: padding 36, pole jednostki **220**, odstęp między sekcjami **24** (całość
    933 z 952 px; przy 260 / 40 by się nie zmieściło).
  - **Tablet 810** `9846:10001`: 4 sekcje się nie mieszczą → pole jednostki 260 + czarny okrągły przycisk „⋮” (jak
    na Mobile) po prawej, padding 24.
  - **Mobile 390** `9846:10047`: pole jednostki na całą szerokość (Fill) + przycisk „⋮”, odstęp 12, padding 16.
  - **Mobile - menu rozwinięte** (`7741:9623`): pasek `9846:10093`; stary „Dymek” (Użytkownicy / Zarządzanie / Moje
    zasoby) usunięty, nowy **akordeon „Menu sekcji - rozwinięte”** `9846:11814` (358 px, 4 px pod polem jednostki,
    styl jak listy desktop): 4 nagłówki sekcji z ikoną i strzałką (kopie pozycji paska, padding 10/8/10/12),
    separatory między sekcjami; rozwinięte „Zarządzanie” - pozycje wcięte 38 px (tekst w linii z nazwą sekcji).

- 2026-11-23 - **Figma: menu sekcji na Mobile jako panel boczny** (prośba użytkownika) - makieta „Navi II - Mobile -
  menu rozwinięte” `9767:41642` (x 5440, y −7181). Dymek-akordeon pod paskiem (`9767:41657`) zamieniony na **panel
  boczny z prawej na całą wysokość ekranu**: „Panel boczny - menu sekcji” `9856:10211` (320 × 800, biel, padding
  20/8/16/8, odstęp 24) - u góry przycisk zamknięcia lucide/x 28 px (jak w menu głównym), pod nim „Lista sekcji”
  `9856:10215` (te same sekcje, nagłówki, pozycje i kreski co w dymku; „Zarządzanie” rozwinięte). Pod panelem
  **„Scrim”** (czarny 44 %, jak w menu bocznym na Tablet) na całej makiecie; ramka makiety przycina zawartość.

- 2026-11-24 - **Figma: paddingi list dropdown ujednolicone + komponent „Dymek”** (prośba użytkownika).
  - Strona „NAWIGACJA II”: wzór = „Dropdown – Edycja treści” `9830:7421` (padding listy **8/8/8/8**, pozycje 35 px
    10/8/10/12, separator 4/7/4/7). Pozostałe listy miały padding 12/8 → 8/8: „Dropdown – Zarządzanie” `9830:7821`,
    „Dropdown – Pozyskiwanie zasobów” `9830:8216`, „Dropdown – Moja instytucja” `9830:8605`, „Dropdown – Zarządzanie”
    (instytucja partnerska) `9835:9871`. Lista pola „Wybierz jednostkę” w instancji „Select - 1 Domyślny” `9767:41214`:
    **nadpisania w instancji** (komponent `9767:41209` na stronie Buttons bez zmian) - padding 4 → 8, pozycje
    11/8/12/14 → 10/8/10/12 (pozycja z ikoną check ma 36 px).
  - Strona „Buttons”, tabela „Przyciski – przegląd”, wiersz „Linki rozwijane: Użytkownicy · Zarządzanie · Moje
    zasoby”: stara ramka „Nav - 2 Otwarty” (`8378:124736`) **usunięta**, w jej miejscu **komponent główny „Dymek”**
    `9908:5221` (zestaw wariantów, właściwość **Stan = Domyślny / Hover**: `9908:5199` / `9908:5200`). Budowa jak wzór
    `9830:7421` (treść „Edycji treści”: 2 grupy po 4 pozycje + separator); Hover = tło pozycji „Aktualności” #F6F6F6
    (kolor hover ze starej ramki). Na makietach dropdowny nadal są zwykłymi ramkami - nie podmienione na instancje.

- 2026-11-24 - **Figma: komponent „Przycisk paska Subnav”** (prośba użytkownika) - strona „Buttons”, ten sam wiersz
  tabeli („Linki rozwijane…”): stara ramka „hover zarządzanie” z trzema szarymi przyciskami (`8347:118514`)
  **usunięta**, w jej miejscu zestaw **„Przycisk paska Subnav”** `9915:378` (nad „Dymkiem”). Wzór = pozycje paska
  z ikonami w „Navi II - Desktop Large - Edycja treści (rozwinięte)” (`9830:7050`). Warianty **Stan = Domyślny**
  `9915:363` / **Otwarty** `9915:370`. Budowa: padding 8/12, wys. 34, ikona Lucide 18 px (kreska 1,5) + tekst
  (styl Button), odstęp 8, strzałka **lucide/chevron-down / chevron-up** 16 px (kreska 1,33, #1A1A1A), odstęp 4.
  Otwarty: tło #E6E6E6, ramka 1 px #D4D4D4 inside (nie wlicza się do układu - oba warianty 157 × 34). Właściwości:
  **Etykieta** (tekst), **Ikona** (podmiana instancji), **Strzałka** (wł./wył. - zwykłe linki bez listy, np.
  „Obiekty instytucji”). Przy wstawianiu do paska odstęp między przyciskami **16** zamiast 40 (padding 12 + 12
  jest już w przycisku). Makiety na „NAWIGACJA II” nadal mają zwykłe ramki - nie podmienione.

- 2026-11-24 - **Figma: makiety „NAWIGACJA II” na kopiach komponentów** (prośba użytkownika). Przyciski paska
  (ramki „Nav item / …” / „Pozycja - …”) zastąpione instancjami **„Przycisk paska Subnav”** (`9915:378`, nazwy
  „Przycisk - <etykieta>”, etykieta/ikona/strzałka ustawione właściwościami; otwarta sekcja = wariant Otwarty,
  prostokąty „Tło – aktywny” zniknęły razem ze starymi ramkami) w 8 paskach: „Navi II - Desktop Large” `9767:37402`,
  5 makiet rozwiniętych (`9830:7044`, `9830:7444`, `9830:7839`, `9830:8228`, `9835:9490`) i we „Wzorze zachowania
  paska” Desktop Large `9846:9919` + Desktop Small `9846:9960`. Odstęp w „Nav2 links”: 40 → **16** (Desktop Small
  24 → **0**), bo padding 12 jest w przycisku - odległości między treściami bez zmian. Skutek: cała grupa
  przesunęła się o 12 px w lewo; zamknięta ostatnia sekcja kończy się 12 px przed krawędzią 1380, a tło otwartej
  sekcji sięga do 1380 (równo z „Anna Sobczak”).
  Listy rozwinięte zastąpione instancjami **„Dymek”** (Stan Domyślny; `9926:5436`, `9926:5457`, `9926:5478`,
  `9926:5499`, `9926:5520`, stare nazwy „Dropdown – …”): teksty pozycji nadpisane, zbędne pozycje / druga grupa /
  separator ukryte (Zarządzanie 7 pozycji = grupa 1 + 3 z grupy 2 bez separatora). Listy i żółte notatki
  przesunięte o −12 px (lista 4 px pod przyciskiem, wyrównana do jego lewej krawędzi, przy ostatniej sekcji do prawej).
  Bez zmian: paski Tablet / Mobile (tylko pole jednostki + „⋮”), panel boczny menu sekcji na Mobile, stary
  komponent „Subnav” `8088:5007`, lista pola „Wybierz jednostkę” (osobny komponent Select).

- 2026-11-24 - **Figma: strzałka ostatniej sekcji paska równo z „Anna Sobczak” + ta sama strzałka w menu konta**
  (prośba użytkownika).
  - 8 pasków Subnav (te same co wyżej): padding prawy ramki „Subnav…” 60 → **48** (Desktop Small 36 → **24**), lewy
    bez zmian. Prawa krawędź rysunku strzałki ostatniej sekcji = prawa krawędź ramki „Anna Sobczak” (sprawdzone
    pomiarem; tło otwartej ostatniej sekcji wystaje 16 px poza tę krawędź). Listy „Dymek” i żółte notatki w 5
    makietach rozwiniętych przesunięte o +12 px (dalej 4 px pod przyciskiem, wyrównane jak wcześniej).
  - **Komponent „Navi Kronika”** (`6075:40683`, wariant **Zalogowany** `7724:24804`, strona „- KOMPONENTY - nowe
    (robocze)”): strzałka przy „Anna Sobczak” (`7724:24885`) podmieniona z lokalnej lucide/chevron-down 18 px
    (kreska 2, #222) na **tę samą co w „Przycisk paska Subnav”**: lucide/chevron-down z biblioteki, 16 px, kreska
    1,33, #1A1A1A. Zmiana w komponencie głównym - dotyczy wszystkich 21 kopii (NAWIGACJA I / II / II 2, Lista
    Instytucji, 9. Zarządzanie obiektami, 3. Zasoby/Obiekty - OLD, linki i tertiary); żadna nie miała własnej
    strzałki (sprawdzone). Przycisk węższy o 2 px (156 → 154).

- 2026-11-24 - **Figma: stan Hover w „Przycisk paska Subnav”** (prośba użytkownika: spójny z podobnymi przyciskami
  na „Buttons”). Hovery na „Buttons”: przyciski Secondary/pola (Sortowanie, Podpowiedź wyszukiwania, Wyloguj się)
  = **nakładka #1A1A1A 6 %** na tło, ramka bez zmian; „Dodaj do kolekcji” = to samo w granacie (#193680 6 %); linki
  tekstowe (Czytaj więcej, Zobacz wszystkie, Tabela) = podkreślenie; pozycja „Dymka” = tło #F6F6F6; czarny „Moje
  konto” = #333. Wybrane: **Hover = tło #1A1A1A 6 %, bez ramki** (reszta jak Domyślny). Na pasku #F4F4F4 daje to
  ok. #E7E7E7 - prawie ton stanu Otwarty (#E6E6E6); Otwarty różni się ramką #D4D4D4 i strzałką w górę.
  Zestaw na „Buttons” ma teraz ID **`9891:51708`** (Domyślny `9891:51709`, **Hover `9938:361`**, Otwarty
  `9891:51714`; tło zestawu #F6F6F6, r 5, ikona krycie 80 % - zmiany użytkownika), w ramce `9923:51730` z podpisami
  Domyślny / Hover / Wybrany (podpisy w ramkach 197 px = rozstaw wariantów). Zestaw `9915:378` z poprzedniej wersji
  **nie istnieje** - 31 przycisków na makietach „NAWIGACJA II” wskazuje na usunięty komponent (nie dostaną hovera,
  dopóki nie zostaną przepięte na `9891:51708`).

- 2026-11-24 - **Figma: przyciski paska na makietach przepięte na komponent z „Buttons”** (prośba użytkownika).
  31 instancji „Przycisk - …” na „NAWIGACJA II” (8 pasków) wskazywało na usunięty zestaw `9915:378` - podmienione
  na „Przycisk paska Subnav” `9891:51708` (Domyślny / Otwarty jak wcześniej), etykiety, ikony i strzałki
  przeniesione właściwościami (sprawdzone wszystkie 31). Wygląd bez zmian poza kryciem ikon 80 % (z komponentu).
  Audyt strony: instancje ze strony „Buttons” = Przycisk paska Subnav ×31, Dymek ×5, Select ×1; pozostałe
  instancje to komponenty z „- KOMPONENTY - nowe (robocze)” (Navi Kronika ×7, gov_top_bar ×7, Podwójna nawigacja ×4)
  i ikony Lucide z biblioteki.

- 2026-11-24 - **Figma: komponent „Przycisk Panel” (okrągły „⋮”)** (prośba użytkownika) - strona „Buttons”, wiersz
  tabeli „Przycisk Panel” (`8347:118486`): ramki „Default” / „Open” zastąpione zestawem **„Przycisk Panel”**
  `9945:13664` (w ramce „Przycisk Panel - warianty” `9945:13654` z podpisami): **Stan = Domyślny** `9945:13658`
  (biel, ramka 1 px #E1E1E1, ikona lucide/ellipsis-vertical 22 px #1A1A1A) / **Otwarty** `9945:13661` (tło #0A0A0A,
  ikona biała); 40 × 40, r 20. Tło zestawu #F6F6F6, r 5 (jak „Przycisk paska Subnav”). Kolumna „Podgląd” w tym
  wierszu miała stałe 163 px i ucinała zestaw - teraz „Fill” jak w innych wierszach.
  Makiety „NAWIGACJA II” - 3 przyciski zamienione na instancje: pasek Tablet `9945:13669` i Mobile `9945:13672`
  („Wzór zachowania paska”, Domyślny) oraz „Navi II - Mobile - menu rozwinięte” `9945:13675` (Otwarty; wcześniej
  kropki z elips, teraz ikona Lucide). Stary komponent „Subnav” `8088:5007` ma własny przycisk - bez zmian.
  Na stronie „NAWIGACJA II 2” jest jeszcze 7 takich przycisków jako zwykłe ramki - nie ruszane.

- 2026-11-24 - **Framer: stopka na szerokich ekranach** (prośba użytkownika, Home „Duży desktop”) - komponent
  „Footer desktop” (`C2z0HEoS0`), ramka „Frame 427319873” (`I8xVLP_7s`, w wariancie „Primary Large”, dziedziczą
  pozostałe warianty): maks. szerokość **1800 → 1600 px**. Sekcje strony głównej mają maks. 1720 px i padding 60
  (kolumna treści 1600 px, wyśrodkowana), a stopka ma padding 60 - teraz treść stopki zaczyna się przy tej samej
  lewej krawędzi co treść strony także powyżej 1720 px (sprawdzone: 2200 px → 300 px, 3000 px → 700 px; wcześniej
  przy 2200 px było 200 px). Do 1720 px wygląd bez zmian. Zmiana od razu w `main`, nieopublikowana.

- 2026-11-24 - **Framer: jedna szerokość kolumny treści na szerokich ekranach** (decyzja użytkownika: ujednolicić) -
  zasada: sekcje / ramki z treścią mają **maks. 1720 px + padding 60** (kolumna 1600 px), jak Home, Instytucje,
  Moje konto i stopka. Zmienione 1920 → 1720 px (w głównym breakpoincie, pozostałe dziedziczą):
  „O portalu” (Desktop Large) - „Section / Portal overview” `HxnHSX2vO`, „Section / Safety and archiving” `IoaTRC3uh`,
  „Section / Learn more” `Mm3xRNzW0`, plus treść hero „inside” `MLvQTY5XU` (wcześniej bez limitu); „Kolekcje”
  (Desktop Large) - hero „inside” `TO6NnIH3K`, wiersz pod hero `C3RRpKDkJ`, „main” `zOmqRBR29`. Tła (hero, belki)
  zostają na całą szerokość. Przy 1440 px i węższych wygląd bez zmian (zrzuty sprawdzone). Nie ruszano ukrytego
  „Notice banner” `lNQ_e1F87` w „Kolekcjach” (padding 60, bez limitu). Zmiana od razu w `main`, nieopublikowana.

- 2026-11-24 - **Framer: nawigacja nie skacze na boki przy zmianie tła** (prośba użytkownika, nagranie ekranu) -
  komponent „Navi” (`SWJhT9Gb9`): przy przewijaniu na górę wariant „Desktop Large White BG” (`Mymr8EEp_`) zmienia
  się w „Desktop Large Translucent” (`ZSUKrGPol`) i linki „O NAS … POMOC” + kreska przesuwały się o ok. 80 px.
  Powód: w białym wariancie linki to instancje „Przycisk nav rozwijany” (`Wh6ZYci5u`, padding 12/8/12/12) i ramki
  „… (hover)” (padding 12) z odstępem 4 px, a odstęp przed kreską 79 px; w przezroczystym zwykłe teksty z odstępami
  20/22 px i 52 px. Poprawka **tylko w wariancie Translucent** (biały bez zmian, jego odstępy wynikają z tła hover):
  grupa linków `q2GapG2v8` odstęp 20 → **24**, „navi_links” `EWfMoUp8s` odstęp 22 → **28** + padding prawy **12**,
  „navi-right” `z7DF8rOdH` odstęp 52 → **79**. Teraz teksty i kreska stoją w obu wariantach w tych samych miejscach
  (zrzuty: O NAS 579, ZASOBY 667, INSTYTUCJE 770, POMOC 886, kreska 1031 px przy 1440). Para wariantów 1024
  („Desktop Small Translucent” / „Desktop White BG”) nie miała różnic. Zasada: przy zmianie odstępów w jednym
  wariancie nawigacji poprawić drugi tak, by położenie tekstów się zgadzało. Zmiana od razu w `main`, nieopublikowana.

- 2026-11-24 - **Framer: lista „Wybór instytucji” na Home zamknięta na canvasie** (prośba użytkownika: nie chce
  widzieć rozwiniętej listy w przestrzeni roboczej). Instancja komponentu „Wybór instytucji” (`LR_e0lpcL`, warianty
  „Zamknięty” `zrmunORyP` / „Otwarty” `hV15UgTcR`) w wyszukiwarce hero na Home, breakpoint „Duży desktop”
  (`XjMbofAH4B48TPUa6Q`), miała nadpisany wariant „Otwarty” - na stronie ≥ 1440 px lista byłaby rozwinięta od razu
  po wejściu. Ustawiony „Zamknięty” jak na pozostałych breakpointach. Zasada: instancje list rozwijanych na stronach
  zawsze w wariancie zamkniętym (stan otwarty tylko w komponencie). Na stronie projektowej „Design” (`G3pEUaHiE`,
  ramka „Duzy desktop”) jest jeszcze instancja `GD9OeDtos` w wariancie „Otwarty” - nie ruszana (do decyzji).
  Zmiana od razu w `main`, nieopublikowana.

- 2026-11-24 - **Framer, Home: tekst w „Otwarte zasoby nauki i kultury”** (prośba użytkownika: pogrubiona fraza nie
  może łamać się na dwie linie). Tekst `TrlUpls2C` („Opis portalu”, preset „Body 1 - tekst długi L”) zmieniony z
  „Zapewniamy bezpłatny dostęp do ponad **19 milionów obiektów** cyfrowego dziedzictwa narodowego.” na
  „**Ponad 19 milionów obiektów** cyfrowego dziedzictwa narodowego udostępniamy bezpłatnie.” - pogrubienie na
  początku, więc zawsze w pierwszej linii (wcześniej łamało się po „19” na Desktop 1024 i Mobile). Sprawdzone
  na zrzutach wszystkich 4 breakpointów. Zmiana od razu w `main`, nieopublikowana.

- 2026-11-24 - **Audyt wizualny / typograficzny Home** (wyniki, nic poza tekstem wyżej nie zmieniano):
  wszystkie widoczne teksty na stronie (20) mają preset tekstu, font wszędzie Aspekta; nagłówki sekcji, nawigacja
  i stopka w komponentach. Znalezione niekonsekwencje - lista w „Do zrobienia” (punkt „Audyt Home”).

## Do zrobienia

- [ ] **Audyt Home (2026-11-24) - do decyzji użytkownika:**
      1) placeholder wyszukiwarki `w7UXI65fG`: Mobile „Szukaj w naszych zbiorach”, reszta „Wyszukaj z ponad 19 milionów
      zbiorów”; style różne na każdym breakpoincie (Body 4 Thin / Button Thin na Dużym desktopie / ręczne 15 px 400
      na Tablecie / 15 px 450 na Mobile), kolor #757575 vs #6B6B6B na Dużym desktopie;
      2) Aktualności `FvqGRkPEb`: Duży desktop ma inny tekst („…zasobów. Dołącz do nas i udostępnij swoje unikatowe
      zbiory szerokiemu gronu odbiorców.”) niż pozostałe („…oraz dzielenia się swoim dorobkiem.”);
      3) „Podziel się swoimi zbiorami…” `eEc7OFqIY`: na Tablecie ręczny kolor #333333, na reszcie kolor z presetu;
      4) wielkie litery w nagłówkach: „Dołącz do Nas”, „Instytucje Partnerskie” vs „Otwarte zasoby nauki i kultury”;
      5) stopka: „w godzinach 08:15-16:15” - łącznik zamiast półpauzy i na 1024 / 1440 łamie się po „08:15-”;
      6) cienka linia 1 px rgba(0,0,0,0.1) **pod stopką** („Recommended_h2” `h93FmTSH9`) na wszystkich breakpointach;
      7) ukryte stare kopie sekcji (88 ukrytych tekstów): „Polecane-section” `MoQkF82Y4`, 4× „O Portalu-section”,
      „Footer wrapper” `hHA1xEUSH` - do usunięcia po zgodzie (zaśmiecają linter i canvas);
      8) „Body 1 - tekst długi L” ma grubość 250 + szary kolor - cienki tekst, warto sprawdzić czytelność / kontrast;
      9) etykiety kategorii w źródle różną wielkością liter („tekst”, „Muzealia”, „film”) - na stronie wielkie przez preset.

- [x] Framer: „O portalu” i „Kolekcje” ujednolicone do maks. 1720 px jak Home i stopka (2026-11-24).

- [x] „NAWIGACJA II”: 31 instancji „Przycisk - …” przepięte z usuniętego zestawu `9915:378` na
      „Przycisk paska Subnav” `9891:51708` (2026-11-24).
- [ ] „NAWIGACJA II”: przyciski / pola, które nie są instancjami komponentów z „Buttons”: pola „Wybierz jednostkę”
      w paskach (zwykłe ramki), przycisk „Anna Sobczak” i reszta menu (w komponencie
      „Navi Kronika” na „- KOMPONENTY - nowe (robocze)”), pozycje panelu bocznego na Mobile - do decyzji użytkownika.

- [ ] Menu boczne Mobile/Tablet: wybrać wariant linków konta (A/B/C w ramce `9816:6120`), dopracować go i zrobić
      wersję Tablet.

- [ ] „Subnav” (NAWIGACJA II): akceptacja wersji „Po” (`9789:6103` w ramce `9789:6055`) → przenieść do oryginału
      `9767:33573`, potem pozostałe breakpointy (Desktop Small / Tablet / Mobile).

- [ ] Framer „Kolekcje”: do decyzji — link zakładki „Obiekty” (gdy powstanie strona Obiektów), licznik
      „12 kolekcji” powiązany z CMS zamiast tekstu, wariant „tytuł sekcji” Tablet / Phone na mniejszych
      breakpointach, usunięcie martwych akcji (`RAB75BF1M`) w ukrytym „Search row”, „Pokaż na stronie”
      w paginacji na Mobile (w makiecie go nie ma).

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
