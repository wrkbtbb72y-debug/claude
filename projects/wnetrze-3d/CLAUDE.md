# Wnętrze 3D („Kubatura”)

<!-- Utworzone 2026-11-15. Krótki projekt — wystarczy ten plik. -->

Zasady wspólne (praca z Framerem, definition of done) są w głównym `CLAUDE.md` repozytorium.

- **Framer:** https://framer.com/projects/Bashful-Career--TrZY6V7hpIyWsOmfEYfW-dBvqu
  (project ID `TrZY6V7hpIyWsOmfEYfW`, nazwa w dashboardzie „Bashful Career”)
- **Produkcja / domena:** _TODO_ (nieopublikowane)
- **Język treści na stronie:** PL
- **Branche we Framerze:** edycje AI **nie tworzą brancha** (sprawdzone 2026-11-15) — zmiany idą
  od razu do `main`, nieopublikowane.

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
- 2026-11-15 — nazwa robocza w nawigacji „Kubatura” (do potwierdzenia/zmiany przez użytkownika).

## Do zrobienia

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
