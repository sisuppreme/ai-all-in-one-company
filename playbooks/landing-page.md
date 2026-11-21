# Playbook: Landing Page

One page, one conversion action: a waitlist signup, a product launch, a campaign page. Single-page and conversion-only by definition (§5.6) — if the project grows a second page type or a CMS, it becomes a Portfolio / Marketing Site and switches playbooks.

## Goal

Ship a single page that loads fast enough to keep the visitors it persuades, makes only claims that trace to evidence, converts through one accessible form, and passes every QA and accessibility gate — in days, not weeks, without cutting the gates that make it trustworthy.

## Departments and order

D1 → D3+D13 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation.

**Standing-rule exception (§5.6):** this is the one playbook with **no explicit D12 or D14 step** — it ships a single page and, in its pure form, collects nothing beyond the conversion form. Two qualifications, both mandatory:

- The **performance gates still apply in full** (G-AN-101, G-AN-111, G-FE-001 below). D12 is not a step; its budgets are enforced by D8 at step 3 using `performance-budgets`/`core-web-vitals` from the analytics bundle. A landing page that is slow has failed its only job.
- If the page collects personal data beyond a single email address (surveys, qualifiers, tracking-heavy campaigns), the exception no longer fits the project: add the D14 step from the Portfolio playbook (register + consent, G-LG-001/G-LG-041) before step 3's verification, and record the addition in `progress.md`.

D17 and D18 appear only as conditional notes (step 2b).

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | frontend-core, design-tokens, motion, forms (D3); wcag, reduced-motion (D13); copywriting, real-content (D9 — drafted in this step) | `bundles/frontend.md`, `bundles/accessibility-i18n.md`, `bundles/seo-content.md` |
| 2b (conditional) | llm-integration, ai-safety (D17) — only for an on-page AI widget; support surfaces (D18) are out of scope for a single page — link out instead | `bundles/ai-features.md` |
| 3 | owasp, secrets-management (D7); placeholder-scan, browser-verification (D8); performance-budgets, core-web-vitals (D12 gates, enforced here) | `bundles/security.md`, `bundles/qa-testing.md`, `bundles/analytics-observability.md` |
| 4 | hosting, ci-cd, rollback (D6) | `bundles/devops-deployment.md` |
| 5 | technical-seo, on-page-seo, social-open-graph (D9) | `bundles/seo-content.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — the one conversion action, the audience, the traffic source (ads, launch post, email), and the page's success metric.
- `fact-sheet.md` — every claim the page will make, with evidence: the product's real status ("in private beta", not "launched"), real numbers only, real names only. If the product does not exist yet, the page says so honestly — a waitlist page for a product "coming soon" is legitimate; a page implying a shipping product that does not exist is a Real Content violation.
- `progress.md`, `DECISIONS.md` — session log and decision record (a landing page still gets both; they will be short).
- `.env.example` — form-handler / email-list credentials by name + purpose (§5.9).

`stack.md` is in this type's mandated manifest and is generated with the rest of the set (G-PM-001); it is not an architecture exercise — for a landing page it is a short record of the default (a static page, or the platform the user's other properties already use), with the choice and its one-line reason recorded in `stack.md` and `DECISIONS.md`. The list above is the hand-written starting set; the manifest (`templates/mandated-manifest-landing-page.txt`) governs the full set, and any mandated file that genuinely does not apply is recorded not-applicable with a reason in the generation record (PM-001, PM-005) — never silently omitted.

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above.
◆ **DECISION — is this really one page, one action?** If the user describes multiple audiences, a blog, or "and also a pricing page", stop: the project is a marketing site. Switch to the Portfolio / Marketing Site playbook and record the switch in `progress.md`. Forcing a site into this playbook is how landing pages end up with no privacy step and five forms. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 1 — Offer and evidence (D1).** Fix the single conversion action and write `fact-sheet.md` before any headline is drafted.
◆ **STOP AND ASK — unsubstantiated claims (§6.3 step 4).** Conversion copy pressures toward invented social proof ("join 10,000+ users") more than any other surface. If the evidence is not in the fact sheet, the claim does not go on the page; offer the user the honest alternatives (real number, no number, or a statement about the product instead of its popularity). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Build and copy (D3+D13, D9 drafting).** Build the page and draft the copy together — on a landing page, copy *is* the interface. Order inside the step: tokens and layout first (contrast script G-AC-011 before styling depends on it), form early (it is the point of the page: G-FE-121 axe form rules, G-FE-122 keyboard-only submit, G-FE-123 double-submit — a double-submitted waitlist signup is a real defect), motion last and reduced-motion-safe (G-FE-041). Copy passes the pre-publish lint (G-CO-051) and substantiation spot-check (G-CO-052) in this step, not at launch.
**Step 2b — AI widget (D17, conditional).** An on-page chat/demo widget is built under `llm-integration` + `ai-safety` (G-AI-001, G-AI-021) and labeled as automated. Support (D18) is not built into a landing page; link to the real support channel.

**Step 3 — Verification (D7+D8, with D12 gates).** Proportionate but complete: OWASP checklist review for the form endpoint and any third-party scripts (G-SE-003), secret scan (G-SE-041), placeholder sweep (G-QA-141; scan rendered output, not source) — landing pages ship with lorem-ipsum testimonials embarrassingly often — browser verification (G-QA-031 gates), and the performance gates: CI budget assertion (G-AN-101) with a landing-page-strict budget set in this step (the page's whole payload should be smaller than a typical app's single route), frontend performance budget (G-FE-001).

**Step 4 — Deploy (D6, last build step).** Hosting production checks (G-DO-071 external production check, G-DO-073 exposure probe), pipeline (G-DO-001), rollback (G-DO-151 — for a static page this is minutes of work and is still done and recorded), DNS/TLS (G-DO-101, G-DO-111). Connect the form to the real list/handler and send a live test submission end-to-end before calling it done.

**Step 5 — Discovery (D9).** Indexability (G-CO-001) if the page is meant to be found organically (campaign pages driven purely by ads may be deliberately unlisted — record the choice), metadata and Open Graph so shares render correctly (G-CO-011 metadata lint, G-CO-111 social-open-graph gates), description-to-page promise check (G-CO-013), and the field-data check scheduled: G-AN-111 verifies real-user vitals after launch traffic arrives.

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-062 | Requirement lint; fact-sheet claim-trace audit | Steps 1, 3 |
| G-AC-011 / G-AC-012 / G-AC-015 | Contrast script; axe-core in CI; WCAG criterion checklist | Step 2 |
| G-FE-121 / G-FE-122 / G-FE-123 | Form axe rules; keyboard-only submit; double-submit test | Step 2 |
| G-FE-041 / G-FE-042 | Reduced-motion emulation pass; reduce-block presence | Step 2 |
| G-CO-051 / G-CO-052 / G-CO-061 | Copy pre-publish lint; substantiation spot-check; claim-trace audit | Steps 2, 3 |
| G-SE-003 / G-SE-041 / G-QA-141 | OWASP checklist review; secret scan; placeholder sweep | Step 3 |
| G-AN-101 / G-FE-001 | CI budget assertion; frontend performance budget in CI | Step 3 |
| G-AN-111 | Field report check (post-launch, once traffic exists) | Step 5 |
| G-DO-001 / G-DO-071 / G-DO-073 / G-DO-151 | Broken-test drill; external production check; exposure probe; rollback drill | Step 4 |
| G-CO-001 / G-CO-011 / G-CO-013 / G-CO-111 | Indexability diff; metadata lint; description-to-page promise check; social-open-graph gates | Step 5 |

Family summary (§5.6): G-QA-* all green; G-AC-* WCAG 2.2 AA pass; G-AN-* Core Web Vitals budget met.

## Failure handling

- **A gate fails:** fix and re-run; same failure twice → §6.3 (log in `progress.md`, batch blockers with options). On a one-page project there is little unblocked work to continue with — that makes the log-and-ask step faster, not skippable.
- **Substantiation fails (G-CO-052, G-PR-062):** the claim comes off the page. There is no waiver-without-user-agreement for Real Content (§5.7 rank 3), and "the campaign launches tomorrow" is not evidence.
- **Performance budget fails (G-AN-101):** remove or defer weight (hero media, third-party scripts, fonts) until it passes. A landing page does not get a budget waiver for convenience; the user's explicit recorded decision is the only exception (G-AN-103 waiver scan keeps it visible and expiring).
- **The form handler is not ready** (no list provider account, no keys): §5.9 handoff — the agent lists the exact credential needed by name and purpose. ◆ **STOP AND ASK** with options: (A) user creates the account and provides the test key, (B) ship the page with the form visibly disabled and an honest "opens on <date>" state — never a form that accepts input and silently discards it (a DET-FAKE failure and a Real Content violation). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` (§6.3 step 5).
- **A secret leaks:** revoke/rotate immediately; incident recorded without the value (§5.9 step 4).

## Definition of done

- Live on the real domain (or campaign subdomain); G-DO-071/G-DO-073 green; rollback recorded; the conversion form proven end-to-end with a real submission reaching the real list.
- Every claim on the page traces to `fact-sheet.md`; zero placeholder text, zero invented proof (G-QA-141, G-CO-061 clean).
- Payload within the strict landing budget in CI; field vitals check scheduled and passing once traffic exists (G-AN-111).
- WCAG 2.2 AA checklist complete; form fully keyboard-operable; motion reduced-motion-safe.
- Zero P0/P1 defects (QB-01); `progress.md` records the launch state and where the signup data goes.
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **Waitlist page for "Ledgerly"**, a bookkeeping tool launching in six weeks, traffic from a launch post.

1. Step 0: core loaded; static project scaffolded; email-list API key listed by name in `.env.example`.
2. Step 1: conversion action fixed — email signup for launch notification. The user suggests "Join 2,000+ freelancers already waiting"; the real waitlist is 143 people from a beta form. Fact sheet records 143; the headline uses the real number.
3. Step 2: page built — hero, three feature blocks (features that exist in the beta, verified against the product), one form. Form passes keyboard-only submit and double-submit tests (G-FE-122, G-FE-123).
4. Step 2 (motion): the animated product carousel fails reduced-motion emulation → replaced with a static screenshot under `prefers-reduced-motion` (G-FE-041 green); conflict logged (D13 over D3, §5.7).
5. Step 3: placeholder sweep finds "Lorem ipsum" in a footer blurb left from the template — replaced with the real company line (G-QA-141 clean on re-run).
6. Step 3: budget assertion fails — an unoptimized hero video puts the page at 2.1 MB against a 600 KB budget → video becomes a poster image with click-to-play; G-AN-101 green.
7. Step 4: deployed to the launch subdomain; a live test signup lands in the real list; rollback recorded.
8. Step 5: Open Graph card verified on a real share preview; meta description rewritten so it promises "launching in March" (true) instead of "available now" (G-CO-013).
9. Post-launch: first week of traffic, field report shows LCP p75 1.9 s (G-AN-111 pass).
10. Done — one page, one form, every number on it true.
