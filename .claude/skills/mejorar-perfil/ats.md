# Que el CV pase los filtros ATS

Parte de `mejorar-perfil`. La cargan su paso 5, `nueva-postulacion` (CV adaptado), `disenador-visual` (cuando la pieza es un CV) y `recruiters-sinteticos` (el recruiter que filtra).

Hablá en rioplatense, con voseo (o en portugués de Brasil si es el idioma de la conversación; ver «Idioma» en `CLAUDE.md`).

## Qué se puede garantizar y qué no

Un ATS (Workday, Greenhouse, Lever, Taleo, SmartRecruiters, iCIMS y otros) hace dos cosas: **lee** el CV para cargar los campos (contacto, puestos, fechas, educación) y **ayuda a buscar**: quien selecciona filtra o busca por palabras clave, y algunos ordenan por coincidencia con el aviso.

- **Se puede garantizar** que el archivo se lea bien: que el texto salga entero y en orden, que el contacto, las secciones y las fechas se reconozcan, y que estén las palabras clave del aviso que son verdad. Eso lo comprueba el script de abajo.
- **No se puede garantizar** el resultado. Cada ATS lee distinto, cada empresa configura sus filtros (preguntas excluyentes, ubicación, años) y después decide una persona. No existe un "puntaje ATS" universal: los que muestran las páginas de CV son estimaciones propias. No lo prometas ni lo inventes.

## Formato

| Regla | Por qué |
|---|---|
| **Una columna**, de arriba abajo | Con dos columnas muchos ATS mezclan las líneas de una y otra |
| **Sin tablas, cuadros de texto, formas ni gráficos** (barras de nivel, estrellas, tortas) | Su texto se pierde o sale fuera de orden; una barra de nivel no dice nada a una máquina |
| **Contacto en el cuerpo**, no en el encabezado ni en el pie de página | Varios ATS ignoran encabezado y pie |
| **Sin íconos en lugar de palabras** (📧, ☎, el logo de LinkedIn) | El ícono no se lee: el mail o el teléfono quedan sin etiqueta. Escribí "mail", "tel." o directamente el dato |
| **Texto real, no imágenes de texto.** Ningún CV escaneado ni exportado como imagen | Si el texto no se puede seleccionar, el ATS ve una hoja en blanco |
| **Fuentes estándar** (Calibri, Arial, Helvetica, Garamond, Georgia, Times), entre 10 y 12 pt; títulos un poco más grandes | Las fuentes raras pueden extraerse con caracteres cambiados |
| **Viñetas simples** (•, -, ▪) | Símbolos decorativos pueden salir como caracteres sueltos |
| **Formato de archivo:** .docx o PDF exportado desde un procesador de texto (no "imprimir como imagen"). Si el aviso pide uno, ese | Los dos se leen bien si están bien hechos; un PDF de Canva con capas o un diseño en columnas suele fallar |
| **Nombre del archivo:** `Nombre-Apellido-CV.pdf`, o `Nombre-Apellido-CV-EN.pdf` y `Nombre-Apellido-CV-PT.pdf` para el inglés y el portugués | Quien lo descarga lo encuentra; `cv_final_v3.pdf` no ayuda |
| **Sin texto oculto** (palabras clave en blanco o en tamaño 1) | Varios ATS lo muestran en texto plano y quien lo ve descarta el CV. **Prohibido** |

## Títulos de sección

Los comunes, sin creatividad:

| Español | Inglés | Portugués |
|---|---|---|
| Resumen (o Perfil profesional) | Summary | Resumo |
| Experiencia (o Experiencia laboral) | Experience (o Work Experience) | Experiência profissional |
| Educación (o Formación) | Education | Formação acadêmica |
| Certificaciones | Certifications | Certificações |
| Habilidades (o Herramientas) | Skills | Competências (o Habilidades) |
| Idiomas | Languages | Idiomas |
| Proyectos | Projects | Projetos |

Nada de "Mi recorrido", "Lo que sé hacer" o "Where I've been".

## Cada puesto

Siempre en el mismo orden y con el mismo formato, una línea cada dato:

```
Cargo — Empresa
Ciudad, país (o Remoto) · mar. 2021 – actualidad
• viñeta
```

- **Fechas con mes y año**, el mismo formato en todo el CV (`mar. 2021` o `03/2021`, no los dos). Solo el año hace que algunos ATS calculen mal los años de experiencia.
- El cargo es texto, no una imagen ni un logo.
- Si hubo varios cargos en la misma empresa, cada uno con sus fechas.

## Palabras clave

- **Salen del aviso** (`postulaciones/<empresa-rol>/rol.md`) o, para el CV base, de los avisos típicos del rol objetivo (`contexto/posicionamiento.md`, `investigacion/*-mercado.md`).
- **Escritas como las escribe el aviso:** si dice "CI/CD", va "CI/CD" y no solo "integración continua"; si dice "Kubernetes", no alcanza con "K8s".
- **Sigla y nombre completo, una vez cada uno:** "Behavior-Driven Development (BDD)". Así se encuentra por cualquiera de las dos.
- **En dos lugares:** en `Habilidades` (lista simple, separada por comas o "·") y dentro de una viñeta que muestre dónde se usó. La lista sola no convence a la persona; la viñeta sola puede no pesar para el ATS.
- **El cargo objetivo** aparece en el resumen con el nombre del aviso ("QA Automation Engineer"), si es verdad que es ese rol.
- **Solo lo que es verdad.** Una palabra clave que la persona no usó no entra aunque el aviso la pida: va como brecha en `analizar-oferta`, no al CV.
- Sin relleno: repetir una palabra diez veces no suma y se nota.

## La comprobación con el script

Cuando haya un archivo final (.docx o .pdf), o sobre el .md antes de generarlo, corré desde la raíz del proyecto:

```bash
python .claude/skills/mejorar-perfil/revisar-ats.py cv/<archivo> --idioma es --claves "Selenium, CI/CD, Java, Scrum"
```

- `--idioma es` o `en`: qué títulos de sección espera.
- `--claves`: las palabras clave del aviso (o del rol objetivo), separadas por coma. Las elegís vos leyendo el aviso: requisitos excluyentes primero, después los deseables. También se pueden pasar en un archivo, una por línea, con `--claves-archivo`.

Qué revisa:

1. **Que el texto se extraiga.** Si sale vacío, el PDF es una imagen.
2. **Formato del .docx:** tablas, cuadros de texto, imágenes, columnas, y datos de contacto en el encabezado o el pie.
3. **PDF:** cantidad de páginas y si alguna sale sin texto. Necesita la librería `pypdf`; si no está, avisa y sugiere instalarla (`pip install pypdf`) o revisar el .docx.
4. **Contacto:** mail, teléfono y LinkedIn.
5. **Secciones:** cuáles de las esperables encontró y en qué orden aparecen.
6. **Fechas:** si hay formatos mezclados.
7. **Palabras clave:** cuáles están, cuáles faltan y el porcentaje.

El script **no reemplaza la lectura**: no ve dos columnas en un PDF ni sabe si una palabra clave es verdad. Lo que no pudo comprobar lo dice al final.

## Qué hacer con el resultado

- Cada problema de formato se corrige en el archivo y se vuelve a correr.
- Cada palabra clave que falta se clasifica antes de tocar el CV:
  - **La usó y no está escrita:** se suma a una viñeta y a Habilidades, con el dato en `contexto/perfil.md`.
  - **La usó con otro nombre:** se escribe como la dice el aviso.
  - **No la usó:** no entra. Se dice en una línea y queda como brecha.
- Mostrá el resultado en una tabla corta (qué pasó, qué falló, qué se hizo) y qué no se pudo comprobar.
