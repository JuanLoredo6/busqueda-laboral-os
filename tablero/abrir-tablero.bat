@echo off
rem SPDX-License-Identifier: MIT
rem Abre el tablero con el servidor local: lo que marques se guarda solo.
rem Si esta uv instalado, suma la transcripcion local de voz (faster-whisper, Python 3.13).
rem Deja esta ventana abierta mientras uses el tablero.
cd /d "%~dp0"
where uv >nul 2>nul && (uv run --no-project --python 3.13 --with faster-whisper --with "av<19" servidor.py %* & goto fin)
where py >nul 2>nul && (py -3 servidor.py %* & goto fin)
python servidor.py %*
:fin
if errorlevel 1 pause
