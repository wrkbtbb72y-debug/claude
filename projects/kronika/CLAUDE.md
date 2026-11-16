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
  (1440) to ramka „Desktop Large” `8670:4812` (pozostałe 3 breakpointy jeszcze nie powstały);
  wariant **„Desktop Large – wyniki wyszukiwania”** `8949:9184`; kopia zapasowa sprzed zmian
  2026-11-16: „Lista obiektów - kopia zapasowa” `8911:31206` (karty odłączone od komponentu).
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
  - **Przełącznik Obiekty / Kolekcje** (`8701:4842`) przeniesiony z hero na górę sekcji listy,
    tuż pod hero (padding sekcji u góry 120 → 24 px; 40 px do tytułu „Lista obiektów”).
    Kolory pod jasne tło: aktywny #121212 + kreska 3 px, nieaktywny #6C6C6C; style tekstu
    Button Active / Button Thin. Hero zostaje 380 px — tytuł „Przeglądaj obiekty”
    z wyszukiwarką wyśrodkowany w pionie między okruszkami a dolną krawędzią hero (prośba
    użytkownika). Sekcja listy ma teraz wysokość „Hug” (wcześniej stała 1777 px).
    **Linia bazowa** (prośba użytkownika): pod oboma opcjami cienka linia 1 px #D6D6D6
    („Linia bazowa”, prostokąt absolutny, rozciągany na szerokość przełącznika, pod opcjami);
    gruba kreska aktywnej opcji (3 px #121212, obrys „Inside”) leży na niej, wyrównana do
    dołu. Obie opcje mają stałą wysokość 32 px (padding 4/4), żeby teksty były w jednej linii.
    To samo w ramce wyników wyszukiwania (`8949:9453`).
  - **Karta „Object tile”** (komponent `8669:3701`): marginesy 16 px ze wszystkich stron
    (ikona „Dodaj do kolekcji” 20 px dosunięta do prawej krawędzi przycisku 32 px, więc
    wizualnie też 16 px), rytm pionowy: zdjęcie –16– kategoria –16– tytuł –4– autor –24–
    kreska –16– muzeum –16– dół karty. Style tekstu: tytuł → H4 - Nagłówki (Duży desktop,
    20/500, wcześniej 18/500 bez stylu), autor i muzeum → Table Thin (14/400). Karta urosła
    383 → 397 px. Zmiana w komponencie — dotyczy też ramki „Obiekty - propozycja”;
    kopia zapasowa zamrożona (instancje odłączone).
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
  - We Framerze nic nie zmieniano.

## Do zrobienia

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
