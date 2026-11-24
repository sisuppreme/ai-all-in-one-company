# ui-ux-upscaler

Takes an EXISTING application with an EXISTING UI and upscales it 50x to the OmniForge premium standard — audit-first, behaviour preserved, theme decided, staged passes, full motion system, signature elements merged with content. The spine is the v1.3.0 Existing-Project Upgrade Protocol (7 steps) in `custom-instructions/claude.md`: audit → preserve → theme decision → staged passes → hard rules → score gate → report. This skill expands each step into operable rules; the deep 50x detail lives in `specs/` — this file is the tight core that references it. A finished audit with no applied upgrade is a failed task.

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-24
- **Sources:** design-intelligence, theme-library expanded specs, motion, scroll-experiences, the v1.3.0 Existing-Project Upgrade Protocol
- **Depends on:** design-intelligence, theme-library, motion, scroll-experiences, design-system, design-tokens, typography, layout-responsive, component-library, ui-states
- **Feeds into:** frontend-core, ai-retrofit, clone-redesign, prototype-hardening, project-takeover

## When to use / Do NOT use

- **Use when:** an already-built, already-shipped application must be raised to the premium standard without changing what it does — a dashboard, storefront, SaaS area, or internal tool whose UI is dated, generic, or slop, and whose behaviour, content, data, routes, and APIs must keep working.
- **Do NOT use when:** the build is greenfield (use design-intelligence to decide it first, then build); the ask is a single-component fix (use component-library / ui-states); or the ask is a behaviour or architecture change (use ai-retrofit, prototype-hardening, or project-takeover — this skill governs the UI/UX standard they must reach, it does not redesign the product).
- **Scope: web apps only.** Native mobile apps get an adaptation note only (§8), never full specs from this skill.

## Rules

1. **FE-361 — Audit first, no silent restyle.** Nothing is changed before the audit in §1 exists: every page and component scanned, every defect listed in `UI-UPGRADE-AUDIT.md`, BEFORE score recorded. A restyle that starts by opening an editor has already failed.
2. **FE-362 — Preserve what works.** Functionality, content, data, routes, APIs, and behaviour keep working; the upgrade is presentation-layer first. Never delete a working feature to make the design easier — bend the design around the product, never the product around the design.
3. **FE-363 — Theme is decided, never drifted.** One theme for the whole app (§2): either the app's own identity deepened, or one library theme adopted whole from its expanded spec. No page invents its own theme, palette, or motion language.
4. **FE-364 — Passes run whole-app, in order.** Tokens → typography → layout → components/states → motion → scroll → polish (§3). Each pass finishes across the ENTIRE app before the next starts; a pass that is half-done everywhere is not a pass.
5. **FE-365 — A full motion system ships on every page.** Every term in §4, used heavily, in the app's own style, never copy-pasted between apps or themes. A missing term needs a recorded in-theme reason, never silent absence.
6. **FE-366 — Signature elements are merged, 5–20 per app.** Each element passes the merge test in §5: remove it and the page must lose information or story. Pasted-on decoration is a defect, whatever it cost to build.
7. **FE-367 — Zero behaviour regression.** Every pass is checked against the pre-change baseline (§7): same flows, same outcomes, same data. A pass that breaks a flow is rolled back, not patched around.
8. **FE-368 — Score before shipping.** The upgraded app is re-scored on the design-intelligence gate: AFTER ≥ 64/80, every audit defect fixed or explicitly reported with its reason. No claim of "premium" without the score.
9. **FE-369 — Use the internals to understand, never to show.** The UI agent must USE all of the app's skills — architecture, backend, database, API, and the rest — to understand how the app works, but must NEVER surface their internals in the UI (§6).
10. **FE-370 — The UI speaks only user-facing concepts.** Labels, copy, empty states, errors, and navigation express tasks, content, and actions the user understands — never the machinery underneath (§6 ban list).
11. **FE-371 — The leak audit is a veto.** The audit carries a BEFORE leak score and an AFTER leak score, target zero. Any leak in the shipped UI is a gate FAIL, whatever the design-intelligence /80 score is.
12. **FE-372 — Cursor feather-light or none, and premium means one pass more.** A custom cursor is permitted only if it is feather-light — transform-only, on the single rAF loop, zero perceptible lag, gone under reduced motion; a cursor that makes the pointer hard to move is a defect. When the build feels premium, do one more pass: detail inside the signature elements, physics in the motion, life in every section.

## §1 — Audit-first system

Write `UI-UPGRADE-AUDIT.md` at the project root before touching any UI. It is the contract for the whole upgrade; every later pass and gate reads from it (full audit method: `specs/01-audit-and-scoring.md`).

**What the audit must cover — nothing exempt.** Every page and every component, at 1440 px and 390 px, against the design-intelligence anti-slop table and the UI/UX skills (design-system, design-tokens, typography, layout-responsive, component-library, ui-states, motion, scroll-experiences, webgl-3d). Four defect classes, each instance listed with its location:

1. **Slop instances** — every live symptom from the anti-slop table, with its row number (generic hero, uniform sections, pasted-on decoration, template-smell palette swap, dead sections, footer as afterthought).
2. **Missing systems** — no token source (hard-coded values), no type scale, no motion system, no scroll system, incomplete UI states (rest/hover/focus/active/disabled/loading/empty/error), no reduced-motion handling, no skeleton/loading states.
3. **Hard-rule violations** — heavy custom cursor; any reveal that can leave content invisible; pasted-on decoration; motion with no reduced-motion variant; layout-property animation; multiple competing rAF loops.
4. **Architecture leaks** — every instance of §6's ban list found in any user-facing surface, counted by class for the leak audit (FE-371).

**BEFORE score.** Score the app as-is on the design-intelligence quality gate (8 categories, 0–10 each) and record the BEFORE total /80 in the audit file, with the per-category scores and the evidence (screenshots, widths). A BEFORE score is meaningless if any page was skipped: score the worst page, not the landing page.

**Baseline capture (feeds §7).** Before any change, capture the behaviour baseline: the app's routes and primary flows end-to-end (happy path + one error path each), key screenshots per page, and the performance profile (frame rate on a mid-range profile, load weight). The baseline is what regression is measured against — no baseline, no proof of zero regression.

**Structural changes need justification first.** Anything the audit says must change structurally gets its justification written in the audit file BEFORE it is touched (FE-362).

## §2 — Theme decision

Decide once, record the decision and its reasoning in the audit file, then hold it for the whole app (full decision method and worked examples: `specs/02-theme-decision.md`).

**Decision tree.**

1. **Does the app already have an identity worth keeping?** Identity = a palette, type voice, or material language users already recognise as this product, not merely "a colour". If yes → **deepen it**: give it the full treatment — one token source, a real type scale, a motion system and scroll system in its own style, signature elements built from its own content. Do not import a library theme on top of a live identity.
2. **If it has no identity, or its identity is generic AI slop** (starter template + palette swap, gradient hero, default type) → **adopt a library theme whole**, chosen by the design-intelligence decision process (brand personality → audience → content type → theme family → specific theme). Adopt its FULL system from the theme's canonical expanded spec (`skills/frontend/theme-library/expanded/theme-NNN.md`) — palette anchors, typography, motion system, scroll choreography — applied to the project's own content. Never the one-line catalog summary; never the theme's palette alone.
3. **Record the rejected alternative.** At least one named alternative (the other path, or the nearest other theme) and why it was rejected. A decision with no rejected alternative was not a decision.

**Worked reasoning sketch — path A (deepen).** Brief: a 3-year-old internal analytics dashboard, dark navy + mono data voice, engineers already call it "the navy board". Choices: keep navy + mono as the identity; deepen with one token source (navy ramp, one signal accent, tabular numerals), a display/body/data type scale, dial 2 (quiet — a tool, not a story), signature element: the usage chart's own line becomes a live spine that draws the real query volume as the page loads. Why: the identity is real and recognised; replacing it would cost trust and retraining for zero gain. Rejected: adopting a library theme whole (would erase a working identity to chase novelty).

**Worked reasoning sketch — path B (adopt).** Brief: a SaaS billing area built from the framework starter, no identity, every page a different grey. Choices: adopt one library theme whole by the decision process — e.g. an archive/ledger family theme for a finance-adjacent product, dial 2, restrained neutrals + one accent, grotesque + mono-for-data. The theme's expanded spec is the build source for every pass in §3. Why: there is nothing worth keeping, and a whole adopted system beats a decorated template on every category of the score gate. Rejected: "keep the starter and polish it" (polish on a template is still the template — the audit's slop symptoms would survive).

## §3 — Staged passes

Apply each pass across the ENTIRE app before starting the next. Each pass has an entry condition (the previous pass is done everywhere) and an exit criterion (checked before the next pass starts). Full per-pass specs: `specs/03-staged-passes.md`.

| # | Pass | Entry → exit criterion |
|---|---|---|
| 1 | Design tokens | One token source (colour, spacing, radii, shadows, durations, easings); zero hard-coded values outside it. Exit: literal lint clean — grep finds no colour, spacing, or duration literal in component code. |
| 2 | Typography | One modular scale (ratio 1.25 quiet / 1.333 expressive), display/body/data registers, line length 45–75 chars for prose, contrast AA at every state. Exit: no off-scale size, no default font pairing left. |
| 3 | Layout & responsive | One grid, spacing on an 8 pt scale, proximity ratio ≥ 2:1 between vs within groups, breakpoint behaviour per layout-responsive. Exit: no page overflows or collapses at 1440 / 768 / 390 px. |
| 4 | Components & UI states | Every component gets its full state set — rest, hover, focus, active, disabled, loading, empty, error — per component-library and ui-states. Exit: state matrix complete for every component on every page; no fake or missing states. |
| 5 | Motion system | The theme's full motion system on every page (§4). Exit: every §4 term present in-theme or its absence recorded with an in-theme reason. |
| 6 | Scroll experiences | Scroll as a designed system — progress, pinned or scrubbed sections where the theme calls for them — driven by one shared lerped rAF loop, never raw scroll handlers per element. Exit: one loop, smoothed progress, no jitter on fast scroll or trackpad. |
| 7 | Polish | Signature elements (§5) merged into the content; footer designed as a section; reduced-motion variant complete. Exit: merge test passed for every element; JS-off and reduced-motion passes green. |

**Order is load-bearing.** Motion before tokens produces seven unrelated timings; polish before states produces decoration over broken flows. If a pass exposes a defect in an earlier pass, fix it in that pass and re-run its exit criterion — do not patch forward. Per-component upgrade specs: `specs/04-component-upgrades.md`. Framework-specific implementation (React, Vue, plain HTML/CSS/JS): `specs/07-frameworks.md`.

## §4 — Motion system for existing apps

The app gets a COMPLETE motion system in its own style — the same list motion FE-091 requires, translated into this app's material language, never copy-pasted from another theme or app (full per-term specs: `specs/05-motion-system.md`). Every term below is used heavily, each naming its job (feedback, continuity, or the one attention moment); a term that cannot name its job is removed:

- **Scroll-triggered reveals** — choreographed per section (varied distance, duration, mask, order in the app's style), never one identical fade-up on every section. JS-gated hidden states only, force-reveal fallback, re-trigger on re-entry; content fully visible with JS off.
- **Scroll-driven / scrub animation** — values interpolated from smoothed progress; reserved for change, process, or journey the scrub makes clearer than a static diagram.
- **Parallax** — ≤ 3 depths, small offsets, never over forms, tables, or checkout, never making text swim against its background.
- **Pinned sections** — for scenes, not text blocks; one pinned moment per three viewport heights at most.
- **Smooth scrolling** — eased, interruptible, never trapping the user or outrunning reveal triggers.
- **Progress indicator** — real progress (scroll position, task completion, form steps), never decoration; counters and indicators animate only real, sourced figures.
- **Staggered + masked reveals** — entrances staggered by role, masked/clip-path where the theme's material calls for it.
- **Kinetic typography** — type as the event where the line is a claim worth performing; never on legal, instructional, or must-stay-quotable copy.
- **Marquee** — where in-theme, one per page at most, pausable, stopped under reduced motion.
- **Counters** — real numbers only, animated once, final value legible without motion.
- **SVG line-draw** — the line traces something real: a seam, a route, a signature, a data line that balances.
- **Image scale-in-frame** — the image settles inside its frame; the frame never crops content the user needs.
- **Hover / magnetic / tilt micro-interactions** — feather-light, transform-only, immediate feedback; every hover delight gets a tap/scroll equivalent for touch.
- **Custom cursor** — FE-372: system cursor by default; custom only feather-light, transform-only, on the single loop, zero perceptible lag, removed under reduced motion.
- **Skeleton loading** — for real waits over ~300 ms; skeletons for instant loads feel slower than the load.
- **Page transitions** — shared-element continuity between views, never across payment, auth, or error states.
- **Reduced motion** — a complete static variant ships in the same pass as every animation: signature elements in final states, counters at final values, state changes legible, zero loops.

**One loop.** All scroll-linked motion runs on one shared lerped `requestAnimationFrame` loop; scroll values are never applied raw. Animation stays on `transform` and `opacity`. Particle counts are capped and declared. The loop must hold frame budget on a mid-range phone, or one dial level is dropped — never content, readability, or the reduced-motion variant.

## §5 — Signature elements

5–20 signature elements per app, built from the app's own content and material — 3D where possible (webgl-3d), otherwise excellently animated (full build specs per element: `specs/06-signature-elements.md`). Count is per app, not per page: a dashboard's elements live across its pages; a storefront's across catalogue, product, and checkout.

**The merge test (all four must hold).**

1. **It carries content.** Delete-test: removing it removes information or story, not just decoration — the jar holds the collection count, the ledger line balances real totals, the progress spine IS the study plan.
2. **It is built from the content's own material.** Shapes, colours, and behaviour come from the app's real subject and theme — not a generic effects library.
3. **It lives in the layout.** It occupies grid space planned for it, sized so it never covers the content it accompanies at any scroll position; content wins every overlap dispute.
4. **It obeys the page's physics.** Same smoothed scroll progress, same state, same dial as everything around it — no independent loops fighting the page's rhythm.

**Worked sketch.** Dashboard: the usage chart's line lifts out of the chart as a 3D ribbon that the user can scrub along the real timeline — the element IS the data, and removing it removes the ability to read change over time. Storefront: the product's own material (fabric, vessel, grain) reassembles in the hero as the visitor scrolls the product story — the animation demonstrates the product, not decorates beside it. Billing area: the invoice total draws itself as a balancing ledger line across the plan table, debit and credit animating to the real totals.

**Cursor rule (standing).** Cursor effects must never be heavy: if a custom cursor makes the pointer hard to move, it is a defect, not premium. Performance first — feather-light or dropped (FE-372).

## §6 — Architecture leak: the UI must never show the machinery

**Principle (FE-369).** The UI agent must USE all of the app's skills to understand the app — architecture, backend, database, API, and every other skill that describes how it works — but must NEVER surface their internals in the UI. Understanding is input; the UI is output. The test that caught this failure: a generated UI exposed which database the app uses, how many pages it has, and the architecture — everything leaked. That build fails, whatever its visual score.

**Hard ban list — no user-facing surface may contain any of these:** no DB names/types, no table/collection names, no page/route counts or structures, no API endpoints, no internal module/service names, no tech-stack labels, no schema/field names. The UI may only express user-facing concepts (tasks, content, actions the user understands).

**Where leaks hide — check all of them in the audit and at every gate:** navigation labels and section titles ("Users table", "API settings"); empty states and error messages ("No rows in orders_collection", "Failed to fetch /api/v2/invoices", coded errors like `ERR_POSTGRES_23505`); footers and about pages ("Built with Next.js + Supabase", "12 pages"); settings and admin areas that mirror the schema ("Field: user_id", "Collection: sessions"); onboarding copy that counts the product's own structure ("5 pages, 3 modules"); tooltips and placeholders that name endpoints or fields. A leak in an error message is still a leak; a leak only admins see is still a leak — the surface is user-facing if any human reads it.

**How to fix a leak (FE-370).** Translate, never delete the meaning: "No rows in orders_collection" → "No orders yet — create your first order"; "Failed to fetch /api/v2/invoices" → "Couldn't load your invoices — check your connection and try again"; a settings page organised by table name → reorganised by user task ("Your team", "Billing", "Notifications"). If a label cannot be translated into a user concept, the surface itself is wrong — redesign it around the task, do not rename the leak. Full leak taxonomy, translation table, and worked fixes: `specs/09-architecture-leak.md`.

**Leak audit (FE-371).** Inside `UI-UPGRADE-AUDIT.md`, the leak audit is its own section: every leak found, grouped by the seven ban classes above, each with its location and its user-facing replacement — plus a BEFORE leak score (count of leaks, by class) and, after the upgrade, an AFTER leak score. Target: zero leaks. **The leak gate is a veto:** any leak in the shipped UI = gate FAIL, whatever the design-intelligence /80 score is.

## §7 — Regression & rollback

Zero behaviour regression is the pass/fail line for the whole upgrade (full plan: `specs/10-regression-rollback.md`).

**Baseline first.** The §1 baseline (routes, primary flows, screenshots, performance profile) is captured before any change and frozen. Every pass is checked against it: same flows complete, same outcomes, same data shown, same URLs, same API calls.

**Regression checklist (run after every pass, not just at the end).** Every primary flow end-to-end (happy path + one error path); every form submits and validates as before; every state in the §3 pass-4 matrix still reachable; no new console errors; no route removed or renamed; no API call added, removed, or changed in payload; performance profile no worse than baseline on the mid-range profile.

**Feature-flag / branch strategy.** The upgrade lives on its own branch, merged only after the score gate passes; where the app supports flags, each pass ships behind a flag so the old UI can be restored per pass without a redeploy. A pass is never merged on "looks right" — it is merged on checklist green + gate green.

**Rollback plan.** Each pass records its inverse before it starts (token file to restore, component set to revert, flag to flip). If a pass breaks a flow: stop, roll that pass back, record the break and its cause in the audit file, and re-plan that pass — do not patch forward over a broken flow, and never delete the feature the pass broke to make the design easier (FE-362).

## §8 — Scoring & shipping

**Re-score AFTER.** Score the upgraded app with the same design-intelligence gate, same widths (1440 px and 390 px), same eight categories. AFTER must reach ≥ 64/80, every category at or above its threshold, both hard categories (never-invisible safety, reduced motion) at 10. If it fails, loop back to the lowest-scoring category's pass — do not declare completion below the gate (full scoring method: `specs/11-scoring-shipping.md`).

**Every audit defect is fixed or explicitly reported.** The audit file closes with each defect marked fixed (with its pass) or left unchanged with its reason. "Left unchanged" without a reason is an open defect, and the gate fails.

**Before/after report contents.** The audit file closes with: defects found (by class, with counts), passes applied, BEFORE → AFTER score with per-category movement, leak BEFORE → AFTER score (target zero), and anything deliberately left unchanged with its reason. The reply to the user states plainly: what was upgraded, the before/after score, the leak score, and what (if anything) was left and why. No claim of "premium" without the score.

**Scope restated.** Web apps first and only for full specs. A native mobile app gets an adaptation note only: same audit, same theme decision, same leak ban list, same score gate — but motion, scroll, and signature-element specs are re-derived for the mobile platform, not taken from this skill.

## BAN list

- **BAN-FE-181 — Restyle without audit.** Banned: changing any UI before the §1 audit exists. Defeats: DET-VIS-006 (rule FE-361). Bad: a dashboard is "modernised" in a weekend; no audit file, no BEFORE score, and the old slop symptoms survive under a new palette. Instead: write UI-UPGRADE-AUDIT.md first, score BEFORE, then pass by pass. Severity: BLOCK.
- **BAN-FE-182 — Theme swapped per page.** Banned: different themes, palettes, or motion languages on different pages of one app. Defeats: DET-VIS-011 (rule FE-363). Bad: the marketing pages adopt a library theme while settings keeps the starter grey and billing invents a third palette. Instead: one decided theme for the whole app (§2); bend dial and layout by page type, never the theme. Severity: BLOCK.
- **BAN-FE-183 — Pasted-on signature elements.** Banned: any animated element that fails a merge test in §5. Defeats: DET-VIS-028 (rule FE-366). Bad: a glowing particle field behind a pricing table whose sections never mention, fill, or interact with it; a spinning 3D logo covering the hero copy. Instead: rebuild the element from the content's own material, sized into the grid — or cut it. Severity: BLOCK.
- **BAN-FE-184 — Motion that strands content.** Banned: any reveal or animation whose failure mode is invisible content. Defeats: DET-VIS-041 (rule FE-365). Bad: section headings shipped at opacity 0 in CSS; a fast scroll skips their observer and nothing re-checks them, so five headings never appear. Instead: JS-gated hidden states, force-reveal timeouts, re-trigger on re-entry, content complete with JS off. Severity: BLOCK.
- **BAN-FE-185 — Token drift.** Banned: hard-coded colours, spacing, durations, or easings outside the token source, and per-component improvised motion values. Defeats: DET-VIS-001 (rule FE-364). Bad: seven components, seven unrelated timings and three near-identical greys; the interface feels like seven products. Instead: the pass-1 token source, consumed everywhere; the literal lint stays clean. Severity: WARN.
- **BAN-FE-186 — Architecture leak: internals surfaced in the UI.** Banned: any user-facing surface that names the machinery — DB names/types, table/collection names, API endpoints, internal module/service names, tech-stack labels, schema/field names (§6). Defeats: DET-CON-003 (rule FE-370). Bad: an empty state reads "No rows in orders_collection"; a footer reads "Built with Next.js + Supabase"; an error shows `ERR_POSTGRES_23505`. Instead: translate to user-facing concepts — "No orders yet", "Couldn't load your invoices — try again" — or redesign the surface around the task. Severity: BLOCK.
- **BAN-FE-187 — Structure leak: counts and maps of the app itself.** Banned: UI copy or navigation that exposes the app's own structure — page/route counts or structures, sitemap-style nav, endpoint paths in labels or tooltips. Defeats: DET-UX-006 (rule FE-370). Bad: onboarding copy boasts "5 pages, 3 modules"; a settings nav lists routes as "GET /api/v2/invoices"; a tooltip shows a field name instead of what the field means. Instead: organise by user task and name things by what the user does with them, never by where they live in the code. Severity: BLOCK.

## Gates

- **G-FE-181 — Audit completeness.** Verifies: FE-361, FE-371. Check: manual — read UI-UPGRADE-AUDIT.md before any UI change: every page and component listed, defects grouped by the four §1 classes, BEFORE score recorded with evidence, baseline captured. Pass: nothing exempt, worst page scored. Fail: no UI work starts. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-182 — Staged-pass exit.** Verifies: FE-364. Check: manual + automated — after each §3 pass, its exit criterion is evidenced (literal lint clean after pass 1; no overflow at 1440/768/390 after pass 3; state matrix complete after pass 4; one loop, no jitter after pass 6). Pass: exit criterion green for the whole app. Fail: the next pass does not start. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-183 — Motion and safety audit.** Verifies: FE-365, FE-372. Check: manual + device — fast-scroll and trackpad passes on a mid-range phone; every §4 term present in-theme or its absence recorded; reveals JS-gated with force-reveal fallback; reduced-motion emulation shows a complete static page; cursor is the system cursor or a feather-light exception with zero perceptible lag. Pass: no jitter, no stranded content, no heavy cursor. Fail: block shipment. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-184 — Signature merge check.** Verifies: FE-366. Check: manual — for each of the 5–20 signature elements, run the four §5 merge tests with screenshots as evidence. Pass: every element passes all four; count is 5–20. Fail: rebuild the element into the content or cut it. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-185 — Regression gate.** Verifies: FE-362, FE-367. Check: automated + manual — run the §7 regression checklist against the frozen §1 baseline after every pass and before merge: flows, forms, states, console, routes, API calls, performance. Pass: zero behaviour regression. Fail: roll the pass back (§7), record the break, re-plan. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-186 — Leak audit (veto).** Verifies: FE-369, FE-370, FE-371. Check: manual — walk every user-facing surface (navigation, labels, empty states, errors, footers, settings, onboarding, tooltips) against the §6 ban list; count leaks by class into the audit file's BEFORE and AFTER leak scores. Pass: AFTER leak score is zero. Fail: veto — the gate fails and shipment blocks, whatever the /80 score is. A single leak is a FAIL. Recorded in: UI-UPGRADE-AUDIT.md.
- **G-FE-187 — Final score gate.** Verifies: FE-368, FE-371. Check: manual scoring of the upgraded app on the eight design-intelligence categories at 1440 px and 390 px, hard categories tested directly (JS disabled; reduced-motion emulation on), plus the AFTER leak score from G-FE-186. Pass: total ≥ 64/80, every category at threshold, hard categories at 10, leak score zero, every audit defect fixed or explicitly reported with its reason. Fail: loop back to the lowest-scoring category's pass; never declare completion below the gate. Recorded in: UI-UPGRADE-AUDIT.md.

## Anti-patterns

- **Restyle without audit.** The upgrade starts in the editor; the audit is written afterwards to rationalise what was made. Catch it: G-FE-181 runs before any UI change — no audit, no work.
- **Theme swapped per page.** Each page gets the theme its builder liked that day; the app reads as five products. Catch it: one decided theme (§2) checked at G-FE-182; a page that bends the theme is recorded, a page that abandons it is reverted.
- **Pasted-on signature elements.** Expensive animated set-pieces dropped onto pages they do not belong to. Catch it: the §5 merge test at G-FE-184 — if deleting it loses only decoration, it was pasted on.
- **Motion that strands content.** Reveals shipped in CSS, observers with no fallback, fast scrolls that skip triggers. Catch it: G-FE-183 — block the observer and assert every reveal still lands visible.
- **Token drift.** Each pass reintroduces hard-coded values and improvised timings because "this one is special". Catch it: the pass-1 literal lint re-run at every gate; drift is fixed in the token source, never in the component.
- **"Premium" claimed without a score.** The upgrade is declared done because it looks good in a screenshot. Catch it: G-FE-187 — no score, no ship; and a leak anywhere vetoes the ship even at 64/80 or above.
- **Leak by renaming.** An internal name is relabelled cosmetically ("orders_collection" → "Orders Collection") and called fixed. Catch it: G-FE-186 checks meaning, not spelling — if the surface still organises by the schema instead of the user's task, it still leaks.

## Examples

- `examples/example-1.md` — Internal analytics dashboard: starter-grey default vs a deepened navy/mono identity at dial 2, whose usage ribbon IS the data. Corrects FE-361, FE-363, FE-366, FE-369.
- `examples/example-2.md` — E-commerce storefront: template shop vs one library theme adopted whole, product material reassembling in the hero. Corrects FE-363, FE-364, FE-365, FE-370.
- `examples/example-3.md` — SaaS settings/billing area: schema-mirroring settings vs task-organised billing with a balancing ledger line — and a leak audit that goes to zero. Corrects FE-362, FE-367, FE-370, FE-371.
- Worked end-to-end case studies (dashboard, storefront, settings/billing — each with BEFORE → AFTER scores and a leak audit): `specs/08-case-studies.md`.

## Recall anchors

- Audit first: no audit, no UI work; score the worst page, not the landing page.
- One theme, whole app, passes in order — a half-done pass everywhere is not a pass.
- If deleting it loses only decoration, it was pasted on.
- Use the internals to understand; never show them — any leak vetoes the ship.
- No score, no "premium": ≥ 64/80, hard gates at 10, leak score zero, or fix and re-score.

## Checklist

- [ ] UI-UPGRADE-AUDIT.md written before any UI change: all pages/components, four defect classes, BEFORE score, baseline captured (G-FE-181).
- [ ] Leak audit inside the audit file: leaks counted by ban class, BEFORE leak score recorded (FE-371).
- [ ] Theme decision recorded with its reasoning and one rejected alternative (FE-363).
- [ ] Behaviour baseline frozen: routes, flows, screenshots, performance profile (FE-362).
- [ ] Passes applied whole-app in §3 order, each exit criterion evidenced before the next starts (G-FE-182).
- [ ] Full motion system present on every page, each term in-theme or its absence recorded (FE-365).
- [ ] 5–20 signature elements, each passing all four merge tests (G-FE-184).
- [ ] System cursor, or a feather-light custom cursor with zero perceptible lag (FE-372).
- [ ] Regression checklist green after every pass; broken pass rolled back, not patched forward (G-FE-185).
- [ ] Reduced-motion variant complete and JS-off reading verified (G-FE-183).
- [ ] AFTER leak score is zero — leak gate veto checked on every user-facing surface (G-FE-186).
- [ ] AFTER score ≥ 64/80, hard categories at 10, every defect fixed or reported with reason, before/after report closed (G-FE-187).
