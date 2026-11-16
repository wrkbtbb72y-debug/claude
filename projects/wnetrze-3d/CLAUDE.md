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
  - Koło: **geoida** (zmiana 2026-11-16) — wyraźnie kula, ale z miękkimi wybrzuszeniami
    i wklęsłościami (±6–17% promienia), lekko spłaszczona lub wydłużona, promień 2,6–6 m;
    wcześniejsze warianty (dysk, igła, torus, plastry) usunięte na prośbę użytkownika;
  - Kwadrat: cienki monolit (do ~85% wysokości sali), długa przechylona belka, skręcony graniastosłup,
    tesserakt (sześcian w sześcianie), rozpadający się sześcian (krawędzie odsunięte od siebie);
  - Głaz: zdeformowany głaz, odłamki zawieszone w powietrzu, kryształ z wyrwanymi wierzchołkami.
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

### Jak spadają bryły (od 2026-11-16)

- **Pierwsza bryła** spada w snop światła i ląduje na podłodze. Przy uderzeniu jej **dolna część
  lekko się odkształca** (rozpłaszcza i rozszerza w dolnych ~35% wysokości, sprężyste drgnięcie,
  potem zostaje niewielkie trwałe spłaszczenie).
- **Druga i trzecia** nie dotykają podłogi — spadają na pierwszą i **wbijają się w nią**
  (zatrzymują się z dolną częścią zagłębioną na 25–45% wysokości). Ich środek jest **lekko
  przesunięty** względem środka pierwszej (10–25% jej promienia), trzecia wchodzi z przeciwnej
  strony niż druga. Bryły z rodziny „Kwadrat” wchodzą ukośnie jak ostrze (przechył 20–40°),
  pozostałe z lekkim przechyłem; nie są dużo większe od pierwszej (max 1,25× jej rozmiaru)
  i zawsze mieszczą się pod sufitem. Lewitowanie brył usunięte.
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

### Kamera „na linii horyzontu” (zmiana spoza sesji z Claude, zauważona 2026-11-16)

W kodzie `Wnetrze3D.tsx` ktoś zmienił kamerę: jest **nieruchoma, frontalna, z okiem na poziomie
podłogi** — cała podłoga zlewa się w jedną prostą linię (horyzont), na której stają bryły.
Wysokość tej linii na ekranie ustawia nowa kontrolka **„Linia”** (`horizon`, domyślnie 0,68).
Ruch kursorem i dryf kamery w tej wersji nie obracają widoku. Wymiary sali na instancji:
34 × 89 m, wys. 13,5 m. Kontrolka „Wys. oczu” nie jest już używana. Zmiany zachowane.

## Struktura (Home `augiA20Il`, `/`)

Breakpointy: Desktop `WQLkyLRf1` (1200), Tablet `yQMtFz1Ve` (810), Phone `sg8iiRp42` (390).

- **Ekran** `N06uDCvcg` — stack pionowy, `100vh` (min 520px), pełna szerokość (celowo bez maxWidth).
  - **Nawigacja** `GTrNEG7XB` — 64px (Phone 56px): znak „Kubatura” + wskazówka
    „Poruszaj kursorem, aby się rozejrzeć” `pvlTW1vEa` (ukryta na Tablet/Phone).
  - **Wnętrze 3D** `Hohropvqf` — komponent kodowy `Wnetrze3D.tsx`, wysokość `1fr`.
  - **Panel sterowania** `xHih95kf6` — „Dodaj bryłę” `A8IrKWoZJ` (ukryte na Phone) + przyciski
    `vmmVh1mwZ` (override `withPrzyciskiBryl`): Koło `O9pkhZJRu`, Kwadrat `gcLtVqWZ1`, Głaz `kPExmBcjU`;
    „Nadaj kształt” `ZqJgdZL2N` (`withNadajKsztalt`), „Od nowa” `C6hHtDu5I` (`withOdNowa`).
    Etykieta panelu `A8IrKWoZJ` ma override `withEtykietaPanelu` (tekst zależny od etapu).

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
- Tekst (PP Neue Montreal): Znak (17/600), Etykieta (14/400), Podpis (13/400, kolor drugorzędny).
- Komponent **Przycisk akcji** `HAR1CjvV6`: warianty Główny (jasny) / Drugorzędny + hover i pressed,
  zmienna „Etykieta”. Preset tekstu „Etykieta akcji” (14/600, kolor Tło).
- Komponent **Przycisk bryły** `IhvcEuszi`: warianty Koło / Kwadrat / Głaz (różnią się ikoną SVG
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
- 2026-11-15 — nazwa robocza w nawigacji „Kubatura” (do potwierdzenia/zmiany przez użytkownika).

## Do zrobienia

- [ ] Potwierdzić, czy zostaje przycisk „Od nowa” (dodany z własnej inicjatywy).
- [ ] Inspiracje od użytkownika (2026-11-15) jeszcze niewykorzystane w pełni: wklęsła czerwona
      połówka dysku, kamienie rozsypane na podłodze, kilka długich świetlików, skośne słupy.

- [ ] Potwierdzić nazwę w nawigacji („Kubatura” jest robocza) i ewentualne linki w nawigacji.
- [ ] Kolejne przyciski w dolnym pasku (np. „Wyczyść” — override `withWyczysc` jest gotowy).
- [ ] Sprawdzić działanie w podglądzie Framera (kliknięcia, ruch kursora) — z poziomu AI widać
      tylko statyczne screenshoty.
