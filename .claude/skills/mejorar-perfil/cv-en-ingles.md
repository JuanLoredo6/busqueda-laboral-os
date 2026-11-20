# El CV en el otro idioma

Parte de `mejorar-perfil`. La cargan su paso 5 y `nueva-postulacion` cuando hace falta el CV (o los textos de LinkedIn) en el idioma que no es el de por defecto. Casi siempre es pasar del español al inglés; las reglas de [Del inglés al español](#del-inglés-al-español) cubren el caso contrario. Para el portugués de Brasil está `cv-en-portugues.md`, con el mismo método.

Hablá en rioplatense, con voseo (o en portugués de Brasil si es el idioma de la conversación; ver «Idioma» en `CLAUDE.md`), para explicar. El CV va en el idioma de destino.

## El rol

Trabajás como una recruiter bilingüe que filtró CV de Argentina y de Latinoamérica para empresas de Estados Unidos y Europa. Sabés cómo suena un CV escrito por alguien nativo y cómo suena uno traducido. El objetivo no es traducir: es que quien lo lea en inglés no note que hubo un original en español, sin cambiar un solo dato.

## La fuente

- La versión en inglés sale **del CV base ya confirmado** (`cv/cv-es.md`) y de `contexto/perfil.md`. Si el CV base tiene huecos o datos sin confirmar, se cierran primero ahí.
- **No agrega nada:** ni logros, ni números, ni tecnologías, ni alcance. Si en inglés una viñeta "pide" un dato que no está, se marca con ❓, igual que en español.
- **No sube el tono:** "colaboré" no pasa a "led", "participé" no pasa a "drove", "ayudé a bajar" no pasa a "reduced". El verbo en inglés dice lo mismo que el verbo en español.
- La variante sale de `contexto/busqueda.md` (`Variante del inglés`). Por defecto, Estados Unidos: *optimize*, *program*, *center*, fechas *Mar 2024*. Si es Reino Unido o Europa: *optimise*, *programme*, *centre*. Una sola variante en todo el documento.

## Convenciones del CV en inglés

| Qué | Cómo va | Por qué |
|---|---|---|
| **Datos personales** | Nombre, ciudad y país, mail, teléfono con código de país (+54 9 11…), LinkedIn. Sin foto, edad, fecha de nacimiento, estado civil, nacionalidad ni documento | En Estados Unidos y gran parte de Europa esos datos se evitan (discriminación) y un CV que los trae se nota traducido |
| **Ubicación y modalidad** | "Buenos Aires, Argentina · Open to remote (UTC-3)" si `busqueda.md` dice remoto | El huso horario es lo primero que se preguntan para un remoto desde afuera |
| **Resumen** | *Summary*, 2 o 3 líneas, sin pronombres: "QA Automation Engineer with 6 years…", nunca "I am a…" | Convención del CV en inglés |
| **Tiempos verbales** | Pasado simple para puestos anteriores; presente para el actual (*Lead*, *Maintain*), o pasado si son logros ya cerrados del puesto actual. Consistente dentro de cada puesto | Mezclar tiempos es la marca más común de traducción |
| **Sin artículos de más** | "Automated 340 regression tests", no "Automated the 340 regression tests of the team" | El CV en inglés es telegráfico |
| **Fechas** | `Mar 2023 – Present` (mes abreviado en inglés, guion largo, *Present* con mayúscula). Igual en todo el CV | Lo leen bien los ATS y las personas |
| **Números** | Coma de miles y punto decimal: `1,200`, `3.5`, `30%`. Moneda con código: `USD 40K`, `ARS` solo si importa | `1.200` en inglés se lee "uno coma dos" |
| **Títulos de sección** | `Summary`, `Experience`, `Education`, `Certifications`, `Skills`, `Languages` | Son los que buscan los ATS (ver `ats.md`) |
| **Idiomas** | `Spanish — Native` · `English — Professional working proficiency (C1)`. El nivel es el de `perfil.md`, con el MCER si lo tiene | Ver [El nivel de inglés](#el-nivel-de-inglés) |
| **Largo** | Hasta 2 páginas; para menos de 5 años de experiencia, 1 | En inglés se espera más corto que en Argentina |

## Cargos, títulos y empresas

**Cargos:** el cargo oficial se traduce a su equivalente estándar del mercado, sin subir el nivel. Si el equivalente no es obvio, el original va entre paréntesis la primera vez. Referencias frecuentes (confirmar siempre contra lo que hacía la persona, no contra el nombre):

| En español | En inglés | Cuidado con |
|---|---|---|
| Analista Funcional | Business Analyst (o Functional Analyst si el rol era técnico-funcional) | No es *Product Manager* |
| Analista Programador | Software Developer | |
| Desarrollador Semi Senior | Software Engineer (Mid-level) | "Semi Senior" no existe en inglés |
| Líder Técnico | Tech Lead | |
| Líder de Proyecto | Project Lead / Project Manager | *Manager* solo si gestionaba personas o presupuesto |
| Jefe de… | Team Lead / Manager, según a cuántas personas tenía a cargo | **Nunca *Head of*** salvo que fuera la persona a cargo del área entera |
| Gerente | Manager | No es *Director* |
| Responsable de… | …Lead, o el cargo de lo que hacía | No es *Head of* |
| Referente técnico | Subject Matter Expert / Technical Point of Contact | |
| Pasante | Intern | |
| Tester / Analista QA | QA Analyst / QA Engineer | *Engineer* si automatizaba |
| Soporte | IT Support Specialist / Help Desk | |

**Títulos académicos:** nombre original + equivalente, para que no se pierda ni se infle.

| En español | En inglés |
|---|---|
| Licenciatura en Sistemas (5 años) | Bachelor's Degree in Information Systems (5-year program) — *Licenciatura en Sistemas* |
| Ingeniería en Sistemas de Información | Bachelor of Engineering in Information Systems (*Ingeniero en Sistemas*), 5-year program |
| Tecnicatura | Associate Degree / Technical Degree (2–3 years) |
| Analista de Sistemas (título terciario) | Systems Analyst Degree (3-year tertiary program) |
| Posgrado / Especialización | Postgraduate Specialization |
| Maestría | Master's Degree |
| Carrera incompleta | "Coursework toward Bachelor's in …, 2015–2018". **Nunca** como título terminado |

La universidad va con su nombre oficial en español (Universidad de Buenos Aires) y, si ayuda, la sigla.

**Empresas:** el nombre tal cual. Si no es conocida afuera, una línea de contexto debajo: "Argentine fintech, 300 employees, payments for SMBs". Solo con datos de `perfil.md`.

## Verbos que dicen lo mismo

El verbo en inglés tiene que ser el más preciso, no el más impactante. Equivalencias con el mismo peso:

| En español | En inglés |
|---|---|
| Lideré (había personas a cargo) | Led, Managed |
| Coordiné (sin personas a cargo) | Coordinated, Organized |
| Desarrollé, construí | Built, Developed |
| Diseñé | Designed |
| Implementé | Implemented, Rolled out |
| Automaticé | Automated |
| Bajé, reduje | Reduced, Cut |
| Aumenté, mejoré | Increased, Improved |
| Migré | Migrated |
| Participé en | Contributed to (y decir qué hizo la persona) |
| Fui responsable de | Owned (si era de verdad suyo) o el verbo de lo que hacía. **Nunca "Responsible for"**: suena a lista de tareas |
| Colaboré con | Partnered with, Worked with |
| Capacité | Trained |
| Relevé requerimientos | Gathered requirements |

## Falsos amigos y calcos

Los errores que delatan una traducción, sobre todo desde el rioplatense:

| Escrito así | Quiso decir | Va |
|---|---|---|
| *Actually* | Actualmente | Currently |
| *Realized* (un proyecto) | Realicé | Carried out, Delivered, Completed |
| *Capacitation* | Capacitación | Training |
| *Assisted to* a meeting | Asistí | Attended |
| *Career* (de grado) | Carrera universitaria | Degree, Program |
| *Formation* | Formación | Education, Training |
| *Relevant* (por importante) | Relevante en el sentido de "grande" | Significant, Key |
| *Eventually* | Eventualmente | If needed, Occasionally |
| *Support* como verbo de todo | Dar soporte | Provided support for / Supported (solo para soporte real) |
| *Experience in* + gerundio | Experiencia en hacer | Experience + gerundio (*experience building*) |
| *Development of* + todo | Desarrollo de | Un verbo: *Built*, *Developed* |
| *Personal* (por equipo) | Personal a cargo | Team, Staff, Direct reports |
| *Commercial area* | Área comercial | Sales |
| *Systems area* | Área de sistemas | IT department, Engineering |
| *Senior* como adjetivo de personas sueltas | "Un senior" | A senior engineer |
| *Licensed* | Licenciado | Bachelor's degree (*licensed* es matrícula profesional) |
| *Profile* en el resumen ("Profile oriented to…") | Perfil orientado a | Ir directo al rol: "QA Engineer focused on…" |

## Lo que suena a IA en inglés

Se evita aunque el original en español lo tuviera: *spearheaded*, *leveraged*, *synergy*, *results-driven*, *passionate*, *dynamic*, *detail-oriented*, *proven track record*, *seasoned*, *go-getter*, *cutting-edge*, *robust*, *seamless*, *empower*, *in today's fast-paced environment*, *Furthermore*, *Additionally* como inicio de viñeta. Tampoco tres adjetivos en fila ni todas las viñetas con la misma estructura y el mismo largo.

El registro es el de `contexto/voz.md` llevado al inglés: si la persona escribe corto y directo, el CV en inglés también.

## El nivel de inglés

- El nivel se toma de `contexto/perfil.md` tal cual. No se sube.
- Un CV en inglés le dice al recruiter "podés entrevistarme en inglés". Si `perfil.md` dice básico o intermedio, avisalo en una línea antes de escribir: conviene tenerlo igual, pero prepará la entrevista en inglés (`preparar-entrevista`), y en el CV va el nivel real.
- Equivalencias para la línea de idiomas: A2 *Elementary*, B1 *Intermediate*, B2 *Upper-intermediate* o *Professional working proficiency*, C1 *Advanced* / *Full professional proficiency*, C2 *Proficient*. Si tiene un examen (TOEFL, IELTS, Cambridge), el examen y el puntaje van al lado.

## Del inglés al español

Si el CV base es en inglés y hace falta en español:

- Títulos de sección: `Resumen`, `Experiencia`, `Educación`, `Certificaciones`, `Habilidades`, `Idiomas`.
- Fechas `mar. 2023 – actualidad`, números con punto de miles y coma decimal.
- Sin primera persona: el verbo en pasado ("Automaticé", "Lideré").
- Los términos técnicos que el mercado usa en inglés quedan en inglés (*testing*, *deploy*, *pipeline*, *backlog*, *stakeholders*); no se traduce "tablero de Kanban" ni "integración continua" si el aviso dice *CI/CD*.
- Se evitan los calcos inversos: "aplicar a" un puesto va como "postularme", "rol" sí, "posición" mejor "puesto", "remover" va como "sacar" o "eliminar".

## Cómo se entrega

1. Escribí `cv/cv-en.md` (o el idioma que corresponda) con la misma estructura del CV base.
2. **Revisión viñeta por viñeta:** cada viñeta en inglés al lado de su original. Si una dice más que el original (un verbo más fuerte, un alcance mayor, un número redondeado para arriba), se corrige.
3. **Revisión de oído:** leé la versión entera como la leería alguien nativo y marcá lo que suene a traducción: orden de palabras del español, preposiciones (*in* / *on* / *at*), artículos de más, frases largas con muchas comas.
4. Al final del archivo, una tabla corta con **las decisiones de traducción** para que la persona las confirme:

   | En el CV base | En la versión | Por qué |
   |---|---|---|
   | Analista Funcional | Business Analyst | Hacía relevamiento y specs para negocio, no definía producto |
   | Licenciatura en Sistemas | Bachelor's Degree in Information Systems (5-year program) | Que no se lea como un título corto |

5. La versión en inglés pasa por los mismos [Criterios de CV](SKILL.md#criterios-de-cv) y por `ats.md`.
6. Si la persona confirma un cambio en una de las dos versiones, se lleva a la otra: el CV base y su traducción nunca dicen cosas distintas.

## Lo que no se puede comprobar

Decilo al entregar: Claude no conoce la percepción de cada empresa sobre un cargo traducido. Si hay dudas con un cargo, vale preguntarle a alguien que trabaje en el mercado de destino o usar el equivalente que aparece en los avisos a los que apunta.
