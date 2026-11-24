# Migraciones

Cuando una versión nueva cambia algo que vive en los datos de la persona (un campo de `postulaciones.json`, una sección de una plantilla, un skill que se renombra o se saca), `git pull` no alcanza: los datos están fuera de git y no se actualizan solos. Cada uno de estos archivos dice cómo llevar los datos a esa versión. `ACTUALIZACION.md` los aplica en orden.

## Cuándo se escribe una

Todo cambio del sistema que haga alguna de estas cosas suma su `migraciones/X.Y.Z.md`, con el número de la versión que lo publica:

- cambia el formato de un archivo de datos (`postulaciones.json`, `practica.json`, los de `contexto/`);
- suma, renombra o saca una sección de una plantilla que ya se copió a `contexto/`;
- renombra o saca un skill (los pedidos de las acciones que lo nombran dejan de funcionar);
- cambia cómo se abre o se usa algo que la persona ya tiene andando (el tablero, una tarea programada).

Si la versión no toca nada de eso, no lleva migración.

## Cómo se escribe

- **Un archivo por versión**, `X.Y.Z.md`, con el título `# Migración a X.Y.Z · <título de la versión>`.
- **Qué cambió en los datos**, en dos o tres líneas.
- **Pasos numerados**, cada uno con su condición («si `postulaciones.json` no tiene `sync`…»). Se tienen que poder aplicar dos veces sin romper nada: el paso mira primero si ya está hecho.
- Cada paso dice si es **inequívoco** (se aplica solo) o si **se pregunta**. Se pregunta todo lo que borra, renombra o pisa algo de la persona (límite L9) y todo lo que depende de un dato que solo ella tiene. Nunca se completa un dato de la persona con una suposición (límite L1).
- **Qué contarle**: lo nuevo que puede usar, en una o dos líneas.
- **Comprobación**: cómo se sabe que quedó bien.
