# Búsqueda laboral OS

[English](README.en.md) · **Español** · [Português](README.pt-BR.md)

Un sistema para ordenar tu búsqueda laboral con **Claude Code**: tu perfil, LinkedIn y CV, cada postulación, la preparación de entrevistas y un tablero que te dice qué hacer hoy. Todo queda en carpetas de tu computadora.

Lo armamos para un taller entre colegas de IT que estamos buscando nuestro próximo desafío. Sirve para cualquier perfil: desarrollo, QA, datos, producto, diseño, infraestructura, proyectos.

> **🎓 Taller en vivo «Buscá con sistema»**: dos encuentros con acompañamiento personalizado para usar este sistema en tu búsqueda, en español. Fechas, precios y becas en **[busca-con-sistema.pages.dev](https://busca-con-sistema.pages.dev/)**.
>
> ¿Sos headhunter o reclutador independiente? Mirá la sección **Recruiters** de la misma página.

---

## Instalación asistida

Necesitás un plan **Claude Pro o Max** y la **app de escritorio de Claude** ([claude.com/download](https://claude.com/download)). No hace falta saber programar ni tener cuenta de GitHub.

1. Abrí la app, pestaña **Code**, y elegí tu carpeta **Documentos** como carpeta de trabajo.
2. Pegá este pedido:

```
Instalá el sistema de búsqueda laboral siguiendo, etapa por etapa, la guía https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/INSTALACION.md
```

Claude te guía etapa por etapa: descarga el sistema, te ayuda a abrirlo en su carpeta, conecta Gmail y Google Calendar (solo lectura) y comprueba que todo funciona. La guía completa, con los pasos previos y qué hacer si algo se traba, está en **[INSTALACION.md](INSTALACION.md)**.

Al terminar, en la carpeta del sistema, escribí:

```
/empezar
```

### Si preferís hacerlo a mano

Con Git instalado, en una terminal:

```bash
git clone https://github.com/JuanLoredo6/busqueda-laboral-os.git mi-busqueda
```

En la app de escritorio: elegí la carpeta `mi-busqueda` como carpeta de trabajo de una sesión nueva.

### Problemas frecuentes

| Qué pasa | Qué hacer |
|---|---|
| Escribo `/empezar` y no aparece | Claude Code está abierto en otra carpeta. Abrí una sesión nueva **en la carpeta del sistema** (la que tiene `CLAUDE.md` adentro). Los skills solo se cargan ahí |
| Claude me pide permiso para todo | Dentro de la carpeta del sistema, leer y editar archivos ya está permitido. Te va a pedir permiso para buscar en internet o correr otros comandos: leé qué quiere hacer y aceptá si tiene sentido |
| El tablero dice «Todavía no hay datos» | Corré `/empezar` primero. Si ya lo hiciste, pedile a Claude: «regenerá el tablero» |
| El tablero no se actualiza | Recargá la página (F5). Si sigue igual, pedile a Claude: «corré tablero/sincronizar.sh» |
| El tablero dice que la sincronización automática está «atrasada» | La tarea programada corre solo con la app de escritorio de Claude abierta. Abrila y tocá 🔄 SYNC para ponerte al día |
| `/sincronizar-correo` dice que falta un conector | Tocá el **+** junto al cuadro de mensaje → conectores → Gmail o Google Calendar → Conectar. Si Claude sigue sin verlo, abrí una sesión nueva. Detalle en [INSTALACION.md](INSTALACION.md), etapa 5 |
| En Mac me dice que falta `git` | Aceptá la ventana que ofrece instalar las herramientas de desarrollo, esperá a que termine y volvé a intentar |
| No sé qué hacer ahora | Preguntale a Claude «¿qué hago ahora?» o escribí `/mapa-de-skills` |

---

## Cómo se usa

| Cuándo | Qué le decís a Claude |
|---|---|
| La primera vez | `/empezar` |
| Para mejorar LinkedIn y el CV (dejá el PDF de LinkedIn en `linkedin/`, tu CV en `cv/`, o los dos) | `/mejorar-perfil` |
| Cuando ves un aviso que te interesa | `/analizar-oferta` y pegás el link o el texto |
| Para postularte | `/nueva-postulacion` |
| Cuando pasa algo ("me respondieron de X") | Contáselo, o `/actualizar` |
| Para traer lo que llegó por mail o al calendario | 🔄 SYNC en el tablero, o `/sincronizar-correo` |
| Para escribirle a alguien | `/redactar-mensaje` |
| Antes de una entrevista | `/preparar-entrevista` |
| Los viernes | `/repaso-semanal` |
| Para ver todo lo que hay | `/mapa-de-skills` |

No hace falta acordarse de los nombres: si le pedís algo con tus palabras, Claude elige el skill que corresponde.

### El tablero

Abrí `tablero/tablero.html` con doble clic y dejalo abierto en una pestaña. Muestra:

- **Hoy:** si tenés algo que hacer hoy y qué.
- **Lo que tenés que hacer:** las acciones agrupadas en vencidas, hoy, próximos días y sin fecha.
- **Postulaciones:** un kanban con las columnas Por enviar, Esperando respuesta y En conversación, y los días sin novedades de cada una.
- **Números:** postulaciones enviadas, tasa de respuesta, conversaciones activas y acciones vencidas.

Se actualiza solo cada vez que Claude cambia algo.

**Para que lo que marcás se guarde solo**, abrilo con `tablero/abrir-tablero.bat` en Windows o `tablero/abrir-tablero.command` en Mac (necesita Python). Así, marcar una acción como hecha, mover una tarjeta, anotar una novedad, sumar una acción o corregir con ✏️ la fecha de envío queda guardado al instante, sin pasar por Claude. Cerrar una postulación sigue pasando por Claude, porque necesita el resultado. El servidor solo escucha en tu computadora y deja de andar cuando cerrás su ventana.

Si lo abrís con doble clic, lo que marcás queda pendiente: tocá **Copiar pedido para Claude** y pegalo en Claude Code para que quede guardado. El botón **⚡** de cada acción copia un pedido para que Claude te ayude con esa tarea.

Con el servidor, el botón **🎯 Práctica** abre la práctica de las entrevistas que preparaste con `/preparar-entrevista`. Respondés cada pregunta escribiendo o en voz alta (el dictado es opcional: si tenés [uv](https://docs.astral.sh/uv/) instalado, la voz se transcribe en tu computadora con Whisper y el audio no sale de ahí; la primera vez baja unos 480 MB. Sin uv, usa el dictado del navegador, que procesa el audio en la nube). La página mide cuánto tardás, guarda tus respuestas en la carpeta de la entrevista y te da un pedido de una línea para que Claude te devuelva el feedback y actualice tu puntaje de preparación.

**Tablero retro.** Si preferís algo con más juego, abrí `tablero/abrir-tablero-retro.bat` en Windows o `tablero/abrir-tablero-retro.command` en Mac: tus postulaciones se ven como un pueblo en pixel art que recorrés con el teclado. Cada estado es un barrio y cada postulación una casa, con un «!» cuando tiene algo pendiente; adentro de cada casa están la empresa, el rol, tu encaje, el historial y un escritorio con sus tareas. **A** mira y entra, **S** copia el pedido para Claude, **D** da por hecha una tarea, **Enter** muestra las prioridades y el personaje camina solo hasta la que elijas, y **M** abre el minimapa. En la plaza están el tablón, el buzón de la sincronización, el calendario y las mudanzas; en la Universidad, el faro y tu casa, mejorar el perfil, el repaso semanal y la configuración (día o noche, a pie o en bici, música y sonidos). Usa los mismos datos y el mismo servidor local que el kanban, en otro puerto (8766), así podés tener los dos abiertos: lo que marcás se guarda igual.

Para verlo con datos de ejemplo antes de cargar los tuyos, abrí el tablero y tocá **Ver el tablero con datos de ejemplo**.

### Novedades desde Gmail y Google Calendar (opcional)

Claude puede revisar tu correo y tu agenda **solo para leer** y llevar al tablero lo que llega: confirmaciones, respuestas de recruiters, entrevistas agendadas, rechazos.

1. Conectá Gmail y Google Calendar en claude.ai → **Configuración → Conectores**, con tu cuenta de Google. Después abrí una sesión nueva de Claude Code en la carpeta del sistema.
2. Tocá **🔄 SYNC** en el tablero y pegá el pedido en Claude Code, o escribí `/sincronizar-correo`. La primera vez Claude te pide permiso para leer: elegí **permitir siempre** para buscar y leer mails y para listar eventos.
3. Para que corra sola **cada 2 horas, de 8 a 22**, escribí `/sincronizar-correo configurar`. Se crea una tarea programada en la app de escritorio de Claude, que corre mientras la app está abierta.

Lo que es claro (una entrevista con fecha, un rechazo explícito) se aplica solo. Lo dudoso, las ofertas y los mails sospechosos quedan en **«Para revisar»** en el tablero, para que decidas vos. Claude nunca responde, archiva ni borra mails.

---

## Qué hay adentro

```
busqueda-laboral-os/
├── INSTALACION.md     La guía de instalación asistida
├── CLAUDE.md          Instrucciones para Claude: límites, carpetas, modelo de datos
├── contexto/          Tu fuente de verdad: perfil, qué buscás, tu voz, decisiones · importado/ con lo que traigas de antes
├── linkedin/          Tu PDF de LinkedIn · sugerencias/ con los textos nuevos
├── cv/                Tu CV
├── postulaciones/     postulaciones.json (datos del tablero) + una carpeta por postulación
├── entrevistas/       Una carpeta por empresa con la preparación
├── investigacion/     Informes fechados: diagnóstico, mercado, métricas, repasos
├── tablero/           tablero.html (abrilo con doble clic) · abrir-tablero y abrir-tablero-retro
├── plantillas/        Lo que /empezar copia la primera vez
└── .claude/skills/    Los 19 skills
```

### Los skills

**Día a día**

| Skill | Para qué |
|---|---|
| `empezar` | Puesta en marcha: trae lo que ya tenés (CV, LinkedIn, notas, el contexto de otra IA), carga tu perfil, qué buscás y tu voz, y deja el tablero listo |
| `mejorar-perfil` | Lee tu PDF de LinkedIn, tu CV o los dos, compara qué tiene cada uno, te entrevista y te da textos listos para copiar y pegar, más el CV. También en inglés o en portugués de Brasil, como los escribiría alguien nativo |
| `analizar-oferta` | Encaje de un aviso con tu perfil (0 a 100), requisitos uno por uno, si vale la pena, y la ficha de la empresa |
| `nueva-postulacion` | Carpeta con la ficha de la empresa, CV adaptado, respuestas del formulario y tarjeta en el tablero |
| `actualizar` | Lleva cada novedad al tablero y crea las acciones que siguen |
| `sincronizar-correo` | Trae las novedades de Gmail y Google Calendar al tablero, a demanda (🔄 SYNC) o cada 2 horas de 8 a 22 |
| `redactar-mensaje` | Mensajes a recruiters, referidos, follow-ups y agradecimientos con tu voz |
| `preparar-entrevista` | Preguntas probables, historias reales para cada una en formato STAR-L y simulacro con feedback |
| `repaso-semanal` | Números de la semana, lo que se está cayendo y tres prioridades |

**Estrategia de la búsqueda**

| Skill | Para qué |
|---|---|
| `diagnostico-busqueda` | Por qué no avanza: síntoma, causa e hipótesis para probar, y qué números mirar para saber si avanzás |
| `mercado-laboral` | Dónde hay demanda para tu perfil y qué empresas apuntar, con fuentes |
| `posicionamiento` | A qué rol apuntás, qué problema resolvés, para quién y qué descartás. Después, ángulos para presentarte, tu pitch de 30 segundos y tu titular |
| `plan-de-networking` | A quién pedirle una charla, qué preguntarle y cómo escribirle |
| `aprendizajes-busqueda` | Qué te dice el feedback real (rechazos, entrevistas, charlas) |

**Herramientas de criterio**

| Skill | Para qué |
|---|---|
| `poner-a-prueba` | Repregunta cada logro y cada decisión hasta que se sostenga |
| `recruiters-sinteticos` | Prueba tu CV, pitch o mensaje contra recruiters simulados |
| `disenador-visual` | Especificar y construir CV, portada, presentación o portfolio |
| `mapa-de-skills` | El índice de todo lo anterior |

---

## Tus datos

- Todo lo tuyo (perfil, CV, postulaciones) queda **solo en tu computadora**. El `.gitignore` evita que se suba a GitHub por error.
- **No subas tu copia a un repositorio público.** Si querés un respaldo, copiá la carpeta a tu nube (Drive, OneDrive, iCloud) o usá un repositorio **privado**.
- Claude no envía mensajes ni postulaciones por vos: redacta, y vos mandás.

## Actualizar el sistema

Cuando haya una versión nueva, abrí Claude Code en la carpeta del sistema y pedile «actualizá el sistema». Si tu copia es anterior a la 0.12.0, pegá este pedido:

```text
Actualizá el sistema de búsqueda laboral siguiendo la guía https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/ACTUALIZACION.md
```

Claude hace primero un respaldo de tus datos, trae el código nuevo (con Git o con el ZIP, según cómo lo instalaste), adapta tus datos a lo que cambió y te cuenta qué hay de nuevo. El paso a paso está en [ACTUALIZACION.md](ACTUALIZACION.md).

Qué cambió en cada versión: [CHANGELOG.md](CHANGELOG.md).

## Si cambiás de computadora

Tus datos no están en GitHub (el `.gitignore` los deja afuera), así que no alcanza con volver a descargar el sistema: se pasa **la carpeta entera en un ZIP**, con sus carpetas ocultas (`.git`, `.claude`). Así viajan tus datos, la versión de tus datos y la conexión para recibir actualizaciones.

1. **En la computadora actual**, abrí Claude Code en la carpeta del sistema y pegá:

   ```text
   Voy a pasar este sistema a otra computadora. Confirmá que estás en la carpeta del sistema y contame qué datos míos hay. Armá un ZIP de la carpeta entera, con las carpetas y archivos ocultos (.git, .claude, .version-datos), en mi Escritorio con el nombre mi-busqueda-traspaso y la fecha de hoy. Comprobá que el ZIP los tiene, decime cuánto pesa y si tengo una tarea programada de sincronización. No subas el ZIP a ningún lado ni borres nada de esta carpeta.
   ```

2. **Llevá el ZIP** en un pendrive o en tu propia nube (Drive, OneDrive, iCloud), sin compartir el link: adentro está tu CV. Cuando termines, borralo de ahí.
3. **En la computadora nueva**, instalá la app de Claude, entrá con la misma cuenta, pestaña **Code**, entorno **Local**, abrí la carpeta **Documentos** y pegá (con la ubicación del ZIP):

   ```text
   Traje mi sistema de búsqueda laboral de otra computadora en un ZIP que está en [dónde quedó]. Descomprimilo en Documentos como mi-busqueda (si ya existe, no la pises y preguntame). Comprobá que estén CLAUDE.md, .claude/skills/empezar/SKILL.md y mis datos en postulaciones y contexto. Decime la ruta completa y cómo abrir una sesión nueva en esa carpeta.
   ```

4. En la sesión nueva, escribí **seguí con la instalación**: Claude ve que el sistema ya está y retoma desde los conectores de Gmail y Calendar y el tablero.
5. Si usabas la sincronización automática, volvé a crearla con `/sincronizar-correo configurar`: las tareas programadas no pasan de una computadora a otra. Los chats viejos tampoco, pero todo lo importante está en los archivos.

La copia es una foto del momento: desde ahí, trabajá en la computadora nueva. Si seguís anotando en las dos, se desincronizan. La carpeta vieja queda como respaldo.

---

## Instrucciones de instalación para Claude Code

*Esta sección es para Claude.* Si te pidieron instalar este sistema, seguí el protocolo de [INSTALACION.md](INSTALACION.md), parte 2, etapa por etapa.

---

## Créditos

- Sistema armado por Juan Rodríguez Loredo para el taller. Licencia MIT: ver [LICENSE](LICENSE).
- Trece piezas del sistema (skills o partes de un skill) son adaptaciones de los skills de producto de **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT). Detalle en [CREDITOS.md](CREDITOS.md).
- Varias secciones adaptan métodos de **Paweł Huryn** ([The Product Compass](https://www.productcompass.pm)), publicados con licencia MIT en [pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) y [pm-brain](https://github.com/phuryn/pm-brain). Detalle en [CREDITOS.md](CREDITOS.md).
