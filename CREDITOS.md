# Créditos

## Skills adaptados del pack de Pedro Romero Luna

Trece skills de `.claude/skills/` son **adaptaciones** de los skills de **Pedro Romero Luna** publicados en
[pedroromeroluna/ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills)
con licencia MIT. Los originales son herramientas de discovery de producto. Acá se tradujeron al
español rioplatense y se reescribieron para una búsqueda laboral: el objeto pasa de ser un producto
a ser tu perfil y tu búsqueda. El método de fondo es suyo: la jerarquía de evidencia, el tope de
repreguntas, las rondas con respuesta recomendada, los huecos que se anotan y nunca se rellenan, y
los entregables fechados.

El texto de la licencia original está en
[`.claude/skills/LICENSE-ai-first-product-skills.txt`](.claude/skills/LICENSE-ai-first-product-skills.txt).
Cada skill adaptado lo dice en su primera línea.

| Original de Pedro | Adaptado | Qué hace en la búsqueda |
|---|---|---|
| `grill` | `poner-a-prueba` | Repregunta cada logro y cada decisión hasta que haya evidencia |
| `product-strategy` | `diagnostico-busqueda` | Separa síntoma de causa y prioriza hipótesis sobre tu búsqueda |
| `market-research` | `mercado-laboral` | Investiga la demanda para tu perfil con fuentes citadas |
| `prd` | `posicionamiento` | Escribe tu capa estratégica: rol objetivo, para quién, qué no |
| `ideation-engine` | `propuesta-de-valor` | Explora ángulos para presentarte y arma tu pitch |
| `synthetic-users` | `recruiters-sinteticos` | Prueba CV, pitch y mensajes contra recruiters simulados |
| `ux-research` | `plan-de-networking` | Diseña una ronda de charlas con gente de la industria |
| `insight-engine` | `aprendizajes-busqueda` | Convierte el feedback real en aprendizajes con evidencia |
| `product-metrics` | `metricas-busqueda` | Indicador principal, palancas y antimétricas de tu búsqueda |
| `cpo` | `criterio-producto` | Responder casos de Producto, Negocio y Liderazgo |
| `cto` | `criterio-tecnico` | Responder preguntas técnicas y de diseño de sistemas |
| `visual-designer` | `disenador-visual` | Especificar y construir CV, portada, presentación o portfolio |
| `product-builder-resolver` | `mapa-de-skills` | Índice de todos los skills del sistema |

Si te interesa el discovery de producto, instalá los originales desde su fuente (requiere Node.js):

```bash
npx skills add pedroromeroluna/ai-first-product-skills
```

## Métodos tomados de los repositorios de Paweł Huryn

Algunas secciones de los skills existentes adaptan métodos de **Paweł Huryn** ([The Product Compass](https://www.productcompass.pm)),
publicados con licencia MIT en [phuryn/pm-skills](https://github.com/phuryn/pm-skills),
[phuryn/product-engineering](https://github.com/phuryn/product-engineering) y
[phuryn/pm-brain](https://github.com/phuryn/pm-brain). No se sumó ningún skill: se tradujeron al español
rioplatense y se adaptaron a una búsqueda laboral dentro de los skills que ya había. Cada sección adaptada lo dice en su encabezado.

El texto de la licencia está en [`.claude/skills/LICENSE-phuryn.txt`](.claude/skills/LICENSE-phuryn.txt).

| Original | Dónde quedó | Qué aporta |
|---|---|---|
| `work-humanizer` (product-engineering) | `redactar-mensaje`, sección «Revisión de voz» | Modo entrevista, control de certeza de cada dato, muletillas de IA a sacar, opción más corta |
| `review-resume` (pm-skills) | `mejorar-perfil`, sección «Criterios de CV» | Viñeta logro + medida + acción, largo por puesto, cargos estándar, cambio de rol |
| `strategy-red-team` y `pre-mortem` (pm-skills) | `diagnostico-busqueda` | Mejor versión antes de cuestionar, "barato de probar", criterio para abandonar, ejercicio de los tres meses |
| `summarize-interview` (pm-skills) y `/ingest` (pm-brain) | `preparar-entrevista`, «Plantilla de notas» | Notas con citas literales separadas de la interpretación |
| `value-curve` (product-engineering) | `posicionamiento`, «Competencia y diferencial» | Curva de valor contra perfiles que compiten y alternativas a contratar |
| `/review` (pm-brain) | `repaso-semanal` | Contexto viejo, hipótesis estancadas, decisiones a revisar, citar cada señal |
| Esquema de decisiones (pm-brain) | `poner-a-prueba`, «Qué la haría cambiar» | Cada decisión clave con lo que descarta y una condición observable para revisarla |
| Hook de validación (pm-brain) | `tablero/validar.py` | El JSON del tablero se valida con código después de cada edición |

Para que dos skills no compartan las mismas frases en su descripción, se usó la idea de probar cada skill con pedidos que sí y que no
deberían activarlo, de [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) (licencia Apache 2.0). No se copió código ni texto.
