#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
"""Revisa si un CV se lee bien en un sistema de selección (ATS).

Lo usa el skill mejorar-perfil (ver ats.md). Para .docx y .md solo usa la
biblioteca estándar. Para .pdf necesita pypdf (pip install pypdf).

Uso:
  python revisar-ats.py <cv.docx|cv.pdf|cv.md> [--idioma es|en]
                        [--claves "A, B, C"] [--claves-archivo archivo.txt]

Salida:
  0  sin problemas
  1  hay problemas para corregir
  2  no se pudo leer el archivo
"""
import argparse
import re
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

SECCIONES = {
    "es": [
        ("Resumen", ["resumen", "perfil profesional", "perfil", "sobre mi", "acerca de mi"]),
        ("Experiencia", ["experiencia laboral", "experiencia profesional", "experiencia"]),
        ("Educación", ["educacion", "formacion academica", "formacion"]),
        ("Certificaciones", ["certificaciones", "certificados", "cursos"]),
        ("Habilidades", ["habilidades", "herramientas", "aptitudes", "conocimientos", "competencias"]),
        ("Idiomas", ["idiomas"]),
    ],
    "en": [
        ("Summary", ["summary", "professional summary", "profile"]),
        ("Experience", ["work experience", "professional experience", "experience", "employment history"]),
        ("Education", ["education"]),
        ("Certifications", ["certifications", "licenses & certifications", "certificates"]),
        ("Skills", ["skills", "technical skills", "core skills", "tools"]),
        ("Languages", ["languages"]),
    ],
}
OBLIGATORIAS = {"es": ["Experiencia", "Educación", "Habilidades"], "en": ["Experience", "Education", "Skills"]}

MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
TELEFONO = re.compile(r"(?:\+?\d[\d\s().-]{7,}\d)")
LINKEDIN = re.compile(r"linkedin\.com/in/[\w-]+", re.I)

MESES = (r"(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre"
         r"|january|february|march|april|june|july|august|september|october|november|december"
         r"|ene|feb|mar|abr|may|jun|jul|ago|sept|sep|set|oct|nov|dic|jan|apr|aug|dec)\.?")
FORMATOS_FECHA = {
    "mes abreviado y año (mar. 2021)": re.compile(rf"\b{MESES}\s+(?:de\s+)?\d{{4}}\b", re.I),
    "número de mes y año (03/2021)": re.compile(r"\b(?:0?[1-9]|1[0-2])[/.-](?:19|20)\d{2}\b"),
    "año y mes (2021-03)": re.compile(r"\b(?:19|20)\d{2}-(?:0[1-9]|1[0-2])\b"),
}
SOLO_ANIO = re.compile(r"(?<![\w/.-])(?:19|20)\d{2}\s*[–—-]\s*(?:(?:19|20)\d{2}|actualidad|presente|hoy|present|current)\b", re.I)
MES_ANTES = re.compile(rf"\b{MESES}\s*(?:de\s+)?$", re.I)


def hay_periodos_solo_anio(texto):
    """Un período como "2019 – 2021" sin mes delante del primer año."""
    return any(not MES_ANTES.search(texto[max(0, m.start() - 15):m.start()]) for m in SOLO_ANIO.finditer(texto))


def normalizar(texto):
    sin_tildes = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in sin_tildes if not unicodedata.combining(c)).lower()


def leer_docx(ruta, problemas, avisos):
    try:
        z = zipfile.ZipFile(ruta)
        doc = ET.fromstring(z.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as e:
        raise ValueError(f"no es un .docx válido ({e})")

    cuerpo = doc.find(f"{W}body")
    lineas = []
    for p in cuerpo.iter(f"{W}p"):
        texto = "".join(t.text or "" for t in p.iter(f"{W}t"))
        if texto.strip():
            lineas.append(texto)

    tablas = len(cuerpo.findall(f".//{W}tbl"))
    if tablas:
        problemas.append(f"Tiene {tablas} tabla(s). Muchos ATS leen las tablas fuera de orden: pasá su contenido a texto en una columna.")
    if doc.findall(f".//{W}txbxContent"):
        problemas.append("Tiene cuadros de texto. Su contenido suele perderse: pasalo al cuerpo del documento.")
    if doc.findall(f".//{W}drawing") or doc.findall(f".//{W}pict"):
        avisos.append("Tiene imágenes (foto, íconos o logos). El ATS no las lee: que ningún dato dependa de una imagen.")
    for cols in doc.iter(f"{W}cols"):
        num = cols.get(f"{W}num")
        if num and int(num) > 1:
            problemas.append(f"Está armado en {num} columnas. Pasalo a una sola columna.")
            break

    for nombre in z.namelist():
        if re.match(r"word/(header|footer)\d*\.xml$", nombre):
            parte = ET.fromstring(z.read(nombre))
            texto = " ".join(t.text or "" for t in parte.iter(f"{W}t"))
            if MAIL.search(texto) or TELEFONO.search(texto) or LINKEDIN.search(texto):
                tipo = "encabezado" if "header" in nombre else "pie de página"
                problemas.append(f"Hay datos de contacto en el {tipo}. Varios ATS lo ignoran: pasalos al cuerpo.")
    return "\n".join(lineas)


def leer_pdf(ruta, problemas, avisos):
    try:
        from pypdf import PdfReader
    except ImportError:
        raise ValueError("para leer PDF hace falta pypdf (pip install pypdf). Mientras tanto, revisá el .docx o el .md")
    lector = PdfReader(str(ruta))
    paginas = [p.extract_text() or "" for p in lector.pages]
    vacias = [i + 1 for i, t in enumerate(paginas) if len(t.strip()) < 30]
    if len(vacias) == len(paginas):
        problemas.append("No se pudo extraer texto: el PDF parece una imagen o un escaneo. Exportalo desde el procesador de texto.")
    elif vacias:
        problemas.append(f"Las páginas {vacias} salen sin texto: pueden ser imágenes.")
    if len(paginas) > 2:
        avisos.append(f"Tiene {len(paginas)} páginas. Lo esperable es 1 o 2.")
    avisos.append("En PDF no se puede detectar si hay dos columnas: mirá que el texto de arriba salga en orden.")
    return "\n".join(paginas)


def leer(ruta, problemas, avisos):
    ext = ruta.suffix.lower()
    if ext == ".docx":
        return leer_docx(ruta, problemas, avisos)
    if ext == ".pdf":
        return leer_pdf(ruta, problemas, avisos)
    if ext in (".md", ".txt"):
        avisos.append("Es el texto fuente: se revisa el contenido, no el formato del archivo final. Corré el script de nuevo sobre el .docx o el PDF.")
        texto = ruta.read_text(encoding="utf-8")
        return re.sub(r"^#+\s*", "", texto, flags=re.M)
    raise ValueError(f"formato {ext or 'sin extensión'} no soportado (usá .docx, .pdf o .md)")


def revisar_contacto(texto, problemas, avisos):
    primeras = "\n".join(texto.splitlines()[:15])
    if not MAIL.search(texto):
        problemas.append("No se encontró un mail.")
    elif not MAIL.search(primeras):
        avisos.append("El mail no está al principio del CV.")
    if not TELEFONO.search(texto):
        avisos.append("No se encontró un teléfono.")
    if not LINKEDIN.search(texto):
        avisos.append("No se encontró el link a LinkedIn (linkedin.com/in/...).")


def revisar_secciones(texto, idioma, problemas, avisos):
    lineas = [normalizar(l).strip(" :•-*#\t") for l in texto.splitlines()]
    encontradas = []
    for nombre, variantes in SECCIONES[idioma]:
        for i, linea in enumerate(lineas):
            if len(linea) <= 40 and any(linea == v or linea.startswith(v + " ") for v in variantes):
                encontradas.append((i, nombre))
                break
    nombres = [n for _, n in encontradas]
    for obligatoria in OBLIGATORIAS[idioma]:
        if obligatoria not in nombres:
            problemas.append(f"No se encontró la sección «{obligatoria}» con un título estándar (ver ats.md).")
    orden = [n for _, n in sorted(encontradas)]
    return orden


def revisar_fechas(texto, problemas, avisos):
    usados = {nombre: len(rx.findall(texto)) for nombre, rx in FORMATOS_FECHA.items()}
    usados = {k: v for k, v in usados.items() if v}
    if len(usados) > 1:
        detalle = ", ".join(f"{k}: {v}" for k, v in usados.items())
        problemas.append(f"Hay formatos de fecha mezclados ({detalle}). Usá uno solo en todo el CV.")
    solo_anio = hay_periodos_solo_anio(texto)
    if solo_anio:
        avisos.append("Hay períodos solo con el año (2019 – 2021). Con mes y año los ATS calculan mejor los años de experiencia.")
    if not usados and not solo_anio:
        avisos.append("No se encontraron fechas reconocibles en los puestos.")


def revisar_claves(texto, claves):
    base = normalizar(texto)
    estan, faltan = [], []
    for clave in claves:
        patron = r"(?<![\w])" + re.escape(normalizar(clave)) + r"(?![\w])"
        (estan if re.search(patron, base) else faltan).append(clave)
    return estan, faltan


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(description="Revisa si un CV se lee bien en un ATS.")
    parser.add_argument("archivo")
    parser.add_argument("--idioma", choices=["es", "en"], default="es")
    parser.add_argument("--claves", default="", help="palabras clave separadas por coma")
    parser.add_argument("--claves-archivo", help="archivo con una palabra clave por línea")
    args = parser.parse_args()

    ruta = Path(args.archivo)
    if not ruta.exists():
        print(f"No existe el archivo: {ruta}")
        return 2

    claves = [c.strip() for c in args.claves.split(",") if c.strip()]
    if args.claves_archivo:
        claves += [l.strip() for l in Path(args.claves_archivo).read_text(encoding="utf-8").splitlines() if l.strip()]

    problemas, avisos = [], []
    try:
        texto = leer(ruta, problemas, avisos)
    except ValueError as e:
        print(f"No se pudo leer {ruta.name}: {e}")
        return 2

    print(f"Revisión ATS de {ruta.name} (idioma: {args.idioma})")
    print(f"Texto extraído: {len(texto)} caracteres, {len(texto.split())} palabras")

    if texto.strip():
        revisar_contacto(texto, problemas, avisos)
        orden = revisar_secciones(texto, args.idioma, problemas, avisos)
        print("Secciones encontradas, en orden: " + (" → ".join(orden) if orden else "ninguna"))
        revisar_fechas(texto, problemas, avisos)

        if claves:
            estan, faltan = revisar_claves(texto, claves)
            pct = round(100 * len(estan) / len(claves))
            print(f"\nPalabras clave: {len(estan)} de {len(claves)} ({pct}%)")
            if estan:
                print("  Están: " + ", ".join(estan))
            if faltan:
                print("  Faltan: " + ", ".join(faltan))
                avisos.append("Antes de sumar una palabra clave que falta, confirmá que la persona la usó (ver ats.md).")

    print("\nProblemas para corregir:" if problemas else "\nSin problemas de lectura.")
    for p in problemas:
        print(f"  ✗ {p}")
    if avisos:
        print("\nPara revisar:")
        for a in avisos:
            print(f"  · {a}")
    print("\nNo se comprueba: si hay dos columnas en un PDF, si las palabras clave son verdad, "
          "ni cómo lo configura cada empresa en su ATS.")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
