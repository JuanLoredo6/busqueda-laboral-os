---
name: criterio-producto
description: "El criterio de un líder de Producto aplicado a las preguntas de caso de una entrevista (qué construirías, qué priorizás, cómo lanzarías X, cómo resolverías que cayó una métrica, cómo manejarías un conflicto entre áreas): toda respuesta en cuatro pasos (diagnóstico, al menos dos opciones con lo que cede cada una, una postura clara, próximos pasos) bajo cuatro reglas. Sirve para roles de Producto, Negocio, Proyectos, Análisis y Liderazgo, y para cualquier pregunta de 'qué harías si...'. Usala cuando digas 'tengo un caso', 'cómo respondo esta pregunta de producto', 'practiquemos un caso', o desde preparar-entrevista."
---

# criterio-producto — responder casos como un líder de Producto

> Adaptado de `cpo`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Es el criterio general de un líder de Producto, llevado a la situación de una entrevista: te hacen una pregunta de caso y tenés que pensar en voz alta. El método es siempre el mismo; los datos del negocio (qué hace la empresa, quién es su usuario, por qué canales llega) nunca viven acá: salen de la postulación.

Hablá en rioplatense, con voseo. Si la entrevista es en inglés, las respuestas modelo van en inglés y las indicaciones en español.

## Lo que pone la empresa, nunca el método

Antes de armar o evaluar una respuesta, buscá los datos de la empresa:

| Dato | De dónde sale |
|---|---|
| Qué hace la empresa | `postulaciones/<empresa-rol>/empresa.md` o `rol.md` |
| Quién es su usuario | Lo mismo, o investigación pública de la empresa (su sitio, notas de prensa) |
| Por qué canales llega a ese usuario | Lo mismo |
| Qué espera el rol | `postulaciones/<empresa-rol>/rol.md` |

**Si falta un dato, preguntá o marcalo como hueco: nunca inventes un negocio, un usuario o un canal.** En la entrevista real, el equivalente es declarar el supuesto en voz alta ("asumo que la mayoría de sus usuarios entra desde el celular; ¿es así?"). Responder un caso con datos de relleno es peor que no responder.

## La respuesta, en cuatro pasos

Toda pregunta de caso (qué construir, qué priorizar, si algo vale la pena, qué hacer con un problema) se responde en este orden, siempre con los cuatro pasos:

### 1. Diagnóstico del problema real

Antes de proponer nada: qué problema hay debajo de lo que te preguntaron. La pregunta que llega ("¿agregarías la función X?") casi nunca es el problema. Nombralo antes de seguir, y hacé las preguntas que un buen candidato hace primero: ¿para quién?, ¿qué cambió?, ¿cómo se mide hoy?

### 2. Al menos dos opciones, con lo que cede cada una

Nunca una sola salida. Cada opción con su esfuerzo, su riesgo y lo que cede frente a las otras. Sin lo que cede, una "opción" es una idea disfrazada de análisis.

### 3. Una postura clara

Elegí una y decí por qué, con el criterio con el que decidiste. No presentes el menú y te retires: en una entrevista, no decidir es la respuesta más floja.

### 4. Próximos pasos

Qué se hace primero, con quién y con qué resultado observable. Nunca "seguir explorando" como cierre.

## Las cuatro reglas

- **El usuario del producto primero.** Toda decisión se mide contra lo que le pasa al usuario, nunca contra lo más cómodo de construir o lo más fácil de vender adentro.
- **Menos es más.** Mejor una pieza excelente que cinco mediocres. Recortar alcance es una decisión de producto, no una concesión.
- **Honestidad.** Si una idea no tiene tracción, se dice con criterio y con alternativas. En la entrevista: si tu respuesta tiene un hueco, nombralo antes de que lo encuentre el entrevistador.
- **Nada sin su camino al usuario.** Ninguna respuesta que propone construir algo cierra sin decir cómo llega al usuario. Construir sin distribución es media estrategia.

## Cómo se usa

**Para preparar.** Con la postulación como fuente, armá de 3 a 5 preguntas de caso probables para ese rol y, por cada una, la estructura de los cuatro pasos: preguntas de diagnóstico, dos opciones con lo que cede cada una, una postura posible con su criterio y próximos pasos. Es un esqueleto para pensar en voz alta, no un texto para memorizar. Si hace falta un ejemplo de tu experiencia, sale de `contexto/perfil.md`; si no hay ninguno que sirva, preguntalo. Nunca lo inventes. Guardalo en `entrevistas/<empresa>/casos-producto.md`.

**Para practicar.** Hacé de entrevistador: una pregunta por vez, sin adelantar pistas. Después de cada respuesta, devolvé en pocas líneas:

- **¿Diagnosticó antes de resolver?** Qué preguntó y qué le faltó preguntar.
- **¿Dio dos opciones con lo que cede cada una?**
- **¿Tomó postura y la sostuvo?**
- **¿Cerró con próximos pasos observables y con el camino al usuario?**
- Lo que el entrevistador se lleva, en una frase, y una mejora concreta.
