# 19. The Linotype Line — Expanded (v1 + v2)

The page is not laid out; it is *cast*. Every line of text on a Linotype
Line page is a slug — a physical bar of hot metal that slides out of the
machine glowing amber, shimmers as it cools, and settles to lead grey in
reading order. Pull-quotes are whole slugs lifted out of the text and set
at an angle in the margin tray. Progress is a galley tray filling with the
slugs the visitor has caused to be cast. This document is the complete
build specification. Where it disagrees with the short library entry, this
document is the build target.

---

## 1. Concept & world

**The story.** In 1886 Ottmar Mergenthaler's Linotype did to typesetting
what the press had done to the manuscript: it made composition mechanical
without making it thoughtless. An operator sat at a 90-key keyboard —
arranged by letter frequency, ETAOIN SHRDLU down the first two columns —
and each keystroke dropped a brass matrix from the magazine; when a line
was complete the machine cast it, in one piece, in molten type metal: *a
line o' type*. This theme rebuilds that act as a page grammar. The page
is the machine's output, still warm. Lines arrive the way slugs arrive —
from the machine side, in casting order, glowing — and cool as the
visitor reads past them, so the top of the page is always the oldest,
coolest metal and the reading edge is always the freshest cast. The
header carries the galley tray where finished sections accumulate as
physical slugs; the margin carries a tray where the page's own best lines
are lifted out and set at an angle; the footer is the machine itself —
its 90-key keyboard, its belt and pulleys — drawn at the foot of the page
it has just composed. Nothing on the page is *about* printing as
decoration. The page is printed matter caught in the act of becoming
printed matter.

**The mood.** Industrial, warm, exact. Foundry black and cooled lead do
the structural work; paper is the sheet the slugs are proofed on; amber
exists only as heat — it is never a brand colour, never an accent, never
a button. The emotional arc of a page is thermal: *cast hot → read warm →
filed cool*. A visitor should feel that the page was made, line by line,
by a machine with a memory — including its one famous mistake, the
operator's error row, kept and corrected in the margin (§6.5).

**Best-fit sites and audiences.**
- Writing tools and editors: a product that composes text for a living,
  whose pages can honestly be cast line by line as the reader arrives.
- Journalism history, media museums, and press-heritage publications —
  the theme is their subject, enacted rather than illustrated.
- Industrial-heritage brands: foundries, machine works, letterpress and
  type-revival studios, any brand whose founding story involves hot
  metal and a composing room.
- Long-form essay and documentation sites where the unit of thought is
  genuinely the line, and reading progress deserves a physical measure
  (§6.4's tray counts real lines, not percentages).
- Type and typography products: specimen pages where the slug *is* the
  product being shown.

**When NOT to use it.**
- For content that is not line-shaped. Dashboards, data grids, media
  galleries and app UI have no casting order; forcing slugs under a
  settings panel turns the theme into zebra striping (§9, slop mode 4).
  §6.17 gives tables an honest slug treatment, but a page that is *mostly*
  table belongs to another theme.
- For breaking-news or safety content where a 400ms cast delay per line
  could postpone comprehension: use the pre-cooled static variant
  (§6.2's reduced-motion layout) as the permanent layout.
- When the client cannot tolerate the etaoin shrdlu line (§6.5). It is
  not optional garnish; a Linotype page without its error row is a
  costume, and §10 gate 7 fails builds that omit it.
- For brands whose identity is cold, clinical, or weightless — heat is
  the theme's only accent and it cannot be switched off without
  switching off the theme.
- On pages shorter than three sections: the galley tray (§6.4) needs at
  least three slugs to read as accumulation rather than decoration.

**The one law.** *No heat without a cast.* Amber appears on a page only
where a line has just been cast, is being hovered warm (§6.9), or is
cooling — and every amber moment is attached to a specific, real line of
the page's own text. A builder who reaches for amber as a generic accent
has not built this theme; §10 gate 5 measures it.

---

## 2. Palette

Four anchor inks, taken from the library entry unchanged. Derived tokens
are labelled **derived** and exist only to do jobs the anchors cannot do
at accessible contrast; no fifth hue is introduced. Amber is rationed by
the one law (§1): at rest, on a fully cooled page, amber coverage is
≤2% of pixels — the newest slug's cooling tail, the tray's newest slug,
and focus rings. Everything else amber is an event, not a surface.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--paper` Paper | `#F0EAD9` | The proof sheet: light-section ground, slug faces on light sections | ~62% of surface | Ground for `--black` (14.63:1), `--amber-deep` (5.45:1), `--lead-ink` (5.54:1) |
| `--black` Foundry black | `#191919` | The machine: dark-section ground, slug notch ends, reversed-type ground, structural rules | ~20% | On `--paper` 14.63:1; carries `--paper` type (14.63:1), `--amber` (6.56:1), `--lead` (5.39:1) |
| `--lead` Cooled lead | `#8E8E93` | Cooled slug faces and edges, skeleton bars, secondary metal, the filed state of every line | ~14% | On `--black` 5.39:1 — apparatus and large text on metal only; on `--paper` 2.71:1 — **never text on paper** |
| `--amber` Hot metal amber | `#E08A2C` | Heat itself: fresh casts, cooling gradients, hover warmth, the shimmer's tint | ≤2% at rest | On `--black` 6.56:1 — display/apparatus on metal; on `--paper` 2.23:1 — **never text on paper, never a fill behind text on paper** |
| `--amber-hot` (**derived**) | `#F5A83D` | The first 200ms of a cast on metal sections: the glow peak before cooling hands over to `--amber` | event-only | On `--black` 8.83:1 |
| `--amber-deep` (**derived**) | `#8A4F0E` | The only amber permitted as marks/text on paper: the proofreader's strike (§6.5), small tray numerals, form error notes | as needed | On `--paper` 5.45:1; on `--paper-shade` 4.62:1 — apparatus ≥12px semibold |
| `--lead-ink` (**derived**) | `#5C5C60` | Small apparatus text on paper the reader must read: captions, tray labels, slug counts | as needed | On `--paper` 5.54:1; on `--paper-shade` 4.86:1 |
| `--lead-deep` (**derived**) | `#4A4A4E` | Essential small text in the lead family on paper: form help, table footnotes | as needed | On `--paper` 7.34:1 |
| `--metal` (**derived**) | `#232320` | Dark-section working ground, one step off the black: slug faces on metal sections, tray interiors | as needed | `--paper` on it 13.11:1; `--amber` 5.88:1; `--lead` 4.83:1 |
| `--paper-shade` (**derived**) | `#E4DCC4` | Slug faces and tray faces on paper sections; skeleton pulse base | as needed | `--black` on it 12.84:1; a shadow of the paper, not a new colour |
| `--hairline` (**derived**) | black at 16% | Slug bottom edges, tray rules, table hairlines | hairlines only | Never a text colour |

**Dark-mode behaviour — the night shift.** The theme does not invert.
A galley sheet is a physical sheet; in dark mode the *room* darkens and
the sheet stays a sheet. Concretely: everything outside the sheet — page
surround, header surround, footer ground beyond the machine drawing —
becomes `--black`; every token *on* the sheet (`--paper`, `--paper-shade`,
all text pairings) is mode-invariant, so every contrast figure above
holds in both modes. Metal sections are unchanged — the machine was
already black. The sheet gains one addition: a lamp tint, a radial
gradient of `rgba(224,138,44,.04)` centred at 50% 0% over the paper —
the foundry's amber work-lamp, felt rather than seen. Cooling colours do
not change at night; heat is heat at any hour.

**Heat rationing, stated as a build rule.** Amber may exist in exactly
five licensed places: a casting or cooling line (§6.1, §6.2), the
heat-shimmer (§6.6), hover warmth (§6.9), the clunk's cool-down flash
(§6.10), and focus rings (`--amber` on metal, `--amber-deep` on paper).
An amber logo, an amber sale badge, amber link text on paper — each is a
§10 gate failure, because amber that means "look at me" today cannot
mean "this line is still hot" tomorrow.

---

## 3. Typography

Two faces, both doing the jobs they did in the composing room. **Zilla
Slab** is the slug face: it sets everything the machine casts — body
lines, headlines, apparatus, data — because a slug's type is one face,
cast solid. **Fraunces** is the display face: the foundry's show type,
used for the page's title line and chapter openings, the way a poster
line was set in foundry type above machine-set body copy. No third face
is admitted; the proofreader's strike (§6.5) is drawn, not typed, so no
handwriting face is needed anywhere in the theme.

| Role | Face / weight | Size / line-height | Rules |
|---|---|---|---|
| Display 1 | Fraunces, opsz 144, 560 | clamp(44px, 5.6vw, 80px) / 0.98, tracking −0.01em | Once per page. Set as discrete slug lines (§6.1) — authored line by line, never auto-wrapped |
| Display 2 / chapter head | Fraunces, opsz 72, 560 | 38px / 42px | Opens a composing chapter; followed by a 2px `--black` rule and one slug of air |
| Slug headline (H3) | Zilla Slab 600 | 24px / 32px | A headline is a fat slug: cast as one line where possible; two-line headlines cast as two slugs, staggered (§6.2) |
| Lead line | Zilla Slab 400 | 21px / 32px | First paragraph of a section; its slugs carry the section's warmest cooling curve |
| Body slug line | Zilla Slab 400 | 18px / 28px | **The 28px is the slug unit (§4).** Body text is never set off the baseline grid |
| Body small | Zilla Slab 400 | 16px / 24px | Secondary reading text; 24px = 6/7 slug — used only inside cards and the tray, where the grid is local |
| Apparatus | Zilla Slab 600 | 12px / 16px, uppercase, tracking 0.14em | Tray labels, chapter marks, slug-end stamps; `--lead-ink` on paper, `--lead` on metal |
| Data / counters | Zilla Slab 500, tabular figures | 14px / 20px; hero counters 28px / 32px | All counts tabular, always: "lines set: 1,204" never jitters as it increments |
| Caption | Zilla Slab 400 | 14px / 20px | `--lead-ink` on paper (5.54:1), `--lead` on metal (5.39:1) |
| Reversed micro-type | Zilla Slab 600 | 9px / 10px, uppercase, tracking 0.08em | The slug notch's reversed sorts (§4). Decorative duplicate of the line's own first sorts; `aria-hidden`, never the only copy of any word |

**Per-role rules.**
- *Display* is authored, not flowed: any headline long enough to wrap is
  re-authored into cast lines at build time. A browser-chosen line break
  is a broken slug.
- *Body* lines are real text in real paragraphs. The slug treatment (§4)
  is a surface — bar face, notch rail, baseline grid — laid under
  ordinary selectable text. Text is never split into per-line spans in
  body copy; screen readers and find-in-page meet prose, not furniture.
- *Emphasis* inside a slug line is weight (600) or a warm slug (§6.9's
  hover is the pointer's version; authored emphasis is a slug set at
  `--dur-cool` × 3, visibly warmer for longer). Zilla Slab's italic is
  refused for emphasis — a slug has no italic; sloped metal is a casting
  fault.
- *Numbers* are always tabular and always true: every counter on the
  page counts DOM lines or sections (§6.4), never a marketing figure.
- *Reversed type* appears only in slug notches and the keyboard's key
  caps are never reversed — the keyboard is read, the slug is cast.

---

## 4. Layout language

**The slug unit.** `--slug: 28px` — the body line-height — is the page's
only vertical measure. Section padding is 4 slugs (112px) above and
3 slugs (84px) below; paragraph spacing is exactly 1 slug; chapter heads
sit on slug boundaries. A layout that drifts off the slug grid reads, in
this theme, as a page set by hand in a machine room: wrong. Horizontal
spacing runs on a 4px sub-grid, but nothing vertical is ever sized in
anything but slugs and half-slugs.

**The measure and the tray.** At ≥1200px the page is a three-track
composition: a 56px machine rail (the margin press furniture: chapter
marks, the etaoin gutter, hairline rules), a reading measure of 62ch
(≈648px at 18px Zilla), and a 300px margin tray, separated by 32px
gutters, centred in a 1184px maximum. The tray is not a sidebar: it is a
physical tray, face `--paper-shade`, ruled on its left by a 2px `--black`
rule, and it holds only slugs (§6.3) and the chapter's apparatus. Below
1200px the tray retires into the measure (§6.3 breakpoints); below 768px
the rail retires too and the page is a single column of slugs.

**Slug bar anatomy.** Every cast line sits on a bar with four parts:
1. **The notch** — a 26px segment at the line's left, face `--black`,
   carrying the line's first two or three sorts reversed in `--paper`
   micro-type (§3). The notch is the slug's casting end; it is how a
   reader knows a line is a slug and not a stripe.
2. **The face** — `--paper-shade` on paper sections, `--metal` on metal
   sections. When a line is hot, the face carries the cooling gradient
   (§5) as an overlay *behind* the type: the type itself never changes
   colour mid-cool, so no line ever passes through an unreadable state.
3. **The edge** — a 1px bottom edge, `--hairline` on paper, `--lead` at
   35% on metal: the seam where this slug meets the next.
4. **The air** — slugs in a paragraph touch edge-to-edge (the bar *is*
   the line-height); paragraphs are separated by one empty slug of air,
   a blank bar with no notch. Leading, in this theme, is literal.

**Header galley tray.** The fixed header (56px) carries, under the
nameplate row, a horizontal galley tray 34px tall: a ruled channel into
which one slug chip (46×18px, face `--lead`, notch in `--black`) is
deposited per completed section, beside the "lines set: n" counter
(§6.4). The tray is the page's table of contents told as output: a
visitor can count how much page exists by counting slugs.

**Chapters and the pin.** A page divides into composing chapters —
themed sections of 3–7 slugs' height or more. During the middle chapters
the 90-key keyboard ornament pins to the viewport foot (§6.11) while
lines cast above it; it releases at the footer proper, where the full
machine drawing lives (§6.7). At most one element pins at a time; the
tray slug lift (§6.3) is scrubbed, never pinned.

**Density rules.** No more than two metal sections consecutively — the
reader must return to paper. A section may not mix faces: a slug is
paper-faced or metal-faced for its whole section. Whitespace is spent as
leading (empty slugs inside the measure) before it is spent as margin:
the page breathes between its lines, not around them.

**Placed imperfections.** Three, licensed, no others: the etaoin shrdlu
error line, struck in the margin (§6.5); the tray slugs' −2° set angle
(§6.3) — always −2°, always the same direction, like a compositor's
habit; and one dropped slug per listing galley (§6.14), a card sitting
2px low, marked in the build notes. Random rotation, random offsets,
and decorative misalignment are slop (§9), not character.

---

## 5. Full motion system

All scroll-driven motion runs on **one shared requestAnimationFrame
loop** with lerp factor 0.12: the tray lift, the notch-rail parallax,
the counters, and the shimmer's position all read the same smoothed
scroll value. Nothing in the theme animates on raw scroll events.

**Named easings** (the machine's own curves):
- `--ease-cast: cubic-bezier(.22,.9,.26,1)` — out of the magazine
  channel fast, stopped dead by the mould. All slug entrances.
- `--ease-clunk: cubic-bezier(.3,1.35,.4,1)` — the lock: 4px of travel,
  a hair of overshoot, seated. Clicks and tray deposits.
- `--ease-cool: cubic-bezier(.45,.05,.55,.95)` — near-linear thermal
  fade; cooling must feel like physics, not choreography.
- `--ease-lift: cubic-bezier(.33,.75,.3,1)` — the tray lift's release
  when scrub hands over to settle.
- `--ease-shimmer: ease-in-out` — the heat loop's breathing.

**Duration tokens:** `--dur-cast: 400ms` · `--dur-cool: 1000ms` ·
`--dur-stagger: 90ms` (per line, casting order) · `--dur-clunk: 300ms` ·
`--dur-warm: 250ms` · `--dur-strike: 300ms` · `--dur-draw: 900ms`
(belt-and-pulley) · `--dur-slide: 500ms` (galley-slide transition) ·
`--dur-shimmer: 1800ms` (one shimmer breath).

**Every motion term, in this theme's language:**
- *Scroll-triggered reveals* → sequential line casting (§6.2): a
  section's lines cast in reading order as it enters.
- *Scroll-driven / scrubbed animation* → the tray slug lift (§6.3) and
  the keyboard pin (§6.11): bound to the smoothed scroll value, fully
  reversible — scrolling up sets the slug back down.
- *Parallax* → the notch rails drift at a 0.94 factor against the paper
  text: the metal layer moves slower than the sheet it is proofed on.
  Amplitude is capped at 6px per section so a notch never detaches from
  its line.
- *Pinned sections* → the keyboard chapters (§6.11). One pin per page,
  ever.
- *Progress indicator* → the galley tray + "lines set: n" (§6.4):
  progress as physical output, not a percentage.
- *Staggered reveals* → the casting stagger, 90ms per line (§6.2).
- *Masked reveals* → slugs enter from behind the mould mask: the bar's
  clip opens from the machine side as the slug slides (§6.1).
- *Blur-to-sharp* → **refused.** Hot metal is never out of focus; heat
  is a colour event, not an optical one. The theme's equivalent is
  glow-to-cool (§6.1).
- *Kinetic typography* → casting itself, and the counters (§6.4):
  type that arrives as manufacture.
- *Marquee* → **refused.** A cast line does not crawl; it is set, read,
  and filed. The only horizontal traveller on the page is the heat
  shimmer crossing the freshest slug (§6.6).
- *Animated counters* → "lines set: n" and "words cast: n" (§6.4),
  incremented per real line cast, tabular figures.
- *SVG line-draw* → the belt-and-pulley machine drawing (§6.7) and the
  proofreader's strike (§6.5).
- *Image scale-in-frame* → slug-frame images (§6.8): 1.06 → 1 inside
  the bar frame, cooling as they centre.
- *Hover physics* → warm-a-degree (§6.9) and tray-slug tilt (§6.3):
  heat and gravity, never springs for their own sake.
- *Magnetic hover* → **refused.** A slug seated in the chase does not
  chase the pointer; it warms where it sits (§6.9).
- *Custom cursor* → **refused** (standing rule). The system cursor is
  the operator's hand; the theme does not dress it.
- *Skeleton loading* → empty bars (§6.12).
- *Page transitions* → the galley-slide (§6.12): the old tray slides
  off, a fresh tray casts in.
- *Ambient loops* → exactly two: the heat shimmer over the freshest
  slug, and the oil sheen across metal sections (§6.6). Both pause
  off-screen and under `prefers-reduced-motion`.
- *Reduced motion* → the pre-cooled page (§6.1–§6.12 variants): every
  line filed in lead grey from first paint, all information identical.

---

## 6. Signature elements

Eighteen elements: the twelve signature elements of the library entry
(§6.1–§6.12) and six page-family elements (§6.13–§6.18). Every element
carries its full build spec and its v2 layers. Shared easings and
durations are defined once in §5; colour tokens in §2; the slug anatomy
in §4.

### 6.1 Cast-and-cool hero lines

- **What & why.** The hero is composed in front of the visitor: each
  headline line slides in as a glowing slug and cools from amber to lead
  over the following second, in casting order. It is the theme's thesis
  performed once, at the top, on the page's most important sentences:
  *this page is being made, line by line, and you are watching the
  machine that makes it.* If a visitor sees nothing else, they have seen
  the theme.
- **Structure.** The hero headline is authored as discrete slug lines —
  one `<span class="slug-line">` per cast line inside the `<h1>`, each
  line a full slug bar (§4 anatomy: notch, face, edge). Lines are block
  elements; the headline's line breaks are the author's, never the
  browser's (§3). Beneath the headline slugs, the standfirst casts as
  body slugs (§6.2) once the headline has cooled.
- **Motion spec.** Per line: `translateX(-28px) → 0` over `--dur-cast`
  (400ms) with `--ease-cast`, entering from behind the mould mask
  (clip-path inset from the left opening in the same 400ms). The face
  overlay starts at the cooling gradient's hot end — on paper sections,
  an amber wash peaking at 55% `--amber` over `--paper-shade`; on metal,
  `--amber-hot` at 80% over `--metal` — and cools along `--ease-cool`
  over `--dur-cool` (1000ms) to the resting face. Lines cast in order,
  staggered 120ms (hero lines are display slugs; the stagger is wider
  than body casting's 90ms so each line can be read as it lands).
  The type itself never changes colour: contrast of the resting text on
  the hottest overlay state is ≥7:1 at every frame (§2 figures are
  computed at the hot end, not the cool end).
- **Choreography timeline (v2).** t=0 page painted, hero lines parked
  behind the mask in final type → t=80ms line 1 begins cast → t=480ms
  line 1 seated, cooling from t=480 → t=200ms line 2 begins (120ms
  stagger) → … last line seated at t=80+120×(n−1)+400 → each line's cool
  completes 1000ms after its own seating → the standfirst's first body
  slug casts 150ms after the last headline line seats → hero fully cool
  at ≈ t=80+120×(n−1)+1400ms. For the reference 3-line hero: fully cool
  at ≈1.72s. Once per page load; never replayed.
- **State matrix (v2).** *Rest (pre-trigger):* lines in final position
  and final colour — this is also the no-JS state; JS parks them only
  after confirming it can run the sequence. *Hover:* §6.9 warmth applies
  to hero slugs as to any slug. *Focus:* headline is not focusable;
  links inside it take the standard focus (2px outline, `--amber-deep`
  on paper / `--amber` on metal, offset 2px). *Active:* n/a.
  *Scrolled-past:* cooled state, static; the hero does not re-cast on
  return. *Disabled:* JS off = rest state permanently. Touch: identical
  — casting is time-driven, not pointer-driven.
- **Content merge.** The slugs *are* the headline: real text, real line
  breaks, set in the page's display face. Remove the motion and the hero
  is a headline on bars — the composition remains, only the manufacture
  is hidden.
- **Failure fallback.** The 1.2s law (library standing rule): if the
  cast sequence has not completed 1.2s after its trigger — JS error,
  jank, background tab — a watchdog snaps every hero slug to the cooled
  end state. The watchdog, not `transitionend`, owns the decision.
- **Reduced-motion variant.** All hero lines pre-cooled in lead from
  first paint. No slide, no glow. The headline reads identically.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: Display 1 at
  44px floor, stagger tightens to 100ms. <768px: lines cast one at a
  time with no overlap (stagger = full 400ms cast), because overlapping
  motion on a small screen reads as a glitch, and the notch shrinks to
  18px carrying one sort.
- **Edge cases & failure modes (v2).** *Late fonts:* the cast clock
  starts at `document.fonts.ready` or first contentful paint + 300ms,
  whichever is later; a slug never casts in a fallback face. *Very long
  hero (5+ lines):* stagger compresses to 90ms so total cast time stays
  ≤2.2s. *Tab hidden mid-cast:* the sequence completes on return — the
  watchdog compares wall-clock, so a hidden tab lands on cooled slugs,
  not a frozen glow. *Scroll-away during cast:* casting continues
  off-screen; heat does not wait for an audience.
- **Accessibility spec (v2).** The `<h1>` is one continuous accessible
  name: slug-line spans are `display:block` inside the heading with no
  aria fragmentation; the notch's reversed sorts are `aria-hidden`
  duplicates. Cooling is a background overlay — no text or contrast
  state is announced or altered. Nothing in the hero moves focus.
  Motion is decorative over static semantics, so no live region is used.
- **Performance budget & mobile variant.** ≤6 hero slugs × (1 transform
  + 1 background overlay) = ≤0.4ms/frame in the shared loop; the cooling
  gradient is a pre-rendered linear-gradient whose opacity animates —
  no per-frame gradient repaint. Mobile variant: the sequential
  non-overlap cast above; gradient steps reduced from 5 to 3.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--metal`,
  `--black`, `--amber`, `--amber-hot`, `--ease-cast`, `--ease-cool`,
  `--dur-cast`, `--dur-cool`, `--slug`.

### 6.2 Sequential line casting on scroll

- **What & why.** The theme's heartbeat, repeated for every section:
  as a section enters, its lines cast in sequence — glow, shimmer,
  cool — staggered 90ms per line, so reading downward is watching the
  page being set. One ritual, identically repeated, is what makes a
  page feel composed rather than decorated.
- **Structure.** Sections are ordinary semantic blocks (`<section>`,
  `<p>`, lists, blockquotes). Body text is *not* split into per-line
  spans (§3): the slug surface is applied per block — the bar-face
  gradient locked to the 28px baseline grid (§4), the notch rail at the
  block's left — and the cast is performed on the block's surface:
  a cooling overlay whose reveal sweeps line by line down the block,
  timed to the block's rendered line count (measured once at layout:
  `blockHeight / 28`). Headline slugs inside the section (H3, pull
  lines) are discrete slug elements and cast as §6.1.
- **Motion spec.** Trigger: section's first line crosses 70% viewport
  height. The cooling overlay starts at the hot gradient (§6.1) and a
  "cast front" — the boundary between hot and cool — travels down the
  block at one line per 90ms: each line glows as the front passes, then
  cools over `--dur-cool` (1000ms) on `--ease-cool`. A line's shimmer
  (§6.6) settles one beat (180ms) after the front passes it. Sections
  entering together (fast scroll) cast in document order with the front
  shared: the page is one machine and casts one line at a time.
- **Choreography timeline (v2).** t=0 section crosses 70% → t=0 line 1
  glow begins → t=90ms line 2 → … line *k* at t=90×(k−1) → each line's
  cool completes at its glow +1000ms → section fully cool at
  t=90×(k−1)+1000ms. A 6-line paragraph: fully cool at ≈1.45s. When the
  section completes, its slug is deposited in the galley tray (§6.4) and
  the "lines set" counter lands on the new total.
- **State matrix (v2).** *Rest:* cooled end state — also the no-JS and
  print state. *Hover:* §6.9 per line (the hovered line warms within
  its block; the block's other lines stay cool). *Focus:* text is text;
  links take standard focus. *Active:* n/a. *Scrolled-past:* cooled,
  overlay removed from the DOM layer (the block returns to a plain
  surface — cooled slugs cost nothing). *Disabled:* JS off = rest
  permanently. Touch: identical; casting is scroll-driven, not
  hover-driven.
- **Content merge.** Casting happens *to the text being read, in
  reading order* — the animation's sequence and the content's sequence
  are the same sequence. There is no separate animated layer with its
  own content anywhere in the element.
- **Failure fallback.** Base CSS renders the cooled state; JS applies
  the hot overlay only to lines it is about to cast. Any failure — no
  JS, observer failure, reduced data — leaves fully readable, fully
  cooled text. The 1.2s law (§6.1) applies per section: an interrupted
  cast snaps cool.
- **Reduced-motion variant.** Sections arrive pre-cooled. This variant
  is also the mandated permanent layout for safety-critical content
  (§1).
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: stagger 75ms
  (narrower measure, fewer lines per block, same total time).
  <768px: the cast front still travels line by line, but blocks taller
  than 12 lines cast in two fronts (top 6, then next 6) so a long
  article section never takes >2.1s to finish cooling.
- **Edge cases & failure modes (v2).** *Content longer than designed:*
  the line count is measured, not assumed — a 40-line block casts for
  90×39+1000 ≈ 4.5s; acceptable because cooling trails behind reading,
  but blocks >40 lines are split at paragraph boundaries by the builder
  (§15). *Shorter:* a 1-line block casts and cools in 1.0s flat.
  *Scroll back up:* cooled lines stay cool — metal does not reheat by
  being looked at; only §6.9's hover warms. *Resize:* line counts are
  re-measured; already-cooled blocks are never re-cast.
  *Font swap after cast:* the baseline grid re-locks to 28px; faces are
  gradient overlays, so a swap cannot strand a line mid-glow.
- **Accessibility spec (v2).** Casting is presentational: the text's
  semantics, reading order, and contrast (≥7:1 at the hottest frame,
  §6.1) never change. No aria-live announcements for casts — a screen
  reader user is reading, not watching a foundry, and the counter (§6.4)
  is `aria-hidden` with a static text equivalent in the footer (§6.16).
  Focus is never moved by a cast.
- **Performance budget & mobile variant.** One overlay per casting
  block, animating `clip-path` inset + opacity: ≤0.3ms/frame; at most
  2 blocks cast concurrently (the shared front enforces this
  naturally). Mobile variant: gradient steps 3, shimmer omitted on
  blocks beyond the first per section.
- **Tokens consumed (v2).** `--paper-shade`, `--metal`, `--amber`,
  `--amber-hot`, `--ease-cool`, `--dur-cool`, `--dur-stagger`, `--slug`.

### 6.3 Margin-tray pull-quote slugs

- **What & why.** A pull-quote in this theme is not a styled aside: it
  is the quote's own slug, lifted bodily out of the text column and set
  at −2° in the margin tray as the visitor scrolls through the quotes
  chapter. The same line of type, relocated — the tray ends up holding
  the page's best lines, which is exactly what a compositor's tray held.
- **Structure.** Each pull-quote exists twice in the DOM by design: its
  home line in the text (a normal slug line, §6.2) and its tray slug —
  a discrete slug bar in the tray track (§4), set at `rotate(-2deg)`,
  carrying the quote text in Zilla Slab 600 20px/28px. The home line is
  the accessible, reading-order copy; the tray slug is `aria-hidden`
  (a visual echo) — except at <1200px, where the tray retires and the
  tray slug becomes the only, fully accessible copy (§6.3 breakpoints).
- **Motion spec.** Scrubbed, not triggered: across a 60vh scroll span
  centred on the quote's home line, the tray slug's `translateY` moves
  from +46px (resting low in the tray, half behind the tray's front
  rule) to 0 (fully lifted and set), driven by the shared lerp loop
  (0.12). Its tilt settles from −4.5° to the licensed −2° across the
  same span with `--ease-lift` applied to the scrub value. Scrolling up
  reverses the lift exactly — the slug is set back down. At the span's
  end the slug is *filed*: its face cools (§6.2's curve, 1000ms) and it
  stays in the tray for the rest of the page.
- **Choreography timeline (v2).** Scrub span: quote line at 85%
  viewport → 25% viewport. 0–30% of span: slug rises 46→28px, tilt
  −4.5→−3.4°. 30–75%: rises 28→6px, tilt →−2.3°. 75–100%: final 6px
  with the clunk overshoot curve applied to the last 4px (`--ease-clunk`
  on the scrub tail), tilt lands at exactly −2.00°, cool begins. Cool
  completes 1000ms after the span ends (or after the visitor stops
  scrolling past it, whichever is later).
- **State matrix (v2).** *Rest:* filed state — slug in tray at −2°,
  cooled. *Hover (desktop):* the slug warms (§6.9) and tilts an extra
  −0.5° toward the tray's front edge over 200ms; its home line warms in
  sympathy at 50% intensity — the pair is visibly one line in two
  places. *Focus:* tray slugs are not focusable (decorative echo);
  the home line's links take standard focus. *Active:* n/a.
  *Scrolled-past:* filed, static. *Disabled:* JS off — the tray slug
  sits filed at −2° from first paint; the lift is an enhancement of a
  state, not the state itself. Touch: no hover sympathy; the scrub is
  identical.
- **Content merge.** The tray holds *this page's own lines* — quotes
  lifted from the text the visitor is reading, in the order they occur.
  A tray slug whose text does not appear verbatim in the column is a
  §10 gate failure.
- **Failure fallback.** No JS / no scrub support: slugs render filed.
  If the lerp loop detects <40fps sustained, scrub quantises to 4
  steps (the lift becomes a small staircase — still legible as lifting,
  cheaper to paint).
- **Reduced-motion variant.** Slugs filed from first paint; no lift, no
  tilt change, no sympathy warmth. The tray still holds the page's best
  lines — the content merge survives with zero motion.
- **Breakpoints (v2).** ≥1200px: as specced, tray 300px. 768–1199px:
  the tray retires into the measure — pull-quotes render as full-width
  slug bars *inside* the column at their home position, set at −2°,
  lifting 12px on scrub through a 40vh span. <768px: same in-column
  treatment, tilt reduced to −1° (a 2° slug at 350px wide clips its
  own notch), scrub span 30vh, and the slug becomes the accessible copy
  (home line suppressed to avoid duplication).
- **Edge cases & failure modes (v2).** *Two quotes in one chapter:*
  lifts are serialised by the shared loop — the second slug's span
  begins only after the first is filed; trays never perform two lifts
  at once. *Quote longer than 3 lines:* tray slugs cap at 3 lines;
  longer quotes are excerpted at a clause boundary with the slug-end
  stamp "⋯" and the full line stays in the column. *Jump scroll
  (anchor link past the chapter):* slugs land filed — scrub states are
  computed from scroll position, never accumulated.
- **Accessibility spec (v2).** Desktop: tray slug `aria-hidden`, home
  line carries the semantics (as a `<blockquote>` where the quote is
  genuinely quoted). Mobile: roles swap — the in-column slug is the
  blockquote, the home line is suppressed. Tilt is decorative; the
  slug's text contrast is body-grade (≥7:1 cooled, ≥4.5:1 at hottest
  sympathy warmth). No focusable elements are created by the lift.
- **Performance budget & mobile variant.** One transform on one slug at
  a time: ≤0.2ms/frame. The tray's other slugs are static. Mobile
  variant: the in-column treatment above — no tray track is laid out at
  all, saving the 300px track's paint cost.
- **Tokens consumed (v2).** `--paper-shade`, `--black`, `--amber`,
  `--lead`, `--ease-lift`, `--ease-clunk`, `--dur-cool`, `--slug`.

---

### 6.4 Galley-tray progress and the lines-set counter

- **What & why.** Progress on a Linotype page is not a percentage bar:
  it is output. The header's galley tray (§4) fills with one cast slug
  chip per completed section, and beside it the counter keeps the
  machine's tally — "lines set: n" — incrementing per line actually
  cast. The visitor can *count* the page. A progress indicator that is
  also a table of contents and also a production record is this theme's
  answer to the thin top bar every other site ships.
- **Structure.** In the fixed header: `<div class="galley-tray">`
  holding one `<span class="tray-slug">` per section (46×18px, face
  `--lead`, notch `--black`, section number reversed in the notch),
  in section order; and `<output class="lines-set">` with the label
  "lines set" in apparatus type and the count in tabular Zilla 500.
  A second counter, "words cast", appears only in the footer colophon
  (§6.16) as the page's final tally. Slug chips are links to their
  sections — the tray is navigation, not just display.
- **Motion spec.** A section completes when its last line's cool begins
  (§6.2). Its chip casts into the tray: `translateX(-52px) → 0` over
  300ms `--ease-clunk`, arriving warm (`--amber` face at 60%) and
  cooling to `--lead` over `--dur-cool`. The counter increments per
  line during the section's cast — not in one jump at the end: as each
  line's glow begins (§6.2), the tally ticks +1, digits rolling in
  tabular figures with a 120ms `--ease-cast` step per increment,
  batched to at most one visible tick per 90ms (the casting stagger —
  the counter *is* the casting, counted).
- **Choreography timeline (v2).** During §6.2's cast: t=90×(k−1) line
  k glows, tally ticks to include it. Section end: last line's cool
  begins → +0ms chip begins its 300ms deposit → +300ms chip seated,
  warm → +1300ms chip cooled to lead. The header never animates more
  than one chip at a time; sections completed in a jump scroll deposit
  their chips in order at 120ms intervals, already cool — output
  catching up with a fast reader is filed, not performed.
- **State matrix (v2).** *Rest:* tray holds the chips of all completed
  sections; incomplete sections have empty slots (a ruled outline —
  the tray shows its own capacity). *Hover:* a chip warms (§6.9, face
  to `--amber` 35%) and its section number brightens; the counter is
  not interactive. *Focus:* chips are links — 2px outline `--amber`
  (header is metal), offset 2px; focus order follows section order.
  *Active:* chip presses 1px (`--ease-clunk` release) before navigating.
  *Scrolled-past:* the tray is fixed; "past" applies per chip — a chip
  whose section is above the viewport is cooled lead; the chip for the
  section currently being read is the warm one. *Disabled:* JS off —
  all chips render present and cooled (the whole page exists; the tray
  degrades to a static contents strip), counter shows the page's true
  total lines, computed at build time. Touch: identical, hover states
  absent, chips are 46×34px tap targets via the tray's padding.
- **Content merge.** The tray accumulates the actual lines composed so
  far — its contents are the page's sections, its count is the page's
  lines. Both numbers are DOM-derived at runtime and build-derived in
  the fallback; an invented count is a §10 blocking failure.
- **Failure fallback.** No JS: static tray, full count, chips as anchor
  links. If the runtime line measurement fails (detached DOM, exotic
  embed), the counter hides rather than lie — the tray alone still
  reads as a contents strip.
- **Reduced-motion variant.** Chips appear seated and cooled at section
  completion; the counter sets to its value without rolling. Deposit
  order and contents are identical.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: chips shrink
  to 34×16px, counter keeps full "lines set: n". <768px: the tray
  channel hides its empty slots (a 12-section page cannot show 12
  slots at 350px); chips for completed sections only, counter label
  shortens to "lines: n". The header never exceeds two rows.
- **Edge cases & failure modes (v2).** *Many sections (>14):* chips
  compress to 26px wide, notches lose their numerals (kept in the
  link's accessible name); the tray never scrolls horizontally — a
  tray you must scroll is a second page hiding in the header.
  *Dynamic content (client-side route change):* the tray resets via
  §6.12's galley-slide; counts are re-measured per route. *Scroll back
  to top:* chips stay — output is not un-cast by rereading.
- **Accessibility spec (v2).** The tray is a `<nav aria-label="Sections,
  as cast">`; chips are links with names like "Section 3, The Magazine
  — cast". The live counter is `aria-hidden` (a ticking number is noise
  to a screen reader); a visually hidden static text — "This page sets
  N lines in M sections" — carries the fact once. Focus order: nameplate
  → tray chips in order → page.
- **Performance budget & mobile variant.** Counter ticks are text
  updates batched to the shared loop's frames: ≤0.1ms/frame. Chip
  deposits are single transforms. Mobile variant: the compressed tray
  above; the "words cast" footer tally is omitted under 768px (one
  number is enough on a phone).
- **Tokens consumed (v2).** `--black`, `--metal`, `--lead`, `--amber`,
  `--paper`, `--ease-clunk`, `--ease-cast`, `--dur-cool`.

### 6.5 The etaoin shrdlu error line

- **What & why.** The Linotype's keyboard was arranged by frequency —
  ETAOIN SHRDLU down the first columns — and an operator who made a
  mistake ran a finger down those keys to fill the line with gibberish,
  marking it for the proofreader's melting pot. This theme keeps the
  ritual: once per page, in the margin of its chapter, a line types
  itself as "etaoin shrdlu", and shortly after, the proofreader strikes
  it through. The machine's famous mistake, kept and corrected in
  place — the theme's signature honesty, and its one licensed joke,
  told deadpan.
- **Structure.** In the margin rail (§4) of one designated chapter —
  by default the chapter nearest the page's midpoint — a margin slug
  line in Zilla Slab 400 italic-free 16px, `--lead-ink`, reading
  "etaoin shrdlu" followed by the fill's tail "cmfwyp" at 60% opacity
  (operators filled the whole line). The strike is an inline SVG path
  across the line, drawn in `--amber-deep` at 2px — the proofreader in
  this foundry strikes in burnt amber, the colour of a correction that
  costs metal. A margin note in apparatus type beneath: "operator's
  error — struck, kept". The line is real DOM text.
- **Motion spec.** Trigger: the chapter enters at 50% viewport. The
  line types itself: characters appear left to right at 45ms per
  character (12 characters ≈ 540ms) with a 2px slug-notch blink at the
  typing front — no caret, the machine has no caret; the front is a
  brass matrix edge (a 2×18px `--amber-deep` bar). 700ms after the last
  character, the strike draws across the full line in `--dur-strike`
  (300ms) with `--ease-cast`, overshooting the final "p" by 6px the
  way a hand does. Then nothing: the error sits struck for the rest of
  the page.
- **Choreography timeline (v2).** t=0 chapter crosses 50% → t=150ms
  typing begins (the machine notices its operator late, as machines
  do) → t≈690ms line complete → t=1390ms strike begins → t=1690ms
  strike lands, overshoot settles → t=1800ms margin note fades from
  `--lead` 0% to full over 200ms. Total ≈2.0s, once per page, never
  repeated, never on a second chapter.
- **State matrix (v2).** *Rest:* the completed state — line present,
  struck, note visible. This is the no-JS state: the error ships
  pre-struck in the static build and JS rewinds it only if it can run
  the full ritual. *Hover:* the struck line warms faintly (§6.9 at 40%
  intensity) — even errors are this page's lines. *Focus:* not
  focusable; the note is plain text. *Active:* n/a. *Scrolled-past:*
  struck state, static. *Disabled:* JS off = rest. Touch: identical.
- **Content merge.** The error is a real line in the margin's
  composition, in the chapter where a compositor would make it, at the
  page's midpoint where fatigue sets in. It is not a sticker, a footer
  gag, or an Easter egg hunt: it sits in the margin doing the margin's
  work — showing the page's manufacture, including its failure.
- **Failure fallback.** Static build ships the line struck (the SVG
  strike's final path is the CSS default; JS rewinds it to animate).
  If the typing is interrupted (tab switch), the watchdog completes
  the line and strike instantly at the 1.2s law's margin equivalent
  (2.5s for this element — the ritual is longer than a cast).
- **Reduced-motion variant.** Line present and struck from first paint;
  note present. No typing, no strike draw. The honesty survives; the
  performance does not.
- **Breakpoints (v2).** ≥1200px: margin rail, as specced. 768–1199px:
  the rail retires — the error line moves into the measure as a
  full-width margin slug between paragraphs of the designated chapter,
  same ritual. <768px: same in-column placement, typing at 35ms per
  character (a phone screen shows less line; the joke must not outstay
  its welcome).
- **Edge cases & failure modes (v2).** *Page too short for a midpoint
  chapter:* the error belongs to the second chapter; a one-chapter page
  (landing hero only) omits it — §1's minimum page length exists
  partly for this. *Multiple pages, one session:* once per page, every
  page — it is the machine's habit, not a campaign. *Screen-reader
  text alternatives:* the struck line's accessible name is "etaoin
  shrdlu — the operator's error row, struck through by the
  proofreader", so the joke is told, not hidden, to AT users.
  *Translation:* the line is never translated; it is a keyboard
  artefact, and the margin note translates around it.
- **Accessibility spec (v2).** The line uses `<s>` semantics with the
  aria label above; the strike SVG is `aria-hidden`. Typing is visual
  only — the full line is in the DOM from first paint (JS masks it to
  type), so AT users get the completed error immediately. Contrast:
  `--lead-ink` on paper 5.54:1, strike `--amber-deep` is a graphic at
  3:1+ against both line and ground.
- **Performance budget & mobile variant.** Typing is 16 text-node
  updates over 540ms + one SVG path draw: negligible, off the shared
  loop (a one-shot timer chain). Mobile variant: the in-column
  placement above.
- **Tokens consumed (v2).** `--lead-ink`, `--amber-deep`, `--paper`,
  `--paper-shade`, `--ease-cast`, `--dur-strike`.

### 6.6 Heat-shimmer idle and the oil sheen

- **What & why.** Hot metal announces itself: air above a fresh slug
  wobbles. This element is the theme's ambient life — a refraction
  shimmer idling over the freshest-cast slug only, moving to each new
  slug as it is cast — plus an oil sheen that drifts slowly across dark
  metal sections, the machine's lubrication made visible. Two loops,
  both earned: the shimmer is a line's own heat; the sheen is the
  machine's own surface.
- **Structure.** The shimmer is a pseudo-element layer over the current
  freshest slug: a 100%×(slug height + 10px) strip carrying an SVG
  turbulence displacement (feTurbulence + feDisplacementMap, scale 2px)
  over a transparent copy of the slug's gradient — the *air* distorts,
  the type does not (the slug's text is never the shimmer's target; a
  second, text-free overlay refracts the bar's face and edges only).
  The sheen is a 140%-wide linear gradient (`--lead` at 0% → 7% → 0%)
  on metal sections, translating across on a 26s loop.
- **Motion spec.** Shimmer: ±1px displacement oscillation on
  `--dur-shimmer` (1800ms) `--ease-shimmer`, infinite while its slug is
  the freshest and on screen. When a new line casts (§6.2), the
  shimmer's allegiance transfers at the new line's glow peak: the old
  slug's shimmer fades over 300ms, the new one's fades in over 300ms —
  heat follows manufacture. Sheen: `translateX(-20%) → (20%)` over 26s
  linear, alternate; only while the metal section is ≥10% in view.
- **Choreography timeline (v2).** Continuous. Transfer beats: t=0 new
  line glows → t=0 old shimmer fade begins (300ms) → t=150ms new
  shimmer at 50% → t=300ms transfer complete. On page load, the hero's
  last-cast line holds the shimmer until §6.2's first section cast
  takes it. When the page's final line has cooled for 4s with no new
  cast, the shimmer retires (fade 600ms) — a finished page is a cool
  page, and stillness is its correct end state.
- **State matrix (v2).** *Rest:* sheen drifting on visible metal;
  shimmer on the freshest slug. *Hover:* hovering the shimmering slug
  is §6.9 warmth — the shimmer's amplitude rises to ±1.4px while
  hovered (attention stokes heat). *Focus:* no interaction.
  *Active:* n/a. *Scrolled-past:* both loops pause when their host is
  off-screen (IntersectionObserver gates, zero cost when idle).
  *Disabled:* JS off — no shimmer, no sheen; metal sections are flat
  `--metal`, which they were designed to survive. Touch: shimmer as
  specced (it is scroll-born, not hover-born); hover amplitude n/a.
- **Content merge.** The shimmer sits on a specific line and means
  *this one is newest* — it is information (where the casting frontier
  is) rendered as physics. The sheen never crosses text at more than
  7% opacity and never touches paper sections.
- **Failure fallback.** No SVG filter support: the shimmer degrades to
  a soft amber glow pulse (opacity 0→.18→0 on the same 1800ms) — less
  true, still honest about which line is fresh. No JS: neither loop
  exists; nothing is missing from the content.
- **Reduced-motion variant.** Both loops off. The freshest slug is
  identified statically instead: its notch carries `--amber-deep`'s
  mark "fresh" in apparatus type. Information preserved, motion zero.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced. <768px:
  shimmer displacement drops to ±0.6px and the sheen's loop lengthens
  to 40s — small screens and small batteries get smaller weather.
- **Edge cases & failure modes (v2).** *Low-power / <40fps sustained:*
  the shared loop sheds the sheen first, then reduces the shimmer to
  the glow-pulse fallback. *Long pages:* only one shimmer exists at
  any moment by construction — the element cannot multiply.
  *`save-data`:* both loops off, same as reduced motion.
- **Accessibility spec (v2).** Both loops are purely decorative and
  `aria-hidden`; neither carries information an AT user lacks (the
  "fresh" mark covers the shimmer's meaning). Displacement never
  applies to live text, so reading is never distorted. Loops respect
  `prefers-reduced-motion` without exception — an ambient loop that
  ignores the preference is a §10 blocking failure.
- **Performance budget & mobile variant.** SVG filter on one slug-sized
  strip: ≤0.5ms/frame, the theme's most expensive ambient — hence one
  instance, ever. Sheen: one gradient transform per metal section,
  ≤0.2ms/frame, max 2 sections concurrently visible. Mobile variant:
  the reduced amplitudes above.
- **Tokens consumed (v2).** `--amber`, `--lead`, `--metal`,
  `--amber-deep`, `--ease-shimmer`, `--dur-shimmer`, `--slug`.

---

### 6.7 The belt-and-pulley footer draw

- **What & why.** At the foot of the page, the machine that cast it is
  finally shown: the Linotype's belt-and-pulley drive, drawn as an SVG
  line illustration that draws itself as the footer enters, above the
  90-key keyboard ornament (§6.11's full-size home). The ornament is
  not decoration pasted at the bottom — it is the page's colophon as
  machinery: *the thing that made every line above this one.*
- **Structure.** One inline SVG, viewBox 1200×180: two pulley wheels
  (Ø 120px and Ø 72px) with spokes, a belt path looping both, the
  drive shaft, and the casting mechanism's silhouette at the right —
  all stroked in `--lead` at 2px on `--black`, no fills. Beneath it,
  the keyboard band (§6.11). Beside it, the colophon text (§6.16).
  Every path's final state is the CSS default; JS rewinds
  `stroke-dashoffset` to draw.
- **Motion spec.** Trigger: footer crosses 60% viewport. Paths draw in
  mechanical order — belt first (the loop that moves everything), then
  the large pulley, the small pulley, the shaft, the mechanism — each
  path's draw duration proportional to its length at a constant
  900px/s, total ≈ `--dur-draw` (900ms) staggered so paths overlap by
  30%: the machine assembles itself at machine speed. On completion,
  the pulleys begin a slow rotation (large wheel 360° per 24s linear;
  small wheel geared inversely, 360° per 14.4s — the ratio is the
  wheels' real diameter ratio, 120:72) and the belt's dash pattern
  creeps to match. Rotation is the page's only perpetual footer motion
  and it stops the moment the footer leaves view.
- **Choreography timeline (v2).** t=0 footer crosses 60% → t=0 belt
  begins (path ≈700px, 780ms) → t=250ms large pulley begins (560ms) →
  t=450ms small pulley (380ms) → t=600ms shaft + mechanism (420ms) →
  t≈1020ms drawing complete → t=1200ms rotation fades in over 800ms
  (a machine does not lurch into motion). Total to full life ≈2.0s,
  once per page.
- **State matrix (v2).** *Rest:* drawn, rotating while visible.
  *Hover:* hovering a pulley slows its rotation to 25% speed over
  400ms — a hand resting on the wheel — and its label (apparatus,
  "main drive, 1886 pattern") appears beside it. *Focus:* the SVG is
  decorative (`aria-hidden`); the colophon text beside it carries the
  facts. *Active:* n/a. *Scrolled-past:* rotation paused off-screen.
  *Disabled:* JS off — the machine sits fully drawn and still; the
  drawing was always the end state. Touch: no hover slow; rotation
  as specced.
- **Content merge.** The drawing is the same machine the page has been
  describing since the hero: its belt drives the casting the visitor
  watched. Its labels name real parts with real functions. Remove the
  draw animation and a labelled machine diagram remains — content,
  not garnish.
- **Failure fallback.** Static SVG, fully drawn (CSS default state).
  If dash measurement fails (path without `getTotalLength` support),
  the draw is skipped and the machine simply appears — with the
  rotation, which needs no measurement.
- **Reduced-motion variant.** Machine drawn and still. No draw-in, no
  rotation. Labels present.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: SVG scales to
  measure width, mechanism silhouette simplified (builders may drop
  the third path group). <768px: the drawing stacks above the keyboard
  band at 100% width; rotation slows ×1.5 (24s → 36s) — a small screen
  gets a calmer machine.
- **Edge cases & failure modes (v2).** *Footer reached by jump link:*
  the draw plays from the jump (trigger is positional). *Print:* the
  SVG prints as a line diagram; rotation obviously absent; the
  colophon must not depend on it (§6.16). *Repeat visits:* the draw
  plays per page load — it is the machine starting its shift.
- **Accessibility spec (v2).** `role="img"` with an accessible name —
  "Line drawing of the Linotype's belt-and-pulley drive" — or
  `aria-hidden` where the adjacent colophon already says it; choose
  one per build, never both. Rotation is decorative and stops under
  reduced motion. Pulley labels are real text, not SVG text, so they
  scale with the page's type.
- **Performance budget & mobile variant.** Draw: ≤5 paths animating
  dashoffset, ≤0.3ms/frame for ≈1s. Rotation: 2 transforms, ≤0.1ms/
  frame, observer-gated. Mobile variant: the simplified stack above.
- **Tokens consumed (v2).** `--black`, `--lead`, `--amber-deep`,
  `--dur-draw`, `--ease-cast`.

### 6.8 Slug-frame images

- **What & why.** Even photographs are cast in this theme: every image
  sits inside a slug-bar frame — the bar's notch and reversed-type
  edges extended around the picture — and as the image centres in the
  viewport it scale-settles inside its frame while its amber cast
  cools. A page whose pictures obey the same manufacture as its lines
  never breaks its own fiction.
- **Structure.** `<figure class="slug-frame">`: a bar (§4 anatomy)
  widened to image height — notch column at the left carrying the
  figure's number reversed ("FIG. 3"), the image inside a clipped
  frame with a 1px `--hairline` edge, and the caption set as the
  frame's final slug line beneath (Zilla 14px, `--lead-ink`). The
  image's intrinsic ratio is reserved in CSS (`aspect-ratio` from the
  asset's real dimensions) — frames never reflow.
- **Motion spec.** Trigger: figure enters at 75% viewport. The image
  scales 1.06 → 1 over 700ms `--ease-cast` (clipped by the frame — the
  picture is cast into its bar), while an amber overlay on the image
  cools from 22% to 0 over `--dur-cool` on `--ease-cool`, timed so the
  image is fully cool exactly as it crosses viewport centre. The
  caption slug casts per §6.2 as the figure completes.
- **Choreography timeline (v2).** t=0 figure crosses 75% → t=0 scale
  and cool begin together → t=700ms scale seated → t=1000ms cool
  complete (centre-crossing on a standard scroll) → t=1000ms caption
  casts (90ms stagger per its lines). Fast scroll: figures entering
  already past centre render seated and cool — the state is computed
  from position, not accumulated.
- **State matrix (v2).** *Rest:* seated, cooled, captioned.
  *Hover (desktop):* the frame's slug warms (§6.9 applies to the frame,
  not the photograph — the image itself does not re-tint; the bar
  around it warms to `--amber` 20%). *Focus:* images with links take
  the standard outline on the frame. *Active:* n/a. *Scrolled-past:*
  static. *Disabled:* JS off — images seated at scale 1, no overlay;
  the frame and caption are pure CSS. Touch: identical minus hover.
- **Content merge.** The frame is the image's slug: its notch carries
  the figure number, its caption is set as a cast line, and the image
  undergoes the page's universal rite (cast, cool). Nothing about the
  frame is detachable decoration — remove it and the figure loses its
  number and its place in the page's count of figures (§12 voice).
- **Failure fallback.** Image fails to load: the frame holds its ratio
  with `--paper-shade` face and the caption plus alt text set as slug
  lines inside it — a broken image degrades to a labelled empty slug,
  never a collapsed hole. No JS: as specced in *Disabled*.
- **Reduced-motion variant.** No scale, no cool: image seated, caption
  present. The frame remains (it is layout, not motion).
- **Breakpoints (v2).** ≥1200px: figures may span measure + tray
  (984px) for chapter-opening plates. 768–1199px: measure width only.
  <768px: notch column shrinks to 18px, figure number rotates into the
  caption ("Fig. 3 — …"), scale travel reduces to 1.03 → 1.
- **Edge cases & failure modes (v2).** *Portrait images:* the frame's
  notch runs vertically the full height — tall slugs are correct in
  this theme; do not crop a portrait into a landscape bar.
  *Tiny images (<200px wide):* no scale animation (nothing to cast);
  cool only. *Lazy-loaded below-fold images:* the trigger is
  positional, so a late-loading image casts when it arrives *and* is
  in view; if it loads already in view past centre, it renders cool.
- **Accessibility spec (v2).** Real `alt` on every image; the frame and
  notch are presentational. Caption is a real `<figcaption>`. Scale
  and cool are decorative; the image is fully visible in its rest
  state at all times (the overlay never exceeds 22% and the scale
  never clips content out of the frame's reserved box).
- **Performance budget & mobile variant.** One transform + one opacity
  per figure, ≤2 figures animating concurrently (the shared loop
  serialises beyond that): ≤0.3ms/frame. Images themselves are the
  page's real weight — see §14. Mobile variant: the reduced scale
  above.
- **Tokens consumed (v2).** `--paper-shade`, `--hairline`, `--amber`,
  `--lead-ink`, `--black`, `--ease-cast`, `--ease-cool`, `--dur-cool`.

### 6.9 Warm-a-degree hover

- **What & why.** Attention reheats metal. Hovering any slug warms it:
  an amber tint rises under the pointer and cools again on leave. It
  is the theme's whole hover language — no lifts, no shadows, no
  underlines that the machine couldn't produce — and it teaches the
  visitor the theme's physics in one gesture: *what you attend to
  gets hot.*
- **Structure.** A per-slug overlay (the same cooling-gradient layer
  §6.2 uses) driven to a warm state: on paper slugs, `--amber` at 0→
  18% over the face; on metal slugs, `--amber` at 0→28% (heat reads
  stronger on black). The overlay sits behind the type (§4), so text
  contrast never drops below the §2 hot-end figures.
- **Motion spec.** Warm: overlay to full warmth over `--dur-warm`
  (250ms) `--ease-cool`. Cool on leave: back to rest over 600ms
  `--ease-cool` — cooling is slower than warming, as it is in the
  foundry. The warmth is uniform across the slug (heat soaks the whole
  bar), never a radial pointer-follow gradient: slugs do not do
  spotlights.
- **Choreography timeline (v2).** t=0 pointer enters → t=250ms full
  warmth → pointer leaves at t=x → t=x+600ms rest. Re-entry during
  cool: warms from the current value (the overlay's value is stateful,
  never snapped). A slug still cooling from its cast (§6.2) ignores
  hover warmth until it reaches rest — fresh metal is already hot.
- **State matrix (v2).** *Rest:* cool face. *Hover:* as specced, desktop
  pointers only (`hover: hover` media). *Focus:* keyboard focus warms
  the focused slug identically and holds the warmth while focus stays —
  focus is attention too, and this is how keyboard users get the
  theme's physics. *Active:* §6.10's clunk supersedes on slugs that
  are controls. *Scrolled-past:* n/a. *Disabled:* the overlay is a
  visual state only; disabling JS removes warmth, nothing else.
  Touch: no hover warmth; a tap on a control slug is §6.10, a tap on
  text does nothing — text is not a button.
- **Content merge.** Warmth is a property of the line being read, in
  its tray position, applied to its own bar. It cannot be detached and
  reused as a generic hover effect elsewhere in the UI: buttons that
  are not slugs do not warm (§11 gives controls their own treatments).
- **Failure fallback.** Overlay is CSS-driven (`:hover`/`:focus-within`
  set a custom property the loop-free transition animates); if the
  property fails, slugs simply don't warm. No content depends on it.
- **Reduced-motion variant.** Warmth applies *instantly* (no 250ms
  ramp) at half intensity (9% / 14%) and removes instantly — the state
  change is information (which line has attention), the ramp is not.
- **Breakpoints (v2).** All breakpoints: identical on devices with a
  hover-capable pointer. Touch devices at any size: focus warmth only.
- **Edge cases & failure modes (v2).** *Pointer crossing many slugs
  fast:* each slug's cool is independent; a fast sweep leaves a cooling
  trail — correct physics, and the 600ms cool caps the trail's length.
  *Slug inside the pinned keyboard's shadow region:* warmth still
  applies; layers are independent. *Forced-colors mode:* the overlay
  is suppressed and focus/hover fall back to the platform outline —
  specified, not accidental.
- **Accessibility spec (v2).** Warmth is never the only signal of
  anything: links keep their §11 treatment (weight + rule) independent
  of warmth. Focus warmth accompanies, never replaces, the visible
  outline. Overlay behind text keeps contrast ≥7:1 at full warmth
  (§2, hot-end figures).
- **Performance budget & mobile variant.** CSS transitions on opacity
  of one overlay per hovered slug: no shared-loop cost. Mobile: focus
  warmth only, as above.
- **Tokens consumed (v2).** `--amber`, `--ease-cool`, `--dur-warm`,
  `--paper-shade`, `--metal`.

---

### 6.10 The casting-clunk click

- **What & why.** Clicking a slug that is a control gives the machine's
  answer: the slug slides 4px toward the machine (left, into its
  notch), locks with the clunk overshoot, and flashes a cool-down —
  an amber spike that decays to lead in 300ms. The click *casts* the
  choice. It is the theme's only click animation, and its restraint is
  the point: one soundless, physical confirmation per deliberate act.
- **Structure.** Applies to slug-shaped controls: tray chips (§6.4),
  tray slugs that link (§6.3's mobile variant), galley cards' slugs
  (§6.14), and the casting form's submit slug (§6.15). The element
  carries the §4 bar anatomy; the clunk is a transform on the whole
  bar plus the §6.9 overlay driven to a spike.
- **Motion spec.** On activation: `translateX(0 → −4px)` over 90ms
  `--ease-cast` (the slide into the mould), a 1px overshoot return
  (`--ease-clunk`, 60ms), then the flash: overlay spikes to `--amber`
  45% and cools to rest over the remaining 150ms of `--dur-clunk`
  (300ms total). Navigation or the control's action fires at the lock
  moment (t≈150ms), not after the flash — the machine does not make
  the visitor wait for its own cooling.
- **Choreography timeline (v2).** t=0 activation → t=90ms slug seated
  −4px → t=150ms overshoot resolved, action fires, flash at peak →
  t=300ms flash cooled, slug returns to x=0 over the final 80ms
  (overlapping the cool). Total 300ms; the visitor perceives one
  clunk, not three moves.
- **State matrix (v2).** *Rest:* seated, cool. *Hover:* §6.9 warmth
  (control slugs warm like any slug). *Focus:* outline + warmth held
  (§6.9). *Active:* the clunk above — `:active` alone (no JS) gives
  the −4px slide without the flash, so the gesture survives JS
  failure in degraded form. *Scrolled-past:* n/a. *Disabled:* a
  disabled slug control renders as a filed slug — face `--lead`,
  notch greyed, no warmth, no clunk, `aria-disabled` with the reason
  in its label where the product knows it ("Section 4 — not yet
  cast" is a state, not an error). Touch: the clunk fires on tap-up;
  tap targets ≥44px (§6.4's tray padding rule applies theme-wide).
- **Content merge.** The clunk acts on the line itself, in its tray
  position: the thing clicked is the thing that moves, flashes, and
  navigates. There is no detached ripple, toast, or spinner pretending
  the act happened elsewhere.
- **Failure fallback.** The control is a real link/button: without JS
  it navigates on click with the `:active` slide only. The flash is
  enhancement; the action never is.
- **Reduced-motion variant.** No slide, no flash: the control's state
  change is instant, and the confirmation is the navigation itself
  plus a 120ms `--amber-deep` outline pulse on paper (a colour beat,
  not a movement).
- **Breakpoints (v2).** All sizes identical; at <768px the slide is
  3px (a phone's slug is lighter metal).
- **Edge cases & failure modes (v2).** *Double-click / impatient
  repeat:* the clunk is idempotent — re-activation during the 300ms
  restarts the flash but never double-fires the action (the control's
  own semantics govern; the animation holds no state). *Keyboard
  activation (Enter/Space):* the clunk plays identically — keyboard
  users get the machine's answer too. *Slug that is not a control:*
  no clunk, ever; text slugs warm (§6.9) and nothing more. A page
  where body text clunks is a toy, not a theme (§9).
- **Accessibility spec (v2).** The clunk is decorative feedback on a
  real control with a real accessible name; nothing about the action
  is conveyed by motion alone. Focus outline persists through the
  flash. The 300ms total stays under vestibular-risk thresholds: 4px,
  once, no oscillation.
- **Performance budget & mobile variant.** One transform + one opacity
  per activation: negligible, off the shared loop (event-driven).
  Mobile variant: the 3px slide above.
- **Tokens consumed (v2).** `--amber`, `--amber-deep`, `--lead`,
  `--ease-cast`, `--ease-clunk`, `--dur-clunk`.

### 6.11 The pinned keyboard chapters

- **What & why.** The Linotype's keyboard — 90 keys in frequency order,
  ETAOIN SHRDLU down the first two columns — is the machine's input,
  and during the page's composing chapters it pins to the viewport
  foot while lines cast above it: the input stays under the composition
  it produces. When the composing ends, the keyboard releases and
  settles into the footer (§6.7), where it lives at full size.
- **Structure.** A keyboard band, 92px tall at desktop: 90 key caps in
  the true Linotype arrangement (three banks; the first two columns
  read E T A O I N / S H R D L U), caps 26×26px at ≥1200px, face
  `--metal`, legends in `--paper` Zilla 600 11px, the ETAOIN/SHRDLU
  columns' caps edged in `--amber-deep` — the only permanent amber
  licence outside §2's list, granted because those columns *are* the
  theme's signature (§6.5's line is typed on them). The band pins via
  `position: sticky` within the chapters wrapper — no JS pinning, no
  layout jumps: the wrapper reserves the band's height at all times.
- **Motion spec.** Pinning itself is motionless (sticky). Two motions
  live on the band: as each line casts above (§6.2), the keys of that
  line's most frequent letters *dip* — the cap of the line's dominant
  letter presses 2px for 120ms `--ease-clunk` at the moment the line's
  glow begins (one dip per line, the operator's hand abstracted to its
  busiest finger); and when the chapters end, the band un-pins and
  the full keyboard in the footer (§6.7) receives it — no animation of
  transfer, a cut: the pinned band is a *preview* of the footer's
  keyboard at 60% scale, and the footer shows it whole.
- **Choreography timeline (v2).** Continuous during chapters 2…n−1.
  Per cast line: t=line's glow → the dominant-letter cap dips (120ms)
  → returns. Pin start: first chapter's first line crossing 70%.
  Pin end: footer's top crossing 100% viewport — the sticky releases
  by construction. If the page has only two chapters, the band never
  pins (§1's minimum length) and lives only in the footer.
- **State matrix (v2).** *Rest (outside chapters):* band absent from
  the viewport foot; footer keyboard static. *Hover:* hovering a cap
  shows its letter's rank in apparatus beneath the band ("E — 1st,
  12.7% of English") — real frequency data, the keyboard teaching its
  own logic. *Focus:* caps are not focusable (the band is an ornament
  with a lesson, not a control); the rank readout is plain text in the
  DOM beside the band. *Active:* n/a. *Scrolled-past:* released.
  *Disabled:* JS off — the band still pins (sticky is CSS) but no caps
  dip; the ornament survives its animation. Touch: no hover readout;
  the rank line is printed statically under the band instead.
- **Content merge.** The keyboard is not clip-art at the page's edge:
  its dips are driven by the actual lines being cast above it, its
  arrangement is the real ETAOIN SHRDLU layout, and its footer home is
  beside the machine drawing (§6.7) that its keystrokes power. A
  generic QWERTY keyboard here would be a §10 failure — the layout is
  content.
- **Failure fallback.** No sticky support (ancient embeds): the band
  renders once, statically, at the chapters wrapper's end — the lesson
  without the pin. No JS: as *Disabled*.
- **Reduced-motion variant.** The band pins (position is not motion)
  but caps never dip; the rank readout is static. Under
  `prefers-reduced-motion` combined with <768px, the band does not pin
  at all — a phone's viewport is too small to lend 92px to an ornament
  (§14's cut order agrees).
- **Breakpoints (v2).** ≥1200px: 90 caps at 26px, band 92px.
  768–1199px: caps 20px, band 76px, rank readout on tap/focus only.
  <768px: the band shows the first two banks only (60 caps) at 16px,
  band 64px, and pins only during the single longest chapter.
- **Edge cases & failure modes (v2).** *Chapter shorter than the
  viewport:* pinning still works (sticky within the wrapper) but no
  cap dips if no line casts while pinned. *The etaoin chapter (§6.5):*
  when the error line types, the ETAOIN and SHRDLU caps dip in
  sequence, 45ms apart, in typing order — the one time the keyboard
  performs, and it is performing the mistake. *Footer keyboard and
  pinned band both visible* (short last chapter): the pinned band
  fades to 0 over 200ms as the footer's band enters — the page never
  shows two keyboards at once.
- **Accessibility spec (v2).** The band is `role="img"` with the name
  "The Linotype keyboard: ninety keys arranged by letter frequency,
  ETAOIN SHRDLU down the first columns". Dips are decorative. The
  rank readout is real text. The pinned band never covers content:
  the wrapper's reserved height means text scrolls *above* a fixed
  floor, and the band is excluded from the reading column's width at
  every breakpoint.
- **Performance budget & mobile variant.** Sticky: zero loop cost.
  Dips: one transform per cast line, ≤0.1ms/frame. The band's caps are
  one background sprite/DOM of 90 small elements painted once. Mobile
  variant: the 60-cap band above.
- **Tokens consumed (v2).** `--metal`, `--black`, `--paper`, `--lead`,
  `--amber-deep`, `--ease-clunk`.

### 6.12 Empty-bar skeleton and the galley-slide transition

- **What & why.** Loading and navigation are the compositor's own
  furniture. While content loads, the page shows empty slug bars —
  the bars are there, the type is not yet cast — which fill with
  reversed type as real content arrives. On navigation, the galley
  slides off and a fresh tray of slugs casts in. Both states tell the
  truth about what is happening: *not yet composed* and *recomposing*.
- **Structure.** Skeleton: for each expected block, an empty bar at the
  block's exact slug anatomy (§4) — notch present, face `--paper-shade`
  (or `--metal`), with a `--lead` pulse at 35%→55% opacity on a 1400ms
  loop travelling left to right (the machine warming). Bars match the
  real layout's line counts where the server knows them; where it
  doesn't, a standard 5-bar paragraph + headline bar is used and the
  swap is height-matched to prevent layout shift. Transition: a
  full-measure galley panel (the outgoing page's tray surface) that
  slides, carrying the incoming page's first slugs at its leading edge.
- **Motion spec.** Skeleton fill: as each block's content arrives, its
  bars cast per §6.2 (glow → cool) — loading *is* casting, so the
  skeleton and the content share one rite and the page never "pops".
  If all content arrives at once, bars cast in reading order with the
  90ms stagger, capped at 12 bars of ceremony; the rest arrive filed.
  Transition: outgoing galley `translateX(0 → −100%)` over
  `--dur-slide` (500ms) `--ease-cast`; the incoming page's hero begins
  its §6.1 cast at t=350ms, overlapping the slide's tail; the galley
  tray (§6.4) resets during the slide, hidden by the motion.
- **Choreography timeline (v2).** Skeleton: t=0 bars shown (after a
  200ms grace — content faster than 200ms never shows a skeleton at
  all) → per block arrival, cast per §6.2 → page fully cast when the
  last block cools. Transition: t=0 navigation committed → t=0 slide
  begins → t=350ms incoming hero line 1 casts → t=500ms slide complete
  → hero continues per §6.1. Total perceived interruption ≈500ms.
- **State matrix (v2).** *Rest:* n/a (transient states). *Hover/focus:*
  skeleton bars are inert and removed from the accessibility tree
  (`aria-hidden`, with a single `role="status"` "Composing the page"
  announcement). During the transition, focus moves to the incoming
  page's headline at slide end — the one licensed focus move in the
  theme, because the page itself changed. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled:* JS off — no skeleton (server
  renders content), no transition (plain navigation). Touch:
  identical; slide distance is viewport-relative at all sizes.
- **Content merge.** The skeleton's bars are the page's own layout in
  waiting — same measure, same slug counts, same tray. The transition
  slides the *galley*, the page's own furniture, not a branded wipe
  unrelated to the content it replaces.
- **Failure fallback.** Content that fails to load leaves its bars
  standing with an error slug cast in place (§11's alert slug: "This
  line could not be cast — retry" as a real button). A transition that
  errors mid-slide completes instantly to the incoming page — the
  visitor is never left between pages.
- **Reduced-motion variant.** No skeleton pulse (static empty bars),
  no slide: navigation is a cut, and incoming content arrives filed
  and cooled. The status announcement remains.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: slide
  distance 100% of the measure. <768px: the transition slide is
  refused — a full-screen slide on a phone reads as the app breaking;
  navigation cuts, and the incoming hero still casts (its own rite,
  §6.1, is not a transition).
- **Edge cases & failure modes (v2).** *Slow block in a fast page:*
  blocks cast as they arrive, out of order if necessary — but the
  galley tray (§6.4) counts a section only when *all* its blocks have
  arrived, so the tally never claims a half-set section. *Back
  button:* the restored page arrives filed and cooled (history state
  is output, not a performance). *Prefetch:* a prefetched page skips
  the skeleton entirely.
- **Accessibility spec (v2).** One `role="status"` announcement per
  load ("Composing the page" → "Page composed: N lines set"), never
  per bar. Skeleton bars `aria-hidden`. The transition's focus move
  targets the incoming `<h1>` with `tabindex="-1"` and no visible
  outline flash. Reduced-motion users get cuts, per above.
- **Performance budget & mobile variant.** Skeleton pulse: one
  gradient per bar, ≤6 bars pulsing concurrently, ≤0.3ms/frame.
  Transition: one full-screen transform for 500ms — the theme's most
  expensive single move, licensed once per navigation. Mobile: the
  cut variant above.
- **Tokens consumed (v2).** `--paper-shade`, `--metal`, `--lead`,
  `--amber`, `--ease-cast`, `--dur-slide`, `--dur-stagger`.

---

### 6.13 The nameplate navigation

- **What & why.** A Linotype carried its maker's nameplate — *Mergenthaler
  Linotype Co.* — cast into the machine's frame. The site's header does
  the same: the nameplate is a foundry-black plate with the site's name
  reversed out of it, and the navigation sits beneath it as the galley
  tray (§6.4) plus a row of section slugs. Header, progress, and
  contents are one piece of furniture because on the machine they were
  one piece of iron.
- **Structure.** Header (fixed, two rows, 90px total at desktop): row 1
  — the nameplate (site name in Fraunces 560 22px, `--paper` on
  `--black`, letterpress-debossed 1px), left; the issue line right
  (apparatus: date, edition, "set in Zilla & Fraunces" — real data,
  §12). Row 2 — the galley tray (§6.4) full width. Primary navigation
  lives in the tray's left end: up to 5 section slugs (bar anatomy at
  apparatus scale) preceding the progress chips; beyond 5 sections, a
  "galley index" slug opens the full contents as a dropdown tray
  (§11). On mobile the two rows compress to one (56px): nameplate +
  lines-set counter + index slug.
- **Motion spec.** On scroll past 140px the header compresses: row 1's
  issue line fades (200ms), the nameplate shrinks to 18px, total height
  90→64px over 300ms `--ease-cast` — the machine lowers its profile as
  reading begins, and expands again within 8px of the top (hysteresis
  prevents hunting). Nav slugs warm on hover (§6.9) and clunk on click
  (§6.10). The current section's nav slug is *filed warm*: its face
  holds `--amber` at 12% permanently while its section is in view —
  the one standing warmth in the header, marking the live line.
- **Choreography timeline (v2).** Compression: t=scrollY crosses 140 →
  300ms compress. Expansion: t=scrollY < 132 → 300ms expand. Section
  change: the outgoing nav slug cools (600ms, §6.9's cool), the
  incoming warms to its standing 12% over 250ms — the header's warmth
  migrates with the reading, one slug at a time.
- **State matrix (v2).** *Rest:* expanded at top, compressed in flow.
  *Hover:* nav slugs warm (§6.9). *Focus:* standard outline (`--amber`
  on the black plate), focus order: nameplate (home link) → nav slugs
  → tray chips (§6.4) → index. *Active:* §6.10 clunk. *Scrolled-past:*
  the compressed state *is* the scrolled state. *Disabled:* JS off —
  header renders expanded and static (compression is a scroll listener
  + CSS class; without it the header is simply taller). Touch: no
  hover warmth; current-slug warmth identical.
- **Content merge.** The nameplate is the brand, the issue line is real
  publication data, the tray is the page's contents and output record.
  The header contains nothing that is not the site or the page.
- **Failure fallback.** No JS: static expanded header, all links live.
  Sticky failure: header falls back to absolute at top — navigation
  remains reachable via the footer's colophon links (§6.16).
- **Reduced-motion variant.** Compression is instant (height steps, no
  transition); warmth states apply instantly at §6.9's reduced
  intensities.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: issue line
  drops its edition field. <768px: single-row compressed header at all
  scroll positions (a phone never gets the tall plate); nav slugs move
  entirely into the index tray.
- **Edge cases & failure modes (v2).** *Long site names:* the nameplate
  truncates at 24 characters with the full name in the home link's
  accessible name — a plate is cast to fit its frame. *Many sections:*
  §6.4's chip compression applies; nav slugs cap at 5 + index by
  construction. *Anchor jumps:* the current-slug warmth recomputes
  from position on the next loop frame — never stale by more than
  100ms.
- **Accessibility spec (v2).** Landmark `banner` + `nav` with distinct
  labels ("Site" / "Sections, as cast"). The current section's slug
  carries `aria-current="true"` — warmth is never the only signal.
  Compressed and expanded headers expose identical content to AT.
  Contrast: nameplate 14.63:1; apparatus on black ≥5.39:1 (`--lead`).
- **Performance budget & mobile variant.** Compression: one height
  transition on the header, layout-thrash-free (content below is
  offset by the reserved wrapper, CLS 0). Warmth migrations: §6.9
  costs. Mobile variant: the single-row header above.
- **Tokens consumed (v2).** `--black`, `--paper`, `--lead`, `--amber`,
  `--amber-deep`, `--ease-cast`, `--dur-warm`.

### 6.14 Galley cards

- **What & why.** A listing in this theme is a galley of proofs: each
  card is a short stack of slugs — headline slug, standfirst slugs, a
  figure where the story has one (§6.8 at card scale) — laid in the
  galley tray's grid the way a compositor laid proofs for inspection.
  Cards are not tiles floating over a background; they are output,
  filed in rows, waiting to be read or corrected.
- **Structure.** `<article class="galley-card">`: a tray cell (face
  `--paper-shade` on paper sections, `--metal` on metal; 1px
  `--hairline` rule; 8px padding = 2 sub-grid units) containing 3–5
  slug lines: kicker slug (apparatus, with the card's galley number in
  its notch — "G.14"), headline slug (Zilla 600 20px/28px), up to two
  standfirst slugs (16px/24px local grid), and a meta slug (date,
  lines count, reading time — computed from the card's real text).
  The whole card is one link (headline carries the accessible name;
  the card uses the stretched-link pattern). One card per galley — the
  one nearest the galley's vertical centre — is the dropped slug (§4):
  seated 2px low.
- **Motion spec.** Entry: cards cast with their section (§6.2 applies
  to the galley as one block: the cast front travels card by card,
  left to right, top to bottom, 90ms per card's first line). Hover:
  the card's slugs warm (§6.9) and the card lifts 2px toward the
  reader with its tray shadow deepening 20% over 200ms `--ease-lift` —
  a proof picked up from the tray. Click: §6.10's clunk on the
  headline slug. The dropped slug does not lift on hover — it sits
  low and warms only; its imperfection is permanent, not a state.
- **Choreography timeline (v2).** Section cast: t=0 galley crosses 70%
  → cards cast in reading order, each card's lines staggered 90ms,
  card *k* beginning at t=90×(lines before it) → galley cool completes
  per §6.2's arithmetic. Hover lift: 200ms in, 250ms out (setting a
  proof down is gentler than picking it up).
- **State matrix (v2).** *Rest:* filed in the tray grid. *Hover:* warm
  + lift as specced (desktop). *Focus:* the headline link's outline
  draws around the whole card (the card is the link's visible body);
  warmth follows focus (§6.9). *Active:* §6.10. *Scrolled-past:*
  static. *Disabled:* JS off — cards render filed and cooled; the
  stretched link works. *Visited:* a visited card's notch turns
  `--lead-deep` and gains the apparatus mark "filed" — the reader's
  own output record, stored in the browser's visited state only (no
  tracking store). Touch: no lift; tap is the clunk.
- **Content merge.** The card's slugs are the story's own headline and
  standfirst; its meta counts the story's real lines. A card with its
  animation removed is a complete, honest listing entry.
- **Failure fallback.** Static tray grid (the rest state). Images
  inside cards follow §6.8's broken-image rule: a labelled empty slug.
- **Reduced-motion variant.** Cards arrive filed; hover lift removed;
  warmth instant at reduced intensity (§6.9).
- **Breakpoints (v2).** ≥1200px: 3 cards per row in the measure+tray
  span. 768–1199px: 2 per row. <768px: 1 per row; the dropped slug's
  offset reduces to 1px; card slugs use the 16/24 local grid
  throughout.
- **Edge cases & failure modes (v2).** *Variable standfirst lengths:*
  cards in a row equalise to the row's tallest (the tray is a grid,
  not a masonry) — short cards gain an empty air slug at the base, so
  meta slugs align across the row like baselines in a chase.
  *Missing image:* the figure slug is omitted, never faked; the card
  runs one slug shorter and the row equalises with air. *Long
  headlines:* authored to two slugs maximum (§3); a third line is an
  authoring error the build flags (§15), not a layout the card
  improvises.
- **Accessibility spec (v2).** One link per card with the headline as
  its name; kicker and meta are `aria-hidden` duplicates of data
  available on the story page (galley numbers are apparatus, announced
  via the card's `aria-describedby` only in the index view). Focus
  outline encloses the card at 2px, offset 2px. Lift and warmth are
  decorative.
- **Performance budget & mobile variant.** Entry rides §6.2's shared
  front (no extra loop cost). Hover lift: one transform per card.
  Mobile variant: single column above; cast stagger per card capped
  at 45ms so a 10-card galley finishes its ceremony in ≤2s.
- **Tokens consumed (v2).** `--paper-shade`, `--metal`, `--hairline`,
  `--lead-deep`, `--amber`, `--ease-lift`, `--ease-clunk`, `--slug`.

### 6.15 The casting form

- **What & why.** The theme's conversion moment — subscribe, order,
  enquire — is a casting job: the visitor's details are set as lines
  and cast into a slug the machine keeps. The form is a keyboard and a
  mould: fields are matrix cases (each labelled like a compartment of
  the case), and submitting *casts the line* — the form's contents
  slide together, clunk, and return as a cast slug bearing the
  visitor's own words, filed as the confirmation.
- **Structure.** A single column at 58ch inside a tray frame (§4).
  Each field: apparatus label above ("Name — as it will be cast"),
  input with transparent ground, a 1px `--hairline` bottom rule (the
  slug's edge), Zilla 18px text appearing *on* the line. Required
  fields carry a brass point — a 6px `--amber-deep` square after the
  label — not an asterisk in UI grey. The submit control is the
  **casting lever**: a full-width slug bar, face `--black`, text
  `--paper`, labelled with the plain verb of the site ("Cast my
  subscription"). Success replaces the form with the **cast slug**: a
  slug bar at −2° (the tray angle, §6.3) carrying the confirmation —
  reference number in tabular figures, what was cast, what happens
  next — which the visitor can keep on screen; it is also the content
  of the confirmation email's first line.
- **Motion spec.** Focus: the field's rule inks from `--hairline` to
  `--black` over 200ms and the field's notch fills `--amber-deep` —
  the matrix is selected. Filled: the rule holds at 60% black (a set
  line is darker than an untouched one). Error: the rule turns
  `--amber-deep` and a proof mark appears in the tray margin — an SVG
  circle around the field's number with a ≤5-word note in
  `--amber-deep` Zilla 600 ("Date precedes today"), drawn in
  `--dur-strike` (300ms): a proof mark is struck, not faded. Submit:
  the lever clunks (§6.10, full travel), the form's field slugs slide
  together — gaps close from 28px to 4px over 400ms `--ease-cast`,
  the stack warming to `--amber` 25% — hold while the request sends;
  on success the stack resolves into the single cast slug (fade/slide
  300ms) which cools over `--dur-cool`. On failure the stack re-opens
  (400ms) with the error proof marks applied.
- **Choreography timeline (v2).** Submit: t=0 lever clunk begins →
  t=150ms action fires, slugs begin closing → t=550ms stack closed,
  warm → request resolves at t=r → success: t=r stack resolves to the
  cast slug (300ms), slug cools by t=r+1300ms, focus moves to the
  slug's heading. Failure: t=r stack re-opens (400ms), proof marks
  draw at t=r+200ms staggered 90ms per field.
- **State matrix (v2).** *Rest:* hairlines faint, notches empty.
  *Hover:* fields do not warm (the case is not a slug until filled);
  the lever warms (§6.9). *Focus:* as specced; focus order is field
  order, lever last, and the cast slug's heading receives focus only
  on success. *Active:* lever = §6.10. *Scrolled-past:* n/a.
  *Disabled (submitting):* fields locked, lever face `--lead`, label
  "Casting…" — a real state with real text, not a spinner. Touch:
  inputs at 18px (no iOS zoom), proof marks move beneath their fields
  (a phone tray has no margin).
- **Content merge.** The form is a document of the transaction: its
  fields are the data, its confirmation is the cast slug of that data,
  its errors are proofreader's marks on the visitor's own lines. The
  metaphor never substitutes for the mechanics — validation, labels,
  and submission are a plain working form underneath (§6.15 fallback).
- **Failure fallback.** A plain HTML form: labels, inputs, submit,
  server validation re-rendering the same proof notes as text. No-JS
  visitors lose the casting, keep the transaction. A failed request
  (network) preserves all entries and casts an error slug (§11) above
  the form: "The line did not cast — your words are kept. Try again."
- **Reduced-motion variant.** No slide-together, no clunk travel: the
  lever's state changes instantly, "Casting…" is text, success swaps
  to the cast slug without cooling (it arrives filed).
- **Breakpoints (v2).** ≥1200px: form in the measure, proof marks in
  the tray. 768–1199px: proof marks in a 200px right rail.
  <768px: full-bleed tray frame (side rules drop, top/bottom rules
  remain — a slip torn to width), proof marks beneath fields.
- **Edge cases & failure modes (v2).** *Long input:* fields are single
  lines by design; overflow text scrolls inside the line and the rule
  never wraps — a slug is one line, and multi-line needs use the
  textarea variant (a 3-slug case, ruled at each slug boundary).
  *Autofill:* filled-state rules apply on `change`, so autofilled
  forms read as set, not untouched. *Double submit:* the lever locks
  at first activation (§6.10's idempotence). *Success slug vs. spam
  filters:* the reference number is real (server-issued) or the slug
  carries no number — never a decorative one.
- **Accessibility spec (v2).** Every field has a real `<label>`; the
  brass point is `aria-hidden` beside a visually hidden "(required)".
  Errors are linked via `aria-describedby`, announced once via a
  polite live region ("2 lines need correction"), and persist until
  corrected — errors never time out on a printed form or a cast one.
  The cast slug's heading is focusable (`tabindex="-1"`) for the
  success focus move. Contrast: error notes `--amber-deep` on paper
  5.45:1 at 14px semibold minimum.
- **Performance budget & mobile variant.** Submit sequence: transforms
  on ≤8 field slugs, ≤0.4ms/frame for ≤1s. No loops. Mobile variant:
  the torn-slip frame above.
- **Tokens consumed (v2).** `--black`, `--paper`, `--hairline`,
  `--amber`, `--amber-deep`, `--lead`, `--ease-cast`, `--ease-clunk`,
  `--dur-strike`, `--dur-cool`, `--slug`.

---

### 6.16 The foundry footer

- **What & why.** The footer is the machine room's back wall: the belt-
  and-pulley drawing (§6.7), the 90-key keyboard at full size (§6.11's
  home), and the colophon — what the page was set in, on what, by whom,
  and the final tally: "This page set N lines · M words cast". A footer
  that reports the page's own manufacture is the theme's closing proof
  that the paper was real all along.
- **Structure.** On `--black`, three bands: (1) the machine band —
  §6.7's SVG left, colophon text right (apparatus + caption in
  `--lead`/`--paper`): faces used, the slug unit, the edition line
  ("Set on the Linotype Line · Slug № per page"), legal line, and 2–3
  text links with §6.9 warmth and a drawn rule on hover. (2) The
  keyboard band — §6.11 at full size, static. (3) The tally band —
  "lines set: N · words cast: M · sections filed: K" in tabular Zilla
  500 20px, the numbers computed from the page's real DOM (the static
  text equivalent of §6.4's counters, and their accessible home).
- **Motion spec.** The machine band draws per §6.7. The tally counts
  up once as the footer enters — each number rolling over 900ms
  `--ease-cool` to its true value (they are the page's final figures;
  §6.4's live counter has been approximating them all along and lands
  exactly). Links: rule draws left→right 200ms on hover. Nothing else
  moves; the end of the page is its coolest, quietest part.
- **Choreography timeline (v2).** t=0 footer crosses 60% → §6.7's draw
  begins → t=300ms tally roll begins (all three numbers together, one
  machine settling its accounts) → t=1200ms tally landed → draw
  completes ≈t=1020ms, rotation fades in by t=2000ms (§6.7). The
  pinned keyboard band (§6.11) has released before any of this — the
  footer never shares the screen with its own preview.
- **State matrix (v2).** *Rest:* drawn machine, landed tally, static
  keyboard. *Hover:* links warm + rule; pulleys slow (§6.7).
  *Focus:* standard outlines (`--amber` on black). *Active:* links
  press 1px. *Scrolled-past:* n/a — it is the end. *Disabled:* JS off
  — tally shows build-time true figures; machine drawn; all links
  live. Touch: identical minus hover.
- **Content merge.** Every footer element is the page's own record:
  the machine that cast it, the keyboard that set it, the count of
  what it made. A footer link that leaves the foundry (social, legal)
  is set as a slug line like everything else — no alien icon row.
- **Failure fallback.** Static bands; tally from build-time data. If
  runtime counting fails, the tally band shows the build-time figures
  (never blanks, never zeros — a footer that reports "0 lines set" is
  lying about a page the visitor just read).
- **Reduced-motion variant.** Tally lands instantly; machine still;
  link rules instant.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: machine band
  stacks (SVG above colophon). <768px: keyboard band shows 60 caps
  (§6.11's mobile bank rule); tally wraps to two lines, tabular
  alignment kept.
- **Edge cases & failure modes (v2).** *Counts vs. §6.4:* the footer's
  figures must equal the header counter's final values exactly; a
  mismatch is a §10 failure (the machine's books must balance).
  *Multi-page sites:* the tally is per page, labelled as such ("This
  page set…"), never a site-wide vanity total.
- **Accessibility spec (v2).** The tally band is the counters'
  accessible home: plain text, read once. Footer nav labelled
  distinctly from §6.13's. Contrast on black: `--paper` 14.63:1,
  `--lead` 5.39:1 (apparatus ≥12px semibold only), link rules are
  graphics at ≥3:1.
- **Performance budget & mobile variant.** The tally roll is three
  text updates on the shared loop for 900ms: negligible. Everything
  else is §6.7/§6.11's budgets. Mobile variant: the stacked bands
  above.
- **Tokens consumed (v2).** `--black`, `--paper`, `--lead`, `--amber`,
  `--ease-cool`, `--dur-draw`.

### 6.17 Slug-stack tables and data

- **What & why.** Tables are where editorial themes usually surrender
  to generic UI. Here a table is a stack of slugs in a chase: each row
  a bar, the header row a fat slug reversed out of foundry black, the
  numbers set in tabular slab figures. Data presented as cast lines
  keeps the theme's physics — rows can be warmed, counted, and filed —
  without pretending a spreadsheet is a story.
- **Structure.** A real `<table>`: caption set as a headline slug;
  `<thead>` row as a reversed slug (face `--black`, text `--paper`,
  apparatus 12px uppercase); body rows as slug bars (face alternating
  `--paper` / `--paper-shade` — the alternation is the bars' edges,
  not zebra decoration: each row keeps its notch, numbered in section
  order); numeric cells right-aligned tabular; a `<tfoot>` tally row
  in `--lead-ink` semibold whose totals are the column's real sums
  where sums are meaningful, and absent where they are not.
- **Motion spec.** Tables cast with their section (§6.2's front
  travels row by row, 45ms per row — rows are half a text line's
  ceremony). Row hover warms the row's slug (§6.9). Sortable columns
  (where the product sorts): on sort, rows re-file — a 180ms
  `--ease-cast` crossfade as the stack reorders, and the sorted
  column's header notch fills `--amber-deep`. No FLIP acrobatics: a
  chase is re-set, not juggled.
- **Choreography timeline (v2).** Section cast: rows at t=45×(r−1),
  cool per row +1000ms. Sort: t=0 header clunks (§6.10 at apparatus
  scale) → t=0–180ms rows crossfade → t=180ms new order filed, notch
  filled. The "lines set" counter (§6.4) counts table rows as lines —
  they are.
- **State matrix (v2).** *Rest:* filed stack. *Hover:* row warmth.
  *Focus:* sortable headers are real `<button>`s with standard
  outlines; cell focus n/a. *Active:* header clunk. *Scrolled-past:*
  static. *Disabled:* JS off — the table is a table; sorting degrades
  to server-side links in the headers. Touch: no row warmth; sort
  identical.
- **Content merge.** The rows are the data; the slug treatment is
  their presentation as the page's cast output. Row counts feed the
  page tally (§6.16) honestly.
- **Failure fallback.** Plain table, all states CSS. A table too wide
  for its measure scrolls inside a tray-framed region with the notch
  column sticky — the chase holds the rows; the page never breaks
  its measure for a table.
- **Reduced-motion variant.** Rows arrive filed; sort is an instant
  reorder with the notch fill instant.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: secondary
  columns may hide behind a "full table" slug toggle (a real button
  that expands the chase) — columns are never silently dropped.
  <768px: tables with >4 columns switch to slug cards (each row a
  §6.14-style card of label:value slugs) — the data survives
  re-composition; it is never squeezed into illegibility.
- **Edge cases & failure modes (v2).** *Long tables (>40 rows):*
  cast ceremony caps at the first 12 rows; the rest arrive filed
  (§6.12's cap logic). Pagination, where present, is §11's galley
  folios. *Empty cells:* an em-dash slug space — never a blank that
  reads as a rendering bug. *Totals that don't apply:* the tfoot is
  omitted; a tally row with nothing to tally is a lie of form.
- **Accessibility spec (v2).** Real table semantics throughout
  (`th scope`, caption); sort state via `aria-sort`; the reversed
  header's contrast is 14.63:1. The mobile card transformation keeps
  label:value pairing in the accessibility tree (it is a re-layout,
  not a semantics change).
- **Performance budget & mobile variant.** Row casting rides §6.2's
  front. Sort crossfade: one opacity pass on ≤40 rows, ≤0.4ms/frame
  for 180ms. Mobile variant: the card transformation above.
- **Tokens consumed (v2).** `--black`, `--paper`, `--paper-shade`,
  `--lead-ink`, `--amber-deep`, `--ease-cast`, `--slug`.

### 6.18 The empty galley — 404 and empty states

- **What & why.** A page that cannot be found is, in this theme, a
  galley with no slugs in it: the tray is there, ruled and ready, and
  it is empty — with one slug lying on the floor beneath it, the
  page that fell. Empty states (no results, no filings) use the same
  image at smaller scale. The theme's saddest furniture, played
  straight: no mascot, no pun in the headline — the compositor's
  honesty extends to absence.
- **Structure.** Centred in the measure: a tray outline (2px `--black`
  rules, `--paper-shade` face) at full measure width, 3 slugs tall,
  empty; beneath it, one slug bar at −2° on the page ground carrying
  the lost page's would-be headline slug: "The page you asked for was
  never cast." Below: the recovery slugs — links home, to the galley
  index (§6.13), and to search (§11) — as three warm-ready slug bars.
  For in-page empty states, the same composition at the container's
  width with the container's own sentence ("No filings match that
  name — the tray is empty.").
- **Motion spec.** On load, the fallen slug casts once (§6.1's rite at
  body scale: slide + cool, 400ms + 1000ms) and settles at −2° — the
  page performs its one small accident, then stillness. The empty
  tray does not shimmer (nothing is fresh here; §6.6 stays home). The
  recovery slugs warm on hover (§6.9) and clunk on click (§6.10).
- **Choreography timeline (v2).** t=0 page painted, tray empty →
  t=200ms the fallen slug casts from the tray's left edge → t=600ms
  seated at −2° → t=1600ms cooled. Recovery slugs cast in at t=300ms
  staggered 90ms, filed warm-ready. Total ceremony ≈1.6s, once.
- **State matrix (v2).** *Rest:* the composed absence. *Hover/focus:*
  recovery slugs per §6.9/§6.10. *Active:* clunk. *Scrolled-past:*
  n/a (the state fills its page). *Disabled:* JS off — everything
  present and cooled from first paint; the links work. Touch:
  identical.
- **Content merge.** The empty tray is the site's real furniture
  (§6.14's galley) with its contents genuinely absent; the fallen
  slug carries the explanation as a cast line. Nothing is illustrated
  that the page doesn't mean.
- **Failure fallback.** The static composition *is* the fallback. A
  404 that fails to render its theme still returns the correct status
  and the three recovery links as plain text — the build's server
  template guarantees the links exist outside the themed layer.
- **Reduced-motion variant.** Fallen slug pre-cast and cooled at −2°;
  recovery slugs filed. Identical words, identical links.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced.
  <768px: tray narrows to the measure; fallen slug's angle reduces to
  −1° (§6.3's small-screen rule); recovery slugs stack full-width.
- **Edge cases & failure modes (v2).** *Search with zero results:*
  the empty state names the query ("No filings match 'mercantile' —
  the tray is empty.") and offers the cleared search as the first
  recovery slug. *Genuinely empty collections* (a new archive): the
  sentence is prospective ("Nothing has been filed here yet — the
  tray is ready.") and the recovery slug is the contribution action.
  The wording difference matters: absence-by-accident and
  absence-by-youth are different states (§12).
- **Accessibility spec (v2).** The 404 page's `<h1>` is the fallen
  slug's sentence — the explanation is the headline, not a caption to
  an illustration. The tray outline is decorative (`aria-hidden`).
  Recovery links have full descriptive names ("Back to the front
  page", not "Home"). Status codes are correct (404/200 as
  applicable) — theming never fakes a status.
- **Performance budget & mobile variant.** One cast + three slug
  casts: the cheapest page on the site. Mobile variant: above.
- **Tokens consumed (v2).** `--paper-shade`, `--black`, `--paper`,
  `--amber`, `--ease-cast`, `--dur-cool`, `--slug`.

---

## 7. Page application map

**Home.** The full ceremony: §6.1 hero cast, chapters casting per
§6.2, one quotes chapter with tray lifts (§6.3), the keyboard pinning
through the middle chapters (§6.11), the etaoin line in the midpoint
chapter (§6.5), closing with the machine footer (§6.16). The home page
is the machine's showroom shift — every element appears, each once, in
casting order.

**Listing / archive (the galley).** §6.14 cards in tray grids;
§6.17 tables where the listing is data-shaped (issue indexes,
specimen lists). The galley tray (§6.4) counts *stories filed* as well
as lines on this page type — the header counter's label changes to
"filed: n" (same mechanism, honest label). Filters, where present,
are §11's chapter tabs: changing a filter re-files the galley (cards
crossfade per §6.17's sort rule), never re-casts it — the stories
exist; only their order is compositor's work.

**Detail / article (the long read).** The purest form: one measure,
chapters of pure §6.2 casting, tray quotes (§6.3) where the article
earns them, figures as §6.8 slug frames, the keyboard pinning through
the middle (§6.11). The lines-set counter is this page type's reason
to exist — a 2,000-line investigation should *feel* like 2,000 lines
of metal. End mark: the article closes with a filed slug bearing
"■ — end of the line" and the article's own tally (§6.16 at article
scale).

**About (the foundry).** The one page type allowed a second machine
drawing: the works' own history set as chapters, portraits as §6.8
frames with founders' names reversed in their notches, a §6.17 table
for the timeline (dates cast as rows). Warmth ration relaxes nowhere —
heritage is not a licence for amber wallpaper (§9).

**Contact / order / subscribe (the casting).** §6.15 is the page: a
short standfirst cast per §6.2, the form, and nothing else competing.
Checkout equivalents keep the form's rite and drop the keyboard pin
(transactions do not pin ornaments over payment fields — §1).

**404 / empty.** §6.18, whole page or in-container.

**Search results.** A listing (§6.14) whose headline slug is the
query, cast verbatim — "Results for 'mercantile'" is a line the
visitor dictated to the machine. Zero results: §6.18's named-query
variant.

---

## 8. Worked examples

### 8.1 The hero — "The Gazette, set live" (home)

**The build.** A journalism-history quarterly's home hero. Fraunces
Display 1 in three authored slug lines — "Every line / on this page /
was cast for you." — over a paper section; beneath, a standfirst of
three body slugs and one apparatus line ("Est. 1886 · Set nightly ·
No. 214"). The header tray (§6.4) starts empty; its slots rule the
page's six sections.

**Scroll/load timeline.** t=0 first paint: all hero lines present in
final type (the no-JS state), JS arms the cast. t≈120ms (fonts ready)
line 1 slides from the mould mask, 400ms `--ease-cast`, face hot.
t=240ms line 2 begins; t=360ms line 3. t=520ms line 1 seated, cooling
since t=520 on `--ease-cool`. t=910ms line 3 seated; the standfirst's
first slug casts at t=1060ms, its lines at 90ms stagger. t≈1520ms all
headline slugs cooled; t≈2260ms standfirst fully cool; the shimmer
(§6.6) takes up residence on the standfirst's last line. The visitor
has watched the page's promise be manufactured in ≈2.3s, and the tray
already holds its first chip when §1's section completes below.

**What the builder checks.** Line breaks are the author's at 360px,
768px, and 1440px (Display 1 is re-authored per breakpoint band, §3);
the hottest frame's text contrast ≥7:1; the 1.2s watchdog armed.

### 8.2 Mid-page — the quotes chapter (detail page)

**The build.** Chapter 3 of a long read on Mergenthaler: six paragraphs
of body casting (§6.2), two pull-quotes whose home lines sit in
paragraphs 2 and 5 ("The machine did not replace the compositor; it
promoted him." / "A line o' type is a sentence that has been to the
foundry."), the tray (§6.3) ruled and waiting at the chapter's right.

**Scroll timeline.** Visitor scrolls at reading pace. Paragraph 1
crosses 70%: its 7 lines cast front-down, cool trailing; tally ticks 7.
Paragraph 2 crosses: as its quote line's glow begins, the tray slug —
same sentence — begins its 60vh scrub: rising 46px, tilt settling
−4.5°→−2°, as the home line passes 85%→25% of the viewport. The slug
files, cools; §6.6's shimmer moves to paragraph 3's first line as it
casts. Paragraph 5's quote repeats the rite; the tray now holds two
slugs at −2°, a small archive of the chapter's best metal. Scrolling
back up: both slugs stay filed (output is not un-cast); scrolling
down fast past the chapter: both land filed, cool, unperformed
(§6.3's jump rule).

**What the builder checks.** Tray quotes match home lines verbatim
(gate 6); lifts never overlap; the chapter's chip deposits in §6.4
only after paragraph 6 cools.

### 8.3 Conversion — "Cast my subscription" (subscribe page)

**The build.** §6.15's form for the quarterly's print subscription:
three fields (name, address line, email), the casting lever, a price
table (§6.17, 3 rows: Quarterly / Annual / Foundry patron) above the
form in the measure. The page's one chapter; no keyboard pin (§7).

**Scroll/interaction timeline.** Load: headline slug casts (§6.1 at
H3 scale), price rows cast at 45ms stagger as the table crosses 70%.
The visitor tabs: Name field's rule inks, notch fills `--amber-deep`.
Types; rule holds at 60%. Email entered malformed; on blur, the proof
mark draws (300ms) in the tray rail: circled field number, note
"Address wants its @" — five words, proofreader's grammar (§12).
Corrected; the mark stays until the field validates on submit
(errors persist, §6.15). Submit: lever clunks (t=0–150ms, action
fires), field slugs close 28px→4px gaps by t=550ms, stack warm; the
request resolves at t≈900ms; the stack resolves into the cast slug at
−2°: "Cast. Subscription № 0417 — Annual, to A. Rahman. First issue
posted Friday." Focus lands on the slug's heading; the slug cools by
t≈2200ms. The galley tray gains the page's final chip: the conversion
was the last section, and the machine's tally (§6.16 pattern, inline)
reads "This page set 41 lines · 1 subscription cast."

**What the builder checks.** The form works end-to-end with JS off
(server proof notes as text); the reference number is server-issued;
the success slug's facts match the submitted data exactly.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Amber everywhere.** Heat as a brand colour: amber buttons, amber
   links, a warm amber wash over whole sections. *Cure:* the one law
   (§1) and §10 gate 5 — at rest, ≤2% amber pixels, all of it attached
   to a line that earned it.
2. **Shimmer on everything.** A page where every slug wobbles is a
   page of jelly, not metal. *Cure:* one shimmer, on the freshest
   slug, by construction (§6.6). If a design shows two, it fails
   review on sight.
3. **Gibberish reversed type.** Notches filled with random letters or
   lorem sorts. *Cure:* the notch carries the line's own first sorts,
   reversed (§4). It costs nothing — the text is already there.
4. **Slug bars as zebra striping.** Alternating row colours with no
   notches, no edges, no casting — a table skin wearing the theme's
   name. *Cure:* a bar without the §4 anatomy (notch, face, edge,
   air) is not a slug; §6.17's tables keep the anatomy at data scale.
5. **Unreadable mid-glow text.** Cooling gradients applied to the
   *type* instead of the face, so lines pass through 2:1 contrast on
   their way to rest. *Cure:* heat lives behind the type (§4, §6.1);
   contrast is specified at the hottest frame, not the coolest.
6. **Etaoin as a sticker.** The error line in the footer, in the logo,
   three times a page, winking. *Cure:* once per page, in the margin,
   struck, with its note (§6.5). It is a ritual, not a mascot.
7. **A QWERTY keyboard.** The footer ornament drawn as a generic
   keyboard because the real layout was research. *Cure:* the 90-key
   ETAOIN SHRDLU arrangement is content (§6.11); a build with QWERTY
   has drawn a different machine.
8. **Invented counters.** "Lines set: 10,000" as a marketing figure,
   or counts that don't match the DOM. *Cure:* every number is
   measured (§6.4, §6.16); the two tallies must balance (gate 4).
9. **Tray quotes that aren't quotes.** Pull-slugs whose text appears
   nowhere in the column — marketing copy smuggled into the margin.
   *Cure:* verbatim or nothing (gate 6).
10. **Random angles.** Tray slugs at −2°, −5°, +3° "for energy".
    *Cure:* −2°, one direction, always (§4). A compositor's habit is
    a system; random rotation is a screensaver.
11. **Casting everything, always.** Hero, cards, tables, footer text,
    legal lines all performing the full glow on every page — the
    ceremony becomes wallpaper and the reader stops seeing it.
    *Cure:* ceremony is rationed by page type (§7): the long read
    casts lines; the checkout casts almost nothing until its lever.
12. **The dropped slug multiplied.** One licensed imperfection per
    galley (§6.14) becomes five "for character". *Cure:* one. A tray
    of dropped slugs is a spilled tray.

---

## 10. Quality gate

A build may not ship in this theme until every **blocking** item
passes and at least 8 of the 10 **standard** items pass. The reviewer
checks evidence — a JS-off load, a screenshot at rest, the DOM — not
intentions.

**Blocking — all must pass.**
1. **JS-off test:** with JavaScript disabled, every page shows all
   content cooled and complete; the etaoin line is present and struck;
   the form submits; the tray shows the true full counts.
2. **Fallback test:** with animation triggers broken, the 1.2s law
   fires per section and no line remains hot, masked, or parked.
3. **Reduced-motion test:** with `prefers-reduced-motion`, no element
   travels, shimmers, dips, or rolls; the pre-cooled page carries
   identical information, including the "fresh" mark (§6.6).
4. **Truth audit:** "lines set", "words cast", tray chips, and the
   footer tally are DOM-derived and mutually consistent; one invented
   or mismatched figure fails the build.
5. **Heat audit:** a full-page screenshot at rest measures ≤2% amber
   pixels, and every amber region touches a line that cast, is
   hovered/focused, or is the current nav slug (§6.13).
6. **Tray audit:** every tray slug's text appears verbatim in the
   column; every tray slug sits at −2.0° ± 0.1°.
7. **Etaoin audit:** exactly one error line per page, in its chapter's
   margin (or its in-column equivalent), struck in `--amber-deep`,
   with its note — and the keyboard, wherever drawn, is the 90-key
   ETAOIN SHRDLU layout.
8. **Cursor & cover audit:** system cursor unchanged everywhere; the
   pinned keyboard and tray never overlap reading text at any scroll
   position (checked at 5 depths, 3 breakpoints).

**Standard — at least 8 of 10.**
9. Cast arithmetic: hero fully cool ≤2.3s; a 6-line paragraph ≤1.6s;
   no page performs more than 2 concurrent casts.
10. One shared rAF loop (lerp 0.12) drives scrub, parallax, counters,
    and shimmer transfer; no frame over 20ms attributable to theme
    code on a mid-range Android during a full-page scroll.
11. Contrast at the hottest frame: body text ≥7:1 on its face at every
    point of every cooling curve.
12. Counters tabular, upward only, landing exactly; the header tally
    and footer tally agree to the line.
13. The form works fully without JS; proof-mark errors persist until
    corrected and are announced once; the success slug's facts match
    the submitted data.
14. Type discipline: Display 1 once per page; no auto-wrapped slug
    headlines; no Zilla italic used for emphasis anywhere.
15. Dark mode: the sheet's tokens are mode-invariant; only the room
    darkens; the lamp tint is present and ≤4% amber.
16. The skeleton never appears for content arriving within 200ms;
    skeleton bars match the real layout's slug counts.
17. Print stylesheet: `@media print` removes shimmer, sheen, pins,
    and overlays; every line prints cooled on paper — the proof that
    the slugs were text all along.
18. The five-second test: a first-time viewer describes the page as
    "being printed, line by line" — not "retro", not "steampunk",
    not "a newspaper theme".

**Minimum bar, in one line:** a build that passes the blocking eight
has earned the right to be judged on premiumness; anything less is a
striped page with a keyboard sticker, and it goes back to the foundry.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed as slugs do **not** warm or clunk — the machine's
rites belong to its lines (§6.9, §6.10).

- **Buttons (primary).** The casting lever (§6.15): `--black` slug bar,
  `--paper` label, clunk on activation. One per view.
- **Buttons (secondary).** Filed slugs: `--lead` face at 30% over
  paper, `--black` label; warm on hover, clunk on click.
- **Text inputs.** §6.15's matrix-case fields: label above, hairline
  rule, notch fills on focus.
- **Textarea.** The 3-slug case: ruled at each 28px boundary, text
  flows across rules like copy on a galley.
- **Selects.** A filed-slug control opening a tray list (options as
  slug rows, §6.17 row treatment); the chosen option's notch fills
  `--amber-deep`.
- **Checkboxes & radios.** Proof ticks: a 16px square case; checked =
  the §6.5 strike-style tick drawn in `--amber-deep` (two strokes,
  200ms). Radios are round matrices — a filled brass centre, drawn
  not faded.
- **Tables.** §6.17 slug-stack tables, complete.
- **Badges.** Slug-end stamps: a 22px notch segment carrying the
  badge text reversed (status as a casting mark — "FILED", "No. 214").
  Badges never use amber unless the status is *fresh* (§6.6's mark).
- **Alerts.** Cast error/success slugs (§6.12, §6.15): a full-width
  slug at the tray angle's 0° (alerts sit straight — urgency is not
  filed casually), face `--paper-shade`, left notch in `--amber-deep`
  (error) or `--black` (notice), the message as a real slug line, a
  dismissal clunk where dismissal is allowed.
- **Pagination.** Galley folios: previous/next slugs and numbered
  folio slugs (46px, notch-numbered); the current folio is filed warm
  at §6.13's standing 12%.
- **Modals.** The inspection plate: a centred `--black` plate (the
  machine's inspection hatch) with the content set as paper slugs
  inside it; opens with a 200ms `--ease-cast` rise of 8px — the plate
  is lifted, never zoomed. Focus trapped; escape closes with the
  clunk.
- **Toasts.** Fresh-line notices: a single slug slides from the
  header tray's right end (§6.12's cast at apparatus scale), cools,
  and files itself after 5s or on dismissal. Maximum one at a time —
  the machine casts one line at a time.
- **Tabs.** Chapter tabs: slug ends in a row, the active tab filed
  warm (12% standing warmth, §6.13); switching re-files the panel
  (§6.17's crossfade), never re-casts it.
- **Accordions.** Folding galleys: the header slug stays; the body
  slugs unfold by height over 300ms `--ease-cast`, casting their
  first lines as they open if never opened before.
- **Search.** The magazine search: an input styled as §6.15's field
  with a "Cast the query" lever; results are a §7 listing whose
  headline slug is the query verbatim.
- **Progress (task-level).** §6.4's tray; long operations (uploads,
  exports) report as "casting: n of m lines" with a tray of their
  own in the modal plate.
- **Tooltips.** Operator's notes: apparatus text on a `--black` chip,
  appearing after 600ms hover/focus, naming the thing's machine truth
  ("E — 1st, 12.7% of English", §6.11).
- **Dividers.** Leading strips: a 1-slug air gap with a centred
  hairline and, at chapter breaks, a 2px `--black` rule with a single
  reversed sort (❦ refused — ornaments are type here: the divider's
  sort is the chapter's number).
- **Breadcrumbs.** A filed trail: ancestor slugs at 60% size, cooled,
  separated by notch slashes; the current page is the warm slug.
- **Avatars / bylines.** The compositor's mark: initials reversed in a
  28px notch square beside the name slug. No photographs in circles —
  a byline is a slug, not a sticker.
- **Cards.** §6.14 galley cards, complete.
- **Forms.** §6.15, complete.
- **Navigation.** §6.13, complete.
- **Footer.** §6.16, complete.
- **Loader / empty states.** §6.12 and §6.18, complete.

---

## 12. Content & copywriting voice

**The register.** The compositor's voice: plain, mechanical, proud of
the work, incapable of hype. Sentences are set like lines — one idea
per line, no line longer than the measure. The machine never says
"revolutionary"; it says what it cast, how many lines, and when.

- **Headlines** are statements of fact with a foundry's confidence:
  ✓ "Every line on this page was cast for you." ✗ "Experience the
  magic of AI-powered content synergy!" Headline case is sentence
  case; the machine shouts only on the etaoin line, and even that is
  lowercase.
- **Labels** name the machine's real parts and the visitor's real
  acts: ✓ "Cast my subscription", "Lines set", "Filed under".
  ✗ "Let's go!", "Submit", "Yay, you're in!". The verb is the trade's
  verb or the plain verb — never a growth-hack verb.
- **Buttons** say what will be cast or filed: ✓ "Cast the line",
  "File this section". ✗ "Click here".
- **Error messages** are the proofreader's corrections — brief,
  specific, in the margin: ✓ "Address wants its @" / "Date precedes
  today". ✗ "Oops! Something went wrong :(" — the proofreader does
  not say oops, and nothing in this theme has a face.
- **Empty states** are §6.18's two sentences, kept distinct:
  absence-by-accident ("The page you asked for was never cast.") vs.
  absence-by-youth ("Nothing has been filed here yet — the tray is
  ready."). Never "Nothing here but us chickens".
- **Success** is a colophon, not a celebration: ✓ "Cast. Subscription
  № 0417 — Annual. First issue posted Friday." — what, which, when.
  ✗ confetti, exclamation, "Welcome aboard!!".
- **Numbers** are always real and always tabular (§3): lines, words,
  sections, dates, prices. A number the machine didn't count does not
  appear.
- **Banned words:** "magic", "seamless", "supercharge", "leverage"
  (verb), "oops", "just" (as a minimiser), and any exclamation mark
  outside a genuinely quoted line. **Owned words:** cast, set, file,
  slug, galley, tray, proof, line — used literally, never as puns in
  headlines more than once per page.

---

## 13. Full-page scroll choreography map

The home page, top to footer, in order. (Other page types per §7 keep
the same beats for the elements they carry.)

1. **Load.** Header tray empty, slots ruled (§6.4). Hero slugs parked
   in final type; JS arms the cast.
2. **Hero cast** (§6.1): lines slide and cool in casting order ≈2.3s;
   standfirst follows; shimmer settles on the last standfirst line.
   *Feel: the page is being made for you, now.*
3. **Chapter 1 casts** (§6.2): the cast front travels down the first
   section; the tally ticks per line; the chapter's chip deposits in
   the tray, warm, and cools.
4. **First figure** (§6.8): the plate scale-settles and cools as it
   centres; its caption casts.
5. **Keyboard rises** (§6.11): entering chapter 2, the band pins to
   the viewport foot; caps begin dipping per cast line. *Feel: the
   machine's hands are under the work.*
6. **Quotes chapter** (§6.3 + §8.2): two tray lifts, serialised; the
   tray accumulates the page's best lines at −2°.
7. **The error** (§6.5): at the midpoint chapter, "etaoin shrdlu"
   types in the margin — the keyboard band dips E-T-A-O-I-N in
   sequence — and the proofreader strikes it. The page's one held
   breath.
8. **Metal section**: a dark chapter; the oil sheen (§6.6) drifts;
   slugs cast on `--metal` faces; amber reads hotter here and is
   rationed harder (gate 5 is measured per section, not per page).
9. **Galley** (§6.14): the listing chapter casts card by card; the
   dropped slug sits its 2px low, unremarked.
10. **The casting** (§6.15 or its home-page form): the conversion,
    played per §8.3 when the visitor acts; untouched, it simply
    waits, filed and cool — the page does not nag.
11. **Release.** The keyboard band fades as the footer approaches;
    the machine band (§6.7) draws itself; the tally (§6.16) rolls
    and lands on the page's true figures. *Feel: the shift ends; the
    books balance.*
12. **Rest.** A finished page is a cool page: shimmer retired,
    sheen paused off-screen, every slug filed. Stillness is the last
    beat, and it is composed, not empty.

**Catch-up law.** At any scroll velocity, beats land in this order or
land instantly in their end states — never out of order, never
half-performed (§6.2, §6.3). The choreography serves the reading; the
reading never waits for the choreography.

---

## 14. Whole-page performance budget

**Asset ceilings (home page, compressed):** HTML ≤ 60KB · CSS ≤ 38KB ·
JS ≤ 30KB gz (the theme needs one loop, one observer, and arithmetic —
a Linotype page shipping 300KB of JS has misunderstood its machine) ·
fonts ≤ 120KB total (Zilla Slab 400/500/600 + Fraunces opsz variable,
subset, `font-display: swap` with the §6.1 font gate) · images per
§6.8, responsive, ≤ 900KB per page all-in.

**Frame budget.** The shared loop's per-frame theme cost ≤ 1.2ms
(sum of §6 budgets: cast overlays ≤0.3, scrub ≤0.2, shimmer ≤0.5,
counters ≤0.1, dips ≤0.1). No frame over 20ms attributable to theme
code during a full-page scroll on a mid-range Android. Long tasks:
none over 50ms; line measurement (§6.2) runs once per block at layout
and is cached — never per frame.

**CLS / LCP.** CLS ≤ 0.02: slug anatomy is reserved space; the header
compresses inside its reserved wrapper (§6.13); skeleton bars match
real slug counts (§6.12). LCP ≤ 2.0s on 4G: the hero's first line is
server-rendered in final type — the cast is an enhancement of a
painted page, never its gate.

**Cut order** (when the budget is exceeded, cut in this order; the
casting itself is never cut):
1. The oil sheen (§6.6).
2. The shimmer's SVG displacement → glow-pulse fallback (§6.6).
3. Notch-rail parallax (§5).
4. The keyboard's per-line cap dips (§6.11) — the pin stays.
5. Cooling gradient steps 5 → 3 (§6.1).
6. The belt-and-pulley's rotation (the draw stays; §6.7).
**Never cut:** casting order and stagger, the etaoin line, any
counter's truth, any fallback, the reduced-motion variants.

---

## 15. Build-order checklist

1. Tokens first: §2's palette (anchors + derived), §5's easings and
   durations, `--slug` — one source of truth, no magic numbers
   downstream.
2. The static page: full content, cooled, complete with JS disabled —
   and passing gates 1, 4, 6, 7 in that state before any motion
   exists. (The theme is built filed and warmed up, never the reverse.)
3. Slug anatomy (§4): notch, face, edge, air — as one component, used
   by every element; per-element bar hacks are refused in review.
4. Baseline grid lock: body blocks measured against the 28px grid;
   the §6.2 line-count measurement, cached.
5. Header: nameplate + tray (§6.13, §6.4) with build-time true counts
   in the no-JS state.
6. Casting engine: the shared rAF loop (lerp 0.12), the cast front,
   the 1.2s watchdog — §6.2, then §6.1 as its special case.
7. Counters wired to the engine (§6.4); footer tally reconciled
   (gate 4's balance check in the test suite).
8. Tray lifts (§6.3) with the verbatim-quote check as a build-time
   lint: tray texts are extracted from the column, never re-typed.
9. The etaoin line (§6.5) + keyboard (§6.11) with the ETAOIN SHRDLU
   layout verified against the reference arrangement; QWERTY anywhere
   fails the build.
10. Ambient layer (§6.6) with its fps-shedding and `save-data` gates.
11. Images (§6.8), tables (§6.17), cards (§6.14) — the content
    families, in that order.
12. The casting form (§6.15) end-to-end without JS; then its motion.
13. Skeleton + transitions (§6.12), 404/empty (§6.18), footer (§6.16).
14. Reduced-motion pass: every element's variant exercised, not
    assumed; dark-mode room check (§2).
15. The gate (§10) run as a checklist with evidence attached —
    screenshots at rest for gate 5, a JS-off capture for gate 1, the
    tally reconciliation for gate 4 — before the theme is used in a
    build.
