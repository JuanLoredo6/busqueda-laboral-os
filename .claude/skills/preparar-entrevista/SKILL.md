---
name: preparar-entrevista
description: "Prepara una entrevista con un método de criterio, no de respuestas de memoria: según el tipo (RR. HH., comportamiento, técnica, caso, hiring manager, panel) arma las preguntas probables, las preguntas que conviene hacer antes de responder, la estructura de cada respuesta atada a una historia real de tu perfil y lo que el entrevistador evalúa, y después te toma un simulacro y te devuelve feedback. Sirve para cualquier perfil IT. Usala cuando digas 'tengo una entrevista', 'preparame para X', 'qué me pueden preguntar', 'tomame la entrevista', 'hagamos un mock', o desde una acción del tablero."
---

# preparar-entrevista — llegar con criterio, no con un guion

La mayoría de las preguntas de entrevista no tienen una respuesta correcta: se evalúa cómo pensás. Los buenos candidatos no se apuran: preguntan antes de responder, deciden, explican lo que ceden y se apoyan en experiencias reales. Este skill entrena eso.

Hablá en rioplatense, con voseo, frases cortas. Si la entrevista es en inglés, las respuestas modelo van en inglés y las indicaciones en español.

## Antes de empezar

Leé siempre:

- `contexto/perfil.md`, sobre todo **Historias para entrevistas**: es la única fuente de ejemplos.
- `contexto/busqueda.md`: cómo contar la salida y qué no se menciona nunca.
- `contexto/voz.md`: las respuestas tienen que sonar dichas por la persona.
- `postulaciones/<empresa-rol>/` (`rol.md`, historial, respuestas) y `entrevistas/<empresa>/` si ya hay algo preparado.

Si no se sabe con quién es la entrevista, el formato, el idioma o la duración, preguntalo en una línea. Esas cuatro cosas cambian qué se prepara.

Si en el perfil hay menos de tres historias para entrevistas, antes de preparar nada proponé una ronda corta para sumar dos o tres (con `poner-a-prueba`): son la base de todo.

## Los tipos de entrevista y qué pesa en cada uno

| Tipo | Qué evalúan | Qué preparar |
|---|---|---|
| **RR. HH. / primera charla** | Motivación, encaje con la cultura, condiciones, cómo contás tu historia | Pitch de 1 minuto ("contame de vos"), por qué esta empresa, motivo de salida con la frase acordada, disponibilidad. La pretensión salarial solo si la persona decidió qué decir |
| **Comportamiento** | Cómo actuaste en situaciones reales | 5 a 7 historias del perfil en formato situación → qué hiciste vos → resultado → qué aprendiste |
| **Técnica** | Cómo razonás un problema técnico | Usá `.claude/skills/criterio-tecnico/SKILL.md` |
| **Caso de producto o negocio** | Cómo pasás de un problema ambiguo a una decisión | Usá `.claude/skills/criterio-producto/SKILL.md` |
| **Hiring manager** | Si resolviste problemas como los del equipo y cómo trabajás | Lo que le duele al equipo (del aviso y de la investigación), 2 historias que lo respondan, preguntas sobre el equipo |
| **Panel o ronda final** | Todo lo anterior, más consistencia | Repaso de todo, sobre todo lo que se dijo en rondas anteriores |

## Las familias de preguntas de comportamiento

Las preguntas cambian, las familias se repiten. Traducilas al dominio de la empresa:

1. **Un problema difícil que resolviste.** Evalúan: si entendiste el problema antes de resolverlo.
2. **Un conflicto con alguien** (compañero, líder, cliente). Evalúan: si escuchás, si separás a la persona del problema, cómo cerró.
3. **Una decisión con información incompleta.** Evalúan: si decidís, qué supuestos declaraste, qué cediste.
4. **Un error o un fracaso.** Evalúan: honestidad, si te hacés cargo y qué aprendiste. No hay truco: importa menos el error que lo que hiciste después.
5. **Prioridades en conflicto o poco tiempo.** Evalúan: cómo elegís y cómo comunicás lo que queda afuera.
6. **Aprender algo rápido.** Evalúan: cómo aprendés. Cada vez más: cómo usás herramientas de IA en tu trabajo.
7. **Influir sin autoridad o liderar** (según seniority). Evalúan: cómo lográs que otros se muevan.

## Modo 1: preparación escrita

1. **Elegí qué pesa** según el tipo de entrevista. Decí por qué en una línea.
2. **Por cada pregunta probable** (de 6 a 10 en total):
   - **La pregunta**, traducida a la empresa y al rol (con lo que dicen `rol.md` y la investigación).
   - **Lo que conviene preguntar antes de responder**, si aplica (en casos y técnicas, siempre).
   - **Cómo armar la respuesta:** la estructura para pensar en voz alta, no un texto para memorizar.
   - **La historia real que la sostiene**, citando `contexto/perfil.md` (📌 con la sección). Si ninguna encaja, marcalo ❓ y preguntá si hay una. **Nunca la inventes.**
   - **Lo que están evaluando**, en una línea.
   - **El objetivo de tiempo:** casi todas entre 1 y 2 minutos.
3. **Las preguntas difíciles de esta persona** (huecos en el CV, salida reciente, cambio de rol, sobrecalificación), con la forma de responderlas según `busqueda.md`.
4. **Preguntas para hacerle a la empresa:** 3 o 4 que muestren criterio (qué problema tiene hoy el equipo, cómo se mide el éxito en el rol a los 6 meses, qué decisión difícil tienen abierta).
5. **Repaso de 5 minutos:** una lista corta para leer antes de entrar.
6. Guardalo en `entrevistas/<empresa>/preparacion-<tipo>.md`. Si ya existe una preparación para esa empresa, sumá una sección en vez de pisarla.

Marcas: 📌 dato literal de una fuente, con su ubicación · 🔍 lectura tuya que ninguna fuente afirma · ❓ dato que falta y completa la persona.

## Modo 2: simulacro

Cuando la persona pida que le tomes la entrevista:

1. Hacé **una pregunta por vez**, como lo haría ese entrevistador, y esperá la respuesta. No adelantes pistas.
2. Actuá como un entrevistador real: si te hace preguntas, respondelas con datos razonables del caso. Si salta a una solución sin preguntar nada, dejalo seguir. La evaluación viene después.
3. Después de cada respuesta, en pocas líneas:
   - **¿Frenó a entender antes de responder?** (en casos y técnicas)
   - **¿Respondió lo que le preguntaron?** ¿Con estructura?
   - **¿Usó un ejemplo real?** ¿Coincide con `contexto/perfil.md`? Si dijo algo que el perfil no tiene y es real, preguntá si lo sumás.
   - **¿Duración razonable?**
   - **Lo que el entrevistador se lleva**, en una frase, y **una** mejora concreta.
4. Al terminar: la respuesta más fuerte, la más floja y qué practicar antes de la entrevista. Si quiere, guardalo en `entrevistas/<empresa>/simulacro-<AAAA-MM-DD>.md`.

Si la persona prefiere practicar en voz alta, sugerí que use el dictado de su sistema o de la app de Claude y pegue la transcripción.

## Después de la entrevista

Ofrecé, en la misma sesión o cuando vuelva:

- Anotar cómo fue (preguntas que hicieron, qué salió bien, qué no) en `entrevistas/<empresa>/notas-<AAAA-MM-DD>.md`. Es la materia prima de `aprendizajes-busqueda`.
- El agradecimiento del mismo día con `redactar-mensaje`.
- Actualizar el tablero con `actualizar`.

## Reglas

- No inventes logros, números, decisiones ni aprendizajes. Todo ejemplo sale de `contexto/perfil.md` o de lo que la persona confirme.
- Respetá lo que `contexto/busqueda.md` dice sobre la salida y lo que no se menciona.
- Las respuestas modelo son un esqueleto, no un discurso. Si suenan pulidas o de manual, reescribilas más simples, con la voz de `contexto/voz.md`.
- Antes de entregar, revisá cada ejemplo contra el perfil y decí qué no pudiste comprobar.
