---
name: mejorar-perfil
description: "Mejora tu perfil de LinkedIn y tu CV a partir de lo que tengas más completo (el PDF que exporta LinkedIn, tu CV o los dos): lo lee sección por sección, hace un diagnóstico, compara CV y LinkedIn para encontrar lo que está en uno y falta en el otro, te entrevista para conseguir los logros y datos que faltan, y entrega sugerencias listas para copiar y pegar (titular, Acerca de, cada experiencia, aptitudes) respetando los límites de caracteres, más un CV actualizado. Nunca inventa logros. Usala cuando digas 'mejorá mi LinkedIn', 'revisá mi perfil', 'acá está mi PDF', 'actualizá mi CV', 'revisá mi CV', 'mi perfil no atrae recruiters', 'tengo el CV pero no el LinkedIn', o cuando dejes un PDF en linkedin/ o un CV en cv/."
---

# mejorar-perfil — LinkedIn y CV listos para copiar y pegar

Toma el PDF de LinkedIn, el CV o los dos (lo que esté más completo es la base), detecta qué le falta para que un recruiter lo encuentre y lo entienda en 30 segundos, te entrevista para conseguir lo que falta, y te devuelve los textos nuevos listos para pegar.

Hablá en rioplatense, con voseo. Los textos del perfil van en el idioma que elijas (español, inglés o ambos) y con tu voz (`contexto/voz.md`).

## Antes de empezar

1. Buscá el PDF más reciente en `linkedin/` y el CV más reciente en `cv/` (que no sea uno que generó este skill; si hay varios, preguntá cuál es el vigente). Según lo que haya:

   | Hay | Cómo se trabaja |
   |---|---|
   | **Los dos** | Preguntá cuál está más completo: ese es la base. El diagnóstico suma la comparación entre los dos (paso 1) |
   | **Solo el CV** | Arrancá con el CV, sin esperar el PDF. Los textos de LinkedIn salen del CV y de `contexto/perfil.md`. Ofrecé en una línea bajar el PDF (perfil → **Más** o **Recursos** → **Guardar en PDF**) para comparar con lo que tiene publicado hoy, pero no lo exijas |
   | **Solo el PDF** | Como siempre: el PDF es la base y el CV se arma en el paso 5 |
   | **Ninguno** | Si `contexto/perfil.md` tiene la experiencia cargada, trabajá desde ahí. Si no, pedí el CV (archivo o texto pegado) o el PDF, y esperá |

   Un CV en .docx se lee con el skill de documentos si está disponible; si no, pedí que lo pegue en el chat o lo exporte a PDF.
2. Leé completos: el PDF y el CV que haya, `contexto/perfil.md`, `contexto/busqueda.md` y, si existen, `contexto/posicionamiento.md` y el último `investigacion/*-mapa-de-valor.md`.
3. Si no hay posicionamiento, avisá en una línea: el perfil queda mejor si antes se define a qué rol apuntás (`/posicionamiento`). Ofrecé hacerlo primero o seguir con lo que dice `contexto/busqueda.md`.
4. Preguntá en una ronda: idioma del perfil (español, inglés o ambos) y si también quiere el CV.

## Criterios de CV

> Adaptado de `review-resume`, de Paweł Huryn ([pm-skills](https://github.com/phuryn/pm-skills), licencia MIT).

Valen para el CV, para la sección Experiencia de LinkedIn y para el CV adaptado de cada postulación. `recruiters-sinteticos` y `nueva-postulacion` citan esta sección (`.claude/skills/mejorar-perfil/SKILL.md#criterios-de-cv`) y no la copian.

| Criterio | Qué se revisa | Cómo se arregla |
|---|---|---|
| **Viñeta con resultado** | ¿Dice qué lograste, cómo se midió y qué hiciste vos? | Logro (X) + medido por (Y) + haciendo (Z): "Bajé el ciclo de release de 3 días a 1 (X, Y) automatizando 340 casos de regresión (Z)". Solo con datos de `contexto/perfil.md`; si falta Y, va a `poner-a-prueba`. No todas las viñetas tienen que tener número: alcanza con que la mayoría de los logros lo tenga |
| **De 3 a 5 viñetas por puesto** | ¿Hay puestos con 6 o más, o con una sola? | Fusionar o recortar las que no tienen resultado; los puestos de hace más de 7 años pueden quedar en una línea |
| **Sin primera persona** | "Yo lideré", "mi equipo", "nosotros" | Arrancar con el verbo: "Lideré", "Coordiné" |
| **Resumen específico** | 2 o 3 líneas arriba: ¿dicen el rol, el dominio y un logro, o son genéricas? | Reemplazar "profesional proactivo" por lo que solo vos podés decir |
| **Orden estándar** | Contacto → resumen → experiencia (la más reciente primero) → formación → certificaciones → herramientas | Reordenar. Los sistemas de selección buscan los títulos comunes |
| **Fechas consistentes** | Mismo formato en todo el CV (mes y año), sin huecos sin explicar | Unificar; un hueco se cuenta como dice `contexto/busqueda.md` |
| **Cargos que se entienden afuera** | ¿Hay cargos internos o inventados ("Ninja", "Squad Lead Orion")? | Cargo oficial y, entre paréntesis, el equivalente estándar del mercado: "Analista Funcional (Product Owner)". **Nunca un equivalente de nivel más alto** que el cargo real |
| **Habilidades demostradas, no listadas** | ¿Las habilidades clave aparecen solo en una lista suelta? | Que cada una aparezca también dentro de una viñeta con su ejemplo |
| **Cambio de rol o poca experiencia** | Si apunta a un rol que nunca tuvo con ese nombre | Proyectos propios, cursos terminados, voluntariado y tareas del rol objetivo dentro de puestos anteriores, contados con la lente del rol nuevo y sin inflar |
| **Mail y link** | ¿El mail se ve profesional? ¿Está el link a LinkedIn? | Sugerirlo; nunca se crea una cuenta en nombre de la persona |

## Paso 1: diagnóstico

Por cada sección del perfil, una línea con qué funciona y qué no, contra lo que hace un recruiter (busca por palabras clave del rol, lee el titular y el primer párrafo, mira el último puesto). Si no hay PDF, revisá la experiencia, las habilidades y la formación sobre el CV, y el titular y el Acerca de quedan como "sin versión actual para comparar":

| Sección | Qué se revisa |
|---|---|
| **Titular** | ¿Dice el rol al que apuntás (no solo el último cargo), con 2 o 3 palabras clave y algo que te diferencie? |
| **Acerca de** | ¿Las primeras 2 líneas (lo que se ve sin "ver más") dicen qué resolvés y para quién? ¿Hay logros concretos? ¿Termina con qué buscás? |
| **Experiencia** | ¿Cada puesto tiene resultados con evidencia o solo responsabilidades? ¿El último puesto es el más trabajado? |
| **Aptitudes** | ¿Están las palabras clave de los avisos a los que apuntás? ¿Las 3 destacadas son las más relevantes? |
| **Formación y certificaciones** | ¿Están completas y actualizadas? |
| **Lo que falta** | Por ejemplo: sin foto o sin portada (lo dice el usuario, el PDF no lo muestra), sin URL personalizada, sin "Open to work" configurado para recruiters |

Si hay CV, sumá una línea por cada criterio de [Criterios de CV](#criterios-de-cv) que no cumpla, con la cita literal del CV.

**Si están los dos, compará CV y LinkedIn.** Es común que uno esté más completo que el otro. Una tabla corta con lo que difiere, con la cita de cada lado:

| Qué | En el CV | En LinkedIn | Qué se hace |
|---|---|---|---|
| Logros, puestos, proyectos o certificaciones que están en uno solo | 📌 cita | — | Llevarlo al otro (sale en las propuestas del paso 3) |
| Fechas, cargos o empresas que no coinciden | 📌 cita | 📌 cita | Preguntá cuál es la correcta; no elijas vos |
| Tecnologías o habilidades que aparecen en uno solo | 📌 cita | — | Confirmá que las usó antes de sumarlas |

Lo que se confirma se suma a `contexto/perfil.md`.

Mostralo como una lista corta, ordenada por impacto. No reescribas nada todavía.

## Paso 2: entrevista para conseguir lo que falta

El problema más común no es la redacción: son los logros sin evidencia. Corré el método de `.claude/skills/poner-a-prueba/SKILL.md#método` sobre cada puesto con logros flojos, empezando por el más reciente:

- Una ronda por puesto, con 2 o 3 preguntas concretas.
  > "En tu puesto en <empresa> dice 'automatización de pruebas'. ¿Cuántas pruebas automatizaste, qué porcentaje de la regresión cubrían, cuánto tiempo bajó el ciclo de release? Una buena respuesta: 'automaticé 340 casos, 80% de la regresión, el release pasó de 3 días a 1'."
- Si no sabe el número exacto, sirve un rango honesto o un hecho concreto ("pasamos de releases mensuales a semanales"). Nunca un número inventado.
- Lo que no se cierra va a `contexto/datos-pendientes.md`.
- Cada dato confirmado se suma a `contexto/perfil.md` en el momento.

Como mucho 4 rondas. Si quedan puestos viejos sin trabajar, decí que se pueden dejar más breves: un recruiter mira sobre todo los últimos 5 a 7 años.

## Paso 3: los textos nuevos

Escribí un archivo fechado: `linkedin/sugerencias/<AAAA-MM-DD>-perfil.md`.

Por cada sección, este formato:

````markdown
## Titular

**Antes:** <texto actual, o "sin versión actual (no hay PDF de LinkedIn)">

**Por qué cambia:** <una línea>

**Propuesta** (183 / 220 caracteres):

```
<texto listo para pegar>
```

**Alternativa:** <opcional, otra versión con otro énfasis>
````

Reglas de los textos:

- **Límites de LinkedIn:** titular 220 caracteres; Acerca de 2.600; descripción de cada experiencia 2.000. Contá los caracteres y escribilos al lado.
- **Titular:** rol objetivo + especialidad o stack + diferencial. Nada de "Buscando nuevas oportunidades" como titular entero.
- **Acerca de:** las 2 primeras líneas dicen qué resolvés y para quién. Después, 3 o 4 logros con evidencia, cómo trabajás y qué buscás. Párrafos cortos. Sin frases genéricas ("apasionado", "proactivo", "orientado a resultados").
- **Experiencia:** una línea de contexto (qué hacía la empresa o el equipo) y de 3 a 5 viñetas con la forma de [Criterios de CV](#criterios-de-cv). Las viñetas en LinkedIn se pegan con el carácter "•".
- **Acerca de y titular** pasan por `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`. El Acerca de casi siempre necesita su modo entrevista.
- **Aptitudes:** lista de hasta 15 para agregar, en orden, con las 3 a destacar primero. Solo las que la persona realmente usó.
- **Todo dato sale de `contexto/perfil.md`.** Lo que no esté confirmado no entra. Si un texto quedaría mejor con un dato que falta, marcalo con ❓ en vez de inventarlo.
- Si eligió dos idiomas, cada sección va en los dos, uno debajo del otro.

Al final del archivo: una lista de **acciones en LinkedIn que no son texto** (foto, portada, URL personalizada, Open to work solo para recruiters, pedir 2 recomendaciones a ex compañeros con un mensaje sugerido).

## Paso 4: probar antes de pegar (opcional, recomendado)

Ofrecé pasar el titular y el Acerca de por `recruiters-sinteticos` con un recruiter del rol objetivo y un escéptico. Si se hace, las correcciones se suman al mismo archivo como "Versión 2".

## Paso 5: el CV

Si lo pidió:

1. Escribí el contenido en `cv/cv-<idioma>.md` con la misma información (el CV puede ser algo más largo y detallado que LinkedIn, hasta 2 páginas), cumpliendo [Criterios de CV](#criterios-de-cv).
2. Seguí el criterio de `.claude/skills/disenador-visual/SKILL.md#método` y su apartado para ATS: una columna, títulos de sección comunes, sin tablas ni imágenes de texto.
3. Ofrecé generarlo como .docx o PDF (con los skills de documentos si están disponibles en la sesión) o como página HTML imprimible en `cv/`. Si no hay con qué, el .md queda como fuente para que lo pase a su plantilla.

## Paso 6: cierre

- Nombrá los archivos que escribiste.
- Explicá cómo aplicarlo: abrir LinkedIn, editar sección por sección, copiar del bloque de código y pegar.
- Sumá al tablero una acción "Aplicar los cambios del perfil en LinkedIn" con fecha de hoy o mañana, y una "Completar datos pendientes del perfil" si quedaron huecos.
- Recordá: cuando aplique los cambios, conviene bajar un PDF nuevo a `linkedin/` para que el sistema trabaje con la versión vigente (y, si se arrancó solo con el CV, para comparar en la próxima pasada).

## Reglas

- Nunca inventes logros, números, tecnologías, cargos ni fechas.
- Nunca subas el nivel de un cargo ("líder" donde no lo hubo, "senior" si no lo era). Si la persona lo pide, explicá el riesgo: es lo primero que se verifica en una referencia.
- Claude no edita LinkedIn ni publica nada: entrega los textos y la persona los pega.
