@echo off
rem SPDX-License-Identifier: MIT
rem Abre el tablero retro: tus postulaciones como un pueblo en pixel art que se recorre con el teclado.
rem Usa el mismo servidor local que abrir-tablero (lo que marques se guarda solo), en otro puerto (8766),
rem asi podes tener los dos tableros abiertos a la vez.
rem Si esta uv instalado, suma la transcripcion local de voz (faster-whisper, Python 3.13).
rem Deja esta ventana abierta mientras uses el tablero.
cd /d "%~dp0"
where uv >nul 2>nul && (uv run --no-project --python 3.13 --with faster-whisper --with "av<19" servidor.py --pagina retro %* & goto fin)
where py >nul 2>nul && (py -3 servidor.py --pagina retro %* & goto fin)
python servidor.py --pagina retro %*
:fin
if errorlevel 1 pause
