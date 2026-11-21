# Playbook: Portfolio / Marketing Site

A multi-page, CMS-driven site whose job is persuasion: services, work samples, about, contact. If the project is a single page built only to convert visitors to one action, use the Landing Page playbook instead (§5.6 distinction: portfolio/marketing = multi-page + CMS-driven; landing = single-page + conversion-only).

## Goal

Ship a fast, credible marketing site where every claim, client name, metric, and testimonial traces to a verifiable fact — because on a marketing site the Real Content Rule *is* the product — with motion that respects reduced-motion settings, WCAG 2.2 AA, Core Web Vitals budgets met, and all QA gates green.

## Departments and order

D1 → D2 → D3+D13 → D7+D8 → D6 → D9 — exactly as the §5.6 table; no deviation. D12 and D14 appear as explicit steps 5 and 6 per the §5.6 standing rule; D17 and D18 appear as conditional steps 4b and 6b.

## Skills to load

Load `bundles/core.md` first (always-on core). Then, per step:

| Step | Skills | Bundle |
|---|---|---|
| 0 | project-templates, progress-tracking (D10); secrets-management (D7); qa-gates (D8) | `bundles/core.md` |
| 1 | requirements-writing, fact-sheet (D1) | `bundles/product-requirements.md` |
| 2 | stack-selection (D2) | `bundles/architecture.md` |
| 3 | frontend-core, motion, design-tokens, component-library (D3); wcag, accessibility-audit, reduced-motion (D13) | `bundles/frontend.md`, `bundles/accessibility-i18n.md` |
| 4 | copywriting, real-content (D9 — copy drafted here against the fact sheet, launched at step 9) | `bundles/seo-content.md` |
| 4b (conditional) | llm-integration, ai-safety (D17) — only for an on-site AI feature such as a chat assistant | `bundles/ai-features.md` |
| 5 | performance-budgets, core-web-vitals (D12) | `bundles/analytics-observability.md` |
| 6 | privacy-laws, legal-documents, cookie-consent (D14) | `bundles/legal-privacy.md` |
| 6b (conditional) | help-center, support-ticketing (D18) — only if the site ships support surfaces | `bundles/customer-experience.md` |
| 7 | owasp, secrets-management (D7); placeholder-scan, browser-verification (D8) | `bundles/security.md`, `bundles/qa-testing.md` |
| 8 | hosting, ci-cd, rollback (D6) | `bundles/devops-deployment.md` |
| 9 | technical-seo, on-page-seo, copywriting (final pass) (D9) | `bundles/seo-content.md` |

## Docs to write first

Before any code, scaffold from `project-templates` and write:

- `requirements.md` — pages, audiences, the one conversion action per page, CMS needs.
- `fact-sheet.md` — the evidence base for all copy: real client names (with permission), real project outcomes, real metrics with sources and dates, the team's real names and credentials. **Anything not in this sheet does not appear on the site.**
- `stack.md` — CMS/hosting choice with dated criteria (G-AR-023).
- `progress.md`, `DECISIONS.md` — session log and decision record.
- `CONTENT_METADATA.md` — page inventory, per-page intent, metadata and Open Graph requirements.
- `.env.example` — CMS, form-handler, and analytics credentials by name + purpose (§5.9).

## Step-by-step sequence

**Step 0 — Core and scaffold.** Load `bundles/core.md`; generate the project (G-PM-001, G-PM-002); write the docs above.

**Step 1 — Requirements and evidence (D1).** Requirements fix the page list and the conversion action per page. Then build `fact-sheet.md` *before* any copy is drafted: interview the user for real clients, real results, real numbers.
◆ **STOP AND ASK — missing evidence (§6.3 step 4, Real Content §5.7 rank 3).** If the user wants a results claim, testimonial, or client logo they cannot substantiate, stop and offer concrete options: (A) publish the section as an honest empty state or omit it, (B) the user supplies the evidence and it enters the fact sheet, (C) reframe to a claim that *is* substantiated. Never draft the unsubstantiated version "as a placeholder" — placeholders on marketing sites ship. (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)

**Step 2 — Platform (D2).** CMS and hosting chosen by criteria recorded first (G-AR-023): who edits the site after launch, how often, and their technical level decide the CMS — not the agent's familiarity.

**Step 3 — Build (D3+D13).** Design tokens and components first, pages second, motion last and deliberately: every animation passes the reduced-motion emulation pass (G-FE-041) and the reduce-block presence check (G-FE-042) — D13 outranks D3 on any conflict (§5.7: accessibility rank 5, design rank 15), so a motion effect that fails reduced-motion is adapted or dropped, never shipped as-is. Forms (contact/lead) pass G-FE-121/G-FE-122. Contrast script on tokens before pages are built on them (G-AC-011).

**Step 4 — Copy (D9 drafting).** `copywriting` drafts from `fact-sheet.md` only: pre-publish lint (G-CO-051), substantiation spot-check on every quantitative or comparative claim (G-CO-052), naming lint so no competitor or client name is misstated (G-CO-053). **Content-as-input builds:** where the build is static and the copy is an input to step 3 rather than content entered afterward (no CMS between the build and the page), the copy step's inputs are gathered before the build step — draft the copy from `fact-sheet.md` at step 3, build with it, and run this step's gates against it afterward. The numbered order above is unchanged for CMS-shaped builds, where copy is entered into the built site. Case-study pages present the client's real work and real outcomes; stock imagery is never captioned as the client's premises, team, or product (G-FE-004 imagery inspection).
**Step 4b — AI features (D17, conditional).** A chat assistant or similar is built under `llm-integration` + `ai-safety` (G-AI-001, G-AI-021) and is labeled as automated where a visitor could mistake it for a person (Real Content Rule).

**Step 5 — Performance budgets (D12, explicit step).** Budgets per template asserted in CI (G-AN-101); marketing sites accumulate hero video, carousels, and third-party embeds, so the budget is set at this step and every later addition is checked against it — an embed that breaks the budget is removed or click-to-load, not waived quietly.

**Step 6 — Legal and privacy (D14, explicit step).** Register covers the contact form, analytics, and any embedded third parties (maps, video, chat widgets — each is a processor). Consent gates trackers (G-LG-041); privacy document diffed against the register (G-LG-031). Client logos and testimonials also get a permission check here: permission recorded in `fact-sheet.md`, or the logo does not ship.

**Step 7 — Verification (D7+D8).** OWASP checklist review proportionate to surface (G-SE-003) — a form handler and a CMS are real attack surface; secret scan (G-SE-041); placeholder sweep over all pages and CMS seed content (G-QA-141; scan rendered output, not source); browser verification of every template (G-QA-031 gates); claim-trace audit across the whole site (G-PR-062).

**Step 8 — Deploy (D6, last build step).** Hosting production checks (G-DO-071, G-DO-073 exposure probe — marketing repos love leaking `.env` and draft pages), pipeline drill (G-DO-001), rollback drill (G-DO-151), DNS/TLS per `domains-dns`/`ssl-certificates` (G-DO-101, G-DO-111).

**Step 9 — Discovery (D9).** Indexability diff (G-CO-001), metadata lint and intent-map coverage (G-CO-011, G-CO-012), description-to-page promise check — the meta description must not promise what the page does not deliver (G-CO-013) — and the final substantiation re-check on the production copy (G-CO-052).

## Gates that must pass

| Gate | Name | Phase |
|---|---|---|
| G-PM-001 / G-PM-002 | Project-templates manifest diff; unreplaced-token scan | Step 0 |
| G-PR-031 / G-PR-062 / G-PR-063 | Requirement lint; claim-trace audit; price mirror diff (if pricing is published) | Steps 1, 7 |
| G-AR-023 | Stack criteria predate the decision | Step 2 |
| G-FE-001 / G-FE-004 | Performance budget in CI; imagery inspection | Steps 3, 7 |
| G-FE-041 / G-FE-042 / G-FE-043 | Reduced-motion emulation pass; reduce-block presence; motion-token lint | Step 3 |
| G-AC-011 / G-AC-012 / G-AC-015 | Contrast script; axe-core in CI; WCAG criterion checklist | Step 3 |
| G-FE-121 / G-FE-122 | Form axe rules; keyboard-only submit (contact/lead forms) | Step 3 |
| G-CO-051 / G-CO-052 / G-CO-053 | Copy pre-publish lint; substantiation spot-check; naming lint | Steps 4, 9 |
| G-CO-061 / G-CO-063 | Claim-trace audit; evidence register completeness (testimonials, logos) | Steps 4, 7 |
| G-CO-064 | Named human verification of the production copy (human-required; a single agent prepares the verification packet and stops at publication — see the gate's single-agent disposition) | Step 9 |
| G-AN-101 / G-AN-111 | CI budget assertion; field report check (post-launch) | Steps 5, 9 |
| G-LG-001 / G-LG-031 / G-LG-041 | Register coverage; document-vs-register diff; pre-consent network scan | Step 6 |
| G-SE-003 / G-SE-041 / G-QA-141 | OWASP checklist review; secret scan; placeholder sweep | Step 7 |
| G-DO-001 / G-DO-071 / G-DO-073 / G-DO-151 | Broken-test drill; external production check; exposure probe; rollback drill | Step 8 |
| G-CO-001 / G-CO-011 / G-CO-013 | Indexability diff; metadata lint; description-to-page promise check | Step 9 |

Family summary (§5.6): G-QA-* all green; G-AC-* WCAG 2.2 AA pass; G-CO-* SEO pass; G-AN-* Core Web Vitals budget met.

## Failure handling

- **A gate fails:** fix in the owning step and re-run; same failure twice → §6.3 protocol (log, continue unblocked work, batch blockers with options).
- **Substantiation fails (G-CO-052, G-PR-062):** the claim is cut or reframed to what the evidence supports. This is the one failure class where "ship now, fix the copy later" is explicitly forbidden — an unsubstantiated claim on a live marketing site is the defect, live. No waiver without the user's explicit agreement, and the agent must tell the user plainly that the claim is unsubstantiated (§6.3 step 4d).
- **Motion vs reduced-motion conflict:** D13 wins by precedence (§5.7); adapt or drop the effect and log the conflict in `DECISIONS.md`. The G-FE-041 gate is re-run against the adapted effect — precedence never skips the gate.
- **Budget fails after an embed is added (G-AN-101):** the embed becomes click-to-load or is removed. Performance (rank 12) loses to nothing here except the user's explicit, recorded decision to accept the slower page — recorded as a budget waiver with an expiry (G-AN-103 waiver scan).
- **A gate is itself wrong:** recorded waiver in `progress.md` + `DECISIONS.md` (§6.3 step 5); Real Content and legal waivers need explicit user agreement.
- **A secret leaks:** revoke/rotate immediately; incident recorded without the value (§5.9 step 4).

## Definition of done

- Live on the real domain; G-DO-071/G-DO-073 green; rollback drill recorded; monitoring up (QB-02).
- Every claim, metric, testimonial, and logo on the site traces to `fact-sheet.md` with evidence or permission on file; claim-trace and substantiation gates green on production copy.
- All templates within Core Web Vitals budgets in CI; field check scheduled and passing at 28 days (G-AN-111).
- WCAG 2.2 AA checklist complete; all motion passes reduced-motion emulation.
- Zero P0/P1 defects (QB-01); the user can edit routine content in the CMS without the agent, and `handover.md` says how.
- **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* — every gate except the provisioning-waived ones green, each waived gate recorded as a provisioning waiver per §6.3, and the unblocking conditions listed in `progress.md`. The deployment requirements above remain open until the environment exists; pre-provisioning complete is not done.

## Worked mini-example

Sample project: **Studio Meridian**, a 9-page site for a four-person brand-design studio.

1. Step 0: core loaded; project scaffolded; form-handler and CMS keys listed by name in `.env.example`.
2. Step 1: page list fixed (home, services, work, studio, contact). Fact-sheet interview: the studio claims "40+ brands launched" — they can evidence 23. The sheet records 23.
3. Step 2: criteria (non-technical editor, weekly updates, low cost) recorded first → hosted CMS chosen (G-AR-023).
4. Step 3: tokens pass contrast script; the hero's parallax scroll effect fails the reduced-motion pass (G-FE-041) → adapted to a static layered hero under `prefers-reduced-motion`, conflict logged in `DECISIONS.md`.
5. Step 4: copy drafted from the fact sheet; substantiation check cuts "award-winning" (no award on file) and keeps the 23-brands claim with the client list as evidence (G-CO-052, G-CO-063).
6. Step 5: budgets set; a third-party video embed breaks the home-page budget → converted to click-to-load, gate green (G-AN-101).
7. Step 6: register covers form, analytics, and the video embed as processor; consent scan passes after the embed change (G-LG-041).
8. Step 7: exposure probe finds a draft pricing page reachable in production — removed and re-probed (G-DO-073 runs early as a staging check, then again at step 8).
9. Step 8: deployed on the studio's domain; rollback drill passes; monitoring live.
10. Step 9: meta description for Services promises "same-week delivery" that the page does not offer — rewritten to match the page (G-CO-013). Done.
