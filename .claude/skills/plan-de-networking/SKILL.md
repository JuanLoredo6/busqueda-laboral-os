---
name: plan-de-networking
description: "Diseña una ronda de charlas con gente de la industria (personas que contratan, ex compañeros, gente que ya tiene el rol al que apuntás) para validar la hipótesis más riesgosa de tu búsqueda: a quién buscar según lo que hizo y no según el cargo, qué formato usar, la guía de preguntas atadas a la hipótesis y el mensaje para pedir la charla. Escribe el Plan de networking en investigacion/. Usala cuando digas 'con quién hablo', 'cómo hago networking', 'quiero pedir una charla', 'cómo sé si esto es así', o después de diagnostico-busqueda o mercado-laboral."
---

# plan-de-networking — el Plan de networking

> Adaptado de `ux-research`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Diseña la ronda de conversaciones que ataca la hipótesis más riesgosa de tu Diagnóstico (nunca todas juntas) y cierra con un plan listo para probar. Las charlas informativas no son pedir trabajo: son pedir 20 minutos para entender cómo contrata una empresa o qué pide un rol. Muchas veces terminan en una recomendación, pero ese no es el objetivo de la charla.

Hablá en rioplatense, con voseo.

## Cuándo se usa

| Cuándo | Desde / hacia |
|---|---|
| Ya hay un Informe de `mercado-laboral` o un Diagnóstico | Viene de `mercado-laboral` o `diagnostico-busqueda` |
| El Plan queda escrito | Hacia `recruiters-sinteticos`, para probar la guía y el mensaje antes de usarlos |
| Sin Informe de mercado | Solo, con el Diagnóstico como entrada mínima; sin eso, preguntá qué querés averiguar |

## La entrevista

Se corre con el método de `.claude/skills/poner-a-prueba/SKILL.md#método` (citado, nunca copiado) sobre la elección de la hipótesis, el criterio para elegir a quién y cada pregunta de la guía.

### Un objetivo por ronda

Cada ronda ataca una sola hipótesis: la primera del Diagnóstico, con la misma priorización (riesgo × impacto × barato de probar) que ya hizo `diagnostico-busqueda`. Su criterio para abandonarla es lo que la ronda tiene que poder confirmar o descartar. Si pedís "averiguar todo junto", apretá: ¿cuál te cuesta más si resulta falsa? Esa va en esta ronda; las otras esperan.

### A quién: por lo que hizo, no por el cargo

El criterio de a quién buscar se escribe en conducta verificable, nunca solo en cargo o empresa. "Gente de IT" o "recruiters" no es un criterio. "Personas que en los últimos 12 meses contrataron a un QA para un equipo de pagos" sí, y "gente que pasó de soporte a desarrollo en los últimos 3 años" también. Si el criterio es demasiado amplio, repreguntá: ¿qué tuvo que haber hecho esta persona para que su respuesta te sirva?

Fuentes para encontrarlas: tu red de LinkedIn (primer y segundo grado), ex compañeros, comunidades del rubro, la lista de empresas objetivo de `mercado-laboral`. Nunca se arma una lista de datos personales sacados de cualquier lado: se trabaja con perfiles públicos y con tu propia red.

### Explorar → charlas; dimensionar → encuesta

El formato lo decide la pregunta de la ronda:

- Si la pregunta es "¿por qué pasa esto?" o "¿cómo contratan hoy?": **charlas** de 20 minutos, de 3 a 6 personas, en profundidad.
- Si la pregunta es "¿a cuántos les pasa?" o "¿qué tan seguido?": **encuesta** corta o una publicación con pregunta en una comunidad.

Mezclar los dos sin decidir cuál manda da un plan sin foco. Se elige uno y se dice por qué.

### Por qué una empresa abre un puesto: cuatro fuerzas

Cuando la ronda explora por qué una empresa contrata un rol como el tuyo, la guía cubre las cuatro fuerzas, no solo los requisitos técnicos:

| Fuerza | Qué busca entender |
|---|---|
| Empuje | Qué les duele hoy sin esa persona: qué se atrasa, qué se rompe, quién está sobrecargado |
| Atracción | Qué esperan que cambie cuando entre la persona correcta |
| Ansiedad | Qué miedo tienen al contratar: que no encaje, que se vaya pronto, que le falte seniority |
| Hábito | Cómo lo resuelven hoy sin contratar: horas extra, un freelancer, una agencia, una herramienta de IA |

Una guía que solo pregunta "¿qué tecnologías piden?" cubre una de las cuatro y vuelve incompleta.

### La técnica madre: la última vez real

La pregunta madre de cualquier guía no es "¿qué opinás de...?". Es "contame la última vez que [situación]": reconstruir paso a paso qué pasó, cuándo, con quién, qué hicieron antes y después.

> Mal: "¿Qué buscan las empresas en un QA?"
>
> Bien: "Contame la última vez que contrataron a alguien de QA en tu equipo. ¿Cómo arrancó la búsqueda? ¿Qué CV pasaron el primer filtro y por qué? ¿Qué hizo que eligieran a esa persona?"

Las preguntas de opinión ("¿te parece que...?") salen de la guía, salvo para cerrar la charla.

### Cada pregunta atada, o sale

Cada pregunta de la guía se ata explícitamente a la hipótesis de la ronda o a una de las cuatro fuerzas. Una pregunta que no se ata a nada sale de la guía: "por las dudas" no es un criterio.

### El mensaje para pedir la charla

Corto (hasta 5 líneas), con tu voz (`contexto/voz.md` si existe):

- Por qué esa persona (lo que hizo, del criterio de arriba).
- Qué pedís: 20 minutos para entender algo concreto.
- Que no estás pidiendo trabajo.
- Facilidad para decir que no.

**Claude no envía ningún mensaje.** Lo redacta y vos lo mandás.

## El Plan de networking

Cierra escribiendo, fechado:

```
investigacion/<AAAA-MM-DD>-plan-networking.md
```

Fechado y nunca pisado. Con estas cinco secciones, en este orden y con estos títulos:

```
## Objetivo de la ronda
## A quién buscar
## Formato
## Guía de preguntas
## Mensaje para pedir la charla
```

- **Objetivo de la ronda:** la hipótesis elegida y por qué es la más riesgosa.
- **A quién buscar:** el criterio en conducta verificable y, si se los identificó, de 3 a 6 nombres o perfiles con el motivo de cada uno.
- **Formato:** charla o encuesta, con la pregunta que lo decide.
- **Guía de preguntas:** cada pregunta con la hipótesis o la fuerza a la que se ata.
- **Mensaje para pedir la charla.**

Al final, ofrecé sumar una acción por persona al tablero ("Pedirle charla a <nombre>") en `postulaciones/postulaciones.json` (ver `CLAUDE.md`).

## Lo que este entregable no es

Es la versión 1 de la guía: todavía no se probó. Probarla contra personajes simulados antes de la primera charla real es trabajo de `recruiters-sinteticos`. Procesar lo que digan las personas reales es trabajo de `aprendizajes-busqueda`.
