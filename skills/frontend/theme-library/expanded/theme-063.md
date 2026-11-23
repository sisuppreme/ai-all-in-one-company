# 63. Sonar Room — Expanded (v1 + v2)

> A deep-sea survey vessel's sonar room, after midnight, mid-dive.
> The page is dark water and the reader is the operator: nothing on
> it is simply *shown* — everything is *sounded*. A beam sweeps a
> live scope in the hero and the headline phosphoresces where the
> beam crosses it. A hull gauge pinned to the left edge measures
> the reader's own scroll as a descent, 0 → 4,800 m, and the room
> obeys the physics of that depth: the ping interval lengthens,
> the pressure climbs, the light dies. Sections arrive the way
> returns arrive — dim, then sharp, then gone quiet. The page ends
> where every dive ends: on the seabed, charted, with one dashed
> segment where the signal honestly failed.

**The theme's one law: the room reports only what the water
returns.** Every figure printed anywhere on the page traces to
one declared record — Dive Sheet № 214 (§6.17) — and to nothing
else: the scope's five contacts are the sheet's five contacts,
the echogram's seabed is the sheet's Station 1, the footer's
profile is the sheet's seven stations, and the form's berth
number is the sheet's berth count plus one. What the water did
not return, the page does not invent: contact A4 has no depth
because its return carried none, the ghost contact is never
logged, and the weak segment of the seabed profile is drawn
dashed because the sheet says WEAK. A build that gives A4 a
depth, logs the ghost, rounds 84.2 to 84, or lets a readout and
its instrument disagree by one digit has broken the law — the
room's whole authority is that its numbers are the dive's
numbers, printed once and obeyed everywhere.

---

## 1. Concept & world

**The world.** A working sonar room on a survey vessel — not a
submarine film set, not a "dark mode dashboard with waves". One
operator, one watch, one dive in progress. The room's furniture
is instruments: a circular scope, a hull depth gauge riveted to
the left edge, an echogram console writing its waterfall, a log
of contacts the water has returned. The visitor is not browsing
a website; they have relieved the previous operator and the dive
is already under way. Every design decision in this theme is
answerable to one question: *would this exist in the room, and
would it behave the way the water makes it behave?*

**The dive is the page.** Scroll is descent, stated in metres on
a real instrument, and the page's total depth is the sheet's:
4,800 m from surface (hero) to seabed (footer). Sections are not
"content blocks"; each is a return received at a stated depth
along the way down — the log cards are sounded at ≈900 m, the
echogram console at ≈1,800 m, the sounding table at ≈2,600 m,
the counting soundings at ≈3,300 m, the berth form at ≈3,900 m.
The depth gauge, the ping interval, the pressure figure and the
background's darkness are four printings of one number — the
reader's scroll fraction × 4,800 — and §10's gate re-derives all
four from the sheet before the theme may ship.

**Mood.** Quiet, competent, slightly lonely. The room is dark
because the operator's night vision matters; the phosphor is
green because that is what the tube emits; the amber is spent
only where the water answered. Nothing in the room performs for
the visitor. The sweep keeps its period whether or not anyone
watches; the snow falls whether or not anyone scrolls. That
indifference is the luxury: a page that behaves like an
instrument underway, not a page auditioning.

**Best-fit sites and audiences.**

- Ocean-survey, subsea-inspection, offshore-robotics and
  hydrographic companies whose actual work is sounding,
  mapping and logging — the theme is their own room, and the
  log-card and sounding-table elements carry their real data
  shapes (range, bearing, depth, return character).
- Marine research institutes, aquarium deep-sea exhibits and
  ocean-documentary productions: audiences who will stay for a
  slow page because the slowness is the subject.
- Sonar, acoustic-modem, AUV/ROV and marine-instrument makers:
  the scope and echogram are product-shaped, and the theme's
  honesty rules (unidentified stays unidentified) read as
  engineering credibility to exactly the buyers who check.
- Any brand whose claim is *we go down and find out* — salvage,
  cable-route survey, wreck documentation, environmental
  baseline studies.

**When NOT to use it.**

- Anything that must be scanned in five seconds: a pricing
  page, a checkout, a signup funnel. The room's reveals are
  paced by a ping interval that lengthens to 6.0 s; a visitor
  in a hurry is a visitor in the wrong ocean. (§7 routes
  checkout out of the room entirely.)
- Bright, dense, catalogue-style content — product grids,
  news indexes, documentation with 40 links per viewport. The
  layout language (§4) budgets darkness as a material; density
  spends it all.
- Audiences on very low-end devices as the *only* experience:
  the canvas scope, snow and echogram are budgeted (§14) and
  cut in order, but a build that cannot hold the frame budget
  should choose another theme rather than a stuttering room.
- Any brand that needs the unknown resolved. This theme's
  signature honesty — A4 UNIDENTIFIED, the ghost unlogged, the
  weak return dashed — is a stance. A client who asks for the
  ghost to be "identified for engagement" has asked for a
  different theme.

**The five contacts are the cast.** A1 · WRECK (the found
thing), A5 · CABLE (the man-made line), A3 · SEAMOUNT (the
geology), A2 · VENT FIELD (the deep destination, at the
profile's Station 4 depth), A4 · UNIDENTIFIED (the honesty).
Every element in §6 is one of these, the water around them, or
the instruments that heard them. There is no sixth thing.

---

## 2. Palette

Five anchors from the original entry, kept exactly. The room is
a single-hue world — black-green water, one phosphor, one amber
— and the discipline is in the ratios: roughly 78% abyss, 12%
chart white and grey print, 7% phosphor, 3% amber. Amber above
5% of a viewport is a defect (§9): amber means *the water
answered*, and water does not answer everywhere at once.

| Token | Hex | Role | Usage | Contrast on `--abyss` |
|---|---|---|---|---|
| `--abyss` | `#06110E` | The water. Page ground, scope face, every unlit surface | ~78% of every viewport | — |
| `--phosphor` | `#57D9A3` | The beam and what it touches: sweep, rings, reveals, active readouts, focus | ~7% | 10.4:1 |
| `--amber` | `#E8B34B` | Returns only: contacts, heading origin dots, echogram trace, totals, the form's stamp | ~3% | 9.2:1 |
| `--pressure` | `#5C6B66` | Pressure grey: gauge furniture, ring lines, captions, table rules, disabled print | ~6% | 3.3:1 — **never body text** |
| `--chart` | `#E6EDE8` | Chart white: body text, headings at rest, log print | ~6% | 15.3:1 |

**Derived tokens** (computed from the anchors, never new hues):

| Token | Value | Derivation & use |
|---|---|---|
| `--abyss-2` | `#0A1A15` | Panel ground — console bezels, card faces, the form's ledger plate; one step of light above the water so a panel reads as *furniture in* the room, not a hole in it |
| `--abyss-3` | `#0E241C` | Raised panel / hover ground for cards and table rows |
| `--deep` | `#020604` | The vignette's end colour: the background lerps `--abyss` → `--deep` across the descent (§6.5); at 4,800 m the room is this dark and no darker |
| `--phosphor-dim` | `#2E7A5E` | The beam's trail at rest, headline glow floor, unlit-cluster dots in the loader; phosphor at ~45% luminance |
| `--phosphor-faint` | `rgba(87,217,163,0.14)` | Range-ring strokes, sweep afterglow wash, skeleton smudges |
| `--amber-deep` | `#9A742A` | Amber for print-sized marks on `--abyss-2`: origin dots at rest, the dashed weak-return segment, table total rules |
| `--grey-line` | `rgba(92,107,102,0.35)` | Hairlines: table rules, gauge ticks at minor interval, card borders |

**Pairing rules.**

- Body text is `--chart` on `--abyss` (15.3:1) or on `--abyss-2`
  (14.1:1). No exceptions, no grey body copy: in a dark room,
  dim text is not "elegant", it is an operator squinting.
- `--pressure` at 3.3:1 is furniture, not language. It may set
  tick labels, ring numbers, captions and disabled states —
  always at ≥11px, always beside a `--chart` or `--phosphor`
  element that carries the same information in words. A figure
  that exists *only* in pressure grey does not exist (§10 gate).
- `--phosphor` is the only colour allowed to glow. Glow is a
  box-shadow / text-shadow in the element's own colour at ≤40%
  alpha; amber never glows except a contact at the instant the
  beam strikes it (§6.1), and chart white never glows at all —
  print does not shine.
- Amber is rationed by the **amber census**: per viewport, amber
  may appear as (a) struck contacts, (b) heading origin dots,
  (c) one totals row or stamp. The echogram's trace is the one
  licensed exception — it is an instrument, not decoration.
- Dark-mode behaviour: the theme *is* dark; there is no light
  variant and none is offered. Under `prefers-contrast: more`,
  `--pressure` lifts to `#7E8F89` (4.6:1) for furniture and the
  vignette's lerp is halved so print contrast never drops.

---

## 3. Typography

Two families, kept from the original entry, with a hard border
between them: **Space Grotesk** speaks (headlines, body, the
room's voice); **JetBrains Mono** measures (depth, bearing,
range, pressure, interval, the log's figures). A number set in
Space Grotesk is a defect; a sentence set in JetBrains Mono
outside a readout or log line is a defect. The border is the
theme's typographic law, and §10 greps for it.

| Role | Font | Size / line-height / tracking | Notes |
|---|---|---|---|
| Display (hero headline) | Space Grotesk 500 | clamp(2.75rem, 7.2vw, 5.25rem) / 1.02 / −0.02em | The phosphor headline (§6.2); sentence case, never all-caps — the room does not shout |
| H2 (section headings) | Space Grotesk 500 | clamp(1.75rem, 3.4vw, 2.5rem) / 1.08 / −0.015em | Carries the amber origin dot (§6.7); heading text is `--chart`, the dot is the only amber |
| H3 (card & console titles) | Space Grotesk 500 | 1.125rem / 1.25 / −0.01em | Contact names, station names |
| Body | Space Grotesk 400 | 1.0625rem / 1.65 / 0 | Measure 34–44rem; the room's prose voice (§12) |
| Lead / standfirst | Space Grotesk 400 | 1.3125rem / 1.5 / 0 | One per page, in the hero only |
| Readout XL (depth) | JetBrains Mono 500 | clamp(2rem, 4.6vw, 3.25rem) / 1 / 0.01em | Tabular figures; the gauge's depth (§6.3) |
| Readout (data voice) | JetBrains Mono 400/500 | 0.8125rem / 1.5 / 0.04em | Bearings, ranges, intervals, log lines; uppercase for labels only (`BRG 038°`) |
| Caption / tick label | JetBrains Mono 400 | 0.6875rem / 1.4 / 0.06em | `--pressure`, ≥11px, never the sole carrier of a figure (§2) |
| Table figures | JetBrains Mono 400 | 0.875rem / 1.55 | Right-aligned, tabular; totals in `--amber` (§6.14) |

**Type laws.**

1. **Numerals are always mono.** Any digit in the DOM belongs to
   JetBrains Mono — readouts, tables, counters, the form's berth
   number, the footer's sheet line. Space Grotesk's proportional
   figures would make a counting readout wobble horizontally;
   in this room, a wobbling digit reads as a broken instrument.
2. **The unit is part of the number.** `4,800 M`, `2,624.7 FM`,
   `481 BAR`, `BRG 038°`, `RNG 1,240 M` — a bare figure is an
   unfinished reading. Units set in the same mono, one space
   after the figure, never superscripted, never shrunk.
3. **Bearings are three digits, always.** `038°`, never `38°`.
   Ranges take a thousands comma (`1,240 M`). Depths on the
   gauge take a comma from 1,000 up (`4,800 M`) and one decimal
   in fathoms (`2,624.7 FM`) because the sheet states it so.
4. **Headlines are statements, not slogans.** Sentence case,
   full stop optional, no exclamation anywhere on the page —
   the room has no exclamation register (§12). The one licensed
   all-caps is the mono label voice (`RETURN STRONG`,
   `UNIDENTIFIED`), which is instrument print, not shouting.
5. **The log voice is past tense and third person.** Log lines
   record what the water did: "Contact A4 held at long range.
   No depth return." — never "We found something exciting!"

**Scale behaviour.** Display type is fluid between 375px and
1440px viewports and frozen outside that band; readout XL never
shrinks below 2rem (the gauge is an instrument, and an
instrument that gets smaller on a small screen gets its own
layout instead — §6.3's breakpoints). Line-height tightens one
step (1.65 → 1.6 body) below 768px where the measure narrows.

---

## 4. Layout language

**The room plan.** The page is a vertical shaft of water with
furniture fixed to its walls. A 72px instrument rail — the
pinned depth gauge (§6.3) — occupies the left edge from below
the masthead to the seabed, on every page, at every scroll
position. Content lives in a single column to its right,
max-width 76rem including the rail, with the reading measure
(§3) left-aligned inside it: text hugs the instrument wall the
way a logbook hugs the console. Full-bleed is reserved for the
two instruments that *are* rooms: the scope hero (§6.1) and the
echogram console (§6.8), which span the content column entire.

**Grid.** 12 columns at ≥1200px inside the content area; the
log-card grid (§6.9) runs 3-up, the sounding table (§6.14) runs
full measure, the form (§6.15) runs a 7/5 split (fields / the
sheet's berth ledger). At 768–1199px the grid is 8 columns and
cards run 2-up; below 768px it is 4 columns, cards 1-up, and the
gauge rail leaves the edge to become a surface bar (§6.3) — the
room rearranges its furniture, it does not crush it.

**Spacing rhythm.** A 4px base unit; section gaps are depth
gaps — 9rem (144px) of open water between sounded sections at
desktop, 6rem at tablet, 4.5rem on mobile. The gap is not empty:
marine snow (§6.12) crosses it and the depth tape fills through
it, so the reader *descends through* the spacing. Within a
section, 2rem between heading and first element, 1rem inside
cards. Whitespace in this theme is water: it has a medium in it
(snow), a direction (down), and a cost (depth) — §9 lists
"empty black sections with nothing in them" as a failure mode.

**Density rules.** One instrument per viewport, one idea per
section, one amber event per viewport (§2's census). A section
that contains a canvas (scope, echogram) contains no second
animated element larger than a heading ring. Cards cap at six
per grid (the sheet's five contacts plus, on listing pages, one
chart-request card — never a seventh invented contact).

**Section choreography (page level).** Every section is
"sounded" in the same order: the heading's origin dot pings
(§6.7), the heading sharpens, the section's elements return in
range order — nearest first, farthest last — exactly as echoes
arrive. The full beat-by-beat map is §13; the per-element specs
are §6. Reverse scroll replays nothing: what has been sounded
stays sounded (§6.6's latch rule) — the dive does not un-happen
on the way back up, though the gauge honestly re-ascends.

**The seabed rule.** Every page type ends on its bottom: the
home page on the profile chart (§6.11), listing pages on a
sounded "end of transect" line, the 404 on uncharted water
(§6.18). A page that ends mid-water — footer floating over the
same darkness as the hero — has not finished its dive.

---

## 5. Full motion system

One shared requestAnimationFrame loop drives every scroll-scrubbed
and time-based value in the room: the lerped scroll position, the
beam angle, the snow, the echogram's write head, the gauge. There
is no second loop, no CSS animation on a scrubbed value, no
`setInterval` choreography. The loop's lerp factor is **0.085**
(the "heavy-water" constant: the room answers the scroll the way
water answers a hull — promptly, but with mass). All durations
below are the room's own; easings are named for what they imitate.

**Named easings.**

| Token | Curve | Imitates | Used by |
|---|---|---|---|
| `--ease-sweep` | `linear` | The beam's constant rotation — a motor, not a gesture | Scope beam (§6.1) |
| `--ease-decay` | `cubic-bezier(0.12, 0.61, 0.19, 1)` front-loaded, long tail | Phosphor afterglow dying exponentially | Headline glow (§6.2), trail, contact decay (§6.1) |
| `--ease-sound` | `cubic-bezier(0.22, 0.9, 0.28, 1)` | A ping ring leaving the transducer — fast birth, long travel | Ping rings (§6.6, §6.7), click return (§6.6) |
| `--ease-settle` | `cubic-bezier(0.33, 1, 0.42, 1)` | A return sharpening and holding | Reveals (§6.6), card arrivals (§6.9), loader sharpen (§6.16) |
| `--ease-tumble` | `steps(9, end)` over 540ms | A mechanical counter's digit drum | Unit flip (§6.3), counting soundings (§6.10) |

**The depth functions (the room's physics — all from §6.17).**
Every scrubbed instrument reads the same lerped depth
`d` (0 → 4,800 m, = scroll fraction × 4,800):

- **Ping interval** `I(d) = 2.4 + 3.6 × (d / 4800)` seconds —
  2.4 s at the surface, 4.2 s at 2,400 m, 6.0 s on the bottom.
  Sound travels ~1,500 m/s; a longer range is a longer wait, and
  the room waits honestly (§6.4).
- **Beam period** `B(d) = 6.5 + 4.5 × (d / 4800)` seconds —
  6.5 s → 11 s. The scope slows as the water deepens (§6.1).
- **Pressure** `P(d) = 1 + d / 10` BAR — 1 BAR at the surface,
  481 BAR on the bottom (§6.5).
- **Unit flip** at `d = 1,000`: the depth readout changes from
  metres to fathoms (`FM = M / 1.8288`; 4,800 m = 2,624.7 fm)
  with the tumbling-digit change (§6.3).
- **Vignette** closes and the ground lerps `--abyss` → `--deep`
  across the full descent (§6.5).

**Motion-term translation table** — every standard term, in this
room's language or refused with its reason:

| Term | In Sonar Room |
|---|---|
| Scroll-triggered reveals | Ping reveals (§6.6): sections sharpen as an expanding ring passes, fired at mid-viewport |
| Scroll-driven / scrub animation | The descent itself: gauge, interval, pressure, vignette, background lerp — all scrubbed from the one lerped depth |
| Parallax | Marine snow at three depths + one near blurred layer (§6.12); content layers never parallax against their own text |
| Pinned sections | The depth gauge is pinned for the whole dive (§6.3); the scope stage pins for its first 40vh on tall viewports |
| Smooth scrolling | The rAF lerp at 0.085 *is* the smoothing; native scroll is never hijacked — the wheel stays the reader's |
| Progress indicator | The depth tape filling downward on the gauge (§6.3). A top progress bar is refused: the room already has an instrument for this |
| Staggered reveals | Returns arrive in range order, nearest first (§6.9); stagger interval derives from the ping interval, not a fixed 80ms |
| Masked line reveals | Refused. Text is not unmasked in a sonar room; it is *sounded* — blur-to-sharp under a passing ring (§6.6) is the room's equivalent |
| Kinetic typography | Refused. Type does not dance in an instrument room; digits tumble (§6.3) because counters do, and that is the only moving type |
| Marquee | Refused. Nothing scrolls sideways in the room. The one horizontal writer is the echogram (§6.8), which is an instrument trace, not a ticker |
| Counters | Counting soundings (§6.10): digit-by-digit with a mechanical tick, each figure stopping dead at the sheet's value |
| SVG line-draw | The seabed profile (§6.11) draws itself station by station; the weak segment draws dashed because the sheet says so |
| Image scale-in-frame | Plates and stills arrive as echo smudges that sharpen (§6.16's loader language applied to images) — no Ken Burns, no zoom |
| Hover micro-interactions | Soft ping on hover (§6.6), console-tilt on cards at max 3° (§6.9) |
| Magnetic / tilt | Tilt only, max 3°, lerped — a console screen catching light. Magnetic pull is refused: instruments are bolted down |
| Custom cursor | **Refused.** Normal system cursor only — an operator's pointer is a tool, not a firefly (§10 gate greps for it) |
| Skeleton loading | Faint echo smudges that sharpen (§6.16) — the room has no grey boxes; unloaded water is just water not yet sounded |
| Page transitions | A full sweep crosses the room; new content phosphoresces behind the beam (§6.16), watchdog-capped at 2,000ms |
| Reduced motion | The room lit: all content at rest and fully visible, sweep/decay/snow off, gauge still scrubs (it is information, not decoration) — specified per element in §6 |

**Ambient loops — exactly two licensed.** (1) The scope sweep
with its phosphor trail (§6.1). (2) The marine snow (§6.12).
The echogram's write (§6.8) is an instrument doing its job, not
an ambience, and is counted separately in §14's budget. Any
fourth always-on motion is a defect. Everything else in the room
moves because the reader scrolled, hovered, clicked or waited
for a ping the depth had already scheduled.

**Watchdog law.** Every JS-armed pre-state carries two timeouts
from the original entry — **2.6 s and 6 s** — after which the
element is forced to its fully visible rest state, script or no
script. The DOM ships complete and legible; scripts only ever
*dim* what is already printed, and only after they have armed
successfully. A reveal that can strand content is not a reveal,
it is a bug with a duration.

---

## 6. Signature elements

### 6.1 Live sonar scope

- **What & why.** The hero is the vessel's scope, live: a circular
  canvas instrument, range rings out to 5,000 m, a rotating beam
  with a decaying phosphor trail, and the sheet's five fixed
  contacts at their true bearings and ranges. It belongs because
  it is the room's reason to exist — the instrument the whole
  page is built around — and because it teaches the visitor the
  theme's grammar in the first three seconds: things appear when
  the beam reaches them, glow, and decay. Nothing else on the
  page needs that explained again.
- **Structure.** One `<canvas>` (square, min(78vh, 92vw) capped at
  760px) centred in the hero, drawn entirely in 2D canvas: rings
  and bearing spokes in `--grey-line`, the beam as a conic wedge
  filled with a `--phosphor` gradient (alpha 0.20 at the leading
  edge → 0 at −50°), contacts as 5px dots positioned by polar
  conversion of the sheet's bearing/range pairs (range scaled
  logarithmically, `r = R × log(1 + rng/500) / log(11)`, so the
  890 m cable and the 4,410 m unknown are both legible). Contact
  labels are DOM, not canvas — absolutely positioned mono chips
  (`A1 · WRECK`) beside each dot, so they are selectable,
  searchable and screen-readable. The headline (§6.2) sits inside
  the scope's lower-left quadrant as DOM over the canvas. A DOM
  fallback list of the five contacts renders beneath the canvas
  for no-JS and is visually hidden only when the canvas arms.
- **Motion spec.** Beam rotates at `--ease-sweep` (linear),
  period `B(d) = 6.5 + 4.5 × (d/4800)` s (§5): 6.5 s in the hero,
  lengthening as the reader descends. The trail decays behind
  the beam over ~1.2 s (`--ease-decay` applied as a per-frame
  alpha fade of the wedge's trailing gradient stops). When the
  beam's bearing crosses a contact's bearing (±2.5° window), the
  contact strikes: dot flashes `--amber` at full brightness,
  emits one expanding ring (`--ease-sound`, 1,600ms, radius 6 →
  46px, alpha 0.9 → 0), its label chip brightens to `--chart`,
  then all decay over 2,400ms (`--ease-decay`) to the contact's
  rest state — a `--phosphor-dim` dot at 55% and a `--pressure`
  label. Contacts never strike out of turn; the beam is the only
  clock.
- **States.** Rest (between strikes): contacts dim, beam turning,
  rings still. Struck: as above, 2,400ms decay. Hover on a
  contact chip: the dot brightens to `--phosphor` and the chip
  shows the contact's full sheet line (range, bearing, depth or
  NO RETURN) — the scope answers a pointed question. Focus (chips
  are real links to §6.9's cards): same brightening plus the
  standard 2px `--phosphor` outline. Scrolled-past: the scope
  keeps sweeping (it is the room's clock) but its strike rings
  are suppressed once the hero is 80% out of view — no amber
  events the reader cannot see. Disabled: canvas unsupported →
  the DOM fallback list is the element (§ below).
- **Content merge.** The scope's contacts *are* the page's
  content, pre-announced: each chip links to that contact's log
  card (§6.9), the headline sits inside the sweep (§6.2), and the
  sheet's figures (ranges to 5,000 m ring) are the instrument's
  own scale. Remove the page's subject and the scope has nothing
  to strike; remove the scope and the cards lose their origin.
- **Failure fallback.** Watchdogs: if the canvas context fails or
  the rAF loop has not ticked within 1,200ms of arming, the
  canvas is removed and the DOM contact list (always in the
  markup, fully printed) becomes visible — the hero degrades to
  a chart of the five contacts with the headline above it, all
  legible. No JS: identical fallback, from first paint. Content
  is never inside the canvas; the canvas is an instrument *over*
  a printed chart.
- **Reduced-motion variant.** Beam parked at 038° (A1's bearing —
  the wreck, the found thing, lit first), all five contacts at
  rest brightness with labels fully printed, no trail, no strike
  rings, no decay. The scope reads as a chart on the wall:
  complete, still, legible.
- **Performance budget & mobile variant.** Canvas redraw is one
  full repaint per frame at devicePixelRatio capped at 1.5;
  measured cost ≤0.9ms/frame on a mid-tier laptop (§14). Snow
  (§6.12) shares the same canvas pass. Mobile (<768px): scope
  diameter 92vw, DPR capped at 1.25, trail shortened to 0.8 s,
  strike rings capped at 2 concurrent, and the beam period
  floored at 8 s so the smaller tube never hurries.
- **Choreography timeline (v2).** Page load → t=0 room black,
  headline printed dim → t=300ms beam fades in at bearing 000° →
  first revolution at 6.5 s: t≈690ms beam crosses 038°, A1
  strikes (flash + ring + label) → t≈2,180ms crosses 121°, A2
  strikes → t≈3,680ms crosses 204°, A3 strikes → t≈5,180ms
  crosses 287°, A4 strikes dimmer (its return is weak — flash at
  60% alpha, no ring beyond 30px) → t≈5,810ms crosses 322°, A5
  strikes → revolution completes, all contacts decayed to rest →
  cycle repeats at the depth's current period.
- **State matrix (v2).** *Rest:* beam turning, contacts dim.
  *Hover (chip):* dot to phosphor, full sheet line shown.
  *Focus (chip):* as hover + outline. *Active (chip pressed):*
  one hard ping (§6.6's click return) at the contact, then
  navigation to its card. *Scrolled-past:* sweep continues,
  strikes muted past 80% out of view. *Disabled (no canvas):*
  printed chart list. *Touch:* chips are 44px targets; a tap is
  the active state — no hover preview is required to reach any
  information, since labels print range and name at rest.
- **Breakpoints (v2).** ≥1200px: scope 760px, headline inside the
  sweep, chips outside the rim. 768–1199px: scope min(70vh,
  88vw), chips inside the rim at the contact's bearing. <768px:
  scope 92vw, headline moves *below* the scope (the tube is too
  small to hold type honestly), chips become a printed list
  under the canvas — the mobile scope is an instrument with a
  log beneath it, not a shrunken poster.
- **Edge cases & failure modes (v2).** *Tab hidden mid-sweep:*
  rAF pauses; on return the beam resumes from its parked angle —
  no catch-up strikes, no burst of rings. *Reader scrolls fast
  to the bottom:* period lengthens toward 11 s via the lerped
  depth — the beam never spins up to chase the scroll. *Contact
  at the rim (A4, 4,410 m):* drawn at 88% radius on the log
  scale; its strike ring clips at the rim, which is correct —
  the scope's edge is a real limit. *Ghost contact (§6.12)*
  enters this canvas only, at 5,600 m — beyond the outer ring —
  drawn half-clipped at the rim.
- **Accessibility spec (v2).** The canvas is `aria-hidden`; the
  five chips are real `<a>` elements with accessible names
  carrying the full sheet line ("Contact A1, wreck, range 1,240
  metres, bearing 038, depth 212 metres"). Focus order: headline
  → chips in contact order A1–A5 → hero body links. Contact
  information never exists only as a canvas flash: every strike's
  data is in the chip text and in §6.9's cards. Strike flashes
  are single dots ≤6px brightening — far below any photosensitive
  threshold, and §10 audits flash area.
- **Tokens consumed (v2).** `--abyss`, `--phosphor`,
  `--phosphor-dim`, `--phosphor-faint`, `--amber`, `--pressure`,
  `--chart`, `--grey-line`, `--ease-sweep`, `--ease-decay`,
  `--ease-sound`, `--dur-beam-base` (6.5s), `--dur-trail` (1.2s),
  `--dur-strike-decay` (2400ms).

### 6.2 Phosphor headline

- **What & why.** The hero headline is a contact on its own
  scope: a `--chart` text layer with a `--phosphor` glow layer
  behind it that lights as the beam crosses the headline's
  bearing and decays exponentially between passes, resting at a
  dim but fully legible 55%. It belongs because it makes the
  brand's name obey the room's law — discovered by the sweep,
  not displayed — and it is the visitor's first proof that the
  page's physics are real: the glow's timing *is* the beam's
  position, not a looping CSS shimmer.
- **Structure.** A single `<h1>` with two stacked spans: the
  print layer (`--chart`, always fully opaque) and a glow layer
  (`aria-hidden`, same text, `--phosphor`, blurred 18px,
  `mix-blend-mode: screen`) whose opacity is written per frame
  by the shared loop from the beam angle. The headline sits at a
  declared bearing — 205°, lower-left of the scope — and that
  bearing is a build constant shared with §6.1, so glow and beam
  can never disagree.
- **Motion spec.** As the beam's bearing approaches 205°, glow
  opacity ramps 0 → 0.85 across the 50° before crossing
  (`--ease-decay` curve inverted); at crossing it peaks, then
  decays exponentially with a 1.9 s half-life to the 0.18 floor
  (≈55% perceived brightness over the print layer) until the
  next revolution. Revolution period is `B(d)` (§5), so the
  headline's pulse slows as the reader descends — the title
  itself breathes at the depth's rate.
- **States.** Rest: print layer at full opacity, glow at floor —
  always readable, never dependent on the beam. Lit: glow peak
  at beam crossing. Hover: none — the headline is not a control
  and does not respond to the pointer (instruments ignore
  fingers). Scrolled-past: once the hero leaves the viewport the
  glow layer is frozen at floor and dropped from the frame
  budget. Disabled (no JS): glow layer absent, print layer is
  the headline, complete.
- **Content merge.** The glow is not decoration on the title; it
  is the title being *sounded*, on the same clock as every
  contact strike. The headline's bearing (205°) sits 1° off
  A3's bearing (204°) — deliberate: the beam strikes the
  seamount with the headline's glow already rising toward its
  peak 1° later, so mountain and name sound in the same breath
  of the same pass, and the hero's
  first revolution reads as a sentence: beam, mountain, name.
- **Failure fallback.** The print layer ships in the DOM at full
  opacity; the glow layer is added by script only after the loop
  is running. Watchdog: if the loop stalls, the glow freezes —
  the headline's legibility never depended on it. There is no
  state of this element in which the title is invisible.
- **Reduced-motion variant.** Glow layer removed entirely. The
  headline is plain `--chart` print — which is its rest state
  anyway, so the reduced page loses an effect and nothing else.
- **Performance budget & mobile variant.** One opacity write per
  frame on one element; negligible. The blur is a static filter
  on the glow layer (compositor-cached), never re-rasterised per
  frame. Mobile: blur radius 12px, glow peak 0.7 — smaller tube,
  dimmer bloom.
- **Choreography timeline (v2).** Beam at 155° → glow begins its
  ramp → beam at 205° → glow peaks 0.85 → +1.9 s glow at ~0.51 →
  +3.8 s at ~0.30 → +5.7 s at floor 0.18 → next revolution
  repeats, at the period the current depth sets.
- **State matrix (v2).** *Rest:* print full, glow floor. *Hover:*
  none (not a control). *Focus:* the h1 is not focusable; skip
  link targets land above it. *Active:* n/a. *Scrolled-past:*
  glow frozen at floor, cost removed. *Disabled:* print only.
  *Touch:* identical to desktop — the effect is time-driven, not
  pointer-driven.
- **Breakpoints (v2).** ≥1200px and 768–1199px: headline inside
  the scope at bearing 205°, glow as specified. <768px: headline
  below the scope (§6.1), glow layer still beam-synced — the
  beam's period is read from the same loop, so a headline
  outside the tube still lights when the beam crosses 205°; the
  fiction holds because the room, not the tube, is what sweeps.
- **Edge cases & failure modes (v2).** *Beam period at maximum
  (11 s):* the glow spends ~7 s near floor between passes — by
  design; the floor is legible print, not a loading state.
  *Headline wraps to three lines on a narrow scope:* the glow
  layer wraps identically (same text, same box) — a mismatch
  here is a §10 failure. *Font swap late (FOUT):* the glow layer
  uses the same font stack and is hidden until `document.fonts`
  resolves or 900ms passes, whichever first — the two layers
  never show different faces.
- **Accessibility spec (v2).** One real `<h1>`; the glow duplicate
  is `aria-hidden` and `user-select: none`. Contrast of the
  print layer is 15.3:1 at every moment of the cycle — the glow
  only ever adds light behind already-legible text. Screen
  readers encounter the headline once, as text.
- **Tokens consumed (v2).** `--chart`, `--phosphor`, `--ease-decay`,
  `--headline-bearing` (205°), `--glow-peak` (0.85),
  `--glow-floor` (0.18), `--dur-glow-half-life` (1.9s).

### 6.3 Pinned depth gauge

- **What & why.** A hull instrument fixed to the left edge for
  the whole dive: the big mono depth readout, the unit that
  flips from metres to fathoms past 1,000 m with a tumbling-digit
  change, and the vertical depth tape that fills downward with
  true tick labels. It belongs because it is the page's contract
  with the reader — *your scroll is a descent, and here is its
  measure* — and because every other depth-driven behaviour in
  the room (interval, pressure, darkness) is visibly *read off
  this instrument*, so the reader trusts them as one system.
- **Structure.** A `<aside>` rail, 72px wide, `position: fixed`
  left, full height below the masthead, on `--abyss-2` with a
  `--grey-line` right border and two printed "rivet" dots (CSS)
  at top and bottom corners — hull furniture, stated once and
  never animated. Inside, top to bottom: the depth readout
  (readout XL, §3) stacked as figure over unit; the depth tape —
  a 2px vertical track with a `--phosphor` fill whose height is
  the scroll fraction, tick labels at 0 / 1,000 / 2,000 / 3,000 /
  4,000 / 4,800 m in caption mono, rotated 0° and right-aligned
  to the rail; below the tape, the secondary readouts (§6.4,
  §6.5) mount in the same rail. The readout is DOM text, updated
  by the loop — never canvas.
- **Motion spec.** Depth value = lerped scroll fraction × 4,800,
  written to the readout each frame the value changes by ≥0.5 m
  (the readout never flickers sub-metre noise). Tape fill height
  is the same fraction, compositor-transformed (`scaleY` on the
  fill, origin top). **The unit flip:** at `d` crossing 1,000 m
  (either direction), the figure re-renders in the other unit
  with a tumbling-digit change — each digit position rolls
  through 9 glyphs over 540ms, `--ease-tumble`, staggered 40ms
  per position from the left, the unit label crossfading
  `M` → `FM` at the roll's midpoint. In fathoms the figure is
  `M / 1.8288` to one decimal: the bottom reads `2,624.7 FM`.
  The flip is a *change of instrument scale*, announced as such
  (§ below), not a glitch effect.
- **States.** Rest (surface): `0 M`, tape empty, ticks printed.
  Descending: figure and fill track the lerp. At the flip:
  tumbling, then fathoms. On the bottom (fraction 1): `2,624.7
  FM`, tape full, the 4,800 tick lit `--phosphor`. Ascending
  (scroll up): everything reverses honestly — the gauge is a
  measurement, not a latch; only §6.6's reveals latch. Hover:
  none (not a control). Disabled (no JS): the gauge prints its
  surface state `0 M` with a full printed tick scale — a chart
  of the dive's depth, still truthful as far as it goes.
- **Content merge.** The gauge measures the page itself: its
  4,800 m is the sheet's dive depth, its ticks are the depths at
  which the page's sections are sounded (§13's map prints the
  same figures), and its value is the single input to §6.4's
  interval, §6.5's pressure and the background lerp. It is not a
  progress widget wearing a costume; it is the room's master
  instrument, and three other elements cite it.
- **Failure fallback.** If the loop dies, the gauge freezes at
  its last true reading — a stopped instrument, still printed,
  never blank. Watchdog at 6 s: if no scroll event has ever
  fired (a reader who lands and reads the hero without
  scrolling), the gauge simply holds `0 M`, which is *correct*.
  No JS: static printed scale as above; the page loses its
  descent meter and nothing else.
- **Reduced-motion variant.** The readout still updates (it is
  information), but the tumbling flip is replaced by an instant
  unit change with a 200ms crossfade, and the tape fill jumps in
  100 m steps rather than gliding — measurement without theatre.
- **Performance budget & mobile variant.** One text write + one
  transform per frame worst case; ≤0.1ms. Mobile (<768px): the
  rail un-pins and becomes a surface bar fixed to the top under
  the masthead — depth readout left, a horizontal tape (the
  same fill, rotated into a 2px bar) centre, pressure right —
  44px tall, so the dive's measure survives the rearrangement
  (§4). The tumbling flip is kept; it is the gauge's signature.
- **Choreography timeline (v2).** First scroll → lerp engages →
  readout leaves 0 within 120ms of the gesture → tape fill
  follows at the same lerp → at fraction 0.2083 (1,000 m):
  digits tumble 540ms, unit crossfades at 270ms → fathoms for
  the rest of the descent → fraction 1.0: bottom state, 4,800
  tick lit → scroll up: fathoms until 1,000 m, reverse tumble,
  metres to the surface.
- **State matrix (v2).** *Rest:* `0 M`, tape empty. *Hover:*
  none. *Focus:* the gauge is not focusable; its values are
  mirrored in each section's printed depth label for readers who
  never look at the rail. *Active:* n/a. *Scrolled-past:* n/a —
  it is fixed; it is never past. *Disabled:* printed static
  scale. *Touch:* the surface-bar variant; values identical,
  tape horizontal.
- **Breakpoints (v2).** ≥1200px: 72px rail, readout XL full size,
  all six tick labels. 768–1199px: rail narrows to 60px, readout
  XL at 2rem floor, minor ticks (1,000/3,000) drop their labels
  (ticks remain). <768px: surface bar as above; tick labels
  reduced to 0 and 4,800 only.
- **Edge cases & failure modes (v2).** *Very tall page zoomed
  out / short page:* fraction is computed from real scrollable
  height, so the bottom is always 4,800 m at the true page end —
  the instrument measures *this* page, and §10 verifies the
  bottom state at the footer. *Reader resizes mid-dive:*
  fraction recomputes; no tumble is triggered by resize alone
  (the flip fires only on a threshold *crossing by scroll*).
  *Print:* the gauge prints once, at the surface state, beside
  the first page — print has no descent.
- **Accessibility spec (v2).** The live readout is
  `aria-hidden` (a per-frame changing number is noise to a
  screen reader); instead, each section carries a visually
  hidden + printed depth label ("Section sounded at 1,800
  metres") in the accessibility tree, and the gauge's static
  tick scale is real text. The unit flip is announced via a
  polite live region that speaks only on the flip itself:
  "Depth now in fathoms." Touch targets: the gauge has none —
  it is an instrument, not a control, and nothing in it is
  tappable.
- **Tokens consumed (v2).** `--abyss-2`, `--phosphor`,
  `--pressure`, `--chart`, `--grey-line`, `--ease-tumble`,
  `--dur-tumble` (540ms), `--depth-max` (4800), `--flip-depth`
  (1000), `--fm-per-m` (1.8288), `--loop-lerp` (0.085).

---

### 6.4 Ping-interval readout

- **What & why.** Beside the gauge, a small mono readout —
  `PING 2.4 S` — whose value lengthens from 2.4 s to 6.0 s as
  depth increases, and which is not a display *about* the room's
  rhythm: it *is* the room's rhythm. The heading rings (§6.7)
  fire on this interval; the reveals (§6.6) are gated by it.
  It belongs because it is the theme's honesty made visible —
  real sonar waits longer at longer range, and a room whose
  pings never slowed would be lying about the water.
- **Structure.** A two-line block in the gauge rail under the
  depth tape: label `PING` in caption mono (`--pressure`) over
  the value in readout mono (`--chart`), e.g. `4.2 S`. Pure DOM
  text, updated by the shared loop from the same lerped depth as
  §6.3. Directly beneath it, a 24px "interval bar": a hairline
  track on which a single phosphor dot travels left-to-right
  across exactly one interval and resets — the wait, drawn.
- **Motion spec.** Value = `I(d) = 2.4 + 3.6 × (d/4800)`,
  rendered to one decimal, updated when it changes by ≥0.1 s.
  The interval bar's dot traverses in real time at the current
  interval; when the interval changes mid-traverse (reader
  scrolling), the dot's speed re-scales smoothly over 300ms —
  the bar never jumps. At each completed interval the loop
  emits the room's ping event: heading rings (§6.7) fire, and
  any pending reveal (§6.6) whose section is in position is
  released. The ping is an event in the system, not a visual
  loop pasted over it.
- **States.** Rest (surface): `PING 2.4 S`, dot cycling at 2.4 s.
  Deep: value climbs to `6.0 S` on the bottom. Hover: none.
  Focus: none (not a control). Scrolled-past: n/a (rail is
  fixed). Disabled (no JS): prints `PING — S` with the label;
  the sheet's surface value is *not* printed as if live — an
  instrument that cannot measure says so (§ below).
- **Content merge.** This readout is the merge: the number and
  the behaviour are one object. §6.7's rings, §6.6's reveal
  gating and this figure all read `I(d)`; change the depth and
  all three change together, which §10's gate verifies by
  sampling at 0 m, 2,400 m and 4,800 m (2.4 / 4.2 / 6.0 s).
- **Failure fallback.** If the loop stalls, the readout freezes
  at its last true value and the dot stops — a stopped clock in
  a room whose other instruments (§6.3) have also stopped; the
  page's content is unaffected because reveals carry their own
  watchdogs (§6.6) and never *depend* on the ping to eventually
  appear. No JS: the em-dash state above; nothing on the page
  waits for a ping that cannot come.
- **Reduced-motion variant.** The value still updates (it is
  data); the travelling dot is removed and replaced by a static
  bar whose *length* encodes the interval against a 6 s scale —
  the wait is shown, not performed.
- **Performance budget & mobile variant.** Negligible: one text
  write on change, one transform on the dot. Mobile: the readout
  moves into the surface bar (§6.3) as a compact `PING 4.2 S`
  chip at the bar's right end; the interval bar is cut (the
  bar has no room for a drawn wait, and the rings still fire on
  the true interval).
- **Choreography timeline (v2).** Depth changes → value re-renders
  within one frame of a 0.1 s change → dot re-scales speed over
  300ms → interval completes → ping event: rings fire (§6.7),
  pending reveals release (§6.6) → next interval begins at the
  depth's current value.
- **State matrix (v2).** *Rest:* surface value 2.4 s. *Hover:*
  none. *Focus:* none. *Active:* n/a. *Scrolled-past:* n/a
  (fixed rail). *Disabled:* em-dash print. *Touch:* chip variant
  in the surface bar; the interval still governs the room.
- **Breakpoints (v2).** ≥1200px: two-line block + interval bar in
  the rail. 768–1199px: value only (bar cut — the rail is 60px
  and the bar would crowd the tape). <768px: surface-bar chip,
  no bar.
- **Edge cases & failure modes (v2).** *Reader parked at one
  depth reading for minutes:* the ping keeps firing at that
  depth's interval indefinitely — correct; a held station still
  pings. *Interval changing faster than the dot can traverse
  (violent scrolling):* the dot's traversal is cosmetic; the
  ping event schedule is computed from elapsed time, not from
  the dot, so no pings are lost or doubled. *Background tab:*
  ping events pause with rAF; on return, one ping fires and the
  schedule resumes — missed pings are not back-filled.
- **Accessibility spec (v2).** `aria-hidden` like the depth
  readout — a changing timer is not announced. The interval's
  *consequence* (content appearing) is ordinary DOM content and
  needs no announcement. The static reduced-motion bar carries a
  visually hidden text equivalent ("Ping interval lengthens
  with depth, 2.4 to 6 seconds").
- **Tokens consumed (v2).** `--pressure`, `--chart`,
  `--phosphor`, `--grey-line`, `--ping-min` (2.4s),
  `--ping-max` (6.0s), `--loop-lerp` (0.085).

### 6.5 Pressure readout & vignette

- **What & why.** A `PRESS` figure on the gauge climbs 1 BAR →
  481 BAR as the reader descends, while a vignette closes in and
  the page background lerps toward near-black. It belongs
  because depth in this theme is *felt*, not just numbered: the
  same scroll that raises the pressure figure physically darkens
  and tightens the room, so the reader's body learns the dive
  before their eye reads the gauge. The figure keeps the effect
  honest — the darkness is a measurement, printed beside itself.
- **Structure.** The readout is a two-line block in the rail
  beneath §6.4 (`PRESS` label over value, same typography). The
  vignette is a fixed full-viewport overlay div
  (`pointer-events: none`, `aria-hidden`) carrying a radial
  gradient transparent at centre → `--deep` at the corners,
  whose opacity is scrubbed 0.15 → 0.85 across the descent; the
  page ground colour itself lerps `--abyss` → `--deep` on the
  same fraction, applied to the root element's background so
  overscroll and rubber-band areas darken too.
- **Motion spec.** `P(d) = 1 + d/10` BAR, integer, updated on
  change. Vignette opacity and background lerp read the lerped
  depth fraction directly (no separate easing — they *are* the
  lerp made visible). The vignette's inner radius also tightens
  slightly (62% → 54% of the viewport diagonal) so the closing
  is spatial, not just darker. Nothing here animates on a timer;
  a still reader sits in still water at constant pressure.
- **States.** Rest (surface): `1 BAR`, vignette 0.15 (a faint
  room edge — the room has corners even at the surface).
  Descending: figure climbs, room closes. Bottom: `481 BAR`,
  vignette 0.85, ground at `--deep`. Hover/focus: none. Disabled
  (no JS): `PRESS — BAR` printed; vignette held at its surface
  0.15 via a no-JS default class — the static room is the
  surface room, lit as §6.6's fallback requires.
- **Content merge.** The pressure figure, the vignette and the
  background are three printings of `P(d)`/depth fraction; §10
  samples all three at 2,400 m (241 BAR, vignette ≈0.5, ground
  mid-lerp) and fails the build if any disagrees. The effect
  also serves the content: as sections deepen, their `--abyss-2`
  panels sit on a darker ground, so contrast *rises* with depth
  — the room protects its own print.
- **Failure fallback.** The overlay is decorative and removable:
  if the loop dies it freezes mid-vignette with all content
  beneath untouched (it never carries content, never sits above
  text at an opacity that can hide it — 0.85 at the *corners*,
  ≤0.25 over the centred reading column by gradient geometry).
  No JS: surface state, fully lit.
- **Reduced-motion variant.** The figure still updates; the
  vignette is fixed at 0.3 and the background lerp is disabled —
  pressure is reported, not performed on the reader's eyes.
  (A scrubbed darkening is vestibular-adjacent for some readers;
  the theme does not argue.)
- **Performance budget & mobile variant.** One opacity write on
  a composited overlay + one background-colour write per frame
  worst case; ≤0.15ms. Mobile: vignette gradient re-centred on
  the narrower column, max opacity 0.8 (small screens sit closer
  to the eye; the room closes less).
- **Choreography timeline (v2).** Scroll → lerped depth rises →
  figure increments roughly +1 BAR per 10 m of page depth →
  vignette opacity and ground track the same fraction with no
  lag beyond the shared lerp → at the bottom all three settle:
  481 BAR / 0.85 / `--deep` → ascent reverses all three in step.
- **State matrix (v2).** *Rest:* 1 BAR, surface light. *Hover:*
  none. *Focus:* none. *Active:* n/a. *Scrolled-past:* n/a
  (fixed). *Disabled:* em-dash figure, surface vignette.
  *Touch:* identical values; vignette max 0.8.
- **Breakpoints (v2).** ≥1200px: readout in rail; vignette radius
  62% → 54%. 768–1199px: same, radius band narrowed 2 points.
  <768px: readout in the surface bar (§6.3) at the bar's right;
  vignette as the mobile variant above.
- **Edge cases & failure modes (v2).** *Reader with
  `prefers-contrast: more`:* the lerp range halves (§2) and the
  vignette caps at 0.5 — pressure is still printed in full; only
  its theatre is rationed. *Very bright ambient (the page read
  outdoors):* the surface state is the brightest the room gets;
  that is a theme constraint, stated in §1's when-NOT list.
  *Footer reached:* the seabed section (§6.11) sits in the
  darkest state — its chart is drawn in `--phosphor`/`--amber`
  precisely so it reads at 481 BAR.
- **Accessibility spec (v2).** Readout `aria-hidden` (live
  number); the vignette is `aria-hidden` and `pointer-events:
  none`. Text contrast is *computed at the bottom state*, not
  the surface: `--chart` on `--deep` is 16.1:1, `--pressure`
  furniture 3.5:1 — §10 measures at full depth. No information
  is carried by darkness alone; depth is always also a printed
  figure.
- **Tokens consumed (v2).** `--deep`, `--abyss`, `--pressure`,
  `--chart`, `--press-surface` (1), `--press-per-10m` (1),
  `--vignette-min` (0.15), `--vignette-max` (0.85),
  `--loop-lerp` (0.085).

### 6.6 Ping reveals

- **What & why.** Each section arrives the way a return arrives:
  dimmed and blurred while unsounded, then — as it crosses
  mid-viewport and the room's next ping reaches it — an expanding
  phosphor ring passes over it and it sharpens to full legibility.
  It belongs because it is the theme's core verb: *content exists
  when sounded*. Without it the page is a dark site with a sonar
  picture on top; with it, reading *is* the survey.
- **Structure.** Sections carry `data-sound` in the DOM, fully
  printed. The pre-state (opacity 0.35, blur 6px, saturate 0.7)
  is applied by a JS-added class (`is-unsounded`) only after the
  script arms and only to sections below the fold — above-fold
  sections are sounded by the hero's first sweep (§8.1) and never
  pass through a visible pre-state. The ring is a single reusable
  absolutely-positioned div (border 1px `--phosphor`, border-radius
  50%) spawned at the section heading's origin dot (§6.7),
  expanding over the section's bounding box diagonal.
- **Motion spec.** Trigger: IntersectionObserver at 50% viewport
  height marks the section *in position*; the reveal itself waits
  for the next ping event (§6.4) — so a section never sharpens
  mid-interval, and at depth the wait is honestly up to 6.0 s.
  On the ping: ring expands 0 → 120% of the section's diagonal
  over 1,400ms (`--ease-sound`), alpha 0.8 → 0; the section
  sharpens across the ring's passage — blur 6px → 0 and opacity
  0.35 → 1 over 900ms (`--ease-settle`), timed so the sharpening
  front tracks the ring's edge. **Watchdogs (the element's law):**
  2,600ms after a section enters position, if no ping has
  released it, it sharpens anyway; at 6,000ms an absolute
  watchdog forces *every* unsounded section on the page visible,
  whatever the observer believes. A reveal may be late; it may
  never be absent.
- **States.** Unsounded (JS-armed, below fold): dimmed/blurred
  but *present* — headings' text is in the DOM and findable.
  Sounding: ring passing, sharpening. Sounded: full rest state,
  latched — scrolling away and back never re-dims (the dive does
  not un-happen, §4). Hover: n/a at section level (children have
  their own). Disabled (no JS / script failed): no pre-state is
  ever applied; the page is simply printed — this is the default
  the pre-state is an enhancement *over*.
- **Content merge.** The ring's origin is the section's own
  heading dot (§6.7), its timing is the room's ping (§6.4), and
  its order across a page is range order (§4) — the reveal is
  not an entrance effect applied to content, it is the content
  being received by the instrument the page is about.
- **Failure fallback.** The double watchdog above, plus: if
  IntersectionObserver is unavailable, a scroll listener arms
  the same triggers; if *that* fails, the 6 s absolute watchdog
  still fires from a plain timeout set at arm time. Three
  independent paths, all ending at visible. §10's gate includes
  a JS-disabled render and a throttled-CPU render; both must
  show every section.
- **Reduced-motion variant.** No pre-state, no ring, no blur:
  sections are printed at full legibility from first paint (the
  "room lit" state). The ping still fires for §6.7's rings in
  their reduced form (a dot brightening), but nothing waits for
  it.
- **Performance budget & mobile variant.** Blur is the expensive
  property: it is applied only to sections currently sounding
  (≤2 concurrent, enforced) and removed at rest. Ring is one
  transformed div. Mobile: blur pre-state reduced to 3px and
  opacity 0.45 (small screens, weaker GPUs), ring duration
  1,100ms, concurrent sounding capped at 1.
- **Choreography timeline (v2).** Section crosses mid-viewport →
  marked in position → next ping event (≤ `I(d)` away) → t=0
  ring spawns at the heading dot → t=0–900ms sharpening front
  tracks the ring → t=900ms section at full rest → t=1,400ms
  ring fades out at 120% → latch set. Watchdog path: in position
  + 2,600ms with no ping → sharpen over 600ms with no ring.
- **State matrix (v2).** *Rest (sounded):* full print. *Hover:*
  n/a. *Focus:* a section receiving focus (skip link, find-in-page
  jump) is sounded instantly, ring or no ring — focus outranks
  the ping, always. *Active:* n/a. *Scrolled-past:* latched
  visible. *Disabled:* printed, no pre-state. *Touch:* identical
  triggers; the mid-viewport line is the same.
- **Breakpoints (v2).** ≥1200px: full spec (blur 6px, ring to
  120%). 768–1199px: blur 4px, ring to 110%. <768px: blur 3px,
  opacity floor 0.45, one sounding at a time, ring to 100% of
  the (narrower) diagonal.
- **Edge cases & failure modes (v2).** *Reader scrolls the whole
  page in one fling:* sections enter and leave position faster
  than pings fire — the 2.6 s watchdog sounds them in order as
  the scroll settles; nothing is left dimmed behind the reader.
  *Reader jumps via anchor to the footer:* the target section
  sounds instantly (focus rule), sections above it are sounded
  by the absolute watchdog within 6 s of arming — the log is
  never a page of blurred text behind the reader. *Content
  taller than 2× viewport:* the trigger is the section's
  *heading* crossing mid-viewport, not a percentage of the
  section, so long sections sound on arrival like short ones.
  *Scroll up into an unsounded section:* cannot happen — the
  latch and the watchdogs have sounded everything below the
  reader's deepest point.
- **Accessibility spec (v2).** The pre-state is visual only:
  `aria-hidden` is never applied, content is fully in the
  accessibility tree while blurred (a screen reader's dive has
  no unsounded water). Focus-into-section forces sounding
  (above). Blur never drops effective contrast below the
  pre-state floor for text the reader is meant to read *now* —
  unsounded sections are by definition not yet at mid-viewport.
  Reduced-motion and no-JS states are fully printed.
- **Tokens consumed (v2).** `--phosphor`, `--ease-sound`,
  `--ease-settle`, `--dur-ring` (1400ms), `--dur-sharpen`
  (900ms), `--watchdog-ping` (2600ms), `--watchdog-absolute`
  (6000ms), `--blur-unsounded` (6px), `--opacity-unsounded`
  (0.35).

---

### 6.7 Heading ping rings

- **What & why.** Every section heading carries a small amber
  origin dot at its left, and on the room's live ping interval
  the dot emits an expanding ring that fades over ~2 s. It
  belongs because it makes every heading a transducer: each
  chapter of the page audibly (visually) sounds itself, at the
  rate the current depth demands — so the reader *sees* the
  ping interval (§6.4) happening all over the page, not just
  printed on the gauge.
- **Structure.** The dot is a 7px CSS circle (`--amber-deep` at
  rest) inline before the heading text, in the heading's own
  box. Rings are drawn on a single shared full-page canvas
  overlay (`pointer-events: none`) that §6.6's reveal rings and
  §6.12's snow also use — one canvas, three duties, one paint.
  Each heading registers its dot's position on resize/scroll;
  the overlay reads the registry, never the DOM per frame.
- **Motion spec.** On each ping event (§6.4), every *sounded*
  heading within or near the viewport (one viewport above and
  below) emits one ring: radius 4 → 130px over 2,000ms
  (`--ease-sound`), stroke alpha 0.55 → 0, dot flaring to full
  `--amber` for the first 300ms then decaying (`--ease-decay`).
  Unsounded headings do not ring — their first ring is their
  reveal (§6.6). Rings from neighbouring headings overlap and
  add (screen blend) where sections are dense — interference
  patterns are physically true and visually free.
- **States.** Rest: dot at `--amber-deep`, still. Pinging: flare
  + ring as above. Hover (heading's section link, where the
  heading is a link): one immediate soft ring regardless of the
  schedule — attention is a ping too, but it does not reset the
  room's clock. Focus: same ring + the link's outline.
  Scrolled-past: headings above the viewport stop ringing (the
  registry's near-viewport rule). Disabled: dots print static;
  a still dot beside a heading is punctuation, not a failure.
- **Content merge.** The dot is the heading's origin point in
  the survey — §6.6's reveal ring is born at this same dot, and
  §6.14's table rows cite sections by the depths these headings
  sit at. The ring rate is §6.4's number; the dot's colour is
  the amber census's licensed heading use (§2). Nothing here is
  a generic "pulse animation": remove the ping system and the
  dots have nothing to emit.
- **Failure fallback.** The overlay canvas is decorative; its
  absence (no canvas, loop dead) leaves printed dots and full
  headings. Headings are never styled by the canvas, never
  hidden by it. Watchdog: none needed — nothing can strand.
- **Reduced-motion variant.** No rings. On each ping the dot
  brightens to `--amber` and returns over 600ms — a lamp, not a
  wave. Under `prefers-reduced-motion` with JS off: static dots.
- **Performance budget & mobile variant.** Rings are strokes on
  the shared overlay; ≤6 concurrent by the near-viewport rule;
  ≤0.2ms/frame. Mobile: ring radius caps at 90px (the column is
  narrow; a 130px ring would cross the gauge bar), and only the
  single nearest heading rings per ping.
- **Choreography timeline (v2).** Ping event → t=0 all eligible
  dots flare → rings expand 2,000ms → t=300ms dots begin decay
  → t≈1,100ms dots at rest → t=2,000ms rings gone → silence
  until the next ping, `I(d)` later.
- **State matrix (v2).** *Rest:* dim dot. *Hover:* immediate soft
  ring (link headings). *Focus:* ring + outline. *Active:* the
  click's hard ping (§6.6 family — amber flash at the dot,
  500ms). *Scrolled-past:* silent. *Disabled:* printed dot.
  *Touch:* no hover ring; the schedule's rings continue.
- **Breakpoints (v2).** ≥1200px: radius 130px, all near-viewport
  headings. 768–1199px: radius 110px. <768px: radius 90px,
  nearest heading only.
- **Edge cases & failure modes (v2).** *Two headings 40px apart
  (a short section):* both ring; the overlap brightens — allowed,
  it reads as a strong return from a dense layer. *Heading at
  the very top under the fixed masthead:* its dot registers its
  true position; rings clip under the masthead's ground, which
  is correct occlusion. *Long headings wrapping:* the dot sits
  on the first line's baseline box; rings centre on the dot,
  not the text block.
- **Accessibility spec (v2).** Dots and rings are `aria-hidden`
  decoration on real heading elements; heading text and order
  are untouched. The ping's information content ("the room is
  alive at this rate") is carried in words by §6.4's readout.
  No focusable element is created by this element.
- **Tokens consumed (v2).** `--amber`, `--amber-deep`,
  `--phosphor`, `--ease-sound`, `--ease-decay`, `--dur-ring-heading`
  (2000ms), `--ring-radius` (130px).

### 6.8 Echogram console

- **What & why.** A live scrolling waterfall console: the seabed
  return writes itself across the screen in real time as an
  amber trace with echo smear, a scattering-layer band drifts
  and breathes mid-water, and a mono readout reports the live
  seabed depth and return character. It belongs because it is
  the dive's second instrument — the scope looks *around*, the
  echogram looks *down* — and because it shows the reader the
  water column they are currently descending through, drawn from
  the same sheet as everything else.
- **Structure.** A console panel (`--abyss-2`, bezelled, §11)
  spanning the content column: a canvas waterfall (height
  320px) over a printed axis (depth ticks 0 → 200 m in caption
  mono along the left — the echogram's window is the top 200 m
  of water beneath the hull, stated on the panel), and a readout
  strip beneath in data mono: `SEABED 84.2 M · RETURN SOFT ·
  STN 1`. The readout is DOM text. Beneath the panel, a printed
  caption explains the window in one sentence of body text —
  the console never asks the reader to guess its scale. The
  canvas draws: new column every 120ms at the right edge,
  history scrolling left; the seabed trace is a function of the
  station profile (§6.17) interpolated across the transect,
  smeared downward 6–18px in fading amber (soft bottom smears
  more — that is what SOFT means, drawn).
- **Motion spec.** Continuous write, 120ms per column (~8.3
  columns/s), trace brightness breathing ±8% on a 7 s cycle (the
  gain riding, as real gains do). The scattering layer — a
  diffuse phosphor-faint band — sits at 60–90 m in the window,
  drifting ±6 m over 40 s and thinning/thickening over 25 s:
  the deep scattering layer is alive and the console says so
  without a word. Return character cycles with the transect
  position the reader's scroll implies: at the hero it reads
  Station 1 (SOFT, 84.2 m); as the reader descends past the
  console's section, the readout walks the stations in order —
  the console reports the water under the *page*, station by
  station, and §6.17's table is its source.
- **States.** Rest (live): writing, readout current. Hover: the
  write pauses (an operator freezing the trace to look) and a
  `HELD` tag appears in the readout strip; leaving resumes —
  the pause is labelled, never silent. Focus (the panel is
  focusable as a region with a label): same hold. Scrolled-past:
  the write continues (it is an instrument, and §14 budgets it)
  but slows to one column per 400ms once a full viewport away —
  a console nobody watches writes slower. Disabled (no canvas):
  the panel prints a static echogram *image* — an SVG rendering
  of Station 1's trace, in the DOM as `<img>` with full alt —
  with the same readout strip in print.
- **Content merge.** The trace is the sheet's seabed, the readout
  is the sheet's station line, the smear depth is the sheet's
  return character drawn as physics. Put different survey data
  in the sheet and the console draws a different sea. It is a
  display *of the content*, not a screensaver beside it.
- **Failure fallback.** Canvas failure → the static SVG plate
  (always in the DOM, revealed by the same arming logic as
  §6.1's fallback). The readout strip is DOM and prints
  regardless. Watchdog 1,200ms on first column: no column, no
  canvas — plate instead.
- **Reduced-motion variant.** The plate state, live-updated
  only in its readout text (station changes still print — data
  is not motion). No scrolling waterfall, no breathing.
- **Performance budget & mobile variant.** The waterfall redraws
  one 2px column per tick and shifts history via a cached
  offscreen canvas blit — ≤0.5ms/frame average. Mobile: window
  height 220px, column every 200ms, scattering layer kept (it
  is the console's life) but its drift halved.
- **Choreography timeline (v2).** Section sounds (§6.6) → console
  bezel prints → first column writes at +120ms → trace
  establishes leftward → readout strip types its station line
  (no typewriter effect — it *prints*, one frame) → continuous
  write → reader scrolls on: station walk begins as the next
  sections sound.
- **State matrix (v2).** *Rest:* writing. *Hover:* held, `HELD`
  tag. *Focus:* held, tag + region outline. *Active:* n/a.
  *Scrolled-past:* slow write (400ms columns). *Disabled:*
  static plate + printed readout. *Touch:* tap-and-hold is the
  hold state; the tag still prints.
- **Breakpoints (v2).** ≥1200px: 320px window, full station walk.
  768–1199px: 260px window. <768px: 220px window, readout strip
  wraps to two lines (station line, then return line) — never
  truncated, never shrunk below caption size.
- **Edge cases & failure modes (v2).** *The transect's deep
  stations (4,800 m) in a 200 m window:* the console's window is
  the water *beneath the hull*, and its readout at deep stations
  prints `SEABED BELOW WINDOW — SEE PROFILE §FOOTER` rather
  than drawing a false trace — the instrument admits its range,
  and points at §6.11. (Stations 1–3 trace in-window; 4–7 print
  the admission.) *Long hover:* the hold persists; the trace
  resumes from the hold point with a 1-column gap marked —
  real traces have gaps where the operator looked away.
  *Reader returns up-page:* the station walk reverses; the
  console reports the water it is under, both ways.
- **Accessibility spec (v2).** Canvas `aria-hidden`; the panel is
  a labelled region whose readout strip is real text and whose
  static plate carries alt text describing Station 1's trace
  ("Echogram: seabed return at 84.2 metres, soft bottom, wide
  smear; scattering layer at 60 to 90 metres"). The station
  walk changes text at most once per section sounded — no live
  region; the changes are announced by nothing and missed by no
  one, since §6.14 prints the same stations as a table.
- **Tokens consumed (v2).** `--abyss-2`, `--amber`,
  `--amber-deep`, `--phosphor-faint`, `--pressure`, `--chart`,
  `--dur-column` (120ms), `--dur-gain-breath` (7s),
  `--window-depth` (200).

### 6.9 Echo-return log cards

- **What & why.** The survey's findings as the log the instrument
  produced: one card per contact on the sheet — name, mono
  readouts (range, bearing, depth), return character, a pulsing
  contact dot — arriving staggered like successive returns. It
  belongs because a survey's product *is* its log; presenting
  findings as feature cards with icons would break the fiction
  and the facts at once. Here the card's form is the data's
  form.
- **Structure.** A `<ul>` grid (§4: 3-up desktop) of `<article>`
  cards on `--abyss-2`, each: header row — contact dot (9px,
  `--amber` ring + `--phosphor-dim` core) and contact ID in data
  mono (`A1`); the name in H3 (`WRECK`); a definition list of
  the sheet's figures (`RNG 1,240 M · BRG 038° · DEPTH 212 M ·
  RETURN STRONG`); one line of log prose in body text ("Held on
  every pass since the second sweep. Cross-checked against the
  2019 chart: the wreck has not moved."); and, for A4, the depth
  row prints `DEPTH — NO RETURN` — the absence is a row, not a
  gap. Cards link to their detail view (§7) except A4, whose
  card is deliberately linkless and labelled `UNLOGGED RETURN`
  in its footer row — the room does not invent a page for what
  it could not identify. (The ghost has no card at all, §6.12.)
- **Motion spec.** Arrival: when the grid sounds (§6.6), cards
  return in range order — A5 (890 m) first, then A1 (1,240),
  A2 (2,860), A3 (3,940), A4 (4,410) — each rising 14px and
  sharpening over 700ms (`--ease-settle`), successive cards
  offset by `I(d)/6` (at the cards' depth of ≈900 m, `I` ≈
  3.08 s, so ≈510ms apart — the stagger is the ping, divided).
  The contact dot pulses on the room's ping while its card is
  in view: flare 300ms, decay 1,700ms. Tilt: on hover, cards
  tilt toward the pointer at max 3° (`rotateX/Y` from lerped
  pointer position, 0.12 lerp — a console screen catching
  light), settling flat over 500ms on leave.
- **States.** Rest: printed, dot dim. Pinging: dot flare per
  schedule. Hover: tilt ≤3°, dot to full `--amber`, card ground
  to `--abyss-3`. Focus (card link): tilt suppressed (a tray
  does not tilt for a keyboard), dot flares, 2px outline on the
  card. Active: one hard ping at the dot (§6.6's click return,
  amber flash 500ms) then navigation. Scrolled-past: printed,
  dots keep the ping only within one viewport. Disabled: A4's
  linkless state is the designed disabled pattern; a contact
  with no detail page in a real build uses the same treatment.
- **Content merge.** Every figure on every card is a sheet
  figure; the card order in the DOM is contact order (A1–A5)
  while the *arrival* order is range order — print and physics
  each get their truth. The prose line is the log's voice (§12),
  one per contact, written from the sheet's notes field.
- **Failure fallback.** Cards are DOM print; the arrival is a
  JS-armed transform/opacity enhancement with §6.6's watchdogs
  behind the grid. No JS: a printed log grid, complete. Tilt
  failure (no pointer, no loop) leaves flat cards — their rest
  state.
- **Reduced-motion variant.** Cards print in as a block with
  their section (no rise, no stagger); dots do not pulse (a
  steady dim dot); no tilt. The log is read, not watched.
- **Performance budget & mobile variant.** Arrival transforms on
  ≤5 cards; tilt math is two lerped values on the one hovered
  card. Mobile: 1-up grid, tilt off (no pointer), dot pulse
  kept (it is the room's clock, cheap), stagger compressed to
  `I(d)/10`.
- **Choreography timeline (v2).** Grid sounds → t=0 A5 sharpens
  (700ms) → t≈510ms A1 → t≈1,020ms A2 → t≈1,530ms A3 →
  t≈2,040ms A4 (arriving dimmest — its return is weakest, flare
  capped at 60%) → all at rest → dots join the ping schedule.
- **State matrix (v2).** *Rest:* printed, dot dim. *Hover:* tilt
  ≤3°, dot full, ground lifts. *Focus:* dot flare + outline, no
  tilt. *Active:* hard ping, navigate. *Scrolled-past:* print.
  *Disabled:* linkless card pattern (A4). *Touch:* no tilt;
  tap = active.
- **Breakpoints (v2).** ≥1200px: 3-up (A1–A3 / A4–A5 + chart
  card slot per §4). 768–1199px: 2-up. <768px: 1-up, figures
  list wraps to two lines per card — figures never truncate.
- **Edge cases & failure modes (v2).** *A real survey with 40
  contacts:* the grid paginates (§11) at 12 per page; arrival
  order within a page is still range order; the sheet (§6.17)
  is the full record and the cards say so. *A contact whose
  prose line is long:* cards in a row equalise height by grid;
  prose clamps at 3 lines with the full line on the detail
  view — the log card is a summary and admits it. *Duplicate
  bearings in real data:* arrival order falls back to contact
  ID; the sheet's order governs ties, stated in §6.17.
- **Accessibility spec (v2).** Each card is one link (where
  linked) whose accessible name is the full sheet line
  ("Contact A1, wreck, range 1,240 metres, bearing 038, depth
  212 metres, return strong"); the visible figure list is
  `aria-hidden` duplication of that name's facts. Dot is
  decorative. Focus outline 2px `--phosphor` at 3px offset;
  touch targets are the whole card (≥120px tall).
- **Tokens consumed (v2).** `--abyss-2`, `--abyss-3`, `--amber`,
  `--amber-deep`, `--phosphor`, `--phosphor-dim`, `--chart`,
  `--pressure`, `--ease-settle`, `--tilt-max` (3deg),
  `--dur-card-return` (700ms).

---

### 6.10 Counting soundings

- **What & why.** The survey's headline figures — 214 surveys,
  38,200 km² mapped, 10,894 m deepest, 99.2% coverage — count up
  digit-by-digit with a mechanical tick when their section is
  sounded. It belongs because figures in this room are *read off
  the instrument*: a sounding arrives one ping at a time, and a
  statistic that fades in like marketing copy would be a lie
  about how the number was earned. The count is the earning,
  replayed.
- **Structure.** A four-figure band, each figure a block: the
  value in readout XL mono (the counting element), its label in
  caption mono beneath (`SURVEYS LOGGED`, `KM² MAPPED`,
  `DEEPEST SOUNDING`, `BLOCK COVERAGE`), and a one-line source
  note in body text tying it to the sheet ("Sheet № 214 is the
  latest of the 214"; "10,894 m — Sheet № 167, this dive's
  bottom is 4,800 m"). The source note is mandatory furniture:
  a figure without its provenance is exactly what §9 calls
  chartjunk. The final values are the DOM text; counting is a
  text-write sequence over them.
- **Motion spec.** On sounding (§6.6), each value counts from 0
  to its sheet figure over 1,800ms, digit drums rolling
  (`--ease-tumble` character cycling in each position, positions
  settling right-to-left as the count converges — the units drum
  stops first, as on a real counter), with a soft tick (a 1px
  phosphor flash under the figure) on each settled position.
  Figures start together; larger figures do not take longer —
  the count is one sounding, 1,800ms for all four. Each stops
  *dead* at its sheet value: 214, 38,200, 10,894, 99.2. A figure
  that overshoots, eases past, or rounds is a §10 failure.
- **States.** Rest (printed): the sheet values, static — this is
  the shipped state. Counting: drums rolling per above. Hover:
  none (figures are not controls). Focus: n/a. Scrolled-past:
  values at rest. Disabled (no JS): the printed values — the
  count is an enhancement over print, never a gate before it.
- **Content merge.** The four figures are §6.17's summary block,
  and their source notes are the sheet's own distinctions
  (fleet record vs this dive) printed beside them — the section
  teaches the reader to read the room's numbers the way the
  room prints them: every figure with its sheet attached.
- **Failure fallback.** Print is the fallback; the watchdog is
  §6.6's pair (the section sounds, the count plays or is skipped
  — at 6 s the values are the sheet's regardless, because they
  were never anything else in the DOM).
- **Reduced-motion variant.** No count. The figures are read as
  printed. (A number appearing is information; a number *rolling*
  is theatre, and reduced motion keeps the information.)
- **Performance budget & mobile variant.** Text writes on four
  elements for 1,800ms once per page load; negligible. Mobile:
  2×2 grid, readout XL at its 2rem floor, source notes kept —
  provenance is never the thing cut for space.
- **Choreography timeline (v2).** Section sounds → t=0 all four
  drums start → t≈600ms units positions settle (ticks) →
  t≈1,200ms tens/hundreds settle → t=1,800ms all four at sheet
  values, final tick → rest, permanently.
- **State matrix (v2).** *Rest:* sheet values printed. *Hover:*
  none. *Focus:* n/a. *Active:* n/a. *Scrolled-past:* rest
  values. *Disabled:* printed values. *Touch:* the count fires
  on sounding identically — it is scroll-triggered, not
  pointer-triggered.
- **Breakpoints (v2).** ≥1200px: four across. 768–1199px: four
  across at reduced readout size (2.25rem). <768px: 2×2.
- **Edge cases & failure modes (v2).** *The decimal figure
  (99.2%):* the drum rolls the integer part; the `.2` is printed
  from the start — a tenth of a percent is a measured residue,
  not a drum position; the sheet's rounding note (§6.17) says
  shares and coverage are printed as measured. *Reader scrolls
  past mid-count:* the count completes off-screen (it is
  time-based once fired) so returning shows rest values, never
  a half-rolled drum. *Re-entry:* the count never replays; a
  sounded figure stays sounded (§4's latch).
- **Accessibility spec (v2).** The counting element is
  `aria-hidden` during its 1,800ms; a visually hidden static
  text carries the final values for assistive tech from first
  paint ("214 surveys logged; 38,200 square kilometres mapped;
  deepest sounding 10,894 metres; block coverage 99.2 percent").
  Nobody's screen reader listens to a drum roll.
- **Tokens consumed (v2).** `--chart`, `--phosphor`,
  `--pressure`, `--ease-tumble`, `--dur-count` (1800ms),
  `--dur-tick` (120ms).

### 6.11 Seabed profile chart & the seabed footer

- **What & why.** The page ends on the bottom it has been
  descending toward: an SVG profile of the dive's seabed drawn
  across the footer section — seven stations, the line dropping
  from 84.2 m to the 4,800 m floor — including an amber dashed
  segment where the return honestly weakened, and beneath it the
  footer's colophon printed like the last line of a chart. It
  belongs because a dive that does not reach its bottom is
  unfinished; the footer is not page furniture here, it is the
  destination.
- **Structure.** A full-measure `<figure>`: the SVG profile
  (viewBox 1200×360, depth axis inverted — down is down) with
  station points as phosphor dots, station labels in caption
  mono (`STN 4 · 2,512 M · HARD`), the weak segment (Stn 5 →
  Stn 6) as a dashed `--amber-deep` stroke with its own label
  (`WEAK RETURN — DRAWN DASHED, AS RECEIVED`), and a depth axis
  at 0 / 1,000 / 2,000 / 3,000 / 4,000 / 4,800 m. Below the
  figure, the footer proper: three columns of print — the
  vessel and sheet line ("RV MERIDIAN · DIVE SHEET № 214 ·
  SOUNDED AND SET IN THE SONAR ROOM"), the footer navigation
  (real links, §11), and the closing totals line that re-prints
  the dive's summary from the sheet (descent 4,800 m · 7 stations
  · 5 contacts logged, 1 unlogged). The chart is also a table in
  disguise: a visually hidden (and print-visible) data table of
  the seven stations accompanies it (§6.14 prints the same table
  visibly mid-page; the figures agree because both are the sheet).
- **Motion spec.** On sounding, the profile draws itself station
  by station: stroke-dashoffset animation across 2,600ms
  (`--ease-settle`), each station dot flaring as the line
  reaches it (300ms phosphor flare), labels printing in the
  same order. The weak segment draws last within its span and
  draws *dashed from the first dash* — it never draws solid and
  converts; the honesty is in the stroke, not an annotation
  added later. The colophon columns print with the section's
  standard reveal (§6.6), no separate effect.
- **States.** Rest: the full chart, drawn. Drawing: per above,
  once, latched. Hover (station dot): the dot flares and its
  label lifts to `--chart`, showing the station's full line.
  Focus: station dots are not focusable; the chart's data lives
  in its table (§6.14) for keyboard and AT users. Scrolled-past:
  drawn. Disabled: the SVG ships fully drawn in markup
  (dashoffset is a JS-armed pre-state, removed by the same
  watchdog pair as §6.6) — a no-JS reader gets the finished
  chart.
- **Content merge.** The profile *is* the dive: its x-axis is
  the page the reader just scrolled (stations in the order the
  echogram walked them, §6.8), its floor is the gauge's maximum
  (§6.3), its weak segment is the sheet's WEAK printed in §6.14's
  table. The footer does not decorate the page's end; it
  *concludes* it, and the colophon's totals are the third
  printing of figures the gate cross-checks (§10).
- **Failure fallback.** Fully-drawn-in-markup default (above);
  the draw is an enhancement. SVG unsupported (legacy): the
  accompanying data table becomes visible in its place — the
  bottom is still charted, as figures.
- **Reduced-motion variant.** Chart printed fully drawn; station
  dots steady; no draw, no flare. The destination does not need
  to arrive — it needs to be there.
- **Performance budget & mobile variant.** One stroke animation
  on one path, once; negligible. Mobile: the SVG scales to
  column width with labels at Stn 1, 4, 6 only (the axis keeps
  all ticks; intermediate station labels move into the table
  below the figure, which is visible on mobile by default) —
  the chart is never shrunk into illegibility.
- **Choreography timeline (v2).** Footer section sounds → t=0
  draw begins at Stn 1 (84.2 m) → line descends through Stn 2–5
  (≈430ms per span) → weak span draws dashed Stn 5 → Stn 6 →
  Stn 7 rises → t=2,600ms profile complete, final dot flare →
  colophon prints beneath → the dive is over; the gauge reads
  the bottom.
- **State matrix (v2).** *Rest:* drawn chart + colophon. *Hover:*
  station flare + label lift. *Focus:* n/a on the chart; footer
  links take the standard focus treatment. *Active:* footer
  links navigate normally (leaving via §6.16's sweep).
  *Scrolled-past:* drawn. *Disabled:* printed chart (markup
  state). *Touch:* station hover states are not required for
  any data — labels print at rest on touch layouts.
- **Breakpoints (v2).** ≥1200px: full labels, 360px chart height.
  768–1199px: chart 300px, Stn 2/5 labels abbreviated to depth
  only. <768px: chart 240px, three station labels + visible
  table, colophon stacks to one column.
- **Edge cases & failure modes (v2).** *A transect with a
  shallower maximum than the page depth:* impossible in this
  theme — the sheet's deepest station *is* the page's depth
  (4,800 m); a build whose sheet says otherwise fails §10's
  figure audit. *Print:* the chart prints fully drawn with its
  table — the one page of the site a reader may pin to a wall,
  designed to deserve it. *Very long footer nav:* capped at two
  link columns; the seabed does not grow a sitemap.
- **Accessibility spec (v2).** The SVG is `role="img"` with a
  title and desc summarising the profile ("Seabed profile,
  seven stations, descending from 84.2 metres to a floor of
  4,800 metres; the return weakens between stations 5 and 6"),
  plus the accompanying data table for exact figures. Footer
  landmarks are standard (`<footer>`, labelled nav). Contrast:
  profile stroke phosphor on deep-state ground ≥9:1.
- **Tokens consumed (v2).** `--phosphor`, `--amber-deep`,
  `--pressure`, `--chart`, `--grey-line`, `--ease-settle`,
  `--dur-profile-draw` (2600ms), `--depth-max` (4800).

### 6.12 Ghost contact & marine snow

- **What & why.** Two inhabitants of the water, specified
  together because they share a canvas and a purpose — the page
  is a medium, not a backdrop. Marine snow: particulate drift at
  three parallax depths plus one near, out-of-focus layer,
  falling through every section. The ghost: occasionally a
  `DISTANT · UNCHARTED` contact drifts into the scope's rim for
  a few sweeps, flashes dimmer than any logged contact when
  struck, and is gone — never logged, never carded, never
  explained. Together they state the theme's humility: the water
  is inhabited and not fully known.
- **Structure.** Snow: ~90 particles on the §6.7 overlay canvas
  (shared pass), in four layers — far (1px, `--phosphor-dim` at
  25%, parallax 0.94×), mid (1.5px, 40%, 0.97×), near (2px, 55%,
  0.99×), and foreground (3–4px, blurred via a pre-rendered soft
  sprite, 12% alpha, 1.04× — the layer that passes *in front of*
  the reader). Each particle falls 6–14 px/s with a 0.3 Hz
  lateral sway. Ghost: a state in §6.1's scope model — a contact
  with no sheet entry, bearing drifting 1.5°/s, range pinned at
  the rim (5,600 m, half-clipped), present for 2–3 beam
  revolutions on a randomised schedule (first appearance no
  earlier than 90 s into the visit, then every 120–240 s, seeded
  per session so a visit is auditable).
- **Motion spec.** Snow falls continuously (ambient loop № 2,
  §5) and parallaxes against the lerped scroll: layers shift at
  their rates so a fast scroll streaks the far layer least —
  depth you can feel in the periphery. The ghost, when struck
  by the beam, flashes at 45% of a logged contact's brightness,
  emits no ring, and its chip — it has one, `DISTANT ·
  UNCHARTED`, the only chip not backed by the sheet — prints no
  range beyond `RNG — BEYOND SCOPE`. After its revolutions it
  drifts off the rim bearing and does not return that session
  at the same bearing.
- **States.** Snow: always falling (rest = falling; it has no
  other state). Ghost: absent (the overwhelming majority of the
  time) → present at rim → struck (dim flash) → gone. Hover:
  the ghost's chip is not a link and takes no hover — you cannot
  interrogate it; that is its point. Scrolled-past: snow
  continues everywhere (it is the medium); the ghost exists
  only in the hero's scope. Disabled (no canvas): no snow, no
  ghost — the printed page is a calm room, and §6.17's sheet
  carries the ghost's only mention ("one contact declined to be
  logged") as a prose note.
- **Content merge.** The snow is *in* the water every reading
  passes through — it crosses text, panels and instruments
  alike, at alphas low enough never to compete (§10 measures
  particle-over-text contrast). The ghost merges by refusal: it
  is the one thing the page's systems (log, cards, table,
  totals) all decline to absorb, and that shared refusal is the
  theme's thesis stated in behaviour.
- **Failure fallback.** Both are canvas-only enhancements over a
  complete printed page; their absence is invisible as an
  absence. No watchdog needed beyond §6.1's canvas check, which
  governs this canvas too.
- **Reduced-motion variant.** Snow: a static, sparsely printed
  dot field (the fallback sprite pattern, far layer only) — the
  water has texture, nothing falls. Ghost: never appears. A
  reduced-motion reader's sea is fully charted, and the sheet's
  prose note still records that the survey's was not.
- **Performance budget & mobile variant.** Snow is the room's
  second-largest frame cost: ≤0.5ms/frame at 90 particles,
  counted in §14. The frame-time governor (§14) sheds snow
  first: foreground layer, then near, then count halves. Mobile:
  48 particles, three layers (foreground cut — a phone is held
  close; nothing should drift across its lens), ghost kept (it
  costs nothing and means everything).
- **Choreography timeline (v2).** Load → snow already falling
  (first frame) → scroll: layers shear at their parallax rates
  → t≥90 s: ghost enters the rim on a drift bearing → beam
  strikes: dim flash, no ring → 2–3 revolutions → ghost exits →
  snow continues, unchanged, unbothered.
- **State matrix (v2).** *Rest:* snow falling, ghost absent.
  *Hover:* snow indifferent; ghost chip non-interactive.
  *Focus:* unaffected. *Active:* n/a. *Scrolled-past:* snow
  everywhere; ghost hero-only. *Disabled:* neither; prose note
  in the sheet. *Touch:* identical (time- and scroll-driven).
- **Breakpoints (v2).** ≥1200px: 90 particles, 4 layers.
  768–1199px: 64 particles, foreground layer at half count.
  <768px: 48 particles, 3 layers, foreground cut.
- **Edge cases & failure modes (v2).** *Snow over the form
  (§6.15) while a visitor types:* particle alpha over panel
  grounds is capped at 20% and particles never render inside
  input boxes (the overlay clips to the page ground, panels are
  DOM above it) — weather does not enter the instruments.
  *Ghost schedule colliding with a page transition (§6.16):*
  transitions clear the ghost; a new session of the scope
  re-seeds. *A reader who never sees the ghost:* the expected
  case — the sheet's note and this spec carry its existence;
  the demo does not force an appearance for screenshots (§9).
- **Accessibility spec (v2).** Entirely `aria-hidden` canvas
  behaviour; nothing the ghost or snow "says" is information —
  the ghost's *meaning* (the survey admits an unknown) is
  printed in §6.17's prose and §6.9's A4 card for every reader.
  Snow alpha over text is audited (§10) so it can never reduce
  effective contrast below the printed values.
- **Tokens consumed (v2).** `--phosphor-dim`, `--phosphor-faint`,
  `--amber`, `--ease-decay`, `--snow-count` (90),
  `--ghost-range` (5600), `--ghost-first` (90s).

---

### 6.13 Sonar-room masthead & bearing navigation

- **What & why.** The site's navigation, built as the room's
  surface equipment: a slim fixed masthead carrying the vessel
  wordmark, the section links set as *bearings* (each link
  labelled with the depth at which its section is sounded), and
  at its right edge the live position line — current depth in
  mono — so the masthead and the gauge (§6.3) tell one story
  from two posts. It belongs because navigation in this world is
  orientation: the operator always knows their depth and their
  heading, and the masthead is where that knowledge lives when
  the rail is out of sight (mobile) or out of mind.
- **Structure.** A `<header>` + `<nav aria-label="Dive">`,
  fixed top, ground a gradient from `--abyss` to transparent
  over 64px (the surface light dissolving into water — the
  masthead is *at* the surface, and scrolling down leaves it in
  the bright layer, stated by its slightly lighter ground
  `--abyss-2` at 92% once the reader passes 100 m). Links: the
  page's sections by name with their sounding depths in caption
  mono (`LOG — 900 M`, `CONSOLE — 1,800 M`, `SOUNDINGS —
  3,300 M`, `BERTHS — 3,900 M`). The current section's link
  carries a phosphor bearing dot and `aria-current="location"`.
  The position line at right: `AT 1,842 M` in data mono,
  mirroring the gauge's lerped depth in metres (always metres
  here — the masthead speaks the surface's unit, the gauge owns
  the flip; the two are reconciled in §10 by conversion, and
  the difference is a stated rule, not an inconsistency).
- **Motion spec.** Entrance at load: the masthead prints in
  with the hero (no slide-down theatrics — furniture is bolted).
  Current-section changes: the bearing dot transfers with a
  400ms crossfade (`--ease-settle`), the old link dimming as
  the new one lights, driven by the same section-boundary table
  the depth labels use. The position line updates with the
  loop, throttled to 0.5 m changes like the gauge. On scroll
  past 100 m the masthead ground deepens (above) over 600ms;
  on return it lightens. No hide-on-scroll, ever: an operator's
  instruments do not leave their posts.
- **States.** Rest: current dot lit, position line current.
  Hover (link): link to `--chart`, a soft ping ring at the
  link's dot position (§6.7's language at masthead scale,
  radius 40px). Focus: ring + 2px outline. Active/current:
  dot lit `--phosphor`, link `--chart`, `aria-current`.
  Disabled: a link to an unpublished section prints in
  `--pressure` with no dot and no anchor — a bearing to water
  not yet surveyed. Scrolled-past: n/a (fixed).
- **Content merge.** The links are the dive's stations: their
  depths are §13's choreography depths, their order is the
  descent's order, and clicking one is an order to dive to that
  depth — the scroll it triggers is the gauge's descent,
  performed. Navigation *is* the page's depth structure,
  printed at the top.
- **Failure fallback.** Plain fixed header with printed links —
  the enhancements (dot transfer, position line) are loop-fed
  and their failure leaves a complete, working masthead.
  Watchdog: if the loop has not ticked by 1,200ms, the position
  line prints `AT — M` (the instrument admits it) rather than a
  wrong figure.
- **Reduced-motion variant.** Dot transfers are instant; the
  ground-deepening is instant at the 100 m threshold; the
  position line still updates (data). No rings on hover — a
  brightening dot only.
- **Performance budget & mobile variant.** Negligible DOM cost.
  Mobile (<768px): wordmark + position line + a menu button;
  links move into a surface panel ("the chart drawer") that
  opens downward over the water on `--abyss-2` at 98%, links
  full-width with their depths, 250ms `--ease-settle`. The
  depth gauge's surface bar (§6.3) docks *beneath* the
  masthead, so mobile's top stack reads: vessel, measure,
  water.
- **Choreography timeline (v2).** Load → masthead printed →
  hero sweep begins → first scroll past 100 m: ground deepens
  600ms → section boundary crossed: dot crossfades 400ms,
  position line continuous → bottom: last link lit, position
  line `AT 4,800 M` → ascent reverses the dot's journey.
- **State matrix (v2).** *Rest:* current lit. *Hover:* chart +
  soft ring. *Focus:* ring + outline. *Active:* current —
  dot lit, `aria-current`. *Scrolled-past:* n/a. *Disabled:*
  pressure-grey linkless item. *Touch:* drawer variant;
  targets ≥44px.
- **Breakpoints (v2).** ≥1200px: full links with depths,
  position line. 768–1199px: links without depth captions
  (depths move into the drawer and the sections' own labels).
  <768px: wordmark + position + menu button; drawer.
- **Edge cases & failure modes (v2).** *Many sections (a
  9-section dive):* links abbreviate to their short names
  before they wrap — the drawer carries full names + depths at
  every breakpoint. *Position line vs gauge disagreement:* the
  gate (§10) samples both at three depths and converts —
  metres here, the gauge's current unit there; a raw mismatch
  fails the build. *Anchor jump to the form:* the dot lands on
  BERTHS and the form's section sounds instantly (§6.6's focus
  rule) — the masthead never claims a depth the page hasn't
  reached.
- **Accessibility spec (v2).** Landmarks standard; skip link is
  the masthead's first element, printed `--chart` on
  `--abyss-3`, visible on focus. `aria-current` carries
  current-ness semantically; the dot is decorative. Position
  line is `aria-hidden` (live number); each section's printed
  depth label serves AT readers (§6.3).
- **Tokens consumed (v2).** `--abyss`, `--abyss-2`, `--abyss-3`,
  `--chart`, `--pressure`, `--phosphor`, `--ease-settle`,
  `--dur-dot-transfer` (400ms).

### 6.14 The sounding table

- **What & why.** For the reader who needs the dive plain: a
  true data table of the transect — one row per station, with
  seabed depth, return character, and the contacts heard at
  that station — printed in the data voice, with a totals row
  carrying the sheet's summary. It belongs because a survey
  that cannot be read as a table is a light show; the table is
  the theme's honesty in its most native form, and it is the
  element §1's hurried reader is sent to. Its one concession to
  the room: hovering a row fires a soft ping at the row's left
  edge (§6.6's language), so even the table is sounded.
- **Structure.** A semantic `<table>` with `<caption>` ("Soundings
  by station — Dive Sheet № 214"), scoped headers, seven station
  rows from the sheet (Stn 1: 84.2 m, SOFT, —; Stn 2: 312 m,
  SOFT, —; Stn 3: 1,140 m, STRONG, A5 heard bearing away; Stn 4:
  2,512 m, HARD, A2 VENT FIELD; Stn 5: 3,975 m, STRONG, —; Stn 6:
  4,800 m, WEAK, —; Stn 7: 4,214 m, STRONG, —), the WEAK row's
  return cell carrying a dashed amber underline — the table
  prints the weakness the chart draws. Totals in `<tfoot>`:
  `7 STATIONS · DEEPEST 4,800 M · MEAN 2,433.9 M` — the mean
  computed from the sheet and repeated verbatim in §6.17
  (84.2 + 312 + 1,140 + 2,512 + 3,975 + 4,800 + 4,214 =
  17,037.2; ÷ 7 = 2,433.9) — totals set
  in `--amber` per §3 (amber sets totals in this room's tables
  only where the sheet marks the row as a total).
- **Motion spec.** The table does not animate. No reveal beyond
  its section's sounding (§6.6). Row hover: ground lifts to
  `--abyss-3` over 200ms (`--ease-settle`) and one soft ping
  ring (radius 60px) emits from the row's left edge. That is
  all, deliberately: the one element a hurried reader uses is
  the one element that never performs.
- **States.** Rest: printed, hairline rules (`--grey-line`).
  Hover (row): lift + ping. Focus: rows are not focusable;
  the table's one interactive descendant (a station's "hear
  the pass" replay link on Stn 4, §8.2) takes standard focus.
  Active: n/a. Scrolled-past: printed. Disabled: a station
  whose data is provisional in a real build prints its figures
  in `--pressure` with a `PROVISIONAL` tag in the return cell —
  the table admits the state of its evidence.
- **Content merge.** The table *is* §6.17's station half in the
  reading flow — same order, same figures, same WEAK — and its
  rows are the profile's points (§6.11) and the echogram's
  walk (§6.8). Table, chart and console are three readings of
  one record, and §10 re-adds the table's column against the
  sheet.
- **Failure fallback.** None required — static HTML and a CSS
  hover. This element is the fallback's fallback: with JS,
  canvas and the loop all dead, the dive is still fully
  readable here.
- **Reduced-motion variant.** Identical, minus the hover ping
  (the lift becomes instant). The table was already the
  reduced-motion ideal; it changes least of any element.
- **Performance budget & mobile variant.** Zero JS beyond the
  shared hover ping. Mobile (<768px): the table becomes a
  stacked station list — each station a block, figures in
  definition-list layout, same order, same totals, WEAK still
  dashed — no horizontal scrolling is ever permitted (a
  sounding you must pan is a sounding lost). The transformation
  is markup + CSS chosen at build, not a JS re-render.
- **Choreography timeline (v2).** Section sounds (§6.6) → table
  at rest → row hover: lift 200ms, ping emits → leave: lift
  releases 200ms. Nothing else, ever, at any depth.
- **State matrix (v2).** *Rest:* printed rules. *Hover:* lift +
  ping. *Focus:* the Stn 4 replay link only. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* provisional rows
  dimmed + tagged. *Touch:* tap-hold lifts a row for 600ms;
  no ping (touch has no hover to answer).
- **Breakpoints (v2).** ≥1200px: full 4-column table.
  768–1199px: the "contacts heard" column folds into the
  station cell as a sub-line. <768px: stacked station list.
- **Edge cases & failure modes (v2).** *A station with no
  return at all (a real survey's dropped ping):* the row prints
  `NO RETURN` in the return cell and `—` for depth — absence is
  data and prints in full `--chart`, never dimmed into hiding.
  *Totals vs sheet drift in a CMS build:* the totals row is
  generated from the same record object as §6.17 (§15's build
  order enforces it) — a hand-typed total is a §10 failure.
  *Print:* the table is the print stylesheet's centrepiece —
  full grid, no striping, abyss on chart white inverted for
  paper.
- **Accessibility spec (v2).** Real table semantics throughout:
  caption, `scope="col"` headers, `scope="row"` station names,
  totals in `<tfoot>`. Screen readers receive the dive in its
  most native form. Contrast: `--chart` on `--abyss` 15.3:1;
  amber totals 9.2:1; the WEAK dashed underline is paired with
  the printed word WEAK — never colour alone.
- **Tokens consumed (v2).** `--abyss`, `--abyss-3`, `--chart`,
  `--pressure`, `--amber`, `--amber-deep`, `--grey-line`,
  `--ease-settle`.

### 6.15 Berth-request form & its stamped confirmation

- **What & why.** The room's conversion: a visitor requests a
  berth on the next survey. The form is styled as a page from
  the dive log — fields for name, email, and the watch they'd
  stand (a select of the sheet's three watches) — and on submit
  the confirmation is a log entry, stamped: `BERTH № 10 OF 12 ·
  SURVEY № 215`, the number derived in print from the sheet
  ("9 of 12 berths taken on Survey № 215 — yours is the tenth")
  *before* the visitor writes a word. It belongs because it is
  the one place the visitor enters the log themselves, and the
  theme's law holds: the berth number is a kept promise counted
  from the record, not a random reference string.
- **Structure.** A real `<form>` with native validation,
  enhanced never replaced: labelled inputs on `--abyss-3`,
  `--chart` text, 2px `--phosphor` focus outline plus a soft
  ping at the field's edge (§6.6's hover language on focus).
  Layout 7/5 (§4): fields left; right, the *berth ledger* — a
  printed mini-table of Survey № 215's berths from the sheet
  (12 rows: 9 `TAKEN` with watch assignments, 3 `OPEN`), so the
  visitor sees the count their number comes from. On submit,
  the form region swaps to the confirmation: a log-entry block
  on `--abyss-2` with the amber stamp (rotated −2°, a real
  stamp's imperfection), the entry line in log voice, and the
  ledger re-printed with berth 10 now `TAKEN — THIS ENTRY`.
  Without JS the form posts natively and the confirmation is a
  server-rendered page with the same entry and the next number.
- **Motion spec.** Field focus: edge ping + ground lift over
  250ms. Submit: the button fires one hard ping (amber flash,
  §6.6); the form dims to 70% over 300ms in a *recording* state
  — the button's label becomes `LOGGING…` with an unlit-dot
  pulse (§6.16's smudge language — never a spinner). Success:
  the confirmation prints in over 500ms (`--ease-settle`), the
  stamp lands at t=350ms with a 120ms scale settle (1.06 → 1.0)
  — a stamp *strikes*; it does not fade politely. Error: the
  offending field's marker is an amber asterisk (the log's
  correction mark) with the error line printed beneath in
  `--chart` — no shake, no red: this room has no red.
- **States.** Rest: printed form, ledger showing 9 taken.
  Focus: per-field ping + lift. Active (submitting): form at
  70%, fields disabled, button logging. Success: confirmation
  entry + updated ledger. Error: field marked, error printed,
  focus moved to the first error, values preserved.
  Scrolled-past: an in-flight submission completes regardless.
  Disabled (endpoint down): the form prints a log note —
  "The log is closed for this watch; requests resume at the
  next" — and holds the visitor's entries in the fields,
  unsent and unlost.
- **Content merge.** The watches in the select are the sheet's
  watches; the berth count is the sheet's count; the
  confirmation number is that count + 1; the ledger beside the
  form is the sheet's berth table. The conversion is transacted
  *inside* the record, and §10 re-derives the stamp from the
  sheet.
- **Failure fallback.** Submission watchdog at 4,000ms: no
  response → the form restores from 70%, prints "the entry
  could not be logged — your words are still here" with values
  intact; the submit carries an idempotency token so a retry
  can never double-book berth 10. No JS: native post, server
  confirmation, same numbers.
- **Reduced-motion variant.** Confirmation prints instantly;
  the stamp is present at rest rotation (no strike); errors
  print without transition. The entry is the reward, not its
  landing.
- **Performance budget & mobile variant.** Form JS ≤5 KB gz,
  deferred; the ledger is print. Mobile: single column, ledger
  *below* the fields (the promise still precedes the ask — the
  preamble line "9 of 12 taken" prints above the form at every
  breakpoint), submit full-width, targets ≥48px.
- **Choreography timeline (v2).** Focus field → ping 250ms →
  submit → hard ping, form dims 300ms → logging pulse →
  response → confirmation rises 500ms → t=350ms stamp strikes
  (120ms settle) → ledger re-prints with berth 10 taken →
  rest. Watchdog ceiling 4,000ms on the submission.
- **State matrix (v2).** *Rest:* form + ledger printed. *Hover:*
  field edge ping. *Focus:* ping + lift + outline. *Active:*
  submitting state as above. *Scrolled-past:* submission
  completes. *Disabled:* log-closed note, values held.
  *Touch:* identical; submit sticky at the form's foot within
  its own box below 768px.
- **Breakpoints (v2).** ≥1200px: 7/5 split, ledger beside.
  768–1199px: single column, ledger above the fields (compact
  4-row view: taken count + open berths listed). <768px:
  single column, preamble line + full ledger below.
- **Edge cases & failure modes (v2).** *The last berth (a build
  where the sheet says 11 taken):* the preamble and stamp
  derive from the sheet, so the form promises № 12 and, at 12
  taken, the form's rest state becomes a waitlist entry —
  `WAITLIST № 1` — derived the same way; the form never
  hardcodes its own arithmetic. *Duplicate submit (same
  visitor, same watch):* the confirmation prints with a log
  note — "second entry for this name — held as corroboration,
  berth unchanged" — the log treats agreement as evidence, not
  error. *Watch select changed after an error:* values persist;
  only the invalid field is marked.
- **Accessibility spec (v2).** Native labels, visible, `--chart`
  (15.3:1); errors via `aria-describedby` + an
  `aria-live="polite"` summary in the log's voice; the
  confirmation is an `aria-live` region announcing "Logged.
  Berth number 10 of 12, Survey 215" once. Focus management:
  error → first invalid field; success → confirmation heading.
  The stamp's rotation is decorative; its text is real text.
- **Tokens consumed (v2).** `--abyss-2`, `--abyss-3`, `--chart`,
  `--pressure`, `--phosphor`, `--amber`, `--amber-deep`,
  `--ease-settle`, `--ease-sound`, `--dur-stamp` (120ms),
  `--dur-watchdog-form` (4000ms).

---

### 6.16 Echo-smudge loader & the full-sweep transition

- **What & why.** Loading in the sonar room is unsounded water:
  regions still arriving show faint echo smudges — soft
  phosphor-faint blurs in the shape of the coming content — that
  sharpen as their data lands; and leaving a page sends one full
  sweep across the room, the new page's content phosphorescing
  behind the beam. It belongs because a spinner would be a
  machine from another world, while a smudge is exactly what a
  not-yet-resolved return looks like on a real scope. The loader
  and the transition are the same physics at two scales, as §6.6
  is at section scale.
- **Structure.** Smudge regions are DOM elements with
  `data-smudge`, styled with layered radial gradients
  (`--phosphor-faint` over `--abyss-2`) shaped by the region's
  own box — a smudge for a card is card-shaped, for a figure is
  figure-shaped; there are no grey rectangles in the room. The
  real content is in the DOM beneath (server-rendered) or
  injected complete; the smudge is a veil class removed on
  readiness. The transition is a mode of §6.1's beam drawn on
  the §6.7 overlay canvas at page scale: a phosphor wedge
  sweeping 360° over 900ms while the outgoing page dims, then
  navigation, then the incoming page's hero sweep (§8.1) picks
  up the same revolution — one continuous sounding across the
  boundary.
- **Motion spec.** Smudge pulse: the veil breathes at ±6%
  opacity on a 2.8 s sine — present, unresolved, alive.
  Sharpen on data: veil fades and the region's blur (4px → 0)
  resolves over 450ms (`--ease-settle`). **Hard ceiling: any
  region still smudged at 1,500ms prints its content anyway** —
  the room does not hold a reader hostage to a slow return.
  Transition: sweep 900ms, navigation, arrival hero sounding;
  total perceived interruption ≤2,000ms, watchdogged — the
  destination forces its lit state at 2,000ms regardless.
- **States.** Smudged (breathing veil) → sharpening → printed.
  Error (a region's data fails): the veil lifts and the region
  prints a log note — "this return did not resolve — [sound
  again]" with a real retry control; a smudge never breathes
  forever. Focus: smudged regions are `aria-hidden` and
  unfocusable until printed. Scrolled-past: regions below the
  fold resolve on arrival regardless of view. Disabled (no JS):
  no veils exist; pages are server-printed complete.
- **Content merge.** The smudge is shaped like its content and
  made of the content's own not-yet-resolved return; the
  transition's sweep is the hero scope's beam at room scale, so
  moving between pages is moving between soundings of one dive
  — the depth gauge (§6.3) does not reset its story, only its
  value, and the new page's sheet (§6.17) is the next dive's.
- **Failure fallback.** Per-region 1,500ms ceiling (print
  regardless) and the 2,000ms transition watchdog (destination
  forces lit). A failed navigation mid-sweep leaves the reader
  on the current page, lit — the sweep is a veil over a page
  that still works.
- **Reduced-motion variant.** No breathing, no sweep: smudges
  are static faint fields swapped instantly for print on data;
  transitions are plain navigations whose destination hero is
  in its lit rest state.
- **Performance budget & mobile variant.** Veils are CSS
  gradients (zero raster); the sweep is one canvas wedge on the
  shared overlay. Mobile: sweep shortens to 650ms; smudge pulse
  cut (static veils) to save battery.
- **Choreography timeline (v2).** Region requested → veil prints
  with the layout → data lands → sharpen 450ms → rest.
  Ceiling 1,500ms forces print. Transition: click → sweep
  900ms → navigate → arrival hero sounding (≤1,400ms) → lit
  page. Watchdog ceiling 2,000ms.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* veiled regions unfocusable, `aria-hidden`. *Active:*
  a submitting form region shows the smudge pulse (§6.15's
  logging state). *Scrolled-past:* pre-resolved print.
  *Disabled / no-JS:* server print, no veils. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  full, pulse period 3.2 s. <768px: static veils, 650ms sweep.
- **Edge cases & failure modes (v2).** *Data lands before the
  veil paints (warm cache):* the region prints directly — the
  best smudge is the one never seen. *Partial failure (2 of 5
  cards land):* landed cards print; unlanded hold veils until
  their own retry or the ceiling, then print their log notes
  individually — the log opens with gaps admitted. *Double
  navigation mid-sweep:* the watchdog belongs to the final
  destination; the reader lands lit, once.
- **Accessibility spec (v2).** Veiled containers carry
  `aria-busy="true"` and are removed from the accessibility tree
  until printed; one polite announcement ("Page sounded") fires
  when the last above-fold region prints — not one per region.
  The sweep is never announced. Log-note contrast: `--chart` on
  `--abyss` 15.3:1.
- **Tokens consumed (v2).** `--phosphor-faint`, `--abyss-2`,
  `--chart`, `--ease-settle`, `--dur-smudge-ceiling` (1500ms),
  `--dur-sweep-transition` (900ms),
  `--dur-watchdog-transition` (2000ms).

### 6.17 The dive sheet — the one record

- **What & why.** Every figure on the page traces to this
  record: Dive Sheet № 214 of RV *Meridian*, the descent the
  home page performs. It is specified as an element because it
  is *rendered* as one — a closing section that prints the
  sheet itself, tables and notes, so the reader can audit the
  room against its source. A theme whose numbers come from a
  document the reader can inspect is a theme that can be
  trusted; that auditability is the element.
- **Structure.** A section styled as the sheet: a header line
  (`DIVE SHEET № 214 · RV MERIDIAN · TRANSECT K-7`), then three
  printed tables and a notes block, all set from one data
  object in the build (§15) — the same object that feeds §6.1,
  §6.8, §6.9, §6.10, §6.11 and §6.14.
  **The dive.** Descent 0 → 4,800 m. Pressure rule `P = 1 +
  d/10` BAR (481 BAR at the bottom). Fathom rule `FM = M /
  1.8288`, unit flips past 1,000 m; bottom = 2,624.7 FM. Ping
  rule `I = 2.4 + 3.6 × (d/4800)` s (2.4 / 4.2 / 6.0 at 0 /
  2,400 / 4,800 m). Beam rule `B = 6.5 + 4.5 × (d/4800)` s
  (6.5 → 11 s).
  **Contacts** (scope, cards and this table print identically):

  | ID | Name | RNG (m) | BRG | Depth (m) | Return |
  |---|---|---|---|---|---|
  | A1 | WRECK | 1,240 | 038° | 212 | STRONG |
  | A2 | VENT FIELD | 2,860 | 121° | 2,512 | HARD |
  | A3 | SEAMOUNT | 3,940 | 204° | 1,860 | STRONG |
  | A4 | UNIDENTIFIED | 4,410 | 287° | — NO RETURN | WEAK |
  | A5 | CABLE | 890 | 322° | 96 | SOFT |

  **Stations** (echogram walk, sounding table and profile print
  identically): Stn 1 — 84.2 m, SOFT; Stn 2 — 312 m, SOFT; Stn 3
  — 1,140 m, STRONG; Stn 4 — 2,512 m, HARD (A2 lies at this
  station's depth); Stn 5 — 3,975 m, STRONG; Stn 6 — 4,800 m,
  WEAK; Stn 7 — 4,214 m, STRONG. Sum 17,037.2 m; **mean
  2,433.9 m**; deepest 4,800 m = the page's depth.
  **Summary block** (counting soundings, §6.10): 214 surveys
  logged (this sheet the latest); 38,200 km² mapped of the
  38,508 km² Block K — 38,200 / 38,508 = 99.2% coverage; mean
  178.5 km² per survey (38,200 / 214); deepest sounding
  10,894 m, Sheet № 167 (a fleet record — *not* this dive,
  whose bottom is 4,800 m, and the sheet says so in the same
  breath).
  **Berths.** Survey № 215 sails next; 12 berths; 9 taken
  (watches: 3 per watch across the sheet's three watches —
  FIRST / MIDDLE / MORNING); the form's confirmation is
  therefore Berth № 10 (§6.15), derived, never typed.
  **Notes.** (1) A4's depth is absent because its return
  carried none; no element may estimate it. (2) One further
  contact, distant and uncharted, was heard at the scope's rim
  during this dive and declined to be logged (§6.12); it
  appears in no table and no total. (3) Shares and coverage are
  printed as measured; the counts govern.
- **Motion spec.** The sheet section sounds like any section
  (§6.6) and then does not move. Its tables take §6.14's rest
  behaviour (row hover lift only). The one animation licensed
  here: the notes' numerals none — the sheet is the still point
  the room's motion is audited against.
- **States.** Rest: printed sheet. Hover: table row lift
  (§6.14). Focus: the sheet's one link (to the full archive,
  §7) takes standard focus. Scrolled-past: printed. Disabled:
  the sheet *is* the disabled state of the whole theme — with
  every system dead, this section still carries the entire
  dive in print.
- **Content merge.** Total: the sheet is not *about* the
  content; the content is *from* the sheet. §10's figure audit
  is a diff between this section's tables and every other
  element's printings.
- **Failure fallback.** None exists because none is needed —
  static print. If the build's data object fails to load, the
  sheet is server-rendered from the same object at build time;
  there is no runtime in which the page has figures but no
  sheet.
- **Reduced-motion variant.** Identical. The sheet was never
  animated.
- **Performance budget & mobile variant.** Static HTML; the
  contacts table stacks like §6.14's on mobile; the stations
  list prints in full (seven rows are cheap at every width).
- **Choreography timeline (v2).** Section sounds (§6.6) →
  header prints → tables print in order (dive rules, contacts,
  stations, summary, berths, notes) → rest, permanently. No
  beats follow; the sheet is where the page's choreography
  comes to be checked, not performed.
- **State matrix (v2).** *Rest:* printed. *Hover:* row lift.
  *Focus:* archive link standard. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* itself the fallback.
  *Touch:* stacked tables, all figures present.
- **Breakpoints (v2).** ≥1200px: tables side by side in pairs
  (contacts / stations), summary as a four-figure band echoing
  §6.10. 768–1199px: tables stack, summary 2×2. <768px: all
  stacked; the dive-rules block prints as a definition list.
- **Edge cases & failure modes (v2).** *A real deployment with
  a different dive:* the sheet is regenerated from the survey's
  data and every dependent element re-derives — §15's build
  order makes the record step 1 precisely so no figure can be
  typed twice. *Rounding:* depths print as the sheet states
  them (84.2 keeps its decimal; 312 does not gain one) —
  precision is data, not formatting. *The ghost in totals:*
  excluded, and the exclusion is itself printed in Note 2.
- **Accessibility spec (v2).** Real tables with captions and
  scoped headers throughout; the summary band duplicates
  §6.10's figures in text (not as a live region). The sheet is
  the most AT-complete section on the page by design — the
  audit trail is accessible first.
- **Tokens consumed (v2).** `--abyss-2`, `--chart`, `--pressure`,
  `--amber`, `--grey-line`, `--depth-max` (4800),
  `--sheet-no` (214).

### 6.18 No return — empty state & 404

- **What & why.** Where the survey finds nothing — a log search
  with no contacts, a filter with no stations, a URL that is
  not on the chart — the water returns nothing, and the page
  says so in the log's voice: `NO RETURN`, one unsounded region
  of dark water, and the way back printed as real links. It
  belongs because absence is a survey result: a sector with no
  return is recorded, not errored, and a 404 in this room is
  simply water the sheet does not cover.
- **Structure.** The empty region is a bounded area of plain
  `--abyss` (no panels, no smudge, no snow concentration — the
  overlay's snow thins to the far layer only inside it, a
  stated rendering rule: even the weather is sparse where
  nothing was found) with a centred print block: the heading
  `NO RETURN` in H2 form *without* an amber origin dot — the
  one heading on the page with no dot, because nothing here
  sounds — one line of log prose ("This water is not on Dive
  Sheet № 214. The sweep passed and the water kept its
  counsel."), and the exits: `RETURN TO THE SURFACE` (home),
  `OPEN THE LOG` (§6.9), `REQUEST A BERTH` (§6.15 — an
  uncharted visitor is a plausible recruit). The 404 is the
  full-page form; filtered-empty is the in-page form, same
  block, smaller sea.
- **Motion spec.** None, and the none is specified: no sweep
  crosses this page (the beam has nothing to strike), no ring
  fires, the snow's far layer drifts at its normal rate. The
  stillness is the message and §10 checks for it — a 404 that
  performs is a 404 that lies about being lost.
- **States.** Rest: the printed block, still water. Hover:
  exits take the standard link treatment (soft ping — the
  *links* may sound; the emptiness may not). Focus: first exit
  is the natural first tab stop after the skip link.
  Scrolled-past: n/a (the block is the page). Disabled: the
  block is plain print; there is nothing to disable.
- **Content merge.** The empty state is written from the sheet:
  it names the sheet it is absent from, its exits are the
  dive's real destinations, and its missing origin dot is a
  reference every reader of the page has already learned to
  read (§6.7). Even the void is in the room's grammar.
- **Failure fallback.** The block is static HTML with real
  links; it *is* a fallback state for other failures (§6.16's
  unresolved regions print their notes in this voice). No
  watchdog applies.
- **Reduced-motion variant.** Identical — the element is
  already still. (The one element whose reduced form needs no
  work, stated so the audit in §10 can pass it honestly.)
- **Performance budget & mobile variant.** Near zero: one
  region, no canvas duties beyond the shared snow thinning.
  Mobile: the block centres in the column; exits stack
  full-width, ≥48px targets.
- **Choreography timeline (v2).** Arrival (via §6.16's sweep on
  navigation, or directly) → the block is already printed →
  nothing happens → the reader chooses an exit → the sweep
  (§6.16) carries them back into sounded water. The timeline's
  emptiness is the spec.
- **State matrix (v2).** *Rest:* still, printed. *Hover:* exits
  ping softly; the block does not react. *Focus:* standard on
  exits. *Active:* exit navigation via §6.16. *Scrolled-past:*
  n/a. *Disabled:* plain print. *Touch:* stacked exits.
- **Breakpoints (v2).** ≥1200px: block centred in a 60vh sea.
  768–1199px: 50vh. <768px: the block fills the column; the sea
  is the spacing (§4) above and below.
- **Edge cases & failure modes (v2).** *A filter that empties
  the log grid (§6.9):* the block appears *in the grid's
  place*, keeping the section's heading and its dot — a
  filtered emptiness is a result within the dive, unlike the
  404's uncharted water, and the two forms are distinguished
  exactly by that dot. *Search with results:* the block never
  flashes during typing — it renders only on a submitted,
  resolved, empty result set. *The ghost (§6.12) is never
  offered as a 404 joke* — no "the ghost took this page" copy;
  the room's unknown is not a mascot (§9).
- **Accessibility spec (v2).** The heading is a real `<h1>` on
  the 404 page (H2 in-page); exits are real links with
  descriptive names; the block's prose is plain text. Status
  semantics: the 404 route serves a real 404 status — the
  room's honesty extends to HTTP.
- **Tokens consumed (v2).** `--abyss`, `--chart`, `--pressure`,
  `--phosphor`, `--sheet-no` (214).

---

## 7. Page application map

| Page type | How the room plays it |
|---|---|
| **Home (the dive)** | The full descent as specified: scope hero (§6.1) → log cards ≈900 m → echogram ≈1,800 m → sounding table ≈2,600 m → counting soundings ≈3,300 m → berth form ≈3,900 m → seabed footer 4,800 m (§6.11). The gauge, interval, pressure and vignette run the whole way. This is the reference build every other page is a shallower cut of. |
| **Listing (survey index)** | A fleet of sheets: each survey is a log-card row (§6.9's grammar at list scale) with its sheet number, block, and deepest station. The descent is shorter — the gauge tops at the listing's own stated depth (the shallowest survey's, printed) — because the instrument must measure *this* page (§6.3's rule), and the masthead prints that maximum so the substitution is declared, not hidden. |
| **Detail (one contact / one survey)** | A single contact gets a full sounding: its card expanded into a page — scope replay centred on its bearing (§8.2), its log prose in full, its station's row from §6.14, its figures from the sheet and no others. A4's detail page does not exist (§6.9); requesting it serves §6.18 — the room's most honest route. |
| **About (the vessel & crew)** | The room at rest: masthead, a shallow descent (gauge to the vessel's own draft story, max depth = the vessel's deepest dive, 10,894 m stated as the *ship's* record with its sheet cited), crew printed as watch lists in the sheet's format. The scope appears once, small, as the vessel's portrait — an instrument photographed, not performed (no live strikes on an about page; the watch is off). |
| **Contact / conversion** | The berth form (§6.15) is the conversion pattern everywhere it appears. A plain contact page uses the same log-entry form grammar with the entry numbered from the sheet's correspondence count — the derivation rule (§6.15's edge case) generalises; the number is always countable from a printed record. |
| **Checkout / payment** | **Refused the theme.** Money changes hands in daylight: checkout routes to a plain, bright, un-themed flow (§1's when-NOT). The room links to it with an ordinary link and does not apologise — an instrument room that tried to be a till would fail at both. |
| **Documentation / long-form** | The sounding-table pattern (§6.14) becomes the layout: tables and print, gauge replaced by a chapter depth rail (chapters as stations), reveals at their most restrained (sound on arrival, no rings beyond headings). The theme's voice (§12) suits procedures: past tense, measured, no exclamation. |
| **404 / empty** | §6.18, both forms. |
| **Print** | The dive as a chart: sheet (§6.17) + table (§6.14) + profile (§6.11), abyss inverted to paper, all motion states at rest. Print is a first-class page type in this theme because surveys are filed on paper. |

---

## 8. Worked examples

### 8.1 The hero — the first sounding (worked example 1)

*The build:* masthead (§6.13) printed; gauge rail (§6.3) at
`0 M`; the scope (§6.1) centred, headline (§6.2) at bearing
205°; lead paragraph beneath the scope; the five contact chips
in DOM order A1–A5.

*The scroll/timing timeline, from load:*

- t=0 — the room is black; the headline's print layer, the
  masthead and the gauge's surface state are already legible.
  Nothing has been hidden to make an entrance with.
- t=300ms — the beam fades in at 000° and begins its 6.5 s
  revolution (surface period). Snow is already falling (§6.12).
- t≈690ms — beam crosses 038°: A1 strikes — amber flash, ring,
  chip brightens. The visitor learns the grammar.
- t≈2,180ms / 3,680ms — A2, then A3 strike. At t≈3,700ms the
  beam crosses 205° and the headline's glow peaks — the name
  peaks a breath after the seamount struck, as §6.2 specifies.
- t≈5,180ms — A4 strikes dim (60%, short ring): the room's
  honesty, performed in the first five seconds.
- t≈5,810ms — A5 strikes. First revolution complete; all
  contacts decay to rest by t≈8,200ms.
- First scroll — the gauge leaves 0 within 120ms of the
  gesture; by 900 m the log cards' section is sounding (§6.6):
  cards return in range order at ≈510ms spacing (§6.9); the
  ping readout has lengthened to ≈3.1 s and the heading rings
  the reader can still see have slowed to match — one system,
  felt in three places.

*What the visitor feels:* they have not been shown a hero; they
have taken over a watch. The page was already at work.

### 8.2 Mid-page — the echogram and Station 4 (worked example 2)

*The build:* the console section at ≈1,800 m: heading with its
origin dot (§6.7), the echogram console (§6.8), and beneath it
a "hear the pass" replay link on the Station 4 row's behalf —
the page's one licensed replay control.

*The timeline:*

- The section crosses mid-viewport; the next ping (interval now
  ≈3.75 s at 1,800 m) releases its reveal: ring from the
  heading dot, console sharpens over 900ms.
- The waterfall is already writing (it never stopped — §6.8);
  its readout currently walks Station 3 (`SEABED 1,140 M ·
  RETURN STRONG` — printed as *below window* per §6.8's range
  rule, with the trace showing the scattering layer only; the
  console admits its window honestly).
- The reader hovers the console: the write holds, `HELD` prints
  in the readout strip. They are operating the instrument, and
  it says so.
- They activate "hear the pass — Stn 4": a focused replay — the
  console's readout prints Station 4's line (`2,512 M · HARD ·
  A2 VENT FIELD`), the scope grammar is quoted at console scale
  (one amber flash on the readout's station tag, 500ms), and
  the A2 card (§6.9) — two sections up — pulses its dot once in
  answer. Two instruments agree about one contact, in front of
  the reader. That agreement, not any single effect, is the
  premium moment this theme sells.
- Scrolling on, the readout walks to Station 5; the sounding
  table (§6.14) sounds next at ≈2,600 m, printing the same
  stations as figures — the reader has now met Station 4 three
  times (console, card, table) and the figures have never
  differed by a digit.

### 8.3 Conversion — a berth enters the log (worked example 3)

*The build:* the form section at ≈3,900 m (§6.15): preamble
("Survey № 215 — 9 of 12 berths taken. Yours will be № 10."),
fields left, berth ledger right.

*The timeline:*

- The section sounds; the ledger prints with its 9 `TAKEN`
  rows — the promise is visible before any field is touched.
- The visitor focuses the name field: edge ping, ground lift.
  They complete the form; the watch select offers the sheet's
  three watches (FIRST / MIDDLE / MORNING) and no fourth.
- Submit: hard ping at the button; the form dims to 70%;
  `LOGGING…` with the unlit-dot pulse. The ping interval at
  this depth is ≈5.3 s — the room is slow down here, and the
  submission's 4 s watchdog (§6.15) is *shorter* than a ping:
  the conversion never waits for the room's rhythm, a stated
  exception — commerce is a surface activity conducted at
  depth, and the spec says so rather than letting the visitor
  discover it.
- Response at ≈900ms: confirmation rises; at +350ms the amber
  stamp strikes — `BERTH № 10 OF 12 · SURVEY № 215` — and the
  ledger re-prints with row 10 as `TAKEN — THIS ENTRY`. The
  visitor can count the berths above theirs and verify the
  number with their own eyes. That verifiability is the
  conversion's persuasion: a room that counts honestly about
  small numbers will be believed about large ones (38,200 km²,
  §6.10).
- The gauge, throughout, has kept descending if they scroll —
  the room does not stop for the transaction; the log simply
  gains a line.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A constant ping interval.** Pings that fire every 2 s from
   surface to seabed announce that the "physics" is a CSS
   timer. *Cure:* `I(d)` from §5, sampled by §10 at three
   depths; the readout and the rings must agree.
2. **The ghost, identified.** A tooltip, card or easter-egg
   reveal naming the ghost contact converts the theme's thesis
   into a gimmick. *Cure:* §6.12's refusal is structural — the
   ghost has no sheet row, so no element *can* cite it.
3. **Amber everywhere.** Amber buttons, amber links, amber
   badges: the return colour spent on chrome until a real
   contact strike means nothing. *Cure:* the §2 amber census,
   audited per viewport.
4. **A depth gauge that lies.** Gauge max ≠ page depth, ticks
   at round numbers the sheet doesn't state, a bottom reading
   that arrives before the footer. *Cure:* §6.3's fraction
   rule and §10's bottom-state check.
5. **Blurred text the reader is trying to read.** Reveals that
   keep body copy at 40% while the reader is mid-paragraph —
   the unsounded pre-state applied above the fold or left
   unlatched. *Cure:* §6.6's fold rule, latch, and focus rule.
6. **Sonar clichés pasted on:** a green radar sweep over a
   stock photo of the sea; submarine periscope chrome; "ping"
   sound effects (the room is silent — no audio ships, ever).
   *Cure:* every visual must be an instrument or a return;
   §11 refuses the decorative components by name.
7. **Numbers that wobble.** Proportional figures in a readout,
   a counter that overshoots and settles, a pressure figure
   that disagrees with the depth by rounding. *Cure:* §3's
   mono law, §6.10's dead stop, §10's figure audit.
8. **Empty black sections.** Long scrolls of pure darkness
   "for atmosphere" with no snow, no tape progress, no
   instrument — the reader is not descending, they are lost.
   *Cure:* §4's water rule: every gap has snow in it and a
   depth being traversed.
9. **The sweep as wallpaper.** A beam animation looping behind
   unrelated content (a testimonial carousel over a scope) —
   the instrument demoted to décor. *Cure:* the scope appears
   once per page as an instrument with the sheet's contacts, or
   not at all (§7's about-page rule).
10. **Exclamation-mark copy.** "Discover the DEEP!" over a room
    whose law is measurement. *Cure:* §12's voice rules; the
    gate greps for `!` in shipped copy and fails the build.
11. **A red error state.** Form errors in red import another
    world's alarm into a room that has no red in its palette.
    *Cure:* §6.15's amber correction mark + printed words.
12. **Forced ghost appearances.** A "demo mode" or a ghost that
    arrives on a fixed 10 s loop so screenshots catch it —
    rationing is the meaning. *Cure:* §6.12's seeded schedule;
    §10 reviews the seed logic, not a stopwatch.

---

## 10. Quality gate

Blocking checks — all must pass before the theme ships in a
build. Signed by a non-builder (§15).

1. **Figure audit.** Every figure printed by §6.1, §6.8, §6.9,
   §6.10, §6.11, §6.13, §6.14 and §6.15 is diffed against
   §6.17's sheet: contacts (5), stations (7, sum 17,037.2,
   mean 2,433.9), summary (214 / 38,200 / 38,508 / 99.2 /
   178.5 / 10,894 with its Sheet № 167 attribution), berths
   (9 taken → stamp № 10). Any mismatch fails.
2. **Depth-function sampling.** At lerped depths 0 / 2,400 /
   4,800 m: ping interval reads 2.4 / 4.2 / 6.0 s; beam period
   6.5 / 8.75 / 11 s; pressure 1 / 241 / 481 BAR; masthead
   position line agrees with the gauge after unit conversion.
3. **Unit-flip check.** Crossing 1,000 m both directions:
   tumbling change fires once per crossing, lands on
   `546.8 FM` at the threshold's far side and `2,624.7 FM` at
   the bottom; no flip on resize alone.
4. **Watchdog drill.** With the observer disabled and with JS
   throttled to 10% CPU: every section is fully visible within
   6 s of arming; with JS disabled entirely, the page is
   complete at first paint.
5. **Amber census.** Per viewport at five scroll positions:
   amber appears only as struck contacts, heading dots, one
   totals/stamp, or the echogram trace. Screenshot-reviewed.
6. **Cursor grep.** No `cursor: url`, no `cursor: none`, no
   custom-cursor library in the bundle. The system pointer is
   the only pointer.
7. **Mono grep.** No digit rendered in Space Grotesk anywhere
   (computed-style audit over readout, table, counter and form
   subtrees); no bearing printed with fewer than three digits.
8. **Contrast at depth.** Text contrast measured in the
   *bottom* state (vignette 0.85, ground `--deep`): body
   ≥15:1, readouts ≥10:1, furniture ≥3.3:1 and never sole
   carrier of a figure.
9. **Ghost audit.** The ghost exists in no table, total, card
   or total count; its schedule is seeded per session with
   first appearance ≥90 s; A4 has no depth anywhere in the
   build (grep for A4 near a depth figure fails the build if
   paired).
10. **Flash audit.** No element flashes a large area; contact
    strikes are ≤6px dots + rings at ≤0.55 alpha — verified
    against photosensitivity thresholds.
11. **Reduced-motion render.** With `prefers-reduced-motion`:
    the room is fully lit and printed, gauge still reports,
    no sweep, no snow-fall, no count-up, ghost absent.
12. **Exclamation & red audit.** Zero `!` in shipped copy;
    zero red hues in the palette tokens (errors are amber +
    words, §6.15).

---

## 11. Component inventory

Every component a real site in this theme needs, with its
treatment — or its refusal and the in-room replacement.

| Component | Treatment in the room |
|---|---|
| Primary button | A *sounding order*: `--abyss-3` plate, `--chart` label in Space Grotesk, one hard ping on press (§6.6). Never amber-filled — amber is a return, not a button. |
| Secondary button | Hairline `--grey-line` plate, `--pressure`-to-`--chart` on hover; soft ping on hover. |
| Text link | `--chart` with a phosphor underline that draws 200ms on hover — a bearing line being laid. |
| Input / select / textarea | §6.15's ledger fields: `--abyss-3` ground, mono for figures, Space Grotesk for prose, amber asterisk correction mark. |
| Data table | §6.14 is the pattern: hairlines, mono figures, amber totals, WEAK dashed. |
| Card | §6.9's log card: the only card species in the room. Generic "feature cards" are refused — findings are logged, not featured. |
| Badge / tag | A *return tag*: caption mono in a hairline box (`RETURN STRONG`). Status is a measurement here, so badges print measurements. |
| Alert | A *log note*: an entry line in the log's voice on `--abyss-2`, amber mark, no icon, no red (§6.15's error pattern generalised). |
| Toast | **Refused.** Nothing floats over the water. Transient news becomes a log note inserted at the point of action, or it waits. |
| Modal | **Refused.** The room has no pop-ups; a decision that needs a surface gets a page (§7) or an in-flow panel that prints into the column. |
| Tabs | **Refused.** A dive is linear; parallel content states contradict the descent. Sequential sections with heading dots replace tabs. |
| Accordion | One licensed use: the station briefs on a detail page — a brief opens like a log page turning (height 300ms `--ease-settle`), one open at a time, all content printed in the DOM regardless. |
| Pagination | *Transect paging*: `TRANSECT 2 OF 5 · STATIONS 13–24` with prev/next bearing links — the survey continues along a line, it does not jump between "pages". |
| Breadcrumbs | A *depth line*: `SURFACE / LOG / A2 VENT FIELD` in caption mono — orientation by the dive's own structure. |
| Progress bar | **Refused** — the depth tape (§6.3) is the progress instrument. |
| Spinner | **Refused** — echo smudges (§6.16) are the loading state. |
| Tooltip | A *sounding note*: on hover/focus, a small printed line giving the figure's sheet source ("Depth as logged, Sheet № 214") — tooltips in this room cite provenance, not definitions. |
| Hero | §6.1 + §6.2, the only hero pattern. |
| Footer | §6.11, the only footer pattern — every page reaches its bottom. |
| Search | A *log search*: an input over §6.9's grid; no-match renders §6.18's in-page form. |
| Form errors | §6.15: amber asterisk + printed words + focus management. Never red, never a shake. |
| 404 / empty | §6.18. |
| Audio | **Refused absolutely.** The room is silent; no ping sounds ship. A "sound on" toggle is a §9 failure wearing a feature's clothes. |

---

## 12. Content & copywriting voice

Two registers, mirroring §3's two typefaces:

**The Room** (Space Grotesk — headlines, body, the site's
speaking voice): calm, declarative, present-tense for the
room's state, sparing. Headlines are statements of fact or
quiet claims: "We sound the water column." / "The log is the
product." Never slogans, never exclamation, never "discover /
unlock / supercharge". Body copy explains instruments plainly
and stops.

**The Log** (JetBrains Mono — readouts, labels, log lines):
past tense, third person, measured. "Contact A4 held at long
range. No depth return." "Berth № 10 logged for the MORNING
watch." The log never says "we're excited"; it says what the
water did.

**Fixed strings (verbatim, never paraphrased):**

- Gauge surface state: `0 M` — and the flip announcement:
  "Depth now in fathoms."
- Echogram admission: `SEABED BELOW WINDOW — SEE PROFILE`
- A4's depth, everywhere: `— NO RETURN`
- Ghost chip: `DISTANT · UNCHARTED` / `RNG — BEYOND SCOPE`
- Form preamble pattern: "Survey № 215 — 9 of 12 berths taken.
  Yours will be № 10."
- 404 heading: `NO RETURN`

**Error voice:** the log corrects without scolding — "the
entry could not be logged — your words are still here";
"a berth needs a watch — choose FIRST, MIDDLE or MORNING".
Errors name the fact and the remedy in one line.

**Empty voice:** §6.18's line is the template: name the sheet,
state the pass, keep the counsel. "This water is not on Dive
Sheet № 214. The sweep passed and the water kept its counsel."

**Numbers in copy** follow §3's laws in prose too: bearings
three digits, units attached, the sheet cited whenever a
figure is claimed in a sentence ("…mapped 38,200 km² of Block
K (Sheet № 214)").

✓ "Held on every pass since the second sweep."
✗ "An amazing discovery we can't wait to share!!"
✓ "No depth return."
✗ "Depth: ???"

---

## 13. Full-page scroll choreography map

The home dive, beat by beat, surface to seabed. Depths are the
lerped gauge reading at each beat; intervals are `I(d)` at
that depth.

| Beat | Depth | What the visitor sees and feels |
|---|---|---|
| 1 | 0 m | Load: printed room, beam fades in at 300ms, first revolution strikes A1→A5, headline sounds at 205°. Snow falling. Interval 2.4 s, period 6.5 s. |
| 2 | 0–200 m | First scroll: gauge wakes, tape begins to fill, masthead ground deepens at 100 m. The hero scope keeps sweeping behind the reader — the watch continues without them. |
| 3 | ≈900 m | Log cards sound on a ping: ring from the section dot, cards return in range order (A5, A1, A2, A3, A4) at ≈510ms spacing. Interval ≈3.1 s. Pressure ≈91 BAR; the vignette has begun to close. |
| 4 | ≈1,000 m | **The flip.** Mid-scroll, the gauge tumbles into fathoms — the dive's one ceremonial moment, earned by depth. Live region announces it once. |
| 5 | ≈1,800 m | Echogram console sounds; its readout walks the stations as the descent continues; a hover holds the trace (`HELD`). Interval ≈3.75 s. |
| 6 | ≈2,600 m | Sounding table sounds — and then is still. The dive's quietest beat, deliberately: figures, a dashed WEAK, no performance. |
| 7 | ≈3,300 m | Counting soundings: four drums roll 1,800ms and stop dead on the sheet. Interval ≈4.9 s; the room is audibly slower now — heading rings the reader passes fire at long, patient intervals. |
| 8 | ≈3,900 m | Berth form sounds. The ledger's 9 taken berths print; the visitor may enter the log (§8.3). Pressure ≈391 BAR; ground near `--deep`. |
| 9 | 4,800 m | The bottom: profile draws itself station by station over 2,600ms, weak span dashed, colophon prints. Gauge at `2,624.7 FM`, pressure 481 BAR, interval 6.0 s. The dive is complete and the chart proves it. |
| 10 | ascent | Scrolling up: gauge and pressure honestly reverse, the unit re-flips at 1,000 m, but nothing un-sounds — sounded sections stay lit, cards stay printed. The dive happened; only the depth is given back. |

---

## 14. Whole-page performance budget

| Budget line | Limit |
|---|---|
| Total page weight (home, first load) | ≤ 640 KB (fonts subset: Space Grotesk 400/500 + JetBrains Mono 400/500, woff2, ≤ 120 KB combined; canvas code ≤ 38 KB gz; no images on the home dive — the scope is drawn, not photographed) |
| Frame budget | ≤ 1.6 ms/frame total JS+paint on a mid-tier laptop: scope ≤0.9ms, snow ≤0.5ms, gauge/masthead writes ≤0.2ms |
| Long tasks | None > 50ms after load; the arming sequence splits across three frames |
| Concurrent animations | Beam + snow + echogram write + ≤2 sounding sections + ≤6 heading rings; hard caps in §6 |
| Layout shift | 0.00 target: all instruments reserve their boxes in print; nothing arrives and pushes text |

**The frame-time governor.** A rolling 60-frame average is
kept; if it exceeds 20ms, cuts apply in this order, silently
and reversibly: (1) snow foreground layer off; (2) snow count
halves; (3) echogram write slows to 240ms columns; (4) scope
DPR drops to 1.0; (5) heading rings cap at 2 concurrent. The
governor never cuts: the beam, the gauge, a sounding in
progress, or any printed content. A slow device gets a calmer
room, never a broken one.

**Cut order when the *weight* budget is exceeded:** the ghost
schedule (existence only — its prose note stays), the snow's
near layer, the echogram's scattering-layer drift (band prints
static), card tilt, the headline glow layer. Never cut: the
sheet (§6.17), the table (§6.14), any watchdog, the
reduced-motion variant, the unit flip.

---

## 15. Build-order checklist

1. **The record first.** Encode Dive Sheet № 214 (§6.17) as the
   build's single data object; every later step reads it.
2. Print the static page: all sections, tables, sheet, footer —
   complete and legible with no JS and no CSS animation.
3. Typography and palette tokens (§2, §3); run the mono grep
   by hand on the static render.
4. The gauge rail + masthead (§6.3, §6.13) with the shared
   loop and lerp; verify the depth functions against §5 at
   three depths.
5. The unit flip (§6.3) with its announcement; test both
   crossings.
6. Pressure + vignette (§6.5); measure contrast at the bottom
   state.
7. Ping system (§6.4) as an event source; heading rings
   (§6.7) as its first consumer.
8. Ping reveals (§6.6) with both watchdogs; run the watchdog
   drill (gate check 4) before proceeding.
9. Scope + headline (§6.1, §6.2) on the shared canvas; contact
   strikes from the record's bearings.
10. Snow + ghost (§6.12); seed the ghost schedule.
11. Echogram (§6.8) with its static plate fallback; station
    walk wired to section soundings.
12. Log cards (§6.9) and counting soundings (§6.10).
13. Sounding table (§6.14), profile + footer (§6.11), sheet
    section (§6.17) — all generated from the step-1 object.
14. Berth form (§6.15) with derived numbering and the 4 s
    watchdog; loader/transition (§6.16); 404 (§6.18).
15. Reduced-motion pass: every element's variant, verified as
    a full render, not a spot check.
16. **The gate (§10), signed by a non-builder.** No signature,
    no ship.
