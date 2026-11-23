# Theme 004 — Letterpress Atelier (Expanded)

Expansion of theme #4 in `themes-001-025.md`, written to the Expansion
Standard (20x depth). Identity preserved exactly: same concept, same palette,
same typefaces, same twelve signature elements — deepened to full build
specs, plus the page-family elements the original entry did not carry.

The one-sentence law of this theme: **nothing on the page travels — everything
deepens.** If an element translates more than 4px outside the two sanctioned
exceptions (sheet-lift reveal, platen transition), it is not this theme.

---

## 1. Concept & world

A working letterpress atelier at the moment of impression. The page is a
single sheet of cotton paper lying on the platen; every headline, rule,
border and image block on it has been physically pressed into the sheet by
type locked in a chase. Depth is real and optical: a raking light source
crosses the sheet as the visitor reads, so the highlight and shadow inside
every debossed glyph shift angle continuously while nothing on the page
moves. Ink is a material with coverage percentages, not a colour: fresh
sections arrive at 88% saturation and settle to 100% as their impression
lands, and in every large display word one letter — a worn sort in the case —
prints at 82% coverage forever.

The emotional register is slowness you can feel in your fingertips: the
resistance of a press handle, the tooth of cotton paper, the patience of a
craft where one sheet at a time is the production speed. This is the opposite
of a feed. A page in this theme should feel like it was made once, carefully,
for this visitor — because in the fiction of the theme, it was: the colophon
footer states the edition, and the edition is one.

**Best-fit sites and audiences**

- Wedding and event stationers selling suites (invitation, RSVP, menu,
  order-of-service) where the product *is* pressed paper.
- Boutique hotels and inns (12–60 rooms) whose physical collateral — key
  cards, menus, in-room notes — is letterpressed, and whose guests book on
  atmosphere rather than price comparison.
- Craft distilleries, binderies, small-batch roasters and perfumeries
  releasing numbered editions of 50–500 units.
- Print studios and paper mills selling commissions and stock by weight.
- Audiences: buyers aged roughly 30–60 who already pay premiums for physical
  craft; readers who will trade density for ceremony.

**When NOT to use it**

- Anything data-dense or scan-driven: dashboards, SaaS consoles, comparison
  tables, news. Deboss depth at small sizes destroys legibility, and this
  theme forbids body text below 15px.
- Dark-mode-first products. Paper is the material; there is no black version
  of a cotton sheet (see §2, dark-mode behaviour).
- Playful, loud, youth-consumer brands. The theme has no bounce, no overshoot
  beyond a 1.02 press settle, and no saturated colour beyond oxblood at 5%.
- Checkout flows longer than one screen. The commission slip (§6.16) is the
  only form pattern; multi-step wizards break the single-sheet fiction.
- Sites that must ship under ~150KB of CSS/JS on low-end devices in
  emerging-market conditions — the raking-light system (§5) needs a
  persistent rAF loop and layered shadows; the static fallback exists, but if
  the fallback would be the *majority* experience, choose another theme.

---

## 2. Palette

Four inks and the paper. Nothing else is ever introduced — no success green,
no link blue. Oxblood does double duty as the second ink and the
error/proofing colour, the way a real atelier reaches for the red pencil.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--paper` | `#F5F0E6` | The sheet itself: page background, card stock, skeleton base | ~68% of pixels | Reference surface for every contrast figure below. Never used as text on ink. |
| `--paper-tooth` | `#EAE0CB` | The shadow side of the paper grain; skeleton fills, un-inked areas, image placeholder blocks | ~12% | Only ever adjacent to `--paper`; the 6% luminance step between them is the grain, nothing stronger. |
| `--ink` | `#14424A` | Deep teal: primary ink — all body text, display type, rules, borders | ~14% | On `--paper`: contrast ≈ 9.4:1. The only colour allowed for text under 24px. |
| `--ink-88` | `#14424A` at 88% | Pre-impression state of any inked element (see §5, impression-on-entry) | transient | Never a resting state. An element photographed at 88% is mid-press. |
| `--ink-82` | `#14424A` at 82% | The under-inked letter (§6.2) — worn-sort coverage | 1 glyph per display word | Decorative by definition; never applied to body text, prices, or form labels. |
| `--oxblood` | `#6E1F24` | Second ink: kickers, proof marks, form errors, the "sold out" stamp, hover state of primary buttons | ~4% | On `--paper`: contrast ≈ 7.6:1 — passes for text at any size, but rationed so it always reads as an event. |
| `--brass` | `#A67C2E` | Metal furniture only: the progress rule, ornament, focus ring, active-nav marker, seal | ~2% | On `--paper`: contrast ≈ 3.4:1 — **never text, never an icon that carries meaning alone**. Brass is touched, not read. |
| `--deboss-hi` | `#FFFDF6` | The highlight lip inside every deboss (light side) | shadow layer only | Always paired with `--deboss-lo` in the same shadow stack; never a fill. |
| `--deboss-lo` | `rgba(20,66,74,0.30)` | The shadow lip inside every deboss (dark side) | shadow layer only | Derived from `--ink` so the depth always belongs to the ink, not to a grey. |
| `--hairline` | `#14424A` at 35% | Hairline rules, table leaders, field underlines on the commission slip | hairlines only | At 35% it prints as a pencil-faint rule; anything structural uses full `--ink`. |

**Dark-mode behaviour:** this theme does not invert. A `prefers-color-scheme:
dark` visitor gets the **pressroom-at-dusk variant**: `--paper` warms to
`#EFE5CF`, `--ink` deepens to `#0F333B`, the raking light locks to its lowest
angle (28°, §5) and stops scrubbing — the sheet is being read under one lamp
at night, not glowing. Ratios above are preserved within 0.3:1. A true black
background is a different material and a different theme.

**Ink-coverage discipline:** saturation is spent like ink from a tin. A
viewport may contain at most: one oxblood element in motion, one brass
element in motion, and one breathing word (§6.8). If everything is special,
the sheet looks machine-printed — the exact failure this theme exists to
avoid.

---

## 3. Typography

Two families, both with physical manners. **Fraunces** (variable: `opsz`,
`wght`, `SOFT`, `WONK`) is the display face — high optical sizes, soft
serifs, slightly uneven colour at large sizes, which the theme treats as ink
texture rather than a defect. **Zilla Slab** is the text and apparatus face:
body copy, captions, data, form labels, the colophon.

| Role | Face & settings | Size / line-height | Tracking | Rules specific to this theme |
|---|---|---|---|---|
| Display (hero) | Fraunces, `opsz` 144, `wght` 560, `SOFT` 60, `WONK` 1 | 64px / 1.04 (desktop), 44px / 1.08 (mobile) | −0.015em | Subject to letter pressing (§6.1) and the under-inked letter (§6.2). Never set in oxblood — display is teal ink or nothing. |
| H1 (page title) | Fraunces, `opsz` 100, `wght` 540 | 52px / 1.1 | −0.01em | One per sheet. Receives impression-on-entry as a block (no per-letter press below the hero). |
| H2 (section head) | Fraunces, `opsz` 72, `wght` 520 | 38px / 1.16 | −0.005em | Always preceded by its brass ornament (§6.9) and followed by a 3px + 1px double rule. |
| H3 / suite name | Zilla Slab 600 | 22px / 1.3 | 0 | Slab, not serif — suite names are apparatus, like labels pasted on type cases. |
| Kicker | Zilla Slab 600, uppercase | 12.5px / 1.4 | +0.18em | The only uppercase setting on the sheet. Oxblood permitted; teal default. |
| Body | Zilla Slab 400 | 18px / 1.68 | 0 | Measure 58–66ch. Never below 15px anywhere on the sheet. Colour `--ink` at 100% only — grey body text is un-inked type and reads as a printing fault. |
| Caption / credit | Zilla Slab 400 | 14.5px / 1.5 | +0.005em | Used for paper credits ("600gsm cotton, deckle edge") under images. |
| Data (editions, weights, prices) | Zilla Slab 500, tabular figures (`font-variant-numeric: tabular-nums`) | 16–20px / 1.4 | 0 | All counters (§5) render in this style. Paper weights always stated in gsm, editions as "Edition of N". |
| Colophon / apparatus | Zilla Slab 400 | 13.5px / 1.6 | +0.01em | Footer only. Set like the back page of a book: face credits, paper credit, edition line. |

**Per-role rules that may not be broken**

- Fraunces is never used below 28px; below that its soft serifs fill in and
  read as blur, not craft.
- The under-inked letter (§6.2) appears once per display word, never on the
  same letter twice on one page, never on a word shorter than 4 letters, and
  never in the hero's first word (the first word must print clean — the press
  warms up *during* the headline, not before it).
- Line breaks in display type are set by hand in the markup (`<span
  class="line">`), because the press sequence (§6.1) and the sheet-lift
  reveal (§6.7) both choreograph per line. Automatic wrapping at a new
  breakpoint re-flows the lines but never re-orders them.
- Numerals in prose are oldstyle (Zilla Slab default); numerals in data are
  tabular. The two never mix in one line — a price inside a sentence is set
  as data and breaks the sentence's rhythm deliberately, like a stamped
  figure on a printed form.

---

## 4. Layout language

**The sheet.** Every page is one sheet of cotton paper, full-bleed
`--paper`, with the paper-tooth grain (§5) fixed beneath the content. There
are no cards floating on a grey app background, no drop-shadowed panels —
the sheet is the ground, and everything on it is printed, locked, or laid
on it.

**The module: one-eighth of type-high.** Real type-high is 0.918 inch ≈
88px at 96dpi. The spacing system divides it: the base unit is **11px**
(88 ÷ 8). All spacing is a multiple of 11: section padding 132px (12 units)
desktop / 66px (6 units) mobile; block gaps 22 or 33px; the double-rule gap
is 5.5px (half unit) — the only half-unit allowed, because it is a printed
rule, not layout air.

**Grid.** A centred specimen composition. Reading column 62ch maximum,
centred. Specimen spreads (alphabet, suites) may open to a 12-column grid
across 76rem, but the text column always re-centres inside it — the eye
should feel the sheet's centre line even on wide sections. Margins are
unprinted paper: minimum 8vw on desktop, 22px (2 units) on mobile, and
margin space is never filled with sticky widgets or rails. The brass
progress rule (§6.6) is the only element allowed to live in the margin,
because it is furniture, not content.

**Type-high borders.** Image blocks and suite cards are framed as type
blocks locked in the chase: an outer rule 3px solid `--ink`, a 5.5px gap of
bare paper, an inner rule 1px solid `--ink`. No radius, ever — type blocks
are square. The frame is part of the block: when the image settles
(§5, image treatment), it settles *inside* this frame, and the frame itself
receives impression with its section.

**Section choreography.** Sections alternate two rhythms only: **specimen**
(centred, symmetrical, one idea, generous air — hero, alphabet, ornament
breaks) and **ledger** (left-aligned reading column with data set as
apparatus — editions, papers, prices). A page may not introduce a third
rhythm. Between sections, the brass ornament (§6.9) is the only divider;
there are no background-colour bands on the sheet, because paper does not
change colour halfway down.

**Density rules.** Maximum one display headline, one pinned scene, and
three animated elements visible per viewport. Whitespace is spent the way
the atelier spends cotton paper: the most expensive material on the page,
used to make the printed parts feel pressed rather than placed.

---

## 5. Full motion system

One engine drives almost everything: **the raking light.** A single
`requestAnimationFrame` loop lerps a scroll-progress value (factor 0.085)
and maps it to a light azimuth from **118°** at the top of the page to
**62°** at the bottom. The azimuth is published as two CSS custom properties
(`--lx`, `--ly`, the light vector) and every deboss shadow on the page is
computed from them — so when the light moves, *all* depth on the sheet moves
together, the way one lamp lights one sheet. Nothing else on the page runs a
scroll listener.

Named easings, used verbatim everywhere below:

- `press-out` — `cubic-bezier(0.22, 1, 0.36, 1)` — the platen coming down:
  fast commitment, long settle. All impression animations.
- `ink-settle` — `cubic-bezier(0.4, 0, 0.2, 1)` — colour and saturation
  changes (the 88% → 100% settle).
- `sheet` — `cubic-bezier(0.65, 0, 0.25, 1)` — paper moving against air
  resistance; used only by the sheet-lift and the platen transition.
- `thud` — `cubic-bezier(0.3, 1.4, 0.5, 1)` with a hard 120ms cap — the
  click press. The overshoot lives in shadow depth, never in scale beyond
  0.99.

Every motion term, in this theme's language:

| Motion term | Letterpress translation | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveal | **Impression-on-entry**: the section is pressed as it arrives — deboss depth 0 → 100%, ink 88% → 100%, zero translation | 700ms `press-out` (depth), 900ms `ink-settle` (saturation) | IntersectionObserver, section top crossing 78% of viewport height |
| Parallax | Three strata only: paper-tooth grain fixed (0×), body type drifts 2px over a section's traverse (0.98×), the pinned specimen's examples move at full speed (1×). Total relative shear never exceeds 3px | Continuous, from the light loop's lerped progress | Scroll |
| Pinned scene | The specimen alphabet (§6.5) pins for exactly 100vh while usage examples scroll past it | Pin 100vh; examples traverse at 1× | Scroll, specimen section |
| Masked line reveal | **Sheet-lift** (§6.7): the covering sheet lifts off the printed image, clip-path inset animating from the bottom edge, a soft paper shadow riding the lifting edge | 900ms `sheet` | Load (hero) / scroll entry (later images) |
| Blur-to-sharp reveal | **Ink sharpening**: pressed letters land with a 0.7px blur (wet ink spread) that contracts to 0 as the impression completes — sharpness is dryness | Blur resolves inside the 380ms press of each letter, `press-out` | Load, per letter (§6.1) |
| Animated counters | Edition sizes and paper weights count in tabular Zilla Slab, one digit column rolling like a numbering machine's wheel | 900ms `ink-settle`, staggered 60ms per digit column | Scroll entry of the data block |
| Progress indicator | **Brass-rule ink progress** (§6.6): the margin rule fills with teal ink; the fill front is a meniscus, not a hard edge | Scrubbed to lerped scroll progress | Scroll |
| Marquee | **The sorts tray drift** (footer only): one line of oversized Fraunces glyphs — `& A a E e G g R r ſ` — drifts left at 9px/s across the colophon, as if a compositor's tray were sliding past. The only horizontal loop on the sheet | Linear, 9px/s, seamless at 2× content width | Always (footer in view); paused off-screen |
| Ambient loop | **Breathing hero word** (§6.8): one word's `opsz` swells ±6% on a 5s loop; paper grain brightens almost imperceptibly as the light passes (§6.3) | 5s ease-in-out, alternate | Time, hero in view |
| Micro-interactions | **Press-harder hover** (§6.10): depth +30% under the pointer; light-angle on cards tilts ≤3° toward the pointer | 200ms `press-out` | Hover / pointermove (throttled to the light loop) |
| Hover physics | No bounce, no lift. A hovered block is *pressed*, so its shadow deepens and its scale goes to 0.995 — the page pushes back with paper resistance, eased `thud` without the overshoot | 200ms in, 260ms release | Hover |
| Page transition | **Platen transition** (§6.12): fresh sheet slides up onto the platen and takes its impression | 620ms total: 260ms `sheet` slide, then 360ms `press-out` impression | Route change |
| Image treatment | Photographs print as **duotone plates**: teal-ink duotone at 92% contrast, scale-in-frame 1.06 → 1 inside the type-high border, settling with the section's impression. Colour photography is never shown raw on the sheet | 800ms `press-out` | Scroll entry |
| Skeleton loading | **Un-inked skeleton** (§6.11): type and blocks present at 12% ink, filling to full as content arrives | 500ms `ink-settle` per block, staggered 80ms | Load state |
| Kinetic typography | Only two sanctioned forms: the per-letter press (§6.1) and the breathing word (§6.8). No sliding, bouncing, or rotating type anywhere else — type on a press does not dance | — | — |
| Reduced motion | Light locks at 40°. Everything renders pre-pressed at 100% ink. Transitions become a 150ms opacity crossfade. Counters print their final figures. See each element's variant in §6 | — | `prefers-reduced-motion: reduce` |

**Global motion budget.** At any moment: ≤ 3 elements mid-animation per
viewport, 1 rAF loop total, shadow stacks ≤ 3 layers per element, and the
light loop sleeps when the tab is hidden or the page has not scrolled for
2s (waking on the next scroll event). If a device reports
`hardwareConcurrency ≤ 2` or the first impression frame takes > 50ms, the
build degrades to the mobile variant of every element (§6) automatically.

---

## 6. Signature elements — full build specs

The twelve elements of the original theme, in the original order, each with
its full spec — then the page-family elements (§6.13–§6.17) the original
entry lacked. Shared conventions for every spec below: base CSS always
describes the **final, fully printed state**; JavaScript adds a `data-press`
attribute to arm an animation's start state, so a no-JS or failed-JS page is
simply a printed page. A global watchdog (§6.11) forces the final state of
anything still armed after 1000ms.

### 6.1 Sequential letter pressing

- **What & why.** The hero headline is set in the chase sort by sort: each
  letter presses in individually — scale 1.04 → 1, deboss depth 0 → 100%,
  blur 0.7px → 0 — in reading order. It belongs to this theme because on a
  real press the headline quite literally does not exist until it is
  pressed; the animation is the manufacturing process of the page's first
  sentence, not an intro effect.
- **Structure.** DOM only. The headline is split server-side (or at build
  time — never by a runtime splitter that delays first paint) into
  `<span class="sort">` per letter inside `<span class="line">` per
  hand-set line (§3). Each sort carries `text-shadow` built from `--lx/--ly`
  (§5). Spaces are un-animated gap spans so word rhythm survives.
- **Motion spec.** Per letter: 380ms `press-out`; stagger 45ms in reading
  order, line by line; the press of letter *n* starts when letter *n−1* is
  at ~60% depth, so the line ripples rather than ticks. Total for a 24-sort
  headline: ≈ 1.45s. Trigger: load, after fonts confirm via
  `document.fonts.ready` (pressing in a fallback face then swapping is a
  misprint).
- **States.** *Rest:* fully pressed, depth 100%. *Hover:* governed by
  §6.10 (per-letter press-harder). *Active:* n/a. *Scrolled-past:* static —
  the press never re-runs; a printed sheet does not re-print when you look
  back at it.
- **Content merge.** The letters are the headline. Removing the animation
  leaves the identical headline; the animation adds only the memory of how
  it got there.
- **Failure fallback.** Sorts render pressed by default; JS arms the
  un-pressed state only when it can also run the sequence. Watchdog: any
  sort still un-pressed at 1000ms is forced to final state in one frame.
- **Reduced-motion variant.** No sequence. The headline is simply printed;
  if the visitor has reduced motion *and* full data, the under-inked letter
  (§6.2) still applies — it is a state, not a motion.
- **Performance budget & mobile variant.** ≤ 40 sorts animated per page
  (hero only); animation touches `transform`, `filter`, and shadow vars
  only. Mobile: stagger tightens to 30ms and letters press per *word*
  (≤ 8 units) below 480px, because 24 sequential shadow animations on a
  low-end GPU smear the ripple into mush.

### 6.2 The under-inked letter

- **What & why.** In each large display word, one letter renders at 82% ink
  coverage and arrives last in the press sequence, staying permanently
  imperfect — a worn sort in the case. It is the theme's signature flaw: the
  proof that a human craft made this, in a medium where perfection reads as
  machine output.
- **Structure.** A single sort span with class `sort--worn`, coloured
  `--ink-82`. Selection is editorial, fixed in the markup by the content
  author (never random at runtime — a different letter failing on every
  visit reads as a bug, not a worn sort). Rules in §3 govern placement.
- **Motion spec.** The worn sort presses with the same 380ms `press-out` as
  its neighbours but starts 120ms after the word's last regular sort, and
  its saturation settles to 82% instead of 100% (`ink-settle`, 900ms). It
  never "recovers" — no hover, scroll position, or revisit inks it fully.
- **States.** *Rest:* 82%, permanent. *Hover:* §6.10 deepens its *shadow*
  like any letter, but its coverage stays 82% — pressure cannot fix a worn
  sort, and that restraint is the point. *Scrolled-past:* unchanged.
- **Content merge.** It is a letter of the word. A screen reader reads the
  word whole; the flaw is purely in the ink.
- **Failure fallback.** If variable-opacity rendering fails, the letter
  prints at 100% — the page loses a nuance, never a character.
- **Reduced-motion variant.** Identical (it is a static state). It is also
  the one element exempt from the "everything at 100%" reduced-motion
  rule — removing it would remove the theme's signature.
- **Performance budget & mobile variant.** Zero cost: one colour value.
  Mobile: unchanged, but never applied to display type below 34px, where
  82% coverage on a small glyph reads as a rendering glitch.

### 6.3 Raking-light deboss

- **What & why.** One light source rakes across the whole sheet, scrubbed to
  scroll: as the visitor descends, the light's azimuth swings 118° → 62°,
  and the highlight/shadow lips inside every debossed glyph, rule and border
  rotate with it. Depth is felt rather than faked because the depth is
  *consistent* — a single lamp lighting a single sheet — and because it
  moves while nothing else does.
- **Structure.** No canvas, no WebGL. A fixed full-viewport `div.sheet-light`
  carries the paper-tooth grain (an SVG `feTurbulence` tile, 180 × 180px,
  opacity 0.5, `mix-blend-mode: multiply`) and a soft radial warmth centred
  on the light vector. Deboss itself is pure CSS: every `.deboss` element
  stacks two shadows computed from `--lx/--ly` — highlight lip
  `calc(var(--lx) * 1.5px) calc(var(--ly) * 2px) 1px var(--deboss-hi)`,
  shadow lip at the negative offset in `--deboss-lo`.
- **Motion spec.** Continuous. Scroll progress (document) lerps at 0.085
  per frame toward target; azimuth = 118 − 56 × progress degrees. The grain
  brightens 4% as the light vector crosses each section — a breath, not a
  flash. No easing curve; the lerp *is* the easing.
- **States.** *Rest (top of page):* light at 118°, shadows fall
  down-left — morning light from the pressroom window. *Scrolled-past:*
  light at 62°, shadows up-left; the top of the sheet reads as already-read,
  its depth flatter, because the lamp has moved on. *Hover:* unaffected
  globally; cards borrow the vector locally (§6.10).
- **Content merge.** The light falls on the type itself. There is no
  overlay "effect layer" a visitor could point to — remove it and the page
  is the same page, unlit.
- **Failure fallback.** If the rAF loop never starts, `--lx/--ly` keep
  their CSS default (light at 90°, straight from the left) and every deboss
  renders statically. The page loses weather, not content.
- **Reduced-motion variant.** Light locked at 40° (a low, calm angle),
  grain static at resting opacity.
- **Performance budget & mobile variant.** One rAF loop; per frame it
  writes two CSS variables and nothing else — shadow repaint is the
  browser's, and the loop sleeps after 2s without scroll (§5). Budget:
  shadow stacks ≤ 3 layers, no `box-shadow` on elements larger than
  40% of the viewport except the sheet itself. Mobile: azimuth range
  narrows to 100° → 75° and the loop updates at most every other frame —
  full-range light swings on a small screen make body-text shadows swim.

### 6.4 Impression-on-entry sections

- **What & why.** Every section receives its impression as it enters: its
  deboss depth animates 0 → 100% and its ink saturates 88% → 100%, as if
  the sheet were being fed through the press section by section while you
  read. This is the theme's scroll reveal — the replacement for the
  fade-and-rise that this theme forbids.
- **Structure.** Each `<section data-impress>` wraps its content; depth is
  driven by a per-section CSS variable `--depth` (0 → 1) consumed by every
  deboss shadow and ink colour inside it (`color-mix` between `--ink-88`
  and `--ink` states). One IntersectionObserver for the whole page.
- **Motion spec.** Trigger: section top crosses 78% of viewport height.
  Depth: 700ms `press-out`. Saturation: 900ms `ink-settle`, starting 80ms
  after depth so the shape lands before the colour dries. Sections taller
  than 150vh impress in two beats — header block first, body block when its
  own top crosses 78%.
- **States.** *Rest (un-entered):* depth 0, ink 88% — visible, legible,
  merely un-pressed; this matters, because a section glimpsed at the
  viewport edge must never look broken. *Entered:* 100%/100%, permanent.
  *Scrolled-past:* stays pressed. Impressions do not lift.
- **Content merge.** The animation changes the section's own ink and depth.
  There is no wrapper effect; the section *is* the thing being printed.
- **Failure fallback.** Default state in CSS is fully impressed; JS arms
  the un-impressed state only for sections below the fold at load, and the
  1000ms watchdog (§6.11) presses anything still armed. With JS off, the
  page is a finished sheet.
- **Reduced-motion variant.** Sections arrive pre-impressed. No 88% state
  exists anywhere on the page.
- **Performance budget & mobile variant.** Observer callbacks only — no
  scroll math. Colour/depth transitions on ≤ 1 section at a time by
  construction (sections enter sequentially). Mobile: identical, but the
  two-beat rule for tall sections becomes three beats, because a 150vh
  section on a phone is most of the page.

### 6.5 Pinned specimen alphabet

- **What & why.** The full alphabet specimen — `AaBbCc…` set huge in
  Fraunces, with figures and the ſ — pins for one viewport height while
  usage examples scroll past beside it: an invitation, a label, a menu, all
  set in the same face. The pin stages the atelier's core claim: one case
  of type, every job on the premises. It is a reference workbench, not a
  slideshow.
- **Structure.** A two-track section: left track `position: sticky` holds
  the specimen (set at 19vw, three lines, in a type-high border §4); right
  track holds 3–4 example blocks, each a real artefact (invitation suite,
  bottle label, menu card) reproduced as HTML in the face, not images of
  artefacts — so the examples inherit the raking light and impress with
  the section. Pin implemented with sticky positioning, not a JS pinning
  library, so it degrades to a normal stack.
- **Motion spec.** Pin duration: exactly 100vh of scroll. As each example
  block passes the specimen's vertical centre, the specimen letters used
  *in that example's headline* deepen their impression by +15% for as long
  as the example is centred (±10vh window) — the case shows which sorts are
  on the job. Depth change 300ms `ink-settle`. Trigger: scroll, computed in
  the light loop from the section's progress.
- **States.** *Rest (before pin):* specimen at normal depth. *Pinned:*
  letter-highlighting as above. *Scrolled-past (released):* the whole
  specimen impresses once more, briefly, to 105% depth over 400ms — the
  press signing its work — then rests at 100%.
- **Content merge.** The examples are the specimen at work; the highlighted
  letters are the same letters. Nothing here is a diagram *of* the content —
  it is the content, twice.
- **Failure fallback.** Sticky unsupported or JS off: specimen and examples
  form one ordinary stacked section; the letter-highlighting simply never
  happens. Reading order in the DOM is specimen first, then examples, so
  the stack reads correctly.
- **Reduced-motion variant.** No pin. Specimen appears as a static block
  above the examples; no letter highlighting.
- **Performance budget & mobile variant.** Sticky is compositor-cheap; the
  per-frame work is one progress calculation shared with §6.3's loop.
  Mobile: no pin at any width below 860px — the specimen becomes a
  horizontal specimen strip (three glyphs, 34vw) above the examples,
  because a 19vw alphabet beside a phone-width column leaves neither
  readable.

### 6.6 Brass-rule ink progress

- **What & why.** Reading progress is a brass margin rule — a 2px vertical
  rule in the left margin, 40vh tall, centred — that fills with deep teal
  ink from the top as the page is read. Brass because it is furniture (the
  press's own metal), ink because progress here means *how much of the
  sheet has been printed into the reader*. It replaces both the browser
  scrollbar's job and any percentage counter, in the theme's materials.
- **Structure.** A fixed `div.brass-rule` in the left margin (never inside
  the content column), containing a track (brass at 30%) and a fill
  (`--ink`) whose height is set from the light loop's lerped progress. The
  fill's leading edge carries a 6px meniscus: a `border-radius: 50%`
  ellipse of ink at 60%, so the front reads as liquid, not a progress bar.
  Top and bottom of the rule are capped with two 7px brass finials —
  furniture ends.
- **Motion spec.** Scrubbed, no duration: fill height = lerped scroll
  progress (§5), so the ink lags the scroll by ~180ms of lerp tail — the
  slight delay of ink finding its level. At 100% the meniscus settles flat
  over 300ms `ink-settle`.
- **States.** *Rest (top):* empty track, brass only. *Mid-read:* partial
  fill. *End of page:* full, and the bottom finial inks teal — the rule is
  spent. *Hover:* none; furniture does not respond to being looked at.
- **Content merge.** The rule is the page's own margin furniture, measuring
  the page itself in the page's materials. It is hidden below 1100px
  viewport width rather than moved into the content — a margin rule inside
  the text column would be a sidebar widget, which this theme does not have.
- **Failure fallback.** If the loop fails, the rule renders as an empty
  brass track — a decorative margin rule, misleading no one, since it never
  displays a wrong number (it displays no number at all).
- **Reduced-motion variant.** The fill jumps in 10% steps at section
  boundaries instead of scrubbing — progress by leaves turned, not by
  liquid.
- **Performance budget & mobile variant.** One height write per frame,
  shared loop. Mobile (< 1100px): the rule is omitted entirely; progress is
  carried by the folio-style section counter in the footer colophon
  (§6.17) — "Leaf 3 of 7" — which is where a book puts it anyway.

### 6.7 Sheet-lift image reveal

- **What & why.** The hero image is uncovered as a covering sheet lifts off
  it: the clip-path inset rises from the bottom edge, and a soft shadow —
  the lifting sheet's own shadow — rides the reveal edge. In the atelier,
  you lift the protective tissue off a fresh print to see it; the reveal is
  that gesture, and the image is what was under the tissue.
- **Structure.** The image block (in its type-high border, §4) contains the
  duotone plate (§5) and an absolutely-positioned `div.tissue` in
  `--paper` with the grain, clipped by the same inset that reveals the
  image: image `clip-path: inset(0 0 X% 0)` and tissue occupying the
  un-revealed remainder, its bottom edge carrying a 12px soft shadow
  (`rgba(20,66,74,0.18)`, blur 12px). One animated value drives both.
- **Motion spec.** 900ms `sheet`. Hero: starts 250ms after the headline's
  last sort presses (§6.1). Later images: on scroll entry at 70% viewport.
  The shadow's opacity peaks at mid-lift (0.18 at 50%) and is 0 at both
  ends — the sheet casts no shadow lying flat or fully lifted.
- **States.** *Rest:* fully revealed, tissue gone (`visibility: hidden`
  after completion, not merely transparent). *Hover:* none — a revealed
  print is not re-covered. *Scrolled-past:* stays revealed.
- **Content merge.** The tissue is the print's own protective sheet, and
  the photograph is the section's actual subject (the suite, the room, the
  bottle) in duotone plate form. The reveal uncovers content; it does not
  decorate it.
- **Failure fallback.** Images are un-clipped by default in CSS; JS arms
  the clip only when the reveal can run. `alt` text and the caption credit
  render regardless. If the image itself fails to load, the type-high
  border remains with its caption — a framed, captioned empty block, which
  in a specimen layout reads as intentional rather than broken.
- **Reduced-motion variant.** No lift. The plate is simply present,
  impressing with its section (§6.4).
- **Performance budget & mobile variant.** `clip-path` on one element at a
  time; the tissue is removed from the tree after the reveal. Mobile:
  duration shortens to 650ms and the shadow blur halves — small screens
  show less sheet, and the effect must not outstay its size.

### 6.8 Breathing hero word

- **What & why.** One word of the hero headline — chosen editorially,
  usually the craft noun ("pressed", "cotton", "by hand") — breathes: its
  Fraunces `opsz` axis swells ±6% on a slow loop, the press's heartbeat.
  It is the only idle motion in the hero, and it lives inside a letterform,
  so the hero stays a printed page that happens to be alive.
- **Structure.** The word is a `span.breath` with
  `font-variation-settings` animated between `opsz` 135 and 144 (at a
  64px setting). Requires the variable font; if only static Fraunces
  weights load, the element is inert (see fallback).
- **Motion spec.** 5s ease-in-out, `alternate`, infinite — but only while
  the hero is in the viewport (IntersectionObserver pauses it off-screen)
  and only one breathing word per page. The swell is optical size, not
  scale: letterforms genuinely redraw fatter/thinner rather than zooming,
  so line breaks never move (opsz at fixed size does not change advance
  widths enough to reflow — verified per §10).
- **States.** *Rest:* mid-swell. *Hover:* the breath does not respond —
  pressing is §6.10's job; two interactions on one word would quarrel.
  *Scrolled-past:* paused.
- **Content merge.** The pulse is in the word itself. It draws the eye to
  the word the atelier most wants read, the way a printer would point.
- **Failure fallback.** Static-font or no-variable-support: the word sits
  at `opsz` 140. Nothing is missing; the page is a still print.
- **Reduced-motion variant.** Off. The word is set at `opsz` 140, full
  stop — a breathing word is precisely the class of ambient motion
  reduced-motion visitors have asked not to receive.
- **Performance budget & mobile variant.** Font-variation animation
  re-rasterises one word per frame; budget it to hero only, ≤ 12 glyphs.
  Mobile: amplitude halves to ±3% and the period lengthens to 6.5s —
  small glyphs rasterise coarsely, and a subtle breath survives where a
  strong one would shimmer.

### 6.9 Self-drawing brass ornament

- **What & why.** The printer's ornament — a fleuron rule: a centred
  fleuron flanked by two hairlines — draws itself in SVG between sections,
  in brass. It is the section divider of the theme, and it draws because on
  the page it is *printed furniture*: each divider is struck as the reader
  arrives at it, the way the press strikes it onto the sheet.
- **Structure.** Inline SVG, three paths (left rule, fleuron, right rule),
  `stroke: var(--brass)`, stroke-width 1.5, drawn via `stroke-dashoffset`.
  Total ornament width 176px, centred, sitting in the 132px section gap.
  The fleuron path is a fixed asset of the theme — a specific fleuron, not
  a generic swirl — reused identically everywhere, because a printer owns
  one ornament sort and uses it for years.
- **Motion spec.** 700ms total on section-boundary entry: left rule draws
  0 → 100% in 260ms `press-out`, fleuron draws in 300ms, right rule 260ms,
  overlapping by 60ms so the strike feels continuous. Trigger: the boundary
  crosses 85% of viewport height — slightly earlier than the section's own
  impression (§6.4), so the divider is struck just before the section it
  introduces is pressed.
- **States.** *Rest:* fully drawn, brass at 100%. *Hover:* none.
  *Scrolled-past:* stays drawn; ornaments never un-draw.
- **Content merge.** The ornament is the divider between two real sections;
  remove the animation and the divider remains, printed. It marks a
  structural joint in the content, never a decorative pause inside a
  section.
- **Failure fallback.** Paths render fully drawn by default (`dasharray`
  applied by JS only when arming). SVG blocked: a CSS double-rule of the
  same width renders instead — the joint is still marked.
- **Reduced-motion variant.** Ornament appears pre-drawn with its section's
  impression.
- **Performance budget & mobile variant.** Three short path animations,
  ≤ 2 ornaments animating at once (boundaries enter sequentially by
  construction). Mobile: identical; ornament width shrinks to 132px below
  480px so it never crowds the margins it sits in.

### 6.10 Press-harder hover

- **What & why.** Hovering a display letter deepens its impression — shadow
  depth +30% — as if a thumb pressed that sort harder. On cards, the deboss
  light-angle tilts up to 3° toward the pointer, as if the block were
  rocked slightly in the hand. Feedback in this theme is *pressure*,
  because pressure is the theme's verb; a hover that lifts or glows would
  be a different craft's accent.
- **Structure.** Pointer position is fed into the existing light loop
  (throttled to its frames — no separate listener). For letters: a
  per-element `--press` variable (1 → 1.3) multiplying shadow offsets.
  For cards: the card's local light vector rotates toward the pointer by
  ≤ 3°, computed from the pointer's offset from the card's centre.
- **Motion spec.** In: 200ms `press-out`. Release: 260ms `press-out`
  (paper recovers slower than it yields). Letter depth +30% exactly;
  headline letters only — body text never responds to hover, because you do
  not press the text you are reading. Card tilt: rotation of the *light*,
  never of the card — the block does not move, its depth re-lights.
- **States.** *Rest:* `--press` 1. *Hover:* 1.3 / light tilted.
  *Active (pressed):* hands over to the click press (§5, `thud`: scale
  0.99, ink darkens 8%, 120ms). *Scrolled-past:* n/a. Touch devices: the
  first tap applies the hover state, the second activates — matching how a
  visitor picks a block up before committing to it.
- **Content merge.** The response happens in the glyph's own shadow and the
  card's own depth. Nothing appears, floats, or glows; the object itself
  answers the hand.
- **Failure fallback.** No pointer or no JS: elements sit at rest depth.
  Keyboard focus gets the same +30% depth via `:focus-visible` — focus in
  this theme is a brass ring (§6.16) *plus* the press, so keyboard visitors
  feel the same physics.
- **Reduced-motion variant.** Depth change becomes instant (0ms) but still
  applies — state feedback is information, not decoration; only its
  *tween* is removed.
- **Performance budget & mobile variant.** Pointermove writes are folded
  into the single rAF loop; per-frame cost is two variable writes on the
  hovered element only. Mobile: no hover exists — cards instead deepen
  their impression by +15% while touched (`:active`), and letters do
  nothing. Never simulate hover on scroll.

### 6.11 Un-inked skeleton loading (the loader)

- **What & why.** While content loads, the page shows its own un-inked
  state: headline, rules and blocks present at 12% ink — type set in the
  chase but not yet inked. When real content arrives, each block inks in.
  The skeleton is the theme's honest intermediate state (an atelier does
  have an un-inked stage), not grey rectangles borrowed from an app UI.
- **Structure.** The real layout, rendered with a `data-inking` state:
  text elements at `--ink` 12%, image blocks as `--paper-tooth` plates
  inside their real type-high borders, rules at `--hairline`. No separate
  skeleton markup — the page's own elements wear the state, so there is
  zero layout shift when ink arrives (CLS 0 by construction).
- **Motion spec.** Per block: ink 12% → 100% over 500ms `ink-settle`,
  staggered 80ms in reading order, depth following 100ms behind colour —
  ink first, then the press comes down on it. The **global watchdog**:
  anything still below full ink 1000ms after its content resolves is forced
  to final state in one frame. Nothing on this sheet may shimmer, pulse,
  or sweep while loading — a wet sheen is another theme's material.
- **States.** *Loading:* 12%. *Resolving:* staggered ink-in. *Loaded:*
  indistinguishable from a normally impressed page. *Error:* a block that
  fails stays at 12% and gains an oxblood proof mark (§6.16's circled
  mark) with a caption — "This leaf failed to print. Retry." — never a
  spinner.
- **Content merge.** The skeleton occupies the content's exact geometry
  because it *is* the content, un-inked. The visitor reads the page's
  structure — headline size, column measure, block count — from the
  skeleton itself.
- **Failure fallback.** If content resolution hangs, the watchdog still
  inks the skeleton's placeholder text regions to 100% at 1000ms — a
  legible, captioned un-printed block, never an eternal 12% ghost.
- **Reduced-motion variant.** Blocks ink in instantly when ready (no
  stagger); the 12% state remains, because it communicates loading, but it
  never animates.
- **Performance budget & mobile variant.** Zero extra DOM, zero extra
  requests. Mobile: identical; the stagger compresses to 50ms because more
  blocks share the first viewport.

### 6.12 Platen page transition

- **What & why.** On navigation, a fresh sheet slides onto the platen from
  the bottom of the viewport and takes its impression as it settles: slide,
  then depth. Leaving a page in this theme is the press cycle — the old
  sheet is done, a new one is fed. It is the theme's only large translation,
  sanctioned because feeding a sheet *is* translation in the real craft.
- **Structure.** A full-viewport `div.platen-sheet` in `--paper` with the
  grain, initially translated 100% below the viewport, containing nothing
  but the incoming page's masthead line (the destination's kicker) — the
  one part of a sheet you can identify while it is still feeding. The
  router swaps content beneath it at the covered moment.
- **Motion spec.** Total 620ms. Phase 1: sheet slides up to cover,
  260ms `sheet`. Phase 2 (content swapped, sheet still covering): the
  sheet's own grain and masthead take impression (depth 0 → 100%, 200ms
  `press-out`). Phase 3: the sheet does not slide away — it *becomes* the
  page: its background is the page's paper, so at full impression the
  overlay simply hands over (opacity of the overlay's extra grain layer →
  0, 160ms) and is removed. The visitor perceives one sheet arriving and
  being printed, not a wipe.
- **States.** *Rest:* no overlay in the DOM. *During:* input is locked for
  the 620ms (the press is mid-cycle). *Interrupted (back button mid-
  transition):* the sheet completes its impression instantly and hands
  over — never a half-covered page.
- **Content merge.** The transition surface is the destination sheet
  itself, paper and grain identical to the page beneath it; the masthead
  line it carries is the destination's real kicker.
- **Failure fallback.** If the router or JS fails, navigation is a normal
  full-page load — which, in this theme, looks like a fresh sheet anyway.
  The transition is an enhancement layered on plain links, never a
  requirement.
- **Reduced-motion variant.** No slide. A 150ms crossfade between pages,
  arriving pre-impressed.
- **Performance budget & mobile variant.** One overlay element, transform
  and shadow only, removed after handover; budget: zero long tasks, the
  content swap is the app's own routing cost. Mobile: identical, but phase
  1 shortens to 200ms — a phone screen is a small platen and the sheet has
  less far to feed.

---

### Page-family elements

The original entry specified no navigation, hero composition, card, form or
footer pattern. These five complete the family, built from the same chase,
the same inks, and the same press physics.

### 6.13 Chase-locked navigation

- **What & why.** The nav is the chase: a horizontal iron frame across the
  top of the sheet in which the wordmark and links sit locked like sorts in
  a row, separated by brass furniture blocks (thin brass spacers). A
  letterpress nav cannot float, shrink, or hamburger into an app drawer
  without breaking the fiction — so it does none of those things. It is
  short (wordmark + ≤ 5 links + the commission link) because a chase holds
  one line.
- **Structure.** A header bar: wordmark in Fraunces 24px at the left,
  links in Zilla Slab 600 uppercase 12.5px / +0.18em (the kicker setting,
  §3), separated by 1px-wide brass furniture rules 18px tall. Beneath the
  bar, the theme's double rule (3px + 1px, 5.5px gap). The bar is *not*
  sticky in the app sense; it is `position: sticky` with a paper background,
  because a chase stays at the head of the sheet — on scroll it receives
  impression (below) rather than detaching.
- **Motion spec.** On load, the bar's links press in left to right, 200ms
  `press-out`, 35ms stagger — the compositor locking the row. On scroll
  past 40px, the bar takes a permanent impression for the rest of the page:
  its bottom double rule deepens (shadow depth 0 → 60%, 300ms `press-out`)
  and the paper behind it gains the grain at full opacity — the sheet's
  head is now "in the press" while the body scrolls beneath the chase.
  Active page: its link sits at depth 130% (pre-pressed, §6.10's value)
  with a 7px brass furniture block centred beneath it.
- **States.** *Rest (top of page):* flat, depth 0, airy. *Scrolled:*
  impressed state as above. *Hover (link):* press-harder, §6.10 values.
  *Focus:* brass ring + press (§6.10). *Current page:* brass block marker,
  permanent.
- **Content merge.** The links are the site's real sections (Suites,
  Papers, The Atelier, Commissions); the furniture blocks between them are
  the literal spacing material of the row. The nav's restraint — five
  links, one line — is an information-architecture rule of the theme, not
  a styling choice: if the site needs nine top-level links, it needs a
  different theme.
- **Failure fallback.** Plain header with links; sticky and impression are
  enhancements. Without CSS the bar is a list of links above a rule — a
  letterhead, which is what it is.
- **Reduced-motion variant.** Links pre-pressed; scrolled state applies
  instantly at the 40px threshold.
- **Performance budget & mobile variant.** One scroll threshold check
  inside the existing light loop. Mobile: the chase holds two rows — the
  wordmark row and a links row — still fully visible, never a hamburger;
  if links exceed one row at 360px, links drop to 11.5px before any are
  hidden. A letterpress sheet does not hide its contents in a drawer.

### 6.14 The Platen Hero (hero composition)

- **What & why.** The hero is the press bed at the start of a run: masthead
  kicker, the pressed headline (§6.1, §6.2, §6.8), one tissue-covered plate
  (§6.7), and a data line of edition facts counting up (§5). It assembles
  in manufacturing order — type first, then the plate is uncovered, then
  the numbering machine stamps the facts — because the hero is the page
  being made, in front of the visitor, once.
- **Structure.** Centred specimen composition (§4): kicker (oxblood,
  letterspaced), headline (2 hand-set lines maximum), a 44px air gap, the
  plate in its type-high border at ≤ 62ch wide, then the data line — three
  apparatus facts in tabular Zilla Slab separated by brass points (e.g.
  "Edition of 250 · 600gsm cotton · Printed to order"). One CTA, set as a
  brass-bordered block (the "commission plate", §6.16's button language),
  beneath the data line. No second CTA; a press bed holds one job.
- **Motion spec.** The full hero timeline, from `document.fonts.ready`:
  t=0 kicker impresses (300ms). t=120ms headline sorts begin (§6.1,
  ≈ 1.45s total). Worn sort lands last (§6.2). t=+250ms after the final
  sort, the tissue lifts (§6.7, 900ms). As the plate reveals, the data
  line's counters run (§5, 900ms). Breathing word (§6.8) starts only after
  everything else is still — the heartbeat begins when the making ends.
  Total hero choreography: ≈ 2.9s, after which the page is inert except
  for the breath and the light.
- **States.** *Rest:* the finished front sheet. *Scrolled-past:* the hero
  impresses no more; its light stays wherever the global azimuth has
  travelled (§6.3) — returning to the top re-lights it, it does not
  re-print it.
- **Content merge.** Every animated thing in the hero is a hero content
  element: the headline, the plate, the edition facts. There is no
  background animation, no decorative layer; the hero's motion *is* its
  content arriving by manufacture.
- **Failure fallback.** The entire timeline is armed by JS; disarmed, the
  hero is a complete, static front page — kicker, headline, plate, facts,
  CTA — in correct reading order.
- **Reduced-motion variant.** The hero arrives whole: pre-pressed
  headline, plate uncovered, counters at final figures, no breath.
- **Performance budget & mobile variant.** The hero is the page's entire
  animation budget for the first 3s — nothing below the fold animates
  until the hero timeline completes or the visitor scrolls. Mobile:
  headline 44px, plate full-column, data line stacks to two lines, total
  timeline compresses to ≈ 2.2s via §6.1's per-word pressing.

### 6.15 Specimen suite cards

- **What & why.** A card in this theme is a locked type block: one suite or
  product, framed in the type-high border, its plate settling inside the
  frame, its name set as apparatus, its facts (paper, edition, price) set
  as data. Cards are specimens on the sheet — laid out in a grid the way
  blocks are laid in a chase, with visible gutters of bare paper — not
  tiles floating over a background.
- **Structure.** `article.suite` in the double-rule frame (§4). Inside:
  plate (duotone, §5 image treatment) at 4:3, suite name (Zilla Slab 600,
  22px), one line of description (18px body, ≤ 90 characters — cards do
  not carry paragraphs), a data row in tabular figures ("600gsm · Edition
  of 250 · £180"), and a text link "View the suite" with the rubric-style
  underline (§6.10's press on hover, not a colour change).
- **Motion spec.** Entry: the card impresses with its section (§6.4) and
  its plate scales-in-frame 1.06 → 1 over 800ms `press-out`, delayed 120ms
  behind the frame's impression so the block locks before the plate
  settles. Hover: §6.10 — light-angle tilts ≤ 3° toward the pointer, name
  deepens +30%. Click: `thud` (scale 0.99, ink +8%, 120ms) then navigate.
  Cards stagger their entry by 90ms per card within a row — the compositor
  laying blocks one at a time — never a cascade of more than 4.
- **States.** *Rest:* printed, depth 100%. *Hover:* re-lit, name pressed.
  *Sold out:* the plate desaturates to 60% ink and an oxblood "Edition
  closed" stamp line replaces the price in the data row — set, not
  rotated-sticker styled; even the bad news is typeset. *Scrolled-past:*
  static.
- **Content merge.** The card's frame, plate and data are the product's
  catalogue entry; the grid is the atelier's specimen sheet. A card with
  its animation removed loses nothing but the memory of being laid down.
- **Failure fallback.** Static framed entries in a grid; plates un-clipped
  and un-scaled by default in CSS.
- **Reduced-motion variant.** Cards arrive impressed with their section;
  hover tilt is removed but the name's press becomes instant (§6.10).
- **Performance budget & mobile variant.** ≤ 12 cards animate per page;
  plates are `content-visibility: auto` below the fold. Mobile: one
  column, plates at 3:2 (a phone shows less of the suite, so the crop
  tightens on the pressed detail), stagger removed — cards impress with
  their section only, because a 6-card stagger on a small screen is a
  queue the visitor did not ask to wait in.

### 6.16 The commission slip (forms)

- **What & why.** The theme's only form pattern: a printed order slip, the
  kind pinned above the press with a spike. Fields are not boxes — they
  are leader lines on a printed form, with the label set as apparatus
  above the line and the visitor's entry appearing *on* the line in Zilla
  Slab, like handwriting's tidier cousin. Submitting the slip is the
  site's checkout-equivalent: a commission request (suite, paper, quantity,
  date, address), never a multi-step wizard (§1).
- **Structure.** A single column at 58ch inside a type-high border — the
  slip is a block on the sheet. Each field: label (kicker setting, teal),
  input with transparent background, no border except a 1px `--hairline`
  bottom rule, 18px text, 11px padding below the baseline. Required fields
  carry a brass point after the label, not an asterisk in a UI grey. The
  submit control is the **commission plate**: a brass-bordered block,
  full-width of the slip, label in kicker setting — "Press the commission"
  is too cute; the label is the plain verb of the site ("Request this
  suite").
- **Motion spec.** Focus: the field's leader line inks from `--hairline`
  to full `--ink` (200ms `ink-settle`) and the field's label takes a
  shallow impression (depth 40%, 200ms `press-out`) — the slip acknowledges
  where the pencil is. Error: the offending field's line turns oxblood and
  a proof mark appears in the slip's right margin — a hand-drawn-style SVG
  circle around the field's number with a 3-word note in oxblood Zilla
  Slab ("Date precedes today") — drawn in 300ms, because a proof mark is
  struck, not faded. Submit: the plate presses (`thud`, 120ms), then the
  whole slip takes a full impression (depth → 100%, 500ms `press-out`) and
  holds it while the request sends — the form is quite literally being
  pressed. Success replaces the slip's contents with the colophon-style
  confirmation (§6.17's voice): edition line, reference number in tabular
  figures, what happens next, in apparatus type.
- **States.** *Rest:* hairlines faint, labels flat. *Focus:* as above.
  *Filled:* the field's line stays at 60% ink — a completed line on a form
  is darker than an untouched one. *Error:* oxblood proof state, persistent
  until corrected (errors never time out on a printed form). *Submitting:*
  slip impressed, inputs disabled, plate at depth 130%. *Success:*
  confirmation block, impressed once, permanently.
- **Content merge.** The form is a document of the business — the same slip
  the atelier would pin to the board. Its fields, its proof marks and its
  confirmation are the transaction's paper trail, styled as the paper
  itself rather than as software wearing a paper costume.
- **Failure fallback.** A plain HTML form: labels, inputs, a submit
  button, server-side validation re-rendering the same proof notes as
  text. Every enhancement (leader-line inking, impression) is CSS/JS over
  that form. No-JS visitors lose the theatre and keep the transaction.
- **Reduced-motion variant.** Focus and error states apply instantly;
  submit skips the impression hold and shows a static "Pressing…" line in
  apparatus type.
- **Performance budget & mobile variant.** No animation loops; transitions
  on focus/error only. Mobile: the slip goes full-bleed (its border
  becomes top and bottom double rules only — a slip torn to width), inputs
  at 18px (also preventing iOS zoom), and the proof note moves *beneath*
  its field because a phone slip has no right margin.

### 6.17 Colophon footer

- **What & why.** The footer is a real colophon — the back-page apparatus
  of the book: what the site was set in, what it was printed on, which
  edition this visit is, and who holds the copyright. Plus the sorts tray
  drift (§5) and the leaf counter that replaces the brass rule on narrow
  screens (§6.6). It is the last impression on the sheet, and it is where
  the theme tells the truth about itself.
- **Structure.** Centred apparatus column (13.5px, §3): line 1, the
  ornament (§6.9, pre-drawn). Line 2: "Set in Fraunces & Zilla Slab ·
  Printed on 600gsm cotton (this page weighs nothing and remembers
  everything)". Line 3: the edition line — "Edition of one · Yours" plus
  the leaf counter "Leaf N of M" (visible < 1100px only, §6.6). Line 4:
  the atelier's legal line and two or three text links (Imprint, Terms,
  Contact) with rubric-style underlines. Above the colophon, the sorts
  tray strip: a 15vh band of oversized Fraunces glyphs at 12% ink drifting
  at 9px/s (§5) — the case being put away at the end of the day.
- **Motion spec.** The colophon impresses with its section (§6.4) — the
  final press of the page. The sorts drift runs only while the footer band
  is in view. The leaf counter updates at section boundaries (200ms
  crossfade of the numeral, tabular). Nothing else moves; the end of the
  sheet is the quietest part of it.
- **States.** *Rest:* printed colophon. *Hover (links):* underline draws,
  §6.10 press. *Scrolled-past:* n/a — it is the end.
- **Content merge.** The colophon is content: type credits, paper credit,
  edition statement, legal line. The drifting sorts are the same glyphs
  the specimen (§6.5) catalogued, put away in their tray — the day's work
  ending inside the site's own fiction.
- **Failure fallback.** Static centred text block; the sorts strip renders
  as a static specimen line. Every link is a plain link.
- **Reduced-motion variant.** Sorts strip static; leaf counter updates
  instantly; colophon pre-impressed.
- **Performance budget & mobile variant.** The drift is one transform on
  one element, paused off-screen. Mobile: the colophon is unchanged (it
  was always a narrow column); the sorts strip shortens to 10vh and the
  leaf counter appears, as specified.

---

## 7. Page application map

**Home.** The full press run: chase nav (§6.13), Platen Hero (§6.14), a
ledger section of current editions with counters (§5), the pinned specimen
(§6.5), a suite grid (§6.15), an ornament, a short reading column on the
atelier's papers, colophon (§6.17). The home page is the only page allowed
the pinned specimen — pinning is a once-per-visit ceremony.

**Listing (the suites index).** No hero plate; the page opens with an H1
that impresses as a block (§6.4) and a one-line apparatus summary ("14
suites · 3 papers · editions of 100–500"). The grid is §6.15 cards in chase
rows of three. Filtering, if any, is a printed index line — text links that
re-lay the grid with a single re-impression (depth dip to 40% and back,
350ms) rather than animated shuffling; blocks do not fly around a chase.
Sort order is editorial (the atelier's order), never algorithmic.

**Detail (one suite).** The sheet-lift plate (§6.7) returns as the page's
opening gesture — on a detail page the visitor has come to see one thing,
and uncovering it is the right ceremony. Reading column: the suite's story;
ledger column beside it: paper, gsm, edition size, price, per-unit facts in
tabular data, counters running once on entry. The commission slip (§6.16)
closes the page — on detail pages the form *is* the conversion, pre-filled
with the suite's name on its first line, the way a slip pulled for a known
job already has the job written on it.

**About (the atelier).** The quietest page: no pin, no counters except the
founding year and the press's year counted once, in apparatus. Long reading
column, illuminations as duotone plates of the press and the bindery with
sheet-lift reveals, the raking light doing all the work. The page ends with
the staff set as a printer's imprint list — names and roles in apparatus
type, no avatar circles; a letterpress atelier credits people the way a
book does.

**Contact / commission.** The slip (§6.16) is the whole page, preceded by
one reading paragraph (response time, in prose: "The press answers within
two working days") and followed by the colophon. No map embed — a map is a
screen object; the address is set as apparatus text, with a plain link out
to the visitor's map service.

**Checkout equivalents.** There is none beyond the slip, by design (§1).
If the business later needs payment, payment happens on the processor's
own sheet, linked from the confirmation — the theme does not imitate a
till.

**404 / error leaves.** A single centred leaf: the fleuron, "This leaf was
not bound in" in Fraunces, one apparatus line, and a link home set as a
rubric underline. Even the error is a page of the book, and it impresses on
entry like any section.

---

## 8. Worked example — the home hero, built end to end

The hero of a wedding stationer's home page, exactly as it ships.

**Markup order.** `<header class="chase">` (§6.13) → `<section
class="hero">` containing, in DOM order: the kicker `<p class="kicker">`
("Letterpress stationery · Est. 2011"), the headline as two hand-set lines
of sort spans — line 1 "Pressed by hand,", line 2 "kept for good." — the
plate `<figure class="plate">` (the suite photograph as teal duotone inside
its type-high border, caption "The Hartley Suite · 600gsm cotton, deckle
edge"), the data line ("Edition of 250 · 600gsm cotton · Printed to
order"), and the commission plate linking to the suite's detail page.

**The worn sort.** In "Pressed", the second `s` is the worn sort (82%,
arrives last in its word). In "kept", the `k` is worn. Two words, two
different letters, neither in the first word's first position — and the
first line's first word "Pressed" carries its flaw on a doubled letter,
where a real worn sort hides best.

**Timeline on load.** Fonts confirm (`document.fonts.ready`). The chase
links lock in (200ms, 35ms stagger). The kicker impresses at t=0. Sorts
begin at t=120ms: 21 sorts across two lines at 45ms stagger, 380ms each —
line 1 done ≈ t=1.28s, line 2 ≈ t=1.57s, the worn `k` landing at ≈ t=1.69s.
At t≈1.94s the tissue lifts off the plate (900ms) while the data line's
three facts count up beneath it. At ≈ t=2.84s the word "hand" — set as the
breathing word, `opsz` 135→144 — takes its first breath. The hero is then
still. A visitor who does nothing has watched a page be manufactured in
under three seconds and is now simply reading it.

**Scroll behaviour.** Scrolling lerp-engages the light: by the time the
hero leaves, the azimuth has swung ~14° and the headline's depth has
visibly re-lit — the visitor feels the lamp move before they could name
it. The brass rule in the left margin begins to fill. The first section
below (current editions) impresses at the 78% line, its counters rolling
as the hero's breath pauses off-screen.

**What the same hero is with JS disabled.** A letterhead, a headline, a
framed photograph with its credit, three facts, a link — complete,
centred, and calm. The build's test is that a screenshot of the no-JS hero
and a screenshot of the settled hero differ only in shadow angle.

---

## 9. Anti-slop — how this theme goes cheap, and the cure

- **Drop shadows instead of deboss.** A soft grey `box-shadow` under cards
  makes the sheet look like a SaaS dashboard in a beige skin. *Cure:* depth
  lives only inside elements (the two-lip shadow stack, §6.3), computed
  from the light vector; nothing on the sheet casts a shadow *onto* the
  sheet except the lifting tissue (§6.7) and the platen sheet (§6.12) —
  the two things that are physically above the paper.
- **Fade-and-rise reveals.** The generic 20px rise is this theme's exact
  negation. *Cure:* impression-on-entry (§6.4) is the only entrance;
  translation budget for a whole page is the sheet-lift, the platen, and
  3px of parallax shear. Any other `translateY` in the stylesheet is a
  defect.
- **Gold-gradient text and foil effects.** Brass is furniture, not a text
  treatment; gradient-clipped headline text is a wedding-invitation cliché
  from a stock site. *Cure:* brass appears only as rule, ornament, finial,
  focus ring, and marker (§2) — always flat, always matte.
- **The worn letter everywhere.** Under-inked letters sprinkled across
  body copy or every headline turn the signature flaw into visual noise
  and hurt legibility. *Cure:* the §3 ration — display words only, one per
  word, never the same letter twice per page.
- **Vintage filters and texture overload.** Sepia photographs, coffee-stain
  PNGs, torn-edge dividers: costume, not craft. *Cure:* photographs are
  honest duotone plates (§5); the only texture is the paper's own tooth at
  0.5 opacity; there are no stains on a sheet the atelier is proud of.
- **Light that disagrees with itself.** Two elements whose shadows fall in
  different directions destroy the single-lamp illusion instantly.
  *Cure:* one loop, one vector (§6.3); no element may hard-code a shadow
  direction.
- **Motion inflation.** Adding a marquee to the hero, counters to every
  number, or a pin to every page because the vocabulary exists. *Cure:*
  the §2 ink-coverage discipline and the §4 density caps are gates, not
  guidelines — §10 checks them.
- **App chrome creep.** Sticky toolbars, toast notifications, floating
  action buttons, chat bubbles. *Cure:* the theme's complete chrome is the
  chase (§6.13), the brass rule (§6.6), and the colophon (§6.17). A
  requirement that needs a toast is a requirement for a different theme.

---

## 10. Quality gate — minimum bar before this theme may be used

Every box must pass; a single failure returns the build.

- [ ] **No-JS screenshot test:** with JavaScript disabled, every page is
      complete and legible; the settled-state and no-JS screenshots differ
      only in light angle and the tissue/plate states.
- [ ] **Watchdog test:** with the animation loop artificially stalled, all
      content reaches its final state within 1000ms (§6.11).
- [ ] **Single-light audit:** at three scroll positions, every deboss on
      screen agrees on one light direction (checked by eye against the
      `--lx/--ly` values); no hard-coded shadow directions in the CSS.
- [ ] **Translation audit:** grep the stylesheet — outside `.tissue`,
      `.platen-sheet`, and the 3px strata shear, no `translate` exceeds
      4px.
- [ ] **Worn-sort ration:** exactly one under-inked letter per display
      word, none in body text, prices, or form labels; no letter repeated
      on a page (§3, §6.2).
- [ ] **Ink discipline:** per viewport — ≤ 1 oxblood element in motion,
      ≤ 1 brass element in motion, ≤ 1 breathing word (§2).
- [ ] **Contrast:** body text `--ink` on `--paper` ≥ 9:1 as built
      (including the dusk variant); brass never carries text (§2).
- [ ] **Reduced motion:** with `prefers-reduced-motion`, the light is
      locked at 40°, no pin, no breath, no lift, no drift — and the page
      still contains 100% of its content and its worn sorts.
- [ ] **Performance:** one rAF loop total; first impression frame ≤ 50ms
      on a mid-range Android; CLS = 0 across load (the skeleton is the
      layout, §6.11); hero timeline complete ≤ 3s on desktop, ≤ 2.4s on
      mobile.
- [ ] **Breath reflow check:** the breathing word's line never reflows at
      any viewport width during the swell (§6.8).
- [ ] **Form honesty:** the commission slip works end-to-end with JS and
      CSS both disabled, errors included (§6.16).
- [ ] **The stranger test:** show the settled page to someone who has
      never seen it. If they say "vintage template" instead of "printed
      page", the build has failed §9 — return to the anti-slop list.

---

*End of Theme 004 — Letterpress Atelier (Expanded). Standing rules reminder:
normal system cursor only; no reveal may ever hide content permanently;
`prefers-reduced-motion` honoured per element above; every element merges
with the content it carries.*

---

## Part II — Deepening (50x standard)

Part I specified what each element is and how it moves. Part II specifies it
to the millisecond, in every state, at every width, when things go wrong,
for every visitor — and names the exact tokens it consumes, so two builders
working separately produce the same sheet. Nothing in Part I is redesigned;
every number below either comes from Part I or is derived from its press
physics.

**Conventions used throughout Part II**

- **Timelines.** `t=0` is the element's own trigger moment, defined in its
  first line. All times are milliseconds from that trigger. "Settled" means
  the element is indistinguishable from its no-JS printed state.
- **State matrices.** Columns are Desktop (pointer + keyboard) and Touch.
  Where an element is not focusable or not a control, the matrix says so
  and names what carries that state instead — an undesigned state is a
  defect; an explicitly refused state is a decision.
- **Tokens are normative.** The CSS variable names in each element's token
  list are the contract. Shared tokens, defined once here:
  - Easings: `--ease-press: cubic-bezier(0.22, 1, 0.36, 1)` (Part I
    `press-out`); `--ease-ink: cubic-bezier(0.4, 0, 0.2, 1)` (`ink-settle`);
    `--ease-sheet: cubic-bezier(0.65, 0, 0.25, 1)` (`sheet`);
    `--ease-thud: cubic-bezier(0.3, 1.4, 0.5, 1)` (`thud`, hard cap 120ms).
  - Light: `--lx`, `--ly` (light vector, §6.3), `--az` (azimuth in deg,
    118 → 62 across the page, locked 40 under reduced motion, locked 28 in
    the dusk variant).
  - Depth & pressure: `--depth` (0–1, per impressed section, §6.4);
    `--press` (1 at rest, 1.3 under press-harder, §6.10).
  - Paper & ink: `--paper`, `--paper-tooth`, `--ink`, `--ink-88`,
    `--ink-82`, `--oxblood`, `--brass`, `--deboss-hi`, `--deboss-lo`,
    `--hairline` (§2 — unchanged, not redefined here).

---

### D6.1 Sequential letter pressing — deepening

**Choreography timeline** (t=0 = first sort starts; in the hero this is
hero-timeline t=120, §6.14/D6.14). Per sort *n* (1-indexed), start =
45 × (n−1):

| Beat | What happens |
|---|---|
| start + 0–140ms | Depth 0 → 52% along `--ease-press` (the curve is front-loaded: the platen commits first); blur 0.7px → 0.4px; scale 1.04 → 1.02 |
| start + 140–280ms | Depth 52% → 90%; blur 0.4px → 0.15px; the sort's shadow lips separate to their full `--lx/--ly` offsets |
| start + 280–380ms | Depth 90% → 100%; blur → 0; scale → 1. The impression has landed |
| start + 80–980ms | Saturation track, independent: ink 88% → 100% over 900ms `--ease-ink`. The shape dries slower than it lands |
| last sort + 0 | Worn sort (§6.2) begins, 120ms after its word's last regular sort, on the same 380ms press, its saturation track ending at 82% |
| 380 + 45 × (N−1) | Sequence settled. For the §8 hero (21 sorts): ≈ t=1,280 for line 1's last sort, full headline settled ≈ t=1,690 including the worn `k` |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Fully pressed, depth 100%, ink 100% (worn sort 82% coverage, §6.2) | Identical |
| Hover | Hovered sort only: `--press` 1 → 1.3 over 200ms `--ease-press`, release 260ms (§6.10). Neighbours unaffected | No hover. A tap on the headline does nothing — it is not a control, and the first tap must never be swallowed |
| Focus | Not focusable. The headline is text; keyboard focus in the hero lives on the commission plate (§6.16). If a build wraps headline text in a link, that build is wrong (§6.14: one CTA, separate) | Same |
| Active | n/a — no activation exists | n/a |
| Scrolled-past | Static forever. Never re-presses, including on scroll back to top; only the light (§6.3) keeps moving over it | Identical |
| Disabled | n/a as a control. Its un-printed analogue is the skeleton state (§6.11): sorts at 12% ink until content resolves | Identical |

**Breakpoint behaviour**

- **≥1200px:** display 64px/1.04; per-letter pressing; stagger 45ms; cap
  40 animated sorts per page (hero only).
- **768–1199px:** display 52px/1.1; stagger tightens to 38ms (the line is
  shorter, the ripple must not dawdle); per-letter up to 36 sorts, any
  remainder presses per word.
- **<768px:** display 44px/1.08; pressing is per *word* (≤ 8 units),
  stagger 90ms per word, blur cap 0.5px — 24 sequential shadow animations
  on a low-end GPU smear the ripple into mush (§6.1).

**Edge cases & failure modes**

- `document.fonts.ready` never resolves (font CDN hang): the §6.11
  watchdog fires at 1000ms from `DOMContentLoaded` and forces every sort
  to final state in one frame. A headline pressed in a fallback face and
  then swapped is a misprint; a headline that never presses is a printed
  headline. The watchdog chooses the print.
- Headline longer than the sort cap (long German compound, an editor who
  ignored §3): degrade to per-word pressing at any width rather than
  truncating or animating 60 sorts.
- Visitor scrolls away mid-sequence: the sequence completes off-screen
  (≤ 1.7s); nothing queues behind it. The breathing word (§6.8) still
  waits for the hero to be in view before its first breath.
- Back/forward cache restore: sorts render settled; the sequence is a
  first-manufacture event and never replays within a session.
- JS split failure (malformed hand-set line spans): base CSS is the final
  state (§6 preamble), so the failure mode is a static headline — the
  correct failure.

**Accessibility spec**

- The `<h1>` carries `aria-label` with the complete headline text; the
  sort spans are `aria-hidden="true"`. Without this, several screen
  readers spell the headline letter by letter — the one reading of this
  headline that is never acceptable.
- DOM order is reading order; hand-set `<span class="line">` breaks never
  reorder content for assistive tech.
- Contrast: `--ink` on `--paper` ≈ 9.4:1 at every state (the 88% start
  state is transient and never a resting state). The worn sort's effective
  contrast is ≈ 5.8:1, permitted only because it is display type ≥ 34px
  (WCAG large-text floor is 3:1) and never carries unique information.
- Motion safety: the press changes depth, blur and scale only — no
  luminance flashing; per-sort change rate is far below 3 flashes/second.
  Under `prefers-reduced-motion` the sequence does not run at all (§6.1).

**Tokens consumed:** `--ink`, `--ink-88`, `--ink-82` (worn sort only),
`--deboss-hi`, `--deboss-lo`, `--lx`, `--ly`, `--press`, `--ease-press`,
`--ease-ink`, `--dur-sort: 380ms`, `--stagger-sort: 45ms` (38ms at
768–1199, 90ms per word <768), `--wet-blur: 0.7px` (0.5px <768).

---

### D6.2 The under-inked letter — deepening

**Choreography timeline** (t=0 = the worn sort's own press start, which is
its word's last regular sort start + 120ms): 0–380ms, the standard press
(depth 0 → 100%, blur 0.7px → 0, `--ease-press`) — mechanically identical
to its neighbours, because the sort is worn, not broken. Its saturation
track runs 80–980ms on `--ease-ink` and terminates at 82%: at t≈500 the
letter is visibly drier than its neighbours, at t=980 it has settled into
its permanent imperfection. There is no later beat. Ever.

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | 82% coverage, permanent | Identical |
| Hover | Shadow deepens via `--press` exactly like a sound sort (§6.10); coverage stays 82% — pressure cannot fix a worn sort | No hover; `:active` deepens shadow only |
| Focus | Not focusable (a glyph, not a control) | Same |
| Active | n/a | n/a |
| Scrolled-past | 82%. Revisits, reloads within the session, and scroll position never re-ink it — the choice is fixed in markup, never randomised at runtime (§6.2) | Identical |
| Disabled | n/a. In the skeleton state (§6.11) the worn sort is 82% of 12% — it is the faintest thing on the un-inked sheet, which is correct: the flaw inks last because it inks least | Identical |

**Breakpoint behaviour**

- **≥1200px:** full effect at display 64px.
- **768–1199px:** full effect at 52px.
- **<768px:** effect only on display type ≥ 34px; below that the sort
  prints at 100% — at small sizes 82% coverage reads as a rendering
  glitch, not a worn sort (§6.2 mobile rule).

**Edge cases & failure modes**

- `color-mix`/opacity unsupported: the letter prints at 100%. The page
  loses a nuance, never a character (§6.2).
- Forced-colors mode (Windows High Contrast): the effect is removed
  entirely; the sort renders in full `CanvasText`. A decorative ink flaw
  must never survive into a mode whose entire purpose is legibility.
- Editor marks two worn sorts in one word, or one in a price: build-time
  lint against the §3 ration fails the build — this is an editorial error,
  not a runtime state.
- Print stylesheet: the worn sort prints at 82% grey — correct. A printed
  page about printing keeps its flaw on paper.

**Accessibility spec**

- The word is read whole by screen readers (the sort spans are
  `aria-hidden` under the h1's `aria-label`, D6.1); the flaw is purely
  optical and carries zero information.
- Effective contrast ≈ 5.8:1 against `--paper` — above the 4.5:1 body-text
  floor even though the ≥34px display-only rule already places it under
  the 3:1 large-text rule. It is the only element in the theme permitted
  below 9:1, and only because it never appears below 34px.
- Reduced motion: identical in all respects — it is a state, not a motion,
  and is the one element exempt from the "everything at 100%" rule (§6.2).

**Tokens consumed:** `--ink-82`, `--deboss-hi`, `--deboss-lo`, `--lx`,
`--ly`, `--press`, `--ease-press`, `--ease-ink`, `--dur-sort: 380ms`.

---

### D6.3 Raking-light deboss — deepening

**Choreography timeline** (continuous; t=0 = page load, light at rest):

| Beat | What happens |
|---|---|
| t=0 | `--az` = 118°, `--lx/--ly` at their morning values; grain at resting opacity 0.5 |
| First scroll input | The loop wakes (it sleeps after 2s without scroll, §5); target progress = document scroll fraction |
| Each frame while scrolling | Progress lerps toward target at 0.085/frame; `--az` = 118 − 56 × progress; two CSS variable writes per frame, nothing else |
| Progress crosses a section boundary | The grain brightens +4% over ≈ 600ms of scroll travel — the lamp passing a new leaf — then returns to rest opacity |
| Scroll stops | Lerp tail ≈ 180ms brings the light to its final angle; after 2s still, the loop sleeps |
| Progress = 1 | `--az` = 62°. The sheet is fully read and lit from low left |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Light 118°, shadows fall down-left — morning at the pressroom window | Identical |
| Hover | No global response. Cards borrow the vector locally (§6.10, ≤ 3° tilt); the lamp itself never follows the pointer | No hover; touch-drag scroll scrubs the light like any scroll |
| Focus | Unaffected — focus is carried by the brass ring + press on the focused element (§6.10), never by moving the light | Same |
| Active | Unaffected | Unaffected |
| Scrolled-past | Light at 62°; already-read sections read flatter — the lamp has moved on. Scrolling back up reverses the azimuth exactly; the light has no memory and no hysteresis beyond the lerp | Identical |
| Disabled | The loop disabled (JS off, or the §5 degradation trigger) = light frozen at the CSS default 90°, straight from the left. Every deboss still renders; the page loses weather, not depth | Identical |

**Breakpoint behaviour**

- **≥1200px:** full azimuth range 118° → 62°; per-frame updates.
- **768–1199px:** range narrows to 108° → 68° — a tablet's sheet is
  smaller; a full swing makes mid-page shadows visibly swim.
- **<768px:** range 100° → 75° (§6.3 mobile rule); loop updates at most
  every other frame; grain tile drops to 140 × 140px.

**Edge cases & failure modes**

- rAF throttled by a backgrounded tab: the loop sleeps with the tab
  (§5); on return, progress snaps to the current scroll fraction in one
  frame — no fast-forward sweep of the lamp across the sheet.
- Very long page (progress denominator huge): azimuth is a function of
  fraction, not pixels, so a 30-leaf page and a 3-leaf page get the same
  lighting arc; per-section grain brightening is keyed to boundaries, not
  fractions, so it still fires per leaf.
- SVG `feTurbulence` grain unsupported (very old engines): the
  `.sheet-light` layer renders empty; deboss shadows — pure CSS — are
  unaffected. The sheet loses tooth, keeps depth.
- `hardwareConcurrency ≤ 2` or first impression frame > 50ms: §5
  degradation locks the light at 90° and stops the loop entirely (the
  static variant), rather than running a juddering lamp.
- User scrolls back up quickly: the lerp follows; because the factor is
  symmetric, the light retraces its arc with the same ~180ms lag — it
  never leads the scroll.

**Accessibility spec**

- The light is decorative physics on content that is fully legible at
  every azimuth: `--ink` on `--paper` stays ≈ 9.4:1 regardless of shadow
  angle, because contrast lives in the ink colour, not the shadow.
- Shadow lips are never the sole carrier of meaning: `--deboss-hi` /
  `--deboss-lo` decorate glyph edges; remove both and every word is
  unchanged.
- Reduced motion: light locked at 40°, grain static (§6.3) — a low, calm,
  single angle. Dusk variant: locked at 28°.
- Vestibular safety: nothing on the page translates under this system;
  only shadow angles move, at scroll speed, user-driven.

**Tokens consumed:** `--lx`, `--ly`, `--az`, `--deboss-hi`, `--deboss-lo`,
`--paper-tooth` (grain tint), `--lerp-light: 0.085`, `--az-top: 118deg`,
`--az-bottom: 62deg` (108/68 at 768–1199; 100/75 <768; 40deg locked under
reduced motion; 28deg in the dusk variant).

---

### D6.4 Impression-on-entry sections — deepening

**Choreography timeline** (t=0 = section top crosses 78% of viewport
height):

| Beat | What happens |
|---|---|
| t=0 | Observer fires; `--depth` animation armed for this section only |
| t=0–700ms | Depth 0 → 100% on `--ease-press`. Every deboss inside the section deepens together — one platen, one stroke |
| t=80–980ms | Saturation 88% → 100% on `--ease-ink`, starting 80ms behind depth: the shape lands before the colour dries |
| t≈980ms | Section settled; observer unobserves it. Impressions do not lift |
| Tall section (> 150vh) | Two beats: header block on its own 78% crossing, body block on its own. <768px: three beats (§6.4 mobile rule) |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (un-entered) | Depth 0, ink 88% — visible, legible, merely un-pressed. A section glimpsed at the viewport edge must never look broken | Identical |
| Hover | Section-level hover does not exist; interactive children carry their own (§6.10, §6.15, §6.16) | Same |
| Focus | A section is not focusable; focus entering a section (skip-link jump, anchor link) counts as entry — see edge cases | Same |
| Active | n/a | n/a |
| Scrolled-past | Pressed, permanently. Scrolling back up never un-impresses | Identical |
| Disabled | JS off or observer unsupported: every section renders at depth 100%, ink 100% — the CSS default is the finished sheet (§6 preamble) | Identical |

**Breakpoint behaviour**

- **≥1200px:** as specified; two-beat rule above 150vh.
- **768–1199px:** identical timings; the 78% trigger line is unchanged
  (it is a proportion, not a pixel count, so it scales with the sheet).
- **<768px:** three beats for tall sections; depth duration shortens to
  600ms — a phone viewport holds less sheet, and a 700ms press on a
  half-screen section outstays its welcome.

**Edge cases & failure modes**

- Keyboard/skip-link jump to a mid-page anchor: sections between the top
  and the target never crossed 78% in view. Rule: any section whose top
  is above the current scroll position is impressed instantly (it is
  "already read" by position). No visitor may land on an un-pressed
  section by jumping.
- Find-in-page jump: same rule — position, not observation, is the
  authority after any discontinuous scroll.
- Content injected after load (a late suite grid): new sections are
  observed on insertion and impress on entry; if inserted already inside
  the viewport, they impress after one frame at the standard timeline.
- Section taller than 300vh (an editor ignored §4 density): beats
  subdivide per 100vh of section height rather than leaving the lower
  two-thirds un-pressed until reached.
- Observer fires during the platen transition (§6.12): impressions queue
  behind the transition's handover and run on the new page's own scroll
  position — the press never strikes two sheets at once.

**Accessibility spec**

- The un-entered state (88% ink) still contrasts ≈ 8.2:1 against
  `--paper` — legible to low-vision readers even mid-approach; no content
  is ever presented below AA at any point of the animation.
- Screen readers: impression is purely visual; the section's text is in
  the accessibility tree at full value from first paint, unpressed or
  not. Nothing is `aria-hidden` at any depth.
- Reduced motion: sections arrive pre-impressed; the 88% state does not
  exist anywhere on the page (§6.4).

**Tokens consumed:** `--depth`, `--ink`, `--ink-88`, `--deboss-hi`,
`--deboss-lo`, `--lx`, `--ly`, `--ease-press`, `--ease-ink`,
`--dur-impress: 700ms` (600ms <768), `--dur-dry: 900ms`,
`--impress-trigger: 78%`.

---

### D6.5 Pinned specimen alphabet — deepening

**Choreography timeline** (t=0 = specimen's top reaches the viewport top;
the pin lasts exactly 100vh of scroll):

| Beat | What happens |
|---|---|
| Pre-pin (approach) | Specimen impresses with its section (§6.4 timeline) before the pin engages — it is printed first, then held |
| t=0 (pin engages) | Left track sticks (`position: sticky`); right-track examples begin their traverse at 1× |
| Example *k* centred (±10vh window) | The specimen sorts used in example *k*'s headline deepen +15% over 300ms `--ease-ink`; sorts not on the job stay at 100% |
| Example *k* leaves centre | Its sorts return to 100% over 300ms; the next example's sorts take the emphasis. Crossfade, never a snap |
| t=100vh (pin releases) | The whole specimen impresses once more to 105% depth over 400ms `--ease-press` — the press signing its work — then rests at 100% as normal flow resumes |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (before pin) | Specimen at normal depth above/beside its examples | ≥860px: identical. <860px: no pin exists — specimen strip state (below) |
| Hover | Example blocks: §6.10 press-harder on the block. Specimen glyphs themselves do not hover — they are a reference, not controls | No hover; examples respond to touch via `:active` deepening (+15%, §6.10 mobile rule) |
| Focus | Specimen not focusable. Examples that are links/cards take focus in DOM order — specimen first in DOM, so the strip reads before the examples (§6.5 fallback order is the focus order too) | Same |
| Active | n/a on the specimen; example links use the `thud` click press (§5) | Same |
| Scrolled-past (released) | Static specimen in flow at 100%, post-signature. Scrolling back up re-pins (sticky is positional) but the +15% highlighting and the 105% signature do not re-run within the session | Strip state: static |
| Disabled | Sticky unsupported or JS off: one ordinary stacked section, specimen first, then examples (§6.5) | Identical |

**Breakpoint behaviour**

- **≥1200px:** two-track pin as specified; specimen at 19vw, three lines,
  in its type-high border.
- **768–1199px:** pin retained (≥860px) but the specimen drops to two
  lines at 16vw and examples narrow to the reading column; at 768–859px
  the strip variant applies (below).
- **<768px (and 768–859px):** no pin at any width below 860px (§6.5). The
  specimen becomes a horizontal strip — three glyphs at 34vw — above the
  examples; letter highlighting is cut entirely (a strip cannot show
  which sorts are on the job without lying about scale).

**Edge cases & failure modes**

- Example headlines use a sort the specimen doesn't show (a `Q` in a
  specimen cropped to three lines at tablet width): only shown sorts
  highlight; the rule is "the case shows the sorts it holds", and an
  unshown sort simply gets no emphasis — never an error state.
- Examples shorter than the pin (editor supplied 2 short blocks): the pin
  still lasts 100vh; the empty traverse is filled by the section's own
  bottom air (§4) — the build must not shorten the pin to match content,
  because pin length is the ceremony's measure.
- Examples taller than planned (5 blocks): pin stays 100vh; later
  examples traverse unpinned flow after release. The specimen never pins
  twice on one page (§7: home page only, once per visit).
- Sticky inside a transformed ancestor (a careless wrapper breaks
  `position: sticky`): degrades to the stacked fallback silently and
  correctly — which is why sticky, not a JS pinning library, is the
  mechanism (§6.5).

**Accessibility spec**

- Reading and focus order: specimen, then examples in DOM order, pinned
  or not — the visual pin never reorders the document for assistive tech.
- The +15% sort highlighting is decorative emphasis on letters already
  present as text; the specimen block carries an `aria-label` summary
  ("Fraunces specimen: full alphabet, figures, and the long s") so screen
  readers get the artefact, not 52 individual glyphs spelled out.
- Contrast unchanged (ink on paper ≈ 9.4:1); the 105% signature deepens
  shadows only.
- Reduced motion: no pin, no highlighting, static specimen above examples
  (§6.5).

**Tokens consumed:** `--depth`, `--ink`, `--deboss-hi`, `--deboss-lo`,
`--lx`, `--ly`, `--ease-ink`, `--ease-press`, `--pin-length: 100vh`,
`--sort-lift: 15%`, `--sign-depth: 105%`.

---

### D6.6 Brass-rule ink progress — deepening

**Choreography timeline** (continuous, scrubbed; t=0 = first frame of the
shared light loop):

| Beat | What happens |
|---|---|
| t=0 (top of page) | Track renders: brass at 30%, finials at both ends, fill height 0, meniscus flat |
| Scrolling | Fill height = lerped progress (§6.3 loop), trailing the true scroll by ≈ 180ms of lerp tail — ink finding its level |
| Progress crosses each section boundary | No beat of its own; the rule is continuous furniture, and a tick per section would make it a widget |
| Progress = 1 | Meniscus settles flat over 300ms `--ease-ink`; the bottom finial inks from brass to `--ink` — the rule is spent |
| Scroll back up | Fill recedes with the same lerp; the finial un-inks when progress leaves 1. The rule reports position, not achievement |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Empty brass track, finials brass | ≥1100px: identical. <1100px: the rule does not exist (below) |
| Hover | None, by law: furniture does not respond to being looked at (§6.6) | n/a |
| Focus | Not focusable, not interactive; it is `aria-hidden` (below) | Same |
| Active | n/a | n/a |
| Scrolled-past | It has no past state — it always shows *now*: current fill for current position | Leaf counter equivalent (below) |
| Disabled | Loop failed: renders as an empty brass track — a decorative margin rule that misleads no one, because it never displays a number (§6.6) | Same |

**Breakpoint behaviour**

- **≥1200px:** full rule: 2px wide, 40vh tall, centred in the left
  margin, 6px meniscus ellipse, 7px finials.
- **768–1199px:** visible only ≥1100px; at 768–1099px it is omitted (the
  margin cannot hold furniture and air at once).
- **<768px:** omitted entirely. Progress is carried by the folio leaf
  counter in the colophon (§6.17) — "Leaf 3 of 7" — which is where a book
  puts it anyway.

**Edge cases & failure modes**

- Page shorter than one viewport (a 404 leaf, a short contact sheet):
  progress is 1 from load; the rule renders full with its finial inked —
  a one-leaf sheet is fully read by being seen.
- Anchor jump to the footer: fill snaps via the loop's position
  authority (D6.4 rule) — the lerp covers the distance in ≈ 300ms rather
  than scrubbing through every intermediate value at scroll speed.
- Print: the rule prints as an empty brass track at the margin — honest
  furniture; a printed sheet has no reading position.
- RTL locales: the rule mirrors to the right margin; fill still runs
  top → bottom (reading progress is vertical in this theme's fiction).

**Accessibility spec**

- `aria-hidden="true"` and no role: progress here is ambient furniture.
  Screen-reader users get position from the heading structure and the
  leaf counter text (§6.17), which is real content in the DOM — the
  accessible channel is the book's channel, not a `progressbar` widget
  this theme refuses to wear.
- It never carries information by colour alone for any visitor: it
  carries no information at all beyond what scroll position already
  gives. Nothing is lost when it is omitted <1100px.
- Reduced motion: fill jumps in 10% steps at section boundaries —
  progress by leaves turned, not by liquid (§6.6).

**Tokens consumed:** `--brass`, `--ink`, `--lx` (shared loop only),
`--ease-ink`, `--rule-h: 40vh`, `--rule-w: 2px`, `--meniscus: 6px`,
`--finial: 7px`, `--progress` (the loop's lerped 0–1 value, shared with
§6.3).

---

### D6.7 Sheet-lift image reveal — deepening

**Choreography timeline** (t=0 = lift begins; hero: hero-timeline
t≈1,940, i.e. 250ms after the final sort; later plates: their own scroll
entry at 70% viewport):

| Beat | What happens |
|---|---|
| t=0 | One value arms: image `clip-path: inset(0 0 100% 0)`; tissue occupies the un-revealed remainder; edge shadow at 0 |
| t=0–450ms | Inset bottom 100% → 50% on `--ease-sheet`; the lifting edge's shadow rises to its peak (opacity 0.18, blur 12px) at mid-lift — the sheet casts most shadow half-raised |
| t=450–900ms | Inset → 0%; shadow falls back to 0 — flat or gone, the sheet casts nothing |
| t=900ms | Tissue set `visibility: hidden` and removed from the tree; the plate is simply a plate |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Fully revealed; tissue absent from the DOM, not merely transparent (§6.7) | Identical |
| Hover | None — a revealed print is not re-covered | None |
| Focus | The plate's frame is not focusable; if the plate is a link (suite cards, §6.15), focus lands on the card, and the lift is unaffected | Same |
| Active | n/a | n/a |
| Scrolled-past | Stays revealed. The tissue never returns within the session | Identical |
| Disabled | Clip never armed (JS off / watchdog): plate renders un-clipped inside its type-high border (§6.7) | Identical |

**Breakpoint behaviour**

- **≥1200px:** 900ms lift; shadow blur 12px; hero plate ≤ 62ch wide.
- **768–1199px:** 800ms lift; shadow blur 10px.
- **<768px:** 650ms lift; shadow blur 6px — small screens show less sheet,
  and the effect must not outstay its size (§6.7 mobile rule).

**Edge cases & failure modes**

- Image fails to load: the type-high border and caption credit remain —
  a framed, captioned empty block, which in a specimen layout reads as
  intentional (§6.7). The lift still runs on the empty frame if armed
  before the error; if the error arrives first, no lift — never animate
  a broken-image icon.
- Slow network, image arrives after the lift completed: the plate fades
  in at 100% ink over 300ms `--ease-ink` inside its already-revealed
  frame. The ceremony does not re-run for a late plate.
- Image arrives after the §6.11 watchdog (1000ms): same 300ms ink-in;
  the frame has been standing captioned and honest in the meantime.
- Visitor scrolls fast past a below-fold plate: if the plate's section
  was crossed without the lift completing, the plate is revealed
  instantly when next in view — a half-lifted tissue frozen mid-air is
  the one state this element may never be caught in.
- Print: tissue absent, plate prints as its duotone — the print
  stylesheet never includes the covering sheet.

**Accessibility spec**

- The plate is a real `<img>` (or `<figure>`) with meaningful `alt` —
  the suite, the room, the bottle — present in the accessibility tree
  from first paint; the clip is visual only and never `aria-hidden`s the
  image.
- The tissue is `aria-hidden="true"` and carries no text; the caption
  credit (§3) is ordinary text, readable at every lift position.
- Contrast: captions are `--ink` on `--paper` (≈ 9.4:1); nothing is ever
  printed on the tissue.
- Reduced motion: no lift; the plate is present and impresses with its
  section (§6.4).

**Tokens consumed:** `--paper`, `--paper-tooth`, `--ink`,
`--deboss-lo` (edge-shadow tint `rgba(20,66,74,0.18)`), `--ease-sheet`,
`--dur-lift: 900ms` (800 / 650 by breakpoint), `--lift-shadow: 12px`
(10 / 6 by breakpoint).

---

### D6.8 Breathing hero word — deepening

**Choreography timeline** (t=0 = first breath begins — only after every
other hero element is still, §6.14):

| Beat | What happens |
|---|---|
| t=0 | Word at `opsz` 135 (at the 64px hero setting) |
| t=0–2,500ms | `opsz` 135 → 144, ease-in-out — the inhale; letterforms redraw fatter, advance widths shift by < 0.4% (verified non-reflowing, §10) |
| t=2,500–5,000ms | `opsz` 144 → 135 — the exhale. One full breath: 5s |
| t=5,000ms… | Alternates indefinitely, but only while the hero is in the viewport (observer-paused off-screen, §6.8) |
| Hero leaves view | Breath pauses at whatever phase it holds — it does not finish its cycle theatrically; a held breath is still a breath |
| Hero returns | Breath resumes from the held phase |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Mid-swell; there is no "flat" resting state while the hero is on screen | Identical, amplitude halved (below) |
| Hover | No response — pressing is §6.10's job; two interactions on one word would quarrel (§6.8) | No hover |
| Focus | Not focusable (a word of the headline; focus lives on the commission plate, D6.1) | Same |
| Active | n/a | n/a |
| Scrolled-past | Paused off-screen; the word rests at its held `opsz` | Identical |
| Disabled | Variable font unavailable or static weights only: word sits at `opsz` 140, inert — a still print (§6.8) | Identical |

**Breakpoint behaviour**

- **≥1200px:** `opsz` 135 ↔ 144 (±6%), 5s period, at 64px.
- **768–1199px:** `opsz` range ±5% around the 52px setting, 5.5s period.
- **<768px:** amplitude ±3%, period 6.5s (§6.8 mobile rule) — small
  glyphs rasterise coarsely, and a subtle breath survives where a strong
  one would shimmer.

**Edge cases & failure modes**

- The swell reflows the line at some width (a narrow measure, a long
  breathing word): the §10 breath-reflow check has failed — the cure is
  editorial, in order: choose a shorter breathing word; reduce amplitude
  to ±3% at that breakpoint; drop the breath at that breakpoint. Never
  fix it with `overflow: hidden` on the headline.
- Variable font loads after the hero settles: the breath may begin late
  (first breath starts on `fonts.ready` + hero-settled, whichever is
  later) — a breath that starts late is fine; a word that changes face
  mid-breath is a misprint.
- Two editors each mark a breathing word: build lint enforces the §2
  ration (one breathing word per page); the second mark fails the build.
- Battery-saver / data-saver signals (`Save-Data`, low-power heuristics):
  treat as static-font case — word at `opsz` 140, no breath. Ambient
  motion is the first luxury the theme surrenders.

**Accessibility spec**

- Purely ambient and information-free: the word is part of the h1's
  `aria-label` text (D6.1) and reads identically at every `opsz`.
- Reduced motion: off, full stop — the word is set at `opsz` 140 (§6.8).
  A breathing word is precisely the class of motion reduced-motion
  visitors have asked not to receive.
- The swell is a 5s+ cycle — orders of magnitude below any photosensitive
  threshold, and it changes letterform weight, not luminance.

**Tokens consumed:** `--opsz-breath-lo: 135`, `--opsz-breath-hi: 144`,
`--opsz-breath-rest: 140`, `--dur-breath: 5s` (5.5s / 6.5s by
breakpoint), `--breath-amp: 6%` (5% / 3% by breakpoint).

---

### D6.9 Self-drawing brass ornament — deepening

**Choreography timeline** (t=0 = section boundary crosses 85% of viewport
height — struck just before the section it introduces impresses at 78%,
§6.4):

| Beat | What happens |
|---|---|
| t=0–260ms | Left hairline draws 0 → 100% (`stroke-dashoffset`, `--ease-press`) |
| t=200–500ms | Fleuron draws (300ms), overlapping the left rule's tail by 60ms so the strike feels continuous |
| t=440–700ms | Right hairline draws (260ms), overlapping the fleuron's tail by 60ms |
| t=700ms | Ornament complete, brass at 100%. Total: 700ms (§6.9) |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Fully drawn, brass 100% | Identical |
| Hover | None — a divider is furniture (§6.9) | None |
| Focus | Not focusable; `aria-hidden` (below) | Same |
| Active | n/a | n/a |
| Scrolled-past | Stays drawn; ornaments never un-draw | Identical |
| Disabled | JS off: paths render fully drawn by default (`dasharray` is applied by JS only when arming, §6.9). SVG blocked: the CSS double-rule fallback renders at the same width | Identical |

**Breakpoint behaviour**

- **≥1200px:** ornament width 176px, stroke 1.5, sitting in the 132px
  section gap.
- **768–1199px:** width 160px; timings unchanged.
- **<768px:** width 132px (§6.9 mobile rule), section gap is 66px so the
  ornament sits tighter; stroke stays 1.5 — a thinner stroke at small
  size reads as a scratch, not a rule.

**Edge cases & failure modes**

- Two boundaries enter within 700ms of each other (fast scroll): both
  draw; the §6.9 cap of 2 concurrent ornaments holds because boundaries
  enter sequentially by construction — a third waits for the earlier
  one's completion frame, then draws. None is ever skipped to final
  state silently; skipped-to-final is reserved for the watchdog.
- The fleuron asset fails (inline SVG corrupted in a template edit): the
  CSS double-rule fallback covers the joint — the structural mark
  survives the ornament (§6.9).
- Boundary crossed during the platen transition: the ornament of the
  *new* page's first section draws after handover, on that page's own
  timeline (D6.4 queueing rule).
- Print: ornaments print fully drawn — they are part of the sheet.

**Accessibility spec**

- `aria-hidden="true"`, `role="presentation"`: the ornament marks a
  structural joint that the heading structure already announces to
  assistive tech. It must never be the only signal of a section break —
  it isn't; every section it introduces has a real heading (§3, H2).
- Brass on paper is ≈ 3.4:1 — permitted because the ornament is pure
  decoration carrying no information (§2: brass is touched, not read).
- Reduced motion: appears pre-drawn with its section's impression
  (§6.9).

**Tokens consumed:** `--brass`, `--ease-press`, `--ornament-w: 176px`
(160 / 132 by breakpoint), `--ornament-stroke: 1.5`, `--dur-ornament:
700ms`.

---

### D6.10 Press-harder hover — deepening

**Choreography timeline** (t=0 = pointer enters the element, or focus
lands):

| Beat | What happens |
|---|---|
| t=0–200ms | `--press` 1 → 1.3 on `--ease-press`: shadow offsets scale ×1.3, depth reads +30%. On cards, the local light vector begins rotating toward the pointer (≤ 3°) in the same beat |
| t=200ms | Full press held while hovered. No further motion — pressure is a state, not an animation loop |
| Pointer leaves (t=L) | Release: `--press` 1.3 → 1 over 260ms `--ease-press` — paper recovers slower than it yields (§6.10) |
| Click during hover | Hands over to the click press: scale 0.99, ink darkens 8%, 120ms `--ease-thud` hard cap, then activation |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | `--press` 1; card light at the global `--lx/--ly` | Identical |
| Hover | As timeline. Letters: headline/display sorts only — body text never responds (§6.10) | No hover exists. Cards deepen +15% while touched (`:active`); letters do nothing. Hover is never simulated on scroll |
| Focus | `:focus-visible` gives the same +30% depth **plus** the brass ring (§6.16) — keyboard visitors feel the same physics, and can see where they are | Focus (switch/keyboard on touch devices) identical |
| Active | Click press: scale 0.99, ink +8%, 120ms `--ease-thud`; overshoot lives in shadow depth, never scale beyond 0.99 | Touch press: same `thud` on tap, after the +15% touch deepening |
| Scrolled-past | Elements out of view hold no state; a hovered element scrolled away releases normally (pointerleave fires) | Same |
| Disabled | A disabled control (§6.16 plate, D6.16) does not press: `--press` locked at 1, no ring, cursor default — a plate that cannot be struck must not pretend to yield | Identical |

**Breakpoint behaviour**

- **≥1200px:** full system — per-sort press on display type, ≤ 3° card
  light tilt.
- **768–1199px:** card tilt ≤ 2° (smaller blocks, less light to borrow);
  per-sort press unchanged.
- **<768px:** no hover layer at all; `:active` deepening +15% on cards
  and the commission plate only; letters inert.

**Edge cases & failure modes**

- Pointer moves fast across a headline: per-sort presses overlap like a
  hand brushing the case — permitted and pleasant, because each sort's
  cost is two variable writes folded into the single rAF loop (§6.10);
  no per-sort listeners exist to thrash.
- Pointer rests on an element while the page scrolls beneath it: the
  press holds (the element is still hovered); the card's light tilt
  recomputes from the pointer's new relative position each frame of the
  shared loop — no stale angle.
- Touch laptop / hybrid pointer: the first tap applies hover, the second
  activates (§6.10) — for links this is the platform convention and the
  theme follows it rather than inventing its own.
- `pointer: coarse` media query true: the build uses the touch column
  even at desktop widths (a kiosk is a touch device wearing a big
  screen).

**Accessibility spec**

- Hover never reveals content: everything a hover shows (deeper shadow,
  tilted light) is emphasis on what is already fully visible. Nothing in
  this theme is hover-gated.
- Focus is never hover's poor cousin: `:focus-visible` = brass ring
  (2px `--brass`, offset 3px — ≥ 3:1 against paper at ≈ 3.4:1, the one
  sanctioned brass-as-signal use, §2) plus the same +30% press.
- Touch targets: interactive elements keep their §6.16/§6.15 sizes
  (links in cards ≥ 44px tall hit area via padding; the press is a
  shadow effect and never shrinks the target).
- Reduced motion: the depth change applies instantly (0ms) but still
  applies — state feedback is information, not decoration (§6.10).

**Tokens consumed:** `--press`, `--press-hover: 1.3`, `--press-touch:
1.15`, `--lx`, `--ly`, `--brass` (focus ring), `--ink` (active +8% via
`color-mix`), `--ease-press`, `--ease-thud`, `--dur-press-in: 200ms`,
`--dur-press-out: 260ms`, `--tilt-max: 3deg` (2deg at 768–1199).

---

### D6.11 Un-inked skeleton loading — deepening

**Choreography timeline** (t=0 = a block's content request resolves; the
watchdog runs on its own clock from `DOMContentLoaded`):

| Beat | What happens |
|---|---|
| t<0 (loading) | The page's real elements wear `data-inking`: text at 12% ink, image blocks as `--paper-tooth` plates in their real type-high borders, rules at `--hairline`. Zero layout shift — the skeleton *is* the layout |
| t=0 | First resolved block begins inking |
| Per block, staggered 80ms in reading order | Ink 12% → 100% over 500ms `--ease-ink`; depth follows 100ms behind colour — ink first, then the press comes down on it |
| Last block + 500ms | Page indistinguishable from a normally impressed page |
| Watchdog, t=1000ms after a block's content resolves (or after `DOMContentLoaded` for hung requests) | Anything still below full ink is forced to final state in one frame. Nothing shimmers, pulses, or sweeps while waiting — a wet sheen is another theme's material |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (loaded) | No skeleton state exists — loaded blocks are ordinary impressed content | Identical |
| Hover | Skeleton blocks do not respond; there is nothing to press yet | Same |
| Focus | A skeleton block that contains a focusable element (a late-loading slip) is not focusable until inked — focus must never land on a ghost. Focus order follows the resolved DOM | Same |
| Active | n/a while loading | n/a |
| Scrolled-past | Blocks above the viewport ink on resolution regardless of view (they are read by position, D6.4 rule) | Identical |
| Disabled / error | A failed block stays at 12% and gains the oxblood proof mark with its caption — "This leaf failed to print. Retry." (§6.11). Retry is a real button (§6.16 plate language, small size), focusable, and re-enters the loading state on activation. Never a spinner | Identical |

**Breakpoint behaviour**

- **≥1200px:** stagger 80ms; blocks ink in reading order across the full
  specimen spread.
- **768–1199px:** stagger 65ms.
- **<768px:** stagger 50ms — more blocks share the first viewport, and a
  slow ink-in queue on a phone reads as a broken page (§6.11 mobile
  rule).

**Edge cases & failure modes**

- Content hangs forever (dead API): the watchdog inks the placeholder
  regions to 100% at 1000ms with their captions — a legible, captioned,
  un-printed block, never an eternal 12% ghost (§6.11).
- Content resolves out of order (footer data before hero facts): the
  stagger follows *resolution* order per block, but the hero's data line
  is exempt — it inks only within the hero timeline (D6.14), because
  counters arriving before the headline presses would break the
  manufacture order.
- Partial failure (3 of 12 suite cards fail): failed cards hold the
  proof-mark state in place; the grid does not reflow around them —
  blocks in a chase do not slide to close gaps.
- Retry succeeds: the block inks on the standard 500ms timeline from
  retry resolution, proof mark removed at ink start.
- Cache-fast load (everything resolves before first paint): no skeleton
  is ever painted; the page simply arrives impressed. The skeleton is a
  state content passes through, not a ceremony it must perform.

**Accessibility spec**

- The loading region carries `aria-busy="true"` until its last block
  inks; resolution is announced politely via a visually-hidden live
  region ("The sheet is printed") — never per block.
- Skeleton text at 12% ink is placeholder geometry, not content: real
  text is absent from the accessibility tree until it exists (the
  un-inked state renders the *shape* of text regions with no glyphs
  promised to AT). Where genuine placeholder copy is shown (a caption),
  it is real text at full `--ink`.
- The error state's proof note is text, not just a mark: "This leaf
  failed to print. Retry." at ≈ 7.6:1 (`--oxblood` on `--paper`).
- Reduced motion: blocks ink instantly when ready; the 12% state remains
  (it communicates loading) but never animates (§6.11).

**Tokens consumed:** `--ink` (12% via `color-mix` → `--ink-12`),
`--paper-tooth`, `--hairline`, `--oxblood`, `--ease-ink`,
`--dur-ink-in: 500ms`, `--stagger-ink: 80ms` (65 / 50 by breakpoint),
`--watchdog: 1000ms`.

---

### D6.12 Platen page transition — deepening

**Choreography timeline** (t=0 = navigation activated on a plain link the
router has enhanced):

| Beat | What happens |
|---|---|
| t=0 | Input locks (the press is mid-cycle); `div.platen-sheet` enters the DOM, translated 100% below the viewport, carrying only the destination's kicker |
| t=0–260ms | Phase 1: sheet slides up to cover on `--ease-sheet` |
| t≈260ms | Covered moment: the router swaps content beneath the sheet |
| t=260–460ms | Phase 2: the sheet's grain and masthead kicker take impression — depth 0 → 100%, 200ms `--ease-press` |
| t=460–620ms | Phase 3: the overlay's extra grain layer fades to 0 (160ms); the sheet *becomes* the page — its paper is the page's paper, so there is no wipe, only a handover |
| t=620ms | Overlay removed from the DOM; input unlocks; the new page's own impressions run from its scroll position (D6.4 queueing) |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | No overlay in the DOM (§6.12) | Identical |
| Hover | n/a during the 620ms — input is locked | n/a |
| Focus | Focus moves to the destination's `<h1>` (tabindex −1) at handover, t=620 — never left on the removed overlay or the old page's link. The destination kicker the sheet carried is visual only | Same |
| Active | The activating link shows its click press (§6.10 `thud`) in the same frame the transition arms — feedback is never delayed by the ceremony | Same |
| Scrolled-past | n/a (a transition has no scroll state); the new page opens at its top, or at its anchor if the link carried one — the sheet covers the jump either way | Identical |
| Disabled | Router or JS failed: navigation is a normal full-page load, which in this theme looks like a fresh sheet anyway (§6.12). The transition is an enhancement on plain links, never a requirement | Identical |

**Breakpoint behaviour**

- **≥1200px:** full 620ms (260 slide / 200 impression / 160 handover).
- **768–1199px:** 560ms (230 / 190 / 140).
- **<768px:** phase 1 shortens to 200ms (§6.12 mobile rule — a phone
  screen is a small platen); total ≈ 520ms (200 / 180 / 140).

**Edge cases & failure modes**

- Back button mid-transition: the sheet completes its impression
  instantly and hands over — never a half-covered page (§6.12).
- Rapid double navigation (two links in 100ms): the second activation
  is ignored until handover; the press finishes the sheet it is printing.
- Destination errors (404 leaf): the transition still runs and delivers
  the §7 error leaf — the ceremony belongs to the press, not to the
  success of the job.
- Same-page anchor link: no platen transition. Feeding a new sheet to
  move down the current one is theatre without a job; anchors scroll
  (instantly under reduced motion; the light loop follows position).
- Prefetch failure: fall back to the plain link's default navigation;
  the transition never blocks travel.

**Accessibility spec**

- During the 620ms, the old page is `inert`; the overlay is
  `aria-hidden` (its kicker duplicates the destination heading the
  visitor is about to meet). At handover, focus lands on the new h1 and
  the route change is announced by the h1's text itself — no separate
  live-region chatter.
- The transition never traps focus: there are no focusable elements in
  the overlay, and the lock lasts 620ms maximum, watchdog included.
- Reduced motion: no slide — a 150ms opacity crossfade between pages,
  arriving pre-impressed (§6.12).
- Browser back/forward with the transition disabled (bfcache): pages
  restore in their settled states; the press does not re-run for
  history navigation.

**Tokens consumed:** `--paper`, `--paper-tooth`, `--ink`, `--depth`,
`--ease-sheet`, `--ease-press`, `--dur-platen: 620ms` (560 / 520 by
breakpoint), `--platen-slide: 260ms` (230 / 200 by breakpoint).

---

### D6.13 Chase-locked navigation — deepening

**Choreography timeline** (t=0 = first paint of the header):

| Beat | What happens |
|---|---|
| t=0–200ms + 35ms × link index | Links press in left to right, 200ms `--ease-press` each — the compositor locking the row (§6.13). Wordmark first, commission link last |
| Scroll crosses 40px | The chase takes its permanent impression for the page: bottom double rule deepens (shadow depth 0 → 60%, 300ms `--ease-press`); paper behind the bar gains full grain opacity |
| Scroll returns above 40px | The impression stays — a locked chase is not unlocked by looking back (§6.13: "permanent impression for the rest of the page") |
| Page end | Nothing. The chase is the head of the sheet, not a progress instrument (that is §6.6's job) |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Flat, depth 0, airy; links at rest press | Identical |
| Hover | Link: §6.10 press-harder (+30% depth, 200/260ms) | No hover; `:active` deepening +15% |
| Focus | Brass ring (2px, offset 3px) + the +30% press (§6.10 focus rule) | Same for keyboard/switch focus |
| Active | Current page's link sits at depth 130% permanently, with the 7px brass furniture block centred beneath it (§6.13). Note the vocabulary: here "active" is *current-page*, carried by the marker; a link being clicked shows the `thud` press (§6.10) | Identical |
| Scrolled-past | Impressed state (above) for the rest of the page | Identical |
| Disabled | A nav link is never disabled; a link to the current page is *not* disabled either — it is marked current (`aria-current="page"`) and remains a link to the sheet you are on | Identical |

**Breakpoint behaviour**

- **≥1200px:** one row — wordmark 24px Fraunces, ≤ 5 links + commission
  link in the kicker setting (Zilla Slab 600, 12.5px, +0.18em), 1px brass
  furniture rules 18px tall between links.
- **768–1199px:** one row holds to ≈ 900px; below that, the two-row
  variant (wordmark row, links row) — still fully visible, never a
  hamburger (§6.13).
- **<768px:** two rows always. If links still overflow one row at 360px,
  links drop to 11.5px before any are hidden (§6.13). A letterpress sheet
  does not hide its contents in a drawer.

**Edge cases & failure modes**

- Site grows a sixth section: the chase refuses it — §6.13 is an
  information-architecture rule, not a styling preference. The sixth
  section is reached from a page (the suites index pattern, §7), not from
  the chase. A build that wraps the chase to two rows on desktop has
  failed the gate (§10).
- Sticky unsupported: the bar is an ordinary header at the sheet's head;
  the scrolled impression state simply never applies.
- Long wordmark (a two-word atelier name at 24px + 5 links): links drop
  to 12px before the wordmark shrinks — the name of the house outranks
  the furniture.
- The scrolled-impression threshold (40px) vs the hero's pinned elements:
  the check lives inside the shared light loop (§6.13 budget); no
  separate scroll listener is added for the chase.

**Accessibility spec**

- Real `<nav>` with `aria-label="Sections"`; list markup for the links;
  current page marked `aria-current="page"` — the brass block beneath it
  is `aria-hidden` decoration duplicating that fact.
- Focus order is DOM order: wordmark, links, commission link. The
  sticky bar never creates a second tab stop or a focus trap.
- Link contrast: `--ink` on `--paper` ≈ 9.4:1; the brass furniture rules
  are decoration (≈ 3.4:1, §2) and separate links visually without
  carrying meaning.
- Hit targets: each link's hit area ≥ 44px tall (padding inside the bar)
  even though the glyphs are 12.5px — a chase row is tall furniture.
- Reduced motion: links pre-pressed; the scrolled state applies
  instantly at the 40px threshold (§6.13).

**Tokens consumed:** `--ink`, `--brass`, `--paper`, `--deboss-hi`,
`--deboss-lo`, `--press`, `--ease-press`, `--dur-nav-press: 200ms`,
`--stagger-nav: 35ms`, `--nav-impress-scroll: 40px`,
`--nav-marker: 7px`.

---

### D6.14 The Platen Hero — deepening

**Choreography timeline** (t=0 = `document.fonts.ready` resolved; the
hero is the page's entire animation budget for its first 3s, §6.14):

| Beat | What happens |
|---|---|
| t=0 | Kicker impresses: 300ms `--ease-press`, depth 0 → 100% |
| t=0–≈450ms | Chase links lock in above (D6.13 timeline, 200ms + 35ms stagger) — the frame is locked before the type is struck |
| t=120ms | Headline sorts begin (D6.1 timeline): 45ms stagger, 380ms per sort |
| t≈1,570ms | Headline settled (21-sort reference hero, §8) |
| t≈1,690ms | Worn sort landed (D6.2) — the last event of the headline |
| t≈1,940ms | Tissue lifts off the plate (D6.7 timeline, 900ms) |
| t≈1,940–2,840ms | Data-line counters run beneath the lifting plate: 900ms `--ease-ink`, digit columns staggered 60ms (§5) |
| t≈2,840ms | Breathing word takes its first breath (D6.8) — the heartbeat begins when the making ends |
| After | Hero inert except breath and light. Total choreography ≈ 2.9s |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest (settled) | The finished front sheet: kicker, pressed headline, uncovered plate, counted facts, one commission plate | Identical, timeline compressed (below) |
| Hover | Per child element: sorts §6.10, plate none (§6.7), commission plate §6.16. The hero as a whole has no hover state | `:active` deepenings on the plate only |
| Focus | Commission plate is the hero's only focusable element; brass ring + press (§6.10). Focus arriving early (keyboard user tabs during the timeline) does not skip or hurry the presses — focus and manufacture are independent | Same |
| Active | Commission plate click: `thud` (§6.10), then navigation/platen (§6.12) | Same |
| Scrolled-past | No re-print on return; the hero's light is wherever the global azimuth has travelled (D6.3). Breath pauses off-screen, resumes on return (D6.8) | Identical |
| Disabled | JS off / watchdog: the complete static front page in correct reading order (§6.14) — kicker, headline, plate, facts, CTA | Identical |

**Breakpoint behaviour**

- **≥1200px:** headline 64px, plate ≤ 62ch, data line on one line (three
  facts, brass points between), total ≈ 2.9s.
- **768–1199px:** headline 52px, stagger 38ms (D6.1); plate ≤ 56ch; total
  ≈ 2.6s.
- **<768px:** headline 44px pressing per word (≤ 8 units, D6.1); plate
  full-column; data line stacks to two lines; total ≈ 2.2s (§6.14 mobile
  rule).

**Edge cases & failure modes**

- Visitor scrolls before the timeline completes: below-fold impressions
  wait (§6.14 budget rule) but the hero timeline itself is load-triggered
  and finishes off-screen if it must — except the breath, which waits
  for view (D6.8). Nothing queues up behind a scrolled-past hero.
- Editor writes a 3-line headline: §3 caps hand-set display lines at 2
  for the hero; a third line fails lint, because the timeline's
  arithmetic (and the sheet's air) is built for two.
- Plate image missing: the hero runs its full timeline on the framed,
  captioned empty block (D6.7) — the manufacture order does not depend
  on the photograph arriving.
- Returning visitor (session repeat): the full timeline runs again — a
  new visit is a new sheet off the press. Only bfcache restores skip it
  (D6.1).

**Accessibility spec**

- Landmark order: the hero is a `<section>` with the h1 first in reading
  order after the kicker (the kicker is a `<p>`, never a heading).
- All hero text is in the accessibility tree at full value from first
  paint; the timeline is visual manufacture, not content delivery
  (D6.1/D6.4 rule).
- The single CTA's label is the plain verb of the site (§6.16 — "Request
  this suite", never "Press the commission"); its focus ring is the
  brass ring at ≈ 3.4:1 plus the +30% press.
- Reduced motion: the hero arrives whole — pre-pressed headline, plate
  uncovered, counters at final figures, no breath (§6.14).

**Tokens consumed:** `--oxblood` (kicker), `--ink`, `--ink-88`,
`--brass` (data-line points, CTA border), `--paper`, `--ease-press`,
`--ease-ink`, plus the child elements' tokens (D6.1, D6.2, D6.7, D6.8) —
the hero consumes no private tokens of its own; it is a composition, and
its only private values are the beat offsets above.

---

### D6.15 Specimen suite cards — deepening

**Choreography timeline** (t=0 = the card's section impression begins,
§6.4):

| Beat | What happens |
|---|---|
| t=0–700ms | The card's frame impresses with its section (depth 0 → 100%) — the block locks in the chase first |
| t=120–920ms | The plate settles inside the frame: scale-in-frame 1.06 → 1, 800ms `--ease-press`, delayed 120ms behind the frame — the block locks before the plate settles (§6.15) |
| Row stagger | Cards within a row offset by 90ms per card (card *k*: t += 90 × (k−1)); never a cascade of more than 4 (§6.15) |
| Settled | Card is a printed catalogue entry; only hover/focus physics remain live |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed, depth 100%; plate settled; data row in tabular figures | Identical |
| Hover | Light angle tilts ≤ 3° toward the pointer (§6.10); suite name deepens +30% | No hover |
| Focus | The card's link ("View the suite") takes the brass ring + name press (§6.10); the whole card is not a tab stop — one card, one link | Same |
| Active | Click: `thud` (scale 0.99, ink +8%, 120ms), then navigate (§6.12 transition) | Tap: `:active` deepening +15% during touch, `thud` on release-activation |
| Scrolled-past | Static | Static |
| Disabled | The card's disabled analogue is **sold out**: plate desaturates to 60% ink, the oxblood "Edition closed" stamp line replaces the price in the data row (§6.15), and the link is removed — an edition that cannot be commissioned offers no dead control. The card remains readable as a catalogue record | Identical |

**Breakpoint behaviour**

- **≥1200px:** chase rows of three (§7 listing pattern); plates 4:3;
  stagger on.
- **768–1199px:** rows of two; plates 4:3; tilt ≤ 2° (D6.10).
- **<768px:** one column; plates 3:2 (the crop tightens on the pressed
  detail, §6.15); stagger removed — cards impress with their section
  only, because a 6-card stagger on a small screen is a queue the visitor
  did not ask to wait in.

**Edge cases & failure modes**

- More than 12 cards on a page: the §6.15 budget caps *animated* cards
  at 12; cards beyond that arrive pre-impressed with their section (they
  still get §6.4's section impression — what they lose is the individual
  plate settle, not their print).
- A suite with no photograph: the plate block carries the suite's
  specimen initial (its first letter set huge in Fraunces inside the
  frame) — a type block standing in for a plate, in the theme's own
  material, never a grey placeholder box.
- Long suite name (3 lines at 22px): the data row never moves — cards in
  a row share the data-row baseline via the grid; a tall name eats the
  description line's allowance (description truncates to its ≤ 90
  characters, §6.15) before it may push the data row.
- Filter re-lay (§7 listing): the grid re-impresses as one beat — depth
  dips to 40% and back over 350ms — with the *new* card set in final
  positions. Cards never fly between positions; blocks do not fly around
  a chase.

**Accessibility spec**

- Each card is an `<article>`; the suite name is a heading; the single
  link's text names the suite ("View the Hartley Suite") — never "View
  the suite" repeated twelve times to a screen reader.
- The sold-out stamp line is text in the data row, not an image overlay:
  "Edition closed" is read, at `--oxblood` ≈ 7.6:1.
- Plate `alt` names the suite's appearance ("The Hartley Suite:
  deckle-edged invitation with brass-rule border"), not the filename.
- Hit area: the link's padded area ≥ 44px tall; the card's tilt is
  visual only and never moves the target.
- Reduced motion: cards arrive impressed; hover tilt removed; the name
  press becomes instant (§6.10 rule via §6.15).

**Tokens consumed:** `--ink`, `--brass`, `--paper-tooth`, `--oxblood`
(sold-out line), `--deboss-hi`, `--deboss-lo`, `--lx`, `--ly`, `--press`,
`--ease-press`, `--ease-thud`, `--dur-plate-settle: 800ms`,
`--stagger-card: 90ms`, `--card-cap: 12`.

---

### D6.16 The commission slip — deepening

**Choreography timeline** (interaction-triggered; t=0 = the event named):

| Beat | What happens |
|---|---|
| Focus lands on a field (t=0) | Leader line inks `--hairline` → full `--ink` over 200ms `--ease-ink`; the field's label takes a shallow impression (depth 40%, 200ms `--ease-press`) — the slip acknowledges where the pencil is |
| Field blurs, filled | Its line rests at 60% ink — a completed line is darker than an untouched one |
| Field blurs, empty & required | Line returns to `--hairline`; no error yet — a printed form does not scold a line the pencil merely visited |
| Submit with errors (t=0) | Each offending field's line turns `--oxblood`; its proof mark — the circled field number with a ≤ 3-word note ("Date precedes today") — draws in the slip's right margin over 300ms `--ease-press`, staggered 60ms per error in field order. Focus moves to the first error field and its note is announced |
| Submit, valid (t=0) | The plate presses (`thud`, 120ms); the whole slip takes a full impression (depth → 100%, 500ms `--ease-press`) and *holds* it while the request sends — the form is being pressed |
| Response arrives | Success: slip contents replaced by the colophon-voice confirmation (§6.16), impressed once, permanently. Failure: the slip releases its impression (depth → resting over 300ms) and a proof note appears at the slip's head — the request, not a field, is marked |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Hairlines faint (`--hairline`), labels flat, plate at rest depth | Identical; slip full-bleed (below) |
| Hover | Fields: no hover state — a form line does not respond to being looked at. Plate: §6.10 press-harder (+30%) | Fields: none. Plate: `:active` +15% |
| Focus | As timeline: line inks, label impresses 40%. Focus ring on the plate = brass ring + press (§6.10). Inputs themselves show focus through the line — never an outline box, which would be software chrome on a printed form | Same; the on-screen keyboard's arrival never shifts the slip (its geometry is fixed by its border) |
| Active | Plate click: `thud` 120ms, then the submit beats above | Same on tap |
| Scrolled-past | n/a for fields; a slip half-scrolled keeps its filled/error states exactly — form state is never a scroll effect | Identical |
| Disabled | *Submitting:* inputs disabled, plate at depth 130% and inert, slip impressed (§6.16). Disabled fields render their entered values at full `--ink` (readable — a disabled grey would be un-inked type, §3) with lines at 60%; the plate's label changes to the apparatus line "Pressing…" only under reduced motion (§6.16) — with motion, the held impression *is* the label | Identical |

**Breakpoint behaviour**

- **≥1200px:** slip at 58ch inside its type-high border; proof notes in
  the right margin, aligned to their field's baseline.
- **768–1199px:** slip at 54ch; margin notes remain (the margin is
  narrower but exists).
- **<768px:** slip full-bleed — border becomes top and bottom double
  rules only (a slip torn to width); inputs at 18px (also preventing iOS
  zoom); proof notes move *beneath* their fields, because a phone slip
  has no right margin (§6.16 mobile rule).

**Edge cases & failure modes**

- Server-side error the client didn't catch (date valid but the edition
  sold out an hour ago): the error returns as a head-of-slip proof note
  in the same voice ("This edition closed yesterday") and the affected
  field gets the margin mark — the proof system covers the whole slip,
  not just fields.
- Double submit (impatient double-click): the plate is disabled at first
  activation; the held impression is also the visual lock. A second
  request is never sent.
- Browser autofill: filled lines take the 60% ink state on the next
  frame — autofilled handwriting is still handwriting on the line.
- JS validation fails to load: the plain HTML form submits and the
  server re-renders with the same proof notes as text (§6.16 fallback).
  Every enhancement is CSS/JS over a working form.
- Very long error note from the server: client notes are ≤ 3 words by
  rule (Part II §F voice rules); server notes are re-rendered verbatim
  but wrapped in the margin at caption size — the margin mark (circle +
  field number) is the constant, the note is the variable.

**Accessibility spec**

- Every field: a real `<label>` in the kicker setting, programmatically
  associated; the brass point marking "required" is duplicated by the
  `required` attribute and an `aria-hidden` visual only — screen readers
  get the requirement from the platform, not the punctuation.
- Errors: each proof note is tied to its field with
  `aria-describedby`, the field carries `aria-invalid="true"`, and the
  first error is focused on submit. Errors never time out (§6.16) and
  are never colour-only: line colour + margin mark + text note, three
  channels.
- The submitting state sets `aria-busy="true"` on the slip; success
  replaces it with a confirmation headed as a heading, so the outcome is
  in the reading order, not a toast (this theme has no toasts — §F).
- Touch targets: fields' hit rows ≥ 48px tall (11px padding below the
  baseline plus the label row); the plate is full-slip-width and ≥ 52px.
- Contrast: labels and entered text `--ink` on `--paper` ≈ 9.4:1; error
  notes `--oxblood` ≈ 7.6:1; the `--hairline` at rest is a border, not
  text, and the field it underlines is always labelled in full ink.
- Reduced motion: focus/error states apply instantly; submit skips the
  impression hold and shows the static "Pressing…" apparatus line
  (§6.16).

**Tokens consumed:** `--ink`, `--hairline`, `--oxblood`, `--brass`,
`--depth`, `--press`, `--ease-ink`, `--ease-press`, `--ease-thud`,
`--dur-field-ink: 200ms`, `--dur-proof: 300ms`, `--dur-slip-press:
500ms`, `--line-filled: 60%`.

---

### D6.17 Colophon footer — deepening

**Choreography timeline** (t=0 = the colophon's section impression,
§6.4):

| Beat | What happens |
|---|---|
| Approach | The sorts-tray strip (15vh of oversized Fraunces glyphs at 12% ink) begins drifting at 9px/s only when the band enters view (§6.17) |
| t=0–700ms | Colophon impresses with its section — the final press of the page |
| Section boundaries (page-wide) | The leaf counter ("Leaf N of M", visible <1100px only) crossfades its numeral over 200ms `--ease-ink`, tabular figures so the line never changes width |
| Footer leaves view | Drift pauses. The case is put away only while someone is watching it be put away |
| Page settled | Nothing else moves; the end of the sheet is the quietest part of it (§6.17) |

**State matrix**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed colophon: ornament (pre-drawn), type credits, edition line, legal line, links | Identical; sorts strip 10vh, leaf counter present (below) |
| Hover | Links: rubric underline draws + §6.10 press | No hover |
| Focus | Links: brass ring + press (§6.10 focus rule), underline drawn | Same |
| Active | Links: `thud` press, then navigation (§6.12) | Same |
| Scrolled-past | n/a — it is the end of the sheet | n/a |
| Disabled | Drift disabled (JS off): the sorts strip renders as a static specimen line (§6.17). The colophon text is never in a disabled state — it is print | Identical |

**Breakpoint behaviour**

- **≥1200px:** centred apparatus column (13.5px, §3); sorts strip 15vh;
  leaf counter hidden (the brass rule, §6.6, carries progress here).
- **768–1199px:** colophon unchanged; at <1100px the leaf counter
  appears in the edition line (§6.6 hand-off); sorts strip 12vh.
- **<768px:** colophon unchanged (it was always a narrow column); sorts
  strip 10vh; leaf counter present (§6.17 mobile rule).

**Edge cases & failure modes**

- Very short page (the 404 leaf): the colophon is the second thing on
  the sheet; its impression runs on load like any section's, and the
  leaf counter reads "Leaf 1 of 1" — a one-leaf book is still a book.
- Edition line data missing (a build without the edition apparatus):
  the line is omitted, never faked — the colophon tells the truth about
  itself (§6.17), and an invented edition number would be exactly the
  kind of lie this footer exists to refuse.
- The sorts drift's glyph set (`& A a E e G g R r ſ`, §5) renders in a
  fallback face if Fraunces fails: the strip drops to static (a drifting
  strip in the wrong face is a costume, §9) while the colophon text
  still impresses.
- Print: the colophon prints as text; the sorts strip prints as its
  static specimen line; the leaf counter does not print (a printed sheet
  is all leaves at once).

**Accessibility spec**

- The colophon is a `<footer>` (`contentinfo`); its lines are plain
  text in reading order; the edition and leaf-counter lines are real
  text — the leaf counter is the accessible progress channel that
  replaces the `aria-hidden` brass rule (D6.6).
- The drifting sorts are `aria-hidden="true"` — oversized decorative
  glyphs must never be read out as letters.
- Links meet the §6.10 focus spec; contrast is `--ink` on `--paper`
  ≈ 9.4:1 at apparatus size (13.5px is above the theme's 15px floor
  exception only here, because apparatus is credits, not body — and it
  still passes AA at 9.4:1).
- Reduced motion: sorts strip static; leaf counter updates instantly;
  colophon pre-impressed (§6.17).

**Tokens consumed:** `--ink`, `--brass`, `--paper-tooth`, `--depth`,
`--ease-ink`, `--dur-drift: 9px/s` (linear), `--strip-h: 15vh` (12 /
10 by breakpoint), `--leaf-fade: 200ms`.

---

## E. Component inventory — every component, in the theme's materials

A real site needs more than the §6 elements. Each component below is the
theme's answer, built from the same chase, inks and press physics. If a
component is not listed here and cannot be built from these rules, the
requirement belongs to a different theme (§9, app chrome creep).

| Component | Letterpress treatment |
|---|---|
| **Primary button** | The commission plate (§6.16): brass-bordered block, kicker-setting label in `--ink`, rest depth 100%; hover §6.10 (+30%); click `thud` (0.99, ink +8%, 120ms); disabled = plate at 60% ink with `--hairline` border, inert, label unchanged (never greyed into illegibility — disabled text stays ≥ 4.5:1) |
| **Secondary button** | The proof plate: same block geometry with the double-rule ink border (3px + 1px) instead of brass, transparent fill. It is the same object in the other ink — hierarchy is carried by material, not size |
| **Text link** | Rubric-style underline (§6.15/§6.17): hairline at rest, draws to full `--ink` on hover while the text presses +30%; visited links take the underline at 60% permanently — a line already read is marked, like a pencil tick in a margin |
| **Text input** | A slip field (§6.16): label above, leader line below, entered text in Zilla Slab 18px *on* the line. No boxes, no placeholder-as-label; a placeholder, if unavoidable, is a printed example in `--hairline`-weight text ("e.g. 250 sheets") and never the only label |
| **Textarea** | The letter field: three leader lines ruled on the slip, text flowing across them at 18px/1.68; the lines are a repeating background rule, so handwriting sits on lines like a written sheet. Grows by ruled lines, never a scrollbar inside the sheet |
| **Select** | A printed-list select: native `<select>` wearing the slip field's leader line and a brass point as its marker. The open list is the platform's own — the theme styles the closed field and refuses to fake the open menu, which would be software wearing a paper costume (§6.16's rule applied to menus) |
| **Checkbox** | The proof tick: a 16px square rule box (1px `--ink`); checked = an ink tick drawn inside over 150ms `--ease-press`, as if ticked by hand on the proof. Indeterminate = a horizontal sort through the box |
| **Radio** | The sort choice: a 16px circular rule; chosen = a centred ink point (a brass point for the commission-critical choice). A radio group is set as a vertical list with 11px gaps — a list of sorts in the case |
| **Toggle / switch** | **Refused as a switch.** A sliding pill is app chrome. The theme's binary is a pair of radio sorts (above) or, for a proofing decision, the proof pair: two rubric options on one line — "Proofed · Not yet" — the chosen one underlined. State changes are decisions recorded on the sheet, not levers thrown |
| **Number field** | A slip field whose value is set as data (Zilla Slab 500, tabular). Steppers are two brass points ( − / + ) flanking the line, 44px targets; typing is always allowed — the numbering machine accepts hand-setting |
| **Table** | The ledger table: head row under the double rule (3px + 1px), body rows separated by `--hairline` rules, figures right-aligned in tabular Zilla Slab with dotted leaders running from label to figure — a price-list, not a spreadsheet. Row hover: the row's figures press +15% (data is apparatus; it deepens, it does not highlight). No zebra striping — paper does not alternate |
| **Badge** | The edition seal: a small double-rule block in apparatus type — "Edition of 250", "600gsm cotton". Status is set as a line, never a pill: "Edition closed" in `--oxblood` (§6.15). Pills are refused — a badge here is a printed block or it is nothing |
| **Alert** | The press notice: a type-high-bordered block at the head of its section. Information in `--ink` with the fleuron; problems in the proof voice with the oxblood circled mark (§6.16). It impresses with its section and stays until resolved or dismissed by a rubric "Set aside" link — alerts on a sheet are leaves, not banners |
| **Pagination** | Leaf pagination: a centred apparatus line — "Leaf 2 of 5" — flanked by rubric links "Earlier leaves" / "Later leaves". Numbered leaves (1 2 3 …) may follow in tabular figures, the current leaf at depth 130% like the nav's current marker (§6.13). Never an app-style pager with boxed numbers |
| **Modal** | A sheet laid over the sheet: the underlying page dims toward `--paper-tooth` (the light leaves it), and a second sheet — `--paper`, type-high border, full colophon margins — settles centred by impression (depth 0 → 100%, 300ms `--ease-press`), never by scale or fade-up. It is used for one job only: examining a plate closely (the suite at full size, with its caption and data). Focus is trapped inside the laid sheet; Esc or the rubric "Return the sheet" link lifts it (reverse impression, 200ms). Anything that wants a modal for a form belongs on the slip (§6.16) |
| **Toast** | **Refused** (§9). Outcomes are printed in place — the confirmation block (§6.16), the press notice (above), the colophon line. See §F for the voice those printed outcomes use |
| **Tabs** | The specimen index: a row of kicker-setting labels separated by brass furniture rules, the active label at depth 130% with the 7px brass block beneath (the chase's current-marker, §6.13, reused). Switching dips the panel's depth to 40% and re-impresses over 350ms — the re-lay beat of §7's filter. Panels are leaves of one sheet, not screens |
| **Accordion** | The folded leaf: a `<details>` whose summary is a ledger line with a brass point that inks from `--hairline` to `--brass` when open; the revealed block impresses (depth 0 → 100%, 350ms `--ease-press`) — unfolding is a small press stroke. Only one fold open per group: a sheet shows one fold at a time |
| **Tooltip** | The margin note: a term underlined with a dotted `--hairline` (a pencil line); hover or focus sets a small apparatus note (13.5px) in the margin beside it on desktop, beneath it <768px. It appears by impression (200ms), never follows the pointer, and its content is a definition or a paper fact — never a restated label |
| **Breadcrumb** | The running head: apparatus line at the head of detail pages — "Suites · The Hartley Suite" — segments joined by brass points, ancestors as rubric links, the current leaf unlinked at full ink. It sits above the H1 like a book's running head, not in a grey bar |
| **Pull quote** | The specimen line: one line set in Fraunces H2, centred, the brass ornament (§6.9) drawn above it, attribution in apparatus beneath. It impresses with its section. A quote in this theme is a line worth setting in display type — if it isn't, it stays in the reading column |
| **Tag / chip** | The paper tag: a small hairline-bordered apparatus label ("600gsm", "Deckle edge", "Edition of 250") — a fact tied to its object like a string tag on a parcel. Tags are never removable and never filters; filtering is the printed index line (§7). A removable chip is app chrome |
| **Search** | The index search: one slip field at the head of the listing page, labelled "Search the index"; results re-lay the grid with the single re-impression beat (§7). No search icon button, no expanding search pill — a field on the sheet, like every field here |
| **Skip link** | "Skip to the sheet": apparatus text, invisible until focused, then printed at the sheet's top-left with the brass ring. It is the first thing a keyboard visitor meets, set like everything else |
| **Divider** | The brass ornament (§6.9) between sections; the double rule within blocks. No other divider exists |

---

## F. Content & copywriting voice

**The voice in one sentence:** the atelier writes the way its colophon is
set — plainly, exactly, and only about things it can point to: paper,
ink, numbers, dates. If a sentence could be pasted onto a SaaS landing
page, it is rewritten or cut.

**Headlines.** Sentence case, concrete nouns, one idea. The craft verb
may appear literally at most once per page ("Pressed by hand" is a fact
about the process; "Crafted with passion" is weather). No exclamation
marks anywhere on the sheet. No superlative without a number attached.

- Do: "Pressed by hand, kept for good." / "Twelve rooms, one press, no
  two menus alike."
- Don't: "Experience the timeless elegance of artisanal luxury!" /
  "Discover our amazing bespoke creations."

**Kickers and labels.** Uppercase apparatus naming the class of thing,
never the sell: "Wedding suites", "Cotton papers", "The edition". A
kicker that promises ("Limited offer!") is a proof error.

**Buttons.** The plain verb of the transaction, in kicker setting:
"Request this suite", "Send the commission", "Reserve the room". Never
"Submit", never "Press the commission" (§6.16 — the theatre is in the
physics, not the label), never "Get started".

**Data.** Paper always in gsm ("600gsm cotton", never "thick luxury
paper"). Editions always "Edition of N". Prices set as data, in tabular
figures, with the currency before the figure. Dates in prose are written
out — "Saturday 14 June" — because a printed form spells its dates;
dates in tables are tabular.

**Error voice — the proofreader's note.** Short, located, factual; it
says what is wrong and where, in the margin, without blame and without
apology theatre. Three words is the client-side budget (§6.16); server
notes may run to a sentence but keep the register.

- Do: "Date precedes today." / "Quantity exceeds the edition of 250." /
  "This edition closed yesterday."
- Don't: "Oops! Something went wrong." / "You entered an invalid date."
  / "Error 422."

**Empty-state voice — the unprinted leaf.** An empty state states the
fact and the next event, in apparatus: "No suites are on the press this
month. The next edition is set in March." Never a mascot, never "Nothing
to see here!", never a fake CTA to fill the silence.

**Confirmation voice — the colophon.** A success is recorded the way the
footer records the edition: what was requested, its reference in tabular
figures, what happens next, and the timescale in prose. "Commission
received · № 0417. The press answers within two working days." That is
the whole confirmation pattern — and it is why this theme has no toasts
(§E): outcomes are printed where they happened, in this voice, and they
stay on the sheet.

**Microcopy rulings.**

| Context | Write | Never write |
|---|---|---|
| Loading | (nothing — the un-inked sheet is the message, §6.11) | "Loading… please wait" over a spinner |
| Submitting | "Pressing…" (apparatus, reduced-motion only, §6.16) | "Submitting your request…" |
| Sold out | "Edition closed" | "Out of stock!" / "Sold out 😢" |
| Form hint | "The date the suite is needed" | "Please enter a valid date" (that is an error's job, after the fact) |
| Search, no results | "No leaf in the index matches." | "No results found. Try different keywords?" |
| 404 | "This leaf was not bound in." (§7) | "404 — Page not found" |
| Price note | "£180 · Edition of 250" | "Only £180 — while stocks last!" |

---

## G. Three worked examples, end to end

§8 built one hero. These three build the other two-thirds of a real page —
and the hero again, for a different trade — each with its scroll timeline,
so a builder can see the theme *sequenced*, not just specified.

### G.1 Hero — a boutique hotel ("The Marlowe Inn")

**The job.** Twelve rooms; the inn's menus, key cards and in-room notes
are letterpressed in-house, and the site must feel like checking in
slowly. Headline: "Twelve rooms," / "one press." — the worn sort is the
`o` in "rooms" (never the first word's first letter, §3; "Twelve" prints
clean). Breathing word: "press". Plate: the inn's frontage as a teal
duotone, caption "The Marlowe Inn · Menus set weekly, in the hall".
Data line: "12 rooms · Est. 1962 · Menus set weekly". CTA (the
commission plate, hotel verb): "Reserve a room".

**Scroll timeline** (t = ms from `fonts.ready`; scroll beats by hero
traverse):

| Beat | Timeline |
|---|---|
| t=0 | Kicker "A country inn · Est. 1962" impresses (300ms) |
| t=120–≈1,450 | Sorts press: 19 sorts over two lines at 45ms stagger; worn `o` lands at ≈ t=1,570 on its +120ms delay |
| t≈1,820 | Tissue lifts off the frontage plate (900ms); beneath it the data line counts: 12 (rooms) rolls first, 1962 second — the year counts *up* through the inn's life, a numbering machine with a memory |
| t≈2,720 | "press" takes its first breath. Hero settled |
| Scroll 0–25% of hero traverse | Light swings 118° → ≈104°; the headline's depth re-lights — the visitor feels the lamp before they could name it. Brass rule begins to fill |
| Scroll: hero at 50% gone | Breath pauses mid-phase (D6.8); the plate is scrolled-past and never re-lifts |
| Scroll: next section (rooms ledger) top crosses 78% | It impresses (§6.4) while the hero's last light leaves it — one press stroke ends as the next begins |

**Failure rehearsal.** Fonts hang: watchdog prints the whole hero at
t=1000, plate uncovered, counters at 12 and 1962 — a letterhead for the
inn, complete. The booking link works. Nothing about the failure is
visible as failure.

### G.2 Mid-page section — the papers ledger (a stationer's home page)

**The job.** The atelier's paper stocks, mid-page, in the ledger rhythm
(§4): a reading column of prose about cotton paper, beside a ledger table
(§E) of the four stocks — name, weight, sheet size, price per 100 sheets —
with one duotone plate of the paper vault. This is the section that
proves the theme can carry *data* without becoming a dashboard.

**Composition.** Ornament (§6.9) above. H2 "The papers" with its double
rule. Left: 62ch prose, two paragraphs. Right (ledger column): the table
— head under the double rule, four rows on hairlines, figures tabular
with dotted leaders ("Cotton, handmade …… 600gsm …… £42"). Below the
table, two counters as apparatus facts: "4 stocks · 1,850 sheets on the
shelf" — the sheet count is real inventory data or it is not printed
(Real Content: the counter counts the stock figure the CMS holds, or the
line is omitted, §6.17's truth rule applied mid-page).

**Scroll timeline:**

| Beat | Timeline |
|---|---|
| Boundary crosses 85% | The ornament draws (700ms, D6.9) — the divider is struck first |
| Section top crosses 78% (t=0) | Section impression: depth 0 → 100% (700ms), ink 88% → 100% (from t=80, 900ms). Prose and table impress *together* — one platen stroke for the whole leaf |
| t=120 (relative) | The plate settles in-frame (1.06 → 1, 800ms) inside its type-high border |
| Data block crosses 78% | Counters roll: "4" in one column beat; "1,850" across four digit columns staggered 60ms, 900ms total — the numbering machine stamping the stock |
| Scroll through | Table row hover presses figures +15% (§E); the light crosses the section, azimuth moving ≈ 8° across its traverse; the prose's deboss re-lights with it |
| Section leaves top | Nothing un-impresses. The ledger is read; its ink stays |

**What the visitor feels.** A page of a stock book being printed as they
reach it — and, crucially, the table reads *faster* than a SaaS table,
because the leaders carry the eye and the figures are honest tabular
type. Depth never touches the figures' legibility: counters and data sit
at the shallow end of the deboss range by §3's data rules.

### G.3 Conversion section — the commission slip (a suite detail page)

**The job.** The bottom of "The Hartley Suite" detail page (§7): the
slip, pre-filled with the suite's name on its first line — a slip pulled
for a known job already has the job written on it. Fields: suite
(pre-filled), paper (radio sorts: 600gsm cotton / 300gsm cotton /
recycled laid), quantity (number field), date needed (date field), name,
address (letter field, three ruled lines). Plate: "Request this suite".

**Scroll timeline:**

| Beat | Timeline |
|---|---|
| Approach | The section above (the suite's story) is scrolled-past and static; the slip's type-high border enters |
| Slip top crosses 78% (t=0) | The slip impresses as one block (700/900ms, §6.4) — the whole form is struck at once, never field by field |
| t≈980 | Settled. The pre-filled suite line already sits at the 60% "filled" ink (D6.16) — the visitor sees the job is half-written, which is the conversion argument: *this slip is already yours* |
| Visitor scrolls the slip fully into view | Nothing further animates. A form is a document, not a show |

**Interaction timeline** (the same slip, used):

| Beat | Timeline |
|---|---|
| Focus: quantity (t=0) | Line inks to full over 200ms; label impresses to 40%. Visitor types 300 |
| Blur | Line rests at 60%. The figure is set in tabular 500 — it looks stamped already |
| Focus: date; visitor picks a past date; blur | No scolding yet (D6.16: a visited line is not an error) |
| Plate pressed (t=0) | `thud`, 120ms. Validation: the date field's line turns `--oxblood`; the proof mark draws in the margin over 300ms — circled field number, note "Date precedes today". Focus moves to the date field; the note is announced via `aria-describedby` |
| Visitor corrects the date (t=0) | On correction, the proof mark is struck through by a single hairline (a proofreader's deletion — 150ms) and the line returns to 60% filled ink. The error is *answered*, not vanished: the struck mark remains visible until submit, the paper trail of the proof |
| Plate pressed again (t=0) | `thud`; the whole slip impresses to 100% over 500ms and holds; inputs disable at full-ink legibility (D6.16) |
| Response (t≈+900) | The slip's contents are replaced by the confirmation, impressed once: "Commission received · № 0417. Suite: The Hartley. Paper: 600gsm cotton, 300 sheets, for Saturday 14 June. The press answers within two working days." (§F confirmation voice) |
| Failure variant | Network fails: the slip releases its impression over 300ms; a press notice (§E) prints at the slip's head — "The commission was not received. The line is open — try again." — and every entered value is still on its line. Nothing the visitor wrote is ever lost to a failed press |

---

## H. Full-page scroll choreography map — the canonical home page

The §7 home page, top to footer. Progress is document scroll fraction;
`--az` and the brass rule (§6.6) are functions of it. Every beat is
something the visitor *sees happen to the content* — there are no beats
that happen to decoration alone.

| Scroll | Beat | What the visitor sees and feels |
|---|---|---|
| 0% (load) | The manufacture: chase locks (D6.13), kicker impresses, headline sorts press, worn sort lands last, tissue lifts, counters stamp, breath begins (D6.14) | A page being made in front of them, once, in under 3s — then stillness |
| 0–8% | Light leaves its morning angle (118° → ≈110°); brass rule's meniscus first moves | The lamp is alive; progress has a material |
| ≈8% | Ornament №1 draws (85% crossing); editions ledger section impresses at 78% | The divider is struck, then the section is printed under it |
| 8–20% | Editions ledger: counters roll once (edition sizes, gsm); specimen rhythm gives way to ledger rhythm (§4) | Numbers arrive like a numbering machine, then the page is a document again |
| ≈22% | Grain brightens +4% as the light crosses the section boundary (D6.3) | A breath of weather on the sheet — felt, not noticed |
| 25–40% | The pinned specimen (§6.5): alphabet holds for 100vh while the invitation, label and menu examples traverse; sorts highlight +15% as each example centres | The case of type, showing which letters are on each job — the atelier's whole claim, staged |
| ≈40% | Pin releases: specimen signs at 105%, rests at 100%. Ornament №2 draws | The press signs its work; the sheet moves on |
| 42–58% | Suite grid (§6.15): frames impress, plates settle 120ms behind, rows staggered 90ms (≤ 4) | Blocks being laid in the chase, one at a time |
| ≈58% | Light passes 90° — shadows now fall straight-left; the sheet feels like midday in the pressroom | The day is turning, though nothing said so |
| 60–75% | Papers reading column (§6.4, two-beat impression for its length); one plate's tissue lifts at 70% entry | The quietest stretch: prose, one uncovered photograph, the light doing all the work |
| ≈76% | Ornament №3 draws; the atelier paragraph impresses; founding-year counter rolls once, alone | Restraint as a beat — one number on a whole leaf |
| 78–90% | Commission invitation section: a short reading column and the commission plate (the page's second and last CTA) | The ask, made of paper, after the evidence |
| ≈90% | Light at ≈66°; shadows lengthen up-left; already-read sections read flatter behind the visitor | Afternoon. The sheet is nearly read |
| 92–100% | Sorts-tray strip starts drifting as it enters; colophon impresses — the final press; leaf counter (if <1100px) settles on the last leaf | The case being put away; the book's back page tells the truth about itself |
| 100% | Brass rule full, bottom finial inked; light at 62°; breath long paused (hero far above) | The sheet is read. Everything is still. Nothing is looping except the tray, quietly, at the end of the day |

**Map rules.** (1) No two press strokes overlap: a section's impression
never runs while another is mid-stroke — sequential entry makes this
structural, and the D6.4 queue holds any exception. (2) The light is the
only continuous system; everything else is a beat with a start and an
end. (3) Any page type other than home re-maps by deletion (the listing
loses the pin and the breath; the detail page keeps the lift and the
slip) — beats are removed, never added, per §2's ink discipline.

---

## I. Whole-page performance budget

The theme's physics are cheap by design (one loop, CSS shadows), and this
budget keeps them that way. Exceeding any line is a §10 gate failure.

**Asset weight (per page, compressed):**

| Asset | Budget | Notes |
|---|---|---|
| HTML | ≤ 35KB | Sort spans are markup, not JS output (§6.1) |
| CSS | ≤ 48KB gzip | The full shadow system is arithmetic on 4 custom properties, not per-element shadow libraries |
| JS | ≤ 22KB gzip | One loop, one observer, the slip's validation, the router hook. No pinning/animation libraries — sticky and CSS do the work |
| Fraunces variable | ≤ 85KB | Subsetted (latin), `opsz` + `wght` axes only; `SOFT`/`WONK` are served but the subset keeps them — they are the face's manners (§3) |
| Zilla Slab 400/500/600 | ≤ 60KB total | Three static weights, subsetted |
| Grain SVG tile (inline) | ≤ 1.2KB | One 180 × 180 `feTurbulence` tile, reused by background repeat |
| Fleuron ornament SVG (inline) | ≤ 0.8KB | One path asset, reused identically (§6.9) |
| Hero plate | ≤ 180KB | Duotone WebP/AVIF; it is the LCP element and is budgeted like one |
| All plates per page | ≤ 700KB | Duotones compress hard; a plate over budget is re-exported, never lazy-excused above the fold |
| **Total initial load** | **≤ 1.05MB** | Fonts + hero plate dominate, as they should — the materials are the weight |

**Frame budget (60fps target):**

- Per frame, the light loop does: one progress lerp, one azimuth
  computation, **two** CSS variable writes (`--lx`, `--ly`), one brass
  fill height write, one chase threshold check. Measured cost target
  ≤ 0.4ms of JS per frame. No layout reads inside the loop — element
  positions are cached on resize and on section registration.
- Shadow repaint is the browser's cost and is bounded structurally:
  ≤ 3 shadow layers per element, no `box-shadow` animation on elements
  larger than 40% of the viewport except the sheet itself (§6.3).
- At most 3 elements mid-animation per viewport, 1 section mid-impression
  (§5, §4 — the budget restates the design rules as engineering limits).

**Long-task & metrics limits:**

- No long task > 50ms anywhere, including the hero timeline: every beat
  in D6.14 is CSS-driven or a ≤ 16ms JS arming step.
- LCP ≤ 2.0s on a mid-range Android over 4G (the hero plate, preloaded);
  CLS = 0 across load (the skeleton is the layout, §6.11); INP ≤ 200ms
  (the slip's heaviest interaction — validation + proof marks — is
  ≤ 30ms of JS).
- First impression frame ≤ 50ms; if it exceeds that, the §5 degradation
  trigger fires and the static-light variant ships instead.

**Cut order when the budget is exceeded** (cut in this order, and only
in this order — the list runs from most decorative to most structural):

1. Sorts-tray drift (§6.17) — static specimen line.
2. Breathing word (§6.8) — word rests at `opsz` 140.
3. Raking light range — narrow to 100° → 75° at all widths, then lock
   at 90° (loop stops).
4. Letter pressing — per-word instead of per-letter (D6.1).
5. Plate settle — plates impress without the scale-in-frame.
6. Grain tile — removed; the sheet is smooth cotton.

**Never cut, at any budget:** impression-on-entry with its fallbacks,
the 1000ms watchdog, the reduced-motion variants, the no-JS printed
page, the slip's working form. Those are not effects; they are the
theme's honesty, and a build that cuts them is a different, worse theme
wearing this one's palette.

---

## J. Build-order checklist

Build in this sequence. Each step depends on the ones above it; the
checkpoints are gates, not suggestions.

1. **Tokens first.** Declare the §2 palette, the Part II shared tokens
   (easings, `--lx/--ly/--az`, `--depth`, `--press`), and the 11px module
   (§4). Nothing is styled before the tokens exist.
2. **Base CSS = the printed sheet.** Build every page fully static:
   chase, sections, cards, slip, colophon — final states only, no JS.
   This is the fallback and the foundation in one.
3. **Checkpoint: the no-JS test.** Screenshot every page with JS
   disabled. It must already look like the finished site (§10, first
   gate). If it doesn't, nothing above this line proceeds.
4. **Type system.** Font loading with `document.fonts.ready` gating;
   hand-set line spans in display markup; the worn-sort ration lint
   (§3) wired into the build.
5. **Impression system.** `data-press` arming, the IntersectionObserver
   (§6.4), two/three-beat tall sections, the anchor-jump position rule
   (D6.4), and the 1000ms watchdog (§6.11) — before any individual
   element animates, the *safety* animates.
6. **The light loop.** §6.3 loop with `--lx/--ly/--az`, the sleep/wake
   rules, the §5 degradation trigger, and the brass rule (§6.6) riding
   the same loop.
7. **Hero assembly**, in manufacture order: kicker → sorts (§6.1) →
   worn sort (§6.2) → tissue (§6.7) → counters → breath (§6.8), per the
   D6.14 timeline.
8. **Section elements.** Ornaments (§6.9), specimen pin (§6.5), cards
   (§6.15), press-harder (§6.10) — in that order, because each borrows
   the previous one's machinery.
9. **The slip.** Form, leader-line focus states, client validation,
   proof-mark system, server re-render path (§6.16, §E, §F voice).
10. **Platen transition** (§6.12) — last of the motion work: it depends
    on routing, on every destination state existing, and on the
    interruption rules.
11. **Reduced-motion pass.** Implement and verify every element's
    variant as a set (light locked 40°, no pin/breath/lift/drift,
    counters printed) — not element by element from memory.
12. **Breakpoint pass.** Verify D-section breakpoint rows at 1280, 1024,
    834, 390 and 360px — including the chase's two-row turn, the strip
    specimen, the full-bleed slip.
13. **Performance pass.** Measure against §I; if over, cut in §I's order
    and record the cuts in the project's progress notes.
14. **Final gate.** §10's checklist, plus a spot-check of five state
    matrices from Part II chosen at random — if any sampled state is
    undesigned in the build, the build returns to the step that owns it.

---

*End of Part II — Theme 004 (Letterpress Atelier) deepened to the 50x
standard (v2): every element carries its choreography timeline, state
matrix, breakpoint behaviour, edge cases, accessibility spec and token
list; the theme carries its component inventory, copywriting voice,
three further worked examples, scroll choreography map, performance
budget and build order. Standing rules reminder, restated for Part II:
normal system cursor only; no reveal may ever hide content permanently;
`prefers-reduced-motion` honoured per element; every element merges with
the content it carries.*
