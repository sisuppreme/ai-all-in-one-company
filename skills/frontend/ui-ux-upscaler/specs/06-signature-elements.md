# UI/UX Upscaler — Spec 06: Signature Elements

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Expands Protocol
> Step 4 Pass 7 (polish). Authority: design-intelligence §3.3 (merge test), §7
> (worked examples); motion FE-092/FE-094; EXPANSION-STANDARD.md §6 (per-element
> full build spec, v2 deepening layers).
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** a signature element is built from the app's USER-VISIBLE
> content/data only — never from its tables, endpoints, modules, or schema. An element
> named after, shaped by, or labelled with a stack internal fails Pass 7
> (`09-architecture-leak.md` §4). Count 5–20 per app.

## 1. Count, placement, and the merge test

- **Count:** 5–20 signature animated elements per app (not per page). Fewer than 5 =
  the app has no identity; more than 20 = decoration is accreting (motion FE-094's
  "dial that only goes up" anti-pattern). The count is recorded in the audit file §8
  with each element's page and grid home.
- **Placement:** at most one spectacle element per 3 viewport heights of scroll
  (FE-328); at most one attention moment per viewport (motion FE-088). Elements are
  distributed by page family in the decision record — a landing page may carry 6–8,
  a dashboard 5–6 quiet ones, a checkout 0–1 (dial 1–2; a checkout element must be
  nearly still — e.g. a progress line that fills, not a scene).
- **The merge test (all four must hold — design-intelligence §3.3):**
  1. It carries content — remove it and the page loses information or story, not decoration.
  2. It is built from the content's own material — shapes, colours, behaviour from the
     theme's world and the brand's real subject, not a generic effects library.
  3. It lives in the layout — planned grid space, sizes that never cover the content
     it accompanies at any scroll position (S-19 = automatic fail).
  4. It obeys the page's physics — same smoothed scroll progress, same state, same dial
     as everything around it; no independent loops fighting the page's rhythm.
  An element failing any one is pasted-on spectacle (BAN-FE-162): rebuild it into the
  content or cut it. "Make it subtler" is not a fix.

## 2. Element ideation from the app's own content/data (not from a generic list)

Never start from a list of effects. Start from the app's real content and ask, per
page family, four questions in order:

1. **What does the user count, track, or complete here?** (bookings, readings,
   invoices, chapters, steps) — that quantity is an element: a vessel that fills, a
   line that balances, a spine that holds a place.
2. **What changes state here?** (a booking confirmed, a reading synced, a vessel
   mended, a chapter finished) — that transition is an element: the change itself,
   animated, carrying the real data.
3. **What journey does the user take here?** (a route, a process, a day, a
   multi-step flow) — that journey is an element: a line, a train, a spine that the
   user travels along.
4. **What is the brand's material?** (paper, ledger, shelf, sonar, kiln — from
   `02-theme-decision.md` §3.3) — that material is the element's body: the element is
   built from it, not decorated with it.

If no question yields an element, the page family gets no signature element — a
deliberate absence recorded with a reason is correct; a generic element invented to
fill a quota is S-3. Worked ideation: a survey app's readings arriving as sonar
pings (the data IS the ping); a book marketplace's shelf filling as listings load
(the shelf IS the count); an accounting app's ledger line balancing on real totals
(the line IS the promise). Each is derived, not selected.

## 3. Per-element full spec format (every element, no exceptions)

```
E-NN — <Name> — <Page family> — <Grid home (e.g. pricing section, right column, 2 cols)>
- What it is and why it belongs: <one paragraph — the content it carries + the material it is built from>
- Structure: <DOM/canvas/SVG approach; viewBox/sizes; what is real DOM (must be) vs decorative>
- ms choreography timeline: <beat by beat from trigger, in ms — see §3.1>
- State matrix: <rest / hover / focus / active / scrolled-past / disabled / touch — each designed, none left "n/a" without a reason>
- How it merges with content: <the delete-test, demonstrated: what information/story leaves if it is removed>
- Failure fallback: <JS-off state; watchdog timing; canvas/WebGL failure; what the user sees if the animation never runs — content fully visible>
- Reduced-motion variant: <the complete static variant — final states, full content, zero loops>
- Performance budget: <frame cost, particle cap, asset weight; what is cut first>
- Mobile variant (<768 px): <specified cheaper version — what is cut/simplified, with numbers>
- Breakpoints: <≥1200 px / 768–1199 px / <768 px — layout, motion intensity, what is cut at each size>
- Edge cases & failure modes: <slow network, no canvas/WebGL, low-power device, content longer/shorter than designed, user scrolling back up, tab hidden mid-animation>
- Accessibility spec: <focus order + visible focus, aria/labelling, contrast at every state, touch target sizes>
- Tokens consumed: <exact CSS variable names>
- Leak check: <the element names/shows no stack internals — state the check result>
```

### 3.1 Choreography timeline rules

- Timeline starts at a named trigger (load gated on `document.fonts.ready` raced
  against 500 ms; scroll entry; user action) and ends at a named final state with a
  hard ceiling (watchdog time, e.g. forced complete by 1200 ms, final by 4000 ms).
- Every beat states its start offset (t=0, t=140, …), its duration, its easing
  (named token), and what moves. Beats that overlap state their overlap explicitly.
- One-way rules where the material demands it (mending, balancing, filling): scrolling
  up never un-does the element; the front position is monotonic (theme #41 law).
- The timeline is seeded/deterministic where randomness is used (seed = element index
  × 7919, theme #41 precedent) so the approved choreography is the shipped one.

## 4. Six worked element concepts (tied to concrete app content)

Each concept follows the §3 format in abbreviated form here; the full spec is written
per element in the project's own Pass 7 record. These are PATTERNS to adapt — do not
copy any of them verbatim into an app whose content they do not fit; an element that
does not fit the app's content fails the merge test even if it is beautifully built.
(The three patterns named in the brief — ledger line, progress spine, mending vessel —
are adapted here into new concrete forms, not copied.)

### E-01 — The Balancing Ledger Rule (accounting SaaS "Northwind Ledger", pricing section)

- **What/why:** a horizontal rule drawn across the pricing table that balances: the
  debit column (plan cost, £18/mo) and the credit column (time saved, 6.5 hrs/mo at the
  user's own logged hours) animate to the plan's real totals, and the rule settles
  level only when the two sides match. It IS the product's promise (books that balance)
  carrying real figures — remove it and the pricing section loses its proof.
- **Structure:** inline SVG, viewBox 0 0 800 120, above the pricing table; two column
  totals as real DOM text (tabular numerals); the rule is a 2.5 px stroke whose
  `stroke-dashoffset` is driven by the shared loop.
- **Timeline:** t=0 section enters → t=0–900 rule draws left→right (`--ease-draw`,
  stepped bursts 5–13%, breaths 50–180 ms) → t=900–1500 debit total counts to £18
  (600 ms, `--ease-out`) → t=1500–2100 credit total counts to 6.5 hrs → t=2100 rule
  settles: rotate 0.8°→0° over 300 ms `--ease-settle`, one 1.5% overshoot, no bounce →
  t=2400 final: rule level, totals still. Watchdog: forced complete 4000 ms.
- **States:** rest — level, totals still. Hover — the rule brightens at the pointer's
  projection (feather-light, 240 ms fade, §5 of `05-motion-system.md`). Focus — the
  pricing CTA's focus triggers the settle replay once. Scrolled-past — level, still.
  Touch — no hover; the settle plays once on entry.
- **Merge:** the totals are the plan's real figures from the app's own pricing data;
  the rule's level IS the balance claim. Delete it and the claim is unverified copy.
- **Fallback:** no JS — rule drawn, totals present as text. Watchdog 4000 ms.
  Reduced motion — rule drawn, totals at final values, no counting.
- **Budget/mobile:** 1 SVG path + 2 text nodes; 0 particles. <768 px — rule 92 vw,
  totals stack below it, draw 700 ms.
- **Edge cases:** plan with no time-saved figure → element does not render (a balance
  with one side missing is a lie; the section falls back to a static rule + totals).
  User scrolls back up — rule stays level (one-way).
- **A11y:** SVG `aria-hidden`; totals are real text; contrast 13.10:1 on the ground.
- **Tokens:** `--accent`, `--text`, `--ease-draw`, `--ease-settle`, `--dur-count 600ms`.
- **Leak check:** totals are user figures (money, hours) — no table, endpoint, or
  record count appears. PASS.

### E-02 — The Reading Spine (exam-prep / guide app, article pages)

- **What/why:** a vertical spine down the article's left margin that fills as the
  reader checks off topics and holds their place between visits (persisted per user,
  per guide). It IS the study plan — remove it and the reader loses their place and
  their progress.
- **Structure:** a 2 px track (full article height) + a fill (transform scaleY, origin
  top) + a marker per topic (12 px dot, done = filled + check 200 ms draw). Progress
  is real: checked topics / total topics, from the user's own stored state.
- **Timeline:** t=0 page load → t=0–400 spine track fades in (200 ms) + fill grows to
  the stored progress over 600 ms `--ease-out` → on topic check: marker fills 200 ms,
  fill extends 240 ms, count text updates ("7 of 12 topics") → on revisit: fill
  restores instantly (no re-animation — repeat visitors are re-scanning).
- **States:** rest — fill at stored progress. Hover — marker tooltip names the topic
  (tap equivalent on touch). Focus — marker is a real checkbox (keyboard operable).
  Scrolled-past — spine persists in the margin (sticky within the article, never
  covering text). Disabled — n/a (a locked topic shows a lock icon + reason, not a
  disabled marker with no explanation).
- **Merge:** the spine's fill IS the user's progress; its markers ARE the topics.
- **Fallback:** no JS — spine present at 0% with all topics listed as text; progress
  text ("0 of 12") still present. Reduced motion — fill jumps to stored progress, no
  growth animation; markers are static checks.
- **Budget/mobile:** transform/opacity only; 0 particles. <768 px — spine moves to a
  top progress line (the margin is too narrow); markers become a compact "7/12" chip.
- **Edge cases:** guide with 1 topic → spine does not render (a spine for one item is
  decoration). Topics added after the user started → fill re-bases to the new total,
  never jumps backwards without explanation (a note: "2 new topics added").
- **A11y:** the spine is a `role="progressbar"` with `aria-valuenow` + text alternative;
  markers are labelled checkboxes; contrast ≥4.5:1 at every state.
- **Tokens:** `--accent`, `--surface-muted`, `--success`, `--text`, `--dur-fill 600ms`.
- **Leak check:** progress is topics completed — never pages, routes, or modules. PASS.

### E-03 — The Mending Seam (repair-studio site, story section)

- **What/why:** the studio's hero vessel arrives broken and mends with gold as the
  visitor scrolls its own history — the crack runs through the section's real timeline
  (founded 2019, dropped 2021, repaired 2023), and each seam segment closes over one
  dated event. The repair service IS the brand story; the seam IS the timeline.
- **Structure:** inline SVG vessel (viewBox 0 0 640 480) in 3 shard groups + 2 seam
  paths + 15 fissures (theme #41 pattern, re-derived for this studio's vessel and
  dates — not copied: the fracture plan follows THIS vessel's stress points).
- **Timeline:** t=0 section enters → shards converge 640 ms `--ease-lock`, stagger
  140 ms → seam 1 draws in stepped bursts (≈900 ms) over the 2019–2021 events →
  seam 2 draws (≈900 ms) over 2021–2023 → settle dip 550 ms → runners arm (light
  travels seams at 90 px/s, ≤2 lit). Watchdog: force-healed 6000–7000 ms after entry.
- **States:** broken (JS-armed only) → mending → mended → lit (pointer glow at the
  seam, 46 px proximity, 240 ms fade-in). Scrolled-past — mended, runners running.
  Touch — sheen plays once 600 ms after the mend.
- **Merge:** every seam carries a mend note (`data-mend="dropped, March 2021 — studio
  shelf"`) naming a real break; the footer prints the mend record from those notes.
  A seam without a note fails the gate.
- **Fallback:** no JS — vessel whole, seams gold, notes present as text. Reduced motion —
  vessel arrives mended. **Budget/mobile:** 3 shard groups + 2 seams + 15 fissures;
  ≤9 KB inline; <768 px — offsets halve, stagger 100 ms, dip cut, dust puff cut.
- **Edge cases:** visitor scrolls during the mend — the mend is time-based and completes
  off-screen; return visit — `sessionStorage` marks the vessel mended (gold is never
  taken back). **A11y:** SVG `role="img"` + `aria-label` carrying the mend note; the
  story is text, not the animation.
- **Tokens:** `--gold`, `--crack`, `--paper`, `--charcoal`, `--ease-lock`, `--ease-draw`.
- **Leak check:** mend notes name real-world events (dates, places) — no stack terms. PASS.

### E-04 — The Route Sweep (field-survey SaaS "Fieldnote", day-map section)

- **What/why:** the surveyor's day route draws itself as a sweep line across the map
  as the visitor scrolls — each waypoint is a real reading the surveyor took (time,
  location, value), and the sweep IS the day's work. Remove it and the map is a static
  picture with no story.
- **Structure:** SVG map (the survey area, real geography) + one route path + waypoint
  dots (real readings) + a sweep head (12 px ring). Path length measured at build-in
  (`getTotalLength()`), never estimated.
- **Timeline:** t=0 section enters → t=0–1200 route draws (`--ease-draw`, scrub-linked
  to scroll progress through the section — the visitor's descent IS the surveyor's
  day) → each waypoint lights as the front passes it (dot fills 200 ms + value label
  fades 200 ms) → t=1200 sweep head rests at the final waypoint, pulsing once (600 ms,
  then still — a pulse that never stops is a defect). Scrubbed: scrolling back up
  freezes the front at its highest reached value (one-way, like a day already walked).
- **States:** rest — route drawn, waypoints lit. Hover — waypoint tooltip shows the
  reading (tap equivalent). Focus — waypoints are buttons (keyboard reachable).
  Scrolled-past — route drawn, still.
- **Merge:** the route is the user's real data (their readings, their day). A route
  drawn from demo data fails the gate.
- **Fallback:** no JS — route drawn, waypoints + values as a list below the map.
  Reduced motion — route drawn, no sweep, waypoints lit. **Budget/mobile:** 1 path +
  ≤12 dots; <768 px — map full-width, route draws 800 ms, waypoint labels become a
  list (no hover tooltips on touch).
- **Edge cases:** day with 0 readings → element does not render (an empty map with a
  route is a lie). Readings with no location → listed as text, not plotted.
- **A11y:** map `role="img"` + text alternative (the readings list); waypoint buttons
  labelled with time + value; contrast ≥4.5:1.
- **Tokens:** `--accent` (signal), `--surface`, `--text`, `--ease-draw`.
- **Leak check:** waypoints are readings (time, place, value) — never endpoints or
  tables. PASS.

### E-05 — The Shelf That Fills (used-book marketplace "Harbour Books", catalogue)

- **What/why:** the catalogue's shelf fills as listings load — each book that arrives
  takes its place on the shelf (spine widths vary by the book's real page count), and
  the shelf's fullness IS the listing count. An empty shelf is the empty state; a full
  shelf is the catalogue.
- **Structure:** DOM shelves (rows) + book spines as DOM elements (width = f(page
  count), 8–28 px; colour from the book's cover palette, sampled — never random);
  the shelf edge is a 4 px rule. Books are real links (title, author, price in text).
- **Timeline:** t=0 listings load → books slide onto the shelf left→right, stagger
  40 ms capped at 8 (≤320 ms + 420 ms slide) → shelf edge draws under each row as it
  fills (200 ms) → count line updates ("1,204 books on your shelf", counts once
  600 ms). Repeat visits: books present, no re-animation.
- **States:** rest — shelf full, books still. Hover — book slides out 4 px + lifts
  2 px, 160 ms (its title shows). Focus — ring on the book link. Active — press
  120 ms. Touch — tap = the book's detail (no hover state needed).
- **Merge:** spine width encodes page count; the shelf's fullness encodes the catalogue
  size; the empty shelf IS the empty state (L-C4: "No books yet — list your first").
- **Fallback:** no JS — books listed as a plain list (the shelf is enhancement; the
  catalogue is DOM). Reduced motion — books present, no slide.
  **Budget/mobile:** transform/opacity only; <768 px — one column of book rows (spines
  become cards), stagger 24 ms.
- **Edge cases:** book with no page count → default spine 16 px (recorded, not hidden).
  10,000 listings → shelf shows the first page's books only; the count line carries
  the total (never render 10,000 spines).
- **A11y:** books are a real list of links; spine width is decorative (page count is
  also text); contrast ≥4.5:1.
- **Tokens:** `--paper`, `--ink`, `--accent`, `--ease-shelf`.
- **Leak check:** the count is books — never rows, records, or tables. PASS.

### E-06 — The Usage Meter as a Vessel (SaaS settings/billing, usage section)

- **What/why:** the plan's usage is a vessel that fills — storage used (7.2 GB of
  10 GB) is water in a jar; the jar's fill level IS the usage, and the line where the
  water will reach at the current rate (projected 9.1 GB by 1 Dec) is a second, fainter
  line. The user reads their usage at a glance; the meter IS the billing fact.
- **Structure:** SVG jar (viewBox 0 0 200 260) + fill rect (transform scaleY, origin
  bottom) + projected line (dashed, `--text-muted`) + real text below ("7.2 GB of
  10 GB used · 2.8 GB left").
- **Timeline:** t=0 section enters → t=0–800 fill rises to 72% (800 ms `--ease-out`,
  transform-only) → t=800–1100 projected line draws (300 ms) → t=1100 count text
  settles ("7.2 GB"). Watchdog: final values by 2000 ms.
- **States:** rest — fill at real usage. Hover — tooltip names the largest user
  (by user concept: "Photos — 4.1 GB"). Focus — the meter is a `role="meter"` with
  `aria-valuenow`; the breakdown is a list below. Scrolled-past — still.
  Near-limit (≥90%): the fill's top 10% is `--error` tint + text "Almost full — 2.8 GB
  left" (never colour alone).
- **Merge:** the fill level IS the usage number; remove it and the section is a bare
  number with no sense of scale.
- **Fallback:** no JS — fill at 72% (server-rendered inline style), text present.
  Reduced motion — fill at final level, no rise.
  **Budget/mobile:** 1 SVG + 1 transform; <768 px — jar 160 px wide, text below.
- **Edge cases:** usage 0% → jar empty with text "Nothing stored yet"; usage 100% →
  jar full + error tint + the upgrade action (never a bare "limit reached" with no path).
  Projected line beyond 100% → clamped at the rim + text "You'll run out on ~24 Nov".
- **A11y:** `role="meter" aria-valuemin/max/now` + text alternative; contrast ≥4.5:1.
- **Tokens:** `--accent`, `--surface-muted`, `--error`, `--text`, `--dur-fill 800ms`.
- **Leak check:** usage is in user units (GB) — never a DB name, table, or service.
  The old label "PostgreSQL 15 · 7.2 GB" is exactly the leak this element replaces
  (`09-architecture-leak.md` pair L-7). PASS.

## 5. The cursor rule (restated here because Pass 7 is where it is re-broken)

System cursor only (motion FE-093, `05-motion-system.md` §5). Pass 7 is the pass where
a builder is most tempted to add a "delightful" cursor to match a new element — that
temptation is a defect. A heavy cursor is removed in Pass 5 and must not return in
Pass 7; the Pass 7 checklist includes a `cursor: none` grep = 0 and the
pointer-overshoot test (5 fast moves, 0 misses). Feather-light effects live ON the
elements (a seam glowing at the pointer's projection, a book sliding out 4 px) — the
cursor itself stays the system's.

## 6. 3D where possible, otherwise excellently animated

- 3D is used where the element's material genuinely has depth (a vessel, a jar, a
  book's spine) and the performance budget holds on a mid-range phone (`05` §7).
  WebGL/3D is a recorded exception to the one-loop rule (§1.1 of `05`) with its own
  frame budget — and it degrades to the excellently-animated 2D version (SVG/canvas)
  when WebGL is unavailable, on low-power devices, or under reduced motion. The 2D
  fallback is the same element, not a placeholder: it carries the same content.
- Where 3D would fake the product (a photographable object rendered instead of
  photographed — design-intelligence §7 Example B, the clay world that would fake the
  pots), 2D excellently animated is the correct choice, and the decision is recorded.
- "Excellently animated" means: the §3 spec is complete (choreography, states,
  fallback, budget, mobile) and the element passes the merge test — not that it has
  more keyframes.

## 7. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 merge test | `01-audit-and-scoring.md` §5 Cat. 2 scoring; `03` Pass 7 checklist |
| §2 ideation | `02-theme-decision.md` §3.3/§4.2 (deriving motion from material) |
| §3 spec format | The Pass 7 record format — every element in the project follows it |
| §4 worked concepts | Patterns for `08-case-studies.md` (each study's 5–20 elements) |
| §5 cursor | Standing rule — also `05` §5, `03` Pass 5/7 checklists |
