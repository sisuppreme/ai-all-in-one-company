# 52. Fog Harvest — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A coastal-fog site where content condenses: sections
begin obscured in fog and become legible as droplets gather, so
reading the page feels like a window clearing. Palette anchors:
fog white `#EDEEEC`, mist `#C9CFCC`, wet sage `#7E8C8A`, cypress
dark `#3C4A48`, rusted tank `#B4552D`. Type: Newsreader (display)
+ Source Sans 3 (body). Sections are layered as fog banks over
cypress-dark content; a fog-collector mesh progress diagram in
the margin fills droplet by droplet as the reader advances; the
hero headline waits behind fog until a circular hand-wipe clears
it; the headline's final letter drips once. The site's credit
line, kept verbatim from the original entry: *"this page, like
our vineyard, is watered by fog."*

## 1. Concept & world

Fog Harvest is the website of people who farm weather. On the
dry coasts where this theme lives — Chungungo in Chile, the
Namib fringe, the Canary laurel slopes — the rain does not fall,
so the water is caught sideways: great nets of woven mesh stand
on the ridge, the camanchaca rolls in off the cold sea, droplets
condense on the strands, merge, run down into a gutter, and a
vineyard drinks. The page performs exactly that physics on its
own content. Nothing on a Fog Harvest page is revealed by
appearing; it is revealed by *condensing*. A section arrives the
way a headland arrives through morning fog — a softness, an edge,
then the hard detail — and it becomes fully legible at the
moment the reader reaches it, because clarity on this page is
not a decoration applied to content, it is the harvest itself:
the reader's attention is the mesh, and what gathers on it is
the text.

The world the page performs is a pane of glass on a fog morning,
wiped by a hand. The hero waits behind a fogged pane until the
wipe clears it (§6.1). Cards are smaller panes, wiped by the
visitor's own pointer (§6.9). Sections condense as they travel
to the reading line and — this is the discipline that separates
the theme from a blur effect with a marketing department — they
never re-fog behind the reader into illegibility while they are
still on screen, and no text anywhere is ever asked to be read
through moving fog. Down the margin, the instrument of the whole
fiction stands drawn: the collector mesh (§6.4), filling droplet
by droplet as sections are completed, so the page's progress
indicator is not a bar but a water level — the reader has
harvested the page by reading it, and the mesh shows how much.

**The theme's one law: fog is a crop, not a curtain.** Two
clauses, both audited by the gate. (1) *Fog never performs.* Fog
may exist only ahead of the reading position (sections not yet
reached), behind it as settled weather (the static frame, the
resting banks), or in the act of clearing at the reading line
itself. At the reading line, clarity is total — clarity value
1.0, blur 0px, opacity 1 — and it is *guaranteed*, not hoped for:
every obscured state is JS-armed over complete printed content
and carries a watchdog that snaps it clear (§6.2), so a Fog
Harvest page with dead JavaScript, a stalled loop, or a flung
scroll is a clear page, merely unperformed. A build in which any
sentence can be caught mid-blur at the moment its reader arrives
has used fog as a curtain and fails. (2) *Every litre is
accounted.* Every figure the page prints — litres harvested,
fog-days, square metres of mesh, the tank level in the footer —
is a printing of one declared yield object (§6.6): the mesh
area, the mean capture rate, and the season's fog-day count,
with the arithmetic printed beside the figures. A litre that
cannot be traced to that object is invented weather, and
invented weather is the theme's one unforgivable slop.

**Best-fit sites and audiences.** Fog-harvest and atmospheric-
water projects first, literally: collector cooperatives,
vineyards and farms watered by fog, desalination and
water-technology firms whose product is patience. Then any
business whose truth is *things emerging slowly from obscurity*:
a coastal hotel or retreat that sells the morning the fog lifts;
a lighthouse or harbour authority; a tea or coffee grower in
cloud forest; a weather service, observatory or climate
research station publishing field notes; a perfumer or distiller
built on condensation (the still is a fog machine with intent);
a conservation trust for cloud-forest or redwood ecosystems,
where fog drip is the ecology. The audience it suits reads
slowly and trusts slowness: people who will watch a section
condense because the condensing *is* the brand's argument — we
wait for water; we do not perform urgency. Conversion on such
sites is a visit booked, a case ordered, a membership joined —
acts taken after the fog has cleared, never during.

**When NOT to use it.** Not for anything that must be scanned
fast: news, listings, comparison tables beyond the one licensed
season table (§6.14), dashboards, checkout flows where a blurred
millisecond reads as a bug. Not for emergency, medical or safety
information — content that must be legible at first pixel cannot
wait for weather. Not for sites whose content arrives in a feed:
condensation is an authored, per-section act with a declared
clarity curve, and forty feed items fogging in sequence is a
weather system, not a page (§9, failure 7). Not where the client
cannot supply real yield figures: §6.6's counters print a
declared model or they do not print, and a fog page over invented
litres is a curtain over a lie. Not on text-heavy legal or
compliance pages: the law's guarantee (total clarity at the
reading line) is achievable, but counsel will not enjoy
defending a blur, however capped.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme, and
the gate greps built CSS for undeclared hex values.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--fog` | `#EDEEEC` | Fog white — the page's ground, the fog layer itself, light surfaces | ~44% of viewport area | Carries `--ink` at **12.45:1**, cypress at 7.96:1, `--sage-deep` at 5.87:1, `--rust-deep` at 6.27:1. As a *layer* over content it is the veil (§6.2), never a text colour. |
| `--mist` | `#C9CFCC` | Mist — the second surface: un-cleared card stock, skeleton tone, bank mid-tone | ~18% | On fog white 1.36:1 — a surface distinction only, never text on fog. Carries `--ink` at 9.17:1 and cypress at 5.86:1 when it is the ground (skeleton labels, §6.16). |
| `--sage` | `#7E8C8A` | Wet sage — droplets, mesh strands, graphical weather | ~10% | On fog white **3.00:1** — graphical and ≥24px display only, never body text (§3 law 3). On cypress 2.65:1 — forbidden pairing, ruled graphical-nothing: sage is never set on cypress. |
| `--cypress` | `#3C4A48` | Cypress dark — the content ground beneath the banks, dark sections, footer | ~24% | Carries fog white at 7.96:1 and mist at 5.86:1. Carries rust at 1.89:1 — **forbidden**: the tank never prints on the trees (§9, failure 9). |
| `--rust` | `#B4552D` | Rusted tank — the one warm accent: the tank, the yield figures' marks, the form's seal | ≤2% (rationed, §5) | On fog white **4.22:1** — large text and marks only; small text uses `--rust-deep`. On cypress forbidden (above). |
| `--ink` (derived) | `#232B29` | Cypress-black — body text on light grounds | — | On fog white 12.45:1; on mist 9.17:1. The reading colour; fog is weather, ink is print, the two never swap roles. |
| `--cypress-deep` (derived) | `#2A3533` | The grove at night — footer ground, the dry page's ground (§6.18) | — | Carries fog white at **10.90:1**, mist at 8.02:1, `--rust-pale` at 4.73:1 (large/labels only). |
| `--sage-deep` (derived) | `#4E5E5B` | Dried sage — the only sage licensed for text | — | On fog white 5.87:1 — captions, apparatus, the log's voice (§12). Droplets at rest render in this tone deepened by their specular (§6.3). |
| `--rust-deep` (derived) | `#8F3E1F` | Tank rust, dried — small text in the accent: errors, the credit's figures, form apparatus | — | On fog white 6.27:1. Fresh marks (the tank fill, the seal) render in `--rust`; their printed captions use the deep tone. |
| `--rust-pale` (derived) | `#D98B66` | Rust in fog-light — the accent's voice on dark grounds | — | On cypress-deep 4.73:1 — labels and ≥18px text on the footer only; never body text, never on cypress (3.46:1). |
| `--veil` (derived) | `rgba(237,238,236,.86)` | The fog layer at working strength — hero veil (§6.1), card veils (§6.12) | — | A layer, never a colour: it sits over complete content and its opacity is a scrubbed value (§5), not a design choice made twice. |
| `--droplet` (derived) | `#4E5E5B` + specular `#FFFFFF` at 55% | Water on the page — corner beads, runs, mesh droplets, the click droplet | — | Graphical only. A droplet is drawn as a sage-deep body with one specular point; a droplet without its specular is a grey dot and fails §9, failure 5. |

**Usage discipline.** A page is roughly half fog and mist,
a quarter cypress, a tenth sage weather, and rust as a rounding
error with a tank. The ratio is audited by screenshot sampling
in the gate (§10): rust pixels above 3% of any viewport means
the tank has become a colour scheme. Fog white is both the
ground and the weather — the one token that is a place and a
condition — which is why the veil's opacity, not its colour,
carries all the meaning.

**Dark behaviour — the page does not invert; the fog comes in
for the night.** Fog Harvest is a light theme by physics: fog is
bright. Under `prefers-color-scheme: dark`, the page does not
pretend the fog went black. Light sections keep `--fog` grounds
(fog at night is still the brightest thing on the coast road);
the cypress sections deepen to `--cypress-deep`; the banks
(§6.11) render at 60% of their light-scheme opacity because
night fog reads thinner against dark ground; droplets keep
their sage-deep bodies and their specular drops to 40% (less
light to catch). Every text pairing above is unchanged in class
— fog grounds still carry ink at 12.45:1, cypress-deep carries
fog white at 10.90:1 — so no ratio in the table moves. A build
that "adds dark mode" by inverting fog white to charcoal has
made the weather out of the wrong material and fails §9.

## 3. Typography

**Faces.** Newsreader (display, numerals, the credit line) —
chosen because its soft, slightly wet serif reads like print
seen through glass that has *just* cleared: high detail, no
hardness. Source Sans 3 (body, apparatus, form) — the working
sans of the log-book. No third face exists in the theme; the
mesh diagram's labels (§6.7) are Source Sans 3 at caption size,
because an instrument is labelled by the hand that keeps the
log, not by the display face.

**The scale** (desktop; §6 breakpoint tables carry the smaller
sizes):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Hero display | Newsreader 480 (opsz auto) | 64px / 1.04 | −0.015em | The wiped headline (§6.1); max 9 words (§12) |
| Section display | Newsreader 480 | 40px / 1.12 | −0.01em | One per section, at the section's hard-detail edge (§4) |
| Sub-display | Newsreader 400 italic | 26px / 1.3 | 0 | Standfirsts, the credit line's register |
| Body | Source Sans 3 400 | 17px / 1.58 | 0 | Measure 62–68ch (§4) |
| Body small | Source Sans 3 400 | 15px / 1.55 | 0 | Card body, table cells |
| Caption / apparatus | Source Sans 3 500 | 13px / 1.45 | +0.01em | `--sage-deep` or `--ink`; source lines (§12) |
| Data numerals | Newsreader 500 | 44px (counters) / 17px (inline) | 0, tabular lining | The yield figures (§6.6); never Source Sans |
| Mesh labels | Source Sans 3 600 | 11px / 1.3 | +0.06em, uppercase | Diagram labels only (§6.7) |

**Five type laws.**
1. **Numerals are Newsreader, always.** The yield is the site's
   headline act, so its figures wear the display face — a litre
   count in the body sans reads as a spreadsheet that wandered
   onto a vineyard. Inline data in prose ("212 fog-days") is
   Newsreader 500 at body size, lining figures.
2. **Type never moves to clear.** Condensation is blur and
   opacity only (§6.2): no size, weight, tracking or position
   change during a clear, so a section's layout at 60% clarity
   is pixel-identical to its layout at 100% — zero CLS is a
   law, not a metric. The single exception is the hero's drip
   (§6.1), which happens *beneath* the final letter, in space
   the layout already reserves.
3. **Wet sage never sets text under 24px.** At 3.00:1 on fog
   white, `--sage` is weather and graphics; text in the sage
   register is `--sage-deep` (5.87:1) at any size, or `--sage`
   only at display sizes where it functions as an image.
4. **Nothing is read through fog.** Type under a live veil
   (§6.1 before the wipe, §6.12 card veils at rest) is either
   decorative display type whose printed twin sits beneath at
   full contrast (the hero's structure, §6.1), or it is not
   body text. Body copy's first fogged state is 60% clarity
   with the 40% floor (§6.2) and it reaches 1.0 at the reading
   line — the law of §1 measured in the type layer.
5. **Italics are water.** Newsreader italic is reserved for
   things the fog said: standfirsts, the credit line, the
   season table's weather notes (§6.14), the dry page's single
   line (§6.18). Apparatus, errors and labels are never italic —
   the log does not murmur.

## 4. Layout language

**The bank and the clearing.** Every section is built as two
strata: a *bank* — a fog-gradient field 120–200px tall at the
section's head, fog white at full strength at the top edge,
thinning to nothing at its foot — and a *clearing* beneath it,
where the section's hard detail lives at full contrast. The
bank is where the section's weather is; the clearing is where
its facts are. A section that fogs its clearing has broken §1;
a section with no bank is a page from another theme that has
wandered in. On cypress sections the geometry inverts in value
only: the bank is a mist gradient over the cypress ground,
thinning downward into the dark clearing.

**Grid and measure.** One column of content at 62–68ch,
centred, with two margin instruments that never enter the
measure: the **collector rail** at ≥1200px — a 76px-wide margin
column on the left holding the progress mesh (§6.4) and, on the
science section, the drawn diagram's margin half (§6.7) — and
the **tank gauge** (§6.17) in the footer. Between 768–1199px
the rail collapses to a 48px strip carrying the mesh at reduced
cell size; below 768px the mesh leaves the margin and sits as a
single row above the footer (§6.4 breakpoints). Whitespace is
the theme's shade: sections breathe in fog, so vertical rhythm
is generous — 96px between sections on desktop, 64px tablet,
48px mobile — and the pause *is* the bank of the next section,
never empty padding stacked on top of it.

**Density law.** Fog is rationed by area: at any scroll
position, live (animating or scrubbed) fog may cover at most
35% of the viewport, and text-bearing fog — the condensing
sections' veils — at most 20%. The banks at rest, the hero
veil before its wipe, and the pinned vineyard's fog (§6.5) are
counted in the 35%. A page that needs more fog than the ration
has too many sections above the fold or a pin running long;
the cure is in §9, failure 7, and it is editorial, not
technical.

**Section choreography.** Sections alternate ground in a
declared order — fog, fog, cypress, fog, cypress — never three
dark in a row (the grove closes in) and never a rust ground
anywhere (the tank is an object, not a surface). Each section's
display line sits at the bank's foot, the exact pixel row where
its fog reaches zero: the headline is the first hard detail the
weather gives up, and the layout draws the eye to the hand-over.

**The reading line.** The theme's master measurement: a
horizontal line at 55% of viewport height. Clarity curves,
droplet triggers, counter firings and mesh fills are all keyed
to elements crossing it (§5). It is not drawn. A build that
draws it — a debug hairline left in, a progress hairline
borrowed from another theme — has confused the instrument with
the furniture; the collector mesh is the only progress the
visitor is shown.

## 5. Full motion system

Five named easings, defined once, used everywhere; an element
that invents a sixth fails the gate's grep.

| Easing token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-wipe` | `cubic-bezier(.25,.7,.2,1)` | Quick contact, long glide — a hand crossing glass | Hand-wipe hero (§6.1), hover glass-wipe (§6.9), fog-roll transition (§6.16) |
| `--ease-condense` | `cubic-bezier(.45,.05,.25,1)` | Slow gather, firm arrival — droplets becoming a surface | Condensing sections (§6.2), speckle clear (§6.8), skeleton condense (§6.16), card veils |
| `--ease-drip` | `cubic-bezier(.55,.06,.68,.19)` | Gravity — starts reluctant, ends fast | Corner runs (§6.3), click droplet (§6.10), hero drip (§6.1), counter droplet (§6.6) |
| `--ease-drift` | `cubic-bezier(.45,.02,.55,.98)` | Near-sinusoidal sway — weather moving at weather speed | Fog banks (§6.11), vineyard fog edge (§6.5) |
| `--ease-settle` | `cubic-bezier(.25,.8,.35,1)` | A bead landing in a cell and resting | Mesh droplets (§6.4), diagram strokes' ends (§6.7), card rest (§6.12) |

**Durations ledger** (the theme's complete vocabulary; an
element may combine but not invent): hand-wipe 1600ms; hero
drip — form 700ms, fall 380ms; section clarity scrubbed (no
fixed duration; the scroll is the clock) with a 600ms
`--ease-condense` completion glide when the scroll stops
mid-curve; corner droplet swell 450ms, merge 200ms, run 900ms;
mesh droplet swell 450ms + settle 250ms; vineyard clear
scrubbed across a 150vh pin; counter count 1400ms, counter
droplet at +150ms after the litre figure lands; mesh diagram
draw 1800ms in build order; speckle clear 600ms; hover wipe
pointer-lerped, re-fog 800ms; click droplet run 620–900ms by
card height; bank drift 46s / 64s alternating cycles; fog-roll
transition 450ms in + 700ms thin; watchdogs 2400ms (hero),
1200ms (sections, cards, images), 3000ms (skeleton), 4000ms
(pinned scene).

**Every motion term, translated or refused.**
- *Scroll-triggered reveals* — condensation (§6.2): sections
  gather clarity as they travel; the trigger is position, the
  reveal is weather. Nothing fades up from below; fog thins
  where the reader stands.
- *Scroll-scrubbed animation* — section clarity, the vineyard
  clear (§6.5), bank parallax, the mesh fill (§6.4): all
  scrubbed from the one shared loop (§5, below).
- *Parallax* — fog banks drift at 0.92× against the content
  beneath them (fog lags the land; the land is what moves
  fast), capped at ±22px and clamped to authored overflow so
  a bank's edge can never open a gap at a section boundary.
- *Pinned sections* — exactly one: the long vineyard clear
  (§6.5), 150vh. A second pin is refused; a page gets one long
  clear, the way a morning gets one.
- *Masked reveals* — the hand-wipe's circular mask (§6.1) and
  the hover wipe's radial mask (§6.9). Masks always sit over
  complete content (§6.1's structure is the theme's
  constitution: the printed layer beneath is whole).
- *Blur-to-sharp* — the theme's native tongue, and therefore
  the most rationed: blur exists only as the *fog state* of
  §6.2 (cap 6px) and §6.1 (cap 14px on the veil layer, never
  on the text layer itself), always paired with the opacity
  floor (never below 0.40 under any circumstance, 0.55 at
  authored entry), and always with the scroll-end snap (§6.2).
  Blur anywhere else — a hover blur, a modal backdrop blur, a
  blurred hero photograph — is §9, failure 2.
- *Kinetic typography* — **refused** beyond the hero's single
  drip. Letters on a fog coast do not dance; the weather moves
  so the words can be still.
- *Marquee* — **refused.** Nothing on this coast travels
  sideways forever. The banks drift (§6.11) and return; that
  is the page's only ambient travel, and it breathes rather
  than loops a message.
- *Animated counters* — the harvest counters (§6.6): counted
  once, on centre, in Newsreader numerals, ending with a
  droplet. A counter that re-runs on scroll-back is a gauge
  pretending; §6.6's are latched.
- *Progress indicators* — the collector mesh (§6.4) is the
  only one. Percentages are banned from progress contexts
  (§12): the mesh *is* the fraction, filled in water.
- *Micro-interactions* — hover glass-wipe (§6.9), click
  droplet run (§6.10), wet-glass card tilt (§6.12), the form's
  droplet submit (§6.13).
- *Ambient loops* — the drifting banks (§6.11) only: two
  cycles, ≤0.5 opacity, paused off-screen and on hidden tabs.
  Droplets never loop; water that falls forever is a leak.
- *Page transitions* — the fog roll (§6.16): fog in to white,
  then thins onto the new page.
- *Reduced motion* — every element's variant, stated per
  element in §6; the global rule is the original entry's: **the
  page rests fully condensed and clear, fog only as a static
  frame.**

**The shared loop.** One `requestAnimationFrame` loop drives
every scrubbed value — section clarity, vineyard fog, bank
parallax, mesh fill state, hover-wipe centre — with a lerp
factor of **0.12** for scroll-scrubbed values: the original
entry's "muffled, fog-soft easing" implemented as physics, not
as scroll hijacking. Native scroll is never intercepted; the
loop reads position and eases the *weather* toward it, so the
content is always exactly where the reader put it and only the
fog lags, by design, at most a beat behind. The loop sleeps
when every scrubbed value is within 0.1% of target and when
the tab is hidden. Time-based acts (the wipe, the drips, the
counts) run on CSS transitions/animations or one-shot rAF
timers, never on the shared loop.

**The clarity function.** One function serves every condensing
surface, so two builders — or two elements — can never disagree
about how clear a thing is at a given scroll position. For a
section whose top enters at viewport fraction `p` (0 = top of
viewport, 1 = bottom): clarity `C = clamp((0.95 − p) / 0.50,
0.55, 1)` while the section travels the middle band, reaching
`C = 1` when its reading matter crosses the reading line
(§4). Rendered as `blur = 6 × (1 − C) / 0.45 px` capped at 6px
and `opacity = C`, with the floor enforced in the function
itself: no caller may pass a value that renders opacity below
0.40. The function is printed here because the gate tests it
(§10): sample a section at three scroll positions and the
rendered values must match the function to the pixel.

**Rust ration.** The tank is spent like water: per page, at
most the tank gauge (§6.17), the counters' droplet marks
(§6.6), the form's seal (§6.13), and error text in
`--rust-deep`. A page rendering more rust than that has made
a colour out of a container and fails §10's pixel audit.

## 6. Signature elements

### 6.1 The hand-wipe hero

- **What & why.** The hero headline sits behind a fog layer —
  backdrop blur 14px under fog white at 86% — until a circular
  clear patch, ~120px across, opens at the headline's centre
  and expands with an ease-out over ~1.6s until the whole line
  is legible, droplets beading at the patch's rim as it grows.
  It belongs because the wipe is the site's whole transaction in
  one gesture: a hand clears the pane, and what is behind the
  pane is the business. The fog is the medium the business
  harvests, so clearing it is the product story, told before a
  word of body copy is read.
- **Structure.** A real `<h1>` in Newsreader, complete in the
  DOM at full contrast from first paint — the printed layer.
  Above it, a veil layer (`aria-hidden`, `pointer-events:
  none`): a fog-white field at `--veil` strength with a radial
  mask whose clear centre is a CSS custom property (`--wipe-r`,
  0→160% of the headline's width), plus a rim ring of 9–14
  droplet dots positioned on the mask's edge circle, each a
  3–6px sage-deep bead with its specular (§2). The blur lives
  on a *duplicate* of the headline inside the veil
  (`backdrop-filter` is refused here — it blurs whatever is
  beneath, including the printed layer's edges at the rim; the
  duplicate-blur structure keeps the printed layer untouched).
  Beneath the final letter, a reserved 18px drip channel in the
  layout holds the drip bead (§3 law 2's licensed exception).
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage` — a returning visitor finds the pane already
  wiped), gated on `document.fonts.ready` raced against 800ms:
  wiping in a fallback face would misalign the rim droplets, so
  if fonts lose the race the hero ships clear. t=0: patch opens
  at the headline's optical centre, radius 60px. 0–1600ms
  `--ease-wipe`: radius grows to cover the line, decelerating —
  a hand slows as the wipe completes. Rim droplets bead at
  300–1200ms, each swelling 450ms `--ease-condense` as the rim
  passes its position. At 1600ms the veil is removed from the
  DOM (not merely faded — a lingering veil layer is a
  compositing cost and a lie). Then the drip: a bead forms
  beneath the final letter over 700ms `--ease-condense`,
  detaches, falls 380ms `--ease-drip` through the reserved
  channel, and lands with a 2px splash flatten. Once. It never
  repeats, on any visit, in any state.
- **States.** Fogged (JS-armed only) → wiping → clear (rest;
  veil absent). Hover/focus: none — the headline is not a
  control and does not re-fog for attention. Scrolled away
  mid-wipe: the wipe completes on its own timeline; the hero is
  clear when the reader returns. Focus entering the hero
  mid-wipe completes the wipe instantly (a keyboard visitor is
  never asked to wait for weather).
- **Content merge.** The wipe reveals the brand's actual
  headline — the `<h1>` and the page's subject — not a logo
  sting or an intro panel. The standfirst beneath waits at the
  bank's foot (§4) and begins its own condensation (§6.2) only
  after the veil is removed, so the hero's two acts never
  overlap into murk.
- **Failure fallback.** Watchdog at 2400ms: if the wipe has not
  completed, the veil is removed and the drip is cancelled —
  the headline stands printed. No JS: the veil is never
  inserted; the headline is simply the headline. Slow network:
  the hero is HTML-first; the veil script is deferred and the
  watchdog runs from DOMContentLoaded, not from script load.
- **Reduced-motion variant.** No wipe, no drip. The headline
  stands clear, and the fog survives only as the static bank
  frame above it (§6.11 at rest) — the original entry's rule:
  fog as a frame, not an event.
- **Performance budget & mobile variant.** Veil is one layer +
  ≤14 rim dots; mask animates a custom property registered via
  `@property` (compositor-driven, no layout). ≤9KB inline SVG/
  CSS. Mobile (<768px): patch opens at 90px, wipe 1300ms, rim
  droplets 7, drip channel 14px — the gesture reads at arm's
  length or it is cut, and here it reads.
- **Choreography timeline (v2).** t=0 fonts ready (or 800ms
  race lost → clear state, ceremony skipped) → t=0 patch at
  60px → t=300–1200 rim beads swell as the rim passes →
  t=1600 radius full, veil removed → t=1750 drip bead begins
  forming under the final letter → t=2450 bead detaches →
  t=2830 bead lands, splash flattens → t=2900 standfirst's
  condensation arms (§6.2). Watchdog ceiling 2400ms cancels
  everything past the veil if the wipe itself stalls.
- **State matrix (v2).** *Rest:* clear, veil absent, drip
  spent. *Hover:* none. *Focus:* focus within hero completes
  a running wipe instantly. *Active:* n/a. *Scrolled-past:*
  completed; returning shows the clear hero. *Disabled /
  no-JS:* printed clear at first paint. *Touch:* identical;
  first touch on the hero completes a running wipe (a tap is
  a hand on the glass).
- **Breakpoints (v2).** ≥1200px: 64px display, patch 120px,
  wipe 1600ms, 9–14 rim beads. 768–1199px: 52px, patch 110px,
  wipe 1500ms, 8–11 beads. <768px: 38px, patch 90px, wipe
  1300ms, 7 beads, drip channel 14px.
- **Edge cases & failure modes (v2).** *Headline edited in a
  CMS:* the wipe is geometry, not per-letter authoring — it
  survives edits; a headline over 9 words is refused at build
  (§12) because the patch cannot cover two lines honestly.
  *Tab hidden mid-wipe:* rAF pauses; on return, wall-clock
  past 2400ms fires the watchdog. *Backdrop-filter absent:*
  irrelevant by structure (duplicate-blur). *Second visit:*
  session flag ships it clear; the drip does not re-form.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; the veil and rim are
  `aria-hidden`. The wipe is never announced. Contrast is the
  printed layer's at all times — `--ink` on `--fog` 12.45:1 —
  because the readable layer is beneath, whole, and the veil
  only ever covers its own duplicate.
- **Tokens consumed (v2).** `--fog`, `--veil`, `--ink`,
  `--sage-deep`, `--droplet`, `--ease-wipe`, `--ease-condense`,
  `--ease-drip`, `--dur-wipe` (1600ms), `--dur-drip-form`
  (700ms), `--dur-watchdog-hero` (2400ms).

### 6.2 Condensing sections

- **What & why.** Every content section enters at 60% clarity
  — blur 6px, opacity 0.55, never below the 40% floor — and
  scrubs to full clarity across its travel through the middle
  50% of the viewport. It belongs because it is the theme's
  physics made into a reading experience: clarity is earned at
  reading position, and the copy becomes readable exactly when
  you arrive to read it. It is also the element the whole law
  (§1) exists to govern: this is where fog could become a
  curtain, and where the spec refuses to let it.
- **Structure.** Each `<section>` carries its complete content
  in the DOM at full contrast. JS arms a veil treatment on the
  section wrapper only: `filter: blur()` + `opacity` driven by
  the shared clarity function (§5) from the shared loop. The
  filter applies to a wrapper that contains no fixed-position
  descendants (a build constraint, §15), and the section's own
  bank (§4) is a separate, unblurred gradient stratum above the
  wrapper — the weather graphic never blurs, only the not-yet-
  read content does, which keeps the bank's edge crisp against
  the softening content and reads as depth, not as a broken
  page.
- **Motion spec.** Trigger: scroll scrub, continuous. Clarity
  follows §5's function exactly: entry C=0.55 (blur 6px,
  opacity 0.55) as the section's top crosses 95% of viewport
  height, rising to C=1.0 as its reading matter crosses the
  reading line at 55%. Lerp 0.12 from the shared loop — the fog
  lags the scroll by a beat, the content never does. If the
  scroll stops mid-curve, a 600ms `--ease-condense` completion
  glide carries the section the rest of the way to the clarity
  its position demands (fog settles; it does not freeze
  mid-gesture). Scrolling back up: clarity is *held* for any
  section whose reading matter has passed the reading line —
  read content never re-fogs on screen (the ratchet); sections
  not yet reached re-arm only when they leave the viewport
  entirely below.
- **States.** Unreached (printed clear in DOM; armed-fogged
  only when JS has run and the section is below the fold) →
  condensing (scrubbed) → clear at the reading line (latched)
  → scrolled-past (clear, permanently for this visit). Hover/
  focus: focus entering a condensing section snaps it clear
  instantly — focus is arrival. Disabled state: a section may
  never be rendered un-readable as a "disabled" treatment;
  unavailable content uses the log's voice (§12), not fog.
- **Content merge.** The condensation is not an overlay on the
  section; it is the section's own state, applied to its own
  wrapper, and what condenses is the section's real headline,
  copy and figures. Remove the effect and the section is
  unchanged in order, layout and content — the test §10 applies
  to every element in this theme.
- **Failure fallback.** Three independent guarantees: (1) the
  DOM ships clear — arming is JS-only, so no-JS is a clear
  page; (2) an IntersectionObserver fallback fires if the
  shared loop stalls: any section intersecting the middle band
  for >1200ms without reaching C=1 is snapped clear; (3) a
  scroll-end snap — 150ms after scroll events cease, every
  section above the reading line is forced to C=1. The 40%
  floor is enforced inside the clarity function (§5), so no
  bug in a caller can render a section below it.
- **Reduced-motion variant.** No condensation. Sections stand
  printed and clear; the banks (§6.11) remain as static frames.
  The information the motion carried — *this is new, this is
  ahead* — is carried instead by the bank gradient alone.
- **Performance budget & mobile variant.** Filter on one
  wrapper per section, only while that section is in the
  condensing band (the loop disarms sections outside it, so at
  most 2 wrappers carry a live filter at any moment). Blur
  radius is the expensive term: capped at 6px, and on
  <768px capped at 4px with the entry clarity raised to 0.65 —
  phone GPUs blur dear, and a smaller softening reads the same
  at arm's length. Sections taller than 200vh condense in two
  halves keyed to their internal reading matter (§6.2 edge
  cases), never as one 200vh blur.
- **Choreography timeline (v2).** Section top crosses 95%
  viewport height → armed at C=0.55 → scrubbed rise per §5
  function → reading matter crosses 55% line → C=1.0, latch
  set → scroll-stop mid-curve → +150ms the 600ms completion
  glide → section leaves viewport top → stays clear (ratchet).
  Observer fallback: +1200ms in band below C=1 → snap.
- **State matrix (v2).** *Rest (unreached):* printed clear in
  DOM, armed fogged below the fold. *Hover:* none (sections
  are not controls). *Focus:* focus-within snaps clear.
  *Active:* n/a. *Scrolled-past:* clear, latched. *Disabled:*
  refused as a treatment (see States). *Touch:* identical
  scrub; fling scroll triggers the scroll-end snap on
  deceleration end, so a flung section never lands fogged.
- **Breakpoints (v2).** ≥1200px: blur cap 6px, entry C=0.55.
  768–1199px: blur cap 5px, entry C=0.60. <768px: blur cap
  4px, entry C=0.65, completion glide 500ms.
- **Edge cases & failure modes (v2).** *Very tall section:*
  split at its internal sub-headings; each half condenses on
  its own reading matter. *Very short section* (shorter than
  30vh): condenses on the shared curve but with its band
  compressed — it must still reach C=1 by the reading line,
  and the gate tests a 20vh section explicitly. *Anchor jump:*
  the target section and everything above the reading line
  snap clear instantly; fog never greets a jump. *Find-in-page
  match in a fogged section:* browsers scroll to it — the
  scroll-end snap clears it; builders must not `content-
  visibility` the sections, which would hide matches.
  *Print:* stylesheet forces C=1, filters none (§14).
- **Accessibility spec (v2).** Fog is a visual treatment only:
  the accessibility tree always holds the clear text, in
  order. Clarity changes are never announced. Because the
  printed layer is the DOM itself, contrast at rest is the
  full token pairing (12.45:1 body); during condensation the
  *rendered* contrast dips, which is precisely why the law
  guarantees C=1 at the reading line and the floor at 0.40 —
  and why no interactive element may sit in a section region
  that is below C=0.9 while it is focusable: sections arm
  their interactive children `tabindex`-safe by snapping clear
  on focus (above), never by removing them from the tab order.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--ease-condense`, `--clarity-entry` (0.55), `--clarity-floor`
  (0.40), `--blur-section-max` (6px), `--dur-glide-complete`
  (600ms), `--dur-watchdog-section` (1200ms), `--lerp-scroll`
  (0.12).

### 6.3 Running corner droplets

- **What & why.** At each section's top corners, 3–5 droplet
  dots swell, merge into one bead, then run down the section
  edge over ~900ms with gravity easing — once per section per
  visit. It belongs because it is condensation with somewhere
  to go: the fog that cleared from the section gathers at its
  corners and leaves as water, down the very border of the pane
  that holds the content. It is the theme's smallest complete
  sentence: fog → droplet → run → harvested.
- **Structure.** Per section, two corner clusters (top-left,
  top-right) of 3–5 dots, 3–7px, drawn as inline SVG circles in
  `--droplet` with the specular point (§2), positioned on the
  section's border line — on the border, not beside it, so the
  run that follows travels the section's own edge: a 2px-wide
  run channel reserved in the section's border geometry (§4)
  from top corner to bottom corner. The merged bead is one
  circle scaled to the summed volume (7–10px). All dots are
  `aria-hidden`, `pointer-events: none`, and exist in the DOM
  only after JS arms them (the printed page has dry corners).
- **Motion spec.** Trigger: the section reaching 60% viewport
  entry — deliberately *before* its clarity completes (§6.2),
  so the gathering reads as the cause of the clearing. Left
  cluster first, right cluster +120ms. Each dot swells over
  450ms `--ease-condense`, staggered 60ms dot to dot; at
  +500ms the dots merge — translating to the cluster's lowest
  dot over 200ms `--ease-settle` — into the bead; at +700ms
  the bead detaches and runs the section's full edge height
  over 900ms `--ease-drip`, wobbling ±1.5px, accelerating; at
  the bottom corner it flattens (scaleY 0.6 over 80ms) and is
  removed. Total act ≈ 1600ms per corner. Once per section per
  visit: a `data-run` latch on the section; scroll-back never
  re-runs it.
- **States.** Dry (rest, pre-trigger; also the permanent no-JS
  state) → swelling → merging → running → spent (removed).
  Hover/focus: none — corners are not controls; hovering a
  section does not summon its weather early. Scrolled-past
  before trigger: if a section is flung past 60% entry to
  above the viewport without the act completing, the act is
  marked spent unwatched (the latch sets at trigger, not at
  completion) — the page does not queue weather for a reader
  who has left.
- **Content merge.** The droplets gather on the section's own
  border and run down its own edge: the pane that holds this
  section's content is the surface being condensed on. The
  run's length is the section's real height, so a tall section
  quite literally sheds more water — the decoration is a
  measurement.
- **Failure fallback.** The act is pure ornament over complete
  content: if any timer fails, dots are removed by a 2000ms
  sweep that clears any cluster still in the swelling state.
  No JS: no dots, dry corners, nothing missing.
- **Reduced-motion variant.** No swell, no run. One static bead
  rests at each section's bottom corner — the water, already
  down — at 60% opacity. The information (this section has
  been harvested) survives as a mark, not a performance.
- **Performance budget & mobile variant.** ≤10 dots + 2 beads
  per section, SVG circles, transform/opacity only; acts are
  one-shot timers, not loop work. Mobile (<768px): one cluster
  per section (top-left only), 3 dots, run shortened to the
  first 60vh of the edge — a phone section can be 300vh tall
  and a 3-second run outstays its welcome.
- **Choreography timeline (v2).** Section crosses 60% entry →
  t=0 left dots begin swelling (60ms stagger) → t=120 right
  cluster begins → t=500 left merge (200ms) → t=620 right
  merge → t=700 left bead detaches, runs 900ms → t=820 right
  bead detaches → t=1600/1720 beads flatten at the bottom
  corners and are removed → latch `data-run` set at t=0.
- **State matrix (v2).** *Rest:* dry corners. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* spent
  (latched at trigger). *Disabled / no-JS:* dry corners, no
  dots in DOM. *Touch:* identical; no touch trigger — the act
  is scroll-keyed, not gesture-keyed.
- **Breakpoints (v2).** ≥1200px: 2 clusters, 4–5 dots, full-
  edge run. 768–1199px: 2 clusters, 3–4 dots, full-edge run.
  <768px: 1 cluster, 3 dots, run capped at 60vh.
- **Edge cases & failure modes (v2).** *Section shorter than
  the run:* the bead flattens at the bottom corner whenever it
  arrives — the 900ms is a duration for a 100vh edge, scaled
  by real edge height (min 300ms, max 1400ms). *Section
  re-entering after latch:* nothing — spent is spent.
  *Borderless section variant:* the run channel is a layout
  reservation, not a visible border; sections without a drawn
  border still carry the channel (the water runs down the
  pane's edge whether or not the edge is inked). *Reduced
  data / low-power:* the sweep still applies; acts are
  cancelled wholesale under `save-data` (§14 cut order).
- **Accessibility spec (v2).** Entirely decorative and
  `aria-hidden`; nothing is announced; no focusable element is
  created. The bead's motion is ≤10px objects at a section
  corner — below vestibular concern at the stated sizes, and
  absent under reduced motion.
- **Tokens consumed (v2).** `--droplet`, `--sage-deep`,
  `--ease-condense`, `--ease-settle`, `--ease-drip`,
  `--dur-swell` (450ms), `--dur-merge` (200ms), `--dur-run`
  (900ms per 100vh), `--dur-watchdog-dots` (2000ms).

### 6.4 The fog-collector progress mesh

- **What & why.** A margin diagram of the collector net —
  diamond mesh, drawn as an SVG — fills droplet by droplet,
  one droplet per section completed, each droplet swelling
  then settling into its mesh cell. It belongs because it is
  the page's progress indicator drawn as the actual instrument
  the site exists about: the visitor is not "62% through the
  page", they have filled 8 of 13 cells of a fog collector by
  reading, and the water in the mesh is the page, harvested.
  It replaces the progress bar, which this theme refuses (§5)
  because a bar measures distance and a mesh measures yield.
- **Structure.** A vertical diamond-mesh SVG in the collector
  rail (§4): two pole lines, a grid of diamond cells — one
  cell per content section on the page, counted from the DOM
  at build (a 13-section home page has 13 cells; the count is
  authored into the markup, not discovered at runtime, so the
  mesh's promise is printed and checkable). Each cell holds one
  droplet slot: an SVG circle in `--droplet` with specular,
  rendered at scale 0 when empty. Beneath the mesh, the gutter
  line and a miniature tank outline that receives the mesh's
  implied drip. The whole diagram is `role="img"` with a text
  alternative that states the count in words ("Collector mesh:
  8 of 13 sections read") — updated at the same beats as the
  visual fill, never more often.
- **Motion spec.** Trigger: a section's clarity latching to
  C=1 at the reading line (§6.2) completes that section; its
  cell's droplet swells over 450ms `--ease-condense` to full
  bead, holds 100ms, then settles — a 250ms `--ease-settle`
  drop of 3px into the cell's lower vertex, where it rests for
  the visit. Fills are queued: if two sections latch within
  300ms (a fast scroll), droplets fill in section order with a
  150ms stagger, never simultaneously — the mesh fills the way
  water arrives, in sequence. Scroll-back never un-fills a
  cell (the ratchet, §6.2): harvested is harvested.
- **States.** Empty (page load; cells drawn, droplets at scale
  0) → filling (per-section beats) → full (every cell beaded;
  the tank outline beneath takes a `--rust` fill line at the
  level the mesh implies — the one place the mesh touches the
  tank). Hover: hovering the mesh highlights the cell of the
  section currently at the reading line (a 1px `--sage-deep`
  cell stroke) — orientation, not interaction; the mesh is not
  a navigation control and clicking it does nothing (nav lives
  in §6.12; an instrument that is also a menu is neither).
  Focus: the mesh is not focusable. Scrolled-past: the fill
  persists — it is the record of the visit.
- **Content merge.** The mesh's cells *are* the page's sections
  in order, and its fill state is the reader's real progress
  through real content. It sits in the margin the layout
  reserves for instruments (§4), beside the content it
  measures, the way the real collector stands beside the
  vineyard it waters.
- **Failure fallback.** No JS: the mesh renders fully drawn
  with every cell beaded — the printed state is a completed
  harvest, and the text alternative reads as the full count.
  If the fill logic fails mid-visit, a 3000ms watchdog beads
  every cell whose section has latched, so the instrument
  never understates the reader's progress.
- **Reduced-motion variant.** Droplets appear in their cells
  instantly at the latch beat (no swell, no settle); the
  ratchet and the count are unchanged. The instrument still
  measures; it simply does not perform the measuring.
- **Performance budget & mobile variant.** One inline SVG,
  ≤6KB; fills are one-shot transitions on ≤20 circles. Below
  1200px the rail narrows (§4) and cells shrink proportionally;
  below 768px the mesh leaves the margin and renders as a
  single horizontal row of cells above the footer (§6.17),
  same fill logic, same alternative text — the instrument
  moves, the measurement doesn't change.
- **Choreography timeline (v2).** Section N latches C=1 →
  t=0 cell N droplet begins swell (450ms) → t=450 bead full →
  t=550 settle begins (250ms, −3px) → t=800 bead rests in the
  vertex → if section N+1 latched within the window, its beat
  starts at t≥150 after N's start, in order → final cell →
  tank fill line draws 600ms `--ease-settle`.
- **State matrix (v2).** *Rest:* cells drawn, fill = sections
  completed. *Hover:* current section's cell outlined.
  *Focus:* not focusable. *Active:* n/a. *Scrolled-past:*
  fill persists (ratchet). *Disabled / no-JS:* fully beaded
  printed state. *Touch:* identical; hover outline replaced by
  the current-cell outline showing whenever the mesh is on
  screen.
- **Breakpoints (v2).** ≥1200px: 76px rail, cells ~34px,
  vertical mesh. 768–1199px: 48px rail, cells ~22px, labels
  off. <768px: horizontal row above footer, cells ~18px,
  poles/gutter omitted, tank line kept.
- **Edge cases & failure modes (v2).** *Page with 1 section:*
  the mesh is one cell and the theme should not have been
  chosen (§1) — the build warns, does not break. *Page with
  >20 sections:* cells group — the mesh caps at 20 cells and
  the last cell represents the final group, with the
  alternative text still exact ("19 of 23 sections read" is
  computed from sections, not cells). *Section added by CMS:*
  cell count is a build-time audit (§15): markup mesh cells
  must equal DOM sections or the build fails, never silently
  mismeasures. *Anchor jump to the last section:* sections
  above the reading line latch in order and the queue fills
  the mesh in one 150ms-staggered pass.
- **Accessibility spec (v2).** `role="img"`, alternative text
  updated at fill beats only (never per scroll frame), phrased
  as a count of sections read. The SVG's internal shapes are
  `aria-hidden`. The mesh creates no focusable elements and
  sits outside the content's reading order in the DOM (placed
  after `<main>` with a `aria-label` on its container), so a
  screen-reader user's path down the page is the content's
  own order.
- **Tokens consumed (v2).** `--droplet`, `--sage`, `--sage-deep`,
  `--rust`, `--mist`, `--ease-condense`, `--ease-settle`,
  `--dur-swell` (450ms), `--dur-settle-drop` (250ms),
  `--dur-watchdog-mesh` (3000ms).

### 6.5 The long vineyard clear

- **What & why.** The vineyard section pins for ~150vh while
  its fog layer thins from 90% to 0% in one continuous scrub,
  revealing the vine-rows photograph beneath. It belongs
  because it is the theme's one long act of weather: the
  morning the fog lifts off the actual vines the copy is
  describing — weather and crop in a single image, given the
  time a real lifting takes. Every other clear on the page is
  a moment; this one is a duration, and the duration is the
  argument: this water arrives slowly or not at all.
- **Structure.** A pinned stage (sticky, 100vh) inside a 250vh
  track (100vh stage + 150vh of travel). Layers, back to
  front: the vine-rows photograph (a real `<img>`, fully
  loaded in the DOM, alt text complete); the fog layer — a
  fog-white field with a soft bottom edge (a 30vh gradient
  skirt, so the clear rises from the ground the way real fog
  burns off upward from the rows); the caption block, printed,
  sitting in the stage's lower third *above* the fog's skirt
  line at all times (the caption is never fogged — §3 law 4 —
  it is positioned where the fog has already left). The fog
  layer is `aria-hidden`, `pointer-events: none`.
- **Motion spec.** Trigger: scroll scrub through the pin,
  driven by the shared loop (lerp 0.12). Fog opacity follows
  pin progress `q` (0→1 across the 150vh of travel):
  `opacity = 0.90 × (1 − q)^1.3` — the exponent makes the first
  half of the travel thin the fog only to ~0.37 (fog resists),
  and the last third clears it fast (fog goes all at once when
  it goes). The skirt's gradient rises with the same `q`. At
  q=1 the fog layer is removed from the DOM. Scroll-back
  reverses the scrub honestly until q falls below 0.02, at
  which point the layer is re-inserted fogged — the one
  licensed reversal in the theme (§6.2's ratchet governs
  *read text*; a photograph not yet read is weather, and
  weather may return). But the caption, once read, never
  re-fogs: it was never in the fog layer.
- **States.** Fogged (q=0, 90%) → thinning (scrubbed) → clear
  (q=1, layer removed). Hover/focus: none on the photograph;
  focusable elements inside the stage (the caption's link, if
  any) are reachable throughout, and focus entering the stage
  does not alter the scrub — a keyboard user scrolls the same
  travel. Scrolled-past: clear, layer absent.
- **Content merge.** The fog lifts off the real photograph of
  the real vineyard the adjacent copy describes — not a stock
  mist picture, not a generic landscape. The copy's claims
  (row orientation, the mesh poles visible at the frame's top
  edge) are checkable in the photograph once it clears; the
  clear is the verification.
- **Failure fallback.** The pin is a sticky enhancement: if
  sticky or the loop fails, the section renders as a normal
  section with the photograph clear and the fog layer absent
  (it is JS-inserted). A 4000ms watchdog on the pin: if the
  stage has been pinned 4000ms without q advancing past 0.05
  (a stalled scroller, an embedded webview), the fog thins on
  a 1200ms `--ease-drift` time-based glide to clear — the
  photograph is never held hostage by a scroll mechanic.
- **Reduced-motion variant.** No pin. The section is a normal
  section: photograph clear, a static fog bank frame at its
  head (§6.11), caption beneath. The long clear's information
  — the vines were in fog, now they are not — is carried by
  the caption's own first line, which the copy (§12) writes to
  survive the still version.
- **Performance budget & mobile variant.** One image (the
  page's LCP candidate — served at full priority, never
  lazy), one fog layer (a gradient, not a filter — the clear
  is opacity on a flat layer, the cheapest scrub in the
  theme). Mobile (<768px): the pin shortens to 100vh of
  travel and the fog starts at 80% — a phone's scroll is
  quicker and its reader's patience shorter; below 400px
  height viewports the pin is dropped entirely (a pinned
  stage taller than the visible area traps small landscape
  phones), falling back to the reduced structure without the
  motion preference being involved.
- **Choreography timeline (v2).** Stage pins → q 0→0.5 fog
  0.90→~0.37, skirt rising → q 0.5 caption fully uncovered
  (it was never covered; its *context* completes) → q 0.85
  fog ~0.08, rows fully legible → q 1.0 fog layer removed,
  pin releases → section continues as a normal clear section.
  Watchdog branch: pinned 4000ms at q<0.05 → 1200ms glide to
  clear.
- **State matrix (v2).** *Rest (unreached):* stage unpinned,
  fog at 90% armed (JS only). *Hover:* none. *Focus:* no
  change to scrub; focusable caption link always reachable.
  *Active:* n/a. *Scrolled-past:* clear, layer removed.
  *Disabled / no-JS:* unpinned, photograph clear, no fog
  layer in DOM. *Touch:* identical scrub; fling through the
  pin scrubs honestly — q is positional, so a fling simply
  clears the fog at fling speed, which reads as a gust and is
  licensed.
- **Breakpoints (v2).** ≥1200px: 150vh travel, fog 90%,
  exponent 1.3. 768–1199px: 130vh travel, fog 88%. <768px:
  100vh travel, fog 80%, exponent 1.2; <400px viewport
  height: pin dropped, static structure.
- **Edge cases & failure modes (v2).** *Photograph fails to
  load:* the fog layer is not inserted — fog over a broken
  image would hide the failure; the alt text and the section's
  printed frame stand, and the error is visible, as it should
  be. *Slow image:* the pin does not arm until the image's
  `load` fires or 2500ms passes, whichever first; a fog clear
  over an unloaded frame is a reveal of nothing. *Reader
  scrolls back into the pin from below:* the reversal rule
  (above) re-fogs the photograph only. *Multiple vineyard
  sections:* refused — one pin per page (§5).
- **Accessibility spec (v2).** The photograph's alt text is
  complete and static; the fog layer is `aria-hidden` and its
  opacity is never announced. The caption is ordinary text,
  readable at every q. During the pin, the section's position
  in the accessibility tree is unchanged (sticky is visual
  only). Vestibular note: the scrub is reader-paced — no
  autonomous motion — and the reduced-motion variant removes
  the pin entirely.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--ease-drift`, `--pin-travel` (150vh), `--fog-pin-start`
  (0.90), `--dur-watchdog-pin` (4000ms), `--lerp-scroll`
  (0.12).

### 6.6 Harvest counters

- **What & why.** Litres harvested, fog-days per year and mesh
  square-metres count up in Newsreader numerals when the data
  band centres, with a droplet dropping into the litre figure
  at count end. It belongs because these numbers are the
  collector's real yield — the fog the reader just cleared,
  quantified — and because the count-up, done under §1's second
  clause, is the theme's honesty made visible: every figure
  traces to the declared yield object printed beside it.
- **Structure.** A data band of three figures, each a
  `<figure>`: the numeral (Newsreader 500, 44px), the unit
  label (Source Sans caption), and the **source line** — a
  13px `--sage-deep` line stating the figure's derivation
  ("1,260 m² of mesh × 4.6 L per m² per fog-day × 84 fog-days
  this season"). The three figures print from one yield object:
  mesh area `A = 1,260 m²`, mean capture `R = 4.6 L/m²/fog-day`,
  season fog-days `D = 84`, giving litres `L = A × R × D =
  486,864 L`; fog-days per year `212` is the ten-year mean,
  printed with its own source line ("mean of the 2015–2024
  log"). The numerals exist in the DOM at their true values
  from first paint; the count-up is a JS overlay animation of
  the displayed text only.
- **Motion spec.** Trigger: the band's centre crossing the
  reading line, once per visit (latched). Each figure counts
  over 1400ms `--ease-condense` from 88% of its value to the
  value — a count from near, not from zero: fog counters never
  start at 0, because the collector was harvesting before the
  visitor arrived, and a from-zero count would lie about that
  (§9, failure 6). Figures stagger 120ms. At the litre figure's
  completion (+150ms), one droplet forms above the numeral and
  drops into it over 380ms `--ease-drip`, flattening on the
  baseline — the yield, delivered. Scroll-back never re-runs;
  the figures rest at truth.
- **States.** Printed-at-truth (rest, and the permanent no-JS
  state) → counting (one pass) → at-truth (rest, droplet
  spent). Hover: none. Focus: focus entering the band before
  it has counted completes the count instantly. Scrolled-past
  uncounted (flung): the count is marked done and the figures
  stand at truth — a gauge does not perform for an absent
  reader.
- **Content merge.** The figures are the science section's own
  data, sitting in the band the copy refers to ("the mesh
  above this ridge…"), and their source lines are part of the
  figure, not a footnote elsewhere: the number and its
  provenance are one element, inseparable in the layout.
- **Failure fallback.** The DOM prints truth; JS only animates
  the display toward it. Any failure — observer, timer, loop —
  leaves the true figures standing. There is no state in which
  a wrong number can persist: the animation's final frame is
  the DOM value, set by construction, and a 2000ms watchdog
  forces the text content to the true values if the count is
  interrupted.
- **Reduced-motion variant.** No count, no droplet. The figures
  stand at truth with their source lines — which is most of
  the element anyway; the count is the ceremony, the source
  line is the substance.
- **Performance budget & mobile variant.** Text-only animation
  (three text contents, 1400ms), no layout. Mobile: figures
  stack, numerals 36px, the droplet drops into the litre
  figure only (the band's one droplet is spent there at every
  size — rationed, §5).
- **Choreography timeline (v2).** Band centre crosses reading
  line → t=0 litres begin (1400ms, from 88%) → t=120 fog-days
  begin → t=240 mesh m² begins → t=1400 litres land →
  t=1550 droplet forms above litre numeral → t=1930 droplet
  lands, flattens → all figures at truth, latch set.
- **State matrix (v2).** *Rest:* true figures printed.
  *Hover:* none. *Focus:* focus-within completes count
  instantly. *Active:* n/a. *Scrolled-past:* at truth,
  latched. *Disabled / no-JS:* true figures, source lines,
  nothing animated. *Touch:* identical; no tap trigger.
- **Breakpoints (v2).** ≥1200px: three figures in a row, 44px
  numerals. 768–1199px: three in a row, 38px. <768px: stacked,
  36px, source lines full width under each figure.
- **Edge cases & failure modes (v2).** *Figures updated by the
  client mid-season:* the yield object is the single source —
  `D` changes, `L` recomputes, and every printing (band,
  footer tank §6.17, season table §6.14) must agree; the gate
  recomputes `A × R × D` and compares all three printings
  (§10). *A figure with no honest value:* it is not printed —
  the band ships with two figures rather than inventing a
  third (§12). *Locale formatting:* numerals format with the
  visitor's locale grouping; the count animates the formatted
  string's numeric value, never a raw digit string.
- **Accessibility spec (v2).** The figures' true values are in
  the accessibility tree from first paint (the animation
  writes to an `aria-hidden` display span while a visually
  hidden twin holds the truth — or, simpler and preferred:
  the count runs only when the band is *not* being read, and
  completes on focus; builders choose one, the gate tests that
  a screen reader at the band hears the true figures, never a
  mid-count number). Source lines are ordinary text, read as
  part of each figure.
- **Tokens consumed (v2).** `--fog`, `--ink`, `--sage-deep`,
  `--rust`, `--droplet`, `--ease-condense`, `--ease-drip`,
  `--dur-count` (1400ms), `--count-from` (0.88),
  `--dur-watchdog-count` (2000ms).

### 6.7 The collector-mesh diagram

- **What & why.** An SVG net diagram — poles, mesh diamonds,
  drip line, collection tank — strokes itself in over ~1.8s in
  the science section, in build order. It belongs because it is
  the labelled diagram of the system the adjacent copy explains,
  line for line: the reader watches the collector being built
  in the order a crew builds it, and the drawing *is* the
  explanation, not an illustration beside it.
- **Structure.** One inline SVG (~340×420px in the margin-and-
  measure layout of the science section): two pole paths, the
  diamond mesh (a path grid of 6×8 diamonds), the drip line
  along the mesh's foot, the gutter, the tank outline at the
  base — in `--rust` stroke, the tank's one licensed diagram
  appearance (§5 ration: the tank in a drawing is the tank) —
  and five labels in Source Sans 600 11px uppercase (§3): POLE,
  MESH, DRIP LINE, GUTTER, TANK. Every path ships at full
  `stroke-dashoffset: 0` (drawn) in the DOM; JS arms the draw
  by setting dash offsets. Labels are real SVG `<text>`, in
  the accessibility tree via the figure's caption.
- **Motion spec.** Trigger: the diagram's centre crossing the
  reading line, once. Draw order is build order: poles first
  (300ms), mesh diamonds row by row from the top (900ms, each
  row 110ms, `--ease-settle` at each row's end), drip line
  (200ms), gutter (150ms), tank outline (250ms) — total
  1800ms. Labels fade in at the moment their part completes
  (200ms each), never before: a label for an undrawn part is a
  caption to nothing. The tank's fill line rises last, to the
  level §6.6's yield object implies for the season (84 of 212
  fog-days ≈ 40% of a season's tank — computed from the object,
  not authored).
- **States.** Drawn (rest; the permanent no-JS state) →
  drawing (one pass) → drawn with tank level. Hover: hovering
  a labelled part thickens its stroke 1px→1.75px and sets its
  label in `--ink` — the diagram answers inspection. Focus:
  the diagram is one figure, not five controls; it is not
  focusable part by part (the copy beside it carries the same
  information as text). Scrolled-past mid-draw: the draw
  completes on its own timeline.
- **Content merge.** The diagram is the science section's
  central content, placed inside the measure beside the
  paragraphs that name its parts in the same order the draw
  builds them — paragraph one is poles, paragraph two is mesh.
  A reader who only reads, and a reader who only watches, get
  the same explanation in the same order.
- **Failure fallback.** Ships drawn. If the draw is
  interrupted (tab hidden, loop stall), a 2600ms watchdog sets
  all offsets to 0 and all labels visible. No JS: the complete
  labelled diagram, printed.
- **Reduced-motion variant.** The diagram stands drawn with
  its tank level; labels all present. Nothing about the
  information changes.
- **Performance budget & mobile variant.** One SVG ≤8KB;
  dash-offset animation on ~60 paths for 1800ms, once.
  Mobile (<768px): the diagram takes the full measure width
  (it is content, not margin furniture, at this size), draw
  1500ms with rows at 90ms — and the mesh diamonds reduce to
  5×6, a legibility cut, declared here rather than discovered
  on a small screen.
- **Choreography timeline (v2).** Centre crosses reading line
  → t=0 poles draw (300ms), POLE label at t=300 → t=350 mesh
  rows begin (8 rows × 110ms) → t=1230 MESH label → t=1250
  drip line (200ms) + label → t=1450 gutter (150ms) + label →
  t=1600 tank outline (250ms) → t=1850 TANK label → t=1900
  tank fill rises (400ms) to the computed level → drawn rest.
- **State matrix (v2).** *Rest:* drawn, labelled, tank level
  set. *Hover:* part stroke thickens, label darkens. *Focus:*
  not focusable (figure-level). *Active:* n/a.
  *Scrolled-past:* drawn. *Disabled / no-JS:* drawn at first
  paint. *Touch:* tap on a part gives the hover treatment for
  1200ms (touch has no hover; the diagram still answers a
  pointing finger).
- **Breakpoints (v2).** ≥1200px: 340px wide, margin-adjacent
  two-column science layout. 768–1199px: 300px, same layout
  compressed. <768px: full measure, 5×6 mesh, draw 1500ms.
- **Edge cases & failure modes (v2).** *Copy edited so the
  part order changes:* the draw order is build order, not
  copy order — if the paragraphs are reordered, §15's
  checklist requires the draw order be re-matched; the gate
  compares them. *Tank level exceeds the drawn tank:* the
  level is a fraction of the season by construction (≤1.0);
  a yield object that computes >1.0 is a data error and the
  build fails loudly rather than overfilling a drawing.
  *SVG text rendering differences:* labels use the body face
  with system fallback; a fallback face widens labels ~4% —
  the diagram's label positions carry 8% slack by design.
- **Accessibility spec (v2).** The figure carries a `<figcaption>`
  that explains the system in prose (the same explanation as
  the adjacent copy, condensed), and the SVG is `role="img"`
  with a `<title>`. The draw is never announced. All label
  text meets caption contrast on its ground (`--sage-deep` on
  fog 5.87:1 at rest; hover `--ink` 12.45:1).
- **Tokens consumed (v2).** `--ink`, `--sage`, `--sage-deep`,
  `--rust`, `--cypress`, `--ease-settle`, `--ease-condense`,
  `--dur-draw-diagram` (1800ms), `--dur-watchdog-diagram`
  (2600ms).

### 6.8 Speckled image frames

- **What & why.** Photographs carry a droplet speckle overlay
  at their edges; as each image centres, the speckle beads
  merge and clear inward over ~600ms while the image scales
  1.05 → 1.0. It belongs because the photograph sits behind
  the same wet glass as the reader: clearing it is inspecting
  the product — the crate of bottles, the row of vines, the
  crew on the ridge — and the inspection is timed to the
  moment the image becomes the thing being looked at.
- **Structure.** A `<figure>` with the real `<img>` (complete,
  alt text, never lazy below the fold's first two) inside a
  frame whose inner edge carries the speckle: 24–40 droplet
  dots (SVG or box-shadow sprites, `--droplet` with specular)
  distributed on the frame's inner perimeter, denser at the
  bottom edge (water gathers low). The image scales inside an
  `overflow: hidden` frame — scale-in-frame, the frame never
  moves. The speckle layer is `aria-hidden`, `pointer-events:
  none`, JS-inserted.
- **Motion spec.** Trigger: scroll scrub keyed to the image's
  approach to the viewport centre. As the image's centre
  travels the band from 70% to 50% of viewport height, the
  speckle clears inward: edge beads shrink and merge toward
  the frame's corners over 600ms `--ease-condense` (scrubbed,
  lerp 0.12), and the image scales 1.05→1.0 on the same scrub.
  At centre, the frame is dry and the image is at rest size.
  Scroll-back above the band re-speckles only if the image
  has not yet been centred once (the ratchet applies once an
  image has been *inspected*; an uninspected image may re-fog
  its glass).
- **States.** Speckled (armed, approaching) → clearing
  (scrubbed) → dry & centred (rest, latched) → scrolled-past
  (dry). Hover: hovering a speckled image does not clear it —
  inspection here is positional, not gestural (the card wipe
  §6.9 is the gestural one; two clearing gestures on adjacent
  elements would compete). Focus: an image inside a focusable
  link clears instantly when the link takes focus.
- **Content merge.** The speckle is on the photograph's own
  frame and the photograph is the section's evidence — the
  vineyard rows §6.5 cleared at landscape scale, the crew and
  the crates here at object scale. The frame's bottom-heavy
  speckle is the same physics as §6.3's corner runs, at a
  different scale: one weather system, consistently applied.
- **Failure fallback.** Images ship dry and at rest size; the
  speckle is JS-inserted and its scrub is loop-driven with a
  1200ms observer fallback that dries any centred image whose
  speckle has not cleared. A failed image shows its alt text
  in a dry frame — never behind speckle (§6.5's rule: fog
  never hides a failure).
- **Reduced-motion variant.** Images stand dry at 1.0. No
  speckle, no scale. The frame's printed inner edge (a 1px
  `--mist` line) remains as the still version of the wet
  frame.
- **Performance budget & mobile variant.** Speckle is one
  sprite layer per image, transform/opacity only; at most 3
  images scrub simultaneously (the loop disarms the rest).
  Mobile (<768px): speckle count halves (12–20 dots), scale
  range narrows to 1.03→1.0 — small screens forgive less
  magnification, and the cut is declared, not discovered.
- **Choreography timeline (v2).** Image centre enters 70%
  line → speckle begins clearing from the top edge (water
  leaves the top first as the pane tilts into view) → centre
  crosses 60% → side beads merge toward corners → centre
  crosses 50% → last bottom beads shrink into the bottom
  corners, image reaches 1.0 → latch: dry. Total scrub
  ≈600ms at reading scroll speed.
- **State matrix (v2).** *Rest (dry):* image at 1.0, frame
  dry. *Hover:* none (positional element). *Focus:* link
  focus clears instantly. *Active:* n/a. *Scrolled-past:*
  dry, latched. *Disabled / no-JS:* dry at 1.0, no speckle
  in DOM. *Touch:* identical scrub; no tap-to-clear.
- **Breakpoints (v2).** ≥1200px: 24–40 dots, scale 1.05.
  768–1199px: 20–32 dots, scale 1.04. <768px: 12–20 dots,
  scale 1.03, clearing band widened (75%→50%) so the clear
  completes before a fast phone scroll passes the image.
- **Edge cases & failure modes (v2).** *Very small images*
  (<200px wide): speckle omitted — a thumbnail's frame cannot
  hold 24 dots honestly; the image stands dry (declared
  exemption, §15). *Portrait images:* speckle distribution
  follows the perimeter, denser at the bottom as always.
  *Image swapped by CMS:* the speckle is geometry on the
  frame, not the image — swaps are safe. *Dark photograph:*
  droplet speculars at 55% white may glare; on images whose
  mean luminance is below 30%, speckle renders at 70% opacity
  (a build-time flag on the figure, `data-speckle-dim`).
- **Accessibility spec (v2).** The speckle is decorative and
  hidden from AT; the image's alt text is unaffected and
  available at all times — including while speckled, because
  the speckle is a layer over a complete image, not a state
  of the image itself. Scale never crops content: the frame
  is sized to the 1.05 crop, so at rest the full image shows.
- **Tokens consumed (v2).** `--droplet`, `--mist`, `--ease-
  condense`, `--dur-speckle-clear` (600ms), `--scale-frame-
  from` (1.05), `--dur-watchdog-image` (1200ms), `--lerp-
  scroll` (0.12).

### 6.9 The hover glass-wipe

- **What & why.** Hovering any card clears a ~90px-radius
  circular patch in its fog veil — a radial-gradient mask
  tracking the pointer, lerped for a wiped feel — and leaving
  re-fogs over 800ms. It belongs because it hands the hero's
  gesture (§6.1) to the visitor at object scale: you wipe the
  card's own condensation to read its offer, and inspection
  becomes touch. It is the theme's one pointer-following
  effect, and it is rationed to cards for exactly that reason.
- **Structure.** Each card (§6.12) carries a veil layer: a
  duplicate of the card's face at `--veil` strength with a
  radial mask — clear inside `--wipe-x/--wipe-y` radius 90px,
  fogged outside, the mask edge softened over 24px with 5–7
  droplet beads sitting on the rim (the wipe gathers water as
  it moves, §6.1's rim at hand scale). The card's real content
  beneath is complete and is the accessible layer; the veil is
  `aria-hidden`, `pointer-events: none`.
- **Motion spec.** Trigger: pointerenter / pointermove on the
  card (pointer-fine devices only). The wipe centre follows
  the pointer with lerp 0.18 per frame from the shared loop —
  the original entry's figure — fast enough to feel held, slow
  enough to feel like a hand dragging water. Radius breathes
  88–94px with pointer speed (a faster hand clears a wider
  patch, capped). On pointerleave, the patch closes over
  800ms `--ease-condense` — re-fogging is slower than wiping,
  because condensation is slower than a hand. On touch: no
  hover wipe; a tap gives the click droplet (§6.10) instead,
  and the card's veil is at its resting 0% on touch devices
  entirely (see §6.12 — touch cards ship unwiped and unveiled;
  a veil that can only be cleared by a pointer a touch user
  doesn't have would be a curtain, §1).
- **States.** Veiled-at-rest (desktop, pre-hover: veil at 22%
  strength — a card at rest is *damp*, not fogged shut; its
  headline is legible through the damp, its body is read after
  the wipe or after §6.2's section clarity, whichever first) →
  wiping (pointer present) → re-fogging (800ms) → veiled-at-
  rest. Focus: keyboard focus on the card or its link clears
  the veil entirely over 300ms — focus is a wipe by other
  means. Active (press): the veil clears fully for the press.
  Disabled card: no veil at all — an unavailable offer is
  printed plainly with its reason (§6.12), never fogged.
- **Content merge.** The veil is the card's own condensation
  on the card's own face; what the wipe reveals is the card's
  actual offer text, price and link. The wipe's rim beads are
  the card's water. Nothing is revealed that is not the card.
- **Failure fallback.** The veil is JS-inserted; no JS means
  unveiled cards. If the loop stalls, a veil whose card is
  hovered or focused clears via the CSS fallback: `:hover` /
  `:focus-within` on the card sets the veil's opacity to 0
  with the same 800ms transition — the gesture degrades to a
  fade, never to a stuck veil. A 1200ms watchdog removes any
  veil stuck above rest strength while its card is in the
  viewport centre band.
- **Reduced-motion variant.** No tracking wipe. Hover/focus
  fades the veil to 0 over 200ms (a state change, not a
  gesture); the rim beads are omitted. Cards remain fully
  usable and fully readable.
- **Performance budget & mobile variant.** One mask per card,
  compositor-driven via `@property`-registered custom
  properties; at most 6 veiled cards per page (§6.12's cap)
  and only the hovered card's mask animates. Mobile/touch:
  the element does not exist (see Motion spec) — the budget
  is spent on §6.10's tap droplet instead.
- **Choreography timeline (v2).** Pointer enters → t=0 veil
  begins tracking (lerp 0.18) → rim beads fade in at the rim
  by t=150 → pointer moves → patch follows, radius breathing
  88–94px → pointer leaves → t=0 re-fog begins (800ms) →
  beads shrink into the closing rim → t=800 veil at rest 22%.
  Focus branch: t=0 veil fades fully (300ms) → focus leaves →
  800ms re-fog to rest.
- **State matrix (v2).** *Rest:* veil 22%, headline legible.
  *Hover:* tracking wipe at pointer. *Focus:* veil cleared
  (300ms). *Active:* veil cleared for the press duration.
  *Scrolled-past:* veil at rest (cards re-damp; they are
  objects, not read text — §6.2's ratchet does not apply to
  veils, only to clarity). *Disabled:* no veil, plain print.
  *Touch:* no veil at any state.
- **Breakpoints (v2).** ≥1200px: radius 90px, rim beads 5–7.
  768–1199px (pointer-fine tablets/laptops): radius 80px,
  beads 4–6. <768px: element absent (touch rule); a
  pointer-fine small window (rare) gets radius 72px.
- **Edge cases & failure modes (v2).** *Pointer leaves through
  a child link:* pointerleave on the card is the trigger, not
  the child's — moving onto the card's own link keeps the
  wipe. *Fast pointer exit:* the re-fog runs from wherever
  the patch is; no snap. *Card inside a condensing section:*
  the section's clarity (§6.2) and the card's veil compose —
  veil strength multiplies the section's rendered opacity, and
  §4's density ration counts the combination, which is why
  cards live in sections that reach C=1 early in their travel
  (§15 build order). *Forced-colors mode:* veils are removed
  entirely (masks and gradients are not honoured there, and a
  veil that cannot render its mask would render as a block).
- **Accessibility spec (v2).** The veil never carries
  information: the card's content is in the tree, complete,
  at all times, and the resting 22% veil leaves the headline
  at ≥4.5:1 rendered contrast (veil over `--ink` on `--fog`
  computes to ~7:1 at rest strength — measured, §10). Focus
  clearing is the keyboard equivalent of the wipe and is
  mandatory, not an enhancement. Touch targets are the card's
  own (§6.12), unaffected by the veil (`pointer-events:
  none`).
- **Tokens consumed (v2).** `--veil`, `--fog`, `--ink`,
  `--droplet`, `--ease-wipe`, `--ease-condense`, `--wipe-r`
  (90px), `--veil-rest` (0.22), `--dur-refog` (800ms),
  `--lerp-wipe` (0.18), `--dur-watchdog-card` (1200ms).

### 6.10 The click droplet run

- **What & why.** A click on a card releases one droplet at
  the click point that runs down the card's surface, wobbling
  ±2px, accelerating, and drops off the bottom edge. It belongs
  because it is feedback rendered as the site's material —
  water on glass — on the very card acted upon: you touched
  the pane, and the pane answers in its own substance. In a
  theme where every other effect is weather, the click is the
  one thing the visitor makes happen with a finger, and it
  should feel like it.
- **Structure.** One droplet element per card (reused, not
  spawned per click): an SVG bead in `--droplet` with specular,
  8px at release, positioned at the click point on the card's
  surface layer (above the veil §6.9, below nothing else;
  `pointer-events: none`, `aria-hidden`). The card's surface
  is `position: relative` with `overflow: visible` at the
  bottom edge only for the droplet's exit — implemented as the
  droplet living in a card-level layer that extends 14px below
  the card's box, so the drop can fall off the edge without
  the card clipping it or growing.
- **Motion spec.** Trigger: click (or Enter/Space activation —
  the droplet releases from the activated control's centre,
  see Accessibility). t=0: the bead forms at the point over
  120ms `--ease-condense` (a press gathers water). Then the
  run: down the card's height over 620–900ms (duration from
  real card height: 1.1ms per px, clamped) `--ease-drip`,
  wobbling ±2px on a 90ms sine, growing 8→11px as it gathers
  the veil's damp on its way. At the bottom edge it detaches
  and falls 14px accelerating, flattening at the layer's end
  and removed. A second click mid-run restarts the bead at the
  new point (one droplet per card at a time — water rationed,
  §5's spirit). The click's *actual* action (the card's link,
  the form's button) is never delayed by the droplet: the
  droplet is commentary, not a gate.
- **States.** Dry (rest) → forming (120ms) → running → falling
  → gone. Hover: none. Focus: keyboard activation releases the
  droplet from the control's centre (above). Disabled card:
  no droplet — a disabled surface does not answer touch, and
  its printed reason (§6.12) is the answer instead.
  Scrolled-past: the droplet belongs to the act, not the
  scroll; it completes regardless.
- **Content merge.** The droplet runs down the acted card's own
  face and off its own edge — the feedback is located exactly
  where the act happened, in the material the whole site is
  made of. It carries no information and pretends to carry
  none; its honesty is that it is *only* a touch answered.
- **Failure fallback.** Pure ornament: any failure leaves the
  click's real action untouched. A 1500ms sweep removes any
  bead still present. No JS: clicks simply work, dryly.
- **Reduced-motion variant.** No run. The click point shows a
  static bead for 400ms that fades — a touch acknowledged
  without travel. (Under reduced motion the card's veil is
  also handled per §6.9's variant.)
- **Performance budget & mobile variant.** One bead per card,
  transform-only, one-shot. Mobile/touch: this is the touch
  device's primary card feedback (replacing §6.9's absent
  wipe): tap releases the droplet at the tap point, run
  shortened by the card's real height as always. Budget is
  trivially met at every size.
- **Choreography timeline (v2).** Click at point P → t=0 bead
  forms at P (120ms) → t=120 run begins, wobble 90ms period,
  growth 8→11px → t=120+run bead reaches bottom edge →
  detach, fall 14px (~140ms `--ease-drip`) → flatten, remove
  → card dry. Keyboard branch: bead forms at the activated
  control's centre, same timeline.
- **State matrix (v2).** *Rest:* dry. *Hover:* none. *Focus:*
  no droplet on focus alone (focus clears the veil, §6.9 —
  the droplet is for acts, not arrivals). *Active:* bead
  forms on the press, runs on release-activation.
  *Scrolled-past:* n/a. *Disabled:* no droplet, no veil.
  *Touch:* tap = click, identical timeline.
- **Breakpoints (v2).** ≥1200px: bead 8→11px, wobble ±2px.
  768–1199px: same. <768px: bead 9→12px (a fingertip's
  droplet is bigger), wobble ±2px, exit fall 12px.
- **Edge cases & failure modes (v2).** *Click near the bottom
  edge:* run clamps to a 200ms minimum — the bead still forms
  and falls; a droplet released at the edge mostly falls,
  which is correct physics and reads fine. *Rapid clicking:*
  the bead restarts at each new point; the card's action
  fires per click as normal. *Card height changes mid-run*
  (an expanding card): the run's target is recomputed at
  detach time from the live box; the bead never falls through
  a card that grew. *Click on the card's link:* navigation
  proceeds; the droplet is abandoned mid-run if the page
  unloads — it was commentary.
- **Accessibility spec (v2).** Decorative, `aria-hidden`,
  never announced, never the sole feedback for an action —
  every clickable card has its own focus/press states (§6.12)
  independent of the droplet. Keyboard activation produces
  the droplet at the control's centre so a keyboard user's
  act is answered in the same material, at the place their
  focus visibly is.
- **Tokens consumed (v2).** `--droplet`, `--ease-condense`,
  `--ease-drip`, `--dur-bead-form` (120ms), `--run-rate`
  (1.1ms/px, clamped 620–900ms), `--dur-watchdog-bead`
  (1500ms).

### 6.11 Drifting fog banks

- **What & why.** Fog drifts continuously across section tops
  in slow banks — the theme's only ambient loop. It belongs
  because a fog coast is never still, and the banks are the
  page's weather between events: everything else in the theme
  happens *because* of fog; the banks are the fog simply
  being there. They also do layout work — a bank is each
  section's head (§4) — so the ambience is load-bearing, not
  wallpaper.
- **Structure.** Per section, one bank layer at the section's
  head: a 120–200px field of two overlapping radial-gradient
  masses in `--fog`/`--mist` over the section ground, edges
  feathered to zero, `pointer-events: none`, `aria-hidden`.
  On cypress sections the masses render in mist at reduced
  strength (§2's night rule applies in miniature: banks over
  dark ground at 60%). The bank is part of the section's
  printed structure — it exists with JS off, as a static
  gradient. JS adds only the drift.
- **Motion spec.** The two masses translate horizontally in
  opposition: mass A drifts +38px over 46s, mass B −30px over
  64s, both `--ease-drift`, alternate direction, looping — a
  bank that breathes back and forth rather than conveyor-
  belting (a linear infinite translate would eventually show
  its seam; an oscillation has none). Parallax from the shared
  loop: the bank layer also translates vertically at 0.92×
  scroll (§5), capped ±22px, clamped to authored overflow.
  Opacity ceiling 0.5 for the moving masses (the printed
  gradient beneath carries the rest of the bank's presence).
  Drift pauses when the section is off-screen (the loop's
  sleep rule) and when the tab is hidden.
- **States.** Banked (rest; static gradient — also the no-JS
  and reduced-motion state) → drifting (JS, on-screen).
  Hover/focus: none — weather does not respond to a pointer;
  a bank that reacts to hover has become a toy (§9, failure
  8). Scrolled-past: drift continues while visible; the bank
  is the section's head, not its event.
- **Content merge.** The bank is the section's own head and
  the source its condensation (§6.2) is imagined to come
  from: the fog that will clear from this section is visibly
  gathered above it. It carries no text and covers no text —
  the section's display line sits at the bank's foot, below
  the gradient's zero line (§4), at every scroll position and
  drift phase (the ±22px parallax clamp is sized to guarantee
  exactly this).
- **Failure fallback.** The bank ships static; drift is an
  enhancement layer. No watchdog is needed for a gradient to
  exist; if the loop dies, the banks are still banks.
- **Reduced-motion variant.** Static banks, full stop. The
  original entry's rule — fog only as a static frame — is
  this element's resting state promoted to its only state.
- **Performance budget & mobile variant.** Gradients, not
  images or filters; two transformed layers per *visible*
  section (the loop disarms off-screen banks). Mobile
  (<768px): one mass per bank (the second is cut — §14's cut
  order spends here first), drift amplitude ±24px, cycle
  52s. Low-power devices (`save-data` or the loop's frame-
  budget trip, §14): drift off, banks static.
- **Choreography timeline (v2).** Continuous: mass A 0→+38px
  (46s) → return (46s); mass B 0→−30px (64s) → return (64s);
  the two cycles beat against each other with a full
  realignment every ~6 minutes, so the bank never repeats a
  configuration within a reading. Scroll: vertical parallax
  lerped 0.12 in the shared loop, independent of the drift
  cycle.
- **State matrix (v2).** *Rest:* static bank. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* bank remains
  its section's head, drifting while visible. *Disabled /
  no-JS:* static bank, complete. *Touch:* identical (drift is
  not a gesture response).
- **Breakpoints (v2).** ≥1200px: two masses, ±38/−30px, bank
  160–200px. 768–1199px: two masses, ±30/−24px, bank
  140–180px. <768px: one mass, ±24px, bank 120–150px.
- **Edge cases & failure modes (v2).** *Bank over a short
  section:* bank height caps at 40% of section height — a
  30vh section gets a 12vh bank, never a fogged section with
  a headline lost in it (§4's density law counts this).
  *Two banks adjacent* (short sections back to back): the
  lower section's bank halves its opacity — stacked weather
  must not sum into a whiteout. *Forced colors:* banks are
  removed (gradients are not honoured; a bank rendered as a
  block would cover the section head).
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`,
  outside the reading order. Motion is slow (≤38px over 46s —
  effectively sub-perceptual per frame), reader-independent,
  and fully removed under reduced motion. No text ever sits
  on the moving masses (the foot-of-bank rule, above).
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ease-drift`,
  `--drift-a` (46s), `--drift-b` (64s), `--bank-opacity-max`
  (0.5), `--parallax-bank` (0.92), `--parallax-cap` (22px).

### 6.12 The fog-line navigation

- **What & why.** The site's navigation is a fixed head bar
  drawn as the topmost fog bank: the wordmark and section
  links sit in a fog-white stratum whose lower edge is a
  thinning gradient — the page's own weather, gathered at the
  top where a reader's eye starts. It belongs because a Fog
  Harvest site should be navigable from inside its fiction:
  the wayfinding is the ridgeline, and the current section is
  marked by the one droplet the mesh (§6.4) cannot hold — the
  reader's own position, shown as a bead under the current
  link.
- **Structure.** A `<header>` (fog ground, 64px) with the
  wordmark in Newsreader, 4–6 section links in Source Sans,
  and a gradient skirt (28px) beneath the bar thinning to
  transparent. The current-section marker is a 6px `--droplet`
  bead centred under the current link's label. The header is
  in the DOM in normal flow; JS adds `position: sticky`
  behaviour enhancements (shadow on scroll) only — no-JS keeps
  a static header at the page top, complete.
- **Motion spec.** On scroll past 140px, the bar gains a 1px
  `--mist` bottom rule and the skirt shortens 28→12px over
  300ms `--ease-settle` (the fog compresses as you commit to
  the page). The current-section bead migrates as sections
  latch at the reading line (§6.2): it slides to the new
  current link over 450ms `--ease-settle`, with a 2px droplet
  flatten as it arrives. Migration is scrollspy-honest: the
  bead marks the section at the reading line, never a hovered
  or clicked link that the reader hasn't reached.
- **States.** Rest (top of page: full skirt, no rule) →
  settled (scrolled: rule + short skirt). Hover: a link's
  label takes a `--sage-deep` underline drawn left-to-right
  over 220ms. Focus: visible focus ring in `--cypress` 2px
  offset — the theme's focus colour everywhere (§11). Active:
  the current link is `--ink` at 600 weight with the bead;
  others `--sage-deep`. Disabled: a section that does not
  exist yet (a planned page) is not linked at all — the nav
  never carries a fogged, greyed decoy link (§1: fog is not a
  disabled state).
- **Content merge.** The nav is the page's first bank and its
  links are the real sections in their real order — the same
  order the mesh (§6.4) fills and the sections condense. Three
  instruments, one sequence: nav, mesh, page.
- **Failure fallback.** Static header, all links live, current
  section marked in the printed state by the bead under the
  first link (or server-rendered per page). Scrollspy failure
  leaves the bead wherever it was — a stale position marker is
  a venial sin; a missing nav is not, and the nav never
  depends on the scrollspy to exist.
- **Reduced-motion variant.** The bead jumps (no slide), the
  skirt change is instant. Everything else identical.
- **Performance budget & mobile variant.** One bar + one bead,
  transform-only. Mobile (<768px): the links collapse into a
  menu button (≥48px target) opening a fog-ground panel in
  normal flow beneath the bar — not an overlay (overlays are
  refused, §11); the bead marks the current section inside
  the panel when opened, and the closed button carries a
  6px bead beside its label if the current section is not
  the first — position survives the collapse.
- **Choreography timeline (v2).** Scroll crosses 140px →
  skirt 28→12px + rule fades in (300ms) → section N latches
  at reading line → bead slides to link N (450ms) → flatten
  2px at arrival (80ms) → bead rests. Scroll returns above
  140px → skirt restores (300ms).
- **State matrix (v2).** *Rest:* full skirt, bead under
  current link. *Hover:* underline draws 220ms. *Focus:*
  cypress ring, bead unmoved (focus is not position).
  *Active:* current link weighted + bead. *Scrolled-past:*
  n/a (the nav is the frame). *Disabled:* nonexistent links
  are absent, never disabled. *Touch:* menu panel variant;
  tap targets ≥48px.
- **Breakpoints (v2).** ≥1200px: full bar, 6 links max, skirt
  28px. 768–1199px: full bar, links at 15px, skirt 24px.
  <768px: menu-button collapse, panel in flow, skirt 16px.
- **Edge cases & failure modes (v2).** *More than 6 sections:*
  the nav groups — sections beyond six live under a "More
  banks" link to the listing page; the bead's migration maps
  grouped sections to the group link. *Long wordmark + long
  labels:* the bar wraps to two rows before it truncates —
  a truncated nav label is a broken instrument. *Sticky
  unsupported (ancient webview):* the header is simply static;
  nothing else in the theme depends on it sticking.
- **Accessibility spec (v2).** Landmark `<header>` + `<nav
  aria-label>`; current section link carries `aria-current=
  "location"` in step with the bead (the bead is the visual
  twin of the ARIA state, updated at the same beat). Focus
  order is DOM order. The mobile panel is a disclosure
  (`aria-expanded`), Esc closes it, focus returns to the
  button.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--sage-deep`, `--cypress`, `--droplet`, `--ease-settle`,
  `--dur-nav-settle` (300ms), `--dur-bead-migrate` (450ms).

### 6.13 Condensation cards

- **What & why.** The card family — offers, wines, visits,
  tanks — built as small panes of wet glass: a fog-ground
  card with a resting damp veil (§6.9), a wet-glass tilt, and
  the click droplet (§6.10). It belongs because the card is
  where the theme's gestures live; the family spec exists so
  that six cards on a page are six panes from one window, not
  six inventions. A page carries at most 6 veiled cards (§6.9's
  budget); a seventh offer joins the season table (§6.14) as a
  row, which is the theme's way of saying a listing is a
  ledger, not a wall of panes.
- **Structure.** `<article>` on `--fog` with a 1px `--mist`
  edge, radius 0 (glass panes are cut square in this theme;
  §11's radius law) — anatomy in fixed order: the offer's
  image or mark (top, in a speckled frame §6.8 when it is a
  photograph), Newsreader headline (24px), body (15px, ≤3
  lines), the figure line (price/quantity in Newsreader
  numerals with its unit), and one link — the whole card is
  not a link; the link is a link, styled as the card's action
  line with a `--sage-deep` rule. The veil layer (§6.9) sits
  over the face. Tilt: the card rotates toward the pointer,
  max 3°, on the shared loop's lerp.
- **Motion spec.** Entrance: cards condense with their section
  (§6.2) — they have no separate entrance. Tilt: pointermove
  over the card rotates it ≤3° (rotateX/rotateY from pointer
  position, lerp 0.14), with the card's shadow shifting 2px
  opposite — a pane tipping in its frame; tilt freezes while
  the card holds focus-within (a keyboard user's card does not
  lean away from them) and is absent on touch. Rest: tilt
  returns over 400ms `--ease-settle` on pointerleave. The
  veil and droplet are §6.9/§6.10's specs, invoked here.
- **States.** Rest: damp veil 22%, no tilt, headline legible.
  Hover: wipe tracking (§6.9) + tilt ≤3°. Focus-within: veil
  cleared, tilt locked at 0°, focus ring on the focused
  element. Active: veil cleared, droplet forming (§6.10).
  Scrolled-past: as rest. Disabled (an offer genuinely
  unavailable — the tank is empty, the visit is full): the
  card prints *without* veil or tilt, its figure line replaced
  by the reason in the log's voice ("The March mornings are
  full — the April bank opens on the 1st"), and no link. Fog
  is never the disabled treatment (§1).
- **Content merge.** A card is its offer: the image is the
  wine, the figure is its price from the same record the
  season table (§6.14) prints, the link is its page. The wet
  glass is the card's surface, not a treatment applied to a
  generic box — remove the veil, tilt and droplet and the
  card is still recognisably this site's offer, in this
  theme's type and tokens.
- **Failure fallback.** Cards ship unveiled, untilted, fully
  linked. Every effect on the card is JS-added; every failure
  mode of every effect leaves a printed card.
- **Reduced-motion variant.** No tilt; veil per §6.9's variant
  (fade on hover/focus); droplet per §6.10's variant. The
  card's content and order are untouched.
- **Performance budget & mobile variant.** ≤6 cards per page;
  tilt is one transform on the hovered card only. Mobile:
  no tilt, no veil (§6.9's touch rule), droplet on tap
  (§6.10); cards stack at full measure; the figure line
  stays Newsreader — small screens do not demote the data.
- **Choreography timeline (v2).** Section condenses → card
  clear with it (§6.2 curve) → pointer enters → t=0 veil
  wipe begins (§6.9) + tilt starts (lerp 0.14 toward ≤3°) →
  pointer leaves → tilt returns (400ms), veil re-fogs (800ms)
  → rest. Click branch: §6.10's timeline, concurrent.
- **State matrix (v2).** *Rest:* damp, flat, legible.
  *Hover:* wipe + tilt. *Focus:* veil clear, tilt 0°, ring
  visible. *Active:* droplet forming, veil clear.
  *Scrolled-past:* rest state. *Disabled:* printed plainly,
  reason in place of figure, no veil/tilt/link. *Touch:*
  unveiled, untilted, tap droplet.
- **Breakpoints (v2).** ≥1200px: 3-across grid, tilt 3°.
  768–1199px: 2-across, tilt 2.5°. <768px: 1-across, no tilt,
  no veil, figure line 20px Newsreader.
- **Edge cases & failure modes (v2).** *Card with no image:*
  the mark variant — a Newsreader initial or the mesh glyph
  (§6.7's diamond) in place of the photograph; never a grey
  placeholder box (a placeholder is fog by another name).
  *Long headline:* caps at 2 lines by copy rule (§12), not by
  truncation — a truncated offer is a broken promise.
  *Price changes:* the figure prints from the record object;
  card and table (§6.14) cannot disagree (§10 audit).
  *Card inside the pinned vineyard stage:* refused — cards
  live in clearing sections, never inside the pin (§6.5's
  stage holds one photograph and one caption).
- **Accessibility spec (v2).** One link per card, with a
  real label ("Order the 2023 Niebla — case of six"), never
  "Read more". Focus ring `--cypress` 2px, offset 2px, on the
  link; the card itself is not focusable. Tilt and veil are
  visual only; the card's text is in the tree complete.
  Touch targets: the link ≥44px tall via its action-line
  padding.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--sage-deep`, `--veil`, `--ease-settle`, `--tilt-max`
  (3deg), `--dur-tilt-return` (400ms), `--lerp-tilt` (0.14).

### 6.14 The season table

- **What & why.** The one licensed data table: the season's
  harvest by month — fog-days, litres, mesh in service — a
  ruled ledger in the fog ground. It belongs because a fog
  farm's credibility is a record kept over time, and because
  the theme needs exactly one place where data is allowed to
  be dense, so that everywhere else can be weather. The
  table's rows are also the audit trail for §6.6's counters:
  the season's 84 fog-days and 486,864 litres are the sum of
  this table's printed rows, and the gate checks the sum.
- **Structure.** A real `<table>` with `<caption>` ("The
  season, month by month — from the ridge log"), column heads
  in Source Sans 600 11px uppercase, month rows in Source
  Sans 15px, numerals in Newsreader 500 lining figures,
  right-aligned. Rules: 1px `--mist` between rows, a 2px
  `--cypress` rule under the head and above the totals row.
  The totals row is the yield object's printings (§6.6):
  fog-days total = `D`, litres total = `A × R × D` recomputed
  from the rows, not typed. A weather note column sets its
  text in Newsreader italic (§3 law 5 — the fog's own words:
  "the long bank in the second week").
- **Motion spec.** The table condenses with its section
  (§6.2) and has no other entrance. Its one act: when the
  totals row crosses the reading line, a single droplet forms
  at the totals rule and runs down the table's right edge to
  the totals row over 700ms `--ease-drip` — the season,
  collected. (This is a §6.3-family act, keyed to the table,
  and it spends the page's droplet budget accordingly — §5's
  ledger counts it.) Sorting: none. A season is chronological
  or it is fiction; the table refuses sort controls (§11).
- **States.** Rest: printed, complete — the table is the
  element least allowed to be an event. Hover: a row takes a
  `--mist` wash at 40% (200ms) — the log answers a pointing
  finger with a shade, not a wipe (tables are read, not
  wiped; §6.9 is for cards). Focus: cells are not focusable;
  the table's one link (the full log, in the caption's line)
  takes the standard ring. Scrolled-past: printed.
  Disabled: n/a — a month with no fog is a row of honest
  figures ("0 fog-days — the dry month"), never a missing
  row: the log does not skip a month it dislikes.
- **Content merge.** The table is the science section's
  evidence and the counters' source; it sits in the section
  whose copy cites it ("the table below is the ridge log,
  kept daily"), and its caption names the keeper. It is not
  a component dropped into the theme — it is the theme's
  memory, typeset.
- **Failure fallback.** A table needs no fallback: it ships
  printed. The droplet is JS ornament with §6.3's sweep
  behind it.
- **Reduced-motion variant.** No droplet. The table stands —
  it was always standing.
- **Performance budget & mobile variant.** Zero animation
  budget beyond the one droplet. Mobile (<768px): the table
  sheds the weather-note column into a footnote line under
  the table (the notes are content; they move, they are not
  cut), numerals stay Newsreader at 15px, and the table
  scrolls horizontally never — five columns at 15px fit
  360px, which is why the column count is capped at five in
  §11.
- **Choreography timeline (v2).** Table condenses with
  section → totals row crosses reading line → t=0 droplet
  forms at the head rule → runs the right edge (700ms) →
  flattens at the totals row → spent. Once per visit.
- **State matrix (v2).** *Rest:* printed. *Hover:* row wash
  40% mist. *Focus:* caption link ring only. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled / no-JS:* printed,
  complete, droplet absent. *Touch:* no hover wash; rows
  answer tap with the same wash for 600ms.
- **Breakpoints (v2).** ≥1200px: five columns incl. weather
  note. 768–1199px: five columns, note column narrower.
  <768px: four columns + notes as footnotes, 15px throughout.
- **Edge cases & failure modes (v2).** *A season with 13
  rows* (a long season): the table prints all rows — the log
  is not paginated (§11 refuses pagination here); the page
  grows, honestly. *Mid-season present:* the current month's
  row carries "(to the 14th)" in its note and its figures are
  the count to that date — the same `D` the counters use, so
  the table and the band can never disagree about today.
  *Rounding:* litres print whole (no decimals — a tenth of a
  litre is not a measurement a mesh makes); the totals row
  sums the printed rows exactly, and any rounding lives in
  the rows, visibly.
- **Accessibility spec (v2).** Real table semantics: `<th
  scope="col">`, caption, totals row as `<tfoot>`. Numerals
  are text, read as numbers. The row wash is visual only.
  Contrast: `--ink` on `--fog` 12.45:1 in cells; head labels
  `--sage-deep` 5.87:1 at 11px uppercase 600 — the floor for
  apparatus, audited in §10.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--sage-deep`, `--cypress`, `--droplet`, `--ease-drip`,
  `--dur-table-run` (700ms).

### 6.15 The harvest form

- **What & why.** The conversion element: booking a fog-
  morning visit, ordering a case, joining the harvest list —
  one form family, set as a page from the ridge log. It
  belongs because conversion on a fog site should feel like
  writing in the log the site has been keeping all along:
  the visitor's entry joins the record, and the form's
  success is not a tick but a droplet — their litre, entering
  the tank. The form is also where §1's second clause is
  tested hardest: its figures (places left, case price) print
  from the record, and its confirmation number is derived
  from the log's real count, never invented.
- **Structure.** A `<form>` on `--fog` with ruled lines
  (1px `--mist` under each field, the log's ruling): fields
  in log order — name, direction (email), the choice (visit
  date / case / list) as a radio row drawn as mesh cells
  (each option a diamond cell that takes a droplet when
  chosen, §6.4's geometry at hand scale), quantity where the
  choice needs one, and the submit — a rust tank-button, the
  form's one rust object (§5 ration): a rectangle in `--rust`
  with fog-white text ("Enter it in the log"). Errors print
  beneath their field in `--rust-deep`, in the keeper's voice
  (§12), with the field's rule turning `--rust-deep` 2px.
  The confirmation replaces the form in place: a log entry —
  the visitor's own details re-set as a printed row, the
  entry number, and the droplet act (below).
- **Motion spec.** Field focus: the field's rule inks from
  `--mist` to `--cypress` left-to-right over 260ms. Radio
  choice: the chosen cell's droplet swells in over 450ms
  `--ease-condense` (the mesh gesture, §6.4); the previously
  chosen cell's droplet dries over 300ms. Submit: the button
  presses (translateY 1px, 120ms), the form's fields settle
  to print, and on success a droplet forms at the form's top
  rule, runs its right edge (700ms `--ease-drip`, §6.14's
  act, kin) and drops into a small tank outline at the form's
  foot, whose fill line rises by one unit — then the
  confirmation entry fades in over 400ms `--ease-condense`.
  The confirmation's entry number is computed: the log's
  current entry count (printed in the form's head line, "The
  log holds 214 entries") + 1 — derived from the DOM's
  printed count, so the number the visitor gets is the number
  the log actually reaches.
- **States.** Rest: ruled, empty, the head line stating the
  log's count. Focus: rule inks (above). Filled: rules rest
  at `--sage-deep` (a written line is darker than an empty
  one). Error: field rule `--rust-deep`, message beneath,
  focus moved to the first error on submit-failure, input
  preserved — the log does not lose a visitor's writing.
  Submitting: button text becomes the keeper's present tense
  ("Entering…") for any wait past 600ms; the button is never
  pre-disabled for validation (validation speaks in errors,
  not in grey — a disabled submit is fog on a control, §1).
  Success: the confirmation entry (above). Disabled form
  (the season is closed): the form is replaced by the log's
  line ("The log is closed until the autumn bank") and a
  link to the list — a form that cannot be used is not
  rendered as a form.
- **Content merge.** The form is a page of the same log the
  season table (§6.14) prints and the footer (§6.17) closes:
  same ruling, same numerals, same keeper's voice in its
  errors. Its success writes the visitor into that record —
  the confirmation is formatted as the log's next row, not as
  a marketing panel.
- **Failure fallback.** The form is a native form: it submits
  without JS (the droplet and the in-place confirmation are
  enhancements; the server returns the same confirmation as a
  page). Validation exists server-side regardless of the JS
  layer. If the in-place confirmation fails after a successful
  submit, the form restores the visitor's input and prints
  the log's apology with the entry number if one was issued —
  never a silent loss.
- **Reduced-motion variant.** No droplet run, no swell: the
  chosen cell's droplet appears, the confirmation replaces
  the form with a 150ms fade. Focus inking is instant.
- **Performance budget & mobile variant.** The form's whole
  animation budget is two droplets and three rule transitions.
  Mobile (<768px): radio cells stack as full-width rows (the
  diamond becomes a left-edge mark — geometry yields to
  thumbs, the droplet does not), fields at 16px (no iOS
  zoom), submit full-width at 52px tall.
- **Choreography timeline (v2).** Focus field → rule inks
  260ms → choose a cell → droplet swells 450ms → submit →
  button press 120ms → (wait >600ms → "Entering…") →
  success → droplet forms at top rule → runs edge 700ms →
  drops into tank outline, fill +1 unit (300ms) →
  confirmation entry fades in 400ms, entry number = printed
  count + 1 → focus lands on the confirmation heading.
- **State matrix (v2).** *Rest:* ruled, head line with count.
  *Hover:* submit button deepens to `--rust-deep` (200ms);
  radio cells show a 40% droplet ghost. *Focus:* rule inks;
  ring `--cypress` on the control. *Active:* button press
  1px. *Scrolled-past:* the form keeps its state (a half-
  written log entry is not cleared by scrolling). *Disabled:*
  whole-form closure replaces the form (above); per-field
  disabled is refused. *Touch:* 16px fields, ≥48px radio
  rows, droplet on tap-choice identical.
- **Breakpoints (v2).** ≥1200px: form at 62ch within the
  measure, radio cells in a row of diamonds. 768–1199px:
  same, cells smaller. <768px: stacked radio rows, 16px
  fields, full-width submit.
- **Edge cases & failure modes (v2).** *The printed count is
  stale* (another visitor entered first): the confirmation
  number is issued by the server at submit; the in-place
  enhancement displays the server's number on response, and
  the +1 computation is only the pre-submit expectation,
  labelled as the log's next *expected* entry in the head
  line if the site is multi-visitor — the spec's rule: the
  form never promises a number it cannot keep. *Double
  submit:* the button disables after the first activation
  (an act, not a validation state) and the droplet runs once.
  *Autofill:* filled rules take the filled state on the
  `input` events autofill fires; if a browser fills silently,
  the rules rest at mist — cosmetic only, no logic depends on
  rule colour. *Long names/directions:* fields are single-
  line and scroll internally; the confirmation re-sets them
  at whatever length arrived, wrapped in the log row.
- **Accessibility spec (v2).** Real `<label>` per field,
  `aria-describedby` for hints and errors, errors announced
  via a live region summary at the form's head ("Two entries
  want correcting — the direction, and the date") with focus
  moved to the first error. Radio cells are real radios
  (visually diamonded), keyboard-operable in their group.
  The droplet and tank acts are `aria-hidden`; the
  confirmation is a heading + text, focused on arrival.
  Contrast: field text `--ink` on `--fog` 12.45:1; error text
  `--rust-deep` 6.27:1; submit fog-on-rust 4.22:1 at 17px
  600-weight — large-text licensed, audited (§10).
- **Tokens consumed (v2).** `--fog`, `--mist`, `--ink`,
  `--cypress`, `--sage-deep`, `--rust`, `--rust-deep`,
  `--droplet`, `--ease-condense`, `--ease-drip`, `--dur-ink-
  rule` (260ms), `--dur-swell` (450ms), `--dur-form-run`
  (700ms).

### 6.16 The fogged skeleton & the fog roll

- **What & why.** Loading is a fully fogged skeleton that
  condenses as content arrives, and the page transition rolls
  fog in to white, then thins onto the new page. It belongs
  because in this theme even absence has weather: a page that
  is not ready yet is not blank or spinning — it is fogged,
  and it clears the way everything here clears, by gathering
  into legibility. The skeleton's shapes are the page's own
  layout under fog, so what condenses is recognisably the page
  that is coming.
- **Structure.** The skeleton mirrors the target page's layout
  exactly: bank, display-line block, body blocks at the real
  measure, figure blocks — rendered as `--mist` masses under a
  `--veil` layer at 86%, with the section's droplet corners
  (§6.3 geometry) unformed. No spinner exists in the theme
  (§11 refuses it: a spinner is a machine; this coast waits
  for weather, and the fog *is* the waiting, shown). The
  transition is a single full-viewport fog layer (fog white,
  gradient-skirted edges) inserted between documents by the
  router/transition layer.
- **Motion spec.** Skeleton: as each region's real content
  arrives, that region condenses over 600ms `--ease-condense`
  (the §6.2 curve at region scale: blur 6→0 on the region's
  veil, masses resolving to content). Regions condense in
  reading order regardless of arrival order — if the footer
  data lands first, it waits, fogged, until the regions above
  it have cleared; a page that assembles bottom-up is a page
  condensing wrong. Hard ceiling: at 3000ms every remaining
  region condenses with whatever it has (real content or the
  log's apology line, §12) — fog may not hold a page past 3
  seconds. Transition: on navigation, fog rolls in over
  450ms `--ease-wipe` to full white (the layer's leading edge
  is a soft skirt, so the roll reads as a bank arriving, not
  a wipe cut), the document swaps beneath the white, and the
  fog thins onto the new page over 700ms `--ease-condense`,
  revealing the new page already printed beneath it (the new
  page's own §6.2 arming proceeds normally under the thinning).
- **States.** Skeleton: fogged → condensing (per region) →
  clear. Transition: clear → rolling in → white (document
  swap, ≤100ms target) → thinning → clear. Hover/focus during
  skeleton: the skeleton contains no interactive elements —
  focus is held on the page's skip link / heading shell, and
  the first real focusable element receives focus only when
  its region has condensed. Scrolled-past: n/a.
- **Content merge.** The skeleton is the page's own layout —
  same banks, same measure, same figure shapes — so the
  condense is a clarification, not a replacement: nothing
  moves when content lands (zero CLS, §3 law 2 applied to
  loading). The transition's fog is the same weather the new
  page's hero will wipe (§6.1): travelling between pages on
  this site is going out into the fog and arriving.
- **Failure fallback.** If content fails, its region condenses
  at the 3000ms ceiling onto the log's error line in place —
  fog never hides a failure (§6.5's rule). If the transition
  layer fails, navigation is a plain document load: the fog
  roll is an enhancement over the platform's own behaviour,
  never a dependency of it. A transition interrupted mid-roll
  (back button) restores the source page clear — the roll
  layer is removed on `pageshow` regardless of state.
- **Reduced-motion variant.** No skeleton fog: regions appear
  as they arrive with a 150ms fade, under a static bank. No
  fog roll: navigation is instant (the platform default);
  the new page arrives printed. Waiting is still shown
  honestly — the skeleton's masses without the veil.
- **Performance budget & mobile variant.** The skeleton is
  CSS masses, no images; the transition layer is one gradient
  field. Mobile: identical, with the ceiling at 2500ms (a
  phone's reader has waited longer already by the time the
  page is requested). The fog roll is the first thing cut
  under §14's budget pressure — navigation must never pay for
  weather.
- **Choreography timeline (v2).** Skeleton: t=0 fogged →
  regions condense in reading order as content lands (600ms
  each, overlapping allowed by ≤200ms) → t≤3000 ceiling forces
  the remainder. Transition: click → t=0 fog rolls in (450ms)
  → white, document swaps → t=550 fog begins thinning
  (700ms) → t=1250 new page clear, layer removed → new page's
  own acts proceed.
- **State matrix (v2).** *Rest:* no skeleton (content
  present), no roll layer. *Hover:* n/a. *Focus:* held at
  shell until regions condense. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled / no-JS:* no skeleton fog
  (server-rendered pages arrive whole; a client region that
  needs JS shows the log's line, not a fogged block, when JS
  is absent). *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: skeleton mirrors full layout
  incl. rail. 768–1199px: rail omitted from the skeleton (the
  mesh is not content). <768px: skeleton at mobile measure,
  ceiling 2500ms.
- **Edge cases & failure modes (v2).** *Content faster than
  the fog:* if all regions arrive within 300ms, the skeleton
  is skipped entirely — a page that is ready does not perform
  waiting. *Partial failure:* one region errors, others
  condense normally; the errored region clears at its own
  arrival or the ceiling, onto its error line. *Transition
  to a page with a hero wipe:* the roll's thinning and the
  hero's wipe (§6.1) are sequenced, never stacked — the roll
  completes, then the wipe arms; two veils over one headline
  would double-blur the printed layer's duplicate and break
  §3 law 4's contrast accounting.
- **Accessibility spec (v2).** The skeleton region carries
  `aria-busy="true"` on `<main>` until the last region
  condenses, with a visually hidden status ("The page is
  condensing") announced once, not per region. The transition
  is visual only; the new page's heading receives focus per
  the router's normal contract. Nothing in either act traps
  or moves focus unexpectedly.
- **Tokens consumed (v2).** `--fog`, `--mist`, `--veil`,
  `--ease-condense`, `--ease-wipe`, `--dur-region-condense`
  (600ms), `--dur-skeleton-ceiling` (3000ms), `--dur-roll-in`
  (450ms), `--dur-roll-thin` (700ms).

### 6.17 The tank footer

- **What & why.** The footer is the collection tank at the
  foot of the page: a cypress-deep ground holding the site's
  record — the yield figures' third printing, the credit
  line, the log's closing entry — with the tank gauge drawn
  at its head: a horizontal tank outline whose fill line
  stands at the season's true level. It belongs because every
  page in this theme ends where the water ends up. The footer
  is not a sitemap with a logo; it is the vessel the whole
  page has been filling, and its level is a fact (§1, clause
  2), computed from the same yield object as §6.6 and §6.14.
- **Structure.** `<footer>` on `--cypress-deep`: at its head,
  the tank — an SVG outline (the §6.7 tank, grown) spanning
  the measure, its fill a `--rust` band whose height is the
  season fraction `D / 212` (84 of 212 fog-days ≈ 40%),
  computed, with the level labelled in Newsreader numerals
  ("486,864 litres, of a 1,228,752-litre season") — the
  annual figure also computed: `A × R × 212`. Beneath: three
  columns in fog white / mist — the record (yield figures,
  third printing), the site (links, plain), and the keeper's
  column (contact, the log's hours) — and the final line, set
  in Newsreader italic (§3 law 5), the credit, verbatim:
  *"This page, like our vineyard, is watered by fog."* The
  credit names the water source the way the collectors of
  Chungungo are credited in the original entry: as provenance,
  not as a slogan.
- **Motion spec.** The footer condenses with its section
  position (§6.2 applies to the footer's own travel; it is
  the last section). Its one act: when the tank crosses the
  reading line, the fill line rises from the season's start
  level (0 — the tank began the season empty, which is a fact
  about tanks, not a counter's lie; §6.6's from-88% rule
  governs *gauges of accumulation*, and the tank's honest
  zero is its empty state at season start, printed beside it)
  to the true level over 1200ms `--ease-condense`, once,
  latched. The credit line does not animate. Ever. It is
  printed.
- **States.** Rest: printed, fill at truth (the no-JS state).
  → rising (one pass) → at level. Hover: footer links take
  the standard `--rust-pale` underline draw (220ms) — the one
  place rust-pale works for its living (§2). Focus: standard
  ring in fog white on the deep ground. Scrolled-past: at
  level, latched.
- **Content merge.** The footer's figures are the same yield
  object's third printing (band §6.6, table §6.14, tank
  here), and the gate's three-printings audit (§10) compares
  them character-for-character after locale formatting. The
  tank the visitor watched fill in miniature in the mesh
  (§6.4) and the diagram (§6.7) stands here at full width:
  the page's instruments were all drawings of this vessel.
- **Failure fallback.** Printed at level with true figures.
  The rise is an enhancement; its failure leaves the truth
  standing, as everywhere in this theme.
- **Reduced-motion variant.** Fill at level, no rise. Credit
  printed. Nothing else in the footer ever moved.
- **Performance budget & mobile variant.** One SVG tank +
  text; the rise is one height transition. Mobile: columns
  stack (record first — the figures lead at every size), the
  tank spans the measure, the credit line last, always last.
- **Choreography timeline (v2).** Footer travels and
  condenses (§6.2 curve) → tank crosses reading line → t=0
  fill begins rising from season-start 0 → t=1200 fill at
  true level, label settles → latch. Columns and credit are
  clear throughout their own condensation; they do not wait
  for the tank.
- **State matrix (v2).** *Rest:* printed, fill at truth.
  *Hover:* link underlines in `--rust-pale`. *Focus:* fog-
  white ring. *Active:* n/a. *Scrolled-past:* at level.
  *Disabled / no-JS:* printed at level. *Touch:* identical;
  no hover underline (links are plainly styled).
- **Breakpoints (v2).** ≥1200px: three columns, tank at
  measure width. 768–1199px: two columns + keeper's beneath.
  <768px: stacked, record first, credit last.
- **Edge cases & failure modes (v2).** *Season fraction >1*
  (a wetter year than the mean): the tank's scale is the
  *record* season, not the mean — the label states which
  ("of a 1,228,752-litre mean season; the record is 2021,
  1,410,090 litres") and the fill caps at the tank's rim with
  the overflow stated in the label, never silently clipped:
  a tank that overfills its drawing is a data story, told in
  words. *Zero season* (a new site, no harvest yet): the
  tank stands empty and the record column prints the log's
  first line instead of figures (§12's empty voice) — the
  footer does not invent a first season.
- **Accessibility spec (v2).** Landmark `<footer>`; the tank
  is `role="img"` with its level as text ("Tank: 486,864
  litres of a 1,228,752-litre mean season") — the same words
  as the visible label, so the figure is not image-only.
  Link contrast on cypress-deep: fog white 10.90:1, mist
  8.02:1, `--rust-pale` 4.73:1 (labels/large only, per §2).
- **Tokens consumed (v2).** `--cypress-deep`, `--fog`,
  `--mist`, `--rust`, `--rust-pale`, `--ease-condense`,
  `--dur-tank-rise` (1200ms).

### 6.18 The dry page (404)

- **What & why.** The error page is the one page where no fog
  came: a fully clear, still page — cypress-deep ground, one
  printed line, the way home. It belongs because the theme's
  weather has a meaningful absence: a dry season is the
  fog farm's real fear, and the page the visitor reaches by
  mistake should feel like the morning the bank never arrived
  — nothing obscured, nothing moving, the tanks holding what
  they held. It is the theme's restraint proven: the most
  atmospheric page on the site is the one with no atmosphere
  performed at all.
- **Structure.** A short page on `--cypress-deep`: the
  wordmark (fog-line nav, static variant §6.12), the status
  line in Newsreader ("This page is not in the log."), two
  plain lines in the keeper's voice stating the fact and the
  likeliest intended destinations (the season, the visit
  page, the home bank — three real links, chosen from the
  site's actual top destinations), and at the foot the tank
  at its true level (§6.17's tank, unrisen) with the line:
  "The tanks hold what they held." No fog layer, no bank, no
  droplet exists on this page.
- **Motion spec.** None. The choreography is specified as
  *none* — the only element in the theme whose motion spec is
  a refusal. Links take the standard hover underline (a state
  change, not an act). Any builder who adds a drifting bank
  "to keep it on-theme" has inverted the theme: the dry page
  is on-theme *because* it is dry.
- **States.** Rest is the only state. Hover/focus: standard
  link treatments (§6.17's footer rules, on the same ground).
  Disabled: n/a. The page has no armed states, no latches,
  no watchdogs — there is nothing here to fail.
- **Content merge.** The dry page carries the site's real
  recovery content: the three destinations are the site's
  actual most-visited pages (a build-time fact, reviewed
  quarterly per §15), and the requested path is printed in
  the keeper's line ("the log has no entry for /harvest-
  2019") — the error is specific, logged-shaped, and useful,
  not a generic mist with a number in it. The HTTP status is
  a real 404; the theme never soft-404s with weather.
- **Failure fallback.** The page is the fallback pattern for
  the whole theme: if any other page's machinery fails
  catastrophically, what remains should resemble this —
  clear, printed, navigable.
- **Reduced-motion variant.** Identical. There is nothing to
  reduce.
- **Performance budget & mobile variant.** The lightest page
  on the site: no loop runs (the shared loop is not even
  started — the build ships this page without the weather
  script, ≤20KB total). Mobile: identical structure, stacked.
- **Choreography timeline (v2).** t=0: the page is printed.
  That is the timeline. (The gate checks this section's
  timeline by confirming no animation exists to describe.)
- **State matrix (v2).** *Rest:* printed, clear, still.
  *Hover:* link underline. *Focus:* fog-white ring.
  *Active:* n/a. *Scrolled-past:* the page rarely scrolls;
  if it does, nothing changes. *Disabled / no-JS:* identical
  — this page is the no-JS state of the whole theme, arrived
  at on purpose. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px: the
  same short page; only the measure narrows. No element is
  cut at any size — there is nothing spare to cut.
- **Edge cases & failure modes (v2).** *A 404 for a page
  that exists but errored (500 dressed as 404):* refused —
  the dry page is for missing entries; a server error gets
  the log's apology page (a sibling pattern, same stillness,
  different line). *Search engines:* the page returns a true
  404 status and `noindex`. *The requested path contains
  markup:* it is printed escaped, always — the keeper's line
  is text, never HTML.
- **Accessibility spec (v2).** The status line is the `<h1>`;
  the page is a model of the theme's clarity law with the
  weather removed: every word at full contrast (fog white on
  cypress-deep 10.90:1), focus visible, reading order exact.
  It is the page the gate's auditors are sent to when they
  ask what the theme's content looks like with nothing
  performed on it.
- **Tokens consumed (v2).** `--cypress-deep`, `--fog`,
  `--mist`, `--rust-pale`. (No easing tokens. That is the
  point.)

## 7. Page application map

**Home.** The full weather system: hand-wipe hero (§6.1),
condensing sections (§6.2) in the declared ground order (§4),
corner droplets (§6.3), the margin mesh filling (§6.4), the
one pinned vineyard clear (§6.5) at the page's middle, the
counters (§6.6) in the science band, cards (§6.13) capped at
six, the tank footer (§6.17). The home page is the only page
licensed to run every element; it is also the page the density
ration (§4) is audited on, because it is where a builder will
try to spend it all at once.

**Listing (the season's wines / the visit mornings).** A
ledger page wearing light weather: the season table's grammar
(§6.14) extended into a listing — rows, not a wall of cards;
at most three featured panes (§6.13) above the ledger for the
season's principals. Condensation applies to sections, never
to rows: a listing's rows are read comparatively, and §1's
clarity-at-the-reading-line is satisfied by the section curve
alone. No pin. The mesh (§6.4) fills by section as always.

**Detail (one wine, one visit, one tank).** The detail page
starts at the clearing: hero is a speckled frame (§6.8) at
full measure — no hand-wipe (the wipe is the home hero's
signature; a detail page the visitor chose to open does not
make them wait behind glass). Facts in the log's voice, the
figure lines from the record, the harvest form (§6.15) at the
foot in its booking variant. One bank at the head, sections
condensing normally.

**About / the ridge (the place and the crew).** The
photography page: speckled frames (§6.8) carry it, the
collector diagram (§6.7) appears here in its second licensed
home if the science section lives on this page instead of the
home (the diagram exists once per site section-plan, §15 —
never twice on one site at two sizes pretending to be two
diagrams). Banks run slightly taller (the place *is* weather)
within the §4 ration.

**Science / the log.** The counters (§6.6), the diagram
(§6.7) and the season table (§6.14) in their canonical order:
claim, instrument, record. This page is the audit surface —
the gate's three-printings check (§10) is performed against
it — so it carries the least decoration of any page: banks at
minimum height, no cards, no pin.

**Contact / visit (conversion).** The harvest form (§6.15) as
the page's centre, one bank, the log's practical facts
(directions, the ridge road's fog warning — real information
in the log's voice) beside it. No counters, no pin: a page
someone visits to *do* something gets the clearest weather on
the site.

**The dry page (404).** §6.18. No weather, by law.

## 8. Worked examples

The site in all three: **Alto Niebla Vineyard**, on the ridge
above Chungungo — 1,260 m² of mesh, a vineyard watered by fog,
selling a wine, a visit, and a place on the harvest list. The
yield object (§6.6) is the site's single source: A = 1,260 m²,
R = 4.6 L/m²/fog-day, D = 84 fog-days this season, L = 486,864
L; the ten-year mean is 212 fog-days, a 1,228,752-litre mean
season.

### 8.1 The hero (home)

**Build.** The page opens on fog white. At the head, the fog-
line navigation (§6.12) with its full 28px skirt. Below it,
the hero bank (§6.11 printed stratum) and, at the bank's foot,
the headline — "The vineyard that drinks the fog" (7 words,
Newsreader 64px) — printed in the DOM at full contrast, with
its veil duplicate above it (§6.1's structure). The standfirst
in Newsreader italic: *"No rain falls here. The water arrives
sideways, and we catch it."* In the left rail, the mesh (§6.4)
stands drawn and empty: 9 cells for the home page's 9
sections. The drip channel (18px) waits beneath the headline's
final letter.

**Scroll timeline.** t=0 (load, first visit): fonts race
(800ms cap) → the wipe begins: a 120px patch opens at the
headline's optical centre and grows on `--ease-wipe`; rim
beads swell as the rim passes them. t=1600: veil removed; the
headline stands clear. t=1750–2450: the drip bead forms
beneath the final "g", falls at t=2450, lands t=2830. The
standfirst's section arms its condensation (§6.2). The
visitor scrolls: the nav skirt compresses at 140px; the
standfirst condenses to C=1 as it crosses the reading line;
the first corner droplets (§6.3) gather at its corners at 60%
entry — *before* it is fully clear, cause before effect; cell
1 of the mesh swells and settles. By the time the visitor has
read the standfirst, they have wiped a pane, watched water
gather and run, and filled the first cell of a collector —
the site's entire argument, performed three times at three
scales, inside the first screen and a half.

### 8.2 Mid-page: the long clear and the instrument (home)

**Build.** Section five of nine, on fog ground: the pinned
vineyard stage (§6.5) — the photograph of Alto Niebla's rows
at dawn, the mesh poles visible along the frame's top edge,
fog layer at 90% with its 30vh skirt; the caption printed in
the stage's lower third: *"Block 3, looking east. The poles
along the top of the frame are the collectors; the rows below
them have never been irrigated from a well."* Below the pin,
the science section on cypress: the mesh diagram (§6.7) in
the margin-adjacent layout, the counters band (§6.6) beneath
it, its three source lines printed.

**Scroll timeline.** The stage pins. q 0→0.5 across the first
75vh of travel: the fog thins 0.90→~0.37 — the rows are
*ghosts*, poles first (they stand highest, and the skirt
rises from the ground). The caption was never covered; what
changes is that its photograph arrives to meet it. q 0.85:
fog at ~0.08, the rows fully legible, the copy's claim —
poles at the frame's top — now checkable by eye. q 1.0: the
fog layer is removed, the pin releases, cell 5 fills in the
rail. The science section condenses (§6.2) as it travels;
when the diagram's centre crosses the reading line, it draws
itself in build order — poles, mesh rows, drip line, gutter,
tank — 1800ms, labels landing with their parts; the tank's
fill rises to 40% (84 of 212, computed). The counters fire
as the band centres: litres from 428,440 (88%) to 486,864
over 1400ms, then the droplet drops into the figure. The
visitor has now seen the water arrive (the clear), the
instrument that catches it (the diagram), and the amount
(the counters with their arithmetic printed) — claim,
instrument, record, in the order §7 prescribes for the
science page, here folded into the home page's middle.

### 8.3 Conversion: the fog-morning visit (visit page)

**Build.** The visit page carries one bank, the log's
practical facts (the ridge road, the 8 a.m. start — "the fog
is a morning thing; by eleven the ridge is clear and so are
we"), and the harvest form (§6.15) in its booking variant:
name, direction, the choice as mesh-cell radios — *A morning
on the ridge*, *A morning + the tank room*, *The harvest
list* (no date needed) — a date field for the first two, and
the rust submit: "Enter it in the log." The form's head line
reads: "The log holds 214 entries. The March mornings are in
it up to the 21st." — the count printed from the record, the
scarcity stated as a fact of the log, not as pressure (§12).

**Scroll timeline.** The page's sections condense lightly
(banks at minimum height — §7's conversion rule). The visitor
focuses the name field: its rule inks cypress over 260ms.
They choose *A morning on the ridge*: the cell's droplet
swells in (450ms) — they have put water in the mesh by
choosing. They mistype the direction without an @: on submit,
the form does not fog or shake; the direction's rule turns
`--rust-deep`, the keeper's line appears beneath it — "That
direction will not carry — the @ is missing, looks like." —
focus moves to the field, their writing intact. Corrected,
they submit: the button presses, past 600ms it reads
"Entering…", then success — a droplet runs the form's right
edge (700ms) into the foot tank, whose line rises one unit,
and the confirmation replaces the form as the log's next row:
"Entered as № 215 — a morning on the ridge, the 14th of
March, for [their name]. The log will write to [their
direction] before the fog does." The number is the printed
count + 1, the date is the one they chose, the promise is the
site's real one. Nothing on the page performed urgency;
everything on it performed record-keeping, which is why the
visitor believes it.

## 9. Anti-slop — what makes THIS theme look cheap

Each failure is named as it appears in the wild, with its
cause and its cure. The gate (§10) tests for the blocking
ones.

1. **The whiteout.** Fog layered on fog — bank over condensing
   section over veiled card — until the page is a milk bottle.
   *Cause:* every element's fog authored independently, nobody
   counting the sum. *Cure:* §4's density ration (35% live fog,
   20% text-bearing) is a budget with an auditor, not a vibe;
   §6.9's composition rule keeps veiled cards out of early-
   condensing sections.
2. **Blur as a screensaver.** Blur on photographs, on hover,
   on modals, on the hero image — the theme's one serious
   material sprayed everywhere until it means nothing.
   *Cause:* "blur-to-sharp" read as a house style instead of a
   rationed state. *Cure:* §5's refusal list — blur exists
   only as §6.1's veil duplicate (14px) and §6.2's fog state
   (6px cap), each with its floor and its watchdog.
3. **The curtain.** A section caught mid-blur at the reading
   line; a visitor reading through moving fog; a reveal that
   never completes on a flung scroll. *Cause:* scrub without
   latch, snap or watchdog. *Cure:* §1 clause 1, implemented
   as §6.2's three guarantees (printed DOM, observer fallback,
   scroll-end snap) — and tested in §10 at three scroll
   speeds, including a fling.
4. **Rain-machine droplets.** Droplets everywhere, looping,
   falling forever — corner runs on every card, beads on every
   heading, a page dripping like a broken gutter. *Cause:*
   the droplet is charming, so it gets spent like confetti.
   *Cure:* the droplet budget (§5 ledger, §6 counts): corner
   runs once per section, one bead per card per click, one in
   the counters, one in the table, one in the form — each
   counted, each once. Water that falls forever is a leak.
5. **The grey dot.** Droplets drawn as flat grey circles with
   no specular, no sage body — beads that read as bullet
   points. *Cause:* the droplet treated as a shape instead of
   a material. *Cure:* §2's droplet spec (sage-deep body, one
   specular point at 55% white, bottom-weighted) is the only
   licensed drawing of water in the theme.
6. **Counters from zero.** Litres counting up from 0, as if
   the collector started when the page loaded. *Cause:* the
   default count-up pattern, imported unexamined. *Cure:*
   §6.6's from-88% rule and its reason, printed in the spec:
   the harvest predates the visitor, and the count's job is
   to arrive at the truth, not to perform accumulation.
7. **Fog on a feed.** Forty posts condensing in sequence, a
   listing's rows blurring comparatively, a dashboard fogging
   its tables. *Cause:* the theme applied as a skin over
   content it was never shaped for. *Cure:* §1's when-NOT list
   and §7's listing rule (sections condense; rows never do).
   If the content is a feed, the answer is another theme.
8. **The reactive bank.** Fog that follows the pointer across
   sections, banks that swell on hover — weather turned into
   a pet. *Cause:* ambient layers given interaction because
   interaction was available. *Cure:* §6.11's rule — the
   pointer's only fog gestures are the card wipe (§6.9) and
   the hero's tap-to-complete; the weather itself ignores the
   visitor, which is what makes it weather.
9. **Rust on the trees.** The tank colour printed on cypress
   (1.89:1 — illegible and ugly), rust buttons on dark
   sections, a rust footer band. *Cause:* the accent treated
   as a brand colour rather than a material with a home.
   *Cure:* §2's forbidden pairings are gate-greppable: rust
   lives on fog ground, in the tank, the seal and the marks —
   or it does not appear.
10. **The invented litre.** Yield figures with no source line,
    a tank level chosen because it "looked right", counters
    and footer disagreeing by a rounding nobody declared.
    *Cause:* numbers treated as copy. *Cure:* §1 clause 2 —
    one yield object, source lines as part of the figure
    (§6.6), three-printings audit (§10). A fog site that lies
    about water has nothing left.
11. **The apology skeleton.** A loading state that sits fogged
    for six seconds because a region is slow, teaching the
    visitor that fog means *broken*. *Cause:* no ceiling.
    *Cure:* §6.16's 3000ms hard ceiling with in-place error
    lines — fog may represent waiting for three seconds; past
    that it must admit what it is.
12. **Dripping chrome.** The browser's own furniture dressed
    in fog: fogged modals, a fogged cookie banner, blur on the
    OS dialog's web cousin. *Cause:* theme leakage past the
    page's edge. *Cure:* §11's inventory — system surfaces
    (alerts, the one licensed dialog pattern) print plainly on
    fog ground with no veil; the weather belongs to the site's
    content, not to its obligations.

## 10. Quality gate

Blocking items must all pass before the theme may be used in
a build. The gate is run by someone who did not build the
page (§15), against a production build, on a real device
profile — not the builder's monitor.

**Blocking**
1. **Clarity-at-the-line test.** At three scroll speeds
   (reading pace, brisk, full fling), every section reaches
   C=1.0 (blur 0, opacity 1) no later than its reading matter
   crossing the 55% line, and no section is ever rendered
   below the 0.40 floor. (§1, §6.2)
2. **Clarity-function audit.** Three sampled sections'
   rendered blur/opacity match §5's published function to the
   pixel at three scroll positions each.
3. **Dead-JS test.** With JavaScript disabled, the page is
   complete and clear: hero printed, sections readable, mesh
   beaded, counters at truth, diagram drawn, form submittable.
4. **Figure-truth audit.** `A × R × D` is recomputed from the
   yield object and compared against all three printings
   (§6.6 band, §6.14 totals row sum, §6.17 tank label);
   the season table's rows sum to its totals row exactly.
5. **Density audit.** Screenshot sampling at six scroll
   positions: live fog ≤35% of viewport, text-bearing fog
   ≤20%; rust pixels ≤3%.
6. **Blur census.** Grep + render check: blur exists only at
   §6.1 (≤14px, veil duplicate) and §6.2 (≤6px sections);
   no other element computes a blur at any state.
7. **Droplet census.** Count droplet acts on a full page
   traversal against §9.4's budget (sections + 1 counters +
   1 table + 1 form + per-click beads); any looped or
   uncounted droplet fails.
8. **Contrast audit.** Every text pairing measured at rest:
   body 12.45:1, apparatus ≥5.87:1, card headline under its
   resting veil ≥4.5:1, footer links ≥8.02:1 (mist) / 10.90:1
   (fog white); forbidden pairings (rust on cypress, sage on
   cypress, sage text <24px) absent.
9. **Watchdog drill.** With the shared loop artificially
   stalled, every armed element reaches its printed state via
   its fallback within its stated watchdog (hero 2400ms,
   sections 1200ms, skeleton 3000ms, pin 4000ms).
10. **Reduced-motion pass.** With `prefers-reduced-motion`,
    the page is the finished clear page: no pin, no wipe, no
    drift, no runs; all information present in the same order.

**Advisory**
11. The five-second test: a first-time visitor, shown the
    hero for five seconds, can say what the site harvests.
12. The Chungungo test: the credit line is present, verbatim
    in spirit — the water's source is named as provenance
    somewhere on every page (footer minimum).

## 11. Component inventory

Every component a real Fog Harvest site needs, with its themed
treatment. Components the theme refuses are listed with the
refusal's reason and the in-theme replacement — a refusal
without a replacement is a gap, and there are no gaps.

| Component | Treatment in this theme |
|---|---|
| Primary button | The tank button: `--rust` rectangle, fog-white text, radius 0, press = 1px translate (§6.15). One per view. |
| Secondary button | Fog-ground, 1px `--cypress` rule, cypress text; hover fills `--mist` 40% over 200ms. |
| Text link | `--sage-deep` with a drawn rule (220ms); in the footer, fog white with `--rust-pale` draw. |
| Navigation | The fog-line navigation (§6.12). |
| Hero | Hand-wipe hero (§6.1) on home; speckled frame (§6.8) on detail pages. |
| Cards | Condensation cards (§6.13), max 6 veiled per page. |
| Data table | The season table (§6.14) — the only table pattern; max 5 columns. |
| Form fields | Log-ruled fields (§6.15): mist rule, inking to cypress on focus, `--sage-deep` at rest when filled. |
| Radio / choice | Mesh-cell radios (§6.15): diamond cell, droplet on choice. |
| Checkbox | A single mesh cell, squared: droplet in the cell when checked; label in the log's voice. |
| Select | **Refused** — a native dropdown is a machine part in a weather page. Replacement: mesh-cell radio rows (§6.15) for ≤6 options; a listing page (§7) for more. |
| Tabs | **Refused** — a fog page is read downward like weather arriving; it does not file itself. Replacement: sections + the fog-line nav's scrollspy bead. |
| Accordion | The log's drawer: a ruled row whose content condenses open (600ms `--ease-condense`) — one licensed pattern, for the visit page's practical questions only. |
| Modal / dialog | **Refused as overlay.** Replacement: the fog roll (§6.16) to a dedicated page, or an in-flow expansion (the accordion pattern). The one exception — a legal consent that must interrupt — prints as a plain fog-ground panel in flow, unveiled (§9.12). |
| Toast | **Refused.** Replacement: a log line — a printed entry appearing at the head of the relevant section in the keeper's voice, persistent until dismissed by reading (§12). |
| Tooltip | **Refused.** Replacement: the caption and the source line — if a figure needs explaining, its provenance prints beside it (§6.6), not on hover. |
| Progress bar | **Refused.** Replacement: the collector mesh (§6.4). |
| Spinner | **Refused.** Replacement: the fogged skeleton (§6.16) with its 3000ms ceiling. |
| Pagination | **Refused** for the log and the table (the record is whole). For long listings: the bank index — a single link row ("Earlier seasons") to whole pages; a season is not sliced. |
| Badge / tag | The droplet chip: a small fog-ground lozenge (the theme's one radius, 999px, because a chip is a bead flattened — §4's exception, named) with a 6px droplet dot and a Source Sans label. Used for states the log must state ("Full", "In the log"), never for marketing. |
| Alert / notice | A log entry panel: fog ground, 2px `--cypress` left rule, keeper's voice, printed — never veiled, never auto-dismissing (§9.12). Errors in forms use `--rust-deep` (§6.15). |
| Breadcrumbs | **Refused** — sites in this theme are shallow (≤3 levels) by §1's fit; the fog-line nav + the section's own bank carry orientation. Deeper sites choose another theme. |
| Search | A log lookup: one ruled field (§6.15 pattern) on its own page; results as season-table rows (§6.14 grammar), each row's fog state: printed, never condensing comparatively (§7 listing rule). |
| Image | Speckled frames (§6.8); diagram figures (§6.7) for instruments. |
| Footer | The tank footer (§6.17). |
| 404 | The dry page (§6.18). |
| Focus ring (cross-cutting) | `--cypress` 2px, 2px offset on light grounds; fog white 2px on cypress grounds. Never sage (3.00:1 is not a focus indicator), never rust. |
| Radius law (cross-cutting) | 0 everywhere — glass is cut square — except the droplet chip (999px, a flattened bead) and the droplet itself. A builder who rounds a card has brought another theme's furniture. |

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the palettes.

**The Keeper** — the site's voice: the person who tends the
mesh and writes the log. Weather-plain, unhurried, concrete.
Speaks of fog, water, mornings and work in short sentences.
Never sells; states. Headlines are claims about the place
that the page then verifies ("The vineyard that drinks the
fog" — verified by §8.2's photograph). Maximum 9 words for a
display line; a headline that needs a tenth word is two
headlines arguing.

**The Log** — the data's voice: figures, source lines, table
apparatus, form errors, empty states. Numerals with their
provenance attached, always. The Log never rounds silently,
never exclaims, and — the register's signature — *the Log
admits*: a dry month is printed, an error is owned, a stale
count is labelled with its date.

**Headline style.** ✓ "The vineyard that drinks the fog."
✓ "Eighty-four mornings of fog, so far." ✗ "Unlock the power
of atmospheric moisture!" ✗ "Welcome to Alto Niebla —
est. 2016, family-owned, award-winning…" (a headline is not a
brochure's first paragraph).

**Label style.** Labels are log entries: noun + fact. ✓
"Litres this season — 486,864". ✓ "March mornings — full to
the 21st". ✗ "Amazing yield!!" ✗ "Hurry — only a few left!"
(scarcity on this site is a printed fact of the log with a
date on it, §8.3, or it is not said).

**Error voice** (the Keeper, correcting a log entry — never
the machine, never the visitor's fault). ✓ "That direction
will not carry — the @ is missing, looks like." ✓ "The date
wants a day as well as a month." ✗ "Invalid email format."
✗ "Oops! Something went wrong." (The Log admits specifics or
it says nothing.)

**Empty-state voice.** ✓ (the dry month, in the table) "0
fog-days — the dry month. The tanks held." ✓ (a new site's
footer) "The log opens with the autumn bank. Nothing is
entered yet, and nothing is invented for the space." ✗ "No
data available." ✗ Any empty state that fills itself with a
decorative fog bank and a apology — the dry page (§6.18) is
the model: stillness and a fact.

**Banned words & constructions.** "Unlock", "supercharge",
"seamless", "leverage", exclamation marks in the Log's
register (the Keeper may have one per page, and the worked
examples have none), percentages in progress contexts (the
mesh is the fraction, §6.4), "content" for the site's own
material (it is *the season*, *the log*, *the wine*), and any
yield figure without its source line within the same figure.

**Owned words.** Fog, bank, mesh, ridge, log, tank, morning,
the clearing, to condense (used literally, of the page and
the weather alike), watered by fog.

**Verbatim fixed strings** (builders do not paraphrase):
- The credit: *"This page, like our vineyard, is watered by
  fog."* (§6.17)
- The dry page's line: *"The tanks hold what they held."*
  (§6.18)
- The form's submit: *"Enter it in the log."* (§6.15)
- The skeleton's status (visually hidden): *"The page is
  condensing."* (§6.16)

## 13. Full-page scroll choreography map

The home page (§8's site), top to bottom, nine sections. Every
beat names what the visitor sees and what it is *for*; a beat
with no purpose is cut, not kept.

1. **Load.** Nav banked (§6.12), mesh empty in the rail, hero
   behind its veil. The visitor understands: something is
   behind glass.
2. **The wipe (0–1600ms).** The hand clears the headline; rim
   beads gather. *The site's transaction, performed once.*
3. **The drip (1750–2830ms).** One bead falls from the final
   letter. *Fog becomes water — the thesis, in one drop.*
4. **First scroll.** Nav compresses (140px); standfirst
   condenses to the reading line; its corner droplets gather
   *before* it clears (cause, then effect); mesh cell 1 fills.
   *The reader learns the page's physics by using it.*
5. **The offer panes.** Six cards (§6.13) condense with their
   section; the visitor's pointer wipes one; a click sends
   its droplet down and off. *Inspection as touch; the offers
   are panes, not posters.*
6. **The long clear (section 5).** The pin: 150vh of fog
   thinning off the vineyard photograph, poles first, rows
   last. *The morning, at full length — the page's centre of
   gravity.*
7. **The instrument (section 6, cypress).** The diagram draws
   itself in build order; the counters count from 88% and
   take their droplet; the season table waits below, printed.
   *Claim → instrument → amount, in that order.*
8. **The record (section 7).** The season table; its totals
   droplet runs as the totals row arrives. *The audit trail,
   typeset — belief, having been earned, is now documented.*
9. **The form & the tank (sections 8–9 + footer).** The
   harvest form in its log ruling; the visitor who enters is
   entered. The footer tank rises to 40% as it arrives; the
   credit line is the last thing read. *Everything the page
   gathered is in the vessel; the last line names the source.*

**Reverse pass.** Scrolling up: read sections stay clear
(ratchet, §6.2); the mesh stays filled; counters stay at
truth; the vineyard photograph alone may re-fog below q=0.02
(§6.5's licensed reversal — unread weather may return; read
text may not). The visitor going back up reads a clearer page
than the one they came down, which is correct: they have
harvested it.

**Jump scroll.** An anchor jump or a scrollbar drag to the
foot: everything above the reading line snaps clear in order,
the mesh queue fills in one staggered pass (§6.4), counters
stand at truth uncounted, the pin is skipped entirely (its
stage renders clear). The page never makes a jumping visitor
watch the weather they skipped.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 780KB | Of which images ≤ 520KB (the vineyard photograph is the spend; it is also the LCP) |
| Weather script | ≤ 38KB gz | The shared loop, clarity function, and all §6 acts |
| Inline SVG (mesh + diagram + tank) | ≤ 20KB total | §6.4 ≤6KB, §6.7 ≤8KB, §6.17 ≤6KB |
| Fonts | Newsreader (2 weights + italic) + Source Sans 3 (2 weights), subset, ≤ 120KB | `font-display: swap` with the §6.1 font race as the guard |
| Frame budget | ≤ 1.6ms of JS per frame in the shared loop | The loop computes values; CSS/compositor applies them. At most 2 live blur filters + 6 transform layers at any moment (§6.2, §6.9 caps) |
| Long tasks | None > 50ms after load | The mesh/diagram SVG parsing is the risk; both are inline and small by the caps above |
| CLS | 0.00 target, 0.02 ceiling | §3 law 2 (condensation changes no layout) and §6.16 (skeleton = real layout) are the mechanisms |

**Cut order** (when a build exceeds budget, cut in this
order — never improvise):
1. The fog-roll transition (§6.16) — navigation goes plain.
2. Bank drift (§6.11) — banks stand static.
3. Corner droplet runs (§6.3) on sections below the fold —
   the first three sections keep theirs.
4. Speckle counts (§6.8) halve again; frame scale narrows.
5. The hero drip (§6.1) — the wipe stays; the drip is the
   ceremony's ornament, not its meaning.
6. Card tilt (§6.13) — the wipe (§6.9) stays; tilt is the
   cheapest loss.

**Never cut:** the printed-DOM guarantee, any watchdog, the
clarity floor, the source lines, the reduced-motion variants.
A build that ships fog without its fallbacks has not saved
weight; it has removed the theme and kept its riskiest
surface.

## 15. Build-order checklist

1. **Static page first.** The complete site, printed and
   clear, no weather script: every section readable, mesh
   beaded, counters at truth, diagram drawn, form working.
   This is the page §10's dead-JS test will grade — build it
   as a deliverable, not as a by-product.
2. **Tokens & type.** §2's closed token list (grep-gated),
   §3's scale and laws; the forbidden pairings encoded as
   lint rules, not intentions.
3. **The yield object.** One data source for §6.6/§6.14/
   §6.17; the three-printings audit wired into CI before any
   element that prints a figure is built.
4. **Layout.** Banks and clearings (§4), the rail, the
   reading-line constant shared by every trigger.
5. **The shared loop + clarity function.** §5's function
   implemented once, unit-tested against its published curve
   before any element consumes it.
6. **Condensing sections (§6.2)** with all three fallbacks;
   then corner droplets (§6.3) keyed to them.
7. **The mesh (§6.4)** — cell count audited against DOM
   sections at build time.
8. **The hero wipe (§6.1)** — after §6.2, because the
   standfirst's arming depends on the wipe's completion.
9. **The pin (§6.5)**, its watchdog, and the sub-400px-height
   pin-drop.
10. **Counters (§6.6), diagram (§6.7), table (§6.14)** — the
    science chain, in §7's order.
11. **Cards (§6.13) with wipe (§6.9) and droplet (§6.10)**;
    images (§6.8) with their speckle.
12. **Form (§6.15)**, nav (§6.12), footer (§6.17), banks'
    drift (§6.11) — the frame, last, because it is the part
    that may be cut (§14) and must therefore be the part
    least depended upon.
13. **Skeleton & transition (§6.16); the dry page (§6.18)**
    shipped without the weather script.
14. **Reduced-motion pass** — every element's variant
    verified against §10.10, on a device, not a toggle in
    devtools alone.
15. **The gate (§10)** run by a non-builder; failures return
    to the step that owns them. The theme ships when the
    gate passes, not when the weather looks nice in the
    builder's browser.
