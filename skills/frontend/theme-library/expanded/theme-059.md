# 59. Linen Field — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** From flax field to woven cloth in one scroll: the page
opens as a blue-flowered flax field, is harvested, retted, scutched,
spun — and ends as finished linen that the final sections are
literally printed on. Palette anchors: flax stem `#A8B98A`, flax
flower `#8FA3C7`, retted straw `#D9C9A3`, woven linen `#EFE9DA`, loom
shadow `#4A4238`. Type: Newsreader (display) + Source Serif 4
(body). The background itself is the product in progress — loose
burlap weave up top, tightening stage by stage to fine damask at the
footer; a single margin thread is spun finer and woven denser per
section as the progress indicator; thread counts are treated as
poetry in the copy ("woven at 165 threads, because 200 felt like
showing off").

## 1. Concept & world

Linen Field is a process page wearing its own manufacture. The
visitor does not read *about* how linen is made while looking at a
picture of linen; the ground under the words is itself at whatever
stage of making the scroll has reached. At the top the reader stands
in the crop — blue flax flowers on green stems, the weave beneath
the text so loose it is barely cloth at all, more a memory of
burlap. Scrolling is working: the field is harvested, the stalks are
retted in water until the fibres loosen, scutched and hackled clean,
spun into a single thread, and woven — and at each stage the page's
own ground tightens one step, until the footer and the order form
sit on fine damask and the closing copy is, without metaphor,
printed on finished linen.

**The theme's one law: the ground is earned.** No section may rest
on cloth finer than the scroll has woven. Weave fineness is a single
global value — `--weave`, 0 at the field (14px burlap pitch) to 1 at
the footer (3px damask pitch) — produced by one declared function of
scroll progress and printed four ways: the background texture, the
image frames (§6.8), the margin thread (§6.6) and the footer's
damask field (§6.17). A build in which any one of the four disagrees
with the others — a damask-framed photograph sitting in the raw
field, a footer finer than the form above it — has broken the law,
and §10's audit fails it. The companion law governs figures: every
printed number — thread count, harvest weight, retting days, metres
woven — is a field of one crop record object (§6.15), printed in
several places but authored once. Invented figures are a blocking
gate failure, not a copywriting shortcut.

**Best fit.** Linen and natural-textile makers, certainly — bedding,
table linen, apparel cloth — but the deeper fit is any maker whose
product is a slow agricultural or craft process the buyer should
*feel* taking time: heritage mills, seed-to-garment brands,
farm-produced fibre, natural dye houses, basketry and rope works
whose material journey is the argument. Audiences: buyers who pay
premiums for provenance and process; readers who will trade speed
for the sensation of a thing being made properly. The theme rewards
long, unhurried scrolling and punishes skimming — deliberately.

**When NOT to use it.** Not for anything whose promise is speed,
novelty or disposability: the page's whole rhetoric is that good
cloth takes a season. Not for data-dense dashboards — the grounds
are textured and the density law (§4) caps how much may sit on one
screen. Not for a product with no process story: if the material
arrives from a supplier's catalogue with no field behind it, the
tightening weave is a lie told in texture, and the theme's law
forbids it. Not for urgent conversion flows — the checkout
equivalent (§7) is the last stage of a journey, and a visitor who
lands there cold gets the fallow-page honesty of §6.18, not a
shortcut.

**Mood.** Agricultural patience rendered in cloth: sun, water, and
the slow violence of retting, resolved into the calm of a folded
sheet. Nothing on the page hurries. Even the hover is a palm
smoothing fabric (§6.9).

**Why the order is the economics.** Linen costs what it costs
because of the retting dam and the scutching line — weeks and labour
that a synthetic cloth skips. A page that opens on finished damask
and *mentions* the process asks the visitor to take the price on
faith; a page that makes the visitor's own scroll perform the five
stages has shown the receipt before showing the price (§6.14's form
is deliberately unreachable in spirit until the weaving stage —
§7's map places it there). This is why the stages may be shortened
but never reordered or skipped (§6.2): a skipped retting is not a
design shortcut, it is a false claim about how the cloth was made,
and visitors who know linen — the audience this theme is for — can
tell a skipped stage the way a weaver can tell a missed beat.

## 2. Palette

Five anchors, inherited exactly. Four derived tokens, each a
darkening of an anchor for text duty, because two of the anchors
(flax stem, flax flower) are field colours that cannot carry text on
linen — measured 1.74:1 and 2.11:1 respectively, ruled never-text
below. Contrast figures were computed for this expansion (WCAG
relative luminance) and are stated beside every pairing that carries
words.

| Token | Hex | Role | Ratio / pairing law |
|---|---|---|---|
| `--stem` | `#A8B98A` | Flax stem green: field bands, stage washes, the spun thread's first state | 4.69:1 on `--loom` — graphical and large-display only; never body text |
| `--flower` | `#8FA3C7` | Flax flower blue: the hero flowers, stage markers, one licensed accent per stage band | 3.87:1 on `--loom` — graphical only; never text at any size |
| `--straw` | `#D9C9A3` | Retted straw: the retting/scutching stage grounds, skeleton burlap, card cloth in mid-page | `--loom` on it 6.03:1 — text licensed |
| `--linen` | `#EFE9DA` | Woven linen: the default ground from spinning onward, all finished cloth | `--loom` on it 8.15:1 — the primary text pairing |
| `--loom` | `#4A4238` | Loom shadow: all body text, rules, the weave's shadow threads | 8.15:1 on `--linen`; 6.03:1 on `--straw` |
| `--stem-deep` | `#4F6136` | Derived: stem darkened for text — stage labels, links, the thread's spun state | 5.60:1 on `--linen` — text licensed |
| `--flower-deep` | `#46587C` | Derived: flower darkened for text — data figures, the one blue word per stage | 5.88:1 on `--linen` — text licensed |
| `--straw-deep` | `#6E5F43` | Derived: straw darkened — captions, datelines, the crop record's small print | 5.13:1 on `--linen` — text licensed at ≥13px |
| `--loom-soft` | `#5C5344` | Derived: loom shadow lightened one step — secondary text on finished cloth | 6.25:1 on `--linen` — text licensed |

**Usage ratios.** Across a full page: `--linen` ≈55% of surface (it
wins as the scroll proceeds), `--straw` ≈15% (the middle stages),
`--stem` ≈12% (field and stage washes), `--loom` ≈10% (text and
shadow threads), `--flower` ≤3% — the blue is a flower, not a brand
colour; a page where blue exceeds 5% of pixels has planted a garden,
not a field (§9, failure 4). `--flower-deep` and `--stem-deep`
together carry ≤5% as text accents.

**The weave is drawn in palette.** The background texture (§6.1) is
never a grey noise: its warp threads are the ground token of the
current stage and its weft shadows are `--loom` at 6–10% — the cloth
is coloured by the same tokens as the copy, which is why text
contrast survives on it (§5's texture law: texture lives in
background layers only, and every text-bearing ground is one of the
three licensed pairings above, checked at its stage).

**Dark ruling — the field at dusk, not an inversion.**
`prefers-color-scheme: dark` does not invert the page. Grounds
deepen toward `--loom`: the field becomes a dusk field (stem washes
at `--stem` 22% over `--loom`), finished-cloth sections become
shadow-cloth with `--linen` text at 8.15:1, and the weave renders as
shadow-on-shadow (weft at `--linen` 5%). The flowers keep `--flower`
at graphical strength — a blue visible at dusk, which is when flax
flowers are in fact most noticeable. The footer damask prints in
`--linen` on `--loom`. Nothing turns white-on-black; the cloth gets
evening, not a negative.

## 3. Typography

Two faces, inherited: **Newsreader** for display (its optical sizes
let the hero print large and soft, like type pressed into cloth) and
**Source Serif 4** for body and data. No third face is licensed; the
crop record's figures are Source Serif 4 tabular, never a grotesque
imported for "data credibility" (§9, failure 9).

**The scale** (desktop ≥1200px; §6 breakpoint fields carry the
smaller sizes): hero display 64px Newsreader 480, optical size auto,
line-height 1.04, tracking −0.01em at rest (the tightening headline,
§6.5, *begins* at +0.06em and beats down to this); stage titles 40px
Newsreader 500, lh 1.12; section heads 28px Newsreader 560, lh 1.2;
standfirst 20px Source Serif 4, lh 1.55; body 17px Source Serif 4,
lh 1.62, measure 62ch maximum; captions and datelines 13px
`--straw-deep`, lh 1.5, tracking +0.01em; figures (thread counts,
weights) 15px tabular Source Serif 4; the margin thread's stage
labels 12px `--stem-deep`, small caps, tracking +0.14em.

**Five type laws.**

1. **Type is printed, never pasted.** Display text always sits
   directly on the stage's cloth ground — never on a card floating
   above a different ground, never with a drop shadow. The one
   shadow licensed on the page belongs to the weave itself.
2. **Figures are facts and set like them.** Every number from the
   crop record sets tabular, unadorned, at body size or one step up
   — never in display size, never coloured `--flower`. A thread
   count shouted at 64px is a billboard, not a record (§9, failure
   7).
3. **Italics are the grower's voice.** Newsreader italic is reserved
   for first-person field notes and the copy's poetic asides —
   including the fixed line "woven at 165 threads, because 200 felt
   like showing off." System copy, errors and labels never italicise
   (§12).
4. **One blue word per stage.** `--flower-deep` may colour at most
   one word or figure per stage band — the stage's name in its
   dateline, or its governing figure. Two blue words and the eye
   reads a link farm, not a flower (§9, failure 4).
5. **The headline beats down.** Display tracking is a process value:
   headlines enter at +0.06em over loose weave and are beaten to
   their rest tracking as their reveal completes (§6.5). A headline
   found at rest tracking before its beat has finished is a build
   error the §10 gate checks by screenshot timing.

**Line-height grows with the making.** Body lh is 1.62 on finished
cloth but the field sections set at 1.7 — loose ground, loose lines;
the tightening is felt in the text block before it is seen in the
texture. Stage datelines always precede their titles (the record
before the claim, §12).

## 4. Layout language

**The page is one bolt, unrolled downward.** Sections are not cards
on a ground; they are consecutive lengths of the same cloth, joined
at stage boundaries marked by a woven selvedge rule — a 6px band in
which the weave runs at double density, the cloth's own seam. There
are no section background colour changes: the ground changes only by
*stage* (§6.2), five times on a full journey page, and the change is
a texture-and-tint step the scroll performs, not a designer's
alternation.

**Grid.** ≥1200px: a 12-column grid, content measure 7 columns
centred-left, a 148px right margin rail reserved for the thread
(§6.6) and its stage labels — the margin is the loom's edge, and
nothing else may be placed in it. 768–1199px: 8 columns, margin rail
64px, thread only. <768px: single column, the thread retires to a
3px top selvedge (§6.6's mobile variant). Body measure caps at 62ch
everywhere; figures and the crop record table may use 9 columns.

**Density falls as the cloth finishes.** Field sections are airy —
the crop needs room — with stage bands of 90–120vh and copy in short
lengths. Spinning and weaving sections tighten: longer copy, the
record table, the product cards at 3-across. The footer damask is
the densest surface on the page and the calmest: density of
*information* rises exactly as density of *texture* falls. A build
that crowds the field or airs out the footer has the rhythm
backwards (§9, failure 6).

**Whitespace is fallow.** Unplanted space in field sections is left
genuinely empty — no decorative SVG, no watermark flower. In cloth
sections whitespace is the unprinted part of the sheet and is kept
clean of texture at full strength: the damask ground under the
footer copy prints at 60% texture opacity so the last length reads
as the finest, quietest cloth (§6.17).

**Stage bands and pins.** The five stages (§6.2) are the page's only
pins: each stage band pins for 60vh of scroll while its ground step
completes. Everything else scrolls naturally. Total pinned distance
on a journey page is capped at 300vh; a page that needs a sixth pin
has a sixth stage, and flax has five.

**The margin thread's geometry.** The thread runs the rail's centre
from the hero's baseline to the footer's final line. Its state —
fuzzy fibre, spun yarn, woven stripe — is a function of `--weave`,
never of local section styling: one thread, one journey, printed
identically on every page type (§7).

## 5. Full motion system

Five named easings, authored for cloth and crop — no generic
ease-in-out anywhere in the theme:

- `--ease-beat`: `cubic-bezier(.2,.9,.25,1.15)` — the loom's beat:
  a firm approach and a 4px settle past the mark, used by stage
  locks and the headline's beating. Overshoot is vertical only and
  capped at 4px.
- `--ease-loom`: `cubic-bezier(.33,.8,.3,1)` — the loom-beam mask
  rising (§6.4): steady, unhurried, no bounce; cloth does not
  bounce.
- `--ease-breeze`: `cubic-bezier(.45,.05,.55,.95)` — a sine
  approximation for stems and the ambient sway wave (§6.3): slow in,
  slow out, the middle fastest, like wind arriving.
- `--ease-weave`: `cubic-bezier(.25,.6,.35,1)` — texture crossfades
  and stage ground steps (§6.1, §6.2).
- `--ease-press`: `cubic-bezier(.3,.7,.4,1)` — the crease press and
  the palm band's settle (§6.9, §6.10): pressure applied, then held.

**The shared loop.** One `requestAnimationFrame` loop, lerp **0.12**
for scrubbed values (weave fineness, thread draw, stage progress),
**0.18** for the palm band's light (a hand moves faster than a
loom), drives every scroll-coupled value on the page. No scroll
handler writes styles. The loop sleeps when the tab is hidden and
when no value is more than 0.001 from its target.

**Motion vocabulary — translated or refused.** Scroll-triggered
reveals: the loom-beam (§6.4). Pinned scenes: the five stages
(§6.2), the only pins. Parallax: flax stems against woven layers at
0.92×/1.06× in field sections only — cloth sections do not parallax,
finished cloth lies flat. Masked line reveals: the loom-beam mask,
and the headline's fibre-through print (§6.5). Blur-to-sharp:
**refused** — linen is never out of focus; the headline's fibres
fade, the letters never blur. Animated counters: crop-record figures
(§6.15), counting only between two true values. Progress indicator:
the margin thread (§6.6) — progress is never a percentage, a bar, or
a number (§9, failure 3). Marquee: **refused** — cloth does not
crawl; the footer's process strip is a still recap. Ambient loops:
exactly two — the breeze wave (§6.3) and, on the footer only, the
damask's light at rest — and the breeze is the page's single
licensed ambient motion above the footer. Micro-interactions: palm
band (§6.9), crease press (§6.10), card corner-lift (§6.13). Page
transitions: the cloth-lift (§6.16). Image treatments: scale-in-frame
inside stage-matched woven frames (§6.8), and the stem draw (§6.7) —
the theme's one SVG line-draw, rationed to a single diagram per
page.

**Durations ledger (the binding numbers).** Loom-beam reveal 700ms;
headline beating 1200ms cap; stem draw 1800ms; breeze pass 2500ms,
ambient repeat every ~25s at 40% amplitude; stage beat settle 260ms
(the 4px `--ease-beat` lock); stage ground crossfade 600ms
`--ease-weave`; weave scrub continuous, no duration — it is a
function, not an animation; crease fade-in 300ms `--ease-press`;
palm band travel lerped at 0.18, settle 240ms; card corner-lift
350ms; counter roll 900ms; cloth-lift transition 550ms out / 450ms
in; skeleton minimum display 400ms, hard resolve 2000ms.

**The texture law.** All texture crossfades, weave scrubs and stage
grounds live in background layers (`::before`/dedicated ground divs,
`pointer-events: none`, `z-index` below content). Body text always
sits on one of §2's three licensed pairings at its stage. An
animation that would move, fade or cover the text layer itself —
beyond the armed pre-states of §6.4/§6.5, each watchdog-backed — is
not a Linen Field animation and is refused at review.

**Watchdog ledger (every cap on the page, in one place).** Weave
crossfade freeze 1600ms (§6.1); stage-pin crossfade snap 1200ms
(§6.2); breeze return-to-upright 3000ms (§6.3); loom-beam reveal
1600ms, with a 2500ms global disarm sweep after load (§6.4);
headline beat snap 1400ms (§6.5); stem-draw completion 2200ms
(§6.7); skeleton hard resolve 2000ms (§6.16); transition cloth
removal 1200ms (§6.16). A build that introduces an armed state
without adding its cap to this ledger fails §10's no-strand audit
by construction — the ledger is the audit's checklist.

## 6. Signature elements

### 6.1 The tightening weave

- **What & why.** The page's background is a woven texture whose
  thread spacing scrubs continuously tighter across the full scroll
  — loose burlap at the field (14px pitch), fine damask at the
  footer (3px pitch). It is the theme's thesis rendered as ground:
  the reader does not scroll past the process, the reader's scroll
  *is* the process, and by the footer the copy is printed on finished
  linen because the visitor wove it there.
- **Structure.** A fixed ground stack behind all content: five
  authored texture layers (one per process stage, §6.2), each an
  inline SVG warp-and-weft pattern tiled at its stage's pitch —
  14px, 10px, 7px, 5px, 3px — warp threads in the stage's ground
  token, weft shadows in `--loom` at 6–10%. Adjacent layers crossfade
  by opacity under the shared loop; a sixth, continuous layer carries
  a fine 3px damask motif (a woven diamond, drawn in thread, not
  printed) whose opacity is `--weave` itself, so the finished
  pattern literally fades in as the cloth finishes. The whole stack
  is `aria-hidden`, `pointer-events: none`.
- **Motion spec.** Trigger: scroll, global. `--weave` = the declared
  function: page scroll progress mapped through the five stage bands
  (§6.2), each band contributing its fifth; within a band the value
  eases with `--ease-weave` at the band's edges so no pitch step ever
  jumps. Lerp 0.12 in the shared loop. The texture never animates on
  a timer — a still page has still cloth.
- **States.** Rest: the stage's texture, settled. Scrolled-past /
  scrolled-back: fully reversible — scrolling up loosens the weave
  again, because the journey is the visitor's to retrace; only the
  stage *locks* (§6.2) are one-way. Hover/focus/active: none — the
  ground is not a control.
- **Content merge.** The ground is the product being made; every
  other element reads its state from `--weave` (frames §6.8, thread
  §6.6, footer §6.17), so the weave is not a backdrop but the page's
  central fact, printed four ways per the law in §1.
- **Failure fallback.** No JS: the ground stack ships at its
  mid-stage layer (7px, straw-woven) as a static texture — the
  original entry's reduced-motion ruling applied to the no-JS case:
  a fixed, honest, mid-fineness cloth under everything, all copy
  fully readable. If the loop stalls, a 1600ms watchdog freezes the
  crossfade at whichever layer pair is nearest settled; texture can
  never strand mid-fade over text because both layers sit under the
  licensed text pairings at every blend (§2).
- **Reduced-motion variant.** The weave rests at mid-fineness for
  the whole page (7px straw weave, static), exactly as the original
  entry rules; stage bands print as a static process strip (§6.2).
  The information — this ground is woven, in stages — survives; the
  scrub rests.
- **Performance budget & mobile variant.** Five SVG pattern layers,
  ≤18KB total inline; animation is opacity on composited layers
  only — no background repaint of the content layer, no layout.
  Budget: ≤0.5ms/frame of the shared loop. Mobile (<768px): three
  layers (14px, 7px, 3px), the damask motif layer cut, crossfades
  stepped at stage boundaries instead of continuous.
- **Choreography timeline (v2).** Continuous: scroll Δ → target
  `--weave` recomputed → lerped at 0.12 → layer opacities written →
  at each stage boundary, §6.2's beat fires (260ms) → texture
  settles at the new pitch within ~600ms of scroll rest.
- **State matrix (v2).** *Rest:* current stage texture. *Hover /
  focus / active:* none. *Scrolled-past:* the stage behind reads at
  its own pitch when revisited — the value is positional, not
  latched. *Disabled / no-JS:* static mid-weave. *Touch:* identical;
  scrub follows touch scroll through the same loop.
- **Breakpoints (v2).** ≥1200px: five layers + damask motif.
  768–1199px: four layers (10px stage merged into its neighbours),
  motif at 70% opacity cap. <768px: three layers, no motif, stepped
  crossfades.
- **Edge cases & failure modes (v2).** *Very short page* (a single
  section): `--weave` maps across the section's own height so the
  ground still travels field→cloth, compressed. *Jump scroll to
  footer* (anchor, find-in-page): the loop's catch-up rule sets
  `--weave` directly to the positional value within one frame — the
  cloth is where the reader is, never still travelling. *Overscroll /
  rubber-banding:* value clamps 0–1; the ground never "unweaves"
  past burlap. *SVG pattern unsupported:* the ground falls back to
  the stage's flat token — flat straw is still the right colour of
  honest.
- **Accessibility spec (v2).** The stack is decorative and
  `aria-hidden`; it never carries information the copy doesn't state
  (stage names and figures are in the text, §6.2/§6.15). Text
  contrast is §2's licensed pairings at every stage and blend,
  verified in §10's audit at five sampled scroll positions.
- **Tokens consumed (v2).** `--linen`, `--straw`, `--stem`, `--loom`,
  `--weave` (written), `--ease-weave`, `--lerp-scrub` (0.12).

### 6.2 Five process stages

- **What & why.** Five pinned stage bands — harvest, retting,
  scutching, spinning, weaving — each of which advances the ground
  one step toward cloth and beats once, a 4px loom-settle, as its
  stage locks. The stages are the page's chapters and its argument:
  linen is not bought, it is *gone through*. Each band's copy
  describes the transformation its ground is simultaneously
  undergoing, so text and texture tell the same story at the same
  moment.
- **Structure.** Five `<section>` bands in fixed order, each with a
  stage dateline (stage number, name, its governing figure from the
  crop record — harvest: 2,140 kg of straw; retting: 9 days in the
  dam; scutching: 386 kg of clean fibre; spinning: one thread, 165
  to the inch at the loom; weaving: 342 metres from this crop), a
  Newsreader stage title, and the stage's copy length. Each band pins
  via `position: sticky` for 60vh while its ground step completes;
  the ground step itself is §6.1's layer crossfade, keyed to the
  band's pin progress.
- **Motion spec.** Trigger: scroll through the pins. As a band's pin
  engages, its ground crossfades 600ms `--ease-weave`; at pin
  progress 0.85 the stage *locks*: the whole band settles 4px over
  260ms `--ease-beat` — the loom beating the weft home — and the
  margin thread advances its state (§6.6). The lock is one-way per
  session: scrolling back up loosens the weave (§6.1) but does not
  un-beat a locked stage's copy block, which stays settled; the beat
  never replays.
- **States.** Approaching (ground at previous stage) → pinning
  (crossfade running) → locked (beat fired, copy settled, dateline's
  figure inked in `--flower-deep` — the stage's one blue word, §3
  law 4) → scrolled-past (band released, ground holds the new
  stage). Hover/focus: none on the band; focus entering a band
  mid-pin does not disturb the pin.
- **Content merge.** The stage's copy *is* the process the ground is
  performing: the retting band's text about water and waiting sits
  on straw that is visibly coarser than the field above it and finer
  than nothing yet. Remove the texture and the copy loses its
  evidence; remove the copy and the texture is decoration — the
  merge is the element.
- **Failure fallback.** No JS: the five bands print unpinned, in
  order, each on its own stage's static ground (the layers ship
  assigned per-band), with a printed process strip — five named
  steps with their figures — at the head of the first band. Watchdog:
  if a pin's crossfade has not completed 1200ms after the pin
  engages (loop stall, hidden tab), the ground snaps to the stage's
  settled texture and the beat is skipped, never left pending.
- **Reduced-motion variant.** No pins, no beats. The stages rest as
  the static process strip: five bands in order, grounds fixed at
  each stage's texture, the strip at top naming all five with their
  figures — the original entry's ruling, kept verbatim in spirit.
- **Performance budget & mobile variant.** Pins are sticky, not
  JS-transformed; the only animated values are layer opacities and
  one 4px translate per lock. Mobile (<768px): pins shorten to 30vh,
  the beat becomes 2px, and scutching's band merges its copy into
  retting's (four bands) — the process loses a held breath, never a
  fact: scutching's figure prints in retting's dateline as its second
  line.
- **Choreography timeline (v2).** Band top reaches 70% viewport →
  pin engages → ground crossfade begins (600ms) → pin progress 0.85
  → beat (260ms, 4px settle) + thread state advance (§6.6) +
  dateline figure inks blue → pin releases at band end → next band.
- **State matrix (v2).** *Rest:* settled stage ground, copy at rest.
  *Hover:* none. *Focus:* entering mid-pin — pin completes on its
  own timeline; a focus-triggered jump (§6.4's rule) snaps the ground
  to the stage's settled state. *Active:* n/a. *Scrolled-past:*
  locked, settled, beat spent. *Disabled / no-JS:* static strip.
  *Touch:* identical, pins driven by touch scroll through the shared
  loop.
- **Breakpoints (v2).** ≥1200px: 60vh pins, 4px beat, five bands.
  768–1199px: 45vh pins, 3px beat. <768px: 30vh pins, 2px beat, four
  bands (scutching merged, figure preserved).
- **Edge cases & failure modes (v2).** *Stage copy longer than the
  band:* the band grows; the pin distance is a minimum, never a
  cage — copy is never clipped to fit the choreography. *A page with
  only three stages* (a short product page, §7): stages may be
  omitted from the *end* of the sequence only (a page may stop at
  spinning; it may not skip retting) — the process has an order and
  the order is the content. *Browser without sticky:* bands degrade
  to sequential sections with the same crossfades keyed to viewport
  entry.
- **Accessibility spec (v2).** Stage bands are `<section>`s with
  `aria-labelledby` pointing at their stage titles; the pin never
  traps focus or scroll. The beat is visual only and never
  announced. Each stage's figure is real text in its dateline, not
  an image. Reading order in the DOM is the process order — a screen
  reader walks the field in the same sequence the eye does.
- **Tokens consumed (v2).** `--stem`, `--straw`, `--linen`, `--loom`,
  `--flower-deep`, `--ease-weave`, `--ease-beat`, `--dur-stage-fade`
  (600ms), `--dur-beat` (260ms).

### 6.3 Breeze-swayed flax

- **What & why.** In the hero, some fourteen flax stems (SVG, drawn
  from the theme's botanical plate) sway once in a passing breeze on
  load — staggered rotations of 2–4° travelling left to right over
  ~2.5s — then stand still. It belongs because the field is alive
  before it is a product: the headline grows out of an actual crop,
  and the crop's one gesture of life is spent in the first three
  seconds, not looped forever like a screensaver.
- **Structure.** An inline SVG stand of 14 stems anchored along the
  hero's lower edge, each stem a `<g>` with its own transform-origin
  at the root, heights and flower counts varied by an authored seed
  (no two adjacent stems alike; exactly 9 carry flowers — the field
  is not all bloom). The stems stand *behind* the headline layer and
  *in front of* the ground stack; their bases are planted in a
  stem-green ground band so no stem floats.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against 800ms (the breeze waits for the headline to be
  printed, §6.5, not for images — there are none). Each stem rotates
  2–4° (authored per stem, taller stems more) over 900ms
  `--ease-breeze`, staggered 110ms left to right — a wave crossing
  the stand in ~2.5s total — then returns to 0° over 700ms and rests.
  Ambient repeat: every ~25s a fainter wave (40% amplitude, stems in
  field sections only) passes; it is cancelled while the tab is
  hidden, while any stage pin is mid-beat, and after the visitor has
  scrolled past the weaving stage (the field is harvested by then;
  the harvested field does not sway — §9, failure 8).
- **States.** Rest: stems upright, still. Swaying: the wave in
  transit. Hover: none — the field is not a control; a pointer over
  the hero does not stir it (a breeze answers weather, not cursors).
  Scrolled-past: still; the ambient wave no longer reaches sections
  the visitor has left.
- **Content merge.** The stems are the brand's raw material standing
  in the hero, rooted at the headline's baseline — the name grows
  out of the crop it names. The stand's flower count and the hero's
  dateline ("sown in March, in the Long Field") are the same field
  the crop record (§6.15) later accounts for.
- **Failure fallback.** Watchdog at 3000ms: any stem not returned to
  0° is set to 0° and the wave is marked spent — a stem may never be
  left leaning. No JS: stems stand upright in the SVG as drawn; the
  field is a still plate, complete.
- **Reduced-motion variant.** No sway, ever — neither the load wave
  nor the ambient repeat. The stand prints as the still botanical
  plate. The aliveness is stated by the copy ("the field, standing")
  instead of performed.
- **Performance budget & mobile variant.** One inline SVG ≤12KB;
  rotation on 14 `<g>` elements, compositor-only. Mobile (<768px):
  8 stems, wave 1.8s, ambient repeat cut entirely — a phone's field
  sways once, on arrival, and rests.
- **Choreography timeline (v2).** t=0 fonts ready → t=+200ms the
  headline's beating begins (§6.5) → t=+600ms the wave leaves the
  leftmost stem → stems crest in sequence at 110ms intervals → last
  stem settles by t≈3200ms → field still → ambient waves at ~25s
  intervals, 40% amplitude, field sections only.
- **State matrix (v2).** *Rest:* upright. *Hover:* none. *Focus:*
  focus entering the hero does not trigger or cancel the wave; if
  the wave is running when focus lands on the headline, it completes
  — it never moves text, only stems behind it. *Active:* n/a.
  *Scrolled-past:* still, ambient cancelled for that section.
  *Disabled / no-JS:* still plate. *Touch:* identical; no
  touch-stirring.
- **Breakpoints (v2).** ≥1200px: 14 stems, full wave. 768–1199px: 11
  stems, 2–3° rotations. <768px: 8 stems, single load wave, no
  ambient.
- **Edge cases & failure modes (v2).** *Slow font load:* the 800ms
  race loser means the breeze fires anyway at t=800ms — weather does
  not wait for typography, but the stems sit behind the headline
  layer so an unprinted headline is never overlapped mid-sway.
  *Hero shorter than the stand:* stem heights scale to the hero's
  ground band; stems never rise into the headline's lines. *Repeat
  visit in session:* the load wave is spent once per session
  (`sessionStorage`); returning to the top finds a still field and
  the ambient timer only.
- **Accessibility spec (v2).** The SVG is `aria-hidden` decoration;
  the field's facts (sowing, field name) are in the dateline text.
  Sway is below vestibular concern at 2–4° and is fully removed
  under reduced motion. No information is carried by the motion.
- **Tokens consumed (v2).** `--stem`, `--flower`, `--ease-breeze`,
  `--dur-sway` (900ms), `--dur-sway-stagger` (110ms),
  `--dur-ambient-period` (~25s).

### 6.4 Loom-beam reveals

- **What & why.** Sections are uncovered by a horizontal loom-beam
  mask rising over ~700ms — the section's content revealed from its
  bottom edge upward, the weave at the mask's leading edge
  momentarily compressed, as if the beam that weaves the cloth is
  also the thing unveiling what is printed on it. Content in this
  theme is woven into view, never faded in from nowhere.
- **Structure.** Each revealable section ships complete in the DOM.
  When JS arms it, a `clip-path: inset()` mask is applied with the
  section's ground layer showing a compressed weave band (the same
  SVG texture at 60% pitch, one thread tall zone) at the mask's
  rising edge. The text layer itself is never transformed — only the
  clip opens. Sections above the fold on load are never armed; they
  are simply present.
- **Motion spec.** Trigger: the section's top crossing 78% of the
  viewport. The mask rises over 700ms `--ease-loom`; the compressed
  band travels with the edge and relaxes to the section's normal
  pitch in the final 120ms. One reveal at a time per viewport;
  sections entering together queue at 90ms offsets. A section
  scrolled past quickly (fling) is revealed instantly by the
  catch-up rule — the beam does not chase a reader who has already
  arrived.
- **States.** Unarmed (default, no-JS, above-fold): fully visible.
  Armed: clipped to its bottom 8% (a selvedge line of the section
  shows — never a blank). Revealing: mask rising. Revealed: clip
  removed entirely (not left at inset 0 — removed, so no clipping
  context survives). Scrolled-past unrevealed (armed but jumped):
  revealed instantly by anchor/focus/watchdog.
- **Content merge.** The reveal is performed by the page's own
  instrument: the beam is part of the loom that §6.2's stages have
  been assembling, and the compressed weave at its edge is the
  section's own ground under pressure. The section is not decorated
  by the reveal; it is manufactured by it, in view.
- **Failure fallback.** Watchdog at 1600ms after arming: if the
  reveal has not completed, the clip is removed and the section
  stands whole. A second, global 2500ms sweep after load disarms any
  section still clipped. No JS: nothing is ever armed; the page is
  complete at first paint — the original entry's safety rule, kept.
- **Reduced-motion variant.** No mask, no rise. Sections are present;
  the only acknowledgement of the beam is the selvedge rule that
  joins sections (§4), printed statically.
- **Performance budget & mobile variant.** Clip-path animation on
  the section wrapper only; the compressed band is a background
  layer. ≤0.3ms/frame during a reveal. Mobile (<768px): the rise is
  500ms and the compressed band is cut — the mask simply opens; the
  beam is implied by the selvedge, not drawn.
- **Choreography timeline (v2).** Section top crosses 78% viewport →
  t=0 mask begins rising (700ms `--ease-loom`) → t=580ms compressed
  band begins relaxing → t=700ms clip removed → section's own
  counters (§6.15) or draws (§6.7) may start, never before t=700ms.
- **State matrix (v2).** *Rest:* revealed, whole. *Hover:* none.
  *Focus:* focus landing inside an armed section reveals it
  instantly before focus paints — a keyboard visitor never tabs
  into a clipped section. *Active:* n/a. *Scrolled-past:* revealed
  (catch-up). *Disabled / no-JS:* never armed. *Touch:* identical;
  fling-scroll triggers catch-up, not a queue of rises.
- **Breakpoints (v2).** ≥1200px: 700ms rise with compressed band.
  768–1199px: 650ms, band at 70% pitch. <768px: 500ms, no band.
- **Edge cases & failure modes (v2).** *Section taller than the
  viewport:* the mask rises over the section's first viewport-height
  only; the remainder was never clipped (arming clips only the first
  100vh of a long section). *Print:* stylesheet removes all clips —
  paper gets the whole bolt. *Back-button return mid-reveal:* the
  reveal state is not persisted; a returned page arms fresh and the
  catch-up rule settles anything already in view instantly.
- **Accessibility spec (v2).** Content is in the accessibility tree
  in full from first paint — the clip is visual only, `aria-hidden`
  is never applied to a clipped section. Focus order is DOM order,
  unaffected by reveal state. The 8% armed state shows a selvedge
  line, never a blank region that could read as a loading failure.
- **Tokens consumed (v2).** `--ease-loom`, `--dur-reveal` (700ms),
  `--weave` (read), `--loom`.

### 6.5 The tightening headline

- **What & why.** The hero headline prints onto the loose weave:
  its letters begin at +0.06em tracking with the burlap's fibres
  showing through the glyphs, and over ~1.2s the tracking is beaten
  down to its rest value (−0.01em) as the fibres fade — type being
  woven and beaten into place, exactly what the loom does to cloth.
  The brand name is the first thing woven on the page.
- **Structure.** A real `<h1>` in Newsreader carrying the full
  headline text from first paint, over the hero's ground layer. When
  JS arms it (only when fonts are ready — see fallback), a duplicate
  fibre-textured layer (the headline's own text clipped through the
  burlap SVG at 14px pitch, `aria-hidden`) sits over the base at the
  wide tracking; the base sits beneath at full contrast throughout.
  The animation tightens `letter-spacing` on both layers together
  and fades the fibre layer out.
- **Motion spec.** Trigger: load, after `document.fonts.ready`
  (raced at 800ms). Tracking +0.06em → −0.01em over 1200ms
  `--ease-beat` — the beat's overshoot lives in the easing's settle,
  felt as the letters seating themselves. The fibre layer's opacity
  falls 0.85 → 0 across the same 1200ms, weighted to the final third
  (fibres vanish as the beating completes, not before). At
  completion the fibre layer is removed from the DOM.
- **States.** Printed (default, no-JS, fonts-late): base headline at
  rest tracking, full contrast — always the fallback state. Arming →
  beating (tracking travelling, fibres fading) → beaten (rest;
  fibre layer gone). Hover/focus: none; focus landing mid-beat
  completes the beat instantly. Scrolled-past mid-beat: the beat
  completes on its own timeline.
- **Content merge.** The headline is the page's `<h1>` and subject;
  its making *is* the hero's first event, synchronised with the
  field's breeze (§6.3 fires at t=+600ms into the beat). The
  standfirst beneath waits for the beat's end before its own
  loom-beam reveal (§6.12) — the name is woven before anything is
  said under it.
- **Failure fallback.** Watchdog at 1400ms: tracking snaps to rest,
  fibre layer removed. If fonts lose the 800ms race, the headline
  ships printed and is never armed — a fibre layer aligned to the
  wrong face would misprint the name, and this theme does not
  misprint (§9, failure 2). No JS: printed, complete.
- **Reduced-motion variant.** No beating. The headline stands at rest
  tracking with the fibres rendered statically at 25% opacity inside
  the glyphs — the fact (this type sits in cloth) survives as a
  texture; the performance rests.
- **Performance budget & mobile variant.** One duplicate text layer,
  animating `letter-spacing` and opacity only; the fibre texture is
  the ground's own SVG, reused. Mobile (<768px): the beat shortens
  to 900ms and starts at +0.04em — a smaller loom, a lighter beat.
- **Choreography timeline (v2).** t=0 fonts ready → fibre layer
  armed → t=0–1200ms tracking beats down, fibres fading from
  t=700ms → t=+600ms the breeze leaves the leftmost stem (§6.3) →
  t=1200ms fibre layer removed → t=+150ms standfirst reveal begins
  (§6.12).
- **State matrix (v2).** *Rest:* beaten, rest tracking. *Hover:*
  none. *Focus:* mid-beat focus completes instantly.
  *Active:* n/a. *Scrolled-past:* beaten. *Disabled / no-JS:*
  printed at first paint. *Touch:* identical; first touch anywhere
  in the hero completes a running beat.
- **Breakpoints (v2).** ≥1200px: 64px, 1200ms beat, +0.06em start.
  768–1199px: 48px, 1050ms, +0.05em. <768px: 36px, 900ms, +0.04em,
  fibre layer at 60% starting opacity.
- **Edge cases & failure modes (v2).** *Headline longer than two
  lines:* the beat applies per line with a 60ms line stagger, cap
  still 1400ms total; a headline over 9 words is refused at build
  (§12 — a headline is a name, not a sentence). *CMS-edited
  headline:* the fibre layer is generated from the live text at arm
  time, so edits can never misalign it; if generation fails, the
  headline ships printed. *Variable font axis shift:* optical sizing
  is locked during the beat to keep the fibre clip registered.
- **Accessibility spec (v2).** The `<h1>` text is complete and at
  full contrast in the base layer at all times — the readable layer
  never depends on the animation. The fibre layer is `aria-hidden`,
  `pointer-events: none`. Contrast during the beat is the base
  layer's: `--loom` on the hero ground, 8.15:1 once the hero ground
  is read as finished cloth at its licensed pairing (§2).
- **Tokens consumed (v2).** `--loom`, `--linen`, `--ease-beat`,
  `--dur-beat-headline` (1200ms), `--tracking-loose` (+0.06em),
  `--tracking-rest` (−0.01em).

### 6.6 Margin thread progress

- **What & why.** A single thread runs the page's margin from hero
  to footer and undergoes the process itself: in the field it is
  hair-thin and fuzzy — loose fibre; through retting and scutching
  it cleans; by spinning it is a smooth, even yarn; at the footer it
  is woven into a dense damask stripe. It is the progress indicator,
  and it is honest in a way bars are not: it shows not how much page
  remains but how much *making* has happened, in the material the
  page is about.
- **Structure.** An SVG in the 148px margin rail (§4): one vertical
  path whose drawn length is scrubbed to scroll, rendered in three
  stacked treatments keyed to `--weave` — a fuzzy fibre (the path
  stroked with a turbulence-displaced duplicate at low opacity), a
  smooth yarn (single 2px stroke in `--stem-deep`), and, for the
  final fifth, a woven stripe (the path replaced by a 14px damask
  band segment, woven diamond motif). Five stage labels sit beside
  the thread at their bands' heights, 12px small caps, inked from
  `--straw-deep` to `--stem-deep` as their stage locks (§6.2).
- **Motion spec.** Trigger: scroll scrub, global, shared loop lerp
  0.12. The thread's drawn length is the scroll's own proportion;
  its *treatment* crossfades at the stage fifths (fuzzy → clean at
  `--weave` 0.4, clean → smooth at 0.6, smooth → stripe at 0.85) over
  400ms `--ease-weave`. Scrolling back un-draws and un-spins the
  thread — the indicator is positional, holding no false memory.
- **States.** Rest: thread drawn to the current position, treatment
  of the current stage. Scrolled-past / back: exactly positional.
  Hover: hovering the rail widens the thread's hit area and shows
  the current stage's name beside it (the one tooltip-like behaviour
  the theme licenses, rendered as a woven label, §11). Focus: the
  thread is not focusable; its information is duplicated in the
  stage datelines.
- **Content merge.** The thread is one fibre of the very crop the
  page processes — §6.15's record accounts for it in jest and in
  earnest: the footer's colophon (§6.17) notes the thread among the
  crop's yield. Progress, crop and cloth are one object seen three
  ways.
- **Failure fallback.** No JS: the rail prints the static process
  strip — five stage labels joined by a printed line, the full
  journey visible at once (the same strip §6.2's fallback uses).
  Watchdog: if the loop stalls, the thread freezes at its last true
  position; it can never display a position the reader is not at.
- **Reduced-motion variant.** The thread prints fully drawn in its
  five treatments along the rail, static — a woven contents-marker
  rather than a live indicator; stage labels all inked. Position is
  then carried by the selvedge navigation (§6.11) alone.
- **Performance budget & mobile variant.** One SVG path + opacity
  crossfades; ≤0.2ms/frame. Mobile (<768px): the rail is gone; the
  thread becomes a 3px selvedge fixed at the viewport's top edge,
  its treatment shown by its texture segment under the current
  scroll position — fuzzy, smooth, or damask-striped — with no
  labels (labels live in the stage datelines, which remain).
- **Choreography timeline (v2).** Continuous: scroll Δ → drawn
  length lerps (0.12) → at each stage lock (§6.2's beat) the
  corresponding label inks (200ms) → at `--weave` 0.85 the stripe
  segment begins weaving in (400ms) → at page end the stripe
  completes exactly at the footer's final line.
- **State matrix (v2).** *Rest:* positional, current treatment.
  *Hover:* stage-name label shows beside the rail. *Focus:* n/a
  (not focusable). *Active:* n/a. *Scrolled-past:* positional —
  behind the reader the thread reads at the reader's furthest stage
  only when the reader is there; it holds no maximum. *Disabled /
  no-JS:* static strip. *Touch:* identical; the top selvedge variant
  scrubs with touch scroll.
- **Breakpoints (v2).** ≥1200px: 148px rail, labels, stripe 14px.
  768–1199px: 64px rail, thread only, labels in datelines. <768px:
  3px top selvedge, no rail.
- **Edge cases & failure modes (v2).** *Page shorter than the
  journey* (§7's short pages): the thread compresses — treatments
  still sequence in order across whatever length exists; a page may
  shorten the thread but never reorder it. *Print:* the rail prints
  as the static strip. *Zoom 200%:* the rail yields — below an
  effective 768px the top-selvedge variant takes over rather than
  crushing the measure.
- **Accessibility spec (v2).** `aria-hidden` — progress here is
  ambient, and its information (which stage, how far) is carried by
  the stage datelines and headings in the text. The theme refuses a
  `role="progressbar"` for the thread: a woven thread is not a form
  control, and labelling it one would announce percentages the theme
  forbids (§9, failure 3).
- **Tokens consumed (v2).** `--stem-deep`, `--straw-deep`, `--linen`,
  `--loom`, `--weave` (read), `--ease-weave`, `--lerp-scrub` (0.12).

### 6.7 Flax stem draw

- **What & why.** In the field section, a botanical SVG of a flax
  stem — roots, stem, leaves, the five-petalled flower — strokes
  itself in over ~1.8s in growth order, each part labelled as it
  completes. It is the theme's one line-draw, rationed to a single
  diagram per page, and it belongs because the plant is the page's
  first fact: before the crop is a crop it is a stem, and the
  diagram grows at something like the plant's own patience.
- **Structure.** One inline SVG (≤10KB), paths authored from the
  botanical plate in growth sequence: root hairs → stem → leaf
  pairs (4) → flower stem → five petals → seed boll. Labels are real
  HTML text beside the diagram (never SVG text), each label's leader
  line part of the draw. The completed diagram ships as the DOM
  default; drawing is a mask the JS arms.
- **Motion spec.** Trigger: the diagram's centre crossing 60% of the
  viewport, once per session. Paths draw via `stroke-dashoffset`
  over a total 1800ms `--ease-loom`, allocated by path length (the
  stem takes the longest share, ~600ms; petals 120ms each); each
  label fades in 200ms as its part completes. The draw never
  restarts on re-entry.
- **States.** Drawn (default/rest). Arming → drawing (parts in
  growth order) → drawn. Hover on a labelled part: its label inks
  from `--straw-deep` to `--stem-deep` and the part's stroke warms
  10% — a finger resting on the plate. Focus: labels are not
  focusable; the diagram is a figure with a caption, not a control.
- **Content merge.** The diagram is the field section's evidence:
  the copy beside it names the parts the draw is labelling (the boll
  the copy calls the harvest). It is cataloguing the same stem that
  stands, drawn at hero scale, in §6.3's stand.
- **Failure fallback.** Watchdog at 2200ms: any path still masked
  snaps to drawn. No JS: the diagram stands complete with all labels
  printed — the plate as a book would print it.
- **Reduced-motion variant.** No draw. The plate prints complete;
  labels all present. Growth is described by the caption ("drawn in
  the order it grows") rather than performed.
- **Performance budget & mobile variant.** Dash-offset animation on
  ≤20 paths, one-shot. Mobile (<768px): the draw compresses to
  1200ms and leaf-pair labels reduce to two (stem, flower) — the
  plate shrinks, its facts don't.
- **Choreography timeline (v2).** Centre crosses 60% → t=0 roots
  (180ms) → stem (600ms) → leaf pairs (4 × 110ms, alternating) →
  flower stem (150ms) → petals (5 × 120ms) → boll (130ms) → labels
  trailing their parts by 0ms, 200ms fades → t≈1800ms plate complete
  → the field section's counter (§6.15) may start.
- **State matrix (v2).** *Rest:* drawn. *Hover:* label/part warming
  as above. *Focus:* n/a. *Active:* n/a. *Scrolled-past:* drawn;
  jumping straight past it (anchor) completes it instantly.
  *Disabled / no-JS:* printed plate. *Touch:* identical; hover
  warming replaced by the same on first tap of a label.
- **Breakpoints (v2).** ≥1200px: full plate, 5 labels. 768–1199px:
  full plate, labels at 12px. <768px: 1200ms draw, 2 labels, plate
  at full measure width.
- **Edge cases & failure modes (v2).** *Diagram reused on a second
  page type* (§7's about page): the once-per-session rule is per
  page, not per site — a new page may draw its own plate, but two
  plates on one page is a build error (§10). *Dash math on very
  long paths:* lengths are measured at build time and baked as data
  attributes; a path whose measured length disagrees with its bake
  by >5% ships drawn (the audit prefers a still plate to a wrong
  draw).
- **Accessibility spec (v2).** The figure carries a real `<figcaption>`
  summarising the plant's parts in order; the SVG is `role="img"`
  with an aria-label naming it a botanical plate of flax. The draw
  is never announced. Labels are HTML, readable at every state —
  they fade in only when JS arms them; unarmed, they are simply
  present.
- **Tokens consumed (v2).** `--stem`, `--stem-deep`, `--flower`,
  `--straw-deep`, `--ease-loom`, `--dur-draw` (1800ms).

### 6.8 Stage-matched image frames

- **What & why.** Photographs sit in woven frames whose weave
  fineness matches the reader's current process stage — burlap-framed
  in the field, straw-framed at retting, damask-framed near the
  footer. Even the photography is dressed in the cloth of the
  moment, woven by the same scroll that weaves the page.
- **Structure.** Each framed image is a `<figure>` whose frame is a
  border built from the ground stack's own SVG textures (§6.1),
  reading the global `--weave` — the frame is not styled per image
  but inherits the page's current pitch, with its corners mitred as
  folded cloth (a 45° thread turn, drawn, not a radius). The image
  itself scales in-frame from 1.06 to 1 on entry. Captions set in
  13px `--straw-deep` on the stage's ground, outside the frame.
- **Motion spec.** Trigger: scroll state for the frame's fineness
  (continuous, from `--weave`, no separate animation); entry:
  the image scales 1.06 → 1 over 700ms `--ease-weave` as the figure
  crosses 70% viewport, inside its frame — the frame never scales.
  A frame's pitch updates only at stage boundaries (stepped, 400ms
  crossfade) rather than continuously, so a photograph is never seen
  to crawl.
- **States.** Rest: image settled, frame at the current stage's
  pitch. Hover: the palm band (§6.9) may cross cloth cards, never
  photographs — a photograph is evidence, not cloth for sale.
  Scrolled-past: frame holds the pitch of wherever the reader is
  now, not where the image lives — the frame belongs to the reader's
  stage, and §1's law audits exactly this.
- **Content merge.** The frame is the page's cloth wrapped around
  the evidence: a photograph of the dam, taken during retting,
  framed in the straw weave the reader has just retted. Frame and
  ground are one material at one fineness — the audit (§10) samples
  a frame's pitch against `--weave` at three scroll positions.
- **Failure fallback.** No JS: frames print at the pitch of the
  stage band they sit in (assigned per-band in markup) — still
  stage-matched, statically. Images carry real `alt` and are never
  masked; a failed image leaves its frame holding the caption and a
  woven placeholder field in the stage's texture (never a broken
  glyph).
- **Reduced-motion variant.** No scale-in; images rest in-frame.
  Frames still step at stage boundaries (a state change, not a
  motion) — or, on the strictest reading honoured here, print at
  their band's pitch statically as in the no-JS case.
- **Performance budget & mobile variant.** Frames reuse §6.1's
  pattern assets — no extra downloads. Scale is transform-only.
  Mobile (<768px): frames simplify to a selvedge edge on two sides
  (top, left) at the band's pitch; the mitred corners are cut.
- **Choreography timeline (v2).** Figure crosses 70% → image scale
  700ms → settled → at each subsequent stage boundary, frame
  crossfade 400ms to the new pitch, synchronised with §6.1's layer
  crossfade so frame and ground change in the same beat.
- **State matrix (v2).** *Rest:* settled, current pitch. *Hover:*
  none on the photograph. *Focus:* focus on the figure (where it is
  a link, §7 detail pages) shows the §11 focus treatment on the
  frame's outer selvedge, pitch unchanged. *Active:* n/a.
  *Scrolled-past:* pitch follows the reader. *Disabled / no-JS:*
  band pitch, static. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full woven frame, mitred corners.
  768–1199px: frame at 70% border width. <768px: two-sided selvedge
  frame.
- **Edge cases & failure modes (v2).** *Image aspect ratios vary:*
  the frame is built from the figure's box, not the image's — any
  aspect is framed without distortion; the scale-in crops nothing
  (the image is whole at 1.06 inside an overflow-hidden frame and
  settles to exactly whole). *Two stages visible at once* (a tall
  viewport spanning a boundary): the frame takes the pitch of the
  stage occupying the larger share of the viewport — one frame, one
  pitch, never a gradient.
- **Accessibility spec (v2).** Frames are decorative (`aria-hidden`
  borders); the photograph's `alt` and caption carry its content.
  The scale-in never delays the image's availability to assistive
  technology. Contrast: captions sit on the stage ground at §2's
  licensed pairings, never on the frame.
- **Tokens consumed (v2).** `--weave` (read), `--straw-deep`,
  `--ease-weave`, `--dur-frame-step` (400ms), `--dur-img-settle`
  (700ms).

### 6.9 Palm-over-linen hover

- **What & why.** Hovering a product card runs a soft, warm light
  band across its cloth surface, following the pointer's vertical
  position — a palm smoothing over linen. Inspecting bedding *is*
  touching it; the hand-feel of linen is the product's whole
  argument, and this is that argument made interactive without a
  single gimmick control.
- **Structure.** Each cloth card (§6.13) carries a light layer: a
  120px-tall radial band in `--linen` warmed 6% toward `--straw`,
  clipped to the card, `pointer-events: none`, its centre lerped to
  the pointer's y within the card by the shared loop at 0.18. The
  band brightens the card's own weave texture (the card's ground is
  §6.1's texture at the card's stage pitch) rather than painting
  over it — light on cloth, not a gloss sticker.
- **Motion spec.** Trigger: pointerenter / pointermove on a card.
  The band fades in over 240ms `--ease-press` and follows with lerp
  0.18 (the hand is quicker than the loom); on leave it settles —
  drifting 12px toward the card's centre while fading over 300ms,
  the palm lifting away. The band never exceeds 8% luminance lift:
  a palm shades and warms, it does not spotlight (§9, failure 5).
- **States.** Rest: no band. Hover: band present, following.
  Focus: keyboard focus on the card (or its link) brings the band
  to the card's vertical centre, steady — focus gets the same
  inspection light, aimed at the middle because there is no hand.
  Active (press): the band narrows to 80px and deepens 2% — pressure
  — for the press's duration, pairing with §6.10's crease.
  Scrolled-past: n/a. Disabled card (out of stock, §6.13): no band;
  the cloth is not for touching.
- **Content merge.** The band's whole meaning is the card's surface:
  it reveals the weave the card is selling, following the visitor's
  own hand position. On a plain div it would be a spotlight effect;
  on woven cloth, at 8%, it is a palm.
- **Failure fallback.** No JS / no fine pointer: no band; cards
  carry a static 3% warm gradient printed in their cloth so the
  surface still reads as lit cloth, not flat colour. If the loop
  stalls mid-hover, the band freezes where it is and fades on the
  next pointerleave — it can never stick as a bright patch (§10
  checks the 8% cap by screenshot).
- **Reduced-motion variant.** The band does not travel. On hover or
  focus it appears at the card's centre at 5% lift, instantly, and
  disappears instantly — the information (this surface is cloth,
  lit warmly) without the gesture.
- **Performance budget & mobile variant.** One gradient layer per
  hovered card only (created on enter, removed on leave); transform
  + opacity. Touch: no hover band — a tap is a press (§6.10), and
  the press's narrowing band fires centred for 300ms as the tap's
  acknowledgement.
- **Choreography timeline (v2).** Pointerenter → t=0 band fades in
  (240ms) at the pointer's y → move: band lerps 0.18 per frame →
  pointerdown: narrow to 80px, deepen 2% → pointerup: restore →
  pointerleave: drift 12px to centre + fade 300ms → layer removed.
- **State matrix (v2).** *Rest:* absent. *Hover:* following at ≤8%.
  *Focus:* centred, steady, 6%. *Active:* narrowed, deepened.
  *Scrolled-past:* n/a. *Disabled:* absent. *Touch:* tap-centred
  300ms acknowledgement only.
- **Breakpoints (v2).** ≥1200px: 120px band, full behaviour.
  768–1199px: 100px band. <768px: touch rules — no travelling band;
  the tap acknowledgement at 90px.
- **Edge cases & failure modes (v2).** *Fast pointer crossing many
  cards:* one band exists at a time; leaving a card removes its
  layer before the next is created — no card keeps a ghost palm.
  *Pointer at the card's very edge:* the band clamps inside the
  card, never spilling onto the page's ground (a palm does not hover
  off the cloth). *Forced-colors mode:* the band is removed
  entirely; cards rely on their borders and the system's highlight.
- **Accessibility spec (v2).** Purely decorative layer,
  `aria-hidden`, never the sole carrier of any state (selection is
  §6.10's crease + the pile count, both non-visual too). Focus
  visibility is §11's woven outline, not the band — the band is a
  courtesy light, and at 6% it is never mistaken for the focus ring.
- **Tokens consumed (v2).** `--linen`, `--straw`, `--ease-press`,
  `--lerp-palm` (0.18), `--dur-palm-in` (240ms), `--dur-palm-out`
  (300ms).

### 6.10 Pressed-crease click

- **What & why.** Clicking a product card presses a crease into it:
  a fine fold line — a 1px highlight/shadow pair — fades in across
  the card over 300ms and *stays* for the session. Selection in this
  theme is folding laundry: chosen products are folded into a pile
  the visitor is building (§6.13), and the crease is the fold mark
  that proves it. A card clicked again unfolds — the crease fades
  out over 300ms and the card leaves the pile.
- **Structure.** The crease is an absolutely-positioned 1px pair
  (highlight in `--linen` at 70%, shadow in `--loom` at 18%) across
  the card at 38% of its height — a fold is never at the middle;
  laundry folds in thirds. Its angle is authored per card index
  (−0.4° to +0.4°, deterministic) because no two hand folds match.
  State lives in the card's `aria-pressed` and a session pile
  object; the pile itself renders in §6.13.
- **Motion spec.** Trigger: click / Enter / Space on the card's
  button. Crease fades in 300ms `--ease-press`, accompanied by the
  card settling 2px (the press) over the same 300ms and §6.9's band
  narrowing. Unfold: crease fades 300ms, card rises back. No bounce:
  cloth pressed is cloth held.
- **States.** Unfolded (rest): no crease, card flat. Pressing:
  300ms transit. Folded: crease present, card 2px settled, the
  card's corner-lift (§6.13) henceforth lifts the *creased* corner —
  the fold is part of the card now. Disabled card: no press, no
  crease; its cloth is spoken for.
- **Content merge.** The crease is on the product's own cloth,
  marking the visitor's own act of choosing — it is the selection
  state, not a decoration near it. The pile (§6.13) counts creased
  cards from the DOM, so the mark, the state and the count are one
  fact printed three ways.
- **Failure fallback.** No JS: cards are ordinary links to their
  product pages (the pile is an enhancement, never a gate) — the
  original entry's readability rule applied to commerce. If the
  pile's storage fails, creases still render for the session from
  the in-memory object; nothing about the card depends on
  persistence.
- **Reduced-motion variant.** The crease appears instantly (no fade,
  no 2px settle) and disappears instantly. The fold as a *state* is
  fully preserved; only its pressing is not performed.
- **Performance budget & mobile variant.** Two 1px divs and a
  transform per card; negligible. Mobile (<768px): the crease sits
  at 33% height and the settle is 1px — a smaller fold for a smaller
  cloth.
- **Choreography timeline (v2).** Click → t=0 press begins (card
  −2px, band narrows, §6.9) → t=120ms crease pair begins fading in
  → t=300ms crease at full, card settled, pile count updates (§6.13,
  200ms ink fade) → the card's corner is now its creased corner for
  §6.13's lift.
- **State matrix (v2).** *Rest:* flat, uncreased. *Hover:* palm band
  (§6.9) only. *Focus:* woven outline (§11); Enter/Space presses
  identically to click. *Active:* the press transit itself.
  *Scrolled-past:* creases persist — a folded card stays folded
  wherever the reader wanders. *Disabled:* no press. *Touch:* tap
  presses; the 300ms band acknowledgement (§6.9) stands in for the
  narrowing.
- **Breakpoints (v2).** ≥1200px: crease at 38%, settle 2px.
  768–1199px: same, settle 2px. <768px: crease at 33%, settle 1px.
- **Edge cases & failure modes (v2).** *Rapid double-click:* the
  press toggles once per completed 300ms transit; clicks inside a
  transit are queued to its end, never stacked — a card cannot be
  half-folded. *Pile limits:* none imposed — a visitor may fold the
  whole shop; the pile (§6.13) wraps and counts honestly at any
  size. *Card removed from the DOM by filtering (§7 listing):* its
  crease state is held in the pile object and re-applied if the card
  returns; the count never disagrees with the visible creases after
  a filter settles (§10's three-printings audit covers this).
- **Accessibility spec (v2).** The card's control is a real
  `<button aria-pressed>` (or a link styled as the card with the
  press state on an inner button — build chooses per §11, the state
  is always programmatic, never visual-only). The pile count is a
  polite live region ("Three cloths folded"). The crease itself is
  `aria-hidden`; its contrast is deliberately low — it is a fold,
  not text.
- **Tokens consumed (v2).** `--linen`, `--loom`, `--ease-press`,
  `--dur-crease` (300ms).

### 6.11 Selvedge navigation

- **What & why.** The site navigation is the cloth's selvedge — the
  finished edge that keeps the bolt from fraying. It runs as a
  header band woven at the *current* stage's pitch (reading
  `--weave` like the frames, §6.8), its links separated by woven
  ticks, the current page marked by a double-density stitch segment
  under its link. A nav that is the cloth's own edge can never look
  pasted on.
- **Structure.** A `<header>` band, ground = the stage texture at
  the reader's current pitch over `--linen`; wordmark left in
  Newsreader; links as text (no pills, no boxes — cloth has no
  pills); the current link underlined by a 6px double-density woven
  segment that slides between links on navigation (§6.16 handles the
  page change; the stitch settles after). A secondary line carries
  the crop line: "The Long Field · sown March · this year's cloth" —
  the nav states whose cloth this is.
- **Motion spec.** Trigger: page load (the stitch is already under
  the current link — it never animates in on load) and stage
  boundaries (the band's pitch steps with §6.1's crossfade, 400ms).
  On in-site navigation the stitch slides 350ms `--ease-loom` to the
  new link as the cloth-lift (§6.16) completes. Header compresses on
  scroll: past 140px the band's padding tightens 20px → 12px over
  300ms and the crop line retires — the selvedge narrows, it does
  not vanish.
- **States.** Rest: full band. Scrolled: compressed band, stitch
  intact. Hover on a link: its woven tick inks `--stem-deep` (200ms)
  — never a background fill. Focus: §11's woven outline. Current:
  stitched. Disabled: n/a.
- **Content merge.** The nav's ground is woven by the same scroll as
  everything else; at the field it is burlap-edged, at the footer a
  fine edge — the wayfinding wears the journey. The crop line ties
  the chrome to the content's own record (§6.15).
- **Failure fallback.** No JS: the band prints at mid-pitch, stitch
  under the current link as static markup, crop line present,
  compression absent. Nothing about navigation depends on the loop.
- **Reduced-motion variant.** No stitch slide (it is simply under
  the current link), no compression animation (the band is at its
  compressed height from the first scroll position past 140px,
  stepped not animated). Pitch steps remain — they are state, not
  motion.
- **Performance budget & mobile variant.** The band reuses §6.1's
  textures. Mobile (<768px): the band holds wordmark + two primary
  links + a "The cloth" disclosure that opens the full list as a
  folded panel (links stacked as folded lengths, §11); the stitch
  marks the current link there too.
- **Choreography timeline (v2).** Load: band present, stitch placed
  → scroll past 140px: compression 300ms → stage boundaries: pitch
  step with §6.1 (400ms) → navigation: cloth-lift (§6.16) → stitch
  slide 350ms as the new page settles.
- **State matrix (v2).** *Rest:* full band. *Hover:* tick inks.
  *Focus:* woven outline. *Active:* link press — the tick deepens
  for 120ms. *Scrolled-past:* compressed. *Disabled:* n/a. *Touch:*
  identical; disclosure panel opens on tap with ≥48px targets.
- **Breakpoints (v2).** ≥1200px: full band, crop line, 148px rail
  alignment with §6.6. 768–1199px: crop line cut, links at 15px.
  <768px: disclosure variant.
- **Edge cases & failure modes (v2).** *Many links:* beyond six, the
  rest fold into the disclosure at every width — a selvedge is an
  edge, not a sitemap. *Long wordmark:* it wraps to two lines and
  the band grows; the stitch geometry is measured from the live
  link, never assumed. *Sticky failure:* the band falls back to
  static at the top; nothing else references its position.
- **Accessibility spec (v2).** A real `<nav>` with `aria-current` on
  the stitched link (the stitch is decoration; the state is
  programmatic). Focus order is DOM order. Link text contrast:
  `--loom` on the band's ground, 8.15:1 at the finished pitch and
  6.03:1 minimum on the coarsest straw step — checked at both ends
  (§10).
- **Tokens consumed (v2).** `--linen`, `--loom`, `--stem-deep`,
  `--weave` (read), `--ease-loom`, `--dur-stitch` (350ms).

### 6.12 First-field hero composition

- **What & why.** The hero is the field before anything is done to
  it: the flax stand (§6.3) rooted along its lower edge, the
  headline beating into the loose weave (§6.5), a dateline that is a
  sowing record — "Sown in March, in the Long Field · the blue is
  the flower, the green is the stem" — and one action line pointing
  down the bolt: "Walk the making ↓". It composes the theme's whole
  cast in one screen and promises nothing the scroll won't perform.
- **Structure.** A 100vh (min 620px) section on the burlap ground
  (14px pitch, §6.1's first layer over a `--stem`-washed field
  ground). Order: dateline (13px, `--straw-deep` — on the field
  ground the licensed pairing is loom-on-straw at the band's tint,
  §2 audit covers the hero ground specifically), the `<h1>` (§6.5),
  the standfirst (20px, one sentence of process, italic — the
  grower's voice, §3 law 3), the action line, and the stand of stems
  along the bottom. The margin thread (§6.6) is born at the
  headline's baseline, fuzzy.
- **Motion spec.** Load sequence only: dateline present at first
  paint → headline beat 1200ms (§6.5) → breeze at beat +600ms (§6.3)
  → standfirst revealed by a loom-beam rise (§6.4) at beat end →
  action line's arrow settles 4px `--ease-beat` at +150ms. Nothing
  else moves; the hero then holds still for the ambient breeze
  (§6.3).
- **States.** Rest: the composed field. Scrolled-past: the hero's
  stems parallax at 0.92× against the sections below for its final
  viewport of travel, then it is gone — the field does not follow
  the reader into the mill. Hover/focus: only the action line is
  interactive (its arrow deepens 2px on hover, 200ms).
- **Content merge.** Every hero element is a §6 element in its first
  state — the hero is not a separate design but the theme's
  instruments assembled at their starting positions: weave loosest,
  thread fuzziest, headline unbeaten, crop unharvested.
- **Failure fallback.** No JS: the hero prints composed — headline
  beaten (printed), stems standing, standfirst present, thread as
  the static strip (§6.6). The 2500ms global sweep (§6.4) guarantees
  no armed hero state can outlive its welcome.
- **Reduced-motion variant.** The composed still: headline printed
  with static fibres (§6.5), stems still, standfirst present, no
  arrow settle. The field at rest is the hero's honest portrait.
- **Performance budget & mobile variant.** The hero's assets are the
  shared SVG textures + the stem stand (≤30KB total). Mobile
  (<768px): hero 92vh, stems 8 (§6.3), standfirst 18px, the thread
  born as the top selvedge (§6.6).
- **Choreography timeline (v2).** t=0 first paint (dateline,
  printed headline base) → fonts ready: beat begins (1200ms) →
  t=+600ms breeze wave → t=1200ms standfirst rise (700ms, §6.4) →
  t=+150ms arrow settle → hero at rest; ambient breeze only.
- **State matrix (v2).** *Rest:* composed. *Hover:* action arrow
  only. *Focus:* focus on the action line shows §11's outline; if
  the beat is running, focus completes it (§6.5's rule).
  *Active:* the action line's press scrolls one stage (§6.2's first
  band) — it is an anchor, behaving like one. *Scrolled-past:*
  parallax exit, then absent. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 100vh, 64px headline. 768–1199px:
  92vh, 48px. <768px: 92vh min 540px, 36px, stems 8, dateline wraps
  to two lines above the headline.
- **Edge cases & failure modes (v2).** *Short landscape screens:*
  the min-height yields — the hero may exceed 100vh rather than
  crop the stand; a decapitated field is worse than a tall one.
  *Headline at maximum length (§6.5's 9-word cap):* the stand drops
  to 10 stems so type and crop never compete for the same line.
- **Accessibility spec (v2).** The hero's reading order is dateline →
  headline → standfirst → action — the DOM order, unmanipulated.
  The stems are `aria-hidden` (§6.3). The action line is a real
  anchor to the first stage band with a descriptive label ("Begin:
  the harvest").
- **Tokens consumed (v2).** `--stem`, `--straw`, `--straw-deep`,
  `--loom`, `--ease-beat`, `--weave` (read).

### 6.13 Cloth cards & the folded pile

- **What & why.** Products are cloths, presented as folded lengths:
  each card's ground is the weave at its stage pitch, its top edge a
  folded hem (a double-density band), its name and thread count set
  as a woven label. Cards lift like folded cloth raised by one
  corner — max 3°, the corner chosen being the card's creased corner
  once folded (§6.10). Chosen cloths gather in the folded pile: a
  fixed foot tray that stacks the folded cards' labels in the order
  folded, counting them aloud. The shop's whole metaphor is the
  laundry basket, kept dignified.
- **Structure.** Cards in a 3-across grid (cloth sections, §4): each
  a `<article>` with hem band, woven label (name, count figure from
  the record — e.g. "165 threads", weight, price), a stage-matched
  framed swatch image (§6.8), and the press control (§6.10). The
  pile is a `<aside>` foot tray, hidden until the first fold, listing
  folded labels with an unfold control each, a total (sum of the
  folded cloths' prices, computed from the DOM), and the way onward
  to §6.14's form.
- **Motion spec.** Card entry: loom-beam reveal (§6.4). Corner-lift
  on hover: rotate up to 3° about the lifted corner over 350ms
  `--ease-press`, shadow deepening as a folded length's would — the
  lift is scrubbed to pointer position (corner nearest the pointer
  lifts) on fine pointers; focus lifts the top-left corner, steady.
  Pile: on a fold, the tray rises 200ms and the new label inks in
  (200ms fade); on the last unfold, the tray retires 300ms.
- **States.** Rest: flat, hem showing. Hover: corner-lift ≤3° + palm
  band (§6.9). Focus: corner-lift (top-left) + woven outline.
  Folded: creased (§6.10), lift pivots on the creased corner.
  Out-of-stock cloth: the card's hem is stamped "All cut" in
  `--straw-deep`, its press control disabled, no lift, no band —
  the cloth is spoken for and the card says so plainly.
- **Content merge.** The card is not a box containing a product; it
  is the product, folded. Its ground is the page's cloth, its label
  is woven, its selection is a fold, and the pile is the visitor's
  own folding accumulated — commerce conducted entirely in the
  material.
- **Failure fallback.** No JS: cards are links to product pages with
  prices in text; the pile does not exist and nothing refers to it.
  If the tray's DOM is removed by a11y tooling or an error, folding
  still works card-locally (§6.10) — the pile is a view of the
  state, never its home.
- **Reduced-motion variant.** No corner-lift (cards rest flat; hover
  state is the palm band's static variant, §6.9), tray appears and
  retires instantly. Folds and counts are unaffected.
- **Performance budget & mobile variant.** Lifts are transform-only
  on the hovered card. Mobile (<768px): grid 1-across, lift cut
  (tap = press, §6.10), the pile becomes a pinned bottom strip
  showing count + total + the onward link, labels expandable.
- **Choreography timeline (v2).** Entry: §6.4 reveal → hover: band
  in (240ms) + lift to ≤3° (350ms) → press: §6.10's sequence → tray
  rise (200ms) + label ink (200ms) → unfold: crease out (300ms),
  label fades (150ms), tray retires if emptied (300ms).
- **State matrix (v2).** *Rest:* flat. *Hover:* lift + band.
  *Focus:* lift (top-left) + outline. *Active:* press transit
  (§6.10). *Scrolled-past:* state (creases, pile) persists.
  *Disabled:* "All cut" card — no lift/band/press. *Touch:* no lift;
  tap presses; pile strip pinned.
- **Breakpoints (v2).** ≥1200px: 3-across, foot tray. 768–1199px:
  2-across, tray as foot band. <768px: 1-across, bottom strip pile.
- **Edge cases & failure modes (v2).** *Many folds:* the tray lists
  scroll horizontally in fold order; the total recomputes from the
  DOM on every fold/unfold — the §10 audit folds three cards,
  unfolds one, and requires label, count and total to agree.
  *Prices in mixed currencies or per-metre vs per-cloth:* the label
  states its unit in words ("per metre", "the whole cloth") — a
  total is only shown when all folded cloths share a unit basis,
  else the tray shows the count alone and says why (§12's honesty
  rule for figures).
- **Accessibility spec (v2).** Cards' press controls are real
  buttons with `aria-pressed` (§6.10); the pile is a labelled
  region with a polite live count; unfold controls are named per
  cloth ("Unfold the damask tablecloth"). Lift and band are
  decorative. Touch targets ≥48px on the strip variant.
- **Tokens consumed (v2).** `--linen`, `--straw`, `--straw-deep`,
  `--loom`, `--ease-press`, `--dur-lift` (350ms).

### 6.14 The bolt form

- **What & why.** The conversion form is a length cut from the bolt:
  its fields are ruled lines on finished damask (it lives in the
  weaving stage, §7 — you cannot order cloth the page hasn't woven),
  its quantity is a length in metres cut against a printed scale at
  the field's edge, and its success state is the cut length itself —
  ticketed with the order's reference, its end frayed honestly
  (a woven fringe edge, drawn) because cut cloth frays. The form's
  errors are the weaver's voice (§12): plain, material, unembarrassed.
- **Structure.** A `<form>` on the damask ground (§6.17's texture at
  60%): fields for the cloth (a select rendered as a woven list —
  the folded pile's contents offered first if any, §6.13), length in
  metres (number field with the scale rule printed beside it, 0.5m
  steps, the record's remaining bolt length stated as text: "342
  metres from this crop; 41 already cut"), name, direction (address),
  and the cutting button — a full-width woven band labelled "Cut my
  length". Error notes sit in the margin in `--flower-deep` — no,
  in the weaver's plain `--loom` with a woven tick: errors are not
  flowers (§12). The success panel replaces the form: the ticketed
  length, its fringe, the reference (derived from the record: crop
  year + the order's position in the day's cutting list, counted,
  never randomised).
- **Motion spec.** Focus: the field's ruled line draws in from the
  left over 260ms `--ease-loom` and a small woven tick settles at
  the line's start. Length field: as the value changes, the scale
  rule's marker moves and a fringe preview at the form's foot grows
  or shrinks thread by thread (each 0.5m = one fringe thread, capped
  at 24 threads, the count beyond stated in words). Submit: the
  button band presses (§6.10's grammar, 300ms), the form's ground
  crossfades to the success length over 500ms `--ease-weave`, the
  ticket's reference inks last (200ms).
- **States.** Rest: ruled lines at 40% ink. Focus: line drawn, tick
  settled. Filled: line at 70% ink (a written line is darker —
  §6.16's sibling ruling). Error: line in `--flower-deep`? No —
  error lines carry a double tick and the note in the margin; colour
  alone never carries the error (the note is text). Submitting:
  button pressed, fields disabled, a "Cutting…" line in the form's
  own voice. Success: the ticketed length. Disabled (bolt
  exhausted): the form is replaced by the fallow note (§6.18's
  grammar) — "This crop is all cut" — with the next sowing's date.
- **Content merge.** The form sits on the cloth it sells, cut from
  the record it cites: its availability figure is §6.15's record
  printed a second way, and its success is a piece of the page's own
  bolt, fringed. Nothing about it is a generic checkout wearing a
  costume.
- **Failure fallback.** No JS: a plain, working form (native submit)
  with all figures printed as static text and the scale as a printed
  ruler image with alt text. Validation errors from the server
  render in the same margin-note grammar. A failed submit preserves
  every field's value — cut cloth is not wasted, and neither is
  typing.
- **Reduced-motion variant.** Lines ink instantly on focus, fringe
  preview steps without thread-by-thread growth, success replaces
  instantly. All states and figures identical.
- **Performance budget & mobile variant.** The fringe is ≤24 small
  divs/SVG strokes; negligible. Mobile (<768px): the scale rule
  moves above the length field (horizontal), the margin notes stack
  under their fields, the button band stays full-width at ≥52px.
- **Choreography timeline (v2).** Focus → line draw 260ms + tick →
  length change → marker move (150ms) + fringe thread ±1 per 0.5m →
  submit → press 300ms → ground crossfade 500ms → ticket reference
  inks 200ms → pile (§6.13) clears its folded cloths into the order
  (labels retire in order, 90ms stagger).
- **State matrix (v2).** *Rest:* 40% lines. *Hover:* field rows warm
  3% (the palm's memory, §6.9, at rest strength). *Focus:* drawn
  line + tick + §11 outline on the input. *Active:* button press.
  *Scrolled-past:* values persist; returning finds the form as left.
  *Disabled:* bolt-exhausted fallow state. *Touch:* identical;
  targets ≥48px, the scale marker drags with the stepper buttons
  provided (the field is never drag-only).
- **Breakpoints (v2).** ≥1200px: two-column fields on damask, margin
  notes in the rail. 768–1199px: single column, notes under fields.
  <768px: single column, scale above the field, fringe preview cut
  to 12 threads with the count in words.
- **Edge cases & failure modes (v2).** *Length beyond the bolt:* the
  field refuses past the record's remainder with the weaver's note
  ("The bolt holds 41 metres more — shall we cut that, and the rest
  from the next crop?") and offers the split; it never silently
  clamps. *Pile empty:* the cloth select lists the full range; the
  form never requires the pile. *Zero-length:* treated as an error
  in the same voice ("A length of nothing is a sample — ask for a
  swatch instead") with a swatch link.
- **Accessibility spec (v2).** Real labels, `aria-describedby` for
  notes and the scale's text equivalent ("Length in metres, in
  half-metre steps; 41 metres remain on this bolt"). Errors are
  announced via a polite live region and focus moves to the first
  error field. Contrast: form text `--loom` on damask `--linen`,
  8.15:1; notes `--loom` — errors never rely on hue.
- **Tokens consumed (v2).** `--linen`, `--loom`, `--loom-soft`,
  `--stem-deep`, `--ease-loom`, `--ease-weave`, `--ease-press`,
  `--dur-field-line` (260ms).

### 6.15 Field figures

- **What & why.** The page's numbers — straw harvested, days in the
  dam, clean fibre, thread count, metres woven — count up once when
  their stage locks, and every one of them is a field of the single
  crop record. The figures are the process's evidence; a visitor who
  remembers one number should remember a true one, and the same
  number must read identically in the dateline (§6.2), the record
  table (here) and the footer (§6.17) — three printings, one object.
- **Structure.** A record table in the weaving stage: rows named in
  the record's own words ("Straw from the Long Field — 2,140 kg";
  "In the dam — 9 days"; "Clean fibre after scutching — 386 kg";
  "At the loom — 165 threads to the inch"; "Cloth from this crop —
  342 metres"), each row's figure a tabular Source Serif numeral
  (§3 law 2). The datelines of §6.2 and the footer's colophon read
  the same object at build time; in the DOM the figures are the
  final values, always.
- **Motion spec.** Trigger: the owning stage's lock (§6.2) for
  dateline figures; the table's own entry (70% viewport) for its
  rows. Each figure counts from the previous stage's true value (or
  from 0 where the record begins) to its true value over 900ms
  `--ease-weave`, whole steps only, tabular — a kilogram counter
  never shows decimals it doesn't own. Counting happens once per
  session per figure.
- **States.** Rest: the true figure, printed. Counting: transit
  between two true values. Scrolled-past uncounted (jumped): the
  true figure, instantly — the record does not perform for an empty
  room. Hover/focus: none.
- **Content merge.** The figures are not dashboard dressing; they
  are the crop's account of itself, placed at the stages that earned
  them. The thread count row carries the theme's fixed poetic line
  as its note (§12) — the poetry is attached to the fact it
  describes.
- **Failure fallback.** No JS: figures print at their true values
  (they are the DOM). Watchdog: a count interrupted (tab hidden)
  snaps to the true value on return — a figure may never rest at a
  number the record doesn't hold.
- **Reduced-motion variant.** No counting. Figures print true. The
  record loses nothing — its power was never the roll.
- **Performance budget & mobile variant.** Five counters maximum per
  page, text-only updates at most once per frame. Mobile: identical;
  the table stacks label-over-figure at <768px, figures unchanged.
- **Choreography timeline (v2).** Stage lock (§6.2) → dateline
  figure counts 900ms → table entry → rows count in row order, 120ms
  stagger, each 900ms → footer figure (§6.17) does not count (it is
  a colophon, not a counter — it prints).
- **State matrix (v2).** *Rest:* true figure. *Hover / focus:*
  none. *Active:* n/a. *Scrolled-past:* true figure. *Disabled /
  no-JS:* true figure. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: table at 9 columns (§4).
  768–1199px: table at full measure. <768px: stacked rows.
- **Edge cases & failure modes (v2).** *Record updated mid-season*
  (more cloth cut, §6.14): the bolt-remainder figure is the record's
  one living value; it reprints (no count) wherever it appears, and
  the audit (§10) requires all its printings to agree at any sampled
  moment. *A figure the record cannot supply:* the row is omitted —
  the record has no "approximately" (§12); an absent row is honest,
  an invented figure is a gate failure.
- **Accessibility spec (v2).** Counting figures carry
  `aria-hidden` animated spans with a visually-hidden true value
  beside them, so assistive technology always reads the record, not
  the performance. The table is a real `<table>` with row headers.
- **Tokens consumed (v2).** `--loom`, `--flower-deep`,
  `--ease-weave`, `--dur-count` (900ms).

### 6.16 Burlap skeleton & the cloth-lift transition

- **What & why.** Loading in this theme is loose burlap: skeleton
  lengths woven at the coarsest pitch (14px), their blocks the shape
  of the coming content, because a page being made first exists as
  raw material. Navigation lifts the woven page like a cloth — the
  current page rises from its bottom edge, folding softly, and the
  new page is laid beneath it. The two are one element's two duties:
  nothing in this theme appears from nothing; it is either still
  burlap or being lifted away.
- **Structure.** Skeleton: per-route placeholder lengths in the
  burlap texture, block heights matched to the real layout's anatomy
  (headline bar at measure, text lengths, a framed square where
  §6.8's figure will sit), `aria-busy` on the region, and the fixed
  status line in the weaver's voice: "Still on the loom…" Transition:
  a full-viewport cloth layer (the leaving page's own ground texture
  at its final pitch) that lifts via a bottom-anchored fold —
  rotateX from the bottom edge to −24° with a soft shadow gathering
  beneath — while the incoming page fades in under it.
- **Motion spec.** Skeleton: shows only if content is not ready
  within 150ms; resolves length by length as real content lands,
  each swap a 300ms `--ease-weave` crossfade; hard resolve at
  2000ms — whatever is still burlap at 2000ms is replaced by the
  honest note "This length is still on the loom" with a retry, never
  left as a silent skeleton. Transition: lift 550ms `--ease-loom`,
  incoming page revealed beneath in the lift's final 200ms; return
  navigation reverses the fold. Modified clicks (new tab etc.)
  bypass entirely.
- **States.** Skeleton: waiting → resolving → resolved (removed).
  Transition: at rest (no layer) → lifting → laid (layer removed).
  A third navigation inside 5s degrades the lift to a 200ms
  crossfade — even cloth tires of ceremony.
- **Content merge.** The skeleton is the page at its first process
  stage and the transition is the page handled as the cloth it has
  become — both are the theme's material logic applied to the
  browser's two rudest moments (waiting, leaving).
- **Failure fallback.** If the transition's layer fails to remove
  (JS error mid-navigation), a 1200ms watchdog removes it — a cloth
  may never be left hanging over a page. No JS: ordinary navigation,
  no skeleton (server renders the page whole).
- **Reduced-motion variant.** No skeleton animation (burlap lengths
  print statically if needed at all), no lift — pages change by
  instant swap with the selvedge stitch (§6.11) marking the new
  place.
- **Performance budget & mobile variant.** The cloth layer is one
  composited element reusing §6.1's textures. Mobile (<768px): the
  lift becomes a simple rise-and-fade (no rotateX fold — small
  screens get a lifted hem, not a folded bolt), 400ms.
- **Choreography timeline (v2).** Navigation click → t=0 lift begins
  (550ms) → t=350ms incoming page begins fading beneath → t=550ms
  cloth layer removed, focus lands on the destination's headline →
  stitch slide (§6.11, 350ms) settles the nav.
- **State matrix (v2).** *Rest:* no layer. *Hover / focus:* n/a.
  *Active:* the lift itself. *Scrolled-past:* n/a. *Disabled /
  no-JS:* native navigation. *Touch:* identical; swipe-back gestures
  are the browser's and are never hijacked.
- **Breakpoints (v2).** ≥1200px: full fold lift. 768–1199px: fold at
  −16°. <768px: rise-and-fade 400ms.
- **Edge cases & failure modes (v2).** *Slow route:* the skeleton's
  2000ms honesty rule fires regardless of the transition's state.
  *Anchor-only navigation* (same page): no lift — the stitch and
  the scroll do the work. *Prefetch:* prefetched pages skip the
  skeleton entirely; burlap is for genuine waiting only.
- **Accessibility spec (v2).** The skeleton region is `aria-busy`
  with the status line as its accessible name; focus is never moved
  by the skeleton. The transition moves focus to the destination
  headline only after the layer is removed, and announces the page
  via its title as normal navigation does.
- **Tokens consumed (v2).** `--straw`, `--loom`, `--ease-loom`,
  `--ease-weave`, `--dur-lift-page` (550ms), `--dur-skeleton-cap`
  (2000ms).

### 6.17 The damask colophon footer

- **What & why.** The footer is the finished cloth's own end: the
  finest damask on the page (3px pitch, motif at full), the margin
  thread (§6.6) arriving woven as its stripe, and a colophon that
  accounts for the page the way a cloth's end accounts for the bolt —
  what field, what record, what remains. Body text sits directly on
  the damask here, the promise of §1 kept literally: the last words
  are printed on finished linen.
- **Structure.** A `<footer>` on the damask ground at 60% texture
  opacity (§4's calm ruling): three columns — the process recap
  (five stages as a still strip with their figures, §6.15's third
  printing), the house columns (cloth, field notes, contact — plain
  links), and the colophon proper: "Woven from the Long Field's
  crop · 342 metres · the margin thread is one of them" set in
  Newsreader italic, then the legal line in 13px `--straw-deep`. The
  thread's stripe terminates in a woven knot segment at the
  colophon's first line.
- **Motion spec.** Entry: the footer is revealed by the last
  loom-beam (§6.4) like any section. The damask motif's light rests
  — the footer's one ambient behaviour is a 9s, ±2% luminance breath
  in the motif layer only, the page's second licensed ambient loop
  (§5), paused off-screen and killed entirely once the visitor
  scrolls back above the weaving stage. The process strip does not
  animate; a recap is a record, not a show.
- **States.** Rest: printed damask, colophon set. Hover on links:
  woven tick inks (§6.11's grammar). Scrolled-past: the footer is
  the end; there is no past.
- **Content merge.** The footer is not styled like the theme; it is
  the theme's product, finished — the ground the whole scroll was
  making, finally sat upon by the site's own small print.
- **Failure fallback.** No JS: the footer prints complete, motif
  static, strip and colophon present. Nothing in the footer waits
  for anything.
- **Reduced-motion variant.** No breath in the motif. The damask
  rests fully printed — under reduced motion the whole page's weave
  is mid-fineness (§6.1), and the footer prints its damask as a
  *pattern* (drawn, static) rather than the earned texture: the one
  place the theme lets the finished cloth appear unearned, because a
  footer must be a footer.
- **Performance budget & mobile variant.** Motif breath is one
  opacity value on one layer. Mobile (<768px): columns stack —
  colophon first (the account before the links), strip becomes a
  vertical list, the thread's stripe arrives as the top selvedge's
  final segment (§6.6).
- **Choreography timeline (v2).** Footer enters → §6.4 reveal 700ms
  → thread stripe completes at the colophon's line (§6.6) → motif
  breath begins after 1s of rest → scrolling away above weaving
  ends the breath permanently for the session.
- **State matrix (v2).** *Rest:* printed. *Hover:* link ticks.
  *Focus:* §11 outline. *Active:* n/a. *Scrolled-past:* n/a.
  *Disabled / no-JS:* printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three columns, motif full.
  768–1199px: two columns, colophon spanning. <768px: stacked,
  colophon first.
- **Edge cases & failure modes (v2).** *Short pages* (§7): the
  footer's damask still prints at full fineness even where the
  journey was compressed — the law (§1) governs the *earned* texture
  of sections; the footer is the maker's mark and is licensed to be
  finished, as a book's colophon is printed on the book's best paper
  regardless of the reader's path. §10's audit samples section
  grounds, not the footer's. *Missing record:* if the crop record
  fails to load, the colophon prints its form with the figures
  omitted and the line "the record is in the field book" — never a
  placeholder number.
- **Accessibility spec (v2).** Footer text `--loom` on `--linen`
  damask at 8.15:1, measured over the motif at its 60% setting
  (§10's audit samples it). The process strip duplicates §6.15's
  table in summary; it is marked as a summary list, not a second
  table, so assistive technology meets the record once in full.
- **Tokens consumed (v2).** `--linen`, `--loom`, `--straw-deep`,
  `--weave` (read), `--ease-loom`.

### 6.18 The fallow page

- **What & why.** The 404 is an unplanted field: a length of the
  page where nothing was sown. It shows the field ground at its
  loosest (the journey reset to before the beginning), one line in
  the grower's voice — "Nothing was sown here." — the address the
  visitor asked for, printed as the record would print it, and the
  two honest ways onward: back to the field (home) or to the cloth
  (the shop). A fallow field is not an error in farming; it is a
  field resting, and the page treats the visitor's wrong turn with
  the same lack of embarrassment.
- **Structure.** A single section on the field ground (burlap at
  14px over the stem wash): the heading "This length was never
  sown." in Newsreader, the requested path in the record's tabular
  setting, one line of explanation ("The address is written down,
  but no crop answers to it."), and two woven links. A single flax
  stem (§6.7's plate, small) stands at the margin — unsown ground
  still borders the field. No search box is offered: the theme
  refuses to pretend a search would till this (§11).
- **Motion spec.** None, by design — the fallow page's choreography
  is stillness. The stem does not draw; the breeze does not pass.
  The only motion available is the visitor's own departure via
  §6.16's lift.
- **States.** Rest: the fallow field, entire. Every interactive
  state belongs to its two links (§6.11's grammar).
- **Content merge.** The 404 is the journey's negative: the one page
  where the process never began, proving by contrast what every
  other page's ground means. Its ground is §6.1's first layer with
  the weave value forced to 0 — the law (§1) holds even here:
  nothing was made, so nothing is woven.
- **Failure fallback.** The fallow page *is* a fallback; it must
  itself never fail — it ships as static HTML with no armed states,
  no JS dependencies, and its links are ordinary anchors.
- **Reduced-motion variant.** Identical — stillness was already the
  design.
- **Performance budget & mobile variant.** The lightest page on the
  site: shared textures only, ≤40KB total. Mobile: identical,
  stacked.
- **Choreography timeline (v2).** None. Arrival → the field, resting
  → departure by §6.16 when the visitor chooses a link.
- **State matrix (v2).** *Rest:* fallow. *Hover / focus:* its links
  only (§6.11 grammar, §11 outline). *Active:* link press.
  *Scrolled-past:* n/a — the page is one screen by design at every
  breakpoint (min-height 100vh, content centred in the upper two
  thirds, the lower third left fallow). *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: as described. 768–1199px: stem at
  70% scale. <768px: stem cut — the margin is too narrow for a
  border plant; the field is field enough.
- **Edge cases & failure modes (v2).** *A path that exists but whose
  crop failed* (a product whose cloth is all cut): that is §6.14's
  bolt-exhausted state, not this page — the fallow page is only for
  addresses never sown, and using it for sold-out cloth would lie
  about the record. *Very long requested paths:* the path prints
  truncated at 60 characters with the full path in its `title` — the
  record abbreviates, it does not overflow.
- **Accessibility spec (v2).** The heading is the page's `<h1>`; the
  requested path is real text. The page's stillness is total —
  nothing moves, flashes or autoplays on the page where the visitor
  is already lost.
- **Tokens consumed (v2).** `--stem`, `--straw`, `--loom`,
  `--weave` (forced 0).

## 7. Page application map

- **Home / journey page.** The full bolt: hero (§6.12), five stages
  (§6.2), the record (§6.15), cloth cards (§6.13), the bolt form
  (§6.14), damask footer (§6.17). The reference build; every other
  page type is a length cut from it.
- **Listing (the cloth room).** Opens at the spinning stage's ground
  — a listing is yarn, not field: no hero field, no breeze; the
  weave begins at 5px and tightens across the list. Cards §6.13,
  frames §6.8, filters as woven lists (§11). The margin thread runs,
  compressed (§6.6's short-page rule).
- **Detail (one cloth).** Begins at weaving: the ground is damask
  from the first screen (the law's licensed exception — a single
  cloth *is* finished goods; §10's audit checks detail pages against
  the finished pitch, not the journey). Swatch frames §6.8 at full
  fineness, the record rows for this cloth only (§6.15), the bolt
  form (§6.14) as the page's conversion. The field appears once, as
  the cloth's provenance note with §6.7's plate.
- **About (the field book).** The grower's pages: field and retting
  grounds throughout (the about page lives early in the process —
  it is about the makers, not the product), §6.7's plate licensed
  here as its one draw, stage bands reduced to two (harvest,
  retting) under §6.2's order rule.
- **Contact / the field gate.** A short page at straw ground: the
  form grammar of §6.14 at letter scale (a note, not a cutting),
  success = the note ticketed. No pile, no prices.
- **The fallow page.** §6.18, for addresses never sown.

## 8. Worked examples

### 8.1 The hero — "the field, standing" (scroll timeline)

Build order within the hero: ground stack (§6.1, burlap layer over
the stem-washed field ground) → dateline → headline base layer →
stem stand (§6.3) → standfirst (armed for §6.4) → action line →
thread birth (§6.6). Timeline: t=0 first paint — dateline and the
printed headline are already legible; the page is honest before it
is beautiful. Fonts resolve (~t=300ms) → the headline arms and beats
(1200ms, §6.5): tracking +0.06em → −0.01em, fibres fading from
t=700ms. At beat +600ms the breeze leaves the leftmost stem and
crosses the stand by t≈3200ms (§6.3). At beat end the standfirst
rises under its loom-beam (700ms, §6.4) and the action line's arrow
settles. The visitor's first scroll now meets a hero already at
rest — nothing in the hero performs twice.

### 8.2 Mid-page — the retting band (scroll timeline)

The reader leaves harvest (ground at 10px pitch) and the retting
band's top crosses 78% viewport: its copy was armed by §6.4 and the
beam rises (700ms). The band pins (60vh): across the pin, §6.1's
crossfade runs straw-ward (600ms, `--ease-weave`) — the ground
coarsens in colour as it refines in pitch, retting's paradox — and
the margin thread's treatment cleans from fuzzy toward smooth
(§6.6). At pin progress 0.85 the beat fires: 4px settle, 260ms, and
the dateline's figure — "9 days in the dam" — inks `--flower-deep`,
the stage's one blue word-group, while §6.15's counter for the
retting row counts to 9 (900ms). The copy beside the figure explains
what 9 days of water does to a stem. Text, texture, thread and
figure have all told the same fact in the same 2 seconds.

### 8.3 Conversion — cutting a length (scroll timeline)

The reader, in the weaving stage, has folded two cloths (§6.10,
§6.13): the pile tray holds their labels and their shared-unit
total. Entering §6.14's form, the cloth select already lists the
two folded cloths first. Focus enters the length field: its line
draws (260ms), the scale shows "342 metres from this crop; 41
already cut" — so 301 remain, and the record agrees with itself in
both places because it is one object. The visitor enters 3.5: the
scale marker moves, seven fringe threads grow at the form's foot.
An error on the direction field (no second line) draws the double
tick and the weaver's note: "The second line is wanting — cloth
goes astray without it." Corrected, the cut button presses (300ms),
the ground crossfades to the cut length (500ms), the ticket inks its
reference — crop year and the day's cutting count, derived — and the
pile's two labels retire in order, folded into the order. The
bolt-remainder figure reprints at 297.5 everywhere it lives, without
counting (§6.15's living-value rule).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The disagreed ground.** A damask frame in the raw field, a
   footer finer than its form. *Cure:* one `--weave`, four
   printings, §10's audit samples all four at five scroll positions.
2. **The misprinted headline.** Fibre layers misaligned after a font
   swap or CMS edit. *Cure:* §6.5's race and live-generation rules —
   when in doubt, the headline ships printed.
3. **The percentage bar.** Progress rendered as %, a bar, or "Step 3
   of 5". *Cure:* the thread (§6.6) is the only progress the theme
   knows; percentages are banned from progress copy (§12).
4. **The blue garden.** `--flower` spread as a brand colour across
   buttons and links. *Cure:* the ≤3% pixel budget (§2) and §3's
   one-blue-word law; blue is a flower, rationed like one.
5. **The spotlight palm.** Hover bands at 20% lift, glossy and
   proud. *Cure:* §6.9's 8% cap — a palm warms cloth; it does not
   stage-light it.
6. **The backwards rhythm.** A crowded field, an airy footer.
   *Cure:* §4's density law — information tightens as texture
   loosens its grip; audit by screenshot at both ends.
7. **The shouted figure.** Thread counts at display size, coloured,
   exclaimed. *Cure:* §3 law 2 — figures set tabular at record size,
   and the poetry line (§12) does the boasting quietly, in italic.
8. **The haunted field.** The breeze still swaying sections the
   visitor has harvested past. *Cure:* §6.3's cancellation rules —
   past the weaving stage, the field is cut and does not move.
9. **The imported grotesque.** A sans crept in for "UI clarity" on
   data. *Cure:* two faces only (§3); Source Serif's tabular figures
   are the data voice.
10. **The instant cloth.** A detail page or listing that opens on
    burlap it never weaves, or a journey page whose footer arrives
    unearned because the pins were cut for time. *Cure:* §7's
    licensed exceptions are named and audited; everything else
    earns its ground or ships the static strip (§6.2).
11. **The frayed lie.** Fringes, folds and creases applied to things
    that are not cloth — fringed buttons, folded modals. *Cure:*
    the material metaphors belong to material objects only (§11's
    refusals); chrome stays chrome, woven.
12. **The generic pastoral.** Stock-photo wheat, clip-art leaves,
    "artisanal" in the copy. *Cure:* the theme's imagery is flax or
    nothing — §6.7's plate, §6.3's stand, §6.8's real photographs of
    the actual process — and §12's banned list keeps the copy honest.

## 10. Quality gate

Blocking (all must pass before the theme ships in a build):

1. **Ground-law audit.** At five sampled scroll positions, the
   background pitch, one frame's pitch (§6.8), the thread's
   treatment (§6.6) and — at the foot — the damask (§6.17) agree
   with `--weave` within one stage step. Any disagreement fails.
2. **Figure-truth audit.** Every number on the page is traced to
   the crop record object; the same figure agrees across dateline,
   table and footer printings (§6.15). An untraceable figure fails.
3. **No-strand audit.** With JS disabled, and again with the loop
   artificially stalled, every section is fully readable; every
   watchdog in §6 fires within its stated cap.
4. **Contrast audit.** Text sampled on its stage ground at the
   coarsest and finest pitches meets §2's licensed pairings (≥6.03:1
   for body on straw, 8.15:1 on linen; footer measured over the
   motif at 60%).
5. **Blue census.** `--flower` pixels ≤3% of any viewport sample;
   `--flower-deep` text ≤1 blue word-group per stage band (§3).
6. **Pin census.** Exactly the stage pins exist (5 journey / fewer
   only by §6.2's end-omission rule); total pinned distance ≤300vh.
7. **Palm cap.** §6.9's band measured at ≤8% luminance lift in a
   hover screenshot.
8. **Three-printings rehearsal.** Fold three cloths, unfold one:
   creases, pile labels, count and total agree (§6.13); submit
   §6.14's form with an error: values preserved, note in the
   weaver's voice, focus on the first error.
9. **Reduced-motion pass.** The full journey under
   `prefers-reduced-motion`: static strip, mid weave, printed
   headline, no breeze, no lift — and every fact still present.
10. **Gate signed by a non-builder.** The auditor is never the
    agent who built the page (§15, step 15).

## 11. Component inventory

Every component a real Linen Field site needs, with its themed
treatment — and the refusals, which are part of the inventory.

- **Buttons.** Woven bands: full-width or measure-width bands in the
  stage's cloth with `--loom` text; press = §6.10's settle (2px,
  300ms). Primary (the cut button, §6.14) is a double-density band.
  No rounded corners anywhere in the theme — cloth is cut square;
  the only radius is a fold's softness, which is a shadow, not a
  radius.
- **Links.** Text with woven-tick underlines (§6.11's grammar);
  visited links ink `--straw-deep` — a read link is a handled cloth.
- **Inputs.** Ruled lines on the ground (§6.14): 40% ink at rest,
  drawn on focus, 70% when filled. Labels above, in the record's
  voice. Never floating labels — cloth does not float.
- **Selects.** A woven list: the closed field shows the chosen cloth
  as a folded label; opening unfolds the list downward (350ms
  `--ease-loom`), options as folded lengths. Native `<select>`
  underneath for no-JS and assistive technology.
- **Checkboxes / radios.** Woven ticks and filled squares drawn in
  thread (SVG stroke, 200ms draw) — a tick is a stitch, square
  corners.
- **Tables.** The record table (§6.15) is the pattern: row rules are
  selvedge lines, row headers in the record's voice, figures
  tabular. No zebra striping — the weave is the texture; striping
  would double-weave the page.
- **Cards.** Cloth cards (§6.13) only; there is no generic card.
- **Badges.** Refused. A cloth's state is stated in words on its
  label ("All cut", "Last length") — a badge is a sticker on linen.
- **Alerts / notices.** Margin notes in the weaver's voice (§12),
  set as woven slips pinned at the relevant field or section — the
  §6.14 grammar generalised. Never a banner across the top: nothing
  interrupts the bolt.
- **Toasts.** Refused. Confirmations live where the act happened
  (the ticketed length, §6.14; the filed note) — cloth does not pop.
- **Modals.** Refused. Anything that would be a modal is a folded
  panel in the flow (the nav disclosure, §6.11; the pile's expanded
  labels, §6.13) — the page folds; it does not overlay.
- **Tabs.** Refused. Stages are a journey, not tabs; a "tabbed"
  process would let a visitor skip retting, and §6.2 forbids the
  skip in spirit and in fact.
- **Pagination.** A bolt is continuous: listings continue by "the
  next length" — an in-flow continuation that appends the next
  lengths under a selvedge rule. Numbered pages are refused; the
  record counts metres, not pages.
- **Accordions.** Folded lengths: a heading band that unfolds its
  content downward (400ms `--ease-loom`), one open at a time, the
  fold line visible. Used for field notes and care instructions.
- **Progress bars / spinners.** Refused, both (§9, failure 3; §6.16
  is the loading language).
- **Tooltips.** One licensed exception: the thread's stage-name
  label (§6.6), rendered as a woven label. Nothing else explains
  itself on hover.
- **Search.** Refused on the fallow page (§6.18); on the cloth room
  (§7) search is a woven list filter, in-flow, filtering the real
  cards (§6.13) with a counted result line in the record's voice.
- **Breadcrumbs.** The stage path: field › harvest › retting › … —
  the process as the path, each step a link to its band. A product's
  breadcrumb is its making.
- **Focus treatment (all components).** A woven outline: 2px
  double-density stitch in `--stem-deep` offset 3px, drawn as a
  dashed thread — visible on every ground (§2 pairings), never a
  glow.

## 12. Content & copywriting voice

Two registers. **The Grower** speaks in Newsreader italic, first
person, from the field: short, weather-aware, unhurried — datelines,
field notes, the poetic asides. **The Record** speaks in Source
Serif roman, third person, from the field book: labels, figures,
errors, confirmations — plain, exact, kind. A sentence must know
which of them is speaking; mixing registers inside a sentence is the
voice's one unforgivable sin.

**Headlines** are names, not slogans: the crop, the cloth, the
stage. ✓ "The Long Field, this year." ✗ "Discover Nature's Miracle
Fabric!" (an exclamation, a miracle and a slogan — three bans in
nine words). **Labels** are the record's nouns: "Length, in metres",
"Direction — the second line is for the lane". **Figures** always
carry their unit and their source is the record: ✓ "342 metres from
this crop" ✗ "hundreds of metres woven!".

**The fixed line.** The theme's anti-slop detail is a verbatim
string, set in the Grower's italic as the thread-count row's note
(§6.15): *"woven at 165 threads, because 200 felt like showing
off."* It appears once per page, attached to the fact it describes,
never as a hero slogan.

**Error voice** (the Weaver, a third register used only at the
form): plain, material, forward-looking. ✓ "The second line is
wanting — cloth goes astray without it." ✓ "A length of nothing is
a sample — ask for a swatch instead." ✗ "Oops! Invalid input."
✗ "Please kindly re-check your details." **Empty states:** the
fallow grammar (§6.18): ✓ "Nothing was sown here." ✗ "No results
found 😢". **Confirmation voice:** the ticket speaks: ✓ "Cut and
ticketed. Your length leaves with Friday's post." ✗ "Success! Your
order has been placed successfully!"

**Banned words:** artisanal, rustic (as praise), miracle, oops,
successfully, "just", percentages in progress copy, exclamation
marks in the Record's voice (the Grower may use one per page, in a
field note, about weather). **Owned words:** sown, retted, scutched,
hackled, beaten (of weft), length, bolt, fallow, the dam.

## 13. Full-page scroll choreography map

The journey page, top to footer, every beat in order:

1. **Arrival.** Dateline + printed headline legible at first paint;
   the field stands in burlap (14px). The visitor sees a crop, not a
   loading state.
2. **The beating.** Headline tightens over 1200ms; fibres fade; the
   name seats itself (§6.5).
3. **The breeze.** One wave crosses the stems (§6.3); the field is
   alive, once.
4. **The standfirst rises** under the loom-beam (§6.4, §6.12); the
   thread is born fuzzy at the headline's baseline (§6.6).
5. **Harvest.** First pin: ground steps to 10px, beat at 0.85, the
   dateline's 2,140 kg inks and counts (§6.2, §6.15); stems parallax
   away above (§6.12).
6. **The plate grows.** §6.7's stem draws itself in growth order in
   the field copy's margin.
7. **Retting.** Pin: ground to straw at 7px; thread cleans; "9 days"
   counts; the copy is about water and waiting, and the pin makes
   the reader wait a measured 60vh for it.
8. **Scutching.** Pin: ground refines; 386 kg counts; the shortest
   band — scutching is quick, violent work and the page hurries it
   politely.
9. **Spinning.** Pin: ground to 5px; the thread goes smooth in the
   margin — the visitor watches the indicator become the product.
10. **Weaving.** Pin: ground to 3px and the damask motif fades in
    (§6.1); the record table's rows count (§6.15); the fixed line
    appears under the thread count.
11. **The cloth room.** Cards revealed length by length (§6.4,
    §6.13); palms cross cloth (§6.9); the first fold creases and the
    pile tray rises (§6.10).
12. **The cutting.** The form on damask (§6.14): lines draw, fringe
    grows by half-metres, the ticket inks.
13. **The end of the bolt.** Footer (§6.17): the thread arrives as a
    stripe and knots at the colophon; the process strip recaps the
    five figures; the motif breathes, once the reader rests.

**Reverse pass.** Scrolling up loosens the weave and un-draws the
thread (both positional), but locked stages stay beaten, counted
figures stay counted, creases stay creased — the page forgets its
texture before it forgets its facts. **Jump scroll** (anchor, find,
scrollbar drag): everything positional snaps within one frame
(§6.1's catch-up); everything latched (beats, counts, draws) is
completed instantly for stages above the landing point — the record
never performs for an empty room (§6.15).

**Timing contract.** Read at a natural pace, the journey page runs
2½–4 minutes: roughly 20 seconds in the field (beats 1–4), 15–25
seconds per stage pin (beats 5–10), and the cloth room and form at
the reader's own speed (beats 11–13). A reader who finishes in
under 40 seconds has flung through every pin — the catch-up rules
guarantee they still met every fact, printed and settled, but the
page does not chase them with delayed ceremony: nothing on this
page performs late for a reader who has already left the room.

## 14. Whole-page performance budget

- **Total page weight:** ≤850KB on the journey page, of which
  textures and the stem plate ≤60KB (all inline SVG, reused across
  §6.1/§6.3/§6.7/§6.8/§6.11 — the patterns are authored once and
  referenced, never duplicated per element); photographs (real
  process photography, §6.8) ≤600KB, lazy below the fold; fonts:
  Newsreader + Source Serif 4 subset to the page's glyphs, ≤120KB.
- **Frame budget:** the shared loop ≤1.6ms/frame all-in (weave
  scrub 0.5, thread 0.2, palm 0.3 when active, pins 0.3, slack 0.3);
  no single frame may exceed 8ms outside a stage crossfade, and a
  crossfade frame may not exceed 12ms. Long tasks: none over 50ms;
  the stem draw's path setup is build-time, not runtime.
- **Animation discipline:** transforms and opacity only, everywhere;
  `letter-spacing` animates on exactly one element (the headline,
  1200ms, once). No layout thrash: all scrubbed values are read once
  per frame from a single scroll snapshot.
- **Measurement method.** Budgets are verified on a Moto G-class
  Android over throttled 4G (1.6Mbps, 150ms RTT) with the loop's
  per-frame cost read from the Performance API across a full
  journey scroll, not estimated from a desktop trace — the theme's
  audience reads on farm and workshop phones, and the loom must
  keep time there first.
- **Cut order when the budget is exceeded:** (1) the footer's motif
  breath (§6.17); (2) the ambient breeze repeat (§6.3 — the load
  wave stays); (3) frame pitch stepping becomes band-static (§6.8's
  fallback); (4) the damask motif layer (§6.1) above the footer;
  (5) card corner-lift (§6.13). **Never cut:** the weave scrub
  itself, the thread, any watchdog, any figure, the crease/pile
  state system. A Linen Field page that cannot afford its ground has
  too many photographs, and the photographs go first (§6.8's budget
  is where the audit looks).

## 15. Build-order checklist

1. **The crop record first.** Author the record object (field,
   straw, dam days, fibre, thread count, metres, remainder) before
   any markup — every figure on the page will read it (§6.15).
2. **Static bolt.** Build the full page unpinned, unanimated, on the
   static mid-weave: all copy, all figures true, all forms working.
   This is the no-JS ship shape; it must already be a good page.
3. **Ground stack.** The five texture layers + damask motif (§6.1),
   flat-token fallbacks, contrast audit at both pitches (§10.4).
4. **Stage bands.** Pins, beats, datelines (§6.2); order rule and
   mobile merge checked.
5. **The thread.** Rail geometry, three treatments, static-strip
   fallback (§6.6).
6. **Hero assembly.** Dateline, headline base, stand, standfirst
   (§6.12); then the headline's fibre layer and beat (§6.5); then
   the breeze (§6.3).
7. **Reveals.** Loom-beam arming with watchdogs (§6.4); above-fold
   exemption verified.
8. **The plate.** §6.7's draw with baked path lengths.
9. **Frames.** §6.8's stage-matching wired to `--weave`.
10. **Cards and pile.** §6.13's grid, §6.9's palm, §6.10's crease —
    in that order, testing the three-printings agreement (§10.8) as
    soon as all three exist.
11. **The form.** §6.14 with its scale, fringe and ticket; error
    rehearsal with values preserved.
12. **Chrome.** Selvedge nav (§6.11), skeleton + lift (§6.16),
    footer (§6.17), fallow page (§6.18).
13. **The shared loop.** Move every scrubbed value into the single
    rAF loop (0.12 / 0.18); delete any surviving scroll handlers.
14. **Reduced-motion pass.** §10.9 end-to-end; the static strip,
    printed headline and mid weave verified as a complete page, not
    a degraded one.
15. **The gate.** §10 run by a non-builder; ground-law and
    figure-truth audits signed before the theme may be used.
