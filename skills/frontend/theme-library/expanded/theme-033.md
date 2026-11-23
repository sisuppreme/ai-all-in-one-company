# 33. Silk Unspooling — Expanded (v1 + v2)

> One continuous silk thread enters at the top of the page and is woven
> through every section — it underlines, loops, knots and finally ties
> off at the footer. The thread IS the navigation. Identity preserved
> exactly from the original library entry: the same five palette
> anchors (Raw silk `#F7F2EA`, Mulberry gold `#C9A86A`, Madder red
> `#7A1F2B`, Cocoon shadow `#2E2A26`, Mulberry leaf `#A8B5A0`),
> Cormorant Garamond (display, italic accents) + Karla (body), and all
> nine original signature elements deepened — not redesigned — plus
> one signature-grade element drawn from the original motion system
> (§6.10, measured figures) and eight page-family elements, for 18
> fully specified elements.

## 1. Concept & world

A bolt of silk begins as a single filament. A silkworm spins roughly
1,000–1,500 metres of it in one unbroken strand to build its cocoon,
and a reeler who knows the work can draw that strand off in warm water
without ever snapping it — one thread, from the cocoon to the spool to
the loom, unbroken the whole way. This theme takes that fact as its
interface. **One continuous silk thread enters at the top of the page
and is woven through every section.** It drops in and settles under
the hero headline (§6.1). It draws itself down the page exactly as far
as the visitor has read, so its drawn length *is* the reading progress
(§6.2). It loops itself around a product when the visitor reaches for
it (§6.3). At the page's conversion point it gathers, tightens and
ties a visible knot (§6.4). And wherever the page asks for money, the
thread visibly frays — three or four fine fibres separate from the
main line and tremble — because handmade silk is honest about being
handmade, exactly where money changes hands (§6.6). At the foot of the
page the thread does not fade out or get cut: it ties off into the
corner of a small woven sampler and ends, the way a real thread ends
(§6.8).

**The theme's one law: one thread, unbroken.** The master thread is a
single SVG path from the top of the document to the footer tie-off. It
may underline, loop, knot and fray, but it never breaks, never
branches into a second independent thread, and never appears somewhere
it connects nothing. Two corollaries follow and both are blocking at
the quality gate (§10). First: **the thread never decorates** — every
metre of it is performing connection (it physically links the sections
it passes), progress (its drawn length is the scroll fraction), touch
(the product loop, the knot) or honesty (the fray at money). A
decorative squiggle that happens to look like thread is a different
theme's ornament and is forbidden here. Second: **the thread never
crosses text.** It runs in the margin rail and through section
furniture — under headlines, around frames, beside prices — with a
minimum 16px clearance from any glyph; a thread that strikes through
a line of body copy has failed as surely as a broken one.

**Best-fit sites and audiences.** Silk and textile ateliers selling
scarves, yardage and finished cloth; couture and bridal houses whose
product is literally sewn; heritage craft marketplaces and single-maker
shops; silk-road and craft-tourism storytelling (a journey is a thread
through places); tea houses and slow-hospitality brands with a maker's
story; a weaver's or dyer's portfolio; a museum's textile exhibition
microsite. The audience is a visitor who has come to *consider*, not to
transact at speed — someone for whom the making is part of the price.
The page's pace is the pace of reeling: continuous, unhurried, and
impossible to skim without the thread noticing (it only draws as far
as you actually go).

**When NOT to use it.** Not for dashboards, admin tools, or anything
with dense data tables — a thread cannot annotate forty rows without
becoming the tangle the law forbids. Not for discount retail or
urgency-driven commerce: the fray at money points is *honesty*, and a
site shouting "SALE ENDS TONIGHT" in madder red while its thread
trembles reads as parody. Not for news or anything updated hourly —
the thread is composed for a fixed document, and a page whose sections
reorder daily would need its path re-surveyed daily. Not for
high-frequency trading, sports scores, or any content whose value is
its refresh rate. And not for a brand that cannot commit to the
metaphor end-to-end: a Silk Unspooling home page bolted onto a generic
checkout is worse than no theme at all, because the knot at conversion
(§6.4) is the theme's promise and a foreign checkout breaks it in the
visitor's hand.

## 2. Palette

Five anchors from the original entry, plus a closed list of labelled
derived tokens. Contrast figures below are measured, not estimated.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--silk` | `#F7F2EA` | Raw silk — the page ground, the cloth everything hangs on | ~78% of surface | Ground for `--cocoon` text at **12.77:1** ✓ and `--madder` at **9.15:1** ✓ |
| `--cocoon` | `#2E2A26` | Cocoon shadow — body text, the thread's shadow pass, footer ground | ~12% | On `--silk` 12.77:1 ✓; the only colour permitted for body text on light grounds |
| `--gold` | `#C9A86A` | Mulberry gold — **the thread itself**, gilt rules, sampler weft | ~6% | On `--silk` only **2.03:1** — decorative and thread use ONLY, never text; on `--cocoon` 6.30:1 ✓ (dark-scheme labels) |
| `--madder` | `#7A1F2B` | Madder red — the knot, the cinch, CTA ink, fray tips, error voice | ~3% | On `--silk` 9.15:1 ✓ text-grade; rationed: at most one madder element per viewport (§9) |
| `--leaf` | `#A8B5A0` | Mulberry leaf — quiet fills, sampler warp, success-adjacent washes | ~1% | On `--silk` only **1.93:1** — fills and large shapes ONLY, never text |

**Derived tokens (the complete list — no others may be invented at
build time):**

| Token | Hex | Derivation & role |
|---|---|---|
| `--silk-deep` | `#EFE5D2` | Raw silk shaded one step — hanging-piece cards, the order form's ground, table zebra. `--cocoon` on it: 11.39:1 ✓; `--madder` on it: 8.17:1 ✓ |
| `--gold-ink` | `#75591F` | Gold darkened to text grade — prices, yardage figures, labels that must be read. On `--silk` **5.88:1** ✓; on `--silk-deep` 5.24:1 ✓. This is the ONLY gold that may carry words or numbers |
| `--madder-deep` | `#5E1621` | Madder in shadow — the knot's underside, pressed states. On `--silk` 11.68:1 ✓ |
| `--leaf-deep` | `#5A6A50` | Leaf darkened to text grade — "in stock / ready" statements, the sampler's caption. On `--silk` 5.22:1 ✓ |
| `--fibre` | `#E4D3AC` | A single separated fibre — fray strands (§6.6), the loose end (§6.7). Decorative only; never the main thread's colour (a page drawn in fibre colour reads as undrawn) |
| `--thread-shadow` | `#2E2A26` at 18% | The thread's contact shadow on the cloth, offset 0 2px, blur 3px — the thread lies ON the silk, it is not printed in it |

**Dark-mode behaviour — lamplight, not inversion.** In the dark
scheme the workshop is lit by a lamp after hours: the ground becomes
`--cocoon`, body text becomes `--silk` (12.77:1 ✓), and the thread —
the same `--gold` — now glows gently against the dark at 6.30:1, the
one element that gains presence at night. Madder is replaced for text
by its lamplight lift `#D08A94` (5.25:1 on cocoon ✓) but the knot and
cinch keep true `--madder` as shape, never as words. Leaf becomes
viable for large labels (6.63:1 on cocoon) but stays out of body text
out of habit, not necessity. The fray (§6.6) uses `--fibre` strands in
both schemes — separated silk catches light the same way day or night.
Nothing inverts; the sampler (§6.8) keeps its light ground in both
schemes, a woven swatch pinned to the dark wall.

**Pairing laws.** (1) The thread is always `--gold` with its
`--thread-shadow`; a madder thread, a leaf thread, or a gradient
rainbow thread is a gate failure — one thread, one colour, whole page.
(2) Gold text is always `--gold-ink`; a price set in `--gold` is
unreadable *and* off-law (2.03:1). (3) Madder is the colour of
commitment only: knot, cinch, CTA, error, fray tips. Links are
`--cocoon` underlined by the thread's own device (§6.12), never madder
— if everything is madder, the knot means nothing.

## 3. Typography

Two families, cast permanently. **Cormorant Garamond** is the cloth's
voice — display, headlines, and every italic. **Karla** is the hand's
voice — body, labels, data, forms. The casting never swaps: a headline
in Karla or a price in Cormorant is a build error (§9).

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero) | Cormorant Garamond 500 | 64px / 1.02 (≥1200), 44px / 1.05 (<768) | −0.01em | The unspooling word (§6.5) is set from this role, italic |
| Headline (H2) | Cormorant Garamond 500 | 40px / 1.08 | −0.005em | Always underlined by the thread itself (§6.2), never by a CSS border |
| Subhead (H3) | Cormorant Garamond 600 | 26px / 1.15 | 0 | Section furniture headings — the sampler caption, card titles |
| Italic aside | Cormorant Garamond italic 500 | 21px / 1.35 | 0 | **The Weaver speaks** (§12): maker's asides, fray captions, the tie-off line. Italic is always a person talking |
| Body | Karla 400 | 17px / 1.65 | 0 | Measure 58–66ch; the thread's margin rail is outside the measure, always |
| Body strong | Karla 700 | 17px / 1.65 | 0 | Sparingly — the hand points, it does not shout |
| Label / apparatus | Karla 600, uppercase | 12px / 1.4 | 0.14em | "MEASURED FROM THE SPOOL", "TIED AT THE FOOT OF THIS PAGE" — the workshop's signage |
| Data / yardage | Karla 400, tabular figures | 15px / 1.5 | 0 | Prices, metres, counts. Tabular is law: a yardage figure that jitters while counting (§6.10) breaks the measure metaphor |
| Caption | Karla 400 italic-adjacent (Karla has no true italic cut used here — captions are 400 at 14px) | 14px / 1.5 | 0 | Figure captions sit inside the thread's loop (§6.3), never below-left in grey |

**Type laws.** (1) **Italic is a person.** Every Cormorant italic on
the page is the Weaver's voice (§12) — an aside, a confession, a
caption at a price. System italics for emphasis inside body copy are
forbidden; Karla bold does that work. (2) **The underline belongs to
the thread.** No text-decoration underlines on headlines, ever; the
SVG thread passing beneath a headline is the only underline a headline
may have. Inline links in body copy use a 1px `--gold-ink` underline —
the colour of a single drawn fibre — and that is the only exception.
(3) **Numbers are measured, not decorated.** All figures (prices,
yardage, counts) in Karla tabular; Cormorant's old-style figures are
banned from data because their varying heights read as ornament where
the theme needs a ruler. (4) **No letterspaced Cormorant.** Display
serif at 0.14em tracking looks like a wedding invitation template;
letterspacing belongs to Karla labels only. (5) **The shout does not
exist.** There is no all-caps Cormorant, no 90px headline, no bold
display weight above 600 — silk does not shout, and a theme about a
single quiet thread cannot either.

## 4. Layout language

**The margin rail.** The master thread lives in a dedicated rail: at
≥1200px a 96px-wide band at the left of the content column, inside
which the thread travels vertically, departing rightward only to
perform a named act — underline a headline, loop a frame, knot at a
CTA, fray at a price — and returning to the rail after each act. The
content column is 1180px max, offset so the rail never competes with
the measure. At 768–1199px the rail narrows to 56px and the thread's
excursions shorten (loops become three-quarter loops, §6.3). Below
768px the rail collapses to a 28px gutter and the thread runs at the
page's left edge; its acts become underlines and the knot only —
loops and frays move *inside* the gutter beside their content rather
than around it, because a phone-width frame has no room to be circled.

**Sections hang from the thread.** The original entry's image is the
layout law: sections are pieces on a line. Each section's furniture —
its headline, its lead image or card row — is positioned as if hung
from the thread's path at that height: headline baselines align to the
thread's underline pass; card rows hang with a deliberate 8–14px
vertical stagger between neighbours (piece 2 hangs 10px lower than
piece 1, piece 3 level with piece 1 — a rhythm, not randomness, and the
stagger values come from the fixed set {0, 8, 10, 14} so two builders
hang the same line). Nothing is centred on this page except the knot
(§6.4) and the sampler (§6.8): the two moments of commitment and
completion earn symmetry; everything else hangs.

**The thread's geometry (surveyed, not improvised).** The master path
is authored per page at build time against the real content — never
generated by a generic sine-wave script. Rules: minimum bend radius
40px (a silk thread drapes, it does not kink — the one exception is
the knot itself); vertical runs are straight within ±3px (gravity);
every act's excursion begins and ends on the rail centreline; the path
passes *behind* section furniture (z-index below cards and images,
above the ground) so pieces read as hung in front of their line; and
the path's total length is measured at runtime with
`getTotalLength()` and treated as the page's true length for progress
(§6.2) — the thread never claims the visitor has read further than
its own drawn end.

**Spacing rhythm.** An 8px base unit; section gaps are 96px (≥1200),
72px (768–1199), 56px (<768) — the gap is where the thread travels
unaccompanied, and it must be long enough for the travel to read as
journey, not as a connector between boxes. Whitespace is the cloth:
large unprinted areas of `--silk` are the material the thread is laid
on, and filling them with decorative blocks is the equivalent of
printing a pattern on raw silk — it destroys the ground the whole
theme stands on. Density law: at most one act of the thread per
viewport height. A page where the thread underlines, loops, frays and
knots inside a single screen is a tangle, however pretty each act is
alone.

**The footer is a tie-off, not a sitemap with a logo.** The document's
last 100vh is composed as an ending: the loose end swaying (§6.7), the
sampler weaving itself (§6.8), the tie-off knot, and only then the
house's ordinary footer furniture (address, links, colophon) set
quietly below the knot in Karla — the paperwork after the work.

## 5. Full motion system

Five named easings, owned by this theme. No other easing may be used;
in particular the generic `ease`, bounce and elastic curves are banned
— silk overshoots by millimetres, not by cartoon physics.

| Token | Curve | Used by |
|---|---|---|
| `--ease-silk` | cubic-bezier(0.22, 0.61, 0.21, 1) — a long, low-friction glide | The master thread's draw (§6.2), product loop (§6.3), parallax settle |
| `--ease-swing` | cubic-bezier(0.37, 0.01, 0.24, 1) with a damped-oscillation keyframe set | The thread drop's pendulum (§6.1), fibre sway phase (§6.7) |
| `--ease-cinch` | cubic-bezier(0.7, 0, 0.2, 1.4) — pull tight, 4% overshoot, hold | Knot cinch (§6.9), knot tightening final beat (§6.4) |
| `--ease-spool` | cubic-bezier(0.33, 0.9, 0.4, 1) — measured, even take-up | Counters (§6.10), sampler draw (§6.8), letter unspooling steps (§6.5) |
| `--ease-settle` | cubic-bezier(0.25, 0.8, 0.3, 1) | Reveals, hover states, the sheen sweep's fade |

**Every motion term, translated into this theme's language:**

- **Scroll-triggered reveals — "thread-first, content-second."** No
  block ever appears alone. The thread's relevant segment arrives or
  completes its act first (150–300ms), and the content it serves
  settles in behind it (`--ease-settle`, 420ms, translateY 12px → 0).
  A reveal with no thread involvement does not exist on this page.
- **Scroll-driven / scrubbed animation.** Exactly two scrubbed values
  exist: the master thread's drawn length (§6.2) and the CTA knot's
  tightening (§6.4). Both are written by the single shared rAF loop
  (lerp 0.12). Nothing else scrubs — a page where everything is
  scrubbed feels like a machine; a thread is pulled by hand.
- **Parallax.** Product imagery moves at *thread-speed* — the image
  layer translates at 0.94× scroll while its text stands still, the
  small lag of a piece sliding on its line. Exactly one parallax
  behaviour, one rate, images only. Headlines, body and the thread
  itself never parallax (the thread IS the reference frame).
- **Pinned scenes.** One pin per page maximum: the CTA knot (§6.4).
  The pin exists because a knot needs two hands and a held breath;
  pinning anything else spends the gesture.
- **Staggered reveals.** Entrance blocks stagger thread-first in
  reading order at 90ms intervals (§6.11). Stagger is capped at 5
  items; a sixth item appears with the fifth (a line of pieces is
  hung in one motion, not typed out).
- **Masked reveals.** The sampler's weft lines reveal by a woven mask
  (§6.8) — each weft stroke is clipped by the warp it crosses. Text is
  never mask-revealed in this theme; letters arrive by unspooling
  (§6.5) or not at all.
- **Blur-to-sharp — REFUSED.** Silk does not come into focus; it is
  laid down. The theme's equivalent of arrival-softness is the thread
  arriving *undrawn* and drawing. Any blur filter on content is a gate
  failure (§10).
- **Kinetic typography — REFUSED, one exception.** Type does not move
  on this page, except the single unspooling hero word (§6.5), whose
  letters travel along the thread's own curve — the exception is the
  theme's thesis (type spun from thread), not a licence.
- **Marquee — REFUSED.** A marquee is an endless loop; this thread has
  two ends and both are accounted for (the drop, §6.1; the tie-off,
  §6.8). Endless motion contradicts the law.
- **Animated counters.** Yardage and price figures count like thread
  measured off a spool — even take-up, ticking at measured intervals,
  stopping dead at the true figure (§6.10). Counters count only real
  quantities (§12): metres in stock, pieces on the line, the drawn
  percentage of the thread. Invented counters are a gate failure.
- **Progress indicator.** The thread itself (§6.2). There is no other
  progress UI anywhere on the page — no bar, no percentage badge, no
  scroll hint arrow. The drawn length is the progress, and §6.12's
  navigation knots corroborate it.
- **Ambient loops.** Exactly two, both quiet: the loose end's fibre
  sway (§6.7, ±6px, 5s) and the silk sheen sweep (a `--silk-deep`
  gradient band, peak opacity 0.05, crossing silk grounds over 2400ms
  every 6000ms, `--ease-settle` — the cloth catching light as the room
  changes). Both pause off-screen and under reduced motion.
- **Hover physics.** The product loop (§6.3) and the knot's magnetic
  pull (§6.4/§6.9): the knot leans at most 6px toward the pointer —
  silk is light, a stronger pull reads as a magnet toy, not thread.
- **Micro-interactions.** The knot cinch (§6.9), link underlines
  drawing as single fibres (180ms `--ease-silk`), button presses that
  settle 1px with no shadow change — the hand pressing cloth.
- **Page transitions.** The thread pulls through (§6.16): on
  navigation the drawn thread completes to the tie-off in 350ms and
  the new page's thread drops in — leaving and arriving are the same
  gesture at two ends of one thread. Without JS, plain navigation; the
  transition enhances links it can intercept and never traps one.
- **Skeleton loading.** Unwoven warp (§6.16): content areas show as
  sets of parallel warp lines awaiting their weft — the cloth before
  it is cloth — with a 1200ms law after which plain `--silk-deep`
  blocks replace them.
- **Smooth scrolling.** Native scroll, lerped read-out. The theme does
  NOT hijack the scrollbar or impose inertial custom scrolling: the
  visitor's hand is on the thread, and a hijacked scroll makes the
  draw (§6.2) lie about whose hand it is. The rAF loop lerps the
  *drawn value* toward the true scroll position (0.12), which gives
  the silky low-friction feel honestly — the page moves at the
  visitor's speed; only the thread glides.
- **Reduced motion (global).** `prefers-reduced-motion` selects the
  finished cloth: thread fully drawn and static, knot tied, sampler
  woven, counters at final figures, no sway, no sheen, no pin (the CTA
  section stands unpinned with its knot already tied). Per-element
  variants are specified in §6 and are stricter than this summary
  wherever they differ.

## 6. Signature elements

### 6.1 Thread drop and settle

- **What & why.** The page's first act and its premise performed in
  under two seconds. On load, a single gold thread drops from the top
  edge of the viewport, swings **once** with damped pendulum physics,
  and settles into its resting place: the underline beneath the hero
  headline. It belongs because the thread must *arrive* before it can
  guide — a thread that is simply already there is a border; a thread
  that drops, swings and chooses its place under the headline is a
  presence, and the headline's underline being the thread's first
  resting place teaches the visitor, wordlessly, the rule they will
  use for the whole page: *follow the line; it is going somewhere.*
- **Structure.** The first 340px of the master thread's single SVG
  path (§6.2), isolated as its own `<path class="thread-drop">` only
  for the entrance: a vertical drop segment from y=−20 to the headline
  underline's y, with a shallow S-curve into the underline run. The
  drop is animated by morphing between two pre-authored path states —
  hanging (straight, swung 14px off rest at the bottom) and rest (the
  surveyed underline path) — never by a physics engine; two authored
  states and a damped keyframe set between them. The full thread path
  (§6.2) is present underneath from first paint, drawn to exactly the
  same resting geometry, so the handover at settle is invisible.
- **Motion spec.** Trigger: page load, gated on `fonts.ready` with a
  900ms watchdog (below). Drop: the thread falls 340px over **620ms
  `--ease-swing`**, arriving at the underline position displaced 14px
  to the reading-start side. Pendulum: one swing — 14px → −8px →
  +4px → −1.5px → 0, each pass ~62% of the previous amplitude, total
  swing **1180ms**, settling dead at **1800ms** from drop start. No
  second swing, ever: a thread that keeps swinging is a mobile over a
  cot, not a tool being laid down. The hero content (§6.11) begins its
  thread-first stagger at t+500ms, while the swing is still decaying —
  the page starts living before the thread is perfectly still, the way
  a workshop does.
- **Choreography timeline (v2).** t+0: page paints with the full
  thread already drawn to the hero's scroll fraction (the fallback
  state) → t+80ms: JS arms the drop — the visible segment is swapped
  to the drop path at its hanging state → t+80–700ms: the drop falls →
  t+700ms: the segment reaches the underline, displaced 14px → t+700–
  1880ms: the pendulum decays through −8 / +4 / −1.5px → t+1880ms:
  rest; the drop path is removed and the master path (§6.2) owns the
  segment from here → the unspooling word (§6.5) may not begin before
  t+700ms, because its letters travel along this same curve and the
  curve must exist first.
- **State matrix (v2).** *Rest (pre-arm / no-JS):* thread drawn,
  underline in place — the finished state, identical desktop and
  touch. *Dropping:* 620ms, non-interactive, pointer-events none.
  *Swinging:* 1180ms decay, non-interactive. *Settled (terminal):*
  hands over to §6.2's scrub without a visible seam. *Hover:* none —
  the drop does not respond to the pointer; a visitor who grabs at the
  thread in its first second is told nothing, which is correct: it is
  not a toy. *Focus:* not focusable. *Scrolled-past (visitor scrolls
  during the drop):* the drop cancels instantly to the settled state
  at the current scroll fraction — the visitor's hand outranks the
  ceremony, always. *Disabled:* no JS → the rest state, permanently.
- **Content merge.** The thread settles *into the headline's
  underline* — the drop's destination is a piece of typography the
  page needs anyway. Remove the headline and the drop has nowhere to
  land; remove the drop and the headline has lost the underline §3
  forbids it to fake with CSS. The two are one object.
- **Failure fallback.** The master thread ships drawn in the DOM; the
  drop is an armed enhancement layered over an identical resting
  geometry. If `fonts.ready` has not resolved by 900ms the drop is
  skipped entirely (never fired late into a page the visitor is
  already reading). If the animation is interrupted — tab hidden,
  scroll, resize across a breakpoint — the segment snaps to rest. A
  2000ms absolute watchdog from first paint forces the settled state
  regardless of what any timer believes.
- **Reduced-motion variant.** No drop, no swing. The thread is simply
  there, drawn, underlining the headline — the finished cloth (§5).
- **Breakpoints (v2).** ≥1200px: as specced, drop 340px, swing
  amplitude 14px. 768–1199px: drop 280px, amplitude 10px, total settle
  1500ms. <768px: drop 200px, amplitude 7px, settle 1200ms — a phone
  screen is closer to the eye and a long swing reads as instability,
  not grace; the swing passes reduce to three (−5 / +2 / 0).
- **Edge cases & failure modes (v2).** *Return visit within the
  session:* the drop plays once per session (sessionStorage flag);
  later loads show the settled thread — a workshop you have already
  entered does not re-perform its opening. *Very tall hero (headline
  underline below 480px):* drop length is capped at 420px and the
  thread enters from the top of the *hero*, not the viewport — the
  surveyed path decides, the viewport does not. *Slow device:* if the
  rAF loop measures <30fps sustained during the drop, the swing is cut
  to its final pass and the thread settles — physics that stutters is
  worse than no physics. *Print:* the thread prints drawn at rest.
- **Accessibility spec (v2).** The thread is `aria-hidden` SVG in both
  schemes; the headline it underlines is ordinary DOM text, first in
  reading order. The drop is never announced and moves no focus.
  Nothing about the hero's meaning waits for the settle: the headline,
  standfirst and CTA are readable from first paint, under a thread
  that — in the worst case — simply never swung.
- **Performance budget & mobile variant.** One path morph on one SVG
  path, ≤60 frames of compositor work, zero layout. The drop segment's
  path data is ≤40 points. Mobile: the reduced geometry above; the
  morph is replaced by a transform on the segment group (cheaper on
  low-end GPUs) with the same keyframe timings.
- **Tokens consumed (v2).** `--gold`, `--thread-shadow`, `--ease-swing`,
  `--drop-dur` (620ms), `--swing-dur` (1180ms), `--watchdog-drop`
  (2000ms).

### 6.2 Scroll-drawn master thread

- **What & why.** The theme's spine, its progress indicator, its
  navigation and its connective tissue in a single line. One SVG path
  runs the full document height — down the margin rail, out to
  underline each headline, around section furniture, through every
  join — and it **draws itself in exact proportion to scroll**: the
  drawn length is how far you have read, to the pixel. It belongs
  because it collapses four separate UI systems (progress bar, section
  connector, scroll cue, decoration) into the one object the theme is
  about, and because a drawn thread is the only honest progress
  indicator for a page about unspooling: you can see how much silk is
  left on the spool by how much is still undrawn.
- **Structure.** A single `<svg class="master-thread">` absolutely
  positioned over the full document (width 100%, height = document
  height, `preserveAspectRatio="none"` is FORBIDDEN — the path is
  authored in true document coordinates inside a viewBox matching the
  layout grid, so 1 unit = 1px at the reference width and the path
  re-surveys at each breakpoint, §4). The path carries: the gold stroke
  (2.5px, round caps), a `--thread-shadow` duplicate offset beneath it,
  and named act sub-ranges (underline runs, loop detours, the knot, the
  fray zone, the sampler tie-off) recorded as length intervals at build
  time so other elements (§6.3, §6.4, §6.6) can address their stretch of
  the line. Drawing is `stroke-dasharray`/`stroke-dashoffset` against
  `getTotalLength()`, written by the shared rAF loop.
- **Motion spec.** Trigger: scroll, continuous. The target drawn
  length = (scroll fraction of the document) × (total path length),
  computed against the *thread's own geometry*: the path is surveyed
  so that its length accumulates in step with document height — a
  metre of thread is drawn per metre of page read, 1:1, with no easing
  applied to the mapping itself (the mapping is a measurement, not an
  animation). The loop lerps the written value toward the target at
  **0.12** per frame, which is where the silky glide lives: fast
  scroll → the thread streams behind the hand and catches up over
  ~300ms; slow reading → the thread creeps at reading pace. The draw
  is **ratcheted at act boundaries only**: within an act (a loop, the
  knot) the local elements own their sub-ranges; between acts the
  master draw is a pure function of scroll position and reverses
  symmetrically on scroll-up — thread re-spools as you re-read upward,
  which is correct: un-reading un-draws.
- **Choreography timeline (v2).** Spatial, not temporal — the timeline
  is the page: hero → the drop settles (§6.1) and hands this element a
  drawn length equal to the hero's fraction → each section boundary:
  the draw crosses the join during the same frames the section's
  thread-first reveal (§5) fires → at each act, the draw pauses its
  plain travel and the act's own spec (§6.3/§6.4/§6.6) governs its
  sub-range → the final 100vh: the draw slows into the loose end
  (§6.7) and stops exactly at the sampler's corner, where §6.8 ties it
  off. At 100% scroll the drawn length is the total length — not
  99.4%, not "close enough": the survey (§4) reserves the last 1% of
  path for the last 1% of scroll so the tie-off and the page end are
  the same event.
- **State matrix (v2).** *Rest (any scroll position, loop idle):* the
  thread drawn to the exact fraction; identical desktop/touch. *Drawing
  (scrolling):* lerp 0.12 toward target. *Catching up (fast fling):*
  the drawn value streams; if the gap exceeds 25% of total length
  (anchor jump, scrollbar drag to foot), the draw **snaps** to target
  in one frame — a thread does not perform a kilometre of travel for a
  teleporting reader. *Hover:* none (the thread is not a control; its
  acts have their own hover states). *Focus:* none. *Scrolled-past:*
  drawn past — the state is the scroll position, nothing latches
  except the acts' own terminal states. *Disabled (no JS):* the path
  ships with NO dash attributes — fully drawn, the whole page
  connected from first paint.
- **Content merge.** The path is surveyed *through the content*: it
  underlines the actual headlines, detours around the actual frames,
  frays at the actual prices. It is not a line laid beside the page;
  it is the page's sections, physically connected. Delete a section
  and the survey loses a stretch — the build fails its own geometry
  check (§10), which is the proof the merge is real.
- **Failure fallback.** No-JS: fully drawn (above). JS failure mid-page:
  a 1500ms watchdog on the loop — if no frame has been written for
  1500ms while scroll position changed, dash attributes are removed
  and the thread stands complete. Resize: the path re-surveys to the
  new breakpoint's authored geometry and the drawn fraction is
  preserved (fraction, not pixels — the reader's place is kept).
  Path-too-long guard: if a page's surveyed path exceeds 60,000 units,
  act sub-ranges are simplified at build time (fewer underline
  excursions) rather than letting dash math degrade on low-end devices.
- **Reduced-motion variant.** The thread is drawn 1:1 with scroll
  position with NO lerp (the written value equals the target every
  frame) — it remains a truthful progress line but glides not at all;
  under `prefers-reduced-motion` + no-JS it is simply fully drawn.
- **Breakpoints (v2).** ≥1200px: full survey, 96px rail, all acts.
  768–1199px: 56px rail, loops become three-quarter excursions (§6.3),
  underline runs shorten to the headline's first line. <768px: 28px
  gutter, the path hugs the left edge; acts reduce to underlines, the
  fray (§6.6, moved in-gutter) and the knot (§6.4); total path length
  typically 55–65% of the desktop survey — the phone page is a shorter
  thread, honestly, not the same thread squeezed.
- **Edge cases & failure modes (v2).** *Content grows after load
  (late image, webfont swap):* the survey re-measures on
  `ResizeObserver` of the document body, debounced 200ms, and the
  drawn fraction is preserved across the re-survey — the thread may
  lengthen but the reader never loses their place. *A section is
  removed by an A/B variant:* build-time geometry check fails loudly
  in CI (§10) rather than shipping a thread that detours around
  nothing. *Overscroll (rubber-band):* the target clamps to [0, total]
  — the thread never draws past its tie-off nor negative. *Horizontal
  scrollbar present (a build defect elsewhere):* the thread's viewBox
  is document-width at the reference grid; it does not chase horizontal
  scroll, ever.
- **Accessibility spec (v2).** The entire SVG is `aria-hidden="true"`,
  `focusable="false"`. Progress information the thread carries visually
  is duplicated in §6.12's navigation (real links, `aria-current` on
  the section the thread has reached) — no information exists only in
  the drawing. Contrast: the gold thread on silk is 2.03:1, which is
  lawful ONLY because the thread is never information-bearing alone
  (see the duplication rule); where a thread act does carry state —
  the knot's tied/untied (§6.4) — the state is also in text.
- **Performance budget & mobile variant.** One dashoffset write per
  frame, one path, no other layout or paint cost; the SVG is
  `content-visibility` exempt (it spans the document) but its stroke
  paint is confined to the drawn region by the dash itself. Budget:
  ≤0.4ms/frame of main-thread time. Mobile: the shortened survey above,
  stroke 2px, shadow pass dropped below 768px (the thread lies flatter
  on a small screen and the paint saving is real).
- **Tokens consumed (v2).** `--gold`, `--thread-shadow`, `--ease-silk`,
  `--loop-lerp` (0.12), `--thread-w` (2.5px), `--watchdog-thread`
  (1500ms), `--rail-w` (96px / 56px / 28px).

### 6.3 Product loop — the thread handles the merchandise

- **What & why.** Hovering (or focusing, or first-tapping) a product
  makes the master thread leave its rail, travel to the product's
  frame, and **loop once around it** — a full circuit of the frame's
  perimeter — before returning to the rail and continuing down the
  page. It belongs because it is the theme's answer to the hover
  state: instead of the card lifting, shadowing or zooming (every
  other shop on the internet), *the thread itself reaches out and
  handles the piece the visitor is considering.* The loop is also
  information: a looped product is the page's way of saying "this one
  is in your hand now," and §6.14's cards key their selected state to
  it.
- **Structure.** Each product frame carries a pre-authored loop detour
  in the master path's survey (§6.2): at the frame's height, the path
  leaves the rail, traces the frame's perimeter at a 10px offset
  (outside the frame, on the cloth), and rejoins the rail. The loop is
  not a separate element — it is a sub-range of the one path, addressed
  by its length interval. At rest (visitor has scrolled past but not
  hovered), the draw (§6.2) passes *through* the detour's endpoints on
  the rail line, skipping the circuit; on hover, the sub-range's local
  draw animates the circuit. Implementation: the detour is a cloned
  overlay path (same geometry, `aria-hidden`) whose dash draw is
  driven locally, so the master draw is never disturbed — the thread
  appears to loop while its spine keeps its place. The clone is
  removed from the DOM when the loop completes or is cancelled.
- **Motion spec.** Trigger: pointerenter / focus-within on the product
  card; on touch, first tap (the tap that would navigate is held —
  §6.14's two-tap rule). Circuit: the loop draws around the frame over
  **700ms `--ease-silk`**, starting at the frame's top-left corner
  (where the thread arrives from the rail) and running clockwise in
  LTR (counter-clockwise in RTL — the loop follows reading direction).
  Hold: the completed loop rests around the frame for as long as hover
  lasts, with the thread's contact shadow deepening 18% → 26% (the
  loop lies *on* the cloth, pressed by attention). Release: on
  pointerleave, the loop un-draws in reverse over **420ms
  `--ease-settle`** — faster than it drew, the way a hand lets go
  quicker than it reaches. Only ONE loop may exist on the page at any
  moment; entering a second product cancels the first instantly (no
  un-draw — the thread is needed elsewhere).
- **Choreography timeline (v2).** t+0: pointer enters the card →
  t+60ms: intent delay passes (a skim across a row of cards must not
  fire three loops) → t+60ms: the overlay path is inserted, dash at 0
  → t+60–760ms: the circuit draws clockwise from top-left →
  t+760ms: circuit complete; the frame's caption (§3: captions live
  inside the loop) settles 120ms later → hold: loop rests, shadow at
  26% → pointer leaves → t+0–420ms: reverse un-draw → t+420ms: overlay
  removed; the rail line is unbroken throughout.
- **State matrix (v2).** *Rest:* no loop; the thread passes on the
  rail. *Drawing:* 700ms circuit. *Looped (hover held):* full circuit,
  deepened shadow; the card's price fray (§6.6), if the card carries
  one, is unaffected — loop and fray coexist (the hand holds the piece
  while the thread stays honest about its price). *Focus-within:*
  identical to hover — keyboard visitors get the full loop, drawn at
  the same 700ms. *Active (click during loop):* the loop completes
  instantly and §6.9's cinch or navigation proceeds — the loop never
  delays an action. *Scrolled-past:* loops never run off-screen; a
  card leaving the viewport mid-draw cancels to rest. *Touch:* first
  tap draws the loop (420ms, the shorter touch circuit below) and
  shows the card's actions; second tap activates. *Disabled (card out
  of stock):* the loop draws only **three-quarters** of the circuit
  and stops, the open quarter facing the rail — the thread reaches for
  the piece and cannot take it; the card's "sold / awaiting the next
  dye lot" text (§12) says in words what the open loop says in line.
- **Content merge.** The loop is drawn around the product's actual
  frame at its actual size — a tall scarf and a square cushion get
  differently shaped loops because the survey traces each frame. The
  caption sits inside the circuit. Remove the product and its detour
  leaves the survey with it (§6.2's geometry check). This is the
  test the element passes and a generic "card hover glow" fails: the
  animation's geometry IS the content's geometry.
- **Failure fallback.** No-JS / no-hover: no loop exists and nothing is
  missing — the product is fully presented, priced and purchasable
  without ever being looped. If the overlay path fails to insert
  (DOM error), the card falls back to §6.14's border-weight hover
  (2.5px → 3.5px `--gold-ink`) so focus and hover remain visible by
  other means. A 1000ms watchdog removes any loop overlay whose
  animation has not completed — a stuck half-loop around a product is
  worse than none.
- **Reduced-motion variant.** No draw, no un-draw. On hover/focus the
  completed loop appears instantly around the frame (opacity step, no
  travel) and disappears instantly on leave. The three-quarter loop
  for unavailable pieces is likewise instant. The information — *this
  piece is in hand; that one cannot be taken* — survives intact.
- **Breakpoints (v2).** ≥1200px: full circuit at 10px offset, 700ms.
  768–1199px: three-quarter circuit (the rail side stays open — the
  narrower rail cannot spare the thread for a full detour), 600ms,
  offset 8px. <768px: no circuit — the thread's in-gutter segment
  beside the card thickens 2px → 3.5px and a single fibre underline
  draws under the card's title (300ms); touch two-tap rule unchanged.
- **Edge cases & failure modes (v2).** *Pointer skims a grid
  diagonally:* the 60ms intent delay + one-loop rule means at most one
  loop is ever drawing; skims fire none. *Card resizes mid-loop
  (image loads late):* the overlay path is re-fitted to the frame's
  new box on the next frame; if the frame moved >40px, the loop
  cancels to rest rather than tracing a ghost of the old box.
  *Rapid hover cycling between two cards:* each entry restarts cleanly;
  overlays are pooled (max 1 in DOM). *Loop during the knot pin
  (§6.4):* products do not appear inside the pinned CTA section, by
  layout law (§4 density) — the conflict is designed out, not handled.
- **Accessibility spec (v2).** The loop is decorative emphasis on an
  already-labelled card: the card's link/button carries its full name
  ("Mulberry scarf, 180 × 70 cm — view") regardless of loop state.
  Focus-visible uses the loop PLUS §6.14's outline, never the loop
  alone (2.03:1 gold cannot be a sole focus indicator). The unavailable
  three-quarter loop is always paired with real text (§12) — the line
  never carries the message alone. Touch targets: the whole card,
  ≥44px in both dimensions by construction.
- **Performance budget & mobile variant.** One overlay path, one dash
  animation, compositor-only; pooled to a single instance. Budget:
  ≤0.2ms/frame while drawing. Mobile: the gutter variant above — no
  overlay path at all below 768px.
- **Tokens consumed (v2).** `--gold`, `--gold-ink`, `--thread-shadow`,
  `--ease-silk`, `--ease-settle`, `--loop-dur` (700ms), `--loop-out`
  (420ms), `--intent-delay` (60ms).

### 6.4 CTA knot tightening — commitment, tied

- **What & why.** The page's one pinned scene and its conversion
  point. As the visitor scrolls into the call-to-action section, the
  section pins and the master thread — which has travelled the whole
  page to get here — gathers itself beside the CTA into a loose loop
  and then, scrubbed to the pin's scroll, **tightens into a visible
  knot**: its loops shrink, its crossing pulls through, and it comes
  to rest as a tied knot with two short ends. It belongs because
  commitment in this theme is not a button colour change; it is the
  thread the visitor has followed since the first screen *tying
  itself off at the ask*. The knot is also the theme's thesis about
  conversion: nothing is taken, something is joined — the visitor's
  thread and the house's thread become one knot.
- **Structure.** The CTA section is a 260vh scroll chapter containing
  a 100vh sticky stage. Centred on the stage (the page's one centred
  composition, §4): the knot — a pre-authored sub-range of the master
  path drawn as three nested loop states (loose: loop radius 54px;
  gathering: 38px; tied: 22px with the crossing pulled through and two
  26px ends) — flanked by the CTA copy and the single action button.
  The knot's three states are three authored path geometries; the
  scrub interpolates dash-draw and a scale on the knot group (1 →
  0.86) rather than morphing path data, so the knot never dissolves
  into spaghetti mid-scrub. The button sits inside the knot's final
  radius's reading position — at rest, the tied knot frames the
  button's left edge, tying the action into the knot visually.
- **Motion spec.** Trigger: scroll through the pin. Pin length 160vh
  of travel (260vh chapter − 100vh stage). Scrub mapping: pin progress
  q 0–0.35 → the thread arrives and the loose loop forms (dash-draw of
  the loop sub-range); q 0.35–0.8 → the loops shrink (group scale
  1 → 0.88, loop sub-ranges cross-fade loose → gathering → tied
  geometries at q 0.5 and q 0.7); q 0.8–1.0 → the final cinch: scale
  0.88 → 0.86 with `--ease-cinch`'s overshoot applied as a 120ms
  end-beat when q first reaches 1, and the button inks from `--cocoon`
  outline to solid `--madder` (§6.9 owns the click itself; this is the
  scroll-side readiness). All values written by the shared loop (lerp
  0.12). Scrolling back up **reverses symmetrically until q 0.8** —
  the knot loosens as the visitor withdraws, which is honest — but
  once the cinch beat has fired (q reached 1), the knot stays tied for
  the rest of the session: a commitment witnessed is not unwitnessed
  by scrolling away.
- **Choreography timeline (v2).** Spatial (pin progress q): q=0 —
  stage pins, thread arrives from the rail, no loop yet, CTA copy at
  rest → q=0.2 — loose loop half-drawn → q=0.35 — loose loop complete
  (radius 54px), copy's first line settles (thread-first rule, §5) →
  q=0.5 — gathering geometry crosses in, scale ≈0.93 → q=0.7 — tied
  geometry, scale ≈0.88, the crossing visibly pulled through →
  q=0.85 — the two ends shorten to 26px → q=1.0 — cinch beat (120ms),
  button inks madder, pin releases over the following 40vh of chapter
  tail → the thread continues from the knot toward the footer (§6.7)
  — tied, but not ended: the page still has its ending to make.
- **State matrix (v2).** *Approaching (q<0):* ordinary section,
  thread in rail. *Forming:* q 0–0.35 as above. *Tightening:*
  q 0.35–1. *Tied (terminal, post-cinch):* knot at rest, button
  madder; persists on scroll-back (above). *Hover (on the button):*
  the knot leans ≤6px toward the pointer (§5 magnetic rule) and the
  button's madder deepens to `--madder-deep`. *Focus (button):*
  knot lean + focus ring on the button (§6.15's form rules apply to
  the action). *Active:* §6.9's cinch click. *Touch:* identical scrub
  (the pin is scroll-driven, not pointer-driven); the chapter is
  220vh on touch (below). *Disabled (button disabled — e.g. the
  booking window is closed):* the knot forms but does NOT cinch; at
  q=1 it rests at the gathering geometry (scale 0.90, loops open) and
  the §12 closed-window line appears — the thread will not tie a knot
  around an action that cannot be taken.
- **Content merge.** The knot is tied *around the page's actual ask*:
  the button it frames is the conversion, the copy it gathers beside
  is the offer. The thread has carried the visitor through every
  section to reach this point — its arrival is the journey, its knot
  is the decision. A CTA section without the knot is just a button;
  the knot without a real action behind it is the one decoration this
  theme forbids itself (§10 gate: the knot's button must perform a
  real conversion — signup, booking, order — never a newsletter
  checkbox dressed as commitment).
- **Failure fallback.** No-JS: the section is unpinned, the knot ships
  in its **tied** geometry in the DOM (the finished state), the button
  is madder and functional. Pin unsupported (old browser): same —
  the chapter collapses to a normal section with the scrub replaced by
  an IntersectionObserver one-shot that sets the tied state at 50%
  visibility. Watchdog: if the shared loop stalls for 1500ms inside
  the pin, the knot snaps to the geometry matching the last known q —
  never leaves a half-morphed knot on screen.
- **Reduced-motion variant.** No pin, no scrub. The section stands as
  an ordinary section with the knot already tied beside the button —
  the finished state, chosen at build time in the DOM, not reached by
  animation. The disabled-state open knot (§ above) is likewise a
  static authored geometry.
- **Breakpoints (v2).** ≥1200px: as specced (260vh chapter, radii
  54/38/22px). 768–1199px: chapter 240vh, radii 46/33/19px, knot stage
  offset left of centre by the narrower rail. <768px: chapter 200vh,
  radii 38/27/16px, knot above the button rather than framing its edge
  (a phone stage has no flank to spare), cinch beat kept — the one
  beat that must survive every size, because it is the point.
- **Edge cases & failure modes (v2).** *Visitor flings past the whole
  chapter:* q jumps to 1; the cinch beat fires once (it is a state
  arrival, not a scroll performance) and the knot is tied — flinging
  is also a way of arriving. *Visitor enters the chapter from below
  (anchor link to the footer, scrolls up):* the knot is encountered
  tied (if cinched) or gathering; the scrub is a pure function of q
  until the cinch latch, so no impossible states exist. *Two CTAs on
  one page:* forbidden by the density law (§4) — one knot per page;
  secondary actions use §6.15's form submit or plain buttons and the
  thread passes them in the rail without gathering. *The conversion is
  a long form, not a button:* §6.15 governs; the knot chapter then
  precedes the form as the commitment moment and the form's own submit
  performs §6.9's cinch at smaller scale.
- **Accessibility spec (v2).** The knot is `aria-hidden`; its state is
  duplicated in words — the section's apparatus label reads "THE KNOT
  IS TIED" / "THE KNOT WAITS" (§12 fixed strings) and updates at the
  cinch, politely, once. The button is a real `<button>`/link with its
  action named ("Book the dyeing workshop — Saturday sittings"), never
  "click here". Focus order: copy → button → onwards; the pin never
  traps focus (sticky, not fixed). The madder button on silk: 9.15:1
  ✓; its label in `--silk` on `--madder`: 9.15:1 ✓.
- **Performance budget & mobile variant.** One sticky stage, one SVG
  group transform + two crossfading sub-ranges — compositor work only,
  ≤0.3ms/frame from the shared loop. No layout inside the pin. Mobile:
  the reduced chapter/radii above; crossfades become a single geometry
  swap at q 0.6 on devices measuring <40fps.
- **Tokens consumed (v2).** `--gold`, `--madder`, `--madder-deep`,
  `--thread-shadow`, `--ease-cinch`, `--ease-silk`, `--loop-lerp`
  (0.12), `--knot-r` (54px / 38px / 22px), `--pin-len` (160vh).

### 6.5 Unspooling word — type spun from thread

- **What & why.** One italic Cormorant word in the hero headline —
  the word the page most wants to be remembered by — does not simply
  appear. Its letters arrive **one by one along a shallow curve**,
  each letter travelling the thread's own path into its place in the
  word, as if the word were being spun off the spool letter by letter.
  It is the theme's single licensed piece of kinetic type (§5), and it
  belongs because it states the whole metaphor inside the typography:
  *the words on this page are made of the same stuff as the line
  running down its margin.* One word per page. A second unspooling
  word anywhere is a gate failure — a spool that performs twice is a
  trick, not a material.
- **Structure.** The chosen word is a `<span class="unspool-word">`
  inside the hero H1, its letters wrapped in per-letter spans by the
  build (server-side, so the DOM ships whole). Each letter carries a
  pre-authored offset along a shallow curve — the curve is a 120px
  segment of the master thread's geometry extended: letters start
  displaced along the thread's direction of travel (from the reading
  start, above the baseline by up to 10px, following the thread's
  underline run) and settle into the word's normal typeset positions.
  The full word is the DOM's text from first paint; the per-letter
  transforms are JS-armed only, and the word's accessible name is the
  whole word on the heading, never letter salad.
- **Motion spec.** Trigger: the thread drop's arrival (§6.1) — letters
  may not begin before the thread has settled under the headline
  (t+700ms at the earliest). Each letter: **90ms stagger** in reading
  order (RTL reverses), travelling its curve offset → 0 over **460ms
  `--ease-spool`**, opacity 0.25 → 1 (letters are never fully
  invisible — §5's no-stranding rule applies to type too; a letter at
  0.25 is a letter not yet spun tight, not a hidden letter). A 5-letter
  word completes in ~820ms; the law caps the word at 9 letters (a
  longer word is re-chosen at copy time, §12 — the copywriter picks a
  word the spool can spin). As each letter lands, the thread's
  underline beneath it (§6.2) draws its corresponding segment — letter
  and line arrive together, beat for beat.
- **Choreography timeline (v2).** t+0 = §6.1 settle begins → t+120ms:
  letter 1 leaves its curve offset → t+120–580ms: letter 1 travels →
  each subsequent letter starts +90ms → final letter lands at
  t+120 + 90×(n−1) + 460ms → t+completion: the word is ordinary type
  from here; the per-letter spans keep their transforms at 0 and are
  never animated again, by any later event, on any scroll. The word
  unspools **once per session**; return loads show it set.
- **State matrix (v2).** *Set (default / no-JS / return visit):* the
  word as normal headline type. *Unspooling:* letters in transit,
  460ms each, staggered. *Landed (terminal):* set, permanently.
  *Hover/focus:* none — the word is headline text, not a control; it
  never re-performs for attention. *Scrolled-past:* set. *Disabled:*
  n/a. Touch identical to desktop (the trigger is the drop, not the
  pointer).
- **Content merge.** The word is the headline's own most important
  word — chosen by the copy rules (§12: the word that names the craft
  or the promise — "unspooled", "hand-dyed", "woven") — and its
  letters travel along the thread's actual curve into the headline
  the thread underlines. It is not a text effect applied to a word;
  it is the word being manufactured from the page's material, in the
  place the material passes.
- **Failure fallback.** The word ships set in the DOM. JS arms the
  offsets only if it can also run the settle (the same code path); a
  1200ms watchdog from arming forces all letters to offset 0 / opacity
  1. If `fonts.ready` resolves late (>900ms), the unspooling is
  skipped — late-loading Cormorant would change letter widths mid-
  travel and a travelling letter that changes shape is a broken spool.
- **Reduced-motion variant.** The word is set. No travel, no stagger,
  no opacity ramp. (This is the theme's most-refused element under
  reduced motion: kinetic type is precisely what the preference
  exists to still.)
- **Breakpoints (v2).** ≥1200px: as specced (curve offset up to 120px
  travel, 10px rise). 768–1199px: travel ≤80px, stagger 80ms.
  <768px: travel ≤44px, rise ≤6px, stagger 70ms, duration 380ms — the
  word still spins, briefly, within the smaller stage; if the hero
  headline wraps so the word sits on line 2, offsets are computed from
  the word's own box (the curve is relative to the word, never to the
  page).
- **Edge cases & failure modes (v2).** *The chosen word contains a
  ligature or accented glyph that cannot split:* the word is re-chosen
  (§12) — letters are split only on grapheme boundaries that render
  identically joined and apart; if any letter renders differently
  alone (Arabic-script headlines, Indic conjuncts), the element is
  disabled for that locale and the word ships set — the theme yields
  to the script, always. *Word at a line-break boundary:* spans are
  `display: inline-block` per letter which forbids intra-word breaks;
  the headline's wrap points are authored around it. *Slow font swap
  mid-word:* covered by the fonts gate above.
- **Accessibility spec (v2).** The heading's accessible name is the
  full sentence with the word whole (`aria-label` on the H1 or the
  word span marked `aria-label="<word>"` with letter spans
  `aria-hidden`). Screen readers never meet the letters separately.
  The opacity floor (0.25) is a visual state only; contrast of the
  settled word is the headline's own (§3, `--cocoon` on `--silk`
  12.77:1 ✓ — the unspooling word is set in `--cocoon` italic, NOT in
  gold: gold italic at display size was the original sketch and it
  fails contrast law, §2).
- **Performance budget & mobile variant.** ≤9 transformed spans for
  <1s, once per session; transforms only, no layout thrash (letters
  are measured once at arm time). Mobile: reduced travel above; on
  <40fps devices the stagger compresses to 40ms and travel to a pure
  120ms fade-settle per letter.
- **Tokens consumed (v2).** `--cocoon`, `--ease-spool`, `--unspool-step`
  (90ms), `--unspool-dur` (460ms), `--watchdog-unspool` (1200ms).

### 6.6 Frayed honesty — the thread frays where money is asked

- **What & why.** The theme's signature detail, carried over from the
  original entry word for word in intent: **wherever the page asks for
  money — a price, a booking total, a deposit — the master thread
  visibly frays.** Three to four fine fibre strokes separate from the
  main line beside the figure, splay outward by 1–3px, and tremble
  very slightly, for as long as the figure is on screen. It belongs
  because it is the theme's ethics made visible: machine-perfect silk
  at the exact point of transaction would be a lie about a handmade
  thing, so the thread admits its nature precisely where a lesser
  theme would polish hardest. The fray is also functional — it is the
  page's price marker. A visitor scanning for the cost finds the place
  where the thread comes undone, and §6.14's cards and §6.15's form
  both rely on it as the money's address.
- **Structure.** At each money point, the master path's survey (§6.2)
  includes a **fray zone**: the main line continues unbroken (the law:
  the thread never breaks — it frays, which is different), and 3–4
  additional fibre paths (`--fibre` stroke, 1px) branch from the main
  line at the zone's start, splay to offsets of +1.5px, +2.5px, +3px
  (one fibre at −1.5px on the other side — fray is not symmetric) over
  a 60–90px run beside the figure, and rejoin or taper out at the
  zone's end. Each fibre is a separate short path in the same SVG.
  The figure itself (price, total) is ordinary DOM text in `--gold-ink`
  tabular Karla (§3) positioned so the fray zone runs along its
  reading-start edge with the §1 16px glyph clearance. A fray caption
  in the Weaver's italic (§12) sits within 24px of every fray zone —
  the honesty is captioned, never left as a puzzle (e.g. *"the thread
  frays here — this piece is priced by the hour at the loom"*).
- **Motion spec.** Trigger: the money figure's first entry into the
  viewport (IntersectionObserver, threshold 0.4). The fibres separate
  over **500ms `--ease-silk`**: offsets grow 0 → their splayed values
  in stagger (fibre 1 at t+0, fibre 2 at t+70ms, fibre 3 at t+140ms,
  fibre 4 at t+210ms) — the fray *unspools slightly*, it does not pop.
  Tremble: once separated, each fibre carries a ±0.6px sine tremble,
  periods 2.6s / 3.1s / 3.7s (deliberately non-harmonic so the fray
  never pulses in unison — unison reads as vibration, i.e. a machine),
  amplitude halved at the fibre's anchored ends. The tremble is the
  theme's smallest ambient motion and its most rationed: it exists
  ONLY inside fray zones. When the figure leaves the viewport, the
  tremble pauses (observer) but the fibres stay separated — a price
  once seen does not re-perfect itself when scrolled back to.
- **Choreography timeline (v2).** t+0: figure crosses 40% visibility
  → t+0–500ms: fibres separate in stagger → t+500ms: tremble begins
  (phase-offset per fibre) → hold: tremble continues while the figure
  is in view → figure exits: tremble pauses within one frame →
  re-entry: tremble resumes, separation does not repeat → the main
  line's draw (§6.2) passes through the zone unaffected throughout —
  fray and draw are independent systems sharing one SVG.
- **State matrix (v2).** *Unfrayed (figure never yet seen):* main line
  only — the honest pre-state, and the permanent state under no-JS.
  *Separating:* 500ms staggered splay. *Frayed (terminal):* fibres
  splayed, trembling in view, still out of view. *Hover (on the
  figure or its card):* the tremble amplitude eases to ±0.3px — the
  thread steadies slightly under attention, the way a hand steadies
  what it is about to touch; the separation does not change. *Focus
  (figure inside a focused control, e.g. the form's total, §6.15):*
  same steadying. *Scrolled-past:* frayed, paused. *Disabled:* a
  money point that is not currently real (a sold piece's struck price)
  does NOT fray — fray marks a live ask; a dead price gets §6.14's
  plain strike and no fibres.
- **Content merge.** The fray exists only where a real figure exists,
  is positioned by that figure's box, and is captioned by words about
  that figure's pricing. It cannot be placed decoratively: the build's
  geometry check (§10) requires every fray zone to be anchored to a
  money element in the DOM, and counts them — a page with a fray and
  no price fails; a price with no fray fails the other way. This
  two-way audit is the strongest content-merge guarantee in the theme.
- **Failure fallback.** No-JS: no fibres are in the DOM (they are
  JS-inserted into the SVG), prices stand plainly — the page loses its
  confession and keeps its commerce, which is the correct order of
  losses. If the observer never fires (edge-case browsers), a 1500ms
  fallback separates all fray zones in view at load. Fibres are pure
  stroke paths: no canvas, no filter, nothing to fail expensively.
- **Reduced-motion variant.** The fibres appear **already separated**,
  perfectly still — no stagger, no tremble, ever. The honesty is in
  the splay, not the shake; reduced motion keeps the meaning and
  removes only the tremble. (This element's reduced variant is a
  designed state, not an absence — the fray must survive it, because
  the fray is content.)
- **Breakpoints (v2).** ≥1200px: 4 fibres, splay to 3px, zone 90px
  beside the figure. 768–1199px: 3 fibres, splay to 2.5px, zone 72px.
  <768px: the fray moves into the 28px gutter at the figure's height
  (the figure has no side room on a phone), 3 fibres, splay to 2px,
  zone 56px, caption below the figure instead of beside it.
- **Edge cases & failure modes (v2).** *Many prices on one screen
  (a listing grid):* the density law (§4) caps fray zones at **2 per
  viewport height**; in a grid, only the first two money points in
  reading order fray and the rest carry the caption's short form
  ("frayed at the first price, above") — a wall of trembling fibres
  is anxiety, not honesty. §6.14's listing rule implements this.
  *Price changes dynamically (quantity selector):* the figure updates
  (§6.10's measured count), the fray does not re-separate — it is
  already honest about the new number. *Currency/localisation moves
  the figure:* the zone is anchored to the figure's box at survey
  time and re-anchored on the §6.2 re-survey; a zone that cannot find
  its figure removes itself rather than fraying at nothing.
  *Tremble and photosensitivity:* ±0.6px at ~0.3Hz is orders below any
  flash/vestibular threshold; the tremble is sub-pixel-class motion,
  and it still pauses off-screen and dies under reduced motion.
- **Accessibility spec (v2).** Fibres are `aria-hidden`. The fray's
  meaning is carried by its caption (§12), which is real text adjacent
  to the figure and read in normal order — a screen-reader visitor
  gets the honesty in words ("priced by the hour at the loom") exactly
  where a sighted visitor gets it in line. The figure's contrast is
  `--gold-ink` on its ground (5.88:1 on silk ✓, 5.24:1 on silk-deep ✓).
  Tremble never applies to the figure itself — numbers do not shake on
  this page, only thread does.
- **Performance budget & mobile variant.** ≤4 short paths per zone,
  ≤2 zones animating per viewport; tremble is a transform on path
  groups (compositor) at ≤0.15ms/frame total. Zones beyond the second
  in a viewport are static-separated (no tremble). Mobile: gutter
  variant above; tremble amplitude ±0.4px.
- **Tokens consumed (v2).** `--fibre`, `--gold`, `--gold-ink`,
  `--ease-silk`, `--fray-dur` (500ms), `--fray-stagger` (70ms),
  `--tremble-amp` (0.6px), `--fray-max-per-view` (2).

### 6.7 Fibre sway — the loose end

- **What & why.** Below the last content section, before the sampler,
  the master thread runs out — and its final 180px hangs as a **loose
  end**: the main line plus two separated fibres, swaying continuously
  and gently, ±6px on a 5s sine, the fibres lagging the main line the
  way real fibres trail a thread in still air. It belongs because it
  is the page's proof of life at the exact spot reading ends: every
  other element on the page is driven by the visitor's scroll or hand,
  but the loose end moves on its own, because a real thread in a real
  room is never perfectly still. It is also a promise kept — the
  thread that entered with a swing (§6.1) leaves with a sway; the
  page's first and last motions rhyme.
- **Structure.** The terminal sub-range of the master path (§6.2): the
  final 180px of surveyed path, drawn as a gentle hanging curve below
  the last section's foot, plus two fibre paths (`--fibre`, 1px) that
  branch at 40px and 90px along the loose end and run 70px and 46px
  respectively before tapering. The whole group is one SVG `<g>`
  transformed by the shared loop (the sway is a transform, not a path
  redraw — the geometry never changes, only its lean). The group hangs
  in the footer's open cloth (§4: the last 100vh is composed as an
  ending), clear of the sampler (§6.8) which sits below-right of it.
- **Motion spec.** Trigger: time — ambient, begins when the loose end
  first enters the viewport, never before (a sway nobody can see is
  not run). Main line: rotate ±1.1° about the group's top anchor ≈
  ±6px at the tip, sine period **5000ms**, `--ease-swing` phase.
  Fibre 1 lags the main line's phase by **0.4s** and sways ±4px;
  fibre 2 lags by **0.8s**, ±2.5px — the lag cascade is the whole
  effect; fibres moving in unison with the line read as a rigid
  banner, not silk. Amplitude breathes very slightly (a 23s secondary
  sine modulating amplitude 0.8–1.0) so the motion never becomes a
  metronome the eye can predict and then resent. Pauses when the group
  is off-screen (observer) and when the tab is hidden.
- **Choreography timeline (v2).** Continuous; t+0 = group enters view
  → sway fades in over 1200ms (amplitude 0 → full, so the end never
  *starts* moving abruptly) → steady state: main ±6px / 5s, fibres
  lagging → when §6.8's sampler begins (group scrolled further), the
  sway continues unchanged — the two footer acts are neighbours, not
  a sequence → when the tie-off knot (§6.8) completes, the sway
  amplitude halves over 2000ms and holds at half: a tied thread still
  breathes, but it is held now. That halving is the page's last
  motion beat.
- **State matrix (v2).** *Still (pre-view / no-JS):* the loose end
  hangs at rest geometry — complete and correct. *Swaying:* as
  specced. *Tied (post-§6.8):* half amplitude, same periods. *Hover:*
  none — the loose end is not interactive; reaching for it does
  nothing, which is right: it is the end of the thread, not a handle.
  *Focus:* not focusable. *Scrolled-past:* paused off-screen.
  *Disabled:* n/a. Desktop and touch identical (ambient motion does
  not care about pointers).
- **Content merge.** The loose end is the master thread's own end —
  the same path the visitor has followed for the whole page, arriving
  at its terminus. Its sway is not an animation applied to the footer;
  it is the subject of the entire page, at rest, in the place the
  layout (§4) reserves for the ending. Remove the page's thread and
  there is nothing here to sway.
- **Failure fallback.** The group ships at rest geometry in the DOM;
  the sway is a loop-written transform on top. Loop failure = a still
  loose end, which is indistinguishable from a calm room. No watchdog
  is needed because the fallback state is the DOM state.
- **Reduced-motion variant.** Perfectly still, forever — including
  after the tie-off. This element and §6.5 are the theme's two total
  refusals under reduced motion: ambient motion for its own sake is
  exactly what the preference declines.
- **Breakpoints (v2).** ≥1200px: loose end 180px, sway ±6px as
  specced. 768–1199px: 150px, ±5px. <768px: 120px, ±4px, fibre 2
  dropped (two lines read clearly at phone width; three tangle) —
  amplitude also halves at the tie-off as specced, from the smaller
  base.
- **Edge cases & failure modes (v2).** *Short page (the loose end is
  in view at load):* the sway fades in after the §6.1 drop settles —
  the page never runs two signature motions at full amplitude in the
  same first screen; the drop wins, the sway waits its 1800ms.
  *Battery-saver / throttled rAF:* the loop's sine is computed from
  wall-clock time, not frame count, so a throttled tab sways slowly
  and correctly rather than stuttering. *The visitor never scrolls to
  the footer:* the sway never runs — budget respected by the observer
  gate.
- **Accessibility spec (v2).** `aria-hidden` group; nothing is
  announced, nothing is focusable, no information rides on the sway.
  The tie-off's completion (which halves the sway) is announced by
  §6.8's own text, not by this element.
- **Performance budget & mobile variant.** One group transform per
  frame while in view: the cheapest element on the page (≤0.05ms).
  Mobile: the reduced geometry above; the 23s amplitude-breathing
  modulation is cut on <40fps devices (steady amplitude instead).
- **Tokens consumed (v2).** `--gold`, `--fibre`, `--ease-swing`,
  `--sway-amp` (6px), `--sway-period` (5000ms), `--sway-lag-1`
  (0.4s), `--sway-lag-2` (0.8s).

### 6.8 Footer sampler & tie-off — the thread ends by being woven

- **What & why.** The master thread's destination. When the footer
  enters, a small woven sampler — a rectangle of crossing warp and
  weft strokes, 220×160px — **draws itself line by line**, and as its
  last weft line completes, the master thread arrives at the sampler's
  top corner and **ties off into it with a final knot**: a small,
  still version of §6.4's knot, tied once, forever. The sampler is the
  page's colophon made cloth: woven into it, in the sampler tradition,
  are the house's mark, the year, and a line of the Weaver's italic
  worked as if stitched (§12's fixed tie-off line). It belongs because
  a thread that simply stops at the footer would break the law's
  spirit — the thread must *end the way threads end*: tied, and put
  to work in a piece of weaving. The sampler also closes the theme's
  argument: the page began with a single filament (§6.1) and ends with
  cloth — the whole journey from thread to textile, performed by one
  line.
- **Structure.** An inline SVG, 220×160px (≥1200), set in the footer
  on its own `--silk` ground in both colour schemes (§2: the swatch
  pinned to the wall). Warp: 11 vertical strokes in `--leaf` (the
  mulberry leaf warp — the leaf feeds the worm, the worm spins the
  thread; the sampler's structure is the food, its weft is the silk);
  weft: 9 horizontal strokes in `--gold`, woven — each weft stroke is
  drawn as alternating over/under segments at the warp crossings, the
  alternation flipping each row, so the drawing is a true plain weave
  and not a grid laid over lines. The house mark and year are set as
  stitched text (Cormorant, letterspaced 0, rendered as short dash
  strokes along the glyph shapes is FORBIDDEN — fake stitch text is
  clip-art; instead the mark is typeset in `--leaf-deep` Cormorant
  italic *inside* the sampler's border, the way a woven label is
  woven in, §12). The tie-off: the master path's final sub-range
  (§6.2) terminates at the sampler's top-left corner, where a 14px
  knot group (two loop geometries, loose → tied) mirrors §6.4 at
  keepsake scale.
- **Motion spec.** Trigger: sampler crosses 50% visibility. Weaving:
  warp strokes draw first, top to bottom of the loom — each 140ms
  `--ease-spool`, staggered 45ms, total ≈ 500ms — then weft rows draw
  left to right in reading order, each row **260ms `--ease-spool`**,
  staggered 120ms, total ≈ 1.2s; the over/under alternation is in the
  authored path data, so the "weaving" is the drawing order itself.
  Tie-off: when the final weft row completes, the master thread's last
  segment draws into the corner (300ms `--ease-silk`) and the knot
  group cinches (scale 1 → 0.82 → 1, **380ms `--ease-cinch`** — the
  same beat as §6.9, the theme's one gesture of finality, at keepsake
  scale). Simultaneously §6.7's sway halves. The weaving runs **once**;
  it never re-weaves on re-entry (a woven sampler does not unweave
  because you looked away).
- **Choreography timeline (v2).** t+0: sampler 50% visible → t+0–500ms:
  warp draws (11 strokes, 45ms stagger) → t+500ms: a 160ms held beat —
  the loom is warped, the weft has not begun; the pause is authored,
  not a gap → t+660–1860ms: weft rows draw (9 rows, 120ms stagger) →
  t+1860ms: final row completes → t+1860–2160ms: the master thread's
  tail draws into the corner → t+2160–2540ms: the knot cinches →
  t+2540ms: §6.7's sway begins its 2000ms halving; the footer's
  ordinary furniture (§6.17) settles in thread-first order below —
  the page is finished, and only then does its paperwork appear.
- **State matrix (v2).** *Unwoven (pre-trigger / no-JS — see
  fallback):* see below; the DOM question is decided by the fallback
  rule. *Weaving:* as specced, non-interactive. *Woven (terminal):*
  the sampler complete, knot tied, static forever. *Hover:* the
  sampler is not a control; hovering it does nothing (it is a made
  thing, not a button). *Focus:* not focusable; its woven-in text is
  duplicated as real footer text for AT (below). *Scrolled-past:*
  woven state persists. *Disabled:* n/a. Touch identical.
- **Content merge.** The sampler is the footer's content, not its
  decoration: it carries the house mark, the year, and the tie-off
  line — the colophon information every footer must state, stated in
  cloth. And the master thread's arrival is surveyed geometry (§6.2):
  the draw that measured the visitor's whole reading terminates *in
  this corner*, so the sampler is where the progress indicator
  physically ends. A footer sampler pasted onto a page whose thread
  does not arrive at it is precisely the failure §10 audits for.
- **Failure fallback.** The sampler ships **woven** in the DOM (all
  strokes at full draw, knot tied) — JS rewinds it to unwoven only
  when it can run the weaving (same arm-and-run rule as §6.5). No-JS
  visitors see the finished sampler and a tied thread, which is the
  correct complete footer. Watchdog: any stroke still undrawn 2000ms
  after the trigger snaps to drawn — a half-woven sampler left by a
  stalled observer is finished by the watchdog, not left as a ruin.
- **Reduced-motion variant.** The sampler is woven and the knot tied,
  statically, from first paint. No draw, no cinch. The finished cloth
  is the variant.
- **Breakpoints (v2).** ≥1200px: 220×160px, 11 warp / 9 weft as
  specced. 768–1199px: 190×140px, 9 warp / 8 weft (the weave coarsens
  honestly at smaller size rather than drawing hairlines). <768px:
  160×120px, 8 warp / 7 weft, stagger compressed (warp 30ms, weft
  rows 90ms, total weave ≈ 1.4s), tie-off unchanged — the knot is the
  same size at every breakpoint (14px group), because an ending does
  not shrink.
- **Edge cases & failure modes (v2).** *Footer reached by anchor jump
  (thread snapped to 100%, §6.2):* the sampler still weaves on entry —
  the visitor teleported past the journey but the ending is still
  made in front of them; only if the sampler is already woven does
  nothing happen. *Print:* the sampler prints woven; the tie-off knot
  prints tied; the sway (§6.7) prints at rest. *The year in the
  sampler:* it is the current year at build/publish, typeset as
  content — never computed by script at view time (a sampler that
  re-weaves its date nightly is a clock wearing a costume).
- **Accessibility spec (v2).** The SVG sampler is `aria-hidden`; its
  information content (house mark, year, tie-off line) is present as
  real text in the footer's colophon line immediately below it
  (§6.17) — "Woven and tied by [House], [Year]." — so nothing is
  SVG-only. The weaving is never announced. Contrast of the woven-in
  label: `--leaf-deep` on `--silk` 5.22:1 ✓ (and the duplicate text
  uses `--cocoon`, 12.77:1 ✓).
- **Performance budget & mobile variant.** 20 short stroke animations,
  once per page, dash-based, ≤0.2ms/frame during the ~2.5s sequence.
  Mobile: the coarser weave above; stroke widths rise 1.5px → 2px so
  the weave reads at arm's length.
- **Tokens consumed (v2).** `--gold`, `--leaf`, `--leaf-deep`,
  `--fibre`, `--ease-spool`, `--ease-silk`, `--ease-cinch`,
  `--weave-warp` (140ms), `--weave-weft` (260ms), `--tie-off-dur`
  (380ms), `--watchdog-weave` (2000ms).

### 6.9 Knot cinch click — the hand tightens what the scroll tied

- **What & why.** Clicking the CTA (or the order form's submit, §6.15)
  **cinches its knot**: the knot's loop scales to 0.82 and back with a
  silk-tight ease while the button inks madder red — confirmation
  feedback performed on the thread tied around the action, not on a
  generic button state. It belongs because §6.4's knot is tied by
  *scrolling* (the visitor's journey earns the knot); the click is the
  visitor's hand taking hold of the tied knot and pulling it snug —
  the difference between arriving at a commitment and sealing it. Every
  other theme in the library confirms with a checkmark, a toast or a
  colour pulse; this one tightens the knot the whole page has been
  travelling toward, and then the knot stays cinched: sealed is a
  state, not an animation.
- **Structure.** The knot group of §6.4 (or its smaller sibling in
  §6.15's form), plus the action button it frames. The cinch animates
  the knot group's scale and the crossing segment's dash (the pull-
  through travels 8px), and the button's ink: background `--madder`
  → `--madder-deep` at the press's depth, label `--silk`. After a
  successful action, a short apparatus line (§3 label style) appears
  beneath the button in the §12 fixed string — *"Tied and cinched —
  [reference]"* — where the reference is the real booking/order number
  returned by the action (§6.15's truth rule: no reference, no
  string; a failed action gets the §12 error voice and the knot
  *loosens* one geometry instead, below).
- **Motion spec.** Trigger: click / Enter / Space on the action.
  Cinch: knot scale 1 → **0.82** over **160ms `--ease-cinch`** (the
  pull), hold 60ms at full tightness (the hand feels the knot seat),
  release to **0.94** — NOT back to 1 — over **220ms `--ease-settle`**:
  the knot rests cinched, visibly tighter than §6.4 left it, for the
  rest of the session. Button ink deepens simultaneously (160ms).
  The pull-through segment draws its 8px during the pull. Total beat:
  440ms. A second click (double-click, impatient tap) does not
  re-cinch: the knot is already tight; the button's own disabled/
  processing state (§6.15) governs repeats.
- **Choreography timeline (v2).** t+0: activation → t+0–160ms: knot
  pulls to 0.82, crossing travels 8px, button deepens → t+160–220ms:
  the seat — held at full tightness → t+220–440ms: release to 0.94
  rest → t+440ms: the action's own result arrives on its own timeline
  (navigation, §6.15's confirmation state, §6.16's pull-through) — the
  cinch never waits for the network and never pretends the result has
  landed before it has; if the action fails, at failure's arrival the
  knot loosens to §6.4's gathering geometry over 500ms `--ease-silk`
  and the error line speaks (§12) — an honest untying, performed at
  the same dignity as the tying.
- **State matrix (v2).** *Tied-uncinched (post-§6.4):* knot at scale
  1 (relative), button madder. *Cinching:* 440ms as specced.
  *Cinched (terminal, success):* knot at 0.94 rest, button
  `--madder-deep`, reference line present. *Loosened (failure):*
  gathering geometry, error line present; a corrected retry re-runs
  §6.4's final beat then this cinch. *Hover (pre-click):* the knot
  leans ≤6px toward the pointer (§6.4) — the hand approaching.
  *Focus:* lean + ring. *Active:* the cinch itself. *Disabled button:*
  no cinch exists (§6.4's disabled rule: the knot never gathered) —
  clicking a disabled action does nothing to the thread.
  *Scrolled-past:* cinched state persists (session state, like §6.4's
  latch). Touch: identical, minus the hover lean.
- **Content merge.** The cinch happens on the knot that §6.4 tied
  around *this* action, and its success line carries *this* action's
  real reference. It is not a button press effect; it is the third
  act of the thread's own story (arrive §6.2 → tie §6.4 → cinch §6.9)
  and it cannot be transplanted to an action the thread never
  travelled to — §10 audits that every cinch-capable button sits
  inside a knot's frame.
- **Failure fallback.** No-JS: the button works as a plain madder
  button with the knot tied beside it (§6.4's fallback); form
  submission and its confirmation are server-rendered (§6.15) — the
  cinch is an enhancement of a complete action, never the action's
  only feedback. If the knot group is missing (build error), the
  button falls back to a 1px press-settle (§5 micro-interactions) and
  the build fails §10.
- **Reduced-motion variant.** No scale travel. On activation the knot
  swaps instantly to its cinched geometry (the 0.94 rest state is an
  authored geometry, not only a transform), the button deepens
  instantly, and the reference line appears. The state change is fully
  communicated; only the pull is stilled.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: pull to 0.84,
  release rest 0.95 (the smaller knot travels less). <768px: pull to
  0.86, hold 40ms, release 0.95; the pull-through travel is 6px. The
  beat's total stays ≤440ms at every size — a seal that takes longer
  on a phone feels like lag, not ceremony.
- **Edge cases & failure modes (v2).** *Action succeeds but slowly
  (3s network):* the cinch completes at 440ms into the button's
  processing state (§6.15's spooling label); the knot does NOT loosen
  while waiting — waiting is not failure. Only an actual error
  response loosens it. *Action is a download/link, not a submission:*
  the cinch still fires (it seals the visitor's intent) and §6.16's
  pull-through follows for navigation. *Keyboard activation:* identical
  beat (Enter/Space are clicks here). *The visitor cinches, then
  navigates back:* the knot is found cinched (session latch) with its
  reference line — the page remembers being sealed, in state and in
  words.
- **Accessibility spec (v2).** The button's name never changes during
  the cinch; its result is announced by the reference/error line as a
  polite live region (`aria-live="polite"`, once). The knot is
  `aria-hidden`. Focus stays on the button through the beat and moves
  only per §6.15/§6.16's navigation rules. Contrast: `--silk` label on
  `--madder-deep` ≈ 11.7:1 ✓ (derived from §2's madder-deep figure).
  Touch target: the button, ≥48px height (§6.15).
- **Performance budget & mobile variant.** One group transform + one
  8px dash + one colour transition: negligible (≤0.1ms/frame, 440ms,
  once per action). Mobile: the reduced travel above; no other change.
- **Tokens consumed (v2).** `--gold`, `--madder`, `--madder-deep`,
  `--silk`, `--ease-cinch`, `--ease-settle`, `--ease-silk`,
  `--cinch-dur` (440ms), `--cinch-rest` (0.94).

### 6.10 Measured figures — counted off the spool

- **What & why.** Every number that animates on this page — yardage in
  stock, pieces on the line, a price assembling itself, the thread's
  own drawn percentage in §6.12's navigation — counts **like thread
  being measured off a spool**: an even take-up at a measured pace, a
  faint tick at each whole unit, and a dead stop at the true figure.
  No ease-out flourish, no overshoot past the number and back (a
  measuring hand does not overshoot the mark and rewind — it stops ON
  the mark). It belongs because numbers in this theme are measurements
  of physical stuff — metres, pieces, hours at the loom — and a
  counter that behaves like a slot machine lies about the stuff it
  counts. The original entry's line is the spec: figures count up
  *like thread measured off a spool*, and this element is that line
  made law for every figure on the page.
- **Structure.** Any element with `data-measure` carries its final
  figure as its text content in the DOM (server-rendered, tabular
  Karla, §3). The counter is a JS enhancement that replays the figure
  from a stated start (0 for stock/yardage, the un-discounted figure
  for a price assembling after a correction, §6.15) to the DOM's true
  value. A hairline "measure rule" — a 1px `--gold-ink` line with tick
  marks at each 10% — sits under yardage figures only, filling in step
  with the count: the ruler the thread was measured against. Prices do
  not get the rule (a price is asked, not measured — §6.6 owns prices);
  stock and yardage do.
- **Motion spec.** Trigger: the figure's first entry into the viewport
  (threshold 0.5). Rate: **one unit per 90ms** for counts ≤ 40; for
  larger figures the rate compresses so total duration lands between
  900ms and 1600ms, stepping in whole units only, on `--ease-spool`'s
  even take-up — the value at time t is `round(final × spoolEase(t))`
  with the guarantee that consecutive frames never jump more than 2%
  of the final figure (no leaping from 3 to 97). The tick: at each
  whole-unit change the figure's measure rule (if present) advances
  one tick and the figure itself makes a 1px vertical settle
  (`--ease-settle`, 60ms) — the measured length being laid down, unit
  by unit. **The count runs once.** Re-entry does not recount (the
  thread is already measured; re-measuring on every scroll-past is a
  carnival trick). Dynamic updates (stock changing after a purchase)
  count from old to new at the same rate, in whichever direction —
  measuring off or winding back are both honest motions.
- **Choreography timeline (v2).** t+0: figure 50% visible → t+120ms:
  first unit ticks (a breath before measuring begins — the hand finds
  the spool's end) → units tick at the computed rate → final unit: the
  figure settles with a slightly longer 120ms settle and the measure
  rule completes → terminal: the figure is plain text forever after;
  the `data-measure` replay machinery removes itself.
- **State matrix (v2).** *Unmeasured (pre-trigger / no-JS):* the true
  figure, plain — the fallback IS the content. *Measuring:* ticking as
  specced. *Measured (terminal):* true figure, rule complete.
  *Updating:* old → new count on a real data change. *Hover/focus:*
  none — figures do not perform for pointers. *Scrolled-past:*
  measured state persists; an unmeasured figure scrolled past unseen
  (>50% never visible) is set to measured instantly by the §6.2-style
  catch-up rule — the visitor must never scroll back up to find a
  figure still at zero pretending the shelf is empty. *Disabled:* n/a.
  Touch identical.
- **Content merge.** The figures are the page's real quantities —
  stock drawn from the same data that disables §6.3's loop when a
  piece is gone, prices that §6.6 frays beside. The measure rule under
  a yardage figure is filled by that figure's own count. Inventing a
  figure to have something to count ("10,000 happy customers") is the
  §9 slop this element exists to prevent: §10's counter-truth audit
  traces every `data-measure` value to a data source or strikes the
  element from the build.
- **Failure fallback.** No-JS: true figures everywhere (they are the
  DOM). Observer failure: figures are simply true — the replay is the
  only thing that can fail, and its failure is invisible. If a data
  update arrives mid-count, the count re-targets to the newest true
  figure from its current value.
- **Reduced-motion variant.** No counting. Figures stand at their true
  values; updates swap instantly. The measure rule stands complete.
- **Breakpoints (v2).** Identical behaviour at all sizes; only the
  measure rule shortens (<768px: ticks at each 25% instead of 10% —
  a phone-width ruler has fewer honest marks).
- **Edge cases & failure modes (v2).** *Figure is 0 (out of stock):*
  no count runs; the zero stands with §6.14's awaiting-lot line — a
  zero measured ceremoniously is a taunt. *Decimal yardage (2.5 m):*
  counts in 0.1 steps at the same unit rate; the decimal is part of
  the measurement, never rounded for theatre. *Huge figures
  (12,480 m of stock):* the compression cap holds duration ≤1600ms;
  grouping separators are present from the first frame (the figure
  counts "8,214" not "8214" — the ruler is graduated in the locale's
  own marks). *Locale change:* figures re-render from data in the new
  locale's format, uncounted.
- **Accessibility spec (v2).** The figure's final value is in the
  accessibility tree from first paint (the replay masks visually,
  like §6.5's typing rule — text is never withheld from AT). Counting
  is never announced live (a yardage figure ticking through a screen
  reader is cruelty); a figure that *updates* from a user action
  announces its final value once, politely. Contrast per §2
  (`--gold-ink` 5.88:1 ✓ for figures; `--cocoon` 12.77:1 ✓ for stock
  counts set as body data).
- **Performance budget & mobile variant.** One rAF-driven text update
  per counting figure, ≤3 figures counting concurrently (a queue
  beyond that — measuring is serial work, like the spool). ≤0.1ms/
  frame each. Mobile: identical; the queue cap drops to 2.
- **Tokens consumed (v2).** `--gold-ink`, `--cocoon`, `--ease-spool`,
  `--ease-settle`, `--measure-rate` (90ms/unit), `--measure-min`
  (900ms), `--measure-max` (1600ms).

### Page-family elements

### 6.11 Hero composition (page family: hero)

- **What & why.** The first screen, composed as the thread's arrival:
  the drop (§6.1) falls, the headline stands underlined by the settled
  thread, one word of it unspools (§6.5), the standfirst and the
  house's single primary action settle in thread-first order, and —
  quietly, at the hero's foot — the thread departs downward into the
  page, already drawing (§6.2). This element is the *composition*
  spec: how the parts §6.1/§6.5/§6.2 assemble into one first screen
  without competing. It belongs as a separate element because each of
  its parts is specified elsewhere and a hero is exactly where
  individually-correct parts go to fight.
- **Structure.** A 100vh (≥1200) / auto-min-92vh stage: headline block
  in the content column (never centred — §4's centring is reserved),
  its underline surveyed as the drop's landing (§6.1); the unspooling
  word inside the headline (§6.5); standfirst (Karla, 19px, measure
  ≤52ch) beneath; one primary action (a plain `--cocoon` button or the
  §6.4-bound CTA's *invitation link* — the hero never contains the
  knot itself; commitment lives down-page where the journey earns it);
  a hero image, if any, hung on the line at the column's end (stagger
  offset 14px, §4) with its caption inside a §6.3-ready frame. The
  thread's rail enters from the top edge at the rail's x and exits at
  the hero's foot — the hero is the thread's first room, with a door
  at each end.
- **Motion spec.** The sequence is fixed and total ≤2400ms: drop
  (§6.1, 0–1800ms) → unspool (§6.5, from t+700ms) → standfirst settles
  at t+900ms (420ms `--ease-settle`, thread-first: the headline's
  underline segment completes its draw 150ms before the standfirst
  moves) → action settles at t+1080ms → hero image (if present) is
  simply *there* (images do not enter on this page; they hang, §5's
  reveal law applies to blocks, and a photograph that slides in is a
  slideshow). On scroll, the hero's only motion is §6.2's draw and the
  image's thread-speed parallax (§5, 0.94×) — the hero does not fade,
  scale or pin.
- **Choreography timeline (v2).** t+0 paint (complete hero, fallback
  state) → t+80ms drop arms → t+700ms thread lands, unspool begins →
  t+900ms standfirst settles → t+1080ms action settles → t+1880ms
  thread at rest; hero complete → first scroll: §6.2 owns everything
  from here. Return visits (session): drop and unspool skipped (§6.1/
  §6.5 latches), standfirst/action present — total entrance 0ms.
- **State matrix (v2).** *Composed (default):* the finished hero.
  *Composing:* the 2400ms sequence. *Scrolled:* draw + parallax only.
  *Hover/focus:* the action's own states (§6.15 button rules); the
  hero image's frame accepts §6.3's loop if it is a product, else
  nothing. *Disabled:* n/a. Touch: same sequence, drop per §6.1's
  mobile geometry.
- **Content merge.** The hero IS the composition of the theme's
  elements around the page's actual headline, standfirst and action —
  there is no hero-specific decoration to remove. The test: cover the
  thread and the hero is a clean, complete first screen; uncover it
  and every part is connected. Both states are designed; neither is
  an accident.
- **Failure fallback.** Every part ships composed (§6.1/§6.5
  fallbacks); the composition adds no failure mode of its own except
  sequencing, and its watchdog is §6.1's 2000ms absolute: after it,
  the hero is composed regardless of which beats fired.
- **Reduced-motion variant.** The composed hero, instantly: thread
  drawn and settled, word set, standfirst and action present.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: headline
  52px, image hangs below the action instead of at the column's end.
  <768px: single column — headline, standfirst, action, image in
  reading order; the thread in its 28px gutter underlines the
  headline's first line only (§6.2 mobile survey); entrance sequence
  compresses to ≤1600ms.
- **Edge cases & failure modes (v2).** *Headline longer than two
  lines:* the underline surveys under the LAST line (the thread
  underlines the whole statement, not its first breath); the drop
  lengthens accordingly within §6.1's 420px cap. *No hero image:*
  the composition is unchanged — the thread's departure at the foot
  carries the eye down; an empty hanger position is left empty, never
  filled with a decorative swatch. *A/B headline variants:* each
  variant is surveyed at build; an unsurveyed variant fails §10.
- **Accessibility spec (v2).** Reading order: headline → standfirst →
  action → image caption — the visual composition and the DOM order
  agree (the image's visual position at the column's end is achieved
  with layout, not with order-breaking positioning). The action is
  reachable by keyboard within the first three tab stops of the page.
- **Performance budget & mobile variant.** The hero runs §6.1 + §6.5's
  budgets concurrently and nothing else; total first-screen motion
  cost ≤0.6ms/frame. Mobile: compressed sequence above.
- **Tokens consumed (v2).** `--ease-settle`, `--stagger-hero` (180ms),
  plus the tokens of §§6.1, 6.2, 6.5 which this element orchestrates.

### 6.12 Thread-margin navigation (page family: navigation)

- **What & why.** Navigation in this theme is not a bar of links
  pretending the thread doesn't exist. The site's sections are listed
  as **knots on a short vertical thread** in the header's compact nav
  (and, on the long page itself, the master thread's passage is the
  navigation — §6.2). Each nav item is a small knot glyph tied on a
  2px line segment; the item for the section the visitor is currently
  reading is the knot the master thread has *reached* — drawn in
  `--madder`, its segment filled — while unreached sections' knots
  sit open in `--gold-ink`. It belongs because progress and navigation
  are the same fact on this page (how far the thread has gone = where
  you are = where you can go), and a separate nav system would state
  that fact twice in two languages.
- **Structure.** A `<nav>` in the header: horizontal on ≥1200 (knots
  on a horizontal thread segment — the one place the thread runs
  sideways, a laid-down length of the same line), vertical in the
  mobile menu. Each item: a real `<a>` with a knot span (an SVG knot
  glyph, 12px, two states: open/tied) + the section name in Karla
  label style (§3). The current item carries `aria-current="true"`
  and the tied/madder knot. A compact apparatus line under the nav
  states the thread's progress in words for AT and for anyone who
  wants it plainly: "THE THREAD HAS REACHED: THE DYE LOTS" (§12 fixed
  pattern) — updated at section boundaries only.
- **Motion spec.** Knot tying on arrival: when §6.2's draw crosses a
  section boundary, that section's nav knot cinches (the §6.9 beat at
  nav scale: scale 1 → 0.85 → 0.96 rest, **300ms `--ease-cinch`**) and
  inks madder; the previous section's knot stays tied but returns to
  `--gold-ink` (tied = visited; madder = *here*). Scrolling back above
  a boundary unties nothing — visited stays visited (the §6.4 latch
  logic, at nav scale). Hover on an item: its knot leans 3px toward
  the label (the thread stirring) and the label underlines with the
  single-fibre draw (180ms, §5). Click: §6.16's pull-through for
  page changes, or a plain scroll to the section for same-page
  anchors — with the thread's draw (§6.2) following the scroll as
  always, so navigation by knot and navigation by scroll never
  disagree about where the thread is.
- **Choreography timeline (v2).** Boundary crossing (t+0, from §6.2)
  → t+0–300ms: the newly reached knot cinches and inks → t+300ms: the
  apparatus line's text swaps (no animation — paperwork, §6.2's label
  rule) → on click: pull-through (§6.16) or anchor scroll; the knot
  of the destination ties on arrival, by the same boundary rule.
- **State matrix (v2).** *Unreached:* open knot, `--gold-ink` label.
  *Current:* tied knot, madder, `aria-current`. *Visited:* tied knot,
  `--gold-ink`. *Hover/focus:* lean + fibre underline; focus adds the
  standard ring (the knot alone is never the focus indicator).
  *Active:* cinch beat replays at 200ms (a small acknowledgement pull).
  *Disabled:* a section that does not exist on this page is absent
  from the nav — never a greyed knot. Touch: knots are ≥44px tap
  rows in the vertical menu; the lean is absent, the states identical.
- **Content merge.** The nav's items are the page's real sections in
  reading order, generated from the same section list the thread's
  survey (§6.2) is built from — add a section and both gain a stretch
  and a knot, or the build fails (§10). The progress the knots show is
  §6.2's drawn length restated, not a second measurement.
- **Failure fallback.** No-JS: all knots render tied in `--gold-ink`
  except the server's known current section (first, by default) in
  madder; links work as plain anchors. The apparatus line is
  server-rendered for the first section. Nothing about navigation
  depends on the draw.
- **Reduced-motion variant.** Knots swap states instantly (tied/open,
  madder/gold-ink are colour-and-shape states, not motions); no
  cinch, no lean.
- **Breakpoints (v2).** ≥1200px: horizontal thread nav in the header.
  768–1199px: horizontal, labels shorten to the §12 short names (the
  sections carry authored short names for this breakpoint — never
  CSS-truncated). <768px: the header shows the current section's knot
  + name and a "THE THREAD" menu button opening the vertical list;
  the button's target is ≥44px and `aria-expanded` is honoured.
- **Edge cases & failure modes (v2).** *More sections than the header
  holds (>7):* the nav shows first-level sections only; sub-sections
  are reached by the thread (scroll) and by in-page apparatus links —
  a nav of 14 knots is a bracelet, not a wayfinding tool. *Single-
  section page:* the nav is omitted entirely (a thread with one knot
  is a loop of string). *Boundary thrash (visitor hovering at a
  section edge):* knot state changes are debounced 150ms and the
  cinch never replays for a re-crossed boundary within the same
  visit to that section.
- **Accessibility spec (v2).** Real `<nav>`, `aria-label="Sections,
  along the thread"`; `aria-current` maintained; the knot glyphs are
  `aria-hidden` (state is in the label's colour AND in the apparatus
  line's words — never in the glyph alone). Focus order = reading
  order. Madder label on silk: 9.15:1 ✓; gold-ink: 5.88:1 ✓.
- **Performance budget & mobile variant.** State swaps on boundary
  events only; zero per-frame cost. Mobile: the menu variant above.
- **Tokens consumed (v2).** `--gold-ink`, `--madder`, `--gold`,
  `--ease-cinch`, `--ease-silk`, `--nav-cinch` (300ms),
  `--knot-glyph` (12px).

### 6.13 Silk sheen sweep (page family: ambient surface)

- **What & why.** Every few seconds, a broad band of slightly deeper
  silk crosses the page's cloth grounds — the light in the room
  changing as someone passes a window. It is the theme's second and
  final ambient loop (§5), and it belongs because raw silk's defining
  visual property is that it is not matte: a page of perfectly flat
  `#F7F2EA` reads as paper, and this theme's ground must read as
  *cloth* for the thread laid on it to make sense. The sweep is the
  cheapest possible way to keep the ground textile — no texture image,
  no noise filter, just light, moving slowly, at an opacity most
  visitors will feel rather than see.
- **Structure.** A single fixed, pointer-events-none overlay div
  carrying a linear-gradient band (`--silk-deep` at 0 → 0.05 opacity
  peak → 0, band width 60% of viewport, angled 12° off vertical to
  match §6.1's light), translated across the viewport by a CSS
  animation on transform only. It sits above section grounds and
  below content (z between ground and furniture) — light falls on the
  cloth, not on the words: text layers are above the sweep, so glyph
  contrast never modulates. In the dark scheme the band is `--gold`
  at 0.04 peak — lamplight breathing.
- **Motion spec.** Cycle: **6000ms** period; the crossing itself takes
  **2400ms `--ease-settle`** (enter slow, cross steady, leave slow),
  then 3600ms of stillness. Direction alternates per cycle (left→right,
  then right→left) so the room's light has no mechanical habit. The
  animation pauses when the tab is hidden and when any part of the
  page is being read under `prefers-reduced-motion` (below). It never
  runs during §6.4's pin (the knot chapter's light is held — a held
  breath does not flicker) nor during §6.16's transition.
- **Choreography timeline (v2).** Continuous loop; cycle t+0: band at
  −60% x → t+0–2400ms: crossing → t+2400–6000ms: band off-screen,
  stillness → direction flips → repeat. First cycle begins 4000ms
  after load (the entrance sequence owns the first seconds; §6.11).
- **State matrix (v2).** *Resting (between crossings / no-JS):* no
  band anywhere — the ground is plain silk, complete. *Crossing:*
  as specced. *Paused:* tab hidden, pin active, transition active,
  reduced motion. *Hover/focus:* unaffected (the light does not care
  where the pointer is). *Disabled:* n/a. Identical on touch, except
  the period lengthens (below).
- **Content merge.** The sweep acts on the ground the content lies on
  and on nothing else — it is the cloth's own property, like §6.2's
  thread-shadow is the thread's. Its merge test is subtraction: remove
  it and every word, price and knot remains, on a ground that reads
  slightly more like paper. That is the correct size of an ambient
  effect: missed when gone, unnoticed when present.
- **Failure fallback.** The overlay is created by CSS only; if it
  fails, nothing is missing. No JS is involved at all — this element
  cannot strand content, and its absence is its fallback.
- **Reduced-motion variant.** None. The overlay is not rendered under
  `prefers-reduced-motion` (a media query removes it, not merely
  pauses it — a frozen band across the cloth would be a stain).
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: band width
  70%, peak 0.045. <768px: period 9000ms, crossing 3000ms, peak 0.04 —
  a smaller room, slower light; on devices measuring <40fps the sweep
  is cut entirely (it is first in §14's cut order, by design).
- **Edge cases & failure modes (v2).** *Photosensitivity:* a 0.05
  opacity luminance drift over 2.4s is far below any flash threshold;
  the band never strobes, never reverses mid-crossing. *Band over the
  fray zones (§6.6):* the sweep passes under the SVG thread layer too
  (the thread is furniture) — fibres do not brighten; only cloth does.
  *Print:* the overlay does not print.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`, no
  information, no state. Text contrast is unaffected by construction
  (text layers sit above the band).
- **Performance budget & mobile variant.** One transform on one fixed
  layer; the cheapest ambient in the library's terms. Mobile: the
  slowed variant above, cut entirely under low-fps measurement.
- **Tokens consumed (v2).** `--silk-deep`, `--gold`, `--ease-settle`,
  `--sheen-period` (6000ms), `--sheen-cross` (2400ms),
  `--sheen-peak` (0.05).

### 6.14 Hanging piece cards (page family: cards / listing)

- **What & why.** The listing unit: each product is a **piece hanging
  on the line** — a card suspended from the master thread's height at
  its row, with the §4 stagger (neighbours hang 0/8/10/14px lower in
  rhythm), its image inside a frame the thread can loop (§6.3), its
  price carrying the fray (§6.6), and its name in Cormorant with the
  Weaver's italic note beneath when the maker has something to say
  about this piece. It belongs because a grid of identical floating
  cards is the single most recognisable shape of AI-slop commerce
  (§9); pieces on a line cannot be mistaken for it — the stagger, the
  thread above each row, and the fray at each price make the listing a
  place, not a spreadsheet.
- **Structure.** `<article class="piece">`: a hanger point (the card's
  top edge meets the row's thread segment — a surveyed spur of the
  master path drops 18px to the card's top-centre and returns, so each
  card is literally attached to the line), figure (image in its frame,
  §5's thread-speed parallax inside the frame at image scale 1.06→1
  settle), name (Cormorant 600, 24px), the Weaver's note (italic,
  optional, max 12 words — §12), yardage/stock line (§6.10 figures),
  price (`--gold-ink` tabular, with its fray zone surveyed beside it),
  and one action ("See this piece" link or the booking button). Rows
  are 3-across ≥1200, 2-across 768–1199, 1-across <768; the thread's
  row segment runs above each row at its own height.
- **Motion spec.** Entry: thread-first (§5) — the row's thread segment
  and the cards' hanger spurs draw (300ms `--ease-silk`), then cards
  settle in stagger (90ms apart, 420ms `--ease-settle`, translateY
  12px → 0, and a 0.4° rotation settling to the card's hang angle —
  pieces come to rest hanging, with the tiniest swing decay, 600ms,
  amplitude ≤0.4°: a hung piece moves a breath and stops; more is a
  mobile over a cot, §6.1's rule). Hover: §6.3's loop (the card's own
  frame), plus the card's hang angle straightens by its stagger offset
  (the piece levels as you take hold of it — transform only, 240ms).
  The price fray is §6.6's, surveyed per card.
- **Choreography timeline (v2).** Row enters (t+0) → t+0–300ms: thread
  segment + spurs draw → t+150ms: first card begins settling → cards
  stagger 90ms → t+~900ms: row hung, swing decayed → per-card: fray
  separates when its price crosses §6.6's threshold (subject to the
  2-per-viewport cap — in a 3-across row, the first two prices in
  reading order fray; the third carries §6.6's short-form caption) →
  hover at any later time: §6.3's timeline.
- **State matrix (v2).** *Hung (rest):* card at its stagger offset and
  hang angle, price frayed (if in the viewport's fray budget).
  *Settling:* entry beat above. *Hovered/focused:* looped (§6.3),
  levelled. *Active:* press-settle 1px (§5). *Unavailable:* the card
  hangs **lower** — its spur is 12px longer and the card sits 12px
  below the row's rhythm, with §6.3's three-quarter loop and the
  awaiting-lot line in place of the action; a sold piece is not
  removed from the line (the line remembers what hung there) but it
  cannot be taken. *Scrolled-past:* hung; entry never replays.
  *Touch:* first tap loops (§6.3), second tap follows the action.
- **Content merge.** Every part of the card is the piece's own data —
  its image in the loopable frame, its price beside its fray, its
  stock as a measured figure, its maker's note in the maker's voice.
  The hanger spur ties the card to the surveyed thread: delete the
  piece and the spur leaves the survey (§6.2's check). A card for a
  piece with no image uses a woven-swatch figure (a §6.8 sampler at
  card scale, in the piece's dye colours) — never a grey box, never a
  stock photo of someone else's silk.
- **Failure fallback.** No-JS: cards stand in their rows, level, fully
  priced and actionable; spurs and thread are drawn (the survey ships
  drawn, §6.2); frays absent (§6.6's fallback) and prices plain. The
  listing loses its hanging and keeps its shop.
- **Reduced-motion variant.** Cards stand level at their stagger
  offsets (the stagger is layout, not motion, and survives); no
  settle, no swing, no loop-draw (§6.3's instant variant), frays
  pre-separated and still (§6.6).
- **Breakpoints (v2).** ≥1200px: 3-across, stagger set {0,10,0} per
  row rhythm (the middle piece hangs lowest — a line sags in the
  middle, §4's rhythm made physical). 768–1199px: 2-across, stagger
  {0,8}. <768px: 1-across, stagger 0 (a single column has no line to
  sag), spurs shorten to 10px, the fray moves to the gutter (§6.6).
- **Edge cases & failure modes (v2).** *Long names / notes:* name
  clamps at 2 lines, note at 12 words by copy law (§12) — a card that
  grows taller than its row-mates keeps its hanger (the spur is fixed)
  and the row's rhythm absorbs it; rows are not equal-height forced
  (equal heights are the grid-slop this element replaces). *Filtering
  / sorting the listing:* re-hung pieces settle with the entry beat
  compressed to 200ms and no swing; the thread re-surveys to the new
  row heights (§6.2 re-measure) — a filtered line is a re-hung line,
  and the survey says so. *A whole catalogue page (60 pieces):* entry
  beats are capped — only rows entering the viewport animate; rows
  rendered by "load more" arrive hung (no ceremony tax on pagination).
- **Accessibility spec (v2).** One primary link per card (the name),
  stretched-link pattern forbidden here (the loop needs the card's
  hover area distinct from its link — the link is the name + figure
  as one anchor, the action is the same destination, not a second
  tab stop). Unavailable state is text ("Awaiting the next dye lot —
  mulberry, expected [month]"), never the lowered hang alone. Focus:
  §6.3's loop + 2px `--gold-ink` outline offset 3px. Price contrast
  5.88:1 ✓; note italic `--cocoon` at 19px on silk-deep 11.39:1 ✓.
- **Performance budget & mobile variant.** Entry transforms on ≤3
  cards per row; parallax inside frames shares §5's loop and is cut
  first on <40fps (§14). Mobile: single column, no parallax, spurs
  static.
- **Tokens consumed (v2).** `--silk-deep`, `--gold`, `--gold-ink`,
  `--cocoon`, `--ease-silk`, `--ease-settle`, `--hang-stagger`
  (0/8/10/14px), `--spur` (18px), `--settle-card` (420ms).

### 6.15 The measure & cut form (page family: forms / conversion)

- **What & why.** Silk is sold by measure and cut to order, so the
  theme's conversion form is a **measure & cut form**: fields ruled
  like a cutting ticket, a yardage selector that is literally a
  measured length (§6.10's rule made interactive), a total that
  assembles by measurement — and, beside the total, the page's
  strongest fray (§6.6): the thread comes most undone at the exact
  figure the visitor is about to pay. The submit is a knot: §6.9's
  cinch at form scale, with the confirmation arriving as a tied
  reference line. It belongs because conversion is where themes go to
  die (a generic checkout in a themed site), and this form refuses:
  every one of its parts — measure, fray, knot — is the theme's own
  substance doing the form's ordinary jobs.
- **Structure.** `<form class="measure-form">` on `--silk-deep`:
  fields as bottom-ruled inputs (transparent ground, 2px `--cocoon`
  bottom rule, Karla 17px), apparatus labels above (§3). The yardage
  control: a horizontal measure rule (0 to the piece's available
  metres, ticked at each 0.5m) with a draggable/ steppable marker —
  implemented as a real `<input type="range">` restyled, plus a
  number input as its twin (the two never disagree; either drives
  both). The total: §6.10 measured figure, recomputed live, with its
  fray zone surveyed along its left edge — the form's fray is
  authored, not surveyed from the page thread (the form is a room of
  its own; its thread segment enters from the form's top-left corner,
  frays at the total, and ties at the submit). Submit: the knot
  button (§6.9) — "Tie the knot — order this piece" is FORBIDDEN as a
  label (§12: the action names the act, "Order 2.5 metres — £…"); the
  knot glyph sits beside the true label.
- **Motion spec.** Field focus: the field's rule thickens 2px → 3px
  and a `--gold-ink` fibre slides in beneath it from the reading start
  (200ms `--ease-silk`) — the line you are writing on is underlined by
  a drawn fibre. Yardage marker: moving it draws the thread segment
  from the form's corner toward the total at the same proportion
  (scrubbed by the shared loop, lerp 0.12) — choosing more cloth
  literally pulls more thread across the form. Total updates: §6.10's
  measured count between old and new (≤600ms, compressed rate), and
  the fray's fibres re-tremble at ±0.6px (they do not re-separate,
  §6.6). Error: the field's rule turns `--madder`, the ground washes
  `--madder` at 6%, and the error caption letters in the Weaver's
  voice (§12) beneath the field (opacity settle 240ms — form errors
  are never letter-by-letter; urgency outranks ceremony inside forms).
  Submit: §6.9's cinch (440ms); processing state: the button's label
  becomes the §12 spooling string ("Measuring… / Cutting… / Tying…"
  rotating at 900ms — honest stages, mapped to the request's real
  phases where known, else a single "Tying…" — never a fake progress
  percentage). Success: the form is replaced by its confirmation — the
  tied knot at rest, the reference line (§6.9), and the Weaver's
  italic receipt note.
- **Choreography timeline (v2).** Form enters → thread segment draws
  from the corner to the (initial) total's fray over 500ms
  `--ease-silk`, thread-first before the fields settle (stagger 60ms,
  §5's form exception: fields settle fast, forms are workplaces) →
  interaction beats as specced → submit t+0: cinch (§6.9 timeline) →
  processing → success/failure per §6.9 (failure loosens the form's
  knot one geometry and the error speaks; the visitor's entered values
  are NEVER cleared by an error — a form that eats a customer's
  measurements has broken the theme's covenant, §9).
- **State matrix (v2).** *Rest:* fields ruled, total measured and
  frayed, knot untied. *Focus:* fibre underline + rule thickening.
  *Valid-filled:* a small knot glyph (tied, `--gold-ink`) appears at
  the field's end — the field is "tied off" when its value passes
  validation on blur. *Error:* madder rule, wash, caption; the knot
  glyph absent. *Submitting:* cinch + spooling label, fields inert
  (`aria-busy` on the form). *Success (terminal):* confirmation state.
  *Disabled (piece unavailable):* the form is replaced by §6.18's
  awaiting state — a form for an untakeable piece is never rendered
  live. Touch: identical; the yardage marker's touch target is the
  full rule height, 48px.
- **Content merge.** The measure rule IS the quantity control; the
  fray IS at the total; the knot IS the submit. Strip the theme away
  and the remaining form is a plain, working order form (the fallback
  below) — strip the form away and the thread segment has nothing to
  do in this room. Both directions of the test pass.
- **Failure fallback.** No-JS: a standard form — range replaced by the
  number input alone (the range is the enhancement; the number input
  ships visible and the range is JS-built from it), total
  server-computed on submit, confirmation a server-rendered page with
  the reference. The fray and thread segment are absent; the form
  works. Validation is server-side always; client validation is a
  courtesy layer.
- **Reduced-motion variant.** No fibre slide (rule thickens
  instantly), totals swap instantly, cinch becomes §6.9's instant
  geometry swap, spooling label is static ("Tying…"). The fray stands
  pre-separated and still (§6.6) — in a form, the honesty matters
  most and moves least.
- **Breakpoints (v2).** ≥1200px: two-column fields (name/contact) over
  full-width measure rule and total. 768–1199px: single column, rule
  full width. <768px: single column, total + fray stack (fray in the
  gutter above the total, §6.6 mobile), submit full-width ≥52px tall
  — the knot you tie with a thumb is bigger, not smaller.
- **Edge cases & failure modes (v2).** *Yardage beyond stock:* the
  marker stops at the available length with the §12 line ("The bolt
  holds 4 metres — we cannot cut 5 from it"); the number input clamps
  with the same message, never a silent reset. *Total in a second
  currency:* the figure re-measures (§6.10 update rule) and the fray
  persists — honesty is not denominated. *Server 500 on submit:* §6.9's
  loosening + the §12 server error line; all values intact; retry is
  the same knot. *Autofill:* filled fields get their tied glyphs on
  the form's first validation pass (autofill is also a hand filling
  the form).
- **Accessibility spec (v2).** Real `<label>`s, `aria-describedby`
  for errors, errors announced via a polite live region once per
  field. The range and number inputs share one accessible name
  ("Yardage, in metres") and are both in the tab order as ONE stop
  (the twin is `tabindex="-1"` — two stops for one quantity is a
  trap). The fray is `aria-hidden`; the total is a real output whose
  updates announce politely at change end, not per tick. Focus ring:
  2px `--madder` outline offset 2px (madder is lawful here — focus
  inside the conversion room is commitment-adjacent). Contrast: labels
  `--cocoon` on `--silk-deep` 11.39:1 ✓; error text `--madder-deep`
  on the wash ≈ 10.9:1 ✓.
- **Performance budget & mobile variant.** The form's thread segment
  is one path; the total's count shares §6.10's budget. No other
  animation. Mobile: stacked variant above; the thread segment's
  scrub is cut (segment draws once at entry) on <40fps.
- **Tokens consumed (v2).** `--silk-deep`, `--cocoon`, `--gold-ink`,
  `--gold`, `--fibre`, `--madder`, `--madder-deep`, `--ease-silk`,
  `--ease-settle`, `--fray-dur` (500ms), `--cinch-dur` (440ms).

### 6.16 Thread pull-through & the unwoven warp (page family: loader / transition)

- **What & why.** Two state-change rituals sharing one material.
  **Leaving:** on navigation, the current page's thread completes
  itself — the undrawn remainder draws swiftly to the tie-off — and
  the new page's thread drops in (§6.1): the visitor never leaves a
  thread hanging; every departure is a finished page and every arrival
  is the same thread, continued. **Loading:** content still arriving
  shows as **unwoven warp** — sets of parallel vertical lines (the
  warp on the loom) in the exact box the content will occupy, which
  the weft of real content crosses and completes as it lands. Both
  belong because they are the theme's own substances (thread, warp)
  doing the two jobs every site must do, and because the pair enforces
  the theme's deepest habit: nothing on this page is ever a spinner,
  a shimmer, or a grey rectangle borrowed from another material world.
- **Structure.** Pull-through: the master SVG (§6.2) plus a transition
  state on the shared loop — on an intercepted internal navigation,
  the loop's target is forced to 100% and the lerp quickens (0.3) so
  the remaining thread draws in ≤350ms; at full draw, the sampler's
  tie-off knot (§6.8) flashes its cinch at transition scale (200ms),
  the route changes, and the new page runs §6.1. Warp skeleton: the
  real content container rendered with a `.is-warp` class — inside it,
  6–10 vertical `--gold-ink` hairlines at the content's own column
  rhythm (for text: lines at the measure's line positions; for an
  image: a framed box with warp lines at thirds) at 30% opacity, and
  NO weft. Content arrival replaces the warp children in place; the
  container never resizes (aspect/measure reserved in markup).
- **Motion spec.** Pull-through: 350ms draw completion + 200ms knot
  beat, total ≤550ms, then navigation — the ritual is short because
  leaving is not the destination. If the destination is slow, the new
  page's own warp (below) takes over; the transition never holds a
  visitor hostage on a fully-drawn thread (hard cap: the route swaps
  at 550ms regardless). Warp: as each content block lands, its weft
  "crosses" — the block fades/slides in over 300ms `--ease-settle`
  while its warp lines fade out in the same beat (the crossing is the
  two opacities passing). **1200ms law:** any warp still standing at
  1200ms has its lines stripped to a plain `--silk-deep` block — the
  standing rule that no content area may stay abstract if the
  machinery fails; the block then receives content plainly when it
  comes.
- **Choreography timeline (v2).** Pull-through (t+0 = activation):
  t+0: draw target forced to 100%, lerp 0.3 → t+≤350ms: thread
  complete → t+350–550ms: tie-off cinch beat → t+550ms: route swaps;
  new page: §6.1's drop (compressed to 900ms total for transitions —
  arrivals mid-journey are brisker than first entries). Warp (per
  block, t+0 = fetch start): warp stands → content lands → 300ms
  crossing → block live; or t+1200ms: strip to plain block → content
  lands → plain appearance.
- **State matrix (v2).** *Idle:* no transition, no warp (server pages
  ship loaded). *Pulling through:* as specced; pointer inert on the
  outgoing page from t+200ms. *Warped:* loading blocks as warp.
  *Crossing:* 300ms. *Loaded:* normal page. *Hover/focus:* links show
  §6.12's fibre underline; the transition has no hover state.
  *Disabled / no-JS:* plain navigation; warp never rendered unresolved
  (server pages ship content; warp exists only inside client fetches
  that own the 1200ms law).
- **Content merge.** The pull-through draws the page's OWN thread to
  its own tie-off — the transition is the page completing itself, not
  a curtain dropped over it. The warp occupies the content's own box
  at the content's own rhythm; layout shift is zero by construction.
- **Failure fallback.** Middle-click, new-tab, modified clicks and
  external links bypass the pull-through entirely (it enhances `<a>`
  clicks, never replaces href behaviour). A transition interrupted by
  a second click cancels cleanly to plain navigation. Warp without a
  fetch owner is forbidden at build (§10) — skeletons exist only where
  code owns their resolution.
- **Reduced-motion variant.** Pull-through: no draw completion, no
  knot beat — instant navigation with a 120ms `--gold-ink` outline
  flash on the §6.12 nav (the change of page is marked, quietly).
  Warp: plain `--silk-deep` blocks, content appears at 120ms opacity.
- **Breakpoints (v2).** Identical at all sizes; on <768px the
  pull-through's draw completion cap shortens to 250ms (a phone's
  thread is shorter, §6.2, and the ritual scales with it).
- **Edge cases & failure modes (v2).** *Back/forward buttons:* no
  pull-through (the browser's history gesture rules; the theme does
  not intercept it). *Same-page anchors:* no transition (§6.12's
  scroll). *A fetch that errors:* the warp block resolves into §6.17's
  slipped-knot notice with its retry — a block apologises in the
  theme's voice rather than warping forever. *Prefetched destination:*
  the pull-through still runs its ≤550ms — the ritual is the point,
  not the wait.
- **Accessibility spec (v2).** During pull-through the outgoing page
  is `inert` from t+200ms; on arrival, focus moves to the new page's
  H1 (`tabindex="-1"`) with a polite announcement "Along the thread:
  [page name]" (§12). Warp blocks carry `aria-busy="true"` until
  crossed; a region with warp announces once ("The loom is still
  warping this page") — never per block.
- **Performance budget & mobile variant.** The pull-through reuses
  §6.2's single path (no extra DOM); warp lines are CSS gradients per
  block (no images). Mobile: shortened caps above.
- **Tokens consumed (v2).** `--gold`, `--gold-ink`, `--silk-deep`,
  `--ease-silk`, `--ease-cinch`, `--ease-settle`, `--pull-dur`
  (350ms), `--warp-strip` (1200ms).

### 6.17 Footer furniture & slipped-knot notices (page family: footer / alerts)

- **What & why.** Two related duties. **The footer furniture:** below
  the sampler and the tie-off (§6.8), the page still owes its ordinary
  paperwork — the house's address, its section links restated, the
  colophon line ("Woven and tied by [House], [Year]"), legal small
  print. This element specifies that paperwork's treatment: it arrives
  last, sits below the knot, and is set entirely in Karla at caption
  sizes — the workshop's desk drawer under the loom, necessary and
  unglamorous, never competing with the ending above it. **The
  slipped-knot notice:** the theme's alert. When something needs the
  visitor's attention mid-page (a dye lot is delayed, a booking window
  moved, a fetch failed per §6.16), the notice is a **slipped knot**:
  a short length of thread beside the notice whose knot has visibly
  slid loose — one loop open, ends uneven — because in this world,
  "something needs attention" is said by the thread's one failure
  state, and it is reserved for exactly that. A notice without the
  slipped knot is body text; a slipped knot without a real notice is
  forbidden (§10).
- **Structure.** Footer furniture: a `--cocoon` ground band (both
  schemes — the footer's desk is dark at noon and at lamplight)
  containing, in order: the colophon line in `--silk` Karla 14px; the
  section links as plain text links (`--silk` at 80%, fibre underlines
  §5); address and contact in apparatus style; legal line at 12.5px,
  `--silk` at 64% (on cocoon ≈ 6.9:1 ✓ — small print must still be
  readable print). No logo lockup, no social icons row (social links
  are text, named — "Instagram" is a word a visitor can read; a glyph
  is a logo they must decode). Notice: an inline block in the flow
  (never a toast, never an overlay) with a 44px thread segment at its
  reading-start edge carrying the slipped knot glyph (authored SVG:
  the §6.4 knot with its left loop opened 30% and one end 10px longer),
  the notice headline in Karla 700, and its body in Karla 400 with the
  remedy as a real link/button inside the notice.
- **Motion spec.** Footer furniture: settles once, thread-first
  (§6.8's timeline hands it t+2540ms), stagger 60ms per block, 360ms
  `--ease-settle` — after the ending, paperwork files itself quietly.
  It never animates again. Notice: on appearance (it is inserted in
  flow, pushing content — notices here are part of the document, not
  interruptions of it), the slipped knot's open loop **slips a further
  4px** over 500ms `--ease-silk` and stops — the slip is seen to
  happen once, then the notice is still; a notice that keeps moving
  is an alarm, and this theme has no alarms, only things needing a
  hand. Dismissal (where the notice is dismissible): the knot is
  **re-tied** by the dismissal — loop closes, ends even, 380ms
  `--ease-cinch` (§6.9's beat) — and the notice block settles out over
  300ms. Re-tying on dismiss is the theme's whole alert philosophy in
  one gesture: attention was needed, a hand came, the knot holds
  again.
- **Choreography timeline (v2).** Notice: t+0 inserted (layout shifts
  once, announced below) → t+0–500ms: the loop slips its 4px → hold:
  still, however long the notice lives → dismissal t+0–380ms: re-tie
  → t+380–680ms: block settles out, content reflows up. Footer:
  §6.8's t+2540ms → blocks stagger 60ms → t+~2900ms: page complete.
- **State matrix (v2).** *Notice live:* slipped knot, still.
  *Notice hovered/focused:* nothing moves (the remedy control has its
  own states). *Notice dismissed:* re-tie + settle-out (terminal).
  *Notice critical (the money kind — a payment failed):* the knot
  slips AND the notice's edge carries §6.6's fray fibres (still,
  pre-separated) — the theme's only escalation, combining its two
  honesty devices; the headline speaks in §12's error voice.
  *Footer:* static after its one settle, all states. *Disabled:* a
  notice whose remedy is unavailable keeps its text and loses its
  button (the remedy becomes words: "write to the house at…", §12).
  Touch identical.
- **Content merge.** The footer's furniture is the site's real
  paperwork, and the sampler above it (§6.8) carries the same facts in
  cloth — the two are one colophon in two materials, and §10 checks
  they agree (house name, year). The notice's slipped knot is tied on
  a segment of thread surveyed into the notice's own position: it is
  the page's line, failing locally, where the failure is.
- **Failure fallback.** No-JS: footer fully present (it ships
  settled); notices are server-rendered in flow with the knot already
  slipped (the slip animation is the enhancement). A notice that
  cannot be dismissed without JS is not marked dismissible in the
  no-JS render — no dead controls, ever.
- **Reduced-motion variant.** Footer present, no settle. Notice
  appears with its knot already slipped the full amount; dismissal
  removes it instantly after the re-tie is shown as a static swap
  (one frame of tied knot, then gone — the meaning survives as a
  two-frame story).
- **Breakpoints (v2).** ≥1200px: footer in three columns under the
  knot. 768–1199px: two columns. <768px: one column, colophon first
  (the fact before the furniture); notice knot segment shortens to
  32px and sits above the headline instead of beside it.
- **Edge cases & failure modes (v2).** *Two notices at once:* they
  stack in flow in severity order (money first); the page never shows
  two slipped knots in one viewport — the second notice waits below
  the fold by layout, not by a queue (there is no notification queue
  in a workshop). *A notice inside the pinned knot chapter (§6.4):*
  forbidden by layout — the pin's stage contains the knot and the ask
  only; notices live before or after the chapter. *Stale notice (its
  condition resolved by time):* notices carry their condition in data
  and are re-checked on render; a slipped knot for a mended problem
  is a false alarm and a §9 failure.
- **Accessibility spec (v2).** Notices use `role="status"` (or
  `role="alert"` only for the payment-failed kind) and are in the
  reading order where they sit. The slipped knot is `aria-hidden`;
  the notice's headline carries the meaning in words. Footer links
  are real links with full names. Contrast on the cocoon band: `--silk`
  12.77:1 ✓, legal line ≈6.9:1 ✓, fibre underlines decorative with
  the link text itself fully contrasted.
- **Performance budget & mobile variant.** One settle sequence (footer)
  and ≤1 slip animation (notice) per page; negligible cost. Mobile:
  the stacked variants above.
- **Tokens consumed (v2).** `--cocoon`, `--silk`, `--gold`, `--fibre`,
  `--madder`, `--ease-silk`, `--ease-cinch`, `--ease-settle`,
  `--slip-dur` (500ms), `--retie-dur` (380ms).

### 6.18 The broken thread (page family: 404 / empty state)

- **What & why.** The theme's law says the thread never breaks — so
  the one place it is *shown* broken is the page whose whole subject
  is absence: the 404, and its sibling, the empty state (an empty
  listing, a search with no pieces). Here, and only here, the master
  thread arrives from the top, reaches the middle of the page, and
  **ends mid-air**: two frayed ends facing each other across a 48px
  gap, fibres splayed (§6.6's device at its widest), swaying very
  slightly out of phase (§6.7's device, saddened) — the line the
  visitor was following does not continue, because this is not a page
  the thread was ever woven through. Below the gap, the remedy: the
  way back to where the thread runs unbroken (the home link, the full
  listing, the search again) — presented as **mending**: a fresh
  length of thread is already laid beside the remedy link, ready to
  be tied. It belongs because a generic "404 — page not found" would
  be the one place this theme shrugs; instead the theme's worst event
  is shown in its own material, and its remedy in its own verb.
- **Structure.** The standard page shell with the master thread
  surveyed only as far as the gap (the survey honestly ends — §6.2's
  path for this page terminates at the gap's near end; a second short
  path segment begins at the far end and runs 120px before tapering
  out, unconnected, the piece that was cut away with the missing
  page). Each end carries 4 fray fibres at §6.6's maximum splay (4px).
  The H1 is §12's fixed line — *"This page was never woven."* — with
  the apparatus sub-line stating the fact plainly ("The address asked
  for a page the house has not made"). The remedy block: one primary
  link (home / full listing) with a 60px fresh thread segment laid
  beside it, its end formed as an untied loop — the mending, ready.
  For the empty state, the same composition with §12's empty voice
  and the remedy "see everything on the line" — plus, where the
  emptiness is a maker's reality (no pieces in this dye lot yet), the
  expected date in words.
- **Motion spec.** On entry: the near thread draws to the gap over
  600ms `--ease-silk` (a compressed §6.2 — the visitor watches the
  line run out), the fibres at both ends separate (500ms, §6.6's
  stagger), and the two ends take up their out-of-phase sway (±3px,
  periods 4.6s and 5.4s — near §6.7's rhythm but detuned, so the gap
  feels *wrong* in a way the visitor feels before they name it).
  Hovering/focusing the remedy link: the fresh segment's loop
  **reaches** — it extends 12px toward the far frayed end over 300ms
  `--ease-silk` (it does not bridge the gap; mending begins at the
  click, not the hover) — and on activation, §6.16's pull-through runs
  in reverse spirit: the fresh thread draws across, the page changes,
  the new page's thread drops in unbroken.
- **Choreography timeline (v2).** t+0: page paints (both ends drawn,
  frayed — the fallback state) → JS arms: near end rewinds to 60% →
  t+0–600ms: draw to the gap → t+400ms: fibres separate (overlapping
  the draw's end) → t+900ms: sway begins (fade-in 1200ms, §6.7's rule)
  → hold: the detuned sway, indefinitely → remedy hover: the reach
  (300ms) → activation: §6.16.
- **State matrix (v2).** *Broken (rest):* gap, frayed ends, detuned
  sway. *Remedy hovered/focused:* the reach. *Remedy active:*
  pull-through. *Scrolled:* the 404 page is short by design (one
  viewport plus the footer furniture, §6.17 — the sampler still
  weaves in the footer of a 404: the house's cloth exists even where
  this page doesn't, and its thread — the footer's own segment —
  is intact; the break is local to the missing page, a distinction
  the composition states carefully). *Disabled:* n/a. Touch: the
  reach fires on first tap (§6.3's two-tap rule), activation on
  second.
- **Content merge.** The broken thread is not an illustration beside
  the error message; it IS the error, drawn by the same surveyed path
  system (§6.2) that connects every real page — its termination is a
  survey fact (this page has no through-route), and the remedy's fresh
  segment is §6.16's transition object. The empty state uses the same
  composition because it is the same fact: the thread found nothing
  to weave through here.
- **Failure fallback.** No-JS: the composition ships in its rest state
  (ends drawn and frayed, sway absent) and the remedy link works —
  the page is a complete, honest 404 with zero scripting. The HTTP
  status is a real 404 (the theme never soft-404s for the sake of the
  composition).
- **Reduced-motion variant.** Ends drawn and frayed, perfectly still
  — the detuned sway is precisely the kind of wrong-feeling motion
  the preference exists to remove; the gap and the fray carry the
  meaning without it. The reach becomes an instant 12px extension on
  focus/hover.
- **Breakpoints (v2).** ≥1200px: gap 48px, sway ±3px as specced.
  768–1199px: gap 40px. <768px: gap 32px, the two ends stack in the
  28px gutter's column (the break reads vertically — the thread comes
  down and stops), remedy full-width below.
- **Edge cases & failure modes (v2).** *A soft-404 risk (the route
  exists but its content is gone):* the empty-state variant is used
  with a 200 status and the §12 empty voice — the composition is
  shared, the status and words are not blurred. *Search emptiness
  with a typo'd query:* the remedy block adds the corrected-query link
  ("the thread runs through 'mulberry' — 14 pieces") only when the
  correction is computed from real results (§6.10's truth rule); an
  invented suggestion is forbidden. *The visitor arrives from the
  pull-through (§6.16):* the transition completes onto this page
  whose thread then runs out at the gap — the sequence is authored so
  the arrival drop (§6.1) is skipped here (a broken page does not
  perform the entrance; it is found, not entered).
- **Accessibility spec (v2).** The H1 states the fact; the apparatus
  line states it plainly a second time (the poetic line never stands
  alone for AT or for anyone in a hurry). The SVG is `aria-hidden`.
  The remedy link's name is complete ("Return to the home page, where
  the thread runs unbroken" is the §12 flourish — its short form
  "Home" is used in the link with the flourish in the adjacent line:
  link names stay scannable, §12). Focus lands on the H1 on arrival
  (SPA) per §6.16's rule.
- **Performance budget & mobile variant.** One short draw, one fray,
  one detuned sway — the cheapest signature-scale composition on the
  site, as befits a page that should be fast to leave. Mobile: the
  vertical variant above.
- **Tokens consumed (v2).** `--gold`, `--fibre`, `--cocoon`,
  `--ease-silk`, `--fray-dur` (500ms), `--sway-period` (4600ms /
  5400ms detuned), `--gap-broken` (48px).

## 7. Page application map

**Home.** The full journey in one page: hero composition (§6.11) →
a line of featured pieces (§6.14) → the maker's chapter (a text
section the thread underlines and otherwise leaves alone — the theme
must prove it can be quiet) → the knot chapter (§6.4) → loose end,
sampler, furniture (§§6.7, 6.8, 6.17). The home page carries the
theme's complete argument: filament to cloth.

**Listing / collection.** Rows of hanging pieces (§6.14) on re-surveyed
thread; the fray budget (§6.6: 2 per viewport) is this page's
governing constraint, and the listing header states the count of
pieces as a measured figure (§6.10) — "14 pieces on the line" is a
fact counted from the DOM's own catalogue data. Filters re-hang the
line (§6.14). No knot chapter: a listing is a place to browse, and
commitment theatre in a catalogue is pressure, not craft (§9).

**Piece / product detail.** The thread gives this page its full
attention: the hero frame is looped on arrival (once, 700ms — the
house takes the piece in hand for you, then lets go), the yardage
selector is §6.15's measure rule at page scale, the price frays
(§6.6) with its caption in the Weaver's voice, and the order form is
§6.15 entire. Related pieces hang below as a short line (§6.14, one
row). The detail page is where the theme must convert, and it does so
with the fewest elements, not the most: loop, measure, fray, knot.

**About / the maker.** The thread underlines and keeps its distance.
Long text, portraits hung on the line, one measured figure where a
number is truly known (years at the loom, counted honestly or not
stated). The maker's chapter is the theme's restraint test: a page
where the thread performs almost nothing is the proof that the theme
is a material and not a screensaver.

**Journal / story.** Reading pages: the thread in the rail, progress
by §6.2, drop caps forbidden (Cormorant italic pull-quotes in the
Weaver's voice instead, §12). The sampler footer closes the article
as it closes every page — the house's mark under a story as under a
shop.

**Booking / checkout.** §6.4's knot chapter precedes §6.15's form
(the commitment, then the paperwork). Inside checkout proper — payment
steps, address, confirmation — the theme QUIETS: thread in the rail,
fray at every total, no loops, no pins, no sway. A visitor giving
card details is owed the calmest room in the house (§9: motion at the
payment step is a trust failure). The confirmation page is §6.9's
cinched knot and reference line, full-page: the journey's end stated
in the theme's own grammar.

**Contact.** A short page: the thread underlines the heading, the
form is §6.15's field treatment without the measure rule (a letter
is not cut to length), and the submit cinches a small knot — even
correspondence is tied off here.

## 8. Worked examples

### 8.1 The hero — a thread arrives (home page, "Mulberry & Madder, silk dyers")

The page is a dyer's home page. The H1 reads: "Silk, dyed the slow
way" — with **"slow"** as the unspooling word (§6.5: it names the
house's promise). Timeline: t+0 the composed hero paints (headline
set, thread drawn under it, standfirst present — a no-JS visitor
loses nothing). t+80ms the drop arms; the thread falls 340px down the
96px rail, swings once through +14 / −8 / +4 / −1.5px, and settles
into the headline's underline by t+1880ms (§6.1). At t+700ms, as the
thread lands, "slow" begins to unspool: s-l-o-w, letters travelling
the underline's own curve at 90ms stagger, each landing as the thread
segment beneath it draws (§6.5). The standfirst — "We dye mulberry
silk in small lots, with madder and weld, and we sell it by the
metre." — settles at t+900ms; the invitation link ("See the pieces on
the line") at t+1080ms. The hero photograph (a dyed skein on a line,
of course) hangs at the column's end, 14px stagger, unmoving. The
visitor scrolls: the thread streams ahead of their reading at lerp
0.12 (§6.2), and the skein slides at 0.94× inside its frame (§5).
Nothing else on the screen has moved. That restraint is the example's
point: three motions in the first screen, each one the thread.

### 8.2 Mid-page — the line of pieces (home page, second chapter)

Three pieces hang in a row (§6.14): a mulberry scarf (£86), a weld-
yellow cushion cover (£54), a madder wrap (sold — awaiting the next
dye lot). The row enters: the thread's segment and the three hanger
spurs draw over 300ms; the cards settle at 90ms stagger, the middle
piece hanging 10px lower (the sag), each with its ≤0.4° breath of
swing decay. The scarf's price crosses 40% visibility: its fray
separates over 500ms, four fibres, and trembles (§6.6) beside the
caption: *"Priced by the hour at the loom — eleven hours in this
one."* The cushion's price is the viewport's second fray; the wrap —
being sold — has no fray at all: its card hangs 12px lower on a
longer spur, its price struck plainly, its line reading "Awaiting the
next dye lot — madder, expected October." The visitor hovers the
scarf: after 60ms of intent, the thread leaves the rail and loops the
scarf's frame in 700ms (§6.3), caption settling inside the circuit.
They move to the wrap: the scarf's loop un-draws, and the wrap's loop
draws only three-quarters and stops — the open quarter facing the
rail, saying in line what its text says in words. The visitor has
learned the shop's whole language — hang, fray, loop, the open loop
of the untakeable — without a single tooltip.

### 8.3 Conversion — measuring, fraying, tying (piece page → order)

The visitor orders 2.5 metres of the madder silk. On the piece page,
§6.15's form: they drag the measure rule's marker — a real range
input wearing the rule's ticks — from 1m to 2.5m; the form's thread
segment pulls across the form in proportion (lerp 0.12), and the
total counts from £34 to £85 by §6.10's measured take-up, ticking at
whole pounds, stopping dead at £85. Beside the total, the fray stands
at its widest on the page (this is the moment of money) with the
Weaver's caption: *"Cut from the bolt when you order — never before."*
They complete the fields (each tying off its small gold-ink knot on
blur), and press "Order 2.5 metres — £85". The knot beside the button
cinches: 1 → 0.82 in 160ms, the seat, release to 0.94 (§6.9); the
label spools through "Measuring… Cutting… Tying…" against the
request's real phases. The confirmation replaces the form: the knot
at its cinched rest, the line "Tied and cinched — Order № 214", and
the Weaver's receipt in italic: *"Your length leaves the bolt on
Thursday. The cut edge will be pinked, not hemmed — as you asked."*
Had the payment failed, the knot would have loosened one geometry,
the error would have spoken in §12's voice ("The card was refused —
the thread has not been cut, and nothing is owed"), and every field
would still hold the visitor's measurements.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The thread as generic squiggle divider.** A wavy SVG line pasted
   between sections, connecting nothing, progressing nowhere. *Cure:*
   the survey (§6.2) — one path, through the content, drawn by scroll.
   If a stretch of thread could be deleted without any element
   noticing, it was decoration; delete it or give it a job.
2. **Fray everywhere.** Fibres at headings, at buttons, at the logo —
   the honesty device sprayed until it means nothing and reads as
   damage. *Cure:* §6.6's two-way audit — fray exists only at live
   money, ≤2 zones per viewport, each captioned.
3. **A knot that doesn't tie.** A static knot illustration near a CTA,
   or a knot animation on a button that does nothing real. *Cure:*
   §6.4's gate — the knot forms by scroll, cinches by click (§6.9),
   and its button performs a real conversion or the chapter is cut.
4. **Thread crossing text.** The line striking through body copy "for
   dynamism." *Cure:* the 16px glyph clearance (§1) is surveyed, and
   §10's geometry check measures it; dynamism is not worth an
   unreadable sentence.
5. **Pendulum slapstick.** The drop swinging wide, bouncing, looping —
   physics as comedy. *Cure:* §6.1's numbers: one swing, 14px, 62%
   decay per pass, dead by 1800ms. A thread is laid down by a careful
   hand.
6. **Gold text.** Prices or labels set in `--gold` (2.03:1) because
   "it looks premium." It looks unreadable. *Cure:* `--gold-ink`
   (5.88:1) for anything read; `--gold` is for line and light only.
7. **The uniform card grid.** Twelve identical cards, equal heights,
   no thread, no stagger, no fray — the theme worn as a colour scheme
   over a template. *Cure:* §6.14 entire: hang them, stagger them,
   let the sold one hang lower.
8. **Invented figures.** "Trusted by 10,000 weavers" counting up in
   the hero. *Cure:* §6.10's counter-truth audit — every measured
   figure traces to data or is struck from the build.
9. **Motion at the payment step.** Loops, pins and sway competing
   with a card form. *Cure:* §7's checkout rule — inside payment, the
   thread sits in its rail and the fray stands still at the total;
   calm is the conversion feature.
10. **Two threads.** A second decorative line "for balance," a thread
    in the sidebar, a thread-coloured chart. *Cure:* the one law
    (§1). One thread, unbroken — a second thread is not emphasis, it
    is a contradiction of the theme's only idea.
11. **The form that eats its input.** A failed order clearing the
    visitor's measurements, forcing re-entry. *Cure:* §6.15's covenant
    — errors loosen the knot and keep the data; the hand that slips
    does not also throw away the cloth.
12. **Sampler as clip-art.** A stock "cross-stitch" image in the
    footer, or fake stitched text. *Cure:* §6.8's authored plain weave
    — 11 warp, 9 weft, over/under in the path data, the mark typeset
    as a woven label. If it wasn't woven by the drawing, it doesn't
    ship.

## 10. Quality gate

**Blocking (all must pass):**

1. **One-thread audit.** The page contains exactly ONE master path;
   its geometry is surveyed against the shipped DOM (every act's
   sub-range lands on its element); deleting any section in a test
   build makes the geometry check fail. A second independent thread
   anywhere = fail.
2. **Clearance audit.** The thread's minimum distance to any glyph is
   ≥16px at all three breakpoints, measured on the rendered page.
3. **Fray two-way audit.** Every fray zone is anchored to a live money
   element with its caption present; every live money element has its
   fray (or the §6.6 grid short-form); fray zones per viewport ≤2.
   A fray at a non-money element = fail; a naked price = fail.
4. **Progress truth.** At 25/50/75/100% scroll, the drawn fraction of
   the master thread equals the scroll fraction within ±1.5%; at 100%
   the thread is fully drawn and the tie-off (§6.8) has fired.
5. **Knot truth.** §6.4's knot chapter exists at most once; its button
   performs a real conversion; the disabled state rests at gathering
   geometry; the cinch (§6.9) fires on activation and its reference
   line carries a real reference or does not appear.
6. **JS-off test.** With scripting disabled: thread fully drawn, knot
   tied, sampler woven, forms submittable, prices plain, the 404
   composition complete. Any content reachable only via JS = fail.
7. **Counter-truth audit.** Every `data-measure` figure traces to a
   data source named in the build notes; the drawn percentage in
   §6.12 is §6.2's value restated, not separately computed.
8. **Contrast audit.** No text in `--gold` or `--leaf` on light
   grounds; figures in `--gold-ink` or `--cocoon`; madder ration
   (≤1 madder element per viewport, the knot chapter excepted during
   its pin).

**Standard (must pass, or be consciously waived in the build notes):**

9. Reduced-motion pass: every §6 variant verified — thread drawn
   without glide, fray still and separated, knot pre-tied, sampler
   woven, sway and sheen absent (not frozen).
10. The drop plays once per session and never after a scroll; the
    unspooling word is the page's only kinetic type and ≤9 letters.
11. Frame budget: the shared loop's total per-frame cost ≤1.2ms on a
    mid-tier phone with the thread drawing, one loop and the sway
    concurrently live; §14's cut order verified by disabling in order.
12. The five-second test: a first-time visitor, shown the hero for
    five seconds, can say where the thread is going and why it frays
    at the price — if they describe "a pretty line," the captions and
    the survey have failed, not the visitor.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their in-world
replacement — a refusal without a replacement is a gap, not a stance.

| Component | Treatment in this theme |
|---|---|
| Primary button | The knot button (§§6.4/6.9/6.15): madder, silk label, knot glyph at its reading-start edge; press = cinch or 1px settle |
| Secondary button | `--cocoon` outline on silk, fibre underline on hover (§5); never madder — madder is rationed to the one commitment per page |
| Text link (body) | `--cocoon` text, 1px `--gold-ink` underline (the single-fibre exception, §3); hover draws the underline 180ms |
| Navigation | §6.12's knots on a thread; current = tied + madder + `aria-current` |
| Header | Plain silk band: house name (Cormorant), §6.12 nav, no sticky shadow — a 1px `--gold-ink` hairline appears under the header when the thread's draw passes 2% (the page, not chrome, says you have begun) |
| Cards | §6.14 hanging pieces — the only card form permitted |
| Price display | `--gold-ink` tabular + §6.6 fray + Weaver caption; the price component IS the fray zone |
| Quantity / yardage input | §6.15's measure rule (range + number twin, one tab stop) |
| Text input / textarea | §6.15's ruled fields; valid = tied gold-ink knot glyph; error = madder rule + Weaver-voice caption |
| Select | Ruled field treatment; the native chevron replaced by a small knot glyph (the one place a glyph may indicate a control — it is the theme's own mark, drawn, not an icon font) |
| Checkbox / radio | Small empty square / circle in `--cocoon`; checked = filled with a tied-knot glyph in `--gold-ink`; focus ring standard |
| Table (yardage / care data) | "The cutting table": Karla tabular, rows ruled with hairlines, the thread passes down its left edge in the rail; NO zebra striping (stripes are print-shop language); row hover = the row's fibre underline draws |
| Badge / tag | A woven label: `--silk-deep` rectangle, `--leaf-deep` or `--gold-ink` Karla label text, square corners (woven labels are not pill-shaped — pills are refused) |
| Alert / notice | §6.17's slipped knot, in flow, never an overlay |
| Toast | **REFUSED.** A toast is an interruption from outside the document; the replacement is §6.17's in-flow notice at the place the news concerns, or — for action confirmations — §6.9's reference line at the action itself |
| Modal | **REFUSED.** Nothing in a workshop flies in over the work. Replacement: a dedicated page/section reached by §6.16's pull-through (quick-view of a piece becomes a short detail section, not an overlay) |
| Tabs | **REFUSED.** Sections on a page are places the thread travels between, not panels swapped in place. Replacement: §6.12's knot navigation + scroll; on a piece page, care/shipping details are successive underlined sections |
| Accordion | Permitted, restyled: each item's heading carries a small knot; opening unties it (380ms `--ease-cinch` reversed — the loop opens, §6.17's glyph logic) and the panel settles thread-first; only one open at a time (a line holds one loose knot) |
| Pagination | "Further along the thread": prev/next as text links with knot glyphs; the current position stated as a measured figure ("Pieces 1–12 of 34, measured along the line") — never numbered page pills |
| Progress bar | **REFUSED** as a component — progress is §6.2's thread and §6.12's knots; a bar anywhere is a second progress language and a §9 failure |
| Spinner | **REFUSED** — loading is §6.16's unwoven warp or the §6.15 spooling label |
| Tooltip | **REFUSED.** Detail lives in captions beside the thing (the fray caption is the model) — never in a hover bubble detached from its object |
| Breadcrumbs | A short thread segment in the header's second line with a knot per ancestor; the current page is the untied end. On <768px, collapses to the parent link only |
| Search | A ruled field (§6.15 treatment) whose results re-hang as §6.14 pieces; empty results are §6.18's empty state with a real computed suggestion or none |
| Image / figure | Hung frame (§6.14) with caption inside §6.3's loop reach; silk imagery is photographed matte — glossy product shots on white are off-world (§9-adjacent: imagery is content, and a marketplace packshot breaks the cloth) |
| Divider | The thread itself, or a hairline `--gold-ink` at 40% where the thread does not pass. Wavy/squiggle SVG dividers are FORBIDDEN (§9.1) |
| Footer | §§6.7/6.8/6.17 entire — loose end, sampler, furniture |
| 404 / empty | §6.18's broken thread |

## 12. Content & copywriting voice

Two voices, cast like the two typefaces (§3), and they never swap.

**The Weaver speaks** — Cormorant italic, first person plural of the
house ("we"), the maker talking about the making. Used for: fray
captions, piece notes, the receipt after an order, the tie-off line,
asides in the maker's chapter. The Weaver's sentences are short,
concrete, and priced in real units (hours, metres, dye lots). The
Weaver never sells; the Weaver *admits*.

- ✓ "Priced by the hour at the loom — eleven hours in this one."
- ✓ "Cut from the bolt when you order — never before."
- ✗ "Indulge in the sumptuous luxury of handcrafted elegance."
  (Three banned words in one sentence, and nothing admitted.)
- ✗ "Our premium artisans leverage traditional techniques." (The
  Weaver has hands, not "artisans" who "leverage".)

**The House speaks** — Karla, plain record: labels, apparatus lines,
errors, confirmations, the furniture. The House states facts and
keeps promises; it does not perform folksiness. Apparatus lines are
uppercase label style (§3): "MEASURED FROM THE SPOOL", "THE THREAD
HAS REACHED: THE DYE LOTS", "TIED AT THE FOOT OF THIS PAGE".

**Fixed strings (verbatim — do not paraphrase at build time):**

- Tie-off line (woven label + footer colophon): "Woven and tied by
  [House], [Year]." / the Weaver's sampler line: *"One thread, from
  the cocoon to this corner."*
- Cinch success: "Tied and cinched — [Order/Booking] № [reference]"
- Knot-chapter apparatus: "THE KNOT IS TIED" / "THE KNOT WAITS" /
  (disabled) "THE KNOT WAITS — THE WINDOW IS CLOSED"
- Empty listing: "Nothing hangs on this part of the line." + the
  fact (expected lot/date) or the remedy link.
- 404 headline: "This page was never woven." + apparatus: "THE
  ADDRESS ASKED FOR A PAGE THE HOUSE HAS NOT MADE"

**Error voice (the House, plainly, with the remedy in the same
breath):** an error names what happened, what it costs (nothing, yet),
and the next action. ✓ "The card was refused — the thread has not
been cut, and nothing is owed. Check the number, or write to the
house." ✓ (form field) "The address ends mid-word — the courier will
lose it." ✗ "Oops! Something went wrong." (No "oops" in a workshop;
nothing "went" — things are refused, tangled, or cut short, and the
message says which.) The one weaving metaphor permitted in errors is
the tangle, rationed to system failures: "The thread has tangled on
our side — your measurements are kept. Try the knot again."

**Headline style.** Cormorant headlines name a material fact or a
promise with a number in reach: "Silk, dyed the slow way", "Four
metres left on the mulberry bolt". Banned headline moves: questions
("Ready to elevate your wardrobe?"), superlatives without a measure
("the finest silk in the world" — finest by what ruler?), and the
word "collection" as a headline (it is a listing label, not a
thought).

**Banned words** (greppable at the gate): luxurious, sumptuous,
opulent, indulge, elevate, curated (as praise), premium (as praise),
artisan-crafted, "game-changer", "oops". **Owned words:** spool,
yardage, bolt, warp, weft, reel, dye lot, pinked (edge), measure,
tie off, by the hour at the loom. A page that uses none of the owned
words has not been written in this theme, whatever its colours are.

## 13. Full-page scroll choreography map

The home page, top to footer, in order. (Other page types substitute
their §7 beats; the order discipline — thread first, content second,
one act per viewport — is invariant.)

| Beat | Scroll position | What the visitor sees | What they feel |
|---|---|---|---|
| 1 | Load | The drop falls and settles under the headline (§6.1); "slow" unspools (§6.5) | A presence arrives and chooses its place |
| 2 | 0–8% | The thread begins drawing ahead of the reading (§6.2); hero skein slides at thread-speed (§5) | The line is going somewhere; follow |
| 3 | ~12% | First headline of chapter 2: its underline segment completes 150ms before the chapter settles (thread-first, §5) | Being led, section by section |
| 4 | ~20–35% | The line of pieces (§6.14): spurs draw, pieces settle with the sag; first price frays (§6.6) | A shop that is a place; honesty at the price |
| 5 | ~35% | Hover beat (visitor-paced): the loop around a considered piece (§6.3) | The thread handles what they reach for |
| 6 | ~45–55% | The maker's chapter: underlines only; the thread nearly silent | Restraint — the theme can be quiet |
| 7 | ~60% | A measured figure counts off the spool (§6.10): metres on the bolt | Numbers here are physical |
| 8 | 68–84% | The pin: the knot gathers, tightens, cinches (§6.4); the button inks madder | The journey arrives at its ask |
| 9 | 84–92% | Thread continues, tied but not ended; §6.12's last knot cinches in the nav | Commitment witnessed, page not over |
| 10 | 92–97% | The loose end, swaying (§6.7) | The page is alive at rest; the end is near |
| 11 | 97–100% | The sampler weaves (§6.8); the thread ties into its corner; the sway halves | Filament became cloth; the ending is made, not stopped |
| 12 | 100% | Footer furniture settles below the knot (§6.17) | Paperwork after the work — the visit is complete |

**Reverse pass.** Scrolling up re-spools the thread symmetrically
(§6.2) and un-crosses no acts: pieces stay hung, frays stay separated,
figures stay measured, the knot — once cinched — stays tied (§6.4's
latch). The only things that reverse are the draw itself and the
parallax. A page that un-performs its content on scroll-up teaches
the visitor that nothing here was real.

**Jump-scroll catch-up.** Anchor jumps and scrollbar drags snap the
draw (§6.2's 25% rule); acts whose zones were jumped past take their
terminal states instantly (frays separated, figures measured, pieces
hung) — the visitor who teleports finds a finished page, never a
page mid-ceremony at every section at once.

**Emotional arc.** Arrival (wonder, small) → guidance (trust) →
handling (desire, at the loop) → honesty (respect, at the fray) →
quiet (the maker's chapter) → commitment (the knot) → completion
(the sampler). If a build's arc peaks anywhere but the knot, its
sections are in the wrong order.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home, incl. fonts) | ≤ 780KB; the thread system itself (SVG + JS) ≤ 38KB gz — a line is cheap, and this theme's whole machinery must stay cheaper than one hero photograph |
| Fonts | Cormorant Garamond (500, 600, italic 500) + Karla (400, 600, 700) — 5 files, subset, ≤ 120KB total, `font-display: swap` with the §6.1/§6.5 fonts gates |
| Master path | ≤ 60,000 units surveyed length (§6.2 guard); ≤ 900 path points total across all thread SVGs on the page |
| Animation frame budget | Shared rAF loop ≤ 1.2ms/frame main-thread on a mid-tier phone with draw + one loop + sway live; per-element budgets are stated in §6 and sum under this |
| Long tasks | None > 50ms after first paint; the survey's `getTotalLength()` and re-measures run in the load task or debounced (§6.2), never inside a scroll frame |
| Images | Hero ≤ 180KB (it hangs, it does not perform — it need not be huge); piece images ≤ 90KB each, lazy below the first row |
| Layout shift | CLS ≤ 0.02 — hangers, warps (§6.16) and frames reserve their boxes in markup |

**Cut order (when the budget is exceeded, cut in this order, and
only in this order):** 1. §6.13's sheen sweep (it exists to be cut
first). 2. §5's image parallax. 3. §6.7's amplitude-breathing
modulation (steady sway remains). 4. §6.14's entry swing decay
(pieces settle without the breath). 5. §6.3's loop on touch (the
gutter variant serves all touch). **Never cut:** the draw (§6.2),
the fray (§6.6), the knot (§6.4) and its cinch (§6.9), the sampler
(§6.8), any reduced-motion variant, any fallback. A build that cuts
the fray to save the sheen has understood nothing and fails §10 on
review regardless of its frame rate.

## 15. Build-order checklist

1. **Static cloth first.** Build the complete page with the thread
   FULLY DRAWN, knot tied, sampler woven, frays absent, figures at
   final values, forms submittable. This no-JS page is the product;
   everything after this step is enhancement. Verify §10.6 (JS-off)
   now, not later.
2. **Survey the thread.** Author the master path against the real
   layout at all three breakpoints; record act sub-ranges (underlines,
   loops, knot, frays, tie-off); wire the §10.1/§10.2 geometry checks
   into CI.
3. **The shared loop.** One rAF loop, lerp 0.12, wall-clock based;
   register §6.2's draw as its first citizen. No element gets its own
   loop — a second loop in review is a defect.
4. **The draw + nav.** §6.2's scrub with snap/catch-up rules; §6.12's
   knots keyed to the same boundary events; apparatus line.
5. **Entrance.** §6.1's drop (session-latched, fonts-gated,
   scroll-cancellable), then §6.5's unspool keyed to it; §6.11's
   sequence timings.
6. **Acts in reading order.** §6.14's hanging rows → §6.3's loop →
   §6.6's frays (with the viewport cap) → §6.10's figures.
7. **The knot chapter.** §6.4's pin + scrub + latch + disabled
   geometry; §6.9's cinch wired to the real conversion; reference
   line bound to the real reference.
8. **Forms.** §6.15 entire — ruled fields, measure rule, total + fray,
   spooling label, error covenant (values never cleared).
9. **The ending.** §6.7's loose end → §6.8's sampler + tie-off (and
   the sway halving) → §6.17's furniture. Then §6.18 for the 404 and
   empty states, reusing the ending's furniture.
10. **Transitions & loading.** §6.16's pull-through on internal links;
    warp skeletons only where a fetch owner exists, with the 1200ms
    law implemented and tested by throttling.
11. **Ambient last.** §6.13's sheen and §6.7's sway fade-ins — the two
    loops are added only when everything above is calm, and are the
    first things removed if it stops being calm (§14).
12. **Reduced-motion pass.** Implement every §6 variant as a designed
    state (not `animation: none` sprayed globally); verify the fray
    and the sampler survive it as content.
13. **Audits.** Run §10's blocking eight with measurements, not
    impressions: path count, clearance, fray anchoring, progress
    fractions at four scroll depths, knot truth, JS-off, counter
    tracing, contrast/madder ration. Record the numbers in the build
    notes.
14. **Voice pass.** §12's banned-word grep over all copy; owned-word
    presence check; fixed strings compared verbatim; error messages
    read aloud — if an error sounds like a startup, rewrite it until
    it sounds like a workshop.
15. **The five-second test** (§10.12) with a first-time viewer, then
    ship. If they say "a pretty line," return to step 2 — the survey
    or the captions failed, and no amount of step-11 polish will fix
    it.
