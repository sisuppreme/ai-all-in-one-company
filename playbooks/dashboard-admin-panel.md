# Playbook: Dashboard / Admin Panel

An authenticated data interface: charts, tables, filters, and administrative actions over an existing (or new) API. The users are operators, staff, or customers managing their own data — the risks are wrong data shown confidently, and authorization gaps that leak one user's data to another.

## Goal

Ship a panel where every chart answers a stated question with data traced to a real query, every action is authorized server-side per role and per tenant, tables and charts are usable by keyboard and screen reader, and the panel deploys behind the same security and QA gates as any production app.

## Departments and order

D1 → D2+D7 → D3+D13+D4+D5 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation. This playbook has no D11 step (a panel moves no money itself; if it administers billing, the billing *mutations* belong to the SaaS playbook's step 4 skills and gates). D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule; D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | system-design (D2); threat-modelling, owasp (D7) | `bundles/architecture.md`, `bundles/security.md` |
| 3 | data-visualisation, frontend-core, component-library, forms (D3); wcag, accessibility-audit (D13); api-building, rbac, backend-auth, validation (D4); schema-design (D5) | `bundles/frontend.md`, `bundles/accessibility-i18n.md`, `bundles/backend.md`, `bundles/database.md` |
| 4 | (no new department — deepening step: rbac + data-visualisation gates executed in full) | — |
| 4b (conditional) | llm-integration, ai-safety (D17) — only for AI features such as natural-language querying or auto-summaries | `bundles/ai-features.md` |
| 5 | performance-budgets, dashboards, monitoring (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, audit-trails, legal-documents (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | support-ticketing, user-onboarding (D18) — only if the panel ships support surfaces | `bundles/customer-experience.md` |
| 7 | security-audit, api-security, dependency-safety (D7); placeholder-scan, e2e-testing, accessibility-testing (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | ci-cd, hosting, rollback (D6) | `bundles/devops-deployment.md` |
| 9 | web-analytics, technical-seo (internal/noindex configuration only) (D9) | `bundles/seo-content.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — roles, the decisions each screen supports, and the actions each role may take.
- `fact-sheet.md` — the metric definitions the panel will display: each metric's name, formula, source table/event, and owner. A chart without a definition in this sheet is not built.
- `stack.md` — stack choice with dated criteria (G-AR-023).
- `progress.md`, `DECISIONS.md` — session log and decision record.
- `ARCHITECTURE.md` — where the panel's API lives, how it authenticates, and the authorization model (roles × resources matrix, drafted here, enforced in step 3).
- `SCHEMA.md` — invariants for any new tables (audit log append-only, tenant key on every row the panel reads).
- `API_CONTRACTS.md` — the panel's read/write endpoints and their authorization requirements per role.
- `.env.example` — API and database credentials by name + purpose (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above.

**Step 1 — Requirements (D1).** For every screen, name the decision it supports and the role that makes it. A screen with no decision is cut or justified in `DECISIONS.md` — dashboards accumulate vanity charts faster than any other surface. Metric definitions go into `fact-sheet.md` now, with formulas, so step 3 builds charts against definitions instead of inventing them.

**Step 2 — Architecture + security design (D2+D7).** The authorization model is designed here, not discovered during testing: roles × resources × actions matrix in `ARCHITECTURE.md`, threat model focused on privilege escalation and cross-tenant reads (the two panel-specific catastrophic failures).
◆ **DECISION — whose data does the panel show?** One organization's own data (single-tenant admin) or many customers' data (multi-tenant)? Multi-tenant makes `tenant-isolation` mandatory and adds the cross-tenant gates (G-DB-051, G-BE-062) to step 7. If the user has not specified, ask (§6.3 step 4). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 3 — Build (D3+D13+D4+D5).** API and authorization first: every endpoint enforces the matrix server-side (G-BE-061 authorization matrix test, G-BE-063 client-trust scan — a role flag checked only in the UI is a failed gate, not a shortcut). Charts second, each built against its `fact-sheet.md` definition and passing the data-visualisation gates: accessible alternative in the DOM (G-FE-131), the one-sentence message test (G-FE-132), axis/label/source inspection (G-FE-133). Tables get the same D13 treatment as any UI: keyboard walk (G-AC-002), criterion checklist (G-AC-015).
**Real-data rule for development:** build against a seeded database whose seed data is labeled synthetic in `progress.md` and generated from the metric definitions — never against hand-typed "sample numbers" pasted into components, and never against production data copied to a laptop (§5.9; D14 step 6 governs any real-data use).

**Step 4 — Authorization and data deepening.** Run the full rbac and tenant suites before any polish work: authorization matrix test (G-BE-061), cross-tenant access test (G-BE-062, multi-tenant only), audit-log completeness (G-BE-064) — every administrative mutation writes an audit record naming actor, action, and target.
**Step 4b — AI features (D17, conditional).** Natural-language query or auto-summary features are built under `llm-integration` + `ai-safety` (G-AI-001, G-AI-021), and their queries pass through the *same* authorization layer as the UI — an AI feature that can read data the user's role cannot is a critical finding, full stop.

**Step 5 — Performance budgets (D12, explicit step).** Budgets for the heaviest screens (largest table, densest chart) asserted per G-AN-101 — in CI where a pipeline exists, otherwise via the gate's local/offline assertion path with the tool substitution recorded in `progress.md`; the panel's own observability is set up here too (`dashboards`, `monitoring`) so operators can see the panel's health, not just the product's.

**Step 6 — Legal and privacy (D14, explicit step).** A panel concentrates personal data: the register (G-LG-001) covers everything the panel can display or export; exports and bulk views get explicit treatment (who may export, what is logged — G-LG-081 audit-trails gates); retention and access are documented in the privacy record. If the panel is internal-only, that status and the user's reason are recorded in `requirements.md` (QB-02 exception) — internal-only never means unregistered.

**Step 7 — Verification (D7+D8).** Security pass weighted to this playbook's risks: API authorization matrix suite (G-SE-021), API inventory diff so no undocumented endpoint ships (G-SE-022), OWASP checklist (G-SE-003) — 0 critical; accessibility testing as its own D8 pass (G-QA-051 accessibility-testing gates) in addition to the step 3 checks; placeholder sweep (G-QA-141; scan rendered output, not source) — including chart empty states, which must render as honest empty states, not demo data; e2e suite green (G-QA-021).

**Step 8 — Deploy (D6, last build step).** Pipeline (G-DO-001), production checks (G-DO-071, G-DO-073), rollback drill (G-DO-151). The panel deploys behind authentication from the first production minute — there is no "temporary public preview" of an admin surface.
◆ **STOP AND ASK — production data access (§5.9/§6.3).** Connecting the panel to live production data for the first time requires the user's explicit go-ahead and the read/write scope agreed in writing in `progress.md`. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 9 — Discoverability settings (D9).** Deliberately minimal: the panel is configured `noindex`, excluded from the sitemap (G-CO-091 count reconciliation confirms it), and product analytics are wired only as the register in step 6 allows (`web-analytics`). If part of the surface is public (e.g. a public status view), that part alone gets the indexability pass (G-CO-001).

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-032 | Requirement lint; traceability coverage | Step 1 |
| G-AR-001 / G-AR-002 | Container walk; design document completeness | Step 2 |
| G-DB-001 / G-DB-002 | Schema lint; constraint-presence check | Step 3 |
| G-BE-001 / G-BE-051 | API contract suite; auth test pack | Step 3 |
| G-BE-061 / G-BE-063 / G-BE-064 | Authorization matrix test; client-trust scan; audit-log completeness | Steps 3, 4 |
| G-BE-062 / G-DB-051 | Cross-tenant access test; cross-tenant test suite — multi-tenant only | Step 4 |
| G-FE-131 / G-FE-132 / G-FE-133 / G-FE-134 | Accessible-alternative DOM check; chart message test; axis/label/source inspection; colorblind simulation | Step 3 |
| G-AC-011 / G-AC-012 / G-AC-015 / G-AC-002 | Contrast script; axe-core in CI; WCAG checklist; keyboard walk | Step 3 |
| G-AN-101 / G-AN-102 | Budget assertion (CI or local path); budget-file lint | Step 5 |
| G-LG-001 / G-LG-002 / G-LG-081 | Register coverage; data-map completeness; audit-trail gates | Step 6 |
| G-SE-003 / G-SE-021 / G-SE-022 | OWASP checklist — **0 critical**; API authorization matrix suite; API inventory diff | Step 7 |
| G-SE-041 / G-SE-051 / G-QA-141 / G-QA-021 | Secret scan; vulnerability gate; placeholder sweep; e2e suite green | Step 7 |
| G-QA-051 | Accessibility-testing gates (D8 pass) | Step 7 |
| G-DO-001 / G-DO-071 / G-DO-073 / G-DO-151 | Broken-test drill; external production check; exposure probe; rollback drill | Step 8 |
| G-CO-091 | Sitemap count reconciliation (panel excluded) | Step 9 |

Family summary (§5.6): G-SE-* 0 critical findings; G-QA-* all green; G-AC-* WCAG 2.2 AA pass.

## Failure handling

- **A gate fails:** fix in the owning step, re-run; same failure twice → §6.3 protocol (log, continue unblocked work, batch with options).
- **Authorization or cross-tenant gate fails (G-BE-061/062/063, G-DB-051, G-SE-021):** release-blocking, no waiver path short of the user's explicit agreement after being told plainly what the failure means ("a support agent's account can read another customer's records"). These are P0 defects by definition (QB-01). The panel does not deploy with one open.
- **A chart's data disagrees with its definition:** the chart is wrong, not the definition — unless the definition itself is wrong, in which case `fact-sheet.md` is corrected first, the change logged in `DECISIONS.md`, and every chart using that metric is re-checked. Never quietly adjust a formula in code.
- **Two skills contradict:** §5.7 precedence (security 1, legal 2, accessibility 5 all outrank data-visualisation/design 15); log in `DECISIONS.md`.
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` (§6.3 step 5); security/legal waivers need explicit user agreement.
- **A secret leaks:** revoke/rotate immediately; incident recorded without the value (§5.9 step 4).

## Definition of done

- Deployed behind authentication on a real host; G-DO-071/G-DO-073 green; rollback drill and monitoring live (QB-02).
- Authorization matrix enforced server-side and proven by test for every role; cross-tenant isolation proven if multi-tenant; every mutation audit-logged.
- Every chart and table traces to a metric definition in `fact-sheet.md`; empty states are honest; no demo data anywhere in the shipped build.
- WCAG 2.2 AA checklist complete, including chart alternatives and full keyboard operation.
- Zero P0/P1 defects (QB-01); `progress.md`, `DECISIONS.md`, and `runbook.md` current.
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **OpsBoard**, an internal-plus-customer-admin panel for a small SaaS (roles: support agent, billing admin, customer admin; multi-tenant).

1. Step 0: core loaded; project scaffolded; API credentials listed by name only.
2. Step 1: six screens specified, each with its decision ("refund queue → who approves refunds"); a seventh "engagement overview" screen is cut — no decision named — and the cut is logged.
3. Step 2: roles × resources matrix drafted; user confirms multi-tenant → tenant-isolation gates added.
4. Step 3: API enforces the matrix server-side; the revenue chart is built against its fact-sheet definition (MRR = sum of active subscription amounts, excluding trials).
5. Step 4: cross-tenant test catches a cached query keyed without tenant ID (G-BE-062 fail) — cache key fixed, suite green; audit log verified for refund approvals (G-BE-064).
6. Step 5: the 50k-row events table blows its budget → server-side pagination; G-AN-101 green.
7. Step 6: register records that support agents can view customer emails; export action restricted to billing admins and audit-logged (G-LG-081).
8. Step 7: API inventory diff finds an undocumented debug endpoint left from development — removed, diff clean (G-SE-022); accessibility pass fixes a chart with no text alternative (G-FE-131).
9. Step 8: user approves production-data connection in writing; panel deploys behind SSO; rollback drill passes.
10. Step 9: panel confirmed absent from the sitemap and `noindex` set (G-CO-091). Done.
