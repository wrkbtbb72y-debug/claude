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

## Struktura (Home `augiA20Il`, `/`)

Breakpointy: Desktop `WQLkyLRf1` (1200), Tablet `yQMtFz1Ve` (810), Phone `sg8iiRp42` (390).

- **Ekran** `N06uDCvcg` — stack pionowy, `100vh` (min 520px), pełna szerokość (celowo bez maxWidth).
  - **Nawigacja** `GTrNEG7XB` — 64px (Phone 56px): znak „Kubatura” + wskazówka
    „Poruszaj kursorem, aby się rozejrzeć” `pvlTW1vEa` (ukryta na Tablet/Phone).
  - **Wnętrze 3D** `Hohropvqf` — komponent kodowy `Wnetrze3D.tsx`, wysokość `1fr`.
  - **Panel sterowania** `xHih95kf6` — „Dodaj bryłę” `A8IrKWoZJ` (ukryte na Phone) + przyciski
    `vmmVh1mwZ`: Koło `O9pkhZJRu`, Kwadrat `gcLtVqWZ1`, Głaz `kPExmBcjU`.

## Jak to działa (kod)

- `Wnetrze3D.tsx` — własny renderer linii na `<canvas>` (bez bibliotek): perspektywa, przycinanie
  linii za kamerą, fizyka spadania, „mgła” (dalsze linie gasną w ciemności). Kontrolki: kolory (tło,
  linie, bryły), grubość, wymiary sali (domyślnie 44 × 72 m, wys. 16 m), wys. oczu (2,6 m),
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
- 2026-11-15 — nazwa robocza w nawigacji „Kubatura” (do potwierdzenia/zmiany przez użytkownika).

## Do zrobienia

- [ ] Potwierdzić nazwę w nawigacji („Kubatura” jest robocza) i ewentualne linki w nawigacji.
- [ ] Kolejne przyciski w dolnym pasku (np. „Wyczyść” — override `withWyczysc` jest gotowy).
- [ ] Sprawdzić działanie w podglądzie Framera (kliknięcia, ruch kursora) — z poziomu AI widać
      tylko statyczne screenshoty.
