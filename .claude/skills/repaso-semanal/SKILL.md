---
name: repaso-semanal
description: "Hace el repaso de la semana de búsqueda en 10 minutos: lee el tablero, calcula los números de la semana (postulaciones, respuestas, conversaciones) contra tus métricas, detecta acciones vencidas y postulaciones olvidadas, revisa las antimétricas, propone las 3 prioridades de la semana que viene y las suma al tablero si las aceptás. Usala cuando digas /repaso-semanal, 'cómo me fue esta semana', 'cómo voy', 'repasemos', 'qué hago la semana que viene', o los viernes."
---

# repaso-semanal — 10 minutos para no perder el hilo

Una búsqueda larga se desordena sin un momento fijo para mirar el conjunto. Este repaso es ese momento: corto, con números y con tres prioridades claras para la semana siguiente.

Hablá en rioplatense, con voseo. Con un tono que sostenga: reconocé lo hecho antes de marcar lo que falta.

## Qué leer

- `postulaciones/postulaciones.json` (tarjetas, historial, acciones).
- `contexto/busqueda.md`, sección **Cómo mido la búsqueda** (indicador principal y antimétricas, si ya se definieron con el modo métricas de `diagnostico-busqueda`).
- Los dos repasos anteriores en `investigacion/*-repaso-semanal.md`, si existen, para comparar.
- `contexto/decisiones.md` (sobre todo las ⭐ y su "Cambio de idea si...") y el último `investigacion/*-diagnostico-busqueda.md`.
- La fecha de la última modificación de `contexto/perfil.md`, `contexto/posicionamiento.md` y del último informe de mercado (la fecha de modificación del archivo; esas carpetas no están en git).

La semana es de lunes a domingo de la fecha de hoy, salvo que la persona diga otra cosa.

## El repaso, en cinco partes

### 1. Lo que hiciste

Contá desde el JSON (no lo preguntes):

- Postulaciones enviadas (con fecha de envío en la semana).
- Respuestas recibidas (tarjetas que pasaron a `conversacion` o a `cerrada` con historial en la semana).
- Conversaciones: charlas y entrevistas de la semana.
- Acciones completadas.
- Otros avances que muestre el historial o `investigacion/` (perfil mejorado, diagnóstico, networking).

Una frase de reconocimiento concreta, sin exagerar.

### 2. Los números

| Métrica | Esta semana | Semana anterior | Acumulado |
|---|---|---|---|
| Postulaciones enviadas | | | |
| Tasa de respuesta (respondidas / enviadas, acumulado) | | | |
| Conversaciones (charlas + entrevistas) | | | |
| Indicador principal (si está definido) | | | |

Si no hay indicador definido, decilo en una línea y ofrecé definirlo al terminar el repaso (unos 10 minutos más, con `.claude/skills/diagnostico-busqueda/metricas.md`) o dejarlo como una de las prioridades de la semana que viene. Lo decide la persona. Con menos de 10 postulaciones, aclará que los porcentajes todavía no dicen mucho.

### 3. Lo que se está cayendo

- **Acciones vencidas:** fecha anterior a hoy y sin hacer. Por cada una: hacerla, reprogramarla o descartarla (lo decide la persona).
- **Postulaciones olvidadas:** en `esperando` con más de 14 días sin novedad y sin acción de seguimiento. Proponé un follow-up, buscar un contacto, o cerrarla como `sin-respuesta` (solo si la persona confirma).
- **Antimétricas:** si alguna pasó su umbral, decilo claro. Por ejemplo, demasiadas postulaciones fuera de lo que buscás o una semana sin ninguna conversación con una persona.
- **Datos pendientes** viejos en `contexto/datos-pendientes.md`.

> Las cuatro revisiones que siguen están adaptadas del `/review` de `pm-brain`, de Paweł Huryn ([pm-brain](https://github.com/phuryn/pm-brain), licencia MIT).

- **Contexto viejo:** `contexto/perfil.md` o `contexto/posicionamiento.md` sin cambios hace 6 semanas o más mientras hubo entrevistas o feedback nuevo; un informe de mercado de más de 45 días. Proponé qué actualizar, sin hacerlo.
- **Hipótesis estancadas:** las del último diagnóstico que llevan 30 días o más sin ninguna evidencia nueva en el tablero, las notas o `investigacion/`. Proponé probarlas, reformularlas o dejarlas.
- **Decisiones que piden revisión:** las de `contexto/decisiones.md` cuya condición de "Cambio de idea si..." ya se cumplió según los datos del tablero.
- **Contactos sin seguimiento:** acciones de networking o charlas hechas hace más de 3 semanas sin un próximo paso.

Cuando marques que algo dejó de sostenerse (una decisión, una hipótesis, el posicionamiento), **citá cada señal por separado, con su fecha y su fuente** ("Beta: rechazo después de la técnica, 03/11, notas-2026-11-03.md"), nunca un resumen como "el plan no está funcionando". Y **no lo resuelvas en este repaso:** la decisión sigue como está, la señal queda escrita y la persona decide en otro momento si la cambia. Lo de esta parte que no tiene datos se dice en una línea, no se rellena.

### 4. Una lectura

Dos o tres líneas: qué está funcionando y qué no, con los datos de arriba. Si hay un patrón que se repite (por ejemplo, todas las respuestas vienen de referidos, o todo se frena después de la primera charla), señalalo y sugerí el skill que lo ataca:

- `diagnostico-busqueda` si no se sabe por qué no avanza.
- `aprendizajes-busqueda` si hay feedback acumulado.
- `plan-de-networking` si los referidos funcionan y faltan contactos.
- `mejorar-perfil` o `recruiters-sinteticos` si el problema está en el primer filtro.

Marcá con 🔍 lo que es lectura tuya y no un dato.

### 5. Tres prioridades para la semana que viene

Proponé tres, concretas y con día, en una ronda con el formato de `poner-a-prueba` (se aceptan con "sí" o se cambian por número). Por ejemplo:

```
1. Pedirle referido a Martín para Acme.
   Recomendado: lunes.

2. Analizar 5 avisos nuevos de QA en fintech.
   Recomendado: martes y miércoles.

3. Preparar la entrevista técnica con Beta.
   Recomendado: jueves, el día antes.
```

Las aceptadas se suman como acciones al tablero (`postulaciones/postulaciones.json`), con fecha, prioridad alta y su pedido.

## Salida

Escribí el repaso fechado en `investigacion/<AAAA-MM-DD>-repaso-semanal.md` con las cinco partes. Aplicá en el JSON los cambios decididos (acciones reprogramadas, descartadas, nuevas; tarjetas cerradas). El cierre en el chat es de 3 líneas: lo mejor de la semana, lo que hay que cuidar y la primera acción del lunes.

## Sugerencia de rutina

Si la persona quiere que el repaso le llegue solo, explicá que puede crear una tarea programada en Claude Code (por ejemplo, viernes a las 17) que corra `/repaso-semanal` en esta carpeta. No la crees sin que lo pida.
