# 50. Charcoal & Ink — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** Shou-sugi-ban charred cedar meets sumi-e ink wash:
blackened wood surfaces, and content painted onto the page with a
brush that occasionally runs dry. Palette anchors: charcoal
`#121110`, char grain `#2E2A26`, ash edge `#6E6259`, washi
`#F4EFE6`, hanko red `#A62B25`. Type: Zen Old Mincho (display) +
Noto Sans JP (body). The page alternates charred-wood panels —
alligator-scale char cracks — with washi content sheets; every
section opens with a single brush-stroke divider; images are
revealed through ink-bleed feathered edges, never clean rectangles;
a margin ink stick grinds down as the visitor reads.

## 1. Concept & world

Charcoal & Ink is the website of a single hand. Its two materials
are both made by destroying something gently: cedar is burned until
its surface turns to alligator-scale char — black, cracked, and
more durable than the raw wood ever was — and sumi ink is made by
grinding a solid stick of soot and glue against a stone with water,
spending the stick to make the mark. The page holds both facts at
once. Its dark surfaces are not "dark mode"; they are *burnt wood*,
with a crack field you could count. Its light surfaces are not
"cards"; they are *sheets of washi* laid over the char, and
everything printed on them was put there by a brush — which means
some of it is wet, some of it is dry, and the difference is
information.

The world the page performs is the calligrapher's studio at the end
of a working day. The headline was brushed this morning and has
dried. The dividers are painted as you arrive at each section, by
your own scrolling hand. The long showcase stroke is drawn by your
scroll across 200vh — your pace is the brush's pace, and the stroke
is wetter when you move slowly, drier when you fling. Down the
margin, the ink stick that is writing the page is visibly consumed
by the reading: the further you read, the shorter it gets, and the
inkwell beneath it darkens with ground ink. When you choose
something — a work, a size, a date — you do not tick a box; you
stamp it with the red hanko, and the stamp stays on the item for
the rest of the session, rotated a degree or two off true, one
corner over-inked, because a hand pressed it.

**The theme's one law: ink is spent, never sprinkled.** Every mark
on the page is one of exactly three kinds, and the quality gate
audits all three. (1) *Drawn marks* are drawn by an act — the
visitor's scroll paints the dividers and the long stroke, their
click stamps the hanko, a completed count fills a brush numeral.
(2) *Printed marks* ship already dry: anything the animation would
have drawn exists in the DOM in its finished state, so the page
with JavaScript disabled is the same page, merely unperformed.
(3) *Dry marks* — the scratchy, broken strokes where the brush ran
out — are rationed to mean scarcity, and the ration is exact: **at
most one dry passage per section, always at the point where the
content itself runs thin** (the last character of the headline,
the final short paragraph of a sheet, the one unavailable size in
a list). A dry stroke anywhere else — decoration dryness, random
scratchiness applied for texture — is a gate failure, because in
this world a dry brush is a sentence about the content, and the
page does not lie about its content. The corollary is the char
law: **`--charcoal` may only ever appear as charred wood** — a
surface carrying the crack field (§4) — never as a flat dark
rectangle, a dark footer band, or a "dark section" dropped between
light ones. Flat black is a colour choice; char is a material, and
this theme trades in materials.

**Best-fit sites and audiences.** Calligraphers, sumi-e and
brush-lettering artists; tea and incense houses; makers of brushes,
ink sticks, washi and stones selling the tools of the practice;
galleries showing East Asian ink work; a potter's or woodworker's
studio whose process involves fire; a small press printing with
letterpress and soot-black ink; a funeral or memorial practice that
wants gravity without religiosity (the char-and-ash register reads
as *aftermath handled with care*); a single-teacher school of any
hand discipline — brush, sword, bow — where one master's hand is
the brand. The audience it suits is patient and literate: people
who read a page top to bottom, who notice that a stamp is rotated,
who understand that a short ink stick means a long read. It is a
theme for sites whose conversion is a commission, an enrolment, or
a visit — considered acts, sealed rather than clicked.

**When NOT to use it.** Not for anything that must feel fast,
cheap, or plentiful: discount retail, delivery apps, coupon and
deal surfaces (the dry-brush ration would lie there — scarcity
theatre over abundance is exactly the slop this theme exists to
refuse). Not for dashboards or data-dense tools: the crack field
and the wash edges are enemies of tabular scanning, and §11 refuses
the data table outright rather than dress it. Not for children's
products (the register is ash and aftermath). Not for multi-author
platforms: the whole fiction is one hand, one stick, one seal — a
feed of forty contributors breaks it on contact. Not where the
client cannot supply real brush work: the headline (§6.1) is
painted from authored stroke masks, and a font pretending to be a
stroke is the first failure in §9. If there is no calligrapher —
hire one for a day, or choose another theme.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme, and
the gate greps for undeclared hex values in built CSS.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--charcoal` | `#121110` | Charred cedar surface — panels, masthead, footer ground | ~30% of viewport area across a page | Carries washi text at **16.47:1**; carries `--ash-pale` at 7.45:1. Never flat: always under the crack field (§4). |
| `--char-grain` | `#2E2A26` | The raised grain between cracks; char-panel inner surfaces, sheet shadows on char | ~12% | On washi **12.43:1** (usable as text on sheets); washi on it 12.43:1. Ash on it is 2.41:1 — forbidden pairing, ruled graphical-nothing: ash is never set on grain. |
| `--ash` | `#6E6259` | Ash edge — the grey rim where char meets air; captions, apparatus, hairlines on washi | ~6% | On washi **5.16:1** — the only mid-tone licensed for text, and only at caption size or larger (§3 law 4). On charcoal 3.19:1 — graphical only (rules, the crack field's lit edges), never text. |
| `--washi` | `#F4EFE6` | The sheet — content surfaces, body ground | ~48% | Carries `--ink` at 14.62:1, charcoal at 16.47:1, ash at 5.16:1, hanko at 6.12:1. The page's default reading ground. |
| `--hanko` | `#A62B25` | The seal — stamps, the one licensed red | ≤1% (rationed, §5) | On washi **6.12:1** (stamp text, the rare red word). On charcoal 2.69:1 and on grain 2.03:1 — the seal is therefore **never stamped directly onto char**; on dark surfaces it sits on a washi seal-slip (§6.9). |
| `--ink` (derived) | `#211D19` | Wet sumi at full density — body text, drawn strokes at rest | — | On washi 14.62:1. Distinguished from `--charcoal` by warmth and by use: charcoal is a *surface*, ink is a *mark on* a surface. The two never swap roles. |
| `--ink-dry` (derived) | `#575046` | The dry brush — broken strokes, the rationed dry passages | — | On washi 6.94:1 — dry marks remain fully legible; dryness is a texture, never an excuse for low contrast. |
| `--washi-deep` (derived) | `#E9E1D0` | The second sheet — underside of a turned sheet, skeleton tone, seal-slip stock | — | On charcoal 14.50:1. Used where a sheet's back or a thinner sheet shows. |
| `--ash-pale` (derived) | `#ADA193` | Ash in lamplight — text on char surfaces | — | On charcoal 7.45:1; on char grain 5.62:1. The only grey licensed for text on dark surfaces. |
| `--hanko-deep` (derived) | `#7E1D18` | Dried seal ink — stamp text at small sizes, error voice | — | On washi 8.83:1. Fresh stamps render in `--hanko`; their printed captions and the form's errors use the deep tone. |
| `--wash` (derived) | `rgba(33,29,25,.08)` | Ink wash — hover veils, the wet sheen's body, table row veils | — | A tint, never a text colour; always over washi or washi-deep. |

**Usage discipline.** A page is roughly half sheet, a third char,
and the remainder grain, ash and wash combined; red is a rounding
error with a signature. The ratio is audited by screenshot sampling
in the gate (§10): hanko-red pixels above 1.5% of any viewport is
"the seal used as a colour" and fails.

**Dark behaviour — the page does not invert; the studio lights a
lamp.** Charcoal & Ink is already a dark-and-light theme by
construction: char panels and washi sheets alternate in both
schemes. Under `prefers-color-scheme: dark`, sheets do not go
black. Instead: sheet ground shifts from `--washi` to
`--washi-deep` (the sheet seen by lamplight), the crack field's lit
edges warm by one step (ash at 3.19:1 graphical duty only), the
meniscus crescent (§6.7) brightens, and char panels stay exactly
`--charcoal` — burnt wood does not get darker at night. Text
pairings are unchanged and every measured ratio above still holds,
because no text-bearing surface changes its value class. A design
that "adds a dark mode" by inverting the sheets has misunderstood
the materials and fails §9.

## 3. Typography

**Faces.** Zen Old Mincho for display — headlines, section titles,
the brush numerals, stamp captions. Noto Sans JP for body,
apparatus and UI text. Both ship with Japanese glyph coverage
because the theme's world is bilingual at the level of single
words: a work's title may carry its kanji beside the romanisation,
set in the same Mincho, never in a novelty "brush font" (§9,
failure 1). No third face exists in the theme; tabular figures for
the counters come from Noto Sans JP's `font-variant-numeric:
tabular-nums`, not from a data font.

**Scale** (root 16px; the scale is in whole and half steps because
the studio measures in brush widths):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero headline) | Zen Old Mincho 900 | 56px / 1.15 (≥1200px); 44px tablet; 34px mobile | 0 | Painted, §6.1. Never set in a browser font-weight below 900 — a thin Mincho reads as print, not brush. |
| Section title | Zen Old Mincho 900 | 32px / 1.25 | 0 | Follows its divider stroke (§6.3); the stroke is sized from the title's measure (§4). |
| Sheet heading | Zen Old Mincho 700 | 22px / 1.35 | 0.01em | Sub-heads inside a sheet. |
| Lead | Noto Sans JP 400 | 19px / 1.75 | 0 | First paragraph of a sheet. |
| Body | Noto Sans JP 400 | 16.5px / 1.8 | 0 | Line-height is generous because washi sheets breathe; 1.8 is a law, not a default. |
| Caption / apparatus | Noto Sans JP 500 | 13px / 1.6 | 0.04em | Ash on washi; ash-pale on char. |
| Brush numeral | Zen Old Mincho 900 | 40px (counters) | 0 | §6.14; numerals are drawn, not typed — see the counter spec. |
| Stamp text | Noto Sans JP 700 | 11px | 0.12em, uppercase | Inside and beneath hanko marks; `--hanko-deep` on washi. |

**Type laws.**
1. **Mincho is the hand, Sans is the record.** Anything the artist
   is imagined to have written — titles, numerals, the colophon's
   line — is Mincho. Anything the studio records — prices, dates,
   form labels, errors — is Sans. A price in Mincho is a costume;
   a headline in Sans is a memo.
2. **The headline is painted, not typed** (§6.1). Its DOM text is
   complete and ordinary; the painting is a mask performance over
   it. Screen readers and no-JS visitors get the same words.
3. **Line-height grows on sheets, tightens on char.** Sheet body
   1.8; char-panel body (washi text on charcoal) 1.65 — the eye
   reads slower on grain, and the density admits it.
4. **Ash text never goes below 13px.** At 5.16:1 on washi, ash is a
   caption voice; below 13px it becomes a rumour. On char, ash is
   never text at all (3.19:1) — `--ash-pale` (7.45:1) speaks there.
5. **Red is a signature, not an emphasis.** Hanko red appears in
   type only inside stamps, in the single licensed red word of a
   colophon, and in form errors (as `--hanko-deep`). Links are ink,
   underlined with a hairline; a red link is a gate failure.

## 4. Layout language

**The alternation is the grid.** The page is a vertical sequence of
two surface kinds: **char panels** (full-bleed, `--charcoal` under
the crack field) and **washi sheets** (inset, `--washi`, with a
sheet shadow of `--char-grain` at 24% and a deckle-feathered edge
of 6–10px, never a border-radius — paper in this studio is torn or
cut, not rounded; the theme's global radius is **0**, and §11
enforces it component by component). A sheet never touches another
sheet; char always intervenes, the way a scroll is mounted between
boards. Within a sheet, content sits on a 12-column grid at
≥1200px (max measure 1120px, sheet padding 64px), 8 columns at
768–1199px, 4 below 768px with 20px sheet padding.

**The crack field.** Char surfaces carry the alligator-scale char
pattern: an SVG tile of irregular polygons (authored once, ~9KB,
`--char-grain` lines on `--charcoal`, with roughly one polygon in
seven catching a lit `--ash` edge at 3.19:1 graphical duty). The
tile is generated per site from a seed so two studios' char does
not match (§9, failure 6). The field is a background — it never
sits over text, and text-bearing char panels keep a 24px clear
margin inside the field's busiest band. Cracks do not animate; char
is what remains *after* the event. Only light moves on char (the
parallax, §5; the meniscus is in the footer inkwell, not here).

**The divider rule.** Every section — on sheet or char — opens with
exactly one brush-stroke divider (§6.3), sized to the section
title's measure: the stroke runs 100% of the title's width at
≥1200px, never the full content width; a divider wider than its
title is a underline that lost its nerve (§9). The stroke is the
section's first content, not a horizontal rule with a costume:
titles are never styled with borders, and `<hr>` does not exist in
the theme.

**The margin and the stick.** At ≥1200px the page carries a fixed
left margin rail of 72px on sheet sections (mirrored into the char
panels' clear margin) holding the ink stick and inkwell (§6.6) and
nothing else — no share buttons, no rail nav, no progress
percentage. The rail is the studio's desk edge. Below 1200px the
stick retires (§6.6 breakpoints) rather than crowd the sheet.

**Density and whitespace.** Sheets are dense at the top and spare
at the bottom: a sheet's final fifth is mostly empty washi, because
a painting leaves the lower paper empty and a sheet that fills to
its edge reads as a form, not a work. Char panels are the reverse —
their content clusters at the vertical centre, with char breathing
above and below. Whitespace in this theme is *unpainted paper* and
*burnt margin*; it is never "spacing" in the abstract, and §13's
choreography map treats the empty fifths as beats, not gaps.

**Vertical rhythm.** Sections separate by 0px — surfaces abut, as
mounted. Inside a sheet, the rhythm is 28px (one brush width at
display size); inside a char panel, 36px. Sheet-to-char transitions
are hard edges. The only soft edge on the page is an image's
ink-bleed feather (§6.4).

## 5. Full motion system

Five named easings, defined once, used everywhere; an element that
invents a sixth fails the gate's grep.

| Easing token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-brush` | `cubic-bezier(.6,.02,.2,1)` | Fast attack, long decelerating tail — a stroke laid down | Dividers, long stroke, bamboo draw, headline masks |
| `--ease-wash` | `cubic-bezier(.3,.6,.3,1)` | Slow in, slow out — liquid spreading | Ink-bleed reveals, washes-in, meniscus |
| `--ease-stamp` | `cubic-bezier(.2,2.2,.3,1)` | Overshoot with a hard settle — a seal pressed and held | Hanko stamps (§6.2, §6.9), counter landings |
| `--ease-grind` | `linear` | The stick shortens at reading speed; easing would be a lie | Ink stick (§6.6) only |
| `--ease-settle` | `cubic-bezier(.25,.8,.35,1)` | Paper and wood coming to rest | Sheet turns, card lifts, navigation |

**Durations ledger** (the theme's complete vocabulary; an element
may combine but not invent): stroke paint 350ms per character
(headline) / scrubbed (dividers, long stroke); bleed tighten
900ms; wash-in stagger 90ms; stamp press 200ms; sheen dry 3000ms;
meniscus breath 6000ms; counter roll 1200ms; sheet turn 550ms;
watchdog defaults 1400ms (entrance), 2600ms (pinned scenes),
1000ms (hovers and small acts).

**Every motion term, translated or refused.**
- *Scroll-triggered reveals* — the divider-then-wash entrance:
  stroke paints (§6.3), then content washes in staggered 90ms.
  Nothing fades up from below; ink arrives horizontally, as a hand
  moves.
- *Scroll-scrubbed animation* — dividers, the long stroke (§6.5),
  the ink stick (§6.6): all scrubbed from one shared rAF loop.
- *Parallax* — char panels drift against the sheet above them at
  0.94× (the char is the mounting board; it lags the sheet by
  design), capped at ±18px and clamped to authored overflow so no
  gap can open at a panel's edge.
- *Pinned sections* — exactly one: the long stroke showcase
  (§6.5), 200vh. A second pin on a page is refused; the hand draws
  one long stroke per page.
- *Masked reveals* — the headline's per-character SVG masks (§6.1)
  and the ink-bleed image masks (§6.4). Masks always sit over
  complete content (§6.1's safety rule is the theme's constitution).
- *Blur-to-sharp* — **refused.** Ink does not defocus; it dilutes.
  Where another theme blurs, this theme washes: a low-density pass
  (`--wash` at double strength) that resolves to full density.
  Blur on text is §9, failure 9.
- *Kinetic typography* — **refused** beyond the painted headline.
  Letters in this studio are brushed once and then are still; type
  that keeps moving is a sign, not a painting.
- *Marquee* — **refused.** Nothing in a studio loops sideways. The
  footer's colophon line is still; the meniscus (§6.7) is the
  page's only ambient loop, and it breathes rather than travels.
- *Animated counters* — brush numerals (§6.14): figures roll as if
  re-brushed, once, on entry.
- *Progress indicators* — the ink stick (§6.6) is the only one.
  Percentages are banned (§12): the stick *is* the fraction.
- *Micro-interactions* — wet-sheen hover (§6.8), hanko click
  (§6.9), stamp-press buttons (§11).
- *Page transitions* — the sheet turn (§6.16).
- *Reduced motion* — every element's variant, stated per element
  in §6; the global rule is the original entry's: **all strokes
  pre-painted, the hanko placed, no wiping.**

**The shared loop.** One `requestAnimationFrame` loop drives every
scrubbed value — divider paint, long-stroke draw, stick length,
inkwell darkness, char parallax, showcase wetness — with a lerp
factor of **0.11** for scrubbed values (the brush-drag feel: the
original's "slight resistance, then flow" is implemented as this
lerp, not as scroll hijacking; native scroll is never intercepted,
and wheel/trackpad behaviour is the platform's own). The loop
sleeps when no scrubbed value is within 0.1% of its target and
when the tab is hidden. All hover and time-based acts run on CSS
transitions/animations, not the loop.

**Hanko ration.** Red is spent like ink: per page, at most the hero
seal (§6.2), the visitor's own stamps (§6.9, each on a different
item), the footer seal, and form errors in `--hanko-deep`. A page
rendering more than seven red objects has used the seal as a
colour and fails §10's pixel audit.


## 6. Signature elements

### 6.1 The brushed headline

- **What & why.** The hero headline is painted character by
  character, each glyph revealed by an authored brush-stroke mask
  at its own ink density, the final character deliberately
  dry-brushed and scratchy. It belongs because the title of a
  calligrapher's site is itself a calligraphy work: its making is
  the hero's content, and a visitor who watches it being brushed
  has learned the site's whole argument before reading a word of
  body copy. The dry last character is the theme's law in miniature
  — the headline is where the content is richest, so the brush
  spends itself exactly to the end of it.
- **Structure.** A real `<h1>` in Zen Old Mincho 900 carrying the
  full headline text in the DOM from first paint. Over it, an
  SVG mask layer (one `<mask>` per character, each mask an authored
  stroke path drawn by the site's calligrapher as vector data —
  never generated from the font outline, §9 failure 1) clips a
  duplicate ink layer. Per-character density is a mask opacity:
  characters paint at 82–100% density in an authored sequence; the
  final character's mask carries the dry-brush texture (a
  fractal-noise displacement on the stroke edges plus three
  authored gaps in the stroke). The base `<h1>` sits beneath at
  full contrast at all times for no-JS and assistive technology;
  the ink layer is `aria-hidden`.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against an 800ms timer — painting in a fallback face would
  misalign every mask, so if fonts lose the race the headline
  ships printed (see fallback). Each character paints over 350ms
  `--ease-brush`, strokes staggered 110ms character to character in
  writing order (left to right for Latin, top to bottom for a
  vertical kanji cluster if the headline carries one). A
  six-character headline completes in 350 + 5×110 = 900ms; the
  ceremony caps at 1600ms — a headline longer than twelve
  characters shortens its stagger to fit, and longer than twenty
  is refused at build time (a title that long is a sentence, §12).
  The dry final character paints last and takes 420ms — dryness is
  slower, the brush dragged.
- **States.** Unpainted (JS-armed only, masks at 0) → painting
  (characters landing in order) → painted (rest; ink layer at full
  density, masks retired). Hover/focus: none — the headline is not
  a control and does not re-paint for attention. Scrolled-past
  mid-paint: the paint completes on its own timeline regardless of
  scroll; returning visitors (`sessionStorage`) find it printed.
- **Content merge.** The headline is the page's `<h1>` and its
  subject; the painting is not an intro bolted onto the hero, it is
  the hero's first content being made in front of the visitor, and
  the standfirst beneath it (§6.12's hero sheet) waits for the
  final dry character before its own wash-in begins.
- **Failure fallback.** Watchdog at 1400ms: if the paint has not
  completed, the ink layer snaps to full density and the masks are
  removed — the original entry's safety rule, kept verbatim in
  spirit: a painted reveal is a mask over complete content with an
  instant-complete state if a stroke is ever interrupted, so the
  dry-brush effect can never leave a character half-formed. No JS:
  the base `<h1>` is simply the headline, printed.
- **Reduced-motion variant.** No painting. The headline stands
  printed at full density with the final character rendered in its
  dry texture statically — the information (this character is the
  dry one) survives; only the performance rests.
- **Performance budget & mobile variant.** Masks are inline SVG,
  ≤14KB total for the headline; painting animates mask
  `stroke-dashoffset` and opacity only — no layout, no paint of the
  base layer. Mobile (<768px): characters paint at 300ms with an
  80ms stagger and the dry character's displacement is pre-baked
  into its mask (no live filter on a phone GPU).
- **Choreography timeline (v2).** t=0 fonts ready (or 800ms race
  lost → printed state, ceremony skipped) → t=0–350 character 1
  paints → stagger 110ms per character → final character at
  t=(n−1)×110, paints 420ms dry → t≤1600 paint complete → t=+150ms
  the hero word's edges begin drying (§6.2) → t=+500ms the hanko
  presses (§6.2) → standfirst wash-in begins as the stamp lands.
- **State matrix (v2).** *Rest:* painted, full density, dry final
  character. *Hover:* none. *Focus:* focus entering the hero does
  not alter the paint; if focus lands mid-paint the paint completes
  instantly (a keyboard visitor is never asked to watch a ceremony
  before reading). *Active:* n/a. *Scrolled-past:* completed,
  printed. *Disabled / no-JS:* printed at first paint. *Touch:*
  identical; first touch anywhere completes a running paint.
- **Breakpoints (v2).** ≥1200px: 56px display, 350ms/110ms paint.
  768–1199px: 44px, 320ms/95ms. <768px: 34px, 300ms/80ms,
  pre-baked dry mask, ceremony cap 1200ms.
- **Edge cases & failure modes (v2).** *Font swap after arming:*
  masks are armed only after `document.fonts.ready` resolves; a
  late swap disarms the layer and prints. *Tab hidden mid-paint:*
  rAF pauses; on return, wall-clock past 1400ms triggers the
  watchdog snap. *Headline edited in a CMS:* stroke masks are
  keyed to character count and authored per headline — an edited
  headline without new masks ships printed, never misaligned
  (build check, §15). *Very long headline:* refused at 20
  characters, §12.
- **Accessibility spec (v2).** The `<h1>` text is complete in the
  accessibility tree from first paint; the ink layer is
  `aria-hidden="true"` and `pointer-events: none`. Painting is
  never announced. Contrast is the base layer's at all times:
  `--ink` on `--washi` 14.62:1 (or washi on charcoal 16.47:1 on a
  char hero) — the mask never reduces the readable layer's
  contrast because the readable layer is beneath, whole.
- **Tokens consumed (v2).** `--ink`, `--ink-dry`, `--washi`,
  `--charcoal`, `--ease-brush`, `--dur-stroke-char` (350ms),
  `--dur-stagger-char` (110ms), `--dur-fallback-hero` (1400ms).

### 6.2 The hanko stamp on the hero word

- **What & why.** After the headline paints, one chosen word of it
  — the artist's name, or the work's key word — dries lighter at
  its edges, and the red hanko presses onto it: the artist signs
  the title. It belongs because a sumi-e work is not finished when
  the painting dries but when the seal is set; the stamp is the
  hero's full stop, and it teaches the visitor the gesture §6.9
  will later hand to them.
- **Structure.** An inline SVG seal (the artist's actual seal
  glyphs, carved as paths — a seal is a carving, not a font) inside
  a rounded-corner square (the theme's single licensed radius:
  3px, because seals are carved with softened corners; §4's radius
  law names this exception) in `--hanko` on the sheet, positioned
  overlapping the chosen word's final character by ~30% of the
  seal's width, rotated **2°** — the original entry's anti-slop
  detail, promoted to a spec: rotation is authored per site
  between 1.5° and 2.5°, never 0°, and one corner of the seal
  carries an over-inked blob (an authored opacity blot at the
  leading corner, 12% darker). The chosen word's edge-drying is a
  static gradient mask on its ink layer, armed by JS.
- **Motion spec.** Trigger: the headline's paint completing
  (§6.1 timeline). t=0: the chosen word's edges lighten over 600ms
  `--ease-wash` (a drying, not a fade — the centre stays dense).
  t=+500ms: the seal presses — scale 1.35→1 with opacity 0→1 over
  200ms `--ease-stamp`, landing with a 60ms hold at 1.02 scale
  before settling, the way a hand presses, pauses, lifts. The seal
  then stays for the life of the page. Once per session; a
  returning visitor finds the seal already set and the word
  already dry-edged.
- **States.** Unstamped (JS-armed only) → drying → pressing →
  sealed (rest, permanent). Hover over the seal: a 150ms
  `--ease-settle` deepening of the over-inked corner by 6% — the
  ink is dry but the eye re-presses it; no tooltip, no link,
  unless the site makes the seal its home link, in which case
  focus shows the theme's standard focus ring (§11) offset 3px.
  Scrolled-past: sealed.
- **Content merge.** The seal signs the actual headline word — it
  overlaps live type, sits in the hero's composition (§6.12), and
  its glyphs are the same seal that closes the colophon (§6.17)
  and that the visitor borrows in §6.9. One seal, three duties,
  no other red object in the hero.
- **Failure fallback.** If the headline shipped printed (font race
  lost, no JS, watchdog), the seal ships placed at its final
  rotation and the word ships dry-edged: the signed state is the
  DOM default, the ceremony is the enhancement. Watchdog: seal
  forced placed at paint-complete +1200ms regardless.
- **Reduced-motion variant.** The seal is placed, the word is
  dry-edged, nothing presses. The signature is present; the hand
  is not shown.
- **Performance budget & mobile variant.** One SVG ≤3KB, one
  transform animation. Mobile: seal scales to 34px (from 46px),
  overlap reduces to 20% so it never covers a second character of
  a small headline.
- **Choreography timeline (v2).** Paint complete (t=0) → t=0–600
  word edges dry → t=500–700 seal presses (200ms, overlapping the
  drying's tail — the hand does not wait for full dry, as real
  seals are set on nearly-dry ink) → t=700–760 hold at 1.02 →
  t=760 settle to 1.0 → standfirst wash-in releases (§6.12).
- **State matrix (v2).** *Rest:* sealed, 2° rotation, corner
  over-inked. *Hover:* corner deepens 6% over 150ms (pointer-fine
  only). *Focus:* only if the seal is the home link — ring per
  §11; otherwise not focusable. *Active:* n/a (or link behaviour).
  *Scrolled-past:* sealed. *Disabled / no-JS:* placed. *Touch:* no
  hover deepening; the seal is simply there.
- **Breakpoints (v2).** ≥1200px: 46px seal, 30% overlap.
  768–1199px: 40px, 25% overlap. <768px: 34px, 20% overlap, and if
  the headline wraps to three lines the seal moves to the word's
  right margin rather than onto a second line's text.
- **Edge cases & failure modes (v2).** *Chosen word wraps away
  from its authored position:* the seal is positioned relative to
  the word's span (inline anchor), never absolutely to the hero —
  a reflow carries seal and word together. *Seal glyph asset
  missing:* the hero ships without the ceremony and the build
  fails (§15) — a seal drawn from a font is §9 failure 1. *Dark
  hero (char panel):* the seal sits on a `--washi-deep` seal-slip
  (§2's ruling: hanko never stamps char directly, 2.69:1).
- **Accessibility spec (v2).** The seal is decorative signing of
  visible text: `role="img"` with `aria-label` "Seal of [artist
  name]" when it stands for the name, otherwise `aria-hidden`.
  It never covers the word's glyphs below legibility — overlap
  caps at 30% of one character, and the word remains readable
  through the seal's 88% opacity field.
- **Tokens consumed (v2).** `--hanko`, `--hanko-deep`, `--ink`,
  `--washi-deep`, `--ease-stamp`, `--ease-wash`, `--dur-stamp`
  (200ms), `--seal-rotate` (authored 1.5–2.5°).

### 6.3 Stroke dividers

- **What & why.** Every section opens with a single brush stroke
  that paints left to right, scrubbed to the section's entrance,
  its width and dryness varying per section. It belongs because in
  this studio a section does not begin with a heading dropped from
  a template; the hand paints a line, and then the section exists
  under it. The divider is the section's first brush act — content
  follows the stroke that announces it.
- **Structure.** An inline SVG per section: one authored stroke
  path (a tapered brush line, width profile varying 3–9px along
  its length, drawn once per site as vector data and reused with
  per-section variation by scale and one of three authored dryness
  grades), sized to the section title's measure (§4's divider
  rule). The path is clipped to the sheet or panel it opens; the
  section title sits directly beneath it in the DOM, fully printed
  from first paint.
- **Motion spec.** Trigger: scroll scrub via the shared loop
  (lerp 0.11). The stroke's drawn fraction maps to the section
  head's travel through the viewport's lower 45%→15% band: the
  stroke begins as the section's top crosses 85% of viewport
  height and completes as it reaches 55% — a paint duration the
  visitor controls with their scroll, typically 400–900ms of
  scrolling. `stroke-dashoffset` is written only by the loop.
  Once complete, a divider never un-paints: scrolling back up, the
  stroke stays — ink does not return to the brush (§5's ratchet,
  shared with §6.6).
- **States.** Unpainted (JS-armed only: dashoffset at full length)
  → painting (scrubbed, reversible *while* painting — scroll up
  mid-stroke and the brush lifts back) → painted (rest, permanent
  for the session). Hover/focus: none. Scrolled-past quickly: the
  loop's catch-up paints any divider whose section is above the
  band instantly on the next frame — a flung page arrives fully
  divided.
- **Content merge.** The divider is sized from its own section's
  title and immediately precedes it; it is the title's underline
  grown into an act. Remove the animation and the printed stroke
  still belongs — it is the section's furniture, not a reveal
  effect over hidden content (the content washes in *after* it,
  §5, but is never masked by it).
- **Failure fallback.** The DOM ships with the stroke fully drawn
  (dashoffset 0); JS arms the unpainted state only after the loop
  confirms a frame. Loop stall watchdog (1000ms without a frame
  while a divider is mid-paint): all dividers snap drawn. No JS:
  every section opens with its stroke, printed.
- **Reduced-motion variant.** All strokes pre-painted (the
  original entry's standing rule). Sections open with stroke and
  content together, statically.
- **Performance budget & mobile variant.** One dashoffset write
  per visible divider per frame; off-screen dividers are skipped
  by the loop's registry. Mobile (<768px): stroke width profile
  compresses to 2–6px and the scrub band widens (90%→50%) so a
  thumb's shorter throws still complete the paint.
- **Choreography timeline (v2).** Section top at 85% vh (t=0) →
  stroke fraction tracks lerped scroll through the band → stroke
  complete at 55% vh → t=+120ms the section title's wash-in
  begins (§5 stagger, 90ms per block) → content fully washed by
  ≈t=+700ms at reading pace. Jump-scroll: fraction set to 1 in
  one frame, wash-in skipped to printed.
- **State matrix (v2).** *Rest:* painted. *Hover:* none.
  *Focus:* a divider is never focusable; focus entering a section
  whose divider is unpainted paints it instantly. *Active:* n/a.
  *Scrolled-past:* painted (catch-up rule). *Disabled / no-JS:*
  printed. *Touch:* identical scrub; the wider mobile band
  applies.
- **Breakpoints (v2).** ≥1200px: stroke = title measure, 3–9px
  profile, band 85%→55%. 768–1199px: same sizing, band 88%→52%.
  <768px: 2–6px profile, band 90%→50%.
- **Edge cases & failure modes (v2).** *Section shorter than the
  band:* the divider completes when the section's *title* crosses
  55%, measured on the title, not the section box. *Two sections
  entering together* (short sections, fast scroll): both paint;
  the loop writes both offsets; neither waits. *Title edited
  longer:* stroke scales to the new measure (it is sized from the
  rendered title box at arm time, re-measured on resize).
  *Print:* strokes render drawn (print stylesheet forces the
  printed state).
- **Accessibility spec (v2).** Dividers are `aria-hidden`
  decoration adjacent to a real heading; the heading's text and
  order are untouched. The stroke's contrast against its ground
  is `--ink` on washi (14.62:1) or washi on charcoal (16.47:1) at
  full density; mid-paint fractions are transient and never the
  sole carrier of meaning.
- **Tokens consumed (v2).** `--ink`, `--ink-dry`, `--washi`,
  `--charcoal`, `--ease-brush`, `--loop-lerp` (0.11).

### 6.4 Ink-bleed image reveals

- **What & why.** Photographs and plates are revealed through
  feathered ink-bleed masks: the image soaks into the sheet from
  its edges inward, the feather tightening as the image centres,
  and no image on the page ever appears inside a clean rectangle.
  It belongs because in this world a photograph is treated as an
  ink wash laid on washi — it has edges the way a wash has edges,
  by absorption, not by cropping. The bleed is the site's way of
  admitting the image into the material.
- **Structure.** Each image sits in a `<figure>` on its sheet with
  an SVG filter/mask pair: a radial feather mask whose soft edge
  (authored per image, 24–64px of feather at full size) starts
  expanded — the image visible only at its dense centre, edges
  dissolved into the sheet — and contracts to its resting feather
  as the reveal completes. The resting state still has a feather:
  10–18px of bleed into the paper, permanent. The `<img>` itself
  is complete in the DOM with real `alt`; the mask is a visual
  treatment over a whole image, never a crop that hides content
  (the full image is always inside the feather).
- **Motion spec.** Trigger: scroll, via the shared loop. Reveal
  maps to the figure's travel through the viewport's 80%→45%
  band: feather contracts from its armed width to resting width
  and a `--wash` veil over the image lifts from 18% to 0 over the
  same travel, `--ease-wash` applied to the loop's output.
  Typical duration at reading pace ≈900ms. The reveal is
  one-way: a centred image keeps its resting feather; scrolling
  back does not re-dissolve it (ink, once soaked, stays).
- **States.** Dissolved (JS-armed only) → soaking (scrubbed,
  reversible mid-travel) → rested (resting feather, veil gone,
  permanent). Hover: none of its own — cards carrying images use
  §6.8's sheen above the rested image. Focus-within (image as
  link): the feather tightens a further 4px over 200ms
  `--ease-settle` — attention dries the edge slightly; the image
  itself never scales (no zoom-on-hover in this theme, §9).
- **Content merge.** The image's caption is set in the sheet
  directly under the bleed, and the feather bleeds *toward* the
  caption's paper — image and caption share one sheet and one
  soaking. Plates in the showcase (§6.5) and works in the cards
  (§6.13) all enter through this same bleed; there is no second
  image treatment on the page.
- **Failure fallback.** No JS or loop failure: images stand at
  resting feather with no veil — the printed state. If an image
  file fails to load, the figure shows its caption and a
  `--washi-deep` field with the work's title set in Mincho (the
  sheet records what should soak here) — never a broken-image
  glyph. Watchdog: any figure above the fold at load is rested by
  1400ms regardless of band position.
- **Reduced-motion variant.** Images stand at resting feather,
  veil absent. The bleed edge — the information that this image
  lives on paper — is fully present; only the soaking rests.
- **Performance budget & mobile variant.** Mask via CSS
  `mask-image` with an inline SVG data URI per feather grade
  (three grades shared by all images, ≤2KB total) — no per-image
  filters, no canvas. Mobile: feather widths scale ×0.6 (14–38px
  armed, 6–11px resting) and the veil lift is cut (the soak alone
  carries the reveal on small sheets).
- **Choreography timeline (v2).** Figure top at 80% vh (t=0) →
  feather contracts and veil lifts scrubbed through the band →
  figure at 45% vh: rested → caption wash-in follows at +90ms
  (§5 stagger) → hover/focus behaviours arm only after rest (a
  half-soaked image does not yet ask for attention).
- **State matrix (v2).** *Rest:* resting feather, no veil.
  *Hover:* none (sheen belongs to §6.8). *Focus:* feather −4px
  over 200ms when the figure is a link. *Active:* n/a.
  *Scrolled-past:* rested (catch-up on fling). *Disabled /
  no-JS:* rested, printed. *Touch:* no focus-tighten on tap; tap
  follows the link if any.
- **Breakpoints (v2).** ≥1200px: feather 24–64px armed / 10–18px
  resting. 768–1199px: 18–48px / 8–14px. <768px: 14–38px /
  6–11px, veil cut.
- **Edge cases & failure modes (v2).** *Slow image load:* the
  reveal waits for the image's `load` event or 1200ms, whichever
  first — a late image soaks in already-rested rather than
  re-performing (a photograph arriving late is laid on the sheet,
  not re-developed). *Very tall image:* the band measures the
  figure's top third. *Image with transparency:* refused at
  intake — washi work is opaque; a transparent PNG over the sheet
  shows the sheet through its whites and breaks the wash fiction
  (§15 intake check). *Dark image on dark char:* images live on
  sheets, never directly on char (§4), so the case cannot arise.
- **Accessibility spec (v2).** Real `<img>` with authored `alt`;
  the mask never removes image content from the accessibility
  tree and the full image is visually present at rest. Captions
  are `<figcaption>`, associated, in `--ink` at 14.62:1 (never in
  ash at image size). Focus ring on linked figures per §11,
  drawn outside the feather so the bleed never swallows it.
- **Tokens consumed (v2).** `--washi`, `--washi-deep`, `--wash`,
  `--ink`, `--ease-wash`, `--loop-lerp` (0.11).

### 6.5 The long stroke showcase

- **What & why.** The calligrapher's showcase section pins for
  200vh while one long stroke is drawn across it in real scroll
  time, its wetness varying with scroll speed. It belongs because
  it is the theme's thesis performed at full size: the visitor's
  scroll *is* the brush, and their hand's pace is drawn onto the
  page — move slowly and the stroke swells wet and dark; fling
  and it thins, dries, nearly breaks, but (by the safety rule)
  never does. Beneath the stroke, the showcase's works rest on
  their sheet, already printed; the stroke crosses *above* the
  sheet's margin band, through the section's own composition,
  not over the works themselves.
- **Structure.** A pinned section (sticky inner, 200vh of scroll
  travel) containing: the sheet with three to five works (each
  entered already via §6.4), and one SVG stroke layer spanning
  the section's width at its vertical centre — a single authored
  path ~1400px of drawn length at desktop, with a width profile
  (2px at the lift-off, swelling to 14px mid-stroke, tapering to
  a dry 3px tail) modulated by two masks: a *draw mask*
  (dashoffset, scrubbed) and a *wetness mask* (opacity/density
  field written from scroll velocity). Velocity is sampled by the
  shared loop from its own lerped scroll delta, smoothed over
  300ms so a single wheel notch does not spike the stroke dry.
- **Motion spec.** Trigger: scroll scrub through the pin. Draw
  fraction = pin progress 0→1 mapped with `--ease-brush` applied
  to the loop output. Wetness: density = clamp(1.15 −
  velocity/2400, 0.55, 1) where velocity is px/s of lerped
  scroll; at rest the stroke rests at the density of its last
  drawn segment — wetness is a property of the drawn part only,
  the undrawn part has no density to vary. At pin end the stroke
  completes (final 8% draws over the last 16vh regardless of
  pace, so the tail always lands), the section unpins, and the
  stroke remains as the section's divider-grown-large: it becomes
  the showcase's permanent furniture.
- **States.** Undrawn (JS-armed only) → drawing (scrubbed;
  reversible — scroll up and the brush retreats, wetness of the
  retreating segment re-computed as it re-draws) → drawn (rest,
  permanent). Hover: none. Scrolled-past (jump): stroke drawn in
  full at its authored resting density profile (the velocity
  record of a jump is a lie the page declines to tell — a jumped
  stroke is an even stroke).
- **Content merge.** The stroke is drawn *through* the showcase's
  composition — it passes behind the section title's sheet edge
  and over the char margin, threading the works' sheet like the
  guideline a calligrapher rules before writing. The works
  themselves are never under the wet part of the stroke: the path
  is authored through the section's margin band (§4), so the
  performance frames the content instead of covering it — the
  standing rule that animated objects never cover their content,
  kept by path authorship rather than by z-index apology.
- **Failure fallback.** No JS / loop dead: the stroke stands
  drawn at resting density and the section is unpinned (pin is
  JS-armed; the static section is a normal sheet sequence).
  Watchdog at 2600ms of pin time without scroll progress: the
  pin releases and the stroke completes — a visitor on a
  scroll-jacking browser or an embedded webview is never trapped
  in someone else's showcase.
- **Reduced-motion variant.** No pin. The stroke stands drawn,
  the works stand rested, the section is a still sheet — with
  one apparatus line preserved: "ONE STROKE, DRAWN AT THE
  READER'S PACE." The fact of the performance is recorded; the
  performance rests.
- **Performance budget & mobile variant.** One dashoffset + one
  mask opacity write per frame; the stroke SVG ≤8KB. The pin is
  the page's only one (§5) and its 200vh is the page's longest
  scroll contract. Mobile (<768px): pin shortens to 140vh,
  stroke length ~90vw, wetness range narrows (0.7–1) — a thumb's
  velocity signal is coarser and the theme does not pretend
  otherwise; below 400px wide the pin is cut entirely and the
  stroke ships drawn (a very small screen gets the painting, not
  the performance).
- **Choreography timeline (v2).** Section top reaches viewport
  top (t=0, pin engages) → progress 0–0.85: draw + wetness
  scrubbed → works' captions wash in staggered as the stroke
  passes their column (each at the frame the draw fraction
  crosses its x-position, +90ms) → progress 0.85–1: final 8%
  lands, tail dries to its authored scratch → pin releases →
  the section's own divider (§6.3) is already beneath, drawn —
  the long stroke hands the eye down to ordinary scale.
- **State matrix (v2).** *Rest (after):* drawn, resting density.
  *Hover:* none. *Focus:* focus entering the section during the
  pin does not move the pin; if a focused element would be
  scrolled out by pin mechanics, the pin yields (focus wins —
  the section unpins and completes the stroke). *Active:* n/a.
  *Scrolled-past:* drawn, even density. *Disabled / no-JS:*
  unpinned, drawn. *Touch:* scrubbed identically; velocity from
  touch scroll deltas.
- **Breakpoints (v2).** ≥1200px: 200vh pin, full wetness range.
  768–1199px: 170vh pin, wetness 0.62–1. <768px: 140vh,
  wetness 0.7–1; <400px: no pin, stroke printed.
- **Edge cases & failure modes (v2).** *Scroll velocity
  unavailable* (keyboard scroll, scrollbar drag): velocity reads
  as the 300ms-smoothed delta regardless of input device;
  keyboard paging produces a dignified mid-density stroke.
  *Resize mid-pin:* progress is a fraction, not pixels — the
  stroke re-maps without a jump. *Embedded iframe with its own
  scroll:* the pin measures its own container's scroll; if no
  scroll progress is possible, the 2600ms watchdog completes it.
  *Works taller than the sheet:* the section is authored to a
  max of five works (§15); a sixth work starts a second sheet
  *after* the pin, never inside it.
- **Accessibility spec (v2).** The stroke is `aria-hidden`. The
  works, title and captions are ordinary DOM in reading order,
  reachable and readable at every pin position; the pin never
  moves focus and never traps scroll for assistive technology —
  a `prefers-reduced-motion` or AT-detected session gets the
  unpinned variant (the build exposes the same static variant
  under a `data-static` hook the AT stylesheet can target).
  Pin progress is not announced (it is weather, not content).
- **Tokens consumed (v2).** `--ink`, `--ink-dry`, `--charcoal`,
  `--washi`, `--ease-brush`, `--loop-lerp` (0.11),
  `--dur-fallback-pin` (2600ms).

### 6.6 Ink stick progress

- **What & why.** In the left margin rail, a sumi ink stick
  stands in its inkwell; as the visitor reads, the stick shortens
  — ground down by the reading — and the inkwell disc beneath it
  darkens with the ink being made. It belongs because it is the
  theme's progress indicator with the lie removed: ordinary
  progress bars fill up as you consume; this one is *consumed* as
  you progress. Reading the page uses up the ink it is written
  with, and the visitor can see the cost of the page in the tool.
- **Structure.** A fixed rail element (≥1200px only, §4) holding
  an SVG ink stick — a black lozenge 148px tall at page top,
  its top edge carrying the maker's stamped label in miniature —
  above a circular inkwell disc (the stone's well, 44px). The
  stick's rendered height and the well's fill darkness are both
  written by the shared loop from one value: document scroll
  fraction. Stick height = 148 × (1 − fraction) px, floor 18px
  (a stick is never ground to nothing on one page — the stub
  remains, and the colophon acknowledges it, §6.17). Well
  darkness: the disc's ink pool interpolates from `--char-grain`
  at fraction 0 to `--ink` at fraction 0.35 and holds — a well
  fills early and then simply *is* full; grinding continues into
  it. A hairline of ground ink dust (ash specks) accumulates at
  the well's rim past fraction 0.6.
- **Motion spec.** Trigger: scroll scrub, `--ease-grind`
  (linear — easing a grinding would be a lie about labour). The
  loop writes height and pool colour each frame the fraction
  changes by >0.1%. The stick also *tilts* almost imperceptibly
  — 0° at top, 2.5° at bottom, the lean of a stick worked by a
  right hand — written from the same fraction. No other motion:
  the stick does not bounce, glow, or celebrate at 100%.
- **States.** Full (page top) → grinding (any scroll) → stub
  (page bottom, 18px, resting in a full well). Hover over the
  rail: the stick's label enlarges via a 200ms `--ease-settle`
  scale on the label group only — the one moment the tool is
  inspected. Focus: the rail is not focusable and contains no
  controls. Scrolled-past/jump: fraction is fraction; the stick
  is exactly as ground as the reading position says.
- **Content merge.** The stick is not beside the content; it is
  the page's own supply. Its consumption is calibrated to the
  page's real length — a short page grinds a long stick barely,
  and the theme accepts the honesty: the fraction is of *this
  page*, and §12's copy never claims the stick measures anything
  else. The ink it grinds is the ink §6.3's dividers and §6.5's
  stroke are drawn with — same `--ink`, one supply.
- **Failure fallback.** No JS: the stick stands at a fixed
  three-quarter height over a three-quarter-dark well — the
  printed emblem of the tool, neither full nor stub (a printed
  page is always mid-work). Loop failure mid-page: the stick
  freezes at its last true fraction; a frozen stick is a small
  lie of at most one screen's reading, accepted and logged in
  §14's budget as the element's failure cost.
- **Reduced-motion variant.** The stick does not grind. It stands
  at three-quarter height, well three-quarter dark — the same
  printed emblem as no-JS. Progress information is carried by the
  ordinary means (headings, the colophon's position) as on any
  static page.
- **Performance budget & mobile variant.** Two style writes per
  changed frame; the SVG is ≤2KB. Below 1200px the rail retires
  entirely (§4): no mini-stick, no percentage substitute, no top
  progress bar — the theme would rather have no progress
  furniture than a translated one (§9, failure 7). The reading
  itself is the progress on a small screen.
- **Choreography timeline (v2).** Page top: stick 148px, well
  `--char-grain` → fraction 0.35: well reaches full `--ink` →
  fraction 0.6: rim dust appears → fraction 1: stick 18px stub,
  tilt 2.5°, well full → the colophon's seal (§6.17) is pressed
  by the visitor who arrives — the stub and the seal are the
  page's two ends of one act.
- **State matrix (v2).** *Rest:* at current fraction, still.
  *Hover:* label group scales 1→1.6 over 200ms (pointer-fine
  only, ≥1200px where the rail exists). *Focus:* not focusable.
  *Active:* n/a. *Scrolled-past:* n/a (it *is* the scroll state).
  *Disabled / no-JS:* printed three-quarter emblem.
  *Touch:* the rail does not exist at touch widths (<1200px);
  nothing is substituted.
- **Breakpoints (v2).** ≥1200px: full rail, 148px stick.
  768–1199px: retired. <768px: retired. (The retirement is a
  designed absence, specified here so no builder "helpfully"
  re-adds a bar.)
- **Edge cases & failure modes (v2).** *Page shorter than the
  viewport:* fraction is 1 at load; the stick ships at stub over
  a full well — a one-screen page is a page already read, and
  the tool says so. *Content injected below the fold* (a loaded
  archive, §11): fraction re-measures on the loop's next frame;
  the stick may *regrow* by the injected amount — the one
  licensed un-grinding, because the page genuinely got longer;
  §12's voice never mentions it. *Browser find-in-page jumps:*
  fraction follows; the stick is a gauge, not a diary.
- **Accessibility spec (v2).** `aria-hidden="true"` — the stick
  is an emblem, and its information (how far through the page)
  is positional, available to AT through headings and landmarks.
  It is never the sole carrier of progress: no content, price or
  state is communicated by stick length. Contrast is irrelevant
  by design (no text in the rail except the maker's label at
  11px, washi on `--ink` 14.62:1, decorative).
- **Tokens consumed (v2).** `--ink`, `--char-grain`, `--ash`,
  `--washi`, `--ease-grind`, `--ease-settle`, `--loop-lerp`
  (0.11).

### 6.7 Meniscus shimmer

- **What & why.** In the footer, the inkwell — the same well the
  margin stick grinds into, shown at full size at the page's end
  — holds a surface of liquid ink, and at its rim a crescent of
  light breathes slowly: the meniscus shimmer. It belongs because
  it is the page's closing proof of life: after all the dried
  strokes and set seals, the ink at the page's end is still
  liquid. The medium outlasts the message. It is the theme's only
  ambient loop (§5), rationed to the footer so the page's body
  stays still.
- **Structure.** An inline SVG inkwell (the stone, 120px wide)
  set into the colophon block (§6.17), its pool an ellipse of
  `--ink` with a crescent path along its upper rim in `--washi`
  at low opacity. The crescent's opacity and a 1px vertical drift
  of its highlight are animated by a CSS keyframe loop; the pool
  itself is still. The well's rendered darkness matches the
  margin stick's well at page bottom (full) — same object, two
  views, one state (§6.6's fraction drives both; the footer well
  is painted at the fraction the visitor has actually reached,
  which at the footer is 1).
- **Motion spec.** Trigger: time (ambient), gated on the footer
  entering the viewport (IntersectionObserver; the loop does not
  run for an unseen footer). Crescent opacity breathes
  0.10→0.22→0.10 over 6000ms, `--ease-wash` in and out; the
  highlight drifts ±1px over the same cycle. No other property
  moves. The cycle is not synchronised to anything else on the
  page — a breathing thing keeps its own time.
- **States.** Still (footer off-screen, or pre-arm) → breathing
  (footer visible) → still (footer leaves; the cycle pauses
  rather than resetting — it resumes mid-breath, like a held
  breath let go). Hover over the well: the crescent stills at
  its current opacity for as long as the pointer rests — looking
  closely at water stills it. Focus: the well is not focusable.
- **Content merge.** The well is the colophon's furniture
  (§6.17): it sits beside the seal and the practice record, the
  three objects a studio desk holds at day's end. Its liquid
  state is the counterweight to the footer's dried seal — the
  page ends with both a finished act (the stamp) and an
  unfinished medium (the ink).
- **Failure fallback.** No JS / observer failure: the crescent
  stands at its mid opacity (0.16), printed. The well reads as a
  still pool — correct in every state, merely unbreathing.
- **Reduced-motion variant.** No breathing. Crescent at 0.16,
  pool still. The ink is liquid in fact, not in performance.
- **Performance budget & mobile variant.** One CSS keyframe
  animation on one small SVG; zero JS per frame. Mobile:
  identical (the footer well is 96px); the drift component is
  cut, opacity breath only — a smaller pool, a simpler breath.
- **Choreography timeline (v2).** Footer enters (t=0) → t=0–3000
  crescent rises 0.10→0.22 → t=3000–6000 falls back → cycle
  repeats while visible → footer exits: freeze at current phase
  → re-entry resumes from that phase (phase is kept in a CSS
  animation-play-state toggle, never restarted).
- **State matrix (v2).** *Rest (visible):* breathing. *Hover:*
  stilled at current opacity. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* paused off-screen. *Disabled / no-JS:*
  printed at 0.16. *Touch:* no hover-still; breathing continues
  (a finger does not rest on water the way a gaze does — the
  spec accepts the difference rather than fake a press).
- **Breakpoints (v2).** ≥1200px: 120px well, opacity + drift.
  768–1199px: 108px, same. <768px: 96px, opacity only.
- **Edge cases & failure modes (v2).** *Dark scheme:* the
  crescent brightens one step (0.14→0.26 range) — lamplight on
  ink (§2). *Battery saver / hidden tab:* CSS animations pause
  with the tab natively; no JS state to corrupt. *Footer
  reached by jump:* the observer fires on entry regardless of
  how the visitor arrived; the breath starts at phase 0.
- **Accessibility spec (v2).** `aria-hidden`; the well is an
  emblem beside real colophon text. The animation is a 6s
  opacity breath — well outside photosensitivity concern, no
  flashing, and it honours `prefers-reduced-motion` by standing
  still. Nothing is communicated by the shimmer.
- **Tokens consumed (v2).** `--ink`, `--char-grain`, `--washi`,
  `--ease-wash`, `--dur-meniscus` (6000ms).

### 6.8 Wet-sheen hover

- **What & why.** Hovering a card lays a wet sheen across it: a
  gloss gradient that follows the pointer like fresh ink on a
  just-brushed surface, then dries — fading — over 3s after the
  pointer leaves. It belongs because attention, in this studio,
  is moisture: the surface you look at is briefly wet, as if the
  brush had just passed, and your leaving lets it dry. It is the
  theme's hover physics — no lifts, no shadows popping, no scale;
  paper does not jump when touched, it dampens.
- **Structure.** A `::after` gloss layer on each sheen-bearing
  card (§6.13's work cards, §11's buttons in their sheet form):
  a radial gradient (`--wash` at double strength falling to
  transparent over 240px) centred on a `--mx/--my` custom
  property pair written from pointer position, composited above
  the card's surface but below its text layer (text sits in a
  positioned child above the sheen — the sheen wets the *paper*,
  never the print, and contrast of text is therefore unchanged
  at every moment of the effect).
- **Motion spec.** Trigger: pointermove over the card (pointer-
  fine devices only). The gradient centre follows the pointer
  with the shared loop's lerp (0.11) — the sheen trails the hand
  by a breath, like liquid would. On enter, sheen opacity rises
  0→1 over 250ms `--ease-wash`. On leave, it dries: opacity
  falls 1→0 over 3000ms `--ease-wash` with a long tail — the
  last 10% takes a full second, the way a damp patch's edge
  lingers. Re-entering mid-dry re-wets from the current opacity.
- **States.** Dry (rest) → wetting (enter, 250ms) → wet
  (following) → drying (leave, 3000ms) → dry. Focus (keyboard):
  focus-within lays the sheen statically at the card's centre at
  60% strength, no follow — keyboard attention also wets the
  paper, but the brush is the card's own, centred. Active
  (press): the sheen deepens 20% for the press duration — a
  pressed sheet takes the ink harder.
- **Content merge.** The sheen exists only on surfaces the theme
  treats as paper: work cards, sheet buttons, the commission
  sheet's paper (§6.15). It never appears on char panels (char
  does not gloss — burnt wood is matte for life, §9 failure 8)
  and never on images themselves (their bleed edge is their
  finish, §6.4).
- **Failure fallback.** No JS: no sheen (the custom properties
  are never written; the layer sits at opacity 0). The card's
  ordinary hover state — its §11 treatment: a 1px ink hairline
  darkening — is pure CSS and survives. A sheen that fails
  mid-dry simply stops fading (opacity frozen ≤ its current
  value); the watchdog is unnecessary because the failure state
  is a slightly damp card, not hidden content.
- **Reduced-motion variant.** No follow, no dry. Focus and hover
  show the static centred sheen at 40% strength instantly — the
  information "this surface is attended" is kept; the liquid
  rests.
- **Performance budget & mobile variant.** One gradient layer
  per card, transform-free (background-position via custom
  properties on a composited layer); the loop writes two
  properties per hovered card per frame, and only while a card
  is hovered. Touch: no sheen on tap (a tap is a stamp's job,
  §6.9); cards on touch get their §11 pressed state only.
- **Choreography timeline (v2).** Pointer enters (t=0) → t=0–250
  sheen rises → following while inside (lerp 0.11 trail ≈90ms
  behind the hand) → pointer leaves (t=L) → t=L–L+3000 drying,
  final 10% across the last 1000ms → dry. Press during wet:
  +20% depth for the press, releasing back to the drying curve.
- **State matrix (v2).** *Rest:* dry, opacity 0. *Hover:* wet,
  following. *Focus:* static centre sheen 60%. *Active:* +20%
  depth. *Scrolled-past:* n/a (hover-scoped). *Disabled:* a
  disabled card takes no sheen — dry paper that cannot be used
  is not wetted. *Touch:* none.
- **Breakpoints (v2).** ≥1200px: gradient radius 240px.
  768–1199px: 200px. <768px: pointer-fine only (a mouse on a
  small screen still gets 160px); touch gets none at any size.
- **Edge cases & failure modes (v2).** *Pointer leaves through
  a child link:* the dry begins on card leave, not child leave
  (pointerleave on the card, not mouseout). *Two cards
  overlapped by a turned sheet (§6.16):* the covered card's
  sheen is inert (pointer-events follow the sheet stack).
  *High-contrast mode:* the sheen is decorative and may be
  removed by forced-colors; the §11 hairline remains.
- **Accessibility spec (v2).** Purely decorative layer,
  `pointer-events: none`, excluded from the accessibility tree.
  Text contrast is structurally unchanged (sheen below text).
  Focus is indicated by §11's ring, never by the sheen alone —
  the focus sheen is a companion, not the signal.
- **Tokens consumed (v2).** `--wash`, `--ink`, `--ease-wash`,
  `--dur-dry` (3000ms), `--loop-lerp` (0.11).

### 6.9 Hanko click

- **What & why.** Clicking a selectable item — a work in the
  gallery, a size, a date in the booking list — stamps a small
  red hanko beside it: rotated, slightly unevenly inked,
  persisting for the session as the visitor's selection record.
  It belongs because choosing, in this studio, is sealing: the
  visitor borrows the artist's gesture (§6.2) and their choices
  are marked onto the items themselves, in the artist's medium,
  instead of being collected in a cart icon's badge count. The
  stamp *is* the state — an item is chosen because it bears the
  seal.
- **Structure.** Each stampable item carries a stamp anchor (a
  positioned span at its corner, in the sheet's margin side). The
  stamp itself is the artist's seal SVG at 26px (§6.2's asset,
  small die), rendered in `--hanko` at 88% opacity with the
  authored over-inked corner, rotated by a per-item authored
  angle between −3° and +3° (each item's angle is fixed in the
  markup — the same item always takes the stamp at the same
  tilt, because a hand remembers). Selection state lives in the
  item's `aria-pressed` / radio semantics (§11); the stamp is
  its visual voice. Stamps persist in `sessionStorage` (item
  ids), re-placed instantly on revisit within the session.
- **Motion spec.** Trigger: click / tap / Enter / Space on a
  stampable item. The seal presses: scale 1.3→1, opacity 0→1,
  200ms `--ease-stamp`, with the 60ms hold at 1.02 (§6.2's press,
  miniaturised). Un-stamping (clicking a chosen item in a
  toggle group) is *not* an un-press: the stamp fades to a 12%
  ghost over 400ms `--ease-wash` and stays as a ghost — a lifted
  seal leaves a stain; the record that you chose and un-chose is
  kept honestly until the session ends. In a radio group, the
  previous item's stamp ghosts as the new one presses.
- **States.** Unstamped → pressing (200ms) → stamped (rest;
  slight uneven ink, per-item rotation) → ghosted (12%, after
  un-choice) → re-stamped (press again over the ghost, landing
  at full). Hover on a stamped item: no change (the seal is
  dry). Focus: §11 ring on the item; the stamp is not the focus
  indicator.
- **Content merge.** The stamp lands *on the item's own sheet
  corner*, overlapping its margin, never its title or price. The
  selection it records is the item's real state — the commission
  form (§6.15) reads the stamped items as its input; there is no
  separate cart state to disagree with the seals. What is
  stamped is what is ordered; the gate rehearses this (§10).
- **Failure fallback.** No JS: stampable items use their native
  semantics (checkbox/radio/button states with §11's CSS
  treatments) and no stamps appear — selection still works,
  unsealed. A stamp that fails to render (asset missing) fails
  the build (§15), never the page: runtime falls back to the
  §11 selected treatment (ink-filled marker).
- **Reduced-motion variant.** Stamps appear/disappear instantly
  (ghost at 12% without the fade). The record is identical; the
  press is not performed.
- **Performance budget & mobile variant.** One 3KB SVG reused by
  reference (`<use>`), one transform per stamp event; no loops.
  Mobile: stamps are 22px, anchors move fully into the margin so
  a thumb's stamp never covers the item's first line; tap
  targets stay §11's 44px regardless of the stamp's size.
- **Choreography timeline (v2).** Click (t=0) → item's native
  state flips immediately (state never waits for theatre) →
  t=0–200 seal presses → t=200–260 hold → t=260 settled → in a
  radio group, the previous stamp's ghost fade runs t=0–400 in
  parallel → the commission sheet (§6.15), if present on the
  page, updates its summary line at t=260 (after the press, as
  a clerk updates the record after the seal lands).
- **State matrix (v2).** *Rest:* stamped or unstamped per state.
  *Hover:* none on the stamp; item hover per §6.8/§11. *Focus:*
  ring on item. *Active:* the press itself. *Scrolled-past:*
  stamps persist (session record). *Disabled:* a disabled item
  cannot be stamped; an item disabled *while* stamped keeps its
  stamp but the form treats it as unchosen and §6.15 says so in
  its error voice — the seal records history, the form reads
  validity, and the two are never confused. *Touch:* tap =
  click, identical press.
- **Breakpoints (v2).** ≥1200px: 26px stamps, corner anchors.
  768–1199px: 24px. <768px: 22px, margin anchors, ghost opacity
  15% (small screens need the stain slightly darker to read).
- **Edge cases & failure modes (v2).** *Session storage
  unavailable* (private mode): stamps live for the page view
  only; nothing breaks, the record simply doesn't survive a
  reload, and no message nags about it. *Item removed from the
  DOM while stamped* (a work sells): its stamp record is
  dropped silently; the form's summary recounts from live DOM
  (§6.15's rule: the sheet reads the room, not the memory).
  *Rapid double-click:* the press restarts cleanly; state is
  idempotent per final click parity.
- **Accessibility spec (v2).** The stamp is `aria-hidden`; state
  is carried by real semantics — `aria-pressed` on toggle
  items, native checked on radios/checkboxes — and announced by
  the platform, never by the visual seal. The ghost state is
  never the sole signal of anything (it records history for the
  eye only). Stamp contrast on washi: `--hanko` 6.12:1 as a
  graphic; on char surfaces the stamp sits on a `--washi-deep`
  seal-slip (§6.2's ruling) at the item's corner.
- **Tokens consumed (v2).** `--hanko`, `--hanko-deep`,
  `--washi-deep`, `--ease-stamp`, `--ease-wash`, `--dur-stamp`
  (200ms).

### 6.10 The bamboo study

- **What & why.** In the artist section, beside the biography
  sheet, a bamboo study — culm, nodes, a spray of leaves — draws
  itself stroke by stroke as the section arrives. It belongs
  because the bamboo is the calligrapher's practice subject: the
  plant whose painting exercises every stroke the art contains
  (the culm is one stroke, the leaves are three kinds of press),
  and an artist page that shows the practice drawing itself says
  more about the hand than the biography's adjectives. It is the
  theme's second drawn work after the headline, at section scale.
- **Structure.** An inline SVG study (~420×520px at desktop) of
  authored stroke paths in drawing order: culm segments bottom to
  top (each a single path with the node gap left unpainted, as a
  real culm is drawn in lifts), branch strokes, then leaves in
  clusters of three to five, each leaf one tapered path. Two ink
  densities only: culm at full `--ink`, leaves alternating `--ink`
  and `--ink-dry` — but this dryness is *not* the §1 ration: leaf
  density variation is the drawing's own shading, inside a work,
  the way a real study's leaves vary; the ration governs the
  page's *functional* strokes (dividers, headline), and §9 names
  the difference so the exception cannot leak.
- **Motion spec.** Trigger: scroll, once, when the study's sheet
  crosses 60% viewport height. Strokes draw in authored order at
  calligraphic pace: culm segments 300ms each `--ease-brush`,
  branches 220ms, leaves 140ms, stagger 60ms within a cluster,
  160ms between clusters — the whole study completes in ≈2.8s.
  It draws once per session and never re-draws; a returning
  visitor finds the study finished on its sheet.
- **States.** Undrawn (JS-armed only: dashoffsets at full) →
  drawing (ordered strokes) → drawn (rest, permanent). Hover:
  none. Scrolled-past mid-draw: the draw completes on its
  timeline (it is time-based once triggered, not scrubbed — a
  study is drawn by the artist's hand, not the visitor's, and
  the fiction keeps whose hand is whose: §6.5's stroke is yours,
  this one is hers).
- **Content merge.** The study is the artist section's portrait:
  it sits where a photograph of the artist would go on another
  theme, captioned with the section's one line about practice
  (§12 fixes the caption form). The biography text wraps the
  sheet it shares; remove the animation and the finished study
  still portraits the section.
- **Failure fallback.** Ships drawn (dashoffset 0 in DOM); JS
  arms the undrawn state. Watchdog 2600ms from trigger: study
  snaps drawn. No JS: a finished study beside the biography —
  the printed state.
- **Reduced-motion variant.** The study stands drawn. No partial
  state, no draw.
- **Performance budget & mobile variant.** ≤10KB SVG, dashoffset
  writes only during the 2.8s draw. Mobile: the study scales to
  the sheet width; draw durations shorten ×0.8 (a small study is
  a quicker sketch) and leaf clusters merge their stagger to
  40ms.
- **Choreography timeline (v2).** Sheet crosses 60% (t=0) →
  culm segments t=0–1200 (4 × 300ms, lifts between) → branches
  t=1200–1900 → leaf clusters t=1900–2800 → drawn → the
  biography's first paragraph, which waits at 40% wash until
  t=900 (the culm stands), reaches full at t=1100 — the text
  arrives while the drawing is still young, neither waits for
  the other to finish.
- **State matrix (v2).** *Rest:* drawn. *Hover:* none. *Focus:*
  not focusable; focus entering the section mid-draw does not
  alter it. *Active:* n/a. *Scrolled-past:* drawn (completes on
  timeline). *Disabled / no-JS:* drawn. *Touch:* identical
  trigger.
- **Breakpoints (v2).** ≥1200px: 420×520, full timeline.
  768–1199px: 340px wide, durations ×0.9. <768px: sheet-width,
  durations ×0.8, cluster stagger 40ms.
- **Edge cases & failure modes (v2).** *Section reached by
  anchor jump:* trigger fires on arrival; draw plays once —
  an anchored visitor still gets the performance, because they
  arrived at the section, which is the trigger's meaning.
  *Artist section absent* (a site variant without biography):
  the element is simply not built; no other element may borrow
  its draw (the study is not a generic reveal, §9).
  *Multiple studies:* refused — one study per page, as one
  artist.
- **Accessibility spec (v2).** The SVG carries `role="img"` and
  an `aria-label` naming it ("Bamboo study, ink on washi") —
  it is a work, not decoration, and is labelled as one. Its
  drawing is not announced; the finished state is what the
  label describes.
- **Tokens consumed (v2).** `--ink`, `--ink-dry`, `--washi`,
  `--ease-brush`, `--dur-fallback-pin` (2600ms).

### 6.11 Charred masthead navigation

- **What & why.** The site's navigation is a char panel: a band
  of charred cedar across the page top, the studio's name set in
  washi Mincho, the section links as small washi sheets pinned
  along the grain, and the current section's sheet bearing a
  hairline of ink at its foot. It belongs because the visitor
  should know the materials before the first scroll: the nav is
  the first char surface and the first sheets they touch, a
  sample board of the page's two substances.
- **Structure.** A `<header>` on `--charcoal` with the crack
  field (§4) at its quietest density, height 72px desktop.
  Studio name left (Zen Old Mincho, washi, 20px). Links right:
  each a `--washi` slip (padding 8px 14px, radius 0) with
  `--ink` text; the current page's slip is longer — it extends
  6px below the band's baseline with an ink hairline drawn at
  its foot (the slip is *filed deeper*, not highlighted). A
  compact variant (name + a single "Sheets" disclosure) serves
  small screens; the disclosure opens a full char panel overlay
  with the slips stacked as sheets.
- **Motion spec.** On load, the slips settle in: each translates
  6px up and fades its wash in, staggered 70ms, 300ms
  `--ease-settle` — paper laid on wood, once. On scroll down
  past 400px the band compresses to 52px (the name shrinks to
  17px, slips to their labels' minimum) over 350ms
  `--ease-settle`, scrubbed by the shared loop; scrolling back
  up restores it. The current-slip's ink hairline draws 300ms
  `--ease-brush` when the current section changes via in-page
  navigation (the §6.16 transition carries the change).
- **States.** Rest (full height) → compressed (scrolled) →
  rest. Hover on a slip: §6.8's sheen at half strength (a slip
  is small paper; it dampens lightly) plus the slip lifts 1px —
  the one licensed lift in the theme, 1px, because a slip being
  picked up is paper behaviour. Focus: §11 ring in washi on
  char (16.47:1 ground — the ring is drawn in `--washi` with an
  ink offset, visible on both the band and the slip).
- **Content merge.** The nav's slips are the page's actual
  sections — the same list §6.16's transition turns between —
  and the current slip's deeper filing is the same fact the
  footer's colophon states in words. No utility icons, no search
  box in the band: a studio's board holds its sheets and its
  name, nothing else (search, where a site needs it, lives in
  the archive sheet, §7).
- **Failure fallback.** No JS: full-height band, all slips
  present, current slip pre-filed in the markup. The compression
  is JS-armed; without it the band simply stays tall — a
  printed masthead.
- **Reduced-motion variant.** No settle-in, no compression: the
  band is one height (60px, the compromise) for the whole page.
- **Performance budget & mobile variant.** The crack tile is
  shared with all char panels (one asset). Compression writes
  one height value via the loop. Mobile (<768px): name +
  disclosure; the overlay panel is a plain char sheet stack, no
  animation beyond a 200ms `--ease-settle` wash-in.
- **Choreography timeline (v2).** Load (t=0) → slips settle
  staggered, done by t≈0+4×70+300 → first scroll past 400px:
  compression tracks lerped scroll → in-page navigation: old
  slip's hairline wipes (150ms), new slip files deeper and its
  hairline draws (300ms) as the turned sheet lands (§6.16).
- **State matrix (v2).** *Rest:* full or compressed by scroll.
  *Hover:* half-sheen + 1px lift. *Focus:* washi ring.
  *Active:* slip presses 1px down (the lift reverses — picked
  up, then set). *Scrolled-past:* compressed state.
  *Disabled / no-JS:* static full band. *Touch:* no hover
  behaviours; the disclosure target is 48px tall.
- **Breakpoints (v2).** ≥1200px: 72px band, full slips.
  768–1199px: 64px, slips at 13px labels. <768px: 56px, name +
  disclosure only.
- **Edge cases & failure modes (v2).** *Many sections (7+):*
  slips wrap to a second row inside the band at tablet widths
  rather than shrinking below 13px; at mobile the disclosure
  absorbs any count. *Long studio name:* the name truncates
  with an ellipsis in Mincho at mobile — a name is not shortened
  by letter-spacing tricks. *Sticky over the pinned showcase
  (§6.5):* the masthead is sticky, the showcase pins beneath
  it; z-order is authored so the stroke never crosses the band.
- **Accessibility spec (v2).** `<nav>` with `aria-label`;
  current slip carries `aria-current="page"` — the deeper
  filing is visual, the semantics are explicit. Slip text:
  `--ink` on `--washi` 14.62:1; name washi on charcoal 16.47:1.
  Disclosure is a real `<button>` with `aria-expanded`; the
  overlay traps no focus (it is a panel, dismissed by Esc or
  by choosing).
- **Tokens consumed (v2).** `--charcoal`, `--char-grain`,
  `--ash`, `--washi`, `--ink`, `--wash`, `--ease-settle`,
  `--ease-brush`, `--loop-lerp` (0.11).

### 6.12 The first sheet — hero composition

- **What & why.** The hero is a single washi sheet laid over a
  char panel that extends 18vh above and below it: the sheet
  carries the brushed headline (§6.1), the drying sealed word
  (§6.2), a standfirst, and one action — a sheet-button (§11)
  that leads to the commission sheet. It belongs because the
  page's first screen should be one object, not a stack of
  widgets: a painting on its mounting board, with everything
  the visitor needs painted or printed on the one sheet.
- **Structure.** Char panel (full-bleed, crack field at quiet
  density) → sheet inset (max 1120px, §4 grid) → inside, top to
  bottom: the apparatus line (studio, place, one date — Sans,
  ash), the headline block (Mincho, with §6.2's seal), the
  standfirst (lead type, max 34 words — §12 caps it), the
  action row (one primary sheet-button; at most one text link
  beside it). The margin rail (§6.6) begins at this panel — the
  stick stands full beside the first sheet.
- **Motion spec.** The hero's choreography is the sum of its
  parts, sequenced by §6.1's timeline: sheet settles onto the
  char (translateY 12px→0, 500ms `--ease-settle`, once, on load)
  → headline paints → word dries, seal presses → standfirst
  washes in (staggered lines, 90ms, `--ease-wash`) → action row
  washes in last. Total ≈2.6s at most; every act after the paint
  is skippable by scroll (scrolling completes the hero to its
  printed state instantly — the page never holds a reader
  hostage to its own entrance).
- **States.** Composing (JS-armed sequence running) → composed
  (rest). Hover/focus belong to the children (§6.2, §6.8, §11).
  Scrolled-past: composed. The hero never re-composes.
- **Content merge.** Everything in the hero is the site's real
  first content — name, claim, invitation — on the one sheet.
  There is no hero image separate from the work: if the site
  has a signature work, its plate may occupy the sheet's lower
  third via §6.4's bleed, inside the same composition, captioned
  on the same sheet.
- **Failure fallback.** No JS: the sheet stands composed —
  headline printed, seal placed, standfirst and action present.
  The settle is the only motion lost. Watchdog: the sequence's
  last act (action row) is forced visible by 2000ms regardless
  of the paint's state.
- **Reduced-motion variant.** The composed sheet, statically:
  every element at its rest state from first paint.
- **Performance budget & mobile variant.** The hero's budget is
  its children's (masks ≤14KB, seal ≤3KB, crack tile shared).
  Mobile: the char margins shrink to 8vh, the sheet fills the
  width minus 16px gutters, and the apparatus line drops its
  date (the sheet is smaller; the record is kept in the
  colophon instead).
- **Choreography timeline (v2).** t=0 sheet settle (500ms) →
  headline paint (per §6.1, from fonts-ready) → seal press →
  standfirst wash (3 lines × 90ms stagger) → action row wash
  (+180ms) → hero composed; the first divider (§6.3) arms as
  the visitor scrolls.
- **State matrix (v2).** *Rest:* composed. *Hover:* children's
  behaviours only. *Focus:* first focusable element is the
  action button; focus arriving during composition completes
  the composition instantly. *Active:* n/a (container).
  *Scrolled-past:* composed. *Disabled / no-JS:* composed.
  *Touch:* first touch completes a running composition.
- **Breakpoints (v2).** ≥1200px: 18vh char margins, 1120px
  sheet. 768–1199px: 12vh margins, sheet full-width minus
  48px. <768px: 8vh margins, 16px gutters, apparatus drops the
  date.
- **Edge cases & failure modes (v2).** *Standfirst longer than
  34 words:* refused at build (§12) — the sheet's lower fifth
  must stay empty (§4 density law), and a long standfirst eats
  it. *Hero on char instead of sheet* (a variant for very short
  pages): the headline paints in washi ink on the char panel,
  seal on a seal-slip (§6.2) — all other beats unchanged; the
  variant is chosen at build, never responsive-switched.
  *Slow first paint:* the settle waits for first paint; the
  paint waits for fonts (§6.1's race); nothing queues behind a
  blocked asset because the hero has no image dependency by
  default.
- **Accessibility spec (v2).** Landmark order: header (§6.11),
  then the hero sheet as the page's first `<section>` with the
  `<h1>` first inside it. Reading order is DOM order; the
  settle transform never reorders. Contrast per §2 pairings
  throughout; the action button meets §11 (ink on washi,
  14.62:1, 48px tall).
- **Tokens consumed (v2).** `--charcoal`, `--washi`, `--ash`,
  `--ink`, `--ease-settle`, `--ease-wash`.

### 6.13 Hanging-scroll work cards

- **What & why.** Works — paintings, commissions, pieces for
  sale — are presented as small hanging scrolls: each card is a
  washi sheet with a char-grain roller bar at its foot (a 10px
  `--char-grain` bar with ash end-caps), the work's plate
  bleeding in at its head (§6.4), title and record beneath. It
  belongs because a work in this studio is not a tile in a grid
  of products; it is a scroll taken down and hung for viewing,
  and the card's furniture says so without a word of copy.
- **Structure.** A grid of cards (3 across ≥1200px, 2 at
  tablet, 1 at mobile), each: `<article>` on `--washi`, plate
  figure (§6.4), title (Mincho 22px), record line (Sans: year,
  medium, dimensions — the facts, §12), price or status line,
  and the stamp anchor (§6.9) at the sheet's lower-right corner.
  The roller bar is a `::after` at the card's foot. Cards are
  whole-item links where the site sells or shows detail; the
  stampable ones carry their own button (§6.9) inside, never a
  nested-link conflict (the card link wraps the plate and
  title; the stamp button is a sibling control).
- **Motion spec.** Entrance: cards wash in staggered 90ms as
  their row enters (§5), plates soaking per §6.4. Hover
  (pointer-fine): §6.8's sheen, plus the roller bar's shadow
  deepens 10% over 250ms `--ease-settle` — the scroll's weight
  registers; the card does **not** lift or scale (a hanging
  scroll does not jump off its hook; §9 failure 5). The bar
  itself sways 0.4° over 1200ms `--ease-settle` on hover entry
  and settles — the one sway in the theme, rationed to the
  object that physically sways.
- **States.** Rest → hovered (sheen + shadow + sway settle) →
  pressed (link active: bar shadow +20%, 100ms). Stamped state
  per §6.9. Sold/unavailable works: the plate's bleed rests at
  80% density and the status line reads in the §12 voice; the
  card takes no sheen and no stamp — what is gone is not
  wetted.
- **Content merge.** The card *is* the work's record: plate,
  title, facts, price, and the visitor's seal when chosen. The
  commission sheet (§6.15) lists stamped cards by title — the
  card grid and the form are two views of one set, kept in
  agreement by §6.9's DOM rule.
- **Failure fallback.** No JS: cards stand printed, plates at
  resting bleed, links live. The sway and sheen are
  enhancements; nothing about the work's facts waits on them.
- **Reduced-motion variant.** No sway, no wash-in (cards
  printed), sheen static per §6.8's variant.
- **Performance budget & mobile variant.** Card cost is its
  plate's (§6.4 shared masks). Mobile: single column, roller
  bar 8px, sway cut (a scroll on a phone screen does not sway
  for a thumb that isn't holding it).
- **Choreography timeline (v2).** Row enters (t=0) → plates
  begin soaking (scrubbed, §6.4) → card washes stagger t=0,
  +90, +180 across the row → records printed from first paint
  throughout (facts never wait for the wash — only the plate
  performs) → hover arms after the row's wash completes.
- **State matrix (v2).** *Rest:* printed, plate rested.
  *Hover:* sheen + shadow + 0.4° sway settle. *Focus:* §11
  ring on the link; sheen centred per §6.8. *Active:* shadow
  +20%. *Scrolled-past:* rested. *Disabled:* sold cards are
  not disabled controls — they are records; their link, if
  any, points to the work's archive page (§7). *Touch:* tap
  follows the link; stamp button is a separate 44px target.
- **Breakpoints (v2).** ≥1200px: 3 across, bar 10px.
  768–1199px: 2 across, bar 10px. <768px: 1 across, bar 8px,
  sway cut.
- **Edge cases & failure modes (v2).** *A work with no plate*
  (a text commission — a poem brushed to order): the card
  shows its title as the plate — Mincho title large on
  washi-deep, bled at its edges — never a placeholder graphic.
  *Long titles:* two lines max, then the record line moves
  down; cards in a row keep equal height by the record's fixed
  three-line block, not by truncating titles silently (a
  truncated title gets an ellipsis and the full title in the
  link's `aria-label`). *Many works (30+):* the archive sheet
  (§7) paginates by sheet-turn (§6.16), never infinite scroll —
  a studio's works are finite and the page says so.
- **Accessibility spec (v2).** Card link text is the work's
  title + status ("Title — available" / "Title — sold,
  archive"), never "view". Plate `alt` names the work, not
  its medium twice. Stamp button has its own label ("Seal
  [title] as chosen"). Contrast: record line in `--ink`
  (14.62:1), never ash at card size (§3 law 4 allows ash only
  ≥13px — the record is 13px Sans, in ink; ash is reserved for
  the year in the apparatus position, 13px, 5.16:1, passing at
  that size).
- **Tokens consumed (v2).** `--washi`, `--washi-deep`,
  `--char-grain`, `--ash`, `--ink`, `--wash`, `--ease-settle`,
  `--ease-wash`.

### 6.14 Brush-numeral counters

- **What & why.** The studio's numbers — strokes in the
  practice record, years of practice, works completed — count
  up on entry, and the figures are brush numerals: each digit
  is a small Mincho figure that lands as if re-brushed, dense
  and slightly irregular, not a rolling odometer. It belongs
  because numbers in this world were also written by the hand;
  a counter that ticks like a slot machine would import a
  casino into the studio. The count is a record being written
  out, once, in front of the visitor.
- **Structure.** A record block on a sheet (or on char, in
  washi): each figure is a `<span class="brush-figure">` with
  its final value in the DOM, a Mincho numeral at 40px, and
  beneath it the record's label in Sans apparatus. JS splits
  the count into a per-digit roll: intermediate digits are
  rendered as the same Mincho glyphs at rising density (a
  `--wash`-weighted ink that deepens), so the number appears to
  be inked in rather than flipped through.
- **Motion spec.** Trigger: the record block crossing 65%
  viewport height, once per session. Count duration 1200ms
  `--ease-brush` (fast attack, long settle — the hand writes
  the big stroke first): values ease from 62% of final to
  final — counters in this theme never start from zero, because
  the record did not start when the visitor arrived; counting
  from 0 is a lie about the studio's past (§12's figure rule).
  Digits land staggered 60ms right to left (units settle first,
  as a hand finishes a number at its end). At landing, each
  digit takes a 1px `--ease-stamp` settle.
- **States.** Printed (DOM default, full value) → counting
  (JS-armed at trigger) → counted (rest, permanent). Hover:
  none. Scrolled-past before trigger: the block counts when
  next seen, or ships printed if jumped past entirely (a
  jumped-to footer shows finished records).
- **Content merge.** The figures are the studio's real record —
  years, works, strokes — maintained as content, and the same
  figures appear in the colophon (§6.17) in words. A figure
  that cannot be sourced to the studio's record does not get a
  counter; §12 bans invented round numbers ("10,000 strokes!"
  is §9 failure 10 unless the record says so).
- **Failure fallback.** No JS: figures stand printed at full
  value. The counting is a performance of the record, never its
  container.
- **Reduced-motion variant.** Figures stand printed. No count.
- **Performance budget & mobile variant.** Text-only animation
  (opacity/density per digit), no assets. Mobile: figure size
  32px, stagger 40ms, duration 900ms.
- **Choreography timeline (v2).** Block at 65% (t=0) → digits
  begin at 62% value, density low → t=0–1200 value and density
  rise on `--ease-brush` → units land t≈1050, tens t≈1110,
  hundreds t≈1170 (60ms right-to-left) → counted; labels were
  printed throughout.
- **State matrix (v2).** *Rest:* counted/printed full value.
  *Hover:* none. *Focus:* not focusable. *Active:* n/a.
  *Scrolled-past:* printed if never triggered. *Disabled /
  no-JS:* printed. *Touch:* identical trigger.
- **Breakpoints (v2).** ≥1200px: 40px figures. 768–1199px:
  36px. <768px: 32px, 900ms count.
- **Edge cases & failure modes (v2).** *Figure updated in the
  CMS:* the count re-derives from the DOM value at trigger
  time — the animation reads the record, never a data
  attribute copy of it. *Very large figures (100,000+):* the
  count duration stays 1200ms (density carries the drama; a
  longer count is a longer lie about how long writing takes).
  *Decimal or unit-bearing figures:* refused — counters count
  whole things (strokes, years, works); measures live in
  records as text.
- **Accessibility spec (v2).** The figure's final value is in
  the DOM and the accessibility tree from first paint; the
  counting spans are `aria-hidden` duplicates (the printed
  value is a visually-hidden sibling if the visible one is
  being animated — build chooses one technique and §15 checks
  it). The count is never announced mid-roll.
- **Tokens consumed (v2).** `--ink`, `--wash`, `--washi`,
  `--ease-brush`, `--ease-stamp`.

### 6.15 The commission sheet — conversion form

- **What & why.** The page's conversion — commissioning a work,
  booking a lesson, ordering a piece — is a single washi sheet:
  ruled with hairlines like a letter, its fields labelled in the
  record's Sans, its chosen items listed from the visitor's own
  stamps (§6.9), and its submission sealed, not "submitted": the
  sheet is stamped with the studio's seal and a confirmation is
  written onto it. It belongs because a commission in this world
  is a letter to the artist, and the form's dignity is the
  conversion's argument — a visitor who has watched ink being
  spent carefully trusts the sheet with their request.
- **Structure.** A `<form>` on a washi sheet (char panel behind
  it, §4 alternation), fields in one column at ≥768px (two
  columns for the short record fields — name, direction — at
  ≥1200px only). Field treatment per §11: hairline-ruled inputs,
  ink-on-focus. The chosen-items summary is a live region list
  at the sheet's head, generated from stamped DOM items (§6.9's
  rule) with each line carrying the item's title and record. The
  submit control is a full-width sheet-button (§11) labelled in
  the §12 voice ("Seal and send"). Success replaces the sheet's
  body with the confirmation: the studio's seal pressed (§6.2's
  press at 40px), the request's own words quoted back, and the
  record line (date, items, the stated reply time).
- **Motion spec.** Field focus: the field's hairline inks —
  a 1px `--ash` rule deepens to 2px `--ink` over 200ms
  `--ease-brush`, drawn left to right (a small stroke under the
  field being written in). Summary updates land with a 150ms
  `--ease-settle` wash. Submit: the button presses (§11), the
  sheet's fields wash to 60% density over 400ms `--ease-wash`
  (the letter is being folded), then the confirmation sheet
  replaces it with the seal pressing at its head (200ms
  `--ease-stamp`) — total ceremony ≤900ms, and the confirmation
  content is in the DOM and announced at t=0 of it, not after
  the press.
- **States.** Composing (fields live) → sealing (submit,
  ≤900ms) → sealed (confirmation, rest). Error state: the
  sheet does not shake, redden wholesale, or clear — the
  offending field's rule inks `--hanko-deep`, its error line
  appears in the margin voice (§12) in `--hanko-deep` (8.83:1),
  and focus moves to the first error on submit. A field
  corrected: its rule returns to ink and the error line is
  struck through with a hairline before removal — the record
  keeps its corrections visible for a beat, like a proof.
- **Content merge.** The form's items are the page's stamped
  items; its fields are the commission's real facts (name,
  direction, the work's size, the letter itself). Nothing in
  the sheet is decorative: even its ruled hairlines are the
  fields' own rules. The seal on success is §6.2's seal — the
  studio seals the letter it received.
- **Failure fallback.** No JS: a plain, fully working form
  (native submit, server confirmation page styled as the sealed
  sheet). The summary list ships with a server-rendered or
  static "chosen on this page" note if stamps cannot be read.
  A failed submit (network) keeps every field's content — the
  sheet is never cleared by an error; §12's voice apologises
  and the visitor's words remain.
- **Reduced-motion variant.** No wash, no press: submit swaps
  to the confirmation instantly, errors appear instantly. The
  record-keeping (nothing cleared, corrections struck) is
  state, not motion, and is kept in full.
- **Performance budget & mobile variant.** No assets beyond the
  shared seal SVG. Mobile: single column, fields at 16px
  (no zoom-on-focus), the submit button sticky at the sheet's
  foot within the form's scroll context only — never a
  floating action bar (§11 refuses those).
- **Choreography timeline (v2).** Focus field (t=0) → rule
  inks t=0–200 → stamp placed elsewhere on page → summary line
  lands +150ms after the stamp settles (§6.9) → submit (t=S)
  → fields wash t=S–S+400 → confirmation swaps t=S+400 → seal
  presses t=S+400–S+600 → record line washes in t=S+600–S+800.
  Error path: submit → first error focused, rule inked, at
  t=S+100 (errors never wait for ceremony).
- **State matrix (v2).** *Rest:* composing, fields at hairline.
  *Hover:* sheet-button per §11; fields take no hover state
  (paper being written on is not hovered, it is focused).
  *Focus:* rule inks 200ms; ring per §11 in addition (the ink
  is the theme's voice, the ring is the guarantee). *Active:*
  button press per §11. *Scrolled-past:* n/a. *Disabled:*
  submit disabled only while a submit is in flight (≤900ms);
  fields are never disabled by validation state. *Touch:*
  identical; targets 48px.
- **Breakpoints (v2).** ≥1200px: two-column record fields,
  sheet max 880px. 768–1199px: one column, sheet full measure.
  <768px: one column, 16px fields, sticky-in-form submit.
- **Edge cases & failure modes (v2).** *No items stamped:*
  the form still works — the summary reads in §12's voice
  ("Nothing sealed yet — the letter below is enough") and the
  commission is a letter-only request; the form never blocks
  on an empty selection. *Item unstamped while the sheet is
  open:* the summary line ghosts (§6.9) then removes at 400ms;
  the letter field is untouched. *Very long letter:* the
  textarea grows by lines to a 12-line cap, then scrolls
  internally — the sheet never stretches past its mounting.
  *Autofill:* filled fields take the inked rule immediately
  (the browser wrote; the sheet acknowledges).
- **Accessibility spec (v2).** Native labels, `aria-describedby`
  for error lines, `aria-invalid` on error fields, errors in a
  `role="alert"` summary at the sheet's head on submit *and*
  inline (both — the head summary is the record, the inline
  line is the correction). Confirmation is a `role="status"`
  region present from the swap. Contrast: labels `--ink`
  14.62:1; errors `--hanko-deep` 8.83:1; placeholder text is
  banned (§11) — labels are always visible, as a letter's
  headings are.
- **Tokens consumed (v2).** `--washi`, `--charcoal`, `--ink`,
  `--ash`, `--hanko`, `--hanko-deep`, `--ease-brush`,
  `--ease-wash`, `--ease-stamp`, `--ease-settle`.

### 6.16 Sheet-turn transition & the unpainted sheet

- **What & why.** Moving between the site's pages turns a
  sheet: the current sheet lifts from its char mounting at the
  left edge and turns over (rotateY on a left hinge), revealing
  the next sheet already laid beneath; while a page loads, its
  skeleton is an *unpainted sheet* — washi with the layout's
  blocks present as pale wash rectangles and one stroke not yet
  painted at its head. It belongs because the site's pages are
  sheets in one mounting; you do not teleport between them, you
  turn. And a loading state in this studio is not a spinner —
  it is paper awaiting the brush.
- **Structure.** Transition: a clone-free technique — the
  outgoing page's sheet element is snapshotted by CSS transform
  on a wrapper (the live DOM itself turns; no raster copy), the
  incoming page is loaded beneath (same-document view transition
  or a fast fetch into the mounting), hinge at the sheet's left
  edge, `--washi-deep` as the turning sheet's underside tone.
  Skeleton: the incoming sheet rendered with its blocks as
  `--wash` fields at final geometry, its divider (§6.3) present
  but unpainted (dashoffset armed), title block a wash field of
  the title's true width class (short/medium/long, from the
  route's record).
- **Motion spec.** Turn: 550ms `--ease-settle` — rotateY 0→−78°
  with a softening shadow, the underside tone crossing at 40%,
  then the turned sheet is removed and the new sheet rests
  (it does not turn *in* — a turned page lands flat; only the
  leaving page performs). Trigger: in-site navigation clicks.
  A 900ms watchdog: if the incoming page is not ready, the turn
  holds at −30° for at most 400ms more, then completes to the
  skeleton sheet rather than holding a visitor mid-gesture.
  Skeleton resolution: blocks wash to content staggered 60ms
  as data lands, the head stroke paints (350ms `--ease-brush`)
  when the title lands.
- **States.** Resting → turning (550ms) → resting (new page).
  Back/forward navigation: the turn reverses hinge side
  (right hinge, rotateY +78°) — the sheet turns back. Hover:
  n/a. Interrupted turn (a second navigation mid-turn): the
  latest wins; the turning sheet snaps flat over the newest
  target (150ms) — sheets do not queue.
- **Content merge.** The thing that turns is the page's actual
  sheet — its content goes with it, readable until the hinge
  passes ~50°. The skeleton's blocks are the real layout's
  geometry; nothing shifts when content lands (the sheet was
  cut to size before it was painted).
- **Failure fallback.** No JS / no view-transition support:
  ordinary navigation, instant. A failed page load lands on
  §6.18's blank sheet with the navigation intact — never a
  browser error, never a stuck half-turn (the watchdog
  guarantees the turn resolves to *something* flat).
- **Reduced-motion variant.** No turn: a 150ms crossfade of
  `--wash` veils between sheets (the studio's wash standing in
  for the gesture), or instant where the platform prefers.
  Skeleton blocks appear and resolve without stagger.
- **Performance budget & mobile variant.** The turn transforms
  one wrapper (compositor-only); pages are ordinary documents.
  Mobile: turn shortens to 420ms and the rotation caps at
  −64° (a small sheet turns less theatrically); skeleton
  identical.
- **Choreography timeline (v2).** Click (t=0) → outgoing sheet
  begins turning t=0 → underside tone crosses t≈220 → incoming
  ready: turn completes t=550, new sheet resting, its divider
  paints per §6.3 as the eye lands → incoming late: hold −30°
  to t=900 → skeleton sheet flat at t=950 → blocks resolve as
  data lands, head stroke paints on title land.
- **State matrix (v2).** *Rest:* flat sheet. *Hover:* n/a.
  *Focus:* focus moves to the incoming page's `<h1>` (or its
  skip target) at turn completion — never mid-turn; a
  `aria-live` polite announcement names the new page once, at
  rest. *Active:* the clicked link's slip (§6.11) updates at
  completion. *Scrolled-past:* n/a. *Disabled / no-JS:*
  standard navigation. *Touch:* swipe-back gestures are the
  platform's; the turn follows the same timeline for taps.
- **Breakpoints (v2).** ≥1200px: 550ms, −78°. 768–1199px:
  500ms, −72°. <768px: 420ms, −64°.
- **Edge cases & failure modes (v2).** *Slow page (>1300ms):*
  skeleton path (above) — the turn never exceeds its contract.
  *Same-page anchor clicks:* no turn (anchors are movements
  within a sheet, §6.11's hairline handles them). *External
  links:* no turn; the sheet stays — you do not turn a page to
  leave the book. *Print:* transitions do not exist; each page
  prints as its sheet.
- **Accessibility spec (v2).** The transition is visual only;
  semantics follow the platform's navigation model (focus to
  the new page's heading, title updated, one polite
  announcement). No content is unreachable during the turn —
  the outgoing page remains in the tree until the incoming is
  ready. Reduced-motion and vestibular safety: the crossfade
  variant is also served under `prefers-reduced-motion`
  regardless of other settings.
- **Tokens consumed (v2).** `--washi`, `--washi-deep`, `--wash`,
  `--charcoal`, `--ease-settle`, `--ease-brush`.

### 6.17 Colophon footer & the inkwell

- **What & why.** The footer is a char panel holding the day's
  end of the studio desk: the inkwell with its breathing
  meniscus (§6.7), the artist's seal pressed into the colophon,
  the practice record in words (the §6.14 figures, written
  out), and the site's remaining links as small washi slips.
  It belongs because a sumi-e work's colophon is part of the
  work — the footer is where this page signs itself, states its
  materials, and leaves the ink still wet (§6.7) beside the
  dried seal.
- **Structure.** Full-bleed char panel (crack field, §4):
  three columns at ≥1200px — (1) the inkwell SVG (§6.7) with
  the stick's stub resting beside it (the §6.6 stick at its
  page-bottom state, drawn once here at rest — the rail and the
  footer are the same desk seen from two distances, and their
  states agree because both render fraction 1 at the foot);
  (2) the colophon text: studio name (Mincho), materials line
  ("Cedar, soot, washi, water"), the practice record in words,
  the copyright line; (3) link slips (washi, §6.11's treatment)
  for the site's secondary pages. The seal: pressed at the
  colophon's foot, 40px, rotated **2°**, one corner over-inked
  — the original entry's anti-slop detail lives here as law:
  the footer seal is *stamped by hand, not placed by grid*,
  and its rotation is authored per site (1.5–2.5°), never
  reused from the hero's value (§6.2's is its own).
- **Motion spec.** On the footer's first entry: the colophon
  washes in (stagger 90ms), the seal presses (200ms
  `--ease-stamp`, at the wash's end — the signature comes
  last), and the meniscus begins its breath (§6.7). The link
  slips take §6.11's hover. Nothing else moves; a footer that
  performs beyond its signing has forgotten its station.
- **States.** Unentered → entered (washed, sealed, breathing)
  → rest. Re-entry: no re-wash, no re-press (the seal is set);
  the meniscus resumes (§6.7). Scrolled-past by jump: entered
  state applied instantly.
- **Content merge.** The footer's record is the page's own:
  the practice figures are §6.14's, the materials line names
  the theme's actual tokens' materials, the seal is §6.2's.
  Legal links live on slips like everything else — the studio
  has no grey microtext row; §12's voice writes even the
  privacy line as a sentence.
- **Failure fallback.** No JS: footer stands washed, seal
  placed, meniscus printed (§6.7). All links live from first
  paint.
- **Reduced-motion variant.** Printed state; meniscus still.
- **Performance budget & mobile variant.** Shared assets only
  (crack tile, seal). Mobile: columns stack — inkwell and stub
  first (the desk), colophon second, slips last in a wrap;
  the seal stays at the colophon's foot, never floated to a
  corner for composition's sake.
- **Choreography timeline (v2).** Footer enters (t=0) →
  columns wash t=0, +90, +180 → seal presses t=270–470 →
  meniscus breath begins t=500 → rest. The stick stub beside
  the well is drawn at t=0 (it was ground by the reading; it
  does not perform its own arrival).
- **State matrix (v2).** *Rest:* sealed, breathing (when
  visible). *Hover:* slips per §6.11; well per §6.7. *Focus:*
  slips take §11's washi ring on char. *Active:* slip press
  per §6.11. *Scrolled-past:* entered state. *Disabled /
  no-JS:* printed. *Touch:* no hover states; slips are 44px
  targets.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px:
  two columns (inkwell + colophon; slips wrap beneath).
  <768px: stacked as above.
- **Edge cases & failure modes (v2).** *Very short page:* the
  footer may be in view at load — the entered sequence plays
  once on load in that case; the meniscus breathes from the
  start, which is correct: a one-screen page is a desk already
  reached. *Seal asset shared with §6.2:* the rotation values
  differ by authoring (§15 checks they are not equal — two
  stamps at the identical angle read as one stamp copied,
  §9 failure 3).
- **Accessibility spec (v2).** `<footer>` landmark; colophon
  text washi on charcoal 16.47:1; apparatus lines `--ash-pale`
  7.45:1 (never `--ash` on char for text, §3 law 4). The seal
  carries the same labelling rule as §6.2. Link slips meet
  §11 contrast and target size.
- **Tokens consumed (v2).** `--charcoal`, `--char-grain`,
  `--ash-pale`, `--washi`, `--ink`, `--hanko`, `--ease-stamp`,
  `--ease-wash`, `--dur-meniscus` (6000ms).

### 6.18 The blank sheet — 404

- **What & why.** A missing page is a blank sheet in the
  mounting: a washi sheet on char, its divider painted, and
  beneath it — nothing brushed. One line in the record's voice
  states the fact, and the sheet offers the studio's real
  next steps (the sheets that do exist). It belongs because
  the theme's honesty law (§1) applies most at failure: the
  page does not invent a work to fill the space, does not
  apologise in a mascot's voice, and does not leave the
  visitor on bare char — there is a sheet; it is simply, and
  statedly, unpainted.
- **Structure.** The standard alternation (§4): char panel,
  sheet inset. On the sheet: the divider stroke (painted, per
  §6.3's printed state), the heading in Mincho ("This sheet is
  unpainted"), one Sans line naming what was asked for (the
  path, in the record's voice, §12), and three link slips to
  real destinations (the works, the artist, the commission
  sheet). At the sheet's lower fifth — where §4's density law
  leaves paper empty anyway — a single dry-brush hairline: the
  page's one rationed dry mark (§1), placed where the content
  ran out. That placement is the joke and the law keeping it.
- **Motion spec.** Almost none, by design: the sheet settles
  (500ms `--ease-settle`, §6.12's beat) and the divider stands
  painted. The dry hairline does not draw. A 404 that performs
  has misunderstood the assignment; stillness is the
  statement. (The meniscus is not here; the inkwell lives in
  the footer below, which follows as usual.)
- **States.** One state: presented. Hover/focus on the slips
  per §6.11. Nothing else is interactive.
- **Content merge.** The blank sheet is the error's true
  content — the absence is the message, framed by the same
  furniture as every other page so the visitor knows they are
  still in the studio. The requested path is printed (recorded,
  §12) — the studio acknowledges what was asked for even in
  refusing it.
- **Failure fallback.** The 404 *is* a fallback; its own
  fallback is that it is plain HTML with live links — if every
  enhancement fails, this page is indistinguishable from its
  enhanced self.
- **Reduced-motion variant.** Identical (the settle is cut;
  nothing else existed).
- **Performance budget & mobile variant.** The lightest page on
  the site: shared assets only, no images, no counters.
  Mobile: identical composition, sheet gutters per §6.12.
- **Choreography timeline (v2).** Load (t=0) → sheet settles
  t=0–500 → rest. (Deliberately the shortest timeline in the
  theme.)
- **State matrix (v2).** *Rest:* presented. *Hover:* slips per
  §6.11. *Focus:* first focusable is the first slip; the
  heading is the page's `<h1>` and takes programmatic focus
  on load per §11's error-page rule, so AT visitors land on
  the fact. *Active:* slip press per §6.11. *Scrolled-past:*
  n/a. *Disabled / no-JS:* identical. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: standard sheet. 768–1199px:
  standard, 48px gutters. <768px: 16px gutters; slips stack
  full-width.
- **Edge cases & failure modes (v2).** *A path that exists but
  whose work sold:* not a 404 — the work's archive page (§7)
  serves it as a record; the blank sheet is only for what was
  never here. *Soft 404 risk:* the page returns a real 404
  status; the theme's beauty is not an excuse for a 200.
  *Repeated blanks:* no escalating copy, no "still lost?" —
  the sheet says the same true thing every time.
- **Accessibility spec (v2).** `<h1>` states the fact; the
  requested path is text, not an image; slips are links with
  destination names ("The works", never "click here").
  Contrast per §2 throughout; the dry hairline is decorative
  and `aria-hidden`.
- **Tokens consumed (v2).** `--washi`, `--charcoal`, `--ink`,
  `--ink-dry`, `--ash`, `--ease-settle`.

## 7. Page application map

- **Home.** Char masthead (§6.11) → first sheet hero (§6.12,
  painted headline, seal) → works sheet (three §6.13 cards) →
  showcase char panel with the long stroke (§6.5) → artist
  sheet (bamboo study §6.10, counters §6.14) → commission
  sheet (§6.15) → colophon footer (§6.17). The home page is
  the only page that carries the pin (§6.5); every other page
  type borrows its elements at resting scale.
- **Works / listing.** Masthead → sheet of §6.13 cards in rows
  of three, paginated by sheet-turn (§6.16) at 12 works per
  sheet — a studio's output is countable, and the page count
  is printed in the apparatus ("Sheet 2 of 3") rather than
  hidden behind infinite scroll. Filters, where needed, are
  text slips in a row above the grid (by medium, by
  availability), never a sidebar of facets: the studio does
  not stock a warehouse.
- **Work detail.** One work, one sheet: plate at full bleed
  (§6.4) at the sheet's head, title Mincho, the full record
  (medium, dimensions, year, the work's own colophon line),
  price or status, and the stamp button (§6.9) as the page's
  act. Below, on char, the work's making: two or three process
  plates with captions. The next work is a sheet-turn away
  (§6.16), named at the foot ("Next sheet: [title]").
- **Artist / about.** The bamboo study sheet (§6.10), the
  practice record (§6.14 figures in a row), a biography in two
  sheets separated by a char panel carrying one long
  quotation from the artist — set in washi Mincho on the char,
  no quotation marks (the char is the frame; §12).
- **Lessons / booking.** A sheet listing the teaching terms as
  a record (days, hours, the room's address) with date rows
  that take the stamp (§6.9 radio behaviour); the commission
  sheet (§6.15) below collects the letter. Dates are rows in a
  list, never a calendar widget (§11 refuses it: a month grid
  is a spreadsheet in costume here).
- **Commission / contact.** §6.15 alone on its char mounting,
  preceded by one short sheet stating the terms of commissioning
  (sizes, times, the deposit) in the record's voice — the terms
  are read before the letter is written, as a studio would
  state them before taking the seal out.
- **Archive (sold works).** §6.13 cards at their sold state —
  plates at 80% density, status lines in §12's voice, each
  linking to its detail-as-record. The archive is a sheet of
  records, not a graveyard: density is information, honestly
  printed.
- **404.** §6.18's blank sheet.

## 8. Worked examples

### 8.1 The hero, end to end — a calligrapher's home page

*Build.* Char masthead (§6.11) with the studio name "Kuroki
Brushworks" and four slips. Below, the hero char panel: crack
field at quiet density, sheet inset 1120px. On the sheet: the
apparatus line "KUROKI BRUSHWORKS — KYOTO — EST. 1998"; the
headline "The brush remembers" (21 characters — inside §6.1's
cap), its stroke masks authored from the artist's own brushed
original, scanned and traced; the word "brush" chosen for the
seal (§6.2); the standfirst at 31 words; one sheet-button,
"Commission a work", and a text link, "See the works".

*Scroll timeline.* t=0 first paint: sheet printed in full (the
no-JS truth). JS arms: sheet settles 500ms; fonts resolve at
~300ms; paint runs 350ms × characters at 110ms stagger ≈ 2.5s
for 21 characters — over §6.1's 1600ms cap, so the stagger
compresses to 60ms and the paint lands in ≈1.55s (the cap rule
working as designed: the ceremony fits its contract, not the
other way round). The final "s" paints dry over 420ms. "brush"
dries at its edges; the seal presses at +500ms into the drying,
settles by +760ms; standfirst washes in three lines; the button
washes last. The visitor scrolls at t≈2s: the composition
completes instantly to printed state, the first divider begins
painting as the works sheet's head crosses 85%.

### 8.2 Mid-page — the long stroke showcase on the same page

*Build.* After the works sheet, a char panel: the showcase.
Its sheet carries four works (plates via §6.4), the stroke
path authored through the panel's margin band above the sheet,
crossing the char, touching the sheet's edge at two points —
the guideline threading the mounting. Pin 200vh.

*Scroll timeline.* The visitor reaches the panel; it pins.
Progress 0–0.2: the stroke draws across the first char stretch,
wet (their pace is reading pace, ~600px/s → density ≈0.9).
They pause to look at a work: velocity → 0, the stroke waits —
scrubbed, it can only be where the scroll is; the *wetness* of
the next segment is being decided by the pause (density will
read 1.0 when they move — a rested brush is a loaded brush, and
the formula says so). They fling to the section's end: velocity
spikes past 2000px/s, density thins toward 0.6, the stroke
pales and its tail nearly breaks — then the final 8% lands at
its authored pace regardless, the pin releases, and the stroke
remains across the panel as the visitor reads the colophon
sheet below. Scrolling back up later: the stroke is simply
there, drawn — ink does not return to the brush.

### 8.3 Conversion — commissioning a work

*Build.* The visitor has stamped two works on the listing
sheet (§6.9 — "Sealed as chosen" on each) and follows the
commission slip. The commission page: terms sheet first
(sizes, the three-month making time, the deposit — record
voice), then §6.15's sheet. Its summary head lists the two
stamped works by title. The letter field is pre-headed, in
the sheet's furniture, "For a work in the manner of —" and
the two titles follow; the visitor edits freely.

*Scroll/interaction timeline.* They focus the name field: its
rule inks over 200ms. They write the letter. They submit with
the direction field empty: at +100ms the direction field's
rule inks `--hanko-deep`, focus moves to it, and its margin
line reads, in §12's error voice: "The direction is wanting —
a letter needs a place to go." Nothing they wrote is cleared.
They fill it; the error line is struck through for a beat,
then removed; the rule returns to ink. They submit again: the
fields wash to 60% over 400ms (the letter folding), the
confirmation sheet lands, the studio's seal presses at its
head, and the record line reads: "Received on the 14th. Two
works sealed. The studio replies within three days." The two
works' stamps, back on the listing sheet, remain — the record
of the choosing outlives the form.

## 9. Anti-slop — what makes THIS theme look cheap

1. **A brush font pretending to be strokes.** The headline set
   in a "calligraphy-style" typeface with no authored masks.
   *Cure:* §6.1's masks are traced from real brushed originals;
   no originals, no theme ( §1's when-NOT-to-use).
2. **Flat black sections.** `#121110` rectangles with no crack
   field — a dark-mode template wearing the palette. *Cure:*
   the char law (§1): charcoal only ever appears as charred
   wood, tile present, gate-checked by screenshot.
3. **Two stamps at the same angle.** Copy-pasted seals at
   identical rotation read as a logo repeated. *Cure:* every
   seal's rotation is authored per placement (§6.2, §6.17);
   §15 checks no two on a page are equal.
4. **Dry brush everywhere.** Scratchy texture applied to every
   stroke "for style" — scarcity theatre. *Cure:* the §1
   ration — one dry passage per section, at the content's thin
   point; the gate counts dry passages per section.
5. **Cards that jump.** Lift-and-scale hover imported from
   product grids. *Cure:* §6.13 — paper dampens (§6.8) and
   scrolls sway 0.4°; nothing leaves its hook.
6. **The same crack tile on every site.** A stock char texture
   makes two studios identical. *Cure:* the tile is generated
   per site from a seed (§4); the gate compares against the
   theme's own demo tile.
7. **A progress bar "for usability".** A translated stick is a
   bar with a costume. *Cure:* §6.6 — below 1200px there is no
   progress furniture at all, by design, and the absence is
   specified so it cannot be "fixed".
8. **Sheen on char.** Gloss on burnt wood — material nonsense.
   *Cure:* §6.8 is sheet-only; char is matte for life.
9. **Blurred text reveals.** Ink does not defocus. *Cure:* §5
   refuses blur-to-sharp; dilution (wash density) is the
   theme's equivalent.
10. **Invented round numbers.** "10,000 strokes" with no
    record. *Cure:* §6.14's source rule — every figure traces
    to the studio's record or is not counted.
11. **Red as an accent colour.** Hanko-red links, red badges,
    a red sale banner. *Cure:* the §5 ration and §10's pixel
    audit (red ≤1.5% of any viewport).
12. **Zen clip-art.** Bamboo dividers from an icon set, a
    stock enso favicon, kanji used as decoration by a site
    that cannot read them. *Cure:* every Japanese glyph on the
    page must be a word the site means (§12's glyph rule);
    decorative kanji is the theme's fastest tell.

## 10. Quality gate

Blocking unless marked (A = advisory):

- [ ] **Char law:** every `--charcoal` surface carries the
  crack field; screenshot audit finds no flat dark rectangle.
- [ ] **Dry ration:** dry passages counted per section ≤1,
  each at a content-thin point, each defensible in one
  sentence.
- [ ] **Seal audit:** every seal's rotation measured; no two
  on a page equal; every seal has its over-inked corner;
  hanko-red pixels ≤1.5% of any tested viewport.
- [ ] **Printed-state test:** with JS disabled, every page is
  complete — headline printed, seals placed, strokes drawn,
  forms working, counters at full value.
- [ ] **Watchdog test:** with the rAF loop frozen, every
  armed element reaches its printed state within its stated
  fallback (1400/2600/1000ms classes).
- [ ] **Stroke-source test:** headline masks and seal glyphs
  are authored vector data from real originals; no brush
  fonts anywhere (font audit).
- [ ] **Figure-truth audit:** every counter figure and every
  figure in copy traces to the studio's record; counts in
  §6.15's summary equal the stamped items in the live DOM
  (rehearsed with 0, 1, and 3 stamps).
- [ ] **Contrast audit:** text pairings measured against §2's
  table; no ash text on char; no hanko on char except on a
  seal-slip; no text below its law's size floor.
- [ ] **Motion audit:** easings grep — only the five named
  easings in built CSS; pins per page ≤1; marquee and
  blur-to-sharp absent.
- [ ] **Reduced-motion pass:** full page walk with
  `prefers-reduced-motion`: all strokes pre-painted, seals
  placed, no wiping, no pin, counters printed.
- [ ] (A) **Stick honesty:** on the longest page, the stub at
  the foot reads as *nearly* spent, not theatrically empty —
  the 18px floor is doing its work.
- [ ] (A) **Five-second test:** a first-time viewer, shown the
  hero for five seconds, can say "a calligrapher" and "the
  title was painted" unprompted.

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. The global rules: radius **0** everywhere
except the seal's carved 3px (§6.2); no shadows except the
sheet's mounting shadow (`--char-grain` at 24%, offset 0/10px,
blur 0 — a hard offset, because a mounted sheet's shadow is a
line, not a glow); focus ring is a 2px `--ink` outline offset
3px on sheets, 2px `--washi` outline offset 3px on char.

- **Buttons.** *Primary:* a sheet-button — `--washi` on char or
  `--ink` on washi (filled), Mincho label at 15px, 48px tall,
  hairline border of the ground's contrast colour. Press: the
  button takes a 1px translate down and its label's density
  deepens (the stamp-press family, `--ease-stamp` 150ms) —
  buttons in this theme are *pressed*, not clicked. *Secondary:*
  a text link with a hairline underline that inks on hover
  (§6.15's rule behaviour). *Refused:* pill buttons, gradient
  buttons, icon-only buttons without labels.
- **Inputs & textarea.** Ruled fields (§6.15): transparent on
  the sheet, a 1px `--ash` hairline beneath, inking to 2px
  `--ink` on focus over 200ms `--ease-brush`. Labels always
  visible above (Sans 13px, ink). No floating labels, no
  placeholder-as-label. Textarea grows by lines (§6.15).
- **Selects.** Refused as native dropdowns on sheets: choices
  are *rows that take the stamp* (§6.9) — a short list of
  options printed on the sheet, each a radio row. Where a
  platform forces a native select (checkout address country),
  it is styled as a ruled field with a Sans label and accepted
  as a foreign object, min 48px tall.
- **Radios & checkboxes.** Radio = a stampable row (§6.9).
  Checkbox = a small square seal-slip that takes a miniature
  ink mark (a brushed tick, authored path) when checked —
  never the platform's tick in a rounded box.
- **Tables.** **Refused** as data grids. Tabular records are
  set as *record lists*: ruled hairlines, label left in Sans
  apparatus, value right in Mincho or Sans — the practice
  record (§6.14) and the work's record (§7) are the pattern. A
  genuine multi-column dataset does not belong to this theme
  (§1).
- **Badges & tags.** Refused as coloured pills. A status is a
  line in the record ("Available", "Sold — in the archive")
  or a small seal-slip with ink text. No counts in bubbles;
  §6.9's stamps carry selection, not tallies.
- **Alerts.** A sheet-level alert is a *margin note*: a
  `--washi-deep` slip pinned at the sheet's head with the
  message in the record's voice and, for errors, a
  `--hanko-deep` rule at its left. No toast (below), no banner
  that pushes the sheet down mid-reading — the note waits at
  the head of the sheet it concerns.
- **Modals.** Refused. Anything a modal would do is a sheet:
  a work's enlargement is its detail page (§7) reached by
  sheet-turn; a confirmation is §6.15's sealed state. The one
  overlay in the theme is the mobile nav panel (§6.11), which
  is a char board of slips, not a dialog.
- **Toasts.** Refused outright. Feedback is written where it
  belongs: stamps on items, records in summaries, the sealed
  confirmation. A message that vanishes in 4 seconds is a
  rumour; the studio writes things down.
- **Tabs.** Refused. Sections are sheets in sequence (§4);
  where a page must offer alternate views (works by medium),
  the filter slips (§7) re-lay the grid — the visitor sees the
  room re-hung, not a panel swapped.
- **Accordions.** One licensed form: the terms sheet's clauses
  open as *unfolding paper* — a clause's body washes in under
  its hairline (300ms `--ease-wash`), one open at a time, the
  closed clauses' hairlines unbroken. Used only for terms and
  care instructions; never for primary content.
- **Pagination.** Sheet-turn (§6.16) with a printed apparatus
  line — "Sheet 2 of 3" — and named next/previous slips.
  Numbered page pills are refused.
- **Breadcrumbs.** Refused. A studio's site is shallow; the
  masthead's slips (§6.11) and the detail page's "next sheet"
  line carry orientation.
- **Search.** Where required (a large archive), it lives on
  the archive sheet as a ruled field (§6.15's treatment) whose
  results re-lay the card grid; the query is a line written on
  the sheet, never an expanding icon.
- **Loader.** The unpainted sheet (§6.16). Spinners are
  refused in all forms.
- **Progress.** The ink stick (§6.6) is the only progress
  component. No bars, no percentages, no step indicators — a
  multi-step commission is one sheet (§6.15), not a wizard.
- **Cards.** §6.13's hanging scrolls. No other card exists.
- **Tooltip.** Refused. Anything worth saying is printed on
  the sheet (apparatus lines exist for exactly this).
- **Avatar / byline.** The artist is represented by the seal
  and the bamboo study (§6.10), never a circular headshot.

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the two typefaces
(§3 law 1).

**The Hand** (Mincho contexts — headlines, titles, the
colophon's line): brief, concrete, first-person where the
artist speaks. Headlines name a thing or an act, never a
benefit: ✓ "The brush remembers" / ✓ "Works in soot and
water" / ✗ "Elevate your space with timeless art" / ✗
"Discover the magic of calligraphy". One clause is a headline;
two is a sentence asking to be a paragraph.

**The Record** (Sans contexts — labels, prices, errors,
apparatus): plain, exact, dated. It states facts and keeps
receipts. ✓ "Received on the 14th. Two works sealed. The
studio replies within three days." / ✗ "Yay! We got your
message!!" — and note: the Record uses **no exclamation marks,
anywhere, ever**; the gate greps for them in visible copy.

- **Labels.** Verbs of the studio: "Seal and send" (submit),
  "Seal as chosen" (stamp button's label pattern: "Seal
  [title] as chosen"), "Turn the sheet" (pagination next),
  "The works", "The artist", "The commission". ✗ "Submit",
  ✗ "Add to cart", ✗ "Click here".
- **Error voice.** The Record, apologising without grovelling,
  always naming the remedy: ✓ "The direction is wanting — a
  letter needs a place to go." / ✓ "That day is already
  sealed. Choose another, or write and ask." / ✗ "Oops!
  Invalid email format." An error never blames the visitor's
  competence; the letter is incomplete, the writer is not.
- **Empty states.** Stated as unpainted paper, never as
  absence-with-apology: ✓ (archive search) "Nothing is
  brushed under that word yet." / ✓ (no stamps) "Nothing
  sealed yet — the letter below is enough." / ✗ "No results
  found 😢".
- **Figures.** Every number traces to the studio's record
  (§6.14). Counts are written as figures in counters and as
  words in the colophon ("thirty-one years"). Percentages are
  banned from copy — the stick (§6.6) is the only fraction the
  site expresses, and it expresses it in wood and ink.
- **Glyph rule.** Japanese text appears only where the site
  means it: a work's real title, the artist's name, a term
  defined on the page. ✓ a title given as "The Salt Hours —
  塩の時間" where the work is so titled. ✗ decorative kanji in
  a hero background. A builder who cannot read a glyph may
  not ship it.
- **Fixed strings (verbatim).** 404 heading: "This sheet is
  unpainted." Showcase apparatus: "ONE STROKE, DRAWN AT THE
  READER'S PACE." Materials line: "Cedar, soot, washi,
  water." Sold status: "Sold — in the archive." These strings
  are the theme's furniture; translating the site translates
  them as units, never word-by-word into nonsense.

## 13. Full-page scroll choreography map

The home page, top to bottom (other page types reuse the same
beats at their elements). "Sees/feels" is the visitor's
experience; timings reference §6.

1. **The board.** Masthead slips settle (70ms stagger) as the
   sheet below settles onto its char. *Sees:* the materials,
   named. *Feels:* a desk being laid.
2. **The painting.** Headline brushes in; the last character
   dries scratchy. *Feels:* someone is in the studio, working.
3. **The signing.** "brush" dries at its edges; the seal
   presses and holds. Standfirst and the one button wash in.
   *Feels:* the work is finished and offered.
4. **The first stroke.** Scroll: the works sheet's divider
   paints under the visitor's hand; the stick in the margin
   has begun, almost imperceptibly, to shorten. *Feels:* my
   reading is spending something.
5. **The works.** Plates soak in through their bleeds; cards
   stand as hung scrolls. A hover dampens one. A click seals
   one — the stamp lands and stays. *Feels:* choosing is a
   physical act here.
6. **The long stroke.** The showcase pins. The visitor's own
   pace draws the stroke — slow and wet, or flung and nearly
   dry. Captions wash as the stroke passes their columns.
   *Feels:* the page is being drawn by my hand, and it can
   tell how I move.
7. **The release.** The pin lets go; the stroke remains as
   furniture. The stick is visibly shorter now; the well is
   dark. *Feels:* progress I can point at.
8. **The artist.** The bamboo study draws itself — her hand
   this time. The counters ink in their figures: years,
   works, strokes. *Feels:* a practice, measured in a life.
9. **The letter.** The commission sheet: the sealed works are
   listed at its head, already written into the letter's
   heading. The visitor writes; rules ink under their fields.
   *Feels:* correspondence, not checkout.
10. **The desk at day's end.** The footer: colophon washes in,
    the seal presses last, and beside the ground-down stub the
    inkwell's surface breathes — the ink still liquid.
    *Feels:* the work is done; the medium is not.

**Reverse pass.** Scrolling back up: nothing un-paints,
un-stamps, or un-grinds except the stick, which is a gauge of
position and honestly re-lengthens as the visitor returns
upward (it measures *where you are*, §6.6 — the dividers
measure *what has been read*, and the two instruments are
never confused). The showcase, re-entered from below, is
already drawn; its pin does not re-engage for a drawn stroke
(the pin exists to draw, not to detain).

**Jump scroll.** Any jump (anchor, find, scrollbar drag)
lands on the printed state: strokes drawn, studies finished,
counters printed, stamps where the session left them. The
page a jumper sees is the page a slow reader earned — the
choreography rewards pace with performance, never with
content.

## 14. Whole-page performance budget

- **Asset weight (home page):** HTML/CSS/JS ≤ 180KB gzipped;
  fonts ≤ 120KB (Mincho + Sans JP subsets, `display=swap` with
  the §6.1 race protecting the paint); crack tile ≤ 9KB;
  headline masks ≤ 14KB; seal ≤ 3KB; bamboo ≤ 10KB; long-stroke
  SVG ≤ 8KB; ink stick ≤ 2KB. Images (works' plates) are the
  only heavy assets: ≤ 160KB per plate at card size, lazy below
  the second sheet, and they are content, budgeted per site —
  the theme's own chrome is ≤ 330KB all-in.
- **Frame budget:** the shared loop's per-frame work is capped
  at 1.6ms on a mid-tier phone: writes per frame are limited
  to the visible scrubbed set (≤2 dividers, the stick, the
  pin's stroke, ≤2 parallax panels) — the registry culls
  off-screen elements. No layout reads inside the loop except
  the cached section offsets, re-measured on resize and on
  §6.6's licensed re-measure only.
- **Long tasks:** none over 50ms after first paint; the
  headline's mask arming is split per character across frames
  if the headline exceeds 12 characters.
- **Cut order when the budget is exceeded:** (1) the bamboo
  study ships drawn (its draw is the first theatre to rest);
  (2) meniscus drift component (opacity breath stays);
  (3) card sway; (4) hero sheet settle; (5) parallax (char
  stands still — it is burnt, it can bear it). **Never cut:**
  the printed-state guarantee, the watchdogs, the divider
  scrub, the stamp, the stick. A page that keeps its laws and
  loses its ornaments is still this theme; the reverse is not.
- **Failure cost accounting:** the loop's death costs the page
  its scrubbed motion only; every element's fallback (§6) is
  its printed state, so the worst case is a beautiful static
  site — the budget treats total JS failure as a supported
  configuration, not an error.

## 15. Build-order checklist

1. **Static mounting first.** Char panels with the seeded
   crack tile, washi sheets, the alternation, the grid — the
   complete page, printed, no JS. Gate §10's printed-state
   test passes on this build alone.
2. **Type and record.** Faces, scale, the two registers;
   write all copy before any motion exists (copy written to
   fit animation is §9's first symptom).
3. **Authored assets.** Commission the brushed headline
   original and the seal carving; trace masks and seal paths;
   generate the site's crack tile from its seed. Verify no
   brush fonts in the font audit.
4. **Dividers + wash-in** (§6.3, §5) on the shared loop;
   watchdog before proceeding.
5. **The hero ceremony** (§6.1, §6.2, §6.12) with its font
   race and session rule.
6. **Images** (§6.4) with the three shared feather grades.
7. **The showcase pin** (§6.5) — last of the scroll systems,
   because its watchdog protects the others' failure modes
   too; verify the focus-yield rule with a keyboard walk.
8. **The stick** (§6.6) and its two-view agreement with the
   footer well (§6.17).
9. **Interaction layer:** sheen (§6.8), stamps (§6.9) with
   session persistence, counters (§6.14).
10. **The commission sheet** (§6.15) against a real endpoint;
    rehearse the form-keeping rule (0/1/3 stamps; error
    paths; nothing cleared).
11. **Transitions & skeleton** (§6.16), then the blank sheet
    (§6.18) wired to a real 404 status.
12. **Footer** (§6.17) with its own seal rotation; check the
    two rotations differ.
13. **Reduced-motion build** — the full walk, §10's pass.
14. **Audits:** §10 in full, including the red pixel audit,
    the dry-ration count, and the exclamation grep.
15. **Sign-off** by someone who did not build it — the gate
    is signed by a non-builder, as a seal is pressed by the
    hand that owns it, not the hand that carved it.
