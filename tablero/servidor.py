#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
"""Servidor local del tablero: sirve tablero.html y guarda en postulaciones.json
los cambios mecánicos que la persona marca (acción hecha, tarjeta movida, nota,
acción nueva), sin pasar por Claude. También sirve practica.html: lee la práctica
de cada entrevista (entrevistas/<carpeta>/practica.json) y guarda las respuestas
en un archivo nuevo por práctica.

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
import re
import socket
import sys
import urllib.parse
import urllib.request
import tempfile
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

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


# ---------- práctica de entrevistas ----------
# Cada entrevista tiene entrevistas/<carpeta>/practica.json (lo escribe Claude con
# preparar-entrevista). Las respuestas de cada práctica van a un archivo nuevo,
# practica-<AAAA-MM-DD>[-n].json, que nunca se pisa (límite L9).
CARPETA = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")
SESION = re.compile(r"^practica-\d{4}-\d{2}-\d{2}(-\d+)?\.json$")
MAX_TEXTO = 20000
MAX_RESPUESTAS = 60


def carpeta_entrevista(raiz, carpeta):
    if not isinstance(carpeta, str) or not CARPETA.match(carpeta):
        return None
    return os.path.join(raiz, "entrevistas", carpeta)


def leer_practica(raiz, carpeta):
    base = carpeta_entrevista(raiz, carpeta)
    if not base:
        return 400, {"error": "Nombre de carpeta inválido."}
    ruta = os.path.join(base, "practica.json")
    if not os.path.isfile(ruta):
        return 404, {"error": "Esa entrevista no tiene práctica armada. Pedísela a Claude con /preparar-entrevista."}
    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except json.JSONDecodeError as e:
        return 409, {"error": f"practica.json está roto ({e.msg}, línea {e.lineno}). Pedile a Claude que lo corrija."}
    sesiones = sorted(n for n in os.listdir(base) if SESION.match(n))
    return 200, {"carpeta": carpeta, "practica": datos, "archivos": sesiones}


MAX_DETALLE = 200 * 1024


def leer_postulacion(raiz, carpeta):
    """Lo que el tablero retro muestra dentro de una casa: rol.md, empresa.md y los nombres de los documentos."""
    if not isinstance(carpeta, str) or not CARPETA.match(carpeta):
        return 400, {"error": "Nombre de carpeta inválido."}
    base = os.path.join(raiz, "postulaciones", carpeta)
    if not os.path.isdir(base):
        return 404, {"error": "Esa postulación todavía no tiene carpeta."}
    textos = {}
    for clave, nombre in (("rol", "rol.md"), ("empresa", "empresa.md")):
        ruta = os.path.join(base, nombre)
        if os.path.isfile(ruta):
            with open(ruta, encoding="utf-8", errors="replace") as f:
                textos[clave] = f.read(MAX_DETALLE)
    archivos = sorted(n for n in os.listdir(base) if n.lower().endswith(".md"))
    return 200, {"carpeta": carpeta, "rol": textos.get("rol"), "empresa": textos.get("empresa"), "archivos": archivos,
                 "aprendizajes": aprendizajes_de(raiz, base, empresa_de(raiz, carpeta))}


APRENDIZAJE = re.compile(r"aprend|feedback|devoluci|rechazo", re.I)


def empresa_de(raiz, carpeta):
    try:
        with open(os.path.join(raiz, "postulaciones", "postulaciones.json"), encoding="utf-8") as f:
            datos = json.load(f)
        return next((p.get("empresa") for p in datos.get("postulaciones", []) if isinstance(p, dict) and p.get("id") == carpeta), None)
    except (OSError, json.JSONDecodeError):
        return None


def aprendizajes_de(raiz, base, empresa):
    """Aprendizajes registrados de una postulación: documentos de su carpeta con ese tema y las secciones
    de los informes de aprendizajes de investigacion/ que nombran a la empresa. Se devuelven tal cual."""
    lista = []
    for n in sorted(os.listdir(base)):
        if n.lower().endswith(".md") and APRENDIZAJE.search(n):
            with open(os.path.join(base, n), encoding="utf-8", errors="replace") as f:
                lista.append({"fuente": "postulaciones/" + os.path.basename(base) + "/" + n, "texto": f.read(MAX_DETALLE)})
    inv = os.path.join(raiz, "investigacion")
    nombre = (empresa or "").split("(")[0].strip().lower()
    if nombre and os.path.isdir(inv):
        for n in sorted(os.listdir(inv)):
            if not (n.lower().endswith(".md") and "aprendizaje" in n.lower()):
                continue
            with open(os.path.join(inv, n), encoding="utf-8", errors="replace") as f:
                texto = f.read(MAX_DETALLE)
            for sec in re.split(r"\n(?=#{2,3} )", texto):
                if nombre in sec.lower():
                    lista.append({"fuente": "investigacion/" + n, "texto": sec.strip()})
    return lista


def leer_perfil(raiz):
    """Lo que muestra tu casa en el tablero retro: el perfil (para los trofeos) y el posicionamiento (el espejo)."""
    textos = {}
    for clave, nombre in (("perfil", "perfil.md"), ("posicionamiento", "posicionamiento.md")):
        ruta = os.path.join(raiz, "contexto", nombre)
        if os.path.isfile(ruta):
            with open(ruta, encoding="utf-8", errors="replace") as f:
                textos[clave] = f.read(MAX_DETALLE)
    return 200, {"perfil": textos.get("perfil"), "posicionamiento": textos.get("posicionamiento")}


def listar_practicas(raiz):
    base = os.path.join(raiz, "entrevistas")
    lista = []
    if os.path.isdir(base):
        for nombre in sorted(os.listdir(base)):
            ruta = os.path.join(base, nombre, "practica.json")
            if not CARPETA.match(nombre) or not os.path.isfile(ruta):
                continue
            try:
                with open(ruta, encoding="utf-8") as f:
                    d = json.load(f)
            except (json.JSONDecodeError, OSError):
                lista.append({"carpeta": nombre, "error": True})
                continue
            e = d.get("entrevista") or {}
            prep = d.get("preparacion") or {}
            # Acepta también el formato de las prácticas armadas como artefacto (empresa y rol arriba, «cuando» en texto).
            lista.append({"carpeta": nombre, "postulacion": e.get("postulacion"),
                          "empresa": e.get("empresa") or d.get("empresa"), "rol": e.get("rol") or d.get("rol"),
                          "tipo": e.get("tipo"), "fecha": e.get("fecha") or e.get("cuando"), "puntaje": prep.get("puntaje"),
                          "preguntas": len(d.get("preguntas") or [])})
    return 200, {"practicas": lista}


def guardar_sesion(raiz, pedido):
    carpeta = pedido.get("carpeta")
    codigo, info = leer_practica(raiz, carpeta)
    if codigo != 200:
        return codigo, info
    preguntas = {p.get("id"): p for p in (info["practica"].get("preguntas") or []) if isinstance(p, dict)}
    respuestas = pedido.get("respuestas")
    if not isinstance(respuestas, list) or not respuestas or len(respuestas) > MAX_RESPUESTAS:
        return 400, {"error": "No hay respuestas para guardar."}
    limpias = []
    for r in respuestas:
        if not isinstance(r, dict):
            continue
        texto = str(r.get("texto") or "").strip()[:MAX_TEXTO]
        pid = r.get("pregunta")
        if not texto or pid not in preguntas:
            continue
        dur = r.get("duracionSeg")
        dur = int(dur) if isinstance(dur, (int, float)) and 0 < dur < 4 * 3600 else None
        limpias.append({
            "pregunta": pid,
            "preguntaTexto": preguntas[pid].get("texto") or preguntas[pid].get("pregunta") or preguntas[pid].get("corta"),
            "texto": texto,
            "fuente": "dictado" if r.get("fuente") == "dictado" else "escrita",
            "duracionSeg": dur,
            "palabras": len(texto.split()),
        })
    if not limpias:
        return 400, {"error": "No hay respuestas para guardar."}
    base = carpeta_entrevista(raiz, carpeta)
    sesion = {"version": 1, "carpeta": carpeta, "fecha": ahora().strftime("%Y-%m-%dT%H:%M"), "respuestas": limpias}
    texto = json.dumps(sesion, ensure_ascii=False, indent=2) + "\n"
    with candado:
        for n in range(1, 100):
            nombre = f"practica-{hoy()}.json" if n == 1 else f"practica-{hoy()}-{n}.json"
            try:
                # "x": falla si el archivo existe, así nunca se pisa una práctica anterior.
                with open(os.path.join(base, nombre), "x", encoding="utf-8", newline="\n") as f:
                    f.write(texto)
                return 200, {"archivo": nombre, "respuestas": len(limpias)}
            except FileExistsError:
                continue
    return 409, {"error": "Hay demasiadas prácticas guardadas hoy."}


# ---------- transcripción local (opcional) ----------
# Si está instalado faster-whisper (MIT), la práctica transcribe la voz en esta
# computadora: el audio no sale a ningún servicio ni se guarda. El modelo se baja
# de Hugging Face la primera vez y queda en el caché local.
# Con abrir-tablero se instala solo vía uv (Python 3.13). Sin él, la página usa el
# dictado del navegador.
MAX_AUDIO = 40 * 1024 * 1024
IDIOMAS = {"es": "es", "en": "en", "pt": "pt"}


class Transcriptor:
    def __init__(self, modelo):
        self.nombre = modelo
        self.modelo = None
        self.estado = "apagada"   # apagada | sin-libreria | cargando | lista | error
        self.error = None
        self.candado = threading.Lock()
        self.carga = threading.Lock()
        if not modelo:
            return
        try:
            import faster_whisper  # noqa: F401
        except ImportError:
            self.estado = "sin-libreria"
            return
        self.estado = "cargando"
        threading.Thread(target=self.cargar, daemon=True).start()

    def cargar(self):
        with self.carga:
            if self.modelo is not None:
                return
            try:
                from faster_whisper import WhisperModel
                print(f"Transcripción: cargando el modelo «{self.nombre}» (la primera vez lo baja, puede tardar unos minutos)…")
                self.modelo = WhisperModel(self.nombre, device="cpu", compute_type="int8")
                self.estado = "lista"
                print("Transcripción: lista. El audio se transcribe en esta computadora.")
            except Exception as e:  # sin internet la primera vez, disco lleno, etc.
                self.estado = "error"
                self.error = str(e)[:300]
                print(f"Transcripción: no pude cargar el modelo ({self.error}). La práctica usa el dictado del navegador.")

    def info(self):
        return {"estado": self.estado, "modelo": self.nombre, "error": self.error}

    def transcribir(self, audio, idioma):
        if self.estado != "lista":
            return 503, {"error": "La transcripción local todavía no está lista.", **self.info()}
        lengua = IDIOMAS.get(str(idioma or "es")[:2].lower(), "es")
        inicio = datetime.datetime.now()
        try:
            with self.candado:
                segmentos, _ = self.modelo.transcribe(io.BytesIO(audio), language=lengua, beam_size=5,
                                                      vad_filter=True, condition_on_previous_text=False)
                texto = " ".join(s.text.strip() for s in segmentos).strip()
        except Exception as e:
            return 422, {"error": "No pude leer el audio: " + str(e)[:200]}
        segundos = (datetime.datetime.now() - inicio).total_seconds()
        return 200, {"texto": texto, "segundos": round(segundos, 1)}


transcriptor = Transcriptor(None)


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
        ruta, _, consulta = self.path.partition("?")
        if ruta == "/api/estado":
            # La carpeta de datos identifica a este tablero: así otro lanzador sabe si el puerto es suyo.
            self.responder(200, {"servidor": True, "version": VERSION, "raiz": os.path.normcase(self.raiz),
                                 "carpeta": os.path.basename(self.raiz.rstrip("\\/"))})
            return
        if ruta == "/api/transcripcion":
            self.responder(200, transcriptor.info())
            return
        if ruta == "/api/practicas":
            self.responder(*listar_practicas(self.raiz))
            return
        if ruta == "/api/perfil":
            self.responder(*leer_perfil(self.raiz))
            return
        if ruta == "/api/postulacion":
            carpeta = (urllib.parse.parse_qs(consulta).get("id") or [""])[0]
            self.responder(*leer_postulacion(self.raiz, carpeta))
            return
        if ruta == "/api/practica":
            carpeta = (urllib.parse.parse_qs(consulta).get("e") or [""])[0]
            self.responder(*leer_practica(self.raiz, carpeta))
            return
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/tablero.html")
            self.end_headers()
            return
        nombre = self.path.split("?")[0].lstrip("/")
        if nombre == "datos.js":
            # Se arma en el momento desde postulaciones.json de la raíz elegida: así el tablero ve los
            # cambios aunque esa carpeta no tenga el hook que regenera datos.js (por ejemplo, si los datos
            # viven fuera del repo). Si el JSON está roto, se sirve el último datos.js bueno.
            cuerpo = None
            ruta_json = os.path.join(self.raiz, "postulaciones", "postulaciones.json")
            if os.path.isfile(ruta_json):
                with open(ruta_json, encoding="utf-8") as f:
                    texto = f.read()
                try:
                    json.loads(texto)
                    cuerpo = ("window.DATOS_TABLERO = " + texto.strip() + ";\n").encode("utf-8")
                except json.JSONDecodeError:
                    cuerpo = None
            if cuerpo is None:
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
        if nombre not in {"tablero.html", "tablero-retro.html", "practica.html", "ejemplo.js"}:
            self.send_error(404)
            return
        super().do_GET()

    def do_POST(self):
        if not self.host_valido() or not self.origen_valido():
            self.send_error(403)
            return
        ruta, _, consulta = self.path.partition("?")
        if ruta == "/api/transcribir":
            self.recibir_audio(consulta)
            return
        if self.path not in ("/api/cambios", "/api/practica/respuestas"):
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
        except Exception:
            self.responder(400, {"error": "Pedido mal formado."})
            return
        if self.path == "/api/practica/respuestas":
            if not isinstance(pedido, dict):
                self.responder(400, {"error": "Pedido mal formado."})
                return
            self.responder(*guardar_sesion(self.raiz, pedido))
            return
        try:
            cambios = pedido["cambios"]
            assert isinstance(cambios, list)
        except Exception:
            self.responder(400, {"error": "Pedido mal formado."})
            return
        codigo, cuerpo = guardar_cambios(self.raiz, cambios)
        self.responder(codigo, cuerpo)

    def recibir_audio(self, consulta):
        if not (self.headers.get("Content-Type") or "").startswith("audio/"):
            self.send_error(415)
            return
        try:
            largo = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            largo = 0
        if largo <= 0 or largo > MAX_AUDIO:
            self.send_error(413)
            return
        audio = self.rfile.read(largo)  # queda en memoria: no se escribe a disco
        idioma = (urllib.parse.parse_qs(consulta).get("idioma") or ["es"])[0]
        self.responder(*transcriptor.transcribir(audio, idioma))


class Servidor(ThreadingHTTPServer):
    # HTTPServer reusa la dirección por defecto. En Windows eso deja abrir un segundo tablero en un puerto
    # que ya está en uso, y el navegador termina viendo los datos del otro. Se pide el puerto en exclusiva.
    allow_reuse_address = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def raiz_en_puerto(puerto):
    """La carpeta de datos del tablero que ya escucha en ese puerto, o None si no es un tablero."""
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{puerto}/api/estado", timeout=2) as r:
            j = json.loads(r.read().decode("utf-8"))
        return j.get("raiz") or "" if j.get("servidor") else None
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description="Servidor local del tablero de búsqueda.")
    ap.add_argument("--puerto", type=int, default=8765)
    ap.add_argument("--raiz", default=os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(AQUI))
    ap.add_argument("--no-abrir", action="store_true")
    ap.add_argument("--modelo", default=os.environ.get("TRANSCRIPCION_MODELO", "small"),
                    help="modelo de faster-whisper para la práctica (small, base, medium…)")
    ap.add_argument("--sin-transcripcion", action="store_true")
    args = ap.parse_args()

    global transcriptor
    with contextlib.suppress(Exception):  # tildes bien escritas también si la salida va a un archivo
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    Manejador.raiz = os.path.abspath(args.raiz)
    # Si el puerto lo usa otro tablero (otra carpeta de datos), no se abre ese: se busca el siguiente libre.
    # Si lo usa este mismo tablero, se abre el que ya está andando.
    servidor = None
    for puerto in range(args.puerto, args.puerto + 20):
        try:
            servidor = Servidor(("127.0.0.1", puerto), Manejador)
            break
        except OSError:
            otra = raiz_en_puerto(puerto)
            if otra is not None and otra == os.path.normcase(Manejador.raiz):
                url = f"http://127.0.0.1:{puerto}/tablero.html"
                print(f"Este tablero ya está abierto en {url}")
                if not args.no_abrir:
                    webbrowser.open(url)
                return 0
            print(f"El puerto {puerto} lo usa otro programa" + (" (otro tablero, con otra carpeta de datos)" if otra else "") + ": pruebo el siguiente.")
    if servidor is None:
        print(f"No encontré un puerto libre entre {args.puerto} y {args.puerto + 19}. Cerrá otros tableros y volvé a probar.")
        return 1
    Manejador.puerto = puerto
    args.puerto = puerto
    transcriptor =Transcriptor(None if args.sin_transcripcion else args.modelo)
    if transcriptor.estado == "sin-libreria":
        print("Transcripción local: no está instalada (se abre con abrir-tablero, que usa uv). La práctica usa el dictado del navegador.")
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
