# Criterio de producto — responder casos como un líder de Producto

> Es parte de `preparar-entrevista` (`.claude/skills/preparar-entrevista/SKILL.md`). Se carga para entrevistas de caso de producto o negocio, o cuando la persona quiere practicar o resolver una pregunta de caso, aunque no tenga una entrevista agendada. Sirve para roles de Producto, Negocio, Proyectos, Análisis y Liderazgo, y para cualquier pregunta de "qué harías si...".

> Adaptado de `cpo`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Es el criterio general de un líder de Producto, llevado a la situación de una entrevista: te hacen una pregunta de caso y tenés que pensar en voz alta. El método es siempre el mismo; los datos del negocio (qué hace la empresa, quién es su usuario, por qué canales llega) nunca viven acá: salen de la postulación.

Hablá en rioplatense, con voseo (o en portugués de Brasil si es el idioma de la conversación; ver «Idioma» en `CLAUDE.md`). Si la entrevista es en inglés o en portugués, las respuestas modelo van en ese idioma y las indicaciones en el idioma de la conversación.

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

## Los tipos de pregunta de Producto

> La clasificación toma como referencia [Product Manager Interview Questions](https://www.productcompass.pm/p/product-manager-interview-questions), de Paweł Huryn (The Product Compass). Ese artículo no tiene licencia abierta: no se copió texto; los ejemplos son propios y usan productos de la región. Son ilustrativos: en la preparación real, la pregunta se arma con el producto de la empresa.

Todas se responden con los cuatro pasos. Cambia dónde está el peso:

| Tipo | Qué evalúan | Dónde pesa la respuesta | Ejemplos |
|---|---|---|---|
| **Product sense** (mejorar o diseñar algo) | Empatía con el usuario, creatividad, conexión con el negocio sin irse a la estrategia | Diagnóstico: quién es el usuario, qué trabajo quiere resolver y cómo mide el éxito; recién después, dolores | "Mejorá Mercado Pago para alguien que cobra por primera vez con QR." · "Diseñá una función de Rappi para pedidos en grupo en una oficina." · "¿Cómo harías que más personas mayores de 60 usen la app de un banco digital?" |
| **Estrategia** | Si ves el mercado, la competencia y dónde jugar | Opciones y postura: qué se gana y qué se cede en cada camino | "¿Debería una billetera virtual lanzar crédito para comercios? ¿Por qué ahora o por qué no?" · "Un competidor regional bajó comisiones a cero: ¿qué hacés?" |
| **Analítica y métricas** | Si separás síntoma de causa con datos | Diagnóstico: segmentar antes de concluir | "Los pedidos semanales cayeron 10 %: ¿qué mirás primero?" · "¿Cuál sería la métrica principal de un marketplace de servicios para el hogar?" |
| **Ejecución** | Cómo llevás una decisión a un lanzamiento | Próximos pasos: orden, dependencias, cómo se mide el éxito | "Tenés que lanzar un nuevo medio de pago en tres países: ¿cómo lo planificás?" · "El lanzamiento se atrasa dos semanas: ¿qué recortás?" |
| **Técnica para Producto** | Si hablás con Tecnología sin ser ingeniero | Diagnóstico y opciones: el costo técnico de cada camino | "¿Cómo le explicarías una API a alguien de Comercial?" · "Tecnología propone reescribir el checkout: ¿cómo decidís si vale la pena?" |

En **product sense**, los cuatro pasos se recorren así:

1. **Diagnóstico:** quién es el usuario (elegí un segmento y decí por qué), qué trabajo quiere resolver y cuáles son sus dolores principales.
2. **Opciones:** varias soluciones antes de quedarte con una; no recortes ideas demasiado temprano.
3. **Postura:** elegí por impacto en el usuario y esfuerzo, y decí qué queda afuera.
4. **Próximos pasos:** la prueba más barata que podría refutarla (un prototipo, una prueba a mano) y la métrica de éxito, atada a la experiencia del usuario y no solo al negocio.

## Cómo se usa

**Para preparar.** Con la postulación como fuente, armá de 3 a 5 preguntas de caso probables para ese rol y, por cada una, la estructura de los cuatro pasos: preguntas de diagnóstico, dos opciones con lo que cede cada una, una postura posible con su criterio y próximos pasos. Es un esqueleto para pensar en voz alta, no un texto para memorizar. Si hace falta un ejemplo de tu experiencia, sale de `contexto/perfil.md`; si no hay ninguno que sirva, preguntalo. Nunca lo inventes. Guardalo en `entrevistas/<empresa>/casos-producto.md` (o en `entrevistas/practica/` si es práctica sin postulación).

**Para practicar.** Hacé de entrevistador: una pregunta por vez, sin adelantar pistas. Después de cada respuesta, devolvé en pocas líneas:

- **¿Diagnosticó antes de resolver?** Qué preguntó y qué le faltó preguntar.
- **¿Dio dos opciones con lo que cede cada una?**
- **¿Tomó postura y la sostuvo?**
- **¿Cerró con próximos pasos observables y con el camino al usuario?**
- Lo que el entrevistador se lleva, en una frase, y una mejora concreta.

## Ejemplo de esqueleto

Ilustrativo, con una empresa ficticia: es un esqueleto para pensar en voz alta, no un texto para memorizar.

```text
Pregunta: "La conversión del checkout cayó 15% este mes. ¿Qué hacés?"

1. Diagnóstico: ¿cayó en todos los canales o en uno? ¿Desde qué fecha? ¿Hubo un release, un cambio de precios o de medio de pago? ¿Cómo se mide hoy la conversión?
2. Opciones:
   a. Revertir el último cambio del checkout: rápido y de bajo riesgo, pero cede aprender qué lo rompió.
   b. Segmentar la caída antes de tocar nada: un día más de pérdida, a cambio de atacar la causa real.
3. Postura: b, salvo que la caída coincida exacto con un release; en ese caso, a, y se investiga después.
4. Próximos pasos: hoy, cortar los datos por canal y dispositivo con el equipo de datos; mañana, decisión con el dato a la vista; aviso a Soporte para que reporte quejas sobre el checkout.
```
