# UI/UX Upscaler — Spec 04: Component Upgrades

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Expands Protocol
> Step 4 Pass 4 (components & UI states). Authority: `skills/frontend/component-library/SKILL.md`,
> `skills/frontend/ui-states/SKILL.md`, `skills/frontend/design-tokens/SKILL.md`,
> design-intelligence §2–§5.
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule (this file's §2, binding on every component below):**
> labels, empty states, and error messages use ONLY user-facing concepts; error states
> must NEVER name endpoints, schemas, tables, or services. Full spec: `09-architecture-leak.md`.

## 1. How to read every component spec below

Each component follows the same contract. A component that ships without any row of
its contract is unfinished, not "mostly done".

### 1.1 The state matrix (all components)

| State | Definition | Design requirement |
|---|---|---|
| Rest | Default, untouched | On-scale type, token colours, resting shadow/radius per theme |
| Hover | Pointer over (fine pointers only) | Transform/opacity only, 120–240 ms, token easing; never the sole carrier of meaning (touch has no hover) |
| Focus | Keyboard / programmatic focus | Visible focus ring: 2 px outline, `--focus` token, 2 px offset, never removed; focus must never be obscured by pinned elements (WCAG 2.4.11) |
| Active | Pressed / held | Immediate feedback (≤50 ms to first visual change); translateY 1 px or scale 0.98, 120 ms; no bounce/elastic on functional state changes (BAN-FE-044) |
| Disabled | Cannot be used right now | 40–50% opacity OR token disabled colours; `aria-disabled` / `disabled` attribute; must still explain WHY (adjacent text or tooltip — a disabled button with no reason is a defect) |
| Loading | Waiting on real data/action | Skeleton matching the layout for waits ≥300 ms; inline spinner (16 px, 600 ms rotation) for button actions; never a blank area; never a skeleton for waits <300 ms |
| Empty | No data to show | Real empty state: what is empty (user concept), why, and the next action — never "No data" alone, never a table/collection name |
| Error | Something failed | User-concept message + next step + retry action; NEVER the stack (see §2); error styling: `--error` token, icon + text (never colour alone) |

Touch: every hover state has a tap/scroll equivalent; touch targets ≥44×44 px;
no hover-dependent information (tooltips on hover must also open on tap/focus).

### 1.2 Breakpoint behaviour (all components)

- **≥1200 px:** full spec as written.
- **768–1199 px:** spacing ×0.875, type stays on-scale (snap down one scale step max);
  multi-column components collapse to fewer columns per the per-component row below;
  motion intensity follows the page dial (`02-theme-decision.md` §5).
- **<768 px:** single column unless the component's row says otherwise; touch targets
  ≥44 px enforced (this is where most violations hide — verify, don't assume);
  hover-only affordances replaced by tap equivalents; drawers/sheets replace modals
  where the row says so.

### 1.3 Behaviour contract (all components)

"Upscaled 50x" changes presentation only. Before/after behaviour test per component:
same clicks, same keyboard flow, same outcomes, same data. If a visual change alters
an outcome, stop — justify it in the audit file (Protocol Step 2) and get it approved
before touching it. Never delete a working feature to make the design easier.

### 1.4 Tokens consumed (convention)

Every component lists the exact CSS variables it consumes (`--color-*`, `--space-*`,
`--radius-*`, `--shadow-*`, `--dur-*`, `--ease-*`). A component consuming a value
outside its listed tokens is a token lint failure (Pass 1 grep).

## 2. Copy / label rules per component family (leak rules — binding)

These rules apply to EVERY component in §3–§18. A component that passes its visual
spec but violates this section fails Pass 4.

| Rule | Requirement | Example |
|---|---|---|
| L-C1 User concepts only | Labels name what the user sees/does, never what the system stores. Nouns come from the user's world (books, readings, invoices, bookings), never from the schema. | "Your books" not "records"; "1,204 books on your shelf" not "1,204 rows" |
| L-C2 No stack terms anywhere | No DB names/types, table/collection names, API endpoints, module/service names, tech-stack labels, schema/field names — in labels, headings, placeholders, helper text, tooltips, aria-labels, or `title` attributes. Full ban list: `09-architecture-leak.md` §2. | — |
| L-C3 Errors name the next step, never the cause's internals | Error = what happened in user terms + what to do + retry. Never an HTTP status, endpoint path, constraint name, or service name. | "We couldn't save your invoice. Check your connection and try again. [Retry]" — not "422: invoices.customer_id FK violation" |
| L-C4 Empty states carry a next action | Every empty state: what is empty (user concept) + why (if known, in user terms) + the one next action (button/link). Never "No data", never a table name. | "No bookings yet — when someone books, they'll appear here. [Share your booking link]" |
| L-C5 Counts are user counts | Numbers shown are counts of user things (books, bookings, readings), with the unit named. Never counts of pages, routes, modules, tables, or records. | "12 bookings" not "12 pages · 4 modules" |
| L-C6 Loading text is user text | Loading/skeleton labels name what is loading in user terms ("Loading your bookings…"), never the resource being fetched. No endpoint, no table, no "Fetching /v2/…". | "Loading your bookings…" not "Fetching /api/bookings" |
| L-C7 Admin screens are still user surfaces | Admin/settings screens follow the same rules. An admin is a user; "admin" does not license stack terms. Technical detail an admin genuinely needs (e.g. storage used) is expressed in user concepts — see `09-architecture-leak.md` §7. | "Storage: 7.2 GB of 10 GB used" not "PostgreSQL 15 · 7.2 GB" |
| L-C8 URLs shown to users | A URL displayed in the UI (share link, breadcrumb, "view" link) shows the user-facing path only. Never an internal API URL, never a query string naming fields. | — |

**Copy check method (Pass 4 exit):** extract every user-facing string the pass touched
(labels, placeholders, helper text, empty/error/loading strings, aria-labels); run the
leak checklist (`09-architecture-leak.md` §5) over the extracted list; leak count must
be 0. A string that "only developers will see" is still user-facing if it renders in
the browser — the test is rendering, not intent.

## 3. Top navigation + sidebar navigation

- **Before/after criteria:** BEFORE — logo + 5–8 undifferentiated links, no active state
  beyond colour, mobile hamburger that opens a full-screen list with no hierarchy.
  AFTER — one clear primary action (the page's next step, per the 3-second test), active
  route indicated by weight + a 2 px indicator bar (not colour alone), grouped links
  (≤7 top-level, rest grouped), mobile nav that preserves the grouping.
- **State matrix:** Rest — 64 px bar (≥1200 px), 56 px (<768 px), `--surface` ground,
  16 px links. Hover — link underline draws 160 ms `--ease-out`, or background
  `--surface-muted` 120 ms. Focus — 2 px `--focus` ring, 2 px offset, visible on the
  link (not the bar). Active — current route: 600 weight + 2 px accent bar under the
  link; `aria-current="page"`. Disabled — n/a for nav links; a disabled nav item is
  removed, not greyed (a greyed link that cannot be clicked is a dead end with no reason).
  Loading — nav never shows a loading state; route changes use the page transition
  (`05-motion-system.md` §2). Empty — n/a. Error — n/a (a failed route load is a page
  error state, §18).
- **Breakpoints:** ≥1200 px — full horizontal nav, sidebar 264 px fixed where the app
  has one (dashboard). 768–1199 px — sidebar collapses to 72 px icon rail with labels
  on hover/focus (labels also available on tap); top nav condenses to logo + primary
  action + menu. <768 px — top nav 56 px; sidebar becomes a bottom sheet / drawer
  (slide 280 ms `--ease-out`, scrim 200 ms fade); drawer focus is trapped while open
  and returns to the trigger on close.
- **Accessibility:** nav is `<nav aria-label>`; sidebar groups are lists with headings;
  skip link ("Skip to content") first in tab order, visible on focus; mobile drawer
  `role="dialog" aria-modal`, Esc closes, focus returns.
- **Tokens:** `--surface`, `--surface-muted`, `--text`, `--text-muted`, `--accent`,
  `--focus`, `--space-4/6/8`, `--dur-fast 160ms`, `--ease-out`.
- **Upscaled 50x means:** the active indicator animates between routes (240 ms slide,
  transform-only); the sidebar section for the current area expands with a 200 ms
  height/opacity choreography; the mobile drawer opens with a staggered link entrance
  (40 ms stagger, capped at 8 links). **Must NOT change:** route structure, link
  destinations, auth gating.
- **Copy rules (§2):** link labels are user jobs ("Bookings", "Your shelf"), never module
  names ("CRM Module", "Admin Panel v2"). The sidebar footer shows no counts of pages
  or modules (L-C5).

## 4. Buttons + links

- **Before/after:** BEFORE — 4+ button styles, inconsistent radii/padding, primary and
  secondary indistinguishable, links that look like buttons and vice versa.
  AFTER — 3 variants only (primary, secondary, ghost/destructive as a separate
  destructive variant), each with one radius, one padding scale, one focus ring.
- **State matrix:** Rest — primary: `--accent` fill, `--on-accent` text, 40 px height
  (44 px touch), 12/20 px padding, radius `--radius-md`; secondary: transparent fill,
  1 px `--border` stroke; ghost: no fill, no stroke. Hover — primary darkens 8%
  (token `--accent-hover`) + translateY −1 px, 160 ms; secondary border darkens.
  Focus — 2 px `--focus` ring, 2 px offset (never `outline: none` without replacement).
  Active — translateY 1 px / scale 0.98, 120 ms; feedback begins ≤50 ms.
  Disabled — 45% opacity, `aria-disabled`, cursor `not-allowed`, with a reason in
  adjacent text or tooltip. Loading — 16 px spinner replaces the icon (label stays,
  width preserved to avoid layout shift — reserve the spinner's 16 px + 8 px gap in
  the resting layout); button is `aria-busy`, clicks ignored but focusable.
  Empty/Error — n/a (buttons don't have empty/error states; their *outcomes* do — §18).
- **Breakpoints:** ≥1200 px — as above. <768 px — primary actions full-width in forms
  and sheets; minimum height 44 px; destructive actions never adjacent to primary
  without a 12 px gap.
- **Accessibility:** real `<button>` / `<a>`; icon-only buttons have `aria-label`;
  destructive actions confirm (modal, §10) unless the action is undoable (then undo
  toast, §11, within 5 s). Contrast: primary text on accent ≥4.5:1.
- **Tokens:** `--accent`, `--accent-hover`, `--on-accent`, `--border`, `--focus`,
  `--error`, `--dur-fast 160ms`, `--ease-out`.
- **Upscaled 50x means:** the primary button's hover is a 160 ms lift + 8% darken, not
  a colour snap; the loading spinner is the theme's material (e.g. a drawing ledger
  line, a filling vessel — 600 ms loop, transform-only); destructive hover arms in
  two stages (hover 160 ms → `--error` fill at 200 ms) so a destructive click is never
  a surprise. **Must NOT change:** what the button does, its order in a form, or its
  keyboard behaviour.
- **Copy rules (§2):** button labels are verbs in user terms ("Save invoice", "Book now"),
  never stack verbs ("Submit POST", "Sync DB"). Loading label keeps the verb
  ("Saving…") — never "Posting /v2/invoices" (L-C6).

## 5. Forms (inputs, selects, checkboxes, validation, multi-step)

- **Before/after:** BEFORE — inputs with no labels (placeholder as label), validation
  only on submit, errors as red text under the field naming the constraint, multi-step
  with no progress honesty. AFTER — every input has a persistent visible label,
  inline validation on blur + submit, errors name the fix in user terms, multi-step
  progress is honest (see below).
- **State matrix (inputs):** Rest — 44 px height, 12 px padding, 1 px `--border`,
  radius `--radius-md`, 16 px body text, label 14 px 600 above the field (never inside
  as a placeholder). Hover — border darkens 120 ms. Focus — 2 px `--focus` ring +
  border `--accent`, 160 ms. Active — caret visible, no layout change. Disabled —
  `--surface-muted` fill, `--text-muted` text, reason in helper text. Loading — n/a
  (fields don't load; their *options* do — select options loading shows "Loading
  options…" in user terms). Empty — placeholder is an EXAMPLE ("e.g. Ayesha Khan"),
  never an instruction and never a field name. Error — 2 px `--error` border + error
  icon + message below the field, `aria-invalid="true"`, `aria-describedby` to the
  message; error message names the fix ("Enter a date in the future") — never the
  schema ("`bookings.date` must be > NOW()").
- **Selects:** native `<select>` styled, or a custom listbox with full keyboard support
  (arrow keys, type-ahead, Esc, Enter); options loading state per §1; no option text
  names a table/field.
- **Checkboxes/radios:** 20×20 px box (44 px hit area via padding), check draws 160 ms
  (SVG stroke-dash, `--ease-out`); focus ring on the box; group has a `<fieldset>` +
  `<legend>`; error state on the group, not just the box.
- **Validation:** on blur for a touched field, on submit for all; success is shown by
  the absence of error + a check icon (200 ms draw) — never a green wall of text.
  Multi-step: progress shows "Step 2 of 4 — Your details" (user concepts), the bar
  fills by completed steps only (never jumps 25%→100% on the last step), each step's
  state (done/current/upcoming) is text + icon, not colour alone; the back button
  preserves entered data.
- **Breakpoints:** ≥1200 px — two-column forms where the theme allows, labels above
  fields (never beside, except checkboxes). <768 px — single column, 44 px fields,
  step indicator condenses to "Step 2 of 4" text + a thin honest bar.
- **Accessibility:** every input has a `<label for>`; error messages are
  `role="alert"` on submit and `aria-live="polite"` on blur; required fields marked
  with text "(required)" as well as `aria-required`; autocomplete attributes on
  identity/payment fields.
- **Tokens:** `--surface`, `--border`, `--accent`, `--focus`, `--error`, `--success`,
  `--text`, `--text-muted`, `--radius-md`, `--dur-fast 160ms`.
- **Upscaled 50x means:** the field's focus is a 160 ms ring + border choreography, not
  a snap; the multi-step transition slides the step content 240 ms with a masked reveal
  (outgoing fades 160 ms, incoming rises 12 px over 240 ms); the success check draws in
  200 ms. **Must NOT change:** validation rules, required/optional status, submission
  behaviour, data shape.
- **Copy rules (§2):** labels, placeholders, helper text, and error messages per L-C1–C4.
  A validation error that names a field ("`users.email` unique") is a leak (L-C3) and a
  failed component — rewrite it before the component passes.

## 6. Data tables

- **Before/after:** BEFORE — unstyled grid, no row hover, no sort indication, 200 rows
  with a stranded-reveal bug, pagination as "Page 1 of 12" with no result count honesty.
  AFTER — tabular numerals, sortable headers with direction indicators, row hover +
  selected states, sticky header, honest counts ("Showing 1–25 of 1,204 bookings").
- **State matrix:** Rest — 48 px rows (44 px touch), 12/16 px cell padding, header
  12 px 600 uppercase 0.08em tracking, row divider 1 px `--border`. Hover — row
  `--surface-muted` 120 ms. Focus — row/cell focus ring 2 px where rows are actionable;
  sortable header is a `<button>` with `aria-sort`. Active — row press: 120 ms
  `--surface-muted` deepen. Disabled — n/a (rows aren't disabled; actions within a row
  can be, per §4). Loading — skeleton rows matching the column layout (5 rows, shimmer
  1200 ms, transform-only) for waits ≥300 ms. Empty — full-width empty state with a
  next action (L-C4), never "0 rows". Error — table area replaced by an error state
  with retry (L-C3), never a stack trace or status code.
- **Breakpoints:** ≥1200 px — full table, sticky header, horizontal scroll only if the
  table genuinely exceeds the container (then the scroll is announced and the first
  column pins). 768–1199 px — low-priority columns hide (record which columns hide at
  which width in the spec — never hide the primary identifier or the row action).
  <768 px — table becomes a card list (each row = one card, primary value first,
  16 px; secondary values 14 px muted) — a horizontally scrolling table on a phone is
  a failed breakpoint.
- **Accessibility:** real `<table>` with `<th scope>`; sort state in `aria-sort`;
  pagination is nav with `aria-label`; row actions reachable by keyboard; sticky header
  never covers the focused row.
- **Tokens:** `--surface`, `--border`, `--text`, `--text-muted`, `--accent`, `--focus`,
  `--dur-fast 120ms`.
- **Upscaled 50x means:** rows enter with a 40 ms stagger (capped at 12 rows, 480 ms
  total) on first load only — repeat visits show rows present (dashboards are re-scanned
  daily; re-animating is a defect); sort re-orders with a 240 ms FLIP-style transform
  (opacity/transform only); the count line counts to the real total once (600 ms).
  **Must NOT change:** sort semantics, filter behaviour, pagination behaviour, data.
- **Copy rules (§2):** column headers are user nouns ("Booking", "Guest", "Total"),
  never field names ("`bookings.guest_id`"); counts are user counts (L-C5); the empty
  state names the filter that produced it ("No bookings for March — try clearing the
  date filter [Clear filter]").

## 7. Dashboards (stat cards, charts, filters)

- **Before/after:** BEFORE — 4 identical stat cards with invented numbers, charts with
  unreadable legends, filters with no empty state. AFTER — stat cards carry live data
  with sources, charts have readable labels at every state, filters show their active
  state and their empty result honestly.
- **State matrix (stat cards):** Rest — 16 px padding, label 12 px 600 uppercase,
  value 32 px tabular, delta 14 px with icon (▲/▼ + text "up 12% from last month" —
  never colour alone). Hover — lift 2 px + shadow, 200 ms (cards that are links only;
  non-link cards do not lift — a lift that promises a click that doesn't exist is a lie).
  Focus — ring on the card link. Active — press 120 ms. Disabled — n/a. Loading —
  skeleton card matching the layout (label/value/delta blocks). Empty — card shows
  "—" with "No data yet" + the reason in user terms. Error — card shows its error state
  with retry (L-C3).
- **Charts:** labels ≥12 px, contrast ≥4.5:1; tooltips on hover AND tap AND focus (S-13);
  chart data is real (a chart of invented data is S-9 + a data-integrity defect);
  the chart's loading state is a skeleton of the chart's shape, not a spinner.
  **Filters:** active filters shown as removable chips (44 px hit area, Esc/× removes,
  `aria-label="Remove filter: March"`); filter combinations returning 0 rows show the
  empty state (L-C4) with "Clear all filters" — never a blank table.
- **Breakpoints:** ≥1200 px — bento/grid per the theme; 768–1199 px — 2-column cards;
  <768 px — 1-column, charts full-width, filters collapse into a sheet.
- **Accessibility:** stat values are text (not images); charts have a text alternative
  (a visually-hidden table or a "View as table" toggle); deltas are text, not colour alone.
- **Tokens:** `--surface`, `--border`, `--text`, `--text-muted`, `--accent`, `--success`,
  `--error`, `--shadow-md`, `--dur-fast 200ms`.
- **Upscaled 50x means:** stat values count to their real values once (800 ms,
  `--ease-out`, tabular numerals, no counting on repeat visits); the chart draws its
  line/bars in 600 ms on first view (SVG stroke/transform, not layout); the filter bar
  animates chip add/remove in 160 ms. **Must NOT change:** the numbers, the filter
  logic, the chart's data source.
- **Copy rules (§2):** stat labels are user concepts ("Bookings this month"), deltas name
  the comparison ("vs February"); chart titles name the question the chart answers
  ("Where do bookings come from?"), never the table ("`bookings_by_channel`").

## 8. Cards + lists

- **Before/after:** BEFORE — identical cards, image + title + "Learn more", no states.
  AFTER — cards carry their content type (product, article, booking, person) with a
  distinct but consistent treatment; lists are scannable (consistent row height, primary
  value first).
- **State matrix:** Rest — radius `--radius-lg`, 1 px `--border`, 16 px padding, image
  16:9 or the content's own ratio (never a forced crop that cuts the subject).
  Hover — lift 2 px + shadow `--shadow-md`, 200 ms; image scales 1.03 in-frame
  (scale-in-frame, `05` §2 — the image grows inside its frame, the frame never moves).
  Focus — ring on the card link (the whole card is one link where it navigates; nested
  links inside a card link are forbidden). Active — press 120 ms.
  Disabled — n/a (cards aren't disabled). Loading — skeleton card matching the layout.
  Empty — list empty state per L-C4. Error — list error state per L-C3.
- **Breakpoints:** ≥1200 px — grid per theme (3–4 columns catalogue); 768–1199 px — 2
  columns; <768 px — 1 column, cards full-width, image 16:9.
- **Accessibility:** cards are articles with headings in order; images have alt text
  describing the content (never "image"); list markup is a real list.
- **Tokens:** `--surface`, `--border`, `--shadow-md`, `--text`, `--text-muted`,
  `--radius-lg`, `--dur-fast 200ms`.
- **Upscaled 50x means:** the card's image scale-in-frame is 400 ms `--ease-out`; the
  card's entrance stagger is 40 ms capped at 8 cards; the list's dividers are the
  theme's material (a seam, a rule, a shelf edge — not a default 1 px grey line
  unless the theme is genuinely minimal). **Must NOT change:** the card's destination,
  the list order, or the data shown.
- **Copy rules (§2):** card titles are the content's own title; metadata lines name user
  things ("3 nights · 2 guests"), never record counts.

## 9. Modals + drawers

- **Before/after:** BEFORE — modal that traps focus badly or not at all, no Esc, backdrop
  click closes without warning on a dirty form. AFTER — focus trapped while open,
  returned on close, Esc closes (except a dirty form, which confirms), backdrop click
  never discards unsaved work silently.
- **State matrix:** Rest — centred, max-width 560 px (≥1200 px), radius `--radius-lg`,
  shadow `--shadow-lg`, header + body + footer. Open — backdrop fades 200 ms, panel
  rises 12 px + fades 240 ms `--ease-out` (transform/opacity only). Focus — trapped
  inside; first focus goes to the heading (or the first field for a form modal);
  focus returns to the trigger on close. Active — n/a. Disabled — n/a.
  Loading — modal content loading shows a skeleton of the modal's layout, not a
  spinner in an empty box. Empty — n/a. Error — modal error state with retry (L-C3).
  Drawer (mobile + secondary panels): slides from the right (≥768 px) or bottom
  (<768 px, sheet), 280 ms `--ease-out`; scrim fades 200 ms.
- **Breakpoints:** ≥1200 px — modal centred 560 px; 768–1199 px — 480 px; <768 px —
  modal becomes a bottom sheet (full-width, radius top only, drag handle present but
  never required — a close button always exists).
- **Accessibility:** `role="dialog" aria-modal="true" aria-labelledby`; Esc closes;
  focus trap + return; backdrop is `aria-hidden`; the page behind is inert while open.
- **Tokens:** `--surface`, `--shadow-lg`, `--radius-lg`, `--border`, `--focus`,
  `--dur-fast 240ms`, `--ease-out`.
- **Upscaled 50x means:** the open choreography is 240 ms total (backdrop 200 ms fade
  + panel 240 ms rise, overlapping, not sequential); the close is 180 ms (faster than
  open — exits are always faster); a dirty-form close shows the confirm step as a
  second modal state, not a `window.confirm`. **Must NOT change:** what the modal does,
  its trigger, or its dismissal rules for destructive actions.
- **Copy rules (§2):** modal titles are user actions ("Cancel booking?"), body copy names
  the consequence in user terms ("You'll lose the 2 nights you selected"), never the
  stack. No endpoint, table, or service name in any modal.

## 10. Toasts + alerts

- **Before/after:** BEFORE — `alert()` or a toast that stacks forever, no action, no
  dismiss. AFTER — one toast at a time (queue, max 3), auto-dismiss 5 s with a visible
  countdown, action where the user needs one (Undo), dismiss button always present.
- **State matrix:** Rest — bottom-right (≥1200 px) / bottom-centre full-width minus
  16 px margins (<768 px), `--surface` + 1 px `--border` + icon + message + action +
  dismiss, 14 px text. Enter — rises 12 px + fades 200 ms. Hover — pause the
  auto-dismiss countdown while hovered/focused. Focus — dismiss + action are keyboard
  reachable; toast container is `aria-live="polite"` (assertive only for errors that
  block the user's task). Active — n/a. Disabled — n/a. Loading — n/a. Empty — n/a.
  Error — error toast: `--error` icon + message per L-C3 + Retry action where a retry
  exists; never a status code.
- **Breakpoints:** <768 px — full-width minus margins, stacked max 2 visible.
- **Accessibility:** `role="status"` / `role="alert"` as appropriate; auto-dismiss never
  removes a toast the user is interacting with; toasts never cover a focused element
  or the primary action.
- **Tokens:** `--surface`, `--border`, `--success`, `--error`, `--text`, `--dur-fast 200ms`.
- **Upscaled 50x means:** the toast's icon draws in 200 ms (check stroke, alert mark);
  the countdown is a 5 s thin progress line in the toast's own accent (transform
  scaleX, not width). **Must NOT change:** the message's meaning, the undo window (5 s),
  or the action's outcome.
- **Copy rules (§2):** toast copy is one sentence in user terms + the action ("Booking
  saved. [Undo]"). Never "200 OK", never an endpoint.

## 11. Tabs + accordions

- **Before/after:** BEFORE — tabs as styled divs with no keyboard support, accordions
  that jump the page. AFTER — real tab pattern (arrow-key navigation, `aria-selected`),
  accordions that animate height without layout thrash (transform/opacity where possible,
  measured-height animation only with a recorded exception).
- **State matrix:** Rest — tab 44 px height, 16 px text, inactive `--text-muted`.
  Hover — `--surface-muted` 120 ms. Focus — ring 2 px. Active (selected) — 600 weight
  + 2 px accent underline, `aria-selected="true"`. Disabled — tab disabled only with a
  reason ("Available after you save"); otherwise the tab is present and reachable.
  Loading — tab panel loading shows a skeleton of the panel. Empty — panel empty state
  per L-C4. Error — panel error state per L-C3.
- **Breakpoints:** <768 px — tabs scroll horizontally (scrollable tab list, scroll
  position preserved) or become an accordion; accordions stack full-width.
- **Accessibility:** `role="tablist/tab/tabpanel"`, arrow keys move between tabs, Home/End
  jump; accordion buttons have `aria-expanded` + `aria-controls`; panel content is in
  the tab order only when its tab is selected.
- **Tokens:** `--surface-muted`, `--accent`, `--text`, `--text-muted`, `--focus`,
  `--dur-fast 160ms`.
- **Upscaled 50x means:** the tab indicator slides 240 ms between tabs (transform-only);
  the panel changes with a 200 ms masked fade (outgoing 120 ms, incoming 200 ms).
  **Must NOT change:** tab order, panel contents, or the URL state (if tabs are
  deep-linked, the link stays).
- **Copy rules (§2):** tab labels are user sections ("Bookings", "Settings"), never module
  names; accordion headings are questions the user asks, not field groups.

## 12. Search + command palette

- **Before/after:** BEFORE — a search box with no results state, no keyboard shortcut,
  results that name database fields. AFTER — search with a real empty state, keyboard
  shortcut (`/` or Cmd+K, shown in the UI), results grouped by user concept with a
  next action per result.
- **State matrix:** Rest — 44 px input, icon + placeholder ("Search bookings, guests…"
  — user nouns, never "Search records"). Hover — border darkens. Focus — ring + the
  shortcut hint visible. Active — typing: results update as-you-type with a 150 ms
  debounce (never per-keystroke network calls). Disabled — n/a. Loading — results
  area shows skeletons for waits ≥300 ms. Empty — "No results for 'X'" + suggestions
  ("Try a guest name or a booking date") + a next action. Error — error state per L-C3.
  Command palette: opens 200 ms (fade + scale 0.98→1), fuzzy results grouped by user
  concept, arrow-key navigation, Enter runs, Esc closes, footer shows the shortcut hints.
- **Breakpoints:** <768 px — search becomes a full-screen sheet; palette is full-screen.
- **Accessibility:** `role="searchbox"`, results are a listbox with `aria-activedescendant`
  or roving tabindex; the shortcut is announced; results count is announced politely.
- **Tokens:** `--surface`, `--border`, `--accent`, `--focus`, `--text-muted`,
  `--dur-fast 200ms`.
- **Upscaled 50x means:** the palette's open is 200 ms; result rows highlight with a
  120 ms background fade; the "no results" state has a next action, not a dead end.
  **Must NOT change:** search semantics, ranking, or the actions results perform.
- **Copy rules (§2):** result titles are user things; result subtitles name the user
  context ("Booked 12 Mar · 2 guests"), never the table or the endpoint that served it.

## 13. Settings / billing screens

- **Before/after:** BEFORE — settings as a wall of toggles with stack labels ("PostgreSQL",
  "API v2", "12 pages"), billing as a table of field names. AFTER — settings grouped by
  user job (Profile, Notifications, Billing, Privacy), each group with a plain-language
  heading; billing shows the plan, the next charge date, and usage in user units.
- **State matrix:** per §5 (forms) for each control; toggles: 48×28 px track, knob
  24 px, state change 200 ms transform-only, state announced (`aria-checked`, and text
  "On/Off" beside the toggle — never colour alone). Plan card: current plan marked
  with text "Current plan" + a 2 px accent border. Loading — skeleton per section.
  Empty — n/a (settings always have content; an empty billing history shows L-C4 with
  the next invoice date). Error — per L-C3 with retry.
- **Breakpoints:** ≥1200 px — sidebar + content (see §3); <768 px — single column,
  sections as accordions (§11).
- **Accessibility:** settings groups are sections with headings; toggles are real
  switches (`role="switch"`); billing amounts are text with currency, never images.
- **Tokens:** `--surface`, `--border`, `--accent`, `--success`, `--error`, `--focus`,
  `--dur-fast 200ms`.
- **Upscaled 50x means:** saving a setting gives immediate inline feedback (the row's
  "Saved" check draws 200 ms; no page reload, no toast for every toggle — toasts are
  for errors and for the one action the user asked to confirm). Billing usage is a
  real meter in user units (see `06-signature-elements.md` §4 for the meter-as-element
  pattern). **Must NOT change:** plan semantics, charge behaviour, or privacy defaults.
- **Copy rules (§2):** this family is the highest-leak-risk surface in most apps
  (see `09-architecture-leak.md` §3.4 + case study (c) in `08-case-studies.md`).
  Storage is "7.2 GB of 10 GB used" (user units, `09` §7); the plan is "Pro — £18/month,
  next charge 1 Dec"; never "PostgreSQL 15", never "/v2/billing", never a table name.

## 14. Onboarding flows

- **Before/after:** BEFORE — 5 steps of undifferentiated forms, no sense of progress,
  no skip, no "why are you asking this". AFTER — ≤5 steps, each step states why the
  information is needed (one line, user terms), progress is honest, skip is always
  available where the step is optional, completion has a real next action.
- **State matrix:** per §5 (forms) + §11 (step progress); step states: done (check,
  200 ms draw), current (accent + "Step 2 of 4"), upcoming (muted). Loading — step
  transition 240 ms masked slide (§5). Empty — n/a. Error — per-step error per L-C3,
  the step is not lost (data preserved).
- **Breakpoints:** <768 px — single column, progress condenses to text + thin bar.
- **Accessibility:** steps are a list with `aria-current="step"`; focus moves to the
  new step's heading on transition; skip links are real buttons.
- **Tokens:** per §5 + `--accent`, `--success`.
- **Upscaled 50x means:** the step transition is the theme's material (a page turning,
  a shelf filling, a route advancing — 240 ms, never a generic slide); the completion
  state is the user's first real content, not a confetti screen (a confetti screen is
  S-3 pasted decoration). **Must NOT change:** the data collected, the order of
  required steps, or the ability to skip optional steps.
- **Copy rules (§2):** each step's "why" line is user terms ("So we can address your
  invoices correctly"); never "Required by `users.company_name` NOT NULL".

## 15. Empty states

- **Before/after:** BEFORE — blank area, or "No data". AFTER — an illustration or
  in-theme element that IS the empty content's story (an empty shelf, an unfilled
  vessel — see `06-signature-elements.md`), a headline in user terms, one line of
  explanation, one primary next action.
- **State matrix:** Rest — centred, 64 px vertical padding, headline 20 px, body 16 px
  muted, action button primary. Hover/Focus/Active — per §4 on the action. Loading —
  n/a (empty is not loading; if the state is unknown, show a skeleton, not an empty state
  — a premature empty state is a defect). Error — distinct from empty (error per L-C3).
- **Breakpoints:** <768 px — padding 40 px, headline 18 px, action full-width.
- **Accessibility:** empty state is a section with a heading; the action is a real button/link.
- **Tokens:** `--surface`, `--text`, `--text-muted`, `--accent`.
- **Upscaled 50x means:** the empty state's element is merged (it depicts the thing
  that is empty — the shelf with no books, the calendar with no bookings — and fills
  as content arrives). **Must NOT change:** the condition that produces the empty state.
- **Copy rules (§2):** L-C4 is the whole spec here. An empty state that names a table
  ("No rows in `bookings`") fails Pass 4 outright.

## 16. Loading states (skeleton)

- **Before/after:** BEFORE — spinner in a blank page, or nothing (blank wait). AFTER —
  skeletons that match the layout being loaded, shown only for waits ≥300 ms, replaced
  by content with a 200 ms fade (no flash, no layout shift — the skeleton reserves the
  content's space).
- **State matrix:** Rest — skeleton blocks in `--surface-muted`, radius matching the
  content, shimmer 1200 ms (a 40% `--surface` band travelling, transform-only).
  Hover/Focus/Active/Disabled — n/a (skeletons are not interactive; pointer events off).
  Loading — the skeleton IS the loading state. Empty/Error — if loading resolves to
  empty or error, the skeleton is replaced by §15/§18, never left in place.
- **Breakpoints:** skeleton layout follows the component's breakpoint layout (a card
  skeleton at <768 px is single-column, like the cards).
- **Accessibility:** skeleton container has `aria-busy="true"` and `aria-live="polite"`;
  skeletons are `aria-hidden` (they carry no information); reduced-motion shows static
  skeleton blocks (no shimmer).
- **Tokens:** `--surface-muted`, `--surface`, `--dur-shimmer 1200ms`.
- **Upscaled 50x means:** the shimmer is the theme's material (a light sweep, a filling
  vessel — 1200 ms, transform-only); the content's entrance after load is a 200 ms fade,
  not a pop. **Must NOT change:** the loading threshold (300 ms) or the content that loads.
- **Copy rules (§2):** skeleton labels (where any text shows) per L-C6 — user terms only.

## 17. Error states

- **Before/after:** BEFORE — browser default, stack trace, status code, or a red
  "Error!" with no next step. AFTER — a human error state: what happened (user terms),
  what to do, retry/secondary action, and (where it helps) a way to get help — all
  without naming the stack.
- **State matrix:** Rest — icon + headline (20 px) + one line of explanation + primary
  action (Retry) + secondary (Go back / Get help). Hover/Focus/Active — per §4 on the
  actions. Loading — retry shows its loading state (§4). Empty — n/a (error is not empty).
  Error-of-error — if retry fails twice, the state changes: it offers the help path
  prominently ("Still not working? Contact support — include reference ABC-123", where
  the reference is a user-facing code, not a trace ID naming a service).
- **Breakpoints:** <768 px — full-width, actions stacked, primary first.
- **Accessibility:** error state is `role="alert"` on arrival; focus moves to its
  heading; the retry is a real button.
- **Tokens:** `--error`, `--surface`, `--text`, `--text-muted`, `--accent`.
- **Upscaled 50x means:** the error state's icon draws in 200 ms; the retry is immediate
  (no flourish before the action unlocks — feedback theatre, motion FE-087). **Must NOT
  change:** the error condition, or the data the user had entered (a form error never
  clears the form).
- **Copy rules (§2):** L-C3 is the whole spec here. See `09-architecture-leak.md` §6
  for the rewrite table (8+ pairs). An error state naming an endpoint, schema, table,
  or service fails Pass 4 outright.

## 18. Cross-reference map

| Component | Pass 4 exit evidence | Leak check (§2) |
|---|---|---|
| §3–§4 Nav, buttons | State-matrix screenshots, keyboard walk | Link/button labels extracted, 0 leaks |
| §5 Forms | Validation walk (error path + success path) | Error strings extracted, 0 leaks |
| §6–§8 Tables, dashboards, cards | Skeleton/empty/error renders per component | Headers, counts, empty states extracted, 0 leaks |
| §9–§12 Modals, toasts, tabs, search | Focus trap + toast queue test | Modal/toast/search strings extracted, 0 leaks |
| §13 Settings/billing | Billing walk (plan, charge, usage in user units) | Full string extraction — highest-risk surface, 0 leaks |
| §14–§17 Onboarding, empty, loading, error | Step walk, empty/error renders | "Why" lines, empty/error copy extracted, 0 leaks |
