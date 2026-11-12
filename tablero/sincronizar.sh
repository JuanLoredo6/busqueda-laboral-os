#!/usr/bin/env bash
# Regenera tablero/datos.js a partir de postulaciones/postulaciones.json.
# Lo corre solo un hook de Claude Code (.claude/settings.json) después de cada edición.
# También se puede correr a mano: bash tablero/sincronizar.sh
DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
JSON="$DIR/postulaciones/postulaciones.json"
JS="$DIR/tablero/datos.js"
[ -f "$JSON" ] || exit 0
if [ ! -f "$JS" ] || [ "$JSON" -nt "$JS" ]; then
  { printf 'window.DATOS_TABLERO = '; cat "$JSON"; printf ';\n'; } > "$JS"
fi
exit 0
