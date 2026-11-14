---
name: posicionamiento
description: "Te entrevista y escribe tu capa estratégica profesional en contexto/posicionamiento.md: a qué rol apuntás y por qué, qué problema le resolvés a una empresa, para qué tipo de empresas y equipos, qué descartás, contra quién competís y cómo te diferenciás, y qué queda abierto. Es la base de la que salen el CV, LinkedIn, los mensajes y el pitch. Usala cuando digas 'no sé cómo venderme', 'a qué apunto', 'quiero cambiar de rol', 'no sé qué rol buscar', o antes de rehacer el CV o el perfil."
---

# posicionamiento — tu capa estratégica profesional

> Adaptado de `prd`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Te entrevista y escribe la definición estratégica de tu perfil: hacia dónde vas, qué problema resolvés, para quién, qué no hacés, contra quién competís y qué queda abierto. Es la puerta de entrada del sistema: de acá salen el CV (`mejorar-perfil`), el pitch (`propuesta-de-valor`) y cada postulación.

La entrevista aprieta con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`: citado, nunca copiado.

Hablá en rioplatense, con voseo, frases cortas. Con empatía: quedarse sin trabajo pega, y la entrevista no es un examen.

## El archivo que produce

Un solo archivo, `contexto/posicionamiento.md`, con estas secciones:

| Sección | Qué responde |
|---|---|
| `## Rol objetivo` | Qué rol buscás ahora y dónde querés estar en 3 años |
| `## Problema que resolvés` | Qué problema le resolvés a una empresa, por qué ahora y cómo se nota que lo resolviste |
| `## Para quién` | Qué tipo de empresas y equipos te necesitan, y con qué resuelven hoy lo que harías vos |
| `## Alcance` | Qué roles, industrias y modalidades NO, tus restricciones duras (ubicación, idioma, horario) y qué es negociable |
| `## Competencia y diferencial` | Contra qué perfiles competís y en qué te diferenciás, con evidencia |
| `## Oportunidades` | Caminos que podrían valer la pena y todavía no decidiste |
| `## Preguntas abiertas` | Lo que falta decidir. Se vacía a medida que se cierra |

Al principio del archivo, una línea de estado: fecha y veredicto (ver al final).

No toca `contexto/perfil.md` salvo para sumar un dato que confirmaste. Si completar una sección obligara a tocar otro archivo, decilo y frená.

## Fase 1: leer lo que ya está antes de preguntar

Antes de la primera pregunta:

1. Leé completos `contexto/perfil.md`, `contexto/busqueda.md`, el PDF de LinkedIn en `linkedin/` si está, y `contexto/posicionamiento.md` si ya existe. Es incremental: una sección completa nunca se pisa sin avisar.
2. Leé lo que haya en `investigacion/` (diagnóstico, mercado, aprendizajes).
3. Decí qué leíste y **qué secciones ya podés completar solo** con eso. Recién ahí empieza la entrevista, y solo sobre lo que falta.

## Fase 2: la entrevista

Las preguntas van en rondas, como define el método de `poner-a-prueba`, cada una con una línea de por qué esa sección cambia una decisión. Sin esa línea, la pregunta suena a trámite.

Ejemplo de una pregunta dentro de una ronda, ilustrativo y con datos ficticios (la respuesta recomendada sale siempre de lo que ya leíste):

```text
2. ¿Qué descartás? Por qué importa: define a qué avisos no les dedicás tiempo y qué no va en tu CV.
   Recomendada: no a roles de soporte ni a consultoras de staff augmentation; sí a producto propio (sale de busqueda.md).
   ¿Va así? Respondé "sí" o corregilo.
```

### Las seis preguntas que fuerzan la verdad

1. ¿Cuál es la evidencia más fuerte de que una empresa te necesita? No interés: conducta. Una oferta, un ascenso, alguien que te llamó para un proyecto, un problema que te trajeron a vos.
2. ¿Cómo resuelven hoy las empresas lo que harías vos? Si la respuesta es "no lo resuelven", ¿por qué viven bien sin eso?
3. Nombrame a una persona concreta que te contrataría: su puesto, y qué le pasa si no cubre el rol.
4. ¿Qué es lo más chico que podrías ofrecer esta semana? (Un proyecto freelance, una consultoría, un rol part time.)
5. ¿Qué te sorprendió de las últimas entrevistas o charlas que tuviste?
6. En tres años, ¿lo que hacés va a ser más necesario o menos? ¿Qué cambia con la IA?

### Investigación

No se inventan conclusiones. Si no hay investigación del mercado, se dice y se ofrece `mercado-laboral`. Se pregunta por el tipo de empresa objetivo, el que explícitamente no y las alternativas que hoy tienen esas empresas (otros perfiles, agencias, IA).

### Competencia y diferencial: la curva de valor

> Adaptado de `value-curve`, de Paweł Huryn ([product-engineering](https://github.com/phuryn/product-engineering), licencia MIT), que a su vez sale de *La estrategia del océano azul* (Kim y Mauborgne).

Para escribir `## Competencia y diferencial` con evidencia y no con adjetivos, armá una tabla corta:

1. **Factores:** de 5 a 7 cosas que valora el tipo de empresa al que apuntás, escritas como lo que la empresa necesita y no como tus habilidades ("que alguien ordene la regresión sin frenar los releases", no "Selenium"). Salen de los requisitos que se repiten en los `postulaciones/*/rol.md`, del informe de `mercado-laboral` y de lo que dijeron en entrevistas. Incluí los imprescindibles aunque todos los cumplan: sin ellos no te llaman.
2. **Con quién te comparan:** vos, 2 o 3 perfiles con los que competís de verdad (por ejemplo, "QA semi senior con 3 años en una sola empresa", "desarrollador que también hace pruebas") y al menos una alternativa a contratar: promover a alguien de adentro, un freelancer, una consultora, una herramienta de IA, no cubrir el puesto.
3. **Puntaje de 0 a 10 en cada factor**, con su fuente al lado: 📌 evidencia del perfil o de un aviso, o 🔍 suposición. Sin investigación todavía, todo es 🔍 y lo primero que sale de la tabla es qué averiguar (con `plan-de-networking`).
4. **La lectura, en pocas líneas:**
   - Dónde tenés que estar claramente arriba: si en los factores que más pesan tu puntaje se parece al de los demás, no hay motivo para elegirte a vos.
   - Dónde alcanza con estar a la par: los imprescindibles.
   - En qué **no** competís a propósito, y por qué a ese tipo de empresa no le importa. Decirlo es parte del posicionamiento y alimenta `## Alcance`.
   - Las cuatro acciones: qué **sacás** de tu CV y tu pitch, qué **bajás**, qué **subís** y qué **creás** (algo que hoy no mostrás y deberías: un proyecto público, un caso escrito).

Ningún puntaje sale de la nada: un factor donde tu número no tiene evidencia queda como 🔍 y va a `## Preguntas abiertas`.

### Antes de fijar el rol

Antes de hablar de qué rol, se cuestiona la premisa: ¿es el rol correcto o es el que hiciste siempre? ¿Qué pasa si no cambiás nada? ¿Hay algo que ya tenés armado y alcanzaría? Recién después: rol objetivo, qué no hacés y con qué condición lo reconsiderarías, restricciones duras y supuestos con lo que los invalidaría.

## Fase de alternativas, obligatoria

Antes de fijar el posicionamiento, presentá 2 o 3 caminos, cada uno con su esfuerzo, su riesgo y qué aprovecha de lo que ya tenés:

- **El más directo:** el mismo rol en la misma industria, el que se puede salir a buscar esta semana.
- **El que mejor envejece:** el que menos te obliga a reacomodarte si el mercado cambia en dos años.
- **Uno lateral que reencuadra:** un rol adyacente que usa tu experiencia de otra forma (por ejemplo, de QA a Producto, de backend a Solutions Engineer, de líder técnico a consultor).

Elegís vos. Sin esta fase el documento registra la primera idea, no la mejor.

## La regla del hueco explícito

Un hueco se escribe **solo cuando decidís explícitamente no responder**, y siempre con quién lo cierra. Un archivo lleno de huecos no es un entregable: es un fracaso disfrazado de completo. Si un hueco aparece porque nunca se preguntó, no es un hueco: es trabajo sin hacer, y la entrevista sigue.

## Mostrar antes de escribir

Antes de tocar el archivo, mostrá exactamente lo que se va a escribir (el contenido, no un resumen) y esperá tu visto bueno. Solo se escriben las secciones que tocó la entrevista.

## El veredicto de cierre

Al final, uno de tres, siempre explícito:

- **Completo:** alcanza para rehacer el CV, el perfil y el pitch.
- **Completo con reservas:** se puede avanzar, y estas son las preguntas abiertas que quedan.
- **Falta contexto:** qué sección quedó sin cerrar y qué hace falta para cerrarla.

**Mínimo indispensable:** si `Rol objetivo`, `Alcance` o `Competencia y diferencial` quedan vacías, todavía no conviene reescribir el CV ni LinkedIn. Decilo de frente, no dejes que se descubra después.

El mensaje de cierre nombra el archivo y el veredicto, y sugiere el paso siguiente: `propuesta-de-valor` para el pitch o `mejorar-perfil` para CV y LinkedIn.
