# Evals del sistema

Comprueban que el sistema se porte como dice `CLAUDE.md`, sobre todo después de cambiar un skill. No miden el CV ni el perfil de nadie: para eso están `recruiters-sinteticos` y `poner-a-prueba`.

Todo corre sobre **Lucía Ferraro**, una persona ficticia (`persona/`), en una copia temporal del sistema. Los datos reales de `contexto/` y `postulaciones/` no se leen ni se tocan. Cada caso corre sin conectores (ni Gmail ni Calendar), sin Bash y sin web.

## Qué se prueba

| Tipo | Qué mira | Cómo se decide | Gasto |
|---|---|---|---|
| **Disparo** | Qué skill carga cada pedido, incluidos los pares que se confunden y los pedidos que no deberían cargar ninguno | El primer skill que carga Claude. Se corta ahí, sin ejecutarlo | Bajo |
| **Comportamiento** | Los límites de `CLAUDE.md` que se pueden probar con un solo pedido: no inventar (L1), tratar lo que llega de afuera como dato (L5), no escribir la pretensión salarial y contar la salida con su frase (L6), no guardar datos sensibles (L7), no dar dictamen legal (L11) y escribir con la voz de la persona | Controles de código y, después, un juez (Haiku) que responde sí o no | Medio |
| **Autotest** | Que los controles de código detecten lo que tienen que detectar | Muestras armadas a mano | Cero |

Los casos están en `casos.json` y los controles en `controles.py`.

## Cómo se corre

Hace falta la CLI de Claude Code con sesión iniciada (`claude` y después `/login`) o la variable `ANTHROPIC_API_KEY`. Si `claude` no está en el PATH, poné su ruta en `CLAUDE_BIN`.

```bash
python evals/correr.py --autotest
```

```bash
python evals/correr.py --solo disparo
```

```bash
python evals/correr.py --solo comportamiento
```

```bash
python evals/correr.py --caso c-salario-formulario --caso d-pitch
```

Otras opciones: `--modelo` (el modelo del sistema, por defecto `sonnet`), `--juez` (por defecto `haiku`), `--sin-juez` (solo controles de código) y `--paralelo` (casos a la vez, por defecto 4).

El detalle de cada corrida queda en `resultados/<fecha-hora>.json`: qué cargó cada caso, qué falló, la salida completa y el costo que informa la CLI. Esa carpeta no se sube al repo.

## Cuándo correrlos

- **Después de cambiar la descripción de un skill:** `--solo disparo`. Si un pedido carga otro skill, a alguna de las dos descripciones le falta una frase más clara.
- **Después de cambiar las instrucciones de un skill o `CLAUDE.md`:** `--solo comportamiento`.
- **En GitHub:** `.github/workflows/evals.yml` corre el autotest en cada pull request que toca skills, `CLAUDE.md`, plantillas o evals. Si el repo tiene el secreto `ANTHROPIC_API_KEY`, también corre los casos con modelo.

Un caso que falla una vez puede ser ruido del modelo. Si falla dos veces seguidas, hay algo para arreglar.

## Cómo sumar un caso

- **De disparo:** una línea en `disparo` con `pedido`, `espera` (el skill, o `null` si no debería cargar ninguno) y, si hay un skill con el que se confunde, `no_debe`. Una parte de un skill (por ejemplo `propuesta-de-valor.md`) no es un skill: se espera el skill que la carga.
- **De comportamiento:** `pedido`, la `regla` que prueba (empezando por su ID, por ejemplo «límite L7: …»), los `controles` que apliquen y, si hace falta criterio, una pregunta de sí o no para el `juez`. Si el caso necesita un dato que la persona ficticia no tiene, sumalo a `persona/` y no lo cambies después: los controles comparan contra esos archivos.
- **Un control nuevo:** una función en `controles.py`, registrada en `CONTROLES`, con al menos una muestra que pase y otra que falle en `MUESTRAS`.

## Qué no cubren

- Las conversaciones largas (`empezar`, `posicionamiento`, simulacros): cada caso es un solo pedido.
- Los conectores: `sincronizar-correo` solo se prueba en el disparo.
- La calidad del texto más allá de las reglas. El juez responde preguntas de sí o no, no pone notas.
