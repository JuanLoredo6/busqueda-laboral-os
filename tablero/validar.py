#!/usr/bin/env python3
"""Valida postulaciones/postulaciones.json contra el modelo de datos de CLAUDE.md.

Lo llama tablero/sincronizar.sh. Solo usa la biblioteca estándar.

Uso: python validar.py <ruta al JSON>

Salida:
  0  todo bien
  1  el archivo no es JSON válido (sincronizar.sh no regenera datos.js)
  2  es JSON válido pero no respeta el modelo de datos (datos.js se regenera igual)
Los problemas se escriben en stderr, uno por línea, para que Claude los corrija.
"""
import json
import re
import sys

FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FECHA_HORA = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")
COLUMNAS = {"por-enviar", "esperando", "conversacion", "cerrada"}
RESULTADOS = {"descartada", "descartada-por-mi", "retirada", "sin-respuesta",
              "oferta-aceptada", "oferta-rechazada"}
PRIORIDADES = {"alta", "media", "baja"}
FUENTES = {"gmail", "calendar"}


def main(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except json.JSONDecodeError as e:
        print(f"postulaciones.json no es JSON válido: {e.msg} (línea {e.lineno}, columna {e.colno}). "
              "tablero/datos.js NO se actualizó.", file=sys.stderr)
        return 1

    problemas = []

    def fecha(valor, donde, nula=True, hora=False):
        if valor is None and nula:
            return
        patron = FECHA_HORA if hora else FECHA
        if not isinstance(valor, str) or not patron.match(valor):
            formato = "AAAA-MM-DDTHH:MM" if hora else "AAAA-MM-DD"
            problemas.append(f"{donde}: fecha {valor!r} no tiene el formato {formato}")

    if not isinstance(datos, dict):
        print("postulaciones.json tiene que ser un objeto con postulaciones y acciones.", file=sys.stderr)
        return 2

    if datos.get("actualizado"):
        fecha(datos["actualizado"], "actualizado", hora=True)

    postulaciones = datos.get("postulaciones")
    acciones = datos.get("acciones")
    if not isinstance(postulaciones, list):
        problemas.append("falta la lista 'postulaciones'")
        postulaciones = []
    if not isinstance(acciones, list):
        problemas.append("falta la lista 'acciones'")
        acciones = []

    ids = set()
    for i, p in enumerate(postulaciones):
        if not isinstance(p, dict):
            problemas.append(f"postulaciones[{i}] no es un objeto")
            continue
        pid = p.get("id")
        donde = f"postulación {pid or i}"
        if not pid:
            problemas.append(f"postulaciones[{i}] no tiene id")
        elif pid in ids:
            problemas.append(f"{donde}: id repetido")
        ids.add(pid)
        columna = p.get("columna")
        if columna not in COLUMNAS:
            problemas.append(f"{donde}: columna {columna!r} no es una de {sorted(COLUMNAS)}")
        resultado = p.get("resultado")
        if columna == "cerrada" and resultado not in RESULTADOS:
            problemas.append(f"{donde}: está cerrada y su resultado {json.dumps(resultado)} no es uno de {sorted(RESULTADOS)}")
        if columna != "cerrada" and resultado is not None:
            problemas.append(f"{donde}: tiene resultado {resultado!r} pero no está en «cerrada»")
        encaje = p.get("encaje")
        if encaje is not None and not (isinstance(encaje, (int, float)) and 0 <= encaje <= 100):
            problemas.append(f"{donde}: encaje {encaje!r} tiene que ser null o un número de 0 a 100")
        fecha(p.get("creada"), f"{donde}, creada")
        fecha(p.get("enviada"), f"{donde}, enviada")
        fecha(p.get("ultimaNovedad"), f"{donde}, ultimaNovedad")
        for j, h in enumerate(p.get("historial") or []):
            fuente = h.get("fuente") if isinstance(h, dict) else None
            if not isinstance(h, dict) or not h.get("texto"):
                problemas.append(f"{donde}: historial[{j}] sin texto")
                continue
            fecha(h.get("fecha"), f"{donde}, historial[{j}]", nula=False)
            if fuente is not None and fuente not in FUENTES:
                problemas.append(f"{donde}: historial[{j}] con fuente {fuente!r}")

    ids_acciones = set()
    for i, a in enumerate(acciones):
        if not isinstance(a, dict):
            problemas.append(f"acciones[{i}] no es un objeto")
            continue
        aid = a.get("id")
        donde = f"acción {aid or i}"
        if not aid:
            problemas.append(f"acciones[{i}] no tiene id")
        elif aid in ids_acciones:
            problemas.append(f"{donde}: id repetido")
        ids_acciones.add(aid)
        if a.get("postulacion") is not None and a["postulacion"] not in ids:
            problemas.append(f"{donde}: apunta a la postulación {a['postulacion']!r}, que no existe")
        if a.get("prioridad") not in PRIORIDADES:
            problemas.append(f"{donde}: prioridad {a.get('prioridad')!r} no es una de {sorted(PRIORIDADES)}")
        if not isinstance(a.get("hecha"), bool):
            problemas.append(f"{donde}: 'hecha' tiene que ser true o false")
        fecha(a.get("fecha"), f"{donde}, fecha")
        fecha(a.get("hechaEl"), f"{donde}, hechaEl")
        if a.get("hecha") is True and not a.get("hechaEl"):
            problemas.append(f"{donde}: está hecha y no tiene hechaEl")

    sync = datos.get("sync")
    if isinstance(sync, dict):
        for j, r in enumerate(sync.get("porRevisar") or []):
            if isinstance(r, dict) and r.get("fuente") not in FUENTES:
                problemas.append(f"sync.porRevisar[{j}]: fuente {r.get('fuente')!r} no es gmail ni calendar")
            if isinstance(r, dict) and r.get("postulacion") is not None and r["postulacion"] not in ids:
                problemas.append(f"sync.porRevisar[{j}]: apunta a la postulación {r['postulacion']!r}, que no existe")

    if problemas:
        print("postulaciones.json no respeta el modelo de datos de CLAUDE.md:", file=sys.stderr)
        for p in problemas:
            print(f"- {p}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
