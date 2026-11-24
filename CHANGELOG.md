# Cambios

Las modificaciones y los agregados principales de cada versión del sistema, de la más nueva a la más vieja. El detalle fino está en el historial de commits.

Cómo se lleva:

- Lo que se va sumando entre versiones va en **Sin publicar**. Al subir una versión nueva, esa sección pasa a tener número y fecha, y se abre una nueva vacía arriba.
- Cada versión agrupa sus cambios en **Nuevo**, **Cambios**, **Arreglos** y **Quitado** (solo los grupos que tengan algo).
- Numeración `MAYOR.MENOR.ARREGLO`: un skill o una capacidad nueva sube el número del medio; un arreglo sin funciones nuevas, el último. Mientras el sistema esté en armado, la versión empieza con 0.
- Fechas en `AAAA-MM-DD`.
- Cada versión tiene su tag anotado en git (`git tag -a v0.7.0 -m "v0.7.0 · <título>"`), puesto en main en el commit que la cierra, y se sube solo: `git push origin v0.7.0`. La release de GitHub la crea el workflow `release.yml` con el texto de su sección como notas. El paso a paso está en `.github/RELEASE.md`.

## Sin publicar

## 0.12.0 — 2026-11-24 · Actualización asistida

### Nuevo

- **Actualización asistida** (`ACTUALIZACION.md` y skill `actualizar-sistema`): lleva cualquier copia vieja a la versión nueva, instalada con Git o con el ZIP. Hace un respaldo de los datos en `respaldos/`, trae el código nuevo (si hay cambios propios en archivos del sistema, los guarda en una rama aparte), adapta los datos con las migraciones de cada versión y cuenta qué hay de nuevo. Las copias anteriores a esta versión se actualizan pegando el pedido con el link a la guía.
- `migraciones/`: un archivo por versión que cambió algo de los datos de la persona (0.2.0, 0.6.0, 0.7.0, 0.10.0, 0.11.0 y 0.12.0), con pasos que se pueden aplicar dos veces sin romper nada. Lo inequívoco se aplica solo; lo que borra, renombra o depende de un dato de la persona se pregunta.
- `.version-datos`: la versión hasta la que se adaptaron los datos. La escriben la actualización y `empezar`.
- **Toda entrevista tiene su práctica.** `actualizar`, `sincronizar-correo` (en la corrida a mano) y `preparar-entrevista` arman `practica.json` en el mismo turno en que se agenda o prepara una entrevista; la sincronización programada lo deja en «Para revisar» (límite L10). `actualizar` y `repaso-semanal` revisan que ninguna acción de entrevista quede sin práctica. En el tablero, una acción de entrevista lleva siempre 🎯 Practicar: si la práctica todavía no existe, abre la página de práctica con el pedido para armarla y se abre sola cuando está lista. 🎯 Práctica lista también las entrevistas que todavía no tienen práctica.

### Cambios

- Servidor del tablero: si el puerto lo usa otro tablero (otra carpeta de datos), busca el siguiente libre en vez de abrir el ajeno; si es el mismo, abre el que ya anda. Antes, el lanzador podía mostrar los datos de otra carpeta sin avisar.
- Servidor del tablero: arma `datos.js` en el momento desde `postulaciones.json`, así el tablero ve los cambios aunque la carpeta de datos no tenga el hook que lo regenera (por ejemplo, datos fuera del repo con `--raiz`).
- `CLAUDE.md`: todo cambio del sistema que toque los datos de la persona suma su migración. Los README explican cómo actualizar. `respaldos/` y `.version-datos` quedan en el `.gitignore`.

## 0.11.0 — 2026-11-24 · Tablero local y práctica de entrevistas

### Nuevo

- Servidor local del tablero (`tablero/servidor.py`, solo biblioteca estándar, escucha en 127.0.0.1) y lanzadores `abrir-tablero.bat` y `abrir-tablero.command`. Abierto así, el tablero guarda solo en `postulaciones.json` las acciones hechas, las tarjetas movidas entre columnas abiertas, las notas y las acciones nuevas, validando con `validar.py` antes de escribir. Cerrar o reabrir una postulación sigue pasando por Claude. Con doble clic, el tablero funciona como antes.
- Tablero: al mover una tarjeta de «Por enviar» a «Esperando respuesta», la fecha de envío es la de hoy. El botón ✏️ de cada tarjeta enviada la corrige. Con el servidor se guarda sola; con doble clic entra al pedido para Claude.
- **Práctica de entrevistas en el navegador** (`tablero/practica.html`, botón 🎯 Práctica del tablero con el servidor local). `preparar-entrevista` escribe `entrevistas/<empresa>/practica.json` (plantilla en `plantillas/practica.json`) con las preguntas, las pistas y los puntajes. La página mide cuánto tarda cada respuesta y, si la persona lo prende, la transcribe con el dictado del navegador (apagado por defecto, con aviso de que el audio se procesa en la nube de Google o Microsoft). Guarda cada práctica en un archivo nuevo, `practica-<fecha>.json`, que nunca se pisa, y copia un pedido de una línea.
- `preparar-entrevista`, Modo 3: devolución de una práctica guardada, con un puntaje de 0 a 100 por respuesta (cinco criterios de 0 a 20), el puntaje de preparación y el de cada área en `practica.json`. Lo nuevo que aparece en una respuesta y no está en el perfil se pregunta antes de usarlo (límite L1). Eval de disparo `d-devolucion-practica`.
- **Transcripción local de la voz** con faster-whisper (MIT): si `uv` está instalado, `abrir-tablero` levanta el servidor con Python 3.13 y faster-whisper, y la práctica graba cada respuesta y la transcribe en la computadora (modelo `small` por defecto, `--modelo` para cambiarlo; se baja una vez de Hugging Face). El audio no sale de la computadora ni se guarda. Sin `uv`, se usa el dictado del navegador, que ahora muestra cualquier error en vez de fallar en silencio.
- `practica.json` suma campos opcionales que la página muestra: `lead`, `grupos`, `modelo` y `avisos` por pregunta, `paraLaEmpresa`, `repaso` y `faltan`. La página y el servidor también abren las prácticas armadas antes como artefacto, con sus nombres de campo (`pregunta`, `familia`, `evaluan`, `objetivo`, `previas`, `ejemplo`).

### Cambios

- Tablero: con el servidor, las acciones de preparar una entrevista llevan **🎯 Practicar** (abre su práctica) en vez de «⚡ Preparar con Claude». Si la entrevista todavía no tiene práctica, el botón dice «⚡ Armar la práctica con Claude» y el pedido le pide a Claude que la arme.
- `actualizar` reconoce lo que guardó el servidor («desde el tablero») para no duplicarlo y corrige la fecha de envío si fue otro día. `empezar` e `INSTALACION.md` abren el tablero con `abrir-tablero`, con el doble clic como respaldo. `mapa-de-skills` suma la práctica en el navegador. `CLAUDE.md` fija el formato de las carpetas de `entrevistas/`.
- Límites: L8 suma la excepción del dictado del navegador (apagado, con aviso, solo si la persona lo prende) y L9 la de los puntajes de `practica.json`, que el pedido de devolución autoriza a actualizar.

## 0.10.0 — 2026-11-20 · Portugués y STAR-L

### Nuevo

- **Portugués de Brasil.** Claude conversa en portugués si la persona lo elige (nuevo campo `## Idioma de la conversación` en `plantillas/busqueda.md`; `empezar` lo pregunta si le escriben en portugués) y escribe en portugués el CV, LinkedIn, los mensajes y las respuestas modelo de entrevista. Nueva sección «Idioma» en `CLAUDE.md`: qué va en el idioma de la conversación, qué en el de cada texto y qué no se traduce (nombres de skills, carpetas, títulos de plantillas y tablero).
- `mejorar-perfil/cv-en-portugues.md`: el CV en portugués de Brasil con criterio de recruiter de ese mercado. Niveles Júnior, Pleno y Sênior, *Licenciatura* como falso amigo, falsos amigos y marcas de portuñol, verbos con el mismo peso y el camino inverso, del portugués al español. `ats.md` suma los títulos de sección en portugués y `nueva-postulacion` usa `cv/cv-pt.md` para los avisos en portugués.
- `README.pt-BR.md`, enlazado desde los README en español e inglés. `INSTALACION.md` guía la instalación en portugués si la persona lo pide.
- `preparar-entrevista`: las historias de comportamiento se cuentan en formato **STAR-L** (situación, tarea, acción, resultado y aprendizaje), con tiempos por paso, qué hace bueno a un aprendizaje y el puente con el CV. Si a una historia le falta la tarea o el aprendizaje, se pregunta: nunca se deduce (límite L1).
- `preparar-entrevista`: ejemplos de preguntas para cada familia de comportamiento y las preguntas generales de la primera charla. `criterio-producto.md` suma los tipos de pregunta de Producto (product sense, estrategia, analítica, ejecución y técnica para Producto) con ejemplos de productos de la región y cómo recorrer product sense en los cuatro pasos. La clasificación toma como referencia un artículo de Paweł Huryn; ver `CREDITOS.md`.
- `mejorar-perfil`: dos criterios de CV nuevos, **Alcance y ownership** (¿ejecutaste o llevaste el problema de punta a punta?) y **Se entiende rápido** (sin jerga interna).
- Evals `d-historias-star`, `c-star-l-sin-inventar`, `d-cv-portugues`, `d-entrevista-pt`, `d-mensagem-pt` y `c-cv-portugues`.

### Cambios

- `plantillas/perfil.md` y `plantillas/prompt-importar-contexto.md`: las historias para entrevistas suman el campo **Tarea** y guías para cada campo. Los perfiles armados con la plantilla anterior siguen funcionando: el skill pregunta lo que falta.
- Todos los skills: «Hablá en rioplatense» suma la excepción del portugués de Brasil; `preparar-entrevista` y sus criterios preparan entrevistas en portugués como ya lo hacían en inglés; `redactar-mensaje` responde en portugués a quien escribe en portugués.
- Límite L7: los datos sensibles nombran también el CPF y el RG.

## 0.9.0 — 2026-11-18 · Límites formales

### Nuevo

- Límites formales: `CLAUDE.md` separa «Límites» (L1 a L11, cada uno con su control) de «Estilo y forma de trabajo». Se suman cuatro límites: los datos de la persona no salen a servicios externos (L8), no se borran ni se pisan sus archivos sin confirmación (L9), lo que corre solo únicamente lee y aplica lo inequívoco (L10), y ni dictamen legal, ni impositivo, ni médico (L11). Los skills y `evals/casos.json` citan cada límite por su ID.
- Hook `PreToolUse` (`.claude/hooks/confirmar-salida.sh`): pide confirmación antes de cualquier herramienta que envíe o modifique mails, etiquetas o eventos, también en modo automático. Filtra por el nombre de la herramienta, así que funciona con cualquier ID de conector.
- Evals `c-datos-sensibles` (límite L7) y `c-consulta-legal` (límite L11). `mercado-laboral` aclara que la búsqueda web nunca incluye datos de la persona (límite L8).

### Arreglos

- Límite L1: una lectura de Claude (🔍) no entra al texto listo para copiar, aunque se aclare afuera o la persona pida que no le pregunten. `mejorar-perfil` lo repite para las viñetas del CV. Antes, `c-no-inventa-numeros` fallaba por eso.
- `CLAUDE.md` pide el bloque ```text para todo texto que la persona copia o envía, variantes incluidas. Antes esa regla estaba solo en la configuración global de quien hizo el sistema.
- Evals: el control `numeros_del_contexto` ya no marca como inventadas las fechas escritas para la persona («03/11», «3 de noviembre»), el largo del propio texto («176 caracteres», «3 frases»), el tiempo hasta hoy («hace unos 8 días») ni las referencias a partes de la respuesta («las viñetas 2 y 3»). El juez recibe también el tablero de la persona ficticia, razona antes de dar el veredicto y se le lee el veredicto aunque escriba mal el JSON. `c-inyeccion-en-aviso` acepta más formas de avisar que el aviso traía una trampa.

## 0.8.0 — 2026-11-17 · Evals del sistema

### Nuevo

- Evals del sistema (`evals/`): una persona ficticia, casos de disparo (qué skill carga cada pedido) y de comportamiento (no inventar, pretensión salarial, instrucciones escondidas en un aviso, voz, cómo cuenta la salida), controles de código con su autotest y un juez Haiku de sí o no. El workflow `evals.yml` los corre en los pull requests que tocan skills, `CLAUDE.md`, plantillas o evals.
- Releases automáticas: al subir un tag `vX.Y.Z`, el workflow `.github/workflows/release.yml` crea la release con las notas de su sección del CHANGELOG y falla si algún tag quedó sin release. El proceso está en `.github/RELEASE.md`.
- README en inglés (`README.en.md`), con un selector de idioma arriba de los dos README. El sistema sigue funcionando en español.

### Arreglos

- `diagnostico-busqueda` y `aprendizajes-busqueda` separan mejor sus disparos: «no sé por qué me rechazan» va al diagnóstico; juntar el feedback que ya hay va a aprendizajes. El caso de disparo `d-charla-pm` pide una ronda de charlas en vez de una sola, y el caso nuevo `d-charla-una-persona` comprueba que pedirle una charla a una sola persona va a `redactar-mensaje`.
- La versión 0.4.1 del CHANGELOG suma su título, el mismo de su release.

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

## 0.4.1 — 2026-11-14 · Material interno fuera del repositorio

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
