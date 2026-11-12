---
name: mapa-de-skills
description: "El índice de todos los skills de este sistema de búsqueda laboral: qué skill resuelve cada cosa, en qué orden conviene usarlos y qué no cubre ninguno. Usala para elegir el skill correcto en vez de adivinar, cuando alguien pregunte 'qué puedo hacer con esto', 'qué skills hay', 'por dónde empiezo', 'cuál uso para...', o cuando un pedido no encaja claramente en un skill."
---

# mapa-de-skills — qué skill usar para cada cosa

> Adaptado de `product-builder-resolver`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT).

Una fila por necesidad. La columna Skill dice cuál cargar; todos viven en `.claude/skills/<skill>/SKILL.md`. Hablá en rioplatense, con voseo.

## El día a día

| Necesidad | Skill |
|---|---|
| Arrancar el sistema por primera vez: entrevista inicial, perfil, qué buscás y tu voz | `empezar` |
| Mejorar LinkedIn y el CV a partir del PDF de LinkedIn, con textos listos para copiar y pegar | `mejorar-perfil` |
| Analizar un aviso: encaje con tu perfil, requisitos excluyentes, si vale la pena | `analizar-oferta` |
| Registrar una postulación nueva: carpeta, CV adaptado, respuestas y tarjeta en el tablero | `nueva-postulacion` |
| Contar una novedad ("me respondieron de X", "tengo entrevista el jueves") y actualizar el tablero | `actualizar` |
| Escribir un mensaje a un recruiter, un follow-up o un agradecimiento con tu voz | `redactar-mensaje` |
| Preparar una entrevista (RR. HH., técnica, de caso o con hiring manager) y hacer un simulacro | `preparar-entrevista` |
| Repasar la semana: qué venció, qué sigue, cómo van los números | `repaso-semanal` |

## Estrategia de la búsqueda

| Necesidad | Skill |
|---|---|
| Entender por qué la búsqueda no avanza: síntoma, causa e hipótesis | `diagnostico-busqueda` |
| Investigar dónde está la demanda para tu perfil y qué empresas apuntar | `mercado-laboral` |
| Definir a qué rol apuntás, qué resolvés, para quién y qué descartás | `posicionamiento` |
| Encontrar la mejor forma de presentarte y armar tu pitch | `propuesta-de-valor` |
| Definir qué números mirar para saber si avanzás | `metricas-busqueda` |
| Planear charlas con gente de la industria para validar una hipótesis | `plan-de-networking` |
| Sacar conclusiones del feedback real (rechazos, entrevistas, charlas) | `aprendizajes-busqueda` |

## Herramientas de criterio

| Necesidad | Skill |
|---|---|
| Poner a prueba lo que decís de vos (CV, LinkedIn, respuestas, decisiones) | `poner-a-prueba` |
| Probar una pieza contra recruiters simulados antes de mandarla | `recruiters-sinteticos` |
| Responder casos de Producto, Negocio o Liderazgo en entrevistas | `criterio-producto` |
| Responder preguntas técnicas y de diseño de sistemas en entrevistas | `criterio-tecnico` |
| Especificar y construir una pieza visual (CV, portada, presentación, portfolio) | `disenador-visual` |

## Recorridos típicos

- **Primera semana:** `empezar` → `mejorar-perfil` → `posicionamiento` → `propuesta-de-valor`.
- **Cada aviso que te interesa:** `analizar-oferta` → `nueva-postulacion` → (`recruiters-sinteticos` si es importante).
- **Cada novedad:** `actualizar` (y `redactar-mensaje` si hay que contestar).
- **Cada entrevista:** `preparar-entrevista` (que usa `criterio-producto` o `criterio-tecnico` según el rol).
- **Cada semana:** `repaso-semanal`.
- **Cuando se traba:** `diagnostico-busqueda` → `metricas-busqueda` → `mercado-laboral` o `plan-de-networking` → `aprendizajes-busqueda`.

Un pedido que ninguna fila cubre no se resuelve improvisando con uno de estos skills: se dice qué falta.
