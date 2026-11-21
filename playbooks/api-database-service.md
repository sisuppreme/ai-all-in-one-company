# Playbook: API + Database Service

A service whose interface is an API, not pages: other software is the user. There is no UI to hide behind — the contract, the data model, and the authorization layer are the entire product.

## Goal

Ship an API whose published contract is proven by consumer contract tests in the deploy pipeline, whose schema invariants are enforced by the database itself (not by hope in the handler code), whose every endpoint is authenticated, authorized, and rate-limited, and which deploys with CI/CD, monitoring, and a tested rollback.

## Departments and order

D1 → D2+D7 → D4+D5 → D7+D8 → D6 — exactly as the §5.6 table; no deviation. There is deliberately **no D3/D13 step** (no UI exists; if a UI is later added, it is built under the Dashboard playbook against this service's contract) and **no D9 step** (an API has no search surface; its documentation lives in step 3). D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule — the service ships to production and processes data, so the exception that applies to Landing Pages does not apply here. D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | system-design, api-architecture, api-versioning (D2); threat-modelling, owasp, api-security (D7) | `bundles/architecture.md`, `bundles/security.md` |
| 3 | api-building, backend-auth, rbac, validation, rate-limiting (D4); schema-design, migrations, indexing (D5); api-documentation (D2) | `bundles/backend.md`, `bundles/database.md`, `bundles/architecture.md` |
| 4 | contract-testing, integration-testing (D8 — stood up here, enforced at step 7) | `bundles/qa-testing.md` |
| 4b (conditional) | llm-integration, ai-safety (D17) — only if the service exposes AI-backed endpoints | `bundles/ai-features.md` |
| 5 | performance-budgets, apm, monitoring (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, data-residency, legal-documents (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | support-ticketing, status-communications (D18) — only if the service has external consumers who need support/status surfaces | `bundles/customer-experience.md` |
| 7 | security-audit, dependency-safety (D7); qa-gates, placeholder-scan (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | ci-cd, hosting, reliability, rollback (D6) | `bundles/devops-deployment.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — consumers, use cases, the resources and operations in scope, non-functional targets (latency, availability, data retention).
- `fact-sheet.md` — the service's verifiable commitments: rate limits, retention periods, regions, uptime target — the numbers that will appear in docs and status pages, each with its operational source.
- `stack.md` — stack and database choice with dated criteria (G-AR-023).
- `progress.md`, `DECISIONS.md` — session log and decision record.
- `API_CONTRACTS.md` — the contract source of truth: resources, operations, request/response schemas, error model, versioning policy. Written in step 1 as a draft, finalized in step 2, and never edited after consumers exist without a versioning decision in `DECISIONS.md`.
- `ARCHITECTURE.md` — components, data ownership, failure behavior.
- `SCHEMA.md` — the invariants the database must enforce (uniqueness, referential integrity, money/quantity types, tenant keys if applicable).
- `SECURITY.md` — one file with two named sections: a vulnerability-reporting section (how to report a vulnerability, per PROJECT_ANATOMY Appendix A) and the project's security-design section (authentication scheme, authorization model, threat model summary).
- `.env.example` — database URL, signing keys, provider credentials by name + purpose (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above; load `secrets-management` before any credential exists.

**Step 1 — Requirements (D1).** Name the consumers explicitly — "the public" is not a consumer. For each consumer: what they read, what they write, what breaks for them if the service is down or slow. Those answers set the versioning policy and the step 5 budgets.
◆ **DECISION — who may call this API?** First-party only, named partners, or public sign-up? The answer decides the auth scheme (step 2), rate-limit tiers (step 3), and whether step 6b exists. If unspecified, ask (§6.3 step 4). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Architecture + security design (D2+D7).** API style and versioning policy decided and recorded (`api-architecture`, `api-versioning`); the error model is part of the contract from day one (one error shape, stable codes). Threat model weighted to API-specific failures: broken object-level authorization, excessive data exposure, mass assignment, injection. Auth scheme chosen here (tokens/OAuth per `backend-auth` and, for third-party consumers, `oauth-sso` from D11 via `bundles/integrations-payments.md`).

**Step 3 — Build (D4+D5).** Schema first: invariants in `SCHEMA.md` become database constraints, checked by G-DB-001/G-DB-002; money and quantities in exact types (G-DB-003 type audit). Handlers second, contract-first: every endpoint validates at the boundary (G-BE-021 boundary test pack, G-BE-023 mass-assignment probe), recomputes trusted values server-side (G-BE-004), and is idempotent where a retry could double-apply (G-BE-003 duplicate-submit test). Rate limiting is built, not bolted on (G-BE-151 burst test, G-BE-152 spoof test). Documentation is generated/verified against the running service in this step (`api-documentation`) — docs that describe endpoints the service does not have fail the API inventory diff at step 7 (G-SE-022).

**Step 4 — Contract testing stood up (D8).** Consumer contracts are captured as tests and published (G-QA-083 publication completeness), and the deploy pipeline is wired so `can-i-deploy` is a real gate, not a badge (G-QA-084 pipeline wiring inspection). From this step on, a contract-breaking change fails the provider build or requires a recorded versioning decision — never a silent break.
**Step 4b — AI endpoints (D17, conditional).** AI-backed endpoints are built under `llm-integration` + `ai-safety` (G-AI-001 SDK containment, G-AI-021 injection suite, G-AI-004 fault-injection bounds — a provider outage must degrade the endpoint, not hang it).

**Step 5 — Performance budgets (D12, explicit step).** Budgets are latency and error budgets per endpoint class, asserted in CI and monitored in production (G-AN-101 adapted to p95 latency assertions per endpoint class; `apm` and `monitoring` wired so a budget breach pages a human, G-AN-091 apm gates). A service without latency budgets has no definition of "slow", and therefore no definition of done.

**Step 6 — Legal and privacy (D14, explicit step).** Register of what the service stores and processes (G-LG-001, G-LG-002 data-map completeness), retention enforced as code (deletion jobs), data-residency commitments checked against where the database actually runs (G-LG-011 data-residency gates), and consumer-facing terms/DPA drafted from the register (G-LG-031).

**Step 7 — Verification (D7+D8).** The API security suite in full: authorization matrix suite (G-SE-021), API inventory diff (G-SE-022), API scan plus SSRF probe (G-SE-024), OWASP checklist (G-SE-003) — 0 critical; contract gate live (G-QA-081 can-i-deploy, G-QA-082 seeded-break negative control proving the gate actually bites); secret scan (G-SE-041); dependency gate (G-SE-051); placeholder sweep over docs and seed fixtures (G-QA-141; scan rendered output, not source). **No deployment until green.**

**Step 8 — Deploy (D6, last build step).** CI/CD with the contract gate in the pipeline (G-DO-001 broken-test drill, G-DO-004 gating-job integrity scan — a `can-i-deploy` step with `continue-on-error` is a failed gate), migrations applied with their down-paths checked (G-DO-153 migration down-path check), production checks (G-DO-071, G-DO-072 readiness honesty test — the health endpoint must fail when the database is down, not report green), rollback drill (G-DO-151), monitoring and alerts live (`reliability`, G-DO-131 SLO inventory audit).
◆ **STOP AND ASK — production credentials and data (§5.9/§6.3).** First connection to a production database, and any migration against production data, requires the user's explicit go-ahead with the backup verified first (restore drill current, G-DO-134). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-032 | Requirement lint; traceability coverage | Step 1 |
| G-AR-021 / G-AR-023 | Manifest-to-ADR coverage; stack criteria predate the decision | Step 2 |
| G-DB-001 / G-DB-002 / G-DB-003 | Schema lint; constraint-presence check; type audit | Step 3 |
| G-DB-061 / G-DB-063 | Migration reversibility; from-empty build | Step 3 |
| G-BE-001 / G-BE-002 / G-BE-003 / G-BE-004 | Contract test suite; persistence test per write endpoint; duplicate-submit test; trusted-value audit | Step 3 |
| G-BE-021 / G-BE-023 | Boundary test pack; mass-assignment probe | Step 3 |
| G-BE-051 / G-BE-061 | Auth test pack; authorization matrix test | Step 3 |
| G-BE-151 / G-BE-152 | Rate-limit burst test; spoof test | Step 3 |
| G-QA-081 / G-QA-082 / G-QA-083 / G-QA-084 | can-i-deploy deploy gate; seeded-break negative control; publication completeness; pipeline wiring inspection | Steps 4, 7 |
| G-AN-101 / G-AN-091 | Budget assertion (latency budgets in CI); apm gates | Step 5 |
| G-LG-001 / G-LG-002 / G-LG-011 / G-LG-031 | Register coverage; data-map completeness; data-residency gates; document-vs-register diff | Step 6 |
| G-SE-003 / G-SE-021 / G-SE-022 / G-SE-024 | OWASP checklist — **0 critical**; API authorization matrix suite; API inventory diff; API scan + SSRF probe | Step 7 |
| G-SE-041 / G-SE-051 / G-QA-141 | Secret scan; vulnerability gate; placeholder sweep | Step 7 |
| G-DO-001 / G-DO-004 / G-DO-153 | Broken-test drill; gating-job integrity scan; migration down-path check | Step 8 |
| G-DO-071 / G-DO-072 / G-DO-151 / G-DO-131 | External production check; readiness honesty test; rollback drill; SLO inventory audit | Step 8 |

Family summary (§5.6): G-SE-* 0 critical findings; G-QA-* contract tests green.

## Failure handling

- **A gate fails:** fix in the owning step, re-run; same failure twice → §6.3 (log in `progress.md`, continue unblocked work, batch blockers with concrete options).
- **Contract gate fails (G-QA-081):** the change does not deploy. The options are exactly two: make the change backward-compatible, or ship it as a new version under the recorded versioning policy with consumer notice. "Deploy anyway, consumers will adapt" is not an option, and bypassing the gate via pipeline edit fails G-DO-004 on the next run.
- **Authorization or inventory gate fails (G-SE-021, G-SE-022):** P0 defect (QB-01). An undocumented endpoint or a broken object-level check means the service's actual surface is unknown — nothing deploys until the inventory and the running service agree.
- **Migration down-path fails (G-DO-153):** the migration is rewritten until it is reversible, or split so the irreversible part is a separate, user-approved step with a verified backup. Irreversible-by-default is not accepted.
- **Two skills contradict:** §5.7 precedence (security 1, legal 2, data integrity 8 above backend convenience 9 and performance 12); log in `DECISIONS.md`.
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` (§6.3 step 5); security/legal waivers need explicit user agreement.
- **A secret leaks:** revoke/rotate immediately; incident recorded without the value (§5.9 step 4).

## Definition of done

- Deployed on a real host; external production check and readiness honesty test green; monitoring, SLOs, and alerts live; rollback and migration down-paths proven (QB-02).
- The published contract and the running service are identical (inventory diff clean), and the deploy pipeline refuses contract-breaking changes (can-i-deploy enforced, negative control passing).
- Every endpoint authenticated, authorized per the matrix, validated at the boundary, and rate-limited — proven by the step 7 suites, not by inspection.
- Schema invariants enforced by the database; a from-empty build reproduces the schema exactly (G-DB-063).
- Zero P0/P1 defects (QB-01); documentation matches the service; `progress.md`, `DECISIONS.md`, `runbook.md`, and `handover.md` current.
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **Ledger API**, a double-entry bookkeeping API consumed by two first-party apps.

1. Step 0: core loaded; project scaffolded; database URL and token-signing key listed by name in `.env.example`.
2. Step 1: consumers named (web app, mobile app); requirements fix resources — accounts, entries, balances — and a p95 target of 150 ms for reads.
3. Step 2: versioning policy recorded (URL major version, additive changes free, removals only at major bumps); threat model puts broken object-level authorization at the top.
4. Step 3: schema enforces balanced entries (debits = credits per transaction) as a database constraint (G-DB-002); the type audit moves amounts from float to numeric (G-DB-003).
5. Step 3: duplicate-submit test proves a retried "post entry" creates one entry, not two (G-BE-003); mass-assignment probe confirms a client cannot set `balance` directly (G-BE-023).
6. Step 4: both consumers' contracts published; can-i-deploy wired into the pipeline (G-QA-083, G-QA-084).
7. Step 5: latency budgets asserted per endpoint class; APM shows the balance endpoint breaching at p95 210 ms → missing index added (G-DB-081 indexing gates), budget green.
8. Step 6: register records 7-year retention for ledger data (legal requirement, sourced); deletion job exempts ledger tables and covers user profile data only.
9. Step 7: API inventory diff finds an undocumented `/admin/reseed` endpoint from scaffolding — removed; seeded-break control proves can-i-deploy blocks a field removal (G-QA-082).
10. Step 8: user approves the production migration after the restore drill is verified current; deploy runs migrations with down-paths checked (G-DO-153); readiness test confirms the health endpoint fails when the database is stopped (G-DO-072). Done.
