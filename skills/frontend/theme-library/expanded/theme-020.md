# 20. Halftone Confessions — Expanded (v1 + v2)

*Expansion written to `EXPANSION-STANDARD.md` v1 + the v2 deepening pass
(50x standard), ordered 2026-11-23. This file is the complete, buildable
specification of theme #20. The original library entry's identity is
preserved exactly — the scroll-out inversion, the contact-sheet world, the
four palette anchors, Archivo + Newsreader — and deepened, never
redesigned. Where this file and the short library entry disagree, this
file governs.*

**The one law of the theme, stated before everything else:** the dots are
always a photograph's own screen. A dot field that is not a specific
photograph resolving is decoration, and decoration is the one thing this
theme refuses. Every pitch, every shimmer, every resolving frame on the
page traces back to a real image the visitor can eventually see sharp.

---

## 1. Concept & world

Newspaper photography before colour was a negotiation between the reader
and a field of dots. Hold a 1962 front page at reading distance and the
dots disappear into a face; bring it close and the face dissolves into
mechanics — ink, pitch, screen angle. Halftone Confessions builds a
website out of that negotiation. The site is about how seeing works, and
its signature move inverts every other site on the internet: **scrolling
zooms out.** The visitor arrives too close — inside the photograph, among
dots the size of coins — and earns the picture by stepping back. Distance
is not a metaphor in this theme; it is the scroll control.

The world is the newspaper darkroom and the photo desk that sat beside
it: contact sheets pinned above the developing tray, grease-pencil crop
marks on the prints, frame numbers chalked along the sheet's edge, a
caption typed under every frame with the photographer's name, the date,
and the desk's standing instruction — *not to be cropped*. The page is a
contact sheet that develops as it is read. Sections are sheets. Images
are frames. Progress is a frame counter and an exposure strip. The
footer is the fixer bath: everything that survives the page ends up
there, fixed and permanent.

**Mood.** Patient, forensic, quietly emotional. The theme trusts the
visitor to look twice. Nothing flashes; things *resolve*. The emotional
arc of a page is the arc of a print coming up in the tray — first a
ghost, then a suspicion, then a face — and the copy is written by people
who caption photographs for a living: terse, factual, and devastating in
the details they choose to include.

**Why the inversion works (the perceptual ground).** Human vision reads
a halftone at two distances: inside roughly one metre the eye resolves
the screen itself and the picture dissolves; beyond it the visual
system integrates the dots into continuous tone. Every reader of a
printed newspaper has performed this experiment a thousand times
without naming it. The theme simply maps that metre onto 120vh of
scroll: `--pitch-0` at scale 1.6 is the photograph at 20cm, all
mechanics; `--pitch-5` at scale 1.0 is the same photograph at arm's
length, all face. This is why the resolve must be *scrubbed and
reversible* rather than played: the visitor's hand is moving the paper
toward and away from their own eyes, and a played animation would break
the proprioception — the felt sense that *I* am holding this print.
It is also why no other element in the theme zooms in: zooming in is
what the visitor's scroll is *for*, in reverse.

**Best-fit sites and audiences.**

- Documentary photographers and photo studios whose archive *is* the
  product — the theme lets the archive behave like an archive.
- Photojournalism retrospectives, museum and gallery exhibition sites,
  book launches for photography monographs.
- Optics, vision-science and camera-craft brands that can honestly claim
  "how seeing works" as their subject.
- Long-form visual essays where one portrait carries the whole piece and
  the reader should meet it slowly.

**When NOT to use it.**

- E-commerce grids of fifty products: the resolve choreography is a
  per-image cost and a per-image claim; fifty frames resolving is fifty
  interruptions, and product shots must be legible instantly.
- Dashboards, data tools, anything scanned under time pressure. The
  theme's first 120vh is deliberately spent on one photograph.
- Sites whose imagery is illustration, UI screenshots or logos. Halftone
  is a photographic process; screening a screenshot is a costume.
- Brands that need cheerfulness at first paint. The hero begins as an
  abstract field of dots — magnificent, and not cheerful.

---

## 2. Palette

Four anchors, inherited from the original entry, plus derived tokens
that exist only to keep the anchors honest at text sizes.

| Token | Hex | Role | Ratio | Pairing & contrast |
|---|---|---|---|---|
| `--paper` | `#EFEDE8` | Photo-paper ground; sheet surfaces, mats, light sections | 62% of the page | Ground for `--dot` text (≈15.5:1) and `--tray` text (≈7.8:1) |
| `--dot` | `#141414` | Dot black; the halftone dots themselves, frame lines, display text | 22% | On `--paper` ≈15.5:1; the dots are printed in this and nothing else |
| `--tray` | `#20504C` | Developing-tray teal; dark sections, navigation rail, door transitions | 12% | `--paper` text on it ≈7.8:1; it is the darkroom's dark, never a brand splash |
| `--fixer` | `#C98F2D` | Fixer amber; grease-pencil marks, stamps, the exposure strip's active band edge | 4% | Graphic marks only: ≈2.6:1 on paper is *below* text contrast by design — amber never sets text (see `--fixer-deep`) |
| `--fixer-deep` | `#8A5E0C` | Derived: amber darkened one register for text-bearing uses | within the 4% | ≈4.9:1 on `--paper` — stamp words, amber labels, error text in the desk voice |
| `--paper-warm` | `#E6E1D4` | Derived: aged paper for sheet backing, card reverses, the skeleton's unexposed tone | — | Sits one step behind `--paper`; never carries text alone |
| `--dot-soft` | `#33322E` | Derived: softened black for body text at small sizes and caption secondary lines | — | ≈11.9:1 on `--paper`; used where full `--dot` would shout |
| `--tray-deep` | `#13322E` | Derived: the tray at rest — footer ground, dark-scheme ground, door black | — | `--paper` on it ≈9.6:1 |
| `--sheen` | `rgba(239,237,232,.14)` | Wet-print sheen gradient stop for the tray-lift (§6.10) | — | Only ever a moving gradient over a print, never a surface colour |
| `--mark-line` | `rgba(20,20,20,.88)` | Frame border and rule colour (dot black at print strength) | — | 2px frame lines, 1px hairlines at .45 alpha variant `--mark-hair` |

**Usage discipline.** The 62/22/12/4 ratio is measured on the home page
at rest, hero excluded. Amber above 6% of any viewport means someone has
started decorating with the grease pencil — §9 failure. Teal appears as
whole environments (a section *is* in the tray) or as instruments (rail,
strip), never as a button colour sprinkled on paper.

**Dark-mode behaviour.** There is no inverted paper mode. Under
`prefers-color-scheme: dark`, the page goes *into the tray*: sheet
grounds become `--tray-deep`, mats become `--tray`, text becomes
`--paper`, and halftone dots print in `--paper` on the dark ground —
exactly what a contact sheet looks like under darkroom light. Frame
lines become `rgba(239,237,232,.75)`. Amber is unchanged (grease pencil
reads under any light). A site that cannot restyle its photography for
the tray ground must not ship the dark scheme; a half-dark Halftone page
is worse than a light one.

---

## 3. Typography

Two voices, inherited: the desk and the story.

- **Archivo** — the photo desk: captions, frame numbers, labels, buttons,
  data. Always uppercase at caption sizes, always letter-spaced, always
  tabular for numbers. The desk does not emote; it records.
- **Newsreader** — the stories the photographs illustrate: headlines,
  body, pull quotes. Sentence case, optical sizes on, italics for the
  photographer's own words only.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Hero essay title | Newsreader 500 | 68px / 1.02 (≥1200) | −0.01em | Set beside the hero frame, never over the dots |
| Display 1 | Newsreader 500 | 52px / 1.08 | −0.01em | One per page; the sheet's headline |
| Display 2 | Newsreader 500 | 38px / 1.14 | 0 | Section (sheet) titles |
| Heading | Newsreader 600 | 26px / 1.25 | 0 | Frame-group heads inside a sheet |
| Body | Newsreader 400 | 19px / 1.62 | 0 | Measure 58–66ch; the essay measure |
| Body small | Newsreader 400 | 16.5px / 1.58 | 0 | Secondary reading, card text |
| Caption | Archivo 500 | 12px / 1.55 | 0.09em, uppercase | The desk block under every frame: name, place, date, instruction (§12) |
| Desk label | Archivo 600 | 11px / 1.4 | 0.16em, uppercase | Instruments, buttons, badges, nav |
| Data | Archivo 500 | 13px / 1.4 | 0.02em, `tabular-nums` | Frame counts, print counts, exposure figures |
| Frame counter | Archivo 600 | 12px / 1 | 0.12em, `tabular-nums` | `FR. 07 / 36` — the digits never reflow (§6.5) |

**Per-role laws.**

- Text is *never* halftoned, blurred, or set over a dot field. Type is
  print; dots are photographs. The two materials do not mix (§9).
- Captions are part of the frame's DOM, in reading order, never an
  overlay and never revealed by hover on touch devices.
- Archivo numerals are tabular everywhere they count; a frame counter
  that jitters horizontally as digits change is a §10 failure.
- Newsreader italics are reserved: a quote from the photographer, or the
  one-line standfirst. Desk text never italicises.

---

## 4. Layout language

**The sheet.** The page is a stack of contact sheets laid on the desk.
A sheet is a full-width band with a `--paper` ground, a 2px `--mark-line`
top border, and a sheet header: sheet number ("SHEET 2"), title in
Display 2, and the sheet's frame range ("FR. 07–14"). Sheets alternate
with tray bands (`--tray` or `--tray-deep` grounds) where the darkroom
takes over — dark sections are *between* sheets, like prints lifted into
the tray and set down again.

**The margin rail.** At ≥1200px a fixed 76px rail rides the left edge:
the frame counter at its top, the exposure strip running its height,
the sheet number at its foot. The rail is the darkroom's fixed furniture
while sheets move past it. It carries no navigation and no branding —
instruments only (§6.5, §6.13).

**Frames.** A photograph lives in a frame: 2px `--dot` border, a 12px
paper mat inside the border, the image inside the mat. Grease-pencil
marks are drawn on the mat and the border — the desk marks the print,
not the picture. Contact grids run 3 frames per row at ≥1200px, 2 at
768–1199px, 1 below 768px, with 28px gutters — the gutter is the sheet's
own paper showing between prints, and it is the theme's whitespace:
**the mat and the gutter are the whitespace system.** There is no other
empty space in this theme; generous emptiness elsewhere reads as an
undeveloped sheet.

**Spacing rhythm.** Base unit 8px. Sheet padding 96px vertical (64px
below 768px). Frame-to-caption gap 12px. Section choreography: a sheet
opens with its header, develops its frames in grid order (§5), and
closes with a full-width hairline and the next sheet's number — the
visitor always knows which sheet they are on, the way a printer does.

**Density rules.** One hero frame per page. Maximum 9 frames per sheet;
a tenth frame starts a new sheet. Maximum 2 tray bands per page. The
hero pin (§6.1) is the only pinned scene on any page (§10).

**Placed imperfections.** Crop marks sit 1–2px off true — grease pencil
is a hand tool (§6.3). Frame borders are exactly true. The distinction
is the theme in miniature: the *desk's hand* may wobble; the *print*
may not.

**Frame anatomy, layer by layer.** Every frame on every page is the
same five-layer stack, bottom to top, and builders do not improvise a
sixth layer: (1) the *sheet* — `--paper` ground, shared by the whole
band; (2) the *border* — 2px `--mark-line`, the frame's drawn edge,
with the frame number set into its top-left corner in Desk label type
on a 6px paper tab that breaks the line, the way a number is chalked
over a border on a real sheet; (3) the *mat* — 12px of paper inside
the border (8px below 768px), the surface grease marks live on; (4)
the *image stack* — base sharp `<img>` with its rendition overlays
(§6.1/§6.2), clipped to the frame's crop inset once §6.3 has run; (5)
the *mark layer* — one SVG carrying crop marks (§6.3) and, on
portraits, the face circle (§6.4), positioned over mat and image edge
alike, `pointer-events: none`, `aria-hidden`. The caption block is
*not* a layer: it sits below the border in normal flow, 12px under the
frame, because on a real contact sheet the caption is typed on the
sheet under the print — and because text that flows can never be
covered by a layer that floats (§10, item 8).

**Sheet header anatomy.** A sheet header is three lines and a rule:
the range line (Desk label: "SHEET 2 · FR. 07–15 OF 36" + the picked
tally right-aligned when non-zero), the title (Display 2), and the
standfirst line when the sheet carries an essay fragment (Body small,
one line, ≤ 90 characters — a sheet header that needs a paragraph is
two sheets). Below, the 2px `--mark-line` rule. Total header height is
fixed per breakpoint (148px / 132px / auto-stacked on mobile) and
reserved in layout, so a tally appearing mid-scroll never shifts a
single frame (CLS 0, §14).

---

## 5. Full motion system

Every motion term, in this theme's own language. One shared
requestAnimationFrame loop with lerp factor `--lerp: 0.12` drives all
scroll-scrubbed values; nothing in this theme runs its own scroll
listener.

**The pitch ladder — the theme's central token system.** Halftone states
are discrete, pre-developed renditions of each photograph, crossfaded —
never a live filter. The ladder is fixed:

| Token | Dot pitch | Reads as |
|---|---|---|
| `--pitch-0` | 22px | Pure abstraction — coins on paper |
| `--pitch-1` | 14px | A suspicion of a picture |
| `--pitch-2` | 9px | The picture, squinted at |
| `--pitch-3` | 5.5px | Newsprint at arm's length |
| `--pitch-4` | 3.5px | Fine screen, nearly resolved |
| `--pitch-5` | 0 | The photograph itself (the sharp original) |

One "dot-frequency step" anywhere in this spec = one rung of this
ladder. All halftone renditions are developed at build time (§14);
the browser only crossfades prints. **Nothing is developed live.**

**Dot geometry.** The renditions are true halftone screens, not dot
*patterns*: round dots on a square grid at the classic **45° screen
angle** for black (the angle at which a single-colour screen is least
visible to the eye — the pipeline's one non-negotiable setting).
Dot area follows image luminance per cell; highlights are pin dots
(≥ 4% area — below that, a newspaper dot drops out entirely, and the
pipeline clips at 4% so skies go honestly to paper), shadows plug at
92% (beyond that, newsprint fills in, and the pipeline lets it —
muddy shadows are the medium telling the truth). Midtones carry an
**8% dot-gain compensation**: press dots grow, and the renditions are
rendered 8% lean in the 40–60% tones so the *perceived* pitch matches
the ladder's nominal values on a calibrated screen. The two shimmer
screens (§6.6) are the exception to the 45° rule — they sit at 15°
and 75°, the colour-separation angles, precisely because their slight
wrongness against the print's own 45° screen is what produces the
moiré shimmer.

**Crossfade weighting.** Adjacent rungs never crossfade linearly. The
outgoing rung's opacity follows `1 − easeDevelop(t)` and the incoming
follows `easeDevelop(t)` over the same window, so the *sum* of dot
coverage stays roughly constant through the handover — a linear fade
dips through a ghostly double-image at the midpoint (two screens at
half strength read as dirt, not as focus), while the eased handover
reads as one screen tightening. This weighting is used identically by
§6.1, §6.2, §6.8, §6.9 and §6.12; it is the theme's single most
important rendering detail, and §10's reviewers check for the dirt
dip by eye on the hero.

**The frame data model.** Every frame carries its darkroom record as
data attributes, authored at content time — this model is what makes
two builders produce the same page:

- `data-frame="12"` — the frame's number on the roll. Unique per page
  (§6.11's registry refuses duplicates). Drives the counter, the
  badge, the marquee and the pick's identity.
- `data-pitches="2,3,4"` — which ladder rungs this frame ships
  (hero: `0,1,2,3,4`; section: `2,3,4`; card: `3,4`). The rendition
  files follow the naming `fr12-p3.webp` beside the base `fr12.webp`.
- `data-crop="6,4,6,10"` — the desk's crop insets (top/right/bottom/
  left, % of the image box) consumed by §6.3; absent = no crop.
- `data-face="0.52,0.38,0.16,0.20"` — face ellipse (cx, cy, rx, ry as
  fractions) consumed by §6.4; up to two ellipses, semicolon-separated;
  absent = the desk circled nobody.
- `data-focal="0.38"` — the subject's vertical position as a fraction,
  consumed by §6.2's focus value on tall frames; defaults to 0.38.
- The caption is *not* data: it is DOM, in the fixed desk form (§12) —
  photographer, place, date, instruction — because captions are
  content for every visitor including those without JavaScript, and
  data attributes are for machines.

A frame missing `data-frame` is a build error, not a default: the
registry (§6.11) counts only numbered frames, and an unnumbered print
on a contact sheet is exactly the kind of quiet wrongness §10 exists
to catch.

**Named easings.**

- `--ease-develop: cubic-bezier(0.22, 0.61, 0.21, 1)` — development:
  fast appearance, long chemical settle. Reveals, crossfade weighting.
- `--ease-fix: cubic-bezier(0.55, 0.06, 0.35, 1)` — fixing: slow commit,
  hard stop. Picks, stamps, the door.
- `--ease-tray: cubic-bezier(0.34, 1.18, 0.4, 1)` — a print lifted and
  set down: 18% overshoot, once. Tray-lift tilt only.
- `--ease-pencil: cubic-bezier(0.4, 0, 0.3, 1)` — the grease pencil's
  near-linear draw with a soft start.

**Duration tokens.** `--dur-draw: 400ms` (crop marks), `--dur-circle:
600ms` (face circle), `--dur-jitter: 150ms` (stamp), `--dur-sharpen:
250ms` (one pitch step), `--dur-pick: 500ms` (full resolve on pick),
`--dur-door: 400ms` (darkroom-door transition), `--dur-tilt: 300ms`,
`--dur-develop: 900ms` (skeleton resolve).

**Term by term.**

- **Scroll-triggered reveals** — grease-pencil reveals (§6.3): a frame's
  crop marks draw, then its clip-path opens. Trigger: frame top crosses
  82% of viewport height. Duration: marks 400ms, clip 600ms
  `--ease-develop`, 60ms apart.
- **Scroll-driven scrub** — the theme's engine. The hero resolve (§6.1)
  and the centre-sharpen band (§6.2) are scrubbed, lerped at 0.12, and
  fully reversible: scrolling back up un-resolves. Distance works both
  ways; a visitor who scrolls back is stepping closer again, and the
  dots honestly grow.
- **Pinned scenes** — one only: the hero portrait pins for 120vh while
  it resolves (§6.1). No other element pins, ever (§10).
- **Parallax** — two layers only, both inside the frame system: frame
  borders and crop marks (the desk's fixed layer) drift at 0.96× scroll
  speed while photographs inside their mats drift at 1.0× — a 4%
  differential, felt as the print settling in its frame, never seen as
  a trick. Maximum offset 10px, clamped.
- **Masked reveals** — crop-mark clip-paths (§6.3): the reveal window is
  the desk's crop, so the mask is content.
- **Blur-to-sharp** — this theme's sharp is *pitch*-to-sharp. A 0.6px
  Gaussian blur accompanies `--pitch-0` and `--pitch-1` only (the eye
  reads coarse dots + slight blur as "too close"); from `--pitch-2` up
  the renditions are unblurred. No other blur exists on the page.
- **Kinetic typography** — restrained to the instruments: the frame
  counter's digit roll (§6.5) and the hero caption rising 12px as the
  face resolves (§6.14). Headlines never animate letter by letter; the
  desk would not allow it.
- **Animated counters** — frame counter and print counts (§6.11), in
  Archivo tabular, counting only real frames and real picks.
- **Progress indicators** — the exposure strip (§6.5): eight bands
  darkening in steps, like a test strip — progress here is *stepped*,
  never a smooth bar, because exposure is stepped.
- **Marquees** — one: the roll-edge marquee in the footer (§6.17),
  film-edge markings travelling at 24px/s, pausing on hover. Nowhere
  else.
- **Ambient loops** — two, both inside the prints: multi-angle dot
  shimmer (§6.6, 8s) and tray-grain breathing in dark bands (opacity
  0.05↔0.09, 7s, `--ease-develop` in/out). Both pause off-screen and
  under `prefers-reduced-motion`.
- **Micro-interactions** — stamp jitter (§6.7, 150ms), pencil-tick on
  picked prints, button press = the print pressed flat (scale 0.99,
  120ms `--ease-fix`).
- **Hover physics** — tray-lift tilt (§6.10) and attention-sharpen
  (§6.8): the two hovers, both about handling a print.
- **Page transitions** — the darkroom door (§6.12): fade through
  `--tray-deep` black in 400ms, next page's first print fades up
  already sharp.
- **Image treatments** — scale-in-frame is literal: in this theme an
  image's scale *is* its pitch (§6.1, §6.2). Images never zoom for
  decoration; a scale change always means a focus change.

---

## 6. Signature elements

### 6.1 Scroll-out resolve (the inversion)

- **What & why.** The theme's signature and its thesis performed. The
  hero portrait begins as a field of huge abstract dots — pitch
  `--pitch-0`, 22px, no face findable — pinned full-viewport. Scrolling
  does what stepping back from a newspaper photograph does: the portrait
  scales *down* (1.6 → 1.0) and its pitch climbs the ladder in
  proportion, until at the end of 120vh of scroll the dots resolve into
  the photographer's face at reading distance and the pin releases into
  the contact sheets. Every other site zooms in to show detail; this one
  zooms out to show the picture. If a visitor does only this, they have
  understood the site.
- **Structure.** A `<section class="hero-frame">` of 220vh: a 100vh
  sticky stage holding one frame (2px border, 12px mat) containing the
  base `<img>` (the sharp portrait — always the DOM image, always with
  full alt text) and a stack of halftone rendition overlays
  (`--pitch-0`…`--pitch-4`), each an `<img>` of the pre-developed
  rendition, `aria-hidden`, absolutely positioned over the base. The
  whole frame scales; overlay opacities crossfade pairwise. Beside the
  frame (≥1200px) or beneath it (<1200px), the essay title and the
  scroll instruction in desk type: "SCROLL TO STEP BACK."
- **Motion spec.** Scroll progress `p` over the 120vh scrub range,
  lerped at `--lerp` in the shared loop. Frame scale: `1.6 − 0.6p`.
  Pitch mapping: `p` 0–0.2 → `--pitch-0` dominant; each 0.2 band hands
  over to the next rung with a 0.08 crossfade overlap weighted by
  `--ease-develop`. Blur: 0.6px at `p < 0.25`, easing to 0 by `p = 0.4`.
  At `p = 1` all overlays are at opacity 0 — what remains is the
  photograph itself, unscaled, in its frame. The pin releases; the
  frame counter (§6.5) starts counting from FR. 01.
- **Choreography timeline (v2).** Page load → hero renders at
  `--pitch-0`, scale 1.6, overlays armed → first scroll input → within
  one frame (≤16ms) the loop begins moving `p` → `p` 0.2: pitch-0 fades
  1→0.25 as pitch-1 rises → `p` 0.45: a suspicion of the face (pitch-2)
  → `p` 0.7: the face is findable (pitch-3) → `p` 0.9: pitch-4, nearly
  print → `p` 1.0: overlays gone, scale 1.0, pin releases over the next
  40vh of section tail → the hero caption (§6.14) has risen its 12px
  across the same range. Total visitor time: one deliberate scroll,
  ≈2.5–4s. The resolve never auto-plays; distance is the visitor's act.
- **State matrix (v2).** *Rest (top of page):* abstract dot field,
  scale 1.6 — desktop and touch identical. *Hover:* none (the hero is
  not a control). *Focus:* the hero contains no focusable element except
  the essay link in its caption block, which never affects the scrub.
  *Active:* n/a. *Scrolled-past:* the portrait sits sharp in its frame
  at the top of sheet 1's flow; scrolling back re-enters the scrub and
  the dots return — the state is a pure function of scroll position.
  *Disabled (no JS):* overlays are never inserted; the sharp portrait
  shows at scale 1.0 in a normal 100vh section. That is the designed
  disabled state, not an error.
- **Content merge.** The dots are the portrait's own screen and the
  scale is the visitor's distance from it — the essay's subject (how
  seeing works) is operated by the reader's own hand. Remove the
  animation and the hero is a framed portrait with a title: poorer,
  never broken.
- **Failure fallback.** The standing 800ms law, inherited from the
  original entry: if scroll position becomes unreadable, or the shared
  loop stalls for 800ms, or rendition images fail to load, all overlays
  clear (opacity 0, then `display:none`) and the sharp portrait stands.
  A watchdog owns this; `transitionend` never does.
- **Reduced-motion variant.** No pin, no scrub, no scale: the hero is a
  static 100vh section with the sharp portrait in its frame and the
  title beside it. The essay loses its demonstration and keeps its
  subject — the caption (§12) carries the sentence "You are standing at
  reading distance" so the idea survives without the motion.
- **Breakpoints (v2).** ≥1200px: as specced, title beside the frame,
  frame at 62vh height. 768–1199px: title moves beneath the frame;
  scrub range shortens to 100vh; scale range 1.45 → 1. <768px: scrub
  range 80vh, scale 1.3 → 1, frame full-bleed width with mat reduced to
  8px; the pitch ladder drops `--pitch-1` (crossfades 0→2 directly) to
  halve compositing cost on phones.
- **Edge cases & failure modes (v2).** *Scroll-back:* fully reversible,
  no hysteresis — `p` is scroll position, nothing is latched. *Fast
  fling to page bottom:* the loop's lerp settles `p` to its true value;
  overlays crossfade quickly but never stick mid-ladder — a settle
  timer forces the exact rung for the final `p` within 300ms of scroll
  rest. *Very tall portrait:* the frame crops by the desk's crop (§6.3
  marks show the crop); the face must sit in the frame's upper two-
  thirds — a content rule, checked at the gate (§10). *Rendition 404:*
  that rung is skipped in the mapping; two consecutive missing rungs
  trigger the full fallback. *Low-power device:* if the loop measures
  sustained <40fps, the ladder collapses to 3 rungs (0, 3, 5) and the
  scale animation is dropped — pitch alone still performs the thesis.
- **Accessibility spec (v2).** The base `<img>` carries the portrait's
  real alt text; overlays are `aria-hidden` and `alt=""`. Screen-reader
  order: essay title → portrait → caption. The scrub is scroll-driven
  and therefore free of focus requirements; no content is reachable
  only by scrolling the pin (the caption block after the hero repeats
  the hero's links). `prefers-reduced-motion` gets the static hero
  above. The dot field at `--pitch-0` is decorative abstraction to a
  screen reader and is announced as nothing — correct, because the
  *photograph* is what is announced.
- **Performance budget & mobile variant.** Six renditions of one image:
  hero rendition set ≤ 900KB total (§14), each rendition at 0.75×
  display resolution (dots mask the difference). Compositing: at most 2
  overlays non-transparent at once; the rest are `visibility:hidden`.
  Loop cost ≤ 1.2ms/frame for this element. Mobile variant: the 4-rung
  ladder and 80vh scrub above; rendition set ≤ 480KB.
- **Tokens consumed (v2).** `--paper`, `--dot`, `--mark-line`,
  `--pitch-0`…`--pitch-5`, `--lerp`, `--ease-develop`, `--fixer-deep`
  (scroll instruction), `--dur-develop`.

### 6.2 Centre-sharpen frequency crossfade

- **What & why.** Every photograph on every sheet lives in a focus band
  that travels with the reading eye. As a frame approaches the viewport
  it is coarse; exactly at viewport centre it is at its sharpest;
  leaving, it dissolves back toward dots. Attention is focus, applied
  continuously to the whole sheet — the reader never has to ask a
  picture to resolve; looking at it *is* resolving it.
- **Structure.** Each section image is the same stack as the hero in
  miniature: base sharp `<img>` plus JS-inserted rendition overlays at
  `--pitch-2`, `--pitch-3`, `--pitch-4` (section images enter the ladder
  at rung 2 — they were never meant to be pure abstraction). A
  `data-frame` wrapper carries the frame number that §6.5 counts.
- **Motion spec.** Per frame, focus value `f = 1 − |frameCentre −
  viewportCentre| / (0.75 × viewportHeight)`, clamped 0–1, computed in
  the shared loop from cached positions (recomputed on resize only).
  `f` maps to the ladder: `f < 0.35` → pitch-2 dominant; 0.35–0.7 →
  pitch-3 → pitch-4 crossfade; `f > 0.85` → overlays at 0, the sharp
  photograph. Crossfade weighting uses `--ease-develop`. A frame at
  rest far off-screen holds pitch-2 at full overlay — the sheet reads
  as a field of soft prints until approached.
- **Choreography timeline (v2).** Frame enters viewport bottom →
  overlay pitch-2 at 1.0 → frame centre travels the lower third: pitch-3
  rises 0→0.6 → centre band (±12% of viewport height around centre):
  pitch-4 flashes through and clears, image sharp for exactly the
  centre pass → face-circle (§6.4) and stamp (§6.7) fire their one-shot
  triggers inside this band → frame exits upward: the ladder reverses,
  pitch-2 restored by the time the frame is 25% out. Full pass at
  reading speed: ≈1.8s per frame.
- **State matrix (v2).** *Rest (off-screen):* pitch-2 overlay full.
  *Hover:* §6.8 takes precedence — hover forces one rung sharper than
  the scroll value while hovered. *Focus:* keyboard focus on a frame's
  link forces the frame to full sharp (overlays 0 over `--dur-sharpen`)
  for as long as focus is within — a focused picture is an attended
  picture. *Active:* §6.9 pick locks sharp permanently. *Scrolled-past:*
  pitch-2 restored (the band has moved on). *Disabled:* no overlays;
  every image sharp.
- **Content merge.** Sharpness is a property of the print and of the
  reader's position — the two things the essay is about. The band is
  not an effect applied to images; it is the page's model of attention,
  and the copy says so (§12).
- **Failure fallback.** Same 800ms law as §6.1: loop stall, unreadable
  positions, or missing renditions → overlays clear, all images sharp.
  A frame whose rendition set partially fails degrades to the rungs it
  has; a frame with no renditions is simply sharp.
- **Reduced-motion variant.** No band, no crossfade: all images render
  sharp at all scroll positions. The centre-pass one-shots (§6.4, §6.7)
  are pre-applied in their final state.
- **Breakpoints (v2).** ≥1200px: 3-rung ladder as specced. 768–1199px:
  2 rungs (pitch-3, sharp) — the band still travels, cheaper.
  <768px: 2 rungs, and the focus band widens (divisor 0.9 × viewport
  height) because a phone frame occupies more of the viewport.
- **Edge cases & failure modes (v2).** *Frames taller than the
  viewport:* `f` is computed from the frame's *focal point* (the face
  or subject point stored in `data-focal`, defaulting to 38% from top)
  instead of its centre — a tall print sharpens when its subject is
  centred, not when its middle is. *Scroll-back:* the ladder reverses
  exactly; no frame is ever left sharper than its position earns,
  except picked prints (§6.9), which stay sharp by the visitor's own
  act. *Grid reflow on resize:* positions recache within one frame;
  overlays hold their last state during the resize frame — no flash of
  mixed pitches. *Many frames:* only frames within 1.5 viewports of
  the viewport have overlays attached at all (§14); the rest are bare
  sharp images until approached.
- **Accessibility spec (v2).** Overlays `aria-hidden`; base images keep
  their alt text. Focus-forces-sharp (above) guarantees keyboard users
  never tab to a dotted picture. The focus band is not announced — it
  is presentation, and the sharp state it produces is the content's
  default for assistive technology at all times.
- **Performance budget & mobile variant.** Per frame: ≤3 overlays,
  ≤0.3ms/frame loop cost, ≤6 frames live at once. Renditions per
  section image ≤ 180KB total (§14). Mobile variant: the 2-rung ladder
  and ≤4 live frames.
- **Tokens consumed (v2).** `--pitch-2`, `--pitch-3`, `--pitch-4`,
  `--pitch-5`, `--lerp`, `--ease-develop`, `--dur-sharpen`.

### 6.3 Grease-pencil reveal

- **What & why.** A frame does not fade in like a web image; it is
  *marked up* like a print on the desk. Just before a frame enters, its
  grease-pencil crop marks draw themselves on the mat — four corner
  ticks and the crop line in fixer amber — and then the photograph
  reveals through the clip-path those marks describe. The reveal window
  is the desk's actual instruction for this print: what the desk said
  to keep is what the visitor gets.
- **Structure.** An inline SVG per frame, absolutely positioned over
  the mat, carrying the crop-mark paths (corner ticks 18px, crop
  rectangle inset per the frame's real crop data in `data-crop`). The
  image wrapper's `clip-path: inset()` starts at the full mat and
  animates to the crop inset. Marks are drawn with `stroke-dashoffset`
  in `--fixer`, 3px stroke, round caps, with a deliberate 1–2px hand
  wobble baked into the path data — the wobble is authored per frame
  from a seeded variation, never random per load (the desk's hand is
  consistent).
- **Motion spec.** Trigger: frame top crosses 82% viewport height.
  Marks draw over `--dur-draw` (400ms, `--ease-pencil`), corners in
  reading order (TL, TR, BR, BL), 40ms stagger. 60ms after the last
  mark, the clip-path opens from full-mat to crop inset over 600ms
  `--ease-develop`. The frame's §6.2 overlays arm only after the clip
  completes — a print is cropped before it is focused.
- **Choreography timeline (v2).** t=0 trigger → t=0–400ms marks draw
  (4 × ~85ms + staggers) → t=460ms clip begins → t=1060ms crop reached,
  photograph fully revealed inside its crop → t=1100ms §6.2 band takes
  over the frame. Total ≈1.1s, once per frame per page load; scrolling
  back up never un-draws the marks (the desk does not un-mark a print).
- **State matrix (v2).** *Rest (pre-trigger):* frame shows its
  photograph at pitch-2 inside the full mat, marks undrawn — visible,
  readable, unrevealed in the theme's sense. *Hover:* no state (marks
  are not controls). *Focus:* focus within the frame draws the marks
  instantly (no 400ms wait) if not yet drawn. *Active:* n/a.
  *Scrolled-past:* marks drawn, clip at crop — permanent. *Disabled:*
  marks rendered fully drawn in the static HTML (they are content —
  the crop is real), clip at crop from first paint.
- **Content merge.** The crop marks carry the frame's real crop: the
  `data-crop` values are the same insets the layout uses. A frame with
  no crop instruction gets corner ticks only and a full-mat reveal —
  the desk left it alone, and the page shows that too.
- **Failure fallback.** If the SVG fails or JS is absent, the frame is
  simply there: photograph visible, marks pre-drawn in static markup
  (the no-JS HTML ships marks drawn and clip at final inset). The
  animation is the drawing, never the existence, of the marks.
- **Reduced-motion variant.** Marks pre-drawn, clip at crop, no draw
  animation — identical final state from first paint.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: marks draw in
  300ms (smaller mats, shorter paths). <768px: mat is 8px; crop marks
  shrink to 12px ticks and draw in 250ms; frames with `data-crop`
  insets under 4% skip the clip animation (imperceptible) but keep the
  marks.
- **Edge cases & failure modes (v2).** *Frame enters during a fast
  fling:* triggers batch — marks for frames that entered more than
  600ms ago are set drawn instantly rather than queueing a backlog of
  drawings behind the scroll. *Re-entry after tab switch:* drawn state
  persists; nothing re-draws. *Crop data missing:* treated as no-crop
  (corner ticks only) — never invent a crop. *SVG path length
  mis-measure:* dash lengths are computed from `getTotalLength()` at
  arm time, not hardcoded, so a restyled mat cannot desync the draw.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the crop is
  conveyed to assistive technology by the caption, which includes the
  desk instruction in text ("Cropped to the hands, per the desk").
  Focus order is unaffected (marks are not focusable). Amber marks at
  3px on paper meet the 3:1 graphical-object bar against the mat
  because they are drawn over the photograph's edge and the mat
  together; where a mark lies wholly on light photograph tones, a 1px
  `--dot` underlay path at 25% opacity guarantees the line reads —
  grease pencil over a pale sky is a real darkroom problem and the
  spec treats it as one.
- **Performance budget & mobile variant.** One SVG (≤ 6 paths) per
  frame, one clip-path animation per frame, once. ≤ 0.2ms/frame while
  drawing. Mobile variant: shorter draws above; SVGs are inline and
  shared-symbol where crops repeat.
- **Tokens consumed (v2).** `--fixer`, `--dot`, `--dur-draw`,
  `--ease-pencil`, `--ease-develop`, `--mark-line`.

### 6.4 Face-circle draw

- **What & why.** On portraits, the desk circles the face. The first
  time a portrait reaches full sharpness — its centre pass, §6.2 — a
  grease-pencil ellipse draws itself around the face on the print:
  slightly imperfect, overlapping its own start by a few degrees, the
  way a hand actually closes a circle. It is the theme's most emotional
  element and its most restrained: one circle, on the chosen face, once.
- **Structure.** An SVG ellipse path inside the frame's mark layer
  (§6.3), positioned from the frame's face data (`data-face="x,y,rx,ry"`
  as fractions of the image box — authored per portrait, never
  auto-detected at runtime). Stroke `--fixer`, 3px, drawn by
  dashoffset over `--dur-circle`. The ellipse path is generated with a
  3% radius wobble and a 12° overshoot past the close point.
- **Motion spec.** Trigger: the frame's first arrival at full sharpness
  (`f > 0.85` in §6.2's band, or a §6.9 pick). Draw: 600ms
  `--ease-pencil`, starting 120ms after sharpness is reached (the desk
  looks first, then circles). The circle persists for the rest of the
  page view at 88% opacity.
- **Choreography timeline (v2).** t=0 frame reaches full sharp →
  t=120ms pencil touches down at the ellipse's top → t=120–720ms the
  ellipse draws clockwise, overshooting its start by 12° → t=720ms
  pencil lifts; the overlap segment fades from 100% to 88% over 200ms
  (the double-struck part of a real circle dries darker, then evens)
  → static thereafter.
- **State matrix (v2).** *Rest:* no circle until first sharp pass.
  *Hover:* the circle deepens to 100% opacity while its frame is
  hovered (the desk's hand returns to its mark). *Focus:* focus within
  the frame draws the circle instantly if undrawn. *Active:* n/a.
  *Scrolled-past:* circle remains drawn — scroll position never erases
  an annotation. *Disabled:* circles are present in static markup on
  portraits the desk circled (an editorial fact), drawn from first
  paint.
- **Content merge.** The circle is an annotation *on* the photograph,
  *about* the photograph — it identifies the face the essay is about.
  Portraits where the face is not the subject get no circle; the
  absence is also editorial. A page may carry at most 3 circles (§10).
- **Failure fallback.** No face data → no circle, silently. SVG failure
  → no circle; the portrait and caption are complete without it. The
  circle is the one element whose absence never needs a substitute.
- **Reduced-motion variant.** The circle appears fully drawn (fade-in
  0ms — present from the frame's first sharp render, which under
  reduced motion is first paint).
- **Breakpoints (v2).** Identical at all sizes; on <768px the stroke
  stays 3px (a phone is held closer; the mark must not thin away).
  Ellipse geometry is fractional, so it tracks the image box at every
  breakpoint without re-authoring.
- **Edge cases & failure modes (v2).** *Multiple faces:* `data-face`
  may carry up to 2 ellipses (a two-shot); the second draws 150ms after
  the first, and §10 caps the page total. *Face near the crop edge:*
  the ellipse clips at the crop inset — a half-circle at the frame's
  edge is honest darkroom practice and is kept, not "fixed".
  *Re-sharpening:* the draw fires once; later centre passes only
  restore opacity. *Picked print (§6.9):* picking an uncircled portrait
  also triggers the draw — the visitor's pick is the desk's attention.
- **Accessibility spec (v2).** `aria-hidden` decoration; the caption of
  a circled portrait names the subject ("The circle is the desk's: the
  face is the photographer's mother"), so the annotation's meaning is
  in text for every visitor. Contrast: as §6.3, with the underlay rule
  on pale image areas.
- **Performance budget & mobile variant.** One path, one 600ms draw,
  once per portrait. Negligible. No cheaper variant needed; the mobile
  cost is identical.
- **Tokens consumed (v2).** `--fixer`, `--dur-circle`, `--ease-pencil`.

### 6.5 Frame-counter + exposure-strip progress

- **What & why.** Progress on a contact sheet is not a percentage; it
  is *which frame you are on* and *how much of the roll is exposed*.
  The margin rail carries both instruments. The frame counter reads
  `FR. n / 36` and ticks as each frame's focal point passes viewport
  centre. The exposure strip — a vertical test strip of eight bands —
  darkens band by band as the page is read, each band one stop denser
  than the last, exactly like the test strip a printer pins beside the
  tray to judge exposure. Together they measure this sheet's own
  frames, nothing else.
- **Structure.** Rail (`<aside class="rail">`, fixed, ≥1200px; a
  compact header variant below that, §6.13): counter in Archivo tabular
  (`FR. <span id>07</span> / 36`), and the strip: 8 stacked bands, each
  a `<div>` whose background is a stepped mix of `--paper` → `--dot`
  (band k final density = k/8). The active band's edge is ruled in
  `--fixer`. Both instruments are driven by the shared loop from the
  same scroll value; the counter's `n` is *counted from the DOM* —
  frames with `data-frame` whose focal point has passed centre — never
  from a hardcoded total.
- **Motion spec.** Counter: on tick, the digit pair rolls 120ms
  (translateY −100% → 0 through a masked window, `--ease-fix`) — a
  mechanical counter's flick, not a fade. Strip: band k activates when
  overall page progress passes k/8; activation is a 300ms
  `--ease-develop` density settle (a band *developing* to its stop),
  stepped — bands never partially darken between stops at rest.
- **Choreography timeline (v2).** Scroll → frame focal crosses centre
  → within the same loop frame, counter rolls (120ms) and, if the
  crossing also passes a strip threshold, the band begins its 300ms
  settle → at page end: counter reads the true final frame, strip is
  fully exposed, and the footer's roll-edge (§6.17) shows the same
  final count — the instruments agree, always.
- **State matrix (v2).** *Rest:* counter at FR. 01 (or the first
  frame's number), strip at band 0. *Hover:* the strip is a control
  only in its header variant (clicking a band jumps to that eighth of
  the page — a test strip you can point at); the rail strip is
  read-only. *Focus:* header-variant bands are buttons with visible
  focus (2px `--fixer-deep` outline, offset 2px). *Active:* pressed
  band inks immediately. *Scrolled-past:* instruments hold their true
  values — scrolling back *decrements* the counter and un-develops
  bands (exposure here is a reading position, not an achievement).
  *Disabled:* the counter renders as static text "36 FRAMES" in the
  sheet header; the strip renders fully exposed as a graphic.
- **Content merge.** Both instruments enumerate this page's actual
  frames. A page with 23 frames reads / 23 — the 36 in the original
  entry is a roll of film, and the spec keeps the honesty: the total is
  the page's real frame count, presented in the roll's language.
- **Failure fallback.** If the loop fails, the instruments freeze at
  their last true values; if JS is absent, the static variants above.
  A frozen counter is a broken instrument and §10 fails it — the
  fallback is for the visitor, not for the builder.
- **Reduced-motion variant.** Counter changes instantly (no roll);
  bands snap to their stop (no settle). Values identical.
- **Breakpoints (v2).** ≥1200px: full rail as specced. 768–1199px: the
  rail collapses to the header variant — counter + a horizontal
  8-band strip in the sticky header (§6.13). <768px: counter only, in
  the header; the strip is omitted (a phone's header cannot hold both
  honestly) and the footer's static strip graphic closes the page
  instead.
- **Edge cases & failure modes (v2).** *Pages with fewer than 8
  frames:* bands map to progress eighths regardless — the strip
  measures the *page*, the counter measures *frames*; their decoupling
  is deliberate and documented in the caption beside the rail ("The
  strip times the reading; the counter counts the frames"). *Frames
  added by filtering (§6.15):* the counter recounts from the DOM on
  every filter change; a counter that disagrees with the visible sheet
  is a §10 failure. *Jump scroll (End key):* instruments settle to
  true values within 300ms; bands may settle in cascade (40ms stagger)
  rather than teleporting — the one place a cascade is allowed.
- **Accessibility spec (v2).** The rail is `aria-hidden` as an
  instrument *display*; its information is duplicated accessibly: a
  visually-hidden live region announces sheet changes ("Sheet 2 of 4")
  on sheet boundaries only — never per frame (36 announcements is a
  harassment, not a feature). Header-variant bands are real buttons
  with labels ("Go to the halfway point — frame 18"). Contrast: strip
  bands are graphics; the counter text is `--dot` on `--paper` at
  15.5:1.
- **Performance budget & mobile variant.** Two small DOM writes per
  loop frame at most, and only on change. Negligible compositing.
  Mobile variant: the header counter above.
- **Tokens consumed (v2).** `--dot`, `--paper`, `--fixer`,
  `--fixer-deep`, `--tray`, `--ease-fix`, `--ease-develop`, `--lerp`.

### 6.6 Multi-angle dot shimmer

- **What & why.** Lay two halftone screens at slightly wrong angles and
  the dots interfere — moiré, the darkroom's beautiful accident. On the
  page's largest prints, two overlaid screens rotate ±0.4° against each
  other in an 8-second loop, and the dot field breathes with a faint,
  living shimmer. In tray-dark sections, a teal grain breathes instead.
  This is the theme's only purely ambient motion, and it lives *inside
  the prints* — the shimmer is in the paper, not on the page.
- **Structure.** A shimmer layer inside qualifying frames (hero +
  frames ≥ 480px wide): two absolutely-positioned overlays, each a
  repeating radial-gradient dot pattern matched to the frame's current
  pitch, at screen angles 15° and 75° (the classic separation angles),
  rotating in opposite directions. In tray bands, a grain layer
  (SVG feTurbulence noise, `--tray`-tinted) with an opacity loop.
- **Motion spec.** Rotation: ±0.4° peak, sinusoidal, 8s period, the two
  screens counter-rotating. Overlay opacity: 0.05–0.09, peaking
  mid-cycle. Grain: opacity 0.05 ↔ 0.09 over 7s `--ease-develop`
  in/out. Both loops run only while their frame is in the viewport
  (IntersectionObserver gates the class; the shared loop advances the
  phase).
- **Choreography timeline (v2).** Frame enters viewport → shimmer
  fades in over 600ms (never pops) → 8s cycles continue, phase-locked
  across frames so the whole sheet breathes together → frame leaves →
  400ms fade out, phase preserved for re-entry.
- **State matrix (v2).** *Rest:* shimmer running at low opacity.
  *Hover:* pauses on the hovered frame (a print held still for
  inspection — §6.8's companion). *Focus:* pauses on the focused
  frame. *Active:* n/a. *Scrolled-past:* gated off. *Disabled:* no
  shimmer layers inserted.
- **Content merge.** The shimmer is a property of the print's screen —
  it exists only where dots exist, at the dots' own pitch, inside the
  frame's mat. It never touches type, never crosses a frame border.
- **Failure fallback.** Absent layers = static prints. Any failure
  mode (gradient unsupported, observer absent) degrades to stillness,
  which this theme always prefers to a broken effect.
- **Reduced-motion variant.** No shimmer, no grain loop. Both layers
  omitted entirely — not frozen mid-cycle, *omitted*.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: shimmer only
  on the hero and full-width frames. <768px: shimmer off (small
  screens strobing is a defect, not an effect); grain breathing in
  tray bands remains, at half amplitude.
- **Edge cases & failure modes (v2).** *Moiré strobing:* if the two
  screens' interference produces a visible beat pattern stronger than
  the dots themselves (checked at the gate on real devices, §10), the
  rotation amplitude halves to ±0.2° for that frame size — the spec's
  ceiling is taste, measured on hardware, not in a design tool.
  *Photosensitivity:* the loop is slow (8s) and low-contrast by
  construction; it never flashes — luminance change per frame is under
  1%. *Battery:* loops gate off when the tab is hidden and when
  `prefers-reduced-data`/battery-saver signals are present where
  detectable.
- **Accessibility spec (v2).** `aria-hidden`, pointer-events none.
  Under reduced-motion: omitted (above). The shimmer never carries
  information; a visitor who never sees it has the complete page.
- **Performance budget & mobile variant.** Two gradient layers per
  qualifying frame, transform-only animation, ≤ 4 frames shimmering
  simultaneously (§14 cut order removes this element first). Mobile:
  off, as specced.
- **Tokens consumed (v2).** `--pitch-*` (matched per frame), `--tray`,
  `--paper`, `--lerp`.

### 6.7 "Not to be cropped" stamp jitter

- **What & why.** Every caption on the desk's sheets carries the
  standing instruction as a small printed stamp: NOT TO BE CROPPED.
  The first time its caption becomes fully sharp — the frame's centre
  pass — the stamp jitters once: a 1° rotation shake over 150ms, like
  the sheet being tapped on the desk. Defiant, tiny, and once only. It
  is the desk insisting, at the exact moment the visitor finally sees
  the picture properly, that the picture be left as it was made.
- **Structure.** A `<span class="stamp">` inside the caption block:
  Archivo 600, 10.5px, uppercase, `--fixer-deep` text (the amber that
  passes contrast, §2), double border (2px outer, 1px inner) in
  `--fixer-deep` at 80%, padding 3px 7px, rotated −1.5° at rest (a
  stamp is struck by hand; it is never level). Frames the desk *did*
  crop carry instead the stamp CROPPED AS MARKED — the instruction is
  per-frame data, not wallpaper (§9).
- **Motion spec.** Trigger: the frame's first full-sharp moment
  (§6.2 `f > 0.85`, or pick §6.9). Jitter: rotate −1.5° → −0.5° →
  −2.2° → −1.5° over `--dur-jitter` (150ms, linear keyframes — a tap
  has no easing). Once per frame per page view.
- **Choreography timeline (v2).** t=0 sharp reached → t=80ms jitter
  begins (the desk reacts *after* seeing) → t=230ms stamp at rest,
  −1.5°, forever. If the face-circle (§6.4) fires on the same frame,
  the circle draws first (120ms delay, 600ms) and the jitter waits
  until t=720ms — the desk circles the face, *then* taps the sheet.
- **State matrix (v2).** *Rest:* stamp present, level-off at −1.5°,
  from first paint — the stamp is print, not animation. *Hover:* no
  state. *Focus:* no state. *Active:* n/a. *Scrolled-past:* jitter
  already spent; stamp static. *Disabled:* stamp present, static —
  identical to rest, because rest was already print.
- **Content merge.** The stamp is part of the caption — the desk's real
  instruction about this frame, in the caption's own type block. It is
  never a badge, sticker or corner ribbon; it sits in the caption line
  where a stamp on a contact sheet sits.
- **Failure fallback.** None needed and none permitted: the element is
  static-first. If JS never runs, the stamp is simply a stamp.
- **Reduced-motion variant.** No jitter. The stamp is print; reduced
  motion removes only the tap.
- **Breakpoints (v2).** Identical at all sizes. On <768px captions
  stack (name line, then instruction line with the stamp) — the stamp
  keeps its size and rotation; it is never shrunk below 10.5px text.
- **Edge cases & failure modes (v2).** *Frames whose sharp moment
  never comes* (a frame the visitor scrolls past too fast to centre):
  the jitter fires on the frame's *exit* centre-crossing instead —
  every stamp taps exactly once, on whichever pass first centres the
  frame, in either direction. *Many stamps on screen:* jitters are
  staggered by the motion queue at ≥90ms apart — a sheet of stamps
  tapping in ripple reads as the desk working down the sheet; a
  simultaneous dozen reads as a glitch. *Repeat visits:* once per page
  view, by design; the desk re-stamps a fresh sheet.
- **Accessibility spec (v2).** The stamp is real text in the caption,
  read by screen readers as part of the instruction ("Not to be
  cropped"). The jitter is `aria-hidden` motion on a text element —
  no information moves, only emphasis. Contrast: `--fixer-deep` on
  `--paper` ≈4.9:1 at 10.5px bold — passes AA for the stamp's large-
  text-equivalent weight class; the gate (§10) verifies with a checker,
  not by eye.
- **Performance budget & mobile variant.** One 150ms transform on one
  small element, once per frame. Negligible at every size.
- **Tokens consumed (v2).** `--fixer-deep`, `--fixer`, `--dur-jitter`.

### 6.8 Attention-sharpen hover

- **What & why.** Hover is attention, and attention in this theme is
  focus. Resting the pointer on a frame sharpens it exactly one
  dot-frequency step — pitch drops one rung (a 30% finer screen) — and
  leaving lets it relax back. It is the smallest possible performance
  of the theme's thesis: the picture responds to being looked at, by
  one measured step, never all the way. Full sharpness must be earned
  by position (§6.2) or by picking (§6.9); hover is a lean-in, not a
  claim.
- **Structure.** No new DOM: the element drives the frame's existing
  §6.2 overlay stack. A `data-hover-rung` offset is applied to the
  frame's current scroll-driven rung while hovered (or while the frame
  contains focus, §6.2's focus rule, which goes further — to sharp).
- **Motion spec.** On hover enter: crossfade one rung over
  `--dur-sharpen` (250ms, `--ease-develop`). On leave: relax back over
  350ms (attention leaves more slowly than it arrives — a print
  settling back onto the sheet). If the scroll band changes rung
  mid-hover, the hover offset applies to the new rung seamlessly.
- **Choreography timeline (v2).** t=0 pointer enters frame → t=0–250ms
  one-rung crossfade → held while hovered (shimmer on this frame
  pauses, §6.6 — a held print is a still print) → t=leave → 350ms
  relax → frame returns to its scroll-earned state.
- **State matrix (v2).** *Rest:* scroll state. *Hover:* +1 rung.
  *Focus:* full sharp (§6.2), stronger than hover, and wins while both
  apply. *Active (mid-pick):* §6.9's 500ms resolve overrides.
  *Scrolled-past:* hover still applies (+1 rung from pitch-2) — a
  visitor reaching back up the sheet can still lean into a frame.
  *Disabled:* no overlays, no hover effect; the image is sharp.
- **Content merge.** The sharpening happens to the photograph itself,
  in its own screen. There is no glow, lift or shadow pretending to be
  attention — the picture gets clearer, which is what attention *is*.
- **Failure fallback.** If overlays are absent or cleared (the 800ms
  law), hover does nothing and nothing looks broken — the frame is
  already sharp.
- **Reduced-motion variant.** Hover changes nothing. (A crossfade is
  motion; the theme does not smuggle it back as an "instant" state
  change either — under reduced motion the frame's state is its scroll
  state, full stop.)
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced.
  <768px / touch: **no hover sharpen** — touch has no hover, and a
  tap is reserved for picking (§6.9). Emulated hover on tap is
  explicitly forbidden: it makes the first tap lie about the second.
- **Edge cases & failure modes (v2).** *Pointer crossing a grid
  quickly:* a 60ms hover-intent delay before the crossfade starts —
  sweeping the sheet must not strobe a dozen frames. *Frame at pitch-5
  already (picked or centred):* hover is a no-op; the offset clamps at
  the ladder's top. *Pointer leaves mid-crossfade:* the relax starts
  from the current crossfade weights, never snaps.
- **Accessibility spec (v2).** Hover carries no information — it is
  emphasis only; everything hover reveals is available by scroll,
  focus or pick. Keyboard parity is via the stronger focus rule. No
  focus outline is ever suppressed on frames: 2px `--fixer-deep`
  outline, 2px offset, on the frame border.
- **Performance budget & mobile variant.** Reuses §6.2's stack; one
  crossfade. Mobile variant: element absent (above).
- **Tokens consumed (v2).** `--pitch-*`, `--dur-sharpen`,
  `--ease-develop`, `--fixer-deep`.

### 6.9 Pick-a-print click

- **What & why.** A contact sheet exists to be chosen from. Clicking a
  frame *picks* it: the print resolves to full sharpness — every rung
  at once, the whole ladder climbed in one gesture — and its full
  photo-desk caption expands beneath it: photographer, place, date,
  the crop instruction, and the print's availability line. Picking is
  the theme's primary interaction and its conversion seed: a picked
  print is the one the visitor can request (§6.16 pre-fills from it).
- **Structure.** The frame is a `<button class="frame-pick">` wrapping
  the frame visual (or a real button in the caption row on grids where
  the whole-frame button harms layout — one pattern per site, chosen
  at build). Picked state: `aria-pressed="true"`, a pencil tick (§6.3's
  mark language, drawn 200ms) appears on the mat's corner, the frame's
  overlays clear permanently, and the caption region expands
  (grid-template-rows 0fr → 1fr, 400ms `--ease-fix`). Print count
  (§6.11) increments.
- **Motion spec.** Resolve: all overlays crossfade to 0 over
  `--dur-pick` (500ms, `--ease-develop`), rung weights collapsing in
  ladder order (coarsest clears first — the print comes up through its
  frequencies). Caption expansion starts at t=200ms so the eye lands
  on sharpness first, words second. Unpicking (second click) reverses:
  caption closes 300ms, overlays restore to the frame's current
  scroll-earned rung over 400ms — the print goes back on the sheet.
- **Choreography timeline (v2).** t=0 click → t=0–500ms resolve
  cascade → t=200ms caption begins opening → t=600ms caption fully
  open, tick drawn on the mat → t=600ms the request form (§6.16), if
  present on the page, updates its print reference line. Total ≈0.6s,
  feeling like a print being pulled from the sheet and read.
- **State matrix (v2).** *Rest:* unpicked, scroll-state sharpness.
  *Hover:* §6.8's lean-in, plus the frame's cursor affordance is the
  normal system pointer (standing rule: cursor unchanged — the frame
  border thickens 2px → 3px on hover instead of any cursor trick).
  *Focus:* full sharp (§6.2) + visible outline. *Active:* the press —
  frame scales 0.99 for 120ms `--ease-fix`. *Scrolled-past:* a picked
  print stays picked and stays sharp — the visitor's act outranks the
  focus band, permanently, until unpicked. *Disabled:* picking still
  works without animation (caption expands instantly, image already
  sharp); with JS absent, captions ship expanded and the pick is a
  plain link to the print's detail page.
- **Content merge.** The pick operates on the print and reveals the
  print's own caption — the interaction *is* the contact sheet's real
  use. The expanded caption is content that exists in the DOM from
  first paint (collapsed by the grid-rows technique, never
  `display:none`-authored-away), so no-JS and screen-reader visitors
  lose nothing.
- **Failure fallback.** Overlay failure → the pick still expands the
  caption and draws the tick; the image was already sharp. The
  interaction degrades to an accordion and remains fully meaningful.
- **Reduced-motion variant.** Pick toggles instantly: caption open,
  tick present, image sharp. No cascade.
- **Breakpoints (v2).** ≥1200px: caption expands in place within the
  grid cell; the grid does not reflow other frames (the caption region
  is reserved space inside the frame block — a sheet does not jump when
  a print is picked). 768–1199px: same. <768px: the expanded caption
  takes the full column width under the frame (frames are 1-per-row;
  the caption flows beneath, pushing later frames down — on a phone
  the picked print is the page's focus and the push is honest).
- **Edge cases & failure modes (v2).** *Multiple picks:* allowed up to
  3 simultaneous picks per sheet (a desk shortlist); a 4th pick
  un-picks the oldest, whose caption closes with a 150ms delay so the
  exchange reads as a swap, not a vanish. The cap and the current picks
  are announced in the sheet header ("2 PICKED"). *Picking during the
  §6.2 band pass:* pick wins immediately; the band skips picked frames
  thereafter. *Pick state and filtering (§6.15):* picks persist across
  filters by frame id and re-apply when the frame returns.
- **Accessibility spec (v2).** Real button semantics, `aria-pressed`,
  label "Pick print FR. 12 — A. Okafor, Dockside". The caption region
  is `aria-describedby` of the button. Focus stays on the button after
  picking (never moved into the caption). Touch target: the whole
  frame, minimum 44px in its smallest dimension at every breakpoint —
  frames are large by design, so this is structural. The tick is
  `aria-hidden`; picked state is announced by the button's pressed
  state, not the drawing.
- **Performance budget & mobile variant.** One 500ms multi-overlay
  crossfade per pick, ≤ 3 concurrent. Mobile: identical, with the
  caption flow variant above.
- **Tokens consumed (v2).** `--pitch-*`, `--dur-pick`, `--ease-develop`,
  `--ease-fix`, `--fixer`, `--dot`.

### 6.10 Tray-lift tilt

- **What & why.** A contact sheet on the desk is paper; a print being
  examined is lifted from the tray, tilted toward the light, still wet.
  Hovering a sheet (the grid as a whole, not single frames) tilts it up
  to 2° toward the pointer with a wet-sheen gradient travelling across
  it — the sheet handled as one physical print. Where §6.8 is about
  looking at a frame, §6.10 is about handling the sheet.
- **Structure.** The sheet grid wrapper carries `transform:
  perspective(1200px) rotateX/rotateY` driven from pointer position
  over the sheet, plus a sheen layer (`--sheen` gradient, 40% wide,
  skewed 18°) whose position is the pointer's x mapped across the
  sheet. Frames inside do not tilt individually — paper bends as one
  sheet or not at all.
- **Motion spec.** Tilt: pointer position maps to rotateY ±2° /
  rotateX ∓1.2°, lerped at 0.18 in the shared loop (snappier than the
  scroll lerp — a hand is quicker than a scroll). Sheen: position
  lerps at 0.1, opacity 0 → 1 over 200ms on enter, out over 300ms on
  leave. Settle on leave: 450ms `--ease-tray` back to flat — the
  overshoot easing exists for this landing.
- **Choreography timeline (v2).** t=0 pointer enters sheet → sheen
  fades in at the pointer's edge → tilt builds over ≈250ms of lerp →
  held, following the pointer with the sheen one beat behind (the lag
  is the wet look — light arrives after the lift) → pointer leaves →
  sheen out 300ms, tilt settles 450ms with one 18% overshoot.
- **State matrix (v2).** *Rest:* flat, no sheen. *Hover:* as specced.
  *Focus:* no tilt (keyboard visitors get a flat, stable sheet —
  always). *Active:* a pointer-down on the sheet flattens it instantly
  (you press a print flat to pick from it — §6.9's presses feel
  grounded because the sheet stops floating). *Scrolled-past:* tilt
  only applies while the sheet is ≥40% in viewport. *Disabled:* flat
  sheet, no sheen layer.
- **Content merge.** The tilt belongs to the sheet-as-object; it never
  applies to text sections, forms or the hero frame. The sheen is the
  tray's wet light on the paper — it crosses frames and gutters alike
  because it is *on the sheet*, and it never brightens a caption past
  readability (sheen caps at `--sheen`'s 14% and captions sit below the
  grid, outside the sheen layer).
- **Failure fallback.** Transform failure or loop stall → flat sheet.
  The sheet's flat state is its designed rest; nothing is lost.
- **Reduced-motion variant.** No tilt, no sheen. The sheet is paper on
  a desk, which is already the truth.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: tilt halves
  (±1° / ∓0.6°) — smaller sheets, shorter lever. <768px / touch:
  **element absent** — a sheet under a thumb does not tilt, and
  scroll-linked fake tilt on touch is a §9 failure.
- **Edge cases & failure modes (v2).** *Pointer at sheet corners:*
  tilt clamps at the maxima; the mapping is of the pointer's position
  *within* the sheet, so leaving the sheet is the only way past the
  clamp. *Tilt + §6.2 band running together:* both write to different
  elements (sheet wrapper vs frame overlays) — the loop composes them;
  a frame being picked mid-tilt still resolves correctly because the
  pick's transforms are on the frame, the tilt on the wrapper.
  *Long sheets:* tilt pivot is the sheet's visual centre as clipped by
  the viewport, not the DOM centre, so a 3-viewport sheet pivots where
  the visitor is looking.
- **Accessibility spec (v2).** Pure presentation; `aria-hidden` sheen;
  no information in the tilt. Keyboard and touch receive the complete
  sheet flat. Motion is pointer-contingent and stops the instant the
  pointer does — it cannot run away from the visitor.
- **Performance budget & mobile variant.** One transform + one
  gradient position per sheet, ≤ 0.3ms/frame, max 1 sheet tilting.
  Mobile variant: absent (above) — the cheapest possible.
- **Tokens consumed (v2).** `--sheen`, `--ease-tray`, `--paper`,
  `--lerp`.

### 6.11 Print-count data

- **What & why.** The desk counts what it does. Frame numbers, sheet
  totals and the picked-print count advance in Archivo tabular figures
  as frames pass and prints are picked — small numbers, honestly come
  by. This element is the data voice of §6.5's instruments at the
  level of the whole page: the sheet header's frame range, the "n
  PICKED" tally, the footer's final count. Every figure on the page
  traces to a DOM fact.
- **Structure.** Count displays are `<output>` elements bound to the
  page's frame registry (the same `data-frame` set §6.5 counts).
  Figures: sheet header range ("FR. 07–14 OF 36"), picked tally in the
  sheet header and in §6.16's reference line, footer total ("36
  FRAMES · 3 PICKED · 1 SHEET REQUESTED" as events accrue).
- **Motion spec.** A count changing rolls its digits 120ms
  (`--ease-fix`, masked-window roll as §6.5) — data here ticks like
  the counter because it *is* the counter, repeated at each scale.
  Counts never animate toward a number they have not reached: a tally
  goes 2 → 3 because a third print was picked, at the moment of the
  pick (§6.9 t=600ms), never as a scroll-triggered flourish.
- **Choreography timeline (v2).** Event (frame centred / print picked
  / request filed) → registry updates → each bound `<output>` rolls
  within the same loop frame → instruments agree across the page
  within 120ms of the event, always.
- **State matrix (v2).** *Rest:* counts at their true initial values
  (frames counted from the DOM at arm time). *Hover/focus/active:* no
  states — data is not a control. *Scrolled-past:* counts hold their
  true cumulative values (picks persist; the frame counter component
  follows §6.5's positional rule). *Disabled:* static true counts
  rendered server-side ("36 FRAMES" — picks read 0, correctly, since
  no pick has happened).
- **Content merge.** The numbers enumerate this sheet's frames and this
  visitor's picks. There is no other data in the theme — no invented
  statistics, no "10,000 prints shipped" (§12's truth rule, §10's
  audit).
- **Failure fallback.** A count that cannot verify its registry does
  not render a number; it renders the frame's static label ("SHEET 2")
  instead. A wrong number is worse than no number — the desk's rule,
  and the gate enforces it.
- **Reduced-motion variant.** Counts change instantly, no roll.
- **Breakpoints (v2).** Identical figures at all sizes; on <768px the
  sheet header range shortens to "FR. 07–14" (the total moves to the
  footer, where there is room to be complete).
- **Edge cases & failure modes (v2).** *Filtering (§6.15):* totals
  recount — a filtered sheet of 6 reads "6 FRAMES SHOWN · 36 ON THE
  ROLL", both numbers true, labelled as such. *Unpick:* tallies
  decrement with the same roll, reversed direction (digits roll down —
  the counter runs backwards honestly). *Duplicate frame ids:* a
  build error the registry refuses: the second frame is uncounted and
  §10 fails the build.
- **Accessibility spec (v2).** `<output>` semantics; changes are *not*
  live-announced per tick (see §6.5 — sheet-boundary announcements
  only). The picked tally is part of the pick button's accessible
  description in the sheet header for screen-reader users navigating
  by headings.
- **Performance budget & mobile variant.** Negligible: registry is a
  cached NodeList + a Set of picked ids. Mobile: the shortened header
  form above.
- **Tokens consumed (v2).** `--ease-fix`, `--dot`, `--dot-soft`.

### 6.12 Developing skeleton + darkroom-door transition

- **What & why.** Two states, one process. Loading is *developing*: a
  frame that has not loaded is a coarse dot block at `--pitch-1` that
  resolves through the ladder as its image arrives — the skeleton is
  the photograph in the tray, coming up. Navigation is the *darkroom
  door*: the page fades through tray-teal black — the door's light
  seal — and the next page's first print fades up already developed.
  Neither state borrows a generic spinner or a blank fade; both are
  the darkroom's own events.
- **Structure.** Skeleton: each pending frame renders its frame, mat
  and a dot-block (pre-rendered `--pitch-1` rendition if available,
  else a dot-pattern placeholder at the frame's aspect ratio with the
  frame number in the mat — an unexposed frame is still a numbered
  frame). Door: a fixed overlay in `--tray-deep` with a 1px `--tray`
  hairline at its leading edge (the door's light seal catching the
  frame), opacity-driven.
- **Motion spec.** Skeleton resolve: on image load, the block climbs
  pitch-1 → pitch-3 → sharp over `--dur-develop` (900ms,
  `--ease-develop`, two crossfades), then joins §6.2's band at its
  earned rung. Door: exit fade 180ms to full `--tray-deep`, hold ≤
  120ms, enter fade 220ms with the new page's hero already sharp —
  total `--dur-door` (400ms) plus hold. Door never delays first
  content: it runs only on client-side navigations where the next
  page is already available.
- **Choreography timeline (v2).** *Load:* t=0 frames render as numbered
  dot blocks → each image's arrival starts its own 900ms develop →
  hero develops first (it is prioritised in load order) → sheet fully
  developed ≈1.4s on a mid connection. *Navigation:* t=0 click → 180ms
  door closes → ≤120ms hold → 220ms door opens on the new sheet →
  instruments (§6.5) initialise at the new page's true values within
  the same frame as the open completes.
- **State matrix (v2).** *Rest:* n/a (transient element). *Hover/
  focus:* the door never traps focus — focus moves to the new page's
  heading at the open, per standard routed-page practice. *Active:*
  a second navigation during a door cancels the hold and re-times
  from the current opacity. *Scrolled-past:* n/a. *Disabled:* no door
  (full page loads, browser default), skeletons are static numbered
  frames until images arrive, then simply appear — developing is an
  enhancement of loading, never a gate on it.
- **Content merge.** The skeleton's dot block *is* the frame's
  photograph at its coarsest honest state, and the door's black is the
  darkroom's black. Loading and leaving are the two moments a generic
  theme rents from a UI kit; this theme owns both.
- **Failure fallback.** An image that errors holds its numbered frame
  with the desk's line in the caption position: "THIS FRAME DID NOT
  DEVELOP." (§12's error voice) — a broken frame is shown as a broken
  frame, never a silent gap in the sheet. Door failure → plain
  navigation.
- **Reduced-motion variant.** No door (instant navigation), skeletons
  appear sharp on load with no develop climb.
- **Breakpoints (v2).** Identical across sizes; on <768px the door's
  hairline is omitted (a phone's door is just dark).
- **Edge cases & failure modes (v2).** *Slow image on a fast page:*
  frames develop independently; one late frame never holds the sheet's
  choreography (its §6.3 marks draw on entry regardless — the desk
  marks the print it *expects*). *Back/forward cache:* a restored page
  shows everything developed; the door does not replay. *Prefetch
  hits:* if the next page is fully prefetched, the door still runs
  its 400ms — the seal is a ritual of the place, and 400ms is its
  whole cost; under `Save-Data` the door is skipped.
- **Accessibility spec (v2).** Skeleton frames carry the image's alt
  text from the start (the frame is labelled before it develops).
  Route changes announce via the new page's `<h1>` focus. The door
  overlay is `aria-hidden` and pointer-events-none except during its
  400ms, when it blocks clicks to prevent double navigation — and
  releases on any failure.
- **Performance budget & mobile variant.** Skeletons reuse the
  rendition pipeline (no extra assets beyond the pitch-1 renditions,
  already budgeted). Door: one fixed overlay, opacity only. Mobile:
  as specced.
- **Tokens consumed (v2).** `--pitch-1`, `--pitch-3`, `--pitch-5`,
  `--tray-deep`, `--tray`, `--dur-develop`, `--dur-door`,
  `--ease-develop`.

### 6.13 Darkroom rail navigation (page family: navigation)

- **What & why.** Navigation in a darkroom is a row of labelled trays.
  The header is a slim `--tray-deep` band — the darkroom's door frame —
  carrying the wordmark in Archivo, the section links as tray labels,
  and (below 1200px) the compact frame counter that the rail hands
  over (§6.5). Links are not buttons and not pills: they are labels
  typed on the tray's edge, and the current section's label is ruled
  under with a grease-pencil line.
- **Structure.** `<header>` fixed at top, 56px, `--tray-deep` ground,
  `--paper` text. Wordmark left (Archivo 700, 15px, tracking 0.18em).
  Nav centre/right: Desk-label links, 28px hit area vertically padded
  to 44px. Current link: 2px `--fixer` underline (the pencil rule),
  drawn once on load (300ms `--ease-pencil`) and re-drawn on route
  change. The ≥1200px margin rail (§6.5) is this header's vertical
  sibling — same ground, same type, one furniture set.
- **Motion spec.** Header hides on scroll down past 300px and returns
  on scroll up (translateY, 250ms `--ease-fix`), *except* it never
  hides while focus is within it. The pencil underline re-draws on
  navigation via §6.12's door completing. No other header motion —
  the door frame does not perform.
- **Choreography timeline (v2).** Load → header present, underline
  draws 300ms → scroll down 300px → header slides away over 250ms →
  scroll up any amount → header returns 250ms → navigation → door
  (§6.12) → new page: header present from first paint, underline
  under the new section, drawn.
- **State matrix (v2).** *Rest:* visible at top. *Hover:* link text
  brightens `--paper` 80% → 100% and the label's letterspacing opens
  0.16em → 0.19em over 150ms (a label leaned toward). *Focus:* 2px
  `--fixer` outline (the amber that reads on teal is the graphic
  `--fixer` at full strength — on `--tray-deep` it measures ≈4.6:1
  against the ground for the outline's purpose). *Active:* link
  pressed — background `--tray` flash 120ms. *Scrolled-past:* the
  hidden-on-scroll-down state. *Disabled:* a static header, always
  visible; hiding is a JS enhancement.
- **Content merge.** The header is the darkroom's door frame and the
  rail is its wall: the site's instruments and its wayfinding are one
  built environment, in the room's darkest material, so the sheets —
  the content — are the only light things on the page.
- **Failure fallback.** No JS: static header, no hide, underline
  present under the current section (server-rendered class).
- **Reduced-motion variant.** Header never hides; underline present
  without drawing.
- **Breakpoints (v2).** ≥1200px: header + margin rail (counter lives
  in the rail). 768–1199px: header carries the compact counter +
  horizontal exposure strip (§6.5). <768px: header carries counter
  only; nav collapses behind a "SHEETS" disclosure button that opens
  the link list as a tray pulled down (300ms `--ease-tray`, links at
  48px rows).
- **Edge cases & failure modes (v2).** *Header + hero pin:* the hero
  (§6.1) pins beneath the header; the header's hide-on-scroll is
  suspended during the pin (the visitor is inside the photograph —
  the door frame stays). *Long wordmarks:* the wordmark truncates
  never; nav yields (links wrap to the disclosure pattern at whatever
  width they stop fitting, measured, not breakpoint-guessed).
- **Accessibility spec (v2).** Landmark header, nav with
  `aria-current="page"` on the underlined link (the pencil line is
  never the only indicator — the current link is also 700 weight).
  Disclosure button: `aria-expanded`, focus returns to it on close.
  Skip link lands on the first sheet's heading, styled as a desk
  label on paper.
- **Performance budget & mobile variant.** One transform on one
  element. Mobile: the disclosure variant above.
- **Tokens consumed (v2).** `--tray-deep`, `--tray`, `--paper`,
  `--fixer`, `--fixer-deep`, `--ease-fix`, `--ease-pencil`,
  `--ease-tray`.

### 6.14 The pinned hero frame (page family: hero)

- **What & why.** The hero composition around §6.1's mechanism: a
  contact sheet's frame № 00 — the one frame the desk pinned above the
  tray for the whole room to see. Full-viewport stage, the frame
  centred at 62vh, the essay title standing beside it on the paper
  like a caption writ large, and beneath the frame its caption block:
  photographer, place, date, and the instruction. The hero is a print
  first and a headline second; the title never touches the dots.
- **Structure.** Section of 220vh (the §6.1 scrub range + release
  tail). Sticky stage: left, the frame (border, mat, image stack,
  crop marks pre-drawn — the desk marked this one before you arrived);
  right (≥1200px), a 4-column text block: Desk-label kicker ("FRAME
  00 — THE PORTRAIT"), Newsreader hero title, standfirst, and the
  scroll instruction with a thin `--fixer-deep` rule. Below the stage,
  as the pin releases, the frame's full caption block (§6.7's stamp
  lives here) and the sheet-1 header follow immediately — the hero
  *becomes* the top of sheet 1 rather than ending.
- **Motion spec.** §6.1 owns the frame. The composition adds: the
  caption block rises 12px and fades 0 → 1 across `p` 0.75 → 1 (the
  words arrive when the face does — kinetic type in service of the
  resolve, §5); the scroll instruction fades out across `p` 0 → 0.15
  (once you have stepped back, the instruction has done its work).
- **Choreography timeline (v2).** Load → dot field, title present,
  instruction present, caption at 0 → scroll: resolve (§6.1 timeline)
  → `p` 0.75: caption begins rising → `p` 1: face sharp, caption
  landed, stamp jitters (§6.7 — the hero's stamp is the first to tap)
  → release tail: the frame scrolls away as sheet 1's first frame,
  counter starts (§6.5).
- **State matrix (v2).** *Rest:* as loaded. *Hover:* none on the
  composition (the frame is §6.1's). *Focus:* the caption's link, if
  any, standard. *Active:* n/a. *Scrolled-past:* the hero is sheet 1's
  first frame in the flow, sharp, circled if a portrait (§6.4 fires
  at `p` 1 — the hero's face is circled as it resolves, the page's
  one guaranteed circle). *Disabled:* static portrait + title +
  caption, 100vh.
- **Content merge.** The hero's text is the frame's caption at two
  scales — the title is what the desk would chalk on the wall, the
  caption block is what it types under the print. Nothing in the hero
  is marketing copy wearing a frame; it is a captioned photograph with
  an essay attached.
- **Failure fallback.** §6.1's fallback, inherited: sharp portrait,
  full caption, no pin. The composition is layout, and layout does not
  fail.
- **Reduced-motion variant.** Static hero (per §6.1) with caption at
  final position and the standfirst carrying the distance sentence
  (§6.1).
- **Breakpoints (v2).** ≥1200px: side-by-side as specced. 768–1199px:
  title above the frame, frame at 54vh, caption below. <768px: title,
  frame (full-bleed, 8px mat), caption — a single column that reads
  like a broadsheet front page.
- **Edge cases & failure modes (v2).** *Essay title longer than 3
  lines:* the text block grows downward; the frame never shrinks to
  accommodate type — the photograph's size is the hero's constant.
  *Portrait with no face* (a landscape hero): §6.4 does not fire; the
  caption's arrival at `p` 0.75 is the hero's closing beat instead,
  and §10's circle cap is spent elsewhere or nowhere. *Short
  viewports (<600px height):* the pin range compresses to 90vh so the
  resolve completes within one screen of travel.
- **Accessibility spec (v2).** Reading order: kicker → title →
  portrait (alt) → standfirst → caption. The sticky stage is
  `aria-hidden`-free — all its content is ordinary DOM in order; the
  pin is visual only. The scroll instruction is text, not an icon.
- **Performance budget & mobile variant.** Inherits §6.1's budget;
  the caption rise is one transform on one block. Mobile: the stacked
  variant above.
- **Tokens consumed (v2).** `--paper`, `--dot`, `--fixer-deep`,
  `--mark-line`, `--lerp`, `--ease-develop`.

### 6.15 Print cards (page family: cards)

- **What & why.** Off the home page, the theme still needs cards —
  for a photographer's other series, a book's plates, an exhibition's
  works. The print card is a small contact frame standing for a larger
  sheet elsewhere: frame, mat, one image (at its earned pitch), and
  the desk caption, with a "VIEW THE SHEET" desk link. Cards here are
  not tiles in a design system; each is a print that points at its
  roll.
- **Structure.** `<article class="print-card">`: frame (2px border,
  10px mat), image with §6.2's 2-rung stack (cards sharpen at centre
  like everything else), caption block (series name in Newsreader 20px,
  desk line: frame count + date range in Archivo), footer row: the
  desk link + a frame badge ("24 FR."). Whole card is *not* a click
  target — the link is (a card that is secretly one big button is a
  §9 failure; prints are picked deliberately, §6.9).
- **Motion spec.** Entry: §6.3's reveal (marks + clip) in grid order,
  70ms stagger across a row. Hover: the card's image leans in one rung
  (§6.8 applies per-image) and the card's mat shadow deepens one step
  (the print lifting 2mm off the desk — shadow only, no transform, so
  cards never collide). Link hover: the desk link's underline draws
  200ms `--ease-pencil`.
- **Choreography timeline (v2).** Card row enters → marks draw in
  order → clips open → images join the focus band → at centre, card
  images reach pitch-4 (cards never auto-reach pitch-5; full sharp is
  for the sheet itself, one click away — the card is a promise, and
  the promise is calibrated).
- **State matrix (v2).** *Rest:* pitch per band. *Hover:* +1 rung,
  shadow step. *Focus:* link focus = card image full sharp (the §6.2
  focus rule) + outline on the link. *Active:* link press, 120ms.
  *Scrolled-past:* band state. *Disabled:* sharp images, static
  marks, working links.
- **Content merge.** A card's image is the series' actual key frame
  and its caption is the series' actual desk record (frames, dates).
  The card *is* the archive's index entry, not a teaser invented for
  the grid.
- **Failure fallback.** Sharp image, drawn marks, link — the static
  card is complete.
- **Reduced-motion variant.** Sharp images, marks drawn, no stagger.
- **Breakpoints (v2).** ≥1200px: 3 per row. 768–1199px: 2 per row,
  mat 8px. <768px: 1 per row; the frame badge moves into the caption
  line (no absolute positioning on small cards).
- **Edge cases & failure modes (v2).** *Series with no key frame:*
  the card shows the sheet's first frame — never a placeholder
  graphic; an archive card with an invented image is a §10 failure.
  *Filtering a card grid:* filtered-out cards leave the registry
  (§6.11 recounts) and remaining cards re-reveal without marks
  re-drawing (marks persist per frame id). *Long series names:* 2-line
  clamp with the full name in the link's accessible label — the desk
  abbreviates on paper and completes in the record.
- **Accessibility spec (v2).** Article semantics; the image alt is the
  key frame's own alt; the link's text names the series ("View the
  sheet: Dockside, 1987"). Focus order follows the grid's reading
  order. Touch targets: link ≥44px tall via padding.
- **Performance budget & mobile variant.** Cards use the 2-rung
  rendition set (≤ 90KB per card image, §14). Mobile: 1-per-row, same
  set.
- **Tokens consumed (v2).** `--mark-line`, `--paper-warm`, `--dot`,
  `--dot-soft`, `--fixer-deep`, `--ease-pencil`, `--pitch-3`,
  `--pitch-4`.

### 6.16 Request-a-print form (page family: forms / conversion)

- **What & why.** The conversion act in a darkroom is filing a request
  for a print. The form is an enlarger log card: the print reference
  line (pre-filled from the visitor's pick, §6.9), the requester's
  details on ruled lines, the size selector as a strip of frame
  formats, and a submit that reads like the desk stamping the card —
  FILE THE REQUEST. A submitted card comes back with its filing stamp:
  a reference number that is the request's real position in the day's
  log.
- **Structure.** `<form class="log-card">` on `--paper-warm` (the
  card stock differs from sheet paper — forms are cards, not sheets),
  2px border, inside a tray band section so the card sits in the
  dark. Fields: label (Desk label) above a 1px ruled line input
  (transparent ground, Newsreader 18px entries — the visitor writes in
  the story's type, the desk labels in its own). Print reference: a
  read-only line showing the picked frame ("FR. 12 — A. OKAFOR,
  DOCKSIDE, 1987") with a CHANGE link to the sheet. Size selector:
  three stamp-radio options (8×10 / 11×14 / 16×20) as bordered desk
  labels, the chosen one filled `--tray` with `--paper` text.
  Consent checkbox: a square the visitor ticks with a pencil tick
  (§6.3's draw, 200ms) — "The desk may crop to the marked line" —
  default unticked, honestly.
- **Motion spec.** Focus: the field's ruled line inks from
  `--mark-hair` to full `--dot` (200ms `--ease-pencil`) and a small
  grease tick appears in the card's margin beside the active field
  (the desk is following along). Error: the line turns `--fixer-deep`
  and the error prints beneath in the desk's voice (§12), 0ms delay —
  errors are print, not animation. Submit: the card presses (scale
  0.995, 150ms `--ease-fix`), a FILED stamp strikes the card's corner
  (rotate −4°, scale 1.3 → 1, 180ms `--ease-fix`) with the reference,
  and the form is replaced by its own filed copy — the visitor sees
  the card they filed, stamped.
- **Choreography timeline (v2).** t=0 submit (valid) → card presses
  150ms → t=200ms stamp strikes → t=380ms the confirmation line types
  in beneath the stamp in Archivo ("LOGGED AS № 0417 — THE DESK
  REPLIES WITHIN TWO DAYS") → focus moves to the confirmation heading.
  Invalid: t=0 → first error field's line inks amber-deep and its
  message prints; focus moves to that field; the card does not press.
- **State matrix (v2).** *Rest:* ruled lines at hair strength, stamp
  options unfilled. *Hover:* stamp options get a 1px → 2px border
  weight change. *Focus:* line ink + margin tick (above); radio focus
  shows the `--fixer-deep` outline. *Active:* submit press.
  *Scrolled-past:* n/a. *Disabled (no JS):* a plain working form —
  labels, inputs with real borders at hair strength, a submit button;
  the filed state is a server-rendered confirmation page in the same
  card design.
- **Content merge.** The form is the darkroom's own paperwork, and its
  pre-filled reference line is the visitor's actual pick carried
  across the page — the conversion is the continuation of §6.9's act,
  not a new funnel. The reference number on the stamp is the request's
  real log position (server-issued), never a random flourish (§11's
  truth rule).
- **Failure fallback.** Submission failure (network/server): the card
  stays unfilled-stamped, entries intact, with the desk's failure line
  (§12) and a retry — a request is never lost silently in the tray.
- **Reduced-motion variant.** No press, no stamp strike: the filed
  state appears with the stamp present. Focus and error behaviour
  identical (they are state changes, not motion).
- **Breakpoints (v2).** ≥1200px: card at 560px in the tray band, size
  stamps in a row. 768–1199px: card 520px. <768px: card full-width,
  size stamps stack full-width at 48px rows, inputs at 18px (also
  preventing iOS zoom).
- **Edge cases & failure modes (v2).** *No print picked:* the
  reference line reads "NO PRINT PICKED — THE DESK WILL ASK" and a
  sheet link is offered; the form still files (a general request is
  legitimate business). *Changed pick mid-form:* the reference line
  updates live and notes the change ("REFERENCE UPDATED — FR. 19").
  *Long names/addresses:* fields are single-line with horizontal
  scroll inside the line — the card never grows mid-typing (layout
  stability is a darkroom virtue). *Spam/duplicate submits:* the press
  disables the button for the request's duration; a second strike is
  impossible.
- **Accessibility spec (v2).** Real `<label>`s, `aria-describedby` for
  errors, errors announced via `role="alert"` on the summary line
  only (not per keystroke). The stamp radios are real radio inputs
  with visible custom rendering that never hides the native focus.
  Touch targets ≥44px. The filed confirmation is a heading + text,
  focus-managed (above). Contrast: entries `--dot` on `--paper-warm`
  ≈13.9:1; error text `--fixer-deep` on `--paper-warm` ≈4.6:1.
- **Performance budget & mobile variant.** No animation loops; the
  stamp strike is one transform. Mobile: the stacked variant above.
- **Tokens consumed (v2).** `--paper-warm`, `--paper`, `--dot`,
  `--mark-hair`, `--fixer-deep`, `--fixer`, `--tray`, `--ease-fix`,
  `--ease-pencil`.

### 6.17 Fixer footer (page family: footer)

- **What & why.** Everything that survives development goes into the
  fixer. The footer is a `--tray-deep` band — the page's final tray —
  holding the colophon in desk type: what the site was printed with,
  the roll's final counts (§6.11), the desk's links, and along its top
  edge the roll-edge marquee: film-edge markings travelling slowly —
  frame numbers and stock notations — the roll itself passing through
  the fixer one last time.
- **Structure.** Footer: top strip (36px, `--dot` ground) carrying the
  marquee: repeated edge markings in Archivo 11px `--paper` at 70% —
  "FR. 01 ▸ FR. 02 ▸ … SAFETY FILM — 36 EXP ▸" generated from the
  page's real frame registry (the numbers are the page's frames).
  Body: three desk columns (the archive, the desk, the record) +
  colophon line: "Set in Archivo & Newsreader · Printed as halftone
  at five pitches · © the desk" + §6.11's final counts line.
- **Motion spec.** Marquee: 24px/s linear, seamless loop of two
  identical strips, pauses on hover and when off-screen. Nothing else
  in the footer moves; the fixer is where motion stops — a page that
  ends in stillness after all that resolving.
- **Choreography timeline (v2).** Footer enters → marquee already
  travelling (it started when the footer was 1 viewport away, so it
  never "starts" in view) → counts line shows final true values →
  the last frame's stamp (§6.7) has already tapped above; the page's
  final beat is the roll edge passing, unhurried.
- **State matrix (v2).** *Rest:* marquee travelling. *Hover:* marquee
  pauses; links brighten as §6.13. *Focus:* marquee pauses while
  focus is in the footer (a reader of small print is not chased).
  *Active:* link press flash as §6.13. *Scrolled-past:* n/a — it is
  the end. *Disabled:* the marquee renders as a static edge strip
  (one pass of markings, no loop) — the roll's edge as a printed
  graphic.
- **Content merge.** The marquee's numbers are the page's own frames
  and the counts are the page's own tallies; the footer is the roll's
  record of itself, not a sitemap wearing a costume. Links are the
  desk's real departments.
- **Failure fallback.** Static strip + static counts (server-rendered
  frame total; picks read as the session's true count or are omitted
  — §6.11's no-wrong-numbers rule).
- **Reduced-motion variant.** Static edge strip, as the disabled
  state. The footer under reduced motion is identical to the footer
  with JS off — correct for the place where everything is fixed.
- **Breakpoints (v2).** ≥1200px: three columns + colophon.
  768–1199px: two columns. <768px: one column, counts line wraps to
  two lines, marquee strip height 32px.
- **Edge cases & failure modes (v2).** *Pages with very many frames
  (a 60-frame longread):* the marquee lists sheet ranges ("FR. 01–12
  ▸ SHEET 1") instead of every number — the edge stays readable at
  24px/s. *Marquee seam:* the two strips are width-matched to the
  content's exact period; a visible seam jump is a §10 failure.
- **Accessibility spec (v2).** The marquee is `aria-hidden` (its
  information — the frame count — is in the counts line as text).
  Footer landmarks and link text are complete sentences' worth of
  meaning ("The archive — all sheets"), never "click here".
- **Performance budget & mobile variant.** One translating strip,
  transform only, gated off-screen. Mobile: as specced.
- **Tokens consumed (v2).** `--tray-deep`, `--dot`, `--paper`,
  `--dot-soft`, `--fixer`.

### 6.18 The blank frame (page family: 404)

- **What & why.** A missing page is an unexposed frame on the roll:
  the frame border is there, the mat is there, the frame number is
  there — and inside, nothing developed. The 404 shows FR. ∅ in a full
  frame at `--pitch-0`'s dot pattern *with no photograph behind it*
  (the one place in the theme where a dot field is honestly empty,
  labelled as such), the desk's line, and the way back to the sheets.
- **Structure.** A centred frame (max 640px) on a paper ground: mat,
  dot-block interior with the frame counter reading "FR. — / —", the
  caption block in full desk form: "FRAME NOT EXPOSED. The roll
  continues at the sheets below." Links: the home sheet + the archive
  index, as desk links (§6.15's pattern).
- **Motion spec.** One permitted gesture: on load, the dot block
  *attempts* to develop — pitch climbs one rung over 900ms and falls
  back to coarse (nothing there to resolve). Once. It is the theme's
  saddest joke and it is told once, quietly.
- **Choreography timeline (v2).** t=0 frame present → t=300ms develop
  attempt begins → t=750ms one rung finer → t=1200ms settles back to
  coarse → static. The caption and links are usable from t=0; the
  gesture never gates them.
- **State matrix (v2).** *Rest:* post-gesture stillness. *Hover:*
  links as §6.15. *Focus:* standard. *Active:* n/a.
  *Scrolled-past:* n/a (the page is one frame). *Disabled:* static
  blank frame, full caption, working links.
- **Content merge.** The 404 is a frame *of this roll* — its number
  is absent from the sequence honestly, and the way back is phrased
  as continuing the roll. No generic "oops" exists in this theme.
- **Failure fallback.** The static frame. There is nothing beneath
  this element to fail to.
- **Reduced-motion variant.** No develop attempt; static blank frame.
- **Breakpoints (v2).** ≥1200px: frame 640px. <768px: frame full-width
  minus 32px margins; the counter line shortens to "FR. —".
- **Edge cases & failure modes (v2).** *Search referrals:* if the
  missing URL resembles a frame id, the caption adds the desk's guess
  ("Nearest exposed frame: FR. 12") with its link — a guess labelled
  as a guess. *Soft 404s are forbidden:* this page ships with a real
  404 status; the theme does not decorate routing errors elsewhere.
- **Accessibility spec (v2).** The `<h1>` is the desk line itself
  ("This frame was not exposed"), the dot block is `aria-hidden`, and
  the links are reachable in two tabs from the heading.
- **Performance budget & mobile variant.** One small animation, once.
  No renditions loaded — the block is a pattern, not a photograph,
  and says so.
- **Tokens consumed (v2).** `--pitch-0`, `--pitch-1`, `--mark-line`,
  `--paper`, `--dot`, `--fixer-deep`, `--ease-develop`.

---

## 7. Page application map

- **Home.** The full performance: hero frame (§6.14/§6.1), sheet 1
  (the photographer's selected frames), one tray band (the process —
  how prints are made and requested), sheet 2 (the latest roll), the
  log-card form (§6.16), fixer footer. Frame budget: hero + ≤ 9 + ≤ 9.
- **Listing / archive index.** Sheets of print cards (§6.15) grouped
  by roll or year, each sheet headed with its range; a filter row in
  desk type (by year, by place) that re-deals the sheets — filtered
  frames keep their numbers (a frame's number is its identity, not its
  position; the counter recounts per §6.11's shown/total rule).
- **Detail / the sheet page.** One roll, all its frames at full
  §6.2/§6.3/§6.9 treatment, the essay in Newsreader between frame
  groups, and the request form at the foot pre-filled from any pick.
  This is the theme's native page; the home page is its advertisement.
- **About / the desk page.** The photographer's portrait gets the
  hero treatment at half scale (pin range 70vh — an about page earns
  a smaller ceremony), the desk's history as sheets of captioned
  frames, the process in a tray band.
- **Contact / request.** §6.16's log card as the whole page's centre,
  in a full tray environment, with the picked print (if any) shown
  framed beside the card at pitch-5 — the visitor sees the exact print
  they are requesting while they file.
- **404.** §6.18's blank frame.

---

## 8. Worked examples

### 8.1 The hero — a documentary studio's portrait of its founder

*The site: "Marsh & Daughter," a two-generation documentary studio.
The hero photograph: the founding mother at her enlarger, 1989,
photographed by the daughter.*

- **Build.** §6.14 composition. Frame at 62vh, rendition set at six
  pitches (hero set, 0.75× resolution, 812KB total). Face data
  authored: `data-face="0.52,0.38,0.16,0.20"`. Crop: none — the desk
  left this one whole, so §6.3 draws corner ticks only and the caption
  carries NOT TO BE CROPPED.
- **Scroll timeline.** 0vh: dots at 22px, a grey weather system, no
  face. Title beside it: "She taught the town to look." 30vh: pitch-2,
  the enlarger's shape separates from the dark. 65vh: pitch-3 — a
  woman's profile is *suspected*. 95vh: pitch-4, the face is hers.
  120vh: overlays clear, scale 1.0; across the last quarter the
  caption has risen into place — "E. MARSH — The darkroom, Mill Lane,
  Oct 1989. NOT TO BE CROPPED." — the face-circle draws around her
  profile (t+120ms, 600ms), the stamp taps once at t+720ms, the pin
  releases, and FR. 01 starts counting as sheet 1 arrives.
- **What the visitor feels.** They leaned in, found nothing, stepped
  back, and were met. The studio's whole claim — attention rewarded —
  has been *done to them* before a word of body copy.

### 8.2 Mid-page — sheet 2, "The Dockside Frames"

*Nine frames from one 1987 roll: a ferry crew at dawn.*

- **Build.** A §4 sheet: header "SHEET 2 — THE DOCKSIDE FRAMES ·
  FR. 07–15", 3×3 contact grid, each frame with its crop data (six
  cropped as marked, three whole), two portraits with face data, one
  frame — the harbour master's hands on a rope — that the essay quotes
  in text beside the grid.
- **Scroll timeline.** The sheet header enters; §6.3 deals the frames
  in grid order (marks 400ms, clips 600ms, 70ms row stagger). The
  focus band (§6.2) travels: as FR. 09 — the captain, mid-laugh —
  centres, it sharpens through pitch-3 → pitch-4 → clear; at full
  sharp the face-circle draws (the essay's subject, circled), and
  FR. 09's stamp — CROPPED AS MARKED — taps. The visitor hovers FR. 11
  (one rung sharper, shimmer stills), clicks it: 500ms resolve,
  caption expands — "A. OKAFOR — Dockside, 14 Mar 1987. Cropped to
  the hands, per the desk. Print available." — tick on the mat,
  header tally rolls to "1 PICKED", counter agrees. Scrolling on,
  FR. 11 stays sharp among dissolving neighbours: the visitor's print,
  held.
- **What the visitor feels.** A sheet they have *worked* — marked,
  chosen from, tallied — exactly the pleasure of a real contact sheet
  and a loupe.

### 8.3 Conversion — requesting the print of FR. 11

- **Build.** The tray band below sheet 2 carries §6.16's log card,
  its reference line already reading "FR. 11 — A. OKAFOR, DOCKSIDE,
  1987" from the pick. Beside the card, FR. 11 framed at pitch-5.
- **Scroll/interaction timeline.** The band enters (tray ground, the
  card lit like paper under the enlarger). The visitor tabs in: each
  field's line inks as focused, the margin tick following. They choose
  11×14 (stamp fills teal), leave the crop-consent box unticked (the
  desk will print the full frame — the honest default honoured).
  Submit: the card presses 150ms, the FILED stamp strikes at −4° with
  "№ 0417", the confirmation line types in Archivo beneath it, focus
  lands on "Filed as № 0417." The footer counts update: "1 SHEET
  REQUESTED." Nothing bounced, nothing span, nothing asked twice.
- **What the visitor feels.** They did not fill in a form; they filed
  a card at a desk that was already expecting the print they picked.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Dots on text.** A headline screened, blurred or set over the dot
   field "for texture." *Cure:* §3's law — type is print, dots are
   photographs. Any build with a halftone headline is rejected whole.
2. **The generic dot-noise background.** A pitch pattern used as page
   wallpaper behind ordinary sections. *Cure:* every dot field is a
   specific photograph's rendition (§1's one law). If you cannot name
   the photograph, the dots come off.
3. **Moiré strobing.** Shimmer amplitude or opacity pushed until the
   sheet vibrates. *Cure:* §6.6's ceilings (±0.4°, opacity ≤0.09),
   verified on real hardware; when in doubt, halve it — the shimmer
   should be noticed second, never first.
4. **Sepia nostalgia.** Warm filters, torn edges, "vintage" anything.
   *Cure:* the paper is neutral `#EFEDE8`; the theme is about a
   *process*, not a decade. The word "vintage" is banned from copy
   (§12).
5. **Counters that lie.** A frame counter reading /36 on a 23-frame
   page, or print counts that animate on scroll without a pick.
   *Cure:* §6.11's registry — every figure traces to the DOM or the
   build fails §10.
6. **Stamps as stickers.** NOT TO BE CROPPED slapped at a jaunty angle
   on frames the desk cropped, or used as a badge on cards and
   buttons. *Cure:* the stamp is per-frame caption data (§6.7), in
   the caption, at print size, saying the true instruction.
7. **A resolve that never completes.** The hero left at pitch-2 by a
   short pin range, or overlays stuck by a stalled loop. *Cure:*
   §6.1's guaranteed completion by 120vh and the 800ms watchdog; the
   gate tests with throttled CPU.
8. **Hover-sharpen on touch.** Tap = sharpen, second tap = pick, and
   the visitor never learns the sheet's grammar. *Cure:* §6.8 —
   touch picks on first tap; hover effects are pointer-only,
   media-gated.
9. **Grease marks everywhere.** Crop marks on logos, circles on every
   face, ticks on every card. *Cure:* marks are editorial acts with
   caps (§10: ≤3 circles/page) — the desk marks what matters.
10. **The zoom that betrays the thesis.** Any decorative image zoom,
    anywhere, for any reason. *Cure:* §5 — scale means focus in this
    theme; the only scale on the page is the resolve's, and it goes
    *out*.
11. **Shimmer fighting the resolve.** Ambient shimmer (§6.6) left
    running on the hero while it is scrubbing — two motions on one
    screen, and the moiré crawls across a face that is trying to
    arrive. *Cure:* the shimmer gates off on any frame whose rung is
    actively changing; it breathes only on prints at rest.
12. **Desk type gone casual.** Captions drifting into sentence case,
    a label set in Newsreader "because it looked softer," an
    exclamation mark in a button. *Cure:* §3/§12's voice separation
    is mechanical — Archivo uppercase is the desk, Newsreader is the
    story, and a build review greps for the violations rather than
    trusting taste.

---

## 10. Quality gate

A build may not ship in this theme until every **blocking** item
passes and at least 9 of the 11 **standard** items pass. Evidence, not
intentions: screenshots, a JS-off load, a throttled-CPU pass.

**Blocking — all must pass.**

1. **JS-off test:** with JavaScript disabled, every photograph is
   sharp, every caption expanded, all links and the form work, marks
   are drawn, stamps are present.
2. **Watchdog test:** with the scroll loop deliberately stalled, all
   overlays clear to sharp within 800ms + one frame, on every page.
3. **Reduced-motion test:** no pin, no scrub, no shimmer, no door, no
   tilt; all images sharp; the hero's standfirst carries the distance
   sentence.
4. **Truth audit:** every number on the page — frame totals, picked
   tallies, filing references — traces to the DOM registry or a
   server-issued value. One invented figure fails the build.
5. **Resolve completion:** the hero reaches pitch-5 and scale 1.0 by
   exactly 120vh of scroll at 4× CPU throttle, and the pin releases.
6. **Contrast audit:** amber text appears only as `--fixer-deep`
   (≥4.5:1 on its ground); body and caption text ≥7:1 on paper;
   `--fixer` is used for graphic marks only.
7. **Mark discipline:** ≤3 face-circles per page; crop marks only on
   frames with real crop data; stamps match each frame's true
   instruction.
8. **Cursor & cover audit:** system cursor unchanged everywhere; no
   overlay, sheen or mark ever covers caption text at any scroll
   position (checked at 5 depths).
9. **Pin discipline:** exactly one pinned scene (the hero); the pin
   disables under 600px viewport height and under reduced motion.

**Standard — at least 9 of 11.**

10. The focus band (§6.2) holds 60fps on a mid-range Android device;
    no frame over 20ms attributable to theme code in a full-page
    scroll.
11. Rendition discipline: no image ships a live-filter halftone;
    every screened image traces to the build-time pipeline (§14).
12. The counter and strip agree with the visible sheet after
    filtering, picking and jump-scrolls (End key test).
13. Shimmer is invisible at arm's length on a second viewing — a
    reviewer who has seen the page twice should have to *look* for
    it.
14. Captions follow §12's desk form exactly (name, place, date,
    instruction) on 100% of frames.
15. The door transition completes in ≤520ms including hold, and is
    skipped under Save-Data.
16. Tray-lift never applies to text, forms or the hero; tilt is
    absent on touch.
17. The 404 is served with a real 404 status and its develop-attempt
    runs once, ≤1.2s.
18. Dark scheme (if shipped) is the full tray conversion of §2 — no
    half-dark pages.
19. Print stylesheet: `@media print` removes overlays, shimmer,
    marquee and door; the page prints as clean sheets — the theme's
    final proof the paper was real.
20. **The five-second test:** a first-time visitor, shown the hero
    mid-resolve, says some version of "the picture is coming into
    focus as I step back" — not "cool dot effect."

**Minimum bar, in one line:** a build that passes the blocking nine
has earned the right to be judged on premiumness; a build that also
makes a reviewer *step back from their own screen* has earned the
theme.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed do not get invented ad hoc — they are built from
the nearest listed relative.

- **Buttons.** Desk buttons: Archivo 600 12px uppercase, 2px `--dot`
  border on paper (or `--paper` border on tray), padding 12px 20px,
  no radius (prints are square). Press = scale 0.99, 120ms
  `--ease-fix`. Primary action on paper is filled `--dot` with
  `--paper` text; on tray bands, filled `--paper` with `--tray-deep`
  text. Amber is never a button fill.
- **Inputs.** Ruled-line fields per §6.16: label above, 1px line,
  Newsreader entries. On tray grounds the line is `--paper` at 45%
  and the entry is `--paper`.
- **Selects.** Native select restyled as a desk line with a pencil
  chevron (SVG, `--fixer-deep`); on <768px the native control takes
  over fully (the desk does not fight the platform).
- **Checkboxes & radios.** The pencil-tick checkbox and stamp radios
  of §6.16. A radio group is a row of stamp options; a checkbox is a
  square awaiting a tick. Native inputs remain the focusable element,
  always.
- **Tables.** Exposure tables: a test-strip table — header row in
  Desk label, body in Archivo tabular, row bands alternating `--paper`
  / `--paper-warm` like strip densities, the recommended row ruled in
  `--fixer-deep` text. No rounded corners, no shadows: a strip is
  flat.
- **Badges.** Frame badges ("FR. 12", "24 FR.", "PICKED"): small
  bordered desk labels, 1px `--dot` border, never filled, never
  amber-filled. PICKED adds the pencil tick.
- **Alerts.** Darkroom-log alerts: a bordered block in the tray band
  style with the desk's line (§12) — information in `--tray`, warning
  in `--fixer-deep`, error as a "did not develop" block (§6.12's
  frame treatment). No toast-autodismiss for errors; the log keeps
  what it records until the visitor closes it.
- **Pagination.** Sheet pagination: "SHEET 1 OF 4" with PREV / NEXT
  SHEET desk links ruled in pencil on hover. Numbered pages, if
  needed, are frame numbers in a row — the visitor is turning sheets,
  not paging a database.
- **Modals.** The inspection loupe: a picked print enlarged — the
  frame at pitch-5 centred on a `--tray-deep` ground, its full
  caption beneath, close as a desk link ("RETURN TO THE SHEET").
  Opens 300ms `--ease-fix` (door-black fade, then the print), focus
  trapped, Esc returns to the frame. This is the *only* modal pattern;
  nothing else on the site interrupts.
- **Toasts.** One: the filed confirmation (§6.16) — and it is not a
  toast but the stamped card itself. No other toasts exist in this
  theme.
- **Tabs.** Sheet tabs on listing pages: binder divider tabs — labels
  on `--paper-warm` tabs rising 6px above the sheet's top border, the
  active tab in `--paper` with its label in `--dot`, switching
  re-deals the sheet's frames (§6.3, marks persisted).
- **Accordions.** The caption expansion (§6.9) is the accordion
  pattern; FAQ-style accordions, if a site needs them, use the same
  mechanics with a pencil-plus that rotates to a tick — and their
  content is set in Newsreader, because answers are story, not desk.
- **Search.** Archive search: a ruled-line field (§6.16 pattern) with
  results dealt as print cards (§6.15); the empty result is a blank
  frame (§6.18's language at card size: "NO FRAMES MATCH — THE DESK
  KEEPS THE NEGATIVES BY YEAR AND PLACE" + filter suggestions).
- **Progress.** The exposure strip (§6.5) is the only progress
  component. Loading bars are forbidden; loading is developing
  (§6.12).
- **Tooltips.** Desk notes: a small `--dot` block, `--paper` Archivo
  11px text, appearing 400ms after hover/focus, naming the
  instrument's fact ("Band 4 of 8 — you are halfway through the
  roll"). Never on touch.
- **Dividers.** Hairlines in `--mark-hair`; sheet boundaries are the
  2px `--mark-line`. The grease-pencil rule (drawn, `--fixer`) is
  reserved for the current-nav indicator and the hero's instruction —
  a divider that means something.
- **Skeleton.** §6.12's developing frame. No grey-pulse skeletons
  exist in this theme.

---

## 12. Content & copywriting voice

Two voices (§3), kept apart with discipline.

**The desk (Archivo) — records, never sells.**

- *Captions, the form of the theme:* `NAME — Place, date. Instruction.`
  ✓ "A. OKAFOR — Dockside, 14 Mar 1987. Cropped to the hands, per the
  desk." ✓ "E. MARSH — The darkroom, Mill Lane, Oct 1989. Not to be
  cropped." ✗ "Stunning capture by our talented team!" — the desk
  does not exclaim; there are no exclamation marks in desk type,
  anywhere, ever.
- *Labels & buttons:* imperatives of the darkroom. ✓ "Pick this
  print", "File the request", "Return to the sheet", "View the
  sheet". ✗ "Get started", "Learn more", "Submit".
- *Errors, the log's voice:* what happened, in the process's terms,
  plus the remedy. ✓ "This frame did not develop. Check the frame
  number and file again." ✓ (form) "The desk needs a date — prints
  are logged by day." ✗ "Oops! Something went wrong."
- *Empty states:* ✓ "No frames on this sheet yet. The roll is still
  in the camera." — an empty state is a true statement about the
  archive, never an apology.

**The story (Newsreader) — the essayist who captions nothing.**

- *Headlines:* sentence case, concrete, built on the photograph's
  fact. ✓ "She taught the town to look." ✓ "The last ferry crew of
  the old dock." ✗ "Capturing Moments, Creating Memories." ✗ any
  headline containing "vintage", "timeless" or "journey".
- *Standfirsts:* one sentence that states the distance idea plainly
  when the hero needs it (§6.1): "Every photograph on this page is a
  field of dots until you give it distance."
- *Body:* written at reading distance — specific names, dates,
  places; the essay trusts the same facts the captions record.

**Banned words (both voices):** vintage, retro, timeless, stunning,
delve, elevate, seamless, "in today's world". **Owned words:** frame,
sheet, roll, desk, tray, fixer, pitch, resolve, "not to be cropped".

---

## 13. Full-page scroll choreography map

The home page, top to footer, every beat in order. (Detail and listing
pages follow the same order with their own frame sets.)

1. **Arrival.** Door-black lifts (first visit) or the sheet is simply
   there (repeat). Skeleton frames develop in load order, hero first
   (§6.12). Header present; nav underline drawn.
2. **The hero field.** `--pitch-0` dots, scale 1.6. Counter reads FR.
   00. The instruction stands: SCROLL TO STEP BACK.
3. **The resolve (0–120vh).** §6.1's ladder, the caption rising across
   the last quarter, face-circle at completion, hero stamp taps,
   instruction long gone.
4. **Release into sheet 1.** The hero becomes FR. 01; the counter
   starts its true count; sheet 1's header states its range.
5. **Sheet 1 develops.** Frames deal in grid order (§6.3); the focus
   band (§6.2) travels; the first portraits circle; stamps tap one by
   one, ≥90ms apart, as the desk works down the sheet.
6. **First pick (wherever the visitor chooses).** §6.9's resolve +
   caption; the tally rolls; the sheet's shimmer stills on the held
   print.
7. **Tray band 1 — the process.** Ground drops to `--tray`; grain
   breathes; the process copy sits in paper type; a single full-width
   frame (the darkroom itself) sharpens at centre. The page's one
   rest.
8. **Sheet 2.** As beat 5, with the band now practised — the visitor
   reads faster; the choreography does not change to reward them, it
   simply keeps its discipline.
9. **The data line.** §6.11's counts, in a ruled band: frames on the
   roll, prints picked, sheets in the archive — all true, all
   tabular.
10. **The request.** Tray band 2: the log card (§6.16), reference
    line carrying the visitor's pick; the filed stamp is the page's
    loudest moment and it is 180ms long.
11. **The fixer.** Footer (§6.17): roll-edge marquee travelling,
    counts final, links in desk columns. Stillness. The roll has
    passed through the fixer; what remains is permanent.

**Emotional arc, stated once:** abstraction → suspicion → recognition
→ work → rest → mastery → transaction → permanence. If a build's page
cannot be described in those beats, its choreography has drifted.

---

## 14. Whole-page performance budget

**Asset ceilings (home page).**

| Asset | Ceiling | Notes |
|---|---|---|
| HTML + CSS + JS | ≤ 260KB (gz) | The theme's JS is one loop + registries; it should be far under |
| Fonts | ≤ 120KB | Archivo (500/600/700) + Newsreader (400/500/600 + italic), subset, `font-display: swap` |
| Hero rendition set | ≤ 900KB | 6 pitches at 0.75× display resolution, WebP q80 |
| Per section image, all renditions | ≤ 180KB | 3–4 pitches at 0.75× |
| Per card image, all renditions | ≤ 90KB | 2 pitches |
| Page total (initial view) | ≤ 1.6MB | Renditions below the fold load on approach (IO at 1.5 viewports) |

**The rendition pipeline (build-time, mandatory).** Halftones are
developed offline: a build script (ImageMagick/Sharp) renders each
photograph at the ladder's pitches with the classic 45° screen for
black, dots in pure `--dot` on `--paper`-white image ground, exported
as WebP. Live in-browser halftone (canvas filters, SVG filter chains)
is forbidden for content images — it is slower, inconsistent across
GPUs, and (§9) it always ends up applied to text by someone.

**Frame budget.** The shared loop's total per-frame cost ≤ 4ms on a
mid-range Android: §6.1 ≤ 1.2ms, §6.2 ≤ 0.3ms × ≤ 6 live frames,
§6.10 ≤ 0.3ms, instruments ≤ 0.2ms. Long tasks ≤ 50ms; rendition
swaps are preloaded so a crossfade never waits on the network
mid-scroll. CLS: 0 for all theme elements (frames reserve aspect
boxes; captions reserve their expansion space per §6.9).

**Cut order when the budget is exceeded** (in this order, documented
in the build's notes): 1) §6.6 shimmer; 2) tray-grain breathing;
3) §6.2 ladder 3 rungs → 2; 4) hero renditions 6 → 4; 5) §6.10
tray-lift. Never cut: the resolve itself, the counters' truth, the
fallbacks, the reduced-motion variant.

**Measurement protocol.** Budgets are verified, not assumed: (a) the
loop's per-frame cost is measured with the Performance API over a
full-page scroll on a Moto G-class device or 4× CPU-throttled
desktop, taking the 95th-percentile frame, not the mean — the mean
hides the jank that visitors feel; (b) rendition weights are audited
from the build output manifest, per image, against the ceilings
above, and the manifest ships with the build's notes; (c) LCP is the
hero's *base* image (the sharp portrait is the LCP candidate even
while its overlays show dots — the browser paints the stack, and the
audit confirms the hero frame paints within 2.5s on a mid-tier
connection, dot field included); (d) INP is measured on the pick
(§6.9): click-to-caption-open must land under 200ms, which the 500ms
resolve does not threaten because the press feedback is instant and
the caption begins at t=200ms by design. A build that cannot produce
these four measurements has not finished §15, whatever it looks like.

---

## 15. Build-order checklist

1. **Static sharp site first:** all pages complete with sharp images,
   drawn marks, expanded captions, working form — passes §10 items
   1 and 6 with no JS written yet.
2. **Tokens & type:** palette (§2), pitch ladder, easings, type scale
   (§3) as CSS custom properties; the dark scheme (§2) stubbed.
3. **Layout:** sheets, rail, frames, mats (§4); print stylesheet.
4. **Rendition pipeline:** the build script (§14) + a sample image
   audited at every pitch against the original entry's intent.
5. **Instruments:** frame registry, counter, exposure strip (§6.5,
   §6.11) — before any beauty, the page must count honestly.
6. **The hero resolve** (§6.1, §6.14) with its watchdog; gate item 5
   tested at 4× throttle before proceeding.
7. **The focus band** (§6.2) + focal-point data pass over all frames.
8. **Marks & reveals:** §6.3 reveals, §6.4 circles, §6.7 stamps, with
   their one-shot queue.
9. **Handling:** §6.8 hover, §6.9 pick, §6.10 tilt; pick → form
   reference wiring (§6.16).
10. **Ambient:** §6.6 shimmer + grain, gated and capped.
11. **States & edges:** skeleton/door (§6.12), footer (§6.17), 404
    (§6.18), filtering recounts (§6.15/§6.11).
12. **Reduced-motion pass:** every element's variant implemented and
    diffed against its static state — same information, zero motion.
13. **Fallback pass:** JS-off, stall, missing-rendition and error
    drills (§10 items 1–3).
14. **Quality gate:** §10 in full, on real hardware, with evidence
    filed.
