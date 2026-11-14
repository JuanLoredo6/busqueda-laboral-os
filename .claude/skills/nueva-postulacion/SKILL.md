---
name: nueva-postulacion
description: "Registra y prepara una postulación: crea o completa su carpeta en postulaciones/ (una por empresa y rol), adapta el CV al aviso sin inventar nada, responde las preguntas del formulario con tu voz, redacta la carta o el mensaje si hace falta, y suma o mueve la tarjeta en el tablero con su seguimiento. Nunca envía nada. Usala cuando digas 'me quiero postular a X', 'ayudame con este formulario', 'ya me postulé a X', 'registrá esta postulación', o después de analizar-oferta."
---

# nueva-postulacion — preparar y registrar una postulación

Deja cada postulación preparada y registrada igual que las demás, para que dentro de tres semanas sepas qué mandaste, cuándo y qué sigue.

Hablá en rioplatense, con voseo.

## Dos casos

- **Todavía no te postulaste:** se prepara todo y después se registra el envío.
- **Ya te postulaste:** se registra directo (saltá al paso 5) y se crea el seguimiento.

## Paso 1: la carpeta

- Si viene de `analizar-oferta`, la carpeta `postulaciones/<empresa-rol>/` y su `rol.md` ya existen. Leelos.
- Si no, pedí el link o el texto del aviso, creá la carpeta (minúsculas, con guiones) y guardá en `rol.md`: link, fecha, un resumen propio con ubicación, modalidad y requisitos excluyentes, y el aviso original pegado al final. Si no hay análisis previo, ofrecé correr `analizar-oferta` primero (2 minutos).

Leé `contexto/perfil.md`, `contexto/busqueda.md`, `contexto/voz.md` y, si existe, `contexto/posicionamiento.md`.

## Paso 2: CV adaptado

Partí del CV vigente en `cv/` (o de `contexto/perfil.md` si no hay CV).

- **Reordená y enfatizá; no inventes.** Se puede: cambiar el titular hacia el rol del aviso, subir los logros que responden a lo que piden, usar los términos del aviso donde sean verdad ("CI/CD" en vez de "automatización de despliegues"), recortar lo que no aporta.
- **No se puede:** agregar tecnologías, logros, cargos o años que el perfil no tenga.
- El CV adaptado sigue cumpliendo `.claude/skills/mejorar-perfil/SKILL.md#criterios-de-cv`.
- Guardá el contenido en `postulaciones/<empresa-rol>/cv.md` con una lista corta al principio de qué cambió respecto del CV base y por qué.
- Si el formato lo pide, ofrecé generar el .docx o PDF (ver `mejorar-perfil`, paso 5).

Si el cambio es mínimo, decilo y recomendá mandar el CV base: no hace falta adaptar todo.

## Paso 3: formulario

Si el formulario tiene preguntas abiertas, pedí que las pegue. Para cada una:

- Respuesta con su voz (`contexto/voz.md`), corta y concreta, con un ejemplo real de `contexto/perfil.md` (📌 con la sección).
- Las preguntas delicadas siguen `contexto/busqueda.md`:
  - **Motivo de salida:** usá la frase acordada, sin agregar detalles.
  - **Pretensión salarial:** no la completes. Marcala ❓ y preguntale qué quiere poner, salvo que `busqueda.md` diga otra cosa.
  - **Disponibilidad y ubicación:** lo que diga `busqueda.md`.
- Datos personales (documento, dirección, teléfono): no los pidas ni los escribas. Los completa la persona directamente en el formulario.

Cada respuesta abierta pasa por la revisión de `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz` antes de entregarse. Si una respuesta "la podría haber escrito cualquiera" (por qué esta empresa, por qué este rol), usá su modo entrevista.

Guardá preguntas y respuestas en `postulaciones/<empresa-rol>/respuestas.md`.

## Paso 4: mensaje o carta (si suma)

Si hay alguien a quien escribirle (quien publicó el aviso, un recruiter, un contacto que puede referirte), ofrecé un mensaje corto con `redactar-mensaje`. Una carta de presentación solo si la piden o si hay una brecha que conviene abordar de frente.

## Paso 5: registrar

Cuando la persona confirme que **ya envió** (Claude nunca envía):

En `postulaciones/postulaciones.json`, con el modelo de datos de `CLAUDE.md`:

- La tarjeta pasa a `"columna": "esperando"`, con `enviada` y `ultimaNovedad` con la fecha de envío, `canal` (portal, LinkedIn, mail, referido), `contacto` si hay, `estado` en una frase ("Postulado por el portal el 12/11") y `proximo` ("Esperar respuesta; follow-up el 19/11").
- Sumá una línea al `historial`.
- Marcá como hecha la acción "Postularme a <empresa>" si existía.
- Creá la acción de seguimiento: "Follow-up a <empresa> si no respondió", con fecha 7 días después (5 días hábiles), `condicion: "solo si no hubo respuesta"` y pedido `/redactar-mensaje follow-up <empresa-rol>`. Si el canal fue un portal sin contacto, la acción es "Buscar un contacto en <empresa> para hacer seguimiento".

Si todavía no envió: dejá la tarjeta en «Por enviar» con `proximo: "Enviar"` y una acción con fecha para enviarla.

## Cierre

Una línea con lo que quedó en la carpeta, la tarjeta y la próxima acción con su fecha. Si el tablero está abierto, se actualiza solo.

Ejemplo, ilustrativo y con datos ficticios:

```text
Listo: en postulaciones/acme-qa-automation-senior/ quedaron el CV adaptado (titular y 2 logros reordenados)
y 3 respuestas del formulario. La tarjeta está en «Esperando» desde hoy (portal).
Próxima acción: follow-up a Acme el 19/11, solo si no respondieron.
No pude comprobar en tu perfil "liderazgo de 4 personas": confirmalo o lo saco.
```

## Reglas

- Claude no envía postulaciones, mensajes ni formularios. Prepara y registra.
- Nada en el CV ni en las respuestas que no esté en `contexto/perfil.md` o que la persona no confirme.
- Antes de cerrar, revisá cada respuesta contra el perfil y decí qué no pudiste comprobar.
