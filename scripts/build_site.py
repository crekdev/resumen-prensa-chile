#!/usr/bin/env python3
"""Arma la carpeta _site/ que se publica en GitHub Pages.

- index.html            -> última edición
- editions/YYYY-MM-DD.html -> archivo histórico (una por día hábil)
- editions/index.html   -> listado del archivo (generado aquí)
"""
import re, shutil, html
from pathlib import Path

root = Path(__file__).resolve().parent.parent
site = root / "_site"
if site.exists():
    shutil.rmtree(site)
(site / "editions").mkdir(parents=True)

shutil.copy(root / "index.html", site / "index.html")
(site / ".nojekyll").write_text("")

MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto",
         "septiembre","octubre","noviembre","diciembre"]
rows = []
for f in sorted((root / "editions").glob("????-??-??.html"), reverse=True):
    shutil.copy(f, site / "editions" / f.name)
    y, m, d = f.stem.split("-")
    txt = f.read_text(encoding="utf8")
    ed = re.search(r'class="edition">([^<]+)<', txt)
    lead = re.search(r'<p><span class="dropcap">(.)</span>(.*?)</p>', txt, re.S)
    resumen = ""
    if lead:
        resumen = re.sub(r"<[^>]+>", "", lead.group(1) + lead.group(2))
        resumen = html.escape(resumen[:220].rsplit(" ", 1)[0] + "…")
    rows.append(
        f'<li><a href="{f.name}"><strong>{int(d)} de {MESES[int(m)-1]} de {y}</strong>'
        f'{" · " + html.escape(ed.group(1)) if ed else ""}</a><p>{resumen}</p></li>'
    )

(site / "editions" / "index.html").write_text(f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Archivo — Resumen de Prensa Chile</title>
<style>
body{{font-family:Georgia,serif;background:#f2eee1;color:#211d16;max-width:760px;margin:2rem auto;padding:0 1.25rem}}
a{{color:#1c6b57}} h1{{margin-bottom:.2rem}} ul{{list-style:none;padding:0}}
li{{padding:1rem 0;border-bottom:1px solid #c7b998}} p{{margin:.4rem 0 0;color:#5c5643;font-size:.95rem}}
@media (prefers-color-scheme:dark){{body{{background:#17140f;color:#ece4d1}}a{{color:#7ecdb3}}li{{border-color:#4a4230}}p{{color:#b8ad91}}}}
</style></head><body>
<p><a href="../">← Última edición</a></p>
<h1>Archivo de ediciones</h1>
<ul>{''.join(rows)}</ul>
</body></html>""", encoding="utf8")
print(f"OK: {len(rows)} ediciones en {site}")
