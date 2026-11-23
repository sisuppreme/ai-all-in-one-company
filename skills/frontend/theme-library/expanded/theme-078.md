# 78. Trajectory Tables — Expanded (v1 + v2)

> Vintage ballistics and orbital computation as printed
> mathematical tables — the beauty of columns of figures,
> interpolation rules, and the confidence of pre-computer
> mathematics. The site does not display its answers. It
> *computes* its welcome, in mono, in public, with the working
> shown. For aerospace engineering firms, simulation software,
> mathematics education — anyone whose product is a number that
> must be believed.

**The theme's one law: no figure without its working.** Every
number printed anywhere on the page is either a row of the one
declared master table (§6.10, Table VII) or derived from two of
its printed rows by the printed interpolation rule (§6.12) — and
the derivation is shown, not asserted. Corrections never erase:
a corrected figure stays legible beneath its red strike, with the
recomputed value beside it and the corrector's initials in the
margin. A build that prints a figure it cannot trace to Table
VII, that rounds a value for tidiness, or that deletes a struck
figure, has broken the law three ways.

---

## 1. Concept & world

Before the computer was a machine, it was a person — usually
several people, at desks, with printed tables, computing
trajectories by hand and initialling their work. This theme is
that room, bound: a site that behaves like a volume of
trajectory tables from the great age of printed mathematics.
Pages are sheets. Sections are numbered tables. Navigation is
the thumb-index on the fore-edge. Emphasis is not bold or colour
— it is the double rule drawn beneath a final answer, an honour
the book grants sparingly. Error is not hidden — it is corrected
in red, in the open, because a table you cannot audit is a table
you cannot trust.

The world has three inhabitants. **The tables themselves** —
columns of figures in tabular mono, ruled every line, captioned
and numbered, carrying the site's actual data (product ranges,
performance figures, pricing tiers, course syllabi — whatever
the site must tabulate). **The computor** — the unseen hand
whose pencil-grey worked example re-computes itself in the
margin (§6.6), whose initials close every correction, whose
presence says *a person stands behind these figures*. **The
reader-as-computor** — the visitor, who does not merely read
the tables but operates them: scrolling interpolates (§6.2),
hovering lays a straightedge (§6.4), clicking corrects (§6.5).
The site's thesis is that operating a table is more persuasive
than admiring one.

**Best-fit sites and audiences.** Aerospace and defence
engineering firms publishing performance envelopes; simulation
and CAD/CAE software whose marketing is benchmark tables;
ballistics and reloading data publishers; mathematics and
physics education (the interpolation method is genuinely
taught here, §6.12); observatory and ephemeris services;
engineering consultancies whose credibility is numerical.
Audiences: engineers, technical evaluators, students — readers
who align columns with their eyes and distrust a number with no
provenance.

**When NOT to use it.** Consumer retail and lifestyle brands
(the ceremony reads as cold); anything whose data changes
faster than daily (a printed table promises permanence —
live dashboards belong to another theme); sites with almost no
tabular content (the theme has nothing to bind); audiences who
need emotional warmth in the first three seconds (this theme's
warmth is earned slowly, in pencil, in margins). If the client
cannot supply real, stable, checkable figures, do not use this
theme — its law (§6.10) will expose the invention within one
page.

**The volume's declared contents.** One master table rules the
whole site (§6.10): Table VII, trajectories at 45° elevation in
vacuum, g = 9.80665 m/s², six printed rows (v₀ = 200…300 m/s).
The hero's computed headline, the interpolating row, the arc's
apogee label, the margin example, the request form's answers —
every figure on the page is one of those rows or an honest
interpolation between two of them, with the second-difference
correction applied where the rule demands it. A real build
declares its own master table the same way: one table, named,
from which the whole site derives.

---

## 2. Palette

Five anchors from the original entry, plus four derived tokens.
The palette is a printed sheet: paper, ink, the rule line, the
correction, the binding. Nothing else is permitted to be a
colour.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--paper` | `#F0EAD8` | Table paper — the page ground, every sheet | ~78% of surface | Ground for ink (11.9:1), red (5.0:1), maroon (8.5:1) |
| `--ink` | `#2B2B28` | Tabular ink — all figures, body text, rules that carry meaning | ~14% | On paper 11.9:1 — the only colour body text may wear |
| `--rule` | `#B9AE94` | Rule lines — the horizontal ruling of every table, hairlines, table borders | ~5% (as lines, not areas) | On paper ~1.9:1 — a line, never text, never a fill behind text |
| `--red` | `#B03A2E` | Correction red — strikes, recomputed values, corrector's initials, the one licensed alarm | ≤2% | On paper 5.0:1 (AA pass); licensed ONLY for corrections and their kin — never decoration, never a CTA |
| `--maroon` | `#6E2B2B` | Binding maroon — thumb tabs, binding edge, footer ground, plate-frame mounts | ~1% + footer | On paper 8.5:1; paper on maroon 8.5:1 (footer text) |
| `--paper-deep` (derived) | `#E4DABD` | Recessed sheets — plate grounds, the interpolation box's well, skeleton sheets | as needed | Ink on it 10.6:1; never the main ground two sheets running |
| `--paper-bright` (derived) | `#F8F3E5` | Raised slips — the computed slip (§6.15), correction slips, card faces | as needed | Ink on it 12.6:1; a slip must sit on paper or paper-deep, never float on maroon |
| `--pencil` (derived) | `#75705F` | Pencil grey — the computor's hand: worked-example workings, margin notes, initials-in-draft | ≤1% | On paper 4.1:1 — below AA for small text BY DESIGN: pencil never carries unique content; anything that matters is reprinted in ink (see below) |
| `--brass` (derived) | `#8F7134` | The straightedge (§6.4) and only it — a metal tool, not a colour | one element | Graphic only, never text; on paper ~3.9:1 as a 2px rule with a 1px ink edge |

**Contrast rulings.** Ink on paper (11.9:1) is the default for
everything readable. Red (5.0:1) passes AA and is still rationed:
it is licensed for struck figures, recomputed values, initials,
and the errata sheet — a page with red anywhere else has spent
its alarm on decoration. Maroon (8.5:1) carries tab labels and
footer text. Pencil (4.1:1) is the theme's deliberate exception,
governed by the **pencil rule**: pencil shows *working*, never
*answers* — the worked example's final line is always reprinted
in ink (§6.6), margin pencil notes always duplicate an ink
statement elsewhere on the sheet, and no link, label, price or
instruction may exist only in pencil.

**Dark-mode behaviour.** There is none, by ruling. A bound
volume does not invert at night; the sheet is the sheet. The
theme ships one scheme. (A build that needs a dark reading room
wants a different theme; inverting paper to black would turn
corrections invisible and the binding into a void.) The single
exception: the plate frames (§6.9) may mount images on maroon,
in daylight and dark alike.

**Foxing.** Plate corners (§6.9) carry a foxed tint — a
radial-gradient stain in `--rule` at 18% over paper-deep. It is
texture, not a token: it may never sit behind text, and its
seeded positions are fixed per plate so the book does not
re-fox itself between visits.

---

## 3. Typography

Two families, as the original entry rules. **Spectral** —
display and prose: captions, section titles, the Rules plate's
text, all sentences. **IBM Plex Mono** — every figure, every
table cell, every folio, label and initial: the book's
instrument hand. There is no third family and no sans anywhere;
a UI string that "needs" a sans is rewritten until Spectral or
Plex Mono can carry it.

**The figure law.** All numerals are IBM Plex Mono, lining and
tabular (`font-variant-numeric: lining-nums tabular-nums`),
always. Figures align in columns to the decimal point; a column
whose figures do not align is a broken table (§9). Thousands
take a comma (6,373.22), decimals take a point, and the number
of decimals is a per-column constant declared in the table's
caption — a column never mixes 6,373.2 and 6,373.22. Negative
corrections take a true minus (−10.20), never a hyphen.

**Type scale** (1.250 ratio on a 16px base, rem):

| Role | Font | Size | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Display / computed headline | Spectral 600 | 3.052rem (48.8px) | 1.08 | −0.01em | The headline is a statement; its *figure* is set in Plex Mono at the same size (§6.1) |
| Section title ("Table VII") | Spectral 600 | 1.953rem (31.3px) | 1.15 | 0 | Always numbered, always captioned beneath |
| Table caption | Spectral italic 400 | 1.25rem (20px) | 1.35 | 0 | States the table's quantities, units and decimal ruling |
| Body / prose | Spectral 400 | 1rem (16px) | 1.55 | 0 | Measure 58–68ch; prose explains, it never tabulates |
| Table figure (cell) | Plex Mono 400 | 0.9375rem (15px) | 2.0 (the ruled line) | 0 | Sits on the rule grid (§4); right-aligned to the decimal |
| Row / column header | Plex Mono 500 | 0.8125rem (13px) | 1.4 | 0.08em, uppercase | Quantities with units: "RANGE R (m)" |
| Interpolated row figure | Plex Mono 500 | 0.9375rem (15px) | 2.0 | 0 | Weight, not colour, marks it as derived (§6.2) |
| Margin note / initials | Plex Mono 400 | 0.75rem (12px) | 1.45 | 0.02em | Pencil for the hand, ink for the record |
| Folio (§6.14) | Plex Mono 500 | 0.8125rem (13px) | 1 | 0.12em | "ROW 250.0 · t = 0.500" |
| Thumb-tab label | Spectral 600 | 0.8125rem (13px) | 1 | 0.14em, uppercase, rotated | Set on maroon, paper colour (8.5:1) |

**Per-role rules.** Display type never carries a figure in
Spectral — numerals inside a headline are re-set in Plex Mono
mid-line (the seam is the point: words are read, figures are
*computed*). Captions are italic and always answer three
questions: what quantity, in what units, between what limits.
Headers are uppercase mono with the unit in parentheses, never
abbreviated beyond SI. Initials are two letters, uppercase,
period-closed ("E.M."), set in red when they close a correction
and pencil when they close a working. Nothing is ever set in
red except correction matter (§2). Underlining is forbidden as
a text style — the underline is the double rule (§6.7), an
honour, not a formatting button; links in prose are marked by a
single hairline rule beneath, drawn in `--rule`, deepening to
ink on hover.

---

## 4. Layout language

**The sheet.** The page is a bound volume opened flat: a
max-width sheet of 1180px centred on a maroon binding ground
(the browser window's margin shows `--maroon` at the outer
edges on ≥1200px, like boards extending past the leaves).
Inside the sheet, a two-column grid: a **margin column** of
196px at the left (folios, worked example, initials, notes —
the computor's territory) and the **table column** taking the
rest. Prose may span both; tables never enter the margin;
margin matter never enters the tables.

**The rule grid.** Every table sits on a baseline of ruled
lines: horizontal hairlines (`--rule`, 1px) every 30px — the
cell line-height (§3) — so a table of n rows is exactly n ×
30px of ruling, and figures sit ON the lines like entries in a
ledger. Vertical rules are forbidden inside tables (the vintage
tables ruled horizontally only); columns are separated by
whitespace and alignment alone. A heavier rule (2px ink) closes
the header row and the table's foot; the double rule (§6.7) is
reserved for final answers and section titles.

**Section choreography.** Sections are tables, numbered in
roman numerals in the order the volume binds them (Table I,
II, III…), each opening with its title and caption, its thumb
tab (§6.11) registered on the fore-edge at the section's own
height. The trajectory arc (§6.3) is drawn on a fixed overlay
spanning the sheet's full height, passing behind the section
headers — the one graphic that crosses the whole book, because
the curve and the tables are one mathematics. Sheets are
separated not by gaps but by a **gathering break**: 64px of
paper carrying a single centred folio mark and the next table's
number.

**Density rules.** Tables are dense (30px rows) and proud of
it; prose is airy (1.55 line-height, 64px section padding).
Never mix the two densities inside one block. A sheet carries
at most one interpolating table (§6.2) — the reader can operate
only one instrument at a time. Whitespace in this theme is not
emptiness: it is the unruled part of the sheet, and it is spent
around final answers (the double-ruled figure gets 48px of
clear paper above and below) and nowhere else.

**The fore-edge.** The right edge of the sheet is a working
edge: thumb tabs (§6.11) protrude 34px from it at their
sections' heights, and the folio rail (§6.14) rides the margin
column. Nothing decorative may live on the fore-edge — it is
the book's finding apparatus.

---

## 5. Full motion system

Motion in a book of tables is the motion of a computor's hand
and eye: rules are drawn, values are typed, a straightedge
slides, a sheet turns. Nothing floats, bounces or glows. Every
effect below is the theme's own translation of a standard
motion term; terms the book cannot honestly translate are
refused, with the refusal stated.

**The shared loop.** All scroll-scrubbed values (the
interpolated row §6.2, the arc draw §6.3, the folio §6.14, the
settle below) read from ONE `requestAnimationFrame` loop,
lerping the current scroll position toward the target at
`--loop-lerp` 0.12 per frame. No element runs its own scroll
listener. The loop idles (skips work) when no scrubbed element
is within 1.5 viewports, and pauses entirely when the tab is
hidden. Every figure the loop produces is computed from the
printed record (§6.10) by the printed rule (§6.12) at the moment
it is displayed — the loop never invents a number.

**Named easings** (the book's five hands):

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-draw` | cubic-bezier(0.65, 0, 0.25, 1) | A rule drawn by a steady hand: slow start, confident middle, exact stop | Rule draws, arc draw, double-rule sweep |
| `--ease-type` | steps, timed per character | A typewriter/comptometer cadence — discrete, never smooth | Typed intermediate values (§6.1, §6.6) |
| `--ease-settle` | cubic-bezier(0.22, 1.15, 0.36, 1) | A sheet settling onto the desk: 2% overshoot, then rest | Scroll settle, tab press, slip arrival |
| `--ease-strike` | cubic-bezier(0.85, 0, 0.15, 1) | The red pencil coming down: fast, decisive, no hesitation | Corrections (§6.5), strikes in §6.1 |
| `--ease-turn` | cubic-bezier(0.7, 0, 0.2, 1) | A sheet turning from its edge: heavy start, soft landing | Page transitions (§6.8) |

**The motion terms, translated:**

- **Scroll-triggered reveals.** A table entering the reading
  line has its rules drawn (each hairline scales 0→100% over
  400ms `--ease-draw`, staggered 24ms per rule, max 12 rules —
  longer tables draw header and footer rules only) and its
  figures fade from pencil to ink over 300ms — the sheet is
  *inked in*, never slid or bounced into view.
- **Scroll-driven / scrubbed animation.** The theme's core:
  the interpolated row (§6.2) and the arc (§6.3), both driven
  by the shared loop from the same scroll fraction, so the row
  the reader is between and the point on the curve are always
  the same argument. Scrubbing is the reading.
- **Parallax.** One layer only, and barely: the trajectory arc
  overlay (§6.3) translates at 0.96× the scroll rate against
  the sheets, so the curve drifts 4% against the book it
  annotates — the feel of a plate laid over the pages. No other
  parallax exists; tables do not float over each other.
- **Pinned sections.** One pin per page maximum: the
  interpolating table (§6.2) pins for its bracketing scroll
  range (the two printed rows it interpolates between), because
  the reader must hold the instrument still to operate it. The
  pin releases with the table's own footer rule drawn.
- **Smooth scrolling & settle.** Native scroll, smoothed by
  the loop's lerp for all derived values; when scrolling stops,
  derived figures settle over 180ms `--ease-settle` — the ruled
  settle — landing on the exact interpolated value, never a
  rounded neighbour.
- **Progress indicator.** The margin folio (§6.14): the
  interpolated row position itself ("ROW 250.0 · t = 0.500").
  Progress in this book is a position inside a table, not a
  bar. A percentage bar anywhere is a §9 failure.
- **Staggered & masked reveals.** Stagger exists only in the
  rule draw (24ms per rule) and the computed headline's typed
  column (§6.1). Masked reveals are refused: a mask hides
  figures, and figures are never hidden (§1 law) — reveals here
  *draw* or *ink in*, they do not uncover.
- **Kinetic typography.** Refused for prose. The only moving
  type is figures being typed by the computation (§6.1, §6.6)
  — numerals arriving at comptometer cadence because they are
  being produced, not performed.
- **Marquee.** Refused. Nothing in a bound volume parades.
  (The errata sheet, §6.17, is a list, read at the reader's
  pace.)
- **Counters.** Every counter is an interpolation (§6.2) or a
  computation (§6.1): figures count because the underlying
  argument moves, and they stop at exact values with full
  decimals — a counter that eases to a round number is a §9
  failure. There are no decorative stat counters.
- **SVG line-draw.** The trajectory arc (§6.3), the double rule
  (§6.7), the red strike (§6.5) and the pencil checks of the
  form's receipt (§6.15) — drawn paths, all of them *records of
  a hand having passed*, none of them ornament.
- **Image scale-in-frame.** Plate images (§6.9) scale 1.06→1
  inside their foxed frames over 700ms `--ease-draw` as they
  cross the reading line — a plate being laid flat, not a zoom.
- **Hover / magnetic / tilt micro-interactions.** Hover is the
  straightedge (§6.4) — a tool sliding under a row. Magnetic
  pull and tilt are refused: paper does not lean toward the
  reader's hand. Clicks land with the tab-press (§6.11) or the
  strike (§6.5), 1–2px of `--ease-settle`, nothing more.
- **Custom cursor.** Refused, as everywhere in this library:
  the system cursor, unchanged. The straightedge is the theme's
  pointer-companion and it belongs to rows, not to the pointer.
- **Skeleton loading.** The in-press skeleton (§6.16): blank
  ruled sheets with a printed "IN PRESS" note — the book admits
  it is not ready rather than shimmering.
- **Page transitions.** The thumb-tab sheet turn (§6.8): 500ms
  `--ease-turn`, the sheet turning from its indexed edge.
- **Reduced motion.** A real variant per element (§6): tables
  print complete with final values, the interpolated row prints
  as a static worked line at the table's mid-argument, the arc
  prints fully drawn with its apogee at the mid-row, no typing,
  no drawing, no pins. The book is complete on paper; motion is
  its performance, never its content.

**Master timing table.** Rule draw 400ms · figure ink-in 300ms
· typed character 24ms (columns cap at 1.6s total, §6.1) ·
strike 180ms · recompute typing 24ms/char · straightedge slide
160ms · tab press 120ms · sheet turn 500ms · plate settle
700ms · settle 180ms · worked-example cycle ≈20s (line every
900ms) · watchdog deadlines: loop 3000ms, typing 2000ms, turn
1200ms, skeleton 1500ms (§6.16). No animation on the page runs
longer than 2s except the worked example's slow cycle and the
arc's scroll-scrubbed draw, both of which are content, not
transition.

---

## 6. Signature elements

### 6.1 The computed headline

- **What & why.** The hero's key figure is not written, it is
  *derived* on screen. Beneath the Spectral headline ("Range at
  250 metres per second, computed from Table VII"), a column of
  intermediate values types down in Plex Mono at comptometer
  cadence: the two bracketing rows (240 → 5,873.56; 260 →
  6,893.28), their difference (1,019.72), the half-difference
  for t = 0.500 (509.86), the linear sum (6,383.42) — then two
  corrections strike in red: the second-difference correction
  −10.20 (§6.12's rule), recomputed beside itself, initialled
  "E.M." — and the final figure **6,373.22 m** arrives and is
  double-underlined by the animated double rule (§6.7). It
  belongs because it performs the page's thesis in its first
  seconds: this site's numbers have workings, and the workings
  are shown.
- **Structure.** A DOM computation block in the hero sheet: the
  headline (Spectral, its numeral re-set in Plex Mono per §3),
  then a ruled mini-table (the computation column) whose lines
  are real `<div>` rows on the 30px rule grid — label left
  ("R(240) from Table VII"), figure right-aligned to the
  decimal. Correction lines are struck with an SVG line
  (§6.5's strike) and carry the recomputed value in red mono
  plus initials in the margin column. The final line is heavier
  (Plex Mono 500) and carries the double-rule SVG beneath. All
  lines exist in the DOM at their final values from first
  paint; the typing is a JS-armed reveal over finished text.
- **Motion spec.** Trigger: load, once, when the hero is first
  painted (not on scroll — the welcome is computed on arrival).
  Lines type at 24ms/character (`--ease-type`), line gap
  120ms; the two strikes land at 180ms `--ease-strike` each,
  260ms apart; the recomputed value types at 24ms/char; the
  double rule sweeps 500ms `--ease-draw`. Total budget 3.4s
  worst case; a "skip" is implicit — any scroll past 40% of
  the hero snaps the block to its finished state. The whole
  sequence runs once per session; a return visit shows the
  finished computation (sessionStorage flag) with only the
  double rule re-drawn.
- **States.** Rest (finished computation, all lines printed,
  final figure double-ruled) / computing (lines typing in
  sequence) / struck (corrections applied, red visible) /
  settled (post-sequence; the block is thereafter a static
  printed record). No hover state — a computation is not a
  button; its one interactive descendant is the "see the rule"
  link to §6.12.
- **Content merge.** The headline figure IS the hero's
  content — the product's headline performance number,
  computed from the site's own master table. Remove Table VII
  and the hero cannot be written; the element cannot be pasted
  onto a site whose numbers have no table behind them.
- **Failure fallback.** Watchdog at 2000ms: if the typing
  sequence has not completed (blocked script, starved frames),
  all lines snap to printed and the double rule renders
  complete. No-JS: the block ships finished — full computation
  printed, corrections struck in static red, final figure
  double-ruled. The visitor loses the performance, never the
  proof.
- **Reduced-motion variant.** The computation prints complete
  on arrival: every line present, strikes drawn, final figure
  double-ruled. Nothing types, nothing strikes.
- **Performance budget & mobile variant.** DOM text only; the
  typing is a class-toggle per line (no layout thrash — lines
  are pre-sized on the rule grid). Budget ≤0.2ms/frame during
  the sequence. Mobile (<768px): the computation column takes
  the full sheet width, the margin initials move inline after
  the recomputed value, typing cadence unchanged.
- **Choreography timeline (v2).** t=0 first paint (finished
  computation printed, double rule drawn) → JS arms → lines
  reset to blank-but-sized and type in sequence: row lines
  ≈t=200–900ms → difference ≈t=1000ms → half-difference
  ≈t=1250ms → linear sum ≈t=1500ms → strike 1 lands t=1760ms
  → recompute types to ≈t=2100ms → strike 2 / initials
  ≈t=2360ms → final figure inks in 300ms → double rule sweeps
  t≈2700–3200ms → settled. Watchdog deadline t=2000ms snaps
  any unfinished tail to print (the strikes and final figure
  are never the part left undone — the watchdog completes
  from the *end* of the sequence backwards).
- **State matrix (v2).** *Rest:* finished record. *Hover:*
  none (block is not interactive). *Focus:* the "see the rule"
  link takes a 2px ink outline, offset 2px; focusing it does
  not restart the computation. *Active:* n/a. *Scrolled-past:*
  if the visitor scrolls past mid-sequence, the block snaps
  finished — nobody returns to a half-typed welcome.
  *Disabled:* n/a. *Touch:* identical; no hover dependency
  anywhere in the sequence.
- **Breakpoints (v2).** ≥1200px: computation column 520px in
  the table column, initials in the margin. 768–1199px:
  column 100% of table column, initials in margin still.
  <768px: single column, initials inline, headline figure
  wraps beneath the headline text (never shrinks below
  2.441rem — a computed figure does not go small).
- **Edge cases & failure modes (v2).** *Slow network:* the
  block is HTML text — it prints before fonts arrive; Plex
  Mono fallback (ui-monospace) keeps columns aligned because
  the fallback is also tabular. *Long figures:* the column is
  sized for 10 characters; a wider figure (7+ integer digits)
  drops the block to 14px mono rather than wrapping — a
  wrapped figure is a broken column. *Revisit:* session flag
  prevents re-typing; the finished computation is the page's
  permanent hero. *Scroll-up return:* static; the book does
  not recompute for an audience of one twice.
- **Accessibility spec (v2).** The computation is a `<table>`
  (or role=table) with a caption naming it a worked
  computation; struck values use `<del>` with the recomputed
  value in an adjacent cell, so AT reads the correction as a
  correction. The typing animation is `aria-hidden` in
  progress; a visually-hidden static copy carries the finished
  computation from first paint, swapped at settle. Contrast:
  ink 11.9:1, red 5.0:1 (§2). No focusable elements inside
  except the rule link.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--red`,
  `--pencil`, `--rule`, `--ease-type`, `--ease-strike`,
  `--ease-draw`, `--dur-type-char` (24ms), `--watchdog-type`
  (2000ms).

### 6.2 Interpolating table values

- **What & why.** The theme's instrument. A printed table —
  in the reference build, Table VII itself (§6.10) — carries
  between its two central printed rows a live **interpolated
  row**: as the visitor scrolls through the table's pinned
  range, the row's argument moves continuously between the
  bracketing rows (240 → 260) and every figure in the row is
  computed by real linear interpolation between the printed
  values, with the second-difference correction applied to the
  curved columns (range, apogee) exactly as §6.12's rule
  prescribes, and none to the linear column (time), whose
  first differences are constant. At t = 0.500 the row reads
  v₀ 250.0 · R 6,373.22 · H 1,593.31 · T 36.05 — the same
  figures the hero computed (§6.1) and the arc prints (§6.3),
  because all three are the same mathematics. It belongs
  because it makes the reader operate the table's own method
  by reading: scrolling *is* interpolating.
- **Structure.** A real `<table>` on the 30px rule grid. The
  interpolated row is a `<tr class="interp">` inserted between
  the bracketing printed rows, styled as a ruled slip: heavier
  weight figures (Plex Mono 500), a hairline box rule, and a
  small "INTERPOLATED" marker in the margin column with the
  current t value. The table pins (`position: sticky`) inside
  a scroll range of 160vh mapped linearly to the bracket
  interval. All computation is done in JS from the printed
  rows' `data-` values, which duplicate the printed figures
  exactly — the DOM text is the source of truth, the data
  attributes its machine copy, and a build check (§10)
  verifies they agree.
- **Motion spec.** Trigger: scroll, scrubbed, via the shared
  rAF loop (lerp 0.12). Scroll fraction across the pinned
  range maps to t ∈ [0, 1] across the bracket; figures update
  every frame the lerped position moves, formatted to the
  column's declared decimals (§3). The second-difference
  correction applies the term −t(1−t)/2 × δ², evaluated
  live per frame — δ² itself is a constant per bracket,
  computed once from the three consecutive printed rows
  straddling the bracket and recorded in the build's audit
  (§10), so the per-frame work is one multiplication. At the bracket ends the
  interpolated row lands exactly on the printed row's values
  (t=0 and t=1 are identities, verified in §10) and the slip
  styling relaxes to print. Settle: 180ms `--ease-settle`
  when scrolling stops.
- **States.** Rest (at a printed row — slip reads as print) /
  interpolating (t strictly between, slip styling full,
  marker showing t to 3 decimals) / scrolled-past (table
  unpinned, row frozen at the bracket's far row value) /
  corrected (if §6.5 has struck a figure in this table, the
  interpolation derives from the corrected value and the row
  marker adds the corrector's initials).
- **Content merge.** The interpolated row carries the site's
  real data at arguments the printed table does not reach —
  it is how a visitor asks the table a question it did not
  print. It is the opposite of decoration: remove it and the
  table answers only six questions; with it, the table
  answers the whole interval.
- **Failure fallback.** Watchdog at 3000ms on the shared loop:
  if the loop has not advanced, the pin releases and the
  interpolated row prints statically at the bracket midpoint
  (t = 0.500, values 250.0 · 6,373.22 · 1,593.31 · 36.05,
  marked "INTERPOLATED — MIDPOINT PRINTED"). No-JS: the same
  static midpoint row ships in the DOM; JS replaces its
  values live. The table is complete and honest either way.
- **Reduced-motion variant.** No pin, no scrub: the static
  midpoint interpolated row prints between the bracketing
  rows, with its t and the rule reference in the margin. The
  method is still demonstrated; the hand does not move.
- **Performance budget & mobile variant.** One sticky table,
  one row's text updated per frame — text writes only when a
  displayed figure actually changes (figures are rounded to
  column decimals before comparison, so most frames write
  nothing). Budget ≤0.3ms/frame. Mobile (<768px): the pin
  range shortens to 100vh, the table scrolls horizontally
  within its sheet if columns overflow (figures never shrink
  below 13px), the t marker moves above the row.
- **Choreography timeline (v2).** Table header crosses the
  reading line → rules draw (400ms) → pin engages as the
  bracket rows centre → t sweeps 0→1 across 160vh of scroll:
  at t=0.25 the row reads 245.0 · R 6,120.84 (linear
  6,128.49, second-difference correction −7.65) → t=0.500:
  the hero's figures (250.0 · 6,373.22) → t=0.75: 255.0 ·
  R 6,630.70 (linear 6,638.35, correction −7.65) → t=1:
  lands on the printed 260 row,
  slip styling relaxes → pin releases as the table's footer
  rule draws. Scrolling back up runs the same values in
  reverse — interpolation has no direction.
- **State matrix (v2).** *Rest:* as above. *Hover:* rows
  take the straightedge (§6.4); the interpolated row's hover
  additionally prints its full derivation in the margin
  ("(5,873.56 + 6,893.28)/2 − 10.20"). *Focus:* the table is
  focusable as a region; keyboard scroll drives the same
  scrub. *Active:* n/a. *Scrolled-past:* frozen at far row.
  *Disabled:* n/a. *Touch:* scrub is scroll — identical;
  no hover derivation, so the derivation also prints when
  the row is tapped.
- **Breakpoints (v2).** ≥1200px: full table in the table
  column, marker in margin. 768–1199px: margin marker moves
  to a line above the table. <768px: horizontal scroll
  within sheet, pin range 100vh, t readout fixed to the
  sheet's top edge while pinned.
- **Edge cases & failure modes (v2).** *Fast scroll:* the
  lerp caps the row's travel; values remain exact for the
  displayed t (the row never shows a value for a t it is
  not at). *Jump scroll (anchor link into the table):* the
  row snaps to the landed t within one frame — no sweep
  through intermediate values pretending to be read.
  *Corrected bracket (§6.5):* interpolation re-derives from
  the corrected figure and the marker carries the initials;
  the audit (§10) re-runs. *Very long tables:* only one
  bracket is live per table; other brackets print static
  midpoint rows.
- **Accessibility spec (v2).** The interpolated row's values
  are NOT live regions (a scrubbing figure must not spam
  AT); instead the row carries an `aria-label` updated on
  settle only: "Interpolated at 250.0: range 6,373.22
  metres." The static midpoint row is the no-JS/reduced
  content and is fully readable. Column headers are `<th>`
  with units; the t marker is text, not colour. Touch
  targets: n/a (the table is not a control), links within
  captions ≥40px.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`,
  `--ink`, `--rule`, `--pencil`, `--ease-settle`,
  `--loop-lerp` (0.12), `--dur-settle` (180ms),
  `--watchdog-loop` (3000ms).

### 6.3 Trajectory arc with live apogee label

- **What & why.** One SVG trajectory arc spans the sheet
  above the section headers for the whole page — the curve
  of Table VII's own trajectory, drawn as a plate laid over
  the book. At its apex sits the apogee label, and the label
  is live: it prints the apogee figure the interpolating
  table (§6.2) is currently producing (1,593.31 m at the
  midpoint), updating as the reader scrolls the table. It
  belongs because it keeps the book's two forms of the same
  mathematics — curve and column — honest against each
  other, visibly, at all times.
- **Structure.** A fixed-position SVG overlay the height of
  the document's sheet column, `pointer-events: none`,
  `aria-hidden` (its data lives in §6.2's row, accessibly).
  The path is a true parabola segment computed from the
  record: apex at the bracket midpoint's apogee, scaled so
  the curve's rise spans the headers' band. The label is an
  HTML element (not SVG text) pinned to the apex point:
  "APOGEE 1,593.31 m — FROM TABLE VII, INTERPOLATED" in
  12px mono, on a paper-bright slip with a hairline rule.
  Draw progress is the path's `stroke-dashoffset`, driven
  by the shared loop from the same scroll fraction as §6.2.
- **Motion spec.** Trigger: scroll, scrubbed. The arc draws
  0→100% across the scroll range of the interpolating table
  (the curve is complete when the table has been operated
  through its bracket) under `--ease-draw`'s character via
  the lerp. The apex label's figure updates on the same
  frames as §6.2's row (shared computation, one source). The
  overlay drifts at 0.96× scroll (§5's single parallax) —
  applied to the overlay's translate, never to the label's
  figure. After the table's range, the completed arc remains
  drawn for the rest of the page at 60% ink weight — a plate
  already consulted.
- **States.** Rest (before the table: arc undrawn, label
  prints the FIRST printed row's apogee — 1,019.72 m at
  v₀ 200 — a true figure, never a placeholder) /
  drawing (scrubbed, label live) / complete (past the
  table: full curve at 60%, label holds the last
  interpolated apogee) / corrected (§6.5 strike in the
  table re-derives the label within one frame, label slip
  gains the initials).
- **Content merge.** The arc is the site's data drawn
  instead of tabulated — for an aerospace client it is the
  product's trajectory over its own specification tables.
  Its label is a figure with provenance, not a decorative
  callout; remove the table and the arc has nothing true
  to say, so it is not built.
- **Failure fallback.** If the shared loop's watchdog
  (3000ms) fires, the arc renders fully drawn at 60% and the
  label prints the midpoint apogee 1,593.31 m statically.
  No-JS: the arc ships fully drawn in the DOM (dasharray
  unset), label static at the midpoint figure, marked
  "INTERPOLATED". The plate is printed; the drawing is the
  enhancement.
- **Reduced-motion variant.** Arc printed fully drawn,
  label static at the midpoint apogee with its provenance
  line. No drift, no draw.
- **Performance budget & mobile variant.** One path's
  dashoffset + one label's transform per frame; the path is
  pre-measured once (`getTotalLength` cached). Budget
  ≤0.2ms/frame. Mobile (<768px): the arc spans only the
  hero and the interpolating table's sheet (a full-page
  plate on a narrow sheet crowds the ruling); beyond that
  range it does not render, and the label lives at the
  table's own apex line instead.
- **Choreography timeline (v2).** Page top: arc absent
  (0%), label shows the first row's apogee → table range
  begins: draw starts, label switches to live interpolation
  → t=0.500: label reads 1,593.31 m, arc half-drawn, apex
  point reached → t=1: draw completes → rest of page: arc
  holds at 60%, label holds last figure → footer: the arc's
  endpoint lands exactly at the colophon's rule (§6.17) —
  the curve terminates in the binding.
- **State matrix (v2).** *Rest / drawing / complete /
  corrected:* as above. *Hover:* none — the overlay takes
  no pointer events, ever. *Focus:* none (aria-hidden;
  its content is §6.2's). *Active:* n/a. *Scrolled-past:*
  complete state. *Disabled:* n/a. *Touch:* identical —
  scroll is the only input.
- **Breakpoints (v2).** ≥1200px: full-sheet span, label at
  apex with slip. 768–1199px: span narrows to the table
  column, label slip shrinks to figure + "TABLE VII".
  <768px: hero + table range only (see budget), label
  inline at the table.
- **Edge cases & failure modes (v2).** *Label collision:*
  the apex band is reserved in §4's choreography — headers
  never enter the arc's top 90px; if a build's header would,
  the arc's scale compresses (the figure never moves to
  accommodate — the curve does). *Resize:* path recomputed
  from the record on resize (debounced 200ms), draw
  fraction preserved. *Print:* the arc prints fully drawn
  — a printed book shows the whole curve.
- **Accessibility spec (v2).** Entirely `aria-hidden` as
  decoration-with-data: every figure it shows is available
  accessibly in §6.2's row and §6.10's table. It never
  carries unique content (the pencil rule's graphic twin).
  Contrast of the label slip: ink on paper-bright 12.6:1.
- **Tokens consumed (v2).** `--ink`, `--paper-bright`,
  `--rule`, `--red` (initials only, when corrected),
  `--ease-draw`, `--loop-lerp` (0.12), `--watchdog-loop`
  (3000ms).

---

### 6.4 Straightedge row hover

- **What & why.** Hovering a table row slides a brass
  straightedge under it — a 2px `--brass` rule with a 1px ink
  edge, the width of the table — and the row's figures sharpen
  (Plex Mono 400 → 500 weight, ink at full strength). It is how
  a computor actually reads a table: the eye is kept on the
  line by a tool laid against it. It belongs because the theme's
  hover is an instrument, not a glow — the only hover in the
  library that is a physical object from the theme's own desk.
- **Structure.** One straightedge element per table (not per
  row): an absolutely positioned div inside the table's
  relative wrapper, translated on Y to the hovered row's rule
  line. Rows are `<tr>` with pointer events; the edge tracks
  `offsetTop` of the current row. Figure sharpening is a class
  on the row. The edge sits BELOW the figures' baseline,
  riding the row's own rule line — it underlines the row the
  way the physical tool does.
- **Motion spec.** Trigger: pointerenter on a row. Slide:
  transform translateY over 160ms `--ease-settle` (the small
  overshoot reads as the tool settling against the rule).
  Moving between adjacent rows is one continuous slide, never
  a fade out/in. Sharpening is instant with the slide's start.
  On leave, the edge holds its last row for 300ms, then fades
  to 0 over 200ms — a tool put down, not snatched away.
- **States.** Rest (no edge, or edge faded) / laid (edge under
  the hovered row, figures sharpened) / travelling (mid-slide
  between rows) / keyboard (focus within the table lays the
  edge under the focused row — keyboard readers get the tool
  too). On the interpolated row (§6.2), the laid state also
  summons the margin derivation.
- **Content merge.** The straightedge exists only on tables
  and only does the table's work: keeping a reader's place in
  columns of figures. It cannot appear on prose, cards or
  navigation — a build that edges a paragraph has misunderstood
  the tool.
- **Failure fallback.** If JS never runs, there is no edge and
  nothing is missing: rows are fully legible print. If the
  pointer is coarse (touch), the edge never appears (see
  matrix) and rows rely on their ruling alone, as print does.
- **Reduced-motion variant.** The edge appears under the row
  without sliding (instant placement, no overshoot); fade-out
  becomes instant removal. The tool is present; the hand does
  not travel.
- **Performance budget & mobile variant.** One transform per
  pointer move, throttled to the shared loop's frames; no
  layout reads after the first (row offsets cached on resize).
  Budget ≤0.1ms/frame while hovering. Mobile (<768px): no
  straightedge (no hover); a tapped row holds the sharpened
  weight for 1.2s as the touch equivalent, with no edge drawn.
- **Choreography timeline (v2).** Pointer enters row →
  t=0 sharpen + slide starts → t=160ms edge settled against
  the rule → row-to-row: continuous 160ms slides chained →
  pointer leaves table → t=300ms hold expires → 200ms fade →
  rest. Total gesture vocabulary: one slide, one fade.
- **State matrix (v2).** *Rest:* absent. *Hover:* laid.
  *Focus:* laid under the focused row (focus and hover share
  the tool; last input wins). *Active:* pressing a figure in
  the row hands over to §6.5's correction; the edge stays
  laid beneath the correction as it lands. *Scrolled-past:*
  fades with its table. *Disabled:* n/a. *Touch:* tap =
  sharpen only, 1.2s, no edge.
- **Breakpoints (v2).** ≥1200px and 768–1199px: identical
  (the tool is the table's width, whatever that is).
  <768px: touch behaviour only; on a narrow table scrolled
  horizontally, the edge — if a fine pointer exists — spans
  the table's full scroll width, not the viewport.
- **Edge cases & failure modes (v2).** *Fast pointer sweeps:*
  the slide lerps toward the latest row; intermediate rows
  are passed over without sharpening flicker (sharpen applies
  only to the settled row). *Row height changes (a correction
  wraps):* offsets re-measured on the correction event.
  *Sticky header overlap:* the edge's z-order is below the
  table's own header rule — it never strikes through a header.
- **Accessibility spec (v2).** Purely presentational for AT:
  the edge is `aria-hidden`; the sharpening duplicates no
  information. Keyboard focus lays the edge as a visual aid
  alongside the real focus ring (2px ink outline on the
  focused cell/row, offset −2px so it reads against the
  ruling). The brass at ~3.9:1 is a graphic with a 1px ink
  edge — it is never the sole indicator of anything.
- **Tokens consumed (v2).** `--brass`, `--ink`, `--rule`,
  `--ease-settle`, `--dur-edge` (160ms).

### 6.5 Click-to-correct

- **What & why.** Clicking a figure in any table strikes it
  through in correction red and types the recomputed value
  beside it in red mono; the correction is initialled in the
  margin. This is the book's living culture made interactive:
  printed tables were corrected by hand for decades, and the
  correction — visible, initialled, unreversed — is what makes
  the next reader trust the book. In a real build the
  "recomputed value" is genuine: the figure is re-derived from
  the record (§6.10) by the rule (§6.12) at click time — if the
  printed figure was right, the correction recomputes to the
  same value and the strike does not land (the computor checks
  first; see states). The demo correction in the reference
  build strikes the one planted error: Table VII's apogee at
  v₀ 280 printed as 1,988.65, recomputed to the true 1,998.65.
- **Structure.** Figures are `<button class="fig">` inside
  their cells (a table of buttons in print clothing — tabular
  mono, no chrome). The strike is an inline SVG line across
  the figure, drawn by dashoffset. The recomputed value is a
  `<span class="recomp">` inserted after the figure in red
  mono, with the original kept struck but legible (opacity
  0.55, never display:none — the law). Initials ("E.M.") are
  placed in the margin column aligned to the row, in red.
  Corrections persist for the session (and in a real build,
  are submitted to the errata sheet §6.17 — a correction the
  visitor makes is a correction the book records).
- **Motion spec.** Trigger: click / Enter / Space on a
  figure. Sequence: the figure is "checked" — a pencil tick
  prints in the margin (120ms) while the recomputation runs
  (a genuine recompute, ~180ms of visible pause — the hand is
  working) → if the value differs: strike draws 180ms
  `--ease-strike` → recomputed value types at 24ms/char in
  red → initials print in the margin (fade 200ms). If the
  value agrees: no strike; the pencil tick stays and a margin
  note prints "checked — agrees" in pencil. Total ≤900ms.
- **States.** Rest (printed figure) / checking (tick printed,
  recompute pending) / agrees (tick + pencil note; figure
  unchanged) / corrected (struck, recomputed value beside,
  initialled) / locked (a corrected figure cannot be
  re-corrected; clicking it selects the recomputed value's
  derivation note in the margin instead).
- **Content merge.** Corrections are the content's
  maintenance performed in public — for a data publisher this
  is the errata workflow itself, not a demo of one. Every
  derived element that consumed the struck figure (the
  interpolated row §6.2 if the figure is in its bracket, the
  arc label §6.3, the form §6.15) re-derives from the
  corrected value within one frame and carries the initials —
  the book stays consistent under correction, or the
  correction is theatre.
- **Failure fallback.** No-JS: the planted correction ships
  pre-applied in the static errata sense — the figure prints
  struck with its recomputed value beside it, exactly as a
  hand-corrected copy would look; the interactivity is the
  performance of a correction that, on paper, has already
  happened. If the recompute fails (record missing), the
  strike never lands and a pencil margin note prints
  "cannot recompute — see the errata sheet": the book admits
  the failure in its own voice rather than striking blindly.
- **Reduced-motion variant.** Strike and recomputed value
  appear without drawing or typing (instant state change
  after the 180ms checking pause, which is content, not
  motion). The pencil tick prints instantly.
- **Performance budget & mobile variant.** One figure's DOM
  per correction; the re-derivation cascade touches at most
  §6.2's row and §6.3's label. Budget ≤0.5ms per correction
  event. Mobile (<768px): figures' tap targets are the full
  cell (40px min height on the 30px grid — correction-enabled
  tables on mobile use a 40px rule pitch, declared in the
  table's caption); initials move inline after the recomputed
  value when no margin column exists.
- **Choreography timeline (v2).** t=0 click → pencil tick
  prints (120ms) → checking pause to t≈300ms → branch:
  *agrees* → pencil note prints, done (≈t=500ms);
  *differs* → strike draws t=300–480ms → recomputed value
  types t=480–700ms → initials fade in to t=900ms →
  dependents (§6.2/§6.3) re-derive at t=480ms in the same
  frame as the strike completes.
- **State matrix (v2).** *Rest / checking / agrees /
  corrected / locked:* as above. *Hover:* the straightedge
  (§6.4) lays under the row; the figure itself takes a
  hairline dotted underline in red at 40% — the only hint
  that a figure may be questioned, and it is a question
  mark's worth of emphasis, no more. *Focus:* 2px red
  outline (the correction colour, because focus here means
  "under examination"), offset 2px. *Active:* the checking
  sequence. *Scrolled-past:* corrections persist — scroll
  position is irrelevant to the record. *Disabled:* figures
  in a table declared final (a "closed" table) are not
  buttons; the caption says so. *Touch:* tap = click; the
  dotted hover hint is absent, the caption carries the
  instruction instead ("Touch a figure to have it checked").
- **Breakpoints (v2).** ≥1200px: initials in the margin
  column. 768–1199px: initials in margin still (margin
  narrows to 148px). <768px: initials inline; struck figure
  and recomputed value stack (struck above, recomputed
  below) inside the cell rather than squeezing side by side
  — a correction is never allowed to break the column's
  alignment for other rows.
- **Edge cases & failure modes (v2).** *Double-click /
  repeat clicks during checking:* ignored until the
  sequence resolves (the hand is busy). *Correcting a
  bracket figure while §6.2 is mid-scrub:* the interpolated
  row freezes for the 480ms of the strike, then re-derives
  — the reader never watches a value change under their
  hand without the strike explaining it. *Session restore:*
  corrections re-apply instantly on load (no re-performance)
  with the errata sheet (§6.17) listing them.
- **Accessibility spec (v2).** Figures are real buttons with
  labels ("Check figure 1,988.65, apogee at 280"). A
  correction is announced once via a polite live region:
  "Corrected: apogee at 280 is 1,998.65, initialled E.M."
  The struck original remains readable (it is the record);
  `<del>`/`<ins>` semantics pair the values. Red on paper
  5.0:1 (§2); the strike is a line, not a colour-only
  signal — the recomputed value's presence is the signal.
- **Tokens consumed (v2).** `--red`, `--ink`, `--pencil`,
  `--ease-strike`, `--dur-type-char` (24ms),
  `--dur-strike` (180ms).

### 6.6 Self-recomputing worked example

- **What & why.** In the margin column, a small worked
  example — "EXAMPLE: RANGE AT 250, FROM TABLE VII" — quietly
  re-computes itself on a slow cycle: its lines fade to
  pencil-grey, erase, and re-derive line by line, ending with
  fresh initials each cycle (rotating through the computor
  pool: E.M., J.H., A.R. — the room had more than one hand).
  It is the book's ambient life: the method, demonstrated
  forever, by a tireless junior computor. It belongs because
  a book of tables is a workplace, and the margin is where
  the work shows.
- **Structure.** A margin block on the rule grid, five lines
  of Plex Mono in pencil: the two bracket rows, the
  difference, the half-difference with correction, the final
  line — which alone reprints in INK at the cycle's end (§2's
  pencil rule: pencil shows working, the answer is ink). The
  block is `aria-hidden` as a duplicate (§6.1 carries the
  same computation accessibly) — its value is presence, not
  information. Cycle state is a CSS/JS class sequence on the
  block's lines; the initials element swaps text per cycle.
- **Motion spec.** Trigger: time, ≈20s cycle, only while the
  block is within the viewport (IntersectionObserver) and
  the tab is visible. Beat: lines hold printed 9s → fade to
  pencil-grey ghost over 1.2s → blank 800ms → re-type line
  by line at 24ms/char with 900ms between lines → final line
  inks in (colour pencil→ink, 400ms) → initials print →
  hold. The cycle is deliberately slow and peripheral; it
  must never be the most active thing on the screen.
- **States.** Rest (fully printed, between cycles) / fading
  (ghosting to pencil) / recomputing (lines typing) / inking
  (final line turning to ink, initials printing). The block
  has no hover/focus/active states — it is not interactive,
  and pausing it on hover is refused (the computor does not
  stop because you are watching; that is the point of him).
- **Content merge.** The example works the SAME computation
  as the hero (§6.1) from the SAME table (§6.10) — it is the
  method kept warm in the margin of every page it appears
  on, so a visitor who lands mid-book still watches the
  house method performed. On pages whose master table
  differs, the example works that page's table. It is never
  a generic animation: change the record and the example's
  figures change.
- **Failure fallback.** No-JS or loop failure: the example
  prints complete and static, final line in ink, initialled
  once (E.M.). A static worked example in a margin is what
  real printed books carry — the fallback is the original.
- **Reduced-motion variant.** Static printed example, as
  the fallback. No cycle, ever — this element's entire
  motion is ambient, so reduced motion retires it to print.
- **Performance budget & mobile variant.** One small block;
  timers, not per-frame work (it does not use the shared
  loop). Budget ~0ms/frame. Mobile (<768px): the margin
  column collapses (§4) and the example moves to a ruled
  block beneath its table — and its cycle slows to 30s,
  because on a small screen it is nearer the reading line
  and must be quieter.
- **Choreography timeline (v2).** t=0 printed (ink final
  line, initials E.M.) → t=9s fade begins → t=10.2s ghost →
  t=11s blank → lines re-type t=11–17.5s (5 lines, 900ms
  apart) → final line inks t=17.5–17.9s → initials print
  (J.H.) t=18s → hold to t≈27s → cycle repeats with A.R.
  Initials rotation is seeded by cycle count, so the room's
  hands rotate in a fixed, auditable order.
- **State matrix (v2).** *Rest / fading / recomputing /
  inking:* as above. *Hover / focus / active:* none (not
  interactive, not focusable). *Scrolled-past:* cycle
  suspends off-screen and resumes at the hold beat — the
  computor does not perform for an empty room, and does not
  restart mid-line on return. *Disabled:* n/a. *Touch:*
  identical (no interaction to translate).
- **Breakpoints (v2).** ≥1200px: margin column, 12px mono.
  768–1199px: margin narrows; example keeps 5 lines, label
  shortens to "EXAMPLE — RANGE AT 250". <768px: beneath
  the table, full width, 30s cycle.
- **Edge cases & failure modes (v2).** *Multiple examples
  on one page:* forbidden — one computor per page (§4's
  density rule); a second table's example would race the
  first. *Long computations:* the example is capped at 6
  lines; a method needing more is a §6.12 rules plate, not
  a margin example. *Tab hidden mid-cycle:* timers are
  wall-clock-checked on return; the block settles to the
  printed state rather than resuming mid-ghost.
- **Accessibility spec (v2).** `aria-hidden="true"` in
  full: the computation is available non-ambiently in
  §6.1 and §6.12. Pencil contrast (4.1:1) is licensed
  here precisely because the block carries no unique
  content and its final line prints in ink at 11.9:1
  (§2's pencil rule, enforced by §10's gate).
- **Tokens consumed (v2).** `--pencil`, `--ink`, `--rule`,
  `--ease-type`, `--dur-type-char` (24ms),
  `--cycle-example` (≈20s).

---

### 6.7 Double-rule underline sweep

- **What & why.** The book's highest honour: two rules drawn
  beneath a figure or title — the first full width, the second
  shorter (72%) and offset 5px below, exactly as a computor
  underlines a final answer twice. It is granted to final
  answers (§6.1's computed figure, §6.15's returned slip) and
  to section titles when they lock into the reading line. It
  belongs because emphasis in this world is typographic
  ceremony with a ration: a page may hold at most three
  double rules, and each one means *this is settled*.
- **Structure.** An inline SVG under the honoured element:
  two paths (full-width, 72%-width), stroke ink 2px and
  1.5px, drawn by dashoffset. The SVG is sized to the
  element's text width (measured once, re-measured on
  resize/font-load). For titles, the sweep is armed by an
  IntersectionObserver at the reading line (§4's 55% line).
- **Motion spec.** Trigger: computation settle (§6.1/§6.15)
  or title crossing the reading line. First rule draws over
  380ms `--ease-draw`; a 90ms beat; second rule draws over
  300ms. Once drawn, permanent for the session — an honour
  is not re-performed on every scroll pass. Scrolling back
  up never un-draws.
- **States.** Rest (undrawn — element not yet honoured) /
  drawing (two beats) / honoured (drawn, permanent). Titles
  that never reach the reading line (jump-scroll past them)
  are honoured instantly without the sweep — the honour is
  the state, not the performance.
- **Content merge.** The double rule is the site's way of
  marking which numbers are final — in a data product, the
  certified figure among estimates. Its ration (≤3 per page)
  is a content discipline enforced by §10: if everything is
  final, nothing is.
- **Failure fallback.** No-JS: honoured elements ship with
  the rules drawn (static SVG, dasharray unset). Loop/IO
  failure: titles print honoured; the sweep is the only
  casualty.
- **Reduced-motion variant.** Rules print drawn. No sweep.
- **Performance budget & mobile variant.** Two path
  dashoffsets, once per honoured element per session;
  negligible. Mobile: identical — ceremony does not shrink.
- **Choreography timeline (v2).** Trigger lands → 90ms
  pause (the hand positions) → rule 1 draws 380ms → 90ms
  beat → rule 2 draws 300ms → honoured. Total 860ms, once.
- **State matrix (v2).** *Rest / drawing / honoured:* as
  above. *Hover / focus / active:* none — the rule is not
  interactive and does not respond to the honoured element's
  states. *Scrolled-past:* remains honoured. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** All sizes identical; the second
  rule's 72% is relative to the element's width at every
  breakpoint. On <768px, if the honoured figure wraps to
  two lines, the rules draw under the LAST line only, at
  that line's width — the answer is where the figure ends.
- **Edge cases & failure modes (v2).** *Font swap shifting
  width:* re-measure on `document.fonts.ready`; a rule
  drawn 4px short is re-drawn complete (the honour is
  redrawn, never patched). *More than 3 candidates on a
  page:* the build fails §10 — the element itself never
  arbitrates.
- **Accessibility spec (v2).** Decorative (`aria-hidden`);
  finality is ALSO stated in text where it matters ("final
  value" in §6.1's accessible copy) — the rule is never the
  sole carrier of the "settled" meaning.
- **Tokens consumed (v2).** `--ink`, `--ease-draw`,
  `--dur-rule-1` (380ms), `--dur-rule-2` (300ms).

### 6.8 Thumb-tab page transitions

- **What & why.** Navigation between the volume's sections
  and pages is performed by the thumb tabs (§6.11): the
  destination tab presses in, and the sheet turns from its
  indexed (right) edge — the current sheet rotates a few
  degrees on its binding edge and fades as the destination
  sheet settles beneath it. It belongs because the book's
  finding device is its navigation: you browse the volume
  the way it was bound to be browsed, by its tabs.
- **Structure.** A transition layer over the sheet: on
  navigation, the outgoing sheet is cloned into a
  `.sheet-turn` wrapper (or the incoming sheet is revealed
  beneath — implementation detail, one DOM strategy per
  build, declared in §15), transform-origin at the right
  edge, `rotateY` from 0 to −14deg with a maroon shadow
  gradient deepening across the turn, while the incoming
  sheet scales 0.995→1 with `--ease-settle`. The tabs
  themselves live in §6.11; this element is the turn.
  History is real (pushState / real links) — the turn
  decorates navigation, never replaces it.
- **Motion spec.** Trigger: tab click / nav link activation
  (same-site navigations only). Tab press: 120ms
  `--ease-settle` (§6.11). Turn: 500ms `--ease-turn` —
  rotate and shadow over the first 320ms, incoming settle
  over the last 180ms. Watchdog at 1200ms: if the incoming
  content has not mounted, the turn completes instantly to
  the destination (a slow sheet is shown, not performed).
- **States.** Rest (no turn) / pressing (tab feedback) /
  turning (outgoing sheet in motion) / settling (incoming
  sheet landing) / arrived (rest, destination's tab now
  pressed-state per §6.11). Browser back/forward performs
  the turn in reverse direction (sheet returns from the
  edge) — the book remembers which way it was opened.
- **Content merge.** The turn is the volume's own physics:
  sections reached by tabs turn; pages outside the volume
  (checkout, external links) do NOT turn — they are not
  sheets in this book, and pretending otherwise breaks the
  metaphor exactly where money changes hands.
- **Failure fallback.** No-JS / failed fetch: ordinary
  navigation, full page load, no turn. The links are real
  `<a href>`; the turn is a progressive enhancement layered
  on click interception, removed the moment anything in
  the chain fails.
- **Reduced-motion variant.** No turn: instant swap with a
  120ms crossfade of the sheet grounds only (paper to
  paper), tab state updates. Navigation speed is the
  accessibility feature here.
- **Performance budget & mobile variant.** One transformed
  wrapper; the clone is paint-only (no duplicate media
  loads — media elements are moved, not re-fetched, or the
  turn is skipped on media-heavy sheets). Budget ≤1ms/frame
  during the turn. Mobile (<768px): the turn axis becomes
  the bottom edge (a sheet lifted from below, like turning
  a page upward on a small desk) at 420ms; tabs are a top
  rail (§6.11), so the press and the turn stay connected.
- **Choreography timeline (v2).** t=0 tab press (120ms) →
  t=80ms turn begins (outgoing rotate/shadow, 320ms) →
  t=300ms incoming sheet visible beneath at 0.995 → t=400–
  500ms settle to rest → arrived; focus moves to the
  destination's title at t=500ms (never before the sheet
  lands). Watchdog t=1200ms force-arrives.
- **State matrix (v2).** *Rest / pressing / turning /
  settling / arrived:* as above. *Hover:* tabs only
  (§6.11). *Focus:* keyboard navigation triggers the same
  turn; focus is never left on the outgoing sheet.
  *Active:* n/a. *Scrolled-past:* n/a (page-level).
  *Disabled:* a tab for the current page does not turn.
  *Touch:* tap = click; the turn is identical, axis per
  breakpoint.
- **Breakpoints (v2).** ≥1200px: right-edge turn, tabs on
  the fore-edge. 768–1199px: same, turn angle −10deg (the
  sheet is narrower; less drama). <768px: bottom-edge turn
  420ms, angle-equivalent 8deg lift.
- **Edge cases & failure modes (v2).** *Rapid double
  navigation:* the second press cancels the first turn at
  its current angle and turns directly to the new
  destination — sheets never queue. *Deep link / refresh:*
  no turn on first load; the book opens at the sheet it
  was told to open at. *Print:* transitions do not exist;
  each sheet prints as itself.
- **Accessibility spec (v2).** Focus management is the
  spec: on arrival, focus moves to the destination title
  (tabindex −1), and the navigation is announced by the
  title itself — no live-region narration of the turn.
  The turn is decorative motion over a real navigation;
  with reduced motion or no JS the navigation is complete
  without it. Turn never traps scroll: the destination is
  scrollable from t=0 of the settle.
- **Tokens consumed (v2).** `--maroon`, `--paper`,
  `--ease-turn`, `--ease-settle`, `--dur-turn` (500ms),
  `--watchdog-turn` (1200ms).

### 6.9 Foxed plate frames

- **What & why.** Images — plates — sit inside frames set
  within the binding margins: a paper-deep mount, a hairline
  ink frame rule, corners foxed with the seeded stain (§2),
  and a caption that is not a description but a *computed
  figure*: "PLATE IV — THE ARC AT 250, APOGEE 1,593.31 m."
  Even pictures must justify themselves numerically in a
  book of tables. It belongs because it disciplines imagery
  into the book's evidentiary system: a plate is evidence
  for a figure, captioned by it.
- **Structure.** A `<figure>` with the mount (paper-deep
  padding 18px, ink hairline inset), the image, and a
  `<figcaption>` in Plex Mono 12px: plate number (roman),
  subject, and the figure it evidences — which, where the
  figure is interpolated, is computed live from §6.2's
  current t and carries the marker "INTERPOLATED" (the
  caption re-derives under correction like everything
  else). Foxing is a pseudo-element radial-gradient at two
  seeded corners per plate, fixed by the plate's number
  (seeded, never random per visit).
- **Motion spec.** Trigger: scroll into view. The plate
  settles: image scales 1.06→1 inside the frame over 700ms
  `--ease-draw` (a plate laid flat), the frame rule draws
  400ms, the caption's figure — if live — counts from the
  bracket's near row to the current interpolated value over
  the same 700ms (it is an interpolation, not a count-up:
  it lands on §6.2's exact figure). Once settled, a live
  caption keeps following §6.2 while the table is being
  operated.
- **States.** Rest (unsettled — image at print scale
  already: the 1.06 start is JS-armed only) / settling /
  settled / live (caption following the interpolated row) /
  corrected (caption figure re-derived, initials appended
  to the caption in red 10px).
- **Content merge.** A plate without a figure is refused at
  build (§10): every image on the site must evidence a
  number from the record — a product photograph evidences
  its performance figure, a portrait evidences the sitter's
  table ("the computor of Table VII, 41 years at the desk"
  is a figure of a kind the book accepts). Decorative
  imagery has no frame to sit in.
- **Failure fallback.** No-JS: plate printed settled,
  caption static at the midpoint figure where interpolated
  (marked as such), foxing present (it is CSS). Broken
  image: the mount prints with the caption and a ruled
  empty plate area carrying the plate's number — the book
  shows the plate is missing rather than collapsing the
  layout.
- **Reduced-motion variant.** Plate prints settled; live
  captions print at the midpoint figure and do not follow
  the row. No scale, no draw.
- **Performance budget & mobile variant.** One image +
  transforms; live captions update only when §6.2's
  displayed figure changes. Budget ≤0.1ms/frame. Mobile
  (<768px): mount padding 12px, plates full sheet width,
  caption wraps to two lines (figure on its own line,
  right-aligned — alignment survives wrapping).
- **Choreography timeline (v2).** Plate crosses reading
  line → frame rule draws (400ms) → image settles 1.06→1
  (700ms) → caption figure interpolates to current value
  (700ms, shared timing) → settled; if §6.2 is operated
  later, caption resumes following within one frame.
- **State matrix (v2).** *Rest / settling / settled /
  live / corrected:* as above. *Hover:* the plate lifts
  its mount shadow by 1px over 160ms — the only lift in
  the theme, and it is a shadow, not a tilt. *Focus:* a
  linked plate takes a 2px ink outline on the frame.
  *Active:* n/a. *Scrolled-past:* settled state holds.
  *Disabled:* n/a. *Touch:* no hover lift; settle on
  scroll identical.
- **Breakpoints (v2).** ≥1200px: plates sit in the table
  column at up to 640px, or span both columns for a
  full-sheet plate (max one per sheet). 768–1199px: table
  column only. <768px: full width, padding 12px, foxing
  reduced to one corner (two stains crowd a small plate).
- **Edge cases & failure modes (v2).** *Slow image:* the
  mount and caption print on time; the image fades in
  inside its frame when loaded (the frame is never
  re-sized by the image — aspect ratios are declared in
  the plate's data, as a printer declares a plate's
  dimensions). *Caption figure unavailable (record
  missing):* caption prints the subject only, with a
  pencil note "figure not yet computed" — a plate may be
  uncaptioned honestly, never captioned inventedly.
- **Accessibility spec (v2).** Real `<figure>`/
  `<figcaption>`; alt text describes the image's content
  (the caption is its data, not its description — both
  exist). Live captions are not live regions; their
  settled value is readable on demand. Foxing is CSS,
  invisible to AT, and never overlays the image's
  informative area (corners only, ≤12% of the frame).
- **Tokens consumed (v2).** `--paper-deep`, `--ink`,
  `--rule`, `--red` (initials only), `--ease-draw`,
  `--dur-plate` (700ms).

---

### 6.10 The master table record (Table VII)

- **What & why.** The page's constitution: one declared
  table from which every figure on the site derives. In the
  reference build it is **Table VII — Trajectories at 45°
  elevation, vacuum, g = 9.80665 m/s²**, printed in full
  wherever the site's data is presented, and named in every
  derivation. Its printed rows:

  | v₀ (m/s) | RANGE R (m) | APOGEE H (m) | TIME T (s) |
  |---|---|---|---|
  | 200 | 4,078.86 | 1,019.72 | 28.84 |
  | 220 | 4,935.43 | 1,233.86 | 31.73 |
  | 240 | 5,873.56 | 1,468.39 | 34.61 |
  | 260 | 6,893.28 | 1,723.32 | 37.49 |
  | 280 | 7,994.58 | 1,998.65 | 40.38 |
  | 300 | 9,177.45 | 2,294.36 | 43.26 |

  One cell of the printed record is wrong, deliberately
  preserved from the source printing: the apogee at v₀ 280
  stands as 1,988.65 where the formula gives 1,998.65 — it
  is §6.5's correction waiting to happen, and §10's audit
  whitelists exactly that one cell. Every other row
  recomputes clean from the generating formulae R = v₀²/g,
  H = v₀²/4g, T = v₀√2/g, and the audit fails the build on
  any further disagreement beyond the last printed decimal.
  A real build's record is its own data, audited the same
  way. It belongs because the theme's law — no figure
  without its working — needs a fixed point: this table is
  where every working starts.
- **Structure.** A `<table>` in a dedicated sheet (the
  "Table of the Volume" sheet, reached from every page's
  thumb index), plus a machine-readable twin: the same rows
  as a JSON block in the page (`<script type="application/
  json" id="table-vii">`) from which §6.1/§6.2/§6.3/§6.15
  derive. The printed table and the JSON are generated from
  one source file at build time — they cannot drift, and
  §10's gate diffs them. Decimal ruling (§3): R and H to 2
  decimals, T to 2, v₀ integers; the caption declares it.
- **Motion spec.** The record itself does not perform: its
  rules draw on entry (§5's reveal, 400ms) and its rows take
  the straightedge (§6.4) and corrections (§6.5) — the
  record is acted upon, never animated for its own sake.
  The one exception: a row that a correction has touched
  carries its red recompute permanently (§6.5's locked
  state), so the record visibly ages like a real corrected
  copy.
- **States.** Rest (printed, audited) / corrected (one or
  more rows struck-and-recomputed, initials in margin) /
  cited (when another element is deriving from it, the
  record's caption line shows a pencil note "in use above"
  — a courtesy, implemented as a class from the deriving
  element's observer). No other states: a record does not
  hover, load or empty.
- **Content merge.** This IS the content — the site's data
  in its canonical form. Every other element in §6 is a way
  of reading it. A build whose marketing pages cite figures
  not in its record has two options: extend the record
  (a new table, numbered, audited) or delete the figure.
- **Failure fallback.** The record is static HTML and JSON;
  it has no failure mode short of the page itself failing.
  If the JSON twin fails to parse, deriving elements fall
  back to reading the printed DOM rows (they are identical
  by construction) and log the fault to the errata sheet
  (§6.17) — the book notes its own binding fault.
- **Reduced-motion variant.** Identical (the record does
  not move). Rule draw becomes print.
- **Performance budget & mobile variant.** One table; the
  JSON twin ≤2KB. Mobile (<768px): the table scrolls
  horizontally inside its sheet; the v₀ column sticks at
  the left (the argument must never scroll away from its
  figures).
- **Choreography timeline (v2).** Sheet enters → rules
  draw 400ms → rows ink in → if a session correction
  exists, it re-applies instantly at print (no
  re-performance, §6.5) → rest. When cited, the pencil
  note prints within 200ms of the deriving element's
  activation and erases when the visitor leaves that
  element's sheet.
- **State matrix (v2).** *Rest / corrected / cited:* as
  above. *Hover:* via §6.4. *Focus:* rows focusable only
  through their figures (§6.5's buttons). *Active:* n/a.
  *Scrolled-past:* unchanged — the record does not react
  to being left. *Disabled:* n/a. *Touch:* horizontal
  scroll with sticky argument column.
- **Breakpoints (v2).** ≥1200px: full table in the table
  column, caption above, audit line below ("Checked
  against the generating formulae, [date], E.M.").
  768–1199px: same, margin notes inline. <768px:
  horizontal scroll, sticky v₀, caption wraps.
- **Edge cases & failure modes (v2).** *Record grows:*
  tables beyond 40 rows paginate by gathering (40 rows per
  sheet, folios §6.14) — a record is never truncated to
  fit a design. *Two records on one site:* permitted —
  numbered tables (VII, VIII…), each derivation names its
  table; two records may never share a page's hero.
  *Corrected record re-published:* the errata sheet
  (§6.17) carries the correction forward; the printed row
  updates and the strike history moves to the errata —
  the book's memory is the errata sheet, not the row.
- **Accessibility spec (v2).** A model table: `<caption>`
  with quantities, units, limits and decimal ruling;
  `<th scope="col">` headers; the audit line is text.
  The JSON twin is `aria-hidden` machinery. Figures are
  reachable as §6.5 buttons with full labels.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--rule`,
  `--red` (corrections only), `--pencil` (cited note).

### 6.11 Thumb-index navigation rail

- **What & why.** The volume's sections are found by
  thumb-index tabs on the sheet's fore-edge: maroon tabs,
  one per table/section, protruding 34px, labelled in
  rotated Spectral caps ("TABLE VII", "RULES", "PLATES",
  "ERRATA"), each registered at the height of its own
  section so the edge reads as a map of the book. The
  current section's tab sits pressed (translated 4px into
  the sheet, shadowed as a thumb would press it). It
  belongs because a bound volume's navigation is physical
  and positional: you find Table VII by where its tab is,
  not by remembering a menu.
- **Structure.** A `<nav>` fixed to the sheet's right edge
  (inside the sheet container, absolute on desktop), tabs
  as real `<a>` links in a vertical stack ordered as the
  sections are bound. Tab vertical positions are registered
  to their sections (a tab's top aligns with its section's
  title within the rail's compressed scale — the rail is a
  minimap: positions are proportional to document position,
  recomputed on resize). The current tab is marked by
  scrollspy from the shared loop's position (no separate
  listener).
- **Motion spec.** Press (click/activation): tab translates
  4px in over 120ms `--ease-settle`, then §6.8's turn runs.
  Scrollspy changes: the pressed state hands over with a
  160ms crossfade of the inset shadow — tabs do not slide
  along the edge (their positions are the book's geography;
  only the pressing moves). Hover: tab protrudes a further
  3px over 120ms — a thumb testing the edge.
- **States.** Rest (flush) / hovered (protruded 3px) /
  pressed-current (inset 4px, `aria-current`) / pressing
  (during §6.8's turn) / focus (2px paper outline on the
  maroon, offset −4px — the only outline in the theme drawn
  in paper, because the ground is maroon).
- **Content merge.** The rail is the table of contents with
  positions: its labels are the site's real sections, its
  geometry is the page's real length. A section added to
  the page adds a tab at its true proportional place — the
  nav cannot lie about the book's shape.
- **Failure fallback.** No-JS: tabs are ordinary links in a
  list; scrollspy never runs, no tab is pressed, navigation
  is complete. The rail degrades to a contents list at the
  sheet's head in the no-JS print (CSS reorders it into
  flow) — a book without a working thumb index still has a
  contents page.
- **Reduced-motion variant.** Press and hover translations
  become instant state changes; scrollspy still marks the
  current tab (state, not motion).
- **Performance budget & mobile variant.** ≤8 tabs; the
  scrollspy reads the shared loop's position. Budget
  ~0ms/frame. Mobile (<768px): the fore-edge rail becomes
  a horizontal tab strip pinned to the sheet's top —
  labels unrotated, horizontally scrollable, current tab
  pressed downward 3px; §6.8's turn axis follows (§6.8's
  bottom-edge turn).
- **Choreography timeline (v2).** Page load: tabs print
  flush, current tab presses in at t=300ms (after first
  paint — the book is opened, then the thumb finds its
  place) → scroll: pressed state hands over as sections
  cross the reading line → click: press 120ms → turn
  (§6.8) → arrival: destination tab is the pressed one.
- **State matrix (v2).** *Rest / hover / focus / active
  (pressing) / current:* as above. *Scrolled-past:* n/a
  (the rail is fixed; it IS the scrolled-past indicator).
  *Disabled:* the current page's tab in a page-level nav
  context does not turn (§6.8) but still anchors to its
  section. *Touch:* tap = press + turn; no hover protrude.
- **Breakpoints (v2).** ≥1200px: fore-edge rail, tabs
  34px protrusion, rotated labels. 768–1199px: rail
  narrows (protrusion 26px, labels shorten to numerals
  "VII", "R.", "PL." with full names in `aria-label`).
  <768px: top strip, unrotated, scrollable.
- **Edge cases & failure modes (v2).** *Many sections:*
  past 8 tabs, the rail groups by gathering ("TABLES
  I–VI" as one tab to an index sheet §6.13) — tabs never
  shrink below 44px of edge each; a crowded fore-edge is
  a binding fault. *Very long page:* proportional
  positions compress but keep order; two tabs may not
  overlap — the later section's tab yields downward and
  the audit (§10) flags the crowding.
- **Accessibility spec (v2).** A labelled `<nav>`
  ("Thumb index"); `aria-current="location"` on the
  pressed tab; labels are text (rotated visually, read
  normally); paper-on-maroon 8.5:1 (§2). Touch targets
  ≥44×44px (the tab's hit area extends into the sheet).
  Keyboard order follows the binding order.
- **Tokens consumed (v2).** `--maroon`, `--paper`,
  `--ink`, `--ease-settle`, `--dur-press` (120ms).

### 6.12 The Rules for Interpolation plate

- **What & why.** A printed box — the book teaching its own
  method, as the original entry demands. On paper-deep, under
  a double rule, Spectral prose states the actual rule the
  whole site runs on: *"To find a value between two printed
  rows: take the difference of the rows, multiply by the
  fraction of the interval traversed, and add to the lower
  row. Where the column curves, apply the second-difference
  correction −t(1−t)/2 × δ², where δ² is the difference of
  the differences. Where the column is straight, no
  correction is due, and none may be taken."* — followed by
  the worked line at t = 0.500 in mono. It belongs because
  the theme's interactivity is a method, and a method that
  is not printed is a trick.
- **Structure.** A `<section>` styled as a plate: paper-deep
  ground, double rule at its head (§6.7's SVG, printed
  static here — the plate is a document, not an honour
  candidate), prose in Spectral, the formula set in Plex
  Mono on its own ruled lines, and the worked line beneath.
  It sits immediately after the interpolating table (§6.2)
  in the page order — the instrument, then its rules.
- **Motion spec.** Almost none, by design: the plate's
  rules draw on entry (§5, 400ms) and its worked line's
  figures ink in. The formula does not animate. A rule that
  performs is a rule that is not being read.
- **States.** Rest (printed) / cited (when §6.1's "see the
  rule" link or §6.2's marker references it, a pencil note
  in its margin reads "cited above" — the book cross-
  references itself). No other states.
- **Content merge.** The plate is the site's methodology
  page in miniature — for an education client it IS the
  lesson; for an engineering client it is the methods note
  their evaluators look for. Its figures are the record's
  (§6.10), its rule is the code's (§6.2's implementation
  must match the printed rule exactly — §10 audits the
  code against the plate, not the plate against the code).
- **Failure fallback.** Static print is its only mode;
  there is nothing to fall back from.
- **Reduced-motion variant.** Identical, rules printed.
- **Performance budget & mobile variant.** Static text;
  zero budget. Mobile: full sheet width, formula lines
  scroll horizontally if needed (a formula never wraps
  mid-term).
- **Choreography timeline (v2).** Entry: rules draw
  400ms → prose inks → worked line figures ink 300ms →
  rest. When cited from §6.1 during the hero's computation,
  the note prints at the strike's moment — the reader who
  looks down mid-computation finds the rule already
  expecting them.
- **State matrix (v2).** *Rest / cited:* as above.
  *Hover / focus / active:* the plate contains one link
  (to the full methods sheet, where the site has one) with
  standard link treatment (§11). *Scrolled-past:* nothing
  changes. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: plate spans the table
  column, margin holds the citation note. 768–1199px:
  same, note inline. <768px: full width, formula scrolls.
- **Edge cases & failure modes (v2).** *A build whose
  interpolation is not linear* (spline, Everett full
  form): the plate must print the rule actually used,
  verbatim-audited — the plate is written from the code's
  mathematics by the mathematician, never by the copywriter
  from the code's behaviour. *Translation:* the rule is
  prose and translates as prose; the formula and figures
  do not translate (§12).
- **Accessibility spec (v2).** The formula is real text
  (not an image of mathematics), with a prose paraphrase
  immediately beneath for AT that reads symbols poorly:
  "In words: the correction grows from nothing at the
  printed rows to its largest at the middle of the
  interval." Contrast ink on paper-deep 10.6:1.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`,
  `--pencil`, `--rule`, `--ease-draw`.

---

### 6.13 Table of Tables — the listing sheet

- **What & why.** The volume's listing page (products,
  courses, datasets — whatever the site enumerates) is a
  *Table of Tables*: each entry is a ruled row, not a card —
  entry number (roman), title (Spectral), the entry's key
  figure in mono (from the record or the entry's own table),
  its limits, and its thumb tab reference. A visitor reads
  the catalogue the way they read any table in the book: by
  rows, with the straightedge (§6.4) available. It belongs
  because a listing in this theme must be a table or admit
  it is not part of the volume.
- **Structure.** A `<table>` styled as the listing: rows
  44px (taller than data rows — entries carry a title plus
  a one-line Spectral description beneath, set on two ruled
  lines), the key figure right-aligned, a final column
  "TAB" giving the entry's own tab label. Rows are links
  (the title cell carries the `<a>`, the row highlights as
  one). Filtering, where the site needs it, is by printed
  gathering ("GATHERING II — ELEVATIONS 30°–60°") — sections
  of the table, not a filter UI.
- **Motion spec.** Entry rules draw (§5, 400ms, capped);
  rows ink in. Hover lays the straightedge (§6.4, full
  two-line height). No other motion — a catalogue that
  performs is a catalogue that is not being compared.
  Pagination is by gathering (§6.14's folios): turning a
  gathering is a §6.8 turn in miniature (300ms, within the
  sheet).
- **States.** Rest / hovered (edge laid) / focused (edge +
  outline on the title link) / current (the entry the
  visitor came from carries a pencil tick in its margin —
  the book remembers where you were). Empty gathering: the
  sheet prints its rules and a pencil note, "No tables in
  this gathering" (§12's empty voice) — never a blank page.
- **Content merge.** Each row's key figure is live data
  from the entry's own table — change the entry's record
  and the listing's figure changes. The listing is an index
  of the book's numbers, not a marketing grid wearing
  numbers as decoration.
- **Failure fallback.** A printed table of links: complete
  without JS. Live figures print at their record values;
  nothing about the listing depends on motion.
- **Reduced-motion variant.** Rules print; gathering turns
  are instant swaps.
- **Performance budget & mobile variant.** Rows are DOM;
  gatherings cap at 24 rows per sheet. Budget ~0ms/frame.
  Mobile (<768px): the description line drops (title,
  figure, tab remain — the figure never drops), rows 52px,
  horizontal scroll forbidden: the listing must fit the
  sheet, so the limits column is the one that goes.
- **Choreography timeline (v2).** Sheet enters → rules
  draw → rows ink top-down (24ms stagger, capped at 12) →
  rest. Gathering turn: press (120ms) → sheet swap 300ms
  → new rows print (no draw — a turned-to gathering is
  already printed).
- **State matrix (v2).** *Rest / hover / focus / current:*
  as above. *Active:* row press = navigation (§6.8 turn
  from the listing sheet). *Scrolled-past:* the pencil
  tick on the origin row persists. *Disabled:* an entry
  withdrawn from the volume prints struck in red with its
  errata reference (§6.17) instead of vanishing — the
  catalogue admits its withdrawals. *Touch:* tap = open;
  no edge.
- **Breakpoints (v2).** ≥1200px: full columns (number,
  title+description, limits, figure, tab). 768–1199px:
  limits column folds into the description line.
  <768px: number, title, figure, tab only.
- **Edge cases & failure modes (v2).** *Long titles:* two
  lines max, then the title is shortened by the editor,
  never by ellipsis CSS — a truncated title in a table of
  contents is a misprint. *Figure unavailable:* the cell
  prints an em-rule and a pencil note in the margin; the
  row is never given an invented figure to complete the
  grid (§1 law).
- **Accessibility spec (v2).** Real table semantics;
  row links labelled by title + figure ("Table VIII,
  elevations, range to 9,177 metres"). Withdrawn entries
  announce their struck state in text ("withdrawn — see
  errata"), not by colour alone.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--rule`,
  `--red` (withdrawals only), `--pencil` (tick, notes),
  `--ease-draw`.

### 6.14 Folio progress rail

- **What & why.** Progress through the book is printed in
  the margin as a folio: while the interpolating table
  (§6.2) is being operated it reads "ROW 250.0 · t = 0.500";
  elsewhere it reads the sheet's own position — "SHEET 4 OF
  9 · TABLE VII" — updating as gatherings pass. It belongs
  because progress in a bound volume is a folio, and this
  folio is honest: it reports a position inside the data,
  not a percentage of persuasion.
- **Structure.** A margin-column element, `position:
  sticky` at the reading line's height, Plex Mono 13px,
  two lines: the position line and the provenance line
  ("FROM TABLE VII" / the current sheet's table). A
  hairline rule above and below. It reads its values from
  the shared loop's state (the same computation as §6.2) —
  the folio never computes anything of its own.
- **Motion spec.** No motion of its own: its figures change
  as the loop's values change (text updates only when the
  displayed value changes, as §6.2). When the visitor
  leaves the table's range, the folio crossfades (200ms)
  from row-position mode to sheet-position mode.
- **States.** Row mode (inside §6.2's range: argument +
  t) / sheet mode (elsewhere: sheet n of N + current
  table) / end mode (at the colophon: "END OF THE VOLUME"
  — the folio's one ceremonial state).
- **Content merge.** The folio is the book's own apparatus
  reporting the reader's real position in real units —
  rows and sheets, never percents. On a one-sheet page it
  does not render (a single sheet needs no folio).
- **Failure fallback.** No-JS: the folio prints statically
  per sheet ("SHEET 4 · TABLE VII") — each sheet's folio
  is authored in its HTML, as a printer prints it. The row
  mode is the enhancement.
- **Reduced-motion variant.** Identical except the mode
  crossfade is instant. (The folio's figures in reduced
  motion follow §6.2's static midpoint: "ROW 250.0 ·
  PRINTED".)
- **Performance budget & mobile variant.** Text writes on
  change only; ~0ms/frame. Mobile (<768px): the folio
  becomes a slim bar pinned to the sheet's top edge (below
  §6.11's tab strip): one line, "ROW 250.0 · t = 0.500",
  12px mono — the margin it lived in no longer exists.
- **Choreography timeline (v2).** Sheet 1: folio prints
  "SHEET 1 OF 9" → table range nears: crossfade 200ms to
  row mode as the pin engages → t sweeps: folio tracks →
  pin releases: crossfade back to sheet mode at the new
  sheet number → colophon: end mode.
- **State matrix (v2).** *Row / sheet / end modes:* as
  above. *Hover / focus / active:* none — the folio is
  not interactive and not focusable. *Scrolled-past:* it
  is the scrolled-past indicator. *Disabled:* n/a.
  *Touch:* identical (top-bar form).
- **Breakpoints (v2).** ≥1200px: margin, two lines,
  sticky. 768–1199px: margin narrows; provenance line
  drops (position only). <768px: top bar, one line.
- **Edge cases & failure modes (v2).** *Sheet count
  changes (dynamic content):* the folio's "OF N" is
  computed from the DOM's sheet count at load and
  re-computed on any sheet insertion — a folio that
  miscounts the book is a misprint and §10 checks it.
  *Anchor jump into mid-table:* folio snaps to the
  landed t within one frame (§6.2's jump rule).
- **Accessibility spec (v2).** `aria-hidden` while in row
  mode (its values duplicate §6.2's settled aria-label);
  in sheet mode it is plain text in flow order at the
  sheet's head for AT (the sticky visual copy is the
  duplicate). Position information is never the only way
  to know where you are — headings carry sheet numbers
  too (§4).
- **Tokens consumed (v2).** `--ink`, `--pencil`, `--rule`,
  `--loop-lerp` (0.12).

### 6.15 Request-a-computation form (the conversion section)

- **What & why.** The volume's conversion act is not
  "sign up" — it is *submitting an argument and receiving a
  computed slip*. The form asks for the visitor's v₀ (and,
  in a real build, their name and the address the slip is
  sent to — the site's actual lead fields wearing the
  theme's clothes) and returns a printed computation slip:
  the bracketing rows, the interpolation worked in full,
  the correction applied, the final figure double-ruled
  (§6.7), initialled by the computor on duty, and numbered
  from the volume's own count ("SLIP № 48" — the 47 slips
  the sheet prints as already issued, plus this one; the
  count is DOM-derived, §10 audits it). It belongs because
  conversion in a book of tables is a request the book can
  honour with its own method — the visitor leaves with a
  figure and its working, which is the site's whole promise
  in one slip.
- **Structure.** A form sheet: fields as ruled lines
  (§11's input treatment — borderless on a printed rule,
  mono entries), labels as column headers. On submit, the
  form does not navigate: a paper-bright slip (§2) is
  placed beneath the form sheet's foot rule — it fades and
  settles 240ms `--ease-settle` — carrying
  the full computation in mono, generated from §6.10's
  record by §6.12's rule in the browser, or server-side in
  a real build (the slip must be identical either way;
  §10 cross-checks one against the other). The slip is
  *placed*, never slid or flipped in (§5: sheets are
  placed). Out-of-range
  arguments are refused in the book's voice (§12): "Table
  VII is printed between 200 and 300. For arguments
  beyond, see Table VIII" — never a silent clamp, never
  an extrapolated figure (extrapolation is the one
  computation the book will not perform).
- **Motion spec.** Submit: the form's rules hold; a pencil
  "computing" note prints in the margin (the hand is at
  work — the honest form of a loading state, capped at
  900ms; if the answer takes longer, §6.16's skeleton
  takes the slip's place). Slip arrival: settle 240ms →
  its lines type at 24ms/char in computation order (§6.1's
  cadence, shorter: the slip shows bracketing rows,
  difference, fraction line, correction, final) → final
  figure double-ruled (§6.7, 860ms) → initials print.
  Total performance ≤2.6s.
- **States.** Rest (form printed, no slip) / computing
  (pencil note, fields disabled — a computation in
  progress is not interrupted) / answered (slip placed,
  double-ruled, numbered) / refused (out-of-range or
  invalid: the refusal prints on a slip of its own —
  refusals are also issued in writing, in §12's voice,
  with the nearest valid table named) / error (submission
  failed: the slip prints the failure plainly and the
  form re-opens; nothing is struck because nothing was
  asserted).
- **Content merge.** The slip's figure is the visitor's
  own argument computed from the site's real record — the
  lead magnet is the product's method, worked on the
  visitor's number. A build whose form returns a generic
  "thanks" has left the theme at the exact moment of
  conversion (§9).
- **Failure fallback.** No-JS: the form is a real form —
  it submits to the server and the answer returns as a
  printed slip on the result sheet (the same slip, server-
  rendered). The in-page performance is the enhancement;
  the computation is the service.
- **Reduced-motion variant.** Slip appears without settle
  or typing: full computation printed, double rule drawn,
  initials present. The computing note still shows (it is
  information, not motion) for waits over 300ms.
- **Performance budget & mobile variant.** The computation
  is arithmetic on six rows — negligible; the typing is
  class toggles. Budget ≤0.2ms/frame. Mobile (<768px):
  form fields full sheet width; the slip stacks beneath
  the form (never overlays it); slip № and initials move
  to the slip's head line.
- **Choreography timeline (v2).** t=0 submit → fields
  disable, pencil note prints (120ms) → computation
  (≤900ms) → slip settles t≈300–540ms → lines type to
  ≈t=1500ms → double rule sweeps t=1500–2360ms →
  initials print → answered; focus moves to the slip's
  final figure line (tabindex −1) at settle's end.
  Refusal path: slip settles with the refusal text only —
  no typing, no double rule (a refusal is not a final
  answer and does not earn the honour).
- **State matrix (v2).** *Rest / computing / answered /
  refused / error:* as above. *Hover:* fields take the
  double-rule focus treatment (§11); the submit button is
  a tab-style press (§6.11's mechanics in maroon).
  *Focus:* 2px ink outline under the field's rule —
  fields are found by their rules. *Active:* submit
  press 120ms. *Scrolled-past:* an answered slip persists
  (it is a document the visitor was issued). *Disabled:*
  during computing, all fields disabled with the reason
  in the margin note. *Touch:* identical; targets ≥44px
  (form sheets use a 44px rule pitch, declared in §11).
- **Breakpoints (v2).** ≥1200px: form in the table
  column, margin holds the computing note and the issued-
  slips count. 768–1199px: same, count inline.
  <768px: single column, slip stacked, count at the
  form's head.
- **Edge cases & failure modes (v2).** *Boundary
  arguments:* v₀ exactly 200 or 300 is a printed row —
  the slip says so and returns the row itself, uncorrected
  ("the argument is printed; no interpolation is due").
  *Repeated submissions:* each issues a new slip with the
  next number; earlier slips remain below, a growing
  bundle tied by the count. *The planted error's bracket
  (v₀ in 260–280 or 280–300):* interpolation derives from
  the PRINTED (erroneous) apogee until §6.5 corrects it —
  the slip then carries a pencil note "apogee column under
  correction, E.M." — the book never silently computes
  from a value it knows is struck.
- **Accessibility spec (v2).** Real `<form>`, real labels,
  errors as text beside the field in §12's voice and
  linked by `aria-describedby`. The answered slip is a
  `<section aria-label="Your computation">`; its arrival
  is announced once, politely, with the final figure.
  Contrast: slip ink on paper-bright 12.6:1; refusal text
  in ink (never red — a refusal is not a correction).
- **Tokens consumed (v2).** `--paper-bright`, `--ink`,
  `--pencil`, `--red` (initials on corrected columns
  only), `--maroon` (submit), `--ease-settle`,
  `--ease-type`, `--dur-type-char` (24ms).

---

### 6.16 In-press skeleton & sheet-turn loader

- **What & why.** When a sheet or a slip is not yet ready,
  the book says so in print: blank ruled sheets — the rule
  grid with no figures — headed by a printed note, "IN
  PRESS — THIS SHEET IS BEING SET", with the sheet's table
  number and its expected contents named ("TABLE VIII —
  ELEVATIONS 30°, IN PREPARATION"). No shimmer, no spinner:
  a printing house admits a sheet is at press. It belongs
  because the skeleton is the theme's honesty about absence
  — the ruled emptiness is exactly the shape of what is
  coming, ruled to its true row count where known.
- **Structure.** A sheet skeleton: paper ground, the 30px
  rule grid drawn (static), a header block with the table
  number and caption area left blank-ruled, and the printed
  note in Spectral italic where the caption will stand.
  Row count matches the expected table's where the build
  knows it (declared in the skeleton's data), else a
  standard 8-row gathering. Hard ceiling: 1500ms — at the
  deadline the skeleton is replaced by whatever has
  arrived, or by the failure note (below); a sheet may not
  stay "in press" past its own deadline.
- **Motion spec.** None while waiting (a ruled sheet does
  not shimmer — §9). On arrival, the real sheet's rules
  redraw (§5, 400ms) and figures ink in — the setting of
  the type is the transition. The skeleton itself is
  dismissed without ceremony.
- **States.** In press (ruled, noted) / arrived (replaced
  by the sheet) / failed (deadline passed with nothing:
  the note changes to ink — "THIS SHEET COULD NOT BE SET —
  THE VOLUME CONTINUES AT TABLE IX" with a link onward;
  the ruled sheet remains as the record of the gap).
- **Content merge.** The skeleton is shaped by the real
  sheet it stands for — its table number, its row count,
  its place in the binding. It is a placeholder that knows
  what it is holding the place *of*.
- **Failure fallback.** The failed state IS the fallback,
  and it is printed, permanent and honest. No-JS: server
  renders either the sheet or the failure note; the
  in-press state is a client-side courtesy only.
- **Reduced-motion variant.** Identical (there is no
  motion to reduce); arrival redraw becomes print.
- **Performance budget & mobile variant.** Static DOM;
  one timer. Budget ~0ms. Mobile: identical, rule pitch
  per the sheet it stands for.
- **Choreography timeline (v2).** t=0 skeleton prints
  (rules already drawn — a skeleton never "loads" its own
  rules) → content arrives (t≤1500ms): redraw + ink-in
  400ms → sheet at rest → OR deadline t=1500ms: failure
  note inks in 300ms → the volume continues.
- **State matrix (v2).** *In press / arrived / failed:*
  as above. *Hover / focus:* the failure state's onward
  link is the only interactive descendant. *Active:* n/a.
  *Scrolled-past:* an in-press sheet scrolled past keeps
  its deadline — time at press does not pause for an
  absent reader; on return it shows arrived or failed.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** All breakpoints identical in
  behaviour; the skeleton takes its sheet's own grid at
  each size.
- **Edge cases & failure modes (v2).** *Partial arrival
  (half the rows):* the sheet prints what arrived with a
  pencil note "rows beyond 12 not yet set" — a partial
  table is printed as partial, never padded with invented
  rows (§1 law). *Repeated failures:* the errata sheet
  (§6.17) logs the sheet's failure with its date — the
  book keeps its own production record.
- **Accessibility spec (v2).** `role="status"` with the
  note as its text ("Table VIII is in press"); the failed
  state moves the note to a heading so AT finds the gap
  in the document outline. Ruled emptiness is CSS —
  nothing for AT to trip over.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`,
  `--ink`, `--rule`, `--pencil`, `--watchdog-press`
  (1500ms).

### 6.17 Binding colophon & errata footer

- **What & why.** The volume closes as a book closes: a
  maroon binding footer carrying the colophon ("Set in
  Spectral and IBM Plex Mono. Computed from Table VII.
  Corrections to the errata sheet are welcomed and will be
  initialled."), the volume's imprint and — the living
  part — the **errata sheet**: the running list of every
  correction the book carries (the planted apogee error
  and its state, any §6.5 corrections made this session,
  any §6.16 failures), each with its table, its struck and
  recomputed values, its initials and its date. The
  trajectory arc (§6.3) terminates at the colophon's head
  rule: the curve lands in the binding. It belongs because
  a book of tables is judged by its errata — a volume with
  no errata sheet is claiming it has never been wrong.
- **Structure.** A `<footer>` on `--maroon`, paper text
  (8.5:1): three gatherings — the colophon (Spectral,
  paper), the imprint (mono: volume, edition, the record's
  name and audit date), and the errata list (a small table
  on the maroon: struck figure in paper at 60% with its
  strike, recomputed figure full paper, initials, date).
  Session corrections from §6.5 append to the errata list
  live. The arc's endpoint is positioned to meet the
  footer's head rule exactly (§6.3).
- **Motion spec.** The footer does not perform: its one
  motion is an errata entry arriving (when §6.5 corrects)
  — the entry inks in on the maroon over 300ms when the
  visitor next reaches the footer; if they are already
  looking at it, it inks in live with the initials last.
- **States.** Rest (errata as printed at build) / appended
  (session corrections added, count in the colophon line
  updated: "Errata this session: 1") / audited (the
  imprint's audit date is the build's; it does not change
  at runtime — the book does not pretend to re-audit
  itself nightly).
- **Content merge.** The errata sheet is the site's
  correction record — for a data publisher it is a real,
  linkable, citable page of record, the thing evaluators
  bookmark. The colophon names the actual record and
  typefaces of THIS build.
- **Failure fallback.** Static print; the session-append
  is the only enhancement. If §6.5's storage fails, the
  errata still lists the build's printed corrections.
- **Reduced-motion variant.** Entries print without
  ink-in. Everything else identical.
- **Performance budget & mobile variant.** Static footer;
  appends are single-row inserts. Budget ~0ms. Mobile
  (<768px): the three gatherings stack; the errata table
  scrolls horizontally on the maroon (paper figures on
  maroon at 8.5:1 remain legible).
- **Choreography timeline (v2).** Visitor reaches footer:
  colophon printed → errata entries (if any session
  corrections pending) ink in sequence 300ms each,
  initials last → rest. The arc's endpoint has already
  landed at the head rule (§6.3's complete state).
- **State matrix (v2).** *Rest / appended / audited:* as
  above. *Hover:* errata entries take the straightedge in
  paper (the brass does not read on maroon; the edge here
  is a paper rule at 60%). *Focus:* links take a 2px
  paper outline. *Active:* n/a. *Scrolled-past:* n/a (it
  is the past). *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three gatherings side by
  side. 768–1199px: colophon + imprint side by side,
  errata beneath full width. <768px: stacked, errata
  scrolls.
- **Edge cases & failure modes (v2).** *No errata:* the
  sheet prints "No errata recorded for this edition" —
  an empty errata sheet is printed, never omitted (its
  absence would read as concealment). *Many session
  corrections:* the list caps at the session's real count
  — it is a record, it does not paginate; beyond 12, it
  scrolls within the footer gathering.
- **Accessibility spec (v2).** Footer landmarks and
  headings in order; the errata is a real table with
  headers (Table / Printed / Corrected / Initials /
  Date). Struck figures on maroon use `<del>`; contrast
  of the 60% struck figure on maroon ≈4.6:1 — legible,
  and its struck state is semantic, not colour-only.
- **Tokens consumed (v2).** `--maroon`, `--paper`,
  `--rule`, `--ease-draw`.

### 6.18 Plate not in this volume — the 404 sheet

- **What & why.** A missing page in a bound volume is a
  collation fault, and the book says so as a printer
  would: a sheet headed "PLATE NOT IN THIS VOLUME", the
  requested reference printed in mono, and the collation
  note — "This reference was called for but is not bound
  in. The volume contains Tables I–IX; the nearest bound
  sheet is Table VII" — with links ruled beneath to the
  nearest sheets and the Table of Tables (§6.13). Its
  choreography is specified as *nearly none*: a fault is
  stated, not performed. It belongs because even the
  book's errors must be issued in the book's own form.
- **Structure.** A single sheet: folio (§6.14's static
  form, "SHEET — UNNUMBERED"), the heading (Spectral),
  the requested path in Plex Mono on a ruled line, the
  collation note (Spectral), and three ruled links (the
  record §6.10, the listing §6.13, the volume's first
  sheet). The thumb rail (§6.11) prints with NO tab
  pressed — the only sheet in the book with no tab, which
  is itself the signal.
- **Motion spec.** None beyond the sheet's rule draw on
  entry (§5). No arc (the curve does not annotate a sheet
  that does not exist), no worked example (the computor
  does not perform over a fault).
- **States.** One state: printed. (A 404 with states is a
  404 showing off.)
- **Content merge.** The nearest-sheet links are computed
  from the requested reference against the volume's real
  contents — a request for "table-x" names the nearest
  bound table by the book's own numbering, not a generic
  "go home".
- **Failure fallback.** This IS the fallback — server-
  rendered, static, complete with no JS.
- **Reduced-motion variant.** Identical.
- **Performance budget & mobile variant.** One static
  sheet; zero budget. Mobile: identical, links stack.
- **Choreography timeline (v2).** Specified as *none*:
  the sheet prints. The absence of choreography is the
  choreography — §13's map records this beat as a rest.
- **State matrix (v2).** *Rest:* printed. *Hover /
  focus:* the three links take standard treatments
  (§11). *Active:* navigation (§6.8 does NOT turn to
  leave a fault sheet — plain navigation; the book does
  not ceremonially exit its own error). *Scrolled-past:*
  n/a. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** All sizes: one sheet, same
  contents; <768px the mono reference line wraps (paths
  may break anywhere — a path is not a figure).
- **Edge cases & failure modes (v2).** *A reference that
  almost matches a bound sheet* ("tabel-vii"): the note
  names the probable sheet ("perhaps Table VII was
  meant") — collation faults include misprints, and the
  book is polite about them. *Repeated faults from one
  source:* not the sheet's business; the server logs,
  the sheet states.
- **Accessibility spec (v2).** A real 404: correct HTTP
  status (the build's duty, stated here so it is not
  forgotten), heading hierarchy intact, the requested
  reference readable as text. No motion, no traps.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--rule`,
  `--pencil`.

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full ceremony: computed headline (§6.1) computing the flagship figure from the master table (§6.10); the interpolating table (§6.2) as the second sheet; rules plate (§6.12) after it; plates (§6.9) evidencing figures; the worked example (§6.6) in the margin throughout; arc (§6.3) over everything; request form (§6.15) as the closing sheet before the colophon (§6.17). |
| **Listing** | The Table of Tables (§6.13): entries as rows with live key figures, gatherings instead of filters, withdrawn entries struck not deleted. |
| **Detail** (one table / product / dataset) | The entry's own table becomes the record for the page: its interpolating row (§6.2) brackets that table's central interval; its plates caption from its figures; its worked example works its rows. The volume's master table is cited, not repeated. |
| **About** | The computor's room: the firm's history set as a table of years and figures (founded, first table published, records held — each a figure with a source), the margin example working the firm's own founding computation. Portraits are plates (§6.9) captioned by figures ("41 years at the desk"). |
| **Methods / documentation** | The rules plate (§6.12) grown to full sheets: every method the product uses, printed with its formula and a worked line; code samples are set as ruled mono tables (line numbers are a column — the one place a vertical rule is permitted, as a gutter). |
| **Contact / checkout equivalents** | Checkout itself is REFUSED the theme (§6.8): payment leaves the volume (plain, fast, unceremonial). Contact and lead capture ARE the request form (§6.15) — the conversion the book can honestly perform. |
| **Search / index** | The Table of Tables with a mono search line (§11): results are rows, counts are printed ("7 tables answer to 'apogee'"), zero results print the pencil empty note (§6.13). |
| **Error (404)** | §6.18 — the collation-fault sheet. |
| **Print** | The volume prints as itself: arcs fully drawn, interpolated rows at their printed midpoints, corrections shown as printed. A stylesheet that hides the tables to "save ink" fails §10. |

---

## 8. Worked examples

### 8.1 The hero — "the site computes its welcome" (home, first sheet)

**The scene.** An aerospace firm's home page. The sheet
opens on paper: binding maroon at the window's edges, the
thumb rail (§6.11) registered down the fore-edge, folio
(§6.14) reading "SHEET 1 OF 9". The headline, Spectral:
"Range, computed — not quoted." Beneath it, the computation
block (§6.1) and, in the margin, the worked example (§6.6)
already printed (it does not perform during the hero's
computation — one hand at a time; its cycle starts only
after the headline settles).

**The timeline.** t=0: the finished computation stands
printed (the no-JS truth). JS arms; the block blanks to
sized lines. t≈200ms: "R(240), Table VII — 5,873.56" types
in mono. t≈500ms: "R(260) — 6,893.28". t≈800ms: "Difference
— 1,019.72". t≈1050ms: "Half-difference, t = 0.500 —
509.86". t≈1350ms: "Linear value — 6,383.42". Beat.
t≈1760ms: the red strike crosses "6,383.42" (180ms,
`--ease-strike`); beside it types "−10.20, second
difference" and in the margin, red initials "E.M."
t≈2300ms: the final line inks in, heavier: "RANGE AT 250 —
6,373.22 m", and the double rule sweeps beneath it
(t≈2400–3200ms, §6.7). The arc (§6.3) has not yet drawn —
its label already reads the first row's apogee, 1,019.72 m,
waiting for the table below. The visitor has watched the
site's headline number earn its underline. Nothing else on
the sheet has moved.

**Why it works.** Every figure the visitor will meet later
— the table's, the arc's, the form's — is this computation
again. The hero is not an introduction to the method; it
is the method, performed once at full size.

### 8.2 Mid-page — operating Table VII (home, third sheet)

**The scene.** The interpolating table (§6.2) sheet: the
full Table VII (§6.10) printed, the rules plate (§6.12)
immediately after, a plate (§6.9) to the side captioned
"PLATE IV — THE ARC AT 250, APOGEE 1,593.31 m —
INTERPOLATED". The arc overlay crosses above the sheet's
header, undrawn at the sheet's top.

**The scroll timeline.** The table's header crosses the
reading line: rules draw (400ms). The bracket rows (240,
260) centre; the pin engages. The visitor scrolls 160vh:
the interpolated row wakes between the printed rows — at
t=0.25 it reads 245.0 · 6,120.84 · 1,530.21 · 35.33 (time
interpolating exactly: (34.61+37.49)/2 at midpoint is
36.05; at t=0.25, 34.61 + 0.25×2.88 = 35.33 ✓ — the time
column takes no correction and the row's margin derivation
says why). The arc draws in step above; its label follows
the apogee column. At t=0.500 the row reproduces the
hero's figures exactly — the visitor recognises them, and
the recognition is the design's argument: *the same
numbers, because the same table*. The visitor hovers the
280 row: the straightedge (§6.4) lays beneath it. They
click the apogee figure 1,988.65: the pencil tick prints,
the pause, the strike — recomputed 1,998.65 types in red,
"E.M." in the margin (§6.5). The arc's label and the
plate's caption do not change (280 is outside the live
bracket) — but the folio (§6.14) adds the initials to its
provenance line, and the errata sheet (§6.17) has already
gained its entry for when they arrive. Scrolling on, the
pin releases as the table's footer rule draws; the rules
plate inks in beneath — the method, printed, exactly
where a reader who wants to check the trick will look.

### 8.3 Conversion — the request slip (home, closing sheet)

**The scene.** The final sheet before the colophon: the
request form (§6.15), headed "REQUEST A COMPUTATION", its
fields ruled lines: "ARGUMENT v₀ (m/s)", "YOUR NAME",
"SLIP TO BE SENT TO". In the margin, the issued count:
"Slips issued from this volume: 47."

**The submit timeline.** The visitor enters 275 and
submits. Fields disable; the margin prints in pencil:
"Computing — E.M." At t≈400ms the slip is placed beneath
the form: paper-bright, headed "SLIP № 48 — TABLE VII".
Its lines type in order: "R(260) — 6,893.28 · R(280) —
7,994.58"; "Difference — 1,101.30"; "Three-quarters,
t = 0.750 — 825.98" (0.750 × 1,101.30 = 825.975 →
825.98); "Linear value — 7,719.26"; then the strike-free
correction line (a slip does not strike its own fresh
work — it applies the correction as a line): "Second
difference −7.65" (δ² for range across 260–300:
6,893.28 − 2×7,994.58 + 9,177.45 = 81.57; −0.75×0.25/2 ×
81.57 = −7.65); "RANGE AT 275 — 7,711.61 m" — and the
double rule sweeps beneath it (§6.7), initials "E.M."
print at the slip's foot, and beneath, in pencil: "Apogee
column under correction — see the errata sheet" (275
brackets the planted error's row for the apogee column;
the slip's apogee line is therefore printed from the
printed row with its caveat, §6.15's ruling). The visitor
has a number, its working, its caveat and its number in
the book. The lead fields were the price of the slip; the
slip is the product's method, demonstrated on the
visitor's own argument. (Audit note: true R(275) =
275²/9.80665 = 7,711.66; the slip's 7,711.61 differs by
0.05 — the honest residue of two-decimal printed rows,
and §12's voice allows the slip to say so if a visitor
checks: "Figures are computed from the printed rows; the
rows are rounded at the second decimal, and the slip
inherits their rounding." A book that hides this is
lying by omission; this one prints it.)

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Figures that do not align.** A column whose decimals
   wander is instant slop in a table theme. *Cure:* tabular
   mono everywhere, right-aligned to the decimal, per-column
   decimal constants (§3), audited (§10).
2. **A counter that eases to a round number.** Decorative
   stat-counters ("10,000+ computations!") break the law and
   the mood. *Cure:* every moving figure is an interpolation
   or a computation stopping at its exact value (§5).
3. **Red used as an accent colour.** Red buttons, red links,
   red badges — the correction colour spent on decoration
   leaves nothing for corrections. *Cure:* §2's ration —
   red appears only where something is being corrected.
4. **Fake vintage texture.** Coffee stains, torn edges,
   distressed paper PNGs — costume, not computation.
   *Cure:* the only texture is foxing on plate corners
   (§6.9), seeded and rationed; the paper is clean because
   the book is *kept*.
5. **A trajectory arc that is decorative clip-art.** A
   generic swoosh over a hero. *Cure:* the arc is the
   record's own curve with a live, provenanced label (§6.3)
   — or it is not drawn.
6. **Interpolation theatre.** A row that "counts" without
   computing — values that do not satisfy the printed rule.
   *Cure:* §10's audit evaluates the rule at sampled t
   values against the implementation; theatre fails.
7. **Struck text that vanishes.** Corrections that delete
   the original (or hide it behind a tooltip). *Cure:* the
   law — struck figures stay legible at 0.55, forever (§6.5).
8. **A generic sans sneaking into UI chrome.** One system-ui
   button and the book is a website in costume. *Cure:* two
   families only (§3); rewrite strings until they fit.
9. **Hover glow / lift on rows.** Shadows and tints borrowed
   from dashboard design. *Cure:* the straightedge (§6.4) —
   the hover is a tool or it is nothing.
10. **Percent progress bars.** A bar filling across the top
    of a book of tables. *Cure:* the folio (§6.14) — position
    in rows and sheets.
11. **Invented figures to complete a grid.** A listing row
    given a plausible number because the cell looked empty.
    *Cure:* the em-rule and pencil note (§6.13); an honest
    gap beats a completed lie.
12. **The computor as mascot.** A cartoon clerk with a
    pencil, waving. *Cure:* the computor is initials, pencil
    workings and a tick — a presence made of work, never a
    character (§6.6).
13. **Extrapolation offered as a feature.** "Project beyond
    the table!" *Cure:* §6.15's refusal, in writing — the
    book's refusal to extrapolate is its credibility.
14. **Double rules everywhere.** Titles, buttons, cards all
    double-underlined until the honour is wallpaper.
    *Cure:* the ration — ≤3 per page (§6.7), enforced by
    §10.

---

## 10. Quality gate

Blocking checks — the theme may not ship until all pass:

- [ ] **Figure audit.** Every printed row of the record
  (§6.10) recomputes from its generating formulae within
  the last printed decimal — except whitelisted planted
  cells (exactly one: apogee at v₀ 280), listed in the
  errata (§6.17).
- [ ] **Derivation audit.** Sampled at t = 0.13, 0.25,
  0.500, 0.77, 0.91: §6.2's row, §6.3's label and §6.15's
  slip agree with §6.12's printed rule applied to §6.10's
  rows, to the column's last decimal. §6.1's hero figures
  equal §6.2's t = 0.500 figures exactly.
- [ ] **Identity at the brackets.** §6.2 at t=0 and t=1
  reproduces the printed rows exactly (no correction due,
  none taken).
- [ ] **DOM/data agreement.** The JSON twin (§6.10) diffs
  clean against the printed table; §6.2's data attributes
  match the printed figures.
- [ ] **Slip count audit.** §6.15's issued count equals the
  slips actually printed in the sheet's DOM; the next slip
  number is count + 1.
- [ ] **No-figure-without-working sweep.** Every numeral on
  every page traces to the record or a shown derivation.
  (Grep for numerals; sample 20; all must trace.)
- [ ] **Red census.** Red appears only in corrections,
  initials, errata and §6.5's focus ring. Any other red
  fails.
- [ ] **Double-rule census.** ≤3 honoured elements per
  page.
- [ ] **Watchdog drill.** With the rAF loop blocked:
  hero prints finished ≤2000ms, table prints its midpoint
  row ≤3000ms, arc prints drawn with the midpoint label,
  skeleton fails honestly at 1500ms.
- [ ] **No-JS pass.** The whole site read with scripts
  disabled: every figure present at its true or printed-
  midpoint value, corrections pre-applied, navigation
  complete.
- [ ] **Reduced-motion pass.** Full read with
  `prefers-reduced-motion`: no typing, drawing, pinning
  or turning; all content present in print form.
- [ ] **Alignment pass.** Every column's decimals align at
  360px, 768px and 1440px widths; no figure wraps.
- [ ] **Correction cascade.** Correcting §6.5's planted
  figure re-derives §6.2 (when in bracket), §6.3 and
  §6.15 within one frame, each carrying the initials.
- [ ] **Gate signed by a non-builder** — the checker
  initials the gate in the margin, as the book would.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment — or its refusal, with the in-theme
replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | A maroon tab-press (§6.11's mechanics): Spectral caps on maroon, paper text; press = 4px inset, 120ms. Reserved for the sheet's one commitment (submit, request) |
| Secondary button | Underlined Spectral text with a hairline rule that deepens rule→ink on hover (160ms); never a box |
| Text input | A ruled line: borderless field sitting on a printed rule, Plex Mono entries; focus = the rule doubles (a second hairline draws beneath, 160ms) — the §3 underline honour in miniature, rationed to forms |
| Select / picker | A printed list on a paper-bright slip: the options as ruled rows, chosen one ticked in pencil. Native `<select>` is refused — its chrome is not the book's |
| Checkbox | A small ruled box ticked by a self-drawn pencil check (SVG, 300ms, seeded wobble as §6.5's tick grown up) |
| Radio group | Ruled rows; the chosen row's figure column carries a pencil tick; unchosen rows stay blank — a table of mutually exclusive rows |
| Tabs | The thumb tabs (§6.11) — the only tabs. In-sheet content tabs are refused: a sheet is read top to bottom |
| Accordion | Refused. Sheets do not fold; long matter is a longer sheet with gathering breaks (§4) |
| Modal / dialog | Refused as chrome. The one overlay need (a figure's full derivation) prints in the margin (§6.2/§6.5) — the book annotates, it does not pop up |
| Toast | Refused. Outcomes are issued as slips (§6.15) or printed as margin notes; nothing floats and vanishes from a book of record |
| Alert / banner | A correction slip: paper-bright, red head rule, the matter stated in §12's voice, initialled. Used only for record-level matters (a table under correction) |
| Badge / chip | Refused as pills. States are printed words in mono ("INTERPOLATED", "UNDER CORRECTION", "WITHDRAWN") in the figure's own row |
| Pagination | Gathering folios (§6.14): "GATHERING II" with prev/next as ruled entries; never numbered page pills |
| Table | The theme's atom (§6.10's pattern): horizontal rules only, 30px pitch, tabular mono, caption with quantities/units/decimals |
| Card | Refused as a floating box. The card's job is done by the plate (§6.9) and the listing row (§6.13) |
| Progress bar | Refused; replaced by the folio (§6.14) |
| Spinner | Refused; replaced by the in-press skeleton (§6.16) and the form's pencil computing note (§6.15) |
| Skeleton | §6.16 — blank ruled sheets with a printed note, no shimmer |
| Tooltip | A pencil margin note printed beside the item on focus/hover — positioned text in the margin column, never a floating grey box |
| Breadcrumbs | A collation line in mono at the sheet's head: "VOLUME › TABLE VII › ROW 280" — the book's own addressing |
| Search | A mono input line (§6.13): results are rows; the count is printed as a figure ("7 TABLES") |
| Empty state | A ruled sheet with a pencil note in §12's voice (§6.13's pattern) |
| Error state | §6.18's collation sheet for pages; §6.15's printed refusal for forms |
| Avatar / identity | Refused — the computor has initials, not a face (§6.6). Organisational identity is the colophon's imprint (§6.17) |
| Toggle / switch | Refused; binary states are ticks in boxes (checkbox row above) |
| Form validation | Messages print beneath the field's rule in §12's voice, in ink; the field's rule takes a red underline ONLY when the entry contradicts the record (a value the table cannot serve) — red keeps its meaning even here |

---

## 12. Content & copywriting voice

Two registers, kept apart. **The book's voice** (Spectral) is
the volume speaking: measured, complete sentences, no slang,
no exclamation marks anywhere in the theme. **The computor's
hand** (Plex Mono, pencil or red) is one working person's
annotations: terse, exact, dry — the margin voice of someone
who has checked this before.

- **Headlines** (book): a statement about the figure, with
  the method named where possible. ✓ "Range, computed — not
  quoted." ✗ "Blast Off to Better Performance!!" — noise,
  and two exclamation marks the book would never print.
- **Captions** (book, italic): quantity, units, limits —
  always all three. ✓ "Table VII. Range, apogee and time of
  flight at 45°, for initial velocities from 200 to 300
  metres per second. Figures to two decimals." ✗ "Our
  amazing data" — a caption that praises is a caption that
  has stopped informing.
- **Labels** (mono): literal, unit-bearing. ✓ "ARGUMENT
  v₀ (m/s)" / "SLIPS ISSUED" / "UNDER CORRECTION". ✗
  "Your journey starts here" — the book has no journeys.
- **The computor's notes** (hand): ✓ "Checked — agrees." /
  "Apogee column under correction." / "Rows beyond 12 not
  yet set." ✗ "Oops! Something went wrong 😅" — the hand
  does not perform cheerfulness, and there are no emoji in
  the volume, ever.
- **Error messages** (form, book voice with the hand's
  plainness): ✓ "Table VII is printed between 200 and 300.
  For arguments beyond, see Table VIII." — states the
  limit, names the remedy. ✗ "Invalid input" — invalid is
  a verdict, not an explanation.
- **Empty states**: ✓ "No tables in this gathering." ✗
  "Nothing to see here!" — the book reports an absence; it
  does not joke about one.
- **Numbers**: exact, or their derivation shown, or their
  absence admitted. ✓ "6,373.22 m, interpolated from Table
  VII." ✗ "Over 6,000 metres!" — a rounded boast is the
  one sentence this theme exists to prevent.
- **Fixed strings** (verbatim, never paraphrased by a
  build): the refusal — "The table is printed between
  [lower] and [upper]."; the agreement — "Checked —
  agrees."; the closing colophon line — "Corrections to
  the errata sheet are welcomed and will be initialled."
- **Translation rule**: prose translates; formulae, figures,
  initials and the fixed strings' structure do not.
  Numerals stay lining tabular in every locale; a locale
  that groups thousands differently groups them in the
  record and everywhere alike (the audit re-runs per
  locale).

---

## 13. Full-page scroll choreography map

Every motion beat from the sheet's head to the binding, in
order (home page; other page types drop their absent beats
and keep the order):

1. **Open.** The sheet prints: headline standing, computation
   block (§6.1) in its finished state, folio (§6.14) at
   "SHEET 1 OF 9", the computor's example (§6.6) printed in
   the margin. The visitor sees a finished book.
2. **The welcome computes.** §6.1 arms and performs: rows
   type, the correction strikes, the final figure is
   double-ruled (≈3.2s). The example's cycle has NOT started
   — one hand at a time.
3. **The margin wakes.** As the hero settles, §6.6 begins
   its first slow cycle (≈20s) — the room's ambient life,
   deliberately after the welcome, never during.
4. **First gathering break.** Scroll: the folio updates by
   sheet; the arc (§6.3) is present above the headers,
   undrawn, its label holding the first row's apogee.
5. **The instrument.** The table sheet (§6.2/§6.10): rules
   draw, the pin engages, t sweeps 0→1 across 160vh; the
   arc draws in step; the folio switches to row mode; the
   plate's caption (§6.9) follows the apogee. This is the
   page's longest beat and its centre of gravity.
6. **The correction (visitor's beat).** If the visitor
   clicks the planted figure (§6.5), the strike, recompute
   and initials land inside beat 5's stillness — the folio
   gains the initials; the errata (§6.17) silently gains
   its entry. If they never click, the beat is a rest.
7. **The rules.** The pin releases; §6.12's plate inks in —
   the method, printed, at the exact moment a sceptical
   reader wants it.
8. **Plates.** §6.9 plates settle one per sheet, captions
   live while beat 5's table is revisited, static
   otherwise.
9. **The listing.** §6.13's rows, the straightedge (§6.4)
   travelling under the visitor's reading — the quietest
   beat, by design, after the instrument.
10. **The request.** §6.15's form sheet: on submit, the
    computing note, the slip placed, its lines typed, its
    figure double-ruled — the hero's ceremony at slip
    scale, closing the page's argument (the welcome was
    computed; so is your answer).
11. **The binding.** The colophon (§6.17): the arc's
    endpoint lands on the footer's head rule; session
    errata ink in; the folio reads "END OF THE VOLUME".
    The book closes.

**Reverse pass.** Scrolling up: nothing un-draws, un-strikes
or un-honours. The interpolated row re-derives in reverse
(it has no direction); the folio counts sheets back; the
example keeps its own time. A book read backwards is the
same book.

**Jump scroll.** Anchor landings snap every scrubbed value
to the landed position within one frame (§6.2) and honour
skipped titles instantly (§6.7) — the book does not perform
the pages you did not read.

---

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 640KB | Fonts are the weight: Spectral (2 weights + italic) and Plex Mono (2 weights), subset to Latin + figures, ≈180KB; plates are the rest — a plate over 120KB must justify itself to §10 |
| Animation frame budget | ≤ 1.6ms/frame total | Shared loop: interpolation + arc + folio ≤ 0.7ms (§6.2 0.3 + §6.3 0.2 + §6.14 ~0); straightedge ≤ 0.1ms while hovering; all else is event-driven |
| Long tasks | None over 50ms | The computations are arithmetic on six rows; the typing is class toggles; nothing on the page may block |
| Layout shift | 0.00 CLS from motion | Every animated line is pre-sized on the rule grid (§6.1); plates declare aspect ratios (§6.9); the slip's space is reserved by its sheet (§6.15) |
| Ambient loops | Exactly 1 | §6.6's worked-example cycle (timer-driven, off-screen paused). The arc and row are scroll-driven, not ambient. A second ambient loop fails §10 |
| Watchdogs | Loop 3000ms · typing 2000ms · turn 1200ms · press 1500ms | §6.16's ceiling is the theme's promise: nothing waits longer than 1.5s without the book admitting it in print |

**Cut order when the budget is exceeded** (cut in this
order, never skip ahead): 1) plate image weight (recompress;
the frame stays) → 2) the arc's full-page span (restrict to
hero + table sheets, as mobile does) → 3) the worked
example's cycle on mid-tier devices (print it static; the
margin keeps the example, loses the performance) → 4) rule-
draw stagger on long tables (header/footer only, already
the cap) → 5) font weights (drop Spectral 600 to 500
before touching Plex Mono — figures are never the cut).

**Never cut:** the printed fallback of any element, the
watchdogs, the interpolation's exactness (a cheaper
approximation of the rule is a different rule — §6.12
forbids it), the struck figures' legibility, or the errata
sheet.

---

## 15. Build-order checklist

The sequence in which this theme is implemented — records
before performances, print before motion, as the book
itself would insist:

1. **Declare the record.** Author the master table
   (§6.10) as data: rows, units, decimal ruling, generating
   formulae. Run the figure audit (§10) on the data alone.
2. **Print the static volume.** All sheets as finished
   print: tables complete, hero computation printed,
   midpoint interpolated row in place, arc drawn, errata
   listed. The no-JS site must already be the whole book.
3. **The rule grid & type.** Baseline ruling, tabular
   mono, alignment pass at three widths (§10).
4. **The rules plate.** §6.12 written from the mathematics
   (by whoever owns the formulae), before any interpolation
   code exists — the code will be audited against it.
5. **The shared loop.** One rAF loop, lerp 0.12, with the
   3000ms watchdog and its print fallbacks wired first.
6. **Interpolation.** §6.2 from the printed rule; identity
   checks at t=0/1; derivation audit (§10) against sampled
   t values.
7. **The arc.** §6.3 fed by §6.2's computation (never its
   own); label provenance; endpoint registered to §6.17.
8. **The computed headline.** §6.1's performance over the
   printed block; watchdog completing from the end
   backwards; session flag.
9. **The straightedge & corrections.** §6.4, then §6.5
   with its cascade into §6.2/§6.3/§6.15 and the errata
   append (§6.17).
10. **Navigation.** Thumb rail (§6.11) with proportional
    registration, then the turn (§6.8) with its watchdog.
11. **Plates & listing.** §6.9 (captions deriving, never
    describing), §6.13 (live figures from entry records).
12. **The form.** §6.15: refusal logic before success
    path (the book's refusals are its character); slip
    numbering DOM-derived; server twin cross-checked.
13. **Skeleton & 404.** §6.16 with its 1500ms ceiling;
    §6.18 with correct HTTP status.
14. **The margin example.** §6.6 last of the elements —
    ambient life is added to a finished room, never used
    to furnish an empty one.
15. **The gate.** §10 run in full, by a non-builder, who
    initials it in the margin. Only then may the theme be
    used in a build.

---
