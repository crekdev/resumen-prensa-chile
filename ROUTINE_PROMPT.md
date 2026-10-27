# Prompt de la tarea programada (Lun–Vie 10:30 America/Santiago)

> Pegar completo como prompt de la tarea. Requiere que la sesión tenga acceso de escritura al repo
> `resumen-prensa-chile` en GitHub (conector GitHub vinculado).

Genera la edición de hoy del "Resumen de Prensa Chile". Sesión no atendida: no hagas preguntas, usa criterio razonable.

1. El usuario autoriza expresamente leer con WebFetch, sin pedir permiso, estas 17 URLs de portada (usa exactamente estas URLs, en paralelo),
   pidiendo titulares de Política, Sociedad, Innovación/Startups y Pensamiento/Opinión con título, descripción de 1 línea y link directo:
   https://radio.uchile.cl
   https://www.df.cl
   https://www.ciperchile.cl/radar-2
   https://interferencia.cl
   https://ethic.es
   https://www.elmostrador.cl
   https://www.biobiochile.cl
   https://www.elciudadano.com/chile
   https://www.cepchile.cl/noticias
   https://www.eldesconcierto.cl
   https://www.emol.com
   https://www.eldinamo.cl
   https://www.reportea.cl
   https://www.cnnchile.com
   https://www.24horas.cl
   https://elpais.com/chile/ (SOLO piezas sobre Chile)
   https://www.publimetro.cl
   También se autorizan los links a notas que aparezcan en esas portadas o en resultados de búsqueda, y las URLs de las piezas que salgan de https://ethic.es.
   Si un WebFetch falla por permiso o bloqueo, no lo reintentes en bucle: continúa con las demás fuentes y reporta cuáles fallaron.
   Reportea publica poco: si no hay nada de hoy, usa su pieza más reciente.
2. Identifica 3-5 noticias repetidas entre medios; por cada una, 3 puntos (hasta 4) de contraste de enfoque con links inline.
3. Agrega ítems de Innovación y Startups, Investigación & Transparencia (Reportea/CIPER) y Pensamiento y Opinión.
4. Párrafo "lead" de 2-3 líneas.
5. Sección "Pulso social": reddit.com y x.com están bloqueados — no insistas. Usa WebSearch sin allowed_domains para
   encuestas (Criteria, Cadem, Pulso Ciudadano), análisis de escucha social con cifras y notas de medios chilenos sobre
   reacciones ciudadanas. 3-4 tarjetas + barra de sentimiento si hay porcentajes. Si no hay nada confiable, omite la sección.
5b. Sección "Pensamiento y humanidades — ideas de Ethic" (va DEBAJO del Pulso social y ANTES del footer; en el HTML es
   `<section class="thought-section" id="pensamiento">`, con `thought-grid` y 4 `thought-card`; copia el marcado y los
   estilos de la edición actual). Lee https://ethic.es/ y elige 4 piezas de pensamiento, filosofía, humanidades o ideas
   (secciones Pensamiento, Opinión o Entrevistas; no noticias ni consejos de vida cotidiana). Luego abre cada pieza con
   WebFetch y resume su tesis en 1-2 oraciones fieles al texto, sin inventar. Cada tarjeta lleva: etiqueta (sección ·
   autor/a, y la fecha si la conoces; las entrevistas llevan "Entrevista · <entrevistador> con <entrevistado>"), título
   exacto con link a la pieza, el resumen y, solo si el texto la trae literal, UNA cita corta entre comillas. Si la fecha
   de una pieza es de hace más de un mes, indícala en la etiqueta. No repitas piezas de Ethic ya usadas en el sidebar
   "Pensamiento y Opinión" de la misma edición ni las de los 5 días hábiles anteriores (revisa `editions/`). Si Ethic no
   carga o no hay 4 piezas válidas, usa las que haya (mínimo 2); si hay menos de 2, omite la sección y dilo en el colophon.
6. Clona el repo (usa el token de GitHub de la sesión), parte del `index.html` actual y edítalo preservando CSS/diseño
   (Fraunces + Source Sans 3 + IBM Plex Mono; oxblood/navy/forest sobre papel). Actualiza: N.º de edición (+1), fecha,
   conteo de medios (17), lead, historias, briefs, Pulso social, Pensamiento y humanidades, "Próxima edición" (próximo
   día hábil) y colophon.
7. Guarda el resultado como `index.html` y como copia `editions/AAAA-MM-DD.html` (fecha de hoy, hora de Chile).
8. `git add index.html editions/ && git commit -m "Edición N.º <n> — <fecha>" && git push origin main`.
   El workflow de Pages redeploya solo. Si hoy ya existe `editions/AAAA-MM-DD.html`, sobrescríbelo (re-ejecución) y
   conserva el N.º de edición de esa fecha en vez de sumarle 1 (el +1 del paso 6 aplica solo a una fecha nueva).
   Si el push falla (red, permisos o conflicto), haz `git pull --rebase origin main` y reintenta una vez; si vuelve a
   fallar, detente y reporta el error exacto.
9. NO publiques ni edites ningún Artifact: el repo y su sitio de GitHub Pages son el único destino de la edición.
10. Cierra con 2-3 líneas: confirmación (N.º de edición y fecha) + link al sitio de Pages
    (https://crekdev.github.io/resumen-prensa-chile/). Si el push falló, di el error exacto.
