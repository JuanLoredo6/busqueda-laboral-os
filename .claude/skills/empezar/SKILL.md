---
name: empezar
description: "Pone en marcha el sistema de búsqueda laboral la primera vez: da la bienvenida, crea los archivos de contexto desde las plantillas, pide el PDF de LinkedIn y el CV, hace una entrevista corta para completar el perfil, qué buscás y tu voz, deja el tablero listo y explica qué sigue. Usala cuando la persona escriba /empezar, 'arranquemos', 'primera vez', 'cómo empiezo', 'configurá el sistema', o cuando contexto/perfil.md no exista todavía."
---

# empezar — la puesta en marcha

Es la primera sesión de alguien que probablemente acaba de quedarse sin trabajo. Que sea cálida, concreta y corta: en 30 o 40 minutos tiene que salir con su perfil cargado, el tablero funcionando y una idea clara de qué hacer mañana.

Hablá en rioplatense, con voseo, frases cortas. Una pregunta o una ronda por vez.

## Paso 0: ¿ya está empezado?

Si `contexto/perfil.md` ya existe y tiene contenido, no lo pises. Decí qué encontraste y preguntá si quiere completar lo que falta o arrancar de cero (en ese caso, renombrá los archivos viejos con sufijo `-anterior`).

## Paso 1: bienvenida y mapa (2 minutos)

En pocas líneas:

- Qué es esto: un sistema dentro de Claude Code para ordenar la búsqueda. Todo queda en carpetas de su computadora; nada se sube a ningún lado.
- Las carpetas principales: `contexto/` (quién sos y qué buscás), `linkedin/` y `cv/`, `postulaciones/` (una carpeta por postulación más los datos del tablero), `entrevistas/`, `investigacion/` y `tablero/`.
- Dos reglas que Claude respeta siempre: no inventa nada sobre vos, y no envía ni publica nada sin tu confirmación.

## Paso 2: crear los archivos

Copiá las plantillas sin pisar nada que ya exista:

| Plantilla | Destino |
|---|---|
| `plantillas/perfil.md` | `contexto/perfil.md` |
| `plantillas/busqueda.md` | `contexto/busqueda.md` |
| `plantillas/voz.md` | `contexto/voz.md` |
| `plantillas/decisiones.md` | `contexto/decisiones.md` |
| `plantillas/datos-pendientes.md` | `contexto/datos-pendientes.md` |
| `plantillas/postulaciones.json` | `postulaciones/postulaciones.json` |

## Paso 3: los documentos

Pedí que deje en la carpeta `linkedin/` el PDF de su perfil y, si tiene, el CV actual en `cv/`. Explicá cómo bajar el PDF:

> En LinkedIn, entrá a tu perfil → botón **Más** (o **Recursos**) → **Guardar en PDF**. Arrastrá el archivo a la carpeta `linkedin/` de este proyecto.

Si no tiene LinkedIn o no puede bajarlo, que pegue el texto del CV en el chat. Si no tiene nada, se arma desde la entrevista.

Cuando estén, leelos completos (el PDF con la herramienta de lectura, por páginas si es largo) y volcá en `contexto/perfil.md` todo lo que ya dicen: datos básicos, experiencia, formación, habilidades. **Copiá, no mejores**: mejorar es trabajo de `mejorar-perfil`. Marcá con ❓ lo que está incompleto (un puesto sin logros, fechas que no coinciden entre el CV y LinkedIn).

## Paso 4: entrevista corta

Con el método de `.claude/skills/poner-a-prueba/SKILL.md#método` (rondas numeradas con una respuesta recomendada que se acepta con "sí"), completá lo mínimo para arrancar. No más de tres rondas:

**Ronda 1, qué buscás** → `contexto/busqueda.md`:
- Rol y seniority al que apunta, industrias, modalidad y ubicación, tipo de contratación, desde cuándo puede empezar.

**Ronda 2, lo delicado** → `contexto/busqueda.md`:
- Cómo quiere contar su salida del último trabajo. Proponé una frase neutra y breve; usa la suya si la tiene. Nunca agregues detalles que no dio.
- Qué no se menciona nunca (por ejemplo, la pretensión salarial).

**Ronda 3, los logros** → `contexto/perfil.md`:
- Por cada uno de los dos trabajos más recientes: un logro con evidencia. Si responde con algo vago, una repregunta con ejemplo (como mucho dos). Si no aparece, va a `contexto/datos-pendientes.md`.

**La voz:** pedí que pegue dos o tres mensajes que haya escrito (un mail, un mensaje de LinkedIn, un post). Con eso completá `contexto/voz.md`. Si no tiene a mano, se completa más adelante.

## Paso 5: el tablero

1. Escribí su nombre en `persona` y la fecha de hoy en `actualizado` dentro de `postulaciones/postulaciones.json`.
2. Si ya tiene postulaciones en curso, cargalas ahora (una por una, con el modelo de datos de `CLAUDE.md`) con sus carpetas en `postulaciones/<empresa-rol>/`.
3. Sumá tres acciones para los próximos días:
   - "Mejorar el perfil de LinkedIn y el CV" (pedido: `/mejorar-perfil`).
   - "Definir mi posicionamiento" (pedido: `/posicionamiento`).
   - "Buscar 5 avisos que me interesen y analizarlos" (pedido: `/analizar-oferta`).
4. Comprobá que existe `tablero/datos.js` (lo genera solo un hook al editar el JSON). Si no, corré `bash tablero/sincronizar.sh`.
5. Decile que abra `tablero/tablero.html` con doble clic (o arrastrándolo al navegador) y lo deje abierto: se actualiza solo cada vez que Claude cambia algo.

## Paso 5 bis: sincronización con Gmail y Calendar (opcional)

Preguntá si usa Gmail y Google Calendar para la búsqueda. Si dice que sí, explicá en dos líneas que Claude puede revisar el correo y la agenda (solo lectura) para traer novedades al tablero: con el botón 🔄 SYNC, o sola cada 2 horas de 8 a 22. Si quiere activarla, seguí el modo **Configurar** de `.claude/skills/sincronizar-correo/SKILL.md`. Si prefiere dejarlo para después, sumá la acción "Conectar Gmail y Calendar al tablero" sin fecha, con pedido `/sincronizar-correo configurar`.

## Paso 6: cierre

En pocas líneas:

- Qué quedó cargado y qué falta (lo de `contexto/datos-pendientes.md`).
- **La rutina que recomienda el sistema:**
  - Cada día: mirar el bloque «Hoy» del tablero.
  - Cada aviso que interese: `/analizar-oferta`.
  - Cada novedad: contársela a Claude (`/actualizar`).
  - Cada viernes: `/repaso-semanal`.
- El paso siguiente concreto: `/mejorar-perfil`.
- Que para ver todos los skills puede pedir `/mapa-de-skills`.

Ejemplo de cierre, ilustrativo y con datos ficticios:

```text
Quedó cargado: tu perfil con 3 trabajos y 2 logros, qué buscás (QA senior, remoto) y tu voz.
Falta: logros de tu trabajo en Empresa B y las fechas de tu formación (están en contexto/datos-pendientes.md).

La rutina:
- Cada día, mirá «Hoy» en el tablero.
- Cada aviso que te guste: /analizar-oferta.
- Cada novedad: contámela con /actualizar.
- Cada viernes: /repaso-semanal.

Mañana: /mejorar-perfil. Para ver todo lo que podés hacer: /mapa-de-skills.
```

## Reglas

- No inventes logros, fechas ni números. Lo que no esté, se pregunta o se anota como pendiente.
- No mejores los textos en este paso: solo se cargan.
- Si la persona se angustia o cuenta algo difícil de su salida, respondé con calma y humanidad, sin dramatizar, y seguí a su ritmo. La búsqueda es un proceso largo; el sistema está para que no tenga que cargarlo todo en la cabeza.
