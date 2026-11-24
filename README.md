# OmniForge — ai-all-in-one

**A company in a repository.**

OmniForge packages the working knowledge of a complete web-application company — product, architecture, frontend, backend, data, DevOps, security, QA, SEO, legal, analytics, accessibility, integrations, AI features, and customer experience — as structured skills that **one AI agent** can load and execute end-to-end: research, build, verify, deploy, document, and hand over professional **web applications**, with real content only and every claim sourced.

- **Repository (public):** https://github.com/sisuppreme/ai-all-in-one-company
- **Created by:** MUHIUM — Founder of Mihora Tech
- **Licence:** MIT — see [`LICENSE`](LICENSE)
- **Custom-instructions pin:** **v1.4.0 (2026-11-24)** — the pin carried by all four files in [`custom-instructions/`](custom-instructions/)
- **Content verified on disk:** 2026-11-24 — `scripts/validate-skills.py`: **Checked 238 skills. ALL PASS**

> **Version note (read this first).** The `VERSION` file and `CHANGELOG.md` still record **v1.1.0** — no formal version bump has been recorded for the work landed after it. The content in this repository is newer than that file: the custom-instructions pin is v1.4.0 (2026-11-24), and every count in this README was verified against the files on disk on 2026-11-24. The "What's new" section below records what each step after v1.1.0 actually added, so nothing here depends on the stale `VERSION` file.

## Contents

- [What OmniForge is — and what it is not](#what-omniforge-is--and-what-it-is-not)
- [At a glance](#at-a-glance)
- [What's new](#whats-new)
- [Who it is for](#who-it-is-for)
- [Quick start — use it on your platform](#quick-start--use-it-on-your-platform)
- [How a project runs](#how-a-project-runs)
- [The 18 departments and all 238 skills](#the-18-departments-and-all-238-skills)
- [The premium design standard](#the-premium-design-standard)
- [Theme library — 100 original themes](#theme-library--100-original-themes)
- [UI/UX Upscaler — upgrade an existing app](#uiux-upscaler--upgrade-an-existing-app)
- [Playbooks — 22 guided missions](#playbooks--22-guided-missions)
- [Bundles — token-capped loads](#bundles--token-capped-loads)
- [Gates and detection](#gates-and-detection)
- [Quality evidence — how it was proof-tested](#quality-evidence--how-it-was-proof-tested)
- [Repository map](#repository-map)
- [Maintaining this repo](#maintaining-this-repo)
- [FAQ](#faq)
- [Licence and credits](#licence-and-credits)

## What OmniForge is — and what it is not

| OmniForge is | OmniForge is not |
|---|---|
| A skill repository: 238 skills in a fixed, memory-proof format, one per capability | A framework, a library, or a starter template you install into your app |
| A complete company workflow: requirements → architecture → build → security → QA → deployment → handover | A code generator that writes an app from one prompt with no checks |
| Gate-driven: every step is checked against named gates, with evidence recorded in `progress.md` | A vibes-based checklist — a gate claimed passed without evidence is not passed |
| Real-content only: every fact, figure, name, and claim in any output must be real and sourced | A demo-content machine — no invented testimonials, statistics, or functionality, ever |
| Designed and proof-tested for **one AI agent working alone** — no sub-agents, no leads, no hand-offs | A multi-agent orchestration system |
| Web applications, end to end (Phase 1 scope) | Mobile apps or desktop apps — those are a later phase and are not covered by the current playbooks |

Every skill follows one memory-proof format:

- **Numbered rules with stable IDs** (e.g. `FE-369`, `G-FE-186`, `BAN-FE-191`)
- **A BAN list** — each banned pattern names the detection parameter it defeats and gives the correct replacement
- **Gates with evidence requirements** — at least 3 gates inside every skill
- **Anti-patterns, worked examples, recall anchors, and a checklist**

## At a glance

| Component | Count | Where |
|---|---|---|
| Skills | **238** | `skills/<department>/<skill>/SKILL.md` |
| Departments | **18** (D1–D18) | `skills/` |
| Detection parameters | **203** across 7 families (visual, code, infra, content, UX, fake, crawl) | `skills/detection/` |
| Playbooks | **22** — 13 by app type + 8 hybrid missions + 1 UI/UX upscaler | `playbooks/` |
| Bundles | **45 files** — always-on core, 21 department bundle files, 22 playbook bundles, plus reference-only `ALL_SKILLS.md` | `bundles/` |
| Gates | **69** acceptance gates + **10**-gate skill-release QA protocol (G-QA-01…10), plus at least 3 gates inside every skill | `gates/`, `skills/` |
| Worked examples | **715** before/after example files (3 per skill; `vector-db` carries a fourth) + 18 department example documents | `skills/*/examples/`, `examples/` |
| Premium themes | **100** fully expanded theme specifications | `skills/frontend/theme-library/expanded/` |
| Cross-department contracts | **14** | `docs/contracts/` |
| Tracked files in the repo | **1,290** | whole repository |
| Validation (2026-11-24) | **Checked 238 skills. ALL PASS** | `scripts/validate-skills.py` |

## What's new

### v1.4.0 — 2026-11-24 — hard leak gate + repo-use enforcement (custom-instructions pin)

- **Architecture-Leak Rule — hard gate, fail-closed.** An application's structure must never leak into its UI: no DB names/types, table/collection names, page/route counts or structures, API endpoints, internal module/service names, tech-stack labels, or schema/field names on any user-facing surface. Any leak in the shipped UI is a gate FAIL, whatever the design score is. Target leak score: **zero**.
- **Repo-Use Enforcement (FE-381–FE-384, G-FE-191, BAN-FE-191).** The agent must read the named skill files from the repo *before* generating anything, stop (fail-closed) if a required skill cannot be read, and carry an attestation block in `progress.md` and in its reply — repo version, skills read, and every rule applied with its exact `file:line` evidence. A UI task's attestation must also name the theme and its canonical expanded spec, the design-intelligence gate score, and the AFTER leak score.
- **UI/UX Upscaler skill embedded in all 4 platform files**, so the leak gate cites a skill the instruction file actually contains.

### v1.3.0 — 2026-11-23 — Existing-Project Upgrade Protocol

- A staged upgrade protocol added to all 4 platform files: audit first, staged passes, score gate (design-intelligence gate, AFTER score ≥ 64/80, every audit defect fixed or explicitly reported).

### The 100-theme premium library — 2026-11-23

- **`design-intelligence` skill** (new): art-direction decision systems, self-critique quality gates, anti-slop symptom → cause → fix detection, adaptation by brand/audience/content type, worked reasoning examples.
- **`theme-library` skill**: **100 completely original premium themes**, each expanded to the full 50x standard — per-element build specs, choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens, worked examples, scroll choreography map, performance budget, build order.
- **Premium rewrites of `motion` and `scroll-experiences`**: the old skills were written almost entirely as bans/restraint — they stopped bad motion but contained no positive premium-craft standard. They now carry the positive standard too.

### v1.1.0 — 2026-11-21 — Phase 8 hybrid expansion

- **8 new skills** for work that is not "build new" (227 → 235): `clone-redesign` and `rebrand-execution` (D16), `project-takeover` and `prototype-hardening` (D15), `seo-migration` (D9), `ai-retrofit` (D17), `market-expansion` (D1), `saas-conversion` (D2).
- **8 new hybrid playbooks** (13 → 21), one per hybrid mission.
- One rule-ID collision between the two new D15 skills, found during integration and fixed by renumbering `project-takeover` into its own free ID block.

### v1.0.0 — 2026-11-21 — first public release

- 18 departments (D1–D18), 227 skills in the memory-proof format, 203 detection parameters, 13 project playbooks, 69 acceptance gates + G-QA-01…10, ready-to-paste custom instructions for 4 platforms, `BOOTSTRAP.md` repo-first protocol, script-generated `SKILLS_INDEX.md`.
- Published public on GitHub under MIT (2026-11-21) — decisions D-004/D-019 in `docs/DECISIONS.md`.

## Who it is for

- **A single AI agent working alone.** The repository is designed and proof-tested for one agent with no sub-agents, no leads, and no hand-offs. Everything the agent needs — routing, precedence when skills disagree, what to do when stuck, when to ask the operator — is written down in the repo itself.
- **Its operator.** The person who commissions projects, answers the three approval points (requirements, deploy target and cost, go-live), supplies secrets through the handoff checklist, and gives the final ship approval. Operators should read [`USER_GUIDE.md`](USER_GUIDE.md) — it walks the whole route in plain language, including a Roman Urdu quick-start.
- **Contributors.** See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [Maintaining this repo](#maintaining-this-repo). `SKILLS_INDEX.md` and `bundles/` are generated — never hand-edit them.

Phase 1 scope is **web applications**. Mobile and desktop applications are a later phase and are not covered by the current playbooks.

## Quick start — use it on your platform

Repository home: https://github.com/sisuppreme/ai-all-in-one-company

Every platform starts the same way: **one** custom-instructions file from [`custom-instructions/`](custom-instructions/), pasted into the platform's instructions box. Then, if the agent cannot open GitHub itself, paste [`bundles/core.md`](bundles/core.md) plus the one playbook bundle that matches your project (all bundles: https://github.com/sisuppreme/ai-all-in-one-company/tree/main/bundles). Never paste `bundles/ALL_SKILLS.md` — it is a human reference only.

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

### Clone it

```bash
git clone https://github.com/sisuppreme/ai-all-in-one-company.git
cd ai-all-in-one-company
```

### Also available on Agensi

The skills are also listed as 5 free packs on Agensi (the platform caps a pack at 50 skills, so the library is split, not cut):

| Pack | Covers | Link |
|---|---|---|
| Pack 1 | Product, Architecture, Backend | https://www.agensi.io/skills/omniforge-pack-1-product-architecture-backend |
| Pack 2 | Frontend, UX, Accessibility, Cloning | https://www.agensi.io/skills/omniforge-pack-2-frontend-ux-accessibility-cloning |
| Pack 3 | Database, AI, DevOps | Submitted — pending review (as of 2026-11-22) |
| Pack 4 | QA, Security, Legal, DX | Submitted — pending review (as of 2026-11-22) |
| Pack 5 | SEO, Analytics, Payments, Memory | Submitted — pending review (as of 2026-11-22) |

The GitHub repository is the complete, canonical package — always use it first.

## How a project runs

### 1. Bootstrap — repo first, always

The agent follows [`BOOTSTRAP.md`](BOOTSTRAP.md) before doing anything else:

1. Read `VERSION` and the top `CHANGELOG.md` entry; note each loaded skill's last-verified date.
2. Read `BOOTSTRAP.md` in full.
3. Scan [`SKILLS_INDEX.md`](SKILLS_INDEX.md) by department and keywords to route the task — do not read every entry.
4. Load in stages — Stage 1: `bundles/core.md` (always-on core). Stage 2: the playbook bundle for the project type. Stage 3: individual skills in full, only where a step needs what a bundle omits.
5. Create the project documents **before any code**: `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md` — plus the full file set from the project type's manifest.
6. Follow the loaded skills' gates at every step, recording a written pass/fail per criterion in `progress.md`, with evidence (command output, test result, or screenshot).
7. Update `progress.md` as work proceeds.

**Small-task fast path:** a single-file fix or one-skill task loads just that skill and its gates instead of the full bootstrap.

### 2. Docs before code, memory always

- Project documents come first; no code before docs.
- `progress.md` is the live record — repo version, per-gate pass/fail with evidence, blockers, substitutions. If you want to know where a project stands, ask the agent to show you `progress.md`.
- Facts are checked against `fact-sheet.md`. Every figure, name, and claim in the product must trace to a real source recorded there.

### 3. Your three approval points

The agent must stop for your approval at exactly three points:

| # | Approval point | When |
|---|---|---|
| 1 | `requirements.md` + the estimate | After requirements are written |
| 2 | Deploy target + cost | Before deployment — agree a monthly cost cap upfront; the agent must get approval before provisioning anything above the estimate |
| 3 | The live switch | Before go-live |

A decision already recorded in the commissioning brief or in `requirements.md` counts as the approval for its point — the agent does not re-ask what the brief already answers.

### 4. Gates — three lawful outcomes, no silent skips

Every step's gates are checked with evidence recorded in `progress.md`. A gate has exactly three lawful outcomes:

- **Pass** — on evidence.
- **Pass by its manual/substitute-evidence form** — where the gate defines one.
- **Recorded waiver** — in writing, with its unblocking conditions. A waiver of a security, legal, or Real Content gate needs the operator's explicit agreement.

Never a silent skip. A gate pass must cite evidence; a gate passed without evidence is not passed.

### 5. Precedence — when two skills disagree

Higher rank wins; every conflict is logged in the project's `DECISIONS.md`. The full 19-rank order is in `BOOTSTRAP.md`; the top ranks are:

1. Security (D7), including D17 AI-safety rules
2. Legal / privacy (D14), including D16 clone-ethics
3. Real Content Rule — no fakes, ever
4. QA gates (D8, process gates only)
5. … (remaining ranks in `BOOTSTRAP.md`)

### 6. If the agent gets stuck

It follows the stuck protocol in [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) — skill → links → log → user → safe default — instead of inventing a way out. Where no user is reachable (an unattended run), it logs and continues on the safe defaults, and records the substitution in `progress.md`.

### 7. Repo-use enforcement (v1.4.0)

- **Read before generating (FE-381).** Before generating anything, read the named skill files from the repo, fetched fresh. Record the read list in `progress.md` before any output exists — one line per skill file, with its repo path and the repo version it was read from.
- **Fail-closed (FE-382).** If a required skill file cannot be fetched or read, stop that scope and tell the user exactly which file and why. Never proceed on model defaults. For UI/UX work there is no pasted-bundle substitute: if the UI/UX skill files cannot be read from the repo, UI work stops.
- **Attestation (FE-383).** Every output carries an attestation block in `progress.md` and in the reply: repo version used, skills read before generating, and rules applied with exact `file:line` evidence. A rule listed without a `file:line` is not applied. If there is no attestation, the repo was not used — treat the work as undone.
- **Compulsory UI/UX set (FE-384).** For any task that creates or changes a UI, the attestation must include the theme chosen and its canonical expanded spec path, the design-intelligence quality-gate score, and the AFTER leak score. The only exception is the user's explicit instruction not to use these skills.

## The 18 departments and all 238 skills

| Dept | Department | Skills | Folder |
|---|---|---|---|
| D1 | Product & Requirements | 14 | `skills/product-requirements/` |
| D2 | Architecture & System Design | 14 | `skills/architecture/` |
| D3 | Frontend, Design & Motion | 19 | `skills/frontend/` |
| D4 | Backend & APIs | 16 | `skills/backend/` |
| D5 | Databases & Data | 20 | `skills/database/` |
| D6 | DevOps & Deployment | 17 | `skills/devops-deployment/` |
| D7 | Security | 14 | `skills/security/` |
| D8 | QA & Testing | 15 | `skills/qa-testing/` |
| D9 | SEO & Content | 15 | `skills/seo-content/` |
| D10 | Project & Memory | 10 | `skills/project-memory/` |
| D11 | Integrations & Payments | 12 | `skills/integrations-payments/` |
| D12 | Analytics & Observability | 13 | `skills/analytics-observability/` |
| D13 | Accessibility & i18n | 10 | `skills/accessibility-i18n/` |
| D14 | Legal & Privacy | 10 | `skills/legal-privacy/` |
| D15 | Developer Experience | 10 | `skills/developer-experience/` |
| D16 | Cloning & Replication | 9 | `skills/cloning-replication/` |
| D17 | AI Features | 11 | `skills/ai-features/` |
| D18 | Customer Experience | 9 | `skills/customer-experience/` |

### D1 — Product & Requirements (14)

`acceptance-criteria` · `competitive-analysis` · `discovery` · `fact-sheet` · `market-expansion` · `personas-jtbd` · `pricing-monetization` · `product-metrics` · `requirements-writing` · `roadmapping` · `scope-control` · `unit-economics` · `user-research` · `user-stories`

### D2 — Architecture & System Design (14)

`adr-writing` · `api-architecture` · `api-documentation` · `api-paradigms` · `api-versioning` · `architecture-patterns` · `c4-diagrams` · `data-architecture` · `domain-driven-design` · `event-driven` · `multitenancy-saas` · `saas-conversion` · `stack-selection` · `system-design`

### D3 — Frontend, Design & Motion (19)

`client-routing` · `component-library` · `data-fetching` · `data-visualisation` · `design-intelligence` · `design-system` · `design-tokens` · `forms` · `frontend-core` · `frontend-state` · `layout-responsive` · `motion` · `pwa-offline` · `scroll-experiences` · `theme-library` · `typography` · `ui-states` · `ui-ux-upscaler` · `webgl-3d`

### D4 — Backend & APIs (16)

`admin-tools` · `api-building` · `backend-auth` · `error-handling` · `feature-flags` · `file-uploads` · `media-processing` · `notifications` · `queues-jobs` · `rate-limiting` · `rbac` · `realtime` · `rest-conventions` · `sdk-design` · `user-reporting` · `validation`

### D5 — Databases & Data (20)

`backup-recovery` · `caching` · `data-access` · `data-ingestion` · `data-quality` · `data-warehousing` · `etl-pipelines` · `indexing` · `migrations` · `nosql-patterns` · `pipeline-orchestration` · `query-performance` · `read-replicas` · `schema-design` · `search-engines` · `seed-data` · `sql-fundamentals` · `tenant-isolation` · `transactions-concurrency` · `vector-db`

### D6 — DevOps & Deployment (17)

`cdn-strategy` · `ci-cd` · `cloud-costs` · `containers` · `deployment-strategies` · `domains-dns` · `free-tiers` · `hosting` · `incident-response` · `infrastructure-as-code` · `kubernetes` · `preview-environments` · `reliability` · `rollback` · `scaling` · `servers-vps` · `ssl-certificates`

### D7 — Security (14)

`api-security` · `auth-hardening` · `content-moderation` · `dependency-safety` · `encryption` · `owasp` · `pci-compliance` · `penetration-testing` · `secrets-management` · `security-audit` · `security-headers` · `session-security` · `supply-chain` · `threat-modelling`

### D8 — QA & Testing (15)

`accessibility-testing` · `browser-verification` · `bug-triage` · `chaos-testing` · `contract-testing` · `e2e-testing` · `integration-testing` · `load-testing` · `placeholder-scan` · `qa-gates` · `security-testing` · `test-data` · `test-strategy` · `unit-testing` · `visual-regression`

### D9 — SEO & Content (15)

`aeo` · `content-strategy` · `copywriting` · `geo` · `growth-experiments` · `internal-linking` · `lifecycle-email` · `on-page-seo` · `real-content` · `seo-migration` · `sitemaps` · `social-open-graph` · `structured-data` · `technical-seo` · `web-analytics`

### D10 — Project & Memory (10)

`changelog` · `decision-logs` · `documentation-writing` · `handover` · `memory-retrieval` · `postmortem-writing` · `progress-tracking` · `project-templates` · `readme-writing` · `runbook-writing`

### D11 — Integrations & Payments (12)

`api-keys-management` · `dunning` · `invoicing-tax` · `oauth-sso` · `payments` · `refunds-disputes` · `sdk-embeddables` · `sms` · `subscriptions` · `third-party-apis` · `transactional-email` · `webhooks`

### D12 — Analytics & Observability (13)

`alerting` · `apm` · `core-web-vitals` · `dashboards` · `error-tracking` · `event-tracking` · `experimentation-platform` · `logging` · `monitoring` · `performance-budgets` · `performance-optimization` · `product-analytics` · `revenue-analytics`

### D13 — Accessibility & i18n (10)

`accessibility-audit` · `accessibility-law` · `inclusive-copy` · `internationalization` · `keyboard-accessibility` · `localization-workflow` · `reduced-motion` · `rtl-layouts` · `screen-readers` · `wcag`

### D14 — Legal & Privacy (10)

`age-requirements` · `audit-trails` · `clone-ethics` · `compliance-audit` · `cookie-consent` · `data-residency` · `dsar-handling` · `legal-documents` · `licensing` · `privacy-laws`

### D15 — Developer Experience (10)

`code-generation` · `dependency-management` · `dev-environment` · `legacy-migration` · `monorepo-tooling` · `project-takeover` · `prototype-hardening` · `refactoring` · `tech-debt` · `versioning`

### D16 — Cloning & Replication (9)

`asset-harvesting` · `behavior-cloning` · `clone-redesign` · `design-extraction` · `fidelity-verification` · `page-inventory` · `page-reconstruction` · `rebrand-execution` · `site-discovery`

### D17 — AI Features (11)

`ai-cost-control` · `ai-evaluation` · `ai-observability` · `ai-retrofit` · `ai-safety` · `embeddings-search` · `llm-integration` · `prompt-engineering` · `rag-retrieval` · `recommendations` · `search-relevance`

### D18 — Customer Experience (9)

`activation-metrics` · `churn-prevention` · `feedback-loops` · `help-center` · `in-app-chat` · `status-communications` · `support-ticketing` · `trial-conversion` · `user-onboarding`

### Detection parameters — the 203 tells (not skills)

The detection parameters live in [`skills/detection/`](skills/detection/) (7 family folders: `visual`, `code`, `infra`, `content`, `ux`, `fake`, `crawl`). They name what AI-generated work typically gets wrong; skills and gates are built to defeat them. Each parameter carries signal, AI-typical vs. professional form, check, false positives, severity, source, and fix. They are indexed inside their own `PARAMETERS.md` files, not in `SKILLS_INDEX.md`.

## The premium design standard

A site built with OmniForge must be unmatched — never "AI slop". The standard is enforced by the compulsory UI/UX skill set, not left to taste:

- **Compulsory UI/UX skills (always applied to any UI work, unless the user explicitly says not to):** `design-intelligence`, `design-system`, `design-tokens`, `typography`, `layout-responsive`, `component-library`, `ui-states`, `motion`, `scroll-experiences` — plus `webgl-3d` when the chosen theme calls for it, and `ui-ux-upscaler` whenever the task upgrades an already-built application's UI.
- **Full motion system on every page, in the theme's own style — never copy-paste.** Every theme carries its own motion system that practically uses, heavily, the full motion vocabulary: scroll-triggered reveals, scroll-driven / scrub animation, parallax, pinned sections, smooth scrolling, progress indicator, staggered + masked reveals, kinetic typography, marquee, counters, SVG line-draw, image scale-in-frame, hover / magnetic / tilt micro-interactions, custom cursor, skeleton loading, page transitions, and reduced-motion support.
- **5–20 signature animated elements per theme**, specially designed for that theme and **merged with the site's content** — never pasted on top of it. A built element (a jar, a train, an instrument, any themed object) must be integrated with the content it serves; if it looks like a pointless add-on, it is a defect. 3D where possible, otherwise excellently animated.
- **Feather-light cursor, or none.** Heavy custom cursors are banned. If a custom cursor makes the pointer hard to move, it is a defect, not premium. Normal system cursor by default; performance first.
- **Reveals can never leave content invisible.** Every reveal needs a fallback, and the page stays readable with JavaScript disabled.
- **Scroll-driven motion is smoothed** (requestAnimationFrame lerp, no jitter). `prefers-reduced-motion` is honoured.
- **Design-intelligence quality gate:** before any UI work is called done, run the `design-intelligence` quality gate and record its result in `progress.md` with the other gates. The AFTER score must reach the gate's pass mark (**≥ 64/80**) and every defect in the audit list must be fixed — or explicitly reported, with a reason, in the audit file.
- **"Most premium" standard:** when it feels like premium has reached its end, push more premium beyond that point. Quality never drops when quantity rises.
- **Architecture must never leak into the UI** — see the leak gate below.

### Architecture-Leak Rule — hard gate, fail-closed (v1.4.0)

The UI agent uses all of the project's skills to understand the app but surfaces **none** of their internals in the UI. The test: show any UI surface to a non-technical user. If they need to know how the app is built to understand it, it leaks. If a sentence would still make sense after replacing the entire stack (Postgres → SQLite, REST → GraphQL, React → Vue), it does not leak.

| Ban | Banned from all user-facing surfaces |
|---|---|
| B-1 | DB names / types — "PostgreSQL", "MongoDB", "SQLite", versions |
| B-2 | Table / collection names — "`bookings`", "`users`", "rows", "records" as a storage term |
| B-3 | Page / route counts or structures — "12 pages", "4 modules", sitemap-style counts |
| B-4 | API endpoints — "/v2/bookings", "/api/users/42", any URL path naming a resource operation |
| B-5 | Internal module / service names — "Billing Service", "Auth Module", "Sync Worker" |
| B-6 | Tech-stack labels — "React", "Next.js", "Node", "AWS", "Powered by X" badges naming infrastructure (payment-provider exception: a provider may be named only on the payment step itself, as a trust mark) |
| B-7 | Schema / field names — "`users.email`", "`bookings.guest_id`", camelCase/snake_case identifiers, "NOT NULL", "FK violation" |
| B-8 | Status codes / technical error identifiers — "404", "422", "500", trace IDs, "Error: Cannot read properties of undefined" (an opaque support reference like "ABC-123" is allowed) |

"User-facing surface" means every pixel the user can see or hear: copy, labels, headings, placeholders, helper text, tooltips, aria-labels, `title` attributes, error/empty/loading strings, URLs shown in the UI, page titles, notification text, email subjects the app sends, PDF/invoice text, and anything rendered by an error boundary or a framework default. "Only developers will see it" is not a defence. A leak in an error message is still a leak; a leak only admins see is still a leak.

- **The gate (FE-371, G-FE-186) is a veto: any leak in the shipped UI = gate FAIL, whatever the /80 score is.** A 72/80 app with 1 leak does not ship. The leak score stands beside the /80 total as its own line — never folded into it.
- **Fix by translating, never by deleting the meaning (FE-370):** "No rows in `orders_collection`" → "No orders yet — create your first order"; "Failed to fetch /api/v2/invoices" → "Couldn't load your invoices — check your connection and try again". Cosmetic renaming ("`orders_collection`" → "Orders Collection") is still a leak: the check is meaning, not spelling.
- **Detection:** copy scan (ban-list grep over every user-facing string); error-path walkthrough (every error path triggered and its string read); the non-technical-user test on 5 surfaces.
- Full taxonomy, translation table, and worked fixes: `skills/frontend/ui-ux-upscaler/SKILL.md` §6 and `skills/frontend/ui-ux-upscaler/specs/09-architecture-leak.md`; design-intelligence §5 leak audit.

## Theme library — 100 original themes

The library holds **100 themes**, each specified exactly once, in full, in [`skills/frontend/theme-library/expanded/`](skills/frontend/theme-library/expanded/) (canonical source: `expanded/theme-NNN.md`, zero-padded). The four range files (`themes-001-025.md`, `themes-026-050.md`, `themes-051-075.md`, `themes-076-100.md`) are indexes only. [`EXPANSION-STANDARD.md`](skills/frontend/theme-library/EXPANSION-STANDARD.md) is the depth standard every expanded spec was written and verified against. Each theme is a completely original design — not a variation of an existing template — with its own full motion system and 5–20 signature animated elements merged into its content.

| # | Theme | # | Theme |
|---|---|---|---|
| 001 | The Midnight Press Run | 051 | Quarry Cut |
| 002 | Marginalia | 052 | Fog Harvest |
| 003 | Redacted Archive | 053 | Moon Garden |
| 004 | Letterpress Atelier | 054 | Beeswax & Comb |
| 005 | The Colophon | 055 | River Stone |
| 006 | Palimpsest | 056 | Frost Fern |
| 007 | The Proofreader's Desk | 057 | Ochre & Pigment |
| 008 | The Index Card Library | 058 | Storm Glass |
| 009 | The Sunday Supplement | 059 | Linen Field |
| 010 | Risograph Confessional | 060 | Meteorite Iron |
| 011 | The Telegraph Wire | 061 | The Flight Director's Ledger |
| 012 | Microfilm Reader | 062 | Celestial Navigation Atelier |
| 013 | The Shipping Forecast | 063 | Sonar Room |
| 014 | Broadside & Ballad | 064 | The Cyanotype Vault |
| 015 | The Corrections Column | 065 | Waveform Observatory |
| 016 | Vellum & Wax | 066 | The Data Cartographer's Atlas |
| 017 | The Classifieds | 067 | Calibre & Escapement |
| 018 | Manicule & Catchword | 068 | Cryo Lab Monograph |
| 019 | The Linotype Line | 069 | The 1962 Space Clipper Brochure |
| 020 | Halftone Confessions | 070 | Telemetry Tape |
| 021 | The Almanack | 071 | The Bioluminescent Census |
| 022 | Dust Jacket | 072 | Solar Weather Almanac |
| 023 | The Printer's Devil | 073 | The Instrument Maker's Bench |
| 024 | Tabloid Confessional | 074 | Lagrange Post |
| 025 | The Obituaries Page | 075 | Seismograph Diary |
| 026 | Movable Type Chaos | 076 | Ice Core Archive |
| 027 | The Society Pages | 077 | The Listening Dish |
| 028 | Errata Slip | 078 | Trajectory Tables |
| 029 | The Weather Map | 079 | Vent Field Survey |
| 030 | First Edition | 080 | The Ephemeris Press |
| 031 | Basalt Cathedral | 081 | Dead Reckoning |
| 032 | Tidal Ledger | 082 | Containment Log: Tokamak Shift B |
| 033 | Silk Unspooling | 083 | The Tide Engine |
| 034 | Kiln Opening | 084 | The Tube Weather Bureau |
| 035 | Dune Cartography | 085 | Transit Photometry |
| 036 | Monsoon Arrival | 086 | The Drift Buoy Network |
| 037 | Glacier Confession | 087 | Calibration Standard No. 9 |
| 038 | Paper Mulberry | 088 | Subglacial Dispatch |
| 039 | Verdigris | 089 | Custodian of the Orbit |
| 040 | Loam & Strata | 090 | Cymatics Garden |
| 041 | Kintsugi | 091 | The Projectionist's Booth |
| 042 | Salt Mirror | 092 | Museum After Dark |
| 043 | Forest Floor, Magnified | 093 | Marginalia |
| 044 | Hammam | 094 | The Long Exposure |
| 045 | Indigo Vat | 095 | The Cartographer's Table |
| 046 | Amber Hour | 096 | From the Wings |
| 047 | Fjord Stillness | 097 | Reel to Reel |
| 048 | Sun-Fired Clay | 098 | Tales by the Hearth |
| 049 | Pearl Diver's Breath | 099 | The Grand Tour Ledger |
| 050 | Charcoal & Ink | 100 | The Velvet Note |

## UI/UX Upscaler — upgrade an existing app

New builds are only half the story. The **`ui-ux-upscaler` skill** (`skills/frontend/ui-ux-upscaler/`, web apps only for now) takes an existing application's existing UI and upscales it to the same premium standard — full motion system on every page, 5–20 signature animated elements merged into content, feather-light cursor, original premium design, quality never dropping. It is the full skill form of the v1.3.0 Existing-Project Upgrade Protocol, with its own playbook ([`playbooks/ui-ux-upscaler.md`](playbooks/ui-ux-upscaler.md)) and bundle ([`bundles/ui-ux-upscaler.md`](bundles/ui-ux-upscaler.md)).

| Spec | What it covers |
|---|---|
| `01-audit-and-scoring.md` | Audit first — score the existing UI before touching it |
| `02-theme-decision.md` | Choosing the theme for the existing app |
| `03-staged-passes.md` | Staged upgrade passes, in order |
| `04-component-upgrades.md` | Component-by-component upgrades |
| `05-motion-system.md` | Installing the theme's full motion system |
| `06-signature-elements.md` | The 5–20 signature animated elements, merged into content |
| `07-frameworks.md` | Framework-specific upgrade notes |
| `08-case-studies.md` | Worked upgrade case studies |
| `09-architecture-leak.md` | The leak ban list B-1–B-8, detection, checklist, translation pairs |
| `10-regression-rollback.md` | Regression checks and rollback |
| `11-scoring-shipping.md` | Final scoring and the ship gate |

Key rules: audit before generating (FE-361); the AFTER score must reach ≥ 64/80 with every audit defect fixed or explicitly reported; the AFTER leak score must be zero (G-FE-186) — any leak is a gate FAIL whatever the /80 score is; stop, fix, re-check, never ship with a known leak "to fix later".

## Playbooks — 22 guided missions

Each playbook states its goal, department order, skills to load, gates by ID, failure handling, definition of done, and a worked mini-example.

### 13 playbooks by app type

| Playbook | Build |
|---|---|
| `saas-web-app` | SaaS web app |
| `content-blog-site` | Content / blog site |
| `api-database-service` | API + database service |
| `e-commerce-store` | E-commerce store |
| `clone-rebuild` | Clone rebuild |
| `dashboard-admin-panel` | Dashboard / admin panel |
| `booking-scheduling` | Booking & scheduling |
| `online-learning-lms` | Online learning (LMS) |
| `landing-page` | Landing page |
| `portfolio-marketing-site` | Portfolio / marketing site |
| `internal-crud-admin-tool` | Internal CRUD admin tool |
| `two-sided-marketplace` | Two-sided marketplace |
| `realtime-chat-app` | Realtime chat app |

### 8 hybrid playbooks (v1.1.0) — work that starts from something that already exists

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

### 1 upscaler playbook

| Playbook | Mission |
|---|---|
| `ui-ux-upscaler` | Upgrade an existing application's UI to the full premium standard — audit, staged passes, leak gate, score gate |

## Bundles — token-capped loads

Bundles are generated, token-capped loads — never hand-edit them. `core.md` is always on (under 10,000 tokens). Department bundles carry the full rules/gates/bans; longer examples point to the source skills.

| Bundle group | Files | Notes |
|---|---|---|
| Always-on core | `core.md` | Load first, every project |
| Department bundles | 21 files covering 18 departments | `seo-content`, `devops-deployment`, and `frontend` are each split across two files |
| Playbook bundles | 22 files, one per playbook | The default complete load for a playbook walk |
| Reference only | `ALL_SKILLS.md` | Human reference / offline search only — **never load it whole** |

## Gates and detection

- **Acceptance gates:** 69 inherited gates in [`gates/ACCEPTANCE_GATES.md`](gates/ACCEPTANCE_GATES.md), plus the 10-gate skill-release QA protocol ([`gates/QA_PROTOCOL_GATES.md`](gates/QA_PROTOCOL_GATES.md), G-QA-01…10), plus at least 3 gates inside every skill.
- **Gate registry:** [`gates/`](gates/) also holds `FINAL_ACCEPTANCE_CHECKLIST.md`, `DEFECT_TAXONOMY.md`, `NUMBERS_REGISTRY.md`, `VISUAL_QA_INDEX.md`, and the placeholder scan lists.
- **Detection first:** the 203 detection parameters name what AI-generated work typically gets wrong; skills and gates are built to defeat them.
- **Hard rules (summary):**
  - **Real Content Rule:** every fact, figure, name, and claim in any output must be real and sourced — never invent data, testimonials, statistics, or functionality.
  - **Detection first:** see above.
  - **No silent skips:** gates pass on evidence, pass by a named fallback form, or are waived in writing.
  - **Docs before code, memory always:** project documents come first, and `progress.md` is updated as work proceeds.
  - **Architecture never leaks into the UI** (v1.4.0 hard gate — see above).

## Quality evidence — how it was proof-tested

This repository was proof-tested before release, by fresh agents working only from the repo itself (full record: [`docs/METRICS.md`](docs/METRICS.md), Phase 6; per-project detail: `docs/work-log/phase-6.md`):

- **Validation:** `scripts/validate-skills.py` over the full repo — **238 skills checked, ALL PASS** (re-run 2026-11-24; the v1.0.0 record was 227/227, the v1.1.0 record 235/235). All bundles regenerated with **0 cap failures**.
- **Findability (§5.3 formal test):** a fresh agent given only `BOOTSTRAP.md` + `SKILLS_INDEX.md` picked the correct skill first on **10/10 tasks (bar: 9/10)**, spanning 7 departments.
- **Proof projects** — four complete builds, each gate-checked:
  - **P1 TaskBoard** (the single-agent proof, run under `custom-instructions/ai-studio.md`): a multi-tenant SaaS task manager with billing and English/Urdu-RTL internationalization — 43/52 gates passed (4 waived in tool form with substitute evidence, 4 blocked in the provisioning/Stripe-live class, 1 partial), **29/29 automated tests green**.
  - **P2 Atlas Blog**: 19/19 gates passed.
  - **P3 Ledger API**: 42/48 gates passed; the built service shipped with zero open defects.
  - **P4 ShopClone**: 49/56 gates passed (3 waived with recorded decisions).
  - Every defect the proofs surfaced in the repo itself was fixed or verified closed; no gate's pass criterion was weakened to get there. All four proofs were built and verified locally; live deployment depends on the operator's hosting provisioning.
- **Playbook dry runs:** the remaining playbooks were each executed end-to-end by a lone agent — **all 13 playbooks covered**. Their 66 friction points were triaged into 28 root-cause clusters; all 22 open clusters were fixed.
- **Detection calibration:** the 39 visual parameters that text-only testing could not reach were screenshot-tested against professional sites — 4 false-positive parameters found, narrowed, and re-walked clean (6/6 checks clear).
- **Cross-review:** 94 of 227 skills were deep-read by independent reviewers before release — 0 blockers; all 6 majors and actionable minors fixed.
- **Slop and fake content:** 0 slop hits and 0 fake-content hits in the proofs that record them.
- **Phase 8 quality process (D-020):** 30 builders, 10 cross-assigned debaters, a 5-member review board, and a 4-member final committee, with structured handoffs and a coordinator verification layer between tiers. The debaters fixed 44 flaws; the board signed off 5/5.

## Repository map

| Path | What it holds |
|---|---|
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | The start-here protocol every agent follows before doing anything else, including the 19-rank precedence order for when skills disagree |
| [`SKILLS_INDEX.md`](SKILLS_INDEX.md) | Script-generated catalog of all 238 skills: department, keywords, dependencies, size, gates. Scan it; do not read it whole |
| `VERSION`, [`CHANGELOG.md`](CHANGELOG.md) | Version file (still records 1.1.0 — see the version note at the top) and its release record |
| [`skills/`](skills/) | The 18 department folders plus `skills/detection/` (the 203 detection parameters in 7 family files) |
| [`bundles/`](bundles/) | Generated, token-capped loads: `core.md` (always-on, under 10,000 tokens), 21 department bundle files, 22 playbook bundles, `ALL_SKILLS.md` (reference only — never load it whole) |
| [`playbooks/`](playbooks/) | 22 project playbooks (13 by app type + 8 hybrid mission playbooks + 1 UI/UX upscaler playbook) — goal, department order, skills to load, gates by ID, failure handling, definition of done, worked mini-example |
| [`gates/`](gates/) | The gate registry: `ACCEPTANCE_GATES.md` (69 gates), `QA_PROTOCOL_GATES.md` (G-QA-01…10), `FINAL_ACCEPTANCE_CHECKLIST.md`, `DEFECT_TAXONOMY.md`, `NUMBERS_REGISTRY.md`, `VISUAL_QA_INDEX.md`, and the placeholder scan lists |
| [`custom-instructions/`](custom-instructions/) | Ready-to-paste entry points for Claude Code, Claude, Google AI Studio, and generic agents, plus a README explaining the set — pin v1.4.0 (2026-11-24) |
| [`templates/`](templates/) | `SKILL_TEMPLATE.md`, `USER_BRIEF.md`, `SECRETS_CHECKLIST.md`, the markdownlint starter config, and the 21 mandated per-project-type file manifests (the 13 original project types plus the 8 hybrid missions) |
| [`scripts/`](scripts/) | The repo's own tooling: `build-index.py`, `build-bundles.py`, `validate-skills.py`, `generate-project.py`, the SEO checkers, and `scripts/qa/` reference implementations |
| [`examples/`](examples/) | One worked example document per department (18 files) |
| [`docs/`](docs/) | The records and references: `PROJECT_ANATOMY.md` (the full project map), `METRICS.md` (every number, defined), `DECISIONS.md` (every deviation, with reasons), `WORK_LOG.md` + `work-log/` (the build record), `TROUBLESHOOTING.md` (stuck + waiver protocols), `MAINTENANCE_RUNBOOK.md`, `GLOSSARY.md`, `BAR_TRACEABILITY.md`, `DEPARTMENT_LINKS.md`, `contracts/` (the 14 cross-department contracts), and the research/mapping papers |
| [`USER_GUIDE.md`](USER_GUIDE.md) | The operator's guide — plain language, including a Roman Urdu quick-start |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How changes are proposed and reviewed |

## Maintaining this repo

`SKILLS_INDEX.md` and `bundles/` are generated — never hand-edit them. After changing any skill, regenerate and validate:

```bash
python3 scripts/build-index.py
python3 scripts/build-bundles.py
python3 scripts/validate-skills.py
```

See [`docs/MAINTENANCE_RUNBOOK.md`](docs/MAINTENANCE_RUNBOOK.md) for the full maintenance procedure and [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to propose changes. Rule IDs are registered in `docs/RULE_ID_REGISTRY.md` — new rules take the next free IDs; never reuse or collide.

## FAQ

- **Do I need to read all 238 skills?** No. You (the operator) read this README and `USER_GUIDE.md`. Your agent scans `SKILLS_INDEX.md`, loads the core bundle + the playbook bundle for your project type, then individual skills only where a step needs more.
- **Can I just paste the whole repo into my agent?** No — never paste `bundles/ALL_SKILLS.md` whole. Use the staged route: one custom-instructions file, then `bundles/core.md`, then one playbook bundle.
- **What does the agent need from me?** Your project description (or a filled `templates/USER_BRIEF.md`), decisions at the three approval points, and secrets via `templates/SECRETS_CHECKLIST.md` when a project needs them. Never paste secrets into project documents or code.
- **What can it build?** Web applications — SaaS, stores, blogs, dashboards, booking, LMS, marketplaces, chat apps, APIs, and the 8 hybrid missions (clone, rebrand, rescue, migrate, harden a prototype, AI-ify, localize, convert to SaaS). Not mobile or desktop apps — yet.
- **My app already exists — can OmniForge improve it?** Yes — that is the `ui-ux-upscaler` skill and playbook: audit, staged passes, leak gate, score gate. Web apps only for now.
- **What if the agent gets stuck or a skill conflicts with another?** It follows the stuck protocol and the 19-rank precedence order in `BOOTSTRAP.md`, logs the conflict in `DECISIONS.md`, and asks you rather than inventing a way out.
- **What if a gate fails?** The agent fixes the work — it is not allowed to weaken the gate to make it pass. A waiver needs to be recorded in writing, and a waiver of a security, legal, or Real Content gate needs your explicit agreement.
- **How much does it cost?** The repository itself is free (MIT). Your costs are your agent/platform usage and whatever hosting the project needs — the agent agrees a monthly cost cap with you before provisioning anything.
- **Where do I report a problem or propose a change?** See `CONTRIBUTING.md`. Include the skill path, the rule ID, and the evidence (what the agent did, what the gate said).

## Licence and credits

**MIT** — see the [`LICENSE`](LICENSE) file in this repository. Per `docs/DECISIONS.md` **D-004/D-019**, the MIT licence was applied when the repository was published public on GitHub (2026-11-21).

- **Creator:** MUHIUM — Founder of Mihora Tech.
- **Repository:** https://github.com/sisuppreme/ai-all-in-one-company
- **Also on Agensi:** 5 free packs (see the table in [Quick start](#quick-start--use-it-on-your-platform)).
