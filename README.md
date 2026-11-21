# OmniForge — ai-all-in-one

**A company in a repository.** OmniForge packages the working knowledge of a complete web-application company — product, architecture, frontend, backend, data, DevOps, security, QA, SEO, legal, analytics, accessibility, integrations, AI features, and customer experience — as structured skills that **one AI agent** can load and execute end-to-end: research, build, verify, deploy, document, and hand over professional **web applications**, with real content only and every claim sourced.

- **Version:** 1.1.0 (see `VERSION` and `CHANGELOG.md`)
- **Published, public:** https://github.com/sisuppreme/ai-all-in-one-company — the address the custom-instructions files are written against.

## What's inside

| Component | Count | Where |
|---|---|---|
| Skills | 235 | `skills/<department>/<skill>/SKILL.md` |
| Departments | 18 (D1–D18) | `skills/` |
| Detection parameters | 203 across 7 families (visual, code, infra, content, UX, fake, crawl) | `skills/detection/` |
| Playbooks | 21 — 13 per common web-app type + 8 hybrid mission playbooks (v1.1.0) | `playbooks/` |
| Bundles | 43 files — the always-on core, 20 department bundle files (18 departments; `seo-content` and `devops-deployment` each split across two files), 21 playbook bundles (one per playbook), plus a reference-only `ALL_SKILLS.md` | `bundles/` |
| Gates | 69 inherited acceptance gates + the 10-gate skill-release QA protocol (G-QA-01…10), plus at least 3 gates inside every skill | `gates/`, `skills/` |
| Worked examples | 706 before/after example files (3 per skill; `vector-db` carries a fourth) + 18 department example documents | `skills/*/examples/`, `examples/` |

Every skill follows one memory-proof format: numbered rules with stable IDs, a BAN list (each banned pattern names the detection parameter it defeats and gives the correct replacement), gates with evidence requirements, anti-patterns, examples, recall anchors, and a checklist.

## Who it is for

- **A single AI agent** working alone — the repository is designed and proof-tested for one agent with no sub-agents, no leads, and no hand-offs. Everything the agent needs (routing, precedence when skills disagree, what to do when stuck, when to ask the operator) is written down in the repo itself.
- **Its operator** — the person who commissions projects, answers the three approval points (requirements, deploy target and cost, go-live), supplies secrets through the handoff checklist, and gives the final ship approval.

Phase 1 scope is **web applications**. Mobile and desktop applications are a later phase and are not covered by the current playbooks.

## How to start

1. **Give your agent the entry point for its platform** — copy the matching file from `custom-instructions/` (`claude-code.md`, `claude.md`, `ai-studio.md`, or `generic.md`) into the agent's custom instructions. Each file contains the repo address, the version pin, the bootstrap order, the hard rules, and the precedence summary.
2. **The agent follows `BOOTSTRAP.md`** — the repo-first protocol: read `VERSION` + the top `CHANGELOG.md` entry, scan `SKILLS_INDEX.md`, load in stages (core bundle → playbook bundle → individual skills only where a step needs more), and create the project documents (`requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md`) **before any code**.
3. **Work runs under gates.** Every step's gates are checked with evidence recorded in `progress.md`. A gate has exactly three lawful outcomes: pass, pass by its manual/substitute-evidence form, or a recorded waiver — never a silent skip.
4. **If the agent gets stuck**, it follows the stuck protocol in `docs/TROUBLESHOOTING.md` (skill → links → log → user → safe default) instead of inventing a way out.

Operators: read `USER_GUIDE.md` — it walks the whole route in plain language, including a Roman Urdu quick-start.

### Hybrid playbooks (v1.1.0)

Not every project starts from a blank page. The 8 hybrid playbooks are mission-level workflows: each combines several departments in the order the mission actually needs them, and each anchors on one of the 8 skills added in v1.1.0 for work that is not "build new" — `clone-redesign` and `rebrand-execution` (D16), `project-takeover` and `prototype-hardening` (D15), `seo-migration` (D9), `ai-retrofit` (D17), `market-expansion` (D1), and `saas-conversion` (D2).

| Playbook | Mission |
|---|---|
| `clone-and-redesign` | Clone a reference product's function, then redesign everything — original design, brand, and copy |
| `clone-and-rebrand` | Keep a working product's function; replace its identity end-to-end (name, logo, palette, voice) |
| `rescue-and-relaunch` | Take over a broken or abandoned live product, audit it, fix in priority order, and relaunch safely |
| `replatform-migration` | Move a live product to a new stack or platform with zero data loss and search rankings preserved |
| `prototype-to-production` | Turn a rough MVP or prototype (including AI-generated output) into production-grade software |
| `ai-ify-existing-product` | Add AI features to a live non-AI product without breaking what already works |
| `localize-new-market` | Launch an existing product in a new country — language, payments, legal, pricing, support |
| `single-app-to-saas` | Convert a single-client application into a multi-tenant SaaS with billing and tenant isolation |

## Use it on your platform — exact files and links

Repository home: https://github.com/sisuppreme/ai-all-in-one-company

Every platform starts the same way: **one** custom-instructions file from `custom-instructions/`, pasted into the platform's instructions box. Then, if the agent cannot open GitHub itself, paste `bundles/core.md` plus the one playbook bundle that matches your project (all bundles: https://github.com/sisuppreme/ai-all-in-one-company/tree/main/bundles). Never paste `bundles/ALL_SKILLS.md` — it is a human reference only.

### Google AI Studio

1. Open this file and copy its full content: https://github.com/sisuppreme/ai-all-in-one-company/blob/main/custom-instructions/ai-studio.md
2. Go to https://aistudio.google.com, start a new chat, and paste the content into **System instructions**.
3. In your first message, also paste:
   - Core bundle (always): https://github.com/sisuppreme/ai-all-in-one-company/blob/main/bundles/core.md
   - The playbook bundle for your project type, e.g. SaaS: https://github.com/sisuppreme/ai-all-in-one-company/blob/main/bundles/saas-web-app.md
4. Describe your project. The agent then works under the repo's rules and gates.

### Claude (claude.ai)

1. Copy this file: https://github.com/sisuppreme/ai-all-in-one-company/blob/main/custom-instructions/claude.md
2. Create a **Project** in Claude and paste the content into the project's **custom instructions**.
3. Add `bundles/core.md` and your playbook bundle as project files/knowledge (links above).

### Claude Code

1. Copy this file: https://github.com/sisuppreme/ai-all-in-one-company/blob/main/custom-instructions/claude-code.md
2. Save it as `CLAUDE.md` in your project folder (or append it to an existing `CLAUDE.md`). Claude Code can clone this repository itself, so no bundle pasting is needed.

### Any other agent (ChatGPT, Gemini, Copilot, generic)

1. Copy this file: https://github.com/sisuppreme/ai-all-in-one-company/blob/main/custom-instructions/generic.md
2. Paste it into the tool's custom/system instructions.
3. If the agent can open links or clone repositories, just give it the repository home link above — the instructions file tells it the rest. If it cannot, paste `bundles/core.md` plus your playbook bundle as in the AI Studio steps.

## Repository map

| Path | What it holds |
|---|---|
| `BOOTSTRAP.md` | The start-here protocol every agent follows before doing anything else, including the 19-rank precedence order for when skills disagree |
| `SKILLS_INDEX.md` | Script-generated catalog of all 235 skills: department, keywords, dependencies, size, gates. Scan it; do not read it whole |
| `VERSION`, `CHANGELOG.md` | Current version (1.1.0) and its release record |
| `skills/` | The 18 department folders plus `skills/detection/` (the 203 detection parameters in 7 family files) |
| `bundles/` | Generated, token-capped loads: `core.md` (always-on, under 10,000 tokens), 20 department bundle files (18 departments; `seo-content` and `devops-deployment` each split across two files), 21 playbook bundles, `ALL_SKILLS.md` (reference only — never load it whole) |
| `playbooks/` | 21 project playbooks (13 by app type + 8 hybrid mission playbooks) — goal, department order, skills to load, gates by ID, failure handling, definition of done, worked mini-example |
| `gates/` | The gate registry: `ACCEPTANCE_GATES.md` (69 gates), `QA_PROTOCOL_GATES.md` (G-QA-01…10), `FINAL_ACCEPTANCE_CHECKLIST.md`, `DEFECT_TAXONOMY.md`, `NUMBERS_REGISTRY.md`, `VISUAL_QA_INDEX.md`, and the placeholder scan lists |
| `custom-instructions/` | Ready-to-paste entry points for Claude Code, Claude, Google AI Studio, and generic agents, plus a README explaining the set |
| `templates/` | `SKILL_TEMPLATE.md`, `USER_BRIEF.md`, `SECRETS_CHECKLIST.md`, the markdownlint starter config, and the 21 mandated per-project-type file manifests (the 13 original project types plus the 8 hybrid missions) |
| `scripts/` | The repo's own tooling: `build-index.py`, `build-bundles.py`, `validate-skills.py`, `generate-project.py`, the SEO checkers, and `scripts/qa/` reference implementations |
| `examples/` | One worked example document per department (18 files) |
| `docs/` | The records and references: `PROJECT_ANATOMY.md` (the full project map), `METRICS.md` (every number, defined), `DECISIONS.md` (every deviation, with reasons), `WORK_LOG.md` + `work-log/` (the build record), `TROUBLESHOOTING.md` (stuck + waiver protocols), `MAINTENANCE_RUNBOOK.md`, `GLOSSARY.md`, `BAR_TRACEABILITY.md`, `DEPARTMENT_LINKS.md`, `contracts/` (the 14 cross-department contracts), and the research/mapping papers |
| `CONTRIBUTING.md` | How changes are proposed and reviewed |

## The 18 departments

D1 Product & Requirements (14 skills) · D2 Architecture & System Design (14) · D3 Frontend, Design & Motion (16) · D4 Backend & APIs (16) · D5 Databases & Data (20) · D6 DevOps & Deployment (17) · D7 Security (14) · D8 QA & Testing (15) · D9 SEO & Content (15) · D10 Project & Memory (10) · D11 Integrations & Payments (12) · D12 Analytics & Observability (13) · D13 Accessibility & i18n (10) · D14 Legal & Privacy (10) · D15 Developer Experience (10) · D16 Cloning & Replication (9) · D17 AI Features (11) · D18 Customer Experience (9).

## Quality evidence

This repository was proof-tested before release, by fresh agents working only from the repo itself (full record: `docs/METRICS.md`, Phase 6; per-project detail: `docs/work-log/phase-6.md`):

- **Validation:** `scripts/validate-skills.py` over the full repo — **227 skills checked, ALL PASS**. All 34 bundles regenerated with **0 cap failures**.
- **Findability (§5.3 formal test):** a fresh agent given only `BOOTSTRAP.md` + `SKILLS_INDEX.md` picked the correct skill first on **10/10 tasks (bar: 9/10)**, spanning 7 departments.
- **Proof projects** — four complete builds, each gate-checked:
  - **P1 TaskBoard** (the single-agent proof, run under `custom-instructions/ai-studio.md`): a multi-tenant SaaS task manager with billing and English/Urdu-RTL internationalization — 43/52 gates passed (4 waived in tool form with substitute evidence, 4 blocked in the provisioning/Stripe-live class, 1 partial), **29/29 automated tests green**.
  - **P2 Atlas Blog**: 19/19 gates passed.
  - **P3 Ledger API**: 42/48 gates passed; the built service shipped with zero open defects.
  - **P4 ShopClone**: 49/56 gates passed (3 waived with recorded decisions).
  - Every defect the proofs surfaced in the repo itself was fixed or verified closed; no gate's pass criterion was weakened to get there. All four proofs were built and verified locally; live deployment depends on the operator's hosting provisioning.
- **Playbook dry runs:** the remaining 8 playbooks were each executed end-to-end by a lone agent — **all 13 playbooks covered**. Their 66 friction points were triaged into 28 root-cause clusters; all 22 open clusters were fixed.
- **Detection calibration:** the 39 visual parameters that text-only testing could not reach were screenshot-tested against professional sites — 4 false-positive parameters found, narrowed, and re-walked clean (6/6 checks clear).
- **Cross-review:** 94 of 227 skills were deep-read by independent reviewers before release — 0 blockers; all 6 majors and actionable minors fixed.
- **Slop and fake content:** 0 slop hits and 0 fake-content hits in the proofs that record them.

## Hard rules (summary)

- **Real Content Rule:** every fact, figure, name, and claim in any output must be real and sourced — never invent data, testimonials, statistics, or functionality.
- **Detection first:** the 203 detection parameters name what AI-generated work typically gets wrong; skills and gates are built to defeat them.
- **No silent skips:** gates pass on evidence, pass by a named fallback form, or are waived in writing — a waiver of a security, legal, or Real Content gate needs the operator's explicit agreement.
- **Docs before code, memory always:** project documents come first, and `progress.md` is updated as work proceeds.

## Licence

**MIT** — see the `LICENSE` file in this repository. Per `docs/DECISIONS.md` **D-004/D-019**, the MIT licence was applied when the repository was published public on GitHub (2026-11-21).

## Maintaining this repo

`SKILLS_INDEX.md` and `bundles/` are generated — never hand-edit them. After changing any skill, regenerate and validate:

```bash
python3 scripts/build-index.py
python3 scripts/build-bundles.py
python3 scripts/validate-skills.py
```

See `docs/MAINTENANCE_RUNBOOK.md` for the full maintenance procedure and `CONTRIBUTING.md` for how to propose changes.
