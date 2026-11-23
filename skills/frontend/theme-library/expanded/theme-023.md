# 23. The Printer's Devil — Expanded (v1 + v2)

*Expansion of theme #23 from `themes-001-025.md`, written directly to the
full standard: the 10-part v1 structure plus the v2 deepening layers
(per-element choreography timelines, state matrices, breakpoint behaviour,
edge cases, accessibility specs and token lists; per-theme component
inventory, copywriting voice, three worked examples, scroll choreography
map, performance budget and build-order checklist). Identity preserved
exactly: the apprentice-narrated workshop floor, the same four inks —
Workshop paper `#EFE7D3`, Devil's black `#201D19`, Ink-blue `#2C3E50`,
Thumbprint tan `#B99B6B` — Libre Franklin shouting the job-work posters,
Newsreader carrying the devil's first-person narration, and all 12
original signature elements deepened, not redesigned.*

---

## 1. Concept & world

Every print shop once employed a boy — the printer's devil — who inked
the type, swept the floor, ran the errands and got blamed for everything
that went wrong. This theme hands him the website. The site is his
workshop floor: a spread of paper sheets pinned and stacked on boards,
type locked in iron chases, job-work posters slapped up as sections, and
the evidence of the devil everywhere a careful designer would hide it —
ink fingerprints on the corners he held, pied type (spilled sorts) in one
margin where he dropped the case, a trail of inky footprints across one
sheet he walked over while it was still wet. The mistakes are not a
skin. They are the floor's honest record, and the narration is his:
first person, unrepentant, funny in the way of someone who has been
scolded by every master printer in the county and outlived them all.

The theme's one mechanical law, from which everything else hangs: **ink
is applied by a brayer, and the brayer is real.** A rolling ink brayer
passes over each headline as it arrives and inks it — patchy to solid —
the coverage following the roller's exact position. Headlines are not
revealed; they are *printed*, on the page, in front of the visitor, by
the same tool that then travels the gutter as the page's progress
indicator. When the visitor hovers a headline, the devil runs the brayer
over it again. When they click, he presses. The whole interface is one
boy, one roller, one floor.

**The world in one paragraph.** It is 1890-ish and always slightly after
hours. The master has gone home; the devil is finishing the run by
lamplight. Sheets are workshop paper, warm and toothy. Type is iron —
Libre Franklin at poster weights for anything the shop wants the street
to read, Newsreader italics for everything the devil mutters to you
directly. Nothing on this floor is clean, but everything on it is
*accounted for*: every smudge has a cause, every count is a real tally
of work done on this page, and the one apology on the site is signed.

**Best-fit sites and audiences.**

- Print shops, letterpress studios, riso and screen-print workshops —
  the literal floor. The theme is their trade drawn honestly, and
  printers will check the details (quoin, chase, pied type) the way
  sailors check knots.
- Design studios with a workshop identity and a sense of humour —
  especially studios that still make physical things.
- Maker / DIY brands: toolmakers, paper goods, binders, small-batch
  manufacturers whose product pages benefit from "a person made this,
  here is his thumbprint" honesty.
- Book arts, zine fairs, print festivals, museum shops for print
  exhibitions — anywhere the audience already loves ink.
- A personal portfolio for a designer-illustrator who wants the
  first-person apprentice voice as a narrative device.

**When NOT to use it.**

- Anything that must read as institutionally spotless: banks, insurers,
  medical and legal services. The theme's entire charm is supervised
  mess; a compliance officer will see only the mess.
- Luxury minimalism. This floor has fingerprints on it on purpose.
- Content with no narrator. If the client will not write (or let you
  write) first-person devil copy, the theme collapses into a beige
  vintage skin — the voice *is* the theme.
- Data-dense dashboards. The chase-and-sheet layout composes pages; it
  does not grid 400 rows of telemetry.
- Anywhere a real person's name would be attached to the "mistakes."
  The devil is fictional staff. The apology footnote apologises for
  *him*, never for a named employee or the client.

**The five-second test.** A first-time viewer should say "someone works
here" — not "vintage," not "retro print theme," not "cute." If they
cannot tell you whose floor it is and what he does on it, the build has
failed §10.

---

## 2. Palette

Four inks, no more. The floor owns black, blue, tan and the paper they
land on. There is deliberately **no red and no green**: a two-ink job
plus paper and the boy's thumb. Errors, warnings and success all have to
speak in these four voices (§12 gives them their grammar).

| Token | Hex | Role | Usage ratio | Pairing / contrast |
|---|---|---|---|---|
| `--paper` | `#EFE7D3` | Workshop paper — every sheet, the page ground | ~62% of pixels | Ground for black (13.62:1) and blue (8.91:1) text |
| `--paper-deep` | `#E2D5B8` | Derived: sheet undersides, chase shadow side, skeleton sheets | ~6% | Never carries text; depth cue only |
| `--paper-edge` | `#D8C9A4` | Derived: torn/deckle edges, poster tape marks, hairline rules on paper | ~3% | Decorative lines only |
| `--ink` | `#201D19` | Devil's black — body ink, headline ink at full coverage, poster black | ~18% | On paper 13.62:1 — the only colour body text may use at <18px |
| `--ink-soft` | `#4A453C` | Derived: secondary text, captions, the devil's muttered asides in print | ~4% | On paper ≈7.4:1 — captions ≥12px only |
| `--ink-blue` | `#2C3E50` | Ink-blue — links, data, second poster colour, form focus | ~5% | On paper 8.91:1; paper on blue 8.91:1 (filled buttons) |
| `--blue-deep` | `#22303E` | Derived: blue pressed/hover state, button active | <1% | On paper ≈11.5:1 |
| `--tan` | `#B99B6B` | Thumbprint tan — fingerprints, pied-type spill tint, tape, brass-adjacent warmth | ~2% | On paper 2.14:1 — **decorative only, never text, never an only-signal**; on black 6.36:1 (footer marks may use it) |
| `--tan-deep` | `#93764A` | Derived: fingerprint at full darkness, spill shadow | <1% | Decorative only |

**Hard pairing rules.**

1. Body text is `--ink` on `--paper`. Nothing else, ever, below 18px.
2. `--tan` never carries information alone. A fingerprint, a tape strip
   and a spill tint may *accompany* meaning; the meaning itself is
   always in black or blue. (2.14:1 cannot be read, and the theme knows
   it — that is why the devil's marks are marks, not words.)
3. `--ink-blue` and `--ink` are never adjacent as text-on-text (blue on
   black measures 1.53:1). Blue sits on paper or carries paper.
4. Patchy ink is a **texture mask over solid-colour type**, never a
   colour blend and never an opacity fade of the glyph. The measured
   worst-case local contrast inside a 65%-coverage patch is ≈4.79:1 —
   legal only because (a) it applies to display headlines ≥28px,
   (b) it is a transit state that resolves to 13.62:1 within the pass
   duration, and (c) glyph cores stay solid; the patch lives in the
   glyph's outer 35%. For headlines <28px the coverage floor rises to
   80% (worst case ≈7.73:1). §6.2 carries the full ruling.
5. Poster colour blocking may invert (paper type on a full blue or
   black poster ground) at display sizes only, ≥24px Franklin 700+.

**Dark-mode behaviour — "after hours."** The shop does not invert; the
lamp comes down. Grounds become the black of the ink itself:
`--ink #201D19` becomes the page ground, sheets become `#2A2721`
(derived: black warmed one step toward the tan, "paper seen by
lamplight"), paper text becomes `#EFE7D3` (13.62:1 against the ground,
the same pair reversed), blue lifts to `#7E9BB5` (derived lamplight
blue, ≈5.9:1 on the ground — links and data only, ≥14px), tan stays
`#B99B6B` (6.36:1 on black — the one token that improves after hours).
The brayer, fingerprints and spill are unchanged: ink is ink at any
hour. Skeleton sheets use `#2A2721`; the gutter brayer rides a
`--paper-edge`-at-25% track. A build that simply inverts the palette
fails §10 — the test is whether the fingerprints still read as *on* the
sheet.

**Ink-coverage tokens.** Coverage is a first-class value in this theme:
`--coverage` (0–1 custom property per headline) drives the patch mask.
Floors: `--coverage-start: 0.65` (display) / `0.80` (small), and
`--coverage-full: 1`. No element may rest below its floor's solid state:
coverage always ends at 1.

---

## 3. Typography

Two families, two jobs, and the jobs never swap. **Libre Franklin** is
the shop's iron type: posters, headlines, figures, labels — anything
meant to be read across the room. **Newsreader** is the devil himself:
narration, body copy, asides — anything meant to be read across the
table. A headline set in Newsreader or a paragraph set in Franklin is
a wrong sort in the case, and §9 lists it as a failure mode.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Poster display (hero headline) | Libre Franklin 800 | 64–96px / 0.98 | −0.01em | ALL CAPS permitted only here and on job posters; the hero headline is a poster, inked by §6.2 |
| Headline (section) | Libre Franklin 700 | 34–44px / 1.05 | −0.005em | Sentence case; every section headline gets a brayer pass (§6.2) |
| Sub-headline / poster line | Libre Franklin 600 | 20–24px / 1.15 | 0 | May sit inside job posters (§6.8) as the poster's own line |
| Narration (body) | Newsreader 400 | 18–19px / 1.62 | 0 | First person where the devil speaks; 62–68ch measure |
| Narration italic (asides) | Newsreader italic 400 | 17–18px / 1.55 | 0 | The devil muttering: footnotes, apologies, margin remarks; always signed or clearly his |
| Data / figures | Libre Franklin 500, tabular | 15–28px by use / 1.2 | 0.01em | Counters (§6.11), prices on job tickets, the ink-coverage % — always tabular, always real counts |
| Label / shop mark | Libre Franklin 600 | 11.5–12.5px / 1.3 | 0.14em, UPPERCASE | "INKED:", "SHEETS PRINTED", drawer labels; the only tracked type on the floor |
| Caption / footnote | Newsreader italic 400 | 14.5–15.5px / 1.5 | 0 | The footprint apology (§6.5) lives here |

**Type laws.**

1. **Franklin shouts, Newsreader talks.** If a line would be pasted on
   a wall, it is Franklin. If it would be said to one person, it is
   Newsreader. No third behaviour exists.
2. **Figures are Franklin, always tabular.** A count in Newsreader is a
   wrong sort. The ink-coverage percentage (§6.3) is a figure.
3. **The devil's italics are signed by context.** Italic Newsreader is
   always the devil speaking — narration, asides, the apology. Never
   use italics for generic emphasis inside Franklin-set material;
   posters emphasise with weight and size, like real job work.
4. **No letterspaced lowercase, no underlined links in narration.**
   Links in narration are ink-blue with a 1px underline offset 3px that
   thickens to 2px on hover — a rule drawn under the word, not a
   browser default.
5. **Poster caps are rationed.** ALL-CAPS Franklin appears on the hero,
   on job posters and on labels. A page with more than three caps
   blocks is a wall of shouting; §9 fails it.
6. Line-length: narration 62–68ch; poster lines ≤14 words; the
   devil's sentences run long and comma'd, the posters' run short and
   full-stopped (§12).

---

## 4. Layout language

The page is a **workshop floor seen from above**: a wide board (the
floor itself, `--paper-deep` at the outermost margins on ≥1200px) on
which paper sheets are laid — some squared, some a degree off, all of
them *placed*, none of them floating in a void. Sections are sheets and
job posters on that floor. The grid underneath is strict; the placement
on top of it is allowed exactly the looseness a hand would give it, and
not one degree more.

**The floor grid.**

- ≥1200px: 12 columns, 24px gutters, max content width 1200px, plus a
  **fixed 72px left gutter rail** outside the grid — the devil's gutter,
  home of the travelling brayer (§6.3) and the pied-type spill (§6.4).
  The rail is layout, not decoration: content never enters it, and it
  never enters content.
- 768–1199px: 8 columns, 20px gutters, gutter rail narrows to 48px.
- <768px: 4 columns, 16px gutters, gutter rail collapses into the top
  progress strip (§6.3 breakpoint ruling); sheets stack full-width.

**Sheets.** Every section is a sheet: `--paper` ground, a 1px
`--paper-edge` hairline, a hard offset shadow (`6px 6px 0` in
`--paper-deep`, never blurred — paper does not cast soft shadows
indoors), and corners that may carry one fingerprint (§6.6) or one tape
strip (`--tan` at 55%, 64×18px, rotated −3°). Sheet padding: 40px
desktop, 28px tablet, 20px phone. Sheet rotation: **0° by default**;
a sheet may rest at ±0.4° only if it is a job poster (§6.8) — running
text sheets are always square, because the devil can read straight
even if he can't spell.

**The chase.** The hero and one mid-page section are composed inside a
**chase**: a rectangular iron frame (12px `--ink` border, inner
furniture blocks of `--paper-deep`) that holds type blocks. The chase
is the theme's pinned stage (§6.1, §6.7). Chase dimensions: full
content width, height driven by its composition, never taller than
92vh. Type blocks inside a chase sit on an 8px baseline grid with 16px
furniture gaps; the quoin (a small wedge block, bottom-right) is
visible and is the last thing to move in any lock-up.

**Spacing rhythm.** The floor works in 8px units with three named
measures: **sort** (8px, intra-block), **stick** (24px, between blocks
on a sheet), **forme** (64px desktop / 40px mobile, between sheets).
Vertical rhythm is forme-stick-sort and nothing else; a 13px gap
anywhere is a dropped sort (§9).

**Density rules.** Sheets are dense the way a workshop is dense:
everything on them is *in use*. A sheet may not be more than ~35%
empty paper unless it is a poster (posters earn their air). Whitespace
in this theme is **the floor between sheets** — the deep-paper margin
where the spill lives — not padding inflated inside sheets. If a
section feels empty, the cure is a smaller sheet, never a taller one.

**Placed imperfections — the complete ration.** Imperfection is a
budget, spent deliberately, and §10 counts it:

- Fingerprints: at most **3 per page** (one darkening, §6.6; up to two
  static, printed at fixed 0.5 opacity).
- Pied type: **one spill**, in the gutter, ≤14 sorts (§6.4).
- Footprint trail: **one section**, ≤9 prints (§6.5).
- Sheet rotation: posters only, ≤0.4° at rest (hover tilt is §6.8's).
- Smudge gradients at sheet edges: ≤2 sheets per page, opacity ≤0.08.

A fourth fingerprint is not "more theme." It is a dirty page, and the
devil gets blamed for things he didn't do (§9).

---

## 5. Full motion system

Five named easings, all drawn from the bench:

| Token | Curve | Used by |
|---|---|---|
| `--ease-roll` | `cubic-bezier(0.30, 0.70, 0.20, 1.00)` | The brayer's travel — starts willing, settles as the roller loads |
| `--ease-lock` | `cubic-bezier(0.34, 1.30, 0.40, 1.00)` | Type blocks locking into the chase — a 30% overshoot, the block kisses the furniture and sits |
| `--ease-slap` | `cubic-bezier(0.16, 1.00, 0.30, 1.00)` | Sheets slapped down, posters arriving — fast in, one-frame settle |
| `--ease-press` | `cubic-bezier(0.55, 0.00, 0.20, 1.00)` | The press click squash — slow load, quick release |
| `--ease-drift` | `cubic-bezier(0.45, 0.00, 0.55, 1.00)` | Ambient motion — smudge breathing, fingerprint darkening steps |

**Duration tokens:** `--dur-snap: 120ms` (press click), `--dur-block: 450ms`
(type block slide), `--dur-pass: 950ms` (a full-measure brayer pass,
scaled by headline width per §6.2), `--dur-sheet: 450ms` (sheet-slap
transition), `--dur-count: 800ms` (counter roll), `--dur-ambient: 4000ms`
(smudge breath cycle).

**Every motion term, in this theme's language:**

- **Scroll-triggered reveals** — nothing "reveals" on this floor; it is
  *printed*. Headlines ink under the brayer (§6.2), posters slap up
  (§6.8), sheets arrive with a 12px rise + `--ease-slap` 380ms as their
  top crosses 85% of the viewport. Reveal is a press action or it
  doesn't happen.
- **Scroll-driven / scrubbed animation** — the gutter brayer's journey
  (§6.3) is the page's one true scrub, driven by the shared rAF lerp
  (0.14) against scroll progress; the pinned chase composition (§6.7)
  locks its blocks on scrubbed progress through its 100vh pin.
- **Parallax** — two slow layers only: the floor layer (fingerprints,
  spill, smudge) drifts at 0.92× scroll speed beneath the sheets at
  1.0×. Nothing else parallaxes; paper on a bench does not float in
  depth, and a third layer reads as a website, not a floor (§9).
- **Pinned sections** — exactly two pins per page maximum: the hero
  chase lock-up (§6.1, pin only on ≥1200px and only until lock-up
  completes, ≤60vh of travel) and the chase composition (§6.7, 100vh).
  A third pin fails §10.
- **Smooth scrolling** — the shared loop lerps a virtual scroll value
  (factor 0.14) that drives the gutter brayer, the floor parallax and
  the chase scrub. Native scroll position is never hijacked; only the
  *instruments* are smoothed.
- **Progress indicator** — the gutter brayer + ink-coverage percentage
  (§6.3). There is no progress bar anywhere on the floor; a bar is a
  machine part this shop doesn't own.
- **Staggered reveals** — type blocks into the chase at 120ms stagger
  (§6.1); job posters at 150ms (§6.8); footprint prints at 300ms
  (§6.5). Stagger is a boy working in order, never a cascade of more
  than 6 items.
- **Masked reveals** — the brayer pass is the theme's mask: a clip-path
  edge that follows the roller (§6.2). No other masked reveals; one
  mask, owned by one tool.
- **Blur-to-sharp** — *refused as a reveal.* Wet ink is patchy, not
  blurry; the theme's equivalent is coverage (§6.2). A blurred headline
  on this floor reads as a camera trick, and §9 fails it. (Blur is
  licensed once, inside §6.12's skeleton sheen, at ≤2px, on skeleton
  sheets only.)
- **Kinetic typography** — rationed to the pied sort's tumble (§6.4)
  and the counters' digit roll (§6.11). Type on this floor is iron; it
  does not dance. Letters move when they are *handled* — locked,
  spilled, counted — and sit still when they are read.
- **Marquee** — *refused.* Nothing in a print shop scrolls sideways
  forever; the poster's lines are pasted and stay pasted. The theme's
  substitute for ambient horizontal interest is the footprint trail
  (§6.5), which crosses once and stays.
- **Counters** — sheets printed, sorts set (§6.11): Franklin tabular,
  800ms roll, counted from the page's real DOM (sections printed so
  far, sorts on the page), never invented totals.
- **SVG line-draw** — the footprint trail's connecting scuff (§6.5)
  and the form's ruled lines (§6.16) draw; nothing else. Line-draw is
  the devil's pencil, used where a hand would actually mark.
- **Image scale-in-frame** — photographs sit in job-ticket frames
  (§6.15) and scale 1.06→1 over 700ms `--ease-roll` as the frame
  enters, clipped by the frame — the print being slid into its mount.
- **Hover / magnetic / tilt micro-interactions** — re-ink hover
  (§6.9), poster slap-tilt ≤2.5° (§6.8), press click (§6.10).
  *Magnetic hover is refused*: paper does not lean toward a hand
  before the hand arrives.
- **Custom cursor** — *refused, standing rule.* The system cursor is
  the visitor's own hand; the devil does not lend them his.
- **Skeleton loading** — pale sheets inked by a brayer sweep (§6.12).
- **Page transitions** — the sheet-slap: current sheet lifts off,
  fresh sheet slaps down, 450ms (§6.12).
- **Reduced motion** — every element carries its variant (§6 passim);
  globally: everything fully inked, brayer parked at the gutter's foot,
  spill already spilled, trail already walked, counters at final
  figures. The floor is shown *after* the work, which is a complete
  and honest state.

**Global motion laws.**

1. **One rAF loop.** A single requestAnimationFrame loop lerps the
   virtual scroll (0.14) and publishes `--scroll-p`, `--brayer-y`,
   `--floor-y` and per-headline coverage values. No element runs its
   own scroll listener.
2. **The 900ms promise.** If any inking or lock-up sequence is
   interrupted (tab hidden, trigger broken, JS error downstream), a
   900ms watchdog per element forces its final state: fully inked,
   fully locked, fully counted. No content may sit in a transit state
   longer than 900ms without its animation actively running.
3. **Coverage only rises.** Once inked, a headline never un-inks on
   scroll — except §6.9's hover, which is the visitor asking the devil
   to run the brayer again, locally, and which always ends at full.
4. **The devil works in order.** Sequences are serialised through one
   motion queue: lock-up → inking → counters. Two brayer passes never
   run at once on the same screen; the queue holds a pass until the
   previous finishes or its watchdog fires.

---

## 6. Signature elements

The theme's 12 signature elements (§6.1–§6.12) plus 6 page-family
elements (§6.13–§6.18). Every element carries its full v1 build spec
and its v2 layers: choreography timeline, state matrix, breakpoint
behaviour, edge cases, accessibility spec, tokens consumed.

### 6.1 Chase lock-up entrance

- **What & why.** The hero is composed the way a page was composed: an
  iron chase frame sits empty for one beat, then the hero's own type
  blocks — headline block, narration block, the job poster's block —
  slide in from four sides and lock, the quoin tightens, and only then
  does the headline get inked (§6.2). The visitor watches the page be
  *made* before they read it. It is the theme's thesis in 2 seconds.
- **Structure.** `section.chase` (12px `--ink` frame, `--paper-deep`
  furniture) containing 4–6 `.block` children, each a real content
  block (h1 block, narration block, poster block, figure block).
  Blocks are positioned by the chase grid; pre-lock offsets are
  applied by JS adding `.arming` (transforms up to ±48px toward their
  entry side). Without JS the class is never added and the chase is
  simply composed — the entrance is an enhancement over a finished
  page, per the standing rule.
- **Motion spec.** Trigger: load, after `document.fonts.ready` or a
  300ms cap, whichever first. Blocks slide 450ms `--ease-lock`, stagger
  120ms in reading order (headline block first, quoin last-but-one).
  Quoin tighten: all blocks compress 4px toward the lock point
  (bottom-right) over 200ms `--ease-roll` at +80ms after the last block
  lands. Headline inking (§6.2) starts at quoin +120ms. Total sequence
  ≤2,050ms; the 900ms watchdog (§5) applies per block from its own
  start, not to the whole sequence.
- **States.** Rest (pre-load): composed, fully inked. Arming: blocks
  offset, headline at coverage floor. Locking: as spec. Locked: final
  state, all transforms removed from the DOM (not left as `transform:
  none` residue — the class is stripped) so later hovers start clean.
- **Content merge.** The blocks are the hero's actual content in its
  actual layout. Remove the animation and the hero is identical, pixel
  for pixel. The chase is not a frame around the hero; it is the
  hero's structure, drawn honestly.
- **Failure fallback.** No JS / fonts timeout / IO failure: the chase
  renders composed and inked; the sequence is skipped entirely, not
  half-run.
- **Reduced-motion variant.** No arming, no slide, no quoin. The chase
  is composed on arrival; the headline is fully inked.
- **Performance budget & mobile variant.** Transforms on ≤6 blocks,
  compositor-only (transform/opacity), zero layout after fonts settle.
  <768px: the chase does not arm — blocks stack vertically and only
  the headline inks (§6.2 small-headline ruling); a stacked chase
  sliding from four sides is a drawer emptying, not a lock-up.
- **Choreography timeline (trigger = fonts-ready, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | `.arming` applied; headline block at −48px top, narration at −40px left, poster at +40px right, figure at +32px bottom |
  | 2 | t0 +0–450ms | Headline block slides, `--ease-lock` |
  | 3 | t0 +120–570ms | Narration block slides |
  | 4 | t0 +240–690ms | Poster block slides |
  | 5 | t0 +360–810ms | Figure block slides |
  | 6 | t0 +480–930ms | Pied sort arms at its case position (see §6.4, fires at beat 8) |
  | 7 | t0 +890–1,090ms | Quoin tighten: all blocks compress 4px toward bottom-right, `--ease-roll` |
  | 8 | t0 +1,010ms | Pied sort tumbles (§6.4) |
  | 9 | t0 +1,210ms | Headline brayer pass begins (§6.2) |
  | 10 | t0 +2,050ms | Sequence closed; classes stripped; counters (§6.11) armed |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (composed) | Final layout, inked | Same |
  | Arming | Blocks offset ≤48px, headline at coverage floor | Never occurs (no arming <768px) |
  | Locking | Serialised slides per timeline | Never occurs |
  | Scrolled-past | Identical to rest — the chase never un-locks | Same |
  | Focus during sequence | Sequence continues; focus outline renders on the block's final position, not its animated one | Same |
  | Disabled | n/a — no interactive state on the chase itself | n/a |

- **Breakpoint behaviour.** ≥1200px: full sequence, chase may pin for
  up to 60vh while locking if the hero is taller than the viewport
  (pin releases the moment the quoin lands). 768–1199px: sequence runs
  unpinned, offsets halve (±24px), stagger 90ms. <768px: no arming
  (see budget note); only §6.2 inking and §6.4's spill, already spilled.
- **Edge cases & failure modes.** Fonts loading slowly: the 300ms cap
  starts arming in fallback font only if the headline block uses
  Franklin — if Franklin hasn't arrived, arming waits for the 900ms
  watchdog and then composes instantly rather than locking in the
  wrong face. Tab hidden mid-sequence: rAF pauses; on return, the
  watchdog has already forced final states — the sequence never
  resumes half-done. Content taller than 92vh: the chase grows; pin
  is disabled (a pin taller than its travel reads as a stuck page).
  Scroll-back: nothing reverses; a locked chase stays locked.
- **Accessibility spec.** The sequence is decorative over real DOM
  order: screen readers meet the composed hero immediately (arming
  transforms are visual only, `aria-hidden` never applied to blocks).
  Focus is never moved by the sequence. Headline coverage animation
  does not affect text exposure — the text node is complete from
  first paint. Reduced-motion: see variant. Contrast: headline at
  coverage floor obeys §2 rule 4.
- **Tokens consumed.** `--ink`, `--paper-deep`, `--dur-block`,
  `--ease-lock`, `--ease-roll`, `--coverage-start`, plus scoped
  `--lock-offset: 48px` (24px at 768–1199px).

### 6.2 Brayer inking pass

- **What & why.** The theme's signature and its mask: a rolling brayer
  — roller with a forked handle, drawn as an inline SVG 84×40px at
  desktop scale — passes left→right over a headline as the headline
  enters, and behind the roller the headline's ink goes from patchy
  (65% coverage texture) to solid. The roller *causes* the ink. Every
  section headline on the page gets exactly one pass on first entry.
- **Structure.** Each headline is wrapped in `.inkable` with two
  stacked copies of the same text: `.ink-patchy` (the headline rendered
  with an SVG turbulence mask at `--coverage-start`, glyph cores solid
  per §2 rule 4) clipped by a `clip-path: inset(0 X% 0 0)` whose X is
  driven by `--ink-x`, and `.ink-solid` beneath. The brayer SVG is a
  single shared element, re-parented to the active headline (or
  absolutely positioned against it) — there is only one devil, so
  there is only one brayer (§5 law 4). The patch mask is an SVG
  `<filter>`/`<mask>` pair defined once in a hidden defs block.
- **Motion spec.** Trigger: headline's top crosses 78% of viewport
  height, via the shared loop's IO feed. Pass duration scales with
  headline width: `dur = clamp(600ms, width × 1.35ms/px, 1,400ms)`
  `--ease-roll`. The roller leads the clip edge by 6px (ink lands
  *under* the roller, not ahead of it). Roller rotation: the drum
  rotates 1 turn per 220px of travel (a 70mm brayer circumference,
  stated so two builders match). On completion: patchy layer removed
  from the DOM, coverage set to 1, brayer returns to the gutter
  (§6.3) by the shortest path — it fades its handle first, then slides
  (180ms), never teleports across content.
- **States.** Rest (uninked, below fold): headline shows at coverage
  floor with patch texture — readable per §2 rule 4, because a sheet
  waiting on the bench is still a printed sheet, just a poor pull.
  Inking: per spec. Inked: solid, patch layer gone. Scrolled-past:
  solid forever (§5 law 3). Hover: §6.9. Focus: a headline that is
  also a link inks identically; focus ring is `--ink-blue` 2px offset
  3px, drawn outside the clip so the pass never clips the ring.
- **Content merge.** Patchy and solid are two states of the headline's
  own letters. The brayer inks *this* headline, not a decoration near
  it. Remove the roller and the headline still inks (the clip edge
  alone) — remove the headline and there is nothing to ink.
- **Failure fallback.** The 900ms watchdog: if the pass hasn't
  completed 900ms after trigger (IO fault, hidden tab), coverage snaps
  to 1 and the patch layer is removed. With JS disabled, headlines
  render solid — the patchy layer is JS-inserted, never in the static
  HTML.
- **Reduced-motion variant.** No pass, no patch. Headlines are solid
  on arrival; the brayer stays parked in the gutter.
- **Performance budget & mobile variant.** One pass at a time (§5 law
  4); clip-path + transform on one element; the patch mask is a static
  SVG texture, not a per-frame filter — per-frame cost is one
  custom-property write. Mobile (<768px): pass duration floor drops to
  500ms, roller scales to 60×28px, and headlines <28px use the 80%
  coverage floor (§2 rule 4).
- **Choreography timeline (trigger = headline crosses 78% line, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Brayer leaves the gutter / previous post, handle fades in transit (120ms) |
  | 2 | t0 +120ms | Roller contacts headline's left edge; `--ink-x` at 0% |
  | 3 | t0 +120ms → +120+dur | Roller travels; clip edge follows at −6px; drum rotates 1 turn / 220px |
  | 4 | t0 +120+dur | Roller lifts at the right edge; coverage = 1 |
  | 5 | +180ms | Patch layer removed; brayer slides back to gutter (§6.3 position) |
  | 6 | +900ms max | Watchdog deadline — if beats 3–5 haven't completed, snap to final |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (below fold) | Coverage-floor texture, readable | Same |
  | Inking | Roller + clip per timeline | Same, smaller roller |
  | Inked / scrolled-past | Solid, patch layer removed | Same |
  | Hover | §6.9 re-ink | No hover — first tap inks if somehow uninked, second tap follows the link |
  | Focus | Ring outside clip; pass unaffected | Same |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: full spec, roller 84×40px.
  768–1199px: roller 72×34px, duration scale 1.2ms/px. <768px:
  roller 60×28px, duration floor 500ms, coverage floor 0.80 for
  headlines <28px, and a headline wider than the viewport inks in one
  pass per line (multi-line headlines ink line by line, top line
  first, 90ms stagger — the devil rolls each line like a separate
  pull).
- **Edge cases & failure modes.** Very long headline (3+ lines):
  per-line ruling above; total sequence capped at 2,200ms, after which
  remaining lines snap solid (watchdog). User scrolls fast past a
  headline: if it exits the top before its pass starts, it is inked
  instantly off-screen (coverage only rises; nobody watches an empty
  bench). User scrolls back up: headline is solid (§5 law 3). SVG
  mask unsupported (very old engine): the patch layer never inserts;
  headlines are solid — degrade to print, never to blank. Content
  edited in a CMS to include inline links inside a headline: the clip
  applies to the whole `.inkable`; links remain clickable throughout
  the pass (clip-path does not block hit-testing outside the clipped
  region — links under the un-inked region are still exposed text,
  so they are reachable; the build must not set `pointer-events:
  none` on `.inkable`).
- **Accessibility spec.** Both text copies are real text; the patchy
  copy is `aria-hidden="true"` and the solid copy is the accessible
  one, so assistive tech always reads the finished headline. The
  brayer SVG is `aria-hidden`, `focusable="false"`. Contrast at the
  coverage floor per §2 rule 4 (≥4.79:1 worst-case local, display
  sizes only, resolving to 13.62:1). No focus movement. Touch target:
  the headline itself is not a target unless it is a link (then ≥44px
  height via its line box).
- **Tokens consumed.** `--ink`, `--coverage-start`, `--coverage-full`,
  `--ease-roll`, `--dur-pass`, scoped `--ink-x`, `--brayer-w: 84px`.

### 6.3 Gutter brayer progress

- **What & why.** The page's progress indicator is the devil's brayer
  travelling down the left gutter as you read, trailing the page's
  ink-coverage figure: "INKED: 62%". It is the same brayer that inks
  the headlines (§6.2) — when a pass is called, it leaves the gutter,
  inks, and returns to its scroll position. Progress here is not an
  abstract bar; it is how much of the floor has been printed.
- **Structure.** Fixed rail `.gutter` (72px ≥1200px, 48px tablet,
  hidden as a rail <768px) containing a track line (1px
  `--paper-edge`), the shared brayer element at reduced scale
  (44×22px in the gutter), and a vertical figure readout: the
  percentage set in Franklin tabular, rotated 0° (figures are read
  upright; the devil turns his head, the type doesn't). The percentage
  is computed from real inked state: inked headlines + completed
  sections ÷ total, weighted by section height — the build must
  compute it from the DOM, and §10 tests it against a manual count.
- **Motion spec.** The gutter brayer's `translateY` is scrubbed to
  lerped scroll progress (`--scroll-p` from the shared loop, lerp
  0.14): top of rail at 0%, foot at 100%, travel = rail height −
  brayer height. The drum counter-rotates against travel (it rolls
  *down* the page). The percentage updates when its value changes by
  ≥1%, in whole figures only — no decimals on this floor. When §6.2
  summons the brayer, the gutter instance is the same element: it
  scales up (44→84px width, 200ms `--ease-roll`) as it leaves, and
  the gutter shows a faint parked outline (the roller's rest mark,
  `--paper-edge`) while it's away.
- **States.** Rest (top of page): brayer at rail top, "INKED: 0%" —
  or the true figure if sections above the fold already inked.
  Travelling: per scrub. Away (inking a headline): rest mark shown,
  percentage holds. End of page: brayer at rail foot, "INKED: 100%",
  and the drum gives one full extra turn (360ms) — the devil's
  flourish, the only purely decorative beat in the system, rationed
  to once per page-load. Scrolled-back-up: brayer travels back up;
  the percentage does *not* decrease (coverage only rises, §5 law 3)
  — the figure reads the floor's state, the brayer reads your
  position; they are allowed to disagree, and §12's copy never claims
  otherwise.
- **Content merge.** The indicator is the tool that does the page's
  work, reporting the page's real inked state. It is not a widget
  beside the content; it is the content's own work log.
- **Failure fallback.** If the shared loop fails, the gutter brayer
  parks at the foot and the figure reads the static truth (sections
  inked in the static render = 100%). No JS: the rail renders with the
  brayer parked at the foot and no figure (a figure computed by JS is
  not faked in HTML).
- **Reduced-motion variant.** Brayer parked at the foot of the rail
  for the whole visit; the percentage still updates (it is data, not
  motion) in whole figures.
- **Performance budget & mobile variant.** One transform + one text
  write per frame at most, and the text write only on a ≥1% change.
  <768px: the rail becomes a 44px top strip under the header: brayer
  travels horizontally, figure at the strip's right end. Same element,
  same loop, rotated journey.
- **Choreography timeline.** Continuous (scrubbed) — beats are events,
  not times: scroll → lerp publishes `--scroll-p` → brayer translates
  and drum rotates → figure recomputed on section-ink events (§6.2
  completions, §6.11 tallies) → figure swaps in one frame, no tween
  (figures are struck, not faded).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest / travelling | Per scrub | Top strip, horizontal travel |
  | Away inking | Rest mark in gutter; figure holds | Strip shows rest mark |
  | End of page | Foot position + one drum turn | Same, in strip |
  | Hover | None — the gutter is not interactive | n/a |
  | Focus | The rail is `aria-hidden` decoration around a `role="progressbar"` value (see accessibility) | Same |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: 72px rail, brayer 44×22px,
  figure 15px Franklin. 768–1199px: 48px rail, brayer 36×18px, figure
  13px, rotated into the rail's foot. <768px: top strip (above),
  figure 13px, travel = strip width − 120px.
- **Edge cases & failure modes.** Short page (nothing to scroll):
  brayer rests at the foot, figure reads its true value; the flourish
  turn does not fire (there was no journey). Very long page: no
  change — scrub is proportional. Headline inked while brayer is
  mid-travel: the summon interrupts the scrub position, not the
  figure; on return, the brayer resumes from current `--scroll-p` in
  one frame (it is a tool being carried, not a vehicle). Print
  stylesheet: the whole rail is removed (`display: none` in print —
  §14).
- **Accessibility spec.** The rail is presentational except for one
  `role="progressbar"` element with `aria-valuemin="0"`,
  `aria-valuemax="100"`, `aria-valuenow` = the inked figure and
  `aria-label="Page inked"`. The value updates at most once per
  section completion (never per frame) so screen readers are not
  spammed. The brayer SVG is `aria-hidden`. Contrast: figure is
  `--ink` on the floor ground (13.62:1 against `--paper`; the rail
  sits on `--paper-deep`, where `--ink` still measures ≈11.9:1).
- **Tokens consumed.** `--paper-edge`, `--ink`, `--ease-roll`, scoped
  `--brayer-y`, `--scroll-p`, `--dur-pass`.

---

### 6.4 Pied-type tumble

- **What & why.** Pied type is type that has been spilled and mixed —
  the apprentice's classic disaster. During the hero lock-up (§6.1),
  one sort — a single real letter from the hero headline's own word —
  tumbles out of the chase, bounces once on the floor, and lands in
  the gutter's spill pile, where it stays for the entire page. Every
  section the visitor reads below is read in the company of that
  dropped letter. It never gets swept up. That is the joke, and the
  joke is load-bearing: it proves the floor is a place, not a picture.
- **Structure.** The spilled sort is a `<span class="pied-sort">`
  containing one glyph, set in Franklin 800 at 28px, styled as a type
  block: reversed (paper glyph on an `--ink` block face, 34×34px,
  2px `--paper-deep` base edge so it reads as a piece of metal, not a
  letter in a box). The spill pile is a fixed cluster inside the
  gutter rail (§4): 8–14 static sorts at rest rotations, plus this
  one that arrives. The tumbled glyph is chosen at build time from
  the hero headline (a letter that appears in it, stated in the
  markup — never randomised per visit; the floor is the same floor
  for every visitor).
- **Motion spec.** Trigger: §6.1 beat 8 (quoin +0ms). Path: the sort
  leaves the chase's bottom-left corner, falls 120–180px (to the
  gutter pile) with rotation 0→−210°, 700ms `--ease-lock` modified by
  a gravity curve on the vertical axis (two-property animation:
  translate on `cubic-bezier(0.5, 0, 0.9, 0.4)`, rotate on
  `--ease-lock`), one bounce of 8px (90ms) at landing, settle. Then
  it never moves again — not on scroll, not on hover, not ever.
- **States.** Rest (pre-lock-up): the sort sits in the chase as part
  of the headline block (it is a duplicate display of the glyph; the
  headline's real text is untouched). Falling: per spec. Landed:
  static forever, part of the pile. Scrolled-past: unchanged.
- **Content merge.** The spilled letter is a sort from the hero's own
  case — the same glyph the headline is set in. The pile sits in the
  gutter the brayer travels (§6.3), so the visitor's progress
  indicator passes the evidence of the accident on every journey.
- **Failure fallback.** If §6.1's sequence is skipped (any fallback
  path), the sort renders already in the pile. The pile is complete
  in static HTML; the tumble is JS theatre over it.
- **Reduced-motion variant.** Already spilled. No tumble, no bounce.
- **Performance budget & mobile variant.** One element, one 700ms
  transform animation, once per page. <768px: the gutter is a top
  strip (§6.3), so the spill pile relocates to the foot of the hero
  sheet, left corner, and the sort is already there — a tumble across
  a phone screen crosses content, which the standing rules forbid.
- **Choreography timeline (trigger = §6.1 beat 8, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Sort detaches from chase corner, begins fall + rotation |
  | 2 | t0 +610ms | Sort reaches pile height, rotation at −205° |
  | 3 | t0 +610–700ms | 8px bounce, rotation settles to −210°, base edge lands |
  | 4 | t0 +700ms → ∞ | Static. The pile is complete. |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | In chase | Display duplicate inside headline block | Same |
  | Falling | Per timeline | Never occurs (pre-spilled) |
  | Landed / scrolled-past | Static in pile | Static at hero foot |
  | Hover / focus / active | None — the pile is not interactive; hovering it does nothing, deliberately | Same |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px and 768–1199px: full tumble into
  the gutter pile (fall distance shortens to ~120px on tablet as the
  chase narrows). <768px: pre-spilled at the hero sheet's foot.
- **Edge cases & failure modes.** Hero headline edited so the chosen
  glyph no longer appears in it: the build must re-pick from the new
  headline — §10 includes a check that the spilled glyph occurs in
  the hero headline's text. Short viewport (chase taller than
  screen): the tumble still fires on lock-up; if the pile is
  off-screen at that moment, the sort lands unseen and is simply
  there when the visitor arrives — acceptable, because its *presence*
  is the content, not its journey. Scroll-back: nothing un-spills.
- **Accessibility spec.** Purely decorative: `aria-hidden="true"`,
  not focusable, no text alternative (the glyph duplicates headline
  text that exists accessibly elsewhere). Contrast is irrelevant to
  a decorative metal block, but the block still uses the theme's
  real ink/paper pair. Reduced motion: pre-spilled.
- **Tokens consumed.** `--ink`, `--paper`, `--paper-deep`,
  `--ease-lock`, scoped `--spill-rot: -210deg`.

### 6.5 Ink-footprint trail

- **What & why.** Across exactly one section — chosen at build time,
  ideally the longest reading section — a trail of small ink
  footprints crosses the sheet diagonally, heel-toe, the devil having
  walked over the wet page. The trail draws itself one print at a
  time as the section enters, connected by a faint scuff line, and
  the section's footnote apologises for him by name (§12 gives the
  exact form of words). It is the theme's anti-slop signature: the
  messiest thing on the page, and the most precisely rationed.
- **Structure.** An inline SVG overlaying the section's sheet
  (`position: absolute; inset: 0`, `pointer-events: none`), sized to
  the sheet, containing ≤9 footprint paths (a boot print: sole
  ellipse + heel block, ~26×11px, `--ink` at 0.55 opacity — prints on
  paper are never full black) alternating left/right with a natural
  54px stride, rotated along a diagonal path from the sheet's
  bottom-left quadrant to its top-right, plus one dashed scuff path
  (`stroke-dasharray` drawn) connecting them at 0.18 opacity. The
  prints must route *around* the text block's line boxes where the
  diagonal crosses them — the path is authored per section at build
  time with a 12px clearance from text; the devil walked over the
  margins and the leading, not through the words (§9 fails a print
  that lands on a glyph).
- **Motion spec.** Trigger: section top crosses 70% of viewport. One
  print every 300ms: each print stamps in at 90ms (scale 1.15→1,
  opacity 0→0.55, `--ease-press` — a foot coming down), the scuff
  segment to the next print draws over the same 300ms. Total ≤2,700ms
  for 9 prints. Once walked, the trail is permanent.
- **States.** Rest (below fold): no prints (the SVG is empty of
  visible prints; the section reads clean). Walking: per spec.
  Walked / scrolled-past: full trail at rest opacities. Hover: none.
- **Content merge.** The prints cross the section's own paper, around
  its own text, and the section's own footnote answers for them. The
  trail belongs to this section the way a stain belongs to a page —
  it is in exactly one place because he only walked here once.
- **Failure fallback.** Watchdog at section-entry +900ms per print
  batch: if the sequence stalls, all remaining prints stamp in at
  once at rest opacity. No JS: the trail renders fully walked (it is
  printed in the static SVG; JS hides prints to replay the walk —
  inverted from the usual pattern, and §10 tests the no-JS state
  explicitly).
- **Reduced-motion variant.** Fully walked on arrival. No stamping.
- **Performance budget & mobile variant.** ≤9 small SVG paths + one
  dashed stroke; animation is opacity/transform on paths, no filters.
  <768px: the trail shortens to ≤5 prints and routes down the sheet's
  left margin vertically instead of diagonally (a phone sheet is too
  narrow for a diagonal that clears the text).
- **Choreography timeline (trigger = section at 70% line, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Print 1 stamps (90ms), scuff segment 1 begins |
  | 2 | t0 +300ms | Print 2 stamps; scuff segment 1 completes |
  | 3 | … +300ms each | Prints 3–8, alternating feet, stride 54px |
  | 4 | t0 +2,400ms | Print 9 stamps (the last print is a half-print at the sheet's edge — he stepped off) |
  | 5 | t0 +2,700ms | Trail complete; footnote's apology is already in the DOM (it never animates) |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Clean sheet | Clean sheet |
  | Walking | Prints stamp serially | Same, ≤5 prints, vertical route |
  | Walked / scrolled-past | Full trail, static | Same |
  | Hover / focus | None — overlay is `pointer-events: none` | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: 9 prints, diagonal route.
  768–1199px: 7 prints, diagonal shallows (crosses in the sheet's
  lower third). <768px: 5 prints, left-margin vertical route.
- **Edge cases & failure modes.** Section shorter than the trail:
  prints compress stride to a 38px minimum; below that, prints are
  cut from the middle (the first two and last one always survive —
  he arrived and he left; the middle is negotiable). Section content
  reflows (font swap, resize): the SVG is `preserveAspectRatio=
  "none"` on the scuff only; prints are positioned in % coordinates
  so they track the sheet; if a resize moves a print onto text, the
  print's opacity drops to 0.3 rather than covering a glyph (the
  standing rule outranks the joke). Scroll-back: trail stays walked.
- **Accessibility spec.** Entirely decorative: SVG `aria-hidden`,
  `focusable="false"`, `pointer-events: none`. The apology footnote
  is ordinary text and is the accessible trace of the element.
  Prints at 0.55 opacity are marks, not information (§2 rule 2).
- **Tokens consumed.** `--ink`, `--ease-press`, scoped `--stride:
  54px`, `--print-o: 0.55`.

### 6.6 Darkening fingerprint corner

- **What & why.** On one corner of one sheet — the corner a thumb
  would hold — an ink fingerprint sits printed at low opacity, and
  over the course of the visit it *very slowly* darkens, in steps so
  small the visitor will never catch it moving: the devil is still
  around, still handling the pages. It is the theme's ambient
  heartbeat, and its slowness is the entire design: a fingerprint
  that visibly pulses would be a haunted house effect; this one is
  discovered, on the third visit to the page, already darker than
  you remember.
- **Structure.** An inline SVG fingerprint (concentric ridge arcs,
  authored once, ~54×54px) placed at the bottom-right corner of the
  designated sheet (build-time choice: the longest sheet, where a
  reader's thumb rests), rotated −12°, clipped by the sheet's corner
  radius, `pointer-events: none`. Opacity is a custom property
  `--print-o` starting at 0.34. Up to two further *static*
  fingerprints (0.5 opacity, never animated) may exist on other
  sheets per the §4 ration; this is the only one that darkens.
- **Motion spec.** Trigger: time. Every 20s of *visible, in-viewport*
  time (the sheet on screen, tab focused), opacity steps +0.02 over
  a 1,200ms `--ease-drift` fade, capped at 0.62. The counter pauses
  when the sheet is off-screen or the tab hidden — he only handles
  the page while you're looking at the floor, which is worse, and
  correct. Total possible darkening across a 10-minute visit: 0.34 →
  0.62 in 14 steps. The value is not persisted across visits; each
  visit he starts again.
- **States.** Rest: 0.34. Darkening: stepped per spec. Capped: 0.62,
  still. Scrolled-past: holds its current value (darkening is
  monotonic — fingerprints do not fade).
- **Content merge.** The print sits where a thumb holds *this* sheet,
  on its corner, under its text block's corner — placed at build time
  to overlap only paper, never glyphs (12px clearance, same law as
  §6.5).
- **Failure fallback.** Any failure leaves a static print at 0.34 —
  the resting state is complete. No JS: static at 0.42 (the
  mid-value, chosen so the no-JS floor looks handled, not untouched).
- **Reduced-motion variant.** Static at 0.42 for the whole visit.
  (Opacity stepping is motion; the variant honours it.)
- **Performance budget & mobile variant.** One opacity write per 20s
  — the cheapest element on the floor. All breakpoints identical;
  on <768px the print scales to 44×44px.
- **Choreography timeline.** Ambient: t+20s → fade 1,200ms → hold
  18.8s → repeat, ×14 to cap. Beats are deliberately unremarkable;
  if a tester can perceive a step while watching, the step is too
  big and §10 fails it.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | 0.34 | 0.34 |
  | Darkening | +0.02 / 20s visible, cap 0.62 | Same |
  | Capped / scrolled-past | Holds current value | Same |
  | Hover / focus | None — not interactive, no hover response (a fingerprint that reacts to you is a sensor, not a print) | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** All sizes: same behaviour; size 54px
  ≥768px, 44px <768px. Corner: bottom-right ≥768px; bottom-left
  <768px (the thumb corner of a one-handed phone grip — a detail
  two builders must both get, so it is stated here).
- **Edge cases & failure modes.** Sheet reflows under the print:
  the print is anchored to the sheet's corner, not the content, so
  it cannot drift onto text. Very short visit (<20s): the print
  never darkens — correct; he didn't get to your page yet. Multiple
  tabs: each tab has its own devil; values are per-tab and never
  synced.
- **Accessibility spec.** Decorative: `aria-hidden`, no alternative.
  Opacity changes are not announced. The print is a mark, not
  information (§2 rule 2), and its contrast is intentionally
  sub-text — it must never be the only carrier of anything.
- **Tokens consumed.** `--ink`, `--ease-drift`, scoped `--print-o`.

---

### 6.7 Pinned chase composition

- **What & why.** Mid-page, the visitor meets the chase again — and
  this time they watch a whole section get composed inside it. The
  chase pins for 100vh of scroll while its type blocks lock in one by
  one and the section's lines set line by line, until the forme is
  complete and the pin releases. It is §6.1's entrance grown into a
  full scene: the first section of the site, typeset in front of you.
  One pinned composition per page (§5 pin ration: hero lock-up +
  this).
- **Structure.** A second `.chase` (§6.1's frame language, furniture
  included) wrapping the section's real blocks: headline block, two
  or three text blocks, one figure block, quoin at bottom-right.
  Pinning is `position: sticky` on the chase inside a 200vh track
  (100vh of pinned travel), never JS-positioned. Blocks carry
  `data-set` order. Line-by-line composition: text blocks are split
  at build time into line spans (measured after fonts, re-split on
  breakpoint change) whose ink coverage (§6.2's mask, reused) fills
  per line.
- **Motion spec.** Scrubbed to pinned progress `p` (0–1 across the
  100vh travel), published by the shared loop. Beats: headline block
  locks at p 0.05 (450ms feel, driven by scrub not clock — see edge
  cases); text block 1 locks p 0.25, its lines ink p 0.30–0.45;
  block 2 locks p 0.50, lines p 0.55–0.70; figure block locks p 0.75;
  quoin tightens p 0.90–0.97 (4px compress); pin releases at p 1.0
  with the completed forme. Block lock motion mirrors §6.1 (slide
  from its side, `--ease-lock` character) but is *scrub-mapped*: the
  block's offset is a function of p, so scrolling back un-locks it —
  the one place on the floor where coverage law (§5 law 3) is
  suspended, because the visitor is driving the press by hand. The
  suspension is stated here so two builders rule it the same way:
  inside the pin, and only inside the pin, motion is reversible.
- **States.** Rest (before pin): chase composed-empty — furniture
  visible, blocks at their pre-lock offsets rendered at 35% ink so
  the un-composed state is legible, never blank. Composing: per
  scrub. Composed (p ≥ 0.97): full section, solid. Scrolled-past:
  composed, static, identical to a normal section.
- **Content merge.** The blocks composing are the section itself.
  After the pin, the chase remains as the section's frame — the
  forme stays on the page as the furniture of the content it made.
- **Failure fallback.** If sticky positioning is unavailable or the
  shared loop fails, the chase renders composed (the pre-lock state
  is a JS-applied class; static HTML is the finished section).
  Watchdog: if pinned progress stalls (loop fault), blocks snap to
  composed at the next scroll event.
- **Reduced-motion variant.** No pin. The section appears composed,
  as an ordinary chase-framed section, in normal flow.
- **Performance budget & mobile variant.** Scrub writes are custom
  properties on ≤6 blocks + line spans (≤24) — batched in the shared
  loop, transform/opacity only. <1200px: the pin is cut entirely —
  blocks lock on entry (§6.1's tablet behaviour) and lines ink per
  §6.2. A pinned scene on a small screen traps the reader in the
  devil's demonstration when they came to read; the theme refuses.
- **Choreography timeline (scrubbed; p = pinned progress).**

  | Beat | p | What happens |
  |---|---|---|
  | 1 | 0.00 | Chase reaches pin point; blocks at offsets, 35% ink |
  | 2 | 0.05 | Headline block locks |
  | 3 | 0.25 / 0.30–0.45 | Text block 1 locks; its lines ink top→bottom |
  | 4 | 0.50 / 0.55–0.70 | Text block 2 locks; lines ink |
  | 5 | 0.75 | Figure block locks |
  | 6 | 0.90–0.97 | Quoin compresses 4px; all coverage to 1 |
  | 7 | 1.00 | Pin releases; section scrolls away composed |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (pre-pin) | Blocks offset, 35% ink, legible | Composed section (no pin <1200px) |
  | Composing | Scrub-mapped locks and line inking | n/a |
  | Composed / scrolled-past | Full section in its chase | Full section in its chase |
  | Hover | Headline re-ink available (§6.9) after composition | Tap behaviour per §6.9 |
  | Focus | Focusable content inside is reachable in DOM order throughout; a block's links are inert until its lock beat passes (they are visibly un-set type), then live | All live (no pin) |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: full pin, 200vh track.
  768–1199px: no pin; entry lock-up per §6.1 tablet ruling.
  <768px: no pin, no lock-up; headline inks (§6.2), blocks static.
- **Edge cases & failure modes.** Scrolling back up through the pin:
  composition reverses (the stated suspension) — blocks un-lock in
  reverse order, lines un-ink; this is the visitor running the press
  backwards and it must feel as mechanical as forwards, no easing
  asymmetry. Jump-scroll (anchor link past the section): the section
  renders composed; the pin never engages retroactively. Content
  longer than the design (a third text block): it joins the queue
  (locks p 0.62, lines 0.65–0.78, figure shifts to 0.85, quoin
  0.93–0.98) — the map scales, stated so builders match. Short
  viewport (<640px height): pin travel shortens to 70vh and line
  inking compresses proportionally.
- **Accessibility spec.** During the pin, all text is in the DOM in
  reading order; the 35%-ink pre-state measures ≈3.1:1 at worst —
  below text contrast — so the pre-state is applied **only to blocks
  that are not yet composed AND the composed text is simultaneously
  available to assistive tech** (visual spans are `aria-hidden`
  duplicates; the real text is visually present at full ink in a
  `sr-only`-inverted arrangement is forbidden — instead: pre-state
  ink floor is raised to 55% for any block containing the section's
  only copy of text, giving ≈5.4:1, and the 35% state is used only
  for the headline block whose text is display-size). Focus order
  follows DOM order, never composition order. Pin progress is not
  announced. Reduced motion: no pin (above).
- **Tokens consumed.** `--ink`, `--paper-deep`, `--ease-lock`,
  `--coverage-start`, scoped `--pin-p`, `--lock-offset`.

### 6.8 Job-poster stagger + slap tilt

- **What & why.** The shop's job-work — the posters, tickets and
  notices that are the sections of the page — arrive the way fresh
  sheets are slapped onto a wall: one by one, fast, with a tilt that
  says a hand put them there. Posters are the theme's card/section
  hybrid: Franklin display lines, a rule, the facts. On hover a
  poster tilts like a sheet whose top edge you just lifted.
- **Structure.** `article.poster` — a sheet (§4) with poster
  typography (§3): display line, rule (`--paper-edge` 2px), body in
  Newsreader, a Franklin figure row where the poster carries data.
  Rest rotation from a build-time table (deterministic, not random:
  posters rotate [−0.4°, +0.3°, 0°, +0.4°, −0.3°] cycling by index, so
  every build of the page hangs the same wall). One tape strip
  (`--tan` 55%) at the top edge of posters whose index is even.
- **Motion spec.** Entry: posters rise 14px + rotate from rest+1.2°
  to rest, 380ms `--ease-slap`, stagger 150ms in DOM order, trigger
  per row at 85% viewport line. Hover tilt: rotation increases by up
  to +2.5° around the top edge (`transform-origin: 50% 0`), the far
  corner lifting 6px with the hard shadow growing to `10px 10px 0`,
  220ms `--ease-roll` in, 300ms out — top edge leading, like a sheet
  peeled an inch off the wall. The tilt is toward the pointer's half
  (left half → tilt left) at ≥1200px; a uniform +2° below that.
- **States.** Rest: hung, at table rotation. Entering: per spec.
  Hover: tilted per spec; any links inside remain aligned (the whole
  poster is one rigid sheet — children never counter-rotate).
  Active (pressing a poster's button/link): §6.10's press applies to
  the poster (scaleY 0.98 at the poster's base). Scrolled-past: at
  rest rotation, static. Focus-within: tilt is suppressed and a 2px
  `--ink-blue` outline draws the poster's true rectangle — focus
  must never sit on a rotated target (§ accessibility).
- **Content merge.** The posters *are* the sections — services,
  notices, prices. Their arrival is the wall being pasted for the
  day; their tilt is a hand lifting the sheet you are reading. A
  poster with its motion removed is the same poster, hung.
- **Failure fallback.** Static HTML is the hung wall: posters at rest
  rotation, fully readable. Entry transforms are JS-armed.
  Watchdog per poster: 900ms to rest state.
- **Reduced-motion variant.** Posters arrive hung (no rise, no
  stagger); hover tilt is removed (shadow change only, 0° — a state
  change the visitor can still perceive without motion).
- **Performance budget & mobile variant.** ≤6 posters animate per
  entry batch; transform-only. <768px: rest rotation is 0° for all
  posters (a narrow wall of tilted sheets reads as damage, not
  charm), stagger drops to 80ms, hover tilt n/a (touch: the press,
  §6.10, is the feedback).
- **Choreography timeline (trigger = row crosses 85% line, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Poster 1 rises/rotates in, 380ms `--ease-slap` |
  | 2 | t0 +150ms | Poster 2 (same row) |
  | 3 | t0 +300ms | Poster 3 — stagger caps at 3 per row; a 4th starts a new t0 at its own line |
  | 4 | settle | All at rest rotation; shadows at `6px 6px 0` |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Table rotation, hard shadow | 0° rotation |
  | Entering | Rise + rotate, staggered | Rise only, 80ms stagger |
  | Hover | Tilt ≤2.5°, top-edge origin, shadow grows | n/a |
  | Active | §6.10 press at poster base | §6.10 press |
  | Focus-within | Tilt suppressed, blue outline on true rectangle | Outline only |
  | Scrolled-past | Rest | Rest |
  | Disabled (a poster's sold-out/closed state) | Poster stays hung; its figure row is struck through with a drawn rule (§6.15) and its button disabled — a closed job is still on the wall | Same |

- **Breakpoint behaviour.** ≥1200px: pointer-half tilt. 768–1199px:
  uniform +2° tilt, table rotations halved. <768px: 0° rest, no
  tilt, press only.
- **Edge cases & failure modes.** A poster taller than the viewport:
  tilt origin stays at its top edge; tilt is disabled if the poster
  exceeds 120vh (lifting a sheet taller than you are is slapstick,
  and §9 rations slapstick). Text-heavy poster (client pasted a
  paragraph into a display line): the poster layout holds — display
  line wraps at poster measure, rule and body follow; §12's voice
  rules are the cure, the layout never breaks first. Scroll-back:
  posters do not re-enter; hung is hung.
- **Accessibility spec.** Rotation is visual only; reading order is
  DOM order. Focus-within behaviour above guarantees a rectangular,
  untilted focus target; focus outline is `--ink-blue` 2px, offset
  2px, on the unrotated box. Posters that are links have ≥44px
  targets (the whole poster is the target where it is one card-link;
  inner links are separate targets, never nested). Contrast: poster
  text obeys §2 pairings; inverted posters (paper on blue/black)
  only at ≥24px Franklin 700+.
- **Tokens consumed.** `--paper`, `--paper-deep`, `--paper-edge`,
  `--tan`, `--ink-blue`, `--ease-slap`, `--ease-roll`, scoped
  `--rest-rot`.

### 6.9 Re-ink hover

- **What & why.** Hover a headline and the devil, unasked, runs his
  brayer over it again: the ink's patchiness briefly returns —
  coverage drops to 80% — and refills under the pointer's position,
  the roller tracking the pointer's x within the headline. It is the
  theme's handshake: proof that the ink on this page is wet, the
  tool is live, and the boy is paying attention to what you're
  reading.
- **Structure.** Reuses §6.2's two-layer headline (the patchy layer
  is re-inserted on first hover, then kept, display-toggled). No
  brayer element travels for hover — at headline scale the roller
  would cover the word it inks (standing rule: animated objects
  never cover their content). Instead the *coverage edge* follows
  the pointer: `--ink-x` maps to pointer x clamped to the headline
  box; left of the edge, coverage is 1; right of it, the patch
  shows at the hover floor (0.80).
- **Motion spec.** Pointer enters: patch fades in at the headline's
  right portion over 160ms (coverage floor 0.80 — a hover never
  drops a headline to its entry state; this is a touch-up, not a
  first pull). Pointer moves: the coverage edge follows with the
  shared loop's lerp (0.20 — tighter than scroll, hands are quicker
  than pages). Pointer leaves: coverage refills left→right at
  500ms `--ease-roll` regardless of pointer exit position (he
  finishes the pass properly), patch layer hides at completion.
  Refill is capped: if the pointer re-enters mid-refill, the refill
  pauses and hover behaviour resumes from current coverage.
- **States.** Rest: solid. Hover: patch at ≥0.80 right of the edge.
  Refilling: per spec. Scrolled-past: identical (hover works on any
  inked headline, any number of times — he never tires of it).
  Focus (keyboard): a focused headline-link gets the same touch-up
  once, automatically, edge sweeping left→right over 500ms on focus
  — keyboard visitors meet the devil too.
- **Content merge.** The re-ink acts on the headline's own ink,
  following the visitor's own pointer. It is the §6.2 system,
  localised to a hand's width.
- **Failure fallback.** If the patch layer fails to insert, hover
  does nothing — the headline stays solid. A hover that can leave a
  headline *less* readable than rest is forbidden by construction:
  the floor is 0.80 (worst-case local contrast ≈7.73:1, §2).
- **Reduced-motion variant.** No patch, no refill. Hover state is
  the link underline thickening (§3 law 4) only.
- **Performance budget & mobile variant.** One custom property per
  frame on one headline. Touch: no hover — a long-press (≥350ms) on
  a headline triggers the focus-style auto sweep once; ordinary taps
  are never hijacked.
- **Choreography timeline (trigger = pointerenter, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Patch layer fades in (160ms) at floor 0.80, edge at pointer x |
  | 2 | t0 +160ms → | Edge tracks pointer (lerp 0.20) |
  | 3 | pointerleave | Refill sweeps left→right, 500ms `--ease-roll` |
  | 4 | +500ms | Coverage 1; patch layer hides |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Solid | Solid |
  | Hover | Patch ≥0.80 right of pointer edge | Long-press: one auto sweep |
  | Focus | One auto sweep on focus | Same |
  | Active | §6.10 press (coverage unaffected) | §6.10 press |
  | Scrolled-past | Hover fully available | Same |
  | Disabled | A disabled headline-link shows no patch and no sweep | Same |

- **Breakpoint behaviour.** Identical at all sizes; the coverage
  floor is 0.80 everywhere (the <28px entry floor already applies
  the same value, §6.2, so hover and entry agree on small
  headlines).
- **Edge cases & failure modes.** Pointer skims across five
  headlines in a second: each touch-up is independent and cheap;
  the motion queue (§5 law 4) does not serialise hovers (they are
  not passes), but a headline mid-refill in another section is
  unaffected. Pointer leaves the window mid-hover: refill fires on
  `pointerleave` to `null` target the same way. Headline inside the
  pinned chase (§6.7) before composition completes: hover is inert
  until the block locks (you cannot re-ink what isn't printed).
- **Accessibility spec.** Hover never reduces contrast below
  ≈7.73:1 worst-case local (§2 math at 0.80). The patch layer is
  `aria-hidden`; the accessible text is always the solid copy
  (§6.2). Focus sweep gives keyboard users the same state change;
  nothing about the link's name or role changes on hover. Touch
  targets unchanged.
- **Tokens consumed.** `--coverage-full`, `--ease-roll`, scoped
  `--ink-x`, `--hover-floor: 0.80`.

---

### 6.10 Brayer-press click

- **What & why.** A click on this floor is a press: the clicked
  headline or poster squashes — scaleY 0.97 from its base — while its
  ink darkens 10%, the way a brayer leaned on darkens a pull. It is
  the theme's universal click feedback, used on headlines that link,
  posters, and buttons (buttons get the squash on their plate, §11),
  so the whole site answers a hand with pressure, never with a
  ripple or a glow.
- **Structure.** A `.pressable` behaviour: `transform: scaleY()` with
  `transform-origin: 50% 100%`, and ink darkening via a coverage-adjacent
  property — for text, `color` steps from `--ink` to a 10%-darker
  blend (`--ink` mixed toward black, token `--ink-pressed: #171410`);
  for posters, the sheet's shadow compresses `6px 6px 0` → `3px 3px 0`
  in the same beat, because a pressed sheet sits flatter on the wall.
- **Motion spec.** Press: 120ms `--ease-press` to scaleY 0.97 +
  darkened ink + compressed shadow. Release: 180ms `--ease-roll`
  back. If the click navigates, the press completes its down-beat
  before the §6.12 transition begins (the queue serialises: press
  120ms → transition). Keyboard Enter/Space on a focused pressable
  fires the identical cycle (Space on keyup, per platform
  convention; the down-beat visual tracks `:active`).
- **States.** Rest: full height, standard ink. Active/pressing: per
  spec. Focus: ring per §6.2/§6.8 (the squash never moves the ring's
  box by more than the 3% squash — the outline is drawn on the
  un-squashed box via `outline-offset` compensation, stated so
  builders match). Disabled: no squash, no darkening; a disabled
  pressable sits at 92% ink (visibly un-pressed stock) with
  `aria-disabled` where it is a control.
- **Content merge.** The pressure lands on the thing clicked — its
  own ink darkens, its own sheet flattens. Feedback is the material
  answering, not an effect beside it.
- **Failure fallback.** Without JS, `:active` CSS alone carries a
  reduced version (scaleY 0.98, no shadow change) — the press is
  CSS-first; JS only adds the navigation serialisation.
- **Reduced-motion variant.** No squash. Ink darkens 10% instantly
  on active and restores on release — the information (you pressed
  it) survives without the motion.
- **Performance budget & mobile variant.** Transform + colour on one
  element, 300ms total. Identical on touch (tap = press), with the
  down-beat held a minimum 90ms so a fast tap still registers.
- **Choreography timeline (trigger = pointerdown / keydown, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0–120ms | Squash to 0.97, ink → `--ink-pressed`, shadow compresses |
  | 2 | release / +120ms | Hold if navigating: transition queue takes over (§6.12) |
  | 3 | +180ms | Release curve restores height, ink, shadow |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Full height, `--ink` | Same |
  | Hover | §6.9 (headlines) / §6.8 tilt (posters) — press not yet applied | n/a |
  | Active | Squash + darken per timeline | Same, ≥90ms hold |
  | Focus | Ring on un-squashed box | Ring on focus-visible |
  | Scrolled-past | Press fully available | Same |
  | Disabled | 92% ink, no squash, no darken | Same |

- **Breakpoint behaviour.** Identical at all sizes; squash origin is
  always the element's base (a poster pressed from its top edge
  would look dropped, not pressed).
- **Edge cases & failure modes.** Rapid double-click: the second
  press restarts the down-beat from current scale (no accumulation —
  scale is absolute 0.97, never multiplicative). Press on a headline
  mid-inking (§6.2): the press waits for the pass (queue), because
  pressing wet ink is the one thing even the devil won't do; the
  wait is ≤ the pass remainder and the click is not lost. Drag-off
  release (pointer leaves mid-press): release curve fires from
  current state; no stuck squash — a `pointercancel` handler is
  mandatory, and §10 tests it.
- **Accessibility spec.** The press is feedback, not state: it never
  carries meaning alone (a pressed button that toggles also changes
  its `aria-pressed` and its label's figure, §6.16). Focus ring
  geometry per above. Squash is 3% — below the threshold that
  disturbs reading of the clicked line. Touch targets ≥44px are
  measured un-squashed.
- **Tokens consumed.** `--ink`, `--ink-pressed`, `--paper-deep`,
  `--ease-press`, `--ease-roll`, `--dur-snap`.

### 6.11 Workshop counters

- **What & why.** Two tallies run on this floor, set in Franklin
  tabular figures: **SHEETS PRINTED** and **SORTS SET**. They count
  up as the visitor moves through the page — but what they count is
  the page's real work: sheets printed = sections that have entered
  and been inked; sorts set = the actual glyph count of headlines
  inked so far, computed from the DOM. The devil keeps honest books;
  a counter that invents its total is the one fraud he won't commit,
  and §10 audits the figures against a hand count.
- **Structure.** A counter block (`.tally`) placed in the footer of
  the chase sections and once in the swept-floor footer (§6.17):
  label (Franklin 600 tracked caps, §3) + figure (Franklin 500
  tabular, 28px). Figures are text nodes updated by the shared loop;
  the digit roll is a per-digit `translateY` strip (0–9) inside an
  overflow-hidden window per digit position — iron digits on a
  counting frame, not a slot machine: no blur, no spin past the
  target digit.
- **Motion spec.** Trigger: a section completes inking (§6.2) or a
  headline's pass lands. The affected tally rolls from its current
  value to the new true value over 800ms `--ease-roll`, digits
  rolling upward only, ones column first, carries cascading left at
  60ms per column. Counts are monotonic within a visit (§5 law 3's
  bookkeeping twin). If three sections complete within one second,
  the tally rolls once to the combined true figure — the devil adds
  the pile, then counts it.
- **States.** Rest (page load): both tallies show the true count of
  work already done above the fold (usually SHEETS PRINTED: 1,
  SORTS SET: the hero headline's glyph count, if inked). Rolling:
  per spec. Final (page fully inked): both at their true totals,
  still. Scrolled-past/back: figures never decrease.
- **Content merge.** The tallies are the floor's work log, printed on
  the sheets they count. They live where a tally would live: at the
  foot of the work, in the devil's hand (§6.17 repeats them as the
  day's totals).
- **Failure fallback.** No JS: the footer tally (§6.17) prints the
  static totals computed at build time (total sections, total
  headline glyphs — both knowable statically), and in-page tallies
  are omitted rather than faked at 0.
- **Reduced-motion variant.** Figures update instantly to the true
  value at each trigger. No roll.
- **Performance budget & mobile variant.** Text writes only on ink
  events; the roll animates ≤5 digit strips. Identical on mobile;
  figure size 24px.
- **Choreography timeline (trigger = ink event, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | New true value computed from DOM |
  | 2 | t0 +0–800ms | Digits roll upward, ones first, carries at 60ms/column |
  | 3 | t0 +800ms | Figure rests at the true value; `aria` figure updated (see accessibility) |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | True current figure | Same |
  | Rolling | Digits roll to true value | Same |
  | Final / scrolled-past | True totals, static | Same |
  | Hover / focus | None — tallies are readouts, not controls | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** Identical behaviour; tally block stacks
  label-over-figure <768px.
- **Edge cases & failure modes.** A headline edited in the CMS
  changes the sorts total: the count is computed at runtime from
  live DOM text, so it stays true by construction; the static
  footer fallback is build-time and must be regenerated on content
  change (§15 build order includes the recount step). Glyph count
  definition, stated for matching builds: count = characters in
  inked headlines excluding spaces and punctuation — letters and
  digits the devil actually set. Very large counts (long pages):
  figures group with thin spaces every three digits, Franklin
  tabular handles the width; the roll caps at 5 columns, higher
  columns snap.
- **Accessibility spec.** The rolling figure is `aria-hidden`; a
  sibling `sr-only` text carries the current true value, updated at
  most once per roll completion (`aria-live` off — a tally is
  ambience, and announcing every section would be noise; the value
  is available on demand). Labels are real text. Contrast: figures
  `--ink` on `--paper` 13.62:1.
- **Tokens consumed.** `--ink`, `--ease-roll`, `--dur-count`.

### 6.12 Brayer-inked skeleton + sheet-slap transition

- **What & why.** Loading and leaving are both presswork. While a
  page or a client-fetched section loads, the visitor sees pale
  skeleton sheets — the sheet's true layout in `--paper-deep` blocks
  — and a brayer sweep passes over them, inking the skeleton toward
  solidity; when the real content lands, it lands *as* the inked
  sheet. On navigation, the current sheet is pulled off the press
  and a fresh one slapped down. No spinners exist in this shop;
  waiting is shown as a sheet not yet printed.
- **Structure.** Skeleton: a `.sheet-skeleton` mirroring the target
  layout (headline bar at the headline's measure, text bars at the
  text's line count — mirrored, never generic grey boxes of random
  width; §9 fails a skeleton that doesn't match its sheet). A
  skeleton brayer (the shared element, ghosted at 40%) sweeps it.
  Transition: an overlay sheet (`.sheet-slap`, full viewport,
  `--paper`, chase edge at its foot) that covers on exit and
  uncovers on entry.
- **Motion spec.** Skeleton sweep: the ghost brayer crosses the
  skeleton sheet in 1,100ms `--ease-roll`; behind it, skeleton
  blocks deepen `--paper-deep` → 78% ink-tone. The sweep loops with
  a 600ms pause only while loading persists; minimum skeleton
  display 350ms (no flash-of-skeleton on fast loads). Content
  arrival: skeleton blocks are replaced by real content in place —
  the headline then gets its true §6.2 pass if it hasn't had one.
  Transition: exit — current page's sheet lifts (translateY −2%,
  shadow grows) 180ms while the slap sheet covers from the bottom
  450ms `--ease-slap`; entry — slap sheet lifts off upward 380ms
  revealing the new page already composed (its hero chase does not
  re-run §6.1 on transition arrivals; it arrives locked, headline
  inking only).
- **States.** Loading: skeleton + sweeps. Loaded: real sheet.
  Transitioning out/in: per spec. Idle: no overlay in the DOM (the
  slap sheet is removed after entry, not parked invisible — a
  parked overlay is a future bug).
- **Content merge.** The skeleton is the sheet's own layout waiting
  for its ink; the transition is the press cycle applied to the
  page itself. Both states are the site's material behaving, not a
  loading theme pasted over it.
- **Failure fallback.** Load failure: the skeleton is replaced by
  the §6.18 error sheet (a pied page) with a retry press — never an
  endless sweep; a sweep that runs >6s without content is a failed
  build state, and the element itself swaps to the error sheet at
  6s. Transition failure (route error): the slap sheet lifts back
  off the *same* page and the error is announced in the devil's
  voice (§12).
- **Reduced-motion variant.** Skeleton is static (blocks at 78%
  tone, no sweep); transition is a 120ms crossfade.
- **Performance budget & mobile variant.** Skeleton sweeps animate
  one transform + block tones (custom property), loop cost trivial.
  Transition identical on mobile; the slap sheet's chase edge is
  drawn at the foot only ≥768px (phones get a plain sheet edge —
  the frame would eat 12px of a 360px screen for a 450ms joke).
- **Choreography timeline (navigation trigger, t0).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0–180ms | Current sheet lifts −2%, shadow grows (§6.10's press completes first if a click started this) |
  | 2 | t0 +120–570ms | Slap sheet covers from bottom, `--ease-slap` (450ms) |
  | 3 | covered | Route swaps beneath the sheet |
  | 4 | +0–380ms | Slap sheet lifts upward off the new page |
  | 5 | +380ms | Overlay removed from DOM; new page's headline inks (§6.2) |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Loading | Mirrored skeleton, ghost sweep ≤6s | Same |
  | Loaded / rest | Real sheet; no overlay in DOM | Same |
  | Transitioning | Lift → cover → swap → uncover | Same, plain sheet edge |
  | Hover / focus | n/a during transition; focus moves to the new page's h1 on entry (announced) | Same |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px / 768–1199px: full spec.
  <768px: chase edge omitted on the slap sheet (above); skeleton
  mirrors the stacked layout.
- **Edge cases & failure modes.** Slow network on a client-fetched
  section: the skeleton occupies that section's sheet only; the
  rest of the page is live and readable. Prefetch/back-forward
  cache: on `pageshow` with `persisted`, any parked skeleton or
  overlay state is force-cleared before paint. Slow connection
  (Save-Data / `effectiveType` ≤2g): transitions are disarmed
  (instant swap) and the skeleton shows once-swept, static.
  Scroll-back: n/a.
- **Accessibility spec.** Skeleton container carries `aria-busy=
  "true"` and a visually-hidden "Printing the sheet…" status; on
  load completion `aria-busy` clears and the status updates once.
  Transition: focus is managed (h1 of the new page, `tabindex="-1"`),
  and the swap is announced via the status region — a page change
  the visitor can't see happen must still be a page change they are
  told about. Skeleton blocks are `aria-hidden` (they are not
  content and must not be read as grey gibberish).
- **Tokens consumed.** `--paper`, `--paper-deep`, `--ink`,
  `--ease-roll`, `--ease-slap`, `--dur-sheet`.

---

### 6.13 Floor-board navigation

- **What & why.** The shop's navigation is the job board by the door:
  a horizontal board across the top where the day's jobs are pinned —
  the site's sections listed as job tickets, the current one inked
  darkest with its ticket pulled 4px forward off the board. The devil
  points at it; he does not decorate it. On scroll the board stays
  (a shop's board is by the door, always), compressing its tickets to
  label-only past 140px of scroll.
- **Structure.** `header.board`: the shop name set as a small poster
  (Franklin 800, 22px, one line), then `nav` as a row of `.ticket`
  links — each a mini-sheet (paper ground, hairline, hard shadow
  3px) with a Franklin 600 label. The current page's ticket carries
  `.current` (ink at full, pulled forward via shadow `5px 5px 0` and
  a tan tape strip). A right-side slot holds the one action the shop
  wants (the job-ticket form link, §6.16, styled as a filled blue
  ticket).
- **Motion spec.** On load, tickets slap in with §6.8's entry at
  80ms stagger (they are small sheets; the wall pastes quickly).
  Scroll past 140px: the board compresses — vertical padding 16→8px,
  the shop poster's line steps 22→17px, 240ms `--ease-roll`, with
  hysteresis (expands again below 90px) so it never flutters at the
  boundary. Ticket hover: the ticket lifts its bottom edge —
  rotateX 4° from its top pin, 180ms — a ticket being read. Current
  ticket never lifts (it's already pulled forward).
- **States.** Rest: board full height. Compressed: per spec.
  Hover (ticket): lifted bottom edge. Focus: 2px `--ink-blue`
  outline on the ticket's rectangle (tickets are unrotated, so no
  §6.8 compensation needed). Active: §6.10 press. Current: pulled
  forward, tape strip, `aria-current="page"`.
- **Content merge.** The board is the shop's real wayfinding — the
  tickets are the sections, named as jobs ("The Work", "Prices",
  "Send a Job"). Navigation that looks like the place's own board
  needs no teaching.
- **Failure fallback.** Static header, all tickets visible, current
  marked. No JS needed for any nav function.
- **Reduced-motion variant.** No slap-in (tickets present), no
  compression animation (the board switches height instantly at the
  threshold — or, if the build prefers, never compresses; both are
  legal, state which in the build notes — this spec's reference
  build switches instantly).
- **Performance budget & mobile variant.** Compression animates
  padding/height on one element — use `transform: scaleY` on the
  poster line + padding transition, no layout thrash (the board is
  `position: sticky`, height change pushes content — cap it: total
  height delta ≤18px so the push is one small step, not a scroll
  jump). <768px: the board holds the poster line + a "Jobs" ticket
  that opens the ticket list as a sheet dropped over the page
  (§11 modal treatment); tickets stack vertically, full-width,
  ≥48px tall.
- **Choreography timeline (load, t0 = header paint).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Poster line stamps in (coverage sweep 300ms, §6.2 at label scale) |
  | 2 | t0 +80ms × n | Tickets slap in, 80ms stagger |
  | 3 | scroll 140px | Compression, 240ms |
  | 4 | scroll <90px | Expansion, 240ms |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Full board | Poster + Jobs ticket |
  | Compressed | Past 140px scroll, hysteresis at 90px | Same |
  | Hover | Ticket bottom edge lifts 4° | n/a (tap = press) |
  | Focus | Blue outline, ticket rectangle | Outline in opened sheet |
  | Active | §6.10 press | §6.10 press |
  | Current | Pulled forward + tape, no lift | Same |
  | Disabled | A section not yet open shows as a ticket at 60% ink, not a link, labelled in the devil's voice ("not on the board yet") | Same |

- **Breakpoint behaviour.** ≥1200px: full board, ≤7 tickets.
  768–1199px: ≤5 tickets + a "More jobs" ticket folding the rest
  into the drop sheet. <768px: Jobs-sheet pattern (above).
- **Edge cases & failure modes.** More sections than tickets fit:
  the fold rule above — never shrink tickets below 44px targets to
  cram them in. Long section names: tickets take two lines max,
  then the name is shortened in the ticket only (the devil
  abbreviates job names on tickets; the page itself keeps its full
  name — §12). Sticky failure (old engine): board scrolls away;
  navigation remains reachable in the footer (§6.17 repeats it).
- **Accessibility spec.** `nav` landmark with `aria-label="Jobs on
  the board"`; current ticket `aria-current="page"`; the Jobs sheet
  on mobile is a disclosure (`aria-expanded`, Esc closes, focus
  returns to the Jobs ticket). All targets ≥44px. Contrast: ticket
  labels `--ink` on `--paper` (13.62:1); the blue action ticket is
  paper on blue (8.91:1).
- **Tokens consumed.** `--paper`, `--paper-deep`, `--paper-edge`,
  `--tan`, `--ink`, `--ink-blue`, `--ease-roll`, `--ease-slap`.

### 6.14 Front-sheet hero composition

- **What & why.** The page-family hero: §6.1's chase, §6.2's inking
  and §6.4's spill composed into the standard first screen — chase
  centred on the floor, narration beneath the headline inside the
  chase, the job poster block at the chase's right, and below the
  chase the devil's opening line in Newsreader italic with the
  first tally (§6.11). It is specified separately from §6.1 because
  builders assemble heroes from this recipe, not from the entrance
  spec.
- **Structure.** Floor ground (`--paper-deep` margins ≥1200px) →
  chase (§6.1) containing: headline block (Franklin 800, §3 poster
  display), narration block (Newsreader, ≤34ch inside the chase —
  the devil's greeting, 2–3 lines), poster block (the current job /
  offer as a §6.8 poster at chase scale), figure block (one image in
  a job-ticket frame, §6.15, or a Franklin figure composition).
  Below the chase: the opening line + tally row. Total hero height
  ≤92vh at ≥1200px so the next sheet's top edge shows — the floor
  continues, and the visitor should see that it does.
- **Motion spec.** §6.1's lock-up, §6.2's headline pass, §6.4's
  tumble, §6.11's first tally — in §6.1's timeline order. Nothing
  else moves in the hero. The poster block inside the chase does
  not tilt on hover while the chase is locked (it is under glass,
  in effect); its hover is §6.9-style ink response on its display
  line only.
- **States.** Assembled per §6.1's matrix. The hero's one
  interactive state beyond links: none. A hero with a carousel,
  a video or a second CTA is off-theme (§9).
- **Content merge.** The hero *is* the shop's front sheet: what the
  shop is, in the devil's voice, with today's job pinned in the
  chase. Every block is content a static page would carry in the
  same positions.
- **Failure fallback.** The composed chase, fully inked (§6.1).
- **Reduced-motion variant.** Composed chase; headline solid;
  spill pre-spilled; tally at true figure.
- **Performance budget & mobile variant.** The hero carries the
  page's LCP: the headline is text (no image LCP permitted in the
  hero — the figure block's image is below the headline in paint
  priority and must not be the LCP element; §14 budgets it). <768px:
  chase stacks (headline, narration, poster, figure), no lock-up,
  hero may exceed 92vh — the next-sheet peek rule yields to phone
  reality, stated so builders don't crop copy to keep it.
- **Choreography timeline.** §6.1's ten beats, verbatim. The tally
  row below the chase fades its figures in at beat 10 (they count
  from the hero's own inking).
- **State matrix.** §6.1's matrix applies; add: focus — the hero's
  primary link (inside the poster block) is reachable in DOM order
  after the narration; the lock-up never moves focus.
- **Breakpoint behaviour.** ≥1200px: four-block chase, pin-optional
  per §6.1. 768–1199px: chase 2×2 (headline+narration over
  poster+figure), offsets halved. <768px: single stack, no chase
  frame border on the sides (top and bottom rules only — a chase
  torn to width, echoing §6.16's slip).
- **Edge cases & failure modes.** Headline longer than the chase
  measure at 96px: the display size steps down the §3 scale
  (88/80/72…) until it fits two lines max — a hero headline never
  runs to three lines; if it still doesn't fit, the copy is wrong,
  not the chase (§12 headline law). Missing figure image: the
  figure block becomes a Franklin figure composition (the shop's
  est. date + a drawn brayer at poster scale) — never an empty
  frame.
- **Accessibility spec.** One `h1` (the headline block). Landmarks:
  header (§6.13) then main begins at the chase. The chase frame is
  presentational (`aria-hidden` on frame furniture spans). Alt text
  for the figure image is written as the devil would caption it
  (§12) but must still describe the image — voice never eats
  information.
- **Tokens consumed.** All of §6.1/§6.2/§6.4's, plus `--paper-deep`.

### 6.15 Job-ticket cards

- **What & why.** The listing card of this floor: a job ticket — the
  card a customer would fill in and pin up. Used for services,
  products, portfolio pieces, prices: anything the shop offers as a
  job. A ticket has a perforated top edge (the stub line), the job's
  name in Franklin, its facts in Franklin figures, the devil's one
  line about it in Newsreader italic, and a tear-off action at the
  stub.
- **Structure.** `article.ticket-card`: sheet stock (§4) at card
  scale; top stub separated by a dashed `--paper-edge` rule with
  two punched notches (radial-gradient masks at the rule's ends);
  display name (Franklin 700, 22px); figure row (price/time/size in
  tabular Franklin); italic line (Newsreader, ≤90 chars); action
  link in the stub ("Take this job →" — the stub is the part you
  tear off, so the action lives there). Image, where present, sits
  in a job-ticket frame: 4px `--paper` mount, 1px hairline, the
  photo printed at a slight warm cast (a `sepia(0.12)` ceiling —
  stated, because unbounded filters are how this theme dies, §9).
- **Motion spec.** Entry: §6.8's poster entry (rise + settle,
  120ms stagger within a grid row). Images scale-in-frame 1.06→1,
  700ms `--ease-roll`, on entry. Hover: the card lifts its bottom
  edge 3° (smaller than a poster's 2.5° wall-tilt in feel because
  the origin is the stub — actually rotateX from the top, 200ms),
  shadow `6px→9px`. The stub action, on hover of the card, inks
  from `--ink-soft` to `--ink-blue` — the tear line invites.
- **States.** Rest: hung in the grid. Hover: per spec. Focus-within:
  tilt suppressed, blue outline (§6.8's rule). Sold out / job
  closed: the figure row is struck with a drawn rule (SVG line,
  300ms draw on state change, or pre-drawn if rendered closed) and
  the stub reads "Job's done" in italic — the ticket stays on the
  board; closed work is still the shop's record. Scrolled-past:
  rest.
- **Content merge.** The ticket is the offer's actual paperwork:
  name, figures and the devil's line are the content a listing
  needs, in the form the shop would really pin up.
- **Failure fallback.** Static grid of tickets, fully readable;
  entry is JS-armed. Closed state renders correctly server-side.
- **Reduced-motion variant.** No entry rise, no tilt; image
  arrives framed (no scale); the strike rule is pre-drawn.
- **Performance budget & mobile variant.** Grid entries batch at
  ≤6 per IO batch. <768px: cards full-width, stub action height
  ≥48px, image frame at 3:2.
- **Choreography timeline (entry, per row, t0 = row at 85%).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0ms | Card 1 rises 12px → rest, 380ms `--ease-slap`; its image begins scale-in |
  | 2 | t0 +120ms | Card 2 |
  | 3 | t0 +240ms | Card 3 (row cap) |
  | 4 | t0 +700ms | Images settle at 1.0 |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Hung, stub action soft ink | Same |
  | Hover | Bottom edge lifts 3°, stub action → blue | n/a |
  | Focus-within | Outline, no tilt | Outline |
  | Active (stub) | §6.10 press on the stub | §6.10 press |
  | Closed | Struck figures, "Job's done" stub, action disabled | Same |
  | Scrolled-past | Rest | Rest |

- **Breakpoint behaviour.** ≥1200px: 3 per row. 768–1199px: 2 per
  row. <768px: 1 per row, stub ≥48px.
- **Edge cases & failure modes.** Long job names: two lines max at
  22px, then the card grows — grid rows are masonry-free (equal
  heights per row via the figure row pinned to the stub), so a tall
  card stretches its row, never overlaps. Missing price: the figure
  row shows the devil's line instead ("ask the devil — he knows")
  — a figure row is never left blank, because a blank row reads as
  a bug, not a mystery. Many cards (24+): entry stagger applies
  per IO batch, never a 24-card cascade.
- **Accessibility spec.** Card link strategy: the stub action is
  the card's one link (the display name is not also a link — one
  door per ticket); the whole card is not clickable (tilt + nested
  targets is a trap). Closed cards: stub action `aria-disabled`,
  removed from tab order, strike rule is decorative (`aria-hidden`)
  with "Job's done" as the accessible state. Contrast per §2;
  the sepia ceiling keeps image contrast honest.
- **Tokens consumed.** `--paper`, `--paper-edge`, `--paper-deep`,
  `--ink`, `--ink-soft`, `--ink-blue`, `--ease-slap`, `--ease-roll`.

---

### 6.16 The job-ticket form

- **What & why.** The conversion pattern: the visitor fills in a job
  ticket — the same ticket stock as §6.15, bigger — and pins it to
  the board. Fields are ruled lines on the ticket, labels set as
  shop marks (§3), the visitor's entry appearing on the line in
  Newsreader (handwriting's neighbour). Submitting is pinning the
  ticket up; success is the ticket appearing on the board with a
  thumbprint where the devil received it. Every form on the site —
  contact, order, signup — is this ticket with different fields.
- **Structure.** `form.job-ticket` on a single sheet (58ch max,
  §4 sheet stock, stub edge at top with the form's name as the job
  name). Fields: label (Franklin 600 caps 12px) above a 1px
  `--paper-edge` ruled line; input transparent, 18px Newsreader,
  padding 8px 2px. Required marks: a small ink dot after the label
  (a Franklin full stop at 14px — the shop does not use asterisks;
  the dot is explained once in the form's head line: "Fields with a
  dot are needed. — the devil"). Submit: the **pin button** — a
  filled `--ink-blue` plate, full ticket width, label in Franklin
  600 caps ("Pin it to the board", or the form's own verb, §12).
- **Motion spec.** Focus: the field's ruled line draws in — an SVG
  rule under the field scales 0→100% in `--ink-blue`, 260ms
  `--ease-roll`, from the left (the devil underlining where you're
  writing); the label steps from `--ink-soft` to `--ink`.
  Filled: the line rests at 60% blue. Error: the line turns
  `--ink-blue` full (there is no red on this floor — §2) and a
  devil's note appears in the ticket's right margin: Newsreader
  italic, the error in his voice (§12), with a small drawn arrow
  (SVG, 200ms draw) from note to field. Submit: the pin button
  presses (§6.10), then the whole ticket takes a 2px settle
  (translateY +2px, shadow compresses — the ticket being pinned
  flat) over 300ms while the request sends. Success: the form is
  replaced by the board state — the same ticket, fields now printed
  (not editable), a fingerprint (§6.6's SVG, at 0.5) at its corner,
  and the confirmation line in the devil's voice with the job's
  reference figure (Franklin tabular).
- **States.** Rest: hairlines faint, labels soft. Focus: per spec.
  Filled: line at 60% blue. Error: full-blue line + margin note,
  persistent until corrected (a note on a ticket does not time
  out). Submitting: ticket settled, inputs disabled, button label
  reads "Pinning…". Success: printed ticket + thumbprint +
  reference. The form has no "disabled submit until valid" state —
  the pin button is always live; an invalid submit produces the
  notes (a shop takes your ticket and tells you what's missing; it
  does not refuse the paper).
- **Content merge.** The ticket is the transaction's paperwork in
  the shop's own form. Its states are the states of a real job
  ticket: blank, filled, corrected, pinned, filed.
- **Failure fallback.** Plain HTML form: labels, inputs, native
  validation off only when JS validation is confirmed loaded;
  server-side errors re-render as the same margin notes in text.
  No-JS success is a normal page load to the confirmation sheet,
  which is the same printed-ticket design, static.
- **Reduced-motion variant.** Focus/error states apply instantly
  (line colour steps, notes appear); submit skips the settle;
  success is the same printed ticket.
- **Performance budget & mobile variant.** No loops; transitions on
  focus/submit only. <768px: ticket full-bleed (side borders drop,
  top/bottom rules remain — the torn-to-width ruling, §6.14);
  margin notes move *beneath* their field (a phone ticket has no
  right margin); inputs 18px (also prevents iOS zoom); pin button
  ≥52px tall.
- **Choreography timeline (submit, t0 = pin pressed).**

  | Beat | Time | What happens |
  |---|---|---|
  | 1 | t0 +0–120ms | Pin button press (§6.10) |
  | 2 | t0 +120–420ms | Ticket settles 2px, shadow compresses; inputs disable |
  | 3 | send… | Label "Pinning…"; if send exceeds 1,200ms, the devil's line appears under the button ("He's gone to fetch the master. One moment.") |
  | 4 | success | Form swaps to printed ticket; fingerprint stamps at corner (90ms, §6.5's stamp curve); reference figure counts up (§6.11, 400ms — a short count for a short number) |
  | 5 | error | Ticket un-settles (200ms); notes draw per field; focus moves to the first note's field |

- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Faint lines, soft labels | Same |
  | Focus | Rule draws blue, label inks | Same (on tap-focus) |
  | Filled | Line rests 60% blue | Same |
  | Error | Full-blue line + margin note + arrow | Note beneath field |
  | Submitting | Settled ticket, "Pinning…" | Same |
  | Success | Printed ticket + thumbprint + reference | Same |
  | Disabled | Only during submitting; the button is never pre-disabled | Same |

- **Breakpoint behaviour.** ≥1200px / 768–1199px: margin notes in
  the right margin (ticket at 58ch leaves a real margin inside its
  section sheet at ≥1024px; at 768–1023px notes go beneath fields —
  stated, because margin width, not breakpoint name, is the real
  condition: notes need ≥180px of margin). <768px: notes beneath,
  full-bleed ticket.
- **Edge cases & failure modes.** Long error text: notes wrap to
  ≤4 lines in the margin; beyond that the note shortens and the
  field's `aria-describedby` carries the full text (§12's error
  voice keeps them short by law). Autofill: filled-state line
  applies on `change`, so an autofilled ticket reads as filled,
  not blank-with-text. Double submit: the settled state disables
  inputs at beat 2; a second activation is impossible by
  construction, not by flag. Server rejects after success render
  (async race): never un-print a ticket — the confirmation carries
  its reference; a later failure is a new devil's note delivered by
  the channel the form collected (email), not a UI reversal.
- **Accessibility spec.** Labels are real `<label>`s; the dot is
  `aria-hidden` with "(needed)" in the label's accessible name via
  `sr-only` text — the visual shorthand never eats the semantics.
  Errors: `aria-invalid`, `aria-describedby` to the note's id,
  focus management per beat 5, error summary at the ticket head
  for 3+ errors (a list in the devil's voice, each item a link to
  its field). Contrast: blue line on paper is decorative state;
  the *text* of notes is `--ink` (13.62:1), never blue — blue is
  the underline, ink is the words. Touch targets: fields ≥48px
  hit area via padding; the pin button ≥52px.
- **Tokens consumed.** `--paper`, `--paper-edge`, `--ink`,
  `--ink-soft`, `--ink-blue`, `--blue-deep`, `--ease-roll`,
  `--ease-press`.

### 6.17 Swept-floor footer

- **What & why.** The footer is the floor at closing time: swept,
  the day's tallies chalked — no, inked — at its foot, the shop's
  particulars set as a colophon, and the devil's thumbprint for a
  signature. It repeats the navigation (boards get lost; floors
  don't), prints the day's totals (§6.11's tallies at final
  figures), and carries the one line of legal copy, which the devil
  delivers without enjoying it (§12).
- **Structure.** A full-width `--ink` band (the floorboards after
  hours — the dark-mode ground, used in both modes, so the page
  always ends on the boards): colophon column in paper text —
  line 1: the shop mark as a small poster; line 2: the tallies
  ("TODAY ON THIS FLOOR — SHEETS PRINTED: n · SORTS SET: m",
  Franklin tabular, figures from §6.11's true totals); line 3:
  navigation repeated as plain text links; line 4: the legal line
  and the thumbprint (tan on black, 6.36:1 — the one place tan may
  sit at text-adjacent duty, as a *mark*, §2); a broom-line: a 1px
  `--paper-edge` rule at 30% with a swept gap in the middle where
  the spill pile's last sort rests.
- **Motion spec.** The footer enters like a sheet (rise 12px,
  380ms) — after that, nothing in the footer moves except the
  tallies' final roll (§6.11) when the last section inks above it.
  The thumbprint does not darken here; §6.6's print is on its sheet,
  and one living print per page is the ration.
- **States.** Rest: printed boards. Links: hover underlines draw
  (paper rule, 200ms). Focus: paper outline 2px. Scrolled-past:
  n/a — it is the end.
- **Content merge.** The footer is the day's record: totals of work
  actually done on this page, the shop's name and obligations, and
  the boy's mark. A visitor who reads only the footer still learns
  whose floor it was.
- **Failure fallback.** Static band, build-time totals (§6.11's
  static rule), all links plain.
- **Reduced-motion variant.** No entry rise; tallies instant.
- **Performance budget & mobile variant.** One entry animation.
  <768px: colophon stacks, tallies wrap to two lines, thumbprint
  at the legal line's end.
- **Choreography timeline.** Entry rise at footer top crossing 92%
  of viewport (it is the last sheet; it should barely move, and
  92% is late enough that it usually arrives already settled —
  deliberate).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Printed boards | Stacked boards |
  | Hover (links) | Paper underline draws | n/a |
  | Focus | Paper outline | Same |
  | Scrolled-past | n/a | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: colophon centred at 62ch with
  tallies on one line. 768–1199px: tallies wrap. <768px: stacked,
  thumbprint inline after the legal line.
- **Edge cases & failure modes.** Tallies when JS counted nothing
  (all content above the fold, no ink events): the footer shows
  the runtime's true figures (hero's work counts — §6.11's rest
  state), never 0/0. Legal line length: it is set in Newsreader
  14px and wraps freely; the devil's voice stops at the legal
  line's edge (§12 — legal copy is the master's, verbatim).
- **Accessibility spec.** `contentinfo` landmark. Paper on black
  13.62:1. The thumbprint is `aria-hidden` (a signature mark; the
  name it signs is in text beside it). Tally figures follow
  §6.11's sr-only rule.
- **Tokens consumed.** `--ink`, `--paper`, `--tan`, `--paper-edge`,
  `--ease-slap`, `--dur-count`.

### 6.18 The pied page (404 & empty states)

- **What & why.** A missing page on this floor is pied type: the
  page was set, and then somebody dropped it. The 404 is a sheet
  whose text has spilled — the headline's sorts scattered across
  the sheet in a pied pile, one line of narration upright in the
  devil's voice ("I had that page somewhere. It's pied now — give
  me a minute to sort it."), and the way back offered as the two
  nearest jobs on the board. Empty states (no results, empty
  basket) use the same grammar at smaller scale: an empty chase, a
  line in his voice, one action.
- **Structure.** A sheet (§4) containing: the pied pile (the 404's
  own glyphs as §6.4 sort blocks, pre-scattered at build-time
  rotations in a loose heap, ~40% of the sheet), one upright
  Franklin line ("PIED."), the narration line, and two ticket
  links (§6.13 tickets) to the board's main jobs. For empty
  states: a mini-chase outline (furniture only) + line + action.
- **Motion spec.** On load, three sorts near the pile's edge
  settle (a 40ms, 2px drop each, 90ms stagger) — the pile is still
  settling when you arrive; then stillness. Nothing else moves:
  a page that is lost should not also be busy.
- **States.** Rest: as built. The ticket links carry §6.13/§6.10
  states. There is no hover theatre on a pied page.
- **Content merge.** The error is told in the floor's own accident
  language, and the recovery is the board's real jobs — not a
  generic "go home" (though home may be one of the two tickets if
  it genuinely is a nearest job).
- **Failure fallback.** This *is* the fallback pattern; its own
  fallback is that it is static HTML with working links.
- **Reduced-motion variant.** No settling sorts.
- **Performance budget & mobile variant.** Three tiny transforms,
  once. Mobile: pile shrinks to the sheet's top third, narration
  and tickets below.
- **Choreography timeline.** Load +200ms: sort 1 settles; +290ms:
  sort 2; +380ms: sort 3; then stillness for the life of the page.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Pied sheet, upright line, two tickets | Stacked |
  | Hover / focus | Ticket states only (§6.13) | Press only |
  | Active | §6.10 on tickets | §6.10 |
  | Scrolled-past | n/a (single sheet) | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥768px: pile and text side by side
  (pile left 40%, text right). <768px: stacked, pile first at
  reduced height (heaped in a corner, not a wall).
- **Edge cases & failure modes.** A 404 for a URL that almost
  matches a real job: the devil's line may name the near job
  ("If you meant PRICES, it's on the board.") — only when the
  match is computed from the real route table, never a guessed
  suggestion. Empty search results: the line reports the actual
  query ("Nothing on the floor for 'risograph'. He swept twice.")
  — the query is data, quoted exactly, escaped properly.
- **Accessibility spec.** The pied glyphs are `aria-hidden`
  (scattered letters are not a reading order); the upright line
  is the `h1`; status is conveyed by the page's real HTTP status
  and the heading, not by the visual spill. Links ≥44px.
  Contrast per §2.
- **Tokens consumed.** `--ink`, `--paper`, `--paper-deep`,
  `--ease-press`, scoped `--spill-rot` family.

---

## 7. Page application map

- **Home.** The full floor: §6.14 hero chase, §6.7 pinned
  composition as the first section, job posters (§6.8) for the
  shop's main offers, the footprint trail (§6.5) across the longest
  reading section, tallies (§6.11) in the chase footers, §6.17
  closing the day. All rations (§4) apply at their fullest here —
  home is where the devil shows off, and where over-spending the
  ration is most tempting (§9).
- **Listing (jobs / products / work).** Board header (§6.13), a
  poster-line intro (Franklin, one brayer pass), then §6.15
  job-ticket grids. Filters, where needed, are drawer labels (§11)
  pinned above the grid — tickets are filed, not faceted. The
  gutter brayer (§6.3) still runs; the trail and the darkening
  print do *not* appear on listing pages (their ration is spent on
  home and detail; a trail on every page is a commute, not an
  accident).
- **Detail (one job / product / piece).** The item is one large job
  ticket (§6.15 at full-sheet scale): its image in the ticket
  frame, figures in the figure row, the devil's line longer here
  (a paragraph of narration — detail pages are where he talks
  most). One static fingerprint is permitted on this sheet. The
  conversion is §6.16's ticket pinned at the sheet's foot or in
  its right column ≥1200px.
- **About (the shop / the staff).** A narration-led page: long
  Newsreader, headlines inked as usual, the staff shown as job
  posters with woodcut-style portraits in ticket frames. The
  devil's own poster is the last one and the only one whose italic
  line is in the first person plural ("we sweep up") — a small
  law, kept in §12.
- **Contact / checkout equivalent.** §6.16's job ticket, alone on
  its sheet, board above, boards below. Checkout (multi-step)
  becomes a *stack of tickets*: one ticket per step on one sheet,
  each pinned as completed (printed, thumbprinted) — never a
  wizard with a progress bar; the stack growing is the progress.
- **404 / empty.** §6.18.
- **Article / journal (if the shop keeps one).** Reading sheets,
  square and unrotated, headlines inked, narration measure 64ch;
  the darkening print's sheet is a legal home for the article
  page instead of home (one living print per *site section* is
  still one per page — the ration is per page, and §10 counts per
  page).

## 8. Worked examples

### 8.1 The hero — "Hartley & Rye, Job Printers" (home)

A fictional job printer's front sheet, built end-to-end.

- **Content.** Chase with four blocks: headline block — "WE PRINT
  ANYTHING THAT HOLDS STILL." (Franklin 800, 88px, two lines);
  narration block — "Hartley & Rye, job printers. I do the inking.
  — the devil" (Newsreader, 3 lines); poster block — this week's
  job: "WEDDING INVITATIONS · SET IN CASLON · FROM £90" as a §6.8
  poster; figure block — the shop-front photograph in a ticket
  frame. Below the chase: the opening line ("Mind the wet sheets.")
  and the tally row.
- **Load timeline.** Fonts cap 300ms → §6.1 beats 1–7 (blocks lock,
  quoin at ~+890ms) → pied sort "G" (from "ANYTHING") tumbles at
  +1,010ms into the gutter pile → headline pass at +1,210ms: the
  headline is 940px wide, so `dur = clamp(600, 940 × 1.35, 1400)
  = 1,269ms`, roller crossing until ~+2,480ms → tallies arm; the
  hero's SHEETS PRINTED rolls to 1, SORTS SET rolls to 34 (the
  headline's letters and digits, spaces and stops excluded —
  counted from the DOM, and the worked number here is a check the
  builder re-derives, not a constant).
- **Scroll timeline.** First scroll: the gutter brayer leaves the
  rail top; at the hero's foot the visitor has INKED ≈8%. The
  pinned composition (§8.2) waits below.

### 8.2 Mid-page — the pinned composition, "How a job gets printed"

- **Content.** The §6.7 chase composing a four-block explainer:
  headline block "HOW A JOB GETS PRINTED", text blocks "You bring
  the words…" and "We set them in iron…", figure block (the press
  photograph), quoin.
- **Scroll timeline (200vh track).** p 0.05 headline locks (its
  pass runs as a clock-driven §6.2 once locked — inside the pin,
  the headline inks by clock, the blocks by scrub; the two systems
  meet here and the order is: lock, then ink, stated so builders
  match). p 0.25 block 1 locks; p 0.30–0.45 its five lines ink
  top→bottom. p 0.50 block 2; p 0.55–0.70 lines. p 0.75 figure.
  p 0.90–0.97 quoin. Release at 1.0; the composed chase scrolls
  away as the section's frame, and §6.11 adds its sheets/sorts to
  the tallies as it completes (SHEETS PRINTED +1 at p 0.97).
- **The visitor feels:** they pushed the forme together by
  scrolling. If they scroll back, it comes apart in their hands —
  the one reversible machine on the floor (§6.7).

### 8.3 Conversion — "Send a job" (the job-ticket form)

- **Content.** §6.16's ticket: fields — Your name (dot), Your
  email (dot), The job (select styled as a drawer label row:
  Invitations / Posters / Tickets / Something else), How many,
  When by, Tell the devil (textarea, ruled lines ×3). Head line:
  "Fill the ticket. He'll pin it up today." Pin button: "Pin it
  to the board".
- **Interaction timeline.** Focus on Your name: rule draws blue
  (260ms). Visitor submits with email malformed: ticket
  un-settles, note appears beneath (mobile) / in margin (desktop):
  "That email won't reach anyone — the @ is missing, looks like."
  with arrow; focus moves to the field. Corrected, resubmitted:
  press 120ms → settle 300ms → at +1,200ms still sending, the
  line "He's gone to fetch the master. One moment." appears →
  success: printed ticket, thumbprint stamp at the corner,
  confirmation: "Pinned. Your job is № 214 on the board — we'll
  write before the ink's dry." The № counts up 400ms (§6.11) and
  is the server's real reference, never a generated prop.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Fingerprints everywhere.** A print on every sheet, every
   corner, the logo, the favicon. *Cure:* the §4 ration — 3 per
   page, one alive. Scarcity is what makes a print evidence;
   abundance makes it a pattern, and a pattern is wallpaper.
2. **Random rotation.** Sheets tilted at random angles per page
   load, or running-text sheets rotated "for charm." *Cure:* the
   deterministic poster table (§6.8); text sheets at 0°, always.
   Randomness reads as carelessness — the one thing the devil,
   for all his faults, is not.
3. **Blurred "wet ink" headlines.** Blur-to-sharp reveals pasted
   from another theme. *Cure:* coverage, not blur (§5 refusal).
   Ink is patchy; only cameras are blurry.
4. **Invented counters.** "10,000 sheets printed!" on a brochure
   site. *Cure:* §6.11's DOM-count law, audited in §10. The
   devil's numbers are small and true.
5. **A generic loading spinner** anywhere. *Cure:* §6.12's inked
   skeleton, mirrored to the real layout. A spinner is a machine
   this shop doesn't own.
6. **The devil as a mascot illustration** — a cartoon imp with a
   pitchfork in the corner, waving. *Cure:* he is never drawn.
   His presence is his work: ink, prints, spills, voice. A mascot
   makes him a logo; the evidence makes him a person.
7. **Distressed-texture wallpaper** — coffee stains, grunge
   overlays, torn edges on every sheet. *Cure:* the floor's marks
   are the rationed, authored ones (§4). Texture sprayed from a
   stock pack is the exact slop this theme exists to refuse.
8. **Voice drift** — narration slipping into generic "quirky
   brand" copy, or the devil apologising for the *company's* real
   failings (a 500 page in a funny voice). *Cure:* §12's laws —
   he apologises for ink, never for service; real errors get the
   master's plain voice (§6.18's boundary).
9. **Posters shouting in caps everywhere.** *Cure:* §3 law 5 —
   three caps blocks per page, counted in §10.
10. **The brayer as a logo mark / nav icon / button.** The tool
    appears doing work (§6.2, §6.3, §6.12) or not at all. A brayer
    in the logo is a clip-art shop sign.
11. **Soft shadows and rounded "card" styling** drifting in from a
    UI kit. *Cure:* hard offset shadows only; corners square or
    torn, never pill. Paper in 1890 had no border-radius roadmap.
12. **Footprints through the text.** The trail crossing glyphs for
    the sake of the diagonal. *Cure:* §6.5's 12px clearance law and
    the resize fade rule. The joke never outranks a sentence.

## 10. Quality gate

Blocking items must all pass; standard items need 9 of 11.

**Blocking.**

1. **JS-off test:** with JavaScript disabled, every page is fully
   readable: headlines solid, chase composed, spill spilled, trail
   walked, tallies at build-time truth (§6.17), forms submittable.
2. **Watchdog test:** with IO and rAF deliberately broken, every
   animated element reaches its final state within its 900ms
   promise (§5 law 2); no headline rests patchy, no block rests
   offset.
3. **Coverage audit:** every headline's accessible text is the
   solid copy; patch floors obey §2 rule 4 (0.65 display / 0.80
   small); measured worst-case local contrast ≥4.79:1 in transit,
   13.62:1 at rest.
4. **Truth audit:** the counters, the inked percentage, the form's
   reference figure and the spilled glyph (§6.4) all trace to the
   live DOM or the server — one invented figure fails the build.
5. **Ration audit:** per page — fingerprints ≤3 (one darkening),
   spills = 1 (≤14 sorts), trails ≤1 (≤9 prints), pins ≤2, caps
   blocks ≤3, rotations only per the §6.8 table.
6. **Cursor & cover audit:** system cursor unchanged everywhere;
   no animated element overlaps text at any scroll depth (checked
   at 5 depths, home + detail); the brayer never covers the word
   it is inking (§6.9's no-roller ruling included).
7. **Reduced-motion test:** with `prefers-reduced-motion`, the
   page is the finished floor: inked, locked, spilled, walked,
   tallied — and the pin (§6.7) does not engage.
8. **Print stylesheet:** `@media print` removes the gutter rail,
   overlays, transitions and the slap sheet; sheets print as clean
   paper with solid ink — the floor, filed.

**Standard (9 of 11).**

9. Brayer pass duration matches §6.2's width formula within
   ±50ms; drum rotation is 1 turn / 220px.
10. One rAF loop drives scroll instruments; a full-page scroll on
    a mid-range Android holds 60fps with no theme-attributable
    frame over 20ms.
11. Counters roll upward only, land on DOM-true values, and the
    glyph-count definition (§6.11) is the one in the code.
12. The darkening print's steps are imperceptible in a 60s watch
    test (§6.6) and it pauses off-screen.
13. Poster rotations match the deterministic table; text sheets
    measure 0.0°.
14. After-hours (dark) mode follows §2's lamp ruling — no inverted
    palette, fingerprints still on their sheets.
15. Forms: the pin button is never pre-disabled; errors are margin
    notes in §12's voice with full `aria` wiring (§6.16).
16. Skeleton mirrors its sheet's layout (§6.12) — measured, not
    eyeballed: headline bar within 10% of the real headline's
    measure.
17. Type jobs never swap: no Newsreader headline, no Franklin
    paragraph, figures always Franklin tabular (§3).
18. The five-second test (§1): a first-time viewer says someone
    works here, and can name what he does.
19. Voice spot-check: three sampled devil lines could not be
    pasted into another theme's site unchanged (§12 + the
    anti-filler law).

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their replacement — a
builder must not "fix" a refusal with a default UI kit part.

| Component | Themed treatment |
|---|---|
| Primary button | The pin plate (§6.16): filled `--ink-blue`, paper Franklin 600 caps label, §6.10 press |
| Secondary button | An unpinned ticket: paper ground, 1px `--ink` border, ink label; hover inks its border to 2px (the devil tracing the edge), press per §6.10 |
| Text link | Ink-blue, drawn rule underline (§3 law 4); in narration only — posters link by being tickets |
| Input (text/email/number) | §6.16 ruled-line field |
| Textarea | Ruled lines ×3 (repeating-linear-gradient at the 18px line rhythm), same focus draw on the first line |
| Select | A drawer-label row: the closed select looks like a label pulled from the case (paper, hairline, Franklin label + a drawn ▾ in ink); the open list is a small sheet |
| Checkbox / radio | A sort box: a 18px Franklin-outline square; checked = the box is *set* — filled with ink and the ✓/● reversed out in paper, with §6.10's squash on toggle. Radios are round sorts (the shop owns a few) |
| Toggle switch | **Refused.** A job is pinned or it isn't: use the checkbox sort, or a two-ticket choice (§6.15 tickets as radio cards) |
| Table | A ledger sheet: Franklin header row (caps, ruled under with 2px ink), Newsreader rows, figure columns right-aligned tabular; row hover = a faint tan wash at 8% (a thumb passed over the line) |
| Badge / tag | A small tape strip (`--tan` 55%, Franklin 600 11px caps, ink text at 13.62:1 against the tan's paper backing — tape sits on paper, text sits on the tape's paper side; where contrast is in doubt the badge is a paper chip with a tan edge) |
| Alert (info) | A devil's note pinned at the sheet's head: italic Newsreader, ink, with a drawn pin dot; never a coloured banner |
| Alert (error) | §6.16's margin note pattern, or §6.18's pied grammar for page-level failure; there is no red — urgency is carried by placement and voice, not hue |
| Toast | **Refused.** News on this floor is pinned to a sheet (§6.16 success, §6.17) or it isn't news. A confirmation that vanishes in 4s is a rumour |
| Modal | A sheet slapped over the floor: full sheet (§4 stock) centred, floor dims to `--ink` at 55% behind it, entry = §6.12's slap at modal scale (300ms); Esc lifts the sheet off |
| Pagination | The board's job numbers: Franklin figures as tickets; current = pulled forward (§6.13); prev/next are tickets labelled in voice ("Older jobs", "Newer jobs") |
| Tabs | Drawer labels on the case: a row of label holders (paper-edge rules), the open drawer's label inked full with its tab pulled 3px down — you are looking into that drawer |
| Accordion | Type blocks in a chase: opening a block slides the furniture (other blocks) apart 200ms `--ease-lock`; only one block open per chase |
| Search | A ticket field (§6.16) labelled "Look on the floor for…" with results as §6.15 tickets; the empty result is §6.18's mini-chase |
| Breadcrumb | The devil's directions, in italic: "You are: Board → Prices → Wedding invitations" — set as one narration line, links blue |
| Progress bar | **Refused** (§5). Progress is the gutter brayer (§6.3) or a growing stack of pinned tickets (§7 checkout) |
| Spinner | **Refused** (§6.12). Waiting is an unprinted sheet |
| Tooltip | A margin note: italic Newsreader on a paper chip, appearing 300ms after hover/focus beside its word — the devil explaining in the margin, where explanations live |
| Divider | A drawn rule: 1px `--paper-edge`, or for section breaks the torn edge (SVG, §6.15's notch family) |
| Avatar / portrait | Woodcut-style duotone in a ticket frame (§6.15); never a circle crop — paper is square |
| Price / figure block | Franklin tabular, always (§3 law 2), with the unit in the label voice (§12) |
| Skip link | A plain paper ticket at the page's top-left on focus: "Skip to the work" |

## 12. Content & copywriting voice

Two voices, matching the two typefaces (§3 law 1). **The Poster**
(Franklin) says what the shop offers, in short lines, full stops, no
exclamation marks — job work never shouts about itself, it is simply
large. **The Devil** (Newsreader, often italic) says everything else,
first person, present tense, dry.

**Headline style (Poster).** ≤9 words, a statement or an offer, set
as fact: ✓ "We print anything that holds still." ✓ "Wedding
invitations, set by hand." ✗ "Print Your Dreams Today!!!" (shouting,
exclamation, and a promise no shop can keep). ✗ "Welcome to our
website" (a poster that welcomes is a poster wasted).

**Label style.** Franklin caps, a noun and no verb: "INKED:",
"SHEETS PRINTED", "THE JOB", "WHEN BY". Labels are shop marks, not
sentences.

**The Devil's narration.** First person singular, comma-rich,
unhurried, funny by understatement: ✓ "I do the inking. The master
does the spelling, which is why the posters are right and this
sentence is long." ✓ "Mind the wet sheets." ✗ "Oops! Looks like
something went wrong lol" (he is not a chatbot; he has never said
"oops" or "lol" in 130 years). ✗ Third-person brand voice anywhere
he should be speaking ("Our team is passionate about print" — the
team is one master and a boy; say so or say nothing).

**Error voice.** His fault-domain is ink, paper and his own feet —
never the visitor's competence and never the company's service:
✓ (form) "That email won't reach anyone — the @ is missing, looks
like." ✓ (load failure) "The sheet didn't come off the press. Try
the handle again." (retry button: "Try the handle"). ✗ "Invalid
input." ✗ Any error that blames the visitor ("You entered…") — the
devil blames the materials and himself, in that order.

**The apology law.** The footprint footnote (§6.5) and its kin
follow one form: the devil is named, the fault is his, it is not
really an apology: ✓ "The footprints are the devil's. He walked over
it wet. He has been told." He apologises for ink, spills and
footprints. He never apologises for prices, delays or policy —
those are the master's, in the master's plain voice, outside the
narration (§9 failure mode 8).

**Empty-state voice.** ✓ "Nothing on the floor for 'risograph'. He
swept twice." — the fact (nothing found), the evidence (he looked),
no pleading.

**Success voice.** Short, filed, with the figure: ✓ "Pinned. Your
job is № 214 on the board." ✓ "Done. He'll write before the ink's
dry."

**Banned words and constructions.** "Oops", "lol", "awesome",
"leverage", "synergy", "solutions" (the shop does *jobs*), "user"
(he says "you"), exclamation marks in Poster voice (rationed to
zero), "just" in error messages, and any sentence that could be
pasted onto a bakery's website unchanged (the anti-filler law,
applied to copy).

**Fixed strings (verbatim in every build).** Gutter readout:
"INKED: n%". Tallies: "SHEETS PRINTED", "SORTS SET". Form head
note: "Fields with a dot are needed. — the devil". Skeleton status:
"Printing the sheet…". These strings are part of the theme's
furniture; translating the site translates them as units.

## 13. Full-page scroll choreography map

Home page, top to footer. (Other page types inherit the beats that
apply; §7.)

| # | Scroll position | Beat | What the visitor sees and feels |
|---|---|---|---|
| 0 | Load | §6.1 lock-up + §6.4 tumble + §6.2 hero pass | The page is made in front of them; a letter escapes |
| 1 | First scroll | §6.3 brayer leaves the rail head; floor layer drifts at 0.92× | The tool comes with you |
| 2 | Hero foot | §6.11 tallies rest at hero totals; INKED ≈8% | The books are open |
| 3 | §6.7 pin engages | Composition begins: blocks lock on scrub | You typeset the explainer by hand |
| 4 | Pin mid | Lines ink; quoin at p 0.90 | The forme tightens |
| 5 | Pin release | Composed section scrolls away in its chase | The work stays; the frame was its furniture |
| 6 | Posters row | §6.8 stagger slap-in, 150ms | The day's jobs go up on the wall |
| 7 | Long reading section | §6.5 trail walks (300ms/print); §6.6's print is on this sheet, darkening on its own clock | Somebody has been here before you |
| 8 | Each headline | §6.2 pass, queued serially (§5 law 4) | Every headline is printed as it arrives — the rhythm of the page |
| 9 | Ticket grid | §6.15 entries per row | The offers are paperwork, pinned in rows |
| 10 | Form sheet | §6.16 ticket at rest; focus draws its rules as used | The paperwork invites a hand |
| 11 | Footer top | §6.17 rises 12px at the 92% line; tallies show the day's true totals | Closing time; the books balance |
| 12 | Scroll back up | Coverage stays (law 3); brayer travels back; the pin (§6.7) alone reverses | The floor remembers what was printed |

**Emotional arc, stated so builders pace it:** *making* (hero) →
*working* (pin) → *the day's wall* (posters, tickets) → *the
evidence* (trail, print) → *the paperwork* (form) → *closing time*
(footer). A build that spends its loudest beats late (a poster
cascade in the footer, say) has the arc backwards.

**Jump-scroll catch-up.** Anchor jumps and restored scroll
positions land on a finished floor: everything above the landing
point is inked, locked and tallied instantly (computed from the
landing position, not animated). The visitor never watches a page
print itself backwards to catch up with them.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Initial HTML+CSS+JS (gz) | ≤140KB (fonts excluded, counted separately) |
| Fonts | Franklin (2 weights: 700, 800; 600 swapped in via 700 if budget tightens) + Newsreader (400 + italic) ≤110KB total, `font-display: swap` with the §6.1 300ms cap |
| Images | Hero figure ≤120KB (it must not be LCP, §6.14); ticket images ≤60KB each, lazy below the fold |
| SVG assets | All theme SVGs (brayer, fingerprint, footprints, spill sorts are DOM) inline; total inline SVG ≤18KB |
| Animation frame budget | Shared loop ≤4ms/frame of JS on a mid-range Android; per-frame writes limited to custom properties on ≤8 elements + the active §6 element |
| Long tasks | None >50ms attributable to theme code; the DOM glyph count (§6.11) runs once per ink event, never per frame |
| LCP | ≤2.2s on 4G Moto-class: the headline is text and paints before its pass — coverage never delays paint |
| CLS | ≤0.03: chase blocks are laid out at final geometry before arming (arming transforms do not move layout) |
| INP | ≤200ms; the press (§6.10) is transform/colour only |

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead): 1) the darkening print's stepping (ship it static at
0.42); 2) the floor parallax layer (sheets still sit on
`--paper-deep` margins); 3) §6.7's pin → entry lock-up (§6.7's own
tablet ruling); 4) poster entry stagger (posters arrive hung);
5) the footprint trail's stamping (trail pre-walked). **Never cut:**
the §6.2 inking system, the fallbacks/watchdogs, the counters'
truth, or any reduced-motion variant — those are the theme, the
rest is its weather.

**Print.** The `@media print` rules of §10 item 8 are part of the
budget: a page that prints as a clean sheet has proven its paper
was real.

## 15. Build-order checklist

1. Static floor first: sheets, chase, posters, tickets, footer —
   fully readable with no JS, headlines solid, spill spilled,
   trail walked, static tallies computed (§6.17). Gate: §10 item 1
   passes before any motion exists.
2. Design tokens: palette (§2), type scale (§3), easings and
   durations (§5) as CSS custom properties with the exact names
   §6 cites.
3. The shared rAF loop with `--scroll-p` and the motion queue
   (§5 laws 1, 4) + the 900ms watchdog utility (§5 law 2) —
   before any element that will use them.
4. §6.2's two-layer headline system + SVG patch defs; verify §2
   rule 4's floors with the real fonts.
5. §6.3 gutter brayer (it is §6.2's brayer's home; build them as
   one element with two posts).
6. §6.1 lock-up + §6.4 tumble (they share a timeline; build
   together, test the no-JS and watchdog paths).
7. §6.7 pinned composition (desktop only; verify the <1200px
   ruling early — it changes the DOM order of work).
8. §6.8 posters + §6.15 tickets (shared entry system), then
   §6.13 board, §6.14 hero assembly from the parts.
9. §6.9 re-ink + §6.10 press (interaction layer, after all
   headlines and pressables exist).
10. §6.11 counters — with the DOM-count function unit-checked
    against a hand count of a fixture page (the §10 truth audit
    starts here, not at review).
11. §6.5 trail + §6.6 print (the rationed marks, placed last so
    their placement is judged against finished sheets).
12. §6.16 form + §6.18 pied page (conversion and failure, the two
    states a demo build forgets).
13. §6.12 skeleton + transition (only once routes/sections exist
    to load).
14. Reduced-motion pass: walk every element's variant; run §10
    item 7.
15. After-hours (dark) pass per §2; print stylesheet per §10
    item 8.
16. Full §10 gate, in order, with the five-second test last and
    out loud.

---

*End of theme #23 — The Printer's Devil, expanded to the full
v1 + v2 standard. Word count and element count are reported by the
expanding agent on delivery; the file's own §10 is the authority on
whether a build of it may ship.*
