---
name: metricas-busqueda
description: "Arma la capa de medición de tu búsqueda: un indicador principal que cambie decisiones (por ejemplo, conversaciones con hiring managers por semana), el árbol de palancas que lo mueven y dónde se mide cada una, un número por hipótesis con su valor de hoy sacado del tablero, y las antimétricas con su umbral de alarma (postular a todo, quemarte). Escribe el Informe de métricas en investigacion/. Usala cuando digas 'cómo voy', 'cómo mido mi búsqueda', 'estoy avanzando?', 'qué número miro', o cuando diagnostico-busqueda no encuentre un número."
---

# metricas-busqueda — el Informe de métricas

> Adaptado de `product-metrics`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

`diagnostico-busqueda` exige que "si no hay un número, el problema no está claro". Este skill arma ese número: define el indicador principal de tu búsqueda, el árbol de palancas que lo sostienen y, para cada hipótesis activa, un número, cómo se mide y cuánto vale hoy.

Hablá en rioplatense, con voseo.

## Cuándo se usa

| Cuándo | Desde / hacia |
|---|---|
| El filtro de la métrica de `diagnostico-busqueda` no pasa | Viene de `diagnostico-busqueda` |
| El Informe queda escrito | Hacia `posicionamiento`, o de vuelta a `diagnostico-busqueda` con el número ya definido. `repaso-semanal` lo usa cada semana |
| Sin filtro previo | Solo |

## La entrevista

Se corre con el método de `.claude/skills/poner-a-prueba/SKILL.md#método` (citado, nunca copiado), con sus ingredientes tal cual.

Antes de preguntar:

- Si hay un Diagnóstico en `investigacion/`, leelo: las hipótesis activas salen de ahí y no se vuelven a preguntar.
- Leé `postulaciones/postulaciones.json`: es la fuente de casi todos los valores de hoy (cuántas postulaciones, en qué columna, fechas, cuántas pasaron a conversación). Calculalos vos, no los preguntes.

Cuatro pasos, en este orden:

### 1. Indicador principal

Un solo indicador candidato, con el motivo en una línea: qué decisión tuya mueve, no por qué "es importante". Si el motivo no nombra una decisión ("porque mide el éxito"), se devuelve con una repregunta.

> Ejemplo: "Conversaciones con hiring managers por semana. Si baja de 1 durante dos semanas, cambio de canal: menos postulaciones en frío y más referidos."

Conseguir el trabajo no sirve como indicador: llega una vez y no te dice nada mientras tanto.

### 2. Árbol de palancas

El indicador arriba y abajo las palancas, las variables que lo mueven si cambian. Por ejemplo:

```
Conversaciones con hiring managers por semana
├── Postulaciones dirigidas por semana          (tablero: tarjetas nuevas con fecha de envío)
├── Tasa de respuesta                           (tablero: pasan de «Esperando respuesta» a «En conversación»)
├── Referidos pedidos por semana                (tablero: acciones tipo "pedir referido" hechas)
└── Primeras charlas que pasan a entrevista     (tablero: notas de cada postulación)
```

Cada palanca lleva dónde se mide: qué campo del tablero, qué archivo o qué registro manual. Una palanca sin "dónde se mide" es un hueco, no una línea completa.

### 3. Un número por hipótesis activa

Para cada hipótesis (las que trae el Diagnóstico, o las que surjan acá si no hay): qué número la confirma o la refuta, cómo se mide y cuánto vale hoy.

**Regla firme: sin valor con fuente, no hay dato.** Un valor de hoy que no se puede citar con su origen (el tablero, un registro, una cifra fechada) no se escribe como si se pudiera: se anota como hueco con quién lo cierra, con el formato de `poner-a-prueba`. Inventar el número para que la fila quede completa está prohibido.

### 4. Antimétricas

Lo que no tiene que empeorar mientras el indicador mejora, con el umbral que dispara la alarma: un número o una condición verificable, nunca "si empeora mucho". Ejemplos:

- **Postular a todo:** más del 20% de las postulaciones de la semana fuera de `## Alcance` de `contexto/posicionamiento.md`.
- **Quemarte:** más de X horas por día dedicadas a la búsqueda durante una semana, o una semana entera sin ninguna conversación con una persona.
- **Postulaciones olvidadas:** alguna tarjeta con más de 14 días sin novedad y sin acción de seguimiento.

### La métrica de vanidad

Después de cada métrica propuesta, preguntá: **¿qué decisión cambia este número, se mueva para donde se mueva?**

Si no hay respuesta, o la respuesta es otra métrica, es de vanidad. Decilo así: "esta es una métrica de vanidad: no cambia ninguna decisión", y pedí la decisión concreta antes de aceptarla. Los ejemplos típicos en una búsqueda son las postulaciones enviadas en total, las vistas del perfil y las conexiones nuevas. No se descarta en silencio ni se acepta para no cortar la entrevista.

## El Informe de métricas

Cierra escribiendo, fechado:

```
investigacion/<AAAA-MM-DD>-metricas.md
```

Fechado y nunca pisado. Con estas cuatro secciones, en este orden y con estos títulos:

```
## Indicador principal
## Árbol de palancas
## Número por hipótesis
## Antimétricas
```

- **Indicador principal:** la métrica, el motivo en una línea (qué decisión mueve) y su valor de hoy.
- **Árbol de palancas:** cada palanca en una línea, con dónde se mide y su valor de hoy.
- **Número por hipótesis:** una entrada por hipótesis activa, con número, forma de medirlo y valor de hoy o hueco con responsable.
- **Antimétricas:** cada una con su umbral.

Si apareció una métrica de vanidad, queda escrita igual con la etiqueta "(vanidad: no cambia [la decisión que se pidió])". Nunca se borra en silencio.

Con tu visto bueno, el indicador principal y las antimétricas también se copian a `contexto/busqueda.md`, sección `## Cómo mido la búsqueda`. Esa es la versión viva que usa `repaso-semanal`.

## Lo que este entregable no es

No es un tablero de control: es la definición de qué mirar y por qué. El tablero (`tablero/tablero.html`) muestra los números; `repaso-semanal` los lee cada semana contra estos umbrales.
