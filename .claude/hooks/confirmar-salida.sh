#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
# Límites L3, L4 y L10 de CLAUDE.md: nada sale en nombre de la persona y Gmail y Calendar son de solo lectura.
#
# Lo corre un hook PreToolUse de Claude Code (.claude/settings.json) antes de cualquier herramienta
# que envía o modifica mails, etiquetas o eventos. El filtro por nombre de herramienta está en
# settings.json y no depende del ID del conector, así que funciona en cualquier instalación.
#
# No bloquea: le pide a la persona que confirme esa llamada, aunque la sesión esté en modo automático.
# En una corrida sin nadie que confirme (por ejemplo, una tarea programada), la llamada no se hace.

entrada="$(cat)"
herramienta="$(printf '%s' "$entrada" | sed -n 's/.*"tool_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)"
herramienta="${herramienta##*__}"
[ -n "$herramienta" ] || herramienta="una herramienta que envía o modifica"

printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Límites L3 y L4 (CLAUDE.md): %s envía o modifica algo en tu nombre. Confirmá solo si lo pediste vos para este caso."}}\n' "$herramienta"
exit 0
