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
| Arrancar el sistema por primera vez: traer el CV, LinkedIn o el contexto que armaste con otra IA, entrevista inicial, perfil, qué buscás y tu voz | `empezar` |
| Mejorar LinkedIn y el CV a partir del PDF de LinkedIn, del CV o de los dos, con textos listos para copiar y pegar | `mejorar-perfil` |
| Analizar un aviso: encaje con tu perfil, requisitos excluyentes, si vale la pena | `analizar-oferta` |
| Registrar una postulación nueva: carpeta, CV adaptado, respuestas y tarjeta en el tablero | `nueva-postulacion` |
| Contar una novedad ("me respondieron de X", "tengo entrevista el jueves") y actualizar el tablero | `actualizar` |
| Traer al tablero las novedades que llegaron por Gmail o Google Calendar (botón 🔄 SYNC, o sola cada 2 horas) | `sincronizar-correo` |
| Escribir un mensaje a un recruiter, un follow-up o un agradecimiento con tu voz | `redactar-mensaje` |
| Preparar una entrevista (RR. HH., técnica, de caso o con hiring manager) y hacer un simulacro | `preparar-entrevista` |
| Practicar o responder casos de Producto, Negocio o Liderazgo, o preguntas técnicas y de diseño de sistemas | `preparar-entrevista` (sus criterios de producto y técnico) |
| Repasar la semana: qué venció, qué sigue, cómo van los números | `repaso-semanal` |

## Estrategia de la búsqueda

| Necesidad | Skill |
|---|---|
| Entender por qué la búsqueda no avanza: síntoma, causa e hipótesis | `diagnostico-busqueda` |
| Definir qué números mirar para saber si avanzás | `diagnostico-busqueda` (su modo métricas) |
| Investigar dónde está la demanda para tu perfil y qué empresas apuntar | `mercado-laboral` |
| Definir a qué rol apuntás, qué resolvés, para quién y qué descartás | `posicionamiento` |
| Encontrar la mejor forma de presentarte y armar tu pitch y tu titular | `posicionamiento` (su fase de propuesta de valor) |
| Planear charlas con gente de la industria para validar una hipótesis | `plan-de-networking` |
| Sacar conclusiones del feedback real (rechazos, entrevistas, charlas) | `aprendizajes-busqueda` |

## Herramientas de criterio

| Necesidad | Skill |
|---|---|
| Poner a prueba lo que decís de vos (CV, LinkedIn, respuestas, decisiones) | `poner-a-prueba` |
| Probar una pieza contra recruiters simulados antes de mandarla | `recruiters-sinteticos` |
| Especificar y construir una pieza visual (CV, portada, presentación, portfolio) | `disenador-visual` |

## Recorridos típicos

- **Primera semana:** `empezar` → `mejorar-perfil` → `posicionamiento` (y después su fase de propuesta de valor, para el pitch).
- **Cada aviso que te interesa:** `analizar-oferta` → `nueva-postulacion` → (`recruiters-sinteticos` si es importante).
- **Cada novedad:** `actualizar` (y `redactar-mensaje` si hay que contestar). Las que llegan por mail o calendario las trae `sincronizar-correo`.
- **Cada entrevista:** `preparar-entrevista` (con su criterio de producto o técnico según el tipo de entrevista).
- **Cada semana:** `repaso-semanal`.
- **Cuando se traba:** `diagnostico-busqueda` (con su modo métricas si falta un número) → `mercado-laboral` o `plan-de-networking` → `aprendizajes-busqueda`.

Un pedido que ninguna fila cubre no se resuelve improvisando con uno de estos skills: se dice qué falta.

## Ejemplo

```text
Pedido: "Me rechazaron tres veces después de la entrevista técnica, ¿qué hago?"

Respuesta: Eso es "cuando se traba". Arrancaría con diagnostico-busqueda para separar el síntoma de la causa.
Si ya tenés notas de esas entrevistas, aprendizajes-busqueda saca los patrones. Para practicar la próxima,
preparar-entrevista con su criterio técnico. ¿Empezamos por el diagnóstico?
```
