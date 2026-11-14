---
name: redactar-mensaje
description: "Escribe mensajes de la búsqueda con tu voz y nunca los envía: primer contacto a un recruiter o a quien publicó un aviso, pedido de referido, pedido de charla informativa, follow-up, agradecimiento después de una entrevista, respuesta a un rechazo, aceptación o rechazo de una oferta, y avisos a tu red. Adapta el largo al canal (LinkedIn, mail, invitación de conexión) y usa solo datos reales. Usala cuando digas 'escribile a X', 'armame un follow-up', 'cómo le respondo', 'necesito un mensaje para', 'agradecé la entrevista', o desde una acción del tablero."
---

# redactar-mensaje — mensajes que suenan a vos

Los mensajes de una búsqueda tienen que ser cortos, concretos y sonar escritos por una persona. Este skill los redacta; vos los revisás y los mandás.

Hablá en rioplatense, con voseo, para explicar. El mensaje va en el idioma y el registro que corresponda (si el destinatario escribe en inglés o de usted, se responde igual).

## Antes de escribir

Leé `contexto/voz.md` (cómo escribe la persona y qué palabras no usa nunca), `contexto/busqueda.md` (cómo cuenta su salida, qué no se menciona) y, si es de una postulación, `postulaciones/<empresa-rol>/` (aviso, historial, mensajes anteriores).

Si falta saber algo esencial, preguntá en una sola ronda: a quién, por qué canal, qué pasó antes y qué querés lograr con el mensaje.

## Tipos de mensaje y su forma

| Tipo | Largo | Lo que no puede faltar |
|---|---|---|
| **Invitación de conexión en LinkedIn** | Hasta 200 caracteres (límite de LinkedIn para cuentas gratuitas; 300 en algunas) | Por qué esa persona, en una frase |
| **Primer contacto a recruiter o hiring manager** | 3 a 5 líneas | El rol concreto, por qué encajás (un logro real), un pedido claro y fácil de responder |
| **Pedido de referido** | 4 a 6 líneas | Cómo se conocen, el link al aviso, por qué encajás, facilitarle el trabajo (ofrecé mandarle un resumen para reenviar) y facilidad para decir que no |
| **Pedido de charla informativa** | Hasta 5 líneas | Ver `plan-de-networking`: por qué esa persona, 20 minutos, no es pedir trabajo |
| **Follow-up** | 2 a 4 líneas | Referencia a la postulación o charla con fecha, un dato nuevo o un aporte si lo hay, pregunta concreta. Nunca "solo quería saber si..." |
| **Agradecimiento post entrevista** | 3 a 5 líneas, el mismo día | Algo específico de la charla, por qué te entusiasma, una respuesta que quedó floja reforzada (si aplica) |
| **Respuesta a un rechazo** | 2 a 3 líneas | Agradecer, pedir feedback breve si hubo entrevista, dejar la puerta abierta |
| **Aceptar o rechazar una oferta** | Lo necesario | Claridad, fechas y agradecimiento. Para negociar, preguntá primero qué quiere lograr la persona |
| **Aviso a tu red** (post o mensaje) | Corto | Qué buscás (rol, industria, modalidad), qué hiciste con un logro, cómo pueden ayudar. Sin dramatizar la salida |

## Reglas de escritura

- **Con la voz de la persona.** Si `voz.md` está vacío, escribí simple y directo, y preguntá si suena a ella.
- **Sin frases de plantilla:** nada de "espero que este mensaje te encuentre bien", "me apasiona", "sinergia", "no dudes en contactarme".
- **Un solo pedido por mensaje**, y fácil de responder.
- **Datos reales:** todo logro o dato sale de `contexto/perfil.md`. El motivo de salida, con la frase de `busqueda.md`, sin agregar nada.
- **El nombre del destinatario**, si se sabe. Si no, no inventes uno: dejá `<nombre>`.
- **Nada de presión** ni de urgencia fingida.

## Revisión de voz

> Adaptado de `work-humanizer`, de Paweł Huryn ([product-engineering](https://github.com/phuryn/product-engineering), licencia MIT).

Todo texto que sale en nombre de la persona pasa por acá antes de entregarse: mensajes, respuestas de formularios, el Acerca de de LinkedIn, un post. Los demás skills citan esta sección (`.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`) y no la copian.

### Primero: ¿lo podría haber escrito cualquiera?

Si el mismo pedido en una línea, hecho por otra persona, daría un texto casi igual, al texto le falta lo que solo ella sabe: el ejemplo real, el número, qué pasó, qué piensa. Ninguna corrección de estilo lo arregla. Pasá al **modo entrevista**. Es lo normal en un Acerca de, un aviso a la red, un primer contacto o una respuesta abierta de formulario. Un follow-up o una confirmación de horario, con todos sus datos a mano, se escriben directo.

### Modo entrevista

- **Una sola ronda, como mucho 5 preguntas.** Cada una completa un hueco que el lector notaría, y cita la frase que su respuesta va a reemplazar.
- **Pedí que lo cuente, no que llene un formulario:** "En dos o tres frases, como se lo contarías a alguien: ¿qué pasó la primera vez que el equipo usó la automatización?" funciona mejor que "Dame un ejemplo".
- **Barato de responder:** cada pregunta se contesta en menos de un minuto, y se puede saltear.
- **El material son sus frases.** Se mantienen su orden, sus palabras raras y su forma de razonar. Solo se corrige claridad, gramática y largo. Si hay un borrador de Claude, es una lista de puntos a cubrir, no el esqueleto.
- **Una pregunta salteada** da una frase más simple o un recorte, nunca un detalle inventado.
- Si la persona escribió el texto ella misma y pide una revisión, **no lo reescribas:** señalá cada problema con su arreglo puntual, para que su voz quede.

### Lo que no cambia nunca

- **La certeza de cada dato.** "Ayudé a" no se vuelve "lideré", "cerca de 300" no se vuelve "300", "participé en" no se vuelve "armé". Es la regla de no subir el nivel, aplicada frase por frase.
- **Quién hizo qué.** Un logro del equipo sigue siendo del equipo.
- **Motivos y condiciones que la persona no dio**, aunque parezcan obvios: no se agregan.
- **Lo vago no se vuelve más vago.** Si una frase es vaga y no hay un dato para precisarla, queda como la dijo la persona o se corta.

### Muletillas a sacar

Una sola no prueba nada; varias juntas son la marca de un texto de IA.

- **Contraste con algo que nadie dijo:** "no es solo X, es Y", "más que un trabajo, un desafío". Decí Y.
- **Anuncio antes del punto:** "Te cuento:", "Lo importante es esto:", "Voy al grano:", "Tres cosas cambiaron:". El punto va directo.
- **Cierres de fórmula:** "En resumen", "Sin más", "Quedo atento a tus comentarios", "No dudes en contactarme", "Espero que este mensaje te encuentre bien". Se termina en lo último concreto o en el pedido.
- **Vocabulario inflado:** apasionado, proactivo, sinergia, desafiante, potenciar, impulsar, robusto, integral, de punta, "aportar valor", "en un mundo cada vez más...". También lo que liste `contexto/voz.md` en "no uso nunca".
- **Adjetivos sin dato atrás:** "significativo", "notable", "gran impacto". Se pega el número o el hecho de `contexto/perfil.md`, o se corta el adjetivo.
- **Tríadas por reflejo:** tres cosas solo cuando hay tres cosas.
- **Puntuación de IA:** rayas (—) y punto y coma, salvo que la persona los use; negritas sueltas; emojis de viñeta; varios signos de exclamación.
- **Ritmo parejo:** todas las frases del mismo largo, o todas arrancando igual. Variá en la dirección que haga falta, sin agregar personalidad postiza ("La verdad,", "Ojo:", un chiste que la persona no hizo).

### Control final

1. **Control de hechos, frase por frase**, contra la fuente (`contexto/perfil.md`, las respuestas de la persona): cada dato, nombre, fecha y compromiso está, con el mismo valor y la misma certeza, y no apareció ninguno nuevo.
2. **Barrido de muletillas**, buscándolas en el texto final: los ojos se las saltean.
3. **Leelo como si lo dijera la persona.** Lo que ella no diría, más simple.
4. **Opción más corta** (en textos de más de 100 palabras): tapá cada párrafo y fijate si el lector extrañaría un dato, un pedido o el punto. Si lo que sobra suma un cuarto del texto o más, ofrecé la versión corta en una línea ("Opción más corta: sacar el párrafo 2, queda un 30% más corto") sin aplicarla. Si no, "ya está ajustado". Nunca se ofrece cortar las pruebas: los ejemplos, los números, el pedido.

## Entrega

1. Pasalo por la **Revisión de voz** de arriba. Mostrá el mensaje listo para copiar, en un bloque de código, con el conteo de caracteres si el canal tiene límite.
2. Si hay dos enfoques razonables, ofrecé una alternativa corta.
3. Si es para una postulación, guardalo en `postulaciones/<empresa-rol>/mensaje-<tipo>-<AAAA-MM-DD>.md`.
4. Preguntá si lo va a mandar. Cuando confirme que lo mandó, registralo con `actualizar` (historial, acción hecha, próximo follow-up).

Ejemplo de follow-up por LinkedIn, ilustrativo y con datos ficticios (el logro y el tono salen siempre de `perfil.md` y `voz.md`):

```text
Hola Laura, ¿cómo estás? El 12/11 me postulé a QA Automation Senior en Acme.
Desde entonces terminé una certificación en Playwright, que piden en el aviso.
¿Sabés si el proceso sigue abierto?

(191 caracteres)
```

**Claude nunca envía el mensaje**, aunque tenga una herramienta de correo o de LinkedIn conectada, salvo que la persona lo pida expresamente para ese mensaje. Aun así, mostrá el texto final y el destinatario y esperá un "sí" antes de enviarlo.
