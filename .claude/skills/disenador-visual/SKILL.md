---
name: disenador-visual
description: "Especifica una pieza visual de tu búsqueda antes de hacerla (CV, portada o foto de LinkedIn, portfolio, presentación para un caso de entrevista, una página personal), pantalla por pantalla o diapositiva por diapositiva: propósito, estructura, jerarquía, contenido real de cada bloque y criterios visuales. Después revisa si la sesión tiene con qué construirla y recién ahí lo ofrece. Usala cuando digas 'quiero que mi CV se vea mejor', 'armame una portada', 'tengo que presentar un caso', 'necesito un portfolio', o cuando otro skill necesite criterio visual."
---

# disenador-visual — la especificación visual y su construcción

> Adaptado de `visual-designer`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Escribe qué tiene que decir una pieza visual y cómo se organiza, antes de abrir cualquier herramienta. La pieza puede ser:

- **Un documento:** el CV, una carta.
- **Una imagen:** la portada de LinkedIn.
- **Una presentación:** las diapositivas de un caso que te pidieron para la entrevista.
- **Una página:** un portfolio o una página personal.

**La especificación es el entregable. Construirla es una rama que solo se abre si hay con qué**: ver «Construir» al final.

Hablá en rioplatense, con voseo.

## Cuándo se usa

| Cuándo | Desde / hacia |
|---|---|
| Ya hay un brief del pitch (`investigacion/*-mapa-de-valor.md`, de la fase de propuesta de valor de `posicionamiento`) | Viene de ahí: el titular y los tres logros son el contenido principal |
| Te pidieron una presentación para una entrevista | Solo, con `postulaciones/<empresa-rol>/` como fuente |
| Cualquier pieza con un lector y un propósito | Solo |

## Regla número uno

**Nunca inventa contenido que la pieza no tiene.** Un CV con un logro que nadie midió, una diapositiva con un número inventado o un portfolio con proyectos que no existen parecen terminados y no lo están. Lo que falta se pregunta; lo que sigue faltando se escribe como hueco en la especificación, nunca se rellena con algo creíble. El contenido sale de `contexto/perfil.md`.

## La entrevista

Antes de escribir cualquier estructura, se aprietan el propósito, el lector y la condición de éxito con el método de `.claude/skills/poner-a-prueba/SKILL.md#método` (citado, nunca copiado). Tres preguntas cargan el peso, y ninguna se responde con "que quede lindo":

- **¿Quién lo lee y en qué situación?** Un recruiter que mira 80 CV en una tarde no lee como un hiring manager que se prepara para tu entrevista.
- **¿Qué tiene que pasar después de leerlo?** Una acción, una decisión, una cosa entendida. Una pieza con tres propósitos no tiene ninguno.
- **¿Qué es lo único que, si no se entiende, hace fracasar la pieza?** Alrededor de eso se arma la jerarquía.

## Método

El criterio visual compartido. Cualquier skill del repo que necesite razonar sobre una pieza visual cita esta sección (`.claude/skills/disenador-visual/SKILL.md#método`) y no la copia.

### 1. Una jerarquía por superficie

Cada página, pantalla o diapositiva tiene **un** elemento principal, y la especificación lo nombra. Lo principal se lee primero, es lo más grande o lo más contrastado, y está solo en esa condición. Dos principales son cero: el ojo elige, y no elige el que querías.

> En un CV, lo principal de la primera página es casi siempre el titular más el logro más fuerte, no tu nombre en letra gigante.

### 2. El aire es contenido

El espacio vacío no es lugar desperdiciado: es lo que hace legible la jerarquía. Si un bloque no entra sin sacar aire, no entra. Se decide qué se corta; no se aprieta.

### 3. El contraste lleva significado, nunca decoración sola

Las diferencias de tamaño, peso o color se usan para decir algo (esto va primero, esto es secundario) y cada una lleva en la especificación lo que significa. **Nunca solo con color:** también con tamaño, peso o posición, para que sobreviva a quien no distingue los colores y a un CV impreso en blanco y negro.

### 4. Un bloque, un mensaje

Cada bloque (una sección del CV, una diapositiva, un área de la portada) dice una cosa y se resume en una línea. Esa línea va en la especificación antes que el contenido: lo que no se puede resumir no está pensado.

### 5. El estado incómodo

Cada pieza declara su situación incómoda y qué dice cuando pasa: el hueco de fechas en el CV, la objeción que te van a hacer en la presentación del caso, el portfolio que se abre desde un celular.

### Para CV: la lectura de los sistemas de selección (ATS)

Un CV se lee dos veces: primero una máquina y después una persona. Para la máquina: una columna, texto seleccionable (no imágenes de texto), títulos de sección comunes ("Experiencia", "Educación"), fechas en un formato consistente y las palabras clave del aviso donde sean verdad. Para la persona: lo de arriba.

## La especificación

Cierra escribiendo, fechado:

```
investigacion/<AAAA-MM-DD>-spec-<pieza>.md
```

(Si la pieza es para una postulación, en `postulaciones/<empresa-rol>/`.)

Fechado y nunca pisado. Con estas cinco secciones, en este orden y con estos títulos:

```
## La pieza y su propósito
## Estructura y jerarquía
## Contenido, bloque por bloque
## Criterios visuales aplicados
## Huecos y lo que no cubre
```

- **La pieza y su propósito:** qué tipo de pieza es, quién la lee y en qué situación, qué tiene que pasar después y lo único que no puede fallar.
- **Estructura y jerarquía:** las superficies en orden y el elemento principal de cada una.
- **Contenido, bloque por bloque:** cada bloque con su mensaje en una línea y después su contenido real: texto literal, qué dato va, qué imagen y qué muestra. Texto real, nunca relleno.
- **Criterios visuales aplicados:** qué ingrediente del método gobernó cada decisión, y dónde se fue en contra de uno y por qué.
- **Huecos y lo que no cubre:** qué dato o texto falta, quién lo da, y lo que quedó afuera a propósito.

## Construir

**Después de escribir el documento, y solo entonces**, revisá si la sesión tiene con qué construir ese tipo de pieza:

- Un CV o una carta: Claude puede generar un .docx o un PDF (con los skills de documentos si están disponibles) o una página HTML imprimible.
- Una presentación: un deck de Claude o un .pptx.
- Una portada de LinkedIn o una página: HTML que se exporta a imagen, o una integración de diseño conectada (por ejemplo, Figma).

**Si hay con qué:** decilo y ofrecé construirla nombrando la herramienta. Construir es un paso aparte que pedís vos; el documento ya queda escrito igual. Lo construido sigue la especificación y no agrega contenido: lo que falte vuelve como hueco.

**Si no hay con qué:** cerrá con el documento. No instales nada, no pidas credenciales y no rebajes la especificación por falta de herramienta.

## Lo que este entregable no es

No valida que la pieza funcione: eso solo lo dice su lector real (y `recruiters-sinteticos` ayuda a encontrar defectos antes). Tampoco decide qué contás de vos: eso sale de `posicionamiento` y su propuesta de valor.
