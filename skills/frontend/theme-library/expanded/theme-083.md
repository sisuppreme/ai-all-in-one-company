# 83. The Tide Engine — Expanded (v1 + v2)

Identity preserved exactly from the original entry: a Victorian
tide-predicting machine — brass gears, pulleys, and a pen drawing
next year's tides — reimagined as a website. Same five palette
anchors (engine brass `#A67C2E`, tide slate `#33424E`, chart buff
`#EDE3CB`, pen ink `#263238`, harbour red `#A63D2F`). Same two type
families (Fraunces display, Newsreader body and predictions,
tabular figures throughout). All 9 original signature elements are
deepened, not redesigned — the pen-drawn curve, the floating
headline, the ratio-true gears, the breathing layout, the
high-water stamps, the harmonic counters, the pulley hover, the
click-to-stamp, and the honest footer — plus 9 page-family
elements (§6.10–§6.18) to reach 18 fully specified elements.

**The theme's one law: the machine computes; it does not
decorate.** Every figure on the page — every curve, counter,
stamp, table row and footer time — is drawn from one declared set
of harmonic constants, the Constants Plate (§6.11), printed on the
page itself. A number that cannot be re-derived from that plate
is forbidden, however pretty. The corollary, felt everywhere:
**nothing is in a hurry.** The fastest motion on the page is a
stamp landing; everything else moves at tidal speed.

Standing rules held throughout: normal system cursor only; the
DOM ships complete and printed (every drawn, stamped or flooded
state is a JS-armed enhancement over finished content, each with
a named watchdog); one shared rAF lerp loop (0.10) drives all
scrubbed values; per-element reduced-motion variants; and the
anti-filler law — nothing enters from outside the machine room:
no waves clip-art, no anchors-and-rope kitsch, no generic
"nautical" dressing. The sea is present only as mathematics.

---

## 1. Concept & world

The Tide Engine is a website built as a working tide-predicting
machine of the Kelvin type: a brass engine of gears, pulleys,
cams and a travelling pen that sums harmonic constituents and
draws the tide curve for a named harbour. The visitor does not
read *about* the machine; the visitor reads the machine's output,
and the machine is visibly running — gears turning in the
margins at mechanically true ratios, the pen drawing the curve
the headline floats on, the whole page breathing on a compressed
tidal cycle. The page predicts, mechanically, and its rhythms
are tidal: content ebbs and floods, sections are stamped as the
water reaches them, and the footer prints tomorrow's real tide
times for the harbour the site serves.

The world is specific: chart buff paper, engraved dial borders,
pen ink, harbour red reserved for the marks water and men leave
on charts. It is 1876 engineering drawn with 2026 tools, and it
never winks about it. There is no cartoon brass, no steampunk
costume, no sepia filter. The machine's dignity is that it is
*correct*: the gear teeth mesh, the curve is a true sum of its
constituents, the footer times are the hero curve's own output
read at tomorrow's date. Correctness is the aesthetic.

**Best-fit sites and audiences.**

- **Harbour authorities and port services** — berthing, pilotage,
  lock and sill times, dredging windows: organisations whose real
  product is a timetable written by the moon.
- **Tidal energy** — barrage, lagoon and in-stream turbine firms
  whose output literally follows the constituents this page
  draws; the hero curve is their generation curve's cousin.
- **Coastal services** — ferry operators on tidal routes, boatyards,
  sailing schools, lifeboat and coastwatch charities, tidal-pool
  and pier attractions whose opening is a tide state.
- **Slow-luxury hospitality** — tidal island hotels, causeway
  retreats, oyster and seaweed farms with visiting hours set by
  the ebb: places where "you can only arrive at low water" is
  the luxury, not the inconvenience.
- **Publishers of almanacs and chart data** — where the prediction
  table (§6.12) is the product and the machine is its honest
  frame.

**When NOT to use it.**

- Anything whose promise is speed. A same-day courier, a trading
  floor, a breaking-news desk: the theme's whole argument is
  that the important things run on a 12h25m cycle and cannot be
  hurried. Forcing it makes the brand sound slow, not wise.
- Sites with no real tidal or cyclical data. The law requires a
  Constants Plate; a business that cannot declare one honest set
  of recurring numbers (tides, seasons, kiln firings, market
  days) has nothing for the machine to compute, and the theme
  collapses into costume. This is the theme's hardest gate
  (§10, check 1).
- High-density transactional interfaces — comparison tables,
  checkout funnels, dashboards. The theme routes checkout OUT
  (§7); its one conversion is a stamped request (§6.15).
- Audiences who need information in under five seconds in an
  emergency. Storm and safety information must never wait for a
  pen to draw; the theme explicitly refuses live-ops and safety
  content (§6.10 state matrix).

**The emotional register.** Unhurried confidence. The visitor
should feel what a harbourmaster feels looking at a well-kept
chart room: everything here has been computed by people who
respect the water, nothing will surprise them, and the next
hundred years of tides are already, in principle, on the drum.
The page never shouts, never discounts, never counts down to
anything except high water.

---

## 2. Palette

Five anchors from the original entry, seven derived tokens. The
ground is chart buff — this is a light theme, a paper machine;
there is no dark-mode inversion (§2, dark behaviour). Contrast
ratios below are computed from the hex values for this expansion.

| Token | Hex | Role | Usage ratio | Pairing / contrast |
|---|---|---|---|---|
| `--buff` | `#EDE3CB` | Chart buff — the page ground, plate faces | ~62% | Ground for ink (10.3:1) and slate (8.1:1) |
| `--ink` | `#263238` | Pen ink — body text, drawn curve, table figures | ~18% | On buff 10.3:1 — the text pairing |
| `--slate` | `#33424E` | Tide slate — deep plates, footer sea, dial faces | ~12% | Buff on slate 8.1:1; slate on buff 8.1:1 |
| `--brass` | `#A67C2E` | Engine brass — gears, dial rims, engraved display | ~6% | On buff 3.0:1 — display ≥28px and marks only, never text |
| `--red` | `#A63D2F` | Harbour red — stamps, high-water marks, the seal | ~2% | On buff 4.9:1 — the one accent allowed to carry small text |

**Derived tokens.**

| Token | Hex | Derivation / role |
|---|---|---|
| `--buff-shade` | `#DFD0A8` | Buff in plate shadow — engraved recesses, table flood banding, skeleton plates. On buff 1.3:1 — surface only, never text. |
| `--buff-line` | `#C9B78D` | Hairline engraving on buff — dial ticks, plate rules, chart grid. Never text. |
| `--brass-bright` | `#C09A4A` | Polished brass — gear tooth highlights, needle tips, hover states of brass parts. On buff 2.4:1 — marks only. |
| `--brass-deep` | `#7E5E22` | Engraved brass darkened by ink — dial numerals and brass-register labels. On buff 4.7:1 — the only brass allowed to set text, ≥13px, letterspaced. |
| `--slate-deep` | `#26333D` | The footer sea at depth — footer ground, 404 plate. Buff on it 9.2:1. |
| `--ink-soft` | `#263238` at 68% | Secondary text on buff (captions, plate notes) — composite ≈5.4:1. Never below 68%. |
| `--red-deep` | `#843024` | Harbour red in shadow — stamp edges, pressed-seal rim. Text use forbidden; red text is `--red` only. |

**Palette laws.**

1. **Red is rationed by meaning, not by taste.** Harbour red
   appears only where water or a human hand has marked the
   chart: high-water stamps (§6.5), the visitor's own stamp
   (§6.8), the seal on a confirmation (§6.15), the flood line
   on the tide staff (§6.17). Maximum three red elements per
   viewport; the §10 gate counts them. A red button, a red
   sale badge, a red link — each is a §9 failure.
2. **Brass never sets body text.** At 3.0:1 on buff it cannot.
   Brass is metal: gears, rims, needles, rules. Where a label
   must live on a brass part, it is engraved in `--brass-deep`
   (4.7:1) or cut through to buff.
3. **The curve is ink, always.** The drawn tide (§6.1) is
   `--ink` at full strength on buff. Constituent curves beneath
   it are ink at 18–30% — visible as workings, never competing.
   A coloured curve (teal, gradient, glow) is a §9 failure.
4. **Flood banding is shade, not colour.** Table rows and plates
   distinguish flood from ebb with `--buff-shade` banding and a
   red edge tick at high water — never with blue "water"
   washes. The sea is not blue anywhere on the page; it is
   slate when it must be a surface at all.
5. **Dark behaviour: the machine room at night, not an
   inversion.** There is no `prefers-color-scheme: dark`
   variant. Two plates are natively dark — the footer sea
   (`--slate-deep`) and the 404 (§6.18) — because the chart
   room's day is paper. A build that inverts the theme has
   misunderstood it: brass on black is a nightclub, not an
   engine room.

---

## 3. Typography

Two families, as in the original entry. **Fraunces** sets display
— it has the engraved, slightly maritime serif character of a
chart title cartouche, and its optical sizes let a headline feel
cut rather than printed. **Newsreader** sets predictions and
body — a reading serif with honest old-style figures for prose
and, critically, a clean tabular set for the tables. No third
family is admitted; data numerals are Newsreader tabular, dial
numerals are Fraunces at display settings or Newsreader tabular
engraved in `--brass-deep`.

**Type scale (desktop, ≥1200px).**

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Cartouche (hero headline) | Fraunces 72pt opsz | 64px / 1.02 | −0.01em | Floats on the waterline (§6.2); never more than 3 lines |
| Plate title (H2) | Fraunces 48pt opsz | 40px / 1.08 | −0.005em | Set like an engraved plate heading, centred on its plate |
| Section head (H3) | Fraunces | 27px / 1.15 | 0 | Always paired with its state-of-tide label (§4) |
| Body | Newsreader | 18px / 1.58 | 0 | Measure 34–38em; the reading column is a chart column |
| Prediction text | Newsreader | 17px / 1.5 | 0 | Times and heights inside prose still tabular |
| Table figures | Newsreader tabular | 15px / 1.45 | 0.01em | All tide tables, counters, footer times — tabular always |
| Dial & plate labels | Newsreader caps | 12.5px / 1.3 | 0.14em | Engraved register; `--brass-deep` on brass, `--ink-soft` on buff |
| Stamp text | Fraunces small caps | 13px / 1.2 | 0.06em | High-water marks and seals (§6.5, §6.15) |

**Type laws.**

1. **Every numeral that reports the tide is tabular.** Times,
   heights, ranges, counts of predictions — if a digit can
   change, it is set tabular so columns never shiver. Prose
   numerals in running text may be old-style; the moment a
   number is *data*, it is tabular. The §10 gate greps the
   tables for proportional figures.
2. **A tide time is never printed without its harbour and its
   height.** "06:12" alone is forbidden anywhere on the page —
   the format is `HW 06:12 · 4.87 m · Aldermouth`. A time
   without a place is a rumour; the machine does not deal in
   rumours.
3. **Fraunces never sets a table, a form label or an error.**
   Display type is the cartouche and the plate titles. Tables
   and forms are Newsreader, because the machine's working
   documents were set by clerks, not engravers.
4. **Headlines are statements of fact, not promises.** The
   cartouche register is declarative and dated: "Tomorrow's
   tides for Aldermouth, drawn tonight." Superlatives,
   exclamation marks and countdown language are forbidden
   (§12 gives the voice rules in full).
5. **Engraved labels are rationed.** The letterspaced caps
   register is for dials, plates and stamps only — never for
   body emphasis, never for buttons longer than three words.
   A page where everything is engraved is a page where nothing
   is.

**Responsive type.** <768px: cartouche 40px/1.05, plate titles
30px, body 17px/1.55, table figures 14px. The tabular law does
not relax at any size; columns narrow, digits never switch
sets.

---

## 4. Layout language

The page is a chart laid on the engine-room table, and its
spine is the pen arm and its drawn curve: the curve enters in
the hero, continues as the margin tide staff (§6.17) down the
whole page, and resolves in the footer (§6.9), where the same
constants print tomorrow's times. A visitor who reads nothing
but the margins has still read the tide.

**Plates, not sections.** Content lives on chart-buff plates —
rectangles of `--buff` with a double engraved border (an outer
rule in `--buff-line`, an inner rule offset 6px, corners squared
like a chart's neatline) — laid over a slightly deeper buff
ground. Plates are never rounded, never shadowed with blur;
depth is shown by the engraved double rule and by a 2px offset
`--buff-shade` underlay on the south-east edges, as if each
plate were a sheet laid on the one beneath. Cards (§6.14) are
small plates; the prediction table (§6.12) is the largest plate
on most pages.

**The margins are the machine room.** At ≥1200px, the left
margin (184px) carries the gear clusters (§6.3) pinned at two
stations and the tide staff (§6.17); the right margin (184px)
carries the pen arm's continuation and the high-water stamps
as they land (§6.5). Content never enters the margins and the
machine never enters the content column — except the stamps,
which cross the plate edge by exactly 14px, because that is
where water leaves its mark: over the edge.

**Spacing breathes.** The vertical rhythm is a base 8px grid,
but plate gaps carry the tidal breath (§6.4): gap values are
computed as `base + breath`, where breath oscillates ±6px on
the compressed cycle (one full 12h25m breath ≈ 90s, §5). The
rhythm is specified here as layout, executed by §6.4, and it is
the only layout property on the page that moves with time
rather than scroll.

**Section choreography.** Sections alternate flood and ebb in
register, announced by the turning slate (§13): a flood section
leads with its highest figure (the range, the height, the
count); an ebb section leads with what the water leaves behind
(the method, the constants, the workings). Density follows the
same alternation — flood plates are figure-dense (tables,
counters), ebb plates are prose-loose (method, story) — so the
page's information density itself tides.

**Density and whitespace rules.** Whitespace is chart margin:
it exists so the engraved work can be read, and it is never
filled with decoration. Maximum plate width 1180px; reading
column 38em centred inside its plate; tables may run the full
plate width. One plate per viewport height is the target
density on desktop; a plate taller than 160vh must be split at
a turning slate.

**Grid.** 12 columns inside the plate at ≥1200px (gutter 24px),
8 at 768–1199px (gutter 20px), 4 below 768px (gutter 16px).
The margins-as-machine-room exist only ≥1200px; below that the
machine folds into the plates (§6.3, §6.17 breakpoints).

---

## 5. Full motion system

One engine drives everything: a single requestAnimationFrame
loop, lerp factor **0.10** — deliberately heavy, because brass
has momentum — writing every scrubbed value (gear angles, pen
progress, staff fill, breath phase) from one scroll sample and
one clock. No element runs its own loop. The loop sleeps when
the tab is hidden and when the page is idle at a parked state
for >4000ms, waking on scroll, hover or the breath's next
quarter-phase.

**Named easings** (the machine's five):

| Easing | Curve | Used for |
|---|---|---|
| `--ease-flood` | cubic-bezier(0.45, 0.00, 0.55, 1.00) — a true sinusoidal swing, fast mid-tide, slow at the turns | Counters' visual easing where the harmonic function itself is not drawn, plate rises, staff fill |
| `--ease-slack` | cubic-bezier(0.70, 0.00, 0.30, 1.00) with a specified 120ms dwell at 50% | Anything that must hesitate at the turn: headline settle, slate turns, label swaps |
| `--ease-stamp` | cubic-bezier(0.20, 1.40, 0.40, 1.00) — fast down, one 2px paper overshoot, dry settle in 90ms | Stamps (§6.5, §6.8), the seal (§6.15), tick marks |
| `--ease-haul` | cubic-bezier(0.30, 0.60, 0.60, 1.00) — a pulley taking up load: slow bite, steady pull | Pulley-rope hover (§6.7), plate lifts, drawer-of-charts openings |
| `--ease-draw` | linear — a pen does not ease | Curve drawing (§6.1), staff line growth, engraved line-draws |

**Every motion term, translated into the machine's language:**

- **Scroll-triggered reveals.** Plates do not fade up. A plate
  is *laid on the table*: it arrives with a 240ms `--ease-haul`
  settle of 6px and its engraved border draws (stroke-dashoffset,
  `--ease-draw`, 480ms) as it lands. Content inside is visible
  from the first frame — the draw decorates the frame, never
  gates the words.
- **Scroll-driven / scrubbed animation.** The gears (§6.3), the
  pen's continuation (§6.1), the tide staff (§6.17) and the
  stamp thresholds (§6.5) are all scrubbed from the one loop.
  Scroll *is* the machine's hand-crank: turn it and the engine
  turns, at ratios stated per element.
- **Parallax.** Two depths only, both mechanical: margin gears
  counter-rotate (that is their parallax — they move *against*
  the page), and constituent curves beneath the summed curve
  (§6.1) lag the pen by their phase — parallax as mathematics,
  not as drifting layers. No background layer translates at a
  fractional scroll rate anywhere on the page.
- **Pinned sections.** Two pins are licensed: the pen arm across
  the hero curve's continuation (§6.1, ~180vh) and the constants
  plate beside the weekly table (§6.11/§6.12, table height).
  Nothing else pins. A pin in this theme is a machine part held
  in the frame while work passes under it.
- **Smooth scrolling.** Native scroll, unsmoothed — the lerp
  lives in the values, not in the scroll position. Hijacking
  the wheel to imitate a crank is forbidden; the crank is a
  metaphor the values obey, not a trap for the visitor's hand.
- **Progress indicator.** The tide staff (§6.17): a vertical
  curve in the left margin filling toward a red high-water line
  that sits at the current section's flood point. Progress is
  read as water level, never as a percentage bar.
- **Staggered reveals.** Table rows (§6.12) and constants
  (§6.11) enter in reading order at 40ms intervals — the order
  a clerk reads a ledger, top to bottom, never a centre-out
  burst. Maximum stagger window 400ms regardless of row count.
- **Masked reveals.** The curve's draw is the only mask: content
  that must "reveal" does so by being drawn (§6.1) or stamped
  (§6.5). Text is never masked by a sliding panel — words on a
  chart are printed, and print is either there or not.
- **Kinetic typography.** One licensed instance: the headline
  floating on the waterline (§6.2). No other type moves. A
  theme whose machine is calm does not have nervous letters.
- **Marquee.** Refused. A tide table does not scroll sideways;
  the nearest licensed relative is the endless drum (§6.12's
  table continuing onto next week's plate), which moves at the
  visitor's pace or not at all.
- **Counters.** Harmonic (§6.6): values follow the summed
  constituent function between their endpoints — fast at
  mid-tide, slow at the turn — never a linear or generic
  ease-out tween.
- **SVG line-draw.** The pen curve (§6.1), dial borders (§4),
  the footer's route of the pen (§6.9), the staff (§6.17). All
  `--ease-draw`, all drawn over content that is already legible.
- **Image scale-in-frame.** Photographs (§6.13) settle from
  1.06 to 1.00 inside their engraved frames across the plate's
  flood window — the image is a chart being laid flat, not a
  zoom effect.
- **Hover / magnetic / tilt micro-interactions.** Hover is the
  pulley (§6.7): things are *hauled*, rising ≤3px as a rope
  tightens. Magnetic pull and tilt are refused — brass machine
  parts do not lean toward visitors, and charts do not tilt on
  the table.
- **Custom cursor.** Refused, explicitly and permanently. The
  system cursor is the visitor's own hand; the machine does
  not lend them a brass one.
- **Skeleton loading.** The drained chart (§6.18): plates shown
  as undrawn engravings — borders and grid printed, figures
  absent — for at most 1200ms before content or an honest
  empty state replaces them.
- **Page transitions.** The pen lifts, the plate is turned
  (§6.16): 420ms out, 420ms in, the new plate's border drawing
  as it lands. No crossfades of whole pages — paper does not
  dissolve.
- **Reduced motion.** A real variant per element (§6), and a
  global rule: with `prefers-reduced-motion`, the engine is at
  rest at high water — curve fully drawn, gears still, breath
  locked at mid-gap, every prediction printed as a figure.
  Nothing is removed; everything is *stopped*, which is what
  reduced motion means in a machine room.

**Ambient loops — exactly two licensed.** (1) The tidal breath
(§6.4): 90s cycle, ±6px spacing, waterline and idle gear-turn
in phase. (2) The pen's idle tremor (§6.1): a 0.4px vibration
at the pen tip while parked, the machine's mains hum. Any third
ambient loop requires a §10 gate exception in writing.

**Master timing table.** Border draw 480ms · plate settle 240ms
· headline settle 1400ms (incl. slack dwell) · stamp 260ms ·
pulley rise 320ms · counter runs 1600–2400ms (harmonic) ·
constituent highlight 300ms · page turn 840ms total · breath
90,000ms · gear idle 4°/s (great wheel). Nothing on the page
animates between 900ms and 90s except the counters and the
headline settle — the gap is deliberate: the machine is either
prompt (under a second) or tidal (a minute and a half), never
busy in between.

---

## 6. Signature elements

### 6.1 The pen-drawn tidal curve

- **What & why.** An SVG pen arm draws the hero's tidal curve
  across a full day as the live sum of the harbour's harmonic
  constituents — M2, S2, N2, K1, O1 — each constituent drawn
  faintly beneath the summed curve it contributes to. It is the
  theme's engine and its argument: the hero image is computed,
  not illustrated. A visitor who distrusts the picture can open
  the Constants Plate (§6.11), read the same five constituents,
  and re-derive the curve. The machine shows its workings
  because the workings are the beauty.
- **Structure.** One inline SVG (viewBox 1200×420) on the hero
  plate: five constituent paths (ink at 18–30% opacity, 1px),
  one summed path (`--ink`, 2.5px, round cap), a pen-arm group
  (two brass links, a pivot at the plate's top-left gantry, the
  pen nib at the curve's current point), and a printed axis —
  hours 00–24 along the base, heights 0–6m up the left, both
  set in tabular Newsreader. The summed path's geometry is
  generated at build/load from the declared height function
  `h(t) = Z0 + Σ Hᵢ·cos(ωᵢt − gᵢ)` over the Constants Plate
  record (§6.11); the path is never a hand-drawn asset.
- **Motion spec.** On load, the pen draws the first 6 hours in
  1800ms (`--ease-draw`, linear — a pen does not ease), then the
  draw hands over to scroll: the remaining 18 hours are scrubbed
  to the hero pin's 180vh range (§5), the nib advancing along
  the path as the visitor reads. Constituent paths draw in
  parallel, each offset by its own phase. While parked, the pen
  tip carries the licensed idle tremor (0.4px, §5). All values
  written by the shared rAF loop (lerp 0.10).
- **States.** Drawing (load) → scrubbing (pinned range) →
  complete (curve whole, pen parked at 24:00, tremor only) →
  revisited (scroll back: the pen retraces without redrawing —
  the ink is already on the paper). The curve never un-draws;
  ink is permanent, as on the machine's drum.
- **Content merge.** The curve *is* the hero's content: the
  headline floats on it (§6.2), the day's four turnings are
  marked on it with their printed times and heights, and the
  footer's tomorrow (§6.9) is this same function read at a
  later date. Remove the curve and the hero has nothing to say.
- **Failure fallback.** The 3000ms watchdog: if the path
  generation or the loop has not confirmed a drawn state within
  3000ms of arming, the SVG is replaced by its own static
  rendering — the complete curve, fully drawn, pen parked —
  shipped as the SVG's default state in the DOM. No-JS: the DOM
  ships with the full curve drawn and the pen arm at rest;
  drawing is a JS-armed performance over a finished chart.
- **Reduced-motion variant.** The complete curve, printed.
  Constituents visible beneath it, turnings marked, pen parked
  at 24:00. Nothing draws, nothing scrubs.
- **Performance budget & mobile variant.** Path generation is
  one pass of 288 samples (5-minute steps) per constituent —
  under 4ms on a mid phone, run once at load and once per
  resize (debounced 250ms). Per frame the loop writes one
  `stroke-dashoffset` and one transform. Mobile (<768px): the
  pen arm is cut (the curve draws itself, nib only), viewBox
  crops to 720×420 with the axis re-set, constituents reduced
  to M2 and S2 only beneath the sum.
- **Choreography timeline (v2).** t=0 plate border draws
  (480ms) → t=200ms axis prints → t=300ms pen lowers →
  t=300–2100ms first 6 hours draw, constituents in parallel →
  t=2100ms headline begins its float-settle (§6.2) → scroll:
  nib advances 18 hours across 180vh → at 24:00 the pen lifts
  8px over 300ms (`--ease-slack`) and parks → watchdog deadline
  t=3000ms passes unused (draw confirmation logged at t≈2100ms).
- **State matrix (v2).** *Rest:* complete curve, pen parked,
  tremor on. *Hover:* hovering the curve highlights the nearest
  constituent (§6.11's interaction, mirrored here) and prints
  that hour's height at the nib. *Focus:* the SVG is a figure
  with a text alternative (§6.1 accessibility); it takes no
  focus itself. *Active:* n/a. *Scrolled-past:* complete curve
  remains; the pen does not follow the visitor down the page —
  the staff (§6.17) takes over. *Disabled / no-JS:* static
  complete curve. *Touch:* scrub is scroll-driven, identical.
- **Breakpoints (v2).** ≥1200px: full arm, five constituents,
  1200×420. 768–1199px: arm shortened (single link), five
  constituents, axis heights at 1m intervals only. <768px: nib
  only, two constituents, hours at 3-hour intervals.
- **Edge cases & failure modes (v2).** *Constants record
  missing or malformed:* the build fails loudly at generation
  time, never at runtime — a page without constants does not
  ship (§10 check 1). *Resize mid-scrub:* path re-generated,
  dash state re-derived from the stored scroll fraction — the
  nib never jumps to 0. *Very long hero (slow connection,
  fonts late):* the draw waits for the plate's own layout, not
  for webfonts; axis text is set in the fallback serif for at
  most one frame before Newsreader arrives — figures are
  tabular in both.
- **Accessibility spec (v2).** The SVG carries `role="img"` and
  a full text alternative: "Tide curve for Aldermouth, [date]:
  high water 06:12, 4.87 metres; low water 12:24, 0.61 metres;
  high water 18:37, 4.79 metres; low water 00:49, 0.72 metres."
  — generated from the same record, so the alternative can
  never disagree with the picture. The four turnings are also
  printed as text on the plate beneath the chart.
- **Tokens consumed (v2).** `--ink`, `--buff`, `--buff-line`,
  `--brass`, `--brass-bright`, `--red` (turning ticks only),
  `--ease-draw`, `--ease-slack`, `--lerp` (0.10).

### 6.2 Headline floating on the waterline

- **What & why.** The hero headline rides the drawn curve: its
  baseline sits on the waterline at the headline's horizontal
  centre, rising and settling with the tide's height there, and
  bobbing ±4px on the tidal breath once settled. Typography
  subject to the page's physics — the title is *on* the tide,
  not above it. It is the theme's one licensed kinetic type
  (§5), and its restraint is the point: one floating headline
  is poetry; a page of floating text is seasickness.
- **Structure.** The H1 (Fraunces cartouche setting, §3) is
  positioned over the hero SVG, its transform written by the
  shared loop from the height function evaluated at the
  headline's centre-x and the current breath phase. A printed
  duplicate of the headline — same words, static, in normal
  flow — precedes it in the DOM and is what no-JS and reduced
  motion keep; the floating copy is `aria-hidden`.
- **Motion spec.** Entrance: as the curve completes its first
  draw (§6.1), the headline settles onto the waterline over
  1400ms (`--ease-slack`, including the 120ms slack dwell at
  the turn — it arrives, hesitates as water does at high tide,
  and rests). Thereafter: bob ±4px on the 90s breath, phase-
  locked to §6.4, plus a scrubbed component — as the pen's
  draw passes beneath the headline's centre, the headline rides
  the newly drawn height. Maximum total travel 14px; the line
  box never collides with the plate title spacing (§4).
- **States.** Pre-draw (sitting on the printed duplicate's
  position) → settling → floating (breath bob) → scrolled-past
  (the hero pins end; the headline leaves with its plate,
  mid-bob, without ceremony).
- **Content merge.** The headline's height *reports* the tide:
  at the hero's first screen the visitor can see whether the
  water at the headline's hour is high or low, and the caption
  beneath prints that hour's figure from the record. The
  decoration is a reading.
- **Failure fallback.** The 2000ms watchdog: if the loop has
  not confirmed the settle by 2000ms, the floating copy is
  removed and the printed duplicate stands alone — which is
  also the no-JS state. The headline can never be left mid-air
  or missing.
- **Reduced-motion variant.** The printed duplicate only,
  sitting at the waterline's mean height. No bob, no settle.
- **Performance budget & mobile variant.** One transform write
  per frame, shared with §6.1's frame. Mobile (<768px): bob
  amplitude ±2px, settle shortened to 900ms; below 360px wide
  the float is disabled entirely (the cartouche wraps to three
  lines and a riding three-line headline reads as an error,
  not a tide).
- **Choreography timeline (v2).** t=0 printed duplicate visible
  → curve draws (§6.1) → t=2100ms floating copy fades in over
  the duplicate at the drawn height → t=2100–3500ms settle with
  slack dwell at t≈2800ms → t=3500ms duplicate removed from
  visual flow (kept for AT) → breath bob begins, phase-locked
  to §6.4 → watchdog deadline t=2000ms — *before* the settle
  completes, the watchdog checks arming only (loop alive,
  height function returning), not arrival; arrival is confirmed
  by the settle's own end event.
- **State matrix (v2).** *Rest:* floating, bobbing. *Hover:*
  none — the headline is not an instrument. *Focus:* the
  headline is the page H1 and takes no focus; keyboard visitors
  meet the printed duplicate's text in the accessibility tree.
  *Active:* n/a. *Scrolled-past:* gone with the plate.
  *Disabled / no-JS:* printed duplicate. *Touch:* identical;
  bob continues, amplitude reduced on small screens.
- **Breakpoints (v2).** ≥1200px: 64px cartouche, bob ±4px.
  768–1199px: 48px, bob ±3px. <768px: 40px, bob ±2px, float
  disabled <360px.
- **Edge cases & failure modes (v2).** *Headline longer than
  three lines* (a long harbour name, a translated build): the
  float is disabled by a build-time line count — the duplicate
  stands and the curve passes beneath it. *Height function
  returns a value outside the plate* (a harbour with range
  >6m): the SVG's height axis rescales at generation; the
  headline rides the rescaled curve, never the raw metres.
  *Scroll-up revisit:* the bob resumes from the breath's
  current phase — no re-settle performance.
- **Accessibility spec (v2).** One H1 in the accessibility tree
  (the printed duplicate); the floating copy is `aria-hidden`
  and `pointer-events: none`. Motion is transform-only and
  under the vestibular threshold (±4px, 90s period); the
  reduced-motion variant removes it entirely.
- **Tokens consumed (v2).** `--ink`, `--ease-slack`, `--lerp`
  (0.10), breath phase from §6.4.

### 6.3 Ratio-true gear clusters

- **What & why.** Gear trains pinned in the left margin at two
  stations, rotating scrubbed to scroll at mechanically correct
  ratios: a 40-tooth great wheel drives a 4-tooth pinion at
  exactly 10:1, and a second pair — 32 teeth driving 8 — at
  4:1, teeth meshing without slip, external pairs
  counter-rotating as real gears do. The margins are the
  machine room of the page: decoration that obeys engineering.
  A gear that turns at a decorative ratio is a picture of a
  gear; these are gears.
- **Structure.** Two inline SVG clusters. Cluster A (hero
  station): great wheel (40 teeth, module drawn to a 148px
  pitch circle), pinion (4 teeth, 14.8px pitch circle — the
  ratio is in the geometry, not just the script), an idler
  between them so the pair's centres sit on the margin's rule.
  Cluster B (mid-page station): 32-tooth wheel and 8-tooth
  pinion on the same rule. Teeth are generated paths (involute-
  approximated by arc segments) written at build; each wheel is
  a `<g>` rotated about its own centre by the loop. Engraved
  direction arrows and tooth counts ("40", "4", "32", "8") are
  printed beside each wheel in `--brass-deep` — the machine
  labels its parts.
- **Motion spec.** Scrub mapping: the great wheel turns 360°
  across 6000px of document scroll (6° per 100px). The pinion
  turns −3600° over the same span (the negative sign is the
  meshing: it counter-rotates). Cluster B's wheel turns at the
  same 6°/100px datum through its own axle; its pinion at
  −24°/100px (4:1). Idle: with no scroll for >1500ms, the
  great wheel idles at 4°/s in phase with the breath (§6.4),
  the whole train following at ratio. All angles derive from
  one datum angle in the shared loop — slip is impossible by
  construction, because no wheel owns an independent value.
- **States.** Driven (scrolling) → idling (breath-driven, after
  1500ms still) → parked (tab hidden; the loop sleeps and the
  train stops mid-tooth without apology) → scrolled-past (a
  cluster outside the viewport is not written to; its angle is
  re-derived from the datum on re-entry, so it is always
  exactly where the train says it should be).
- **Content merge.** The clusters sit at the two stations where
  the page's argument changes gear: Cluster A beside the hero
  (the prediction), Cluster B beside the constants plate (the
  method). Their tooth counts are printed, their ratios are
  stated in §6.11's method note, and the footer (§6.9) prints
  the train's specification as part of the machine's plate. The
  gears are the page's workings, shown.
- **Failure fallback.** The 2000ms watchdog: if the loop has
  not confirmed rotation by 2000ms, the clusters stand static
  at their datum-zero pose — which is also the no-JS state,
  since the SVGs ship fully drawn in the DOM. A static gear is
  an engraving; the page loses motion, never meaning.
- **Reduced-motion variant.** Static engravings at datum zero.
  No idle, no scrub.
- **Performance budget & mobile variant.** Four transform
  writes per frame maximum, transform-only, no layout. SVG
  weight ≤9KB for both clusters (generated teeth, no filters,
  no shadows). Mobile (<768px): the margin stations do not
  exist (§4) — Cluster A folds into the hero plate's top-right
  corner at 64px, Cluster B is cut entirely; the surviving
  pair keeps its true 10:1 ratio at the smaller size.
- **Choreography timeline (v2).** t=0 clusters printed at datum
  zero → first scroll: datum angle follows scroll within one
  frame (lerp 0.10 — the train takes up its drive with brass
  weight, ~200ms to full follow) → scroll stops → t=+1500ms
  idle engages at 4°/s, phase-locked to the breath → tab hides:
  train parks → watchdog deadline t=2000ms passes unused.
- **State matrix (v2).** *Rest:* idling at 4°/s. *Hover:*
  hovering a wheel pauses the idle for that cluster and prints
  its ratio in the margin ("40 : 4 — ten to one") — inspection
  stops the machine politely; scroll drive is never paused.
  *Focus:* the clusters are decorative (`aria-hidden`) and
  take no focus; the ratio text is duplicated in §6.11's
  method note for AT. *Active:* n/a. *Scrolled-past:* not
  written; angle re-derived on return. *Disabled / no-JS:*
  static engraving. *Touch:* identical — drive is scroll,
  never drag.
- **Breakpoints (v2).** ≥1200px: both clusters in the margin at
  full size. 768–1199px: Cluster A only, at 96px, inside the
  hero plate's margin; Cluster B cut. <768px: Cluster A at
  64px in the plate corner; ratios and tooth labels retained
  (the labels are the content; the size is not).
- **Edge cases & failure modes (v2).** *Datum overflow:* the
  datum angle is kept modulo 360° in the loop; tooth phase is
  computed from the modulo, so a 100,000px page cannot drift
  the mesh. *Reverse scroll:* the train reverses exactly —
  gears, unlike reveals, are allowed to run backwards, because
  the visitor is cranking the machine by hand. *A cluster's
  station section removed by a CMS:* the cluster is cut with
  its section (it is bound to the section's node), never left
  floating in an empty margin.
- **Accessibility spec (v2).** `aria-hidden` throughout; the
  information (ratios, tooth counts, the method) is carried in
  §6.11's text. Motion is peripheral and slow; the
  reduced-motion variant stills it. No focusable parts.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--brass-deep`, `--buff-line`, `--lerp` (0.10).

---

### 6.4 Tidal breathing layout

- **What & why.** The page's vertical spacing expands and
  contracts by up to ±6px on a compressed tidal cycle: the full
  12h25m (745-minute) semidiurnal cycle compressed to a 90-second
  breath — the page runs at ≈497× tidal speed (44,700s ÷ 90s).
  Subliminal rather than showy: a visitor should feel that the
  page is calm in a rhythmic way long before they could say
  why. Layout as tide — the page's body has the rhythm it
  predicts. This is the theme's second licensed ambient loop
  (§5) and the phase master for §6.2's bob and §6.3's idle.
- **Structure.** One CSS custom property, `--breath` (−1…+1),
  written by the shared loop from the breath phase
  (sinusoidal, period 90,000ms, phase-locked across the whole
  page). Plate gaps, the hero's internal padding and the tide
  staff's waterline (§6.17) consume it:
  `gap: calc(var(--gap-base) + var(--breath) * 6px)`. Nothing
  else consumes it — the breath moves *space*, never content,
  never type, never the plates' internal layout, so text can
  never reflow: gaps are between plates, and a plate's interior
  is rigid.
- **Motion spec.** Continuous, period 90,000ms, sinusoidal
  (velocity zero at both extremes — the slack at the turn is
  built into the sine). Amplitude: ±6px on inter-plate gaps,
  ±3px on hero padding. The phase is derived from the wall
  clock, not from page load: two visitors opening the page at
  the same moment see the same breath phase, because the
  machine's time is the harbour's time, not the session's.
- **States.** Flooding (gaps opening, first 45s of the cycle)
  → high slack (gaps at maximum, velocity ~0) → ebbing (gaps
  closing) → low slack. The states are never labelled on the
  page; they are felt. Parked state (tab hidden): the phase
  freezes and resumes from the wall clock on return — the page
  does not pretend the tide waited for it.
- **Content merge.** The breath is the layout's tide: sections
  announced as flood sections (§4) are given the wider base gap
  (40px + breath), ebb sections the narrower (28px + breath),
  so the page's density rhythm and its breathing are one
  system. The footer prints the breath's specification —
  "this page breathes on the Aldermouth semidiurnal cycle,
  compressed 497 to one" — as part of the machine's plate
  (§6.9).
- **Failure fallback.** The 5000ms watchdog: if the loop has
  not written `--breath` within 5000ms of arming, the property
  is locked at 0 (mid-breath, base gaps) by a class on the
  root — which is also the no-JS state, since `--breath`
  defaults to 0 in the stylesheet. Layout is complete and
  correct at every breath value including never.
- **Reduced-motion variant.** `--breath` locked at 0. Base gaps
  everywhere. The page is at rest at mid-tide, permanently.
- **Performance budget & mobile variant.** One custom-property
  write per frame; the layout cost is bounded by construction —
  only inter-plate gaps depend on it, so the browser reflows
  plate positions, never plate interiors. Mobile (<768px):
  amplitude ±3px on gaps, hero padding fixed — small screens
  get the rhythm at half strength, because a 6px shift is a
  larger fraction of a small viewport.
- **Choreography timeline (v2).** t=0 `--breath` at its
  wall-clock phase (no start-up sweep — the tide was already
  running) → continuous 90s cycle → tab hidden: writes stop →
  tab visible: phase re-derived from the wall clock within one
  frame → watchdog deadline t=5000ms passes unused.
- **State matrix (v2).** *Rest:* breathing. *Hover:* none —
  the breath does not respond to the visitor; that is its
  dignity. *Focus:* none. *Active:* n/a. *Scrolled-past:* the
  breath is page-wide and position-independent. *Disabled /
  no-JS:* locked at 0. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: ±6px gaps, ±3px hero padding.
  768–1199px: ±4px gaps, ±2px padding. <768px: ±3px gaps,
  padding fixed.
- **Edge cases & failure modes (v2).** *Long pages (100+
  plates):* gap changes are uniform, so cumulative drift is
  zero by construction — the breath cannot walk the footer off
  its position over time, because every gap returns to base
  each cycle. *Scroll anchoring:* because interiors are rigid
  and only gaps move by ≤6px, a reading visitor's line can
  drift at most 6px per half-cycle — under the threshold of
  notice, and the browser's scroll anchoring absorbs it.
  *Print:* the stylesheet prints at `--breath: 0`.
- **Accessibility spec (v2).** The breath moves no text and
  changes no reading order; it is invisible to assistive
  technology. Vestibular safety: 6px over 45s is far below
  motion-sensitivity thresholds, and the reduced-motion
  variant removes it entirely.
- **Tokens consumed (v2).** `--breath`, `--gap-base` (per plate
  type, §4), `--lerp` (0.10).

### 6.5 High-water stamps

- **What & why.** As scroll passes each section's flood point,
  a high-water mark stamps onto the section plate's edge: the
  predicted high-water time and height for that section's
  subject, engraved-style, in harbour red, overlapping the
  plate edge by exactly 14px (§4). Progress recorded the
  harbour's way — marks left by water that has been there. The
  stamp is the theme's progress made physical, and its red is
  one of the three licensed red appearances per viewport (§2).
- **Structure.** A stamp is a small rotated plate fragment
  (−3° — a hand stamp never lands square) absolutely positioned
  at its section's edge: double-rule border in `--red`, inside
  it the stamp text set in Fraunces small caps (§3): `HW 18:37`
  on the first line, `4.79 M` on the second, the harbour's
  initials in the corner. Stamps are in the DOM from load,
  printed at 12% opacity as *unstamped ghosts* — the visitor
  can see where marks will fall — and the stamp action fills
  them to full red with the landing motion. Ghost and stamp
  are the same node; nothing appears from nowhere.
- **Motion spec.** Trigger: the section's flood point (its
  principal figure) crossing 62% of viewport height, scrubbed
  from the shared loop's scroll sample. Landing: 260ms
  `--ease-stamp` — the stamp scales 1.15→1.00 with a 2px paper
  overshoot and settles; a 90ms `dry` beat follows where the
  red deepens from `--red` at 82% to full (ink taking to
  paper). Once stamped, permanent: scrolling back up never
  un-stamps a mark. Water has been there; the mark stays.
- **States.** Ghost (12%, awaiting its flood) → landing (260ms)
  → drying (90ms) → stamped (full red, permanent) →
  scrolled-past (unchanged — permanence is the state).
- **Content merge.** Each stamp carries its section's own
  principal prediction from the record — the flood section's
  stamp prints that flood's high water; the method section's
  stamp prints the range it derives. The stamps, read in
  order down the margins, are the page's table of contents
  written in tide times; the tide staff (§6.17) fills to meet
  them.
- **Failure fallback.** No watchdog is needed for correctness —
  the ghost state is fully legible (the time and height are
  printed, at 12% red over buff ≈ readable as a pencil mark,
  and duplicated in the section's own figures). If the loop
  never runs (no-JS), every stamp stands as a ghost: the
  information is complete, only the ceremony is missing. If
  the loop starts late, stamps whose flood points are already
  passed land instantly at full red without the 260ms
  performance — the machine does not re-enact history.
- **Reduced-motion variant.** Stamps appear at full red when
  their section enters the viewport — no landing, no drying
  beat. Ghosts remain ghosts until then.
- **Performance budget & mobile variant.** One class change and
  one transform per stamp, ever — the cheapest element on the
  page after it lands. Mobile (<768px): stamps move inside the
  plate edge (no 14px overlap, which would collide with the
  narrower margin) and shrink to 84%, rotation kept.
- **Choreography timeline (v2).** Scroll: flood point crosses
  62% viewport → t=0 stamp begins landing (scale 1.15) →
  t=170ms contact (scale 1.00, overshoot 2px) → t=260ms settle
  → t=260–350ms drying (red 82%→100%) → permanent. Jump-scroll
  past three sections: all three land in one frame, staggered
  40ms in reading order (§5's ledger order), total 340ms.
- **State matrix (v2).** *Rest:* ghost or stamped, per scroll
  history. *Hover:* a stamped mark deepens its red by 6% and
  its tooltip-free title attribute is *not* used — instead,
  hovering prints the full turning (`HW 18:37 · 4.79 M ·
  ALDERMOUTH`) in the plate's caption line (§6.17 mirrors it).
  *Focus:* stamps are not focusable; their content is in the
  section's figures. *Active:* n/a. *Scrolled-past:* stamped
  forever. *Disabled / no-JS:* all ghosts, all legible.
  *Touch:* identical; no hover expansion — the caption line
  shows the current section's turning by default on touch.
- **Breakpoints (v2).** ≥1200px: edge overlap 14px, full size.
  768–1199px: overlap 8px, 92% size. <768px: inside the edge,
  84% size.
- **Edge cases & failure modes (v2).** *A section with no
  principal prediction* (a pure prose page): its stamp prints
  the next turning of the harbour instead, labelled `NEXT` —
  the machine never invents a section-specific figure it does
  not have. *Two flood points in one viewport* (short
  sections): both stamp, 40ms apart, reading order. *Print:*
  all stamps print at full red regardless of scroll state —
  paper gets the completed chart.
- **Accessibility spec (v2).** Stamps are `aria-hidden`
  duplicates: every stamped figure appears in its section as
  real text (§3 law 2 format). The ghost state's 12% red is
  decorative-only precisely because the data lives elsewhere —
  contrast law is satisfied by the duplicate, not the stamp.
- **Tokens consumed (v2).** `--red`, `--red-deep`, `--buff`,
  `--ease-stamp`, `--lerp` (0.10).

### 6.6 Harmonic counters

- **What & why.** Tide heights, times-to-turn and prediction
  counts count toward their values along the summed harmonic
  function itself — fast at mid-tide, slow at the turn — never
  a linear tween or a generic ease-out. Even the numbers move
  tidally; easing as subject matter. A counter in this theme is
  a small tide: it leaves one slack, hurries through the
  middle, and settles into the next slack exactly as water
  does, because it is driven by the same mathematics as §6.1's
  curve, normalised between its endpoints.
- **Structure.** A counter is a tabular Newsreader figure
  (§3) with `data-from`, `data-to` and `data-unit` attributes
  printed in the DOM — the *final* value is the DOM text; the
  count is a JS performance over a printed figure. Heights
  render to 2 decimal places, times count as minutes-then-
  format (`06:12`, never a raw minute count), ranges to 2
  decimals. The driver evaluates the normalised harmonic shape
  `s(u) = (1 − cos(πu))/2` blended with the M2 constituent's
  own phase curve for the harbour's record — specified once in
  §5, shared by every counter on the page.
- **Motion spec.** Trigger: the counter's plate entering 70%
  of viewport height. Duration by magnitude: heights and
  ranges 1600ms; counts of predictions (the large numbers,
  §6.11's 1,214) 2400ms; times-to-turn 2000ms. All run on the
  shared loop's clock. A counter runs **once**: revisiting a
  plate shows the printed final value — the machine does not
  re-perform its arithmetic for an audience that has already
  read it.
- **States.** Printed (final value in DOM) → armed (JS has
  zeroed the display to `data-from`, plate not yet at 70%) →
  counting (harmonic run) → settled (final value, identical
  to the printed one — the count must land *exactly* on the
  DOM figure, and the §10 gate diffs them). There is no
  paused state; a counter whose plate leaves the viewport
  mid-count completes instantly off-screen.
- **Content merge.** The counters count the record's own
  figures: the hero plate counts the day's range (4.26 m on
  the example day — §6.9's printed range, re-derived); the
  constants plate counts the season's predictions (1,214,
  §6.11); the berth form's plate counts the berths the tide
  serves. No counter counts anything decorative (visitors,
  years, awards) — in this theme a number is a prediction or
  it is prose.
- **Failure fallback.** The DOM ships with final values
  printed; JS arms the count by replacing the text only after
  the loop confirms (the 2000ms watchdog covers arming: if
  unconfirmed, text is never touched). No-JS: final values,
  full stop. A counter can never display a wrong number —
  worst case, it displays the right one without ceremony.
- **Reduced-motion variant.** No count. Final values stand as
  printed.
- **Performance budget & mobile variant.** One text write per
  counter per frame, at most 3 counters live simultaneously
  (plates gate their own counters); text writes are the only
  layout-touching writes allowed in the loop, and tabular
  figures (§3 law 1) guarantee zero reflow while they change.
  Mobile: identical, durations × 0.8 — small screens finish
  sooner; the harmonic shape does not change.
- **Choreography timeline (v2).** Plate crosses 70% viewport →
  t=0 count begins from `data-from` → t≈45% of duration:
  mid-tide, maximum digit velocity → t=100% settle exactly on
  the printed figure → the figure's plate stamp (§6.5) lands
  within the same 400ms window when the counter is its
  section's principal figure — number first, mark second, as
  on a real chart.
- **State matrix (v2).** *Rest:* settled on the printed value.
  *Hover:* none. *Focus:* counters are text; screen readers
  receive the final value only (the counting node is
  `aria-hidden` during the run, with a visually-hidden twin
  holding the final figure — AT never hears a number
  mid-count). *Active:* n/a. *Scrolled-past:* settled.
  *Disabled / no-JS:* printed values. *Touch:* identical.
- **Breakpoints (v2).** All sizes: same behaviour; figure size
  follows §3's responsive scale. The 70% trigger is
  viewport-relative at every size.
- **Edge cases & failure modes (v2).** *From equals to* (a
  figure unchanged since the last plate): the counter does
  not run; a machine does not count from 4.26 to 4.26.
  *Negative ranges or datum crossings* (a low water below
  chart datum at a real harbour): the harmonic shape is
  direction-agnostic; the count runs downward through zero
  with the minus sign printed from the first frame, never
  appearing mid-run. *Very large counts* (>10,000 predictions
  at a mature harbour): duration caps at 2800ms; the shape,
  not the duration, absorbs the magnitude.
- **Accessibility spec (v2).** Final values are the accessible
  values (twin-node pattern, above). Counting is decorative
  motion over printed data; reduced motion removes it. No
  counter is the sole carrier of its figure — each is
  repeated in its plate's table or caption.
- **Tokens consumed (v2).** `--ink`, `--ease-flood` (fallback
  shape where the record's phase curve is unavailable),
  `--lerp` (0.10).

---

### 6.7 Pulley-rope hover

- **What & why.** Hovering a plate, card or prediction row
  tightens a drawn pulley rope above it: an SVG line from the
  plate's top edge to a small brass pulley at the plate's
  gantry point draws taut, and the element rises ~3px as if
  taken up by the machine. Inspection is done by the engine's
  own rigging. This is the theme's only hover physics (§5):
  things are hauled, never tilted, never magnetised, never
  glowed at. The rise is small because a chart plate on a table
  does not leap — it is lifted just enough to show it has been
  taken up.
- **Structure.** Each haulable element carries a `data-haul`
  hook and one shared SVG overlay per plate (ropes are drawn
  in the plate's own coordinate space, `pointer-events: none`,
  `aria-hidden`): a rope path (1.5px `--brass-deep`) from the
  element's top-centre to the gantry pulley (a 14px brass
  circle with a printed sheave groove), drawn slack by default
  — a shallow catenary sag of 6px — and taut when hauled. The
  element's lift is a transform on the element itself.
- **Motion spec.** Hover/focus in: rope takes up over 320ms
  `--ease-haul` (slow bite, steady pull — the sag straightens
  in the first 120ms, the lift follows across the remaining
  200ms, so the rope visibly *causes* the rise). Lift: 3px
  plates and cards, 2px table rows. Hover out: release over
  380ms `--ease-haul` reversed — the element settles back with
  the rope's sag returning last. One haul at a time per plate:
  moving directly between two rows hands the rope over with a
  160ms cross-take, never two taut ropes on one gantry.
- **States.** Slack (rest) → taking up → hauled (taut, risen)
  → releasing → slack. Focus produces the identical state —
  keyboard inspection hauls the same rope, which is how the
  theme keeps one interaction language for both hands.
- **Content merge.** The pulley is part of the plate's printed
  furniture — the gantry and pulley are drawn on the plate
  whether or not JS runs, and the rope's slack state is the
  plate's resting illustration. Hauling a prediction row lifts
  the row the visitor is reading: the interaction points at
  the content, it does not decorate around it.
- **Failure fallback.** No watchdog required: without the loop,
  ropes stand slack and elements stand at rest — the complete,
  correct, no-JS state. A failed haul is indistinguishable
  from rest, which is the fallback working as designed.
- **Reduced-motion variant.** No lift, no rope motion. Hover
  and focus instead deepen the element's engraved border by
  one weight (a printed emphasis, not a movement) — the
  inspection signal survives, the motion does not.
- **Performance budget & mobile variant.** Per haul: one path
  `d` update (or a pre-drawn taut path cross-faded by opacity
  — the cheaper route, and the specified one: two paths, slack
  and taut, opacity-swapped) plus one transform. Touch
  (<768px and all coarse pointers): no hover exists, so the
  haul is bound to first tap on cards only (the card rises
  2px as its link arms, releasing on navigation) — table rows
  on touch get the border emphasis instead, because a lifted
  row under a finger is unreadable.
- **Choreography timeline (v2).** Pointer enters → t=0–120ms
  sag straightens → t=100–320ms lift 0→3px → hauled. Pointer
  leaves → t=0–200ms settle 3→0px → t=180–380ms sag returns →
  slack. Focus via keyboard: identical timings, triggered by
  `:focus-visible`.
- **State matrix (v2).** *Rest:* slack. *Hover:* hauled.
  *Focus:* hauled (same rope). *Active* (pressing a hauled
  card): lift increases to 4px for the press — the machine
  takes the strain — then the click's own action (§6.8 where
  applicable). *Scrolled-past:* n/a (hover is local).
  *Disabled:* a disabled control is never hauled; its rope is
  printed slack and greyed to `--buff-line`. *Touch:* tap-haul
  on cards only, as above.
- **Breakpoints (v2).** ≥1200px: full gantry ropes on plates,
  cards, rows. 768–1199px: ropes on cards and rows; whole
  plates are not hauled (a 1180px plate rising 3px reads as a
  layout bug at this width). <768px: tap-haul on cards only.
- **Edge cases & failure modes (v2).** *Rapid hover sweeping
  across a table:* the 160ms cross-take debounces — a sweep
  hauls nothing until the pointer rests 80ms; the machine does
  not flap. *Element taller than its plate's gantry reach*
  (a long card): the rope anchors to the element's visible
  top, not its layout top. *Rope over text:* ropes draw in the
  plate's margin space above elements, never across a text
  block — the overlay's geometry is computed from element
  edges, and any rope that would cross text is routed to the
  plate edge instead.
- **Accessibility spec (v2).** The haul is pure emphasis: no
  information is carried by the rope or the lift. Focus is
  always visible independently (the border deepening is the
  focus indicator's companion, never its replacement — the
  standard focus ring stands, drawn in `--red` at 2px, one of
  the licensed red uses being *marks made by the visitor's own
  hand*). Touch targets are unaffected by the 3px lift.
- **Tokens consumed (v2).** `--brass`, `--brass-deep`,
  `--buff-line`, `--red` (focus ring), `--ease-haul`.

### 6.8 Click-to-stamp a prediction

- **What & why.** Clicking a prediction row — in the weekly
  table (§6.12) or a plate's turning list — stamps that
  turning's high-water mark in harbour red at the row's edge:
  predicted time, height, and the visitor's own mark. The
  reader marks the chart like a harbourmaster. It is the
  theme's one deliberate annotation interaction, and its
  product is real: stamped turnings collect into the visitor's
  marked list (§6.15's form arrives with them pre-filled), so
  the gesture is the first step of the conversion, not a toy.
- **Structure.** Rows carry `data-turning` (the record key of
  their turning). The stamp is §6.5's stamp node at row scale
  (72%), positioned at the row's right edge, rotated −3°,
  initially absent — unlike §6.5's ghosts, this mark does not
  exist until the visitor makes it, because it is *theirs*.
  State persists in `sessionStorage` as a list of turning keys
  (never sent anywhere until the form is submitted, §6.15).
  A "marked turnings" count prints in the table plate's
  caption in §3's full format discipline.
- **Motion spec.** Click: the stamp lands in 260ms
  `--ease-stamp` (identical landing to §6.5 — one stamp
  language page-wide), with the row's own haul (§6.7) releasing
  simultaneously so the row settles as the mark lands. A second
  click on a stamped row lifts the mark: 200ms fade and a 1px
  rise — unstamping is quiet, because removing a pencil mark
  is quieter than making one. The marked count updates with
  §6.6's harmonic count over 600ms when it changes by one.
- **States.** Unmarked → stamping (260ms) → marked (permanent
  for the session) → unstamping (200ms) → unmarked.
  Scrolled-past has no meaning here; marks persist across the
  whole visit and across pages (the marked list is the one
  piece of state the machine carries between plates).
- **Content merge.** The stamp marks *the prediction itself*,
  and the marked list is the working set the berth form
  (§6.15) consumes — a visitor who has marked the two turnings
  that bracket their visit arrives at the form with the tide
  already filled in. Annotation as the top of the funnel: the
  most honest conversion pattern the theme can offer.
- **Failure fallback.** Without JS, rows are plain table rows
  (the data complete); the stamp affordance is a JS-armed
  enhancement announced by the table's caption ("select a
  turning to mark it" prints only when the loop confirms
  arming — the 2000ms watchdog again). If `sessionStorage` is
  unavailable (private mode), marks live for the page only and
  the caption says so in plain words: "marks will not survive
  this visit — the harbour keeps no copy."
- **Reduced-motion variant.** Marks appear/disappear without
  the landing performance; the count updates instantly.
- **Performance budget & mobile variant.** One node insert and
  one transform per mark; storage writes are a single small
  JSON array. Mobile: stamps at 64% scale, anchored inside the
  row's edge; rows' tap targets grow to 48px when the table is
  in marking mode (§6.12).
- **Choreography timeline (v2).** Click → t=0 haul releases,
  stamp enters at scale 1.15 → t=170ms contact → t=260ms
  settled → t=260–350ms drying (§6.5's beat, shared) → caption
  count counts 600ms harmonic → if this is the first mark, the
  table caption's second line prints the route onward: "marked
  turnings travel with you to the berth request (§6.15)".
- **State matrix (v2).** *Rest:* unmarked or marked. *Hover:*
  the row hauls (§6.7); a marked row's stamp deepens 6%.
  *Focus:* rows are focusable buttons-in-row (the row's
  turning cell is the control, 48px target); Enter/Space
  stamps identically. *Active:* the landing *is* the active
  feedback. *Scrolled-past:* n/a. *Disabled:* a turning in the
  past (its time already gone on the real clock) cannot be
  marked — the row prints `GONE` in the stamp's place, in
  `--ink-soft`; the machine does not let you book yesterday's
  tide. *Touch:* tap = click, identical.
- **Breakpoints (v2).** ≥1200px: stamp 72% at row's right edge,
  overlapping 10px. 768–1199px: 68%, inside the edge. <768px:
  64%, inside; the table switches to its stacked form (§6.12)
  and the stamp sits at the turning's own line.
- **Edge cases & failure modes (v2).** *Marking every turning
  on the plate (28):* allowed; the caption count and the form
  handle the full set — but the form (§6.15) asks the visitor
  to narrow to the two that bracket a visit, in the form's own
  voice. *Clock skew* (visitor's clock wrong, `GONE` misapplied):
  gone-ness is computed against the harbour's time as printed
  by the build's data, not the visitor's clock, wherever the
  build provides it; the rule is stated in §6.12's caption.
  *Two tabs:* storage events re-sync the marked list; last
  writer wins, marks merge by union — a mark is never lost to
  a race.
- **Accessibility spec (v2).** The control is a real button
  with an aria-label in full format: "Mark high water 06:12,
  4.87 metres, Aldermouth" / "Unmark…". `aria-pressed` carries
  the state. The stamp graphic is `aria-hidden`. The marked
  count is a live region at `aria-live="polite"`, announced as
  "Three turnings marked."
- **Tokens consumed (v2).** `--red`, `--red-deep`, `--ink-soft`,
  `--ease-stamp`, `--ease-haul`.

### 6.9 The honest footer tides

- **What & why.** The footer prints tomorrow's actual high and
  low tide times for the site's named harbour, computed from
  the same harmonic constants the hero curve uses. The
  decoration is the data — the page's prettiest element is also
  its most useful, and it is the law (§1) made visible at the
  exact place every other theme puts boilerplate. A visitor
  who reads only the footer has still been served a prediction
  by the machine.
- **Structure.** A `--slate-deep` footer plate, full width. Its
  top edge carries the pen's route: a single-line SVG of
  tomorrow's curve (24 hours, compressed into the footer's
  width, ink picked out in buff at 60%) drawn across the whole
  footer as its horizon. Beneath it, four turning blocks in
  tabular Newsreader, buff on slate-deep (9.2:1), in §3 law 2's
  full format. Then the machine's plate: a small engraved
  register listing the engine's specification — constituents
  used, the breath compression (497:1), the gear train
  (40:4, 32:8), the constants' source and epoch — and the
  ordinary footer matter (links, legal) set as chart-room
  notices, in that order: prediction first, paperwork second.
- **Motion spec.** The footer curve draws once, `--ease-draw`
  1200ms, when the footer first enters the viewport — the pen
  finishing the page. The four turnings print with §6.6
  counters (1600ms) on that same first entry. Nothing else in
  the footer ever moves; a footer is a plate, not a performance.
- **States.** Undrawn (below the fold, curve at its printed
  40% ghost) → drawn (first entry) → printed (permanent).
  No-JS: the curve ships drawn and the turnings printed — the
  footer's data is server/build-rendered, never client-fetched,
  so the most useful element on the page is also the most
  robust.
- **Content merge.** Total: the footer's turnings are §6.1's
  function at tomorrow's date, its curve is that function
  drawn, its machine plate is §6.11's method in miniature. The
  §10 gate recomputes the four times from the Constants Plate
  and fails the build on a drift beyond ±6 minutes or ±0.05m —
  the footer is where the law is audited.
- **Failure fallback.** The data is static-rendered; there is
  no runtime failure mode that can blank it. If the curve's
  draw never arms (loop dead), the ghost state stands — the
  turnings, which are text, are unaffected.
- **Reduced-motion variant.** Curve printed whole; turnings
  stand as figures; no counters.
- **Performance budget & mobile variant.** One 1200ms draw,
  once. Footer SVG ≤3KB. Mobile (<768px): the four turnings
  stack two-over-two, the machine plate's register wraps to a
  single column, the curve keeps its full width (it is the
  horizon; cropping it would crop the day).
- **Choreography timeline (v2).** Footer enters → t=0 pen
  starts at 00:00 → t=1200ms curve complete at 24:00 →
  t=300–1900ms the four counters run, staggered in reading
  order at 40ms (§5's ledger stagger) → permanent print.
- **State matrix (v2).** *Rest:* printed. *Hover:* turning
  blocks haul 2px (§6.7's language at footer scale) when they
  are links to the full table (§6.12); non-link turnings do
  not move. *Focus:* identical haul. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled / no-JS:* printed, drawn.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: four turnings in a row, machine
  plate at right. 768–1199px: four in a row, plate below.
  <768px: two-over-two, plate below, curve full-width.
- **Edge cases & failure modes (v2).** *The date line:* "tomorrow"
  is computed in the harbour's timezone, never the visitor's —
  the footer prints the harbour's date explicitly ("for
  Saturday 14 June, Aldermouth time") so a visitor nine zones
  away is never misled. *A harbour with only three turnings in
  a calendar day* (real, near the diurnal edge): the footer
  prints three blocks and a fourth reading `— the day carries
  three turnings —`; it never pads the row with a borrowed
  time. *Daylight-saving transitions:* times print in the
  harbour's civil time with the offset named on the plate.
- **Accessibility spec (v2).** The turnings are text in a
  `<footer>` landmark, in reading order, in full format. The
  curve SVG is `aria-hidden` (its data is the four blocks
  beside it). Contrast 9.2:1 for the turning text; the machine
  plate's small register is buff at 82% on slate-deep (≈6.4:1),
  never below.
- **Tokens consumed (v2).** `--slate-deep`, `--buff`,
  `--buff-line`, `--brass-deep`, `--ease-draw`, `--lerp` (0.10).

---

### 6.10 Dial-plate navigation

- **What & why.** The masthead is an engraved brass-bound plate:
  the harbour's name in the cartouche register, the navigation
  links set as dial labels around a small tide dial whose needle
  shows the *current state of the visitor's reading* — which
  part of the page's cycle they are in (first flood, ebb,
  second flood, the turn) — and, beneath the dial, the harbour's
  next real turning in full format. Navigation as an instrument
  the machine keeps wound: it tells you where you are in the
  page and where the water is in the day, in one glance.
- **Structure.** A fixed-height plate (72px desktop) in `--buff`
  with the double engraved border (§4). Left: wordmark (Fraunces
  24px) and harbour name. Centre/right: nav links as letterspaced
  caps labels (§3 dial register), each with a tick mark above it
  on the plate's rule — the active page's tick is filled in
  `--red`, the one licensed red in the header, because the active
  page is a mark the visitor has made. Right: the tide dial, a
  44px SVG circle with hour ticks, one needle, and the next
  turning printed beside it in tabular figures.
- **Motion spec.** The needle is driven by the shared loop: it
  maps document scroll progress onto the dial's 12h25m face (a
  full page = one full cycle, top = the visitor's arrival
  turning) with `--ease-flood` smoothing — it sweeps, it does
  not tick. On page load the needle settles from the previous
  page's stored angle (sessionStorage, the machine remembers
  where you left the dial) over 600ms `--ease-slack`. Link hover:
  the link's tick draws (120ms `--ease-draw`) and the link hauls
  2px (§6.7). Nothing else in the masthead moves.
- **States.** Reading states (needle angle by scroll) → at the
  footer, the needle completes its cycle and rests at the
  arrival turning — the dial has shown the whole tide. Stuck
  state: the masthead is *not* sticky in the app sense; it is
  pinned for the first 100vh (the hero's duration) and then
  releases and scrolls away — a chart room's plate is on the
  wall, not following you around the harbour. A compact
  return-plate (wordmark + next turning only, 48px) docks at
  the top after 200vh for wayfinding.
- **Content merge.** The dial's second job is real data: the
  next turning beside it is the harbour's actual next high or
  low water from the record, updating at each turning (build/
  data-driven, §6.9's discipline). The masthead is the only
  element allowed to carry live tide state, and it carries it
  in the same full format as everywhere else.
- **Failure fallback.** No-JS: the masthead prints with the
  needle at the arrival turning and the next turning as static
  text — complete. Loop failure (2000ms watchdog): the needle
  locks at its last written angle and the dial becomes an
  engraving; links are ordinary links throughout.
- **Reduced-motion variant.** The needle jumps (no sweep) at
  quarter-cycle boundaries only; the settle on load is instant;
  hover ticks print without drawing.
- **Performance budget & mobile variant.** One transform write
  per frame for the needle, shared loop. Mobile (<768px): the
  dial shrinks to 36px and moves beside the wordmark; nav links
  collapse into a "chart drawer" — a plate that hauls down
  (§6.7's `--ease-haul`, 380ms) listing the links as a printed
  index with their ticks; the next-turning line remains visible
  in the masthead at all times (it is the harbour's, not the
  menu's).
- **Choreography timeline (v2).** Load → t=0 masthead plate
  border draws (480ms) → t=200ms needle settles from stored
  angle (600ms) → t=480ms next-turning prints → scroll: needle
  sweeps with progress → 200vh: return-plate docks (240ms
  `--ease-haul`) → footer: needle completes the cycle.
- **State matrix (v2).** *Rest:* needle sweeping with scroll.
  *Hover:* tick draws, link hauls. *Focus:* identical to hover;
  the focus ring is §6.7's red ring. *Active:* the current
  page's tick is red-filled, permanent. *Scrolled-past:* the
  masthead has released; the return-plate carries wordmark,
  dial (36px) and next turning. *Disabled / no-JS:* static
  plate, needle at arrival. *Touch:* drawer pattern, above.
- **Breakpoints (v2).** ≥1200px: full plate, 44px dial, all
  links. 768–1199px: links to four, dial 40px, return-plate
  from 150vh. <768px: drawer nav, dial 36px, next turning
  always visible.
- **Edge cases & failure modes (v2).** *Very short pages* (the
  404, §6.18): the dial maps the page anyway — a short page is
  a short tide; the needle still completes its cycle at the
  footer. *Stored angle from another harbour* (a network of
  harbour sites sharing the engine): the stored value is keyed
  by harbour; a foreign key is ignored and the needle starts
  at the arrival turning. *Next-turning data stale* (the build's
  data older than the last turning): the dial prints the
  turning without `NEXT` and the caption in §6.11 carries the
  data's epoch — the machine dates its knowledge, always.
- **Accessibility spec (v2).** A `<nav>` landmark with an
  aria-label naming the harbour. The dial is `aria-hidden`;
  the next turning is real text. The drawer's button carries
  `aria-expanded` and the drawer closes on Escape, returning
  focus to the button. Active page: `aria-current="page"`,
  never carried by the red tick alone.
- **Tokens consumed (v2).** `--buff`, `--buff-line`, `--brass`,
  `--brass-deep`, `--red`, `--ink`, `--ease-slack`,
  `--ease-draw`, `--ease-haul`, `--lerp` (0.10).

### 6.11 The Constants Plate

- **What & why.** The harmonic constants table, presented as the
  machine's engraved maker's plate: the five constituents with
  their amplitudes, phases and periods, the mean sea level, the
  derived spring and neap ranges, the source and epoch of the
  constants, and the method note (including the gear train's
  specification from §6.3). This plate is the theme's law (§1)
  given a physical address: it is the one record every figure on
  the page traces to, and it is printed *on* the page, in the
  open, where any visitor can check the machine's sums. Its
  worked record, used consistently across this whole expansion:
  **Aldermouth** — Z0 2.94 m; M2 H 1.86 m, g 142°, T 12.4206h;
  S2 H 0.64 m, g 178°, T 12.0000h; N2 H 0.38 m, g 121°, T
  12.6583h; K1 H 0.11 m, g 205°, T 23.9345h; O1 H 0.09 m, g 188°,
  T 25.8193h. Amplitude sum 3.08 m; spring range 2 × (1.86 +
  0.64 + 0.38) = **5.76 m**; neap range 2 × (1.86 − 0.64) =
  **2.44 m**; high-water interval **12h25m**. A real build
  substitutes its harbour's surveyed constants and re-derives
  every figure in this file from them.
- **Structure.** A slate plate (`--slate`, buff text 8.1:1) —
  the one dark plate in the body, because a maker's plate is
  screwed to the machine, not laid on the chart. A tabular
  Newsreader table: constituent, symbol, period (h), amplitude
  H (m), phase g (°). Below: the derived register (Z0, amplitude
  sum, spring range, neap range, HW interval) set as §6.6
  counters' printed values. Below that: the method note in
  Newsreader 15.5px, and the season's prediction count — on the
  worked record, **1,214 predictions drawn since the season
  plate was fitted** — which §6.15's stamp arithmetic depends on.
  The plate pins beside the weekly table (§5's second licensed
  pin) on long pages.
- **Motion spec.** Rows enter in ledger order (§5): 40ms stagger,
  each row's rule drawing `--ease-draw` 300ms as it lands.
  Hovering or focusing a constituent row highlights that
  constituent's faint curve in the hero (§6.1) and in the
  plate's own miniature curve (a 260×64px SVG sum at the plate's
  head, the highlighted constituent at full ink, the sum
  dimmed) — cross-highlight latency one frame, fade 300ms
  `--ease-flood`. The derived counters run (§6.6) on first entry.
- **States.** Printed → rows landing (first entry) → at rest
  (the plate's normal state: a plate does not perform twice) →
  highlighting (a row held) → released (fade back 300ms).
- **Content merge.** This *is* the content — the theme's source
  of truth, wearing its plate. Every other element in §6 cites
  it; §6.1's curve is its picture, §6.9's footer is its output,
  §6.12's table is its week. A build that hides this plate
  behind a "learn more" has broken the law and fails §10
  check 1.
- **Failure fallback.** Static by default: the plate ships
  printed in full, counters at final values, miniature curve
  drawn. JS adds only the stagger and the cross-highlight. The
  2000ms watchdog covers the counters' arming (§6.6); the plate
  itself needs none.
- **Reduced-motion variant.** All rows printed, no stagger, no
  counters; cross-highlight becomes instant on/off (it is an
  information state, not a motion).
- **Performance budget & mobile variant.** The miniature curve
  is generated with the hero's (same 288-sample pass, reused
  data — the plate adds no second computation of the sum).
  Mobile (<768px): the table transposes to a stacked register
  (constituent per block: symbol and period on the first line,
  H and g on the second) — the figures never shrink below 14px
  tabular, because a constants plate you cannot read is a
  decoration, and this theme has none.
- **Choreography timeline (v2).** Plate enters → t=0–400ms rows
  land in ledger order, rules drawing → t=400ms derived counters
  begin (2400ms for the 1,214; 1600ms for the ranges) → at rest.
  Row hover → next frame: miniature and hero curves highlight
  → 300ms fade to full emphasis → release: 300ms back.
- **State matrix (v2).** *Rest:* printed plate. *Hover:* row
  emphasis + cross-highlight. *Focus:* identical (rows are
  focusable as a single tab stop per row via a roving tabindex
  — the plate is an instrument, read with the arrow keys).
  *Active:* n/a. *Scrolled-past:* printed; the pin releases at
  the weekly table's end. *Disabled / no-JS:* printed in full.
  *Touch:* tap a row to hold its highlight; tap again or
  elsewhere to release.
- **Breakpoints (v2).** ≥1200px: slate plate, five-column table,
  pins beside §6.12. 768–1199px: no pin; plate above the table.
  <768px: stacked register form, miniature curve kept (it is
  the plate's portrait of itself).
- **Edge cases & failure modes (v2).** *A harbour with more
  constituents* (a real harmonic set can run to 30+): the plate
  prints the five *principal* constituents and a register line —
  "and 24 lesser constituents, summed but not engraved; the
  full set is printed in the harbour's almanac" — with the
  amplitude sum corrected to the full set. The law holds: what
  is summed is declared, even when not every term is engraved.
  *Shallow-water constituents* (M4, MS4 at estuary harbours):
  they take rows in the same table with their compound periods
  (6.2103h for M4) — the table's form does not change.
  *Constants revised mid-season* (a resurvey): the plate prints
  the epoch and the revision ("constants of the 2026 survey");
  figures elsewhere carry the same epoch in §6.9's machine
  plate, so two plates can never silently disagree.
- **Accessibility spec (v2).** A real `<table>` with a caption
  ("Harmonic constants for Aldermouth, survey of 2026") and
  column headers. The cross-highlight is duplicated as text:
  holding a row prints that constituent's contribution at the
  plate's foot ("M2 alone would give a range of 3.72 metres" —
  2 × 1.86, from the record). Roving tabindex with visible
  focus (§6.7's ring, in buff on slate).
- **Tokens consumed (v2).** `--slate`, `--buff`, `--buff-line`,
  `--brass-bright`, `--red` (never on this plate), `--ease-draw`,
  `--ease-flood`, `--lerp` (0.10).

### 6.12 The prediction table

- **What & why.** The weekly tide table — the theme's listing
  element and, for most real builds, its core product: seven
  days of turnings for the harbour, each row a turning with its
  time, height, and state, banded by flood and ebb, stamped by
  §6.5 as the visitor reads down it and markable by §6.8. If the
  hero is the machine's portrait, this is its work. The worked
  plate carries **28 turnings** — seven days at four turnings,
  the count the record's rhythm gives the example week.
- **Structure.** A chart plate (§4) holding a real `<table>`:
  day (with its date), turning (HW/LW with the day's ordinal —
  "HW 2"), time, height, and a state column (springs/neaps
  marker by the day's range against §6.11's derived register:
  a day whose range exceeds 4.80m is marked `SPRINGS` in the
  dial register, below 3.20m `NEAPS`, between, nothing — the
  table does not label the ordinary). Flood rows banded
  `--buff-shade` from the turning until the next high water;
  each high-water row carries a red edge tick (§2's licensed
  red). The table's caption carries the marking instruction
  (§6.8) and the marked count.
- **Motion spec.** Rows enter in ledger order (40ms stagger,
  400ms cap, §5) on first entry. Scrolling the table: §6.5's
  stamps land on each day-plate's edge at its flood point.
  Nothing in the table animates on hover except the §6.7 haul
  (2px) and §6.8's stamp. The table is a document; its motion
  budget is spent at its borders, never inside its figures.
- **States.** Printed → entering (first view) → at rest →
  marking mode is not a mode: any row is markable at any time
  (§6.8). Past days (before the harbour's today) print at
  `--ink-soft` with their turnings `GONE` (§6.8) — the table
  shows the whole week, including the part of it that has
  already happened, because a chart shows the coast, not just
  the destination.
- **Content merge.** The table is generated from the same
  height function as §6.1 and §6.9 — one function, three
  printings (curve, week, footer), and the §10 gate spot-checks
  five rows against a recomputation. Its days drive §6.14's
  cards (each harbour card's "next window" is read from this
  table's data) and §6.15's form (marked turnings pre-fill it).
- **Failure fallback.** The table is build-rendered HTML; with
  no JS it is complete and correct, missing only stamps and
  hauls. If the data feed for a *future* week is unavailable at
  build time, the plate prints the weeks it has and an honest
  final row: "the drum is wound to 21 June; further weeks are
  drawn as the constants are proved" — never a fabricated row.
- **Reduced-motion variant.** Rows printed, no stagger; stamps
  appear per §6.5's variant; hauls become border emphasis
  (§6.7's variant).
- **Performance budget & mobile variant.** 28 rows is the
  design load; a build printing a full month (124 rows) must
  paginate by week plates rather than grow the plate — the
  stagger cap (400ms) and the stamp thresholds assume a
  week-sized plate. Mobile (<768px): the table stacks — each
  turning becomes a two-line block (turning + time, then
  height + state), day headings as plate rules; figures stay
  14px tabular minimum; marking targets 48px.
- **Choreography timeline (v2).** Plate enters → t=0–400ms rows
  land in ledger order → as scroll proceeds: day stamps land at
  each day's flood point (§6.5) → the tide staff (§6.17) fills
  in step → at the plate's end, the constants plate (§6.11)
  unpins.
- **State matrix (v2).** *Rest:* printed table. *Hover:* row
  haul 2px. *Focus:* rows' turning cells are the §6.8 controls;
  focus ring per §6.7. *Active:* §6.8's stamp landing.
  *Scrolled-past:* stamps stand; rows do not re-enter.
  *Disabled:* past turnings disabled for marking, printed
  `GONE`. *No-JS:* complete table. *Touch:* stacked form,
  48px targets.
- **Breakpoints (v2).** ≥1200px: five columns, full plate width.
  768–1199px: state column folds into the turning cell (the
  `SPRINGS` marker rides under the date). <768px: stacked
  blocks, as above.
- **Edge cases & failure modes (v2).** *A day with three or
  five turnings* (real, at the diurnal edge and on double-high-
  water coasts): the table prints what the function returns —
  three rows or five — and the week's count line corrects
  itself ("27 turnings this week"); no row is invented to make
  the plate rectangular. *Double high waters* (e.g. a harbour
  with a stand): the two peaks print as HW 1 and HW 2 with the
  stand's duration noted in the state column. *A row whose
  height exceeds the plate's printed axis* (an exceptional
  spring): heights are figures, not bars — nothing overflows;
  figures cannot break a table.
- **Accessibility spec (v2).** Real table semantics with
  `scope="col"` headers and day headers as `scope="row"`.
  The flood banding is never the only carrier of flood/ebb —
  the turning column prints HW/LW in words. Marked-state is
  §6.8's `aria-pressed`. The caption's marked count is the
  §6.8 live region.
- **Tokens consumed (v2).** `--buff`, `--buff-shade`,
  `--buff-line`, `--ink`, `--ink-soft`, `--red`, `--ease-draw`,
  `--lerp` (0.10).

---

### 6.13 Charted photograph frames

- **What & why.** Photographs in this theme are charts, not
  decoration: each sits inside an engraved plate frame with a
  caption that states the tide at the moment the photograph
  claims to show — "the causeway at low water, 0.61 metres" —
  so an image is a claim about the water, checkable against the
  record like every figure. A photograph of the harbour at high
  water captioned as low water is a §9 failure, not a stock
  choice. The frame's neatline, corner coordinates and caption
  register make photography answerable to the machine.
- **Structure.** A `<figure>` on a small plate: the image inside
  the double engraved border (§4), a coordinate strip along the
  frame's bottom edge (the harbour's charted position, set in
  the dial register), and a `<figcaption>` in Newsreader with
  the tide statement in full format (§3 law 2). Images are
  duotone-mapped at build to the slate–buff range (never a CSS
  filter at runtime): the sea in a photograph is slate, the sky
  is buff, because the palette (§2 law 4) admits no blue.
- **Motion spec.** On its plate's flood entry, the image settles
  from scale 1.06 to 1.00 inside the frame over 900ms
  `--ease-flood` — a chart being laid flat (§5's image
  treatment). The frame's border draws (480ms `--ease-draw`)
  in the same window. That is the whole performance; a charted
  photograph does not parallax, tilt or zoom on hover — hover
  hauls the whole figure 3px (§6.7), nothing more.
- **States.** Unframed (image at 1.06, border undrawn, below
  the flood point) → settling → charted (permanent). A figure
  whose plate is revisited shows the charted state; charts do
  not re-lay themselves.
- **Content merge.** The caption's tide statement is generated
  from the same record as the table (§6.12): a "visit at low
  water" card (§6.14) shows the causeway photograph captioned
  with the actual next low water it is selling. Image, caption
  and commerce are one fact in three forms.
- **Failure fallback.** The image ships in the DOM with its
  caption; the settle and draw are JS-armed over it. If the
  image itself fails to load, the frame prints its caption and
  a charted outline (the plate's engraved border around an
  empty neatline with the words "plate not received" in the
  dial register) — a missing photograph is admitted on the
  plate, never hidden by a broken-image icon.
- **Reduced-motion variant.** Image at 1.00, border printed.
  No settle.
- **Performance budget & mobile variant.** Duotone at build;
  responsive `srcset` with the frame's aspect fixed (4:3 or
  the chart's own 3:2) so layout never shifts. Per-image
  budget ≤120KB at desktop size, ≤60KB mobile. The settle is
  one transform on the `<img>` only. Mobile: coordinate strip
  drops (the caption carries the tide statement alone), aspect
  kept.
- **Choreography timeline (v2).** Plate flood point crosses →
  t=0 border begins drawing → t=0–900ms image settles 1.06→1.00
  → t=480ms border complete → t=900ms charted; caption was
  legible from t=0 (captions never wait for their pictures).
- **State matrix (v2).** *Rest:* charted. *Hover:* figure hauls
  3px (§6.7). *Focus:* when the figure is a link (inside a
  §6.14 card), the card's focus ring applies. *Active:* n/a.
  *Scrolled-past:* charted. *Disabled / no-JS:* printed frame,
  image at rest scale. *Touch:* identical, no haul until tap
  (§6.7's touch rule).
- **Breakpoints (v2).** ≥1200px: full frame with coordinate
  strip. 768–1199px: strip kept, caption wraps to two lines.
  <768px: strip dropped, frame margins tighten to the plate
  rule.
- **Edge cases & failure modes (v2).** *A photograph whose tide
  state is unknown* (archive imagery): the caption says so —
  "the archive does not record the tide" — rather than guessing
  a state. Honesty about a picture is the same law as honesty
  about a figure. *Portrait images in a landscape frame:* the
  neatline crops by chart rules (the subject's waterline stays
  in frame) — specified per image at build, never `object-fit`
  by default. *Very dark photographs:* the duotone map lifts
  shadows to slate-deep at the darkest; a photograph that
  cannot hold the map is not used (§9).
- **Accessibility spec (v2).** Alt text describes the scene and
  repeats the tide state ("The causeway to the island at low
  water; two walkers crossing; the tide at 0.61 metres") — the
  caption is not a substitute for alt, nor alt for the caption.
  Contrast: captions are ink on buff (10.3:1).
- **Tokens consumed (v2).** `--buff`, `--buff-line`, `--slate`,
  `--ink`, `--ease-flood`, `--ease-draw`, `--lerp` (0.10).

### 6.14 Harbour plate cards

- **What & why.** The card family — berths, services, visiting
  windows, sister harbours — built as small chart plates: each
  card is a plate with its engraved border, one charted
  photograph (§6.13) or an engraved dial in its head, its facts
  in Newsreader, and one figure that matters set as the card's
  principal prediction — for a berth, the next tidal window;
  for a causeway, the next safe crossing; for a service, the
  hours the tide allows it. A card without a figure from the
  record is not a card in this theme; it is a leaflet, and it
  belongs to another theme.
- **Structure.** An `<article>` plate (double border, §4) in a
  grid of 3 (≥1200px). Head: figure or dial. Body: title
  (Fraunces 22px), two lines of Newsreader fact, the principal
  figure in tabular 20px with its full format (§3 law 2), and
  one link styled as a dial label ("Read the plate →" is
  forbidden; the link names its destination: "Aldermouth
  berths"). The principal figure is build/data-rendered from
  the same record as §6.12 — a card never hand-types a tide.
- **Motion spec.** Cards enter with their plate (§5's plate
  settle, 240ms `--ease-haul`, border draw 480ms), staggered
  in reading order at 40ms across the row. Hover/focus: the
  §6.7 haul (3px, rope at the card's gantry). The principal
  figure counts (§6.6) on first entry when it is a height or a
  range; times print statically (a time counting looks like a
  clock malfunction; heights count because water rises).
- **States.** Printed → entering → at rest → hauled (hover/
  focus) → the card's link followed (the §6.16 transition takes
  over). A card whose window has passed today re-prints its
  figure for the next window at the turning — the card is
  alive to the record, on the record's schedule, not the
  visitor's.
- **Content merge.** The card's figure is the harbour's own
  next fact, drawn from §6.12's data; two cards for the same
  harbour can never disagree, because neither owns its number.
  The grid as a whole is the harbour's day at a glance.
- **Failure fallback.** Cards are static HTML plates; JS adds
  settle, haul and counts only. A card whose data is missing
  at build prints its figure line as "the drum is not wound to
  this window" (§6.12's honesty formula) rather than a stale
  time — stale tide data is a safety failure, not a content
  gap, and the theme treats it as such.
- **Reduced-motion variant.** Cards printed; haul becomes
  border emphasis; figures stand.
- **Performance budget & mobile variant.** Grid reflow is
  CSS-only. Per card ≤130KB including its photograph (§6.13's
  budget). Mobile (<768px): single column, cards at full plate
  width, the photograph aspect kept; the principal figure
  moves above the fact lines (on a small screen the figure is
  the card).
- **Choreography timeline (v2).** Row enters → t=0/40/80ms
  cards settle in reading order, borders drawing → figures
  count where applicable (1600ms) → at rest. Turning passes
  while the page is open: the affected card's figure re-prints
  with a 300ms `--ease-flood` crossfade of the digits only —
  the one mid-visit update the theme permits itself, because
  the tide does not wait for a reload.
- **State matrix (v2).** *Rest:* printed card. *Hover:* haul
  3px. *Focus:* haul + red ring (§6.7) on the card's link.
  *Active:* link press deepens the haul to 4px (§6.7's active).
  *Scrolled-past:* printed. *Disabled:* a card for a closed
  berth prints its state in the dial register (`CLOSED UNTIL
  THE SPRING TIDES`) and its link is removed, not greyed into
  ambiguity. *No-JS:* complete cards. *Touch:* tap-haul per
  §6.7.
- **Breakpoints (v2).** ≥1200px: 3 across. 768–1199px: 2 across.
  <768px: 1 across, figure promoted (above).
- **Edge cases & failure modes (v2).** *Cards of unequal fact
  length:* the plate grid equalises by the figure line, which
  is anchored to the card's foot — facts may vary, figures
  align, because a row of cards is a row of instruments.
  *A harbour with no photograph:* the dial head (an engraved
  miniature of §6.10's dial set to the card's window) replaces
  it; a stock photograph of a different harbour is a §9
  failure. *Overflow grids (>9 cards):* paginate by plate
  (§6.12's rule), never scroll-jack a carousel — charts are
  laid side by side or not at all.
- **Accessibility spec (v2).** Cards are articles with real
  headings; the whole card is *not* a link (the named link is),
  so AT users get the facts without a single giant target.
  Figures are text. The mid-visit figure update is *not* a
  live region — a tide changing under a screen reader mid-
  sentence is noise; the value is correct when read.
- **Tokens consumed (v2).** `--buff`, `--buff-shade`,
  `--buff-line`, `--ink`, `--brass-deep`, `--ease-haul`,
  `--ease-flood`, `--lerp` (0.10).

### 6.15 The berth-request form

- **What & why.** The theme's one conversion: a request for a
  berth, a crossing, a table by the window at high water —
  presented as the machine's order plate. The visitor states
  their vessel (or party), their dates, and the turnings that
  bracket their visit — which arrive pre-filled if they marked
  them (§6.8). Submission does not "send a form": the machine
  takes the order, winds, and stamps the request with the next
  prediction number in the harbour's sequence. On the worked
  record, the Constants Plate (§6.11) prints 1,214 predictions
  drawn this season; the confirmation is therefore stamped
  **№ 1215** — the request becomes one of the machine's own
  predictions, entered in the same ledger. That derivation is
  the theme's whole theory of conversion: you are not a lead,
  you are a line in the harbour's book.
- **Structure.** A chart plate containing a real `<form>`:
  fields for name, vessel/party, arrival date, the bracketing
  turnings (two selects populated from §6.12's data — future
  turnings only), and a notes field. Labels in Newsreader
  15px, inputs as ruled ledger lines (bottom rule
  `--buff-line`, ink text, no boxes — the form is a page of
  the ledger). The submit control is a brass plate button
  engraved `ENTER THE REQUEST`. The confirmation replaces the
  form *in the same plate*: the stamped entry (§6.5's stamp at
  140% scale) with № 1215, the requested window restated in
  full format, and the harbour's undertaking in §12's voice.
- **Motion spec.** Field focus: the field's rule draws in
  `--brass-deep` (200ms `--ease-draw`) and the field hauls 2px
  (§6.7). Submit: the plate's miniature gear pair (§6.3's
  Cluster B geometry at 48px, in the plate's corner) turns
  through one full ratio cycle — great wheel 36°, pinion
  −360° — over 900ms while the request is sent; then the stamp
  lands (260ms `--ease-stamp`) on the confirmation entry. Total
  ceremony ≤1400ms after the response returns; the response
  itself is never waited on with a spinner — if it takes
  longer, the gears keep idling at ratio and the plate prints
  "the engine is winding" after 2000ms.
- **States.** Printed (empty ledger page) → filling (per-field
  focus states) → invalid (a field's rule turns `--red` and
  the error prints *in the ledger margin* beside the field, in
  §12's error voice — never a toast, never a shake) → winding
  (submit in flight) → entered (confirmation stamped, № from
  the record) → the entered state is the page's resting state;
  a second request starts from a fresh plate below, numbered
  onward.
- **Content merge.** The form's turnings come from §6.12, its
  pre-fill from §6.8, its number from §6.11, its stamp from
  §6.5, its gears from §6.3. It is the element where every
  other element's discipline pays out — remove the record and
  the form has nothing true to say.
- **Failure fallback.** The form is a working HTML form with a
  server action; JS adds pre-fill, gear ceremony and the
  in-plate confirmation. Without JS it submits and the server
  returns the entered plate as a page — the number derivation
  happens server-side from the same count, so № 1215 is issued
  identically with or without the ceremony. Submission failure
  (network): the plate prints the failure in the margin voice
  and *keeps the visitor's entries* — the ledger does not lose
  a page.
- **Reduced-motion variant.** No gear turn, no stamp landing;
  the confirmation prints whole. Focus rules still draw
  (instantly).
- **Performance budget & mobile variant.** The form adds no
  library; validation is native + a 40-line script. The gear
  ceremony reuses §6.3's generated paths. Mobile (<768px):
  single column, turning selects become stacked radio plates
  (48px targets) when the bracketing pair is the marked pair —
  the common case is two taps, not two dropdowns.
- **Choreography timeline (v2).** Arrive with marks → fields
  pre-filled, caption notes "your marked turnings are entered"
  → focus: rule draws 200ms → submit → t=0 gears begin ratio
  cycle → response returns → t=+0 stamp lands 260ms, dries
  90ms → confirmation figure (№ 1215) counts 600ms harmonic
  (§6.6) → entered. No marks: identical minus pre-fill.
- **State matrix (v2).** *Rest:* printed form. *Hover:* fields
  and button haul per §6.7. *Focus:* rule draw + haul; focus
  order is the ledger order (name → vessel → dates → turnings
  → notes → submit), never rearranged by layout. *Active:*
  submit press = the winding state. *Scrolled-past:* n/a.
  *Disabled:* while winding, fields lock (a ledger page being
  stamped is not edited); a harbour that takes no requests
  prints the plate closed with its reason and season, never a
  disabled grey form. *No-JS:* server round-trip, above.
  *Touch:* 48px targets, radio plates for the marked pair.
- **Breakpoints (v2).** ≥1200px: two-column ledger (fields in
  pairs), gear pair in the plate corner. 768–1199px: single
  column, gears kept. <768px: single column, gears cut (the
  stamp alone carries the ceremony).
- **Edge cases & failure modes (v2).** *Marked turnings that
  do not bracket the chosen date* (the visitor changed dates
  after marking): the margin prints the discrepancy in the
  form's voice and offers the correct bracketing pair as a
  one-tap correction — the machine checks the tide against the
  date, because that is its job. *A date with no turning pair*
  (beyond the wound drum, §6.12): the form says how far the
  drum is wound and takes the request as an enquiry, stamped
  `UNWOUND` instead of a number — a request beyond prediction
  is recorded as beyond prediction. *Double submission:* the
  winding state locks the plate; a second Enter is a no-op,
  and the server dedupes by the issued number.
- **Accessibility spec (v2).** Real labels, programmatically
  associated; errors use `aria-describedby` to the margin note
  and `aria-invalid` on the field — the red rule is never the
  only signal. The confirmation is a heading + text, announced
  by focus moving to it once (and only once). Required fields
  are marked in words ("required" in the label), not asterisks
  alone.
- **Tokens consumed (v2).** `--buff`, `--buff-line`,
  `--brass-deep`, `--brass`, `--red`, `--ink`, `--ease-draw`,
  `--ease-stamp`, `--ease-haul`, `--lerp` (0.10).

---

### 6.16 Engine transition & the pen-lift loader

- **What & why.** Moving between pages is turning a plate on
  the engine-room table: the pen lifts, the finished plate is
  taken away, the next plate is laid down and its border draws
  as it lands. No crossfade — paper does not dissolve (§5). The
  loader for slow arrivals is the same gesture held: the pen
  hovers, trembling (§6.1's idle tremor at 0.4px), above an
  undrawn plate whose border is printed — the machine is
  present and working; the chart is not yet drawn. Waiting is
  shown as a held pen, never as a spinning gear (a spinning
  gear in this theme would be a lie: the gears turn at ratio
  or not at all).
- **Structure.** A transition layer (fixed, `--buff`, above
  content, below nothing else) carrying one plate outline and
  the pen-arm group reused from §6.1 at gantry scale. Outgoing:
  the layer's plate prints the *leaving* page's title in the
  cartouche register for the duration of the turn — the visitor
  sees the plate being filed. Incoming: the new page renders
  beneath, and the layer lifts away as the new plate's own
  border draw (§5) completes.
- **Motion spec.** Total 840ms (§5): out 420ms — pen lifts 12px
  (120ms `--ease-slack`), plate slides down 24px and fades to
  the layer (300ms `--ease-haul`); navigation occurs at the
  covered midpoint; in 420ms — new plate settles (240ms
  `--ease-haul`) while its border draws (480ms, overlapping).
  Loader state: if the incoming document is not ready at the
  midpoint, the pen holds with its tremor and the plate's
  border draws to 82% and waits — the draw completes only
  when the page does. Hard ceiling: at 4000ms the layer is
  dismissed regardless (the watchdog), leaving whatever page
  exists beneath fully usable.
- **States.** Idle (layer absent) → lifting → covered
  (midpoint; loader sub-state if waiting) → laying → idle.
  A failed navigation returns through the same turn in
  reverse — the leaving plate is laid back down; the visitor
  is never left on the layer.
- **Content merge.** The transition is the machine's handling
  of its own plates: the leaving title, the pen, the border
  draw are all parts already met (§6.1, §5). It introduces no
  new visual vocabulary, which is why it can be brief.
- **Failure fallback.** Plain navigation. The transition is a
  JS-armed enhancement over ordinary links; without it, links
  behave as links have since 1993. The 4000ms watchdog
  guarantees the layer can never strand a visitor on a buff
  screen — the theme's standing rule applied to its most
  dangerous element.
- **Reduced-motion variant.** No turn. Navigation is instant;
  a 120ms fade of the masthead plate only, so the change of
  page is registered without a performance.
- **Performance budget & mobile variant.** The layer is one
  div, one SVG (≤4KB, paths shared with §6.1), transforms and
  opacity only. Mobile: the turn shortens to 560ms total and
  the pen is the nib only (§6.1's mobile ruling).
- **Choreography timeline (v2).** Click → t=0 pen lifts →
  t=120–420ms plate files away → t=420ms midpoint (navigate;
  loader holds if needed, border at 82%, tremor on) → ready →
  border completes, plate settles 240ms → t=840ms layer gone.
  Watchdog at t=4000ms dismisses unconditionally.
- **State matrix (v2).** *Rest:* absent. *Hover:* n/a (the
  layer takes no input; `pointer-events` pass through except
  during the covered 420ms, when they are captured to prevent
  double navigation). *Focus:* focus is moved to the new
  page's H1 at the midpoint and the layer is `aria-hidden`
  throughout. *Active:* n/a. *Scrolled-past:* n/a. *Disabled /
  no-JS:* absent; plain links. *Touch:* identical timings
  minus 280ms.
- **Breakpoints (v2).** ≥1200px: full pen arm. 768–1199px: arm
  shortened. <768px: nib only, 560ms.
- **Edge cases & failure modes (v2).** *Back/forward
  navigation:* the turn plays in the direction of travel —
  back lays the plate from the left file, forward from the
  right; the browser's own history is never intercepted beyond
  the visual turn, and bfcache restores skip the turn entirely
  (the page is simply *there*, as a filed plate should be).
  *Anchor links within a page:* no turn — the pen does not lift
  for a walk across the same chart. *Prefetch failure:* the
  midpoint falls back to a full load under the held pen.
- **Accessibility spec (v2).** The layer is `aria-hidden`,
  carries no text alternatives, and never holds focus. Screen
  reader users experience ordinary navigation with the new
  page's title announced by the browser as usual — the
  ceremony is visual only, by design.
- **Tokens consumed (v2).** `--buff`, `--buff-line`, `--brass`,
  `--ink`, `--ease-slack`, `--ease-haul`, `--ease-draw`,
  `--lerp` (0.10).

### 6.17 The margin tide staff

- **What & why.** The page's progress indicator, built as a
  tide staff: a vertical gauge in the left margin carrying a
  drawn curve that fills with ink as the visitor reads, rising
  toward a red high-water line positioned at the current
  section's flood point. Progress read as water level (§5) —
  you do not learn that you are "62% through"; you learn that
  the water has reached the third plate and the next mark is
  the method's high water. It is also §6.1's continuation: the
  pen's curve, having finished the hero, runs down the margin
  as the staff for the rest of the page.
- **Structure.** A fixed-position SVG rail in the left margin
  (≥1200px), 48px wide, full viewport height: a staff rule
  with height ticks (0–6m, the record's axis), the fill curve
  (a vertical sine segment whose inked length = reading
  progress through the page's plates), red high-water ticks at
  each section's flood point aligned with §6.5's stamps, and
  the current section's turning printed at the fill's head in
  tabular 12px (rotated 0° — the staff's figures read upright,
  in a small printed block at the rail's foot). The fill head
  carries the pen nib, parked from §6.1.
- **Motion spec.** The fill is scrubbed by the shared loop
  (lerp 0.10) from document scroll fraction mapped through the
  *page's own* curve shape — progress advances harmonically,
  faster through mid-page, slower at the first and last plates,
  because the staff is a tide, not a ruler. Crossing a section's
  red tick coincides (same frame) with that section's stamp
  landing (§6.5): the water reaches the mark and the mark is
  stamped — one event, two instruments.
- **States.** Rising (scrolling down) → slack (paused; the
  nib trembles, §6.1) → ebbing (scrolling up: the fill
  *falls* — progress indicators in this theme are honest about
  retreat; the stamps, however, stay stamped, §6.5) → full
  (footer reached: the staff stands at high water and the
  footer's curve (§6.9) takes the pen).
- **Content merge.** The staff's ticks are §6.5's stamps'
  positions and §6.12's turnings' order: three instruments
  reading one ascent. Its foot block prints the current
  section's next turning in full format — the margin is never
  without a true figure on it.
- **Failure fallback.** The rail ships printed with the fill at
  0 and all ticks visible; without the loop it is a static
  chart of the page's sections (a table of contents in gauge
  form) — legible and useful unanimated. The 2000ms watchdog:
  if the loop never confirms, the foot block prints the *first*
  section's turning (its static default) and the rail stands
  as the printed chart.
- **Reduced-motion variant.** The fill jumps between section
  ticks at section boundaries (four to six steps per page) —
  progress still readable, motion reduced to state changes.
- **Performance budget & mobile variant.** One path length
  write per frame. Below 1200px the margin does not exist
  (§4): the staff folds into the return-plate (§6.10) as a
  120px horizontal staff under the dial — same ticks, same
  fill, rotated into the plate. <768px: the horizontal staff
  keeps only the section ticks and the foot block's turning;
  the height axis is cut.
- **Choreography timeline (v2).** Hero completes → pen hands
  to the staff (nib fades from hero position to rail head over
  300ms as the hero leaves) → scroll: fill rises harmonically
  → each red tick crossing = same-frame stamp landing (§6.5)
  → footer: fill reaches high water, nib hands to §6.9's
  curve.
- **State matrix (v2).** *Rest:* fill at current progress,
  tremor on. *Hover:* hovering the rail prints all sections'
  names along the ticks (the rail becomes an index) — the one
  place the theme lets the margin speak prose. *Focus:* the
  rail is not focusable; its index function is duplicated by
  §6.10's navigation. *Active:* n/a. *Scrolled-past:* n/a (the
  rail is the scrolled-past, drawn). *Disabled / no-JS:*
  static chart. *Touch:* the folded horizontal staff; hover
  index replaced by the return-plate's own menu.
- **Breakpoints (v2).** ≥1200px: vertical rail, full axis.
  768–1199px: horizontal staff in the return-plate. <768px:
  horizontal, ticks + turning only.
- **Edge cases & failure modes (v2).** *Pages with one section*
  (the 404): the staff shows a single tick and stands at it —
  a staff with one mark is still a staff. *Extremely long
  pages:* the harmonic mapping is computed from plate offsets,
  so added plates redistribute the curve without any tick
  moving relative to its section. *Resize:* offsets re-read on
  the debounced resize; the fill fraction is preserved, never
  reset.
- **Accessibility spec (v2).** `aria-hidden` — progress is
  announced by the document's own headings; the rail's data
  (turnings, sections) all exists as text in §6.10 and §6.12.
  The foot block's turning duplicates §6.10's next-turning
  text.
- **Tokens consumed (v2).** `--ink`, `--red`, `--buff-line`,
  `--brass`, `--ease-flood`, `--lerp` (0.10).

### 6.18 Drained-chart skeletons, empty states & the off-chart 404

- **What & why.** The theme's waiting and absence states, drawn
  as what they are: a chart not yet drawn. Skeletons are
  *drained charts* — the plate's border and grid printed, the
  figures' places ruled and empty, the water gone out of the
  page. Empty states are plates that state, in the theme's
  voice, what the tide has not brought in. The 404 is the
  off-chart plate: a slate plate (§6.11's material) marking the
  edge of the surveyed water, with the way back drawn as the
  pen's route to the nearest charted page. Absence in this
  theme is surveyed and labelled, never improvised.
- **Structure.** Skeleton: plate outlines with `--buff-line`
  rules where figures will stand (heights as ruled lines of
  the correct tabular widths — a skeleton row is the exact
  width of the figure it waits for, so nothing shifts when the
  tide comes in). Empty state: a printed plate, the engraved
  heading (`NOTHING BROUGHT IN`), one sentence in §12's empty
  voice, and the plate's one permitted action (usually: read
  the next turning, §6.9's data, which is never empty). 404:
  a `--slate-deep` full plate, a charted coastline that ends
  mid-line — the drawn coast simply stops, with the engraved
  legend `HERE THE SURVEY ENDS` — the missing page's address
  printed as an unsounded depth (`— fathoms, no bottom —`),
  and three routes back (home plate, the weekly table, the
  constants) drawn as pen lines.
- **Motion spec.** Skeletons do not pulse. A drained chart is
  still: the only motion is the pen's held tremor (§6.16) if
  the wait exceeds 1200ms, and a single fill event when data
  arrives — figures print with §6.6 counters where applicable,
  rules ink over 300ms `--ease-draw`. Maximum skeleton life
  1200ms (§5) before the plate must resolve to content or to
  the honest empty state. The 404's coast line draws once on
  entry (900ms `--ease-draw`) and stops mid-line — the stop is
  the meaning.
- **States.** Skeleton: ruled → filling (data arriving) →
  printed (content) or → declared empty (timeout at 1200ms
  with no data: the plate converts to the empty state rather
  than ruling forever). Empty: printed, terminal. 404: drawn
  once, terminal.
- **Content merge.** The skeleton's ruled widths are generated
  from the real content's shape (the table's column widths,
  the card's figure width) — it is the content's own outline at
  low water. The 404's routes back are the site's three most
  charted plates, named and figured.
- **Failure fallback.** These states *are* the fallback layer
  of the theme; their own fallback is that they are static
  HTML requiring no loop: a skeleton that never fills is, at
  worst, a printed plate with an apology in the margin (§12's
  error voice) — and the 1200ms conversion rule is enforced by
  a plain timeout independent of the rAF loop, so a dead loop
  cannot strand a visitor on ruled lines.
- **Reduced-motion variant.** Identical, minus the coast draw
  (printed whole, still stopping mid-line) and the tremor.
- **Performance budget & mobile variant.** Skeletons are pure
  CSS plates — no assets, no JS weight beyond the timeout.
  Mobile: the 404's coast draws across the narrower plate with
  the legend beneath it; routes stack.
- **Choreography timeline (v2).** Data pending → t=0 ruled
  plate stands → t=1200ms either figures ink in (300ms) or the
  plate declares itself empty → terminal. 404 entry → t=0–900ms
  coast draws and stops → legend prints → routes draw
  (300ms each, ledger order) → terminal.
- **State matrix (v2).** *Rest:* terminal states as above.
  *Hover:* 404 routes haul (§6.7); empty-state actions haul.
  *Focus:* routes are ordinary links with §6.7's ring.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled / no-JS:*
  skeletons never appear (content is server-rendered); the
  404 is a static plate. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full plates. 768–1199px:
  skeleton rules keep content widths. <768px: 404 legend and
  routes stack; skeleton plates single-column.
- **Edge cases & failure modes (v2).** *Partial data* (a table
  whose last two days are unwound): the filled rows print and
  the unwound rows carry §6.12's honesty line — a skeleton is
  never used to disguise missing data that is known to be
  missing; skeletons are for *waiting*, not for *absence*.
  *Repeated empty states* (a search with no results, §11):
  the empty plate names the search's terms as the unsounded
  depth — the metaphor holds because the visitor's query is
  genuinely the thing not found.
- **Accessibility spec (v2).** Skeletons are `aria-hidden` with
  an `aria-busy` region announcing "the plate is being drawn"
  once; empty states and the 404 are real headings and text.
  The 404's coast SVG is `aria-hidden`; its legend and routes
  are text.
- **Tokens consumed (v2).** `--buff`, `--buff-line`,
  `--buff-shade`, `--slate-deep`, `--ink`, `--ink-soft`,
  `--ease-draw`, `--lerp` (0.10).

---

## 7. Page application map

**Home.** The full engine, in order: dial-plate masthead
(§6.10) → hero with the pen-drawn curve (§6.1), floating
headline (§6.2) and Cluster A gears (§6.3) → the day's four
turnings as a printed strip → harbour plate cards (§6.14) for
the harbour's services → the constants plate (§6.11) beside
the first three days of the prediction table (§6.12) → the
method in prose (an ebb section, §4) → the berth-request plate
(§6.15) → the honest footer (§6.9). The home page is the one
page that runs every element; it is the machine with its case
open.

**Listing (the full predictions).** The weekly table (§6.12)
is the page; week plates paginate by plate, never by infinite
scroll — a visitor turning to next week turns a plate (§6.16).
The constants plate pins beside the first week and then
releases. Filters, where a build needs them (harbour, month),
are dial registers (§11), and a filtered table re-derives from
the same function — a filter never reaches a second data
source.

**Detail (a berth, a service, a visiting window).** One plate
family: the subject's charted photograph (§6.13), its figures
as counters (§6.6), its own turnings table (the subject's
window extracted from §6.12's data), and the berth form
(§6.15) pre-set to the subject. The pen curve for the detail
page is the subject's *own* curve — a berth's depth curve, a
causeway's crossing curve — drawn by the same engine from the
subject's declared constants, which the build must supply or
the page does not ship (§10 check 1 applies per page, not per
site).

**About (the harbour, the firm).** An ebb-register page (§4):
prose-loose, the machine present but quiet — Cluster B gears
beside the method paragraph, the constants plate printed in
full as the firm's credentials, one charted photograph per
plate, stamps marking the founding flood and the record's
epochs. About pages in this theme prove themselves with
constants, not with adjectives.

**Contact / conversion.** §6.15's plate, reached from anywhere
with its marks (§6.8) intact. There is no separate checkout in
this theme: a request is entered, stamped and numbered, and
the harbour answers by its own means. A build that needs
payment takes it outside the theme (the theme's plates end at
the stamped entry; the confirmation says so, §12) — bolting a
generic checkout onto the engine room is a §9 failure.

**404 and utility pages.** §6.18. Search, where a build has it,
is an index plate (§11) whose results are turning-style rows;
its empty state is §6.18's surveyed absence.

---

## 8. Worked examples

### 8.1 The hero — "Tomorrow at Aldermouth"

The harbour authority's home hero, end to end. The plate is
1180px wide, chart buff, double-ruled. At its head, the
cartouche: "Tomorrow's tides for Aldermouth, drawn tonight" —
Fraunces 64px, three lines at most, floating (§6.2). Beneath
it the curve plate: the SVG (1200×420) with its printed axis —
hours 00–24, heights 0–6m — and the five constituent workings
faint beneath the sum.

*Scroll timeline.* t=0 (load): masthead border draws (480ms);
the hero plate's border draws (480ms); axis prints. t=300ms:
the pen lowers and draws the first six hours in 1800ms,
constituents in parallel, each at its phase. The day's four
turnings are already printed as text beneath the chart (the
fallback and the AT text): `HW 06:12 · 4.87 M · LOW 12:24 ·
0.61 M · HW 18:37 · 4.79 M · LOW 00:49 · 0.72 M` — the example
day's printings from the Aldermouth record (§6.11), intervals
6h12 / 6h13 / 6h12, the day's range 4.87 − 0.61 = **4.26 m**.
t=2100ms: the headline begins its 1400ms settle onto the
waterline at its centre — which sits over the morning flood,
so it comes to rest high on the curve, hesitates at the slack
(t≈2800ms), and floats. Cluster A, in the left margin, has
been idling at 4°/s since t=1500ms. As the visitor scrolls
the 180vh pin, the pen draws the remaining 18 hours; the
headline rides the newly drawn height as the draw passes
beneath it; at 24:00 the pen lifts and parks, and §6.5's first
stamp — the hero's own, printing `HW 18:37 · 4.79 M` — lands
on the plate's edge as the flood point crosses 62%. The
visitor leaves the hero having seen the whole day drawn, one
mark stamped, and the range counted (§6.6: 0 → 4.26 m,
2400ms harmonic, landing exactly on the printed figure).

### 8.2 Mid-page — the constants beside the week

Halfway down the home page, the method section: the slate
Constants Plate (§6.11) pinned at the left of the weekly
prediction table (§6.12) — the machine's credentials beside
its work. The plate prints the Aldermouth record in full:
five constituents, Z0 2.94 m, amplitude sum 3.08 m, spring
range 5.76 m, neap range 2.44 m, interval 12h25m, and the
season count, 1,214 predictions.

*Scroll timeline.* The section's turning slate announces an
ebb section (method) feeding a flood section (the table). As
the plate enters, its rows land in ledger order (40ms
stagger, rules drawing); the derived counters run — ranges at
1600ms, the 1,214 at 2400ms, all harmonic (§6.6). The
visitor hovers the M2 row: within a frame, the plate's
miniature curve highlights M2's constituent at full ink, the
hero (far above, off-screen) does the same for when they
return, and the plate's foot prints the derived line: "M2
alone would give a range of 3.72 metres" (2 × 1.86 — checked
against the record). Beside it, the week's 28 turnings enter
in ledger order; the visitor clicks the row for Saturday's
second high water and §6.8's stamp lands at its edge
(260ms), the caption count moving to "One turning marked."
The constants plate unpins exactly as the table's last row
passes — credentials and work leave the frame together.

### 8.3 Conversion — entering a berth request

The visitor marked two turnings in §8.2's table — the pair
bracketing a Saturday visit. The berth plate (§6.15) sits
below the table. Its caption reads: "Your marked turnings are
entered." The bracketing selects are pre-filled from
§6.8's session marks; the date field carries the Saturday.

*Scroll/submit timeline.* The plate enters with the standard
settle; the visitor adds a name and a vessel ("Moth, 6.2 m,
 dries out") — each focused field drawing its rule in
brass-deep (200ms). One field is left empty: on submit, its
rule turns red and the margin prints, in the form's voice,
"The vessel's draught is wanted — the harbour cannot promise
a berth it cannot float" (§12's error register). Corrected.
Second submit: the plate's gear pair turns one ratio cycle
(900ms — wheel 36°, pinion −360°) while the request is sent;
the response returns; the stamp lands at 140% scale (260ms,
drying 90ms); the confirmation counts to its number over
600ms: **№ 1215** — derived on the plate, in the open: the
season's 1,214 predictions (§6.11) plus this one. Beneath
the stamp, the entered window restated in full format —
`HW 06:12 · 4.87 M · ALDERMOUTH` … `LOW 12:24 · 0.61 M` — and
the harbour's undertaking: "The harbour will answer before
the next high water." The visitor's request is now a line in
the same ledger as the tides themselves, which is the
theme's entire argument, completed.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The decorative curve.** A hero "wave" drawn by a designer
   in a vector tool, vaguely sinusoidal, unrelated to any
   printed figure. *Cure:* the curve is generated from the
   Constants Plate (§6.1, §6.11) or the build does not ship.
   If a curve cannot be re-derived, it is clip-art with better
   PR.
2. **Gears that mesh wrong.** Decorative cogs with mismatched
   modules, teeth passing through each other, pairs rotating
   the same direction, ratios invented per page. *Cure:* one
   datum angle, geometry that encodes the ratio (§6.3), tooth
   counts printed. A visitor who counts teeth is this theme's
   favourite visitor; do not disappoint them.
3. **Steampunk costume.** Sepia filters, rivets on everything,
   Victorian clip-art borders, "ye olde" copy. *Cure:* the
   machine is *engineering*, drawn clean: engraved rules,
   honest brass, no distressing, no costume (§12 bans the
   vocabulary).
4. **Blue water.** Teal gradients, wave SVGs along section
   edges, a "nautical" navy-and-rope palette creeping in.
   *Cure:* §2 law 4 — the sea is slate or it is mathematics;
   it is never blue, and it never laps decoratively at a
   footer.
5. **Linear counters.** Numbers tweening evenly, or with a
   generic ease-out, in a theme whose whole point is harmonic
   motion. *Cure:* §6.6's shape, driven by the record, landing
   exactly on the printed figure.
6. **Red everywhere.** Sale badges, red buttons, red links,
   red "new" flags. *Cure:* §2 law 1's census — three red
   elements per viewport, each one a mark made by water or by
   a hand. Red is evidence, not emphasis.
7. **Invented precision.** "Trusted by 40+ harbours," tide
   times typed by a copywriter, a footer printing *a* harbour's
   tides from a stock table while the hero uses another set.
   *Cure:* one record (§6.11), every figure traced, the §10
   recomputation audit. In this theme a wrong number is not a
   typo; it is the one unforgivable defect.
8. **The hurried page.** Countdown timers, urgency banners,
   "only 2 berths left," motion everywhere at 300ms. *Cure:*
   §5's timing table — prompt or tidal, nothing busy in
   between — and §12's ban on urgency vocabulary.
9. **Floating everything.** The headline's float copied onto
   section titles, cards bobbing, a whole page at sea. *Cure:*
   §6.2 is the one licensed float; seasickness is not a brand.
10. **The hidden method.** Constants behind a tooltip, the
    method on a PDF, "proprietary algorithm" copy. *Cure:*
    §6.11 printed on the page, pinned beside the work. A
    machine that hides its workings is asking to be trusted;
    this one shows them and does not need to ask.
11. **Photographs that lie about the water.** A causeway shot
    at high water selling a low-water visit. *Cure:* §6.13's
    captioned tide state, checked like a figure.
12. **A generic checkout in fancy dress.** The engine's plates
    wrapped around a standard payment funnel. *Cure:* §7's
    ruling — the theme ends at the stamped entry (§6.15);
    payment lives outside, honestly labelled.

---

## 10. Quality gate

Blocking checks — the theme may not be used in a build unless
every one passes.

1. **One record.** A Constants Plate (§6.11) exists on the
   page (or one click from every page, printed, not in a
   tooltip), and every figure on the page — curve, counters,
   stamps, table, cards, footer — is traced to it in the
   build's figure register.
2. **Recomputation audit.** Five figures chosen at random
   (including the footer's next turning and one table row)
   are recomputed from the declared height function; all must
   agree within ±0.05 m and ±6 minutes.
3. **Gear audit.** Tooth counts, pitch circles and ratios
   agree (40:4 = 10:1; 32:8 = 4:1); one datum angle drives the
   train; meshing pairs counter-rotate. Verified by scrubbing
   6000px and measuring the pinion at −3600° ±1°.
4. **Red census.** No viewport shows more than three red
   elements; every red element is a stamp, a stamp-in-waiting,
   a flood tick, a focus ring or the active nav tick.
5. **Watchdog drill.** With the rAF loop killed, every element
   reaches its fallback state: curve printed, headline on its
   duplicate, gears as engravings, stamps as ghosts, counters
   at final values, transition layer dismissed within 4000ms.
6. **No-JS pass.** The full page read with JavaScript disabled:
   every figure, table, form and footer time present and
   correct.
7. **Reduced-motion pass.** With `prefers-reduced-motion`, the
   engine is at rest at high water (§5): no float, no breath,
   no draw, no count — and no content missing.
8. **Tabular audit.** Every data numeral on the page is set in
   tabular figures (§3 law 1); every tide time carries its
   height and harbour (§3 law 2).
9. **Timing audit.** No animation duration falls in the
   forbidden middle (900ms–90s) except §6.6 counters and
   §6.2's settle, per §5's table.
10. **Ambient census.** Exactly two ambient loops (breath,
    pen tremor). A third is a build failure, not a flourish.
11. **Photograph audit.** Every charted photograph's captioned
    tide state matches the state the image shows (§6.13).
12. **Non-builder sign-off.** The gate is signed by someone
    who did not build the page, with the figure register and
    the recomputation worksheet attached. The machine's
    examiner is never its maker.

Minimum bar summary: one record, traced figures, true gears,
rationed red, fallbacks drilled, and a page that reads
completely with the engine stopped.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Components the theme refuses are listed with
their in-theme replacements — a refusal without a replacement
is a gap, and this inventory has none.

| Component | Themed treatment |
|---|---|
| Primary button | A brass plate button: `--brass` face, engraved label in `--brass-deep` cut through to buff, 2px plate edge. Press: the plate seats 1px (the stamp's cousin, §6.15). Text is an instruction the machine can keep ("Enter the request", "Draw next week"). |
| Secondary button | A buff plate with a double engraved border and ink label; hover hauls 2px (§6.7). Never a ghost button — paper has no ghosts. |
| Text link | Ink, underlined with a `--buff-line` rule that draws to `--brass-deep` on hover (§6.7's draw). Links name destinations ("Aldermouth berths"), never "click here" or "learn more". |
| Form inputs | Ledger lines (§6.15): bottom rule, ink text, label above in Newsreader 15px. Focus draws the rule brass-deep. |
| Selects | Dial registers: a closed select shows its value as a dial label with a brass needle tick; the open list is a plate. Where the choice is a turning, options print in full format (§3 law 2). |
| Radio / checkbox | Stamps in waiting: a small double-rule square (radio: circle) that fills with a red tick — `--ease-stamp` — when chosen. The tick is a mark the visitor makes, so red is licensed (§2 law 1). |
| Tables | §6.12 is the pattern: real tables, tabular figures, flood banding in `--buff-shade`, red edge ticks at high water. |
| Cards | §6.14 harbour plates. |
| Badges | Refused as decoration. The one badge-form the theme admits is the state marker (`SPRINGS`, `NEAPS`, `GONE`, `UNWOUND`) set in the dial register on a plate rule — a reading, not a sticker. |
| Alerts | Margin notes: an alert prints in the plate's margin in the §12 voice, ruled in red only when the matter is the tide itself (a changed prediction, a closed berth). Info alerts are ink; the margin is the channel (§6.15's errors live there too). |
| Toasts | Refused. Nothing in a chart room pops up and vanishes; a message that matters is entered in the margin and stays until read. Replacement: margin notes (above) and the form's entered state (§6.15). |
| Modals | Refused. The machine has no trapdoors. Content that would be a modal becomes a plate on the page (the constants method note is §6.11, printed, not a dialog). The one exception: none. |
| Tabs | Turning slates: a row of slate tabs named by their state (Flood / Ebb / Method), the active slate in `--slate` with buff text, switching with §5's plate settle. Tab panels are plates. |
| Accordion | The chart drawer: rows that haul open (§6.7's `--ease-haul`, 380ms) like drawers in the chart cabinet, each labelled with what it holds ("The lesser constituents"). One drawer open at a time — a cabinet rule. |
| Pagination | Plate turning (§6.12, §6.16): "Next week" is a plate edge with the week's first turning printed on it. Numbered pages, where unavoidable, are folio numbers in the plate corner — charts have folios. |
| Breadcrumbs | The pen's route: a line of named plates separated by drawn ticks, the current plate stamped (§6.5 at 60% scale). |
| Progress | §6.17's tide staff. A percentage bar anywhere is a §9 failure. |
| Loader | §6.16's held pen / §6.18's drained chart. Spinners refused in all forms. |
| Search | An index plate: the query field as a ledger line, results as turning-style rows (name, one figure, plate reference). No-results is §6.18's surveyed absence naming the query as the unsounded depth. |
| Tooltip | Refused. Anything worth saying is printed (the constants plate prints contributions at its foot, §6.11). Hover reveals emphasis and highlights, never sole-copy information. |
| Date display | Always with its harbour and, where a tide is implied, its turnings (§3 law 2). Relative dates ("in 3 days") are refused — the machine deals in dates and times. |
| Price display | Where a service has a price, it prints as a figure in the ledger register (tabular, with its unit and what it buys: "£18 · the berth, per tide"). Prices never perform (no strikethrough theatre, no countdown). |
| Footer | §6.9, without exception. |

---

## 12. Content & copywriting voice

Two registers, one rule: **the machine reports; the harbour
understates.**

**The Machine register** — predictions, tables, stamps,
confirmations. Declarative, dated, figured. Every sentence in
this register can be checked against the record, and most
contain a number.

- ✓ "High water 18:37, 4.79 metres. The causeway is covered
  from 16:50."
- ✓ "Entered as № 1215. The harbour will answer before the
  next high water."
- ✗ "Don't miss tonight's spectacular high tide!!" (urgency,
  exclamation, an unfigured superlative — three bans in nine
  words.)
- ✗ "Tides are super high this weekend" (no figure, no
  harbour, no date — the machine does not deal in "super".)

**The Harbour register** — prose, about pages, the method.
Plain, unhurried, first-person-plural where the harbour speaks
of itself. It explains the machine without mystique and
without apology.

- ✓ "We have predicted the tides at Aldermouth from the same
  five constituents since the plate was fitted. The workings
  are printed beside the table; check them."
- ✓ "The engine does not hurry, and neither does the water.
  Your berth is kept from the first high water of your stay."
- ✗ "Our cutting-edge proprietary tidal algorithm leverages…"
  (the machine is not an algorithm to its harbour; it is an
  engine with a plate on it.)
- ✗ "Ye tides of olde…" (costume voice — §9 failure 3. The
  harbour speaks modern English with good manners.)

**Headline style.** Statements of fact with a date in them
(§3 law 4): "Tomorrow's tides for Aldermouth, drawn tonight."
A headline that could run on any day is rewritten until it
could only run on its own day.

**Label style.** Dial register (§3): short, nominal, exact —
`NEXT TURNING`, `SPRING RANGE`, `MARKS`. Labels never contain
verbs of persuasion.

**Error voice.** The margin register: what is wanted, why the
harbour needs it, in one sentence, without blame.

- ✓ "The vessel's draught is wanted — the harbour cannot
  promise a berth it cannot float."
- ✓ "That turning has gone. The next is printed above."
- ✗ "Oops! Invalid input." (No "oops" in a chart room; no
  "invalid" — the entry is *wanting*, not wrong.)

**Empty-state voice.** §6.18's register: name what the tide
has not brought, and print the next turning, which is never
empty.

- ✓ "Nothing brought in on this tide. The next high water is
  18:37, 4.79 metres, and the table turns with it."
- ✗ "Nothing here… yet 👀" (no emoji anywhere in the theme;
  no "yet" doing urgency's work.)

**Fixed strings (verbatim, never paraphrased).** The stamp
format `HW 18:37 · 4.79 M`; the full-format turning
`HW 06:12 · 4.87 M · ALDERMOUTH`; the unwound line "the drum
is wound to [date]; further weeks are drawn as the constants
are proved"; the footer line "drawn from the constants printed
on this page"; the closed-berth line `CLOSED UNTIL THE SPRING
TIDES` (with the actual reopening turning printed beneath it
in full format — a fixed string is never an excuse to omit a
figure).

**Banned vocabulary.** "Leverage", "cutting-edge", "seamless",
"spectacular", "don't miss", "hurry", "limited time", any
exclamation mark in the Machine register, any emoji anywhere,
and "algorithm" where "engine" is true.

---

## 13. Full-page scroll choreography map

The home page (§7), beat by beat, top to footer. The breath
(§6.4) runs under all of it; the staff (§6.17) reads all of it.

1. **Arrival.** Masthead plate border draws (480ms); needle
   settles from the stored angle (600ms); the next real
   turning prints beside the dial. The visitor knows where
   the water is before they have read a word of copy.
2. **The hero draw.** Hero border draws; pen lowers at
   t=300ms; the first six hours draw (1800ms) with the
   constituents beneath; the day's four turnings stand printed
   under the chart from the first frame.
3. **The settle.** Headline floats down onto the waterline
   (1400ms, slack dwell at its middle) and begins its ±4px
   breath bob. Cluster A is idling in the margin (4°/s since
   1500ms of stillness).
4. **The crank.** Scrolling the 180vh pin draws the remaining
   18 hours; gears take up their scroll drive (great wheel
   6°/100px, pinion −60°/100px); the headline rides the draw
   as it passes beneath. At 24:00 the pen lifts, parks, and
   hands its nib to the margin staff.
5. **First stamp.** The hero plate's flood point crosses 62%:
   its high-water stamp lands (260ms + 90ms dry) in the same
   frame as the staff's fill crosses the matching red tick.
   The visitor has been *marked in* — progress is now a
   physical record in the margin.
6. **The turnings strip and cards.** The day's strip prints;
   harbour cards settle in reading order (40ms stagger),
   figures counting harmonically where they count. The page
   alternates: flood (figures) giving way to ebb (prose) at
   each turning slate.
7. **The method.** Cluster B's station: the prose plate, gear
   pair at ratio beside it. Density drops; the breath is most
   noticeable here, by design — the page's quietest room is
   where its rhythm is felt.
8. **Constants beside the week.** The slate plate pins; rows
   land in ledger order; counters run (1,214 over 2400ms);
   the week's 28 turnings enter beside it; stamps land day by
   day as the visitor reads down; marks (§6.8) are made here,
   most visitors' first.
9. **The request.** The berth plate: marks pre-filled, rules
   drawing under focus, and — on submit — the gear cycle, the
   stamp, № 1215. The choreography's climax is a number being
   entered in a book.
10. **The footer.** The staff stands at high water; the pen
    crosses to the footer and draws tomorrow's curve (1200ms);
    the four turnings count; the machine plate prints the
    engine's specification. The page ends with a prediction
    for a day the visitor has not seen yet — the machine
    still working as they leave.

**Reverse pass.** Scrolling up: gears reverse exactly, the
staff's fill ebbs, stamps stay stamped, counters stay settled,
cards stay charted. The page never re-performs; going back is
walking back through a chart room where the marks you made are
still on the charts.

**Jump scroll.** A visitor who jumps (scrollbar drag, End
key) gets the completed state: all stamps whose flood points
are passed land in one frame at 40ms stagger (§6.5), counters
stand at final values, the curve stands drawn. The machine
does not re-enact history for a visitor who skipped it.

---

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home, desktop) | ≤820KB | HTML/CSS/JS ≤210KB; SVG (curve, gears, dial, staff) ≤26KB generated; photographs ≤120KB each, ≤480KB per page (§6.13) |
| Fonts | ≤96KB | Fraunces (one optical-size variable file, subset to Latin + figures) + Newsreader (variable, subset); tabular figures are in the subset — a subset that drops them fails §10 check 8 |
| Frame budget | ≤1.6ms JS per frame | The shared loop's writes: ≤6 transforms, 1 custom property (`--breath`), ≤3 counter text writes (§6.6), 1 path length (staff). No layout reads inside the loop — all offsets are cached at arm/resize. |
| Long tasks | None >50ms | Curve generation (288 samples × 5 constituents) is the largest task at ≈4ms; it runs once at load, once per debounced resize. |
| Layout stability | CLS 0.00 | Plates reserve their full geometry; the breath moves only gaps between rigid plates (§6.4); figures are tabular (§3 law 1). |
| Interaction latency | Haul/stamp first frame ≤16ms after the event | Both are class/transform changes prepared at arm time. |

**Cut order when the budget is exceeded** (in this order —
cut from the top, restore from the bottom):

1. Constituent curves beneath the sum, from five to two (M2,
   S2) — on all viewports, not just mobile.
2. Cluster B gears (the mid-page station); Cluster A never
   cuts.
3. Photograph count per page (fewer, larger plates).
4. The pen arm's linkage (nib only, §6.1's mobile form) at
   desktop too.
5. The headline's scrubbed ride (breath bob only).

**Never cut:** the Constants Plate, any figure, any fallback,
the watchdogs, the footer turnings, the reduced-motion
variants. A build that balances its budget by removing the
method or the fallbacks has not understood what the budget is
for.

---

## 15. Build-order checklist

1. **Declare the record.** Survey or obtain the harbour's
   constants; write the Constants Plate data (§6.11) and the
   figure register. Nothing is designed before the record
   exists.
2. **Build the height function** and prove it against the
   record's derived values (spring 5.76, neap 2.44, interval
   12h25m on the worked record) — the §10 recomputation
   worksheet starts here.
3. **Static printed page first.** The complete page with the
   engine stopped: full curve drawn, all figures printed,
   table, form, footer — passing §10 checks 6 and 8 with no
   JavaScript present.
4. **Tokens and plates.** Palette (§2), type scale (§3),
   plate geometry and grid (§4).
5. **The shared loop** with its datum angle, scroll sample,
   breath phase and watchdog registry (§5).
6. **The curve and the headline** (§6.1, §6.2), including the
   text alternative generated from the record.
7. **Gears** (§6.3) — generated teeth, one datum, printed
   ratios.
8. **Breath** (§6.4) wired to gaps only.
9. **Stamps and counters** (§6.5, §6.6) — ghosts, landings,
   twin-node counters.
10. **Haul and marking** (§6.7, §6.8) with session persistence.
11. **Footer** (§6.9) — build-rendered turnings, machine
    plate, date-line rules.
12. **Navigation and staff** (§6.10, §6.17) — dial, drawer,
    folded staff forms.
13. **Table and cards** (§6.12, §6.14, §6.13) from the one
    function; photograph tide audit.
14. **The form** (§6.15) — server issue of the prediction
    number first, ceremony second.
15. **Transitions and absence** (§6.16, §6.18), then the full
    §10 gate — recomputation, watchdog drill, red census,
    no-JS and reduced-motion passes — signed by a non-builder
    (§10 check 12) before the theme is used.

---
