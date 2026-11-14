---
name: recruiters-sinteticos
description: "Prueba tu CV, tu perfil de LinkedIn, tu pitch, un mensaje a un recruiter o tus respuestas de entrevista contra recruiters y hiring managers simulados, antes de usarlos de verdad. Cada rasgo del personaje marcado como evidencia, dato público o suposición, cada reacción con el rasgo en que se apoya, y siempre un escéptico. Encuentra defectos y escribe la versión 2 de la pieza. No valida nada. Usala cuando digas 'cómo lo leería un recruiter', 'probá mi CV', 'esto convence?', 'simulá un hiring manager', o antes de mandar una postulación importante."
---

# recruiters-sinteticos — diagnóstico y versión 2 de tu pieza

> Adaptado de `synthetic-users`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Prueba una pieza de tu búsqueda (CV, perfil de LinkedIn, pitch, mensaje, carta, respuestas de entrevista) contra personajes simulados con rasgos explícitos: un recruiter que filtra, un hiring manager, alguien escéptico. Sirve para encontrar defectos antes de gastar una postulación real.

Hablá en rioplatense, con voseo.

## Cuándo se usa

| Cuándo | Desde / hacia |
|---|---|
| Tenés una pieza lista para mandar | Solo, o desde `posicionamiento` (el pitch de su propuesta de valor), `mejorar-perfil` o `redactar-mensaje` |
| La versión 2 queda escrita | Usala de verdad. Lo que pase con recruiters reales lo procesa `aprendizajes-busqueda` |

## Regla número uno

**Esto NO valida NADA.** Abrí la sesión con esa frase y repetila al cerrar. Ninguna reacción de un personaje simulado prueba que la pieza funciona con personas reales. Sirve para una sola cosa: encontrar defectos antes de usarla. Un diagnóstico que se lee como si hubiera validado la pieza está mal escrito.

## Antes de armar los personajes

Preguntá en una línea, si no está claro: ¿qué pieza y para qué postulación? Si hay una postulación, leé `postulaciones/<empresa-rol>/rol.md`: el aviso es la mejor fuente de rasgos con evidencia.

## Los personajes

Se arman con el método de `.claude/skills/poner-a-prueba/SKILL.md#método` (citado, nunca copiado): cada rasgo propuesto se aprieta por su origen antes de entrar.

Cada rasgo lleva su origen marcado, uno por uno:

| Marca | Origen |
|---|---|
| **(evidencia)** | Algo real: lo que dice el aviso, lo que te dijo un recruiter de esa empresa, feedback de una entrevista anterior, el perfil público de quien te va a entrevistar |
| **(dato público: <fuente>)** | Un estudio o encuesta pública sobre cómo contratan (por ejemplo, encuestas de recruiters, informes de mercado laboral, la encuesta de Stack Overflow), con nombre y link |
| **(suposición)** | Una construcción sin evidencia ni dato público detrás |

Un rasgo sin marca no entra.

**Antes de marcar un rasgo como suposición, buscalo en fuentes públicas.** Si una fuente lo cubre, se marca `(dato público: <fuente>)`; si no, queda `(suposición)`.

**Un dato público nunca se marca como evidencia.** Describe a recruiters en general, no a quien va a leer tu CV.

**Siempre al menos un escéptico**, con su motivo: alguien que ya vio cien CV iguales esta semana, alguien con una objeción concreta (sobrecalificado, poca experiencia en el stack, saltos de trabajo cortos, un hueco en las fechas, el inglés), o alguien que busca un perfil distinto al tuyo. Personajes que solo confirman no encuentran defectos.

Elenco típico, ajustado a la pieza:

- **Recruiter que filtra:** 30 segundos por CV, busca palabras clave del aviso.
- **Hiring manager:** quiere saber si resolviste problemas como los suyos.
- **El escéptico.**
- Para puestos técnicos, opcional: **alguien del equipo** que te entrevistaría.

**Cada reacción nombra el rasgo en que se apoya**, con su marca: "Lo descarto, el aviso pide Kubernetes y no aparece en ningún lado (se apoya en: requisito excluyente del aviso, evidencia)". La reacción siempre es inventada, sea cual sea la marca del rasgo. Nombrar el rasgo muestra qué reacciones se apoyan en algo y cuáles son pura construcción.

**Ningún "me encanta" sin su costo al lado.** Toda reacción entusiasta va con su duda o su fricción: qué le preocupa, qué tendría que creer para llamarte. Una reacción que es solo entusiasmo es señal de que la pieza se está probando para confirmar, no para aprender.

## Defectos a buscar

Revisá la pieza contra esta lista. Cada defecto encontrado se anota con su reescritura al lado, no solo se señala:

| Defecto | Ejemplo | Reescritura |
|---|---|---|
| Responsabilidad en vez de resultado | "Responsable del mantenimiento de la API" | "Mantuve la API de pagos con 99,9% de disponibilidad durante 2 años" (con el dato real de `contexto/perfil.md`) |
| Logro sin evidencia | "Mejoré mucho los tiempos de entrega" | El número real, o el hecho concreto; si no existe, pasarlo a `poner-a-prueba` |
| Faltan palabras clave del aviso | El aviso pide "CI/CD" y el CV dice "automatización de despliegues" | Usar el término del aviso donde sea verdad |
| Jerga interna de tu empresa anterior | "Lideré el proyecto Fénix del squad Orion" | Decir qué era: "la migración del sistema de facturación" |
| Genérico, podría ser de cualquiera | "Profesional proactivo, orientado a resultados" | Una frase que solo puedas decir vos |
| Mensaje sin pedido o sin contexto | "Hola, me interesa trabajar en tu empresa" | Qué viste, por qué vos, qué pedís concretamente |
| Demasiado largo para el canal | CV de 4 páginas, mensaje de LinkedIn de 6 párrafos | Ajustar al canal (CV: 1-2 páginas; mensaje: hasta 5 líneas) |

Si la pieza es un CV o la sección Experiencia de LinkedIn, revisala también contra `.claude/skills/mejorar-perfil/SKILL.md#criterios-de-cv`. Si es un texto en nombre de la persona (mensaje, pitch, Acerca de), contra las muletillas de `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`: un recruiter que ve diez mensajes iguales por día las reconoce.

**Nunca se inventa un logro para arreglar un defecto.** Si la reescritura necesita un dato que no está en `contexto/perfil.md`, se marca ❓ y se te pregunta.

## El entregable

Cierra escribiendo, fechado:

```
investigacion/<AAAA-MM-DD>-prueba-<pieza>.md
```

(Si la pieza es de una postulación, va en `postulaciones/<empresa-rol>/<AAAA-MM-DD>-prueba-<pieza>.md`.)

Con estas cuatro secciones, en este orden y con estos títulos:

```
## Personajes
## Simulación
## Defectos y reescrituras
## Versión 2
```

- **Personajes:** cada uno con sus rasgos marcados y el escéptico identificado.
- **Simulación:** las reacciones a la pieza, cada una con el rasgo en que se apoya, y todo entusiasmo con su costo.
- **Defectos y reescrituras:** cada defecto de la lista que apareció, con su reescritura.
- **Versión 2:** la pieza corregida, lista para usar.

La sección **Versión 2** abre y cierra con la regla número uno escrita: "esto NO valida NADA".

## Lo que este entregable no es

No reemplaza la reacción de recruiters reales: reduce cuánto defecto llega a la primera postulación. Juntar el feedback real y sacar conclusiones es trabajo de `aprendizajes-busqueda`.
