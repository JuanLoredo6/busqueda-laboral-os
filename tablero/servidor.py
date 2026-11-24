#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
"""Servidor local del tablero: sirve tablero.html y guarda en postulaciones.json
los cambios mecánicos que la persona marca (acción hecha, tarjeta movida, nota,
acción nueva), sin pasar por Claude.

Solo usa la biblioteca estándar. Escucha solo en 127.0.0.1: nada sale de la
computadora (límite L8). Lo que necesita criterio (cerrar una postulación, cambiar
el estado o el próximo paso) no se aplica acá: queda como pedido para Claude.

Uso:
  python tablero/servidor.py              abre el tablero en el navegador
  python tablero/servidor.py --no-abrir   solo levanta el servidor
  python tablero/servidor.py --puerto 8766
  python tablero/servidor.py --raiz <carpeta del proyecto>

Sin el servidor, tablero.html sigue funcionando con doble clic como siempre.
"""
import argparse
import contextlib
import datetime
import io
import json
import os
import sys
import tempfile
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import validar  # noqa: E402

VERSION = 1
COLUMNAS_DIRECTAS = {"por-enviar": "Por enviar", "esperando": "Esperando respuesta",
                     "conversacion": "En conversación"}
MAX_CUERPO = 256 * 1024
candado = threading.Lock()


def ahora():
    return datetime.datetime.now()


def hoy():
    return ahora().strftime("%Y-%m-%d")


class Rechazo(Exception):
    """Un cambio que no se aplica acá y queda para Claude."""


def nuevo_id_accion(acciones):
    base = "a-" + ahora().strftime("%Y%m%d") + "-"
    usados = [a.get("id", "") for a in acciones if isinstance(a, dict)]
    n = 1
    for i in usados:
        if i.startswith(base) and i[len(base):].isdigit():
            n = max(n, int(i[len(base):]) + 1)
    return base + str(n)


def aplicar(datos, c):
    """Aplica un cambio del tablero. Devuelve una frase con lo que hizo o levanta Rechazo."""
    posts = {p.get("id"): p for p in datos.get("postulaciones", []) if isinstance(p, dict)}
    acciones = datos.setdefault("acciones", [])
    tipo = c.get("tipo")
    f = hoy()

    if tipo == "hecha":
        a = next((x for x in acciones if isinstance(x, dict) and x.get("id") == c.get("id")), None)
        if not a:
            raise Rechazo("la acción ya no existe en el archivo")
        if a.get("hecha"):
            return "ya estaba hecha"
        a["hecha"] = True
        a["hechaEl"] = f
        return "acción marcada como hecha"

    if tipo == "nota":
        p = posts.get(c.get("id"))
        texto = str(c.get("texto") or "").strip()
        if not p:
            raise Rechazo("la postulación ya no existe en el archivo")
        if not texto:
            raise Rechazo("la nota está vacía")
        hist = p.setdefault("historial", [])
        if any(isinstance(h, dict) and h.get("fecha") == f and h.get("texto") == texto for h in hist):
            return "la nota ya estaba"
        hist.append({"fecha": f, "texto": texto})
        p["ultimaNovedad"] = f
        return "nota sumada al historial"

    if tipo == "mover":
        p = posts.get(c.get("id"))
        destino = c.get("destino")
        if not p:
            raise Rechazo("la postulación ya no existe en el archivo")
        if destino not in COLUMNAS_DIRECTAS:
            # Cerrar necesita un resultado y suele cambiar acciones: lo decide la persona con Claude.
            raise Rechazo("cerrar una postulación necesita el resultado: pasáselo a Claude")
        if p.get("columna") == destino:
            return "ya estaba en esa columna"
        if p.get("columna") == "cerrada":
            raise Rechazo("reabrir una postulación cerrada lo resuelve Claude")
        origen = p.get("columna")
        p["columna"] = destino
        p["ultimaNovedad"] = f
        texto = "Movida a «" + COLUMNAS_DIRECTAS[destino] + "» desde el tablero."
        if origen == "por-enviar" and destino == "esperando" and not p.get("enviada"):
            p["enviada"] = f
            texto = "Enviada (movida a «Esperando respuesta» desde el tablero)."
        p.setdefault("historial", []).append({"fecha": f, "texto": texto})
        return "tarjeta movida"

    if tipo == "fecha-enviada":
        p = posts.get(c.get("id"))
        nueva = str(c.get("fechaNueva") or "")
        if not p:
            raise Rechazo("la postulación ya no existe en el archivo")
        try:
            datetime.datetime.strptime(nueva, "%Y-%m-%d")
        except ValueError:
            raise Rechazo("la fecha no es válida (formato AAAA-MM-DD)")
        if nueva > f:
            raise Rechazo("la fecha de envío no puede ser futura")
        if p.get("columna") == "por-enviar":
            raise Rechazo("la postulación todavía figura como no enviada")
        anterior = p.get("enviada")
        if anterior == nueva:
            return "ya tenía esa fecha"
        p["enviada"] = nueva
        hist = p.setdefault("historial", [])
        # Si el envío lo registró el tablero, se corrige esa misma línea en vez de sumar otra.
        auto = next((h for h in hist if isinstance(h, dict) and h.get("fecha") == anterior
                     and str(h.get("texto", "")).startswith("Enviada (movida a")), None)
        if auto:
            auto["fecha"] = nueva
        else:
            hist.append({"fecha": f, "texto": "Fecha de envío corregida desde el tablero: " + nueva +
                         (" (antes " + anterior + ")." if anterior else ".")})
        return "fecha de envío corregida"

    if tipo == "accion-nueva":
        texto = str(c.get("texto") or "").strip()
        if not texto:
            raise Rechazo("la acción no tiene texto")
        if any(isinstance(a, dict) and (a.get("texto") or "").strip().lower() == texto.lower()
               and not a.get("hecha") for a in acciones):
            return "la acción ya estaba"
        post = c.get("postulacion") or None
        if post and post not in posts:
            raise Rechazo("la postulación de la acción no existe")
        fecha = c.get("fechaAccion") or None
        if fecha and not validar.FECHA.match(str(fecha)):
            raise Rechazo("la fecha no tiene el formato AAAA-MM-DD")
        acciones.append({
            "id": nuevo_id_accion(acciones), "texto": texto, "postulacion": post, "fecha": fecha,
            "prioridad": "media", "hecha": False, "hechaEl": None, "pedido": "",
        })
        return "acción sumada"

    raise Rechazo("tipo de cambio desconocido")


def escribir_atomico(ruta, texto):
    carpeta = os.path.dirname(ruta)
    fd, tmp = tempfile.mkstemp(dir=carpeta, prefix=".tmp-", suffix=os.path.splitext(ruta)[1])
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        os.replace(tmp, ruta)
    except BaseException:
        with contextlib.suppress(OSError):
            os.remove(tmp)
        raise


def validar_texto(texto, carpeta):
    """Corre validar.py sobre el texto. Devuelve (código, mensajes)."""
    fd, tmp = tempfile.mkstemp(dir=carpeta, prefix=".val-", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(texto)
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            codigo = validar.main(tmp)
        return codigo, err.getvalue().strip()
    finally:
        with contextlib.suppress(OSError):
            os.remove(tmp)


def guardar_cambios(raiz, cambios):
    ruta_json = os.path.join(raiz, "postulaciones", "postulaciones.json")
    ruta_js = os.path.join(raiz, "tablero", "datos.js")
    if not os.path.isfile(ruta_json):
        return 409, {"error": "Todavía no existe postulaciones/postulaciones.json. Corré /empezar en Claude Code."}
    with candado:
        with open(ruta_json, encoding="utf-8") as f:
            original = f.read()
        try:
            datos = json.loads(original)
        except json.JSONDecodeError:
            return 409, {"error": "postulaciones.json está roto. Pedile a Claude que lo corrija; no toqué nada."}
        if not isinstance(datos, dict):
            return 409, {"error": "postulaciones.json no tiene el formato esperado. No toqué nada."}

        resultados = []
        for i, c in enumerate(cambios):
            if not isinstance(c, dict):
                resultados.append({"indice": i, "ok": False, "motivo": "cambio mal formado"})
                continue
            try:
                resultados.append({"indice": i, "ok": True, "detalle": aplicar(datos, c)})
            except Rechazo as e:
                resultados.append({"indice": i, "ok": False, "motivo": str(e)})

        if any(r["ok"] for r in resultados):
            datos["actualizado"] = ahora().strftime("%Y-%m-%dT%H:%M")
            texto = json.dumps(datos, ensure_ascii=False, indent=2) + "\n"
            carpeta = os.path.dirname(ruta_json)
            codigo_antes, _ = validar_texto(original, carpeta)
            codigo, mensajes = validar_texto(texto, carpeta)
            if codigo == 1 or (codigo == 2 and codigo_antes == 0):
                # El cambio rompería un archivo que estaba bien: no se escribe.
                return 422, {"error": "El cambio no respeta el modelo de datos. No toqué nada.", "detalle": mensajes}
            escribir_atomico(ruta_json, texto)
            escribir_atomico(ruta_js, "window.DATOS_TABLERO = " + texto.rstrip("\n") + ";\n")
            return 200, {"resultados": resultados, "avisos": mensajes or None}
        return 200, {"resultados": resultados}


class Manejador(SimpleHTTPRequestHandler):
    raiz = None
    puerto = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=AQUI, **kwargs)

    def log_message(self, formato, *args):  # sin ruido en la consola
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def host_valido(self):
        # Evita que otra página (DNS rebinding) le hable al servidor.
        host = (self.headers.get("Host") or "").lower()
        return host in {f"127.0.0.1:{self.puerto}", f"localhost:{self.puerto}"}

    def origen_valido(self):
        origen = self.headers.get("Origin")
        return origen in {f"http://127.0.0.1:{self.puerto}", f"http://localhost:{self.puerto}"}

    def responder(self, codigo, cuerpo):
        datos = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def do_GET(self):
        if not self.host_valido():
            self.send_error(403)
            return
        if self.path.split("?")[0] == "/api/estado":
            self.responder(200, {"servidor": True, "version": VERSION})
            return
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/tablero.html")
            self.end_headers()
            return
        nombre = self.path.split("?")[0].lstrip("/")
        if nombre == "datos.js":
            # Se lee de la raíz elegida (puede no ser la carpeta de este script).
            ruta = os.path.join(self.raiz, "tablero", "datos.js")
            if not os.path.isfile(ruta):
                self.send_error(404)
                return
            with open(ruta, "rb") as f:
                cuerpo = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/javascript; charset=utf-8")
            self.send_header("Content-Length", str(len(cuerpo)))
            self.end_headers()
            self.wfile.write(cuerpo)
            return
        if nombre not in {"tablero.html", "ejemplo.js"}:
            self.send_error(404)
            return
        super().do_GET()

    def do_POST(self):
        if not self.host_valido() or not self.origen_valido():
            self.send_error(403)
            return
        if self.path != "/api/cambios":
            self.send_error(404)
            return
        if "application/json" not in (self.headers.get("Content-Type") or ""):
            self.send_error(415)
            return
        try:
            largo = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            largo = 0
        if largo <= 0 or largo > MAX_CUERPO:
            self.send_error(413)
            return
        try:
            pedido = json.loads(self.rfile.read(largo).decode("utf-8"))
            cambios = pedido["cambios"]
            assert isinstance(cambios, list)
        except Exception:
            self.responder(400, {"error": "Pedido mal formado."})
            return
        codigo, cuerpo = guardar_cambios(self.raiz, cambios)
        self.responder(codigo, cuerpo)


def main():
    ap = argparse.ArgumentParser(description="Servidor local del tablero de búsqueda.")
    ap.add_argument("--puerto", type=int, default=8765)
    ap.add_argument("--raiz", default=os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(AQUI))
    ap.add_argument("--no-abrir", action="store_true")
    args = ap.parse_args()

    Manejador.raiz = os.path.abspath(args.raiz)
    Manejador.puerto = args.puerto
    try:
        servidor = HTTPServer(("127.0.0.1", args.puerto), Manejador)
    except OSError:
        url = f"http://127.0.0.1:{args.puerto}/tablero.html"
        print(f"El puerto {args.puerto} está ocupado. Si el tablero ya está abierto, entrá a {url}")
        if not args.no_abrir:
            webbrowser.open(url)
        return 1
    url = f"http://127.0.0.1:{args.puerto}/tablero.html"
    print(f"Tablero en {url}")
    print("Dejá esta ventana abierta mientras lo uses. Para cerrarlo: Ctrl+C.")
    if not args.no_abrir:
        webbrowser.open(url)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
