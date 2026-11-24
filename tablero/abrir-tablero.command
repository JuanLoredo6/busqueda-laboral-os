#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Abre el tablero con el servidor local: lo que marques se guarda solo.
# En Mac se abre con doble clic. Dejá esta ventana abierta mientras uses el tablero.
cd "$(dirname "$0")" || exit 1
if command -v python3 >/dev/null 2>&1; then exec python3 servidor.py; else exec python servidor.py; fi
