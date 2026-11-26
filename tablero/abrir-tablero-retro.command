#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Abre el tablero retro: tus postulaciones como un pueblo en pixel art que se recorre con el teclado.
# Usa el mismo servidor local que abrir-tablero (lo que marques se guarda solo), en otro puerto (8766),
# así podés tener los dos tableros abiertos a la vez.
# Si está uv instalado, suma la transcripción local de voz (faster-whisper, Python 3.13).
# En Mac se abre con doble clic. Dejá esta ventana abierta mientras uses el tablero.
cd "$(dirname "$0")" || exit 1
if command -v uv >/dev/null 2>&1; then exec uv run --no-project --python 3.13 --with faster-whisper --with "av<19" servidor.py --pagina retro "$@"; fi
if command -v python3 >/dev/null 2>&1; then exec python3 servidor.py --pagina retro "$@"; else exec python servidor.py --pagina retro "$@"; fi
