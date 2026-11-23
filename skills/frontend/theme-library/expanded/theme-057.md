# 57. Ochre & Pigment — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A site ground from earth pigments: every colour on
the page is a named mineral, sections are pigment cakes in a
painter's box, and the design process itself is grinding, mixing,
binding. Palette anchors: red ochre `#C1442E`, yellow ochre
`#D9A441`, raw umber `#5C4A32`, green earth `#3F4A3A`, chalk white
`#EFE6D4`. Type: Alegreya (display) + Alegreya Sans (body). The
page is a tin of pigment cakes on a chalk ground; two pigments
visibly mix at every section boundary; the colophon footnotes
every colour with its Colour Index name (PY43, PR102, PBr7, PG23,
PW18).

## 1. Concept & world

Ochre & Pigment is the website of people who make colour out of
ground earth, and it refuses to treat colour as a style choice.
On this page a colour is a *material with a biography*: it was
dug, washed, levigated, ground, dried into a cake, and it will
become paint only when somebody binds it. The page performs that
biography in order. It opens dry — matte, powdery, matte fields
sitting in their slots like cakes in a tin — and it *wets* only
where the visitor acts: scrolling mixes two neighbouring
pigments where their sections touch, hovering binds a cake's
surface into gloss, clicking grinds it one step finer. Nothing
on the page is glossy by default, because nothing in the
workshop is paint by default. Paint is what happens to pigment
under work, and the visitor does the work.

The world is the pigment merchant's bench. At the top, a pile of
red-ochre powder is ground under a muller until it becomes the
smear the headline stands on — the page manufactures its own
ground before it speaks. Down the page, each section is one cake
in the tin, labelled with its pigment's name and Colour Index
number the way a real cake is stamped. Between cakes, in a 120px
band, the two neighbours do what neighbouring earths do when a
palette knife drags across both: they mix, at a printed ratio,
into a third earth that belongs to neither. In the margin, the
reader's progress is a test smear — the streak a painter pulls
on the edge of the slab to check a colour — growing section by
section until, at the footer, it stands as the finished stripe
of the whole palette. The colophon then does the theme's
signature act of honesty: it footnotes every colour used
anywhere on the site with its pigment index name, so the palette
is not a mood but a bill of materials.

**The theme's one law: every colour is a pigment, and every
pigment is named.** No colour may appear on the page that is not
either (a) one of the five declared pigment anchors or their
declared bound/deep variants in §2, or (b) a declared *mix* of
exactly two pigments that sit in adjacent slots, at a ratio
printed on the page where the mix occurs. An unnamed colour — a
stray hex in a stylesheet, a browser-default blue link, a pure
`#000` shadow, a stock gradient — is a blocking gate failure,
because in this world colour is inventory: if it is on the page,
it came out of a cake, and the cake has a name and an index
number. Three corollaries follow. First, **mixes happen only
between neighbours**: red ochre may mix with the yellow ochre in
the next slot, never with the green earth three slots away — a
cross-box mix is a colour with no biography and is refused.
Second, **dry is the shipped state**: the DOM arrives matte and
complete; binding (gloss, saturation, depth) is applied only by
an act — scroll, hover, click — and can always be traced to the
act that caused it. Third, **every printed figure is a workshop
figure**: grind times, mesh sizes, weights and prices come from
the merchant's catalogue object (§6.13), never from a designer's
sense of a round number; a grind time that no grinder recorded
is an unnamed colour in numeral form.

**Best-fit sites and audiences.** Pigment and paint merchants
selling earth colours, watercolour cakes, gouache and dry
pigment by weight; makers of handmade paint, inks and pastels;
natural-dye and fresco suppliers; tile, limewash and clay-plaster
makers whose product is literally coloured earth; printmakers
and letterpress shops mixing their own inks; art-supply
retailers with a serious pigment catalogue; a pottery-glaze
studio; conservation and restoration suppliers, whose customers
specify materials by Colour Index name and will check the
colophon the way they check a datasheet. The audience is
material-literate: painters who know PY43 from PY42, who read a
ratio as information, who trust a shop that footnotes its own
palette. Conversion here is an order by weight, a sample request,
or a trade account — considered purchases made by people buying
a substance, not a shade.

**When NOT to use it.** Not for synthetic colour: a neon,
fluorescent or RGB-native brand cannot be named in earth
pigments without lying, and the law forbids the lie. Not for
fast, bright consumer retail — the dry-first register reads as
slow and dusty to a visitor who wants pop; that visitor is not
wrong, they are elsewhere. Not for data-dense dashboards: cake
slots and mix bands are enemies of tabular scanning, and §11
refuses the dense data table rather than dress it. Not where the
client cannot supply a real catalogue: the theme's figures
(grind times, indices, ratios) must come from the merchant's
records; a shop that cannot say how long its red ochre is ground
cannot keep the third corollary. Not for multi-brand platforms —
the tin holds one maker's box.

## 2. Palette

Five anchors, each a real earth pigment with its Colour Index
name. Every anchor also carries a **bound** variant — the same
pigment mixed with binder (gum arabic), which in reality darkens
and saturates an earth colour — because the theme's central
contrast fact lives here: *binding deepens*. Contrast figures
below were computed for this expansion against the chalk ground
unless stated.

| Token | Hex | Pigment (Colour Index) | Role | Share | Contrast & licensing |
|---|---|---|---|---|---|
| `--chalk` | `#EFE6D4` | Chalk / whiting, PW18 (calcium carbonate) | The ground: page sheet, tin paper, card faces | ~58% | The light surface everything is measured against |
| `--red-ochre` | `#C1442E` | Red ochre, PR102 (natural red iron oxide) | Hero pigment, first cake, key fields | ~10% | On chalk 4.1:1 dry — display ≥24px only in dry state |
| `--red-ochre-bound` | `#B03A26` | PR102 bound in gum arabic | The hero pigment at work: hover/bound states, sub-heads | (state) | On chalk 4.9:1 — binding deepens it past AA body; the theme's proof that the process is real |
| `--red-ochre-deep` | `#9E3520` | Declared mix PR102 : PBr7 = 3 : 1 | Red-family text: prices, labels, links on chalk | ~2% | On chalk 5.7:1 — the only red licensed for body-size text |
| `--yellow-ochre` | `#D9A441` | Yellow ochre, PY43 (natural yellow iron oxide) | Second cake, warm fields, the smear's second stripe | ~8% | On chalk 1.8:1 — never text on chalk; on raw umber 3.8:1, large only |
| `--yellow-ochre-deep` | `#7D581B` | Declared mix PY43 : PBr7 = 1 : 1 | Ochre-family text: grind labels, ticket figures on chalk | ~1% | On chalk 5.2:1 — the only yellow licensed for text |
| `--raw-umber` | `#5C4A32` | Raw umber, PBr7 (natural brown iron oxide + manganese) | Third cake, body-text-licensed field, tin shadows | ~9% | On chalk 6.8:1 — body text licensed; chalk on umber 6.8:1 |
| `--green-earth` | `#3F4A3A` | Green earth / terre verte, PG23 (celadonite, glauconite) | Fourth cake, closing fields, footer ground | ~8% | On chalk 7.5:1 — body text licensed both directions |
| `--ink-earth` | `#453521` | Declared mix PBr7 : PG23 = 3 : 1, ground deep | The reading ink: body text on chalk | text | On chalk 9.5:1 — the darkest colour on the page, and itself a named mix |
| `--chalk-dim` | `#E2D5BE` | PW18 with 6% PBr7 (the tin's inner paper) | Slot recesses, skeleton fields, disabled grounds | ~4% | Background only; never a text surface for `--ink-earth` below 17px |

**Usage law.** Chalk is the ground, not a colour among colours:
no section may be chalk-on-chalk, and every cake field sits on
chalk or in a chalk-lined slot so the pigment reads as a material
sample. The five anchors appear in tin order — red ochre, yellow
ochre, raw umber, green earth, chalk — wherever the whole box is
shown (hero, smear stripe, colophon), because a painter's box
has an order and the reader learns it. **Mix tokens are not
hexes**: a boundary mix is computed live with `color-mix()` from
its two named neighbours at its printed ratio (§6.4), so the mix
can never drift from its recipe; the only pre-mixed hexes are the
three declared deep mixes in the table, each with its ratio
printed here and repeated in the colophon.

**Batch variation is law, not error.** Earth pigments are dug,
not manufactured: two cakes of PR102 from different batches
differ measurably, and the theme prints the difference instead
of correcting it. Each cake token carries its batch's measured
value in the catalogue (§6.13) — batch 14's red ochre is
`#C1442E`; batch 9 was `#BC3F2C`, and the colophon of a page
built during batch 9's run says so. A build must never
"harmonise" two batches into one hex for tidiness: the
variation is the provenance, a painter buying batch 14 is
entitled to batch 14's colour on the screen, and the boundary
mixes (§6.4) are computed from the *current batch's* tokens, so
a batch change re-recipes the whole site honestly. The one
thing that may not vary is the licensing: a batch whose dry
value would drop a text pairing below §2's floor is not
published until its deep mix is re-measured and re-declared.

**Dark mode — the box, closed.** The page does not invert. Under
`prefers-color-scheme: dark` the tin is read by lamplight:
grounds take their bound row (`--chalk` → `--chalk-dim` deepened
one step to `#D9C8A8`, declared as PW18 under lamplight), cake
fields use their bound variants, and text pairings are
re-measured, not assumed: `--ink-earth` on lamplight chalk is
7.9:1, chalk text on bound green earth 6.9:1. Yellow ochre stays
field-only at night exactly as by day. A design that needs a
true black surface does not belong to this theme (§1).

## 3. Typography

Two faces from one family, because the workshop speaks in two
registers and both are printed, never shouted.

- **Alegreya** (500, 700) — display and headings. An old-style
  serif with calligraphic warmth; its slightly irregular stroke
  is the typographic form of hand-ground material. Display sizes:
  56px/1.04 (hero, ≥1200px), 44px/1.08 (tablet), 34px/1.12
  (mobile); section heads 32px/1.15; card heads 21px/1.25.
  Tracking 0 at all sizes — Alegreya's spacing is part of its
  grain and is never tightened.
- **Alegreya Sans** (400, 500, 700) — body, tickets, data. Body
  17px/1.55 on chalk (16px/1.55 below 768px); captions and ticket
  lines 13px/1.45; the **index voice** — pigment names with their
  Colour Index numbers — is Alegreya Sans 700, 11px, uppercase,
  letter-spacing 0.12em, and is the only tracked type on the page.

**Type laws.** (1) *Figures are lining and tabular, or they are
not figures.* Grind times, weights, prices and ratios are set in
Alegreya Sans with `font-variant-numeric: lining-nums tabular-nums`;
Alegreya's old-style figures are banned from data — a grind time
that waves up and down like handwriting cannot be compared down
a column. (2) *Italics are Latin and mineral names only* —
*terra rossa*, *goethite*, *celadonite* — never emphasis; a word
that needs stress gets the index voice or a deeper pigment, not
a slant. (3) *The headline is set dry before it is set bound*:
headline type renders first in its matte state (§6.2); no other
heading on the page performs the bind — one ceremony per page,
at the name. (4) *Ratios are type, not decoration*: a mix ratio
is always printed in the form `3 : 1` in the index voice beside
the mix it describes; a boundary without its printed ratio is an
unnamed colour (§1) and fails the gate. (5) *No heading may name
a colour it is not set in or standing on*: a section head about
green earth stands on the green-earth cake or is set in
`--green-earth`; a red headline over a green field is a labelling
error a child would catch in a real tin.

## 4. Layout language

**The tin.** The page is one tin: a 1240px maximum measure
(≥1200px), 24px tin gutters, in which each section sits as a
**cake in a slot** — a full-bleed colour field or chalk sheet,
separated from its neighbours by the 120px boundary band where
the two pigments mix (§6.4). Slots are square-cornered at 2px
radius: cakes are pressed rectangles, not pebbles, and a slot's
recess is shown by a 1px `--chalk-dim` inner line at its top
edge and a 6px matte offset beneath — the cake sits *in*
something. There are no drop shadows in this theme; depth is the
recess line and the offset, both in named pigments.

**The margin bench.** At ≥1200px a 72px left margin rail runs
the page's full height: it holds the paint-smear progress
(§6.6) and nothing else — the bench edge where the painter tests
colour. At 768–1199px the rail narrows to 48px; below 768px the
smear retires to a 4px top stripe (§6.6) and the tin goes
full-width with 16px gutters.

**Density and order.** One cake per reading beat: a section's
field is 60–90vh of one pigment with its content, never two
cakes side by side above 768px (below it, cakes stack — a tin
stood on end). Sections follow tin order down the page wherever
the content allows; when editorial order must differ, the smear
and colophon still list the box in tin order, and the boundary
mixes are recomputed for the actual neighbours — the recipe
follows the adjacency, never the plan. Whitespace is **the
blotting paper**: chalk space between cakes is where the eye
rests and where tickets, ratios and index lines are printed; it
is never filled with ornament, because the paper in a real tin
is plain.

**The boundary band.** Every slot boundary is exactly 120px
(64px below 768px): the upper pigment's field ends, the band
mixes, the lower pigment begins. The band is layout, not
decoration — remove it and two cakes would touch, which in a
real box means contaminated pigment.

## 5. Full motion system

Every motion term, in the language of the bench. One shared
requestAnimationFrame loop drives all scrubbed values with a
lerp of **0.12** (the *dry* rate); inside the pinned mix and the
boundary bands the same loop's effective lerp is **0.09** — wet
material resists, and the scroll feels it (§6.5). All pre-states
are JS-armed only; the shipped DOM is the dry, complete page.

Named easings: `--ease-grind` `cubic-bezier(0.65, 0, 0.35, 1)` —
circular pressure, slow to start, sustained; `--ease-settle`
`cubic-bezier(0.34, 1.3, 0.64, 1)` — a cake dropping into its
slot with one granular overshoot; `--ease-mix`
`cubic-bezier(0.45, 0, 0.2, 1)` — the knife drag, long and even;
`--ease-gloss` `cubic-bezier(0.16, 1, 0.3, 1)` — binder sweeping
wet and fast; `--ease-stamp` `cubic-bezier(0.34, 1.56, 0.64, 1)`
— a dry stamp landing and lifting. Duration tokens:
`--dur-grind` 1400ms, `--dur-gloss` 600ms, `--dur-settle` 380ms,
`--dur-judder` 40ms, `--dur-draw` 1500ms, `--dur-swirl` 500ms,
`--dur-smear` 900ms, `--dur-count` 1200ms.

- **Scroll-triggered reveals** are *cake settles*: a section
  slides laterally 24px into its slot and judders in three 40ms
  steps as it seats (§6.3). Trigger: slot top crossing 78% of
  the viewport. Nothing fades up; pigment does not apparate, it
  is placed.
- **Scroll-scrubbed motion** is *mixing*: boundary bands blend
  at the scroll's ratio (§6.4), the pinned process section
  performs the full grind-to-paint mix across 150vh (§6.5), and
  the margin smear lengthens (§6.6).
- **Parallax** is *dry over bound*: a section's powder-dry
  background field drifts at 0.92× against its bound, glossier
  content layer at 1.0× — two material states of the same
  pigment, never two pictures. Amplitude capped at 14px.
- **Pinned scenes**: exactly one — the full mix (§6.5). A second
  pin is refused; a workshop has one slab.
- **Masked reveals** are *palette-knife wipes*: images inside
  cake frames are uncovered by a 500ms `--ease-mix` wipe in the
  direction of reading, with a powder edge (a 3px granular rim in
  the frame's pigment) left at the trailing side.
- **Blur-to-sharp is refused** except inside the grinding hero,
  where blur is literal (powder becoming paste, §6.1).
  Elsewhere powder does not blur — it *granulates*: reveals use
  a granular texture dissolve (an SVG turbulence mask at 3
  density steps), because a blurred cake would read as fog, and
  fog is another theme's material.
- **Animated counters** count *workshop figures only*: grind
  times in minutes, mesh numbers, grams — each counting once,
  from 88% of value to value, over `--dur-count`, when its
  ticket enters (§6.13).
- **Progress** is the margin smear (§6.6); there is no progress
  bar anywhere in the theme.
- **Marquees are refused.** Pigment does not run. The only
  horizontal band that moves is the boundary mix, and it moves
  because the visitor scrolls.
- **Granular dissolves** (the blur substitute above) run in
  three density steps — turbulence scale 0.9, 0.55, 0.3 over
  300ms — keyed to the same armed/observer pattern as every
  other reveal, with the middle step held 80ms longer than the
  others: powder clumps before it clears, and the uneven timing
  is what keeps the dissolve reading as grain rather than as a
  fade wearing a texture.
- **Ambient loops**: one — the hanging dust (§6.10), hero only,
  24 motes. A second ambient loop anywhere is a gate failure.
- **Micro-interactions**: binder-gloss hover (§6.7), muller
  click-grind (§6.8), cake tilt ≤3° on lift (§6.12).
- **Page transitions** are *palette-knife smears*: the next
  page's first pigment smears across at 450ms `--ease-mix`,
  content swaps beneath, the smear lifts (§6.16).
- **Smooth-scroll resistance**: the shared loop's lerp is the
  theme's friction — 0.12 dry, 0.09 in wet zones — implemented
  as lerped scrub values, never as scroll hijacking; the native
  scrollbar always tells the truth about position.


## 6. Signature elements

### 6.1 The grinding hero

- **What & why.** A pile of red-ochre powder sits on the hero's
  slab under a stone muller disc; on load the disc circles three
  revolutions over 1400ms, the pile blurring, spreading and
  smoothing into a paint smear that becomes the ground the
  headline stands on. It belongs because the merchant's first
  claim is *we grind what we sell* — and the hero proves it by
  manufacturing the page's own ground in front of the visitor
  before a word of sales copy is read. The headline does not
  have a background; it has a *product, mid-manufacture*.
- **Structure.** A real hero section on `--chalk`: the pile is a
  radial-gradient granular field (two layered SVG turbulence
  textures at 0.9 and 0.55 opacity, tinted `--red-ochre`) inside
  a 420×260px slab area; the muller is an inline SVG disc (stone
  grey is banned — the disc is drawn in `--raw-umber` line over
  `--chalk-dim`, both named) that travels a circular path via
  `offset-path`. The smear end-state is a second layer — a smooth
  `--red-ochre-bound` field with a knife-edge trailing rim —
  crossfaded in as the pile's blur peaks. The `<h1>` sits in the
  DOM above the slab, complete from first paint; the grind plays
  in the ground *beneath* it, never over the text.
- **Motion spec.** Trigger: load, gated on
  `document.fonts.ready` raced against 800ms; a late font prints
  the hero already ground (see fallback). Disc: 3 revolutions,
  1400ms `--dur-grind`, `--ease-grind`, radius shrinking 64px →
  18px as the pile spreads (a muller works inward). Pile blur
  0 → 6px across t=200–1100ms; granular texture opacity 1 →
  0.25; smear layer opacity 0 → 1 across t=700–1400ms. At
  t=1400ms the disc lifts 8px and rests at the slab's edge —
  the tool put down, not vanished.
- **States.** Unground (JS-armed only) → grinding → ground
  (rest; smear at full bound depth, disc at rest). Hover: none —
  the slab is not a control. Scrolled-past mid-grind: the grind
  completes on its own clock; returning visitors
  (`sessionStorage`) find the hero already ground.
- **Content merge.** The smear the grind produces *is* the
  headline's ground field for the rest of the session — the same
  DOM layer, not a copy of it. The hero's standfirst names the
  batch ("Ground this morning: PR102, batch 14"), so the
  performance and the stock record are one fact printed twice.
- **Failure fallback.** Watchdog at 1800ms: if the grind has not
  completed, pile, blur and disc snap to the ground end-state.
  No JS: the hero ships ground — smear layer at full opacity,
  disc at rest — because the shipped state is the finished
  state (§1, dry is shipped; here the *ground* state is the
  finished one, printed).
- **Reduced-motion variant.** No grinding. The hero stands
  ground, and beside the batch line a static three-frame strip
  (pile → paste → smear, three small fields) shows the process
  as a diagram — the information survives, the performance
  rests.
- **Performance budget & mobile variant.** Textures are two
  inline SVG filters, ≤9KB; the grind animates `transform`,
  `filter: blur` on one layer and opacity — no layout. Budget
  ≤1.6ms/frame on a mid phone. Mobile (<768px): the slab is
  300×190px, the grind runs 2 revolutions over 1100ms, and the
  blur is pre-baked into the smear layer's gradient (no live
  filter on a phone GPU).
- **Choreography timeline (v2).** t=0 fonts ready (or 800ms race
  lost → ground state, ceremony skipped) → t=0 disc drops 4px
  onto the pile → t=0–1400 three revolutions, radius 64→18px →
  t=200 blur begins → t=700 smear layer starts in → t=1100 blur
  peaks at 6px, texture at 0.25 → t=1400 disc lifts, rests →
  t=1450 headline bind begins (§6.2) → t=2100 hero complete.
- **State matrix (v2).** *Rest:* ground, disc at rest, smear
  bound. *Hover:* none. *Focus:* focus entering the hero
  completes a running grind instantly — a keyboard visitor is
  never asked to wait for paint before reading. *Active:* n/a.
  *Scrolled-past:* ground. *Disabled / no-JS:* ground at first
  paint. *Touch:* identical; first touch completes a running
  grind.
- **Breakpoints (v2).** ≥1200px: slab 420×260px, 3 revolutions,
  1400ms. 768–1199px: slab 360×220px, 3 revolutions, 1300ms.
  <768px: slab 300×190px, 2 revolutions, 1100ms, pre-baked blur.
- **Edge cases & failure modes (v2).** *Slow network:* textures
  are inline, so the grind never waits on an asset; if fonts
  lose the 800ms race the ceremony is skipped, not delayed.
  *Tab hidden mid-grind:* rAF pauses; on return, wall-clock past
  1800ms fires the watchdog snap. *Re-entry:* the grind runs
  once per session; a second run would claim the batch was
  ground twice (§9, failure 7).
- **Accessibility spec (v2).** The slab and disc are
  `aria-hidden`; the `<h1>` and batch line are complete text
  from first paint. The grind is never announced. Contrast under
  the headline is the smear's: chalk text on `--red-ochre-bound`
  measures 4.9:1 at display size — licensed at ≥24px; the
  standfirst sits on chalk in `--ink-earth` at 9.5:1.
- **Tokens consumed (v2).** `--red-ochre`, `--red-ochre-bound`,
  `--raw-umber`, `--chalk`, `--chalk-dim`, `--ease-grind`,
  `--dur-grind` (1400ms), `--dur-fallback-hero` (1800ms).

### 6.2 Dry-to-bound headline

- **What & why.** The hero headline's letters stamp in dry —
  matte, powdery, each with a 1px granular texture offset — and
  then a binder gloss sweeps across them over 600ms, leaving
  them glossy paint. Typography undergoes the product's process:
  the brand name is pigment first and paint second, in that
  order, because that is the order the workshop works in.
- **Structure.** A real `<h1>` in Alegreya 700, full text in the
  DOM. Each letter is wrapped (JS-only enhancement; the no-JS
  headline is one unwrapped line) in a span carrying two layers:
  a dry layer (the glyph in its pigment at matte texture, via a
  clipped turbulence background) and a bound layer (the glyph
  with a specular gradient, `background-clip: text`). The sweep
  is a 120px-wide gloss band moving across the bound layer's
  background-position; behind the band, letters rest bound;
  ahead of it, they rest dry.
- **Motion spec.** Trigger: the hero grind's completion
  (t=1450ms in §6.1's timeline), or load + 300ms if the grind
  was skipped. Letters stamp in dry over 8 × 45ms staggers
  (360ms total, `--ease-stamp`, 1px drop, texture offset
  resolving), hold dry for a 250ms beat — the visitor must
  *see* dry — then the gloss band sweeps left to right over
  600ms `--dur-gloss`, `--ease-gloss`. Total ceremony ≤1250ms.
- **States.** Dry (rest state before the sweep; also the shipped
  state) → sweeping → bound (rest). Hover/focus: none; the
  headline is not a control and never re-binds for attention.
  Scrolled-past: bound. The bind happens once per session.
- **Content merge.** The headline is the merchant's name and the
  page's `<h1>`; the ceremony is not an intro screen in front of
  the content, it is the name being made by the process the name
  sells. §3 law 3 confines the ceremony to this one headline.
- **Failure fallback.** Watchdog at 1600ms from arming: letters
  snap to bound, band removed. No JS: the headline stands dry —
  matte is a complete, honest state for type in this theme, and
  §2's dry contrast (chalk on dry red ochre is *not* used;
  the headline is set in `--red-ochre-deep` on chalk, 5.7:1)
  keeps it fully legible unbound.
- **Reduced-motion variant.** The headline stands dry, with its
  pigment and index named in the standfirst — the dry state is
  the information; the sweep is the only thing that rests.
- **Performance budget & mobile variant.** Two text layers on
  one line; the sweep animates `background-position` only.
  ≤6KB of texture. Mobile: the stamp stagger compresses to
  8 × 30ms and the gloss band widens to 160px so the sweep reads
  at 34px type.
- **Choreography timeline (v2).** t=0 (grind complete) → letters
  stamp dry, 45ms stagger → t=360 all dry → t=360–610 dry hold
  → t=610 gloss band enters left → t=1210 band exits right,
  letters bound → t=1250 band layer removed from the DOM.
- **State matrix (v2).** *Rest (pre-ceremony):* dry, complete,
  legible. *Hover:* none. *Focus:* focus into the hero completes
  the bind instantly. *Active:* n/a. *Scrolled-past:* bound.
  *Disabled / no-JS:* dry, permanently — a valid end state.
  *Touch:* identical; no touch state on type.
- **Breakpoints (v2).** ≥1200px: 56px, band 120px, stagger 45ms.
  768–1199px: 44px, band 120px, stagger 40ms. <768px: 34px,
  band 160px, stagger 30ms, ceremony cap 1000ms.
- **Edge cases & failure modes (v2).** *Headline longer than 14
  letters:* stagger compresses to fit the 1250ms cap; longer
  than 24 letters is refused at build (§12 — a merchant's name
  is not a sentence). *CMS-edited headline:* letter spans are
  generated at runtime from the `<h1>` text, so an edited name
  re-wraps correctly; an edit that changes the pigment named in
  the standfirst is a content error, caught by §10's audit.
  *Font swap:* spans are generated only after
  `document.fonts.ready`.
- **Accessibility spec (v2).** The `<h1>` carries the plain text;
  letter spans are `aria-hidden` duplicates of it (the heading
  is exposed once, whole). The sweep is never announced.
  Contrast in both states is licensed: dry `--red-ochre-deep` on
  chalk 5.7:1; bound state darkens the same letters to the deep
  mix at 5.7:1 — the gloss band is a highlight *above* the
  licensed colour and never the colour itself.
- **Tokens consumed (v2).** `--red-ochre-deep`, `--chalk`,
  `--ease-stamp`, `--ease-gloss`, `--dur-gloss` (600ms),
  `--dur-stagger-letter` (45ms).

### 6.3 Cake-slot sections

- **What & why.** Every content section is a cake: as it reaches
  reading position it slides laterally 24px into its tin slot
  and seats with a granular settle — a three-step judder, 40ms
  apart, amplitudes 3px, 2px, 1px — the small shudder of a
  pressed cake dropping into a tin. It belongs because the
  layout *is* the catalogue: the reader opens the box one cake
  at a time, in tin order, and the settle is the sound of the
  box being handled.
- **Structure.** Each `<section>` is a slot: a full-bleed field
  (a pigment anchor or a chalk sheet) with the §4 recess line
  and matte offset, containing its content in the standard
  measure. The slide is a `transform: translateX(-24px)` armed
  state on the slot's inner field only — the slot frame itself
  never moves, so boundaries (§6.4) stay registered while the
  cake seats inside them.
- **Motion spec.** Trigger: slot top crossing 78% viewport
  height, via the shared loop reading the lerped scroll value.
  Slide: 380ms `--dur-settle`, `--ease-settle`, from −24px to
  0; then the judder: three steps at +0/+40/+80ms, offsets
  +3px/−2px/+1px on the Y axis, each 40ms `--dur-judder` linear —
  granular, not springy. Total 460ms. A slot seats once; seating
  is latched.
- **States.** Unseated (JS-armed only, field at −24px, content
  fully rendered and legible — the slide is positional, never a
  fade) → seating → seated (rest). Hover: none at section level.
  Scrolled-past unseated (fast fling): seats instantly with no
  judder — a cake flung past is a cake placed.
- **Content merge.** The section's field is its pigment's cake:
  the green-earth section is *in* green earth, its ticket
  (§6.12) stamped with PG23. The settle is the box admitting the
  reader to that pigment; there is no separate reveal chrome.
- **Failure fallback.** Watchdog per slot at 1200ms after first
  intersection: field snaps to 0, judder cancelled. No JS: every
  field ships seated at 0 — the shipped page is the full tin,
  open.
- **Reduced-motion variant.** No slide, no judder. Slots ship
  seated; the recess line alone marks the slot.
- **Performance budget & mobile variant.** One transform per
  slot, compositor-only; judder is three keyframed steps, no
  per-frame JS. Mobile (<768px): slide distance 12px, judder
  two steps (2px, 1px) — a smaller tin, a smaller shudder.
- **Choreography timeline (v2).** t=0 slot top crosses 78% →
  t=0–380 slide −24→0px `--ease-settle` → t=380 judder +3px →
  t=420 −2px → t=460 +1px → t=500 seated; the slot's counters
  (§6.13) start at t=460 if the slot carries them.
- **State matrix (v2).** *Rest:* seated. *Hover:* n/a. *Focus:*
  focus landing inside an unseated slot seats it instantly
  (focus never waits for furniture). *Active:* n/a.
  *Scrolled-past:* seated instantly, judder skipped. *Disabled /
  no-JS:* seated. *Touch:* identical; fling velocity above
  2.5px/ms counts as scrolled-past.
- **Breakpoints (v2).** ≥1200px: 24px slide, 3-step judder.
  768–1199px: 18px slide, 3-step judder. <768px: 12px slide,
  2-step judder, slots stack full-width.
- **Edge cases & failure modes (v2).** *Slot taller than the
  viewport* (a long catalogue section): the trigger is the
  slot's *top*, so a tall cake still seats once, at entry.
  *Anchor jump into mid-page:* all slots above the jump target
  are seated instantly; the target slot seats without judder.
  *Scroll back up:* seated slots never unseat — a cake taken
  from the tin is not put back by looking away.
- **Accessibility spec (v2).** The slide moves a fully rendered
  section 24px; text is legible at every frame (no opacity is
  ever animated on content). Focus order is DOM order; the
  transform does not affect it. The judder is 3px maximum —
  below vestibular concern, and removed entirely under
  reduced motion.
- **Tokens consumed (v2).** `--chalk-dim`, `--ease-settle`,
  `--dur-settle` (380ms), `--dur-judder` (40ms), `--slot-slide`
  (24px).


### 6.4 Live boundary mixing

- **What & why.** At every section boundary, a 120px band blends
  the two adjacent pigments, scrubbed by scroll: as the boundary
  crosses the viewport's reading line the mix ratio runs from
  the upper pigment to the lower, passing through the true
  intermediate earths — red ochre genuinely becomes a mixed
  earth tone where it meets yellow ochre. It belongs because
  mixing is the theme's central verb, and here the page performs
  it with its own body rather than describing it: the two
  product families on either side are the ingredients.
- **Structure.** The band is a dedicated element between slots
  with a `color-mix(in srgb, var(--pig-a) calc(100% - var(--mix)), var(--pig-b) var(--mix))`
  background, where `--pig-a`/`--pig-b` are set from the two
  neighbouring slots' pigment tokens and `--mix` (0–100) is
  written by the shared loop. The band carries the printed
  recipe in the index voice at its centre — "PR102 : PY43 —
  1 : 1 AT THE LINE" — updating its stated ratio at the 25/50/75
  crossings. A 3px knife-drag streak (a lighter line in the mix
  at +8% lightness) runs through the band's middle third.
- **Motion spec.** Trigger: continuous scrub. `--mix` follows
  the boundary's position between 65% and 35% viewport height,
  mapped 0→100 and lerped at the wet rate 0.09 — the mix lags
  the scroll slightly, the way a dragged knife lags the hand.
  The recipe text crossfades (200ms) at each quarter crossing.
  Fully reversible: scroll up and the mix un-mixes, ratio
  running home.
- **States.** Rest: the band sits at whatever ratio the scroll
  position dictates — at page load, boundaries below the fold
  rest at 0 (pure upper pigment at their top edge). Hover: none.
  Scrolled-past: 100 (pure lower pigment). The band is never
  animated on a timer; it has no life of its own.
- **Content merge.** The band's two ingredients are the actual
  colour fields of the sections it separates, and its recipe
  line names them by index. The mix is not a gradient decoration
  between contents; it is the two contents, combined, with the
  combination documented on its face.
- **Failure fallback.** No JS: `--mix` rests at 50 and the band
  shows the true midpoint mix with the recipe printed as
  "1 : 1" — the honest static form of a blend. If `color-mix()`
  is unsupported, the band falls back to the pre-computed
  midpoint hex of its declared pair (each pair's midpoint is a
  declared token in the build, listed in the colophon like any
  other colour).
- **Reduced-motion variant.** The band rests at its 50% mix with
  the 1 : 1 recipe, static — colours shown pre-mixed, as the
  original entry's safety rule requires.
- **Performance budget & mobile variant.** One custom property
  write per band per frame, background repaint of a 120px strip
  only; ≤4 bands exist on any page. Mobile: band height 64px,
  recipe line shortens to the two index names ("PR102 : PY43"),
  ratio stated at the line only.
- **Choreography timeline (v2).** Boundary enters 65% line →
  `--mix` 0→25 across the first quarter of travel (recipe: "3 :
  1") → 50 at the reading line (recipe "1 : 1", knife streak at
  full contrast) → 75 ("1 : 3") → exits 35% line at 100, band
  rests as the lower pigment's leading edge.
- **State matrix (v2).** *Rest:* at scroll-dictated ratio.
  *Hover:* none. *Focus:* none — the band holds no focusables.
  *Active:* n/a. *Scrolled-past:* 100. *Disabled / no-JS:* 50,
  static, recipe printed. *Touch:* identical scrub; the 0.09
  lerp keeps the mix smooth under fling.
- **Breakpoints (v2).** ≥1200px: 120px band, full recipe line.
  768–1199px: 96px band, full recipe. <768px: 64px band, index
  names only in the band; full recipe moves to the colophon.
- **Edge cases & failure modes (v2).** *Non-neighbour pairs:*
  the build refuses a band whose two pigments are not adjacent
  in tin order unless the sections themselves are adjacent on
  the page — adjacency on the page is what licenses the mix
  (§1). *Editorial reorder:* bands are generated from the DOM's
  actual neighbours at build, so a reordered page re-recipes
  itself. *Jump scroll:* `--mix` snaps to the position's true
  value on the next frame — the lerp never leaves a band
  showing a ratio its position contradicts by more than one
  frame.
- **Accessibility spec (v2).** The band is decorative
  (`aria-hidden`); its recipe is duplicated in the colophon as
  real text for any reader who wants the mixes enumerated. No
  text sits on the band except the recipe line, set in
  `--ink-earth` on a chalk chip (9.5:1) — never directly on the
  mix, whose contrast varies by design.
- **Tokens consumed (v2).** `--mix` (per-band custom property),
  the neighbouring slots' pigment tokens, `--ink-earth`,
  `--chalk`, `--ease-mix`, `--lerp-wet` (0.09).

### 6.5 The pinned full mix

- **What & why.** The process section pins for 150vh while a raw
  earth lump scrubs through four stages — lump → powder → paste
  → finished paint stroke — crossfading with the scroll, a
  muller disc circling throughout. It is the theme's thesis
  performed at reading speed: the recipe printed beside it
  ("grind 40 minutes, mull in gum arabic, rest overnight") is
  enacted by the page, stage by stage, at the pace the visitor
  chooses. If §6.1 is the claim, this is the evidence.
- **Structure.** A 150vh pin track containing a sticky stage:
  left, the material — four stacked layers of the same form (an
  SVG earth lump; a granular powder field; a paste smear with
  knife marks; a finished stroke — a single confident
  `--red-ochre-bound` brush band with a dry trailing edge),
  crossfaded by stage weights written from the shared loop.
  Right, the recipe text in four steps, the current step's index
  line inked, the others at 55%. The muller disc (as §6.1)
  circles the material area at a radius keyed to the stage —
  wide over the lump, tight over the paste, still over the
  stroke.
- **Motion spec.** Trigger: scroll through the pin, scrubbed,
  lerp 0.09. Stage weights: lump 1→0 across pin progress
  0–0.3; powder peaks 0.15–0.5; paste 0.4–0.8; stroke 0.7–1.0,
  drawn by a clip wipe in its final tenth so the stroke is
  *laid*, not faded in. Muller: one revolution per 0.25 of pin
  progress (4 total), radius 70px → 26px → 0. Recipe steps
  activate at progress 0.05 / 0.35 / 0.62 / 0.88.
- **States.** Rest (before pin): lump, recipe step 1 inked.
  Scrubbing: stages weighted as above, fully reversible — scroll
  up and paint un-makes itself back to earth, because the
  demonstration is a scrub, not a latch. Scrolled-past: the
  finished stroke, all four recipe steps inked (the recipe has
  been read). Hover: none.
- **Content merge.** The material being mixed is the pigment the
  adjacent catalogue sells, the recipe is the merchant's actual
  process printed in §8.2's worked form, and the finished stroke
  is the same stroke that appears, at rest, on the product
  ticket for PR102 (§6.12) — one stroke, drawn once, used as
  the product's portrait everywhere.
- **Failure fallback.** No JS / no pin support: the four stages
  print as a vertical four-frame strip beside the recipe (the
  reduced-motion form), each frame captioned — the process is
  content, and content ships. Watchdog: if the pin's sticky
  fails (a browser quirk), the track collapses to the strip
  form within one frame of detection.
- **Reduced-motion variant.** The four-frame strip, static, with
  the muller drawn at rest on the paste frame. No pin, no scrub.
- **Performance budget & mobile variant.** Four layers, opacity
  and one clip-path animated; the muller is one transform.
  ≤1.6ms/frame. Mobile (<768px): the pin shortens to 110vh, the
  layout stacks (material above recipe), the muller makes 2
  revolutions; below 480px the pin is dropped entirely in favour
  of the strip — a phone reader gets the recipe, not the
  theatre.
- **Choreography timeline (v2).** Pin engages → p=0.05 step 1
  inks, muller starts wide → p=0.15–0.3 lump powders → p=0.35
  step 2 → p=0.4–0.5 paste forms, muller tightens → p=0.62 step
  3 → p=0.7 stroke begins under the paste → p=0.88 step 4 →
  p=0.9–1.0 stroke clip-wipes to full, muller rests → pin
  releases with the stroke complete.
- **State matrix (v2).** *Rest:* lump + step 1. *Hover:* none.
  *Focus:* focus entering the recipe does not move the scrub;
  the stage weights follow scroll only, so a keyboard reader's
  place is never stolen. *Active:* n/a. *Scrolled-past:*
  finished stroke, recipe fully inked. *Disabled / no-JS:*
  four-frame strip. *Touch:* identical scrub; fling settles to
  the true stage within the 0.09 lerp's reach (~300ms).
- **Breakpoints (v2).** ≥1200px: 150vh pin, side-by-side.
  768–1199px: 130vh pin, side-by-side at narrower measure.
  <768px: 110vh stacked; <480px: strip, no pin.
- **Edge cases & failure modes (v2).** *Reader scrolls fast
  through:* stage weights are pure functions of pin progress —
  any position shows its true stage, no state can be skipped
  into inconsistency. *Reader dwells mid-pin:* the muller idles
  at its stage radius with a 2% radius breathing (±1.5px, 4s) —
  the only sub-loop in the element, and it stops the moment
  scroll resumes. *Print:* the strip form prints.
- **Accessibility spec (v2).** The stage area is `aria-hidden`
  theatre; the recipe is real text, all four steps readable in
  order regardless of scrub position (inactive steps at 55% use
  `--ink-earth` at 55% over chalk = 5.4:1 effective, licensed
  for 17px text). A visually hidden summary states the process
  in one sentence for AT.
- **Tokens consumed (v2).** `--red-ochre`, `--red-ochre-bound`,
  `--raw-umber`, `--chalk`, `--ink-earth`, `--ease-mix`,
  `--lerp-wet` (0.09), `--pin-mix` (150vh).

### 6.6 Margin paint-smear progress

- **What & why.** In the left margin rail, a paint smear
  lengthens with scroll: a test streak pulled in the current
  section's pigment, changing pigment at each section boundary,
  until at the footer it stands complete as a five-stripe
  palette swatch — the site's palette card, earned by reading.
  It belongs because painters really do check colour as a smear
  on the slab's edge; progress here is not a bar filling but a
  colour being tested, section by section.
- **Structure.** A fixed rail element (72px wide ≥1200px)
  holding one smear segment per section: each segment is a
  26px-wide streak with a knife-dragged top edge (an SVG mask)
  in its section's pigment, its height proportional to the
  section's share of page length. Beside each segment, in the
  index voice rotated 0° and set small, the pigment's index
  name (PR102, PY43…) appears when its segment completes. At
  the footer the rail's segments align into the stripe beside
  the colophon (§6.17), which lists the same five in the same
  order.
- **Motion spec.** Trigger: continuous scrub via the shared
  loop, lerp 0.12. The active segment's length follows the
  reader's progress through its section (scaleY from the
  segment's top, transform-origin top); on section completion
  the segment's end snaps the last 4% over 200ms `--dur-smear`
  `--ease-mix` — the knife lifting. Pigment changes are exact at
  boundaries: the new segment begins in the new pigment, and
  the boundary between segments shows the §6.4 mix at 50% as a
  6px blend line.
- **States.** Rest: segments complete above the reading line,
  the active segment partial, the rest un-pulled (shown as a
  2px chalk-dim hairline — the slab's clean edge). Hover:
  hovering a completed segment shows its pigment's name and
  grind time in a ticket tooltip (§11). Scrolled-past: all
  segments complete, stripe whole. The smear never animates on
  a timer.
- **Content merge.** The smear's segments are the sections'
  own pigments in the sections' own proportions, and its final
  form is the colophon's palette stripe — progress, catalogue
  and colophon are three printings of one list, and §10's gate
  checks they agree stripe for stripe.
- **Failure fallback.** No JS: the rail ships with the complete
  stripe printed (all segments full, all index names shown) —
  as navigation furniture it must never depend on the reader's
  position to exist. Watchdog: if the loop stalls, segments
  snap to the scroll position's truth on the next frame.
- **Reduced-motion variant.** The complete stripe, static, with
  index names — a palette card in the margin from the start.
- **Performance budget & mobile variant.** One scaleY per active
  segment; completed segments are never repainted. Mobile
  (<768px): the rail retires; progress becomes a 4px top stripe
  of five fixed segments that fill in the current pigment — the
  same information, bench-less.
- **Choreography timeline (v2).** Section entered → its segment
  begins pulling within 100ms → segment tracks section progress
  → boundary crossed → segment snaps its last 4% (200ms), index
  name fades in (300ms), blend line prints → next segment begins
  → footer reached → rail aligns with the colophon stripe.
- **State matrix (v2).** *Rest:* truthful partial stripe.
  *Hover:* ticket tooltip on completed segments (pointer only).
  *Focus:* segments are not focusable; the colophon carries the
  same list as text. *Active:* n/a. *Scrolled-past:* complete.
  *Disabled / no-JS:* complete stripe printed. *Touch:* no
  hover; index names show on completion only.
- **Breakpoints (v2).** ≥1200px: 72px rail, names beside
  segments. 768–1199px: 48px rail, names appear in the tooltip
  position only. <768px: top stripe form, no names (names live
  in the colophon).
- **Edge cases & failure modes (v2).** *A page with two sections
  or nine:* segments are generated from the DOM's sections and
  their pigments — two segments or nine, the stripe is the
  page's truth, and the colophon is generated from the same
  list. *Very short final section:* its segment has a 24px
  minimum height so the last pigment is never a sliver.
  *Scroll to top:* segments un-pull above the reading line —
  the smear is a position instrument, not a trophy; only the
  footer's stripe is permanent.
- **Accessibility spec (v2).** The rail is `aria-hidden`
  decoration; a visually hidden `role="progressbar"` is *not*
  used — reading progress is not announced. The palette list is
  real text in the colophon. Segment pigments are never the
  only carrier of section identity (each section's ticket
  prints its index name in text).
- **Tokens consumed (v2).** All five anchor tokens (per
  segment), `--chalk-dim`, `--ink-earth`, `--ease-mix`,
  `--dur-smear` (900ms cycle; 200ms snap), `--lerp-dry` (0.12).


### 6.7 Binder-gloss hover

- **What & why.** Hovering a product card sweeps a gloss sheen
  across its matte cake surface, following the pointer's
  x-position, and the card's colour saturates ~10% under the
  gloss: dry pigment becoming wet paint under the visitor's own
  hand. It belongs because binding is the moment pigment turns
  into the product being sold — and the theme gives that moment
  to the visitor's attention rather than to a "buy" button's
  styling. A card you have looked at properly is, briefly,
  paint.
- **Structure.** The card (§6.12) carries a gloss layer: a
  140px-wide linear-gradient sheen (chalk at 0% → 18% → 0%)
  clipped to the card's cake face, positioned by a `--gloss-x`
  custom property written from pointermove through the shared
  loop (lerp 0.2 for this layer — gloss is quick). Beneath it, the
  cake face's filter saturates from 1.0 to 1.1 and its colour
  crossfades 30% toward the pigment's bound variant. Both layers
  are `pointer-events: none` and sit above the face, below the
  card's text.
- **Motion spec.** Trigger: pointerenter / pointermove on fine
  pointers. Sheen in: 240ms `--ease-gloss`; tracking: continuous
  while hovered; out: 400ms `--ease-gloss` fade with the
  saturation relaxing over 600ms — gloss dries slower than it
  wets. Keyboard focus produces the same bind, centred, over
  300ms (focus is attention too).
- **States.** Rest: matte, dry, saturation 1.0. Hover: gloss
  tracking, saturation 1.1, 30% bound blend. Focus: gloss
  centred, same blend. Active (pressed): the gloss holds while
  §6.8's grind begins. Scrolled-past: matte — a card leaves the
  viewport dry, always. Disabled (sold-out card): no gloss; the
  cake stays dry and its ticket says so (§6.12).
- **Content merge.** The gloss binds the *product's own swatch* —
  the cake face is the pigment the card sells, at its true
  colour; the sheen never touches the card's text or price. The
  interaction is the product demonstration, not a highlight
  effect pasted over it.
- **Failure fallback.** No JS: cards rest matte with their bound
  variant shown as a static 12px bound stripe at the cake's foot
  — the bound colour is still shown, unperformed. If
  pointermove is unavailable (touch), see the touch ruling in
  the state matrix.
- **Reduced-motion variant.** No sheen sweep. Hover/focus swaps
  the cake face instantly to its bound variant (a state change,
  not a motion) — the dry/bound information survives intact.
- **Performance budget & mobile variant.** One gradient layer
  and one filter per hovered card, one card at a time by
  construction. Touch devices: no hover gloss; a tap binds the
  card for 900ms (the same blend, centred) before the tap's
  navigation or grind proceeds — the tap is the touch
  equivalent of the look.
- **Choreography timeline (v2).** t=0 pointer enters → t=0–240
  sheen fades in at pointer x → saturation ramps 1.0→1.1 across
  300ms, bound blend 0→30% → tracking at lerp 0.2 while hovered
  → pointer leaves → t=0–400 sheen out → t=0–600 saturation
  relaxes to 1.0, blend to 0 → card dry.
- **State matrix (v2).** *Rest:* matte. *Hover:* gloss tracking.
  *Focus:* gloss centred, 300ms in. *Active:* gloss held under
  the grind swirl (§6.8). *Scrolled-past:* matte. *Disabled:*
  no gloss, ever — a sold-out cake cannot be bound.
  *Touch:* tap binds 900ms centred; no tracking.
- **Breakpoints (v2).** ≥1200px: sheen 140px, full tracking.
  768–1199px: sheen 120px. <768px: cards are full-width; gloss
  applies on tap-bind only (no hover exists), sheen 160px.
- **Edge cases & failure modes (v2).** *Pointer crosses the card
  quickly:* the 240ms in-ramp means a passing pointer barely
  wets the surface — correct behaviour, a glance is not a bind.
  *Pointer over the card's text:* the gloss layer sits below
  text; legibility is unchanged at every gloss position.
  *Multiple cards, fast sweeping:* only the currently hovered
  card holds gloss; the previous card's dry-out continues
  independently.
- **Accessibility spec (v2).** The gloss is decorative and never
  announced; the bound state is *also* conveyed by the card's
  ticket, which gains the word "BOUND" in the index voice while
  glossed — a non-visual channel for the same fact. Contrast of
  card text is measured on the dry face and is unchanged by the
  gloss (text sits above the sheen at full opacity).
- **Tokens consumed (v2).** The card pigment's anchor + bound
  tokens, `--chalk`, `--ease-gloss`, `--dur-gloss` (600ms),
  `--lerp-gloss` (0.2).

### 6.8 Muller click-grind

- **What & why.** Clicking a product card spins a small muller
  swirl — a rotating arc, 500ms — at the click point, and the
  card's colour deepens one permanent step; a tiny "GROUND
  FINER" note appears on its ticket. Three grinds take a cake
  from *coarse* to *fine* to *extra fine*, each step a real,
  deeper saturation of the same pigment. The interaction performs
  the craft verb on the actual product: grinding is both the
  feedback and a state of the goods, kept for the session.
- **Structure.** The swirl is an inline SVG arc (stroke in the
  pigment's deep mix) centred on the click coordinates within
  the card, rotating 300° over `--dur-swirl` while shrinking
  28px → 16px. Deepening is a stepped class on the card
  (`data-grind="0|1|2|3"`) driving the cake face's blend toward
  its bound variant: 0% / 25% / 50% / 75%, with the ticket's
  grind line rewriting itself — "GROUND COARSE" → "GROUND FINE"
  → "GROUND EXTRA FINE" — and the "GROUND FINER" note flashing
  once per grind beside it.
- **Motion spec.** Trigger: click/tap on the card's cake face
  (not on its links or buttons, which keep their own jobs).
  Swirl: 500ms `--ease-grind`, one rotation, then removed.
  Deepening crossfade: 350ms `--ease-mix`, starting at t=150ms
  (as the swirl's pressure peaks). Note: fades in at t=300ms,
  holds 1200ms, fades 300ms. At grind 3 the face is capped —
  further clicks swirl but do not deepen, and the note reads
  "FULLY GROUND".
- **States.** Rest: at its session grind step. Hover: §6.7's
  gloss runs beneath the swirl. Active: swirl + deepening.
  Scrolled-past: grind state persists (sessionStorage) — a cake
  you ground stays ground when you scroll back. Disabled:
  sold-out cards do not grind; the click does nothing and the
  ticket's "OUT OF STOCK" line is why.
- **Content merge.** The grind state is product information: the
  order form (§6.15) reads the card's grind step and pre-selects
  the matching fineness for that pigment — what you ground is
  what you are offered to buy. The click is not a game layered
  on the catalogue; it sets the catalogue's state.
- **Failure fallback.** No JS: cards rest at grind 0 with their
  fineness printed as a plain fact on the ticket ("GROUND
  COARSE — finer grinds at the counter"), and the order form
  offers all three finenesses as ordinary radio choices. The
  swirl's absence loses nothing but the gesture.
- **Reduced-motion variant.** No swirl. A click deepens the step
  instantly and the note appears statically for 1200ms. The
  state machine is identical; only the rotation rests.
- **Performance budget & mobile variant.** One small SVG per
  click, removed after 500ms; deepening is a background
  crossfade on one card. Mobile: identical — tap is the natural
  grind gesture — with the swirl at 36px for thumb legibility.
- **Choreography timeline (v2).** t=0 click → swirl fades in at
  click point → t=0–500 rotation 300°, radius 28→16px → t=150
  deepening crossfade begins (350ms) → t=300 "GROUND FINER"
  note in → t=500 swirl removed → t=1500 note out → card rests
  one step deeper, ticket rewritten.
- **State matrix (v2).** *Rest:* session grind step shown.
  *Hover:* gloss (§6.7) under everything. *Focus:* Enter/Space
  on a focused card grinds it, swirl centred — the verb is
  keyboard-complete. *Active:* as timeline. *Scrolled-past:*
  state kept. *Disabled:* no grind, no swirl. *Touch:* tap =
  click, same timeline.
- **Breakpoints (v2).** ≥1200px: swirl 28px. 768–1199px: 28px.
  <768px: swirl 36px, note set at 12px to fit the card's ticket.
- **Edge cases & failure modes (v2).** *Rapid clicking:* clicks
  during a running swirl queue one pending grind; a third click
  is ignored until the queue clears — the muller cannot be in
  two places. *Grind then navigate away and back:* session state
  restores the step and the ticket line, without replaying the
  swirl. *A pigment with no bound variant in §2:* impossible by
  construction — every anchor ships a bound row, and §10 audits
  it.
- **Accessibility spec (v2).** The grind is a real button
  behaviour on the card face (`role="button"` region with
  `aria-label="Grind [pigment] finer"`), and each grind writes
  its result to a visually hidden live region ("Red ochre now
  ground fine") — the deepening is never colour-only
  information. Focus outline is the §11 standard: 2px
  `--ink-earth` offset 2px, visible on every pigment face.
- **Tokens consumed (v2).** The card pigment's anchor, bound and
  deep tokens, `--ease-grind`, `--ease-mix`, `--dur-swirl`
  (500ms).

### 6.9 Muller-and-slab diagram

- **What & why.** In the process section, an SVG diagram of the
  grinding slab, the muller and a pigment pile strokes itself in
  over ~1.5s, each part labelled as it is drawn — slab, muller,
  pile, knife. It belongs because the tool is the trade: the
  diagram teaches the visitor to read every other element on the
  page (the hero's disc, the click's swirl) by showing the
  instrument whole, drawn with the same stroke discipline the
  painter uses.
- **Structure.** One inline SVG, four path groups in the
  pigment's deep mix at 2px stroke, each with
  `pathLength="100"` and a dashoffset armed state; labels are
  real HTML text beside leader lines (never SVG text, so they
  scale and translate with the page), each label fading in as
  its part completes. The drawing order is the using order:
  slab (the ground) → pile (the material) → muller (the tool) →
  knife (the test).
- **Motion spec.** Trigger: the diagram's top crossing 70%
  viewport height, once. Total 1500ms `--dur-draw`: slab
  0–450ms, pile 350–750ms (overlapping — the pile sits *on* the
  slab), muller 700–1150ms, knife 1100–1500ms, each
  `--ease-mix`; labels at each part's completion +100ms, 250ms
  fade. The drawn state is the shipped state; arming is
  JS-only.
- **States.** Rest (shipped): fully drawn, all labels present.
  Drawing: per timeline. Scrolled-past un-drawn (fling): drawn
  instantly. Hover: hovering a part re-inks its label in the
  deep mix and thickens its stroke to 3px for as long as
  hovered — the diagram answers handling like the tool does.
  Focus: each part group is focusable in order with the same
  re-ink.
- **Content merge.** The diagram stands inside the process
  recipe (§6.5) at the step where the tools are named; its
  labels use the recipe's own words. It is the recipe's plate,
  not an illustration break.
- **Failure fallback.** No JS: drawn, labelled, complete — the
  shipped state. Watchdog at 2000ms after trigger: any undrawn
  part snaps drawn. A browser without dashoffset support shows
  the drawn state (the armed state is applied via a class only
  added when the API exists).
- **Reduced-motion variant.** Drawn and labelled from the start;
  hover/focus re-ink still applies (it is a state, not a
  motion).
- **Performance budget & mobile variant.** One SVG ≤7KB,
  animating dashoffset on four paths. Mobile: the diagram
  scales to full measure width; labels stack beneath their
  parts in reading order rather than beside them, and the draw
  compresses to 1100ms.
- **Choreography timeline (v2).** t=0 trigger → slab draws
  0–450 → label "SLAB" at 550 → pile 350–750 → label at 850 →
  muller 700–1150 → label at 1250 → knife 1100–1500 → label
  "KNIFE — FOR THE TEST SMEAR" at 1600 → diagram at rest.
- **State matrix (v2).** *Rest:* drawn. *Hover:* part re-inks.
  *Focus:* part re-inks, label announced via `aria-describedby`.
  *Active:* n/a. *Scrolled-past:* drawn. *Disabled / no-JS:*
  drawn. *Touch:* tap = hover's re-ink, held 900ms.
- **Breakpoints (v2).** ≥1200px: diagram 520px wide, labels
  beside. 768–1199px: 440px, labels beside. <768px: full width,
  labels beneath, 1100ms draw.
- **Edge cases & failure modes (v2).** *Diagram in a slot that
  seats late:* the draw trigger waits for the slot's settle
  (§6.3) to finish, so the drawing never fights the judder.
  *Reader scrolls away mid-draw:* the draw completes off-screen
  on its own clock; returning finds it drawn. *Print:* drawn
  state prints.
- **Accessibility spec (v2).** The SVG is `role="img"` with a
  full text alternative ("A stone slab; on it a pile of red
  ochre; a muller resting on the pile; a palette knife beside
  them") — the drawing performance is never the only carrier.
  Labels are HTML text at 13px minimum, `--ink-earth` on chalk
  (9.5:1).
- **Tokens consumed (v2).** `--red-ochre-deep`, `--ink-earth`,
  `--chalk`, `--ease-mix`, `--dur-draw` (1500ms).


### 6.10 Hanging pigment dust

- **What & why.** In the hero's light, 24 fine dust motes drift
  at 3–6px/s, tinted red ochre, denser near the pile. A grinding
  room's air is full of the material; the dust is the workshop's
  atmosphere made visible, and it hangs over the hero copy
  because the hero is where the grinding happens. It is the
  theme's single licensed ambient loop (§5), rationed hard.
- **Structure.** One `<canvas>` absolutely positioned over the
  hero's slab area only (never over the headline's text block —
  the dust field's bounds are the slab plus a 40px halo), 24
  particles with seeded positions, sizes 1–2.5px, opacity
  0.25–0.5 in `--red-ochre`. Density falls off with distance
  from the pile's centre by the seeding, not by a runtime
  calculation. The canvas is `pointer-events: none` and
  `aria-hidden`.
- **Motion spec.** Trigger: time loop, only while the hero is in
  view (IntersectionObserver gates the loop; off-screen, the
  canvas is not drawn at all). Each mote drifts on a slow sine
  wander at 3–6px/s with a 0.5px/s downward settle — dust falls,
  barely. No mote ever crosses into the headline's line box: the
  field's top edge stops 16px below the headline's baseline
  zone.
- **States.** Rest: drifting while hero visible. Hover: none —
  the dust does not react to the pointer (air is not a control).
  Scrolled-past: loop stopped, canvas cleared. Disabled:
  `prefers-reduced-motion` or a `save-data` hint stops the loop
  entirely and the canvas is removed.
- **Content merge.** The dust is tinted with the hero pigment
  and sourced from the pile's position: it is the grind's
  by-product, drawn only where grinding occurs on the page. It
  appears in no other section — dust in the catalogue would be
  atmosphere pasted over content, and §9 names it a failure.
- **Failure fallback.** No canvas support or no JS: no dust, and
  nothing is missing — the element is atmosphere only, carrying
  zero information. A static granular texture in the slab field
  (§6.1) already gives the hero its grain.
- **Reduced-motion variant.** Removed entirely. Not paused —
  removed; a frozen dust field would read as dirt on the
  screen.
- **Performance budget & mobile variant.** 24 particles on one
  small canvas, ≤0.3ms/frame; the loop sleeps off-screen.
  Mobile: 12 motes, sizes 1–2px, same field rules.
- **Choreography timeline (v2).** Hero enters → loop starts
  within 200ms, motes fade in over 800ms (a hard cut of dusty
  air appearing would be noticeable; a fade is air thickening)
  → drift continuous → hero leaves → loop stops within one
  frame, canvas cleared (no fade-out: unseen is unseen).
- **State matrix (v2).** *Rest:* drifting, hero in view.
  *Hover:* none. *Focus:* none. *Active:* n/a. *Scrolled-past:*
  stopped and cleared. *Disabled:* removed (reduced motion /
  save-data / no canvas). *Touch:* identical; no touch state.
- **Breakpoints (v2).** ≥1200px: 24 motes over the 420px slab.
  768–1199px: 18 motes. <768px: 12 motes over the 300px slab.
- **Edge cases & failure modes (v2).** *Low-power device:* if
  the shared loop's frame budget (§14) is exceeded twice in a
  second, the dust is the first thing cut — it is the budget's
  designated first sacrifice, named here so no builder cuts
  anything else first. *Hero resized:* the field re-seeds to
  the new slab bounds on resize, debounced 300ms.
- **Accessibility spec (v2).** Pure decoration: `aria-hidden`,
  no alternative text, no information. Opacity cap 0.5 and size
  cap 2.5px keep it below distraction thresholds for low-vision
  readers, and its exclusion zone keeps it off all text.
- **Tokens consumed (v2).** `--red-ochre`, `--dur-fade-air`
  (800ms).

### 6.11 The tin lid — navigation

- **What & why.** The site's header is the tin's lid: a chalk
  band carrying the merchant's name and, beneath it, the nav as
  a row of cake labels — each destination printed in its
  section's pigment with its index name, the way cakes are
  labelled in the lid of a real box. Navigation belongs to the
  theme when the map of the site *is* the box's contents list;
  the visitor learns the palette by learning the site.
- **Structure.** A sticky header, 64px, `--chalk` with a 1px
  `--raw-umber` rule beneath (the lid's edge). Nav items are
  text links; each carries a 10px cake chip (a 10×10px field of
  its pigment, 2px radius) before its name and its index number
  after it in the index voice ("PIGMENTS PR102 · PY43 · PBr7 ·
  PG23" reads as the catalogue's own table of contents). The
  current section's chip is shown *bound* (its bound variant)
  while the others stay dry.
- **Motion spec.** Trigger: scroll. The current-section chip
  binds (crossfade to bound variant, 300ms `--ease-gloss`) as
  its section crosses the reading line, driven by the shared
  loop's section tracking — the same tracking that drives §6.6,
  so lid and smear can never disagree about where the reader
  is. The header itself never shrinks, slides or hides: a lid
  does not creep.
- **States.** Rest: all chips dry except the current section's.
  Hover: a nav item's chip binds on hover (300ms) — a preview of
  §6.7's verb at navigation scale. Focus: chip binds and the
  standard outline shows. Active (the current page): chip bound
  plus the item's name in `--ink-earth` 700. Scrolled-past: the
  tracking follows position, chips binding and drying as
  sections pass.
- **Content merge.** The nav labels are the sections' real
  pigment names and indices — the lid is the colophon (§6.17)
  in miniature, generated from the same section list, so the
  three printings (lid, smear, colophon) agree by construction.
- **Failure fallback.** No JS: all chips print dry and the
  current page's item is marked with `aria-current` and weight
  alone. The header is plain, complete HTML from first paint.
- **Reduced-motion variant.** Chip bind/dry swaps are instant
  state changes; no crossfade.
- **Performance budget & mobile variant.** Chip swaps are
  background-colour changes on 10px elements; negligible.
  Mobile (<768px): the lid keeps the name and a "THE BOX" button
  opening the full label list as a chalk sheet (§11's sheet
  pattern) — the labels are never compressed into an anonymous
  hamburger glyph, because the labels are the content.
- **Choreography timeline (v2).** Section boundary crosses the
  reading line → outgoing chip dries (300ms) and incoming chip
  binds (300ms), overlapped by 100ms so exactly one chip is
  fully bound at any settled moment → §6.6's smear segment
  changes pigment on the same frame.
- **State matrix (v2).** *Rest:* current chip bound. *Hover:*
  hovered chip binds. *Focus:* focused chip binds + outline.
  *Active:* current item bound + 700 weight. *Scrolled-past:*
  tracking continuous. *Disabled:* a nav item for an empty
  section (no stock) prints at 55% with its chip dry — and is
  still a link (§6.18's honesty). *Touch:* tap navigates; no
  pre-bind.
- **Breakpoints (v2).** ≥1200px: full label row. 768–1199px:
  labels without index numbers (indices remain in the
  sections). <768px: name + "THE BOX" sheet.
- **Edge cases & failure modes (v2).** *More sections than
  pigments:* a section without its own pigment (an about page)
  takes a chalk chip with an umber rule — a paper label, named
  as such in the colophon ("PAPER — no pigment"); it never
  borrows a neighbour's colour. *Long names:* labels truncate
  at 18 characters with the full name in the section's own
  head; the index number never truncates.
- **Accessibility spec (v2).** Landmarks: `<header>` + `<nav
  aria-label="The box">`. Chip colours are redundant coding —
  every item is fully named in text. `aria-current="true"` on
  the active item. Focus outline 2px `--ink-earth`, offset 2px,
  on chalk at 9.5:1.
- **Tokens consumed (v2).** `--chalk`, `--raw-umber`,
  `--ink-earth`, all anchor + bound tokens (chips),
  `--ease-gloss`.

### 6.12 The pigment ticket — product cards

- **What & why.** Each product is a cake with a ticket: the
  cake face (the pigment's true colour, matte), and below it a
  printed ticket carrying the pigment's name, its Colour Index
  number, its grind state, its weight options and its price.
  The card belongs because a pigment is bought as a substance
  with a specification, and the ticket *is* that specification —
  the same slip that would be tied to the cake in the shop.
- **Structure.** An `<article>`: cake face (aspect 4:3, the
  pigment anchor, powder texture at the rim — a 6px granular
  edge via the §6.1 texture), then the ticket on `--chalk`:
  name (Alegreya 21px), index line (index voice: "PR102 ·
  NATURAL RED IRON OXIDE"), grind line (§6.8's state), source
  line ("Terra rossa, Tuscany — washed, levigated"), price per
  100g in tabular figures, and the order link. Cards sit in
  their section's slot in a row of three (≥1200px).
- **Motion spec.** Trigger: entry — cards seat with their slot
  (§6.3) and their images (where a card carries a photograph of
  the raw earth) uncover by the §5 knife wipe, 500ms
  `--ease-mix`, staggered 90ms card to card. Hover and click
  behaviours are §6.7 and §6.8, which are specified on this
  card. Tilt: on hover the card lifts like a cake taken from
  the tin — rotate to a maximum of 3° toward the pointer's side
  and translateY −4px, 300ms `--ease-settle`, returning flat on
  leave; the tilt is the §5 hover-physics budget, never more.
- **States.** Rest: matte, at session grind step. Hover: gloss
  (§6.7) + tilt ≤3°. Focus: gloss centred, outline on the
  ticket. Active: grind (§6.8). Scrolled-past: at rest.
  Disabled (out of stock): the cake face is shown with a paper
  band across it printed "OUT OF STOCK — NEXT GRINDING [month]"
  with the month from the catalogue object; no gloss, no grind,
  no tilt — a banded cake cannot be handled.
- **Content merge.** Every line on the ticket is catalogue data
  (§6.13's object): name, index, source, price, stock. The cake
  face is not a product photo substitute — it is the product,
  sampled. A card with invented provenance would violate §1's
  third corollary; the build generates tickets from the
  catalogue, so a pigment without a source line cannot produce
  a card at all.
- **Failure fallback.** No JS: the full card, matte, with the
  bound stripe (§6.7) and a fineness line in place of the grind
  interaction. Images ship uncovered (the wipe is JS-armed).
- **Reduced-motion variant.** No wipe, no tilt. Cards print
  complete; gloss becomes §6.7's instant bound swap.
- **Performance budget & mobile variant.** Texture is one shared
  SVG filter reused by all cards (not per-card copies). Mobile:
  cards stack full-width, tilt is cut (a stacked cake is not
  lifted), the knife wipe shortens to 350ms.
- **Choreography timeline (v2).** Slot seats (§6.3) → card
  images wipe at +100ms, 90ms stagger → ticket lines are static
  throughout (data never performs) → hover: gloss (§6.7) + tilt
  in over 300ms → click: grind (§6.8) → leave: tilt returns
  300ms, gloss dries per §6.7.
- **State matrix (v2).** *Rest:* matte, session grind step.
  *Hover:* gloss + ≤3° tilt. *Focus:* gloss centred, outline,
  no tilt (tilt is a pointer pleasure; focus stays level).
  *Active:* grind swirl. *Scrolled-past:* rest state.
  *Disabled:* banded, inert. *Touch:* tap binds (§6.7), second
  tap grinds (§6.8), links tap normally — the three are
  distinguished by target, never by timing tricks.
- **Breakpoints (v2).** ≥1200px: 3 per row, tilt on.
  768–1199px: 2 per row, tilt ≤2°. <768px: 1 per row, no tilt,
  cake aspect 16:9 so the ticket stays above the fold line of
  the card.
- **Edge cases & failure modes (v2).** *Long pigment names*
  ("Yellow ochre, pale, French"): the name wraps to two lines
  and the ticket grows; the cake face never shrinks to
  compensate — the substance outranks the slip. *Price changes
  in the catalogue:* tickets are generated, so a price exists
  in exactly one place (§6.13). *A pigment whose dry colour is
  near-chalk* (chalk itself, PW18, is sold too): its cake face
  carries the umber recess rule at full strength so the face
  reads as a surface, not a hole.
- **Accessibility spec (v2).** The card's order link is a real
  link with the pigment named ("Order red ochre PR102"); the
  cake face is decorative (`aria-hidden`) because the ticket
  names everything it shows. Ticket text: name in
  `--ink-earth` 9.5:1, index line in the pigment's deep mix at
  ≥5.2:1, price tabular. Touch targets: order link ≥44px.
- **Tokens consumed (v2).** The pigment's anchor, bound and deep
  tokens, `--chalk`, `--ink-earth`, `--ease-settle`,
  `--ease-mix`.


### 6.13 Grind figures — the catalogue counters

- **What & why.** Where the site states its working figures —
  grind times in minutes, mesh numbers, grams per cake, cakes
  in stock — the numbers count up once as their ticket enters:
  "GROUND 40 MIN · MESH 120 · CAKE 57 G". The counters belong
  because in this theme a number is a measurement of work done
  to a material; watching 40 arrive is watching the grinding
  take its time, compressed. They are also the theme's honesty
  test: every counted figure comes from the catalogue object,
  and §10 recounts them against it.
- **Structure.** A figures band inside the relevant section: a
  row of figure blocks, each a value (`<span class="fig">` with
  the true value in the DOM from first paint) over a label in
  the index voice. The catalogue object — one JSON block per
  page, generated from the merchant's records — is the single
  source the counters, tickets (§6.12) and ledger (§6.14) all
  read.
- **Motion spec.** Trigger: the band crossing 70% viewport
  height, once per page. Each value counts from 88% of itself
  to itself over `--dur-count` 1200ms, `--ease-mix`, in whole
  units only (a grind time never shows 39.4 minutes — the count
  moves in the unit the workshop measures in), staggered 120ms
  figure to figure. The count is a text rewrite of a number
  already in the DOM; the end value is byte-identical to the
  shipped value.
- **States.** Rest (shipped): true values printed. Counting:
  per timeline. Scrolled-past uncounted: true values (the count
  is skipped, never faked). Hover/focus: none — figures are not
  controls. Disabled: a figure the catalogue marks provisional
  prints with a "— PROVISIONAL" label and does not count; an
  unmeasured number does not perform certainty.
- **Content merge.** The figures are the section's working data
  — the process section's grind times, the catalogue's stock —
  not a stats banner bolted on for energy. A page with no
  measured figures has no counters; §9 names the invented-stats
  band a failure.
- **Failure fallback.** No JS: true values, printed. Watchdog:
  if the count is interrupted (tab hidden), values snap to true
  on return — the shipped number is the floor the animation can
  never leave wrong.
- **Reduced-motion variant.** True values, printed. No count.
- **Performance budget & mobile variant.** Text rewrites on ≤6
  figures, once; negligible. Mobile: the band wraps to two
  columns and the count shortens to 800ms.
- **Choreography timeline (v2).** Band crosses 70% → figure 1
  counts 0–1200ms → figures 2–4 stagger +120ms each → all rest
  at true values by t=1600ms → the band never counts again this
  page.
- **State matrix (v2).** *Rest:* true values. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* true values.
  *Disabled:* provisional figures labelled, uncounted.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: one row, up to 5 figures.
  768–1199px: one row, up to 4 (the fifth wraps). <768px: two
  columns, 800ms counts.
- **Edge cases & failure modes (v2).** *A figure of 0* (a
  pigment out of stock): counts from 0 to 0 — i.e. prints, with
  its "OUT OF STOCK" label (§6.12); a zero never performs a
  count. *Very large figures* (grams in stock, 12,400): the
  count runs in whole hundreds below the final 88%→100% range
  so it still lands in 1200ms. *Catalogue updated:* all figures
  regenerate from the one object.
- **Accessibility spec (v2).** Counting spans are `aria-hidden`;
  a visually hidden static copy of each true value serves AT,
  so a screen reader never hears a number mid-count. Values are
  tabular (§3 law 1) so the count never shifts layout.
- **Tokens consumed (v2).** `--ink-earth`, the section pigment's
  deep token (labels), `--ease-mix`, `--dur-count` (1200ms).

### 6.14 The mixing ledger — recipes table

- **What & why.** A real table of the site's mixes: each row a
  boundary on the page — pigment A, pigment B, the ratio at the
  line, the resulting earth's name and its use ("the colour of
  the process section's ground at its middle"). The ledger
  belongs because §1's law makes every mix a claim, and claims
  are kept in a ledger: this table is where the page's colour
  arithmetic can be audited, row by row, against the boundaries
  the reader has already scrolled through.
- **Structure.** A `<table>` on a chalk sheet inside the umber
  slot: columns MIX (two cake chips + index names), RATIO (at
  the line), THE EARTH (the mixed colour's field chip at its
  midpoint), USED FOR. Rows are generated from the same boundary
  list that builds §6.4's bands and §6.6's smear — one list,
  three printings. The mixed chip in each row is the live
  `color-mix()` at that row's ratio, so the table shows the
  actual colour, not a swatch approximation.
- **Motion spec.** Trigger: entry. Rows seat with the slot
  (§6.3); then each row's mixed chip *mixes* — its two
  ingredient chips slide 12px toward it from either side over
  500ms `--ease-mix`, staggered 110ms per row, as if the knife
  had just passed. The table's text never moves. A row whose
  boundary the reader has already crossed (§6.4 state) arrives
  pre-mixed — the ledger records what the reader has done.
- **States.** Rest: all rows printed, chips mixed. Hover: a row
  lifts its chip trio 2px and the row's boundary is located —
  a "SEE IT ↑" link scrolls to that boundary on the page.
  Focus: same, with outline. Scrolled-past: printed.
  Disabled: a mix whose ratio is provisional (a new pairing
  being tested) prints its ratio with "— ON TRIAL" and its chip
  at the trial ratio; trials are labelled, never hidden.
- **Content merge.** The ledger is not a colour-theory essay; it
  is the index of this page's actual boundaries, and its rows
  link to them. Delete a boundary from the page and its row
  disappears from the ledger, because both are generated from
  one list.
- **Failure fallback.** No JS: the table prints complete, chips
  at their static midpoints (the `color-mix()` fallback hexes
  of §6.4). The table is fully usable — it is a table.
- **Reduced-motion variant.** Chips print mixed; no slide-in.
  The "SEE IT" links still work.
- **Performance budget & mobile variant.** ≤8 rows per page by
  construction (a page has ≤7 boundaries). Mobile: the table
  becomes stacked rows — MIX over RATIO over THE EARTH — with
  no horizontal scroll; a colour ledger that needs sideways
  scrolling has failed its readers.
- **Choreography timeline (v2).** Slot seats → rows' chips mix
  at +150ms, 110ms stagger, 500ms each → all mixed by ~1400ms
  → rows whose boundaries were already crossed skip the slide
  (they arrive mixed, per state) → table at rest.
- **State matrix (v2).** *Rest:* printed, mixed. *Hover:* chip
  trio lifts 2px. *Focus:* same + outline on the row's link.
  *Active:* "SEE IT" scrolls (native anchor, smooth under the
  loop's lerp unless reduced motion). *Scrolled-past:* printed.
  *Disabled:* trial rows labelled. *Touch:* tap = hover's lift,
  held until another tap.
- **Breakpoints (v2).** ≥1200px: four columns. 768–1199px: four
  columns, USED FOR wraps. <768px: stacked rows.
- **Edge cases & failure modes (v2).** *A boundary between a
  pigment and a chalk sheet:* the mix is pigment : PW18, a real
  lightening, and the ledger lists it like any other row — chalk
  is a pigment (§2), so tinting is mixing and is recorded.
  *Duplicate pairs at different ratios* (the same neighbours
  meeting twice on a long page): two rows, distinguished by
  their USED FOR lines; the ratio belongs to the boundary, not
  the pair.
- **Accessibility spec (v2).** A true `<table>` with `<th>`
  scope; chips are `aria-hidden`, every fact (names, indices,
  ratio, use) is text. Ratio figures tabular. Row hover lift is
  never the only signal — the "SEE IT" link is text.
- **Tokens consumed (v2).** `--chalk`, `--ink-earth`, the anchor
  tokens (chips), `--ease-mix`.

### 6.15 The order slab — conversion form

- **What & why.** Ordering happens on the slab: a form laid out
  like a grinding slab's working surface — pigment, fineness,
  weight, then the buyer's direction — where each choice is made
  by stamping a cake, and the fineness choices arrive pre-set by
  the grinding the visitor already did (§6.8). It belongs
  because conversion in this theme is a workshop order, written
  on the tool the work is done with; a generic checkout skin
  over earth pigment would break the fiction at the exact moment
  money appears.
- **Structure.** A `<form>` on a `--chalk` sheet inside the
  final slot: (1) pigment — a row of cake radio chips (§11),
  one per pigment in stock; (2) fineness — three radio lines
  (COARSE / FINE / EXTRA FINE) with the visitor's §6.8 grind
  step pre-selected for the chosen pigment; (3) weight — 100g /
  250g / 1kg radio lines with prices computed live from the
  catalogue's per-100g figure (tabular, printed, never
  animated); (4) name and direction fields as ruled lines (§11);
  (5) the submit — a wide cake of the chosen pigment printed
  "GRIND AND SEND MY ORDER". Success replaces the form with a
  stamped ticket: the order restated, a hanko-style stamp in the
  pigment's deep mix reading "GROUND TO ORDER", and the
  despatch line in the merchant's voice (§12).
- **Motion spec.** Trigger: interaction. Cake radios stamp on
  selection: 180ms `--ease-stamp`, a 1px press and the chip's
  colour deepening to its bound variant. Price recomputation is
  instant text (money never animates). Submit: the button cake
  presses (scaleY 0.97, 120ms), the form's sheet performs one
  palette-knife wipe (§5) at 450ms as the ticket replaces it —
  the order is wiped clean and the ticket laid down. Errors:
  the offending field's rule draws in `--red-ochre-deep` over
  260ms and the error note prints in the grinder's voice
  (§12) — nothing shakes; pigment workers do not shake paper.
- **States.** Rest: complete, submittable, with fineness
  pre-selected from §6.8 where it exists. Focus: field rules
  ink to full `--ink-earth` (260ms draw). Active: as above.
  Disabled: a pigment out of stock shows its cake banded
  (§6.12) and unselectable, its next-grinding month printed.
  Submitted: the stamped ticket, permanent for the session.
  Scrolled-past: the form waits, state kept.
- **Content merge.** The form's entire contents — pigments,
  finenesses, weights, prices, stock — are the catalogue
  object (§6.13) rendered as controls; and its fineness state
  is the visitor's own grinding (§6.8) carried forward. Nothing
  in the form exists that is not either catalogue data or the
  visitor's own work.
- **Failure fallback.** No JS: a plain, fully working form —
  native radios, no pre-selection (all finenesses offered
  equally), prices printed per weight in a small table beside
  the weight lines (the live computation is an enhancement;
  the figures are content and ship). Submission is a normal
  POST; the stamped ticket is the server's confirmation page in
  the same dress.
- **Reduced-motion variant.** No wipe, no stamp press. Selection
  deepens instantly; the ticket replaces the form instantly.
- **Performance budget & mobile variant.** The form is DOM and
  text; the wipe reuses §5's transition layer. Mobile: the slab
  stacks — pigment cakes two per row, fineness and weight lines
  full-width at 48px targets, the submit cake full-width.
- **Choreography timeline (v2).** Pigment cake tapped → stamp
  180ms, fineness re-pre-selects to that pigment's grind step
  (instant) → weight tapped → prices recompute instantly →
  submit → press 120ms → wipe 450ms → ticket laid, stamp lands
  at +500ms (`--ease-stamp`, 180ms) → despatch line prints.
- **State matrix (v2).** *Rest:* ready, pre-selections honest.
  *Hover:* cake chips bind (§6.7's verb at chip scale).
  *Focus:* rules ink, outlines standard. *Active:* press +
  wipe. *Scrolled-past:* state kept. *Disabled:* banded cakes
  unselectable, reason printed. *Touch:* all targets ≥48px;
  stamp on tap.
- **Breakpoints (v2).** ≥1200px: slab two-column (choices left,
  direction right). 768–1199px: one column, cakes three per
  row. <768px: one column, cakes two per row, 48px targets.
- **Edge cases & failure modes (v2).** *Visitor ground a pigment
  then orders a different one:* fineness pre-selects only for
  the ground pigment; others default to FINE, printed as the
  default — pre-selection never invents a preference.
  *Validation failure:* input is kept (error-keeping), focus
  moves to the first error, the error names the field in the
  grinder's voice ("The direction will not carry — the second
  line is empty."). *Double submit:* the button disables after
  the press until the ticket lands.
- **Accessibility spec (v2).** Native radios and inputs with
  real `<label>`s; the cake chip is inside the label, never a
  replacement for it. Errors use `aria-describedby` and print
  beside their fields in `--red-ochre-deep` (5.7:1). The ticket
  region is `role="status"`. Prices are text, announced on
  change via the weight radio's label.
- **Tokens consumed (v2).** `--chalk`, `--ink-earth`,
  `--red-ochre-deep`, all anchor + bound tokens (cakes),
  `--ease-stamp`, `--ease-mix`.


### 6.16 Powder skeleton & the palette-knife transition

- **What & why.** Loading in this theme is dry: a page still
  arriving shows powder skeleton fields — matte, granular fields
  in the slot's pigment at 30% — and moving between pages, a
  palette knife smears the next page's first pigment across the
  screen, the content swaps beneath, and the smear lifts. Both
  belong because in a workshop, material is either dry and
  waiting or being spread; there is no third, spinner-shaped
  state of matter.
- **Structure.** Skeleton: each slot renders its field at 30%
  pigment over `--chalk-dim` with the §6.1 granular texture and
  grey-free "powder bars" (the slot pigment at 45%) where lines
  of text will land — the skeleton is the slot's own anatomy in
  its own pigment, never grey. Transition: a fixed layer
  carrying a knife-smear field (the destination pigment with a
  knife-edge leading rim and a dry trailing edge) that
  translates across at 450ms; the swap happens at full cover
  (~t=220ms).
- **Motion spec.** Trigger: navigation (internal links) for the
  smear; resource pending >150ms for the skeleton. Smear: in
  450ms `--ease-mix`, swap at cover, out 380ms (the knife
  lifting leaves the new page's hero already seated — its slot
  does not re-settle after a smear arrival). Skeleton fields
  resolve slot by slot as content lands, each resolving with
  its §6.3 settle. Skeleton watchdog: any field unresolved at
  6000ms prints the merchant's line "The tin is still being
  packed." with a retry link — a skeleton never spins forever
  in silence.
- **States.** Rest: no layer. Transitioning: smear in → cover →
  out. Loading: powder fields where content is pending, real
  content where it has landed (mixed states are normal and
  honest). Disabled: external links, modified clicks and
  form-posts never smear.
- **Content merge.** The smear's colour is the destination
  page's first pigment — the transition previews the next slot
  in the box — and the skeleton's fields are the page's own
  slots in their own pigments. Neither layer introduces a
  colour the law cannot name.
- **Failure fallback.** No JS: no smear, no skeleton — ordinary
  navigation and ordinary loading, fully functional. If the
  destination fails to load, the smear lifts back (reverse
  380ms) and the reader is where they were, with the failure
  stated in the footer line.
- **Reduced-motion variant.** No smear: instant navigation. No
  animated skeleton shimmer (there is none in any variant —
  powder does not shimmer); skeleton fields are static until
  they resolve.
- **Performance budget & mobile variant.** One fixed layer, one
  transform; skeleton textures reuse the shared filter.
  Mobile: the smear runs at 380ms and covers diagonally (the
  knife angle steepens on a narrow slab).
- **Choreography timeline (v2).** Click → smear enters from the
  reading side, 0–450ms → cover at ~220ms, content swaps →
  450–830ms smear lifts off the far side → destination hero
  stands seated → focus moves to the destination's `<h1>`.
- **State matrix (v2).** *Rest:* absent. *Hover:* none.
  *Focus:* focus is held on the activating link until the swap,
  then moved to the destination heading — never dropped to
  `<body>`. *Active:* as timeline. *Scrolled-past:* n/a.
  *Disabled:* modified/external clicks bypass. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: horizontal smear, 450ms.
  768–1199px: 420ms. <768px: diagonal smear, 380ms.
- **Edge cases & failure modes (v2).** *Rapid double
  navigation:* the second click during a smear is queued; the
  knife finishes its pass before accepting it — two smears
  never overlap into mud. *Back button:* the smear runs in
  reverse direction (from the far side), because the knife is
  coming back across the slab. *Slow destination:* if cover
  lasts >1200ms, the smear's surface prints the destination's
  pigment name and index in the index voice — the wait is
  labelled with the material being fetched.
- **Accessibility spec (v2).** The transition layer is
  `aria-hidden`; route changes are announced by the destination
  heading receiving focus. Skeleton regions use `aria-busy`
  with the merchant's line as the labelled fallback. No content
  is ever reachable *only* after a transition.
- **Tokens consumed (v2).** The destination's first pigment
  token, `--chalk-dim`, `--ink-earth`, `--ease-mix`.

### 6.17 The colophon of colours — footer

- **What & why.** The footer is the theme's signature act: a
  colophon that footnotes *every colour used anywhere on the
  site* with its pigment index name, its ratio where it is a
  mix, and the slot it came from — closing with the finished
  five-stripe palette (§6.6's smear, arrived). It belongs
  because the law (§1) is only real if it is auditable, and the
  colophon is the audit, published on every page: the site
  shows its bill of materials the way a paint box lists its
  cakes on the lid.
- **Structure.** A footer on `--green-earth` (the box's last
  cake) in chalk text: three columns — THE BOX (the five anchors
  with indices and sources), THE MIXES (every boundary recipe on
  this page, generated from §6.14's list), THE MAKING (grind
  figures, the batch line, the merchant's plain legal line) —
  and across the foot, the palette stripe: five segments in tin
  order at the proportions §2 declares. Every entry is text; the
  stripe is the only purely visual element.
- **Motion spec.** Trigger: entry. The stripe's segments draw
  in tin order, each a 300ms `--ease-mix` wipe, staggered 90ms —
  the knife laying the test stripe one last time. The columns
  themselves are static text from first paint. The stripe draws
  once; re-entry shows it drawn.
- **States.** Rest: complete colophon, stripe drawn. Hover: a
  mix entry highlights its boundary's "SEE IT" link (§6.14's
  behaviour, shared). Focus: standard outlines on chalk-green
  (chalk on `--green-earth`, 7.5:1). Scrolled-past: drawn.
  Disabled: none.
- **Content merge.** The colophon's lists are generated from
  the same objects as the lid (§6.11), the smear (§6.6) and the
  ledger (§6.14) — a colour that appears on the page but not in
  the colophon is a build error §10 catches by diffing the two,
  not a discrepancy a reader should ever find first.
- **Failure fallback.** No JS: the colophon prints complete,
  stripe drawn. It is a footer; it has no other job than to be
  there, true.
- **Reduced-motion variant.** Stripe printed drawn; columns
  unchanged.
- **Performance budget & mobile variant.** One small wipe
  animation on five segments. Mobile: columns stack — THE BOX,
  THE MIXES, THE MAKING — and the stripe stays full-width at
  the foot; the audit is never truncated to fit a phone.
- **Choreography timeline (v2).** Footer enters → stripe
  segments wipe in tin order, 90ms stagger, by t=750ms →
  colophon at rest → the smear rail (§6.6) aligns its final
  segment on the same frame as the stripe's last segment lands.
- **State matrix (v2).** *Rest:* complete. *Hover:* mix entries
  highlight. *Focus:* outlines visible. *Active:* links behave
  as links. *Scrolled-past:* drawn. *Disabled / no-JS:*
  complete and drawn. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns (MIXES wraps under BOX). <768px: stacked, stripe
  full-width.
- **Edge cases & failure modes (v2).** *A page using a trial
  mix (§6.14):* the colophon lists it with its "ON TRIAL" mark
  — the audit includes experiments. *A colour used only by an
  error state* (`--red-ochre-deep` on a form): it is already a
  declared token, listed under THE BOX as PR102's deep mix —
  the audit's rule is *every token*, not *every cheerful
  token*.
- **Accessibility spec (v2).** `<footer>` landmark; the three
  columns are headed lists of real text. Chalk on green earth
  7.5:1; the stripe is `aria-hidden` with its contents fully
  duplicated by THE BOX list. Legal line in chalk at 13px
  minimum.
- **Tokens consumed (v2).** `--green-earth`, `--chalk`, all
  anchor tokens (stripe), `--ease-mix`.

### 6.18 The empty slot — 404

- **What & why.** The 404 is an empty slot in the tin: a
  recessed, chalk-dim slot outline where a cake should be, its
  label printed with the pigment the visitor asked for — "NO
  CAKE IN THIS SLOT" — and the box's real contents offered as
  the way back. It belongs because a missing page in this world
  is not an error in the abstract; it is a place in the box
  where the material the visitor wanted is not stocked, and the
  honest response is to show the empty place and the full ones.
- **Structure.** A single slot, recessed (§4's recess line at
  double strength), containing: the plain fact first ("This
  page is not in the box."), the requested path printed in the
  index voice, the empty cake outline (a 2px `--raw-umber` rule
  rectangle at cake proportions, unfilled), and three real
  links — the box's most-stocked pigments — each with its cake
  chip. Below, the colophon (§6.17) prints as on every page,
  listing what the box *does* hold.
- **Motion spec.** Trigger: arrival. The empty slot performs
  exactly one gesture: its recess line draws in over 600ms
  `--ease-mix` when the page loads — the box being opened to
  show the gap. Nothing else moves. The choreography is
  specified as near-stillness on purpose: an empty slot does
  not perform.
- **States.** Rest: the empty slot, drawn. Hover/focus: the
  three links behave as §6.11's nav items. Scrolled-past: n/a
  (the page is one slot tall). Disabled: none.
- **Content merge.** The empty slot is the same furniture as
  every stocked slot (§6.3) with the cake absent — the page's
  own layout states the fact. The offered links are generated
  from the catalogue's stock figures (§6.13), so the "way back"
  always points at pigments actually in stock.
- **Failure fallback.** No JS: the slot prints with its recess
  line drawn. The page is static HTML with working links; its
  fallback is itself.
- **Reduced-motion variant.** Recess line printed drawn; no
  other change.
- **Performance budget & mobile variant.** The lightest page on
  the site by design. Mobile: the slot stacks, links full-width
  at 48px.
- **Choreography timeline (v2).** t=0 load → recess line draws
  0–600ms → the requested path prints (it was always in the
  DOM) → stillness. Total motion on the page: 600ms, once.
- **State matrix (v2).** *Rest:* empty, drawn. *Hover:* links
  bind their chips (§6.11). *Focus:* outlines standard.
  *Active:* links navigate (via §6.16's smear, in the missing
  pigment's nearest stocked neighbour's colour — the knife
  brings what the box has). *Scrolled-past:* n/a. *Disabled /
  no-JS:* complete. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: slot in the standard measure.
  768–1199px: same, narrower. <768px: stacked links, cake
  outline at 16:9.
- **Edge cases & failure modes (v2).** *A path that names a real
  pigment with no page* (a visitor guessing `/py43`): the label
  prints the pigment's true name and index — the box knows the
  material even where it has no page for it — and the links
  offer its section anchor on the catalogue page. *A nonsense
  path:* the label prints the path as given; the box does not
  pretend to recognise it.
- **Accessibility spec (v2).** The plain fact is the `<h1>`.
  The empty outline is `aria-hidden` (the fact is in the text).
  Links are fully named ("Yellow ochre, PY43 — in stock").
  Contrast: `--ink-earth` on the slot's chalk-dim ground is
  8.1:1.
- **Tokens consumed (v2).** `--chalk-dim`, `--raw-umber`,
  `--ink-earth`, `--chalk`, `--ease-mix`.


## 7. Page application map

- **Home.** The full performance: grinding hero (§6.1),
  dry-to-bound name (§6.2), cakes in tin order (§6.3), boundary
  mixes (§6.4), the pinned mix (§6.5), figures (§6.13), the
  colophon (§6.17). The home page is the box, opened on the
  bench.
- **Catalogue / listing.** Cakes by pigment family; each family
  is a slot, its products §6.12 tickets in rows. Boundary mixes
  occur between families actually adjacent on the page.
  Filters are slot-jumps (anchor links), never a faceted panel —
  a tin is browsed by looking along it.
- **Product detail.** One pigment, whole page: its cake as hero
  (no grind — the grind belongs to the home page's name; here
  the cake is shown ground already, with its three fineness
  states as §6.8's steps made static and selectable), its raw
  earth photograph knife-wiped in, its ledger rows (§6.14) for
  every mix it enters, its order slab (§6.15) at the foot.
- **Process / about.** The pinned mix (§6.5) and the diagram
  (§6.9) carry the page; the merchant's story is set on chalk
  sheets between pigment slots, and every process claim carries
  its figure (§6.13).
- **Contact / trade account.** The order slab's sibling: a
  direction form on the slab pattern (§6.15's furniture, no
  cakes to buy), success stamped "FILED IN THE DAY BOOK".
- **404.** The empty slot (§6.18).
- **Print.** The catalogue prints as tickets on chalk; mixes
  print at their midpoint hexes; the colophon prints entire —
  a printed page from this site is a pigment chart, and is
  designed to be kept as one.

## 8. Worked examples

The merchant throughout is **Wren & Daughter, Pigment
Merchants** — a two-person firm grinding earth pigments in a
converted washhouse, selling by weight to painters and fresco
plasterers. Catalogue figures below are the firm's printed
records for the worked examples.

### 8.1 The hero, end to end — the merchant's home page

The page opens on chalk. At the slab, a pile of PR102 powder
(§6.1) waits under the muller; the firm's name stands above it
in Alegreya 700, dry (§6.2's shipped state), and the standfirst
reads: "Earth pigments, ground in the washhouse. Batch 14 on
the slab." On load (fonts ready, t=0) the muller drops and
circles — three revolutions, 1400ms, radius closing 64→18px —
the pile blurring to paste, the smear layer rising beneath the
headline until, at t=1400, the name stands on paint the page
made. At t=1450 the letters, already stamped dry during the
grind's last beat, take the gloss sweep and bind. The visitor
has watched the firm's whole argument — *we grind, we bind,
this is the colour* — in 2.1 seconds, before scrolling. Scroll
timeline: 0–15% of page, hero only; the dust (§6.10) starts as
the grind ends; the first boundary (red ochre into the intro
sheet's chalk — a PR102 : PW18 tint, ledgered) begins mixing as
it crosses the reading line. A returning visitor sees none of
it replayed: the hero stands ground and bound, and the batch
line has moved on to batch 15.

### 8.2 Mid-page — the pinned mix on the process page

Halfway down the process page, the recipe section pins
(§6.5). Left, the material: a lump of Tuscan terra rossa.
Right, the recipe in the grinder's register: "Wash the earth
three times. Grind forty minutes on the slab. Mull in gum
arabic, a little at a time. Rest the paint overnight; it is
better for the rest." Scrolling the 150vh pin, the lump powders
(p=0.15–0.3), the powder pastes under the tightening muller
(p=0.4–0.5), and at p=0.9 the finished stroke wipes in — the
same stroke printed on PR102's ticket in the catalogue, so the
reader who orders later recognises the product by its stroke.
The figures band (§6.13) sits immediately after the pin: GROUND
40 MIN · MESH 120 · REST 12 H — each figure the recipe just
stated, counted once as the band enters. Scroll timeline: pin
at 45–60% of page; the boundary out of the process slot mixes
PR102 into PBr7 (the umber of the ledger section) at a printed
2 : 1, because the ledger's ground is redder than the tin's
order would suggest — adjacency on the page, recipe on the
band, row in the ledger, three printings in agreement. On the
reverse pass the pin un-makes its stroke back through paste and
powder to the lump (§13) — a visitor scrolling up to re-read
the washing step watches the paint honestly un-become, which
the firm prefers to a latch: a recipe you cannot run backwards
in your head is a recipe you have not understood, and the
scrub's reversibility is the page's way of letting the reader
rehearse it.

### 8.3 Conversion — ordering a cake of yellow ochre

From the catalogue, the visitor has ground the yellow-ochre
card twice (§6.8): its ticket reads "GROUND FINE", its face
sits 50% toward bound. Its order link lands on the order slab
(§6.15) with the pigment cake already stamped PY43 and fineness
pre-selected at FINE — the visitor's own work, carried. They
choose 250g; the price line recomputes instantly from the
catalogue's £6.40 per 100g to £16.00, printed, tabular, still.
They write their direction; the second line is left empty and
the error prints in the grinder's voice — "The direction will
not carry — the second line is empty." — with the input kept.
Corrected, the submit cake presses, the knife wipes, and the
ticket lands stamped "GROUND TO ORDER": *Yellow ochre PY43,
ground fine, 250 g — to be ground Thursday and posted Friday.*
The confirmation names the fineness the visitor chose with
their own clicks twenty minutes of browsing earlier; the order
is the browsing, concluded. Scroll timeline: the slab sits at
the catalogue page's foot (85–100%); no scroll ceremony attends
it — conversion furniture is kept calm on purpose, the theatre
having been spent where it teaches.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The generic "earthy palette".** Beige gradients and
   terracotta clip-art that name nothing. *Cure:* the law —
   every colour resolves to a pigment token or a printed mix;
   if it cannot be footnoted in the colophon, it cannot be on
   the page.
2. **Gloss everywhere.** Cards shiny by default, buttons with
   candy highlights. *Cure:* dry is the shipped state; gloss
   exists only as §6.7's earned bind or §6.2's one ceremony.
   Unbound gloss is varnish, and varnish is a lie about the
   material.
3. **Mixing non-neighbours.** A purple gradient between red and
   green sections because it "looks nice". *Cure:* mixes only
   between adjacent slots, from their own tokens, ratio
   printed. Purple is not in the box.
4. **Unnamed colours.** A `#000` shadow, a default-blue link, a
   grey skeleton. *Cure:* shadows are umber offsets, links are
   deep mixes, skeletons are the slot's own pigment (§6.16);
   the gate greps for raw hex outside the token block.
5. **Fake index names.** "PY43" attached to a red, or invented
   codes (PR999). *Cure:* indices are checked against the real
   Colour Index assignments for the five anchors (PR102, PY43,
   PBr7, PG23, PW18); a wrong index is a factual error, treated
   like a wrong price.
6. **Dust over everything.** Ambient particles drifting across
   catalogue text. *Cure:* dust lives in the hero's slab field
   only, 24 motes, with a text exclusion zone (§6.10).
7. **The grind replaying.** Hero ceremonies on every visit,
   every scroll-back. *Cure:* once per session, latched; a
   batch is ground once, and the page does not pretend
   otherwise.
8. **Invented figures.** "Over 10,000 happy painters!" *Cure:*
   counters count only catalogue figures (§6.13); a number with
   no record behind it is refused at the gate.
9. **Cakes as rounded cards.** Big radii, drop shadows, floating
   tiles — stock e-commerce furniture. *Cure:* 2px radius,
   recess lines, matte offsets; cakes sit *in* slots (§4).
10. **Tilt for its own sake.** Cards leaning 10° under the
    pointer. *Cure:* the lift is ≤3°, the motion of a cake taken
    from a tin, and it is cut entirely on stacked mobile cards.
11. **A marquee stripe.** The palette scrolling sideways like a
    banner ad. *Cure:* refused in §5; the stripe is earned at
    the footer or printed static, never run.
12. **The boundary as decoration.** A gradient band whose
    colours match neither neighbour. *Cure:* the band is
    computed from the neighbours' tokens (§6.4) and its recipe
    is printed on it; a band that cannot state its recipe is
    removed.

## 10. Quality gate

Blocking — the theme may not ship with any item failing:

1. **Pigment-law audit.** Every colour value in the built CSS
   resolves to a §2 token or a `color-mix()` of two adjacent
   tokens; a grep for raw hex outside the token block returns
   only the declared midpoint fallbacks (§6.4).
2. **Colophon completeness.** The colophon (§6.17) lists every
   token the build uses, with index name and, for mixes, ratio;
   an automated diff of token block vs colophon is empty.
3. **Index truth.** The five anchors carry their real Colour
   Index names (PR102, PY43, PBr7, PG23, PW18) everywhere they
   appear — lid, tickets, ledger, colophon agree.
4. **Contrast, dry and bound.** Every text pairing passes AA in
   *both* material states: dry anchors per §2's table; bound
   variants re-measured (red ochre bound 4.9:1 is the licensed
   proof); yellow ochre carries no text on chalk in any state.
5. **Three printings agree.** Lid chips (§6.11), smear segments
   (§6.6) and colophon lists (§6.17) are generated from one
   section list; a page edited to reorder sections shows all
   three re-ordered, with boundary recipes recomputed.
6. **Watchdog pass.** With JS throttled to a stalled loop, every
   armed element reaches its finished state by its watchdog
   (hero 1800ms, headline 1600ms, slots 1200ms, diagram 2000ms);
   with JS disabled entirely, the page is complete and readable
   top to bottom.
7. **Grind-once audit.** Hero grind, headline bind, counters
   and diagram each fire once per session and latch; a
   scroll-up never replays any of them.
8. **Figure audit.** Every counted or printed figure traces to
   the catalogue object; the gate recounts three at random
   against the merchant's records.
9. **Dust ration.** Exactly one ambient loop exists (hero dust,
   ≤24 motes, slab field only, text exclusion verified by
   overlay screenshot).
10. **Mix-ratio audit.** Three boundaries are sampled: the
    ratio at the reading line reads 1 : 1 (±3%), and the
    printed recipe matches the computed mix at 25/50/75.


## 11. Component inventory

Every component a real merchant site in this theme needs, with
its treatment. Anything not listed does not appear.

- **Buttons.** Cakes, not pills: a rectangle of the action's
  pigment (2px radius, matte), chalk or ink text per §2's
  licensing, pressing 1px with `--ease-stamp` on active. The
  primary action on a page is the only bound (glossed) button,
  and only after its section has been read — gloss is earned
  (§9.2).
- **Links.** Set in the relevant deep mix (`--red-ochre-deep`
  5.7:1, `--yellow-ochre-deep` 5.2:1), underlined with a 1px
  rule in the same pigment at 40%; on hover the rule binds —
  thickens to 2px and deepens to the full mix.
- **Inputs.** Ruled lines on chalk: a 1px `--raw-umber` rule
  beneath the field that inks to 2px `--ink-earth` on focus
  (260ms draw); labels above in the index voice; no boxes, no
  fills — you write on the slab's paper.
- **Radio choices.** Cake chips: small fields of the option's
  own colour (for pigments) or chalk chips with pigment rules
  (for fineness/weight), stamping on selection (§6.15).
- **Checkboxes.** A small empty cake outline that fills with
  its pigment when checked — the fill is the state, with the
  label always in text beside it.
- **Tables.** The ledger pattern (§6.14): chalk sheet, umber
  rules, tabular figures, chips for colours. The only table
  pattern; dense data tables are refused (§1).
- **Badges / tickets.** The pigment ticket (§6.12) is the only
  badge form: name + index + one fact. A badge that says "NEW"
  is refused — the ticket says "BATCH 14" instead, which is
  information.
- **Alerts.** A slip: a chalk strip ruled in the alerting
  pigment's deep mix, the message in the grinder's voice (§12),
  printed at the head of the slot it concerns. No floating
  notifications.
- **Pagination.** The tin continues: "THE NEXT ROW OF THE BOX →"
  as a full-width slot link. Numbered page lists are refused —
  a box is not numbered, it is opened further.
- **Accordion / FAQ.** Drawers in the tin: chalk sheets that
  seat downward with §6.3's settle, one open at a time, the
  question set in Alegreya 500.
- **Tabs — refused.** Replaced by slot-jumps: a row of cake
  labels (§6.11's chips) anchoring to sections on the same
  page. Content hidden behind a tab is a cake hidden in a
  closed box; this site keeps its box open.
- **Modal — refused.** Replaced by *the lid sheet*: a full
  chalk sheet that seats over the page with §6.3's settle for
  the one job modals do here (the box list on mobile, §6.11) —
  it is a page state, with a URL, never an overlay trap.
- **Toast — refused.** Replaced by the ticket note: confirmations
  print onto the relevant ticket or the order's stamped ticket
  (§6.15), where the reader already is.
- **Tooltip.** The ticket tooltip: a small chalk slip with the
  pigment's name, index and grind time (§6.6's hover), appearing
  after a 600ms dwell, dismissed on leave; never the only
  carrier of anything.
- **Progress bar — refused.** Progress is the smear (§6.6) or
  it is not shown.
- **Spinner — refused.** Loading is powder (§6.16).
- **Select dropdown — refused.** Every choice set on this site
  is short enough to show as cakes or lines (§6.15); a choice
  set that is not (a country list) uses a ruled input with a
  datalist, styled as paper.
- **Search.** A ruled input in the lid sheet; results are
  tickets (§6.12) in a slot, with the empty result printed in
  the empty slot's voice (§6.18): "No cake in the box under
  that name."
- **Breadcrumbs.** The box path: "THE BOX / PIGMENTS / PR102" in
  the index voice, each level a link — the breadcrumb is a
  shelf label.
- **Cards.** §6.12 only. There is no generic card.
- **Dividers.** The boundary band (§6.4) between slots; inside a
  slot, a 1px rule in the slot pigment at 30% — a knife score,
  never a grey line.
- **Images.** Cake-framed (§5's knife wipe, powder rim), always
  captioned with what the photograph shows in workshop terms
  ("The raw earth, before washing") — a caption that names the
  process stage, not the mood.
- **Footer.** §6.17 only.
- **404.** §6.18 only.
- **Forms.** §6.15's slab pattern; errors in §12's voice,
  input always kept.

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the pigments.

**The Grinder** — the workshop voice, for headlines, process
copy, errors and confirmations. Short sentences. Verbs of work:
*grind, wash, mull, bind, cake, rest*. Figures stated plainly
and always with their unit. The Grinder never sells; the
Grinder reports. Headline style: a statement of material fact,
≤9 words — ✓ "Red ochre, ground forty minutes." ✗ "Discover
the Vibrant Magic of Earthy Reds!" (exclamation, vagueness,
and a colour claim no pigment made). Error voice: the fact,
then the want — ✓ "The direction will not carry — the second
line is empty." ✗ "Oops! Please complete all required fields."
Empty-state voice: ✓ "No cake in the box under that name."
✗ "Nothing found. Try again?"

**The Ticket** — the label voice, for indices, ratios, prices,
stock and specifications. Index voice (§3): uppercase Alegreya
Sans, tracked, figures tabular. A ticket line is a fact with
its unit and nothing else — ✓ "PR102 · GROUND FINE · 250 G ·
£16.00" ✗ "Our premium red — a customer favourite!" Ratios
always `3 : 1` with spaces; weights always with the unit;
prices always per stated weight, never a bare number.

**Banned words.** *Vibrant, pop, earthy tones, rustic* (as
praise), *premium, magic, discover* (as a verb of command),
*artisanal* (the firm grinds; it does not artisane), any hex
code in reader-facing copy (colours are named, not numbered —
the numbers live on tickets as indices), and the exclamation
mark outside a quoted customer's letter.

**Owned words and fixed strings.** *Ground finer* (§6.8's
note). *Out of stock — next grinding [month]* (§6.12's band).
*Ground to order* (§6.15's stamp). *The tin is still being
packed.* (§6.16's slow-load line). *No cake in this slot.*
(§6.18). *Batch [n] on the slab.* (§8.1's standfirst pattern).
These strings are verbatim in every build; a build that
paraphrases them has rewritten the firm.

**Numbers rule.** A figure may appear only if the catalogue
object holds it (§6.13); copy written before the figures exist
carries bracketed slots — "[grind time]" — never plausible
inventions awaiting correction.

## 13. Full-page scroll choreography map

The home page, top to footer, in order. (Other page types reuse
the beats their elements appear in.)

1. **0% — the name, dry.** Hero stands dry and complete; dust
   still. The visitor can read everything already.
2. **0–3% — the grind.** (§6.1/§6.2, load-triggered, may
   complete before first scroll.) The ground is made; the name
   binds; dust starts.
3. **First scroll — the first tint.** The hero's red ochre meets
   the intro sheet's chalk at the boundary: PR102 : PW18 mixing
   (§6.4), the smear's first segment pulling in the rail
   (§6.6), the lid's first chip binding (§6.11) — three
   instruments agreeing the reading has begun.
4. **10–30% — the cakes.** Catalogue slots seat one by one
   (§6.3); cards wipe their photographs in; the visitor's first
   hover binds a cake (§6.7), their first click grinds one
   (§6.8). The page is getting wetter under the hand.
5. **45–60% — the pin.** The full mix (§6.5) takes the scroll
   over at the wet lerp; lump to stroke across 150vh; the
   recipe inks step by step.
6. **60–65% — the figures.** The pin releases; the figures band
   counts (§6.13) — the recipe's numbers, confirmed.
7. **65–80% — the ledger.** Mix rows slide their chips together
   (§6.14); boundaries already crossed arrive pre-mixed; the
   reader audits what their scroll has done.
8. **80–85% — the green earth.** The final pigment slot; the
   smear's last segment pulls; the lid's last chip binds.
9. **85–100% — the slab.** The order form (§6.15), calm, its
   fineness pre-set by beat 4's grinding.
10. **100% — the colophon.** The stripe wipes in tin order
    (§6.17); the smear rail aligns with it; the bill of
    materials closes the page. **Reverse pass:** boundaries
    un-mix, the pin un-makes its stroke back to earth, chips
    dry in the lid — but seats, grinds, counts and the colophon
    stay done. The page forgets positions, never work.

## 14. Whole-page performance budget

- **Weight.** Total page ≤850KB: HTML/CSS/JS ≤210KB, inline SVG
  (textures, diagram, mullers) ≤60KB, fonts (Alegreya +
  Alegreya Sans subsets, woff2) ≤120KB, photography ≤460KB
  (cake-frame images at their displayed size, WebP/AVIF).
- **Frame budget.** The shared loop's per-frame work ≤1.6ms on
  a mid-tier phone: one lerp pass writing ≤6 custom properties
  (scroll value, ≤4 boundary `--mix` values, active smear
  segment, gloss x), transforms and opacity only on animated
  layers. No layout reads inside the loop except the cached
  section offsets, re-measured on resize only.
- **Long tasks.** No task >50ms during scroll; counters and
  chip slides are staggered to stay under it.
- **Cut order** (when the budget is exceeded, cut in this order,
  never out of it): 1. dust (§6.10 — designated first sacrifice);
  2. card tilt (§6.12); 3. boundary knife streak; 4. smear snap
  animation (segments jump instead); 5. diagram draw (prints
  drawn). **Never cut:** the boundary mixes themselves, the
  watchdog fallbacks, the reduced-motion variants, the
  colophon's completeness, or any contrast licensing.
- **Mobile budget.** ≤600KB (photography ≤300KB), loop ≤2ms,
  dust at 12 motes.

## 15. Build-order checklist

1. Token block first: the five anchors, bound/deep variants and
   duration/easing tokens from §2/§5 — nothing is styled before
   the pigments exist.
2. The catalogue object: pigments, indices, sources, grind
   figures, prices, stock — the single source (§6.13).
3. Static tin: slots, boundaries at their 50% mixes, colophon —
   the complete no-JS page, checked readable end to end.
4. Typography per §3, including the index voice and the
   figures rule.
5. Header/lid (§6.11) and footer/colophon (§6.17) generated
   from the section list; three-printings agreement checked
   (§10.5).
6. Cards (§6.12) generated from the catalogue; tickets audited
   against it.
7. The shared loop: lerp 0.12/0.09, section tracking, cached
   offsets.
8. Boundary mixing (§6.4) wired to the loop; recipes printed;
   ratio audit (§10.10) run.
9. Smear (§6.6) wired to the same tracking as the lid.
10. Hero: grind (§6.1), headline bind (§6.2), dust (§6.10) —
    in that order, each with its watchdog live before the next
    is added.
11. Slot settles (§6.3), then the pin (§6.5) and diagram
    (§6.9).
12. Interactions: gloss (§6.7), grind (§6.8), counters
    (§6.13), ledger (§6.14).
13. The order slab (§6.15), skeleton and smear transition
    (§6.16), the empty slot (§6.18).
14. Reduced-motion pass: every element's variant verified
    against its spec, one by one.
15. The §10 gate, run whole, signed by someone who did not
    build the page. A gate signed by its own builder is not
    signed.
