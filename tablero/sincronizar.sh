#!/usr/bin/env bash
# Valida postulaciones/postulaciones.json y regenera tablero/datos.js.
# Lo corre solo un hook de Claude Code (.claude/settings.json) después de cada edición.
# También se puede correr a mano: bash tablero/sincronizar.sh
#
# Si el JSON está roto, no pisa datos.js (el tablero sigue mostrando lo último bueno)
# y sale con código 2: Claude Code le muestra el error a Claude para que lo corrija.
# Si es JSON válido pero no respeta el modelo de datos, regenera datos.js y también avisa.
DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
JSON="$DIR/postulaciones/postulaciones.json"
JS="$DIR/tablero/datos.js"
[ -f "$JSON" ] || exit 0

# Busca un Python que funcione de verdad (en Windows, "python3" puede ser un acceso a la tienda).
PY=""
for c in python3 python py; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c "import json" >/dev/null 2>&1; then PY="$c"; break; fi
done

estado=0
if [ -n "$PY" ]; then
  "$PY" "$DIR/tablero/validar.py" "$JSON"
  estado=$?
elif command -v node >/dev/null 2>&1; then
  # Sin Python, al menos se comprueba que sea JSON válido.
  node -e 'try{JSON.parse(require("fs").readFileSync(process.argv[1],"utf8"))}catch(e){console.error("postulaciones.json no es JSON válido: "+e.message+". tablero/datos.js NO se actualizó.");process.exit(1)}' "$JSON"
  estado=$?
else
  echo "Aviso: no encontré Python ni Node para validar postulaciones.json. Comprobá a mano que sea JSON válido." >&2
fi

if [ "$estado" -eq 1 ]; then
  exit 2
fi

if [ ! -f "$JS" ] || [ "$JSON" -nt "$JS" ]; then
  { printf 'window.DATOS_TABLERO = '; cat "$JSON"; printf ';\n'; } > "$JS"
fi

[ "$estado" -eq 2 ] && exit 2
exit 0
