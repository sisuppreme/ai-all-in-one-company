# Playbook — Internal CRUD / Admin Tool

## Goal

Build an internal tool a small team uses to run operations: create/read/update/delete over business data, role-based access, searchable tables and dashboards, and a complete audit trail — boring on purpose, correct by construction, and safe to hand to non-technical staff.

## Departments + order

Step 0 (always-on core) → D1 → D2+D7 → D3+D13+D4+D5 → D14 → D12 → D7+D8 → D6

This follows the brief's order for this type (no D9 — an internal tool has no public surface to optimize), with D14 and D12 as explicit steps: the tool holds business and often personal data, and its tables must stay fast on real data volumes.

## Skills to load

Load this playbook's bundle first: `bundles/internal-crud-admin-tool.md`. Then, per step:

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| requirements-writing | `bundles/product-requirements.md` |
| system-design | `bundles/architecture.md` |
| rbac, api-building, admin-tools | `bundles/backend.md` |
| frontend-core, data-visualisation | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| schema-design, migrations | `bundles/database.md` |
| auth-hardening, owasp | `bundles/security.md` |
| privacy-laws, audit-trails | `bundles/legal-privacy.md` |
| performance-budgets, monitoring | `bundles/analytics-observability.md` |
| placeholder-scan | `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |

Conditional: if the organization requires single sign-on, add a D11 step before D7+D8 (oauth-sso) — SSO is an integration, and it changes the auth design, so it is decided at step 2, not bolted on later. If the tool gains AI features (auto-tagging, summarization), add a D17 step before D7+D8. If non-technical staff need in-product help surfaces, add a D18 step (help-center, user-onboarding) before D6.

## Docs to write first

1. `fact-sheet.md` — what data the tool manages, who the staff roles are, and the real data volumes (rows today, growth). Volumes come from the user or the existing data, never guessed.
2. Role matrix draft — each role × each entity × allowed actions; rbac formalizes it at build time, and the authorization matrix test is generated from it.
3. `progress.md` — playbook trace and gate results.
4. Data classification note — which fields are personal or sensitive; this drives the D14 step and the audit-trail scope.

The full mandated set for this type is `templates/mandated-manifest-internal-crud-admin-tool.txt`, which governs (G-PM-001); the list above is the hand-written starting subset, not the whole set. Mandated files that do not apply at this tool's scale are recorded not-applicable with a reason in the generation record (PM-001) — never silently omitted.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; project files, `progress.md`, secrets baseline.
1. **D1 requirements.** requirements-writing, scoped to operations: the entities, the workflows staff actually perform (including bulk actions and exports), and what "search" must find. *Decision point: if the role list or the data classification is unclear, stop and ask (§6.3) — both are cheaper to fix now than after the schema and permission model exist.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D2+D7 design.** system-design kept deliberately small: one deployable, server-rendered or SPA admin UI, one API, one database (G-AR-001). auth-hardening: staff authentication, session policy, and the privilege-change drill (G-SE-034) designed up front. *Decision point: SSO or local accounts — if the organization has an identity provider, stop and confirm; retrofitting SSO after local auth ships is a rework of D4 and D7.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
3. **D3+D13+D4+D5 build.** schema-design with real constraints (G-DB-001, G-DB-002); migrations reversible (G-DB-061). api-building: every write endpoint persists and proves it (G-BE-002), duplicate submits are safe (G-BE-003). rbac: server-side enforcement generated from the role matrix (G-BE-061 authorization matrix test, G-BE-063 client-trust scan — hiding a button in the UI is not authorization). admin-tools for the operational extras: impersonation is banned unless audited, exports are permissioned, destructive actions are confirmable and reversible where the data allows (G-BE-081 limited-role denial test, G-BE-082 audit-completeness test, G-BE-084 persistence round-trip). Frontend: data-visualisation for tables/dashboards (G-FE-131 accessible-alternative DOM check, G-FE-133 axis/label/source inspection). D13 in the same step — staff tools are used all day; G-AC-001 and keyboard-complete workflows (G-AC-002) are requirements, not polish.
4. **D14 legal/privacy.** privacy-laws register for the personal data the tool holds (G-LG-001, G-LG-002). audit-trails: every create/update/delete and every permission change is recorded with actor and before/after where the data class requires it (G-LG-081 action-coverage test, G-LG-082 tamper test, G-LG-085 retention conformance).
5. **D12 performance.** performance-budgets sized for internal use, asserted per page template (G-AN-101 — CI where a pipeline exists, otherwise the gate's local assertion path with the substitution recorded); table queries paginated and indexed for the real volumes in the fact-sheet so the screens can meet those budgets; monitoring on error rate and slow queries (G-AN-051).
6. **D7+D8 verification.** Security: G-SE-001 (ZAP baseline, 0 criticals — internal is not a synonym for unexposed), G-SE-031 auth abuse pack, G-BE-083 PAN-pattern scan if any payment-adjacent data is displayed. QA: G-QA-111; placeholder-scan G-QA-141 (scan rendered output, not source) — seeded demo rows are labeled test data and never mixed into the production dataset.
7. **D6 deploy.** ci-cd (G-DO-001); hosting on the organization's network or access-controlled host (G-DO-071 external production check, G-DO-073 exposure probe — the tool must not be reachable from the public internet unless that was an explicit, recorded decision).

## Gates that must pass

- **Authorization:** G-BE-061, G-BE-063, G-BE-081 — the role matrix holds; no client-side-only enforcement.
- **Data correctness:** G-BE-002, G-BE-003, G-BE-084, G-DB-001, G-DB-061.
- **Audit:** G-LG-081, G-LG-082, G-LG-085 — every sensitive action traceable to an actor.
- **Security:** G-SE-001 (0 critical findings), G-SE-031, G-SE-034.
- **Accessibility:** G-AC-001, G-AC-002 — WCAG 2.2 AA pass.
- **Privacy:** G-LG-001, G-LG-002.
- **QA:** G-QA-111, G-QA-141 — all green.
- **Performance/deploy:** G-AN-101, G-DO-001, G-DO-071, G-DO-073.

## Failure handling

- **Authorization matrix test fails (G-BE-061):** stop feature work. A role reaching data or actions outside the matrix is the highest-severity defect class in an internal tool; fix the enforcement point, re-run the full matrix, and check sibling endpoints for the same pattern.
- **Audit-coverage test fails (G-LG-081):** the unaudited action does not ship. Add the trail entry at the service layer (not per-screen, where it will be missed again) and re-run.
- **Exposure probe finds the tool publicly reachable (G-DO-073) without a recorded decision:** restrict access immediately and record the incident in `progress.md` before any further deploy.
- **Table performance fails on realistic data (G-AN-101):** fix with pagination/indexing per schema-design; never by raising the budget to fit the query.
- **Any other gate fails:** fix in the owning department, re-run, record both results in `progress.md`.

## Definition of done

Role matrix enforced server-side and fully tested; every sensitive action audit-trailed and tamper-evident; CRUD proven persistent and duplicate-safe; accessible to keyboard and screen-reader users; reachable only by the intended audience; deployed (G-DO-071) with all gates above green. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists.

## Worked mini-example — order-support tool for a small e-commerce team

1. Core loaded; fact-sheet records 3 roles (support, supervisor, admin), ~18k orders, personal data = customer names, addresses, phone numbers.
2. D1 scopes the workflows: find order, issue refund request (supervisor approves), edit address, export daily list.
3. D2 keeps it small: one app, one database; local auth chosen — the org has no IdP (decision recorded, §6.3 not triggered).
4. Build: refund action exists in the API but G-BE-061 shows support role can call it directly → enforcement moved server-side, matrix green.
5. admin-tools: address edits write before/after to the audit trail (G-LG-081 passes); exports restricted to supervisor+ (G-BE-081).
6. data-visualisation: orders table gets an accessible alternative and labeled axes on the volume chart (G-FE-131, G-FE-133).
7. D14: privacy register lists the three personal-data fields and a 2-year retention; G-LG-085 conformance check passes.
8. D12: the orders search at 18k rows exceeds budget → composite index added per schema-design; G-AN-101 green.
9. D7+D8: G-SE-001 clean; G-QA-141 confirms the 200 seeded demo orders live only in the test seed.
10. Deploy behind the company VPN; G-DO-073 confirms no public exposure; G-DO-071 verifies the live tool.
