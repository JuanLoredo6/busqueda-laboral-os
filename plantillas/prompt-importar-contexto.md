# Prompt para traer tu contexto desde otro chat

> Para quien ya habló de su búsqueda o de su carrera con Claude en el chat, ChatGPT, Gemini u otra IA.
> `/empezar` te lo ofrece en el paso 2, antes de crear nada. Copiá el bloque de abajo, pegalo en ese chat (en la conversación
> o el proyecto donde está tu contexto) y pegá la respuesta en Claude Code.
>
> Lo que vuelve no entra solo a tu perfil: Claude te lo muestra por partes y vos confirmás cada una.
> Antes de pegar la respuesta, borrá cualquier dato sensible que haya quedado (documento, datos bancarios,
> contraseñas, datos de salud).

```text
Estoy armando un sistema para ordenar mi búsqueda laboral y quiero llevarle todo lo que vos ya sabés de mí:
lo que hablamos en esta conversación, en otras, en tus memorias o en los archivos del proyecto.

Devolveme un único bloque en Markdown con exactamente estas secciones y en este orden. Reglas:

- Solo lo que yo te dije o te mostré. No completes huecos, no mejores redacciones, no infieras logros.
- Marcá cada línea con [DIJE] si lo dije o mostré yo, o con [INFERIDO] si es una conclusión tuya.
- Los números, fechas, cargos y tecnologías, copialos tal cual los dije. Si no estás seguro, poné [DUDOSO].
- Si una sección no tiene nada, escribí "Sin datos". No la inventes.
- No incluyas documento de identidad, datos bancarios, contraseñas ni datos de salud.

## 1. Datos básicos
Ciudad y país, idiomas con nivel, links (LinkedIn, portfolio).

## 2. Experiencia
Por cada trabajo, del más reciente al más antiguo: empresa, puesto, fechas, qué hacía la empresa,
qué hacía yo, logros con su número o hecho concreto, tecnologías y herramientas.

## 3. Formación y certificaciones

## 4. Habilidades
Técnicas y de trabajo con personas.

## 5. Historias para entrevistas
Situaciones reales que te conté: situación, qué hice, resultado, qué aprendí.

## 6. Qué busco
Roles, seniority, industrias, modalidad y ubicación, tipo de contratación, disponibilidad, qué descarto.

## 7. Cómo cuento mi salida del último trabajo
La frase que uso, si la definimos. Literal.

## 8. Lo que no quiero que se mencione
Temas que te pedí no mencionar (por ejemplo, pretensión salarial). Solo el tema, no el dato.

## 9. Mi tono
Cómo escribo, palabras que uso y que no uso nunca, el tono que me gusta y el que no.
Si tenés textos que escribí yo (no vos), pegá hasta 3 tal cual.

## 10. Mi búsqueda hasta hoy
Postulaciones en curso (empresa, rol, en qué etapa está, fecha), entrevistas, rechazos y feedback que recibí,
números que medí (postulaciones, respuestas, entrevistas).

## 11. Decisiones que ya tomé
Por ejemplo: a qué roles dejé de apuntar y por qué. Con fecha si la sabés.

## 12. Lo que todavía no resolví
Dudas abiertas o datos que me faltaba confirmar.
```
