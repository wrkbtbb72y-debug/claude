# Wnętrze 3D („Kubatura”)

<!-- Utworzone 2026-11-15. Krótki projekt — wystarczy ten plik. -->

Zasady wspólne (praca z Framerem, definition of done) są w głównym `CLAUDE.md` repozytorium.

- **Framer:** https://framer.com/projects/Bashful-Career--TrZY6V7hpIyWsOmfEYfW-dBvqu
  (project ID `TrZY6V7hpIyWsOmfEYfW`, nazwa w dashboardzie „Bashful Career”)
- **Produkcja / domena:** _TODO_ (nieopublikowane)
- **Język treści na stronie:** PL
- **Branche we Framerze:** edycje AI **nie tworzą brancha** (sprawdzone 2026-11-15) — zmiany idą
  od razu do `main`, nieopublikowane.
- **Tabela danych CMS w Figmie - zawsze aktualna** (stała prośba użytkownika, 2026-11-24). Gdy w sesji zmieni się
  cokolwiek, co dotyczy danych projektów w CMS (pola karty lub pełnej strony, typy pól, wymagane, limity, przykłady,
  wartości Category / usługi w What We Do, pola Featured projects), **sam zaktualizuj tabelę** w Figmie: plik
  BIURKO – VAAV (`Hr3x34LirWo1GJa1JRMkun`), ramka „Dane CMS” `328:27`, bez pytania. Wiersze to instancje
  „CMS Table / Row” `330:2` (właściwości No, Field, Type, Where, Required, Rules, Example) - nowy wiersz = nowa
  instancja w grupie, zmiana = `setProperties`, numeracja ciągła. Wartości Category: grupa 05 `330:230`.
  Po zmianie zrzut ramki i wzmianka w podsumowaniu. Szczegóły tabeli: sekcja „Tabela danych do CMS w Figmie”.
  To samo dotyczy arkusza **„Treści CMS - projekty (robocze)”** `332:142` (pola w blokach projektów i kategorie).
- **Nazwy warstw we Framerze: po angielsku** (prośba użytkownika, 2026-11-24). Nowe warstwy nazywać po angielsku;
  starsze notatki niżej używają dawnych polskich nazw - ID węzłów się nie zmieniły.

## Słownik (terminy uzgodnione z użytkownikiem)

- **Punkt zbiegu** (2026-11-19) — punkt, do którego zbiegają się linie siatki biegnące w głąb (oś z) w `SiatkaPerspektywy.tsx`
  (w kodzie `vx`, `vy` / `entry.cam`; położenie ustawiają kontrolki „Punkt zbiegu” = X i „Horyzont” = Y). Na `/` leży przy
  dolnej krawędzi siatki (Horyzont 0). Używać tej nazwy w rozmowie i notatkach.

## Marka NUMINO (ustalone z użytkownikiem 2026-11-22)

- **NUMINO** to marka (studio) budująca **branding dla firm oraz organizacji kultury i sztuki**.
- Tekst do opisu marki (od użytkownika, dosłownie): **„25 years of building brands with cultural impact”**.
- Używać tego przy pisaniu treści strony (hasła, opisy, meta). Innych faktów o marce nie dopisywać bez potwierdzenia.

## O projekcie (brief w skrócie)

Jednoekranowa aplikacja: trójwymiarowe, puste wnętrze o dużej powierzchni i wysokiej kondygnacji,
narysowane **samymi liniami krawędzi** (ściany, sufit, podłoga). Pod nim pasek z przyciskami —
na start wybór bryły: **koło** (kula), **kwadrat** (sześcian), **głaz** (nieregularna bryła).
Wybrana bryła spada z sufitu do wnętrza; bryły też tylko z linii, bez wypełnienia.

Ustalenia z użytkownikiem (2026-11-15):
- kolejne kliknięcia **dokładają** bryły (limit 12, potem znika najstarsza),
- styl **ciemny, blueprint** (tło `#0B0D10`, jasne linie wnętrza, bryły w akcencie `#FF5A36`),
- kamera: **ruch kursora lekko obraca widok**, bez ruchu kamera bardzo powoli dryfuje,
- (zmiana 2026-11-15) kamera **centralnie, wzrok na wprost** (perspektywa z jednym punktem zbiegu),
  jak oczy człowieka w wielkiej sali galerii; klimat **liminalny, monumentalny, prawie groźny**;
  kursor obraca widok **dużo słabiej** i z bezwładnością. Inspiracja skali i rodzaju przestrzeni:
  zdjęcie od użytkownika — szeroka, pusta sala galerii z betonową podłogą, ciężkie prostopadłościenne
  rzeźby ok. 2 m, w tylnej ścianie przejście do kolejnej sali (amfilada),
- bryła **spada z sufitu** i odbija się od podłogi; **nie obraca się** wokół własnej osi
  (zmiana 2026-11-15 — każda ląduje w losowym ustawieniu i stoi nieruchomo) (przerywany obrys miejsca lądowania
  + fala przy uderzeniu).

### Bryły i światło (od 2026-11-15, wersja „całkowicie inne”)

Prośba użytkownika: bryły losowo abstrakcyjne, wrażenie dematerializacji materii, doświadczenie
czegoś „całkowicie innego”, zaburzone proporcje, nieludzka skala; światło na zasadzie mocnego
kontrastu (światło vs mrok); bryły spadając jedna po drugiej mają się przecinać i zniekształcać.

- **Przyciski wybierają rodzinę**, kształt w niej jest losowy:
  - Trójkąt (od 2026-11-16): gruba trójkątna płyta (jak stalowa płyta ze zdjęć) albo ostrosłup;
    faktura jak Kwadrat (pionowe linie), wbija się ukośnie jak ostrze.
  - Walec (od 2026-11-16): walec z lekkim, miękkim wybrzuszeniem wzdłuż wysokości; faktura warstwic.
  - Koło: **geoida** (zmiana 2026-11-16) — wyraźnie kula, ale z miękkimi wybrzuszeniami
    i wklęsłościami (±6–17% promienia), lekko spłaszczona lub wydłużona, promień 2,6–6 m;
    wcześniejsze warianty (dysk, igła, torus, plastry) usunięte na prośbę użytkownika;
  - Kwadrat: **sześcian** (zmiana 2026-11-16) — tylko lekko nieregularny: proporcje 0,8–1,35,
    delikatne zwężenie ku górze (do 18%) i pochylenie; wcześniejsze warianty (monolit, belka,
    skręcona wieża, tesserakt, rozpadający się sześcian) usunięte — „kształt ma przypominać nazwę”;
  - Głaz: **kamień** (zmiana 2026-11-16) — nieregularny, fasetowany głaz o umiarkowanych proporcjach;
    warianty „odłamki” i „kryształ” usunięte.
- Skala od ludzkiej do nieludzkiej (część brył sięga prawie sufitu). Ok. 18% brył zatrzymuje się
  w powietrzu i lewituje.
- **Dematerializacja:** drżenie wierzchołków i pył odrywający się od bryły, unoszący się w stronę
  światła. **Bez linii przerywanych** (2026-11-16, prośba użytkownika): krawędzie brył, faktury
  i obrys miejsca lądowania są zawsze ciągłe — wcześniejsze „oddychające” przerwy usunięte.
- **Interakcje:** każda nowa bryła ląduje częściowo w poprzedniej (przyciągana do snopa światła).
  Bryły odkształcają się nawzajem (pole wypychające i skręcające), mocniej w chwili uderzenia.
  Miejsca przecięć (szwy) świecą kolorem akcentu `#FF5A36`, części głęboko w innej bryle przygasają.
- **Światło vs mrok:** z sufitu pada snop światła — widać tylko **promienie i drobiny w powietrzu**
  (rama świetlika, krawędzie snopa i obrys plamy na podłodze usunięte na prośbę użytkownika). Poza snopem sala tonie w mroku.
  Każde uderzenie bryły daje krótki błysk, który na moment odsłania całą salę.
- Bryły są jasne (`#F2EFE9`), akcent tylko na przecięciach.
- **Tylne linie brył są przygaszone** (2026-11-16): im dalej za środkiem bryły (patrząc od widza),
  tym słabsza linia — do ~15% jasności; dotyczy krawędzi, szwów, faktur i ziarna. Przód czyta się wyraźnie.

### Jak spadają bryły (od 2026-11-16)

- **Wysokość zrzutu** (2026-11-16): dolna krawędź bryły startuje z **1/3** wysokości sali (pierwsza),
  **2/3** (druga) i **3/3** (trzecia; zawsze pod sufitem). Ogólnie: (numer bryły / „Liczba brył”) × wysokość.
  Druga i trzecia zawsze spadają co najmniej ~1 m, zanim wbiją się w pierwszą.
- **Pierwsza bryła** spada w snop światła i ląduje na podłodze. Przy uderzeniu jej **dolna część
  lekko się odkształca** (rozpłaszcza i rozszerza w dolnych ~35% wysokości, sprężyste drgnięcie,
  potem zostaje niewielkie trwałe spłaszczenie).
- **Druga i trzecia** nie dotykają podłogi — spadają na pierwszą i **wbijają się w nią**
  (zatrzymują się z dolną częścią zagłębioną na 25–45% wysokości, licząc od powierzchni pierwszej
  bryły dokładnie pod miejscem upadku). **Druga** spada losowo w **lewą albo prawą połowę** pierwszej
  (patrząc od widza; przesunięcie 30–60% jej promienia, nawet gdy obiekt jest już obrócony),
  **trzecia** — w **przeciwną połowę** niż druga (zmiana 2026-11-16, zamiast „lekko obok środka”).
  Bryły z rodziny „Kwadrat” wchodzą ukośnie jak ostrze (przechył 20–40°),
  pozostałe z lekkim przechyłem; nie są dużo większe od pierwszej (max 1,25× jej rozmiaru)
  i zawsze mieszczą się pod sufitem.
- „Podgląd kształtu” w edytorze: głaz przebity dwiema bryłami kanciastymi (jak na zdjęciach-inspiracjach).

### Przebieg: 3 bryły → „Nadaj kształt” (od 2026-11-15)

- Zrzucić można **3 bryły** (kontrolka „Liczba brył”, domyślnie 3). Etykieta panelu pokazuje
  postęp („Dodaj bryłę · 1 z 3”, potem „Bryły opadają…”).
- Gdy wszystkie wylądują, **przyciski brył znikają** i pojawia się **„Nadaj kształt”**.
- „Nadaj kształt” (ok. 3,4 s): bryły zsuwają się w jeden zwarty obiekt w snopie światła, mocno
  się przy tym odkształcając; rozpad, drżenie i pył ustają (materia „zastyga”), szwy przecięć
  zostają jako złącza w kolorze akcentu, na końcu błysk światła. Potem na powierzchnie
  wchodzą **faktury** (inspiracja: zdjęcia użytkownika — stal kortenowska i granit):
  Kwadrat → pionowe, ciągłe linie (jak zacieki na stali; równy rozstaw, żeby łączyły się
  między ścianami), Głaz → ziarno granitu i drobne pęknięcia,
  Koło → gładkie, poziome warstwice.
- Po nadaniu kształtu pojawia się **„Od nowa”** (czyści salę i przywraca przyciski brył) —
  dodane, żeby nie było ślepego zaułka; do usunięcia, jeśli niepotrzebne.
- Stan sceny komponent ogłasza zdarzeniem `wnetrze3d:stan` (`{ phase, count, total }`,
  fazy: drop → settling → ready → merging → formed); overrides w `ShapeButtons.tsx`
  pokazują/ukrywają przyciski. **W edytorze widać wszystkie przyciski naraz** (overrides
  działają dopiero w podglądzie), dlatego panel ma zawijanie.
- „Podgląd kształtu” (kontrolka) pokazuje w edytorze gotowy, scalony obiekt z fakturami.

### Obracanie obiektu (od 2026-11-16, poprawka po nagraniu użytkownika)

- Cały obiekt (wszystkie bryły razem) obraca się **wyłącznie wokół własnej osi pionowej**
  (przez pierwszą bryłę) i **stoi na ziemi** — bez przechyłu, unoszenia i opadania.
- Sam z siebie obraca się **bardzo wolno** (~0,02 rad/s ≈ pełny obrót w 5 min, od wylądowania
  pierwszej bryły); ruch kursora skręca go tylko odrobinę (±0,05 rad).
- **Przeciągnięcie lewym przyciskiem myszy** (lub palcem) w poziomie obraca obiekt (spokojnie:
  0,0035 rad na piksel), z łagodnie wygasającą bezwładnością; ruch pionowy nic nie robi.
  Kursor nad sceną: „grab”. Bryły nie obracają się osobno. „Od nowa” zeruje obrót.

### Kamera „na linii horyzontu” (zmiana spoza sesji z Claude, zauważona 2026-11-16)

W kodzie `Wnetrze3D.tsx` ktoś zmienił kamerę: jest **nieruchoma, frontalna, z okiem na poziomie
podłogi** — cała podłoga zlewa się w jedną prostą linię (horyzont), na której stają bryły.
Wysokość tej linii na ekranie ustawia nowa kontrolka **„Linia”** (`horizon`; 2026-11-16 obniżona
z 0,68 na **0,84** wysokości sceny, żeby bryły dłużej spadały).
Kamera się nie rusza — ruch kursora działa teraz na obiekt (patrz „Obracanie obiektu”). Wymiary sali na instancji:
34 × 89 m, wys. 13,5 m. Kontrolka „Wys. oczu” nie jest już używana. Zmiany zachowane.

## Struktura (Home `augiA20Il`, `/`)

Breakpointy: Desktop `WQLkyLRf1` (1200), Tablet `yQMtFz1Ve` (810), Phone `sg8iiRp42` (390).

- **Ekran** `N06uDCvcg` — stack pionowy, `100vh` (min 520px), pełna szerokość (celowo bez maxWidth).
  - **Nawigacja** `GTrNEG7XB` — 64px (Phone 56px): **logotyp NUMINO** `NCKX7jaYC` (SVG, 80×46 px,
    Phone 66×38; od 2026-11-16 zamiast napisu „Kubatura”; plik źródłowy w `assets/numino-logo-nav.svg` —
    odwrócony i uproszczony z pliku użytkownika `numino_v2.svg`, który miał białe tło z literami
    „wyciętymi” w nim) + wskazówka
    „Poruszaj kursorem, aby się rozejrzeć” `pvlTW1vEa` (ukryta na Tablet/Phone).
  - **Treść** `Mtv7dJz2Z` (od 2026-11-16) — wiersz poziomy, wysokość `1fr`; Phone: pionowo (tekst nad sceną).
    - **Opis** `au8f8iUvr` — lewa połowa: nagłówek `hXCwV4zV6` „Puste wnętrze, w\u00A0którym trzy
      bryły stają się jedną formą” (preset „Nagłówek”, max 540 px), linia akcentu `WN9Igq2Zz`
      (240 px / Phone 120 px), podpis `F7tItlgMP` „Kubatura — nadaj kształt” (preset „Podpis akcent”).
      Tekst wzorowany na screenie użytkownika (długość/wielkość), treść robocza — do akceptacji.
    - **Wnętrze 3D** `Hohropvqf` — prawa połowa (`1fr`), komponent kodowy `Wnetrze3D.tsx`.
  - **Panel sterowania** `xHih95kf6` — „Dodaj bryłę” `A8IrKWoZJ` (ukryte na Phone) + przyciski
    `vmmVh1mwZ` (override `withPrzyciskiBryl`) — **same ikony, bez tekstu** (26 px, okrągłe 52 px):
    Koło `O9pkhZJRu`, Kwadrat `gcLtVqWZ1`, Głaz `kPExmBcjU`, Trójkąt `gjZINwi2_`, Walec `J9E6tPMgd`;
    **licznik** `hgMTNuQAu` (tekst `UOXcmZpxv`, „0/3” → „3/3”, overrides `withLicznikRamka`/`withLicznik`,
    widoczny do chwili „Pokaż”); **„Pokaż”** `ZqJgdZL2N` (dawniej „Nadaj kształt”, `withNadajKsztalt`),
    „Od nowa” `C6hHtDu5I` (`withOdNowa`).
    Etykieta panelu `A8IrKWoZJ` ma override `withEtykietaPanelu` (tekst zależny od etapu).

### Sekcja „Pasy zdjęć” i ucieczka horyzontu na `/` (2026-11-17)

- Pod „Ekran” (`N06uDCvcg`) doszła druga sekcja: instancja `hbGlvMNwJ` komponentu **„Pasy zdjęć”** `ORE7TUV1o`
  (100% × `100vh`). Komponent jest natywny (bez kodu): 4 poziome pasy jeden pod drugim (`Pas 1–4`, wysokość `1fr`,
  odstęp 2 px, tło „Tło”), każdy wypełniony zdjęciem (cover, kadr w pionie 22%) — widać tylko wycinek wysokości zdjęcia.
- **Najechanie na pas** → `SET_VARIANT` na wariant „Pas N otwarty” (ten pas `2fr`, czyli wysokość dwóch rzędów;
  pozostałe się ścieśniają, sekcja zostaje 100vh); zjechanie z sekcji → wariant „Spoczynek”. Przejście: spring 0,7 s,
  bez odbicia. ID: Spoczynek `j7i3ZSdKb`, pasy `sG5jPNHAZ`, `UOGKN3CAM`, `Lrjm4VgoX`, `DNmDMb6bu`; warianty otwarte
  `IVV9u_LME`, `zwqniuZ8M`, `AzIFoc_OJ`, `SAlA_idyt`.
- Zdjęcia od użytkownika (ulica — mężczyzna z papierosem i chłopiec; zdjęcie obsady „Brook Theater”) mają alt-text.
  Pasy 3 i 4 tymczasowo powtarzają te same zdjęcia — **czekamy na kolejne zdjęcia**. Podmiana: zaznacz pas w wariancie
  „Spoczynek” komponentu i zmień wypełnienie (warianty dziedziczą). Zdjęcia nie są podpięte pod zmienne komponentu,
  bo Framer ignorował wtedy pozycję kadru.
- `SiatkaPerspektywy.tsx`: kontrolka **„Zbliżenie (scroll)”** (`scrollZoom`, 0–12 sześcianów, domyślnie 0 = wył.).
  Przy przewijaniu w dół krata (pionowe i poziome linie, całe warstwy sześcianów) płynnie przysuwa się do kamery —
  wrażenie przybliżania sześcianów; horyzont stoi w miejscu. Pełne przybliżenie, gdy sekcja z siatką jest przewinięta
  o ~70% swojej wysokości; używa tego samego mechanizmu co „Ruch w głąb” (`flow`). Działa tylko w podglądzie / na stronie.
  Na `/` (`OirTRcAEZ`) ustawione 3 sześciany; `/home-2` i `/home-3` bez zmian.
  (2026-11-17 — zastąpiła wcześniejszą „Ucieczkę (scroll)”, gdzie horyzont uciekał do góry; zmiana na prośbę użytkownika.)
- **Zdjęcia w kwadratach** (2026-11-18): w `SiatkaPerspektywy.tsx` grupa „Zdjęcia w kwadratach” (`$control__zdjecia`):
  Pokaż, Zdjęcia (lista obrazów), Opisy (alt) — osobna lista tekstów w tej samej kolejności (lista obrazów przez API
  przyjmuje tylko obraz, bez opisu; opisy trafiają do ukrytej listy dla czytników ekranu), Kwadraty N×N (3), Warstwa
  (1 = najbliższa), Przesuń X/Y (w kwadratach od środka ekranu), Odstęp (ułamek kwadratu), **Padding** (px, od 2026-11-18;
  liczony dla kwadratów w spoczynku, przy przybliżaniu rośnie z kratą), Krycie, Przyciemnienie. Zdjęcia wypełniają
  (cover, kadr ze środka) kwadraty jednej warstwy kraty wokół środka ekranu; linie tej warstwy i bliższe rysują się
  na zdjęciach, dalsze chowają się za nimi; przy scrollu zdjęcia jadą razem z kratą ku kamerze i gasną, gdy ją mijają.
  Kolejność: od lewego górnego kwadratu wierszami. Gdy zdjęć jest mniej niż kwadratów: kontrolka **Powtarzaj**
  (domyślnie wył., 2026-11-18 — użytkownik nie chce powtórzeń) — wył. = zdjęcia trafiają najpierw na kwadraty
  „szachownicy” (dla 3×3: rogi i środek, układ „X”), reszta zostaje pusta; wł. = zdjęcia się powtarzają.
  Na `/` (`OirTRcAEZ`) włączone, 3×3, **9 różnych zdjęć** od użytkownika (2026-11-18; instalacje świetlne w kopułach,
  pawilon z żółtym zadaszeniem, portret mężczyzny w kapeluszu na pustyni), wszystkie z alt-textami. Kolejność dobrana
  tak, żeby podobne kolory nie stykały się bokami: [niebieska kopuła | żółty pawilon | pomarańczowa kopuła] /
  [biała kopuła | FILM (pod nim różowa kopuła z listy) | zielona kopuła] / [mężczyzna w pomarańczowej sali | różowe okno w niebieskim | mężczyzna w kapeluszu].
  Padding zdjęć: 20 px (prośba użytkownika, 2026-11-18) — między zdjęciem a liniami kwadratu widać ciemne tło.
- **Linie w głąb** (2026-11-18, `$control__rays`): linie zbiegające do punktu zbiegu urywały się twardo tuż przed
  pierwszą warstwą kraty. Grupa: **Przedłużenie** (ile sześcianów dalej ku kamerze sięgają; 0 = jak dawniej),
  **Długość zanikania** (na ilu sześcianach w głąb od bliższego końca krycie rośnie od 0% do pełnego; 0 = urwane),
  **Krzywa zanikania** (1 = równo, > 1 = dłużej przezroczyste, < 1 = szybciej nabiera koloru). Działa też na zarys
  odcinków w głąb w „Kosmosie”. Domyślnie 0/0/1 (inne strony bez zmian). Na `/`: przedłużenie 1, zanikanie 2, krzywa 1,4.
  Od 2026-11-18 także **Bez linii ze środka** (`rays.bezSrodka`): pomija 4 linie w głąb z narożników środkowego kwadratu
  (środek siatki zdjęć, z uwzględnieniem Warstwy i Przesunięcia X/Y zdjęć). Na `/` włączone (prośba użytkownika — linie
  przecinały film w środku).
- **Kwadraty na wysokość** (2026-11-18, `rzedy`): wielkość sześcianu liczona z rzeczywistej wysokości komponentu tak,
  by kwadrat pierwszej warstwy (tej ze zdjęciami) miał dokładnie wysokość/N px (0 = według „Wielkości sześcianu”).
  Żeby linie wypadały równo na górnej i dolnej krawędzi, horyzont musi być (N/2 − k − 0,5)/N — dla 5: 0,1 / 0,3 / 0,5 …
  Na `/` (`OirTRcAEZ`): 5 kwadratów na wysokość, horyzont zmieniony z 0,24 (ustawienie użytkownika) na 0,3; „Wielkość
  sześcianu” (220) nieużywana, dopóki „Kwadraty na wysokość” > 0. Siatka 3×3 zdjęć zajmuje środkowe 3 rzędy.
- **Sześciany ze zdjęć** (2026-11-18, `zdjecia.kostki`, wł. na `/`): każde zdjęcie = przednia ściana osobnego sześcianu,
  krawędź = bok zdjęcia (więc steruje nią **Padding**); sześcian sięga w głąb od miejsca zdjęcia (przy przesunięciu 0
  zdjęcia zostają tam, gdzie były). Rysowane w wklejce zdjęć: najpierw tylna ściana i krawędzie w głąb (zdjęcie je
  zasłania), potem zdjęcie, na końcu obrys przedniej ściany; kolor/grubość = linie siatki, jasność **Krawędzie**
  (`krawedzie`, na `/` 1,5). **Przesunięcie Z** (`przesZ`, w sześcianach kraty, + w głąb, − do widza) przesuwa wszystkie
  naraz (pozycje X/Y w kracie bez zmian). Na `/` 0.
  Poprawka (2026-11-18): zdjęcia **w pełni kryjące** (bez mgły głębi; zanik tylko przy mijaniu kamery), linie z płaszczyzny
  zdjęć — po poprawce 2026-11-18 znów **na wierzchu** (wklejka na z + 0,001): leżą między kwadratami, więc nie
  przecinają zdjęć, ale muszą przykrywać ściany boczne sześcianów (te są za płaszczyzną). **Ściany boczne** sześcianu wypełnione **kolorem przewodnim zdjęcia**
  (średnia ważona nasyceniem z miniatury 24×24; obrazy wczytywane z CORS, przy braku zgody — ponownie bez CORS i kolor
  zastępczy grafitowy), cieniowane: góra 1,12×, boki 0,8/0,7×, dół 0,55×; rysowane tylko ściany zwrócone do kamery.
  Film (r2.dev, bez CORS) → kolor z kontrolki **Kolor ścian filmu** (`zdjecia.filmKolor`, opcjonalny; pusty = próba
  odczytu z klatki, potem grafit). Na `/` ustawione `#9A9C88` (szaro-oliwkowy jak pierwsza klatka z palmami).
  **Film 2** (2026-11-18): pola „Film 2 (URL)”, „Film 2 w kwadracie”, „Kolor ścian filmu 2”, „Opis filmu 2 (alt)”
  (`film2`, `film2Miejsce`, `film2Kolor`, `film2Opis`). Na `/`: `…/hero/toaster-cartelle.mp4` w kwadracie **6** (prawy
  w środkowym rzędzie, zamiast zielonej kopuły — zdjęcie zostaje na liście, ale nie jest rysowane), kolor ścian `#5FC08E`
  (miętowe tło klatki), opis wg pierwszej klatki („srebrny toster na rozsypanych krakersach, na miętowym tle”).
  **Film 3** (2026-11-18, `film3`, `film3Miejsce`, `film3Kolor`, `film3Opis`): `…/hero/fornasetti2-cartelle.mp4` w kwadracie
  **4** (pierwszy w środkowym rzędzie, zamiast białej kopuły). Pierwszej klatki nie udało się zobaczyć (zrzuty Framera nie
  wczytały filmu) — **TODO: kolor ścian (teraz grafit zastępczy) i opis („Zapętlony film”)**.
  **Film 4** (2026-11-18, `film4…`): `…/hero/jslack.mp4` w kwadracie **3** (prawy górny, zamiast pomarańczowej kopuły).
  **TODO: kolor ścian i opis** (pierwszej klatki nie widać w zrzutach).
  **Tempo filmów** (2026-11-18, `filmTempo`, `film2Tempo`, `film3Tempo`, `film4Tempo`; 0,1–4, 1 = normalne; `playbackRate`).
  Na `/`: film 3 (kwadrat 4) **0,5** — zwolniony na prośbę użytkownika; pozostałe 1.
  **Przyciemnienie ścian** (`zdjecia.scianyCien`, 0–1, 2026-11-18): przyciemnia tylko boczne ściany sześcianów
  (0 = kolor przewodni, 1 = czarne), zdjęcia bez zmian; od 2026-11-18 (późniejsza zmiana) **działa jednakowo dla sześcianów
  ze zdjęciami i z filmami** (wcześniej filmy były wyłączone). Na `/` 0.
  **Cofnięcie na hover** (`zdjecia.hoverCofniecie`, px, domyślnie 40; 2026-11-18): sześcian ze zdjęciem/filmem pod kursorem
  płynnie cofa się w głąb o tyle px (w skali przedniej ściany, przeliczone na głębię kraty), po zjechaniu wraca.
  Pozycja kursora z `window` (`pointermove`), bo komponent ma `pointerEvents: none`; trafienie liczone na prostokącie
  zdjęcia w spoczynku. Działa tylko w podglądzie/na stronie (w edytorze i przy ograniczonym ruchu — bez efektu).
  Od 2026-11-18 wolniej i płynniej: stały czas przejścia **Czas cofnięcia** (`hoverCzas`, 0,8 s) z ease-in-out (zawraca
  płynnie z bieżącego miejsca) + **Przyciemnienie na hover** (`hoverCien`, 0,25): zdjęcie i ściany ciemnieją razem z cofaniem.
  **Zmiana 2026-11-18:** hover = **lekkie powiększenie** (`hoverPowiekszenie`, 0,05 = 5%, wokół środka przedniej ściany,
  przejście 0,35 s); **kliknięcie** = cofnięcie w głąb (kontrolka „Cofnięcie po kliknięciu”, `hoverCofniecie` 40 px) z
  przyciemnieniem („Przyciemnienie przy cofnięciu”) w „Czasie cofnięcia”; sześcian zostaje cofnięty, dopóki kursor jest
  nad nim, po zjechaniu wraca. Kliknięcie łapane z `window` (`pointerdown`).
  Powiększenie poprawione: ease-out w obie strony (wygładzanie wykładnicze — rusza od razu, łagodnie hamuje), szybciej;
  **Czas powiększenia** (`hoverPowCzas`, 0,4 s — wydłużony z 0,25 s 2026-11-18; ≈ czas dojścia do ~98%).
  **Czas powrotu** (`hoverPowCzasPowrot`, 0,9 s): osobny, dłuższy czas powrotu do zwykłej wielkości po zejściu kursora.
  Kierunek powiększenia (2026-11-18): w stronę środka siatki zdjęć — zakotwiczona krawędź zewnętrzna (lewy górny rośnie
  w prawo i w dół, prawy dolny w lewo i w górę, środkowe w kolumnie/rzędzie symetrycznie wzdłuż tej osi, środkowy na boki).
  Pole reakcji na hover (i kliknięcie) = **cały kwadrat kraty**, w którym stoi sześcian (z odstępem), nie tylko zdjęcie (2026-11-18).
  Sąsiedzi (także po skosie) sześcianu na hover kurczą się od strony, w którą on rośnie, o tyle samo — odstęp (padding)
  między nimi się nie zmniejsza. Wzrost liczony najpierw dla wszystkich (`growMap` [lewo, prawo, dół, góra]), potem rysowanie.
  **Później 2026-11-18: cofnięcie po kliknięciu usunięte** (kod, nasłuch `pointerdown` i kontrolki „Cofnięcie po kliknięciu”,
  „Czas cofnięcia”, „Przyciemnienie przy cofnięciu”) na prośbę użytkownika. Zostaje: powiększenie na hover + kursor „rączka”.
  **Scal rząd nad zdjęciami** (`zdjecia.scalNad`, px, domyślnie 1600, 0 = nigdy; 2026-11-18): gdy szerokość komponentu > próg,
  puste sześciany w rzędzie tuż nad siatką zdjęć (nad jej kolumnami) łączą się w jeden prostopadłościan — pomijane są ich
  wewnętrzne krawędzie: pionowe linie na przedniej i tylnej płaszczyźnie warstwy zdjęć (tylko w tym rzędzie) i odcinki
  linii w głąb między tymi płaszczyznami w wewnętrznych narożnikach.
  Od 2026-11-18 także **rząd pod zdjęciami** (kontrolka przemianowana na „Scal rzędy nad/pod zdjęciami”, ten sam próg).
  **Kliknięcie = „fokus”** (2026-11-18): kliknięty sześcian rośnie do prostokąta całej siatki zdjęć w spoczynku (od krawędzi
  pierwszego do ostatniego zdjęcia, z odstępami), pozostałe kurczą się do swoich środków aż znikną; animacja ease-in-out
  **Czas po kliknięciu** (`fokusCzas`, 0,8 s). Kolejne kliknięcie gdziekolwiek przywraca spoczynek. Podczas fokusu hover
  wyłączony, wybrany sześcian rysowany na końcu, a linie kraty z płaszczyzny zdjęć idą pod sześciany (żeby nie przecinały
  powiększonego zdjęcia). Kliknięcia z `window` (`pointerdown`). Na razie bez linków/podstron.
  Kursor „rączka” (`pointer`) nad sześcianami: ustawiany na `document.body` (dziedziczy się, bo warstwy nad siatką mają
  `pointerEvents: none`), zdejmowany po zjechaniu i przy odmontowaniu komponentu.
  **Zdjęcie na ścianach** (`zdjecia.scianyObraz`, domyślnie wł.; 2026-11-18): ściany boczne pokryte tym samym zdjęciem/filmem
  co przód (kadr „cover” ze środka w proporcjach ściany), w perspektywie — ściana dzielona na 6 pasów w głąb, każdy pas
  rysowany dwoma trójkątami z przekształceniem afinicznym (canvas 2D nie ma mapowania tekstur); cieniowanie nakładką
  (góra jaśniej, boki/dół ciemniej, plus „Przyciemnienie ścian”). Gdy obraz/film nie jest jeszcze wczytany — kolor jak dawniej.
  **Głębokość sześcianów** (`zdjecia.kostkiGlebia`, 0,02–1, 2026-11-18): głębokość względem boku zdjęcia (1 = sześcian,
  mniej = płytszy prostopadłościan). Na `/` 1.
  **Jasność krawędzi** (`zdjecia.krawedzie`, dawniej „Krawędzie”; 2026-11-18 poprawione): 0 = bez krawędzi, 1 = kolor
  linii siatki, powyżej 1 dodatkowe rozjaśnienie bielą (3 = białe) — wcześniej wartości > 1 nic nie zmieniały. Na `/` 1.
- **Film w kwadracie** (2026-11-18): kontrolki „Film (URL)”, „Film w kwadracie” (numer kwadratu wierszami od lewego
  górnego, 0 = bez filmu) i „Opis filmu (alt)”. Film MP4 jest wyciszony, zapętlony, rysowany na tej samej płaszczyźnie co
  zdjęcia (cover + padding); w edytorze i przy ograniczonym ruchu widać tylko pierwszą klatkę. Na `/`: kwadrat 5
  (środek siatki; 2026-11-18 zamieniony miejscami z białą kopułą, która jest teraz w kwadracie 4; różowa kopuła zostaje
  na liście na pozycji 5, ale pod filmem nie jest rysowana),
  URL `https://pub-72bc6220135048bfb52d7bb83acf5ea2.r2.dev/048e2bef5dd7/hero/meatharvest-jslack.mp4` (zewnętrzny hosting
  użytkownika). Opis filmu roboczy („Zapętlony film”) — **TODO: poprosić użytkownika o opis treści**.
  Na Phone kwadraty są szersze niż ekran — widać środkową kolumnę i fragmenty bocznych.
- Wgrywanie plików do Framera z sesji w chmurze wymagało dodania hosta `mcp.framer.com` do sieci środowiska (zrobione).

## Kolumny siatki jak Navi II (Desktop `/`, 2026-11-18)

- Użytkownik dodał drugi pasek nawigacji **„Navi II”** `gtiExDlXS` (absolutnie, top 63 px, szer. 1200 px, padding boczny
  80 px; 4 przyciski `1fr` + środkowy element „middle” `AyXVnZ187` 442 px). Siatka ma się do niego dopasować.
- Wcześniej rozjazd podglądu z canvasem: kwadraty liczone z wysokości (wys./5), a pasek ma stałe wymiary → zgadzało się
  tylko przy jednej wysokości okna.
- `SiatkaPerspektywy.tsx`, grupa „Kamera i przestrzeń”: **Kolumny jak Navi II** (`kolumny`), **Padding boczny**
  (`kolPadding`, 80), **Środek (łącznie)** (`kolSrodek`, 442), **Kolumny w środku** (3), **Kolumny z boku** (2). Linie
  pionowe pierwszej warstwy: środkowe kolumny = środek/3 (stałe), boczne = (szer. − 2·padding − środek)/(2·boczne) =
  szerokość przycisku; kolumny poza ekranem jak boczne; wyśrodkowane na środku komponentu. Rzędy bez zmian (wys./5).
  Zdjęcia, „Bez linii ze środka”, węzły, rozświetlenie i Kosmos korzystają z tych samych kolumn.
- **Stała wysokość rzędów** (2026-11-18, `kolStalaWys`, domyślnie wł. przy „Kolumnach jak Navi II”; `kolWysokosc`
  0 = jak szerokość środkowej kolumny, czyli kwadraty ≈ 147,3 px): rzędy nie zmieniają się z wysokością ekranu
  („Kwadraty na wysokość” jest wtedy pomijane); linie poziome przesunięte tak, by rząd na środku komponentu był
  wyśrodkowany — 3 rzędy zdjęć zawsze na środku siatki. **Lista tytułów (natywna, 60% wysokości) przestała się z nimi
  pokrywać** — 2026-11-18 naprawione: ramka listy `AzgVkCy4j` ma stałe **442 px** (= 3 rzędy), a kolumna „Opis”
  `au8f8iUvr` na Desktopie górny padding **68 px** (= przypięcie górne siatki; „Treść” zaczyna się od góry sekcji,
  siatka od 68 px), więc środek listy = środek siatki. Stacki w liście użytkownik sam zmienił na `height: auto`
  (gap 12/8 px, padding dół 8 px) — leżą jeden pod drugim od góry ramki, nie po jednym na rząd.
- 2026-11-18 (wyrównanie do sześcianów): użytkownik przebudował listę — w `Lista` są 3 widoczne wiersze `1fr`
  (`cbVbz8owY` z tekstem „Design studio…”/nagłówkiem `uMUb36gPC`, `E7a5Yw8Ck` ze Stackiem 2, `y6NlewCHD` ze Stackiem 3;
  Stack 1 ukryty w `kIxYM5cQx`). Wiersze dostały padding 20 px góra/dół (= padding zdjęć) i wyrównanie do góry
  (`stackAlignment: start`; wcześniej środek), więc tekst zaczyna się równo z górą przedniej ściany sześcianów w rzędzie.
  Górny padding „Opis” 68 → **80 px** (siatka przypięta teraz na 80 px). Przy zmianie paddingu zdjęć/przypięcia siatki
  zmienić te wartości razem.
- Później (2026-11-18): stacki „1”, „2”, „3” (`cbVbz8owY`, `E7a5Yw8Ck`, `y6NlewCHD`) mają **wysokość przedniej ściany
  sześcianów** (≈ 107 px = rząd 147,3 − 2 × padding 20): `Lista` ma padding 20 px góra/dół i gap 40 px (= 2 × padding
  zdjęć), stacki `1fr` bez paddingu; wyrównanie treści w stackach zostawione jak ustawił użytkownik.
- **Rzędy do krawędzi** (2026-11-18, `kolRozciagnij`, domyślnie wł.; `kolRzedyBoczne` 1): przy stałej wysokości rzędów
  środkowe rzędy (tyle co „Kolumny w środku”) mają stałą wysokość, a skrajne rozciągają się dokładnie do górnej i dolnej
  krawędzi komponentu — górna linia kraty pokrywa się z dolną ramką paska nawigacji (siatka przypięta na 68 px), dolna
  z dolną krawędzią ekranu; dalsze rzędy (w głębi) mają wysokość skrajnych. Odpowiednik kolumn bocznych w pionie.
- 2026-11-18: na chwilę włączone na Tablecie — **cofnięte** (użytkownik chciał czegoś innego). Zamiast tego
  **Podziel boki zdjęć** (`kamera.podzialBoku`): kolumna tuż obok siatki zdjęć (z lewej i z prawej) jest dzielona na pół
  **tylko w rzędach zdjęć** (6 prostopadłościanów): pionowa linia na przedniej i tylnej ścianie warstwy zdjęć + krawędzie
  w głąb na granicach rzędów. Działa w obu trybach kolumn. Włączone na Desktopie i Tablecie, Phone wył.
  Później tego dnia (prośba użytkownika): podział **na całą wysokość** — pionowe linie od dołu do góry ekranu na przedniej
  i tylnej ścianie warstwy zdjęć, krawędzie w głąb na każdej linii rzędu.
- `/` Desktop (`OirTRcAEZ`): włączone, 80 / 442 / 3 / 2. Tablet i Phone: wyłączone (nadpisanie na replikach) —
  siatka równomierna jak dawniej. **Wartości trzeba zmieniać ręcznie razem z Navi II** (komponent nie czyta paska).
- Siatka (`OirTRcAEZ`) ma przypięcia left 0 / right 0 → rozciąga się na całą szerokość, boczne kolumny rosną
  (potwierdzone przez użytkownika; „1200 px” to tylko rozmiar na canvasie). Navi II ma w danych tylko przypięcie
  right 0 + szer. 1200 px — do sprawdzenia w podglądzie, czy przyciski rosną; jeśli nie, ustawić left/right 0.
  Przypięcie górne siatki zmienione przez użytkownika na 68 px (2026-11-18).

- **Później 2026-11-18:** „Podziel boki zdjęć” **usunięte** (kod i przełącznik) na prośbę użytkownika. Wszystkie
  ustawienia gridu przeniesione z „Kamera i przestrzeń” do osobnej grupy **„Grid”** (`$control__grid`, na początku panelu):
  Włącz (`kolumny`), Padding boczny, Kolumny po bokach (`kolBoczne`), Środek (łącznie), Kolumny w środku, Stała wys.
  rzędów, Wysokość rzędu, Rzędy do krawędzi, Rzędy nad/pod. Kod czyta najpierw `grid`, zapasowo `kamera`. Wartości
  przepisane: Desktop wł. (80 / 2 / 442 / 3 …), Tablet i Phone wył. (nadpisanie `grid.kolumny`).

## Lista tytułów zamiast dużego logo na `/` (2026-11-18)

- Duże logo NUMINO w kolumnie „Opis” (kontener `p1krlsuOc`) **ukryte** (nie usunięte) na wszystkich breakpointach.
  W tej samej kolumnie (`au8f8iUvr`, ma `pointerEvents: none`, lista ma `auto`) jest ramka **„Lista — 3 rzędy kwadratów”**
  `AzgVkCy4j`: wysokość 60% obszaru pod nawigacją = dokładnie 3 środkowe rzędy kwadratów siatki (siatka ma 5 kwadratów
  na wysokość), padding góra/dół = padding zdjęć (teraz 8 px — użytkownik zmienił z 20), więc pierwszy i ostatni wiersz
  zrównują się z krawędziami zdjęć (od 2026-11-18 padding przeniesiony na stacki — patrz niżej). W środku `Lista`
  `HD2wSnn92` (stack pionowy, overflow clip).
- Wiersze: 25 instancji nowego komponentu **„Wiersz listy”** `ZIOR8bv28` (zmienna „Etykieta” `VswI4OLK4`; wariant
  Domyślny `XHXBlNg_F` — przezroczysty, kursor pointer; wariant **Hover** `p0s9Z04Ba` — kolor „Akcent”, przejście 0,15 s).
  **Bez linków** (na prośbę użytkownika) — link dodać na wariancie/instancji, gdy będą strony. Ostrzeżenie lintera
  o nieprzezroczystym tle wariantów zostawione celowo (lista leży na siatce).
- Nowy styl tekstu **„Lista”** `dhBgkQbVl`: PP Neue Montreal 600, 14 px, interlinia 1,1, odstęp −0,01 em, kolor „Tekst”
  (wzór: screen użytkownika z listą tytułów magazynów).
- Treść wierszy: tymczasowo tytuły z tego screena — **TODO: docelowa lista od użytkownika**.
- **Trzy stacki** (2026-11-18): lista podzielona na 3 stacki, każdy na wysokość jednego kwadratu (`height: 1fr` w ramce
  60%, padding góra/dół = padding zdjęć, wiersze rozłożone space-between, więc zrównują się z rzędami zdjęć):
  „20 — A” `ZLpqZFyfJ`, „A — Ar” `czOOevMSP`, „As — Br” `QyG3AXvrR` — po nagłówku (styl **„Lista nagłówek”** `CNPDFVung`:
  jak „Lista”, h3, kolor „Tekst drugorzędny”) i 7 wierszy. Wierszy jest 21: użytkownik sam usunął Atmos Magazine, Autre
  i Avant Garde, a „C/O Vienna Magazine” usunięty, żeby wyszło po równo. 8 linii mieści się w kwadracie od ok. 760 px
  wysokości okna. Nagłówki (zakresy alfabetyczne) robocze.
- Tablet i Phone: lista ukryta (nachodziłaby na zdjęcia) — **TODO: zapytać, gdzie ma być na mniejszych ekranach**.
  Przy niskich oknach (< ok. 760 px) 25 wierszy może się nie zmieścić (lista jest przycinana).

- **Logo w tle** (2026-11-18): kontener `p1krlsuOc` (dawniej „inside” w kolumnie „Opis”, użytkownik przeniósł go do sekcji)
  przemianowany na „Logo w tle”: bezpośrednie dziecko „Ekran”/hero `N06uDCvcg`, **pierwsza warstwa** (za siatką
  perspektywy, zIndex 0 jak siatka, ale wcześniej w kolejności), absolutnie na całą sekcję (przypięcia 0), stack
  wyśrodkowany w obu osiach, `pointerEvents: none` — logo NUMINO (`DTM5Bxuta`, maks. 540 px; Phone 66 px) wyśrodkowane
  względem szerokości i wysokości ekranu; sześciany ze zdjęciami je przykrywają.

- **Przycisk „View all”** (2026-11-18): w prawej kolumnie hero („Column Right X” `Hgbr5CLZ2` → „Lista” `KQAHUSzg4`) stack „3”
  `tSrfZh5Ok` (nagłówek „Web Design” + 3 wiersze) zastąpiony przyciskiem: zawartość usunięta, ramka została jako slot
  (przemianowana „3 — przycisk”, żeby nie zmienić układu rzędów), w środku instancja **„Przycisk akcji”** `TIteksTiL`
  (wariant Główny — jasna pigułka, etykieta „View all”; wybór użytkownika). **TODO: link** (brak strony docelowej).
- **Tekst zamiast „View all”** (2026-11-19): przycisk `TIteksTiL` usunięty, slot `tSrfZh5Ok` przemianowany na „3 — tekst”
  (szer. 118 px, padding prawy 12 px = lustro lewego paddingu 12 px w „Column Left”, wyrównanie do prawej). W środku
  jeden akapit `UNBIO7wfZ` „Images, motion and space, shaped into one quiet form.” (wyrównany do prawej, `textWrap: balance`)
  w nowym presecie **„Lista akapit”** `y2wkQleXW` (jak „Lista”: PP Neue Montreal 400, 14 px, −0,01 em, kolor „Tekst”, ale
  interlinia **23 px** = rytm wierszy listy z lewej). Wychodzą 4 linie na wysokości nagłówka i 3 wierszy „Animation” z lewej.
  Treść robocza, po angielsku jak sąsiednia lista — **do akceptacji** (ew. wersja PL).

### Hover „Archer Magazine” → zdjęcie na środkowym rzędzie (2026-11-19)

Użytkownik zbudował to sam w komponencie (bez kodu); Claude poprawił błędy.
- Nowy komponent **„Wiersz listy ze zdjęciem”** `NeuI0X8QN` (duplikat „Wiersz listy”): warianty Domyślny `invI6kC7U`
  (Mouse Enter → Variant 2) i Variant 2 `r_PB1ieWz` (Mouse Leave → Domyślny), tween 0,35 s. Korzeń Fit content (pole hover
  = sam napis). „Photo wrapper” `YtCQW0LMW`: Absolute, left 326 px, 443 px szer., overflow clip, zdjęcie w środku
  wyśrodkowane (center anchor). Domyślny: **wys. 1 px, top 17,5 px, opacity 0**; Variant 2: **wys. 149 px, top −56,5 px,
  opacity 1** → środek stoi w miejscu, zdjęcie rozsuwa się od środka w górę i w dół i tak samo się chowa.
- **Dlaczego 1 px, nie 0:** animacja wysokości do 0 px jest we Framerze pomijana (zdjęcie znikało nagle przy zjechaniu).
- Pozycja liczona względem wiersza „Archer Magazine” (lewa kolumna i siatka są wyśrodkowane na tej samej linii, więc
  przesunięcie nie zależy od wysokości okna): zdjęcie przykrywa dokładnie środkowy rząd 3 kwadratów (sprawdzone zrzutem
  z tymczasowo włączonym Variant 2). Przy zmianie paddingu listy / położenia siatki — przeliczyć top/left.
- Instancja w lewej kolumnie podmieniona na nowy komponent: `BeP_BB86I` (dawniej `ueKklTq2L`). Ramki nadrzędne
  „2” `r2_9T5NM3`, „Animation links” `E7a5Yw8Ck`, „Lista” `HD2wSnn92` mają Overflow: Visible (ustawił użytkownik).
- Z oryginalnego „Wiersza listy” `ZIOR8bv28` zdjęcie usunięte, korzeń z powrotem Fit content — pozostałe wiersze
  (Arts And Flowers, Arxipelag, prawa kolumna) bez zdjęcia. Jego hover to teraz Variant 2 `PPxxZBGly` przez
  Mouse Enter/Leave (zmiana użytkownika; dawny wariant Hover `p0s9Z04Ba` nie istnieje).

## Siatka perspektywy — układ kontrolek (od 2026-11-18)

Na prośbę użytkownika („za dużo kontrolek, ciężko się połapać”) wszystkie kontrolki `SiatkaPerspektywy.tsx` są w grupach,
w tej kolejności: **Kamera i przestrzeń** (`kamera`: horyzont, punkt zbiegu, kwadraty na wysokość, wielkość sześcianu,
głębia, zbliżenie przy scrollu, ruch w głąb) → **Linie** (`linie`: kolor, grubość, krycie, przerwy, tempo zaniku,
miękkość granic) → **Linie wokół sześcianów** (`wokol`, od 2026-11-19) → Nad horyzontem → Pod horyzontem → Linie w głąb → Bliskie linie → Tajemnica → **Świetliki podróżujące**
(`swietliki`: poziome/pionowe/w głąb + kierunki, długość światła, prędkość, dystans, gaśnięcie, rozświetlenie, kolor
światła) → Świetliki w węzłach → Rozświetlenie → Zdjęcia w kwadratach → Logo 3D → Kosmos → Tło.
- Dawne płaskie kontrolki (`horizon`, `cubeSize`, `lineColor`, `firefliesH` …) przeniesione do grup `kamera` / `linie` /
  `swietliki`; wartości trzech instancji (`/` `OirTRcAEZ`, `/home-2` `GCcSRW8rC`, `/home-3` `GA3zheMSK`) przepisane
  1:1 (tablety/telefony nie miały osobnych nadpisań). Kod czyta najpierw wartość z grupy, a gdy jej brak — dawną płaską
  właściwość (zgodność wstecz). W starszych notatkach poniżej nazwy typu „Horyzont”, „Przerwy” odnoszą się do kontrolek,
  które są teraz w tych grupach.

- **Równe gaśnięcie świetlików** (2026-11-18, `swietliki.rowno`, domyślnie wł. — działa na wszystkich trzech stronach):
  użytkownik nie chciał, by świetliki przed zgaśnięciem naprzemiennie gasły i rozbłyskały. Przyczyny: wbudowane mruganie
  (sinus), zależność jasności od przerw/szumu linii, po której biegną, i gaśnięcie dopiero na końcu trasy. Teraz: pełna
  jasność w chwili pojawienia się na ekranie, równy spadek do zera na długości „Dystansu biegu”, bez mrugania; jasność
  kropki i poświaty zależy tylko od głębi (i zaniku linii w głąb przy kamerze), nie od przerw. „Czas gaśnięcia” działa
  tylko przy wyłączonym „Równym gaśnięciu” (dawne zachowanie).

- **Start świetlików z punktów styku** (2026-11-18, `swietliki.start`: „Punkty styku” `wezly` — domyślnie, wszystkie strony /
  „Krawędź ekranu” `krawedz` — dawne zachowanie): świetliki poziome i pionowe pojawiają się w losowym skrzyżowaniu linii
  (narożniku sześcianów) na swojej linii, widocznym na ekranie, z krótkim łagodnym pojawieniem; potem biegną w kierunku
  z ustawień i gasną jak dotąd. Świetliki w głąb bez zmian (start od krawędzi).
- **Pojawianie świetlików** (2026-11-18): przy „Równym gaśnięciu” jasność od 0 równo rośnie na długości „Dystansu biegu”,
  potem tak samo równo spada do 0 (trasa = 2 × dystans) — pojawianie tak stopniowe jak gaśnięcie, bez nagłego rozbłysku.
- **Jednakowa trasa poziomych i pionowych** (2026-11-18): „Dystans biegu” liczony od **wysokości komponentu** dla obu rodzajów
  (wcześniej od długości linii, więc poziome — dłuższe linie — jechały dłużej). Świetliki w głąb: nadal od długości linii.

### Punkt zbiegu za kursorem (2026-11-21) — usunięte

Dodana i tego samego dnia **usunięta na prośbę użytkownika** opcja „Zbieg za kursorem” (punkt zbiegu przesuwał się w stronę
kursora: prawa część ekranu → w prawo, lewa → w lewo; kontrolki Zakres ruchu, Czas reakcji, Kursor względem, Kierunek).
Kod i kontrolki wycofane z `SiatkaPerspektywy.tsx`. W instancji na `/` (`OirTRcAEZ`) w `$control__kamera` zostały osierocone
wartości `zbieg*` — Framer nie daje ich skasować przez API, kod ich nie czyta (nieszkodliwe). Nie dodawać ponownie bez prośby.

### Linie wokół sześcianów (2026-11-19)

Prośba użytkownika: wzmocnić kreski kraty otaczające sześciany ze zdjęciami, osobnymi kontrolkami; przy kontrolkach na 0
kreski mają wyglądać jak teraz (bazą są globalne ustawienia z grupy „Linie”, kontrolki tylko dokładają).
- `SiatkaPerspektywy.tsx`, grupa **„Linie wokół sześcianów”** (`$control__wokol`, zaraz po „Linie”):
  **Grubość +** (px dodawane do „Grubości”), **Krycie +** (0–1, dociąga krycie do pełnego), **Ciągłość** (0–1, zapełnia
  przerwy z „Przerw”/„Tajemnicy”), **Rozjaśnienie** (0–1, miesza „Kolor” linii z **Kolorem rozjaśnienia**, domyślnie biały),
  **Zakres** (Przód = płaszczyzna zdjęć / **Przód + linie w głąb** — domyślnie, odcinki linii w głąb między płaszczyzną
  zdjęć a tylną płaszczyzną / Cała bryła = też tylna płaszczyzna), **Zasięg poza zdjęcia** (0–6 kwadratów; 0 = tylko
  obrys siatki zdjęć i linie między sześcianami).
- Działa tylko przy włączonych „Zdjęciach w kwadratach”. Obszar = prostokąt siatki zdjęć (N×N, z „Warstwą” i „Przesuń X/Y”),
  linie dzielone dokładnie na jego granicach; odcinki poza nim rysowane jak dotąd. Wszystkie dodatki na 0 → kod omija
  nowy styl (rysunek identyczny jak przed zmianą).
- Na `/` (`OirTRcAEZ`) wszystko na 0 (wygląd bez zmian) — użytkownik dostraja sam. Test (potem cofnięty): Grubość + 1,
  Krycie + 1, Ciągłość 1, Rozjaśnienie 0,7 — wyraźna jasna rama 3×3 wokół sześcianów na wszystkich breakpointach.
- W kodzie była już funkcja `parseColor` (inna sygnatura) — nowa nazywa się `wkParseColor`.
- Później (2026-11-19) użytkownik sam ustawił na `/`: Krycie + 0,35, Ciągłość 0,4, Rozjaśnienie 0,6 (Grubość + 0,
  Zakres „Przód + linie w głąb”, Zasięg 0).

### Zmniejszanie sześcianów od kursora (2026-11-19)

Prośba: wielkość sześcianów ma zależeć od kursora nad siatką — bez kursora bez zmian; kursor nad komponentem → im dalej
od kwadratu, który otacza sześcian, tym sześcian trochę mniejszy.
- Grupa „Zdjęcia w kwadratach”: **Zmniejszanie od kursora** (`zdjecia.kursorZmn`, 0–0,5; 0 = wył.), **Zasięg zmniejszania**
  (`kursorZasieg`, px — przy tej odległości zmniejszenie jest pełne, liniowo), **Odległość od** (`kursorOdn`: „Kwadratu
  sześcianu” `wlasny` — każdy sześcian od swojego kwadratu kraty, domyślnie / „Całej siatki zdjęć” `siatka` — wszystkie
  razem od prostokąta siatki 3×3), **Czas reakcji** (`kursorCzas`, s, wygładzanie).
- Odległość = od kursora do prostokąta (0, gdy kursor w środku); sześcian skalowany wokół środka przedniej ściany, więc
  głębokość maleje razem z nim. „Nad komponentem” = kursor w granicach komponentu (z `window`, bo komponent ma
  `pointerEvents: none`); tylko mysz/pióro (dotyk — bez efektu); wyłączone podczas „fokusu” po kliknięciu, w edytorze
  i przy ograniczonym ruchu. Działa razem z powiększeniem na hover (sześcian pod kursorem ma pełną wielkość + hover).
- Na `/` (`OirTRcAEZ`): 0,15 / 600 px / Kwadratu sześcianu / 0,4 s. Zrzuty Framera nie mają kursora — efekt sprawdzalny
  tylko w podglądzie.

- 2026-11-20 — użytkownik: „zmniejsza je wszystkie jednakowo” (był tryb „Kwadratu sześcianu”, 0,3 — przy kursorze dalej
  niż zasięg wszystkie dochodziły do tego samego maksimum, a bliżej najbliższy był największy). Nowy, trzeci tryb
  **„Siatki — najbliższy najmniejszy”** (`kursorOdn: "najblizszy"`): siła = „Zmniejszanie” × odległość kursora od całej
  siatki zdjęć / „Zasięg” (kursor w siatce → bez zmian), rozłożona wagą po odległości kursora od kwadratu każdego
  sześcianu: najbliższy 1, najdalszy 1 − **Różnica** (`kursorRoznica`, domyślnie 0,7; liniowo pomiędzy). Na `/`:
  najblizszy, Różnica 0,7, Zmniejszanie 0,3 (ustawione przez użytkownika), Zasięg 600 px.

- 2026-11-20 (później) — kontrolka **„Najbliższy maleje o”** (`kursorNajbl`, 0–0,9, widoczna tylko w trybie „Siatki —
  najbliższy najmniejszy”): o ile maleje sześcian najbliżej kursora (pełna wartość, gdy kursor jest „Zasięg” od siatki lub
  dalej). W tym trybie zastępuje „Zmniejszanie od kursora” (ukryte; gdy `kursorNajbl` brak — kod bierze `kursorZmn`).
  Na `/` przepisane z dotychczasowego `kursorZmn` = 0,34 (wygląd bez zmian); Różnica na `/` = 0,4 (ustawienie użytkownika).

- 2026-11-20 — **reakcja także nad paskiem nawigacji**: kontrolka **„Także nad siatką”** (`zdjecia.kursorNad`, px, domyślnie 0,
  widoczna, gdy zmniejszanie jest włączone): obszar „kursor nad komponentem” sięga tyle px ponad górną krawędź siatki.
  Siatka nie dostaje zdarzeń nawigacji — pozycja kursora i tak jest czytana z `window`, więc wystarczyło poszerzyć
  warunek. Na `/` (`OirTRcAEZ`) 80 px = przypięcie górne siatki = wysokość Navi (Phone: Navi 56 px, ale obszar do 80 px
  i tak leży nad siatką); Tablet/Phone dziedziczą. Odległość liczona jak dotąd, więc kursor na pasku jest „daleko
  nad siatką zdjęć” i sześciany maleją wg Zasięgu. Hover sześcianów (powiększenie) bez zmian — działa tylko nad nimi.

### Hover „do krawędzi kwadratu” (2026-11-19)

Prośba: sześcian po najechaniu myszą rośnie tak, by krawędzie przedniej ściany dotknęły wszystkich czterech krawędzi
kwadratu kraty, który ją otacza.
- Grupa „Zdjęcia w kwadratach”: kontrolka **Hover** (`zdjecia.hoverTryb`: „Powiększenie o procent” `procent` — dawne,
  domyślne / „Do krawędzi kwadratu” `kwadrat`). W trybie `kwadrat` wzrost = padding z każdej strony × postęp hover
  (czasy jak dotąd: „Czas powiększenia” / „Czas powrotu”), sześcian rośnie symetrycznie, głębokość rośnie razem ze
  ścianą; sąsiedzi się nie kurczą. „Powiększenie na hover” (%) jest wtedy ukryte.
- Na `/` (`OirTRcAEZ`) ustawione `kwadrat` (padding zdjęć 12 px — o tyle rośnie każdy bok). Sprawdzone pośrednio:
  zrzut z paddingiem 0 (= stan po pełnym najechaniu) — przednie ściany leżą dokładnie na liniach; padding przywrócony.

## Druga strona `/home-2` i Siatka perspektywy (zauważone 2026-11-17)

- Projekt ma drugą stronę `OvsvNzCvS` (nazwa w panelu też „Home”, ścieżka `/home-2` — użytkownik
  zmienił ją 2026-11-17 z `/home`). Breakpointy: Desktop `KMqqOEmhj`, Tablet `OYwlXyB0T`, Phone `cq2IA_2QC`.
- Na obu stronach jest tło **Siatka perspektywy** — komponent kodowy `SiatkaPerspektywy.tsx`
  (instancje: `/` → `OirTRcAEZ`, `/home-2` → `GCcSRW8rC`; absolutnie, 100% × 100%, pod treścią).
- 2026-11-17 — na prośbę użytkownika ustawienia siatki skopiowane z `/` do `/home-2` (obie są teraz
  identyczne, wartości domyślne komponentu). Poprzednie ustawienia `/home-2`, gdyby trzeba było wrócić:
  horyzont 0,35, punktZbiegu 0,33, wielkość sześcianu 460, głębia 0,32, dół (below) krycie 0,8 /
  poziomy 1, miękkość zaniku 1, przerwy 1, długość światła 20, prędkość 115, rozświetlenie 0,3
  (reszta jak domyślne).

### Logo NUMINO z sześcianów (od 2026-11-17)

- Na canvasie strony `/home-2` (luzem, poza breakpointami) leży oryginał **„Logo NUMINO”** `c7tBzcDUX`
  (biała ramka 811×304, maska SVG z logotypem, krycie 41%) — **nie ruszany**.
- Pod nim jest nowa wersja 3D **„Logo NUMINO 3D”** `bSQ2TfYUa` — komponent kodowy `LogoSzesciany.tsx`
  (WebGL): z tej samej ścieżki SVG budowana jest bryła z sześcianów. Zasady (poprawka użytkownika 2026-11-17):
  - **lica kostek stoją frontem do kamery** (obrót 0°, pochylenie 0°, bez kołysania i przeciągania —
    te opcje są w kontrolkach, ale domyślnie wyłączone); głębię widać przez lekką perspektywę i cień;
  - **ciemne miejsca oryginału = głębia**, nie brak kostek: rysy i plamy wewnątrz kresek to zagłębienia
    (kostki cofnięte o 3–4 warstwy i przyciemnione kolorem „Kolor głębi”); puste zostają tylko duże
    zamknięte prześwity liter (np. środek „o”);
  - **żadnych samotnych kostek**: tylna ściana każdej litery jest pełna i płaska, a kawałki niepołączone
    ścianami z resztą (mniejsze niż ~24 kostki) są usuwane;
  - domyślnie 220 kostek szerokości (82 wysokości), głębokość 8, fazowanie krawędzi 1, głębia rowków 4.
- Kolory ścian (kontrolki): przód `#E6ECF2` (kolor logotypu), głębia `#2E343B` (cień 0,85), góra `#FFFFFF`,
  bok lewy `#A9B2BC`, bok prawy `#76808B`, spód `#4A525B`; delikatne fugi i lekki losowy odcień kostek.
- Bez WebGL pokazuje się płaskie logo SVG. Użytkownik przesunął/powiększył instancję (899×337).
- Instancja ma krycie 100% (oryginał 41%) — żeby było widać cieniowanie ścian; do decyzji użytkownika.

### Logo 3D w przestrzeni Siatki perspektywy (`/home-2`, od 2026-11-17)

- Komponent `SiatkaPerspektywy.tsx` ma grupę ustawień **„Logo 3D”** (`$control__logo`): Pokaż, **Poziomo / Pionowo**
  (w sześcianach siatki; 0 = oś punktu zbiegu / horyzont), **Głębia** (odległość od pierwszej warstwy linii
  w sześcianach: ujemna = przed liniami, dodatnia = za nimi), Szerokość (w sześcianach siatki), kostki, grubość,
  fazowanie, głębia rowków, kolory ścian, cień głębi, fugi, krycie. Domyślnie wyłączone (strona `/` bez zmian).
- Bryła to ten sam algorytm i ta sama ścieżka co `LogoSzesciany.tsx` (kod skopiowany do pliku siatki —
  zmiany algorytmu trzeba robić w obu plikach). Rysowana WebGL-em w tym samym rzucie perspektywicznym co siatka,
  frontem do kamery. Linie, świetliki i węzły bliższe kamerze niż środek bryły malują się **na** logo, dalsze **pod** nim —
  przesuwanie „Głębi” przeprowadza logo przed / za kolejne warstwy linii.
- Instancja na `/home-2` `GCcSRW8rC`: Desktop x 0, y 1,1, głębia 0,25 (tuż za pierwszą warstwą), szerokość 3,64;
  Tablet y 1,54, szer. 3,75; Phone y 2,96, szer. 0,32, 100 kostek — dobrane tak, by pokrywało się z dawnym płaskim
  logo (na ekranach o innej wysokości może się lekko przesunąć, bo jest zakotwiczone w punkcie zbiegu).
- Kolory szare (`#6F7176` przód …), jak dawne płaskie logo (biel z kryciem 41% na tle) — zmienione 2026-11-17, patrz niżej.
- **Dopracowanie bryły i światła** (2026-11-17, prośba: mniej przypadkowo poszarpane krawędzie, więcej uzasadnionej głębi,
  światłocień, kontrast, białe rozjaśnienia). Zmiany tylko w `SiatkaPerspektywy.tsx` — `LogoSzesciany.tsx` (osobna instancja
  `bSQ2TfYUa`) ma jeszcze starszy algorytm:
  - **Wygładzanie** (kontrolka, 1,2): raster logo jest rozmywany przed progowaniem, sylwetka bryły też — znikają schodki
    i pojedyncze zadziory; drobne jasne drobiny w rowkach i drobne ciemne plamki w licu są usuwane. Wyraźne rysy zostają;
  - **głębia z formy**: tarasowe fazowanie (2 stopnie) — krawędzie każdej kreski schodzą w głąb, więc masywne partie liter
    wysuwają się do przodu, a cienkie rysy są cofnięte; grubość bryły 12 kostek (było 8); boki ciemnieją płynnie w głąb;
  - **światłocień**: światło kierunkowe (Światło X/Y, domyślnie z prawej u góry — od strony jaśniejszej części sceny)
    + plama światła na bryle + okluzja w rowkach i przy stopniach; kontrolki Światłocień 0,7, Kontrast 1,2;
  - **Blask** (0,85, kolor `#FFFFFF`): białe linie na krawędziach grzbietów zwróconych do światła, najmocniej na najbardziej
    wysuniętych partiach; krawędzie po przeciwnej stronie leżą w cieniu; lekki połysk na bokach od strony światła;
  - nowe kolory: przód `#8A8E94`, góra `#E8EBEF`, bok lewy `#5C6066`, bok prawy `#3A3D42`, spód `#202226`, głębia `#0E1012`,
    fugi 0,15 — ustawione na wszystkich trzech breakpointach (położenie i rozmiar bez zmian).
- Położenie na Desktop zmienione ręcznie przez użytkownika (stan 2026-11-17): x −1,62, y 2,36, głębia 0,92, szerokość 2,37
  (logo w lewym górnym rogu).
- **Głębia przestrzeni** (2026-11-17, prośba: logo ma wyglądać na umieszczone w przestrzeni, nie na samym przodzie):
  - grupa **„Bliskie linie”** (`$control__near`): linie poziome i pionowe najbliżej kamery dostają dodatkowe białe,
    nieco grubsze pociągnięcie, wygasające w głąb (Jasność, Zasięg w sześcianach, Kolor, Grubość, „Też w głąb” dla linii
    zbiegających). Na `/home-2`: jasność 0,9, zasięg 1,5, grubość 1,25; na `/` wyłączone (0);
  - w „Logo 3D” doszła **Mgła głębi** (0,5 na `/home-2`) i Kolor mgły (`#0B0D10`, tło): logo ciemnieje z głębią
    tak samo, jak przygasają linie na tej głębokości — przesunięte dalej „tonie” w przestrzeni.
- Dawne płaskie logo `CjoBJZxs7` zostało, ale jego kontener „inside” `l5LKpFaTq` jest ukryty (żeby nie dublować).

### „Tajemnica” w Siatce perspektywy (2026-11-17)

Prośba: linie wyglądały za regularnie — jak kratka, a nie tajemnicza przestrzeń. W `SiatkaPerspektywy.tsx` doszła grupa
**„Tajemnica”** (`$control__mystery`): **Rzadkość** (odcinki między węzłami nierówno przygasają, każdy z własnym, powoli
„oddychającym” progiem — nigdy nie znikają twardo, bo pełne wycięcia dawały geometryczny „labirynt”), **Oddech** (tempo),
**Nierówność** (różnice jasności linii; 0,4 = dawne zachowanie), **Mrok** + Światło X/Y + Zasięg światła (plama światła,
poza nią linie toną w ciemności). Działa też na rozjaśnione bliskie linie, świetliki i węzły. Na `/` wyłączone.
- Poprawka (2026-11-17, uwagi użytkownika: część linii za jasna, części brak, „krzyże”, linie kończą się na przecięciach):
  przy Rzadkości > 0 przygaszanie to **gładki szum wzdłuż linii, niezależny od węzłów** (fragmenty zaczynają się i kończą
  w dowolnym miejscu i powoli wędrują) — zastępuje wtedy „ramiona” od przecięć z Przerw. **Przerwy** ustalają głębokość
  przygaszenia (przy 0,75 linia nie spada poniżej ~30%), więc żadna nie znika. Na `/` (Rzadkość 0) bez zmian.
- Na `/home-2`: rzadkość 0,62, oddech 0,15, nierówność 0,35, mrok 0,65, światło (0,5; 0,55), zasięg 0,8;
  bliskie linie jasność 0,7. Przerwy zostały na wartości użytkownika (0,75).

### „Kosmos” w Siatce perspektywy (2026-11-17)

Uwaga użytkownika: siatka nadal wyglądała regularnie („jak więzienie z sześcianów”); ma przypominać przestrzeń kosmiczną —
referencja: nagranie ekranu (strona z przestrzenią z rozproszonych linii, pyłem i lotem kamery).
- W `SiatkaPerspektywy.tsx` grupa **„Kosmos”** (`$control__kosmos`): Włącz, Odcinki (liczba), Długość (średnia, w sześcianach),
  Głębia (jak daleko sięgają, w sześcianach — zastępuje wtedy „Głębię” siatki), Pył (liczba punktów), Dryf (ruch ku widzowi,
  sześciany/s), Kolor pyłu. Zamiast pełnej kraty: rozproszone odcinki na osiach tej samej przestrzeni (poziome, pionowe
  i biegnące w głąb), na różnych głębokościach (więcej w głębi), z miękkimi końcami w dowolnym miejscu + migoczący pył.
  Odcinki i pył biorą udział w warstwach głębi (logo i Wnętrze 3D chowają się za bliższymi, wychodzą przed dalsze),
  w mroku/plamie światła i rozjaśnieniu bliskich linii. Szum „Tajemnicy” nie dotyczy odcinków Kosmosu.
- Na `/home-2` włączone: odcinki 380, długość 1, głębia 14, pył 600. Na `/` wyłączone.
- Poprawka (2026-11-17): użytkownik **nie chce ruchu przestrzeni** → dryf 0 i Oddech „Tajemnicy” 0 (wzór nieruchomy;
  świetliki i migotanie pyłu zostają). Ma być widoczny **lekki zarys dawnej kraty** → nowe ustawienie **Zarys siatki**
  (krycie regularnej kraty pod odcinkami; krata ma wtedy swoją dawną głębię z „Głębi” siatki). Na `/home-2`: 0,35.
- Poprawka (2026-11-17, uwagi: „linie w przypadkowych miejscach”, „z przodu za dużo linii ciągłych na całej długości”):
  odcinki poziome i pionowe Kosmosu leżą teraz **na płaszczyznach kraty** (pokrywają się z jej zarysem; odcinki w głąb
  już leżały na liniach kraty); w trybie Kosmos zarys kraty **rwie się głęboko** (przygaszone fragmenty prawie znikają,
  szum gęstszy — krótsze kawałki) i odcinki najbliżej kamery są krótsze.
- Użytkownik sam przesunął logo w siatce (x −1,62, y 2,36, głębia 0,92, szerokość 2,37) i zmienił Głębię siatki na 0,22 —
  zachowane.

### Wnętrze 3D w przestrzeni Siatki perspektywy (`/home-2`, od 2026-11-17)

- `Wnetrze3D.tsx` ma grupę **„Przestrzeń siatki”** (`$control__siatka`): W siatce (wł./wył.), Poziomo, **Podłoga**
  (wysokość podłogi w sześcianach siatki; −0,5 = linia siatki tuż pod horyzontem), **Głębia** (od pierwszej warstwy
  linii, w sześcianach) i **Skala** (sześciany siatki na 1 m sceny). Domyślnie wyłączone (strona `/` bez zmian).
- Jak to działa: Siatka rejestruje się w `window.__siatkaPerspektywy` (kamera: punkt zbiegu, ogniskowa, Z0) i ogłasza
  zmianę kamery zdarzeniem `siatka:kamera`. Wnętrze 3D w trybie siatki szuka siatki, która zawiera jego środek,
  liczy obraz tą samą kamerą (przesunięta kamera sceny, ta sama ogniskowa i punkt zbiegu — także w rendererze WebGL2
  brył po „Pokaż”), ukrywa własny canvas, a siatka wkleja go między swoje linie na głębokości sceny (jak logo 3D).
  Siatka sortuje wszystkie wklejki (logo, scena) od najdalszej; linie trafiają między nie wg głębokości.
- Na `/home-2` instancja Wnętrza `rUoK2HVYm`: szerokość 100% (wcześniej 544 px, żeby scena nie była przycinana),
  W siatce: x 0, podłoga −0,5, głębia 1,5 (między 2. a 3. warstwą linii, za logo), skala 0,106 (bryły mają
  podobną wielkość jak wcześniej). Przeciąganie, przyciski i „Pokaż” działają jak dotąd.
- Zrzuty ekranu Framera (API) nie pokazują spadających brył ani podglądu kształtu — weryfikacja była lokalna
  (Chromium, układ i ustawienia jak na `/home-2`).

### Strona `/home-3` (zauważona 2026-11-17)

- Strona `JIxLbBZCp` (w panelu „Home”, ścieżka `/home-3`, **wersja robocza**). Breakpointy: Desktop `OJAJqh788`,
  Tablet `J3MEdxCTe`, Phone `mLh3ZbMvh`. Siatka perspektywy `GA3zheMSK` (w „Ekran” `feQNStWcD`), płaskie logo NUMINO.
- 2026-11-17 — użytkownik: tryb „Kosmos” na `/home-2` „poszedł w złą stronę”; wzorcem jest siatka z `/home-3`,
  tylko lekko dopracowana — „odrobinę więcej nieregularności linii”. Zmienione wyłącznie `GA3zheMSK`: Przerwy 0,5 → 0,6,
  Tajemnica: Nierówność 0,4 → 0,7, Mrok 0,25 (środek 0,5/0,5, zasięg 1,0); Rzadkość 0 (ramiona przy przecięciach
  zostają jak były), Kosmos wył. `/home-2` bez zmian (nadal Kosmos) — do decyzji, czy przenieść tam ustawienia z `/home-3`.
- Użytkownik sam zmienił na `/home-3`: Wielkość sześcianu 40 (gęsta krata), nawigacja i panel ukryte.
- 2026-11-17 — wg zrzutu-makiety użytkownika: pod logo **rozświetlony fragment kraty** + **przycisk ze strzałką**;
  świetliki na skrzyżowaniach za mocne; linie ku narożnikom mniej widoczne:
  - `SiatkaPerspektywy.tsx`: nowa grupa **„Rozświetlenie”** (`$control__area`): Włącz, Środek X/Y (ułamek ekranu),
    Szerokość/Wysokość (px), Miękkość, Siła, Światełka (na skrzyżowaniach), Rozmiar światełek, Kolor. Rozjaśnia linie
    najbliższej warstwy kraty; poziome wygasają w poziomie, pionowe długo w dół i krótko w górę. Na `/` i `/home-2` wył.
  - `/home-3` (`GA3zheMSK`): Rozświetlenie x 0,5, y 0,72, 130×85 px, miękkość 45, siła 0,85, światełka 0,35/7 px
    (Phone: 90×70, miękkość 28, siła 0,7); Świetliki w węzłach: jasność 0,45, wielkość 7, światło na liniach 16;
    Tajemnica: mrok 0,6, zasięg światła 0,9 (narożniki ciemniejsze).
  - Nowy komponent **„Przycisk strzałka”** `s__oFNsWK` (natywny): okrąg 56 px, tło `rgba(11,13,16,0.55)` + rozmycie 6 px,
    obrys 1 px `rgba(230,236,242,0.35)`, ikona Phosphor „Arrow Right” 22 px w kolorze „Tekst”; warianty Hover
    (tło „Tekst”, ikona „Tło”) i Pressed; zmienna **Link** (do ustawienia na instancji — na razie pusty), aria-label „Dalej”.
    Zainstalowany zestaw ikon Phosphor.
  - Instancja `GuSFfl6t4` na `/home-3` w przezroczystej warstwie **„Warstwa przycisku”** `dlU8WW7D7` (absolutnie na całe
    „Ekran”, bez przechwytywania kliknięć) — wyśrodkowana w poziomie, w pionie odstępy 74fr/26fr (≈ 72% wysokości,
    tak jak środek Rozświetlenia).
  - **Cofnięte tego samego dnia na prośbę użytkownika:** Rozświetlenie wyłączone na `/home-3` (kod grupy w komponencie
    został, domyślnie wył.), przycisk, jego warstwa i komponent „Przycisk strzałka” usunięte (zestaw ikon Phosphor
    został zainstalowany). Słabsze świetliki i ciemniejsze narożniki zostają.
- 2026-11-17 — świetliki za mocne / za długo i za dużo (`/home-3`, `GA3zheMSK`): Świetliki w węzłach: liczba 8 → 5,
  jasność 0,45 → 0,2, wielkość 7 → 5, światło na liniach 16 → 6; świetliki podróżujące: poziome 6 → 3, pionowe 4 → 2,
  w głąb 6 → 3, Dystans biegu 0,55 → 0,22 (gasną wcześniej), Czas gaśnięcia 1,2 → 0,7 s.

## Jak to działa (kod)

- `Wnetrze3D.tsx` — własny renderer linii na `<canvas>` (bez bibliotek): perspektywa, przycinanie
  linii za kamerą, fizyka spadania, „mgła” (dalsze linie gasną w ciemności), oświetlenie snopem.
  Kontrolki: kolory (tło, linie, bryły, przecięcia, światło), mrok (0,72), rozpad (0,6),
  zniekształcenie (1), limit brył (10), grubość, wymiary sali (domyślnie 44 × 72 m, wys. 16 m), wys. oczu (2,6 m),
  przejście do kolejnej sali (wył. — usunięte na prośbę użytkownika), mgła (0,55), siatka podłogi (wył.), czułość kursora, dryf,
  limit brył, „Podgląd brył” (tylko w edytorze, pokazuje 3 przykładowe bryły).
- Kamera stoi na osi sali ok. 1 szerokość sali od tylnej ściany, kąt widzenia ~70° w poziomie.
  Bryły mają stały rzeczywisty rozmiar (~2 m, niezależny od wielkości sali — tak większa sala
  wygląda na większą) i spadają w strefie od ~40% odległości do tylnej ściany.
- `ShapeButtons.tsx` — code overrides na przyciskach: `withKolo`, `withKwadrat`, `withGlaz`
  oraz gotowy `withWyczysc` (czyści wnętrze, jeszcze nie podpięty). Komunikacja przez zdarzenie
  okna `wnetrze3d:bryla` z `detail: { type: "add", shape: "kolo" | "kwadrat" | "glaz" }`
  lub `{ type: "clear" }` — nowy przycisk = override wysyłający to zdarzenie.
- Przyciski działają tylko w podglądzie / na opublikowanej stronie (nie na canvasie edytora).

## Design system

- Kolory (folder Assets → Kolory): Tło, Powierzchnia `#15181C`, Obrys, Tekst, Tekst drugorzędny, Akcent.
- Tekst (PP Neue Montreal): Znak (17/600), Etykieta (14/400), Podpis (13/400, kolor drugorzędny),
  Nagłówek (h1, 300; 64/42/32 px dla Desktop/Tablet/Phone, interlinia 1,05), Podpis akcent (15/400, Akcent).
- Komponent **Przycisk akcji** `HAR1CjvV6`: warianty Główny (jasny) / Drugorzędny + hover i pressed,
  zmienna „Etykieta”. Preset tekstu „Etykieta akcji” (14/600, kolor Tło).
- Komponent **Przycisk bryły** `IhvcEuszi` (od 2026-11-16 bez etykiety, okrągły, ikona 26 px, `ariaLabel`
  „Dodaj koło/kwadrat/…”; doszły warianty Trójkąt `NSLD_xhk7` i Walec `BkiYV_4M6` z hover/pressed): warianty Koło / Kwadrat / Głaz (różnią się ikoną SVG
  i etykietą) + warianty hover i pressed dla każdego.

## Ustalenia i decyzje

- 2026-11-15 — scena 3D jako komponent kodowy (canvas 2D, własna projekcja) — interaktywna grafika
  3D z fizyką nie da się zrobić natywnie we Framerze; bez zewnętrznych bibliotek = lekko i stabilnie.
- 2026-11-15 — przyciski zostają na canvasie (edytowalne), a do sceny mówią przez code overrides
  i zdarzenie okna — pasek można dowolnie przebudowywać bez ruszania kodu.
- 2026-11-15 — zmiana kamery i proporcji (galeria jak na zdjęciu użytkownika): centralnie,
  wzrok na wprost, sala szeroka i niższa (24 × 40 × 7 m) z przejściem w głąb, mgła głębi,
  słabszy i bezwładny ruch kursorem — dla klimatu liminalnego i monumentalnego.
- 2026-11-15 — przejście (wgłębienie) w tylnej ścianie usunięte na prośbę użytkownika — tylna
  ściana jest pełna. Kontrolka „Przejście” zostaje w komponencie, domyślnie wyłączona.
- 2026-11-15 — sala powiększona do 44 × 72 × 16 m (prośba: większa, bardziej monumentalna);
  wysokość oczu bez zmian (2,6 m), więc sufit i ściana górują nad widzem, a bryły ~2 m wyglądają
  na małe względem przestrzeni.
- 2026-11-15 — bryły abstrakcyjne i losowe, dematerializujące się, przecinające i zniekształcające
  się nawzajem; scena oświetlona jednym snopem światła ze świetlika (mocny kontrast światło/mrok);
  bryły jasne, akcent tylko na szwach przecięć — na prośbę użytkownika („całkowicie inne”).
- 2026-11-15 — limit 3 brył i przycisk „Nadaj kształt” scalający je w jeden obiekt z fakturami
  (zacieki rdzy / granit / warstwice wg zdjęć-inspiracji); dodany „Od nowa”; usunięta „klatka”
  snopa światła, zostały promienie — na prośbę użytkownika.
- 2026-11-16 — „Koło” ma bardziej przypominać koło: zawsze geoida z lekkimi wybrzuszeniami
  i wklęsłościami zamiast losowych abstrakcyjnych wariantów.
- 2026-11-16 — żadnych linii przerywanych w bryłach (krawędzie, faktury, obrys lądowania ciągłe).
- 2026-11-16 — pierwsza bryła odkształca się dołem przy uderzeniu; druga i trzecia wbijają się
  w pierwszą (bez kontaktu z podłogą), lekko poza jej środkiem — na prośbę użytkownika.
- 2026-11-16 — obrót tylko wokół osi pionowej, obiekt przytwierdzony do ziemi, dużo wolniej
  (nagranie użytkownika pokazało przechył i odrywanie się od ziemi).
- 2026-11-16 — kształty mają przypominać nazwy (Kwadrat = sześcian, Głaz = kamień, Koło = geoida);
  linia ziemi niżej; obiekt powoli się obraca, reaguje na kursor, obrót przeciąganiem.
- 2026-11-16 — zrzut z 1/3, 2/3 i 3/3 wysokości dla kolejnych brył.
- 2026-11-16 — tylne linie brył ciemniejsze i mniej widoczne (przygaszanie wg głębokości).
- 2026-11-16 — druga bryła w losową połowę (lewą/prawą) pierwszej, trzecia w przeciwną — żeby nie
  spadały jedna nad drugą w tym samym miejscu.
- 2026-11-16 — układ: tekst w lewej połowie, scena 3D w prawej (wg screena-inspiracji); na telefonie tekst nad sceną.
- 2026-11-16 — przyciski brył tylko z ikoną (większą), dwa nowe kształty (Trójkąt, Walec), licznik 0/3–3/3,
  „Nadaj kształt” → „Pokaż”, logotyp NUMINO zamiast „Kubatura” — na prośbę użytkownika.
- 2026-11-17 — logo NUMINO w wersji 3D z sześcianów jako komponent kodowy (WebGL), a nie statyczny obrazek:
  bryła jest prawdziwie trójwymiarowa, a gęstość kostek, głębokość i kolory ścian są kontrolkami;
  oryginał zostaje obok do porównania.
- 2026-11-17 — poprawka logo 3D: kostki frontem do kamery, ciemne miejsca jako zacienione zagłębienia
  (a nie dziury), wszystkie kostki przylegają (pełny tył, usunięte oderwane drobiny) — na prośbę użytkownika.
- 2026-11-17 — logo z sześcianów osadzone w komponencie Siatka perspektywy (wspólna przestrzeń 3D i perspektywa),
  a nie jako osobna warstwa nad nim — tylko tak linie mogą zasłaniać logo albo być przez nie zasłaniane zależnie od głębi.
- 2026-11-17 — rozjaśnione najbliższe linie siatki + mgła głębi na logo, żeby logo czytało się jako obiekt w przestrzeni
  za pierwszą warstwą linii (wcześniej wyglądało, jakby było na samym przodzie).
- 2026-11-17 — Wnętrze 3D osadzone we wspólnej przestrzeni z Siatką perspektywy (wspólna kamera + wklejanie obrazu
  sceny między linie siatki), zamiast scalać dwa duże komponenty w jeden — każdy zostaje osobno edytowalny.
- 2026-11-17 — logo 3D w siatce: głębia wynika z formy (tarasowe fazowanie — masywne partie wysunięte), światło kierunkowe
  z blaskiem na krawędziach zamiast płaskich kolorów ścian, obrys wygładzany — na prośbę użytkownika (mniej przypadkowo
  poszarpane, więcej światłocienia i bieli). Zmiana tylko w siatce; `LogoSzesciany.tsx` celowo nieruszany.
- 2026-11-17 — tryb „Kosmos” w siatce (rozproszone odcinki + pył + dryf) zamiast pełnej kraty — na prośbę użytkownika
  (referencja: nagranie z przestrzenią „kosmiczną”); krata zostaje dostępna (Kosmos wył.).
- 2026-11-17 — sekcja „Pasy zdjęć” jako natywny komponent z wariantami (po jednym na rozwinięty pas) przełączanymi
  na najechanie — wymóg użytkownika: natywne funkcje Framera; rozwinięcie przez `2fr` utrzymuje sekcję na 100vh.
- 2026-11-17 — efekt scrolla pierwszej sekcji w kodzie siatki (kontrolka), bo natywne efekty scrolla Framera
  nie mogą animować właściwości komponentu kodowego. Najpierw horyzont uciekał w górę; użytkownik wolał
  przybliżanie sześcianów (krata jedzie ku kamerze), więc kontrolka „Ucieczka” zastąpiona „Zbliżeniem”.
- 2026-11-18 — zdjęcia na kwadratach kraty rysowane w komponencie siatki (wklejka na głębokości warstwy), a nie jako
  warstwy Framera nad nią — tylko tak leżą w perspektywie, linie je kadrują i jadą z kratą przy scrollu.
- 2026-11-19 — wzmocnienie kresek wokół sześcianów jako osobna grupa kontrolek-dodatków w siatce (nie zmiana
  globalnych „Linii”): na 0 wygląd bez zmian, a reszta kraty zostaje delikatna.
- 2026-11-19 — zmniejszanie sześcianów od kursora liczone domyślnie od kwadratu każdego sześcianu (efekt „soczewki”
  pod kursorem); wariant od całej siatki 3×3 dostępny przełącznikiem „Odległość od”.
- 2026-11-15 — nazwa robocza w nawigacji „Kubatura” (do potwierdzenia/zmiany przez użytkownika).
- 2026-11-20 — tło Hero na `/`: wariant G z 7 propozycji (poświata + rzadkie gwiazdy + lekkie ziarno + winieta).
  Poświata i winieta natywnie (gradienty, edytowalne w panelu), gwiazdy i ziarno w Siatce perspektywy — tylko tak
  gwiazdy mogą mieć paralaksę przy „Zbliżeniu (scroll)” i leżeć pod liniami. Bez dryfu przestrzeni (uwaga z 17.11).

## Do zrobienia

- [ ] Sprawdzić w podglądzie hover „Do krawędzi kwadratu” razem ze zmniejszaniem od kursora.
- [ ] Sprawdzić w podglądzie zmniejszanie sześcianów przy kursorze nad paskiem nawigacji („Także nad siatką” 80 px).
- [ ] Tło Hero (wariant G): obejrzeć w podglądzie mruganie gwiazd, ziarno i paralaksę przy scrollu; ewentualnie dostroić
      jasność gwiazd / siłę ziarna / krycie winiety.
- [ ] Tablet `/`: przycisk „View all” nachodzi na dolny rząd zdjęć (widoczne na zrzucie 2026-11-20, niezwiązane z tłem).
- [ ] Sprawdzić w podglądzie „Zmniejszanie od kursora” (0,15 / 600 px) i ewentualnie dostroić; potwierdzić, czy
      odległość ma być od kwadratu każdego sześcianu, czy od całej siatki zdjęć.
- [ ] Film w kwadracie siatki na `/`: uzupełnić „Opis filmu (alt)” (teraz roboczy) i sprawdzić odtwarzanie w podglądzie.
- [ ] „Pasy zdjęć” na `/`: podmienić zdjęcia w pasach 3 i 4 (oraz ewentualnie 1–2), gdy użytkownik je podeśle.
- [ ] Sprawdzić w podglądzie Framera rozwijanie pasów i przybliżanie kraty przy scrollu (z poziomu AI widać tylko
      statyczne zrzuty); ewentualnie dostroić tempo (spring 0,7 s) i siłę „Zbliżenia” (teraz 3 sześciany).
- [ ] Podpis pod nagłówkiem „Kubatura — nadaj kształt” odwołuje się do starej nazwy i starego przycisku —
      zapytać, czy zmienić (np. na „NUMINO”).
- [ ] Logotyp jako SVG nie ma tekstu alternatywnego (Framer nie pozwala dać `ariaLabel` na SVG) — rozważyć
      opakowanie w ramkę z etykietą/linkiem do strony głównej.

- [ ] Zaakceptować/zmienić tekst nagłówka i podpisu po lewej (robocze).
- [ ] Wskazówka w nawigacji „Poruszaj kursorem, aby się rozejrzeć” jest nieaktualna (kamera stoi,
      obiekt obraca się przeciąganiem) — zaproponować np. „Przeciągnij, aby obrócić”.

- [ ] Logo 3D (`bSQ2TfYUa`): zaakceptować wygląd (głębokość zagłębień, perspektywa, kolory), zdecydować o kryciu
      (100% vs 41% jak oryginał) i czy/gdzie ma zastąpić płaskie logo (np. w nawigacji) oraz czy usunąć oryginał.
- [ ] Logo w siatce (`/home-2`): obejrzeć nowe światło i blask w podglądzie; ewentualnie dostroić Światło X/Y, Blask,
      Wygładzanie. Zdecydować, czy przenieść nowy algorytm do `LogoSzesciany.tsx`.
- [ ] Na Tablet logo w siatce (szer. 3,75) dotyka lewej krawędzi ekranu — do decyzji, czy zmniejszyć.
- [ ] Logo w siatce (`/home-2`): zaakceptować głębię/położenie; zdecydować, czy usunąć ukryte płaskie
      logo `CjoBJZxs7` i osobną instancję `bSQ2TfYUa` z canvasu.
- [ ] Wnętrze 3D w siatce (`/home-2`): sprawdzić w podglądzie Framera (spadanie, „Pokaż”, przeciąganie) i ustawić
      położenie/głębię/skalę wg uznania; na telefonie scena jest w innym układzie — do obejrzenia.
- [ ] Potwierdzić, czy zostaje przycisk „Od nowa” (dodany z własnej inicjatywy).
- [ ] Inspiracje od użytkownika (2026-11-15) jeszcze niewykorzystane w pełni: wklęsła czerwona
      połówka dysku, kamienie rozsypane na podłodze, kilka długich świetlików, skośne słupy.

- [ ] Potwierdzić nazwę w nawigacji („Kubatura” jest robocza) i ewentualne linki w nawigacji.
- [ ] Kolejne przyciski w dolnym pasku (np. „Wyczyść” — override `withWyczysc` jest gotowy).
- [ ] Sprawdzić działanie w podglądzie Framera (kliknięcia, ruch kursora) — z poziomu AI widać
      tylko statyczne screenshoty.

## „View all” → czarna dziura → strona `/all` (2026-11-19)

Prośba: po kliknięciu „View all” grid ze wszystkimi sześcianami wsysany do punktu zbiegu jak do czarnej dziury, potem
przejście na osobną stronę, która wysuwa się spod paska (wejście natywne). Decyzje użytkownika: nowa prosta strona,
wspólny szablon z paskiem, listy po bokach gasną razem z siatką, czas ok. 1,6 s.
- **Efekt w `SiatkaPerspektywy.tsx`**, grupa kontrolek **„Wsysanie”** (`wchlon`): Czas (1,6 s), Przyspieszenie (2,2),
  Cel (Punkt zbiegu / Środek ekranu). Na zdarzenie `siatka:wchlon` gotowa klatka jest kopiowana do bufora i rysowana
  **jednolicie zmniejszona wokół Punktu zbiegu** (jedna skala dla całości), pod koniec wygaszenie. Linie pionowe i poziome
  **nie mogą się odkształcać** (wymóg użytkownika) — dlatego bez pierścieni o różnej skali. Po końcu płótno puste i zdarzenie
  `siatka:wchloniete`. Czas siatka odpisuje w `detail.czas`. `siatka:wchlon-reset` cofa stan. Tylko w podglądzie/na
  stronie; przy ograniczonym ruchu od razu przejście. Na `/` Punkt zbiegu jest przy dolnej krawędzi siatki, więc wszystko
  spływa w dół, pod przycisk „View all” (użytkownik chce właśnie Punkt zbiegu, nie środek ekranu).
  Historia (2026-11-19): 1. wir + ciemne jądro + pierścień (usunięte), 2. pierścienie z „Zasysaniem” (wyginały linie —
  usunięte), 3. obecne jednolite zmniejszenie.
- **Overrides `Wchloniecie.tsx`:** `withWchlonPrzycisk` na „Przycisk View all” `i02ZAUNY5` (natywny link `/all`, htmlTag
  zmieniony z button na div): 1. klik → blokuje link, odpala wsysanie, przycisk gaśnie; po `siatka:wchloniete`
  (zapas: czas + 0,5 s) klika ten sam link ponownie → natywne przejście Framera. `withWchlonGasnie` na „Column Left”
  `AzgVkCy4j` i „Column Right X” `Hgbr5CLZ2` (gasną w 70% czasu).
- **Strona `/all`** `tpDgLHnBl` (Desktop `X9KoqFTlm`, Tablet `r5gZV8E0r`, Phone `eGuLwUNZK`): sekcja „Treść” `JapIuASkU`
  (padding 200/40/80, Phone 160/20/60), tytuł „All work” (preset „Nagłówek”), „The full list is coming soon.” (preset
  „Lista”) — **TODO: docelowa treść**.
- **Szablon „Układ z paskiem”** `cZLu0HAKR` (Desktop `AR663N1bM`, Tablet `Q1u0GgNMy`, Phone `bTOyeNkOf`, wys. 800 px,
  tło token jak Home): Navi `tbRDiBXr1` absolutnie na górze (80 px, Phone 56 px, warianty jak na Home), pod nim
  placeholder. Na razie **tylko `/all`** go używa.
- **Efekt wejścia** (Home Desktop `pageEffects` → `/all`): wejście z y −100% → 0, tween 0,9 s ease [0.16, 1, 0.3, 1]
  (strona zjeżdża z góry).
- **Otwarte:** żeby pasek stał w miejscu podczas przejścia, Home też musi używać szablonu (usunąć lokalny Navi
  `KQifDlO5e`), a w panelu Framera trzeba wyłączyć pasek z efektu przejścia (opcja dostępna tylko w UI; nie udało się
  potwierdzić w dokumentacji — framer.com zablokowany w sieci sesji). Czeka na zgodę użytkownika.

## Tło Hero na `/` — wariant G (2026-11-20)

Prośba: delikatny, minimalistyczny efekt tła pod Siatką perspektywy, dodający głębi. Claude pokazał 7 wariantów na
stronie porównawczej (artefakt „Tło Hero NUMINO”: poświata, gwiazdy, pył, ziarno, mgła, świt na horyzoncie,
połączenie); użytkownik wybrał **G — połączenie**. Warstwy w „Hero” `N06uDCvcg` (od dołu):
- **„Tło — poświata”** `iYBKmeeMR` — ramka absolutna na całą sekcję (przed Siatką), `pointerEvents: none`, gradient
  radialny `64% 90% at 50% 55%`: `rgba(86,104,132,0.16)` → `rgba(60,72,92,0.072)` 45% → 0. Chłodna jasność za sześcianami.
- **Siatka perspektywy** `OirTRcAEZ` — nowe grupy kontrolek (na końcu panelu, przed „Tło”), domyślnie wył.:
  - **„Gwiazdy”** (`gwiazdy`): Włącz, Liczba (190 — na ekran ~1200 × 800, większe dostają proporcjonalnie więcej; pula
    3 × liczba), Jasność (1,1), Wielkość (1; punkty 0,4–1,3 px), Tempo mrugania (1; każda gwiazda 3–9 s), Skupienie
    (1 = gęściej przy środku), Z poświatą (0,035), Kolor (`#E2EAF4`), Paralaksa (scroll) (1: przy „Zbliżeniu (scroll)”
    gwiazdy przybliżają się wokół punktu zbiegu o 6% na sześcian zbliżenia — dużo wolniej niż krata).
  - **„Ziarno”** (`ziarno`): Włącz, Siła (0,035), Tempo (12 kl/s), Wielkość ziarna (1 px).
  - Rysowane w `paintTlo` na początku `draw` (zaraz po wyliczeniu punktu zbiegu), więc linie, zdjęcia i świetliki leżą
    na nich; „Wsysanie” wciąga je razem z kratą. W edytorze i przy ograniczonym ruchu — nieruchome.
  - Na `/` włączone z wartościami jak wyżej (Tablet/Phone dziedziczą); `/home-2`, `/home-3` bez zmian.
- **„Tło — winieta”** `QoQjkrz6V` — ramka absolutna zaraz **po** Siatce (nad liniami, pod kolumnami z tekstem),
  gradient `64% 90% at 50% 55%`: przezroczysty do 44% → `rgba(0,0,0,0.27)` na brzegach. Przyciemnia rogi kraty.
- Środek gradientów (50% / 55%) = środek siatki zdjęć na Desktopie; przy zmianie układu przesunąć oba.

## Strona `/home-4` — kopia Home z dolnym paskiem (2026-11-20)

- Kopia strony `/` na prośbę użytkownika: `rziApPjHh` „Home — dolny pasek”, ścieżka `/home-4`, **wersja robocza**
  (draft). Breakpointy: Desktop `aV1YbUb_x`, Tablet `bjqHDqeZA`, Phone `xxVYaW4J1`. `/` bez zmian.
- W „Hero” `gmcIlSWT9` nowy **„Dolny pasek”** `ddlZ2wN8D`: absolutnie na dole sekcji (left/right/bottom 0), **80 px**
  na wszystkich breakpointach, przezroczysty, obrys **górny** 1 px tokenem obrysu jak dolna kreska Navi (`G7JKeAILq`),
  stack poziomy space-between, padding boczny 40 px (Phone 16 px) jak w Navi, zIndex 1. **Na razie pusty — TODO: treść.**
- Żeby układ dalej się zgadzał (wszystko liczone od środka siatki, który przesunął się o 40 px w górę):
  - Siatka `TpFr32ewi`: przypięcie dolne 0 → **80 px** (dolna linia kraty = górna kreska paska);
  - Hero: padding dolny 0 → **80 px** (kolumny z listami zostają wyśrodkowane na siatce);
  - zdjęcie z hovera „Archer Magazine” (ramka absolutna `Cn0RQ_Nkx`): padding górny 80 → **0**;
  - „View all” `IE5BZ0Huu`: top 715 → **675 px**;
  - „Tło — poświata” `kke_N3CR2` i „Tło — winieta” `IEc6Oe2_x`: środek gradientów 50% / 55% → **50% / 50%**.
- Luźne warstwy z canvasu strony skopiowały się razem z nią; kopię „Tło — winieta” `rM1UIn9Mz` przesunięto na canvasie
  (left −2600), bo linter zgłaszał nakładanie się warstw.

## Font jak na studiofreight.com — Courier Prime (`/`, 2026-11-21)

Prośba: font na `/` „podobny do tego ze studiofreight.com”. Tam: **Publico Text Mono** (Commercial Type — szeryfowy
monospace, cały drobny tekst) + **J.Jannon** (szeryf, tylko duże hasło). Na `/` jest tylko drobny tekst, więc odpowiednik
Publico Text Mono z katalogu Framera: **Courier Prime** (400 / 700; brak 600 → nagłówki 700). Odstępy liter 0 (mono).
- Presety zmienione w miejscu (używane tylko na `/` i `/home-4`, więc **`/home-4` też zmieniła font**): „Lista nagłówek”
  `CNPDFVung` (700), „Lista akapit” `y2wkQleXW` (400), „navi” `FBNRC0So5` (był ABC Arizona Sans Condensed 300 → 400,
  wielkie litery bez zmian).
- „Lista” `dhBgkQbVl` jest też na `/all` → nie zmieniana; nowy preset **„Lista mono”** `f1IfIMiC6` (kopia „Listy”
  w Courier Prime) podpięty w komponentach „Wiersz listy” `ZIOR8bv28` i „Wiersz listy ze zdjęciem” `NeuI0X8QN`
  (oba tylko na `/` i `/home-4`).
- Tekst bez presetów: „View all” `g94uExZhx` i ukryty nagłówek `OU8yqIDhs` + ich nadpisania na Tablecie/Phone.
- Skutek: na Desktopie opis w prawej kolumnie („Images, motion and space”, kolumna 169 px) łamie się na 2 linie
  (mono jest szerszy). Zostawione; do decyzji użytkownika (mniejszy rozmiar / szersza kolumna).
- Cofnięcie: w presetach z powrotem PP Neue Montreal (600/400, odstęp −0,01em, cechy OT cv03/cv04/cv09/cv11/blwf),
  navi — ABC Arizona Sans Condensed 300; w komponentach wierszy z powrotem „Lista”.

## Niższy pasek nawigacji na Desktopie `/` — 56 px (2026-11-21)

Użytkownik zmienił w komponencie **Navi** `cAoTyKwTO` wariant Desktop `Pfq3SGMzj` z 80 na **56 px** (przyciski bez ramek).
Tablet `DCLYzClFb` nadal 80 px, Phone `JEtPeR5s6` 56 px (jak dawniej). Claude dopasował Desktop `/` (wszystko liczone
od dolnej kreski paska):
- Siatka `OirTRcAEZ`: przypięcie górne 80 → **56 px** (górna linia kraty = dolna kreska paska);
  „Także nad siatką” (`zdjecia.kursorNad`) 80 → **56**;
- Hero `N06uDCvcg`: padding górny 80 → **56 px** (kolumny z listami dalej wyśrodkowane na siatce);
- „Tło — poświata” `iYBKmeeMR` i „Tło — winieta” `QoQjkrz6V`: środek gradientów 55% → **53,5%**
  (środek siatki (56 + 800) / 2 = 428 px; rzędy przesunęły się o 12 px w górę);
- „Przycisk View all” `i02ZAUNY5`: top 715 → **703 px** (o 12 px w górę razem z rzędami). Uwaga: przycisk jest
  **ukryty** (`visible: false`, zmiana użytkownika) — pozycja poprawiona na wypadek ponownego włączenia.
- Tablet i Phone: te same właściwości **przypięte nadpisaniami do dawnych wartości** (siatka 80, padding 80, kursorNad 80,
  gradienty 55%, View all 715) — wygląd bez zmian.
- `/home-4`: instancja Navi `RQ8bBRkUD` ma wymuszoną wysokość 80 px → pasek tam się nie zmienił, układ bez zmian.
- Przy kolejnej zmianie wysokości paska zmienić razem: przypięcie siatki, kursorNad, padding Hero, środek gradientów,
  top „View all” (przesunięcie rzędów = połowa różnicy wysokości paska).

## Siatka zdjęć 4×4 na Desktopie `/` (2026-11-21)

Prośba: zamiast 3 rzędów po 3 sześciany — 4 rzędy po 4.
- Wcześniej (tego dnia) użytkownik sam zwiększył „Środek (łącznie)” 442 → **660 px** i dodał drugi pasek Navi na dole
  strony (`hFDkJFCJO`, absolutnie, bottom 0).
- **Kod** `SiatkaPerspektywy.tsx`: grupa „Grid” obsługuje teraz także **parzystą** liczbę „Kolumn w środku” (kontrolka
  krok 1 zamiast 2). Nieparzysta → środek ekranu w środku kolumny (jak dotąd, rysunek identyczny); parzysta → przez środek
  biegnie linia (`kN`, `kE` = 0,5 / 0, `kHi`, `kLo` zamiast dawnych `kM2`/`rM2`). Rzędy o stałej wysokości tak samo
  (wysokość rzędu = Środek / liczba kolumn). Siatka zdjęć N×N przy parzystym N: `j0 = jc + ceil((N−1)/2)` (wcześniej floor),
  to samo przy „Scal rzędy nad/pod”; „Bez linii ze środka” przy parzystym N pomija jedną linię w głąb ze skrzyżowania
  w środku (zamiast 4 z narożników środkowego kwadratu).
- **Desktop** (`OirTRcAEZ`): Grid → Kolumny w środku **4**; Zdjęcia → Kwadraty N×N **4**, **Powtarzaj wł.** (jest tylko
  9 zdjęć na 16 kwadratów — TODO: 7 nowych zdjęć od użytkownika); filmy w tych samych miejscach (wiersz, kolumna):
  film 5 → 6, film2 6 → 7, film3 4 → 5, film4 3 → 3. Środek 660 px bez zmian → kwadraty **165 px** (było 220).
- **Tablet i Phone**: zostają 3×3 (nadpisania: Kolumny w środku 3, N×N 3, Powtarzaj wył., filmy 5/6/4/3) — 4 kolumny
  nie mieszczą się tam w obecnej wielkości kwadratów. Do decyzji użytkownika.
- Do sprawdzenia przez użytkownika: listy po bokach mają nadal 442 px wysokości (nie 660) — są wyśrodkowane, ale nie
  wyrównane do rzędów; zdjęcie z hovera „Archer Magazine” liczone pod dawny środkowy rząd 3 × 147 px (przy 4×4 nie ma
  środkowego rzędu). Na zrzucie Phone dolny pasek Navi `hFDkJFCJO` wypada w połowie ekranu (na siatce).

## Dolny pasek z linkami społecznościowymi na `/` (2026-11-21)

Prośba: kopię paska nawigacji, którą użytkownik wstawił na dół strony, przerobić na dolny pasek w stylu ze screena
(4 równe pola z pionowymi liniami między nimi i linią u góry, wyśrodkowane wersaliki: INSTAGRAM / LINKEDIN / BEHANCE /
DRIBBBLE; na screenie limonkowe tło — przeniesiony sam układ, w kolorach strony).
- Kopia Navi `hFDkJFCJO` (absolutnie na dole breakpointu; na Phone wypadała w połowie ekranu) **usunięta**.
- Nowy **„Dolny pasek”** `HadJ76UFf` w Hero `N06uDCvcg`: `nav` (aria-label „Media społecznościowe”), absolutnie
  left/right/bottom 0, **56 px** (= górny pasek na Desktopie), zIndex 2, przezroczysty, linia górna 1 px tokenem
  „Obrys” `G7JKeAILq` (jak dolna kreska Navi). 4 pola `1fr` (Instagram `P0OXcr50b`, LinkedIn `bLQSaH7CF`, Behance
  `q6gCtjFZq`, Dribbble `d7silKFwI`), linia prawa 1 px w pierwszych trzech, tekst presetem „navi” `FBNRC0So5`
  (Courier Prime 12 px, wersaliki). Ten sam na wszystkich breakpointach (na Phone mieści się).
- **TODO: adresy profili** (Instagram, LinkedIn, Behance, Dribbble) — w projekcie nie ma żadnych; pola są na razie bez
  linków. Po podaniu: `link.href` na polach + `linkStylePreset` na etykietach.
- Siatka kończy się na górnej linii paska: `OirTRcAEZ` bottom 0 → **56 px** (wszystkie breakpointy); Hero padding dolny
  0 → **56 px** (kolumny z listami wyśrodkowane na siatce); gradienty tła: Desktop 53,5% → **50%** (siatka 56–744 px,
  symetrycznie), Tablet/Phone 55% → **51%** (siatka od 80 px); „Przycisk View all” (ukryty) −28 px: Desktop **675**,
  Tablet/Phone **687**.
- Linter: „Visible siblings… too close (−300)” na replikach paska (Tablet/Phone) — fałszywy alarm pomiaru replik,
  zrzuty pokazują równe pola.

## Grid siatki jak grid strony — 3 + 4 + 3, środek wg wysokości (Desktop `/`, 2026-11-21)

Prośba: komponent ma się zachowywać jak grid strony — 4 kolumny na środku z sześcianami, po 3 równe kolumny z każdej
strony, skrajne krawędzie równo z krawędziami ekranu; zbiór sześcianów skaluje się z wysokością ekranu.
- **Kod** `SiatkaPerspektywy.tsx`, grupa „Grid”: nowe **Środek wg wysokości** (`kolOdWys`) i **Wysokość środka**
  (`kolWypeln`, 0,1–1, domyślnie 0,85; widoczna przy włączonym). Gdy wł.: łączna szerokość środkowych kolumn =
  `kolWypeln` × wysokość komponentu (ograniczona, by boczne miały ≥ 10 px), a „Środek (łącznie)” jest ukryty i nieużywany.
  Rzędy na środku są kwadratowe (szer. kolumny), skrajne rzędy dochodzą do krawędzi („Rzędy do krawędzi”).
- **Desktop** (`OirTRcAEZ`): Padding boczny 40 → **0**, Kolumny po bokach 2 → **3**, Środek wg wysokości **wł.**,
  Wysokość środka **0,89** (proporcja 660 / 744 px, którą użytkownik ustawił wcześniej; nad i pod sześcianami ok. 40 px).
  Przy ekranie 1200 × 850: środek ≈ 657 px (kwadrat ≈ 164 px), boczne kolumny ≈ 90 px. „Środek (łącznie)” 660 został jako
  zapas (używany po wyłączeniu).
- Tablet/Phone: Grid wyłączony jak dotąd; przypięte dawne wartości (padding 40, boczne 2, wg wysokości wył.).
- Listy po bokach nadal 442 px — wyśrodkowane, niezależne od wielkości sześcianów.
- 2026-11-21 (później) — **liczba bocznych kolumn sama się dobiera**: nowa kontrolka Grid **„Boczne jak środkowe”**
  (`kolBoczneAuto`; gdy wł., „Kolumny po bokach” jest ukryte). Z każdej strony tyle kolumn (floor lub ceil z
  miejsca / szer. środkowej), by ich szerokość była **najbliższa** szerokości kolumny z sześcianami; skrajne krawędzie
  dalej równo z krawędzią ekranu. Desktop `/`: **wł.** (Tablet/Phone przypięte: wył.). Przykłady (ekran → kolumna
  środkowa, boczne): 1200×850 → 164, 2 × 136; 1440×900 → 175, 2 × 185; 1680×1050 → 209, 2 × 211; 1920×1080 → 215,
  3 × 176; 2560×1440 → 295, 2 × 345.
- 2026-11-22 — **krata tylko w pasie 4 rzędów**: użytkownik nie chciał wąskich pasów kraty (z liniami w głąb) nad
  i pod 4 rzędami sześcianów, ale **bez powiększania rzędów** — nad i pod ma zostać pusta przestrzeń. (Najpierw próba
  „Wysokość środka” 1 — rzędy na całą wysokość — cofnięta.) Nowa kontrolka Grid **„Tylko rzędy środka”**
  (`kolTylkoSrodek`, przy „Rzędach do krawędzi”): canvas przycinany CSS `clip-path: inset(...)` do pasa rzędów o stałej
  wysokości (±1 px na linie brzegowe); nad i pod — puste tło (bez kraty i bez gwiazd z „Tła”; poświata/winieta to osobne
  ramki, zostają). Desktop `/`: wł., „Wysokość środka” z powrotem **0,89**. Tablet/Phone przypięte: wył.
- 2026-11-22 — **scalone prostopadłościany w górnym rzędzie zdjęć**: prośba — w górnym rzędzie sześcianów ze
  zdjęciami/filmami połączyć dwa pierwsze i dwa ostatnie w dwa dłuższe prostopadłościany; w pierwszym zdjęcie z 2.
  sześcianu, w drugim film z 3. sześcianu.
  - Kod, grupa „Zdjęcia w kwadratach”: **Górny rząd** (`scalGora`: „Osobne sześciany” `brak` / „Po dwa” `pary` /
    „Jeden przez cały rząd” `caly`), **Treść 1. bryły** / **Treść 2. bryły** (`scalTresc1/2`: numer kwadratu w górnym
    rzędzie od lewej, którego zdjęcie lub film pokazuje bryła; 0 = jej pierwszy kwadrat). Bryła zajmuje kilka kwadratów
    (`spanW`), głębokość = jak sześcian (min. z boków przedniej ściany); hover/fokus/zmniejszanie liczone dla całej bryły.
    Linie kraty wewnątrz bryły (pionowe na przedniej i tylnej płaszczyźnie warstwy zdjęć + krawędź w głąb przy górnej
    linii) pomijane (`isTopMerge`, jak „Scal rzędy nad/pod”).
  - Zmiana ogólna: zdjęcie dobierane **wg numeru kwadratu** (`pIdx = slotNo`), a nie kolejności sześcianów — scalanie
    nie przesuwa zdjęć w pozostałych kwadratach (bez scalania wynik identyczny; przy „szachownicy” nadal wg kolejności).
  - Desktop `/`: `pary`, Treść 1. bryły **2**, Treść 2. bryły **3** (film4 „jslack”, który był w 3. kwadracie).
    Tablet/Phone (3×3): przypięte `brak`.
- 2026-11-22 — **ten sam film w dwóch kwadratach**: prośba — w dolnym rzędzie, 3. sześcian od lewej (zielone zdjęcie)
  ma pokazywać film z 2. sześcianu w 2. rzędzie. Wszystkie 4 filmy były zajęte, więc nowe kontrolki **„Film (2/3/4)
  także w kwadracie”** (`filmTez`, `film2Tez`, `film3Tez`, `film4Tez`; 0 = brak, widoczne, gdy film jest ustawiony).
  Desktop `/`: `filmTez` **15** (film „meatharvest-jslack”, który gra też w kwadracie 6). Tablet/Phone 3×3 — kwadratu 15
  nie ma, bez zmian.
- 2026-11-22 — **scalanie w dowolnym rzędzie — pole „Scalone bryły”**: prośba — dwa środkowe sześciany w 2. rzędzie
  połączyć w jeden kształt z filmem z 3. sześcianu tego rzędu. Kontrolki „Górny rząd” / „Treść 1./2. bryły” zastąpione
  jednym polem tekstowym **„Scalone bryły”** (`zdjecia.scal`, funkcja `parseScal`): zakresy kwadratów jednego rzędu
  (numery wierszami od lewego górnego), po dwukropku numer kwadratu z treścią, kilka po przecinku, np. `1-2:2, 6-7:7`.
  Nakładające się / wielorzędowe zakresy są pomijane. Linie kraty wewnątrz brył pomijane w każdym rzędzie; krawędź w głąb
  na linii poziomej znika tylko, gdy po obu jej stronach jest bryła (albo brzeg siatki zdjęć).
  Desktop `/`: **`1-2:2, 3-4:3, 6-7:7`** (górny rząd jak dotąd + bryła 6–7 z filmem2 „toaster”). Film „meatharvest”
  (dawniej w kwadracie 6) gra teraz tylko w kwadracie 15. Tablet/Phone: puste.
- 2026-11-22 — **zamiana treści dwóch sześcianów**: „Scalone bryły” przyjmuje też pojedynczy kwadrat z dwukropkiem
  (`a:c` — kwadrat a pokazuje zdjęcie/film kwadratu c, bez scalania; treść liczona wg ustawień sprzed zamian, więc
  `15:16, 16:15` = zamiana). Desktop `/`: dopisane **`15:16, 16:15`** — w dolnym rzędzie film „meatharvest” (filmTez 15)
  jest teraz w ostatnim sześcianie, a pomarańczowe zdjęcie w 3. Pełna wartość: `1-2:2, 3-4:3, 6-7:7, 15:16, 16:15`.
- 2026-11-22 — zamiana w dolnym rzędzie 1. ↔ 2. sześcianu (białe i różowe zdjęcie): dopisane `13:14, 14:13`. Pełna
  wartość „Scalonych brył” na Desktopie `/`: `1-2:2, 3-4:3, 6-7:7, 15:16, 16:15, 13:14, 14:13`.
- 2026-11-22 — **bryła w dolnym rzędzie**: dwa środkowe sześciany (14–15) połączone, z jasnym zdjęciem (pierwotnie
  w kwadracie 13). Usunięte pojedyncze zamiany `15:16` i `14:13` (nakładałyby się z bryłą — parser pomija nakładające
  się wpisy). Desktop `/`: **`1-2:2, 3-4:3, 6-7:7, 13:14, 14-15:13, 16:15`** — dolny rząd: różowe | jasne (bryła) |
  film z palmami. Pomarańczowe zdjęcie (było w 15) wypadło z siatki. Zdjęcie na szerokiej ścianie jest kadrowane ze
  środka („cover”), więc góra jasnego zdjęcia (niebieski owal) jest przycięta — kod nie ma ustawienia punktu kadru.
- 2026-11-22 — bryła w 3. rzędzie: kwadraty 11–12 (kopuła + pomarańczowe) połączone, z pomarańczowym zdjęciem →
  dopisane `11-12:12`. Desktop `/`: **`1-2:2, 3-4:3, 6-7:7, 13:14, 14-15:13, 16:15, 11-12:12`**. Kopuła z 11 wypadła
  w tym miejscu (jest w górnej bryle 1–2). Kadr „cover” ucina górę pomarańczowego zdjęcia (szary owal w połowie).

## Lista tytułów w lewej kolumnie → jednolinijkowy tekst (`/`, 2026-11-22)

Prośba: zastąpić listę („Animation” + Archer Magazine / Arts And Flowers / Arxipelag) krótkim, jednolinijkowym tekstem
symetrycznym do tekstu po prawej („Images, motion and space”) i usunąć wszystkie związane z nią elementy i komponenty.
- Na `/` usunięte: w lewej kolumnie „L” `HD2wSnn92` — przekładki `cbVbz8owY`, `y6NlewCHD` i „Animation links”
  `E7a5Yw8Ck` (nagłówek + 3 instancje wierszy, w tym „Wiersz listy ze zdjęciem” z hoverem); w prawej kolumnie „R”
  `tRvpBEufj` — ukryte (opacity 0) „1” `IJnKLpLY9` (nagłówek) i „2” `lOZG_8ycZ` (lista z instancjami wierszy).
- Nowy tekst **„25 years of branding”** `UDoDYwjDF` (preset „Lista akapit” jak prawy tekst, wyśrodkowany) w „L”
  (padding 20/0 jak prawa „R”, wyśrodkowanie w pionie i poziomie) → lustrzane położenie względem prawego tekstu
  (środek x ≈ 124 vs 1076 przy 1200 px), ta sama wysokość. Treść skrócona z hasła marki „25 years of building brands
  with cultural impact” — do potwierdzenia przez użytkownika.
- „middle” `UK5KtZeEu` (opacity 0, zrzut ekranu w środku) zostaje — to przekładka trzymająca szerokość środkowej
  kolumny w układzie Hero.
- **Komponenty „Wiersz listy” `ZIOR8bv28` i „Wiersz listy ze zdjęciem” `NeuI0X8QN` NIE usunięte** — są jeszcze na
  szkicach `/w` („Home — dolny pasek”) i `/home` (kopia Home). Czeka na decyzję użytkownika. (Ścieżki stron zmienione
  przez użytkownika: dawne `/home-2` → `/x`, `/home-3` → `/y`, `/all` → `/z`, `/home-4` → `/w`.)

### Film 5 — „KANAL” w bryle 11–12 (`/`, 2026-11-22)

- Prośba: zamiast pomarańczowego zdjęcia w bryle 11–12 (3. rząd) film z URL od użytkownika (imgix, GIF → MP4:
  `https://basedesign2.imgix.net/images/Kanal_Case_Thumbnail-GIF-04_1_2026-06-12-121941_gabz.gif?fm=mp4&video-codec=h264&video-bitrate=2500k`).
- Wszystkie 4 filmy były zajęte → w kodzie **Film 5** (`film5`, `film5Miejsce`, `film5Tez`, `film5Kolor`, `film5Opis`,
  `film5Tempo`) na wzór filmu 4. Desktop `/`: film5 w kwadracie **12** (bryła `11-12:12` pokazuje treść kwadratu 12),
  alt „Animacja: czarny napis KANAL na czerwonym tle”. Film wczytuje się już w edytorze (czerwona klatka z napisem).
- Uwaga: to materiał z case study innego studia (Base Design, „Kanal”) — użytkownik decyduje, czy może być na stronie.
- 2026-11-22 — **„Tylko rzędy środka” bez linii brzegowych**: użytkownik zgłosił na Desktopie (podgląd 1322 × 800)
  „drugą poziomą kreskę pod górną kreską” — to była górna linia pasa 4 rzędów (przycięcie miało zapas ±1 px, więc linie
  brzegowe pasa były widoczne; to samo na dole nad dolnym paskiem). Teraz przycięcie `inset(ceil(rT + lw/2 + 1) …
  ceil(h − rB + lw/2 + 1))` — górna i dolna linia pasa poza przycięciem; pionowe linie kończą się na krawędzi pasa.
- 2026-11-22 — **lewy tekst łamie się jak prawy**: prośba — „25 years of branding” ma przechodzić do 2. linii w tych
  samych momentach co „Images, motion and space”. Oba teksty to Courier Prime (stała szerokość znaku) → to samo zachowanie
  przy tej samej liczbie znaków i tej samej szerokości pola. Zmiany: tekst `UDoDYwjDF` → **„25 years building brands”**
  (24 znaki jak prawy; z hasła marki); budowa lustrzana do prawej: w „L” `HD2wSnn92` ramka **„3 — tekst”** `x_wvKCF_k`
  (1fr × 1fr, stack pionowy, środek, gap 10) z tekstem (`textWrap: balance` jak prawy), „L” overflow clip, wyrównanie
  start (prawa „R”: end), gap 40; pusta prawa połówka lewej kolumny `iFkni0iCW` padding 20/0/20/0 (był lewy 12 px) →
  obie połówki 169 px przy 1200. Próg: ≥ ok. 202 px szerokości połówki (ekran ≈ 1330 px) — oba w 1 linii, węziej — w 2.
- 2026-11-22 (poprawka poprzedniej) — użytkownik: „usunąłeś złą kreskę, teraz nie ma żadnej”. Górna/dolna linia pasa
  ma być widoczna; „druga kreska” to była **linia pozioma zewnętrznego rzędu (krawędź komponentu) w dalszej warstwie
  kraty** — w perspektywie wpada do pasa ok. 10 px pod jego górną krawędzią (na dole analogicznie). Teraz: przycięcie
  znów z liniami brzegowymi (±1 px), a przy „Tylko rzędy środka” linie poziome o indeksie poza pasem (`j > kHi`
  lub `j < kLo`) pomijane na każdej głębokości. Do sprawdzenia przez użytkownika w podglądzie 1322 × 800.

## Strona Projects - karta projektu (CMS) - propozycja treści (2026-11-22, wersja 2 z 2026-11-24, do akceptacji)

Prośba: zaproponować rodzaj treści i kategorie karty jednego projektu brandingowego (wzór: karta wydarzenia z datą,
chipem kategorii, awatarem, tytułem, opisem i linkiem). Nic we Framerze nie zmienione; wygląd strony i kart - później.
Rysunek: `assets/projects-karta-cms-propozycja.png` (źródło `assets/projects-karta-cms-propozycja.html`; klienci na
rysunku fikcyjni).
- **Decyzje użytkownika (2026-11-24):** treść kart **po angielsku**; **logo klienta** na karcie - tak; **bez filtrów**
  na stronie Projects; **bez kategorii Sektor** (i chipów sektora) i **bez kategorii Zakres prac** (tagów). Kategorie
  dopasować do obecnego profilu marki na stronie.
- **Na karcie:** 1 Cover (zdjęcie lub film MP4 w pętli + alt), 2 Year (lub zakres 2019–2021), 3 Category - kolorowy
  chip, 4 Client (logo w kółku + nazwa), 5 Title (~70 zn.), 6 Summary (140–220 zn.), 7 „View project →” →
  `/projects/[slug]`.
- **Category** (1 na projekt, tylko etykieta) = 5 dziedzin z sekcji What We Do na `/`: Visual Identity, Art Direction,
  Motion & 3D, Digital Experiences, Space & Print (kolory chipów robocze). Jeśli lista usług w What We Do się zmieni,
  zmienić też kategorie.
- **Tylko w CMS:** Featured on Home + Order (zasila sekcję Featured projects na `/`), Short description (~40 zn.,
  podpis w Featured projects), pełna strona projektu (Challenge / Approach / Outcome, galeria, credits, SEO).
- Usunięte względem wersji 1: Sektor, Branża, Zakres prac, Typ projektu, Miejsce.
- **2026-11-24 (później): logo klienta nigdzie** - ani na karcie, ani w CMS, ani w arkuszu (decyzja użytkownika).
  Rysunek `assets/projects-karta-cms-propozycja.png` z logo jest przez to nieaktualny w tym punkcie; obowiązuje tabela w Figmie.

## Makieta strony `/` w Figmie — Desktop 1200 (2026-11-22)

Prośba: przenieść makietę strony do Figmy (szer. 1200 px), **statycznie** — bez animacji i funkcji (hover, kursor, filmy).
- Plik: [BIURKO – VAAV](https://www.figma.com/design/Hr3x34LirWo1GJa1JRMkun/BIURKO---VAAV?node-id=297-2), strona
  „Numino - 3d grid” `297:2`, ramka **„NUMINO — Home — Desktop 1200”** `310:2` (1200 × 850, jak zrzut Desktopu z Framera),
  na prawo od wcześniejszych elementów strony (ich nie ruszano).
- Warstwy: tło `#0B0D10`, „Tło — poświata” i „Tło — winieta” (gradienty radialne), „Siatka perspektywy” (przycięta do pasa
  rzędów y 95–755) z wektorami linii: przód środek (α 0,34) / boki (0,16), tylna płaszczyzna (0,06), linie w głąb (0,10),
  gwiazdy; „Bryły ze zdjęciami” — 11 grup (przód = prostokąt ze zdjęciem, ściany boczne = wielokąty z tym samym zdjęciem
  + 35% czerni); teksty boczne (Courier Prime 14/23); „Nawigacja” i „Dolny pasek” jako auto-layout; logo jako wektor
  z `assets/numino-logo-nav.svg` (85,4 × 32, rozciągnięte jak we Framerze).
- Geometria odczytana ze zrzutu Framera: punkt zbiegu (599,5; 481), tylna płaszczyzna skala 0,8676, tył brył 0,918,
  padding brył 12 px, kolumny 0 / 135,5 / 271 / 435,25 / 599,5 / 763,75 / 928 / 1064,5 / 1200, rzędy 96 / 260,25 / 424,5 /
  588,75 / 753.
- **Zdjęcia wycięte ze zrzutu 1×** (sieć tej sesji nie pobierała plików z framerusercontent) — niższa jakość; do podmiany
  na oryginały (wypełnienie przodu i ścian bocznych). Filmy pokazane jako stopklatka ze zrzutu; film „jslack” (górny
  prawy prostopadłościan) w edytorze Framera się nie wczytuje → w Figmie szara zaślepka z podpisem „FILM · JSLACK.MP4”.
- Alt-teksty zdjęć zostają we Framerze (Figma nie ma pola alt).

### Przyciemnienie przodu brył na hover (`/`, 2026-11-22)

- Prośba: przednia ściana brył ze zdjęciami/filmami po najechaniu kursorem traci przyciemnienie z 0,9 do 0,5.
- **Kod** `SiatkaPerspektywy.tsx`, grupa „Zdjęcia w kwadratach”: nowa kontrolka **„Przyciemnienie na hover”**
  (`zdjecia.przyciemnienieHover`, 0–1, domyślnie 0). Przednia ściana płynnie przechodzi od „Przyciemnienia” do tej wartości
  w tempie powiększenia na hover („Czas powiększenia” 0,4 s / „Czas powrotu” 0,9 s; postęp `hoverState.grow`). Ściany
  boczne bez zmian („Przyciemnienie ścian”). Gdy wartości brak — jak „Przyciemnienie” (inne instancje: wszystkie mają 0/0).
- Desktop `/` (`OirTRcAEZ`): Przyciemnienie **0,9** (ustawione wcześniej przez użytkownika), na hover **0,5**.
  Tablet/Phone przypięte: 0 / 0 (dotyk nie ma hovera — inaczej zdjęcia byłyby stale ciemne).
- W edytorze Framera hover nie działa (widać stan spoczynku) — sprawdzać w podglądzie.
- Makieta w Figmie (`310:2`) pokazuje zdjęcia bez przyciemnienia — nie zmieniana.

### Rząd kraty nad i pod sześcianami z powrotem (Desktop `/`, 2026-11-22)

- Prośba: przywrócić rząd nad i pod sześcianami usunięty wcześniej tego dnia. Desktop `OirTRcAEZ`: Grid → **„Tylko rzędy
  środka” wył.** (`kolTylkoSrodek` false). Krata znów sięga od dolnej kreski Navi (56 px) do górnej kreski dolnego paska;
  pasy nad i pod 4 rzędami (~40 px) mają linie w głąb i gwiazdy. Wysokość środka 0,89 bez zmian. Tablet/Phone — bez zmian
  (tam ustawienie było wyłączone). Kontrolka zostaje w kodzie — ponowne włączenie przycina kratę jak wcześniej.
- Makieta w Figmie (`310:2`) nadal pokazuje wersję przyciętą (bez tych pasów).
- 2026-11-22 (ciąg dalszy) — prośba: rzędy nad i pod mają mieć **taką samą wysokość i szerokość jak kwadraty
  z sześcianami** (kosztem mniejszych sześcianów). Desktop: Grid → „Wysokość środka” 0,89 → **0,6667** (= 4/6): przy
  „Rzędach nad/pod” 1 wysokość komponentu dzieli się na 6 równych rzędów, a środkowe kolumny = 4 × wysokość rzędu →
  kwadraty. Przy 1200 × 850: rząd/kolumna **123 px** (było ~164), środek 492 px, boczne „Boczne jak środkowe” 3 × 118 px.
  Przy innej wysokości ekranu nadal kwadraty (wszystko liczone z wysokości). Zmiana z 4/6 na inną wartość rozjedzie
  proporcje skrajnych rzędów.
- 2026-11-22 — **„middle” `UK5KtZeEu` = szerokość środka siatki przy skalowaniu**: prośba — przekładka w Hero (opacity 0,
  trzyma szerokość środkowej kolumny) ma mieć szerokość białej kreski pod sześcianami (4 kwadraty) także przy zmianie
  rozmiaru okna. Środek siatki = „Wysokość środka” 0,6667 × wysokość komponentu (= wysokość Hero − 56 − 56), więc
  Desktop: **height 100%** (wnętrze Hero bez paddingu = wysokość siatki) + **aspectRatio 0,6667** (zablokowane
  proporcje; `width` 100px to tylko wartość wejściowa — szerokość liczy się z wysokości). Przy 1200 × 800: 458 px,
  x 371–829 = kreska. (Wcześniej użytkownik ustawił ręcznie 611 px.) Framer odrzuca aspectRatio przy szerokości „auto”.
  Tablet/Phone przypięte: 611 px / height auto (wygląd bez zmian).
  Przy zmianie „Wysokości środka” w siatce zmienić też aspectRatio „middle” na tę samą wartość.
- 2026-11-22 — **przyciemnienie kraty pod bocznymi napisami**: prośba — delikatnie, stopniowo przyciemnić linie pod
  „25 years building brands” i „Images, motion and space”, by mniej nakładały się na tekst. (Użytkownik wcześniej
  uprościł kolumny: tekst stoi bezpośrednio w „L” `HD2wSnn92` / „R” `tRvpBEufj`, 371 × 442 px przy 1200.) W każdej
  dodana jako pierwsze dziecko ramka **„Przyciemnienie pod tekstem”** (L `CSnsXi_dD`, R `Ea8uxk5wi`): absolutnie na całą
  kolumnę, `pointerEvents: none`, `ariaHidden`, wypełnienie `radial-gradient(46% 15% at 50% 50%, rgba(11,13,16,0.62) 0%,
  rgba(11,13,16,0.42) 45%, rgba(11,13,16,0) 100%)` (kolor Tła; ok. 170 × 64 px promienia). Linie pod tekstem ~40% słabsze,
  zanikanie płynne. Uwaga: Framer zamienia px w promieniach gradientu na % — podawać od razu w %. Mocniej/słabiej: zmienić
  krycie 0,62 / 0,42; szerzej: pierwszy promień.
- 2026-11-22 — **maks. 4 kolumny po bokach**: prośba — przy poszerzaniu ekranu przybywało bocznych kolumn kraty (obok
  brył); ma być najwyżej 4 z każdej strony. Kod, grupa „Grid”: nowa kontrolka **„Maks. kolumn po bokach”**
  (`kolBoczneMax`, 0 = bez limitu, widoczna przy „Boczne jak środkowe”) — liczba dobrana przez „Boczne jak środkowe”
  jest przycinana do limitu, a boczne kolumny się poszerzają (krawędzie dalej równo z ekranem). Desktop `/`: **4**.
  Przykłady (kolumna środkowa = (wys. − 112) / 6): 1200×850 → 3 × 118; 1920×1080 → 4 × 159; 1920×800 → było 6, teraz
  4 × 182; 2560×1080 → było 6, teraz 4 × 239. Tablet/Phone: „Boczne jak środkowe” wył. — bez zmian.
- 2026-11-22 — **pionowe kreski nad i pod bryłami z powrotem**: użytkownik (szeroki ekran) zgłosił brak pionowych linii
  w rzędach nad i pod bryłami. Przyczyna: „Scal rzędy nad/pod zdjęciami” (`zdjecia.scalNad` 1600) — przy szerokości
  > 1600 px te rzędy łączyły się w jeden prostopadłościan bez wewnętrznych krawędzi (w edytorze 1200 px niewidoczne).
  Desktop `/`: **`scalNad` 0** (nigdy). Tablet/Phone mają 1600, ale są węższe — bez znaczenia.

## Boczne napisy zmieniają się po kliknięciu bryły (`/`, 2026-11-22)

Prośba: gdy bryła jest kliknięta i powiększona, napisy po bokach zmieniają się na teksty tej bryły; stary napis wylatuje
w górę i jednocześnie znika do 0%, nowy wlatuje od dołu. Użytkownik: „jak się da — na komponentach i wariantach”.
- **Komponenty** (folder Komponenty): **„Napis lewy”** `A1gRbg7LO` i **„Napis prawy”** `k_11UqrF3` — stack z tekstem
  (preset „Lista akapit”, wyśrodkowany, bez tła, przejście wariantów Instant). Warianty: **„Domyślny”** (25 years
  building brands / Images, motion and space) i **„Kwadrat N”** dla każdej bryły na Desktopie (N = numer pierwszego
  kwadratu bryły wierszami od lewego górnego: 1, 3, 5, 6, 8, 9, 10, 11, 13, 14, 16). Teksty edytuje się na canvasie
  w wariantach. Instancje `CIV7J00Mp` (w „L”) i `LolOc7rF8` (w „R”) zastąpiły dawne teksty `UDoDYwjDF` / `XiEwMAVDe`.
- **Treść robocza (zaproponowana przez Claude, do akceptacji)** — opisowa, bez faktów o klientach:
  1 pawilon „Yellow pavilion” / „Light and landscape”; 3 film jslack „Motion study” / „Film loop”; 5 spirala „Endless
  spiral” / „Pattern in motion”; 6 toster „Toast theory” / „3D animation”; 8 różowe okno „Pink window” / „Colour and
  space”; 9 portret „Desert portrait” / „Photography”; 10 niebieska kopuła „Blue oculus” / „Light installation”;
  11 KANAL „Red letters” / „Type in motion”; 13 różowa kopuła „Pink horizon” / „Light and sky”; 14 biała kopuła „White
  dome” / „Architecture and sky”; 16 palmy „Palm drift” / „Landscape in motion”.
- **Kod (to, czego natywnie się nie da):** bryły rysuje komponent kodowy, więc tylko on wie, którą kliknięto.
  `SiatkaPerspektywy.tsx` przy zmianie fokusu wysyła zdarzenie okna **`siatka:fokus`** z `detail { kwadrat }` (0 = brak
  fokusu; zapisuje też `window.__siatkaFokus`). Override **`withNapisFokus`** (`NapisyFokus.tsx`) na obu instancjach
  ustawia wariant „Kwadrat N” (brak wariantu → domyślny Framera) i animuje zmianę (framer-motion, AnimatePresence:
  wyjście y −24 + opacity 0, wejście od y +24; 0,55 s, ease [0.22, 1, 0.36, 1]). Natywne przejście wariantów nie umie
  jednocześnie wypuścić starego napisu w górę i wpuścić nowego od dołu — dlatego ruch jest w overridzie.
- Nowa bryła / zmiana „Scalonych brył” → dodać wariant „Kwadrat N” w „Napisie lewym” (prawy od 2026-11-25 ma tylko „Fokus”).
- Działa tylko w podglądzie / na stronie (edytor pokazuje „Domyślny”). Tablet/Phone: kolumny z napisami ukryte.
- Przy okazji (zmiana użytkownika, nie Claude): w „Dolnym pasku” są teraz 3 pola (bez LinkedIn) i bez pionowych kresek.

### Dolny pasek: pole „Behance” zawsze tak szerokie jak „middle” (Desktop `/`, 2026-11-22)

- Stan wyjściowy (zmiany użytkownika): „Dolny pasek” `HadJ76UFf` ma 3 pola 1fr — Instagram `P0OXcr50b`, Behance
  `q6gCtjFZq`, Dribbble `d7silKFwI` (LinkedIn usunięty), bez pionowych kresek.
- Prośba: Behance zawsze szerokości „middle” `UK5KtZeEu` (= 0,6667 × wys. siatki, liczona z proporcji). Pasek ma stałe
  56 px, więc proporcje nie mogły działać wprost → pasek **powtarza układ Hero**:
  - „Dolny pasek”: absolutnie na całe Hero (top/bottom 0, height 100%), padding **56 / 0 / 56 / 0** jak Hero,
    overflow visible, `pointerEvents: none`, bez obramowania.
  - 3 kolumny (height 100% = wys. siatki): „Kolumna Instagram” `gRmkYEklD` 1fr, **„Kolumna Behance” `NzRVWExTS` width
    auto** z niewidoczną **„Miarką szerokości (jak middle)” `HsHjMxtHI`** (height 100%, aspectRatio 0,6667 — dokładnie
    jak „middle”), „Kolumna Dribbble” `HOPHWE6sN` 1fr.
  - Pola przeniesione do kolumn: absolutnie left/right 0, **bottom −56 px**, 56 px wysokości (czyli w dolnym pasie
    strony), linia górna 1 px tokenem „Obrys” w każdym polu, `pointerEvents: auto`.
  - Przy 1200 × 800: Behance 458 px, x 371–829 = „middle”.
- Proporcje są na „Miarce”, nie na kolumnie: wyzerowanie `aspectRatio` w replice nie działa (dziedziczy się), a ukrycie
  miarki działa. Tablet/Phone: pasek przypięty (top null, height 56, padding 0), Kolumna Behance 1fr, Miarka ukryta,
  pola bottom 0 → 3 równe pola jak wcześniej.
- Przy zmianie „Wysokości środka” siatki zmienić aspectRatio także w Miarce (oprócz „middle”).
- 2026-11-22 — użytkownik potwierdził zrzutem, że zamiana napisów działa (KANAL → „Red letters” / „Type in motion”).
  Potem prośba: **prawy napis na powiększonej bryle = „See more” ze strzałką po prawej**. „Napis prawy” `k_11UqrF3`:
  stack poziomy, gap 8 px; dodana ikona **„Strzałka”** `bp0ahn3e4` (Phosphor „Arrow Right”, 14 px, kolor token
  „Tekst”, grubość 1,5) — ukryta w „Domyślnym”, widoczna we wszystkich wariantach „Kwadrat N”, które mają teraz tekst
  „See more” (opisy brył z prawej strony zastąpione). Lewy napis (tytuł bryły) bez zmian.
  **TODO:** „See more” nie jest jeszcze linkiem — brak stron projektów (por. propozycja karty Projects w CMS); po ich
  powstaniu podlinkować w wariantach (`link.href` + `linkStylePreset`).
- Zmiana użytkownika zauważona przy okazji: środkowe pole dolnego paska to teraz „YouTube” (dawniej Behance; id
  `q6gCtjFZq` i nazwa warstwy bez zmian?) — do sprawdzenia przy linkowaniu.

### Mruganie siatki przy skalowaniu okna (2026-11-22)

- Zgłoszenie (nagranie): przy przeciąganiu okna cała Siatka perspektywy (linie + bryły) co chwilę znikała na pojedyncze
  klatki. Przyczyna w `SiatkaPerspektywy.tsx`, `resize()` (ResizeObserver): ustawienie `canvas.width/height` czyści
  płótno, a w trybie animacji ponowne rysowanie było dopiero w kolejnym `requestAnimationFrame` — ResizeObserver działa
  po klatce animacji, przed malowaniem, więc przeglądarka malowała puste płótno.
- Poprawka: płótno zmieniane tylko przy innym rozmiarze; po zmianie od razu `draw(now, 0)` + `applyHole(now)` (czas
  klatki 0 = stan animacji się nie przesuwa; `step = clamp(dt, 0, 0.05)` — bez dzielenia przez dt).
- Nie da się usunąć: przejście przez granicę breakpointów (1200 px, Desktop ↔ Tablet) to inna instancja komponentu —
  Framer ją przełącza (nowe ustawienia siatki, 4×4 ↔ 3×3), zdjęcia doczytują się z pamięci przeglądarki.

## Dolny pasek jako kolejna sekcja, która przy przewijaniu zakrywa siatkę (`/`, 2026-11-22)

Prośba: dolny pasek ma być kolejną sekcją strony — na starcie wystaje tyle, co dotąd pasek (56 px), a po przewinięciu
w dół zakrywa całą siatkę z bryłami.
- **„Main”** `wUYfTPOi0` (poziomy stos z Hero): `position: sticky`, top 0, zIndex 0 — Hero zostaje w miejscu.
- **„Sekcja — dolny pasek”** `HadJ76UFf` (dawny „Dolny pasek”): przeniesiona z Hero do breakpointu, zaraz po „Main”;
  relative, 100% × **100vh**, tło token „Tło”, zIndex 1, **translateY −56 px** (wystaje 56 px nad dół Hero), padding
  56 / 0 / 56 / 0 (jak Hero — dzięki temu kolumny i „Miarka” dalej dają środkowemu polu szerokość „middle”).
  Pola Instagram / YouTube (`q6gCtjFZq`) / Dribbble: absolutnie **top −56 px** w kolumnach = górny pas sekcji,
  linia górna 1 px. „Wypełnienie pod sekcją” `CHSp1GVo3` (absolutnie bottom −56 px, 56 px, tło) zakrywa pas, który
  translateY zostawia na samym dole strony. Reszta sekcji na razie pusta (miejsce na treść).
- Tablet/Phone: dawne przypięcia paska (56 px, padding 0, pola bottom 0) zresetowane → to samo zachowanie
  (Kolumna Behance 1fr, Miarka ukryta — zostają).
- Nawigacja (Navi, absolutnie u góry breakpointu) przewija się razem ze stroną — nie jest przyklejona.
- **Kod** `SiatkaPerspektywy.tsx`: siatka słucha myszy na całym oknie, więc pod zakrywającą sekcją bryły reagowałyby
  na hover/klik. Nowe `covered(e)`: od elementu pod kursorem w górę do wspólnego przodka z siatką — jeśli po drodze
  jest element z kolorem tła (nie przezroczysty, nie opacity 0), siatka traktuje kursor jak poza nią i ignoruje klik.
- Na canvasie strony przesunięte o 800 px w dół luźne elementy pod Desktopem (Desktop urósł do 2 × 100vh):
  pionowe kreski `j482y2GEM`, `lbTirTotK` i teksty `aaIjkvQMN`, `N7RwZG5ma` (te dwa nachodziły na siebie już wcześniej).
- Przewijania nie widać w edytorze — sprawdzać w podglądzie.

## Sekcja „Featured projects” + Navi fixed (`/`, 2026-11-22)

Prośba: sekcja pod siatką to „featured projects” z listą kilku projektów jeden pod drugim, przedzielonych kreską;
Navi ma być fixed i się nie ruszać.
- **„Sekcja — Featured projects”** `HadJ76UFf`: pionowy stos, height auto, **minHeight 100vh** (zawsze zakrywa siatkę),
  padding dół 80, nadal translateY −56 i zIndex 1. Dzieci:
  - **„Pasek z linkami”** `ZR4kUwPMr` (56 px, overflow visible) z 3 kolumnami jak wcześniej; pola top 0.
    Środkowa kolumna (YouTube) dalej = szerokość „middle”: Miarka `HsHjMxtHI` siedzi teraz w ramce
    **„Miarka — wysokość siatki”** `FynCzwNT6` (height **100vh**, padding 56/0/56/0 — jak Hero, więc wnętrze = wys.
    siatki; wystaje poza pasek, niewidoczna). Tablet/Phone: ramka ukryta, kolumna 1fr.
  - **„Nagłówek sekcji”** `Vmd4wOnMQ` (padding 64/40/24/40; Phone 48/16/16/16): „Featured projects” (h2, preset „navi”).
  - **„Lista projektów”** `uUHwDSEIm`: 5 instancji komponentu **„Wiersz projektu”** `mKIi2lqmd` (folder Komponenty),
    linia dolna 1 px „Obrys”.
- **Komponent „Wiersz projektu”**: zmienne Numer / Tytuł / Zakres / Zdjęcie; wariant **Desktop** (stack poziomy, gap 24,
  padding 16/40, linia górna 1 px „Obrys”): numer (navi, 64 px) · tytuł (Lista akapit, h3, 1fr) · zakres (navi, 240 px) ·
  miniatura 120 × 80 (zdjęcie z alt) · strzałka Phosphor „Arrow Right” 14 px. Wariant **Phone**: padding 16, gap 12,
  numer 28 px, bez zakresu, miniatura 72 × 48 — ustawiony na instancjach w breakpoincie Phone.
- **Treść robocza (do podmiany na prawdziwe projekty)**: 01 Yellow pavilion / Light and landscape, 02 Blue oculus /
  Light installation, 03 Pink horizon / Light and sky, 04 Desert portrait / Photography, 05 Pink window / Colour and
  space — zdjęcia i alt-y z siatki. **TODO:** linki wierszy (brak stron projektów); ew. przejście na CMS (por. propozycja
  karty Projects).
- **Navi fixed**: instancja Navi `KQifDlO5e` w nowej ramce **„Navi — przyklejona”** `GiaHsJO3X` (position fixed,
  top/left/right 0, zIndex 8, tło rgba(11,13,16,0.85) + rozmycie tła 12 px, żeby przewijana lista nie mieszała się
  z napisami). Instancja: relative, 100%.
- Kod `SiatkaPerspektywy.tsx` → `covered()`: siatkę zasłania tylko tło o kryciu ≥ 0,95 (sekcja tak, półprzezroczysta
  Navi nie — reakcja na kursor nad nawigacją jak dawniej).

## Wydajność — cięcie się przy przewijaniu (`/`, 2026-11-22)

Zgłoszenie: strona strasznie się tnie przy scrollu. Siatka (`SiatkaPerspektywy.tsx`, ~3300 linii) przelicza i rysuje
całość w każdej klatce: linie kraty dzielone na odcinki po 9 px, 11 brył, 5 filmów, ściany boczne z teksturą (każda
ściana = 6 pasów × 2 trójkąty, każdy z clip + drawImage **pełnego** źródła, np. 2000 px / klatka filmu).
Zmiany (bez zmiany wyglądu):
- **Tekstury ścian bocznych** z małych kopii (≤ 192 px, `getSideTex`, cache per zdjęcie/film; film odświeżany tylko
  przy nowym `currentTime`) zamiast pełnych źródeł.
- **Nie rysujemy, gdy siatki nie widać**: karta w tle, poza ekranem albo w całości zakryta (3 punkty `elementFromPoint`
  + `coveredEl` — nieprzezroczyste tło ≥ 0,95, np. sekcja Featured projects nad przyklejonym Hero). Sprawdzane przy
  scroll/resize/visibilitychange (raz na klatkę). Filmy wtedy pauzowane, potem wznawiane.
- **W trakcie przewijania co druga klatka** (do 150 ms po ostatnim scrollu) — przyklejona siatka i tak stoi.
- **Gęstość pikseli płótna** w podglądzie/na stronie max **1,5×** (było 2×; edytor bez zmian).
- **„Zbliżenie (scroll)” (`kamera.scrollZoom`) 3 → 0** na wszystkich breakpointach — przy przyklejonym Hero nic nie
  robiło, a czytało `getBoundingClientRect` w każdej klatce.
- **Navi — przyklejona** `GiaHsJO3X`: bez rozmycia tła (backdrop blur nad animowanym płótnem był drogi przy scrollu),
  tło rgba(11,13,16,**0.92**).
- Dalsze możliwości (zmieniają wygląd — do decyzji użytkownika): wyłączyć „Zdjęcie na ścianach” (ściany w kolorze),
  mniej filmów (5 dekoduje się naraz), mniej gwiazd (190), wyłączyć świetliki / przerwy w liniach („gaps”).

## Efekt Hero, gdy wjeżdża sekcja projektów — „odjazd w głąb” + „zgaszenie światła” (`/`, 2026-11-22)

Claude zaproponował 5 pomysłów (odjazd w głąb, czarna dziura przewijana, bryły znikające rzędami, zgaszenie światła,
krata przechodząca w kreski listy); użytkownik wybrał połączenie 1 + 4.
- **Kod** `SiatkaPerspektywy.tsx`, grupa „Kamera”: **„Odjazd przy przewijaniu”** (`kamera.odjazd`, sześciany, 0 = wył.)
  i **„Odjazd — zakres”** (`kamera.odjazdZakres`, × wysokość okna, domyślnie 0,9). Postęp = `scrollY / (zakres × innerHeight)`
  z wygładzeniem (smoothstep + to samo tłumienie co scrollZoom); kamera cofa się przez warstwy kraty (`scrollState.v`
  ujemne → `shift`), bryły maleją ku punktowi zbiegu i gasną w mgle. W trakcie odjazdu rysowana każda klatka
  (`scrollDriven`), poza nim — oszczędzanie co drugiej klatki przy scrollu jak wcześniej.
  Desktop `/`: **odjazd 3, zakres 0,9** (Tablet/Phone dziedziczą).
- **Natywnie (Scroll Transform, trigger `onScrollTarget`, viewport „start”, spring 400/60)**: cele przewijania
  „hero” = Main `wUYfTPOi0`, „projects” = sekcja `HadJ76UFf` (`elementId` + `scrollTargetEnabled`).
  - Hero `N06uDCvcg`: przy „projects” **scale 0,94, opacity 0,35** (prześwituje ciemne tło = ściemnienie).
  - Column Left `AzgVkCy4j` / Column Right X `Hgbr5CLZ2` (napisy): **y −48 px, opacity 0**.
  **2026-11-23 - usunięte** na prośbę użytkownika (napisy nie mają się ruszać przy scrollu): `styleTransformEffect` = brak
  w obu kolumnach (wszystkie breakpointy dziedziczą). Kolumny są nadal w Hero, więc dalej zmniejszają się (0,94) i przygasają (0,35) razem z nim.
- Strojenie: siła odjazdu / zakres w kontrolkach siatki; skala/ściemnienie/odpływ napisów w Scroll Transform warstw.
  W edytorze widać tylko stan początkowy — sprawdzać w podglądzie.
- 2026-11-22 — poprawka: przy odjeździe pojawiały się nowe linie pionowe (kamera cofając się przechodziła przez
  kolejne warstwy kraty, które dorysowywały się przed siatką). Teraz przy `scrollState.v < 0` warstwy o `id < 1`
  (bliższe niż przednia warstwa ze spoczynku; `id = k + floor(shift)`) są pomijane — struktura tylko odsuwa się w głąb,
  z przodu nic nie przybywa. Linie w głąb (od krawędzi ekranu) bez zmian.
- 2026-11-23 — poprawka (nagranie użytkownika): przy odjeździe bryły **jaśniały** — ciemna nakładka przodu
  (`przyciemnienie` 0,9) była mnożona przez `visP = visNear × depthFade(zP)`, a samo zdjęcie tylko przez `visNear`,
  więc w głębi nakładka słabła. Teraz `fadeOdj = depthFade(zP) / depthFade(zRest) × (1 − odjazdCien × postęp odjazdu)`
  (w spoczynku = 1, wygląd bez zmian): przód — nakładka `1 − (1 − dim × visP) × fadeOdj`, ściany boczne — jasność × fadeOdj.
  Bryły ciemnieją tym bardziej, im dalej odjeżdżają. Nowa kontrolka „Kamera” → **„Odjazd — przyciemnienie brył”**
  (`kamera.odjazdCien`, 0–1, domyślnie **0,6**; 0 = tylko mgła, 1 = do czerni).

## Stopka: dolny pasek w stylu echo.txt (`/`, 2026-11-23)

Prośba: „footer bottom” `UmUPg4rLv` (w ramce „Footer” `yVikSkj7m`, pod dużym logo; wcześniej kopia paska z linkami
z napisem „featured projects”) przerobić na pasek jak dolny pasek ze screena echo.txt (bez znacznika „Made in Framer”):
po lewej znak + copyright, na środku pusta kapsuła, po prawej linki społecznościowe i ostatni element przy krawędzi.
- Usunięte stare kolumny (Instagram/Behance z Miarką/Dribbble). Pasek: **„Dolny pasek stopki”** `UmUPg4rLv`, 56 px,
  padding boczny 40, stack poziomy, wyśrodkowany w pionie, bez linii górnej (jak na screenie).
- **„Lewa strona”** `YmcZeRgRB` (1fr, gap 120): „Logo (do góry)” `QJmLUGq_B` (link `/#hero`, płynne przewijanie,
  aria-label „NUMINO, back to top”, hover opacity 0,6) z SVG logo NUMINO `S0_NVRWRA` (35 × 20 px, kopia z Navi)
  + „Copyright” `GErbdfJPy`: „© NUMINO · 25 years of branding” (preset „footer” `kDjaPd3uW`, 11 px, wersaliki).
- **„Kapsuła”** `XT9MUX_sA`: 46 × 12 px, obrys 1 px rgba(255,255,255,0.8), zaokrąglenie 100 px, ozdobna (aria-hidden).
- **„Prawa strona”** `Uxo6CATcF` (1fr, do prawej, gap 120): „Media społecznościowe” `bcIhQ5Hph` (gap 24: Instagram
  `rNGt4vtb4`, YouTube `MWJNJ7yGo`, Dribbble `WQKATF_MS`) + „Connect” `uusspPXOm`; wszystko presetem „footer”.
- Tablet: gap lewej/prawej strony 48. Phone: pasek w kolumnie (height auto, padding 24/16, gap 16), kolejność:
  linki → Connect → logo + copyright; kapsuła ukryta.
- **TODO:** adresy Instagram / YouTube / Dribbble i cel „Connect” - brak danych, teksty bez linków
  (po podaniu: `link.href` + link style preset; w projekcie nie ma jeszcze żadnego link style presetu).
- **Do sprawdzenia przez użytkownika:** ramka „Footer” `yVikSkj7m` ma ten sam `elementId` „projects” co sekcja
  Featured projects `HadJ76UFf` (pozostałość po kopii) - może mylić cel przewijania „projects” w Scroll Transform
  Hero i napisów. Nie zmieniane. Pasek stoi tuż pod logo, a nie na dole 100vh stopki (układ ramki bez zmian).

## Featured projects: przyklejone teksty zmieniane wg zdjęcia na środku (`/`, 2026-11-23)

Wzór: focus-gallery.framer.website (komponent z kodem). Z jego kodu: aktywne jest zdjęcie, którego środek jest najbliżej
środka ekranu; stary tekst znika od razu, nowy wjeżdża 0,3 s (krycie 0 → 1, tytuł z −20 px, opis z +20 px); teksty
40 px od krawędzi ekranu, w pionowym środku; poniżej 1024 px ukryte; zdjęcia: aktywne skala 1,3, reszta 0,7 i krycie 0,4.
Układ zbudował użytkownik z instrukcji Claude (sekcja `HadJ76UFf`): „Lewa kolumna” `RqVV9HufJ` (absolute, Left/Right 0,
Top −100, wysokość całej sekcji, pointer events none, zIndex 3) z przyklejoną ramką „tekst - sticky” `M0WLo0IsD`
(sticky, Top 56, 100vh; pasy „left text” `Xmdf5w5Yk` 1fr / „middle” `Rx6zlkF2_` 546 px / „right text” `kngBPqYgF` 1fr).
Zdjęcia w grupie „1” `KzTe86uZ1` są Scroll Section: photo-1 `HzQMxSHVp`, photo-2 `kA1bO5szG`, photo3 `a0kbIINEc`.
- Komponent „tekst - sticky” (warianty + przejścia) okazał się niepotrzebny: we Framerze nie da się w panelu ustawić
  przejścia pojedynczej warstwie w wariancie (przez API tak). Instancja odpięta (Detach), komponent usunięty.
- Teksty: „Tytuły” `vIFNNRaWe` (260 × 20, w lewym pasie, padding lewy 40) i „Opisy” `KEnBAz7rn` (w prawym, padding
  prawy 40, tekst do prawej); w każdej po 3 teksty nałożone (absolute, top 0): Tytuł 1–3 `JFATg6NBS`, `oceFTVdIz`,
  `jTG5RRS_6`, Opis 1–3 `TESqBFJAK`, `V6j5yUuV_`, `G4uQpy6Vk`. Treść robocza („Tytuł N”, „opis N”) - do podmiany.
- Każdy tekst: Appear, trigger **Scroll Section** = jego zdjęcie, replay; wejście z krycia 0 i x −20 (tytuły) / +20
  (opisy), Ease Out 0,3 s; wyjście do tego samego stanu w 0,01 s.
- Tablet i Phone: „Lewa kolumna” ukryta (jak we wzorze poniżej 1024 px).
- W edytorze widać wszystkie 3 teksty naraz (nałożone) - efekty działają tylko w podglądzie. Do sprawdzenia przez
  użytkownika: moment przełączenia (środek ekranu czy góra) i czy replay chowa tekst przy następnym zdjęciu; jeśli nie,
  wrócić do komponentu z wariantami i przejściami warstw ustawionymi przez API.

- 2026-11-25 - **Tytuły dopasowane do zdjęć; „Touski” zastąpione przez Our Legacy** (prośba użytkownika: klik na tytuł
  lub zdjęcie ma prowadzić do strony projektu; strony projektu jeszcze nie ma - **użytkownik zrobi ją sam**, potem
  podpinamy linki). Stan zastany: tytuły nie pasowały do zdjęć (Scroll Section): przy zdjęciu Nod był „Beta bar”, przy
  puszce Beta - „Touski” (nie ma go w CMS), przy drugim zdjęciu Beta (telefon) - „NOD Objects”. Teraz (tytuły razem
  z opisami): photo 1 `W0o27POab` (Nod) → Title 1 `JFATg6NBS` **Nod Objects** / „Identity, Product”; Photo 2 `kA1bO5szG`
  (Beta) → Title 2 `oceFTVdIz` **Beta Bar** / „Identity, Art Direction”; photo 2 `L48Zyy6zT` (w nim „Photo 3 - Our
  Legacy” `a0kbIINEc`) → Title 3 `jTG5RRS_6` **Our Legacy** / „Art Direction” (kategoria z CMS); zdjęcie = Main image
  Our Legacy z CMS (plakat EVAC). Opis „Website, Graphic Design” (Touski) nieużyty. Zdjęcia dostały alt-texty.
  - **Na później (linki):** „Lewa kolumna” `RqVV9HufJ` ma `pointerEvents: none`, a 3 tytuły leżą na sobie (absolute,
    ukryte tylko kryciem) - samo dodanie linków do tytułów nie zadziała (klik trafiłby w górny, niewidoczny tytuł).
    Trzeba będzie np. link na zdjęciach + tytuły klikalne przez kod albo przebudowa tytułów.

- 2026-11-25 - **Linki do strony projektu** (prośba użytkownika: klik w tytuł lub zdjęcie → strona projektu; zgoda na
  pustą stronę). Zmiany w `main`, nieopublikowane.
  - **Strona „Project”** `JJQ4pAWMy`, ścieżka `/projects/:TpqN6PgHg` (strona CMS kolekcji Projects, adres = Slug, np.
    `/projects/beta-bar`), szablon „Układ z paskiem” `cZLu0HAKR`, breakpointy Desktop `Ob89z3UFi` (1200, wys. 1000),
    Tablet `zzq6hyL6v`, Phone `OMyD7gpoX`. **Celowo pusta - treść projektuje użytkownik.**
  - Featured projects na `/`: linki (href + collectionItem) na zdjęciach `W0o27POab` → nod-objects, `kA1bO5szG` →
    beta-bar, `L48Zyy6zT` → evac-our-legacy-roa i na tytułach `JFATg6NBS` / `oceFTVdIz` / `jTG5RRS_6` (te same projekty).
    Tytuły: nowy styl linku **„Featured title link”** `gIrdK07WJ` (kolor jak preset tytułu rgba(255,255,255,0.8),
    podkreślenie na hover, offset 4 px) + override **`withClickableWhenVisible`** z nowego pliku **`FeaturedLinks.tsx`**:
    tytuł jest klikalny tylko przy kryciu > 0,5 (tytuły leżą na sobie, a „Lewa kolumna” ma pointer events none);
    sprawdza krycie co klatkę tylko, gdy tytuł jest na ekranie (IntersectionObserver). Działa tylko w podglądzie.
  - `/projects`: wiersze obu list („Project Row” `r1XSFaNGa` i `fedaI36BN`) linkują do strony projektu (Slug z listy).
  - Zastane: użytkownik podzielił „Cube col” w wierszu na dwie kolumny 1fr (`v3zJJF85a` + `bVsD9ntJ2`, linia na środku
    kolumny z sześcianem) - kopia na hover dopasowana (`RIiuJi1Zw` 1fr + `xtTHvIcYW` 1fr), obie ukryte na Phone.
    Nakładka z sześcianem bez zmian („Right” 2fr nad obiema kolumnami). Nawigacja w szablonie zmieniona przez użytkownika
    (About / Work / Archive / Contact).

## Zdublowane nazwy Scroll Section - poprawione (`/`, 2026-11-24)

Zgłoszenie: Scroll Transform na „Pasku z linkami” `ZR4kUwPMr` (krycie 1 → 0 przy celu `nv67EJ8nh`, viewport start) nie
działał. Przyczyna: powtarzające się nazwy Scroll Section (`elementId`, w HTML musi być jedyny), powstałe przy duplikowaniu
warstw: „photo3” ×2, „pierwsza” ×3, „projects” ×4. Efekty wskazują cele po ID warstwy, ale na stronie cel jest szukany po
nazwie, więc drugi „photo3” (cel paska) był nieosiągalny.
- Nowe nazwy: `nv67EJ8nh` (ostatnie, małe zdjęcie w grupie „1”) **photo-4**, „Photo 3” `a0kbIINEc` **photo-3**,
  „About” `yJcrtn4nP` **about**, „6” `sX3rRcew2` **sekcja-6**, „Footer” `yVikSkj7m` **footer**
  („projects” zostaje tylko sekcji Featured projects `HadJ76UFf`).
- Scroll Section wyłączone (nie były celem żadnego efektu): „Pasek z linkami” `ZR4kUwPMr`, „Shade” `Sx2ug13OI`,
  „Pasek z linkami” w „Lista projektów” `gz49SgmVh`.
- Linki z kotwicą w projekcie: tylko `/#hero` (logo w stopce) - bez zmian.
- Zasada na przyszłość: po zduplikowaniu warstwy ze Scroll Section zmienić jej nazwę.

## Podsumowanie pod zdjęciami Featured projects (`/`, 2026-11-24)

Prośba: osobna sekcja z opisem i przyciskiem („Projects” `yJcrtn4nP`, kopia z translateY −56, tekst 15 px bez presetu,
na Phone wychodził poza ekran) ma być dopełnieniem sekcji ze zdjęciami; tekst o tym, jakie projekty robimy i że jest
więcej; dobrać wielkość i odstępy.
- **Miejsce w warstwach:** nie osobna sekcja na poziomie breakpointu, tylko część sekcji Featured projects - ramka
  **„Podsumowanie”** `rkxEEThqG` w kolumnie zdjęć (grupa „1” `KzTe86uZ1`), zaraz po „Photo 3”, przed „spacer”
  (`nv67EJ8nh`, cel wygaszania paska - pasek „featured projects” gaśnie dopiero po podsumowaniu). Sekcja `yJcrtn4nP`
  usunięta (jej nazwa Scroll Section „about” zniknęła razem z nią; nic jej nie używało).
- Układ: stos pionowy, do lewej (krawędź równa ze zdjęciami), szer. 100% / max 546 px (= zdjęcia), padding górny 96
  (+ gap grupy 28 = 124 px od ostatniego zdjęcia), odstęp tekst-przycisk 32.
- Tekst „Opis” `czoxkt2o5`: „We shape brands for companies and cultural institutions, across images, motion and space.
  These are a few of them, and there is more to see.” (z marki NUMINO: branding dla firm i kultury + „Images, motion
  and space” ze strony; do akceptacji przez użytkownika).
- **Nowy preset „Opis sekcji”** `Duk87rJ1f`: PP Neue Montreal 300, 24 / 22 / 20 px (Desktop / Tablet / Phone),
  interlinia 1,35em, odstęp −0,01em, kolor token „Tekst”.
- Przycisk „View all” `saShW5RM2` (link `/z`) bez zmian.

## Podsumowanie wyśrodkowane, nowe ostatnie zdanie; angielskie nazwy warstw (`/`, 2026-11-24)

- „Outro” `rkxEEThqG` (dawne „Podsumowanie”): tekst i przycisk wyśrodkowane (stack center, tekst center, textWrap
  balance). Ostatnie zdanie zmienione na prośbę użytkownika: „We shape brands for companies and cultural institutions,
  across images, motion and space. Explore the rest of our work.”
- Wszystkie warstwy na `/` z polskimi nazwami przemianowane na angielskie (49 warstw, ID bez zmian), m.in.:
  Featured Projects `HadJ76UFf`, Side Text Track `RqVV9HufJ`, Titles / Title 1-3, Descriptions / Description 1-3,
  Section Bar `ZR4kUwPMr` (i `gz49SgmVh`, `d5x7_nEeP`), Outro / Outro Text `czoxkt2o5`, View All Button `saShW5RM2`,
  Project List `csMK8sqkt`, Project 01-05, Bottom Fill, Section Heading `bSDOGqGD1`, Footer Bar `UmUPg4rLv`
  (Left Side, Logo (Back to Top), Pill, Right Side, Social Links), Navi - Fixed `GiaHsJO3X`, Perspective Grid
  `OirTRcAEZ`, Left Label / Right Label (instancje „Napis lewy/prawy”), Background - Glow / Vignette, Label (etykiety),
  Instagram / Behance / Dribbble Column, Grid Height Ruler, Width Ruler (as Middle).
- Nie zmieniane (to nie warstwy strony): nazwy komponentów i presetów tekstu (np. „Napis lewy”, „Opis sekcji”),
  kontrolki kodu siatki, aria-label stopki „Media społecznościowe”.

## Sekcja „What We Do” (wariant 1 z propozycji, `/`, 2026-11-24)

Prośba: zamiast drugiej listy projektów (sekcja „6” `sX3rRcew2`) sekcja o tym, czym marka się zajmuje; układ z tekstami
roboczymi; inspiracje: sort-office.com, basement.studio (brands, websites, 3D, products), lusion.co (strategy / art
direction, UX/UI, motion, interactive, WebGL / 3D production). Uwaga: dawny tekst podsumowania („creative coop working
with makers and brands to shape impactful brand experiences”) był prawie dosłownie opisem sort-office.com.
- **Sekcja „6” zostaje** (na prośbę użytkownika, bez zmian, nadal widoczna) - do decyzji: ukryć / usunąć.
- Nowa sekcja **„What We Do (TODO: confirm copy)”** `J09QQV8My` (kopia układu „6”), na Desktopie zaraz po Featured
  Projects, przed „6”. `section`, aria-label „What we do”, Scroll Section **what-we-do**; translateY −56, padding dół 80
  jak „6”.
- W środku „Service List” `vjzrf0wvx`: przyklejony „Section Bar” `Mop_e0NSp` z napisem „what we do”; **„Intro (TODO)”**
  `nWn62nZV_` (padding 96/40/64/40) z „Intro Text” `R5IzFmrsB` (h2, preset „Opis sekcji”, środek, max 546 px):
  „From first idea to final detail, we build brands end to end, for companies and for culture.”
- 6 instancji „Wiersz projektu” (Service 01–06): Brand Strategy / Positioning, naming · Visual Identity / Logos, type,
  brand systems · Art Direction / Photography, campaigns · Motion & 3D / Animation, film, CGI · Digital Experiences /
  Websites, interactive, WebGL · Space & Print / Exhibitions, signage, packaging. Miniatury tymczasowo ze zdjęć projektów.
- **TODO (użytkownik):** potwierdzić listę usług i opisy (to propozycja, nie fakty o marce), dobrać miniatury do usług,
  linki wierszy (strzałka sugeruje link).
- 2026-11-24 - na prośbę użytkownika **bez Brand Strategy**: wiersz usunięty, pozostałe przenumerowane 01-05
  (Visual Identity `UnXZDLWCz`, Art Direction `RVrYvBxB2`, Motion & 3D `wHhhZpKK4`, Digital Experiences `hfUpV2v4Q`,
  Space & Print `ayGvY283I`).

## Tabela danych do CMS w Figmie (2026-11-24)

Prośba: czytelna, prosta tabela wszystkich danych do CMS (kolekcja Projects), posegregowana po kategoriach.
- Plik [BIURKO – VAAV](https://www.figma.com/design/Hr3x34LirWo1GJa1JRMkun/BIURKO---VAAV?node-id=328-27), strona
  „Numino - 3d grid”, ramka użytkownika **„Dane CMS”** `328:27` (szer. 4970 bez zmian; zamieniona na auto-layout
  pionowy, padding 160, wysokość dopasowana do treści - ok. 5330 px).
- Grupy: 01 Karta projektu (pola 1-9), 02 Strona główna - Featured projects (10-12), 03 Pełna strona projektu (13-18),
  04 SEO i udostępnianie (19-20), 05 Wartości pola Category (5 dziedzin z What We Do z kolorami chipów).
  Kolumny: #, Pole (nazwa w CMS), Typ pola w Framerze, Gdzie widać, Wymagane, Zasady / opis, Przykład.
- Wiersze 1-20 to instancje komponentu **„CMS Table / Row”** `330:2` (leży na prawo od ramki; teksty kolumn jako
  właściwości). Fonty: Inter + Courier Prime (jak etykiety na stronie). Treść zgodna z propozycją karty (wersja 2).
- Do potwierdzenia: czy Framer CMS ma pole typu Gallery (inaczej kilka pól Image), limity znaków, kolory chipów.

## Nowa strona „Projects” `/projects` (2026-11-24)

Stan zastany (zmiany użytkownika): sekcja „What We Do” `J09QQV8My` przemianowana na **„projects”**, bez „Intro” i bez
ramki „Service List” (pasek + 5 wierszy bezpośrednio w sekcji), napis paska „our projects”; sekcja „6” usunięta.
- Nowa strona **Projects** `RK_gmhXuR`, ścieżka `/projects`, szablon układu **„Układ z paskiem”** `cZLu0HAKR` (Navi
  u góry, jak `/z` „All”). Breakpointy: Desktop `a7yxUtaxD`, Tablet `hxNFrbGfp`, Phone `gXUpXfgZ5` (wysokość 1200 px).
- Sekcja „projects” `J09QQV8My` przeniesiona z `/` (teksty bez zmian): bez translateY −56 (to było tylko pod Hero),
  padding 80/0/80/0 (Phone 56/0/64/0 - pod Navi 80 / 56 px), „Section Bar” `Mop_e0NSp` sticky **top 0** (Navi w
  szablonie nie jest przyklejona). Wiersze na Phone przełączone na wariant Phone (jak na `/`).
- Na `/` zostały: Main, Featured Projects, Footer.
- Do decyzji: nic jeszcze nie linkuje do `/projects` (przycisk „View all” prowadzi do `/z`, Navi bez linków).

## Arkusz treści projektów przed CMS - Figma (2026-11-24)

Prośba: rozpisać w Figmie to, co trafi do CMS - kategorie i listę projektów (na start 6), przy każdym projekcie osobne
ramki na dane: zdjęcie główne, zdjęcia dodatkowe, tytuł, nazwa, rok, opis długi, opis skrócony; **bez logo klienta**.
- Ramka **„Treści CMS - projekty (robocze)”** `332:142` (2880 szer., x 2257, y 7697, pod tabelą „Dane CMS”).
  A „Kategorie projektów” (5 kart z chipami), B „Projekty” - bloki **Project 01-06** (`332:185`, `332:282`, `332:379`,
  `332:476`, `332:573`, `332:670`, status TODO). Kolejność pól: teksty 01 Project name, 02 Title, 03 Category, 04 Year,
  05 Short description, 06 Long description (lewa kolumna), zdjęcia 07 Main image, 08 Additional images (6 miejsc,
  prawa kolumna). Każde zdjęcie z polem „Alt:”. Pola techniczne (Slug, Order, Featured, SEO) uzupełniane przy przenoszeniu.
- Komponenty (na prawo od ramki): **„CMS Entry / Field”** `331:158` (warianty Size=Short/Long; właściwości No, Label,
  Limit, Value) i **„CMS Entry / Image”** `331:167` (Size=Main 1232×770 / Extra 394×263; Label, Alt). Zdjęcie wkleja się
  jako wypełnienie warstwy „Image”; dodatkowe miejsce = duplikat instancji w siatce „Grid”.
- Tabela „Dane CMS” zaktualizowana (17 pól): Client name → **Project name**, Client logo usunięte, Summary → **Short
  description**, podpis w Featured → **Home caption**, Challenge/Approach/Outcome → jedno pole **Long description**,
  Gallery → **Additional images**, Cover image → **Main image**.
- Pytanie od użytkownika: czy rozpisywać to raczej we Framerze przed oficjalnym CMS. Odpowiedź: na etapie zbierania
  treści Figma (obok siebie zdjęcia i teksty, komentarze); gotowe projekty wpisać do kolekcji Projects we Framerze
  jako **wersje robocze (Draft)** - nie trafiają na stronę, dopóki nie zostaną opublikowane.
- 2026-11-24 - **Long description: maksymalnie 3 zdania** (decyzja użytkownika). Zmienione: tabela „Dane CMS” (wiersz 12),
  arkusz (6 pól „Long description”: limit „maks. 3 zdania”), wariant Size=Long komponentu „CMS Entry / Field” (minHeight 200).
- 2026-11-24 - **6 projektów w arkuszu wypełnionych treścią z sort-office.com** (zgoda i prośba użytkownika: strona NUMINO
  to projekt na kurs dla samorozwoju, projekty Sort Office opisane jako projekty NUMINO; **tylko w Figmie**, Framer bez zmian).
  Kolejność jak na stronie źródłowej: 01 Department of Interest (2025, Digital Experiences), 02 Beta Bar (2021, Visual
  Identity), 03 EVAC x Our Legacy + ROA (2024, Art Direction), 04 Mycoaudio (2026, Visual Identity), 05 Nod Objects
  (2023, Art Direction), 06 Letter Bet (2022, Visual Identity). Pozostałe na stronie: Touski, Reigning Champ, Miriam
  Brellenthin (nieprzeniesione).
  - Short description = jedyne zdanie opisu ze strony (dosłownie). Long description = to zdanie + zdanie o zakresie prac
    NUMINO, przepisanym z listy dyscyplin na stronie (nic ponad to nie dopisywano). Title napisany na bazie opisu.
    Kategorie przypisane przez Claude wg dyscyplin ze strony - do zmiany przez użytkownika.
  - Zdjęcia: wszystkie ze stron projektów (6-10 na projekt, łącznie 42), zmniejszone do maks. 2400 px, wgrane do slotów
    „CMS Entry / Image” (zdjęcie główne = poziome, jeśli było; portretowe w trybie FIT). Alt-texty po angielsku,
    napisane po obejrzeniu zdjęć. Film Mycoaudio (strumień HLS) nieprzeniesiony.
  - Etykieta statusu bloków: „wzór: sort-office.com”. Dane pobrane z `sort-office.com/api/viewer/project/4576252/widgets?pageId=…`
    (strona w Readymagu); do sieci środowiska dodane: sort-office.com, www.sort-office.com, st-p.rmcdn1.net, c-p.rmcdn.net,
    i-p.rmcdn.net.
  - Uwaga: to treści i zdjęcia innego studia - przy publikacji strony poza kursem trzeba je zastąpić.
  - **Zasada (użytkownik, 2026-11-24):** jeśli wejście na sort-office.com się nie uda (sieć, blokada), pobrać treści
    i zdjęcia przez przeglądarkę Chrome użytkownika (Claude in Chrome), zamiast się zatrzymywać.

## „What We Do” na stronie głównej (3 usługi) + „View all” → `/projects` (2026-11-24)

- Nowa sekcja **„What We Do”** `NgsTpcy9z` na `/`, między Featured Projects a Footer: kopia sekcji „projects” ze strony
  `/projects` (tamta bez zmian). Jak inne sekcje na `/`: translateY −56, padding dół 80, przyklejony pasek `tPIZgEwql`
  top 112 z napisem **„what we do”**; Scroll Section „what-we-do”, aria-label „What we do”.
- Tylko 3 wiersze (prośba użytkownika): 01 Visual Identity `FcCmDEssL`, 02 Art Direction `roZ9_yrtv`,
  03 Motion & 3D `Ff9NovRGv` (zakresy jak na `/projects`); na Phone wariant Phone.
- Przycisk „View all” `saShW5RM2` (w Outro pod zdjęciami): link `/z` → **`/projects`**.
- W edytorze przyklejony pasek nachodzi na pierwszy wiersz (rysowany w pozycji przyklejenia) - tak samo było z dawną
  sekcją „6”; sprawdzać w podglądzie.

## „What We Do” - nowy design: trzy kolumny (wariant A, `/`, 2026-11-24)

Użytkownik chciał nowy wygląd zamiast wierszy jak w liście projektów; z 3 propozycji (A kolumny, B wielka typografia
z kadrem na hover, C przyklejony nagłówek + bloki) wybrał **A**.
- W sekcji `NgsTpcy9z` wiersze „Wiersz projektu” usunięte; pasek „what we do” `tPIZgEwql` bez zmian.
- **„Services”** `RRRW9tVPN`: stack poziomy, linia górna i dolna 1 px token „Obrys”. 3 kolumny **„Service 01-03”**
  (`k586JCwzk`, `dPkQTocMB`, `Y5U6n1KY5`), 1fr, padding 40/40/48/40, gap 24, linia pionowa 1 px między kolumnami
  (ostatnia bez obramowania). W kolumnie: „Label” (preset „navi”: 01 / Identity, 02 / Image, 03 / Motion), „Media”
  (100% × proporcja 4:5, przycina; w środku „Image” ze zdjęciem i alt, hover: skala 1,04, 0,6 s), „Text”: „Title”
  (nowy preset **„Service Title”** `BtthkWnh3`: PP Neue Montreal 300, 40 / 28 / 32 px) i „Description” (nowy preset
  **„Service Description”** `jkvAPUd5v`: PP Neue Montreal 400, 16 / 15 / 15 px, krycie warstwy 0,7).
- Opisy (propozycja, do akceptacji): Visual Identity - „Logos, type and brand systems that hold together from a business
  card to a building.” · Art Direction - „Photography and campaigns with one consistent eye, from concept to final
  image.” · Motion & 3D - „Animation, film and CGI that let a brand move, in feeds, on screens and in space.”
- Zdjęcia tymczasowe (niebieska kopuła, różowa kopuła, mężczyzna w kapeluszu) - do podmiany na materiały usług.
- Tablet: padding kolumn 24/32/40, gap 20. Phone: kolumny pod sobą (pełna szerokość, padding 32/16/40, linia dolna),
  kadr 5:4 zamiast 4:5.
- Linter: „clipped by ancestor” przy hover scale - zamierzone (kadr przycina powiększenie).
- 2026-11-24 - **4 kolumny** (prośba „daj 4 sekcje”): dodana „Service 04” `VssJ3SdjA` - 04 / Digital, **Digital
  Experiences**, opis (propozycja) „Websites and interactive work, from editorial sites to WebGL, built to feel like the
  brand.”, zdjęcie różowe okno (alt jak w liście projektów). Linia pionowa teraz też przy „Service 03”, ostatnia bez.
  Preset „Service Title” zmniejszony: 32 / 28 / 28 px (Desktop / Tablet / Phone). Tablet: siatka 2 × 2 (zawijanie,
  kolumny 50%, linie dolne pod 01-02, bez prawej przy 02). Phone: 4 bloki pod sobą.
  Na Desktopie „Digital Experiences” łamie się na 2 linie (opis tej kolumny zaczyna się niżej).

## Wszystkie sekcje `/` w stacku „Main” (2026-11-24)

Prośba (dobra praktyka Framera): na Desktopie poza „Main” zostają tylko „Navi - Fixed” `GiaHsJO3X` i „lenis”
`nMDvE6f04`; wszystkie sekcje w „Main” `wUYfTPOi0`. Zachowanie i skalowanie bez zmian.
- Wcześniej „Main” był **przyklejony** (sticky top 0, stos poziomy, gap 10, overflow clip) i był celem przewijania
  **„hero”**; w środku tylko Hero. Sekcje (translateY −56, zIndex 1) przejeżdżały nad nim.
- Teraz: **Main** = zwykły pionowy stos strony (relative, gap 0, overflow visible, szer. 100%, minHeight 520 zostaje),
  dzieci: **Hero → Featured Projects → What We Do → Footer**. **Hero** `N06uDCvcg` przejął przyklejenie (sticky top 0,
  zIndex 0) i Scroll Section **„hero”** (link logo `/#hero` dalej działa). Sekcje bez zmian (translateY −56, zIndex 1).
- Efekt przewijania „Perspective Grid” `OirTRcAEZ` (Scroll Transform: cel „hero” → „projects”): cel przestawiony
  z Main na Hero (wszystkie breakpointy).
- Sprawdzone: pozycje sekcji na Desktopie identyczne co do piksela (Hero 0, Featured 800, What We Do 3396, Footer 4196);
  zrzuty całej strony na 3 breakpointach.
- Zasada: nowe sekcje `/` wstawiać do „Main” (po Hero), nie bezpośrednio do breakpointu.
- 2026-11-24 - „What We Do”: kadry **kwadratowe** (aspectRatio 1) we wszystkich 4 kolumnach („Media” `BRYavVKSY`,
  `ijOKlcSDs`, `GrFJK3O3U`, `Gtqtg26nf`) na Desktopie, Tablecie i Phone (Phone wcześniej 5:4).

## Kolekcja CMS „Projects” i lista na `/projects` (Framer, 2026-11-24)

Prośba: 6 projektów z arkusza w Figmie na stronę Projects we Framerze. Zmiany od razu w `main` (bez brancha), **nieopublikowane**.
- **Kolekcja „Projects”** `TpqN6PgHg` - pola wg tabeli „Dane CMS” (z separatorami Card / Home / Project page / SEO):
  Project name `HFchKKAAQ`, Slug `Bf6q983Gb` (z Project name), Title `qgpuV6WDb`, Category `eQ0IyN4Qu` (Option: Visual
  Identity `VA1GeXJ6C`, Art Direction `Y2sFLm6x8`, Motion & 3D `jtGZ06V5K`, Digital Experiences `b7OhyQmbP`, Space & Print
  `xf9beZIvU`), Year `BrBc5FKil`, Short description `xShrUeBFp`, Main image `w7Invwqgm`, Cover video `rtvzmXOGY` (MP4),
  Featured on Home `hzf_YoEG3`, Order `HnQdSUTkJ`, Home caption `cNFMWWNRJ`, Long description `qfEMx27Nt` (Formatted Text),
  Additional images `qBQIH4cZl` (List z polem Image `MHyOX44Fq`), Credits `hupGOox3I`, Project website `se0khTjZG`,
  SEO description `xufJ0Ukcr`, Social image `ArE2bbRWJ`.
- **6 wpisów** (treść jak w arkuszu Figmy, wzór sort-office.com): Department of Interest `jDYZzeTRw`, Beta Bar `ghY9NiekE`,
  EVAC x Our Legacy + ROA `mBpYigm6H`, Mycoaudio `PvTnbjtXf`, Nod Objects `hkwX48ete`, Letter Bet `absaBEcBR`; Order 1-6,
  SEO description = Short description, Featured on Home wyłączone, Cover video / Home caption / Credits / Project website /
  Social image puste. Zdjęcia: Main image + Additional images (łącznie 42) z alt-textami po angielsku, wgrane z adresów
  źródłowych (c-p.rmcdn.net) przez `tree.assetReference`.
- **Strona `/projects`** `RK_gmhXuR`, sekcja „projects” `J09QQV8My`: nowa lista CMS **„Project List (CMS)”** `LK791BIIc`
  (sortowanie Order rosnąco) → „Project Row” `r1XSFaNGa` → instancja „Wiersz projektu” `e0sRzCdfk`: numer = Order
  (2 cyfry), tytuł = Project name, zakres = Category (nazwa opcji), zdjęcie = Main image; na Phone wariant Phone.
  Stare wiersze z usługami (Service 01-05) najpierw ukryte, potem **usunięte** na prośbę użytkownika (2026-11-24);
  w sekcji zostały tylko „Section Bar” `Mop_e0NSp` i lista CMS.
- Linter: ostrzeżenie o braku maxWidth na sekcji `J09QQV8My` - sekcja celowo na całą szerokość (linie wierszy od krawędzi
  do krawędzi jak na `/`), zostawione bez zmian.
- Strona projektu „Project” `JJQ4pAWMy` (`/projects/[slug]`) - początek zrobiony 2026-11-25 (sekcja niżej). Linki z wierszy i z Featured projects - zrobione 2026-11-25.
- Tabela „Dane CMS” w Figmie: wiersz 13 Additional images - typ „List (Image)” (rozstrzygnięte: Framer ma pole List).

## Hover wiersza projektu - poprawki (`/projects`, 2026-11-24)

Użytkownik sam zrobił w komponencie „Wiersz projektu” `mKIi2lqmd` efekt hover wg nagrania (jasne tło wsuwa się z góry,
tekst ciemnieje): warstwa **„Hover fill”** `E2DUdvqEW` (absolute, token „Tekst”), wariant gestu **Hover** `r5PayVlbo`
(teksty Tytuł/Zakres w kolorze „Tło”), przejście tween 0,4 s. Ukrył też Numer i Miniaturę.
- **Mruganie tekstu** - przyczyna: „Hover fill” miał z-index 1 w spoczynku i 0 w Hover; Framer przełącza z-index bez
  animacji, więc przy zjechaniu myszką tło wskakiwało nad tekst. Poprawka: z-index 0 we wszystkich wariantach
  i warstwa przeniesiona na spód listy warstw.
- **Jasne paski na Tablecie/Phone** - przyczyna: w spoczynku wysokość tła wynikała z pinów Top −1 / Bottom 63 px, więc
  przy wierszu wyższym niż ~63 px (tytuł w 2 liniach) tło wychodziło na wierzch i zasłaniało jasny tekst. Poprawka:
  spoczynek Top −1, **wysokość 0 px** (bez pinu Bottom); Hover: Top −1 + Bottom 0 (cały wiersz).
- Ostrzeżenia lintera „zero height” (tło w spoczynku) i „brak nieprzezroczystego tła wariantu” - celowe, zostawione.
- Użytkownik zmienił w CMS nazwy: Department of Interest → **Interest**, EVAC x Our Legacy + ROA → **Our Legacy**;
  zsynchronizowane w arkuszu Figmy (Projekt 01 i 03). Lista na `/projects` ma teraz szerokość `1fr` (zmiana użytkownika).
- 2026-11-24 - **Kolor tekstu na hover jak w projekcie Ewy Dąbrowskiej** (prośba użytkownika; wzór: komponent „work” `GEthf1YJG`
  w projekcie Ewy, warstwa „wipe” - tylko odczyt, nic tam nie zmieniano). Technika: tło przycina zawartość (Overflow: Clip)
  i ma w środku **ciemną kopię tekstu** leżącą dokładnie na oryginale; tło przesuwając się odsłania kopię, więc kolor zmienia się
  na krawędzi tła (nie przez przenikanie). W „Wierszu projektu”:
  - użytkownik w międzyczasie zmienił tło na wjeżdżające: „Hover fill” spoczynek Top −64 px, wysokość 64 px; Hover Top 0;
  - w „Hover fill” nowa ramka **„Hover content”** `YecMTotpn` (absolute, Left 0, szer. 100%, stack poziomy jak wiersz: padding
    20/40, gap 24, środek) z kopiami **„Tytuł (hover)”** `S3VjatetE` i **„Zakres (hover)”** `OVym3OEzy` (te same zmienne
    komponentu i style tekstu, kolor „Tło”); Top 64 px w spoczynku i 0 w Hover - porusza się przeciwnie do tła, więc kopia
    stoi w miejscu; Phone: padding 16, gap 12, kopia zakresu ukryta;
  - wariant Hover: usunięta zmiana koloru oryginalnych tekstów; „Hover fill” z-index **2 we wszystkich wariantach** (nad
    tekstami, bez przełączania - inaczej jasny oryginał prześwitywał przez kopię).
- Do sprawdzenia przez użytkownika: animacja w podglądzie. Uwaga: wysokość tła 64 px pasuje do wierszy jednolinijkowych
  (Desktop); na Tablet/Phone wiersze są wyższe. Na `/projects` użytkownik buduje „Horizontal wrapper” (lista 1fr + ramka
  595 px) - na Tablet/Phone ramka 595 px ściska listę (na Phone lista niewidoczna); nie ruszane.
- 2026-11-24 - **„Zakres (hover)” jechał w bok na hover**: użytkownik zmienił szerokości oryginałów na Tytuł 2fr / Zakres 1fr
  (gap 0) i kopiom ustawił to samo tylko w wariancie Hover; w spoczynku kopie miały 1fr / 240 px, więc Framer animował
  szerokość. Poprawka: kopie `S3VjatetE` 2fr i `OVym3OEzy` 1fr także w Desktop (Hover ma te same wartości). **Zasada:**
  każda zmiana układu oryginalnych tekstów wiersza (szerokości, odstępy, padding) musi być powtórzona w „Hover content”
  w **obu** stanach (Desktop i Hover), inaczej kopia rozjedzie się z oryginałem.

## Sześcian projektów na `/projects` (2026-11-24)

Prośba: w miejscu prostokąta `Uc8gjSbE1` (240 × 240, prawy panel obok listy, w „Horizontal wrapper” `O9Gi3eY7d` zbudowanym
przez użytkownika) sześcian 3D, który po najechaniu na wiersz innego projektu obraca się o 90° w prawo lub w dół, a na
ścianie wychodzącej na front pokazuje zdjęcie główne tego projektu.
- Plik kodu **`SzescianProjektow.tsx`** (folder Assets → Kod), dwa eksporty:
  - komponent **„SzescianProjektow”** (instancja „Sześcian projektów” `b02hKELET` w ramce `Uc8gjSbE1`, która dostała nazwę
    „Cube”, przezroczyste tło, overflow visible; instancja 100% × 100%). Sześcian z 6 ścian (CSS 3D, kolor ścian #15181C,
    krawędzie rgba(255,255,255,0.12)), rozmiar z jednostek kontenera (cqmin), cofnięty o pół boku, więc front = rozmiar
    ramki. Stan orientacji to macierz 3×3; obrót „w prawo” = rotateY(+90°), „w dół” = rotateX(−90°) w osiach świata; na
    ścianę, która wyjdzie na front, wstawiane jest nowe zdjęcie z obrotem korygującym (zawsze prosto). Kontrolki: Zdjęcie
    startowe (ustawione: Main image 1. projektu), Kierunek (Losowo / Na przemian / W prawo / W dół; domyślnie Losowo),
    Czas obrotu (0,7 s), Kolor ścian, Krawędzie. Ten sam projekt ponownie = bez obrotu.
  - override **`withSzescianHover`** na instancji wiersza „Project” `e0sRzCdfk` w liście CMS: po najechaniu (i focusie)
    bierze z propsów instancji zdjęcie (pierwsza wartość z `src` = kontrolka Zdjęcie, podpięta pod Main image) i przekazuje
    je sześcianowi przez wspólny mały store w module (`createStore` z „framer” niedostępny w tym projekcie). Pierwszy
    zamontowany wiersz ustawia zdjęcie startowe. Wiersz owinięty w `div` z `display: contents` (zdarzenia myszy).
- Animacja i hover działają tylko w podglądzie / na opublikowanej stronie, nie na płótnie. Na Tablet/Phone sześcian jest
  przycinany przez wąską kolumnę z układu użytkownika.
- 2026-11-25 - **Ruch na start** (prośba użytkownika: „niech się lekko obraca, zanim najedzie się na któryś wiersz”):
  dopóki nikt nie najechał na żaden wiersz listy, sześcian łagodnie się kołysze (wychylenie w lewo/prawo ±18°,
  w górę/dół ok. ±8°, okres 9 s, płynny start 1,5 s) - zdjęcie zostaje z przodu, widać głębię bryły. Pierwsze najechanie
  na **dowolny** wiersz (także pierwszy projekt) płynnie (0,8 s) prostuje sześcian i wyłącza kołysanie na stałe (do
  przeładowania strony); dalej obroty jak dotąd. Technika: zewnętrzna warstwa z `translateZ(-50cqmin)` + obrót
  kołysania (sterowany `requestAnimationFrame`, bez re-renderów), wewnątrz sześcian z macierzą orientacji; w store
  nowa flaga `hovered` (ustawia override `withSzescianHover`). Nowe kontrolki: **Ruch na start** (domyślnie tak),
  **Wychylenie** (°), **Okres ruchu** (s). Na płótnie i przy „ogranicz ruch” w systemie - bez kołysania.
  Stan zastany: instancja `b02hKELET` jest teraz w „Cube Stage” `yJR6xOUDx` (prawa kolumna „Right” `k0rqSWoT9`,
  przebudowa użytkownika; dawna ramka `Uc8gjSbE1` już nie istnieje); override na wierszach `e0sRzCdfk` i `JDCbU_6LI`.
- 2026-11-25 - **„Napis prawy” `k_11UqrF3` uproszczony do 2 wariantów + zmienne** (prośba użytkownika: „za dużo
  wariantów”). Wszystkie 11 wariantów „Kwadrat N” różniło się od siebie niczym (każdy „See more” + strzałka), więc:
  - Warianty: **„Domyślny”** `j80GqzVEb` (+ hover jak dotąd) i **„Fokus”** `Q6mxb3i7d` (dawny „Kwadrat 1”, preset
    „Lista akapit”, strzałka widoczna). Pozostałe „Kwadrat 3...16” usunięte.
  - Zmienne komponentu: **„Tekst”** `AOc8AAI_I` (domyślnie „See our projects”, tekst w „Domyślnym”) i **„Tekst po
    kliknięciu”** `Tt9KdtaSE` (domyślnie „See more”, tekst w „Fokusie”) - teksty zmienia się w panelu instancji.
  - Kod: w `NapisyFokus.tsx` nowy override **`withNapisFokusWariant`** - przy kliknięciu dowolnej bryły ustawia wariant
    „Fokus” (animacja jak dotąd; klucz animacji bez numeru bryły, więc przy przejściu bryła → bryła napis się nie
    przeładowuje, bo tekst jest ten sam). Podpięty do instancji `LolOc7rF8` („/”) i `M2JjoZw2h` („/home”).
    Stary `withNapisFokus` („Kwadrat N”) zostaje dla „Napisu lewego” `A1gRbg7LO` (tam warianty mają różne tytuły brył).
  - Nowa bryła nie wymaga już nowego wariantu w „Napisie prawym” (tylko w lewym). Sprawdzone: Desktop bez zmian
    wizualnych, diagnostyki kodu czyste; Tablet/Phone - kolumny z napisami ukryte jak wcześniej.

- 2026-11-25 - **Napisy w komórkach wiersza projektu wyrównane, hover bez skoków** (prośba użytkownika, komponent
  „Wiersz projektu” `mKIi2lqmd`, `/projects`). Zmiany od razu w `main`, nieopublikowane.
  - Przyczyny skoków na hover: kopia w „Hover content” `YecMTotpn` miała kolumny w innej kolejności (Rok przed Zakresem),
    inne wcięcia (24 zamiast 32 px, dół 4 zamiast 8), „Zakres (hover)” 1fr tylko w wariancie Hover (animowana szerokość),
    a oryginalny „Zakres” `cTVLo9zRf` miał ręczne 11 px zamiast presetu.
  - Teraz kolumny w obu warstwach: Tytuł / Zakres / Rok; **Tytuł padding 0/16/8/40, etykiety (Zakres, Rok) 0/16/12/32** -
    dół 12 zamiast 8, żeby linia bazowa małych etykiet (preset „navi” 12 px) wypadała na linii bazowej tytułu („Lista
    akapit” 20/23 px); sprawdzone na zrzucie 1:1. Zakres też w presecie „navi”. Etykiety (oryginał i kopia) szerokość
    **1fr** we wszystkich wariantach - w wąskich kolumnach (Tablet) zawijają się zamiast wchodzić na linię. Kopia „Zakres
    col (hover)” dostała linię z prawej jak oryginał. Wariant Desktop: `borderWidth` 0 (linter „Border is incomplete”).
  - **Phone:** dotąd hover na telefonie przełączał na wariant „Hover” (układ Desktop). Nowy wariant **„Phone Hover”**
    `rAcWGQbfH` (z Phone; tło i kopia Top 0); Phone → Mouse Enter → Phone Hover, Phone Hover → Mouse Leave → Phone.
  - **Zasada bez zmian:** każda zmiana układu oryginalnych tekstów musi być powtórzona w „Hover content” (Desktop i Hover).
  - Poprawka tego samego dnia (nagranie użytkownika: „kategorie mrugają”): w wariancie Hover oryginalny „Zakres”
    `r5PayVlbocTVLo9zRf` miał własne nadpisanie stylu (ręczne 11 px bez presetu), a Desktop już preset „navi” - przy
    przełączeniu wariantu napis gasł. `resetOverrides` na tym węźle; sprawdzone, że wszystkie teksty wiersza mają ten sam
    preset, rozmiar i krycie w Desktop / Hover / Phone / Phone Hover (kopie różnią się tylko kolorem „Tło”).
    **Zasada:** styl tekstu zmieniać tylko w wariancie głównym (Desktop); w Hover nie nadpisywać fontu ani presetu.
  - Zastane: na `/projects` są dwie listy CMS („Project List (CMS)” i „– kopia” `e9f1RvEmA`, zmiana użytkownika), więc
    każdy projekt widać dwa razy - nie ruszane. Ostrzeżenia lintera „brak tła wariantu” i „-300 px odstępu” w Hover
    content (pomiar warstwy absolutnej) - zostawione.

- 2026-11-25 - **Kolejność kolumn na `/projects`: Tytuł | Kategoria | sześcian | Rok** (prośba użytkownika).
  - Komponent „Wiersz projektu”: nowa pusta komórka **„Cube col”** `v3zJJF85a` (2fr, linia z prawej #222) między Zakresem
    a Rokiem, i jej kopia **„Cube col (hover)”** `RIiuJi1Zw` w „Hover content” (linia rgba(0,0,0,0.12)); na Phone i Phone
    Hover obie ukryte. Proporcje wiersza: Tytuł 1fr / Kategoria 1fr / Cube 2fr / Rok 1fr.
  - Strona: „Project Lists” `dn3Pw0qhu` szerokość 1fr (cała szerokość). Kolumna **„Right”** `k0rqSWoT9` (z „Cube Stage”
    i sześcianem) przeniesiona do nowej nakładki **„Cube overlay”** `yKavc4ANa` (absolute na całym „Horizontal wrapper”,
    stack poziomy, `pointerEvents: none`, z-index 5 - hover i kliknięcia przechodzą do wierszy). W nakładce kolumny jak
    w wierszu, z tymi samymi paddingami: „Spacer (title)” `hNYALf_rm` 1fr pad 0/16/0/40, „Spacer (category)” `EnjSg2JAk`
    1fr pad 0/16/0/32, „Right” 2fr, „Spacer (year)” `qte6_7P5j` 1fr pad 0/16/0/32 - środek sześcianu = środek pustej
    komórki (sprawdzone Desktop i Tablet, ±2 px). **Zmiana paddingów komórek wiersza wymaga tej samej zmiany w spacerach
    nakładki.** Nakładka ukryta na Phone. Pionowa linia w „Right” `pvIiTHICH` ukryta (wypadałaby na środku kolumny).
  - Pozycja absolutna samego „Right” niemożliwa (Framer wymaga pinów w px, nie trzymałoby proporcji) - stąd nakładka.

## Puste 56 px pod stopką na `/` - usunięte (2026-11-24)

Przyczyna: Featured Projects, What We Do i Footer miały translateY −56 (pierwszy pasek wystaje nad dół Hero).
Przesunięcie nie zmniejsza miejsca w układzie, więc pod ostatnią sekcją zostawało 56 px (wcześniej zakrywał je
„Bottom Fill” w stopce, usunięty przez użytkownika).
- Teraz −56 ma **tylko pierwsza sekcja** (Featured Projects `HadJ76UFf`); jej padding dolny 80 → **24** (24 + 56 = te
  same 80 px odstępu do następnej sekcji). What We Do `NgsTpcy9z` i Footer `yVikSkj7m` bez translateY.
  Pasek „what we do” `tPIZgEwql`: sticky top 112 → **56** (wcześniej 112 kompensowało przesunięcie).
- Sprawdzone: stopka na ekranie w tym samym miejscu (y 3340), wysokość strony 4196 → 4140 (Desktop), wszystkie
  breakpointy.
- Zasada: kolejne sekcje w „Main” bez translateY; przesunięcie −56 tylko w pierwszej sekcji po Hero.
- Zastane: What We Do ukryta przez użytkownika (Visible off na wszystkich breakpointach) - nie ruszane.
- Przy okazji: kolumnom 01-02 w What We Do na Tablecie i Phone dopisany kolor obramowania (linter: „Border is incomplete”).

## Dolna część stopki dopracowana (`/`, 2026-11-24)

Prośba: „zrób ładnie dolną część stopki” („Footer Bar” `UmUPg4rLv`). Stan zastany: pasek 56 px bez linii, grupy
rozrzucone (logo i copyright 120 px od siebie, Connect 120 px od linków), pod paskiem 80 px paddingu stopki i reszta
z jej minHeight 100vh - pasek wisiał nad dołem strony.
- Pasek: **72 px**, linia górna 1 px token „Obrys” (jak pozostałe paski strony). Logo + copyright gap **24**
  (Tablet 16), linki + Connect gap **40** (Tablet 24). Kapsuła: obrys rgba(255,255,255,0.5).
- Pasek **na samym dole stopki**: Footer `yVikSkj7m` padding dolny 80 → **0**; „Section Heading” `bSDOGqGD1` (duże logo)
  wysokość **1fr** - wypełnia wolne miejsce stopki (minHeight 100vh), logo na środku; jej padding dolny 24 → 72
  (Phone 16 → 48).
- Phone: pasek w kolumnie, padding 32/16/28, gap 20 (kolejność bez zmian: linki → Connect → logo + copyright).
- Bez zmian: teksty, linki (TODO adresy profili), pasek „Section Bar” na górze stopki z napisem „featured projects”
  (zmiana użytkownika - do sprawdzenia, czy to właściwy napis dla stopki).

## Strona projektu z CMS `/projects/[slug]` - nagłówek i zdjęcie (2026-11-25)

Prośba: na stronie projektu z listy CMS pod navbarem tytuł, krótki opis, kategorie w ramce, pod spodem zdjęcie na całą
szerokość ekranu (inspiracja: strona projektu BVN - duży tytuł, chipy usług w cienkich ramkach, duże zdjęcie).
Zmiany od razu w `main` (bez brancha), **nieopublikowane**.
- Strona „Project” `JJQ4pAWMy`, szablon „Układ z paskiem” (Navi i stopka z szablonu). Breakpointy: Desktop `Ob89z3UFi`,
  Tablet `zzq6hyL6v`, Phone `OMyD7gpoX`.
- **„Project Header”** `RKMnzf5MN` (section, 100%, pionowy stos, gap 32; padding 64/40/48/40, Tablet 56/32/40/32 gap 28,
  Phone 40/16/32/16 gap 24):
  - „Intro” `CANax8HuG` (gap 20, Phone 16): **„Title”** `s7kB366cd` (h1, preset „Nagłówek” 64/42/32, pole CMS
    **Project name** - zmiana z pola Title tego samego dnia na prośbę użytkownika)
    i **„Short Description”** `SJg016FD2` (p, preset „Opis sekcji” 24/22/20, krycie 0,7, maxWidth 760, pole
    **Short description**).
  - **„Categories”** `kzNFtovaT` (stos poziomy z zawijaniem, gap 6) → **„Category Chip”** `Pu3oLUVSJ` (padding 10/14,
    ramka 1 px rgba(255,255,255,0.5) jak kapsuła w stopce, bez zaokrągleń) → tekst `FUGIahypO` (preset „navi”, pole
    **Category**, nazwa opcji). Projekt ma jedną kategorię - stos jest gotowy na więcej chipów, gdyby doszło pole wielokrotne.
- **„Main Image”** `idx6HeO5a`: bezpośrednio w breakpoincie, 100% szerokości (od krawędzi do krawędzi), wypełnienie =
  pole **Main image** (alt z CMS), proporcja **16:9** (Desktop, Tablet), **4:3** (Phone) - stała, żeby pionowe zdjęcia
  nie robiły bardzo wysokiej strony.
- Sprawdzone na zrzutach 3 breakpointów (Beta Bar, Letter Bet). Linter: „siblings too close” między nagłówkiem a zdjęciem -
  fałszywy alarm (odstęp daje dolny padding nagłówka), zostawione.
- Tabela „Dane CMS” w Figmie: kolumna „Gdzie widać” - Category i Short description mają teraz też „pełna strona”;
  Title już tylko „Karta” (na stronie projektu jest Project name).
- Zastane, nie ruszane: na Phone w Navi szablonu logo nachodzi na „ARCHIVE”.

