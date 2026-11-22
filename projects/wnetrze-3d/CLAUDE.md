# Wnętrze 3D („Kubatura”)

<!-- Utworzone 2026-11-15. Krótki projekt — wystarczy ten plik. -->

Zasady wspólne (praca z Framerem, definition of done) są w głównym `CLAUDE.md` repozytorium.

- **Framer:** https://framer.com/projects/Bashful-Career--TrZY6V7hpIyWsOmfEYfW-dBvqu
  (project ID `TrZY6V7hpIyWsOmfEYfW`, nazwa w dashboardzie „Bashful Career”)
- **Produkcja / domena:** _TODO_ (nieopublikowane)
- **Język treści na stronie:** PL
- **Branche we Framerze:** edycje AI **nie tworzą brancha** (sprawdzone 2026-11-15) — zmiany idą
  od razu do `main`, nieopublikowane.

## Słownik (terminy uzgodnione z użytkownikiem)

- **Punkt zbiegu** (2026-11-19) — punkt, do którego zbiegają się linie siatki biegnące w głąb (oś z) w `SiatkaPerspektywy.tsx`
  (w kodzie `vx`, `vy` / `entry.cam`; położenie ustawiają kontrolki „Punkt zbiegu” = X i „Horyzont” = Y). Na `/` leży przy
  dolnej krawędzi siatki (Horyzont 0). Używać tej nazwy w rozmowie i notatkach.

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
