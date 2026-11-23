# 55. River Stone — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** Everything on the page has been worn smooth by
water: pebble-shaped containers, type that flows around obstacles,
and a gentle current running through the whole scroll. No sharp
corner exists anywhere on the page. Palette anchors: dry pebble
`#E9E7E0`, wet pebble `#B9B4A6`, river grey `#7A7668`, algae
`#46554C`, deep pool `#2C3833`. Type: Bitter (display — rounded
terminals) + Source Sans 3 (body). Every card, button, image and
even the cookie banner is a pebble — asymmetric border-radius
blobs; a streambed hero where cards settle among each other; one
dark deep-pool section where everything slows.

## 1. Concept & world

River Stone is the website of a place the water got to first. Its
single material fact is erosion: given enough seasons, a river
takes every edge off everything it touches, and what remains is
not damaged but *finished* — smooth, heavy, cool, impossible to
cut yourself on. The page performs that finishing. Every
container is a pebble: an asymmetric blob of a border-radius, no
two alike, because no two stones in a bed are alike. Every section
sits slightly downstream of the one before it, because the whole
page is in a current. Photographs are stones still being worn —
their masks never quite finish morphing. And once, midway, the
page deepens into a pool where the current nearly stops, the
background goes dark green-black, and every duration on the page
stretches — the interface itself slows its breathing where the
water is deep.

The world the page performs is a streambed at walking pace. The
visitor is not a user clicking through screens; they are the
current, and the content is what the current carries them past.
Offers are stones settled in the bed. Progress is a small pebble
rolling downstream in the margin. Reveals are stones lifted out of
the water, dripping, their undersides darker than their tops.
Nothing arrives with a snap, a slide or a fade-from-nowhere: in
this world things *settle*, *drift*, *lift* and *wet*, and the
four verbs are the entire vocabulary of arrival.

**The theme's one law: no edge on this page was cut; every edge
was worn.** The law is mechanical and the quality gate audits it
two ways. (1) *The corner audit:* every visible container —
card, button, input, image, banner, modal-equivalent, the cookie
notice, the scrollbar thumb where the platform allows styling —
carries one of the declared pebble recipes of §4 (eight-value
asymmetric radii, no value under 18px on any element larger than
44px in either dimension, no value ever 0). A single square
corner, a single 4px "subtle" radius, a single right angle in an
SVG icon stroke is a gate failure: in this world a cut edge is a
lie about how the thing was made. The one licensed exception is
type itself — letterforms keep the foundry's own terminals,
because Bitter's rounded terminals were chosen precisely so the
exception is barely visible. (2) *The wet audit:* a pebble may
only darken — dry `#E9E7E0` toward wet `#B9B4A6` — when the page's
current has actually passed over it: it has been scrolled
through, lifted, hovered, or rained on by the wet-sheen band
(§6.10). Decorative pre-darkened "wet-look" stones scattered for
texture are forbidden, because wetness on this page is a record
of contact, not a style. The corollary governs numbers: **every
figure on the page is a river measurement taken from the one
declared river object** (§2, the gauge record) — the level in
centimetres, the flow in litres per second, the age of the oldest
stone in years — printed in the hero chip, the figures band and
the footer, three printings of one record that can never
disagree. An invented "1,200 happy guests" is a gate failure;
the river does not keep that kind of count.

**Best-fit sites and audiences.** Riverside, lakeside and
streamside lodges, cabins and bath houses; onsen and wild-swimming
retreats; stone and landscaping merchants selling river rock,
pebble and gravel by the tonne; fly-fishing guides and tackle
shops; geological and natural-history museums; water charities
and river trusts; a potter working in river clay; any slow,
restful hospitality offer whose honest claim is *nothing here
will jar you*. The audience it suits is unhurried and slightly
tired of the internet: people booking rest, who read at walking
pace, who will notice that the cookie banner is a stone and feel
looked after by it. Conversion in this world is a booking, an
enquiry, a membership — acts done once, calmly, and remembered.

**When NOT to use it.** Not for anything urgent, sharp or
competitive: news, trading, live sport, flash retail — the
current's tempo would read as indifference, and the corner audit
forbids the visual shouting those genres need. Not for dense
tools or dashboards: pebble radii waste the corners tables live
in, and §11 refuses the data grid outright. Not for brands whose
identity is precision — watchmaking, engineering, aviation — a
worn edge says the opposite of machined. Not for pages that must
carry heavy advertising furniture: third-party ad units arrive as
rectangles, and one rectangle breaks the law for the whole page.
And not where the client cannot accept slowness as a feature:
every duration in this theme is longer than fashion dictates,
deliberately, and a client who asks to "make it snappier" is
asking for a different theme.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme, and
the build fails on an undeclared colour the way it fails on an
undeclared word.

| Token | Hex | Role | Ratio & pairing |
|---|---|---|---|
| `--dry` | `#E9E7E0` | Dry pebble — the page's ground, un-wetted surfaces, card faces at rest | ~62% of surface. Ground for `--pool` text at **9.86:1** and `--algae` text at **6.37:1** (measured) |
| `--wet` | `#B9B4A6` | Wet pebble — a surface the current has passed over; hover-wet, skeleton-wet, the lifted stone's underside | ~14% of surface. On `--dry` it measures only **1.67:1** — surfaces only, *never* text, never an edge that must be found by eye alone (paired always with the §6.7 wet-edge highlight) |
| `--grey` | `#7A7668` | River grey — captions, datelines, the margin line the progress pebble rolls on, disabled states | ~9% of surface. On `--dry` **3.67:1** (measured): licensed for large text ≥18px and captions only, never body copy; on `--pool` 2.68:1, graphical only |
| `--algae` | `#46554C` | Algae — secondary text, links, the current's direction arrows, form rules | ~9% of surface. On `--dry` **6.37:1** (measured): the only mid-tone licensed for body-size text |
| `--pool` | `#2C3833` | Deep pool — the pinned dark section, the footer, primary text ink everywhere | ~6% of surface as ground; as ink on `--dry` **9.86:1** (measured), the page's primary text pairing. `--dry` text on `--pool` also 9.86:1; `--wet` on `--pool` **5.89:1** (measured), the pool's secondary text |

Derived tokens (closed list): `--pool-deep #22302A` (the pool at
its deepest beat, §6.4, reached only at the pin's midpoint);
`--algae-deep #33413A` (algae pressed — focus rings and error
rules, on `--dry` **8.67:1** measured); `--wet-deep #A39D8C` (the
underside of a lifted stone, §6.7; surfaces only); `--sheen
rgba(233,231,224,0.55)` (the wet-sheen band's light, §6.10 —
`--dry` at 55% so the band can only lighten toward dry, never
introduce a new colour); `--edge-wet rgba(70,85,76,0.35)` (the 1px
wet edge that prints where a waterline has just passed, algae at
35%).

**The river object.** All figures derive from one declared
record, authored once per site and printed three ways (§6.12,
§6.15, §6.17). For the worked examples the record is: gauge
height **64 cm** at the lodge stone, flow **1,180 L/s**, oldest
bed stone **11,400 years**, bed stones counted **214**, deepest
pool **2.3 m**. A figure that cannot be traced to a field of
this record — or, on a real build, to the client's own gauge,
survey or stock book — is not printed (§10, gate 4).

**Dark behaviour.** The theme has no dark *mode*; it has the
pool. `prefers-color-scheme: dark` does not invert the page: the
streambed stays dry-lit, because a river at night is still the
same river and the fiction is a place, not a scheme. What dark
preference changes is the pool's share: the deep-pool section
(§6.4) and the footer (§6.17) are joined by the header band
resting at `--pool` instead of `--dry`, and the wet-sheen band's
opacity drops to 0.35 so it reads as moonlight on water rather
than sun. Print: the pool prints as `--dry` with a `--pool`
hairline pebble outline — ink is expensive and the record is the
content; the colophon line about corners (§6.17) prints verbatim.

## 3. Typography

Two families, inherited exactly. **Bitter** — chosen for its
rounded terminals and slight slab weight — carries display,
headings, card titles, prices and the figures; it is the stone
voice: heavy, smooth, unhurried. **Source Sans 3** carries body,
captions, forms and data; it is the keeper's voice: plain,
legible, never performing. No third family exists in the theme;
a monospace need (the gauge record, §6.15) is met by Source Sans
3 with `font-variant-numeric: tabular-nums`, because a river
gauge is read, not machined.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero) | Bitter 700 | 54px / 1.08 (≥1200), 42px (768–1199), 32px (<768) | −0.01em | Sentence case always; the headline is a sentence the river says, not a shout |
| H2 (section) | Bitter 700 | 34px / 1.15 | −0.005em | One per section, seated at the section's upstream edge |
| H3 / card title | Bitter 600 | 21px / 1.25 | 0 | Card titles name the stone (the room, the offer), never a slogan |
| Body | Source Sans 3 400 | 17px / 1.65 | 0 | Measure 56–64ch; line-height is the current's pace — never below 1.55 |
| Caption / dateline | Source Sans 3 600 | 13px / 1.45 | +0.04em, uppercase | `--grey` only at ≥18px-equivalent weight — captions use `--algae` at 13px (§2 contrast ruling) |
| Figures | Bitter 600 | 30px / 1.1 | tabular | Numbers are stones too: Bitter, never the sans |
| Form label | Source Sans 3 600 | 14px / 1.4 | +0.01em | `--pool`; error text `--algae-deep` with the §6.14 rule |

**Type laws.** (1) *Sentence case everywhere* — title case is a
cut edge made of words. (2) *The headline's letters settle, they
do not appear* (§6.12): per-letter animation is restricted to
the hero, capped at 24 characters, and every letter's final
position is its printed position — the DOM ships set in full.
(3) *Figures always carry their unit and their source* — "64 cm
at the lodge stone", never a bare 64 (§12). (4) *No italic for
emphasis in body copy*; Bitter italic is reserved for the river's
own quoted speech in the pool section (§8.2) — one voice, one
device. (5) *Underlines are waterlines*: links are underlined
with a 1px `--algae` line that thickens to 2px on hover over
300ms `--ease-drift`; no other text decoration exists in the
theme, and strikethrough is forbidden — a withdrawn offer is
removed and its absence noted in words (§12), never struck.

## 4. Layout language

**The bed.** The page is a single streambed, one column of
sections flowing downstream inside a 1200px maximum measure,
each section a shallow basin: content rests in pebble clusters
with 28–44px of water (gap) between stones, the gaps irregular
by design — a strict grid reads as a fish farm, and §9 names it
a failure. Section padding is deep: 96px top / 112px bottom at
≥1200px, because stones need water around them; density falls
downstream (the hero bed is fullest; the pool is emptiest; the
footer is a single row of stones on the bank).

**Pebble recipes.** Eight declared radius recipes, named for
their stones, assigned by role and never improvised:
`--pebble-hero: 58% 42% 55% 45% / 50% 55% 45% 50%` (the original
entry's recipe, kept verbatim, for hero cards); `--pebble-card:
46% 54% 52% 48% / 55% 46% 54% 45%`; `--pebble-flat: 38% 62% 44%
56% / 62% 40% 60% 38%` (wide low stones — banners, the cookie
pebble); `--pebble-tall: 52% 48% 40% 60% / 42% 55% 45% 58%`;
`--pebble-btn: 47% 53% 50% 50% / 58% 44% 56% 42%` (buttons and
the form's submit stone); `--pebble-chip: 44% 56% 48% 52% / 52%
48% 55% 45%` (chips, tags, the gauge chip); `--pebble-img` (the
morphing mask's rest state, §6.3: `50% 50% 46% 54% / 56% 44% 56%
44%`); `--pebble-field: 40% 60% 55% 45% / 45% 55% 45% 55%`
(inputs — a worn trough, the shallowest recipe, still never
under 14px on any axis). Alternates mirror horizontally per
nth-child (`scaleX(-1)` on the radius via the paired recipe
`--pebble-card-alt`) so neighbouring stones never share a
silhouette.

**The current's geometry.** Sections alternate a ≤6px lateral
offset (§6.2): odd sections rest at translateX(0), even sections
at up to +6px downstream-drift at mid-travel, returning to 0 at
their rest position — the offset is a *passage*, not a resting
misalignment; a section photographed at rest is aligned. The
margin rail (≥1200px only, 72px wide, left) holds exactly two
things: the rolling progress pebble's wavy line (§6.5) and
nothing else. Whitespace is water: it is the medium the stones
sit in, it is never "empty", and §9 treats a section whose gaps
have been squeezed to uniform 8px as a dried-out bed — a failure
of the theme, not an optimisation.

**The pool's geometry.** The deep-pool section (§6.4) breaks
the bed's measure: full-bleed `--pool`, content narrowed to
52ch, one column, nothing in the margin rail — the pebble
progress line dives and is not drawn inside the pool (the stone
is underwater; §6.5 states the ruling).

## 5. Full motion system

Five named easings, closed list. `--ease-settle:
cubic-bezier(0.34, 1.30, 0.44, 1)` — the collision damp: a
stone arriving overshoots by at most 2px and comes back once,
gently; used by §6.1, §6.8, §6.13. `--ease-drift:
cubic-bezier(0.45, 0.05, 0.35, 1)` — the current: slow in, slow
out, no overshoot; used by §6.2, §6.5, link underlines.
`--ease-lift: cubic-bezier(0.22, 0.90, 0.30, 1)` — the
waterline rising off a lifted stone; used by §6.7, §6.16.
`--ease-ripple: cubic-bezier(0.15, 0.60, 0.35, 1)` — rings
expanding and thinning; used by §6.9, §6.14's success.
`--ease-soak: cubic-bezier(0.55, 0.06, 0.45, 1)` — wetting and
drying, the slowest attack; used by §6.3's morph crossfades,
§6.10, §6.16's skeleton.

**One shared loop.** Every scrubbed value on the page — drift
offsets, morph phase, the progress pebble's position, the
pool's depth factor, parallax translations — is written by a
single `requestAnimationFrame` loop lerping toward scroll
targets at **0.12** (0.10 inside the pool's pin, where the water
is deeper). No scroll handler writes styles. No element runs
its own rAF. The loop sleeps when the tab is hidden and when
every value is within 0.1px of target.

**The motion terms, in this theme's language.** *Scroll-triggered
reveals* are waterline lifts (§6.7) — content is uncovered, never
faded in from nothing. *Parallax* is three-speed streambed
parallax (§6.2): surface stones at 1.0× scroll, mid-bed at
0.96×, deep elements at 0.92× — a total spread of 8%, because a
river's layers move together. *Pinned scenes:* exactly one —
the deep pool (§6.4), ~130vh. *Masked reveals:* the waterline
mask (§6.7) and the streamline's draw (§6.6) are the only masks;
there are no clip-path wipes shaped like anything else.
*Blur-to-sharp* is refused: nothing in a river is out of focus,
it is only underwater, and underwater is rendered by the wet
tokens, not by blur. *Animated counters* count river
measurements only (§6.15), over 1400ms, from the value at the
last printing — never from zero. *Progress* is the rolling
pebble (§6.5); there is no bar. *Marquees* are refused: nothing
in a streambed moves sideways forever; the footer's stone row
is still. *Ambient loops:* exactly two — the pebble-mask morph
(§6.3, 12s) and the wet-sheen band (§6.10, 20s); both pause
off-screen and under `prefers-reduced-motion`, and §10 counts
them. *Micro-interactions:* the hover nudge (§6.8), the click
ripple (§6.9), the button's 1px sink on active. *Hover
physics:* stones tilt like stones rolled in the palm — soft,
heavy, max 4°, §6.13 — never springy, never magnetic.
*Page transitions:* the current carries the page away (§6.16).
*Image treatment:* photographs live inside morphing pebble
masks (§6.3) and are uncovered by waterlines like everything
else; there is no zoom-on-hover — you do not zoom a stone.

**Durations ledger.** Settle 700ms; drift scrub continuous;
morph loop 12,000ms; waterline lift 800ms; nudge 450ms; ripple
700ms; sheen pass 20,000ms; counters 1400ms; pool tempo factor
1.8×; page transition 550ms out / 650ms in. Any duration not in
this ledger does not exist in the theme.

## 6. Signature elements

### 6.1 Streambed settle

- **What & why.** The hero's cards — the lodge's rooms and
  offers — drop 14–20px into their streambed arrangement and
  settle with a soft collision damp, upstream stones first, each
  landing nudging its neighbours 1–2px as if displacing water
  and gravel. It belongs because the hero's layout *is* the
  product: a bed of stones the lodge sits on. A visitor who
  watches the offers settle has understood the place before
  reading a price.
- **Structure.** Real cards in a flex-wrap bed inside the hero
  section, each carrying `--pebble-hero` (alternating
  `--pebble-hero-alt` per nth-child) and its final position in
  normal flow from first paint. The settle is a transform-only
  layer: JS arms each card with `translateY(-(14 + i×2)px)` and a
  `data-settle` index ordered by DOM position read as upstream →
  downstream (left-to-right, then row). Neighbour nudges are
  applied to the two adjacent cards as a transient 1–2px
  translate on the landing frame, decaying over 300ms. No
  wrapper, no canvas; the bed is the DOM.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 600ms timer. Each card falls over 700ms
  `--ease-settle` with a 90ms stagger upstream-first; the
  two-bounce damp is the easing's own overshoot (≤2px) plus one
  authored 1px rebound at t=+120ms after landing. Total ceremony
  for a six-card bed: 700 + 5×90 = 1150ms. A card already in the
  viewport on a return visit (`sessionStorage` flag) ships
  settled; the ceremony is a first-arrival rite, not a loop.
- **States.** Unsettled (JS-armed only, ≤20px above rest) →
  falling → settled (rest). Hover during fall: the fall
  completes — a stone does not stop mid-water for a pointer.
  Scrolled-past: settled; the bed never re-settles on scroll-back.
- **Content merge.** The cards are the rooms and offers
  themselves — name, photograph, price, booking link — and the
  bed they settle into is the hero's layout, not a stage in
  front of it. Remove the animation and the hero is unchanged,
  merely already arrived.
- **Failure fallback.** Watchdog at 1600ms: any card not settled
  snaps to rest and arming classes are stripped. No JS: cards
  are simply in their bed, printed. Slow network: the ceremony
  waits for fonts or the 600ms race, never for images — a card
  settles with its photograph's pebble mask empty-dry (§6.3) and
  the photograph waterlines in when it arrives.
- **Reduced-motion variant.** No fall. Cards ship settled; the
  only motion is the §6.6 streamline drawing itself, and under
  reduced motion that too is printed complete (§6.6).
- **Performance budget & mobile variant.** Transform-only, six
  cards maximum in the hero bed; the settle costs one composited
  layer per card for ≤1150ms, then layers are dropped. Mobile
  (<768px): the bed is one column, fall distance halves to
  8–10px, stagger 60ms, neighbour nudges cut (a single column
  has no lateral neighbours to displace).
- **Choreography timeline (v2).** t=0 fonts ready (or 600ms race
  lost → printed bed, ceremony skipped) → t=0 first upstream
  card begins its 700ms fall → stagger 90ms per card downstream
  → each landing fires its neighbours' 1–2px nudge, decaying
  300ms → last card lands at t≤1150ms → t=+200ms the §6.6
  streamline begins its draw around the settled bed → t=1600ms
  watchdog deadline passes with the bed at rest.
- **State matrix (v2).** *Rest:* settled, dry, full contrast.
  *Hover:* §6.8's nudge (post-settle only). *Focus:* focus
  entering the bed completes any running settle instantly — a
  keyboard visitor is never asked to wait for gravel. *Active:*
  the card's own link behaves per §6.9 on click. *Scrolled-past:*
  settled, printed. *Disabled / no-JS:* settled at first paint.
  *Touch:* identical; first touch anywhere completes a running
  settle.
- **Breakpoints (v2).** ≥1200px: multi-row bed, 14–20px falls,
  90ms stagger. 768–1199px: two-column bed, 12–16px falls, 75ms
  stagger. <768px: one column, 8–10px falls, 60ms stagger, no
  neighbour nudges.
- **Edge cases & failure modes (v2).** *Seven or more hero
  cards:* refused at build — the bed holds six; a seventh offer
  belongs in §6.13's listing, and §9 names the crowded bed a
  failure. *Card taller than the bed's row:* the wrap is
  authored per breakpoint; a CMS-added long title wraps inside
  its pebble (padding 28px minimum) and never changes the fall
  distance, which is index-based, not height-based. *Resize
  mid-fall:* falls are transform-only and layout-independent;
  a resize re-reads rest positions and the loop re-targets.
  *User scrolls during the ceremony:* the bed is in the hero;
  scrolling away pauses nothing — the settle finishes on its own
  timeline and is at rest when the visitor returns.
- **Accessibility spec (v2).** Cards are real `<article>`s with
  real links; the settle is never announced and never delays
  focus. Focus order is DOM order (upstream → downstream), which
  is also the reading order. Card text contrast: `--pool` on
  `--dry` 9.86:1 at rest and at every settle frame, because the
  transform never crosses text with another layer.
- **Tokens consumed (v2).** `--dry`, `--pool`, `--pebble-hero`,
  `--pebble-hero-alt`, `--ease-settle`, `--dur-settle` (700ms),
  `--dur-stagger-bed` (90ms), `--dur-fallback-hero` (1600ms).

### 6.2 Downstream drift & three-speed parallax

- **What & why.** The whole page is in the current: each section
  carries a barely-perceptible lateral translation — at most
  6px — whose direction alternates by section, scrubbed across
  its viewport travel, while three depth layers parallax at
  1.0× / 0.96× / 0.92×. It belongs because drift is the theme's
  thesis stated continuously: you are not scrolling a document,
  you are being carried past a bed. At 6px it is felt, not seen —
  visitors report the page as "calm" without knowing why.
- **Structure.** Sections carry `data-drift="+1"` or `"-1"`
  alternating in DOM order. The shared loop (§5) computes each
  visible section's viewport progress p ∈ [0,1] and writes
  `translateX(dir × 6 × sin(π × p))px` — zero at both rest
  positions, maximum at mid-passage. Parallax layers are marked
  `data-depth="surface|mid|deep"` and receive translateY offsets
  of 0 / −0.04× / −0.08× of their travelled distance, applied to
  decorative strata only (photograph masks, the §6.6 streamline
  layer, background pebble silhouettes) — never to text blocks,
  whose position must stay put for reading.
- **Motion spec.** Trigger: scroll, continuous, via the shared
  loop at lerp 0.12. Drift is a pure function of scroll
  position — no duration, no easing curve of its own; the lerp
  *is* the smoothing. Inside the deep pool (§6.4) the drift
  amplitude multiplies by the pool's depth factor down to
  ≤0.5px: deep water barely moves.
- **States.** At rest (section fully above or below): offset 0.
  In passage: offset follows the sine. Hover/focus: no effect —
  the current does not respond to a pointer. Scrolled-past:
  offset returns to 0 exactly; a section screenshotted at rest
  is aligned with its neighbours, which §10's audit checks.
- **Content merge.** The drift moves the sections themselves —
  the actual copy, cards and forms — not a background behind
  them. The parallax layers are the sections' own photographs
  and drawn strata. There is no decorative layer that exists
  only to move.
- **Failure fallback.** If the loop never runs (no JS, script
  error), every offset is 0 and the page is a still, aligned
  streambed — complete and correct. A `matchMedia` change to
  reduced motion mid-session zeroes targets and the loop settles
  them within ~300ms.
- **Reduced-motion variant.** Drift and parallax are off
  entirely; sections rest aligned; the pool's tempo change
  (§6.4) also rests. Nothing about the information changes.
- **Performance budget & mobile variant.** The loop writes
  transforms for visible sections only (IntersectionObserver
  gates the active set, ≤4 sections + ≤6 parallax layers per
  frame), transform/opacity only, no layout reads inside the
  frame beyond cached rects refreshed on resize. Mobile
  (<768px): drift amplitude halves to 3px (a narrow viewport
  makes lateral motion proportionally larger) and the deep
  parallax layer is cut — two speeds are enough on a phone.
- **Choreography timeline (v2).** Continuous: as a section's
  top crosses the viewport bottom, p leaves 0 → offset grows
  along the sine → peaks (6px, or 3px mobile) as the section's
  centre crosses the viewport centre → returns to 0 as its
  bottom leaves the top. In the pool, the same curve is
  multiplied toward 0.083 (0.5px) by the depth factor across the
  pin's first 30%.
- **State matrix (v2).** *Rest:* 0px. *Hover:* 0px change.
  *Focus:* a section receiving focus mid-drift keeps drifting —
  focus outline travels with its element, both transform from
  the same loop, so they can never separate. *Active:* n/a.
  *Scrolled-past:* 0px, aligned. *Disabled / no-JS:* 0px.
  *Touch:* identical; touch scroll velocity changes only how
  fast p moves, never the amplitude — the current does not
  hurry because the visitor flings.
- **Breakpoints (v2).** ≥1200px: 6px, three speeds, margin rail
  present. 768–1199px: 5px, three speeds. <768px: 3px, two
  speeds, deep layer cut.
- **Edge cases & failure modes (v2).** *Very tall section
  (>200vh of content):* p is computed against the viewport
  travel of the section's *first* 150vh; beyond that the offset
  rests at 0 so a long listing never sits permanently displaced.
  *Horizontal overflow:* drift is capped so section + offset
  never exceeds the bed's padding — sections carry 12px of
  lateral slack in their basin padding for exactly this.
  *Jump scroll (anchor link, find-in-page):* targets update
  instantly and the lerp settles within ~400ms; content is
  readable throughout because text never parallaxes. *Scroll
  back up:* the sine is symmetric — the passage upstream is the
  passage downstream, reversed; nothing is latched.
- **Accessibility spec (v2).** Drift is decorative motion on
  real content; it never moves a focus target by more than the
  focus outline's own travel in the same frame, and it is fully
  removed under `prefers-reduced-motion`. Vestibular note in
  §15's checklist: amplitude is capped at 6px precisely because
  the theme's calm is the accessibility feature. Contrast is
  unaffected at every offset.
- **Tokens consumed (v2).** `--ease-drift`, `--drift-max` (6px),
  `--lerp-page` (0.12), `--lerp-pool` (0.10), `--parallax-mid`
  (0.96), `--parallax-deep` (0.92).

### 6.3 Morphing pebble masks

- **What & why.** Every photograph lives inside a pebble mask
  that is still being worn: its eight-value border-radius slowly
  morphs through a four-keyframe cycle over 12s, phase-offset
  per stone, and additionally reshapes slightly under scroll
  scrub — a stone near the viewport centre is at its roundest;
  entering and leaving, it is marginally more elongated, as if
  seen through moving water. It belongs because the photographs
  are the site's stones (the rooms, the river, the food), and a
  finished, frozen shape would contradict the river's ongoing
  work.
- **Structure.** A `<figure class="pebble-img">` with
  `border-radius: var(--pebble-img)` and `overflow: hidden`
  around a real `<img>`. The morph animates the element's
  `border-radius` between four authored keyframe recipes
  (`--pebble-img-a/b/c/d`, each a full eight-value recipe, all
  values within 38–62% so the stone never approaches a corner
  or a circle). Phase offset is `animation-delay: calc(var(
  --phase) * -1s)` with `--phase` ∈ [0,12) assigned per index.
  The scroll reshape writes a fifth value: the loop interpolates
  the *animation's* playback influence by scaling a CSS variable
  `--round` (0.94–1.0) that multiplies the vertical radii via
  `calc()` in a `border-radius` shorthand on a wrapper — the
  keyframed mask and the scrubbed roundness compose on two
  nested elements so neither fights the other.
- **Motion spec.** Time loop: 12,000ms, `--ease-soak` between
  keyframes (border-radius is not transition-eased by the
  keyframe timing function alone; the keyframes carry
  `animation-timing-function` per segment). Scroll scrub: the
  wrapper's `--round` follows the shared loop (lerp 0.12) toward
  1.0 at viewport centre, 0.94 at the edges of travel. The morph
  never pauses for hover — water does not stop because you look
  at a stone — but it does pause off-screen
  (`animation-play-state` via IntersectionObserver) and in the
  pool it slows to 21,600ms (12s × the pool's 1.8 tempo factor).
- **States.** Rest: mid-cycle, phase-offset. Hover: no change to
  the mask (the card beneath it nudges, §6.8; the stone itself
  keeps being worn). Focus-within: morph continues; the focus
  ring is drawn on the card, never on the mask. Scrolled-past:
  phase preserved — returning shows the cycle where it would
  have been, because the delay is negative and absolute.
- **Content merge.** The mask *is* the photograph's frame: the
  room's window view, the river bend, the breakfast. There is no
  image on the page outside a pebble mask, and no pebble mask
  without an image (or its §6.16 dry skeleton) inside it.
- **Failure fallback.** No JS: masks rest at `--pebble-img`,
  complete photographs in pebble frames — the morph is an
  enhancement of a finished state. If `border-radius` animation
  is unsupported (very old engines), the mask is static; the
  gate (§10) treats that as an acceptable degradation, never as
  missing content. A failed image leaves the dry pebble with its
  alt text set in Bitter inside it (§12's empty voice), not a
  broken-image glyph — the glyph has corners.
- **Reduced-motion variant.** The mask rests at `--pebble-img`
  permanently; `--round` is fixed at 1.0. The photograph is
  identical; only the wearing rests.
- **Performance budget & mobile variant.** `border-radius`
  animation repaints the mask edge each frame: capped at 6
  morphing masks per viewport (further masks rest until scrolled
  near), each mask ≤ 480px on its long edge. Mobile (<768px):
  the cycle lengthens to 16s and only masks in the viewport
  animate (≤3); the scroll-roundness composition is cut — one
  nested wrapper fewer on a phone GPU.
- **Choreography timeline (v2).** Continuous loop, per stone:
  t=phase → recipe a → 3s `--ease-soak` → recipe b → 3s → c →
  3s → d → 3s → a. Scrub overlay: as the stone's centre
  approaches the viewport centre, `--round` lerps 0.94 → 1.0;
  leaving, 1.0 → 0.94. Entering the pool: cycle duration
  stretches ×1.8 across the pin's first 30% (§6.4).
- **State matrix (v2).** *Rest:* morphing at phase. *Hover:*
  morphing (unchanged); card nudges beneath. *Focus:* morphing;
  ring on the card. *Active:* n/a. *Scrolled-past:* phase
  preserved, paused off-screen. *Disabled / no-JS:* static
  `--pebble-img`. *Touch:* identical; no touch state alters the
  mask.
- **Breakpoints (v2).** ≥1200px: 12s cycle, ≤6 live masks,
  roundness composition on. 768–1199px: 12s, ≤4 live. <768px:
  16s, ≤3 live, roundness cut.
- **Edge cases & failure modes (v2).** *Portrait vs landscape
  photographs:* recipes are percentage-based and axis-relative,
  so one recipe set serves both; §15's checklist includes a
  portrait crop check because the vertical radii bite harder on
  tall stones. *Image with its subject at the edge:* the morph's
  maximum bite is 6% of the short axis; §12's image rule requires
  subjects centred with 10% clearance — a face at the frame edge
  is a content failure, not a mask failure. *Huge hero image:*
  the hero mask (§6.12) morphs at half amplitude (values clamped
  44–56%) because a 900px stone repainting its whole edge is the
  theme's most expensive frame.
- **Accessibility spec (v2).** The mask is presentation; the
  `<img>` carries real alt text, and the figure's caption is
  real text outside the mask. Morphing never clips the caption.
  Under reduced motion the mask is static. Contrast of caption
  text is `--pool` on `--dry` 9.86:1 regardless of the mask's
  phase.
- **Tokens consumed (v2).** `--pebble-img`, `--pebble-img-a/b/c/d`,
  `--ease-soak`, `--dur-morph` (12,000ms), `--round` (0.94–1.0).

### 6.4 The deep pool

- **What & why.** Once per page, the bed deepens into a pool:
  the section pins for ~130vh while its background deepens from
  the bed's `--dry` through `--pool` to `--pool-deep` at the
  pin's midpoint and back to `--pool`, every animation duration
  inside stretches ×1.8, drift slows to near zero, and the
  reflective copy — the lodge's story, the river's history — is
  read at the water's own pace. It belongs because depth must be
  *felt in the interface's tempo*, not described: the visitor's
  scroll itself slows down here, and they understand "deep"
  with their hand before their eye.
- **Structure.** A full-bleed `<section class="pool">` with a
  sticky inner (position: sticky, 100vh) inside a 230vh track
  (100vh of pin travel ≈ the original's ~130vh of pinned
  passage). Inside: one column at 52ch, the story copy, one
  pebble-masked photograph (§6.3), the pool's own figures
  (§6.15's second printing). A `--depth` custom property
  (0 → 1 → hold) is written by the shared loop from pin
  progress; background colour, the tempo factor and the drift
  multiplier are all functions of `--depth`, declared in CSS as
  colour interpolation between the three tokens — one variable,
  three expressions, so the pool can never be dark but fast, or
  slow but light.
- **Motion spec.** Trigger: scroll through the pin. Depth curve:
  progress 0–0.35, `--depth` 0→1 (the descent); 0.35–0.75, hold
  at 1 (the deep); 0.75–1, the section unpins and the page
  "shallows" — background returns to `--pool` (it does not
  lighten back to `--dry`: you surface into the footer's bank,
  §6.17, which is also pool-dark; the *next* page or a scroll to
  top restores the dry bed). Tempo: every duration token inside
  the pool is multiplied by `1 + 0.8 × --depth`, reaching the
  full 1.8× at depth. Drift multiplier: `1 − 0.92 × --depth`,
  reaching 0.08 (≈0.5px). Loop lerp inside the pin: 0.10.
- **States.** Approaching: dry bed, normal tempo. Descending:
  colour and tempo interpolate together. At depth: `--pool-deep`
  ground, `--dry` text (9.86:1 against `--pool`; against
  `--pool-deep` higher still), durations at 1.8×, drift ≤0.5px.
  Scrolled-past: the pool rests at `--pool`, unpinned, its
  content fully read; scrolling back up re-runs the descent
  symmetrically — depth is a place, not an event, and it can be
  revisited.
- **Content merge.** The pool holds the page's most important
  slow content — the story, the philosophy, the memorial, the
  long read. It is never a gallery or a price list: §7 forbids
  conversion content inside the pool, because nothing is sold
  underwater. The figures printed here are the river object's
  second printing (§2), agreeing with the hero's to the digit.
- **Failure fallback.** No JS / no sticky support: the section
  renders as a static `--pool` section, full content, normal
  tempo — the depth becomes a colour, which is a loss of
  theatre, never of content. Watchdog: if pin progress cannot
  be computed (loop dead), `--depth` rests at 0.6 — mid-water,
  readable, honest — rather than at an extreme.
- **Reduced-motion variant.** No pin. The section is a static
  `--pool` section with its content in order; tempo factor is
  1.0 (durations are already long; the *stretch* is the motion
  being refused). The depth is conveyed by the copy and the
  colour alone.
- **Performance budget & mobile variant.** The pin is the
  page's single sticky element; colour interpolation runs on
  the compositor via a pre-rendered gradient layer whose opacity
  crossfades (two stacked backgrounds, `--pool` and
  `--pool-deep`, opacity = `--depth`) rather than per-frame
  colour computation. Mobile (<768px): the pin shortens to 160vh
  track / 60vh travel, tempo factor caps at 1.5×, and the pool
  photograph (§6.3) rests its morph — a phone in a pool is
  already working hard.
- **Choreography timeline (v2).** Section top reaches viewport
  bottom → sticky engages as its top reaches viewport top →
  p 0–0.35: `--depth` 0→1, ground `--dry`→`--pool`→(at 0.35)
  `--pool-deep` begins, tempo 1.0→1.8×, drift 6px→0.5px, the
  margin pebble (§6.5) dives and is not drawn → p 0.35–0.75: the
  deep — story copy read at stretched tempo, the pool photograph
  morphing at 21.6s → p 0.75–1: unpin approaches, ground settles
  to `--pool`, tempo and drift restore across the exit → section
  rests as a dark chapter between the bed and the footer.
- **State matrix (v2).** *Rest (above):* dry, 1.0×. *Rest (at
  depth):* `--pool-deep`, 1.8×, text `--dry` 9.86:1+.
  *Hover:* elements inside behave per their own specs at the
  stretched tempo. *Focus:* focus entering the pool during the
  descent completes the descent instantly to the depth of the
  focused element's beat — a keyboard visitor arrives *in* the
  deep, not mid-dive. *Active:* n/a. *Scrolled-past:* `--pool`,
  unpinned, complete. *Disabled / no-JS:* static `--pool`
  section. *Touch:* identical; fling velocity is damped by the
  0.10 lerp so a hard fling cannot skip the deep — it arrives
  a beat later, still slowly.
- **Breakpoints (v2).** ≥1200px: 230vh track, 1.8×, margin rail
  dives. 768–1199px: 210vh track, 1.7×. <768px: 160vh track,
  1.5×, photograph morph rested.
- **Edge cases & failure modes (v2).** *Two pools on one page:*
  refused at build (§7) — a river page has one deepest place;
  a second pin is a second theme fighting the first. *Pool
  content longer than the pin's beats:* the sticky inner
  scrolls its own overflow internally only as a last resort —
  the authored rule is that pool copy is edited to fit 100vh at
  52ch (roughly 380 words + one photograph); longer copy splits
  into a pre-pool section. *Browser with sticky inside overflow
  ancestors:* §15's checklist tests the pin in the real template;
  the fallback is the static section. *User scrolls back to the
  very top quickly:* depth unwinds along the same curve; no
  state is latched except §6.5's notches.
- **Accessibility spec (v2).** The pin never traps scroll: it is
  a sticky passage, escapable at native scroll speed in both
  directions, and focus order follows the DOM through it.
  Screen-reader order is the copy order; `--depth` is
  `aria-hidden` presentation. Text contrast at maximum depth:
  `--dry` on `--pool-deep` exceeds the 9.86:1 of `--pool`;
  `--wet` secondary text on `--pool` is 5.89:1 (measured, §2) —
  captions inside the pool use `--wet`, body uses `--dry`.
- **Tokens consumed (v2).** `--pool`, `--pool-deep`, `--dry`,
  `--wet`, `--depth`, `--lerp-pool` (0.10), `--dur-pool-track`
  (230vh), `--tempo-pool` (1.8).

### 6.5 Rolling progress pebble

- **What & why.** In the left margin rail, a 12px pebble rolls
  downstream along a wavy SVG line as the visitor reads,
  rotating with the distance travelled, and drops one
  section-notch — a small side-stone — each time a section is
  completed. It belongs because progress in this world is not a
  bar filling but a stone being carried: the reader is the
  current, and the pebble is the page's one traveller. It is
  also the theme's only progress indicator; §5 refuses bars.
- **Structure.** A fixed-position rail (≥1200px only) containing
  an inline SVG: one wavy path (the stream line, drawn in
  `--grey` at 40% opacity) whose length is measured at runtime,
  one `<circle>`-free pebble — a `<path>` blob with
  `--pebble-chip` proportions rendered as SVG, filled `--wet`
  with a `--pool` 1px outline — and one notch-stone per section,
  placed at each section's proportional position along the path.
  The pebble's position is `offset-path` along a duplicated CSS
  path where supported, with a transform fallback computed from
  the same measured length. Rotation is written by the loop:
  `rotate(distance / (2πr) × 360deg)` with r = 6px — the pebble
  rolls without slipping, a detail nobody will measure and
  everybody would feel if it were wrong.
- **Motion spec.** Trigger: scroll scrub via the shared loop
  (lerp 0.12), position = document progress mapped onto path
  length. Notch drop: when progress crosses a section boundary,
  that section's notch-stone animates 300ms `--ease-settle`
  from the line's side into its resting notch, once, latched.
  Inside the pool (§6.4) the pebble is not drawn — the stone is
  underwater — and the rail shows only the wavy line fading to
  15% opacity; it resurfaces, at the correct downstream
  position, as the pool shallows.
- **States.** Rest at top: pebble at the path's source, dry
  fill. Rolling: wet fill (the current has it now — §1's wet
  audit, satisfied by contact with the stream line). At a
  notch: the notch drops, the pebble pauses for 0ms — it does
  not pause; the drop happens beside it as it passes.
  Scrolled-past (page bottom): pebble rests at the path's end
  on the footer bank. Hover: none — the rail is not interactive.
  Focus: the rail is `aria-hidden`; the accessible progress is
  the sections' own headings.
- **Content merge.** The notches *are* the sections: their count
  and spacing are generated from the page's real section list,
  so the rail is a true map of this page, not a decoration
  shaped like one. A page with five sections has five notches.
- **Failure fallback.** No JS: the rail renders with the pebble
  at the source and all notches in place — a still map of the
  page. No `offset-path`: the transform fallback covers all
  modern engines; below that, the pebble rests at the source
  and the notches still print.
- **Reduced-motion variant.** The pebble does not roll; it steps
  — position updates discretely at section boundaries (notch to
  notch) with no rotation. The information (where am I, how far)
  is identical.
- **Performance budget & mobile variant.** One SVG path length
  measured once per resize; per frame, one transform write.
  Below 1200px the rail does not exist (§4) — progress on tablet
  and mobile is carried by the sections themselves and the
  footer's record; §9 names a squeezed-in mini-bar a failure,
  and the theme accepts the absence rather than fake the stone.
- **Choreography timeline (v2).** Page load: pebble at source,
  notches undropped → first scroll: fill wets over 400ms
  `--ease-soak` → each section boundary crossed: notch drops
  300ms `--ease-settle`, pebble rolls on → pool entry: rail
  fades to line-only across the descent's 35% → pool exit:
  pebble resurfaces at the mapped position, next notch armed →
  page bottom: pebble rests on the bank, all notches dropped.
- **State matrix (v2).** *Rest:* at source / at bank. *Hover:*
  none. *Focus:* rail is aria-hidden, no focus state. *Active:*
  n/a. *Scrolled-past:* all notches latched dropped; scrolling
  back up does not un-drop them (the reading happened; the
  record stands — the same ruling as §6.15's counters).
  *Disabled / no-JS:* still map. *Touch:* no rail below 1200px.
- **Breakpoints (v2).** ≥1200px: full rail. 768–1199px: absent.
  <768px: absent.
- **Edge cases & failure modes (v2).** *Very short page (fewer
  than three sections):* the rail is not rendered — a stream
  with two stones is a puddle, and §7 refuses the rail below
  three sections. *Sections added by a CMS:* notches are
  generated from the live DOM at load, so the map is true on
  the day it is served. *Resize:* path re-measured, pebble
  re-mapped by progress fraction, no jump in reading terms.
- **Accessibility spec (v2).** `aria-hidden="true"` on the whole
  rail: it duplicates information the headings already carry,
  and a rolling stone announced per frame would be cruelty.
  The sections' headings are the accessible progress. Colour:
  the pebble's `--pool` outline keeps it findable against
  `--dry` for low-vision visitors who use the rail visually.
- **Tokens consumed (v2).** `--wet`, `--pool`, `--grey`,
  `--pebble-chip`, `--ease-settle`, `--ease-soak`, `--lerp-page`
  (0.12).

### 6.6 Streamline flow line

- **What & why.** An SVG streamline draws itself around the hero
  pebbles over ~2s, splitting and rejoining around each card the
  way water splits around stones, and re-draws on resize. It
  belongs because it is the hero's proof: the line can only
  exist if the layout really is a streambed — it flows around
  the *actual* cards, wherever they have settled (§6.1), so a
  rearranged bed produces a different, still-true line.
- **Structure.** An absolutely-positioned inline SVG layered
  behind the hero cards (z-index below the bed, above the
  ground), `pointer-events: none`, `aria-hidden`. The path is
  computed at runtime: a smooth curve entering at the hero's
  upstream edge, flowing along the bed, and at each card,
  bifurcating into two sub-paths that pass either side of the
  card's bounding ellipse and rejoin downstream — implemented
  as one path per card-gap segment, each a cubic through
  authored waypoints derived from the cards' measured rects
  inflated by 14px (the water's clearance). Stroke: 1.5px
  `--algae` at 55% opacity, round caps — a pointed cap would be
  a cut edge (§1).
- **Motion spec.** Trigger: load, beginning t=+200ms after the
  bed settles (§6.1), drawing via `stroke-dashoffset` over
  2000ms `--ease-drift` — the draw speed is roughly constant in
  px/s (dash length normalised per segment) so the water flows
  evenly around big and small stones alike. Re-draw on resize:
  debounced 250ms, the old line fades over 300ms `--ease-soak`
  while the new one draws at 1200ms (a returning rite, quicker).
  The line does not loop and does not move after drawing: water
  that has shown you its path then holds still is a diagram of
  the current, not a screensaver.
- **States.** Undrawn (JS-armed only) → drawing → drawn (rest).
  Hover: none. Scrolled-past and back: drawn; the line is part
  of the hero's furniture once drawn. Return visit: drawn
  instantly (the session flag shared with §6.1).
- **Content merge.** The line's geometry *is* the hero's
  content geometry — remove the cards and the line has nothing
  to flow around and is not drawn (§7: a hero with fewer than
  three stones gets no streamline). It is the only element in
  the theme that is pure diagram, and it earns its place by
  being computed from the layout it diagrams.
- **Failure fallback.** Watchdog at 3000ms from load: if the
  draw has not completed, the line snaps to drawn. No JS: the
  line ships drawn in the DOM? — no: the path is computed from
  measured rects, which no-JS cannot do; the no-JS hero ships
  *without* the line, and §10 accepts this as the theme's one
  JS-born element, because the line asserts something about the
  layout that only the laid-out page can truthfully compute.
  The cards, copy and prices — the content — are all present
  without it.
- **Reduced-motion variant.** The line is printed complete at
  first paint (computed and set without the draw animation) —
  the information survives, the performance rests.
- **Performance budget & mobile variant.** Path computation is
  ≤6 cards × 2 segments, run on load and debounced resize only
  — zero per-frame cost beyond the draw's composited dash
  animation. Mobile (<768px): the bed is one column; the line
  flows down the column's left channel without bifurcations
  (stones in single file are flowed *past*, not around) and
  draws at 1400ms.
- **Choreography timeline (v2).** t=0 bed settles (§6.1) →
  t=+200ms draw begins at the upstream edge → segments draw in
  flow order, each split passing its stone and rejoining →
  t≤2200ms the line exits at the hero's downstream edge, complete
  → resize: old fades 300ms, new draws 1200ms from the same
  upstream start.
- **State matrix (v2).** *Rest:* drawn. *Hover:* none. *Focus:*
  focus entering the hero during the draw completes it
  instantly (same ruling as §6.1). *Active:* n/a.
  *Scrolled-past:* drawn. *Disabled / no-JS:* absent (see
  fallback). *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full bifurcation around every
  card. 768–1199px: bifurcation, clearance 10px. <768px: single
  channel, no bifurcation, 1400ms draw.
- **Edge cases & failure modes (v2).** *Cards reflow after
  fonts load:* the draw is gated on the same fonts race as
  §6.1 and positions are measured after it, so the line fits
  the final bed. *A card's image loads late and grows it:* hero
  cards have fixed pebble aspect ratios (§6.12), so rects do
  not move when images arrive. *Overlapping cards:* the bed's
  gaps are ≥28px by §4; if a CMS theme override collapses them,
  the clearance inflation is reduced to half the real gap —
  the line thins its detour rather than crossing a stone.
- **Accessibility spec (v2).** `aria-hidden`, `pointer-events:
  none`, behind the content: it can never cover text (it flows
  in the gaps, which is the point of it). No contrast obligation
  — it is a diagram line, and its `--algae` at 55% on `--dry`
  is a graphic, not information a visitor must read.
- **Tokens consumed (v2).** `--algae`, `--ease-drift`,
  `--ease-soak`, `--dur-streamline` (2000ms), `--dur-fallback-line`
  (3000ms).

### 6.7 Waterline reveals

- **What & why.** Each section's content is uncovered by a
  horizontal waterline rising from bottom to top as the section
  enters: below the line, content sits in its wet state (a
  `--wet` wash at 18% over the section ground and a 1px
  `--edge-wet` highlight riding at the line itself); above it,
  the content is lifted clear — dry, full contrast, at rest.
  It belongs because it is the theme's only reveal grammar:
  content is not *shown*, it is *lifted out of the river*, the
  way you'd lift a stone and watch the water sheet off it.
- **Structure.** Each section carries a `.waterline` overlay
  (absolutely positioned, `pointer-events: none`) whose height
  is written by the shared loop from the section's viewport
  progress: the line sits at the section's bottom edge when it
  enters and rises to its top as the section's first 60% of
  travel completes. The wet state below the line is a background
  wash on the overlay itself — the section's real content is
  never masked, clipped or opacity-reduced: it is *tinted*,
  fully legible at every frame (§1's law: no reveal may strand
  content, and a tint strands nothing). The 1px highlight is
  the overlay's top border in `--edge-wet`.
- **Motion spec.** Trigger: scroll into view. Rise duration is
  scrub-bound: the line's position is a pure function of scroll
  (loop lerp 0.12), traversing the section across its first 60%
  of viewport travel — roughly 800ms at reading scroll speed,
  which is where the original entry's ~800ms figure lives: it is
  an observed duration of the scrub, not a timer. Scrolling
  back up lowers the line again — a section can be re-immersed;
  only the §6.5 notches and §6.15 counters latch, never the
  water.
- **States.** Submerged (entering; wash over the lower part) →
  lifting (line mid-section) → lifted (line passed; section
  dry, wash gone, a faint `--edge-wet` residue line remains at
  the section's top edge for the rest of the visit — the tide
  mark, §1's wet audit made visible). Hover/focus: no effect on
  the line. Focus entering a still-submerged section lifts its
  line instantly to that element — keyboard visitors read dry
  copy.
- **Content merge.** The waterline acts on the section's own
  content in place; there is no separate reveal layer with its
  own content. The wash's tint is the section's ground colour
  shifted toward `--wet` — the section looks *wetter*, never
  *hidden*.
- **Failure fallback.** No JS: no overlay is inserted, every
  section is dry and complete — the overlay is JS-born and
  JS-owned. Watchdog: if the loop stalls for >1200ms mid-lift
  (long task, hidden tab), the line snaps to the position the
  scroll value demands; content was legible throughout
  regardless, because the wash never exceeds 18%.
- **Reduced-motion variant.** No line, no wash. Sections are
  simply present, dry. The tide-mark residue also rests absent
  — it is the record of a motion.
- **Performance budget & mobile variant.** One overlay per
  section, height writes only while the section is in the
  active set (≤4 per frame), composited. Mobile (<768px): the
  wash drops to 12% (smaller screens, stronger relative tint)
  and the line traverses across the first 50% of travel.
- **Choreography timeline (v2).** Section top enters viewport
  bottom → line at section bottom, wash below it → section
  travels: line rises proportionally, highlight riding at the
  line, content above it drying in place → section's 60% travel
  point: line exits the top, wash reaches 0 → tide mark prints
  at the top edge → section rests dry for the remainder of the
  visit (until scrolled fully out and back, when it may lift
  again).
- **State matrix (v2).** *Rest (lifted):* dry, tide mark at top.
  *Hover:* none. *Focus:* instant lift to the focused element.
  *Active:* n/a. *Scrolled-past:* dry; re-immersion possible on
  return. *Disabled / no-JS:* dry, no overlay. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: 18% wash, 60% travel.
  768–1199px: 15% wash, 55% travel. <768px: 12% wash, 50%
  travel.
- **Edge cases & failure modes (v2).** *Section taller than
  150vh:* the line traverses the first 100vh-worth of the
  section and exits; the rest of the section was never washed —
  a long listing is a series of shallow riffles, and §7 applies
  the waterline per sub-block (each card row its own line) past
  150vh. *Anchor jump into a section's middle:* the line snaps
  to the jumped position's value; no visitor is asked to watch
  a lift for content they deliberately jumped to. *Print:* the
  overlay and tide marks do not print.
- **Accessibility spec (v2).** Because the wash is a tint and
  never an opacity, contrast at the worst frame is bounded:
  `--pool` text over the 18% wash measures above 8.5:1
  (computed from the §2 pairings) — comfortably past AA at every
  moment of the reveal. The overlay is `aria-hidden` and
  pointer-transparent. Reduced motion removes it entirely.
- **Tokens consumed (v2).** `--wet`, `--edge-wet`, `--ease-lift`,
  `--lerp-page` (0.12).

### 6.8 Hover nudge

- **What & why.** Touching a stone moves it slightly in the
  current: hovering (or focusing) a pebble card nudges it 4px
  downstream and 1px down, where it settles with a soft damp —
  and it *stays* nudged until another card is hovered, when the
  first eases home. It belongs because it gives the bed a
  physics of contact: the cards are objects in water, not
  pictures of objects, and the current's direction is taught by
  the nudge's direction — always downstream, never toward the
  visitor, never up.
- **Structure.** A transform on the card (`translate(4px, 1px)`)
  driven by a per-card `--nudge` variable written by the shared
  loop toward 1 (hovered/focused card) or 0 (all others). Only
  one card in a bed may hold `--nudge: 1` at a time; the loop
  enforces the exclusivity, so moving the pointer across a bed
  produces a small travelling displacement, stone to stone. The
  nudge composes with §6.1's settle transform and §6.13's tilt
  on separate nested elements (settle on the card, nudge on its
  inner, tilt on the face) so the three motions never fight over
  one property.
- **Motion spec.** Trigger: pointerenter / focusin. In: 450ms
  `--ease-settle` (the damp is the easing's own). Out (when
  another card takes the nudge, or on blur): 600ms
  `--ease-drift` — returning home is slower than being pushed,
  because the current pushes and the bed resists. A card
  nudged by focus keeps its nudge until focus leaves the bed.
- **States.** Rest: home position. Nudged: +4px/+1px, and the
  card's ground shadow (a soft `--wet-deep` blur beneath it)
  shifts −1px upstream, as if the stone's bed-scour moved with
  it. Hover on a nudged card: held. Scrolled-past: home —
  scrolling a bed out of view resets all nudges.
- **Content merge.** The nudge moves the card itself — its
  photograph, title, price and link travel together. It is not
  a shadow trick or a highlight: the thing you are touching is
  the thing that moves.
- **Failure fallback.** No JS: no nudge; cards rest at home, and
  hover is conveyed by the link underline's thickening (§3) —
  the fallback is a typographic state, not an absence. If the
  loop is dead, a CSS-only `:hover` rule applies the same
  translate without the damp (a plainer physics, still true).
- **Reduced-motion variant.** No translation. The hovered card
  instead gains the `--edge-wet` 1px outline — it looks *wet*,
  not moved: the information (you are touching this stone) is
  carried by surface, not motion.
- **Performance budget & mobile variant.** One transform per
  card per frame at most, only during the 450/600ms transitions.
  Touch: there is no hover — the nudge fires on first tap for
  cards whose primary action is navigation, at half distance
  (2px), and the tap's navigation proceeds on the same press;
  the nudge never delays or intercepts a tap.
- **Choreography timeline (v2).** Pointer enters card A →
  `--nudge` targets: A→1 over 450ms `--ease-settle`, shadow
  shifts at the same beat → pointer moves to card B: A→0 over
  600ms `--ease-drift`, B→1 over 450ms — the two overlap, and
  for ~200ms the bed shows a small travelling wave → pointer
  leaves the bed: last card returns over 600ms → bed at rest.
- **State matrix (v2).** *Rest:* home. *Hover:* nudged (the one
  card). *Focus:* nudged, held until focus leaves the bed.
  *Active (pressed):* §6.9's ripple fires; the nudge holds.
  *Scrolled-past:* home. *Disabled card* (a sold-out offer,
  §6.13): no nudge — a stone that cannot be taken does not
  move for you; its state is carried by its copy. *Touch:*
  2px tap nudge, no exclusivity (each tap independent).
- **Breakpoints (v2).** ≥1200px: 4px/1px. 768–1199px: 3px/1px.
  <768px: tap-only, 2px/0px.
- **Edge cases & failure modes (v2).** *Pointer sweeping fast
  across a bed:* exclusivity is resolved per frame by the loop;
  cards passed over in <80ms never begin a nudge (an intent
  dwell threshold) — the bed ripples only for a deliberate
  touch. *Keyboard tabbing through a long listing:* each focus
  nudges in turn; the 600ms returns overlap behind the visitor
  like a wake — intended, and it settles within a second of the
  last tab. *Nudged card at the bed's edge:* the 4px is inside
  the basin's slack (§4), never causing overflow or a
  scrollbar flicker.
- **Accessibility spec (v2).** The nudge is never the only
  hover/focus signal: links keep their underline thickening and
  cards keep a visible focus ring (`--algae-deep`, 2px, offset
  3px, itself pebble-radiused on the card's recipe). Focus is
  never moved or trapped by the exclusivity rule. Touch targets
  are the whole cards, ≥64px in the short axis.
- **Tokens consumed (v2).** `--ease-settle`, `--ease-drift`,
  `--wet-deep`, `--edge-wet`, `--nudge`, `--dur-nudge` (450ms),
  `--dur-nudge-home` (600ms).

### 6.9 Click ripple

- **What & why.** Clicking a card disturbs its surface: two
  rings expand from the exact click point across the card's
  pebble face, fading over ~700ms — the river's own response to
  being touched. It belongs because feedback in this theme must
  come from the material, not from a UI convention: a stone in
  water answers a touch with a ripple, and a button that
  ripples has told you it felt you, in the theme's language.
- **Structure.** A ripple layer inside the card (absolutely
  positioned, clipped by the card's pebble radius,
  `pointer-events: none`, `aria-hidden`). On activation, JS
  spawns two ring elements at the click coordinates: ring 1 a
  2px border in `--algae` at 45% opacity scaling from 0 to the
  card's full diagonal; ring 2 the same at 25%, delayed 90ms,
  scaling to 78% of ring 1. Both are `border-radius:
  var(--pebble-card)` — the rings are pebble-shaped, not
  circular, because the surface they travel across is a stone,
  and a circular ripple on a pebble reads as a target, not
  water. Keyboard activation ripples from the card's centre.
- **Motion spec.** Trigger: click / tap / Enter / Space on the
  card's action. Duration 700ms `--ease-ripple`, opacity
  fading across the last 40%. The ripple never delays the
  action: navigation or state change proceeds on the same
  press; the ripple is a farewell on the surface left behind,
  or a confirmation on a card that stays (a favourite stone,
  §6.13).
- **States.** Rest: no rings. Rippling: two rings, ≤700ms.
  Rapid repeat clicks: each click spawns its own pair, capped
  at 3 live pairs per card (older pairs fade instantly) — a
  stone pelted with clicks still reads as one surface.
  Scrolled-past: rings complete or are culled with the card's
  layer; no residue.
- **Content merge.** The ripple travels across the card's real
  face — over its photograph's lower third and its ground, but
  the layer sits *below* the card's text (z-order: photograph,
  ripple, text) so copy is never under a moving ring. What is
  disturbed is the stone's surface; what you read stays still.
- **Failure fallback.** No JS: activation feedback is the
  button's native `:active` sink (1px, §5) and the action
  itself. A ripple that fails to spawn changes nothing — the
  click still worked; feedback is a courtesy, not a receipt.
- **Reduced-motion variant.** No expanding rings. The card's
  surface wets briefly instead: a `--wet` wash at 20% fading
  over 300ms from the activation point — contact recorded as
  wetness, per §1's audit.
- **Performance budget & mobile variant.** Two short-lived
  composited layers per click, removed at 700ms; no canvas.
  Mobile: identical — the ripple is the primary tap feedback on
  touch, where the §6.8 nudge is halved, so the rings carry
  more of the conversation and their opacity rises by 10
  points (55% / 35%).
- **Choreography timeline (v2).** t=0 activation → ring 1
  spawns at the point, 2px, 45% → t=90ms ring 2 spawns, 25% →
  t=0–700ms both scale along `--ease-ripple` → t=420ms opacity
  fade begins → t=700ms layers removed, card at rest (or the
  page has navigated, §6.16, and the ripple's last frames are
  the old page's farewell under the transition).
- **State matrix (v2).** *Rest:* clean surface. *Hover:* no
  ripple (§6.8 owns hover). *Focus:* no ripple until activated;
  keyboard activation ripples from centre. *Active:* ripple
  fires; the 1px sink composes under it. *Scrolled-past:* rings
  culled with the layer. *Disabled card:* no ripple — pressing
  a sold-out stone gets the §6.8 ruling: nothing moves, nothing
  rings; its copy explains. *Touch:* ripple at tap point,
  raised opacity.
- **Breakpoints (v2).** ≥1200px: rings to full diagonal.
  768–1199px: same. <768px: same geometry, opacity +10 points,
  ring border 2.5px (a thumb needs a clearer answer than a
  cursor).
- **Edge cases & failure modes (v2).** *Click near the card's
  edge:* rings are clipped by the pebble radius and simply
  travel less far visibly — true to a ripple reaching a bank.
  *Click on a child link vs the card body:* the ripple belongs
  to the activated element's card in both cases; nested
  actions (the §6.13 favourite button) ripple their own small
  pebble only, not the whole card — the disturbance matches the
  thing acted on. *Ripple during the §6.1 settle:* clicks are
  accepted once cards are settled; during the ≤1150ms ceremony
  the hero cards' actions are live but ripples wait for rest —
  you cannot disturb water that is still arriving.
- **Accessibility spec (v2).** The ripple is decorative
  feedback layered under text; it is never the sole signal of
  activation (the action's result — navigation, a state change,
  an `aria-pressed` flip — is). `aria-hidden`, no live-region
  announcement for the ripple itself. Ring contrast at peak:
  `--algae` 45% over `--dry` is a graphic, not text.
- **Tokens consumed (v2).** `--algae`, `--wet`, `--pebble-card`,
  `--ease-ripple`, `--dur-ripple` (700ms).

### 6.10 Wet-sheen band

- **What & why.** A soft diagonal band of light travels slowly
  down the whole page on a ~20s loop, momentarily giving matte
  surfaces a wet look as it passes — even the footer glistens
  when the band reaches it. It belongs because a streambed is
  never uniformly dry or wet: water keeps arriving. The band is
  the page's weather, and it is one of only two ambient loops
  the theme permits (§5), which is what keeps it feeling like
  weather rather than machinery.
- **Structure.** One fixed, full-viewport layer
  (`pointer-events: none`, `aria-hidden`, z-index above section
  grounds, below text-critical overlays) carrying a linear
  gradient in `--sheen` — a 22° diagonal band ~38vh tall with
  soft edges (transparent → 55% → transparent). The layer
  translates vertically from −45vh to +110vh and loops. The
  gradient can only lighten (§2: `--sheen` is `--dry` at 55%),
  so the band does not fake wetness with value — it reads as
  wet because of its second property: a 1px bright leading
  edge (the meniscus) drawn at the band's lower boundary, which
  catches each pebble's top curve as it passes, the way a
  waterline catches a stone. Light above, a bright waterline
  at the edge: the surface below the line reads as just-wetted,
  the way a real stone does when a wave has passed over it.
  Both effects are in the one layer.
- **Motion spec.** Trigger: time loop, 20,000ms per full pass,
  linear in distance (the current does not ease its weather),
  written by the shared loop as a scrub of page time so a
  backgrounded tab resumes mid-pass rather than restarting.
  The band pauses when the tab is hidden, when the page is
  inside the pool's deep beat (§6.4 — underwater, there is no
  surface weather), and under reduced motion. It never speeds
  up, never reverses, and its period is not configurable per
  page: 20s is the theme's weather, everywhere.
- **States.** Passing: surfaces lighten ≤6% in value and grow
  the meniscus line at their top curve. Rest (band elsewhere):
  surfaces are themselves. The band's crossing of a card does
  not wet it in the §1 audit's sense — wetness-by-weather is
  visual only and leaves no tide mark (§6.7 owns records).
- **Content merge.** The band acts on the page's real surfaces
  — cards, photographs, the footer — in place. It carries no
  content of its own and exists only as light on the content
  that exists. Remove every section and the band lights an
  empty bed, which is why §7 requires the band to be the last
  element added to a build (§15): weather is commissioned
  after there is a place for it to happen to.
- **Failure fallback.** No JS: no band; the page is a still,
  dry-lit bed — complete. If the layer fails to composite on a
  weak GPU, §14's budget cuts the band first (it is the theme's
  most expendable beauty) and the page loses weather, not
  meaning.
- **Reduced-motion variant.** Off. Surfaces rest in their own
  light. Nothing replaces it — stillness is the variant.
- **Performance budget & mobile variant.** One fixed layer,
  transform-only, the cheapest ambient loop in the library —
  but it repaints a wide gradient, so on devices reporting
  `save-data` or ≤4GB RAM (§14's probe) it ships disabled.
  Mobile (<768px): the band narrows to 30vh and the period
  stays 20s (weather does not hurry for a smaller sky).
- **Choreography timeline (v2).** t=0 band at −45vh → falls
  linearly → crosses the hero at ~t=3–6s of each pass → mid-page
  ~t=10s → footer ~t=17–19s → exits 110vh at t=20s → next pass
  begins immediately (the loop is continuous; the *noticeable*
  rhythm is one pass per 20s, the unnoticeable truth is that
  the band is always somewhere). Pool deep beat: band opacity
  fades to 0 across the descent's 35% and restores on shallowing.
- **State matrix (v2).** *Rest:* band somewhere on the page.
  *Hover:* no interaction. *Focus:* no interaction; the band
  never crosses a focused element's text at more than 6% value
  change, so focus readability is unaffected at every frame.
  *Active:* n/a. *Scrolled-past:* the band is viewport-fixed,
  so "past" does not apply — it lights whatever is being read.
  *Disabled / no-JS:* absent. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 38vh band, 22°. 768–1199px:
  34vh. <768px: 30vh, period unchanged.
- **Edge cases & failure modes (v2).** *Dark-scheme visitors:*
  the band's opacity drops to 0.35 (§2) so it reads as
  moonlight, not a searchlight. *The band crossing the pool:*
  at the pool's ground the lightening is invisible against
  `--pool` (the gradient lightens toward `--dry` at low alpha
  over a dark ground — a faint lift, acceptable) but the
  meniscus line is suppressed inside the pool entirely: there
  is no surface line underwater. *Long pages (>12 sections):*
  the band is viewport-relative, so its weather reaches the
  footer only when the visitor does — correct: it is light,
  not a page-length animation.
- **Accessibility spec (v2).** `aria-hidden`, pointer-none, and
  value change capped at 6% so no text pairing ever drops
  below its §2 measured contrast minus a twentieth — `--pool`
  on `--dry` stays above 9.3:1 at the band's brightest frame.
  Fully removed under reduced motion. Visitors with
  photosensitivity: the band is a slow luminance drift with no
  flash component (≤0.05Hz effective), inside every guideline's
  safe region.
- **Tokens consumed (v2).** `--sheen`, `--dry`, `--ease-soak`,
  `--dur-sheen` (20,000ms).

### 6.11 Streambed navigation

- **What & why.** The header is a row of stones on the bank: the
  lodge's name set in Bitter on a wide flat pebble
  (`--pebble-flat`), the navigation links as smaller pebbles in
  a loose cluster, and the booking action as the one algae-filled
  stone. It belongs because navigation in this theme cannot be a
  bar — a bar is a cut plank laid across the stream — it must be
  the first stones the visitor steps on, and like stepping
  stones, the current section's stone sits *wet* (the visitor is
  standing on it; §1's audit satisfied by presence).
- **Structure.** A `<header>` (not fixed by default; see states)
  containing: the nameplate pebble (link home), a `<nav>` of
  pebble links (`--pebble-chip` recipe, padding 12px 20px), and
  the booking stone (`--pebble-btn`, `--algae` ground, `--dry`
  text at 6.37:1's inverse — measured: `--dry` on `--algae`
  6.37:1). The current page's nav stone carries `--wet` ground
  and `aria-current="page"`. On scroll past 120vh the header
  re-arrives as a slim bank-line: a sticky strip in which the
  stones shrink to chips in a single row, sliding down over
  400ms `--ease-drift` — the bank follows you downstream, lower
  and quieter.
- **Motion spec.** Trigger: load (the header stones settle with
  a single shared 500ms `--ease-settle` — a smaller, faster
  cousin of §6.1, because furniture arrives before content) and
  scroll (the slim-line transformation at the 120vh threshold,
  with 90px of hysteresis so it cannot flutter at the boundary).
  Nav stone hover: the §6.8 nudge at half distance (2px) — the
  header's stones are smaller and so is their physics.
- **States.** Rest (top): full stones, nameplate prominent.
  Slim-line: chips in a row, nameplate reduced to the name in
  Bitter 600 17px on a chip. Current: wet stone. Hover/focus:
  2px nudge + underline thickening inside the stone. Scrolled
  back to top: full header restores over 400ms.
- **Content merge.** The nav stones are the site's real sections
  — Rooms, The River, The Pool, Find Us — in the page's own
  downstream order, so the header is also the table of contents
  of the streambed. There are no utility links in stones;
  account/legal links live in the footer (§6.17) as flat text.
- **Failure fallback.** No JS: the full header is simply present
  at the top; the slim-line never forms (it is an enhancement
  of abundance — the page is short enough at the top). The nav
  is a list of links in the DOM regardless.
- **Reduced-motion variant.** The header never transforms; it
  scrolls away and a plain sticky text line ("Stillwater Lodge
  — Rooms · The River · The Pool · Book") provides wayfinding
  without a single moving stone.
- **Performance budget & mobile variant.** The sticky strip is
  one composited layer, transform-only. Mobile (<768px): the
  stone cluster becomes a single "bank menu" pebble that opens
  the nav as a vertical fall of stones in an overlay panel —
  each panel link a full-width pebble, staggered 40ms
  `--ease-settle`, Esc closes, focus trapped politely and
  returned on close. The booking stone stays outside the menu,
  always visible: the one action is never buried.
- **Choreography timeline (v2).** t=0 header stones settle
  500ms → scroll: at 120vh the full header scrolls off, slim
  line slides in 400ms as the hero's bottom leaves → downstream:
  slim line rides, current stone updating as sections pass
  (§6.5's notch events drive it — one record, two printings) →
  scroll to top: slim line withdraws, full header restores.
- **State matrix (v2).** *Rest:* full or slim per scroll.
  *Hover:* 2px nudge. *Focus:* 2px nudge + `--algae-deep` ring.
  *Active:* 1px sink (§5). *Scrolled-past:* slim line.
  *Disabled link* (a section not yet open — e.g. bookings closed
  in winter): the stone rests dry, un-nudging, its label
  carrying the reason in words ("Book — opens March"), never
  greyed into illegibility. *Touch:* tap targets are the whole
  stones, ≥48px tall.
- **Breakpoints (v2).** ≥1200px: full stones + slim line +
  margin rail below. 768–1199px: full stones, slim line, no
  rail. <768px: bank-menu pebble + persistent booking stone.
- **Edge cases & failure modes (v2).** *Many sections (7+ nav
  stones):* the cluster wraps to two rows at the top (a wider
  bank) but the slim line scrolls its chips horizontally —
  §15's checklist caps authored nav at 6 stones; a seventh
  belongs in the footer. *Long section names:* stones size to
  content with a 22ch cap; beyond that the name is edited, not
  shrunk (§12: labels are short or they are wrong). *Sticky
  inside a transformed ancestor:* the same §6.4 checklist test
  covers the header.
- **Accessibility spec (v2).** Real `<nav>` with a list; current
  state is `aria-current`, not colour alone — the wet stone
  also carries a 2px `--algae-deep` underline. Focus ring:
  `--algae-deep` 2px offset 3px, following the stone's radius.
  Contrast: nav text `--pool` on `--dry` 9.86:1; on the wet
  stone, `--pool` on `--wet` 5.89:1 — still AA for the 14px+
  semibold labels. The mobile menu is a labelled dialog with
  focus return.
- **Tokens consumed (v2).** `--pebble-flat`, `--pebble-chip`,
  `--pebble-btn`, `--dry`, `--wet`, `--algae`, `--algae-deep`,
  `--pool`, `--ease-settle`, `--ease-drift`.

### 6.12 First-stone hero composition

- **What & why.** The hero is the streambed's first pool: the
  headline set in Bitter display with its letters rounding into
  place — each letter's final nudge displacing its neighbour by
  1px, like stones finding their seating — above the settled
  bed of §6.1, with the gauge chip (the river object's first
  printing: "64 cm at the lodge stone · flowing 1,180 L/s") on
  a chip pebble at the headline's downstream side, and the
  §6.6 streamline drawn around the bed below. It belongs as a
  single composed element because a River Stone hero is not a
  stack of parts; it is one arrangement of stones, water and
  words that must be specified as one seating or it will be
  built as three decorations.
- **Structure.** `<section class="hero">` containing: the
  eyebrow (the place name + season, caption style), the `<h1>`
  (full text in the DOM; per-letter spans are JS-generated
  clones for the seating animation only, `aria-hidden`, over
  the printed headline — the §3 type law's mechanism), the
  standfirst (≤28 words, §12), the gauge chip (a `--pebble-chip`
  stone, `--wet` ground, figures in Bitter tabular), the bed
  (§6.1's cards), and the streamline layer (§6.6). Layout: the
  headline occupies the upstream two-thirds; the chip rests at
  its right, slightly downstream (12px lower) — nothing in the
  hero is centred; a centred hero is a fountain, not a river.
- **Motion spec.** Trigger: load. Letters seat over 600ms
  `--ease-settle`, staggered 28ms per letter, each starting 6px
  upstream and 2px high, its landing nudging the next letter
  1px downstream for 200ms (a displacement wave that dies at
  the line's end). Cap: headlines over 24 characters seat as
  whole words instead (stagger 90ms per word) — a long sentence
  settles like gravel, not like single stones. The chip wets
  (§6.10's soak grammar, 900ms) as the last letter seats, as if
  the headline's arrival splashed it. Then §6.1's bed, then
  §6.6's line (§6.1's timeline owns the full sequence).
- **States.** Unseated (JS-armed only) → seating → seated
  (rest; the printed headline, clones removed). Hover: none —
  the headline is not a control. Scrolled-past and back:
  seated; the hero never re-performs.
- **Content merge.** Every part is content: the headline is the
  page's subject, the chip is the river's real state today,
  the bed is the offers. The composition's claim — *this place,
  this water, these rooms* — is the site's whole argument in
  one screen.
- **Failure fallback.** The DOM ships with the headline printed
  whole and the chip printed with today's figures as static
  text (the build's authored values; on a CMS build, the last
  saved gauge reading, labelled with its date — a stale figure
  with a date is honest, a stale figure without one is §9
  failure 9). Watchdog 1400ms completes any seating. No JS:
  the hero is complete at first paint.
- **Reduced-motion variant.** Headline printed, chip printed
  dry-then-wet instantly (its wet state is information: the
  river is up today), bed settled, streamline printed (§6.6).
- **Performance budget & mobile variant.** Letter clones exist
  for ≤1150ms and are removed; the hero's total animation cost
  is §6.1's + 24 transforms. Mobile (<768px): headline 32px,
  letters seat as words regardless of length (small screens,
  small ceremony), the chip moves below the standfirst — still
  downstream, never above the headline.
- **Choreography timeline (v2).** t=0 fonts race (§6.1) → t=0
  letters begin seating, 28ms stagger → displacement wave runs
  the line → last letter seats t≤600ms + wave decay 200ms →
  chip wets 900ms `--ease-soak` → bed settles (§6.1's timeline)
  → streamline draws (§6.6) → hero at rest, total ≤ ~3.4s of
  ceremony, all of it skippable by scrolling or focusing.
- **State matrix (v2).** *Rest:* printed and seated. *Hover:*
  none. *Focus:* focus anywhere in the hero completes all
  running ceremonies instantly. *Active:* n/a. *Scrolled-past:*
  complete. *Disabled / no-JS:* printed. *Touch:* first touch
  completes ceremonies.
- **Breakpoints (v2).** ≥1200px: 54px headline, chip beside.
  768–1199px: 42px, chip beside at 8px downstream. <768px: 32px,
  word-seating, chip below standfirst.
- **Edge cases & failure modes (v2).** *Headline with a
  two-letter first word:* the displacement wave still runs —
  nudges are relative, not cumulative, so no letter can be
  pushed off its printed position by more than its own 1px.
  *Right-to-left locales:* the seating runs in reading order
  (right to left), the wave travels reading-downstream; the
  chip sits at the reading-end side. §12 requires the headline
  be re-authored, not merely translated, for RTL — a river
  sentence is placed, not mirrored mechanically. *Gauge data
  unavailable at build:* the chip is omitted and the standfirst
  carries the river in words ("The river is up after the
  rain.") — an absent instrument is honest; a decorative one
  is not.
- **Accessibility spec (v2).** The `<h1>` is whole in the
  accessibility tree from first paint; letter clones are
  `aria-hidden` and removed after seating. The chip's figures
  are text, read as "64 centimetres at the lodge stone, flowing
  1,180 litres per second" (the accessible expansion is
  authored in §12's voice, not left to a screen reader's guess
  at "cm"). Contrast: headline `--pool` on `--dry` 9.86:1;
  chip text `--pool` on `--wet` 5.89:1 at 14px semibold — AA.
- **Tokens consumed (v2).** `--dry`, `--wet`, `--pool`,
  `--pebble-chip`, `--ease-settle`, `--ease-soak`,
  `--dur-seat` (600ms), `--dur-fallback-hero` (1400ms).

### 6.13 Pebble cards & the palm tilt

- **What & why.** The listing card — a room, an offer, a stone
  for sale — is a pebble with a photograph in a §6.3 mask, a
  Bitter title, two lines of fact, a price, and one action; and
  it tilts like a stone rolled in the palm: toward the pointer,
  soft and heavy, max 4°, as if being weighed. It belongs
  because the card is the theme's unit of commerce, and in this
  world you do not click a listing, you pick up a stone and turn
  it over. The tilt's heaviness is the point: 4° at 500ms is a
  stone; 12° at 150ms is a toy, and §9 fails it.
- **Structure.** `<article class="stone-card">` with the §6.3
  figure, an `<h3>` title, a fact list (sleeps / faces /
  from-price, or the merchant's equivalents), and a footer row:
  price (Bitter, tabular) + the action link. A favourite
  control — a small chip pebble ("Keep this stone") with
  `aria-pressed` — sits at the card's downstream corner. The
  tilt is applied to the card's face element (inside §6.8's
  nudge wrapper, inside §6.1's settle wrapper where applicable):
  three nested transforms, three owners, no conflicts. The
  card's ground shadow is a blurred `--wet-deep` ellipse beneath
  it that shifts opposite the tilt by 2px, selling the weight.
- **Motion spec.** Tilt: pointer-driven, written by the shared
  loop toward the pointer's position over the card, rotateX/Y
  capped at 4°, lerp 0.10 — deliberately the loop's slowest
  channel, because a stone in a palm does not snap to the hand.
  Release: returns to flat over 700ms `--ease-drift`. Entry:
  cards below the hero enter by §6.7's waterline and a 10px
  settle (a half-size §6.1) staggered 70ms per card in a row.
  Favourite press: the chip wets instantly (`--ease-soak`
  250ms) and the card gains a permanent tide-mark ring — a 1px
  `--edge-wet` outline inset 6px — for the session: a kept
  stone stays wet (§1's audit: it has been handled).
- **States.** Rest: flat, dry (or tide-marked if kept).
  Hover/focus: §6.8 nudge + tilt toward the pointer (focus
  tilts 2° toward the card's centre-top — a keyboard has no
  palm position, so focus gets a polite half-tilt). Active:
  §6.9 ripple on the action. Scrolled-past: flat. Sold-out /
  unavailable: the card rests dry and *unmoving* — no nudge, no
  tilt, no ripple (§6.8's ruling) — with its state in words on
  the fact line ("Taken for the whole of August"), its action
  replaced by a notify link. A stone you cannot have does not
  perform for you.
- **Content merge.** The card is the offer — photograph, facts,
  price, action — and every motion acts on that whole object.
  The tilt is not a frame around the content; it is the content
  being handled.
- **Failure fallback.** No JS: cards rest flat in their beds;
  the favourite chip is a working toggle button whose state is
  carried by its text ("Keep this stone" / "Kept ✓" — the tick
  is a word-substitute glyph inside the label, not an icon
  font). Images missing: the dry pebble with alt text (§6.3's
  ruling).
- **Reduced-motion variant.** No tilt, no settle; the nudge
  becomes the wet outline (§6.8). The kept-stone tide mark
  remains — it is a state, not a motion.
- **Performance budget & mobile variant.** Tilt layers exist
  only for cards in the viewport (≤6); the loop writes two
  rotation values + one shadow translation per live card.
  Mobile (<768px): no tilt (no palm, no pointer) — instead a
  card pressed-and-held for 300ms wets its surface (§6.9's
  reduced grammar at full size) as the touch equivalent of
  being picked up; tap proceeds normally on release.
- **Choreography timeline (v2).** Entry: waterline lifts (§6.7)
  → card settles 10px, 500ms `--ease-settle`, 70ms row stagger →
  rest. Hover: nudge 450ms (§6.8) + tilt lerps in at 0.10,
  reaching the pointer's angle in ~400ms → hold: tilt tracks
  the pointer with the stone's lag → leave: tilt returns 700ms,
  nudge returns 600ms, shadow settles → rest. Keep: chip wets
  250ms, tide ring fades in 400ms `--ease-soak`.
- **State matrix (v2).** *Rest:* flat, dry/kept. *Hover:*
  nudge + tilt ≤4°. *Focus:* nudge + 2° tilt. *Active:* ripple
  (§6.9) + 1px sink. *Scrolled-past:* flat. *Disabled
  (sold-out):* unmoving, state in words. *Touch:* no tilt;
  long-press wet; tap = action.
- **Breakpoints (v2).** ≥1200px: beds of 3, tilt 4°. 768–1199px:
  beds of 2, tilt 3.5°. <768px: single column, no tilt,
  long-press wet.
- **Edge cases & failure modes (v2).** *Cards of very different
  heights in a row:* the bed aligns stones by their tops (a
  streambed is read from the waterline down); tilt pivots at
  each card's own centre, so a tall stone and a short stone
  roll independently and truly. *Pointer leaving through the
  card's top edge mid-tilt:* the return is the same 700ms
  `--ease-drift` — no snap from any exit direction. *A card
  inside the pool:* tilt slows by the pool tempo (×1.8 return)
  and caps at 2° — deep water, heavy stones.
- **Accessibility spec (v2).** The whole card is not a link;
  the action link is a real link with the card's name in its
  text ("Book the Heron Room"), the favourite is a real button
  with `aria-pressed`. Focus ring on the action, `--algae-deep`
  2px. Tilt never moves the focus target more than the nudge's
  4px, and focus triggers the fixed 2° tilt so the target's
  position is predictable. Text contrast: facts `--algae` on
  `--dry` 6.37:1, price `--pool` 9.86:1.
- **Tokens consumed (v2).** `--pebble-card`, `--pebble-card-alt`,
  `--wet-deep`, `--edge-wet`, `--ease-settle`, `--ease-drift`,
  `--ease-soak`, `--tilt-max` (4deg).

### 6.14 The booking form — stones laid in a row

- **What & why.** The conversion form — booking enquiry, stone
  order, membership — is a row of smooth troughs: fields with
  `--pebble-field` radii and ruled bottoms like water-worn
  channels, labels in the keeper's voice, and a submit stone
  (`--pebble-btn`, `--algae` ground) labelled with the act in
  words ("Ask for these nights"). On success, the form does not
  show a tick: it shows a *confirmation stone* — a wide pebble
  carrying the booking's facts and a reference derived from the
  record — while a §6.9 ripple crosses it once, slowly, the
  stone dropped into the pool of the lodge's book. It belongs
  because conversion is the one place the theme must not become
  vague: the form is where the river's calm has to survive
  contact with dates, prices and errors.
- **Structure.** A real `<form>` with native validation
  supplemented (never replaced) by the theme's error grammar.
  Fields: text/email/date inputs and textareas with
  `--pebble-field` radius, `--dry` ground, a 1px `--grey`
  bottom rule that inks to `--algae-deep` 2px on focus over
  300ms `--ease-drift`. Nights/party choices are radio *stones*:
  a row of chip pebbles, the chosen one wet (`--wet` ground +
  tide ring), each a real `<input type="radio">` visually
  composed inside its label. The summary line above the submit
  stone is computed live from the fields ("3 nights · 2 guests
  · Heron Room — £412 in all") and is the form's reckoning:
  every figure in it traces to a field or to the room's printed
  price (§2's audit applied to money). Errors appear as a
  margin note in the keeper's voice beside the field (§12),
  with the field's rule turning `--algae-deep` and a dry-brush
  texture on the rule's last 12px — the one licensed dry mark
  (§1) placed where the content ran thin: the visitor's input.
- **Motion spec.** Focus rule-ink: 300ms. Radio stone wetting:
  250ms `--ease-soak`. Submit: the stone sinks 1px, holds a
  "Sending…" state only past 900ms (a fast success never shows
  a spinner — there is no spinner in this theme, §11), and on
  success the form crossfades over 500ms `--ease-soak` to the
  confirmation stone, across which one ripple pair (§6.9, at
  1.4× duration — a bigger stone, a slower ring) travels at
  t=+150ms. The confirmation's reference is derived, never
  invented: lodge initials + the arrival date's day-of-year +
  the party size (e.g. "SW-214-2") — a reference the keeper
  could recompute from the booking itself.
- **States.** Rest: dry fields, rules at rest. Focus: rule inks,
  label deepens to `--pool`. Filled: the field's ground wets
  very slightly (a 6% `--wet` wash — handled things are wet,
  §1). Error: margin note + dry rule-end, input preserved,
  focus moved to the first error on submit. Submitting: stone
  sunk, fields inert. Success: confirmation stone, form
  replaced (with a "Make another enquiry" text link beneath).
  Disabled submit: never pre-disabled — the form explains on
  submit rather than refusing in advance (§12's error voice
  needs the attempt to speak to).
- **Content merge.** The form's fields are the booking's facts;
  the summary's reckoning is computed from them; the
  confirmation repeats them back. Nothing decorative is added
  at the moment of conversion — the calmest page of the site is
  this one, by design (§13's map gives the form no ambient
  competition: the sheen band (§6.10) is the only loop allowed
  to cross it, and the morph (§6.3) on the form's one photograph
  rests while the form has focus).
- **Failure fallback.** No JS: the form is a working native
  form posting to its endpoint; errors are the server's,
  rendered in the same margin-note grammar. JS validation
  failure (script error): native validation still guards every
  field (`required`, `type`, `min` on dates). A submission that
  fails at the network shows the keeper's failure note (§12)
  with the visitor's input intact and a plain retry — the
  stone is never dropped silently.
- **Reduced-motion variant.** No ripple, no crossfade: the
  confirmation replaces the form instantly, with its facts and
  reference identical. Rule-inking is instant.
- **Performance budget & mobile variant.** The form's JS is the
  summary computation + validation, ≤6KB; the ripple reuses
  §6.9's layer code. Mobile (<768px): fields full-width, radio
  stones wrap as a small bed of 2–3 per row, the submit stone
  is full-width and 56px tall, and the summary line sticks
  above the keyboard's safe area as a plain `--dry` strip —
  the reckoning stays visible while typing, because a total
  you cannot see is a total you cannot trust.
- **Choreography timeline (v2).** Focus: rule inks 300ms →
  typing: summary recomputes per change (figures fade-amend
  200ms, never roll) → submit press: stone sinks, ripple pair
  on the stone itself → response <900ms: straight to success →
  t=success: form crossfades 500ms, confirmation stone settles
  8px `--ease-settle` → t=+150ms: the slow ripple crosses the
  confirmation → rest: the stone sits in the book, tide ring
  printed.
- **State matrix (v2).** *Rest:* dry, rules grey. *Hover*
  (submit stone): §6.8 nudge at 2px. *Focus:* rule inks, label
  deepens. *Active:* sink 1px. *Scrolled-past:* form state is
  preserved (a half-filled form scrolled past and returned to
  is exactly as left — the river does not tidy your stones).
  *Disabled:* the form is never wholesale disabled; individual
  unavailable radio stones (a full room) rest unwettable with
  their reason in the label. *Touch:* targets ≥48px; the radio
  stones are the targets.
- **Breakpoints (v2).** ≥1200px: two-column field pairs, margin
  notes in the right margin. 768–1199px: one column, notes
  beneath fields. <768px: one column, sticky summary strip,
  full-width submit.
- **Edge cases & failure modes (v2).** *Dates in the past /
  party of 30:* the keeper's notes name the fact and the fix
  ("Those nights have already flowed past — the calendar opens
  at tomorrow." / "The lodge sleeps twelve; for thirty, write
  to us and we will lay more stones.") — every error is
  authored in §12's voice, never a system string. *Price
  changes while the form is open:* the summary recomputes from
  the room's printed price at submit time and, if it changed,
  the confirmation restates the charged figure with a note —
  the reckoning is recomputed, never cached. *Double submit:*
  the stone inerts on first press; the reference derivation is
  idempotent for identical facts.
- **Accessibility spec (v2).** Labels are real `<label>`s;
  errors are `aria-describedby`-linked and announced via a
  polite live region that speaks the keeper's sentence, not a
  code. Focus order is field order; the error focus-move goes
  to the first error only on submit. Contrast: labels `--pool`
  on `--dry` 9.86:1; error notes `--algae-deep` on `--dry`
  8.67:1; radio stone chosen state is ground + ring + a
  "chosen" word in the accessible name — never colour alone.
- **Tokens consumed (v2).** `--pebble-field`, `--pebble-btn`,
  `--pebble-chip`, `--dry`, `--wet`, `--grey`, `--algae`,
  `--algae-deep`, `--pool`, `--ease-drift`, `--ease-soak`,
  `--ease-settle`, `--ease-ripple`.

### 6.15 River figures — the gauge record printed

- **What & why.** The figures band prints the river object's
  measurements — gauge height, flow, oldest stone, stones
  counted — as Bitter numerals that count up over 1400ms when
  the band first lifts clear of its waterline, each figure
  carrying its unit and its source line ("at the lodge stone",
  "from the 1911 survey"). It belongs because a river site
  earns trust by measurement, and this band is the theme's
  data made visible: counted the way a gauge is read, from the
  last reading — never from zero, because the river was flowing
  before you arrived.
- **Structure.** A `<section class="figures">` with 3–4 figure
  blocks in a loose bed. Each block: the numeral (Bitter 600
  30px, tabular), the unit, the label, and the source line in
  caption style. The values live once in a `<script
  type="application/json">` river object (§2) that also feeds
  §6.12's chip and §6.17's colophon — one record in the DOM,
  three renderings; server-rendered static values are the
  no-JS printing of the same record.
- **Motion spec.** Trigger: the band's waterline lift (§6.7)
  completing. Count: 1400ms `--ease-drift`, from 82% of value
  to value for heights and flows (a gauge approached, not a
  slot machine), from the *previous survey's* value for ages
  (11,400 counts from 10,900 — the 1911 figure, printed in the
  source line, so the count itself tells the survey's story).
  Figures never count down, never re-count on scroll-back, and
  a figure whose value is 0 is printed as a word ("dry" for a
  0 cm summer gauge) rather than animated to nothing.
- **States.** Uncounted (static printed values — the DOM state)
  → counting (1400ms) → counted (rest, latched for the visit).
  Hover: none. Focus: a figure block receiving focus before
  counting completes snaps to final — numbers are read, not
  watched.
- **Content merge.** The figures are the site's evidence: the
  lodge's river, measured. They sit between the pool and the
  booking form on a lodge page (§13) precisely so the visitor
  meets the river's facts after its story and before its
  prices.
- **Failure fallback.** No JS: the printed values stand — the
  count is a performance of numbers that already exist.
  Watchdog 1800ms snaps any counting figure to final.
- **Reduced-motion variant.** Values print at final instantly.
  The source lines — the actual information — are unchanged.
- **Performance budget & mobile variant.** Counting writes
  text content for ≤4 figures over 1400ms — trivially cheap;
  the band's cost is its waterline (§6.7). Mobile: figures
  stack 2×2, count duration 1100ms.
- **Choreography timeline (v2).** Band enters → waterline lifts
  (§6.7's timeline) → at lift completion: all four figures
  begin together (a gauge board is read at once, not staggered
  like a ceremony) → 1400ms `--ease-drift` → values land
  exactly on the record → source lines fade-amend in beneath
  (they were always there; the eye is simply released to them
  last) → rest, latched.
- **State matrix (v2).** *Rest:* printed values. *Hover:* none.
  *Focus:* snap to final. *Active:* n/a. *Scrolled-past:*
  counted, latched. *Disabled / no-JS:* printed values.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: one row of 4. 768–1199px: one
  row of 3–4 at 26px. <768px: 2×2 bed, 24px numerals.
- **Edge cases & failure modes (v2).** *A figure the client
  cannot source:* it is not printed (§2's audit); the band
  runs with three figures and wider water between them — an
  honest gap, never a padded one. *Live gauge feeds:* out of
  scope for the theme's static record; a site with a real feed
  updates the record server-side per page load and labels the
  reading with its hour ("at 06:00 today") — the count then
  runs from the previous load's value if known, else prints.
  *Very large ages:* formatted with the thin-space thousands
  separator of the locale, in Bitter tabular — never rounded:
  11,400, not "11k" (§12's banned forms).
- **Accessibility spec (v2).** Figures are text with their
  units and sources in the same block; during counting, the
  accessible value is the *final* value (the counting span is
  `aria-hidden`, a visually-hidden sibling carries the true
  figure from first paint — a screen reader is never made to
  listen to a gauge being approached). Contrast: numerals
  `--pool` on `--dry` 9.86:1; source lines `--algae` 6.37:1.
- **Tokens consumed (v2).** `--pool`, `--algae`, `--dry`,
  `--ease-drift`, `--dur-count` (1400ms).

### 6.16 Dry skeleton & the current-carry transition

- **What & why.** Loading is a dry pebble that wets: skeleton
  stones in the exact pebble shapes of the content they stand
  for, resting `--dry` with a `--grey` hairline, darkening
  toward `--wet` as their content arrives — a stone is dry
  until the river reaches it, and the darkening *is* the
  progress, per-part, never a global percentage. Page
  transitions ride the current: the old page drifts 24px
  downstream and wets slightly as it leaves; the new page
  drifts in from 24px upstream, drying into place. It belongs
  because waiting and leaving are the two moments themes
  usually abandon to spinners and cuts; here both stay in the
  river.
- **Structure.** Skeleton: for each content region, a
  `.stone-skeleton` block replicating the region's layout in
  pebble shapes (title stone, line stones at 92%/78%/85%
  widths — never uniform bars; uniformity is a cut edge made of
  lengths), each with `aria-hidden` and the region marked
  `aria-busy="true"` until its content lands. Wetting is a
  background crossfade `--dry` → `--wet` over 600ms
  `--ease-soak` triggered per region when its data resolves,
  followed within 100ms by the content's own §6.7-style lift at
  half height. Transition: a client-side navigation layer (for
  multi-page builds, a view-transition with the theme's
  keyframes; the spec is written for the behaviour, not the
  API) — out: 550ms `--ease-drift`, translateX(+24px) + a 10%
  `--wet` wash rising; in: 650ms, from translateX(−24px),
  drying (wash falling) + the new hero's stones pre-settled
  (transitions never replay §6.1).
- **Motion spec.** Skeleton wet: per region, on resolve, 600ms.
  A region unresolved at 4000ms stops wetting at 60% and prints
  the keeper's slow note inside its largest stone ("The river
  is slow today — this part is still coming.") with a retry
  action at 8000ms. Transition timings above; total ≤1200ms,
  and any navigation input during it is honoured immediately
  (the current does not queue the visitor).
- **States.** Skeleton: dry → wetting → content. Transition:
  resting page → carried out → carried in → resting. Hover/
  focus during transition: the incoming page accepts focus as
  soon as its DOM lands (t=in-start), not at the animation's
  end.
- **Content merge.** The skeleton's shapes are the content's
  shapes — a visitor learns the page's layout from its dry
  stones, and the wetting order is the data's real arrival
  order, so the loading state is a truthful preview, not a
  generic shimmer. The transition carries the actual pages.
- **Failure fallback.** If a region's data fails: the skeleton
  stone dries back to `--dry` and carries the failure note and
  retry (§12's voice) — a dry stone with words on it, never an
  error box with corners. If transitions are unsupported: a
  plain navigation, instant — the theme loses its farewell, not
  its wayfinding. A hard 4s cap: no skeleton may outlive 4000ms
  without printing its slow note.
- **Reduced-motion variant.** Skeletons still wet (colour is
  the information) but transitions are cuts: no drift, no wash
  — the new page is simply there, its stones settled.
- **Performance budget & mobile variant.** Skeleton stones are
  pure CSS shapes — zero image weight, zero JS until data
  lands. Transition layers are the two page roots only.
  Mobile: drift halves to 12px each way; the wet wash in
  transitions drops to 6% (small screens, strong tints).
- **Choreography timeline (v2).** Load: regions print dry
  stones → each resolve: that region wets 600ms → +100ms its
  content lifts → all regions landed: `aria-busy` clears, the
  page is read as arrived. Navigation click: ripple (§6.9) on
  the link's stone → out-drift 550ms, wash rising → DOM swap →
  in-drift 650ms from upstream, wash falling → new page at
  rest, focus at its headline.
- **State matrix (v2).** *Rest:* content, dry. *Hover:* n/a on
  skeletons. *Focus:* incoming page focusable from in-start.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled / failed:*
  dried-back stone with note + retry. *Touch:* identical;
  swipe-back gestures (browser-native) bypass the transition
  entirely — the visitor's own current wins.
- **Breakpoints (v2).** ≥1200px: 24px drifts. 768–1199px: 18px.
  <768px: 12px, wash 6%.
- **Edge cases & failure modes (v2).** *Partial failure (one
  region of five):* the page completes around the dry stone;
  the failed region never blocks the others, and its retry
  re-wets only itself. *Very fast loads (<150ms):* skeletons
  never flash — regions that resolve before first paint simply
  print content; the wetting ceremony has a 150ms minimum-data
  threshold below which it does not perform. *Back/forward
  cache:* a restored page shows its content, not its skeleton —
  the stones remember being wet within the session.
- **Accessibility spec (v2).** `aria-busy` per region and a
  single polite announcement when the page completes ("The
  page has arrived.") — never per-region chatter. Skeleton
  stones are `aria-hidden`. The slow/failure notes are real
  text with a real retry button (≥48px). Transition focus
  management: focus moves to the new page's `<h1>` at in-start,
  and the browser's scroll restoration is respected, not
  overridden.
- **Tokens consumed (v2).** `--dry`, `--wet`, `--grey`,
  `--pebble-card`, `--pebble-flat`, `--ease-soak`,
  `--ease-drift`, `--dur-wet` (600ms).

### 6.17 The bank footer — the record, third printing

- **What & why.** The footer is the bank at the page's end: a
  `--pool` ground on which the day's stones rest — the river
  record printed for the third time (level, flow, oldest stone,
  agreeing with §6.12 and §6.15 to the digit), the site's links
  as flat text in two columns, and the colophon line the
  original entry promised: *"No sharp corner exists anywhere on
  this page — not even here."* It belongs because a footer is
  where themes usually stop designing; this one is where the
  theme's law is signed. The record's presence makes the footer
  a document, not a dumping ground.
- **Structure.** `<footer>` on `--pool`, entered across the
  pool section's shallowing (§6.4) or directly from the bed.
  Inside: a row of three flat pebble stones (`--pebble-flat`)
  carrying the record's three headline figures in `--dry`
  Bitter; the link columns (`--wet` text on `--pool`, 5.89:1);
  the keeper's line (name, place, the river's name); and the
  colophon in `--wet`, small, last. The §6.10 sheen band
  glistens across the footer as it passes — the original
  entry's detail, kept: even the footer gets wet.
- **Motion spec.** The footer itself has one motion: its three
  record stones settle 8px `--ease-settle` staggered 80ms as
  the footer first enters — the last stones of the page finding
  their rest. The figures do not re-count (they were counted in
  §6.15; the footer *prints* them — a record does not re-measure
  itself). Everything else in the footer is still, permanently:
  the bank is where motion ends.
- **States.** Rest: printed, settled. Hover: links underline-
  thicken (§3); the record stones do not nudge — the record is
  not a toy. Scrolled-past: n/a (it is the end).
- **Content merge.** The footer's figures are the river
  object's third printing from the same DOM record (§6.15) —
  they cannot disagree with the hero because they are the same
  nodes' values re-rendered, and §10's gate diffs all three
  printings in the built page.
- **Failure fallback.** No JS: the footer prints complete with
  its figures as static text (the record's server rendering).
  Nothing in the footer is JS-born.
- **Reduced-motion variant.** The record stones print settled.
  All else identical.
- **Performance budget & mobile variant.** Negligible: three
  transforms once. Mobile: the record stones stack vertically,
  link columns stack, the colophon remains last and verbatim.
- **Choreography timeline (v2).** Footer enters → stones settle
  8px, 80ms stagger, ≤500ms total → sheen passes on its own
  20s weather (§6.10) → the page ends. There is no beat after
  the colophon; §13's map closes here.
- **State matrix (v2).** *Rest:* printed. *Hover:* link
  underlines only. *Focus:* `--dry` 2px ring on `--pool`
  (9.86:1 ground pairing). *Active:* 1px sink on links' stones
  — none; footer links are text, they do not sink. *Scrolled-
  past:* n/a. *Disabled / no-JS:* printed. *Touch:* link
  targets ≥44px tall via padding.
- **Breakpoints (v2).** ≥1200px: three stones in a row, two
  link columns. 768–1199px: stones in a row, columns stacked
  beneath. <768px: all stacked.
- **Edge cases & failure modes (v2).** *Record values changed
  between printings (a live-ish build):* forbidden by §6.15's
  ruling — one record per page load; a footer disagreeing with
  its hero is gate failure 4, and the build diffs them.
  *Very long link lists:* the footer caps at two columns of
  seven; the eighth link belongs in the page, not the bank.
- **Accessibility spec (v2).** Footer landmarks and headings
  are real (`<footer>`, visually-hidden "The bank" heading).
  Contrast: `--dry` on `--pool` 9.86:1; `--wet` on `--pool`
  5.89:1 for links and colophon at ≥14px. The colophon line is
  plain text, findable and copyable — it is a claim the visitor
  is invited to check (§10 turns it into the audit).
- **Tokens consumed (v2).** `--pool`, `--dry`, `--wet`,
  `--pebble-flat`, `--ease-settle`.

### 6.18 The stranded stone — the 404

- **What & why.** The not-found page is a single stone stranded
  above the waterline: one large dry pebble, alone on the bed,
  carrying the plain fact ("This page is not in the river."),
  the sought path printed on the stone as a keeper would chalk
  it, and two real ways back — the nearest sections as stepping
  stones. It belongs because an error page is where a theme's
  honesty is tested: this one admits the stone is dry, says
  what was looked for, and offers the actual nearest water —
  never a search box dressed as help, never a joke at the
  visitor's expense.
- **Structure.** A single centred basin: the stranded stone
  (`--pebble-hero`, dry, a `--grey` hairline, and — the one
  licensed imperfection — a faint dry-grass shadow at its base
  rendered as a soft `--wet` blur at 20%: the mark of where
  water used to be), the fact in Bitter 34px, the sought path
  in the keeper's voice ("You asked for /the-old-bridge — the
  river moved it in the spring." — the reason is authored per
  site, and if no reason is known, the line is simply "You
  asked for /that-path."), and two or three stepping-stone
  links (`--pebble-chip`) to the nearest real sections, chosen
  by the server from the path's first segment.
- **Motion spec.** The stranded stone does not settle — it was
  already here when the water left; that stillness is the
  design. One motion exists: on arrival, a single §6.6-style
  streamline approaches the stone from upstream over 1600ms
  `--ease-drift` and *stops* 24px short of it, its end fading —
  the current that no longer reaches. It draws once, never
  loops. The stepping stones behave per §6.11 (nudge, ring).
- **States.** Rest: stranded, still. Hover (stepping stones):
  per §6.11. There is no other state; an error page with a
  loading state has failed twice.
- **Content merge.** The stone carries the fact and the path —
  the error's actual information — and the stepping stones are
  the site's real nearest sections. Nothing else is on the
  page, because nothing else is true of the situation.
- **Failure fallback.** The 404 is a static page by
  construction: no JS is required for anything on it except the
  streamline's draw, whose absence leaves the page complete.
  It must be servable as a plain error document by the host
  with zero application boot — §15's checklist tests it with
  the app down.
- **Reduced-motion variant.** The streamline prints stopped
  short of the stone (its final state) without drawing.
- **Performance budget & mobile variant.** The lightest page
  on the site: ≤40KB total, no loop running except the shared
  one idling. Mobile: the stone scales to the basin, the
  stepping stones stack.
- **Choreography timeline (v2).** t=0 the page is complete and
  readable (the stone, the fact, the path, the ways back) →
  t=+300ms the streamline begins upstream → 1600ms: it stops
  24px short, end fading → stillness. Total ceremony 1.9s,
  none of it gating content.
- **State matrix (v2).** *Rest:* stranded. *Hover:* stepping
  stones only. *Focus:* stepping stones get the ring; the
  stone itself is not focusable. *Active:* n/a. *Scrolled-
  past:* n/a (the page is one basin tall). *Disabled / no-JS:*
  complete. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: stone at 480px wide.
  768–1199px: 400px. <768px: basin-width stone, fact at 28px.
- **Edge cases & failure modes (v2).** *A sought path with no
  near section:* the stepping stones fall back to Home and the
  site's one conversion page — always real, never guessed
  slugs. *Attack-shaped paths (long, encoded):* the path is
  printed truncated at 60 characters with the keeper's line
  shortened accordingly; the page never reflects markup (the
  path is text, escaped, always). *The visitor arrived from
  the site's own broken link:* the colophon of the 404 carries
  a "Tell the keeper" mailto with the path prefilled — the
  theme turns its own failure into a report, not a shrug.
- **Accessibility spec (v2).** The fact is the `<h1>`; the
  response is a real 404 status. Contrast: fact `--pool` on
  the stone's `--dry` 9.86:1; the path line `--algae` 6.37:1.
  Stepping stones are links with real names ("Back to the
  rooms"), ≥48px targets.
- **Tokens consumed (v2).** `--pebble-hero`, `--pebble-chip`,
  `--dry`, `--wet`, `--grey`, `--pool`, `--algae`,
  `--ease-drift`.

## 7. Page application map

- **Home.** The full river in one pass: hero composition
  (§6.12) with bed (§6.1) and streamline (§6.6); a listing reach
  (§6.13); the deep pool (§6.4) holding the story; figures
  (§6.15); one conversion reach (the booking form, §6.14, or a
  single stone-button to it); the bank footer (§6.17). Order
  is law: story (pool) before figures, figures before prices —
  a home page that opens with the form has dammed the river.
- **Listing (rooms / stones / offers).** Header (§6.11), a
  filter row of radio stones (the §6.14 grammar reused — one
  component language for choosing), beds of §6.13 cards entered
  by per-row waterlines (§6.7), pagination as stepping stones
  ("Further downstream →") — never numbered squares; numbers
  may appear as text inside a stone. No pool on a listing page:
  commerce stays in the shallows.
- **Detail (one room / one stone).** A single large pebble-mask
  photograph (§6.3, half-amplitude morph), facts as a stone
  ledger (§11's table treatment), the price and the booking
  form (§6.14) in the same reach — a detail page is one deep
  stone, not a scroll of sections; drift (§6.2) rests at 0
  throughout (short pages do not travel).
- **About / the river itself.** The pool (§6.4) is the page:
  the story at full depth, figures (§6.15) as its shallows at
  the end, no form. This is the one page type where a second
  shallow pool-toned section is licensed (a tributary, §6.4's
  static fallback form) — still never a second pin.
- **Contact / find us.** The form (§6.14) with the enquiry
  fields, the map replaced by a drawn streambed diagram (the
  §6.6 streamline grammar showing the road, the bridge, the
  lodge stone) — a map with corners would break §1; the
  diagram is the honest instrument. Directions are a numbered
  list of stones ("1 — cross at the mill bridge").
- **Checkout / booking confirmation.** The §6.14 form's success
  state as a full page: the confirmation stone large, the
  reckoning printed in full, one calm next action. No upsell
  stones in the confirmation reach — the river does not sell at
  the moment of trust.
- **404.** §6.18, verbatim, for every missing path.

## 8. Worked examples

### 8.1 The hero — Stillwater Lodge, first screen

The site is Stillwater Lodge, six rooms on a chalk stream. The
visitor arrives. t=0: the page is already complete in the DOM —
headline printed ("The river was here first. We built
quietly around it."), the gauge chip printed with this
morning's record, six room stones in their bed. Fonts win the
600ms race. The headline's letters seat: 600ms, 28ms stagger,
the displacement wave running the line and dying at the full
stop; the chip wets over 900ms as the last letter lands — the
river is up today, and the chip's wetness is how the page says
so before a word of body copy. The bed settles: Heron Room
first (upstream, left), 700ms `--ease-settle`, then Kingfisher,
Otter, Withy, Sedge, Millrace, 90ms apart, each landing nudging
its neighbour 1–2px; the last lands at ~1150ms. At +200ms the
streamline begins upstream and spends 2s flowing around the six
settled stones, splitting at Heron's ellipse, rejoining below
Millrace, exiting downstream. By t≈3.4s the first screen is at
rest: a bed of priced, bookable rooms, a true line of water
around them, the river's height in figures at the headline's
side. The visitor has not scrolled and already knows the place,
the water and the offers. Scroll timeline: at the first scroll,
the hero's drift (§6.2) begins its sine; the streamline, drawn,
scrolls with its stones (it is in the hero's layer, not fixed);
the margin pebble (§6.5) wets and starts its roll.

### 8.2 Mid-page — the deep pool, the lodge's story

Halfway down the home page, the bed shallows out into the pool.
The section's top reaches the viewport top; the sticky engages.
Across the first 35% of the pin, `--depth` runs 0→1: the ground
deepens `--dry` → `--pool` → `--pool-deep`; the story's tempo
stretches — the pool photograph's morph slows from 12s to
21.6s; the drift dies to half a pixel; the margin rail fades to
its line alone, the pebble gone under. The copy is the lodge's
story in Bitter's italic (§3's one licensed use — the river
speaking): the 1911 survey, the flood of '68 that took the old
bridge and left the bed's oldest stones counted, why the rooms
are named for birds. 380 words at 52ch: at reading pace the
deep beat (35–75% of the pin) holds the visitor in the dark for
roughly the length of the reading, neither hurrying nor
trapping — scroll is never locked, only weighted. The pool's
figures print inside the deep: depth 2.3 m, oldest stone 11,400
years — the record's second printing, matching the hero chip's
family of numbers. At 75% the section unpins; the ground
settles to `--pool` and stays dark into the footer, so the
page's last movement — figures, form, bank — happens at dusk
light, downstream of the deep.

### 8.3 Conversion — booking the Heron Room

Below the figures band, the booking reach: a photograph stone
of the Heron Room at rest (its morph paused — the form has the
visitor's hands now), and the form. The visitor chooses nights
on radio stones — "Fri 12 – Sun 14" wets as chosen; guests "2"
wets; the summary line recomputes per touch: "2 nights · 2
guests · Heron Room — £284 in all", the £284 traced to the
room's printed £142 on its §6.13 card, the multiplication shown
in the line itself ("2 × £142"). An email typed without its @
earns the keeper's note — "That direction won't reach anyone —
the @ is missing, looks like." — beside the field, its rule's
end gone dry-brushed, input intact, focus unmoved while typing
(the note arrives on blur/submit, never mid-word). Submit: the
stone sinks, no spinner; the answer returns in 600ms; the form
crossfades to the confirmation stone: the nights, the guests,
the £284 restated, and the reference "SW-196-2" — day-of-year
196 for 14 July, party of 2, recomputed by the keeper from the
booking alone — while one slow ripple crosses the stone, the
drop into the lodge's book. Beneath, one text link: "Make
another enquiry." Nothing else is asked. The conversion section
contains no other motion: the sheen band may pass, the stones
do not perform, the calm is the close.

## 9. Anti-slop — what makes THIS theme look cheap

1. **A square corner anywhere.** One 4px radius on a cookie
   banner, one right-angled icon, one rectangular ad slot — the
   law (§1) is binary and the eye finds the single cut edge in
   a field of worn ones instantly. *Cure:* the corner audit
   (§10, gate 1) runs on the built page, not the design file.
2. **Uniform blob radii.** Every card with the same recipe at
   the same rotation reads as a UI kit wearing a costume.
   *Cure:* the eight recipes (§4) alternate and mirror per
   nth-child; two neighbouring stones sharing a silhouette is
   a review failure.
3. **The crowded bed.** Ten hero cards, gaps squeezed to 8px:
   a dried-out gravel tray. *Cure:* six stones maximum in the
   hero bed (§6.1), gaps 28–44px of water, density falling
   downstream (§4).
4. **Decorative wetness.** Stones pre-darkened "for texture"
   that no current has touched — wetness as wallpaper breaks
   the audit and the fiction at once. *Cure:* §1's wet audit;
   a stone is dark because something happened to it.
5. **Snappy stones.** Settles at 200ms, tilts at 12°, ripples
   that splash — the theme's whole claim is weight and time.
   *Cure:* the durations ledger (§5) is closed; any value not
   in it fails review.
6. **A progress bar.** A filling rectangle is the anti-pebble:
   cut, linear, impatient. *Cure:* §6.5's rolling stone or
   nothing (below 1200px, nothing — accepted, not faked).
7. **Fade-in-from-nothing reveals.** Content materialising with
   opacity teaches the visitor that things appear; this theme
   teaches that things are *lifted out*. *Cure:* §6.7's
   waterline is the only reveal grammar; a generic fade class
   in the build is a defect, not a shortcut.
8. **Blue water.** Slipping toward cyan/blue "for freshness"
   betrays the palette: this river runs grey-green over stone.
   *Cure:* the closed token list (§2); an undeclared colour
   fails the build.
9. **Invented figures.** "Hundreds of happy guests", a gauge
   reading nobody took, an age rounded to "ancient".
   *Cure:* §2's river object and gate 4 — every figure traces
   to the record, and the footer diff proves the printings
   agree.
10. **A second pool.** Two pinned dark sections and the page
    has two deepest places, which is none. *Cure:* §6.4's
    refusal; tributaries are static (§7).
11. **Blur used as water.** A blurred photograph "to suggest
    the underwater" is out-of-focus stock with a story told
    about it. *Cure:* §5 refuses blur; underwater is rendered
    by the wet tokens and tempo, never by focus.
12. **The tilt as toy.** Magnetic, springy, pointer-chasing
    cards imported from a fintech landing page. *Cure:*
    §6.13's cap — 4°, lerp 0.10, 700ms return; a stone is
    weighed, not waved.

## 10. Quality gate

Blocking unless marked otherwise. The gate is signed by someone
other than the builder (§15).

1. **Corner audit.** Automated pass over the built page: every
   visible container's computed `border-radius` matches a §4
   recipe; no value 0, no value <14px on any axis of any
   element >44px. Includes the cookie notice, the menu overlay,
   the scrollbar thumb where stylable, and SVG icon strokes
   (round caps/joins only).
2. **Wet audit.** Every element rendered darker than `--dry`
   at rest can name its wetting event (scroll lift, hover,
   keep, weather excluded). A pre-wet decorative stone fails.
3. **No-strand test.** JS disabled, and separately JS killed
   mid-ceremony at 300ms: the page is complete and readable in
   both; every watchdog (§6.1 1600ms, §6.6 3000ms, §6.15
   1800ms, §6.16 4000ms) verified by throttled run.
4. **Three-printings agreement.** The river record's figures in
   §6.12's chip, §6.15's band and §6.17's footer are diffed in
   the built DOM: identical values, identical units. Any figure
   on the page not traceable to the record fails with it.
5. **Ambient census.** Exactly two ambient loops (§6.3, §6.10),
   both paused off-screen and under reduced motion; exactly one
   pin (§6.4). Counted in the build, not remembered.
6. **Tempo audit.** Every duration in the shipped CSS/JS
   appears in §5's ledger; the pool's ×1.8 (×1.5 mobile)
   verified by measuring one in-pool morph cycle.
7. **Reduced-motion completeness.** With `prefers-reduced-
   motion`: no drift, no morph, no roll, no tilt, no transition
   drift — and every state (wet chip, kept stone, counted
   figures, confirmation) still reachable and identical in
   information.
8. **Contrast spot-check.** The five §2 measured pairings
   re-measured on the built page, including text over the
   §6.7 wash at its worst frame (≥8.5:1) and the wet stone's
   `--pool` on `--wet` (5.89:1).
9. **Form-keeping rehearsal** (non-blocking but recorded): an
   error submit, a network-failed submit and a double submit
   each preserve input and speak in §12's voice; the reference
   derivation recomputes by hand.
10. **The still-photograph test** (non-blocking): screenshots
    at rest at five scroll positions show an aligned, calm,
    corner-free page — if any still looks "animated", a motion
    has failed to rest.

## 11. Component inventory

Every component a real site in this theme needs, with its
treatment. Refusals name their replacement; a refused component
found in a build is a gate failure (§10).

- **Primary button.** The algae stone: `--pebble-btn`, `--algae`
  ground, `--dry` label (6.37:1), 1px sink on active, §6.8
  nudge at 2px on hover. One per reach.
- **Secondary button.** A dry stone: `--dry` ground, `--pool`
  1px outline following the recipe, `--pool` label. Never a
  ghost button (a ghost is a stone that isn't there).
- **Text link.** §3's waterline underline; thickens on hover;
  visited links wet slightly (`--algae` → `--algae-deep`) —
  you have been down this channel before.
- **Navigation.** §6.11's stone cluster + slim bank-line.
- **Breadcrumb.** Refused. A river has no breadcrumbs; the
  way back is upstream, and the header's wet stone (§6.11)
  already says where you stand. Replacement: the current nav
  stone + the page's own H1.
- **Card.** §6.13's stone card. No other card exists.
- **Badge / tag.** A chip pebble (`--pebble-chip`), `--wet`
  ground, `--pool` text 5.89:1, worn only for facts ("Sleeps
  4", "River side") — never for marketing ("New!", "Hot!").
  §12 bans the words before §11 has to ban the badge.
- **Price.** Bitter tabular, `--pool`, always with its basis
  ("£142 a night", "£38 a tonne") — a bare price is a figure
  without a source (§3 law 3).
- **Form fields.** §6.14's troughs: label, `--pebble-field`
  input, keeper's margin note for errors.
- **Radio / checkbox.** Radio stones (§6.14). Checkboxes are
  small square-free toggles: a chip pebble that wets when on,
  with the state word ("On"/"Off") inside — never a tick in a
  box, the box has corners.
- **Select.** Refused as a native dropdown (its popup is a
  rectangle the theme cannot reach). Replacement: radio stones
  for ≤6 options; for longer lists, a "stone ledger" page
  section with the options as rows — the choice is made in the
  page, in the theme.
- **Tabs.** Refused. Tabs are a cut deck of cards. Replacement:
  downstream sections with §6.11 stone anchors — the page is
  the navigation.
- **Accordion.** Licensed once per page maximum, as "stones in
  a wall": rows separated by water gaps, opening by a 500ms
  `--ease-settle` height settle of the answer stone beneath
  its question stone. FAQ only.
- **Modal / dialog.** Refused as an overlay rectangle.
  Replacement: the pool pattern — a full-reach section the
  page descends to (used for the booking terms & the long
  policy texts), or the mobile bank-menu (§6.11), the theme's
  one licensed overlay, itself a fall of pebbles on a `--pool`
  ground.
- **Toast.** Refused. News from the site arrives as a stone in
  the bed: a notice pebble inserted at the top of the relevant
  section ("The bridge at Millrace is closed this week."),
  dismissible by a text link, never timed, never stacked.
- **Alert / notice.** The notice pebble above; urgent (safety)
  notices take `--algae` ground with `--dry` text — the theme's
  loudest voice is still a stone.
- **Pagination.** Stepping stones (§7): "← Upstream" /
  "Further downstream →" as chip pebbles, with "Reach 2 of 5"
  as text between — reaches, not pages; a river is not paginated,
  it is travelled.
- **Table.** The stone ledger: no grid lines, rows separated by
  10px of water, each row a very flat pebble (`--pebble-flat`
  at half amplitude), figures right-aligned in Bitter tabular.
  Licensed for the gauge record and price ledgers only;
  data-dense grids are refused outright (§1).
- **Progress.** §6.5's rolling pebble, or (in forms) the
  reckoning summary (§6.14) — where you are is stated in words
  and figures, never filled in a bar.
- **Spinner / loader.** Refused. §6.16's wetting stones are the
  loading state; a region that cannot even skeletonise shows
  the keeper's slow note, not a rotating anything.
- **Tooltip.** Refused. Anything worth saying is said on the
  stone (§12: the gauge chip carries its source in its text).
- **Image.** §6.3's morphing pebble mask, always with a caption
  stone beneath naming the place ("The pool below the mill,
  October") — an unnamed photograph is decoration.
- **Video.** Housed in a `--pebble-tall` mask, poster first,
  native controls (the platform's chrome is the visitor's own
  tool, exempt from the corner audit by §1's type clause
  reasoning — recorded here so the exemption is a decision, not
  an oversight).
- **Cookie notice.** A flat pebble (`--pebble-flat`) resting at
  the bed's downstream corner, two stones inside it: "Yes,
  settle" / "No, keep me dry" — the theme's consent in its own
  grammar, and the original entry's promise kept: even the
  cookie banner is a pebble.
- **Search.** A single trough field (§6.14 grammar) labelled
  "Look in the river…" with results as §6.13 stones. No search
  icon — a magnifier has a handle and a circle, and neither is
  a stone; the field is labelled in words instead.
- **Footer.** §6.17's bank. **404.** §6.18's stranded stone.
  **Skip link.** A plain text link, `--dry` on `--pool`,
  appearing on focus at the page's source — the one element
  allowed to be un-pebbled, because it is a tool, not a place.

## 12. Content & copywriting voice

Two registers. **The Keeper** — the lodge-keeper / stone-
merchant / river-trust warden who runs the place — writes
headlines, labels, errors and empty states: plain, warm,
specific, sentence case, fond of the river's facts. **The
Record** — the gauge board's voice — writes figures, sources
and confirmations: units always, sources always, no adjectives.
A sentence that could belong to a hotel chain or a software
product belongs to neither.

**Headlines** name the place or the fact, in a sentence:
✓ "The river was here first. We built quietly around it."
✓ "Six rooms, all facing the water."
✗ "Welcome to Your Dream Riverside Escape!!!" (three failures:
title case, exclamation, and a dream nobody measured).
✗ "Unlock seamless tranquillity" (software words in a stone
world).

**Labels & buttons** say the act in the visitor's words:
✓ "Ask for these nights" / "Keep this stone" / "Further
downstream".
✗ "Submit" / "Click here" / "Learn more" (learn *what*? the
label must carry its object or be rewritten).

**Figures** follow the Record: "64 cm at the lodge stone",
"1,180 L/s at the weir", "11,400 years — from the 1911 survey".
Banned forms: bare numbers, rounded ages ("ancient",
"thousands of years"), percentages of feelings ("98% of guests
feel restored"), and any count the river object (§2) cannot
source.

**Errors** are the Keeper, kind and exact, always with the fix:
✓ "That direction won't reach anyone — the @ is missing, looks
like."
✓ "Those nights have already flowed past — the calendar opens
at tomorrow."
✗ "Invalid input." / "Error 422." (The visitor is a guest, not
a request.)

**Empty states** admit the dryness: ✓ the stranded stone's
"This page is not in the river." ✓ a listing with no rooms:
"No stones are resting here this season — the river is being
relaid. Try the next reach down." ✗ "No results found." with a
grey icon of a magnifier.

**Fixed strings (verbatim, do not paraphrase).** The colophon:
"No sharp corner exists anywhere on this page — not even here."
The pool's opening line pattern: "Below [the bridge / the
mill], the water deepens." The confirmation's close: "The stone
is in the book." The slow note: "The river is slow today — this
part is still coming."

**Image rule.** Every photograph is captioned with its place
and season (§11); stock imagery of *other* rivers is the
theme's one unforgivable content sin — a streambed site built
from a photo library's river is a lie with good art direction.

## 13. Full-page scroll choreography map

The home page (§7's order), beat by beat. Times are for a
reading-pace scroll; scrubbed beats follow the visitor, timed
beats fire once.

1. **Arrival (t=0–3.4s).** §6.12's ceremony: letters seat, chip
   wets, bed settles (§6.1), streamline draws (§6.6). The
   margin pebble (§6.5) sits dry at the source.
2. **First scroll.** Hero drift begins (§6.2 sine); the pebble
   wets and rolls; notch 1 arms. The hero's morphs (§6.3)
   continue at their phases — the bed is alive under the hand.
3. **The listing reach.** Per-row waterlines lift (§6.7); cards
   settle 10px in rows (§6.13); the sheen band (§6.10) crosses
   somewhere in this reach on its 20s weather, indifferent to
   the visitor — that indifference is the realism.
4. **The descent.** The pool's sticky engages (§6.4):
   `--depth` 0→1 across 35% of the pin; drift dies; the rail
   dives; tempo stretches to 1.8×. The visitor's hand slows —
   the map's central beat, the one the whole page exists to
   produce.
5. **The deep (35–75%).** The story read at pool tempo; the
   pool photograph morphing at 21.6s; figures printing inside
   the dark. No notch drops here — the pebble is underwater
   and the map honestly shows a gap in the rail.
6. **The shallowing (75–100%).** Unpin; ground settles to
   `--pool`; tempo and drift restore; the pebble resurfaces
   downstream of the pool at its mapped position, notch for
   the pool dropping as it surfaces — the record kept even
   where the stone could not be seen.
7. **Figures reach.** §6.15's band lifts and counts once,
   1400ms, from approached values.
8. **The booking reach.** §6.14's form, still: morphs rested,
   sheen the only permitted passer-by. The calmest beat on the
   map, deliberately.
9. **The bank.** §6.17's record stones settle 8px; the
   colophon prints the law. End of the map: the visitor has
   been carried the length of one river, and the last thing
   they read is the page keeping its promise about corners.

*Reverse pass:* beats run backward symmetrically except the
latched ones — notches stay dropped, figures stay counted,
kept stones stay wet. *Jump-scroll catch-up:* anchor landings
snap every scrubbed value to the landing position (§6.2,
§6.7); ceremonies never replay for a jump.

## 14. Whole-page performance budget

- **Weight.** Total page ≤ 900KB at first load: HTML/CSS/JS
  ≤ 210KB (the theme's own JS — the shared loop, the settle,
  the line computation, the form — ≤ 38KB gzipped), fonts
  ≤ 120KB (Bitter 600/700 + Source Sans 3 400/600, subset to
  the site's languages, `font-display: swap` behind the §6.1
  fonts race), images ≤ 570KB with the hero photograph ≤ 180KB
  (WebP/AVIF, pebble-masked crops served at rendered size —
  the mask crops 6% and the srcset knows it).
- **Frame budget.** The shared loop's per-frame cost ≤ 1.6ms
  on a mid-tier phone: ≤ 4 section transforms, ≤ 6 parallax
  layers, ≤ 6 morphing masks, 1 rail write. Long tasks: none
  > 50ms after load; the §6.6 path computation (≤12 segments)
  is the largest single task and is budgeted at 8ms, run once,
  off the critical path.
- **Cut order** (when the budget is exceeded, cut in this
  order, never silently): (1) the wet-sheen band (§6.10) —
  weather goes first; (2) the scroll-roundness composition in
  §6.3 (masks keep their time-morph); (3) the deep parallax
  layer (§6.2); (4) morph cycle pauses beyond 3 live masks;
  (5) the streamline's resize re-draw (load draw stays).
  **Never cut:** the corner audit, the waterline's legibility
  bound, any watchdog, the form's reckoning, the reduced-motion
  variants. A build that cuts a never-cut to meet budget is
  over budget *and* failed.
- **Device probes.** `save-data` or ≤4GB RAM: sheen disabled,
  morphs capped at 3, hero image at the smaller srcset step.
  These are the §6.10/§6.3 rulings, gathered here so the budget
  is one document.

## 15. Build-order checklist

1. The static streambed first: full page, all content, pebble
   recipes applied, corner audit (§10.1) passing with JS off.
2. The river object (§2) authored and its three printings
   (§6.12 chip, §6.15 band, §6.17 footer) rendered from it;
   agreement diffed.
3. Typography and the §3 laws; the Record's source lines
   written for every figure.
4. The shared loop (§5) with drift + parallax (§6.2) behind
   the reduced-motion check.
5. Waterline reveals (§6.7) with watchdogs; no-strand test.
6. The hero composition (§6.12): seating, chip, bed settle
   (§6.1), streamline (§6.6) last of the hero's parts (it is
   computed from the settled bed).
7. Cards (§6.13) with nudge (§6.8), ripple (§6.9), tilt.
8. The deep pool (§6.4): pin tested in the real template
   (sticky ancestors), tempo + depth from the one `--depth`.
9. Progress pebble (§6.5) generated from the live section list.
10. Figures (§6.15) counting from approached values.
11. The form (§6.14): native first, then the reckoning, then
    the keeper's errors, then the confirmation stone;
    form-keeping rehearsal (§10.9).
12. Skeleton + transitions (§6.16); 404 (§6.18) served with
    the app down.
13. Ambient loops last: morphs (§6.3), then the sheen band
    (§6.10); ambient census (§10.5).
14. Reduced-motion pass: every variant in §6 verified
    reachable; still-photograph test (§10.10).
15. The gate (§10) signed by a non-builder, including the
    colophon claim — the signer checks one corner at random,
    by hand, on the live page.
