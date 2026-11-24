# OmniForge — ai-all-in-one-company

**A company in a repository.**

OmniForge packages the working knowledge of a complete web-application company — product, architecture, frontend, backend, data, DevOps, security, QA, SEO, legal, analytics, accessibility, integrations, AI features, and customer experience — as structured skills that **one AI agent** can load and execute end-to-end: research, build, verify, deploy, document, and hand over professional **web applications**, with real content only and every claim sourced.

- **Repository (public):** https://github.com/sisuppreme/ai-all-in-one-company
- **Created by:** MUHIUM — Founder of Mihora Tech
- **Licence:** MIT — see [`LICENSE`](LICENSE)
- **Custom-instructions pin:** **v1.4.0 (2026-11-24)** — the pin carried by all four files in [`custom-instructions/`](custom-instructions/)
- **Content verified on disk:** 2026-11-24 — `scripts/validate-skills.py`: **Checked 238 skills. ALL PASS**

> **Version: 1.4.0 (2026-11-24).** `VERSION` and `CHANGELOG.md` record the same version, and the custom-instructions files are pinned to it. Every count in this README was verified against the files on disk on 2026-11-24.

## Contents

- [What OmniForge is — and what it is not](#what-omniforge-is--and-what-it-is-not)
- [At a glance](#at-a-glance)
- [What's new](#whats-new)
- [Who it is for](#who-it-is-for)
- [Quick start — use it on your platform](#quick-start--use-it-on-your-platform)
- [How a project runs](#how-a-project-runs)
- [The 18 departments and all 238 skills](#the-18-departments-and-all-238-skills)
- [Detection parameters — the 203 tells](#detection-parameters--the-203-tells-not-skills)
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
| Worked examples | **715** before/after example files (3 per skill; [`vector-db`](skills/database/vector-db/SKILL.md) carries a fourth) + 18 department example documents | `skills/*/examples/`, `examples/` |
| Premium themes | **100** fully expanded theme specifications | `skills/frontend/theme-library/expanded/` |
| Cross-department contracts | **14** | `docs/contracts/` |
| Tracked files in the repo | **1,290** | whole repository |
| Validation (2026-11-24) | **Checked 238 skills. ALL PASS** | `scripts/validate-skills.py` |

## What's new

### v1.4.0 — 2026-11-24 — hard leak gate + repo-use enforcement (custom-instructions pin)

- **Architecture-Leak Rule — hard gate, fail-closed.** An application's structure must never leak into its UI: no DB names/types, table/collection names, page/route counts or structures, API endpoints, internal module/service names, tech-stack labels, or schema/field names on any user-facing surface. Any leak in the shipped UI is a gate FAIL, whatever the design score is. Target leak score: **zero**.
- **[`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) skill** (new): upgrades an existing application's UI to the same premium standard — audit, staged passes, leak gate, score gate (237 → 238 skills).
- **Repo-Use Enforcement (FE-381–FE-384, G-FE-191, BAN-FE-191).** The agent must read the named skill files from the repo *before* generating anything, stop (fail-closed) if a required skill cannot be read, and carry an attestation block in `progress.md` and in its reply — repo version, skills read, and every rule applied with its exact `file:line` evidence. A UI task's attestation must also name the theme and its canonical expanded spec, the design-intelligence gate score, and the AFTER leak score.
- **UI/UX Upscaler skill embedded in all 4 platform files**, so the leak gate cites a skill the instruction file actually contains.

### v1.3.0 — 2026-11-23 — Existing-Project Upgrade Protocol

- A staged upgrade protocol added to all 4 platform files: audit first, staged passes, score gate (design-intelligence gate, AFTER score ≥ 64/80, every audit defect fixed or explicitly reported).

### v1.2.0 — 2026-11-23 — 100-theme premium library

- **[`design-intelligence`](skills/frontend/design-intelligence/SKILL.md) skill** (new): art-direction decision systems, self-critique quality gates, anti-slop symptom → cause → fix detection, adaptation by brand/audience/content type, worked reasoning examples.
- **[`theme-library`](skills/frontend/theme-library/SKILL.md) skill**: **100 completely original premium themes**, each expanded to the full 50x standard — per-element build specs, choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens, worked examples, scroll choreography map, performance budget, build order.
- **Premium rewrites of [`motion`](skills/frontend/motion/SKILL.md) and [`scroll-experiences`](skills/frontend/scroll-experiences/SKILL.md)**: the old skills were written almost entirely as bans/restraint — they stopped bad motion but contained no positive premium-craft standard. They now carry the positive standard too.

### v1.1.0 — 2026-11-21 — Phase 8 hybrid expansion

- **8 new skills** for work that is not "build new" (227 → 235): [`clone-redesign`](skills/cloning-replication/clone-redesign/SKILL.md) and [`rebrand-execution`](skills/cloning-replication/rebrand-execution/SKILL.md) (D16), [`project-takeover`](skills/developer-experience/project-takeover/SKILL.md) and [`prototype-hardening`](skills/developer-experience/prototype-hardening/SKILL.md) (D15), [`seo-migration`](skills/seo-content/seo-migration/SKILL.md) (D9), [`ai-retrofit`](skills/ai-features/ai-retrofit/SKILL.md) (D17), [`market-expansion`](skills/product-requirements/market-expansion/SKILL.md) (D1), [`saas-conversion`](skills/architecture/saas-conversion/SKILL.md) (D2).
- **8 new hybrid playbooks** (13 → 21), one per hybrid mission.
- Totals at the time: 235 skills and 21 playbooks. The repo now holds 238 skills and 22 playbooks (see [At a glance](#at-a-glance)) — the extra skills are [`design-intelligence`](skills/frontend/design-intelligence/SKILL.md) and [`theme-library`](skills/frontend/theme-library/SKILL.md) (v1.2.0) and [`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) (v1.4.0), and the extra playbook is [`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md).
- One rule-ID collision between the two new D15 skills, found during integration and fixed by renumbering [`project-takeover`](skills/developer-experience/project-takeover/SKILL.md) into its own free ID block.

### v1.0.0 — 2026-11-21 — first public release

- 18 departments (D1–D18), 227 skills in the memory-proof format, 203 detection parameters, 13 project playbooks, 69 acceptance gates + G-QA-01…10, ready-to-paste custom instructions for 4 platforms, `BOOTSTRAP.md` repo-first protocol, script-generated `SKILLS_INDEX.md`.
- Published public on GitHub under MIT (2026-11-21) — decisions D-004/D-019 in `docs/DECISIONS.md`.

## Who it is for

- **A single AI agent working alone.** The repository is designed and proof-tested for one agent with no sub-agents, no leads, and no hand-offs. Everything the agent needs — routing, precedence when skills disagree, what to do when stuck, when to ask the operator — is written down in the repo itself.
- **One agent at runtime.** The 477 named roles in the Master Brief were the build-time staffing that authored this repository — a work-partitioning architecture, not a runtime requirement. At runtime, one agent loads the core bundle and the skills it needs; it does not run 477 processes. (See `docs/METRICS.md` — "Company headcount vs runtime".)
- **Its operator.** The person who commissions projects, answers the three approval points (requirements, deploy target and cost, go-live), supplies secrets through the handoff checklist, and gives the final ship approval. Operators should read [`USER_GUIDE.md`](USER_GUIDE.md) — it walks the whole route in plain language, including a Roman Urdu quick-start.
- **Contributors.** See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [Maintaining this repo](#maintaining-this-repo).

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

| Pack | Covers | Link / status |
|---|---|---|
| Pack 1 | Product, Architecture, Backend | https://www.agensi.io/skills/omniforge-pack-1-product-architecture-backend |
| Pack 2 | Frontend, UX, Accessibility, Cloning | https://www.agensi.io/skills/omniforge-pack-2-frontend-ux-accessibility-cloning |
| Pack 3 | Database, AI, DevOps | Pending review (as of 2026-11-22) — no public URL yet |
| Pack 4 | QA, Security, Legal, DX | Pending review (as of 2026-11-22) — no public URL yet |
| Pack 5 | SEO, Analytics, Payments, Memory | Pending review (as of 2026-11-22) — no public URL yet |

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

Higher rank wins; every conflict is logged in the project's `DECISIONS.md`. The full 19-rank order (also in `BOOTSTRAP.md`):

1. Security (D7), including D17 AI-safety rules
2. Legal / privacy (D14), including D16 clone-ethics
3. Real Content Rule — no fakes, ever
4. QA gates (D8, process gates only)
5. Accessibility (D13)
6. Requirements / scope (D1)
7. Architecture (D2)
8. Data integrity (D5)
9. Backend correctness (D4)
10. Production / deployability (D6)
11. Payments / integrations correctness (D11)
12. Performance (D12)
13. AI features (D17)
14. Content / SEO (D9)
15. Design / beauty (D3)
16. Clone fidelity (D16)
17. Customer experience (D18)
18. DX / maintenance (D15)
19. Project memory / docs (D10)

Tie rule: within one rank, the more specific skill wins; if still tied, ask the user and log the conflict. Precedence never excuses skipping a gate — when a higher-ranked rule conflicts with a gate, re-run the gate's check against the higher rule's requirement; do not skip it.

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

[`acceptance-criteria`](skills/product-requirements/acceptance-criteria/SKILL.md) · [`competitive-analysis`](skills/product-requirements/competitive-analysis/SKILL.md) · [`discovery`](skills/product-requirements/discovery/SKILL.md) · [`fact-sheet`](skills/product-requirements/fact-sheet/SKILL.md) · [`market-expansion`](skills/product-requirements/market-expansion/SKILL.md) · [`personas-jtbd`](skills/product-requirements/personas-jtbd/SKILL.md) · [`pricing-monetization`](skills/product-requirements/pricing-monetization/SKILL.md) · [`product-metrics`](skills/product-requirements/product-metrics/SKILL.md) · [`requirements-writing`](skills/product-requirements/requirements-writing/SKILL.md) · [`roadmapping`](skills/product-requirements/roadmapping/SKILL.md) · [`scope-control`](skills/product-requirements/scope-control/SKILL.md) · [`unit-economics`](skills/product-requirements/unit-economics/SKILL.md) · [`user-research`](skills/product-requirements/user-research/SKILL.md) · [`user-stories`](skills/product-requirements/user-stories/SKILL.md)

### D2 — Architecture & System Design (14)

[`adr-writing`](skills/architecture/adr-writing/SKILL.md) · [`api-architecture`](skills/architecture/api-architecture/SKILL.md) · [`api-documentation`](skills/architecture/api-documentation/SKILL.md) · [`api-paradigms`](skills/architecture/api-paradigms/SKILL.md) · [`api-versioning`](skills/architecture/api-versioning/SKILL.md) · [`architecture-patterns`](skills/architecture/architecture-patterns/SKILL.md) · [`c4-diagrams`](skills/architecture/c4-diagrams/SKILL.md) · [`data-architecture`](skills/architecture/data-architecture/SKILL.md) · [`domain-driven-design`](skills/architecture/domain-driven-design/SKILL.md) · [`event-driven`](skills/architecture/event-driven/SKILL.md) · [`multitenancy-saas`](skills/architecture/multitenancy-saas/SKILL.md) · [`saas-conversion`](skills/architecture/saas-conversion/SKILL.md) · [`stack-selection`](skills/architecture/stack-selection/SKILL.md) · [`system-design`](skills/architecture/system-design/SKILL.md)

### D3 — Frontend, Design & Motion (19)

[`client-routing`](skills/frontend/client-routing/SKILL.md) · [`component-library`](skills/frontend/component-library/SKILL.md) · [`data-fetching`](skills/frontend/data-fetching/SKILL.md) · [`data-visualisation`](skills/frontend/data-visualisation/SKILL.md) · [`design-intelligence`](skills/frontend/design-intelligence/SKILL.md) · [`design-system`](skills/frontend/design-system/SKILL.md) · [`design-tokens`](skills/frontend/design-tokens/SKILL.md) · [`forms`](skills/frontend/forms/SKILL.md) · [`frontend-core`](skills/frontend/frontend-core/SKILL.md) · [`frontend-state`](skills/frontend/frontend-state/SKILL.md) · [`layout-responsive`](skills/frontend/layout-responsive/SKILL.md) · [`motion`](skills/frontend/motion/SKILL.md) · [`pwa-offline`](skills/frontend/pwa-offline/SKILL.md) · [`scroll-experiences`](skills/frontend/scroll-experiences/SKILL.md) · [`theme-library`](skills/frontend/theme-library/SKILL.md) · [`typography`](skills/frontend/typography/SKILL.md) · [`ui-states`](skills/frontend/ui-states/SKILL.md) · [`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) · [`webgl-3d`](skills/frontend/webgl-3d/SKILL.md)

### D4 — Backend & APIs (16)

[`admin-tools`](skills/backend/admin-tools/SKILL.md) · [`api-building`](skills/backend/api-building/SKILL.md) · [`backend-auth`](skills/backend/backend-auth/SKILL.md) · [`error-handling`](skills/backend/error-handling/SKILL.md) · [`feature-flags`](skills/backend/feature-flags/SKILL.md) · [`file-uploads`](skills/backend/file-uploads/SKILL.md) · [`media-processing`](skills/backend/media-processing/SKILL.md) · [`notifications`](skills/backend/notifications/SKILL.md) · [`queues-jobs`](skills/backend/queues-jobs/SKILL.md) · [`rate-limiting`](skills/backend/rate-limiting/SKILL.md) · [`rbac`](skills/backend/rbac/SKILL.md) · [`realtime`](skills/backend/realtime/SKILL.md) · [`rest-conventions`](skills/backend/rest-conventions/SKILL.md) · [`sdk-design`](skills/backend/sdk-design/SKILL.md) · [`user-reporting`](skills/backend/user-reporting/SKILL.md) · [`validation`](skills/backend/validation/SKILL.md)

### D5 — Databases & Data (20)

[`backup-recovery`](skills/database/backup-recovery/SKILL.md) · [`caching`](skills/database/caching/SKILL.md) · [`data-access`](skills/database/data-access/SKILL.md) · [`data-ingestion`](skills/database/data-ingestion/SKILL.md) · [`data-quality`](skills/database/data-quality/SKILL.md) · [`data-warehousing`](skills/database/data-warehousing/SKILL.md) · [`etl-pipelines`](skills/database/etl-pipelines/SKILL.md) · [`indexing`](skills/database/indexing/SKILL.md) · [`migrations`](skills/database/migrations/SKILL.md) · [`nosql-patterns`](skills/database/nosql-patterns/SKILL.md) · [`pipeline-orchestration`](skills/database/pipeline-orchestration/SKILL.md) · [`query-performance`](skills/database/query-performance/SKILL.md) · [`read-replicas`](skills/database/read-replicas/SKILL.md) · [`schema-design`](skills/database/schema-design/SKILL.md) · [`search-engines`](skills/database/search-engines/SKILL.md) · [`seed-data`](skills/database/seed-data/SKILL.md) · [`sql-fundamentals`](skills/database/sql-fundamentals/SKILL.md) · [`tenant-isolation`](skills/database/tenant-isolation/SKILL.md) · [`transactions-concurrency`](skills/database/transactions-concurrency/SKILL.md) · [`vector-db`](skills/database/vector-db/SKILL.md)

### D6 — DevOps & Deployment (17)

[`cdn-strategy`](skills/devops-deployment/cdn-strategy/SKILL.md) · [`ci-cd`](skills/devops-deployment/ci-cd/SKILL.md) · [`cloud-costs`](skills/devops-deployment/cloud-costs/SKILL.md) · [`containers`](skills/devops-deployment/containers/SKILL.md) · [`deployment-strategies`](skills/devops-deployment/deployment-strategies/SKILL.md) · [`domains-dns`](skills/devops-deployment/domains-dns/SKILL.md) · [`free-tiers`](skills/devops-deployment/free-tiers/SKILL.md) · [`hosting`](skills/devops-deployment/hosting/SKILL.md) · [`incident-response`](skills/devops-deployment/incident-response/SKILL.md) · [`infrastructure-as-code`](skills/devops-deployment/infrastructure-as-code/SKILL.md) · [`kubernetes`](skills/devops-deployment/kubernetes/SKILL.md) · [`preview-environments`](skills/devops-deployment/preview-environments/SKILL.md) · [`reliability`](skills/devops-deployment/reliability/SKILL.md) · [`rollback`](skills/devops-deployment/rollback/SKILL.md) · [`scaling`](skills/devops-deployment/scaling/SKILL.md) · [`servers-vps`](skills/devops-deployment/servers-vps/SKILL.md) · [`ssl-certificates`](skills/devops-deployment/ssl-certificates/SKILL.md)

### D7 — Security (14)

[`api-security`](skills/security/api-security/SKILL.md) · [`auth-hardening`](skills/security/auth-hardening/SKILL.md) · [`content-moderation`](skills/security/content-moderation/SKILL.md) · [`dependency-safety`](skills/security/dependency-safety/SKILL.md) · [`encryption`](skills/security/encryption/SKILL.md) · [`owasp`](skills/security/owasp/SKILL.md) · [`pci-compliance`](skills/security/pci-compliance/SKILL.md) · [`penetration-testing`](skills/security/penetration-testing/SKILL.md) · [`secrets-management`](skills/security/secrets-management/SKILL.md) · [`security-audit`](skills/security/security-audit/SKILL.md) · [`security-headers`](skills/security/security-headers/SKILL.md) · [`session-security`](skills/security/session-security/SKILL.md) · [`supply-chain`](skills/security/supply-chain/SKILL.md) · [`threat-modelling`](skills/security/threat-modelling/SKILL.md)

### D8 — QA & Testing (15)

[`accessibility-testing`](skills/qa-testing/accessibility-testing/SKILL.md) · [`browser-verification`](skills/qa-testing/browser-verification/SKILL.md) · [`bug-triage`](skills/qa-testing/bug-triage/SKILL.md) · [`chaos-testing`](skills/qa-testing/chaos-testing/SKILL.md) · [`contract-testing`](skills/qa-testing/contract-testing/SKILL.md) · [`e2e-testing`](skills/qa-testing/e2e-testing/SKILL.md) · [`integration-testing`](skills/qa-testing/integration-testing/SKILL.md) · [`load-testing`](skills/qa-testing/load-testing/SKILL.md) · [`placeholder-scan`](skills/qa-testing/placeholder-scan/SKILL.md) · [`qa-gates`](skills/qa-testing/qa-gates/SKILL.md) · [`security-testing`](skills/qa-testing/security-testing/SKILL.md) · [`test-data`](skills/qa-testing/test-data/SKILL.md) · [`test-strategy`](skills/qa-testing/test-strategy/SKILL.md) · [`unit-testing`](skills/qa-testing/unit-testing/SKILL.md) · [`visual-regression`](skills/qa-testing/visual-regression/SKILL.md)

### D9 — SEO & Content (15)

[`aeo`](skills/seo-content/aeo/SKILL.md) · [`content-strategy`](skills/seo-content/content-strategy/SKILL.md) · [`copywriting`](skills/seo-content/copywriting/SKILL.md) · [`geo`](skills/seo-content/geo/SKILL.md) · [`growth-experiments`](skills/seo-content/growth-experiments/SKILL.md) · [`internal-linking`](skills/seo-content/internal-linking/SKILL.md) · [`lifecycle-email`](skills/seo-content/lifecycle-email/SKILL.md) · [`on-page-seo`](skills/seo-content/on-page-seo/SKILL.md) · [`real-content`](skills/seo-content/real-content/SKILL.md) · [`seo-migration`](skills/seo-content/seo-migration/SKILL.md) · [`sitemaps`](skills/seo-content/sitemaps/SKILL.md) · [`social-open-graph`](skills/seo-content/social-open-graph/SKILL.md) · [`structured-data`](skills/seo-content/structured-data/SKILL.md) · [`technical-seo`](skills/seo-content/technical-seo/SKILL.md) · [`web-analytics`](skills/seo-content/web-analytics/SKILL.md)

### D10 — Project & Memory (10)

[`changelog`](skills/project-memory/changelog/SKILL.md) · [`decision-logs`](skills/project-memory/decision-logs/SKILL.md) · [`documentation-writing`](skills/project-memory/documentation-writing/SKILL.md) · [`handover`](skills/project-memory/handover/SKILL.md) · [`memory-retrieval`](skills/project-memory/memory-retrieval/SKILL.md) · [`postmortem-writing`](skills/project-memory/postmortem-writing/SKILL.md) · [`progress-tracking`](skills/project-memory/progress-tracking/SKILL.md) · [`project-templates`](skills/project-memory/project-templates/SKILL.md) · [`readme-writing`](skills/project-memory/readme-writing/SKILL.md) · [`runbook-writing`](skills/project-memory/runbook-writing/SKILL.md)

### D11 — Integrations & Payments (12)

[`api-keys-management`](skills/integrations-payments/api-keys-management/SKILL.md) · [`dunning`](skills/integrations-payments/dunning/SKILL.md) · [`invoicing-tax`](skills/integrations-payments/invoicing-tax/SKILL.md) · [`oauth-sso`](skills/integrations-payments/oauth-sso/SKILL.md) · [`payments`](skills/integrations-payments/payments/SKILL.md) · [`refunds-disputes`](skills/integrations-payments/refunds-disputes/SKILL.md) · [`sdk-embeddables`](skills/integrations-payments/sdk-embeddables/SKILL.md) · [`sms`](skills/integrations-payments/sms/SKILL.md) · [`subscriptions`](skills/integrations-payments/subscriptions/SKILL.md) · [`third-party-apis`](skills/integrations-payments/third-party-apis/SKILL.md) · [`transactional-email`](skills/integrations-payments/transactional-email/SKILL.md) · [`webhooks`](skills/integrations-payments/webhooks/SKILL.md)

### D12 — Analytics & Observability (13)

[`alerting`](skills/analytics-observability/alerting/SKILL.md) · [`apm`](skills/analytics-observability/apm/SKILL.md) · [`core-web-vitals`](skills/analytics-observability/core-web-vitals/SKILL.md) · [`dashboards`](skills/analytics-observability/dashboards/SKILL.md) · [`error-tracking`](skills/analytics-observability/error-tracking/SKILL.md) · [`event-tracking`](skills/analytics-observability/event-tracking/SKILL.md) · [`experimentation-platform`](skills/analytics-observability/experimentation-platform/SKILL.md) · [`logging`](skills/analytics-observability/logging/SKILL.md) · [`monitoring`](skills/analytics-observability/monitoring/SKILL.md) · [`performance-budgets`](skills/analytics-observability/performance-budgets/SKILL.md) · [`performance-optimization`](skills/analytics-observability/performance-optimization/SKILL.md) · [`product-analytics`](skills/analytics-observability/product-analytics/SKILL.md) · [`revenue-analytics`](skills/analytics-observability/revenue-analytics/SKILL.md)

### D13 — Accessibility & i18n (10)

[`accessibility-audit`](skills/accessibility-i18n/accessibility-audit/SKILL.md) · [`accessibility-law`](skills/accessibility-i18n/accessibility-law/SKILL.md) · [`inclusive-copy`](skills/accessibility-i18n/inclusive-copy/SKILL.md) · [`internationalization`](skills/accessibility-i18n/internationalization/SKILL.md) · [`keyboard-accessibility`](skills/accessibility-i18n/keyboard-accessibility/SKILL.md) · [`localization-workflow`](skills/accessibility-i18n/localization-workflow/SKILL.md) · [`reduced-motion`](skills/accessibility-i18n/reduced-motion/SKILL.md) · [`rtl-layouts`](skills/accessibility-i18n/rtl-layouts/SKILL.md) · [`screen-readers`](skills/accessibility-i18n/screen-readers/SKILL.md) · [`wcag`](skills/accessibility-i18n/wcag/SKILL.md)

### D14 — Legal & Privacy (10)

[`age-requirements`](skills/legal-privacy/age-requirements/SKILL.md) · [`audit-trails`](skills/legal-privacy/audit-trails/SKILL.md) · [`clone-ethics`](skills/legal-privacy/clone-ethics/SKILL.md) · [`compliance-audit`](skills/legal-privacy/compliance-audit/SKILL.md) · [`cookie-consent`](skills/legal-privacy/cookie-consent/SKILL.md) · [`data-residency`](skills/legal-privacy/data-residency/SKILL.md) · [`dsar-handling`](skills/legal-privacy/dsar-handling/SKILL.md) · [`legal-documents`](skills/legal-privacy/legal-documents/SKILL.md) · [`licensing`](skills/legal-privacy/licensing/SKILL.md) · [`privacy-laws`](skills/legal-privacy/privacy-laws/SKILL.md)

### D15 — Developer Experience (10)

[`code-generation`](skills/developer-experience/code-generation/SKILL.md) · [`dependency-management`](skills/developer-experience/dependency-management/SKILL.md) · [`dev-environment`](skills/developer-experience/dev-environment/SKILL.md) · [`legacy-migration`](skills/developer-experience/legacy-migration/SKILL.md) · [`monorepo-tooling`](skills/developer-experience/monorepo-tooling/SKILL.md) · [`project-takeover`](skills/developer-experience/project-takeover/SKILL.md) · [`prototype-hardening`](skills/developer-experience/prototype-hardening/SKILL.md) · [`refactoring`](skills/developer-experience/refactoring/SKILL.md) · [`tech-debt`](skills/developer-experience/tech-debt/SKILL.md) · [`versioning`](skills/developer-experience/versioning/SKILL.md)

### D16 — Cloning & Replication (9)

[`asset-harvesting`](skills/cloning-replication/asset-harvesting/SKILL.md) · [`behavior-cloning`](skills/cloning-replication/behavior-cloning/SKILL.md) · [`clone-redesign`](skills/cloning-replication/clone-redesign/SKILL.md) · [`design-extraction`](skills/cloning-replication/design-extraction/SKILL.md) · [`fidelity-verification`](skills/cloning-replication/fidelity-verification/SKILL.md) · [`page-inventory`](skills/cloning-replication/page-inventory/SKILL.md) · [`page-reconstruction`](skills/cloning-replication/page-reconstruction/SKILL.md) · [`rebrand-execution`](skills/cloning-replication/rebrand-execution/SKILL.md) · [`site-discovery`](skills/cloning-replication/site-discovery/SKILL.md)

### D17 — AI Features (11)

[`ai-cost-control`](skills/ai-features/ai-cost-control/SKILL.md) · [`ai-evaluation`](skills/ai-features/ai-evaluation/SKILL.md) · [`ai-observability`](skills/ai-features/ai-observability/SKILL.md) · [`ai-retrofit`](skills/ai-features/ai-retrofit/SKILL.md) · [`ai-safety`](skills/ai-features/ai-safety/SKILL.md) · [`embeddings-search`](skills/ai-features/embeddings-search/SKILL.md) · [`llm-integration`](skills/ai-features/llm-integration/SKILL.md) · [`prompt-engineering`](skills/ai-features/prompt-engineering/SKILL.md) · [`rag-retrieval`](skills/ai-features/rag-retrieval/SKILL.md) · [`recommendations`](skills/ai-features/recommendations/SKILL.md) · [`search-relevance`](skills/ai-features/search-relevance/SKILL.md)

### D18 — Customer Experience (9)

[`activation-metrics`](skills/customer-experience/activation-metrics/SKILL.md) · [`churn-prevention`](skills/customer-experience/churn-prevention/SKILL.md) · [`feedback-loops`](skills/customer-experience/feedback-loops/SKILL.md) · [`help-center`](skills/customer-experience/help-center/SKILL.md) · [`in-app-chat`](skills/customer-experience/in-app-chat/SKILL.md) · [`status-communications`](skills/customer-experience/status-communications/SKILL.md) · [`support-ticketing`](skills/customer-experience/support-ticketing/SKILL.md) · [`trial-conversion`](skills/customer-experience/trial-conversion/SKILL.md) · [`user-onboarding`](skills/customer-experience/user-onboarding/SKILL.md)

### Detection parameters — the 203 tells (not skills)

The detection parameters live in [`skills/detection/`](skills/detection/) (7 family folders: `visual`, `code`, `infra`, `content`, `ux`, `fake`, `crawl`). They name what AI-generated work typically gets wrong; skills and gates are built to defeat them. Each parameter carries signal, AI-typical vs. professional form, check, false positives, severity, source, and fix. They are indexed inside their own `PARAMETERS.md` files, not in `SKILLS_INDEX.md`.

## The premium design standard

A site built with OmniForge must be unmatched — never "AI slop". The standard is enforced by the compulsory UI/UX skill set, not left to taste:

- **Compulsory UI/UX skills (always applied to any UI work, unless the user explicitly says not to):** [`design-intelligence`](skills/frontend/design-intelligence/SKILL.md), [`design-system`](skills/frontend/design-system/SKILL.md), [`design-tokens`](skills/frontend/design-tokens/SKILL.md), [`typography`](skills/frontend/typography/SKILL.md), [`layout-responsive`](skills/frontend/layout-responsive/SKILL.md), [`component-library`](skills/frontend/component-library/SKILL.md), [`ui-states`](skills/frontend/ui-states/SKILL.md), [`motion`](skills/frontend/motion/SKILL.md), [`scroll-experiences`](skills/frontend/scroll-experiences/SKILL.md) — plus [`webgl-3d`](skills/frontend/webgl-3d/SKILL.md) when the chosen theme calls for it, and [`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) whenever the task upgrades an already-built application's UI.
- **Full motion system on every page, in the theme's own style — never copy-paste.** Every theme carries its own motion system that practically uses, heavily, the full motion vocabulary: scroll-triggered reveals, scroll-driven / scrub animation, parallax, pinned sections, smooth scrolling, progress indicator, staggered + masked reveals, kinetic typography, marquee, counters, SVG line-draw, image scale-in-frame, hover / magnetic / tilt micro-interactions, custom cursor, skeleton loading, page transitions, and reduced-motion support.
- **5–20 signature animated elements per theme**, specially designed for that theme and **merged with the site's content** — never pasted on top of it. A built element (a jar, a train, an instrument, any themed object) must be integrated with the content it serves; if it looks like a pointless add-on, it is a defect. 3D where possible, otherwise excellently animated.
- **Feather-light cursor, or none.** Heavy custom cursors are banned. If a custom cursor makes the pointer hard to move, it is a defect, not premium. Normal system cursor by default; performance first.
- **Reveals can never leave content invisible.** Every reveal needs a fallback, and the page stays readable with JavaScript disabled.
- **Scroll-driven motion is smoothed** (requestAnimationFrame lerp, no jitter). `prefers-reduced-motion` is honoured.
- **Design-intelligence quality gate:** before any UI work is called done, run the [`design-intelligence`](skills/frontend/design-intelligence/SKILL.md) quality gate and record its result in `progress.md` with the other gates. The AFTER score must reach the gate's pass mark (**≥ 64/80**) and every defect in the audit list must be fixed — or explicitly reported, with a reason, in the audit file.
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

New builds are only half the story. The **[`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) skill** (`skills/frontend/ui-ux-upscaler/`, web apps only for now) takes an existing application's existing UI and upscales it to the same premium standard — full motion system on every page, 5–20 signature animated elements merged into content, feather-light cursor, original premium design, quality never dropping. It is the full skill form of the v1.3.0 Existing-Project Upgrade Protocol, with its own playbook ([`playbooks/ui-ux-upscaler.md`](playbooks/ui-ux-upscaler.md)) and bundle ([`bundles/ui-ux-upscaler.md`](bundles/ui-ux-upscaler.md)).

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
| [`saas-web-app`](playbooks/saas-web-app.md) | SaaS web app |
| [`content-blog-site`](playbooks/content-blog-site.md) | Content / blog site |
| [`api-database-service`](playbooks/api-database-service.md) | API + database service |
| [`e-commerce-store`](playbooks/e-commerce-store.md) | E-commerce store |
| [`clone-rebuild`](playbooks/clone-rebuild.md) | Clone rebuild |
| [`dashboard-admin-panel`](playbooks/dashboard-admin-panel.md) | Dashboard / admin panel |
| [`booking-scheduling`](playbooks/booking-scheduling.md) | Booking & scheduling |
| [`online-learning-lms`](playbooks/online-learning-lms.md) | Online learning (LMS) |
| [`landing-page`](playbooks/landing-page.md) | Landing page |
| [`portfolio-marketing-site`](playbooks/portfolio-marketing-site.md) | Portfolio / marketing site |
| [`internal-crud-admin-tool`](playbooks/internal-crud-admin-tool.md) | Internal CRUD admin tool |
| [`two-sided-marketplace`](playbooks/two-sided-marketplace.md) | Two-sided marketplace |
| [`realtime-chat-app`](playbooks/realtime-chat-app.md) | Realtime chat app |

### 8 hybrid playbooks (v1.1.0) — work that starts from something that already exists

| Playbook | Mission |
|---|---|
| [`clone-and-redesign`](playbooks/clone-and-redesign.md) | Clone a reference product's function, then redesign everything — original design, brand, and copy |
| [`clone-and-rebrand`](playbooks/clone-and-rebrand.md) | Keep a working product's function; replace its identity end-to-end (name, logo, palette, voice) |
| [`rescue-and-relaunch`](playbooks/rescue-and-relaunch.md) | Take over a broken or abandoned live product, audit it, fix in priority order, and relaunch safely |
| [`replatform-migration`](playbooks/replatform-migration.md) | Move a live product to a new stack or platform with zero data loss and search rankings preserved |
| [`prototype-to-production`](playbooks/prototype-to-production.md) | Turn a rough MVP or prototype (including AI-generated output) into production-grade software |
| [`ai-ify-existing-product`](playbooks/ai-ify-existing-product.md) | Add AI features to a live non-AI product without breaking what already works |
| [`localize-new-market`](playbooks/localize-new-market.md) | Launch an existing product in a new country — language, payments, legal, pricing, support |
| [`single-app-to-saas`](playbooks/single-app-to-saas.md) | Convert a single-client application into a multi-tenant SaaS with billing and tenant isolation |

### 1 upscaler playbook

| Playbook | Mission |
|---|---|
| [`ui-ux-upscaler`](playbooks/ui-ux-upscaler.md) | Upgrade an existing application's UI to the full premium standard — audit, staged passes, leak gate, score gate |

## Bundles — token-capped loads

Bundles are generated, token-capped loads — never hand-edit them. [`core.md`](bundles/core.md) is always on (under 10,000 tokens). Department bundles carry the full rules/gates/bans; longer examples point to the source skills.

| Bundle group | Files | Notes |
|---|---|---|
| Always-on core | [`core.md`](bundles/core.md) | Load first, every project |
| Department bundles | 21 files covering 18 departments | `seo-content`, `devops-deployment`, and `frontend` are each split across two files |
| Playbook bundles | 22 files, one per playbook | The default complete load for a playbook walk |
| Reference only | [`ALL_SKILLS.md`](bundles/ALL_SKILLS.md) | Human reference / offline search only — **never load it whole** |

## Gates and detection

- **Acceptance gates:** 69 inherited gates in [`gates/ACCEPTANCE_GATES.md`](gates/ACCEPTANCE_GATES.md), plus the 10-gate skill-release QA protocol ([`gates/QA_PROTOCOL_GATES.md`](gates/QA_PROTOCOL_GATES.md), G-QA-01…10), plus at least 3 gates inside every skill.
- **Gate registry:** [`gates/`](gates/) also holds `FINAL_ACCEPTANCE_CHECKLIST.md`, `DEFECT_TAXONOMY.md`, `NUMBERS_REGISTRY.md`, `VISUAL_QA_INDEX.md`, and the placeholder scan lists.
- **Detection first:** the 203 detection parameters name what AI-generated work typically gets wrong; skills and gates are built to defeat them.
- **Hard rules (summary):**
  - **Real Content Rule:** every fact, figure, name, and claim in any output must be real and sourced — never invent data, testimonials, statistics, or functionality.
  - **No silent skips:** gates pass on evidence, pass by a named fallback form, or are waived in writing.
  - **Docs before code, memory always:** project documents come first, and `progress.md` is updated as work proceeds.
  - **Architecture never leaks into the UI** (v1.4.0 hard gate — see above).

## Quality evidence — how it was proof-tested

This repository was proof-tested before release, by fresh agents working only from the repo itself (full record: [`docs/METRICS.md`](docs/METRICS.md), Phase 6; per-project detail: `docs/work-log/phase-6.md`): These are the repository's own proof results, reported by its authors — not independent production guarantees, and live deployment was not demonstrated end-to-end on live hosting.

- **Validation:** `scripts/validate-skills.py` over the full repo — **238 skills checked, ALL PASS** (re-run 2026-11-24; the v1.0.0 record was 227/227, the v1.1.0 record 235/235). All bundles regenerated with **0 cap failures**.
- **Findability (§5.3 formal test):** a fresh agent given only `BOOTSTRAP.md` + `SKILLS_INDEX.md` picked the correct skill first on **10/10 tasks (bar: 9/10)**, spanning 7 departments.
- **Proof projects** — four complete builds, each gate-checked:
  - **P1 TaskBoard** (the single-agent proof, run under `custom-instructions/ai-studio.md`): a multi-tenant SaaS task manager with billing and English/Urdu-RTL internationalization — 43/52 gates passed (4 waived in tool form with substitute evidence, 4 blocked in the provisioning/Stripe-live class, 1 partial), **29/29 automated tests green**.
  - **P2 Atlas Blog**: 19/19 gates passed.
  - **P3 Ledger API**: 42/48 gates passed; the built service shipped with zero open defects.
  - **P4 ShopClone**: 49/56 gates passed (3 waived with recorded decisions).
  - Every defect the proofs surfaced in the repo itself was fixed or verified closed; no gate's pass criterion was weakened to get there. All four proofs were built and verified locally; live deployment depends on the operator's hosting provisioning.
- **Playbook dry runs:** the remaining playbooks were each executed end-to-end by a lone agent — **all 13 original playbooks covered**. Their 66 friction points were triaged into 28 root-cause clusters; all 22 open clusters were fixed. The 8 hybrid playbooks (v1.1.0) and the UI/UX upscaler playbook (v1.4.0) were added after the Phase 6 dry runs and are not covered by that claim.
- **Detection calibration:** the 39 visual parameters that text-only testing could not reach were screenshot-tested against professional sites — 4 false-positive parameters found, narrowed, and re-walked clean (6/6 checks clear).
- **Cross-review:** 94 of the 227 skills at that time (v1.0.0; the repo now holds 238) were deep-read by independent reviewers before release — 0 blockers; all 6 majors and actionable minors fixed.
- **Slop and fake content:** 0 slop hits and 0 fake-content hits in the proofs that record them.
- **Phase 8 quality process (D-020):** 30 builders, 10 cross-assigned debaters, a 5-member review board, and a 4-member final committee, with structured handoffs and a coordinator verification layer between tiers. The debaters fixed 44 flaws; the board signed off 5/5.

## Repository map

| Path | What it holds |
|---|---|
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | The start-here protocol every agent follows before doing anything else, including the 19-rank precedence order for when skills disagree |
| [`SKILLS_INDEX.md`](SKILLS_INDEX.md) | Script-generated catalog of all 238 skills: department, keywords, dependencies, size, gates. Scan it; do not read it whole |
| [`VERSION`](VERSION), [`CHANGELOG.md`](CHANGELOG.md) | Current version (1.4.0) and its release record |
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
- **My app already exists — can OmniForge improve it?** Yes — that is the [`ui-ux-upscaler`](skills/frontend/ui-ux-upscaler/SKILL.md) skill and playbook: audit, staged passes, leak gate, score gate. Web apps only for now.
- **What if the agent gets stuck or a skill conflicts with another?** It follows the stuck protocol and the 19-rank precedence order in `BOOTSTRAP.md`, logs the conflict in `DECISIONS.md`, and asks you rather than inventing a way out.
- **What if a gate fails?** The agent fixes the work — it is not allowed to weaken the gate to make it pass. A waiver needs to be recorded in writing, and a waiver of a security, legal, or Real Content gate needs your explicit agreement.
- **How much does it cost?** The repository itself is free (MIT). Your costs are your agent/platform usage and whatever hosting the project needs — the agent agrees a monthly cost cap with you before provisioning anything.
- **Where do I report a problem or propose a change?** See `CONTRIBUTING.md`. Include the skill path, the rule ID, and the evidence (what the agent did, what the gate said).

## Licence and credits

**MIT** — see the [`LICENSE`](LICENSE) file in this repository. Per `docs/DECISIONS.md` **D-004/D-019**, the MIT licence was applied when the repository was published public on GitHub (2026-11-21).

- **Creator:** MUHIUM — Founder of Mihora Tech.
- **Repository:** https://github.com/sisuppreme/ai-all-in-one-company
- **Also on Agensi:** 5 free packs (see the table in [Quick start](#quick-start--use-it-on-your-platform)).
