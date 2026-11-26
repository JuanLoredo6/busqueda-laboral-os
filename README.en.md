# Búsqueda laboral OS (Job Search OS)

**English** · [Español](README.md) · [Português](README.pt-BR.md)

A system to organize your job search with **Claude Code**: your profile, LinkedIn and CV, every application, interview preparation and a dashboard that tells you what to do today. Everything stays in folders on your own computer.

We built it for a workshop among IT colleagues who are looking for their next challenge. It works for any profile: development, QA, data, product, design, infrastructure, projects.

> **Language:** Claude talks to you in Spanish (Rioplatense) or Brazilian Portuguese, and writes your CV, LinkedIn, messages and interview answers in Spanish, English or Brazilian Portuguese. Commands, skills, templates and the dashboard are in Spanish. This page explains what it does for English-speaking readers.

> **🎓 Live workshop «Buscá con sistema»** (in Spanish): two sessions with personal guidance to use this system in your job search. Dates, prices and scholarships at **[busca-con-sistema.pages.dev](https://busca-con-sistema.pages.dev/)**.
>
> Are you a headhunter or an independent recruiter? Check the **Recruiters** section on the same page.

---

## Guided installation

You need a **Claude Pro or Max** plan and the **Claude desktop app** ([claude.com/download](https://claude.com/download)). No coding or GitHub account required.

1. Open the app, go to the **Code** tab, and choose your **Documents** folder as the working folder.
2. Paste this request:

```
Instalá el sistema de búsqueda laboral siguiendo, etapa por etapa, la guía https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/INSTALACION.md
```

Claude guides you step by step: it downloads the system, helps you open it in its folder, connects Gmail and Google Calendar (read-only) and checks that everything works. The full guide, with the prerequisites and what to do if something gets stuck, is in **[INSTALACION.md](INSTALACION.md)** (Spanish).

When it's done, in the system's folder, type:

```
/empezar
```

### If you prefer to do it by hand

With Git installed, in a terminal:

```bash
git clone https://github.com/JuanLoredo6/busqueda-laboral-os.git mi-busqueda
```

In the desktop app, choose the `mi-busqueda` folder as the working folder of a new session.

### Common issues

| What happens | What to do |
|---|---|
| I type `/empezar` and nothing shows up | Claude Code is open in a different folder. Start a new session **in the system's folder** (the one with `CLAUDE.md` inside). Skills only load there |
| Claude asks for permission for everything | Inside the system's folder, reading and editing files is already allowed. It will ask before searching the web or running other commands: read what it wants to do and accept if it makes sense |
| The dashboard says «Todavía no hay datos» (no data yet) | Run `/empezar` first. If you already did, ask Claude: «regenerá el tablero» |
| The dashboard doesn't update | Reload the page (F5). If it stays the same, ask Claude: «corré tablero/sincronizar.sh» |
| The dashboard says the automatic sync is «atrasada» (behind) | The scheduled task only runs while the Claude desktop app is open. Open it and click 🔄 SYNC to catch up |
| `/sincronizar-correo` says a connector is missing | Click the **+** next to the message box → connectors → Gmail or Google Calendar → Connect. If Claude still can't see it, start a new session. Details in [INSTALACION.md](INSTALACION.md), stage 5 |
| On a Mac it says `git` is missing | Accept the window that offers to install the developer tools, wait for it to finish and try again |
| I don't know what to do next | Ask Claude «¿qué hago ahora?» or type `/mapa-de-skills` |

---

## How to use it

| When | What you tell Claude |
|---|---|
| The first time | `/empezar` |
| To improve LinkedIn and your CV (leave your LinkedIn PDF in `linkedin/`, your CV in `cv/`, or both) | `/mejorar-perfil` |
| When you see a job post you like | `/analizar-oferta` and paste the link or the text |
| To apply | `/nueva-postulacion` |
| When something happens ("X got back to me") | Just tell it, or `/actualizar` |
| To bring in what arrived by email or on the calendar | 🔄 SYNC on the dashboard, or `/sincronizar-correo` |
| To write to someone | `/redactar-mensaje` |
| Before an interview | `/preparar-entrevista` |
| On Fridays | `/repaso-semanal` |
| To see everything available | `/mapa-de-skills` |

You don't need to remember the names: if you ask in your own words, Claude picks the right skill.

### The dashboard

Open `tablero/tablero.html` with a double click and keep it open in a tab. It shows:

- **Today:** whether you have something to do today, and what.
- **What you need to do:** actions grouped as overdue, today, next few days and no date.
- **Applications:** a kanban with the columns To send, Waiting for a reply and In conversation, and the days without news for each one.
- **Numbers:** applications sent, response rate, active conversations and overdue actions.

It updates by itself every time Claude changes something.

**To have your changes saved automatically**, open it with `tablero/abrir-tablero.bat` on Windows or `tablero/abrir-tablero.command` on Mac (requires Python). Marking an action as done, moving a card, adding a note or a new action, or fixing the sent date with ✏️, is then saved right away, without going through Claude. Closing an application still goes through Claude, because it needs the outcome. The server only listens on your computer and stops when you close its window.

If you open it with a double click instead, your changes stay pending: click **Copiar pedido para Claude** (copy request for Claude) and paste it into Claude Code so it gets saved. The **⚡** button on each action copies a request so Claude can help you with that task.

With the server running, the **🎯 Práctica** button opens the practice for the interviews you prepared with `/preparar-entrevista`. You answer each question by typing or out loud (dictation is optional: if you have [uv](https://docs.astral.sh/uv/) installed, your voice is transcribed on your computer with Whisper and the audio never leaves it; the first time it downloads about 480 MB. Without uv, it uses the browser's speech recognition, which processes the audio in the cloud). The page times your answers, saves them in the interview folder and gives you a one-line request so Claude can give you feedback and update your preparation score.

**Retro dashboard.** If you'd rather have something more playful, open `tablero/abrir-tablero-retro.bat` on Windows or `tablero/abrir-tablero-retro.command` on Mac: your applications become a pixel-art town you walk around with the keyboard (the town is in Spanish). Each status is a neighborhood and each application a house, with a «!» when something is pending; inside each house you find the company, the role, your fit, the history and a desk with its tasks. **A** looks and enters, **S** copies the request for Claude, **D** marks a task as done, **Enter** shows your priorities and the character walks to the one you pick, and **M** opens the minimap. The square has the notice board, the sync mailbox, the calendar and the moving truck; the University, the lighthouse and your home cover improving your profile, the weekly review and the settings (day or night, walking or biking, music and sounds). It uses the same data and the same local server as the kanban, on another port (8766), so you can keep both open: what you mark is saved the same way.

To see it with sample data before loading your own, open the dashboard and click **Ver el tablero con datos de ejemplo** (see the dashboard with sample data).

### Updates from Gmail and Google Calendar (optional)

Claude can check your email and calendar **read-only** and bring what arrives to the dashboard: confirmations, recruiter replies, scheduled interviews, rejections.

1. Connect Gmail and Google Calendar in claude.ai → **Settings → Connectors**, with your Google account. Then start a new Claude Code session in the system's folder.
2. Click **🔄 SYNC** on the dashboard and paste the request into Claude Code, or type `/sincronizar-correo`. The first time, Claude asks for permission to read: choose **always allow** for searching and reading emails and for listing events.
3. To have it run on its own **every 2 hours, from 8 am to 10 pm**, type `/sincronizar-correo configurar`. This creates a scheduled task in the Claude desktop app, which runs while the app is open.

What is clear (an interview with a date, an explicit rejection) is applied automatically. Anything doubtful, offers and suspicious emails stay in **«Para revisar»** (to review) on the dashboard, for you to decide. Claude never replies to, archives or deletes emails.

---

## What's inside

```
busqueda-laboral-os/
├── INSTALACION.md     The guided installation guide
├── CLAUDE.md          Instructions for Claude: limits, folders, data model
├── contexto/          Your source of truth: profile, what you're looking for, your voice, decisions · importado/ with what you bring from before
├── linkedin/          Your LinkedIn PDF · sugerencias/ with the new texts
├── cv/                Your CV
├── postulaciones/     postulaciones.json (dashboard data) + one folder per application
├── entrevistas/       One folder per company with the preparation
├── investigacion/     Dated reports: diagnosis, market, metrics, reviews
├── tablero/           tablero.html (open it with a double click)
├── plantillas/        What /empezar copies the first time
└── .claude/skills/    The 19 skills
```

### The skills

**Day to day**

| Skill | What it's for |
|---|---|
| `empezar` | Setup: brings in what you already have (CV, LinkedIn, notes, the context from another AI), loads your profile, what you're looking for and your voice, and gets the dashboard ready |
| `mejorar-perfil` | Reads your LinkedIn PDF, your CV or both, compares what each one has, interviews you and gives you ready-to-paste texts, plus the CV. Also in English or Brazilian Portuguese, written the way a native speaker would |
| `analizar-oferta` | How well a job post fits your profile (0 to 100), requirement by requirement, and whether it's worth it |
| `nueva-postulacion` | Folder, tailored CV, form answers and a card on the dashboard |
| `actualizar` | Takes every update to the dashboard and creates the next actions |
| `sincronizar-correo` | Brings updates from Gmail and Google Calendar to the dashboard, on demand (🔄 SYNC) or every 2 hours from 8 am to 10 pm |
| `redactar-mensaje` | Messages to recruiters, referrals, follow-ups and thank-you notes in your voice |
| `preparar-entrevista` | Likely questions, real stories for each one in STAR-L format (Situation, Task, Action, Result, Learnings), and a mock interview with feedback |
| `repaso-semanal` | The week's numbers, what's slipping, and three priorities |

**Search strategy**

| Skill | What it's for |
|---|---|
| `diagnostico-busqueda` | Why your search isn't moving: symptom, cause and hypotheses to test, and which numbers to watch to know if you're making progress |
| `mercado-laboral` | Where the demand for your profile is and which companies to target, with sources |
| `posicionamiento` | Which role you're aiming for, what problem you solve, for whom and what you rule out. Then, angles to present yourself, your 30-second pitch and your headline |
| `plan-de-networking` | Who to ask for a chat, what to ask and how to write to them |
| `aprendizajes-busqueda` | What real feedback (rejections, interviews, chats) is telling you |

**Judgment tools**

| Skill | What it's for |
|---|---|
| `poner-a-prueba` | Pushes back on every achievement and every decision until it holds up |
| `recruiters-sinteticos` | Tests your CV, pitch or message against simulated recruiters |
| `disenador-visual` | Specifies and builds a CV, LinkedIn banner, presentation or portfolio |
| `mapa-de-skills` | The index of everything above |

---

## Your data

- Everything that's yours (profile, CV, applications) stays **only on your computer**. The `.gitignore` prevents it from being pushed to GitHub by mistake.
- **Don't push your copy to a public repository.** If you want a backup, copy the folder to your cloud (Drive, OneDrive, iCloud) or use a **private** repository.
- Claude doesn't send messages or applications for you: it drafts, and you send.

## Updating the system

When there is a new version, open Claude Code in the system folder and ask «actualizá el sistema». If your copy is older than 0.12.0, paste this request:

```text
Actualizá el sistema de búsqueda laboral siguiendo la guía https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/ACTUALIZACION.md
```

Claude first backs up your data, brings the new code (with Git or the ZIP, depending on how you installed it), adapts your data to what changed and tells you what is new. The step by step is in [ACTUALIZACION.md](ACTUALIZACION.md) (in Spanish).

What changed in each version: [CHANGELOG.md](CHANGELOG.md).

## If you switch computers

Your data is not on GitHub (the `.gitignore` keeps it out), so downloading the system again is not enough: you move **the whole folder in a ZIP**, with its hidden folders (`.git`, `.claude`). That way your data, the version of your data and the link to receive updates all travel together.

1. **On your current computer**, open Claude Code in the system folder and paste:

   ```text
   I'm moving this system to another computer. Confirm you are in the system folder and tell me what data of mine is here. Make a ZIP of the whole folder, including hidden folders and files (.git, .claude, .version-datos), on my Desktop named mi-busqueda-traspaso plus today's date. Check that the ZIP has them, tell me its size and whether I have a scheduled sync task. Don't upload the ZIP anywhere and don't delete anything from this folder.
   ```

2. **Carry the ZIP** on a USB drive or in your own cloud (Drive, OneDrive, iCloud), without sharing the link: your CV is inside. Delete it from there when you are done.
3. **On the new computer**, install the Claude app, sign in with the same account, **Code** tab, **Local** environment, open the **Documents** folder and paste (with the ZIP's location):

   ```text
   I brought my job search system from another computer in a ZIP located at [where it is]. Unzip it into Documents as mi-busqueda (if it already exists, don't overwrite it and ask me). Check that CLAUDE.md, .claude/skills/empezar/SKILL.md and my data in postulaciones and contexto are there. Tell me the full path and how to open a new session in that folder.
   ```

4. In the new session, type **seguí con la instalación**: Claude sees the system is already there and picks up from the Gmail and Calendar connectors and the board.
5. If you used automatic sync, create it again with `/sincronizar-correo configurar`: scheduled tasks don't move between computers. Old chats don't either, but everything important is in the files.

The copy is a snapshot: from then on, work on the new computer. If you keep adding things on both, they drift apart. The old folder stays as a backup.

---

## Installation instructions for Claude Code

*This section is for Claude.* If you were asked to install this system, follow the protocol in [INSTALACION.md](INSTALACION.md), part 2, stage by stage.

---

## Credits

- System built by Juan Rodríguez Loredo for the workshop. MIT License: see [LICENSE](LICENSE).
- Thirteen pieces of the system (skills or parts of a skill) are adaptations of the product skills by **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), MIT License). Details in [CREDITOS.md](CREDITOS.md).
- Several sections adapt methods by **Paweł Huryn** ([The Product Compass](https://www.productcompass.pm)), published under the MIT License in [pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) and [pm-brain](https://github.com/phuryn/pm-brain). Details in [CREDITOS.md](CREDITOS.md).
