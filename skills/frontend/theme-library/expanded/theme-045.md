# 45. Indigo Vat — Expanded (v1 + v2)

> Expansion of theme #45 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same ten signature elements —
> deepened, never redesigned — plus eight page-family elements.

## 1. Concept & world

Real indigo performs a small act of theatre that no other dye can
match. Cloth lowered into the vat comes up **green** — the dye in its
reduced, oxygen-starved state — and only in the air, over a minute or
two, does it turn blue. A dyer judges the work by that turn: green
means the vat is alive; the blue that follows is the colour the cloth
will keep. This theme builds a website out of that chemistry. Every
section is a **dip**. A surface enters pale, takes the green, and
oxidises to the blue its dip-count has earned — and the dip-count is
not a metaphor the design team invented: it is the number of times
that surface has actually been immersed, counted from real events on
the page. Sections deepen one stage each time they are re-entered
(§6.3). A product deepens when a visitor's hand dips it (§6.9). The
footer, dipped by the whole visit, is the deepest blue on the page and
says so, with the visitor's own number in the sentence (§6.10).

The world is the dye house, treated as a complete interface
vocabulary. The page has a **vat** (the dark band at the hero's foot,
and the liquid every dip goes into), **cloth** (the content surfaces —
sections, cards, the hero panel — each one a piece with a dip history),
**the line** (the drying line the pieces hang from: the layout's
spine, the navigation's form, the transition's path), **the swatch**
(the margin instrument that records the reading's progress as a piece
of cloth darkening dip by dip, §6.4), and **the batch record** (the
ledger where every printed dip count traces to a real garment, a real
vat, a real number of days, §6.17). Nothing on the page is blue
decoration. Blue is a *record*: of immersions, of revisits, of a hand
that chose to dip again. **Depth of colour is the page's argument
about attention** — what you return to is what darkens — performed by
the chemistry itself rather than described by the copy.

**The theme's one law: a dip that didn't happen darkens nothing.**
Every resting shade on the page is the result of a counted immersion:
a section's stage is its real re-entry count this session (§6.3), a
product's stage is its real record plus the dips a visitor's hand
actually gave it (§6.9), the footer's depth is the visit itself
(§6.10). Every *printed* dip count — "9 dips, 3 days" beside a
garment — is the real garment's record, entered in the batch record
(§6.17) where a visitor can audit it. A build that pre-darkens a
section to look "rich", that prints a dip count no garment earned, or
that lets the footer claim dips the session never made, has not bent
the theme — it has painted dry cloth and called it dyed, and the
quality gate (§10) fails it on sight. Everything else in this theme
is craft. That one is the dyer's honesty.

**Dyeing is the interaction model.** The visitor's acts are a dyer's
acts: they watch the first piece come out of the vat and turn (§6.1),
they re-dip sections simply by returning to them (§6.3), they test-dip
a product by hovering it (§6.8) and commit a full dip with a click
(§6.9), and their progress is a swatch darkening in the margin
(§6.4) — a piece of the product being made alongside the reading.
The site does not have users scrolling a feed; it has apprentices at
a vat, learning that indigo cannot be hurried: each dip is shallow,
the depth is in the repetition, and the green always comes before the
blue. That is why the theme fits content with a genuine relationship
to repetition and patience — dyed goods, slow craft, anything whose
quality is literally a count of immersions or passes — and why it
curdles around anything instant, disposable or loud.

**Best-fit sites and audiences.**

- Indigo and natural-dye studios: the theme *is* the product's making;
  the hero performs the exact chemistry the cloth for sale underwent,
  and the batch record (§6.17) is the studio's real production ledger.
- Slow textiles and workwear: denim, sashiko, shibori, woven goods —
  products whose value is stated in dips, stitches and days, and whose
  makers already keep count.
- Craft process storytelling: any maker's site where the process is a
  repeated immersion — glazes dipped, prints pulled, coats applied —
  and the count of passes is a fact the maker is proud to print.
- Heritage dye and textile museums, workshops and courses: the dip
  ladder (§2) is the curriculum — visitors learn the stages by
  scrolling through them.
- Residency and workshop booking for dye houses: the commission form
  (§6.14) takes its order *by the dip* — cloth, yardage, target stage —
  which is how the work is actually specified at a real vat.

**When NOT to use it.**

- For products with no immersion story. If nothing in the catalogue
  was ever dipped, dunked, coated or passed through anything, the
  chemistry is a costume and the dip counts are fiction — §1's law
  cannot be kept, so the theme cannot be used.
- For content that must stay one colour. Brand systems with a locked
  single-blue identity will fight the ladder: this page's surfaces
  *change* stage as a record of use, and a legal team that needs every
  surface at one hex will unpick the theme's spine.
- For urgent, transactional flows. A dip takes 1450ms and the theme is
  proud of it; a checkout that must complete in one impatient minute
  should not ask its visitors to watch cloth oxidise. (The commission
  form §6.14 is the exception: an order *for dyeing* is allowed to
  take the dyeing's time.)
- For audiences who will never scroll back. Re-dipping (§6.3) is the
  theme's deepest mechanic and it only fires on return; a page read
  once, top to bottom, shows the first dip and the footer but never
  the ladder working. If the content has no reason to be revisited,
  half the theme is unloaded.
- Where green reads as "success". Interfaces dense with status
  semantics (dashboards, forms-heavy apps) will misread the transit
  green as confirmation. In this theme green means *not yet blue* —
  the opposite of done — and the collision is unresolvable.

## 2. Palette

Five anchors, inherited unchanged. The palette is a dip ladder: one
undyed cloth, one transit green, and three blues of increasing depth.
Nothing else is admitted; every other colour on the page is one of
these five, tinted, shaded, or set at an opacity over its own ground.

**The dip ladder (the palette's grammar).** A surface rests at exactly
one of five stages. Stages are *states with locked text pairings*, not
a gradient a builder may sample at whim:

| Stage | Name | Ground | Locked text colour | Contrast |
|---|---|---|---|---|
| 0 | Undyed | `--cloth` `#F3EEE3` | `--ink` (vat deep) | **12.88:1** (AAA) |
| 1 | First dip | `--dip-1` `#C9D1BD` | `--ink` (vat deep) | **9.46:1** (AAA) |
| 2 | Second dip | `--blue` `#33526B` | `--cloth` | **7.09:1** (AAA) |
| 3 | Third dip | `--vat` `#16283F` | `--cloth` | **12.88:1** (AAA) |
| 4 | Tenth dip | `--tenth` `#0A1420` | `--cloth` | **16.01:1** (AAA) |

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--cloth` | `#F3EEE3` | Undyed cloth: stage 0 ground, the page's paper, resist areas in shibori (§6.7), text on every blue stage | ~34% of pixels | On first blue **7.09:1**, on vat deep **12.88:1**, on tenth dip **16.01:1** — cloth is the only text colour admitted on blue grounds. On the transit green it is 2.68:1 — never text there (§5's transit rule). |
| `--green` | `#7A9B76` | Fresh-dip green: the transit colour ONLY — what cloth shows between leaving the vat and finishing oxidation | ~2% of pixels, never at rest | A verb, not a state: no surface *rests* at full green. On cloth 2.68:1 — never text, never an indicator on pale grounds. Vat-deep text over full green measures **4.81:1** and tenth-dip text **5.98:1** — the only pairings licensed during the transit window (§5). |
| `--blue` | `#33526B` | First blue: stage 2 ground, the hero cloth's resting colour after the first dip, links and rules on pale grounds | ~22% of pixels | Cloth on it 7.09:1 (AAA). On cloth grounds it is the link colour (7.09:1). On vat deep it falls to 1.82:1 — never letter anything on a deeper ground with a shallower blue. |
| `--vat` | `#16283F` | Vat deep: stage 3 ground, the hero vat band, `--ink` (all text on stages 0–1) | ~26% of pixels | As ink on cloth 12.88:1; on dip-1 tint 9.46:1. Cloth text on it 12.88:1. The vat band is this colour at full depth from first paint — the liquid was always deep; it is the cloth that changes. |
| `--tenth` | `#0A1420` | Tenth dip: stage 4, reserved ceilings — the footer (§6.10), the signature garment's final story state (§6.6), declared master pieces only | ~16% of pixels | Cloth on it 16.01:1 (AAA) — the most legible ground on the page; depth here is clarity, not gloom. A section may not declare a stage-4 ceiling without a reason stated in the batch record (§6.17). |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--dip-1` | `#C9D1BD` | Cloth mixed 35% toward fresh-dip green: stage 1's resting ground — a first dip's blue is weak and the green still shows through the cloth. Ink on it **9.46:1** (AAA); first blue on it 5.21:1 (apparatus ≥12px only). |
| `--cloth-dim` | `#BCBCBA` | Cloth mixed 25% toward vat deep: secondary text and captions on vat-deep and tenth-dip grounds only — **7.83:1** on vat, **9.74:1** on tenth. On first blue it drops to 4.31:1 and is refused there; stage-2 grounds take secondary text in full cloth at 85% opacity instead. |
| `--pale-dip` | `#B9BFBF` | Cloth mixed 30% toward first blue: apparatus and data on vat and tenth grounds — **7.99:1** on vat, **9.94:1** on tenth. The dyer's chalk: figures lettered on deep grounds. |
| `--green-pale` | `#98B091` | Fresh-dip green mixed 25% toward cloth: the transit colour's readable form on deep grounds — **6.35:1** on vat, **7.90:1** on tenth. Used for the oxidation flash in the margin swatch (§6.4) and dip confirmations on dipped surfaces. On cloth it is 2.03:1 — refused there. |
| `--thread` | vat deep at 55% over cloth (≈`#798189` effective) | The drying line itself, pegs, stitch rules and hairlines on pale grounds. Line-work only, never text; on blue grounds the line is cloth at 40%. |
| `--cloth-lamp` | `#DDDAD3` | Cloth mixed 10% toward vat deep: stage 0's ground under the dark-scheme ruling below. Ink on it **10.67:1** (AAA). |

**Dark-mode behaviour: the theme does not invert — the vat room is
already dark at the bottom of the page.** The page *is* a descent
from pale cloth to the tenth dip; there is no light scheme to flip
to. Under `prefers-color-scheme: dark`, only the undyed surfaces
change: stage 0 grounds are read as **cloth by lamplight** —
`--cloth-lamp` (`#DDDAD3`) replaces `--cloth` as the stage-0 ground
and ink holds at 10.67:1. Stages 1–4 are unchanged (a dipped piece
does not care about the room's light), the vat band is unchanged,
and text on blue grounds stays `--cloth` at full value — lamplight
dims the undyed, never the dyed. A build that darkens the blues
further or inverts cloth text onto the tint has misunderstood the
room: the dyer works at night by keeping the pale cloth visible, not
by deepening the vat.

**Pairing law.** Text is ink on stages 0–1, cloth on stages 2–4;
secondary text is cloth-dim on stages 3–4 only, full cloth elsewhere;
apparatus on deep grounds is pale-dip; green and green-pale are never
text on pale grounds; no blue letters a deeper blue. Any other
pairing is a build error, not a variation.

## 3. Typography

Two typefaces, inherited unchanged. **Shippori Mincho** is the cloth
voice — a Japanese Mincho whose strokes carry the same hand-finished
taper as a dyer's lettering brush — and sets display, headings,
garment names and the oxidising word (§6.2). **Zen Kaku Gothic New**
is the record voice and sets body text, captions, counters and all
prose. Data (dip counts, yardage, days) is set in Zen Kaku Gothic New
with `font-variant-numeric: tabular-nums`, never in Mincho: the
dyer's figures are tallied in the record hand, not brushed. There is
no third typeface. Emphasis inside Mincho is weight (500→800);
emphasis inside Gothic is weight (500→700), never italic — Gothic's
voice in this theme does not lean.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display / hero headline | Shippori Mincho 800 | 52–84px / 1.04, `clamp(3.25rem, 7vw, 5.25rem)` | +0.01em | Printed on the raised hero cloth (§6.12); its mask is the cloth's top edge. Never more than 3 lines; the oxidising word (§6.2) is set inside it, never as a separate banner. |
| Section title (piece name) | Shippori Mincho 700 | 34–52px / 1.08, `clamp(2.125rem, 4.5vw, 3.25rem)` | +0.01em | The piece's name as the dyer gives it: the cloth, then its count — "The Apprentice Shirt — Nine Dips". Set in the section's locked stage pairing (§2) at every stage. |
| Garment / product name | Shippori Mincho 700 | 22–28px / 1.18 | 0 | Name only; the dip record rides beneath it in apparatus, never inside the name. |
| Heading (in-section) | Shippori Mincho 700 | 24–30px / 1.15 | 0 | One per cloth region; headings do not cross a stage boundary — a heading is printed on one piece. |
| Body | Zen Kaku Gothic New 400 | 16.5–18px / 1.7 | 0 | Measure 56–64ch. On stage-2 grounds, 17px minimum — the 7.09:1 pairing earns AAA at size, not below it. |
| Caption / record | Zen Kaku Gothic New 400 | 14–15px / 1.55 | 0 | The batch record's voice (§6.17): what the piece is, how many dips, how many days, which vat. |
| Apparatus (dip counts, stages, labels) | Zen Kaku Gothic New 700 | 11–13px, uppercase | +0.16em | Dip counters ("9 DIPS"), stage names ("SECOND DIP"), swatch tallies. Uppercase is rationed to apparatus only. |
| Price | Shippori Mincho 800 | 30–40px / 1.05 | 0 | Set in the card's locked stage pairing; a price is lettered on the cloth it buys, never floated on a badge. |
| The confession line | Zen Kaku Gothic New 500 | 15–17px / 1.6 | 0 | The footer's sentence (§6.10) and the batch record's totals — the theme's honesty is set in the record voice, sentence case, unhurried. |

**Type laws.**

1. **The count rides with the name.** Every garment, product and
   section title that has a dip record carries it in apparatus
   directly beneath the name — name, then count, then prose. A title
   that celebrates a piece before stating its dips has skipped the
   dyeing.
2. **Type never changes colour on its own schedule.** Text colour is
   a property of the surface's stage (§2's locked pairings) and
   changes only when the surface's stage changes, on the same
   timeline (§6.3). A heading that "pops" to an accent colour is a
   build error; there is no accent colour.
3. **The deeper the stage, the slower the reading.** Line-height
   grows with stage: stage 0 body 1.62, stage 1 1.66, stage 2 1.7,
   stage 3 1.74, stage 4 1.78. Dyed cloth is heavier; the type
   admits it.
4. **Figures are tallies.** Any number the page asserts (dips, days,
   metres, price) is set tabular and is subject to the one law (§1):
   counted from a real event or traceable to the batch record.
   Percentages are banned from the theme — a dip is counted, not
   proportioned.
5. **The green word is the only kinetic type.** Exactly one word per
   page may oxidise letter by letter (§6.2), and it is always the
   hero's key word. A second oxidising word anywhere is a gate
   failure — the chemistry is rationed to the word that names it.

## 4. Layout language

**The section is a cloth piece, and pieces hang on a line.** The
page's spine is the **drying line**: a horizontal rule — `--thread`
on pale grounds, cloth at 40% on deep ones — from which each section
hangs by its head. A piece's top edge carries two peg marks (small
vertical ticks, 14px, at 24px and at the piece's width −24px) where
it meets the line; the line runs continuously down the page's left
margin as a vertical rail on ≥1200px, turning horizontal at each
piece's head. Pieces are full-bleed bands in DOM order — the line's
order is the reading order is the dip order — and a screen reader
walks the same line. Reordering pieces for visual variety is
forbidden; the line is strung once, at the survey (§15, step 1).

**The vat anchors the hero.** The hero is two grounds in one screen:
undyed cloth above, and at its bottom edge a **vat band** — vat deep
(`--vat`), 180–260px tall, full-bleed — into which the first dip
(§6.1) is performed. The band is not a footer for the hero or a
divider; it is the liquid the page's first piece comes out of, and
its surface line (the band's top edge, a 2px cloth-at-25% meniscus
rule) is the most important horizontal on the page: everything above
it is air, everything below it is dye. The vat band appears once, in
the hero. Later sections dip into a vat the page no longer needs to
show — the chemistry has been taught.

**The margin is the dyer's bench.** On ≥1200px, the left 104px of
the page is the bench: it holds the line's vertical rail, the margin
swatch (§6.4) pinned at reading height, and stage labels rotated
−90° at each piece's head. Content begins at 104px and reads in a
1120px-max column. The bench holds instruments only; no prose, no
imagery, no advertising may sit on it. Below 1200px the bench folds
away and its instruments relocate per §6.4/§6.11's breakpoint rules —
the swatch becomes a chip in the navigation bar, the rail is cut.

**Hanging geometry.** A piece hangs with air around it: minimum 56px
of page ground above its line and 72px below its hem at ≥1200px
(40px/48px below). Pieces never overlap and never share a line —
two pieces on one line is a washing-day photograph, not this theme.
Corner radius is 0 everywhere except the swatch (§6.4), whose corners
are the cloth's own softness (2px), and image frames (§6.13), which
are woven, not rounded: a 3px double rule in the frame's stage
pairing. Dyed cloth is cut square; nothing in the dye house is a
pill.

**Density law.** Density falls as the page descends, because the
visitor's attention is being dyed, not spent. The hero holds one
piece and the vat. Product pieces (§6.13) may run three-across —
cloth for sale is allowed to be plentiful. The garment (§6.6) is
alone on its line for its whole pinned passage. The craft section
(§6.7) is one pattern, drawn large. The footer (§6.10) holds the
confession and the record's totals, nothing else. A page whose
footer is as busy as its product grid has hung its washing over its
ledger.

**Stage ceilings are declared, never ambient.** Each piece declares
its ceiling in the survey (§15, step 1): most pieces ceiling at
stage 3; product cards ceiling at stage 2 (a card dyed to the tenth
dip could no longer be told from the footer); the garment alone
travels to stage 4, and only at its story's end (§6.6); the footer
*rests* at stage 4 by construction (§6.10). A piece's ceiling is a
fact about the content — how much returning it can bear — and is
recorded in the batch record (§6.17) beside its dip counts.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-dip` | `cubic-bezier(.55,.06,.35,1)` | The lowering: gravity takes the cloth, easing as it meets the liquid | First dip (§6.1), hover dip's fall (§6.8), skeleton cloth (§6.15) |
| `--ease-raise` | `cubic-bezier(.3,.65,.25,1)` | The wet lift: heavy at the start, water shedding, a clean arrive | First dip's rise (§6.1), click dip's settle (§6.9), line-pass transition (§6.15) |
| `--ease-oxidise` | `cubic-bezier(.45,0,.55,1)` | The chemical turn: an even, unhurried colour ramp with no overshoot — chemistry does not bounce | All stage changes (§6.3), the oxidising word (§6.2), garment beats (§6.6) |
| `--ease-sway` | `cubic-bezier(.25,.9,.3,1)` | Cloth settling on the line: one decaying sway, then stillness | Pieces hung on entry (§6.11/§6.13), swatch (§6.4) |
| `--ease-stitch` | `cubic-bezier(.4,0,.3,1)` | The needle's draw: steady pull, firm stop | Shibori draw (§6.7), stitch rules, batch record's line (§6.17) |

**The dip timeline (the theme's master clock).** Every full dip —
the first dip (§6.1), a re-dip (§6.3), a click dip (§6.9) — runs the
same four beats at element-specific durations: **immerse** (the
surface takes the green: colour moves to fresh-dip green across the
piece), **dwell** (a held breath at green — the vat is working),
**oxidise** (green ramps to the target stage's resting colour on
`--ease-oxidise`), **rest** (the stage's locked text pairing is fully
in force). No element invents a private colour path: a dip is a dip,
at 2400ms in the hero and at 1450ms in a section, and the visitor
learns the rhythm once and reads it everywhere.

**The transit rule.** Full green (`--green`) exists only inside the
immerse–oxidise window. During that window the surface's text is set
in vat-deep ink (4.81:1 on full green) or tenth-dip (5.98:1) — the
only pairings licensed over green — and crossfades to the target
stage's locked pairing across the oxidise beat, flipping at the
interpolation midpoint where the build's contrast audit (§10, gate
5) has verified both pairings at ≥4.5:1. Text is never set in cloth
over green (2.68:1) at any frame of any dip.

**Every motion term, translated into the dye house's language:**

- **Scroll-triggered reveals** are hangings: a piece entering the
  viewport is hung on its line — it drops the last 14px into place
  and sways once (§6.11/§6.13). Nothing fades up out of nowhere; on
  this page things are *hung*, and hanging has a line and two pegs.
- **Scroll scrub** is the dip story: the garment's stages (§6.6), the
  swatch's darkening (§6.4) and the shibori's drawing (§6.7) are pure
  functions of scroll position, driven by the shared loop.
- **Parallax** is the vat's depth: exactly one parallax pair exists —
  the hero vat band drifts behind the raised cloth (§6.12). The
  liquid is deep and the cloth is at its surface; nothing else on the
  page pretends to be at two depths.
- **Pinned scenes:** exactly one — the signature garment (§6.6). A
  dye house has one piece on the line long enough to tell its life;
  pinning a second piece is refused.
- **Masked reveals** are the cloth's own edges: the hero headline is
  masked by the raised cloth's top edge (§6.12) — the print appears
  as the cloth rises because the cloth *is* the mask.
- **Blur-to-sharp is refused.** Wet cloth is heavy and dark, never
  blurry; a piece is undyed, transiting, or dyed. Blur is a lens
  effect and there is no lens at the vat.
- **Kinetic typography** is refused except the oxidising word
  (§6.2): one word, colour only, no letter moves. Type does not
  perform; it undergoes.
- **Counters** are the dyer's figures (§6.16): dip counts and
  yardage count when their piece is hung, tabular, stepped like a
  tally being chalked — and every figure obeys the one law.
- **Progress** is the margin swatch (§6.4): a piece of cloth
  darkening one dip per completed section, with a stitched tally
  beneath it. There is no progress bar; there is a swatch.
- **Marquee is refused.** Cloth on a line does not run sideways
  forever. The line is still; the air moves the pieces, slightly,
  and only when they are first hung.
- **Ambient loops:** exactly one — the dye motes (§6.5), inside the
  vat band only, and it is the first thing cut by the performance
  ladder (§14). A second ambient loop anywhere is a gate failure.
- **Micro-interactions:** the hover dip (§6.8), the click dip
  (§6.9), the stitch press (§6.14's submit). Every interaction is an
  immersion or a stitch.
- **Hover physics:** no magnetic pull, no tilt stages. Cloth under a
  hand is dipped (§6.8); cloth does not lean toward the visitor.
- **Page transitions** are a line pass (§6.15): a fresh piece is
  raised across the viewport on the line, and the new page hangs
  beneath it.
- **Smooth scrolling:** wet and heavy. The shared loop lerps
  scroll-driven values at `--lerp` 0.09 — the slowest lerp in the
  library, because wet cloth drags — and native scroll is never
  hijacked: the theme smooths its instruments, not the visitor's
  hand.
- **The shared loop law.** One `requestAnimationFrame` loop owns
  every scrubbed value (garment stages, swatch, shibori draw, vat
  parallax). Lerp 0.09 for colour-bearing values, 0.14 for the
  motes' drift phase. Elements that can be pure CSS (hanging sway,
  oxidation ramps) are; the loop writes only transform, opacity and
  custom properties, and stops writing a value when it settles
  within 0.1% of target.

**Watchdog law.** Every dip has a timer: if a stage change's
observer or the loop fails, the surface is set instantly to its
target stage by 1600ms after the trigger (§6.3). The DOM ships at
each piece's declared *resting* state (stage 0 for sections, the
record state for products, stage 4 for the footer); every transit
state exists only under a JS-armed root class. No-JS is not a
degraded mode — it is the dye house with the day's dipping already
done and the cloth hung dry.

## 6. Signature elements

### 6.1 The first dip

- **What & why.** On load, a white cloth panel lowers into the hero's
  vat band, pauses, and rises green — then oxidises to first blue in
  real time while the visitor watches. It belongs because it is the
  product's making performed once, at the door: before the site asks
  for anything, it shows the visitor the exact chemistry every later
  element will repeat at smaller scales. The raised, oxidised cloth
  then *becomes* the hero's surface — the headline is printed on it
  (§6.12) — so the ceremony is not an intro animation bolted onto the
  hero; it is the hero being manufactured.
- **Structure.** A `<div class="first-cloth">` inside the hero,
  sized to the hero's cloth panel (full column width, 46–54vh),
  initially translated above the vat band's surface line, clipped by
  the hero's overflow. The panel is real DOM carrying the hero's
  headline, standfirst and primary action in final position; the vat
  band (§4) is a sibling beneath it. The panel ships at rest — raised,
  stage 2, headline printed — and JS arms the lowered, undyed
  pre-state only after first paint confirms the loop is alive.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 700ms timer — the dip must not wait for a slow font
  to start the chemistry. t=0: the undyed panel lowers 100% of the
  band's depth over 900ms `--ease-dip`. Dwell: 250ms held at depth
  (the panel's lower 60% submerged; a 2px meniscus line rides its
  surface). Rise: 750ms `--ease-raise`, the panel emerging already
  green — the colour change happens *in* the vat, so the first
  visible frame of the rise is full fresh-dip green. Oxidise: begins
  at rise +150ms and runs 1500ms `--ease-oxidise`, green → first
  blue; the headline prints across the same window (§6.12). Total
  ceremony ≈2.65s; a click, a keypress or the first scroll completes
  it instantly to the resting state. It runs once per session and
  never replays — a returning visitor finds the cloth already dyed.
- **States.** Undyed (pre-dip, JS-armed only) → immersing → dwelling
  → rising green → oxidising → rested at stage 2, headline printed.
  Scrolled-past during the ceremony: the ceremony completes instantly
  (the visitor who leaves mid-dip returns to dyed cloth, not to a
  paused performance).
- **Content merge.** The panel is the hero: its headline, standfirst
  and action are the site's first content, printed on the cloth the
  ceremony produces. Remove the animation and the hero loses nothing
  but the making; keep it and the hero's surface has a provenance no
  static hero can claim.
- **Failure fallback.** Watchdog: if the panel has not reached rest
  by 3000ms after the trigger, it is set to rest instantly — classes
  removed, stage 2 applied. No JS: the panel stands raised and dyed
  at first paint. If fonts fail, the 700ms race starts the dip in a
  fallback face; the panel's fixed height absorbs letterfit shift.
- **Reduced-motion variant.** No dip. The panel stands at stage 2
  with the headline printed; a single apparatus line beneath the
  standfirst records the fact the ceremony would have shown: "FIRST
  DIP — GREEN FROM THE VAT, BLUE IN THE AIR." The information is
  kept; only the theatre rests.
- **Performance budget & mobile variant.** One transformed panel +
  one colour ramp; no images, no canvas. Mobile (<768px): the panel
  is 38vh, lowering shortens to 700ms, oxidise to 1200ms, and the
  meniscus line is cut — a phone's vat is shallower and the ceremony
  admits it rather than lagging behind the thumb.
- **Choreography timeline (v2).** t=0 fonts ready (or 700ms race
  lost) → t=0–900 lowering → t=900–1150 dwell, meniscus settles →
  t=1150–1900 rise, panel green from its first visible frame →
  t=1300–2800 oxidise ramp runs (overlapping the rise's tail) →
  t≈1900 headline fully printed (§6.12's mask completes with the
  rise) → t=2800 panel at rest, stage 2 → the oxidising word (§6.2)
  begins its letters at t=2850.
- **State matrix (v2).** *Rest:* raised panel, stage 2, headline
  printed. *Hover:* none — the ceremony is not a control; the hero's
  action inside it hovers per §11. *Focus:* focus entering the hero
  during the ceremony completes it instantly (a keyboard visitor is
  never asked to wait for cloth). *Active:* n/a. *Scrolled-past:*
  completed instantly, rested. *Disabled / no-JS:* rested at first
  paint. *Touch:* identical; the first touch completes the ceremony
  like a click.
- **Breakpoints (v2).** ≥1200px: panel 46–54vh, full timeline.
  768–1199px: panel 42vh, oxidise 1350ms. <768px: panel 38vh,
  lowering 700ms, oxidise 1200ms, meniscus cut, total ≤2.2s.
- **Edge cases & failure modes (v2).** *Slow network / fonts late:*
  the 700ms race governs; the dip never waits past it. *Tab hidden
  mid-ceremony:* rAF pauses; on return, if elapsed wall-time exceeds
  3000ms the watchdog rests the panel — the visitor never resumes a
  half-dipped hero. *Session return:* `sessionStorage` marks the dip
  done; the panel paints at rest. *Hero shorter than the band:* the
  lowering distance is the band's rendered depth, measured at
  trigger time, never a hard-coded pixel count.
- **Accessibility spec (v2).** The panel's content is in the
  accessibility tree at all times — the ceremony is visual only and
  never removes or reorders content. The dip is never announced. The
  headline is the page's `<h1>` from first paint. During the transit
  window the headline is set in vat-deep ink over green (4.81:1,
  §5's transit rule) and crossfades to cloth as oxidation completes
  (7.09:1 at rest). Focus is never moved by the ceremony.
- **Tokens consumed (v2).** `--cloth`, `--green`, `--blue`, `--vat`,
  `--ease-dip`, `--ease-raise`, `--ease-oxidise`, `--dur-lower`
  (900ms), `--dur-dwell` (250ms), `--dur-oxidise-hero` (1500ms),
  `--dur-fallback-hero` (3000ms).

### 6.2 The oxidising word

- **What & why.** Inside the hero headline, one key word — the word
  that names the chemistry, typically "indigo" itself — oxidises
  green→blue letter by letter after the cloth rises. It belongs
  because it makes the type undergo the process the page sells: the
  word for the dye is itself dyed, in the air, at reading speed. It
  is the theme's smallest complete dip and its signature in
  miniature; visitors who see nothing else of the motion system have
  seen this, and they understand the whole site from it.
- **Structure.** The word is a `<span class="oxidising-word">` inside
  the `<h1>`, its letters wrapped in per-letter spans by JS only
  (the no-JS word is one unbroken span in the headline's ink). Each
  letter carries a `--letter-progress` custom property written by a
  CSS transition, interpolating its colour from `--green` to the
  headline's resting colour along the stage path (green → first
  blue → the cloth pairing of the hero panel's stage 2, where the
  word finally rests slightly deeper than its neighbours: it ends at
  `--vat`-weighted blue so the eye can find which word turned).
- **Motion spec.** Trigger: the first dip's rest (t=2850 in §6.1's
  timeline), or 400ms after the hero enters if the ceremony was
  skipped/completed instantly. Each letter crossfades over 300ms
  `--ease-oxidise`, staggered 90ms letter to letter, left to right —
  the direction of reading is the direction of the turn. A six-letter
  word completes in 300 + 5×90 = 750ms. Runs once per session. Words
  longer than 9 letters are refused at build time: the stagger would
  outlast the headline's welcome, and the dyer chooses a shorter word
  ("indigo", "dyed", "blue") rather than a slower chemistry.
- **States.** Green (armed, pre-trigger) → oxidising (letters mid-
  ramp, each at its own point on the path) → blue (rest, permanent
  for the session). Hover/focus on the headline: no effect — the
  word does not re-turn for attention. Scrolled-past mid-ramp: the
  ramp completes on its CSS timeline regardless of scroll; it is
  750ms and owes nothing to the viewport.
- **Content merge.** The word is not a decoration near the headline;
  it is a word *in* the headline, chosen because the sentence means
  it — "Cloth, dipped in **indigo**" — and its turning is the
  sentence's verb performed. A build whose oxidising word could be
  swapped for any other word without loss has chosen the wrong word.
- **Failure fallback.** No JS: the word stands in the headline's
  resting colour, indistinguishable and complete. Watchdog: any
  letter not at rest by trigger +2000ms is set to rest. If the hero
  ceremony was watchdog-rested, the word rests too — the word never
  performs alone for a visitor who missed the dip.
- **Reduced-motion variant.** The word rests at its final blue from
  first paint. The apparatus line §6.1 adds in this mode ("FIRST DIP
  — GREEN FROM THE VAT, BLUE IN THE AIR") is the word's turning,
  stated instead of shown.
- **Performance budget & mobile variant.** ≤9 letter colour
  transitions, compositor-friendly (colour only, no layout). Mobile:
  identical — the word is the same size class as the headline and
  costs nothing extra; the stagger tightens to 70ms under 768px so
  the turn keeps pace with the smaller ceremony.
- **Choreography timeline (v2).** t=0 trigger (hero rested) → t=0
  letter 1 begins its 300ms ramp → t=90 letter 2 → … → t=(n−1)×90
  last letter begins → t=(n−1)×90+300 word at rest → the hero's
  standfirst, already printed, is joined by the apparatus count
  (§6.16) if the hero carries one.
- **State matrix (v2).** *Rest (before trigger):* word green only
  under the JS-armed class; unarmed DOM is final blue. *Hover:*
  none. *Focus:* none (the word is not focusable). *Active:* n/a.
  *Scrolled-past:* ramp completes off-screen; returning shows the
  blue word. *Disabled:* n/a. *Touch:* identical; no touch state.
- **Breakpoints (v2).** ≥1200px: stagger 90ms. 768–1199px: 80ms.
  <768px: 70ms. Letter count cap (9) is breakpoint-independent.
- **Edge cases & failure modes (v2).** *Word wraps across lines:*
  the oxidising word must fit one line at every breakpoint — checked
  at build; if it wraps, the headline is re-set with the word earlier
  in the line, never allowed to turn across a break. *Right-to-left
  locales:* the stagger follows reading direction (letters turn in
  DOM order, which the build sets to reading order). *Session
  return:* word paints blue; the session flag is §6.1's.
- **Accessibility spec (v2).** The word is exposed to assistive tech
  as one word — the letter spans are `aria-hidden` and the word
  itself carries an `aria-label` with its full text, so no reader
  ever spells it. The colour change is never announced. Contrast:
  during each letter's ramp its pairing follows §5's transit rule
  (ink-weighted path on the panel's stage-2 ground, verified ≥4.5:1
  at the flip point, §10 gate 5); at rest the word measures 7.09:1+
  against the panel.
- **Tokens consumed (v2).** `--green`, `--blue`, `--vat`, `--cloth`,
  `--ease-oxidise`, `--dur-letter` (300ms), `--stagger-letter`
  (90ms).

### 6.3 Stateful re-dipping

- **What & why.** Each section deepens exactly one stage (§2's
  ladder) each time it re-enters the viewport, per session, up to its
  declared ceiling. It belongs because it is the theme's thesis made
  mechanical: in real dyeing, depth is repetition — no single dip
  makes a dark cloth — and here the visitor's own returning is the
  repetition. A section you have read three times is literally darker
  than one you skimmed past, and the page's colour map at any moment
  is a true picture of the reading so far. This is the element the
  whole theme exists to make possible; the first dip (§6.1) teaches
  it, the swatch (§6.4) tallies it, the footer (§6.10) confesses it.
- **Structure.** Each `<section class="piece" data-stage="0"
  data-ceiling="3">` carries its stage as a data attribute; stage
  classes (`.stage-0`…`.stage-4`) set the ground and the locked text
  pairing from §2's tokens — no inline colours anywhere. An
  `IntersectionObserver` with a 40% visibility threshold and a
  full-exit requirement arms the next dip: a piece must leave the
  viewport completely (0% visible) and re-enter to ≥40% before a dip
  fires. Stage state lives in a per-session map keyed by piece id;
  nothing persists beyond the session (the cloth is washed between
  visits — a returning day starts undyed, which is also the honest
  state of a new reading).
- **Motion spec.** Trigger: re-entry per the arming rule above. The
  dip runs §5's master timeline at section scale: immerse 300ms (the
  ground moves toward green — visibly a *tint* path, since the piece
  is large: the colour interpolates through the green-weighted
  midpoint of the two stages), dwell 150ms, oxidise 1000ms
  `--ease-oxidise` to the next resting stage; total 1450ms. Text
  colour crossfades on the oxidise beat per the transit rule (§5).
  One dip per piece at a time; a piece that exits and re-enters
  mid-dip finishes its current dip first — the queue is one deep,
  because cloth already in the air is not re-immersed.
- **States.** At stage (rest, locked pairing) → armed (fully exited)
  → dipping (1450ms) → at next stage (rest, permanent for the
  session). At ceiling: re-entries are no-ops — the piece is as dark
  as its record allows and the observer unobserves it. Focus entering
  a piece never triggers a dip (focus is navigation, not immersion).
- **Content merge.** The stage *is* the content's state: a section's
  ground, its headings, its apparatus all take the stage's pairing
  together, and the piece's printed stage label ("SECOND DIP" in its
  head apparatus) updates with it — the colour and the caption are
  two printings of one count. Nothing about the content is hidden,
  moved or re-ordered by a dip; only its depth changes.
- **Failure fallback.** Watchdog: a dip not completed by 1600ms after
  trigger is set instantly to its target stage. No JS: every piece
  rests at stage 0 (its shipped state) and reads completely. Loop
  killed mid-session: stages freeze where they are; every piece
  remains at a locked pairing, so the page is never caught between
  colours.
- **Reduced-motion variant.** Stage changes apply instantly (no
  immerse, no oxidise ramp) — the record still deepens, because the
  deepening is information, but it changes the way a printed number
  changes: at once, without theatre. The stage label still updates.
- **Performance budget & mobile variant.** One observer, stage
  classes only; a dip animates background-color and color on one
  section — no layout, no paint of children beyond colour. Mobile:
  identical mechanics; the visibility threshold drops to 30% (phone
  viewports are tall relative to pieces) and oxidise shortens to
  850ms so a fast thumb is not chasing its own dyeing.
- **Choreography timeline (v2).** t=0 piece re-enters ≥40% while
  armed → t=0–300 immerse (ground toward the green midpoint) →
  t=300–450 dwell → t=450–1450 oxidise to next stage, text pairing
  flipping at the verified midpoint → t=1450 rest at new stage,
  stage label updates, swatch tally (§6.4) checks the piece's
  completion state → piece must fully exit before it can arm again.
- **State matrix (v2).** *Rest:* current stage, locked pairing.
  *Hover:* none at section level (cards inside dip per §6.8).
  *Focus:* no dip; focus ring per §11. *Active:* n/a.
  *Scrolled-past:* the exit arms the next dip; the piece keeps its
  stage. *Disabled:* at ceiling — observer released, stage fixed.
  *Touch:* identical arming; touch scroll is still scrolling.
- **Breakpoints (v2).** ≥1200px: threshold 40%, oxidise 1000ms.
  768–1199px: threshold 35%, oxidise 950ms. <768px: threshold 30%,
  oxidise 850ms, immerse 250ms.
- **Edge cases & failure modes (v2).** *Piece taller than the
  viewport:* it can never reach 40% of *itself* — the threshold is
  40% of the *viewport's* coverage of the piece's first viewport-
  height, so tall pieces arm and dip on the same rule as short ones;
  a build that thresholds on the piece's own height strands tall
  pieces at stage 0 forever. *Fast fling down and back:* pieces
  passed without a full exit + 40% re-entry do not dip — a fling is
  not a reading and the ladder does not reward it. *Anchor jump into
  a piece:* arrival counts as entry, not re-entry; no dip. *Resize
  mid-dip:* the ramp is colour-only and completes unaffected.
  *Stage label vs colour disagreement:* impossible by construction —
  both are written from the same stage write; §10 gate 3 verifies by
  reading a piece at every stage.
- **Accessibility spec (v2).** Stage changes are never announced
  (they are ambient state, like a visited link's colour — which is
  exactly the model: the stage is a visited-state made honest).
  Every stage's pairing is AAA or AA-large per §2's table, verified
  at rest; the transit window follows §5. The stage label is real
  text in the piece's head, so the state is available non-visually
  to anyone who looks for it. Focus order never changes with stage.
- **Tokens consumed (v2).** `--cloth`, `--dip-1`, `--blue`, `--vat`,
  `--tenth` (ceilings), `--green` (transit), `--ease-oxidise`,
  `--dur-immerse` (300ms), `--dur-dwell-section` (150ms),
  `--dur-oxidise-section` (1000ms), `--dur-fallback-dip` (1600ms).

### 6.4 The margin swatch

- **What & why.** A small cloth swatch pinned on the margin bench
  (§4) darkens one dip per completed section, with a stitched tally
  beneath it ("4 / 9"). It belongs because reading progress in this
  theme cannot be a bar — nothing in a dye house fills left to
  right — so progress is a piece of the product being made alongside
  the reading: as you finish sections, a swatch dyes. It is the
  margin instrument that makes §6.3's distributed state legible at a
  glance, and the only progress indicator the theme permits.
- **Structure.** A `<figure class="swatch">` pinned (sticky) in the
  bench at reading height: a 56×72px cloth rectangle with a woven
  double-rule frame, one stitched top edge (a dashed 2px rule — the
  stitch that pins it), and a `<figcaption>` tally in apparatus:
  dipped count over total sections, plus the current stage name
  ("THIRD DIP"). The swatch's stages are §2's ladder, driven by a
  count of *completed* sections — a section completes when its lower
  edge passes 60% of viewport height (read, not merely entered).
  Sections and swatch dips are counted from the same session map as
  §6.3; the swatch is that map's margin printing.
- **Motion spec.** Trigger: a section completing. The swatch dips on
  §5's timeline at instrument scale: immerse 200ms, oxidise 700ms
  `--ease-oxidise` to its new stage, with a 120ms `--ease-sway`
  settle as if the pin took the weight. The tally's numeral updates
  at the oxidise midpoint. The swatch's ceiling is stage 4 regardless
  of section count — nine sections completed still lands the swatch
  at the tenth dip, because the tally, not the shade, carries the
  exact count. Between completions the swatch is still; it has no
  idle motion (the motes §6.5 are the theme's only ambient loop).
- **States.** At stage (rest) → dipping (900ms) → at next stage.
  Hover: the swatch lifts its caption to full opacity and shows the
  next section's name ("NEXT: THE CRAFT") — the instrument answers
  the only question a progress indicator is ever asked. Focus: the
  swatch is not focusable; its information is duplicated in the
  navigation (§6.11) for keyboard visitors.
- **Content merge.** The swatch is a piece of the site's own cloth,
  dyed by the reading — remove the reading and it stays undyed;
  finish the page and it is the darkest small object on the screen
  until the footer. It measures the visitor's work in the product's
  own units.
- **Failure fallback.** No JS: the swatch prints at stage 0 with the
  tally as "— / 9" replaced by the static text "NINE PIECES ON THE
  LINE" — the count of pieces, which is true without a session.
  Watchdog per §5: a swatch dip not settled by 1200ms is set to its
  stage instantly.
- **Reduced-motion variant.** The swatch changes stage instantly at
  each completion; the tally updates with it. The record deepens;
  the dipping is stated, not shown.
- **Performance budget & mobile variant.** One small element, colour
  transitions only. Mobile (<1200px): the bench is gone, so the
  swatch becomes a 28×36px chip in the navigation bar (§6.11) with
  the tally beside it — same stages, same count, pocket size; below
  768px the stage name is cut and the chip + tally alone ride the
  bar.
- **Choreography timeline (v2).** t=0 section's lower edge crosses
  60% line → t=0–200 swatch immerse → t=200–900 oxidise, tally
  numeral flips at t≈550 → t=900–1020 sway settle → rest at new
  stage. If two sections complete within one dip (a fast reader on a
  short page), the swatch queues one dip and jumps the tally by the
  true count — the shade may lag the tally by one dip, never the
  reverse.
- **State matrix (v2).** *Rest:* current stage, tally current.
  *Hover (≥1200px):* caption full opacity, next-section name shown.
  *Focus:* n/a (not focusable). *Active:* n/a. *Scrolled-past:*
  sticky — it does not scroll past; at the footer it unsticks and
  rests above the confession (§6.10), its work done. *Disabled:*
  n/a. *Touch:* no hover; the chip in the bar shows tally at all
  times.
- **Breakpoints (v2).** ≥1200px: full swatch on the bench, sticky at
  38% viewport height. 768–1199px: chip form in the navigation bar,
  28×36px, tally + stage name. <768px: chip + tally only.
- **Edge cases & failure modes (v2).** *Page with two sections:* the
  swatch still ladders (two completions = stage 2) — the ladder is
  per-completion, not per-fraction, so short pages dye honestly
  shallow swatches. *A section that can never complete* (taller than
  250vh): completion is measured on its final viewport-height — its
  lower edge is its end, whenever that arrives. *Footer reached
  without completing the last section:* the swatch rests one stage
  short and the confession (§6.10) counts only completed pieces —
  the two records agree because they read the same map.
- **Accessibility spec (v2).** The swatch is a figure with a real
  caption; the tally is text, not an image of numbers. Stage changes
  are not announced live (they would fire constantly); the current
  count is available whenever the visitor inspects the bench or the
  bar. Contrast: the tally sits on the page ground, never on the
  swatch itself, in the ground's locked pairing.
- **Tokens consumed (v2).** `--cloth`, `--dip-1`, `--blue`, `--vat`,
  `--tenth`, `--green-pale` (oxidation flash on deep stages),
  `--thread` (stitch rule), `--ease-oxidise`, `--ease-sway`,
  `--dur-oxidise-swatch` (700ms).

### 6.5 Dye motes

- **What & why.** Fine motes swirl slowly inside the hero vat band —
  two counter-rotating drifts of indigo particles suspended in the
  liquid. It belongs because the vat beneath the hero must read as a
  living liquid, not a colour block: a real indigo vat has a
  shimmering, flowering surface and depth you can sense but not see
  into. The motes are that depth cue, and they exist only inside the
  band — the theme's single licensed ambient loop (§5), rationed to
  the one place the liquid is actually shown.
- **Structure.** A `<canvas class="motes" aria-hidden="true">`
  filling the vat band, behind the band's surface line and any band
  content, drawing 26 particles (desktop) as 1.5–3px soft discs in
  `--pale-dip` and `--green-pale` at 18–38% opacity, moving on two
  slow circular drift fields rotating in opposite senses. Particle
  positions are computed in the shared loop from a phase value, not
  integrated per-particle — the field is a function of time, so a
  stalled frame can never scatter the vat. The band's ground is
  painted `--vat` in CSS beneath the canvas; the canvas adds only
  the suspension.
- **Motion spec.** Trigger: hero in viewport (the loop unobserves
  the band when it leaves — motes never drift off-screen). Drift
  period: 46s per full rotation of the outer field, 64s for the
  inner, opposite sense; individual motes also bob ±6px on a 9s
  sine. The motion is deliberately below the threshold of attention:
  a visitor who stares sees movement; a visitor who reads sees a
  living surface. No mote ever crosses the band's surface line into
  the cloth above — the liquid's contents stay in the liquid.
- **States.** Drifting (band in view) → suspended (band off-screen,
  tab hidden, or loop throttled: phases freeze, motes hold) →
  drifting. There is no hover, focus or active state; the vat does
  not respond to the hand — you do not stir a master's vat with a
  cursor.
- **Content merge.** The motes are the vat band's own substance: the
  same band the first dip (§6.1) enters. When the cloth lowers, it
  lowers *through* the mote field (the canvas sits above the band
  ground but below the panel's submerged portion's overlay tint), so
  the ceremony and the ambience are one liquid.
- **Failure fallback.** No canvas / no JS: the band is flat `--vat`,
  which is its printed state and loses nothing but the suspension.
  Canvas context failure: caught, canvas removed, band unchanged.
  The band's content (if any) never depends on the canvas.
- **Reduced-motion variant.** Motes are painted once, statically, at
  their phase-0 positions — the vat still reads as suspension, not
  flatness — and never move. If the build prefers, the static field
  may be a pre-rendered background; it may not simply vanish, because
  flat vat under reduced motion would make the band a different
  element in that mode.
- **Performance budget & mobile variant.** 26 particles, one canvas,
  ≤0.3ms/frame; the first item on §14's cut order. Mobile (<768px):
  12 motes, drift periods lengthened 1.4× (slower reads calmer on a
  small band), canvas resolution capped at 1.5× device pixel ratio.
- **Choreography timeline (v2).** Continuous: phase advances with
  the shared loop's clock; outer field completes a rotation at
  t=46s, inner at t=64s counter-rotating; bob cycle 9s. On band
  entry the field fades in over 600ms (opacity only) so the vat
  never pops into life; on exit it freezes rather than fading — a
  vat you cannot see is a vat at rest.
- **State matrix (v2).** *Rest (in view):* drifting. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* suspended, phase
  held. *Disabled:* static painted field (reduced motion) or flat
  band (no canvas). *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 26 motes, periods 46s/64s.
  768–1199px: 20 motes, periods 52s/72s. <768px: 12 motes, periods
  ×1.4, DPR cap 1.5.
- **Edge cases & failure modes (v2).** *Low-power device:* if the
  loop's frame budget (§14) is exceeded twice in a minute, the motes
  drop to the static field for the session — the vat calms itself
  rather than taxing the visitor. *Band resized:* the field is
  computed from the band's current box each frame; resize cannot
  strand a mote outside the liquid. *Hero without a vat band*
  (interior pages): the element does not exist there — §7 forbids
  importing the band, and therefore the motes, off the home hero.
- **Accessibility spec (v2).** `aria-hidden`, no text, no meaning
  carried. The motion is exempt from the flash rules by amplitude
  (opacity ≤38%, no luminance oscillation above 3/second — the
  fastest bob is 9s). Under reduced motion the field is static per
  the variant above.
- **Tokens consumed (v2).** `--vat`, `--pale-dip`, `--green-pale`,
  `--mote-count` (26), `--dur-drift-outer` (46s), `--dur-drift-inner`
  (64s), `--lerp-motes` (0.14).

### 6.6 The garment pin & dip story

- **What & why.** The signature garment pins on its line while its
  dip-count story scrolls beside it; each story beat deepens the
  pinned garment's image one stage, in sync. It belongs because it
  is the theme's biography form: a real master garment's value *is*
  its history — dipped, dried, dipped again across days — and the
  pin lets the visitor read that history at the speed of the making
  while the garment itself accumulates the colour in front of them.
  The photograph is dipped by its own biography as you read it; no
  other element in the library ties an image's state this directly
  to its text.
- **Structure.** A pinned region of 320vh (desktop): the garment's
  figure — a real product photograph inside a woven frame (§4) with
  a stage-tinted overlay whose colour is a pure function of the
  story's progress — sticks at viewport centre-left; beside it, the
  story column carries 4–5 beats, each a dated entry in the record
  voice ("Day one — first dip. The cloth came up green and the vat
  was judged alive." … "Day three — ninth dip. Hung to cure."). The
  overlay's stage steps are discrete (stage per beat), crossfaded on
  `--ease-oxidise`; the underlying photograph never changes, because
  the garment in the photograph is one garment at one moment — the
  *frame's* tint carries the count, and the caption states the beat's
  stage in apparatus so the tint is never the only record.
- **Motion spec.** Trigger: scroll through the pinned region,
  scrubbed by the shared loop (lerp 0.09). Progress q = region
  scroll fraction; beat boundaries at q = 0.18 / 0.38 / 0.58 / 0.78
  (for five beats). At each boundary the frame tint crossfades
  900ms `--ease-oxidise` to the beat's stage, the beat's entry
  inks from 55% to full pairing, and the garment's printed counter
  (§6.16) steps to the beat's true count (1, 3, 5, 7, 9 dips in the
  reference story — the real garment's record, §6.17). The final
  beat lands the garment at stage 4 — the page's only travelling
  stage-4 surface — and the pin releases 40vh after the last beat so
  the visitor leaves with the finished piece.
- **States.** Approaching (garment hung, stage 0 tint) → pinned,
  beats advancing → finished (stage 4, counter at record) →
  released. Scrolled back up: the story re-runs in reverse — the
  tint lightens beat by beat — because a pin is a reading position,
  not a session record (contrast §6.3, whose stages are session
  state and never reverse). The distinction is the theme's grammar:
  *stories* re-tell; *dyeings* persist.
- **Content merge.** The beats are the garment's real production
  record — dates, dips, the dyer's judgements — and the tint is that
  record's sum at the reader's position. The buy action for the
  garment sits after the pin, at the story's end: you may not
  purchase the piece before you have read how it was made, which is
  the maker's actual sales philosophy set in layout.
- **Failure fallback.** No JS / no pin support: the garment and its
  beats lay out as an ordinary section, the frame at its final
  stage-4 tint, the counter at its record value, every beat fully
  inked. Watchdog: if the loop stalls inside the pin, the tint is
  set to the stage of the beat nearest the current scroll position
  within 1200ms — the story may lose its smoothness, never its
  position.
- **Reduced-motion variant.** No pin. The garment appears once,
  above its beats laid out in order, at stage 4 with the full
  record printed; each beat carries its stage label. The biography
  is read as a ledger — the same facts, filed instead of performed.
- **Performance budget & mobile variant.** One sticky figure, one
  colour crossfade at a time; the photograph is a single image
  (≤180KB). Mobile (<768px): **the pin is cut** — a phone's viewport
  is too short to hold a garment and its story side by side, so the
  beats stack beneath the garment and the tint steps as each beat
  crosses 55% viewport height (observer-driven, 700ms crossfades).
  The story survives; the stage machinery simplifies.
- **Choreography timeline (v2).** q=0 pin engages, garment at stage
  0 tint → q=0.18 beat 2: tint → stage 1 (900ms), counter 1→3 →
  q=0.38 beat 3: tint → stage 2, counter →5 → q=0.58 beat 4: tint →
  stage 3, counter →7 → q=0.78 beat 5: tint → stage 4, counter →9,
  "HUNG TO CURE" apparatus inks → q=1.0 pin releases into the buy
  block.
- **State matrix (v2).** *Rest (before pin):* hung garment, stage 0.
  *Hover:* the frame's woven rule warms to the next stage's pairing
  at 30% — a preview of one dip, no more (§6.8's grammar at figure
  scale). *Focus:* beats are text; the buy action focuses per §11.
  *Active:* n/a. *Scrolled-past:* released, garment rests at stage 4
  above the buy block if the visitor scrolls back — no: scrolling
  back re-enters the pin and the story re-tells (see States). Above
  the region entirely, the garment is absent (it lives in its
  region). *Disabled:* n/a. *Touch:* mobile stacking per the variant
  above.
- **Breakpoints (v2).** ≥1200px: pin 320vh, garment left, story
  right (46% column). 768–1199px: pin 280vh, story column 52%,
  garment frame narrower. <768px: pin cut; stacked beats, observer
  stepping.
- **Edge cases & failure modes (v2).** *Story with 3 beats:* the
  garment still ends at its record stage — boundaries redistribute
  (0.25 / 0.55) and the stage steps skip (0→2→4) — the record, not
  the beat count, sets the stages. *Image fails to load:* the woven
  frame holds a stage-tinted ground with the garment's name and
  record in apparatus — the story proceeds; a missing photograph
  does not strand the biography. *Very fast scroll through the
  region:* the tint snaps to the landed beat's stage (catch-up rule:
  crossfades are owed only to reading, not to teleporting).
- **Accessibility spec (v2).** The beats are ordinary text in DOM
  order — a screen reader reads the biography straight through,
  pin or no pin. The tint is decorative state; every stage is also
  stated in the beat's apparatus label and the counter. The
  photograph's alt text names the garment and its record ("The
  Apprentice Shirt — nine dips, three days"), never its current
  tint. Focus never enters a trap: the pinned figure contains no
  focusables except, after release, the buy action in normal order.
- **Tokens consumed (v2).** `--cloth`, `--dip-1`, `--blue`, `--vat`,
  `--tenth`, `--ease-oxidise`, `--dur-tint` (900ms), `--lerp` (0.09),
  `--pin-garment` (320vh).

### 6.7 Shibori draw

- **What & why.** In the craft section, a shibori resist pattern
  SVG-draws its bound circles — concentric rings, staggered — as the
  visitor scrolls. It belongs because the pattern being explained is
  produced by the binding technique's own geometry: shibori is cloth
  bound so the dye cannot reach it, and the drawing shows the
  binding (the circles) appearing in the order the dyer binds them,
  while the ground around them deepens — the resist stays cloth
  because it was *bound*, and the visitor watches the reason happen.
  It is the theme's one drawn element, and it draws the craft's
  actual diagram, not a motif.
- **Structure.** An inline SVG in the craft section: 5 concentric
  bound circles (radii 18–96px) centred on a fold point, plus two
  satellite bindings at the section's corners, each circle a stitched
  ring (dashed stroke in `--thread` on pale grounds) around a
  cloth-coloured resist disc. Beneath the SVG, the section's ground
  is a stage-1 tint deepening to stage 2 across the draw (§6.3's
  ladder applied as a scrub, not a re-entry — the craft section's
  one licensed scrub-dip, declared in the survey). The pattern's
  caption and the technique's steps are real text beside the SVG,
  each step keyed to a ring by number.
- **Motion spec.** Trigger: scroll scrub through the section's
  160vh draw zone, shared loop (lerp 0.09). Each ring's stroke draws
  over its segment of the zone (ring 1: q 0–0.22, ring 2: 0.14–0.36,
  … ring 5: 0.56–0.78) on `--ease-stitch`, staggered so two rings
  are always mid-draw — the binding is continuous work. As each ring
  completes, its resist disc is *confirmed*: the ground tint steps
  around it, leaving the disc at cloth. At q=1 the ground rests at
  stage 2 with five cloth rings standing in it — the finished
  shibori, produced by the scroll. Scrolling back un-draws in
  reverse (a diagram re-winds; contrast §6.6's story rule — this is
  a diagram, and diagrams re-tell).
- **States.** Undrawn (rings as hairline guides at 18% — the
  pattern is legible as a diagram even un-drawn) → drawing (scrub)
  → drawn (finished piece, ground at stage 2). Hover on a ring: its
  step in the text inks to full pairing (the diagram and its
  instructions are one element). Focus: rings are not focusable;
  the steps are text.
- **Content merge.** The SVG is the craft section's teaching figure:
  the steps reference the rings by number, the rings demonstrate the
  steps, and the deepened ground is the dye the binding resisted.
  Remove the scroll and the finished pattern still prints (fallback)
  — the lesson survives its performance.
- **Failure fallback.** No JS: the pattern prints complete — rings
  drawn, ground at stage 2, discs at cloth — as a finished shibori
  diagram. Loop killed mid-draw: a 1400ms watchdog completes the
  draw instantly to the state matching the scroll position's side
  of the zone (above: drawn; below: guides).
- **Reduced-motion variant.** The finished pattern, printed, with
  the steps numbered against the rings. No draw, no scrub-dip; the
  ground rests at stage 2 as in the no-JS state.
- **Performance budget & mobile variant.** One SVG, seven stroke
  animations on the compositor's behalf via stroke-dashoffset
  written by the loop; no canvas. Mobile (<768px): satellite
  bindings are cut, the five rings remain (they are the lesson), the
  draw zone shortens to 120vh and ring segments compress to match.
- **Choreography timeline (v2).** q=0 zone entered, guides at 18% →
  q=0–0.22 ring 1 draws → rings stagger per the segments above →
  each ring's completion steps the ground tint around it → q=0.78
  ring 5 completes → q=0.78–1 ground settles to stage 2, caption's
  final line ("THE BOUND CLOTH KEEPS ITS COLOUR") inks → rest:
  finished shibori.
- **State matrix (v2).** *Rest (below zone):* guides at 18%, ground
  stage 1. *Hover:* ring's step inks (desktop). *Focus:* n/a for
  rings; steps are text. *Active:* n/a. *Scrolled-past:* drawn,
  ground stage 2 — and re-entering from below re-winds per the scrub.
  *Disabled:* printed complete (no-JS/reduced). *Touch:* identical
  scrub; no hover keying.
- **Breakpoints (v2).** ≥1200px: full pattern, 160vh zone, rings to
  96px radius. 768–1199px: 140vh zone, rings to 80px. <768px:
  satellites cut, 120vh zone, rings to 64px, steps stack beneath the
  SVG instead of beside it.
- **Edge cases & failure modes (v2).** *Zone scrolled through
  instantly:* the pattern lands drawn (catch-up rule). *Section
  re-dipped by §6.3 while drawn:* the craft section is exempt from
  re-entry dipping — its ground is owned by this scrub — and the
  survey declares the exemption; a build that lets both systems dye
  one ground fails §10 gate 3. *SVG unsupported (legacy):* a static
  finished-pattern image with the same caption replaces it; the
  steps remain text.
- **Accessibility spec (v2).** The SVG is a figure with a title and
  description ("Five bound rings resist the dye; the ground deepens
  to the second dip, the rings stay undyed cloth"). The draw is
  never announced. The steps' text conveys the full technique
  without the figure. Ring strokes are `--thread`/stage pairings —
  line-work contrast only, and no information rides on stroke colour
  alone: ring numbers are printed beside the rings.
- **Tokens consumed (v2).** `--cloth`, `--dip-1`, `--blue`,
  `--thread`, `--ease-stitch`, `--dur-draw-zone` (160vh), `--lerp`
  (0.09).

### 6.8 Hover dip

- **What & why.** Hovering a product card darkens its lower edge one
  shade — a gradient rises 40% of the card over 500ms, as if the
  card's hem were touched to the vat. It belongs because inspection
  in a dye house is physical: you test-dip a corner before you
  commit the piece. The hover is that test, performed on the product
  card itself, and it teaches §6.9's click before the visitor ever
  makes it: hover shows one dip's worth of change, temporarily;
  click makes it real. Without the hover, the click's consequence
  would be a surprise; with it, the interface has a rehearsal.
- **Structure.** Each product card (§6.13) carries a `::after` hem
  layer: a gradient from transparent at 60% of the card's height to
  the *next* stage's colour at the card's foot, clipped to the card,
  `pointer-events: none`, opacity 0 at rest. The gradient's terminal
  colour is written from the card's current stage (a stage-1 card's
  hem deepens toward stage 2's blue; a stage-2 card's toward vat).
  Cards at their ceiling (§4: stage 2 for products) show no hem —
  there is no deeper test to offer, and the absence is itself
  information.
- **Motion spec.** Trigger: hover (pointer fine) or focus-within.
  The hem rises: opacity 0→1 and gradient extent 25%→40% of card
  height over 500ms `--ease-dip` — the fall into the liquid is the
  dip easing, not a generic fade. On leave, the hem recedes over
  350ms `--ease-raise` — faster out than in, because a test-dip is
  lifted decisively. The card's text never sits under the hem's
  darkest band: the price and name live in the card's upper 55%, by
  §6.13's layout, so the test never dyes the lettering.
- **States.** Rest (no hem) → testing (hem at 40%) → receding →
  rest. Focus-within holds the hem for as long as focus stays —
  keyboard inspection gets the same rehearsal, held, not timed.
  Active (mid-click): the hem is superseded by §6.9's full dip.
  Disabled (at ceiling): no hem, and the card's counter shows its
  ceiling stage name so the absence reads as a fact, not a fault.
- **Content merge.** The hem is the card's own lower cloth taking a
  test colour — it rises from the card's foot, within the card's
  frame, and its depth is the card's real next stage. It is not a
  shadow, glow or overlay borrowed from another theme's hover kit.
- **Failure fallback.** No JS: the hem is a pure CSS `:hover`/
  `:focus-within` layer and works without a line of script; its
  terminal colour is the card's shipped next-stage token. If CSS
  custom properties fail (legacy), the hem is absent and the card is
  complete without it — the rehearsal is an aid, never a dependency.
- **Reduced-motion variant.** The hem applies instantly at full 40%
  on hover/focus and removes instantly on leave — the state is
  information (what one more dip would do), so it is kept; only its
  travel rests.
- **Performance budget & mobile variant.** One pseudo-element
  gradient per hovered card, opacity/transform only. Mobile: touch
  has no hover — the first tap on a card raises the hem (the test)
  and the tap's target (the dip button, §6.9) is a separate, labelled
  control, so a test never accidentally commits. The hem on touch
  holds until another card is touched or the card leaves the
  viewport's centre band.
- **Choreography timeline (v2).** t=0 pointer enters → t=0–500 hem
  rises to 40% → held while hovered → t=leave → t=0–350 recedes →
  rest. Focus-within: t=0 hem applies over 500ms and holds until
  focus leaves the card, then recedes 350ms.
- **State matrix (v2).** *Rest:* no hem. *Hover:* hem at 40%.
  *Focus:* hem held via focus-within. *Active:* superseded by the
  click dip (§6.9). *Scrolled-past:* hem state irrelevant; a card
  leaving the viewport mid-hover resets instantly (no recede owed
  off-screen). *Disabled:* at-ceiling cards, no hem. *Touch:*
  first-tap test per the mobile variant.
- **Breakpoints (v2).** ≥1200px: hem to 40%, 500ms. 768–1199px: hem
  to 36% (cards are shorter), 450ms. <768px: tap-test model, hem to
  36%, 400ms.
- **Edge cases & failure modes (v2).** *Pointer sweeping across a
  grid:* hems trail at 500ms and never queue — a new hover cancels
  the previous card's rise mid-travel and starts its recede; the
  grid never shows more than one full hem plus one receding. *Card
  re-dipped by click while hem raised:* §6.9's dip absorbs the hem
  (its colour is the dip's first frame). *Card at stage 0 in a dark
  section:* the hem's terminal colour is stage-appropriate per the
  card's own stage, never the section's.
- **Accessibility spec (v2).** The hem is decorative state on a
  control whose real state (its dip count) is text (§6.9). Focus-
  within parity is mandatory, and the hem never covers text (§6.13's
  layout keeps lettering in the upper 55%; §10 gate 6 checks a hem
  at full rise against the card's lowest text line). Touch target:
  the card's dip control is ≥44px (§6.9).
- **Tokens consumed (v2).** `--ease-dip`, `--ease-raise`,
  `--dur-hem` (500ms), `--dur-hem-out` (350ms), the card's next-stage
  colour token.

### 6.9 Click dip & counter

- **What & why.** Clicking a product's dip control adds a real dip:
  its swatch visibly deepens through the full dip timeline and its
  printed counter ticks up — "9 dips" → "10 dips". It belongs
  because it hands the visitor the dyer's one creative act: the
  decision to immerse again. The product they buy is, in part, the
  product they dyed; the counter on the content is the record of
  their hand, kept in the open. It is also the theme's conversion
  mechanic in embryo — a visitor who has dipped a piece three times
  has a relationship with it that no "add to cart" button creates —
  and §6.14's form inherits the count when they order.
- **Structure.** Each product card carries a real `<button
  class="dip-button">` in its foot: apparatus label "DIP AGAIN" with
  the piece's counter beside it — `<output class="dip-count">9
  DIPS</output>` — and a 34×44px swatch chip showing the piece's
  current stage. The button's action writes to the session dip map:
  the product's session dips increment, its stage recomputes from
  record stage + session dips (capped at the product's ceiling), and
  the card's ground, chip and counter update from that one write.
  The count is never typed by the build's HTML at runtime — it is
  rendered from the map, so button, chip, ground and §6.17's record
  cannot disagree.
- **Motion spec.** Trigger: click/tap/Enter/Space on the dip button.
  The card dips on §5's timeline at card scale: immerse 250ms (the
  card's ground and chip take the green path), dwell 120ms, oxidise
  800ms `--ease-oxidise` to the new stage; the counter's numeral
  crossfades at the oxidise midpoint and lands with a 120ms
  `--ease-stitch` stitch-flash on the chip's top edge — the tally is
  sewn in. Total 1170ms. The button disables during the dip (cloth
  in the air cannot be re-immersed) and re-enables at rest. At the
  ceiling, the button's label becomes the ceiling's name — "AT THE
  TENTH DIP" for a master piece, "FULLY DYED" for a stage-2 card —
  and disables permanently for the session: the record is complete.
- **States.** Ready (label "DIP AGAIN", counter at record + session)
  → dipping (1170ms, disabled) → ready at new count → at ceiling
  (disabled, ceiling label). Hover: §6.8's hem (the rehearsal) plus
  the button's own rule inking. Focus: hem + §11's focus ring on the
  button.
- **Content merge.** The dip changes the product itself — its ground,
  its chip, its counter, its record entry (§6.17 gains a session
  line) — and the price does not change: the visitor's dips are
  attention, not a surcharge, and the theme never lets the mechanic
  become a pricing trick. What changes is the piece's depth and the
  visitor's claim on it: §6.14's form opens with "the piece you
  dipped to N" when they order.
- **Failure fallback.** No JS: the button submits as a plain form
  control to the product's page (the dip is a progressive
  enhancement of a link to the piece's record) — no dead buttons.
  Dip interrupted (tab hidden mid-oxidise): on return, the card is
  set to its map stage instantly; the map, not the animation, is the
  truth. Watchdog 1400ms per §5.
- **Reduced-motion variant.** The stage and counter change instantly
  on click; the stitch-flash is cut. The record deepens without the
  immersion being performed — the count is the content.
- **Performance budget & mobile variant.** One card's colour ramp +
  a counter crossfade per click; clicks are human-paced, so no
  queue management beyond the in-dip disable. Mobile: the button is
  a full-width 48px foot strip on the card (thumb-sized), the chip
  rides its left end, and the dip runs 950ms total — phones get the
  same chemistry at a slightly quicker boil.
- **Choreography timeline (v2).** t=0 click, button disables →
  t=0–250 immerse → t=250–370 dwell → t=370–1170 oxidise, counter
  flips at t≈770, stitch-flash at t=1170 → button re-enables (or
  takes its ceiling label) → §6.17's session line is written at
  t=1170 from the same map write.
- **State matrix (v2).** *Rest:* ready, counter current. *Hover:*
  hem (§6.8) + button rule inked. *Focus:* hem + focus ring.
  *Active:* the dip runs; button disabled. *Scrolled-past:* the
  card keeps its session stage (dyeing persists, §6.3's grammar).
  *Disabled:* mid-dip (1170ms) or at ceiling (session-permanent).
  *Touch:* full-width strip, 950ms dip, no hover pre-state (the
  strip's label is the instruction).
- **Breakpoints (v2).** ≥1200px: button in card foot, chip 34×44px.
  768–1199px: same, chip 30×40px. <768px: full-width 48px strip,
  dip 950ms, oxidise 650ms.
- **Edge cases & failure modes (v2).** *Double-click / impatient
  tapping:* the in-dip disable absorbs it; a click queued during the
  dwell is dropped, not buffered — one immersion at a time, as at a
  real vat. *Session dips on a product whose record is already at
  ceiling:* the button ships disabled with its ceiling label; there
  is nothing to rehearse (§6.8 also withholds the hem). *Two cards
  for the same product on one page:* both render from the same map
  entry and dip together — the map is keyed by product, not by card.
- **Accessibility spec (v2).** The button's accessible name includes
  the piece and the consequence: "Dip the Apprentice Shirt again —
  currently nine dips". The counter is an `<output>`; its change is
  announced politely (`aria-live="polite"` on the output, throttled
  to the completed dip — never mid-ramp). At ceiling, the disabled
  button's label states the fact. Touch target ≥44px (48px on
  mobile). Contrast: the button sits in the card's foot on the card's
  stage pairing at every stage.
- **Tokens consumed (v2).** `--ease-dip`, `--ease-oxidise`,
  `--ease-stitch`, `--dur-immerse-card` (250ms), `--dur-oxidise-card`
  (800ms), `--dur-fallback-dip` (1400ms), the product's stage tokens.

### 6.10 Footer confession

- **What & why.** The footer — the deepest blue on the page, resting
  at the tenth dip — honestly reports the visitor's own session in
  one sentence: "This footer took ten dips. Your visit gave this
  page N." It belongs because it is the theme's law (§1) spoken
  aloud at the exit: the page's darkest surface is dark *because of
  the reading*, and it says so, with the visitor's real number —
  sections completed, re-dips given, products dipped by hand, summed
  from the same session map everything else reads. Every other theme
  element performs the chemistry; this one *confesses* it, and the
  confession is what makes the performance trustworthy.
- **Structure.** A `<footer class="confession">` at `--tenth`,
  full-bleed, holding: the confession sentence in the record voice
  (15–17px, cloth), its number in an `<output>` rendered from the
  session map at footer entry; beneath it, the session's itemised
  tally in apparatus — "SECTIONS READ 7 · RE-DIPS 4 · BY YOUR HAND
  2" — each figure from the map, none typed; and the batch record's
  totals line (§6.17) closing the page. The footer never contains
  navigation marketing, newsletter bait or social icons — §4's
  density law reserves it for the confession and the record.
- **Motion spec.** Trigger: footer entry (its top crossing 85%
  viewport height). The footer does not dip — it *rests* at stage 4
  from first paint, the one surface whose depth is by construction.
  What moves is the confession's number: it counts up from 0 to the
  session's true total over 900ms, stepped in 60ms increments
  `--ease-stitch` (a tally being sewn, not a slot machine), landing
  exactly. The itemised tally inks line by line at 120ms stagger as
  the count completes. Nothing else in the footer animates; the
  deepest surface is the stillest.
- **States.** Unreached (resting at tenth, number unprinted — the
  DOM ships with the number's slot empty and the sentence reading
  "Your visit gave this page —." so a no-JS visitor gets the
  sentence's shape without a fabricated figure) → counting (900ms)
  → confessed (permanent). Scrolled back up and down again: no
  recount — the confession is made once; the number updates silently
  if the visitor dips more and returns (the map is live, the theatre
  is not repeated).
- **Content merge.** The footer's content *is* the session's record:
  the number is the sum of everything the visitor did to the page's
  colour, and the itemised tally is §6.3/§6.4/§6.9's counts agreeing
  in public. A footer that confessed a number its own elements
  couldn't reproduce would be the theme's one unforgivable lie —
  §10 gate 2 counts it by hand.
- **Failure fallback.** No JS: the sentence prints without a number
  ("Your visit gave this page its colour." — the fallback wording,
  true in every session) and the tally is replaced by the batch
  record's totals alone. Loop killed: the number is set instantly to
  the map's total when the footer enters (the observer is
  independent of the loop).
- **Reduced-motion variant.** The number prints at its total; the
  tally inks at once. The confession is text; only its counting
  rests.
- **Performance budget & mobile variant.** One counter, one stagger;
  negligible. Mobile: identical, with the tally wrapping to two
  lines — apparatus may wrap in the footer, nowhere else (§3).
- **Choreography timeline (v2).** t=0 footer top crosses 85% →
  t=0–900 number counts in 60ms steps → t=900 number lands →
  t=900–1260 tally lines ink at 120ms stagger → rest: confessed.
  If the session total is 0 (a visitor who jumped straight to the
  footer), the count is skipped and the sentence prints its zero
  honestly: "Your visit gave this page 0. The cloth above is still
  undyed." — the confession confesses skimming, too.
- **State matrix (v2).** *Rest (unreached):* sentence shape printed,
  number slot empty. *Hover:* none. *Focus:* footer links (record,
  §6.17) focus per §11. *Active:* n/a. *Scrolled-past:* confessed
  state persists above the page's end; there is nothing past the
  confession. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: tally on one line. 768–1199px:
  tally wraps at the middle dot. <768px: tally on two lines,
  confession sentence at 15px.
- **Edge cases & failure modes (v2).** *Session with no dips at
  all:* the zero wording above — never a borrowed number. *Visitor
  dips after confessing, returns:* number updates silently to the
  new total; if it grew, the sentence's verb holds ("gave") — the
  confession is a living record, re-inked without re-performance.
  *Footer on interior pages:* the confession runs there too (the map
  is per-session, site-wide), counting the whole visit, not the
  page — the sentence says "this page" only on the home page; on
  interior pages it reads "Your visit has given this site N." The
  wording is chosen by the page type at build time, never at
  runtime.
- **Accessibility spec (v2).** The confession is plain text in the
  footer landmark; the counting is never announced (the final number
  is simply present for anyone who reads the footer). Contrast:
  cloth on tenth 16.01:1 (AAA) — the page's most legible sentence is
  its confession, by design. The tally's apparatus is pale-dip on
  tenth (9.94:1).
- **Tokens consumed (v2).** `--tenth`, `--cloth`, `--pale-dip`,
  `--ease-stitch`, `--dur-confess` (900ms), `--stagger-tally`
  (120ms).

### Page-family elements

### 6.11 The drying-line navigation (page family: navigation)

- **What & why.** The site's navigation is the drying line itself: a
  horizontal rule across the page's head from which the destinations
  hang as labelled pieces — each nav item a small cloth tab suspended
  from the line by two peg ticks. It belongs because the line is the
  theme's spine (§4); making the visitor navigate *along the line*
  teaches the layout's grammar before the first section, and the
  current page's tab hangs at its true dip stage while the others
  hang undyed — where you are is a piece that has been in the vat,
  where you might go is still cloth.
- **Structure.** A `<nav class="line-nav">`: a 2px `--thread` rule
  spanning the header, with `<a>` tabs hanging beneath it, each tab a
  44px-minimum target carrying the destination's name in apparatus
  and a stage swatch-dot (10px) showing that page's resting stage as
  recorded in the survey (the products page hangs at stage 2, the
  record page at stage 3 — destinations have depths, stated before
  the click). The current page's tab is dipped to its stage and
  marked `aria-current="page"`; below 1200px the margin swatch's
  chip (§6.4) joins the bar at its right end.
- **Motion spec.** Trigger: load and hover/focus. On load, the tabs
  hang in: each drops its last 10px and sways once over 600ms
  `--ease-sway`, staggered 70ms left to right — laundry going up in
  reading order. On hover/focus, a tab dips its lower edge one stage
  over 300ms `--ease-dip` (§6.8's hem at navigation scale) and
  recedes on leave over 250ms. The current tab does not sway on load
  — it is already hung and dyed; stillness marks the present.
- **States.** Rest (undyed tabs, current tab at its stage) →
  hovered/focused (hem dipped) → active (navigation, §6.15's line
  pass). Scrolled: the nav is not sticky on ≥1200px (the bench's
  swatch §6.4 carries progress; a second sticky instrument would
  argue with it) — below 1200px the bar *is* sticky, because the
  bench and its swatch are gone and the chip needs a home.
- **Content merge.** The tabs are the site's real destinations with
  their real depths; the line they hang from is the same line the
  sections hang from (§4) — navigation and content share one piece
  of string, which is the theme's whole layout claim in miniature.
- **Failure fallback.** No JS: tabs stand hung at their stages, the
  current tab dipped, all links live — the sway is JS/CSS garnish on
  a complete nav. Watchdog: tabs not settled by 1200ms are set to
  rest.
- **Reduced-motion variant.** Tabs stand hung; hover still dips the
  hem instantly (state, not travel). No sway, ever, in this mode.
- **Performance budget & mobile variant.** Seven or fewer tabs, one
  sway each, once. Mobile (<768px): the line becomes a horizontally
  scrollable strip — the line extends beyond the screen's edge,
  which clothlines do — with the current tab scrolled into view on
  load; pegs are cut, tabs keep their stage dots.
- **Choreography timeline (v2).** t=0 header paints, tabs at −10px
  (JS-armed) → t=0–600 tab 1 sways → staggered 70ms per tab → all
  hung by t≈1020 → hover dips run on demand thereafter.
- **State matrix (v2).** *Rest:* hung, stages shown. *Hover:* hem
  dip 300ms. *Focus:* hem dip + §11 focus ring; focus and hover are
  the same state. *Active:* line pass (§6.15). *Scrolled-past:*
  desktop nav scrolls away (by design); mobile bar sticks.
  *Disabled:* a destination with no page is absent from the line —
  the line never promises a piece that isn't hung. *Touch:* no
  hover; tap is navigation; the current tab's stage is the state.
- **Breakpoints (v2).** ≥1200px: full line, non-sticky, swatch stays
  on the bench. 768–1199px: sticky bar, swatch chip joins at right.
  <768px: scrollable strip, pegs cut, chip + tally at the strip's
  fixed right end (outside the scroll area — the tally must not
  scroll away).
- **Edge cases & failure modes (v2).** *Many destinations (9+):*
  the line takes a second strand — a parallel rule 56px below,
  destinations ordered by depth across both — rather than shrinking
  tabs below 44px. *A destination deeper than stage 3:* only the
  record/footer class of page may dot stage 4 (§2's reservation);
  the survey enforces it. *Long names:* apparatus wraps to two lines
  inside the tab; tabs never truncate a destination's name.
- **Accessibility spec (v2).** A real `<nav>` with a list; current
  page exposed by `aria-current`, not by colour alone (the tab also
  carries a stitched underline). Stage dots are `aria-hidden`; the
  destination's depth is available in the link's `aria-label` where
  it matters ("The batch record — third dip"). Focus order is line
  order. Targets ≥44px at every breakpoint.
- **Tokens consumed (v2).** `--thread`, `--cloth`, `--dip-1`,
  `--blue`, `--vat`, `--ease-sway`, `--ease-dip`, `--dur-hang`
  (600ms), `--stagger-tab` (70ms).

### 6.12 The raised-cloth hero composition (page family: hero)

- **What & why.** The hero's fixed composition: undyed ground above,
  the vat band at the bottom edge, the raised cloth panel (§6.1)
  overlapping the band's surface line, the headline printed on the
  panel as it rises, the oxidising word (§6.2) inside the headline,
  and beneath the standfirst one apparatus line stating the house's
  count ("EST. 1987 · VAT No. 3 · CLOTH DIPPED TO ORDER"). It
  belongs because the hero is the theme's contract in one screen:
  cloth, vat, chemistry, record — and every later section is this
  composition at a smaller scale.
- **Structure.** A `<header class="hero">` occupying 100vh (min
  640px): the panel (§6.1) centred in a 1120px column, overlapping
  the vat band by 18% of the panel's height — the cloth is *at* the
  vat, neither above it nor sunk in it. The headline's reveal is a
  mask: a clip on the panel's inner content wrapper whose top edge
  is the panel's rising edge, so the print appears as the cloth
  clears the surface line. The band carries the motes (§6.5) and, at
  its right end, the scroll cue: a small undyed tab hanging below
  the surface line labelled "THE CLOTH" with a downward stitch —
  the page's sections named before they are seen.
- **Motion spec.** The ceremony is §6.1's timeline; the composition
  adds two beats: the vat band parallaxes behind the rising panel —
  the band's inner content (motes field, surface line) translates at
  0.92× the panel's rise, the page's only parallax pair (§5) — and
  the headline's mask completes exactly with the rise (t=1900 in
  §6.1's timeline), after which the apparatus line stitches in over
  400ms `--ease-stitch`. The scroll cue's tab sways once at t=3200,
  900ms `--ease-sway`, and never again — a cue that keeps waving is
  a distraction wearing a cue's clothes.
- **States.** Ceremony (§6.1's states) → rested hero → scrolled
  (the hero's pieces hang still; the band's motes suspend as it
  leaves). The composition has no hover state of its own.
- **Content merge.** Every element in the frame is load-bearing: the
  panel is the headline's surface, the band is the dip's destination,
  the apparatus line is the house's record summary. A hero image
  added "for warmth" would be a second, false cloth — refused.
- **Failure fallback.** The rested composition is the shipped DOM:
  panel raised at stage 2, headline printed, apparatus line present,
  band deep with its static mote field. Any JS failure leaves a
  complete hero (§6.1's watchdog governs the panel).
- **Reduced-motion variant.** The rested composition plus §6.1's
  apparatus line recording the first dip in words.
- **Performance budget & mobile variant.** The hero's total budget:
  the panel ceremony (§6.1), one canvas (§6.5), no photographic
  image at all — the hero is cloth, type and liquid. Mobile: 92vh,
  panel overlap 12%, band 180px, scroll cue cut (the thumb knows).
- **Choreography timeline (v2).** §6.1's timeline, plus: rise window
  (t=1150–1900) band parallaxes at 0.92× → t=1900 mask completes,
  headline whole → t=1900–2300 apparatus line stitches → t=2850
  oxidising word begins (§6.2) → t=3200 scroll tab's single sway.
- **State matrix (v2).** *Rest:* rested composition. *Hover:* only
  the hero action (§11 button) has a state. *Focus:* §6.1's rule —
  focus completes the ceremony. *Active:* the hero action navigates
  (§6.15). *Scrolled-past:* motes suspended; composition still.
  *Disabled:* n/a. *Touch:* identical, minus the scroll cue.
- **Breakpoints (v2).** ≥1200px: 100vh, overlap 18%, band 260px.
  768–1199px: 96vh, overlap 15%, band 220px. <768px: 92vh, overlap
  12%, band 180px, panel 38vh (§6.1).
- **Edge cases & failure modes (v2).** *Short landscape screens
  (height <560px):* the hero releases its 100vh claim and sizes to
  content + band, so the panel and band never crush the headline —
  the composition is a ratio, not a trap. *Headline longer than 3
  lines:* refused at build (§3); the mask is sized to the set
  headline, never discovered at runtime.
- **Accessibility spec (v2).** The `<h1>` is first in the tab and
  reading order; the mask is visual only (content is never clipped
  from the accessibility tree). The scroll cue is a real link to the
  first section. The band's motes are `aria-hidden` (§6.5).
- **Tokens consumed (v2).** `--cloth`, `--vat`, `--blue`, `--thread`,
  `--ease-stitch`, `--ease-sway`, `--parallax-vat` (0.92).

### 6.13 Cloth-piece cards (page family: cards / listing)

- **What & why.** Products are cloth pieces on the line: flat,
  square-cut cards hung in a row, each carrying its photograph in a
  woven frame, its name, its dip record in apparatus, its price —
  and the two dip interactions (§6.8's hem, §6.9's button) in its
  foot. It belongs because a product in this theme is not a tile in
  a grid; it is a piece of work whose depth is its biography, and
  the card is the smallest surface that can hold a name, a count and
  a hand's worth of dyeing.
- **Structure.** A `<article class="piece-card" data-stage="…">`:
  two peg ticks at its head where it meets the row's line (a
  horizontal `--thread` rule running the grid's width at each row);
  the photograph in a woven frame (3px double rule in the card's
  stage pairing) occupying the upper 55% minus the name zone — by
  layout law, name, record and price all sit in the card's upper
  55%, above §6.8's hem line; the foot holds the dip button and
  counter (§6.9) and the swatch chip. The card's ground is its
  stage's colour (§6.9's map); the frame's indigo deepens as the
  image centres in the viewport — a one-time 600ms `--ease-oxidise`
  tint step on the frame only, as the piece comes off the line into
  the light.
- **Motion spec.** Entry: cards hang in as their row enters — drop
  14px + one sway, 550ms `--ease-sway`, staggered 80ms along the
  row, like pieces hung one after another by one pair of hands.
  Frame deepening: when a card's image crosses the viewport's
  centre band (±15%), its frame tint steps once (600ms). Hover/focus:
  §6.8. Click: §6.9. Nothing else moves; a card at rest is cloth at
  rest.
- **States.** Hung (at record stage) → centred (frame deepened) →
  tested (§6.8) → dipped (§6.9) → at ceiling. Scrolled-past: hung
  state persists; the frame's deepening does not reverse (the piece
  has been seen in the light once).
- **Content merge.** The card's colour is the product's record; its
  foot is the visitor's hand; its frame is the woven edge of the
  cloth itself. Every visual fact on the card is a fact about the
  product.
- **Failure fallback.** No JS: cards stand hung at their record
  stages with counters printed from the record, dip buttons as
  record links (§6.9's fallback). Images missing: the woven frame
  holds the stage ground with the piece's name and record in
  apparatus — a card never shows a broken-image icon in this theme.
- **Reduced-motion variant.** Cards stand hung; frame deepening
  applies instantly on centring; hem and dip per their variants.
- **Performance budget & mobile variant.** Images ≤120KB each, lazy
  below the first row; entry sway is transform-only. Mobile: one
  card per row (pieces hang singly on a phone's line), the row line
  runs per card, entry stagger becomes per-card on entry, dip strip
  per §6.9.
- **Choreography timeline (v2).** Row top crosses 80% → cards drop
  and sway at 80ms stagger, all hung by t≈550+80×(n−1) → each card's
  frame deepens as it crosses the centre band → hover/click grammar
  live from hang completion (a card mid-sway accepts hover; the hem
  waits for the sway's end to avoid two motions on one surface).
- **State matrix (v2).** *Rest:* hung at record stage. *Hover:* hem
  (§6.8). *Focus:* hem + ring. *Active:* dip (§6.9). *Scrolled-past:*
  hung, frame deepened if centred once. *Disabled:* at-ceiling
  cards disable their dip control (§6.9). *Touch:* tap-test (§6.8),
  dip strip (§6.9).
- **Breakpoints (v2).** ≥1200px: 3 across, row line continuous.
  768–1199px: 2 across. <768px: 1 across, frame deepening threshold
  widens to ±25% (shorter screens centre pieces sooner).
- **Edge cases & failure modes (v2).** *A product with no
  photograph:* the frame holds a shibori-mini (§6.7's smallest ring
  set) drawn in the piece's stage — the catalogue's own pattern
  stands in, never a grey box. *Long names:* two lines maximum,
  then the name is re-set smaller (Mincho 700 at 20px) — never
  truncated; a dyer does not cut a name. *Price changes:* the price
  is text; stage changes never touch it (§6.9's merge rule).
- **Accessibility spec (v2).** The card is an article with the
  product name as its heading; the photograph's alt names the piece
  and its colour plainly ("Apprentice Shirt, second-dip blue"). The
  dip record is text. The dip button's name per §6.9. Focus order:
  card by card, left to right along the line.
- **Tokens consumed (v2).** `--thread`, `--ease-sway`,
  `--ease-oxidise`, `--dur-hang-card` (550ms), `--stagger-card`
  (80ms), the product's stage tokens.

### 6.14 The commission form — order by the dip (page family: forms / conversion)

- **What & why.** The conversion form takes an order the way dyeing
  is actually specified: choose the cloth, state the yardage, choose
  the target stage — a radio line of the ladder itself, each stage
  shown as its swatch with its true name and its days ("SECOND DIP —
  2 DAYS IN THE VAT HOUSE") — then the dyer's details. It belongs
  because a generic checkout would waste the theme's whole argument
  at the exact moment it should pay off: here the visitor *commissions
  a dyeing*, the form's central choice is the dip ladder they have
  been watching all page, and if they arrived with a hand-dipped
  product (§6.9) the form opens already knowing it.
- **Structure.** A `<form class="commission">` on a stage-0 cloth
  ground (orders are written on undyed paper; the dyeing is what's
  ordered, not the form's own state): cloth select as a seam list of
  ruled radio lines (selects are refused, §11); yardage as a number
  input with the metre tally; target stage as four radio swatch
  lines (stages 1–4, stage 4 labelled with its truth — "TENTH DIP —
  MASTER PIECES ONLY, QUOTED AFTER THE BATCH RECORD IS READ" — and
  disabled for cloths that cannot take it, with the reason printed);
  name and direction fields as inscription lines; the submit as a
  stitch press: "COMMISSION THE DYEING". Errors appear beneath their
  fields in the record voice (§12), in `--vat` ink with a stitched
  left rule — never in a red this palette does not own.
- **Motion spec.** Field focus: the field's rule inks from
  `--thread` to `--vat` over 200ms `--ease-stitch`, with a 6px
  stitch dash drawing under the label. Stage radio choice: the
  chosen line's swatch dips — 600ms `--ease-oxidise` through its
  green flash to the stage — while the days line beneath updates
  from the batch record's real durations (§6.17). Submit: the button
  presses (translateY 2px, `--ease-stitch` 120ms) and, on success,
  the form is replaced by a dipped confirmation swatch (§6.15's
  grammar in miniature): a cloth panel at the ordered stage bearing
  the commission number, derived from the batch record's sequence —
  "COMMISSION No. 214 — SECOND DIP, FOUR METRES, ENTERED IN THE
  RECORD."
- **States.** Rest → focused field (rule inked) → stage chosen
  (swatch dipped, days stated) → submitting (button pressed, fields
  held) → confirmed (swatch panel) or failed (form kept whole, §12's
  failure note above it: "NOT ENTERED — THE VAT HOUSE COULD NOT BE
  REACHED. YOUR WORDS ARE KEPT ABOVE."). Validation errors are
  per-field, persistent until corrected, and never clear a field.
- **Content merge.** The form's choices are the theme's facts: the
  stages are §2's ladder with §6.17's real durations, the cloths are
  the catalogue's real cloths, and the commission number continues
  the batch record's real sequence. A visitor who dipped a product
  (§6.9) finds the form pre-set to that piece and its count — the
  hand's work carries into the order without a word of copy claiming
  it does.
- **Failure fallback.** The form is a real form: no JS, it submits
  natively, stage radios are native radios with swatch styling,
  errors are server-rendered in the same voice. A failed submit at
  any layer keeps every field exactly as written (§10 gate 7).
- **Reduced-motion variant.** Rules ink instantly; the chosen swatch
  sets to its stage instantly; the confirmation panel appears
  without its dip. The commission is a record; only its dyeing
  rests.
- **Performance budget & mobile variant.** No libraries; the swatch
  dip is one colour ramp. Mobile: stage radios become full-width
  52px lines with the swatch at the left and days at the right —
  the ladder reads down the thumb — and the submit sticks to the
  viewport foot within the form's section only.
- **Choreography timeline (v2).** Focus: rule inks 200ms, stitch
  draws 200ms → stage choice: swatch dips 600ms, days line crossfades
  at t=300 → submit press 120ms → success: form crossfades 250ms to
  the confirmation swatch, which dips 800ms to the ordered stage as
  the commission number inks.
- **State matrix (v2).** *Rest:* undyed form, first cloth line
  unchosen. *Hover:* radio lines' rules warm to `--blue`. *Focus:*
  rule ink + stitch. *Active:* press. *Scrolled-past:* the form
  keeps its entries (a form is a workbench, not a performance).
  *Disabled:* stage 4 for unfit cloths, with reason printed; submit
  disabled only while submitting. *Touch:* 52px lines, sticky
  submit per the variant.
- **Breakpoints (v2).** ≥1200px: two-column (cloth + yardage left,
  ladder right, details below). 768–1199px: one column, ladder
  full-width. <768px: one column, sticky submit, days line wraps
  under its swatch.
- **Edge cases & failure modes (v2).** *A cloth whose record shows
  it cannot reach stage 3:* the ladder offers stages 1–2 only, with
  the limit stated in the cloth's own line ("THIS CLOTH TAKES TWO
  DIPS — ITS RECORD IS IN THE BATCH BOOK") — the form never sells a
  stage the vat cannot give. *Yardage beyond stock:* the tally line
  states the true remainder from the record and caps the input with
  the reason, not a silent clamp. *Pre-set from §6.9:* if the dipped
  product was a finished piece, not a cloth, the form opens in its
  "order this piece" mode with the ladder replaced by the piece's
  own record — the form has two honest shapes and never fakes the
  other.
- **Accessibility spec (v2).** Native radios and inputs with real
  `<label>`s; the stage radios' labels include the days ("Second
  dip — two days in the vat house"). Errors are linked with
  `aria-describedby` and summarised at the form's head on submit.
  The confirmation replaces the form with a heading + record text
  and moves focus to it. Targets ≥44px; the ladder lines ≥52px on
  mobile.
- **Tokens consumed (v2).** `--cloth`, `--vat`, `--blue`, `--thread`,
  `--green`, `--ease-stitch`, `--ease-oxidise`, `--dur-rule` (200ms),
  `--dur-swatch-dip` (600ms).

### 6.15 Undyed skeleton + line-pass transition (page family: loader / transition)

- **What & why.** While a page loads, its pieces are present as
  undyed cloth: pale panels hung on the line in the real layout's
  anatomy, labelled in apparatus with what is coming ("THE CLOTH —
  DYEING"). Navigation between pages is a line pass: a fresh undyed
  piece is raised across the viewport on the line, and the new page
  hangs beneath it already dyed to its resting states. It belongs
  because waiting in this theme has a true form — undyed cloth is
  what every piece is before the work — and a transition that raises
  cloth is the line doing its one job between rooms of the dye
  house.
- **Structure.** Skeleton: the loading page renders its real layout
  with content panels as stage-0 blocks at the real pieces' heights,
  each with a stitched apparatus label; panels are `aria-hidden`
  placeholders *beside* a visually-hidden full text summary, never
  instead of content. Transition: an overlay piece — full-viewport
  undyed panel suspended from a line rule at the viewport's top —
  which lowers to cover, holds while the new page is swapped, then
  raises to reveal it; the new page paints beneath at its resting
  states (no re-dip of §6.3 stages: session stages are in the map
  and apply at first paint).
- **Motion spec.** Skeleton panels settle in with a 300ms
  `--ease-dip` drop as they mount; a panel unresolved after 1200ms
  gains the stitched label "STILL ON THE LINE" (the dyer's patience,
  stated). Transition: cover lowers 450ms `--ease-dip`, hold ≤300ms
  (or until the new page's first contentful paint), reveal raises
  550ms `--ease-raise`; total ≤1300ms, and any navigation that
  cannot complete the swap by 900ms of hold skips the reveal's wait
  and raises anyway — the line never holds a visitor hostage to a
  slow room.
- **States.** Skeleton: mounting → waiting (labelled) → replaced
  (panel crossfades 200ms to the real piece at its resting stage).
  Transition: idle (piece parked above the viewport) → covering →
  holding → revealing → idle.
- **Content merge.** The skeleton is the page's own anatomy in
  undyed cloth — same line, same pieces, no dye yet — and the
  transition piece is the line's cloth, not a branded curtain: it
  carries the destination's name stitched in apparatus at its hem,
  so the pass itself is wayfinding.
- **Failure fallback.** No JS: no skeleton (content streams in as
  the server sends it, complete) and navigation is instant. If the
  transition's swap fails, the piece raises on the *old* page with
  the destination's name struck through in apparatus and §12's line
  beneath the nav: "THE LINE COULD NOT CARRY YOU — THE PAGE IS
  STILL HERE." Nothing is ever left covered.
- **Reduced-motion variant.** No pass: navigation is instant, with
  the destination's tab (§6.11) flashing its stage once (opacity,
  150ms) as the only acknowledgement. Skeletons appear without the
  drop.
- **Performance budget & mobile variant.** The overlay piece is one
  transformed div, reused across navigations. Mobile: cover 380ms,
  reveal 450ms (smaller distances), and the skeleton's labels cut to
  the piece name only.
- **Choreography timeline (v2).** Click → t=0–450 cover lowers,
  destination name at its hem → hold until swap (≤900ms cap) →
  raise 550ms revealing the new page at rest → t≤1300 idle. Skeleton:
  mount drop 300ms → label at 0ms, "STILL ON THE LINE" at 1200ms →
  replacement crossfade 200ms on resolve.
- **State matrix (v2).** *Rest:* parked / no skeleton. *Hover:* n/a.
  *Focus:* a focus-triggered navigation runs the same pass; focus
  lands on the new page's heading after the raise. *Active:* the
  pass. *Scrolled-past:* n/a. *Disabled:* if the router cannot
  intercept, native navigation occurs and the piece never moves.
  *Touch:* identical timings at mobile values.
- **Breakpoints (v2).** ≥1200px: full pass (450/550ms). 768–1199px:
  420/500ms. <768px: 380/450ms, skeleton labels shortened.
- **Edge cases & failure modes (v2).** *Back button:* the pass runs
  in reverse order (raise from the bottom edge is refused — the line
  is at the top; the piece lowers and raises identically, and the
  destination name is the page returned to). *Rapid double
  navigation:* the second click during a hold replaces the
  destination; the piece never double-covers. *Slow page (>900ms):*
  the hold cap raises the piece onto a skeleton of the new page —
  the visitor waits *in* the new room, not in the doorway.
- **Accessibility spec (v2).** The overlay is `aria-hidden` and never
  traps focus; the swap uses the router's standard announcement
  (new page title). Skeleton regions use `aria-busy` on their
  container only while genuinely loading, with the hidden text
  summary available immediately. The pass never delays a screen
  reader's access to the new page: content is exposed at swap, not
  at raise completion.
- **Tokens consumed (v2).** `--cloth`, `--thread`, `--vat`,
  `--ease-dip`, `--ease-raise`, `--dur-cover` (450ms), `--dur-reveal`
  (550ms), `--dur-hold-cap` (900ms).

### 6.16 Dyer's figures — dip counts & yardage (page family: data)

- **What & why.** The page's numbers — lifetime dips in the vat
  house, metres dyed, pieces on the line, days the vat has been
  alive — count up when their piece is hung, in tabular Gothic,
  stepped like a tally being chalked on the vat-house wall. It
  belongs because a dye house runs on counts, and its figures are
  the maker's credentials stated as arithmetic: not "thousands
  happy customers" but "11,204 dips since 1987", a number with a
  ledger behind it (§6.17) that the visitor may audit.
- **Structure.** A `<dl class="dyers-figures">` band inside its
  section: each figure a term (apparatus label: "DIPS IN THIS VAT")
  and a definition holding an `<output>` numeral plus its unit and
  its source line in caption ("FROM THE BATCH RECORD, 1987–2026").
  The figures are rendered from the same data object as §6.17's
  record — the band is the record's summary, printed large.
- **Motion spec.** Trigger: the band's piece hung (§6.11's entry) —
  figures count from 88% of value to value (never from 0: a tally
  does not pretend the vat was empty this morning) over 800ms in
  40ms steps `--ease-stitch`, units settling first, the final digit
  landing with the source line inking beneath it. A figure counts
  once per session.
- **States.** Printed (no-JS/fallback: full value) → counting
  (800ms) → at rest (full value, source inked). Hover: the figure's
  source line underlines with a stitch — the audit is one gesture
  away. Focus: figures are text, not controls.
- **Content merge.** Each figure is the batch record's arithmetic
  made visible; its source line is part of the figure, not a
  footnote beneath the section. A figure without a source line is
  refused at build (§10 gate 2).
- **Failure fallback.** Values print in full in the DOM; the count
  is a JS enhancement that starts from the printed value's 88% —
  if the script dies mid-count, a 1000ms watchdog sets every figure
  to its printed value.
- **Reduced-motion variant.** Figures print at value; source lines
  inked. No counting.
- **Performance budget & mobile variant.** ≤6 figures, text writes
  only, one 800ms window. Mobile: figures stack two per row, count
  duration 650ms.
- **Choreography timeline (v2).** Piece hung → t=0 figures at 88% →
  40ms steps land unit digits first → t=800 values exact → source
  lines ink at 120ms stagger → rest.
- **State matrix (v2).** *Rest:* full values, sources inked.
  *Hover:* source stitch-underline. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* values hold; no recount on re-entry (contrast
  §6.3: figures are history, not cloth — history does not re-dip).
  *Disabled:* n/a. *Touch:* no hover; source lines are always inked
  on touch layouts.
- **Breakpoints (v2).** ≥1200px: one row of ≤6. 768–1199px: 3 + 3.
  <768px: 2 per row, 650ms count.
- **Edge cases & failure modes (v2).** *A figure the record cannot
  support this year* (a new vat, zero completed batches): the figure
  is omitted from the band — the band holds five honest figures
  rather than six with a newborn dressed as a veteran. *Very large
  counts:* tabular Gothic at full size; no abbreviation ("11.2k" is
  a dashboard's shorthand and is banned, §12) — the tally is written
  out, commas and all.
- **Accessibility spec (v2).** Figures are a definition list, read
  as label + value + source. The counting is never announced; the
  final value is the DOM value from first paint (the 88% start is a
  visual write over it, with the true value in an `aria-hidden`
  twin pattern avoided — instead the output's text is the value and
  the count is performed by a visual overlay numeral, so assistive
  tech never reads a partial tally).
- **Tokens consumed (v2).** `--ease-stitch`, `--dur-count` (800ms),
  `--step-count` (40ms), `--pale-dip` (sources on deep grounds).

### 6.17 The batch record (page family: trust / record)

- **What & why.** A real table — the page's audit — listing every
  product and piece with its true dip count, its days, its vat, and
  its ceiling: the ledger behind every number printed anywhere on
  the site. It belongs because §1's law needs a public instrument:
  any visitor who doubts a "9 dips" beside a shirt can find the
  shirt's row here and check the count, the days and the vat against
  the card. In a theme whose entire claim is that colour is a
  record, the record must exist, be findable, and agree — §10 gate 3
  reads the page's counters against this table by hand.
- **Structure.** A `<table class="batch-record">` in its own
  section (resting at stage 3 — the record is deep work): apparatus
  headers (PIECE · DIPS · DAYS · VAT · CEILING), one row per piece,
  rows generated from the same data object as §6.13's cards and
  §6.16's figures. Session activity (§6.9's hand-dips) appears as a
  final ruled block beneath the table — "THIS SESSION, BY YOUR
  HAND" — with one line per dipped product, written at the moment of
  the dip from the session map. The table's foot carries the totals
  the footer (§6.10) repeats.
- **Motion spec.** Entry: the table's head rule draws 600ms
  `--ease-stitch` as the section hangs; rows do not animate
  individually (a ledger does not perform its rows). Session lines
  are appended with a 200ms ink-in. Nothing else moves — the
  record's stillness is its authority, the same stillness §6.10's
  footer keeps.
- **States.** Rest (complete table) → session lines appended (as
  dips occur) → rest. Hover on a row: the row's ground warms one
  tint toward its piece's stage (150ms) — finding a row feels like
  touching its cloth. Focus: rows are not focusable; the section's
  link from §6.11's nav lands here.
- **Content merge.** The record is not *about* the products; it is
  the same data the products render from, printed in ledger form.
  Its session block is §6.9's other printing. If the table and a
  card ever disagree, the build — not the visitor — has failed, and
  §10 gate 3 exists to catch it before the visitor can.
- **Failure fallback.** No JS: the full record table prints (it is
  server-rendered); only the session block is absent, replaced by
  its heading and the true static line "NO DIPS BY YOUR HAND YET
  THIS SESSION" — which JS then maintains. A record that requires
  scripting to exist would be no record at all.
- **Reduced-motion variant.** Identical, minus the head rule's draw
  (printed drawn) and the row warm (instant).
- **Performance budget & mobile variant.** A table; negligible.
  Mobile: the table becomes a stacked ledger — each row a block with
  its apparatus pairs — because a five-column ledger squeezed to
  360px would falsify its own readability; the data is identical,
  the ruling is vertical.
- **Choreography timeline (v2).** Section hangs → head rule draws
  600ms → table at rest → session lines append at each §6.9 dip
  (t=dip completion, 200ms ink) → footer totals (§6.10) read the
  same object at footer entry.
- **State matrix (v2).** *Rest:* complete. *Hover:* row warm.
  *Focus:* n/a within the table. *Active:* n/a. *Scrolled-past:*
  complete; session lines persist. *Disabled:* n/a. *Touch:* no
  row warm; session lines identical.
- **Breakpoints (v2).** ≥1200px: full table. 768–1199px: full table,
  caption sizes drop one step. <768px: stacked ledger blocks.
- **Edge cases & failure modes (v2).** *A catalogue of 200 pieces:*
  the record paginates by vat (one table per vat, in depth order) —
  never by hiding rows behind a "load more" that would make the
  audit partial. *A piece dipped by hand that is not in the table*
  (a one-off): its session line carries the note "NOT IN THE BATCH
  BOOK — A SINGLE PIECE" — the record admits its own edge rather
  than silently absorbing it. *Totals vs rows:* totals are computed
  from the rows at render; a hand-typed total is a gate failure.
- **Accessibility spec (v2).** A real `<table>` with `<th scope>` —
  the audit must be auditable by everyone. The session block is a
  list with a heading, updated without live-region chatter (it is
  read on arrival, like the footer). Contrast: the section rests at
  stage 3, cloth on vat 12.88:1; apparatus in pale-dip (7.99:1).
- **Tokens consumed (v2).** `--vat`, `--cloth`, `--pale-dip`,
  `--ease-stitch`, `--dur-record-rule` (600ms).

### 6.18 The never-dipped page (page family: 404 / empty state)

- **What & why.** The 404 is a piece that was never dipped: an
  undyed cloth hung on the line, at stage 0 on a page where the
  visitor may already have dyed half the site, bearing the record
  voice's plain statement — "This cloth was never dipped" — the
  sought direction struck through in thread, and three real
  suggestions hung beneath it as small dyed pieces. It belongs
  because an undyed page in a dyed session is the theme's most
  eloquent error state: the visitor's own progress (their swatch,
  §6.4) makes the emptiness visible — this piece missed the vat
  because it does not exist.
- **Structure.** A centred stage-0 panel on the page ground: the
  sought path in apparatus, struck through with a stitched rule;
  the heading in Mincho ("This cloth was never dipped."); two lines
  of record prose; three suggestion pieces (§6.13's card anatomy at
  half size) at their true stages; and the swatch's bench position
  left respectfully unchanged — the session's record is not reset by
  an error.
- **Motion spec.** Entry: the undyed panel hangs in with one sway
  (600ms `--ease-sway`) — it is a piece on the line like any other.
  The suggestions hang at 90ms stagger. Nothing dips: the page's one
  stillness is the point, and a "helpful" animation that dyed the
  panel would destroy the sentence it exists to say. The struck
  rule is drawn at build (printed), not animated.
- **States.** Rest (undyed, complete) — the page has no other state.
  Its suggestions carry their normal §6.13 states.
- **Content merge.** The undyed panel is legible *because* of the
  session's dyeing — in a fresh session it is simply a pale page
  with a clear message; in a deep session it is conspicuously the
  only undyed thing left. Both readings are true, and both are the
  theme working as designed.
- **Failure fallback.** The 404 is a static page by construction; it
  must render with no JS, no loop, no observer — the error page is
  the last place a dependency may fail.
- **Reduced-motion variant.** Identical, minus the sway.
- **Performance budget & mobile variant.** Static; the suggestions'
  images follow §6.13's budget. Mobile: panel full-width, suggestion
  pieces stack.
- **Choreography timeline (v2).** t=0 page paints → panel sways
  600ms → suggestions hang at 90ms stagger → rest. That is all, by
  law.
- **State matrix (v2).** *Rest:* undyed panel, suggestions hung.
  *Hover:* suggestions per §6.13. *Focus:* first suggestion / home
  link per §11. *Active:* navigation (§6.15). *Scrolled-past:* the
  page rarely scrolls; if it does, nothing changes. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: panel 720px centred. 768–1199px:
  600px. <768px: full-width, suggestions stacked.
- **Edge cases & failure modes (v2).** *Empty states reuse:* search
  with no results and an empty commission list use this page's
  grammar with their own true sentences ("No cloth in the record
  matches that name.") — never the 404's sentence, which is reserved
  for the never-dipped. *A mistyped product URL:* if the path
  nearly matches a real piece, that piece is the first suggestion,
  labelled with its record — the dyer guesses from the book, not
  from a algorithm's confidence score.
- **Accessibility spec (v2).** The heading is the page's `<h1>`; the
  sought path is text; suggestions are real links with their records
  in text. Contrast: the panel is stage 0 (ink on cloth 12.88:1) —
  the error page is among the most legible pages on the site.
- **Tokens consumed (v2).** `--cloth`, `--ink` (`--vat`), `--thread`,
  `--ease-sway`, `--dur-hang` (600ms).

## 7. Page application map

**Home — the full dyeing.** Hero composition (§6.12) with the first
dip (§6.1) and oxidising word (§6.2); the cloth (product pieces,
§6.13) on their rows; the signature garment's pinned story (§6.6);
the craft section with the shibori draw (§6.7); the dyer's figures
(§6.16); the batch record (§6.17); the commission form (§6.14); the
confession (§6.10). Sections re-dip per §6.3 within their declared
ceilings (§4). The home page is the only page with a vat band and
motes (§6.5) — the vat lives at the front of the house.

**Listing — one line of pieces.** A category page is a single long
line: its pieces (§6.13) in rows of three, its own head apparatus
stating the line's count and the cloth ("TWELVE PIECES — COTTON,
DIPPED TO ORDER"), the margin swatch (§6.4) counting the listing's
own sub-sections (the cloth, the record excerpt, the form's anchor).
Filters, if the catalogue honestly needs them, are stitch-toggles on
the line (§11) — never a sidebar of facets, which is a warehouse's
furniture in a dye house.

**Detail — one piece, at its record.** The piece at full size: its
photograph in the woven frame at its record stage, its name and full
dip record, its batch row excerpted from §6.17, its dip button
(§6.9 — the same map entry as its card, so dipping here deepens the
card everywhere), and the commission form (§6.14) pre-set to the
piece. Its neighbours on the line close the page ("ALSO ON THIS
LINE"). A detail page never re-stages its piece for display: the
record stage is the display stage.

**About — the vat house.** The makers and the method, set on a
stage-1 ground that re-dips like any piece: who tends the vat, how
the ladder is judged, the vat's own biography (a real vat is fed and
kept alive for years, and its age is a figure §6.16 may print with
its source). This is where §1's law is stated in long form — the
about page is the theme's ethics, placed where a committed visitor
digs for it.

**Contact / commission — the form's own page.** §6.14 alone on
undyed ground, reached from anywhere; a direct arrival lands on
cloth that has not been dipped, which is correct: an order begins
undyed, whoever you are.

**The never-dipped page (404).** §6.18, everywhere, unchanged.

**Interior pages and the vat band.** The band and motes are
home-only (§6.5). Interior heroes are a single hung piece on the
line — the page's title piece at its declared stage, its apparatus
beneath — so the site keeps one vat and many lines.

## 8. Worked examples

### 8.1 The hero — green from the vat, blue in the air

*The commission: a natural-indigo studio, "Vat No. 3", selling
dyed-to-order cotton and linen; the home page runs hero → the cloth
(product pieces) → the signature garment → the craft → figures →
record → commission → confession. Declared ceilings: pieces at
stage 3, cards at stage 2, garment to stage 4, footer resting at
stage 4.*

- **The composition (§6.12).** First screen: undyed ground, the line
  nav hung across the head (§6.11), the cloth panel centred over the
  vat band's surface line, the band deep `--vat` with its mote field
  suspended in it. The headline on the panel: "Cloth, dipped in
  **indigo**." — the oxidising word the sentence means (§6.2). The
  apparatus beneath the standfirst: "EST. 1987 · VAT No. 3 · CLOTH
  DIPPED TO ORDER".
- **The ceremony (§6.1).** Fonts ready at t≈140ms: the panel lowers
  900ms into the band, dwells 250ms, rises green from its first
  visible frame; the headline prints through its mask as the panel
  clears the surface line; oxidation runs to t≈2800, the word
  "indigo" turning letter by letter from t=2850, done by ≈3600. A
  visitor who never scrolls has still received the whole thesis:
  cloth went in white, came up green, and is blue now — and so is
  the word.
- **Scroll timeline.** 0–80px: the band's parallax (0.92×) is the
  only movement; the swatch (§6.4) sits undyed on the bench. The
  first piece's top crosses 80%: it hangs (§6.13's grammar at
  section scale) and the reading — and the dyeing — begins.

### 8.2 Mid-page — the garment's nine dips

*The same page, mid-descent: the signature piece is the Apprentice
Shirt, whose true record (§6.17) is nine dips across three days in
Vat No. 3.*

- **Entry.** The pin region engages: the shirt's framed photograph
  sticks, its story column beside it. Beat one is already read:
  "DAY ONE — FIRST DIP. THE CLOTH CAME UP GREEN AND THE VAT WAS
  JUDGED ALIVE." The frame's tint rests at stage 1; the counter
  (§6.16's grammar at piece scale) reads 1 DIP.
- **The beats.** The visitor scrolls the pin: at q=0.38 the tint
  crossfades 900ms to stage 2 and the counter steps to 5 as beat
  three inks — "DAY TWO — FIFTH DIP. THE BLUE HELD AT THE SEAMS."
  At q=0.78, beat five: stage 4, counter 9, "DAY THREE — NINTH DIP.
  HUNG TO CURE." The shirt they can buy is the shirt whose making
  they have just scrolled through, at the depth their reading gave
  it.
- **What the visitor feels.** Patience, repaid. The pin is long
  (320vh) because three days is long; the colour arrives in the
  order the work did. Nothing asked for attention — the story and
  the tint are the same fact at two sizes.

### 8.3 Conversion — commission the second dip

*The same page's end: the commission form (§6.14), reached after
the record (§6.17). The visitor dipped the hemp cloth's card twice
by hand in the listing above (§6.9).*

- **Arrival.** The form opens pre-set: the hemp line chosen, and
  its session line stated — "THE PIECE YOU DIPPED TO 2, BY YOUR
  HAND" — because the map remembers and the form is the map's other
  printing. The ladder offers stages 1–3 for hemp (its record shows
  three is its honest ceiling; stage 4's line is absent, not
  disabled-and-teased).
- **The choosing.** The visitor picks the second-dip line: its
  swatch dips 600ms through its green flash to first blue, and the
  days line updates from the record — "SECOND DIP — 2 DAYS IN THE
  VAT HOUSE". They mistype the direction (no @): on blur the rule
  holds its ink and the record notes beneath, in Gothic: "That
  direction will not carry — check the address before we enter it
  in the book." (§12's error voice: a fact about addresses, not a
  scolding.) They correct it; the note clears. They press COMMISSION
  THE DYEING: the button stitches down, and on success the form is
  replaced by a cloth panel oxidising to the second dip, lettered
  "COMMISSION No. 214 — SECOND DIP, FOUR METRES, ENTERED IN THE
  RECORD."
- **Failure rehearsed.** If the post fails, nothing they wrote is
  cleared; the note above the form reads "NOT ENTERED — THE VAT
  HOUSE COULD NOT BE REACHED. YOUR WORDS ARE KEPT ABOVE." and the
  ladder keeps their stage. A visitor who read a garment's whole
  biography to reach this form is never sent back to undyed by a
  network blink (§10, blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The blue website.** Sections in graded blues with ordinary web
   content poured in, dip counts as decorative labels. *Cure:* §1's
   law and §6.3 — every stage is a counted state with a locked
   pairing; if a section's blue could be set in a style guide
   instead of earned in the session, the build is paint, not dye.
2. **Green as a success colour.** Checkmarks, "in stock" dots and
   confirmation states in the fresh-dip green. *Cure:* §1/§5 —
   green is the transit, the not-yet; success in this theme is a
   record entry (§6.14/§6.17), and §11 refuses the toast that would
   carry it.
3. **Invented dip counts.** "12 dips" beside a stock product photo
   because twelve sounded artisanal. *Cure:* the batch record
   (§6.17) — every printed count has a row, and §10 gate 2 audits
   three of them by hand against the maker's real book.
4. **Oxidation everywhere.** Every heading turning green→blue, every
   card oxidising on entry, until the page is a chemistry
   screensaver. *Cure:* §3 law 5 and §5 — one oxidising word, dips
   on counted events only. The chemistry is rationed so it stays
   legible as an event.
5. **The vat as a footer-coloured band pasted under every hero.**
   *Cure:* §4/§7 — one vat band, on the home hero; interior pages
   hang a title piece. A vat under every page is a swimming pool.
6. **Re-dip farming.** Sections engineered short so visitors rack up
   dips by wiggling the scroll. *Cure:* §6.3's arming rule — full
   exit, 40% re-entry, one dip per exit — plus ceilings; the ladder
   rewards reading, not oscillation, and §10 gate 8 rehearses the
   wiggle.
7. **Dip state as a paywall.** Content revealed only after a section
   reaches a stage ("dip three times to read"). *Cure:* §5's safety
   inheritance — dip state is cosmetic; text contrast is locked per
   stage and nothing waits on a dip to be readable. A build that
   gates content behind dyeing has confused the record with a lock.
8. **The confession with a borrowed number.** A footer that prints
   a plausible N it did not count. *Cure:* §6.10 — the number is
   rendered from the session map at entry, the zero wording exists
   and is used, and gate 2 recounts it.
9. **Rounded, floating cards on a pale background.** *Cure:* §4 —
   pieces hang on a line, square-cut, pegged; a card that floats has
   fallen off the line and taken the layout's grammar with it.
10. **Percentages of blue.** "87% dyed" progress, "indigo-rich"
    sliders. *Cure:* §3 law 4 — dips are counted, stages are named;
    the theme's quantities are integers with ledgers, never
    proportions with adjectives.
11. **Marquee washing lines, blur reveals, tilting cards.** Any
    motion §5 refuses, smuggled back in. *Cure:* the refusal list is
    part of the gate (§10, item 11).
12. **Session amnesia theatre.** A "welcome back" that pretends
    yesterday's dips persisted. *Cure:* §6.3 — the cloth is washed
    between visits and the page says nothing about it; honesty
    includes the session's edge.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **Dip-law audit.** Every resting stage on the page traces to a
   counted event (a §6.3 re-entry, a §6.9 click, a §6.6 beat, a
   declared resting state in the survey), and every printed dip
   count traces to a batch-record row (§6.17). An unearned shade or
   an unrowed count fails.
2. **Confession recount.** In a test session with a scripted scroll
   (known completions, re-dips and hand-dips), the footer's number
   (§6.10) equals the hand-counted total, and its itemised tally
   matches §6.4's and §6.9's counts exactly.
3. **Three-printings agreement.** A product's stage and count agree
   across its card (§6.13), its detail page (§7) and its batch row
   (§6.17) at every point in a scripted session, including after
   hand-dips. The craft section's exemption from §6.3 is declared
   and its ground is owned by §6.7 alone.
4. **No stranded content.** With JS disabled, the whole page reads:
   pieces at resting states, counters printed from the record, form
   working, footer in its fallback wording. With JS on and the loop
   killed, every watchdog (§6.1's 3000ms, §6.3's 1600ms, §6.7's
   1400ms) fires and settles its surface.
5. **Transit contrast audit.** At every frame of a sampled dip
   (hero, section, card), text pairings follow §5's transit rule:
   ink or tenth over green (≥4.81:1), flip at the verified midpoint,
   locked pairing at rest. Cloth text over green at any frame fails.
6. **Hem clearance.** §6.8's hem at full rise never reaches the
   lowest text line of any card at any breakpoint (§6.13's upper-55%
   layout law, checked with real catalogue names at their longest).
7. **Form-keeping.** A failed submit (simulated network error)
   leaves every field, the chosen stage and any §6.9 pre-set exactly
   as the visitor left them, with §12's failure note. Any build that
   clears the form on error fails.
8. **Anti-farming rehearsal.** Scripted scroll oscillation on a
   section boundary for 30 seconds produces at most one dip per
   full exit + 40% re-entry cycle, and none without a full exit.

**Standard (must pass, fixable in review):**

9. Density falls with descent (§4): hero one piece + vat, garment
   alone on its line, footer holding confession + record totals
   only.
10. Exactly one pin (§6.6), one ambient loop (§6.5), one oxidising
    word (§6.2); §5's refusal list honoured — no marquee, no blur
    reveals, no kinetic type beyond the word, no parallax beyond the
    vat pair.
11. Ceilings declared in the survey and enforced: cards ≤ stage 2,
    pieces ≤ stage 3 unless recorded otherwise, stage 4 only per
    §2's reservation.
12. The first dip runs once per session; a returning visitor's hero
    paints at rest, and the apparatus record line (§6.1's reduced
    variant wording) is present under reduced motion.
13. Every interactive element is ≥44px; focus shows §6.8's hem or
    §11's ring; focus never triggers a dip.
14. Mobile: pin cut (§6.6), swatch as bar chip (§6.4), dip strips
    48px (§6.9), record as stacked ledger (§6.17).

## 11. Component inventory

Every component a real Indigo Vat site needs, with its themed
treatment. Components the theme refuses are listed with their
in-theme replacement — a refusal without a replacement is a gap,
not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | Stitch press: the current ground's locked pairing, 2px stitched rule beneath the label; presses 2px on `--ease-stitch` (§6.14). On pale grounds, vat ground with cloth label; on deep grounds, cloth ground with vat label. |
| Secondary button | Ruled line button: transparent, 2px bottom rule in the ground's text colour; hover dips the rule one stage (§6.8's grammar at line scale). |
| Dip button | §6.9's control: apparatus label, counter output, stage chip. A component in its own right — no other button on the site may imitate its shape. |
| Text input | Inscription line (§6.14): apparatus label above, 2px rule below, no box; focus inks the rule vat with a stitch dash. |
| Textarea | Ruled sheet: lines every 29.75px (the body line unit ×1.75), Gothic 17px. |
| Select | Refused. Choices are seam lists: ruled radio lines (§6.14's cloth list generalised) — a dye house lays its cloths out; it does not hide them in a dropdown. |
| Checkbox | Stitch box: unfilled square in thread; filled = a stitched cross in the ground's text colour. |
| Radio | Swatch line (§6.14's ladder grammar): the chosen line's swatch dips to its state; the dot is a peg tick on the line. |
| Toggle / switch | Refused. The vat has states of cloth, not switches; use two seam lines (On the line / In the vat) as radios. |
| Card | Cloth-piece card (§6.13): hung, pegged, woven frame, dip foot. |
| Table | Batch record (§6.17): real table, apparatus headers, no zebra striping — row grounds are the table section's stage, uniform. |
| Tabs | Refused. Depth is not tabbed; pieces are scrolled, pinned (§6.6) or indexed by the line nav (§6.11). A build needing tabs has two lines arguing — string them as two sections. |
| Accordion | Hung fold: a piece whose lower half unfolds downward like cloth unpegged at one end — the fold drops over 350ms `--ease-dip` and hangs; the heading gains a stage tick. One fold open per line. |
| Modal / dialog | The commission's confirmation (§6.14) is inline, not modal. The theme's only dialog is the record excerpt on a detail page (§7): a hung panel over a vat-deep scrim at 82%, closed by its own peg button. |
| Toast | Refused. News from the vat is recorded, not toasted: transient confirmations appear as a one-line entry in the batch record's session block (§6.17) and in the confession's tally (§6.10). |
| Tooltip | Refused. Explanation lives in apparatus and record lines (§6.17); a count that needs a tooltip needs a better record line. |
| Badge | Stage chip: apparatus text on the stage's ground — "SECOND DIP" — the badge states a piece's depth, never a marketing claim ("NEW" is an undyed word and is banned, §12). |
| Alert | Undyed band: a stage-0 seam cut into the current ground, ink text, stitched left rule, §12's error voice, persistent until resolved. On deep grounds the band is cloth — an alert is a piece that has not been dipped, and it reads that way. |
| Pagination | Line pagination: "Further along the line" / "Back along the line" links lettered with the next line's first piece — never numbered pages; a line is continuous. |
| Progress bar | Refused. Progress is the margin swatch (§6.4). |
| Spinner | Refused. Waiting is undyed cloth (§6.15). |
| Skeleton | §6.15's undyed pieces with stitched labels. |
| Search | The record search: a single inscription line in the header; results are returned as pieces on a line (§6.13's anatomy) with their records — search results in this theme are a line of cloth, not a list of links. |
| Breadcrumbs | Replaced by the line nav's current tab (§6.11) plus the swatch: the visitor's position is a place on the line and a depth, not a trail of pages. |
| Skip link | "Skip to the cloth" as a plain ink link appearing on first focus above the line. |
| Focus ring | 2px outline in the ground's text colour, offset 3px; on cards, focus also raises §6.8's hem. On deep grounds the ring is cloth; on pale, vat. |
| Divider | The line itself (§4) or, within a piece, a stitched rule (dashed 2px in `--thread` / cloth at 40%). Wavy SVG dividers are refused — that is a different theme's water, and this theme's water is in the vat, where it belongs. |

## 12. Content & copywriting voice

Two voices, cast like the type. **The Dyer** writes apparatus: dip
counts, stage names, vat numbers, labels — Gothic, uppercase, terse,
every figure tallied. **The Record** writes prose: beat stories,
explanations, errors, confirmations — Gothic sentence case (Mincho
sets names and headings only), plain and patient, the voice of
someone writing up the day's dyeing for whoever comes to the vat
next. The voices never swap: apparatus never sentences, the record
never shouts.

**Headline style.** The cloth and its chemistry, stated. ✓ "Cloth,
dipped in indigo" / "Nine dips, three days, one shirt". ✗ "Dive into
a world of blue!" (exclamation, a dive metaphor the theme refuses —
cloth is lowered, never dived — and a claim with no count in it).
Exclamation marks are banned from the whole theme: dyeing is not
excited.

**Label style.** Apparatus: noun + count. ✓ "SECOND DIP", "9 DIPS ·
3 DAYS · VAT No. 3", "FOUR METRES — HEMP". ✗ "Stage 2 of 5", "87%
dyed" (percentages are banned, §3 law 4 — a dip is counted, not
proportioned).

**Error voice.** A dye-house fact, stated plainly, with the way
back. ✓ "That direction will not carry — check the address before
we enter it in the book." ✓ "NOT ENTERED — THE VAT HOUSE COULD NOT
BE REACHED. YOUR WORDS ARE KEPT ABOVE." ✗ "Oops! Something went
wrong 😞" (the vat house has no "oops", and no emoji survives the
dye).

**Empty-state voice.** ✓ "This cloth was never dipped." / "No cloth
in the record matches that name." ✗ "No results found. Try being
less specific?" — the record does not blame the visitor for the
book's gaps.

**Confirmation voice.** ✓ "COMMISSION No. 214 — SECOND DIP, FOUR
METRES, ENTERED IN THE RECORD." ✗ "Success! 🎉 Your order is in!"
— a confirmation is a ledger entry, not a celebration.

**Banned words:** amazing, revolutionary, seamless, dive in, dip
into (as a metaphor for browsing — dipping is literal here or it is
nothing), unlock, supercharge, NEW (as a badge), oops, vibrant
(the theme's blues are deep, not vibrant).
**Owned words:** dip (counted), stage (named, never numbered in
apparatus), vat, piece, the line, hung, oxidise, cured, by your
hand, entered in the record, never dipped.

**Fixed strings (verbatim, do not paraphrase):** the first dip's
record line — "FIRST DIP — GREEN FROM THE VAT, BLUE IN THE AIR.";
the confession's frame — "This footer took ten dips. Your visit
gave this page N." (N rendered, never typed); the zero confession —
"Your visit gave this page 0. The cloth above is still undyed.";
the 404 heading — "This cloth was never dipped."; the form failure
note — "NOT ENTERED — THE VAT HOUSE COULD NOT BE REACHED. YOUR
WORDS ARE KEPT ABOVE."

## 13. Full-page scroll choreography map

The home dyeing, top to bottom. Every beat in order; instruments run
continuously beneath the beats (swatch §6.4 standing by, re-dip
arming §6.3 listening for exits, motes §6.5 drifting while the hero
lives).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | First dip (§6.1): panel lowers, rises green, oxidises; word turns (§6.2) | The making, witnessed |
| 2 | 0–80px | Vat parallax only (0.92×); swatch undyed on the bench | The liquid is deep; nothing has been read yet |
| 3 | First piece hangs | The cloth section hangs on its line (§6.13 grammar at section scale) | Work laid out |
| 4 | Pieces in view | Cards centre, frames deepen (§6.13); hover tests and hand-dips live (§6.8/§6.9) | Inspection, then commitment |
| 5 | First piece completes | Swatch takes its first dip (§6.4) | The reading is dyeing something |
| 6 | Garment pin engages | Story beats advance the tint (§6.6) | Three days, scrolled |
| 7 | Pin releases | Buy block; the garment at stage 4 | The finished piece |
| 8 | Craft section | Shibori draws; ground scrub-dips (§6.7) | The technique, performed |
| 9 | Figures band | Dyer's figures count (§6.16) | The house's arithmetic |
| 10 | Record section | Head rule draws; the audit stands (§6.17) | The workings, shown |
| 11 | Commission | The form on undyed cloth (§6.14), pre-sets honoured | The ask, on clean paper |
| 12 | Footer enters | Confession counts and lands (§6.10) | The visit, confessed |

**Reverse pass.** Scrolling up: stories re-tell (§6.6's tint
lightens beat by beat, §6.7's rings un-draw), hangings stay hung,
figures stay counted — and §6.3's stages *hold*, because a dyeing is
not undone by walking back past the vat. The page going up is paler
in its diagrams and stories, identical in its records. That asymmetry
is the theme's grammar, and §6.6/§6.3 state it in their own sections
so no builder harmonises it away.

**Jump-scroll catch-up.** Anchor jumps and flings: pieces passed are
hung without ceremony, the garment lands on the beat nearest the
landing point, the shibori lands drawn or undrawn by zone side, the
swatch jumps to the true completed count. No dip is owed to a
teleport (§6.3's arming rule governs: a fling is not a re-entry).

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 780KB, of which images ≤ 420KB |
| Fonts | Shippori Mincho (2 weights) + Zen Kaku Gothic New (2 weights) ≤ 150KB, `font-display: swap` |
| JS | ≤ 70KB gzipped (one loop, two observers, dip map, form) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the first dip's timers are sliced per beat |
| Dip latency | Any triggered stage change settled ≤ 1600ms after trigger (watchdog law) |
| Active colour ramps | ≤ 3 concurrent (one section dip, one card dip, the swatch) — a fourth request queues behind the oldest |
| Motes | 26 particles, ≤0.3ms/frame (§6.5) |

**Cut order when the budget is exceeded** (cut in this order, record
each cut in the build notes):

1. Dye motes (§6.5) — to their static painted field, then gone.
2. Vat parallax (§6.12) — the band stills behind the panel.
3. Card frame deepening (§6.13) — frames rest at their record tint.
4. The line-pass transition (§6.15) — navigation becomes instant
   with the §6.11 tab flash.
5. Hover-dip travel (§6.8) — hems apply instantly (the reduced-motion
   treatment) for all visitors.
6. Garment tint crossfades (§6.6) — tints step at beat boundaries;
   the pin and story stay.

**Never cut:** the dip watchdogs, the locked stage pairings, the
margin swatch, the batch record, the confession's true count, any
reduced-motion variant. A build that cuts the honesty to keep the
ambience has painted the cloth and called it dyed.

## 15. Build-order checklist

1. Survey first: fix the pieces, their order on the line, each
   piece's ceiling and its one-sentence reason, each product's real
   record (dips, days, vat) and the data object the record, cards
   and figures will all render from. Write the survey; everything
   else is generated from it.
2. Build the static dye house: all pieces hung at resting states,
   counters printed from the record, prices legible, form working —
   with no JS. This is the site; the rest is dyeing.
3. Set the palette tokens, the ladder and the pairing law (§2);
   audit contrast at every stage, including §5's transit pairings,
   before any motion exists.
4. Set the type scale and the stage line-heights (§3 laws); set the
   oxidising word and verify it fits one line at every breakpoint.
5. String the line (§4): bench, rail, vat band, hanging geometry;
   author the woven frame and peg marks once, reuse everywhere.
6. Build the instruments from the data object: line nav (§6.11),
   margin swatch (§6.4), dyer's figures (§6.16), batch record
   (§6.17), footer confession (§6.10) with its fallback wording.
   Verify the three-printings agreement by reading all of them
   against the object.
7. Add the shared loop; wire the vat parallax (§6.12) and the
   garment pin (§6.6) with beat boundaries from the real story.
8. Add stateful re-dipping (§6.3) with its arming rule and 1600ms
   watchdog; rehearse the anti-farming oscillation (§10 gate 8).
9. Add the hand: hover dip (§6.8) with hem clearance checked against
   the longest real product names, then click dip (§6.9) writing to
   the one session map.
10. Add the surface ceremony: first dip (§6.1) with its 3000ms
    watchdog and session flag, oxidising word (§6.2), hero
    composition (§6.12).
11. Add the craft scrub (§6.7); declare its exemption from §6.3 in
    the survey and verify no other system dyes its ground.
12. Build the commission form (§6.14) with its ladder from the
    record's real durations and error-keeping rehearsed against a
    simulated network failure.
13. Add figures' counting (§6.16), skeleton and line pass (§6.15),
    the never-dipped page (§6.18).
14. Run the full gate (§10) including the confession recount with a
    scripted session; sign-off by a non-builder, as the dyer who
    judges the vat is never the hand that dipped the cloth.
