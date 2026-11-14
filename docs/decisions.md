# Log decyzji

Format: data · decyzja · powód · status. Najnowsze na górze.
Status: ✅ przyjęte · 🟡 propozycja (czeka na akceptację) · ❌ odrzucone.

---

### 2026-11-14 · Źródło prawdy dla prac: `content/works.csv` → Framer CMS — 🟡
- **Decyzja:** Dane o pracach (tytuły, lata, materiały, opisy) edytujemy najpierw w
  `content/works.csv` w repo; Claude synchronizuje je do kolekcji CMS „Works” we Framerze.
  Zdjęcia żyją we Framerze (asset store), w CSV trzymamy ich nazwy/URL.
- **Powód:** historia zmian w git, możliwość masowych poprawek i generowania tekstów
  (opisy, alt-teksty, PL/EN) przez Claude, jedna kanoniczna lista do wniosków grantowych/CV.
- **Alternatywa:** CMS we Framerze jako jedyne źródło (prościej, jeśli treści będzie
  edytować artystka sama w Framerze) — wtedy CSV tylko jako okresowy eksport.

### 2026-11-14 · Język strony — 🟡
- **Do decyzji:** tylko EN vs PL/EN (lokalizacja Framera). Zob. content-guidelines.md.

### 2026-11-14 · Repo jako baza wiedzy, Framer jako źródło prawdy dla wyglądu — ✅
- **Decyzja:** Wygląd, layout i komponenty utrzymujemy wyłącznie we Framerze. Repo zawiera
  wiedzę, ustalenia, treści i dane. `docs/design-system.md` i `docs/framer-map.md` to
  mapy/snapshoty, aktualizowane po zmianach.
- **Powód:** Framer nie ma pamięci kontekstu między sesjami AI; repo daje Claude stały kontekst.

### (wcześniej) · Kierunek wizualny: ciemna galeria + duży szeryf + efekty scrolla — ✅
- Odtworzone ze stanu projektu. Powody/inspiracje: _TODO — dopisać, jeśli były ustalenia_.
