# Playbook: SaaS Web App

A multi-user software product sold (or given away) as a service: accounts, a database, a web UI, and usually subscription billing. This is the default playbook — when no other playbook matches a project type on at least two of (payments? accounts? content-led or app-led?), use this one (§5.6 closest-match rule; ties go to SaaS).

## Goal

Ship a production SaaS: real accounts and tenant isolation, a tested API and schema, subscription billing verified in test mode before any live key is touched, WCAG 2.2 AA accessibility, and a monitored deployment with a proven rollback — with zero critical security findings and every QA gate green.

## Departments and order

D1 → D2+D7 → D3+D13+D4+D5 → D11 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation. D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule (they are not in the table's order string); D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | system-design, stack-selection (D2); threat-modelling, owasp (D7) | `bundles/architecture.md`, `bundles/security.md` |
| 3 | frontend-core, design-tokens, component-library (D3); wcag, accessibility-audit (D13); api-building, backend-auth, rbac, validation, rate-limiting (D4); schema-design, migrations, tenant-isolation (D5) | `bundles/frontend.md`, `bundles/accessibility-i18n.md`, `bundles/backend.md`, `bundles/database.md` |
| 4 | payments, subscriptions, webhooks (D11) | `bundles/integrations-payments.md` |
| 4b (conditional) | llm-integration, ai-safety (D17) — only if the product has AI features | `bundles/ai-features.md` |
| 5 | performance-budgets, core-web-vitals (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, legal-documents, cookie-consent, dsar-handling (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | support-ticketing, user-onboarding (D18) — only if the product ships support surfaces | `bundles/customer-experience.md` |
| 7 | security-audit, dependency-safety (D7); placeholder-scan, e2e-testing, test-strategy (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | ci-cd, hosting, reliability, rollback (D6) | `bundles/devops-deployment.md` |
| 9 | technical-seo, web-analytics (D9) | `bundles/seo-content.md` |

Total loaded skills must stay within the §5.3 dependency-depth cap (≤12 at once, excluding core): load per step, unload when the step ends (§5.10).

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — the requirement set with priorities and acceptance criteria (D1).
- `fact-sheet.md` — every public claim, price, and plan name the product will make, with sources (D1). Prices here must mirror the billing configuration (G-PR-063).
- `stack.md` — the chosen stack and the criteria that chose it, recorded before the choice is final (G-AR-023).
- `progress.md` — session log, gate results, blockers; updated every session (§5.10).
- `DECISIONS.md` — architecture decisions and any skill conflicts resolved under §5.7 precedence.
- `ARCHITECTURE.md` — containers, data ownership, failure behavior (step 2 output, started now as a stub).
- `SCHEMA.md` — data invariants the schema gates check against (step 3).
- `SECURITY.md` — threat model summary and the OWASP checklist record (step 2, completed at step 7).
- `.env.example` — every secret by name + purpose, no values (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`. Generate the project from `project-templates` (gate G-PM-001 manifest diff, G-PM-002 unreplaced-token scan). Write the docs above. Load `secrets-management` now — every later step that needs a key follows §5.9.

**Step 1 — Requirements (D1).** Run `requirements-writing`: requirements with testable acceptance criteria, a named Must set, and an explicit out-of-scope list. Populate `fact-sheet.md` with every claim and price the marketing surface will repeat.
◆ **DECISION — is billing actually in scope?** If the product is free with no paid tier, drop step 4 and record the drop in `requirements.md` ("Dropped, with reason") and `DECISIONS.md` (§6.3 step 5). Never build a dormant checkout. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Architecture + security design (D2+D7).** Run `system-design` (containers, data ownership, failure behavior) and `threat-modelling` in the same pass — the design is not final until the threat model has been read against it. Record stack choice in `stack.md` with criteria dated before the decision (G-AR-023).
◆ **DECISION — single-tenant or multi-tenant?** If more than one customer organization will share the database, `tenant-isolation` and `multitenancy-saas` are mandatory in step 3, not optional. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 3 — Build (D3+D13+D4+D5).** Build in this internal order: schema first (invariants in `SCHEMA.md`, migrations reversible), API second (contract-first, `api-building`), auth and authorization with the API (`backend-auth`, `rbac`), throttling shipped with the auth surface (`rate-limiting` — login, signup, and password-reset endpoints are rate-limited from this step, not retrofitted after a review finding), UI last against the real API — never against mock data that hides API gaps. D13 runs inside this step, not after it: tokens pass the contrast script (G-AC-011) before components are built on them, and every screen is built to the WCAG 2.2 AA criterion checklist (G-AC-015).

**Step 4 — Billing (D11).** ◆ **STOP AND ASK — no payment provider chosen (§6.3 step 4).** If `requirements.md` names no provider, stop and ask with concrete options (e.g. "Option A: Stripe — subscription tooling and test clocks; Option B: defer billing and ship the free tier only"). Do not pick a provider silently and do not build against a guessed one. Then: request **test-mode keys only** via the §5.9 handoff; build checkout, subscription lifecycle, and webhook handling; verify with the test-clock lifecycle walk (G-IN-011) and the webhook forgery test (G-IN-051). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
**Step 4b — AI features (D17, conditional).** Only if the product has AI features: `llm-integration` (provider SDK contained behind one wrapper, G-AI-001) and `ai-safety` (red-team injection suite, G-AI-021) become part of the build, and their gates join the step 7 list.

**Step 5 — Performance budgets (D12, explicit step).** Set the budget file with `performance-budgets` before the verification phase: per-route budgets asserted in CI (G-AN-101), budget file linted (G-AN-102). A budget written after the first failing measurement is a waiver, not a budget — record it as one.

**Step 6 — Legal and privacy (D14, explicit step).** Build the processing register and data map (`privacy-laws`), draft Terms/Privacy from the register — never from a template copied off another product — and wire cookie consent so nothing non-essential fires before consent (G-LG-041). The published documents must diff clean against the register (G-LG-031). Data-subject capability is gated in this step, not assumed: the DSAR drill (G-LG-021, `dsar-handling`) runs an access request and an erasure request through the real product flow, so account deletion and data export must exist as working capabilities — self-serve, or a documented request path running on the LG-043 response clock — before this step can pass.
**Step 6b — Support surfaces (D18, conditional).** Only if the product ships help/support: `support-ticketing` intake end-to-end test (G-CX-001) and `user-onboarding` fresh-account walkthrough (G-CX-031) join the gate list.

**Step 7 — Verification (D7+D8).** Full OWASP pass (`owasp` checklist review G-SE-003, ZAP baseline G-SE-001), secrets scan over full git history (G-SE-041), dependency vulnerability gate (G-SE-051), placeholder scan (G-QA-141), end-to-end suite green on the preview deployment (G-QA-021), and the qa-gates meta-checks (G-QA-111 negative control, G-QA-113 waiver/provenance check). **No deployment step starts until every gate in this step passes.**

**Step 8 — Deploy (D6, last build step).** CI/CD pipeline with the broken-test drill proven (G-DO-001), hosting checks against the real production domain (G-DO-071 external production check, G-DO-073 exposure probe), rollback drill in staging before the first production deploy (G-DO-151), monitoring and alerts live (`reliability`).
◆ **STOP AND ASK — go-live switch (§5.9 step 6).** Switching from test to live payment keys, purging test data, and re-pointing webhooks requires the user's explicit approval. The agent prepares the checklist; the user approves the switch. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 9 — Launch surface (D9).** Indexability verified on the production routes (G-CO-001), analytics wired (`web-analytics`), and the fact-sheet claim-trace re-run against the live marketing pages (G-PR-062).

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-032 | Requirement lint; traceability coverage | Step 1 |
| G-PR-061 / G-PR-063 | Fact-sheet template completeness; price mirror diff | Steps 1, 4 |
| G-AR-001 / G-AR-002 | Container-to-deployable walk; design document completeness | Step 2 |
| G-AR-023 | Stack criteria predate the decision | Step 2 |
| G-DB-001 / G-DB-002 | Schema lint; constraint-presence check | Step 3 |
| G-DB-061 | Migration reversibility and diff test | Step 3 |
| G-DB-051 / G-AR-091 / G-AR-092 | Cross-tenant test suite (DB and AR); tenant-key schema check — multi-tenant only | Step 3 |
| G-BE-001 / G-BE-002 | API contract test suite; persistence test per write endpoint | Step 3 |
| G-BE-051 / G-BE-061 | Auth test pack; authorization matrix test | Step 3 |
| G-FE-002 / G-AC-011 / G-AC-012 / G-AC-015 | Accessibility floor scan; palette contrast script; axe-core in CI; per-release WCAG criterion checklist | Step 3 |
| G-IN-001 / G-IN-002 | Payment double-submit test; test-mode purchase and decline walk | Step 4 |
| G-IN-011 | Subscription test-clock lifecycle walk | Step 4 |
| G-IN-051 / G-IN-052 | Webhook forgery test; duplicate-delivery test | Step 4 |
| G-AI-001 / G-AI-021 | LLM SDK containment; red-team injection suite — only with step 4b | Step 4b |
| G-AN-101 / G-AN-102 | CI budget assertion; budget-file lint | Step 5 |
| G-LG-001 / G-LG-002 | Privacy register coverage; data-map completeness | Step 6 |
| G-LG-031 / G-LG-041 | Legal document-vs-register diff; pre-consent network scan | Step 6 |
| G-LG-021 | DSAR drill — access + erasure through the real product flow | Step 6 |
| G-SE-001 / G-SE-003 | ZAP baseline scan; OWASP Top 10 checklist review — **0 critical findings** | Step 7 |
| G-SE-041 / G-SE-051 | Full-history secret scan; CI vulnerability gate | Step 7 |
| G-QA-141 / G-QA-021 / G-QA-111 | Placeholder static sweep; e2e suite green; negative-control meta-gate | Step 7 |
| G-DO-001 / G-DO-071 / G-DO-151 | Broken-test drill; external production check; staging rollback drill | Step 8 |
| G-CO-001 / G-PR-062 | Promotion indexability diff; fact-sheet claim-trace audit | Step 9 |

Family summary (§5.6): G-SE-* 0 critical findings; G-QA-* all green; G-IN-* test mode verified; G-AC-* WCAG 2.2 AA pass.

## Failure handling

- **A gate fails:** the owning step fixes the cause and re-runs the gate. Never edit the gate, weaken the check, or mark it passed in `progress.md` without the run. The same failure twice with the same approach → stop retrying and follow §6.3 (log the blocker in `progress.md`, continue all unblocked work, batch blockers into one message with a concrete option each).
- **Billing gate fails in test mode (e.g. G-IN-011):** billing does not ship. Ship everything else only if the user agrees to the §6.3 step 4 option "defer billing, ship free tier"; otherwise the release waits. Never debug billing against live keys.
- **Two skills contradict** (e.g. D12 budget vs D7 CSP headers): §5.7 precedence decides — security (rank 1) beats performance (rank 12) — and the conflict is logged in `DECISIONS.md`. Precedence never excuses skipping a gate; the gate is re-run against the winning rule.
- **A gate is itself wrong** (tests a feature the product does not have, or contradicts another gate): record a waiver in `progress.md` and `DECISIONS.md` — which gate, why it cannot pass, what was checked instead — and flag it as a repo gap (§6.3 step 5). Waivers on security, legal, or Real Content gates need the user's explicit agreement.
- **A secret leaks** (pasted in chat, committed, logged): tell the user immediately to revoke/rotate it, name the exact secret, and record the incident (name + date + rotation status, never the value) in `progress.md` (§5.9 step 4).

## Definition of done

- Deployed on a real host at a real domain; G-DO-071 passes from outside the network; monitoring and alerts live; a staging rollback drill (G-DO-151) and a backup restore drill are on record (QB-02).
- All gates in the table above pass, with results recorded in `progress.md`; zero P0 and zero P1 defects open (QB-01).
- Billing, if in scope, verified end-to-end in test mode (purchase, decline, renewal, cancellation, webhook replay) before the user-approved live switch.
- No placeholder or fake content anywhere: G-QA-141 clean and every public claim traces to `fact-sheet.md` (G-PR-062).
- `progress.md`, `DECISIONS.md`, `runbook.md`, and `handover.md` are current enough that a fresh agent could resume from them alone (§5.10).
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **TaskBoard**, a team task manager with a free tier and a paid Pro plan.

1. Step 0: core bundle loaded; project scaffolded from templates; `progress.md` opened; secrets list drafted (database URL, Stripe test keys, email provider key).
2. Step 1: 24 requirements written, 9 marked Must; `fact-sheet.md` records the two plan prices and the "unlimited projects on Pro" claim with its source.
3. Step 2: system design lands on three containers (web, API, Postgres) + a worker; threat model flags tenant data leakage as the top risk → multi-tenant confirmed.
4. Step 3: schema with tenant-key on every table (G-AR-092 pass); API contract suite green (G-BE-001); cross-tenant suite proves tenant A cannot read tenant B (G-DB-051); tokens pass contrast script before the board UI is built (G-AC-011).
5. Step 4: no provider was named in requirements → agent stops and asks; user picks Stripe (Option A). Test-clock walk carries a trial through renewal, a failed payment, and cancellation (G-IN-011 pass).
6. Step 5: budgets set — 200 KB JS on the board route, LCP 2.5 s — asserted in CI (G-AN-101).
7. Step 6: processing register covers accounts, billing, and analytics; consent scan shows no tracker fires pre-consent (G-LG-041).
8. Step 7: ZAP baseline finds one medium header issue, fixed and re-scanned; secret scan over history clean (G-SE-041); placeholder sweep clean (G-QA-141).
9. Step 8: pipeline deploys to production; rollback drill in staging took 3 minutes (G-DO-151); user approves the test→live key switch from the go-live checklist.
10. Step 9: production routes indexable (G-CO-001); claim-trace re-run — every price on the pricing page matches `fact-sheet.md` and the Stripe configuration (G-PR-063). Done.
