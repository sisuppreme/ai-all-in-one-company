# UI/UX Upscaler — Spec 08: Case Studies

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Three worked
> before/after case studies, each complete end-to-end. All three apps are FICTIONAL
> (named products, real data, real flows — never lorem ipsum). Their BEFORE scores are
> the scores the audit method in `01-audit-and-scoring.md` §5 produces on the described
> defects; their AFTER scores are the scores the same method produces after the
> described passes. Arithmetic is shown in full in each study — see §4 for the
> consistency rule.
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> Each study includes a leak audit (leaks BEFORE → AFTER, target zero, one worked leak
> fix) per the expanded orders — see §1.5 and each study's §(x).6.

## 1. How to read a case study (common structure)

Each study follows the same sections, in order:

1. **The app** — named product, real content/data/flows (fictional but concrete).
2. **Audit excerpt** — top defects found (ID, location, symptom, severity, pass).
3. **Theme decision** — with reasoning + the rejected alternative and why.
4. **Pass-by-pass decisions** — what each of the 7 passes did (and did not do).
5. **Signature elements** — the 5–20 chosen, how each merges with content.
6. **Leak audit** — leaks found in BEFORE, leak count BEFORE → AFTER (target zero),
   one worked leak fix in full (leaking UI → clean UI → verification).
7. **Motion dial per page** — dial per page family, with reasons.
8. **BEFORE → AFTER scores per gate category** — 8 rows + total, arithmetic shown.
9. **Deliberately left unchanged** — what stayed, and why (a reason each, or the gate fails).
10. **Rollback / regression evidence** — what was tested, what the evidence is.

### 1.1 Score consistency rule (binding on this file)

- Every study's BEFORE total = the sum of its 8 BEFORE category scores, shown as an
  addition (e.g. `4+3+6+3+5+4+0+3 = 28/80`). Every AFTER total likewise.
- The headline BEFORE/AFTER in the study title must match the table's totals exactly.
- Each category's movement must be traceable to a pass in §(x).4: a category that moves
  +4 must have the pass work that caused it named. A category that does not move must
  say why (usually: it was already at threshold, or its lever pass is recorded as
  out-of-scope with a reason — which then appears in §(x).9).
- The app-level score is the LOWEST family score (`01` §5.3), not the average — each
  study names its lowest-scoring family and scores from it.

### 1.2 What "real content, never lorem ipsum" means here

Every number, name, date, and flow in these studies is concrete and checkable inside
the fiction: "Northwind Ledger" has a £18/mo plan and a real pricing table; "Harbour
Books" has 1,204 books and a real catalogue; "Fieldnote" has 42 readings from a real
survey day. Counters animate only these numbers. If a study needs a number it does
not have, the number is removed — never invented (S-9).

## 2. Case study (a) — Internal analytics dashboard: "Northwind Ledger"

### 2.1 The app

Northwind Ledger is a B2B accounting SaaS (fictional). The dashboard is its home:
CFOs and finance leads checking the month. Real content: 1,204 invoices this month
(£84,210 billed, £71,430 collected, 214 overdue totalling £9,860); top customers
(Acme Ltd £12,400; Briar & Co £8,910; Calder Group £7,205); the overdue list (14
invoices, oldest 42 days, "Harlow Designs — £1,240 — 42 days overdue"); the cash-flow
chart (12 weeks of real weekly totals, £6,100–£9,800/week). Flows: filter by month/
customer/status; drill into an invoice; export the month as a spreadsheet; mark an
invoice paid. Routes: `/app` (dashboard), `/app/invoices`, `/app/customers`,
`/app/reports`, `/app/settings`.

### 2.2 Audit excerpt (top defects — 41 total in the full audit)

| ID | Location | Symptom | Severity | Pass |
|---|---|---|---|---|
| A-01 | `src/pages/Dashboard.tsx:8` | S-1/S-2: dashboard is 4 identical stat cards (indigo gradient headers, Inter 400) + a chart with no title | BLOCK | 2, 3, 7 |
| A-07 | `src/components/DataTable.tsx:61` | S-5: invoice rows render `opacity: 0` in CSS; fast scroll strands 37 of 200 rows until reload | BLOCK | 4, 6 |
| A-12 | `src/components/StatCard.tsx:22` | S-9: "12,482 users" hard-coded in a card — no source; the real figure is 1,204 invoices | BLOCK | 4, 7 |
| A-19 | `src/App.tsx:44` | S-8: heavy custom cursor, 64 px follower, ~200 ms lag, overshoots nav on 3/5 attempts | BLOCK | 5 (remove) |
| A-23 | `src/pages/Settings.tsx:31` | Leak: "Connected database: PostgreSQL 15" + "12 pages · 4 modules" (see §2.6) | BLOCK | 2, 4 |
| A-27 | `src/components/Chart.tsx:40` | S-13: chart tooltips hover-only; touch users get no values | WARN | 4 |
| A-31 | `src/index.css` | S-17: no `prefers-reduced-motion` handling anywhere; 214 hard-coded hex values | BLOCK | 1, 5 |

### 2.3 Theme decision

- **Inputs:** institutional personality; CFOs/finance leads, burned by flashy fintech
  before; content type tool + reference; identity I-6 = 3 (indigo gradient + starter
  bento, copy swappable with any SaaS).
- **Branch B — adopt.** Family: archive/ledger/instrument (§1.2 row 1). Shortlist:
  #3 Redacted Archive (2 — the ledger's world IS the archive: figures, stamps,
  ruled lines), a calibre/instrument theme (1 — fits the chart, fights the ledger),
  #63 Sonar Room (0 — sonar is signal, not money; needs explaining). Winner: **#3
  Redacted Archive**, canonical spec `skills/frontend/theme-library/expanded/theme-003.md`
  read in full. Mapping: archive palette (paper ground, ink text, one redaction-red
  accent, mono for data); grotesque body + mono for figures (tabular numerals);
  motion: draw-and-balance (the ledger line, §2.5 E-L1); layout: bento + editorial
  hybrid, proof (the overdue list) moved to section 2.
- **Rejected alternative:** deepening the existing identity. Reason: I-6 = 3 — there is
  nothing to deepen; tokenising the indigo gradient would produce a polished starter
  (S-10). Also rejected: a dark cinematic theme at dial 4 — spectacle reads as risk
  to a CFO (FE-322).
- **Leak check:** the archive theme is applied to user figures only (invoices, pounds,
  days overdue) — never to tables or endpoints (§2.6).

### 2.4 Pass-by-pass decisions

- **P1 Tokens:** 214 hard-coded hex → 14 tokens (`--paper`, `--ink`, `--accent-red`,
  `--mono`, …); greps 0. The indigo gradient is deleted (it was not a token — it was
  the starter showing).
- **P2 Typography:** scale ratio 1.25, body 16 px; mono tabular for all figures;
  contrast fixed (the chart's grey labels were 3.1:1 → 4.6:1). Copy: the "12,482 users"
  card is deleted (S-9 — no source); replaced by the real "1,204 invoices" card.
- **P3 Layout:** bento grid (stat cards 4-across ≥1200 px, 2-across 768–1199, 1-across
  <768); overdue list moved to section 2; footer designed as a section. No overflow
  at 320–1920 px.
- **P4 Components:** tables (sticky header, sort indicators, skeleton rows, honest
  counts "Showing 1–25 of 200 invoices"); stat cards (live data, deltas as text);
  filters (active chips, empty state "No invoices for March — [Clear filter]");
  chart tooltips on hover + tap + focus.
- **P5 Motion:** cursor REMOVED (system cursor); reveals once per session (dashboards
  are re-scanned daily); counters once (600 ms, real totals); one shared lerped loop
  replaces 3 scroll handlers; reduced-motion variants in the same pass.
- **P6 Scroll:** no pinning inside the tool; scroll signature is the ledger line
  (§2.5 E-L1) + the data ticking (live values update with a 200 ms fade).
- **P7 Polish:** 6 signature elements (§2.5), each merged; S-19 sweep 0 overlaps.

### 2.5 Signature elements (6)

- **E-L1 The Balancing Ledger Rule** — the pricing/ledger line that balances on real
  totals (£84,210 billed vs £71,430 collected + £9,860 overdue + £2,920 in transit =
  balanced; the rule settles level only when the arithmetic holds). Pattern: `06` E-01.
- **E-L2 The Overdue Stamp** — each overdue invoice carries a stamp ("42 DAYS") that
  presses in 200 ms as the list enters; the stamp IS the overdue fact, not decoration.
- **E-L3 The Cash-Flow Draw** — the 12-week chart line draws (800 ms) on first view;
  the line IS the quarter's story; repeat visits show it drawn.
- **E-L4 The Collection Gauge** — "£71,430 of £84,210 collected" as a filling rule
  (85%); the fill IS the collection rate.
- **E-L5 The Filter Chips' Count** — active filter chips carry their result counts
  ("March · 214 invoices"); removing a chip re-counts in 160 ms.
- **E-L6 The Month Spine** — a spine down the reports page marking the 12 months;
  the current month is the filled marker; it IS the year's progress.

### 2.6 Leak audit

| Leak (BEFORE) | Surface | Count |
|---|---|---|
| "Connected database: PostgreSQL 15" | `/app/settings` | 1 |
| "12 pages · 4 modules" | Sidebar footer | 1 |
| "1,204 rows in `bookings`" (stat card subtitle) | `/app` stat card | 1 |
| "Fetching /v2/invoices…" | Loading text, invoices table | 1 |
| "422: `invoices.customer_id` FK violation" | Mark-paid error toast | 1 |
| "No records found in `invoices`" | Empty filtered list | 1 |
| **Leak score BEFORE: 6 → AFTER: 0 (target zero). Gate veto: cleared.** | | |
- **Worked leak fix (A-23 / pair L-1 + L-4):** BEFORE — settings showed
  "Connected database: PostgreSQL 15" and the sidebar footer showed "12 pages ·
  4 modules". Fix — both removed: settings now reads "Your data is stored securely.
  Backed up daily." (the fact the user cares about is the backup, not the engine);
  the sidebar footer is deleted (the count served no user need). Verification — copy
  scan re-run (ban-list grep over all user-facing strings = 0 hits); non-technical-user
  test: the settings page now reads without any question needing stack knowledge.
  (`09-architecture-leak.md` pairs L-1, L-4.)

### 2.7 Motion dial per page

| Page family | Dial | Reason |
|---|---|---|
| Dashboard `/app` | 2 (Quiet) | Repeat-visit tool; reveals once per session; counters once |
| Invoices `/app/invoices` | 2 | Same — a table is read, not watched |
| Reports `/app/reports` | 2 | Reference content; the month spine is the only scroll signature |
| Settings `/app/settings` | 1 (Still) | Task flow; clarity over choreography |

### 2.8 BEFORE → AFTER scores (lowest family: dashboard)

| Category | BEFORE | AFTER | Movement caused by |
|---|---|---|---|
| 1. Hierarchy & focal order | 4 | 8 | P3 bento + proof moved up; P2 type hierarchy |
| 2. Element integration | 3 | 8 | P7 six merged elements (delete-test demonstrated) |
| 3. Readability & contrast | 6 | 9 | P2 contrast fixes (3.1:1 → 4.6:1 chart labels) |
| 4. Motion smoothness | 3 | 8 | P5 one loop, cursor removed, lerp 0.12 |
| 5. Performance | 5 | 8 | P5 loop merge; P1 token dedup; profile: longest scroll task 180 ms → 42 ms |
| 6. Never-invisible safety | 4 | 10 | P4/P6: JS-gated reveals removed; observer-stub test strands 0/200 rows (was 37) |
| 7. Reduced motion | 0 | 10 | P5 reduce variants in the same pass; emulation pass 0 continuing motion |
| 8. Aliveness | 3 | 9 | P6/P7: ledger line, stamps, gauge — no dead stretch; stillness deliberate in tables |
| **TOTAL** | **4+3+6+3+5+4+0+3 = 28/80** | **8+8+9+8+8+10+10+9 = 70/80** | **BEFORE 28/80 → AFTER 70/80 (target ≥70)** |

### 2.9 Deliberately left unchanged

- The invoice data model and the mark-paid flow (behaviour freeze — Protocol Step 2;
  the flow works; the upgrade is presentation-layer first).
- The export format (spreadsheet .csv) — the format the user opens is named; the
  mechanism is not (`09` §7).
- The chart library (replaced only its styling/tokens, not the library — a library
  swap is out of scope for a UI upgrade and would risk the data).

### 2.10 Rollback / regression evidence

- Branch `upscale/northwind-ledger`; flags `upscale.dashboard`, `upscale.motion.dashboard`.
- Baseline freeze (`10` §1): 5 routes, 4 primary flows (filter, drill-in, export,
  mark-paid), screenshot pairs 1440/390, scroll profile (longest task 180 ms).
- Regression checklist after every pass (`10` §2): all 4 flows green; console 0 errors;
  API calls unchanged in count and shape (verified by request log diff); performance
  profile after Pass 7: longest scroll task 42 ms, 0 frames >50 ms.
- No rollback was needed. The Pass 5 inverse (restore the 3 scroll handlers + the
  cursor) was recorded before Pass 5 started and never used (`10` §4).

## 3. Case study (b) — E-commerce storefront: "Harbour Books"

### 3.1 The app

Harbour Books is a used-book marketplace (fictional). Real content: 1,204 books
("The Midnight Gazette — £14 · Very good · 312 pages · Seller: Mara's Shelf, Bristol";
"Pocket Pal's Guide to Mending — £9 · Good · 188 pages"); categories (Fiction 412,
History 268, Children's 301, Poetry 223); sellers (86 sellers, top seller Mara's Shelf
with 214 books); the basket (2 books, £23 total); checkout (address → payment → confirm).
Flows: browse → filter by category/condition → book detail → add to basket → checkout
→ confirmation. Routes: `/` (home), `/browse`, `/book/:id`, `/basket`, `/checkout`,
`/sell`.

### 3.2 Audit excerpt (top defects — 38 total)

| ID | Location | Symptom | Severity | Pass |
|---|---|---|---|---|
| B-01 | `src/pages/Home.tsx:6` | S-1: generic centred hero (indigo gradient, Inter 400, "Shop books"), copy swappable with any shop | BLOCK | 2, 5, 7 |
| B-05 | `src/components/BookCard.tsx:18` | S-2: all cards identical; spine width/condition carry no information | WARN | 4, 7 |
| B-09 | `src/pages/Checkout.tsx:44` | S-12: marquee + counters + tilt on the checkout page (dial violation — spectacle where the user came to finish) | BLOCK | 5 |
| B-14 | `src/pages/Browse.tsx:30` | S-5: infinite scroll strands items (observer fires once; 23 of 120 books blank on fast scroll) | BLOCK | 4, 6 |
| B-18 | `src/pages/Checkout.tsx:71` | Leak: "Error: Cannot read properties of undefined (reading 'customer_id')" on a failed payment | BLOCK | 4 |
| B-22 | `src/index.css` | S-17: no reduced-motion handling; 187 hard-coded hex values | BLOCK | 1, 5 |
| B-26 | `src/components/Footer.tsx` | S-15: footer is unstyled default (different type, no theme language) | WARN | 3, 7 |

### 3.3 Theme decision

- **Inputs:** craft personality; buyers browsing second-hand books, sellers listing
  from home; content type catalogue + story; audience returns weekly, 62% mid-range
  Android. Identity I-6 = 8 (warm paper palette #F5EFE0, ink #2B2118, lacquer-red
  #9A3B26, Fraunces display + humanist body, copy in a distinct voice: "Every book
  has had a life before yours"). Logo-removal test passes; copy-swap test passes.
- **Branch A — deepen.** Tokens extracted from the live app (8 colours → 6 tokens; 2
  near-duplicate browns merged). Type scale fitted at ratio 1.333, body 17 px. Motion
  derived from the material: books are shelved, thumbed, passed on — *shelving* motion
  (cards slide onto the shelf, 420 ms `--ease-shelf`); scroll signature: a shelf that
  fills as the catalogue loads (the shelf IS the listing count).
- **Rejected alternative:** adopting theme #41 Kintsugi. Reason: the metaphor is close
  (mended things) but wrong — Harbour's story is continuity and passing-on, not
  breakage and repair; gold seams would imply the books are damaged. The brand's own
  material (shelves, stamps, marginalia) already supplies a motion language, so
  adoption would replace a working identity with a borrowed one.
  (Full worked reasoning: `02-theme-decision.md` §6.1 — this study reuses Example D1
  as its decision record; it is not re-argued here.)
- **Leak check:** the deepened identity names no internals; the shelf, the stamp, and
  the count line all use user concepts (§3.6).

### 3.4 Pass-by-pass decisions

- **P1 Tokens:** 187 hard-coded hex → 11 tokens (`--paper`, `--ink`, `--lacquer`, …); greps 0.
- **P2 Typography:** scale 1.333, body 17 px; line length 45–75 ch on story pages;
  the hero copy rewritten ("Every book has had a life before yours" — the brand's own
  voice, now as the hero line instead of "Shop books").
- **P3 Layout:** catalogue grid (4 cols ≥1200 px, 2 cols 768–1199, 1 col <768);
  pacing: dense catalogue / quiet story sections alternating; footer designed as a section.
- **P4 Components:** book cards (spine width encodes page count — see §3.5 E-H1);
  filters with honest empty states; basket (line items with real titles/prices);
  checkout forms (labels above fields, inline validation in user terms).
- **P5 Motion:** checkout stripped of marquee/counters/tilt (dial 1 — the user came to
  finish); catalogue reveals 40 ms stagger capped at 8; one shared loop; reduced-motion
  variants same pass.
- **P6 Scroll:** shelf-fills scroll signature on the catalogue; no pinning on the
  checkout; browse reveals once per session.
- **P7 Polish:** 7 signature elements (§3.5).

### 3.5 Signature elements (7)

- **E-H1 The Shelf That Fills** — the catalogue shelf (pattern `06` E-05): spine width
  = page count; shelf fullness = 1,204 books; empty shelf = the empty state.
- **E-H2 The Passed-On Stamp** — each book's condition ("Very good") is a library
  stamp that presses in 200 ms; the stamp IS the condition grade.
- **E-H3 The Marginalia Line** — on a book's detail page, a previous owner's marginalia
  (one real quoted line, with permission) is revealed line by line as the reader
  scrolls the description — the book's history, told in its own words.
- **E-H4 The Basket String** — the basket total (£23) is tied with a string that
  tightens as books are added (2 books → the string draws taut in 240 ms); the string
  IS the basket's fullness.
- **E-H5 The Seller's Shelf** — a seller's page shows their shelf (Mara's Shelf: 214
  books, spines in her palette); the shelf IS the seller.
- **E-H6 The Checkout Thread** — the checkout steps are a thread through 3 beads
  (address → payment → confirm); the thread fills honestly as steps complete, never
  jumping. (Dial 1: the thread fills, nothing else moves on the checkout.)
- **E-H7 The Footer Press** — the footer is a printing press: the colophon ("Set in
  Fraunces · Printed on paper") is pressed in 400 ms as the footer enters; the footer
  IS the last impression, in-theme.

### 3.6 Leak audit

| Leak (BEFORE) | Surface | Count |
|---|---|---|
| "Error: Cannot read properties of undefined (reading 'customer_id')" | Failed-payment error | 1 |
| "No records found in `orders`" | Empty orders list | 1 |
| "0 results — query: SELECT * FROM books WHERE title LIKE '%x%'" | Search empty state | 1 |
| "Fetching /v2/books…" | Browse loading text | 1 |
| "12 pages · 3 modules" | Footer (old) | 1 |
| **Leak score BEFORE: 5 → AFTER: 0 (target zero). Gate veto: cleared.** | | |
- **Worked leak fix (B-18 / pair L-8):** BEFORE — a failed payment showed "Error:
  Cannot read properties of undefined (reading 'customer_id')" with no next step; the
  user lost their basket state and did not know whether they had been charged. Fix —
  the error state now reads "We couldn't take your payment. You haven't been charged.
  Check your card details and try again. [Retry payment]" and the basket is preserved
  (the form error never clears the form, `04` §17); the technical detail goes to the
  log with reference code HB-4417, shown as "Reference HB-4417 — quote it if you
  contact us". Verification — error-path walkthrough re-run (payment failure stubbed):
  0 leaking strings; the retry succeeds on the second attempt in the test; the basket
  still holds 2 books (£23) after the error. (`09-architecture-leak.md` pair L-8.)

### 3.7 Motion dial per page

| Page family | Dial | Reason |
|---|---|---|
| Home `/` | 3 (Alive) | Marketing + story; shelf fills, stamp presses |
| Browse `/browse` | 3 | Catalogue; reveals once per session; shelf signature |
| Book detail `/book/:id` | 3 | Story (marginalia) + catalogue |
| Basket `/basket` | 2 (Quiet) | Task-adjacent; the string tightens, nothing else |
| Checkout `/checkout` | 1 (Still) | The user came to finish; thread fills, nothing else moves |
| Sell `/sell` | 2 | Form flow with a story header |

### 3.8 BEFORE → AFTER scores (lowest family: checkout)

| Category | BEFORE | AFTER | Movement caused by |
|---|---|---|---|
| 1. Hierarchy & focal order | 5 | 9 | P2 hero rewrite + P3 grid/pacing; 3-second test passes |
| 2. Element integration | 4 | 9 | P7 seven merged elements (shelf, stamp, thread) |
| 3. Readability & contrast | 6 | 9 | P2 contrast fixes; P4 form labels above fields |
| 4. Motion smoothness | 4 | 9 | P5 one loop; checkout stripped of dial violations |
| 5. Performance | 5 | 8 | P5 loop merge; profile: longest scroll task 160 ms → 38 ms |
| 6. Never-invisible safety | 5 | 10 | P4/P6: observer-stub test strands 0/120 books (was 23) |
| 7. Reduced motion | 0 | 10 | P5 reduce variants same pass; emulation 0 continuing motion |
| 8. Aliveness | 4 | 9 | P6/P7: shelf fills, marginalia, press — no dead stretch |
| **TOTAL** | **5+4+6+4+5+5+0+4 = 33/80** | **9+9+9+9+8+10+10+9 = 73/80** | **BEFORE 33/80 → AFTER 73/80 (target ≥72)** |

Note: the headline BEFORE (33/80) differs from the task brief's "~41/80" — the brief's
figure was an estimate; the audit method (`01` §5) on the described defects produces
33/80, and the table shows its arithmetic. The AFTER target (≥72) is met at 73/80.
(See §4 for the consistency rule: the table's arithmetic governs, not the estimate.)

### 3.9 Deliberately left unchanged

- The checkout flow order and the payment provider (behaviour freeze; the provider is
  named only on the payment step as a trust fact, `09` §7 — never as a stack label).
- Book data and seller data (real content; the upgrade never invents a book, a price,
  or a review).
- The "Very good / Good" condition grades (the sellers' own grading scale — the
  upgrade presents it, it does not redefine it).

### 3.10 Rollback / regression evidence

- Branch `upscale/harbour-books`; flags `upscale.browse`, `upscale.checkout`,
  `upscale.motion.browse`.
- Baseline freeze (`10` §1): 6 routes, 3 primary flows (browse→detail, add to basket,
  checkout→confirmation), screenshot pairs 1440/390, scroll profile (longest task 160 ms).
- Regression checklist after every pass (`10` §2): all 3 flows green; basket total
  arithmetic verified (£23 = £14 + £9) after every pass; console 0 errors; API calls
  unchanged in count/shape.
- Rollback used once: Pass 5's first attempt kept a marquee on the checkout (dial
  violation found by the dial audit); the pass was rolled back to its tag, the marquee
  removed, and Pass 5 re-attempted — the break is recorded in the audit file §8 with
  the re-plan (`10` §4: never patch forward).

## 4. Case study (c) — SaaS settings / billing area: "Fieldnote"

### 4.1 The app

Fieldnote is a field-survey SaaS (fictional). The settings/billing area is its most
leak-prone surface (see §4.6). Real content: the "Survey Team" plan — £18/month, next
charge 1 Dec 2026, 3 seats (Anya, Bilal, Chen); usage — 7.2 GB of 10 GB storage, 42
readings waiting to sync, 1,180 readings this month; team members (Anya — admin,
Bilal — surveyor, Chen — surveyor); notification preferences (sync alerts on, weekly
summary on, marketing off); the readings list (42 queued, oldest 3 days, from the
Kaghan survey). Flows: change plan → confirm → updated; invite a member; toggle a
notification; view usage; update payment card. Routes: `/app/settings`,
`/app/settings/billing`, `/app/settings/team`, `/app/settings/notifications`.

### 4.2 Audit excerpt (top defects — 29 total)

| ID | Location | Symptom | Severity | Pass |
|---|---|---|---|---|
| C-01 | `src/pages/Settings.tsx:12` | S-2: settings as a wall of 14 undifferentiated toggles, no grouping by user job | BLOCK | 3, 4 |
| C-04 | `src/pages/Billing.tsx:20` | S-9 + leak: "PostgreSQL 15 · 7.2 GB" as the storage line; usage has no user unit context | BLOCK | 2, 4, 7 |
| C-07 | `src/pages/Billing.tsx:44` | Leak: "API endpoint: /v2/readings · table: field_readings" on the sync panel | BLOCK | 4 |
| C-11 | `src/components/Toggle.tsx:9` | Missing states: toggles show state by colour alone (no On/Off text); no focus ring | BLOCK | 4 |
| C-15 | `src/pages/Team.tsx:31` | S-6: team page is a dead list (no states, no empty state for 0 pending invites) | WARN | 4, 7 |
| C-19 | `src/index.css` | S-17: no reduced-motion handling; 96 hard-coded hex values | BLOCK | 1, 5 |
| C-22 | `src/pages/Settings.tsx:58` | S-13: notification toggles hover-only tooltips explaining what each toggle does | WARN | 4 |

### 4.3 Theme decision

- **Inputs:** precise/technical personality; environmental surveyors on mid-range
  Android in sunlight, gloves on, one hand free; content type tool + reference;
  identity I-6 = 2 (default Inter, indigo gradient, starter settings wall).
- **Branch B — adopt.** Family: instrument/signal (§1.2 row 5). Shortlist: #63 Sonar
  Room (2 — the surveyor's world IS a signal room: readings arrive as pings), #76 Ice
  Core Archive (1 — depth fits, but ice is not the surveyor's material), #3 Redacted
  Archive (1 — fits reports, fights the field side). Winner: **#63 Sonar Room**,
  canonical spec `skills/frontend/theme-library/expanded/theme-063.md` read in full.
  Mapping: sonar palette (dark lab ground, one signal green); mono-forward type, tabular
  numerals everywhere (readings compared in sun); motion: readings arrive as sonar
  pings (240 ms ring); layout: instrument rail + content column; settings grouped by
  user job (Profile, Notifications, Billing, Privacy).
- **Rejected alternative:** deepening the existing identity. Reason: I-6 = 2 — nothing
  to deepen; tokenising the settings wall would polish a wall (S-10). Also rejected:
  #76 Ice Core Archive — the depth metaphor needs explaining to a surveyor whose job
  is lateral coverage, not depth (§1.4 test fails).
  (Full worked reasoning: `02-theme-decision.md` §6.2 — this study reuses Example D2
  as its decision record.)
- **Leak check:** the sonar theme is applied to user-visible readings only; the sync
  panel's old endpoint/table line is rewritten (§4.6).

### 4.4 Pass-by-pass decisions

- **P1 Tokens:** 96 hard-coded hex → 12 tokens (sonar ground, signal green, ink, …); greps 0.
- **P2 Typography:** mono-forward; tabular numerals; contrast fixed for sunlight
  (outdoor legibility: body contrast raised to ≥7:1 where the theme allows — surveyors
  read in sun, and AA is a floor, not a target, on this surface).
- **P3 Layout:** instrument rail (72 px icon rail, 768–1199 px) + content column;
  settings grouped by job into 4 sections with plain-language headings; no overflow
  at 320–1920 px.
- **P4 Components:** toggles (48×28 px, On/Off text + `role="switch"`, focus ring,
  200 ms state change); plan card ("Current plan" text + accent border); usage meter
  (§4.5 E-F3); invite flow (labels in user terms); notification toggles with visible
  explanations (not hover-only tooltips).
- **P5 Motion:** dial 1 on all settings pages (task flow); pings only where a reading
  arrives (240 ms ring, transform-only); reduced-motion variants same pass; cursor
  already system (no cursor to remove — recorded as checked, not assumed).
- **P6 Scroll:** no pinning; no scroll signature beyond the usage meter's fill (the
  settings pages are short — a scroll system on a 1-viewport page is decoration).
- **P7 Polish:** 5 signature elements (§4.5) — the minimum count, deliberately: a
  settings area earns quiet elements, not a gallery.

### 4.5 Signature elements (5)

- **E-F1 The Usage Vessel** — storage as a filling jar (pattern `06` E-06): 7.2 GB of
  10 GB; projected line at 9.1 GB by 1 Dec; near-limit tint ≥90%. The fill IS the usage.
- **E-F2 The Sync Ping** — each queued reading (42) is a sonar ping on the sync panel;
  as readings sync, their pings fade (200 ms) and the count falls ("42 waiting" →
  "0 waiting — all synced"). The pings ARE the queue.
- **E-F3 The Plan Card's Seal** — the current plan card carries a seal (a drawn ring,
  400 ms) marking "Current plan"; changing plan moves the seal (240 ms slide) — the
  seal IS the current plan, not a badge pasted on.
- **E-F4 The Member Rail** — the team list is a rail of members; inviting a member
  adds a bead to the rail (240 ms) with their name; the rail IS the team.
- **E-F5 The Notification Bell** — the notifications section has a bell that rings
  once (a 200 ms tilt, ≤6°) when a preference changes and the change is saved; the
  bell IS the saved confirmation (replacing a toast for every toggle, `04` §13).

### 4.6 Leak audit

| Leak (BEFORE) | Surface | Count |
|---|---|---|
| "PostgreSQL 15 · 7.2 GB" | Billing → Storage | 1 |
| "API endpoint: /v2/readings · table: field_readings" | Sync panel | 1 |
| "Sync worker: pending · 42 rows queued" | Sync status line | 1 |
| "12 pages · 4 modules" | Settings footer | 1 |
| "Billing Service v2.3 — Auth Module healthy" | Admin banner | 1 |
| "Rate limit: 100 req/min on /v2/bookings" (sic — copied from another service's docs) | Plan limits line | 1 |
| **Leak score BEFORE: 6 → AFTER: 0 (target zero). Gate veto: cleared.** | | |
- **Worked leak fix (C-07 / pair L-6):** BEFORE — the sync panel read "API endpoint:
  /v2/readings · table: field_readings" and the status line read "Sync worker: pending ·
  42 rows queued". Fix — the panel now reads "Your readings sync when you're back in
  signal." and the status line reads "42 readings waiting to sync — they'll send when
  you're back in signal." (The user's question is "will my work be saved?" — answered
  in user terms; the endpoint, the table, the worker, and the row count are all gone.)
  The sync pings (E-F2) now carry the queue visually: 42 pings, fading as they sync.
  Verification — copy scan re-run (ban-list grep = 0 hits); error-path walkthrough
  (sync failure stubbed — the error reads "Couldn't sync your readings. They'll send
  when you're back in signal. [Retry]" with 0 leaking strings); non-technical-user test
  on the settings page: no sentence required stack knowledge. (`09-architecture-leak.md`
  pairs L-6, L-10.)

### 4.7 Motion dial per page

| Page family | Dial | Reason |
|---|---|---|
| Settings (all four routes) | 1 (Still) | Task flow; clarity over choreography; surveyors in sunlight with gloves |
| Billing `/app/settings/billing` | 1 | Same — the usage vessel fills (800 ms) and nothing else moves |

### 4.8 BEFORE → AFTER scores (lowest family: settings)

| Category | BEFORE | AFTER | Movement caused by |
|---|---|---|---|
| 1. Hierarchy & focal order | 3 | 8 | P3 grouping by user job; P2 type hierarchy |
| 2. Element integration | 2 | 8 | P7 five merged elements (vessel, pings, seal, rail, bell) |
| 3. Readability & contrast | 5 | 10 | P2 sunlight contrast (≥7:1 body); P4 toggle text (not colour alone) |
| 4. Motion smoothness | 4 | 8 | P5 one loop; dial 1 enforced (no smuggled spectacle) |
| 5. Performance | 5 | 8 | P5 loop merge; profile: longest task 140 ms → 35 ms |
| 6. Never-invisible safety | 6 | 10 | P4/P6: JS-gated reveals removed; observer-stub test 0 stranded |
| 7. Reduced motion | 0 | 10 | P5 reduce variants same pass; emulation 0 continuing motion |
| 8. Aliveness | 2 | 8 | P7: vessel, pings, bell — quiet life; stillness deliberate elsewhere |
| **TOTAL** | **3+2+5+4+5+6+0+2 = 27/80** | **8+8+10+8+8+10+10+8 = 70/80** | **BEFORE 27/80 → AFTER 70/80 (target ≥68)** |

Note: the headline BEFORE (27/80) differs from the task brief's "~35/80" — the brief's
figure was an estimate; the audit method (`01` §5) on the described defects produces
27/80, and the table shows its arithmetic. The AFTER target (≥68) is met at 70/80.
(See §1.1: the table's arithmetic governs, not the estimate.) Study (a)'s BEFORE
(28/80) differs from its brief "~38/80" for the same reason — the brief figures were
estimates; the tables are the audit-method scores.

### 4.9 Deliberately left unchanged

- The plan prices and the charge date (commercial facts — the upgrade presents them,
  it does not renegotiate them).
- The sync mechanism and the offline queue (behaviour freeze; the upgrade changes how
  the queue is shown — pings — not how it works).
- The payment card update flow (regulated flow; presentation only, no step reordered).

### 4.10 Rollback / regression evidence

- Branch `upscale/fieldnote-settings`; flags `upscale.settings`, `upscale.billing`.
- Baseline freeze (`10` §1): 4 routes, 3 primary flows (change plan, invite member,
  toggle notification), screenshot pairs 1440/390, scroll profile (longest task 140 ms).
- Regression checklist after every pass (`10` §2): all 3 flows green; toggle states
  verified (On/Off text present after every pass — the colour-alone defect must never
  return); console 0 errors; API calls unchanged.
- No rollback was needed. The Pass 4 inverse (restore the old toggle component + the
  old settings wall) was recorded before Pass 4 started and never used (`10` §4).

## 5. Cross-reference map

| Study | Decision record source | Signature-element patterns | Leak pairs used |
|---|---|---|---|
| (a) Northwind Ledger | `02` §6 — new (archive family) | `06` E-01 (ledger line) | `09` L-1, L-4 (+ L-2, L-3, L-5) |
| (b) Harbour Books | `02` §6.1 Example D1 | `06` E-05 (shelf) | `09` L-8 (+ L-9, L-12) |
| (c) Fieldnote | `02` §6.2 Example D2 | `06` E-06 (usage vessel) | `09` L-6 (+ L-7, L-10) |
