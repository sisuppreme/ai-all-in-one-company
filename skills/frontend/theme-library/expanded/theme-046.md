# 46. Amber Hour — Expanded (v1 + v2)

> Expansion of theme #46 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same ten signature elements —
> deepened, never redesigned — plus eight page-family elements.

## 1. Concept & world

Forty-one million years ago a bee blundered into resin, and the resin
did the one thing resin does: it kept her. Not her likeness — *her*,
wing veins, pollen load and all, in a medium that admits light but
refuses time. This theme builds a website out of that substance.
Everything on the page is **suspended in amber**: content lives inside
translucent resin blocks, and light does not fall *on* the page — it
passes *through* it, from one source, travelling as the visitor reads.
A product is a specimen. A section is a block. The background panels
are the same resin at a larger pour, with seeds and bubbles caught in
them mid-drift. The page is not decorated with amber; it is *made* of
it, and the making is the interface.

The world is the **cabinet**: a dealer's or a museum's dark case of
drawers, opened for one visitor. Its vocabulary is complete. The
**blocks** are the poured pieces that hold every piece of content,
each with its shell of amber and its plate of checked resin tone
carrying the text. The **strata** are the cabinet's five depths, from
the Surface stratum at the page's head to Dusk at its foot; every
section declares the stratum it sits in, and the light cools from
pale gold to deep amber as it descends through them. The
**inclusions** are the small caught things — seeds, bubbles, a fibre
of bark — drifting almost imperceptibly inside the panels, plus the
bubbles a visitor traps with their own clicks (§6.10). **The light**
is singular and accounted for (§6.3): one position, one temperature,
read by every glow on the page. And the **catalogue record** (§6.17)
is the dealer's book, in which every age the site prints is a row a
visitor can audit. Nothing on the page glows for decoration and no
number is atmosphere. Brightness is physics and ages are bookkeeping.

**The theme's one law: one light, and every age a fact.** Every
brightness on the page is the one light, at its declared position and
temperature, passing through resin: a block's glow is a computed
falloff from the light's centre (§5), the sun-disc (§6.6) is that same
light drawn in profile from the same variables, the letter-glow
(§6.2) is that light travelling along the headline it has just lit.
A glow that appears where the light is not — a halo pasted behind a
button, a card with its own private shine — is a lamp the page
invented, and the gate (§10) fails it on sight. And every age
printed anywhere — a card's label, a figure band's total, the hero's
apparatus — is the artefact's catalogued age, full digits, traceable
to a row in the record (§6.17). A build that rounds "41,000,000" to
"millions of years old" for punch, or lights a corner the light never
reached, has not bent the theme: it has switched on a lamp in a
cabinet that holds one, and written fiction on a dealer's label.

**Looking is the interaction model.** The visitor's acts are a
collector's acts at a cabinet: they watch the light kindle behind
the first specimen (§6.1) and travel along its name (§6.2); they
carry the lamp down the page simply by reading (§6.3); they turn the
featured specimen in its block while its story scrolls past (§6.4);
they lean a block toward the light and watch the glow refract
(§6.9); they trap a bubble in a block they touched, leaving a mark
the resin keeps (§6.10); and when they ask for a specimen, their
enquiry is sealed into the record itself (§6.14, §6.17). The site
does not have users consuming a feed; it has a visitor alone with a
cabinet after hours, and the cabinet's whole behaviour says: these
things waited forty-one million years; they can wait for you to look
properly. That is why the theme fits content whose value *is*
provenance and patience — catalogued specimens, aged goods, deep-time
stories — and why it curdles around anything instant, disposable or
loud.

**Best-fit sites and audiences.**

- Amber, fossil and mineral dealers with real catalogued stock: the
  theme *is* the stock's condition — held, lit, recorded — and the
  catalogue record (§6.17) is the dealer's actual book made public.
- Natural-history museums and their shops: the collection's
  presentation and its commerce in one substance; the natural-history
  section's drawn wing (§6.7) is the museum's teaching voice.
- Heritage science publishing: deep-time features, fossil stories,
  collection essays — long reads the light travels down at reading
  pace (§6.3), with ages that are facts, not colour.
- Aged and single-origin goods with genuine records: vintage dealers,
  archive reissues, cellared goods — anything whose price is partly
  a verified count of years, kept in the dark.
- A collector's cabinet made public: one person's holdings,
  catalogued and lit; the theme's intimacy (one visitor, one lamp)
  is the point.

**When NOT to use it.**

- For stock with no provenance. If the catalogue cannot state each
  piece's age and origin as a fact, §1's law cannot be kept — the
  ages become fiction and the theme cannot be used.
- For urgent, transactional flows. The light takes 2000ms to kindle
  and the theme is proud of it; a flash sale or a checkout that must
  complete in one impatient minute should not ask its visitors to
  wait for resin to warm.
- For content that must be scanned at speed. Dashboards, news
  indexes, documentation: the cabinet rewards looking, stratum by
  stratum, and punishes skimming with darkness. A page that must be
  searched at a glance needs daylight, not amber.
- Where a light scheme is mandatory. The cabinet is dark by physics
  — amber is examined against darkness or not at all (§2's ruling).
  A brand system that requires a white ground will unpick the
  theme's spine.
- For object-less products. Pure software with nothing that can be
  photographed, held or aged: blocks without specimens are empty
  resin, and the theme becomes a colour scheme with a mythology
  (§9, item 2).

## 2. Palette

Five anchors, inherited unchanged. The palette is a descent: one
near-black resin the cabinet is built from, two ambers for the
substance itself, and two lights — the honey the light is made of
and the pale gold it starts as — plus the cream that was caught in
the resin before any of us arrived and now serves as the text colour.
Nothing else is admitted; every other colour on the page is one of
these five, tinted, shaded, or set at an opacity over its own ground.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--resin` | `#2A1608` | Dark resin: the cabinet ground, text plates inside blocks at the deep strata, the page's body | ~44% of pixels | Cream on it **14.24:1** (AAA) — the page's workhorse pairing. Gold on it **10.26:1**; honey on it **6.46:1** (headings and apparatus). This is the tone the safety rule means by "contrast-checked resin". |
| `--amber` | `#8A4B12` | Deep amber: the resin substance itself — block shells, the sun-disc at dusk, strata hairlines at depth | ~20% of pixels | Cream on it **5.60:1** (AA — body ≥16px only, and only where a shell must carry a caption directly). Gold on it **4.04:1** — apparatus ≥14px bold only, never body. Resin text on it is 2.54:1 and refused. |
| `--honey` | `#D98E32` | Honey light: the light's body — glow gradients, the venation ink, warm edges, the disc mid-descent | ~7% of pixels | Resin text on it **6.46:1** — the one warm ground that may carry text (chips, the disc's label). Cream on it is 2.20:1 and refused; honey is a light, not a paper. On `--amber-face` it is 3.46:1 — graphical only. |
| `--gold` | `#F2C063` | Pale gold: the light at the surface — ignition's first colour, letter-glow peaks, focus rings, apparatus on resin | ~4% of pixels | On resin **10.26:1** (AAA). On `--amber-face` **5.49:1**. On honey 1.59:1 — refused; gold never letters a lit ground. |
| `--cream` | `#F7E8C9` | Inclusion cream: all primary text on resin tones, specimen names, the record's prose | ~3% of pixels (text) | On resin 14.24:1, on `--resin-deep` **15.6:1**, on `--amber-face` **7.62:1** (AAA), on deep amber 5.60:1. Cream is the only text colour admitted on amber-family grounds. |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--resin-deep` | `#1B0E04` | Dark resin mixed 35% toward black: the surround outside the cabinet column, the footer ground, the 404's room. Cream on it **15.6:1** — the most legible ground on the page; the deepest place is the clearest, which is the cabinet's courtesy. |
| `--amber-face` | `#6E3A0E` | Deep amber mixed 25% toward dark resin: the text plates inside blocks at the Surface and Honey strata, where a plate warmer than resin is wanted. Cream on it **7.62:1** (AAA); gold **5.49:1**; cream-dim **5.34:1**. |
| `--cream-dim` | `#DCC19B` | Inclusion cream mixed 25% toward deep amber: secondary text, captions and record apparatus on resin grounds — **9.98:1** on resin, **5.34:1** on `--amber-face`. On deep amber it falls under 4:1 and is refused there; amber shells take secondary text in full cream at 85%. |
| `--honey-pale` | `#F4D08C` | Pale gold mixed 40% toward inclusion cream: the glow's mid-tone, halo shoulders, inclusion fills. Graphical only — never text, never an indicator's sole carrier. |
| `--glow` | computed | Not a hex: the light layer's colour, mixed per frame between `--gold` (temperature 0) and `--amber` (temperature 1) by §6.3. Any build that hard-codes a glow colour has invented a second light. |

**The strata tones (the palette's grammar).** A block's plate tone is
a property of its stratum, not a choice: Surface and Honey strata
blocks carry text on `--amber-face` plates; Amber and Deep strata
blocks on `--resin` plates; the Dusk stratum (footer, the record's
foot) on `--resin-deep`. Shells are deep amber at every stratum —
the substance does not change with depth; the light reaching it
does, and §6.3's temperature variable performs that change so no
builder hand-tints a "darker section" (§9, item 1).

**Dark-mode behaviour: the cabinet does not invert, and it does not
offer a light scheme.** Amber is examined in a dark room or not at
all — a "light mode" for this theme would be a photograph of the
cabinet with the case lights on, which is to say a picture of the
theme's absence. Under `prefers-color-scheme: dark`, the only
change is the surround: `--resin-deep` extends to the page's outer
margins (the room darkens around the cabinet). Under
`prefers-color-scheme: light`, nothing changes at all. A build that
inverts cream text onto honey grounds, or lifts the cabinet onto a
white page for daytime, has not themed the site — it has opened the
cabinet in a car park.

**Pairing law.** Text is cream on resin, resin-deep or amber-face
plates; secondary text is cream-dim on those same plates only;
apparatus on resin grounds may be gold (10.26:1) or honey (6.46:1);
resin text is admitted on honey grounds only (6.46:1); gold never
letters amber or honey; cream never letters honey; no text of any
colour sits on the glow layer, on a shell gradient, or on a drift
field. Any other pairing is a build error, not a variation.

## 3. Typography

Two typefaces, inherited unchanged. **Fraunces** is the specimen
voice — a serif with the warmth and slight irregularity of a
hand-lettered cabinet label — and sets display, specimen names,
section titles and prices, with optical sizing on (`opsz` axis:
display text is drawn at its large-size cut, never a scaled text
cut). **Source Serif 4** is the record voice and sets body text,
captions, ages, counters and all prose: the dealer's book is kept in
a book hand. Data (ages, catalogue numbers, counts) is set in Source
Serif 4 with `font-variant-numeric: tabular-nums` — the figures must
stand in columns like entries, and a counting age (§6.8) must not
widen its label as the millions arrive. There is no third typeface.
Emphasis inside Fraunces is weight (560→640); emphasis inside Source
Serif is weight (400→600), never italic-for-emphasis — the record
does not lean; italics are reserved for Latin binomials and titles of
works, as a naturalist writes them.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display / hero headline | Fraunces 640, opsz 144 | 44–76px / 1.06, `clamp(2.75rem, 6.5vw, 4.75rem)` | −0.01em | The specimen's name at cabinet scale; never more than 3 lines; the only letters on the site that may glow (§6.2). Sentence case — a label, not a shout. |
| Section title (stratum piece) | Fraunces 600, opsz 72 | 30–44px / 1.12, `clamp(1.875rem, 4vw, 2.75rem)` | 0 | The piece named as the dealer names it: the thing, then its age in the apparatus beneath — never the age inside the title. |
| Specimen / product name | Fraunces 600 | 20–26px / 1.2 | 0 | Name only; its age rides beneath in apparatus (§3 law 1), never inside the name. |
| Heading (in-block) | Fraunces 600 | 22–28px / 1.18 | 0 | One per block region; a heading is printed on one plate and never crosses a shell boundary. |
| Body | Source Serif 4 400 | 16.5–18px / 1.62–1.74 by stratum (law 4) | 0 | Measure 54–62ch. On amber-face plates 17px minimum — the 7.62:1 pairing earns AAA at size. |
| Caption / record | Source Serif 4 400 | 14–15px / 1.55 | 0 | The record's voice (§6.17): what the piece is, where it was caught, its age, its number. |
| Apparatus (ages, catalogue nos., strata) | Source Serif 4 600 | 11–13px, uppercase | +0.16em | "41,000,000 YEARS", "CAT. No. 46-001", "STRATUM III — AMBER". Uppercase is rationed to apparatus only. |
| Price | Fraunces 640 | 26–34px / 1.05 | 0 | Lettered on the specimen's own plate; a price is part of the label, never floated on a badge or a ribbon. |
| The record line | Source Serif 4 500 | 15–17px / 1.6 | 0 | Confirmations, the catalogue's totals, the 404's sentence — the theme's honesty set in the record voice, sentence case, unhurried. |

**Type laws.**

1. **The age is a figure, not an adjective.** Every age is printed
   in full digits with thousands separators, tabular, followed by
   "years": "41,000,000 years". "Millions of years old", "≈40M
   years", "ancient beyond measure" are banned from labels and
   apparatus (§12) — the catalogue's number is the claim, and
   rounding it is a small fraud the gate audits (§10, gate 2).
2. **Type is lit, never glowing.** Only the hero headline's letters
   glow, once, in sequence (§6.2). Every other letter on the page
   sits on an opaque resin-tone plate at its locked contrast (§2),
   invariant at every light position — the glow passes *behind*
   plates and *around* shells, never under text.
3. **Display is a label, not a banner.** Sentence case, no
   all-caps display, no display italic. Uppercase exists only in
   apparatus at ≤13px. A headline that shouts has mistaken the
   cabinet for a fairground.
4. **Leading loosens with depth.** Body line-height by stratum:
   Surface 1.62, Honey 1.65, Amber 1.68, Deep 1.71, Dusk 1.74.
   Light travels slower in deep resin; so does the eye, and the
   type admits it.
5. **One headline per block.** A block holding two display lines is
   two specimens poured into one piece — a catalogue error, fixed
   in the survey (§15, step 1), never by shrinking type.

## 4. Layout language

**The page is a cabinet, and content lives in blocks.** The outer
surround is `--resin-deep` — the dark of the room. Inside it, the
cabinet column (max 1240px including the rail) stands on `--resin`.
Every content unit is a **block**: a poured piece of amber with a
shell and a plate. The shell is deep amber, 10–14px of visible
substance on every side, carrying the block's inner glow (§6.3) and
its inclusions (§6.5, §6.10). The plate is the opaque resin-tone
inset (§2's strata tones) that carries the text. Text never sits on
a shell, a gradient or the glow layer — that is the layout form of
§3 law 2, and it is why the page stays readable at every light
position.

**Poured geometry.** Blocks are not machined rectangles. Each block
takes one of four declared radius recipes — asymmetric, like a pour
that set as it cooled:

| Recipe | `border-radius` | Temperament |
|---|---|---|
| 1 — the settler | `28px 36px 30px 40px / 36px 30px 40px 28px` | Hero and feature blocks; the calmest pour |
| 2 — the leaner | `36px 24px 38px 28px / 28px 38px 26px 36px` | Cards and the empty block (§6.18) |
| 3 — the deep pour | `24px 32px 26px 34px / 32px 26px 34px 24px` | Record and figures blocks; the squarest, for ledgers |
| 4 — the thin pour | `32px 28px 34px 26px / 26px 34px 28px 32px` | Form and shallow blocks |

Recipes rotate by catalogue order from the survey (§15, step 1);
two adjacent blocks never share a recipe, and a block keeps its
recipe at every breakpoint — a pour does not re-pour on a phone.
The plate inside follows the shell's radius minus the shell
thickness, so plate and shell read as one piece at every size.

**The strata.** The page descends through five declared strata —
**I Surface, II Honey, III Amber, IV Deep, V Dusk** — each a band of
sections with its own apparatus label in the rail and its plate
tone per §2. A stratum boundary is a hairline in honey at 35% with
the stratum's name and depth lettered at the rail: depths are
declared in the survey as "metres of resin" (I 0m, II 18m, III 41m,
IV 67m, V 90m) and are the same numbers the sun-disc's bands (§6.6)
and the navigation (§6.11) print — one cabinet, one set of depths,
three printings (§10, gate 3's cousin). Sections never straddle a
boundary; a section too long for its stratum is two sections.

**The margin is the cabinet rail.** On ≥1200px, the left 96px of
the cabinet is the rail: it holds the sun-disc's track (§6.6), the
strata labels (§6.11) and depth ticks. Instruments only — no prose,
no imagery, no advertising may sit on the rail. Content begins after
the rail in a column of max 1060px. Below 1200px the rail folds
away and its instruments relocate per §6.6/§6.11's breakpoint rules.

**The light layer.** One fixed, full-viewport layer sits between
the cabinet ground and the blocks: the light itself (§6.3),
`pointer-events: none`, `aria-hidden`, a radial gradient in
`--glow` blurred 60px, centred on `--lx/--ly`. Blocks additionally
carry an inner-glow pseudo-element *inside the shell*, above the
shell's amber and below the plate, driven by the per-block
`--glow-i` the loop computes from the same light position. Two
renderings, one light: the audit (§10, gate 1) samples both against
the declared falloff, and any third glow anywhere is a second lamp.

**Density law.** Density falls as the page descends, because the
visitor's attention is being spent on older and older things. The
Surface stratum holds the hero block and nothing else in its first
viewport. Card strata may run three-across — specimens for sale are
allowed to be plentiful. The pinned specimen (§6.4) is alone in its
stratum for its whole passage. The record (§6.17) is one wide block,
unaccompanied. The footer holds the record's totals and the dusk
apparatus, nothing else. A footer as busy as the card grid has hung
a shop sign over the ledger.

**Cabinet air.** Blocks are separated by at least 64px of resin
ground at ≥1200px (40px below) — the dark between blocks is a
material, the cabinet's air, and it is what lets each block be read
as a separate pour. Blocks never overlap, never share an edge, and
never sit on a coloured section background: there are no section
backgrounds in a cabinet, only deeper and shallower resin.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-kindle` | `cubic-bezier(.22,.61,.21,1)` | Light catching: quick to start, long to peak — a flame finding its size | Ignition (§6.1), letter glow (§6.2), block kindling, form warm (§6.14), light-pass (§6.15) |
| `--ease-settle` | `cubic-bezier(.25,.8,.3,1)` | Matter settling in resin: a fall that thickens as it lands | Inclusion settle (§6.1/§6.5), age counters (§6.8), card images (§6.13), bubble appearance (§6.10) |
| `--ease-turn` | `cubic-bezier(.45,.02,.25,1)` | The heavy turn: slow to move, slower to stop — mass in a thick medium | Specimen rotation smoothing (§6.4), tilt release (§6.9) |
| `--ease-rise` | `cubic-bezier(.3,.65,.25,1)` | The bubble's rise: buoyant at first, decelerating as it nears the top and lodges | Bubble trap (§6.10), confirmation bubble (§6.14) |
| `--ease-draw` | `cubic-bezier(.4,0,.2,1)` | The pen's draw: steady pull, firm stop | Wing venation (§6.7), strata rules, record head rule (§6.17), focus rules (§6.14) |

**The one-light model (the theme's master clock).** The page has
exactly one light, described by three values the shared loop owns:
`--lx` and `--ly`, its centre in viewport coordinates, and
`--light-temp`, its temperature 0 (pale gold, surface) → 1 (deep
amber, dusk). The light's target is a lamp carried at reading
height: `ly` targets 42% of the viewport height in document
coordinates, `lx` targets the reading column's centre. Its
temperature is a pure function of document progress,
`temp = scrollY / (docHeight − viewportHeight)`, so dusk always
lands at the footer by construction. Every glow on the page is a
declared function of these three values. A block's inner-glow
intensity is `I = clamp(1 − d / 720, 0, 1)`, where `d` is the
distance in px from the light's centre to the block's centre; its
glow colour is `--glow` mixed at that intensity. There is no other
brightness in the theme. An element that wants to be brighter must
wait for the light to arrive — or be the light's own instrument
(§6.6).

**Every motion term, translated into the cabinet's language:**

- **Scroll-triggered reveals** are kindlings: a block entering the
  viewport catches the light — its shell edge glows first (300ms
  `--ease-kindle`), then its face warms as `--glow-i` rises (600ms),
  groups staggering 90ms by DOM order. Nothing fades up out of
  nowhere; on this page things are *lit*, and lighting has a source.
- **Scroll scrub** is the light's travel (§6.3), the specimen's
  turn (§6.4) and the disc's sinking (§6.6) — pure functions of
  scroll position, driven by the shared loop, reversible to the
  pixel.
- **Parallax** is resin depth, and it is rationed to one family:
  the inclusions inside background panels lag at 0.96× (§6.5).
  Panels, blocks and plates all travel at 1.0× — the cabinet is not
  deep; only the caught matter is suspended, and only it lags.
- **Pinned scenes:** exactly one — the featured specimen (§6.4). A
  cabinet has one piece under examination at a time; pinning a
  second is refused.
- **Masked reveals** are the vignette of the light itself: a
  section's emergence is masked by a soft radial vignette whose
  clear centre is the light's position and whose falloff is the
  one-light function — the mask is not a rectangle wipe, it is the
  light arriving unevenly, as light does.
- **Blur-to-sharp is refused for content.** A fossil does not swim
  into focus; it is lit or it is not yet lit. Blur exists in exactly
  one place: inside the glow layer, where a blurred radial *is* the
  light's body. Text and images never blur at any frame.
- **Kinetic typography** is refused except the glowing letter
  sequence (§6.2): one headline, once, colour and shadow only — no
  letter moves. Type does not perform; it is illuminated.
- **Counters** are the age counters (§6.8): catalogued ages counting
  up in tabular serif when their specimen is lit, every figure
  obeying the one law.
- **Progress** is the sun-disc (§6.6): a disc sinking through the
  strata, dimming as it goes. There is no progress bar and there
  are no percentages anywhere in the theme — an age is counted, a
  reading is a descent, neither is a proportion.
- **Marquee is refused.** Nothing in a cabinet hurries sideways
  forever. The record (§6.17) is a still ledger; the strata are
  still bands; the only endless motion is the inclusions' drift,
  which is not a loop of content but of substance.
- **Ambient loops:** exactly one system — inclusion drift (§6.5).
  The light itself never breathes or pulses; a pulsing lamp is a
  faulty lamp, and this cabinet's lamp is kept. A second ambient
  system anywhere is a gate failure.
- **Micro-interactions:** the refracting tilt (§6.9), the bubble
  trap (§6.10), the seal press (§6.14). Every interaction is an act
  of handling: turning a block, trapping air, sealing an enquiry.
- **Hover physics:** tilt with refraction (§6.9) and a slow
  magnetic drift of at most 3px — a block leans in its resin
  toward a near hand, with the lag of a thing suspended in syrup.
  Nothing snaps, springs or overshoots; resin has no bounce.
- **Page transitions** are a light-pass (§6.15): the one light
  brightens and sweeps down as the page changes, so leaving and
  arriving happen inside the same cabinet.
- **Smooth scrolling:** honeyed inertia. The shared loop lerps the
  light's position at `--lerp-light` 0.09 — the lamp trails a fast
  scroll and catches up after it stops, as a carried light does —
  and scrubbed values at 0.12. Native scroll is never hijacked: the
  theme smooths its light, not the visitor's hand.
- **The shared loop law.** One `requestAnimationFrame` loop owns
  every scrubbed value (light position and temperature, specimen
  rotation, disc position, drift phase, tilt). It writes only
  transform, opacity and custom properties, updates per-block glow
  only for blocks within 900px of the light, and stops writing a
  value when it settles within 0.1% of target.

**Watchdog law.** Every ceremony has a timer: ignition settles by
2400ms (§6.1), the letter pass by its cap (§6.2), the venation by
2200ms (§6.7), counters by 2000ms (§6.8), a bubble's rise by 2800ms
(§6.10). The DOM ships *lit and complete* — blocks kindled, ages
printed, veins inked, the specimen at its resting angle — and every
pre-state exists only under a JS-armed root class applied after
first paint confirms the loop is alive. No-JS is not a degraded
mode: it is the cabinet with its lamp already on.

## 6. Signature elements

### 6.1 Backlight ignition

- **What & why.** On load, the cabinet's one light kindles behind
  the hero headline over 2000ms — a warm radial source brightening
  through the resin, the headline's block warming from within. It
  belongs because it is the page's power arriving honestly: before
  the ignition there is no light to borrow, and every later glow on
  the page refers back to this one source being lit. The hero is a
  specimen lit through its block, exactly as a dealer lifts a lamp
  behind a piece for a visitor — the ceremony is not an intro
  animation in front of the hero; it is the hero becoming visible
  the way amber is always made visible.
- **Structure.** The fixed `.light` layer (§4) positioned behind the
  hero block for the ignition's duration, plus the hero block's own
  inner-glow pseudo-element (§4). The hero ships lit at full rest
  intensity — headline, standfirst and action readable from first
  paint — and JS arms the unlit pre-state (glow at 12%, light scale
  0.82) only after first paint confirms the loop is alive. The
  hero's inclusion field (§6.5's grammar, 6 inclusions in the
  shell's corners) ships at its rest offsets.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 700ms timer — the light must not wait for a slow
  font to catch. t=0: glow opacity 0.12→1 and scale 0.82→1 over
  2000ms `--ease-kindle`; the hero block's `--glow-i` ramps on the
  same curve to its surveyed rest value. From t=1200ms the hero
  inclusions drift 3–6px to their rest offsets over 1200ms
  `--ease-settle` — matter settling as the resin warms. At t=2000
  the light hands over to §6.3's scroll model without a seam: the
  ignition's final `--lx/--ly` are the scroll model's initial
  values. It runs once per session; a returning visitor finds the
  cabinet already lit.
- **States.** Unlit (JS-armed pre-state only) → kindling → lit and
  handed to §6.3. Scrolled-past during the ceremony: the ceremony
  completes instantly — a visitor who leaves mid-kindling returns
  to a lit cabinet, not a paused sunrise.
- **Content merge.** The light is behind the hero's own block: the
  headline is lit *through* the substance it is suspended in.
  Remove the animation and the hero loses nothing but the lighting
  being switched on; keep it, and every glow afterwards has a
  birthday.
- **Failure fallback.** Watchdog: if the glow has not reached rest
  by 2400ms after the trigger, it is set to rest instantly —
  classes removed, values final. No JS: the hero stands lit at
  first paint. If fonts fail, the 700ms race starts the ignition in
  a fallback face; the hero block's fixed min-height absorbs
  letterfit shift.
- **Reduced-motion variant.** No ignition. The light stands at its
  rest position and temperature from first paint, and a single
  apparatus line beneath the standfirst records what the ceremony
  would have shown: "BACKLIT — ONE LIGHT FOR THE WHOLE CABINET."
  The information is kept; only the kindling rests.
- **Performance budget & mobile variant.** One composited radial
  layer (transform + opacity) and one custom property on the hero
  block; no images, no canvas. Mobile (<768px): blur 40px instead
  of 60px, scale range 0.88→1, duration 1600ms, inclusion settle
  cut to 4 inclusions — a phone's cabinet is smaller and its lamp
  catches faster, admitted rather than faked.
- **Choreography timeline (v2).** t=0 fonts ready (or 700ms race
  lost) → t=0–2000 glow kindles on `--ease-kindle`, hero `--glow-i`
  ramping with it → t=1200–2400 hero inclusions settle to rest
  offsets → t=2000 light hands to §6.3 (position/temperature
  continuous) → t=2000 §6.2's letter pass begins → t=2400 watchdog
  deadline passes unneeded.
- **State matrix (v2).** *Rest:* lit, light under §6.3's control.
  *Hover:* none — the ignition is not a control; the hero's action
  inside it hovers per §11. *Focus:* focus entering the hero during
  the ceremony completes it instantly (a keyboard visitor is never
  asked to wait for a lamp). *Active:* n/a. *Scrolled-past:*
  completed instantly, lit. *Disabled / no-JS:* lit at first paint.
  *Touch:* identical; the first touch completes the ceremony like a
  click.
- **Breakpoints (v2).** ≥1200px: full timeline, blur 60px.
  768–1199px: blur 48px, inclusions 5. <768px: duration 1600ms,
  blur 40px, inclusions 4, glow radius 70vw.
- **Edge cases & failure modes (v2).** *Slow network / fonts late:*
  the 700ms race governs; the kindling never waits past it. *Tab
  hidden mid-ignition:* rAF pauses; on return, if elapsed wall
  time exceeds 2400ms the watchdog rests the light — the visitor
  never resumes a half-lit hero. *Session return:*
  `sessionStorage` marks the ignition done; the hero paints lit.
  *Hero block resized by a late image:* the light's centre is the
  block's centre measured per frame by §6.3's model, never a
  hard-coded pixel.
- **Accessibility spec (v2).** The light layer is `aria-hidden` and
  visual only; the headline is the page's `<h1>` from first paint
  and never leaves the accessibility tree. Contrast is invariant
  through the ceremony because the headline sits on its opaque
  amber-face plate (7.62:1) — the glow brightens the shell around
  the plate, never the ground under the letters.
- **Tokens consumed (v2).** `--gold`, `--amber`, `--glow`, `--lx`,
  `--ly`, `--ease-kindle`, `--ease-settle`, `--dur-ignite`
  (2000ms), `--dur-fallback-ignite` (2400ms), `--glow-i`.

### 6.2 The glowing letter sequence

- **What & why.** Once the backlight is lit, warmth passes along
  the hero headline's letters from first to last — 80ms per letter,
  each letter's colour lifting cream→gold with a honey text-shadow
  at its peak, then subsiding to a rested warmth. It belongs
  because it is the light *reading the specimen's name aloud*: the
  same light that kindled behind the block now travels along the
  label, the way a lamp carried past a cabinet case brightens each
  letter of a label in turn. It is the theme's only kinetic
  typography (§5), rationed to one headline, once, for exactly this
  reason.
- **Structure.** The headline ships whole, as one `<h1>` with its
  full text in the accessibility tree. JS clones it into per-letter
  spans (`aria-hidden="true"` on the visual clone, the original
  text retained for AT via the heading's accessible name) only
  when the pass is armed. Each span transitions `color` and
  `text-shadow`; only the active letter and its immediate
  neighbours carry a shadow at any frame (a three-letter window),
  bounding paint cost.
- **Motion spec.** Trigger: §6.1's completion (t=2000), or
  immediately if the ignition completed instantly. Per letter: glow
  envelope 480ms `--ease-kindle` — colour rises 160ms to `--gold`,
  holds 80ms with `text-shadow: 0 0 18px` honey at 55%, falls
  240ms to the rested state (cream with a permanent 8% gold warmth
  mixed in — the letters keep a little of the light that read
  them). Stagger: 80ms per letter, compressed for long headlines
  to `min(80ms, 1600ms / letterCount)` so the pass always completes
  within 2080ms of travel. Cap: headlines longer than 28 letters
  glow only the first line's letters (measured after layout); the
  remaining letters warm together in one 600ms fade at the pass's
  end.
- **States.** Whole and unlit (rest, no-JS) → passing → rested warm.
  The pass runs once per session and never replays — scrolling
  away and back does not re-read the name; a lamp does not re-read
  a label it has already passed.
- **Content merge.** The letters are the headline itself; nothing
  is overlaid, substituted or re-typeset. Remove the pass and the
  title stands complete; keep it, and the title has been *read by
  the light* — the theme's thesis performed at label scale.
- **Failure fallback.** Watchdog: if the pass has not completed by
  ignition-end + 3200ms, all letters are set to the rested state
  instantly. If the split fails (a headline containing markup the
  splitter refuses), the whole headline warms in one 600ms fade
  instead — the fallback is a dimmer version of the same event,
  never an error.
- **Reduced-motion variant.** No pass. The headline stands at its
  rested warmth from first paint; §6.1's reduced-motion record
  line ("BACKLIT — ONE LIGHT FOR THE WHOLE CABINET.") covers the
  information the pass would have given.
- **Performance budget & mobile variant.** ≤28 spans, one
  text-shadow in a three-letter window; no layout properties
  touched. Mobile (<768px): cap 20 letters, shadow blur 12px,
  envelope 420ms — the label is smaller and the light crosses it
  faster.
- **Choreography timeline (v2).** t=0 (ignition complete) → first
  letter rises t=0–160, holds to 240, falls to 480 → letter *n*
  starts at n × stagger → last capped letter ends ≤ t=2080+480 →
  uncapped remainder (if any) warms t=2080–2680 → rested; watchdog
  deadline t=3200.
- **State matrix (v2).** *Rest:* rested warmth, whole headline.
  *Hover:* none — the headline is not a control. *Focus:* focus
  entering the hero completes the pass instantly (§6.1's rule).
  *Active:* n/a. *Scrolled-past:* completed instantly to rested.
  *Disabled / no-JS:* whole headline at rested colour from first
  paint (the rested warmth is the CSS default; the unlit state is
  JS-armed only). *Touch:* identical; first touch completes.
- **Breakpoints (v2).** ≥1200px: cap 28 letters, shadow 18px.
  768–1199px: cap 24, shadow 15px. <768px: cap 20, shadow 12px,
  envelope 420ms.
- **Edge cases & failure modes (v2).** *Headline edited longer
  after build:* the cap and compression rules are computed at run
  time from the actual letter count and line measurement — the
  pass cannot overrun its budget because a copywriter added a
  word. *RTL languages:* the pass follows DOM order, which is
  reading order; in an RTL headline it travels right to left
  without a code path of its own. *Font swap mid-pass:* spans
  inherit the swapped face; the envelope is colour-only, so a swap
  costs nothing but a redraw.
- **Accessibility spec (v2).** The visual spans are
  `aria-hidden="true"`; the heading's accessible name is the full
  headline text, present from first paint — screen readers receive
  the name once, whole, and never meet the pass. At peak glow a
  letter is gold on the amber-face plate (5.49:1) and at rest
  cream (7.62:1); the glow never takes a letter below AA at any
  frame.
- **Tokens consumed (v2).** `--cream`, `--gold`, `--honey`,
  `--ease-kindle`, `--dur-letter` (80ms), `--dur-letter-glow`
  (480ms), `--dur-fallback-letters` (3200ms).

### 6.3 The scroll light source

- **What & why.** The one light travels with the reading. Its
  centre targets a lamp's height — 42% of the viewport — and lags
  behind scroll at lerp 0.09, so pools of light move through the
  strata as the visitor reads, arriving a breath after each new
  section does, the way a carried lamp swings gently as its bearer
  walks. Its temperature cools from pale gold to deep amber across
  the page's whole descent, so the light at the footer is the light
  at dusk. It belongs because it is the theme's physics made
  navigable: illumination is not a per-section effect but a single
  substance the whole page shares, and the visitor steers it simply
  by reading.
- **Structure.** The fixed `.light` layer (§4) plus per-block
  inner-glow pseudo-elements, all reading three custom properties
  the shared loop writes on `:root`: `--lx`, `--ly` (light centre,
  viewport px) and `--light-temp` (0–1). For each block within
  900px of the light, the loop additionally writes that block's
  `--glow-i` from §5's falloff law, `I = clamp(1 − d / 720, 0, 1)`,
  `d` = distance from the light's centre to the block's centre.
  Blocks beyond 900px hold `--glow-i: 0` and are not written.
- **Motion spec.** Continuous. Targets per frame: `ly` = scrollY +
  0.42 × viewport height; `lx` = the reading column's centre x.
  Position lerps at 0.09 — after a scroll stop the light settles
  within 1% of target in ≈800ms. Temperature is scrubbed, not
  lerped: `temp = scrollY / (docHeight − viewportHeight)`, written
  directly (the descent of the day does not lag; only the lamp's
  swing does). Peak layer opacity falls with temperature, 1.0 →
  0.55, and `--glow` mixes gold→amber on the same value. At the
  hero, §6.1's ignition hands its final values to this model with
  no seam.
- **States.** Travelling (scroll active or light unsettled) →
  settled at target (scroll idle, light within 0.1%) → dusk
  (temp = 1, at the footer; the light rests at its deepest and the
  disc §6.6 has set). Scrolling up reverses position and
  temperature exactly — the lamp is carried back up the cabinet
  and the day runs backward, which is correct: temperature is a
  position, not a memory.
- **Content merge.** The light is the medium the content is
  suspended in; sections brighten because the light reaches them,
  not because they animate. The layer is `pointer-events: none`
  and sits beneath every plate, so no text ever sits on the glow
  (§2's pairing law) and contrast is invariant at every light
  position — the merge is physical, not decorative.
- **Failure fallback.** No JS or a dead loop: `--lx/--ly` default
  to the hero position and `--light-temp` to 0.3 in CSS — the
  cabinet stands lit by a fixed lamp, fully readable, every block
  at its surveyed rest `--glow-i`. A loop-stall watchdog (no frame
  for 1200ms) simply stops writing; the values freeze at plausible
  light, because frozen light is still light.
- **Reduced-motion variant.** The light is fixed: position at 38%
  viewport height, temperature fixed at 0.35, per-block `--glow-i`
  at surveyed static values. The page reads as a cabinet under one
  steady lamp; nothing travels, nothing dims.
- **Performance budget & mobile variant.** One composited layer +
  ≤6 blocks' custom properties per frame; writes stop per value at
  settle. Mobile (<768px): falloff radius 520px, ≤4 blocks updated
  per frame, `lx` locked to 50vw — a phone's lamp hangs centred
  over a narrower cabinet.
- **Choreography timeline (v2).** Continuous; the beat structure
  is per scroll gesture: gesture starts → light target jumps →
  light lerps (63% of the distance in ≈10 frames, 99% in ≈48) →
  blocks enter the 720px falloff and kindle (§5) as the light's
  pool reaches them → gesture ends → light settles ≈800ms later →
  loop idles.
- **State matrix (v2).** *Rest:* settled at target. *Hover:* n/a —
  the light does not answer the pointer; it answers reading.
  *Focus:* a focus jump (anchor, keyboard) retargets the light
  instantly to the focused section's centre — a keyboard visitor
  is never left in the dark waiting for the lamp to arrive.
  *Active:* n/a. *Scrolled-past:* n/a (continuous). *Disabled /
  no-JS:* fixed lamp per the fallback. *Touch:* identical;
  fling-scrolls simply give the lamp further to travel.
- **Breakpoints (v2).** ≥1200px: falloff 720px, ≤6 blocks/frame.
  768–1199px: falloff 600px, ≤5 blocks. <768px: falloff 520px,
  ≤4 blocks, `lx` locked.
- **Edge cases & failure modes (v2).** *Very long pages:*
  temperature is progress-based, so dusk lands at the footer by
  construction at any length. *Short pages (<150vh):* the
  temperature range compresses; the footer is still dusk.
  *Resize / rotate:* targets recompute from live measurements;
  the lerp absorbs the jump — the lamp swings to the new geometry
  instead of teleporting. *Anchor teleport to the footer:* the
  light lerps to dusk in ≈800ms and the disc (§6.6) with it — an
  honest quick sunset, not a glitch.
- **Accessibility spec (v2).** The layer is `aria-hidden`; no
  information is carried by glow alone — position in the page is
  also given by the strata navigation's `aria-current` (§6.11) and
  the disc's status text (§6.6). Focus visibility is a gold ring
  on the plate (§11), independent of the light's position, so a
  keyboard visitor's focus never depends on where the lamp is.
- **Tokens consumed (v2).** `--lx`, `--ly`, `--light-temp`,
  `--glow`, `--gold`, `--amber`, `--lerp-light` (0.09), `--glow-i`.

### 6.4 Specimen rotation

- **What & why.** The featured specimen pins inside its block and
  rotates slowly — 0° to 18° across the pin — while its story
  scrolls past beside it. It belongs because it is how a specimen
  is actually examined: turned in the hand, at reading speed,
  while the catalogue entry is read. The rotation is scrubbed to
  the visitor's own scroll, so the turn happens at exactly the
  pace they read the story — the object and its account are one
  gesture, and the block is a hand, not a carousel. Eighteen
  degrees is the whole turn: a fossil is not spun; it is tipped to
  the light.
- **Structure.** A pin region of 340vh: a 100vh sticky stage
  holding the specimen's block, and 240vh of travel. The block
  carries the specimen's photograph (or its drawn plate) in its
  shell window; the story column — three beats of prose with their
  apparatus lines — scrolls in the column beside the stage at
  ≥1200px. The pin itself is CSS `position: sticky`; JS owns only
  the rotation value. The DOM ships with the specimen at 9° — the
  mid-turn pose — and its story in normal flow beneath.
- **Motion spec.** Progress `q` = the pin region's traversal,
  0→1, computed per frame from rects. Rotation = 18° × q,
  smoothed by the shared loop at lerp 0.12 (rotation is a
  scrubbed value, §5). The block's `--glow-i` is boosted ×1.25
  during the pin — the specimen is under examination, and the
  light attends what is being examined (the boost is a declared
  multiplier on §5's falloff, audited like everything else, not a
  private glow). Rotation completes at q=0.9 and holds 18° for the
  final tenth, so the story's last beat is read with the specimen
  already at rest — the turn finishes before the telling does.
- **States.** Before the pin: in flow at 0° (JS-armed; 9° without
  JS). Pinned and turning: q 0→0.9. Held: q 0.9→1 at 18°.
  Released: scrolls away at 18°. Scrolled back: the whole sequence
  reverses exactly — scrub is a pure function, and a visitor who
  re-reads the story turns the specimen back in their hand.
- **Content merge.** The specimen is the product and the story is
  its catalogue entry at full length — provenance, the catching,
  the keeping. Neither exists as decoration for the other: remove
  the pin and the page loses the examination, not a flourish.
- **Failure fallback.** No JS: no pin (sticky is not armed), the
  specimen stands at 9° above its complete story in normal flow.
  Loop dead mid-pin: rotation freezes at its current angle; the
  sticky stage still releases at the region's end, so the story
  can never be trapped behind a stuck fossil — the turn is the
  only thing a dead loop can cost.
- **Reduced-motion variant.** No pin, no rotation: the specimen at
  9° above its story, exactly the no-JS composition. The mid-turn
  pose is chosen deliberately — it is the angle at which the
  worked example's wing (§8.2) catches the light, so the still
  page keeps the examination's best frame.
- **Performance budget & mobile variant.** One transformed layer;
  `will-change` held only while the pin is engaged. Mobile
  (<768px): the pin is cut — specimen static at 9°, story below,
  in flow. 768–1199px: pin kept, travel 180vh, rotation 0→14° —
  a smaller hand turns a smaller arc.
- **Choreography timeline (v2).** q=0 pin engages, specimen at 0°
  → q=0.25 story beat one read, specimen at 4.5° → q=0.55 beat
  two, 9.9° (in the worked example the venation §6.7 draws on
  this beat) → q=0.85 beat three, 15.3° → q=0.9 rotation complete
  at 18° → q=1.0 pin releases, specimen scrolls away at rest.
- **State matrix (v2).** *Rest:* pre-pin, 0° (or 9° no-JS).
  *Hover:* none — the pinned specimen is behind the cabinet's
  glass in spirit: §6.9's tilt is refused here, stated so no
  builder adds it. *Focus:* the story's links and the buy block
  after the pin are focusable in DOM order; the specimen block
  itself is not interactive. *Active:* n/a. *Scrolled-past:*
  rests at 18° in flow. *Disabled / no-JS:* 9°, in flow.
  *Touch:* identical scrub — the turn answers the thumb's scroll,
  never a drag on the specimen itself.
- **Breakpoints (v2).** ≥1200px: 240vh travel, 18°, story beside.
  768–1199px: 180vh, 14°, story beside at narrower measure.
  <768px: pin cut, static 9°, story below.
- **Edge cases & failure modes (v2).** *Story longer than the
  travel:* the survey (§15, step 1) sets travel ≥ story height ×
  1.2, 240vh by default, minimum 160vh — a pin that ends before
  its story is a build error caught in the survey, not in the
  browser. *Story shorter:* travel shrinks to the minimum; the
  specimen never turns in empty space. *Zoom:* sticky and rects
  recompute; q is always measured, never assumed. *Print:* the
  specimen prints at 9° with its full story — the print
  stylesheet takes the reduced composition.
- **Accessibility spec (v2).** Rotation is decorative; the
  photograph's alt carries the specimen's name and catalogue
  number. The story is ordinary flow text in DOM order — no
  content exists only mid-pin, and the sticky stage never
  reorders the reading. The block is not focusable and carries no
  interaction a keyboard visitor could miss.
- **Tokens consumed (v2).** `--ease-turn`, `--glow-i`,
  `--dur-pin` (240vh), `--resin`, `--amber`.

### 6.5 Inclusion drift

- **What & why.** Inside the background panels — the page's large,
  quiet pours between blocks — seeds, bubbles and a fibre of bark
  drift 4–10px on loops of 20–40 seconds, and lag the scroll at
  0.96×. It belongs because the panels are the same substance as
  the blocks, and the substance has things caught in it: matter
  suspended mid-motion since before the visitor arrived, still
  settling. The drift is the theme's one ambient system (§5), and
  its slowness is the point — at 20–40s a cycle, it is perceived
  the way a real inclusion field is: not watched, but *noticed*,
  once, with a small start — the panel was alive.
- **Structure.** Each panel carries a drift field of inline SVG
  inclusions — seed silhouettes, bubble circles with a 1px cream
  rim at 40%, bark fibres — positioned in % coordinates declared
  in the survey (§15, step 1), in two nested groups: a near group
  at full amplitude and a far group at ×0.55 amplitude with
  reversed phase, giving the field a depth the panel's flatness
  would otherwise deny. Fields live only in a panel's surveyed
  empty zones, with ≥24px clearance from any text plate. The SVG
  ships at surveyed rest positions.
- **Motion spec.** Per inclusion: offset = A × sin(2πt/T + φ),
  applied on both axes with a 90° phase difference between x and y
  (a slow ellipse, never a line), A 4–10px, T 20–40s, φ from the
  survey seed — every field's choreography is declared, not
  randomised at runtime. Parallax: the field translates
  (1 − 0.96) × the panel's scroll delta, clamped so no inclusion
  can exit its panel. All values come from the shared loop's
  clock; CSS animations are refused for the field — one clock,
  one pause behaviour, one throttle (§14).
- **States.** Drifting (panel on screen) → paused (panel
  off-screen via observer, or tab hidden — the loop stops writing
  the field) → at rest (reduced motion or no-JS: the surveyed rest
  positions, where the field still reads as suspended — a field
  at rest is a photograph of the same truth).
- **Content merge.** The inclusions are the collection's small
  specimens, and the panels say so: each field carries a caption
  in apparatus — "FIELD 3 — SEEDS, UNNUMBERED" — so the drift is
  catalogued content at background scale, not wallpaper. The
  panels' prose (where a panel carries prose) is written about
  the stratum the field illustrates.
- **Failure fallback.** No JS: the field stands at its surveyed
  rest positions, captioned, complete. Loop dead mid-drift: the
  field freezes wherever it is — every position within its
  amplitude is a plausible fossil position, so a frozen field is
  indistinguishable from a resting one.
- **Reduced-motion variant.** The field at surveyed rest
  positions, no parallax. The caption remains; the information
  (these panels hold caught matter) is fully kept.
- **Performance budget & mobile variant.** ≤14 inclusions per
  panel, ≤42 per page, transforms only, ≤0.4ms/frame for the whole
  system. Mobile (<768px): ≤8 per panel, amplitudes ×0.7, the far
  group cut — a small panel holds a smaller field.
- **Choreography timeline (v2).** Continuous, phase-locked to the
  page clock rather than to entry: a panel scrolled into view is
  already mid-drift (the resin was drifting before the visitor
  arrived). On first paint the field sits at its t=0 phase, which
  the survey sets equal to the rest positions, so arming the drift
  never makes an inclusion jump.
- **State matrix (v2).** *Rest:* surveyed positions (reduced /
  no-JS). *Hover:* none — fields are not interactive; the
  interactive inclusions live in blocks (§6.10), and confusing
  the two is a build error. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* keeps drifting while any part of the panel is
  visible; pauses only fully off-screen. *Disabled:* rest
  positions. *Touch:* identical; drift does not answer touch.
- **Breakpoints (v2).** ≥1200px: full fields, both groups.
  768–1199px: far-group amplitudes ×0.8. <768px: ≤8 per panel,
  amplitudes ×0.7, far group cut.
- **Edge cases & failure modes (v2).** *Panel taller than the
  viewport:* parallax clamp keeps inclusions inside the panel at
  every scroll position — the clamp is computed from the panel's
  padding box in the survey. *Low-power device:* the loop updates
  the field every 3rd frame; at 20–40s periods, 20fps drift is
  indistinguishable from 60fps. *Panel with no empty zone:* the
  survey gives it no field — a crowded panel is prose, and prose
  panels are bare resin (§9, item 7's cousin).
- **Accessibility spec (v2).** Fields are `aria-hidden`; the
  caption is real text and carries everything the field means.
  Inclusions never overlap text (≥24px surveyed clearance), never
  flash (sinusoids at these periods cannot), and pause under
  reduced motion per the variant.
- **Tokens consumed (v2).** `--ease-settle` (arming settle),
  `--honey`, `--gold`, `--cream` (inclusion fills at surveyed
  opacities).

### 6.6 The sun-disc progress

- **What & why.** In the rail, a 34px sun-disc sinks through the
  five strata bands as the page is read, dimming from pale gold to
  deep amber; at the footer it rests in the Dusk band, spent.
  Progress as the day ending inside the resin. It belongs because
  it is §6.3's light drawn in profile: the same temperature
  variable, the same descent, so the instrument and the
  illumination can never disagree — a visitor who watches the
  disc knows where the lamp is, and a builder cannot fake one
  without the other (§10, gate 1 audits them together).
- **Structure.** The rail (§4) carries five bands — hairline ticks
  with apparatus labels ("I — SURFACE · 0 M" … "V — DUSK · 90 M",
  depths from the survey, identical to §6.11's) — and the disc: a
  `div` with a radial gradient (`--glow` at core, transparent at
  rim), positioned by transform along the rail's track. The disc
  is `aria-hidden`; a visually-hidden status in the rail carries
  its reading as text.
- **Motion spec.** Disc position = railTop + p × (trackHeight −
  34), p = document progress — the same p as §6.3's temperature,
  lerped at 0.12 so the disc trails the reading by a breath. Disc
  colour = `--glow` mixed on `--light-temp`; its glow halo fades
  1.0 → 0.25 as temp → 1 (a setting sun throws less light). When
  the disc crosses a stratum boundary (p = 0.2 / 0.4 / 0.6 / 0.8,
  with 0.5% hysteresis against flicker), the entered band's label
  warms over 300ms `--ease-kindle`.
- **States.** At surface (p=0, gold, full halo) → sinking →
  crossed into each stratum (label warms) → at dusk (p=1, deep
  amber, halo spent, resting in band V). Scrolling up raises and
  re-gilds it exactly — the disc is a position, not an
  achievement, and it never pretends a reading was kept.
- **Content merge.** The disc is the page's own light, profiled in
  the margin: gauge and illumination are one fact printed twice.
  Its bands are the strata the sections actually sit in (§4), so
  the gauge also serves as the page's table of depths — the
  instrument is the index (§6.11 shares the rail).
- **Failure fallback.** No JS: the disc rests at the Surface band
  and the rail works as the strata index (§6.11) — nothing claims
  a position it cannot measure. Loop dead: the disc freezes at
  its last true position; a frozen gauge beside live text is
  honest in a way a hidden one is not.
- **Reduced-motion variant.** The disc steps discretely between
  bands at section boundaries — no smooth sink, no halo — and its
  temperature steps with it. Position is still truthful; only the
  travel rests.
- **Performance budget & mobile variant.** One element, transform
  + one custom property per frame. Mobile (<768px): the rail is
  cut; the disc rides the sticky header at 22px, still scrubbed,
  with the five strata as a segmented hairline beneath the header
  (§6.11's mobile form). 768–1199px: rail narrows to 64px, disc
  28px, band names move to the header strip.
- **Choreography timeline (v2).** Continuous with scroll: p
  changes → disc lerps (≈63% in 10 frames) → boundary crossing at
  p thresholds → entered label warms 300ms → status text updates
  (band changes only) → at p=1 the disc settles into band V and
  its halo reaches 0.25.
- **State matrix (v2).** *Rest:* at the true p. *Hover:* the disc
  is not a control; the rail's labels are links (§6.11) with
  their own states. *Focus:* labels focusable; the disc never
  takes focus. *Active:* n/a. *Scrolled-past:* n/a (continuous).
  *Disabled / no-JS:* Surface rest, index mode. *Touch:*
  identical scrub.
- **Breakpoints (v2).** ≥1200px: 34px disc, full bands.
  768–1199px: 28px, names relocated. <768px: 22px header disc +
  segmented hairline.
- **Edge cases & failure modes (v2).** *Short page (<150vh):* p
  still spans the document — dusk at the footer by construction.
  *Anchor jump to the footer:* the disc lerps down in ≈800ms,
  temperature with it — a quick sunset for a teleporting reader,
  honest and visible. *Boundary hover:* the 0.5% hysteresis
  prevents label flicker when a reader parks exactly on a
  boundary.
- **Accessibility spec (v2).** Disc `aria-hidden`. The rail's
  visually-hidden status — "Stratum III of V — Amber" — updates
  on band changes only (never per frame), `role="status"`,
  polite. Position is redundantly carried by §6.11's
  `aria-current`. No meaning is carried by the disc's colour
  alone: band names are text.
- **Tokens consumed (v2).** `--gold`, `--amber`, `--honey`,
  `--glow`, `--light-temp`, `--ease-kindle`.

### 6.7 Wing venation draw

- **What & why.** In the natural-history section, a bee's wing
  venation SVG draws itself — midrib first, then the primary
  veins in branching order, then the cross-veins — over 1800ms.
  It belongs because the drawing is itself one of the collection's
  specimens: the pinned bee (§6.4) is too small to teach its own
  wing, so the cabinet keeps the wing's diagram at ×40, and the
  diagram *forms* under the reader's eye in the order a
  naturalist would ink it — structure before detail, always. The
  draw order is the lesson: a visitor who watches it once knows
  how a wing is built.
- **Structure.** An inline SVG on a resin plate inside the
  section's block: 22 paths in four groups — the wing outline (1,
  pre-drawn at 18% honey: the wing's ghost is present before its
  veins, as a specimen card is present before it is inked), the
  midrib (1), the primaries (6), the cross-veins (14). Draw via
  `stroke-dashoffset` with `pathLength="1"` normalisation on
  every path, so durations are declared per group, not per path
  length. The plate carries the specimen caption in apparatus:
  "WING OF THE BALTIC BEE — VENATION AT ×40 — CAT. No. 46-001/B".
  The DOM ships fully inked.
- **Motion spec.** Trigger: the plate crosses 55% of the
  viewport. Midrib: t=0–500 `--ease-draw`. Primaries: from
  t=380, stagger 90ms, 420ms each, in branching order (each vein
  starts only after its parent segment exists — the stagger is
  the branching, timed). Cross-veins: from t=950, stagger 45ms,
  260ms each. Complete at t=1800. Draws once per session;
  scrolling back does not un-draw it — ink is ink.
- **States.** Ghost (outline at 18%, JS-armed only) → drawing →
  inked (veins honey at 85%, outline at 30%). No-JS: inked from
  first paint.
- **Content merge.** The section's prose names the veins in draw
  order — reading order *is* draw order — so the text and the
  drawing are one explanation at two speeds. The diagram is
  labelled, numbered and captioned like every specimen; it is not
  an illustration dropped into an article.
- **Failure fallback.** Watchdog: if the draw has not completed
  by 2200ms after the trigger, all paths are set inked instantly.
  The SVG is inline — no network, no font, no canvas can fail it.
- **Reduced-motion variant.** Inked at rest, no draw. A record
  line beneath the plate keeps the information the draw carried:
  "THE VEINS ARE DRAWN IN BRANCHING ORDER — MIDRIB, PRIMARIES,
  CROSS-VEINS."
- **Performance budget & mobile variant.** 22 paths, dashoffset
  only, ≤0.2ms/frame during the draw. Mobile (<768px):
  cross-veins cut to 8 (the plate is smaller; the survey declares
  which 8 — the ones the prose names first), total draw 1400ms.
- **Choreography timeline (v2).** t=0 trigger → 0–500 midrib →
  380–1250 primaries land in branching order → 950–1760
  cross-veins stitch the cells → 1800 inked, caption's apparatus
  warms once (300ms `--ease-kindle`) → watchdog deadline 2200
  passes unneeded.
- **State matrix (v2).** *Rest:* inked. *Hover:* the plate warms
  — vein opacity 85%→100% over 300ms, the diagram under a warmer
  light. *Focus:* the plate is a figure, not a control;
  focus-within of the section's first link warms it identically,
  so keyboard visitors get the same lamp. *Active:* n/a.
  *Scrolled-past:* inked. *Disabled / no-JS:* inked. *Touch:*
  tap does not trigger or replay; the draw answers scroll
  position only.
- **Breakpoints (v2).** ≥1200px: plate 520px wide, 14
  cross-veins. 768–1199px: 420px, 14 cross-veins. <768px: full
  column width, 8 cross-veins, 1400ms.
- **Edge cases & failure modes (v2).** *Anchor jump past the
  section:* the draw completes instantly (jump-scroll catch-up,
  §13) — a teleported reader finds the wing inked, not ghosted.
  *Tab hidden mid-draw:* rAF pauses; on return, if wall time
  since trigger exceeds 2200ms the watchdog inks it — the visitor
  never resumes a half-veined wing. *Section re-entered:* inked;
  the draw is a making, and makings are not repeated for an
  audience of one returning reader.
- **Accessibility spec (v2).** The SVG is `role="img"` with an
  `aria-label` describing the wing and its draw order ("Wing of
  the Baltic bee at forty times life size; the veins are drawn
  midrib first, then the primaries in branching order, then the
  cross-veins"). Every fact the diagram shows is also in the
  prose — the draw is never the only carrier of anything.
- **Tokens consumed (v2).** `--honey`, `--gold`, `--ease-draw`,
  `--ease-kindle`, `--dur-venation` (1800ms),
  `--dur-fallback-draw` (2200ms).

### 6.8 Age counters

- **What & why.** When a collection item is lit, its age counts
  up to its catalogued figure — "41,000,000 years" — in tabular
  serif, the digits arriving over 1600ms. It belongs because the
  numbers are the artefacts' own labels and their scale is the
  content's whole claim: a count that takes its time lets the
  visitor *feel* the zeros arrive — thousands, then millions —
  in a way a printed figure, however large, cannot make the body
  register. The count is a small ceremony of scale, performed by
  the label itself.
- **Structure.** A `<span class="age">` in the item's apparatus
  line, carrying `data-age="41000000"` and — printed in the DOM —
  the final string itself, "41,000,000 years". The printed string
  is the truth; JS may replace the text during the count but must
  restore the exact printed string at the end, character for
  character. The suffix " years" sits outside the counting span
  and never moves; only digits count.
- **Motion spec.** Trigger: the item crosses 40% of the viewport
  (having kindled, §5). Count 0 → age over 1600ms on
  `--ease-settle`'s curve — fast through the thousands, dwelling
  in the millions, which is the felt shape of deep time.
  Formatting at every frame via `toLocaleString('en-GB')`;
  tabular numerals throughout, so the label's width is locked to
  the printed string's width before the count starts (JS measures
  and fixes the box — a counting label never pushes its
  neighbours). Counts once per item per session.
- **States.** Printed (rest, no-JS) → counting → printed
  (identical string). Scrolled past quickly: the count completes
  instantly to the printed string — a flung scroll is owed the
  truth, not a ticker.
- **Content merge.** The counter is the item's own label, in the
  order §3 law 1 fixes: name, then age, then prose. There is no
  separate stats band inventing numbers; §6.16's figures render
  from the same catalogue object and obey the same rule.
- **Failure fallback.** Watchdog: by 2000ms after the trigger the
  printed string stands, whatever the counter's state. If
  `toLocaleString` is unavailable, the feature-check fails first
  and the printed string is never replaced — the count is an
  enhancement the label can decline.
- **Reduced-motion variant.** The printed string only; no count.
  The age loses its ceremony and keeps its fact.
- **Performance budget & mobile variant.** Text writes ≤1 per
  frame per counter, ≤3 counters concurrent; no layout properties
  (width pre-locked). Mobile (<768px): duration 1200ms, trigger
  at 30% — a smaller cabinet counts a little faster.
- **Choreography timeline (v2).** t=0 item crosses 40% (its
  block mid-kindle) → width locked → t=0–1600 digits climb on the
  settle curve, commas formatting live → t=1600 exact printed
  string restored, counting class removed → watchdog deadline
  t=2000 passes unneeded.
- **State matrix (v2).** *Rest:* printed. *Hover:* n/a — a label
  is not a control. *Focus:* n/a. *Active:* n/a. *Scrolled-past:*
  printed. *Disabled / no-JS:* printed from first paint. *Touch:*
  identical; the count answers viewport position, not touch.
- **Breakpoints (v2).** ≥1200px: 1600ms, trigger 40%.
  768–1199px: 1400ms, trigger 35%. <768px: 1200ms, trigger 30%.
- **Edge cases & failure modes (v2).** *Young inclusions:* a
  90,000-year seed counts the same way; the format never rounds
  to "0.1 million" — ages under 1000 print as-is ("412 years").
  *Re-entry:* no recount (session set) — an age does not get
  younger for being looked at twice, and the ceremony is not a
  toy. *Age absent from the catalogue:* the label prints "AGE
  UNRECORDED" and no count is armed — an estimate dressed as a
  figure is §1's fraud in miniature.
- **Accessibility spec (v2).** During the count the counting span
  is `aria-hidden`, with a visually-hidden static copy of the
  final string beside it — screen readers hear the true age once,
  whole, never a ticker of intermediate numbers. The final string
  is ordinary text in the apparatus line, in reading order.
- **Tokens consumed (v2).** `--ease-settle`, `--dur-count`
  (1600ms), `--dur-fallback-count` (2000ms).

### 6.9 Refracting tilt

- **What & why.** A resin block under the hand tilts — at most
  4° — and its inner glow shifts *opposite* the tilt, refracting
  as light does through a turning block. It belongs because
  handling is the cabinet's verb: a visitor who leans a block
  toward the light moves the light inside it, and the product's
  material answers, not just its frame. The refraction is the
  tell that the block is a substance and not a card: surfaces
  slide; volumes bend light.
- **Structure.** The block's parent carries `perspective: 900px`.
  The loop tracks the pointer once, globally; an engaged block
  reads the pointer's position over its own rect and writes its
  own `rotateX/rotateY` plus `--glow-x`/`--glow-y` — the inner
  glow's anchor inside the shell — as custom properties. Text
  plates are children of the block and tilt rigidly with it: the
  letters are *in* the resin and never skew, shear or re-flow.
- **Motion spec.** Targets: `ry = 4° × (px − 0.5) × 2`,
  `rx = −4° × (py − 0.5) × 2`, clamped ±4°. The loop lerps
  toward the target at 0.14 while engaged — 63% of the tilt in
  ≈250ms, settled ≈700ms — the lag of a heavy thing in a thick
  medium. The glow anchor shifts opposite: `--glow-x` moves
  −14px × (ry / 4°), one frame behind the tilt, because
  refraction trails the turn. Release: 900ms `--ease-turn` back
  to flat. Magnetic drift: when the pointer passes within 64px
  of the block's edge, the block translates ≤3px toward it at
  lerp 0.06 — a suspended pull, felt as weight, never a snap.
- **States.** Rest flat → engaged (hover or focus-within) →
  releasing → rest. On touch there is no tilt — a tap belongs to
  §6.10. Focus-within tilts to a fixed pose (2°, −2°) with the
  glow anchored accordingly, so a keyboard visitor receives the
  same refraction a pointer visitor does. Press (active): the
  tilt flattens to 1° over 150ms — the block is being handled,
  pressed into the palm.
- **Content merge.** Only blocks tilt, and blocks are the
  content's containers — the specimen, its label, its price tilt
  as one piece of resin. Controls inside keep rectangular hit
  areas in layout; the transform is uniform, so nothing inside
  the block distorts.
- **Failure fallback.** No JS or a dead loop: blocks rest flat
  with their glow at the surveyed rest anchor. No state of the
  tilt hides content — at 4° every word remains on its plate.
- **Reduced-motion variant.** No tilt, no drift. Focus shows
  §11's gold edge-ring instead; the refraction's information
  (this block is in your hand) is carried by the ring.
- **Performance budget & mobile variant.** Transform + two custom
  properties on the one engaged block only; all other blocks are
  untouched per frame. Mobile (<768px): tilt and drift cut
  entirely — blocks rest flat, as they do under touch at any
  size. 768–1199px: tilt ±3°, drift cut.
- **Choreography timeline (v2).** Pointer enters → t≈250 tilt at
  63% of target, glow anchor one frame behind → t≈700 settled at
  target → pointer moves: targets update per frame, glow trails
  → pointer leaves: release 900ms `--ease-turn` → flat; drift
  decays on the same release.
- **State matrix (v2).** *Rest:* flat, rest glow anchor. *Hover:*
  engaged per the spec. *Focus:* fixed 2°/−2° pose on
  focus-within; a focus landing in a form field inside the block
  holds the pose steady (no tracking while typing). *Active:*
  flattened to 1°. *Scrolled-past:* flat — engagement ends when
  the block leaves the pointer, wherever the page goes.
  *Disabled:* a sealed block (the sold specimen's, §6.13) does
  not tilt and does not drift; its apparatus says why. *Touch:*
  flat, always.
- **Breakpoints (v2).** ≥1200px: ±4°, drift on. 768–1199px: ±3°,
  drift off. <768px: cut.
- **Edge cases & failure modes (v2).** *Pointer leaves
  mid-release:* re-engagement starts from the current angle —
  no snap, ever. *Block taller than the viewport:* the tilt
  pivots at the pointer's y (transform-origin follows it,
  clamped 20–80% of the block's height) — a long block tips
  around the hand, not around its centre. *Nested interaction:*
  while a child control is being used (a field focused, a menu
  open), tracking pauses at the fixed pose. *Tilt + pin:* the
  pinned specimen's block (§6.4) is exempt — it is being turned
  by the scroll, and two hands on one fossil is a breakage.
- **Accessibility spec (v2).** Tilt is decorative and never the
  only carrier of state. Interactive children sit ≥16px from
  block edges (§4 clearance), so the ≤10px corner travel at 4°
  never moves a target out from under a settling pointer.
  Focus pose parity is specified above; focus rings (§11) are
  drawn on the plate and tilt with the block, remaining fully
  visible at every angle.
- **Tokens consumed (v2).** `--ease-turn`, `--glow-x`, `--glow-y`,
  `--glow-i`, `--lerp-tilt` (0.14).

### 6.10 Bubble trap click

- **What & why.** Clicking a block traps a bubble in it: a small
  inclusion appears at the click point and rises slowly through
  the block's shell, lodging near its top, where it stays for the
  session. It belongs because it is the visitor's one act of
  *making* in a cabinet of kept things — they add to the fossil
  record, and the resin keeps their mark inside the very content
  they touched. Forty-one million years from now, the conceit
  goes, someone will find the bee, the seed — and this bubble,
  dated to a Tuesday. The click is small; the keeping is the
  theme's whole promise, handed to the visitor.
- **Structure.** Each block carries a bubble layer inside its
  shell (absolute, inset to the shell, `overflow: hidden`,
  `pointer-events: none`): bubbles live in the amber *around* the
  plate, never over it. A click's point is clamped to the shell
  zone — outside the plate, ≥12px from the plate's edge; a click
  landing on the plate is re-seated to the nearest shell point,
  because air is trapped in resin, not in print. Bubble diameter
  cycles 10/13/16px by the block's bubble count — surveyed
  variety, not randomness. Keyboard parity: each block's caption
  carries a real apparatus-styled button, "Trap a bubble", which
  traps at the block's surveyed anchor point (top-left shell).
- **Motion spec.** Appear: scale 0.4→1 at the clamped point,
  200ms `--ease-settle`. Rise: 2400ms `--ease-rise` to the
  shell's inner top −10px, with a horizontal wobble of ±3px in
  two slow sine half-cycles — buoyant, then decelerating, then
  still. No bounce at the lodge: resin does not bounce; the
  bubble decelerates into place and stops. Cap: **6 visitor
  bubbles per block**. The seventh click releases the oldest: it
  rises its last 20px and fades over 600ms as the new bubble
  traps — the resin takes six; the seventh frees the first.
- **States.** Rising → lodged (persists for the session; a
  block's set is DOM state, recounted truthfully wherever it is
  printed). On detail pages the block's caption counts the
  visitor's bubbles in apparatus — "YOUR BUBBLES IN THIS BLOCK:
  3" — a real DOM count, never a stored claim.
- **Content merge.** The bubble is trapped in the block the
  visitor clicked — their reading leaves a physical trace in that
  specimen's resin, beside its label, under the same light. On
  the acquisition form (§6.14) the same physics seals the
  confirmation: the merger of interaction and content is the
  theme's thesis at click scale.
- **Failure fallback.** Without JS, blocks are not controls and
  clicks do nothing — the block's content is complete without a
  single bubble; the trap is an enhancement, never a gate. Loop
  dead mid-rise: the bubble freezes where it is — a bubble
  mid-resin is a plausible fossil — and the next click's 2800ms
  watchdog lodges all frozen bubbles instantly.
- **Reduced-motion variant.** A click places the bubble directly
  at its lodge position — no rise, no wobble; release of the
  oldest is instant. The keeping happens; only the travel rests.
- **Performance budget & mobile variant.** ≤6 bubbles per block,
  transforms + opacity only, ≤0.1ms/frame for the whole system.
  Mobile (<768px): tap is click; rise 1800ms, wobble cut, cap 4
  — smaller blocks hold less air.
- **Choreography timeline (v2).** t=0 click → point clamped to
  shell → t=0–200 bubble appears → t=200–2600 rise with wobble →
  t=2600 lodged; caption count (where printed) updates at lodge
  → if the block was full: oldest releases t=0–600 in parallel →
  watchdog deadline t=2800.
- **State matrix (v2).** *Rest:* the block with its lodged set
  (possibly empty). *Hover:* §6.9's tilt owns hover; the cursor
  stays the normal system cursor — the block does not advertise
  itself with a pointer change (§11's rule for blocks). *Focus:*
  the "Trap a bubble" button focuses per §11 and traps on
  activation. *Active:* press flattens tilt (§6.9); the bubble
  traps on release of the click, not on press — a visitor who
  presses and drags away has not trapped. *Scrolled-past:* the
  set persists. *Disabled:* a sealed block (§6.13's sold piece)
  refuses clicks and disables its trap button, with the reason
  in its apparatus. *Touch:* tap = click, same clamp and rise.
- **Breakpoints (v2).** ≥1200px: rise 2400ms, cap 6.
  768–1199px: rise 2100ms, cap 6. <768px: rise 1800ms, wobble
  cut, cap 4.
- **Edge cases & failure modes (v2).** *Click on a child link or
  button:* no bubble — the click belongs to the control.
  *Rapid clicking:* traps queue at ≥120ms intervals; a click
  during a rise starts its own bubble (rises may overlap — real
  resin takes bubbles in parallel), but the cap and the queue
  bound the total. *Block resized mid-rise:* the lodge target is
  recomputed from the live rect each frame, so a rotating phone
  cannot strand a bubble below its top.
- **Accessibility spec (v2).** The trap button's `aria-label`
  names its block ("Trap a bubble in Block 4 — the Baltic Bee").
  Trapping updates the block's visually-hidden status — "Bubble
  3 of 6 lodged in this block." — `role="status"`, polite,
  throttled to lodge events. Bubbles themselves are
  `aria-hidden`; nothing about them is information a visitor
  needs, which is exactly why they may be play.
- **Tokens consumed (v2).** `--ease-rise`, `--ease-settle`,
  `--dur-bubble` (2400ms), `--gold`, `--cream`.

### Page-family elements

### 6.11 Strata navigation (page family: navigation)

- **What & why.** The cabinet's index: the rail (desktop) or
  header strip (mobile) lists the five strata with their depths
  and the sections in each, and the current stratum is the one
  the light is in. It belongs because a cabinet is navigated by
  depth, not by page furniture: the visitor's position is a
  stratum and a lamp position, and the navigation says both. Nav
  state and illumination are one fact — §6.6's disc rides the
  same rail and crosses the same boundaries.
- **Structure.** A `<nav aria-label="Cabinet strata">` in the
  left rail at ≥1200px: five stratum groups, each with its
  apparatus label ("III — AMBER · 41 M") — depths identical to
  §4's survey values and §6.6's bands — and its section links in
  reading order. The disc's track (§6.6) runs down the rail's
  centre, so index and gauge share one piece of furniture. Links
  are real anchors to section ids; no JS is required to navigate.
- **Motion spec.** When the disc crosses into a stratum, that
  stratum's label warms over 300ms `--ease-kindle` (the same
  event as §6.6's band warming — one event, two printings).
  Hover on a link: its depth tick extends 6px over 200ms
  `--ease-draw`. Navigation jumps run §6.15's light-pass at
  reduced scale (300ms) so a jump down the cabinet is a descent
  of the light, not a teleport — except focus jumps, which are
  instant (§6.3's focus rule: the lamp is already there when a
  keyboard visitor arrives).
- **States.** Current stratum: label in gold, its current
  section's link carries `aria-current="true"`. Strata above the
  light (already read) rest in cream-dim; strata below rest in
  cream at 70% — the rail is lit by the same falloff as
  everything else, computed from `--light-temp`, not hand-set.
- **Content merge.** The nav indexes specimens and strata, not
  pages; on listing and detail pages the same rail indexes that
  page's strata. It is the drawer's label rail, made of the
  cabinet's own materials — apparatus type, honey hairlines,
  resin ground.
- **Failure fallback.** No JS: a static index of working anchor
  links with no current-state claimed — the rail declines to
  assert a position it cannot measure, and loses nothing else.
- **Reduced-motion variant.** Current state steps at band
  crossings; label warmings are instant; jumps are plain anchor
  jumps.
- **Performance budget & mobile variant.** Negligible — a handful
  of class changes at band crossings. Mobile (<768px): the rail
  becomes the sticky header: strata as a five-segment strip
  (names lettered at ≥1200px only; on mobile the current
  stratum's name is printed beside the disc, the rest are ticks)
  with a tap-expanded section list. 768–1199px: rail at 64px,
  section links collapse to stratum names + an in-page index at
  the content head.
- **Choreography timeline (v2).** Band crossing (from §6.6's p
  thresholds) → label warms 0–300 → `aria-current` migrates to
  the entered stratum's first in-view section → status text (§6.6)
  updates once. Hover: tick 0–200. Jump: light-pass 300ms (§6.15).
- **State matrix (v2).** *Rest:* per the light's stratum.
  *Hover:* tick extends. *Focus:* 2px gold outline, offset 3px
  (§11); focus also warms the link's stratum label (keyboard
  visitors see the lamp acknowledge them). *Active:* current per
  above. *Scrolled-past:* strata above the light dim to
  cream-dim — read drawers rest darker. *Disabled:* n/a.
  *Touch:* tap targets are the same links; the strip's expansion
  is a real button with `aria-expanded`.
- **Breakpoints (v2).** ≥1200px: full rail. 768–1199px: 64px
  rail, names only. <768px: header strip + disc (§6.6).
- **Edge cases & failure modes (v2).** *A page with fewer than
  five strata* (a short interior page): unused strata are
  absent from the rail, never greyed — the cabinet labels only
  drawers it has. *A stratum with many sections:* the rail lists
  the first four and a fifth link, "AND 3 MORE IN THE STRATUM",
  anchoring to the in-page index. *Duplicate section names:* the
  survey forbids them — two drawers with one label is a
  cataloguing error.
- **Accessibility spec (v2).** Nav landmark with its label;
  `aria-current` on exactly one link; band-change status per
  §6.6; every target ≥44px tall in the rail (labels are set on
  44px rows — apparatus type is small, its rows are not).
- **Tokens consumed (v2).** `--gold`, `--cream`, `--cream-dim`,
  `--honey`, `--light-temp`, `--ease-draw`, `--ease-kindle`.

### 6.12 The hero composition (page family: hero)

- **What & why.** The first block: the cabinet's finest piece at
  the Surface stratum — the headline as its specimen label, a
  standfirst, the catalogue apparatus line, and the primary
  action, composed so that §6.1's light kindles behind the
  headline and §6.2's pass can read it. It belongs because the
  hero must teach the block grammar the whole page uses — shell,
  plate, label, age — at the largest scale and under the first
  light, so every later block is read fluently.
- **Structure.** One block, radius recipe 1, max 880px, centred
  in a 100vh Surface stratum on the resin ground. On its
  amber-face plate: the `<h1>` (§6.2's headline), the standfirst
  (Source Serif, ≤3 lines), the apparatus line (dealer, city,
  established — §12's form), and the primary action (§11's
  primary button, a real link or button in HTML). A small
  inclusion field (§6.5's grammar, 6 inclusions) lives in the
  shell's corners — the hero block is a pour like any other,
  only finer.
- **Motion spec.** §6.1's ignition (the block's edge-glow is the
  ignition's local part — the hero kindles first among blocks)
  and §6.2's letter pass. The standfirst and action settle —
  opacity and an 8px rise — across t=1600–2000 on
  `--ease-settle`, as the light reaches them: the composition's
  only entrance stagger, and it is the light arriving at the
  label's lower lines, not elements performing. After the
  ceremony the block is a block: §6.9 tilt and §6.10 bubbles
  apply to it as to any other.
- **States.** Ceremony states per §6.1/§6.2 → rest lit, a normal
  block with a famous label.
- **Content merge.** The hero is not a banner above the theme; it
  is the theme's first specimen, and its apparatus line is a
  catalogue entry ("KESTLER & DAUGHTERS — AMBER & INCLUSIONS ·
  GDAŃSK · EST. 1962" in the worked example). A visitor who
  understands the hero understands every block below it.
- **Failure fallback.** No JS: lit, complete, the action working
  from first paint — the ceremony is armed only over a finished
  hero (§5's watchdog law).
- **Reduced-motion variant.** Lit at rest; §6.1's record line
  stands beneath the standfirst; standfirst and action at rest.
- **Performance budget & mobile variant.** The hero is the LCP:
  its headline is text, its field is inline SVG; a photographic
  hero specimen must be preloaded and is the page's single
  priority image (§14). Mobile (<768px): block full-bleed within
  the cabinet's padding, radius recipe scaled ×0.7, field cut to
  the shell's top corners (3 inclusions), headline per §3's
  clamp.
- **Choreography timeline (v2).** t=0 → ignition 0–2000 (§6.1) →
  standfirst/action settle 1600–2000 → letter pass 2000–≤4680
  (§6.2's capped worst case) → hero complete; whole-composition
  watchdog 4800ms.
- **State matrix (v2).** *Rest:* lit block. *Hover:* §6.9 tilt
  applies — the hero is a block. *Focus:* focus entering the
  hero completes both ceremonies instantly (§6.1/§6.2).
  *Active:* the action per §11. *Scrolled-past:* ceremonies
  completed instantly. *Disabled / no-JS:* finished hero.
  *Touch:* first touch completes ceremonies.
- **Breakpoints (v2).** ≥1200px: block 880px, stratum 100vh.
  768–1199px: block 90vw. <768px: full-bleed block, stratum
  auto-height with 96px of cabinet air.
- **Edge cases & failure modes (v2).** *Headline longer than 3
  lines:* §3 law 5 — shorten the copy in the survey; never
  shrink below the clamp minimum and never let the plate grow
  past the stratum. *No-image hero:* the field and the type
  carry it — the survey declares which form the hero takes, and
  a hero with neither specimen nor field is a label without a
  block, refused at the survey.
- **Accessibility spec (v2).** `<h1>` present from first paint;
  the skip link (§11) lands here; headline contrast 7.62:1 on
  its plate at every glow state (plate opaque, §6.1); the
  apparatus line is text, not an image of text.
- **Tokens consumed (v2).** `--resin`, `--amber-face`, `--cream`,
  `--gold`, `--ease-settle`, `--ease-kindle`, `--glow-i`.

### 6.13 Specimen cards (page family: cards / listing)

- **What & why.** The collection made walkable: each card is a
  small resin block holding one specimen — its photograph
  settling in a shell-top window, its name, its age label (§6.8),
  one line of record, and its price or status. It belongs because
  a listing in this theme is not a grid of products but a drawer
  of pours: the same substance as the hero at a smaller size, so
  browsing the collection feels like the cabinet being opened
  drawer by drawer.
- **Structure.** An `<article>` block, radius recipe rotating by
  catalogue order (never two alike adjacent, §4). The shell's top
  window holds the specimen's photograph (the specimen visible
  *through* the resin — the window's edges carry the shell's
  amber at 12% over the image's rim). Below, the plate: name
  (Fraunces), the age output (§6.8), the record line (caption —
  origin, one fact), and the price (Fraunces) or the status in
  apparatus — "IN THE CABINET — NOT FOR SALE", "SOLD — THE BLOCK
  IS SEALED". The name and the window are one link to the detail
  page; the card as a whole is not a click target.
- **Motion spec.** Entry kindle per §5: shell edge glows 300ms
  `--ease-kindle`, face warms 600ms, stagger 90ms by DOM order
  within the drawer. The photograph scale-settles 1.04→1 over
  700ms `--ease-settle` as its card kindles — the specimen
  sinking the last fraction into its pour. The age counts per
  §6.8, starting at the kindle's midpoint. Hover: §6.9 tilt at
  card scale (±3°).
- **States.** Unlit (JS-armed) → kindled → rest. Hover tilt;
  focus-within takes §6.9's fixed pose. Scrolled-past: kindled —
  a lit drawer never un-lights. Sold cards are *sealed*: no
  tilt, no bubble (§6.10 disabled), the status in apparatus; the
  block has left the market and the theme says so in furniture,
  not in a grey wash.
- **Content merge.** The card is the catalogue entry made
  tangible: its age is §6.8's counter, its record line is
  §6.17's row in miniature, its price is lettered on its own
  plate (§3). A card removed from the catalogue object has
  nothing to print — cards render from §6.17's data, never from
  a parallel list.
- **Failure fallback.** No JS: cards lit, ages printed, links
  working. Loop dead: kindle watchdogs (§5) settle every card by
  its stagger deadline + 900ms.
- **Reduced-motion variant.** Cards lit at rest, photograph at
  rest scale, ages printed, tilt off — the drawer stands open
  and still.
- **Performance budget & mobile variant.** Images lazy below the
  fold, ≤38KB at card size, `aspect-ratio` reserved so kindling
  never shifts layout. Mobile (<768px): one column, tilt off,
  stagger 60ms, window crop 16:10 from the same file.
- **Choreography timeline (v2).** Card crosses 30% → edge
  0–300 → face 300–900 → photograph settled by 1000 → age count
  t≈600–2200 (§6.8) → card at rest, a lit drawer.
- **State matrix (v2).** *Rest:* kindled. *Hover:* tilt ±3°.
  *Focus:* fixed pose (§6.9); the name link's ring per §11.
  *Active:* press flatten (§6.9). *Scrolled-past:* kindled.
  *Disabled:* the sealed/sold treatment above. *Touch:* no tilt;
  tap follows the link or traps a bubble on the shell (§6.10's
  clamp keeps taps on the plate from bubbling).
- **Breakpoints (v2).** ≥1200px: 3-across. 768–1199px: 2-across.
  <768px: 1-across, window 16:10.
- **Edge cases & failure modes (v2).** *Specimen without a
  photograph:* the window holds its drawn plate (the §6.7
  grammar — a venation-style line drawing) or a small drift
  field (§6.5) — never a stock "amber texture" gradient (§9,
  item 8). *Long names:* two-line clamp; the plate grows and the
  row's blocks stretch — poured geometry tolerates height
  variance by design, where machined cards would clip. *A drawer
  of one:* a single card takes the row's first position at card
  width, never stretched to fill — the cabinet does not inflate
  a specimen.
- **Accessibility spec (v2).** The name link is ≥44px; the age
  output follows §6.8's AT treatment; sold status is text, never
  colour alone; image alt = specimen name + catalogue number;
  the whole card is not a link, so screen-reader and keyboard
  visitors meet one link per specimen, named by the specimen.
- **Tokens consumed (v2).** `--amber`, `--amber-face`, `--cream`,
  `--gold`, `--ease-settle`, `--ease-kindle`, `--glow-i`.

### 6.14 The acquisition form (page family: forms / conversion)

- **What & why.** "Request this specimen": the conversion is an
  enquiry to the dealer, written on a block — the visitor's name,
  their direction (email), the specimen (pre-set from the card or
  detail page they came from), and a note. It belongs because the
  theme's commerce is a correspondence, not a checkout: unique
  pieces are asked for, by name and number. And its success is
  the theme's own physics — not a toast, not a green tick (green
  does not exist in this cabinet): the form's block warms and a
  bubble is trapped in its shell carrying the enquiry number.
  The visitor's request is *in the resin*, catalogued — and
  §6.17's record appends it as a session row, so the book itself
  acknowledges them.
- **Structure.** A form on a block (radius recipe 4) whose plate
  is `--amber-face`. Fields per §11's inscription lines:
  apparatus label above, 2px rule below, no box. The specimen
  field is a seam list (§11's radio grammar): the specimen
  arrived from, plus up to two of its stratum kin — laid out,
  never hidden in a dropdown. Submit is §11's primary button:
  "SEAL THE ENQUIRY". The block's shell top-left is the surveyed
  lodge point for the confirmation bubble (§6.10's anchor
  grammar).
- **Motion spec.** Field focus: the rule inks gold over 250ms
  `--ease-draw`, a 6px bubble dot travelling the rule's length as
  it inks. Submit press: the button's edge glows 300ms
  `--ease-kindle` (the seal warming). On success: the block's
  `--glow-i` ramps to 1 over 800ms `--ease-kindle`, and the
  confirmation bubble traps at the lodge point — §6.10's rise
  compressed to 1200ms `--ease-rise` — while beside it the
  confirmation line inks in the record voice: "ENQUIRY No.
  46-118 — IN THE BLOCK. THE DEALER REPLIES WITHIN TWO DAYS."
  The number is the server's real response value; in a static
  build it is the record's next number, taken from the catalogue
  object — never invented at the form.
- **States.** Pristine → editing → sealing (submit disabled,
  label "SEALING…") → sealed (the form is replaced by the
  confirmation block content, `role="status"`, the bubble
  lodged) → or failed (everything kept, §12's failure note above
  the form, focus moved to the note). Errors on fields: the rule
  holds its ink, an apparatus note in §12's error voice appears
  beneath the field, nothing the visitor wrote is cleared.
- **Content merge.** The form is a block among blocks, in the
  Dusk-ward end of the page where the record lives; its specimen
  list is the catalogue's own entries; its success is an
  inclusion and a ledger row. A form that could be lifted onto
  any website has failed the merge; this one cannot be — its
  confirmation is a bubble in resin.
- **Failure fallback.** Without JS the form posts natively; the
  server returns a confirmation page whose block prints the
  bubble statically at the lodge point with the same line. A
  failed submit keeps every field, the chosen specimen and the
  visitor's note exactly as left (§10, gate 7).
- **Reduced-motion variant.** Success applies instantly: bubble
  at its lodge, block at rest glow, confirmation line printed.
  The sealing is recorded, not performed.
- **Performance budget & mobile variant.** No libraries;
  validation on blur and submit; the whole element is one block
  and four fields. Mobile (<768px): single column; the
  specimen's mini-card (shown beside the form at ≥1200px) stacks
  above it.
- **Choreography timeline (v2).** Focus → rule inks 0–250, dot
  travels → submit → seal glow 0–300 → server responds →
  success: block warms 0–800, bubble rises 200–1400,
  confirmation line inks at 900 → session row appended in §6.17
  → focus moves to the confirmation (`tabindex="-1"`).
- **State matrix (v2).** *Rest:* pristine, rules at thread
  weight. *Hover:* fields per §11 (rule warms). *Focus:* rule
  inks + dot per the spec; focus never traps a bubble and never
  warms the block. *Active:* submit press per the spec.
  *Scrolled-past:* n/a. *Disabled:* submit disabled only while
  sealing; a specimen that sells while the form is open disables
  its seam line with the reason printed ("SOLD SINCE YOU ARRIVED
  — THE BLOCK IS SEALED") and the visitor's other fields are
  untouched. *Touch:* identical; targets ≥44px.
- **Breakpoints (v2).** ≥1200px: form block 640px beside the
  specimen's mini-card. 768–1199px: stacked, block 560px.
  <768px: full width, seam list stacks.
- **Edge cases & failure modes (v2).** *Direct arrival with no
  specimen:* the seam list starts unchosen — the dealer does not
  presume; the catalogue's first piece is not pre-picked.
  *Double submit:* the disabled state plus a per-session
  idempotency key. *The visitor's own specimen sells mid-edit:*
  per the matrix's disabled row. *Very long notes:* the textarea
  is §11's ruled sheet; it grows by lines and never scrolls
  internally — a long letter is a long sheet.
- **Accessibility spec (v2).** Real `<label>`s; errors linked by
  `aria-describedby` and summarised in the failure note with
  focus moved to it on submit-fail; the confirmation is
  `role="status"` and receives focus on success; the bubble is
  `aria-hidden` — the enquiry number is text, and the text is
  the receipt.
- **Tokens consumed (v2).** `--amber-face`, `--gold`, `--cream`,
  `--cream-dim`, `--ease-draw`, `--ease-kindle`, `--ease-rise`,
  `--glow-i`.

### 6.15 Resin-pour skeleton + light-pass transition (page family: loader / transition)

- **What & why.** Waiting, in this theme, is unpoured resin:
  skeleton blocks are matte deep-amber shapes in the exact
  geometry of the blocks they will become, labelled in apparatus
  — "POURING — THE SPECIMENS". And travel between pages is a
  **light-pass**: the one light brightens and sweeps down the
  viewport as the old page dims into its resin, and the new page
  arrives already lit — movement inside one cabinet, never a
  teleport between worlds. Both belong because they keep the
  theme's physics unbroken at the two moments themes usually
  drop it: loading and leaving.
- **Structure.** Skeleton: block-shaped plates (`--amber` at
  55%, the declared radius recipes, plate insets at `--resin`)
  with the label set in apparatus on the first block. Transition:
  the `.light` layer (§4) plus a full-viewport resin veil
  (`--resin` at variable opacity), orchestrated on same-site link
  clicks as progressive enhancement over ordinary links — the
  links remain links; the pass is a courtesy layered on them.
- **Motion spec.** Skeleton: a slow sheen — the light's gradient
  at 20% — crosses each block once per 2400ms on `--ease-settle`
  (the pour settling); this is the skeleton's only motion and
  the theme's second licensed ambient behaviour, confined to
  skeletons. Blocks resolve individually as their content lands,
  each resolving block kindling per §5. Transition: veil warms
  0→0.35 opacity over 250ms; the light sweeps `--ly` from 20% to
  70% of the viewport over 450ms `--ease-kindle`; navigation
  occurs; the new page fades from the veil over 300ms with its
  light at rest — no ignition replay (§9, item 12).
- **States.** Skeleton → resolving (block by block) → content.
  Transition: idle → passing → arrived. A bfcache restore lands
  in *arrived* directly (see edge cases).
- **Content merge.** The skeleton is shaped like the content —
  same recipes, same plates, same rail — so waiting shows the
  cabinet's joinery rather than a spinner's apology. The
  transition spends the site's one light on the journey, so the
  destination is lit by the same lamp that lit the origin.
- **Failure fallback.** Content slower than 6000ms: the skeleton
  label updates to §12's waiting line — "STILL POURING — THE
  RESIN IS THICK TODAY." — and blocks resolve in whatever order
  data lands; no block waits for a slower sibling. Transition
  failure (navigation error): the veil lifts over 200ms and the
  visitor stays where they were, nothing lost, nothing claimed.
- **Reduced-motion variant.** Skeleton static — no sheen; the
  label carries the state alone. Transitions are instant plain
  navigations.
- **Performance budget & mobile variant.** Skeleton is pure CSS
  shapes — zero assets. The transition intercepts only
  same-origin, unmodified, non-download links (never
  `target="_blank"`, never modifier-clicks). Mobile (<768px):
  the sweep shortens (`--ly` 30%→60%, 350ms) — a smaller cabinet,
  a shorter journey for the lamp.
- **Choreography timeline (v2).** Click → veil 0–250 → sweep
  100–550 → navigation → new page: veil-out 0–300, light at rest
  → complete. Skeleton: label at t=0, sheen cycles 2400ms,
  per-block resolve + kindle on data, waiting line at 6000ms if
  unresolved.
- **State matrix (v2).** *Rest:* n/a (transient element).
  *Hover:* n/a. *Focus:* the pass never moves focus; on arrival
  the new page's `<h1>` receives focus (`tabindex="-1"`) for AT
  continuity, per §6.12's convention. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled:* JS off or reduced motion →
  plain navigation, static skeleton labels in server-rendered
  loading states. *Touch:* identical.
- **Breakpoints (v2).** All sizes: same structure; <768px sweep
  per the mobile variant; the skeleton follows its blocks'
  breakpoints exactly (it *is* the blocks, unpoured).
- **Edge cases & failure modes (v2).** *Back/forward cache:* a
  `pageshow` handler forces the veil to 0 and the light to rest
  — a restored page must never arrive veiled; a 1200ms watchdog
  after `pageshow` repeats the forcing, because a stuck veil is
  a stranded page and stranding is the theme's one unforgivable
  failure. *Slow navigation >3000ms:* the veil holds at 0.35
  with §12's waiting line in its apparatus. *Prefetch:* a
  prefetched page arrives with its light at rest; the pass is
  shortened to the veil-out only.
- **Accessibility spec (v2).** Skeleton regions are `aria-busy`
  with the label as real text; the transition is visual only and
  never announced; arrival focus per the matrix; a veiled page
  is never focusable (the veil is pointer-events-none and the
  navigation is already committed — focus belongs to the
  destination).
- **Tokens consumed (v2).** `--amber`, `--resin`, `--gold`,
  `--ease-kindle`, `--ease-settle`, `--glow`.

### 6.16 Cabinet figures (page family: data)

- **What & why.** The collection's numbers, lettered once, from
  the catalogue object: specimens held (214), the total years in
  the cabinet (the *sum* of the catalogued ages — a real sum,
  "8,412,000,000 YEARS IN THE CABINET"), the oldest piece
  (41,000,000 years), the youngest. It belongs because a dealer's
  arithmetic is a trust instrument: every figure here can be
  recomputed from §6.17's rows by a visitor with patience, and
  the band says so. Figures that cannot survive recomputation do
  not appear — this band is where marketing statistics come to be
  refused.
- **Structure.** A wide, shallow block (radius recipe 3) holding
  three or four figure groups: apparatus label above, the figure
  in Source Serif tabular at 30–40px, a one-line derivation note
  in caption ("SUMMED FROM THE CATALOGUE — EVERY AGE A ROW IN
  THE RECORD"). All groups render from the same data object as
  §6.13's cards and §6.17's rows; the band's apparatus dates the
  count from the object ("COUNTED FROM THE CATALOGUE, NOVEMBER
  2026" — the catalogue's own date, never a typed claim).
- **Motion spec.** When the band kindles (§5), its figures count
  per §6.8's grammar — the total-years figure over 2200ms (it
  has further to go), the others over 1600ms, staggered 120ms
  apart. Labels and derivation notes are static from first
  paint; only digits perform.
- **States.** Printed → counting → printed (identical strings),
  per §6.8. A figure whose source rows change (a specimen sold)
  re-renders from the object on the next page load — the band
  never patches a number by hand.
- **Content merge.** The band is a block in the descent, placed
  between the collection and the record: the visitor reads the
  sums, then meets the ledger they were summed from. Its figures
  are the page's own catalogue at aggregate scale — the same
  fact, coarser grain.
- **Failure fallback.** Printed strings in the DOM; watchdogs
  per §6.8 (2000ms, 2600ms for the total). No JS: the band reads
  as four lettered figures, complete.
- **Reduced-motion variant.** Printed only. The arithmetic loses
  its ceremony and keeps its audit.
- **Performance budget & mobile variant.** One block; ≤4
  concurrent counters. Mobile (<768px): groups in a 2×2 grid;
  the total-years figure takes the full row — billions need
  their width.
- **Choreography timeline (v2).** Band crosses 40% → kindle per
  §5 → counts start staggered at t=300/420/540/660 → all printed
  by t≈2900 (the total last) → watchdog deadlines pass unneeded.
- **State matrix (v2).** As §6.8's, group by group: *Rest:*
  printed. *Hover / focus / active:* n/a — figures are not
  controls. *Scrolled-past:* printed. *Disabled / no-JS:*
  printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 4-across. 768–1199px: 2×2.
  <768px: 2×2 with the total full-row.
- **Edge cases & failure modes (v2).** *A catalogue with one
  specimen:* oldest and youngest are the same piece; the band
  prints both groups with the same figure and the derivation
  note says "A CABINET OF ONE" — honesty at small scale, not a
  hidden group. *Sold pieces:* "held" excludes them; the total
  is the sum of held ages only, and the note's wording ("IN THE
  CABINET") is the scope, printed. *Ages unrecorded:* a specimen
  with "AGE UNRECORDED" (§6.8) is excluded from the sum and the
  note counts it — "SUMMED FROM 213 OF 214 AGES — ONE
  UNRECORDED" — so the total never silently pretends.
- **Accessibility spec (v2).** Per §6.8: counting spans
  `aria-hidden` with visually-hidden final strings; the
  derivation notes are ordinary text. Figures are never the
  only carrier of a claim the prose needs — §6.17's record
  carries them all again, in rows.
- **Tokens consumed (v2).** `--ease-settle`, `--dur-count`
  (1600ms / 2200ms for the total), `--cream`, `--cream-dim`.

### 6.17 The catalogue record (page family: trust / record)

- **What & why.** The provenance ledger, made browsable: a real
  table — catalogue number, specimen, origin, age in years,
  acquired, status — from which every age, count and claim on
  the site traces. It belongs because it is §1's law given an
  address: a visitor who doubts any figure on any card can come
  here and check the row. Dealers who print ages keep books; this
  is the book, and its presence is the theme's whole argument
  about trust — not a badge, a ledger.
- **Structure.** A `<table>` on a wide block (radius recipe 3),
  apparatus headers, rows in catalogue order. Status is text:
  "IN THE CABINET", "SOLD" (with the year), "ON LOAN" (with the
  borrowing institution and the return season). The oldest row
  carries, beneath its age, §12's fixed line — "41,000,000 years
  in the making; ships in 3–5 days." — the record permitting
  itself the deadpan because both halves are verifiably true.
  The table's caption: "The catalogue record — every age on this
  site is a row here."
- **Motion spec.** The head rule draws over 600ms `--ease-draw`
  when the section enters. Rows kindle in catalogue order at
  40ms stagger — opacity only; ledger rows do not perform. On
  §6.14's success, the visitor's enquiry is appended as the
  table's session row, in apparatus: "No. 46-118 — ENQUIRY —
  YOURS — THIS VISIT" — the record takes the visitor in, in the
  same hand as everything else it keeps.
- **States.** Printed (rest) → kindled. The session row exists
  only after a sealed enquiry and only for the session. No other
  dynamics: a ledger does not animate its past.
- **Content merge.** The table *is* the catalogue object made
  visible — §6.13's cards, §6.16's figures and §6.8's ages are
  its other printings, and §10 gate 3 audits all of them against
  it. The record section is placed late in the descent (Deep
  stratum) where a committed visitor digs for it — the theme's
  ethics, filed where ethics are filed.
- **Failure fallback.** A static table without JS — complete,
  every row, every figure. There is no degraded form of a
  ledger.
- **Reduced-motion variant.** Head rule drawn, rows printed, no
  stagger. The session row still appends (it is content, not
  motion).
- **Performance budget & mobile variant.** ≤60 rows per page;
  beyond that, §11's line pagination by stratum ("Further in
  the record"). Mobile (<768px): the table becomes a stacked
  ledger — each row a mini-block with its fields labelled — a
  table squeezed to 360px would be lying about being a table.
- **Choreography timeline (v2).** Section enters → head rule
  0–600 → rows kindle from t=200, 40ms stagger → record at rest
  → (on §6.14 success, whenever it happens) the session row
  appends with a 300ms `--ease-kindle` warm.
- **State matrix (v2).** *Rest:* printed/kindled. *Hover:* a
  row's plate warms over 200ms — the row under the lamp.
  *Focus:* specimen names are links (to detail pages) with §11's
  ring. *Active:* n/a. *Scrolled-past:* printed. *Disabled:*
  n/a. *Touch:* identical; rows are not targets, their links are
  (≥44px).
- **Breakpoints (v2).** ≥1200px: full table. 768–1199px: the
  origin column folds into the specimen cell as a caption.
  <768px: stacked ledger.
- **Edge cases & failure modes (v2).** *Unknown age:* the cell
  prints "AGE UNRECORDED" — never an estimate dressed as a
  figure (§1). *On loan:* institution and return season are
  real data or the row does not ship. *A specimen sold since the
  catalogue was set:* the row's status is the object's, rendered
  at build or request time — a stale "IN THE CABINET" on a sold
  piece is a gate failure (§10, gate 3), not a typo.
- **Accessibility spec (v2).** Real table semantics, `<th
  scope="col">`, the caption as above. The stacked mobile
  variant keeps every field label as text. Row warmth is
  decorative; no status is carried by colour — statuses are
  words.
- **Tokens consumed (v2).** `--ease-draw`, `--ease-kindle`,
  `--cream-dim`, `--amber-face`, `--resin`.

### 6.18 The dark block (page family: 404 / empty state)

- **What & why.** A block with nothing caught in it: an empty
  resin block, unlit except at its edges, one sentence and the
  way back. It belongs because even absence has a specimen state
  in a cabinet — the empty block is catalogued too, as "BLOCK 0
  — NOTHING CAUGHT" — and because a 404 that keeps the theme's
  physics (one block, one lamp at rest, no performance) tells
  the visitor the cabinet is unbroken even where it is empty.
- **Structure.** A centred block (radius recipe 2, 560px) on the
  resin-deep surround, its shell carrying a small drift field at
  rest (§6.5's positions, no drift armed — the field of an empty
  block is still). On its plate: the apparatus line "BLOCK 0 —
  NOTHING CAUGHT", the heading in Fraunces — "Nothing was caught
  in this piece." — one record line of explanation, and two
  links: the cabinet home and the catalogue record (§6.17).
- **Motion spec.** None, by ruling. The empty block does not
  kindle — there is nothing in it to light — and the page's
  light rests above it at temperature 0.5, static (§6.3's model
  with a single block to serve). The stillness is the design: a
  404 that performs has misunderstood the cabinet.
- **States.** Rest only. Links hover and focus per §11.
- **Content merge.** The empty state speaks the theme's language
  truthfully — and the same block serves at section scale for
  the search-empty state ("No specimen in the record matches
  that name." — §12) and the sold-out stratum ("Every piece in
  this stratum has left the cabinet."), so absence has one
  furniture across the site.
- **Failure fallback.** It is the fallback. It must work with no
  JS, no fonts and no images, and it does: text, two links, one
  block.
- **Reduced-motion variant.** Identical — it is already still.
- **Performance budget & mobile variant.** One block; the
  lightest page on the site. Mobile (<768px): block full-width
  within the cabinet's padding.
- **Choreography timeline (v2).** None. The block is at rest
  from first paint and remains so; the absence of a timeline is
  specified here so no builder invents one.
- **State matrix (v2).** *Rest:* the block, still. *Hover /
  focus:* the two links per §11. *Active:* n/a. *Scrolled-past:*
  n/a (the page is one screen where possible). *Disabled:* n/a.
  *Touch:* the links at ≥44px.
- **Breakpoints (v2).** ≥1200px: 560px block, centred.
  768–1199px: 480px. <768px: full column width.
- **Edge cases & failure modes (v2).** *Search-empty variant:*
  the block keeps the visitor's query visible in its record
  line and offers the catalogue link — the visitor is told what
  the record lacks, not blamed for asking (§12's empty voice).
  *A stratum emptied by sales:* the variant line above, plus the
  record link where the sold rows can be seen — absence with its
  paperwork.
- **Accessibility spec (v2).** The heading is the page's `<h1>`;
  the state is conveyed in text, never by the dimness alone;
  links ≥44px with §11's focus ring — on the darkest page of the
  site, focus is at its most visible, which is correct.
- **Tokens consumed (v2).** `--resin-deep`, `--resin`, `--amber`,
  `--cream-dim`, `--gold`.

## 7. Page application map

**Home — the whole cabinet, lit.** Hero composition (§6.12) with
the ignition (§6.1) and the letter pass (§6.2); the collection in
drawers (§6.13); the pinned specimen (§6.4) with the venation
(§6.7) in its natural-history passage; the cabinet figures
(§6.16); the catalogue record (§6.17); the acquisition form
(§6.14). The home page is the only page with an ignition and the
only page whose drift fields (§6.5) run at full count — the front
of the cabinet is the richest pour.

**Listing — one stratum's drawers.** A category page is a single
stratum, deepened: its cards (§6.13) in rows, its own head
apparatus stating the stratum and the count ("STRATUM III — AMBER
· 41 M — TWENTY-TWO PIECES"), figures (§6.16) scoped to the
stratum and recomputed from its rows, and the record (§6.17)
excerpted to the same rows with a link to the full ledger.
Filters, if the catalogue honestly needs them, are seam toggles
on the rail (§11) — never a sidebar of facets, which is a
warehouse's furniture in a cabinet.

**Detail — one specimen, at its record.** The piece at full
size: its photograph in a recipe-1 block at its surveyed rest
angle, its name and full age (§6.8), its catalogue row excerpted
from §6.17 (origin, acquired, status), its story, the bubble
caption with the visitor's own count (§6.10), and the acquisition
form (§6.14) pre-set to the piece. Its stratum neighbours close
the page ("ALSO IN THIS STRATUM" — §6.13 cards). A detail page
never re-stages its piece for display: the record is the display.

**About — the cabinet's keepers.** The dealers and the method:
who keeps the cabinet, how an age is verified before it is
printed (the about page states §1's law in long form — the
theme's ethics, placed where a committed visitor digs for it),
set in Amber-stratum blocks with the record's voice (§12).

**Contact / acquisition — the form's own page.** §6.14 alone on
a Surface block, reached from anywhere; a direct arrival lands
on an unlit-by-ceremony page (interior pages arrive lit at rest,
§6.15) with the seam list unchosen — an enquiry begins
unpresumed, whoever you are.

**The dark block (404).** §6.18, everywhere, unchanged.

**Interior pages and the light.** Ignition (§6.1) and the letter
pass (§6.2) are home-only. Interior heroes are a single block
holding the page's title piece — its name as the headline, its
apparatus beneath — with the light already at rest via §6.15's
pass. The site keeps one lamp and many drawers; only the front
drawer watches it being lit.

## 8. Worked examples

### 8.1 The hero — the light, kept

*The commission: Kessler & Daughters, amber and inclusion
dealers of Gdańsk; a catalogue of 214 specimens, every age
verified against the house book. The home page runs hero → the
collection → the pinned bee → natural history → figures → record
→ acquisition. Declared strata: hero at Surface, collection at
Honey, the bee at Amber, figures and record at Deep, the form
and footer at Dusk.*

- **The composition (§6.12).** First screen: the resin-deep
  surround, the cabinet column, the rail at the left with the
  disc at Surface. The hero block, recipe 1, holds the Baltic
  Bee's photograph in its shell window and, on its amber-face
  plate, the headline: **"Light, kept."** The standfirst: "A
  bee, a seed, a breath of Eocene air — held in resin on the
  Baltic shore, catalogued in Gdańsk, and lit on this page by
  one light only." The apparatus beneath: "KESTLER & DAUGHTERS —
  AMBER & INCLUSIONS · GDAŃSK · EST. 1962 · CAT. No. 46-001 —
  41,000,000 YEARS". The action: "See the collection".
- **The ceremony (§6.1, §6.2).** Fonts ready at t≈150ms: the
  light kindles behind the block over 2000ms, the shell's six
  inclusions settling as it warms; the standfirst and action
  arrive with the light at t≈1600–2000; at t=2000 the warmth
  walks the headline — L, i, g, h, t — eleven letters at 80ms,
  done by ≈2900, each keeping its rested warmth. A visitor who
  never scrolls has received the whole thesis: there is one
  light, it is behind the specimen, and it has read the label.
- **Scroll timeline.** 0–80px: the light (§6.3) begins its
  travel, the disc (§6.6) leaves Surface; the hero block tilts
  under the hand (§6.9) and takes its first visitor bubble
  (§6.10) if clicked. The collection's first drawer crosses
  30%: its edge catches, and the descent is underway.

### 8.2 Mid-page — the bee, turned

*The same page, at the Amber stratum: the signature piece is
the Baltic Bee, Cat. No. 46-001, whose record (§6.17) reads:
caught on the Sambian shore, 41,000,000 years, acquired by the
house in 1974.*

- **Entry.** The pin region engages: the bee's block sticks,
  its story column beside it. Beat one is already read: "THE
  CATCHING — RESIN ON A PINE, A WARM MORNING, A BEE ABOUT HER
  WORK." The specimen at 0°, lit at the stratum's temperature.
- **The beats.** The visitor scrolls the pin: at q=0.25 the
  bee has turned 4.5° and beat two inks — "THE KEEPING — THE
  RESIN HARDENED AROUND HER BEFORE THE FOREST ITSELF WAS
  BURIED." At q=0.55, 9.9°: beat three, and the natural-history
  passage opens — the wing plate (§6.7) draws itself in
  branching order beside the story, because at this angle the
  wing is what the light reaches. At q=0.9 the turn completes
  at 18°; beat four is read with the specimen at rest: "THE
  RECORD — CATALOGUED 1974. NEVER POLISHED. THE HOUSE DOES NOT
  POLISH."
- **The buy block.** The pin releases into the bee's
  acquisition block: its price on its plate, and beneath its
  age label the record's own deadpan, printed because both
  halves are true: **"41,000,000 years in the making; ships in
  3–5 days."** The visitor has just scrolled three days of
  resin-time in forty seconds of reading; the joke, such as it
  is, is the catalogue's, and it is earned.
- **What the visitor feels.** Examination, repaid. The pin is
  long (340vh) because forty-one million years is long; the
  turn is small (18°) because a fossil is tipped, not spun.
  Nothing asked for attention — the story and the turning are
  the same fact at two sizes.

### 8.3 Conversion — seal the enquiry

*The same page's end: the acquisition form (§6.14), reached
from the bee's buy block. The visitor trapped two bubbles in
the bee's block during the pin (§6.10).*

- **Arrival.** The form opens pre-set: the bee's seam line
  chosen, its mini-card beside the form showing the bee's block
  — with the visitor's two bubbles lodged in its shell, because
  the card is the block's other printing and the bubbles are
  DOM truth. The form's apparatus states the piece in full:
  "CAT. No. 46-001 — THE BALTIC BEE — 41,000,000 YEARS".
- **The sealing.** The visitor writes their name and note, and
  mistypes their direction (no @): on blur the rule holds its
  ink and the record notes beneath, in Source Serif: "The post
  cannot reach that address — write it again, slowly." (§12's
  error voice: a fact about the post, not a scolding.) They
  correct it; the note clears. They press SEAL THE ENQUIRY:
  the button's edge warms, and on the house's reply the block
  warms to full glow as a bubble rises in its shell and lodges
  beside the line: "ENQUIRY No. 46-118 — IN THE BLOCK. THE
  DEALER REPLIES WITHIN TWO DAYS." Below, in the record
  (§6.17), a new session row stands in apparatus: "No. 46-118 —
  ENQUIRY — YOURS — THIS VISIT".
- **Failure rehearsed.** If the post fails, nothing they wrote
  is cleared; the note above the form reads "NOT SEALED — THE
  POST COULD NOT BE REACHED. YOUR WORDS ARE KEPT ABOVE." and
  no bubble is trapped — a bubble for an enquiry that never
  arrived would be §1's fraud in miniature (§10, gate 7). A
  visitor who read a bee's whole biography to reach this form
  is never sent back to an empty sheet by a network blink.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The lava-lamp website.** Glows everywhere, each element
   with its own private halo — buttons backlit, cards rimmed,
   a warm blob behind every heading. *Cure:* §1's law and §5's
   model — one light, three variables, one falloff function.
   Any brightness that cannot be recomputed from `--lx/--ly/
   --light-temp` is a second lamp and a gate failure.
2. **Amber as a colour scheme.** Orange-brown rounded cards on a
   white or beige page, "warm premium" copy, no cabinet, no
   blocks, no record. *Cure:* §4 — the theme is a substance and
   a bookkeeping, not a palette; if the page could be re-skinned
   to teal without changing a sentence, it was never Amber Hour.
3. **Rounded ages.** "Millions of years old!", "≈40M years",
   "timeless treasure". *Cure:* §3 law 1 — full digits, tabular,
   "years"; the catalogue's number is the claim and rounding it
   is the one fraud this theme cannot survive.
4. **Text over glow.** Copy set on the light layer or on shell
   gradients, contrast collapsing as the lamp travels — readable
   at the top of the page, soup at the bottom. *Cure:* §2's
   pairing law — text on opaque plates only, audited at the
   light's extremes (§10, gate 5).
5. **Fast amber.** Snappy 150ms hovers, springy blocks, a light
   that teleports to the scroll position. *Cure:* resin rates —
   nothing under 240ms except a press's first frame; the lamp
   lerps at 0.09 and arrives like a carried thing. Speed is the
   one thing forty-one million years cannot be hurried into.
6. **The spinning specimen.** A product rotating on a loop,
   turntable-style, or a carousel of fossils. *Cure:* §6.4 —
   rotation is scrubbed to the reader's scroll, 18° total, and
   stops when the reading stops. A fossil on a turntable is a
   souvenir shop.
7. **Bubble machines.** Ambient bubble fountains, click effects
   that spawn particles, bubbles drifting across text. *Cure:*
   inclusions are rationed and placed — drift fields are
   surveyed (§6.5), visitor bubbles are capped at 6 per block
   and clamped to shells (§6.10). Air in this theme is
   catalogued like everything else.
8. **Fossil clip-art.** Stock "amber texture" gradients, a
   dinosaur silhouette, a cartoon bee. *Cure:* specimens are
   the catalogue's real photographs; where no photograph
   exists, the drawn plate (§6.7's grammar) — a line drawing of
   the actual piece, made for the record.
9. **The percentage sunset.** A progress bar with "62% read", a
   disc that races to dusk on a short page or never sets on a
   long one. *Cure:* §6.6 — the disc is scrubbed to document
   progress and dusk is the footer by construction; and §5 —
   percentages are banned from the theme outright.
10. **Tilt on everything.** Headings, buttons, prose blocks all
    leaning toward the pointer. *Cure:* §6.9 — tilt belongs to
    blocks (the substance), never to type, controls or plates
    alone; a button that tilts is a button showing off.
11. **The breathing lamp.** A glow that pulses gently "for
    ambience" behind the hero. *Cure:* §5 — the light travels
    and dims by position only; a pulsing lamp is a faulty lamp,
    and this cabinet's lamp is kept.
12. **Ignition on every page.** The 2000ms kindling replayed at
    every route until returning visitors dread the front door.
    *Cure:* §7 — ignition and the letter pass are home-only,
    once per session; interior pages arrive lit by §6.15's pass.
    Ceremony rationed is ceremony kept.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **One-light audit.** Five glows sampled across the page (a
   hero shell, a mid-page block, a card, the form block, the
   footer) at three scroll positions: each block's `--glow-i`
   equals `clamp(1 − d / 720, 0, 1)` for its measured `d` within
   ±0.03, and the sun-disc's colour equals `--glow` at the same
   `--light-temp`. A private glow — any brightness not derivable
   from the three variables — fails the build.
2. **Age audit.** Three ages chosen at random from anywhere on
   the site (a card, a detail page, the figures band) are traced
   by hand to their rows in the catalogue record (§6.17):
   digits, commas and "years" identical. A rounded, estimated or
   unrowed age fails.
3. **Three-printings agreement.** A specimen's name, age and
   status agree across its card (§6.13), its detail page (§7)
   and its catalogue row (§6.17) at every point in a scripted
   session — including after a sale state changes. All three
   render from one data object; a hand-patched printing fails.
4. **No stranded content.** With JS disabled, the whole page
   reads: blocks lit, ages printed, veins inked, form working,
   the specimen at 9° with its story in flow. With JS on and the
   loop killed, every watchdog (§6.1's 2400ms, §6.2's 3200ms,
   §6.7's 2200ms, §6.8's 2000ms, §6.10's 2800ms, §6.15's
   pageshow forcing) fires and settles its surface.
5. **Contrast at light extremes.** Text pairings (§2's law) are
   audited with the light at surface, mid-page and dusk
   positions, and at the ignition's first frame: no text over
   glow, no plate below its locked ratio at any frame. A pairing
   that only works when the lamp is elsewhere fails.
6. **Bubble ration.** Drift-field counts per panel equal the
   survey's; visitor bubbles never exceed 6 per block (4 on
   mobile), never render over a plate (clamp verified by
   clicking a plate's centre on three blocks), and the release
   of the oldest at the cap is witnessed in a scripted session.
7. **Form-keeping and honest sealing.** A failed submit
   (simulated network error) leaves every field, the chosen
   specimen and the note exactly as written, with §12's failure
   note — and traps **no** bubble and appends **no** record row.
   A success does both, with the server's real number.
8. **Pin honesty.** The specimen's rotation is a pure function
   of scroll: disabling JS leaves the story fully readable in
   flow; killing the loop mid-pin still releases the sticky
   stage at the region's end. A build whose story can be
   trapped behind its fossil fails.

**Standard (must pass, fixable in review):**

9. Density falls with descent (§4): hero alone in its viewport,
   the specimen alone in its stratum, the footer holding the
   record's totals and the dusk apparatus only.
10. Exactly one pin (§6.4), one ambient system (§6.5), one
    letter pass (§6.2), one ignition per session (§6.1); §5's
    refusal list honoured — no marquee, no blur reveals, no
    kinetic type beyond the pass, no parallax beyond the
    inclusion fields.
11. The four radius recipes rotate by catalogue order with no
    adjacent repeats (§4); strata depths agree across §4's
    labels, §6.6's bands and §6.11's rail.
12. Every interactive element is ≥44px; focus shows §11's gold
    ring or §6.9's fixed pose; focus never kindles, counts or
    traps anything.
13. Mobile: pin cut (§6.4), tilt cut (§6.9), disc in the header
    (§6.6), record as stacked ledger (§6.17), drift fields at
    mobile counts (§6.5).
14. The anti-slop line survives editing: the oldest specimen's
    label (§12's fixed string) is present verbatim on its card
    or buy block — a copy pass that "improves" it into marketing
    fails review.

## 11. Component inventory

Every component a real Amber Hour site needs, with its themed
treatment. Components the theme refuses are listed with their
in-theme replacement — a refusal without a replacement is a gap,
not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | The seal: pale-gold ground (`--gold`), resin text (10.26:1 the other way — resin on gold measures as gold on resin), radius recipe 4 at small scale; its edge warms 300ms `--ease-kindle` on hover — the seal under the lamp. Press: flattens 2px, edge glow peaks. One per block at most. |
| Secondary button | Ruled line button: transparent, 2px bottom rule in the plate's text colour; hover inks the rule gold over 250ms `--ease-draw`. |
| Bubble button | §6.10's "Trap a bubble": apparatus text, transparent, a 10px bubble outline at its left that fills with honey when the block's set is non-empty — the button reports the block's count by its fill (0 = outline, ≥1 = filled) with the true count in its label. |
| Text input | Inscription line (§6.14): apparatus label above, 2px rule below, no box; focus inks the rule gold with the travelling bubble dot. |
| Textarea | Ruled sheet: lines every 29.75px (the body line unit ×1.75), Source Serif 17px, growing by lines, never internally scrolled. |
| Select | Refused. Choices are seam lists: ruled radio lines with the piece's name, number and age (§6.14's specimen list generalised) — a dealer lays the pieces out; she does not hide them in a dropdown. |
| Checkbox | The bubble box: a 16px bubble outline in the plate's text colour; checked = the bubble fills with honey and a 3px seed dot appears at its centre — a thing caught, deliberately. |
| Radio | Seam line (§6.14): the chosen line's rule inks gold and its bubble dot fills; the dot is a peg on the line. |
| Toggle / switch | Refused. The cabinet has states of keeping, not switches; use two seam lines (In the cabinet / Not for sale) as radios. |
| Card | Specimen card (§6.13): block, shell window, plate, age output, record line. |
| Table | Catalogue record (§6.17): real table, apparatus headers, no zebra striping — row plates are the section's stratum tone, uniform. |
| Tabs | Refused. Depth is not tabbed; strata are scrolled, indexed by the rail (§6.11) or paginated by the line. A build needing tabs has two drawers arguing — open them as two strata. |
| Accordion | The split block: a block whose lower face unfolds downward along a surveyed seam over 400ms `--ease-settle`, its inner glow rising as it opens — a pour opened along its crack line. One open per stratum. |
| Modal / dialog | The specimen viewer: the piece's block enlarged over a resin-deep scrim at 88%, its photograph and full record; closed by its own apparatus button ("CLOSE THE BLOCK"). The theme's only dialog; the acquisition confirmation is inline (§6.14), never modal. |
| Toast | Refused. News from the cabinet is recorded, not toasted: transient confirmations appear as a line in the record's session block (§6.17) or in the form's own block (§6.14). |
| Tooltip | Refused. Explanation lives in apparatus and record lines; an age that needs a tooltip needs a better label. |
| Badge | Stratum chip: apparatus text on an amber-face plate — "STRATUM III — AMBER" — the badge states a piece's depth, never a marketing claim ("NEW" is an undated word and is banned, §12). |
| Alert | Unlit block: a matte deep-amber band cut into the current ground, cream text, gold left rule, §12's error voice, persistent until resolved. An alert is a piece the light has not reached, and it reads that way. |
| Pagination | Line pagination: "Deeper in the cabinet" / "Back toward the light" links lettered with the next stratum's name and depth — never numbered pages; a descent is continuous. |
| Progress bar | Refused. Progress is the sun-disc (§6.6). |
| Spinner | Refused. Waiting is unpoured resin (§6.15). |
| Skeleton | §6.15's unpoured blocks with apparatus labels. |
| Search | The record search: a single inscription line in the header; results return as specimen cards (§6.13) with their rows — search results in this theme are a drawer of pieces, not a list of links. |
| Breadcrumbs | Replaced by the strata rail's current label (§6.11) plus the disc: the visitor's position is a depth and a lamp, not a trail of pages. |
| Skip link | "Skip to the specimens" as a plain cream link appearing on first focus above the cabinet. |
| Focus ring | 2px outline in `--gold`, offset 3px, on the element's plate; on blocks, focus-within also takes §6.9's fixed pose. On gold grounds (the seal button) the ring is resin. |
| Divider | The stratum hairline (§4): honey at 35% with the stratum's apparatus at the rail — and one bubble, 8px, sitting on the line at the light's current x-position, so even the furniture reports where the lamp is. Wavy SVG dividers are refused — that is another theme's water; this theme's medium does not wave. |

## 12. Content & copywriting voice

Two voices, cast like the type. **The Dealer** writes apparatus:
catalogue numbers, ages, strata, labels — Source Serif, uppercase,
terse, every figure tallied. **The Record** writes prose:
provenance, descriptions, errors, confirmations — Source Serif
sentence case, plain and patient, the voice of someone writing up
the cabinet for whoever opens it next. The voices never swap:
apparatus never sentences, the record never shouts.

**Headline style.** The thing and its keeping, stated. ✓ "Light,
kept." / "The bee, and what the resin did with her". ✗ "Discover
timeless treasures from a world long gone!" (exclamation, a
"discover" the cabinet refuses — the visitor discovers nothing;
the pieces were catalogued before they arrived — and not one
figure in it). Exclamation marks are banned from the whole theme:
forty-one million years is not excited.

**Label style.** Apparatus: number + name + age. ✓ "CAT. No.
46-001 — THE BALTIC BEE — 41,000,000 YEARS". ✗ "Ancient Bee
(Millions of Years Old!)" (rounded age, §3 law 1; exclamation;
the age demoted to a parenthesis).

**Error voice.** A fact about the post or the form, stated
plainly, with the way back. ✓ "The post cannot reach that
address — write it again, slowly." ✓ "NOT SEALED — THE POST
COULD NOT BE REACHED. YOUR WORDS ARE KEPT ABOVE." ✗ "Oops!
Something went wrong 😞" (the cabinet has no "oops", and no
emoji survives the resin).

**Empty-state voice.** ✓ "Nothing was caught in this piece." /
"No specimen in the record matches that name." ✗ "No results
found. Try being less specific?" — the record does not blame
the visitor for the book's gaps.

**Confirmation voice.** ✓ "ENQUIRY No. 46-118 — IN THE BLOCK.
THE DEALER REPLIES WITHIN TWO DAYS." ✗ "Success! 🎉 Your
request is in!" — a confirmation is a ledger entry with a
bubble in the resin, not a celebration.

**Banned words:** amazing, breathtaking, stunning, timeless
treasure, discover (as an invitation), journey, unlock,
supercharge, NEW (as a badge), oops, millions of years old (as
a substitute for the figure).
**Owned words:** kept, held, caught, in the making, catalogued,
stratum, inclusion, by the light, in the block, entered in the
record, never polished, ships in (the record's deadpan is owned:
deep time and dispatch times may share a label when both are
true).

**Fixed strings (verbatim, do not paraphrase):** the oldest
specimen's label line — "41,000,000 years in the making; ships
in 3–5 days."; the 404 heading — "Nothing was caught in this
piece."; the skeleton label — "POURING — THE SPECIMENS"; the
waiting line — "STILL POURING — THE RESIN IS THICK TODAY."; the
form failure note — "NOT SEALED — THE POST COULD NOT BE
REACHED. YOUR WORDS ARE KEPT ABOVE."; the search-empty line —
"No specimen in the record matches that name."

## 13. Full-page scroll choreography map

The home descent, top to bottom. Every beat in order; instruments
run continuously beneath the beats (the light §6.3 travelling, the
disc §6.6 sinking, drift fields §6.5 in their panels, tilt and
bubbles live on every kindled block).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Ignition (§6.1): the light kindles behind the hero; inclusions settle | A lamp being lit in a dark room |
| 2 | 0–80px | Letter pass completes (§6.2); light hands to the scroll model (§6.3) | The label, read by the light |
| 3 | First scroll | The lamp travels; the disc leaves Surface (§6.6); hero block tilts and takes bubbles (§6.9/§6.10) | Carrying the light down |
| 4 | Collection stratum | Drawers kindle in stagger; photographs settle; ages count (§6.13/§6.8) | Drawers opening, each with its years |
| 5 | Pin engages | The bee's story begins; rotation 0° (§6.4) | A specimen taken in hand |
| 6 | Pin, q≈0.55 | The wing draws itself (§6.7) as the turn reaches the wing's angle | The diagram forming at the right moment |
| 7 | Pin releases | The buy block; the oldest label's deadpan line (§8.2) | Examination, then the honest joke |
| 8 | Figures band | Cabinet figures count (§6.16) | The house's arithmetic |
| 9 | Record section | Head rule draws; the ledger stands (§6.17) | The workings, shown |
| 10 | Acquisition | The form on its block (§6.14), pre-sets honoured | The ask, sealed in resin |
| 11 | Footer | The disc sets into Dusk (§6.6); the record's totals close the page | The day ending inside the resin |

**Reverse pass.** Scrolling up: the lamp travels back and the
temperature re-warms toward gold — the day runs backward, which
is correct for a carried light; the pin's turn reverses with the
story (§6.4). But performances do not un-happen: kindled blocks
stay kindled, the wing stays inked, ages stay printed, bubbles
stay lodged. The page going up is identical in its records and
reversible only in its positions. That asymmetry is the theme's
grammar, and §6.3/§6.4 state it in their own sections so no
builder harmonises it away.

**Jump-scroll catch-up.** Anchor jumps and flings: blocks passed
are kindled without stagger, ages print their final strings,
the wing lands inked, the pin lands at the q of the landing
point, and the light and disc lerp to the landing position in
≈800ms — a quick sunset or sunrise, honest and visible. No
ceremony is owed to a teleport.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 820KB, of which images ≤ 480KB (specimen photography is the content) |
| Fonts | Fraunces (2 weights, opsz) + Source Serif 4 (2 weights) ≤ 160KB, `font-display: swap` |
| JS | ≤ 65KB gzipped (one loop, two observers, light model, form) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the ignition's timers are sliced per beat |
| Glow updates | ≤ 6 blocks' `--glow-i` per frame, only within 900px of the light (§6.3) |
| Drift system | ≤ 42 inclusions page-wide, ≤ 0.4ms/frame (§6.5) |
| Ceremony latency | Any triggered ceremony settled by its watchdog (§5) — ignition 2400ms, letters 3200ms, draw 2200ms, counts 2000ms |

**Cut order when the budget is exceeded** (cut in this order,
record each cut in the build notes):

1. Inclusion drift (§6.5) — to the surveyed rest field, then to
   fewer inclusions per panel.
2. Magnetic drift (§6.9) — tilt keeps its refraction; the pull
   goes.
3. The vignette mask scrub (§5) — sections kindle without the
   travelling mask; the light layer stays.
4. Wing venation draw (§6.7) — the wing arrives inked with a
   300ms warm; the draw order line (§6.7's reduced variant)
   carries the information.
5. The letter pass (§6.2) — the headline warms whole over 600ms
   (its own fallback, promoted).
6. The light-pass transition (§6.15) — navigation becomes plain;
   the cabinet keeps its lamp, loses its journey.

**Never cut:** the one-light model and its audit, the watchdogs,
the locked pairings, the catalogue record, the age counters'
final strings, any reduced-motion variant. A build that cuts
the honesty to keep the ambience has switched off the lamp and
left the glow — §1's fraud, committed by the performance team.

## 15. Build-order checklist

1. Survey first: fix the catalogue — every specimen with its
   real name, number, origin, age (or UNRECORDED), status and
   photograph — as the one data object the cards (§6.13),
   figures (§6.16) and record (§6.17) will all render from.
   Fix the strata, each section's stratum and depth, the four
   radius recipes' rotation, and each panel's drift field
   (positions, amplitudes, periods, phases). Write the survey;
   everything else is generated from it.
2. Build the static cabinet: all blocks poured at rest —
   lit, ages printed, veins inked, specimen at 9°, form
   working — with no JS. This is the site; the rest is light.
3. Set the palette tokens, the strata plate tones and the
   pairing law (§2); audit contrast on every plate, including
   the transit frames of §6.1's ignition, before any motion
   exists.
4. Set the type scale and the stratum line-heights (§3 laws);
   set the hero headline and verify the letter-pass cap (§6.2)
   against its real letter count.
5. Pour the geometry (§4): surround, cabinet column, rail,
   strata hairlines, block shells and plates; author the four
   radius recipes once, reuse everywhere.
6. Build the instruments from the data object: strata nav
   (§6.11), sun-disc (§6.6), cabinet figures (§6.16), catalogue
   record (§6.17). Verify the three-printings agreement by
   reading all of them against the object.
7. Add the shared loop; wire the one-light model (§6.3) —
   position, temperature, per-block falloff — and run §10 gate
   1 by hand on five blocks before building anything that
   glows.
8. Add the drift fields (§6.5) from the survey's seeds; verify
   clearances and the page-wide count.
9. Add the pin (§6.4) with its travel set from the real story's
   height; add the venation (§6.7) keyed to its beat.
10. Add the hand: tilt and drift (§6.9) with the pin exemption,
    then the bubble trap (§6.10) with its clamp and cap
    rehearsed.
11. Add the ceremonies: ignition (§6.1) with its 2400ms
    watchdog and session flag, letter pass (§6.2), hero
    composition (§6.12).
12. Build the acquisition form (§6.14) with its number taken
    from the record, and error-keeping rehearsed against a
    simulated network failure; verify the session row lands in
    §6.17.
13. Add the skeleton and light-pass (§6.15) with the pageshow
    watchdog, the dark block (§6.18), and the mobile cuts
    (§10, item 13).
14. Run the full gate (§10) including the one-light audit and
    the age audit with three ages chosen by someone else;
    sign-off by a non-builder — the dealer who checks the book
    is never the hand that wrote it.
