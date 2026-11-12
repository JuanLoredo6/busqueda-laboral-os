// Datos de ejemplo de una persona ficticia, para mostrar el tablero en el taller.
// Las fechas se calculan desde hoy para que el ejemplo nunca quede viejo.
// Se ven abriendo tablero.html?ejemplo (o con el botón "Ver el tablero con datos de ejemplo").
window.DATOS_EJEMPLO = function () {
  function d(n) {
    var x = new Date();
    x.setDate(x.getDate() + n);
    return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
  }
  return {
    version: 1,
    persona: "Lucía (ejemplo)",
    actualizado: d(0) + "T09:30",
    postulaciones: [
      {
        id: "nimbo-qa-automation-sr", empresa: "Nimbo Pagos", rol: "QA Automation Senior · remoto",
        link: "", canal: "Referido", columna: "conversacion", resultado: null, encaje: 84,
        estado: "Pasó la charla con RR. HH. Entrevista técnica agendada.",
        proximo: "Entrevista técnica con el líder de QA", creada: d(-16), enviada: d(-14), ultimaNovedad: d(-2),
        contacto: "Martina (Talent Acquisition)",
        historial: [
          { fecha: d(-14), texto: "Me refirió Diego, ex compañero de Andes Soft." },
          { fecha: d(-8), texto: "Charla con Martina de RR. HH.: buena, preguntó por la migración a Playwright." },
          { fecha: d(-2), texto: "Me agendaron la técnica con el líder de QA." }
        ]
      },
      {
        id: "tienda-sur-qa-lead", empresa: "Tienda Sur", rol: "QA Lead · híbrido",
        link: "", canal: "LinkedIn", columna: "esperando", resultado: null, encaje: 71,
        estado: "Postulada por LinkedIn con CV adaptado.", proximo: "Follow-up a la recruiter",
        creada: d(-11), enviada: d(-10), ultimaNovedad: d(-10), contacto: "",
        historial: [{ fecha: d(-10), texto: "Postulada por LinkedIn. CV adaptado al foco en liderazgo." }]
      },
      {
        id: "datalab-sdet", empresa: "DataLab", rol: "SDET · contractor EE. UU.",
        link: "", canal: "Portal de la empresa", columna: "esperando", resultado: null, encaje: 66,
        estado: "Postulada por el portal.", proximo: "Esperar respuesta",
        creada: d(-4), enviada: d(-4), ultimaNovedad: d(-4), contacto: "",
        historial: [{ fecha: d(-4), texto: "Postulada por el portal, con CV en inglés." }]
      },
      {
        id: "salud-digital-qa", empresa: "Salud Digital", rol: "QA Engineer Semi Senior",
        link: "", canal: "", columna: "por-enviar", resultado: null, encaje: 58,
        estado: "Analizada: falta experiencia con apps móviles (deseable).", proximo: "Decidir si me postulo",
        creada: d(-1), enviada: null, ultimaNovedad: d(-1), contacto: "", historial: []
      },
      {
        id: "andes-bank-qa", empresa: "Andes Bank", rol: "Analista QA",
        link: "", canal: "Portal de la empresa", columna: "cerrada", resultado: "descartada", encaje: 62,
        estado: "Rechazo automático por correo, sin feedback.", proximo: "",
        creada: d(-20), enviada: d(-19), ultimaNovedad: d(-12), contacto: "",
        historial: [{ fecha: d(-12), texto: "Rechazo automático: 'avanzamos con otros perfiles'." }]
      }
    ],
    acciones: [
      { id: "a1", texto: "Follow-up a la recruiter de Tienda Sur", postulacion: "tienda-sur-qa-lead", fecha: d(-1), condicion: "solo si no hubo respuesta", prioridad: "alta", hecha: false, hechaEl: null, pedido: "/redactar-mensaje follow-up tienda-sur-qa-lead" },
      { id: "a2", texto: "Preparar la entrevista técnica con Nimbo Pagos", postulacion: "nimbo-qa-automation-sr", fecha: d(0), condicion: "", prioridad: "alta", hecha: false, hechaEl: null, pedido: "/preparar-entrevista nimbo-qa-automation-sr" },
      { id: "a3", texto: "Decidir si me postulo a Salud Digital", postulacion: "salud-digital-qa", fecha: d(2), condicion: "", prioridad: "media", hecha: false, hechaEl: null, pedido: "/analizar-oferta salud-digital-qa" },
      { id: "a4", texto: "Repaso de la semana", postulacion: null, fecha: d(3), condicion: "", prioridad: "media", hecha: false, hechaEl: null, pedido: "/repaso-semanal" },
      { id: "a5", texto: "Pedir 2 recomendaciones en LinkedIn a ex compañeros", postulacion: null, fecha: null, condicion: "", prioridad: "baja", hecha: false, hechaEl: null, pedido: "/redactar-mensaje pedido de recomendación en LinkedIn" },
      { id: "a6", texto: "Aplicar los cambios del perfil en LinkedIn", postulacion: null, fecha: d(-6), condicion: "", prioridad: "alta", hecha: true, hechaEl: d(-6), pedido: "" },
      { id: "a7", texto: "Mandar agradecimiento a Martina después de la charla", postulacion: "nimbo-qa-automation-sr", fecha: d(-8), condicion: "", prioridad: "media", hecha: true, hechaEl: d(-8), pedido: "" }
    ]
  };
};
