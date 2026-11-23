# 64. The Cyanotype Vault — Expanded (v1 + v2)

> An architect's blueprint vault printed as cyanotypes: every
> image and diagram is a white-line exposure on Prussian blue,
> and every section is a sheet pulled from a drawer, slid onto
> a light table, exposed, fixed and filed. The page is not a
> portfolio wearing a blueprint texture. It is the vault's own
> working surface — sheets with drawn title blocks, dimension
> lines that measure the actual diagrams at the stated scale,
> and one draughtsman's red pencil that touches each sheet
> exactly once.

**The theme's one law: no sheet stays blank, and no dimension
lies.** Every figure printed anywhere on the page traces to
one declared drawing register (§6.17) — 24,000 mm is six bays
of 4,000, the 266 scheduled items are five rows that add up,
and Request № 47 is the printed 46 requests plus one. Every
scale printed in a title block is the rendered diagram's true
scale: sheet A-101's elevation is drawn 480 units wide in its
SVG because 24,000 mm at 1:50 *is* 480 mm, and the dimension
line beside it measures those 480 units, not a decoration
placed near them. The red pencil is spent exactly once per
sheet at rest — one circled dimension, one correction tick —
and is never a text colour, an error colour or a brand accent.
And no exposure effect may strand a sheet: the line-work
exists complete in the DOM beneath every effect, each reveal
armed by script over the finished sheet and backed by a named
watchdog. A build that leaves a sheet blank blue, prints a
scale its diagram does not keep, spends the red twice on one
sheet, or rounds a register figure has broken the law four
ways.

---

## 1. Concept & world

The vault is the drawing office of **Atelier Marlowe**,
architects, and the site is its public face: a light table on
which the practice's sheets are laid out for clients,
engineers and the merely curious. The world is pre-digital
draughting kept alive as a discipline — cyanotype printing
(iron salts, sunlight, a wash of water), the title block as a
sheet's passport, the checker whose red pencil is the only
human colour in a blue world. The mood is quiet, exact and
slightly ceremonial: drawings are not *displayed* here, they
are *produced* — exposed, fixed, measured and filed in front
of the visitor.

The conceit is load-bearing, not decorative. A cyanotype is
made by exposure, so the page's entrances are exposures. A
sheet is identified by its title block, so navigation state
is a title block. A dimension line exists to state a true
measurement, so the page's counters and progress readouts
state true measurements of the page's own diagrams. A
checker marks a sheet once, so attention itself — hover,
focus, selection — is rationed to one red touch at a time.
Every mechanism in §5 and §6 is the vault's real workflow
wearing no costume.

**Best-fit sites and audiences.** Architecture and engineering
practices; conservation and heritage-restoration studios
(the worked project is one); technical illustrators and
surveyors; museums of design and industrial archives;
any portfolio whose work is literally drawn — set designers,
cartographers, luthiers, type designers presenting specimen
sheets. The audience it flatters is the professional reader:
clients who commission buildings, engineers who will check
the dimensions, students who want to see how a drawing is
put together. It rewards slow, literate browsing and makes
precision feel like hospitality.

**When NOT to use it.** Not for e-commerce — the vault lends
drawings, it does not sell them, and §7 routes commerce out
to the request form. Not for news, feeds or anything updated
hourly: a register is a slow document and the theme's
ceremony curdles into friction at news speed. Not for
content with no drawn or measured artefact at its centre —
if the client's work cannot be drawn, dimensioned or
scheduled, the theme has nothing true to say and becomes the
blue wallpaper §9 forbids. Not for audiences who need large
quantities of photography in natural colour: every image
here is an exposure, and a client who wants their product
shots *as shot* should be refused the theme, kindly, at the
brief stage.

**The worked project.** Throughout this expansion, one
project carries every example: **Project № 114, the Kestrel
Street Baths** — the restoration of a Victorian municipal
baths, drawn by J. Teale (DRN JT) and checked by E. Marlowe
(CHK EM), issued March 2026. Its six sheets on this page
(A-101 to A-106) and its full register (§6.17) are the single
source from which the hero, the table, the form, the footer
and every counter derive their figures.

---

## 2. Palette

Five anchors from the original entry, unchanged. Five derived
tokens do the daily work. Contrast values below are measured
from the hex values for this expansion.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--prussian` | `#1B3A5C` | Prussian blueprint blue — the sheet itself; every sheet's ground | ~62% of pixels | Ground for exposure-white print (10.8:1) and chalk annotation (7.1:1) |
| `--exposure` | `#F4F7F5` | Exposure white — all line-work, all print on sheets, the UV light itself | ~24% | On prussian 10.8:1 — the page's reading contrast; on edge 14.1:1 |
| `--red` | `#C0392B` | Draughtsman's red pencil — one mark per sheet at rest (§6.2) | one stroke per sheet | On prussian 2.1:1 — a hand mark, never text, never an error colour, on any ground |
| `--edge` | `#0F2740` | Sheet edge — sheet borders, the drawer's shadow side, footer ground | ~6% | Exposure white on edge 14.1:1; prussian on edge 1.3:1 — layered grounds only, never a text pairing |
| `--chalk` | `#B9CCE0` | Annotation chalk — dimensions, notes, secondary print on sheets | ~6% | On prussian 7.1:1 — may set annotation text; on edge 9.2:1 |
| `--table` | `#0A1B2E` | The light table — page ground behind and between sheets | ~8% | Sheets sit on it; exposure white on table 15.9:1; it is never a sheet colour |
| `--prussian-raise` | `#22486E` | A sheet lifted toward the light — hover faces, the active index card | within prussian share | Exposure white on raise 9.3:1; distinguishes a handled sheet from a resting one |
| `--chalk-dim` | `#7E97B0` | Retired annotation — superseded dimensions, loan notes, disabled print | <1% | On prussian 3.8:1 — mono labels and large print only, never body text |
| `--fibre` | `rgba(244,247,245,0.05)` | Paper fibre — the sheet's tooth, a fine noise layer over prussian | texture only | Never carries meaning; sits under line-work, above the blue |
| `--uv-glow` | `rgba(244,247,245,0.14)` | UV light — the exposure bar's halo, the table's ambient pulse | transient | White light at intensity, not a sixth hue; never a fill for shapes that must be read |

**Rules that outrank the table.**

- **The red census.** At rest, each sheet carries exactly one
  red mark (§6.2's per-sheet list). The hover underline (§6.9)
  is the same pencil borrowed by the visitor's attention — it
  exists only while a hover or focus lasts, and a sheet never
  shows two red marks at once: while the pencil is lent to an
  underline, nothing else on that sheet is red. The quality
  gate (§10) counts red strokes per sheet in the shipped DOM.
  Errors, required-field markers, sale badges and "new" flags
  are forbidden the red; errors speak in chalk and words (§12).
- **Blue is the material, white is spent.** Prussian is not a
  background colour applied to a web page; it is the sheet.
  Whitespace in this theme is unexposed blue, and exposure
  white is rationed to line-work and print — a large white
  panel is a sheet turned over, which the vault never does.
- **Chalk annotates, white states.** Exposure white sets what
  the drawing *is* — titles, body, figures. Chalk sets what
  the draughtsman *says about it* — dimensions, notes,
  callouts. A paragraph in chalk or a dimension in white is a
  category error the reader feels before they can name it.
- **No light scheme.** There is no inverted day mode. The
  theme *is* a dark-room process; the one light surface in
  the system is the filed request slip the form prints (§6.14)
  — exposure white ground, prussian print — and it is a
  material inside the world (a paper slip), not a theme
  inversion.
- **Dark-mode behaviour.** Operating-system dark mode changes
  nothing. Forced-colours mode is honoured by surrendering:
  sheets print in system colours, title blocks and dimensions
  remain as text, and every effect in §5 is inert (§6, per
  element).

---

## 3. Typography

Two faces, and no third. **Archivo Expanded** is the
lettering hand — display and headings, with the stencil-cut
feel of a drawing title lettered on the sheet. **IBM Plex
Mono** is the office typewriter — annotations, title blocks,
dimensions, body copy and data. The vault owns a lettering
hand and a typewriter; a build that reaches for a third face
has left the building.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Drawn headline (hero sheet) | Archivo Expanded 600 | clamp(2.6rem, 6.2vw, 4.4rem) / 1.04 | +0.01em | Lettered, not typed: set as the sheet's drawn title, blooms with the exposure (§6.1) |
| Sheet title | Archivo Expanded 600 | 2.25rem / 1.1 | +0.01em | One per sheet, always beside its drawing number |
| Section heading within a sheet | Archivo Expanded 500 | 1.5rem / 1.2 | +0.015em | Never larger than the sheet title it serves |
| Body | IBM Plex Mono 400 | 1rem / 1.65 | 0 | The register's prose voice; measure capped at 68ch |
| Annotation / dimension | IBM Plex Mono 500 | 0.8125rem / 1.45 | +0.02em | Chalk; always carries a unit or a drawing number |
| Title block | IBM Plex Mono 500 | 0.75rem / 1.5 | +0.04em, uppercase | DRG / SCALE / DATE / DRN / CHK fields, ruled in a grid |
| Data & counters | IBM Plex Mono 600 | role size / 1.3 | 0 | Tabular numerals, always; figures never letter-spaced |

**Five type laws.**

- **Numerals are always mono, always tabular.** A figure set
  in Archivo — or in proportional numerals that shift width
  as they count — breaks the register's promise that figures
  are fixed objects. Counters (§6.6) count in tabular mono or
  do not count.
- **Scales are written `1:50`, never `1/50`, never "1-50".**
  The colon is the draughting convention and it is also a
  claim: the number after it is checked against the diagram
  (§10's scale-truth audit).
- **Dimensions always carry their unit and their thousands
  comma:** `24,000 mm`, `1,800 mm`, `135 m³`. A bare number on
  a sheet is either a drawing number (A-101), a count from
  the register (266 items), or a mistake.
- **Drawing numbers are identifiers, not decoration.** They
  are set in mono, uppercase, hyphenated — `A-101` — and a
  number printed anywhere must be a sheet that exists in the
  register (§6.17) or a request for one.
- **The dead band.** No text is set between 1.0625rem and
  1.4375rem. The vault speaks in lettering (≥1.5rem) or in
  office print (≤1rem); the in-between sizes are where
  ordinary websites live, and this is not one.

**Stencil discipline.** Archivo Expanded's stencil-cut feel
is used, not illustrated: no drop shadows, no outlines, no
letterpress textures on type. The one typographic effect in
the theme is the hero headline's chemical bloom (§6.1) —
blur resolving as the exposure fixes — and it happens once,
on load, to lettering that is fully present in the DOM from
the first byte.

---

## 4. Layout language

The page is a light table (`--table`) and the content is a
vertical stack of sheets laid on it. Each sheet is a prussian
rectangle with a 1px `--edge` border and a soft table shadow;
sheets are separated by **96px of bare table** — one sheet's
breathing room, the visual equivalent of the drawer pause
between pulling one drawing and the next.

- **Sheet geometry.** Max sheet width 1180px, centred; sheet
  padding 40px desktop, 20px mobile. Sheets never touch each
  other and never touch the viewport edge on desktop — a sheet
  floating edge-to-edge has fallen off the table.
- **The title block is law.** Every sheet carries its drawn
  title block at the bottom-right corner: a ruled mono grid,
  280×96px desktop, printing DRG №, SCALE, DATE, DRN and CHK
  from the register (§6.17). It is part of the sheet's DOM,
  printed, never an overlay widget. On mobile it becomes a
  full-width ruled strip at the sheet's foot — smaller, never
  omitted.
- **Registration crosses.** One cross in each sheet corner,
  inset 16px, drawn by §6.7. They are the sheet's alignment
  marks and the anchor for §6.10's click crosses — same
  geometry, same stroke weight (1.5px), so a visitor's cross
  reads as the same instrument.
- **Dimension lines live outside the drawing.** Diagrams sit
  in a drawn frame; their dimension lines run 24px outside
  the frame's edges, with 8px witness gaps, arrowheads in,
  callouts in chalk mono. Nothing dimensioned is ever
  annotated *across* its face.
- **Density.** A sheet holds one drawing and its apparatus,
  or one schedule and its totals — never two unrelated
  subjects. If content outgrows a sheet, the answer is
  another sheet (another section, another drawing number),
  not a smaller font.
- **Whitespace is unexposed blue.** Empty area on a sheet is
  not a gap to fill; it is the part of the sheet the drawing
  does not need. The register's discipline — density capped,
  blue left blue — is what makes the line-work read as
  precious.
- **The reading line.** The visitor reads down the table;
  sheets are encountered one at a time. All scroll triggers
  in §5 and §6 key to a reading line at 62% of viewport
  height — the point where a sheet laid on the table is
  *being read*, as opposed to merely visible.

---

## 5. Full motion system

Five named easings, all the draughting office's own:
`--ease-expose` (cubic-bezier(0.33, 0, 0.2, 1) — the chemical
bloom: fast strike, long fix), `--ease-slide`
(cubic-bezier(0.22, 0.9, 0.28, 1) — paper settling flat, no
bounce; paper does not bounce), `--ease-rule`
(cubic-bezier(0.45, 0, 0.25, 1) — a ruled line drawn at hand
speed, slight gather at the start), `--ease-fix`
(cubic-bezier(0.3, 0.6, 0.3, 1) — contrast settling as a print
fixes), `--ease-hand` (cubic-bezier(0.6, 0, 0.3, 1) — the
pencil's quick stroke). One shared `requestAnimationFrame`
loop drives every scroll-scrubbed value with lerp
`--loop-lerp` (0.09 — paper drag: heavier than a screen,
lighter than a drawer). Nothing scroll-driven reads the raw
scroll position; everything reads the loop's smoothed value,
so the whole table moves at one physical weight.

**Every motion term, in this theme's language:**

- **Scroll-triggered reveals — sheets slide onto the table.**
  Each sheet translates 40px horizontally with a soft shadow
  lift and settles flat (§6.3), 700ms `--ease-slide`, as its
  top crosses the reading line. Latched: a sheet that has
  arrived does not leave when the visitor scrolls back up —
  it has been pulled from the drawer and filed on the table.
- **Parallax — the sheet's own layers.** Within a sheet, the
  blueprint line-work, the fold-crease shadows and the red
  mark drift at separate shallow rates (1.0 / 0.96 / 1.03 of
  scroll) as the sheet passes — the layers of a physical
  sheet being handled. Rates are small on purpose: parallax
  here is paper thickness, not a landscape.
- **Pinned scenes — the title block and the hero exposure.**
  The active sheet's title block pins to its corner and
  updates as sheets change (§6.5). The hero sheet pins for
  the first 120vh of scroll while its exposure completes, so
  the visitor watches the print fix before the table starts
  to move.
- **Masked line reveals — refused, and replaced.** Masked
  text reveals are a theatre trick; lettering in the vault
  is *exposed*, not unmasked (§6.1's bloom). The refusal is
  total: no clip-path text reveals anywhere in the theme.
- **Blur-to-sharp — the chemical fade.** The one licensed
  blur in the system: line-work blooms from 6px blur to sharp
  behind the UV bar, resolving as fixer acts. Used by the
  hero (§6.1) and the loader (§6.15) only — body text is
  never blurred, anywhere, for any reason.
- **Animated counters — figures counting to their register
  values.** Sheet numbers, scale readouts and dimension
  callouts count (§6.4, §6.6) — always *to* a register
  figure, always in tabular mono, never past it and never to
  a round number invented for the animation.
- **Progress indicator — a dimension line down the page
  edge.** A ruled line at the table's left edge lengthens
  with scroll, callouts at the quarter points reading
  120 / 240 / 360 / 480 — millimetres on sheet A-101, the
  hero's drawn width (§6.17) — so progress is stated as a
  true measurement of the first sheet, not a percentage.
- **Marquee — refused.** The vault does not run a ticker of
  its own contents. The index (§6.12) is a drawer the visitor
  opens; nothing scrolls sideways asking to be noticed.
- **Kinetic typography — refused.** Lettering is draughted,
  not choreographed. The only moving type in the theme is
  the counting readouts, and they move because the *figure*
  is being arrived at, not because the letters are dancing.
- **Ambient loops — exactly two licensed.** The UV glow
  pulse across the light table (6s period, ±4% intensity)
  and dust motes drifting in the exposure light (a 40-particle
  field, §6.1's budget). Paper fibre shift is *not* a loop:
  it is scrubbed to scroll and to sheet hover, the sheet
  being handled, and it stops dead when nothing moves.
- **Micro-interactions & hover physics.** Sheets tilt max
  2°, as paper picked up at one corner (§6.3); hovering an
  annotation borrows the red pencil (§6.9); clicking punches
  a registration cross (§6.10). All hover physics run from
  the loop's lerped pointer values, never raw pointer events.
- **Page transitions — the next sheet slides in.** Navigation
  slides the incoming sheet in from the right over the table
  while the current sheet returns to the drawer (§6.15),
  500ms `--ease-slide`, watchdogged at 2000ms.
- **Image treatments — exposures that fix.** Every image is a
  cyanotype: white-line on prussian, scaling 1.04 → 1.0
  inside its sheet border while its contrast fixes (§6.8).
  The treatment is CSS (an SVG duotone filter), so it holds
  with JavaScript disabled; only the *fixing* is animated.
- **Skeleton loading — blank sheets that expose.** Loading
  regions are blank prussian sheets whose line-work shimmers
  in (§6.15) — the vault's own dormant state, never grey
  boxes, never a spinner.
- **Custom cursor — refused.** Standing rule: the normal
  system cursor only. The visitor's hand in this world is
  the red pencil (§6.9), and it appears under elements, never
  trailing the pointer.

---

## 6. Signature elements

Eighteen elements: the original ten, deepened, plus eight
page-family elements the original entry implied but did not
specify — navigation, index cards, the schedule table, the
request form, the loader and transition, the colophon footer,
the drawing register itself, and the unfiled sheet. Every
figure any element prints comes from §6.17's register.

### 6.1 The UV exposure hero

- **What & why.** The hero sheet (A-101, the North Elevation)
  begins as blank Prussian blue; a vertical UV light bar
  sweeps down the sheet over ~1.6s and the white line-work —
  the headline as drawn lettering, the elevation lines —
  blooms in behind it with a chemical fade, dimension lines
  drawing last. It belongs because the sheet is printed by
  the process it depicts: the studio's drawings are made the
  way cyanotypes are made, on the page itself, in front of
  the client who is being asked to trust the making.
- **Structure.** A `<section>` sheet containing a real inline
  SVG elevation (viewBox 480×248 units — the drawing's true
  drawn size at 1:50, §6.17) and the headline as HTML text
  over it. The UV bar is a DOM element: a 64px-wide vertical
  band of `--uv-glow` with a 2px exposure-white leading edge.
  The line-work's bloom is a CSS filter/opacity pre-state
  (blur 6px, opacity 0.25) applied to a wrapper; the script
  arms it only after registering the watchdog. The sheet's
  full content — headline, elevation, standfirst — is in the
  DOM, complete, before any script runs.
- **Motion spec.** Trigger: load, after first paint. The bar
  travels the sheet's height in 1600ms `--ease-expose`; each
  band of line-work blooms as the bar passes it — blur 6px →
  0 and opacity 0.25 → 1 over 700ms `--ease-expose`, keyed to
  the bar's position, not to independent timers. Dimension
  lines draw last (§6.4's draw, 600ms `--ease-rule`) once the
  bar reaches the sheet's foot. The hero sheet pins for the
  first 120vh of scroll (§5) so the fix completes in view.
  Dust motes drift in the bar's light throughout (§5's second
  licensed ambient loop).
- **States.** Unexposed (the armed pre-state; exists only
  between script-arm and sweep, ≤100ms) / exposing (bar
  travelling, bands blooming) / exposed (rest state; sheet
  fully sharp, dimension lines drawn) / scrolled-past (sheet
  unpins and joins the stack as an ordinary filed sheet).
- **Content merge.** The exposure *is* the content's
  manufacture: the elevation being exposed is the project's
  real hero drawing, the headline is lettered onto the same
  sheet, and the bar's light is the light the print was made
  by. Remove the drawing and there is nothing to expose —
  the effect has no existence independent of the sheet.
- **Failure fallback.** Watchdog at 3000ms from arm: if the
  sweep has not completed, the wrapper's pre-state is removed
  outright — sheet fully exposed, no blur, no bar. No-JS: the
  pre-state is never applied; the sheet ships exposed. Slow
  network changes nothing: the hero is inline SVG and HTML,
  no image waits on the network.
- **Reduced-motion variant.** No sweep, no bloom, no pin: the
  sheet arrives exposed and still, dimension lines complete,
  and the visitor scrolls a static table. The scale readout
  (§6.6) prints 1:50 directly.
- **Performance budget & mobile variant.** One filter
  animation on one wrapper, compositor-driven; the bar is a
  transform. ≤0.4ms/frame from the loop. Mobile (<768px): the
  sweep shortens to 1100ms, the pin is cut (the sheet scrolls
  naturally), dust motes halve to 20 particles, and the drawn
  headline steps down the type scale's clamp.
- **Choreography timeline (v2).** t=0 first paint, sheet
  printed and exposed (the no-JS face) → script arms the
  pre-state and the watchdog → t≈100ms bar enters at the
  sheet's head → t=100–1700ms bar travels, bands bloom
  behind it → t=1700ms bar leaves at the foot, dimension
  lines begin → t=1700–2300ms dimensions draw (§6.4) →
  t=2000ms scale readout settles (§6.6) → t=2600ms the red
  mark is made (§6.2) → watchdog deadline t=3000ms passes
  unused.
- **State matrix (v2).** *Rest:* exposed, sharp, complete.
  *Hover:* nothing — the hero is the process, not a control;
  hovering the sheet lifts its shadow by §6.3's handling
  only. *Focus:* the headline and standfirst are plain text;
  first focusable element is the sheet's own link, underlined
  per §6.9. *Active:* n/a. *Scrolled-past:* exposed state
  persists; the pin releases at 120vh. *Disabled:* n/a.
  *Touch:* identical; no pin, shorter sweep.
- **Breakpoints (v2).** ≥1200px: full ceremony, pin 120vh,
  sheet 1180px. 768–1199px: sweep 1400ms, pin 80vh, sheet
  full table width minus 48px. <768px: sweep 1100ms, no pin,
  motes 20, dimension draw 500ms.
- **Edge cases & failure modes (v2).** *Returning visitor in
  the same session:* the exposure is a manufacture, not a
  greeting — it runs once per session (sessionStorage flag);
  later loads ship exposed. *Tab hidden mid-sweep:* rAF
  pauses; on return the sweep resumes from the bar's
  position, and the watchdog (wall-clock) still guarantees
  completion by 3000ms of visible time. *Very tall
  viewport:* the pin's 120vh is capped so the sheet's foot
  is reachable without scrolling on ≥1600px-tall screens.
- **Accessibility spec (v2).** The SVG elevation is
  `role="img"` with `aria-label` "North elevation of the
  Kestrel Street Baths, drawn at 1:50: 24,000 millimetres
  wide, 12,400 high". The bloom is visual only — text is
  never removed from the accessibility tree, and the
  pre-state's opacity never applies to focusable elements.
  The sweep is not announced; the sheet's content is present
  to assistive technology from the first byte.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--uv-glow`, `--fibre`, `--ease-expose`, `--ease-rule`,
  `--loop-lerp` (0.09), `--dur-expose` (1600ms),
  `--dur-watchdog-hero` (3000ms).

### 6.2 The single red mark

- **What & why.** After each sheet exposes, the draughtsman's
  red pencil makes exactly one mark on it — a circled
  dimension, a correction tick — drawn in a quick hand stroke
  (~300ms). It belongs because it is the human inside the
  system: proof that a checker has read this sheet and put
  their hand to it. Rationed to one per sheet, it stays
  meaningful; spent freely, it would be a brand colour.
- **Structure.** One inline SVG path per sheet, stroke
  `--red`, 2px, with a hand-drawn path (three path variants
  ship, chosen by sheet number, so no two marks are the same
  gesture). The mark's target is declared in the register
  (§6.17): A-101 circles the 9,600 eaves dimension; A-102
  ticks the pool's 12,500; A-103 circles the 1,800 water
  depth; A-104 ticks the 80 bolt gauge; A-105 underlines the
  266 total; A-106's mark is reserved — it is the FILED stamp
  (§6.14), made only when a request is filed.
- **Motion spec.** Trigger: 300ms after the sheet's own
  arrival completes (§6.3's settle, or §6.1's exposure for
  the hero). The stroke draws via stroke-dashoffset over
  300ms `--ease-hand` — one gesture, no flourish, no loop.
  It never redraws: scrolling away and back shows the mark
  already made, as ink is already dry.
- **States.** Unmade (only in the ≤300ms gap after arrival,
  and permanently on A-106 until filing) / drawing (300ms) /
  made (rest state, forever). There is no hover, focus or
  active state; the mark is the checker's, not the visitor's.
- **Content merge.** The mark annotates a real figure on its
  own sheet — the dimension the checker wants the reader to
  notice. It is placed by the register, not by layout: move
  the dimension and the mark moves with it, because the mark
  is *on* the dimension in the DOM (an SVG group wrapping
  both), not positioned over the sheet.
- **Failure fallback.** Watchdog: the mark is drawn by the
  same arm that settles its sheet; if the sheet's watchdog
  fires (§6.3), the mark is applied in its drawn state with
  it. No-JS: marks ship drawn — the DOM carries the completed
  stroke and script rewinds it only when arming the draw.
- **Reduced-motion variant.** The mark is simply present,
  drawn, from the sheet's arrival. A reduced-motion reader's
  sheets are pre-checked, exactly as a posted drawing arrives
  pre-checked.
- **Performance budget & mobile variant.** One path, one
  dashoffset animation per sheet; cost is noise. Mobile:
  identical — the ration does not shrink with the screen.
  On <768px the circled dimension's circle scales with its
  dimension (they are one SVG group), never detached.
- **Choreography timeline (v2).** Sheet settles (t=0) →
  t=300ms pencil strikes → t=300–600ms stroke draws →
  t=600ms mark at rest. Hero sheet: exposure completes
  t=2300ms (§6.1) → mark at t=2600–2900ms. A-106: no timeline
  until §6.14's filing succeeds.
- **State matrix (v2).** *Rest:* made. *Hover:* the mark is
  not hoverable; hovering its dimension borrows the pencil
  per §6.9 and the mark itself does not change. *Focus:*
  n/a. *Active:* n/a. *Scrolled-past:* made, dry.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full-size marks. 768–1199px:
  identical. <768px: marks scale with their target group;
  stroke weight holds at 2px (a pencil line does not thin
  because the sheet is smaller).
- **Edge cases & failure modes (v2).** *A sheet whose marked
  dimension is edited in a CMS:* the mark is bound to the
  dimension's SVG group, so it follows the figure; if the
  figure is deleted, the mark must be re-registered in
  §6.17 or the sheet ships with no mark — an unmarked sheet
  is a process failure §10 catches, never a design choice.
  *Two marks wanted on one sheet:* refused at the register;
  the checker chooses. *The visitor's underline (§6.9) and
  the mark simultaneously:* permitted only because the
  underline is transient and pointer-born; at rest the
  census is always one.
- **Accessibility spec (v2).** The mark is decorative ink on
  a figure that is fully stated in text; it is `aria-hidden`.
  Its meaning — "the checker directs you to this figure" —
  is carried by the dimension's own prominence in the sheet's
  reading order, never by colour alone.
- **Tokens consumed (v2).** `--red`, `--ease-hand`,
  `--dur-redmark` (300ms). One token, by design: the census
  in §10 greps for `--red` and counts strokes per sheet.

### 6.3 Sliding sheets

- **What & why.** Sections arrive as sheets pulled from the
  vault drawer and slid onto the light table: a horizontal
  translate of ~40px with a soft shadow lift, settling flat
  with a paper ease. It belongs because the page's chapters
  *are* physical sheets in the fiction the copy states — the
  index calls them sheets, the title blocks number them —
  and their arrival should be the drawer's motion, not a
  generic fade-up.
- **Structure.** Each sheet is a `<section>` on the table
  (§4's geometry). The slide pre-state (translateX 40px,
  shadow at rest depth) is a class the script applies when
  arming; the shadow is two stacked box-shadows (contact +
  lift) whose spread animates with the translate, so the
  sheet visibly leaves the table surface and lands. Sheets
  also tilt ≤2° during handling (§5) from the loop's lerped
  scroll velocity — a sheet moving fast leans, a sheet at
  rest is flat.
- **Motion spec.** Trigger: the sheet's top crosses the
  reading line (62% viewport height). Translate 40px → 0 and
  shadow lift → rest over 700ms `--ease-slide`; the sheet's
  furniture (§6.7) begins at t=200ms, its red mark (§6.2) at
  settle + 300ms. Stagger: sheets are encountered one at a
  time by the reading line, so no artificial stagger is
  added — the drawer's pace is the scroll's pace. Latched:
  arrival is permanent.
- **States.** In the drawer (armed pre-state; only ever
  below the reading line) / sliding (700ms) / on the table
  (rest) / scrolled-past (on the table, filed — the state
  never reverses).
- **Content merge.** The sheet that slides in is the chapter
  itself — its drawing, title block and text — not a wrapper
  around unrelated content. The vault index (§6.12) lists
  these same sheets by the numbers the sliding sheets carry;
  the motion and the catalogue describe one set of objects.
- **Failure fallback.** Watchdog per sheet at 2500ms from
  arm: a sheet that has not settled snaps to the table —
  translate 0, rest shadow, furniture and mark applied. No-JS:
  no pre-state exists; every sheet is on the table in the
  shipped DOM. Observer failure (no IntersectionObserver):
  the script falls back to the loop's scroll check; if the
  loop itself fails, the watchdog still fires on a timer.
- **Reduced-motion variant.** Sheets are simply on the
  table. No translate, no lift, no tilt — the stack is read
  as a stack, which is the variant's whole design.
- **Performance budget & mobile variant.** Transform and
  shadow only; one sheet animates at a time by construction
  (the reading line sees one arrival per crossing). ≤0.3ms
  per frame. Mobile (<768px): translate shortens to 24px,
  duration 550ms, tilt cut — small sheets are laid down, not
  swung.
- **Choreography timeline (v2).** Sheet top crosses reading
  line (t=0) → t=0–700ms slide and settle → t=200ms furniture
  begins (§6.7) → t=700ms sheet at rest → t=1000ms red mark
  (§6.2) → watchdog deadline t=2500ms passes unused.
- **State matrix (v2).** *Rest:* flat on the table, full
  shadow at rest depth. *Hover:* shadow lifts 2px and the
  sheet tilts ≤1° toward the pointer's edge — paper picked
  up at one corner, from the loop's lerped pointer; content
  never moves under the pointer by more than the tilt.
  *Focus:* a sheet is not focusable; its first control takes
  §6.9's underline. *Active:* n/a. *Scrolled-past:* filed,
  flat. *Disabled:* n/a. *Touch:* no hover lift; arrival
  identical.
- **Breakpoints (v2).** ≥1200px: 40px slide, 1180px sheets.
  768–1199px: 32px slide, sheets at table width minus 48px.
  <768px: 24px slide, 550ms, no tilt, sheet padding 20px.
- **Edge cases & failure modes (v2).** *Jump scroll (anchor
  link, find-in-page):* sheets above the landing point are
  placed on the table instantly by their watchdogs — the
  visitor never lands on a half-drawer page. *Very fast
  scroll through all sheets:* arrivals queue through the
  loop at most two concurrently; the rest snap via watchdog
  rather than staging a six-sheet cascade. *Sheet taller
  than the viewport:* trigger keys to the sheet's top, so a
  long sheet begins arriving as its title enters — its foot
  is never a trigger condition.
- **Accessibility spec (v2).** Arrival motion is never
  announced and never moves focus. Sheets are landmarks
  (`<section>` with `aria-labelledby` to their sheet titles);
  the pre-state's transform does not remove content from the
  accessibility tree or the tab order at any point.
- **Tokens consumed (v2).** `--prussian`, `--edge`,
  `--table`, `--ease-slide`, `--loop-lerp` (0.09),
  `--dur-sheet` (700ms), `--dur-watchdog-sheet` (2500ms).

---

### 6.4 Live dimension arrows

- **What & why.** Beside each diagram, dimension lines extend
  and retract scrubbed to scroll, their mono callouts counting
  to the true scaled measurement as the line grows. It belongs
  because a dimension line is a claim — *this drawing measures
  this* — and the theme's law is that the claim is true: the
  line spans the actual rendered diagram, and the callout is
  the diagram's real size at the sheet's printed scale,
  computed from the register, never typed as decoration.
- **Structure.** Per diagram, an SVG dimension group laid 24px
  outside the drawing frame (§4): witness lines, the dimension
  line with arrowheads in, and a `<text>` callout in chalk
  mono. The line's drawn length is a stroke-dashoffset driven
  by the shared loop from the diagram's passage through the
  viewport. The callout value is computed in the script from
  one formula — drawn units × scale denominator — from the
  register's figures (§6.17), so the number on the sheet and
  the number in the register cannot drift apart. A-101's
  overall width: 480 units × 50 = 24,000 mm. A-103's span:
  300 × 50 = 15,000 mm. A-104's chord depth: 12 × 20 = 240 mm.
- **Motion spec.** Scrubbed, not triggered: as the diagram's
  centre travels the viewport's middle 60vh, the dimension
  extends 0 → full; the callout counts 0 → true figure in
  tabular mono over the same travel, landing exactly on the
  register value as the line completes. Retraction is
  symmetric on reverse scroll — this is the one element that
  un-draws, because measuring is a live act, not a filing.
  Extension reads the loop's lerped progress (0.09), so the
  line has the draughtsman's steady hand, never scroll jitter.
- **States.** Undrawn (diagram below the band) / extending /
  fully drawn with callout at its true figure (diagram centred)
  / retracting (diagram leaving upward) / at rest above the
  band (line drawn, figure held — a measured drawing stays
  measured once the visitor has passed it; retraction happens
  only within the band, not after).
- **Content merge.** The dimension measures the diagram it
  stands beside — the elevation's own width, the section's own
  span — and its callout is that diagram's size in the world
  the drawing describes. It is drafting performed on the
  drawing itself; a dimension group whose diagram is removed
  is removed with it (they are one SVG).
- **Failure fallback.** Watchdog: the dimension's end state is
  a function of scroll position, so a dead loop leaves the
  line wherever it froze — therefore the shipped state is
  *fully drawn with the true callout printed*, and the script
  rewinds to scrub only when the loop is confirmed running.
  No-JS: every dimension on the page is drawn, every callout
  printed at its true figure. The fallback is the design's
  resting face.
- **Reduced-motion variant.** Dimensions are drawn and
  callouts printed, always, at their true figures. No
  extension, no counting — the measurement is stated, which
  is all a reduced-motion reader ever needed from it.
- **Performance budget & mobile variant.** One dashoffset and
  one text update per dimension in the band; at most two
  dimensions animate concurrently. ≤0.2ms/frame. Mobile
  (<768px): only the diagram's primary dimension scrubs (the
  overall width or span); secondary dimensions (bay widths,
  heights) print fully drawn — a small sheet is measured
  once, clearly, not five times faintly.
- **Choreography timeline (v2).** Diagram enters the band
  (t=0 in scroll terms) → line begins extending from the
  witness marks → callout begins counting, locked to the
  line's drawn fraction → diagram centred: line complete,
  callout lands on the true figure → diagram exits the band:
  state latches drawn. Hero: the same draw runs on the
  exposure's timeline instead (§6.1, 600ms `--ease-rule`).
- **State matrix (v2).** *Rest (centred):* drawn, figure
  true. *Hover:* hovering the callout underlines it per
  §6.9 — the pencil checks the figure. *Focus:* callouts are
  not focusable; a diagram's figure caption carries the same
  figure as text. *Active:* n/a. *Scrolled-past:* drawn and
  held. *Disabled:* n/a. *Touch:* identical scrub; no hover.
- **Breakpoints (v2).** ≥1200px: all dimensions scrub,
  callouts outside the frame. 768–1199px: primary + one
  secondary scrub; the rest print drawn. <768px: primary
  only; callouts move inside the sheet's margin below the
  frame (a small sheet has no room outside its frame), still
  chalk mono, still true.
- **Edge cases & failure modes (v2).** *A diagram rendered
  at a size its title block doesn't expect (CMS image swap):*
  the callout is computed from the register and the *stated*
  scale, so a wrong-sized diagram makes the dimension visibly
  not span it — the failure is honest and §10's scale-truth
  audit catches it in testing, rather than the callout lying
  to match. *Content longer than the design expects (a tall
  elevation):* the band is computed on the diagram's middle
  third, so extension completes progressively. *Rounding:*
  callouts count through integers and land on the register
  figure exactly; intermediate values are the drawn fraction
  × the true figure, rounded to whole millimetres — the
  count never displays a figure the register would disown
  at rest.
- **Accessibility spec (v2).** The dimension group is
  `aria-hidden` — its figure is duplicated in the diagram's
  caption and `aria-label` as plain text ("Overall width
  24,000 millimetres"), so no measurement depends on reading
  an animated SVG. Callout contrast: chalk on prussian
  7.1:1 at every point of the count.
- **Tokens consumed (v2).** `--chalk`, `--exposure`,
  `--ease-rule`, `--loop-lerp` (0.09), `--dim-offset` (24px).

### 6.5 The pinned title block

- **What & why.** The active sheet's title block — drawing
  №, scale, date, checked-by — pins to the sheet's corner and
  updates as sheets change, so whichever drawing the visitor
  is reading is always properly filed in view. It belongs
  because the title block is a drawing's identity papers; a
  vault that lets you read a sheet without its papers in
  sight has failed at the one job a vault exists for.
- **Structure.** Not a floating widget: each sheet carries
  its own title block in its DOM (§4), and the *pinning* is a
  behaviour — as a sheet becomes active (its body crosses the
  reading line), its block is already at its corner; the
  pinned behaviour belongs to the masthead's compact readout
  (§6.11), which mirrors the active block's DRG № and SCALE
  when the sheet's own block has scrolled out of view. One
  source of truth — the sheet's block — and one mirror. The
  block itself: a ruled grid, five fields, exposure-white
  hairlines on prussian, mono uppercase.
- **Motion spec.** Sheet change: the masthead mirror
  crossfades — old № fades 150ms, new № fades 150ms, a 300ms
  `--ease-fix` exchange, never a slide or a flip (papers do
  not perform). Within a sheet, the block does not move at
  all; it is printed on the sheet. The mirror appears only
  when the active sheet's own block is off-screen — below
  the reading line's sheet, the block itself is the display.
- **States.** Filed with its sheet (rest; block in place,
  mirror hidden) / mirrored (sheet active, block off-screen,
  mirror showing its № and scale) / exchanging (300ms
  crossfade between sheets) / scrolled-past (the next sheet's
  block takes over by the same rule).
- **Content merge.** The block's fields are the register's
  fields for that sheet (§6.17) — №, scale, issue date, DRN,
  CHK — rendered from the same data as §6.12's index cards
  and §6.17's table. It is the sheet's own papers, not a
  navigation chrome wearing a costume.
- **Failure fallback.** Watchdog: the mirror is driven by a
  scrollspy (IntersectionObserver on sheets); if no sheet
  has been observed within 1000ms of load, the mirror shows
  the first sheet's papers (the visitor is at the top; that
  is never wrong). No-JS: no mirror exists and none is
  needed — every block is printed on its sheet, which is
  the complete design.
- **Reduced-motion variant.** The mirror exchanges instantly,
  no crossfade. Blocks, as ever, are print.
- **Performance budget & mobile variant.** Observer-driven,
  zero per-frame cost. Mobile (<768px): the block is the
  full-width ruled strip at the sheet's foot (§4) and the
  mirror lives in the masthead permanently — on a small
  table, the papers are kept in the bar because the sheet's
  foot is far away.
- **Choreography timeline (v2).** Sheet crosses reading line
  → its block becomes the active papers → if the block is
  off-screen, mirror fades out the previous № (150ms) and in
  the new (150ms) → next sheet crosses → exchange repeats →
  final sheet: A-106's block mirrors until the footer.
- **State matrix (v2).** *Rest:* block printed on its sheet.
  *Hover:* the block is not interactive; hovering its sheet
  lifts the sheet per §6.3 only. *Focus:* the mirror is not
  focusable; it is a readout. *Active:* the active sheet's
  № is set in exposure white in the mirror; inactive mirrors
  do not exist (one mirror, one sheet). *Scrolled-past:*
  superseded by the next sheet's papers. *Disabled:* a sheet
  not yet issued (a future drawing in the index) has no
  block — its index card prints "NOT YET DRAWN" in chalk-dim
  instead (§6.12). *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: block 280×96px at the
  sheet's bottom-right; mirror in masthead only when needed.
  768–1199px: block 240×88px; mirror as desktop. <768px:
  block is the foot strip; mirror permanent in the masthead.
- **Edge cases & failure modes (v2).** *Two sheets crossing
  the reading line in one fast scroll:* the mirror exchanges
  directly to the final sheet — intermediate papers are
  never flashed. *A sheet with no register entry (CMS error):*
  the block prints its № and "UNREGISTERED" in chalk-dim in
  the CHK field — the failure is filed, visibly, in the
  sheet's own papers, and §10's gate fails the build.
  *Print:* every block prints with its sheet; the mirror is
  `display:none` in print — papers belong to sheets.
- **Accessibility spec (v2).** The block is a `<table>`-like
  ruled grid built from a definition list — field names and
  values are real text, readable in order ("Drawing A-101.
  Scale 1:50. Issued 14 March 2026. Drawn J T. Checked
  E M."). The mirror carries `aria-hidden` duplication only;
  screen-reader users meet each block once, on its sheet.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--chalk`, `--chalk-dim`, `--ease-fix`, `--dur-block-xfade`
  (300ms).

### 6.6 The scale-counting readout

- **What & why.** In the hero, the sheet's scale readout ticks
  through 1:200 → 1:100 → 1:50 in mono as the exposure
  completes, settling at 1:50. It belongs because a sheet
  declares its own scale as it fixes — and the declaration is
  checkable: 1:50 is the scale at which the elevation's 480
  drawn units equal the register's 24,000 mm (§6.4, §6.17).
  The count is the sheet measuring itself and reporting.
- **Structure.** A mono readout in the hero sheet's title
  block (§6.5), in the SCALE field — not a separate gadget.
  The field's value is a text node the script steps through
  the three values; the shipped DOM prints 1:50, and the
  script rewinds the field to 1:200 only in the frame it
  arms the exposure (§6.1).
- **Motion spec.** Trigger: the hero exposure. Steps at
  t=900ms (1:200 → 1:100) and t=1700ms (→ 1:50), timed to the
  UV bar's passage — the scale refines as more of the sheet
  is exposed, coarser readings first, exactly as a print
  resolving under light gives up its scale progressively.
  Each step is an instant text exchange (a readout does not
  tween), with a 120ms chalk flash on the field as the new
  value lands. Settling at 1:50 draws a small chalk tick
  beside the field — in chalk, not red: the hero sheet's one
  red mark is the circled 9,600 (§6.2), and this readout may
  not spend it. That ruling is deliberate and recorded here
  because the original entry's "pencil tick" is a draughting
  tick, and draughting ticks are made in whatever the hand
  holds — the annotation hand holds chalk.
- **States.** Reading (1:200, then 1:100, during exposure) /
  settled (1:50 + chalk tick; the rest state) / printed
  (no-JS and reduced-motion: 1:50 from the start).
- **Content merge.** The readout is the title block's own
  SCALE field — the sheet's papers declaring the sheet. Its
  final value is the same 1:50 printed in §6.12's card for
  A-101 and §6.17's register row; three printings, one
  figure, audited in §10.
- **Failure fallback.** Watchdog: the hero's 3000ms watchdog
  (§6.1) covers the readout — if the exposure is forced
  complete, the field is set to 1:50 and ticked in the same
  frame. No-JS: prints 1:50, tick present (the tick is part
  of the printed field, drawn as an SVG stroke in the DOM).
- **Reduced-motion variant.** 1:50, ticked, from the first
  byte. No stepping — a settled sheet does not re-measure
  itself for anyone.
- **Performance budget & mobile variant.** Two text exchanges
  and one opacity flash; cost is zero for practical purposes.
  Mobile: identical — the title block is the foot strip
  (§6.5), and the readout steps in it exactly the same.
- **Choreography timeline (v2).** Exposure arms (t≈100ms,
  §6.1) → field rewinds to 1:200 → t=900ms step to 1:100,
  chalk flash 120ms → t=1700ms step to 1:50, flash → tick
  draws 200ms `--ease-rule` → t=2600ms the sheet's red mark
  is made elsewhere (§6.2) → readout at rest.
- **State matrix (v2).** *Rest:* 1:50, ticked. *Hover:*
  hovering the SCALE field underlines it per §6.9 like any
  annotation. *Focus:* the field is text in the block's
  definition list, reached in reading order; not separately
  focusable. *Active:* n/a. *Scrolled-past:* settled value
  persists. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: in the corner block.
  768–1199px: in the smaller block, same steps. <768px: in
  the foot strip; steps unchanged (the strip is ruled for
  the same five fields).
- **Edge cases & failure modes (v2).** *Exposure skipped
  (returning visitor, §6.1's session rule):* the readout
  ships settled — it never re-counts for a reader who has
  seen the sheet made. *A sheet whose true scale is not in
  the step sequence (A-102 at 1:100, A-104 at 1:20):* only
  the hero counts; other sheets' SCALE fields print settled
  — the count is the hero's ceremony, not a per-sheet tic.
  *Reduced data / CMS scale edit:* the field renders from
  the register; an edited scale that fails §10's audit
  fails the build, not the reader.
- **Accessibility spec (v2).** The stepping values are not
  announced (no live region — a screen reader meets the
  settled 1:50, which is the fact). The field's text is
  "Scale 1:50" in the block's list at all times in the
  accessibility tree; the visual stepping is a print effect
  on a value that never changes meaning.
- **Tokens consumed (v2).** `--chalk`, `--exposure`,
  `--ease-rule`, `--dur-scale-step` (800ms between steps).

---

### 6.7 Self-drawing sheet furniture

- **What & why.** Per sheet, the registration crosses, the
  title-block frame and the fold creases stroke themselves in
  (~800ms) in draughting order as the sheet arrives. It
  belongs because a sheet is *ruled* before it is drawn on —
  the furniture is the draughtsman's first act, and watching
  it happen teaches the visitor how to read everything that
  follows: corners first, papers second, the drawing last.
- **Structure.** One SVG furniture layer per sheet, absolutely
  positioned over the sheet's ground, beneath its content:
  four registration crosses (16px arms, 1.5px stroke) inset
  16px from the corners; the title-block frame (a ruled
  rectangle with its five field dividers, §6.5); two fold
  creases (vertical hairlines at the sheet's third points,
  `--fibre` at double weight — shadows of old folds, not
  lines). All strokes are dashoffset-animated paths; the
  creases fade rather than draw (a crease is a shadow, and
  shadows are not ruled).
- **Motion spec.** Trigger: the sheet's slide (§6.3), at
  t=200ms into it. Order, as a draughtsman works: crosses
  first (four strokes, 300ms, staggered 60ms corner to
  corner), the title-block frame next (its outline 300ms
  `--ease-rule`, field dividers 150ms), creases last (fade
  400ms `--ease-fix`). Total ≈800ms, completing as the sheet
  settles. Once drawn, furniture never redraws.
- **States.** Ruled (rest — all furniture present) / ruling
  (the 800ms sequence) / unruled (exists only in the armed
  pre-state before a sheet's first arrival).
- **Content merge.** The furniture is the sheet's own
  apparatus — the crosses §6.10's clicks echo, the frame
  §6.5's block fills, the creases the parallax (§5) drifts.
  It is drawn on this sheet, at this sheet's corners, sized
  to this sheet; it is not a border theme applied to a box.
- **Failure fallback.** The furniture ships drawn in the DOM;
  the script rewinds dashoffsets only when arming a sheet's
  arrival, and the sheet's 2500ms watchdog (§6.3) applies
  the ruled state if the sequence stalls. No-JS: ruled,
  always — the shipped face of every sheet is a finished
  sheet.
- **Reduced-motion variant.** Furniture present, no draw. A
  reduced-motion reader receives sheets already ruled, which
  is how sheets arrive from any real drawer anyway.
- **Performance budget & mobile variant.** At most nine short
  paths per sheet, dashoffset only; ≤0.2ms/frame during the
  800ms. Mobile: creases cut (a phone-width sheet has no
  folds worth showing), crosses and frame unchanged — the
  papers are never the thing that gets cut.
- **Choreography timeline (v2).** Sheet slide begins (t=0)
  → t=200ms crosses strike, 60ms stagger → t≈500ms block
  frame outlines → t=650ms dividers rule → t=600–1000ms
  creases fade in → t=1000ms furniture at rest, sheet settled
  (t=700ms, §6.3) → t=1000ms red mark (§6.2).
- **State matrix (v2).** *Rest:* ruled. *Hover:* furniture
  does not respond to hover; the sheet's lift (§6.3) carries
  it. *Focus:* n/a — furniture is never focusable.
  *Active:* n/a. *Scrolled-past:* ruled. *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full furniture, creases at
  third points. 768–1199px: full furniture; creases at the
  sheet's single third (one fold on a narrower sheet).
  <768px: crosses + frame only; crosses inset 12px.
- **Edge cases & failure modes (v2).** *A sheet whose content
  is taller than expected:* furniture is positioned to the
  sheet's box, not its content — crosses stay at the true
  corners of the sheet as laid out, which is the only place
  registration marks can honestly be. *Frame vs. block
  content mismatch:* the frame is drawn around the block's
  actual box (measured at layout), so a longer CHK name
  widens the frame rather than overflowing it. *Print:*
  furniture prints — crosses and frame are part of the
  sheet's archival face.
- **Accessibility spec (v2).** The furniture layer is
  `aria-hidden` and pointer-transparent. The title block's
  *content* is real DOM text (§6.5); only its ruled frame is
  in this layer, and a frame carries no information a screen
  reader lacks.
- **Tokens consumed (v2).** `--exposure`, `--edge`,
  `--fibre`, `--ease-rule`, `--ease-fix`, `--dur-furniture`
  (800ms).

### 6.8 Fixing exposures

- **What & why.** Images render as cyanotype exposures:
  white-line, slightly soft, scaling 1.04 → 1.0 within their
  sheet borders while their contrast "fixes" over ~500ms as
  they centre. It belongs because in this world a photograph
  is not placed, it is *printed* — developed on the sheet in
  the same chemistry as the drawings, so site photography
  (the baths as built, the studio at work) enters the vault
  by the vault's own process instead of breaking it.
- **Structure.** A `<figure>` with a real `<img>` (full `alt`,
  real dimensions, lazy-loaded below the fold) treated by a
  CSS SVG duotone filter — luminance mapped to the prussian →
  exposure ramp — so the cyanotype treatment is presentational
  CSS, not a pre-rendered asset: the same photograph can be
  re-exposed if the ramp is ever re-ruled. A chalk caption
  beneath prints the exposure's data like a census record:
  subject, sheet № it belongs to, exposure № from the register
  (the worked project carries four exposures, E-01 to E-04,
  §6.17). The figure sits inside a drawn sheet border; the
  image never bleeds past it.
- **Motion spec.** Trigger: scroll scrub across the figure's
  passage through the viewport's centre band. Scale 1.04 →
  1.0 and a contrast ramp (the filter's mid-point) settle
  together over the central 50vh of travel, read from the
  loop's lerped progress — the print fixes as it centres and
  holds fixed after; scrolling back up does not un-fix it
  (fixer is permanent — the latch is chemical, stated here so
  no builder makes it symmetric). The softness resolves with
  the scale: blur 1.5px → 0 across the same travel.
- **States.** Unfixed (above the band: scale 1.04, contrast
  low, slight blur — a print still in the tray) / fixing
  (scrubbing) / fixed (rest: scale 1.0, full contrast, sharp)
  / scrolled-past (fixed, permanently).
- **Content merge.** The caption's exposure № ties the image
  to the register, and the treated image is the project's
  actual photography — the baths' pool hall as E-02 on sheet
  A-103, the section's own sheet. The duotone ramp uses the
  sheet's own two tones; the photograph is printed *in* the
  sheet's material, not framed by it.
- **Failure fallback.** The shipped state is *fixed*: scale
  1.0, full contrast, sharp — the script sets the unfixed
  pre-state only when the loop is running, so a dead loop
  leaves every photograph fully developed. No-JS: fixed,
  duotone intact (the filter is CSS). Image failed to load:
  the figure holds its border and caption with the `alt`
  printed as the caption's first line and a chalk note,
  "Exposure failed to develop" — an admitted gap on the
  sheet, never a broken-image icon.
- **Reduced-motion variant.** Fixed at all positions: no
  scale, no contrast ramp, no blur. The photograph is simply
  there, printed — a developed exposure under the lamp.
- **Performance budget & mobile variant.** The filter is a
  static SVG filter reference; animating its mid-point is
  the one real cost — capped at one figure in the band at a
  time (§4's density rule guarantees this), ≤0.5ms/frame.
  Images ≤180KB each, responsive sizes, WebP/AVIF. Mobile
  (<768px): scale range narrows to 1.02 → 1.0, blur cut, the
  contrast fix remains — fixing is the meaning, scale is the
  garnish.
- **Choreography timeline (v2).** Figure enters centre band
  → contrast begins rising, scale begins settling, blur
  resolving, all locked to one lerped progress → centred:
  fully fixed → exits upward: fixed state latches → figure
  leaves as a finished print.
- **State matrix (v2).** *Rest (centred):* fixed. *Hover:*
  nothing on the image itself; the caption's sheet link
  underlines per §6.9. *Focus:* the figure is not focusable.
  *Active:* n/a. *Scrolled-past:* fixed. *Disabled (load
  failure):* border + printed alt + chalk note, as above.
  *Touch:* identical scrub.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  scale 1.03 → 1.0. <768px: scale 1.02 → 1.0, no blur,
  contrast fix over the central 40vh.
- **Edge cases & failure modes (v2).** *A colour-critical
  image (a material sample whose colour is the content):*
  the theme refuses it a duotone lie — such images are
  presented as register data (a table row in §6.13) with a
  note, not as exposures; the vault does not falsify
  evidence. *Two figures in one viewport:* §4 forbids it;
  if a CMS build violates it, the second figure ships fixed
  (no second fixing competes). *No SVG filter support:*
  the image renders untreated at full contrast — a plain
  photograph on the sheet, honest and readable.
- **Accessibility spec (v2).** Real `alt` written as an
  exposure caption ("The pool hall from the deep end,
  exposure E-02, sheet A-103"). The duotone is decorative
  treatment of an image whose information is in the alt and
  caption; nothing is communicated by the treatment that
  the text does not carry. Caption contrast: chalk on
  prussian 7.1:1.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--chalk`, `--ease-fix`, `--loop-lerp` (0.09),
  `--dur-fix` (500ms nominal).

### 6.9 Red-pencil hover

- **What & why.** Hovering any annotation or link draws a
  red-pencil underline beneath it — a slightly rough hand
  stroke, 250ms. It belongs because attention in the vault is
  the draughtsman's pencil: the visitor checking a figure is
  doing the checker's act, and the theme lends them the
  checker's instrument. It is also the red census's one
  licensed exception (§2): the same single red, spent on the
  element being checked, only while it is being checked.
- **Structure.** An SVG underline path (three pre-drawn rough
  variants, so repeated hovers do not stamp the same gesture)
  injected under the hovered element, width matched to the
  element's text, stroke `--red` 2px. One underline exists at
  a time per sheet — enforced structurally: the underline is
  a single node per sheet that *moves* to the hovered
  element, the way one pencil moves across a sheet.
- **Motion spec.** Trigger: pointerenter / focus-visible.
  The stroke draws left-to-right over 250ms `--ease-hand`.
  On leave/blur it fades in 150ms (a pencil lifting, not
  erasing — erasure would draw backwards, which reads as
  doubt). Rapid movement across a row of links: the node
  retargets without a fade between — the pencil slides along
  the sheet, redrawing at each stop, 250ms per draw.
- **States.** Rest (no underline; the sheet's only red is
  its §6.2 mark) / drawing (250ms) / held (while hover or
  focus lasts) / lifting (150ms fade). Focus state is
  identical to hover — keyboard checkers get the same pencil.
- **Content merge.** The underline sits under the actual
  annotation or link being checked — a dimension callout, a
  sheet link in §6.12, a form label in §6.14 — and its length
  is that element's length. It annotates content; it never
  decorates chrome. Buttons are excluded: a button is a
  tool, not an annotation, and tools are not underlined
  (§11 gives buttons their own filed-state treatment).
- **Failure fallback.** Pure CSS `:hover`/`:focus-visible`
  carries a plain 2px red underline if the script is absent
  — the pencil survives no-JS as a standard underline in the
  theme's red, rougher in the hand only when the script
  lives. No element's affordance depends on the SVG version.
- **Reduced-motion variant.** The underline appears whole,
  instantly, and disappears instantly. The pencil is present;
  the gesture is not performed.
- **Performance budget & mobile variant.** One node move and
  one dashoffset per hover; negligible. Mobile / touch: no
  hover exists — the underline fires on focus only (keyboard,
  switch control), and taps go straight to §6.10's cross or
  the link's navigation. Nothing on touch waits for a pencil.
- **Choreography timeline (v2).** Pointerenter (t=0) → node
  moves to the element → t=0–250ms stroke draws → held while
  hovered → pointerleave → t=0–150ms fade → node parked.
  Keyboard: focus-visible fires the same timeline.
- **State matrix (v2).** *Rest:* absent. *Hover:* drawn and
  held. *Focus:* drawn and held, plus the element's visible
  focus outline (2px exposure-white at 3px offset — the
  pencil never replaces the focus indicator). *Active
  (pressed):* underline holds; the click's own feedback is
  §6.10's cross or navigation. *Scrolled-past:* a hovered
  element scrolled out from under the pointer releases the
  underline immediately. *Disabled:* disabled elements get
  no underline — the pencil does not check what cannot be
  used, and their chalk-dim print says why (§11). *Touch:*
  focus-only, as above.
- **Breakpoints (v2).** ≥1200px: full behaviour. 768–1199px:
  full. <768px: full for focus; hover via pointer still draws
  (a small screen with a mouse is still a desk).
- **Edge cases & failure modes (v2).** *Hover crossing from
  an underlined element to its neighbour in the same
  millisecond:* the node retargets mid-draw; the partial
  stroke is abandoned, never completed in the wrong place.
  *An element wider than the sheet (a long table row):* the
  underline spans the element's *text*, measured, not the
  row's box — the pencil underlines words, not furniture.
  *The sheet's §6.2 mark and an underline in the same visual
  field:* permitted (one is at rest, one is transient), but
  if the hovered element *is* the marked dimension, the
  underline does not draw — the pencil is already there.
- **Accessibility spec (v2).** The underline is never the
  sole indicator of anything: links are links in the DOM,
  focus carries its own outline, and hover state changes
  nothing semantic. The SVG node is `aria-hidden`. Touch
  targets are unaffected — the underline extends no target
  and shrinks none; targets hold at ≥44px per §11.
- **Tokens consumed (v2).** `--red`, `--exposure`,
  `--ease-hand`, `--dur-pencil` (250ms).

---

### 6.10 Registration-cross click & the pulled list

- **What & why.** Clicking a sheet element punches a small
  registration cross beside it (two strokes, 200ms) and adds
  the sheet to a "pulled for review" list in the vault index.
  It belongs because selecting drawings for review is the
  vault's real workflow: a client walks the table, marks the
  sheets they want pulled, and the office pulls them. The
  cross is not a bookmark icon in costume — it is the mark
  the vault's own furniture (§6.7) taught the visitor to read.
- **Structure.** The cross is the §6.7 registration cross at
  half size (8px arms, 1.5px stroke, exposure white), drawn
  as two SVG strokes placed in the sheet's margin beside the
  clicked element's title. Clicking is bound to a sheet's
  "Pull this sheet" control — a real button in each sheet's
  title-block row (§11) — never to arbitrary content clicks:
  the cross answers a declared intention, not a stray tap.
  The pulled list lives in the index (§6.12), rendered as a
  ruled strip listing pulled №s, persisted in sessionStorage.
- **Motion spec.** Trigger: the Pull control's click. Stroke
  one (vertical) draws 100ms `--ease-hand`, stroke two
  (horizontal) 100ms — a punch, two beats, 200ms total. The
  index strip and the masthead count (§6.11) update in the
  same beat; no page move, no scroll. Clicking again (the
  control now reads "Return to drawer") fades the cross in
  200ms and removes the sheet — a returned sheet is unmarked,
  cleanly, the way a real cross in pencil is erased.
- **States.** Unpulled (no cross; control reads "Pull for
  review") / punching (200ms) / pulled (cross at rest;
  control reads "Return to drawer"; the sheet's index card
  shows the same cross, §6.12) / returning (200ms fade).
- **Content merge.** The cross marks the actual sheet that
  will be pulled, and the list it feeds is the index's own
  pulled strip — the same objects, the same numbers. The
  count the masthead shows ("3 pulled") is the list's length,
  computed, never a parallel tally that could disagree.
- **Failure fallback.** No-JS: the Pull control is a form
  post to the index with the sheet № as its value; the
  server-rendered index shows the pulled strip and the
  sheet's card carries its cross in print. sessionStorage
  unavailable (private mode): the list lives for the page
  only and the strip says so in chalk — "This table only;
  the list is not being kept" — an honest limitation printed,
  not silently lost.
- **Reduced-motion variant.** The cross appears whole on
  click, disappears whole on return. The state change, not
  the punch, is the content.
- **Performance budget & mobile variant.** Two stroke
  animations and a list render; negligible. Mobile: the Pull
  control is a full-width button in the sheet's foot strip
  (§6.5) with a ≥48px target; the cross draws beside the
  sheet title at the sheet's head (the margin is narrow; the
  mark goes where the title is).
- **Choreography timeline (v2).** Click (t=0) → t=0–100ms
  vertical stroke → t=100–200ms horizontal stroke → t=200ms
  index strip + masthead count update → control label
  exchanges to "Return to drawer". Return: click → 200ms
  fade → strip and count update.
- **State matrix (v2).** *Rest:* as filed (pulled or not).
  *Hover:* the Pull control underlines per §6.9 — it is an
  annotation-grade control, labelled in words. *Focus:*
  outline per §6.9 plus the control's own focus ring.
  *Active:* the punch fires on activation, not on press-down
  — a half-press pulls nothing. *Scrolled-past:* state
  persists; crosses are print once punched. *Disabled:* a
  sheet out on loan (§6.12) cannot be pulled — its control
  prints disabled in chalk-dim with the reason beside it,
  "Out on loan — back 4 April" (§6.17). *Touch:* identical;
  target ≥48px.
- **Breakpoints (v2).** ≥1200px: cross in the sheet margin
  beside the title. 768–1199px: same, margin narrows, cross
  holds size. <768px: cross beside the title at the head;
  control full-width in the foot strip.
- **Edge cases & failure modes (v2).** *Pulling every sheet:*
  permitted — the strip lists all №s and the masthead counts
  honestly; the vault does not ration a client's review.
  *A № in storage that the register no longer holds (a sheet
  withdrawn between visits):* the strip prints it struck
  through in chalk with "Withdrawn" — the list admits its
  own staleness rather than dropping the entry silently.
  *Duplicate pulls:* structurally impossible; the control is
  a toggle with one state per sheet.
- **Accessibility spec (v2).** The control is a button with
  `aria-pressed` and a label naming its sheet ("Pull sheet
  A-103 for review"); the cross itself is `aria-hidden` —
  the state is in the button and in the strip, which is a
  list with a heading, reachable and readable. The count
  change is announced once via a polite live region in the
  strip ("Sheet A-103 pulled. 3 sheets pulled.").
- **Tokens consumed (v2).** `--exposure`, `--chalk-dim`,
  `--ease-hand`, `--dur-cross` (200ms).

### 6.11 Light-table masthead & sheet navigation

- **What & why.** The masthead is the light table's near
  edge: the studio wordmark lettered in Archivo Expanded,
  the sheet links in mono (A-101 … A-106, Index), the
  pulled count (§6.10), and the compact mirror of the active
  sheet's title block (§6.5). It belongs because a table has
  an edge where the tools sit — the visitor orients by it
  the way a draughtsman orients by the straightedge taped to
  the board's near side.
- **Structure.** A `<header>` with a real `<nav>`, sticky at
  the table's top, ground a gradient from `--table` to
  transparent over 72px so the bar dissolves into the table
  rather than ruling a line across it. Links are chalk,
  exposure white for the active sheet (set by the same
  scrollspy that drives §6.5's mirror — one source of "which
  sheet am I reading"). The pulled count is a mono readout
  at the bar's right, present only when ≥1 sheet is pulled.
- **Motion spec.** Entrance: at load, the wordmark is printed
  from the first byte; the sheet links rule in as a single
  hairline draw (400ms `--ease-rule`) beneath the bar — the
  straightedge being laid down. Scrollspy changes: the active
  link's colour exchanges over 200ms `--ease-fix`; no sliding
  indicators, no pills — papers change hands quietly. The
  bar does not hide on scroll: the straightedge stays taped.
- **States.** Rest (active sheet's link white, others chalk)
  / exchanging (200ms colour exchange) / at the index (the
  Index link takes the active state; sheet links all chalk).
- **Content merge.** The bar's links are the sheets
  themselves — the same №s the sheets carry in their title
  blocks and the index lists. It is the table's edge, laid
  with the table's own objects; nothing in it exists that is
  not a sheet, the index, or the visitor's own pulled list.
- **Failure fallback.** No-JS: all links printed and working;
  the active state is absent (a plain bar over a working
  table — the vault without electricity). Scrollspy failure:
  §6.5's watchdog rule applies — the first sheet reads active
  until evidence arrives.
- **Reduced-motion variant.** No hairline draw; active
  exchanges are instant. The bar is print.
- **Performance budget & mobile variant.** Observer-driven;
  zero per-frame cost. Mobile (<768px): the bar holds the
  wordmark, the §6.5 mirror (permanent there) and a "Sheets"
  button opening a full-width drawer panel — the vault drawer
  itself, listing the sheets as ruled rows — over the table,
  250ms `--ease-slide`; the panel's ground is `--edge` at
  98% so the table behind it rests.
- **Choreography timeline (v2).** Load → wordmark printed →
  hairline rules in 400ms → first scrollspy reading sets the
  active link → sheet changes exchange colour in 200ms →
  footer reached: the last sheet (A-106) or Index holds the
  active state, per which is on the table.
- **State matrix (v2).** *Rest:* active link white, mirror
  per §6.5. *Hover:* link underlines per §6.9. *Focus:*
  underline plus 2px exposure outline at 3px offset.
  *Active:* the current sheet's link, `aria-current="true"`.
  *Scrolled-past:* n/a (sticky). *Disabled:* a link to an
  unissued sheet prints chalk-dim, unlinked, "Not yet drawn"
  (§6.12's ruling). *Touch:* targets ≥44px; the drawer rows
  ≥48px.
- **Breakpoints (v2).** ≥1200px: full bar — wordmark, six
  sheet links, Index, pulled count, mirror on demand.
  768–1199px: full bar; wordmark shortens to "MARLOWE" (the
  register's short name, §6.17). <768px: wordmark + mirror +
  Sheets button; links in the drawer panel.
- **Edge cases & failure modes (v2).** *More sheets than the
  bar holds (a project page with 38 sheets, §7):* the bar
  never lists 38 links — it lists the project's sheet
  *groups* (Elevations, Plans, Sections, Details, Schedules)
  and the index carries the 38. The bar's job is orientation
  on this table, not the catalogue. *Pulled count vs. strip
  disagreement:* impossible by construction — one list, two
  renderings (§6.10). *Sticky bar over the pinned hero:*
  the hero's pin (§6.1) reserves the bar's 72px in its
  sticky math.
- **Accessibility spec (v2).** Landmark header + `<nav
  aria-label="Sheets on this table">`; `aria-current` on the
  active link; the mirror is `aria-hidden` (§6.5). Skip link
  is the bar's first element, printed exposure on `--edge`,
  visible on focus. Link contrast: chalk on table 8.6:1 at
  rest, exposure on table 15.9:1 active.
- **Tokens consumed (v2).** `--table`, `--edge`, `--chalk`,
  `--exposure`, `--ease-fix`, `--ease-rule`, `--ease-slide`.

### 6.12 Vault index cards

- **What & why.** The index is the vault's catalogue made
  visible: a grid of miniature sheets, one per drawing, each
  carrying its №, title, scale and status, under a header
  line that states the vault's holdings from the register —
  "214 sheets · 9 projects · 3 out on loan". It belongs
  because a vault that cannot be browsed as a catalogue is a
  cupboard; the index is where the theme's discipline scales
  from six sheets to the whole practice.
- **Structure.** A `<ul>` of card `<li>`s, each card a small
  sheet: prussian ground, `--edge` border, a miniature title
  block strip at its foot (№, SCALE, DATE), the drawing's
  title in Archivo Expanded 1.5rem (the dead band's floor,
  §3), and a status line in chalk — "Filed", or for the
  three loaned sheets (A-077, A-078, A-080, §6.17) "Out on
  loan — back 4 April" with a chalk-dim badge. Each card is
  one link to its sheet. Cards group under project headings
  ruled as drawer labels; a filter row (project, sheet type)
  and a № search sit above the grid as ruled mono controls
  (§11).
- **Motion spec.** Cards arrive as small sheets do: §6.3's
  slide at card scale — 24px translate, 550ms `--ease-slide`,
  staggered 60ms per card in reading order as the grid
  crosses the reading line (a drawer being opened and its
  contents fanned). Hover: the card lifts (shadow +2px, tilt
  ≤1°) and its ground warms to `--prussian-raise`. Filtering:
  cards that leave fade 200ms `--ease-fix` and the grid
  reflows once, without animation — a drawer does not shuffle
  its contents theatrically.
- **States.** Filed (rest) / out on loan (badge, card still
  links to the sheet's record page — a loaned drawing can be
  read about, not pulled; its §6.10 control there is
  disabled) / pulled (the §6.10 cross prints on the card,
  synced with the sheet's own cross) / not yet drawn (a
  register placeholder: chalk-dim title "Not yet drawn", no
  link — the register admits the sheet is commissioned, not
  made).
- **Content merge.** Every field on a card is a register
  field (§6.17) — №, title, scale, date, status — and the
  header line's three figures are the register's totals,
  computed from the same rows the cards render. The grid is
  the register, handled one sheet at a time.
- **Failure fallback.** No-JS: the full grid prints, filters
  become a server-side form (project select + № field,
  submitted by GET), and the header line is server-rendered
  from the same register. Card arrival is enhancement only;
  a dead loop leaves a printed catalogue, complete.
- **Reduced-motion variant.** No fan, no stagger: the grid
  prints as a block. Hover lift is a ground change only
  (`--prussian-raise`), no tilt, no shadow travel.
- **Performance budget & mobile variant.** Cards are DOM and
  gradients — no images in the index at all (a catalogue of
  drawings is lettering and numbers; thumbnails would be
  exposures, and exposures live on sheets). Grid: 3 columns
  ≥1200px, 2 at 768–1199px, 1 below 768px. The full 214-card
  index paginates at 24 per page (§11) rather than growing —
  a drawer has a depth.
- **Choreography timeline (v2).** Grid crosses reading line
  → cards fan in, 60ms stagger → rest → filter change:
  leaving cards fade 200ms, grid reflows, arriving cards
  print (no fan on filter — the drawer is already open) →
  pull a sheet elsewhere: its card's cross prints in the
  same beat (§6.10).
- **State matrix (v2).** *Rest:* filed print. *Hover:* lift
  + raise ground + §6.9 underline on the title. *Focus:* the
  card link's outline (2px exposure, 3px offset) + raise
  ground; no tilt for keyboard. *Active:* press flattens the
  lift in 100ms, then navigates. *Scrolled-past:* printed.
  *Disabled:* loaned and un-drawn cards as above — present,
  explained, never hidden. *Touch:* no lift; tap navigates;
  targets are the whole card, ≥64px tall.
- **Breakpoints (v2).** ≥1200px: 3 columns, fan stagger 60ms.
  768–1199px: 2 columns, stagger 40ms. <768px: 1 column, no
  stagger (cards print in reading order as the grid is
  scrolled — arrival is §6.3's, at card scale, one by one).
- **Edge cases & failure modes (v2).** *A search with no
  match:* the grid empties into §6.18's unfiled state — the
  drawer shown open and empty, with the searched № repeated
  back. *A project with one sheet:* the group heading still
  rules — the register does not merge small projects to look
  fuller. *Register edited (a sheet withdrawn):* its card is
  removed at build; a bookmarked card URL lands on §6.18.
- **Accessibility spec (v2).** The whole card is one link
  with one accessible name ("A-103, Section through the pool
  hall, scale 1:50, filed"); status is text, never colour or
  badge alone. The header line is a heading-level summary,
  read before the grid. Filter controls are labelled form
  fields (§11), and result counts after filtering are
  announced politely ("38 sheets — Project 114").
- **Tokens consumed (v2).** `--prussian`, `--prussian-raise`,
  `--edge`, `--chalk`, `--chalk-dim`, `--exposure`,
  `--ease-slide`, `--ease-fix`.

---

### 6.13 The fixings schedule table

- **What & why.** Sheet A-105 is the project's Materials &
  Fixings Schedule as a true data table: five rows from the
  register (glulam bottom chords 7, top chords 7, web members
  70, M20 bolt sets 168, steel shoe plates 14) and a totals
  row carrying 266. It belongs because a schedule is the
  drawing office's other native document — the counted one —
  and the theme's law is tested hardest here: a table whose
  total does not equal its rows is the vault lying in its
  clearest voice.
- **Structure.** A semantic `<table>` with `<caption>`
  ("Materials & fixings schedule — sheet A-105, Project
  114"), scoped column headers (Item / Specification / Per
  truss / № required), tabular mono numerals throughout.
  Rows sit directly on the sheet's prussian; the totals row
  is separated by a double exposure-white rule — the
  draughting convention for a sum — and its figure is set in
  exposure white 600. The "Per truss" column is the table's
  honesty device: 1 / 1 / 10 / 24 / 2 per truss × 7 trusses
  (§6.17) derives every № required in view of the reader.
- **Motion spec.** The table does not animate beyond its
  sheet's arrival (§6.3) — a schedule is read, not performed.
  Its one motion: row hover draws a hairline dimension rule
  under the row in chalk over 200ms `--ease-rule`, the
  draughtsman underlining the row being checked, with §6.9's
  pencil on the item name. That restraint is specified, not
  omitted: the element a quantity surveyor uses is the
  element that never performs.
- **States.** Rest (printed, ruled) / row hover (chalk rule +
  pencil) / provisional (a row whose specification is under
  revision prints its figures in chalk-dim with a
  "Provisional" note in the specification cell — the table
  admits the state of its own evidence rather than hiding
  the row).
- **Content merge.** The table *is* sheet A-105 — its rows
  are the register's schedule (§6.17), its per-truss column
  shows the derivation, and its total is the same 266 the
  footer prints (§6.16) and §6.2's red mark underlines on
  this sheet. Three printings of 266, one register, audited
  in §10.
- **Failure fallback.** None required and none possible: the
  table is static HTML on a sheet that ships complete. No-JS
  is identical minus the hover rule. This element is the
  fallback's fallback — if everything else on the page
  failed, the schedule would still be standing, counted.
- **Reduced-motion variant.** Identical, minus the hover
  rule's draw (it appears whole).
- **Performance budget & mobile variant.** Zero script cost.
  Mobile (<768px): the table becomes a stacked schedule —
  each row a block with its figures in definition-list
  layout, same order, same totals, the double rule intact.
  Horizontal scrolling a schedule is forbidden: a total you
  must pan to read is a total lost.
- **Choreography timeline (v2).** Sheet arrival (§6.3) →
  table at rest → row hover: rule draws 200ms, pencil on the
  item name (§6.9) → leave: rule fades 150ms → the sheet's
  red mark (§6.2) underlines the 266 at arrival + 1000ms, as
  on every sheet.
- **State matrix (v2).** *Rest:* printed. *Hover:* row rule
  + pencil, as above. *Focus:* cells are not focusable; a
  row's item link (to its detail in the register) takes the
  pencil per §6.9. *Active:* n/a. *Scrolled-past:* printed.
  *Disabled:* provisional rows, as above. *Touch:* tap on a
  row holds its rule for 600ms (no pencil — §6.9's touch
  ruling).
- **Breakpoints (v2).** ≥1200px: full 4-column table.
  768–1199px: 3 columns (Per truss folds into the № required
  cell as a sub-line, "24 per truss × 7"). <768px: stacked
  schedule blocks.
- **Edge cases & failure modes (v2).** *A schedule with
  forty rows (a larger project):* the sheet paginates the
  table at 20 rows with subtotal rules per page and the
  grand total only on the last — a sum is printed once, at
  the end, or it is not a sum. *A zero-quantity row (a fixing
  designed out):* the row prints 0 and "Omitted at revision
  C" — an omission is scheduled, not deleted, so the count
  of rows still matches the register. *Print:* the table is
  the print stylesheet's centrepiece — full grid, double
  rule, prussian on white surrendered to ink economy (black
  on white in print; the sheet's data, not its colour, is
  the archive).
- **Accessibility spec (v2).** Real table semantics, caption
  and scoped headers; the totals row is a `<tfoot>` with
  `scope="row"`. Contrast: exposure on prussian 10.8:1;
  chalk-dim provisional figures 3.8:1 are always paired with
  the printed word "Provisional" — never colour alone.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--chalk`, `--chalk-dim`, `--ease-rule`.

### 6.14 The request-a-drawing form & its filed stamp

- **What & why.** Sheet A-106 is the vault's conversion: a
  visitor who needs a drawing — a client, an engineer, a
  student — files a request, and the request becomes a
  register entry. The sheet's preamble prints the derivation
  before a word is written: "46 requests are on file. Yours
  will be № 47." On filing, the confirmation is a filed slip
  and the sheet receives its one red mark at last — the FILED
  stamp (§6.2's reserved mark for A-106). It belongs because
  it is the only element where the visitor adds an entry to
  the register, and the theme's law holds there too: the
  number was promised before it was issued.
- **Structure.** A real `<form>` on the sheet, native
  validation semantics enhanced, never replaced: name, email,
  drawing № (a select of the register's sheets — the six on
  this table, then the project's other 32 by №, then "Any
  sheet in the vault — advise me"), and purpose (a short
  text field). Fields are ruled mono inputs on
  `--prussian-raise`, exposure text, labels above in chalk.
  The preamble line is part of the sheet's print. On success
  the form region is replaced by the filed slip: a ruled
  exposure-white slip (the palette's one light material, §2)
  with prussian print — request №, sheet №, the office's
  undertaking ("The sheet will be pulled within two working
  days") — and the red FILED stamp across its corner.
- **Motion spec.** Field focus: the field's ground lifts
  raise → a 6% exposure tint over 250ms `--ease-fix`, and
  its label takes §6.9's pencil if the pointer is the cause.
  Submit: the sheet dims to 70% over 300ms while the request
  is filed (a "Filing" state whose indicator is §6.15's
  unlit shimmer on the button — never a spinner). Success:
  the slip prints in with a 400ms `--ease-slide` rise; at
  t=200ms the stamp strikes — scale 1.3 → 1.0 in 120ms
  `--ease-hand`, a stamp's single blow — and holds. Error:
  the offending field's label gains a chalk asterisk and its
  error line prints beneath in chalk — no shake, no red,
  ever (§2).
- **States.** Rest (printed form, № 47 promised) / focus
  (per-field lift + pencil) / filing (sheet at 70%, fields
  disabled, shimmer on the button) / filed (slip + stamp;
  the form is gone — a filed request is not re-filable in
  place) / error (field marked in chalk, error line printed,
  focus moved to the first error, values preserved) / office
  closed (endpoint down: the sheet prints a chalk note —
  "The office is not filing tonight; requests resume at
  nine" — and holds the visitor's entries, unsubmitted and
  unlost).
- **Content merge.** The select's options are the register's
  sheets; the preamble's 46 is the register's count; the
  issued 47 is that count + 1; the stamp is the sheet's
  reserved red mark (§6.2); the slip is the palette's one
  paper object. The conversion is not decorated with the
  theme — it is transacted inside the register.
- **Failure fallback.** Watchdog at 4000ms on submission: no
  response restores the form from its 70% state with the
  office-closed note and values intact; the submit carries
  an idempotency token per form instance, so a retried
  filing can never issue two numbers. No-JS: native post;
  the confirmation is a server-rendered slip page with the
  same derivation (the server's register count + 1) and the
  stamp in print.
- **Reduced-motion variant.** The slip appears whole; the
  stamp is printed, not struck. Filing state is a printed
  "Filing…" label, no shimmer.
- **Performance budget & mobile variant.** The form's script
  is ≤5KB gz, deferred, and is the page's only non-loop
  script. Mobile (<768px): single column, fields full sheet
  width, the select becomes a ruled list of the six table
  sheets plus a № text field for the rest (a 38-option select
  on a phone is a drawer dumped on the floor); submit is
  full-width, ≥48px.
- **Choreography timeline (v2).** Focus field → lift 250ms →
  submit → sheet dims 300ms, shimmer → response → form
  region clears → slip rises 400ms → t=200ms stamp strikes
  120ms → slip at rest; watchdog ceiling 4000ms on the
  filing.
- **State matrix (v2).** *Rest:* form printed, № 47 promised.
  *Hover:* labels pencil per §6.9; fields lift on hover of
  the field itself. *Focus:* lift + chalk label brightens to
  exposure + 2px exposure outline. *Active:* filing state as
  above. *Scrolled-past:* the form waits; an in-flight filing
  completes regardless of scroll. *Disabled:* office-closed
  state as above. *Touch:* identical; field targets ≥48px.
- **Breakpoints (v2).** ≥1200px: two-column form (name +
  email side by side), measure 44rem on the sheet.
  768–1199px: single column, measure 38rem. <768px: single
  column full sheet width, select ruling as above.
- **Edge cases & failure modes (v2).** *A request for a
  loaned sheet (A-077):* accepted, and the slip adds the
  loan's return date — "Out on loan until 4 April; your
  request is first in the queue" — the register's facts,
  carried into the confirmation. *A request for a № that
  does not exist (typed in the mobile № field):* the error
  is the register's voice — "No sheet answers to that
  number. The index (§6.12) lists all 214" — and the field
  keeps the typed № for correction. *Double submission:*
  the idempotency token makes the second post return the
  same slip, № 47, never a № 48.
- **Accessibility spec (v2).** Visible labels on every field;
  errors use `aria-describedby` and a polite summary that
  reads the office's own words; the slip is an `aria-live`
  region announcing "Filed as Request № 47" once. Focus
  management: first error on failure, the slip's heading on
  success. The stamp is `aria-hidden` — the filing is in the
  text. Error text contrast: chalk on prussian 7.1:1.
- **Tokens consumed (v2).** `--prussian`, `--prussian-raise`,
  `--exposure`, `--chalk`, `--red`, `--ease-fix`,
  `--ease-slide`, `--ease-hand`, `--dur-watchdog-form`
  (4000ms).

### 6.15 Blank-sheet loader & the sheet-slide transition

- **What & why.** Loading in the vault is a blank sheet: a
  prussian sheet whose furniture is ruled (§6.7's crosses and
  frame) and whose line-work shimmers in as a pale band
  sweeps — the sheet being exposed before it is drawn. The
  page transition uses the same physics at sheet scale:
  leaving, the current sheet slides back toward the drawer;
  arriving, the next sheet slides in from the right over the
  light table. It belongs because a spinner would be a
  machine on the table; a blank sheet is the vault in its
  dormant state — the same object, not yet exposed.
- **Structure.** Skeleton regions are sheet-shaped DOM blocks
  carrying `data-blank` — prussian ground, ruled furniture,
  and a shimmer band (a `--uv-glow` gradient, 120px wide)
  sweeping vertically on a 1400ms loop while content loads.
  Content, when it lands, replaces the blank in place: the
  shimmer stops, the sheet's real furniture redraws per §6.7
  if it is a true sheet, and content prints with a 300ms
  `--ease-fix` settle. The transition is a mode of §6.3: the
  outgoing sheet translates −40px with its shadow falling
  (returning to the drawer), the incoming sheet runs §6.3's
  arrival from the right.
- **Motion spec.** Shimmer sweep 1400ms linear, continuous
  while blank — this is a loading state, not an ambient loop,
  and §5's two-loop licence is untouched because the shimmer
  exists only where content is genuinely absent. Hard
  ceiling: any region still blank at 1500ms prints whatever
  content it has, shimmer or not — the vault does not hold a
  reader hostage to a slow drawer. Transition: out 300ms,
  in 500ms `--ease-slide`; total perceived interruption
  ≤900ms, watchdogged at 2000ms.
- **States.** Blank (furniture + shimmer) / printing (300ms
  settle as content lands) / printed (rest) / failed (a
  region whose content errors: the blank's shimmer stops,
  the sheet prints a chalk note — "This sheet could not be
  pulled — [try again]" with a real retry control; a blank
  never shimmers forever).
- **Content merge.** The blank is shaped like the sheet it
  precedes and ruled with that sheet's furniture — the
  visitor sees the table being prepared for a specific
  drawing, and the transition's sheets are the actual pages
  leaving and arriving. Continuity of paper across pages is
  the theme's answer to the page boundary: it is one table,
  sheet after sheet.
- **Failure fallback.** Watchdogs per region (1500ms ceiling)
  and on the transition (2000ms — the destination forces its
  printed state; a transition may never strand a reader
  between tables). No-JS: no blanks, no transition; plain
  navigation between complete pages.
- **Reduced-motion variant.** Blanks are static ruled sheets
  (no shimmer) that swap to print instantly on data;
  transitions are plain navigations.
- **Performance budget & mobile variant.** The shimmer is one
  gradient transform per blank region; blanks are capped at
  two concurrent regions (a page skeleton is one sheet, not
  six). Mobile (<768px): shimmer band narrows to 80px,
  transition shortens (out 200ms / in 400ms), and the
  skeleton is cut entirely below the fold — off-screen
  content simply arrives printed.
- **Choreography timeline (v2).** Region requested → blank
  rules its furniture (200ms) → shimmer sweeps while loading
  → data lands → shimmer stops, content settles 300ms →
  printed. Ceiling 1500ms forces print. Transition: click →
  out 300ms → navigate → in 500ms (§6.3) → printed table.
- **State matrix (v2).** *Rest:* printed content. *Hover:*
  n/a on blanks. *Focus:* blank regions are `aria-hidden`
  and unfocusable until printed. *Active:* the request
  form's filing button carries this shimmer (§6.14).
  *Scrolled-past:* regions below the fold print on arrival
  regardless of visibility. *Disabled / no-JS:* server print,
  no blanks. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  full, shimmer 100px. <768px: static blanks above the fold
  only, shortened transition.
- **Edge cases & failure modes (v2).** *Data arrives before
  the blank paints (fast cache):* the region prints directly
  — a blank that never appears is the best kind. *Partial
  failure (the index grid loads, one card's data fails):*
  landed cards print; the failed card prints its chalk note
  in place — the drawer opens with the gap admitted.
  *Navigation mid-transition:* the watchdog belongs to the
  destination, so a double navigation still lands printed.
- **Accessibility spec (v2).** Blank containers carry
  `aria-busy="true"` and are removed from the accessibility
  tree until printed; one polite announcement ("Sheet
  loaded") fires when the last above-fold blank prints —
  never one per region. The transition is never announced.
  Retry note contrast: chalk on prussian 7.1:1.
- **Tokens consumed (v2).** `--prussian`, `--uv-glow`,
  `--chalk`, `--ease-fix`, `--ease-slide`,
  `--dur-blank-ceiling` (1500ms), `--dur-watchdog-transition`
  (2000ms).

---

### 6.16 The vault colophon footer

- **What & why.** The footer is the vault's colophon ruled as
  a final strip on the table's far edge: the register's
  totals printed a third time (214 sheets in the vault; 266
  items on sheet A-105; requests on file, 46 — or 47 once the
  visitor has filed, §6.14, the footer reads the same count
  the form read), the credits in title-block form (DRN JT ·
  CHK EM · Atelier Marlowe), and the theme's law restated in
  one line. It belongs because a set of drawings ends with a
  colophon — the sheet that says what the set contains and
  who answers for it.
- **Structure.** A `<footer>` on `--edge`, ruled top with a
  double exposure hairline (the schedule's sum rule, §6.13,
  closing the page as it closes a table). Three ruled
  columns: the totals (mono, computed from the register at
  build — and for the request count, at render), the
  colophon proper (the practice's name lettered, its address
  in mono, the copyright line), and the return link — "Back
  to sheet A-101" — set as a sheet link per §6.11. The fold
  creases of the last sheet (§6.7) end at the footer's rule:
  the table's edge is where the paper stops.
- **Motion spec.** The footer does not animate beyond the
  table's parallax settling (§5) as it arrives. Its one
  behaviour: the request count, if the visitor filed during
  the visit, is already 47 when they arrive — updated at
  filing time (§6.14), never theatrically recounted at the
  footer. Restraint is the spec: the colophon is print.
- **States.** Rest (printed) / after-filing (request count
  reads 47; all else identical — the register absorbed the
  entry without ceremony).
- **Content merge.** The footer's figures are the register's
  (§6.17) in their third printing — index header (§6.12),
  sheets, footer — and its credits are the same DRN/CHK
  initials every title block on the page carries. It closes
  the set by re-stating the set, which is what a colophon is.
- **Failure fallback.** Static HTML; nothing to fall back
  from. If the register count cannot be rendered (a build
  error), the footer prints the count's field blank with
  "—" rather than a wrong figure: the vault prints a gap
  before it prints a lie, and §10 fails the build.
- **Reduced-motion variant.** Identical — there is no motion
  to reduce.
- **Performance budget & mobile variant.** Zero script.
  Mobile (<768px): the three columns stack as three ruled
  rows; the double rule and the return link hold.
- **Choreography timeline (v2).** Last sheet (A-106) settles
  → 96px of table (§4) → footer rules into view with the
  scroll, printed → rest. No beats follow; the page ends the
  way a set of drawings ends.
- **State matrix (v2).** *Rest:* printed. *Hover:* the return
  link underlines per §6.9. *Focus:* outline per §6.9.
  *Active:* n/a. *Scrolled-past:* n/a — nothing is past the
  colophon. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three ruled columns.
  768–1199px: three columns, narrower measure. <768px:
  stacked ruled rows.
- **Edge cases & failure modes (v2).** *A visitor who files
  twice in one visit:* impossible (§6.14's idempotency), so
  the count can only ever be 46 or 47 — the footer's two
  states are exhaustive. *Register growth between builds:*
  the totals are build-time renders of §6.17; a register
  edit that forgets the footer fails §10's three-printings
  audit, by design.
- **Accessibility spec (v2).** The footer is a contentinfo
  landmark; totals are a definition list, read as figures
  with their labels. Contrast: exposure on edge 14.1:1,
  chalk on edge 9.2:1.
- **Tokens consumed (v2).** `--edge`, `--exposure`, `--chalk`.

### 6.17 The drawing register — the one source of every figure

- **What & why.** The register is the theme's single data
  object: the vault's catalogue record from which every
  figure on every sheet derives. It exists as an element —
  rendered on the register page (§7) as ruled tables, and
  present on every other page as the data behind the print —
  because the law (§1) needs a source that can be audited.
  If a number on a sheet is not in this section, it does not
  go on the sheet.
- **Structure.** One declared record, in five parts.
  **(a) The vault:** Atelier Marlowe (short name MARLOWE,
  §6.11); 214 sheets; 9 projects; 3 sheets out on loan —
  A-077, A-078, A-080, back 4 April 2026; 46 requests on
  file. **(b) The project:** № 114, the Kestrel Street Baths,
  restoration; 38 sheets; drawn by J. Teale (DRN JT),
  checked by E. Marlowe (CHK EM). **(c) The six sheets on
  this table:** A-101 North Elevation, 1:50, issued 14 Mar
  2026; A-102 Ground Floor Plan, 1:100, 14 Mar 2026; A-103
  Section A–A through the Pool Hall, 1:50, 21 Mar 2026;
  A-104 Roof Truss Detail T1, 1:20, 21 Mar 2026; A-105
  Materials & Fixings Schedule, NTS, 28 Mar 2026; A-106
  Request Sheet, NTS, the live sheet. **(d) The building, in
  millimetres:** overall width 24,000 = 6 bays × 4,000;
  overall height 12,400 = plinth 600 + plinth-to-eaves 9,000
  + eaves-to-parapet 2,800 (eaves line 9,600); footprint
  depth 15,000; pool hall 18,000 long; pool 12,500 × 6,000,
  water depth 1,800, volume 12.5 × 6.0 × 1.8 = 135 m³;
  section clear height 7,200; truss depth 1,200; truss span
  15,000; 7 trusses (T1–T7) at 4,000 centres; chord section
  240 deep; bolt gauge 80. **(e) The schedule (A-105):**
  bottom chords 7 (1 per truss), top chords 7 (1), web
  members 70 (10), M20 bolt sets 168 (24), shoe plates 14
  (2) — total 7 + 7 + 70 + 168 + 14 = 266 items. **Derived
  drawn sizes:** A-101 at 1:50 draws 480 × 248; A-102 at
  1:100 draws 240 × 150; A-103's span at 1:50 draws 300, its
  clear height 144; A-104 details a 3,000 segment drawing
  150 at 1:20, its chord 12, its gauge 4. **Exposures:**
  E-01 the baths from Kestrel Street (on A-101); E-02 the
  pool hall from the deep end (A-103); E-03 truss T4 as built
  (A-104); E-04 the studio's drawing office (About sheet,
  §7). **Red marks (§6.2):** A-101 circles 9,600; A-102 ticks
  12,500; A-103 circles 1,800; A-104 ticks 80; A-105
  underlines 266; A-106's is the FILED stamp.
- **Motion spec.** The register does not move. On its own
  page it is printed in ruled tables that arrive with their
  sheet (§6.3) and are thereafter still. Everywhere else it
  is data, and data has no motion spec — the elements that
  render it carry theirs.
- **States.** Filed (the rest state) / amended (a revision
  prints as a new row with its revision letter — C is the
  current revision of A-105 — never as a silent edit; the
  superseded row moves to the register's revision table,
  struck in chalk, kept).
- **Content merge.** The register is not *on* the site; the
  site is the register, rendered. Title blocks (§6.5), index
  cards (§6.12), the schedule (§6.13), the form's count
  (§6.14), the footer's totals (§6.16) and every dimension
  (§6.4) are views of this one record — which is why §10 can
  audit them against each other.
- **Failure fallback.** If a rendered figure and the register
  disagree, the register wins and the build fails (§10) —
  the fallback for a data object is an audit, not an
  animation. A figure that cannot be sourced renders as a
  printed gap (§6.16's ruling), never an estimate.
- **Reduced-motion variant.** Identical; there is nothing to
  reduce.
- **Performance budget & mobile variant.** The register is a
  build-time data file (JSON or front-matter), ≤8KB for the
  worked project; rendering is static. On its page, mobile
  stacks its tables per §6.13's rule.
- **Choreography timeline (v2).** None — and that is the
  specification. The register's only timeline is its revision
  history: issued March 2026, revision C current, each
  amendment dated and initialled in the revision table.
- **State matrix (v2).** *Rest:* filed, revision C.
  *Hover / focus / active:* n/a — it is rendered by other
  elements, whose matrices govern. *Scrolled-past:* n/a.
  *Disabled:* a withdrawn sheet's row prints struck, with
  "Withdrawn" and the date — absence is recorded, not
  erased. *Touch:* n/a.
- **Breakpoints (v2).** On the register page: ≥1200px the
  five parts rule as five tables on one sheet; 768–1199px
  they stack on two sheets; <768px stacked blocks per §6.13.
- **Edge cases & failure modes (v2).** *Two projects with a
  sheet № in common:* impossible — №s are vault-unique
  (A-077 belongs to one project only), enforced by the
  register's key. *A figure needed by copy that the register
  lacks (a marketing claim — "214 sheets" is fine, "hundreds
  of projects" is not):* copy may only spend register
  figures; §12's voice rules route every number through this
  section. *Rounding:* the register stores integers (mm,
  counts); any derived figure (§6.4's counting callouts)
  rounds to whole units and lands exact at rest.
- **Accessibility spec (v2).** On its page, the register is
  real tables with captions and scoped headers (§6.13's
  discipline); derivations are printed as text ("24,000 =
  6 bays of 4,000"), so the arithmetic is available to every
  reader, not only to those who can see a dimension line.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--chalk`, `--chalk-dim`.

### 6.18 The unfiled sheet — empty state & 404

- **What & why.** Where the vault finds nothing — an index
  search with no match, a sheet № that does not exist, a
  page never drawn — the answer is an unfiled sheet: a sheet
  with its furniture ruled and its title block printed, whose
  drawing area is blank blue, headed in the register's voice:
  "Not in the register." It belongs because absence in a
  vault is a catalogue fact, not an error: the sheet was
  never drawn, and the vault says so on a sheet, with the
  exits ruled as real links (the index, sheet A-101, the
  request sheet — an unfiled drawing is a plausible reason to
  file a request).
- **Structure.** A sheet per §4: furniture (§6.7) drawn,
  title block present with its fields reading DRG "—",
  SCALE "—", DATE "—", DRN "—", CHK "—" (an unfiled sheet
  has no papers because it has no existence), the heading
  lettered in Archivo, one chalk line of explanation, and
  the three exits as sheet links. Notably: **no red mark** —
  the checker never touched this sheet, because there is
  nothing to check; the red census (§10) expects zero red
  here, and a build that decorates its 404 with the pencil
  has misunderstood the ration. The empty-state variant (in
  the index, §6.12) is the same sheet at card scale: the
  drawer shown open, the searched № repeated back.
- **Motion spec.** The sheet arrives per §6.3 (it is a sheet)
  and its furniture rules per §6.7 — and then nothing. The
  blank does not shimmer (§6.15's shimmer means *loading*;
  this sheet is not loading, it is absent, and the
  distinction is the design). No ambient motion reaches the
  blank area; the UV pulse (§5) passes over the table, not
  across the unfiled sheet.
- **States.** Unfiled (the only state) / searched (the index
  variant, carrying the visitor's № in its chalk line:
  "No sheet answers to A-999.").
- **Content merge.** The unfiled sheet is the register's
  negative space made visible — its title block's dashes are
  the register's fields with no values, and its exits are
  the vault's real doors. It is the one sheet whose content
  is the fact of its own absence.
- **Failure fallback.** The 404 is a static sheet; it is what
  other elements fall back *to*. It must itself work with
  no script, no loop and no register fetch — it is
  server-rendered from a static template, because the page
  that answers for missing things may not itself go missing.
- **Reduced-motion variant.** Identical, minus the arrival
  slide — print, as ever.
- **Performance budget & mobile variant.** The lightest page
  on the site: one sheet, no images, no loop work beyond the
  table's ambient. Mobile: the sheet stacks per §4; the
  exits become full-width ruled rows, ≥48px.
- **Choreography timeline (v2).** Arrival slide (700ms,
  §6.3) → furniture rules (800ms, §6.7) → stillness. The
  timeline's brevity is the specification: two beats, then a
  blank that means it.
- **State matrix (v2).** *Rest:* unfiled print. *Hover:* the
  exit links underline per §6.9. *Focus:* outline per §6.9.
  *Active:* n/a. *Scrolled-past:* n/a (the page is one
  sheet). *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full sheet, heading at the
  sheet-title size. 768–1199px: full sheet. <768px: sheet
  per §4's mobile geometry, exits stacked.
- **Edge cases & failure modes (v2).** *A № that exists but
  is out on loan:* not a 404 — the sheet's record page (§7)
  prints its loan status (§6.12); the unfiled sheet answers
  only for true absence. *A search so broad it matches
  nothing by error (a malformed query):* the chalk line
  prints the query as received — the vault repeats what it
  was asked, so the visitor can see their own typo filed.
  *Server error (500):* never this sheet — a failure is not
  an absence, and §6.14's office-closed note is the model
  for honest failure language instead.
- **Accessibility spec (v2).** The heading is the page's h1;
  the response is a real 404 status. The blank area is
  `aria-hidden` emptiness — the explanation line carries the
  whole meaning in text. Exit links are ordinary links with
  ordinary names. Contrast: exposure on prussian 10.8:1,
  chalk 7.1:1.
- **Tokens consumed (v2).** `--prussian`, `--exposure`,
  `--chalk`, `--edge`, `--ease-slide`.

---

## 7. Page application map

- **Home — the table with six sheets.** The worked page of
  this expansion: hero sheet A-101 (§6.1), then A-102 (plan),
  A-103 (section, carrying exposure E-02, §6.8), A-104
  (truss detail), A-105 (the schedule, §6.13), A-106 (the
  request form, §6.14), the colophon (§6.16). The edge
  dimension line (§5) rules the whole descent.
- **Vault index — the catalogue.** §6.12's grid over all 214
  sheets, grouped by the 9 projects under drawer-label
  headings, filters and № search above, the pulled strip
  (§6.10) at its head when non-empty. Pagination at 24 —
  the index is the one page allowed to be long, because a
  catalogue is a tool, not a story.
- **Sheet detail — one drawing, large.** A single sheet at
  the table's full width: the drawing at its largest honest
  size, all its dimensions live (§6.4), its exposures fixed
  (§6.8), its title block (§6.5), its Pull control (§6.10),
  and ruled links to the previous and next sheets in the
  register ("Next sheet A-104") — the register's order is
  the pagination. Loaned sheets render here in full with
  their status line; the drawing is readable, only the
  pulling is disabled.
- **Project page — one project's drawer.** The project's
  register part (§6.17b/d) as a head sheet — the building's
  figures as a dimensioned summary — followed by its sheets
  as §6.12 cards and its schedule as §6.13's table. Project
  114's page is the worked example's natural home.
- **About — the office as a sheet.** The practice's own
  sheet: unnumbered in the A-series (it takes sheet №
  "O-001", Office series — the register's one joke, and it
  is filed, so it is not a joke but a convention), carrying
  exposure E-04 (the drawing office), the principals as a
  DRN/CHK table, and the vault's holdings stated from the
  register. Even the marketing page is a sheet with papers.
- **Request / contact — sheet A-106 standalone.** The same
  form (§6.14) on its own page for visitors who arrive with
  intent; the preamble's count is the register's, the slip
  identical. One form, two tables — never two forms.
- **Register page — the record itself.** §6.17 rendered in
  full: five ruled tables, the revision table, the loan
  list. The page auditors and engineers bookmark.
- **404 — the unfiled sheet.** §6.18.
- **Checkout — refused the theme.** The vault lends drawings
  and files requests; it does not sell. Any commercial flow
  (booking a consultation, paying for prints) leaves the
  theme at the door: it is handed to the practice's ordinary
  booking page, and the request form's purpose field is
  where commercial intent is *declared*, in words, like
  everything else here.

---

## 8. Worked examples

### 8.1 The hero — sheet A-101 is exposed (worked example 1)

The visitor lands on the light table. The masthead (§6.11)
is printed, its hairline ruling in. Below it, the hero sheet
lies exposed in its no-JS face — headline "The Kestrel Street
Baths, drawn at 1:50", the elevation complete — for exactly
one frame; then the script arms the exposure. The sheet
blanks to prussian (line-work wrapper to blur 6px, opacity
0.25), the UV bar enters at the sheet's head, and over
1600ms it travels down: the lettering blooms first — *The
Kestrel Street Baths* resolving out of the chemical fade —
then the elevation's lines, bay by bay, the six bays of the
24,000 width appearing as the light passes them. At 900ms
the title block's SCALE field steps 1:200 → 1:100; at
1700ms the bar leaves at the foot, the field lands on 1:50
and takes its chalk tick. Dimension lines draw last, 600ms:
the overall width line extends beneath the elevation and its
callout counts to 24,000 mm — 480 drawn units × 50, the
sheet measuring itself in view. At 2600ms the red pencil
circles the 9,600 eaves dimension — the sheet's one mark,
the checker directing the eye to the height that matters.
The sheet pins for 120vh while this completes; then the
table begins to move, and A-101 is simply the first filed
sheet of six. Every figure the visitor has seen — 24,000,
9,600, 1:50 — is in §6.17, and §10 will audit all three
printings of each.

### 8.2 Mid-page — the section sheet and its water (worked example 2)

Halfway down the table, sheet A-103 slides in (§6.3): the
Section A–A through the Pool Hall. Its furniture rules
(§6.7); its drawing — the section at 1:50, span drawn 300
units — sits in its frame with exposure E-02, the pool hall
photograph, unfixed at the sheet's side. As the visitor
scrolls the sheet through the centre band, two measurements
happen at once, both scrubbed to the same lerped progress:
the span dimension extends outside the frame and its callout
counts to 15,000 mm (300 × 50), while E-02 fixes — scale
1.04 → 1.0, contrast settling, blur resolving — the
photograph developing beside the drawing it verifies. The
section's second dimension, the 1,800 water depth, prints
fully drawn on mobile and scrubs on desktop; it is the
figure the red pencil circles at settle + 300ms — the
checker cares about the water, because the water is what a
baths is for, and the volume it makes (135 m³) is stated in
the sheet's chalk note beneath the drawing, derived in
§6.17 where any reader can redo it: 12.5 × 6.0 × 1.8. The
visitor leaves the sheet having watched a drawing measured
and a photograph developed, and both acts were the content.

### 8.3 Conversion — a request is filed as № 47 (worked example 3)

The last sheet, A-106, arrives with its preamble already
printed: "46 requests are on file. Yours will be № 47." An
engineer — the worked visitor — needs the truss detail. She
chooses A-104 from the select (the register's sheets, in
register order), writes her name and email, and in Purpose:
"Checking the T4 connection against the as-built shoe
plates." The fields lift as she focuses them (§6.14); the
labels take the pencil when her pointer passes. She submits.
The sheet dims to 70%; the button shimmers — Filing. At
900ms the response lands: the form region clears, and the
filed slip rises — exposure white, prussian print: "Request
№ 47 — Sheet A-104, Roof Truss Detail T1. Filed 23 November
2026. The sheet will be pulled within two working days." At
slip + 200ms the stamp strikes: FILED, in the draughtsman's
red, across the slip's corner — sheet A-106's one red mark,
unspent until this moment, spent now on the only act that
could earn it. When she scrolls to the colophon (§6.16),
the register line already reads "Requests on file: 47". She
was promised the number before she wrote a word, and the
vault kept the promise in three places she can check.

---

## 9. Anti-slop — what makes THIS theme look cheap

- **Blueprint as wallpaper.** A blueprint texture behind
  ordinary web content — hero text over a faint grid, cards
  with "blueprint styling". The cure: blue is the *sheet*,
  and a sheet carries a drawing, a title block and dimensions
  or it is not in the theme. Texture without apparatus is
  the failure this whole expansion exists to prevent.
- **The lying scale.** A title block that says 1:50 over a
  diagram drawn at no scale at all. The cure is mechanical:
  diagrams are drawn in unit-true viewBoxes (§6.1, §6.17)
  and §10 measures them. A scale that cannot survive a ruler
  is clip-art.
- **Red everywhere.** Red hover states, red buttons, red
  "sale" energy — the pencil spent as a brand colour. The
  cure: the census (§2, §10). One mark per sheet at rest;
  the pencil is lent, never given.
- **Decorative dimension lines.** Arrows and measurements
  that span nothing, callouts with invented numbers ("1200"
  beside a chair). The cure: every dimension group is one
  SVG with its diagram (§6.4) and every callout is computed
  from the register by the printed formula.
- **Lorem title blocks.** "DRG NO. XXX / SCALE 1:XX / DATE
  XX/XX" — papers as set dressing. The cure: blocks render
  from §6.17 or the sheet does not ship; §10 greps for
  placeholder patterns.
- **Untreated photography.** A full-colour photo dropped
  onto a blue sheet "for contrast". The cure: every image is
  an exposure (§6.8) with a register №, or it is data in a
  table (§6.13) — never a colour photograph pasted into the
  chemistry.
- **Blank-blue failure.** The exposure effect running, the
  script failing, the sheet staying blank — the theme's
  signature catastrophe. The cure is architectural: the
  shipped DOM is the finished sheet (§6.1, §6.3) and every
  pre-state is armed, watchdogged, and reversible. A build
  that can strand a sheet is rejected at §10 regardless of
  how it looks with the script alive.
- **Bouncy paper.** Elastic easings, sheets overshooting,
  tilt past 2°, parallax at landscape rates. Paper is heavy,
  flat and damped; the cure is §5's easing set and lerp 0.09
  — motion with the physics of the material, not of a UI kit.
- **The UV bar as a shine sweep.** The light bar reused as a
  generic gloss over buttons and cards. The cure: the bar
  exists in §6.1 and §6.15 only, where something is actually
  being exposed. Light that exposes nothing is a screensaver.
- **Counters to round numbers.** Stats counting to "250+
  projects" or "15 years" — marketing figures in a register's
  clothing. The cure: counters land on register figures
  (§6.17) or they do not run; §12 bans the claims themselves.
- **Fold creases as grunge.** Random crease and stain overlays
  for "character". The cure: creases are at the sheet's third
  points, ruled by §6.7, identical in geometry across sheets —
  a fold is a fact about a sheet's history, not a texture pack.
- **Title-block cosplay on non-sheets.** Title blocks stamped
  on modals, toasts and footers-as-jokes until the papers mean
  nothing. The cure: blocks belong to sheets (§6.5); the
  footer is a colophon (§6.16), the 404's block is dashed
  (§6.18) — the exceptions are specified, singular, and mean
  something each.

---

## 10. Quality gate

Blocking checks; a build that fails any one does not ship.
The gate is signed by someone who did not build the page.

- **Blank-sheet drill.** Disable the script's loop mid-load,
  throttle the network, and kill the observer: every sheet
  must reach its fully printed state via watchdogs alone,
  hero included. Any sheet that can stay blank blue fails.
- **No-JS read.** The whole page, script off: every sheet
  exposed, every dimension drawn, every callout at its true
  figure, the form submittable, the register complete.
- **Scale-truth audit.** For each dimensioned diagram:
  measure the rendered SVG's drawn units, multiply by the
  title block's scale denominator, compare with the callout
  and with §6.17. A-101 must read 480 × 50 = 24,000. Any
  mismatch fails.
- **Figure audit, three printings.** 24,000 / 12,400 / 9,600
  / 15,000 / 1,800 / 266 / 214 / 46 (or 47 post-filing) /
  135 m³ — each figure must agree everywhere it prints:
  register, sheets, index header, footer. One disagreement
  fails.
- **Red census.** Count red strokes per sheet at rest in the
  shipped DOM: exactly one on A-101…A-105, zero on A-106
  until filing, zero on the 404. Grep the CSS: `--red` may
  be consumed only by §6.2's marks, §6.9's underline and
  §6.14's stamp.
- **Derivation audit.** Recompute the register by hand from
  its parts: 6 × 4,000; 600 + 9,000 + 2,800; 7 × 24;
  7 + 7 + 70 + 168 + 14; 12.5 × 6.0 × 1.8. The register must
  survive its own arithmetic.
- **Watchdog drill.** Hero 3000ms, sheets 2500ms, form
  4000ms, transition 2000ms, blank ceiling 1500ms — force
  each to fire and confirm the printed end state.
- **Reduced-motion pass.** With the preference set: no sweep,
  no slide, no scrub, no shimmer — and no content missing,
  no figure unprinted, no state unreachable.
- **Cursor check.** The system cursor everywhere; no custom
  cursor, no cursor follower, no exception requested.
- **Contrast audit.** Body print exposure on prussian
  (10.8:1), annotations chalk (7.1:1), provisional chalk-dim
  always paired with words; red never carries text.
- **Dead-band grep.** No font-size between 1.0625rem and
  1.4375rem in the shipped CSS (§3).
- **Placeholder grep.** No lorem, no "XXX", no "1:XX", no
  untitled sheet, no dimension without a register source.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Components the theme refuses are listed
with their refusal and their in-world replacement.

- **Buttons.** Ruled mono rectangles, exposure print on
  prussian-raise; the primary action on a sheet is its Pull
  control or its form submit, labelled in the office's verbs
  ("Pull for review", "File the request"). Press: ground
  deepens to `--edge` in 100ms. No pill shapes — paper has
  corners.
- **Links.** Chalk, underlined on hover/focus by the pencil
  (§6.9). In body text, links are exposure white with a
  chalk underline at rest — a link must be findable without
  the pencil.
- **Inputs & textarea.** Ruled mono fields on
  `--prussian-raise` (§6.14), labels above in chalk, focus
  lift + outline. Errors in chalk with words, never red.
- **Select.** A ruled mono select; on mobile it becomes the
  ruled list + № field of §6.14.
- **Checkbox / radio.** Drawn as small ruled squares/circles
  in exposure white; the checked state is a chalk tick drawn
  in the box — a hand mark, in chalk, because a visitor's
  tick is not the checker's red.
- **Table.** §6.13's schedule discipline: caption, scoped
  headers, double rule over totals.
- **Badges.** One badge exists: status on index cards
  (§6.12) — a chalk-dim ruled tag ("Out on loan"). No other
  badges; the vault does not sticker its sheets.
- **Alerts / notices.** A chalk notice strip ruled top and
  bottom on the sheet it concerns (§6.14's office-closed
  note is the type specimen). Dismissible only where the
  information is transient; register facts are never
  dismissible.
- **Pagination.** Sheet-order links ("Next sheet A-104") on
  detail pages; numbered pages on the index, set as drawing
  numbers of pages ("Page 3 of 9") in mono.
- **Modal — refused.** A drawing is viewed on its own sheet
  page (§7), never in a lightbox floating over the table;
  sheets do not float. Dialogues that are genuinely needed
  (confirming a return-to-drawer) are handled inline on the
  sheet.
- **Toast — refused.** Confirmations are filed, not floated:
  the form answers with a slip (§6.14), the pull with a
  cross and a strip (§6.10). Nothing in the vault appears
  and vanishes.
- **Tabs — refused.** Sheets stack and drawers group; a
  project page's groups are ruled sections, not tabs. The
  table has no hidden panels.
- **Accordion.** Index groups by project open as drawer
  sections — a ruled heading row that slides its cards in
  per §6.12; one drawer open at a time on mobile.
- **Tooltip — replaced.** The theme's tooltip is the
  dimension callout: information appears as annotation on
  the thing itself, chalk mono, never as a floating hint.
  Where a control needs a hint, its label is lengthened
  instead.
- **Progress.** The edge dimension line (§5) is the only
  progress indicator; spinners and progress bars are refused
  — loading is a blank sheet (§6.15).
- **Breadcrumb.** A ruled mono line in register order:
  Vault / Project 114 / A-103 — the filing path, which is
  what a breadcrumb is in an archive.
- **Search.** The index's № search (§6.12): a mono field
  labelled "Sheet №", submitted, answered by the grid or by
  §6.18's searched state.
- **Cards.** §6.12's miniature sheets; no other card style
  exists in the theme.
- **Form errors.** §6.14's chalk asterisk + printed error
  line + summary; the pattern is reused by every form.
- **Skip link.** §6.11's — exposure on edge, first in the
  bar, visible on focus.

---

## 12. Content & copywriting voice

Two registers, matching the two inks.

**The Sheet** — printed matter: titles, body, the register's
prose. Terse, factual, dimensioned. Statements that could be
checked are the only statements allowed. Headlines are
lettered as facts with their measurements attached: "The
Kestrel Street Baths, drawn at 1:50", not "Reimagining a
Victorian icon". Body sentences are short; a sentence that
needs a comma splice needs a dimension instead.

**The Draughtsman** — annotations: chalk notes, error lines,
empty states, the form's voice. First person plural of the
office ("We file requests in the order they arrive"),
dry, kind, exact. The draughtsman never sells; he annotates.
Errors are stated as register facts with the correction
offered: what was asked, what exists, where to look.

**Rules.**

- Every number in copy comes from §6.17 or is not printed.
  "214 sheets" ✓. "Hundreds of drawings" ✗ — the register
  knows the count; use it or say nothing.
- Claims are dimensions or they are cut. "A hall of 18,000
  millimetres, daylit from the truss" ✓. "A stunning,
  state-of-the-art leisure destination" ✗ — three adjectives
  and no fact is the voice's definition of slop.
- Verbs are the office's: draw, rule, check, file, pull,
  expose, fix, lend, return. Marketing verbs (elevate,
  unlock, supercharge, revolutionise) are banned outright.
- Dates are written in full — "14 March 2026" — as the title
  blocks print them. No relative dates on sheets ("3 days
  ago" is a feed's voice, not a register's).
- Fixed strings, verbatim, everywhere they occur: the form
  preamble "46 requests are on file. Yours will be № 47."
  (numbers from the register); the slip's undertaking "The
  sheet will be pulled within two working days."; the
  unfiled heading "Not in the register."; the searched line
  "No sheet answers to that number."; the office-closed note
  "The office is not filing tonight; requests resume at
  nine."; the loan line "Out on loan — back 4 April." Fixed
  strings are the register's voice made repeatable; they are
  never paraphrased by a page that finds them inconvenient.

**Examples.** Headline — ✓ "Section through the pool hall,
at the water's depth of 1,800" / ✗ "Dive into our most
immersive project yet". Error — ✓ "No sheet answers to
A-999. The index lists all 214." / ✗ "Oops! We couldn't find
that page 😢". Empty state — ✓ "Not in the register." /
✗ "Nothing here… yet!" Button — ✓ "File the request" /
✗ "Get started →".

---

## 13. Full-page scroll choreography map

The home page, top to footer, in order. Every beat is
latched unless stated; the visitor scrolling back up meets a
table already worked — sheets filed, dimensions held,
photographs fixed — because the office does not un-work its
work.

1. **Load.** Masthead prints; its hairline rules in (400ms).
   The hero sheet arms its exposure (§6.1).
2. **The exposure.** UV bar travels (1600ms); lettering and
   elevation bloom; SCALE steps at 900/1700ms (§6.6);
   dimensions draw (600ms); the red pencil circles 9,600 at
   2600ms (§6.2). The sheet pins through 120vh.
3. **Descent begins.** The edge dimension line (§5) starts
   lengthening from 0; its first callout, 120, passes as the
   hero unpins.
4. **Sheet A-102 arrives** (§6.3): slide, furniture, the
   plan's dimensions scrubbing as it centres (§6.4) — the
   pool's 12,500 counting up; red tick at settle + 300ms.
5. **A-103, the section** (§8.2): span dimension scrubs to
   15,000 while E-02 fixes beside the drawing; the pencil
   circles the 1,800 water depth.
6. **A-104, the detail:** the 240 chord dimension and the 80
   gauge print at detail scale — small numbers, drawn large;
   the gauge takes the sheet's tick. Edge line passes 240.
7. **A-105, the schedule:** the table arrives already counted
   (§6.13); the pencil underlines 266. Nothing on this sheet
   scrubs — the visitor is reading figures now, and the page
   respects the change of work.
8. **A-106, the request:** the preamble's promise is read;
   if the visitor files, §8.3's sequence runs — dim, shimmer,
   slip, stamp — the page's only red still unspent until now.
9. **The colophon** (§6.16): the totals a third time; the
   edge line completes at 480 as the footer's rule is
   reached — the visitor has travelled exactly one hero-sheet
   width down the table, and the page says so in millimetres.

**Reverse pass.** Scrolling up: dimensions within their
bands retract symmetrically (§6.4 — the one reversible act,
because measuring is live); everything else holds. Sheets do
not un-slide, exposures do not un-fix, the stamp does not
un-strike. **Jump scroll:** watchdogs place everything above
the landing point in its final state (§6.3); the visitor who
arrives by anchor finds a worked table, never a drawer
mid-swing.

---

## 14. Whole-page performance budget

- **Page weight.** ≤720KB total for the home page: HTML/CSS/
  JS ≤210KB (the loop, scrollspy, form and exposure logic —
  no framework; a theme this ruled does not need one),
  fonts ≤120KB (Archivo Expanded two weights, subset to
  Latin + figures; Plex Mono two weights), images ≤390KB
  (four exposures at ≤180KB each would break this — the home
  page carries two, E-01 and E-02; E-03 and E-04 live on
  their sheets' detail pages).
- **Frame budget.** The shared loop's per-frame work —
  scroll lerp, dimension scrub, exposure scrub, tilt — is
  ≤1.2ms on a mid-tier laptop, ≤2.5ms on a low-power phone,
  measured with the hero pin active (the worst case). At
  most two scrubbed elements animate concurrently (§4's
  density makes this structural, not hopeful).
- **Long tasks.** No task over 50ms after first paint; the
  exposure's arming is one frame's work, fonts are
  `font-display: swap` with the printed state as the fallback
  face (a sheet in a fallback mono is still a sheet).
- **Ambient cost.** The two licensed loops (§5) are one
  gradient opacity and a 40-particle transform field —
  ≤0.3ms/frame combined, paused when the tab is hidden and
  when the hero leaves the viewport for good.
- **Cut order when the budget is exceeded.** First: dust
  motes (the light reads without them). Second: paper-fibre
  shift. Third: sheet tilt on hover. Fourth: parallax layer
  separation (the sheet moves as one). Fifth: the hero pin
  (the exposure still runs, unpinned). **Never cut:**
  watchdogs, title blocks, the dimension system, the red
  ration, the no-JS printed state — the budget is spent on
  ceremony before it is ever spent on truth.

---

## 15. Build-order checklist

The sequence in which the theme is implemented; each step
leaves the page shippable.

1. **The register first.** Encode §6.17 as the data file.
   Nothing renders before the record exists — a builder who
   starts with the hero will invent figures the register
   must later disown.
2. **Static sheets.** Build every sheet as finished print:
   drawing, title block, dimensions drawn, callouts true,
   marks made. This is the no-JS face, and it is built
   before any motion exists.
3. **The duotone.** Apply §6.8's filter to all imagery;
   verify untreated fallbacks.
4. **The masthead and mirror.** Navigation, scrollspy,
   §6.5's mirror with its watchdog.
5. **The index.** Cards from the register, filters, the
   pulled strip's server-rendered form.
6. **The schedule table and the register page.** The counted
   documents; run the derivation audit (§10) now, while the
   figures are young.
7. **The form.** Native first, then the enhanced filing,
   the slip, the stamp; idempotency before styling.
8. **The loop.** The shared rAF loop and the lerp; wire
   scroll progress (the edge dimension) to it.
9. **Sheet arrivals.** §6.3's slide with watchdogs; jump-
   scroll behaviour verified.
10. **The furniture draw.** §6.7, sequenced inside arrivals.
11. **Dimension scrubbing.** §6.4, including the shipped-
    drawn fallback logic; scale-truth audit (§10).
12. **Fixing exposures.** §6.8's scrub and latch.
13. **The hero exposure.** §6.1 + §6.6, armed pre-states,
    session rule, 3000ms watchdog — last of the ceremonies,
    because it depends on everything beneath it being true.
14. **The pencil.** §6.9's underline node, then §6.2's marks
    — red is added to a finished page, counted as it lands.
15. **The gate.** §10 in full, signed by a non-builder:
    blank-sheet drill, no-JS read, audits, census. Only then
    may the theme be used in a build.
