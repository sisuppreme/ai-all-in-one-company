# 62. Celestial Navigation Atelier — Expanded (v1 + v2)

A master navigator's chart room, built as a website. The page is a
star atlas on vellum: every section of content sits at a charted
coordinate, a dashed great-circle route threads the whole page and
knots at each section-waypoint, and the reader does not scroll the
page so much as sail it — plotting a course from departure to
landfall through the material itself. Brass, vellum, deep chart
ink; Cormorant Garamond italics for the display voice, Archivo for
every annotation and readout. The theme's one law: **a position is
printed only when it has been fixed** — every coordinate, distance
and bearing on the page is either in the one declared chart record
(§6.17) or derived from it by a rule printed beside it, and no
number is ever worn as decoration. This expansion deepens all ten
original signature elements and adds the eight page-family elements
a real site needs, each with a full build spec.

## 1. Concept & world

The atelier is a working chart room above a harbour: part observatory,
part print shop, part instrument maker's bench. Its fiction is
precise. A navigator fixes a position by taking sights on known
stars, plotting the lines, and accepting the small triangle of
error where they nearly meet. This theme runs a website on exactly
that discipline. The hero headline is not "shown" — it is *fixed*,
by a sextant sighting on three real stars (§6.1). Sections are not
"revealed" — the reader's course *reaches* them (§6.3). Progress is
not a percentage — it is distance sailed along a plotted course, in
nautical miles, against a total that is the course's true charted
length (§6.5, §6.17). The theme sells patience, precision and the
romance of getting un-lost by geometry.

**The world in one paragraph.** It is the hour before dawn in the
chart room. Vellum sheets lie translucent over a star field; brass
instruments catch what light there is; the ink is deep sea-green
black. Everything is annotated by hand — Archivo notes in the
margins, pencilled corrections, a vermilion tick where a thing has
been logged and verified. Nothing glows neon, nothing floats in
glass. The newest object in the room is the reader.

**Best-fit sites.** A navigation, cartography or maritime-heritage
brand; an observatory, planetarium or astronomy publisher; a
watchmaker or instrument maker with a celestial line; a premium
travel house selling voyages rather than trips (expedition cruises,
tall-ship charters, observatory tours); a bookshop or print atelier
whose catalogue is genuinely organised like an atlas; a consultancy
whose whole pitch is "we find your position and plot the course"
— strategy firms with the discipline to keep the metaphor honest.

**Audiences.** Readers who slow down for craft: sailors, amateur
astronomers, map collectors, engineers who respect an instrument,
gift-buyers for all of the above. The theme rewards literacy in its
world — a reader who knows what a great circle is feels *recognised*,
not decorated at.

**When NOT to use it.** Never for anything that must feel instant:
food delivery, breaking news, flash retail, live dashboards. Never
where the content has no position to fix — if the client's material
cannot honestly be organised as places on a course (a commodity
price list, a settings page), the coordinates become lies and the
law collapses. Never for a brand whose voice is brash or comic; the
atelier cannot raise its voice. And never as a skin over an
unrelated template: the route, the record and the readouts are the
theme, and a build that keeps only the colours has kept nothing.

**The law, mechanised.** Three rules enforce "fixed, not decorated":
(1) the chart record (§6.17) is the single data object — route
geometry, waypoint readouts, the progress total, the table, the
footer coordinates and the form's log number all read from it;
(2) a vermilion census — vermilion appears only where a thing has
been *logged* (knot ticks, registration flashes, the record's seal),
never as a general accent; (3) the star field is a real sky — the
sky over the atelier's office on its founding night (§6.6), so the
backdrop can be checked against an atlas, not just admired.

**How a client's content is charted.** Before any design work, the
content is surveyed like a coast: every major section is assigned
a waypoint in sailing order — the order a reader would naturally
make landfall on them — and given a coordinate from the record's
course (a real passage the client can claim: their home waters,
their founding voyage, their trade route). Minor content becomes
sub-waypoints (§4) or soundings — marginal notes at the nearest
waypoint. Content that cannot be placed on the course honestly
(a legal page, a settings screen) is printed as an inset sheet in
the atelier's plain grammar — vellum, ink, no route — rather than
being forced a coordinate it has not earned. The survey is a
deliverable: the client sees the chart of their site, with every
figure derived, before a single sheet is styled.

## 2. Palette

Five anchors from the original entry, unchanged, plus six derived
tokens. Contrast ratios below are measured (WCAG relative luminance)
for this expansion, and the rulings are part of the spec.

| Token | Hex | Role | Ratio / pairing ruling |
|---|---|---|---|
| `--vellum` | `#EFE6D0` | The ground. Sheets, page body, chart paper. ~62% of any viewport. | Ground for `--ink` at 11.83:1 |
| `--ink` | `#1E2A30` | Deep chart ink. Body text on vellum; the star-field ground on dark panels. | On `--vellum` 11.83:1 — the text pairing |
| `--brass` | `#A97E2F` | Instruments, rules, route dashes, frames. The atelier's metal. | On vellum 2.96:1, on ink 4.00:1 — **never text on vellum**; rules, frames, large display on ink only |
| `--vermilion` | `#C8451B` | Signal vermilion. Logged ticks, registration flashes, the seal. Rationed (§1 census). | On vellum 3.91:1 — large/graphical only, never body text, never a background |
| `--teal` | `#4E7A72` | Sea-faded teal. Secondary data ink: depth notes, secondary routes, table striping tint. | On vellum 3.88:1 — large text and graphics; small text uses `--teal-deep` |
| `--brass-deep` | `#7D5E22` | Brass in shadow. Text-sized brass: labels, readouts, coordinates on vellum. | On vellum 4.83:1 — the only brass allowed at text sizes on vellum |
| `--brass-bright` | `#C49A4A` | Brass in lamplight. Text and fine lines on ink panels (hero, footer). | On ink 5.65:1 — text on dark panels |
| `--ink-soft` | `#46545C` | Annotation ink. Archivo margin notes, captions, secondary readouts on vellum. | On vellum 6.30:1 |
| `--teal-deep` | `#33524C` | Deep water. Small teal text on vellum; footer links. | On vellum 6.89:1 |
| `--vellum-dim` | `#CFC3A8` | Vellum in dim light. Captions and secondary text on ink panels. | On ink 8.41:1 |
| `--vellum-deep` | `#E2D5B8` | Sheet edges, skeleton fills, the underside of a turning sheet. | Decorative only; never a text ground |

**Usage ratios.** Vellum ~62%, ink (text + dark panels) ~22%, brass
~9%, teal ~5%, vermilion under 1% — a viewport with more vermilion
than that has failed the census (§10). Dark panels (hero star field,
footer) invert the ground to `--ink` but keep the same ink-on-paper
logic: `--vellum` and `--vellum-dim` become the writing, `--brass-bright`
the metal.

**Dark-mode behaviour.** The theme has no separate dark mode; it has
*lamplight and daylight sheets*. The hero and footer are always ink
panels (the sky is dark because it is the sky, not because a toggle
said so). A client needing a full dark variant re-grounds every sheet
to `--ink`, promotes `--brass-bright` to the working brass and
`--vellum-dim` to secondary text; vermilion's ration does not change.
What never changes: the pairings' contrast rulings travel with the
tokens, not with the mode.

## 3. Typography

Two families, as in the original, with a strict division of labour:
**Cormorant Garamond** is the navigator's display hand — elegant,
italic-leaning, used for headlines, waypoint names and the colophon;
**Archivo** is the annotation hand — readouts, coordinates, labels,
tables, body annotations. A figure is never set in Cormorant; a
headline is never set in Archivo. Numerals in readouts are always
Archivo with tabular figures (`font-variant-numeric: tabular-nums`)
so a counting readout never changes width as it counts.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero headline) | Cormorant Garamond italic 500 | clamp(2.9rem, 6.2vw, 4.6rem) / 1.04 | −0.01em | The fixed headline; locks in via §6.1 |
| Waypoint heading | Cormorant Garamond 600 | clamp(2rem, 3.6vw, 2.75rem) / 1.1 | 0 | Named like a place, not a feature |
| Section heading | Cormorant Garamond 600 | 1.625rem / 1.2 | 0 | Inside sheets |
| Body | Archivo 400 | 1.0625rem / 1.65 | 0 | The reading voice on vellum |
| Annotation / margin note | Archivo 400 italic | 0.875rem / 1.5 | 0 | `--ink-soft`; reads as pencilled-in |
| Readout (coordinates, nm) | Archivo 600 | 0.8125rem / 1.4 | 0.06em, uppercase | Tabular numerals; `--brass-deep` on vellum, `--brass-bright` on ink |
| Label / eyebrow | Archivo 700 | 0.6875rem / 1.3 | 0.14em, uppercase | Chart furniture labels |
| Table data | Archivo 400/600 | 0.9375rem / 1.5 | 0 | Tabular numerals throughout |
| Colophon | Cormorant Garamond italic 500 | 1.125rem / 1.5 | 0 | The footer signs in the display hand |

**Type laws.** (1) Coordinates always print in the readout style —
degrees, minutes, hemisphere, never bare decimals in prose.
(2) A distance is always "nm" in the readout voice, spelled "nautical
miles" once per page in body copy. (3) No headline exceeds two lines
at any breakpoint; a longer title is re-charted, not shrunk.
(4) Italic is Cormorant's native register — emphasis in display type
is a shift to italic, never to bold or colour. (5) The dead band:
no text between 1.125rem and 1.9375rem except the colophon — the
chart speaks either as annotation or as display, never as murmur.
(6) Figures in prose are spelled as the chart speaks them: a
bearing is "two-five-three" in a spoken context and 253° in print,
never "about 250-ish"; a distance under way is given to the tenth
of a mile in readouts and rounded only in Cormorant display lines,
where the readout beside it still carries the exact figure — the
display hand may summarise, the annotation hand may not.

## 4. Layout language

**The sheet stack.** The page is a stack of translucent vellum sheets
over a fixed star field. Sheets are `--vellum` at 94% opacity with a
1px `--vellum-deep` edge and a soft shadow (0 18px 40px at 12% ink);
the star field shows only at the page margins, in the hero, and in
the gaps between sheets — the sky is what the chart is laid *on*.
Sheets overlap the sheet above by 24px at ≥1200px, like paper squared
on a table, never floating in space with arbitrary gaps.

**The chart grid.** Content inside a sheet sits on a 12-column grid,
but its *placement* is charted: each section carries a coordinate
(its waypoint, §6.17) printed in its top corner, and the route (§6.2)
enters the sheet at the edge nearest the previous waypoint and leaves
toward the next. The route is drawn in the sheet's margin gutter
(64px at ≥1200px) — it never crosses body text. Whitespace is
*sea room*: the empty water around a plotted position, budgeted like
the navigator budgets clearance — generous (a minimum 96px of sheet
between sections), never filled with decoration to "balance" a page.

**Section choreography.** The page alternates: a full-bleed ink panel
(hero; footer) bookends vellum sheets; between sheets, a 120px band
of bare star field — the night between charts — where the route
crosses open sky and the compass rose (§6.4) is briefly the only
furniture. Density rule: one waypoint per sheet, one sheet per
viewport height at minimum; a section that needs two viewports gets
a sub-waypoint (a minor knot, §6.9) rather than a second sheet.

**Anatomy of a sheet.** Every sheet carries the same furniture in
the same places, so a reader learns the chart once and reads every
page by it: the waypoint coordinate in the top-right corner
(readout style, §6.3); a 1px brass head rule under the sheet's
title block; the route entering at the left gutter and leaving at
the right or bottom gutter, always in the gutter, never in the
measure; annotations in the right margin where the measure allows
(≥1200px) and folded beneath their paragraphs where it does not;
and the sheet's foot rule with its sub-waypoint soundings — the
minor marks of §4's density rule. A sheet missing its coordinate
or carrying its route through text is not a styling variant; it is
a mis-file, and §10 treats it as one.

**The fixed furniture.** Three instruments pin for the whole voyage:
the compass rose (bottom-right, §6.4), the margin progress readout
(right margin, §6.5), and the masthead (§6.11) which docks after the
hero. All three are DOM and CSS — none depends on the canvas or the
route's SVG — and all three keep working if every animation is off.

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scroll-scrubbed
value in the theme — route stroke, needle bearing, progress count,
parallax offsets — from a single lerped progress value `p`
(0 = departure, 1 = landfall) with lerp **0.09**: the *sextant-slow*
glide the original specifies. Nothing scroll-driven reads the raw
scroll position; everything reads `p`. Time-based ambient motion
(twinkle, rose ring, grain) runs on the same loop's clock so a
throttled tab throttles the whole room coherently.

**Named easings (the atelier's own).**
`--ease-sight` cubic-bezier(0.22, 0.61, 0.21, 1) — a sextant arc's
sweep: quick to start, patient to arrive. `--ease-plot`
cubic-bezier(0.3, 0.0, 0.2, 1) — line-drawing and reveals.
`--ease-settle` cubic-bezier(0.34, 1.25, 0.4, 1) — the 2px overshoot
settle of a locked fix. `--ease-drift` cubic-bezier(0.45, 0.05, 0.35, 1)
— grain, parallax lag, sheet turns. `--ease-knot`
cubic-bezier(0.6, 0.05, 0.2, 1.15) — the knot flourish's loop and
pull-tight.

**Every motion term, in this theme's language.**
- *Scroll-triggered reveals* — waypoint reveals on route arrival (§6.3): fade + 8px rise, 500ms `--ease-plot`, gated by the route, not by a bare observer.
- *Scroll-driven / scrubbed animation* — the great-circle route's stroke (§6.2), the needle's bearing (§6.4), the nm counter (§6.5): all functions of `p`, reversible, exact.
- *Parallax* — three translucent layers: star field at 0.96× scroll, vellum sheets at 1.0×, chart-ink annotations at 1.03× — a 7% total spread, felt as depth on a table, never as flight.
- *Pinned sections* — the hero sighting stage pins for 130vh while the fix is taken (§6.1); no other pinning — a chart room does not trap its reader.
- *Smooth scrolling* — the lerp on `p` (0.09) plus `scroll-behavior: smooth` for anchor jumps between waypoints; native wheel is never hijacked.
- *Progress indicator* — nautical miles sailed and to-next-waypoint (§6.5); the route itself is the bar.
- *Staggered reveals* — annotations stagger 70ms apart like pencilled notes (§6.3); catalogue cards stagger 60ms (§6.12).
- *Masked reveals* — the headline is sighted through the sextant's brass-rimmed circular mask (§6.1); brass-frame charts scale inside their frames (§6.7).
- *Blur-to-sharp* — refused for text (a chart is inked or it is absent); used only on the star field's depth layer, where distant stars sit 1px soft by design.
- *Kinetic typography* — refused. Headlines do not perform; they are *fixed* (§6.1) and then they hold still like ink.
- *Marquee* — refused. A chart room has no ticker; the log (§6.12's sibling entries) is read at the reader's pace.
- *Counters* — coordinate readouts count digit by digit (§6.3); the nm progress counts continuously (§6.5); every counter's final value is the record's printed value.
- *SVG line-draw* — the route (§6.2), triangulation lines (§6.1), sighting rules (§6.8), registration crosses (§6.10).
- *Image scale-in-frame* — charts settle 1.05 → 1.0 inside engraved brass frames (§6.7).
- *Hover / magnetic / tilt micro-interactions* — sighting hover (§6.8); cards tilt ≤3° like a chart under a magnifier (§6.12); magnetic effects refused — brass instruments are not drawn to a cursor.
- *Custom cursor* — refused, standing rule. The system cursor is the reader's own hand in the room.
- *Skeleton loading* — un-inked vellum outlines (§6.15).
- *Page transitions* — the registration-cross chart change (§6.10).
- *Reduced motion* — the full chart arrives drawn: route complete, needle at final bearing, no twinkle, counters printed (§12's promise, per-element variants in §6).

**Ambient loops — exactly two licensed.** The variable-star twinkle
(§6.6) and the compass rose's outer-ring rotation (§6.4), plus the
vellum grain drift (a 0.4%-opacity background-position wander on a
40s cycle, so slow it reads as paper breathing). Anything else that
moves on a timer is a defect (§9).

**Loop mechanics.** The loop runs only while the page is visible
and at least one driven value is unsettled or an ambient cycle is
live; it parks when the reader is at rest mid-page with all values
settled (the twinkle keeps it alive on ink panels, so in practice
it parks only on long vellum stretches — by design, since a parked
loop on a star panel would freeze the sky). `p` is computed from
scroll position as *charted distance*: the scroll fraction of each
leg's sheet is mapped through the record's cumulative table, so
one pixel of scroll on the long WP2→WP3 leg advances fewer
nautical miles than one pixel on the short WP0→WP1 leg — the
reader sails distances, not pixels. All scrubbed values are pure
functions of `p` or of the clock; there is no accumulated state to
drift, which is why reverse scrolling is exact everywhere in the
theme.

## 6. Signature elements

### 6.1 The sextant sighting

- **What & why.** The page opens by taking its own fix. A brass
  sextant arc sweeps ~40° across the hero star field; three real
  stars — Vega, Deneb, Altair, the Summer Triangle over the atelier
  on its founding night (§6.17) — brighten in sequence; thin brass
  lines draw from each toward a convergence — which, honestly, is
  never a point: the three lines close a small triangle, the
  navigator's *cocked hat*, printed at true scale beside the fix
  as the position's stated uncertainty — and the headline locks
  at the triangle's centre with a 2px settle, seen through the
  sextant's brass-rimmed circular mask. It belongs because the
  brand's first act is its method: the headline is a plotted
  position, established the way a navigator establishes anything —
  by sights, lines, and a fix you can check.
- **Structure.** One inline SVG overlaying the hero (viewBox
  1200×800): the arc (a 40° brass sector path, stroke `--brass`,
  1.5px), three star markers at the record's charted star positions,
  three triangulation lines (1px `--brass-bright`), and a fix marker
  — a small ring at the convergence. The headline is DOM text
  beneath a CSS circular mask (a `clip-path: circle()` on a wrapper,
  rimmed by an SVG ring in brass) that opens as the lines converge.
  The hero stage pins for 130vh; the sighting is scrubbed to the
  first 60% of that pin, then the stage releases and the voyage
  begins. All three stars and the fix are labelled in the SVG's
  `<desc>` for assistive technology.
- **Motion spec.** Trigger: load + the pinned scrub. Arc sweep:
  1200ms `--ease-sight` across 40°. Stars brighten in sequence,
  180ms apart, each a 300ms opacity/glow rise. Lines draw 900ms
  `--ease-plot`, staggered 120ms, from star toward fix. Mask opens
  0 → 340px diameter over 700ms `--ease-sight` as the third line
  lands; headline settles with a 2px overshoot, 240ms
  `--ease-settle`. Total ceremony ≈2.6s; a returning visitor within
  the same session gets the drawn state immediately (session flag),
  because a navigator does not re-take a fix he has already logged.
- **States.** Unsighted (arc parked, stars at field brightness,
  headline masked to a 120px peep) → sighting → fixed (arc resting
  at 40°, lines held at 40% opacity, mask fully open, headline
  locked) → scrolled-past (stage unpins; the fix marker remains as
  the hero's colophon-corner ornament).
- **Content merge.** The convergence point *is* the headline's
  position on the chart, and the fix printed beside it is the
  atelier's own (§6.17): remove the brand and there is nothing to
  fix. The three stars are the record's stars, named in the star
  table (§6.13) — the ceremony and the catalogue are one sky.
- **Failure fallback.** Watchdog at 3000ms from load: if the
  ceremony has not completed (JS stalled, pin unsupported), the
  hero snaps to the fixed state — mask open, lines drawn, headline
  printed. No-JS: the hero ships fixed; the script rewinds the
  mask and lines only in the same frame it arms the watchdog.
- **Reduced-motion variant.** The fixed state, printed: full
  headline visible, triangulation lines drawn at 40%, no sweep,
  no pin (the stage is a normal 100vh hero).
- **Performance budget & mobile variant.** One SVG, four animated
  properties, ≤0.3ms/frame from the shared loop. Mobile (<768px):
  the mask opens to 78vw, the arc sweep shortens to 28°, the pin
  shortens to 115vh; the sequence and the fix are unchanged.
- **Choreography timeline (v2).** t=0 load, watchdog armed →
  t=150ms arc begins its 40° sweep → stars brighten at t≈500 /
  680 / 860ms as the arc passes their bearings → lines draw
  t=900–1800ms, staggered → t≈1750ms third line lands, mask begins
  opening → t=2450ms mask full, headline settles 2px by t=2690ms →
  stage holds to 130vh scroll, then releases.
- **State matrix (v2).** *Rest (pre-load):* unsighted, headline
  present in DOM. *Hover:* none — the instrument works, the pointer
  watches. *Focus:* the hero's first link focuses normally; the
  sighting is `aria-hidden` decoration over printed content.
  *Active:* n/a. *Scrolled-past:* fixed state persists as ornament.
  *Disabled:* n/a. *Touch:* identical scrub on scroll; no pin-trap
  (the pin releases on scroll momentum as on desktop).
- **Breakpoints (v2).** ≥1200px: full ceremony, mask 340px, stage
  130vh. 768–1199px: mask 300px, arc 36°. <768px: mask 78vw, arc
  28°, stage 115vh, star markers enlarged to 5px for legibility.
- **Edge cases & failure modes (v2).** *Slow network:* the SVG is
  inline and the fonts are the only wait — the ceremony starts on
  DOMContentLoaded with system-serif fallbacks metrically matched
  (§3), never blocked on Cormorant's arrival. *Reader scrolls
  during the pin:* the scrub follows `p`; a fast scroll completes
  the fix early — latched, never replayed. *Browser without
  `clip-path: circle()`:* the mask wrapper falls back to a plain
  reveal (opacity), ceremony otherwise intact. *Tab hidden
  mid-ceremony:* on return, the watchdog has already fixed the
  hero; no half-sighted state is ever left standing.
- **Accessibility spec (v2).** The headline is real DOM text,
  readable from first paint — the mask is visual only and never
  removes content from the accessibility tree. The SVG carries
  `role="img"` and a label naming the three stars and the fix
  coordinates. No live-region announcements; the ceremony is
  ambient. Focus enters the hero's content in DOM order, mask or
  no mask.
- **Tokens consumed (v2).** `--ink`, `--vellum`, `--brass`,
  `--brass-bright`, `--ease-sight`, `--ease-plot`, `--ease-settle`,
  `--loop-lerp` (0.09), `--dur-sight` (1200ms), `--dur-triangulate`
  (900ms), `--dur-watchdog-sight` (3000ms).

### 6.2 The great-circle route

- **What & why.** A dashed brass route draws itself down the whole
  page — the great-circle course of Passage № 62 (§6.17) — scrubbed
  to scroll, running in the sheets' margin gutters and across the
  open-sky bands between them, knotting at each section-waypoint.
  It belongs because it is the page's argument made visible: this
  material is a voyage with an order, a distance and a destination,
  and the reader is on it. It is also the theme's progress
  indicator, its reveal trigger and its spine — three jobs, one line.
- **Structure.** One inline SVG spanning the page's full height
  (absolutely positioned, `preserveAspectRatio="none"` on a
  1440×10000 viewBox, path built at load from the record's waypoint
  anchor points by the script; the shipped DOM contains the
  *complete* path). The path is a smooth great-circle-arc
  approximation through the six waypoint anchors, dashed 7px/5px in
  `--brass` at 1.5px. Each waypoint carries a knot group (§6.9).
  Drawing is `stroke-dashoffset` driven from the shared loop's `p`,
  mapped through the record's cumulative distances so the line's
  head is always at the reader's true charted position.
- **Motion spec.** Trigger: scroll, via `p` (lerp 0.09). The drawn
  length equals `p × total path length`; because `p` maps through
  cumulative leg distances, the head moves at a constant *charted*
  speed — fast across long legs, slow across short ones — exactly
  as a pencil moves when plotting by distance. Reversal is exact:
  scroll up and the line un-draws along the same geometry (ink does
  not unwite in the log, §6.9, but the *pencil* route is a working
  line and may be re-plotted).
- **States.** Undrawn (below the fold — the course ahead) → drawing
  (head at the reader's position) → complete (at landfall, the full
  course drawn and held) → re-plotting (on upward scroll).
- **Content merge.** The route connects the actual sections in
  their actual order and its total length is the record's true
  course length; delete a section and the course, the readouts and
  the total all change together (§6.17). It is never a decorative
  squiggle: every bend is a leg between two printed coordinates.
- **Failure fallback.** Watchdog: if the loop has not ticked within
  2000ms of load, the path is set fully drawn. No-JS: fully drawn —
  the shipped dashoffset is 0 and the script is what rewinds it.
  A page printed from the browser shows the complete course (§14).
- **Reduced-motion variant.** The complete route, drawn from first
  paint; knots and readouts printed at final values.
- **Performance budget & mobile variant.** One dashoffset write per
  frame, ≤0.2ms. The path is re-measured on resize (debounced
  250ms). Mobile (<768px): the gutter narrows to 28px and the route
  hugs the left margin; dash pattern shortens to 5px/4px so the
  line stays legible at small scale.
- **Choreography timeline (v2).** Continuous: head position =
  `p × 1,228.3 nm` mapped onto path length → knot arrival fires
  §6.3's reveal and §6.5's "DIST TO NEXT" reset → at `p = 1` the
  head lands on the Horta knot, the final segment holds, and §6.16's
  colophon signs beneath a completed course.
- **State matrix (v2).** *Rest:* drawn to current `p`. *Hover:*
  none. *Focus:* none — the route is not interactive; its knots'
  log state is (§6.9). *Active:* n/a. *Scrolled-past:* segments
  above remain drawn (the wake of the voyage). *Disabled:* n/a.
  *Touch:* identical; `p` follows touch scroll through the same loop.
- **Breakpoints (v2).** ≥1200px: 64px gutters, route centred in
  them. 768–1199px: 44px gutters. <768px: 28px left margin,
  sections indent right of the line; the route never underlaps text
  at any size (the gutter is reserved in the grid, §4).
- **Edge cases & failure modes (v2).** *Content longer than the
  design expects:* extra sections join the course as sub-waypoints
  (minor knots) and the record's total grows — the mapping is
  data-driven, never hard-coded to six. *Anchor jump to the
  footer:* `p` lerps to its target over ~900ms, the line visibly
  plots at speed — a fast-forward sighting, not a teleport.
  *Resize mid-voyage:* path rebuilt from anchors, drawn fraction
  preserved by distance, not by pixels. *Print:* full course, §14.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the same
  information — where you are, what remains — is printed as text by
  §6.5's readout and each section's own coordinate (§6.3). The
  route never carries meaning that text does not.
- **Tokens consumed (v2).** `--brass`, `--vellum-deep`, `--ease-plot`,
  `--loop-lerp` (0.09), `--route-dash` (7px/5px), `--gutter-route`
  (64px), `--dur-watchdog-route` (2000ms).

### 6.3 Waypoint reveals

- **What & why.** Each section is a waypoint: as the route's head
  reaches its knot, the section makes landfall — content fades in
  rising 8px, and its coordinate readout counts up digit by digit
  and settles on the waypoint's true position from the record. It
  belongs because arrival is the theme's reveal grammar: a coast
  does not pop into existence at a viewport threshold, it *resolves*
  as your course reaches it. Tying the reveal to the route (not to
  a bare IntersectionObserver) is what makes the page one voyage
  rather than six animations.
- **Structure.** Each section is a `<section>` with
  `data-waypoint` (its record key), a readout element printing its
  coordinates, and content in the DOM complete from first paint.
  The hidden pre-state (opacity 0, translateY 8px) is applied by
  the script only (`data-armed`), in the same frame that registers
  the section with the loop and arms its watchdog. The readout
  counter is a text node updated by the loop during the count;
  its final string is the record's formatted coordinate.
- **Motion spec.** Trigger: the route head crossing the waypoint's
  cumulative distance (§6.2). Reveal: 500ms `--ease-plot`, fade +
  8px rise. Readout count: 700ms, digits rolling through
  intermediate values and settling right-to-left (minutes last,
  as a navigator writes a fix), ending exactly on the record's
  figures. Annotations inside the section stagger 70ms apart.
  Sections already passed on load (a restored scroll position)
  render revealed at final values — the log of a voyage resumed.
- **States.** Unreached (armed, pre-state) → arriving (revealing,
  counting) → reached (printed, readout settled) → scrolled-past
  (remains printed; the knot gains its wake state, §6.9).
- **Content merge.** The readout is the section's own charted
  position and the count ends on the record's numbers — the reveal
  *delivers information*, it does not decorate its delivery. A
  section with no honest coordinate does not get a readout; it
  gets a sub-waypoint knot and no figures (§1's law).
- **Failure fallback.** Per-section watchdog at 2600ms from arm,
  plus a global rule: any section within 120vh of the viewport
  that is still armed at any scroll stop is force-revealed. No-JS:
  nothing is ever armed; all sections print.
- **Reduced-motion variant.** Sections print as the route reaches
  them — instantly, at final values, readouts pre-settled. The
  gating (course order) survives; the motion does not.
- **Performance budget & mobile variant.** Reveal cost is CSS
  transitions on transform/opacity; the counter is one text write
  per frame per active section, ≤0.2ms. Mobile: rise shortens to
  5px, count to 500ms; stagger 50ms.
- **Choreography timeline (v2).** Route head reaches knot →
  t=0 section fade/rise begins → t=80ms readout count begins →
  t=500ms content at rest → t=780ms readout settled on the record's
  figures → annotations complete their stagger by t≈900ms →
  watchdog deadline t=2600ms passes unused.
- **State matrix (v2).** *Rest:* unreached or reached, per course
  position. *Hover:* §6.8's sighting applies to elements inside,
  independent of reveal state. *Focus:* if focus lands inside an
  unreached section (keyboard jump), the section force-reveals
  instantly — focus never enters invisible content. *Active:* n/a.
  *Scrolled-past:* printed, latched. *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full choreography. 768–1199px:
  stagger 60ms. <768px: rise 5px, count 500ms, stagger 50ms;
  readout sits above the heading instead of in the corner.
- **Edge cases & failure modes (v2).** *Reader scrolls back up
  past a waypoint:* reached sections never un-reveal (landfall is
  latched; only the pencil route re-plots, §6.2). *Very fast
  scroll to landfall:* sections reveal in course order in a
  compressed cascade (each 90ms after the last) — the voyage at
  speed, never a simultaneous pop. *Short content:* a section
  shorter than 40vh still gets its full reveal; the knot spacing
  is by distance, not pixels. *JS fails mid-page:* armed sections
  below the failure point are rescued by the global scroll-stop
  rule and the 2600ms watchdogs.
- **Accessibility spec (v2).** Content is in the accessibility tree
  at all times (the pre-state is opacity/transform only, never
  `visibility` or `display`). The counting readout is
  `aria-hidden` during the count with the final value in a
  visually-hidden sibling, so screen readers hear the settled
  coordinate once, not forty fragments. Reveal is never announced.
- **Tokens consumed (v2).** `--vellum`, `--ink`, `--brass-deep`,
  `--ease-plot`, `--loop-lerp` (0.09), `--dur-waypoint` (500ms),
  `--dur-count` (700ms), `--dur-watchdog-waypoint` (2600ms).

### 6.4 Compass-rose bearing

- **What & why.** A brass compass rose, ~90px, pins in the
  bottom-right corner for the whole voyage. Its needle is scrubbed
  to scroll bearing — page progress mapped to 0–360° — while the
  rose's engraved outer ring rotates almost imperceptibly on its
  own. It belongs because orientation is the navigator's constant
  companion: the instrument reads the reader's own heading through
  the chart, and at landfall the needle has made exactly one full
  turn — the voyage measured as a bearing come home.
- **Structure.** One inline SVG (viewBox 200×200): outer ring with
  32 point ticks and cardinal letters in Cormorant, an inner
  fleur-de-lis north mark, and the needle — a two-tone lozenge
  (`--brass` north half, `--ink` south) rotating about the centre.
  The ring's rotation is a CSS transform driven by the loop's clock;
  the needle's by `p`. A text alternative prints the current
  bearing in degrees beside the rose at ≥1200px ("BRG 147°").
- **Motion spec.** Needle: rotation = `p × 360°`, from the shared
  loop (lerp 0.09) — it swings with the sextant-slow glide and
  settles as the reader settles. Ring: one revolution per 240s
  linear — ambient loop № 2 (§5), slow enough to be noticed only
  by a reader who watches for it. At landfall (`p = 1`) the needle
  completes 360° and rests on north for 600ms before the colophon
  signs (§6.16).
- **States.** Departing (needle north) → under way (needle at
  bearing) → arrived (needle north again, ring still turning) →
  parked (tab hidden: both rotations pause with the loop).
- **Content merge.** The bearing is the reader's actual progress
  rendered as the instrument the whole theme is about; the printed
  BRG readout is the same number §6.5 expresses in miles. Remove
  the voyage and the needle has nothing to read.
- **Failure fallback.** If the loop dies, the needle rests at the
  bearing of the last computed `p` and the BRG text still prints —
  a stopped compass, honestly stopped, never spinning. No-JS:
  needle north, BRG text reads the course's initial bearing 253°
  (§6.17) as a printed label of the course, not of the reader.
- **Reduced-motion variant.** Needle steps to the bearing of the
  nearest waypoint only (six positions, no glide); ring rotation
  off. The instrument still reads; it no longer breathes.
- **Performance budget & mobile variant.** Two transform writes per
  frame, negligible. Mobile (<768px): the rose shrinks to 56px,
  the BRG text moves into the masthead's docked bar (§6.11), and
  the ring rotation is cut (battery and legibility) — needle only.
- **Choreography timeline (v2).** Continuous: needle angle tracks
  `p × 360°` with the 0.09 lerp → at each waypoint the needle
  crosses that leg's true initial bearing (§6.17) at the moment of
  arrival — 253°, 250°, 243°, 232°, 220° are passed in order →
  t=landfall: needle sweeps home to 360°/0°, holds 600ms.
- **State matrix (v2).** *Rest:* at current bearing. *Hover:* the
  rose brightens 8% and the BRG readout underlines — it is
  furniture that acknowledges a glance, nothing more. *Focus:* the
  rose is not focusable; its readout text is ordinary text.
  *Active:* n/a. *Scrolled-past:* n/a — it pins for the whole page.
  *Disabled:* n/a. *Touch:* no hover brightening; bearing identical.
- **Breakpoints (v2).** ≥1200px: 90px rose + printed BRG.
  768–1199px: 72px rose, BRG printed. <768px: 56px rose, BRG in
  the docked masthead, ring static.
- **Edge cases & failure modes (v2).** *Reader at the very top
  before JS arms:* needle north — which is also the true departure
  state, so the fallback is never wrong. *Reverse scroll:* the
  needle retraces its bearings exactly (it is a function of `p`,
  not an accumulating rotation). *Overlap with content:* the rose
  sits in the reserved corner gutter (§4) with `pointer-events:
  none` except its hover zone; it never covers a line of text —
  sheets slide beneath its translucent mount.
- **Accessibility spec (v2).** `role="img"`, label "Compass rose.
  Your bearing through this chart: [degrees] degrees", updated at
  most once per waypoint (not per frame) via a visually-hidden
  text node — orientation without chatter. Decorative ticks are
  `aria-hidden`.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`, `--ink`,
  `--vellum`, `--loop-lerp` (0.09), `--dur-ring` (240s),
  `--rose-size` (90px).

### 6.5 Nautical-mile progress

- **What & why.** In the right margin, the voyage's log-line:
  "SAILED 000.0 NM" counting with scroll, and beneath it "DIST TO
  NEXT WAYPOINT 55.8 NM" — the theme's progress indicator, measured
  in the voyage's own units against the record's true course length
  of 1,228.3 nm. It belongs because a percentage is a landsman's
  number; here, progress is distance over water, and the reader can
  feel a long leg (339.2 nm of open Atlantic between WP2 and WP3)
  in how slowly the next waypoint comes.
- **Structure.** A fixed margin block (DOM text, Archivo readout
  style): two labelled figures and, at landfall, a third line —
  "COURSE COMPLETE — 1,228.3 NM". Values are text nodes updated by
  the shared loop from `p` and the record's cumulative table. The
  block sits in the right margin gutter reserved in §4; on narrow
  screens it relocates into the docked masthead (§6.11) — the same
  DOM node, moved by CSS order, never duplicated.
- **Motion spec.** SAILED counts continuously with `p` (one decimal,
  tabular numerals, updated per frame from the lerped value, so it
  glides and settles like the needle). DIST TO NEXT decrements
  within the current leg and resets at each knot to the next leg's
  length from the record. No easing of its own — it inherits the
  loop's 0.09 lerp, which is the point: all instruments agree
  because all read one `p`.
- **States.** Departing (0.0 / 55.8) → under way (counting) →
  between waypoints after the last knot (DIST TO NEXT reads
  "— LANDFALL" once WP5 is the target) → arrived (COURSE COMPLETE
  line appears, vermilion tick, §6.9's log grammar).
- **Content merge.** Every figure is the record's arithmetic:
  SAILED = `p × 1,228.3`; leg lengths 55.8 / 235.3 / 339.2 / 316.7 /
  281.3 are printed identically in the table (§6.13) and the record
  (§6.17). The readout is the table, worn on the margin.
- **Failure fallback.** No-JS or dead loop: the block prints the
  course summary instead — "COURSE 1,228.3 NM · 6 WAYPOINTS" — a
  static label of the chart, never a frozen 0.0 pretending to be a
  live instrument.
- **Reduced-motion variant.** Figures update in whole nautical
  miles, only at waypoint crossings and at 10nm thresholds — a
  log entered at intervals, not a spinning counter.
- **Performance budget & mobile variant.** Two text writes per
  frame, ≤0.1ms. Mobile (<768px): the block compacts to one line
  ("412.6 NM · NEXT 218.4") in the docked masthead.
- **Choreography timeline (v2).** Continuous with `p` → knot
  crossing: DIST TO NEXT strikes through its zero for 200ms and
  resets to the next leg → landfall: SAILED settles on 1,228.3,
  holds, COURSE COMPLETE prints with its tick at +300ms.
- **State matrix (v2).** *Rest:* current figures. *Hover:* none.
  *Focus:* ordinary text, readable in place. *Active:* n/a.
  *Scrolled-past:* n/a — fixed furniture. *Disabled:* n/a.
  *Touch:* identical figures, compact line.
- **Breakpoints (v2).** ≥1200px: full two-figure block in the
  margin. 768–1199px: full block, narrower margin. <768px:
  one-line compact form in the masthead.
- **Edge cases & failure modes (v2).** *Rounding:* SAILED is
  rounded to 0.1nm for display from the unrounded product, so it
  lands on exactly 1,228.3 at `p = 1` — never 1,228.2 or 1,228.4
  (§10 audits this). *Jump scroll to the bottom:* the figures lerp
  up at the loop's pace, counting fast through the legs — the log
  catching up with the ship. *A leg edited in the record:* all
  figures follow; nothing is hard-coded.
- **Accessibility spec (v2).** The live figures are `aria-hidden`
  (a per-frame counter must not chatter); a visually-hidden status
  updates once per waypoint: "Waypoint 3 of 6 reached. 630.3 of
  1,228.3 nautical miles sailed." Contrast: `--brass-deep` on
  vellum 4.83:1 at readout size with 600 weight — passes as the
  large/semibold readout it is; the labels use `--ink-soft` 6.30:1.
- **Tokens consumed (v2).** `--brass-deep`, `--ink-soft`,
  `--vermilion`, `--loop-lerp` (0.09), `--course-total` (1228.3nm).

### 6.6 Variable-star twinkle

- **What & why.** The hero and inter-sheet bands show the actual
  night sky over the atelier's office (51°28.7′N 000°00.1′W) on its
  founding night, 22 October 1884 (§6.17) — some sixty stars plotted
  at their charted positions, each twinkling at its own period.
  Four are named variable stars whose true periods are printed in
  the star table (§6.13); their on-screen periods are those periods
  compressed into the visible band preserving rank order, and Algol
  gets its true signature — a sharp eclipse dip, not a sine. It
  belongs because the backdrop is a chart, not a wallpaper: its
  stars behave like the real ones the copy names.
- **Structure.** One inline SVG star layer per ink panel (hero;
  the inter-sheet bands reuse a cropped region of the same chart),
  ~60 circles at the record's plotted coordinates, radii 0.8–1.8px
  by magnitude, fill `--vellum`. Twinkle is per-star opacity driven
  by the shared loop's clock with each star's period and phase from
  the record's star table. The three sighting stars (§6.1) are the
  field's brightest and are excluded from idle twinkle while the
  sighting ceremony owns them. The chart is plotted for 21:00
  local time on the founding night: the Summer Triangle stands
  high in the west, the Square of Pegasus crosses the meridian in
  the south, the Plough rides low in the north, and the Milky
  Way's band runs from Cygnus down toward the southern horizon —
  the record's star table (§6.13) lists the field's named stars in
  the order a reader scanning west to east would meet them.
- **Motion spec.** Unnamed stars: sine-eased opacity 0.55–1.0,
  periods 1.7–3.4s assigned by magnitude (brighter = slower).
  Named variables, compressed periods: Algol 4.3s with a 600ms dip
  to 0.25 at each cycle's end (the eclipse); δ Cephei 5.1s smooth
  asymmetric rise/fall; η Aquilae 5.6s; ζ Geminorum 6.0s. No star
  ever reaches opacity 0 — a star dims; it does not blink out of
  its chart.
- **States.** Charted (resting brightness) → twinkling (the loop's
  steady state) → sighted (the three ceremony stars, §6.1) →
  printed (reduced-motion / no-JS: all at resting brightness).
- **Content merge.** The field is the record's sky: the same stars
  appear in §6.13's table with their true periods and magnitudes,
  and the hero's fix (§6.1) is taken on three of them. A build that
  swaps in random dots has broken the theme's checkable claim (§9).
- **Failure fallback.** The stars are static SVG — with no JS they
  simply shine at rest. There is no state in which the sky is
  missing; the ink panel ships with its stars printed.
- **Reduced-motion variant.** No twinkle. All stars at resting
  brightness; the printed sky. (The original's promise, kept
  verbatim in spirit: the full chart arrives drawn.)
- **Performance budget & mobile variant.** Opacity updates for ~60
  nodes per frame is the theme's most expensive ambient cost:
  capped at ≤0.8ms/frame, and stars are updated on a 3-frame
  stagger (each star every third frame — imperceptible at these
  periods). Mobile: field thins to ~36 stars (faintest third cut,
  §14's first cut), periods unchanged.
- **Choreography timeline (v2).** t=0 stars printed at rest →
  loop start: each star eases into its cycle from its record phase
  (no synchronised pulse — the field must never breathe as one) →
  Algol's first dip lands within its first 4.3s → steady state
  indefinitely; the sighting ceremony (§6.1) borrows its three
  stars and returns them to their cycles at the fix.
- **State matrix (v2).** *Rest:* printed brightness. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* bands above the
  viewport pause with the loop's visibility check. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full 60-star field. 768–1199px:
  48 stars. <768px: 36 stars, radii +0.2px for legibility.
- **Edge cases & failure modes (v2).** *Long tab suspension:* on
  return, phases resume from the loop clock — no catch-up burst.
  *A star's position colliding with sheet text:* the field lives
  only on ink panels and margins (§4); sheets are opaque enough
  (94%) that no star shows through body text. *Colour-vision
  safety:* stars differ by brightness and size, never by hue alone.
- **Accessibility spec (v2).** The field is `aria-hidden` in full;
  its information content (which sky, which stars) is carried by
  §6.13's table in text. Twinkle amplitudes stay far below any
  photosensitivity threshold (opacity range ≤0.45, no luminance
  flashes, largest star 1.8px).
- **Tokens consumed (v2).** `--ink`, `--vellum`, `--vellum-dim`,
  `--loop-lerp` (0.09), `--star-count` (60), `--dur-algol` (4.3s).

### 6.7 Brass-frame charts

- **What & why.** Every image on the page is a chart on the
  chart-room table: it sits inside an engraved brass frame, scales
  1.05 → 1.0 as it enters, and a registration cross draws in at each
  corner last — the print-shop mark that says this sheet is aligned
  and ready to be plotted from. It belongs because the atelier has
  no "media"; it has charts, plates and plates-in-progress, and the
  frame is what makes an image an instrument instead of an ornament.
- **Structure.** A `<figure>` with a real `<img>` (full `alt`,
  intrinsic dimensions, lazy below the fold), wrapped in a frame
  div: 1px `--brass` outer rule, 6px vellum mat, engraved corner
  ticks (CSS gradients), and four registration crosses as inline
  SVG strokes positioned at the corners, drawn by stroke offset.
  The caption prints beneath in annotation style with the chart's
  catalogue number from the record's plate list (e.g. "PLATE IV —
  THE SUMMER TRIANGLE, AS SIGHTED").
- **Motion spec.** Trigger: scroll into view (observer, threshold
  0.3). Image scale 1.05 → 1.0 over 800ms `--ease-drift`; the frame
  is still — the chart settles *inside* it. Crosses draw 250ms
  `--ease-plot` each, staggered 60ms in reading order (TL, TR, BL,
  BR), beginning at t=550ms so they land as the settle completes.
  No pan, no Ken Burns: a chart is examined, not flown over.
- **States.** Unentered (image at 1.05, crosses undrawn — applied
  by script only) → entering → registered (scale 1.0, crosses
  drawn, held) → scrolled-past (registered state persists).
- **Content merge.** The frame's caption is the chart's catalogue
  entry; the crosses are the same marks the page transition (§6.10)
  aligns by — one registration language from image to navigation.
  A decorative stock photo in a brass frame fails §9: plates must
  be charts, skies, instruments or the atelier itself.
- **Failure fallback.** Watchdog at 2000ms from arm: unentered
  figures snap to registered. No-JS: figures ship registered —
  scale 1.0, crosses drawn (they are strokes with dashoffset 0 in
  the shipped DOM; the script rewinds them when arming).
- **Reduced-motion variant.** Registered state at all times: no
  scale, crosses printed. The frame and caption carry the meaning.
- **Performance budget & mobile variant.** Transform on the image
  only (compositor), crosses are four small stroke animations;
  ≤0.2ms/frame while entering. Image budget per §14 (≤160KB,
  responsive srcset, WebP/AVIF). Mobile: scale range narrows to
  1.03 → 1.0, mat to 4px; crosses unchanged.
- **Choreography timeline (v2).** Figure crosses 0.3 visibility →
  scale begins → t=550ms crosses start, 60ms stagger → t=800ms
  scale settled → t≈1030ms last cross drawn → registered, held.
- **State matrix (v2).** *Rest:* registered. *Hover:* the frame
  brightens (brass to `--brass-bright` on ink panels, shadow
  deepens 4px on vellum) and §6.8's sighting rule draws beneath
  the caption. *Focus:* a linked figure's focus state is the same
  brightening plus the standard focus outline (§6.8). *Active:*
  n/a. *Scrolled-past:* registered. *Disabled (image failed to
  load):* the frame holds the caption and the chart's plotted
  outline (an SVG line version from the record) with the alt text
  printed as the caption's first line — an un-inked plate, never
  a broken-image icon. *Touch:* no hover brightening; registered
  on entry identically.
- **Breakpoints (v2).** ≥1200px: full frame, 6px mat. 768–1199px:
  5px mat. <768px: 4px mat, scale 1.03, crosses 10px (from 12px).
- **Edge cases & failure modes (v2).** *Very tall plate (a
  full-page chart):* the 0.3 threshold is computed on the figure's
  middle third so it registers progressively rather than waiting
  for its centre. *Two figures in one viewport:* §4's density rule
  forbids it on sheets; in the catalogue grid (§6.12) crosses cap
  their stagger at 4 concurrent draws. *Slow image:* the frame and
  caption print immediately; the image fades in inside the frame
  when it lands — the plate is catalogued before it is inked.
- **Accessibility spec (v2).** Real `alt` written as a chart
  caption ("Star chart of the Summer Triangle over Greenwich,
  22 October 1884, as plotted by the atelier"). Frame and crosses
  are `aria-hidden`. Caption contrast `--ink-soft` on vellum
  6.30:1.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--vellum`, `--vellum-deep`, `--ease-drift`, `--ease-plot`,
  `--dur-frame` (800ms), `--dur-cross` (250ms).

### 6.8 Sighting hover

- **What & why.** To attend to anything in the atelier is to take
  its bearing. Hovering (or focusing) a card, link or chart draws a
  brass rule beneath it — a 300ms stroke — and fades in a small
  coordinate tooltip giving the element's own chart position: the
  waypoint it belongs to and its offset on the sheet ("WP3 · SHEET
  42°N OF THE KNOT"). It belongs because it is the atelier's one
  gesture, applied to the page's own furniture: attention here is
  measurement, and the tooltip is information, not sparkle.
- **Structure.** The rule is a 1px `--brass` scaleX line under the
  element (transform-origin left, the navigator writes left to
  right). The tooltip is a DOM element in readout style on an
  `--ink` chip with `--vellum` text, positioned above the element,
  populated from the element's `data-sight` attribute (waypoint key
  + offset, both from the record's geometry at build time). One
  shared tooltip node serves the whole page.
- **Motion spec.** Rule: scaleX 0 → 1, 300ms `--ease-plot`.
  Tooltip: opacity 0 → 1 and 3px rise, 180ms `--ease-drift`,
  delayed 120ms so a passing cursor does not flash bearings at
  every element it crosses. On leave: rule retracts 200ms, tooltip
  fades 120ms. Focus triggers identically and instantly (no delay —
  a keyboard reader has already declared intent).
- **States.** Unsighted → sighting (rule drawing) → sighted (rule
  held, tooltip up) → released. On touch: first tap sights (rule +
  tooltip), second tap activates — on cards only; links and
  buttons activate on first tap and sight briefly in passing.
- **Content merge.** The tooltip's figures are the element's real
  chart position, computed from the same anchor geometry that
  builds the route (§6.2) — hover a catalogue card and you learn
  where on the course it sits. An element with no position gets no
  tooltip; chrome that cannot be sighted is not atelier furniture.
- **Failure fallback.** No JS: the rule becomes a CSS
  `:hover`/`:focus-visible` underline in `--brass-deep`; tooltips
  are enhancement only and their absence loses nothing the page
  needs. The script never hides link text behind a tooltip state.
- **Reduced-motion variant.** Rule and tooltip appear instantly
  (no draw, no rise); the delay is also removed — state changes
  are instant and complete.
- **Performance budget & mobile variant.** Transform/opacity only;
  one shared tooltip node; ≤0.1ms. Touch (<768px and coarse
  pointers): tooltips suppressed entirely (no hover to hold them);
  the rule still draws on tap-focus for cards.
- **Choreography timeline (v2).** Pointerenter → t=0 rule begins →
  t=120ms tooltip fades in (if the pointer is still present) →
  t=300ms rule complete → hold → leave: tooltip out 120ms, rule
  retracts by t=200ms after leave.
- **State matrix (v2).** *Rest:* unsighted. *Hover:* as above.
  *Focus:* instant sighted state + the visible focus outline
  (2px `--brass-deep` at 2px offset on vellum; `--brass-bright`
  on ink). *Active (pressed):* rule thickens to 2px for the press
  duration — the bearing is being *used*. *Scrolled-past:* a
  sighted element scrolled out releases immediately.
  *Disabled:* no rule, no tooltip; the element prints at 55%
  `--ink-soft` — unsighted because it cannot be sailed to.
  *Touch:* tap grammar as above.
- **Breakpoints (v2).** ≥1200px: full tooltip with waypoint +
  offset. 768–1199px: tooltip with waypoint only. <768px:
  tooltips off, rules on.
- **Edge cases & failure modes (v2).** *Tooltip near the viewport
  top:* flips below the element; near the right edge it anchors
  right — a bearing is never clipped by the chart's edge.
  *Rapid traversal of a card grid:* the 120ms delay plus a single
  shared node means one tooltip at a time, retargeted, never a
  flicker of six. *Element sighted while its section is still
  revealing (§6.3):* the sighting waits for the reveal's 500ms to
  finish — you cannot take the bearing of a coast still resolving.
- **Accessibility spec (v2).** The tooltip is `aria-hidden`; its
  content duplicates information printed in the section's readout
  (§6.3), so nothing is hover-only. Focus is always visible by the
  outline, independent of the rule. Tooltip text `--vellum` on
  `--ink` 11.83:1. Touch targets ≥44px regardless of rule length.
- **Tokens consumed (v2).** `--brass`, `--brass-deep`,
  `--brass-bright`, `--ink`, `--vellum`, `--ease-plot`,
  `--ease-drift`, `--dur-sight-hover` (300ms), `--dur-tip` (180ms).

### 6.9 Knot-tying click

- **What & why.** Clicking a section heading ties a knot on the
  route at that waypoint: the dashed line loops once in a 400ms
  flourish at the knot, and the waypoint's readout gains a
  vermilion "LOGGED" tick. It belongs because a navigator's chart
  is a working document — you mark your passage on it. The reader
  keeps a log of their own voyage, in the theme's rationed
  vermilion (§1's census), and the mark persists for the session.
- **Structure.** Each waypoint knot is an SVG group on the route
  (§6.2): a small circle at the anchor plus a loop path (a 14px
  teardrop loop) whose stroke draws on the tie. The LOGGED tick is
  a DOM element beside the section's readout — vermilion Archivo
  caps, 0.6875rem — toggled by class. State persists in
  `sessionStorage` (waypoint keys), so a reader who sails away and
  returns finds their log intact; it is never sent anywhere.
- **Motion spec.** Trigger: click (or Enter/Space) on the heading's
  knot button — the heading itself carries a real `<button>` styled
  as the heading text, so the gesture is keyboard-native. Loop
  draws 400ms `--ease-knot` (draw 280ms, pull-tight 120ms with the
  knot circle scaling 1.15 → 1.0). The tick fades in at t=300ms.
  Untying (second click) fades the tick and un-draws the loop in
  250ms — the log can be corrected, as logs are.
- **States.** Untied → tying → logged (loop drawn, tick printed) →
  untying → untied. A waypoint the route has not yet reached
  cannot be tied — its button is present but the knot refuses with
  a 150ms shake-free dimming and the note "NOT YET REACHED" in its
  readout: you cannot log a coast you have not made.
- **Content merge.** The log is kept on the chart itself, at the
  sections' own positions, and §6.5's readout gains a line when
  all six are tied: "LOG COMPLETE — EVERY WAYPOINT ENTERED". The
  interaction *is* the content's structure, marked by the reader.
- **Failure fallback.** No JS: headings are plain headings; no
  buttons, no ticks, nothing missing that the page needs.
  `sessionStorage` unavailable (private mode): the log works for
  the page view and simply does not persist — stated nowhere,
  apologised for nowhere; it is a pencil mark, not an account.
- **Reduced-motion variant.** The loop and tick print instantly in
  their final states. The refusal note still prints.
- **Performance budget & mobile variant.** One small stroke
  animation per tie; negligible. Mobile: the knot button's target
  is the full heading row (≥48px tall); the loop is drawn at 12px.
- **Choreography timeline (v2).** Click → t=0 loop begins drawing
  at the knot → t=280ms loop closed → t=280–400ms pull-tight,
  circle settles → t=300ms LOGGED tick fades in → state persisted
  by t=450ms.
- **State matrix (v2).** *Rest:* untied or logged, per session.
  *Hover:* §6.8 sights the heading; the knot circle brightens.
  *Focus:* knot circle gets the focus outline treatment (a brass
  ring at 2px offset in the SVG). *Active:* pull-tight fires on
  release (the tie completes as the click does). *Scrolled-past:*
  logged state persists. *Disabled:* unreached waypoints, as above.
  *Touch:* tap = click; the flourish is identical.
- **Breakpoints (v2).** ≥1200px: 14px loop in the gutter.
  768–1199px: 13px. <768px: 12px, tick moves beneath the readout
  (the margin is too narrow to hold it inline).
- **Edge cases & failure modes (v2).** *All six tied, then one
  untied:* the LOG COMPLETE line withdraws — the log is live, not
  a trophy. *Heading text edited in a CMS:* the button wraps the
  heading's text node, so the accessible name follows the edit;
  the waypoint key is the section's `data-waypoint`, unchanged.
  *Reader ties a knot, then jumps to the footer:* the tick and the
  readout line agree — both read the same session state.
- **Accessibility spec (v2).** The button's accessible name is
  "Log waypoint: [name]" / "Remove log mark: [name]"; its state is
  `aria-pressed`. The tick is text, not colour alone — it reads
  LOGGED. Vermilion at 3.91:1 on vellum is licensed here because
  the tick is large-caps semibold at the label size and is always
  paired with the loop's shape change — never colour-only.
- **Tokens consumed (v2).** `--brass`, `--vermilion`, `--ink-soft`,
  `--ease-knot`, `--dur-knot` (400ms), `--knot-size` (14px).

### 6.10 Registration-cross transition

- **What & why.** Changing pages is changing charts on the same
  table. On navigation, a fresh vellum sheet slides over the old;
  four registration crosses — one at each corner, the same marks
  that register the plates (§6.7) — align and flash vermilion for
  an instant as the sheets register; then the old sheet slides
  away beneath. It belongs because it makes the whole site one
  chart room: you never "leave" the atelier, you lay a new chart
  on its table, and the vermilion flash is the census's licensed
  spend for a completed act (§1).
- **Structure.** A transition layer (fixed, `aria-hidden`): a
  vellum sheet div with four inline-SVG crosses at its corners,
  animated by the router hook (or, on a plain multi-page build, by
  a click interceptor on internal links that plays the entry half
  and lets the destination page play the exit half from a session
  flag). The destination page ships with its own sheet already in
  place; the layer only ever *covers and uncovers*, it never holds
  content.
- **Motion spec.** Cover: sheet slides in from the right over
  450ms `--ease-drift`, crosses fade in as it lands. Register:
  crosses flash vermilion for 160ms at t=500ms (the single frame
  of vermilion — counted in the census). Uncover: the sheet slides
  left and away over 450ms `--ease-drift`, revealing the new page
  already printed beneath. Total ≤1,100ms, watchdogged at 2500ms:
  any stall forces the layer off.
- **States.** Idle (layer absent) → covering → registered (flash)
  → uncovering → idle. Back-button navigation plays the sequence
  in mirror (sheet from the left) — the chart you came from is
  re-laid from the side you left it.
- **Content merge.** The crosses are §6.7's marks at page scale,
  and the incoming sheet carries the destination's own first
  waypoint coordinate printed in its corner — you see where the
  new chart is before it fully lands.
- **Failure fallback.** Any failure — JS off, router absent,
  watchdog fired — is a plain navigation. The transition is pure
  enhancement layered over real links and real page loads; it can
  never strand a reader between charts (the layer is removed, not
  faded, on watchdog).
- **Reduced-motion variant.** No slide, no flash: instant
  navigation. The destination's corner coordinate still prints —
  the information survives, the ceremony does not.
- **Performance budget & mobile variant.** One transform on one
  layer; ≤0.2ms/frame. Mobile: the slide shortens to 320ms each
  way and the sheet enters from the bottom — a chart drawn up the
  table toward the reader.
- **Choreography timeline (v2).** Click → t=0 cover begins →
  t=450ms sheet landed, crosses in → t=500ms vermilion register
  flash (160ms) → navigation commits beneath the sheet →
  t≈700ms uncover begins → t=1150ms layer gone, new chart printed.
  Watchdog ceiling t=2500ms.
- **State matrix (v2).** *Rest:* layer absent. *Hover:* n/a.
  *Focus:* focus is never moved into the layer; on uncover, focus
  lands on the destination's skip link target as in a normal load.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled:* if the reader
  has reduced motion or the layer fails its self-check, the
  interceptor disarms itself for the session. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: side slide, crosses 16px.
  768–1199px: side slide, crosses 14px. <768px: bottom slide,
  crosses 12px, 320ms legs.
- **Edge cases & failure modes (v2).** *External links, downloads,
  mailto:* never intercepted. *A slow destination:* the sheet
  holds in the registered state with §6.15's un-inked outline of
  the incoming chart pulsing faintly — the wait is charted, not
  spinnered — until the 2500ms watchdog forces a plain load.
  *Double-click:* the second click is ignored while covering;
  the first navigation stands.
- **Accessibility spec (v2).** The layer is `aria-hidden` and
  `pointer-events: none` except while covering (when it blocks
  interaction for ≤1.1s, within the watchdog's guarantee). Screen
  readers experience an ordinary page change; the new page's
  `<title>` and heading announce as usual.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`,
  `--vermilion`, `--brass`, `--ease-drift`, `--dur-sheet` (450ms),
  `--dur-register` (160ms), `--dur-watchdog-transition` (2500ms).

### 6.11 Chart-room masthead & course navigation

- **What & why.** The masthead is the chart room's door plate: the
  atelier's name in Cormorant, and beneath it the course itself as
  navigation — the six waypoints by name, each a link that sails
  to its section, each carrying its coordinate in readout style.
  After the hero it docks to a slim bar (name, waypoint index,
  and — on mobile — §6.5's compact progress line). It belongs
  because in this theme navigation is not a menu of pages; it is
  the plotted course of this one, and the reader navigates the
  way the chart is sailed: by waypoint.
- **Structure.** A `<header>` with a real `<nav aria-label="Course">`:
  an ordered list of the six waypoint links (order = course order,
  from the record). Each link: waypoint name (Cormorant 600) +
  coordinate (Archivo readout). The current waypoint's link
  carries a small brass knot marker and `aria-current="location"`,
  driven by the same boundary table as §6.3's reveals — one source
  of "where am I" for nav, route and readouts. The docked bar is
  the same header, `position: sticky`, condensed by CSS.
- **Motion spec.** Entrance: the masthead prints with the hero
  (no separate animation — the door plate is hung before the
  sighting begins). Docking: as the hero's stage releases, the
  header condenses over 300ms `--ease-drift` (name shrinks to
  1.25rem, waypoint names collapse to their knots + coordinates,
  expanding on hover/focus). Current-waypoint changes crossfade
  the knot marker 200ms. No hide-on-scroll — the chart room does
  not hide its own index.
- **States.** Full (at the top) → docked (under way) → at landfall
  (the final waypoint's knot lit, the bar's right end carrying
  "COURSE COMPLETE" once §6.9's conditions and `p = 1` agree).
  A waypoint not yet reached prints its name in `--ink-soft`;
  reached ones in `--ink` — the index itself keeps the log.
- **Content merge.** The nav *is* the record's waypoint list —
  names, order and coordinates identical to §6.13's table and
  §6.17's record. Add a section and the index, the route and the
  table all gain a waypoint together, or the build fails §10.
- **Failure fallback.** No JS: the full masthead prints statically
  with all links working as anchors; docking and current-marking
  are enhancements. The current-waypoint logic has a 1000ms
  watchdog: if the observer never fires, WP0 is marked current —
  at the top of the page, that is never wrong.
- **Reduced-motion variant.** Docking is instant (the bar simply
  is condensed once past the hero); marker changes are instant.
- **Performance budget & mobile variant.** Sticky CSS + an
  IntersectionObserver; zero per-frame cost. Mobile (<768px):
  the docked bar holds the name, a "COURSE" button and §6.5's
  compact line; the waypoint list opens as a full-width vellum
  panel (the chart unrolled) with coordinates printed, 250ms
  `--ease-drift`.
- **Choreography timeline (v2).** Load → masthead printed → hero
  stage releases → header condenses 300ms → each knot crossing:
  previous link dims, new link's knot lights (200ms crossfade) →
  landfall: final knot lit + COURSE COMPLETE at the bar's end.
- **State matrix (v2).** *Rest:* current waypoint marked.
  *Hover:* §6.8 sights the link (rule + coordinate tooltip —
  the link's own coordinate, already printed, confirmed).
  *Focus:* sighting + outline. *Active:* `aria-current` link.
  *Scrolled-past:* n/a (sticky). *Disabled:* a waypoint whose
  section is unpublished prints knotless and unlinked, name at
  50% — a charted coast not yet surveyed. *Touch:* targets ≥44px;
  the panel's links are full-row.
- **Breakpoints (v2).** ≥1200px: full masthead, six links inline.
  768–1199px: six links inline, coordinates drop to the tooltip
  (names + knots printed). <768px: docked bar + COURSE panel as
  above; the full masthead still prints at the very top.
- **Edge cases & failure modes (v2).** *More than six sections:*
  sub-waypoints join the panel list but the inline bar keeps the
  six principal knots (§4's density rule) — the index abbreviates,
  the course does not break. *A section removed:* the boundary
  table is built from the DOM at load, so nav, route and readouts
  can never disagree with the page that exists.
- **Accessibility spec (v2).** Landmarks correct; skip link is the
  header's first element, printed `--vellum` on `--ink`. Link
  contrast: `--ink` on vellum 11.83:1; unreached names `--ink-soft`
  6.30:1 — state is carried by the knot marker and `aria-current`,
  never by colour alone.
- **Tokens consumed (v2).** `--vellum`, `--ink`, `--ink-soft`,
  `--brass`, `--brass-deep`, `--ease-drift`, `--dur-dock` (300ms).

### 6.12 Chart catalogue cards

- **What & why.** The catalogue — charts, plates, instruments for
  sale or study — is a grid of cards, and each card is a chart's
  catalogue entry: its plate in a small brass frame (§6.7's
  language at card scale), its name in Cormorant, its charted
  position in the readout voice, and its particulars in annotation
  style. On hover the card tilts ≤3°, like a chart lifting under a
  magnifier. It belongs because a catalogue in an atelier is an
  index of charts — handled, tilted to the light, and put back in
  order.
- **Structure.** A `<ul>` of `<li>` cards on `--vellum` sheets
  (the card ground is the page ground one shade deeper,
  `--vellum-deep` at 35% over `--vellum`, with a 1px brass rule at
  its head). Each card is an `<article>` wrapped in one link to
  the chart's detail page (§7). The plate image uses §6.7's frame
  at small scale. The card's position line prints the waypoint the
  chart belongs to and its catalogue number ("PLATE IV · WP3"),
  both from the record's plate list.
- **Motion spec.** Entry: cards rise with their section's waypoint
  reveal (§6.3), staggered 60ms in reading order. Tilt: driven by
  pointer position through the shared loop's lerped pointer values
  (rotateX/rotateY, max 3°, never raw pointer events — the chart
  floats on the loop's glide, not on the cursor's jitter); on
  leave it settles flat over 500ms `--ease-settle` with no
  overshoot past 0.2°. The plate's frame brightens 12% on hover.
- **States.** Rest: flat, in order. Hover: tilt ≤3°, frame
  brightened, §6.8's rule beneath the name. Focus: frame brightens
  and the rule draws; tilt does not follow keyboard focus (a chart
  does not tilt for a voice). Active (pressed): tilt flattens in
  100ms — the chart is taken up — then the link follows.
  Scrolled-past: flat print. Disabled: a chart out of print
  renders linkless, plate at 60%, labelled "OUT OF PRINT — CHART
  WITHDRAWN" in annotation style: the catalogue admits its gaps.
- **Content merge.** Every field is a catalogue field — plate,
  name, position, particulars — and the position ties the card to
  the course (§6.11's waypoints), so browsing the catalogue is
  also reading the chart of the page. §10 re-adds the catalogue
  against the record's plate list.
- **Failure fallback.** Tilt and stagger are loop/CSS driven; if
  the loop is dead the cards stand flat and printed, frames
  registered. No JS: identical, with CSS-only hover brightening.
- **Reduced-motion variant.** No tilt, no stagger — the grid
  prints as a block with its section; hover brightens the frame
  only.
- **Performance budget & mobile variant.** Tilt math is two lerped
  values on the one hovered card; plates are §6.7's images at card
  sizes (≤60KB each). Grid: 3 columns ≥1200px, 2 at 768–1199px,
  1 below 768px. Mobile: tilt off; tap sights the card (§6.8's
  touch grammar) and the link navigates on the same tap.
- **Choreography timeline (v2).** Section reveal → cards rise at
  60ms stagger → rest → pointer enters: frame brightens 200ms,
  tilt lerps to pointer angle, rule draws 300ms (§6.8) → leave:
  rule retracts, tilt settles 500ms.
- **State matrix (v2).** *Rest:* flat print. *Hover:* tilt ≤3°,
  frame +12%, rule. *Focus:* frame + rule, no tilt. *Active:*
  flatten 100ms, navigate. *Scrolled-past:* flat. *Disabled:*
  linkless, dimmed plate, OUT OF PRINT label. *Touch:* no tilt;
  tap = sight + navigate.
- **Breakpoints (v2).** ≥1200px: 3-col, tilt on. 768–1199px:
  2-col, tilt ≤2.5°. <768px: 1-col, tilt off, plate height 150px.
- **Edge cases & failure modes (v2).** *A catalogue of 60 charts:*
  pagination (§11) at 12 per page — the grid never grows past two
  viewports, and page changes are §6.10 chart changes.
  *A chart with no plate image:* the card prints its plotted
  outline (the record's SVG line version) in the frame — an
  un-inked plate, catalogued honestly. *Long names:* two-line
  clamp with the full name in the link's accessible name; the
  card's height is set by its grid row, never by its longest title.
- **Accessibility spec (v2).** One link per card with a single
  accessible name ("Plate IV, The Summer Triangle — chart,
  waypoint 3"); the plate's `alt` is empty inside the link (the
  name carries it) to avoid double announcement. Focus outline on
  the card, 2px `--brass-deep` at 3px offset. Text contrast: name
  `--ink` 11.83:1; particulars `--ink-soft` 6.30:1.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--ink`,
  `--ink-soft`, `--brass`, `--ease-settle`, `--ease-plot`,
  `--tilt-max` (3deg), `--loop-lerp` (0.09).

### 6.13 The waypoint & star table

- **What & why.** For the reader who wants the voyage plain: two
  true tables on one sheet. The waypoint table prints the course —
  waypoint, coordinates, leg distance, cumulative distance, initial
  bearing — with a totals row carrying 1,228.3 nm. The star table
  prints the charted sky — the named stars with magnitude, right
  ascension, declination, and for the four variables their true
  periods. It belongs because an atlas that cannot be read as
  tables is a painting; the tables are the theme's honesty made
  structural, and they are §10's audit surface: every figure the
  page performs elsewhere is printed here, still, to be checked.
- **Structure.** Two semantic `<table>`s with `<caption>`s, scoped
  headers, tabular numerals. Waypoint rows sit on alternating
  `--vellum` / `--vellum-deep` at 30% striping; the totals row is
  separated by a brass double rule and its figure set in
  `--brass-deep` (§3: brass-deep sets totals at text size). The
  star table's variable rows carry a vermilion-free marker — a
  brass asterisk — with the footnote: "Periods are the stars' own;
  on the chart they are compressed for the eye, rank order kept
  (§6.6)." Bearings print as three-figure degrees (253°).
- **Motion spec.** The tables do not animate — no reveal beyond
  their section's waypoint arrival (§6.3). Row hover lifts the row
  to `--vellum-deep` at 55% over 180ms `--ease-drift` and §6.8's
  rule draws at the row's margin. That restraint is the spec: the
  one element a hurried reader uses is the one that never performs.
- **States.** Rest: printed, striped. Hover (row): lift + rule.
  Focus: rows are not focusable; a row's detail link (waypoint
  name → its section) sights per §6.8. Active: n/a. Scrolled-past:
  printed. Disabled: a provisional row (a leg under re-survey)
  prints its figures in `--ink-soft` with a "PROVISIONAL" label —
  the table admits the state of its evidence.
- **Content merge.** The waypoint table *is* §6.17's record in
  reading order — same figures, same order, same total; the star
  table is the record's sky in catalogue order, and its first three
  rows are §6.1's sighting stars. Table, route, readouts and sky
  are four readings of one record.
- **Failure fallback.** None required — static HTML with a CSS
  hover. This element is the fallback's fallback: if every
  animation on the page fails, the tables still publish the whole
  voyage and the whole sky.
- **Reduced-motion variant.** Identical, minus the row-hover
  transition (instant lift) and the margin rule.
- **Performance budget & mobile variant.** Zero JS cost. Mobile
  (<768px): each table becomes a stacked list — waypoint blocks in
  definition-list layout, same order, same totals; no horizontal
  scroll is ever permitted (a table you must pan is a chart
  mis-filed).
- **Choreography timeline (v2).** Section arrival (§6.3, 500ms) →
  tables at rest → row hover: lift 180ms, rule 300ms (§6.8) →
  leave: release 200ms. Nothing else, ever.
- **State matrix (v2).** *Rest:* printed stripes. *Hover:* row
  lift + margin rule. *Focus:* cell link sighted. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* provisional rows labelled,
  as above. *Touch:* tap on a row lifts it for 500ms; links
  navigate normally.
- **Breakpoints (v2).** ≥1200px: both tables full width of the
  sheet's measure. 768–1199px: star table drops its RA column into
  the star-name cell as a sub-line. <768px: stacked lists.
- **Edge cases & failure modes (v2).** *A leg re-surveyed between
  editions:* the record changes, the table and every readout
  follow, and the previous figure is printed struck-through in the
  record's errata line (§6.17) — corrections never erase, in the
  tables as in the log. *Print:* the tables are the print
  stylesheet's centrepiece — full grids, no striping, ink on
  vellum-white.
- **Accessibility spec (v2).** Real table semantics with captions
  and scoped headers; the totals row is a `<tfoot>` with
  `scope="row"`. Contrast: `--ink` on vellum 11.83:1; totals in
  `--brass-deep` 4.83:1 at 600 weight; striping is decorative and
  contrast is computed against the lighter ground.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--ink`,
  `--ink-soft`, `--brass`, `--brass-deep`, `--ease-drift`.

### 6.14 Commission-a-chart form

- **What & why.** The atelier's conversion: a visitor commissions
  a chart — a passage planned, a sky plotted for a date, a plate
  drawn for a wall. The form is a sheet on the landfall section
  (WP5): fields for the commissioner's name, the passage or
  occasion, the waters or sky, and the date it is needed by. Its
  preamble prints the commission book's state from the record:
  "127 commissions entered in this book. Yours will be № 128." On
  submit, the confirmation is a book entry — "Entered as № 128" —
  and the route (§6.2) ties a fresh knot at the form's own position:
  the commission joins the voyage it was made on. It belongs
  because the conversion is transacted *inside* the theme's
  discipline: numbered, logged, derivable.
- **Structure.** A real `<form>` with native validation semantics,
  enhanced never replaced: labelled inputs on `--vellum`, ink text,
  2px focus outline in `--brass-deep` plus §6.8's sighting rule at
  the field's foot. The preamble number and the confirmation number
  both derive from the record's printed count (127) — the
  confirmation is a kept promise, not a surprise. Without JS the
  form posts to its endpoint and the confirmation is a
  server-rendered page with the same entry and the same number.
- **Motion spec.** Field focus: rule draws 300ms (§6.8); the
  field's ground warms to `--vellum-deep` at 20% over 200ms.
  Submit: the form dims to 65% over 250ms while the entry is
  written, the button showing §6.15's un-inked outline pulse —
  never a spinner. Success: the confirmation entry prints in with
  a 500ms `--ease-plot` rise; at t=300ms the route ties its knot
  at the form (400ms, §6.9's flourish, in brass — the vermilion
  tick is reserved for the reader's own log marks; the book's
  stamp is the atelier's seal in `--brass-deep`). Error: the
  field's label gains a brass-deep asterisk and its error line
  prints beneath in `--ink` — no shake, no vermilion (vermilion
  is for things logged, and an error is not yet a log entry).
- **States.** Rest: printed sheet, preamble showing № 128. Focus:
  per-field rule + warm. Active (submitting): form at 65%, button
  pulsing un-inked, fields disabled. Success: confirmation entry +
  knot tied + the book's count now reading 128 in the preamble's
  place ("128 commissions entered"). Error: field marked, error
  line printed, focus moved to the first error, values preserved.
  Disabled (endpoint down): the sheet prints a chart-room note —
  "The book is closed tonight; commissions resume at dawn" — and
  holds the visitor's words in the fields, unsent and unlost.
- **Content merge.** The form sits at landfall because a commission
  is what a voyage is *for*; its number derives from the record;
  its confirmation ties a knot on the reader's own route. Remove
  the record and the form cannot promise its number — §10 checks
  that it never tries.
- **Failure fallback.** Watchdog at 4000ms on submission: no
  response → the form restores from 65%, prints "the entry could
  not be written — your words are still here" with values intact;
  the submit carries an idempotency token so a retry can never
  enter the commission twice. Canvas/SVG failure changes nothing:
  the knot is the only casualty, and the printed entry stands.
- **Reduced-motion variant.** Confirmation prints instantly; the
  knot is drawn complete (no flourish). Errors print without
  transition.
- **Performance budget & mobile variant.** Form JS ≤5KB gz,
  deferred; the knot reuses §6.9. Mobile (<768px): single column,
  fields full measure, submit sticky at the sheet's foot within
  the form's own box; the preamble stays above the first field.
- **Choreography timeline (v2).** Focus → rule 300ms → submit →
  form dims 250ms → writing pulse → response → entry rises 500ms
  → t=300ms knot ties on the route (400ms) → confirmation at rest.
  Watchdog ceiling 4000ms.
- **State matrix (v2).** *Rest:* sheet printed, № 128 promised.
  *Hover:* field rules sight (§6.8). *Focus:* rule + warm +
  outline. *Active:* submitting state as above. *Scrolled-past:*
  the form waits; an in-flight submission completes regardless of
  scroll. *Disabled:* book-closed note, values held. *Touch:*
  identical; field targets ≥48px, submit full-width.
- **Breakpoints (v2).** ≥1200px: two-column sheet (passage +
  date side by side), measure 42rem. 768–1199px: single column,
  measure 36rem. <768px: single column full measure, sticky submit.
- **Edge cases & failure modes (v2).** *A date in the past:* the
  chart-room voice corrects without scolding — "That date has
  already made landfall; choose one still ahead of us" — and the
  value is kept for correction. *A duplicate commission (same
  name, passage, date):* the entry prints with a margin note,
  "second entry of this commission — corroboration, not
  duplication," and takes the next number; the book treats
  agreement as evidence. *Honeypot/bot fields:* styled as
  un-inked margin, never as vellum a human would write on.
- **Accessibility spec (v2).** Visible labels on every field
  (`--ink`, 11.83:1); errors use `aria-describedby` and an
  `aria-live="polite"` summary in the book's own words; the
  confirmation is an `aria-live` region announcing "Entered as
  № 128" once. Focus management: error → first invalid field;
  success → confirmation heading. The asterisk is paired with the
  printed words "correct this" — never mark alone.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--ink`,
  `--ink-soft`, `--brass`, `--brass-deep`, `--ease-plot`,
  `--ease-knot`, `--dur-watchdog-form` (4000ms).

### 6.15 Un-inked vellum — loader & skeleton

- **What & why.** Loading in the atelier is un-inked vellum:
  regions still arriving show the pale outline of the coming chart
  — a sheet's border, a plate's frame, a table's rules, drawn in
  `--vellum-deep` line at 40% with nothing yet inked inside — and
  as each region's content lands, it is inked in: lines deepen to
  brass and ink, and the content prints. It belongs because a
  spinner would be a machine in a room that has none; an un-inked
  sheet is the atelier in its dormant state — the same paper, not
  yet written on.
- **Structure.** Skeleton regions are DOM elements with
  `data-uninked`, styled as outline drawings of their own final
  boxes: a plate skeleton is a frame with corner crosses (§6.7's
  marks, un-drawn at 40%); a table skeleton is its rule grid; a
  card skeleton is the card's outline with its head rule. The
  inking is a class swap (`.is-inked`) that deepens the outlines
  over 400ms while the real content — already in the DOM or
  injected complete — prints beneath. The page transition (§6.10)
  reuses the language at full-sheet scale.
- **Motion spec.** Un-inked pulse: outlines breathe 40% ±6%
  opacity on a 3.2s sine — barely alive, clearly awaiting the pen.
  Inking on arrival: 400ms `--ease-plot`, content print rising
  simultaneously (300ms). Hard ceiling: any region still un-inked
  at 1500ms inks its content anyway — the atelier does not hold a
  reader hostage to a slow plate.
- **States.** Un-inked (pulsing outline) → inking → inked/printed
  (rest). Error (a region's data fails): the outline stays at 25%
  and the region prints its chart-room note ("this plate has not
  reached the table — [fetch it again]") with a real retry control.
  Focus: skeleton regions are unfocusable and `aria-hidden` until
  printed. Scrolled-past: regions below the fold ink on arrival
  regardless of visibility.
- **Content merge.** The skeleton is the coming content's own
  outline — shaped by its box, ruled by its grid — and the
  transition's held sheet (§6.10) shows the destination chart's
  outline, so even waiting is done on the record's geometry.
- **Failure fallback.** Watchdog per region at 1500ms (ink
  regardless) and §6.10's 2500ms on transitions. No JS: no
  skeletons exist; content is server-printed complete.
- **Reduced-motion variant.** No pulse: static outlines that swap
  to print instantly on arrival; transitions are plain navigations.
- **Performance budget & mobile variant.** Outlines are CSS
  borders/gradients — zero raster, zero per-frame JS. Mobile:
  pulse cut (static outlines) to save battery; ceiling unchanged.
- **Choreography timeline (v2).** Region requested → outline
  prints with the layout → data lands → inking 400ms, print rises
  300ms → region at rest. Ceiling 1500ms forces inking. Transition
  hold: outline of the incoming chart pulses until §6.10's
  watchdog or the load, whichever first.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* skeletons unfocusable, `aria-hidden`. *Active:*
  submitting regions (§6.14's button) show the un-inked pulse.
  *Scrolled-past:* pre-inked print. *Disabled / no-JS:*
  server print, no skeletons. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full outline detail (crosses,
  rules). 768–1199px: full, pulse period 3.6s. <768px: simplified
  outlines (border + head rule only), no pulse.
- **Edge cases & failure modes (v2).** *Data arrives before the
  outline paints (fast cache):* the region prints directly — an
  outline that never appears is the best kind. *Partial failure
  (2 of 3 catalogue rows land):* landed rows ink; the failed row
  holds its outline to the ceiling, then prints its note — the
  catalogue opens with the gap admitted. *Reader navigates
  mid-load:* the destination's own watchdogs own the landing.
- **Accessibility spec (v2).** Skeleton containers carry
  `aria-busy="true"` and are removed from the accessibility tree
  until inked; one polite announcement ("The chart is inked")
  fires when the last above-fold region prints — not one per
  region. The error note's contrast: `--ink` on vellum 11.83:1.
- **Tokens consumed (v2).** `--vellum-deep`, `--brass`, `--ink`,
  `--ease-plot`, `--dur-uninked-ceiling` (1500ms).

### 6.16 The colophon footer

- **What & why.** The page ends at landfall, and the footer is the
  colophon a chart carries in its corner: the atelier's name and
  its fix — the real coordinates of its actual office, printed to
  be checked — the course's totals in their third printing, the
  chart's edition line, and the sign-off in Cormorant italic. It
  belongs because a chart that does not say where it was made, by
  whom, and from what survey is not finished; and because the
  footer's coordinates resolving to a real place is the theme's
  anti-slop proof (§9), printed where a sceptic will look for it.
- **Structure.** An ink panel (`--ink` ground) in three columns at
  ≥1200px: (1) the atelier — name, office address, and the fix
  "51°28.7′N 000°00.1′W" in readout style with a link that opens
  the position on a public map; (2) the course — "PASSAGE № 62 ·
  FALMOUTH TO HORTA · 1,228.3 NM · 6 WAYPOINTS" and the per-leg
  figures in miniature; (3) the book — commissions entered (the
  record's 127, live-updated by §6.14), the edition line ("Chart
  № 62, third edition, corrected to 2026"), and the sign-off. The
  route (§6.2) terminates at the panel's top edge in the WP5 knot.
- **Motion spec.** The footer does not animate beyond its
  section's waypoint arrival (§6.3). One licensed moment: as `p`
  reaches 1, the needle (§6.4) comes home and the colophon's
  sign-off line — "Plotted, sighted and corrected by hand." —
  underlines itself with a brass rule, 600ms `--ease-plot`, once.
  A footer that performs more than its signature is showing off.
- **States.** Unreached → reached (printed, totals at final
  values) → signed (rule drawn, once per session; a returning
  reader finds it already signed — the chart in the room is a
  finished object).
- **Content merge.** Every figure is the record's third printing:
  total, legs, fix, book count — §10 audits the footer against
  §6.13 and §6.17 figure for figure. The map link makes the fix
  falsifiable, which is the point of printing it.
- **Failure fallback.** Static HTML on an ink panel; there is
  nothing to fail. The signature rule is a CSS class on a printed
  line.
- **Reduced-motion variant.** The sign-off prints already
  underlined. Everything else identical.
- **Performance budget & mobile variant.** Zero ongoing cost.
  Mobile: columns stack — atelier, course, book — and the fix
  stays in the first screenful of the footer; a landfall you must
  scroll to find is a harbour missed.
- **Choreography timeline (v2).** Route head lands on WP5 →
  section reveal (500ms) → needle completes its turn (§6.4) →
  t=+300ms COURSE COMPLETE in §6.5 → sign-off rule draws 600ms →
  the chart is finished.
- **State matrix (v2).** *Rest:* printed colophon. *Hover:* links
  sight per §6.8 (rule + tooltip in the ink-panel colours).
  *Focus:* as hover + `--brass-bright` outline. *Active:* n/a.
  *Scrolled-past:* signed state persists. *Disabled:* n/a.
  *Touch:* links full-row in their columns.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns (book beneath atelier). <768px: stacked, fix first.
- **Edge cases & failure modes (v2).** *The office moves:* the
  record is edited, the fix changes everywhere at once (hero,
  footer, table), and the edition line increments — a chart
  corrected is a chart re-issued, and the colophon says which
  edition the reader holds. *The map link's service is down:* the
  coordinates still print; the fix is checkable by any atlas, the
  link is a courtesy.
- **Accessibility spec (v2).** Footer landmark; the fix is text
  (not an image of coordinates). Contrast on ink: `--vellum`
  11.83:1, `--vellum-dim` 8.41:1, `--brass-bright` 5.65:1 for the
  readout lines.
- **Tokens consumed (v2).** `--ink`, `--vellum`, `--vellum-dim`,
  `--brass-bright`, `--ease-plot`, `--dur-sign` (600ms).

### 6.17 The chart record — the one source of every figure

- **What & why.** The record is the theme's declared data object:
  Passage № 62, the atelier, its sky and its book, written once and
  read by every element. It is specified as an element because in
  this theme the record *is* a page component — it prints in full
  as the chart's own sheet (reachable from the colophon, and
  rendered in §6.13's tables), and every other element is a view of
  it. If a figure appears anywhere on the page and is not in this
  record or derived by a printed rule, the build has failed §1's law.
- **Structure.** One structured object (JSON in the build, a
  printed sheet in the DOM) with five blocks. **The atelier:**
  Celestial Navigation Atelier, Greenwich, London; fix
  51°28.7′N 000°00.1′W; founded 22 October 1884 — the day the
  Meridian Conference adopted the meridian its office stands on.
  **The course** (initial bearings and great-circle distances,
  computed from the coordinates by the haversine rule printed in
  the record's margin): WP0 Departure, Falmouth roads —
  50°08.9′N 005°03.9′W — leg —, cum 0.0; WP1 Bishop Rock abeam —
  49°52.2′N 006°26.7′W — leg 55.8, cum 55.8, bearing 253°; WP2 The
  Soundings — 48°24.0′N 012°00.0′W — leg 235.3, cum 291.1, bearing
  250°; WP3 The Long Swell — 45°36.0′N 019°12.0′W — leg 339.2, cum
  630.3, bearing 243°; WP4 The Trade Road — 42°12.0′N 024°48.0′W —
  leg 316.7, cum 947.0, bearing 232°; WP5 Landfall, Horta, Faial —
  38°31.9′N 028°37.7′W — leg 281.3, cum 1,228.3, bearing 220°.
  **Total course: 1,228.3 nm** (55.8 + 235.3 + 339.2 + 316.7 +
  281.3). **The sky:** the field over the fix on the founding
  night; sighting stars Vega (RA 18h36m56s, Dec +38°47′01″, mag
  0.03), Deneb (20h41m26s, +45°16′49″, 1.25), Altair (19h50m47s,
  +08°52′06″, 0.76); named variables Algol (P 2.867d, eclipsing),
  δ Cephei (5.366d), η Aquilae (7.177d), ζ Geminorum (10.150d).
  **The book:** 127 commissions entered; the form's next is № 128.
  **The plates:** the catalogue's list, §6.12's source — Plate I,
  The Founding Sky (WP0); II, The Sextant, Divided (WP0); III,
  Falmouth Roads at Dawn (WP0); IV, The Summer Triangle, as
  Sighted (WP1); V, Bishop Rock, Abeam at Dusk (WP1); VI, The
  Soundings, Sheet A (WP2); VII, A Page of the Star Catalogue
  (WP3); VIII, The Long Swell, Sea State (WP3); IX, The Trade
  Road, Wind Roses (WP4); X, The Log, One Week Kept (WP4); XI,
  Horta Roads, Landfall (WP5); XII, The Colophon Chart (WP5).
  Twelve plates, two per waypoint; the catalogue's count, the
  cards' position lines and the detail pages' "neighbouring
  charts" all read this list and no other.
- **Motion spec.** None. The record does not move; everything else
  moves *by* it. Its printed sheet reveals with its section like
  any other (§6.3) and that is all.
- **States.** Current edition → corrected (a figure amended: the
  old value is kept, struck through, with the correction dated —
  the record's errata line) → re-issued (edition increments,
  §6.16). There is no draft state visible to readers.
- **Content merge.** Total by construction: route geometry (§6.2),
  readouts (§6.3, §6.5), needle bearings (§6.4), star field (§6.6),
  tables (§6.13), form numbers (§6.14), footer figures (§6.16)
  and nav (§6.11) all read this one object.
- **Failure fallback.** The record prints as a static sheet; if
  the script that distributes it fails, the page's figures are
  still all present in their DOM printings (each element ships its
  final values, §6.3) — the record is the source at build time,
  not a runtime dependency.
- **Reduced-motion variant.** Identical — it is print.
- **Performance budget & mobile variant.** One small object
  (≤4KB); its printed sheet stacks like §6.13's tables on mobile.
- **Choreography timeline (v2).** None of its own. Its figures'
  timelines are the elements' timelines (§6.1–§6.16), each ending
  exactly on the values printed here — the audit in §10 walks
  them in this order.
- **State matrix (v2).** *Rest:* current edition printed.
  *Hover/focus/active:* as a sheet of tables (§6.13's grammar).
  *Scrolled-past:* printed. *Disabled:* n/a. *Touch:* stacked
  print, as §6.13.
- **Breakpoints (v2).** The printed sheet follows §6.13's table
  breakpoints exactly.
- **Edge cases & failure modes (v2).** *A figure disputed (a
  reader's own GPS disagrees with a leg):* the record prints its
  method (haversine on the printed coordinates, mean earth radius
  3,440.065 nm) so the disagreement can be recomputed, not argued.
  *Rounding:* legs print to 0.1 nm from unrounded values; the
  printed legs sum to the printed total exactly (55.8 + 235.3 +
  339.2 + 316.7 + 281.3 = 1,228.3) — if an edit breaks that
  identity, §10 blocks the build. *A waypoint added:* bearings
  and cumulatives are recomputed by the printed rule, never typed.
- **Accessibility spec (v2).** The sheet is ordinary semantic
  tables and text (§6.13's spec); the struck-through errata values
  are marked with `<del>` and the corrections with `<ins>`, so
  the record's history is legible to assistive technology too.
- **Tokens consumed (v2).** `--vellum`, `--ink`, `--ink-soft`,
  `--brass-deep`, `--course-total` (1228.3nm).

### 6.18 Uncharted waters — the 404

- **What & why.** Where the chart runs out — a URL with no sheet, a
  search with no chart — the page says so in the atelier's voice:
  a vellum sheet whose route simply stops at its edge, the water
  beyond printed blank, and the line "THIS WATER IS NOT ON OUR
  CHART" with the way back plotted as real links (return to
  departure, open the catalogue, commission a chart — an uncharted
  need is a plausible reason to be lost). It belongs because
  absence is a charting result: the atelier records what it has
  not surveyed rather than pretending the sea is full.
- **Structure.** A sheet (the 404 page's whole body) with the route
  (§6.2's SVG grammar) drawn entering from the top-left and ending
  mid-sheet in an unterminated dash and a small brass "?" at the
  last plotted position; beyond it, blank vellum with the faintest
  grid of un-inked rhumb lines (§6.15's language at rest). The
  statement prints in Cormorant, the exits as a waypoint list in
  §6.11's style with their coordinates. The empty-search variant
  reuses the sheet inside the catalogue section (§6.12) at panel
  scale.
- **Motion spec.** On load, the route draws to its end (700ms
  `--ease-plot`) and stops — the one place in the theme where the
  line's stopping is the message. The "?" does not bounce, pulse
  or perform. Nothing else moves; uncharted water is still.
- **States.** Uncharted (the only state) → departed (any exit link,
  via §6.10's transition). The empty-search variant clears the
  moment a search matches again — the water is charted after all.
- **Content merge.** The stopped route is the site's own course
  line, and the exits are real waypoints with real coordinates —
  the reader is re-plotted, not apologised at. The blank beyond
  the line is §4's sea room with its meaning inverted: not
  clearance around a position, but the absence of one.
- **Failure fallback.** Static sheet; the drawing is a shipped
  complete SVG (the stop is drawn, not animated, in the DOM). No
  JS required for anything on the page.
- **Reduced-motion variant.** Identical, minus the 700ms draw —
  the route prints already stopped.
- **Performance budget & mobile variant.** One small SVG; zero
  ongoing cost. Mobile: the sheet's route enters from the top and
  stops at 40% height; exits stack full-width below.
- **Choreography timeline (v2).** Load → route draws 700ms to its
  end → stop → the statement and exits are already printed beneath
  (they never wait for the line) → rest.
- **State matrix (v2).** *Rest:* uncharted print. *Hover:* exit
  links sight per §6.8. *Focus:* as hover + outline; the first
  exit is the page's natural first focus after the skip link.
  *Active:* n/a. *Scrolled-past:* n/a (one sheet). *Disabled:*
  n/a. *Touch:* exits are full-row targets ≥48px.
- **Breakpoints (v2).** ≥1200px: full sheet, route stops at 55%
  width. 768–1199px: stops at 50%. <768px: stops at 40% height,
  exits stacked.
- **Edge cases & failure modes (v2).** *A mistyped URL one letter
  from a real chart:* the sheet may print "NEAR THIS WATER:
  [chart name]" as a fourth exit — a nearest-coast suggestion,
  computed from the catalogue, never a guess dressed as fact; if
  no chart is near, the line is absent. *Search with results that
  fail to load:* that is §6.15's error note, not this sheet — the
  atelier distinguishes "not charted" from "not yet inked".
- **Accessibility spec (v2).** The 404 page's `<h1>` is the
  statement itself; HTTP status is a real 404. The stopped route
  is `aria-hidden` with the statement carrying its meaning in
  text. Contrast throughout per §6.13's table values.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--ink`,
  `--brass`, `--brass-deep`, `--ease-plot`, `--dur-stop` (700ms).

## 7. Page application map

- **Home (the passage).** The full voyage as specified: hero fix
  (§6.1), route (§6.2), six waypoint sheets — charts (§6.12),
  instruments, the tables (§6.13), the log, the commission form at
  landfall (§6.14) — colophon (§6.16). This is the theme's native
  page; every other page type is a single chart from the same atlas.
- **Listing (the catalogue).** §6.12's grid at full scale with
  §6.15's inking and §6.18's empty sheet for empty results. The
  route enters at the page's head as a short plotted approach and
  exits at the foot — a listing is a waypoint you pass through, so
  its route segment is drawn complete, not scrubbed (the reader is
  browsing a chart, not sailing a passage).
- **Detail (a single chart).** One plate large in its brass frame
  (§6.7), its catalogue entry as the sheet's table, its waypoint
  printed in the corner, and "NEIGHBOURING CHARTS" — the plates
  before and after it in the record's list — as the foot's two
  exits, plotted as a two-leg mini-route. The commission form
  (§6.14) appears in its compact one-column form.
- **About (the atelier itself).** The founding sheet: the office
  fix, the founding night's sky (§6.6 at panel scale), the
  atelier's own log entries as §6.12-style cards, and the record
  (§6.17) printed in full — the about page is where the theme
  shows its workings.
- **Contact / commission.** §6.14's form as the whole page, on the
  landfall sheet, with the book's preamble and the office fix
  printed beside it. No separate "contact info" chrome: the fix
  and the form are the contact.
- **Checkout equivalents.** A paid commission's payment step leaves
  the chart room deliberately: the sheet prints "THE BOOK PASSES
  TO THE COUNTING HOUSE" and hands off to a plain, fast payment
  page in the client's base system. The atelier does not plot
  courses through card fields — pretending otherwise would break
  the law's spirit (no figure without its fix) and the reader's
  trust at the exact moment money moves.
- **404 / empty.** §6.18, as specified.

## 8. Worked examples

### 8.1 The hero — the fix is taken (worked example 1)

The reader lands on an ink panel: the founding night's sky (§6.6),
stars at rest, the masthead (§6.11) printed above, the headline
masked to a 120px peep at the chart's centre. t=150ms the sextant
arc begins its 40° sweep (§6.1). As it passes their bearings, Vega,
Deneb and Altair brighten in turn; at t=900ms the first brass line
draws from Vega toward the convergence, then Deneb's, then
Altair's. At t≈1750ms the third line lands on the fix —
51°28.7′N 000°00.1′W, printed in readout style as it is struck —
the circular mask opens, and the headline ("Positions, honestly
come by.") locks in with its 2px settle. Beneath it, the annotation
staggers in: "The Celestial Navigation Atelier — charts, passages
and skies, plotted by hand in Greenwich." The route (§6.2) leaves
the hero's foot toward WP0. The reader scrolls; the stage holds to
130vh, the needle (§6.4) leaves north, §6.5 reads SAILED 000.0 NM,
DIST TO NEXT 55.8 NM. Every figure on screen is in §6.17; the
ceremony took 2.7 seconds and can be re-derived from the record by
any reader with an atlas.

### 8.2 Mid-page — the tables at WP3 (worked example 2)

Halfway down the passage, the route's head crosses 630.3 nm and
knots at WP3, The Long Swell. The sheet (§6.3) makes landfall:
heading rises, its readout counts and settles on 45°36.0′N
019°12.0′W. On the sheet, §6.13's two tables print the voyage and
the sky, still and complete — the reader who has been watching
instruments now reads the figures at rest: leg 339.2 nm just
sailed (the course's longest), cumulative 630.3, the needle having
crossed bearing 243° at the knot. A reader who distrusts the
margin counter checks it against the totals row: 1,228.3 nm, the
same number the hero's course promised and the footer will sign.
Below the tables, the star table's footnote explains the twinkle's
compression — the theme confessing its one licensed liberty, in
print, at the exact place a sceptic would look.

### 8.3 Conversion — a commission enters the book (worked example 3)

At landfall (WP5, Horta — 38°31.9′N 028°37.7′W), beneath the
arrivals board of §6.12-style log cards, the commission sheet
(§6.14) prints its preamble: "127 commissions entered in this
book. Yours will be № 128." The reader writes: a passage, Falmouth
to Horta, for a September crossing — the very course they have
just sailed down the page, which is the theme's quiet argument
made literal. Each field sights as it is focused (§6.8). On
submit, the sheet dims, the button pulses un-inked, and the entry
prints: "Entered as № 128 — Falmouth to Horta, September
crossing." At t=300ms the route ties a fresh knot at the form's
position. The book now reads 128. The number was promised before
the reader wrote a word, derived from the record in print, and
kept — the conversion works because the atelier's arithmetic has
been checkable for the entire voyage.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Random star fields.** Dots scattered by a randomiser read as
   wallpaper within a second. Cure: the record's plotted sky (§6.6)
   — real positions, named stars, a checkable claim.
2. **Fake coordinates.** "51.5074° N" typed from imagination, or
   coordinates that resolve to a car park in the wrong ocean.
   Cure: the record (§6.17); every printed position recomputed
   from it; the footer's fix opens on a real map.
3. **A route that decorates.** A wavy line that connects nothing,
   crosses text, or has no distances. Cure: §6.2's geometry is the
   record's legs; the gutter is reserved; the head moves by
   charted distance.
4. **Vermilion everywhere.** The signal colour used as a general
   accent destroys the census and the calm. Cure: §1's ration —
   logged ticks, the register flash, nothing else; §10 greps it.
5. **Pirate cosplay.** Skulls, treasure-map burns, "ahoy" copy,
   parchment textures with coffee stains. The atelier is an
   instrument room, not a theme park. Cure: §12's voice rules;
   vellum is flat, clean and translucent — paper, not a prop.
6. **Compass rose as clip-art.** A stock rose pasted in a corner,
   needle static or spinning freely. Cure: §6.4 — the needle reads
   `p`, the bearings it crosses are the record's true leg bearings.
7. **Counters that land wrong.** A count settling on 1,228.2 or
   "1,228+" against a printed 1,228.3. Cure: §6.5's rounding rule
   and §10's three-printings audit.
8. **Twinkle as glitter.** All stars pulsing together, or blinking
   to zero. Cure: per-star periods and phases from the record,
   opacity floor 0.25–0.55, the 3-frame stagger (§6.6).
9. **Tilt on everything.** Cards, tables and text all leaning at
   the cursor. Cure: tilt lives only on catalogue cards (§6.12),
   ≤3°, loop-lerped; tables never tilt (§6.13).
10. **The route as progress-bar cosplay.** A percentage hidden in
    nautical costume. Cure: the nm figures are the record's real
    legs — the long WP2→WP3 leg must *feel* long (§6.5).
11. **Headline kinetic type.** Letters dancing in a chart room.
    Cure: §5's refusal — the headline is fixed once, by sights,
    and then holds like ink.
12. **Sheets as glassmorphism.** Frosted blur panels with neon
    edges — a different decade's fashion wearing vellum's name.
    Cure: §4 — flat translucent paper, ink edges, no backdrop blur
    anywhere in the theme.
13. **GPS-blue chrome.** Saturated blue links, blue focus glows,
    map-app pins — the satellite age leaking into a chart room.
    Cure: §2 has no blue at all; focus is brass-deep, links are
    ink with §6.8's rule, and the only "pin" is a plotted knot.
14. **The sextant as logo clip-art.** A decorative sextant doodle
    in the header that never sights anything. Cure: the sextant
    exists in this theme only as §6.1's working ceremony; an
    atelier mark, if one is needed, is the knot — the mark the
    reader themselves ties.

## 10. Quality gate

Blocking checks; every one must pass before the theme ships in a
build, signed by someone who did not build the page.

1. **Figure audit.** Every number printed or counted anywhere —
   hero fix, readouts, counters, tables, footer — matches §6.17
   exactly; the legs sum to the total (55.8 + 235.3 + 339.2 +
   316.7 + 281.3 = 1,228.3) in all three printings.
2. **Fix check.** The footer coordinates open on a public map and
   land on the atelier's actual office.
3. **Vermilion census.** Grep the build: vermilion appears only in
   §6.9's LOGGED ticks, §6.10's register flash, and §6.5's COURSE
   COMPLETE tick. Any other occurrence blocks.
4. **Watchdog drill.** With the loop killed, every section prints
   within its watchdog (route 2000ms, waypoints 2600ms, sighting
   3000ms, frames 2000ms, form 4000ms); no content is ever stranded.
5. **No-JS read.** JavaScript disabled: the whole page reads in
   order, route drawn, counters at final values, form submittable.
6. **Reduced-motion pass.** With `prefers-reduced-motion`: no
   twinkle, no sweep, no tilt, no slide; the chart arrives drawn
   and complete.
7. **Needle audit.** At each waypoint crossing, §6.4's printed BRG
   equals the leg's record bearing (253 / 250 / 243 / 232 / 220).
8. **Counter landing.** §6.5's SAILED settles on exactly 1,228.3
   at `p = 1` — never 1,228.2, never 1,228.4.
9. **Star check.** The field's named stars match §6.17's table in
   position, magnitude order and period rank; Algol dips, the
   others breathe.
10. **Tilt & cursor audit.** Tilt exists only in §6.12 at ≤3°;
    the cursor is the system cursor everywhere.
11. **Contrast audit.** Text pairings meet §2's rulings (brass
    never text on vellum; vermilion never body text).
12. **Form promise.** The preamble's № (record count + 1) equals
    the confirmation's № on a test submission, and a failed
    submission loses no input.

## 11. Component inventory

Every component a real atelier site needs, with its treatment.
Anything not listed is built in §6's grammar or not built.

- **Buttons.** Primary: ink ground, vellum text, brass rule beneath
  on hover (§6.8); the label in Archivo caps. Secondary: vellum
  ground, ink text, 1px brass border. No pill shapes — a chart room
  cuts square corners; radius 2px maximum, for the paper's sake.
- **Inputs / selects / textarea.** §6.14's sheet fields: vellum
  ground, ink text, brass-deep focus outline + foot rule; selects
  styled as ledger lines with a brass caret.
- **Tables.** §6.13 exactly — the theme's table is a set piece, not
  a utility; data grids elsewhere reuse it unchanged.
- **Cards.** §6.12's catalogue cards; log-entry cards reuse the
  same sheet, frame and tilt rules with the plate replaced by the
  entry's date readout.
- **Badges / ticks.** The LOGGED tick (§6.9) is the only badge
  grammar: small caps, rationed vermilion, always paired with a
  shape change. Status labels ("OUT OF PRINT", "PROVISIONAL") are
  annotation-style text, never coloured chips.
- **Alerts.** A chart-room note: a vellum-deep band with a brass
  head rule and the note in body text (§6.14's book-closed note is
  the pattern). No red alerts — vermilion is not an error colour
  here; errors are *corrections*, marked in brass-deep with words.
- **Pagination.** Chart numbers: "SHEET 2 OF 5" in readout style
  with §6.10 transitions between sheets; prev/next named by the
  neighbouring chart's title.
- **Modal.** Refused. A chart room lays another sheet on the table
  (§6.10) or prints a note in place; nothing floats in a scrim.
- **Toast.** Refused. Confirmations are entries (§6.14) or ticks
  (§6.9) — permanent marks on the chart, not messages that vanish.
- **Tabs.** Refused. The course is linear (§6.11); parallel content
  is plotted as successive waypoints, not hidden behind tabs.
- **Accordion.** Permitted once, for the log's long entries:
  sheets that unfold — a 300ms `--ease-drift` height opening with
  the entry's readout always visible as its head. Nowhere else.
- **Tooltip.** §6.8's sighting tooltip — the only tooltip grammar.
- **Progress.** §6.5 and the route itself; no other progress UI
  exists in the theme.
- **Breadcrumbs.** The course line in miniature: "DEPARTURE ›
  BISHOP ROCK › THE SOUNDINGS" in readout style, each a link —
  the breadcrumb is the route, abbreviated.
- **Search.** A chart-room index lookup: an input on the catalogue
  sheet; results ink in (§6.15); no results is §6.18's sheet.

## 12. Content & copywriting voice

Two registers, never mixed in one line. **The Chart** — Cormorant,
measured, declarative — speaks for places, headlines and the
colophon: it names, it does not sell. **The Annotation** — Archivo,
plain, exact — speaks for readouts, labels, notes and errors: it
reports figures and states facts. Headlines are named like places
or findings ("The Long Swell", "Positions, honestly come by."),
never like features ("Our Services") and never with exclamation —
the atelier has never once been excited in print.

**Label style.** Readout labels are uppercase Archivo with the
figure after the label, always: "SAILED 412.6 NM", "DIST TO NEXT
WAYPOINT 218.4 NM". Coordinates always in degrees and minutes with
hemispheres. Dates in full ("22 October 1884") — the chart room
does not abbreviate time.

**Fixed strings (verbatim, do not paraphrase).** "DIST TO NEXT
WAYPOINT" · "COURSE COMPLETE — 1,228.3 NM" · "THIS WATER IS NOT ON
OUR CHART" · "Plotted, sighted and corrected by hand." · "NOT YET
REACHED" (the unreached knot's refusal) · "[N] commissions entered
in this book. Yours will be № [N+1]."

**Error voice.** Errors are corrections, entered plainly with the
value kept: ✓ "That date has already made landfall; choose one
still ahead of us." ✓ "The entry could not be written — your words
are still here." ✗ "Oops! Something went wrong." ✗ "Invalid
input!!" An error never uses vermilion and never apologises twice.

**Empty-state voice.** Absence is a survey result: ✓ "This water
is not on our chart." ✓ "No chart in the catalogue answers to that
name — the shelf is honestly empty." ✗ "Nothing found 🙁" ✗
"Try a different search?" (a question the atelier would not ask;
it states, then it offers the exits).

**Worked voice pairs.** Headline: ✓ "The Soundings — where the
chart first earns its keep." ✗ "Dive into our amazing services!"
Annotation: ✓ "Leg 339.2 nm — the course's longest; allow the
reader time." ✗ "Super long section lol." Button: ✓ "ENTER THE
COMMISSION" ✗ "Let's go 🚀".

## 13. Full-page scroll choreography map

The home page, top to footer, in order. `p` is the shared progress
(§5); every beat reads it or the loop's clock.

1. **The door plate.** Masthead (§6.11) printed; sky at rest.
2. **The sighting.** The pinned hero (130vh): arc, stars, lines,
   fix, headline locks (§6.1). Needle leaves north; SAILED begins.
3. **Departure (WP0).** The hero's foot: Falmouth roads readout
   settles (50°08.9′N 005°03.9′W); the route draws its first dash.
4. **The open-sky band.** 120px of bare field; the route crosses
   open sky; DIST TO NEXT counts down the 55.8 nm leg.
5. **Bishop Rock abeam (WP1).** The charts sheet makes landfall;
   catalogue cards stagger in (§6.12); the knot is tie-able (§6.9).
6. **The Soundings (WP2).** The instruments sheet: service entries
   as instrument cards; brass-frame plates register (§6.7). The
   long leg begins — 339.2 nm of quiet: fewer beats, more sea room.
7. **The Long Swell (WP3).** The tables sheet (§6.13): the voyage
   and the sky in print; the needle crosses 243° at the knot.
8. **The Trade Road (WP4).** The log sheet: journal entries as
   cards; a reader who has tied every knot so far reads their own
   LOGGED ticks down the margin — the page remembers their passage.
9. **Landfall approach.** DIST TO NEXT runs down the final 281.3
   nm; the star bands narrow; the colophon's ink panel rises.
10. **Landfall (WP5).** Horta readout settles; the commission
    sheet (§6.14) prints its preamble promise (№ 128).
11. **The signing.** `p` = 1: needle home, COURSE COMPLETE ticks,
    the colophon's rule draws under the sign-off (§6.16). The
    chart is finished; nothing after this point moves except the
    two licensed ambient loops.

**Other pages, briefly.** The catalogue page runs beats 1, 5 and
11 only — masthead, a complete approach route drawn on entry, the
grid, and a short signing line — because browsing is not sailing.
A detail page runs a two-beat course: the plate registers (§6.7),
its entry prints, and the foot's mini-route offers the two
neighbouring charts as the only choreography. The commission page
is beat 10 held for as long as the reader needs: landfall reached,
the book open, no further motion asking for attention while
someone writes.

**Reverse pass.** Scrolling up: the pencil route re-plots (§6.2),
the needle retraces, counters run back — but landfalls stay made,
knots stay tied, the log stays written. Ink does not unwrite; only
the working line is re-drawn. **Jump scroll:** `p` lerps to target
in ~900ms; reveals cascade in course order at 90ms intervals (§6.3)
— the voyage at speed, never a pop.

## 14. Whole-page performance budget

- **Total page weight:** ≤820KB compressed, of which images ≤380KB
  (plates as §6.7), fonts ≤120KB (Cormorant + Archivo subsets,
  `font-display: swap` with matched fallbacks), JS ≤60KB gz, CSS
  ≤45KB. The star field, route, frames and crosses are inline
  SVG/CSS — zero image weight for the theme's own furniture.
- **Frame budget:** the shared loop's per-frame work ≤1.6ms on a
  mid-range laptop: route dashoffset (0.2), needle + BRG (0.1),
  progress figures (0.1), star stagger amortised (0.3), parallax
  transforms (0.2), one active reveal/counter (0.3), headroom
  (0.4). Long tasks: none over 50ms; the path build at load is
  ≤8ms for six waypoints.
- **Cut order when the budget is exceeded.** (1) The faint third of
  the star field (§6.6's mobile ruling, applied upward). (2) The
  vellum grain drift. (3) Card tilt (§6.12) — hover brightening
  stays. (4) The rose ring's rotation. (5) Plate scale range
  narrows (§6.7). **Never cut:** any watchdog, the printed record,
  the route's geometry, the counters' final values, focus states,
  or the reduced-motion variant. A slower chart is acceptable; a
  wrong or stranded one is not.
- **Print.** The print stylesheet inks everything: route complete,
  tables full, star panels rendered as vellum with ink stars (the
  sky prints as a chart, not a black rectangle).

## 15. Build-order checklist

1. **The record first.** Enter §6.17's data object; recompute legs
   and bearings from the coordinates by the printed rule; verify
   the legs sum to the total before any styling exists.
2. **Static chart.** Build the full page printed and complete —
   route drawn, counters settled, form working — with no
   animation armed. This is the no-JS deliverable; it must already
   be beautiful.
3. **Sheets & grid.** §4's stack, gutters reserved for the route
   and the margin readout; verify no sheet ever underlaps the line.
4. **Typography & palette tokens.** §2–§3 as CSS variables with
   the exact names §6 consumes; contrast rulings encoded as
   comments at the token definitions.
5. **The loop.** The shared rAF loop and `p` (lerp 0.09), with the
   visibility pause; nothing scroll-driven ships before this.
6. **Route & readouts.** §6.2, §6.5, §6.4 from the record; needle
   audit against the leg bearings by hand.
7. **Waypoints & reveals.** §6.3 with watchdogs; the scroll-stop
   rescue rule; focus-into-unreached force-reveal.
8. **The sighting.** §6.1's ceremony, session flag, 3000ms
   watchdog; verify the snap-to-fixed state with JS throttled.
9. **Ambient loops.** §6.6's stars (record phases, 3-frame
   stagger) and §6.4's ring — the only two timers in the build.
10. **Interactions.** §6.8 sighting, §6.9 knots with session
    persistence, §6.12 tilt through the loop's pointer values.
11. **Frames, loader, transition.** §6.7, §6.15, §6.10 with their
    watchdogs; test a forced-slow navigation.
12. **Form.** §6.14 with the record-derived number, idempotency,
    the 4000ms watchdog and the book-closed state.
13. **404 & empty states.** §6.18; verify the real 404 status.
14. **Reduced-motion build.** Every §6 variant; walk the whole
    page with the media query forced.
15. **The gate.** §10's twelve checks, signed by a non-builder;
    the vermilion census and figure audit are run from the record,
    not from memory.
