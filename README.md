# Búsqueda laboral OS

Un sistema para ordenar tu búsqueda laboral con **Claude Code**: tu perfil, LinkedIn y CV, cada postulación, la preparación de entrevistas y un tablero que te dice qué hacer hoy. Todo queda en carpetas de tu computadora.

Lo armamos para un taller entre colegas de IT que estamos buscando nuestro próximo desafío. Sirve para cualquier perfil: desarrollo, QA, datos, producto, diseño, infraestructura, proyectos.

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

Se actualiza solo cada vez que Claude cambia algo. Si marcás una acción como hecha o movés una tarjeta en el tablero, tocá **Copiar pedido para Claude** y pegalo en Claude Code para que quede guardado. El botón **⚡** de cada acción copia un pedido para que Claude te ayude con esa tarea.

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
├── CLAUDE.md          Instrucciones para Claude: reglas, carpetas, modelo de datos
├── contexto/          Tu fuente de verdad: perfil, qué buscás, tu voz, decisiones · importado/ con lo que traigas de antes
├── linkedin/          Tu PDF de LinkedIn · sugerencias/ con los textos nuevos
├── cv/                Tu CV
├── postulaciones/     postulaciones.json (datos del tablero) + una carpeta por postulación
├── entrevistas/       Una carpeta por empresa con la preparación
├── investigacion/     Informes fechados: diagnóstico, mercado, métricas, repasos
├── tablero/           tablero.html (abrilo con doble clic)
├── plantillas/        Lo que /empezar copia la primera vez
└── .claude/skills/    Los 18 skills
```

### Los skills

**Día a día**

| Skill | Para qué |
|---|---|
| `empezar` | Puesta en marcha: trae lo que ya tenés (CV, LinkedIn, notas, el contexto de otra IA), carga tu perfil, qué buscás y tu voz, y deja el tablero listo |
| `mejorar-perfil` | Lee tu PDF de LinkedIn, tu CV o los dos, compara qué tiene cada uno, te entrevista y te da textos listos para copiar y pegar, más el CV |
| `analizar-oferta` | Encaje de un aviso con tu perfil (0 a 100), requisitos uno por uno, si vale la pena |
| `nueva-postulacion` | Carpeta, CV adaptado, respuestas del formulario y tarjeta en el tablero |
| `actualizar` | Lleva cada novedad al tablero y crea las acciones que siguen |
| `sincronizar-correo` | Trae las novedades de Gmail y Google Calendar al tablero, a demanda (🔄 SYNC) o cada 2 horas de 8 a 22 |
| `redactar-mensaje` | Mensajes a recruiters, referidos, follow-ups y agradecimientos con tu voz |
| `preparar-entrevista` | Preguntas probables, historias reales para cada una y simulacro con feedback |
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

Cuando haya mejoras en el taller, pedile a Claude "actualizá el sistema" o corré:

```bash
git pull
```

Tus datos no se tocan: están fuera de lo que se versiona.

---

## Instrucciones de instalación para Claude Code

*Esta sección es para Claude.* Si te pidieron instalar este sistema, seguí el protocolo de [INSTALACION.md](INSTALACION.md), parte 2, etapa por etapa.

---

## Créditos

- Sistema armado por Juan Rodríguez Loredo para el taller. Licencia MIT: ver [LICENSE](LICENSE).
- Trece piezas del sistema (skills o partes de un skill) son adaptaciones de los skills de producto de **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT). Detalle en [CREDITOS.md](CREDITOS.md).
