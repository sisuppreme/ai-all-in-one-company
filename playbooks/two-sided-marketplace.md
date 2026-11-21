# Playbook — Two-sided Marketplace

## Goal

Build a marketplace where two populations — sellers/suppliers and buyers — transact through the platform: listings, orders, platform-mediated payments with payouts to sellers, refunds and disputes, and the trust machinery (roles, audit trails, clear money states) that makes strangers willing to trade.

## Departments + order

Step 0 (always-on core) → D1 → D2+D7 → D3+D13+D4+D5 → D11 → D14 → D12 → D7+D8 → D6 → D9

This follows the brief's order for this type, with D14 and D12 as explicit steps: a marketplace holds two sides' personal and money data, and its listing/search surfaces live or die on performance budgets.

## Skills to load

Load this playbook's bundle first: `bundles/two-sided-marketplace.md`. Then, per step:

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| requirements-writing, fact-sheet | `bundles/product-requirements.md` |
| system-design | `bundles/architecture.md` |
| frontend-core | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| api-building, rbac | `bundles/backend.md` |
| schema-design | `bundles/database.md` |
| payments, subscriptions, refunds-disputes, webhooks, invoicing-tax | `bundles/integrations-payments.md` |
| privacy-laws, legal-documents, audit-trails | `bundles/legal-privacy.md` |
| performance-budgets, core-web-vitals | `bundles/analytics-observability.md` |
| owasp, auth-hardening | `bundles/security.md` |
| placeholder-scan | `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |
| technical-seo, structured-data | `bundles/seo-content.md` |

Conditional: subscriptions applies when the marketplace charges sellers a recurring plan (not pure commission) — if the model is commission-only, drop it and record why in `progress.md`. If the marketplace adds AI features (recommendations, search ranking, listing assistance), add a D17 step before D7+D8 (recommendations, search-relevance, ai-safety). If it ships support surfaces, add a D18 step (help-center, support workflows) before D9.

## Docs to write first

1. `fact-sheet.md` — the money facts: commission/fee model, who is merchant of record, payout timing, refund policy. Every figure sourced from the user's decision or the provider's documentation; no fee is invented.
2. `stack.md` — payment provider and payout mechanism (provider-managed split payments vs platform-held balance), with the provider's country and account-type constraints recorded.
3. `progress.md` — playbook trace and gate results.
4. Role matrix draft — buyer / seller / admin capabilities, which rbac will formalize; a marketplace's authorization model is designed, not accreted.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; project files, `progress.md`, secrets baseline.
1. **D1 requirements.** requirements-writing for both sides separately: seller journeys (list, sell, get paid) and buyer journeys (find, buy, get refunded) are distinct requirement sets. fact-sheet locks the money model. *Decision point: if the fee model, merchant-of-record question, or payout timing is undecided, stop and ask (§6.3) — these are business decisions the build cannot guess.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D2+D7 design.** system-design: order state machine, payment/payout flow, what the platform's database is the source of truth for (orders, balances-as-ledger-entries — never a mutable balance column). auth-hardening + rbac design together: three roles minimum, seller data isolated per seller.
3. **D3+D13+D4+D5 build.** schema-design: listings, orders, ledger-style money records with constraints (G-DB-001, G-DB-002). api-building for both sides' APIs (G-BE-001 contract tests). rbac enforced server-side (G-BE-061 authorization matrix test, G-BE-062 cross-tenant access test — one seller must never reach another seller's orders or payout data). Frontend for both sides; D13 in the same step (G-AC-001 on listing, checkout, and seller dashboard templates).
4. **D11 money.** payments in test mode first (G-IN-001 double-submit, G-IN-002 test-mode purchase and decline walk, G-IN-004 card-data absence scan — card data never touches the platform's servers). webhooks are the arbiter of payment state (G-IN-051 forgery test, G-IN-052 duplicate-delivery, G-IN-054 reconciliation-before-fulfillment). Payouts verified in test mode end to end: a test sale produces a test payout to a test seller account. refunds-disputes wired before launch, not after the first chargeback (G-IN-021 refund agreement test, G-IN-022 dispute drill, G-IN-024 open-dispute deadline audit). invoicing-tax: invoices/receipts generated from the ledger, tax treatment per the fact-sheet — no invented rates.
   *Decision point: if the provider cannot pay out to sellers in the marketplace's operating country, or requires a business type the operator does not have, stop and ask (§6.3). Do not substitute manual bank transfers "for now" — that changes the legal and fraud model.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
5. **D14 legal/privacy.** privacy-laws register covers both sides' data (G-LG-001, G-LG-002); legal-documents produces the marketplace terms, seller agreement, and refund policy as shipped pages — the refund policy page and the refunds-disputes behavior must agree word-for-word on deadlines. audit-trails on money and moderation actions (G-LG-081 action-coverage test).
6. **D12 performance.** performance-budgets on listing/search pages (G-AN-101); core-web-vitals field check plan for the public catalog (G-AN-111).
7. **D7+D8 verification.** Security: G-SE-001 (0 criticals), G-SE-031 (auth abuse pack), re-run of G-BE-062 against the near-final build. QA: G-QA-111, placeholder-scan G-QA-141 (scan rendered output, not source) — listing pages seeded with demo products are placeholder content and do not ship. Full money rehearsal in test mode: list → buy → decline → refund → dispute → payout, every state transition recorded.
8. **D6 deploy.** ci-cd (G-DO-001), hosting (G-DO-071). Webhook endpoints live and verified against the production URL before the first real transaction is allowed. *No deployment before step 7 is green; no live-mode keys until the test-mode rehearsal is recorded in `progress.md`.*
9. **D9 finish.** technical-seo + structured-data for the public catalog (G-CO-001, G-CO-081) — only real listings are indexable; empty category pages stay out of the index.

## Gates that must pass

- **Money (blocking):** G-IN-001, G-IN-002, G-IN-004, G-IN-005 (webhook replay), G-IN-051, G-IN-052, G-IN-054 — checkout verified in test mode; G-IN-021, G-IN-022, G-IN-023, G-IN-024 — refunds + disputes verified in test mode; payout path verified in test mode end to end.
- **Authorization:** G-BE-061, G-BE-062 — no cross-seller or cross-buyer data access.
- **Security:** G-SE-001 (0 critical findings), G-SE-031.
- **Legal:** G-LG-001, G-LG-002, G-LG-081; shipped refund policy matches system behavior.
- **Accessibility:** G-AC-001, G-AC-005 — WCAG 2.2 AA pass.
- **QA:** G-QA-111, G-QA-141 — all green, no demo listings in production data.
- **Performance/deploy:** G-AN-101, G-DO-001, G-DO-071.

## Failure handling

- **Payout verification fails in test mode:** launch is blocked, full stop. Diagnose against the provider's test-mode records and the ledger (G-IN-003 reconciliation diff); if the cause is a provider/country constraint, return to the step-4 decision point and ask the user — never paper over it with a manual payout process.
- **Reconciliation diff (G-IN-003/G-IN-023) is non-zero:** money state is wrong somewhere; freeze further money work, trace order-by-order from webhook log → ledger → provider record. A marketplace with an unexplained money diff does not deploy.
- **Cross-tenant test fails (G-BE-062):** treat as a security incident inside the build: fix the authorization path, re-run the full rbac matrix (G-BE-061), and audit whether the same pattern exists in sibling endpoints before continuing.
- **Refund policy page and system behavior disagree:** the system changes to match the published policy, or the policy is corrected with the user's approval before launch — they never ship in disagreement.
- **Any other gate fails:** fix in the owning department, re-run, record both results in `progress.md`.

## Definition of done

Test-mode rehearsal recorded for the full money loop (sale, decline, refund, dispute, payout) with zero reconciliation diff; role matrix enforced and cross-tenant tests green; published policies match system behavior; no demo/placeholder listings in production; deployed (G-DO-071) with live webhooks verified; all gates above green. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists.

## Worked mini-example — marketplace for local home bakers

1. Core loaded; fact-sheet locks the model: 10% commission (user-set), platform is merchant of record, payouts weekly via the provider's split-payment product.
2. D1 writes buyer and seller requirement sets separately; seller onboarding requires a provider payout account before the first listing can go live.
3. D2: order states — placed → paid → fulfilled → completed, with refunded/disputed branches; money stored as ledger entries (G-DB-002 constraints in place).
4. Build: G-BE-062 catches a seller dashboard query missing the seller filter → fixed, matrix re-run green.
5. D11 test mode: test purchase passes (G-IN-002); webhook forgery rejected (G-IN-051); duplicate delivery is idempotent (G-IN-052).
6. Payout rehearsal: test sale → test payout lands in the test seller account; reconciliation diff zero (G-IN-003).
7. Refund/dispute: G-IN-021/022 pass; the published refund policy's 48-hour window matches the implemented window.
8. D14: seller agreement + privacy register complete (G-LG-001); audit trail covers payout and refund actions (G-LG-081).
9. D7+D8: G-SE-001 clean; G-QA-141 removes 12 seeded demo listings from the production seed file.
10. Deploy (G-DO-071); live webhook endpoint verified with the provider's test event before live keys are enabled.
