# Cambios

Las modificaciones y los agregados principales de cada versión del sistema, de la más nueva a la más vieja. El detalle fino está en el historial de commits.

Cómo se lleva:

- Lo que se va sumando entre versiones va en **Sin publicar**. Al subir una versión nueva, esa sección pasa a tener número y fecha, y se abre una nueva vacía arriba.
- Cada versión agrupa sus cambios en **Nuevo**, **Cambios**, **Arreglos** y **Quitado** (solo los grupos que tengan algo).
- Numeración `MAYOR.MENOR.ARREGLO`: un skill o una capacidad nueva sube el número del medio; un arreglo sin funciones nuevas, el último. Mientras el sistema esté en armado, la versión empieza con 0.
- Fechas en `AAAA-MM-DD`.
- Cada versión tiene su tag en git (`v0.7.0`), puesto en el commit que la cierra, y se sube con `git push origin --tags`. Después se publica su release en GitHub con el texto de su sección como notas (`gh release create v0.7.0 --title "v0.7.0 · <título>" --notes-file <notas>`).

## Sin publicar

## 0.7.2 — 2026-11-15 · Licencia MIT en todo el repo

### Cambios

- `CLAUDE.md` nombra la licencia MIT y también a Paweł Huryn en los créditos.
- Los scripts y el tablero (`revisar-ats.py`, `validar.py`, `sincronizar.sh`, `tablero.html`, `ejemplo.js`) llevan su línea de licencia MIT, y el pie del tablero remite a los créditos.
- La «Plantilla de notas» de `preparar-entrevista` enlaza pm-brain con su licencia.
- `preparar-entrevista` acredita en su encabezado los criterios de producto y técnico adaptados de Pedro Romero Luna.
- `README.md` enlaza los tres repositorios de Paweł Huryn y `CREDITOS.md` abre con la licencia del sistema.

### Arreglos

- Se saca del repo `tablero/__pycache__/`, que se había subido por error, y queda en `.gitignore`.

## 0.7.1 — 2026-11-15 · Licencia y créditos en cada skill

### Cambios

- Cada `SKILL.md` declara su licencia en el encabezado (`license:`). Los skills adaptados nombran a Pedro Romero Luna, a Paweł Huryn o a los dos, y remiten a su texto de licencia.
- La nota del `LICENSE` raíz y los créditos del `README.md` también nombran a Paweł Huryn.
- `tablero/validar.py` dice en su encabezado de dónde viene la idea (el hook de validación de pm-brain).

## 0.7.0 — 2026-11-15 · CV en dos idiomas y filtros ATS

### Nuevo

- `mejorar-perfil/cv-en-ingles.md`: el CV y los textos de LinkedIn en el otro idioma, con criterio de recruiter bilingüe. Cubre las convenciones del CV en inglés, las equivalencias de cargos y títulos sin subir el nivel, los falsos amigos del rioplatense, lo que suena a IA en inglés y el nivel de inglés real. Se entrega con una revisión viñeta por viñeta y una tabla de decisiones de traducción para confirmar.
- `mejorar-perfil/ats.md`: formato, títulos de sección y palabras clave para que el CV lo lea bien un sistema de selección, con lo que se puede garantizar y lo que no.
- `mejorar-perfil/revisar-ats.py`: revisa un CV en .docx, PDF o .md. Marca tablas, columnas, cuadros de texto, contacto en el encabezado, PDF sin texto, secciones que faltan, fechas mezcladas y qué porcentaje de las palabras clave del aviso aparece.
- `plantillas/busqueda.md`: sección «Idioma del CV» (español por defecto, configurable) y variante del inglés.

### Cambios

- `mejorar-perfil` lee el idioma por defecto en vez de preguntarlo cada vez, y su paso 5 arma el CV base, la versión en el otro idioma y la comprobación ATS.
- `nueva-postulacion` adapta el CV en el idioma del aviso y comprueba sus palabras clave con el script.
- `disenador-visual`, `recruiters-sinteticos`, `empezar` y `mapa-de-skills` apuntan a las partes nuevas.

## 0.6.0 — 2026-11-14 · De 22 a 18 skills

### Cambios

- Cuatro skills que se pisaban pasan a ser partes del skill que los usa:
  - `propuesta-de-valor` → fase 3 de `posicionamiento`;
  - `metricas-busqueda` → modo métricas de `diagnostico-busqueda`;
  - `criterio-producto` y `criterio-tecnico` → partes de `preparar-entrevista`.
- `preparar-entrevista` suma práctica sin entrevista agendada.
- `repaso-semanal` ofrece definir el indicador si todavía no existe.

### Quitado

- Los skills `propuesta-de-valor`, `metricas-busqueda`, `criterio-producto` y `criterio-tecnico` como skills sueltos. Sus frases de activación pasan a la descripción del skill que los contiene.

## 0.5.0 — 2026-11-14 · Arranque desde el contexto que ya tenés

### Nuevo

- `plantillas/prompt-importar-contexto.md`: un prompt para traer el contexto armado en otra IA, en las secciones de las plantillas y marcando qué dijo la persona y qué infirió la IA.

### Cambios

- `empezar` pregunta primero qué material ya hay (CV, LinkedIn, notas, otra IA), lo vuelca con confirmación por bloque y la entrevista pregunta solo lo que falta.
- `mejorar-perfil` arranca desde el CV, el PDF de LinkedIn o los dos, y compara ambos para encontrar lo que está en uno solo.

## 0.4.1 — 2026-11-14

### Quitado

- El material interno del taller deja de publicarse en el repositorio.

## 0.4.0 — 2026-11-14 · Skills más efectivos

### Nuevo

- `tablero/validar.py`: valida `postulaciones.json` después de cada edición. Si el JSON está roto, no pisa `datos.js`.
- Ejemplos ilustrativos en diez skills y créditos con su licencia en `CREDITOS.md`.

### Cambios

Métodos adaptados de los repositorios de Paweł Huryn (MIT), sin sumar skills:

- `redactar-mensaje`: «Revisión de voz» (modo entrevista, certeza de cada dato, muletillas de IA, opción más corta).
- `mejorar-perfil`: «Criterios de CV» (viñeta con resultado, cargos estándar sin subir el nivel, cambio de rol).
- `diagnostico-busqueda`: prioridad por riesgo × impacto × barato de probar, criterio para abandonar cada hipótesis y «Lo que sí se sostiene».
- `repaso-semanal`: contexto viejo, hipótesis estancadas, decisiones a revisar y contactos sin seguimiento.
- `poner-a-prueba`: las decisiones clave llevan «Descarto» y «Cambio de idea si».
- `preparar-entrevista`: plantilla de notas que separa citas de lecturas.
- `posicionamiento`: curva de valor para competencia y diferencial.

## 0.3.0 — 2026-11-13 · Instalación asistida

### Nuevo

- `INSTALACION.md`: lleva desde cero hasta el sistema funcionando, para quien nunca usó Claude Code. Tres pasos propios y un protocolo de ocho etapas que Claude sigue y comprueba, incluidos los conectores de Gmail y Google Calendar.

## 0.2.0 — 2026-11-12 · Gmail y Google Calendar

### Nuevo

- Skill `sincronizar-correo`: revisa Gmail y Calendar en modo solo lectura, aplica lo inequívoco y deja lo dudoso, las ofertas y los mails sospechosos en «Para revisar». Puede correr sola cada 2 horas, de 8 a 22.
- Tablero: botón 🔄 SYNC, estado de la última sincronización con aviso de atraso y bloque «Para revisar».

## 0.1.0 — 2026-11-12 · Primera versión

### Nuevo

- 21 skills para Claude Code (8 propios y 13 adaptados de los skills de producto de Pedro Romero Luna, MIT).
- Tablero local que lee `postulaciones.json`, se abre con doble clic y no necesita internet.
- Plantillas de contexto (perfil, búsqueda, voz, decisiones, datos pendientes).
- README con instalación y problemas frecuentes.
