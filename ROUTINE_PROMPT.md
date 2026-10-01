# Prompt de la tarea programada (Lun–Vie 10:30 America/Santiago)

> Pegar completo como prompt de la tarea. Requiere que la sesión tenga acceso de escritura al repo
> `resumen-prensa-chile` en GitHub (conector GitHub vinculado).

Genera la edición de hoy del "Resumen de Prensa Chile". Sesión no atendida: no hagas preguntas, usa criterio razonable.

1. Revisa hoy las portadas de estas 17 fuentes con WebFetch (en paralelo), pidiendo titulares de Política, Sociedad,
   Innovación/Startups y Pensamiento/Opinión con título, descripción de 1 línea y link directo:
   radio.uchile.cl, df.cl, ciperchile.cl/radar-2, interferencia.cl, ethic.es, elmostrador.cl, biobiochile.cl,
   elciudadano.com/chile, cepchile.cl/noticias, eldesconcierto.cl, emol.com, eldinamo.cl, reportea.cl, cnnchile.com,
   24horas.cl, elpais.com/chile (SOLO piezas sobre Chile), publimetro.cl.
   Reportea publica poco: si no hay nada de hoy, usa su pieza más reciente.
2. Identifica 3-5 noticias repetidas entre medios; por cada una, 3 puntos (hasta 4) de contraste de enfoque con links inline.
3. Agrega ítems de Innovación y Startups, Investigación & Transparencia (Reportea/CIPER) y Pensamiento y Opinión.
4. Párrafo "lead" de 2-3 líneas.
5. Sección "Pulso social": reddit.com y x.com están bloqueados — no insistas. Usa WebSearch sin allowed_domains para
   encuestas (Criteria, Cadem, Pulso Ciudadano), análisis de escucha social con cifras y notas de medios chilenos sobre
   reacciones ciudadanas. 3-4 tarjetas + barra de sentimiento si hay porcentajes. Si no hay nada confiable, omite la sección.
6. Clona el repo (usa el token de GitHub de la sesión), parte del `index.html` actual y edítalo preservando CSS/diseño
   (Fraunces + Source Sans 3 + IBM Plex Mono; oxblood/navy/forest sobre papel). Actualiza: N.º de edición (+1), fecha,
   conteo de medios (17), lead, historias, briefs, Pulso social, "Próxima edición" (próximo día hábil) y colophon.
7. Guarda el resultado como `index.html` y como copia `editions/AAAA-MM-DD.html` (fecha de hoy, hora de Chile).
8. `git add index.html editions/ && git commit -m "Edición N.º <n> — <fecha>" && git push origin main`.
   El workflow de Pages redeploya solo. Si hoy ya existe `editions/AAAA-MM-DD.html`, sobrescríbelo (re-ejecución) y
   conserva el N.º de edición de esa fecha en vez de sumarle 1 (el +1 del paso 6 aplica solo a una fecha nueva).
   Si el push falla (red, permisos o conflicto), haz `git pull --rebase origin main` y reintenta una vez; si vuelve a
   fallar, detente y reporta el error exacto.
9. NO publiques ni edites ningún Artifact: el repo y su sitio de GitHub Pages son el único destino de la edición.
10. Cierra con 2-3 líneas: confirmación (N.º de edición y fecha) + link al sitio de Pages
    (https://crekdev.github.io/resumen-prensa-chile/). Si el push falló, di el error exacto.
