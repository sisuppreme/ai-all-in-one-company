# 51. Quarry Cut — Expanded (v1 + v2)

> Source entry: themes-051-075.md §51. Identity preserved exactly: the page
> is a block of stone being cut — sections are slabs separated by saw cuts,
> specifications read like quarry tickets, the hero is a fresh-cut stone face
> with the saw marks still on it. Same five palette anchors (Fresh cut
> `#D9D4C8`, Sawn face `#A9A294`, Wet stone `#6E6A5E`, Core dark `#33322C`,
> Survey orange `#C75B27`), same three typefaces (Archivo Expanded display,
> Archivo prose, IBM Plex Mono for specifications), all ten original
> signature elements deepened, plus eight page-family elements to 18 total.

## 1. Concept & world

A Quarry Cut page is not decorated like a quarry; it is *worked* like one.
The page arrives as a single block of stone. The hero is the block's fresh
face, still carrying the circular saw's scoring. Every major section below
it is a slab that has been cut from that block and craned into place, and
the seams between sections are not borders or whitespace — they are saw
cuts, 2px bright lines with a jagged crack path where two slabs have been
parted. Specifications are never presented as marketing copy: they are
quarry tickets, mono-set slips pinned to the slab they describe, giving
dimensions, weight and finish in the yard's own units. The visitor's
progress down the page is surveyed, not scrolled: a chalk line in the left
margin fills survey orange section by section, and each filled segment is
labelled with that section's ticket number, so the progress rail is also
the page index.

The mood is industrial patience. Stone does not bounce, spring or sparkle;
it settles, grinds, splits along a line it was always going to split along,
and sheds dust. Every duration in this theme is therefore long by web
standards and short by quarry standards: a slab settles over 700ms, a saw
cut crosses the hero in 1200ms, dust falls at 4–8px per second. Nothing on
the page moves without a load on it. The one fast thing is the chalk line's
snap at a section boundary — 120ms — because a snapped chalk line is the
one genuinely quick event in a quarry.

**The theme's one law: the ticket never lies.** Every dimension printed on
the page is measured from the rendered thing it labels, at the moment it
is read, converted at the page's declared scale (printed in the footer:
**1 CSS px = 2 mm of stone**, rounded to the nearest 10 mm) — or it is not
printed. A callout that reads "THIS SLAB: 1,840 × 60 MM" is not copy; it is
the output of a measurement of that slab's live box. Yard figures (tonnage,
slabs cut, blade hours) come from the yard record object, and the same
object feeds the stats band, the specification table and the footer's day
tally, so the three can never disagree. An invented dimension, a rounded
age, a count typed twice with two values — each is a blocking gate failure
(§10), not a copy edit.

**Best-fit sites.** Working yards and their suppliers: dimension-stone
quarries, stone merchants, monumental masons, saw and blade manufacturers,
heavy plant hire, aggregate and reclamation firms, stonemasonry training
schools, geological survey publications. Any business whose credibility is
*weight, measure and process* — where the product is literally cut to the
customer's numbers — wears this theme honestly. The worked examples (§8)
use a dimension-stone yard, "Brackenfell Stone", selling sawn slabs and
offcuts.

**When NOT to use it.** Never for anything that must feel light, fast or
soft: food delivery, children's products, wellness, fashion drops, event
ticketing with countdown urgency. Never where the catalogue cannot supply
real dimensions — the law (§1) makes a dimension-less build impossible, and
a Quarry Cut page with placeholder sizes is a forgery, not a theme. Never
for a single-screen app or dashboard: the theme's meaning is vertical
descent through a block, and a page shorter than three slabs has nothing
to cut. Never where the client wants rounded corners and soft shadows —
radius in this theme is 0 except on drill cores (§11), and a softened
Quarry Cut is a different, worse theme.

**The block is one object.** The hero face, the slabs, the yard record and
the footer are generated from one `BLOCK` data object (§4): slab list with
ticket numbers, nominal dimensions and finishes; yard figures; the offcut
list. Rendering may transform it; nothing may contradict it. The footer
prints the object's scale line and record date as the audit trail.

## 2. Palette

Five anchors from the original entry, unchanged. Two derived tones are
admitted — ticket paper and quarry dust — each a mixture of anchors, each
with a single licensed job. Contrast figures below are measured (WCAG
relative luminance) for this expansion, not estimated.

| Token | Hex | Role | Usage ratio | Pairing / contrast (measured) |
|---|---|---|---|---|
| `--fresh` | `#D9D4C8` | Fresh cut — the newly sawn face; primary ground | ~55% | Core dark on fresh **8.69:1** — the body-text pairing of the theme |
| `--sawn` | `#A9A294` | Sawn face — older cut surface, slab grounds, card faces | ~25% | Core dark on sawn **5.07:1** — text licensed, short runs and labels preferred |
| `--wet` | `#6E6A5E` | Wet stone — damp depth, seams, secondary text on light grounds | ~10% | Wet on fresh **3.65:1** — large text and captions only, never body |
| `--core` | `#33322C` | Core dark — ink of the theme; dark slab grounds, footer block | ~8% | Fresh on core **8.69:1**; sawn on core **5.07:1** |
| `--survey` | `#C75B27` | Survey orange — chalk fill, saw line glow, cored stamps, the one accent | ≤2% | On fresh **2.87:1**, on core **3.03:1** — **never text**; graphical marks and ≥24px display numerals only |
| `--ticket` | `#F3F0E7` | Ticket paper (derived: fresh cut lifted toward white) — quarry tickets, form slips | within fresh's share | Core dark on ticket **11.28:1** — the highest-contrast pairing; all form text lives here |
| `--dust` | `#8F897A` | Quarry dust (derived: sawn face toward wet stone) — skeleton blocks, disabled states, hairlines on dark | within sawn's share | On core **3.69:1** — graphical only on dark; never a text colour anywhere |
| `--core-deep` | `#23221D` | The pit floor (derived: core dark deepened) — footer base, 404 ground | within core's share | Ticket on core-deep **13.98:1**; sawn on core-deep **6.28:1**; survey on core-deep **3.76:1** (marks only) |
| `--survey-deep` | `#9E471C` | Burnt survey (derived: survey orange darkened) — the only orange allowed to carry words | <1% | On ticket **5.47:1**, on fresh **4.21:1** — error lines and the CORED stamp's text form only |

**Palette laws.**

1. **Orange is a surveyor's mark, never a surface.** Survey orange appears
   as chalk fill, the saw line's bright edge, drill dots, stamps and ticks
   — total orange pixels ≤2% of any viewport (audited, §10). It never fills
   a button, a card or a background; the one filled control (the form's
   submit, §6.15) is core dark with a survey edge, not an orange block.
2. **Text pairings are closed.** Body text is core on fresh, core on
   ticket, or ticket/fresh on core and core-deep. Wet stone carries
   captions ≥14px and datelines, nothing smaller. Sawn-face grounds carry
   core text at 5.07:1 — licensed for labels, ticket heads and short
   specification runs, not paragraphs.
3. **The wet line.** A slab's ground darkens one step (fresh → sawn → wet
   tint) only where the copy itself is about depth, water or weight below
   ground — the process and pit sections. Decorative darkening to "break
   up the page" is refused; grounds change when the subject does (§9.4).
4. **No light mode, no inversion.** The theme is a lit quarry face: pale
   stone under working light. `prefers-color-scheme: dark` does not invert
   it; instead the "after hours" ruling (§2.1) applies only if the builder
   explicitly ships it. Print is the true light surface: tickets print
   black on white (§14).

### 2.1 After-hours ruling (the dark scheme)

If a dark scheme is required, the yard goes *after hours*: grounds drop one
step (fresh → sawn, sawn → wet-tinted core), text becomes ticket on
core-deep (13.98:1), and a single lamp pool (§6.17) lights the footer. The
saw line and chalk keep survey orange, which rises to 3.76:1 on core-deep —
still marks, still never text. Nothing inverts; stone under a lamp is still
stone. Reduced-data and print builds skip the after-hours scheme entirely.

## 3. Typography

Three families, three jobs, no fourth voice. **Archivo Expanded** (700/800)
is the display face — cut lettering, wide and industrial, used for the hero
headline, slab titles and the masthead wordmark. **Archivo** (400/500/600)
is the prose face — specifications explained, process described, the yard's
sentences. **IBM Plex Mono** (400/500/600) is the ticket face — every
dimension, figure, label, callout, dateline and form field annotation is
mono, because on a quarry ticket everything factual is typed, not typeset.

| Role | Face / weight | Size (≥1200px) | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Display / hero | Archivo Expanded 800 | 64px | 0.98 | −0.01em | Engraved treatment in the hero only (§6.1) |
| Slab title (H2) | Archivo Expanded 700 | 34px | 1.05 | 0 | Always preceded by its ticket number in mono |
| Section head (H3) | Archivo 600 | 20px | 1.2 | 0.01em | Never expanded face below H2 |
| Body | Archivo 400 | 17px | 1.62 | 0 | Measure 58–68ch on fresh grounds |
| Lead / standfirst | Archivo 500 | 20px | 1.5 | 0 | One per slab, max 34 words |
| Ticket head | Plex Mono 600 | 13px | 1.3 | 0.08em, uppercase | "TICKET Nº 04 — SAWN SLABS" |
| Specification / data | Plex Mono 500 | 14px | 1.45 | 0 | Tabular figures are native to the face |
| Callout label | Plex Mono 500 | 12px | 1.3 | 0.04em, uppercase | The measured dimension (§6.3) |
| Caption / dateline | Plex Mono 400 | 12.5px | 1.4 | 0.02em | Wet stone on light, dust never |
| Form label | Plex Mono 600 | 12px | 1.3 | 0.08em, uppercase | On ticket paper only |

**Type laws.**

1. **Figures are mono or they are not figures.** Any number that states a
   fact — dimension, tonnage, count, price, date — is set in IBM Plex Mono.
   A number in Archivo is a claim; a number in mono is a record. Prices in
   display type are a gate failure.
2. **The headline is cut, not styled.** The hero headline's engraved
   treatment (dark top edge, light bottom edge, §6.1) exists only in the
   hero, where the saw reveals it. Slab titles are flat core-dark type —
   stone that has already been cut needs no second effect.
3. **Uppercase is for tickets.** Expanded display sets sentence case;
   uppercase belongs to mono ticket heads, labels and stamps, where it is
   the yard's typing, not shouting.
4. **Line-height loosens with weight of subject.** Body at 1.62 on fresh;
   on sawn grounds 1.66; the pit sections (wet grounds) 1.7 — denser stone,
   more air between lines, the opposite of the usual instinct, because
   small text on mid grounds needs the help (§2, wet at 3.65:1 is
   caption-only for the same reason).
5. **No italic voice.** Archivo italic is refused throughout; emphasis is
   weight or mono. The yard does not lean on words. (The single exception
   is a quoted customer's words in a testimonial ticket, set in Archivo
   italic and attributed — a voice from outside the yard.)

## 4. Layout language

**The block.** The page is one vertical block, full-bleed, divided into
slabs. A slab is a full-width section with a stone ground (fresh, sawn or
wet-tinted per §2 law 3), an inner measure of 1200px, and a ticket pinned
at its head. Between slabs: the saw cut — a 2px bright line (`--ticket` at
full light on light grounds, survey-edged on dark) running the full width,
its path straight except where §6.2's split has parted two slabs along a
jagged crack. There are no rounded corners, no card shadows floating on a
page background, no page background at all distinct from stone: the block
is the page.

**The survey margin.** At ≥1200px a 72px left margin runs the page's full
height. It holds exactly two things: the chalk-line progress rail (§6.4)
and, at each slab boundary, the slab's ticket number rotated 0° (never
vertical text — surveyors write horizontally on the margin stone). Below
1200px the margin retires into the masthead (§6.11) as a horizontal chalk
strip; the space is returned to the measure.

**Slab anatomy.** Every slab, in order: (1) the cut seam at its head, (2)
the ticket — a `--ticket` slip, max 340px wide, pinned at the slab's
top-left inside the measure, carrying ticket number, slab name and the
slab's nominal dimension line, (3) the slab title (H2) in Expanded, (4)
content in the slab's own arrangement. The ticket is never decorative: its
dimension line is §6.3's callout system in resting form, and its number is
the chalk rail's label for that section (§6.4) and the footer's index key
(§6.17). Three printings of one fact, again.

**Density falls with depth.** The block is densest at the face (hero:
headline, standfirst, ticket, one figure) and loosens as it descends —
yard slabs carry 3–6 pieces, the process slab is mostly one diagram and
its copy, the pit/footer slab is sparse. A slab may not carry more than
seven content pieces; the eighth piece means the slab should have been
two, and the build splits it (§15). Whitespace in this theme is *unworked
stone*: it is the part of the block not yet cut, and it is always at a
slab's foot, never scattered between pieces.

**The `BLOCK` object.** One data object generates the page:

```js
BLOCK = {
  scale: "1 CSS px = 2 mm of stone",        // printed in the footer, §6.17
  recordDate: "2026-11-21",                  // the yard record's date
  slabs: [ { ticket: "01", name: "THE FACE", ground: "fresh",
             nominal: "FULL BLOCK FACE" }, … ],
  yard: { tonnes: 1284, slabsCut: 342, bladeHours: 96.5,
          bladesUsed: 7 },                   // §6.7, §6.14, §6.17 — one source
  offcuts: [ { ticket: "OC-11", dims: "640 × 420 MM", finish: "SAWN" }, … ]
}
```

Callout measurements (§6.3) are the exception that proves the law: they are
*not* read from `BLOCK` but measured live from the rendered box and
converted at `BLOCK.scale` — the object declares the scale, the DOM
supplies the size, the ticket prints the product of the two.

**Grid.** Inside the measure: 12 columns, 24px gutters, but stone is not
laid in twelfths — content snaps to a 6-column working grid (each piece
spans 2, 3, 4 or 6) so edges land like cut lines, never at arbitrary
fractions. Vertical rhythm is the **course**: 8px base, slab padding in
courses of 12 (96px head, 120px foot — the foot carries the unworked
stone, §4 above). Images always sit in fresh-cut frames (§6.8) whose outer
box is a grid piece like any other.

## 5. Full motion system

Five named easings carry the whole theme. Stone has no bounce and no
elasticity; it has weight, friction and one snap.

| Token | Curve | Job |
|---|---|---|
| `--ease-saw` | `linear` | The saw's travel (§6.1, §6.10) — a blade does not ease |
| `--ease-settle` | `cubic-bezier(0.17, 0.89, 0.32, 1.08)` | Slabs and pieces dropping into place with ≤8% overshoot — mass arriving |
| `--ease-crack` | `cubic-bezier(0.7, 0, 0.84, 0)` | The split (§6.2) — strain held, then the parting gives |
| `--ease-gravity` | `cubic-bezier(0.55, 0.06, 0.68, 0.19)` | Crumble and dust fall — acceleration, no arrival bounce |
| `--ease-twang` | `cubic-bezier(0.34, 2.2, 0.64, 1)` | The chalk line's 120ms snap at a boundary (§6.4) — the theme's one spring |
| `--ease-draw` | `cubic-bezier(0.4, 0, 0.2, 1)` | Callout lines, diagram strokes, measuring lines extending |

**The shared loop.** One `requestAnimationFrame` loop drives every
scroll-scrubbed value — slab split distance, saw line position in the
showcase, chalk fill, frame scale, background parallax — with lerp factor
**0.10** (the heaviest settle in the library's stone themes; the original
entry's "heavy industrial settle on the smooth scroll" made numeric).
Inputs are read once per frame from `scrollY`; outputs are written as CSS
custom properties on the affected slab only. No scroll handler writes
styles. The loop sleeps when the tab is hidden and when no scrubbed
element is within one viewport of the screen.

**Motion vocabulary — every term, translated or refused.**

- *Scroll-triggered reveals:* slabs settle — pieces translate up 24px and
  land over 700ms `--ease-settle` as the slab's head crosses 82% of the
  viewport, staggered 90ms per piece, once. Nothing fades in from
  invisible: pieces are present at 55% opacity in their pre-state (JS-armed
  only) and arrive to full — stone is never a ghost (§9.2).
- *Scroll-driven / scrubbed animation:* the split (§6.2), the showcase saw
  (§6.12's mid-page example, §8.2), frame scale-in (§6.8), chalk fill
  (§6.4) — all scrubbed through the shared loop, all fully reversible on
  scroll-up except the split's crumble, which is spent (§6.2).
- *Parallax:* the saw-scored background face behind polished content slabs
  moves at 0.92× (an 8% lag, capped ±18px); the hero dust (§6.5) drifts on
  its own time loop. No foreground parallax — stone in front of you does
  not slide.
- *Pinned sections:* the splitting slabs pin (§6.2) and the process slab
  pins around the core-drill diagram (§6.6). Exactly two pin types; a
  third pin in one page is refused at build review.
- *Smooth scrolling:* native, with the loop's 0.10 lerp supplying the
  industrial weight on scrubbed values. Scroll is never hijacked.
- *Progress indicator:* the chalk line (§6.4) — the only progress the theme
  admits, and it is an index, not a bar.
- *Staggered / masked reveals:* slab pieces stagger 90ms; the hero headline
  is masked by the saw cut itself (§6.1) — the theme's one masked reveal,
  and the mask is a tool of the trade.
- *Kinetic typography:* refused. Letters do not dance in a quarry. The one
  licensed exception is the headline letters' final 2px drop into the cut
  (§6.1) — type *set into* stone, staggered 40ms, with a dust puff per
  letter. That is typesetting, not kinetics.
- *Marquee:* refused. Nothing in a yard scrolls sideways forever. The
  footer's offcut list (§6.17) is a static typed list; if it is long, it is
  long.
- *Counters:* stepped, odometer-ticked, never smoothly tweened (§6.7) —
  a tally is struck, not animated.
- *SVG line-draw:* the core-drill diagram (§6.6) and callout measuring
  lines (§6.3) draw with `--ease-draw`; the chalk line's fill is a stroke
  draw at scroll speed.
- *Image scale-in-frame:* §6.8, 1.06 → 1.0 scrubbed, inside saw-marked
  frames.
- *Hover / tilt micro-interactions:* slabs tilt ≤2° (§6.13) like stone on
  a saw table — transform-origin at the slab's lower edge, so the piece
  rocks on its base, never floats. Callouts rise on hover/focus (§6.3).
  Buttons press 1px down with no shadow change — a stamp, not a spring.
- *Custom cursor:* refused — standing rule. The system cursor everywhere;
  over a slab the cursor stays the arrow, because the slab is a thing to
  read, and over a cored corner (§6.9) it becomes `pointer` only on the
  ticket's stamp line, which is a real control.
- *Skeleton loading:* unscored stone blocks (§6.16) — sawn-face rectangles
  with no scoring, filling the exact boxes the content will occupy.
- *Page transitions:* the saw cut (§6.10) — 300ms line, page splits along
  it. Internal anchor travel uses the same cut at half brightness.
- *Ambient loops:* dust (§6.5) and nothing else. One ambient system per
  page; a second is cut at review.
- *Reduced motion:* every element ships its finished state (§6, per
  element): slabs stacked and measured, chalk fully drawn to the current
  section, counters at final figures, no split, no crumble, no dust.

## 6. Signature elements

The ten original elements (§6.1–§6.10) are deepened, never redesigned.
Eight page-family elements (§6.11–§6.18) complete the set: navigation,
hero composition, cards, the specification table, the conversion form,
loading, footer and the 404. Every element carries the v1 fields and the
v2 layers; every scrubbed value runs through the one shared loop (§5).

### 6.1 The hero saw cut

- **What & why.** On load, a 2px bright saw line with a faint dust trail
  travels vertically down the hero stone face over 1200ms, and the
  headline is unmasked behind it, engraved — dark top edge, light bottom
  edge — as if the blade's pass is what cut the letters. It belongs
  because the cut *is* the headline reveal: the brand name is literally
  cut into the stone the quarry sells, and a visitor who watches the pass
  has understood the business before the standfirst arrives.
- **Structure.** A real `<h1>` in Archivo Expanded 800 carrying the full
  headline in the DOM from first paint, engraved via a two-layer text
  treatment (a `--core` face with a 1px `--ticket` offset copy beneath,
  clipped to the glyph bottoms). The saw line is a 2px-wide absolutely
  positioned bar (`--ticket` core with a 6px survey-orange leading edge —
  the blade's hot rim) inside the hero, `pointer-events: none`, masked so
  the headline's reveal is a clip inset keyed to the line's x-position:
  type left of the blade is engraved and visible; type right of it is the
  unscored face. A dust trail of 6 pre-rendered sprite dots trails 40px
  behind the blade, fading over 600ms.
- **Motion spec.** Trigger: load, once per session (`sessionStorage`),
  gated on `document.fonts.ready` raced against 700ms — cutting in a
  fallback face would misplace the engraving, so if fonts lose, the hero
  ships cut (see fallback). The line travels the hero's width in 1200ms
  `--ease-saw` (linear — a blade does not ease). Behind it, each headline
  letter drops its final 2px into the cut as the blade passes its
  x-centre, staggered by position (nominal 40ms per letter at 64px type),
  each drop shedding one dust puff (a 10px radial sprite scaling to 26px,
  fading in 380ms `--ease-gravity`). The standfirst fades to full over
  400ms starting 150ms after the blade exits.
- **States.** Uncut (JS-armed only, pre-session first visit) → cutting →
  cut (rest; the line retires to the hero's right edge as a 2px seam and
  stays as the hero's right border). Hover/focus: none — the headline is
  not a control. Scrolled-past mid-cut: the cut completes on its own
  timeline; scroll never drives it.
- **Content merge.** The headline is the page's `<h1>` and subject; the
  cut is not an intro played over the hero, it is the hero's first act of
  manufacture, and the hero ticket (§6.12) prints only after the blade
  exits — the ticket describes a finished face.
- **Failure fallback.** Watchdog at 1600ms: if the cut has not completed,
  the clip inset snaps to full, the line retires, letters rest seated. No
  JS: the headline stands engraved and complete at first paint; the saw
  line is absent (it is JS-inserted). Slow network: fonts race lost →
  printed state, ceremony skipped, never misaligned.
- **Reduced-motion variant.** No travel, no drops, no puffs. The headline
  stands cut and seated; the seam rests at the hero's right edge. The
  information (this name is cut into this stone) survives entire.
- **Performance budget & mobile variant.** The blade and trail are one
  composited layer animating `transform` and a clip inset — no layout.
  Budget ≤6KB of sprite/CSS. Mobile (<768px): the cut runs 900ms, dust
  trail cut to 3 sprites, letter drops become a single 2px settle of the
  whole line at blade exit (per-letter tracking is a desktop instrument).
- **Choreography timeline (v2).** t=0 fonts ready → blade enters at the
  hero's left edge → letters drop as the blade crosses each x-centre
  (≈40ms apart) → t=1200 blade exits right, seam rests → t=1350
  standfirst begins its 400ms fade → t=1500 hero ticket prints (§6.12) →
  t=1600 watchdog deadline (already satisfied).
- **State matrix (v2).** *Rest:* cut, seated, seam at right edge.
  *Hover:* none. *Focus:* focus entering the hero completes a running cut
  instantly — a keyboard visitor is never asked to wait for a blade.
  *Active:* n/a. *Scrolled-past:* completed. *Disabled / no-JS:* printed
  cut at first paint. *Touch:* identical; first touch completes a running
  cut.
- **Breakpoints (v2).** ≥1200px: 1200ms cut, 64px type, per-letter drops.
  768–1199px: 1050ms, 48px type, per-letter drops at 30ms. <768px: 900ms,
  36px type, whole-line settle, 3-sprite trail.
- **Edge cases & failure modes (v2).** *Headline longer than the face:*
  refused at build — the hero headline is ≤26 characters (§12); a longer
  CMS headline ships printed, blade never armed (build check, §15).
  *Tab hidden mid-cut:* rAF pauses; wall-clock past 1600ms triggers the
  watchdog on return. *Revisit in session:* printed, no replay — a face
  is cut once.
- **Accessibility spec (v2).** The `<h1>` is complete in the accessibility
  tree from first paint; blade, trail and puffs are `aria-hidden`,
  `pointer-events: none`. The engraving never reduces contrast: the
  readable layer is `--core` on `--fresh` at 8.69:1 throughout; the clip
  masks only the decorative offset copy, so no state leaves a letter
  half-legible to AT or eye.
- **Tokens consumed (v2).** `--fresh`, `--core`, `--ticket`, `--survey`,
  `--ease-saw`, `--ease-gravity`, `--dur-saw-hero` (1200ms),
  `--dur-letter-drop` (40ms stagger), `--dur-fallback-hero` (1600ms).

### 6.2 Splitting slabs

- **What & why.** Each major section is a slab; as it passes viewport
  centre inside its pin, the slab separates from the next along a jagged
  crack path by 10–18px, shedding 8–14 tiny crumble dots that fall with
  gravity easing and fade. In the opened gap, the next section's ticket
  header is revealed. It belongs because the crack is the section divider
  made physical: the visitor does not scroll past a boundary, they watch
  the block part along the line the saw scored for it.
- **Structure.** Each splitting pair is two slab elements inside a pin
  wrapper of 160vh. The crack is an SVG path (one authored jagged
  polyline per pair, amplitude 6px, wavelength ~90px) used as a clip on
  the lower slab's top edge and as a stroked hairline in `--wet`. The gap
  content — the next slab's ticket (§4) — sits in the seam, revealed as
  the offset grows. Crumble dots are a pool of 14 absolutely positioned
  2–4px squares per pair, recycled, filled `--sawn` and `--wet`.
- **Motion spec.** Trigger: scroll scrub through the pin, driven by the
  shared loop (lerp 0.10). Split distance = pin progress × the pair's
  declared gap (10–18px, authored per pair in `BLOCK.slabs[].gap`).
  Separation follows `--ease-crack` mapped onto progress 0.15–0.85: strain
  (0–4px over the first half) then the give. Crumble fires once per pair,
  at progress 0.55: 8–14 dots release from points along the crack, fall
  60–140px over 500–900ms `--ease-gravity`, fade in the last 30%. Scroll
  back up: the slabs close symmetrically; the crumble does not replay —
  spent stone does not un-fall — until the pair leaves the viewport
  entirely and re-enters.
- **States.** *Rest (unseparated):* slabs flush, crack a hairline.
  *Splitting:* offset scrubbed, ticket emerging. *Separated (scrolled
  past):* full gap held while the lower slab is read; the pair unpins
  with the gap at its declared value, which becomes the seam's resting
  whitespace. *Hover/focus:* none — slabs are sections, not controls;
  focus entering the lower slab while its pair is mid-pin snaps progress
  to the nearer end so content is never read across a moving seam.
- **Content merge.** The gap is not empty decoration: it carries the next
  section's ticket — number, name, nominal dimension — so the act of
  parting *is* the act of introducing what comes next. Remove the split
  and the page loses its section introductions, not an effect.
- **Failure fallback.** The pin is JS-armed only. No JS: slabs stack
  flush with the 2px saw-cut seam (§4) and full tickets at their heads —
  the complete page, unparted. Missed-pin snap-together fallback: if the
  loop stalls >800ms mid-pin (long task, jank), progress snaps to the
  nearer end and the pin releases; content is never left half-parted
  across a frozen seam. Watchdog per pair at pin entry +2500ms forces the
  separated end state if progress has not moved.
- **Reduced-motion variant.** No pin, no split, no crumble. Slabs rest
  stacked with their saw-cut seams and tickets — identical information,
  identical order.
- **Performance budget & mobile variant.** One clip-path and two
  transforms per pair; crumble pool ≤14 nodes; total per-pair cost ≤0.3ms
  per frame. Mobile (<768px): **the split is cut** — pins are the first
  thing removed (§14 cut order) — slabs stack with a 14px static gap and
  the ticket in the seam, which is the separated end state as a layout.
  Tablet (768–1199px): pin shortens to 130vh, gap capped at 12px,
  crumble 6–8 dots.
- **Choreography timeline (v2).** Pin engages at slab head = viewport top
  → progress 0–0.15 strain builds (crack hairline darkens) → 0.15–0.5
  separation to 60% of gap, ticket's top edge clears the seam → 0.55
  crumble releases → 0.5–0.85 separation completes, ticket fully legible
  → 0.85–1.0 hold → pin releases into the lower slab's settle (§5).
- **State matrix (v2).** *Rest:* flush or fully separated, per scroll
  position. *Hover:* none. *Focus:* snap-to-end rule above. *Active:*
  n/a. *Scrolled-past:* separated, resting gap. *Disabled:* the pin is
  never armed for touch-with-reduced-motion or `save-data` — stacked
  layout. *Touch:* scrubbed by touch scroll identically on tablet;
  stacked on phones.
- **Breakpoints (v2).** ≥1200px: 160vh pin, gap 10–18px, 8–14 dots.
  768–1199px: 130vh, gap ≤12px, 6–8 dots. <768px: no pin; static 14px
  seam gap with ticket.
- **Edge cases & failure modes (v2).** *Jump scroll (anchor, find,
  scrollbar drag):* progress is a pure function of scroll position, so a
  jump lands the pair at the correct end state; crumble does not fire
  retroactively. *Very short slab:* a pair whose lower slab is <50vh
  tall is refused at build (§15) — the pin would trap it. *Scroll-up
  re-entry:* slabs close; crumble rearms only after the pair fully exits
  and re-enters. *Resize mid-pin:* progress recomputed from the new
  geometry in one frame; gap in px is scale-stable.
- **Accessibility spec (v2).** The seam and crack are `aria-hidden`; the
  revealed ticket is ordinary DOM in reading order — it is *positioned*
  by the split, never created by it, and is reachable and legible in the
  stacked fallback at all times. Focus is never moved by the pin. The
  separation does not change tab order.
- **Tokens consumed (v2).** `--sawn`, `--wet`, `--ticket`, `--ease-crack`,
  `--ease-gravity`, `--loop-lerp` (0.10), `--dur-crumble` (500–900ms),
  `--gap-split` (per pair, 10–18px).

### 6.3 Dimension callouts

- **What & why.** Thin measuring lines with end ticks and a mono label —
  "THIS SLAB: 1,840 × 60 MM" — draw out from the hero slab, cards and
  images, stating the true rendered size of the piece they annotate,
  converted at the page's declared scale (§1, §4). It belongs because it
  is the theme's law made visible: the ticket and the object are one
  thing, and the callout is the moment the page proves it.
- **Structure.** An SVG overlay per annotated piece (hero, each yard card
  §6.13, each framed image §6.8), absolutely positioned over the piece's
  box, `pointer-events: none`. Two measuring lines (width across the top,
  height down the right), each a path with 6px end ticks, drawn via
  `stroke-dashoffset`. The label is a real HTML element in Plex Mono 12px
  on a `--ticket` chip pinned to the width line's midpoint. Measurement:
  on draw, JS reads the piece's `getBoundingClientRect()`, multiplies by
  the scale factor from `BLOCK.scale` (2 mm per CSS px), rounds to the
  nearest 10mm, formats with a thousands comma, and sets the label text.
- **Motion spec.** Trigger: first draw is scroll-triggered — when the
  piece centres, its lines extend in two 250ms steps (width line, then
  height line) `--ease-draw`, label fading in at the second step. After
  the first draw, callouts rest *drawn at 45% ink* and rise to full on
  hover/focus of the piece, lines re-extending in one 250ms step. On
  resize ≥40px in either dimension, the measurement is re-taken and the
  label updates with a 200ms crossfade — the ticket re-issues itself
  rather than lie about a resized piece.
- **States.** *Rest:* drawn at 45% (`--wet` lines), label legible.
  *Hover/focus (desktop):* full `--core` lines, label chip to full
  ticket contrast. *Active:* n/a. *Scrolled-past:* rest state persists;
  callouts never un-draw. *Disabled / no-JS:* the label prints the piece's
  **nominal** dimension from `BLOCK` (its catalogue size) with lines fully
  drawn — honest paper truth when live measure is unavailable, and the
  footer scale line (§6.17) says which kind of figure the page is showing
  ("DIMENSIONS MEASURED LIVE" vs "NOMINAL DIMENSIONS").
- **Content merge.** The callout measures the actual product card or
  photograph it annotates — the same box the visitor is looking at. It is
  not a caption about the object; it is the object's own ticket, drawn on
  the object.
- **Failure fallback.** If measurement returns 0 (hidden piece, display
  race), the callout does not draw and the label falls back to the
  nominal figure — a wrong live number is worse than a declared nominal
  one. Watchdog: any callout armed but not drawn within 1200ms of its
  trigger draws instantly at rest state.
- **Reduced-motion variant.** Lines pre-drawn at rest state; hover raises
  ink only (no re-extension); resize updates swap text without crossfade.
- **Performance budget & mobile variant.** One SVG per piece, ≤1.2KB;
  measurement is one rect read per draw, batched with the loop's frame —
  no layout thrash (reads happen before the frame's writes, §5). Mobile
  (<768px): height lines are cut (width only), labels shorten to width ×
  nominal depth from `BLOCK` ("1,840 MM WIDE — DEPTH PER TICKET"), and
  first draw fires on entry at 70% rather than centre.
- **Choreography timeline (v2).** Piece crosses centre → t=0 width line
  extends 250ms → t=250 height line extends 250ms → t=380 label fades in
  (120ms) → rest at 45% ink → hover: t=0–250 both lines re-extend to full
  ink → leave: 300ms settle back to 45%.
- **State matrix (v2).** *Rest:* drawn, 45% ink, true label. *Hover:*
  full ink, re-measured if the box changed since last draw. *Focus:*
  identical to hover (focus-within on the piece). *Active:* n/a.
  *Scrolled-past:* rest. *Disabled:* nominal label, drawn lines.
  *Touch:* no hover — first tap on a piece raises its callout for 3s
  (the tap still follows the piece's own link behaviour if it has one;
  the callout never intercepts).
- **Breakpoints (v2).** ≥1200px: both lines, full label. 768–1199px:
  both lines, label on the width line only. <768px: width line only,
  shortened label (above).
- **Edge cases & failure modes (v2).** *Piece taller than viewport*
  (process slab): height line is capped at the viewport edge with a
  broken-tick terminator and the label reads the true full height — the
  line admits it ran off the stone. *Rotated piece* (§6.13 tilt): callout
  measures the unrotated box; measuring a tilted box would print a lie
  about a resting dimension. *Font loading changing the box:* re-measure
  on `document.fonts.ready` if armed before it.
- **Accessibility spec (v2).** The SVG lines are `aria-hidden`. The label
  is real text associated with its piece via `aria-describedby`, so a
  screen reader hears the dimension as part of the piece's description.
  Contrast: label text `--core` on `--ticket` 11.28:1 at rest and hover;
  the 45% state applies to lines only, never to label text. Focus-raised
  callouts give keyboard visitors the same measurement sighted hover
  gives mouse visitors.
- **Tokens consumed (v2).** `--wet`, `--core`, `--ticket`,
  `--ease-draw`, `--dur-callout-step` (250ms), `--scale-mm` (2, from
  `BLOCK`).

### 6.4 Chalk-line progress rail

- **What & why.** A surveyor's chalk line runs down the left margin for
  the page's full height. As the visitor descends, the line fills survey
  orange section by section, snapping straight with a 120ms twang settle
  at each section boundary, and each filled segment is labelled with its
  section's quarry-ticket number. It belongs because it is the page's
  survey: progress here is not a percentage but a marked line on stone,
  and the rail doubles as the page index — clicking a ticket number rides
  to that slab.
- **Structure.** A fixed-position rail inside the 72px survey margin
  (§4): a 2px vertical track (`--sawn` at 60%), a fill line (survey
  orange, 2px) whose length is set from the shared loop, segment ticks at
  each slab boundary (8px horizontal ticks), and a column of ticket-number
  labels (Plex Mono 11px, `--core`) beside each tick, each a real anchor
  link to its slab. The current segment's label is set in
  `--survey-deep` with a 2px orange tick — words in the deep orange,
  marks in the bright one (§2).
- **Motion spec.** Fill is scrubbed: fill length = page progress through
  the slab list, lerped at 0.10 by the shared loop. At each boundary
  crossing, the line performs the twang: a 3px horizontal overshoot of
  the fill's tip decaying over 120ms `--ease-twang`, and the boundary
  tick stamps in. Fill never retreats past a boundary already stamped on
  scroll-up within the same second — the twang is a ratchet at 1s grain;
  beyond that, fill follows scroll honestly in both directions.
- **States.** *Rest:* filled to the current section, current label
  marked. *Hover:* a ticket label underlines (1px `--core`) — it is a
  link. *Focus:* visible 2px outline in `--survey-deep` offset 2px.
  *Active:* label presses 1px. *Scrolled-past:* earlier segments stay
  filled and stamped. *Disabled / no-JS:* the rail renders fully drawn
  with all labels as a static index — an index needs no animation to be
  an index.
- **Content merge.** Each segment *is* a slab's index entry: number,
  anchor and boundary are the same data as the slab's ticket (§4) and the
  footer index (§6.17). The rail is navigation wearing the theme's
  material, not a progress widget pasted into the margin.
- **Failure fallback.** If the loop fails, the rail degrades to the
  no-JS state (full static index) — labels and links are server-rendered
  DOM, only the fill is JS. A rail that shows no fill but keeps its index
  has lost an ornament, not a function.
- **Reduced-motion variant.** Fill jumps segment to segment at boundaries
  (no scrub, no twang); labels and links identical.
- **Performance budget & mobile variant.** One fixed element, one
  transform per frame; ≤0.1ms/frame. Below 1200px the rail leaves the
  margin and becomes a horizontal chalk strip inside the masthead
  (§6.11): fill runs left-to-right, labels collapse to the current
  ticket number only ("TICKET 04 / 09"), links move into the nav. Below
  768px the strip remains but the twang is cut.
- **Choreography timeline (v2).** Scroll crosses slab boundary → loop
  lerps fill to the boundary over ~300ms of scroll travel → tip reaches
  tick → twang: +3px overshoot, decay 120ms → tick stamps, label marks
  current → fill continues into the next segment with ongoing scroll.
- **State matrix (v2).** *Rest:* as above. *Hover:* label underline.
  *Focus:* outline. *Active:* 1px press. *Scrolled-past:* stamped,
  filled. *Disabled:* static full index. *Touch:* strip form in the
  masthead; labels are 44px tap targets in the nav drawer.
- **Breakpoints (v2).** ≥1200px: margin rail, all labels. 768–1199px:
  masthead strip, current-ticket label only. <768px: masthead strip, no
  twang, number pair only.
- **Edge cases & failure modes (v2).** *Short page (<3 slabs):* theme
  refused at build (§1) — a rail with two segments is a ruler, not a
  survey. *Anchor jump:* fill snaps to the target segment (progress is a
  function of position); twang does not fire for jumped boundaries.
  *Resize:* segment boundaries recomputed from slab offsets in one frame.
- **Accessibility spec (v2).** The rail is a `<nav aria-label="Page
  sections">` list of links; the fill line is `aria-hidden`. The current
  link carries `aria-current="true"`, updated at boundaries (throttled to
  boundary events, never per frame). Label contrast: `--core` on the
  margin's `--fresh` ground 8.69:1; current label `--survey-deep` on
  fresh 4.21:1 at 11px bold mono — licensed as large-equivalent by weight
  and tracking, and always paired with the orange tick so state never
  rests on colour alone.
- **Tokens consumed (v2).** `--survey`, `--survey-deep`, `--sawn`,
  `--core`, `--ease-twang`, `--dur-twang` (120ms), `--loop-lerp` (0.10).

### 6.5 Settling stone dust

- **What & why.** Twenty to thirty near-invisible dust motes drift
  downward inside the hero's light cone at 4–8px/s, looping. It is the
  theme's only ambient loop, and it belongs because the dust lives in the
  hero photograph's light: it makes the fresh-cut face feel like a
  working quarry face in morning light, not a stock photo of stone.
- **Structure.** A single `<canvas>` overlaying the hero figure only,
  sized to the figure's box, `pointer-events: none`, `aria-hidden`.
  Motes are 1–2px squares (stone dust is angular, never round bokeh) in
  `--ticket` at 12–28% opacity, seeded per-load with a fixed seed array so
  the field is stable across frames. The light cone is a CSS radial
  gradient on the figure itself; the canvas is clipped to the same cone
  via `mask-image`, so motes exist only inside the light.
- **Motion spec.** Continuous time loop, active only while the hero is in
  view (IntersectionObserver gate). Each mote falls at its seeded rate
  (4–8px/s), drifts ±6px horizontally on a slow sine (period 6–11s), and
  on leaving the cone's foot fades over 800ms and respawns at its head.
  No scroll input: dust answers to time and light, not to the visitor.
- **States.** *Rest:* drifting. *Hover/focus:* unchanged — dust does not
  react to the visitor; reacting would make it a toy. *Scrolled-past:*
  loop paused off-view. *Disabled:* canvas never created under
  reduced-motion, `save-data`, or a failed 2d context — the hero figure
  stands clean.
- **Content merge.** The motes are inside the hero image's own light,
  clipped to its cone — they are a property of the photograph of the
  face, not a particle layer over the page. Remove the hero figure and
  the dust has nowhere licensed to live; it is never reused on other
  sections.
- **Failure fallback.** Canvas unsupported or context lost: no motes, no
  error, the figure is complete without them. The dust is the one element
  whose total absence changes nothing the visitor came for — which is
  exactly why it is rationed to one figure.
- **Reduced-motion variant.** None. Dust does not render. (A static
  dusting printed in the photograph itself is a photography decision, not
  this element.)
- **Performance budget & mobile variant.** Canvas ≤ the hero figure's
  area; 30 motes max; ≤0.2ms/frame; the loop shares the page rAF but
  skips frames when the hero is off-screen. Mobile (<768px): 14 motes,
  fall rates halved, canvas capped at 60fps → 30fps stepping. Low-power
  signal (`hardwareConcurrency` ≤2 or battery saver): motes cut to 10.
- **Choreography timeline (v2).** Hero enters view → observer starts the
  field (motes pre-seeded at scattered depths, no visible "switch-on") →
  continuous fall/drift/fade/respawn → hero leaves view → loop idles
  within one frame.
- **State matrix (v2).** *Rest:* drifting in light. *Hover:* unchanged.
  *Focus:* unchanged. *Active:* n/a. *Scrolled-past:* paused. *Disabled:*
  absent. *Touch:* identical, reduced counts.
- **Breakpoints (v2).** ≥1200px: 30 motes. 768–1199px: 22. <768px: 14,
  half rate.
- **Edge cases & failure modes (v2).** *Hero figure replaced by CMS:*
  the canvas re-clips to the new figure's cone on resize/replace; if no
  figure exists, the element does not arm. *Long session:* mote count
  and seed are fixed; no accumulation. *High-DPI:* canvas scales to
  devicePixelRatio capped at 2 — dust at 3× is a smear, not a mote.
- **Accessibility spec (v2).** Pure decoration inside an `aria-hidden`
  canvas; the figure's alt text describes the face, never the dust.
  Opacity ceiling 28% keeps motes below the threshold of visual noise for
  low-vision visitors, and the cone keeps them off the headline's
  engraved layer.
- **Tokens consumed (v2).** `--ticket`, `--ease-gravity` (fall character),
  `--dur-dust-fade` (800ms).

### 6.6 Core-drill diagram

- **What & why.** In the process section, an SVG diagram of a drilled
  core sample — concentric rings, the drill path, depth ticks — strokes
  itself in over ~1.5s as the section centres, ring by ring in the order
  the copy beside it describes the extraction. It belongs because it
  diagrams the actual process the page is selling: how a core is taken,
  read and graded before a block is committed to the saw.
- **Structure.** One inline SVG (viewBox 0 0 320 320): an outer ring (the
  bore wall), three concentric core rings (the strata the copy names —
  face stone, heart stone, bed), a dashed drill path entering at 35°, and
  eight depth ticks with mono labels (0.5 M … 4.0 M) taken from the
  process data in `BLOCK`. Each ring is a `<circle>` stroked via
  dashoffset; labels are real SVG `<text>` in Plex Mono, present in the
  DOM from first paint (only the strokes animate).
- **Motion spec.** Trigger: the process slab centres (or the diagram
  crosses 60% viewport on tablet/mobile where there is no pin). The
  process slab pins for 120vh at ≥1200px while the diagram draws:
  bore wall 400ms `--ease-draw`, then rings at 300ms each in copy order,
  drill path 500ms dashed draw, ticks stamp in 60ms apart, labels fade
  with their ticks. Total ≈1500ms. Once per session; drawn state is the
  rest state thereafter.
- **States.** *Rest:* fully drawn, labels legible. *Hover:* hovering a
  ring highlights the corresponding copy paragraph's ticket edge (2px
  `--survey-deep` left rule) — diagram and copy point at each other.
  *Focus:* rings are focusable (`tabindex="0"`, role `img` parts) with
  the same highlight. *Scrolled-past:* drawn. *Disabled / no-JS:* fully
  drawn static diagram — the strokes are CSS-armed, the SVG ships
  complete.
- **Content merge.** The diagram's rings are the copy's strata, in the
  copy's order, with the copy's depths. It is the process section's
  second column, not an illustration beside it: delete the copy and the
  diagram's labels lose their referents.
- **Failure fallback.** Watchdog at 2000ms from trigger: any ring not yet
  drawn snaps to drawn. If SVG is unavailable (never in practice), the
  fallback is the same data as a mono table — the depth list is content,
  the circles are its portrait.
- **Reduced-motion variant.** Fully drawn at first paint of the section;
  hover/focus highlighting still works (it is a state, not a motion).
- **Performance budget & mobile variant.** Inline SVG ≤6KB; stroke
  animation on `stroke-dashoffset` only. Mobile (<768px): no pin; the
  draw compresses to 900ms total (rings 180ms each) triggered at 60%
  entry; depth labels reduce to 0.5 / 2.0 / 4.0 M to keep the face
  legible at small size.
- **Choreography timeline (v2).** Section centres → pin engages →
  t=0 bore wall draws 400ms → t=400 ring 1 (face) 300ms → t=700 ring 2
  (heart) 300ms → t=1000 ring 3 (bed) 300ms → t=1150 drill path 500ms
  (overlapping) → t=1300–1780 ticks stamp 60ms apart → pin releases as
  the copy column's settle completes.
- **State matrix (v2).** *Rest:* drawn. *Hover:* ring ↔ copy highlight.
  *Focus:* same, with visible outline on the ring. *Active:* n/a.
  *Scrolled-past:* drawn. *Disabled:* drawn static. *Touch:* tap a ring
  = hover behaviour, held until another tap.
- **Breakpoints (v2).** ≥1200px: pinned 120vh draw, all 8 ticks.
  768–1199px: no pin, 1200ms draw at 60% entry, all ticks. <768px: 900ms
  draw, 3 ticks.
- **Edge cases & failure modes (v2).** *Copy edited so strata change:*
  rings and labels generate from the same `BLOCK.process` list as the
  paragraphs — a fourth stratum adds a fourth ring and paragraph
  together, or the build fails (§15). *Jump scroll past the section:*
  diagram lands drawn. *Print:* drawn state prints (§14).
- **Accessibility spec (v2).** The SVG carries `role="img"` and an
  `aria-label` summarising the core ("Core sample: face stone to 1.2
  metres, heart stone to 2.8, bed stone to 4.0"), generated from the same
  data. Tick labels are real text. Ring focus outlines are 2px
  `--survey-deep`; the highlight pairing never rests on colour alone —
  the copy paragraph's ticket also gains its stratum name in the head.
- **Tokens consumed (v2).** `--core`, `--wet`, `--sawn`, `--survey-deep`,
  `--ease-draw`, `--dur-ring` (300ms), `--dur-diagram` (≈1500ms).

### 6.7 Counting yard figures

- **What & why.** The stats band's figures — tonnage extracted, slabs
  cut, blade hours — count up in IBM Plex Mono with a stepped,
  odometer-like tick when the band enters: digits strike their values in
  discrete steps, never a smooth tween. It belongs because a tally in a
  yard is struck from a record, and the stepped tick is the sound of the
  tally board being set. The figures are the yard's real production
  numbers from `BLOCK.yard` — the same object that feeds the
  specification table (§6.14) and the footer tally (§6.17).
- **Structure.** A band of 3–4 figure blocks on a `--core` ground (the
  theme's one dark slab above the footer), each block: a mono figure
  (Plex Mono 500, 44px, `--ticket`), a mono label beneath (12px,
  `--sawn`), and the record date in the band's ticket. Each figure is a
  row of digit cells; counting steps the *whole figure* through 14
  intermediate values (record × k/14, rounded as the record rounds —
  tonnes to whole, blade hours to 0.5) at 70ms intervals.
- **Motion spec.** Trigger: band crosses 70% viewport, once per session.
  Count duration ≈1000ms (14 steps × 70ms) per figure, figures staggered
  120ms apart. The step curve is deliberately uneven — steps land on a
  `steps()` timing with a 30ms dwell irregularity seeded per figure — an
  odometer, not a metronome. Final value holds; a 160ms `--ease-settle`
  1px drop seats the figure when its count completes (the tally board's
  tile dropping in).
- **States.** *Rest:* final figures. *Hover:* none. *Focus:* none —
  figures are not controls. *Scrolled-past:* final. *Disabled / no-JS:*
  final figures printed from `BLOCK` at first paint; counting is a
  JS-only ceremony over complete data.
- **Content merge.** The band is the yard's production record presented
  as its tally — and because the same `BLOCK.yard` object renders the
  spec table's capacity row and the footer's day tally, a visitor who
  checks finds one set of numbers everywhere. The count-up is how the
  record is *read out*, not a decoration on it.
- **Failure fallback.** Watchdog at 1800ms: any figure mid-count snaps to
  final. If `BLOCK.yard` is absent the band does not render — the theme
  prints no figure it cannot source (§1).
- **Reduced-motion variant.** Figures stand at final values; the 1px seat
  drop is cut.
- **Performance budget & mobile variant.** Text updates only, ≤4 figures
  × 14 steps; trivially cheap. Mobile (<768px): figures stack 2×2, size
  34px, count steps reduce to 10 × 60ms (600ms) — a phone tally is read
  faster.
- **Choreography timeline (v2).** Band crosses 70% → t=0 figure 1 starts
  stepping → t=120 figure 2 → t=240 figure 3 → each completes ≈1000ms
  after its start with the 1px seat drop → t≈1400 band at rest, record
  date ticket stamps (§6.4's twang at 120ms, the band's one snap).
- **State matrix (v2).** *Rest:* final figures. *Hover:* none. *Focus:*
  none. *Active:* n/a. *Scrolled-past:* final. *Disabled:* printed
  final. *Touch:* identical, compressed steps.
- **Breakpoints (v2).** ≥1200px: 4 across, 44px. 768–1199px: 4 across,
  36px. <768px: 2×2, 34px, 10 steps.
- **Edge cases & failure modes (v2).** *Figure with decimals (blade
  hours 96.5):* intermediate steps round to the record's own precision
  (0.5) — a step may repeat a value; that is honest odometer behaviour,
  not a bug. *Huge figures (tonnage > 9999):* comma formatting at every
  step, width reserved from the final string so the band never reflows
  mid-count. *Re-entry:* counts once per session; re-entry shows finals.
- **Accessibility spec (v2).** The counting element is `aria-hidden`
  during the count; a visually hidden sibling carries the final figure
  from first paint, so AT never hears a number mid-strike. Final figures:
  `--ticket` on `--core` **11.28:1** (§2's measured ticket/core pairing).
  Labels `--sawn` on `--core` 5.07:1.
- **Tokens consumed (v2).** `--core`, `--ticket`, `--sawn`,
  `--ease-settle`, `--dur-count-step` (70ms), `--dur-count` (≈1000ms).

### 6.8 Fresh-cut image frames

- **What & why.** Photographs sit in frames whose edges carry animated
  saw-tooth scoring; the image scales from 1.06 to 1.0 inside the frame
  as it centres, and the scoring catches a moving light gradient. It
  belongs because the frame is the cut edge of the slab the photo
  depicts: product photography presented as the stone itself, fresh off
  the saw, its edge still marked by the blade.
- **Structure.** A `<figure>` with a 10px frame border built from four
  edge strips, each an inline SVG repeating saw-tooth score marks
  (triangular nicks, 7px pitch) in `--wet` on `--sawn`. The `<img>` sits
  inside with `overflow: hidden` on the frame box; scale is applied to
  the image only. The light gradient is a `linear-gradient` overlay on
  the frame strips (never over the image), its position scrubbed. The
  caption is a ticket slip (§4) under the frame carrying the stone's
  name, bed and §6.3's callout anchor.
- **Motion spec.** Trigger: scroll scrub through the shared loop. Scale =
  1.06 − 0.06 × (piece's progress through the centre band of the
  viewport), lerped 0.10; the light gradient's position travels 0→100%
  across the same progress, so scoring glints as the piece passes the
  light. Both fully reversible. At rest (centred) scale is exactly 1.0
  and the gradient rests at 62% — the worked position, not a loop.
- **States.** *Rest:* scale 1.0, scoring lit at rest position. *Hover:*
  the frame's callout (§6.3) rises; the image itself does not move —
  stone photographs are not hover toys. *Focus:* same as hover via
  focus-within. *Scrolled-past:* scale returns toward 1.06 symmetric —
  the piece is only "fresh" while centred. *Disabled / no-JS:* scale
  1.0, static scoring, full caption.
- **Content merge.** The frame's scoring is the depicted slab's own cut
  edge and its caption ticket names the bed the stone came from — frame,
  photo and ticket are one exhibit. A stock photo in this frame without a
  named bed is refused at content review (§9.6).
- **Failure fallback.** Image fails to load: the frame holds a `--sawn`
  ground with the ticket and a mono line "FACE NOT PHOTOGRAPHED — SEE
  TICKET" — the exhibit degrades to its record, never to a broken-image
  icon. Scale scrub failing (loop stall) leaves the image at 1.0 by the
  loop's snap rule (§5).
- **Reduced-motion variant.** Scale fixed at 1.0; gradient static at 62%;
  scoring drawn.
- **Performance budget & mobile variant.** Transform on the image,
  background-position on the strips — compositor only. Frame SVG ≤2KB
  per edge set, shared via `<use>`. Mobile (<768px): frame thins to 6px,
  score pitch 5px, scale range compresses to 1.03→1.0 (small screens,
  small ceremony).
- **Choreography timeline (v2).** Piece enters centre band → scale lerps
  1.06→1.0 across the band's travel, gradient 0→100% in step → centred:
  rest → callout first-draw fires (§6.3) → exits band: symmetric return.
- **State matrix (v2).** *Rest:* 1.0, lit scoring. *Hover:* callout
  rises only. *Focus:* same. *Active:* n/a. *Scrolled-past:* returning
  toward 1.06. *Disabled:* static finished frame. *Touch:* scrub
  identical; no hover state, callout on entry (per §6.3 mobile rule).
- **Breakpoints (v2).** ≥1200px: 10px frame, full scale range.
  768–1199px: 8px frame, 1.04→1.0. <768px: 6px frame, 1.03→1.0.
- **Edge cases & failure modes (v2).** *Portrait vs landscape:* the
  centre band math is height-relative; a tall portrait piece completes
  its scale across its own travel, never early. *Image with its own
  border in the asset:* rejected at ingest — a photographed frame inside
  the cut frame is a forgery (§9.6). *Slow image:* the frame and ticket
  render first; the image fades in over 300ms on load *inside* the
  frame — the only fade-in licensed in the theme, because an unloaded
  photograph is not content being hidden, it is content arriving.
- **Accessibility spec (v2).** Alt text names the stone, bed and finish
  ("Sawn face of Brackenfell grey, Bed 2, honed") — never "image of
  rock". The frame and scoring are decorative (`aria-hidden` on the SVG
  strips). Caption ticket text is `--core` on `--ticket` 11.28:1.
- **Tokens consumed (v2).** `--sawn`, `--wet`, `--ticket`, `--core`,
  `--loop-lerp` (0.10), `--scale-frame` (1.06→1.0).

### 6.9 Core-drill click

- **What & why.** Clicking a slab's ticket stamp line punches a small
  drill-dot — a concentric ring, 6px — into the slab's corner with a
  150ms thud scale, and the slab's ticket gains a "CORED ✓" stamp line.
  The cored slabs are collected into the sample/offcut request list that
  the footer form (§6.15) submits. It belongs because it is how a yard
  visitor actually behaves: you mark the pieces you want sampled, and the
  marks become your order. Inspection *is* the conversion path.
- **Structure.** Each slab ticket carries a real `<button>` styled as the
  ticket's stamp line ("CORE THIS SLAB"). On activation, a drill-dot
  element (two concentric ring borders, 6px core in `--survey`, ring in
  `--core`) is stamped into the slab's top-right corner at a fixed
  offset, and the button's line rewrites to "CORED ✓ — ON YOUR LIST"
  in `--survey-deep`. State lives in a `Set` of ticket numbers mirrored
  to `sessionStorage`; §6.15's form reads the same set.
- **Motion spec.** Trigger: click/tap/Enter/Space on the stamp line. The
  dot scales 1.6→1.0 over 150ms `--ease-settle` with a 1px slab-corner
  shudder (translate 1px, 60ms, once) — the thud. The stamp line
  crossfades 120ms. Un-coring (second activation) fades the dot over
  200ms and restores the line — a core hole can be un-marked on a list
  even if it can't in stone, and the copy says so ("REMOVED FROM LIST —
  THE HOLE STAYS IN THE YARD'S COPY").
- **States.** *Rest (uncored):* stamp line invites. *Hover:* the line's
  rule thickens 1px→2px. *Focus:* 2px `--survey-deep` outline. *Active:*
  1px press + thud. *Cored:* dot present, line rewritten, slab corner
  marked in the footer list (§6.17). *Disabled:* a slab with no samples
  available renders the line as plain text "NO CORES LEFT THIS SEASON" —
  not a disabled button, a fact.
- **Content merge.** The dot marks the actual slab inspected, on the
  slab; the list it feeds is the form's real input. Nothing about the
  interaction is decorative: remove it and the site loses its ordering
  mechanism.
- **Failure fallback.** No JS: the stamp line is an anchor to the form
  (§6.15) with the slab's ticket pre-named in the link text ("ASK FOR A
  CORE OF TICKET 04") — the paper route to the same request. Storage
  unavailable: the set lives in memory for the session; the form still
  reads it.
- **Reduced-motion variant.** Dot appears at final scale (no thud, no
  shudder); stamp line swaps without crossfade.
- **Performance budget & mobile variant.** Negligible: one element per
  cored slab. Mobile: the stamp line is a full-width 48px tap target in
  the ticket; the dot stamps at the ticket's corner instead of the slab's
  (the slab corner may be off-screen on a phone — the mark goes where the
  ticket is).
- **Choreography timeline (v2).** Activation → t=0 dot scales in 150ms +
  corner shudder 60ms → t=120 stamp line crossfades to CORED → footer
  list count (§6.17) ticks +1 (stepped, §6.7's grammar) → form's list
  (§6.15) gains the ticket row.
- **State matrix (v2).** *Rest:* inviting line. *Hover:* rule thickens.
  *Focus:* outline. *Active:* press + thud. *Scrolled-past:* state
  persists (marks are session facts). *Disabled:* fact line, no control.
  *Touch:* 48px target, thud retained (it is 150ms, not a ceremony).
- **Breakpoints (v2).** ≥1200px: dot at slab corner. 768–1199px: same.
  <768px: dot at ticket corner, full-width target.
- **Edge cases & failure modes (v2).** *Coring every slab:* licensed —
  the list is a list; the form (§6.15) handles 1–12 tickets. *Double
  activation in the thud window:* the toggle reads state at activation,
  not at animation end; no double dots. *Session restore:* dots and
  lines re-render from storage at paint, without thuds.
- **Accessibility spec (v2).** A real `<button>` with `aria-pressed`
  reflecting cored state and an accessible name carrying the ticket
  ("Core slab Ticket 04, Sawn Slabs"). State change is announced via the
  form list's `aria-live="polite"` summary ("Ticket 04 added to your
  core list, 3 in all") — the dot itself is `aria-hidden` decoration of
  a state the words already carry. Contrast: stamp text `--survey-deep`
  on `--ticket` 5.47:1.
- **Tokens consumed (v2).** `--survey`, `--survey-deep`, `--core`,
  `--ticket`, `--ease-settle`, `--dur-thud` (150ms).

### 6.10 Saw-cut page transition

- **What & why.** On navigation, a bright horizontal line sweeps the
  viewport in 300ms and the old page splits into two slabs that slide
  apart along it before the new page settles. Leaving the page is the
  same act as cutting the block — the site's one material verb, applied
  to navigation itself.
- **Structure.** A transition overlay: two full-viewport panels (upper
  and lower) skinned with the *outgoing* page's own grounds (fresh above,
  sawn below, sampled from its first and last slabs), a 2px bright line
  (`--ticket` with the survey leading edge, §6.1's blade turned
  horizontal) at their join. The panels are clones of nothing — flat
  stone skins with the outgoing page's ticket number stamped at the
  seam — the content itself is never duplicated or moved.
- **Motion spec.** Trigger: route change (or same-page anchor travel at
  half brightness). t=0 the line ignites at the seam and sweeps its glow
  across in 300ms `--ease-saw`; the panels then part — upper −24px,
  lower +24px over 380ms `--ease-crack` — revealing the incoming page
  already rendered beneath, which settles its first slab (§5 settle,
  700ms) as the panels exit fully by 700ms. Total ≤700ms; the incoming
  page is interactive from t=380 (panels are `pointer-events: none`
  throughout).
- **States.** *Rest:* absent. *Running:* as above; a second navigation
  during the transition cancels to the newest target (panels snap away).
  *Disabled:* no-JS and reduced-motion navigations are plain — the
  browser's own change of page, which needs no apology.
- **Content merge.** The skins carry the outgoing page's ticket number
  and grounds — the transition is *this block being cut*, not a branded
  wipe. The seam stamp ("YOU ARE LEAVING TICKET SET A — THE YARD") is
  the only text, set in mono on the lower panel.
- **Failure fallback.** If the incoming route errors, the panels rejoin
  (reverse part, 250ms) over the outgoing page, which never unloaded —
  a cut that found a flaw is closed, not completed. Transition API
  unsupported: instant navigation, no overlay.
- **Reduced-motion variant.** None — plain navigation.
- **Performance budget & mobile variant.** Two flat panels, transforms
  only; ≤0.2ms/frame. Mobile: parting distance halves to 12px, total
  550ms — phones get the same verb, shorter sentence.
- **Choreography timeline (v2).** t=0 line ignites → t=0–300 glow sweep
  → t=300–680 panels part 24px `--ease-crack` → t=380 incoming page
  interactive, first slab settling → t=700 panels removed from DOM.
- **State matrix (v2).** *Rest:* absent. *Hover/focus/active:* n/a —
  input passes through. *Scrolled-past:* n/a. *Disabled:* absent.
  *Touch:* identical, halved distances.
- **Breakpoints (v2).** ≥1200px: 24px part. 768–1199px: 18px. <768px:
  12px, 550ms total.
- **Edge cases & failure modes (v2).** *Back/forward cache:* a bfcache
  restore never replays the transition. *Slow route (>700ms):* panels
  hold parted at 24px with the skeleton (§6.16) visible beneath — the
  cut waits open rather than closing on an unready page. *Hash-only
  change:* half-brightness variant, panels part 8px, 350ms total.
- **Accessibility spec (v2).** The overlay is `aria-hidden`; navigation
  is announced by the incoming page's own title and focus moves to its
  `<h1>` (or the anchor target) exactly as in an unadorned navigation.
  Focus is never inside the overlay. The 300ms line sweep is below
  flash thresholds (single pass, no repetition).
- **Tokens consumed (v2).** `--ticket`, `--survey`, `--fresh`, `--sawn`,
  `--ease-saw`, `--ease-crack`, `--dur-transition` (700ms).

### 6.11 Bench-mark navigation

- **What & why.** The masthead is a surveyor's bench mark: a core-dark
  bar carrying the yard's wordmark in Expanded, the section links set as
  ticket stubs (mono, numbered with the slabs' ticket numbers), and —
  below 1200px — the chalk strip that inherits the progress rail (§6.4).
  It belongs because navigation in a yard is by ticket number: you do not
  browse a quarry, you ask for a ticket.
- **Structure.** A `<header>` on `--core`, sticky at ≥1200px only while
  the hero is in view, thereafter static (a yard sign does not follow you
  down the pit). Wordmark left (Archivo Expanded 700, `--ticket`), nav
  right: links as ticket stubs — mono 12px uppercase, ticket number +
  name ("04 · SAWN SLABS"), separated by 1px `--wet` rules. The current
  section's stub gains a survey tick and `--ticket` text; others sit in
  `--sawn`. The §6.9 core list count rides at the bar's right end ("YOUR
  CORES: 3") as a link to the form.
- **Motion spec.** On load the bar settles from −8px over 400ms
  `--ease-settle` — a sign craned onto its posts. Current-stub migration
  as sections pass: the survey tick slides between stubs over 250ms
  `--ease-draw`, driven by the same boundary events as §6.4 (never per
  frame). No other motion: the masthead is furniture.
- **States.** *Rest:* as built. *Hover:* stub text to `--ticket`, rule
  beneath draws 1px. *Focus:* 2px `--survey-deep` outline (visible on
  core at 3.76:1 as a mark, backed by the text brightening). *Active:*
  1px press. *Scrolled-past:* static (unstuck) beyond the hero at
  desktop; sticky throughout on mobile where the chalk strip lives in
  it. *Disabled / no-JS:* fully rendered, current stub marked from the
  route.
- **Content merge.** Stub numbers are the slabs' ticket numbers — the
  same numbers as the tickets (§4), the rail (§6.4) and the footer index
  (§6.17). A visitor who learns one numbering has learned the whole
  site's.
- **Failure fallback.** Nothing to fall back from: the bar is static DOM.
  If JS fails, current-stub migration stops; the route-marked stub from
  the server remains correct for the landing section.
- **Reduced-motion variant.** Bar appears without the settle; tick jumps
  between stubs.
- **Performance budget & mobile variant.** Static; tick transform only.
  Mobile (<768px): wordmark + current ticket + a "TICKETS" disclosure
  button opening the stub list as a full-width sheet on `--core` (44px
  targets, Esc closes, focus returns). The chalk strip (§6.4) sits under
  the bar at 3px height.
- **Choreography timeline (v2).** t=0 bar settles 400ms → hero saw cut
  (§6.1) runs beneath it → boundary events migrate the tick 250ms per
  change → past hero (desktop): bar un-sticks and scrolls away with the
  block.
- **State matrix (v2).** *Rest:* settled, current marked. *Hover:* text
  brightens + rule. *Focus:* outline. *Active:* press. *Scrolled-past:*
  un-stuck (desktop) / stuck with strip (mobile). *Disabled:* static,
  route-marked. *Touch:* disclosure sheet pattern.
- **Breakpoints (v2).** ≥1200px: full stubs, hero-sticky. 768–1199px:
  stubs compress to numbers + short names, chalk strip appears.
  <768px: disclosure pattern, strip 3px.
- **Edge cases & failure modes (v2).** *Many sections (>9 slabs):* stubs
  wrap to a second row on tablet; on desktop the bar grows to two rows
  rather than shrinking type below 12px — legibility is not traded for
  tidiness. *Long yard name:* wordmark truncates to its initials mark +
  full name in the hero — the bar is a sign, not the name's only home.
- **Accessibility spec (v2).** `<nav aria-label="Yard sections">`; current
  link `aria-current="true"`. Text contrasts on `--core`: `--ticket`
  11.28:1, `--sawn` 5.07:1 — sawn stubs are
  12px bold mono, licensed as labels, and brighten to ticket on hover and
  focus so no state rests at the floor.
- **Tokens consumed (v2).** `--core`, `--ticket`, `--sawn`, `--wet`,
  `--survey`, `--survey-deep`, `--ease-settle`, `--ease-draw`.

### 6.12 The first face — hero composition

- **What & why.** The hero is the block's fresh face: full-bleed
  fresh-cut ground with the saw-scored background texture, the engraved
  headline (§6.1), a standfirst, the hero ticket, one framed photograph
  of the face (§6.8) with dust in its light (§6.5), and the first
  dimension callout (§6.3) measuring the hero slab itself. It belongs as
  a composition because the hero is not a banner above the page — it is
  slab 01, numbered and ticketed like every slab below it.
- **Structure.** A `<section>` on `--fresh` with a saw-scored SVG texture
  layer (concentric arc scores, `--sawn` at 30%) parallaxing at 0.92×.
  Grid: headline across 6 columns, standfirst 3, the framed face
  photograph 4 columns right with its ticket, hero ticket pinned top-left
  per §4 anatomy. The hero's callout measures the section's own box.
  Height: 100vh capped at 880px, floor 560px — a face you can take in at
  one look.
- **Motion spec.** Load sequence: bar settles (§6.11) → saw cut (§6.1,
  1200ms) → standfirst fade (400ms) → ticket prints (§6.4's twang
  grammar, 120ms stamp) → photograph's frame scrub begins with scroll →
  dust starts on view (§6.5). Scroll: texture parallaxes ±18px cap; the
  hero callout draws as the hero centres on load (it starts centred — it
  draws at t=1500 in the load sequence).
- **States.** *Rest:* cut face, all furniture printed. *Hover:* the
  photograph's callout rises (§6.3). *Focus:* first focusable is the
  hero ticket's core line (§6.9). *Scrolled-past:* hero retires; its
  seam becomes the first saw cut of the page. *Disabled / no-JS:* the
  complete face, statically — headline engraved, ticket printed, photo
  framed.
- **Content merge.** Every hero element is a working part used again
  below: ticket, callout, frame, dust. The hero teaches the page's whole
  grammar in one slab; nothing in it is a one-off effect.
- **Failure fallback.** Each sub-element carries its own fallback
  (§6.1/6.3/6.5/6.8); the composition's own watchdog at 2000ms forces any
  unprinted furniture (ticket, standfirst) to full state.
- **Reduced-motion variant.** The finished face: cut headline, printed
  ticket, still photograph, no dust, no parallax.
- **Performance budget & mobile variant.** Hero budget: photograph ≤180KB
  (the page's largest asset, §14), texture SVG ≤8KB, total hero ≤220KB.
  Mobile (<768px): single column — ticket, headline, standfirst, photo
  full-width; height auto (min 0) — a phone shows a face, not a
  viewport-locked poster.
- **Choreography timeline (v2).** t=0 bar settle → t=0–1200 saw cut,
  letters dropping → t=1350 standfirst → t=1500 ticket stamp + callout
  draw → dust live → scroll: parallax + frame scrub → hero seam becomes
  §6.2's first crack as slab 02 pins.
- **State matrix (v2).** *Rest:* complete face. *Hover:* callout rise.
  *Focus:* per sub-element. *Active:* n/a. *Scrolled-past:* retired to
  seam. *Disabled:* complete static face. *Touch:* same sequence,
  compressed per sub-element mobile rules.
- **Breakpoints (v2).** ≥1200px: 100vh (≤880px), 6-col composition.
  768–1199px: 84vh, photo 5 cols. <768px: stacked, auto height.
- **Edge cases & failure modes (v2).** *Short viewport (landscape
  phone):* height floor releases below 560px rather than cropping the
  ticket — furniture outranks proportion. *No photograph supplied:* the
  face is texture + headline + ticket only, and the layout closes up —
  an unphotographed face is licensed (§6.8's record line), a gap is not.
- **Accessibility spec (v2).** Landmark `<section aria-label>` from the
  ticket name; heading order h1 → ticket heads are `<p>` furniture, not
  headings. All contrasts per §2 pairings; the engraved headline reads
  at 8.69:1 (core on fresh) in every state.
- **Tokens consumed (v2).** `--fresh`, `--sawn`, `--core`, `--ticket`,
  `--loop-lerp` (0.10), plus sub-element tokens (§6.1, 6.3, 6.5, 6.8).

### 6.13 Yard cards — slab listing

- **What & why.** The yard's available slabs are cards — but a card here
  is a cut piece resting on the saw table: a sawn-face block with its
  photograph in a fresh-cut frame (§6.8), its ticket (name, bed, finish,
  nominal dimensions), its §6.3 callout, its §6.9 core line, and a small
  heavy tilt (max 2°) as the pointer crosses it, rocking on its lower
  edge like stone nudged on a table. It belongs because the listing *is*
  the yard: pieces you can measure, mark and ask for.
- **Structure.** A `<ul>` grid of `<li>` cards on the slab's ground. Each
  card: frame + photo, ticket block (Plex Mono head: piece ticket number
  and name; Archivo body: bed and finish in one line), nominal dimension
  line, price per m² in mono where the yard prices publicly, and the core
  stamp line (§6.9). Cards are generated from `BLOCK.slabs`-sibling
  `BLOCK.pieces[]` — the same objects the spec table (§6.14) lists, so
  card and table row can never disagree on a dimension.
- **Motion spec.** Entry: cards settle in slab order, 700ms
  `--ease-settle`, 90ms stagger (§5). Tilt: on pointer move over a card,
  rotate toward the pointer's half by ≤2° around the bottom edge
  (transform-origin: 50% 100%), lerped at 0.14 by the shared loop (a
  dedicated faster lerp — a nudge answers quicker than a scroll); on
  leave, settle back over 500ms `--ease-settle`. The callout draws on
  first centre (§6.3). Nothing else moves: price, ticket and core line
  are still.
- **States.** *Rest:* flat, measured. *Hover:* tilt ≤2° + callout full
  ink. *Focus:* no tilt (keyboard visitors get a still piece and a full
  callout — tilt is a pointer courtesy, never information). *Active:*
  the core line presses per §6.9. *Scrolled-past:* flat. *Disabled /
  no-JS:* flat cards, nominal callouts, core lines as form anchors
  (§6.9 fallback).
- **Content merge.** The card is the piece: its photo is the piece's
  face, its ticket the piece's record, its callout the piece's measured
  size, its core line the way to order a sample of *this* piece. A card
  stripped of any one of these is a picture with a price, which is what
  the theme exists to refuse.
- **Failure fallback.** Photo missing: §6.8's record-line frame. Tilt
  failing (no transform support): flat cards — tilt is the most cuttable
  motion on the page (§14). Data missing for a piece: the piece does not
  render (§1).
- **Reduced-motion variant.** No tilt, no settle stagger; cards stand
  printed in order.
- **Performance budget & mobile variant.** Tilt is one transform per
  hovered card; entry settles are transform+opacity. Mobile (<768px):
  single column, **tilt cut entirely** (touch has no hover and a rocking
  card under a reading thumb is a defect), callouts per §6.3 mobile rule,
  cards full-width so dimensions measure honestly at phone size.
- **Choreography timeline (v2).** Slab head crosses 82% → cards settle
  90ms apart → first card centres → its callout draws (500ms, §6.3) →
  pointer crosses a card → tilt lerps to ≤2° within ~200ms → leave →
  500ms settle to flat.
- **State matrix (v2).** *Rest:* flat. *Hover:* tilt + callout. *Focus:*
  callout only. *Active:* core-line press. *Scrolled-past:* flat.
  *Disabled:* printed flat. *Touch:* no tilt; tap raises callout 3s
  (§6.3).
- **Breakpoints (v2).** ≥1200px: 3 across. 768–1199px: 2 across, tilt
  ≤1.5°. <768px: 1 across, no tilt.
- **Edge cases & failure modes (v2).** *One piece only:* the grid holds
  a single card at 2-col span — a lone piece is displayed like a
  specimen, not stretched. *Very long piece name:* ticket head wraps to
  two lines, card heights in the row equalise by the tallest ticket —
  the row is a bench, pieces rest level. *Cored card:* the §6.9 dot
  stamps the card's corner too (same state, second printing).
- **Accessibility spec (v2).** Cards are list items; the piece name is a
  heading (h3) inside its slab's h2. The core button's name carries the
  piece ticket (§6.9). Tilt is `aria-hidden` behaviour — no state
  information travels by angle. Ticket text `--core` on `--sawn` 5.07:1
  for heads and labels; body lines on the card sit on `--fresh` insets
  at 8.69:1.
- **Tokens consumed (v2).** `--sawn`, `--fresh`, `--core`, `--ticket`,
  `--ease-settle`, `--dur-settle` (700ms), `--tilt-max` (2°).

### 6.14 The specification table

- **What & why.** The yard's full specification — stone, bed, finish,
  thickness range, max slab size, price — as a real `<table>` styled as
  a quarry ledger: mono figures, ruled rows, a ticket head. It belongs
  because a quarry sells by specification, and the table is where this
  theme's law is most exposed: every row's figures come from the same
  `BLOCK.pieces[]` objects as the cards (§6.13), and the capacity row
  quotes `BLOCK.yard` (§6.7) — three printings, one record.
- **Structure.** A `<table>` on `--ticket` ground inside a sawn slab:
  caption as the ticket head ("SPECIFICATION — ALL STONE, CURRENT
  SEASON"), `<th>` row in Plex Mono 600 uppercase, figures right-aligned
  mono, row rules 1px `--sawn`, zebra none (ledger lines do not
  alternate; the rule is the rhythm). Sortable by the dimension column
  via real `<button>`s in the headers. A footer row states the record
  date and scale (§4) — the table carries its own audit line.
- **Motion spec.** Almost none, by design: the table is a record, and
  records do not perform. On first entry, row rules draw left-to-right
  in one 600ms `--ease-draw` pass, rows staggered 40ms — the ledger
  being ruled. Sorting re-orders rows with a 180ms FLIP settle
  (`--ease-settle`, transform only). That is all.
- **States.** *Rest:* ruled, complete. *Hover:* row ground warms one
  step (ticket → fresh) — a finger running down the ledger. *Focus:*
  sort buttons take the §6.11 outline. *Active:* sort press 1px.
  *Scrolled-past:* rest. *Disabled / no-JS:* complete table, unsorted
  (server order = bed order), rules drawn.
- **Content merge.** The table is not a summary of the cards; it is the
  same record in ledger form, and its footer prints the scale the
  callouts (§6.3) measure by — the page's three dimension systems
  (measured, nominal, tabulated) meet in this element and must agree.
- **Failure fallback.** If `BLOCK.pieces` fails to load, the slab shows
  the ticket line "SPECIFICATION NOT ISSUED — ASK THE YARD" with the
  form link (§6.15) — a missing record is stated, never faked with
  placeholder rows.
- **Reduced-motion variant.** Rules pre-drawn; sorting swaps instantly.
- **Performance budget & mobile variant.** Static DOM; FLIP on ≤40 rows
  capped — beyond 40 rows sorting is instant (a big ledger is re-filed,
  not animated). Mobile (<768px): the table becomes stacked ticket rows
  (each row a mini-ticket: name line, then figure pairs) — horizontal
  scrolling a ledger on a phone is refused; the data is identical, the
  ruling adapts.
- **Choreography timeline (v2).** Slab centres → rules draw 600ms,
  40ms/row → rest → sort activation → FLIP 180ms → `aria-sort` updates →
  footer audit line unchanged throughout (it is the constant the motion
  is measured against).
- **State matrix (v2).** *Rest:* ruled. *Hover:* row warms. *Focus:*
  sort outline. *Active:* press. *Scrolled-past:* rest. *Disabled:*
  printed, server order. *Touch:* stacked tickets; sort via a labelled
  select styled as a ticket line (the one licensed select, §11).
- **Breakpoints (v2).** ≥1200px: full table. 768–1199px: table, price
  column folds into the name cell as a second line. <768px: stacked
  tickets.
- **Edge cases & failure modes (v2).** *A piece with no public price:*
  the cell reads "PRICE ON TICKET" — an honest absence, never a dash
  that looks like data. *Thickness range vs single value:* ranges print
  "40–60" in one cell; the sort key is the range's lower bound, stated
  in the header's `aria-label`. *Print:* the table is the page's most
  printed element; §14's print sheet rules it in black on white.
- **Accessibility spec (v2).** Real table semantics: `<th scope>`,
  caption, `aria-sort` on the active header. Figures `--core` on
  `--ticket` 11.28:1. The stacked mobile form preserves reading order
  (name before figures) and the sort select has a visible mono label.
- **Tokens consumed (v2).** `--ticket`, `--fresh`, `--sawn`, `--core`,
  `--ease-draw`, `--ease-settle`, `--dur-rule-draw` (600ms).

### 6.15 The offcut request form — conversion

- **What & why.** The conversion section is a quarry ticket made into a
  form: on ticket paper, the visitor's cored slabs (§6.9) pre-listed as
  the request's line items, fields for name, yard or site address, and
  the cut they want (sample core / offcut / full slab per ticket), and a
  submit that stamps the ticket rather than "sending" it. It belongs
  because in this theme conversion is not a funnel — it is paperwork the
  yard actually processes, and the form's honesty (your marks, your
  list, a reference derived from the record) is the pitch.
- **Structure.** A `<form>` on a `--ticket` slip (max 640px) inside a
  core-dark slab — the office at the pit's edge. Line items: one row per
  cored ticket (number, name, a radio trio SAMPLE / OFFCUT / FULL SLAB,
  a remove line). Below: name and address fields with mono labels (§3),
  a notes field ("THE CUT YOU WANT — PLAIN WORDS ARE FINE"). Submit: a
  core-dark block button with a survey edge (§2 law 1), text "STAMP THIS
  TICKET". On success the slip is replaced by its stamped copy: the same
  data, a "RECEIVED" stamp in `--survey-deep`, and a reference computed
  from the record — `QF-` + the day's ticket count from `BLOCK.yard`
  incremented — printed as the visitor's copy.
- **Motion spec.** Fields focus: the field's rule draws in `--core` over
  260ms `--ease-draw` (the clerk underlining). Line-item rows settle in
  at 90ms stagger when added from §6.9. Submit: the button presses 1px,
  a stamp animation — the RECEIVED stamp scales 1.4→1.0 with
  `--ease-settle` over 180ms at a −3° rest rotation — then the slip's
  contents crossfade to the stamped copy over 300ms. Errors: the field's
  margin note (§12 voice) writes in with a 200ms rule draw; nothing
  shakes — yards do not shake paperwork.
- **States.** *Rest:* cored list pre-filled (or the empty state, below).
  *Hover:* controls per §11. *Focus:* rule draw + visible outline on
  radios. *Active:* press. *Submitting:* button text "STAMPING…" for the
  real request duration, fields inert. *Success:* stamped copy,
  reference printed, list cleared in §6.9's set (the cores are now the
  yard's). *Disabled:* a field the record cannot accept (e.g. OFFCUT for
  a slab with no offcuts) is not disabled — it is absent, with the fact
  stated on the ticket ("NO OFFCUTS FROM THIS BED THIS SEASON").
- **Content merge.** The form's line items *are* the visitor's own marks
  from §6.9 — the conversion was assembled by inspecting the yard, not
  by filling a cart. The reference derives from the same yard record as
  §6.7's figures; the stamped copy is a fourth printing of the record
  agreeing with the other three.
- **Failure fallback.** No JS: the form is a plain HTML form posting to
  the yard's endpoint, line items replaced by a "TICKETS YOU WANT"
  text field pre-filled from the §6.9 no-JS anchor route. Submit failure
  (network): the slip keeps all input, an error line in the clerk's
  voice (§12) states the ticket was not stamped and to try again — input
  is never lost to a failed stamp.
- **Reduced-motion variant.** No stamp scale, no crossfade; states swap
  instantly. Rule draws become instant rules.
- **Performance budget & mobile variant.** The form is DOM-light; the
  stamp is one transform. Mobile (<768px): slip full-width, radio trios
  become stacked 48px rows, submit sticky at the slip's foot within the
  slab — the one sticky control the theme licenses, because a half-filled
  ticket on a phone is where requests die.
- **Choreography timeline (v2).** Slab centres → slip settles 700ms →
  cored rows stagger in 90ms → focus: rule draws 260ms → submit: press →
  real request → stamp lands 180ms → crossfade 300ms → stamped copy at
  rest, reference legible, §6.17 footer count updates.
- **State matrix (v2).** *Rest:* filled from the visitor's marks.
  *Hover:* §11 control states. *Focus:* rule + outline. *Active:* press.
  *Scrolled-past:* state kept (a half-filled ticket survives scrolling —
  it is a document). *Disabled:* absent-with-fact pattern, above.
  *Touch:* 48px rows, sticky submit.
- **Breakpoints (v2).** ≥1200px: slip 640px centred in the dark slab.
  768–1199px: slip 560px. <768px: full-width slip, stacked radios,
  sticky submit.
- **Edge cases & failure modes (v2).** *No cores marked:* the form still
  works — line items empty, an empty-state line in the yard's voice
  ("NO SLABS CORED YET — THE LIST FILLS AS YOU MARK THEM, OR NAME YOUR
  TICKETS HERE") plus the manual ticket field. *Duplicate submit:*
  the stamp is idempotent — a second activation while stamped reprints
  the same reference, never a second ticket. *Validation:* errors are
  margin notes (§12), fields keep their values, focus moves to the
  first error with its note read by `aria-describedby`.
- **Accessibility spec (v2).** Real `<form>`, real labels, radio groups
  in `<fieldset>` with the ticket name as `<legend>`. Error notes are
  text, `--survey-deep` on `--ticket` 5.47:1, paired with a rule change
  so state is not colour-only. Success is a `role="status"` region
  announcing the reference. All targets ≥44px (48px on touch rows).
- **Tokens consumed (v2).** `--ticket`, `--core`, `--core-deep`,
  `--survey`, `--survey-deep`, `--ease-draw`, `--ease-settle`,
  `--dur-stamp` (180ms).

### 6.16 Unscored skeleton & the saw-pass

- **What & why.** Loading in this theme is unscored stone: sawn-face
  blocks with no scoring, no tickets and no type, occupying the exact
  boxes the slabs will occupy — stone that has been delivered but not yet
  cut. Between routes, §6.10's saw cut opens onto this skeleton when a
  page is slow. It belongs because a skeleton that mimics "content
  loading" with grey bars would be a lie about material; an unscored
  block is the honest prior state of a slab.
- **Structure.** Per-slab skeleton blocks mirroring the slab anatomy
  (§4): a full-width `--sawn` block at the slab's min-height, a
  `--fresh` inset where the ticket will sit, nothing else. No shimmer
  sweep (shimmer is a screen habit; stone does not shimmer — a single
  slow light pass at 6s, gradient at 8% opacity, is the maximum licensed
  and is cut under reduced motion and `save-data`).
- **Motion spec.** Entry: skeleton blocks are present at first paint for
  any slab whose data is pending. Resolution: as each slab's data lands,
  its content settles in per §5 (700ms settle) — the block is "cut" into
  its slab. Hard cap: any skeleton unresolved at 4000ms is replaced by
  the slab's failure line (§6.14's pattern: a stated absence with the
  form link), never left as permanent stone.
- **States.** *Rest:* resolved page. *Loading:* unscored blocks.
  *Failed:* stated absence lines. *Disabled / no-JS:* server-rendered
  content — the skeleton is a JS-data pattern only.
- **Content merge.** The skeleton blocks are the slabs' own boxes at the
  slabs' own heights (min-heights declared per slab type in §4's course
  system), so resolution causes zero layout shift — the cut reveals the
  slab that was always that size.
- **Failure fallback.** The 4000ms cap above is the fallback; a skeleton
  that never resolves and never confesses is the one unforgivable state
  (§9.9).
- **Reduced-motion variant.** Blocks static, no light pass; resolution
  swaps instantly.
- **Performance budget & mobile variant.** Skeleton is pure CSS boxes —
  the cheapest element on the page. Mobile: identical, heights from the
  stacked layouts.
- **Choreography timeline (v2).** Paint: blocks in place → data lands
  per slab → each slab settles 700ms in arrival order (not page order —
  the yard delivers as it delivers) → 4000ms cap sweeps any remainder to
  stated absences.
- **State matrix (v2).** *Rest:* none visible. *Hover/focus:* none —
  skeletons are inert, `aria-hidden`, skipped by tab. *Active:* n/a.
  *Scrolled-past:* resolved or confessed. *Disabled:* absent. *Touch:*
  identical.
- **Breakpoints (v2).** All: same pattern, slab min-heights per
  breakpoint anatomy.
- **Edge cases & failure modes (v2).** *Partial data (slab renders,
  pieces fail):* the slab renders with its pieces' absence lines (§6.13)
  — resolution is per-piece, not all-or-nothing. *Fast load:* if data
  lands before first paint, no skeleton is ever shown — no ceremonial
  flash of stone.
- **Accessibility spec (v2).** Skeleton regions carry `aria-busy="true"`
  on the slab container and are removed from the accessibility tree
  until resolved; a single polite announcement "The yard list is being
  cut" fires if loading exceeds 1200ms, and none if it doesn't.
- **Tokens consumed (v2).** `--sawn`, `--fresh`, `--ease-settle`,
  `--dur-skeleton-cap` (4000ms).

### 6.17 The quarry footer & the offcut list

- **What & why.** The footer is the pit floor: a core-deep slab carrying
  the yard's colophon, the day tally (third printing of `BLOCK.yard`,
  §6.7), the section index by ticket number (third printing of the
  numbering, §6.11), the visitor's core list summary (§6.9), the scale
  line that licenses every callout on the page (§1), and the theme's
  signature anti-slop furniture — the **offcut list**: the page's
  leftover fragments (outtakes, sketches, unused photographs) offered as
  a downloadable bundle, because a yard that wastes nothing says so.
- **Structure.** A `<footer>` on `--core-deep`: four columns at desktop
  (colophon + record; index; your cores; the offcut list), the scale
  line and record date ruled across the foot in mono ("SCALE OF THIS
  PAGE: 1 CSS PX = 2 MM OF STONE · RECORD OF 21 NOV 2026 · DIMENSIONS
  MEASURED LIVE"). The offcut list is a typed mono list of the bundle's
  contents with one download link; the bundle is a real file (zip of the
  listed fragments), generated at build from `BLOCK.offcuts`.
- **Motion spec.** The footer does not perform. On entry, its head rule
  draws once (600ms `--ease-draw`) and the day tally's figures are
  already final (they were counted in §6.7's band; the footer prints
  them, it does not recount — a record read twice in two voices is a
  discrepancy waiting to happen). The core list count ticks by §6.9's
  events only.
- **States.** *Rest:* printed record. *Hover:* links underline with the
  drawn rule. *Focus:* `--ticket` outline on core-deep. *Scrolled-past:*
  n/a (it is the past). *Disabled / no-JS:* complete footer; the core
  summary reads "CORES ARE MARKED ON THE TICKETS ABOVE" (the no-JS route
  has no list to count).
- **Content merge.** The footer is the page's audit trail: scale, record,
  index and tally — the four things a sceptical visitor needs to check
  the page's claims, printed where checking ends. The offcut list merges
  the theme's thrift with the site's real leftovers; a bundle of stock
  filler would violate §1 in spirit.
- **Failure fallback.** Static DOM; nothing to fall back from. A missing
  offcut bundle removes the list and prints "NO OFFCUTS THIS SEASON —
  THE BLOCK CUT CLEAN" — the absence is itself yard news.
- **Reduced-motion variant.** Rule pre-drawn; all else identical.
- **Performance budget & mobile variant.** Static. Mobile (<768px):
  columns stack in audit order (scale line first — on a phone the
  licence travels to the top), offcut list last.
- **Choreography timeline (v2).** Footer enters → head rule draws 600ms
  → rest. §6.9 events anywhere above tick the core count here within the
  same frame batch.
- **State matrix (v2).** *Rest:* printed. *Hover:* rule underline.
  *Focus:* outline. *Active:* link press. *Disabled:* printed, no-JS
  wording. *Touch:* 44px link rows in the index column.
- **Breakpoints (v2).** ≥1200px: 4 columns. 768–1199px: 2×2. <768px:
  stacked, scale line first.
- **Edge cases & failure modes (v2).** *Live vs nominal dimensions:*
  the scale line's final phrase switches with §6.3's mode ("MEASURED
  LIVE" / "NOMINAL — JAVASCRIPT OFF") — the footer confesses which kind
  of truth the page is telling. *Record date stale:* the date is
  `BLOCK.recordDate`; a build older than the yard's season must update
  it or the gate (§10) fails the page as an old record.
- **Accessibility spec (v2).** `<footer>` with labelled nav for the
  index; text `--ticket` on `--core-deep` 13.98:1, secondary `--sawn`
  6.28:1. The download link's name carries the bundle's size and
  contents count ("Download the offcut bundle, 14 fragments, 9 MB").
- **Tokens consumed (v2).** `--core-deep`, `--ticket`, `--sawn`,
  `--survey-deep`, `--ease-draw`.

### 6.18 The uncut block — 404

- **What & why.** The 404 is a block that was never cut: a full fresh-cut
  face with no headline engraved, one ticket stating the fact, and the
  yard's index offered as the way back to cut stone. It belongs because
  in this theme a missing page is not an error state — it is material
  that hasn't been worked, and the honest response is to say so and show
  the visitor the yard plan.
- **Structure.** A hero-height fresh face (§6.12's composition minus
  photograph and headline), a single ticket centred-left: "TICKET Nº —
  / THIS BLOCK HAS NOT BEEN CUT / The address asked for stone this yard
  has not quarried." Below: the section index (the §6.17 list, in-page)
  and the three most-asked tickets as §6.13 cards. The saw seam from
  §6.10 rests at the face's right edge, unused — the cut that wasn't
  made.
- **Motion spec.** None on arrival — an uncut block does not perform. If
  the visitor stays 6s, the saw line makes one slow pass (1200ms,
  §6.1's travel) *without* unmasking anything, and stops: the yard
  offering to cut, once, quietly. Links behave normally; leaving runs
  §6.10.
- **States.** *Rest:* uncut face, ticket, index. *Hover/focus:* per
  §6.11/§6.17 link states. *Disabled / no-JS:* identical, minus the 6s
  pass.
- **Content merge.** The index offered is the site's real index; the
  suggested cards are the yard's real most-asked pieces from `BLOCK` —
  recovery furniture made of the site's own stone, not a search box
  pasted onto a joke.
- **Failure fallback.** The 404 is the fallback; it has none of its own
  beyond being server-rendered and complete without JS.
- **Reduced-motion variant.** No 6s pass. All else identical.
- **Performance budget & mobile variant.** Reuses §6.12's assets; no new
  weight. Mobile: stacked, index first after the ticket.
- **Choreography timeline (v2).** Arrival: stillness → (optional t=6s
  single saw pass, no reveal) → visitor chooses from the index.
- **State matrix (v2).** *Rest:* uncut. *Hover/focus:* link states.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled:* printed. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: hero-height face. 768–1199px: 70vh.
  <768px: auto height, index prominent.
- **Edge cases & failure modes (v2).** *The asked-for URL resembles a
  real ticket:* the ticket adds a line "NEAREST CUT: TICKET 04 — SAWN
  SLABS" with the link — a surveyor's redirect, offered, never forced
  (no silent redirects from a 404). *Soft 404s:* refused — this page is
  served with a real 404 status; dressing a 200 as an uncut block is a
  record falsified.
- **Accessibility spec (v2).** The ticket's first line is the `<h1>`
  ("This block has not been cut") — the fact as the heading, in the
  yard's voice, at 8.69:1. Index links carry full ticket names.
- **Tokens consumed (v2).** `--fresh`, `--core`, `--ticket`, `--sawn`,
  `--ease-saw`.

## 7. Page application map

- **Home (the yard page).** The full descent: hero face (§6.12) → yard
  cards slab (§6.13) → process slab with the core-drill diagram (§6.6),
  pinned → stats band (§6.7) → specification table (§6.14) → request
  form (§6.15) → footer (§6.17). Two splitting pairs maximum (§6.2): face
  → yard, process → stats. A home page with more pins is a quarry with
  too many benches open at once.
- **Listing (all stone / one bed).** Masthead + a shallow hero (no saw
  cut — the face was cut on the home page; a listing opens on sawn
  ground), the full card grid (§6.13) with bed filters as ticket stubs,
  the spec table (§6.14) for the bed, form (§6.15). Callouts carry the
  page: filtering re-measures nothing (boxes change → §6.3's resize rule
  re-issues labels).
- **Detail (one piece).** The piece as a single great slab: framed photo
  (§6.8) at 6 cols, its full ticket, its callout at full ink by default
  (a detail page's visitor came to measure), the core-drill diagram
  (§6.6) re-skinned to *this* piece's strata where the data exists, the
  request form (§6.15) with the piece pre-cored. Related pieces are
  offcuts (§6.17's list logic) — smaller pieces of the same bed.
- **About (the yard itself).** The process slab promoted to the page:
  diagram (§6.6), stats (§6.7), the yard's history set as tickets in
  date order. No hero cut — an about page opens on the record, not the
  face; the masthead's settle is its only ceremony.
- **Contact / yard office.** The form (§6.15) as the whole page, office
  hours and the yard's address as tickets, a map replaced by a survey
  sketch (an SVG of the yard's benches with the office marked — a drawn
  plan, not an embedded map tile; the theme draws its own geography).
- **Checkout equivalent.** There is no cart in a quarry. The request
  ticket (§6.15) *is* the checkout: line items, a stamped reference, and
  the yard's reply by phone or email within one working day, stated on
  the ticket. Any build that bolts a generic cart onto this theme has
  stopped building the theme.

## 8. Worked examples

### 8.1 The hero, end to end — Brackenfell Stone's home page

*Build.* The hero is slab 01 (§6.12). `BLOCK.slabs[0]` = ticket 01, "THE
FACE", ground fresh, nominal "FULL BLOCK FACE". The photograph is the
yard's own north face at 07:40, shot square-on, its light cone falling
left-to-right — the dust (§6.5) is seeded inside that cone and nowhere
else. Headline: "STONE, CUT TO YOUR MEASURE." (27 characters — over the
§12 limit; the yard's copy is corrected at build to "CUT TO YOUR
MEASURE." — 20 characters — because the law about headline length is the
theme checking its own copy first.) The hero ticket reads: TICKET Nº 01
— THE FACE / BRACKENFELL GREY, BED 2 / FACE MEASURED LIVE, with §6.9's
core line.

*Scroll timeline.* t=0 masthead settles (400ms). t=0–1200 the saw cut
(§6.1) crosses; letters drop at ≈40ms intervals; the final full stop
drops at t≈1150 with the largest puff (the blade exiting through the
sentence's end). t=1350 standfirst: "Sawn slabs, offcuts and cores from
one working face in the Brackenfell quarry — every piece ticketed with
its true measure." (24 words, inside the 34-word cap.) t=1500 the ticket
stamps (120ms twang) and the hero callout draws: the section measures
1,176 CSS px wide at desktop → label "THIS FACE: 2,350 × 1,760 MM" —
height 880px × 2mm = 1,760, width rounded to the nearest 10. The visitor
scrolls: texture parallaxes 0.92×, the framed face photo (§6.8) scales
1.06→1.0 through the centre band, and at the hero's foot the first
splitting pair (§6.2) begins its strain.

### 8.2 Mid-page — the process slab and the showcase saw

*Build.* Slab 04, "HOW A BLOCK IS READ", ground sawn. Left column: the
copy, three strata paragraphs (face stone, heart stone, bed stone) in
the order `BLOCK.process` declares. Right: the core-drill diagram
(§6.6). Below, the showcase: one wide framed photograph of a slab on the
saw, across which — scrubbed to scroll through a 130vh pin — a saw line
(§6.1's blade, horizontal, at slab height) travels the photograph's
width, and the photograph's two halves part by 6px along it at full
travel: the picture is cut as you watch, at the speed you scroll.

*Scroll timeline.* Slab head crosses 82% → ticket stamps, title settles.
Slab centres → pin engages (120vh): bore wall draws 400ms, rings at
t=400/700/1000 in copy order, drill path overlaps from t=1150, ticks
stamp to t≈1780; hovering the heart ring rules the heart paragraph's
ticket (§6.6). Pin releases → the showcase pin engages (130vh): saw line
progress = pin progress, halves part 0→6px across the middle third, hold
to the end; scroll back and the cut closes — a photograph may be re-sawn
because it is a picture of a cut, not the cut itself (contrast §6.2,
whose crumble is spent: pictures are representations, slabs are facts —
the theme keeps the distinction).

### 8.3 Conversion — coring three slabs and stamping the ticket

*Build.* The visitor has cored Ticket 04 (a sawn slab), Ticket 07 (an
offcut) and Ticket 09 (a hearth piece) while reading (§6.9). The form
slab (§6.15) centres on core-deep ground. The slip arrives pre-filled:
three line-item rows, each with its radio trio; the offcut's row offers
SAMPLE / OFFCUT only — FULL SLAB is absent with the fact printed ("THIS
PIECE IS AN OFFCUT — THERE IS NO FULL SLAB OF IT"), not greyed out.

*Scroll/interaction timeline.* Slip settles 700ms; rows stagger 90ms.
The visitor chooses OFFCUT for 07, SAMPLE for 04 and 09, types a name
and a site address, leaves the email malformed. Submit: press → the
email field's margin note draws its rule (200ms) and writes, in the
clerk's voice: "That direction will not carry — the part after the @ is
wanting." (§12). Nothing else moves; the slip keeps every value. The
visitor corrects it, submits again: "STAMPING…" for the request's real
340ms → the RECEIVED stamp lands (180ms, −3°) → crossfade 300ms → the
stamped copy: reference **QF-0343** (the day's 342 slabs + this ticket,
from `BLOCK.yard`) and the line "The yard answers within one working
day." The footer core count (§6.17) clears to "CORES: 0 — YOUR TICKET
IS WITH THE YARD."

## 9. Anti-slop — what makes THIS theme look cheap

1. **Dimensions as decoration.** Callout labels typed as copy ("1,840 ×
   60 MM" on every card regardless of size). *Cure:* §6.3's live
   measurement and the §10 audit that resizes a card and fails the build
   if the label doesn't change.
2. **Fade-in stone.** Slabs ghosting in from 0% opacity with a soft
   rise — the generic web reveal wearing a hard hat. *Cure:* §5's rule:
   pre-states at 55% minimum, arrival by settle and weight, never by
   appearing.
3. **Orange everywhere.** Survey orange as button fills, link colours
   and section backgrounds. *Cure:* §2 law 1's ≤2% pixel audit; orange
   is a mark, and a page of marks is a page of noise.
4. **Decorative darkening.** Alternating slab grounds for "visual
   rhythm". *Cure:* §2 law 3 — grounds follow the subject's depth, and
   the build review asks of every dark slab: what in this copy is deep,
   wet or heavy?
5. **Crack clip-art.** A generic jagged divider pasted between every
   pair of sections, including ones that never split. *Cure:* the crack
   path exists only where §6.2's split happens; elsewhere the seam is
   the straight saw cut. A crack that parts nothing is wallpaper.
6. **Stock stone.** Photographs of anonymous cliffs and marble veins in
   fresh-cut frames. *Cure:* §6.8's rule — every framed photo names its
   bed in its ticket and alt; unnamed stone is refused at ingest.
7. **Springy physics.** Bouncy hovers, elastic cards, a chalk line that
   wobbles for fun. *Cure:* the five easings of §5 are the whole
   vocabulary; the twang is rationed to boundaries. If it bounces, it
   isn't stone.
8. **Numbers in display type.** A giant Expanded "1,284 TONNES" as a
   design moment. *Cure:* §3 law 1 — figures are mono records; display
   type is for names.
9. **The eternal skeleton.** Loading blocks that never resolve on a slow
   connection. *Cure:* §6.16's 4000ms confession cap.
10. **A cart.** A basket icon in the masthead of a quarry. *Cure:* §7 —
    the ticket is the checkout; marks become line items (§6.9 → §6.15).

## 10. Quality gate

Blocking items are marked ◆. The theme may not ship with a ◆ failing.

1. ◆ **Ticket-truth audit.** Resize three annotated pieces (browser
   zoom + container change). Every §6.3 label updates to the new true
   measure within one frame batch. Any stale label fails.
2. ◆ **Three-printings agreement.** `BLOCK.yard` figures are identical
   in §6.7's band, §6.14's capacity row and §6.17's tally; ticket
   numbering identical across §6.4, §6.11, §6.17. Checked by DOM diff,
   not by eye.
3. ◆ **No stranded content.** With JS disabled, the full page — headline
   engraved, slabs stacked, tickets printed, form submittable — is
   complete. With JS enabled and the loop force-stalled, every watchdog
   (1600/2000/2500/4000ms) lands its element in its finished state.
4. ◆ **Orange census.** Sample five viewports down the page: survey
   orange ≤2% of pixels in each; zero orange text below 24px; zero
   orange surfaces.
5. ◆ **Reduced-motion pass.** With `prefers-reduced-motion`, no pin,
   split, crumble, dust, count-up or transition runs, and every element
   presents its finished state with identical information.
6. **Pin census.** Exactly the licensed pins (§6.2 pairs ≤2 on home,
   §6.6, §8.2 showcase) and no more.
7. **Easing census.** Grep the build: no easing outside §5's six tokens
   (five + the twang) appears in any animation.
8. **Figure census.** Every number on the page is in Plex Mono and
   traces to `BLOCK` or to a live measurement (§6.3). One untraceable
   figure fails the review.
9. **Frame honesty.** Every §6.8 photograph's ticket and alt name a bed
   present in `BLOCK.pieces`.
10. **Performance.** §14's budgets met on the reference device; the
    shared loop's frame cost ≤1.6ms with all scrubbed elements live.

## 11. Component inventory

Every component a real yard site needs, with its Quarry Cut treatment.
Radius is 0 everywhere except the drill dot (§6.9) and core diagram —
circles exist in this theme only where a drill made them.

| Component | Treatment |
|---|---|
| Primary button | Core-dark block, ticket text, 1px survey bottom edge (§2 law 1); press = 1px down, no shadow change. Text is a yard verb: "STAMP THIS TICKET", "ASK FOR THE LIST" |
| Secondary button | Ticket-paper block with 1px core rule; hover fills fresh. Never orange |
| Text link | Core on its ground, 1px rule beneath that draws on hover (§6.17 grammar) |
| Nav stubs | Ticket stubs in the masthead (§6.11) |
| Inputs | Ticket-paper fields, mono labels above, rule draws on focus (§6.15); filled rules rest at 60% ink |
| Select | Refused except §6.14's mobile sort — and there it is styled as a ticket line with a mono label. Everywhere else, choices are radio tickets |
| Radio / checkbox | Ticket rows: a square (never round — nothing is round but cores) that fills core with a ticket tick when chosen |
| Table | The ledger (§6.14) |
| Cards | Yard cards (§6.13) |
| Badge / tag | A stamp: mono uppercase in a 1px rule box, rotated ≤2° when it marks state (CORED, RECEIVED); informational badges are refused — a fact goes on the ticket, not on a pill |
| Alert | A margin note on the ticket (§6.15): rule + clerk-voice line (§12). No coloured banners; severity is wording, not hue |
| Toast | **Refused.** Nothing in a yard pops up and vanishes. Confirmations are stamped copies that stay (§6.15) |
| Modal | **Refused.** A yard has no floating rooms. Extra information is another slab or a ticket drawer (below) |
| Drawer / disclosure | The "ticket drawer": a slab-edge panel that settles down 500ms `--ease-settle` under its ticket (FAQ drawers on the office page), one open at a time, content readable with JS off (JS arms the closed state) |
| Tabs | **Refused.** Beds are filtered by ticket stubs on the listing page (§7), which are links with state, not tab panels — the yard list itself re-files |
| Accordion | The ticket drawer (above), renamed by its material |
| Pagination | Ticket numbers as links ("TICKETS 13–24 OF 61") with prev/next as "EARLIER STONE / LATER STONE"; no page-number pills |
| Progress | The chalk line (§6.4) only; indeterminate progress is the unscored block (§6.16) |
| Spinner | **Refused.** Stone does not spin. Waiting is an unscored block or a stamped "STAMPING…" |
| Tooltip | **Refused.** Anything worth saying goes on a ticket in the layout. (Native `title` on the drill dot is also refused — its meaning is in §6.9's stamp line text) |
| Breadcrumbs | A ticket line: "YARD / BED 2 / TICKET 07" in mono at the detail slab's head — the numbering system is the breadcrumb |
| Search | On the listing page only: a ticket field that filters pieces by name/bed, results re-filed live, count stated in mono ("9 PIECES MATCH 'HEARTH'") |
| Price | Mono, always with its unit and basis ("£84 / M² SAWN") — a bare price is a claim (§3 law 1) |
| Empty state | A stated absence in the yard's voice (§12), e.g. §6.18's uncut block, §6.15's no-cores line |
| 404 | The uncut block (§6.18) |
| Footer | The pit floor (§6.17) |
| Print ticket | Every ticket and the spec table print black on white (§14) — yards run on paper copies |

## 12. Content & copywriting voice

Two registers. **The Yard** speaks in facts, measures and plain verbs —
short sentences, no adjectives that can't be weighed. **The Clerk** speaks
on tickets, forms and errors — courteous, exact, first person plural,
never apologetic in the corporate manner ("we are sorry for any
inconvenience" is banned; the clerk states the fact and the remedy).

**Headlines.** Names and acts, ≤26 characters for the hero (§8.1),
sentence case, Expanded. ✓ "Cut to your measure." ✓ "How a block is
read." ✗ "Premium bespoke stone solutions for discerning spaces." (Every
word untestable; the yard would not say it and could not prove it.)
✗ "ROCK SOLID DEALS!!!" (shouting, and a deal is not a measure.)

**Labels & tickets.** Mono uppercase, noun first, number where the record
has one. ✓ "TICKET Nº 04 — SAWN SLABS" ✓ "BED 2 — NORTH FACE" ✗ "Our
Products" (whose? where?) ✗ "Section 4" (a section is a web word; here
it is a ticket).

**Figures.** Always with unit and basis. ✓ "1,284 T EXTRACTED — SEASON
TO 21 NOV" ✓ "£84 / M² SAWN" ✗ "1,284 tonnes!" (mono record, no
exclamation — the theme bans exclamation marks in yard voice entirely;
a number that needs one isn't carrying its weight).

**Errors (clerk's voice).** State what won't carry and what to fix.
✓ "That direction will not carry — the part after the @ is wanting."
✓ "The second year is earlier than the first. One of them wants
correcting." (for date fields on the office page) ✗ "Oops! Something
went wrong." ✗ "Invalid input."

**Empty states.** ✓ "NO OFFCUTS THIS SEASON — THE BLOCK CUT CLEAN."
✓ "NO SLABS CORED YET — THE LIST FILLS AS YOU MARK THEM." ✗ "Nothing
here yet!" ✗ "Your cart is empty."

**Fixed strings (verbatim, do not paraphrase).** The scale line (§6.17):
"SCALE OF THIS PAGE: 1 CSS PX = 2 MM OF STONE". The cored stamp:
"CORED ✓ — ON YOUR LIST". The 404 ticket head: "THIS BLOCK HAS NOT BEEN
CUT". The form's promise: "The yard answers within one working day."
Banned words in yard voice: *premium, bespoke, stunning, amazing,
solution(s)* as a noun for stone, *leverage, synergy*, and any
superlative that cannot be measured ("finest", "best") — the yard says
"hardest" only with a Mohs figure attached.

## 13. Full-page scroll choreography map

The home page (§7), beat by beat. L = shared loop (lerp 0.10).

1. **Load.** Masthead settles 400ms → saw cut crosses the face 1200ms,
   letters dropping → standfirst → hero ticket stamps, hero callout
   draws (§8.1). Visitor sees a face being cut and ticketed.
2. **Hero scroll.** Texture parallax 0.92× (L), face photograph scales
   to rest (§6.8), dust drifting in its light (§6.5). Chalk line (§6.4)
   begins filling segment 01.
3. **First split.** Slab 02's pin: strain, parting to its declared gap,
   crumble at 0.55, ticket 02 revealed in the seam (§6.2). The block
   parts for the first time — the page's thesis, enacted.
4. **Yard slab.** Cards settle 90ms apart (§6.13); first card's callout
   draws; chalk fills segment 02, twang at the boundary.
5. **Process approach.** Slab 03's ticket; copy settles; chalk segment
   03.
6. **Process pin.** Core-drill diagram draws ring by ring in copy order
   (§6.6); ring↔copy highlighting available. The page slows down —
   deliberately; this is the thinking slab.
7. **Showcase pin.** The saw crosses the slab photograph; halves part
   6px (§8.2). Second and last pin of the descent's middle.
8. **Stats band.** Dark slab; figures strike up in stepped ticks
   (§6.7); the record date ticket stamps. Chalk segment 04 completes.
9. **Specification slab.** Ledger rules draw (§6.14); the visitor checks
   the record against everything above — the page invites its own audit.
10. **Form slab.** The slip settles on core-deep; the visitor's cored
    rows stagger in (§6.15). The descent ends in paperwork, as yard
    visits do.
11. **Footer.** Head rule draws; scale line, tally, index, offcuts
    (§6.17). The chalk line reaches its foot and stops — the survey is
    the page, complete.

Reverse pass: scrubbed values reverse (splits close, frames un-scale,
chalk retreats past the 1s ratchet grain); spent things stay spent
(crumble, counts, stamps, cores). Jump scroll lands every beat at its
position-true state (§6.2).

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤780KB | Photographs dominate; see below |
| Hero (all-in) | ≤220KB | §6.12 — photo ≤180KB, texture ≤8KB |
| Photographs | ≤180KB each, ≤4 per page | AVIF/WebP, square-on shots compress well; a 5th photo is a new slab's budget, argued at review |
| Inline SVG (all) | ≤40KB | Crack paths, frames, diagram, texture |
| JS | ≤60KB gz | The loop, measurement, cores, form — no framework needed for any of it |
| Fonts | ≤110KB | Archivo Expanded (2 weights, subset to Latin + figures), Archivo (3), Plex Mono (3) — subsetting is mandatory; full Archivo is a gate failure |
| Frame cost (shared loop) | ≤1.6ms/frame | With hero dust live + two scrubbed elements; measured on the reference device |
| Long tasks | none >50ms during scroll | Measurement reads are batched pre-write (§6.3) |
| CLS | 0.00 target | Slab min-heights (§6.16) and reserved figure widths (§6.7) exist to hold this |

**Cut order when over budget.** (1) Card tilt (§6.13). (2) Dust mote
count (§6.5) 30→14, then the dust entirely. (3) The showcase pin (§8.2)
becomes a static cut photograph. (4) Splitting pins (§6.2) reduce from
two pairs to one (face → yard survives; it is the thesis). (5) Photograph
count. **Never cut:** live measurement (§6.3), the chalk index (§6.4),
watchdogs and fallbacks, reduced-motion variants, the form's keeping of
input (§6.15). A faster page that lies about a dimension is worse than a
slow one (§1).

**Print.** Tickets, the spec table and the form's stamped copy print
black on white, grounds stripped, callouts at their last measured values
with the scale line — the yard's paper copy of the page, filed.

## 15. Build-order checklist

1. **`BLOCK` first.** The data object (§4) — slabs, pieces, yard record,
   process strata, offcuts — reviewed against the yard's real record.
   No layout exists before the record does.
2. **Static block.** All slabs stacked, tickets printed, headline
   engraved, form submittable, footer complete — with no JS. This is the
   page's truth; everything after is ceremony over it.
3. **Palette/type tokens.** §2/§3 as CSS variables, including the closed
   text pairings as utility classes so an illegal pairing is awkward to
   write.
4. **The shared loop.** rAF + lerp 0.10 + boundary events; nothing
   animates before the loop exists to govern it.
5. **Chalk rail & masthead** (§6.4, §6.11) — the numbering live early, so
   every later element is built against its ticket.
6. **Hero composition** (§6.12) static, then the **saw cut** (§6.1) with
   its 1600ms watchdog.
7. **Callouts** (§6.3) — measurement before any other decoration; the
   §10.1 audit runs from here on at every step.
8. **Cards + frames** (§6.13, §6.8); tilt last within the step.
9. **Splits** (§6.2) with snap-together fallback tested by loop stall.
10. **Diagram** (§6.6) generated from `BLOCK.process` alongside its copy.
11. **Counters** (§6.7) and the **table** (§6.14) from the same objects;
    three-printings diff (§10.2) wired as a build test.
12. **Cores** (§6.9) → **form** (§6.15) → footer list (§6.17): the
    conversion chain end to end, including the no-JS route.
13. **Dust** (§6.5) and **transition** (§6.10) — the two licensed
    luxuries, last, and first in the cut order (§14).
14. **Skeleton** (§6.16) min-heights audited against the real slabs.
15. **404** (§6.18) and the **gate** (§10) signed by a non-builder: the
    person who checks the ticket-truth audit did not write the callouts.
