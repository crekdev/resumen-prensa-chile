# Resumen de Prensa Chile

Resumen diario (lunes a viernes) de prensa chilena: noticias que se repiten entre medios, contraste de enfoques,
innovación/startups, investigación y transparencia, opinión, y un "Pulso social" con encuestas y reacciones ciudadanas.

Sitio estático (HTML/CSS puro, sin build ni dependencias) publicado con **GitHub Pages**.

## Medios monitoreados (17)

Radio U. de Chile · Diario Financiero · CIPER Chile (Radar) · Interferencia · Ethic · El Mostrador · BioBioChile ·
El Ciudadano · CEP Chile · El Desconcierto · Emol · El Dínamo · Reportea · CNN Chile · 24 Horas ·
El País (solo contenido sobre Chile) · Publimetro

## Estructura

| Ruta | Qué es |
|---|---|
| `index.html` | Última edición (es lo que se ve en la raíz del sitio) |
| `editions/AAAA-MM-DD.html` | Archivo histórico: una edición por día hábil |
| `scripts/build_site.py` | Arma `_site/` y genera el listado `editions/index.html` |
| `.github/workflows/pages.yml` | Deploy automático a GitHub Pages en cada push a `main` |
| `ROUTINE_PROMPT.md` | Prompt de la tarea programada que genera y sube cada edición |

## Deploy (una sola vez)

1. En GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Haz push a `main` (o ejecuta el workflow manualmente en la pestaña *Actions*).
3. El sitio queda en `https://<tu-usuario>.github.io/resumen-prensa-chile/`.

Probar en local:

```bash
python3 scripts/build_site.py
python3 -m http.server -d _site 8000   # http://localhost:8000
```

## Actualización diaria

Una tarea programada corre de **lunes a viernes a las 10:30 (hora de Chile)**. Cada corrida investiga las 17 portadas,
reescribe `index.html`, guarda una copia en `editions/AAAA-MM-DD.html` y hace commit + push a `main`;
el workflow redeploya el sitio automáticamente. El detalle está en `ROUTINE_PROMPT.md`.

## Notas de contenido

- Curaduría y síntesis generadas automáticamente a partir de portadas públicas; cada afirmación enlaza a su fuente.
- El "Pulso social" usa encuestas y reportes de terceros con fuente citada; no hace scraping directo de Reddit ni X.
