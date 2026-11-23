# 43. Forest Floor, Magnified — Expanded (v1 + v2)

> Expansion of theme #43 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same ten signature elements —
> deepened, never redesigned — plus eight page-family elements.

## 1. Concept & world

Most websites are read at arm's length. This one is read **on your
knees, through a lens**. The browser is a magnifying glass held over
the forest floor: moss cushions, fern tips, beetle shells and leaf
litter at twenty times life size, and the content is discovered the
way specimens are discovered — by getting close, by looking slowly,
by finding that the square metre you thought was empty is crowded.
A patch of ground that reads as "some leaves" at standing height
contains, at ×20, a moss sporophyte forest, a springtail, the worked
edge of a beetle's elytron and dew held in spheres by surface tension.
The theme's whole argument is that **scale is attention**: the page
does not shout louder as you descend; it resolves finer.

The world is the hand lens and the field notebook, treated as a
complete interface vocabulary rather than a texture. The page has a
**field of view** (the hero frame, where the lens first finds its
subject), **specimens** (the content objects — cards, figures,
records — each presented at a stated magnification inside a
depth-of-field frame whose centre is sharp and whose edges fall
soft), **the margin leaf** (a single drawn leaf running down the
page's edge, whose vein line carries the snail that measures the
reading), **the anatomy plate** (the section where a leaf's vein
system draws itself, because in this world diagrams grow their
subjects), and **the litter** (the footer's deep band of fallen
leaves, where the colophon lies and a beetle crosses once, unhurried,
ignoring everyone). Nothing on the page is leaf-clip-art decoration.
The floor is the information architecture: **what is small is not
minor here; it is the content, and the lens is how you read it.**

**The theme's one law: the lens never invents a specimen.** Every
figure the page prints is a measurement taken from the page itself.
The magnification printed beside a frame (×20) is the scale actually
rendered inside that frame — the ratio between the specimen's drawn
size and its stated true size, both printed on its label. The census
figure ("143 species") is the count of specimen entries the page
actually carries, generated from the same survey object that builds
the cards, the index and the footer tally — never typed by hand. The
scale bar under a specimen is drawn from the same factor as the frame
above it, so a visitor with a ruler can check the page's honesty.
A Forest Floor build that prints ×20 over a ×6 render, or a species
count no DOM produced, has not bent the theme — it has faked the
field notes, and the quality gate (§10) fails it on sight. Everything
else in this theme is craft. That one is field ethics.

**Examination is the interaction model.** The visitor's acts are a
naturalist's acts: they bring the lens to a specimen and the specimen
sharpens (§6.6), they pin a label onto what they have identified
(§6.9), they follow the vein system to understand the leaf (§6.8),
and their progress is kept by the floor's slowest resident at its
own pace (§6.5). The site does not have users skimming a feed; it
has examiners who understand that the floor rewards whoever slows
down. That is why the theme fits content with genuine fine
structure — natural history, microscopy, craft at small scale,
archives of small things, any subject whose detail survives being
looked at closely — and why it curdles around anything coarse,
urgent or interchangeable: a lens held over a billboard is a joke,
and the page knows it.

**Best-fit sites and audiences.**

- Natural history and field science: museums' collection pages,
  nature reserves, bryology and entomology societies, citizen-science
  surveys — content that already thinks in specimens, sites and
  counts, where a species name is a real curatorial fact.
- Microscopy and imaging: microscope makers, imaging labs, materials
  science at small scale — anywhere the product literally is a lens
  and the magnification figures are specifications, not adjectives.
- Small-scale craft: watchmaking, miniature work, seed keeping,
  embroidery, model engineering — trades whose value is in work too
  fine to see unaided, stated in real measurements.
- Gardens, soil and ground: soil health consultancies, moss and
  fern nurseries, rewilding projects — where the floor is the
  product and its inhabitants are the evidence.
- Education in biology: course and exhibit pages where the lens is
  the lesson plan — the student examines, labels and counts, and the
  page keeps the notebook.

**When NOT to use it.**

- For coarse content. If every item is large and self-evident (a
  dashboard, a price list, a settings page), magnification is a lie
  the layout tells; the frames become green rectangles and the theme
  is a costume.
- For urgent transactions. Examination is paced — the focus pull
  takes its 1.5s, the snail does not hurry. A visitor paying a bill
  in forty seconds should not be handed a hand lens.
- Where the small things are invented. If the publisher cannot name
  the specimens — real species, real measurements, real counts —
  the floor is a screensaver. Choose another theme.
- For content that must be scanned at speed. The theme's whole
  argument is the close look; a page whose readers will only ever
  skim the canopy wastes it and misrepresents the detail beneath.
- For audiences who must never be asked to hover or dwell. The lens
  (§6.6) is the theme's central instrument; touch and keyboard carry
  full equivalents (§6.6's state matrix), but a context where no
  examination of any kind is possible has no use for this floor.

## 2. Palette

Five anchors, inherited unchanged. The palette is a square metre of
woodland floor in overcast light: deep shade, two greens of growth,
one pale lichen light, and the brown of last year's leaves. Nothing
else is admitted; every other colour on the page is one of these
five, tinted, shaded, or set at an opacity over its own ground.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--undergrowth` | `#1C2A1A` | The shade: page ground, hero depth, the dark the lens looks into | ~34% of pixels | Lichen on it: **9.30:1** (AAA) — the default text pairing. Dew on it: 13.21:1. Fern-pale on it: 7.83:1 (AAA). New fern on it: 4.78:1 (AA) — new fern may letter headings here, never on moss. Leaf litter on it: 2.60:1 — line-work and grounds only, never text. |
| `--moss` | `#3E5C3A` | The living cushion: mid-page section grounds, frame depths, hover states | ~26% of pixels | Lichen on it: **4.64:1** (AA) — body text on moss is lichen, minimum 16px. Lichen-pale on it: 6.01:1. Fern-pale on it: 3.91:1 — ≥20px display only. New fern on moss: 2.38:1 — forbidden for text in any size; the two growth greens are neighbours, not a pairing. |
| `--new-fern` | `#7A9B5A` | New growth: unfurl accents, the vein system, current-position marks, glints' green edge | ~10% of pixels | On undergrowth 4.78:1 (AA); on humus 5.60:1. It is a drawing colour and a large-type colour, never a body-text colour — body text in new fern is a gate failure (§10). |
| `--lichen` | `#C9D18B` | The pale light: body text on dark grounds, specimen labels, the snail's leaf's lit edge | ~22% of pixels | On undergrowth 9.30:1; on moss-deep 6.60:1; on moss 4.64:1; on leaf litter 3.58:1 — ≥24px display only on litter, never body. Undergrowth on lichen: 9.30:1 — lichen grounds (label tags, §6.9) carry undergrowth text. |
| `--litter` | `#8C5A33` | The fallen layer: the footer band, label-tag leather, frame rims, the beetle's road | ~8% of pixels | Dew on it: 5.09:1 (AA) — display and apparatus only. Lichen-pale on it: 4.63:1 (AA, ≥16px). Undergrowth on it: 2.60:1 — forbidden; litter never carries dark text. Litter is a shallow band, never a full section ground: the floor's dead layer is thin by law (§4). |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--humus` | `#121B11` | Undergrowth deepened: the footer's depth below the litter, the pinned fern's frame well (§6.3), skeleton grounds. Lichen on it **10.90:1**; lichen-pale on it 14.11:1. |
| `--moss-deep` | `#2C4429` | Moss shaded: specimen-card grounds on undergrowth, the notebook form's sheet (§6.15). Lichen on it **6.60:1** (AA); fern-pale on it 5.56:1. |
| `--fern-pale` | `#A8C48A` | New fern lightened toward lichen: the only growth green permitted for text — on undergrowth **7.83:1** (AAA), on moss-deep 5.56:1, on moss 3.91:1 (≥20px only). |
| `--lichen-pale` | `#E3EAC0` | Lichen lightened: display text on moss (6.01:1), the focus pull's final sharpness tint, label-tag highlights. |
| `--dew` | `#EAF3E4` | Almost-white green: dew speculars (§6.3, §6.7), glint cores, text on litter bands at display size (5.09:1). A light colour, never a ground. |
| `--litter-deep` | `#6E4525` | Litter shaded: the label tag's leather (§6.9), footer band edges, frame rims on moss. Dew on it **7.26:1** (AAA); lichen on it 5.11:1. |
| `--spore` | `rgba(201,209,139,.45)` | Lichen at 45%: the drifting bokeh grain (§5) and the slime sheen's tint (§6.5). Decorative only; content beneath must meet contrast with the grain removed. |

**Dark-mode behaviour: the theme does not invert — the floor is
already shade.** There is no light scheme to flip to; the page *is*
a descent from overcast light into undergrowth. Under
`prefers-color-scheme: dark`, the page is read as **the floor at
dusk**: `--undergrowth` deepens to `--humus` (`#121B11`) as the
page ground, lichen text holds (contrast rises to 10.90:1), dew
glints dim by 30% (dew at dusk does not flare), and the litter band
darkens to `--litter-deep` with its dew lettering rising to 7.26:1.
Moss and new fern are unchanged: moss at dusk is moss. A build that
inverts the lichen label tags to dark grounds has not made a dark
mode; it has turned the labels face-down, and §10 fails it.

**Pairing law.** Body text is lichen on undergrowth, humus and
moss-deep; lichen at ≥16px on moss; undergrowth on lichen and
lichen-pale (labels and tags); fern-pale for secondary text on
undergrowth and moss-deep; dew for display on litter. Any other
pairing is a build error, not a variation. In particular: new fern
never sets body text anywhere, and no text of any size is set in
moss on undergrowth (2.00:1) — moss is a ground, not an ink.


## 3. Typography

Two typefaces, inherited unchanged. **Fraunces** is the field voice —
soft, organic, set with its optical sizing open (`opsz` 72+ at
display sizes, so the letterforms swell like the specimens) — and
sets all display, headings, section titles and specimen names.
**Karla** is the notebook voice and sets body text, captions, labels
and all data. Figures (magnifications, counts, measurements) are set
in Karla with `font-variant-numeric: tabular-nums`, never in a mono:
the naturalist's numbers are written in the notebook by hand, not
typed by a machine. There is no third typeface. Emphasis inside
Fraunces is weight and optical size; inside Karla, italic — and
Karla italic is reserved for Latin binomials, which are always set
in italic by scientific law, on this page as in every flora.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Section title (fern title) | Fraunces 560, opsz 100 | 38–60px / 1.04, `clamp(2.375rem, 5.5vw, 3.75rem)` | −0.01em | Set in lichen on its ground; the section's specimen count is lettered beneath it in apparatus before any prose (§6.2). |
| Display / hero headline | Fraunces 600, opsz 144 | 54–92px / 0.98 | −0.015em | The lens's first subject (§6.11). Never more than 3 lines; its letters are the ones that swell (§6.11), so words stay short enough to swell one by one. |
| Specimen name | Fraunces 560 | 21–27px / 1.15 | 0 | The common name as the field guide gives it, followed by the binomial in Karla italic at 0.62× size on the same line: "Dog lichen, *Peltigera canina*". |
| Heading (in-section) | Fraunces 560 | 23–30px / 1.12 | −0.005em | One per section region; headings name organisms or structures, never abstractions ("The vein system", not "Our approach"). |
| Body | Karla 400 | 16.5–18.5px / 1.62 | 0 | Measure 56–64ch. On moss, 17px minimum — the 4.64:1 pairing earns AA at size, not below it. |
| Caption / label | Karla 400 | 13.5–15px / 1.5 | 0 | The notebook's voice: what the specimen is, where it was found, at what magnification it is drawn. |
| Apparatus (magnifications, counts, scale) | Karla 700 | 11–13px, uppercase | +0.13em | Magnifications ("×20"), census figures, scale-bar labels, the snail's percentage in the reduced-motion variant. Uppercase is rationed to apparatus only. |
| Price (collection / booking) | Fraunces 600 | 30–40px / 1.05, tabular via Karla fallback figures | 0 | Set in lichen on moss-deep; a price here is a specimen label — named, measured, sourced — not a shout. |

**Type laws.**

1. **The name is given before the story.** Every specimen opens with
   its common name and binomial in the specimen-name style; prose
   follows. A card that begins with a paragraph has skipped its own
   identification.
2. **Magnification is lettered before it is admired.** Every frame
   states its × figure in apparatus at its rim before the eye reaches
   the specimen (§6.13). A frame without a stated magnification is a
   picture, not a specimen.
3. **Binomials are always italic, always Karla.** *Peltigera
   canina* never appears in Fraunces and never in roman. The law is
   not the theme's invention — it is taxonomy's — and the page obeys
   it the way it obeys the one law (§1).
4. **Figures are measurements.** Any number the page asserts
   (magnification, count, millimetre, price) is set in tabular
   figures and is subject to the one law: computed from the survey
   object or traceable to publisher data (§6.14).
5. **No centred text below the hero.** The field of view may centre
   its headline; the floor itself is left-aligned like a notebook
   page. Centred body text among the specimens is a gate failure.

## 4. Layout language

**The section is a patch of floor.** The page is one continuous
square metre, examined in patches: full-bleed horizontal bands, each
a named patch ("The moss cushion", "The litter layer", "The vein
system"), stacked in the order a kneeling examiner would work across
the ground — living growth first, then structure, then the fallen
layer, then the record. Patches meet at **soft boundaries**: a
depth-of-field edge, a 24–48px band where the ground falls out of
focus (blur applied to a background layer only, never to content),
not a ruled line and never a wave divider borrowed from a beach
theme. The boundary treatment of each patch is authored once per
build and reused at every breakpoint; the floor does not re-grow
itself per screen size.

**Examination order is content order.** Patches appear in the order
the examination deepens: the conspicuous first (the hero's subject),
then the easily missed (the small, the camouflaged, the under-leaf),
then the record (counts, the notebook, the colophon). The DOM order
is the patch order is the reading order — a screen reader examines
the same floor. Reordering patches for visual variety is forbidden;
if the survey changes, the change is recorded in the field record
(§6.16).

**The margin leaf.** On ≥1200px, the right 88px of every patch is
the **margin leaf**: a single drawn leaf, spine vertical, whose
midrib is the vein line the snail traverses (§6.5) and whose lateral
veins mark the section boundaries — one lateral vein per patch,
joining the midrib exactly where its patch begins. The margin leaf
is the page's instrument panel; nothing decorative is placed there,
and no content may stray into it. Below 1200px the leaf is cut
(§6.5's breakpoints); the snail's duties pass to a plain percentage
in the header (§6.12).

**Depth-of-field frames.** A specimen sits inside its frame the way
it sits under the lens: centre sharp, edges soft. The frame is a
rectangle with a radial focus falloff — the specimen's centre 62%
is rendered at full sharpness, the outer band falls to a 2px blur on
the *image layer only*. Frames never overlap patches; a specimen
half in the moss and half in the litter is a surveying error.
Corner radius is 50% only on the lens zone (§6.6) and the dew drops;
specimen frames are rectangular with 2px corners — a field guide's
plates are not rounded, and nothing on this floor floats: no drop
shadows on cards, depth here is focal, never cast.

**Density law.** Density falls as the examination deepens. The
hero's patch holds one subject. Early patches may run two columns of
specimens (the conspicuous layer is crowded); the anatomy patch is
one diagram and its caption; the litter holds exactly what it must:
the record, the notebook's echo, the colophon. A final patch as
dense as the first has misread its own floor — by the end of a real
examination, the notebook is fuller and the ground quieter.

**The litter does not move.** The final band has no parallax, no
drift, no glint cycle; its only motion is the beetle (§6.10), which
is a resident, not an effect. After a page of looking, stillness is
the litter's content statement.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-focus` | `cubic-bezier(.25,.7,.25,1)` | The lens settling: quick approach, long fine settle | Focus pull (§6.1), refocus transition (§6.17), DoF frame settle (§6.13) |
| `--ease-unfurl` | `cubic-bezier(.55,.06,.25,1)` | The frond unrolling: held at the coil, then a release that eases out | Fern unfurl titles (§6.2), vein draw's laterals (§6.8) |
| `--ease-creep` | `cubic-bezier(.45,.05,.55,.95)` | Creature pace: near-linear, soft at both ends, never hurried | Snail (§6.5), beetle (§6.10), letter swell (§6.11) |
| `--ease-glint` | `cubic-bezier(.2,.9,.3,1)` | A flare: fast rise, slow decay, like light leaving a wet surface | Dew glints (§6.7), specular shifts (§6.3), label pin's landing flash (§6.9) |
| `--ease-drop` | `cubic-bezier(.5,0,.8,.4)` | A small thing falling a small distance: gravity in, soft land, no bounce | Label pin (§6.9), notebook submit (§6.15), card placement (§6.13) |

**Every motion term, translated into the floor's language:**

- **Scroll-triggered reveals** are placings: specimen cards are set
  down under the lens one by one (§6.13); titles unfurl (§6.2);
  nothing fades up out of nowhere — on this floor things are
  *found*, and finding has an instrument.
- **Scroll scrub** is the examination itself: the snail (§6.5), the
  dew speculars on the pinned fern (§6.3), the ground tracking
  (§6.4) and the letter swell's reading position are pure functions
  of scroll position, driven by the shared loop.
- **Parallax** is stratigraphic: three depths of ground drift at
  creature speeds (§6.4) — litter at 0.94, moss at 1.0, fern
  silhouettes at 1.05, horizontally-biased like a camera crawling.
  There is no decorative background parallax; the ground is the
  content.
- **Pinned scenes:** exactly two — the dew fern (§6.3) and the
  anatomy plate's vein draw window (§6.8). Pinning anywhere else is
  refused: a floor is crawled across, not camped on.
- **Masked reveals** are the unfurl's spiral clip (§6.2) and the
  focus pull's radial mask (§6.1) — both masks are optics (a coil
  opening, a lens focusing), both reveal content that was printed
  and legible beneath them from first paint.
- **Blur-to-sharp is rationed to one licensed use:** the focus pull
  (§6.1) and its sibling the refocus transition (§6.17), each under
  the blur law below. Blur is never a per-section reveal: a specimen
  is never blurred to be revealed; it is placed (§6.13).
- **Kinetic typography is refused** except the hero headline's letter
  swell (§6.11): each letter magnified 1.0→1.14 in turn, once, at
  the surface. Type does not perform down on the floor.
- **Counters** are field figures (§6.14): magnification and census
  count when their patch is examined, in Karla tabular, stepped like
  a tally being written — and every figure obeys the one law.
- **Progress** is the snail (§6.5): position on the vein line
  against the whole leaf, with the percentage printed for assistive
  technology and for the reduced-motion variant. There is no
  progress bar.
- **Marquee is refused.** Nothing on a forest floor runs sideways
  forever. The nearest licensed motion is the spore drift, which
  falls, slowly, and stops at the litter.
- **Ambient loops:** exactly three — the dew glint cycle (§6.7), the
  spore drift (bokeh grain sinking at 6px/s through the hero and
  anatomy patches only), and the margin leaf's breathing sway
  (±0.4° over 9s, §6.5). All are sparse, slow, and cut first by the
  performance ladder (§14).
- **Micro-interactions:** the lens (§6.6), the label pin (§6.9), the
  glint answer (§6.7). Every interaction is an examiner's act.
- **Hover physics:** no magnetic pull, no tilt stages. A specimen
  under the lens is sharpened; a specimen under the pointer is lit
  by its own dew. The floor does not lean toward the visitor.
- **Page transitions** are a refocus (§6.17): the new page is
  focused, not faded to.
- **Smooth scrolling:** the floor is damp and the crawl is slow.
  The shared loop lerps scroll-driven values at `--lerp` 0.10;
  native scroll is never hijacked — the theme smooths its
  instruments, not the visitor's hand.
- **The shared loop law.** One `requestAnimationFrame` loop owns
  every scrubbed value (snail, speculars, tracking layers, swell,
  lens). Lerp 0.10 for positions, 0.14 for lights (glints and
  specular highlights). Elements that can be pure CSS (unfurl
  stagger, glint cycle) are; the loop writes only transform /
  opacity / custom properties, and stops writing a value when it
  settles within 0.1% of target.

**The blur law.** Blur exists on this page only as an entry effect,
under three hard rules: (1) blur is applied to background and image
layers only — text is never blurred at any moment, in any element,
at any breakpoint; (2) every blur resolves to 0 within a hard cap of
**1500ms** from its trigger, enforced by a watchdog independent of
the animation's own timeline; (3) the DOM ships sharp — every blurred
state exists only under a JS-armed root class, so no-JS, a killed
loop, or a failed script all present the finished, focused page.
The original entry's focus pull was specced at 1.8s end-to-end; the
reconciliation this expansion adopts is that the *blur* reaches 0 by
1500ms (the law) while the radial mask's final 8% settle completes
by 1800ms with the image already sharp — the ceremony may take
1.8s, the unfocus may not.

**Watchdog law.** Every reveal has a timer: if an element's observer
or the loop fails, its content stands in final state by the
element's stated deadline (unfurl 1400ms, placing 1200ms, vein draw
2600ms, focus pull 1500ms). The DOM ships examined; all pre-examined
states exist only under a JS-armed root class. No-JS is not a
degraded mode — it is the field guide with the looking already done.


## 6. Signature elements

### 6.1 Focus pull

- **What & why.** On load, the hero's background — a macro moss
  photograph at ×20 — begins out of focus and pulls sharp radially
  outward from the headline, like a lens finding its subject. It
  belongs because the headline is the lens's first subject: the page
  focuses on its own title before anything else, and the visitor
  learns in the first two seconds that this site is looked *through*,
  not merely looked at.
- **Structure.** A `<div class="field-of-view">` in the hero holding
  the moss plate as an `<img>` (or CSS background on a decorative
  layer), overlaid by a radial mask layer: a `radial-gradient` mask
  whose clear centre starts at the headline's centre point and whose
  radius is a custom property (`--focus-r`) written by the shared
  loop. The blurred copy of the plate sits beneath the sharp copy;
  the mask reveals the sharp copy outward. The headline and all hero
  text are siblings *above* both layers and are never filtered. The
  blurred state exists only under the JS-armed root class.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 500ms timer (the lens must not wait for a slow font
  to start focusing). The plate's blur runs 14px → 0 over 1500ms
  `--ease-focus` — the blur law's hard cap (§5). The mask radius runs
  12% → 140% of the hero's diagonal across 1800ms on the same easing,
  its final settle completing after the blur is already 0. Total
  ceremony ≤1.8s; a click, a keypress or the first scroll completes
  it instantly. It runs once per session (sessionStorage flag); a
  returning visitor gets the focused page at first paint.
- **States.** Focusing → focused (rest) → scrolled-past: the plate
  stays focused and joins the ground tracking (§6.4) as the hero's
  litter layer. It never re-blurs.
- **Content merge.** The pull is performed on the hero's own
  photograph, and its centre is the headline: remove the animation
  and the hero is a sharp plate with a title — the page loses the
  ceremony of the lens arriving, nothing else.
- **Failure fallback.** No JS: the plate stands sharp. Watchdog: the
  blur is forced to 0 at 1500ms and the mask removed at 1800ms
  regardless of the loop's health; if the image itself fails to
  load, the hero ground is `--undergrowth` with the headline set on
  it — the focus pull is skipped, not faked over an empty frame.
- **Reduced-motion variant.** The plate is sharp at first paint. The
  lens has already found its subject; only its arrival rests.
- **Performance budget & mobile variant.** One filter animation on
  one image layer + one mask property; the plate is a single
  responsive image ≤180KB. Mobile (<768px): the blur starts at 10px
  (cheaper filter radius), the mask is centred on the headline's
  first line, and the ceremony shortens to 1200ms blur / 1400ms mask.
- **Choreography timeline (v2).** t=0 fonts ready (or 500ms race
  lost) → t=0–1500 blur 14px→0 `--ease-focus` → t=0–1800 mask radius
  12%→140% → t≈900 the headline's letters begin their swell (§6.11)
  as the sharp centre passes them → t=1800 mask layer removed from
  the tree → ceremony over; the hero is a focused plate.
- **State matrix (v2).** *Rest:* focused plate. *Hover:* none — the
  pull is not an interactive element; the lens (§6.6) is the hero's
  hover instrument. *Focus:* any focus landing inside the hero
  completes the pull instantly (a keyboard visitor never waits for
  focus to read). *Active:* n/a. *Scrolled-past:* focused, tracking
  at the litter rate. *Disabled:* a hero without a plate runs no
  pull — the headline stands on undergrowth. *Touch:* no hover
  state; the pull runs on load as on desktop.
- **Breakpoints (v2).** ≥1200px: full ceremony as specced, mask
  centre at the headline's optical centre. 768–1199px: blur start
  12px, mask 1600ms. <768px: the mobile variant above; the plate is
  cropped to its centre 70% so the focused subject survives the
  narrow frame.
- **Edge cases & failure modes (v2).** *Slow image:* the pull is
  gated on the image's `load` event raced against 1200ms; a plate
  that arrives late fades in already sharp — a late photograph is
  never pulled into focus as a penalty. *Huge headline (3 lines):*
  the mask centre sits on the middle line; the swell (§6.11) still
  reads left to right. *Session flag set but image cache cold:* the
  plate fades in sharp over 300ms; no ceremony is owed twice.
- **Accessibility spec (v2).** The plate is decorative (`alt=""`,
  `aria-hidden` on the mask layer); the headline is a real `<h1>`
  in the DOM before the plate in reading order and is legible from
  first paint — the blur never touches it (§5's blur law). The pull
  is not announced; it carries no information. Focus order is DOM
  order.
- **Tokens consumed (v2).** `--undergrowth`, `--dew`,
  `--ease-focus`, `--dur-focus` (1500ms), `--dur-mask` (1800ms),
  `--blur-start` (14px), `--focus-r` (loop-written).

### 6.2 Fern unfurl titles

- **What & why.** Every section title reveals through a spiral
  clip-path mask that unrolls like a fern frond uncoiling — the
  crozier opens, the leaflets spread, the title stands grown. It
  belongs because headings here grow the way the organisms they name
  grow: typography as botany. A title that names a fern unfurls; a
  title that names the litter unfurls over leaf litter; the reveal
  is the section's first specimen.
- **Structure.** An `<h2 class="fern-title">` wrapped in a
  `.unfurl-frame` whose `clip-path` is an SVG-defined spiral path
  (authored once per build, scaled to the title's box). The title
  text is real DOM in final position, fully legible with the clip
  removed; the clip exists only under the JS-armed root class. A
  small drawn crozier (spiral SVG, 28px) sits at the title's left
  and unrolls with the same progress value — it is the title's own
  frond tip, not an icon pasted beside it.
- **Motion spec.** Trigger: the title's top crosses 72% of viewport
  height. The clip's spiral opens over 900ms `--ease-unfurl`,
  written by the shared loop as a scrubbed-then-released value: the
  first 30% of the opening is tied to scroll (the frond starts as
  you arrive), then releases to a timed finish so a stopped scroll
  never leaves a title half-coiled. The crozier rotates −120°→0°
  across the same 900ms. Titles unfurl once; scrolling back up never
  re-coils them.
- **States.** Coiled (JS-armed only) → unfurling → grown (rest).
  Scrolled-past: grown, still. A title jumped past by anchor
  navigation is grown instantly (the catch-up rule, §13).
- **Content merge.** The mask *is* the title's shape opening — the
  animation draws the same spiral the frond in the section's plate
  shows. Remove it and the title is a title; the section loses its
  germination, nothing else.
- **Failure fallback.** No JS: titles stand grown. Watchdog: any
  title not fully unclipped by 1400ms after its trigger is forced
  open; if `clip-path` path support fails, the frame falls back to a
  rectangular inset clip on the same timeline (the unroll becomes an
  opening curtain — plainer, never stranded).
- **Reduced-motion variant.** Titles stand grown; the crozier is
  drawn open. Growth is information about the section's subject;
  only its performance rests.
- **Performance budget & mobile variant.** One clip-path animation
  per title, ≤8 titles per page, never concurrent (the loop staggers
  triggers by patch). Mobile (<768px): the spiral path is replaced
  by its simplified 6-point version, duration 700ms, and the crozier
  shrinks to 20px.
- **Choreography timeline (v2).** t=0 title top crosses 72% →
  t=0–270 scroll-scrubbed opening (coil loosens as the visitor
  arrives) → t=270 release → t=270–900 timed unroll `--ease-unfurl`,
  leaflets of the clip opening in spiral order → t=900 crozier at
  rest, apparatus line (specimen count) fades in beneath → t=1400
  watchdog deadline passes unneeded.
- **State matrix (v2).** *Rest:* grown title. *Hover:* none (titles
  are not interactive; a title that is also a link takes §6.12's
  treatment). *Focus:* a title receiving focus via anchor jump is
  grown before focus lands (catch-up). *Active:* n/a.
  *Scrolled-past:* grown. *Disabled:* a section with no specimens
  still gets its title — the unfurl is the patch's, not the cards'.
  *Touch:* identical; no hover dependency exists to lose.
- **Breakpoints (v2).** ≥1200px: full spiral path, crozier 28px.
  768–1199px: spiral simplified to 10 points, 800ms. <768px: the
  mobile variant above; titles wrap to two lines and the clip scales
  to the two-line box (the path is defined in % so it scales without
  re-authoring).
- **Edge cases & failure modes (v2).** *Very long title (3 lines):*
  the spiral scales; the unroll order follows the spiral, not the
  reading order — the last visible glyph may be mid-title, which is
  correct frond behaviour and is why the release is timed, not
  scrubbed to the end. *Title at page load (first patch below the
  hero):* if it is already past 72% at first paint, it unfurls at
  t=300 after load, sequenced after the focus pull. *Loop killed:*
  the watchdog opens it; the crozier jumps open with it.
- **Accessibility spec (v2).** The title is a real heading in DOM
  order, legible from first paint beneath the clip (the clip is a
  visual mask, not a text concealment — screen readers never see the
  coil). The crozier is `aria-hidden`. Contrast: lichen on its
  ground per §2's law, in coiled and grown states alike (the clip
  reveals the same text, it does not restyle it).
- **Tokens consumed (v2).** `--lichen`, `--new-fern`, `--ease-unfurl`,
  `--dur-unfurl` (900ms), `--watchdog-unfurl` (1400ms).

### 6.3 Dew specular shift — the pinned fern

- **What & why.** A full-width fern plate pins for one viewport of
  scroll while the specular highlights on its dew drops travel
  across the drops' surfaces, scrubbed to scroll — as if the light
  itself were moving as the visitor leans along the frond. It
  belongs because the specimen photograph is alive at the scale the
  theme claims: its water responds to the reading light. This is
  the theme's one great pinned scene and its proof of scale.
- **Structure.** A `<figure class="pinned-fern">` inside a 200vh pin
  section: the fern plate as an `<img>`, and above it a specular
  layer — 14–22 dew drops, each an SVG ellipse pair (body + highlight)
  positioned on the plate's real dew points, authored per build from
  the photograph. Each highlight's offset is a custom property
  written by the shared loop from the pin's progress `q`. The
  caption and the plate's stated magnification (×20, §6.14) are real
  DOM below the frame, never inside the pin's moving layers.
- **Motion spec.** Pin: the section is 200vh; the figure sticks for
  the middle 100vh. As `q` runs 0→1, each highlight translates across
  its drop — up to 38% of the drop's width, direction set per drop by
  its authored light vector (all vectors agree: one sun, upper
  left) — and its opacity breathes 0.55→1→0.7 on `--ease-glint`.
  The plate itself scales 1.0→1.04 across the pin (the lens pressing
  closer, §5's licensed scale). Lerp 0.14 (lights). Leaving the pin,
  highlights rest at their q=1 positions; scrolling back reverses
  exactly — the light travels back.
- **States.** Approaching (highlights at rest positions) → pinned &
  shifting → released (rest at final positions). Hover on a drop:
  that drop answers with one glint (§6.7's flare, 300ms). Focus: the
  figure is not focusable; its caption link (§6.12) is, and focusing
  it does not disturb the pin.
- **Content merge.** The highlights are on the photograph's own dew,
  at positions the photograph actually holds; the caption's
  magnification is the frame's rendered scale (§1's law). Remove the
  pin and the page has a still fern with still dew — the specimen
  remains, the travelling light goes.
- **Failure fallback.** No JS: the figure stands unpinned, highlights
  at their authored rest positions (the SVG ships that way). Pin
  failure (sticky unsupported): the section is 100vh, the highlights
  scrub against the figure's own viewport passage instead — the
  light still travels, the frame just doesn't hold.
- **Reduced-motion variant.** No pin, no shift: the plate stands with
  its dew lit from the upper left, highlights printed at q=0.5
  (mid-light, the most legible state).
- **Performance budget & mobile variant.** One sticky element, ≤22
  SVG highlights on custom properties, one image ≤240KB. The loop
  writes only `--spec-x`/`--spec-o` per drop. Mobile (<768px): the
  pin is cut entirely — the plate scrolls normally, highlights scrub
  to its passage at half travel (19%), drops reduce to the 8 largest.
- **Choreography timeline (v2).** Pin engages (figure top reaches
  viewport top) → q 0–0.25: highlights begin travelling, plate at
  1.01 → q 0.25–0.75: full travel, opacity peak at q=0.5 → q
  0.75–1: travel completes, plate at 1.04, highlights settle at 0.7
  opacity → pin releases; the caption, already read, scrolls away
  with the figure.
- **State matrix (v2).** *Rest (outside pin):* highlights at nearest
  end state. *Hover (drop):* single glint, that drop only.
  *Focus:* none on the figure; caption link per §11's ring.
  *Active:* n/a. *Scrolled-past:* highlights at q=1 positions,
  plate released. *Disabled:* a plate with no authored dew points
  ships no specular layer — the pin still runs for the scale press,
  or is cut if the build declares it (the survey object records
  which). *Touch:* the pin and scrub are scroll-driven; touch
  scroll drives them identically.
- **Breakpoints (v2).** ≥1200px: 200vh section, full 22 drops.
  768–1199px: 170vh section, 16 drops, travel 30%. <768px: the
  mobile variant above (no pin, 8 drops, half travel).
- **Edge cases & failure modes (v2).** *Fast fling through the pin:*
  highlights are a pure function of `q`; a fling lands them at the
  correct end state with the lerp catching up in ≤400ms — the light
  is never left mid-drop by speed. *Image swapped by CMS:* dew
  points are authored coordinates; a build that swaps the plate must
  re-author the points or drop the layer (§10 gate) — highlights
  floating off dew is the theme's most visible lie. *Very tall
  viewport (>1100px):* the pin section extends to 220vh so the
  figure never pins shorter than one full screen of travel.
- **Accessibility spec (v2).** The plate carries real alt text ("A
  fern frond at twenty times life size; dew drops on the pinnae").
  The specular layer is `aria-hidden`; the light's travel conveys no
  information — the caption states the magnification and the finding
  in words. Contrast of the caption: lichen on undergrowth per §2.
- **Tokens consumed (v2).** `--humus`, `--dew`, `--lichen`,
  `--ease-glint`, `--lerp-light` (0.14), `--pin-fern` (200vh).


### 6.4 Ground tracking parallax

- **What & why.** The page's ground layers — leaf litter, moss,
  fern silhouettes — drift at three creature speeds as the visitor
  scrolls, horizontally-biased, like a camera crawling at ground
  level an inch above the floor. It belongs because depth on this
  floor is stratigraphic: the layers are the ground the content sits
  in, and their relative drift is how the eye knows which layer a
  specimen lies in. This is not background decoration; it is the
  floor's own strata moving under the reading.
- **Structure.** Each patch carries up to three decorative ground
  layers (`.ground-litter`, `.ground-moss`, `.ground-fern`) behind
  its content, each a repeating authored SVG or image strip at 120%
  of the patch's width. The shared loop writes one `--drift` value
  per layer from the patch's scroll progress; each layer translates
  X by `drift × (rate − 1) × 120px` and Y by `drift × (rate − 1) ×
  30px` — horizontal bias 4:1, the crawl's signature. Rates are the
  original entry's, fixed: litter 0.94, moss 1.0 (the reference
  layer — content rides with it), fern silhouettes 1.05.
- **Motion spec.** Pure scrub, no triggers: drift is a function of
  the patch's passage through the viewport, lerp 0.10. Maximum
  excursion: litter ∓7.2px X / ∓1.8px Y; fern ±6px X / ±1.5px Y —
  small numbers by law: the ground crawls, it does not slide. Layers
  are clipped by the patch; a layer never drifts across a boundary
  into the next patch (each patch has its own ground).
- **States.** Always at rest relative to scroll: the layers' state
  *is* the scroll position. Scrolled-past patches hold their end
  drift; returning reverses exactly. There is no hover, focus or
  active state — the ground does not respond to the pointer; the
  lens (§6.6) does.
- **Content merge.** The layers are the patch's named ground — the
  litter layer under the litter patch is last year's leaves, drawn
  from the same survey as the specimens above it. Remove the drift
  and the floor is a still photograph; the specimens and their order
  are untouched.
- **Failure fallback.** No JS / loop killed: layers stand at drift 0,
  aligned — the shipped position. A layer image that fails to load
  leaves the patch's flat ground colour (each ground token has a
  flat fallback: litter→`--litter` at 18% over undergrowth,
  moss→`--moss` at 22%, fern→none, silhouettes are the expendable
  layer).
- **Reduced-motion variant.** No drift: all layers at 0, the floor
  still. The strata are still named and ordered; only the crawl
  rests.
- **Performance budget & mobile variant.** ≤3 transformed layers per
  patch, ≤2 patches' layers active per frame (the loop writes only
  for patches within 1 viewport of the screen). Layers are
  `transform`-only, `will-change` forbidden (the loop's writes are
  the hint). Mobile (<768px): the fern silhouette layer is cut; the
  remaining two rates compress (0.96 / 1.0) and excursion halves.
- **Choreography timeline (v2).** Continuous: as a patch enters at
  the viewport's foot, drift 0 → as its centre crosses the
  viewport's centre, drift 0.5 → as it leaves at the top, drift 1.
  The beats are the reading itself; there is no start or end event
  to choreograph beyond the loop's lerp smoothing the visitor's
  hand.
- **State matrix (v2).** *Rest:* drift = f(scroll), layers aligned
  at 0 when the patch is centred at rest. *Hover:* none. *Focus:*
  none — focus never moves the ground (a keyboard reader's floor is
  still; §6.12's index carries their navigation). *Active:* n/a.
  *Scrolled-past:* end drift held. *Disabled:* a patch may ship one
  layer only (declared in the survey); the rates of the remaining
  layers do not change to compensate. *Touch:* touch scroll drives
  the same scrub; momentum scrolling is smoothed by the same lerp.
- **Breakpoints (v2).** ≥1200px: three layers, full excursion.
  768–1199px: three layers, excursion ×0.7. <768px: the mobile
  variant above.
- **Edge cases & failure modes (v2).** *Content taller than the
  design expects:* drift is computed from the patch's real height,
  so a long patch crawls proportionally slower — correct: more
  ground, same crawl. *A patch shorter than the viewport:* drift
  completes early and holds; layers never overshoot their 120%
  width (excursion is clamped to the authored overflow). *Scroll
  jump (anchor):* layers snap via the catch-up rule — the lerp is
  bypassed for jumps >2 viewports (§13).
- **Accessibility spec (v2).** All ground layers are `aria-hidden`
  and `pointer-events: none`; they carry no information (the patch's
  name and specimens are in the content layer). Drift never moves
  text: content rides the moss reference layer at rate 1.0, i.e. it
  does not move at all relative to the document.
- **Tokens consumed (v2).** `--litter`, `--moss`, `--undergrowth`,
  `--lerp` (0.10), `--drift-x` (120px), `--drift-y` (30px),
  `--rate-litter` (0.94), `--rate-moss` (1.0), `--rate-fern` (1.05).

### 6.5 Snail progress

- **What & why.** A tiny snail — drawn at the scale the theme claims,
  34px shell — traverses the midrib of the margin leaf (§4),
  scrubbed to scroll, leaving a faint slime sheen on the vein behind
  it. It is the page's progress indicator: progress at the pace of
  the floor's smallest resident, drawn on a leaf that is part of the
  layout. It belongs because this theme measures reading the way the
  floor measures travel — slowly, and by distance actually covered.
- **Structure.** The margin leaf is an SVG (spine + one lateral vein
  per patch, §4) fixed in the right margin on ≥1200px. The snail is
  an SVG group (shell spiral, body, two tentacles) positioned along
  the midrib path by the shared loop: `getPointAtLength(progress ×
  pathLength)`, with the snail's rotation set from the path tangent
  ±6°. Behind it, the midrib's travelled portion is overdrawn with
  the sheen: a second path in `--spore` at 2px, its dash offset set
  from the same progress. The percentage is a real `<output>` in the
  header (§6.12), updated from the same value — the snail and the
  number are one instrument printed twice.
- **Motion spec.** Pure scrub, lerp 0.10. The snail's tentacles sway
  ±3° on a 2.4s `--ease-creep` cycle while it travels, and still
  when the scroll rests for >1.5s (a resting snail retracts its
  sway, not its position). The sheen draws at the snail's exact pace
  — it is the snail's own trail, so it can never run ahead of it.
  At patch boundaries the snail crosses the lateral vein's junction
  without pause; the vein itself lights `--new-fern` for 600ms as
  the junction is crossed (the page noting its own chapters).
- **States.** Travelling → resting (scroll still >1.5s: sway stops,
  tentacles settle) → complete (at the leaf's tip: the snail stops,
  the final lateral vein lights, the header output reads the full
  figure). Scrolled back up: the snail reverses along the vein; the
  sheen *un-draws* behind it — the trail is this visit's, honestly
  re-measured in both directions.
- **Content merge.** The leaf's lateral veins *are* the section
  boundaries (§4), and the snail's position on the midrib is the
  reading position in the document — the progress is drawn on the
  page's own anatomy, not on a bar bolted to the viewport. Remove it
  and the header percentage remains; the page loses its pace-keeper,
  not its progress.
- **Failure fallback.** No JS: the snail rests at the leaf's base
  and the header prints the plain percentage statically (0% is never
  printed — no-JS prints "—" replaced by the patch count: "6
  patches", information the server knows). Watchdog: if the loop
  dies, the snail freezes where it is and the header output keeps
  updating from scroll events directly (the number is the fallback
  instrument; it is never allowed to die with the snail).
- **Reduced-motion variant.** No snail: the margin leaf stands
  undrawn by travel, and progress is the plain percentage in the
  header, per the original entry's standing rule. The leaf remains —
  it is layout; only its resident rests.
- **Performance budget & mobile variant.** One path lookup per frame
  (cached path length), two property writes. The snail is cut below
  1200px: at 768–1199px the header percentage alone serves; below
  768px the same, set in apparatus at the header's right. The margin
  leaf itself is cut below 1200px (§4).
- **Choreography timeline (v2).** Continuous: progress = document
  scroll fraction mapped through the midrib's length, so the snail
  moves fastest (in px) where the leaf is longest relative to
  content — the mapping is declared in the survey object (§6.16) so
  the snail, the header output and the choreography map (§13) can
  never disagree about where the reading is.
- **State matrix (v2).** *Rest:* snail at current progress, sway
  stilled after 1.5s. *Hover (snail):* none — it ignores the pointer
  completely; it is a resident, not a control. *Focus:* the snail is
  not focusable. *Active:* n/a. *Scrolled-past (complete):* snail at
  the tip, final vein lit. *Disabled:* on pages too short to scroll
  (<1.2 viewports) the leaf and snail are absent — progress on a
  page that fits on one screen is a fiction, and the theme does not
  print fictions. *Touch:* identical scrub; the snail never intercepts
  touches (`pointer-events: none` on the whole margin leaf).
- **Breakpoints (v2).** ≥1200px: full instrument as specced.
  768–1199px: snail and leaf cut; header percentage. <768px: header
  percentage, apparatus size.
- **Edge cases & failure modes (v2).** *Dynamic content growth
  (late-loaded patch):* path length and document height are
  re-measured on the post-load pass; the snail's fraction is
  preserved across the re-measure (it may move ≤20px as the leaf
  rescales — a resurvey, honestly absorbed). *Print:* the snail is
  hidden; the leaf prints with the sheen at the printed progress —
  the field guide's margin keeps the record of how far the print
  reader's page had been read on screen, or no sheen if never
  scrolled. *Browser find-in-page jump:* catch-up rule (§13) —
  snail snaps with the lerp bypassed.
- **Accessibility spec (v2).** The snail and leaf are `aria-hidden`.
  Progress is announced by the header `<output>` with
  `aria-live="off"` (it updates continuously; announcing it would be
  noise) and by the patch index's `aria-current` (§6.12), which is
  the accessible instrument. The percentage is available to AT at
  all breakpoints, not only where the snail is cut.
- **Tokens consumed (v2).** `--new-fern`, `--lichen`, `--spore`,
  `--ease-creep`, `--lerp` (0.10), `--snail-size` (34px).

### 6.6 Lens hover

- **What & why.** On desktop, a circular zone ~180px across around
  the pointer sharpens and slightly enlarges whatever it passes over
  — specimens, plates, the vein diagram — as if the visitor's hand
  lens were moving across the floor. It belongs because examination
  is the theme's interaction model (§1): the magnifier is the
  reading tool itself, applied to the specimens themselves, not a
  decoration following the mouse. The normal system cursor remains
  visible at the zone's centre at all times — the lens is a zone of
  focus in the page, not a cursor replacement.
- **Structure.** Each examinable surface (specimen frame §6.13,
  pinned fern §6.3, anatomy plate §6.8) carries two stacked copies
  of its image layer: the resting copy (rendered at the frame's
  stated magnification) and the lens copy (rendered at magnification
  ×1.06 sharper — pre-sharpened by being drawn from a higher-resolution
  source, never by a CSS filter trick). The lens copy is clipped to
  a circle (`--lens-x`, `--lens-y`, radius 90px) written by the
  shared loop from the pointer position, lerped at 0.14 so the lens
  glides a fraction behind the hand like a real glass on a cord.
  Text is never in either copy: the lens acts on image layers only,
  so type under the lens is the page's own type, unscaled and
  unblurred, always legible.
- **Motion spec.** Trigger: pointer movement over an examinable
  surface. The clip circle follows with lerp 0.14; the lens copy's
  scale is a constant 1.06 relative to the resting copy (the ×
  figure printed on the frame is the resting scale; the lens adds
  its own honest +6%, and the frame's rim letters "LENS +6%" in
  apparatus so the instrument declares itself, §1). Entering a
  surface: the circle's radius eases 0→90px over 240ms
  `--ease-focus`. Leaving: 90→0 over 180ms. The lens never engages
  during scroll (pointer stationary + page moving = no lens; it
  re-engages on the next pointer move) — a lens dragged by the page
  rather than the hand is a smear, not an instrument.
- **States.** Disengaged → engaging (240ms) → engaged → leaving
  (180ms). On touch: a long-press (350ms) on a specimen engages the
  lens centred on the touch point, held while the finger rests,
  released on lift — examination by finger is slower and the spec
  honours that. Keyboard: focusing a specimen card (§6.13) engages
  the lens centred on the card's specimen for as long as focus
  rests there — the keyboard examiner gets the same glass.
- **Content merge.** The lens magnifies the page's actual specimens
  at their actual positions; it is the theme's thesis performed by
  the visitor's own hand. Remove it and the specimens remain at
  their printed magnification — the page loses the visitor's
  instrument, not its content.
- **Failure fallback.** No JS: specimens stand at their printed
  magnification, sharp. If the high-resolution source fails, the
  lens copy falls back to the resting copy scaled 1.06 by transform
  (slightly soft — the rim's apparatus note is unchanged; the +6%
  is geometric, which the fallback still honours). Pointer events
  unsupported: the element is simply absent; nothing else depends
  on it.
- **Reduced-motion variant.** The lens does not follow the pointer.
  Instead, focusing or tapping a specimen toggles its frame to the
  +6% state statically (the whole frame, not a circle) until focus
  leaves — the examination is available, the gliding glass rests.
- **Performance budget & mobile variant.** One clipped layer per
  examinable surface, composited; the loop writes two custom
  properties per active surface, and only the surface under the
  pointer is ever active. Image cost: the lens copy is the same
  asset at a larger `srcset` step, ≤1.4× the resting copy's bytes.
  Mobile (<768px): the free-moving lens is cut; the long-press
  static variant (whole-frame +6%) serves instead — a small screen
  is itself a lens held close, and a second one is theatre.
- **Choreography timeline (v2).** Pointer enters a surface → t=0–240
  radius 0→90px `--ease-focus`, centre lerping to the pointer →
  engaged: centre follows at lerp 0.14 (the glass trails the hand by
  ~60ms at reading speed) → pointer leaves → t=0–180 radius →0 →
  disengaged. During scroll: radius collapses in 120ms; the next
  pointer move re-opens it at the new position.
- **State matrix (v2).** *Rest:* disengaged. *Hover:* engaged as
  specced. *Focus:* engaged centred on the focused specimen
  (keyboard parity). *Active (pointer down):* the lens holds —
  pressing is how a label gets pinned (§6.9), and the glass must not
  vanish at the moment of the act. *Scrolled-past:* disengaged.
  *Disabled:* surfaces the survey marks unexaminable (pure text
  plates) carry no lens copy; the pointer over them is an ordinary
  pointer. *Touch:* long-press variant as specced.
- **Breakpoints (v2).** ≥1200px: radius 90px, lerp 0.14.
  768–1199px: radius 76px. <768px: the static whole-frame variant
  only.
- **Edge cases & failure modes (v2).** *Pointer crosses two frames
  quickly:* only one lens is ever engaged; the old frame's circle
  collapses at double speed (90ms) so two glasses never coexist.
  *Lens at a frame's edge:* the circle clips at the frame — the
  glass shows the frame's rim, not the page beyond; the rim is part
  of the instrument. *High-DPI:* the lens copy's source step is
  chosen from `devicePixelRatio` so the +6% is sharp, not merely
  larger. *Pointer leaves the window:* collapse as on leave.
- **Accessibility spec (v2).** The lens is a visual instrument only:
  it changes no content, order or meaning, and is `aria-hidden` in
  both copies (the resting copy carries the alt text). Keyboard
  parity is via focus (above), with §11's focus ring on the card —
  the ring, not the lens, is the focus indicator. No information is
  available only through the lens: the +6% reveals comfort, never
  content (a build whose specimen is illegible without the lens
  fails §10).
- **Tokens consumed (v2).** `--ease-focus`, `--lerp-light` (0.14),
  `--lens-r` (90px), `--lens-scale` (1.06), `--lens-x`, `--lens-y`
  (loop-written).


### 6.7 Dew glint cycle

- **What & why.** Across the page's patches, dew drops catch the
  light in a slow, staggered glint cycle — each drop flares for
  300ms, one drop somewhere on the visible floor roughly every 2s.
  It belongs because the specimens keep signalling life at the edges
  of attention while the text is read: the floor is wet, inhabited
  and lit, even where the eye is not. It is the theme's heartbeat,
  and it is rationed like one.
- **Structure.** Dew drops are authored SVG elements inside the
  specimen frames and plates that carry them (the pinned fern's
  drops are §6.3's; other patches carry 2–6 drops each on their
  plates). Each drop has a glint child: a `--dew` ellipse at the
  drop's upper-left, opacity 0 at rest. A scheduler (one timer, not
  per-drop) picks the next drop from the *currently visible* set in
  authored order and fires its flare by toggling a class; CSS runs
  the flare. Drops off-screen are never scheduled — the cycle is a
  property of the seen floor.
- **Motion spec.** Each flare: opacity 0→0.95→0.25 (rest) over
  300ms `--ease-glint` — fast rise, slow decay. Interval: 2000ms
  ±400ms jitter (authored per build, seeded so the order is the
  same for every visitor: the floor's habits are consistent).
  Concurrency: at most 2 flares at once page-wide, and never two in
  the same frame. The cycle pauses entirely when the tab is hidden
  and when any patch's content is being lens-examined (§6.6) — the
  examiner's light outranks the ambient one.
- **States.** Resting (opacity 0.25 printed glint) → flaring (300ms)
  → resting. A drop hovered mid-cycle flares immediately out of turn
  (the visitor's own light, §6.3's rule generalised) and the
  scheduler skips it next round. Scrolled-past patches' drops leave
  the visible set and stop flaring.
- **Content merge.** The drops sit on the specimens' own water — the
  fern's dew, the moss's held rain — at positions the plates
  actually show. The glint is the plate's light behaving. Remove the
  cycle and every drop still stands printed with its resting glint;
  the floor loses its weather, not its water.
- **Failure fallback.** No JS: drops stand at resting glint. If the
  scheduler dies, CSS alone cannot fire flares — drops rest, and
  the page is still (a dead cycle is a calm morning, not an error
  state; nothing is stranded because nothing was hidden).
- **Reduced-motion variant.** No flares: all drops at resting glint,
  printed. Dew at rest is still dew.
- **Performance budget & mobile variant.** One timer, one class
  toggle per flare, opacity-only animation on ≤2 tiny elements at a
  time — the cheapest element in the theme. Mobile (<768px): the
  interval lengthens to 3200ms and only drops in the hero and the
  anatomy patch participate.
- **Choreography timeline (v2).** t=0 page settles → first flare at
  t≈2000 on the first authored visible drop → subsequent flares
  every ~2000ms walking the visible set in authored order, wrapping
  to the start when the set is exhausted → the walk re-surveys its
  visible set on every scroll settle (300ms after scroll ends).
- **State matrix (v2).** *Rest:* resting glint. *Hover (drop):*
  immediate flare, scheduler skips it once. *Focus:* drops are not
  focusable. *Active:* n/a. *Scrolled-past:* out of the set.
  *Disabled:* a plate with no dew carries no drops; the cycle walks
  the remaining set without gaps in its timing. *Touch:* a tap on a
  drop flares it (the hover rule via touch), with no other effect.
- **Breakpoints (v2).** ≥1200px: full cycle. 768–1199px: interval
  2600ms. <768px: the mobile variant above.
- **Edge cases & failure modes (v2).** *All drops scrolled past,
  none visible:* the scheduler idles (no timer churn) until the set
  is non-empty again. *A flare's drop is lens-engaged:* the ambient
  flare is suppressed; §6.6's light governs. *Battery-saver /
  `prefers-reduced-data`:* the cycle is cut entirely — ambience is
  the first thing the floor gives up (§14's cut order agrees).
- **Accessibility spec (v2).** Flares are `aria-hidden` decoration on
  already-described images; they convey nothing. The flare's peak
  (0.95 opacity on a ≤14px ellipse) is below any photosensitivity
  concern at 300ms and ≤2 concurrent; under reduced-motion they are
  absent entirely.
- **Tokens consumed (v2).** `--dew`, `--ease-glint`, `--dur-glint`
  (300ms), `--glint-interval` (2000ms).

### 6.8 Vein draw — the anatomy plate

- **What & why.** In the anatomy patch, a leaf's vein system
  SVG-draws itself — midrib first, then the lateral veins in growth
  order, then the fine tertiary web — while the caption beside it
  names each order as it appears. It belongs because the diagram
  grows its own subject: the drawing *is* the leaf forming, and the
  visitor learns the structure by watching it develop in the order
  the plant built it. It is the theme's teaching instrument.
- **Structure.** An inline SVG plate (authored per build, one leaf,
  ~40–70 paths): the midrib as one path, laterals grouped in growth
  order (basal to apical), tertiaries as a light web group. Each
  path ships with its final `stroke-dasharray` state printed — the
  leaf is complete in the DOM; the draw is armed only by JS adding
  dash offsets. Three caption lines beside the plate ("The midrib —
  the leaf's spine", "Lateral veins — one to each lobe", "The web —
  where the water finishes") each tied to its group's draw window.
  The margin leaf (§4) is this plate's small sibling: same drawing
  grammar, instrument scale.
- **Motion spec.** Trigger: the plate's top crosses 65% of viewport
  height; the patch pins for 130vh (the theme's second licensed
  pin, §5) and the draw is scrubbed to the pin's first 60%, then
  released to a timed finish. Midrib: 500ms `--ease-draw`-equivalent
  — here `--ease-unfurl` at its steadiest. Laterals: each 260ms,
  staggered 90ms in growth order. Tertiaries: fade-draw over 600ms
  as a group at 40% final opacity (the web is fainter in the leaf
  and in the drawing). Total draw ≈1.8s (the original entry's
  figure). Captions ink in (`--lichen` from 40% to full) as their
  group completes. Scrolled back up: the leaf stays drawn — growth
  is not reversed by looking away.
- **States.** Ungrown (JS-armed only) → drawing (per group) → grown
  (rest). Hover on a caption line: its vein group lights `--new-fern`
  at full strength for as long as the hover rests (the naming hand
  and the named structure answer each other). Focus on a caption
  (they are buttons, §11): same lighting, plus the plate scrolls
  into full view if partially cut.
- **Content merge.** The plate is the anatomy section's content —
  the thing being taught is the thing being drawn. The caption's
  three lines are the section's entire text argument; remove the
  draw and the leaf stands complete with its captions printed: the
  lesson remains, the growing goes.
- **Failure fallback.** No JS: the leaf stands fully drawn (dash
  offsets are JS-armed only). Watchdog: any group not drawn by
  2600ms after the trigger is set drawn instantly. Pin failure: the
  draw runs timed (not scrubbed) on the same trigger — the leaf
  grows on arrival instead of under the hand.
- **Reduced-motion variant.** The leaf stands drawn; captions
  printed at full ink; caption buttons still light their groups on
  focus/hover (a state change, not a motion).
- **Performance budget & mobile variant.** One SVG, ≤70 paths,
  dash-offset writes confined to the draw window; the pin's scrub
  writes one custom property consumed by the groups' offsets.
  Mobile (<768px): the pin is cut; the draw runs timed over 1400ms
  on entry; tertiary web ships pre-drawn (the small screen's leaf
  is a smaller leaf, honestly simplified and captioned as such).
- **Choreography timeline (v2).** Pin engages → q 0–0.2: midrib
  draws (500ms of scroll) → q 0.2–0.5: laterals in growth order,
  caption 1 inks at midrib's end, caption 2 as laterals pass half →
  q 0.5–0.6: tertiary web fades in, caption 3 inks → q 0.6: draw
  complete, pin continues to 1.0 as pure dwell (the visitor sits
  with the finished leaf) → pin releases.
- **State matrix (v2).** *Rest:* grown leaf, captions at full ink.
  *Hover (caption):* its group lights. *Focus (caption):* group
  lights + plate centred. *Active:* n/a. *Scrolled-past:* grown.
  *Disabled:* a build with no anatomy patch has no plate; §6.5's
  margin leaf still carries the grammar at instrument scale.
  *Touch:* caption tap = hover's lighting, held 1200ms.
- **Breakpoints (v2).** ≥1200px: pin 130vh, full web.
  768–1199px: pin 115vh, tertiaries at 30% opacity. <768px: the
  mobile variant above.
- **Edge cases & failure modes (v2).** *A leaf with many laterals
  (a big authored plate):* stagger compresses (90ms → max(40ms,
  900/laterals)) so the total never exceeds 2.2s; the watchdog
  scales to total + 400ms. *Visitor scrolls past the pin quickly:*
  the draw's timed release finishes it — a grown leaf is the only
  state a departing visitor can leave behind. *Caption text longer
  than the plate:* captions stack below the plate at <1200px
  (authored layout), the lighting grammar unchanged.
- **Accessibility spec (v2).** The SVG carries `role="img"` and a
  full text alternative ("A leaf's vein system: a central midrib,
  nine lateral veins, and a fine tertiary web"). Caption buttons are
  real `<button>`s with `aria-pressed` while their group is lit.
  The draw conveys sequence, which the captions also state in words
  ("first", "then", "last") — no information lives only in the
  animation.
- **Tokens consumed (v2).** `--new-fern`, `--lichen`, `--moss-deep`,
  `--ease-unfurl`, `--dur-vein` (1800ms), `--watchdog-vein` (2600ms),
  `--pin-anatomy` (130vh).

### 6.9 Label pin

- **What & why.** Clicking a specimen drops a small label tag onto
  it — the tag falls 10px, settles, and stays, lettered with the
  specimen's name and the date of the pinning. It belongs because
  collecting and labelling is the naturalist's act, performed on the
  content cards themselves: the visitor's pins are their field
  record of what they have identified, and the page keeps it for the
  session. A pinned specimen is a read specimen, and the page says
  so.
- **Structure.** Each specimen card (§6.13) has a label anchor point
  at its frame's lower-left. The tag is a DOM element (`.label-tag`)
  in `--litter-deep` leather with `--lichen` lettering: common name,
  binomial, and "PINNED" + the session date in apparatus. Tags are
  created on first pin (never pre-rendered for unpinned specimens),
  stored in sessionStorage as a list of specimen IDs, and restored
  instantly (no fall) on reload within the session. Clicking a
  pinned specimen again lifts its tag off (the unpin: the tag rises
  10px and fades over 200ms — the record is corrected, not punished).
- **Motion spec.** The pin: the tag appears 10px above its anchor,
  falls over 260ms `--ease-drop` with a 40ms settle overshoot of
  1px, and at landing its top edge flashes once `--ease-glint`
  (120ms) — the pin's glint, the smallest dew-flare in the theme.
  A soft pin shadow (2px, `--humus` at 40%) fades in across the
  fall. Subsequent pins on other specimens are independent; there is
  no queue and no page-wide ceremony.
- **States.** Unpinned → falling (260ms) → pinned (rest, persists).
  Hover on a pinned tag: it lifts 1px and its lettering brightens to
  `--lichen-pale` (the tag being read). Focus: the tag is part of
  the card's button (§6.13), so focus shows the card's ring; the
  tag's state is conveyed by the button's `aria-pressed`. Disabled:
  specimens the survey marks unpinnable (the hero's subject — it is
  the lens's, not the visitor's) carry no anchor and no button
  affordance.
- **Content merge.** The tag lands *on the specimen card*, lettered
  with that specimen's real name from the survey object; the
  collection count in the notebook (§6.15) and the footer record
  (§6.16) count these same pins. The visitor's record and the page's
  record are one record.
- **Failure fallback.** No JS: no tags, and cards carry their full
  printed labels (§6.13) — pinning is an addition to a complete
  label, never a replacement for one. sessionStorage unavailable
  (private mode): pins last for the page view only, and the notebook
  says so in its own voice ("This notebook is kept for this visit
  only", §12) — the limitation is declared, not silently suffered.
- **Reduced-motion variant.** The tag appears at its anchor without
  the fall (opacity 0→1 over 120ms); the landing glint is cut. The
  record-keeping is identical.
- **Performance budget & mobile variant.** One small element per
  pinned specimen, transform/opacity only. Mobile (<768px): the fall
  is 6px over 200ms (smaller screen, smaller drop); tags letter at
  12px apparatus minimum — a tag that cannot be read at arm's length
  is not shrunk further; instead it wraps to two lines.
- **Choreography timeline (v2).** Click → t=0 tag created at
  anchor +10px, opacity 0 → t=0–60 opacity to 1 → t=0–260 fall
  `--ease-drop` → t=260 landing: glint flash 120ms, shadow settles →
  t=380 the notebook count (§6.15) ticks +1 → rest. Unpin reverses
  in 200ms with the count ticking at its end.
- **State matrix (v2).** *Rest (pinned):* tag settled, shadow held.
  *Hover (tag):* +1px lift, lettering to lichen-pale. *Focus (card
  button):* ring on the card; tag state in `aria-pressed`.
  *Active:* the fall begins on pointer-up (a cancelled press —
  pointer dragged off — pins nothing). *Scrolled-past:* tags persist
  in place. *Disabled:* unpinnable specimens, above. *Touch:* tap =
  click; the fall is identical.
- **Breakpoints (v2).** ≥1200px: fall 10px, tag at full size.
  768–1199px: fall 8px. <768px: the mobile variant above.
- **Edge cases & failure modes (v2).** *Every specimen pinned:* the
  notebook (§6.15) notes the completed survey in its voice ("Every
  specimen on this floor carries your label") — a state the copy
  must have ready, because keen visitors reach it. *A specimen is
  withdrawn by the CMS mid-session:* its stored pin is dropped on
  load and the count corrects silently — the record describes the
  floor as it is. *Tag text long (a long binomial):* the tag grows
  to fit, max 180px wide, then wraps; it never truncates a Latin
  name — taxonomy is not abbreviated by a layout.
- **Accessibility spec (v2).** Pinning is a `<button>` per card with
  `aria-pressed` and a name that states the act and the state:
  "Pin your label on Dog lichen" / "Remove your label from Dog
  lichen". The tag itself is `aria-hidden` (its text duplicates the
  card's printed label + state). A live region announces pins
  politely ("Label pinned on Dog lichen — 4 pinned") at most once
  per 800ms. Tag contrast: lichen on litter-deep 5.11:1 (AA).
- **Tokens consumed (v2).** `--litter-deep`, `--lichen`,
  `--lichen-pale`, `--humus`, `--ease-drop`, `--ease-glint`,
  `--dur-pin` (260ms), `--pin-fall` (10px).

### 6.10 The footer beetle

- **What & why.** A tiny beetle — drawn at 22px, the theme's scale
  kept even here — crosses the footer once per visit on the same
  unhurried path, taking ~20 seconds, ignoring the user completely.
  It belongs because the footer's resident crossing the colophon
  like it owns the place is the theme's signature of life continuing
  beneath the content: the examination ends, the floor does not.
  It is the original entry's anti-slop detail, kept verbatim in
  spirit: same path, every visit, unhurried.
- **Structure.** An inline SVG beetle (elytra with the centre suture,
  six legs, two antennae) on a fixed authored path across the footer
  band (§6.16): entering from the left litter edge, crossing behind
  the colophon's first line, pausing once at the survey's mark,
  exiting right. The path is a CSS `offset-path` on the beetle
  element; legs animate by a 2-frame steps() alternation while it
  walks. The beetle is a sibling above the footer's ground layer and
  below no text: its path is authored to cross the band's empty
  lane (§6.16 reserves it), never over lettering.
- **Motion spec.** Trigger: the footer enters the viewport, once per
  session (sessionStorage flag). Duration ~20s across the band at
  desktop width, `--ease-creep` (near-linear, soft ends). One pause:
  at 55% of the path, 1200ms still, antennae sway ±4° — then it
  continues. It does not react to hover, click, scroll speed or
  anything else. If the footer leaves the viewport mid-crossing, it
  keeps walking (its life is not scrubbed to yours); if the tab
  hides, it pauses with the document and resumes — a beetle waits
  out the rain under the same leaf.
- **States.** Absent (before first footer entry / after crossing) →
  crossing → paused (once, 1200ms) → crossing → gone. There is no
  rest state on the page after it has gone; the lane stands empty,
  which is also correct.
- **Content merge.** The beetle crosses the *colophon* — the page's
  own record of itself — on a lane the footer reserves for it in the
  layout (§6.16). It is not pasted over the footer; the footer was
  built with a road through it.
- **Failure fallback.** No JS: no beetle (its trigger is JS; the
  shipped DOM has the empty lane). `offset-path` unsupported: the
  beetle does not appear — a fallback walk (transform keyframes) was
  considered and refused: a resident that can only appear by its
  proper road does not teleport along a substitute.
- **Reduced-motion variant.** No beetle. The lane stands empty. (A
  still beetle printed in the lane was considered and refused: a
  motionless beetle is a dead beetle, and the theme does not print
  that.)
- **Performance budget & mobile variant.** One small SVG on a
  composited offset-path, one steps() leg cycle — negligible.
  Mobile (<768px): the crossing shortens with the band (same speed,
  ~9s); the pause is kept. On very narrow screens (<380px) the lane
  is 14px tall and the beetle 16px — it still fits its road, or the
  build cuts it and §6.16's lane closes up.
- **Choreography timeline (v2).** Footer top crosses 90% of viewport
  → t=800 beetle enters left → t≈10.8s reaches the survey mark,
  pauses 1200ms → resumes → t≈20s exits right → flag set; the lane
  is empty for the rest of the session.
- **State matrix (v2).** *Rest:* absent or crossing as above.
  *Hover:* none — it ignores the pointer; a pointer over it passes
  through (`pointer-events: none`). *Focus:* not focusable.
  *Active:* n/a. *Scrolled-past:* if the visitor scrolls past the
  footer and back within the crossing, the beetle is wherever its
  20s has taken it — its clock is real time, not scroll.
  *Disabled:* pages whose footer is a bare legal line (no litter
  band) have no lane and no beetle. *Touch:* identical; it ignores
  touches too.
- **Breakpoints (v2).** ≥1200px: 22px beetle, 20s crossing.
  768–1199px: 20px, ~15s. <768px: the mobile variant above.
- **Edge cases & failure modes (v2).** *Footer already in view at
  load (short page):* the crossing triggers at t=1500 after load —
  a short page still gets its resident. *Visitor reloads
  mid-crossing:* the session flag is set only on completion or on
  entry +5s, whichever first — a reloaded visit may meet the beetle
  again; a completed crossing never repeats in the session.
  *Footer re-rendered by a framework:* the beetle element lives
  outside the re-rendered subtree by build rule (§6.16).
- **Accessibility spec (v2).** `aria-hidden`, no role, no text. It
  conveys nothing and interrupts nothing; screen-reader users lose
  no information, which is precisely the terms on which a purely
  delightful element is licensed in this theme.
- **Tokens consumed (v2).** `--litter`, `--litter-deep`,
  `--undergrowth`, `--ease-creep`, `--dur-beetle` (20000ms),
  `--beetle-size` (22px).

### Page-family elements

### 6.11 The first subject — hero composition

- **What & why.** The hero is the lens's first field of view: one
  subject (a single specimen plate at ×20), the headline above it as
  the thing the focus pull finds (§6.1), and the headline's letters
  swelling slightly in sequence, each magnified in turn — the title
  itself examined letter by letter. It belongs because the hero must
  teach the whole theme in one screen: a lens, a subject, a scale,
  and type that submits to the same magnification as everything
  else.
- **Structure.** A `.field-of-view` section (§6.1's frame): the
  headline (`<h1>`, each word wrapped, each letter a `<span>` —
  server-rendered, never JS-split, so no-JS and AT get whole words),
  the subject plate (one specimen frame, §6.13's grammar, at its
  stated ×20), the apparatus line beneath (magnification, patch
  count, census figure — §6.14's figures, generated), and one action
  (the notebook's door, §6.15) lettered as a label, not a banner.
  The spore drift (§5) falls through this patch only, over the
  plate, never over the headline.
- **Motion spec.** Sequence: the focus pull (§6.1) runs on load; as
  its sharp centre passes the headline (t≈900), the letters swell —
  each letter scales 1.0→1.14 and returns over 380ms `--ease-creep`,
  staggered 55ms in reading order, transform-origin at each letter's
  baseline centre so the word grows like a line of seedlings rather
  than bouncing. A word longer than 12 letters swells in two waves
  (the lens cannot take it in one pass — honest optics). The swell
  runs once per session, with the pull.
- **States.** Arriving (pull + swell) → resting (the field of view,
  lens available on the plate §6.6) → scrolled-past (the plate joins
  the ground tracking at the litter rate §6.4). Hover: the plate
  takes the lens; the headline takes nothing — the title is read,
  not examined, after its swell.
- **Content merge.** The hero's subject is a real specimen from the
  survey (the same object that appears as a card in its patch,
  §6.13 — cross-referenced, not duplicated: the card links back to
  "first seen in the field of view"). The apparatus line's figures
  are the page's real figures (§6.14). Nothing in the hero is a
  mood image.
- **Failure fallback.** No JS: sharp plate, unswollen headline,
  figures printed. Watchdog: §6.1's 1500ms blur deadline governs;
  the swell is CSS-animation-driven from a JS-armed class and a
  letter can never strand mid-swell (the animation's end state is
  scale 1.0 — the printed state).
- **Reduced-motion variant.** No pull, no swell, no drift: the field
  of view stands focused with its subject and figures. The hero
  loses its arrival, nothing else.
- **Performance budget & mobile variant.** The plate ≤180KB
  (§6.1's budget is shared with this element — one image, two
  specs). Letter spans: transform-only, ≤60 letters; a headline
  longer than 60 letters is rewritten, not accommodated (a title
  that long cannot be a first subject). Mobile (<768px): the swell
  stagger tightens to 40ms, peak scale 1.10; the plate crops to its
  centre 70% (§6.1).
- **Choreography timeline (v2).** t=0 pull begins → t≈900 swell
  starts at the first letter → t≈900+55n each subsequent letter →
  last letter settles by ≈t=2400 worst case (60 letters) → the
  apparatus line fades in at the pull's end (t=1800) → rest.
- **State matrix (v2).** *Rest:* focused field of view. *Hover:*
  lens on the plate only. *Focus:* first focus inside the hero
  completes pull and swell instantly (§6.1's rule). *Active:* the
  action label presses per §6.15's grammar. *Scrolled-past:*
  tracking at litter rate. *Disabled:* a hero with no plate runs
  the headline on undergrowth with the swell only — the field of
  view without a subject is a title page, a licensed variant the
  survey declares. *Touch:* no hover; pull and swell as on desktop.
- **Breakpoints (v2).** ≥1200px: plate right, headline left, the
  lens's classic composition. 768–1199px: stacked, plate below the
  headline at 70% width. <768px: stacked full-width, apparatus line
  wraps to two lines.
- **Edge cases & failure modes (v2).** *Headline in a long word
  language (German compounds):* the two-wave rule applies per word;
  letters never split across lines mid-swell (the swell is disabled
  on any word that wraps — a broken word cannot swell honestly).
  *Plate fails:* §6.1's fallback (headline on undergrowth, figures
  still printed — the census does not depend on the hero's photo).
- **Accessibility spec (v2).** The `<h1>` is whole words to AT (the
  letter spans are `aria-hidden` duplicates inside an
  `aria-label`-carrying heading — the standard split-letter pattern,
  applied strictly). The plate's alt names the specimen and its
  magnification. Apparatus figures are text, read in order.
- **Tokens consumed (v2).** `--undergrowth`, `--lichen`,
  `--ease-creep`, `--ease-focus`, `--swell-peak` (1.14),
  `--swell-stagger` (55ms).


### 6.12 The vein-line index — navigation

- **What & why.** The site's navigation is a leaf laid horizontally:
  a midrib line from which each destination hangs as a lateral vein,
  the current page's vein lit in new fern and its specimen count
  lettered at its tip. It belongs because wayfinding on this floor
  follows the leaf's own anatomy — the same grammar as the margin
  leaf (§6.5) and the anatomy plate (§6.8), so the visitor learns
  one drawing and reads the whole site with it.
- **Structure.** A `<nav>` in the header: an SVG midrib (a single
  horizontal path) with one vein path per destination, each vein
  ending at its link. Links are real anchors in a list, in DOM
  order; the SVG is positioned behind them, `aria-hidden`. The
  header also carries the progress `<output>` (§6.5's percentage)
  at its right — the instrument panel's second gauge. On mobile the
  leaf folds: the nav becomes a vertical list and the midrib a
  vertical line on its left, veins horizontal — the same leaf,
  turned.
- **Motion spec.** On load, the midrib draws over 600ms
  `--ease-unfurl` and the veins follow in order, 120ms each,
  staggered 60ms — the leaf grows once, at the top of the first
  page, and is drawn instantly on every subsequent page (a leaf
  does not regrow per page; sessionStorage carries the grown state).
  The current vein lights over 300ms `--ease-glint` when the page
  settles. Hover on a link: its vein thickens 1px→2px and lights
  `--fern-pale` over 160ms; the link's lettering follows.
- **States.** Rest (current vein lit) → hover/focus (vein thickens,
  letters brighten) → active (navigation runs the refocus transition
  §6.17). The current page's link carries `aria-current="page"` and
  its vein stays lit in `--new-fern` at rest.
- **Content merge.** The veins end at real destinations and carry
  their real specimen counts (generated, §6.14): the navigation is
  the survey's table of contents, drawn as the organism the survey
  studies.
- **Failure fallback.** No JS: the leaf stands fully drawn, links
  plain. SVG failure: the list stands alone with §11's ruled-link
  treatment — navigation never depends on its drawing.
- **Reduced-motion variant.** The leaf is drawn at first paint on
  every page; vein lighting is instant.
- **Performance budget & mobile variant.** One small SVG, ≤8 veins
  (a site with more destinations groups them — the leaf has the
  veins it has; overflow becomes a "More patches" vein to an index
  page). Mobile (<768px): the turned leaf as above, draw 400ms,
  veins 80ms.
- **Choreography timeline (v2).** First page, t=200 (after the
  focus pull has begun) → midrib 600ms → veins stagger from t=500 →
  all grown by t≈1400 → current vein lights at settle. Later pages:
  drawn at paint, current vein lit at t=150.
- **State matrix (v2).** *Rest:* grown leaf, current vein lit.
  *Hover:* vein + lettering brighten. *Focus:* identical to hover,
  plus §11's focus ring on the link. *Active:* refocus transition
  (§6.17). *Scrolled-past:* the header is not sticky on ≥1200px (the
  margin leaf is the persistent instrument); at <1200px the header
  sticks and the index miniaturises to current patch + percentage.
  *Disabled:* a destination with no specimens yet shows its vein
  ungrown (a bare stem) with "not yet surveyed" in its title — the
  leaf admits what the survey hasn't reached. *Touch:* tap = the
  link; veins light on the destination page, not on touch-down.
- **Breakpoints (v2).** ≥1200px: horizontal leaf, counts at vein
  tips. 768–1199px: horizontal leaf, counts cut (veins end at the
  links). <768px: the turned leaf, vertical.
- **Edge cases & failure modes (v2).** *Long destination names:*
  veins lengthen to fit; the midrib is elastic, authored in % so
  the leaf scales without re-drawing. *A destination removed:* its
  vein is removed with it — the leaf is generated from the same
  survey object as everything else (§6.16), so it cannot promise a
  patch the site doesn't have.
- **Accessibility spec (v2).** A real list of links with real names
  ("The moss cushion — 34 specimens"); counts are part of the link
  name where shown. The SVG is `aria-hidden`. Focus order is list
  order. The header `<output>` (progress) is present at all
  breakpoints (§6.5).
- **Tokens consumed (v2).** `--new-fern`, `--fern-pale`, `--lichen`,
  `--ease-unfurl`, `--ease-glint`, `--dur-nav-draw` (600ms).

### 6.13 Specimen cards

- **What & why.** The listing unit: a specimen in its depth-of-field
  frame — centre sharp, edges soft — with its name, binomial,
  stated magnification, scale bar and one line of finding (where it
  was found, what it proves). Cards are placed under the lens one by
  one as their patch is examined. They belong because the card *is*
  the theme's unit of content: everything the site lists — species,
  products, records — is a specimen, examined at a stated scale, or
  it is not listed at all.
- **Structure.** An `<article class="specimen">`: the frame (image
  layer with the radial focus falloff of §4 — sharp centre 62%,
  2px-blurred outer band on the image only), the rim apparatus
  (magnification at the top-left, scale bar at the bottom, drawn
  from the same factor), the name block (common name in Fraunces,
  binomial in Karla italic, §3), one finding line, and the pin
  button (§6.9). The frame's stated magnification is an attribute of
  the survey object; the scale bar's pixel length is *computed* from
  it at build time — the two can disagree only if the build is
  broken, which §10 tests.
- **Motion spec.** Placement: as a card's top crosses 78% of the
  viewport, it is set down — translateY 14px→0 and its frame's focus
  falloff settles (blur band 4px→2px) over 520ms `--ease-drop`,
  staggered 90ms across a row (cards are placed one by one, as under
  a lens being moved along a tray). The placement runs once per
  card per session. Cards jumped past are placed instantly
  (catch-up, §13). Hover: the frame's sharp centre widens 62%→74%
  over 300ms `--ease-focus` (the examiner leaning in — the static
  cousin of the lens §6.6, which also operates on the card's image).
- **States.** Unplaced (JS-armed only) → placing → placed (rest) →
  hover/focus (centre widened, pin button lit) → pinned (§6.9's tag
  present). Scrolled-past: placed, still. A specimen withdrawn from
  the survey shows its card in the "superseded" treatment (§11):
  frame at rest focus, a litter rule across its name, and the
  finding line replaced by the record's note — never greyed into
  illegibility.
- **Content merge.** The card's frame holds the specimen's real
  image at its real stated scale; the finding line is the content's
  own claim, sourced per §6.14. Remove the placement and the tray
  stands full: the examination loses its ceremony, the specimens
  remain.
- **Failure fallback.** No JS: cards stand placed, frames at rest
  focus. Watchdog: any card not placed by 1200ms after its trigger
  is forced to rest. Image failure: the frame shows the specimen's
  drawn plate (every specimen has an authored SVG fallback — a
  field guide can always draw what it cannot photograph) with the
  magnification unchanged (a drawing at ×20 is still ×20).
- **Reduced-motion variant.** Cards stand placed; hover widening is
  instant; the pin (§6.9) uses its own reduced variant.
- **Performance budget & mobile variant.** Images ≤90KB per card,
  lazy-loaded below the second row; ≤12 cards' frames hold the
  falloff filter at once (the filter is a static mask, not a live
  blur — it costs paint, not per-frame work). Mobile (<768px): one
  column, placement stagger 0 (cards place as they arrive, singly),
  frame falloff band narrows (the small frame is mostly centre).
- **Choreography timeline (v2).** Card top crosses 78% → t=0
  placement begins (row stagger +90ms per card) → t=0–520 settle
  `--ease-drop`, focus band 4px→2px → t=520 placed; its dew drops
  join §6.7's visible set → hover at any later time widens the
  centre over 300ms.
- **State matrix (v2).** *Rest:* placed, centre 62%. *Hover:*
  centre 74%, pin button lit. *Focus:* identical to hover; ring per
  §11; the lens (§6.6) engages centred on the frame. *Active (pin
  press):* §6.9's fall begins on release. *Scrolled-past:* placed.
  *Disabled:* superseded treatment above; a specimen with no image
  and no plate is not listed (the survey does not list what it
  cannot show). *Touch:* no hover widening; the first tap focuses
  (widens + lens static variant), the second follows the card's link
  if it has one — the two-tap rule is stated in the build notes, and
  the pin button is always directly tappable.
- **Breakpoints (v2).** ≥1200px: 3 per row in early patches, 2 in
  late (density law §4). 768–1199px: 2 per row. <768px: 1 per row,
  frame aspect holds (the specimen is never cropped to fit a row —
  the row fits the specimen).
- **Edge cases & failure modes (v2).** *Finding line longer than
  two lines:* it truncates with the full text on the detail page —
  the card is a label, not the record (§6.16 carries the whole).
  *Mixed magnifications in one row:* allowed and encouraged (the
  tray holds ×5 beside ×40) — each rim states its own, and the
  scale bars differ accordingly; a row that forces one scale on all
  frames is falsifying three of them. *A card taller than the
  viewport (long plate):* placement triggers on its top and the
  falloff settles progressively — the watchdog covers the whole card
  at 1200ms regardless.
- **Accessibility spec (v2).** The card is an article with a real
  heading (the specimen name); the image's alt names the specimen
  and magnification ("Springtail, *Orchesella cincta*, at twenty
  times life size"). The scale bar is `aria-hidden` (its value is
  in the apparatus text). Touch targets: pin button ≥44px. Contrast:
  name lichen on moss-deep 6.60:1; finding line lichen at 90% on
  moss-deep ≥5.9:1.
- **Tokens consumed (v2).** `--moss-deep`, `--lichen`, `--new-fern`,
  `--ease-drop`, `--ease-focus`, `--dur-place` (520ms),
  `--watchdog-place` (1200ms), `--frame-sharp` (62%).

### 6.14 Field figures — magnification & census counters

- **What & why.** The page's numbers, performed as a tally being
  written: the magnification figure counts up to the frame's true
  scale ("×20"), the census counts the floor's specimens ("143
  species"), and both figures are *generated from the survey object*
  — the count is the DOM's real specimen count, the magnification is
  the hero frame's real rendered ratio. It belongs because in a
  theme whose law is that the lens never invents (§1), the figures
  are the law's public proof: they count what is actually here, in
  front of the visitor, while it is counted.
- **Structure.** Apparatus lines (`.field-figure`) in the hero
  (§6.11) and repeated at the census patch: a label ("SPECIMENS ON
  THIS FLOOR"), the figure in Karla tabular, and the source line in
  caption ("counted from this page, today" / the publisher's survey
  credit). The figure element's final value is printed in the HTML;
  the count-up is a JS-armed performance over the printed truth.
  The magnification figure is not counted — it is *focused*: it
  resolves from ×1 to its value as the focus pull completes (§6.1),
  tying the number to the lens's own arrival.
- **Motion spec.** Census: when the figure's line crosses 70% of the
  viewport, it counts from max(0, final − 12%) to final in stepped
  40ms increments over 700ms `--ease-focus` — a tally, not a slot
  machine: steps are irregular by ±8ms (a hand counting, not a
  motor). It lands exactly and holds. Magnification: ×1→×20 across
  the focus pull's 1500ms, in whole steps, landing as the blur
  reaches 0. Figures never re-run within a session.
- **States.** Printed (rest, the shipped state) → counting →
  landed. Hover/focus: nothing — figures are read, not handled.
  Scrolled-past: landed.
- **Content merge.** The figures *are* content — the census is the
  survey's headline claim and the magnification is the frame's
  specification. The count-up is the claim being verified in front
  of the visitor; a figure that cannot be generated from the survey
  object is not printed at all (§10 gate 2).
- **Failure fallback.** No JS: figures stand printed at their final
  values. Loop killed mid-count: the watchdog (1000ms) sets the
  final value — a figure may never rest at a number that is not the
  true one, even for a moment longer than the watchdog allows.
- **Reduced-motion variant.** Figures stand printed. The tally is
  information; only its writing rests.
- **Performance budget & mobile variant.** Text writes only, ≤30
  steps per figure, ≤3 figures per page counting at once. Mobile:
  identical (figures are cheap); the source line wraps under the
  figure.
- **Choreography timeline (v2).** Hero: t=0 pull begins → × figure
  steps with the blur → t=1500 lands at ×20 as the plate sharpens.
  Census patch: line crosses 70% → t=0–700 tally steps → t=700
  landed, source line fades in → watchdog deadline t=1000 passes
  unneeded.
- **State matrix (v2).** *Rest:* printed final value. *Hover:* none.
  *Focus:* none (figures are not focusable; their line is reachable
  by reading). *Active:* n/a. *Scrolled-past:* landed value.
  *Disabled:* a page with one specimen prints "1 specimen" — the
  plural is generated too; grammar obeys the count. *Touch:*
  identical.
- **Breakpoints (v2).** All: identical behaviour; figure size steps
  down with the apparatus scale (§3) at <768px.
- **Edge cases & failure modes (v2).** *The count changes between
  pages (pagination):* each page's census counts *its own* floor —
  the label says "ON THIS FLOOR" and the figure is that page's DOM
  count; a site-wide total, if printed, is labelled as the survey's
  and sourced to the publisher's data (§1 allows both, labelled
  differently, never blended). *A figure of 0:* an empty patch
  prints "None found" in the record's voice (§12), not "0 species" —
  zero is a finding, phrased as one.
- **Accessibility spec (v2).** The final value is the DOM text from
  first paint (the count-up rewrites it, ending at the same value);
  the counting element is `aria-hidden` during the count with a
  visually-hidden static copy carrying the true figure, so AT never
  hears a half-count. Figure contrast: lichen on its ground per §2.
- **Tokens consumed (v2).** `--lichen`, `--fern-pale`,
  `--ease-focus`, `--dur-count` (700ms), `--watchdog-figure`
  (1000ms).


### 6.15 The field notebook — sighting form & conversion

- **What & why.** The page's conversion is a page in the visitor's
  field notebook: a form ruled like notebook paper, whose fields are
  labelled as an examiner's entries ("What you found", "Where — the
  patch or place", "Your name, as you sign the record"), and whose
  submit is the act of entering a sighting in the survey — joining
  the survey, booking the walk, ordering the field guide, whatever
  the site's one committed act is. It belongs in the litter-adjacent
  deep patch (§4's density law): the ask comes after the examination,
  at the point where the visitor has seen enough floor to want a
  record of their own. The form also carries the notebook's other
  duty: it reports the visitor's pins (§6.9) back to them as their
  collection ("Your labels: 4"), so the conversion grows out of what
  they have already done on the floor.
- **Structure.** A `<form class="field-notebook">` on a `--moss-deep`
  sheet: ruled lines every 33px (the body line unit) as a background
  on the sheet layer only; fields are inscription lines (label above
  in apparatus, 2px rule below in lichen at 30%, no boxes); a
  radio group for the sighting's kind, drawn as lateral veins off a
  short midrib (the §6.12 grammar at form scale); the collection
  line ("Your labels: N" — generated from §6.9's store) above the
  submit; the submit is a label tag (§6.9's leather) lettered with
  the act ("ENTER THE SIGHTING"). Errors appear as margin notes in
  Karla italic beside the field, in §12's error voice. Success
  replaces the form with the entered record: the visitor's own
  sighting, set as a specimen card (§6.13) with a fresh label tag.
- **Motion spec.** Field focus: the rule inks from 30% to full
  lichen over 240ms `--ease-focus` and a fern-pale hairline slides
  under it (the notebook underlining the line being written).
  Radio veins: choosing inks the chosen vein `--new-fern` over
  200ms. Submit: the tag presses (translateY 2px, `--ease-drop`
  120ms), holds while the request runs (max 1200ms before the
  failure note, §10 gate), and on success the form's sheet settles
  6px and the record card places itself (§6.13's placement, 520ms).
  The collection count ticks +1 only when a pin lands (§6.9's
  timeline), never on form events.
- **States.** Rest → focused field (rule inked) → error (rule in
  `--litter` lit, margin note present — litter is the error colour
  here because an error is a dead leaf in the notebook: visible,
  natural, to be turned over) → submitting (tag pressed, fields
  locked but legible) → entered (record card in place) / failed
  (note above the form, every field exactly as written — the
  notebook never loses an entry).
- **Content merge.** The form is the survey's own instrument: its
  fields ask for a sighting because the site *is* a survey; its
  success is a specimen card because that is what an entered
  sighting becomes on this floor. The collection line binds the
  visitor's pins into the ask. Remove the motion and the notebook is
  a ruled form that works — the conversion loses its paper, not its
  function.
- **Failure fallback.** No JS: a native form on a ruled sheet,
  submitting to the server, errors returned as printed margin notes.
  Failed submit (network): §10's form-keeping gate — nothing is
  cleared, the failure note reads in §12's voice ("NOT ENTERED —
  THE PAGE WOULD NOT TAKE INK. YOUR WORDS ARE KEPT ABOVE.").
- **Reduced-motion variant.** Focus rules ink instantly; the success
  card appears placed; the tag does not press. The notebook's
  grammar is unchanged.
- **Performance budget & mobile variant.** Ruled lines are a
  repeating-linear-gradient (no image). Mobile (<768px): the sheet
  goes full-width, ruled lines every 36px (touch writing is
  larger), radio veins stack vertically, the collection line moves
  below the submit (the ask first, the tally after — small screens
  reverse the emphasis honestly).
- **Choreography timeline (v2).** Focus field → rule inks 240ms →
  typing (no motion; the notebook does not perform while you write)
  → blur with error: note fades in 200ms as the rule lights litter →
  submit press 120ms → request (≤1200ms) → success: sheet settles,
  record card places 520ms, its tag falls (§6.9) at t=300 → the
  notebook's closing line inks in ("Entered. The survey thanks
  you — the floor keeps the record.").
- **State matrix (v2).** *Rest:* ruled sheet, collection line
  current. *Hover (field):* rule at 55% (a line inviting ink).
  *Focus:* rule full + hairline. *Active (submit):* tag pressed.
  *Scrolled-past:* the sheet holds its state; an entered record
  stays entered. *Disabled:* fields disabled by the survey (a closed
  survey's form) show their rules dashed and the closing line in
  place of the submit ("The survey is closed for this season") —
  the notebook admits a closed season. *Touch:* targets ≥44px;
  focus behaviour identical.
- **Breakpoints (v2).** ≥1200px: sheet at 640px in the deep patch,
  collection line above submit. 768–1199px: sheet 560px.
  <768px: the mobile variant above.
- **Edge cases & failure modes (v2).** *A visitor with no pins:*
  the collection line reads "Your labels: none yet — pin a specimen
  to begin your record", linking to the first patch (the ask grows
  from an honest zero). *Very long sighting text:* the textarea is
  a ruled sheet of 6 lines growing to 12; beyond that it scrolls —
  the notebook's page is finite and says so ("Six lines are kept
  here; the full account goes in your message"). *Double submit:*
  the tag disables on first press; the record is entered once.
- **Accessibility spec (v2).** Real `<label>`s (the apparatus labels
  are the labels, not placeholders); errors are linked by
  `aria-describedby` and announced by a polite live region on
  submit failure only. The radio veins are a real radio group with
  visible focus on the chosen vein + §11's ring. Contrast: labels
  lichen on moss-deep 6.60:1; margin notes lichen italic on
  moss-deep 6.60:1 (litter is the rule's colour, never the note's
  text colour — 2.60:1 would fail, so the error's *text* stays
  lichen and only the rule carries litter).
- **Tokens consumed (v2).** `--moss-deep`, `--lichen`, `--new-fern`,
  `--fern-pale`, `--litter`, `--litter-deep`, `--ease-focus`,
  `--ease-drop`, `--dur-ink` (240ms).

### 6.16 The litter footer — the site record

- **What & why.** The footer is the litter layer itself: a band of
  `--litter` over `--humus`, holding the colophon, the survey's
  credits, and the **field record** — the page's honest account of
  itself: how many specimens this floor carries, at what
  magnifications, surveyed when, and how many labels the visitor has
  pinned this visit. It belongs because a survey ends with its
  record, and the record lies in the litter where everything on the
  floor ends up. The beetle's lane (§6.10) runs through this band:
  the footer was built with a road in it.
- **Structure.** A `<footer class="litter">`: the litter band
  (litter at full strength for its top 40%, grading to litter-deep,
  then humus below — a drawn gradient of three authored stops, not a
  photo), the beetle lane (a 26px clear horizontal strip across the
  band at 62% height, kept empty by layout law), the colophon block
  (site name, the survey's credit line, the record's figures —
  generated from the survey object), the visitor line ("Your labels
  on this visit: N" — §6.9's store, or the honest zero), and the
  legal line in caption. The record's figures are the same generated
  values as §6.12's counts and §6.14's census — one survey object,
  three printings (§10 gate 3).
- **Motion spec.** The footer has almost none, by law (§4): on entry,
  the record's figures are already landed (they count in their own
  patches, §6.14 — the footer *reports*, it does not perform). The
  one motion is the beetle (§6.10), plus the litter band's top edge
  drawing its irregular leaf-line (an SVG path, 800ms `--ease-unfurl`)
  the first time the footer enters — the layer settling onto the
  page. Links hover per §11.
- **States.** Rest (record printed) → beetle crossing (once, §6.10)
  → rest. The visitor line updates live if a pin lands while the
  footer is on screen (the count ticks, §6.9's timeline) — the
  record is kept current even at the bottom of the page.
- **Content merge.** The footer's figures are the page's own census,
  its credits are the survey's, and its lane is a resident's road.
  Remove the leaf-line draw and the footer is a printed record in
  the litter — complete.
- **Failure fallback.** No JS: the record stands printed with the
  visitor line reading "Your labels are kept in the notebook
  (§6.15)" — no-JS cannot count session pins, so it points to where
  they live rather than printing a false zero (§1's law applied to
  the footer itself).
- **Reduced-motion variant.** The leaf-line stands drawn; no beetle.
  The record is identical.
- **Performance budget & mobile variant.** One gradient, one small
  SVG edge. Mobile (<768px): the band compresses (lane at 58%,
  20px), the record stacks above the colophon (the audit before the
  credits, on the small screen too).
- **Choreography timeline (v2).** Footer top crosses 85% → leaf-line
  draws 800ms → t=800+800 the beetle enters (§6.10's timeline takes
  over) → the record simply stands, as records do.
- **State matrix (v2).** *Rest:* printed record. *Hover (link):*
  §11's treatment (rule lights lichen-pale). *Focus:* ring per §11.
  *Active:* n/a. *Scrolled-past:* record stands. *Disabled:* a page
  with no survey (a bare legal page) has a humus footer with the
  legal line only — no litter band, no lane, no record: the theme
  does not dress a page that examined nothing. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: band 190px, lane 26px.
  768–1199px: band 170px. <768px: the mobile variant above; <380px
  the lane closes if §6.10's beetle is cut.
- **Edge cases & failure modes (v2).** *The record disagrees with a
  patch (a build bug):* §10 gate 3 exists for exactly this; the
  footer is generated, so disagreement means the generator was
  bypassed by hand — the fix is in the build, never in the footer.
  *Framework re-renders:* the beetle element lives outside the
  footer's re-rendered subtree (§6.10) by build rule.
- **Accessibility spec (v2).** Footer landmarks and heading order
  hold (the record's heading is a real `<h2>` "The field record").
  Figure contrast: dew on litter 5.09:1 for the record's figures
  (apparatus, ≥ AA at their size); legal line lichen-pale on humus
  14.11:1.
- **Tokens consumed (v2).** `--litter`, `--litter-deep`, `--humus`,
  `--dew`, `--lichen-pale`, `--ease-unfurl`, `--dur-edge` (800ms).

### 6.17 Out-of-focus skeleton + refocus transition

- **What & why.** The theme's loader and page transition, in the
  lens's own grammar: a page that is still loading shows its patches
  as an out-of-focus floor — shapes at the layout's real anatomy,
  blurred as a background layer only — and navigation between pages
  is a refocus: the old page's focus releases, the new page pulls
  sharp (§6.1's ceremony at travelling speed). It belongs because
  waiting, on this floor, is a lens not yet settled — never a
  spinner (the floor has no machinery) and never a blank.
- **Structure.** The skeleton is the page's own layout with content
  replaced by ground-tone blocks (moss at 30%, litter at 20%) inside
  the real patch frames, plus one line of apparatus: "THE LENS IS
  SETTLING". It exists only while the real content streams, and only
  under the JS-armed class; the server ships content, so the
  skeleton is a client-navigation artefact, not a first-load one.
  The transition wraps client-side navigation: on activation, the
  current page's image layers blur to 6px over 220ms, the new page
  is fetched and rendered beneath, then §6.1's pull runs compressed
  (blur 10px→0 over 700ms, mask 900ms).
- **Motion spec.** Skeleton: static (a blurred floor does not
  shimmer — shimmer is a machinery metaphor; the only motion is the
  apparatus line's ellipsis cycling 1.2s steps, cut under reduced
  motion). If content is not ready by 4000ms, the skeleton's line
  changes to the record's voice: "The floor is slow to clear today
  — what has arrived is below", and whatever has arrived renders
  beneath it (partial floors are honest floors). Transition total
  ≤1200ms; a third navigation within 5s degrades to an instant swap
  with a 150ms focus settle (the lens does not perform for a visitor
  in a hurry — the theme rations its ceremony by the visitor's own
  pace).
- **States.** Skeleton → resolving (patches swap in per patch as
  their content lands, each with §6.13's placement) → complete.
  Transition: focused → releasing (220ms) → travelling → pulling
  (700ms) → focused.
- **Content merge.** The skeleton *is* the page's anatomy (its patch
  frames at their real sizes), and the transition's pull is the
  hero's own ceremony reused as the site's travelling grammar — one
  lens, every journey.
- **Failure fallback.** No JS / full-page navigation: pages load
  server-rendered and sharp; there is no skeleton and no transition,
  and nothing is missed but the travelling. A failed fetch during
  transition: the old page refocuses (blur reverses over 300ms) and
  the failure is noted in the header in §12's voice — the visitor
  is never left looking at a blur.
- **Reduced-motion variant.** No skeleton blur (ground-tone blocks
  stand plain), no transition pull: navigation swaps instantly with
  the apparatus line's static text during loads.
- **Performance budget & mobile variant.** The skeleton reuses the
  page's own CSS (no extra asset). Transition blur is capped at 6px
  on image layers only. Mobile (<768px): the transition compresses
  further (pull 500ms) and the third-navigation rule tightens to the
  second navigation in 5s.
- **Choreography timeline (v2).** Navigation activated → t=0–220
  release blur → fetch (skeleton if >300ms) → new page rendered →
  t=0–700 pull (blur 10→0) with mask to t=900 → focused; total
  ceremony ≤1200ms excluding fetch. Watchdog: any blur in the
  transition is force-cleared at 1500ms (§5's blur law governs
  transitions too).
- **State matrix (v2).** *Rest:* focused page. *Hover:* n/a.
  *Focus:* focus is held on the activating link during release,
  then moved to the new page's `<h1>` at the pull's start (focus
  travels with the visitor, not after the ceremony). *Active:* the
  release begins on activation. *Scrolled-past:* n/a. *Disabled:*
  a build without client navigation has no transition — full loads
  only, §6.1's pull on the first. *Touch:* identical timings.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: pull
  600ms. <768px: the mobile variant above.
- **Edge cases & failure modes (v2).** *Back-button navigation:*
  the refocus runs in reverse grammar — the restored page pulls
  from 6px (a returning lens) over 500ms, and scroll position is
  restored *before* the pull so the visitor lands where they left.
  *Prefetched page:* the pull still runs (the ceremony is the
  arrival, not the wait) but at the compressed 500ms. *Skeleton
  shown for a patch that never resolves:* the 4000ms rule renders
  the patch's empty state (§6.18's grammar) in place.
- **Accessibility spec (v2).** During the skeleton, `aria-busy` on
  the main region; the apparatus line is the loading announcement
  (polite, once). Focus management as above; the blur never touches
  text (§5's law), so a screen-reader or low-vision visitor reads
  the new page's headline from the moment it renders, ceremony or
  not.
- **Tokens consumed (v2).** `--moss`, `--litter`, `--undergrowth`,
  `--ease-focus`, `--dur-release` (220ms), `--dur-pull-nav` (700ms),
  `--watchdog-blur` (1500ms).

### 6.18 The unexamined patch — 404 & empty states

- **What & why.** The page for a place the survey has not examined:
  a bare patch of floor — moss ground, one fern at its edge, nothing
  under the lens — headed "Nothing has been found here yet" and
  carrying the honest apparatus: the address that was sought, and
  three real ways back onto surveyed ground. It belongs because a
  survey's integrity is proven by how it treats the unexamined: it
  does not invent a specimen for the empty patch, and it does not
  dress the gap as a feature. Search-empty and filter-empty states
  use the same grammar at patch scale.
- **Structure.** A patch in the moss ground: the heading in Fraunces,
  the sought address in apparatus (the requested path, set as the
  notebook would record it), one line of record ("This patch is not
  in the survey. The nearest examined ground is below."), and three
  suggestion rows — the survey's most-examined patches, generated
  from the survey object (real destinations, real counts). The fern
  at the edge is the §6.2 crozier drawn open and still: the patch's
  only growth is at its margin, which is where growth on an
  unexamined patch would be.
- **Motion spec.** Almost none, by design: the patch stands printed.
  The suggestion rows place themselves (§6.13's placement, without
  stagger — three rows arrive as one tray). The margin snail (§6.5)
  does not appear on the 404 (there is no reading to measure); the
  header percentage reads the honest text "Not surveyed".
- **States.** Rest only. Hover/focus on the suggestion rows: §6.13's
  card grammar. There is no pinned, counting or glinting state on
  this page — an empty patch does not perform.
- **Content merge.** The suggestions are the survey's real patches;
  the sought address is the visitor's real request. The page's
  honesty is its content.
- **Failure fallback.** This *is* the fallback page; its own failure
  mode is being unstyled, which the build prevents by shipping its
  CSS with the shell (the 404 never depends on the page bundle).
- **Reduced-motion variant.** Identical (there is no motion to
  reduce beyond the rows' placement, which becomes instant).
- **Performance budget & mobile variant.** The lightest page on the
  site: no plates, no loop (the shared loop is not even started —
  nothing scrubs here). Mobile: identical, stacked.
- **Choreography timeline (v2).** Load → heading printed → rows
  place over 520ms → rest. That is the whole timeline, and its
  brevity is the point.
- **State matrix (v2).** *Rest:* printed patch. *Hover:* rows per
  §6.13. *Focus:* rows per §11's ring; the heading takes focus on
  load (`tabindex="-1"`) so AT lands on the finding, not the nav.
  *Active:* a row's activation runs §6.17's refocus. *Scrolled-past:*
  n/a (the page rarely scrolls). *Disabled:* a survey with fewer
  than three patches shows what it has — one row is a honest
  suggestion list. *Touch:* identical.
- **Breakpoints (v2).** All: one column, the patch at the measure
  (§3); ≥1200px the margin leaf is absent here too (no snail, no
  leaf — the margin agrees with the header: not surveyed).
- **Edge cases & failure modes (v2).** *A sought address that is
  almost a real one (a typo'd patch name):* the record line names
  the nearest patch by the survey's own string distance and the
  first suggestion row *is* that patch, lettered "Nearest examined
  ground" — help offered as a finding, not a scolding. *Search with
  zero results:* the same patch at section scale, its record line
  naming the query verbatim.
- **Accessibility spec (v2).** The heading is the page's `<h1>` and
  is focused on load; the sought address is text, not an image;
  suggestion rows are links with counts in their names (§6.12's
  grammar). Contrast: lichen on moss 4.64:1 at the heading's size
  and the record line at 17px minimum per §3's moss rule.
- **Tokens consumed (v2).** `--moss`, `--undergrowth`, `--lichen`,
  `--new-fern`, `--ease-drop`, `--dur-place` (520ms).


## 7. Page application map

**Home — the full examination.** Field of view (§6.11), then the
patches in examination order: the conspicuous (the moss cushion and
its specimens §6.13), the pinned fern (§6.3), the anatomy patch
(§6.8), the census patch (§6.14's figures in their own ground), the
notebook (§6.15) in the deep patch, and the litter (§6.16). The
census sits just before the notebook — the count is read just before
the visitor is asked to add their own entry to it.

**Listing — one patch, fully examined.** A listing page is one patch
at greater width: its specimens (§6.13) at that patch's density, its
own magnification range lettered at the head, and the vein-line
index (§6.12) offering the other patches. A listing that mixes
patches on one page has scattered the tray; cross-patch collections
are presented as a *tray drawing* (§6.13's grammar at index scale)
linking into each patch's listing, never as a blended grid.

**Detail — one specimen, in context.** The specimen at full size in
its patch, its record expanded into prose (§6.16's grammar), its
neighbours in the same patch at the foot ("Also on this patch"), and
its magnification stated before its name is celebrated. The detail
page's patch is the specimen's patch; a specimen is never promoted
to the hero for display — the hero's subject (§6.11) is chosen by
the survey, once, and the record says why.

**About — the surveyor's page.** The people and the method, set in
the deep patch: who examines, how the magnifications are measured,
the survey's dates. This is where the measurement declaration
(§6.16) lives in long form — the about page is the theme's
methodology, and it is deliberately deep: casual visitors don't
need it, committed ones crawl for it.

**Contact / conversion — the notebook only.** §6.15's form in its
patch, reached by the examination or directly (a direct arrival
lands the visitor at the notebook with the floor one click up —
examination is the home page's argument, not a toll gate on every
route).

**The unexamined patch (404).** §6.18, everywhere, unchanged.

## 8. Worked examples

### 8.1 The hero — the lens finds its subject

*The commission: a bryology society's site, "The Moss Atlas"; the
home page's examination runs field of view → the moss cushion
(specimens) → the pinned fern → the vein system → the census → the
notebook (join the survey) → the litter. Surveyed floor: 143
specimens across 6 patches.*

- **The composition (§6.11).** First screen: undergrowth ground.
  The headline "Small, and / everywhere" in Fraunces 600 lichen,
  and beside it the subject plate: a cushion of *Hypnum cupressiforme*
  at ×20, its rim lettered with the magnification and its scale bar
  drawn from the same factor. Beneath, the apparatus: "×20 · SIX
  PATCHES · 143 SPECIMENS ON THIS FLOOR" — 143 being the survey
  object's real count, generated, not typed.
- **The ceremony.** Fonts ready at t≈110ms: the focus pull begins
  (§6.1); at t≈900 the sharp centre crosses the headline and its
  letters swell in reading order (§6.11), the last settling by
  ≈t=1900 as the × figure lands on ×20 with the blur reaching 0 at
  t=1500. Spore drift falls through the plate's corner. A visitor
  who never scrolls has still received the whole contract: a lens, a
  subject, a scale, a count.
- **Scroll timeline.** 0–60px: nothing moves but the snail (§6.5)
  waking on the margin leaf. 60–400px: the field of view gives way
  to the moss cushion; its title unfurls (§6.2) as its top crosses
  72%. The visitor is examining.

### 8.2 Mid-page — the fern and its dew

*The same page, mid-examination: the pinned fern patch, where the
society's calendar of walks is presented as a frond's season — each
walk a pinna, each date a dew-lit fact.*

- **Entry.** The patch's title unfurls; the figure rises into its
  200vh pin (§6.3). As the visitor scrolls the pin, the dew
  highlights travel across their drops and the plate presses from
  1.0 to 1.04 — the lens leaning in along the frond while the
  season's walks are read beside the caption.
- **The specimens at scale.** Below the pin, three walk cards
  (§6.13) place themselves one by one: "The February floor — frost
  on the sporophytes", each with its date as its finding line and
  its own stated scale. The visitor's pointer crosses the first
  card: its sharp centre widens; they move across the plate and the
  lens (§6.6) engages, +6%, the rim's apparatus declaring the
  instrument. They pin a label on the walk they mean to join
  (§6.9) — the tag falls, the notebook's count ticks to 1.
- **What the visitor feels.** Slowness with resolution in it — the
  deeper patch moves less, reads finer (line-height 1.62 here), and
  its water answers the light. Nothing asked for attention; the
  lens and the pin answered it.

### 8.3 Conversion — an entry in the notebook

*The same page's deep patch: the notebook (§6.15), where the visitor
joins the survey.*

- **Arrival.** The census patch precedes it: the figures tally to
  their true values (§6.14) — 143 specimens, 6 patches, the
  society's 41st season (sourced to the society's records in the
  legend). The visitor arrives at the notebook having been shown
  the count they are about to join.
- **The entry.** The notebook's sheet shows their collection line
  first: "Your labels: 1" — the walk they pinned above, named. They
  choose the sighting kind on the radio veins ("Join a walk"), write
  their name and direction on the ruled lines. They mistype the
  email (no @): on blur the rule lights litter and the margin note
  reads, in Karla italic: "This direction will not carry — check
  the address before we enter it." (§12's error voice: a field fact,
  not a scolding.) They correct it; the note clears. They press
  ENTER THE SIGHTING: the tag presses into the sheet, and on success
  their entry places itself as a specimen card — their name, the
  walk, a fresh label tag already fallen onto it — lettered "ENTERED
  — SIGHTING № 144", the census's next number, generated.
- **Failure rehearsed.** If the post fails, nothing they wrote is
  cleared; the note above the form reads "NOT ENTERED — THE PAGE
  WOULD NOT TAKE INK. YOUR WORDS ARE KEPT ABOVE." and the tag
  un-presses. A visitor who examined 143 specimens to reach this
  form is never sent back to the surface by a network blink (§10,
  blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The green website.** Forest stock photos and leaf clip-art
   poured over ordinary web content. *Cure:* §1's law and §4 — the
   floor is an examination, specimens obey frame geometry, density
   falls with depth. If swapping two sections' images changes
   nothing, the build is wallpaper, not a floor.
2. **Decorative nature.** Fern corners, vine borders, a butterfly
   "for whimsy". *Cure:* the palette is flat colour and drawn line;
   the only drawn organisms are the snail (§6.5), the beetle
   (§6.10), the margin leaf (§6.12) and the anatomy plate (§6.8) —
   each an instrument or a resident with a job. A drawn thing with
   no job is cut.
3. **Invented magnifications.** A frame lettered ×20 over a render
   at ×6; a species count typed because it sounded abundant.
   *Cure:* the declared survey object, generated figures
   (§6.14/§6.16), and §10's three-printings check.
4. **Blur as a reveal habit.** Every section blurring in "like a
   lens" until the page is a migraine. *Cure:* §5's blur law — two
   licensed uses (§6.1, §6.17), text never blurred, 1500ms hard cap
   with a watchdog. A build that blurs a third thing has left the
   floor.
5. **The lens as a cursor.** A custom cursor shaped like a
   magnifying glass, trailing sparkles, the pointer hidden inside a
   ring. *Cure:* §6.6 — the lens is a zone in the page, the normal
   cursor stays visible at its centre, and the standing rules
   forbid the rest.
6. **Everything pinned.** Pinning every patch "for immersion" until
   the page is a series of traps. *Cure:* §5 — exactly two pins
   (§6.3, §6.8), both cut or converted on mobile.
7. **Cute animal overload.** The snail given a face and a name, the
   beetle waving, a mascot owl in the header. *Cure:* the residents
   are drawn naturalistically and ignore the user (§6.10). The
   theme's charm is that its creatures have their own business.
8. **Rounded, shadowed cards floating on the floor.** *Cure:* §4 —
   frames are rectangular plates at 2px corners, no drop shadows;
   depth here is focal, never cast.
9. **The snail as decoration.** A progress snail whose position
   doesn't match the reading (or a progress bar beside it "to be
   safe"). *Cure:* one survey mapping (§6.5/§6.16), the header
   output generated from the same value, §10 gate 3.
10. **Glint spam.** Dew flaring everywhere like a slot machine.
    *Cure:* §6.7's ration — one scheduler, ~2s interval, ≤2
    concurrent, visible set only. A floor that sparkles constantly
    is a disco, not a woodland.
11. **Marquee patches, kinetic headlines, fade-up reveals.** Any
    motion §5 refuses, smuggled back in. *Cure:* the refusal list
    is part of the gate (§10, item 10).
12. **Approximation theatre.** "Over 100+ species!" counted with
    exclamation, or exact figures with no source. *Cure:* §6.14 —
    figures are generated or sourced in the legend, and the voice
    (§12) bans the exclamation from the theme entirely.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **Lens-law audit.** Every frame's printed magnification equals
   its rendered scale ratio (checked by measuring the frame's
   specimen against its stated true size), and every scale bar is
   drawn from the same factor. A frame whose numbers lie fails.
2. **Figure-truth audit.** Every number the page asserts
   (magnifications, counts, millimetres, prices) traces to the
   survey object or a named publisher source in the legend. An
   untraceable figure fails.
3. **Three-printings agreement.** The index's counts (§6.12), the
   census figures (§6.14) and the footer record (§6.16) state
   identical specimen counts and patch counts — generated from one
   survey object and verified by reading all three.
4. **No stranded content.** With JS disabled, the whole page reads:
   plates sharp, titles grown, figures printed, form working. With
   JS on and the loop killed, every watchdog (§6.1's 1500ms, §6.2's
   1400ms, §6.8's 2600ms, §6.13's 1200ms, §6.14's 1000ms) fires and
   settles its element.
5. **Blur law.** Blur appears only in §6.1 and §6.17, only on image
   layers, never on text, and never past 1500ms from its trigger —
   verified with the loop throttled to 5fps, not just at full speed.
6. **Contrast audit.** Text pairings only from §2's law, verified in
   resting, hover-widened (§6.13) and lens-engaged (§6.6) states.
   New fern body text, moss text on undergrowth, dark text on
   litter: fail.
7. **Form-keeping.** A failed submit (simulated network error)
   leaves every field exactly as written, with §12's failure note.
   Any build that clears the notebook on error fails.
8. **Specimen legibility without instruments.** Every specimen is
   fully legible at its printed magnification with the lens (§6.6)
   never engaged. A build that hides content behind the lens fails.

**Standard (must pass, fixable in review):**

9. Density falls with depth (§4): hero holds one subject, the
   litter holds only record, credits, colophon.
10. Exactly two pins; placement (§6.13) and unfurl (§6.2) are the
    only reveal grammars; the refusal list (§5) is honoured — no
    marquee, no kinetic type beyond §6.11, no third blur.
11. Ambient ration: glint interval ≥1800ms and ≤2 concurrent; spore
    drift only in hero and anatomy patches; all ambient motion
    pauses off-screen and is absent under reduced motion.
12. The focus pull and letter swell run once per session and never
    re-run; the hero's apparatus figures match the generated counts.
13. Every interactive element is ≥44px, focus shows §6.6's lens
    engagement or §11's ring, and focus never leaves a specimen
    mid-placement (§6.13).
14. Mobile: both pins cut or converted per their specs, the snail
    and margin leaf cut, the lens in its static variant, card grids
    per §6.13's breakpoints.


## 11. Component inventory

Every component a real Forest Floor, Magnified site needs, with its
themed treatment. Components the theme refuses are listed with their
in-world replacement — a refusal without a replacement is a gap, not
a stance.

| Component | Themed treatment |
|---|---|
| Primary button | Label tag: litter-deep leather ground, lichen lettering, 2px lichen edge; presses 2px on `--ease-drop` (§6.15). On pale grounds (label tags §6.9), undergrowth lettering. |
| Secondary button | Ruled line button: transparent, 2px bottom rule in the ground's text colour; hover lights the rule fern-pale. |
| Text input | Inscription line (§6.15): apparatus label above, 2px rule below, no box. |
| Textarea | Ruled sheet: lines every 33px (the body line unit), Karla 17px. |
| Select | Refused. Choices are veins: a short list of radio lines off a midrib (§6.15's grammar generalised). |
| Checkbox | Vein box: unfilled square drawn as a vein junction; filled = new-fern fill + ground-colour tick. |
| Radio | Vein line: the chosen line's vein inks new fern; the dot is a small filled node at the junction. |
| Toggle / switch | Refused. A floor has states of examination, not switches; use two vein lines (Examined / Not yet) as radios. |
| Card | Specimen card (§6.13): framed, focused, labelled, pinnable. |
| Table | Field record (§6.16): real table, apparatus headers, no zebra striping — patch bands at most every 6 rows in the ground's 8% tint. |
| Tabs | Refused. Patches are crawled or indexed (§6.12), not tabbed. A build needing tabs has two patches arguing — separate them into sections. |
| Accordion | Drawer specimen: a card whose record expands downward like a tray drawer opening — the row below pushes down over 300ms `--ease-focus`; the heading gains a magnification tick. |
| Modal / dialog | The notebook (§6.15) is the theme's only dialog-shaped surface, and it is a page section, not an overlay. Confirmations are margin notes: an inline band in the current patch with the question and two label tags. |
| Toast | Refused. News from the floor is recorded, not toasted: transient confirmations appear as a one-line record entry at the patch's foot, in the record voice, and remain until the next examination. |
| Tooltip | Refused. Explanation lives in finding lines (§6.13); a specimen that needs a tooltip needs a better finding line. |
| Badge | Magnification chip: apparatus text on the frame's rim — "×20" — the badge states the scale, never a marketing claim ("NEW" is a canopy word and is banned, §12). |
| Alert | Failed-examination band: a seam in the current patch, litter rule, message in §12's error voice, persistent until resolved. |
| Pagination | Patch pagination: "Deeper in" / "Back to the surface" links lettered with the next patch's name and specimen count — never numbered pages; a floor is continuous. |
| Progress bar | Refused. Progress is the snail (§6.5) and its percentage. |
| Spinner | Refused. Waiting is an unsettled lens (§6.17). |
| Skeleton | §6.17's out-of-focus floor with its apparatus line. |
| Search | The survey search: a single inscription line in the header zone; results are returned as a tray of specimen cards grouped by patch, counts stated — search results in this theme are a tray, not a list. |
| Breadcrumbs | Replaced by the index's current vein (§6.12) plus the snail: the visitor's path is a position on the leaf, not a trail of pages. |
| Skip link | "Skip to the specimens" as a plain lichen link appearing on first focus at the surface. |
| Focus ring | 2px fern-pale outline, offset 3px, on every interactive element; on specimen cards, focus also engages the lens (§6.6). |
| Divider | A patch boundary (§4's soft focus edge) or, within a patch, a 2px rule in the ground's text colour at 30%. Wavy SVG dividers are refused — that is a different theme's water. |

## 12. Content & copywriting voice

Two voices, cast like the type. **The Guide** writes apparatus:
specimen names, magnifications, counts, labels — Karla, uppercase,
terse, every figure sourced. **The Record** writes prose: finding
lines, explanations, errors, confirmations — Karla sentence case
with Fraunces for the names, plain and unhurried, the voice of
someone writing up the day's examination for whoever kneels next.
The voices never swap: apparatus never sentences, the record never
shouts.

**Headline style.** Names of things and their scales. ✓ "The moss
cushion, at twenty times life size" / "143 specimens, six patches,
one square metre". ✗ "Discover our amazing tiny world!" (exclamation,
unsourced claim, canopy marketing in a headline's mouth).
Exclamation marks are banned from the whole theme — the floor does
not shout; it resolves.

**Label style.** Apparatus: name + measurement. ✓ "DOG LICHEN —
×20 — SCALE BAR 1 MM", "PATCH 3 OF 6 · 34 SPECIMENS". ✗ "Section 3",
"You are 57% through" in the visible UI (the percentage exists for
AT and the reduced-motion variant; the visible instrument is the
snail).

**Error voice.** A field fact, stated plainly, with the way back.
✓ "This direction will not carry — check the address before we enter
it." ✓ "NOT ENTERED — THE PAGE WOULD NOT TAKE INK. YOUR WORDS ARE
KEPT ABOVE." ✗ "Oops! Something went wrong 😞" (the floor has no
"oops", and no emoji survives magnification).

**Empty-state voice.** ✓ "Nothing has been found here yet." / "Your
labels: none yet — pin a specimen to begin your record." ✗ "No
results found. Try being less specific?" — the record does not blame
the examiner.

**Confirmation voice.** ✓ "ENTERED — SIGHTING № 144. The record of
this entry is kept in the litter." ✗ "Success! 🎉 You're all set!" —
a confirmation is a record entry, not a celebration.

**Banned words:** amazing, magical, hidden world (the floor is not
hidden; it is unexamined — the distinction is the theme), seamless,
dive in, unlock, supercharge, NEW (as a badge), oops.
**Owned words:** specimen, patch, examined, at ×20 (always with its
true figure), found, entered, the floor, the record, not yet surveyed.

**Fixed strings (verbatim, do not paraphrase):** the lens rim note —
"LENS +6%"; the notebook failure note — "NOT ENTERED — THE PAGE
WOULD NOT TAKE INK. YOUR WORDS ARE KEPT ABOVE."; the 404 heading —
"Nothing has been found here yet."; the skeleton line — "THE LENS IS
SETTLING".

## 13. Full-page scroll choreography map

The home examination, top to bottom. Every beat in order; instruments
run continuously beneath the beats (snail §6.5 scrubbing, ground
§6.4 drifting, glints §6.7 on their sparse timer).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Focus pull (§6.1); letters swell (§6.11); × figure lands | The lens arriving |
| 2 | 0–60px | Snail wakes on the margin leaf; header output live | The instrument is live |
| 3 | Moss cushion top crosses 72% | Title unfurls (§6.2) | The first frond opens |
| 4 | Cushion in view | Specimens place one by one (§6.13); dew joins the glint set (§6.7) | A tray being filled |
| 5 | Fern pin engages | Dew speculars begin travelling (§6.3) | Leaning along the frond |
| 6 | Pin q 0.5 | Highlights at full travel; plate at 1.02 | The light at midday |
| 7 | Pin releases | Caption read; walk cards place (§6.13) | The season, at scale |
| 8 | Anatomy pin engages | Midrib draws (§6.8) | The leaf begins to grow |
| 9 | Anatomy q 0.2–0.6 | Laterals, then the web; captions ink in order | Structure, in growth order |
| 10 | Census line crosses 70% | Figures tally to their true values (§6.14) | The count, verified aloud |
| 11 | Notebook in view | Collection line reads the visitor's pins (§6.15) | Their own record, waiting |
| 12 | Litter top crosses 85% | Leaf-line draws (§6.16) | The layer settling |
| 13 | Footer in view | Beetle enters (§6.10); snail reaches the leaf's tip | Life, continuing |

**Reverse pass.** Scrolling up: unfurls stay grown, placements stay
placed, the vein leaf stays drawn (growth is not reversed), while
the scrubbed instruments — snail, speculars, ground drift — reverse
exactly. The only things that re-cover are nothing at all: this
floor does not un-examine. The snail's sheen un-draws honestly
(§6.5) because the trail is a measurement, not a growth.

**Jump-scroll catch-up.** Anchor jumps and flings: everything passed
is placed and grown instantly (§6.2/§6.13's rules), figures stand
landed, the snail snaps to the mapped position, pins hold their end
states with highlights at their correct positions. No ceremony is
owed to a teleport.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 780KB, of which images/plates ≤ 520KB |
| Fonts | Fraunces (2 weights + optical axis) + Karla (2 weights + italic) ≤ 130KB, `font-display: swap` |
| JS | ≤ 65KB gzipped (one loop, observers, pins, form, scheduler) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the focus pull's setup is sliced per layer |
| Reveal latency | Any specimen placed ≤ 1200ms after entering (watchdog law); any blur cleared ≤ 1500ms (blur law) |
| Active lens layers | 1 at a time; glint concurrency ≤ 2 page-wide |

**Cut order when the budget is exceeded** (cut in this order, record
each cut in the build notes):

1. Spore drift (§5) — gone entirely.
2. Dew glint cycle (§6.7) — drops rest at printed glint.
3. Ground tracking's fern layer (§6.4) — litter and moss keep their
   rates.
4. Letter swell (§6.11) — the pull remains; the title rests.
5. Refocus transition (§6.17) — navigation becomes instant with the
   header flash.
6. Lens high-resolution copy (§6.6) — the lens falls back to its
   transform-scaled variant for all visitors.

**Never cut:** the blur watchdog, the snail's header percentage, the
generated figures, the notebook's error-keeping, any reduced-motion
variant. A build that cuts the honesty to keep the ambience has
inverted the theme.

## 15. Build-order checklist

1. Survey first: fix the patches, their order, each specimen's
   frame, its true size and rendered magnification, and the census.
   Write the survey object; everything else is generated from it.
2. Build the static floor: all patches, all content, figures
   printed, plates sharp, form working — with no JS. This is the
   site; the rest is examination.
3. Set the palette tokens and pairing law (§2); audit contrast on
   every ground before any motion exists.
4. Set the type scale and the name-before-story law (§3).
5. Author the patch boundary treatments (§4) — one per patch,
   reused at all breakpoints; reserve the beetle's lane in the
   footer (§6.16) now, before the colophon is laid out.
6. Build the instruments from the survey object: vein-line index
   (§6.12), snail + header output (§6.5), census figures (§6.14),
   footer record (§6.16). Verify the three-printings agreement by
   reading all three.
7. Add the shared loop; wire the snail, ground tracking (§6.4) and
   the dew specular scrub (§6.3) with their clamps.
8. Add the focus pull (§6.1) with its 1500ms watchdog and the blur
   law; test with the loop killed and throttled to 5fps.
9. Calibrate the snail: each lateral vein must cross the snail's
   position exactly as its patch boundary crosses 50% viewport
   height.
10. Add the surface ceremony: hero composition (§6.11) with the
    session rules, unfurl titles (§6.2), specimen placement (§6.13).
11. Author the dew points on the pinned fern's real photograph
    (§6.3); verify every highlight sits on dew at q=0, 0.5 and 1.
12. Add the lens (§6.6) and the label pin (§6.9) with persistence
    and the withdrawn-specimen handling.
13. Build the deep patch: anatomy plate (§6.8), notebook (§6.15)
    with error-keeping rehearsed against a simulated network
    failure, footer (§6.16), and the beetle (§6.10) last among the
    residents — its lane was reserved at step 5.
14. Add figures' counting (§6.14), skeleton/transition (§6.17), the
    unexamined patch (§6.18), and last — only if the budget
    survives — the spore drift (§5).
15. Run §10 in full: lens-law audit, figure-truth audit,
    three-printings agreement, no-JS read, loop-killed read, blur
    law at 5fps, form-keeping, specimen legibility without the
    lens. Gate signed by someone who did not build the page.

