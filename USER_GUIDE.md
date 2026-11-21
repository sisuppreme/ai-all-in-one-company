# USER_GUIDE.md — The Operator's Guide

This guide is for **you, the operator**: the person who commissions work from an AI agent that uses this repository. The agent has its own instructions (`BOOTSTRAP.md` and the skills); this file explains what you need to provide, what to expect, what you will be asked to approve, and what to do when something goes wrong.

Current version: **1.0.0** (see `VERSION` and `CHANGELOG.md`).

> **Roman Urdu mein fori shuruaat** chahiye to seedha neechay walay section **"Roman Urdu Quick-Start"** par jayein.

## 1. Prerequisites

You need:

- **An AI agent** that can read this repository — by git clone, by GitHub raw URLs, or through its file-fetch tool. Any of the four entry points in `custom-instructions/` works: Claude Code, Claude, Google AI Studio, or a generic agent.
- **The repository itself.** Its planned GitHub address is https://github.com/sisuppreme/ai-all-in-one-company (not published yet — until it is, hand the agent the repo files or a local clone).
- **A project folder** where the agent will create the project and its documents.
- **Your decisions at three approval points** (Section 4). Everything else, the agent should be able to do from the repo.
- **Secrets, when a project needs them** (API keys, logins): the agent will ask for specific items using the handoff in `templates/SECRETS_CHECKLIST.md`. Never paste secrets into project documents or code.
- **Python 3** — only if you or the agent will run the repo's maintenance scripts (Section 7).

You do **not** need to read the 227 skills. Your working documents are this guide, the project's own `requirements.md` and `progress.md`, and the approval questions the agent brings you.

## 2. Step 0 — Starting the agent on this repo

Do this once per agent/platform:

1. **Paste the custom instructions.** Open the file in `custom-instructions/` that matches your agent (`claude-code.md`, `claude.md`, `ai-studio.md`, or `generic.md`) and paste it into the agent's custom-instructions / system-prompt area. Each file carries the repo address, the version pin ("OmniForge repo v1.0.0, 2026-11-21"), the bootstrap order, the hard rules, and the precedence summary.
2. **Start a session and give the agent your task** in plain words — what you want built, for whom, and any deadline or budget. A filled `templates/USER_BRIEF.md` is the best form for a new project, but a plain description works; the agent turns it into `requirements.md` and bounces anything vague back to you.
3. **The agent then runs the bootstrap on its own** (`BOOTSTRAP.md`):
   - reads `VERSION` and the top `CHANGELOG.md` entry (if the repo version is over 6 months old, it must warn you and re-check tool claims against live sources);
   - scans `SKILLS_INDEX.md` by department and keywords to route your task;
   - loads in stages — `bundles/core.md` first, then the playbook bundle for your project type, then individual skills only where a step needs what a bundle omits. It must never load `bundles/ALL_SKILLS.md` whole;
   - creates the project documents **before any code**: `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md`, and the full file set from the project type's manifest (`templates/mandated-manifest-<type>.txt`).
4. **Your first approval** is `requirements.md` plus the estimate (Section 4). Check that the goal, audience, key features, and acceptance criteria say what you actually want — this document governs everything after it.

Small jobs have a fast path: for a single-file fix or a one-skill task, the agent loads just that skill and its gates instead of the full bootstrap.

## 3. Running a project with a playbook

There are 13 playbooks in `playbooks/`, one per common web-app type: SaaS web app, content/blog site, API + database service, e-commerce store, clone rebuild, dashboard/admin panel, booking & scheduling, online learning (LMS), landing page, portfolio/marketing site, internal CRUD admin tool, two-sided marketplace, and realtime chat app.

When your task matches a playbook, the agent follows it step by step. Each playbook states the goal, the department order, which skills to load, which gates apply at each step (by gate ID), what to do when something fails, the definition of done, and a worked mini-example.

What you should expect during a run:

- **`progress.md` is the live record.** It holds the repo version, per-gate pass/fail with evidence (command output, test result, or screenshot), blockers, and substitutions. If you want to know where a project stands, ask the agent to show you `progress.md` — a gate claimed passed without evidence is not passed.
- **Gates run at every step**, not once at the end. When a gate fails, the agent fixes the work — it is not allowed to weaken the gate to make it pass.
- **Facts are checked against `fact-sheet.md`.** Every figure, name, and claim in the product must trace to a real source recorded there. If the agent cannot source something, it must say so rather than invent it (the Real Content Rule).
- **Definition of done** includes a named **pre-provisioning complete** state: everything except provisioning-waived gates is green, the waivers are recorded with their unblocking conditions, and what remains is listed — so a project can be honestly "done locally" before any hosting exists.

If your task matches no playbook, the agent routes by keywords through `SKILLS_INDEX.md` to the relevant departments. If nothing matches at all, it loads the core bundle and asks you — that is expected behaviour, not a failure.

## 4. Your approval points

The agent must stop for your approval at exactly three points:

1. **`requirements.md` + the estimate**, after requirements are written.
2. **The deploy target + cost**, before deployment — agree a monthly cost cap upfront; the agent must get your approval before provisioning anything above the estimate.
3. **The live switch**, before go-live.

Two refinements, so you are not asked twice: a decision already recorded in your commissioning brief or in `requirements.md` **counts** as the approval for its point; and if you are unreachable during an unattended run, the agent follows the stuck protocol (log-and-continue, then safe defaults) and records the substitution in `progress.md` — except for money, legal positions, and destructive actions, which always wait for you.

## 5. Gates and the waiver protocol (§6.3)

Gates are the repo's quality checks — each skill carries at least three, and `gates/` holds the shared registry (69 acceptance gates, the G-QA-01…10 QA protocol, and the final acceptance checklist). The rules that protect you:

- **A gate is never skipped silently.** It has three lawful outcomes only: **pass** (with evidence), **pass by its named fallback form** (many gates define a manual form — a checklist walk, a diff, a read-through — or a substitute-evidence path for when a tool or account is unavailable; a manual pass is a real pass, recorded as manual), or a **recorded waiver**.
- **A waiver is a written record**, in the project's `progress.md` and `DECISIONS.md`: which gate, why it cannot pass, what was checked instead, and the condition that unblocks it. Provisioning waivers (no hosting, CI, domain, or provider account exists yet) are the common case — they keep a project honestly finishable without pretending deployment happened.
- **Security, legal, and Real Content gates (precedence ranks 1–3) can only be waived with your explicit agreement.** If an agent asks to waive one of these, that question is real — read it before agreeing. All other waivers need only the written record.
- **If anyone asks the agent to skip a security or QA gate outright**, the agent must refuse the skip and offer the waiver process instead.

## 6. When the agent is stuck

The stuck protocol lives in `docs/TROUBLESHOOTING.md`. In summary, the agent's escalation path is **skill → links → log → user → safe default**:

0. **Name the blocker type** — missing information, two skills contradicting (the `BOOTSTRAP.md` precedence order decides; the conflict is logged), an external outage or tool failure (retry twice, log, move on), a missing credential (the secrets handoff), or an ambiguous/impossible requirement.
1. **Re-read the skill** — its checklist and gates, once, thoroughly. A step that failed twice the same way is not retried a third time without new information.
2. **Check the links** — `docs/DEPARTMENT_LINKS.md` and the skill's Depends-on / Feeds-into neighbours. If no skill covers the problem, it is logged as a repo **GAP** and reported to you (or filed as an issue), never silently papered over.
3. **Log the blocker and keep working** — the blocker, what was tried, and what is needed go into `progress.md`; all unblocked work continues. Accumulated blockers are batched into **one** message to you, with a concrete option per blocker.
4. **Ask you — with concrete options and a recommendation**, never an open "what should I do?". While waiting, the agent keeps working on everything else. If you do not answer, it applies the **safe default**: ship the affected section as an honest empty state, or defer the feature with a dated TODO — and records that the default was applied.
5. **The never list** — never invent data, never skip a gate, never silently drop a requirement, and never guess on money, legal positions, or destructive actions.

Your part in this: when the agent does bring you a batched question, answering it (even with "go with your recommendation") unblocks everything behind it.

## 7. Maintaining the repo

`SKILLS_INDEX.md` and everything in `bundles/` are **generated files — never hand-edit them.** To change the repo: edit the skill (or playbook/gate) source, then regenerate and validate:

```bash
python3 scripts/build-index.py       # rebuild SKILLS_INDEX.md from skill metadata
python3 scripts/build-bundles.py     # rebuild all bundles; enforces the token caps
python3 scripts/validate-skills.py   # format/ID/gate/example checks over every skill
```

The build is healthy when validation reports **"Checked 227 skills. ALL PASS"** and bundle generation reports no cap failures (caps: `core.md` under 10,000 tokens; every other capped bundle at most 30,000 tokens; tokens = ceil(characters ÷ 4)). `scripts/generate-project.py` scaffolds a new project's mandated file set. The full maintenance procedure — versioning, the changelog, periodic re-verification — is in `docs/MAINTENANCE_RUNBOOK.md`; how to propose changes is in `CONTRIBUTING.md`; every structural decision and deviation is recorded in `docs/DECISIONS.md`.

## 8. Troubleshooting pointers

| Symptom | Where to look |
|---|---|
| Agent cannot fetch the repo | Ask it to proceed from a pasted `bundles/core.md` and flag the gap in `progress.md` (`BOOTSTRAP.md`, "Fetching and fallback") |
| Agent asks questions the brief already answered | Point it at `BOOTSTRAP.md`'s approval-points rule: brief-recorded decisions count as approval |
| A gate names a tool that is not installed | `docs/TROUBLESHOOTING.md`, tool-bootstrap section: project-local install first, then the gate's manual form, then a waiver — never a silent skip |
| Two skills give conflicting instructions | The 19-rank precedence order in `BOOTSTRAP.md`; the conflict must be logged in the project's `DECISIONS.md` |
| A claim in the product has no source | It should not be there: the Real Content Rule + the project's `fact-sheet.md` govern every fact |
| Repo version is old | `BOOTSTRAP.md` step 0: over 6 months old means the agent warns you and re-checks tool claims live |
| You want the state of a project | The project's `progress.md` — gates with evidence, blockers, waivers, substitutions |
| A term is unclear | `docs/GLOSSARY.md` |

---

## Roman Urdu Quick-Start

*(Yeh section un operators ke liye hai jo Roman Urdu mein parhna pasand karte hain. Baqi guide English mein hai.)*

### Yeh repo kya hai?

OmniForge aik poori web company ka knowledge aik hi repository mein hai: **227 skills, 18 departments** (product, design, coding, security, testing, waghera), **203 detection parameters** jo AI ki aam ghaltiyon ko pakarte hain, aur **13 playbooks** — mukhtalif qisam ki websites/apps banane ke mukammal tareeqay. Is ka maqsad yeh hai ke **aik hi AI agent**, baghair kisi doosri madad ke, professional web application research se lekar build, test aur handover tak khud bana sakay. Har fact real aur sourced hota hai — fake data, fake reviews ya fake features bilkul mana hain.

### Shuru kaise karna hai — 3 steps

1. **Custom instructions paste karein.** `custom-instructions/` folder se apne agent ke mutabiq file chunein (Claude Code, Claude, AI Studio, ya generic) aur usay agent ki custom instructions mein paste kar dein. Bas aik dafa karna hai.
2. **Apna kaam plain alfaaz mein batayein** — kya banana hai, kis ke liye hai, budget ya deadline kya hai. Agent pehle project ki documents banayega (`requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md`) — **code baad mein, documents pehle**. Requirements par aap ki approval pehla approval point hai; ghoor se parh kar confirm karein.
3. **Agent ko kaam karne dein.** Woh khud `BOOTSTRAP.md` follow karega, sahi playbook aur skills load karega, aur har step par quality gates check karega. Aap ko sirf **3 jagah** approval deni hai: requirements + estimate, deploy target + cost, aur go-live se pehle live switch. Jo faisla aap pehle brief mein likh chuke hain, woh dobara nahi poocha jayega.

### Playbook kaise chalana hai?

Har aam project type ke liye aik playbook hai — masalan SaaS app, blog site, online store, booking system, LMS, chat app. Aap ko kuch khaas nahi karna: bas apna project describe karein, agent khud matching playbook chunta hai aur us ke steps follow karta hai. Progress dekhni ho to agent se **`progress.md`** mangwayein — us mein har gate ka pass/fail saboot ke sath, aur tamam blockers aur waivers likhe hote hain. Gate kabhi khamoshi se skip nahi hota: ya pass hota hai, ya us ki manual form se pass hota hai, ya likha hua waiver banta hai. Security, legal ya real-content gate ka waiver **aap ki wazeh ijazat** ke baghair nahi ho sakta.

### Masla aaye to kya karna hai?

- **Agent phas jaye** to woh `docs/TROUBLESHOOTING.md` ka stuck protocol follow karega: pehle skill dobara parhega, phir linked skills check karega, blocker ko `progress.md` mein log karke baqi kaam jari rakhega, aur aakhir mein aap ko **aik hi message mein, concrete options aur apni recommendation ke sath** poochega. Aap sirf wohi batched sawal jawab dein — "recommendation par chalo" kehna bhi kaafi hai.
- **Koi secret ya API key chahiye** ho to agent `templates/SECRETS_CHECKLIST.md` ke zariye specific cheez mangega. Secrets kabhi code ya documents mein na likhein.
- **Gate fail ho raha ho** to agent kaam fix karega, gate ko kamzor nahi karega. Agar koi tool ya hosting maujood na ho to manual form ya likha hua waiver use hoga — jhooti "pass" report kabhi nahi.
- **Repo update karna ho** to generated files (`SKILLS_INDEX.md`, `bundles/`) haath se edit na karein — skill edit karke yeh teen commands chalayein: `python3 scripts/build-index.py`, `python3 scripts/build-bundles.py`, `python3 scripts/validate-skills.py`. Aakhir mein "ALL PASS" aana chahiye.
