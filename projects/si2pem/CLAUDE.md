# SI2PEM

<!-- Utworzone 2026-11-19. Projekt prowadzony w Figmie (bez Framera). Pola TODO uzupełnić
     z użytkownikiem — nie zgadywać. -->

Zasady wspólne (definition of done, zasady treści) są w głównym `CLAUDE.md` repozytorium.
Ścieżki w tym pliku są względem tego folderu.

- **Figma:** https://www.figma.com/design/kiuBZ1fA0OMqFDdPuhmnHy/SI2PEM (fileKey `kiuBZ1fA0OMqFDdPuhmnHy`)
- **Framer:** brak (projekt tylko w Figmie)
- **Zadanie w GitLabie:** link w nagłówku strony Figmy „zgłoś problem z zasięgiem”
- **Klient / produkcja / termin:** _TODO_

## O projekcie

System Informacyjny o Instalacjach wytwarzających Promieniowanie ElektroMagnetyczne — serwis
z mapą natężenia PEM, planowanymi pomiarami, zgłoszeniami instalacji, statystykami.
Fonty: Raleway (UI), Hind (część nagłówka). Siatka desktop: 1440, marginesy 96.

## Mapa Figmy — strona „zgłoś problem z zasięgiem” (`12729:122`)

| Węzeł | Co to |
|---|---|
| `12735:233` | **Niezalogowany — Propozycja 1** — desktop 1440 (mapa 2/3 + usługi 1/3, 3 karty) — x 2048 |
| `12778:156` | **… — Tablet 810** (2026-11-19) — x 3600 |
| `12779:216` | **… — Mobile 390** (2026-11-19) — x 4510 |
| `12780:293` | **… — Tablet 810 — wariant I** — usługi w 1 rzędzie (3× „Usługa – karta”) — x 3600, y 4500 |
| `12780:463` | **… — Tablet 810 — wariant II** — „Zgłoś problem z zasięgiem” na całą szerokość, pod nim 2 kafelki w rzędzie — x 4510, y 4500 |
| `10059:15984` | „Niezalogowany” — wcześniejsza wersja desktop |
| `12754:4141` / `12754:4144` | „tablet screen” / „mobile screen” — zrzuty obecnej strony (wzór układu kart) |
| `12764:5199` | „MObile” — starsza makieta mobile (z niej baner mapy `12764:5245`) |
| `12764:5707` | „Main new tablet 4” — starsza makieta tablet (834) |
| `12734:229` | Komponenty — kafelek usługi: „Usługa – element” `12734:245`, „Usługa – karta” `12745:509`, „Karta informacyjna – kompaktowa”, „Usługa – karta (strzałka na dole)” `12782:419` |
| `12777:156` | Komponenty — karta sekcji (responsywna): **„Karta sekcji – responsywna”** `12777:158` |

Inne komponenty: nagłówek — zestaw „Frame 427318310” `9329:4788` (Default 1440, Variant3 1440
— używany na desktopie, Variant2 390 — mobile; **brak wariantu tablet**).

## Ustalenia i decyzje

- 2026-11-19 — Wersje Tablet 810 i Mobile 390 Propozycji 1. Karty dolne wg zrzutów obecnej
  strony: tablet — Aktualności na pełną szerokość (778×444), pod nią Statystyki + PEM w dwóch
  kolumnach (odstęp 28); mobile — trzy karty jedna pod drugą (358×440, odstęp 24, tytuł 22).
  Marginesy boczne 16.
- 2026-11-19 — Karty zbudowane na nowym lokalnym komponencie „Karta sekcji – responsywna”
  (auto-layout, właściwości Tytuł/Opis, obraz w warstwie „Obraz” w trybie Fill). Desktopowe
  karty zostały bez zmian (stare komponenty „4736”, „Frame 427318325” i ramka „4734”).
- 2026-11-19 — Nagłówek tabletu to **odłączona** kopia wariantu desktop (Variant3) dopasowana
  do 810, bo zestaw nie ma wariantu tablet. Mobile używa instancji Variant2.
- 2026-11-19 — Baner mapy na mobile = kopia banera ze starszej makiety „MObile” z tekstami
  z desktopu (tytuł „Mapa natężenia pola elektromagnetycznego (PEM)”, przycisk „Przejdź do Mapy PEM”).
- 2026-11-19 — Baner mobile (`12779:240`, 358×470) przerobiony wg screena obecnej strony: tekst
  i przycisk na górze, mapa z plakietką „Pole elektromagnetyczne” na dole, przycięta dolną krawędzią;
  tło przyciemnione do granatu (#2E2E5A, warstwa „Przyciemnienie tła”). Stare nakładki dolnego
  pola tekstowego („xcx”, „TEKST Z TŁEM”) ukryte, nie usunięte. Tekst pozostał z desktopu (z „(PEM)”).
- 2026-11-19 — Usługi (3 kafelki „Usługa – element”) na tablecie i mobile: jedna pod drugą,
  pełna szerokość. Stopka: tablet — logotypy w 2 rzędach (3+2); mobile — linki i logotypy
  zawijane, logotypy w skali 70%.

- 2026-11-19 — Na prośbę użytkownika dwa alternatywne układy usług na tablecie (do wyboru):
  I — trzy obok siebie, na komponencie „Usługa – karta” `12745:509` (ikona nad tytułem; poziomy
  „Usługa – element” jest za szeroki na ~251 px), karty 251×196; II — „Zgłoś problem
  z zasięgiem” 778×90, pod nim Planowane pomiary + Zgłoszenia instalacji (2× 383×90).
  Reszta strony identyczna jak w podstawowej wersji tabletu.
- 2026-11-19 — Wariant I: kafelki usług przełączone na nowy komponent „Usługa – karta (strzałka
  na dole)” `12782:419` (kopia „Usługa – karta”; strzałka bez ramki, 24 px, w prawym dolnym rogu).
  Oryginalny wzorzec „Usługa – karta” bez zmian. Kafelki 251×232.

## Do zrobienia

- [ ] Użytkownik wybiera układ usług na tablecie: podstawowy (stos) / wariant I / wariant II.

- [ ] Ewentualnie dodać wariant „Tablet” do zestawu nagłówka `9329:4788` (na prośbę użytkownika)
  i podmienić odłączony nagłówek tabletu na instancję.
- [ ] Ujednolicić kolory tytułów kart na desktopie (Aktualności/Statystyki #3C3C95, PEM #5133A0) — do decyzji.
