#!/usr/bin/env python3
"""Biblioteka inspiracji — dodawanie wpisów i budowanie mapy.

Użycie (z katalogu głównego repo):

  python3 inspiracje/narzedzia/inspiracje.py dodaj \
      --obraz /sciezka/screen.png --url https://strona.pl \
      --kategoria nawigacja --tytul "Menu pełnoekranowe z dużą typografią" \
      [--tagi minimalizm,czarno-białe] [--notatka "co się podoba"] \
      [--projekt ewa-dabrowska] [--strona "Nazwa strony"]

  python3 inspiracje/narzedzia/inspiracje.py zbuduj
      → przebudowuje MAPA.md i mapa.html (wywoływane też automatycznie po `dodaj`)

  python3 inspiracje/narzedzia/inspiracje.py artefakt --wyjscie /tmp/.../atlas-inspiracji.html
      → samodzielna wersja mapy (obrazy wbudowane) do opublikowania jako Artifact

  python3 inspiracje/narzedzia/inspiracje.py sprawdz
      → kontrola spójności katalogu (brakujące pliki, nieznane kategorie, sieroty)
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import io
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageOps

BAZA = Path(__file__).resolve().parent.parent  # inspiracje/
KATALOG = BAZA / "katalog.json"
OBRAZY = BAZA / "obrazy"
SZABLON = BAZA / "narzedzia" / "szablon.html"
MAPA_MD = BAZA / "MAPA.md"
MAPA_HTML = BAZA / "mapa.html"

MAKS_SZER = 1600          # szerokość zapisywanego screena (px)
MAKS_WYS = 6000           # bardzo długie screeny całych stron są przycinane od góry
LIMIT_ARTEFAKTU = 12_000_000  # bajtów; poniżej limitu 16 MB z zapasem


def wczytaj() -> dict:
    return json.loads(KATALOG.read_text(encoding="utf-8"))


def zapisz(kat: dict) -> None:
    KATALOG.write_text(json.dumps(kat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slug(tekst: str, maks: int = 40) -> str:
    t = unicodedata.normalize("NFKD", tekst.replace("ł", "l").replace("Ł", "L"))
    t = t.encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    if len(t) > maks:
        t = t[:maks + 1].rsplit("-", 1)[0] if "-" in t[:maks + 1] else t[:maks]
    return t.strip("-") or "wpis"


def domena(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def zapisz_obraz(zrodlo: Path, cel: Path) -> None:
    img = Image.open(zrodlo)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        tlo = Image.new("RGB", img.size, (255, 255, 255))
        tlo.paste(img, mask=img.split()[-1])
        img = tlo
    else:
        img = img.convert("RGB")
    if img.width > MAKS_SZER:
        img = img.resize((MAKS_SZER, round(img.height * MAKS_SZER / img.width)), Image.LANCZOS)
    if img.height > MAKS_WYS:
        img = img.crop((0, 0, img.width, MAKS_WYS))
    cel.parent.mkdir(parents=True, exist_ok=True)
    img.save(cel, "JPEG", quality=85, optimize=True, progressive=True)


def cmd_dodaj(a) -> None:
    kat = wczytaj()
    slugi = {k["slug"] for k in kat["kategorie"]}
    if a.kategoria not in slugi:
        sys.exit(f"Nieznana kategoria „{a.kategoria}”. Dostępne: {', '.join(sorted(slugi))}")
    zrodlo = Path(a.obraz)
    if not zrodlo.is_file():
        sys.exit(f"Brak pliku obrazu: {zrodlo}")

    dzis = a.data or dt.date.today().isoformat()
    dom = domena(a.url) if a.url else "bez-linku"
    baza_id = f"{dzis.replace('-', '')}-{slug(dom, 24)}-{slug(a.tytul, 32)}"
    istniejace = {w["id"] for w in kat["wpisy"]}
    wid, n = baza_id, 2
    while wid in istniejace:
        wid, n = f"{baza_id}-{n}", n + 1

    cel = OBRAZY / a.kategoria / f"{wid}.jpg"
    zapisz_obraz(zrodlo, cel)

    wpis = {
        "id": wid,
        "dodano": dzis,
        "kategoria": a.kategoria,
        "tytul": a.tytul,
        "strona": a.strona or dom,
        "url": a.url or "",
        "obraz": cel.relative_to(BAZA).as_posix(),
        "tagi": [t.strip().lower() for t in (a.tagi or "").split(",") if t.strip()],
        "notatka": a.notatka or "",
        "projekty": [p.strip() for p in (a.projekt or "").split(",") if p.strip()],
    }
    kat["wpisy"].append(wpis)
    zapisz(kat)
    print(f"Dodano: {wid}  →  {wpis['obraz']}")
    cmd_zbuduj(None)


# ---------- budowanie mapy ----------

def posortowane(kat: dict) -> list[dict]:
    return sorted(kat["wpisy"], key=lambda w: (w["dodano"], w["id"]), reverse=True)


def zbuduj_md(kat: dict) -> str:
    wpisy = posortowane(kat)
    lin = [
        "# Mapa inspiracji",
        "",
        "<!-- Plik generowany automatycznie przez narzedzia/inspiracje.py — nie edytuj ręcznie. -->",
        "",
        f"**{len(wpisy)}** elementów w **{sum(1 for k in kat['kategorie'] if any(w['kategoria']==k['slug'] for w in wpisy))}** kategoriach. "
        "Pełna, interaktywna wersja: `mapa.html` (oraz Artifact — link w `CLAUDE.md`).",
        "",
        "| Kategoria | Liczba |",
        "|---|---:|",
    ]
    for k in kat["kategorie"]:
        n = sum(1 for w in wpisy if w["kategoria"] == k["slug"])
        lin.append(f"| [{k['nazwa']}](#{k['slug']}) | {n} |")
    lin.append("")
    for k in kat["kategorie"]:
        grupa = [w for w in wpisy if w["kategoria"] == k["slug"]]
        if not grupa:
            continue
        lin += [f'<a id="{k["slug"]}"></a>', f"## {k['nazwa']} ({len(grupa)})", "", f"_{k['opis']}_", "", "<table>"]
        for i in range(0, len(grupa), 3):
            lin.append("<tr>")
            for w in grupa[i:i + 3]:
                obraz = html.escape(w["obraz"])
                tytul = html.escape(w["tytul"])
                link = (f'<a href="{html.escape(w["url"])}">{html.escape(w["strona"])}</a>'
                        if w["url"] else html.escape(w["strona"]))
                tagi = " ".join(f"`{html.escape(t)}`" for t in w["tagi"])
                lin.append(
                    f'<td width="33%" valign="top"><a href="{obraz}"><img src="{obraz}" width="280" alt="{tytul}"></a>'
                    f"<br><b>{tytul}</b><br>{link}<br><sub>{w['dodano']}</sub> {tagi}</td>"
                )
            lin.append("</tr>")
        lin += ["</table>", ""]
    return "\n".join(lin) + "\n"


def zbuduj_html(kat: dict, obrazy: dict[str, str] | None = None) -> str:
    """obrazy: mapa id → src (data URI) dla wersji artefaktu; None = ścieżki względne."""
    wpisy = []
    for w in posortowane(kat):
        w = dict(w)
        w["src"] = obrazy[w["id"]] if obrazy else w["obraz"]
        wpisy.append(w)
    dane = json.dumps({"kategorie": kat["kategorie"], "wpisy": wpisy}, ensure_ascii=False)
    dane = dane.replace("</", "<\\/")
    return SZABLON.read_text(encoding="utf-8").replace("/*__DANE__*/null", dane)


def cmd_zbuduj(_a) -> None:
    kat = wczytaj()
    MAPA_MD.write_text(zbuduj_md(kat), encoding="utf-8")
    strona = zbuduj_html(kat)
    # wersja w repo: pełny dokument, żeby otwarta lokalnie nie szła w quirks mode
    MAPA_HTML.write_text(
        '<!doctype html>\n<html lang="pl"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + strona + "\n</html>\n",
        encoding="utf-8",
    )
    print(f"Zbudowano {MAPA_MD.relative_to(BAZA.parent)} i {MAPA_HTML.relative_to(BAZA.parent)} "
          f"({len(kat['wpisy'])} wpisów)")


def data_uri(sciezka: Path, szer: int, jakosc: int) -> str:
    img = Image.open(sciezka).convert("RGB")
    if img.width > szer:
        img = img.resize((szer, round(img.height * szer / img.width)), Image.LANCZOS)
    if img.height > szer * 3:
        img = img.crop((0, 0, img.width, szer * 3))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=jakosc, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def cmd_artefakt(a) -> None:
    kat = wczytaj()
    for szer, jakosc in ((1100, 80), (900, 74), (720, 68), (560, 62), (440, 58)):
        obrazy = {w["id"]: data_uri(BAZA / w["obraz"], szer, jakosc) for w in kat["wpisy"]}
        strona = zbuduj_html(kat, obrazy)
        if len(strona.encode()) <= LIMIT_ARTEFAKTU:
            break
    else:
        print("UWAGA: mapa przekracza limit nawet przy najmniejszych obrazach — "
              "czas podzielić artefakt (np. osobny na kategorię).", file=sys.stderr)
    wyj = Path(a.wyjscie)
    wyj.parent.mkdir(parents=True, exist_ok=True)
    wyj.write_text(strona, encoding="utf-8")
    print(f"Artefakt: {wyj} ({len(strona.encode()) / 1e6:.1f} MB, obrazy {szer}px q{jakosc})")


def cmd_sprawdz(_a) -> None:
    kat = wczytaj()
    slugi = {k["slug"] for k in kat["kategorie"]}
    bledy = []
    ids = set()
    for w in kat["wpisy"]:
        if w["id"] in ids:
            bledy.append(f"powtórzone id: {w['id']}")
        ids.add(w["id"])
        if w["kategoria"] not in slugi:
            bledy.append(f"{w['id']}: nieznana kategoria {w['kategoria']}")
        if not (BAZA / w["obraz"]).is_file():
            bledy.append(f"{w['id']}: brak pliku {w['obraz']}")
        if not w.get("tytul"):
            bledy.append(f"{w['id']}: brak tytułu")
    uzyte = {w["obraz"] for w in kat["wpisy"]}
    for p in OBRAZY.rglob("*"):
        if p.is_file() and p.name != ".gitkeep" and p.relative_to(BAZA).as_posix() not in uzyte:
            bledy.append(f"plik bez wpisu: {p.relative_to(BAZA)}")
    print("\n".join(bledy) if bledy else f"OK — {len(kat['wpisy'])} wpisów, brak problemów.")
    sys.exit(1 if bledy else 0)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("dodaj")
    d.add_argument("--obraz", required=True)
    d.add_argument("--url", default="")
    d.add_argument("--kategoria", required=True)
    d.add_argument("--tytul", required=True)
    d.add_argument("--strona")
    d.add_argument("--tagi")
    d.add_argument("--notatka")
    d.add_argument("--projekt")
    d.add_argument("--data", help="YYYY-MM-DD, domyślnie dziś")
    d.set_defaults(f=cmd_dodaj)
    sub.add_parser("zbuduj").set_defaults(f=cmd_zbuduj)
    ar = sub.add_parser("artefakt")
    ar.add_argument("--wyjscie", required=True)
    ar.set_defaults(f=cmd_artefakt)
    sub.add_parser("sprawdz").set_defaults(f=cmd_sprawdz)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
