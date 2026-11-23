# 34. Kiln Opening — Expanded (v1 + v2)

> Expansion of theme #34 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are already finished when you arrive. This one is still
in the kiln. The page is **a firing in progress**: it opens in darkness
and heat — kiln dark, ember orange, a crack of light widening as the
door comes off — and as the visitor scrolls, the firing runs its full
course and the kiln **cools**. Colours literally cool down the page:
ember `#E4572E` at the top, through fired clay and ash in the middle,
to the pale green-grey of finished celadon glaze at the foot. The last
section is a cold kiln and a finished shelf of pots. The scroll *is*
the firing schedule, and the corner readout (§6.3) is its pyrometer:
1280°C at the hero, 40°C — room temperature, safe to touch — at the
footer.

The world is the potter's kiln, treated as a complete interface
vocabulary rather than a skin. The page has a **door** (the hero is
inside the kiln; opening it is the page load, §6.1), a **chamber**
(sections are temperature bands of one firing, §6.4), **shelves**
(every product sits on a thin clay kiln-shelf ledge with a contact
shadow and a handwritten firing number, §6.5), **witnesses** (the
temperature readout and the firing-log navigation record what the
firing actually did, §6.3, §6.10), and an **opening** (the footer is
the moment the cold kiln is unloaded and the firing is written up,
§6.15). Nothing on the page is at room temperature until the visitor
has earned the bottom of the scroll.

**The theme's one law: the cooling is real, or the cooling is absent.**
Every temperature the page states is computed from one declared
schedule (§5) — the readout, the section bands, the navigation stamps
and the piece data all read the same curve, so they can never disagree.
A Kiln Opening build that hand-picks a "1280°" for the hero and a
"900°" for a mid-page badge because they looked right has not bent the
theme; it has broken the only promise it makes, and the quality gate
(§10) fails it on sight. The schedule is: ramp to a 1280°C peak
(cone 10, stoneware), a 20-minute soak, then a controlled cool that
slows deliberately through **573°C — the quartz inversion**, the
temperature at which silica in the clay body contracts suddenly and a
careless cool cracks the ware (dunting). The page honours that physics:
the cooling curve flattens at 573°C, the readout lingers there, and the
section at that band is the page's quietest (§13). A potter reading the
site will check the curve. It must be right.

**Heat is the interaction model.** Because the page is hot at the top
and cold at the bottom, attention itself has a temperature: hovering a
cooled piece briefly re-warms its rim (§6.9), pressing a piece seats it
into its shelf shadow (§6.12), and nothing below the ash band ever
glows again. The visitor does not browse the site; they attend a
firing, and then they unload it.

**Best-fit sites and audiences.**

- Potters, ceramic studios and kiln-fired craft makers selling the
  work itself: studio pottery shops, wood/soda/salt firing collectives,
  ceramic artists whose process *is* the brand. The firing numbers on
  the shelves (§6.5) are the maker's real firing log.
- Any maker whose product is transformed by one irreversible thermal
  process: glassblowers and lampworkers, blacksmiths and bladesmiths,
  cast-metal foundries, bakers of wood-fired bread, coffee roasters
  (with the schedule re-declared: 196–210°C, first crack at ~196°C —
  the law travels, the numbers change).
- Process-led storytelling: a single product's journey from raw to
  finished (one vessel, one firing), a workshop's open-day invitation,
  a residency or course page structured as the firing students will
  attend.
- Limited "kiln opening" sales events: the stock genuinely exists only
  when the kiln opens, so the page's cooling-to-availability arc is a
  fact, not a countdown costume.

**When NOT to use it.**

- For anything that must feel instant, cool or clinical. The theme's
  top half is dark, hot and slow; a fintech dashboard or a medical
  service wrapped in ember orange is a category error.
- For content with no transformation in it. If nothing on the page is
  made, fired, baked or changed by heat, the cooling curve is a
  screensaver laid over unrelated text — the exact failure §9 names
  first.
- For high-density catalogues. Shelves (§6.5, §6.11) hold at most
  12 pieces per band before the chamber reads as a warehouse; a
  400-SKU store cannot be a single firing.
- For urgent or breaking content. A firing takes the time it takes;
  the page's scroll feel is heat-heavy at the top by design (§5) and
  nothing in it can say "just in."
- Where the maker will not publish real firing data. The law above:
  invented temperatures are detectable (the curve won't match the
  bands) and they are the one unforgivable shortcut.

## 2. Palette

Five anchors, inherited unchanged. The palette is a temperature scale
before it is a colour scheme: every token is a point on the cooling
curve, and a colour may only appear in the band whose temperature it
names (§6.4 enforces this; §10 audits it).

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--kiln-dark` | `#1A0F0A` | The chamber: hero ground, all grounds above ~800°C, the door's darkness | ~22% of pixels | Near-black with a brown heart — never `#000`. Ash on it: 10.9:1. Ember on it: 4.6:1 — display and glow only, never body text. |
| `--ember` | `#E4572E` | Live heat: the door crack's light, the headline's unfired state, re-warm rims, peak-temperature accents | ≤6% of pixels, hard ration (§9) | On kiln-dark 4.6:1 (large text ≥24px and non-text accents only). On ash 2.5:1 — **never text on light grounds**; ember is a light source, not an ink. |
| `--fired-clay` | `#C97B4A` | The ware itself: shelf ledges, contact-shadow warmth, mid-band grounds in transition, firing numbers' ink at mid-page | ~14% of pixels | On kiln-dark 5.4:1; on ash 2.9:1. As text: only on kiln-dark at ≥18px, or darkened to `--clay-deep` on light grounds. |
| `--ash` | `#D8CFC0` | The cooled surface: mid-to-low band grounds, body text on dark bands, card grounds in the cool half | ~38% of pixels | The page's workhorse light. Ink (`--ink`, derived) on ash: 11.8:1. Celadon-deep on ash: 5.1:1. |
| `--celadon` | `#3E5C50` | Finished glaze: the final band's ground accents, links and interactive ink in the cool half, the footer's voice | ~8% of pixels | On ash 5.9:1 — AA at all sizes, so celadon is the cool half's text-grade accent. On kiln-dark 3.1:1 — never used there; celadon belongs to the cold end only. |

**Derived tokens** (computed from the anchors; never new hues):

| Token | Derivation | Use |
|---|---|---|
| `--ink` | `#241A12` (kiln-dark warmed and lifted ~6%) | Body text on ash and celadon-pale grounds. On ash 11.8:1. The headline's final cooled colour (§6.2). |
| `--clay-deep` | `#9A5527` (fired clay darkened ~22%) | Firing numbers and clay-coloured text on light grounds. On ash 4.7:1 — AA at all sizes. |
| `--celadon-deep` | `#2C443B` (celadon darkened ~18%) | Celadon text on ash where AA-normal is required at small sizes: 7.4:1. |
| `--celadon-pale` | `#DCE5DC` (celadon tinted to 12% over ash) | The final band's ground; the coldest surface on the page. Ink on it 12.6:1. |
| `--ember-bright` | `#FF8A50` (ember lightened toward flame) | The specular core of the door crack (§6.1) and the headline's peak glow (§6.2) — a light, never a fill for text. |
| `--shadow-contact` | kiln-dark at 55% | The contact shadow under every shelf piece (§6.5); deepens as a piece lands. |
| `--hairline` | current ground's ink at 18% | Rules, shelf edges, the firing-log table lines (§6.10). |

**Dark-mode behaviour.** The page already begins in darkness and ends
in light; there is no inverted twin. Under
`prefers-color-scheme: dark`, the cool half deepens instead: ash
grounds drop to `#B9AE9C`, celadon-pale to `#22302A` with ash text
(9.8:1) — the kiln at night, unloaded by lamplight. The hot half is
unchanged: a firing does not care what time it is outside. Contrast
figures above are the light-scheme values; the dark cool-half pairs
are audited separately at the gate (§10).

**Temperature binding.** Each token carries the band it belongs to:
ember lives above 1000°C, fired clay 600–1100°C, ash 150–700°C,
celadon below 150°C (glaze is only *finished* — and only this green —
when cold). An ember accent in the celadon band is not a style choice;
it is a physics error, and §9 lists it as slop.

## 3. Typography

Two typefaces, inherited unchanged. **Fraunces** — a soft, warm serif
with optical sizing and a low-contrast swell that reads as thrown clay
at display sizes — carries display, headings, piece names and the
temperature readout's numerals. **Work Sans** carries body, data,
labels and the firing log. A third hand appears only as data: the
firing numbers (§6.5) are set in Fraunces italic at small size,
slightly rotated (−1.5°), because in the studio they are written on
the shelf edge in pencil — the rotation and italic are the theme's one
permitted informality, and they belong to the number, never to prose.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero headline) | Fraunces 72pt optical, wght 560 | clamp(44px, 7.2vw, 88px) / 1.02 | −0.01em | Set ember at first paint of the animation, cooling to `--ink` (§6.2). Never set in ember on a light ground. |
| H2 (band titles) | Fraunces, wght 520 | clamp(30px, 4vw, 46px) / 1.08 | −0.005em | Each band title names a firing stage, not a marketing section ("The Soak", "Quartz Inversion", "The Opening"). |
| H3 (piece names) | Fraunces, wght 500 | 21px / 1.2 | 0 | The pot's name as the maker names it — "Ash-glazed Yunomi", not "Premium Ceramic Cup". |
| Body | Work Sans 400 | 17px / 1.62 | 0 | Measure 58–66ch. On dark bands set in ash; on light bands in `--ink`. Never in ember or fired clay. |
| Caption / shelf note | Work Sans 400 | 13.5px / 1.5 | 0.005em | Sits under the shelf ledge, left-aligned with the piece's left edge. |
| Data (temperatures, times) | Work Sans 500, tabular figures | 14px / 1.4 | 0.02em | All temperatures carry the unit every time ("1,280°C", never a bare "1280"). Thousands separated, always. |
| Firing number | Fraunces italic 480 | 12.5px | 0.01em, rotate −1.5° | Format is law: `Firing № 214` — the № glyph, a space, the number from the maker's log. Never generated (§10). |
| Readout (§6.3) | Fraunces 72pt, wght 600, tabular | 15px | 0.03em | The pyrometer's voice: value + unit + the word for the stage ("soaking", "cooling", "cold"). |

**Type laws.**

1. **Temperature is always typeset, never implied.** Any sentence about
   heat states its number. "Hot" alone is a banned word in body copy
   (§12); "1,120°C and falling" is the theme's register.
2. **Band titles are firing stages.** A section that cannot be named
   as a stage of the firing does not belong on this page.
3. **The firing number is data, not decoration.** It comes from the
   build's content (the maker's log) and is identical in the shelf
   note, the card (§6.11) and the order form's record (§6.14).
4. **Fraunces never sets body text; Work Sans never sets a headline.**
   The casting does not swap, at any breakpoint.
5. **No all-caps except the readout's stage word and table headers**,
   tracked +0.14em, Work Sans 11px. Shouting is heat the page has
   already spent.

## 4. Layout language

**The gradient is the architecture.** The page is one vertical
temperature field divided into **bands**, each band a stage of the
schedule (§5): Door (1280°C), Soak (1280°C held), Descent (1100°C),
Quartz Inversion (573°C), Ash (300°C), Glaze (120°C), Opening (40°C).
A band's ground colour is its temperature made visible (§6.4), bands
are separated by crackle dividers (§6.7), and content density falls
with temperature: the hot bands are sparse and monumental (one piece,
one statement), the cool bands are dense and useful (shelves of
pieces, the log, the form). Heat is spectacle; cold is inventory.

**Shelves.** The recurring horizontal unit is the **kiln shelf**: a
ledge 14px tall in fired clay with a 1px lighter top edge (the shelf's
worn face) and the pieces standing on it, each with its contact shadow
and firing number written at the shelf's left end. A shelf holds
1 piece in the hot bands, 2–3 in the ash band, up to 4 in the glaze
band. Shelves never float: a shelf's ledge spans the content column
edge to edge, and the caption sits *under* the ledge, in the shadow
side, like a note pencilled on the kiln book.

**Grid and rhythm.** Content column max 1180px, centred; the hero
piece (§6.8) pins at the column's centre. Vertical rhythm is thermal,
not modular: band padding shrinks as the page cools — 18vh in the Door
band, 14vh at Soak, 10vh through Descent and Inversion, 7vh in Ash
and Glaze, 5vh at the Opening — because a cooling kiln is opened
faster than a firing is watched. Horizontal whitespace is the
chamber's air: pieces never sit closer than 48px to a band edge.

**The margin is the kiln wall.** Outside the content column, the page
keeps two fixed instruments and nothing else: the temperature readout
(bottom-right, §6.3) and, on ≥1200px, the firing-log rail (§6.10) at
the left edge. No other fixed chrome is permitted; a sticky marketing
header would be a plastic sign taped to a kiln door.

**Density law.** One idea per band in the hot half; the visitor should
be able to state each hot band's content in five words ("the door
opens", "one vessel, soaking", "the dangerous temperature"). If a hot
band needs a second paragraph, the paragraph moves down a band and
cools with the page.

**Shelf geometry.** A shelf's ledge is 14px tall at every breakpoint;
what changes is its span and load. At ≥1200px the ledge spans the full
1180px column and a glaze-band shelf carries 4 pieces with ≥48px of
air between neighbours. At 768–1199px the ledge spans the column
minus the log rail's ghost (the rail is gone at this size, but its
absence is not filled — the margin stays kiln wall, §4 above). Below
768px a shelf is one piece wide and the ledge shortens to the piece's
width + 32px, so the shelf reads as *that pot's* ledge rather than a
counter the pot happens to stand on. The firing number sits at the
ledge's left end at every size except <768px, where §6.5 moves it
beneath. A shelf never wraps mid-piece: if the next piece does not
fit whole, it starts a new shelf — ware is not cropped to a grid, and
a shelf with one piece on it is a normal sight in a real kiln yard.

## 5. Full motion system

One schedule drives everything. **The firing curve** is a function of
page scroll progress `p` (0 at the hero's top, 1 at the footer's end),
computed once in the shared loop and consumed by the readout (§6.3),
the band crossfades (§6.4), the ember density (§6.6) and the
navigation stamps (§6.10):

- `p` 0 → 0.10: **1280°C held** (the soak — the curve is flat; the
  hero and its pinned piece live here).
- `p` 0.10 → 0.45: falls 1280 → 620°C, ease-in (slow at first — a kiln
  is never crashed open).
- `p` 0.45 → 0.58: **flattens at 573°C** (quartz inversion; the curve
  spends 13% of the page crossing 60 degrees — the slowest, most
  careful passage, and the copy in this band says why).
- `p` 0.58 → 0.88: falls 573 → 120°C, steady.
- `p` 0.88 → 1: falls 120 → 40°C; at 40°C the readout's stage word
  becomes "cold" and the Opening band (§6.15) is safe to touch.

**The declared schedule** (this build's instance — cone-10 stoneware,
electric kiln, 25 hours 20 minutes door-to-door). Every figure in
§6.3, §6.10 and §6.15 is read from this table and no other source:

| Firing clock | Curve point | Temperature | What the kiln is doing |
|---|---|---|---|
| 06:10 | p 0.00 | 40°C | Door closed, first ramp begins |
| 09:40 | — | 573°C rising | Quartz inversion crossed *slowly on the way up too* — the log notes it; the page's plateau is on cooling, where dunting bites |
| 15:40 | p 0.00–0.10 | 1,280°C | Peak. Cone 10 bends. Soak begins |
| 16:00 | p 0.10 | 1,280°C | Soak ends (20 minutes); cooling begins, flaps closed |
| 18:20 | p 0.45 | 620°C | Descent slows; the careful part approaches |
| 19:05–21:30 | p 0.45–0.58 | 590 → 560°C | **The inversion plateau** — 2h 25m to cross 30 degrees |
| 02:15 | p 0.88 | 120°C | Kiln dark outside, still too hot to open |
| 07:30 next day | p 1.00 | 40°C | The opening. Ware unloaded onto the shelves the visitor has been reading |

Re-declaring for another craft (§1's list) means replacing this table
— a roast curve, a bake — and re-deriving every band plateau from it.
A build that keeps this table's shape but swaps only the peak number
has not re-declared; it has relabelled, and §10 item 1 catches it
because the log's times will no longer sum to a firing anyone could
actually run.

**The shared loop.** All scroll-driven values — temperature, band
crossfade positions, ember density, the pinned piece's chapter index,
the readout — are written by **one** `requestAnimationFrame` loop
lerping scroll position at **0.12** (0.09 in the Inversion band: the
page itself cools more carefully there). The loop writes CSS custom
properties (`--temp`, `--cool` per band) and transforms/opacity only;
it never writes layout. When the tab is hidden or the loop idles
300ms past the last scroll input, it sleeps.

**Named easings** (the kiln's five): `--ease-door`
(cubic-bezier(0.7, 0, 0.2, 1) — heavy iron swinging), `--ease-cool`
(cubic-bezier(0.3, 0.6, 0.2, 1) — heat leaving, fast then slow),
`--ease-settle` (cubic-bezier(0.2, 0.9, 0.25, 1) — a pot set down),
`--ease-flicker` (steps, authored per element — flame is not smooth),
`--ease-press` (cubic-bezier(0.6, 0, 0.3, 1) — a hand pressing clay).

**Every motion term, translated:**

- *Scroll-triggered reveals* — shelf placement (§6.5): pieces rise
  26px onto their ledges as their shelf enters, stagger 110ms,
  `--ease-settle`. Nothing fades in from nothing; pots are *placed*.
- *Scroll-driven / scrubbed animation* — the cooling itself (§6.4,
  §6.3): the page's master scrub.
- *Parallax* — heat shimmer above finished pieces in the cool bands
  only (§6.13) and ember rise (§6.6) in the hot bands; layers move at
  0.92 / 1.0 rates. There is no decorative background parallax: the
  chamber does not have scenery.
- *Pinned sections* — the hero piece pins for 120vh while its glaze
  story scrolls past (§6.8); the firing-log rail pins on ≥1200px
  (§6.10).
- *Smooth scrolling* — the shared loop's lerp gives the scroll its
  thermal weight: heavy in the hot half, and from the Ash band down
  the lerp rises to 0.16 — the original entry's "heat-heavy at top,
  crisper as it cools", implemented as one variable.
- *Progress indicator* — the temperature readout (§6.3). There is no
  bar anywhere on the page.
- *Staggered reveals* — shelf placement (§6.5) and the firing log's
  rows (§6.10), both in reading order, both capped (§14).
- *Masked reveals* — the kiln-door crack is a clip-path inset mask
  (§6.1); band titles rise through a 100% mask line (§6.4's companion
  rule in §13).
- *Kinetic typography* — refused, with one exception: the headline's
  last word flickers once (§6.2). Type in a kiln does not dance; it
  heats and cools.
- *Marquee* — refused. Nothing in a kiln moves sideways forever.
- *Counters* — temperatures and firing-log figures count/roll only as
  replays between two true values (§6.3, §6.10); invented figures are
  a gate failure.
- *SVG line-draw* — the crackle network across dividers (§6.7) and
  the footer's firing-curve signature (§6.15).
- *Image scale-in-frame* — pieces settle 1.06 → 1 inside their shelf
  frames as they are placed (§6.13).
- *Hover micro-interactions* — re-warm (§6.9): an ember rim returns at
  500ms, in the kiln's language, and cools on leave.
- *Magnetic / tilt* — refused. Pots on shelves do not lean toward the
  visitor's hand; the press (§6.12) is the only touch.
- *Custom cursor* — refused; normal system cursor only (standing
  rule).
- *Skeleton loading* — unfired bisque skeletons that fire into content
  (§6.17).
- *Page transitions* — the stoke transition (§6.16): the door closes
  and opens on the next page, already cooling.
- *Reduced motion* — the page opens at one fixed mid-cool palette
  (the Ash band's, ~300°C) with no crossfade, no embers, no pin; all
  content present (§6 elements each specify their variant; the
  original entry's ruling, kept verbatim in spirit).

**Watchdog law.** Every timed or scroll-armed animation carries a
forced-complete fallback: 1.5s for the door and headline (§6.1, §6.2),
1.2s for reveals, 1s for the crackle draw. If the loop stalls, the
page resolves to its cooled, readable state — the state the DOM ships
in. A visitor must never be able to find a page stuck hot, dark or
blank because a script stopped.

## 6. Signature elements

### 6.1 Kiln-door opening

- **What & why.** The theme's signature and its thesis performed at
  load. The hero begins as the closed kiln: a kiln-dark field with one
  vertical crack of ember light at its centre — the gap between door
  and chamber that every potter knows, the line of fire you check with
  one eye closed. The crack widens and the hero is revealed *inside*
  the kiln: headline glowing ember (§6.2), the hero piece on its shelf
  (§6.8). It belongs because the hero content genuinely is in the kiln
  at 1280°C — opening the door is not a preloader costume, it is the
  page load itself, and skipping it would be opening the kiln before
  the visitor arrived.
- **Structure.** A `<div class="door">` overlaying the hero only (not
  the page — bands below the hero are never covered), composed of two
  kiln-dark panels meeting at a centre seam. The crack is a
  `clip-path: inset()` mask on the hero's reveal layer plus a 2–6px
  ember gradient bar at the seam (`--ember-bright` core, `--ember`
  falloff, blurred 8px). The hero content beneath is fully rendered
  from first paint; the door is an overlay the JS arms. Door furniture:
  two hinge shadows at the left edge and the spy-hole — a 10px circle
  of ember at 62% height on the seam — because a kiln door is checked
  through its spy-hole before it is opened.
- **Motion spec.** Trigger: page load, after `document.fonts.ready`
  or the 900ms font watchdog, whichever first. The crack widens:
  clip-path inset goes from `inset(0 49.6% 0 49.6%)` to
  `inset(0 0% 0 0%)` over **1600ms `--ease-door`**, the seam bar
  widening 2px → 14px in the first 400ms (the gap glows before it
  opens) then dissolving as the panels part. At 1600ms the overlay is
  removed from the tree. The spy-hole brightens once at t+300ms (the
  check) before the crack moves. **Watchdog: 1500ms** from arming —
  if the animation has not completed, the overlay is removed
  instantly; the hero must never stay behind a door (§5's law).
- **Choreography timeline (v2).** t+0: hero paints beneath the armed
  door, crack a 2px ember line → t+300ms: spy-hole flare (opacity
  0.6 → 1, 120ms) → t+400ms: seam bar at full 14px glow → t+400–2000ms:
  inset widens on `--ease-door`, most travel in the middle 800ms (a
  door on its hinge swings, it does not slide) → t+2000ms: overlay
  removed; §6.2's cooling, already running beneath, becomes the hero's
  only motion → t+3500ms: nothing of the door remains in the DOM.
- **State matrix (v2).** *Rest (no JS):* no overlay exists — the hero
  stands open and cooled; this is the shipped DOM state. *Armed:*
  crack closed, hero covered, 1600ms. *Opening:* as timeline.
  *Open (terminal):* overlay removed. *Hover/focus:* the door is not
  interactive; focus order passes beneath it only after removal, and
  the hero's first link is inert until t+2000ms (an `inert` attribute
  lifted at completion or watchdog). *Scrolled-past:* the door never
  re-arms; a return to the top shows the open, cooling hero.
  *Disabled:* JS off = rest state. Touch identical to desktop; the
  gesture is time, not pointer.
- **Content merge.** The door covers the hero because the hero is the
  kiln's contents. The crack's light is the headline's own ember
  (§6.2) seen through the gap — the glow colour and the headline
  colour are the same token at the same moment.
- **Failure fallback.** Overlay is JS-inserted; without JS it never
  exists. Slow network: fonts watchdog at 900ms starts the opening in
  fallback serif metrics. If `clip-path` inset animation is
  unsupported, the overlay fades (opacity, 400ms) instead — a lesser
  door, still a door, still removed by the same watchdog.
- **Reduced-motion variant.** No door. The hero is simply present,
  open, at the mid-cool palette (§5). The visitor loses the ceremony
  and nothing else.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: opening
  1400ms, seam bar peak 10px. <768px: opening 1200ms, the spy-hole is
  omitted (at phone width the crack alone reads), hinge shadows
  omitted.
- **Edge cases & failure modes (v2).** *Return visit in the same
  session:* the door still opens (it is the page's first act, not a
  splash screen), but at 900ms — the potter opens a familiar kiln
  faster. *Visitor scrolls during the opening:* the hero scrolls
  normally beneath; the overlay is hero-bound, not viewport-fixed, so
  it scrolls away with its band and is removed by the watchdog
  regardless. *Hero image late:* the door opens on schedule over the
  shelf and its caption; the piece (§6.8) fades in on its shelf when
  loaded — the kiln does not wait for a pot that is already inside it.
- **Accessibility spec (v2).** The overlay is `aria-hidden`; the hero's
  heading is the first thing in the accessibility tree and is never
  withheld. The `inert` period is capped at 2000ms and announced
  nowhere — it is a visual ceremony over announced content. Focus is
  never moved by the door. Contrast of the crack is decorative light,
  exempt as non-text, but the seam bar never overlaps text.
- **Performance budget & mobile variant.** One clip-path animation on
  one overlay, compositor-only; the blur on the seam bar is a static
  pre-rendered gradient, not a live filter. Mobile: durations above;
  no other cost.
- **Tokens consumed (v2).** `--kiln-dark`, `--ember`, `--ember-bright`,
  `--ease-door`, `--door-dur` (1600ms), `--watchdog-door` (1500ms).

### 6.2 Headline cooling

- **What & why.** The headline is the first object fired. It arrives
  glowing ember — lit from inside, the way a pot's rim glows at peak —
  and over three seconds it cools through fired clay to ink, its glow
  dying as the colour settles. Its last word flickers once, at 1.2s,
  like a flame catching before it goes out. It belongs because the
  title performs the page's whole plot in miniature: everything here
  was hot, everything here cools, and the cooling is the content
  arriving at its finished state. A headline that simply faded in
  would say none of that.
- **Structure.** The hero `<h1>` as real text in the DOM, in its final
  cooled colour (`--ink` on the hero's lightening ground, or ash —
  per band) from first paint. The cooling is an overlay effect: a
  duplicate text layer (aria-hidden) in ember with a soft glow
  (text-shadow stack: 0 0 18px ember at 0.55, 0 0 46px ember at 0.25),
  masked to the headline's glyphs, whose opacity and colour the
  timeline drives. The last word is wrapped in a `<span class="last">`
  in both layers for the flicker.
- **Motion spec.** Trigger: time — begins when the door (§6.1) passes
  50% open, or at load+600ms if the door is absent. Duration **3000ms
  `--ease-cool`**: overlay colour ember → fired clay (at ~55%) → ink,
  overlay opacity 1 → 0 across the final 600ms, glow shadows shrinking
  46px → 0 in step. The flicker: at t+1200ms the last word's overlay
  opacity steps 1 → 0.35 → 0.9 → 0.5 → 0.85 over 260ms in 5 authored
  steps (`--ease-flicker`) — one catch, never a strobe, never repeated.
  **Watchdog: 1500ms** after trigger, the overlay is forced to its end
  state (the original entry's forced-complete fallback, kept).
- **Choreography timeline (v2).** t+0: overlay at full ember, glow at
  full spread → t+1200ms: the flicker, last word only → t+1650ms:
  colour crosses fired clay; glow at ~40% → t+2400ms: colour reaches
  ink; overlay begins its fade → t+3000ms: overlay opacity 0, removed
  from the tree; the headline is its DOM self → thereafter: the
  headline never glows again except the re-warm law does not apply to
  type (§6.9 is for pieces).
- **State matrix (v2).** *Rest (no JS):* headline in final ink — the
  shipped state, fully readable. *Cooling:* 3000ms as above, desktop
  and touch identical. *Cooled (terminal):* overlay removed. *Hover:*
  none — headlines are not controls. *Focus:* n/a. *Scrolled-past:*
  cooled; scrolling back up does not reheat the headline (the firing
  happened; §5's curve governs bands, not this one-time act).
  *Disabled:* rest state.
- **Content merge.** The cooling happens to the headline's own
  glyphs; the glow is the headline's heat, not a light laid over the
  hero. The flickering word is the headline's last word — chosen by
  the copy, not by the effect (copy law §12: headlines are written so
  the last word can bear a flame — a verb or the vessel's name, never
  a preposition).
- **Failure fallback.** The base text is always present and legible
  beneath the overlay; if the overlay's colour animation is
  unsupported it crossfades opacity only. If JS dies mid-cool, the
  1500ms watchdog (a plain timer, independent of the rAF loop) removes
  the overlay.
- **Reduced-motion variant.** No overlay, no flicker. The headline is
  ink from first paint — the finished pot, unglazed by ceremony.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: glow spread
  32px max, duration 2600ms. <768px: glow 20px max, duration 2200ms,
  flicker amplitude softened (steps between 1 and 0.55) — a phone is
  held closer; the flame is smaller.
- **Edge cases & failure modes (v2).** *Very long headline (3 lines):*
  the flicker word is the last word of the last line; the glow budget
  is per-headline, not per-line — spread caps hold. *Headline edited
  by a CMS to end in a weak word:* the flicker still fires on the last
  word (the mechanism is positional) but §12's copy rule is a gate
  item, not a runtime concern. *Fonts swap mid-cool:* the overlay is
  the same element's duplicate, so it swaps with the base; no
  double-image is possible because both layers share metrics.
- **Accessibility spec (v2).** The overlay is `aria-hidden`; the
  headline is announced once, in full, from first paint. The flicker
  is 5 steps over 260ms at ≤0.65 amplitude — far below any flash
  threshold (no more than 3 flashes/second at high contrast; this is
  ~2 shallow steps). Contrast: the *base* text meets AA at every
  moment (ink on its ground, 11.8:1); the ember overlay is decoration
  over a legible letter, never the letter's only rendering.
- **Performance budget & mobile variant.** One element, colour +
  opacity + text-shadow; text-shadow is the only paint cost and it is
  capped at two layers. Mobile: reduced spreads above.
- **Tokens consumed (v2).** `--ember`, `--ember-bright`, `--fired-clay`,
  `--ink`, `--ease-cool`, `--ease-flicker`, `--cool-dur` (3000ms),
  `--watchdog-cool` (1500ms).

### 6.3 Temperature readout — the pyrometer

- **What & why.** The page's progress indicator and its conscience. A
  fixed readout in the bottom-right corner shows the kiln's current
  temperature, scrubbed to scroll along the declared curve (§5):
  1280°C at the hero, falling as the visitor descends, flattening at
  573°C through the inversion band, reaching 40°C at the footer, where
  its stage word changes to "cold". It belongs because progress on
  this page *is* temperature — a scroll bar would measure the wrong
  quantity. It is also the law's enforcement made visible: because the
  readout, the bands (§6.4) and the log (§6.10) all read one curve,
  any inconsistency is visible to any visitor who watches two of them
  at once.
- **Structure.** A `<div class="pyrometer" role="img">` fixed
  bottom-right, 20px from each edge, above the bands (z-index below
  any modal). Contents: the value in Fraunces tabular ("1,280"), the
  unit "°C", and beneath, the stage word in Work Sans caps 11px:
  SOAKING (p < 0.10), COOLING (falling), INVERSION (the 573°C
  plateau), COOLING again, COLD (40°C). A 24px cone glyph beside the
  value tilts as temperature falls — a witness cone bending — drawn as
  a 3-path SVG whose middle path rotates 0° → 38° across the whole
  scroll: at 40°C the cone is slumped, the firing is provably over.
- **Motion spec.** Scrubbed by the shared loop (`--temp` written per
  frame, lerp per §5). The displayed integer updates at most every
  90ms (a pyrometer does not flicker through every digit; it settles),
  rounding to the curve's value at that moment. The cone's bend is
  continuous with `p`. The stage word changes only at band boundaries,
  with a 120ms opacity crossfade. At 40°C exactly, the readout's own
  colour completes its cool: value in `--celadon-deep`, stage word
  COLD — the only state change the readout ever performs on itself.
- **Choreography timeline (v2).** Spatial: hero — 1,280°C, SOAKING,
  cone upright → descent — value falling ~9°C per 100px of scroll,
  COOLING → inversion band — value crawls 590 → 560°C across the whole
  band, INVERSION, the readout's lerp visibly slower (§5) → ash band —
  falling resumes → glaze band — two digits, then 40 → footer — 40°C,
  COLD, cone slumped at 38°. The readout's whole performance is the
  curve, read aloud.
- **State matrix (v2).** *Rest (top):* 1,280°C SOAKING. *Scrubbing:*
  per curve, desktop and touch identical. *Hover:* none (not a
  control). *Focus:* not focusable. *Scrolled-past / at footer:* 40°C
  COLD, terminal. *Scrolling back up:* the value rises symmetrically —
  the readout reports position on the curve, and reheating on the way
  up is honest: the visitor has gone back into the hot part of the
  page. *Disabled (no JS):* the readout is absent — it is an
  instrument, and a dead instrument showing a fixed number would be a
  lie; the firing log (§6.10) carries the schedule as static text
  instead.
- **Content merge.** The readout measures the page the visitor is
  inside. Its numbers are the bands' numbers; remove the bands and
  the readout has nothing to report — the test every element here
  must pass.
- **Failure fallback.** If the shared loop stalls 800ms, the readout
  snaps to the curve value for the current scroll position on the
  next frame rather than animating toward it (a pyrometer that lags
  is worse than one that jumps). If scroll position is unreadable,
  the readout hides itself rather than guessing.
- **Reduced-motion variant.** The readout still reports — it is
  information, not ornament — but updates in 10°C steps at band
  boundaries only, and the cone is drawn at the bend for the current
  band (5 static poses). No continuous scrub.
- **Breakpoints (v2).** ≥1200px: full readout with cone, value 15px.
  768–1199px: cone omitted, value + stage word. <768px: value only,
  13px, bottom-left (the right thumb's corner is kept clear), stage
  word omitted — the bands themselves carry the stage names at this
  size.
- **Edge cases & failure modes (v2).** *Short page (a single-band
  landing):* the curve still maps p 0→1 across the document, so the
  readout falls the full schedule over a short scroll — fast, but
  truthful to the mapping; §4's density law makes such pages rare.
  *Anchor jump to the footer:* the value snaps (fallback rule above);
  the cone poses at 38° immediately. *Print:* the readout does not
  print; the log (§6.10) prints the schedule as a table.
- **Accessibility spec (v2).** `role="img"` with an aria-label updated
  at band boundaries only ("Kiln temperature 573 degrees, quartz
  inversion") — never per frame; a screen reader is told the stage,
  not the digits. The visual value is aria-hidden. The readout never
  overlaps content: bands reserve a 96px bottom-right clear zone at
  ≥768px (§4).
- **Performance budget & mobile variant.** One text update ≤ every
  90ms + one transform on the cone path, inside the shared loop.
  Mobile: as breakpoints.
- **Tokens consumed (v2).** `--temp`, `--ink`, `--celadon-deep`,
  `--ember`, `--stage-word`, `--lerp` (0.12 / 0.09 inversion).

### 6.4 Cooling crossfades — the bands

- **What & why.** The page's architecture in motion. Each band's
  ground is a temperature: the Door band is kiln-dark at 1280°C, and
  as the visitor scrolls, band grounds crossfade through the cooling
  sequence — dark warming to fired clay at the edges, lightening
  through ash, settling at celadon-pale for the Opening. It belongs
  because the sections are not pages in a stack; they are stages of
  one firing, and the ground changing under the content is the firing
  happening around the pieces. Without it the theme is a dark page
  followed by a light page; with it, there is one continuous kiln.
- **Structure.** Each `<section class="band">` carries `data-temp`
  (its band's plateau temperature from §5's schedule) and two stacked
  ground layers: the band's own ground (bottom) and a crossfade layer
  (top, opacity driven by `--cool`, a 0→1 value the shared loop writes
  per band from the band's viewport position). The crossfade layer is
  the *next* band's ground colour, so a band visibly becomes its
  successor as it leaves the top of the viewport. Content sits above
  both layers, always on a ground whose contrast has been audited at
  both ends of the fade (§10).
- **Motion spec.** Scrubbed, per band: `--cool` maps the band's travel
  from "band top at 70% viewport height" (0 — fully its own
  temperature) to "band top at −10%" (1 — fully the next band's
  ground). Lerp per §5 via the shared loop. Band titles rise through
  a line mask as their band enters (translateY 100% → 0, 600ms
  `--ease-cool`, once) — the title comes up like a piece lifted into
  view. No other per-band entrance: the ground *is* the entrance.
- **Choreography timeline (v2).** Spatial, per band: band below fold —
  its own ground, title masked → band entering — title rises 600ms;
  ground still its own → band centred — ground its own, content at
  full rest → band leaving upward — crossfade runs; by the time the
  band's last shelf leaves, its ground has become the next band's, so
  the seam between bands is never a hard line at any scroll position →
  the final band crossfades to celadon-pale and stays (there is no
  next firing on this page).
- **State matrix (v2).** *Rest (no JS):* every band at its own ground,
  seams as designed hard edges between adjacent temperature colours —
  a complete, honest static page (the original entry's "final cooled
  state from first paint" is per-band: each band shows its finished
  ground). *Scrubbing:* per map. *Hover/focus:* grounds do not respond
  to pointer. *Scrolled-past:* a band above the viewport rests at its
  successor's ground (its `--cool` stays 1) — scrolling back down
  re-runs the fade symmetrically. *Disabled:* rest state.
- **Content merge.** The ground is the kiln's atmosphere around the
  pieces in that band; the crossfade is timed to the band's own
  shelves leaving. The effect has no existence separate from the
  sections it joins.
- **Failure fallback.** Grounds are plain CSS colours beneath the
  crossfade layer; if the loop never runs, bands show their own
  grounds with hard seams — readable, audited, merely less alive. If
  a band's `data-temp` is missing, the loop skips it (its ground is
  static) rather than inventing a temperature (§1's law).
- **Reduced-motion variant.** No crossfade. Bands show their own
  grounds; the whole page additionally sits under the fixed mid-cool
  reading the original entry specifies — implemented as the Ash
  band's ground becoming the page's neutral separator colour. Titles
  are unmasked.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: crossfade
  window narrows (70% → 10% travel). <768px: crossfade window narrows
  further and band padding follows §4's thermal rhythm compressed
  ×0.8; the fade remains (it is the theme, not an ornament) but costs
  one opacity write per band per frame, capped at 3 bands in flight.
- **Edge cases & failure modes (v2).** *Content taller than expected
  in a band:* the band grows; its crossfade window is viewport-relative,
  so a long band simply stays at its own temperature longer — correct:
  more ware, longer at temperature. *A band with no successor
  ground defined:* the final band rule above. *Contrast mid-fade:*
  body text colour also crossfades (ash ↔ ink) on the same `--cool`
  value, and the pair is audited at 0 / 0.5 / 1 (§10) — there is no
  scroll position at which text sits at <4.5:1 on its ground.
- **Accessibility spec (v2).** Grounds are decorative; the information
  (which stage) is in the band title text and the log (§6.10).
  Text/ground pairs audited at three fade points (above). Focus
  outlines are drawn in the band's *ink* token, which crossfades with
  the text, so focus is visible at every point of the fade.
- **Performance budget & mobile variant.** Opacity on pre-painted
  layers only; no gradients repaint (grounds are flat colours). Cap:
  3 bands crossfading per frame. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cool`, `--kiln-dark`, `--fired-clay`,
  `--ash`, `--celadon-pale`, `--ease-cool`, `--lerp`.

### 6.5 Shelf placement

- **What & why.** How every product arrives. A piece rises 26px onto
  its kiln-shelf ledge and settles; its contact shadow deepens as it
  lands; the firing number is already written at the shelf's left end.
  It belongs because placement is how pots actually meet shelves — a
  hand sets them down, one at a time, in order — and because the shelf
  is the product presentation itself: ledge, shadow and firing number
  are the frame every piece on the site is sold inside. A grid of
  cards fading in would present the same photographs and say nothing.
- **Structure.** A `<div class="shelf">` per row: the ledge (a 14px
  fired-clay bar with a 1px `--ash`-at-30% top edge and the firing
  number set in Fraunces italic at its left, §3), and above it the
  pieces — `<figure class="piece">` each with its image (§6.13), name
  (H3) and caption beneath the ledge. The contact shadow is a radial
  gradient ellipse under each piece, in `--shadow-contact`, scaling
  with the piece's rise. Pieces are fully rendered at rest on the
  shelf in the DOM; the rise is a JS-armed pre-state
  (translateY(26px), shadow at 30%).
- **Motion spec.** Trigger: the shelf's top crossing 82% of viewport
  height, once. Each piece: translateY 26px → 0 over **520ms
  `--ease-settle`**, stagger **110ms** in shelf order (left to right,
  the order a shelf is loaded — from the kiln's centre outward is the
  studio's habit and is not negotiable per build). Shadow: scaleX
  0.82 → 1 and opacity 0.3 → 0.55 across the same 520ms, so the piece
  visibly *lands*. Watchdog: 1200ms after trigger, any unplaced piece
  snaps to rest.
- **Choreography timeline (v2).** t+0: shelf crosses the line; first
  piece begins → t+110ms × n: each subsequent piece begins → per
  piece: rise 0–380ms, settle overshoot ≤2px at ~440ms (a pot set down
  rocks a fraction), shadow deepens through the settle → t+520ms +
  110ms × (n−1): shelf fully loaded; the firing number (static
  throughout) now reads as the shelf's label, which it always was.
- **State matrix (v2).** *Rest (no JS / pre-trigger):* pieces on their
  shelves, shadows full — the shipped state. *Placing:* per timeline.
  *Placed (terminal):* rest state; never re-runs on scroll-back.
  *Hover:* the piece re-warms (§6.9) — placement is complete and does
  not replay. *Focus:* a focused piece is placed instantly if its
  shelf is mid-placement (focus never waits for a stagger). *Active:*
  the press (§6.12). *Scrolled-past:* placed. *Disabled:* n/a.
  Touch: identical timings; stagger shortens to 80ms (see
  breakpoints).
- **Content merge.** The ledge, shadow and number are the piece's own
  furniture, present in the static page; the animation is the act of
  the piece being set onto furniture that exists without it. Remove
  the motion and the shelf still presents the pot — remove the shelf
  and the motion has nothing to place.
- **Failure fallback.** Pre-state is JS-armed only. Images late: the
  piece's frame (§6.13) holds its aspect ratio on the shelf, shadow
  present, so a late photograph lands on a shelf that was already
  furnished. IO unsupported: shelves ship placed.
- **Reduced-motion variant.** No rise, no stagger. Pieces are on their
  shelves; the shelf is the whole statement.
- **Breakpoints (v2).** ≥1200px: shelves of up to 4 (glaze band) as
  §4. 768–1199px: max 3 per shelf, rise 20px. <768px: one piece per
  shelf (a phone shelf is a single ledge), rise 14px, stagger moot,
  duration 420ms — and the firing number moves beneath the ledge's
  left end so it never collides with the piece's caption.
- **Edge cases & failure modes (v2).** *Piece with no photograph*
  (sold, or still in the kiln): the shelf holds its **stilt mark** —
  a small clay-coloured placeholder silhouette with the caption
  "In the firing — shelf held" and its real firing number; an empty
  gap on a shelf is a lie about the firing, a held place is the
  truth. *Very tall piece (vase, 3:4 or taller):* the shelf's rise is
  unchanged but the band grows; two tall pieces never share a shelf
  (§4 density). *Shelf of one:* no stagger; the single placement is
  the band's beat.
- **Accessibility spec (v2).** Figures are real `<figure>` with
  `<figcaption>` under the ledge; the firing number is text, read as
  part of the caption ("Firing number 214"). Placement is decorative
  motion over announced content; nothing is announced. Touch targets:
  a piece that links is ≥44px in both dimensions by construction
  (smallest piece image 148px wide).
- **Performance budget & mobile variant.** Transforms + one gradient
  scale per piece; cap 4 pieces animating per frame across the page
  (§14). Mobile: as breakpoints.
- **Tokens consumed (v2).** `--fired-clay`, `--shadow-contact`,
  `--ease-settle`, `--place-dur` (520ms), `--place-stagger` (110ms).

### 6.6 Ember rise

- **What & why.** The air above hot content behaves like kiln air.
  In the dark upper bands, ember particles — tiny points of fired
  clay and ember light — rise and wobble, thinning as the page cools
  until, by the celadon band, there are none: the air is cold and
  still. It belongs because it is the only ambient motion in the hot
  half, and it is *metered by the theme's own physics*: particle
  density is a function of the same curve (§5) that drives everything
  else, so the air itself reports the temperature. Ambient loops that
  ignore the page's state are wallpaper; this one is a gauge.
- **Structure.** One `<canvas class="embers">` per hot band (Door,
  Soak, Descent), absolutely positioned over the band's ground, under
  its content, `pointer-events: none`, `aria-hidden`. Particles:
  ≤30 per band (the original entry's cap, kept), 1–2.5px, coloured
  between `--fired-clay` and `--ember-bright`, each with a fixed
  upward velocity (14–30px/s), a lateral wobble (sine, ±6px, period
  2–4s) and a life of one band-height before respawning at the
  band's base. Density per band = round(30 × band-temp/1280), computed
  from `data-temp` — the Descent band (~1100°C) carries ~26, and a
  band below 600°C carries none and gets no canvas at all.
- **Motion spec.** Continuous while the band is within one viewport
  of the reading position (IO-gated); paused when the tab is hidden.
  Drawn inside the shared loop's tick but on its own 30fps throttle
  (embers do not need 60fps and must not steal from the scrub).
  Scrolling does not move particles directly — they rise through the
  band's own air — but a band leaving upward takes its canvas with it.
- **Choreography timeline (v2).** Continuous: band enters → canvas
  fades in over 600ms (the air is already hot; the fade is the
  visitor's eye adjusting, not the fire starting) → steady state:
  particles rise, wobble, expire at the band's top edge, respawn at
  its base → band exits → canvas fades 300ms and its loop slot is
  released (§14's budget: at most 2 canvases live at once).
- **State matrix (v2).** *Rest (no JS):* no canvas; the band's ground
  alone — the shipped state. *Rising:* per density. *Hover/focus:*
  unaffected — embers ignore the pointer entirely (a hand does not
  stir kiln air on a website). *Scrolled-past:* canvas released.
  *Disabled:* n/a. Touch identical; particle count halves on
  <768px (see breakpoints).
- **Content merge.** The embers live in the band's air, above its
  ground and below its type, and their count is the band's
  temperature in another unit. They never cross into a cooler band:
  the canvas is band-bound, so the physics is visible — scroll to
  the boundary and the air changes.
- **Failure fallback.** Canvas unsupported or context creation fails:
  the band simply has still air; nothing else in the theme references
  the embers. Low-power device (loop measuring <40fps sustained): the
  ember system is the first cut in §14's order — density halves, then
  the system is removed entirely, in that order.
- **Reduced-motion variant.** No embers, ever. Still air at every
  temperature — the original entry's ruling.
- **Breakpoints (v2).** ≥1200px: ≤30 per band as specced. 768–1199px:
  ≤20. <768px: ≤12, velocities ×0.8, canvas resolution capped at
  0.75× device pixels (embers are soft points; resolution is waste).
- **Edge cases & failure modes (v2).** *Band shorter than 60vh:* the
  canvas still spans the band; particle life shortens proportionally
  — the air is shallower, the count formula unchanged. *Two hot bands
  adjacent:* two canvases, one per band, densities by their own
  temperatures; the boundary between them is visible in the air,
  which is the point. *Resize:* canvas re-fits its band; particles
  keep their relative positions.
- **Accessibility spec (v2).** Pure decoration, `aria-hidden`, no
  information carried. Particle luminance stays below the band's text
  contrast floor: embers render at ≤0.8 opacity and never behind a
  text block's glyphs at a size >2px (§10 checks a screenshot diff).
  Fully disabled under reduced motion.
- **Performance budget & mobile variant.** ≤30 particles × ≤2 live
  canvases, 30fps throttle, ≤0.5ms/frame total. First item in §14's
  cut order. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--ember`, `--ember-bright`, `--fired-clay`,
  `--temp`, `--ember-max` (30).

### 6.7 Crackle draw

- **What & why.** The dividers between bands are not rules; they are
  glaze surfaces, and as each divider enters, a crackle network —
  the fine crazing pattern that spreads across a cooling glaze —
  draws itself across it over 1.2 seconds. It belongs because crackle
  is what cooling *does* to glaze: the divider between two
  temperatures is exactly where the surface is under tension, and the
  network is the visible record of the temperature drop the visitor
  just scrolled through. A hairline would separate the bands; the
  crackle *explains* the separation.
- **Structure.** Per divider, one inline SVG spanning the content
  column, height 46px, holding a network of 14–22 polylines generated
  at build time from a seeded path set (the network is authored per
  divider in the build's assets — three master networks, rotated and
  mirrored across the page's dividers so no two adjacent dividers
  crack alike). Stroke: the *cooler* band's ink at 34% (crackle is
  seen in the glaze it cools into), width 1px, fill none. Each path's
  length is measured at runtime for the dash animation; the network
  ships fully drawn in the DOM.
- **Motion spec.** Trigger: divider's centre crossing 78% of viewport
  height, once. Paths draw via stroke-dashoffset over **1200ms
  total**, staggered by path length class (long cracks first — the
  primary fractures run, then the fine crazing fills between them:
  long paths start at t+0, medium at t+180ms, fine at t+420ms, each
  path's own draw 500–800ms on `--ease-cool`). Watchdog: 1000ms after
  trigger, all paths force to drawn.
- **Choreography timeline (v2).** t+0: 3–5 long fractures begin →
  t+180ms: medium branches begin, splitting off the fractures'
  midpoints (the path order is authored so branches start where they
  visually attach) → t+420ms: fine crazing begins → t+1200ms: network
  complete; the divider is a finished glaze surface → never redraws,
  including on scroll-back: a crack does not heal.
- **State matrix (v2).** *Rest (no JS):* network fully drawn — the
  shipped state. *Drawing:* 1200ms as above. *Drawn (terminal):*
  static. *Hover/focus:* none. *Scrolled-past:* drawn. *Disabled:*
  rest state. Touch identical.
- **Content merge.** The network is the divider's own surface — the
  divider has no other visual existence. Its density encodes the
  drop across it: dividers above the inversion band carry the full
  22-path network; below it, 14 — less tension left in the page.
- **Failure fallback.** Ships drawn; JS only re-arms the dash state
  for dividers below the fold. SVG unsupported (effectively never):
  the divider falls back to a 1px hairline in the same colour, present
  in markup as the SVG's background.
- **Reduced-motion variant.** Fully drawn, always. No draw animation
  at any temperature.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: height 38px,
  fine paths reduced by a third. <768px: height 30px, only long +
  medium paths (10–12) — crazing finer than a phone pixel is labour
  no one can see.
- **Edge cases & failure modes (v2).** *Divider at the very top of a
  band already in view at load:* draws at load+300ms like any other.
  *Print:* networks print as drawn (they are content — the glaze is
  part of the piece's record). *Path measurement fails (display:none
  ancestor):* the watchdog's force-drawn state is the default anyway;
  measurement failure skips the animation, never the network.
- **Accessibility spec (v2).** Decorative, `aria-hidden`; the band
  change is announced by the band's heading, not by the divider.
  Stroke contrast is against the cooler band's ground at 34% ink —
  decorative exemption, but never used as the sole indicator of
  anything.
- **Performance budget & mobile variant.** Dash animation on ≤22
  small paths, one divider at a time (dividers are ≥60vh apart by
  §4's rhythm). Mobile: reduced path counts above.
- **Tokens consumed (v2).** `--ease-cool`, `--crackle-dur` (1200ms),
  `--hairline`.

### 6.8 Hero piece pin — one vessel, whole firing

- **What & why.** One vessel endures the firing in view. The hero
  piece — the build's signature pot — pins at centre-screen for
  120vh while its glaze story scrolls past in three short chapters
  (the clay, the firing, the glaze) and the background cools around
  it from 1280°C toward the descent. It belongs because the theme
  needs one object the visitor can watch *being fired*: everything
  else on the page is the kiln; this is the ware. The chapters are
  the piece's own record — its clay body, its firing number, its
  glaze recipe — so the pin is a reading position, not a sticky
  advertisement.
- **Structure.** A `<section class="pin">` of 220vh: a 100vh sticky
  stage holding the piece (centred, on a shelf ledge per §6.5, with
  its firing number) and, to its right (≥1200px) or beneath it
  (<1200px), the chapter column: three `<article class="chapter">`
  blocks in normal flow inside the tall section, each ~66vh apart,
  so exactly one chapter is beside the piece at any scroll position.
  The stage's ground is the band crossfade (§6.4) driven by the
  section's own travel — the kiln cools *around* the pinned piece.
- **Motion spec.** Scrubbed by the shared loop. The piece itself does
  almost nothing — that is the point — two things only: its glaze
  sheen (§6.13's scale is separate) cools, a highlight gradient on
  the vessel's shoulder shifting from ember-tinted (at pin start) to
  neutral by pin end, mapped to the section's temperature; and at
  each chapter boundary the piece settles 4px (a shelf tremor as the
  story turns, 300ms `--ease-settle`). Chapters fade/slide as they
  pass the reading line: the active chapter at full opacity, the
  others at 0.35, crossfading over the 20vh around each boundary.
- **Choreography timeline (v2).** Spatial: pin engages (piece reaches
  centre) at 1280°C, chapter 1 (The Clay) active → 40vh of scroll:
  chapter 1 yields to chapter 2 (The Firing — its firing number,
  its soak, its cone) → 80vh: chapter 3 (The Glaze) → 120vh: pin
  releases; the piece scrolls away on its shelf like every other
  piece, now simply the first pot on the page → the Descent band
  begins. Total visitor time in the pin: one deliberate scroll,
  ~4–6s.
- **State matrix (v2).** *Rest (no JS):* no pin — the piece sits on
  its shelf in a normal 100vh hero, chapters stacked beneath it in
  order, all at full opacity: the complete static page. *Pinned:*
  per map. *Hover:* the piece re-warms (§6.9) even while pinned —
  attention works at any temperature. *Focus:* chapters are ordinary
  articles in DOM order; focus is never trapped by the pin (the
  sticky stage is visual only). *Scrolled-past:* released, cooled.
  *Disabled:* rest state. Touch: same map, chapter column beneath
  (breakpoints).
- **Content merge.** The pinned object is the content the chapters
  describe; the cooling ground is the firing the second chapter
  narrates. Remove the piece and the chapters are a story about
  nothing; remove the chapters and the pin is a statue.
- **Failure fallback.** The pin is `position: sticky` enhancement
  over a complete static layout (above). If the loop stalls, the
  chapters rest at the opacities for the current scroll position —
  all three remain readable at ≥0.35, and the watchdog lifts all to
  full opacity if the loop dies 800ms (a stalled story must become a
  readable page, not a dim one).
- **Reduced-motion variant.** No pin, no sheen shift, no chapter
  fading: the static layout — piece on shelf, three chapters stacked,
  all full opacity. The story survives entire; only the endurance
  test is waived.
- **Breakpoints (v2).** ≥1200px: as specced, chapters right. 768–
  1199px: pin shortens to 100vh of travel, chapters beneath the
  piece inside the stage (the active chapter only, crossfading).
  <768px: **no pin** — a phone's viewport is too small to hold a
  vessel and its story; the piece and chapters stack statically,
  sheen shift retained as a scrubbed gradient (cheap, and it is the
  chapter's point).
- **Edge cases & failure modes (v2).** *Chapter longer than its
  slot:* chapters are capped at 60 words by §12's copy law; a longer
  chapter is a gate failure, not a layout problem. *The piece's image
  is portrait-tall:* the stage scales it to ≤62vh; the shelf ledge
  widens instead. *Scroll-back into the pin:* fully symmetric — the
  sheen re-warms as the curve rises; unlike the door, the pin is a
  place, not an event.
- **Accessibility spec (v2).** Reading order: piece (with alt text
  naming the vessel and its firing number) → chapter 1 → 2 → 3,
  regardless of pin state. Inactive chapters at 0.35 opacity remain
  in the accessibility tree in order — visual emphasis only, and
  0.35-opacity ash/ink text still meets 4.5:1 on its ground (audited,
  §10) so low-vision visitors lose nothing. The pin never moves
  focus.
- **Performance budget & mobile variant.** One sticky element, one
  gradient position write + ≤3 opacity writes per frame inside the
  shared loop. Mobile: no pin (above) — the cheapest variant is the
  honest one.
- **Tokens consumed (v2).** `--temp`, `--ease-settle`, `--shadow-contact`,
  `--fired-clay`, `--lerp`.

### 6.9 Re-warm hover

- **What & why.** Attention briefly re-fires the piece. Hovering (or
  focusing) a cooled piece returns a faint ember glow to its rim —
  the rim light of the kiln coming back for half a second's ramp —
  and on leave it cools again. It belongs because it is the theme's
  one hover language, and it is physical: the piece responds to being
  looked at the way a pot responds to the door opening — a breath of
  heat on its edge. A lift, a shadow-grow or a scale would be
  furniture-store language on a potter's shelf.
- **Structure.** Each `.piece` carries a rim layer: an inset box-shadow
  stack on the image frame (inset 0 0 0 1px ember at 0 → visible,
  plus an outer 0 0 22px ember at low opacity), driven by a `--warm`
  custom property (0 → 1) transitioned in CSS. The rim follows the
  image's own contour (the frame is the image's box; §6.13), so the
  glow belongs to the piece's silhouette, not to a card rectangle.
- **Motion spec.** Trigger: pointerenter / focus-within on the piece.
  `--warm` 0 → 1 over **500ms `--ease-cool`** (heat arrives the way
  heat leaves — fast, then settling). Peak: rim at ember 0.5 opacity,
  outer glow 0.18 — *faint* is a spec value, not a mood (§9 fails
  builds whose re-warm reads as a neon sign). On leave: 1 → 0 over
  700ms (cooling is slower than warming; the asymmetry is the
  physics). No transform, no layout, ever.
- **Choreography timeline (v2).** t+0: pointer rests on the piece →
  t+150ms: rim first visible → t+500ms: full faint warmth; the
  piece's caption firing number warms one step (fired-clay → ember
  at text-safe size only, §2) → hold: warmth steady while hovered;
  it does not pulse or breathe (a held temperature, not a beacon) →
  leave: 700ms cool to rest.
- **State matrix (v2).** *Rest:* `--warm` 0. *Hover (desktop):* per
  timeline. *Focus-within:* identical to hover — keyboard attention
  warms exactly as pointer attention does. *Active:* the press
  (§6.12) overrides — warmth holds at 1 while pressed. *Scrolled-past:*
  rest. *Touch:* no hover; a tap that follows the piece's link goes
  straight through (no first-tap warm tax); a long-press (≥400ms,
  non-link pieces) warms while held. *Disabled piece (sold):* warms
  to 0.4 only — a sold pot is another's now; the shelf note says so,
  and the glow agrees.
- **Content merge.** The glow is on the piece's own rim, and its
  caption's number warms with it: the effect is the piece and its
  record responding together. It cannot be applied to a text block or
  a button — §11 gives buttons their own, cooler language.
- **Failure fallback.** Pure CSS custom-property transition; if
  unsupported, the rim snaps (still capped at the same opacities).
  No JS involved at all.
- **Reduced-motion variant.** The rim appears/disappears instantly at
  the same capped opacities (state change without transition) —
  information (this piece is being attended to) survives; the thermal
  ramp rests.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: outer glow
  14px. <768px: rim only, no outer glow (a phone screen's pieces are
  close together; glow would bleed onto neighbours).
- **Edge cases & failure modes (v2).** *Pointer skims a shelf of
  four:* a 90ms intent delay before warming begins, so a diagonal
  pass doesn't light the whole shelf like a runway; leaving within
  the delay cancels cleanly. *Two pieces focused/hovered in
  sequence:* each cools on its own 700ms — a shelf may briefly hold
  two cooling rims, which reads as a shelf just handled, correctly.
  *Piece in the hot bands:* re-warm is capped by band — above 800°C
  the rim adds nothing (the piece is already hot; `--warm` multiplies
  the band's remaining coolth, computed in CSS from `--temp`).
- **Accessibility spec (v2).** The warm state is never the only
  indicator of focus: the piece's link carries the theme's focus ring
  (2px celadon-deep outline, offset 3px) in addition. Rim contrast is
  decorative. Focus-within parity is mandatory (above).
- **Performance budget & mobile variant.** One custom-property
  transition per piece, compositor-friendly (box-shadow is paint —
  capped at one warming piece at a time by the intent delay; budget
  ≤1.5ms/frame during the ramp). Mobile: rim only.
- **Tokens consumed (v2).** `--warm`, `--ember`, `--fired-clay`,
  `--ease-cool`, `--warm-dur` (500ms), `--cool-back-dur` (700ms).

### 6.10 Firing-log navigation

- **What & why.** Navigation in this theme is the kiln book: the
  written log every firing keeps — time, temperature, what the
  potter saw. On ≥1200px a slim rail pins at the left edge listing
  the page's bands as log entries ("14:20 — 1,280°C — soak begins"),
  each entry stamped with its band's plateau temperature from the
  same curve (§5). The entry for the band in view is written in ink;
  the rest sit in pencil-grey. On smaller screens the log becomes the
  header: a single line — the current entry — above the band title.
  It belongs because a firing is navigated by its record, and because
  the log is the static, printable form of the readout (§6.3): the
  schedule as a document, not an instrument.
- **Structure.** A `<nav class="log">`: an ordered list of entries,
  one per band, each an anchor to its band, containing a time (the
  firing's clock, authored content — the schedule's real times), the
  plateau temperature, and the stage name. Times are the schedule's:
  the firing starts 06:10, peaks 15:40, inversion at 19:05, opening
  next morning 07:30 — a 25-hour firing, which is what cone-10
  stoneware takes; the log says so, and the numbers must sum (§10).
  The current entry is marked by scroll position via the shared
  loop's band index.
- **Motion spec.** Entries never animate in — a log is written, not
  performed. The current-entry marker (a 2px fired-clay rule at the
  entry's left) moves between entries with a 240ms `--ease-settle`
  slide as bands change. On entry change, the new entry's temperature
  figure does a single 300ms roll from the previous entry's value —
  a replay between two true values, the only counter motion the log
  permits itself. Header variant (<1200px): the current entry line
  crossfades 160ms on change.
- **Choreography timeline (v2).** Per band change: t+0: new band
  crosses the reading line → t+0–240ms: marker slides → t+60ms: the
  figure roll begins → t+360ms: log at rest, new entry in ink. No
  other motion exists in this element, by design.
- **State matrix (v2).** *Rest:* all entries present, first in ink.
  *Current:* ink + marker. *Hover (entry):* the entry's temperature
  warms one step (§6.9's language at text scale). *Focus:* standard
  ring; marker does not follow focus (it reports scroll, not
  attention). *Scrolled-past entries:* pencil-grey, still links.
  *Disabled:* a band with no content does not get an entry (the log
  records what happened). Touch: header variant; entries are ≥44px
  rows in the expanded log sheet (below).
- **Content merge.** The entries *are* the bands' schedule — time,
  temperature and stage name are the same data the readout reports
  and the bands enact. Generate the log from the bands' `data-temp`
  and titles at build time; a hand-maintained second copy will drift,
  and drift is a gate failure (§10).
- **Failure fallback.** A plain anchor list; without JS every entry
  sits in ink (no current marker) and the list still navigates. The
  log is the no-JS visitor's map of the firing — it must be complete
  without any machinery.
- **Reduced-motion variant.** Marker snaps; figure roll replaced by
  an instant swap. Nothing else changes.
- **Breakpoints (v2).** ≥1200px: left rail, pinned, entries stacked.
  768–1199px: header line variant. <768px: header line + a "Log"
  button opening the full list as a sheet under the header (300ms
  `--ease-settle` slide, Esc closes, focus returns to the button).
- **Edge cases & failure modes (v2).** *More bands than the rail
  holds (>8):* entries compress (time omitted, temperature + stage
  remain) rather than shrinking type below 12px. *A band added by a
  CMS:* the log rebuilds from band data at build; runtime-injected
  bands without `data-temp` are excluded from the log and flagged by
  §10's audit in CI, never silently numbered.
- **Accessibility spec (v2).** Real `<nav aria-label="Firing log">`;
  current entry carries `aria-current="true"`. Entries are links
  with ≥28px height on desktop rail, ≥44px in the mobile sheet. The
  figure roll is visual only; entry text is complete in the tree at
  all times.
- **Performance budget & mobile variant.** One transform + one text
  swap per band change; nothing per frame. Mobile: header variant.
- **Tokens consumed (v2).** `--fired-clay`, `--ink`, `--ease-settle`,
  `--temp`.

### 6.11 Shelf piece card

- **What & why.** The listing unit: a piece presented for sale or
  record, standing on its own short shelf. Where §6.5 places pieces
  in editorial shelves, the card is the catalogue form — image
  (§6.13), name, glaze line, firing number, and one fact that matters
  (its price, its dimensions, or "sold" — in that priority). It
  belongs in shelf form because in this world there are no floating
  cards; there are pots on shelves, and a listing is a shelf with
  more pots on it.
- **Structure.** `<article class="piece-card">`: shelf ledge (as
  §6.5, card-width), figure on it, then the record block beneath the
  ledge: H3 name, glaze line ("Celadon over ash, cone 10"), the
  firing number, and the fact line. The whole card is one link
  (stretched over the name) unless it carries the reserve action
  (§6.14's form anchor), in which case two explicit targets.
- **Motion spec.** Entry: §6.5's placement at card scale (rise 18px,
  460ms). Hover/focus: re-warm (§6.9) on the figure; the record
  block does not move. Active: the press (§6.12). Nothing else — a
  card that also lifts, tilts and shadows is a shop template wearing
  a pot.
- **Choreography timeline (v2).** Entry per §6.5 scaled; hover per
  §6.9; the card adds no beats of its own, which is its discipline.
- **State matrix (v2).** *Rest:* on shelf, cooled. *Hover:* figure
  warmed. *Focus:* warmed + ring on the name link. *Active:* pressed
  (§6.12). *Scrolled-past:* placed, cooled. *Sold (disabled):* the
  figure desaturates to its ash state (saturate 0.55), the fact line
  reads "Sold — Firing № 214", re-warm capped at 0.4 (§6.9), and the
  card is not a link. Touch: no hover; tap follows the link.
- **Content merge.** Every part is the piece's record: its photograph,
  its glaze, its firing, its price. The shelf is not a frame around
  the card; the card *is* a shelf segment.
- **Failure fallback.** Static shelf card; the no-JS card is the
  finished card.
- **Reduced-motion variant.** No placement rise; re-warm instant
  (§6.9's variant).
- **Breakpoints (v2).** ≥1200px: cards in shelves of 3–4, spans
  varied by piece aspect (a tall vase takes a double-height shelf
  slot — never crop a pot to a grid). 768–1199px: shelves of 2–3.
  <768px: one per shelf, record block full width.
- **Edge cases & failure modes (v2).** *Missing image:* the stilt-mark
  held place (§6.5's rule) with "In the firing" — never a stock
  photo, never a grey box. *Long glaze line:* wraps to two lines;
  the ledge and figure never resize for text. *Price changes:* the
  fact line is server-rendered; no client-side price theatre.
- **Accessibility spec (v2).** One link per card named by the piece's
  full name + firing number. The figure's alt names the vessel and
  glaze ("Ash-glazed yunomi, Firing № 214"). Sold state is text, not
  colour alone.
- **Performance budget & mobile variant.** Inherits §6.5/§6.9 caps.
  Mobile: one per shelf.
- **Tokens consumed (v2).** `--fired-clay`, `--shadow-contact`,
  `--warm`, `--ease-settle`.

### 6.12 Press-into-shelf click

- **What & why.** The theme's click, from the original entry: pressing
  a piece seats it — the piece dips 3px into its shelf and its
  contact shadow deepens and spreads, the way a hand presses a pot
  down to feel it sit true on the shelf. It belongs because it is the
  only honest press feedback in a pottery: not a ripple, not a
  bounce — weight, briefly applied, on the object itself. It pairs
  with links and with the reserve action: the press is the moment of
  commitment, performed on the ware.
- **Structure.** A transform + shadow change on `.piece` (the same
  nodes §6.5 placed): translateY 0 → 3px, shadow scaleX 1 → 1.12 and
  opacity 0.55 → 0.7, over the press. Implemented in CSS on `:active`
  and on a `.pressing` class for keyboard activation (Enter/Space on
  the piece's link gets the same 160ms, fired by JS on keydown so
  keyboard visitors feel the seat too).
- **Motion spec.** Press: **160ms `--ease-press`** down. Release:
  260ms `--ease-settle` back — a pot is lifted off its seat more
  gently than it was pressed. If the press activates navigation, the
  release is cut by the transition (§6.16) — the piece stays seated
  as the door closes, which reads correctly.
- **Choreography timeline (v2).** t+0: pointer down / key down →
  t+160ms: fully seated, shadow at full spread → hold: seated while
  held (no creep, no pulse) → release: 260ms rise → t+420ms: rest.
- **State matrix (v2).** *Rest:* standing. *Hover:* warmed (§6.9),
  standing. *Focus:* warmed + ring, standing. *Active:* seated as
  above, desktop and touch identical. *Scrolled-past:* standing.
  *Disabled (sold):* no press — a sold pot is not handled; the cursor
  and the shelf note agree.
- **Content merge.** The press acts on the piece and its own shadow;
  the shadow is the piece's contact with its shelf (§6.5). Nothing
  outside the piece's shelf segment changes.
- **Failure fallback.** `:active` CSS only; if transforms are
  unavailable the shadow change alone carries it.
- **Reduced-motion variant.** No dip; the shadow deepens instantly on
  active (state shown, motion waived).
- **Breakpoints (v2).** All: dip 3px. <768px: dip 2px (pieces are
  smaller; the seat is shallower).
- **Edge cases & failure modes (v2).** *Press-and-drag off the
  piece:* release fires wherever the pointer lifts; the piece rises
  — no stuck seats (a `pointercancel` handler is mandatory in the
  JS path; the CSS path cannot stick). *Rapid repeated presses:*
  each restarts from current position; no queue.
- **Accessibility spec (v2).** The press is feedback, not state —
  nothing is announced; activation itself follows the link/button's
  native semantics. Keyboard parity via the `.pressing` class is a
  build requirement, audited in §10.
- **Performance budget & mobile variant.** One transform + one shadow
  on one element. Free, at every size.
- **Tokens consumed (v2).** `--ease-press`, `--ease-settle`,
  `--shadow-contact`, `--press-dur` (160ms).

### 6.13 Image scale-in-frame & heat shimmer

- **What & why.** Two image treatments sharing one frame. **Scale-in-
  frame:** as a piece is placed (§6.5), its photograph settles from
  1.06 to 1.0 inside its frame — the pot arriving slightly large in
  the hand and being set down at its true size. **Heat shimmer:** in
  the cool bands only, a finished piece's photograph carries a barely
  perceptible shimmer above its shoulder — heat still leaving the
  glaze, the last sign of the firing — implemented as a 6px-tall
  gradient layer above the image whose background-position oscillates
  ±3px over 7s. Together they belong because both are the photograph
  behaving like the object: arriving handled, cooling quietly.
- **Structure.** Each piece figure is a frame (`overflow: hidden`,
  aspect ratio from the photograph's real dimensions — reserved in
  markup, so placement never shifts layout) holding the `<img>` and,
  for shimmer-eligible pieces (cool bands, §6.4's data-temp < 300°C),
  a `.shimmer` layer pinned to the frame's top 18%. The scale is
  driven with the placement (same trigger, same clock); the shimmer
  is a CSS animation, IO-gated by a class from the shared loop.
- **Motion spec.** Scale: 1.06 → 1 over **700ms `--ease-settle`**,
  starting 80ms after the piece's rise begins (the pot is placed,
  then it settles in the hand's grip). Shimmer: background-position
  ±3px, **7s ease-in-out infinite alternate**, opacity 0.10 max —
  felt before seen; a shimmer a visitor can point at is too strong
  (§9). Paused off-screen, paused on hover (the re-warm's stillness
  is the point of hover, §6.9), never on pieces in hot bands (their
  air is §6.6's embers — a piece gets one atmosphere, not two).
- **Choreography timeline (v2).** t+0 (§6.5 trigger +80ms): scale
  begins → t+700ms: image at true size; if the piece is in a cool
  band, shimmer fades in over 1s → continuous: 7s oscillation →
  hover: shimmer pauses within 200ms → leave: resumes.
- **State matrix (v2).** *Rest (no JS):* image at scale 1, no shimmer
  layer — the shipped state. *Settling:* 700ms. *Settled:* scale 1,
  shimmer running if eligible. *Hover/focus:* shimmer paused, scale
  holds. *Scrolled-past:* shimmer paused off-screen. *Disabled:* n/a.
  Touch: scale identical; shimmer runs (it is not hover-gated there).
- **Content merge.** The scale happens inside the piece's own frame
  and the shimmer rises from the piece's own shoulder. The frame
  never moves; the photograph is handled within it.
- **Failure fallback.** Images ship at scale 1; the loop adds the
  unset state only to images it will actually drive. Late image: it
  arrives at scale 1 (no retroactive settle — a pot photographed
  late is not re-handled).
- **Reduced-motion variant.** No scale, no shimmer. The photograph is
  a photograph.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: scale from
  1.04. <768px: scale from 1.03, shimmer opacity 0.07, layer height
  12% — smaller frames, smaller weather.
- **Edge cases & failure modes (v2).** *Image smaller than its frame
  (low-res asset):* scale-in is disabled for that piece (scaling a
  soft image advertises its softness); the gate (§10) flags the
  asset instead. *Shimmer over a dark glaze photograph:* opacity cap
  drops to 0.06 (the layer is light; on dark glaze it would read as
  fog, not heat).
- **Accessibility spec (v2).** Decorative; alt text unaffected. The
  scale never crops the vessel's rim or foot — frames are composed
  with 8% bleed in the asset itself, so the 1.06 state crops into
  bleed, never into the pot.
- **Performance budget & mobile variant.** Transform on the img +
  one background-position animation per eligible visible piece, cap
  4 shimmering pieces per frame budget. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--ease-settle`, `--settle-img-dur`
  (700ms), `--shimmer-cycle` (7s).

### 6.14 The firing book — reserve / commission form

- **What & why.** The conversion form is the firing book's open page:
  the ledger where a visitor writes their name against a piece. It
  sits in the Opening band (40°C — you do not sign a ledger inside a
  hot kiln), set as ruled ledger lines on ash, its submit button
  stamped like a kiln-book entry: "Enter in the book". It belongs
  because reserving a pot from a firing *is* a ledger act in a real
  studio — name, piece, firing number, entered by hand — and the
  form's confirmation is an entry in that book, not a toast.
- **Structure.** `<form class="book">` inside the Opening band:
  fields as bottom-ruled inputs (transparent ground, 2px ink rule,
  labels above in Work Sans caps), the piece field pre-filled from
  the card the visitor came from (name + firing number, read-only —
  the book already knows which pot), one checkbox drawn as an empty
  shelf square that fills with celadon and a clay tick when checked
  ("Write to me when the next kiln opens"), and the submit as a
  stamp-button (§6.12's press at form scale). On success the form is
  replaced by its ledger entry: the visitor's line, ruled, stamped
  "Entered — Firing № 214" in celadon-deep at −4°.
- **Motion spec.** Entry: the book's page is a shelf (§6.5 places it,
  rise 18px). Field focus: the rule thickens 2px → 3px and a celadon
  line slides beneath it from the left, 200ms `--ease-settle`. Error:
  the rule turns `--ember` — the one place ember is permitted in the
  cold half, because an error is a small fire — the ground washes
  ember at 6%, and the error note writes in beneath in the book's
  voice (§12), 45ms per word, capped 600ms. Submit press: stamp
  160ms `--ease-press`; success stamp fades/scales in 300ms
  `--ease-settle`.
- **Choreography timeline (v2).** Per field: focus → rule + line
  200ms. On submit: t+0 stamp press → t+160ms: form dims to 0.5
  (the book is being written in) → response: success — entry replaces
  form over 300ms, stamp lands at +120ms of that → error — the
  offending field's rule fires ember, note writes in, focus moves to
  the field; the visitor's text is never cleared, on any error,
  including a server 500 (the book does not lose entries).
- **State matrix (v2).** *Rest:* ruled, empty (or piece pre-filled).
  *Focus:* rule + celadon line. *Filled:* rule at ink full weight.
  *Error:* per above. *Submitting:* dimmed, submit disabled, stamp
  held. *Success (terminal):* the ledger entry. *Disabled:* a piece
  already reserved shows the book closed — the entry that exists,
  read-only, with "This piece is entered to another name." Touch:
  fields ≥48px tall, stamp full-width.
- **Content merge.** The form's fields are the ledger's columns; the
  pre-filled piece line is the card's own data (§6.11) carried into
  the book. The confirmation restates the visitor's actual entry —
  name, piece, firing number — because it is a copy of a record, not
  a success message.
- **Failure fallback.** A plain HTML form that posts without JS; the
  ledger entry is then a server-rendered page in the same layout.
  No-JS loses the stamp, never the booking.
- **Reduced-motion variant.** No stamp, no write-in: errors and the
  entry appear instantly, rules change weight only.
- **Breakpoints (v2).** ≥1200px: two-column ledger (piece column
  fixed, visitor column flexible). 768–1199px: single column, piece
  line on top. <768px: single column, stamp full-width, rules 44px+
  touch rows.
- **Edge cases & failure modes (v2).** *Arriving without a piece
  (general commission):* the piece field becomes a select of pieces
  in the current firing — the book's one select, styled as a ruled
  line (§11). *Double submit:* the stamp disables at first press;
  a second entry for the same piece+name is the same entry (server
  idempotency is a build requirement noted in §15). *Sold-out firing:*
  the form is the closed book (disabled state above) plus the
  next-firing checkbox alone — the book still takes names for the
  next firing, which is true and useful.
- **Accessibility spec (v2).** Labels are real `<label>`s; errors are
  `aria-describedby` on their field and announced once via a polite
  live region ("The book could not take that line — the email ends
  mid-word"). Focus order = ledger order. The stamp is decorative;
  the entry's text is the confirmation, in the tree.
- **Performance budget & mobile variant.** CSS transitions + one
  class swap; the write-in is capped at 600ms regardless of note
  length. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--ink`, `--celadon`, `--celadon-deep`,
  `--ember`, `--ease-settle`, `--ease-press`, `--stamp-dur` (160ms).

### 6.15 Ash footer — the opening, written up

- **What & why.** The footer is the cold kiln, unloaded and recorded.
  At 40°C the page ends the way a firing ends: the shelves stand
  empty in celadon-pale, the firing's curve is drawn as a signature
  line (the schedule the page actually ran, §5, as an SVG sparkline
  with the inversion plateau visible in it), and the colophon states
  the firing's facts — its number, its peak, its duration, how many
  pieces came out. It belongs because a firing that is not written up
  did not finish; the footer is the write-up, and its curve is the
  one honest summary of everything the visitor scrolled through.
- **Structure.** `<footer class="opening">` on celadon-pale: the
  curve SVG (full content width, 64px tall, stroke celadon-deep
  1.5px, the plateau segment drawn thicker — the careful part of the
  firing is the emphasised part), beneath it the colophon in three
  columns (the firing: number, peak, hours; the studio: name,
  address, the potter's mark; the book: links as log entries per
  §6.10's voice), and a final line: "Cooled and opened. Nothing on
  this page is still hot."
- **Motion spec.** The curve draws once on entry, 900ms
  `--ease-cool`, plateau segment last (it is drawn in firing order:
  ramp, soak, descent, plateau emphasised by a second pass at 300ms,
  final fall). Links hover per §6.10. Nothing else moves in the
  footer — a cold kiln is still, and the stillness after §6.6's air
  and §6.4's fades is the final content statement (compare §9).
- **Choreography timeline (v2).** t+0: footer enters → curve draws
  0–900ms in firing order → t+900–1200ms: plateau second pass →
  rest, permanently.
- **State matrix (v2).** *Rest (no JS):* curve fully drawn, colophon
  complete — the shipped state. *Drawing:* 1200ms once. *Hover:*
  log-entry links per §6.10. *Focus:* rings in celadon-deep.
  *Scrolled-past:* n/a (it is the end). *Disabled:* n/a. Touch
  identical.
- **Content merge.** The curve is generated from the same schedule
  data as §5/§6.3/§6.10 — a fourth printing of one record. The
  colophon's figures (peak, hours, pieces) are the firing's real
  figures from the build's content; invented footer statistics are
  a gate failure like any other invented figure.
- **Failure fallback.** Static footer; the curve is inline SVG,
  present without JS.
- **Reduced-motion variant.** Curve drawn; no second pass.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns, curve full width above. <768px: one column, curve 44px
  tall, plateau still emphasised.
- **Edge cases & failure modes (v2).** *Schedule data missing a
  plateau (a raku build, §1's re-declared schedule):* the curve
  draws the schedule that exists; the emphasis pass follows the
  declared danger point of that schedule (for raku, the reduction
  moment) — the mechanism is "emphasise the careful part", the
  plateau is this build's instance.
- **Accessibility spec (v2).** The curve is `role="img"` labelled
  "The firing curve: 1,280 degrees, held, cooled slowly through 573,
  opened at 40." Colophon columns are real headings + lists. The
  final line is plain text, in order.
- **Performance budget & mobile variant.** One SVG draw, once. Free.
- **Tokens consumed (v2).** `--celadon-pale`, `--celadon-deep`,
  `--ink`, `--ease-cool`.

### 6.16 Stoke transition — page change

- **What & why.** Leaving a page closes the kiln door and opens it on
  the next: a kiln-dark sheet sweeps from the left (the door swinging
  shut, 260ms), the route swaps beneath it, and the door opens onto
  the new page — which begins, as every page in this theme does,
  inside its own firing, its hero already cooling. It belongs because
  navigation here is not teleportation between documents; it is
  moving ware between chambers, and the door is the only honest way
  through a kiln wall.
- **Structure.** One fixed `.stoke` element (kiln-dark, with the
  seam-glow at its leading edge — the crack's light, §6.1, at 30%
  intensity), parked off-canvas left. It enhances internal `<a>`
  clicks only; modified clicks, new-tab and external links bypass it
  entirely.
- **Motion spec.** Total **520ms**: cover 260ms `--ease-door`, swap
  at full coverage, reveal 260ms (the sheet exits right — the door
  swings through, it does not reverse). The incoming page's door
  (§6.1) does *not* re-run after a stoke (the visitor is already
  inside the firing); its headline cooling (§6.2) starts at reveal
  +200ms. Watchdog: 430ms after cover begins, any incomplete
  transition is torn down and the destination shown plainly.
- **Choreography timeline (v2).** t+0: click; sheet enters → t+260ms:
  full coverage; route swaps; new page at scroll top → t+520ms:
  sheet gone; focus moves to the new page's H1 → t+720ms: headline
  cooling begins (§6.2).
- **State matrix (v2).** *Idle:* parked. *Covering/revealing:* per
  timeline; outgoing page inert during cover. *Hover/focus:* links
  behave normally until activation. *Disabled (no JS):* ordinary
  navigation. Touch identical.
- **Content merge.** The door is the same door as §6.1's — the site's
  one door, used at load and at every passage. Its seam-glow is the
  hero crack's light, dimmer: a door being passed through, not
  opened for the first time.
- **Failure fallback.** Slow destination (>3s at full coverage): the
  sheet holds with the readout's stage word replaced by "stoking…"
  in the sheet's corner — up to 3s, then the transition aborts, the
  sheet retreats (200ms), and native load proceeds. The theme never
  traps a visitor inside a door.
- **Reduced-motion variant.** No sweep: instant navigation with a
  120ms kiln-dark outline flash on the hero to mark the chamber
  change.
- **Breakpoints (v2).** All sizes: 520ms. <768px: 440ms.
- **Edge cases & failure modes (v2).** *Same-page anchors:* no stoke;
  the anchor scrolls (smooth per §5's lerp, instant under reduced
  motion). *Back/forward:* no stoke — the browser's gesture rules.
- **Accessibility spec (v2).** Outgoing page inert from cover start;
  destination live at reveal with focus on its H1 (tabindex −1) and
  a polite announcement "Into the next chamber: [page name]".
  Skipped entirely under reduced motion.
- **Performance budget & mobile variant.** One transform on one fixed
  element. Mobile: 440ms.
- **Tokens consumed (v2).** `--kiln-dark`, `--ember`, `--ease-door`,
  `--stoke-dur` (520ms).

### 6.17 Unfired skeleton — bisque loading

- **What & why.** Loading states are unfired ware. A shelf whose
  content is still loading shows the pieces as **bisque** — the pale,
  matte, once-fired blanks: shelf ledge present, piece silhouettes in
  ash at bisque texture (flat, no glaze sheen, no photograph), caption
  lines as unlettered rules. As content arrives each piece *fires*:
  its photograph crossfades in and its glaze sheen (§6.13) settles —
  the blank becomes the finished pot. It belongs because in this
  world an unfinished object is not an abstraction; it is a real
  earlier state of the same object, and bisque is exactly that.
- **Structure.** The real shelf markup (§6.5) with `.is-bisque`:
  figures hold their aspect-ratio frames filled with the bisque
  silhouette (an inline SVG of the piece's form class — vase, bowl,
  cup, plate — in ash with a 1px clay edge), captions as 60%-width
  rules. Content swap replaces children in place; the shelf never
  resizes.
- **Motion spec.** Per piece, on content landing: bisque → photograph
  crossfade **380ms `--ease-cool`** with the sheen settle (§6.13)
  compressed into the same window. **Hard cap 1200ms:** any piece
  still bisque at 1200ms has its silhouette stripped to plain ash
  (the standing law: no object stays abstract if the machinery
  fails) and receives its content plainly when it comes. Fetch error:
  the piece resolves to the stilt-mark held place (§6.5) with the
  caption in the error voice (§12).
- **Choreography timeline (v2).** t+0 (fetch starts): shelf renders
  bisque → per piece on landing: 380ms firing crossfade → t+1200ms:
  watchdog strips any remaining silhouettes to ash blocks → content
  arriving later lands plainly, no crossfade (the kiln has closed).
- **State matrix (v2).** *Bisque:* silhouettes + rules, `aria-busy`.
  *Firing:* 380ms. *Fired:* normal shelf behaviour (§6.5 onward).
  *Stripped:* plain ash, awaiting content. *Hover/focus:* bisque
  pieces are not interactive. *Disabled:* server-rendered pages ship
  fired; bisque exists only inside client fetches that own their
  watchdog.
- **Content merge.** The skeleton is the shelf's own unfired self —
  same ledge, same geometry, same firing number (the number is known
  before the photograph: it is in the log). Zero layout shift by
  construction.
- **Failure fallback.** As the hard cap above; a bisque shelf without
  JS is never rendered (the shell must not emit `.is-bisque` it
  cannot fire).
- **Reduced-motion variant.** Bisque is plain ash blocks (no
  silhouette, no crossfade — content appears, with a 120ms opacity
  fade at most).
- **Breakpoints (v2).** All sizes identical; <768px caption rules
  reduce to two per piece.
- **Edge cases & failure modes (v2).** *Piece form class unknown:*
  the generic cylinder silhouette is used — bisque blanks are
  approximate by nature. *Content arrives before first paint:*
  no bisque is shown at all (never flash a skeleton for <100ms).
- **Accessibility spec (v2).** Loading shelves carry `aria-busy="true"`
  until fired; the shelf region announces once, politely: "The shelf
  is still in the kiln." Silhouettes are `aria-hidden`.
- **Performance budget & mobile variant.** Silhouettes are inline SVG
  ≤1KB each, reused by form class. No image payload.
- **Tokens consumed (v2).** `--ash`, `--fired-clay`, `--ease-cool`,
  `--fire-dur` (380ms), `--fallback-strip` (1200ms).

### 6.18 The cold kiln — 404 & empty states

- **What & why.** A missing page is a cold, empty kiln: the visitor
  opened a door on a chamber with nothing in it. The 404 is a single
  shelf, empty except for one stilt mark and a line in the book's
  voice: "This shelf is empty. Firing № 214 held no such piece." —
  with the log (§6.10) offered as the way back to shelves that exist.
  Empty states (a firing with no pieces left, a shelf all sold) use
  the same furniture: the empty shelf, honestly drawn, never a
  cartoon and never a stock photograph of somebody else's pottery.
- **Structure.** The Opening band's ground (the kiln is cold — an
  error is not a hot place), one shelf (§6.5's ledge, no pieces), the
  stilt mark centred, the line set in Fraunces, and two log-entry
  links: "To the current firing" and "To the firing book" (§6.14).
  Temperature readout (§6.3), if present, reads 40°C COLD — the one
  time the readout's joke is also its information.
- **Motion spec.** Almost none, deliberately: the shelf places
  (§6.5) with nothing on it — the ledge rises alone, 520ms — and that
  small emptiness, performed once, is the whole animation budget of
  the page. The stilt mark does not move.
- **Choreography timeline (v2).** t+0: page paints (cold ground) →
  shelf ledge settles 520ms → rest. Total motion on the page:
  520ms, once.
- **State matrix (v2).** *Rest:* the empty shelf, complete without
  JS. *Hover/focus:* the two links per §6.10. All other states n/a.
  Touch identical.
- **Content merge.** The empty shelf is the theme's own furniture
  stating an absence in the theme's own terms; the line names the
  firing the visitor asked about (from the URL's piece reference
  where the build can know it, else the current firing).
- **Failure fallback.** This *is* the fallback page; it must render
  with no JS, no fonts and no images — text, a ledge (CSS), a stilt
  mark (inline SVG).
- **Reduced-motion variant.** The ledge does not rise. Identical
  otherwise.
- **Breakpoints (v2).** All sizes: one shelf, centred, max 640px.
- **Edge cases & failure modes (v2).** *Empty shelf in a live listing
  (all sold):* the shelf stands with every piece in §6.11's sold
  state plus the line "Every piece from Firing № 214 is entered to
  another name." and the next-firing checkbox (§6.14) — an ending
  that still takes names.
- **Accessibility spec (v2).** The heading is the line itself ("This
  shelf is empty"); links are plainly named. Nothing decorative is
  announced.
- **Performance budget & mobile variant.** The lightest page on the
  site, by law: ≤40KB total.
- **Tokens consumed (v2).** `--celadon-pale`, `--fired-clay`,
  `--ease-settle`.

## 7. Page application map

- **Home.** The full firing as specced: door (§6.1), pinned vessel
  (§6.8), bands descending through the inversion to the Opening, the
  book (§6.14) in the cold half, the write-up footer (§6.15). The
  home page is the only page that runs the complete 1280 → 40 curve.
- **Listing (a firing's shelves).** Enters already cooling: the curve
  starts at the firing's unloading temperature (the page declares
  `data-temp-start`, typically 300°C — the ware is out and being
  sorted). Shelves of cards (§6.11) in the ash and glaze bands; the
  log (§6.10) lists shelves, not stages. No door, no pin — a listing
  is a workplace, not a ceremony.
- **Detail (one piece).** The piece gets a band of its own at its
  firing's plateau temperature, cooling to the book (§6.14) below:
  its photograph large (§6.13), its chapters (clay, firing, glaze —
  §6.8's three, unpinned), its shelf-mates as one shelf of cards at
  the foot ("From the same firing").
- **About (the studio / the potter).** Told as the kiln's history:
  bands are firings past ("Firing № 1 — the kiln we built"), the
  readout follows the studio's own first firing schedule, declared
  in the log. Portraits sit on shelves like pieces — people in this
  theme are also work.
- **Contact / checkout equivalents.** The firing book (§6.14) is the
  only conversion surface; a basket, if the build has one, is a
  "shelf list" in the Opening band — pieces held at 40°C, in the
  book's voice, with no hot elements anywhere near payment (§9).
- **404 / empty.** The cold kiln (§6.18).
- **Print.** The log (§6.10) prints as the schedule table; bands
  print at their own grounds (backgrounds on) or, if the reader's
  printer strips them, the page remains fully legible in ink on
  white — audited in §10.

**Per-page curves.** Only the home page runs the firing itself. Every
other page type declares its own start point on the *same* schedule
and cools from there: a detail page for a piece from Firing № 214
starts at that firing's plateau only if the page is the piece's
unveiling (a kiln-opening announcement); a routine detail page starts
at 300°C like the listing, because the ware is already out. What no
page may do is invent a private curve: start points are chosen from
the schedule's named moments (peak, unloading 300°C, sorting 120°C,
cold 40°C), the readout's stage words follow the same bands, and a
page that starts cold — the 404 (§6.18), a help page, the book's
confirmation — runs no curve at all and shows no readout. Consistency
of the instrument matters more than its presence: a visitor who
learns on the home page that the readout never lies must find that
true on every page that carries one, which is why §10's audits run
site-wide, not per page.

## 8. Worked examples

### 8.1 The hero — "The door opens on Firing № 214"

*Build: a studio pottery home page for a wood-fired stoneware maker.*
t+0: the page paints kiln-dark; the hero beneath the armed door
already holds the H1 "Fired at 1,280 degrees. Cooled like it
mattered." in ink-on-dark legibility (ash), the vessel — a 34cm
ash-glazed vase, Firing № 214 — on its shelf, the readout at 1,280°C
SOAKING. t+300ms: the spy-hole flares (§6.1). t+400–2000ms: the crack
widens on `--ease-door`; behind it the headline's ember overlay
(§6.2) is already glowing, so the first thing the widening light
reveals is the title at full heat. t+2000ms: door gone; §6.2's cool
is at its fired-clay crossing; the flicker is 800ms away. t+3200ms:
the last word — "mattered." — flickers once and the headline is ink.
The visitor scrolls: the pin (§6.8) holds the vase while chapter 1,
"The clay is dug two valleys over," crosses the reading line; the
readout begins its fall. Every number on screen — 1,280, № 214, the
34cm in the caption — is the maker's real data, and the schedule in
the log (§6.10) sums to the 25 hours the firing actually took.

### 8.2 Mid-page — the Quartz Inversion band

*The page's quietest 13%.* The band's ground is ash darkening toward
its coolest value; the copy is three short paragraphs and one shelf
of two pieces. The readout, entering the band, slows — the shared
lerp drops to 0.09 (§5) and the visitor can *feel* the page take
care: scroll resistance is identical, but every scrubbed value now
moves as if through thicker air. The band's title, risen through its
mask, is "573° — where silica turns". The copy explains, in the
book's voice, that quartz in the clay shrinks suddenly at 573°C and
a kiln cooled carelessly through it cracks its ware from inside —
dunting, the failure you hear as a ping in the night. The two pieces
on the shelf are the firing's survivors of a past dunting, and their
captions say which firing taught the studio this band. The crackle
divider leaving the band carries only 14 paths (§6.7): the tension
is nearly out of the page. A visitor who reads nothing learns the
shape of the lesson from the pacing alone; a potter who reads it
checks the number, finds 573, and trusts the rest of the site.

### 8.3 Conversion — entering a name in the book

*The Opening band, 40°C.* The visitor arrives from the vase's card
(§6.11) via "Enter your name for this piece". The book (§6.14) sits
on its shelf, the piece line already ruled in: "Ash-glazed vase,
34cm — Firing № 214 — £480". The visitor's fields are empty ledger
lines. They type an email missing its ending; on submit the stamp
presses (160ms), the form dims, and the email's rule fires ember —
the cold half's one permitted flame — while the note writes in
beneath in 45ms words: "The book could not take that line — the
address ends mid-word. Write it whole and we will enter it." Their
text is intact. They fix it; the stamp presses again; the form is
replaced by its own ledger entry, ruled and complete, stamped at
−4° in celadon-deep: "Entered — Firing № 214". Below the entry, one
line: "We write once, when the kiln opens. No other letters." The
readout in the corner reads 40°C, COLD. The firing, and the sale,
are finished the same way: by being written down.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Ember as a brand colour.** Ember buttons, ember links, ember
   badges down the whole page. Ember is a *temperature*, rationed to
   ≤6% of pixels and banned below the Descent band (§2). Cure: ember
   appears only where something is hot — the crack, the cooling
   headline, a re-warmed rim, one form error.
2. **A gradient wallpaper.** A static orange-to-green CSS gradient
   behind unrelated content, with the readout faked as decoration.
   The cooling must be the bands' own grounds on the declared curve
   (§6.4, §5); if the temperature can be deleted without changing
   any content's meaning, it was wallpaper.
3. **Invented temperatures.** "1280°" in the hero, "900°" on a badge,
   "peak heat!" in a headline — numbers that match neither the curve
   nor each other. The gate's three-records audit (§10) exists for
   this. Cure: one schedule, four printings (§6.3, §6.4, §6.10,
   §6.15), zero freehand numbers.
4. **Cards that float.** Pieces in rounded rectangles with drop
   shadows and hover lifts. In this theme ware stands on shelves
   (§6.5) and the only hover is heat (§6.9). A floating card is a
   shop template; a shelf is a kiln.
5. **Flame clip-art and fire emojis.** Any literal flame icon,
   animated GIF fire, or 🔥 in copy. The theme's fire is light,
   colour and particles metered by physics (§6.6) — never a picture
   of fire.
6. **Particles everywhere.** Embers in the cold half, embers behind
   the form, embers in the footer. Density is a function of
   temperature (§6.6); an ember below 600°C is a lie about the air.
7. **The door as a preloader.** A branded splash that plays while
   assets load, unrelated to the hero. §6.1's door *is* the hero's
   reveal, capped at 1600ms + watchdog, and never gates content that
   is not the hero.
8. **Crackle as texture pack.** The same crackle PNG tiled behind
   headings. Crackle lives only on dividers (§6.7), drawn, denser
   where the drop is greater.
9. **Hot checkout.** Any ember, glow or urgency language near
   payment. Conversion happens at 40°C in a ledger (§6.14); heat
   near money is pressure, and pressure is slop with a temperature.
10. **Speed where the kiln is careful.** Fast crossfades through the
    inversion band, a readout that spins through 573°C like an
    odometer. The curve's plateau and the 0.09 lerp (§5) are the
    theme's respect for its material; flattening them flattens the
    meaning.

## 10. Quality gate

**Blocking — all must pass:**

1. **One-schedule audit.** Extract every temperature stated anywhere
   in the build (readout curve, band `data-temp`s, log entries,
   footer figures, copy). All must lie on the single declared
   schedule; any freehand number fails the build.
2. **Three-records agreement.** The readout (§6.3), the log (§6.10)
   and the footer curve (§6.15) are generated from the same schedule
   data; a diff between any two fails.
3. **Log arithmetic.** The firing log's times sum to the stated
   firing duration; the peak in the log equals the peak in the
   colophon.
4. **No-strand test.** With JS disabled, and again with the rAF loop
   killed at 800ms, every band is fully readable at its own ground;
   the door, headline overlay and bisque states are absent or
   resolved.
5. **Contrast at the fade.** Body text vs ground audited at
   `--cool` = 0, 0.5, 1 for every band (§6.4): ≥4.5:1 at all three.
6. **Ember ration.** Ember-token pixels ≤6% of the hero viewport and
   zero ember below the Descent band (screenshot audit).
7. **Firing-number truth.** Every firing number on the page comes
   from content data and is consistent across shelf, card, form and
   footer; a number generated in JS fails on sight.
8. **Reduced-motion completeness.** With `prefers-reduced-motion`,
   the page presents the fixed mid-cool palette, no pin, no embers,
   no crossfades — and loses no content, verified by a text diff
   against the full-motion page.

**Standard — should pass, fix before ship if not:**

9. Watchdogs verified by fault injection (door 1500ms, cool 1500ms,
   reveals 1200ms, bisque 1200ms).
10. Ember canvas count: ≤2 live, ≤30 particles each, 30fps throttle.
11. Keyboard press parity (§6.12) and focus-warm parity (§6.9)
    tested with keyboard only.
12. Print check: log table legible, bands legible without
    backgrounds.
13. The five-word test (§4): each hot band's content statable in
    five words.

## 11. Component inventory

| Component | Themed treatment |
|---|---|
| Primary button | A **stamp** (§6.14): ink-ruled rectangle, Work Sans caps, presses with §6.12's seat (translateY 2px + rule deepens). Celadon-deep in the cold half; in hot bands, ash on kiln-dark. Never ember-filled. |
| Secondary button | A ruled ledger line with text — a link that behaves like an entry, underline drawing 160ms on hover. |
| Text input | Ledger line (§6.14): transparent, 2px bottom rule, label above in caps 11px. |
| Select | The book's one select (§6.14 edge case): ruled line, native arrow replaced by a small clay triangle; options are pieces in the current firing. |
| Checkbox | Empty shelf square (14px, 2px clay rule) filling celadon with a clay tick (§6.14). |
| Radio | Witness cones: small cone outlines, the chosen one filled and bent 12°. |
| Table | The firing log itself (§6.10): ruled rows, tabular Work Sans, temperature column right-aligned, no zebra — alternating row *temperature* (ground warms 2% toward clay on peak rows) instead of striping. |
| Badge | A **cone stamp**: small rotated (−3°) outline stamp stating a fact from the record ("Cone 10", "Firing № 214"). Facts only; a badge that markets ("Best seller!") is refused. |
| Alert | A line in the book (§6.14's error voice): ember rule in the cold half, ash rule in the hot half, note written in the book's voice. Never a floating box. |
| Toast | **Refused.** Nothing in a kiln pops up and vanishes. Replacement: the ledger entry (§6.14 success) or a line added to the log. |
| Modal | **Refused** above the waist of the page. Replacement: the piece's detail is a page (§7); the mobile log sheet (§6.10) is the one permitted overlay, because it is the nav, not content. |
| Tabs | **Refused.** A firing has stages, not tabs. Replacement: bands, navigated by the log. |
| Accordion | A **shelf that lowers**: a section whose ledge drops 8px as its content shelf is revealed beneath it (300ms `--ease-settle`) — used for firing notes and care instructions. |
| Pagination | Log entries: "Earlier firing / Later firing" as dated entries (§6.10's voice), never numbered page chips. |
| Progress bar | **Refused.** The readout (§6.3) is the progress. |
| Spinner | **Refused.** Loading is bisque (§6.17). |
| Tooltip | **Refused.** Replacement: the caption under the shelf — information lives under the piece it describes. |
| Breadcrumb | The log path: "Firing № 214 › The Soak › This piece" as one ruled line. |
| Card | The shelf piece card (§6.11). No other card exists. |
| Hero | The door + pinned vessel (§6.1, §6.8) on home; a single shelf at the page's declared start temperature elsewhere (§7). |
| Footer | The ash footer (§6.15). |
| 404 / empty | The cold kiln (§6.18). |
| Search | An index of the book: a ruled input in the Opening band listing matching log entries (pieces by name, glaze, firing) — results are entries, not cards. |

## 12. Content & copywriting voice

**The book's voice.** The site speaks as the kiln book is written:
plain, dated, numerical, unhurried. Short declarative sentences.
Every claim of heat carries its number. The potter is "we"; the
visitor is addressed only in the book's courtesies ("Write your name
and we will enter it"). Nothing is "amazing"; a glaze is "ash over
celadon, cone 10, held twenty minutes" and that is the praise.

- Headlines: a fact of the firing, written so the last word can bear
  the flicker (§6.2). ✓ "Fired at 1,280 degrees. Cooled like it
  mattered." ✗ "Hot new drops just landed!!"
- Labels: the stage, the temperature, the number. ✓ "The Soak —
  1,280°C". ✗ "Featured collection".
- Piece names: the maker's names. ✓ "Ash-glazed Yunomi, Firing
  № 214". ✗ "Premium Ceramic Cup — Best Seller".
- **Error voice** (the book, apologising for its own line): ✓ "The
  book could not take that line — the address ends mid-word. Write
  it whole and we will enter it." ✗ "Invalid email!!"
- **Empty voice**: ✓ "This shelf is empty. Firing № 214 held no such
  piece." ✗ "Oops! Nothing here."
- **Confirmation voice**: ✓ "Entered — Firing № 214. We write once,
  when the kiln opens." ✗ "Success! You're on the list 🎉"
- **Banned words:** hot (unquantified), drop, amazing, premium,
  limited-time, hurry, 🔥 and every fire emoji, "artisanal" (the
  work says it or it isn't true).
- **Owned words:** firing, soak, cone, shelf, entered, cooled,
  opened, the book, dunting (used once, explained, in the inversion
  band — the theme's signature honesty).

## 13. Full-page scroll choreography map

1. **The door (0–3.5s, time-based).** Spy-hole flare, crack widens,
   headline revealed at full ember, flicker at ~3.2s, headline ink
   by ~5s. The visitor feels: *I have opened something that was
   already happening.*
2. **The soak (p 0–0.10).** The vessel pins (§6.8); chapters 1–2
   cross the reading line; the readout holds 1,280°C — the page's
   only stillness at full heat. Embers at full density (§6.6).
3. **The firing chapter (pin, ~40vh in).** Chapter 2 names the
   vessel's number and soak; the piece settles 4px at the chapter
   boundary — the story's turn, felt in the object.
4. **The descent (p 0.10–0.45).** Pin releases; the first shelves
   place their pieces (§6.5); grounds begin their crossfade (§6.4);
   the readout falls ~9°C per 100px. Crackle divider: 22 paths.
5. **Quartz inversion (p 0.45–0.58).** The lerp thickens to 0.09;
   the readout crawls; the band is quiet, two pieces, the dunting
   story (§8.2). The visitor slows without knowing why.
6. **Ash (p 0.58–0.75).** Density rises: shelves of three and four,
   the log's middle entries, ember count at zero — the air has
   changed and the page is now a workplace.
7. **Glaze (p 0.75–0.88).** Celadon enters the grounds; shimmer
   (§6.13) on finished pieces; cards at their most catalogue-like,
   still on shelves.
8. **The opening (p 0.88–1).** 40°C. The book (§6.14) on its shelf;
   the curve draws in the footer (§6.15); the final line. The
   visitor feels the specific calm of a finished process — nothing
   on the page is still hot, including them.
*Reverse pass:* scrolling up re-runs the curve symmetrically (bands
re-heat, readout rises) except the irreversible acts: the door does
not close, placed pieces stay placed, cracks stay cracked. A firing
can be re-read; it cannot be un-fired. *Jump scroll:* anchor jumps
snap all scrubbed values to the curve at the landing position within
one frame (§6.3's rule); one-time acts at skipped bands are marked
done, not queued.

## 14. Whole-page performance budget

- **Assets:** ≤520KB total initial (fonts subset: Fraunces optical
  72pt + Work Sans, ≤110KB; hero vessel image ≤140KB; all other
  piece images ≤60KB each, lazy below the Descent band). Inline SVG
  (crackle masters, silhouettes, cone) ≤18KB.
- **Frame budget:** the shared loop ≤2.2ms/frame on a mid phone:
  curve + readout ≤0.3ms, band crossfades (≤3 in flight) ≤0.5ms,
  embers (30fps throttle, ≤2 canvases) ≤0.5ms, pin + chapters
  ≤0.4ms, headroom 0.5ms. Long tasks: none >50ms after load; the
  door's clip-path is compositor-only.
- **Cut order** (when the budget is exceeded, cut in this order,
  never out of it): 1) ember density halves, then embers off;
  2) shimmer (§6.13) off; 3) crackle draw becomes instant-drawn;
  4) band crossfade window narrows; 5) headline glow spread caps
  halve. **Never cut:** the schedule/readout, shelf placement, the
  book, any fallback or watchdog.
- **Measuring it.** The budget is checked on a mid-range Android
  (the studio's buyers are not on flagship phones) over a throttled
  4G profile, scrolling the full home page at a steady read: the
  loop's per-frame cost is sampled from the Performance API across
  the inversion band specifically, because that is where crossfade,
  pin release and ember fade coincide — the page's most expensive
  13%. If the frame cost passes there, it passes everywhere; a build
  that benchmarks only the hero has measured the one place the kiln
  does nothing but glow.

## 15. Build-order checklist

1. Build the static cold page first: all bands at their own grounds,
   shelves furnished, book working as a plain form, log complete.
   This is the no-JS deliverable — ship-shape before any motion.
2. Declare the schedule as data (one file: curve points, band
   plateaus, log times) and generate readout curve, log and footer
   curve from it (§10's three-records rule is a build step, not a
   hope).
3. Wire the shared rAF loop (lerp 0.12 / 0.09 inversion) writing
   `--temp` and per-band `--cool`; verify the readout against the
   schedule at 20 scroll positions.
4. Band crossfades (§6.4) + text-colour crossfades; audit contrast at
   0 / 0.5 / 1 per band.
5. Shelf placement (§6.5) + scale-in-frame (§6.13) + press (§6.12) +
   re-warm (§6.9).
6. The pin (§6.8) with its static fallback verified by disabling
   sticky.
7. Crackle dividers (§6.7) from the three authored masters.
8. Ember canvases (§6.6) with density from `data-temp`; verify the
   600°C cut-off.
9. The door (§6.1) and headline cooling (§6.2) with both watchdogs;
   fault-inject each.
10. Bisque skeletons (§6.17) inside the client fetch paths only.
11. Stoke transition (§6.16); verify modified-click bypass.
12. Reduced-motion pass: fixed mid-cool palette, no pin/embers/
    crossfade; text-diff against the full page (§10 item 8).
13. The book's error and success paths, including server-500 text
    preservation (§6.14).
14. Run §10's gate — blocking items first, signed by someone who did
    not build the page. The sign-off is recorded in the build's own
    log, with the date and the firing number of the content it
    shipped against — this theme's paperwork habit applies to its
    builders too, and a gate that leaves no entry was never run.
