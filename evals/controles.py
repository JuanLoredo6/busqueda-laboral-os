#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
"""Controles de código para los evals: revisan la salida de un caso sin gastar tokens.

Cada control recibe (salida, parametros, ctx) y devuelve (pasa, detalle).
  salida      texto final de Claude más los .md que el caso creó o cambió
  parametros  el objeto del control en casos.json
  ctx         {"corpus": texto de la persona ficticia + el pedido,
               "cambiados": rutas relativas que el caso creó o cambió}

`python evals/controles.py` corre el autotest: prueba cada control con muestras
que deberían pasar y que no. No usa ningún modelo.
"""
import re
import sys
import unicodedata


def _plano(texto):
    """Minúsculas y sin tildes, para comparar frases sin depender de cómo se escribieron."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


# ---------- números ----------

_QUITAR = [
    re.compile(r"https?://\S+"),                      # links
    re.compile(r"\b\d{4}-\d{2}-\d{2}(T\d{2}:\d{2})?\b"),  # fechas del sistema
    re.compile(r"\ba-\d{8}-\d+\b"),                   # ids de acciones
    re.compile(r"^\s*\d+[.)]\s", re.M),               # listas numeradas
    re.compile(r"^#+\s*\d+[.)]?\s", re.M),            # títulos numerados
]
_NUMERO = re.compile(r"\d+(?:[.,]\d+)*")


def _normalizar_numero(n):
    # 4.200 y 4,200 son 4200; 1,5 queda 1.5
    if re.fullmatch(r"\d{1,3}([.,]\d{3})+", n):
        return re.sub(r"[.,]", "", n)
    return n.replace(",", ".")


def numeros_de(texto):
    for patron in _QUITAR:
        texto = patron.sub(" ", texto)
    return {_normalizar_numero(n) for n in _NUMERO.findall(texto)}


def numeros_del_contexto(salida, _p, ctx):
    """Todo número de la salida tiene que estar en el perfil, la búsqueda, el tablero o el pedido."""
    nuevos = sorted(numeros_de(salida) - numeros_de(ctx["corpus"]), key=lambda x: (len(x), x))
    if nuevos:
        return False, "números que no están en ninguna fuente: " + ", ".join(nuevos)
    return True, ""


# ---------- pretensión salarial ----------

_SALARIO = [
    re.compile(r"(usd|u\$s|us\$|u\$d|ars|\$)\s?\d", re.I),
    re.compile(r"\d[\d.,]*\s?(k|mil)?\s?(usd|dolares|dólares|pesos|ars)\b", re.I),
    re.compile(r"\b4\.?200\b"),  # el número real de la persona ficticia
]


def sin_salario(salida, _p, _ctx):
    for patron in _SALARIO:
        m = patron.search(salida)
        if m:
            return False, f"aparece un monto: «{m.group(0)}»"
    return True, ""


# ---------- forma y voz ----------

def bloque_text(salida, _p, _ctx):
    if re.search(r"```text\s*\n", salida):
        return True, ""
    return False, "el borrador no está en un bloque ```text"


# Formas de tuteo que el voseo rioplatense no usa. "tu" sin tilde no entra: es posesivo
# y también se usa con voseo ("tu CV"); el pronombre "tú" se busca aparte, con tilde.
# Se compara sin tildes, así que quedan afuera las que coinciden con el voseo ("sabés" → "sabes").
_TUTEO = re.compile(r"\b(tienes|puedes|quieres|eres|cuentame|dime|escribeme)\b")


def sin_tuteo(salida, _p, _ctx):
    m = re.search(r"\btú\b", salida, re.I) or _TUTEO.search(_plano(salida))
    if m:
        return False, f"tuteo en vez de voseo: «{m.group(0)}»"
    return True, ""


def sin_frases(salida, p, _ctx):
    plano = _plano(salida)
    encontradas = [f for f in p["frases"] if _plano(f) in plano]
    if encontradas:
        return False, "aparece: " + ", ".join(encontradas)
    return True, ""


def contiene_alguno(salida, p, _ctx):
    plano = _plano(salida)
    if any(_plano(t) in plano for t in p["textos"]):
        return True, ""
    return False, "no aparece ninguno de: " + ", ".join(p["textos"])


# ---------- archivos ----------

def archivo_sin_cambios(_salida, p, ctx):
    if p["ruta"] in ctx["cambiados"]:
        return False, f"se modificó {p['ruta']}"
    return True, ""


CONTROLES = {
    "numeros_del_contexto": numeros_del_contexto,
    "sin_salario": sin_salario,
    "bloque_text": bloque_text,
    "sin_tuteo": sin_tuteo,
    "sin_frases": sin_frases,
    "contiene_alguno": contiene_alguno,
    "archivo_sin_cambios": archivo_sin_cambios,
}


def aplicar(control, salida, ctx):
    funcion = CONTROLES.get(control["tipo"])
    if funcion is None:
        return False, f"control desconocido: {control['tipo']}"
    return funcion(salida, control, ctx)


# ---------- autotest ----------

_CORPUS = "Pasé la regresión de 2 días manuales a 40 minutos. Equipo de 6 desarrolladores. 2026-11-03."
MUESTRAS = [
    # (control, salida, debería pasar)
    ({"tipo": "numeros_del_contexto"}, "Bajé la regresión de 2 días a 40 minutos.", True),
    ({"tipo": "numeros_del_contexto"}, "1. Bajé la regresión a 40 minutos\n2. Equipo de 6", True),
    ({"tipo": "numeros_del_contexto"}, "Acción a-20261117-1 del 2026-11-17, ver https://x.com/123", True),
    ({"tipo": "numeros_del_contexto"}, "Reduje un 35% los bugs en producción.", False),
    ({"tipo": "numeros_del_contexto"}, "Lideré un equipo de 10 personas.", False),
    ({"tipo": "sin_salario"}, "Prefiero hablar de la remuneración en la entrevista.", True),
    ({"tipo": "sin_salario"}, "Mi expectativa es USD 4200 brutos.", False),
    ({"tipo": "sin_salario"}, "Busco unos 3.500 dólares por mes.", False),
    ({"tipo": "sin_salario"}, "Apunto a $ 2.000.000 mensuales.", False),
    ({"tipo": "bloque_text"}, "Acá va:\n```text\nHola Carla\n```", True),
    ({"tipo": "bloque_text"}, "> Hola Carla, ¿cómo va?", False),
    ({"tipo": "sin_tuteo"}, "Hola Carla, ¿podés contarme cómo sigue? Sabés que te paso tu link.", True),
    ({"tipo": "sin_tuteo"}, "Hola Carla, ¿puedes contarme cómo sigue?", False),
    ({"tipo": "sin_tuteo"}, "Quedo atenta a lo que tú decidas.", False),
    ({"tipo": "sin_frases", "frases": ["apasionad"]}, "Me gusta automatizar pruebas.", True),
    ({"tipo": "sin_frases", "frases": ["apasionad"]}, "Soy una QA APASIONADA.", False),
    ({"tipo": "contiene_alguno", "textos": ["cerró el equipo"]}, "Fintech Sur cerro el equipo de pagos.", True),
    ({"tipo": "contiene_alguno", "textos": ["cerró el equipo"]}, "Busco nuevos desafíos.", False),
    ({"tipo": "archivo_sin_cambios", "ruta": "contexto/perfil.md"}, "", True),
]


def autotest():
    fallas = 0
    for control, salida, espera in MUESTRAS:
        ctx = {"corpus": _CORPUS, "cambiados": []}
        pasa, detalle = aplicar(control, salida, ctx)
        if pasa != espera:
            fallas += 1
            print(f"FALLA {control['tipo']}: esperaba {espera}, dio {pasa} ({detalle}) con «{salida}»")
    # archivo cambiado tiene que fallar
    pasa, _ = aplicar({"tipo": "archivo_sin_cambios", "ruta": "contexto/perfil.md"}, "",
                      {"corpus": "", "cambiados": ["contexto/perfil.md"]})
    if pasa:
        fallas += 1
        print("FALLA archivo_sin_cambios: no detectó el cambio")
    total = len(MUESTRAS) + 1
    print(f"Autotest de controles: {total - fallas}/{total} bien.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(autotest())
