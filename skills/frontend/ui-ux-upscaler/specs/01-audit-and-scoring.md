# UI/UX Upscaler — Spec 01: Audit and Scoring

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Authority:
> Existing-Project Upgrade Protocol v1.3.0 Step 1 (`custom-instructions/claude.md`
> lines 83–175) and `skills/frontend/design-intelligence/SKILL.md` §4–§5.
> This file expands Step 1 only. It does not decide a theme (→ `02-theme-decision.md`),
> does not prescribe passes (→ `03-staged-passes.md`), does not score the AFTER state
> except by re-running the method in §5 of this file.
> **SCOPE: web apps ONLY** (native mobile apps get an adaptation note only,
> `02-theme-decision.md` §8, not full specs).
> Cross-references: `04-component-upgrades.md` (per-component defect checks),
> `05-motion-system.md` (motion defect checks), `08-case-studies.md` (worked audits).

## 1. The audit-first rule

1.1 No token, type, layout, component, motion, or signature-element change is made
before `UI-UPGRADE-AUDIT.md` exists at the project root and contains a BEFORE score.
A diff that precedes the audit is reverted, not reviewed.

1.2 An audit with no applied upgrade is a failed task (Protocol Step 1, verbatim rule).
The audit file is therefore written as a work order, not a report: every defect entry
ends in a pass number (`03-staged-passes.md` §2–§8) and an owner route/component.
A defect with no pass assignment is an incomplete audit entry.

1.3 Audit budget: 0.5–2 working days for apps under 40 routes; 2–4 days for 40–150
routes; above 150 routes, audit by route family (see §6) and sample 3 routes per family
in full plus a 10-route spot sweep. Never audit only the landing page: the Protocol
states "Nothing is exempt — every page and component."

1.4 Evidence rule: every scored category (§5) and every defect (§3) carries evidence
— a file path + line range, a screenshot at 1440 px and 390 px, or a measured number
(contrast ratio, frame time, load ms). An assertion without evidence scores as if the
defect were unconfirmed: it is listed as `UNCONFIRMED` and does not move the score
until evidence is attached.

## 2. The UI-UPGRADE-AUDIT.md template

Write the file exactly in this section order. Sections marked `[REQUIRED]` may not be
omitted; `[CONDITIONAL]` sections appear only when the condition holds. Delete no
section to save space — an empty section is filled with `None found — checked <date>
by <method>`, never deleted.

```markdown
# UI Upgrade Audit — <Product name> — <YYYY-MM-DD>

## 0. Audit meta [REQUIRED]
- App: <name, repo URL, commit SHA audited>
- Auditor: <name/agent> · Date: <YYYY-MM-DD> · Viewports checked: 1440×900, 1280×800, 768×1024, 390×844, 360×640
- Routes inventoried: <N> routes in <M> families (table in §1)
- Method: manual walk + automated checks (list tools: e.g. axe, Lighthouse, Playwright no-JS pass, reduced-motion emulation)
- BEFORE score: <X>/80 (method §5; per-category table in §6)

## 1. Route & component inventory [REQUIRED]
| Family | Routes | Components used | Owner (if known) |
| Landing/marketing | / , /pricing, /about | Nav, Hero, PricingTable, Footer | … |
| Dashboard | /app, /app/reports | StatCard, Chart, DataTable, FilterBar | … |
| … | … | … | … |
- Unrouted / orphaned components found: <list or "none">
- Dead routes (404, redirect loops, unreachable): <list>

## 2. Defect list [REQUIRED]
### 2.1 AI-slop instances (taxonomy §3.1 — one row per instance)
| ID | Location (file:line / route) | Symptom (§4 row) | Evidence | Severity | Pass |
| A-01 | src/components/Hero.tsx:12 / / | Generic centred hero, gradient + default font | screenshot hero-1440.png | BLOCK | 2,5,7 |
### 2.2 Missing systems (§3.2)
| System | Present? | Evidence | Pass |
| Design tokens | No — 214 hard-coded hex values (grep count) | grep -r "#[0-9a-fA-F]\{6\}" src \| wc -l = 214 | 1 |
### 2.3 Hard-rule violations (§3.3)
| Rule | Location | Evidence | Pass |
| Heavy custom cursor | src/App.tsx:44 cursor-follow div, 200 ms lag | video cursor-lag.mp4; pointer overshoot on 3/5 clicks | 5 (remove) |

## 3. Architecture-leak audit [REQUIRED] — LEAK AUDIT section (expanded orders 2026-11-24)
- User-facing surfaces checked: <list — nav labels, headings, error strings, empty states, URLs, page titles>
- Leaks found (DB names/types, table/collection names, page/route counts, API endpoints, module names, tech-stack labels, schema/field names): <table: leak | surface | fix | pass>
- **Leak score BEFORE: <N leaks> → AFTER: <M leaks> / target 0.** Both numbers are recorded in this section: BEFORE at audit time, AFTER at close-out (re-counted in full — the AFTER count is a fresh sweep per `09-architecture-leak.md` §4, not a subtraction of "fixed" items).
- **Leak count as a scored item:** the leak score stands BESIDE the /80 total as its own scored line (it is NOT folded into the /80 — folding it would let a high /80 average it away). The audit file §5 table carries the line: `Leak score: BEFORE <N> → AFTER <M> / target 0`.
- **Gate FAIL veto:** ANY leak = gate FAIL regardless of the /80 score. A 72/80 app with 1 leak does not ship; a 79/80 app with 1 leak does not ship. The veto is recorded in the sign-off line (§8): `GATE: PASS only if /80 ≥64 AND hard categories 10/10 AND leak score = 0`. A leak is never "left unchanged" — if it cannot be rewritten in user concepts, the surface that leaks is removed (`09-architecture-leak.md` §6 rewrite rule, §7 translations).
- **Detection method:** copy scan + error-path walkthrough + route/label inventory vs user concepts + non-technical-user test — full method in `09-architecture-leak.md` §4; the audit walk step 6 (§4 of this file) runs it. Ban list with rationale per item: `09` §2 (B-1–B-8). Checklist for the gate: `09` §5 (L-1–L-8).
- **Worked pairs:** at least 8 leak-vs-clean pairs in `09` §6 (L-1–L-12); each leak in this section's table cites the pair it follows.

## 4. Theme decision [REQUIRED — filled by 02-theme-decision.md]
- Path: deepen own identity | adopt library theme <theme-NNN>
- Decision record: inputs (§1.1 of 02), rejected alternative + reason, dial per page (table)
- (This section is a pointer: the full record lives here, not in a side document.)

## 5. BEFORE score [REQUIRED — method §5]
| Category (design-intelligence §5) | Score /10 | Threshold | Evidence |
| 1. Hierarchy & focal order | 4 | ≥8 | … |
| … 8 rows … | | | |
| TOTAL | 38/80 | ≥64 AFTER | |
- Hard categories (6 Never-invisible, 7 Reduced motion): <score> — must be 10 AFTER; BEFORE value recorded honestly.
- Lowest category first: <category N> — the first pass to fix (§5.4).

## 6. Pass plan [REQUIRED]
- Pass order per 03-staged-passes.md; per-pass route order (highest-traffic / highest-defect-density first); rollback point per pass (git tag or commit).

## 7. Deliberately unchanged [REQUIRED — filled at close, see §7]
| Item | Reason it stays | Re-check date |
- (At audit time this section holds only items already ruled out of scope with a written reason; it is completed at close.)

## 8. Close-out — BEFORE → AFTER [REQUIRED at close]
- AFTER score table (same 8 rows, re-scored in full — pre-fix scores void)
- Defects fixed: <N>/<M>; defects explicitly left with reason: <list, each with a reason>
- Regression evidence: <links — no-JS pass, reduced-motion pass, scroll profile, screenshots 1440/390>
- Sign-off: <name, date> — "AFTER ≥64/80, all thresholds met, hard categories 10/10, leak score 0, or NOT SIGNED — reason"
```

### 2.1 Filled example excerpt (fictional app "Northwind Ledger", §8 case (a) source data)

```markdown
## 2. Defect list (excerpt — 3 of 41 defects)
| ID | Location | Symptom | Evidence | Severity | Pass |
| A-01 | src/pages/Landing.tsx:8 / / | §4 #1 generic centred hero: linear-gradient(#6366f1,#8b5cf6), Inter 400, single "Get started" button; identical to starter template | screenshot landing-1440.png; hero copy could describe any SaaS (3-second test: "what is it about?" failed 2/3 testers) | BLOCK | 2,5,7 |
| A-07 | src/components/DataTable.tsx:61 /app/invoices | §4 #5 content invisible: rows render opacity:0 in CSS, IntersectionObserver fires once; fast scroll past 200 rows leaves 37 rows blank until reload | video fast-scroll.mp4 00:41; observer-stub test strands 37/200 rows | BLOCK | 4,6 |
| A-19 | src/App.tsx:44–71 | §4 #8 heavy custom cursor: 64 px follower div, spring lag ≈200 ms, pointer overshoots nav links on 3/5 attempts | cursor-lag.mp4; input latency +180 ms measured | BLOCK | 5 (remove in Pass 5) |
## 3. Architecture-leak audit (excerpt)
| Leak | Surface | Fix |
| "PostgreSQL" | /app/settings "Connected database: PostgreSQL 15" | Replace with "Your data is stored securely" — no DB name, no version |
| "12 pages" | /app sidebar footer "12 pages · 4 modules" | Remove count entirely |
| Leak score BEFORE: 6 | Target AFTER: 0 |
## 5. BEFORE score (excerpt — full table in the real file)
| 1 Hierarchy | 4/10 | 2 Integration | 3/10 | 3 Readability | 6/10 | 4 Motion smoothness | 3/10 |
| 5 Performance | 5/10 | 6 Never-invisible | 4/10 | 7 Reduced motion | 0/10 | 8 Aliveness | 3/10 |
| TOTAL 28/80 — wait, recomputed: 4+3+6+3+5+4+0+3 = 28/80. (The excerpt above is illustrative; the real file must show its own arithmetic — see §5.3 rule: always show the addition.) |
```

> Note on the excerpt: the arithmetic line is deliberately shown, because §5.3 requires
> the addition to be visible in the audit file. A total with no visible addition is
> treated as unscored.

## 3. Defect taxonomy

### 3.1 AI-slop instances — how to find each class in a real codebase

| Class | What it is | How to find it (codebase + rendered page) |
|---|---|---|
| S-1 Template hero | Centred hero, gradient wash, default/system font, one generic CTA, stock abstract image | Render `/` at 1440 px; 3-second test (§5.2). Grep for `linear-gradient` in hero files + `font-family: Inter, system-ui` with no display face. If the hero copy survives a find-replace of the company name with a competitor's, it is S-1. |
| S-2 Uniform sections | Every section same block: 96 px padding, centred heading, 3-card row, new copy | Full-page screenshot; measure section padding variance — if ≥80% of sections share padding within ±8 px and the same grid, S-2. Grep for repeated section class names. |
| S-3 Pasted decoration | Blobs, waves, particle rain, glassmorphism panels unrelated to the product | Screenshot walk; for each decorative element ask the merge test (design-intelligence §3.3): remove it — does any information or story leave? No → S-3. Grep for `blob`, `particle`, `wave`, `glass` in component names. |
| S-4 Jitter / stutter | Scroll animation jumps on fast scroll, trackpad steps, 120 Hz | Profile a full-page scroll on CPU-throttled mid-range profile; look for `addEventListener('scroll'` handlers doing layout reads/writes, and for `transition` on `width/height/top/left`. |
| S-5 Stranded content | Headings/cards never appear (observer missed, no fallback) | Playwright: disable IntersectionObserver, load each route, assert every section visible within its fallback window (none exists → defect). Also: JS-off load, assert all text present. |
| S-6 Dead sections | Viewport stretches with no motion, no focal change, no reason to look | Scroll the full page at reading speed; mark every viewport where nothing moves, changes, or holds attention for >2 viewport heights. |
| S-7 Motion pile-up | Everything animates at once; no focal mover | Count simultaneous animated elements per viewport in a screen recording; >1 attention moment per viewport = S-7. |
| S-8 Heavy cursor | Custom cursor lags, sticks, fights pointer | Move pointer across nav at normal speed; measure overshoot and click-miss rate (≥1 miss in 5 = defect). Grep for `cursor: none` + follower divs. |
| S-9 Invented numbers | Counters/stats nobody can source ("10,000+ happy users", "99.9%") | For every animated counter and every stat on the page, demand the source: DB query, analytics export, or named document. No source → S-9; the counter is removed, not reworded. |
| S-10 Palette-only reskin | Colours changed, layout family untouched — still smells like the starter | Diff the layout grid/pacing against the framework starter the app was built from; if grid, section order, and component set match the starter and only hex values differ, S-10. |
| S-11 Unreadable over motion | Text over dark scenes, video, or animated backgrounds fails contrast at some scroll state | Measure contrast at rest, mid-reveal, and scrolled-past states (not just rest). Any state < 4.5:1 body / 3:1 large text = S-11. |
| S-12 Starter-pack techniques | Marquee + counters + tilt on every section, same durations | Inventory every technique instance per page; any technique appearing ≥3 times with identical duration/easing and no distinct job (design-intelligence §3.1) = S-12. |
| S-13 Hover-only delight | Delight exists on hover; touch gets a lesser site | Test every hover delight at 390 px touch emulation; no tap/scroll equivalent = S-13. |
| S-14 Heavy page | Fans spin, scroll hitches, long tasks | Lighthouse + DevTools Performance: total long tasks > 200 ms on a full scroll, or >2 rAF loops, or unbounded particle counts = S-14. |
| S-15 Orphan footer | Footer looks like a different, older website | Compare footer type, spacing, palette, and motion against the rest of the page; any two mismatches = S-15. |
| S-16 Default type | Framework default type throughout; no display/body/data registers | Check type scale: if body is the framework default size/face and no display face exists, S-16. Grep for font declarations outside the token file. |
| S-17 No reduced-motion variant | `prefers-reduced-motion` absent or partial | Grep shipped CSS for `prefers-reduced-motion`; zero hits while any animation exists = S-17 (BLOCK). Emulate reduced motion and scroll: any continuing non-essential motion = S-17. |
| S-18 No pacing | Loud throughout; no quiet section | Map section loudness (size × contrast × motion) down the page; if no quiet section in any run of 3 sections, S-18. |
| S-19 Covering element | A showcase element covers the content it decorates at some scroll position | Scroll every route at 1440 px and 390 px; any overlap where an animated/decorative element covers text, a control, or a data value at any scroll position = S-19 (BLOCK — cf. design-intelligence §4 #19, the Side A / Side B reel defect). |

### 3.2 Missing systems — the checklist that must be run, not assumed

| System | Present means (auditable test) | Absent means |
|---|---|---|
| Design tokens | One token source file; grep for hard-coded hex/rgb/px spacing outside it returns 0 (excluding third-party CSS) | Any hard-coded value in app code; count and record the number |
| Type scale | One modular scale (ratio stated, e.g. 1.25 or 1.333); every display/body size is on-scale; line length 45–75 ch prose | Off-scale sizes exist; body <16 px or >18 px without a recorded reason |
| Motion system | Named durations/easings as tokens; every animation names its job (design-intelligence §3.1); one rAF loop | Improvised durations per component; >1 rAF loop; any animation without a job |
| Scroll system | Scroll-triggered reveals (varied, not uniform fade-up), scrubbed animation, in-theme progress, pins where earned | Long page with static stacking; or uniform `data-aos="fade-up"` on all sections |
| UI states | Every component has rest/hover/focus/active/disabled/loading/empty/error designed (see `04-component-upgrades.md` §1 matrix) | Any component missing ≥2 states; loading shown as a blank area; errors as browser defaults |
| Reduced-motion handling | Complete static variant per element; `prefers-reduced-motion` block wherever animation exists | See S-17 |
| Skeleton/loading | Real waits ≥300 ms show skeletons matching the layout; waits <300 ms show nothing (no flash) | Spinners on instant loads; blank waits; skeleton shapes that do not match the content |
| Accessibility baseline | Focus visible everywhere; keyboard walk reaches every control; aria labelling on icon-only controls; touch targets ≥44×44 px | Any keyboard trap, invisible focus, or target <44 px |

### 3.3 Hard-rule violations

| Rule (Protocol Step 5) | Violation test | Severity |
|---|---|---|
| System cursor only | Any `cursor: none` + follower, or any cursor effect with perceptible lag (>0 ms perceptible trailing, measured as pointer-to-follower delay >16 ms) | BLOCK — remove in Pass 5; do not "lighten" a heavy cursor, remove it |
| No stranded content | JS-off load leaves any text invisible; observer-stub test strands any section | BLOCK |
| Reduced motion shipped with the animation | Any animation committed without its reduce variant in the same pass | BLOCK |
| Performance budget held | Frame budget broken on mid-range profile (see `05-motion-system.md` §7) | BLOCK if long tasks >200 ms on scroll |
| Content first (JS-off readable) | Any route unreadable with JS disabled, without a written stack reason in the audit | BLOCK unless the reason is recorded and the stack genuinely requires JS (SPA shell with no SSR — then the reason must name the stack and the mitigation) |
| Architecture leak | Any leak in §2 §3 table | BLOCK for the AFTER gate (leak score must reach 0) |

## 4. How to find defects in a real codebase — the audit walk

Order matters. Do not start at the code; start at the rendered product.

1. **Inventory (30–90 min).** Crawl routes (sitemap, router config, nav). List every route
   in §2 §1. Count components per route from the router + imports. Note orphaned
   components (imported nowhere) and dead routes.
2. **Rendered walk, 1440 px (half day).** Every route, top to bottom, at reading speed.
   Screenshot full pages. Run the 3-second test on every landing/hero viewport. Walk
   the design-intelligence §4 table row by row (19 symptoms) against the screenshots.
3. **Rendered walk, 390 px (half day).** Same routes at touch emulation. Check every
   hover delight for a tap equivalent; check every pinned element for focus-obscuring
   and clipping at 360×640 and 1280×600 (scroll-experiences BAN-FE-054).
4. **Codebase sweep (half day).** Greps: hard-coded hex (`#[0-9a-fA-F]{3,8}`), hard-coded
   durations (`\d+ms|\.\d+s` outside the token file), `addEventListener('scroll'`,
   `cursor: none`, `opacity: 0` in CSS (not JS-gated), `data-aos`, particle counts,
   `getBoundingClientRect` in scroll handlers. Count each; record counts, not vibes.
5. **Automated passes (half day).** axe (accessibility), Lighthouse (performance,
   best-practices), Playwright no-JS load per route, Playwright reduced-motion emulation
   scroll, Playwright observer-stub force-reveal test (`05-motion-system.md` §6.4).
6. **Leak sweep (1–2 h).** Grep user-facing strings for DB names, table/collection names,
   endpoint paths, module names, tech-stack labels, counts of pages/routes/modules.
   Read every error string, empty state, and settings label aloud: would a non-technical
   user understand it without knowing the stack? No → leak.
7. **Score (§5).** Score only after steps 1–6. Score from evidence, not memory.

## 5. The BEFORE score method (design-intelligence §5 gate)

### 5.1 Instrument

Eight categories, 0–10 each, total /80. Thresholds are per-category, not just total:

| # | Category | 10 looks like | Threshold |
|---|---|---|---|
| 1 | Hierarchy & focal order | Every viewport has an obvious 1-2-3; 3-second test passes cold | ≥8 |
| 2 | Element integration | Every signature element passes all four merge tests (§3.3 of design-intelligence) — on an existing app, score the decorative elements it already has; absent elements score by the gap (no merged elements = ≤3) | ≥8 |
| 3 | Readability & contrast | All text ≥ WCAG AA (4.5:1 body, 3:1 large) at every scroll state, over every animation | ≥9 — hard |
| 4 | Motion smoothness | Smoothed scroll throughout; no jitter on fast scroll, trackpad, 120 Hz; transform/opacity only | ≥8 |
| 5 | Performance | One rAF loop; capped particles; smooth on mid-range phone; no layout thrash | ≥7 |
| 6 | Never-invisible safety | JS off = fully readable; every reveal has a fallback; re-entry re-triggers | 10 — hard, binary |
| 7 | Reduced motion | Complete static variant: final states, full content, zero loops | 10 — hard, binary |
| 8 | Aliveness | No section feels dead; stillness, where used, is visibly deliberate | ≥7 |

**Pass rule (AFTER):** total ≥64/80 AND every category at/above threshold AND both
hard categories at 10. A total ≥64 with a hard category at 9 is a FAIL.

### 5.2 Scoring each category on a real app — anchors per score band

Score honestly, as a hostile reviewer (design-intelligence FE-329). Use these anchors;
do not score by effort.

- **Cat. 1 Hierarchy:** 0–2 — no focal order anywhere (S-1 + S-2 both live); 3–4 — hero
  has a focal point but sections tie or compete; 5–7 — most viewports have 1-2-3 but
  ≥2 viewports tie; 8–9 — every viewport has 1-2-3, 3-second test passes on all landing
  viewports; 10 — plus the focal margin is ≥1.6× size or a full weight step + sole accent
  everywhere, verified at 1440 px and 390 px.
- **Cat. 2 Integration:** 0–2 — decoration is all pasted-on (S-3 live, merge test fails
  everywhere); 3–5 — some elements carry content, most do not; 6–7 — most pass 3 of 4
  merge tests; 8–9 — every element passes all four; 10 — plus removing any element
  visibly removes information (the delete-test is demonstrable, not asserted).
- **Cat. 3 Readability:** measure, do not eyeball. 10 = 0 failures across all states;
  9 = ≤2 minor failures on non-body text, fixed in Pass 2; 8 = failures on body text in
  one state; ≤7 = failures at rest. Any rest-state body failure caps the category at 7.
- **Cat. 4 Motion smoothness:** 0–2 — raw scroll handlers, visible jitter; 3–5 — some
  smoothing, jitter on fast scroll or trackpad; 6–7 — smooth on desktop, jank on
  throttled mobile; 8–9 — smooth everywhere, transform/opacity only; 10 — plus
  120 Hz clean and no per-effect disagreement.
- **Cat. 5 Performance:** use Lighthouse + scroll profile numbers. 10 = no long task
  >50 ms on scroll, one loop, capped particles; 7 = longest scroll task ≤100 ms;
  5 = ≤200 ms; ≤4 = >200 ms or fans spin on a mid-range phone.
- **Cat. 6 Never-invisible:** binary in practice — 10 = JS-off fully readable AND
  observer-stub test strands 0 sections; anything else scores the fraction visible
  (e.g. 37/200 rows stranded → 10 × 163/200 ≈ 8, rounded down to 8); a page that is
  blank with JS off scores 0. The AFTER requirement is 10, so record the exact
  stranded count, not just the score.
- **Cat. 7 Reduced motion:** 10 = complete static variant, zero continuing non-essential
  motion under emulation, all end states legible; 5 = a reduce block exists but loops
  continue; 0 = no reduce handling at all (the common BEFORE score — see case studies).
- **Cat. 8 Aliveness:** 0–2 — dead stretches >2 viewports (S-6); 3–5 — hero-only life;
  6–7 — most sections alive, 1–2 dead stretches; 8–9 — no dead stretch, stillness
  deliberate where used; 10 — plus ambient life is in-theme at every depth.

### 5.3 Arithmetic and evidence rules

- Show the addition in the audit file: `4+3+6+3+5+4+0+3 = 28/80`. A total without
  visible addition is unscored.
- Attach evidence per category: screenshot pair, measurement, or test output name.
  A category scored without evidence is marked `UNCONFIRMED` and the audit is incomplete.
- Score per route family, then roll up: the app-level BEFORE score is the
  **lowest family score**, not the average. An app whose landing scores 58/80 and whose
  settings scores 30/80 is a 30/80 app — averaging hides the worst page, and the worst
  page is what the user experiences. Record the per-family table; the headline number
  is the minimum.
- Re-scoring: after any fix, re-score the WHOLE app (all 8 categories, all families).
  Pre-fix scores are void. Never carry a category score across a fix.

### 5.4 Fix order

Fix the lowest-scoring category first (design-intelligence §5). Ties break toward the
hard categories (6, then 7, then 3), then toward the category with the most BLOCK defects.
Record the fix order in §2 §6 of the audit file.

## 6. Audit walkthroughs — 4 page types

### 6.1 Landing / marketing page

Walk: hero (3-second test) → social proof → features → pricing → FAQ → footer.
Check S-1, S-2, S-10, S-15 first; then S-3/S-19 (hero showcase element covering copy —
the most common landing BLOCK); then counters (S-9 — demand a source for every number
in the proof section). Measure section padding variance (S-2 test: ≥80% identical
padding = defect). Check the footer against the page (S-15: two mismatches = defect).
Dial expectation: landing pages usually land at dial 3–4 AFTER; BEFORE they are
typically dial 0 (no system) — score Cat. 8 accordingly, not generously.

### 6.2 Dashboard

Walk: nav/sidebar → stat cards → charts → tables → filters. Check: stat cards for
invented numbers (S-9 — a dashboard's numbers must be live data; a hard-coded "12,482
users" in a card is both S-9 and a data-integrity defect); tables for S-5 (stranded rows
on fast scroll — the most common dashboard BLOCK); filters for missing states (no
empty state for a filter combination that returns 0 rows = missing-system defect);
charts for unreadable labels over animation (S-11) and for hover-only tooltips (S-13 —
touch users get no values). Density: dashboards are read repeatedly — reveals fire
once per session or not at all; score Cat. 8 by whether the dashboard feels alive
(live data ticking, in-theme) without spectacle, not by how much moves.

### 6.3 Form-heavy flow (signup, checkout, multi-step wizard, settings forms)

Walk: step by step, including the error path and the success path. Check: every input
for its full state matrix (see `04-component-upgrades.md` §3 — missing focus, error,
or disabled states are defects, one row each); validation messages for architecture
leaks ("422: users.email unique constraint" is a leak AND a readability defect);
multi-step progress for honesty (a progress bar that jumps 25%→100% on the last step
is a Cat. 1 defect); the success state for feedback theatre (a 900 ms flourish before
the next action unlocks = motion FE-087 violation). Dial: task flows dial down
(design-intelligence §3.2) — score Cat. 4/8 against dial 1–2 expectations, not dial 4;
a checkout that pins, scrubs, and marquees is worse than a quiet one.

### 6.4 Content / listing page (blog index, catalogue, search results, docs)

Walk: list controls (sort/filter/search) → first 10 items → pagination/infinite scroll →
item detail. Check: listing density and scannability (line length, row height, image
weight — a listing whose cards are 3 different heights for no reason is S-2); infinite
scroll for S-5 (items loaded below the fold that never reveal); search for its empty
state ("No results for 'X'" with no next action = missing-system defect); detail pages
for S-6 dead stretches (long articles with no progress, no pull-quote, no in-theme life).
Reveals fire once per session on listings (repeat visitors re-scan daily) — a listing
that re-animates every visit scores Cat. 4 down, not up.

## 7. Closing the audit (Step 7)

At close, §2 §8 of the audit file is completed: AFTER score table (same 8 rows,
re-scored in full), defects fixed N/M, defects left with a reason each, regression
evidence (no-JS pass output, reduced-motion pass output, scroll profile, 1440/390
screenshot pairs before/after). The sign-off line is either a pass or an explicit
non-sign with a reason — never a soft pass ("mostly done", "good enough"). A defect
left unfixed without a reason is a failed close-out, and the audit file says so.

## 8. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §2 template | SKILL.md Step 1; every case study in `08-case-studies.md` follows it |
| §3 taxonomy | `04-component-upgrades.md` §1 (component-level defect checks); `05-motion-system.md` §6 (motion defect checks) |
| §5 scoring | `08-case-studies.md` (BEFORE/AFTER tables); `03-staged-passes.md` §9 (gate loop) |
| §6 walkthroughs | `04-component-upgrades.md` (dashboard, forms, listings sections) |
