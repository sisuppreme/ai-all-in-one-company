# 40. Loam & Strata — Expanded (v1 + v2)

> Expansion of theme #40 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are read top to bottom. This one is **dug**. The page is
a soil cross-section — topsoil, clay, a sand seam, chalk, bedrock —
and scrolling is excavation: the deeper the visitor goes, the older,
denser and more valuable what they find becomes. Sections are not
stacked cards; they are **strata**, full-bleed bands of earth with real
boundaries between them, and the content of each section lives inside
its stratum the way a find lives inside its layer. Objects are buried
at their true depths: a root system in the topsoil, a coin in the clay,
a fossil in the chalk. The pricing section is buried deepest of all, in
the bedrock, introduced with the theme's founding sentence: *"the good
stuff is never on the surface."*

The world is the excavation trench, treated as a complete interface
vocabulary rather than a texture. The page has a **surface** (the hero,
at ground level, where the visitor stands before digging), **strata**
(the sections, each a named geological band with a stated depth range),
**finds** (the content objects buried in the strata — cards, figures,
testimonials, prices), a **surveyor's line** (the plumb line dropped
through the hero cross-section that teaches the visitor how deep
everything is), a **depth tape** (the side instrument that counts the
dig down in centimetres), and the **bedrock** (the final stratum, where
the page's most committed content — pricing, the order form, the site
record — is cut into stone that does not move). Nothing on the page is
dirt-coloured decoration. The soil is the information architecture:
**depth is the page's argument about value**, performed by the scroll
itself.

**The theme's one law: a find's depth is a fact, or the find is not
buried.** Every buried object's stratum is determined by something true
about the content — its age, its cost, its permanence, its position in
the argument — and the mapping is printed on the page (§6.17) so a
visitor can audit it. A testimonial from last month does not sit in the
chalk beside a fossil; a flagship price does not float in the topsoil.
The depth tape's centimetres are a declared function of scroll (§6.5):
the page states its total surveyed depth and the tape counts honestly
against it. A Loam & Strata build that buries a thing at a photogenic
depth, or prints a depth figure no formula produced, has not bent the
theme — it has salted the dig, and the quality gate (§10) fails it on
sight. Everything else in this theme is craft. That one is field
ethics.

**Digging is the interaction model.** The visitor's acts are an
excavator's acts: they uncover sections with the spade (§6.2), they
brush the soil off a find to examine it (§6.8), they press a
trowel-notch into a find they want to keep (§6.12), and their depth is
always known (§6.5). The site does not have users skimming a feed; it
has diggers who understand that what is deepest took the longest to
reach and is worth the most when found. That is why the theme fits
content with a genuine gradient of depth — archives, heritage,
geology, slow-made goods, anything whose value honestly increases with
age or effort — and why it curdles around anything flat, urgent or
interchangeable.

**Best-fit sites and audiences.**

- Heritage and archaeology: museums, excavation projects, archive
  collections, historic houses — content that already thinks in layers,
  contexts and finds, where an object's stratum is a real curatorial
  fact.
- Geology, soil and land: geological surveys, soil consultancies,
  vineyards and terroir-led farms (where the strata are literally the
  product), quarries, landscape architects.
- Slow-made and aged goods: aged spirits, cellared wine, mature cheese,
  restored furniture, vintage anything — product stories where depth in
  the ground or the cellar is depth in value, stated in real years.
- Long-form brand archaeology: a company's history told as strata —
  founding artefacts in the chalk, this year's work in the topsoil —
  each layer dated and auditable.
- Education in earth science: course and exhibit pages where the
  cross-section is the curriculum and the dig is the lesson plan.

**When NOT to use it.**

- For flat content. If every item matters equally (a dashboard, a news
  index, a settings page), depth is a lie the layout tells; the strata
  become brown stripes and the theme is a costume.
- For urgent transactions. The dig is paced — sections excavate over
  800ms, the bedrock must be reached, not skipped to. A visitor paying
  a bill in forty seconds should not have to dig for the button.
- Where depth would be theatre. If the publisher cannot state, in
  writing, why each buried thing sits in its stratum, the finds are
  props. Choose another theme.
- For content that must be reordered daily. Strata are permanent by
  fiction: moving a section from clay to chalk is a geological event,
  and the build should treat it as one.
- For audiences who must never be asked to scroll far. The theme's
  whole argument is the descent; a page whose readers will only ever
  see the topsoil wastes it and misrepresents the content beneath.

## 2. Palette

Five anchors, inherited unchanged. The palette is a trench wall at
field light: four bands of earth and one of stone, read top to bottom
in the order the dig encounters them. Nothing else is admitted; every
other colour on the page is one of these five, tinted, shaded, or set
at an opacity over its own stratum.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--topsoil` | `#3B2A1E` | The surface stratum: hero band, header ground, the youngest content | ~18% of pixels | Chalk on it: **10.39:1** (AAA) — the surface band carries chalk text. Sand seam on it: 5.94:1, labels and large type only. |
| `--clay` | `#7A4E2D` | The second stratum: mid-page sections, find-card grounds, hover states | ~24% of pixels | Chalk on it: **5.40:1** (AA) — body text on clay is set in chalk, never in topsoil (1.92:1, a gate failure). Sand on clay: 3.09:1 — graphical and ≥24px display only. |
| `--sand` | `#C1A875` | The seam: thin bright band, depth-tape markings, seam highlights, find glints | ~7% of pixels | On bedrock **8.03:1** (AAA) — sand may letter the bedrock. On topsoil 5.94:1 (AA). Never a text colour on chalk (1.55:1) or on clay at body size. |
| `--chalk` | `#E8E0CC` | The pale stratum and the page's paper: deep sections, all body text on dark strata, skeleton fills | ~33% of pixels | On bedrock **14.05:1** (AAA); on topsoil 10.39:1; on clay 5.40:1. The default text colour for every dark stratum. Flint (`--flint`, below) on chalk is 2.85:1 — line-work only, never text. |
| `--bedrock` | `#17130F` | The final stratum: pricing, the order form, the footer — and the page's deepest ground | ~18% of pixels | Chalk on it 14.05:1; sand on it 8.03:1. Bedrock never moves (§4): no parallax, no drift, no entrance travel — stone is the stillness the dig ends in. |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--loam` | `#5C3B21` | Topsoil lightened toward clay: the transition band at stratum boundaries, card grounds on topsoil. Chalk on it **7.59:1** (AAA). |
| `--clay-bright` | `#9A7B52` | Clay lightened for bedrock use: seam labels and apparatus on bedrock at **4.69:1** (AA, ≥14px or bold only). |
| `--chalk-dim` | `#D8CBA6` | Chalk shaded: secondary text and captions on bedrock at **11.45:1**; on topsoil 8.31:1. |
| `--flint` | `#8A8378` | A found stone, not a soil: find outlines, disabled marks, skeleton line-work. 2.85:1 on chalk — never text, never an interactive affordance alone. |
| `--dust` | `rgba(193,168,117,.55)` | Sand at 55%: the brush-off dusting layer (§6.8) and the soil-sift grains (§6.7). Decorative only; content beneath must meet contrast with the dust removed. |

**Dark-mode behaviour: the theme does not invert — the trench is
already dark at depth.** There is no light scheme to flip to; the page
*is* a descent from a lit surface into dark ground. Under
`prefers-color-scheme: dark`, the surface stratum alone changes: the
hero is read as **the trench at dusk** — `--topsoil` deepens to
`#2A1E14`, chalk text holds (contrast rises to 12.4:1), and the
surveyor's line and depth tape switch to sand at full strength so the
instruments stay legible. Strata below the topsoil are unchanged: clay
at dusk is clay. A build that inverts the chalk stratum to a dark
ground has not made a dark mode; it has buried the page's one pale
layer, and §10 fails it.

**Pairing law.** Text is chalk on topsoil, loam, clay and bedrock;
topsoil ink on chalk; sand only on bedrock and topsoil; clay-bright
only on bedrock. Any other pairing is a build error, not a variation.

## 3. Typography

Two typefaces, inherited unchanged. **Bitter** is the field voice —
slab-serifed, weighted like a site hut's painted sign — and sets all
display, headings, stratum names and find titles. **Source Serif 4**
is the record voice and sets body text, captions, the context record
and all prose. Data (depths, ages, pH, prices) is set in Bitter with
`font-variant-numeric: tabular-nums`, never in a mono: the trench's
figures are lettered by the surveyor, not typed by a machine. There is
no third typeface and no italic display face; emphasis inside Bitter is
weight, inside Source Serif is italic.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Stratum name (section title) | Bitter 800 | 40–64px / 1.02, `clamp(2.5rem, 6vw, 4rem)` | −0.01em | Set in chalk on its stratum; the stratum's depth range is lettered beneath it in the apparatus style before any prose. |
| Display / hero title | Bitter 800 | 56–88px / 0.98 | −0.015em | The settling-soil title (§6.3). Never more than 3 lines; a title that needs 4 lines is two titles. |
| Find title | Bitter 700 | 22–28px / 1.15 | 0 | The find's name as the museum label gives it: object, material, date. |
| Heading (in-stratum) | Bitter 700 | 24–32px / 1.1 | −0.005em | One per stratum region; headings do not cross stratum boundaries. |
| Body | Source Serif 4 400 | 17–19px / 1.62 | 0 | Measure 58–66ch. On clay, 18px minimum — the 5.40:1 pairing earns AA at size, not below it. |
| Caption / context | Source Serif 4 400 italic | 14.5–15.5px / 1.5 | 0 | The context record's voice (§6.17): what the find is, where it lay, what it proves. |
| Apparatus (depths, labels, tape) | Bitter 600 | 11–13px, uppercase | +0.14em | Stratum labels, depth readings, seam names. Uppercase is rationed to apparatus only — body copy is never shouted in caps. |
| Price (bedrock) | Bitter 800 | 34–44px / 1.05, tabular | 0 | Set in sand on bedrock; the price is a find, lettered like one. |

**Type laws.**

1. **Depth is lettered before it is described.** Every stratum opens
   with its name and depth range in apparatus; prose follows. A section
   that begins with a paragraph has skipped its own survey.
2. **The deeper the stratum, the larger the rest.** Line-height grows
   with depth: topsoil body 1.55, clay 1.62, chalk 1.66, bedrock 1.7.
   Reading slows as the ground hardens; the type admits it.
3. **No centred text below the topsoil.** The surface may centre its
   title; strata are left-aligned like trench sections in a report.
   Centred body text in the bedrock is a gate failure.
4. **Figures are finds.** Any number the page asserts (depth, age, pH,
   count, price) is set in Bitter tabular and is subject to the one law
   (§1): computed by a stated formula or traceable to publisher data.
5. **Italics are for the record, not for emphasis in display.** Bitter
   never sets italic; Source Serif italic marks quotation and context.

## 4. Layout language

**The section is a stratum.** The page is one continuous trench wall:
full-bleed horizontal bands, each a stratum, stacked in geological
order — topsoil, clay, sand seam (thin, 64–120px, a marker band that
may carry a single line of apparatus), chalk, bedrock. Bands meet at
**real boundaries**: a 2px irregular edge (an SVG path or clip-path
with a surveyed, non-repeating profile, amplitude ≤6px) — never a
straight CSS border, never a wave divider borrowed from a beach theme.
The boundary profile of each stratum is authored once per build and
reused at every breakpoint; geology does not re-draw itself per screen
size.

**Depth order is content order.** Strata appear in the page in the
order the argument deepens: youngest/most provisional content in the
topsoil, the permanent and the valuable in the bedrock. The DOM order
is the stratum order is the reading order — a screen reader digs the
same trench. Reordering strata for visual variety is forbidden; if the
argument changes, the geology is re-surveyed and the change is
recorded in the context record (§6.17).

**The working margin.** On ≥1200px, the left 96px of every stratum is
the **trench edge**: a vertical zone holding the depth tape (§6.5),
stratum labels rotated −90°, and find markers. Content begins at 96px
and reads in a 1080px-max column. The trench edge is the page's
instrument panel; nothing decorative is placed there, and no content
may stray into it.

**Burial geometry.** A find sits inside its stratum with clear earth
around it: minimum 48px of stratum ground on all sides at ≥1200px,
32px below. Finds never straddle a boundary — an object half in clay
and half in chalk is a surveying error. Cards (§6.12) are cut into
their stratum like a section drawing: flat, full-bleed within their
cell, with the stratum's ground showing between them; there are no
floating rounded rectangles in the earth. Corner radius is 0
everywhere except the trowel-notch (§6.12) and the depth tape's marker
line. Stone and soil are not rounded.

**Density law.** Density decreases with depth. Topsoil sections may
run two-column and busy (it is the disturbed layer, full of recent
things); clay is one wide column with finds; chalk is sparse — one find
per screen at most; bedrock holds exactly what it must: the prices,
the form, the record. A bedrock section as dense as the topsoil has
misread its own geology.

**The bedrock does not move.** The final stratum has no parallax, no
entrance travel, no ambient motion except the seam highlight (§6.9),
which is a light, not a movement. After a page of digging, stillness
is the bedrock's content statement.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-spade` | `cubic-bezier(.7,0,.2,1)` | The spade's sweep: slow bite, fast clear, dead stop | Spade-wipe (§6.2), transitions (§6.15) |
| `--ease-settle` | `cubic-bezier(.25,.8,.3,1)` | Weighted settle: earth dropped from a short height, no bounce, ever | Cross-section assembly (§6.1), card settles, seam highlight (§6.9) |
| `--ease-sift` | `cubic-bezier(.4,.1,.6,.9)` | Granular: uneven, soft, letters and grains finding their level | Settling-soil title (§6.3), soil sift (§6.7) |
| `--ease-press` | `cubic-bezier(.5,0,.8,.4)` | The trowel press: firm in, slow release | Trowel-notch (§6.12), buttons, form submit (§6.13) |
| `--ease-draw` | `cubic-bezier(.45,0,.35,1)` | A line drawn by a steady hand: surveyor's line, root hairs | §6.1, §6.6 |

**Every motion term, translated into the trench's language:**

- **Scroll-triggered reveals** are excavations: the spade-wipe (§6.2)
  uncovers each stratum; nothing fades up out of nowhere — on this page
  things are *found*, and finding has a tool.
- **Scroll scrub** is the dig itself: the depth tape (§6.5), the
  layer-depth parallax (§6.4) and the bedrock seam highlight (§6.9) are
  pure functions of scroll position, driven by the shared loop.
- **Parallax** is stratigraphic: each find moves at its own layer's
  rate (§6.4). There is no decorative background parallax; the ground
  is the content.
- **Pinned scenes:** exactly two — the hero cross-section's surveyor's
  line sequence (§6.1) and the bedrock pricing seams (§6.9). Pinning
  anywhere else is refused: a trench is dug through, not camped in.
- **Masked reveals** are the spade-wipe and the brush-off (§6.8) — both
  masks are tools (spade, brush), both move earth off content.
- **Blur-to-sharp is refused.** A find is never blurred; it is covered
  with dust (§6.8) or still buried. Blur is a camera effect and there
  is no camera in the trench.
- **Kinetic typography is refused** except the settling-soil title
  (§6.3): letters settle 3–5px, once, at the surface. Type does not
  perform underground.
- **Counters** are field figures (§6.16): depth, soil age and pH count
  when their stratum is excavated, in Bitter tabular, stepped like a
  tape being read — and every figure obeys the one law.
- **Progress** is the depth tape (§6.5): centimetres down a surveyed
  total, printed in the legend (§6.17). There is no progress bar.
- **Marquee is refused.** Nothing in a trench runs sideways forever.
  The sand seam may carry one line of apparatus; it does not scroll it.
- **Ambient loops:** exactly two — the soil sift (§6.7) and root-hair
  sway at the topsoil boundary (§6.6). Both are sparse, slow, and cut
  first by the performance ladder (§14).
- **Micro-interactions:** the trowel-notch press (§6.12), the brush-off
  (§6.8), seam lighting (§6.9). Every interaction is a field tool.
- **Hover physics:** no magnetic pull, no tilt stages. A find under the
  brush is cleaned; a find under the pointer is lit by the seam light.
  Earth does not lean toward the visitor.
- **Page transitions** are a spade pass (§6.15): the new page is
  excavated, not faded to.
- **Smooth scrolling:** the dig has weight. The shared loop lerps
  scroll-driven values at `--lerp` 0.11; native scroll is never
  hijacked — the trench smooths its instruments, not the visitor's
  hand.
- **The shared loop law.** One `requestAnimationFrame` loop owns every
  scrubbed value (tape, parallax, seam highlight, surveyor's line).
  Lerp 0.11 for depth values, 0.14 for lights. Elements that can be
  pure CSS (assembly stagger, root growth) are; the loop writes only
  transform/opacity/custom properties, and stops writing a value when
  it settles within 0.1% of target.

**Watchdog law.** Every excavation has a timer: if the spade-wipe's
observer or the loop fails, content is uncovered by 1000ms after it
enters the viewport (§6.2). The DOM ships excavated; all covered states
exist only under a JS-armed root class. No-JS is not a degraded mode —
it is the site survey with the digging already done.


## 6. Signature elements

### 6.1 Cross-section assembly

- **What & why.** The hero is a drawn soil cross-section — the whole
  page in miniature, every stratum banded and labelled with its depth
  range — and it assembles stratum by stratum on load while a
  surveyor's plumb line drops through all the layers. It belongs
  because the cross-section is the page's table of contents and its
  contract: the visitor sees the entire dig, priced in depth, before
  taking a single step down. Every later section is one of these bands,
  at the depth this diagram states.
- **Structure.** A `<figure class="section-drawing">` in the hero: five
  horizontal bands in stratum order, each band a `<a>` (or list item)
  linking to its section, lettered with the stratum name and depth
  range in apparatus, and carrying miniature find markers at the
  positions §6.4 will bury the real finds. The surveyor's line is an
  SVG vertical path at the trench edge (x = 46px at ≥1200px) with a
  plumb-bob diamond at its end. Bands are real DOM in final position;
  the assembly transforms are JS-armed only.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 600ms timer (the line must not wait for a slow font
  to start the survey). Bands settle in stratum order — topsoil first —
  each translating 24px from above its boundary and fading 0→1 over
  520ms `--ease-settle`, staggered 180ms. At t=700ms the surveyor's
  line draws top to bottom over 1400ms `--ease-draw`; the plumb-bob
  fades in at the draw's end and the depth readout beside it counts
  0 → the page's total surveyed depth (§6.5's figure) in stepped 40ms
  increments across the same 1400ms. Total ceremony ≤2.5s; a click or
  first scroll completes it instantly.
- **States.** Assembling → surveyed (rest) → a band hovered/focused
  lifts its find markers (§6.4's glint) and the line's bob nudges to
  that band's depth. Scrolled-past: the drawing stays surveyed; it
  never re-assembles.
- **Content merge.** The drawing *is* the navigation and the depth
  legend in one object: its bands are the sections, its depths are
  §6.5's real mapping, its markers are the real finds. Remove the
  animation and the page loses nothing but the ceremony of the survey.
- **Failure fallback.** No JS: the drawing stands assembled, line drawn,
  readout printed at the total. Watchdog: any band not settled by
  1600ms is forced to rest; the line is drawn instantly if the draw
  has not started by 900ms.
- **Reduced-motion variant.** Assembled at first paint, line drawn,
  readout at total. The survey is information; only its theatre rests.
- **Performance budget & mobile variant.** Five band transforms + one
  SVG draw; no images. Mobile (<768px): the drawing compresses to a
  220px-tall strip, stagger tightens to 110ms, the line draws over
  900ms, and band labels drop their depth ranges (the tape, §6.5,
  carries depth on mobile instead).
- **Choreography timeline (v2).** t=0 fonts ready (or 600ms race lost)
  → t=0–520 topsoil settles → t=180 clay → t=360 sand seam → t=540
  chalk → t=720 bedrock, settled by t=1240 → t=700 line draw begins →
  t=2100 line complete, bob lands, readout reaches total → t=2500
  ceremony over; hero title's settle (§6.3) has run inside this window
  at its own trigger.
- **State matrix (v2).** *Rest:* surveyed drawing. *Hover (band):*
  band's markers glint sand, bob nudges (desktop only). *Focus:*
  identical to hover; the band is a link and takes the §11 focus ring.
  *Active:* navigation (§6.15 spade pass). *Scrolled-past:* surveyed,
  still. *Disabled:* a stratum with no section is absent from the
  drawing — the survey never promises a layer the page doesn't have.
  *Touch:* no hover; a tap is the link.
- **Breakpoints (v2).** ≥1200px: full drawing, 420px tall, line at
  x=46px. 768–1199px: 320px tall, stagger 150ms, line draw 1200ms.
  <768px: 220px strip as above; band tap targets ≥44px tall (bands
  compress visually but their link boxes do not).
- **Edge cases & failure modes (v2).** *A page with three strata only:*
  the drawing draws three bands and the line drops only to the third —
  the survey is of this page, not of the theme's ideal page. *Very
  long page:* total depth figure is computed from the declared mapping
  (§6.17), never from pixel height, so the readout cannot disagree
  with the tape. *Fonts fail:* the 600ms race starts the assembly in a
  fallback face; letterfit shifts are absorbed by the bands' fixed
  heights.
- **Accessibility spec (v2).** The figure carries a `<figcaption>`:
  "Section drawing of this page: five strata, surveyed depth 240
  centimetres." Bands are links with names "Clay — the finds, 60 to
  120 centimetres". The line and bob are `aria-hidden`. Focus order is
  stratum order. Band label contrast: chalk on each stratum per §2.
- **Tokens consumed (v2).** `--topsoil`, `--clay`, `--sand`, `--chalk`,
  `--bedrock`, `--ease-settle`, `--ease-draw`, `--dur-assembly` (520ms),
  `--stagger-strata` (180ms), `--dur-line` (1400ms).

### 6.2 Spade-wipe excavation

- **What & why.** Every stratum section is uncovered by a spade-wipe: a
  straight horizontal edge sweeping down across the section over 800ms,
  the earth above the edge still covering, the content below it
  exposed. It belongs because it is the theme's reveal grammar made
  literal — sections are not shown, they are *dug up*, and the wipe's
  straight edge is the spade's blade, the one honest tool-line in a
  trench. It is also the discipline that keeps the page's motion
  uniform: one reveal, everywhere, always the same tool.
- **Structure.** Each `<section class="stratum">` carries a cover layer:
  an absolutely positioned div in the *previous* stratum's colour (the
  earth being removed is the layer above), `clip-path: inset(0 0 X% 0)`
  where X is written by the shared loop or a CSS transition, with a 3px
  sand edge line at its bottom — the blade's bright edge. Content
  beneath is fully rendered at all times; the cover is the only thing
  that moves. Sections ship uncovered in the DOM; JS arms the cover
  only for sections below the fold at load.
- **Motion spec.** Trigger: section top crosses 78% of viewport height.
  The cover sweeps 0→100% over 800ms `--ease-spade`, the blade edge
  leading. One section excavates at a time; a second section entering
  during a wipe queues and starts at the first's completion or at
  +300ms overlap, whichever is sooner — a digger works one face at a
  time but does not stand idle. Sections already >50% visible at load
  are never covered.
- **States.** Buried (covered, JS-armed only) → excavating (800ms) →
  excavated (permanent; scrolling back up never re-buries — dug is
  dug). Focus entering a buried section excavates it instantly.
- **Content merge.** The cover is the previous stratum's earth and the
  wipe is the act that exposes *this* section's content — the animation
  and the content's arrival are the same event. The blade edge carries
  the section's stratum label in apparatus for the wipe's duration,
  then the label takes its permanent place at the trench edge.
- **Failure fallback.** The 1000ms law: any section still covered
  1000ms after entering the viewport is uncovered instantly, cover
  removed from the DOM. No JS: no covers exist. If the shared loop
  stalls, a per-section `setTimeout` watchdog performs the same
  uncover — `transitionend` is never trusted.
- **Reduced-motion variant.** No wipe. Sections stand excavated; the
  stratum label is simply present. The information (which layer, how
  deep) is carried by §6.5, which stills to a printed scale.
- **Performance budget & mobile variant.** One clip-path animation per
  section, compositor-only; covers are removed after excavation so the
  page's resting DOM carries no overlays. Mobile: wipe shortens to
  600ms and the queue overlap rises to 400ms — phone scrolling is fast
  and a trench that lags behind the thumb feels broken, not weighty.
- **Choreography timeline (v2).** t=0 section top crosses 78% line →
  t=0–800 cover sweeps, blade edge at section's vertical midpoint at
  t≈430 → t=800 cover removed, stratum label settles at the trench
  edge (120ms `--ease-settle`) → queued next section begins at t=800
  or earlier per the overlap rule.
- **State matrix (v2).** *Rest (excavated):* section open, label at
  edge. *Hover:* none — the wipe is not a control. *Focus:* focus
  inside an excavating section completes its wipe instantly.
  *Active:* n/a. *Scrolled-past:* excavated, cover gone. *Disabled /
  no-JS:* excavated. *Touch:* identical timings at the mobile values.
- **Breakpoints (v2).** ≥1200px: 800ms, label rides the blade.
  768–1199px: 700ms. <768px: 600ms, label does not ride (it is printed
  at the section head instead — a phone trench has no margin to ride
  in).
- **Edge cases & failure modes (v2).** *Fast fling to page bottom:*
  every section passed is uncovered instantly (the catch-up rule: a
  section >50% above the viewport centre is excavated without
  ceremony). *Section taller than 300vh:* the wipe uncovers the first
  viewport-height of it and the remainder is simply present — the spade
  opens the face, it does not perform the whole stratum. *Anchor jump
  into a buried section:* target and everything above it excavate
  instantly on arrival. *Resize during a wipe:* the wipe completes at
  its current percentage against the new height; covers are
  percentage-based so no jump occurs.
- **Accessibility spec (v2).** The cover is `aria-hidden` and never
  removes content from the accessibility tree — the DOM is complete
  under it, so screen-reader order is stratum order regardless of the
  visual state. Excavation is never announced. Focus is never moved by
  a wipe. Contrast: the blade's label is sand on the previous stratum
  (≥5.94:1 per §2 pairings) for its 800ms life.
- **Tokens consumed (v2).** `--ease-spade`, `--dur-excavate` (800ms),
  `--sand` (blade edge), `--dur-fallback` (1000ms), the previous
  stratum's colour token.

### 6.3 Settling-soil title

- **What & why.** The hero title's letters sift down 3–5px and settle,
  staggered from the last letter back to the first, like soil finding
  its level after the spade lifts it. It belongs because it is the
  theme's only kinetic type, placed at the surface where kinetic type
  is licensed (§5), and because it teaches the page's physics in one
  gesture: on this site, things settle downward, granularly, and stay
  settled. The last letter moves first — soil settles from the far edge
  of the spade's throw.
- **Structure.** The `<h1>` text is split by JS into per-letter spans
  (`aria-hidden` clones over an intact, screen-reader-only full title —
  or, preferred, the real text remains and spans are presentational
  with the heading's accessible name set explicitly). Each span carries
  a custom property `--drop` of 3, 4 or 5px, assigned by a fixed
  pseudo-random table seeded by letter index (deterministic across
  builds — two builders produce the same settle). The no-JS heading is
  plain set type.
- **Motion spec.** Trigger: the cross-section assembly's topsoil band
  settling (§6.1), or 500ms after load if §6.1 is absent. Each letter
  translates from `−var(--drop)` to 0 over 480ms `--ease-sift`,
  staggered 26ms per letter **from last to first**. Opacity never
  changes — settling soil is visible throughout its fall. Runs once;
  a repeat visit in the same session (sessionStorage) shows the title
  already settled.
- **States.** Unsettled (JS-armed, ≤500ms) → settling (480ms + stagger)
  → settled (permanent). Hover/focus: none — the title is not a
  control and does not perform for pointers.
- **Content merge.** The letters are the headline itself, behaving as
  the material the headline names. The settle is inseparable from the
  words: remove the words and there is nothing to settle.
- **Failure fallback.** Letters are at rest in the DOM; JS lifts them
  only when it can animate them, and a 900ms watchdog forces rest.
  A letter can never be stranded mid-air: the transform's end state is
  the DOM state.
- **Reduced-motion variant.** The title is simply set. No lift, no
  stagger.
- **Performance budget & mobile variant.** ≤60 letter transforms, one
  pass, compositor-only. Mobile: drop range narrows to 2–3px and
  stagger to 18ms — a phone's title is shorter and its settle should
  be quicker, not grander.
- **Choreography timeline (v2).** t=0 trigger → last letter begins →
  each earlier letter +26ms → a 20-letter title's first letter lands
  at t≈480+19×26 ≈ 975ms → all settled; the hero's surveyor's line
  (§6.1) is mid-draw as the title comes to rest — the surface settles
  while the survey begins.
- **State matrix (v2).** *Rest:* settled type. *Hover:* none. *Focus:*
  none (heading is not focusable by default; if it carries
  `tabindex="-1"` as a skip target, focus does not unsettle it).
  *Active:* n/a. *Scrolled-past:* settled. *Disabled / no-JS:* set
  type. *Touch:* identical, at mobile values.
- **Breakpoints (v2).** ≥1200px: drops 3–5px, stagger 26ms.
  768–1199px: drops 3–4px, stagger 22ms. <768px: drops 2–3px, stagger
  18ms; titles wrapping to 3 lines settle per line, last line first.
- **Edge cases & failure modes (v2).** *Very long title (>60 letters):*
  stagger compresses to keep total ≤1400ms (stagger = 900/letters) —
  the ceremony never outlasts the assembly. *Title with a find-word in
  sand colour:* coloured letters settle identically; colour is paint,
  not physics. *Font swap mid-settle:* letters are spans with fixed
  line-height; a late font may shift widths but transforms are
  vertical only, so nothing collides.
- **Accessibility spec (v2).** The heading's accessible name is the
  full title, read once, in order — the letter spans are
  `aria-hidden="true"` and the real string is provided via visually
  hidden text or `aria-label` on the `<h1>`. The settle is decorative
  and unannounced. Contrast: title in chalk on topsoil, 10.39:1, at
  every frame (opacity never dips).
- **Tokens consumed (v2).** `--ease-sift`, `--dur-settle-letter`
  (480ms), `--stagger-letter` (26ms), `--drop-max` (5px).

### 6.4 Layer-depth parallax

- **What & why.** Buried objects — the coin in the clay, the root in
  the topsoil, the fossil in the chalk — drift against their stratum at
  rates proportional to their layer's depth, so scrolling feels like
  the trench wall sliding past in geological layers: shallow finds move
  most, deep finds barely move, the bedrock not at all. It belongs
  because it makes depth *felt* rather than merely stated: the visitor's
  hand learns the strata by how reluctantly each layer gives them up.
- **Structure.** Each find element carries `data-depth` — its stratum's
  rate from the fixed table: topsoil 0.14, loam boundary 0.10, clay
  0.08, sand seam 0.05, chalk 0.03, bedrock 0. The shared loop writes
  `transform: translateY(calc(var(--p) * rate))` where `--p` is the
  section's travel through the viewport in px, clamped so a find never
  translates more than ±28px (topsoil) down to ±6px (chalk) — a find
  must stay inside its stratum (§4 burial geometry) at every scroll
  position; the clamp is computed from the find's clear earth, not
  guessed.
- **Motion spec.** Continuous scrub via the shared loop, lerp 0.11.
  No trigger, no easing curve — depth is a function of position.
  Scrolling up reverses exactly; there is no ratchet, because the wall
  slides both ways even though the dig (§6.2) does not un-dig.
- **States.** In-stratum (always) — the only variable is offset.
  Hover on a find suspends its drift (the brush, §6.8, needs a still
  object); focus does the same. Off-screen finds are not written.
- **Content merge.** The moving things are the finds themselves, inside
  their own strata, at their own layers' rates. The effect has no
  existence apart from the content's burial: unbury the finds and the
  parallax has nothing to move.
- **Failure fallback.** Finds sit at offset 0 in the DOM. Loop failure
  leaves a correct, static trench. A 1200ms watchdog clears any offset
  that would strand a find across a boundary (belt to the clamp's
  braces).
- **Reduced-motion variant.** No drift. Finds rest in their strata;
  depth is carried by the tape (§6.5) and the labels.
- **Performance budget & mobile variant.** Transform writes only, on
  finds within ±1 viewport, capped at 12 active finds per frame.
  Mobile: rates halve and clamps halve (a phone's trench is narrow;
  a 28px drift would push finds into boundaries), and chalk/bedrock
  finds do not drift at all.
- **Choreography timeline (v2).** Spatial map: find enters viewport
  bottom at offset −clamp → crosses centre at offset 0 → exits top at
  +clamp, symmetric in both scroll directions, at its stratum's rate.
- **State matrix (v2).** *Rest (centred):* offset 0. *Hover:* drift
  suspended at current offset, brush-off (§6.8) runs. *Focus:* drift
  suspended; offset eases to 0 over 200ms so a keyboard user reads a
  still find. *Active:* §6.12's notch press, offset held. *Scrolled-
  past:* offset at clamp, unwritten until re-entry. *Disabled:* a find
  that is a disabled control rests at offset 0. *Touch:* no hover
  suspension; drift at mobile rates.
- **Breakpoints (v2).** ≥1200px: full rate table, clamps 28/20/14/6px
  (topsoil/clay/sand/chalk). 768–1199px: rates ×0.7, clamps ×0.7.
  <768px: rates ×0.5, chalk static, bedrock always static.
- **Edge cases & failure modes (v2).** *Find near a stratum boundary:*
  its clamp is its own clear earth (distance to boundary minus 8px),
  which may be 0 — a find buried against a boundary does not drift,
  and the build records why in the context record. *Two finds in one
  stratum:* both take the stratum rate; relative positions never
  change, so finds cannot collide. *Short stratum (less than one
  viewport):* travel is small, offsets stay small — the math is
  proportional, nothing special-cased. *Loop throttled (background
  tab):* on return, offsets snap to mapped values; no catch-up sweep.
- **Accessibility spec (v2).** Purely positional; reading order and
  focus order are DOM order, unaffected by offsets. A find's offset
  never moves it over text (burial geometry + clamps). The drift is
  disabled under reduced motion and suspended on focus, so a focused
  find is always still and fully inside its stratum.
- **Tokens consumed (v2).** `--rate-topsoil` (0.14), `--rate-clay`
  (0.08), `--rate-sand` (0.05), `--rate-chalk` (0.03), `--lerp` (0.11),
  `--drift-max` (28px).

### 6.5 Depth tape

- **What & why.** A surveyor's tape fixed at the trench edge counts the
  dig down in centimetres: tick marks scroll past a fixed marker line
  and the readout states the visitor's current depth against the page's
  total surveyed depth. It belongs because it is the theme's progress
  indicator made of the theme's own instrument — progress here is not a
  percentage of a bar but a depth in the ground, and the tape makes the
  page's central metaphor continuously, quietly measurable.
- **Structure.** A fixed rail inside the trench edge (§4): an inner
  strip of tick marks (SVG, generated from the declared mapping: one
  tick per 10cm, a long tick and numeral per 50cm) translated by the
  shared loop so the tick under the marker line is the current depth;
  a 2px sand marker line at 50% viewport height; and a readout in
  apparatus — "DEPTH 137 CM / 240" — updated at 10cm boundaries only.
  The mapping is declared in §6.17's legend: total page scroll travel
  maps linearly to the page's stated surveyed depth (a build-chosen
  figure, e.g. 240cm for a five-stratum page, printed in §6.1's
  caption and the legend — the same figure everywhere, or the gate
  fails).
- **Motion spec.** Scrubbed, lerp 0.11, in the shared loop. The tick
  strip translates continuously; the readout changes only when the
  depth crosses a 10cm boundary (a readout that flickers every pixel
  is an instrument no surveyor would trust). At total depth the tape
  stops and the readout gains its full stop: "DEPTH 240 CM / 240 —
  BEDROCK."
- **States.** At surface (0cm) → descending (scrubbed) → at bedrock
  (terminal reading). The tape never counts upward past a depth
  already reached in the readout's *session maximum* line ("DEEPEST
  212 CM") — a dig remembers its deepest point even when the visitor
  climbs back up, though the live reading follows position honestly.
- **Content merge.** The tape measures the page itself: its total is
  the cross-section's total (§6.1), its boundaries are the strata's
  boundaries (long ticks are lettered with stratum names as they pass
  the marker), and reaching bedrock on the tape is reaching the pricing
  in fact. It is the dig's own instrument, not a widget beside it.
- **Failure fallback.** No JS: the tape renders as a static printed
  scale in the trench edge — all strata lettered with their depth
  ranges at their positions, readout absent, information intact. Loop
  failure freezes the tape at its last true reading; it never shows a
  depth the scroll hasn't reached.
- **Reduced-motion variant.** The tape is printed as the static scale
  (the fallback above) with the current stratum highlighted as the
  reader passes it — position without motion.
- **Performance budget & mobile variant.** One transform on the tick
  strip + a text write at 10cm boundaries. Mobile (<768px): the rail
  leaves the edge and becomes a 3px sand line at the viewport's left
  with the readout as a small apparatus chip at top-left, updating at
  10cm boundaries — the instrument survives, miniaturised; the tick
  strip is not rendered on mobile at all.
- **Choreography timeline (v2).** Spatial: scroll 0 → 0cm at marker →
  each stratum boundary crosses the marker exactly as its section's
  boundary crosses 50% viewport height (the mapping is calibrated to
  this, §15 step 9) → total scroll → total depth, "BEDROCK" reading.
- **State matrix (v2).** *Rest at a position:* tape holds its reading.
  *Hover:* none — the tape is not a control. *Focus:* none.
  *Active:* clicking a stratum name on the static scale (mobile chip
  excluded) navigates to that stratum (§6.10's index shares this duty
  on desktop). *Scrolled-past:* n/a — the tape is fixed. *Disabled:*
  the tape is never disabled; without JS it is the printed scale.
  *Touch:* the chip is informational only, not a target.
- **Breakpoints (v2).** ≥1200px: full rail in the 96px trench edge,
  tick strip + readout + deepest line. 768–1199px: rail narrows to
  56px; ticks remain, stratum names on long ticks drop (readout
  carries names). <768px: the 3px line + chip described above.
- **Edge cases & failure modes (v2).** *Short page (one stratum):*
  the tape still maps honestly; the readout's total is that stratum's
  depth and "BEDROCK" is not claimed unless the page ends in bedrock.
  *Anchor jump to the footer:* the tape snaps to the mapped depth on
  the next frame — instruments don't perform for teleporting diggers.
  *Declared depth vs. real strata:* if a build adds a section without
  re-surveying the total, tape and cross-section disagree — §10's
  three-records check (drawing, tape, legend) catches it as a blocking
  failure.
- **Accessibility spec (v2).** The tape is `aria-hidden` as an
  instrument; its information is duplicated accessibly: each stratum
  section carries its depth range in its heading apparatus (§3 law 1),
  and the navigation (§6.10) lists strata with depths as real text.
  The readout is not a live region — depth is ambience, not alerts.
- **Tokens consumed (v2).** `--sand`, `--chalk`, `--ease-settle` (chip
  changes), `--lerp` (0.11), `--tape-total` (declared per build),
  `--tick-cm` (10cm step).


### 6.6 Root-hair growth

- **What & why.** From the topsoil band's lower boundary, root hairs —
  fine SVG filaments with finer branches — grow downward into the clay
  when the topsoil section is excavated, each drawing over 400–900ms,
  staggered. It belongs because the topsoil is the page's one living
  layer, and the roots are how the surface content literally feeds the
  depths: they grow from the topsoil's own plants (its headings, its
  hero image) into the stratum below, stitching the first boundary with
  biology instead of a line. A trench whose top layer is alive and
  whose depths are mineral teaches the whole theme in one edge.
- **Structure.** An SVG layer straddling the topsoil/clay boundary,
  full width, 90px tall, `pointer-events: none`, holding 14–22 root
  paths. Each root originates at a real topsoil element's bottom edge
  (a heading's baseline, a card's foot — positions measured at build or
  first layout, never scattered decoratively) and descends 40–90px
  with 2–4 branch hairs. Paths ship drawn (dashoffset 0); JS arms the
  undrawn state only if the boundary is below the fold.
- **Motion spec.** Trigger: the topsoil section's excavation (§6.2)
  completing. Each root draws via stroke-dashoffset over its own
  duration (400–900ms, assigned by root length: 10ms per px of path,
  clamped), `--ease-draw`, staggered 70ms in left-to-right reading
  order. After drawing, roots sway: a ±1.5px horizontal drift at the
  tips on a 7s sine, phase-offset per root — the theme's second ambient
  loop (§5), and the only motion permitted to cross a stratum boundary.
- **States.** Undrawn (JS-armed) → growing (≤900ms + stagger) → grown
  (swaying, terminal). Scrolling away never ungrows them; roots, once
  grown, are part of the section drawing.
- **Content merge.** Every root hangs from a real element of the
  topsoil's content and reaches toward the clay's first find — the
  growth connects two pieces of content across the boundary. A root
  from nothing to nothing is a decoration and is forbidden at the gate.
- **Failure fallback.** Roots ship drawn; no-JS shows the grown
  boundary. If SVG is unavailable the boundary falls back to §4's
  authored edge profile — the strata still meet honestly.
- **Reduced-motion variant.** Roots pre-drawn, no sway. The boundary
  reads as a printed section drawing.
- **Performance budget & mobile variant.** ≤22 path draws once + a
  transform on one SVG group for sway (tips move via a single
  skew/translate on the layer, not per-path animation). Mobile: root
  count caps at 10, sway is cut (first on the §14 ladder after the
  sift), lengths shorten to 30–60px.
- **Choreography timeline (v2).** t=0 topsoil excavation completes →
  t=0 first root begins → +70ms per root → longest root (900ms) plus
  last stagger (21×70=1470ms) bounds the ceremony at ≈2.4s worst case,
  typical ≈1.4s → sway begins per root as each finishes drawing.
- **State matrix (v2).** *Rest:* grown, swaying. *Hover:* none — roots
  are not controls and do not react. *Focus:* none. *Active:* n/a.
  *Scrolled-past:* grown; sway pauses off-screen (IntersectionObserver
  toggles the layer's animation). *Disabled / no-JS:* drawn.
  *Touch:* identical; sway at mobile ruling (cut).
- **Breakpoints (v2).** ≥1200px: 14–22 roots, 90px layer.
  768–1199px: 12–16 roots, 70px layer. <768px: ≤10 roots, 54px layer,
  no sway.
- **Edge cases & failure modes (v2).** *Topsoil section is the whole
  page (single-stratum build):* roots grow into the footer boundary
  instead, from the section's elements toward the bedrock footer — the
  stitch still connects content to content. *Topsoil content reflows
  (late image):* root origins are re-measured on the layout pass
  (§15 step 11) and paths redrawn instantly, not re-grown. *Boundary
  near the fold at load:* roots ship grown (the JS-arming rule only
  applies below the fold).
- **Accessibility spec (v2).** The layer is `aria-hidden`, decorative
  in the strict sense: it carries no information the headings and
  labels don't state. It never overlaps text (it lives in the 90px
  boundary zone, which §4 reserves). Sway is disabled under reduced
  motion and pauses off-screen.
- **Tokens consumed (v2).** `--ease-draw`, `--dur-root-min` (400ms),
  `--dur-root-max` (900ms), `--stagger-root` (70ms), `--topsoil`,
  `--clay`.

### 6.7 Soil sift

- **What & why.** Fine particles — 6–10 grains — occasionally sift from
  a section's top edge and fall slowly through its first 120px,
  dissolving into the stratum below. It belongs because a trench is
  never perfectly still: the band above sheds its material onto the
  band below, and that small, sparse untidiness is what keeps the
  cross-section from looking laminated. It is the theme's first ambient
  loop (§5) and its most rationed: sift too often and the dig becomes
  a snow globe.
- **Structure.** Per section, a canvas-free DOM layer of ≤10 grain
  spans (`--dust` colour, 2–3px, border-radius 50%) absolutely
  positioned at the section's top edge, `pointer-events: none`,
  created by JS only (no-JS pages have no loose soil — correct, they
  are printed surveys). Grains spawn at the boundary's high points —
  the authored edge profile's peaks (§4) — never at random x positions
  over text.
- **Motion spec.** A section sifts at random intervals of 9–20s while
  it is in the viewport, one fall per interval: grains release in a
  loose cluster (stagger 0–300ms), fall 90–120px over 2400–3600ms
  `--ease-sift` with a ±6px horizontal wander, fading out across the
  last 30% of the fall. Maximum one section sifting at any moment
  across the page; the scheduler is a single timer owned by the shared
  loop's housekeeping, not per-section timers.
- **States.** Quiescent (long) → sifting (≤3.6s) → quiescent. Paused
  entirely when the tab is hidden, the section is off-screen, or any
  modal/form interaction is open above the section.
- **Content merge.** The grains are the section's own stratum colour,
  shed from its own boundary peaks onto its own content's ground —
  the earth of the layer above, arriving where gravity says. Spawn
  points avoid text columns (grains fall in the trench edge and the
  inter-card ground), so the sift soils the section's margins, never
  its sentences.
- **Failure fallback.** No JS: no grains, nothing missing. Loop
  failure: the scheduler dies with the loop and the page is a still
  trench — the correct failure for an ambience.
- **Reduced-motion variant.** None. The sift never runs under reduced
  motion; it is the theme's purest ambient and the first thing the
  preference exists to still.
- **Performance budget & mobile variant.** ≤10 tiny transforms, one
  section at a time, ≤3.6s per ~15s — under 0.1ms/frame amortised.
  Mobile: falls shorten to 60–80px, grains cap at 6, intervals widen
  to 14–26s. The sift is cut first on the §14 ladder, before every
  other motion in the theme.
- **Choreography timeline (v2).** Continuous, sparse: interval 9–20s
  (randomised per cycle, seeded per section so two sections never
  synchronise) → release cluster over 300ms → fall 2.4–3.6s → grains
  dissolved → next interval.
- **State matrix (v2).** *Rest:* quiescent. *Hover:* a sift in progress
  over a hovered card is not interrupted (grains are above the dust
  layer's business, §6.8, and pass behind cards' content zones by
  spawn rule). *Focus:* sifting never targets the focused section's
  reading column. *Active:* n/a. *Scrolled-past:* scheduler skips
  off-screen sections. *Disabled:* no-JS / reduced-motion — never runs.
  *Touch:* mobile values above.
- **Breakpoints (v2).** ≥1200px: 6–10 grains, fall 90–120px.
  768–1199px: 6–8 grains, fall 80–100px. <768px: ≤6 grains, fall
  60–80px, intervals 14–26s.
- **Edge cases & failure modes (v2).** *Photosensitivity:* grains are
  2–3px at 55% sand opacity falling at ≤50px/s — orders of magnitude
  below any flash or motion threshold; the spec's slowness is a safety
  property. *Many sections in view (short page, tall screen):* the
  one-at-a-time rule holds globally. *Battery saver:* the scheduler
  checks `document.visibilityState` and viewport presence only; on
  low-power signals (§14) the sift is the first cut.
- **Accessibility spec (v2).** Grains are `aria-hidden`, carry no
  information, and never fall over the reading column. Fully disabled
  under `prefers-reduced-motion`.
- **Tokens consumed (v2).** `--dust`, `--ease-sift`, `--sift-fall`
  (2400–3600ms), `--sift-interval` (9–20s).

### 6.8 Brush-off hover

- **What & why.** A find-card rests under a dusting of its stratum's
  soil — a `--dust` layer softening its image and figures — and
  hovering (or focusing) it brushes the dust off: a mask sweeps across
  over 450ms and the content beneath stands sharp, the way an excavator
  brushes a coin before reading its date. It belongs because examining
  a find *is* cleaning it; the hover state is not a highlight borrowed
  from UI convention but the archaeologist's actual gesture, and the
  sharpened state is the find's true face, which is why focus gets it
  too.
- **Structure.** Each find-card (§6.12) carries a dust layer: an
  absolutely positioned overlay in the stratum's colour at 55% with a
  soft noise background (SVG feTurbulence data-URI, opacity 0.5),
  masked by a linear gradient whose position is a custom property
  written on hover/focus. Beneath it, the card's content is complete
  and sharp in the DOM — the dust never holds the only copy of
  anything, and text is never under dust at rest for longer than the
  card is unexamined: **figures and titles sit above the dust layer**;
  only the find's image/plate and its context lines are dusted.
- **Motion spec.** Trigger: pointerenter or focus-within. The mask
  sweeps left→right (in LTR) over 450ms `--ease-settle`; the dust's
  opacity falls 0.55→0.08 across the same sweep — a trace of dust
  always remains at the card's edges, because a brushed find is
  cleaned, not sterilised. On leave/blur, the dust returns slowly:
  1400ms `--ease-sift`, the soil settling back — the asymmetry (fast
  clean, slow re-dust) is the gesture's honesty.
- **States.** Dusted (rest) → brushing (450ms) → brushed (held while
  hovered/focused) → re-dusting (1400ms) → dusted. Touch: first tap
  brushes (and does not activate the card's link); second tap
  activates — the find is examined before it is taken.
- **Content merge.** The dust is the card's own stratum, lying on the
  card's own find; the brush reveals the find itself, sharper. Nothing
  is revealed that is not the card's content — no tooltip, no overlay
  text, no second face.
- **Failure fallback.** No JS / no hover: cards may ship brushed
  (dust at 0.08) — a build for a touch-only context sets dust to its
  trace level permanently. The dust layer is enhancement; its absence
  is a clean card.
- **Reduced-motion variant.** No sweep: dust toggles between 0.55 and
  0.08 instantly on hover/focus. The information (this find, examined)
  survives; the gesture rests.
- **Performance budget & mobile variant.** One mask-position/opacity
  animation per card, compositor-only. Mobile: tap-driven as above;
  re-dust shortens to 900ms (a phone's finds are re-covered faster
  because the thumb has moved on).
- **Choreography timeline (v2).** t=0 pointerenter → t=0–450 mask
  sweeps, dust 0.55→0.08 → hold brushed → pointer leaves → t=0–1400
  dust resettles to 0.55, edges first (the gradient reverses its bias).
- **State matrix (v2).** *Rest:* dusted (image/context at dust 0.55;
  title and figures always clear). *Hover:* brushed. *Focus:* brushed
  — keyboard parity is non-negotiable. *Active (press):* §6.12's notch
  press runs on the brushed card. *Scrolled-past:* dusted; a card
  mid-re-dust off-screen completes instantly. *Disabled:* a disabled
  find-card (e.g. a sold find) stays dusted at 0.7 and does not brush —
  it is no longer examinable, and its label says why. *Touch:*
  tap-to-brush as above.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: sweep 400ms.
  <768px: tap-driven, sweep 350ms, re-dust 900ms.
- **Edge cases & failure modes (v2).** *Pointer skims a grid of finds:*
  a 70ms intent delay before brushing, so a diagonal path doesn't
  brush six finds in passing; leaving within the delay cancels.
  *Card under dust contains the only copy of a figure:* forbidden by
  structure (figures sit above dust) and checked at §10. *Rapid
  hover cycling:* the sweep restarts from its current value, never
  queues. *Print:* dust prints at trace level; finds print readable.
- **Accessibility spec (v2).** The dust is presentational: the card's
  text is in the accessibility tree at full value at all times, and
  contrast is audited in the *dusted* state for the context lines
  (chalk-dim on clay under 55% dust still ≥4.5:1, verified per build)
  and in the brushed state for everything. Focus brushing guarantees
  keyboard users the same sharp find sighted users get.
- **Tokens consumed (v2).** `--dust`, `--ease-settle`, `--ease-sift`,
  `--dur-brush` (450ms), `--dur-redust` (1400ms), the stratum colour
  token.

### 6.9 Bedrock seam highlight

- **What & why.** The bedrock pricing section pins, and as the visitor
  scrolls through the pin, its three seams — the bands within the
  bedrock where the three price rows are cut — light in turn, each
  seam's sand edge brightening as its row becomes the one being read.
  It belongs because pricing is the deepest find and must be *reached*,
  not merely displayed: the pin is the effort, the seams are the
  strata within the stone, and the highlight is the surveyor's lamp
  moving down the face as the visitor commits to reading what things
  cost down here.
- **Structure.** A `<section class="stratum bedrock pricing">` of
  260vh: a sticky 100vh stage holding the three price rows, each row
  set in its own seam — a horizontal band with a 2px sand top edge (at
  25% strength at rest) and the row's content: plan name (Bitter 700),
  price (§3's price style), its context line, and its action (§6.13's
  form is the destination; each row's button scrolls to or opens it).
  Scrub value `q` = progress through the 260vh. Seam boundaries at
  q=0.33 and q=0.66, with the active seam's edge at full sand and a
  `--sand` wash at 8% over its band.
- **Motion spec.** Scrubbed via the shared loop, lerp 0.14 (lights
  respond faster than depths). Seam activation is a function of q with
  a 0.04 hysteresis band at each boundary so the lamp doesn't flicker
  on a boundary line. Edge brightening transitions over 240ms
  `--ease-settle` once q crosses — scrubbed position, eased light.
  Scrolling up reverses exactly: the lamp climbs back.
- **States.** Seam 1 lit (q<0.33) → seam 2 (0.33–0.66) → seam 3
  (q>0.66) → pin releases into the footer (§6.14) with all seams at
  rest strength — the lamp is put down when the reading is done.
  A row hovered/focused lights its own seam regardless of q (the
  visitor's lamp, not the scroll's).
- **Content merge.** The seams are the price rows' own bands and the
  light reads the row the visitor is reading — the highlight is the
  act of attention, drawn in the stone the prices are cut into. There
  is no separate pricing UI to decorate; the seams are the pricing.
- **Failure fallback.** No JS: no pin; the three rows stack in the
  bedrock in order, seams at rest strength, prices fully legible —
  the printed bedrock. Loop failure mid-pin: the pin is CSS sticky
  (it holds), all seams light to a uniform 60% so no row sits dark.
- **Reduced-motion variant.** No pin, no scrub: the stacked rows of
  the fallback, each seam's edge at 60% — lit evenly, like a museum
  case. Nothing about the prices is motion-gated.
- **Performance budget & mobile variant.** One scrubbed value, three
  opacity/edge writes. Mobile (<768px): the pin is **cut** — a 260vh
  pin on a phone traps the thumb; rows stack, and each row's seam
  lights as the row crosses 55% viewport height (IntersectionObserver,
  one-shot per pass, reversible). The bedrock keeps its argument
  (deepest, lit as read) at phone scale.
- **Choreography timeline (v2).** Spatial: q=0 pin engages, seam 1 lit
  → q=0.33 lamp crosses to seam 2 (240ms brighten) → q=0.66 seam 3 →
  q=1 pin releases, lamp rests → footer. Reverse scroll replays the
  crossings upward with the same hysteresis.
- **State matrix (v2).** *Rest (stacked / pre-pin):* seams at 25%.
  *Hover (row):* its seam to full, others hold scroll state. *Focus:*
  same as hover; focus also scrolls the pin so the focused row's seam
  is the lit one (the lamp follows the reader). *Active:* row button
  press — §6.13. *Scrolled-past:* seams at rest, pin gone.
  *Disabled:* a sold-out row's seam never lights; its price is struck
  in flint and its context line says when it was cut. *Touch:* mobile
  ruling above.
- **Breakpoints (v2).** ≥1200px: full pin, 260vh, rows side-by-side
  within the stage (three seams as vertical bands is forbidden — seams
  are horizontal, geology is horizontal). 768–1199px: pin 220vh, rows
  stacked inside the stage. <768px: no pin (above).
- **Edge cases & failure modes (v2).** *Only two price rows:* two
  seams, boundaries at q=0.5 — the spec generalises; a third empty
  seam is never drawn to complete a pattern. *A fourth row:* the
  bedrock holds at most three seams; a fourth price belongs to a
  second bedrock section or the build is re-surveyed — density law
  (§4). *Jump-scroll into the pin's middle:* q is positional, the
  correct seam lights on the next frame. *Sticky unsupported:* rows
  stack (the fallback) — the section degrades to print, never to a
  trap.
- **Accessibility spec (v2).** Price rows are ordinary sections in DOM
  order; the pin is visual only and never changes focus order. The lit
  seam is not the only signal of the current row — each row's heading
  is a real heading, and on focus the row's seam lights (above), so
  state is never colour-alone for the reader who matters. Prices meet
  §2 (sand on bedrock 8.03:1) in every seam state, including unlit
  (the wash only ever adds light).
- **Tokens consumed (v2).** `--bedrock`, `--sand`, `--ease-settle`,
  `--dur-seam` (240ms), `--lerp-light` (0.14), `--pin-pricing` (260vh).


### Page-family elements

### 6.10 Strata index navigation (page family: navigation)

- **What & why.** Navigation in this theme is the trench's index: a
  miniature cross-section — a vertical stack of thin stratum bands in
  the header, each band a link to its section, lettered with the
  stratum name and its depth range. It belongs because a dig is
  navigated by depth, not by menu: the visitor chooses *how deep to
  go*, and the index is the section drawing (§6.1) reduced to an
  instrument. The band for the stratum currently being read fills with
  its colour at full strength; the rest sit at 45% — you are here,
  measured in earth.
- **Structure.** A `<nav class="strata-index">` in the header: a
  horizontal strip of band segments on ≥1200px (strata are horizontal;
  the index is a section drawing laid flat), each segment an `<a>`
  with stratum name + depth range in apparatus. Current-stratum
  tracking via IntersectionObserver on the sections. On mobile the
  index becomes a "Strata" disclosure button opening a vertical list —
  the one place the theme permits a menu, because a phone has no
  trench edge to hold an index.
- **Motion spec.** Current band fills over 200ms `--ease-settle` as
  its stratum becomes current; hover/focus on a band raises it to 75%
  strength and letters its depth range in sand. Navigation runs §6.15's
  spade pass. No sliding indicators, no underlines that travel — bands
  fill, like sections of a drawing being inked.
- **States.** Bands: unvisited (45%) → current (100% + sand depth
  figures) → visited (70%, a permanent record — the index remembers
  the dig). The header itself is not sticky below the topsoil: once
  the visitor is underground, the depth tape (§6.5) is the instrument
  and the header scrolls away like the surface it is.
- **Content merge.** The index's bands are the page's actual strata
  with their actual depths — generated from the same survey data as
  §6.1 and §6.17. Add a stratum and the index gains a band, because
  the index *is* the survey, not a hand-maintained menu.
- **Failure fallback.** A plain list of anchor links with depths as
  text. Scrollspy is the only JS behaviour; without it all bands sit
  at 70% and the first is marked current by the server where known.
- **Reduced-motion variant.** Fills are instant; the disclosure opens
  without animation.
- **Performance budget & mobile variant.** Observer-driven, negligible.
  Mobile: disclosure list, bands full-width rows ≥48px, depths always
  visible (a phone index that hides depths has hidden the point).
- **Choreography timeline (v2).** Stratum change: outgoing band drains
  100→70% over 200ms as the incoming fills 45/70→100% — the two
  overlap for one beat, like passes of the lamp.
- **State matrix (v2).** *Rest:* per visited state above. *Hover:*
  75% + sand depths. *Focus:* same as hover, plus the §11 focus ring.
  *Active/current:* 100%, `aria-current="true"`. *Scrolled-past:* the
  header is gone with the surface; state persists in the tape.
  *Disabled:* a stratum with no section is absent. *Touch:* disclosure
  rows behave as links; no hover state.
- **Breakpoints (v2).** ≥1200px: horizontal band strip in the header.
  768–1199px: strip wraps to two rows; depth ranges shorten to start
  depth only ("60–"). <768px: disclosure button + vertical list.
- **Edge cases & failure modes (v2).** *More than six strata:* the
  strip shows first-level strata only; sub-sections are indexed inside
  their stratum by §6.17's record. *Single-stratum page:* no index —
  a one-layer dig has no depths to choose between. *Long stratum
  names:* names truncate at 16ch on the strip with the full name in
  the mobile list and `aria-label`.
- **Accessibility spec (v2).** Real `<nav aria-label="Strata of this
  page">`; current band carries `aria-current`; depths are text, not
  colour. Focus order is stratum order. The mobile disclosure is a
  `<button aria-expanded>`; Esc closes it and returns focus.
- **Tokens consumed (v2).** The five stratum tokens, `--sand`,
  `--ease-settle`, `--dur-fill` (200ms).

### 6.11 The surface hero composition (page family: hero)

- **What & why.** §6.1 specifies the drawing; this element specifies
  the first screen it lives in: the surface — topsoil ground, the
  settling title (§6.3), one line of apparatus stating the surveyed
  depth and the number of strata, the section drawing, and a single
  invitation to begin: a "Begin the dig" link styled as the surveyor's
  first marker. Nothing else competes. The hero's job is to stand the
  visitor on undisturbed ground and show them the whole trench before
  they disturb it.
- **Structure.** A 100vh (min 640px) topsoil section: title (≤3 lines),
  apparatus line ("SURVEYED DEPTH 240 CM · FIVE STRATA · THREE FINDS
  BURIED" — every figure from the survey data), the §6.1 drawing at
  its foot, and the begin link anchored to the first stratum. The
  surface carries the site's name and §6.10's index in its header
  zone; no other chrome.
- **Motion spec.** On load: the title settles (§6.3), the drawing
  assembles (§6.1). The begin link's marker — a small sand diamond —
  pulses once at t=2600ms (scale 1→1.25→1, 600ms `--ease-settle`) when
  the assembly completes, then never again: the surface invites once,
  it does not nag.
- **States.** Composing (≤2.5s) → surveyed (rest). Scrolled-past: the
  surface is gone; §6.5's tape has inherited its duties.
- **Content merge.** Every element of the hero is the page's own survey
  data: the title names the site, the apparatus counts its real strata
  and finds, the drawing maps them. A hero figure that doesn't match
  the page below is a §10 blocking failure (three-records check).
- **Failure fallback.** Static surface: set title, assembled drawing,
  printed apparatus. The begin link is a plain anchor.
- **Reduced-motion variant.** Everything at rest; no pulse.
- **Performance budget & mobile variant.** The hero's whole budget is
  §6.1 + §6.3. Mobile: 92vh, title at the 40px floor of its clamp, the
  drawing as §6.1's strip, apparatus wraps to two lines.
- **Choreography timeline (v2).** t=0 load → title settles (≤975ms) ∥
  drawing assembles (≤2500ms) → t=2600 marker pulse → rest.
- **State matrix (v2).** *Rest:* surveyed surface. *Hover:* begin link
  per §11 link treatment; drawing bands per §6.1. *Focus:* same.
  *Active:* begin → smooth descent to stratum one (native scroll,
  loop-smoothed instruments). *Scrolled-past:* gone. *Disabled:*
  static surface. *Touch:* no pulse change; tap targets ≥48px.
- **Breakpoints (v2).** ≥1200px: 100vh, drawing 420px. 768–1199px:
  96vh, drawing 320px. <768px: 92vh, drawing strip 220px, apparatus
  two lines.
- **Edge cases & failure modes (v2).** *Short viewport (<600px tall):*
  the hero releases its 100vh claim and flows — the drawing must
  never push the first stratum's label below a scroll-and-a-half.
  *Returning visitor:* title and drawing at rest (§6.3's session rule;
  §6.1 assembles only on first view per session).
- **Accessibility spec (v2).** Landmarks: header, then `<main>` opening
  with the `<h1>`. The apparatus line is real text. The begin link's
  name is "Begin the dig — to the topsoil" (destination named, not
  "click here").
- **Tokens consumed (v2).** `--topsoil`, `--chalk`, `--sand`,
  `--ease-settle`.

### 6.12 Find cards & the trowel-notch (page family: cards / listing)

- **What & why.** The card in this theme is a find as the museum tray
  holds it: a flat cell cut into its stratum, the find's plate (image
  or drawn object), its name, its context line (§6.17), and — in the
  corner — the place where a trowel-notch will go. Clicking the notch
  presses a small triangular mark into the corner (the excavator's way
  of saying *this one, keep*) and files the find into the visitor's
  finds tray (§6.17). It belongs because a listing in a trench is not
  a grid of products; it is a tray of things dug up, each examinable
  (§6.8) and each markable by hand.
- **Structure.** `<article class="find">`: plate zone (the object,
  dusted per §6.8), name (Bitter 700), context line (Source Serif
  italic: layer, depth, one true sentence), figure row (the find's key
  datum in Bitter tabular), and the notch button — a 44px corner
  target with a triangular outline that fills with sand when pressed.
  The whole card is never one link; the name links to the find's record
  (§6.17), the notch is its own button.
- **Motion spec.** Entry: the card is excavated with its stratum
  (§6.2); it has no separate entrance. Notch press: the triangle scales
  1.3→1 over 160ms `--ease-press` with the card's corner darkening 8%
  (the pressed earth), and the finds-tray count (§6.17) increments with
  a 200ms sand flash. Un-pressing reverses over 240ms `--ease-settle`.
  Hover runs §6.8's brush.
- **States.** Dusted (§6.8) → brushed → notched (triangle filled,
  corner pressed, card gains a 2px sand left edge — the tray's way of
  showing kept finds at a glance) → un-notched. A find already in the
  tray survives navigation (local state, like §6.17's record).
- **Content merge.** The card is the find: its plate is the object, its
  context is its provenance, its notch is the visitor's act upon it.
  The notch marks *this* card's corner — pressed into its earth, not
  floated over it.
- **Failure fallback.** Static card, notch as a plain toggle button
  with text state ("Kept" / "Keep this find") for no-JS form posts.
- **Reduced-motion variant.** Notch toggles instantly; the corner
  darkening is instant; the tray flash is omitted.
- **Performance budget & mobile variant.** Transforms on one small
  element. Mobile: cards stack one per row in chalk and clay (the
  sparse strata), two per row in topsoil only; notch target stays
  44px.
- **Choreography timeline (v2).** t=0 notch click → t=0–160 triangle
  presses, corner darkens → t=160 tray count updates, sand flash
  200ms → card rests notched with its sand edge.
- **State matrix (v2).** *Rest:* dusted, un-notched. *Hover:* brushed
  (§6.8). *Focus:* brushed; notch button takes the focus ring.
  *Active:* press (above). *Scrolled-past:* state persists (notch and
  dust as left). *Disabled:* a withdrawn find (sold, removed) keeps
  its card as a record — notch disabled, context line states the
  withdrawal and its date. *Touch:* first tap brushes, notch is a
  direct target.
- **Breakpoints (v2).** ≥1200px: finds in their stratum's column grid
  (topsoil 3-up, clay 2-up, chalk 1-up per §4 density). 768–1199px:
  2-up / 2-up / 1-up. <768px: 1-up everywhere except topsoil 2-up at
  ≥480px width.
- **Edge cases & failure modes (v2).** *Find with no plate:* the plate
  zone carries the find's drawn section glyph (a simple SVG of its
  layer position) — never a grey box, never a stock photo of somebody
  else's dig. *Very long context line:* clamps at 3 lines; the full
  context lives in the record (§6.17), which the name links to.
  *Tray state lost (storage blocked):* notches work for the session
  and the card says nothing about persistence it can't promise.
- **Accessibility spec (v2).** The notch button's name is "Keep this
  find: [name]" / "Remove from your finds: [name]", with
  `aria-pressed`. The sand edge is never the only kept-signal — the
  button's text state and the tray count carry it too. Card contrast
  per §2 in dusted and brushed states (§6.8's audit).
- **Tokens consumed (v2).** `--sand`, `--ease-press`, `--ease-settle`,
  `--dur-notch` (160ms), the stratum token.

### 6.13 The bedrock order form (page family: forms / conversion)

- **What & why.** Conversion in this theme happens in the bedrock,
  because that is where the page keeps what it values most: the form
  is a face cut into the stone — ruled fields like inscription lines,
  labels in apparatus, and a submit that is *cut*, not clicked: the
  button presses into the bedrock and the confirmation is a newly cut
  seam in the section, lettered with the order's real reference. It
  belongs because a form reached by digging the whole page has earned
  its gravity; treating it like a topsoil signup would betray the
  descent.
- **Structure.** A `<form class="bedrock-form">` inside the bedrock
  section, below the seams (§6.9): fields as inscription lines
  (transparent ground, 2px chalk-dim bottom rule, Bitter 600 apparatus
  labels above, Source Serif 19px input text in chalk), one consent
  line drawn as an unfilled seam box that fills with sand and a bedrock
  tick when checked, and the submit as a cut block: bedrock ground,
  2px sand edge, apparatus text "CUT THE ORDER". Success replaces the
  form with the confirmation seam: a band whose sand edge draws across
  (§6.9's grammar) lettered with the reference and the record line.
- **Motion spec.** Focus: the field's rule brightens chalk-dim→chalk
  and a sand hairline slides in beneath it from the left (180ms
  `--ease-settle`) — the line being inscribed is lit. Error: the rule
  turns the theme's one error colour — clay-bright at full strength on
  bedrock (4.69:1, apparatus size only) — and the error note letters in
  beneath in the record voice (§12), persistent until corrected.
  Submit press: the block presses 2px with its edge darkening (140ms
  `--ease-press`); on success the confirmation seam's edge draws over
  500ms `--ease-draw` and the reference stamps (scale 1.15→1, 160ms).
- **States.** Rest → focused (lit rule) → error (clay-bright rule +
  note) → submitting (block pressed, form inert at full contrast) →
  confirmed (form replaced by the seam). The visitor's entries are
  never cleared by an error, including a server failure: the failure
  note (§12) appears above the form and the form stands as written.
- **Content merge.** The form's fields are the order's own facts (which
  seam's offer, whose name, where to send the record); the confirmation
  is cut into the same bedrock the prices are cut into, with a
  reference drawn from the order system — the conversion becomes part
  of the section's geology.
- **Failure fallback.** A working HTML form posting without JS;
  server-rendered errors in the same notes. The submit is a real
  `<button type="submit">` with its text label visible — the cut-block
  styling decorates a real control, never replaces it.
- **Reduced-motion variant.** No slide, no draw, no stamp: rules change
  colour instantly, the confirmation seam appears complete.
- **Performance budget & mobile variant.** Transitions on focus/submit
  only. Mobile: fields full-width, inputs at 19px (also prevents iOS
  zoom), the submit block full-width at 56px tall — in the bedrock, a
  thumb presses stone.
- **Choreography timeline (v2).** Focus: t=0 rule brightens, hairline
  slides by t=180. Submit: t=0 press → t=140 release → response →
  confirmation edge draws 500ms → reference stamps at t≈660.
- **State matrix (v2).** *Rest:* ruled lines at chalk-dim. *Hover:*
  submit edge warms to full sand. *Focus:* lit rule + hairline (every
  field shows focus visibly — audited §10). *Active:* press.
  *Scrolled-past:* entries persist. *Disabled (submitting):* fields
  disabled at full contrast — labels and text stay chalk; only the
  submit dims. *Touch:* same states, 48px field rows.
- **Breakpoints (v2).** ≥1200px: form in the bedrock's measure, two
  short fields (name / direction) sharing one line-pair. 768–1199px:
  one column. <768px: one column, 19px inputs, full-width submit.
- **Edge cases & failure modes (v2).** *Network failure on submit:*
  the form stands as written; the note reads per §12 ("NOT CUT — THE
  STONE REFUSED. YOUR WORDS ARE KEPT ABOVE.") and the submit
  un-presses. *Double submit:* the pressed state disables until
  resolution. *Autofill:* filled fields take the focused rule colour
  so the visitor can see what the browser inscribed for them.
- **Accessibility spec (v2).** Real `<label>` per field; hints are
  `aria-describedby`, never placeholders (a blank inscription line is
  the invitation). Errors are linked via `aria-describedby` and
  summarised in a polite live region on failed submit only. Contrast:
  labels chalk on bedrock 14.05:1; error text clay-bright 4.69:1 at
  apparatus size (≥13px bold-equivalent) — body-size error prose is
  set in chalk with only the rule in clay-bright.
- **Tokens consumed (v2).** `--bedrock`, `--chalk`, `--chalk-dim`,
  `--sand`, `--clay-bright`, `--ease-settle`, `--ease-press`,
  `--ease-draw`.

### 6.14 Bedrock footer — the site record (page family: footer)

- **What & why.** The page ends in bedrock, and the footer is the site
  record cut into it: who surveyed this page, when, what it contains
  and its surveyed depth — set as the last seam of the bedrock, beneath
  a final sand edge line. It belongs because a dig ends with a record,
  not a link farm: the footer's facts are the excavation's own (strata
  count, finds count, total depth — all from the survey data), and its
  stillness is the theme's last statement. There are no link columns in
  the stone; there is the record, and the way back up (§6.10).
- **Structure.** A `<footer>` inside the bedrock: the sand edge line
  (2px, at 60%), the record block in apparatus and record voice —
  surveyor/publisher name, the page's title, "SURVEYED [real date]",
  the counts line ("FIVE STRATA · THREE FINDS · 240 CM") — legal links
  as plain chalk links in one row, and a single "Back to the surface"
  link whose arrow is a drawn plumb line reversed.
- **Motion spec.** One motion only: the sand edge line draws across
  (dashoffset, 600ms `--ease-draw`) when the footer enters at 85%
  viewport height — the last line the surveyor draws. Nothing else in
  the footer ever moves; the sift (§6.7) does not reach the bedrock.
- **States.** Rest (line drawn or drawing once) → still, permanently.
- **Content merge.** The counts are the page's real counts (the same
  survey data as §6.1, §6.5, §6.10 — the three-records check includes
  the footer as a fourth). The record is the dig's paperwork, filed
  where paperwork survives: in stone.
- **Failure fallback.** Static line, static record. Nothing to fail.
- **Reduced-motion variant.** Line pre-drawn.
- **Performance budget & mobile variant.** One 600ms draw, once.
  Mobile: the record stacks; counts line wraps; the line still draws.
- **Choreography timeline (v2).** t=0 footer crosses 85% line →
  t=0–600 edge draws → stillness.
- **State matrix (v2).** *Rest:* record. *Hover/focus:* links per §11.
  *Active:* "Back to the surface" scrolls to the hero (native, with
  the tape unwinding honestly as position changes). *Scrolled-past:*
  n/a — it is the bottom. *Disabled:* line rendered drawn.
  *Touch:* links ≥44px rows.
- **Breakpoints (v2).** All sizes: record in the bedrock measure.
  <768px: legal row wraps to two lines; counts stay on one line
  (they shrink to 11px apparatus before they wrap — the counts are
  one fact and are not split).
- **Edge cases & failure modes (v2).** *Counts change after a content
  edit:* the footer is generated from the survey data, so it cannot
  drift from §6.1 — a hand-edited footer is a §10 failure. *Multi-page
  sites:* each page's footer records that page's survey; the bedrock
  is per-page geology.
- **Accessibility spec (v2).** A real `<footer>` with the record as
  text; the drawn line is `aria-hidden`. The back-to-surface link is
  named for its destination.
- **Tokens consumed (v2).** `--bedrock`, `--sand`, `--chalk`,
  `--chalk-dim`, `--ease-draw`.

### 6.15 Excavated skeleton + spade page transition (page family: loader / transition)

- **What & why.** The theme's two state-change rituals share one tool.
  **Loading** shows the unexcavated section: the stratum's band present
  at full geometry, its content zone covered by its own earth (a flat
  fill of the stratum colour at 92% with the section's label lettered
  in apparatus — "CLAY — DIGGING") which the spade (§6.2) removes when
  content lands. **Navigation** is a single spade pass: a full-viewport
  sheet of topsoil sweeps down over 500ms, the route changes at full
  cover, and the new page's own spade uncovers it. Both belong because
  waiting and travelling, in a trench, are digging problems, and a
  spinner or a fade would be foreign machinery.
- **Structure.** Skeleton: the real section markup with a cover in the
  §6.2 construction, plus the label. Transition: a fixed
  `.spade-sheet` (topsoil ground, 3px sand bottom edge — the blade)
  parked above the viewport; on navigation it translates down over
  500ms `--ease-spade`, route swaps at full cover, sheet continues
  down and off (second 400ms) revealing the new page already excavated
  (its sections do not re-run §6.2 after a transition — a dug page is
  a dug page).
- **Motion spec.** Skeleton: content landing triggers §6.2's wipe
  (800ms); hard cap — any skeleton still covered at 1200ms has its
  cover stripped and content shown plainly (the standing rule: no
  section stays buried because machinery failed). Transition: 500ms
  cover + swap + 400ms reveal; a 1100ms watchdog tears the sheet down
  and shows the destination if anything stalls.
- **States.** Skeleton: covered → excavating → excavated; covered →
  stripped (1200ms) → plain. Transition: idle → covering → covered
  (swap) → revealing → idle. Browser back/forward: no sheet — the
  browser's gesture rules.
- **Content merge.** The skeleton's cover is the section's own earth
  over its own geometry — zero layout shift by construction. The
  transition sheet is the surface's topsoil: you leave every page by
  being covered with the ground you started on, and arrive by digging.
- **Failure fallback.** Skeletons exist only inside client-side fetches
  that own their watchdog; server-rendered pages ship excavated.
  Transition enhances interceptable links only — middle-click, new
  tab, modified clicks and external links bypass it entirely; without
  JS, navigation is ordinary.
- **Reduced-motion variant.** Skeleton: plain stratum-colour block, no
  label animation, content appears at 120ms opacity. Transition: no
  sheet; instant navigation with the §6.10 index's current band
  flashing its fill once (200ms) to mark the change of ground.
- **Performance budget & mobile variant.** Covers are one clip-path
  each; the sheet is one transform. Mobile: transition shortens to
  400+300ms; skeleton label shortens to the stratum name alone.
- **Choreography timeline (v2).** Transition: t=0 sheet descends →
  t=500 full cover, swap, scroll to top → t=900 sheet exits, new
  surface stands surveyed → t=1100 watchdog deadline (teardown if
  incomplete).
- **State matrix (v2).** *Rest:* no sheet, sections excavated.
  *Hover:* links show §11 hover; the sheet has no hover. *Focus:*
  keyboard-activated links run the same transition; focus lands on
  the destination's `<h1>` at reveal. *Active:* covering/revealing.
  *Scrolled-past:* n/a. *Disabled / no-JS:* plain navigation, no
  skeletons left covered. *Touch:* mobile timings.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: 450+350ms.
  <768px: 400+300ms, sheet's edge 2px.
- **Edge cases & failure modes (v2).** *Slow destination:* the sheet
  holds at full cover with its blade edge pulsing sand 25→60% (the
  dig is working) up to 3s, then retreats upward (300ms) and native
  loading proceeds — the theme never traps a visitor inside a
  transition. *Same-page anchors:* no sheet; §6.2/§6.10 handle the
  descent. *Fetch error into a skeleton:* the section resolves into
  §11's alert treatment with the error in §12's voice — a section
  reports its own failed dig.
- **Accessibility spec (v2).** During transition the outgoing page is
  `inert` from cover start; at reveal, focus moves to the new `<h1>`
  (tabindex −1) with a polite announcement "Dug to: [page name]".
  Skeletons carry `aria-busy="true"` until excavated; the region
  announces "This stratum is still being dug" once, not per section.
- **Tokens consumed (v2).** `--topsoil`, `--sand`, `--ease-spade`,
  `--dur-sheet` (500ms), `--dur-skeleton-cap` (1200ms).

### 6.16 Field figures — depth, age & pH counters (page family: data)

- **What & why.** The page's numbers — surveyed depth, soil age in
  years, pH, find counts — count up when their stratum is excavated,
  in Bitter tabular figures, stepped like readings being taken. It
  belongs because in the field, a figure is a measurement, and a
  measurement arrives by being taken: the count *is* the instrument
  working. It is also the element most exposed to the one law (§1):
  every figure counted to is a figure the publisher must be able to
  source, and the count's choreography never invents precision the
  source doesn't have (a soil age of "about 400 years" counts to 400
  and is lettered "≈400", the approximation printed, not hidden).
- **Structure.** `<span class="field-figure" data-value data-unit
  data-source>`: the final value is the DOM text; JS replaces it with
  the count only when it can animate. Figures sit in their stratum's
  figure row or inside find cards (§6.12) — never floating in chrome.
  `data-source` names the provenance ("site survey 2026", "lab report
  14 March") and is printed in §6.17's legend.
- **Motion spec.** Trigger: the figure's section completing §6.2's
  excavation. Count over 900ms, in 30 stepped increments (30ms steps —
  a tape read in steps, not a slot machine), `--ease-settle` applied
  to the step sizes (large strides first, fine steps at the reading).
  Decimals: pH counts to one decimal and lands exactly; the final step
  is always the true value, held for 120ms before the count is
  declared done (the surveyor reads it twice).
- **States.** Printed (DOM) → counting (900ms) → read (permanent).
  Re-entering the viewport never recounts — a measurement is taken
  once.
- **Content merge.** The figures are the content's own data, counted
  in place, in their stratum. Remove the count and the number remains,
  printed — the animation is the taking of the reading, not the
  reading itself.
- **Failure fallback.** DOM value stands; no-JS shows every figure
  read. A figure whose source cannot be named is not counted and not
  printed — it is omitted, per the one law.
- **Reduced-motion variant.** Figures stand read. No count.
- **Performance budget & mobile variant.** Text writes at 30ms steps
  on ≤6 figures concurrently — negligible. Mobile: count shortens to
  700ms, 24 steps.
- **Choreography timeline (v2).** t=0 excavation completes → t=0–900
  30 steps, strides shrinking → t=900 true value lands → t=1020 held
  reading confirmed → rest.
- **State matrix (v2).** *Rest:* read value. *Hover:* none. *Focus:*
  a focused figure (if inside a link/card) is shown read instantly.
  *Active:* n/a. *Scrolled-past:* read. *Disabled:* n/a. *Touch:*
  mobile timing.
- **Breakpoints (v2).** ≥1200px: 900ms/30 steps. 768–1199px: 800ms/28.
  <768px: 700ms/24.
- **Edge cases & failure modes (v2).** *Figure is zero:* counts
  nothing; a measured zero is lettered "0 — none found", which is a
  finding, not an absence. *Huge figures (soil age 11,700):* steps are
  proportional; grouping separators are present from the first step so
  the figure never changes width class mid-count. *Approximate
  figures:* the ≈ is part of the DOM text and present throughout the
  count.
- **Accessibility spec (v2).** The counting span is `aria-hidden`
  during the count with the final value available to AT from the
  start (visually-hidden twin) — screen readers hear the reading, not
  the taking. Tabular figures prevent layout shift.
- **Tokens consumed (v2).** `--ease-settle`, `--dur-count` (900ms),
  `--count-steps` (30).

### 6.17 The finds tray & context record (page family: trust / record)

- **What & why.** Two linked instruments of honesty. The **context
  record** is a printed table — in the chalk stratum and repeated in
  the legend zone before the bedrock — listing every find on the page:
  its name, its stratum, its depth range, and the one true sentence
  that justifies its burial (§1's law, made auditable). The **finds
  tray** is the visitor's own collection: the finds they notched
  (§6.12), held in a tray that slides from the trench edge, each entry
  with its context line and a link back to where it lies. Together they
  are the theme's trust layer: the page shows its workings, and the
  visitor's keepsakes are kept with their provenance attached.
- **Structure.** Record: a `<table class="context-record">` (real
  table semantics) with columns Find / Stratum / Depth / Why it lies
  there, set in Source Serif with apparatus headers, plus the depth
  mapping declaration ("This page is surveyed to 240 cm. Scroll maps
  linearly to depth; the tape (§6.5) reads the same survey."). Tray: a
  `<aside>` drawer from the right on desktop, a bottom sheet on
  mobile, listing notched finds from local state; the tray button
  lives in the header and carries the count (§6.12's increments land
  here).
- **Motion spec.** The record is print: it does not animate, ever —
  records are not performed. The tray opens with a 380ms
  `--ease-settle` slide (it is a tray being pulled from the trench
  bench) and closes in 300ms; entries settle in with a 40ms stagger.
  The tray count in the header flashes sand (§6.12) when an entry is
  added — the only motion the record system permits itself.
- **States.** Record: static. Tray: closed → opening → open → closing.
  Empty tray: shows the empty voice (§12) and one line explaining the
  notch — an empty tray is a true state, drawn honestly.
- **Content merge.** The record's rows are generated from the same
  survey data as every other instrument; the tray's entries are the
  page's real finds with their real contexts. Neither contains a word
  that isn't true of the page it sits on.
- **Failure fallback.** The record is a static table — no fallback
  needed. The tray without JS becomes a plain section listing the
  finds (notch state unavailable, and the tray says so in §12's voice
  rather than pretending).
- **Reduced-motion variant.** Tray opens instantly; no stagger, no
  flash.
- **Performance budget & mobile variant.** One slide transform.
  Mobile: bottom sheet at 70vh max, entries full-width.
- **Choreography timeline (v2).** Tray open: t=0 slide begins →
  t=380 open, entries settled by t=380+40×n → focus moves to the
  tray's heading. Close reverses at 300ms, focus returns to the tray
  button.
- **State matrix (v2).** *Rest:* record printed; tray closed with its
  count. *Hover:* tray button per §11. *Focus:* tray is a dialog —
  focus trapped while open, Esc closes. *Active:* notch presses
  (§6.12) update the tray live if open. *Scrolled-past:* n/a (fixed
  instruments). *Disabled:* a withdrawn find's tray entry remains,
  marked withdrawn with its date — the tray does not quietly drop
  history. *Touch:* bottom sheet, swipe-down or close button.
- **Breakpoints (v2).** ≥1200px: right drawer 400px. 768–1199px:
  drawer 340px. <768px: bottom sheet; the record table scrolls
  horizontally inside its stratum rather than compressing below
  legibility.
- **Edge cases & failure modes (v2).** *A find in the tray is removed
  from the page by a content update:* its entry persists marked "no
  longer in the ground — record kept", because a tray that silently
  loses a find teaches the visitor their keeping doesn't count.
  *Record vs. page disagreement:* impossible by construction
  (generated from one survey object) and checked by §10 regardless.
- **Accessibility spec (v2).** The record is a real `<table>` with
  `<th scope>` headers — the audit must be auditable by everyone. The
  tray is `role="dialog" aria-modal="true"` with a labelled heading;
  its count is announced politely when it changes while the tray is
  closed ("Two finds in your tray").
- **Tokens consumed (v2).** `--chalk`, `--sand`, `--ease-settle`,
  `--dur-tray` (380ms).

### 6.18 The undisturbed page (page family: 404 / empty state)

- **What & why.** A wrong address in this theme is undisturbed ground:
  the digger arrives at a patch of topsoil where nothing has ever been
  buried, marked with a single surveyor's flag. The 404 page is a
  small topsoil section — the requested path lettered as the plot's
  address, one line in the record voice, and the way back marked by
  the flag's string line to the surface index (§6.10). It belongs
  because the theme's honesty extends to its absences: this ground is
  empty, the page says so plainly, and it does not dress the emptiness
  as a find.
- **Structure.** A single topsoil section: apparatus line "PLOT —
  [requested path]", an `<h1>` in the record voice ("Nothing is buried
  here."), two lines explaining and offering the nearest surveyed
  ground (only when a real near-match exists, computed from the site's
  actual routes), the flag (a small sand triangle on a line, SVG), and
  links to the surface and the strata index. No illustration of a
  mascot with a spade (§9).
- **Motion spec.** One motion: on load, the flag is planted — it drops
  12px and presses into the ground over 300ms `--ease-press`, its
  string line drawing 400ms `--ease-draw` toward the index link. Then
  stillness. An empty plot does not perform.
- **States.** Rest (planted) → still. The near-match line, when
  present, is static text.
- **Content merge.** The struck-through expectation is the visitor's
  actual requested path; the offered ground is the site's actual
  nearest page. Nothing is invented to fill the plot.
- **Failure fallback.** It is a static page with links; the flag ships
  planted in the DOM.
- **Reduced-motion variant.** Flag pre-planted, string drawn.
- **Performance budget & mobile variant.** Two small animations, once.
  Mobile: unchanged composition, links stack.
- **Choreography timeline (v2).** t=0 painted, flag parked 12px high →
  t=150 flag presses (300ms) → t=450 string draws (400ms) → t=850
  still.
- **State matrix (v2).** *Rest:* planted, still. *Hover/focus:* links
  per §11. *Active:* navigation (§6.15). *Scrolled-past:* n/a (one
  screen). *Disabled:* flag rendered planted. *Touch:* links ≥48px.
- **Breakpoints (v2).** All sizes: the plot takes the topsoil measure.
  <768px: the flag sits above the heading instead of beside it.
- **Edge cases & failure modes (v2).** *Near-match computation finds
  nothing close:* the line is omitted — a guessed suggestion on empty
  ground is the one lie this page refuses (§9). *The path is a real
  page under a moved stratum:* the record line says so and links the
  new depth — redirects with an explanation, in the theme's voice.
- **Accessibility spec (v2).** The `<h1>` is the meaning ("Nothing is
  buried here"), not the apparatus. The flag is `aria-hidden`; the
  path is read as "You dug for: [path]".
- **Tokens consumed (v2).** `--topsoil`, `--sand`, `--chalk`,
  `--ease-press`, `--ease-draw`.

## 7. Page application map

**Home — the full dig.** Surface hero (§6.11), then the strata in
argument order: topsoil (the newest, the provisional), clay (the
working content and its finds), the sand seam (a single apparatus line
— a date, a depth, a fact), chalk (the archive, the oldest true
things, one find per screen), bedrock (seams §6.9, form §6.13, record
§6.14). The context record (§6.17) sits at the chalk/bedrock boundary
— the audit is read just before the visitor is asked to commit.

**Listing — a single stratum, fully dug.** A listing page is one
stratum at greater width: its finds (§6.12) in that stratum's density,
its own depth range lettered at the head, and the strata index (§6.10)
offering the other layers. A listing that mixes strata on one page has
collapsed the trench; cross-stratum collections are presented as a
*section drawing* (§6.1's grammar) linking into each stratum's listing,
never as a blended grid.

**Detail — one find, in context.** The find at full size in its
stratum, its context record row expanded into prose (§6.17), its
neighbours in the same layer at the foot ("Also in the clay"), and its
depth stated before its name is celebrated. The detail page's stratum
is the find's stratum; a find is never promoted to the topsoil for
display.

**About — the surveyor's page.** The people and the method, set in the
chalk: who digs, how the depths are assigned, the survey's date. This
is where the mapping declaration (§6.17) lives in long form — the
about page is the theme's methodology, and it is deliberately deep:
casual visitors don't need it, committed ones dig for it.

**Contact / order — the bedrock only.** §6.13's form in its stratum,
reached by the dig or directly (a direct arrival lands the visitor in
the bedrock with the surface one click up — depth is the home page's
argument, not a toll gate on every route).

**The undisturbed page (404).** §6.18, everywhere, unchanged.

## 8. Worked examples

### 8.1 The hero — standing on the surface

*The commission: a soil-and-vineyard consultancy, "Harrow & Loam"; the
home page's dig runs surface → topsoil (current season's work) → clay
(the services, as finds) → chalk (forty years of soil reports) →
bedrock (engagement prices and the order form). Surveyed depth 240cm.*

- **The composition (§6.11).** First screen: topsoil ground. The title
  "Harrow & Loam" in Bitter 800 chalk, and beneath it the apparatus:
  "SURVEYED DEPTH 240 CM · FIVE STRATA · NINE FINDS BURIED" — nine
  being the page's real find count, generated, not typed. The section
  drawing (§6.1) occupies the lower half: five bands, the clay band
  carrying three find markers, the chalk one, the bedrock none (what
  is in the bedrock is not a find; it is the ground everything rests
  on — the drawing says so by omission, and §6.17's record explains).
- **The ceremony.** Fonts ready at t≈120ms: the title's letters begin
  settling from the last letter backward (§6.3), all at rest by
  ≈1100ms. The drawing's bands settle in stratum order from t=0; the
  surveyor's line draws from t=700 and lands its bob at t=2100 as the
  readout steps to 240. At t=2600 the "Begin the dig" marker pulses
  once. A visitor who never scrolls has still received the whole
  survey: every stratum, every depth, every find's position.
- **Scroll timeline.** 0–60px: nothing moves but the tape (§6.5)
  waking at the trench edge. 60–400px: the surface gives way to the
  topsoil stratum; its spade-wipe (§6.2) runs as its top crosses the
  78% line. The visitor is digging.

### 8.2 Mid-page — the clay and its coins

*The same page, mid-descent: the clay stratum holds the services as
three finds — "Soil survey", "Drainage report", "Vineyard plan" —
each a card (§6.12) with a drawn plate, a context line, and a figure
(§6.16).*

- **Entry.** The clay's top crosses 78%: the spade-wipe sweeps 800ms,
  the blade's label reading "CLAY — 60 TO 120 CM". As the wipe
  completes, the three figures count: surveys completed 214, hectares
  mapped 1,150, oldest client soil 41 years — each sourced in
  §6.17's legend ("practice records, January 2026"), each landing
  exactly and holding.
- **The finds at depth.** The cards drift at the clay rate (0.08,
  §6.4) — noticeably less than the topsoil's roots above them moved.
  The visitor's pointer crosses the "Soil survey" card: the brush
  (§6.8) sweeps its dust off in 450ms; its plate — a drawn auger and
  sample jars — stands sharp; its figure was never dusted and never
  moved. They press the trowel-notch: the triangle cuts into the
  card's corner, the tray count in the header flashes sand: one find
  kept.
- **What the visitor feels.** Resistance increasing pleasantly — the
  deeper layer moves less, reads slower (line-height 1.62 here), and
  its objects reward a cleaner look. Nothing asked for attention; the
  brush and the notch answered it.

### 8.3 Conversion — cut into the bedrock

*The same page's end: the bedrock holds three seams — "Seasonal
retainer", "Full survey", "Estate engagement" — and the order form.*

- **Arrival.** The bedrock pins (§6.9). Seam 1 is lit: the retainer,
  its price in sand Bitter at 38px. The visitor scrolls the pin; at
  q=0.33 the lamp crosses to the Full survey seam — the middle offer,
  lettered as the one most dug for (a true statement from the
  practice's records, or it is not lettered). At q=0.66, Estate. The
  pin releases into the form (§6.13).
- **The cutting.** The visitor chooses the Full survey seam's button;
  the form's first field takes focus, its rule lighting chalk with the
  sand hairline sliding under. They mistype the email (no @): on blur
  the rule turns clay-bright and the record notes beneath, in Source
  Serif italic: "This direction will not carry — check the address
  before we cut." (§12's error voice: the error is a surveying fact,
  not a scolding.) They correct it; the note clears. They press CUT
  THE ORDER: the block presses into the stone, and on success the
  confirmation seam draws its sand edge across the form's width,
  lettered "ORDER CUT — REFERENCE HL-2026-0114" with the line "The
  record of this order is kept in the bedrock (§6.14)."
- **Failure rehearsed.** If the post fails, nothing they wrote is
  cleared; the note above the form reads "NOT CUT — THE STONE
  REFUSED. YOUR WORDS ARE KEPT ABOVE." and the block un-presses. A
  visitor who dug 240cm for this form is never sent back to the
  surface by a network blink (§10, blocking gate 7).


## 9. Anti-slop — what makes THIS theme look cheap

1. **The brown website.** Strata as five horizontal colour bands with
   ordinary web content poured into them. *Cure:* §1's law and §4 —
   depth order is argument order, finds obey burial geometry, density
   falls with depth. If swapping two sections' colours changes nothing,
   the build is stripes, not strata.
2. **Decorative dirt.** Soil textures, grain overlays and pebble stock
   photos sprinkled for "earthiness". *Cure:* the palette is flat
   colour and drawn line; the only textures are the dust (§6.8) and the
   sift (§6.7), both rationed and functional. A photograph of soil is
   a confession that the design didn't happen.
3. **Invented depths.** A tape reading "500 cm" because it sounded
   deep; finds buried where they photographed well. *Cure:* the
   declared mapping (§6.17), generated instruments (§6.1/§6.5/§6.10/
   §6.14 from one survey object), and §10's three-records check.
4. **The spade as a logo.** Spade icons on buttons, trowel cursors,
   a cartoon digger mascot on the 404. *Cure:* tools appear only as
   actions — the wipe, the brush, the notch. The theme has no mascot;
   §6.18's flag is the closest it comes, and it is a marker, not a
   character.
5. **Everything pinned.** Pinning every stratum "for immersion" until
   the page is a series of traps. *Cure:* §5 — exactly two pins
   (§6.1's sequence, §6.9), and the bedrock pin is cut on mobile.
6. **Fade-up reveals underground.** Sections fading and rising like a
   SaaS landing page wearing brown. *Cure:* §6.2 is the only reveal;
   a build that adds a second reveal grammar has left the trench.
7. **Pricing in the topsoil.** A hero with prices "for conversion"
   above the dig. *Cure:* §4's density and depth law — prices live in
   the bedrock; a build that surfaces them has falsified its own
   argument that depth is value.
8. **Rounded, shadowed cards floating on the earth.** *Cure:* §4 —
   cards are cut into their stratum, radius 0, no drop shadows; depth
   in this theme is stratigraphic, never cast.
9. **The tape as decoration.** A depth readout that doesn't match the
   strata (tape says chalk at a section the drawing calls clay).
   *Cure:* one survey object, generated instruments, §10 gate 3.
10. **Roots everywhere.** Root hairs drawn at every boundary because
    they were pretty once. *Cure:* §6.6 — roots grow only from the
    living topsoil, from real elements, toward real finds. Biology is
    rationed to the layer that is alive.
11. **Marquee strata, kinetic headlines, blur reveals.** Any motion
    §5 refuses, smuggled back in. *Cure:* the refusal list is part of
    the gate (§10, item 11).
12. **Approximation theatre.** "≈11,700 years" counted with slot-
    machine precision theatre, or exact figures with no source.
    *Cure:* §6.16 — approximations are printed as approximations and
    every figure names its source in the legend.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **Depth-law audit.** Every find's stratum is justified by one true
   sentence in the context record (§6.17), and the record is present
   on the page. An unjustified burial fails.
2. **Figure-truth audit.** Every number the page asserts (depths,
   ages, pH, counts, prices) traces to the declared mapping or a
   named publisher source in the legend. An untraceable figure fails.
3. **Three-records agreement.** The section drawing (§6.1), the depth
   tape's total (§6.5), the strata index (§6.10) and the footer
   record (§6.14) state identical strata, depths and find counts —
   generated from one survey object and verified by reading all four.
4. **No stranded content.** With JS disabled, the whole page reads:
   strata excavated, figures printed, prices legible, form working.
   With JS on and the loop killed, every watchdog (§6.2's 1000ms,
   §6.15's 1200ms) fires and uncovers its section.
5. **Burial geometry.** No find crosses a stratum boundary at any
   scroll position, including §6.4's maximum clamps — checked at the
   deepest scroll offsets, not just at rest.
6. **Contrast audit.** Text pairings only from §2's law, verified in
   dusted (§6.8) and brushed states and in every seam state (§6.9).
   Clay text on clay, sand text on chalk, flint text anywhere: fail.
7. **Form-keeping.** A failed submit (simulated network error) leaves
   every field exactly as written, with §12's failure note. Any build
   that clears the form on error fails.
8. **Bedrock stillness.** The bedrock stratum has no parallax, no
   drift, no sift; its only motions are §6.9's light and §6.13/§6.14's
   single draws. Motion in the stone fails.

**Standard (must pass, fixable in review):**

9. Density falls with depth (§4): topsoil busiest, chalk ≤1 find per
   screen, bedrock holding only seams, form, record.
10. Exactly two pins; spade-wipe is the only reveal grammar; the
    refusal list (§5) is honoured — no marquee, no blur reveals, no
    kinetic type beyond §6.3.
11. Ambient ration: sift intervals ≥9s and one section at a time;
    roots only at the topsoil boundary; sway and sift pause
    off-screen and under reduced motion both are absent.
12. The settling title runs once per session and never re-runs; the
    hero's apparatus figures match the generated counts.
13. Every interactive element is ≥44px, focus shows §6.8's brush or
    §11's ring, and focus never leaves a find mid-drift (§6.4).
14. Mobile: bedrock pin cut, tape miniaturised to line + chip, roots
    ≤10 and unswaying, find grids per §6.12's breakpoints.

## 11. Component inventory

Every component a real Loam & Strata site needs, with its themed
treatment. Components the theme refuses are listed with their
in-trench replacement — a refusal without a replacement is a gap, not
a stance.

| Component | Themed treatment |
|---|---|
| Primary button | Cut block: bedrock ground, 2px sand edge, apparatus label; presses 2px on `--ease-press` (§6.13). On pale strata, topsoil ground with chalk label. |
| Secondary button | Ruled line button: transparent, 2px bottom rule in the stratum's text colour; hover lights the rule sand. |
| Text input | Inscription line (§6.13): apparatus label above, 2px rule below, no box. |
| Textarea | Ruled sheet: lines every 33px (the body line unit), Source Serif 19px. |
| Select | Refused. Choices are seams: a short list of ruled radio lines, the chosen one's rule in sand (§6.13's consent grammar generalised). |
| Checkbox | Seam box: unfilled square cut in the stratum; filled = sand fill + ground-colour tick. |
| Radio | Seam line: the chosen line's rule inks sand; the dot is a small filled circle of the stratum's find colour. |
| Toggle / switch | Refused. A trench has states of ground, not switches; use two seam lines (On the surface / In the ground) as radios. |
| Card | Find card (§6.12): cut into its stratum, dusted, brushable, notchable. |
| Table | Context record (§6.17): real table, apparatus headers, no zebra striping — strata bands at most every 6 rows in the stratum's 8% tint. |
| Tabs | Refused. Depth is not tabbed; strata are scrolled or indexed (§6.10). A build needing tabs has two strata arguing — separate them into sections. |
| Accordion | Drawer compartment: a find whose context expands downward like a section being deepened — the row below pushes down over 300ms `--ease-settle`; the heading gains a depth tick. |
| Modal / dialog | The finds tray (§6.17) is the theme's only dialog. Other confirmations are seams: an inline band that cuts into the current stratum with the question and two cut blocks. |
| Toast | Refused. News from the dig is recorded, not toasted: transient confirmations appear as a one-line record entry at the section's foot, in the record voice, and remain until the next excavation. |
| Tooltip | Refused. Explanation lives in context lines (§6.17); a find that needs a tooltip needs a better context line. |
| Badge | Depth chip: apparatus text on the stratum's ground — "CLAY · 94 CM" — the badge states where a thing lies, never a marketing claim ("NEW" is a topsoil word and is banned, §12). |
| Alert | Failed-dig band: a seam in the current stratum, clay-bright rule on bedrock / errata treatment per §6.13, message in §12's error voice, persistent until resolved. |
| Pagination | Depth pagination: "Deeper" / "Shallower" links lettered with the next stratum's name and depth — never numbered pages; a trench is continuous. |
| Progress bar | Refused. Progress is the depth tape (§6.5). |
| Spinner | Refused. Waiting is an unexcavated section (§6.15). |
| Skeleton | §6.15's covered section with its stratum label. |
| Search | The survey search: a single inscription line in the header zone; results are returned as a mini section drawing (finds grouped by stratum, depths stated) — search results in this theme are a survey, not a list. |
| Breadcrumbs | Replaced by the strata index's visited states (§6.10) plus the tape: the visitor's path is a depth, not a trail of pages. |
| Skip link | "Skip to the bedrock" / "Skip to content" as a plain chalk link appearing on first focus at the surface. |
| Focus ring | 2px sand outline, offset 3px, on every interactive element; on find cards, focus also triggers the brush (§6.8). |
| Divider | A stratum boundary (§4's authored edge) or, within a stratum, a 2px rule in the stratum's text colour at 30%. Wavy SVG dividers are refused — that is a different theme's water. |

## 12. Content & copywriting voice

Two voices, cast like the type. **The Surveyor** writes apparatus:
stratum names, depths, counts, labels — Bitter, uppercase, terse,
every figure sourced. **The Record** writes prose: context lines,
explanations, errors, confirmations — Source Serif, sentence case,
plain and unhurried, the voice of someone writing up the day's dig for
whoever comes next. The voices never swap: apparatus never sentences,
the record never shouts.

**Headline style.** Names of things and their depths. ✓ "The clay:
what the hill kept" / "Nine finds, three strata, one bedrock price".
✗ "Dig into our amazing solutions!" (exclamation, unsourced claim,
topsoil marketing in a headline's mouth). Exclamation marks are
banned from the whole theme — the ground does not shout.

**Label style.** Apparatus: noun + measurement. ✓ "CLAY — 60 TO 120
CM", "DEPTH 137 CM / 240". ✗ "Section 2", "You are 57% through" (the
tape counts centimetres; percentages are a bar's language).

**Error voice.** A surveying fact, stated plainly, with the way back.
✓ "This direction will not carry — check the address before we cut."
✓ "NOT CUT — THE STONE REFUSED. YOUR WORDS ARE KEPT ABOVE." ✗ "Oops!
Something went wrong 😞" (the trench has no "oops", and no emoji
survives burial).

**Empty-state voice.** ✓ "Nothing is buried here." / "Your tray is
empty. Finds you notch are kept here, with their context." ✗ "No
results found. Try being less specific?" — the record does not blame
the digger.

**Confirmation voice.** ✓ "ORDER CUT — REFERENCE HL-2026-0114. The
record of this order is kept in the bedrock." ✗ "Success! 🎉 You're
all set!" — a confirmation is a record entry, not a celebration.

**Banned words:** amazing, revolutionary, seamless, dive in (the theme
digs; it does not dive), unlock, supercharge, NEW (as a badge), oops.
**Owned words:** stratum, seam, find, context, surveyed, at depth,
kept, cut (for bedrock actions), the surface, undisturbed.

**Fixed strings (verbatim, do not paraphrase):** the pricing
introduction — "The good stuff is never on the surface."; the tape's
terminal reading — "BEDROCK"; the 404 heading — "Nothing is buried
here."; the form failure note — "NOT CUT — THE STONE REFUSED. YOUR
WORDS ARE KEPT ABOVE."

## 13. Full-page scroll choreography map

The home dig, top to bottom. Every beat in order; instruments run
continuously beneath the beats (tape §6.5 scrubbing, parallax §6.4
drifting, sift §6.7 on its sparse timer).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Title settles (§6.3); drawing assembles, line drops (§6.1) | Standing on surveyed ground |
| 2 | 0–60px | Tape wakes; surface apparatus holds | The instrument is live |
| 3 | Topsoil top crosses 78% | Spade-wipe excavates the topsoil (§6.2) | The first cut |
| 4 | Topsoil in view | Roots grow at its lower boundary (§6.6); figures count (§6.16) | The living layer |
| 5 | Clay top crosses 78% | Wipe; blade label reads the clay's depths | Deeper, slower |
| 6 | Clay in view | Finds drift at 0.08; brush and notch available (§6.8/§6.12) | Examination |
| 7 | Sand seam passes centre | The seam's single apparatus line crosses the tape's marker; tape letters the seam | A bright thin fact |
| 8 | Chalk top crosses 78% | Wipe; the chalk's one find per screen (§4) | Sparseness as value |
| 9 | Chalk/bedrock boundary | The context record (§6.17) is read — the audit before commitment | The workings, shown |
| 10 | Bedrock pin engages | Seam 1 lights (§6.9) | Arrival at the stone |
| 11 | Pin q 0.33 / 0.66 | Lamp crosses to seams 2, then 3 | Prices, read in order |
| 12 | Pin releases | Form (§6.13) stands in the bedrock | The ask, at full depth |
| 13 | Footer enters | Sand edge draws (§6.14); tape reads BEDROCK | The record, filed |

**Reverse pass.** Scrolling up: excavations stay excavated (the dig
does not un-dig), parallax and tape reverse exactly, the seam lamp
climbs, roots stay grown. The only things that re-cover are dust
(§6.8's slow re-dust) and the visitor's sense of depth, which the tape
reports honestly in both directions while remembering the deepest
point.

**Jump-scroll catch-up.** Anchor jumps and flings: everything passed
is excavated instantly (§6.2's rule), figures stand read, the tape
snaps to the mapped depth, and the seam lamp lights the seam the
visitor landed in. No ceremony is owed to a teleport.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 620KB, of which images/plates ≤ 380KB |
| Fonts | Bitter (2 weights) + Source Serif 4 (2 styles) ≤ 120KB, `font-display: swap` |
| JS | ≤ 60KB gzipped (one loop, observers, tray, form) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the assembly's timers are sliced per stratum |
| Excavation latency | Any section uncovered ≤ 1000ms after entering (watchdog law) |
| Active parallax finds | ≤ 12 per frame; sift grains ≤ 10 page-wide, one section at a time |

**Cut order when the budget is exceeded** (cut in this order, record
each cut in the build notes):

1. Soil sift (§6.7) — gone entirely.
2. Root sway (§6.6) — roots still grow; they hold still.
3. Parallax on chalk finds (§6.4) — chalk rests; topsoil/clay keep
   their rates.
4. The transition sheet (§6.15) — navigation becomes instant with the
   index flash.
5. Brush-off sweep (§6.8) — dust toggles instantly (the reduced-motion
   treatment) for all visitors.
6. Seam-lamp easing (§6.9) — the lamp snaps at boundaries; the pin
   stays.

**Never cut:** the spade-wipe's watchdog, the depth tape, the context
record, the form's error-keeping, any reduced-motion variant. A build
that cuts the honesty to keep the ambience has inverted the theme.

## 15. Build-order checklist

1. Survey first: fix the strata, their order, each find's stratum and
   its one-sentence justification, and the declared total depth.
   Write the survey object; everything else is generated from it.
2. Build the static trench: all strata, all content, figures printed,
   prices legible, form working — with no JS. This is the site; the
   rest is excavation.
3. Set the palette tokens and pairing law (§2); audit contrast in
   every stratum before any motion exists.
4. Set the type scale and the depth line-heights (§3 laws).
5. Author the stratum boundary profiles (§4) — one per stratum,
   reused at all breakpoints.
6. Build the instruments from the survey object: section drawing
   (§6.1), depth tape (§6.5), strata index (§6.10), footer record
   (§6.14). Verify the three-records agreement by reading all four.
7. Add the shared loop; wire the tape and layer-depth parallax
   (§6.4) with their clamps computed from real clear earth.
8. Add the spade-wipe (§6.2) with its 1000ms watchdog and catch-up
   rule; test with the loop killed.
9. Calibrate the tape: each stratum boundary must cross the marker
   exactly as its section boundary crosses 50% viewport height.
10. Add the surface ceremony: title settle (§6.3), assembly (§6.1),
    hero composition (§6.11) with the session rules.
11. Add roots (§6.6) measured from real topsoil elements; re-measure
    on the post-image layout pass.
12. Add the brush and notch (§6.8/§6.12) and the tray (§6.17) with
    its persistence and withdrawn-find handling.
13. Build the bedrock: seam pin (§6.9), order form (§6.13) with
    error-keeping rehearsed against a simulated network failure,
    footer (§6.14).
14. Add figures (§6.16), skeleton/transition (§6.15), the undisturbed
    page (§6.18), and last — only if the budget survives — the sift
    (§6.7).
15. Run §10 in full: depth-law audit, figure-truth audit,
    three-records agreement, no-JS read, loop-killed read, boundary
    geometry at maximum clamps, bedrock stillness. Gate signed by
    someone who did not build the page.
