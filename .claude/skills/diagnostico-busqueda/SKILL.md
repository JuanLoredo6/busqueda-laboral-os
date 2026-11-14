---
name: diagnostico-busqueda
description: "Entrevista socrática sobre tu búsqueda laboral para separar el síntoma de la causa ('no me llaman', 'me rechazan después de la técnica', 'no sé a qué apuntar'), ordenar la evidencia, exigir un número que muestre si el problema se resuelve y priorizar hasta tres hipótesis. Escribe el Diagnóstico de búsqueda en investigacion/. Su modo métricas arma ese número: un indicador principal que cambie decisiones, el árbol de palancas, un número por hipótesis con su valor de hoy sacado del tablero y las antimétricas con su umbral (postular a todo, quemarte), en el Informe de métricas. Usala cuando la búsqueda se traba, cuando no entendés por qué no avanzás, al arrancar una búsqueda o cada tres o cuatro semanas, y cuando digas 'cómo mido mi búsqueda', 'estoy avanzando?', 'qué número miro', aunque no nombres el skill."
---

# diagnostico-busqueda — el Diagnóstico de tu búsqueda

> Adaptado de `product-strategy`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Primera parada cuando la búsqueda no avanza o arranca de cero. Entrevista sin darte la razón demasiado rápido, para separar el síntoma de la causa, y cierra escribiendo el Diagnóstico: el problema, la evidencia que lo sostiene y hasta tres hipótesis priorizadas para probar.

Hablá en rioplatense, con voseo, frases cortas. Con empatía: quien lo usa probablemente se quedó sin trabajo. Ser socrático no es ser frío.

## Cuándo se usa

| Cuándo | Desde / hacia |
|---|---|
| La búsqueda arranca, o hace semanas que no avanza | Solo |
| El Diagnóstico queda escrito | Siguiente paso: `mercado-laboral` (dónde está la demanda para tu perfil) o `posicionamiento` (cómo presentarte) |
| No hay un número que diga si mejoró (falla el filtro de la métrica) | Pasá al [modo métricas](metricas.md) para armarlo antes de seguir |
| La persona pregunta cómo medir la búsqueda o qué número mirar, sin pedir un diagnóstico | Directo al modo métricas: leé y seguí `.claude/skills/diagnostico-busqueda/metricas.md` |

## Antes de empezar

Leé lo que el repo ya sabe, para no preguntarlo: `contexto/perfil.md`, `contexto/busqueda.md` y `postulaciones/postulaciones.json`. Del tablero sacá los números reales: cuántas postulaciones, cuántas respuestas, en qué columna se frenan, cuántos días llevan sin novedades. Con eso llegás a la entrevista con datos, no con impresiones.

## La entrevista

Se corre con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`: citado, nunca copiado.

### Socrática: no le da la razón a la primera

Si el planteo ya llega como solución ("tengo que hacer un curso de IA", "necesito un CV nuevo", "tengo que postularme a más"), no lo aceptes ni lo desarrolles: devolvé la repregunta que separa la solución del problema.

> Mal: "Buena idea, ¿qué curso te interesa?"
>
> Bien: "Eso es una solución. ¿Qué problema resuelve? ¿Te rechazan por falta de IA, o es algo que suponés?"

Repetí hasta que la respuesta nombre un problema concreto en una etapa concreta de la búsqueda, nunca una acción.

**Primero la mejor versión, después la pregunta.** Antes de cuestionar una explicación de la persona, decí en una línea la versión más fuerte de por qué podría ser cierta, y cuestioná esa. Cuestionar la versión débil no enseña nada. Y si una explicación ya viene con buena evidencia, decilo: un diagnóstico que fabrica dudas sirve tan poco como uno que da la razón a todo.

> Esta regla, el ejercicio de abajo y la priorización con "barato de probar" están adaptados de `strategy-red-team` y `pre-mortem`, de Paweł Huryn ([pm-skills](https://github.com/phuryn/pm-skills), licencia MIT).

### Ejercicio opcional: tres meses después

Si la persona llega con mucha angustia o con muchas explicaciones mezcladas, proponé este ejercicio antes de la primera ronda (se puede saltear): *"Imaginá que pasaron tres meses y seguís sin trabajo. ¿Qué pasó?"*. Lo que salga se ordena en tres grupos, con calma y sin dramatizar:

- **Riesgos reales:** tienen evidencia en el tablero, en un feedback o en una conducta. Pasan a la entrevista.
- **Miedos inflados:** suenan razonables pero los datos no los sostienen (por ejemplo, "me rechazan por la edad" cuando las tres respuestas que hubo fueron por inglés). Se dicen en voz alta con el dato que los desinfla, sin minimizar lo que la persona siente.
- **Lo que nadie dice:** algo que la persona sospecha y no está mirando (por ejemplo, que hace dos semanas que no habla con ninguna persona). Se anota como pregunta para la entrevista.

Ningún miedo se descarta sin un dato que lo respalde. Si no hay dato, queda como pregunta abierta.

Las etapas típicas del embudo, para ubicar el problema:

1. **Apuntar:** a qué roles y empresas te postulás.
2. **Ser visto:** que tu CV o tu perfil pase el primer filtro (ATS, recruiter).
3. **Primera charla:** que la charla con RR. HH. termine en una entrevista con el equipo.
4. **Entrevistas técnicas o de caso:** pasarlas.
5. **Oferta:** que la oferta llegue y te sirva.

### Jerarquía de evidencia

Toda la evidencia sobre el problema se ordena con la misma jerarquía de `poner-a-prueba`: `conducta > dato > afirmación > suposición`.

- "Creo que me rechazan por la edad" es una **suposición**.
- "Un recruiter me dijo que buscaban a alguien con más inglés" es una **afirmación**.
- "De 25 postulaciones tuve 2 respuestas, las dos de empresas donde tenía un referido" es un **dato**.
- "En las dos entrevistas técnicas me trabé al diseñar el sistema en voz alta" es una **conducta**.

La evidencia de menor nivel también se anota, con su nivel al lado. No se descarta: se etiqueta.

### El filtro de la métrica

**Si no hay un número, el problema no está claro.** Antes de aceptar el problema como bien planteado, preguntá: ¿qué número se movería si esto se resolviera? Por ejemplo: tasa de respuesta a postulaciones, cuántas primeras charlas pasan a entrevista técnica, entrevistas por semana. Si no hay respuesta, o la que aparece es de vanidad (postulaciones enviadas, vistas del perfil: números que no cambian ninguna decisión), el filtro no pasa. Decilo así y pasá al modo métricas (`.claude/skills/diagnostico-busqueda/metricas.md`) antes de seguir. Nada avanza como si hubiera pasado.

### Hipótesis, con formato fijo

Cada hipótesis se escribe así, sin excepción:

```
Creemos que [quién: recruiters, hiring managers, un tipo de empresa] [hace X] en [qué etapa] porque [causa]; si es cierto, vamos a ver [evidencia].
```

Ejemplo: "Creemos que los recruiters de empresas de producto descartan mi CV en el primer filtro porque mi título dice 'Analista Funcional' y buscan 'Product Owner'; si es cierto, vamos a ver que cambiar el título del CV y de LinkedIn sube la tasa de respuesta en las próximas 15 postulaciones."

Una hipótesis sin la parte "si es cierto, vamos a ver..." no es una hipótesis: es una opinión con forma de hipótesis. Se devuelve con una repregunta.

**Como mucho 3, priorizadas por riesgo × impacto × qué tan barato es probarla**, nunca por orden de aparición. Riesgo: qué poco sabés de si es cierta. Impacto: cuánto movería el número del filtro si se confirma. Barato de probar: si se puede comprobar esta semana con poco esfuerzo (cambiar el titular y mirar las próximas 10 postulaciones es barato; hacer un curso de tres meses no). Entre dos hipótesis parecidas, va primero la que se prueba más rápido. Si aparece una cuarta, anotala en `contexto/datos-pendientes.md`; no entra a la lista.

Cada hipótesis lleva además su **criterio para abandonarla**: el número o la condición a partir de la cual se deja de lado ("si después de 15 postulaciones con el título nuevo la tasa de respuesta no pasa del 5%, el problema no era el título").

## El Diagnóstico

Cierra escribiendo el entregable, fechado, en:

```
investigacion/<AAAA-MM-DD>-diagnostico-busqueda.md
```

Fechado y nunca pisado: el próximo diagnóstico es otro archivo, y la comparación entre los dos dice si avanzaste.

Lleva estas cinco secciones, en este orden y con estos títulos:

```
## Problema
## Evidencia
## Filtro de la métrica
## Hipótesis priorizadas
## Lo que sí se sostiene
```

- **Problema:** el síntoma separado de la causa, en qué etapa del embudo está y por qué ahora.
- **Evidencia:** cada dato con su nivel (`conducta`, `dato`, `afirmación` o `suposición`) al lado.
- **Filtro de la métrica:** si pasó o no. Si no pasó, el pase al modo métricas queda explícito.
- **Hipótesis priorizadas:** hasta 3, con el formato fijo, ordenadas por riesgo × impacto × barato de probar con el motivo del orden, y cada una con su criterio para abandonarla.
- **Lo que sí se sostiene:** lo que la evidencia muestra que funciona (un canal que responde, una etapa que se pasa bien, un logro que siempre genera preguntas), con su nivel de evidencia. Se escribe siempre: sostiene a la persona y evita cambiar lo que anda. Si no hay nada con evidencia, se dice.

Después, por cada hipótesis, proponé una acción concreta para probarla y, si la aceptás, sumala a las acciones del tablero (`postulaciones/postulaciones.json`, ver `CLAUDE.md`).

## Lo que este entregable no es

El Diagnóstico no reemplaza `contexto/posicionamiento.md`, que escribe `posicionamiento`. Es una foto fechada que alimenta los pasos siguientes, no la definición de quién sos profesionalmente.

El mensaje de cierre nombra solo el archivo que escribiste y las acciones que sumaste al tablero.
