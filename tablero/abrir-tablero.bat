@echo off
rem SPDX-License-Identifier: MIT
rem Abre el tablero con el servidor local: lo que marques se guarda solo.
rem Dejá esta ventana abierta mientras uses el tablero.
cd /d "%~dp0"
where py >nul 2>nul && (py -3 servidor.py & goto fin)
python servidor.py
:fin
if errorlevel 1 pause
