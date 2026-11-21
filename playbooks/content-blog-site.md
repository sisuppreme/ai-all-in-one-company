# Playbook: Content / Blog Site

A content-led site: articles, guides, documentation-style publications, where search discovery and reading experience are the product. Use this playbook for docs sites too (§5.6). If the site exists mainly to sell a product with accounts and billing, use the SaaS playbook instead.

## Goal

Ship a fast, indexable publication where every article traces to a brief and a named author, metadata and structured data match what is visibly on the page, Core Web Vitals budgets hold on article templates, WCAG 2.2 AA passes, and the site is deployed with monitoring and rollback.

## Departments and order

D1 → D2 → D3+D13+D4+D5 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation. D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule; D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | stack-selection, system-design (D2) | `bundles/architecture.md` |
| 3 | frontend-core, design-tokens, typography (D3); wcag, accessibility-audit (D13); api-building (D4, only if a CMS/API layer exists); schema-design (D5, content model) | `bundles/frontend.md`, `bundles/accessibility-i18n.md`, `bundles/backend.md`, `bundles/database.md` |
| 4 | content-strategy, technical-seo, on-page-seo, structured-data, sitemaps (D9 — drafting pipeline set up here, executed at step 9) | `bundles/seo-content.md` |
| 4b (conditional) | llm-integration, ai-safety (D17) — only for AI-assisted drafting or on-site AI search/chat | `bundles/ai-features.md` |
| 5 | performance-budgets, core-web-vitals (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, legal-documents, cookie-consent (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | help-center, support-ticketing (D18) — only if the site ships support surfaces | `bundles/customer-experience.md` |
| 7 | owasp, secrets-management (D7); placeholder-scan, browser-verification (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | hosting, ci-cd, rollback (D6) | `bundles/devops-deployment.md` |
| 9 | content-strategy, technical-seo, structured-data, sitemaps, web-analytics (D9) | `bundles/seo-content.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — audience, content types, publishing workflow, and what the site must rank/be found for.
- `fact-sheet.md` — the publication's verifiable facts: author identities and credentials, publication details, any statistics the house style cites. No invented authors, credentials, or reader numbers.
- `stack.md` — CMS/rendering choice (static, headless CMS, or server-rendered) with dated criteria (G-AR-023).
- `progress.md`, `DECISIONS.md` — session log and decision record.
- `CONTENT_METADATA.md` — the content model: fields per content type, author attribution rules, review-by dates, metadata requirements per route.
- `SCHEMA.md` — content storage invariants if a database backs the CMS (draft/published states, slug uniqueness).
- `.env.example` — CMS and analytics credentials by name + purpose (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above.

**Step 1 — Requirements (D1).** Fix the audience, the content types, who writes and who approves, and the publishing cadence the design must support. ◆ **DECISION — comments or reader accounts?** Either one pulls in moderation, auth, and a larger D14 register. If the user has not asked for them, the default is *no comments, no accounts* — record the decision in `requirements.md` rather than building the machinery "just in case." (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Architecture (D2).** Choose the rendering/CMS stack by criteria recorded before the decision (G-AR-023): editorial workflow, build time at expected article count, hosting cost. A static or cached architecture is the default for content; a server-rendered app needs a written reason in `DECISIONS.md`.

**Step 3 — Build (D3+D13+D4+D5).** Content model first (`SCHEMA.md` / `CONTENT_METADATA.md`), templates second, sample content last — and sample content is written as real, publishable articles or clearly-marked draft fixtures, never lorem ipsum that survives to launch (G-QA-141). D13 inside the step: article typography and templates pass the contrast script (G-AC-011) and the criterion checklist (G-AC-015); long-form reading is the primary surface and gets the full keyboard + screen-reader audit (G-AC-002, G-AC-003).

**Step 4 — Content pipeline (D9 setup).** Stand up the `content-strategy` workflow now, while templates are fresh: every article starts from a brief (G-CO-041 brief traceability), metadata is linted in CI (G-CO-011), and the sitemap is generated from the route inventory, never hand-maintained (G-CO-091). Drafting itself happens continuously from here on; the launch gate is step 9.
**Step 4b — AI assistance (D17, conditional).** AI-drafted or AI-assisted articles are disclosed per the publication's stated policy in `fact-sheet.md`, pass the same claim-trace as human copy (G-CO-061), and any on-site AI feature passes `ai-safety` (G-AI-021). Undisclosed AI content presented as human reporting is a Real Content violation (§5.7 rank 3).

**Step 5 — Performance budgets (D12, explicit step).** Article templates carry the strictest budgets (they are the most-visited and most-linked pages): CI budget assertion (G-AN-101) and the field check on the 28-day p75 (G-AN-111) once live.

**Step 6 — Legal and privacy (D14, explicit step).** Register covers analytics, comments/accounts if present, newsletter data if present. Cookie consent with pre-consent scan (G-LG-041); legal documents diffed against the register (G-LG-031).

**Step 7 — Verification (D7+D8).** Even a static site gets the security pass: OWASP checklist review proportionate to the surface (G-SE-003), full-history secret scan (G-SE-041) — CMS tokens leak into repos constantly — placeholder sweep over every template and seed article (G-QA-141; scan rendered output, not source), and browser verification of the article, index, and search routes (G-QA-031 browser-verification gates).

**Step 8 — Deploy (D6, last build step).** Hosting selection and production checks (G-DO-071 external production check, G-DO-075 hosting record audit), pipeline with broken-test drill (G-DO-001), rollback drill (G-DO-151). Domain and DNS per `domains-dns` (G-DO-101 record-sheet match) and TLS per `ssl-certificates` (G-DO-111).

**Step 9 — Launch and discovery (D9).** The full content gate set on the production build: indexability diff (G-CO-001), route inventory crawl (G-CO-002), structured data validated and diffed against visible content (G-CO-081, G-CO-082), sitemap audit (G-CO-091), authorship audit — every byline resolves to a real person or an honest collective, and house bylines name an accountable team, not a fake individual (G-CO-044) — and claim-trace on launch articles (G-CO-061).

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-032 | Requirement lint; traceability coverage | Step 1 |
| G-AR-023 | Stack criteria predate the decision | Step 2 |
| G-DB-001 | Schema lint (content model, if database-backed) | Step 3 |
| G-FE-002 / G-AC-011 / G-AC-012 / G-AC-015 | Accessibility floor scan; contrast script; axe-core in CI; WCAG criterion checklist | Step 3 |
| G-AC-002 / G-AC-003 | Keyboard walk; screen-reader smoke test (article template) | Step 3 |
| G-CO-041 / G-CO-011 | Brief traceability audit; metadata lint | Step 4 |
| G-AN-101 / G-AN-111 | CI budget assertion; field report check (post-launch) | Steps 5, 9 |
| G-LG-001 / G-LG-031 / G-LG-041 | Register coverage; document-vs-register diff; pre-consent network scan | Step 6 |
| G-SE-003 / G-SE-041 / G-QA-141 | OWASP checklist review; secret scan; placeholder sweep | Step 7 |
| G-DO-001 / G-DO-071 / G-DO-151 | Broken-test drill; external production check; rollback drill | Step 8 |
| G-CO-001 / G-CO-002 | Promotion indexability diff; route inventory crawl | Step 9 |
| G-CO-081 / G-CO-082 / G-CO-091 | Structured-data validation; markup-vs-visible diff; sitemap audit | Step 9 |
| G-CO-044 / G-CO-061 | Authorship audit; claim-trace audit | Step 9 |

Family summary (§5.6): G-QA-* all green; G-AC-* WCAG 2.2 AA pass; G-CO-* SEO + structured-data validation pass.

## Failure handling

- **A gate fails:** fix in the owning step, re-run. Same failure twice → §6.3: log in `progress.md`, continue unblocked work, batch blockers with concrete options.
- **Structured data disagrees with the page (G-CO-082):** the launch waits. Markup that claims a different author, date, or headline than the visible page is a trust defect, not a typo — fix the generator, not the one instance.
- **Authorship or claim-trace fails (G-CO-044, G-CO-061):** the article does not publish. An invented expert byline or an untraceable statistic is a Real Content violation (§5.7 rank 3); there is no waiver without the user's explicit agreement, and the correct fix is a real author or a cut claim.
- **Two skills contradict:** §5.7 precedence (Real Content 3 and accessibility 5 both outrank content/SEO 14); log in `DECISIONS.md`.
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` (§6.3 step 5), flagged as a repo gap.
- **A secret leaks:** revoke/rotate immediately, incident recorded without the value (§5.9 step 4).

## Definition of done

- Live on a real host/domain; G-DO-071 green; rollback drill on record; monitoring up (QB-02).
- Every launch article traces to a brief and a real named author; metadata lint, sitemap, and structured-data gates green on the production build.
- Article templates within budget in CI and, after 28 days, in field data (G-AN-111).
- Zero P0/P1 defects (QB-01); no placeholder text, fake authors, or untraceable claims anywhere on the site.
- `progress.md` and `handover.md` current; the publishing workflow (brief → draft → gates → publish) is documented in the project README so the user's next article follows it without the agent re-deriving it.
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **Atlas Blog**, a travel-guide publication launching with 12 articles.

1. Step 0: core loaded; project scaffolded; CMS token and analytics ID listed in `.env.example` by name only.
2. Step 1: requirements fix guides + city pages, no comments, no accounts; decision recorded.
3. Step 2: criteria written first (editorial ease, build time at 500 articles, $0–10/mo hosting) → static generation with a headless CMS wins; decision logged (G-AR-023).
4. Step 3: content model defines guide fields and mandatory author attribution; article template passes contrast script and keyboard walk (G-AC-011, G-AC-002).
5. Step 4: briefs written for all 12 launch articles; metadata lint wired into CI (G-CO-011).
6. Step 5: article template budgeted at 150 KB JS / LCP 2.5 s (G-AN-101).
7. Step 6: register covers analytics + newsletter; consent scan shows the newsletter provider's script loading pre-consent — moved behind consent (G-LG-041).
8. Step 7: secret scan finds the CMS token in an early commit — token rotated, history noted, incident recorded in `progress.md`; placeholder sweep clean.
9. Step 8: deployed to production domain; DNS records match the record sheet (G-DO-101); rollback drill passes.
10. Step 9: one article's JSON-LD names a different author than its byline (G-CO-082 fail) — generator fixed to read the same author field, re-validated; authorship audit confirms all 12 bylines are real people (G-CO-044). Done.
