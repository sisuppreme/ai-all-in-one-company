# Playbook: E-Commerce Store

A storefront that sells products: catalog, cart, checkout, payment, fulfillment, refunds. Accounts may be optional (guest checkout), but payments are never optional — if the project takes money for goods, this playbook governs it.

## Goal

Ship a store where the money path is provably correct in test mode before launch: checkout, payment webhooks, refunds, and invoice totals all verified; no card data ever touches the server; catalog and prices on the page mirror the source of truth; WCAG 2.2 AA; zero critical security findings; every QA gate green.

## Departments and order

D1 → D2+D7 → D3+D13+D4+D5 → D11 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation. D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule; D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | system-design, stack-selection (D2); threat-modelling, owasp, pci-compliance (D7) | `bundles/architecture.md`, `bundles/security.md` |
| 3 | frontend-core, design-tokens, forms (D3); wcag, accessibility-audit (D13); api-building, backend-auth, validation (D4); schema-design, migrations (D5) | `bundles/frontend.md`, `bundles/accessibility-i18n.md`, `bundles/backend.md`, `bundles/database.md` |
| 4 | payments, webhooks, refunds-disputes, invoicing-tax (D11) | `bundles/integrations-payments.md` |
| 4b (conditional) | llm-integration, ai-safety (D17) — only for AI features such as generated product descriptions or a shopping assistant | `bundles/ai-features.md` |
| 5 | performance-budgets, core-web-vitals (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, legal-documents, cookie-consent (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | support-ticketing, help-center (D18) — only if the store ships support surfaces | `bundles/customer-experience.md` |
| 7 | security-audit, dependency-safety (D7); placeholder-scan, e2e-testing (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | ci-cd, hosting, reliability, rollback (D6) | `bundles/devops-deployment.md` |
| 9 | technical-seo, structured-data, copywriting (D9) | `bundles/seo-content.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — catalog, cart, checkout, fulfillment, and returns requirements with acceptance criteria.
- `fact-sheet.md` — prices, shipping terms, return window, and every claim the storefront will print. Page prices must mirror this sheet and the provider catalog (G-PR-063).
- `stack.md` — stack and storefront platform choice with dated criteria (G-AR-023).
- `progress.md`, `DECISIONS.md` — session log and decision record.
- `ARCHITECTURE.md` — containers, order state machine, data ownership.
- `SCHEMA.md` — order, payment, and inventory invariants (an order total is never stored without its line items; stock never goes negative).
- `PAYMENT_SECURITY.md` — the PCI scope statement: which SAQ applies and why no card data reaches the server (step 2, verified at step 7).
- `.env.example` — provider test keys, webhook signing secret, email credentials — names and purposes only (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above; load `secrets-management` before any provider account is touched.

**Step 1 — Requirements (D1).** Requirements for catalog, cart, checkout, fulfillment, refunds, and the store's legal promises (delivery times, return window) — each promise goes into `fact-sheet.md` with its operational source, or it does not go on the site.
◆ **DECISION — physical goods, digital goods, or both?** Physical goods pull in shipping, tax-by-destination, and inventory; digital goods pull in delivery/entitlement and different tax treatment. The answer scopes step 3's schema and step 4's tax configuration. If the user has not said, ask (§6.3 step 4) — do not build both by default. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Architecture + security design (D2+D7).** System design with the order lifecycle as an explicit state machine (cart → pending payment → paid → fulfilled → refunded/closed, with no transition that skips payment confirmation). Threat model plus `pci-compliance`: choose a hosted/redirect checkout or provider elements so raw card numbers never reach the server, and record the SAQ scope in `PAYMENT_SECURITY.md`.

**Step 3 — Build (D3+D13+D4+D5).** Schema first (orders, line items, inventory, idempotency keys on every write), API second, storefront last against the real API. Prices are always recomputed server-side from the catalog — a total sent by the client is never trusted (G-BE-004 trusted-value audit). Checkout forms pass the forms gates (G-FE-121 axe form rules, G-FE-122 keyboard-only submit, G-FE-123 double-submit). D13 runs inside the step: contrast script on tokens (G-AC-011), criterion checklist per screen (G-AC-015).

**Step 4 — Money path (D11).** ◆ **STOP AND ASK — no payment provider chosen (§6.3 step 4).** Ask with concrete options (e.g. "Option A: Stripe hosted checkout — smallest PCI scope; Option B: defer payments and ship a catalog with ordering by inquiry"). Never guess. With test-mode keys only (§5.9): build checkout (G-IN-001 double-submit, G-IN-002 purchase + decline walk), webhook handling as the *only* source of payment truth (G-IN-051 forgery test, G-IN-052 duplicate delivery, G-IN-054 reconciliation-before-fulfillment), refunds (G-IN-021 refund agreement test), and invoicing with totals recomputed by script (G-IN-031) and no tax rate hardcoded in code (G-IN-034). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
**Step 4b — AI features (D17, conditional).** AI-generated product copy is drafted content, not fact: every generated description passes the D9 claim checks in step 9 against `fact-sheet.md`, and `ai-safety` gates (G-AI-021) apply to any customer-facing assistant.

**Step 5 — Performance budgets (D12, explicit step).** Budgets for catalog, product, and checkout routes asserted in CI (G-AN-101). Checkout gets the strictest budget: a slow checkout is lost revenue, and the budget is set before the first measurement, not after.

**Step 6 — Legal and privacy (D14, explicit step).** Processing register (accounts, orders, marketing consent), Terms/Privacy/returns documents drafted from the register and diffed clean against it (G-LG-031), cookie consent with the pre-consent network scan (G-LG-041) — stores are heavy tracker users, so this gate fails often and is fixed, never waived silently.

**Step 7 — Verification (D7+D8).** OWASP pass (G-SE-001, G-SE-003 — 0 critical), PCI checks (G-SE-121 PAN-pattern scan over code and logs, G-SE-122 checkout integration review, G-SE-124 SAQ currency), card-data absence scan (G-IN-004), full-history secret scan (G-SE-041), dependency gate (G-SE-051), placeholder sweep (G-QA-141; scan rendered output, not source), and the provider test-mode decline suite inside the e2e run (G-QA-023). **No deployment until this step is fully green.**

**Step 8 — Deploy (D6, last build step).** Pipeline (G-DO-001), production checks (G-DO-071, G-DO-073), rollback drill (G-DO-151), monitoring and order-flow alerts (`reliability`).
◆ **STOP AND ASK — go-live switch (§5.9 step 6).** Live keys, webhook re-pointing to production endpoints, and test-order purging happen only on the user's explicit approval, from the prepared checklist. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 9 — Launch surface (D9).** Product structured data validated against the visible page (G-CO-081 CI schema validation, G-CO-082 markup-vs-visible diff — a price in JSON-LD that differs from the page price fails), indexability (G-CO-001), and a final claim-trace over prices and promises (G-PR-062, G-PR-063).

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-032 | Requirement lint; traceability coverage | Step 1 |
| G-PR-061 / G-PR-063 | Fact-sheet completeness; price mirror diff | Steps 1, 9 |
| G-AR-001 / G-AR-002 / G-AR-023 | Container walk; design document completeness; stack criteria predate decision | Step 2 |
| G-DB-001 / G-DB-002 / G-DB-061 | Schema lint; constraint-presence; migration reversibility | Step 3 |
| G-BE-001 / G-BE-004 | API contract suite; trusted-value audit (server-side totals) | Step 3 |
| G-FE-121 / G-FE-122 / G-FE-123 | Form axe rules; keyboard-only submit; double-submit test | Step 3 |
| G-AC-011 / G-AC-012 / G-AC-015 | Contrast script; axe-core in CI; WCAG criterion checklist | Step 3 |
| G-IN-001 / G-IN-002 / G-IN-004 | Checkout double-submit; test-mode purchase + decline walk; card-data absence scan | Step 4 |
| G-IN-051 / G-IN-052 / G-IN-054 / G-IN-055 | Webhook forgery; duplicate delivery; reconciliation-before-fulfillment; signing-secret scan | Step 4 |
| G-IN-021 / G-IN-023 | Refund agreement test; refund/dispute reconciliation diff | Step 4 |
| G-IN-031 / G-IN-034 | Invoice totals recomputation; no-rate-in-code scan | Step 4 |
| G-AN-101 / G-AN-102 | CI budget assertion; budget-file lint | Step 5 |
| G-LG-001 / G-LG-031 / G-LG-041 | Register coverage; document-vs-register diff; pre-consent network scan | Step 6 |
| G-SE-001 / G-SE-003 | ZAP baseline; OWASP Top 10 checklist — **0 critical findings** | Step 7 |
| G-SE-121 / G-SE-122 / G-SE-124 | PAN-pattern scan; checkout integration review; SAQ currency check | Step 7 |
| G-SE-041 / G-SE-051 / G-QA-141 / G-QA-023 | Secret scan; vulnerability gate; placeholder sweep; test-mode decline suite | Step 7 |
| G-DO-001 / G-DO-071 / G-DO-151 | Broken-test drill; external production check; rollback drill | Step 8 |
| G-CO-001 / G-CO-081 / G-CO-082 | Indexability diff; structured-data validation; markup-vs-visible diff | Step 9 |

Family summary (§5.6): G-SE-* 0 critical findings; G-QA-* all green; G-IN-* checkout + refunds verified in test mode; G-AC-* WCAG 2.2 AA pass.

## Failure handling

- **A gate fails:** fix the cause in the owning step and re-run. Never edit the gate or record a pass without the run. Same failure twice → §6.3: log in `progress.md`, continue unblocked work, batch blockers with concrete options.
- **A webhook gate fails (G-IN-051/052/054):** the store does not open. Fulfillment driven by anything except verified, reconciled webhooks is the classic double-ship/no-ship bug; there is no partial credit and no waiver for these gates without the user's explicit agreement (security/money path, §5.7 ranks 1 and 11).
- **Refund or totals gates fail (G-IN-021, G-IN-031):** stop the release. A store that cannot refund correctly or whose invoices do not recompute is not launched "to fix later" — money defects compound daily.
- **Two skills contradict:** §5.7 precedence decides (security 1, legal 2, payments correctness 11 above performance 12 and design 15); log in `DECISIONS.md`; re-run the affected gate against the winning rule.
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` with what was checked instead (§6.3 step 5); security/legal/Real Content waivers need explicit user agreement.
- **A secret leaks:** immediate revoke/rotate instruction to the user, incident recorded without the value (§5.9 step 4).

## Definition of done

- Live on a real host and domain; G-DO-071 green from outside; monitoring, alerts, and a recorded rollback + restore drill (QB-02).
- The full money path proven in test mode before the approved live switch: purchase, decline, duplicate webhook, forged webhook rejected, refund, invoice recompute.
- Zero P0/P1 defects (QB-01); all gates above pass with results in `progress.md`.
- No card data in code, logs, or database (G-IN-004, G-SE-121 clean); SAQ scope documented and current.
- Every price and promise on the storefront traces to `fact-sheet.md` and mirrors the provider catalog (G-PR-062, G-PR-063); no placeholder products, reviews, or testimonials (G-QA-141, G-CO-063 evidence register for any testimonial used).
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **Harbor & Thread**, a 40-product apparel store, physical goods, guest checkout allowed.

1. Step 0: core loaded; project scaffolded; secrets listed (Stripe test keys, webhook signing secret, transactional email key).
2. Step 1: requirements fix physical goods + guest checkout; `fact-sheet.md` records prices, "free shipping over $75", and a 30-day return window — each traced to the operations decision that backs it.
3. Step 2: order state machine designed; PCI scope set to SAQ-A via hosted checkout; `PAYMENT_SECURITY.md` written.
4. Step 3: schema enforces non-negative stock and server-computed totals (G-BE-004); checkout form passes keyboard-only submit (G-FE-122).
5. Step 4: provider already named (Stripe) — test-mode purchase and decline walk pass (G-IN-002); a forged webhook is rejected (G-IN-051); the same paid event delivered twice creates exactly one order (G-IN-052).
6. Step 5: checkout route budgeted at 170 KB JS / LCP 2.5 s, asserted in CI (G-AN-101).
7. Step 6: pre-consent scan catches an analytics tag firing before consent; tag moved behind consent, gate re-run green (G-LG-041).
8. Step 7: PAN scan finds a test card number pasted into a debug log line during development — log line removed, history scanned, incident noted; re-scan clean (G-SE-121).
9. Step 8: deployed; rollback drill passes; user approves the live-key switch and webhook re-pointing from the go-live checklist.
10. Step 9: product JSON-LD prices diffed against visible prices (G-CO-082 clean); store is done.
