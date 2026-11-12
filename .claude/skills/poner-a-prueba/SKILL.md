---
name: poner-a-prueba
description: "Pone a prueba lo que decís de vos antes de que quede escrito: cada logro del CV, cada línea de LinkedIn, cada respuesta de entrevista y cada decisión de tu búsqueda. Repregunta con un ejemplo concreto, con un tope de intentos y salidas claras, ordena la evidencia (conducta > dato > afirmación > suposición) y anota lo que queda abierto sin inventarlo. Usala cuando pidas 'revisá mi CV', 'esto se sostiene?', 'apretame', 'cuestioname', antes de mandar una postulación importante, o cuando otro skill necesite entrevistarte: es el método que todos los demás citan."
---

# poner-a-prueba — el interrogatorio que hace creíble tu perfil

> Adaptado de `grill`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Un recruiter o un entrevistador va a repreguntar todo lo que digas. Mejor que lo haga Claude antes. Este skill tiene dos usos:

- **Solo:** pone a prueba un texto concreto (CV, perfil de LinkedIn, respuesta de entrevista, mensaje) o una decisión de la búsqueda.
- **Como método:** cualquier skill del repo que entrevista cita la sección **Método** en vez de copiarla. Puede cambiar los ejemplos o a quién apunta; el método es uno solo.

Hablá en rioplatense, con voseo, frases cortas.

## Método

Citalo como `.claude/skills/poner-a-prueba/SKILL.md#método`. Son diez ingredientes. Del 1 al 5, cómo se aprieta un dato. Del 6 al 10, cómo corre la entrevista entera.

### 1. Repregunta con un ejemplo concreto

Ante una frase que no se puede comprobar ("lideré la migración", "mejoré la performance", "el equipo me valoraba mucho"), no la aceptes ni la reformules: devolvé una repregunta que pida el hecho que hay detrás, con un ejemplo de qué sería una buena respuesta.

> Mal: "¿Podés dar más detalle?"
>
> Bien: "'Mejoré la performance' ¿medido cómo? ¿Bajó un tiempo de respuesta, se cayeron menos tickets, o es una impresión tuya? Una buena respuesta nombra el dato: 'el endpoint de búsqueda pasó de 2,1 s a 400 ms en p95 después de agregar caché'."

### 2. Como mucho dos intentos

Hasta dos repreguntas sobre el mismo dato. La tercera ya no trae información: cansa y convierte la entrevista en un interrogatorio.

### 3. Salidas

Hay dos salidas, y ninguna es seguir insistiendo:

- **Segunda resistencia:** la respuesta a la segunda repregunta sigue sin hecho. No lo descartes ni lo fuerces: anotá el hueco con quién lo cierra y seguí.
- **Evidencia fuerte de entrada:** si la primera respuesta ya trae el hecho (algo que pasó, un número medido), no hay nada que repreguntar. Se confirma y se sigue.

### 4. Jerarquía de evidencia

`conducta > dato > afirmación > suposición`. Si dos respuestas compiten por el mismo hecho, gana la que está más arriba. "Me dijeron que era el mejor del equipo" (afirmación) no pesa lo mismo que "me ascendieron dos veces en tres años" (dato) ni que "me pidieron que armara el onboarding de los nuevos" (conducta).

### 5. Los huecos se anotan, nunca se rellenan

Si un dato no se pudo cerrar, no lo completes con una inferencia para que el CV quede prolijo. Anotalo como abierto en `contexto/datos-pendientes.md`, con quién lo cierra (casi siempre vos: "buscar el número en el informe trimestral", "preguntarle a mi ex líder"). Un logro inventado se cae en la primera entrevista y arrastra todo lo demás.

### 6. Rondas según lo que depende de qué

Ordená las preguntas por lo que depende de cada una. Cada ronda junta, numeradas, todas las que ya se pueden responder. Una que depende de otra todavía abierta va a la ronda siguiente. Después de cada ronda, recalculá qué quedó respondible.

Formato de una ronda (texto plano, legible en la terminal):

```
Ronda 1

1. ¿Tu próximo rol es de individual contributor o de liderazgo?
   Recomendado: individual contributor senior, con mentoría de juniors.

2. ¿Buscás solo remoto o también híbrido?
   Recomendado: remoto o híbrido en tu ciudad.
```

Respondés "sí" para aceptar todas las recomendaciones, o por número para cambiar alguna. El número, la pregunta y la recomendación van siempre en líneas separadas.

> Mal: un mensaje largo con seis preguntas, tres de las cuales dependen de la primera.
>
> Bien: la ronda 1 pregunta qué rol buscás y en qué industria. La ronda 2, con eso respondido, pregunta qué logros destacar, que depende de las dos.

### 7. Una recomendación que se acepta con "sí"

Cada pregunta trae la respuesta que Claude recomienda, escrita para que "sí" la acepte. Estar de acuerdo nunca obliga a decir "no".

> Mal: "Recomendado: ¿no poner el puesto de 2015?" (para estar de acuerdo hay que decir "no")
>
> Bien: "Recomendado: sacar el puesto de 2015 y dejarlo en 'Experiencia anterior'."

### 8. Los hechos se buscan, las decisiones se preguntan

Lo que el repo ya sabe (tu `contexto/perfil.md`, el PDF de LinkedIn, el CV, una postulación anterior) lo busca Claude y no te lo pregunta. Si lo que encuentra contradice lo que dijiste, te muestra la contradicción. La repregunta del ingrediente 1 queda para lo que solo vos sabés. Las decisiones son siempre tuyas.

Si hay subagentes disponibles, la búsqueda va a uno y la ronda sigue con lo que no depende de ese dato. Si no, se busca antes de la ronda que lo necesita.

> Mal: "¿Cuántos años estuviste en tu último trabajo?" (está en el PDF de LinkedIn)
>
> Bien: "Tu LinkedIn dice marzo 2021 a octubre 2026 y el CV dice 2020. ¿Cuál es la correcta?"

### 9. Las palabras vagas se precisan

Antes de la primera ronda, leé `contexto/perfil.md`. Si usás una palabra que choca con lo que ya está escrito ahí, o una palabra vaga o con dos sentidos ("lideré", "experto", "full stack", "senior", "arquitecto"), te frena en ese momento: propone el término preciso y un caso límite que lo pruebe.

> Mal: decís "lideré el equipo" y el perfil dice que eras desarrollador sin reportes directos. La entrevista sigue.
>
> Bien: "Tu perfil dice que no tenías reportes directos y acabás de decir 'lideré el equipo'. Propongo: 'fui referente técnico de un equipo de 5'. Caso límite: ¿definías vos las prioridades del sprint, o las definía otra persona? Recomendado: 'referente técnico'."

Una formulación precisa se escribe en `contexto/perfil.md` cuando la aceptás en una ronda, no al final.

### 10. Se cierra cuando no queda nada abierto y lo confirmás

Termina cuando no queda ninguna pregunta respondible sin responder y confirmás que los dos entienden lo mismo. Antes de esa confirmación, lo único que se escribe son formulaciones precisas (ingrediente 9), huecos (5) y decisiones. No se arma ningún entregable ni se manda nada.

> Mal: respondés la última pregunta y Claude ya empieza a reescribir el CV.
>
> Bien: "No queda nada respondible abierto. Anoté dos huecos. ¿Entendemos lo mismo: buscás un rol de backend senior en fintech, remoto, y el logro principal es la migración de pagos? Sí para cerrar."

## Uso solo

Ponés a prueba un texto o una decisión. Si no dijiste cuál, preguntá en una línea: ¿CV, LinkedIn, una respuesta de entrevista, un mensaje, o una decisión de la búsqueda?

1. Leé `contexto/perfil.md` y el texto a probar.
2. Corré el método sobre cada afirmación que no se pueda comprobar.
3. Distribuí lo que sale. No inventes otros destinos:

| Lo que sale | Dónde va |
|---|---|
| Un dato confirmado o una formulación precisa | `contexto/perfil.md` |
| Un hueco | `contexto/datos-pendientes.md`: una línea con el dato, quién lo cierra y la fecha |
| Una decisión de la búsqueda | `contexto/decisiones.md`: una línea con fecha y la decisión |
| El texto revisado (si lo pediste) | Junto al original, con sufijo `-revisado` (por ejemplo, `cv/cv-revisado.md`) |

Si para seguir haría falta escribir en un destino que no está en esta tabla, decilo y frená.

## Decisiones clave

Todas las decisiones se anotan. Una **decisión clave** se marca con ⭐ en `contexto/decisiones.md` para que quien abra la búsqueda la lea antes que el resto. **Es clave solo si se cumplen las tres condiciones. Dos de tres no alcanzan:**

1. **Difícil de deshacer:** volver atrás cuesta trabajo, plata o credibilidad.
2. **Sorprende sin contexto:** alguien que no estuvo en la conversación no la adivinaría.
3. **Sale de un trade-off real:** había una alternativa concreta y se descartó.

> Clave: "Dejo de postularme a roles de desarrollo y me enfoco en DevRel". Volver atrás implica rehacer el CV y el perfil (1), alguien que ve tu trayectoria esperaría lo contrario (2) y se evaluó seguir como backend (3).
>
> No clave: "Reviso el tablero los lunes". Se cambia fácil (falla la 1), no sorprende a nadie (falla la 2) y no se descartó nada (falla la 3).

**Claude propone la marca y vos la confirmás.** Antes de marcarla, mostrá la decisión con las tres condiciones al lado y cuál se cumple. Marcala solo si la aceptás. Si falla una condición, no la propongas: decí cuál falla.
