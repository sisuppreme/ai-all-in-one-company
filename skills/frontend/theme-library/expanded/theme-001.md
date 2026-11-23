# Theme 001 — The Midnight Press Run (Expanded)

*Expansion of theme #1 from `themes-001-025.md`, written to the 20x-depth
standard in `EXPANSION-STANDARD.md`. Identity is unchanged from the source
entry — same concept, same four anchor colours, same two typefaces, same
twelve signature elements — deepened to full build specification.*

---

## 1. Concept & world

**The world.** It is 2 a.m. on the floor of a working newspaper pressroom.
The edition has been locked, the plates are on the cylinder, and the first
sheets are coming off the press still warm, the ink still wet enough to
smudge a thumb. The Midnight Press Run designs for that exact moment — not
for the finished, folded, doorstep newspaper that every other editorial
theme imitates, but for the *act of printing itself*: type being struck,
rules being drawn, sheets feeding through with a whisper of misregistration
that settles as the run finds its rhythm. Every surface on the page should
feel minutes old. A headline is not "displayed"; it has just been printed.
A photograph is not "placed"; it has just come through the halftone screen.
A progress bar is not a UI widget; it is the ink filling the front page's
own top rule as the reader works down the sheet.

**The mood.** Urgent but unhurried. A pressroom at night is loud machinery
operated by calm people who have done this ten thousand times. The design
equivalent: bold, heavy, condensed type and one loud editorial red, handled
with total restraint everywhere else. Nothing on the page shouts except the
things a real front page shouts — the lead headline and the EXTRA box.
Everything else is ink, paper, and hairlines.

**The reader's felt experience, in sequence.** (1) The masthead lands like
a stamp — the paper announces itself before any story does. (2) The lead
headline is struck line by line, so the reader watches the news *happen*.
(3) As they read down, the sheets feed, the margin cylinder turns, the ink
rule fills: the page quietly proves it is alive and keeping pace with them.
(4) Nothing ever floats, glows, or bounces. Things print, draw, roll, and
settle. The whole vocabulary is mechanical and final — once ink is on
paper, it does not move again, and neither does anything in this theme once
its entrance is done.

**Best-fit sites and audiences.**

- Independent journalism and digital newspapers — the theme *is* their
  trade, drawn honestly. A reader who loves print will recognise the
  misregistration detail and the column-inch progress caption instantly.
- Newsletters and subscription publications (the "edition" model maps
  1:1 onto issues, archives, and subscribe forms — see the clip-coupon
  form, Element 16).
- Heritage and craft brands with a genuine print history — letterpress
  studios, bookbinders, roasters or distillers who print their own labels —
  where the press is a true story, not a costume.
- Long-form essay and reportage sites, where the broadsheet column and the
  pinned front page give long reads a ceremony blogs cannot.
- Annual reports and documentary microsites that want the authority of a
  front page for a single story.

**When NOT to use it.**

- Anything that must feel soft, playful, or futuristic: the pressroom is
  iron and ink. A children's product, a gaming launch, or a neon SaaS
  dashboard in this theme reads as parody.
- Data-dense operational tools (admin panels, trading terminals). The
  broadsheet grid and serif body are for *reading*, not scanning tables at
  speed; counters exist here, but they count editorial things.
- Brands with no editorial content model. If the site has no headlines, no
  editions, no dated material, the edition stamps and column rules have
  nothing true to attach to and become costume — the exact failure this
  theme exists to avoid.
- Sites whose photography is glossy colour product work. The halftone
  treatment (Element 7) will fight it. This theme wants documentary,
  black-and-white-leaning imagery.
- Any build that cannot honour the performance budgets in §6 — the
  cylinder and grain are cheap when built as specified, expensive when
  improvised.

**The one-sentence test.** If a visitor who has never seen the site can
say, within five seconds, "this page was just printed, at night, by people
who do this every night" — the theme is working. If they say "nice vintage
newspaper theme," it has failed: vintage is a museum, this is a workplace.

---

## 2. Palette

Four anchor colours, taken unchanged from the source theme. Everything
else in the table is a *derived working token* — a tint, shade, or pairing
of those anchors, created so builders never improvise a fifth hue.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--ink` | `#101014` | Primary text, masthead, headline ink, filled rules | ~55% of all colour on the page (as text) | On `--newsprint`: ≈16:1. The only colour body text may use at full strength. |
| `--newsprint` | `#F2EDE3` | Page ground, sheet surfaces | The ground itself; ~85% of pixels | Never pure white anywhere in the theme — `#FFFFFF` is banned; it reads as a screen, not a sheet. |
| `--press-red` | `#C8281C` | Editorial marks only: rules, stamps, proofing underlines, EXTRA box, ticker bullet | ≤3% of pixels, hard cap | On `--newsprint`: ≈4.8:1 — legal for large text (≥18px / 14px bold), headlines, rules and UI marks; **never** for body text or captions under 14px. |
| `--smudge` | `#5A5A60` | Secondary text: datelines, captions, bylines, metadata | ~10% | On `--newsprint`: ≈5.9:1 — passes AA for normal text; the workhorse grey. Named for the oil-smudge on a pressman's thumb. |
| `--ink-soft` | `#26262C` | Body text at reading sizes on tinted panels, table text | As needed | Derived from `--ink` toward `--smudge`; use where full `#101014` at 18px would feel shouty on the deep panel. Still ≥12:1 on `--newsprint`. |
| `--ink-faint` | `#4A4A52` | Tertiary labels, footer small print, disabled states | ≤5% | ≈8:1 on `--newsprint`. Never below this strength for anything that must be read. |
| `--smudge-light` | `#8B8B92` | Hairline-adjacent metadata: timestamps in the ticker, column furniture, placeholder text in the coupon form | ≤5% | ≈3.4:1 on `--newsprint` — decorative/metadata only, never essential text. |
| `--rule` | `#CFC8B8` | Column hairlines, card dividers, table rules | Structural | A darkened edge of the newsprint itself — paper shadow, not ink. 1px only; never thicker. |
| `--newsprint-deep` | `#E7E0D0` | "Inside pages": panel fills, brief-rail background, skeleton base, table zebra | ≤20% of pixels | One step darker than the sheet; signals "you are inside the paper now" (archives, rails, footers' upper band). |
| `--newsprint-edge` | `#DCD3BF` | Sheet edges, card borders on the flat ground, input borders | Structural | The colour of a sheet's cut edge against another sheet. |
| `--red-deep` | `#9E1B12` | Press-red in its pressed state: hover/active stamps, the thud-darkened ink, red text that must sit at 14–16px | ≤1% | ≈7.4:1 on `--newsprint` — the only red allowed for small text, and only for words like "EXTRA" labels and error lines. |
| `--red-wash` | `#F0DCD2` | The breaking box's paper wash, error field background in the coupon form | Rare, event-driven | Press-red printed at ~15% screen on newsprint. Appears only when the news (or an error) earns it. |
| `--ink-mist` | `#101014` at 6% opacity | Hero ink-mist drift, photo vignette feet | Atmospheric | Always a gradient to transparent; never a flat overlay. |

**Pairing rules.**

1. Red touches ink or paper, never other colours — there are no other
   colours. A chart, a map, or an embedded third-party widget must be
   re-inked to this palette (greyscale + one red series) or placed inside
   a "clipping" frame (see §7) that declares it foreign matter.
2. `--press-red` and `--red-deep` never appear in the same element: an
   element is either at rest (press-red) or pressed (red-deep).
3. Photographs print in ink: convert to greyscale, then lift the blacks
   4% toward `--smudge` so a photo's darkest tone is never darker than the
   headline beside it. One red element may print *over* a photo (the
   edition stamp), nothing else may.
4. Links in body text are ink with a 1px ink underline at 30% offset —
   they turn `--red-deep` on hover with the proofing underline (Element
   10). Red link text at rest is banned: red is a mark made by a human
   editor, not a default state.

**Dark-mode behaviour — "the night desk."** Dark mode is not an inversion;
it is the same pressroom with the lights off and the desk lamps on. Ground
becomes `--ink` `#101014`; sheet panels become `#17171C` (a plate, not a
sheet — slightly lifted from the ground); body text becomes `--newsprint`
at 92% opacity; hairlines become `#2E2E36`; `--newsprint-deep` panels
become `#1D1D24`. `--press-red` brightens to `#E0483C` (call it
`--press-red-night`) because `#C8281C` on `#101014` falls to ≈2.9:1 and
dies; the brightened red holds ≈4.7:1 against the ink ground — large text
and marks only, same law as the day sheet. The halftone grain inverts with
the photographs (dots become the light). The edition stamp keeps
`--press-red-night`. The cylinder's ink band reads as a lighter sheen
instead of a darker one — it is the same cylinder under a lamp. Every
motion timing in §5–§6 is identical in both modes; only these tokens swap.

---

## 3. Typography

Two families, no exceptions, no third "accent" font — a pressroom owns the
cases it owns.

- **Libre Franklin** (variable, weight 100–900) — everything the press
  *shouts or files*: headlines, kickers, masthead, counters, stamps, nav,
  buttons, table figures. Condensed feel comes from tracking and case, not
  from a separate condensed cut: display sizes run at −0.02em tracking,
  uppercase, weight 800–880.
- **Newsreader** (variable, weight 300–700, with true italics and optical
  sizing) — everything the press *says*: body copy, decks, captions,
  bylines, form labels, footer prose. Optical size axis set to `auto` so
  captions sharpen and display serif (used rarely, for pull-quotes) softens.

**The full type scale** (root 16px; sizes in rem/px, all line-heights
unitless):

| Role | Font | Size | Weight | Line-height | Tracking | Case | Used for |
|---|---|---|---|---|---|---|---|
| Display 1 | Libre Franklin | clamp(3.25rem, 8.5vw, 7rem) / 52–112px | 860 | 0.94 | −0.02em | Upper | The lead front-page headline only. One per page, ever. |
| Display 2 | Libre Franklin | clamp(2.25rem, 5vw, 3.75rem) / 36–60px | 820 | 0.98 | −0.015em | Upper | Section-front headlines, article H1 on detail pages |
| Headline 3 | Libre Franklin | 1.75rem / 28px | 760 | 1.05 | −0.01em | Sentence | Story headlines in rails and cards |
| Headline 4 | Libre Franklin | 1.25rem / 20px | 700 | 1.15 | 0 | Sentence | Card headlines, briefs, table heads |
| Kicker | Libre Franklin | 0.75rem / 12px | 700 | 1.2 | +0.18em | Upper | Section labels, dateline prefixes, nav-adjacent labels. Always followed by the red rule or a hairline. |
| Deck | Newsreader | 1.375rem / 22px | 400 (italic optional) | 1.45 | 0 | Sentence | The standfirst under a headline — the paper's one breath of quiet |
| Body | Newsreader | 1.125rem / 18px | 420 | 1.68 | 0 | Sentence | All article and page body copy. Measure 58–68ch in a column. |
| Body small | Newsreader | 1rem / 16px | 420 | 1.6 | 0 | Sentence | Secondary copy, form help text, footer prose |
| Caption | Newsreader italic | 0.8125rem / 13px | 400 | 1.45 | 0 | Sentence | Photo credits and captions, always in `--smudge`, always with the credit in small caps Franklin 10px after an em dash |
| Byline / dateline | Libre Franklin | 0.6875rem / 11px | 600 | 1.3 | +0.12em | Upper | "BY A. REPORTER — LAHORE, 2 A.M." furniture |
| Data / counter | Libre Franklin | 1rem / 16px, tabular-nums | 650 | 1.2 | +0.02em | — | Circulation counters, column-inch readouts, prices in the coupon form. `font-variant-numeric: tabular-nums` is mandatory — figures must never jitter while rolling. |
| Pull-quote | Newsreader | 1.75rem / 28px | 480 | 1.3 | 0 | Sentence | The only serif display role; set with a 3px press-red left rule. |
| Button / action | Libre Franklin | 0.8125rem / 13px | 700 | 1 | +0.14em | Upper | "SUBSCRIBE", "FILE YOUR STORY" — verbs from the trade, never "Submit". |

**Per-role rules.**

- **Display roles never wrap awkwardly:** Display 1 is set with
  `text-wrap: balance`, a maximum of 3 lines, and is copy-edited to fit —
  if a headline needs 4 lines at 360px wide, the headline is rewritten,
  not shrunk below 44px. A shrunken shout is the theme's most common
  failure (see §9).
- **Headlines are ink, full stop.** No headline may be set in red, grey,
  or a photograph. Red enters a headline's territory only as furniture
  (stamp, rule, underline) — the words themselves are always `--ink`.
- **Body copy is justified only in multi-column article flow** with
  `hyphens: auto` and a declared `lang`; everywhere else it is ragged
  right. Justified text without hyphenation in a 320px column produces
  rivers — banned outright.
- **Drop caps** belong to article body only: Newsreader at 4.6em, float
  left, line-height 0.78, padding 6px 10px 0 0, ink — never red, never
  boxed. One per article.
- **Numbers are Franklin, always.** A figure appearing inside serif body
  copy (a date, a circulation number) is set in Libre Franklin at 0.92em
  with tabular figures — the press sets its numbers in the grotesque case.
  Exception: years inside running prose may stay serif if the sentence is
  narrative ("in 1947 the press…"), at the editor's judgement, applied
  consistently per page.
- **The kicker–rule pair is a unit.** A kicker never appears without its
  hairline or red rule beneath it, and a red rule never appears without a
  kicker or headline it serves. Orphan rules are decoration; paired rules
  are furniture.
- **Weight is the volume knob.** Libre Franklin's variable weight axis is
  how this theme raises its voice (see the EXTRA pulse, Element 9):
  emphasis inside Franklin text is done by weight (420→700), never by
  switching to red, and never by italic — Franklin has no true italic in
  this theme and synthetic oblique is banned.
- **Loading:** both families load with `font-display: swap` and metric
  overrides (`size-adjust`, `ascent-override`) so the fallback stack
  (Georgia for Newsreader roles, Arial Narrow/Helvetica for Franklin
  roles) holds the same column widths; a reflow when the real face lands
  must shift no line by more than 2px. The strike animation (Element 1)
  waits for `document.fonts.ready` or 300ms, whichever comes first —
  headlines never strike in the wrong face.

---

## 4. Layout language

**The grid.** A broadsheet: 12 columns, max content width 1296px, gutters
24px, outer margins fluid (5vw, min 20px). Column hairlines (`--rule`,
1px) are *drawn* between text columns in article flow — real `border-left`
on the column boxes, not background stripes — because the conveyor's
misregistration (Element 3) must be able to move the columns and their
rules together by ±2.5px. On screens ≥1280px a fixed left margin rail of
96px exists outside the grid: it is the press bed, home of the margin
cylinder (Element 4) and the edition line rotated into it. Below 1280px
the rail collapses and the cylinder retires (see Element 4's mobile
variant); the grid keeps its 12 columns down to 768px, becomes 6 columns
at 480–767px, and a single column below 480px.

**Spacing rhythm.** An 8px base unit, but the *felt* rhythm is the
newspaper's: sections are separated by 96px (12 units) of open paper and a
double rule (3px ink line over 1px ink line, 4px apart — the classic
front-page section break), while inside a section, elements breathe at
16/24/40px. Whitespace in this theme is never empty: it is *unprinted
paper*, and it is rationed like paper — generous between stories, tight
inside furniture. A page that feels airy and minimal has failed; a front
page is dense with clear hierarchy. Target density: a desktop viewport at
any scroll position contains at least one headline, one rule, and one
piece of furniture (stamp, dateline, counter) — if a viewport shows only
body text, the layout has drifted into blog territory.

**Section choreography.** Every page follows the front-page order, top to
bottom: (1) masthead + edition line, (2) wire ticker, (3) the lead —
headline, deck, lead photo, (4) the briefs rail or secondary stories in
columns, (5) section fronts with red rules, (6) data furniture (counters,
tables set as box scores), (7) the coupon form or call to action, (8) the
colophon footer. Builders may omit stations a page genuinely lacks, but
may never reorder them: a form above the lead is a flyer, not a front
page.

**Misregistration as a layout material.** Real press sheets drift a
fraction before they settle. The theme uses exactly one expression of it:
during the conveyor entrance (Element 3), columns and their rules sit
±2.5px off in X for the first 60% of the move, then register to 0. At rest,
the registration is *perfect* — 0px, always. Permanent offsets, rotated
elements, or "wonky" resting states are banned: the run settles, that is
the story. The single resting exception is the double rule's red twin in
the breaking box (Element 9's home), offset 2px, because breaking news is
the one sheet still being handled.

**Images sit in wells.** Every photograph lives in a halftone well: a
`--newsprint-deep` bed, the photo itself (greyscale, treated per §2),
a 1px `--newsprint-edge` inner border, and a caption block beneath in the
well's own padding (12px). Wells never float over text, never break the
column grid, and never carry drop shadows — paper on paper has no shadow
at 2 a.m. under flat pressroom light. The only shadow in the theme is the
2px offset hard shadow (ink at 100%, no blur) under a *lifted* card on
hover (Element 15) — the look of a sheet picked up off the pile.

**Alignment law.** Everything aligns to a column edge or a rule. Centred
text exists in exactly two places: the masthead nameplate and the
colophon. Centred headlines, centred body, centred buttons elsewhere are
the visual accent of a template, not a newspaper — banned.

---

## 5. Full motion system

Motion in the Midnight Press Run obeys one physical metaphor: **heavy
machinery, light paper.** The press (cylinder, conveyor, stamps) moves with
weight and finality; the sheets move fast and settle soft. Nothing floats,
nothing springs like a toy, nothing loops for decoration alone — every loop
is a machine idling (grain shimmer, EXTRA pulse, ticker) and stops the
moment it leaves the screen.

**Easing tokens** (the only curves allowed in the theme):

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-strike` | `cubic-bezier(.2,.9,.25,1)` | Type hitting paper: fast attack, hard stop, tiny settle | Headline strikes, stamp-ins, masthead stamp |
| `--ease-sheet` | `cubic-bezier(.22,1,.36,1)` | A sheet gliding off the conveyor and lying flat | Conveyor feed, card entrances, image scale-in-frame |
| `--ease-proof` | `cubic-bezier(.65,0,.35,1)` | A hand drawing a stroke: slow-fast-slow | Red rule draws, proofing underlines, ink-line progress (when animated, not scrubbed) |
| `--ease-press` | `cubic-bezier(.5,0,.75,0)` down / `--ease-sheet` up | The press thud: mass comes down fast, releases gently | Press-thud click, coupon form submit |
| `--ease-wire` | `linear` | The wire never hurries | Ticker marquee only. The only linear motion in the theme. |

**Duration tokens:** `--dur-instant` 120ms (thud, hover state snaps) ·
`--dur-mark` 220ms (underlines, stamp micro-moves) · `--dur-strike` 240ms
(per headline line) · `--dur-rule` 600ms (rule draws) · `--dur-sheet`
900ms (conveyor travel) · `--dur-page` 380ms (sheet change) · `--dur-roll`
1400ms (counter rolls). Any duration a builder needs that is not within
±10% of a token must be justified in the build notes — freehand timings are
how themes rot into generic motion.

**The vocabulary, term by term** (each in this theme's own material):

- **Scroll-triggered reveals** — sections are *fed*, not faded: the
  conveyor drift (Element 3), triggered per section when its top crosses
  80% of viewport height, once only. A section that has printed never
  un-prints on scroll-up.
- **Scroll-scrubbed animation** — three scrubs only, all 1:1 with the
  reader's hand: cylinder rotation (Element 4), ink-line fill (Element 5),
  and the lead photo's scale inside the pin (Element 6). Scrubbed values
  pass through an rAF lerp (factor 0.14 per frame at 60fps) so the press
  feels geared, not glued, to the scrollbar.
- **Parallax layers** — exactly two speeds exist: the sheet (1.0×) and the
  halftone grain over photographs (0.6×, Element 7). Type never parallaxes
  against its own background — words stay registered to their sheet.
- **Pinned scenes** — one per page maximum: the front-page pin (Element
  6), 120vh of travel. A second pin on a page is a traffic jam on the
  conveyor; banned.
- **Masked line reveals** — headline lines are masked by their own line
  box (`overflow: hidden` wrappers) during the strike (Element 1): each
  line rises 12px inside its mask while its ink-bleed blur clears, so
  lines never overlap during the print.
- **Blur-to-sharp reveals** — the wet-ink settle: `filter: blur(2px) →
  blur(0)` over the same 240ms as the strike's scale settle. Blur is used
  nowhere else in the theme; it means *wet*, always.
- **Animated counters** — circulation and column-inch counters roll with
  an odometer of tabular figures (Element 5's readout; §7's data pages),
  1400ms `--dur-roll`, `--ease-sheet`, triggered at 60% viewport entry,
  once. Figures roll *up* only, and land exactly on the true value.
- **Progress indicators** — the ink-line rule (Element 5) is the only
  progress indicator. No spinners, no top bars in any other colour, no
  percentage badges — progress is measured in column inches, in ink.
- **Marquees** — the Late Wire ticker (Element 13): headlines from the
  wire, separated by red bullets, translating linearly at 60px/s,
  pausing on hover and on focus-within. It is a newsroom wire, not a
  crypto ticker: no flashing, no colour changes.
- **Ambient loops** — three, all pausable and all halted off-screen via
  IntersectionObserver: halftone shimmer (6s, Element 7), EXTRA weight
  pulse (1.6s, Element 9), ink-mist drift in the hero (14s, two
  `--ink-mist` gradients translating 24px and back, `alternate`). Total
  ambient CPU budget: under 2% of one core on a mid-range phone.
- **Micro-interactions** — proofing underline on hover (220ms), press-thud
  on click (120ms down, 260ms release), card lift (translateY −3px + hard
  shadow, 200ms). Every interactive thing on the page answers within one
  of these three; there is no fourth feedback style.
- **Hover physics** — paper physics: lifts are ≤3px, tilts are ≤0.5° and
  only on cards (Element 15), nothing is magnetic, nothing follows the
  pointer. The pointer is the reader's finger on the page; the page does
  not chase it. Cursor: the normal system cursor, everywhere, always.
- **Page transitions** — the fresh-sheet change (Element 12), 380ms,
  old sheet down / new sheet up, masthead pre-stamped.
- **Image treatments** — photos scale-in-frame 1.08→1 over 1100ms
  `--ease-sheet` inside their wells while the halftone screen fades from
  24% to its resting 12% opacity — the photograph *develops in the tray*
  as it is read. Triggered at 50% well entry, once.
- **Skeleton loading** — the wet-sheet skeleton (Element 11): unprinted
  columns with a sheen sweep, replaced by top-down inking when copy
  arrives.
- **Reduced motion** — the static printed page (detailed per element in
  §6): every element ships in its final printed state, all scrubs become
  their end values, the ticker becomes a static list of the three latest
  wire items, counters print their final figures.

**Global motion laws.** (1) Every entrance runs **once**; a reader
re-scrolling a printed page sees a printed page. (2) Every reveal carries
the theme's standard safety: a 1.2s timed fallback forces the final state
if the trigger never fires, and with JavaScript disabled every element is
in its final state by default (animations are applied *by* JS/ CSS
classes added after first paint, never required to remove a hidden state
— content is visible in the raw HTML). (3) Scroll-driven work runs only
inside one shared rAF loop for the whole page (cylinder + ink line +
parallax read the same lerp value); three separate scroll listeners are a
defect. (4) No animation may run on an element outside the viewport —
machines idle only when watched.

---

## 6. Signature elements — full build specs

The theme's twelve signature elements (1–12, kept from the source entry and
deepened), followed by the page-family elements (13–17): masthead
navigation, story cards, the clip-coupon form, and the colophon footer.
(The hero is Elements 1+2+6 assembled — its composition spec is §8's
worked example; the loader is Element 11 and the page transition is
Element 12.)

---

### Element 1 — Live-printed hero headline

- **What & why.** The lead headline is struck onto the page line by line,
  exactly as a press strikes type: each line lands with weight, spreads a
  whisper of wet ink, and sharpens. It exists because this theme's whole
  claim is *the moment of printing* — the most important words on the page
  must be seen to be printed, not merely shown. No other theme may borrow
  it: a struck headline on a non-press theme is a typewriter effect in a
  costume.
- **Structure.** The headline is an `<h1>` split server-side (or at build
  time) into per-line `<span class="strike-line">` wrappers, each with
  `overflow: hidden` and `display: block`. Inside each wrapper, an inner
  span carries the animation. Line breaks are decided by the layout, not
  the copywriter's `<br>`s — the split is recomputed on resize (debounced
  200ms) only if the headline has not yet printed; after printing, lines
  are locked and simply reflow as static text. The edition stamp
  (Element 2) sits in the headline's furniture row above it, never inside
  the animated spans.
- **Motion spec.** Trigger: page load, after the masthead stamp completes
  (Element 13), and after `document.fonts.ready` or a 300ms cap —
  whichever is first. Per line: translateY 12px→0 inside the mask,
  scale 1.06→1, `filter: blur(2px)→blur(0)`, opacity is *not* animated
  (ink does not fade in; it arrives). Duration 240ms per line
  (`--dur-strike`), `--ease-strike`, stagger 60ms between line starts, so
  a 3-line headline completes in 240 + 2×60 = 360ms. The kicker above the
  headline strikes first (single line, same spec, no blur — kickers are
  set in smaller type that bleeds less), the deck fades *nothing* — it is
  revealed by a clip-path wipe left→right over 300ms `--ease-proof`
  starting 120ms after the last headline line lands, because the deck is
  the editor's summary typed after the headline is set.
- **States.** *Rest (pre-print, ≤500ms):* the headline area holds its full
  layout space (reserved via the real text in the DOM, visibility held by
  the mask transform only — never `display:none`). *Printing:* lines land
  in sequence. *Printed (rest state forever after):* static, full ink,
  indistinguishable from ordinary type. *Hover:* the headline is a link on
  most pages — hover draws the proofing underline (Element 10) beneath the
  whole block. There is no "scrolled-past" state; printed is printed.
- **Content merge.** The animation is not applied *to* the headline; the
  headline *is* the printed object. Remove the animation and the element
  is still the page's lead headline in the page's lead position — the
  motion adds the act of printing, never the meaning.
- **Failure fallback.** If JS is off, if fonts fail, if the load event is
  delayed — the headline is simply there, fully printed, because the
  hidden-ish pre-state is applied by a JS-added class (`js-strike-armed`)
  within the first frame; no class, no pre-state. The standard 1.2s
  fallback timer also forces the printed state.
- **Reduced motion.** No strike. The headline is present at first paint in
  final form; the deck's wipe is removed too. The edition stamp still
  shows the real time (it is information, not motion).
- **Performance & mobile.** Cost: transform/filter on ≤4 line spans for
  ≤360ms — negligible; `filter` is dropped from the spans the moment the
  animation ends (`animationend` → remove class) so the headline never
  sits on a permanent filter layer. Mobile variant: identical spec —
  type strikes the same at 360px — except the blur is reduced to 1px
  (small-size type bleeds less, and mobile GPUs pay more for blur).

### Element 2 — Real-clock edition stamp

- **What & why.** A small press-red stamp in the furniture of every
  headline: "2nd Edition · 02:14". It proves the page is a living edition,
  printed *now*, for *this* visitor. It is the theme's signature detail —
  the anti-slop line in the source entry — because it must be *true*: the
  time is the visitor's real local time, the edition number is the real
  count of that day's published updates.
- **Structure.** A `<span class="edition-stamp">` in the headline's
  furniture row (with the dateline), styled as a rubber stamp: Libre
  Franklin 11px, 700, +0.14em tracking, uppercase, `--press-red`, 1.5px
  border in the same red at 85% opacity, padding 3px 7px 2px, rotated
  −1.2° (the one resting rotation allowed in the theme — a hand stamp is
  never perfectly square), `border-radius: 2px` with one corner at 3px so
  it reads stamped, not buttoned. The stamp's text is rendered
  server-side with the server's time for the edition's timezone, then
  corrected by JS to the visitor's local clock on load.
- **Motion spec.** On first reveal, the stamp *stamps*: scale 1.35→1,
  opacity 0→1 in the first 30% (a stamp arrives already inked — it does
  not fade up), rotate −2.4°→−1.2°, 180ms `--ease-strike`, triggered with
  its headline's entrance. On the hour (and on edition change), it
  re-stamps in place: lifts (scale 1→1.12, 90ms) and strikes again with
  the new time (180ms). If the tab is hidden at the hour, the re-stamp
  happens silently on return — no backlog of stamps.
- **States.** *Rest:* printed, slightly rotated, red. *Hover:* none — a
  stamp is not interactive; `cursor: default`, no hover state, and it is
  never a link. *Stale:* if the visitor's clock cannot be read (JS off),
  the server-rendered time stands and the stamp still reads true for the
  edition's timezone, with the timezone named in the dateline beside it.
- **Content merge.** It sits where a real paper prints its edition line —
  inside the headline's own furniture, sized to the furniture, part of the
  bibliographic record of the page. It is never a floating badge, never
  in a corner overlay, never on non-editorial pages (checkout success
  pages do not get edition stamps; the colophon carries the record there).
- **Failure fallback.** No JS → server time + named timezone, fully
  legible. No localStorage/timezone API → same. The stamp can never block
  or delay the headline's strike: it renders independently.
- **Reduced motion.** The stamp is present, printed, at rest rotation;
  the hourly re-stamp swaps the text with no scale/rotate motion.
- **Performance & mobile.** One timer, checked every 60s against the
  minute hand — not a per-second clock. Mobile: identical, size unchanged
  (11px is the floor; a smaller stamp is a smudge). On very narrow
  headlines (<340px) the stamp moves to its own furniture line above the
  dateline rather than shrinking.

### Element 3 — Conveyor sheet feed

- **What & why.** Every section enters the page the way a sheet leaves the
  press: travelling up on a slow conveyor, fractionally out of register,
  settling into perfect registration as it stops. It is the theme's
  universal entrance — the thing that replaces the generic fade-up this
  theme bans. The misregistration is the soul of it: a feed that arrives
  perfectly aligned is just a slide; the ±2.5px drift-and-lock is the
  machine.
- **Structure.** Sections carry `data-feed` and are observed by one
  IntersectionObserver (threshold: top crossing 80% viewport height).
  The animated properties live on the section element itself —
  `transform: translateY(26px) translateX(var(--reg))` where `--reg` is
  set per section from a deterministic pseudo-random sequence seeded by
  section index (so the drift pattern is stable across reloads: section
  1 drifts +2px, section 2 −2.5px, section 3 +1.5px… within ±2.5px).
  Inner columns and rules are children, so they inherit the drift —
  the whole sheet is out of register, not a wrapper pretending.
- **Motion spec.** Duration 900ms (`--dur-sheet`), `--ease-sheet`. The
  registration error holds near its full value for the first 55% of the
  travel, then eases to exactly 0 across the final 45% (implemented as a
  two-keyframe animation: 0% { ty:26, reg:±2.5 }, 55% { ty:8, reg:±2.2 },
  100% { ty:0, reg:0 }). Opacity is never touched. Trigger once per
  section; sections already above the fold on load feed in with a 90ms
  stagger cascade from the top, starting 100ms after the headline strike
  completes.
- **States.** *Unfed (pre-trigger):* held at the 0% keyframe by the
  JS-armed class only. *Feeding:* as above. *Settled:* transform removed
  entirely at `animationend` (not left at `translate(0,0)`) so the section
  creates no permanent containing block — this matters because the pinned
  section (Element 6) must not live inside a transformed ancestor.
  *Scrolled-past:* settled is settled; scrolling back up shows a printed
  page.
- **Content merge.** The sections are the sheets. The drift lives in the
  sections' own columns and rules; there is no overlay, no wrapper div
  with a fake paper texture. Delete the animation and the page layout is
  pixel-identical.
- **Failure fallback.** Standard: JS-armed pre-state, 1.2s force-settle
  timer per section if the observer never fires (e.g., a browser without
  IO), content fully present without JS.
- **Reduced motion.** No travel, no drift. Sections are simply present.
  The page reads as the finished paper — which is the correct reduced
  expression of this theme.
- **Performance & mobile.** Transform-only, one observer, sections
  animate ≤900ms each and release their layer at end. Budget: no more
  than 2 sections feeding simultaneously (the observer queues if the
  reader scrolls fast — a fast scroll prints a fast run, sections settle
  in order, none are skipped). Mobile variant: travel shortens to 16px
  and drift to ±1.5px (small screens make 2.5px look broken, not
  mechanical), duration 700ms.

### Element 4 — Margin press cylinder

- **What & why.** A 64px-diameter press cylinder, fixed in the left margin
  rail for the entire read, rotating in exact gear with the reader's
  scroll, its ink band darkening the edition line it runs beside. It is
  the machine made visible — the one moving part the reader can watch
  while everything else is paper. It earns its place by *doing* work: the
  darkening it produces on the edition line is the reader's progress made
  physical, paired with Element 5's ink rule at the top.
- **Structure.** An inline SVG, 64×64 viewBox, drawn in the palette only:
  an outer circle in `--ink` (the steel, inked), a 10px ink band arc in
  `--press-red` at the contact point (the forme), two bolt circles in
  `--smudge`, and a highlight arc in `--newsprint` at 20% opacity. It sits
  in a `position: fixed` rail cell vertically centred in the left margin
  (rail width 96px, cylinder centred at 48px). Beside it in the rail, the
  edition line runs vertically: "MIDNIGHT EDITION — No. 214" in 10px
  Franklin, rotated −90°, whose ink colour interpolates from `--smudge`
  to `--ink` with scroll progress (the cylinder "inks" it as it turns).
  Rotation is applied to an inner `<g>` so the highlight arc stays
  lamp-fixed while the bolts and forme turn — a real cylinder's sheen
  doesn't rotate with the drum.
- **Motion spec.** Rotation scrubbed 1:1 to total page scroll progress:
  0→1080deg (three full turns) across the full read, through the shared
  rAF lerp (factor 0.14). The edition-line ink interpolation uses the
  same progress value, 0→1. No autonomous rotation: when the reader
  stops, the press stops. A stopped press is correct; an idling cylinder
  would be a screensaver.
- **States.** *Rest (top of page):* forme arc at top-dead-centre, edition
  line at `--smudge`. *Turning:* as above. *End of page:* three turns
  complete, edition line fully inked; the cylinder does not reverse on
  scroll-up — it counter-rotates exactly with progress (it is geared, not
  one-way), so scrolling up un-inks nothing visually except the line's
  colour returning toward smudge. *Hidden:* below 1280px viewport width,
  or when the rail would overlap content, the whole rail is `display:
  none` — see mobile variant.
- **Content merge.** It lives in the margin gutter where the press runs
  alongside the sheet, and its output (the inking edition line) is real
  page furniture carrying the real edition number. It is never inside the
  text column, never overlapping a word, never a floating mascot.
- **Failure fallback.** Without JS: the cylinder renders static at
  top-dead-centre and the edition line prints in full `--ink` — the page
  loses the gearing, keeps the furniture. If the SVG fails to load
  (inline, so it cannot 404), nothing else is affected.
- **Reduced motion.** The cylinder is printed static (forme at
  top-dead-centre) and the edition line prints in full ink — the reduced
  page shows the machine at rest, fully legible.
- **Performance & mobile.** One SVG, one transform per rAF frame inside
  the shared loop; cost is a single layer repaint, <0.5ms/frame. Budget:
  the rail must never trigger horizontal scroll — it is inside the
  1296px max-width envelope. Mobile variant (<1280px): cylinder and rail
  retire completely; their job (progress made physical) is fully covered
  by Element 5's ink-line rule, which is why the rule exists at the top
  of the page and not only in the margin. No half-measures: a small
  cylinder squeezed beside 360px text would be a toy, and this theme
  has no toys.

---

### Element 5 — Ink-line progress rule

- **What & why.** The hairline rule under the masthead is a real
  structural rule of the front page — and it fills with ink, left to
  right, exactly as far as the reader has read, captioned in the paper's
  own unit: "column inches read". It replaces every conventional progress
  bar by making progress a property of the page's furniture. It is also
  the mobile carrier of the cylinder's job (Element 4), so it must be
  fully specified in its own right, not treated as a fallback widget.
- **Structure.** The masthead's bottom rule is two stacked 1px lines:
  the track (`--rule`) at full width, and the fill (`--ink`, 2px — one
  pixel proud, because wet ink swells the line) whose `transform:
  scaleX(progress)` with `transform-origin: left` is driven by the shared
  rAF lerp. At the fill's leading edge sits a 3px ink bead (a droplet:
  a 3×3px circle squashed to 2.4px tall). The caption — "37 COLUMN INCHES
  READ" — is a mono-spaced-feeling Franklin readout (tabular figures,
  10px, +0.14em, `--smudge`) docked at the right end of the rule inside
  the masthead furniture; the number is computed from real geometry:
  total article column-inches = body text height in px ÷ 96 × (columns
  factor), read inches = progress × total, rounded down (a reader has
  never read a fraction of an inch the paper hasn't given them).
- **Motion spec.** Pure scrub: scaleX follows lerped scroll progress
  (factor 0.14), no easing curve of its own — the lerp *is* the gearing.
  The caption number updates at most every 6 inches of computed travel
  (integer steps), never per-pixel — a readout that flickers 36→37→36 is
  a broken gauge. On page load with a restored scroll position (browser
  back), the fill starts at the true progress, not at 0: the paper
  remembers where it was read to.
- **States.** *0%:* track only, caption reads "0 COLUMN INCHES READ" —
  or, on pages without a long read (home), the caption names the edition
  instead ("EVENING EDITION — 24 PAGES") and the fill tracks whole-page
  progress. *Mid-read:* as above. *Complete (100%):* the bead reaches the
  right edge, the caption flips to "FULL SHEET READ — No. 214" and the
  fill holds; it does not pulse, bounce, or celebrate. *Hover:* none.
- **Content merge.** The rule is load-bearing furniture: it separates the
  masthead from the front page on every page of the site, progress or no
  progress. The fill is ink *in* the rule. Removing the JS leaves the
  rule; removing the rule would break the masthead — that is the test of
  a merged element, and this one passes it.
- **Failure fallback.** No JS → the rule prints as a plain double hairline
  (track + a static ink line at 100%? No — at 0%: an unread paper must not
  claim to be read). Caption without JS shows the edition line variant.
  Nothing is hidden in any failure mode.
- **Reduced motion.** The fill still tracks progress (it is information,
  updated in 10% steps without lerp — the value steps, it does not glide)
  and the caption updates as usual. Stepped information is the honest
  reduced form of a gauge.
- **Performance & mobile.** One scaleX on a 2px element + a text update
  ≤10×/page: effectively free. Mobile: identical and primary — this is
  the main progress instrument below 1280px. The caption shortens to
  "37 IN. READ" below 480px (units compress, numbers never shrink below
  10px).

### Element 6 — Pinned front page, scrolling late briefs

- **What & why.** The front page's lead — headline, deck, lead photo —
  pins in place while a column of late-edition briefs scrolls up beneath
  it, the way later news keeps arriving at the desk while the front page
  is already on the press. It is the theme's one pinned scene (§5), and it
  earns the pin narratively: the lead is *finished* (printed, fixed), the
  briefs are *still coming in*. A pin without that finished/arriving
  contrast is just a sticky div.
- **Structure.** A two-column stage (desktop): left 7 columns hold the
  pinned lead block (struck headline from Element 1, deck, lead photo
  well); right 4 columns (1 column gutter between) hold the briefs rail
  on `--newsprint-deep`: 4–6 briefs, each a Headline 4 + 2-line Newsreader
  summary + its own mini edition stamp (Element 2, small variant:
  borderless, time only). The pin container is 220vh tall; the lead block
  sticks at `top: 96px` (below the stuck masthead) for the middle 120vh
  of travel. Inside the pin, the lead photo performs the theme's third
  scrub: scale 1.08→1 across the pinned travel (the photo settles into
  its well as the briefs pass). The rail's briefs feed individually with
  Element 3's conveyor at reduced travel (14px) as they enter.
- **Motion spec.** Pin travel: exactly 120vh of scroll (container 220vh,
  lead stuck for the central portion). Photo scrub: progress mapped
  0→1 across the pinned range, lerped at 0.14 in the shared loop. Brief
  feeds: 700ms `--ease-sheet` each, triggered at 85% entry. Release: at
  the end of the container the lead un-sticks and scrolls away with the
  page — no snap, no fade; it simply rejoins the sheet. The hand-off is
  timed so the section that follows (first section front) begins its
  conveyor feed exactly as the lead releases — the run never stops.
- **States.** *Approaching:* lead static, briefs begin feeding. *Pinned:*
  lead fixed, photo scrubbing, briefs flowing. *Released:* everything
  static print. *Short-viewport (height <600px):* the pin is disabled by
  media query — the lead and rail stack and scroll naturally, because a
  pin on a short screen traps more than it tells.
- **Content merge.** The pinned thing is the front page itself; the
  scrolling things are its own later editions. The rail's background is
  the inside-pages paper (`--newsprint-deep`) — the briefs are visibly
  *inside* the same paper, not a sidebar widget from another product.
- **Failure fallback.** No JS / no sticky support: the stage renders as a
  normal two-column block, lead above rail on narrow screens, everything
  readable in source order (lead first — the DOM order is lead, then
  briefs, so the no-CSS reading order is the editorial order).
- **Reduced motion.** No pin. Lead and briefs stack in editorial order and
  scroll as ordinary print; the photo prints at scale 1.
- **Performance & mobile.** `position: sticky` only — no JS pinning
  library, no scroll-jacking. The photo scrub is one transform in the
  shared loop. Mobile (<900px): the stage un-pins entirely; lead prints
  first, briefs follow as a stacked "Late Briefs" section on
  `--newsprint-deep` with the same feed entrances. The story survives
  intact; only the simultaneity is a desktop pleasure.

### Element 7 — Wet-ink halftone grain

- **What & why.** Photographs in a newspaper are not continuous tone —
  they are dot screens, and when the ink is wet the screen shimmers
  faintly as it dries. This grain is that screen: a fine halftone dot
  layer that lives *inside photograph wells only*, shimmering on a slow
  loop and parallaxing slightly slower than the sheet, so a photo feels
  printed and still drying rather than pasted from a stock library. The
  discipline is the point: the moment grain covers a whole page it becomes
  a texture filter from a template pack (§9).
- **Structure.** Each photo well carries a `::after` layer: a repeating
  radial-gradient dot pattern (dot diameter 3px, cell 6px, dots in
  `--ink` at variable opacity), `mix-blend-mode: multiply` on light
  sheets, clipped to the photo's box (`overflow: hidden` on the well),
  `pointer-events: none`. Resting opacity 12%. The shimmer is an opacity
  oscillation 12%→17%→12% plus a background-position drift of 1 cell over
  the loop — the screen seems to breathe as it dries. In dark mode the
  layer switches to `screen` blend with `--newsprint` dots (the dots
  become the light, per §2).
- **Motion spec.** Loop: 6s, `ease-in-out` symmetric, infinite — but only
  while the well is within the viewport (IntersectionObserver toggles a
  `data-drying` attribute; off-screen wells are frozen at resting
  opacity). Parallax: the layer translates at 0.6× the well's scroll
  speed via the shared lerp loop, travel capped at ±10px so dots never
  detach visibly from the image's own features. On the photo's first
  entrance, grain starts at 24% opacity and dries down to the 12% rest
  over the same 1100ms as the scale-in-frame (§5) — a photograph visibly
  finishing.
- **States.** *Wet (entering):* 24% → drying. *Dry (rest):* 12% + 6s
  shimmer. *Scrolled-past:* rest state continues (it is ambient, tied to
  visibility not position). *Print (literal — `@media print`):* the layer
  is removed; a printed photo of a halftone is a moiré, and the theme
  respects real paper too.
- **Content merge.** The grain is the photograph's own printing screen —
  it exists only where ink met photo paper, never over text, never over
  the page ground, never in the masthead. It is inseparable from the
  photos it serves: delete the photos and the grain is gone.
- **Failure fallback.** If blend modes are unsupported, the layer renders
  as a plain low-opacity dot overlay (still clipped, still fine). If the
  image itself fails to load, the well shows the caption and credit on
  `--newsprint-deep` with the grain at rest — an empty but honest frame,
  never a broken-image icon in a void.
- **Reduced motion.** Grain present at flat 12%, no shimmer, no parallax,
  no dry-down (photos arrive dry). The screen is a property of print, not
  a motion effect, so it stays — stilled.
- **Performance & mobile.** Gradient layers are GPU-cheap but repaint on
  opacity change: the shimmer is confined to wells ≤ the photo size, and
  no more than 3 wells may shimmer simultaneously (the observer grants
  `data-drying` to the 3 nearest the viewport centre; others rest). On
  mobile and on `save-data`, the shimmer and parallax are disabled
  entirely (static 12% screen) — the print look survives, the idle cost
  doesn't ship.

### Element 8 — Self-drawing red section rules

- **What & why.** Every section front is introduced by its kicker and a
  pressroom-red rule — and the rule is *drawn*, left to right, like an
  editor's proofing stroke across the top of the section. It is the
  theme's section-transition grammar: before you read a new part of the
  paper, you watch the editor mark it. Red is rationed (§2), so this draw
  is one of the few red events on the page — which is exactly why it can
  carry the weight of a transition.
- **Structure.** An inline SVG per section head, width 100%, height 3px,
  containing a single path (a straight line with a 0.5px hand wobble —
  the path is `M0,1.5 L…,1.4 L…,1.6` with two micro-deviations, so the
  stroke feels ruled by a hand on a straightedge, not lasered). The line
  is `--press-red`, stroke-width 2.5, round cap at the *end* only (the
  stroke starts blunt where the pen landed, ends round where it lifted —
  implemented with two overlaid paths if needed, or a cap gradient; the
  simpler shipping version uses round/round and accepts the compromise,
  noted here so a builder doesn't gold-plate it). Draw via
  `stroke-dasharray/dashoffset`. The kicker text sits above the rule,
  the section headline below it — the rule is between them, doing its
  job.
- **Motion spec.** Trigger: the section head crosses 82% viewport height,
  once. Duration 600ms (`--dur-rule`), `--ease-proof` — the hand-drawn
  curve: unhurried start, confident middle, careful lift. The kicker
  strikes in (Element 1's spec at kicker scale, 180ms) 100ms *before*
  the rule starts: the editor names the section, then underlines it.
  The section's own conveyor feed (Element 3) starts 150ms after the
  rule completes — mark first, then the sheet.
- **States.** *Undrawn:* dashoffset full (JS-armed only). *Drawing:* as
  above. *Drawn (rest):* a static red rule; the SVG is replaced in place
  by its final state (dasharray removed) so no dash pattern can ever
  re-render oddly on zoom. *Hover:* none — it is furniture. On the
  section's *own* page (a section-front landing page), the rule under the
  masthead-equivalent header is pre-drawn: you are already inside the
  marked section.
- **Content merge.** The rule belongs to the section head it introduces —
  it is the third line of a three-line unit (kicker, rule, headline) and
  is meaningless anywhere else. It never appears mid-section, never
  decorates a card, never underlines a button.
- **Failure fallback.** No JS → the rule is a plain 2.5px red rule,
  present in full (the SVG ships undrawn only when JS arms it). Print:
  prints as the rule it is.
- **Reduced motion.** The rule is simply there, full width, from first
  paint of the section. The kicker does not strike.
- **Performance & mobile.** One tiny SVG per section head; dashoffset
  animation is compositor-cheap. Mobile: identical — the draw reads
  beautifully at 360px because it is a line, not a scene. Stroke width
  stays 2.5px at all sizes (a thinner red line at mobile sizes reads as
  an error underline, not a proofing stroke).

---

### Element 9 — "EXTRA" weight-pulse

- **What & why.** In the breaking-news box — the paper's EXTRA — the word
  EXTRA itself pulses along Libre Franklin's variable weight axis,
  400→900→400, like a newsboy's shout swelling and falling. Typography is
  the voice here: no icon, no bell, no flashing background could say
  "this just came in" in the paper's own language the way the word
  getting *louder* does. It is the theme's only typographic ambient loop,
  and it lives only where a real paper shouts.
- **Structure.** The breaking box: a `--red-wash` paper panel with the
  theme's one misregistered double rule (ink rule + red rule offset 2px,
  §4), containing the kicker "BREAKING — LATE WIRE", the word EXTRA set in
  Libre Franklin at 44px with `font-variation-settings: 'wght'`
  animated, the breaking headline (Headline 3, ink), a 2-line Newsreader
  summary, and the item's real edition stamp. The box exists in the DOM
  only when there is genuinely breaking material; an empty EXTRA box is
  never rendered as a placeholder (§9).
- **Motion spec.** Weight pulse: 400→900 over 800ms, 900→400 over 800ms,
  `ease-in-out`, 1.6s loop, infinite — but only while the box is on
  screen (IntersectionObserver-gated like the grain). The pulse animates
  the variable font axis, so the letters *thicken* in place; width grows
  ~6% at peak weight — the box reserves the 900-weight width (measured at
  build or via `font-variation-settings` on a hidden twin) so surrounding
  text never reflows by a single pixel. On the box's first entrance it
  also gets the conveyor feed at half travel (12px) — breaking news
  arrives fast but it still arrives *on paper*.
- **States.** *Rest (off-screen):* weight frozen at 400. *On screen:*
  pulsing. *Hover:* the pulse pauses at whatever weight it holds and the
  proofing underline draws under the headline (Element 10) — the reader
  has grabbed the sheet; the shouting stops while they read. *Clicked:*
  press-thud (Element 10). *Stale:* if the breaking item is older than
  the edition's freshness window (default 90 minutes, set per site), the
  box demotes itself on next render: EXTRA stops pulsing, the box moves
  into the briefs rail as an ordinary brief. Yesterday's EXTRA shouting
  forever is a lie the theme will not tell.
- **Content merge.** The pulse is a property of the word, and the word is
  the content's own name for itself. The box is a story — headline,
  summary, stamp — not a banner ad unit wearing red.
- **Failure fallback.** If variable fonts fail or are subsetted away, the
  word renders at static 800 weight (a permanently bold shout — less
  alive, still honest). No JS → static 800, box fully readable.
- **Reduced motion.** Weight fixed at 800. The box reads as a bold,
  still, red-washed panel — urgency carried by colour and weight, not
  movement.
- **Performance & mobile.** One `font-variation-settings` animation on
  five letters: trivial raster cost, but it does repaint text — the box
  is capped at one per page, and the pulse is disabled on `save-data`
  and on devices reporting ≤2GB RAM via `deviceMemory` where available.
  Mobile: EXTRA at 34px, pulse identical; the box stacks full-width
  above the briefs rail, never as an overlay or a sticky banner — paper
  does not float over paper.

### Element 10 — Proofing-underline hover + press-thud click

- **What & why.** The theme's entire interaction-feedback vocabulary, in
  the editor's two gestures: the proofreader's red underline ("I have
  marked this — it matters") for hover, and the press coming down
  ("printed — done") for click. Two gestures, everywhere, no exceptions:
  a visitor learns the paper's touch language in the first ten seconds
  and never has to relearn it on another page of the site.
- **Structure.** The underline is a `::after` on interactive headlines and
  links: 2px `--press-red` (hover) — but note the pressed/visited
  distinction: on *text links inside body copy*, hover uses `--red-deep`
  at 1.5px, because body-size red must meet the small-text contrast rule
  (§2). The thud applies to cards, buttons, and the coupon submit: a
  `transform: scale(.98)` plus an ink-darkening — the element's ink
  colour steps one token darker (`--ink` text to pure `#000`? No: the
  theme's ink darkens by overlaying `--ink` at 8% over the element's
  ground, implemented as a `::before` wash) — so the whole card looks
  *pressed into* the sheet for a moment.
- **Motion spec.** Underline: `scaleX 0→1`, `transform-origin: left`,
  220ms (`--dur-mark`), `--ease-proof` — a drawn stroke, not a wipe. On
  un-hover it retracts toward the right over 160ms (the pen lifts and
  leaves the way it came — origin flips to right). Thud: down-stroke
  120ms (`--dur-instant`) `--ease-press` (fast, heavy), hold at the
  bottom while pressed, release 260ms `--ease-sheet`. Keyboard focus gets
  the underline *pre-drawn* plus a 2px ink outline offset by 3px — focus
  must be more visible than hover, never less, and never red-alone
  (colour-blind readers get the outline).
- **States.** *Rest:* no underline, natural ink. *Hover:* underline
  drawn, cursor remains the system pointer (links) or default (cards
  that are not links get the underline on their headline only). *Active
  (pressed):* thud bottom state. *Visited links:* the underline colour
  becomes `--smudge` — a proof mark in pencil: this one has been read.
  *Disabled actions:* no underline, no thud, ink at `--ink-faint`, and
  the element is genuinely inert (`disabled` / `aria-disabled` + no
  handler) — a greyed button that still clicks is a misprint.
- **Content merge.** Both gestures act on the ink of the content itself —
  the underline is under the reader's actual headline, the darkening is
  the card's own ink under pressure. There are no ripple overlays, no
  glow rings, no floating tooltips in this theme's feedback language.
- **Failure fallback.** These are enhancements of state, not carriers of
  it: without CSS animations the underline simply appears/disappears with
  `:hover` (transitions dropped, states intact), and links remain
  underlined in body copy per §2's pairing rules, so nothing becomes
  undiscoverable.
- **Reduced motion.** Underline appears instantly (no draw), thud becomes
  a 0ms ink-darken only (the colour step, no scale) — the information
  (this is pressed) survives; the movement doesn't.
- **Performance & mobile.** Transform/opacity-class changes only; zero
  layout. Mobile: no hover exists, so the thud carries all feedback —
  every tappable card and button must thud (a tap with no press feedback
  on a press-themed page feels broken). Touch targets ≥44px even where
  the visible furniture is smaller — the stamp is never a target, so its
  11px size is safe.

### Element 11 — Wet-sheet loading skeleton

- **What & why.** While content loads, the reader sees the unprinted
  sheet: the same columns, the same rules, the same furniture positions —
  with no ink in them yet, and a slow wet sheen passing over the paper as
  if it has just been dampened for the run. A skeleton in this theme is
  not a grey-box wireframe; it is *this page, before printing*. When the
  real copy arrives, the sheet inks in from the top — the run starting.
- **Structure.** Skeleton blocks mirror the real layout 1:1: masthead
  block, headline bars (Franklin-width bars at the real headline's line
  count and widths — generated from the incoming content's metadata where
  known, else from the section's standard pattern), column bars in
  `--newsprint-deep` with `--rule` hairlines between, photo wells as
  empty halftone beds (Element 7's screen at 8%, static). The sheen is a
  single diagonal gradient (`--ink-mist` at 5% → transparent) sweeping
  across the skeleton region. No spinners anywhere in the theme — a
  pressroom has no spinners; it has sheets waiting.
- **Motion spec.** Sheen sweep: 2.2s, `--ease-proof`, infinite, one sweep
  per region (not per block — the sheet is dampened once, as a sheet).
  Ink-in on content arrival: blocks print top-down, each block's real
  content replacing its skeleton with the conveyor feed at quarter travel
  (7px, 400ms `--ease-sheet`) and a stagger of 70ms per block in reading
  order — the run visibly starts at the top of the page. Skeleton
  minimum display: 300ms (a skeleton that flashes for one frame is worse
  than none); maximum honest display: if content takes >4s, the sheen
  stops (a stopped press, not an eternal one) and the furniture prints a
  "LATE WIRE — HOLDING FOR COPY" line in the dateline slot, in smudge.
- **States.** *Waiting:* skeleton + sheen. *Arriving:* top-down ink-in.
  *Loaded:* skeleton removed from the DOM (not hidden — removed, so
  screen readers never meet it; skeletons carry `aria-hidden="true"` and
  the region carries `aria-busy` until inked). *Failed load:* the sheet
  prints the failure as a correction notice (see Element 16's error
  language): a bordered "CORRECTION" box in the content's place — the
  paper admits the story didn't arrive.
- **Content merge.** The skeleton *is* the page's layout with the ink
  withheld; it teaches the reader the page's structure before a word
  loads. It never appears for content that is already on the server
  render — SSR pages print immediately; skeletons are for genuinely
  client-fetched regions only (rails, archives, comments-as-letters).
- **Failure fallback.** If the fetch fails permanently, the correction
  box (above) is the fallback — content-shaped, honest, in-theme. If JS
  is off, client-fetched regions show a printed line: "This rail is set
  in type at the office — enable scripts or read it in the archive"
  with a real link to the archive page. Nothing is ever a blank hole.
- **Reduced motion.** Skeleton present without the sheen (still paper,
  dry), ink-in is instant per block with no stagger travel.
- **Performance & mobile.** The skeleton must weigh less than the content
  it precedes: pure CSS, no images, the sheen is one gradient layer per
  region. Builders must cap concurrent skeleton regions at 2 per viewport
  (a page of five shimmering regions is a disco, not a pressroom).
  Mobile: identical, column bars collapse with the grid.

### Element 12 — Fresh-sheet page transition

- **What & why.** Moving between pages is the press cycle: the finished
  sheet is whisked off the pile and a fresh sheet comes up off the press
  with its masthead already stamped. It is the only moment the theme
  allows itself a full-screen gesture, and it works because it is rare
  (once per navigation), fast (380ms), and *directional* — sheets move
  down and up, never sideways, never fading through each other like
  slides in a deck.
- **Structure.** A transition layer replicating the sheet: the outgoing
  page's scroll container translates down while the incoming page —
  pre-rendered where the platform supports it (View Transitions API or
  SPA router with prefetch) — slides up from below the fold line, its
  masthead block already in final printed state (the new sheet's
  masthead is *always* pre-stamped; a masthead striking twice per
  navigation would be a drum solo). A 3px ink rule — the press bed's
  edge — separates the two sheets during the 380ms they share the screen.
  Focus management: on completion, focus moves to the new page's
  headline (or `main` landmark) and the route change is announced to
  assistive tech; the browser's own history/scroll semantics are never
  hijacked beyond the visual layer.
- **Motion spec.** Total 380ms (`--dur-page`). Outgoing: translateY
  0→+100% over 380ms `--ease-press` (the whisk is fast and final).
  Incoming: translateY +100%→0 over 380ms `--ease-sheet`, starting 40ms
  after the outgoing (a 40ms overlap where the ink rule edge is visible
  between them — the gap between sheets on the pile). The incoming
  sheet's hero then strikes its headline (Element 1) beginning 120ms
  after the sheet lands. Back/forward navigation reverses the geometry:
  the returning sheet comes *down* from the pile (translateY −100%→0)
  and the current one drops — the pile is LIFO, like paper.
- **States.** *Idle:* no layer. *Transitioning:* input is not blocked
  (a reader who clicks during the 380ms is navigating again, and the
  transition yields instantly to the new target — a press that can't
  change editions mid-cycle is broken machinery). *Interrupted (rapid
  nav):* sheets snap to the latest target with no queue.
- **Content merge.** The sheets are the pages themselves — the transition
  moves the reader's actual documents, not a branded overlay. There is
  no logo splash, no loading veil with a monogram; the masthead on the
  incoming sheet is the branding, doing its ordinary job.
- **Failure fallback.** If the platform cannot pre-render (plain MPA
  navigation), the transition is simply not armed: the browser's normal
  navigation happens, and each page still opens with its masthead stamp
  and headline strike. The theme must never hold a page hostage to an
  animation framework — a slow transition layer on a fast connection is
  the one unforgivable pressroom sin.
- **Reduced motion.** No sheet movement: a 120ms crossfade at the
  document level (the single permitted fade in the theme, because the
  alternative — a hard cut between full pages — is what browsers do
  anyway; the fade exists only to soften the cut for motion-sensitive
  readers who enabled the *reduced* setting but still navigate).
  Actually — under `prefers-reduced-motion`, prefer the plain instant
  navigation with no fade at all if the platform allows; the fade is the
  fallback for platforms that force a transition hook.
- **Performance & mobile.** The transition layer must never delay LCP:
  it arms only after the incoming route's critical content is ready or
  prefetched; on slow connections (Save-Data, effectiveType ≤3g) it
  disables itself and navigation is native. Mobile: identical geometry
  (sheets are vertical things; the metaphor survives the small screen
  intact), duration 340ms.

---

### Element 13 — Masthead navigation & the Late Wire ticker

- **What & why.** The navigation of a newspaper is its masthead: the
  paper's name set huge, the edition line, and beneath it the section
  names — the original information architecture, a century older than the
  hamburger menu. This element is the site's header, nav, and breaking
  wire in one printed unit, and it must behave like the top of a front
  page: present on every page, identical in structure, never redesigned
  per section.
- **Structure.** Three bands. **Band 1 — the nameplate:** left, the
  edition furniture (date in Franklin 11px uppercase, "No. 214 — MIDNIGHT
  EDITION"); centre, the nameplate itself (Libre Franklin 880, uppercase,
  clamp(2rem, 6vw, 4.25rem), −0.01em) — the publication's real name;
  right, the weather-and-price slot of a real masthead, repurposed
  honestly: the site's one key live fact (circulation counter, Element 5
  family, or the local time) — never an ad. **Band 2 — the section rule:**
  a 3px ink rule over a 1px ink rule, with the nav between them: section
  links in Franklin 13px 700 uppercase +0.12em, separated by centred
  dots; the current section carries the red proofing underline
  pre-drawn (Element 10's mark, made permanent for "you are here").
  A search action sits at the right end, labelled "ARCHIVE" — in this
  theme you search the archive, not "the site". **Band 3 — the Late
  Wire:** a 28px ticker band on `--newsprint-deep`, prefix block
  "LATE WIRE" in `--press-red` Franklin 11px, then the wire items
  (Headline 4 size, ink, separated by red bullets) translating linearly.
  The ink-line progress rule (Element 5) is the bottom border of Band 2.
  The whole masthead sticks on scroll in compressed form: Bands 1 and 3
  collapse (nameplate shrinks to 1.25rem left-aligned, ticker hides),
  leaving a 52px bar — nameplate, section links, ink rule — because a
  reader deep in a story still needs the paper's name and its progress
  line, not its full ceremony.
- **Motion spec.** *First load:* the nameplate stamps — scale 1.04→1,
  blur 1.5px→0, 220ms `--ease-strike` — before the hero headline strikes
  (Element 1 waits for it). *Ticker:* linear translation at 60px/s
  (`--ease-wire`), items duplicated for a seamless loop whose period is
  the full wire length; pause on hover, on focus-within, and whenever
  the tab is hidden. A new wire item entering the feed is prepended with
  a stamp-in (Element 2's spec) at the prefix block, once — the wire
  does not reshuffle silently under a reading eye. *Compress on scroll:*
  the masthead compresses when the reader passes 140px of scroll, over
  260ms `--ease-sheet`, and expands again only at the very top (with
  40px of hysteresis so it never flutters at the boundary).
- **States.** *Full (top of page):* three bands. *Compressed (reading):*
  52px bar. *Current section:* permanent red underline. *Hover (links):*
  proofing underline draws (Element 10). *Mobile menu open:* see mobile
  variant — the sections print as a full front-page index, not a drawer.
- **Content merge.** The nav is not chrome around the paper; it is the
  paper's own head. The ticker carries real headlines that link to real
  stories; the circulation figure is the publication's real number or is
  omitted — a masthead that lies about its circulation is the oldest sin
  in the trade (§9).
- **Failure fallback.** No JS: full three-band masthead, ticker rendered
  as a static row of the three latest wire headlines (wrapping, fully
  readable), no compression on scroll (the full masthead simply scrolls
  away and a plain anchor "BACK TO THE FRONT PAGE" appears in the
  colophon). All links are ordinary anchors throughout.
- **Reduced motion.** Ticker is a static list (latest three, with a
  "FULL WIRE" link); nameplate prints without the stamp; compression is
  instant (the bar swaps at the threshold with no glide).
- **Performance & mobile.** The ticker's translation is one transform on
  one track; item count is capped at 8 (older wire items retire to the
  archive page). Compression uses the shared rAF loop's progress value,
  no separate scroll listener. Mobile (<768px): the nameplate centres
  (its one allowed centred moment, §4), section links collapse behind a
  "SECTIONS" toggle that opens a full-width printed index — the sections
  listed as a table of contents with page-number-style leaders (dot
  leaders to the section's story count) on `--newsprint`; the ticker
  remains, at 44px/s, because the wire matters more than the furniture.

### Element 14 — Box-score data table

- **What & why.** Newspapers invented the data table that respects
  readers: the box score — dense, ruled, tabular, everything comparable
  at a glance. Any data this theme presents (results, prices, standings,
  specifications) is set as a box score, never as a dashboard card grid.
  It exists because editorial sites constantly leak data into generic
  SaaS tables; the box score keeps data *in the paper*.
- **Structure.** A table with: a kicker head row naming the table ("BOX
  SCORE — CIRCULATION BY EDITION"), column heads in Franklin 11px 700
  uppercase on a `--newsprint-deep` band, hairline `--rule` row
  separators, a 2px ink rule under the head and above the totals row,
  figures in Franklin tabular-nums right-aligned, row labels in
  Newsreader 15px left-aligned. Zebra striping is `--newsprint-deep` at
  50% on alternate rows — a whisper, never a colour. The totals row is
  ink-bold with a red rule above it if — and only if — the total is the
  story.
- **Motion spec.** Rows feed with Element 3's conveyor at quarter travel
  (7px, 500ms) staggered 40ms per row when the table enters at 75%
  viewport height — a box score is *filed*, row by row. Counters inside
  totals roll per §5 (1400ms, once). Sorting (where offered) re-files
  the rows: they do not FLIP-animate across each other like app lists;
  the table re-prints — rows fade nothing, they re-feed at eighth travel
  (4px, 300ms) in the new order, because paper re-sorts by re-printing.
- **States.** *Rest:* printed table. *Hover (sortable head):* proofing
  underline under the column name + a ▲/▼ set in Franklin (never a
  chevron icon font). *Sorted column:* head carries a 2px ink underline.
  *Empty table:* the box prints "NO RETURNS FILED" in the body area in
  smudge — an honest empty, in the paper's voice.
- **Content merge.** The table is the content. Its rules are the page's
  rules; its figures are the page's figures (Franklin tabular, §3). It
  borrows nothing from a chart library's default styling — charts, where
  unavoidable, are re-inked per §2's pairing rules and framed as
  clippings (§7).
- **Failure fallback.** It is a real `<table>` with real `<th scope>` —
  no JS is required for it to exist, sort is an enhancement layered on
  working markup, and screen readers get the table semantics a newspaper
  reader gets from the rules.
- **Reduced motion.** Rows are present; counters print final values;
  sorting swaps instantly.
- **Performance & mobile.** Tables cap at 12 visible rows before the
  "FULL TABLE IN THE ARCHIVE" cut (a front page prints the leaders, the
  archive holds the rest). Mobile: the box score scrolls horizontally
  inside its well with the first column sticky — never reflows into
  stacked "cards", which would destroy the comparability that is the
  entire point of a box score. A fade mask at the scroll edge is
  `--newsprint`, 24px.

### Element 15 — Story cards (the brief block)

- **What & why.** In listings and rails, stories appear as brief blocks:
  a clipped rectangle of the paper itself — kicker, headline, two lines
  of deck, stamp and dateline — that lifts off the pile when touched.
  Cards in this theme are not rounded rectangles with shadows and stock
  thumbnails; they are *cuttings*, and every rule about them follows
  from that.
- **Structure.** A card is a flat `--newsprint` block (on rails, the
  rail's `--newsprint-deep` shows between cards as the gaps in the pile)
  with: a top hairline, the kicker (section + red mini-rule 24px), the
  headline (Headline 4 or 3 by size class), up to 2 lines of Newsreader
  deck (line-clamped, no ellipsis fade — a cutting is cut, the clamp is
  a hard edge), and a furniture footer: edition stamp (small variant)
  left, read-time in column inches ("4 IN.") right — read time is
  expressed in the paper's unit, never "min read", which is a blog
  metric. Photo cards place the photo well (§4) on top, full-bleed to
  the card's edges. Border-radius: 0. Corners are cut square; a rounded
  cutting is a sticker.
- **Motion spec.** *Entrance:* conveyor feed (Element 3) at the card
  grid's stagger: cards in a row feed left→right with 70ms offsets, as
  if laid down by a hand across the pile. *Hover (pointer-fine only):*
  the card lifts — translateY −3px, 200ms `--ease-sheet` — and gains the
  theme's only shadow: a hard 3px offset shadow in `--ink` at 100%, 0
  blur (the sheet's edge against the pile), while its headline draws the
  proofing underline. *Click:* press-thud (Element 10) on the whole
  card. The card is one link (the headline carries the anchor, stretched
  over the card) — the whole cutting is the story's door.
- **States.** *Rest:* flat on the pile. *Hover:* lifted, underlined.
  *Focus-visible:* the lift plus the 2px ink outline (§10's focus spec).
  *Read (visited):* the stamp turns `--smudge` and the headline's ink
  softens to `--ink-soft` — a cutting you have already read looks read;
  the paper keeps your place without a "mark as read" button.
  *Sponsored/foreign matter:* a card that is not editorial is ruled with
  a dashed `--smudge` border and headed "ADVERTISEMENT — NOT FROM THE
  NEWSROOM" in Franklin 10px. The paper never disguises an ad as a
  story; the cutting frame declares it.
- **Content merge.** The card is a piece of the paper — its typography,
  furniture, and units are the article's own, miniaturised, not a UI kit
  component. The lift works because the pile is real: cards sit in a
  visible grid of paper, and lifting one shows the pile beneath
  (`--newsprint-deep` gap), not a shadow over a void.
- **Failure fallback.** Cards are complete without any motion: flat,
  linked, readable. Without CSS grid they stack as a column of briefs —
  which is still a newspaper rail.
- **Reduced motion.** No lift, no feed; hover shows the underline only
  (instantly), visited styling unchanged (it is state, not motion).
- **Performance & mobile.** The hard shadow is a `box-shadow` with no
  blur — the cheapest shadow that exists. Entrance staggering caps at
  8 cards per batch (later rows feed as they near the viewport, per
  Element 3's queue). Mobile: no hover lift (no hover), the thud remains
  on tap; cards go full-width single column, photo wells at 16:9 — a
  cutting the width of the sheet.

### Element 16 — The clip-coupon form

- **What & why.** A newspaper's subscribe form was a coupon you clipped
  with scissors along a dashed line and posted to the office. This
  theme's forms — subscribe, contact, tip submission — are printed
  coupons: dashed cut-line border, a scissors mark, fields ruled like a
  form printed in the paper, and a submit button that reads like an
  instruction from the coupon itself ("POST THIS COUPON"). It converts
  the web's most generic component into the theme's most ownable one,
  and its familiarity does real work: a coupon is understood instantly
  by anyone who has ever seen a newspaper.
- **Structure.** The form block: a 1.5px dashed border in `--smudge`
  (the cut line), a small scissors glyph (an inline SVG, drawn in
  `--smudge`, 14px) sitting on the top border at the left, headlined by
  a Franklin kicker ("SUBSCRIBE BY COUPON — OR DON'T CLIP, JUST TYPE").
  Fields are bottom-ruled only (a 1px `--newsprint-edge` rule that inks
  to 2px `--ink` on focus — you write on the line, as on paper), labels
  in Franklin 11px uppercase above the line, input text in Newsreader
  17px (handwriting's stand-in is the serif, never a script font — a
  fake-handwriting font anywhere in this theme is an instant fail, §9).
  Required marks are a red asterisk set like a proof mark. The submit is
  a solid ink block, Franklin uppercase, full width of the coupon:
  "PRINT MY SUBSCRIPTION" / per-form verb. Errors print as a correction
  box (the paper's corrections column): `--red-wash` ground, `--red-deep`
  Franklin text, above the field, naming the fix in plain words.
- **Motion spec.** *Entrance:* the coupon feeds with Element 3 like any
  section; the scissors do not snip (a moving scissors is a cartoon —
  banned). *Focus:* the field's rule inks over 180ms `--ease-proof`,
  and the label steps from `--smudge` to `--ink` (a weight step
  600→700 too) — the line you are writing on darkens, as a pen presses.
  *Submit:* the button press-thuds (Element 10), then the coupon
  performs the theme's form gesture: it is *torn off* — the coupon block
  translates down 6px and its dashed border is replaced by a torn edge
  (an SVG mask of irregular 2px teeth) while the rest of the page's form
  area prints the receipt: "RECEIVED AT THE OFFICE — 02:14, No. 214"
  with the real time and a reference number. Duration: tear 300ms
  `--ease-press`, receipt strikes in like a stamp (Element 2's spec).
  *Error:* the correction box feeds in at quarter travel; the offending
  field's rule turns `--red-deep` and holds.
- **States.** *Rest:* un-clipped coupon. *Focus:* inked rule.
  *Filled:* the field's text sits on the line; a small red proof tick
  (✓ set in Franklin, not an icon font) appears at the line's right end
  when the field validates on blur. *Submitting:* button thuds and
  holds, label changes to "AT THE PRESS…" — never a spinner.
  *Success:* torn coupon + printed receipt (above). *Error:* correction
  box + red rule; focus is moved to the first error and the box is
  announced (`role="alert"`).
- **Content merge.** The form is a printed artefact of the paper, sized
  to a column (max 560px — coupons are one column wide), placed where
  the front-page choreography puts forms (§4: station 7, after the
  content, never above the lead). Its language is the paper's: the
  receipt is an office stamp, the errors are corrections.
- **Failure fallback.** It is a real `<form>` with real labels, real
  `name`/`autocomplete` attributes, and a server action: with JS off it
  submits natively and the server returns a receipt *page* styled as the
  same office stamp. Client validation never replaces server
  validation; the proof ticks are decoration on a working form.
- **Reduced motion.** No tear: the coupon's border simply becomes the
  torn-edge mask statically at success (the state change is information;
  the movement is not), receipt appears without the stamp motion.
- **Performance & mobile.** The torn edge is one reusable SVG mask; the
  tear is one transform. Mobile: the coupon goes full-column, fields
  stack (they already do — a coupon has one column), input font stays
  ≥16px so iOS never auto-zooms the page — a zooming form is a sheet
  slipping on the press, and it is banned by this line if not by §10.

### Element 17 — Colophon footer

- **What & why.** A newspaper ends with its colophon: who printed this,
  where, under what authority, and the small print that makes it a real
  publication. This footer is that colophon, expanded to carry the
  site's closing furniture — sections index, archive, corrections,
  contact the desk — all set as the back page of the paper, never as a
  dark "footer widget area" from a template.
- **Structure.** On `--newsprint-deep` (the inside-pages paper), topped
  by the double rule (3px over 1px, §4). Four columns on desktop: (1)
  the nameplate repeated small + the imprint paragraph in Newsreader
  13px ("Printed nightly by … at … . Edition No. 214 — set in Libre
  Franklin and Newsreader.") with the *real* publisher details; (2)
  "SECTIONS" — the nav repeated as an index with dot leaders and story
  counts, mirroring Element 13's mobile index; (3) "THE DESK" — contact
  routes written as desk instructions ("Send a tip to the desk", "Write
  a letter to the editor") linking to the coupon-form pages; (4) "THE
  RECORD" — corrections policy, archive, RSS (labelled "WIRE FEED"),
  privacy and terms as "house rules". Below the columns, the closing
  line, centred (its one allowed place, §4): "— END OF EDITION No. 214 —
  STOP PRESS —" with the edition's real closing time, and the final
  hairline. The back-to-top action, where present, is a text link in
  column 4: "RETURN TO THE FRONT PAGE".
- **Motion spec.** The colophon does almost nothing, on purpose — the
  paper is finished. Its single motion: as it enters, the closing line's
  "STOP PRESS" stamps in once (Element 2's spec) — the last thing the
  press does. Links take the proofing underline. Nothing else moves;
  a footer that performs is a footer apologising for the page above it.
- **States.** *Rest:* printed. *Edition change:* the edition number and
  closing time update with the site's real edition cycle; the colophon
  of an archived edition is frozen at that edition's values — archive
  pages must show the colophon of their own night, not tonight's.
- **Content merge.** Every line is the publication's real record: real
  publisher, real counts, real policies. Placeholder imprint text
  ("Lorem ipsum printing co.") in a shipped colophon is a firing
  offence under §9 — the colophon is where the theme's honesty is
  audited.
- **Failure fallback.** Static by construction; no JS involved except
  the stamp flourish, whose absence changes nothing.
- **Reduced motion.** The STOP PRESS line prints without stamping.
- **Performance & mobile.** Zero-cost element. Mobile: columns stack in
  the order imprint → sections → desk → record (the paper's priorities,
  not the designer's), dot leaders survive at all widths.

---

## 7. Page application map

The theme is a newspaper, so its page types are the paper's own sections.
The choreography of §4 (masthead → wire → lead → briefs → section fronts →
data → coupon → colophon) specialises per page as follows.

**Home — the front page.** The full ceremony, exactly as choreographed:
masthead (Element 13) with the day's real edition number, Late Wire
ticker, the pinned front page (Element 6) carrying the day's lead story
and 4–6 late briefs, then two or three section fronts (each opened by
Element 8's drawn red rule), one box-score table (Element 14) if the
publication has a data story that day, the subscribe coupon (Element 16),
colophon (Element 17). The home page is re-composed per edition: story
order is editorial, never algorithmic-by-default — a "for you" front page
is a contradiction this theme does not ship.

**Listing / section front — the inside page.** Masthead compresses sooner
(80px threshold — inside pages are for working, not ceremony). The section
name takes Display 2 with its red rule pre-drawn (you are inside the
marked section, Element 8's rule). Stories lay out as a briefs grid of
story cards (Element 15), 3 columns ≥1100px, 2 ≥700px, 1 below, with the
first story promoted to a half-front-page treatment (Headline 3 + photo
well + 4-line deck). Pagination prints as edition furniture: "PAGE 2 OF
6 — CONTINUED IN THE ARCHIVE" with numbered links set as folio numbers.
Filters, where a section genuinely needs them, are set as a "FILE BY"
rule-row of Franklin labels with proofing underlines — never as pill
chips, which are app furniture.

**Detail / article — the story page.** The article is the paper's core
product and gets the full typographic liturgy: kicker + drawn rule, the
headline struck at Display 2 (Element 1's spec at this scale — the strike
is not reserved for the home hero; every story is printed when opened),
dateline and byline furniture, the edition stamp, deck, then body in a
single 62ch column (multi-column flow is for the front page's density;
inside a story, one column, ragged right, drop cap, pull-quotes with the
red left rule). Photos enter as wells with the dry-down (Element 7).
Mid-article, after roughly 40 column inches, a "LATE BRIEFS" rail interrupts
in `--newsprint-deep` — the desk reminding you the world continued —
then the story resumes. The ink-line (Element 5) measures *this story's*
column inches here, and at the story's end the colophon-line for the
article prints: "— END OF STORY — Filed at 02:14 —" followed by the
reporter's real name and the corrections link for this story. Related
stories are "MORE FROM THE WIRE": three story cards, no carousel.

**About — the masthead story.** Set as the paper's own profile of itself:
Display 2 headline ("The Paper, Since …"), body columns telling the real
history, a box-score table of the publication's real milestones (years as
row labels — a timeline is a table that lost its nerve), photographs of
the real office/press treated as wells. The staff list prints as a
masthead box (the boxed staff list from a real paper's page two): names
in Franklin, roles in Newsreader italic, ruled top and bottom. If the
publication has no real history yet, the page says so in one honest
paragraph — an invented heritage is the theme's cardinal sin (§9).

**Contact / subscribe / checkout equivalents — the office pages.** All
transactional pages are office paperwork: the clip-coupon form (Element
16) is the page's centre, set in a single column on the flat ground with
the masthead above and a shortened colophon below (imprint + record
columns only). A checkout (for a paid edition) prints as a two-part
coupon: the order coupon and, beneath a second cut line, the payment
coupon — the visual separation teaches the reader what is shared with
whom. Confirmation pages are office receipts (Element 16's success
state at page scale): stamp, reference number, real time, and "KEEP
THIS RECEIPT" in Franklin — plus the practical next step as a story
card ("YOUR FIRST EDITION ARRIVES TONIGHT — read the current one").
Error pages (404) print as a correction notice: "CORRECTION — The page
you sought was not in this edition", the correction box styling, and
three story cards from the current front page, because a reader who hit
a dead page is owed the paper, not an apology illustration.

**Archive / search — the bound volumes.** Results print as a folio
index: year rules (drawn, Element 8), then rows of date + headline +
edition number with dot leaders — the bound-volume index of a library
set. Search itself is "SEARCH THE ARCHIVE" from the masthead; the
results header reports in the paper's units ("214 STORIES FILED UNDER
'MONSOON'"). No infinite scroll in the archive: bound volumes have
pages, and pagination is honest about the count.

---

## 8. Worked example — the front-page hero, end to end

One complete section, built exactly as specified: the home page's hero —
masthead base, struck lead headline, lead photo, and the opening of the
pinned briefs stage (Elements 13, 1, 2, 5, 6, 7 in assembly). Assume a
desktop viewport 1440×900, light mode, no reduced-motion preference, JS
enabled. The story: the night's lead, a monsoon flood story.

**The DOM, in order.**

```
<header class="masthead">            (Element 13)
  <div class="nameplate-row"> date furniture | NAMEPLATE | live fact </div>
  <nav class="section-rule"> sections…  ARCHIVE </nav>
  <div class="ink-line"> track + fill + bead + caption (Element 5) </div>
  <div class="late-wire"> LATE WIRE | ticker track </div>
</header>
<main>
  <section class="pin-stage">       (Element 6, 220vh)
    <div class="lead">               (sticky, top: 96px + masthead bar)
      <p class="kicker">MONSOON — THE LEAD <span class="edition-stamp"> (Element 2)
      <h1 class="strike"> 3 × .strike-line > .strike-inner </h1>   (Element 1)
      <p class="deck">…</p>
      <figure class="well"> img + .halftone + caption </figure>    (Element 7)
    </div>
    <aside class="briefs-rail"> 5 × <article class="brief"> … </aside>
  </section>
  …
```

The DOM order is editorial order (lead before briefs) so the no-CSS and
mobile readings are correct before a single style loads.

**The timeline, from navigation start.**

- **t = 0ms.** The fresh sheet lands (Element 12, 380ms) — or, on first
  visit, the server-rendered page simply paints. The masthead is already
  in final state except the nameplate, which is armed for its stamp.
  All hero content is visible in raw HTML at this instant; nothing below
  depends on animation to become legible.
- **t ≈ 60ms.** `document.fonts.ready` resolves (or the 300ms cap is
  running). The nameplate stamps: 220ms, scale 1.04→1, blur 1.5→0,
  `--ease-strike`. The ink-line sits at the reader's true progress
  (0 on a fresh visit). The ticker starts its linear crawl.
- **t ≈ 300ms.** Nameplate done. The kicker strikes (single line, 180ms,
  no blur). The edition stamp — server-rendered "NIGHT EDITION · 02:14",
  already corrected by JS to the visitor's clock — stamps in beside the
  dateline: 180ms, scale 1.35→1, rotate −2.4°→−1.2°.
- **t ≈ 420ms.** Headline line 1 strikes (240ms): rises 12px in its mask,
  scale 1.06→1, blur 2→0. Line 2 starts at +60ms stagger, line 3 at
  +120ms. By **t ≈ 780ms** the full headline — "THE RIVER TOOK THE LOWER
  CITY AT 2 A.M." — is printed. The deck's clip wipe runs 300ms from
  t ≈ 660ms (120ms after line 3 lands, overlapping the tail of the
  strike — the editor starts the summary while the last line settles).
- **t ≈ 900ms.** The lead photo well, already in view, develops: photo
  scale 1.08→1 and grain 24%→12% over 1100ms. The briefs rail's first
  brief feeds (14px travel, 700ms). The hero is fully alive by t ≈ 2s —
  and was fully *readable* from t = 0.
- **Scrolling.** The reader scrolls. The shared rAF loop (one listener,
  lerp 0.14) drives: the cylinder turning in the left rail (3 turns over
  the page), the ink-line filling with its bead, the caption stepping
  "12 COLUMN INCHES READ → 18 → 24…". At the pin stage, the lead sticks;
  the photo completes its settle (the scrub's remaining range); five
  briefs feed past at 700ms each as they enter. After 120vh of travel
  the lead releases exactly as the first section front's red rule begins
  to draw — the run hands off to the next sheet without a dead frame.
- **Interaction.** The reader hovers the lead headline: the proofing
  underline draws beneath it in 220ms. They click a brief: press-thud,
  120ms down, ink darkening — then the fresh-sheet transition carries
  them to that story, whose own headline strikes on arrival.

**The numbers a reviewer can check.** Total entrance choreography ≤2s;
headline fully printed ≤800ms after fonts; pin travel exactly 120vh;
ticker 60px/s; grain loop 6s with ≤3 wells drying at once; one rAF loop;
zero layout shift after t = 0 (all spaces reserved — the stamp's
rotation is inside its furniture box, the EXTRA-width trick is not needed
here, the photo well's aspect ratio is declared in markup).

**The same hero with reduced motion.** Nameplate, kicker, headline,
deck, photo: all present at first paint, final state. No pin — lead and
briefs stack. Ink-line steps in 10% increments. Ticker is a static
three-item list. The page a motion-sensitive reader gets is the finished
front page, which — this is the theme's deepest safety property — was
always a complete design, not a degraded one.

**The same hero with JS disabled.** Identical static front page, server
times in the stamps with the timezone named, ticker as the static list,
progress rule as a plain double hairline. Every word readable, every
link live. The press is stopped; the paper still came out.

---

## 9. Anti-slop — how THIS theme goes cheap, and the cure

Generic advice ("avoid clutter") is useless here. These are the specific
ways a Midnight Press Run build turns into a costume, each with its cure.

1. **The fade-up infection.** Sections fading in with opacity and a soft
   rise — the default of every animation library — because the builder
   reached for the familiar. *Cure:* opacity is never animated in this
   theme (except the stamp's arrival and the reduced-motion page cut).
   Entrances are feeds and strikes (Elements 1, 3). A build review that
   finds `opacity` in an entrance keyframe fails the gate (§10).
2. **Red as a brand colour.** Buttons, links, icons, and badges all red
   "because it's the accent". The page ends up shouting everywhere and
   the EXTRA box has nowhere to go. *Cure:* the ≤3% pixel cap (§2) is
   measured, not vibes: screenshot the page, threshold the red — over
   3% outside the breaking box and the build goes back. Red is a human
   editor's mark; software defaults are ink.
3. **Grain over everything.** A noise overlay across the whole page at
   5% "for texture" — instantly a template. *Cure:* grain exists only
   inside photo wells (Element 7), as the photographs' halftone screen.
   The paper ground is *flat* `--newsprint`; real newsprint reads flat
   at arm's length.
4. **Fake timestamps and invented circulation.** A stamp that says
   "02:14" because the designer liked the look; a counter that says
   "1.2M readers" because the hero needed a number. This is the theme's
   cardinal sin — its signature details are *records*, and a false record
   poisons every true one. *Cure:* every stamp reads a real clock, every
   counter a real figure from the site's data, every edition number the
   real count — or the element is omitted. The Real Content Rule is
   load-bearing in this theme more than in any other.
5. **The shrunken shout.** A Display 1 headline auto-shrunk to 30px to
   fit a long title on mobile, looking like a caption in a loud font.
   *Cure:* headlines are copy-edited to fit (§3): max 3 lines, floor of
   44px on the smallest screen, rewrite the words — never shrink the
   voice.
6. **Costume props.** Scissors that snip, a typewriter sound, coffee-cup
   icons, "vintage" sepia photos, torn edges on every card. One true
   prop per page is a detail; five is a theme park. *Cure:* the theme's
   props are exactly: the cylinder, the stamp, the coupon's scissors
   mark (static), the torn edge (on success only). Anything else must
   argue its way in against this list — and sepia is banned outright:
   photos are greyscale ink, never brown nostalgia.
7. **The floating cylinder.** The press cylinder pasted over content, or
   shrunk into a corner on mobile "so it still appears". *Cure:* it
   lives in the rail or it retires (Element 4). An element that has to
   be miniaturised to survive a breakpoint was furniture for one
   breakpoint only — let it be that, proudly.
8. **Blog drift.** Centred headlines, "3 min read", pill tags, a
   newsletter popup at 10 seconds, related-post carousels. Each is small;
   together they are a blog wearing a masthead. *Cure:* §4's alignment
   law and §7's units (column inches, folio pages, wire items) are
   checked in review. A popup, in particular, can never exist in this
   theme: the coupon is a section of the page, and paper does not
   interrupt.
9. **Permanent misregistration.** Resting elements left rotated or
   offset "for character" — headlines at −0.5°, rules that never align.
   It reads as sloppiness within a day. *Cure:* registration error
   exists only *during* the feed (Element 3) and in the stamp's −1.2°
   (a hand did that). Everything at rest is true to the grid.
10. **The empty EXTRA.** A breaking box rendered with placeholder copy
    "because the layout needs it", or last week's news still pulsing.
    *Cure:* Element 9's staleness demotion is mandatory logic, not a
    suggestion; and when there is no breaking story, the box is absent
    and the front page leads with its second story — a real paper has
    slow nights and prints anyway.

---

## 10. Quality gate — the Midnight Press Run checklist

A build may not ship in this theme until every **blocking** item passes
and at least 10 of the 12 **standard** items pass. The reviewer checks
evidence (screenshots, measurements, a JS-off load), not intentions.

**Blocking — all must pass.**

1. **JS-off test:** with JavaScript disabled, every page shows all
   content in final state, all links work, the form submits, stamps show
   a true time with its timezone named.
2. **Fallback test:** with animation triggers deliberately broken (IO
   unsupported simulation), the 1.2s force-settle fires and no content
   remains in a pre-state on any page.
3. **Reduced-motion test:** with `prefers-reduced-motion` set, no
   element travels, scrubs, pulses, or ticks; the static front page is
   complete and the ticker is a readable list.
4. **Truth audit:** every stamp time, edition number, counter figure,
   and imprint line on the page traces to a real clock, a real count,
   or real publisher data. One invented figure fails the build.
5. **Red ration:** measured red coverage ≤3% of pixels on a full-page
   screenshot (breaking box excluded); no red body text under 14px
   except `--red-deep` at AA contrast.
6. **Registration audit:** at rest, every column, rule, and headline
   measures 0px offset from the grid; the only resting rotations are
   the edition stamps (−1.2°).
7. **Cursor & cover audit:** the system cursor is unchanged everywhere;
   no animated element overlaps or covers text at any scroll position
   (checked at 5 scroll depths on home and article pages).
8. **Pin discipline:** at most one pinned scene per page; the pin
   disables itself under 600px viewport height and under reduced
   motion.

**Standard — at least 10 of 12.**

9. Headline strike completes ≤800ms after fonts ready; deck wipe follows
   the specified offset; no headline ever strikes in a fallback font.
10. One shared rAF loop drives cylinder, ink-line, and parallax;
    scroll stays at 60fps on a mid-range Android device (no frame over
    20ms attributable to theme code during a full-page scroll).
11. Counters use tabular figures, roll once, upward only, and land on
    the true value; the column-inch caption steps in whole inches.
12. Grain appears inside photo wells only; ≤3 wells shimmer at once;
    grain and shimmer are off under `save-data`.
13. The coupon form works fully without JS, keeps inputs ≥16px on
    mobile, and its success state prints a receipt with a real time and
    reference.
14. Type scale is unmodified: Display 1 appears once per page, never
    below 44px at any width; kickers always paired with their rule.
15. Dark mode uses the night-desk tokens (§2): red is `#E0483C`, ground
    is `#101014`, no pure black panels, no pure white text.
16. The ticker pauses on hover, focus, and hidden tab; it carries ≤8
    items, all linking to live stories.
17. Cards lift ≤3px with the hard shadow only; visited cards show the
    pencil-grey stamp; sponsored cards carry the dashed frame and the
    "ADVERTISEMENT" head.
18. Page transitions, where armed, complete in ≤380ms, disable
    themselves on slow connections, and never delay LCP.
19. Print stylesheet: `@media print` removes grain, ticker, cylinder,
    and transitions, and the page prints as a clean sheet — the theme's
    final proof that the paper was real all along.
20. The five-second test (§1): a first-time viewer describes the page as
    *just printed, at night* — not "vintage", not "retro", not "a
    newspaper theme".

**Minimum bar, in one line:** a build that passes the blocking eight has
earned the right to be judged on premiumness; a build that then also
clears the standard list *and* makes a reviewer say the §1 sentence out
loud is a Midnight Press Run. Anything less is a newspaper costume, and
it goes back to the desk.

---

## Part II — Deepening (50x standard)

*Deepening pass written to `EXPANSION-STANDARD.md` v2, ordered 2026-11-23.
Part I (§1–§10) stands unchanged — this part deepens it, never redesigns
it. §11 gives every one of the seventeen elements its six v2 layers:
millisecond choreography, full state matrix (desktop + touch), breakpoint
behaviour, edge cases and failure modes, accessibility spec, and the exact
tokens consumed. §12–§17 then deepen the theme as a whole: component
inventory, copywriting voice, three worked examples with scroll timelines,
the full-page scroll choreography map, the whole-page performance budget,
and the build-order checklist.*

*Reading note on state matrices: "n/a" is always a designed decision, never
an omission — the cell states why the state cannot occur for that element.
Contrast figures are against `--newsprint` in the day sheet unless a night
figure is given; night figures are against the `--ink` ground with
`--press-red-night` `#E0483C` where red is involved.*

---

## 11. Per-element deepening

### Element 1 — Live-printed hero headline (deepening)

**Choreography timeline** (trigger: masthead stamp complete AND
`document.fonts.ready` resolved or the 300ms cap hit — whichever is first;
all times relative to that trigger, t=0):

- **t = 0ms** — kicker strikes: single line, translateY 8px→0 inside its
  mask, 180ms `--ease-strike`, no blur (small type bleeds less, §6.1).
- **t = +40ms** — edition stamp begins its stamp-in (Element 2's timeline
  runs concurrently; the stamp never waits for the headline).
- **t = +90ms** — headline line 1 strikes: translateY 12px→0, scale
  1.06→1, blur 2px→0, 240ms `--dur-strike`, `--ease-strike`.
- **t = +150ms** — line 2 strikes (60ms stagger). **t = +210ms** — line 3
  strikes. A 1-line headline runs line 1 only; a 2-line headline ends at
  t = +390ms; the 3-line maximum ends at **t = +450ms**.
- **t = last line +120ms** — deck clip-wipe starts: clip-path inset
  right 100%→0, 300ms `--ease-proof`. For a 3-line headline that is
  t ≈ +570ms → +870ms. The wipe overlaps nothing else; the photo well
  (Element 7) begins its dry-down only when it enters the viewport, on
  its own trigger.
- **t = animationend (per line)** — the `filter` and transform are removed
  from that line's span immediately; by t ≈ +900ms the whole block is
  plain static type with zero animation residue.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (printed) | Static full-ink headline; the permanent state after t ≈ +900ms | Identical |
| Hover | Proofing underline draws under the whole block (Element 10: scaleX 0→1, 220ms `--ease-proof`) — the headline is a link on most pages | n/a — no hover; the first tap is the click |
| Focus | Underline pre-drawn (no draw animation) + 2px `--ink` outline, offset 3px, around the block | Same on focus-visible (external keyboard / switch control) |
| Active | Press-thud on the block: scale .98 + 8% ink wash, down 120ms `--ease-press`, release 260ms `--ease-sheet` | Same thud on tap — the headline's only touch feedback |
| Scrolled-past | Printed is printed: no state change, no re-strike, ever | Identical |
| Disabled | n/a — a headline is never disabled; if its story is withdrawn, the headline is replaced by the correction line (§13), not greyed | n/a |

**Breakpoints.** **≥1200px:** Display 1 at full clamp (52–112px), up to
3 lines, blur 2px. **768–1199px:** Display 1 clamps to 44–64px; the strike
is unchanged (240ms/line) but the stagger tightens to 50ms — a smaller
page prints a little faster; blur stays 2px. **<768px:** Display 1 floor
44px (§3's law: rewrite the copy, never shrink below 44px); blur drops to
1px; the deck wipe shortens to 240ms; if the headline still needs 3 lines
at 360px, the build fails §10 item 14 — the words are re-edited, not the
type shrunk.

**Edge cases & failure modes.** *Slow network / fonts late:* the 300ms cap
fires the strike in the metric-matched fallback face only if
`document.fonts.ready` has not resolved — no: the strike waits for fonts
or the cap, and at the cap it strikes in whatever face is live, because a
headline that waits 2s for a font is worse than a headline struck in
Georgia; the metric overrides (§3) hold reflow to ≤2px when the real face
lands, and a face-swap after printing never re-strikes. *No canvas/WebGL:*
irrelevant — this element is DOM transforms and one filter; the theme uses
no canvas or WebGL anywhere. *Low-power device:* if
`navigator.hardwareConcurrency ≤ 2` or `deviceMemory ≤ 2`, the blur is
dropped entirely (translate + scale only) — blur is the only GPU-expensive
term in the strike. *Headline longer than 3 lines:* build-time failure,
handled editorially (§3), never by a 4th line striking — the mask system
supports exactly the lines the layout produced at strike time. *Headline
shorter (1 line):* the choreography compresses per the timeline; the deck
wipe still waits for last-line +120ms, so a 1-line hero feels brisk, not
broken. *Scroll-up:* nothing — the strike is load-triggered, not
scroll-triggered; it cannot re-run.

**Accessibility.** The `<h1>` is the page's first heading and is never
`aria-hidden` at any point in the strike — the pre-state is a transform
inside a mask, the text is in the accessibility tree from t = 0, and
screen readers announce the real headline, never line fragments (the
line spans are `aria-hidden` duplicates? No — the spans ARE the text;
splitting must preserve one continuous accessible name: the `<h1>` carries
an explicit `aria-label` with the full headline and the visual spans are
`aria-hidden="true"`). Focus order: the headline link, when it is one,
sits in natural DOM order after the masthead nav. Contrast: `--ink` on
`--newsprint` ≈16:1 at rest, hover, and active (the thud's 8% wash only
darkens); the underline is `--press-red` 4.8:1 — decorative reinforcement
of a state also carried by the outline on focus, never the sole signal.
Touch target: when the headline is a link, its block is the target —
minimum 44px tall is automatic at Display sizes.

**Tokens consumed.** `--ink`, `--newsprint`, `--press-red` (underline via
Element 10), `--ease-strike`, `--ease-proof`, `--ease-press`,
`--ease-sheet`, `--dur-strike` (240ms), `--dur-mark` (220ms),
`--dur-instant` (120ms), plus the type tokens of §3 (Display 1 / Kicker /
Deck). No element-local tokens.

### Element 2 — Real-clock edition stamp (deepening)

**Choreography timeline** (trigger: the stamp's furniture row is painted;
on a hero, t=0 is Element 1's trigger +40ms):

- **t = 0ms** — stamp airborne: scale 1.35, rotate −2.4°, opacity 0.
- **t = 0–55ms** — opacity 0→1 (a stamp arrives already inked; the fade is
  only the paper-contact blur of the motion, complete by 30% of the move).
- **t = 0–180ms** — scale 1.35→1, rotate −2.4°→−1.2°, `--ease-strike`.
  Contact is at t = 180ms; there is no bounce and no overshoot — a stamp
  that bounces is a toy.
- **Hourly re-stamp (and on edition change):** t = 0ms lift — scale
  1→1.12, rotate −1.2°→−2.0°, 90ms `--ease-strike`; t = 90ms the text
  swaps while the stamp is up (the swap is never seen mid-air); t = 90–
  270ms strike — scale 1.12→1, rotate →−1.2°, 180ms. Total 270ms. If the
  tab is hidden at the hour, no timeline runs: the text is correct on
  return, unstamped (§6.2).
- **Clock discipline:** a 60s interval compares the current minute to the
  stamped minute; the re-stamp fires on the first check after the hour —
  the stamp may be up to 59s late to re-stamp, and its *text* is
  corrected by the same check even if the animation is suppressed.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed at −1.2°, `--press-red` border + text, server-or-local time | Identical |
| Hover | None — `cursor: default`; a stamp is a record, not a control | n/a |
| Focus | Never focusable (`tabindex` absent, not a link) | n/a |
| Active | None | n/a |
| Scrolled-past | Unchanged; the hourly re-stamp still fires if the hour turns while it is off-screen? No — the text updates silently off-screen; the stamp animation runs only if the stamp is in the viewport when the check fires | Identical |
| Disabled | n/a — if the clock source fails entirely, the stamp degrades to the *stale* state below, never to disabled | n/a |
| Stale (extra state, designed) | Server-rendered time stands, timezone named in the adjacent dateline; visually identical — staleness is carried by the dateline's honesty, not by greying the stamp | Identical |

**Breakpoints.** **≥1200px:** 11px, in the headline's furniture row.
**768–1199px:** unchanged size and position; the furniture row may wrap
the dateline under the stamp, never the reverse. **<768px:** unchanged
11px (a smaller stamp is a smudge, §6.2); below a 340px headline measure
the stamp takes its own furniture line above the dateline — layout moves,
the stamp never shrinks.

**Edge cases & failure modes.** *Visitor clock wrong:* the stamp prints
the visitor's local time by design (it is *their* edition moment); a
visitor with a wrong clock gets a wrong stamp and a true paper — the
theme does not second-guess the reader's watch, but the edition *number*
always comes from the server, so the record's sequence stays true.
*Timezone API absent:* server time + named timezone (the stale state).
*Slow network:* the stamp is server-rendered HTML — it exists before any
JS or font arrives; only the correction to local time waits. *No
canvas/WebGL:* n/a. *Low-power:* the 60s check is the whole cost; nothing
is throttled further. *Edition changes twice in one hour:* the re-stamp
fires per edition change with the new number; two re-stamps never queue —
a pending one is replaced. *Scroll-up:* n/a — the stamp is load- and
clock-triggered.

**Accessibility.** The stamp is text, not an image of text: it is read by
screen readers as part of the dateline furniture. It carries no
interaction, so no focus or target rules apply. Contrast: `--press-red`
on `--newsprint` ≈4.8:1 at 11px bold uppercase — permitted because the
stamp is *furniture duplicating* information also present in the dateline
text at full contrast (the time is never available ONLY in the stamp);
in the night sheet, `--press-red-night` holds ≈4.7:1 on the ink ground
under the same duplication rule. The −1.2° rotation never applies to the
dateline text beside it.

**Tokens consumed.** `--press-red`, `--press-red-night` (night),
`--ease-strike`, plus element-local `--stamp-rot: -1.2deg` and
`--stamp-lift-rot: -2.4deg`. Type: Byline/dateline role (§3).

### Element 3 — Conveyor sheet feed (deepening)

**Choreography timeline** (trigger: the section's top crosses 80% of
viewport height in the IntersectionObserver; t=0 is the trigger frame):

- **t = 0ms** — keyframe 0%: translateY 26px, `--reg` at its full seeded
  value (±1.5–2.5px, sign and magnitude fixed per section index).
- **t = 0–495ms (55%)** — the sheet travels: translateY 26px→8px;
  `--reg` holds near full value (≥85% of it at the 55% mark, keyframed
  ±2.2px against a ±2.5px start) — the sheet is visibly out of register
  for most of its journey, which is the point.
- **t = 495–900ms (55–100%)** — registration: translateY 8px→0, `--reg`
  eases to exactly 0. The last 405ms is the run finding its rhythm; no
  other property moves.
- **t = 900ms (`animationend`)** — the transform is removed from the
  element entirely (not zeroed — removed), releasing the layer and any
  containing-block side effects (§6.3).
- **Above-the-fold cascade (page load only):** sections already past the
  trigger at load do not all fire at once — they feed in document order
  with a 90ms stagger, the first starting 100ms after Element 1's strike
  completes. A fast scroll queues feeds in document order; at most 2 run
  concurrently, the rest wait at keyframe 0% — a fast scroll prints a
  fast run, but the sheets still land in order (§6.3).

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (unfed) | Held at keyframe 0% by the JS-armed class only; without the class, fully printed | Identical |
| Hover | n/a — the feed is not an interaction; hover over a feeding section changes nothing | n/a |
| Focus | If focus lands inside an unfed section (keyboard jump, find-in-page), that section force-settles instantly — a reader must never focus invisible-offset content | Same (switch control / VoiceOver swipe) |
| Active | n/a | n/a |
| Scrolled-past | Settled and transform-free; scrolling back up shows the printed page — feeds never re-run, never reverse | Identical |
| Disabled | n/a as a state; the whole element is disabled by `prefers-reduced-motion` or by the force-settle fallback (below) | Identical |

**Breakpoints.** **≥1200px:** full spec — 26px travel, ±2.5px drift,
900ms. **768–1199px:** travel 20px, drift ±2px, 800ms — the sheet is
smaller, the machine is the same. **<768px:** travel 16px, drift ±1.5px,
700ms (§6.3's mobile variant: at 360px wide, 2.5px of drift reads as a
rendering bug, 1.5px reads as machinery).

**Edge cases & failure modes.** *IntersectionObserver missing/ancient
browser:* the 1.2s force-settle timer (§5 law 2) prints every armed
section — content is never hostage to an API. *Slow network:* feeds are
armed only on sections whose content has actually rendered; a section
still in skeleton (Element 11) feeds as skeleton and inks in place — the
feed never waits for content, and content never waits for the feed.
*No canvas/WebGL:* n/a — CSS keyframes on one transform. *Low-power
device:* below the §16 frame budget's floor device, drift is dropped
(travel only, `--reg` fixed at 0) — registration error is a repaint of
every column rule, and it is the first motion term this element
surrenders; travel shortens to 600ms. *Content taller than expected (a
section 3× the designed height):* the feed is identical — the transform
is on the section box, not its contents; very tall sections (>250vh)
trigger at the same 80% line and the reader meets an already-settled top
by the time they arrive, which is correct. *Content shorter (a one-line
section):* the feed still runs its full 900ms — a short sheet travels
the same conveyor; shortening it would make small sections feel cheaper
than large ones. *Scroll-up mid-feed:* the animation continues to settle
(CSS animations do not reverse on scroll); a section caught mid-feed
finishes printing while the reader looks elsewhere and is settled when
they return.

**Accessibility.** The pre-state is a transform only — never opacity,
never `visibility` — so the content is in the accessibility tree, in
reading order, at full contrast, from the first paint; a screen reader
user experiences no "unfed" state at all. Focus-into-unfed force-settle
(above) is the one JS behaviour with an accessibility duty, and it is
blocking in the §16 budget. Contrast is unaffected by the drift (the
whole sheet, text and ground together, moves as one). No touch targets
are created or moved by this element; the ≤2.5px drift never displaces a
target by more than the drift itself, and targets are only displaced
*before* they can be tapped (a feeding section is entering, not resting).

**Tokens consumed.** `--ease-sheet`, `--dur-sheet` (900ms), element-local
`--reg` (seeded per section index), `--rule` (the column hairlines that
drift with the sheet). No colour tokens — the feed moves the sheet, it
does not repaint it.

### Element 4 — Margin press cylinder (deepening)

**Choreography timeline** (trigger: continuous — the shared rAF loop;
there is no entrance event):

- **Every frame while the page scrolls:** the loop reads the lerped
  progress value p (0→1, lerp factor 0.14 per frame at 60fps) and sets
  the drum group's rotation to p × 1080deg and the edition line's colour
  interpolation to p. The lerp means the drum reaches a step change in
  scroll position over ~7 frames (≈115ms) — geared, not glued (§5).
- **Scroll stops:** the drum settles to the exact geared angle within
  the same ~115ms and then does not move a fraction of a degree. There
  is no idle rotation at any point in the page's life.
- **Page load at a restored scroll position:** the first frame paints
  the drum at the true angle for that position (p computed before first
  paint from `scrollY`), never at 0 — the press is found as the reader
  left it.
- **End of page (p = 1):** 1080deg exactly, edition line at full `--ink`.
  No completion gesture, no snap — the third turn simply ends.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (top, p = 0) | Forme arc at top-dead-centre, edition line at `--smudge` | n/a — the rail does not exist below 1280px (see Breakpoints) |
| Hover | None — the cylinder is not interactive and shows no hover affordance | n/a |
| Focus | Never focusable; it is `aria-hidden` decoration-with-a-job (its job's output, progress, is duplicated by Element 5's captioned rule) | n/a |
| Active | None | n/a |
| Scrolled-past (p = 1) | Three turns complete, line fully inked; scrolling up counter-rotates exactly — the gearing is symmetric | n/a |
| Disabled | Retired (not greyed — *absent*) below 1280px, under reduced motion (printed static), and when the rail would overlap content | Absent |

**Breakpoints.** **≥1280px** (the rail's own threshold, stricter than
the theme's 1200px band): full spec — 64px drum in the 96px rail, edition
line vertical beside it. **768–1279px:** retired completely; Element 5
carries progress alone. There is no mid-size cylinder. **<768px:**
retired; same carrier. The retirement is a layout fact, not a media-query
afterthought: the rail is inside the 1296px max-width envelope, and the
grid never makes room for a drum it cannot house at full size.

**Edge cases & failure modes.** *Rail would overlap content* (a page
template with a wider measure): the rail yields — `display: none` — the
cylinder never prints over a word (§10 item 7 audits this). *Slow
network:* the drum is one inline SVG in the initial HTML; it cannot
arrive late. *No canvas/WebGL:* n/a — SVG transform. *Low-power:* the
drum is one transform per frame in the shared loop (<0.5ms); if the §16
frame budget is breached page-wide, the drum's update drops to every
second frame (rotation steps of ~2× the angle — a geared press on a
weak motor still turns, just coarser) before any other element is cut.
*Very long page (a 300-inch archive index):* still exactly 3 turns —
the gearing ratio is per-page, so on a long page the drum turns slowly;
that is correct press behaviour, not a bug to fix with more turns.
*Very short page (no scroll):* p is 0 forever, the drum rests at
top-dead-centre and the edition line stays at `--smudge` — an unread
sheet's line is un-inked, honestly. *Scroll-up:* symmetric
counter-rotation; the edition line's colour returns toward `--smudge`
at exactly the rate it inked.

**Accessibility.** `aria-hidden="true"` on the SVG and the rotated
edition line is duplicated in the masthead's accessible furniture (the
edition number appears in Band 1 as ordinary horizontal text), so no
information exists only in the rail. Contrast: the edition line's
interpolation runs `--smudge` (≈5.9:1, AA for its 10px furniture role as
duplicated metadata) to `--ink` (≈16:1); at no point does it pass through
a value lighter than `--smudge`. No focus, no target, no motion that a
reduced-motion user ever sees (static print under the preference).

**Tokens consumed.** `--ink`, `--press-red` (the forme arc),
`--press-red-night` (night forme), `--smudge`, `--newsprint` (highlight
arc at 20%). Element-local: `--drum-turns: 3` (1080deg at p = 1). No
duration or easing tokens — the lerp in the shared loop is the timing.

### Element 5 — Ink-line progress rule (deepening)

**Choreography timeline** (trigger: continuous scrub, shared rAF loop):

- **Every frame while scrolling:** fill scaleX = lerped progress
  (factor 0.14); the 3px bead rides the fill's leading edge (it is a
  child of the fill, so it inherits the transform — no separate
  calculation exists to drift out of sync).
- **Caption updates:** the column-inch figure is recomputed from the
  lerped progress but only *repainted* when the computed whole-inch value
  changes by ≥6 inches of travel (§6.5) — in practice the caption steps
  a handful of times per screen of reading, each step a single text-node
  change, no animation on the digits themselves (a gauge's numbers do
  not perform).
- **Load at restored position:** first paint shows the fill at true
  progress and the caption at the true figure — the timeline has no
  "from 0" beat on a return visit.
- **Completion (p = 1):** the frame where progress reaches 1, the bead
  touches the right edge and the caption swaps to "FULL SHEET READ —
  No. {edition}" in the same frame. No pulse, no hold, no celebration
  beat follows — ever.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (0%) | Track only (`--rule`), caption "0 COLUMN INCHES READ" or the edition variant on non-article pages | Identical |
| Hover | None — the rule is furniture, not a control; it is never clickable, never a seek bar (a reader cannot scrub a newspaper) | n/a |
| Focus | Never focusable | n/a |
| Active | None | n/a |
| Scrolled-past (100%) | Fill full, bead at the edge, caption in the FULL SHEET state; holds indefinitely | Identical |
| Disabled | n/a — under reduced motion the element is not disabled but *stepped*: fill jumps in 10% increments with no lerp (§6.5) | Identical |

**Breakpoints.** **≥1200px:** full caption ("37 COLUMN INCHES READ",
10px Franklin, docked right in the masthead furniture). **768–1199px:**
identical mechanics; the caption shortens to "37 IN. READ" below 900px
of masthead width (measured on the masthead, not the viewport — a
compressed masthead on a wide screen compresses its caption too).
**<768px:** this element becomes the page's *primary* progress
instrument (the cylinder is retired); caption "37 IN. READ"; the rule
and its 2px fill are unchanged — progress does not get thinner because
the screen did.

**Edge cases & failure modes.** *Page with no long read (home, listing):*
the caption switches to the edition variant ("EVENING EDITION — 24
PAGES") and the fill tracks whole-page progress — the rule never claims
column inches a page does not have. *Content loads late and page height
grows (archive rail inking in):* total inches are recomputed on the
shared loop's resize/content observer; the fill may step *back* a few
inches when the sheet gets longer — a gauge recalibrating, shown as a
plain value change, never animated backward theatrically. *No JS:* the
rule prints as track + 0% fill (an unread paper must not claim to be
read, §6.5) with the edition caption. *Low-power:* the fill is one
scaleX on a 2px element — the last thing on the page that could cost
anything; it is exempt from every cut order in §16. *Scroll-up:* the
fill retreats exactly with progress — progress is a measurement, not an
achievement, and it un-measures as honestly as it measures. *Print:*
the rule prints at the reader's current progress? No — print renders
the track and a full ink line (the sheet, whole) with no caption; a
printed copy is the complete paper, not a progress snapshot.

**Accessibility.** The rule is visual furniture; its information is
duplicated for assistive tech by an `aria-valuetext`-free approach: the
caption is real text in the DOM (readable, in the masthead's order), and
the fill itself is `aria-hidden`. Contrast: fill `--ink` on the
`--rule` track — the track is structural (≥3:1 against both ground and
fill is not required of a non-text graphic that duplicates text, but
the caption at `--smudge` ≈5.9:1 passes AA outright). The bead is
decorative. No focus, no target. Under reduced motion the stepped fill
still updates — information is not motion.

**Tokens consumed.** `--ink` (fill), `--rule` (track), `--smudge`
(caption), `--newsprint` (print variant). Type: Data/counter role (§3,
tabular-nums mandatory). No easing/duration tokens — the shared lerp is
the timing.

### Element 6 — Pinned front page, scrolling late briefs (deepening)

**Choreography timeline** (scroll-driven; positions are scroll offsets
within the 220vh stage, expressed as vh of travel):

- **Travel 0vh (stage top reaches the masthead bar):** lead in natural
  flow; briefs 1–2 may already have fed on approach (their own Element 3
  triggers).
- **Travel ≈ 10vh:** the lead reaches `top: 96px` and sticks. From this
  frame the photo scrub is live: photo scale maps 1.08→1 across the
  full 120vh of stuck travel, lerped at 0.14 in the shared loop.
- **Travel 10–110vh:** the briefs rail flows past. Each brief feeds as
  its top crosses 85% of viewport height: 14px travel, 700ms
  `--ease-sheet`, once. With 5 briefs at typical heights, feeds land
  roughly every 18–25vh of travel — the desk keeps filing while the
  front page holds.
- **Travel ≈ 65vh:** the photo passes scale 1.04 — its settle is half
  done exactly when the rail is half read; the two rhythms are geared
  to the same hand.
- **Travel 120vh:** the stage's end arrives; the lead un-sticks and
  rejoins the sheet with no snap, fade, or ceremony.
- **Travel 120vh + ε:** the following section front's head crosses its
  82% line and Element 8's kicker strikes — the hand-off beat. If the
  reader scrolls fast, the un-stick and the rule-draw may share a
  frame; that is correct — a fast run is a fast run.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (approaching) | Lead static in flow, rail feeding | Stacked layout (see Breakpoints) — no pin exists to have states |
| Hover | Briefs and the lead headline take Element 10's underline/thud as ordinary content — the pin adds no hover behaviour of its own | n/a |
| Focus | Tab order is DOM order (lead, then briefs) regardless of the visual pin; if focus moves to a brief below the fold, the browser's scroll-into-view scrolls the *page*, which advances the stage naturally — the pin never traps focus | Same (assistive navigation advances the stage the same way) |
| Active | n/a as a scene state; individual links thud per Element 10 | Same |
| Scrolled-past (released) | Everything is static print; scrolling back up re-enters the stage from below — the lead re-sticks on the way up and the briefs (already fed) stay fed; the photo scrub reverses with progress, as a gear does | Stacked, static |
| Disabled | Pin disabled under 600px viewport height, under reduced motion, and below 900px width — in all three cases the element is not "off", it is *stacked*: lead first, briefs after, in editorial order | Stacked is the only form |

**Breakpoints.** **≥1200px:** full spec — 7-column lead stuck at
top: 96px, 4-column rail, 120vh travel. **900–1199px:** the stage
narrows (lead 6 columns, rail 4, gutter 1); travel shortens to 100vh —
a smaller desk files fewer briefs past the lead (rail capped at 4
briefs; the 5th and 6th move below the stage as ordinary briefs).
**<900px (incl. all <768px):** no pin, no scrub: lead prints first in
full, then the briefs as a stacked "Late Briefs" section on
`--newsprint-deep`, each feeding with Element 3 at 14px travel as it
enters. The simultaneity is a desktop pleasure (§6.6); the story —
finished lead, arriving briefs — survives in sequence.

**Edge cases & failure modes.** *Viewport height <600px at any width:*
pin disabled by media query — a pin on a short screen traps more than
it tells (§6.6). *More briefs than designed (8+ filed):* the rail caps
at 6 (4 in the 900–1199 band); overflow briefs print below the stage as
a "More from the wire" block — the stage never grows taller to fit
content; the edition is edited to the stage, not the reverse. *Fewer
briefs (1–2):* the stage still spans its travel, but the pin releases
early — the container height is set from the rail's real height
(min(travel needed, 120vh)), so a quiet night never leaves the reader
scrolling through 100vh of nothing to honour a spec number. *Lead photo
missing/failed:* the well shows its honest empty frame (Element 7's
fallback) and the scrub has nothing to scale — the pin and rail are
unaffected. *Slow network (rail briefs arrive late):* briefs ink in via
Element 11's regional skeleton inside the rail; the pin does not wait.
*No sticky support (ancient browser):* the stage is a plain two-column
block — sticky is the only mechanism, there is no JS pinning fallback to
go wrong (§6.6). *Scroll-up:* covered in the matrix — re-stick is
native sticky behaviour, feeds never re-run. *Low-power:* the photo
scrub is the only per-frame cost; it is cut before the feeds are (§16):
on the floor device the photo prints at scale 1 and the pin still pins.

**Accessibility.** DOM order is editorial order (lead, then briefs), so
screen-reader and no-CSS order are correct without any ARIA repair; the
visual pin never reorders anything. The sticky lead must never cover
focused content: because the lead is *beside* the rail (never above it),
focus in the rail is never under the lead at any scroll position — §10
item 7's cover audit includes 3 scroll depths inside this stage. The
rail is a labelled region (`aria-label="Late briefs"`) so assistive
users can find or skip the arriving news as a unit. Contrast inside the
rail: body text `--ink` on `--newsprint-deep` ≈13:1; brief stamps
follow Element 2's duplication rule. Touch targets: brief headlines are
full-width rows, ≥44px tall with their padding.

**Tokens consumed.** `--newsprint-deep` (rail ground), `--ease-sheet`,
`--dur-sheet` (at 700ms brief-feed variant), plus the tokens of Elements
1, 2, 3 and 7 for its assembled parts. Element-local: `--pin-travel:
120vh` (100vh in the 900–1199 band), `--pin-top: 96px`.

### Element 7 — Wet-ink halftone grain (deepening)

**Choreography timeline** (trigger: the photo well's first entry at 50%
viewport height):

- **t = 0ms** — the photo's scale-in-frame and the dry-down start
  together: photo scale 1.08→1, grain opacity 24%→12%, both 1100ms
  `--ease-sheet`. The two are one event — a photograph developing.
- **t = 1100ms** — the well is *dry*: grain at its 12% rest. If the well
  is among the 3 nearest the viewport centre, the shimmer loop starts
  on the next 6s boundary: opacity 12%→17% over 3000ms, 17%→12% over
  3000ms, `ease-in-out`, with a 1-cell (6px) background-position drift
  across each full cycle.
- **Continuous while visible:** parallax — the dot layer translates at
  0.6× the well's scroll speed through the shared lerp, capped at
  ±10px; at the cap the layer simply stops travelling (dots never
  visibly detach from the image's features).
- **Well leaves the viewport:** the shimmer freezes at whatever opacity
  it holds (it does not snap to 12% — a half-dried screen is still a
  screen) and resumes on return; the `data-drying` grant passes to the
  next nearest well.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (dry) | 12% screen, shimmer if granted, parallax live | 12% screen, static — shimmer and parallax are disabled on touch devices by the performance rule (§6.7), so touch rest = printed screen |
| Hover | None — the grain is the photo's surface, not a control; hovering a photo does nothing to its screen | n/a |
| Focus | None (a focusable photo link shows Element 10's outline on the *well*, the grain is untouched) | Same |
| Active | None | n/a |
| Scrolled-past | Rest state continues — the grain is visibility-tied, not position-tied | Static rest |
| Disabled | Under `save-data`, low-power, or print: the layer is either flat-static 12% (save-data) or removed entirely (print — a printed halftone of a halftone is a moiré, §6.7) | Same |

**Breakpoints.** **≥1200px:** full spec. **768–1199px:** full spec —
wells are smaller but the dot cell is *not* scaled (3px dots in a 6px
cell at every size; the screen belongs to the printing process, not to
the layout). **<768px:** the screen remains at rest 12% and the dry-down
still runs on entry (it is the photo's entrance, not an ambient extra),
but shimmer and parallax never run — mobile wells print dry-looking
from 1100ms onward.

**Edge cases & failure modes.** *Blend mode unsupported (old browser):*
the layer falls back to a plain low-opacity dot overlay (§6.7) — the
dry-down and rest states are unchanged, only the multiply richness is
lost. *Image fails to load:* the well keeps its `--newsprint-deep` bed,
caption and credit, grain at flat 12% — an honest empty frame; the
dry-down does not run (nothing developed). *Image is a graphic/diagram,
not a photo:* charts re-inked per §2 are *not* halftoned — the screen is
for photographs; a diagram under dots is illegible, and §12's chart
treatment says so again. *Very small wells (card thumbnails):* below
120px wide the dot cell steps to 4px pitch with 2px dots — at 6px pitch
a thumbnail is more dot than picture. *Slow network:* the well reserves
its aspect-ratio box; the grain bed is present before the image, so a
slow photo arrives into a printed frame, never into a void; the
dry-down waits for the image's `load` event, not the well's entry.
*Scroll-up:* parallax reverses with the lerp like every scrub; the
shimmer is indifferent to direction. *Low-power:* shimmer and parallax
off (static screen), dry-down kept — it is 1100ms, once, per photo.

**Accessibility.** The layer is `pointer-events: none`, `aria-hidden`
by construction (a `::after` with no content), and never carries
information — a photo's meaning lives in its `alt` and caption, not its
screen. Contrast: at 12% multiply the screen darkens a photo's
mid-tones by a few percent; captions sit *below* the photo on the well's
own paper, never over the grained area, so caption contrast is the
paper's ≈5.9:1 (`--smudge`) unaffected. Photos whose content is
information (a chart, a document scan) must not rely on fine detail
surviving the screen — the alt text carries the data (§12). No focus,
no targets.

**Tokens consumed.** `--ink` (dots, day), `--newsprint` (dots, night —
screen blend), `--newsprint-deep` (well bed), `--newsprint-edge` (well
border), `--ease-sheet`. Element-local: `--grain-rest: .12`,
`--grain-wet: .24`, `--grain-cell: 6px` (4px in small wells).

### Element 8 — Self-drawing red section rules (deepening)

**Choreography timeline** (trigger: the section head crosses 82% of
viewport height, once):

- **t = 0ms** — the kicker strikes: 180ms at kicker scale (Element 1's
  spec, no blur). The editor names the section.
- **t = 100ms** — the rule begins to draw while the kicker is still
  settling: `stroke-dashoffset` from full to 0, 600ms `--dur-rule`,
  `--ease-proof` — slow-fast-slow, the hand accelerating across the
  sheet and lifting carefully at the end.
- **t = 700ms** — the rule is fully drawn; in the same beat its
  dasharray is removed and the SVG settles into a plain static rule (no
  dash pattern can re-render oddly on zoom, §6.8).
- **t = 850ms** — the section's conveyor feed (Element 3) starts, 150ms
  after the rule completed: mark first, then the sheet. If the section
  was already fed (its body entered before its head crossed 82% — a
  very short viewport), the feed is not re-run; the rule still draws.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (drawn) | A static 2.5px `--press-red` rule between kicker and headline | Identical |
| Hover | None — furniture | n/a |
| Focus | Never focusable | n/a |
| Active | None | n/a |
| Scrolled-past | Drawn, static; scrolling up never un-draws — a proof mark, once made, stays made | Identical |
| Disabled | n/a — under reduced motion or no-JS the rule is simply present in full from first paint (its undrawn state exists only as a JS-armed dashoffset) | Identical |

**Breakpoints.** **≥1200px:** full width of the section's measure, 2.5px
stroke. **768–1199px:** identical — the draw is a line, and a line reads
at any width (§6.8). **<768px:** identical again, deliberately: stroke
stays 2.5px (thinner reads as an error underline, not a proofing
stroke), duration stays 600ms, and the kicker still precedes it by
100ms. This is the one element whose spec does not compress at all on
mobile.

**Edge cases & failure modes.** *Section head is the page's first
content (a section-front landing page):* the rule is pre-drawn — you
are already inside the marked section (§6.8); no timeline runs. *Many
section heads enter at once (a short page, everything above the fold):*
the draws stagger 120ms apart in document order — an editor marks one
section at a time, and simultaneous draws read as a laser show.
*Slow network:* the SVG is inline per head; it cannot arrive late; if
the section's *content* is late, the rule still draws on the head's
schedule and the body inks in under it (Element 11). *No canvas/WebGL:*
n/a — one SVG path. *Low-power:* dashoffset on a 3px-tall SVG is
compositor-cheap; exempt from cuts. *Scroll-up before trigger (reader
jumps to the footer via anchor, passing heads without the observer
firing at 82%):* any head above the current viewport when observed is
treated as already-crossed and draws immediately (or is already drawn
if the jump settled it) — a reader must never scroll up to find an
undrawn rule over a read section. *Zoom/reflow after draw:* the SVG is
in its static post-draw state, so zoom simply scales a rule.

**Accessibility.** The rule is decorative structure (`aria-hidden` —
the section's name is the kicker/headline text, which is real). It is
never the only signal of a section boundary: the kicker text and the
headline carry the structure for assistive tech, and the heading
hierarchy (kicker is a `<p>`, the headline the section's `<h2>`) is
untouched by the draw. Contrast: `--press-red` 2.5px graphic on
`--newsprint` ≈4.8:1 — exceeds the 3:1 non-text threshold, and again it
duplicates text structure. No focus, no target. Under reduced motion
the rule's presence-from-paint is the accessible form: boundaries are
visible immediately, not revealed.

**Tokens consumed.** `--press-red`, `--ease-proof`, `--dur-rule`
(600ms), plus Element 1's kicker strike tokens. Element-local:
`--rule-stroke: 2.5px`.

### Element 9 — "EXTRA" weight-pulse (deepening)

**Choreography timeline** (trigger: the breaking box enters the
viewport; the pulse loop runs only while it is on screen):

- **t = 0ms (first entry)** — the box feeds at half conveyor travel:
  translateY 12px→0, 700ms `--ease-sheet`, `--reg` 0 (breaking news is
  never out of register — it was set carefully, in a hurry).
- **t = 0ms (concurrent)** — the weight pulse starts at 400:
  `font-variation-settings 'wght'` 400→900 over 800ms `ease-in-out`,
  900→400 over 800ms — one full shout every 1600ms, phase-locked to
  entry so two boxes (there is never more than one, §6.9) could never
  pulse against each other anyway.
- **Hover begins (any point in the cycle):** the pulse freezes at its
  current weight within one frame — it does not finish its swell — and
  the headline's proofing underline draws (220ms). The shout stops
  mid-breath because the reader has picked the sheet up.
- **Hover ends:** the pulse resumes *from 400* on the next loop
  boundary, not from the frozen weight — resuming mid-swell looks like
  a stutter; restarting the shout is cleaner.
- **Demotion (staleness):** when the item passes the freshness window
  (default 90 minutes), nothing animates: on the next render the box is
  simply a brief in the rail, weight static. Demotion never happens
  visibly in front of a reader.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (off-screen) | Weight frozen at 400; box static in the `--red-wash` panel | Identical |
| Hover | Pulse paused at held weight; proofing underline drawn under the headline | n/a — no hover; the box is read or tapped |
| Focus | Pulse pauses (same as hover — focus-within counts); underline pre-drawn + 2px ink outline on the box's link | Same on focus-visible |
| Active | Press-thud on the box's link (Element 10) | Thud on tap |
| Scrolled-past | If still within its freshness window, it pulses again on re-entry (the loop is visibility-gated, not once-only — breaking news is alive while it is breaking) | Identical |
| Disabled | Pulse disabled under reduced motion (weight fixed 800), `save-data`, or `deviceMemory` ≤2 — the box remains, the shout becomes a standing bold | Identical |

**Breakpoints.** **≥1200px:** EXTRA at 44px, box in the front-page
choreography position (after the lead, before the section fronts).
**768–1199px:** EXTRA at 40px; the box spans the content width (it
never sits in a rail at this band — breaking news does not queue in a
column). **<768px:** EXTRA at 34px; the box stacks full-width above the
briefs, never as an overlay, sticky banner, or modal (§6.9); the pulse
timings are unchanged — a smaller shout at the same tempo.

**Edge cases & failure modes.** *No breaking story:* the box is absent
from the DOM — not hidden, not placeholdered (§9 item 10). *Variable
font fails / 'wght' axis subsetted away:* EXTRA renders at static 800
(§6.9) — the failure is detected by the absence of width change and
needs no code: a non-variable fallback face simply doesn't animate.
*Width growth at 900 (~6%):* the box reserves the 900-weight measure
(hidden twin at build, §6.9) — if that measurement is ever wrong
(custom font swap), the failure mode is a ≤6% reflow inside the box
only; the box's outer box never moves, because its padding absorbs the
twin's error. *Two items break simultaneously:* the desk edits — the
box carries the lead breaking item; the second files as the rail's
first brief with its own stamp. The theme never renders two EXTRA
boxes; that is an editorial rule enforced in the CMS template, stated
here so a builder doesn't "fix" it. *Slow network:* the box is
server-rendered with the page; a breaking item that arrives by push
after load enters with the half-travel feed and one stamp-in of its
stamp, prepended — never a silent reshuffle (§6.13's wire law applies
here too). *Low-power:* pulse off (see matrix), feed kept. *Scroll-up:*
the box re-pulses on re-entry within its window — the one ambient loop
in the theme allowed to resume, because its content's claim ("this is
breaking") is still true.

**Accessibility.** The pulsing word is text: "EXTRA" is read once by a
screen reader as part of the box's heading structure; the weight
animation is invisible to assistive tech and must never be the only
carrier of urgency — the box's kicker ("BREAKING — LATE WIRE") and its
position carry it. The box is a labelled region
(`aria-label="Breaking news"`) but is NOT a live region: a shouting
`aria-live` box that interrupts a screen-reader user mid-article is
the accessible equivalent of the popup this theme bans; new breaking
items are announced only on the home page's wire via a polite live
region on the *ticker prefix*, once, with the headline text. Contrast:
EXTRA in `--ink` on `--red-wash` ≈11:1 at every weight (weight changes
never change colour); the kicker's `--red-deep` on `--red-wash` ≈5.6:1
— AA for its 12px bold furniture role; headline `--ink` ≈11:1.
Touch target: the box's story link covers the headline + summary,
≥44px tall by construction.

**Tokens consumed.** `--red-wash`, `--press-red` (misregistered twin
rule), `--ink`, `--red-deep` (kicker), `--ease-sheet`, plus the
type-axis token `--wght-pulse: 400→900`. The freshness window is a
build-time constant (`--extra-fresh: 90min`), not a visual token.

### Element 10 — Proofing-underline hover + press-thud click (deepening)

**Choreography timeline** (two gestures; all times from the pointer or
key event):

*Underline (hover/focus):*
- **t = 0ms** — pointer enters: `scaleX` 0→1, origin left, 220ms
  `--dur-mark`, `--ease-proof`.
- **t = 220ms** — the mark is fully drawn; it holds while hovered.
- **Pointer leaves:** origin flips to right; scaleX 1→0 over 160ms —
  the pen leaves the way it came, slightly faster than it arrived.
- **Focus (keyboard):** no draw — the underline is present at full
  scaleX in the same frame as the focus outline (focus must never wait
  220ms to be visible).

*Thud (active):*
- **t = 0ms (pointerdown / keydown on a button-role element):** scale
  1→.98 and the 8% ink wash fades in, both 120ms `--dur-instant`,
  `--ease-press`.
- **Held:** the pressed state holds for as long as the press holds —
  there is no timed release.
- **Release:** scale .98→1 and wash out, 260ms `--ease-sheet`. If the
  press becomes a navigation, the release is cut by the transition
  (Element 12) — the sheet leaves mid-release, which reads as the
  press completing the print run.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | No underline; natural ink; links in body copy keep §2's static 1px ink underline at 30% offset (the drawn mark is *additional*) | Same rest |
| Hover | Underline draws (220ms); cards also lift per Element 15 | n/a — touch has no hover; any `:hover` styles must be gated behind `(hover: hover)` so a tap never leaves a stuck underline |
| Focus | Underline pre-drawn + 2px `--ink` outline, offset 3px — focus is always *more* visible than hover (§6.10) | Same on focus-visible |
| Active | Thud bottom state (scale .98 + wash) | Thud on tap — on touch this is the *primary* feedback for every tappable card and button (§6.10) |
| Scrolled-past | n/a as a scroll state — but visited links anywhere carry the pencil state: underline in `--smudge` when drawn, the read-mark (§6.10) | Identical |
| Disabled | No underline, no thud, ink at `--ink-faint`, genuinely inert (`disabled` / `aria-disabled` + handler removed) — a greyed control that still clicks is a misprint | Identical |

**Breakpoints.** **≥1200px / 768–1199px:** identical specs — feedback
does not shrink with the screen. **<768px:** hover terms drop out
entirely (no pointer), the thud remains at full spec, and every
tappable element's target is audited at ≥44px (§16) because the thud
is now the only confirmation a tap landed. Underline thickness: 2px on
headlines/links ≥16px, 1.5px `--red-deep` on body-size text links
(§6.10's contrast carve-out) at every breakpoint.

**Edge cases & failure modes.** *Pointer leaves mid-draw:* the retract
starts from the current scaleX (CSS transitions reverse from the live
value — no snap). *Rapid hover flicker across a card grid:* each card's
underline is independent; there is no shared debounce — a reader
skimming the pile sees marks flicker like a proofreader's pen, which
is correct behaviour, not a bug to smooth away. *Transitions disabled
(browser setting / reduced motion):* states still change — underline
appears/disappears instantly, thud becomes the 0ms colour step (§6.10);
no state is ever carried *only* by a transition. *No JS:* both gestures
are pure CSS (`:hover`, `:focus-visible`, `:active`) — they work in
the no-JS paper unchanged; only the card lift's JS stagger is absent.
*Low-power:* transform/opacity-class changes only; zero layout, zero
paint beyond the 2px mark — exempt from all cuts. *Scroll-up:* n/a.
*Content longer than the underline's element (a 3-line headline):* the
mark draws under the *block's* last line (the `::after` sits at the
block's foot) — underlining every line is a highlighter, not a proof
mark.

**Accessibility.** Focus visibility is this element's first duty: the
2px `--ink` outline at 3px offset holds ≈16:1 against both
`--newsprint` and `--newsprint-deep` grounds, and the pre-drawn
underline adds a second, redundant signal (colour is never the only
focus cue — the outline is shape, not hue). The underline's red
(`--press-red` ≈4.8:1, `--red-deep` ≈7.4:1 at body size) is a
non-text graphic reinforcing a state that hover/focus already
communicates by outline and (for links) by the static underline —
WCAG non-text contrast (3:1) is met by both reds. Disabled controls
use `--ink-faint` ≈8:1 — deliberately *above* the 4.5:1 floor that
disabled elements are exempt from, because a disabled "PRINT MY
SUBSCRIPTION" must still be readable as a promise, not a ghost. Touch
targets: ≥44px on every thudding element; the thud's scale (.98)
never shrinks the *hit* area, only the visual. Keyboard: buttons
activate on Space/Enter with the thud keyed to keydown/keyup, so the
press rhythm exists for keyboard users too.

**Tokens consumed.** `--press-red` (headline marks), `--red-deep`
(body-text marks), `--smudge` (visited marks), `--ink` (outline +
wash), `--ink-faint` (disabled), `--ease-proof`, `--ease-press`,
`--ease-sheet`, `--dur-mark` (220ms), `--dur-instant` (120ms).
Element-local: `--thud-scale: .98`, `--thud-wash: 8%`.

### Element 11 — Wet-sheet loading skeleton (deepening)

**Choreography timeline** (trigger: a client-fetched region begins
loading; t=0 is the fetch start):

- **t = 0ms** — the skeleton paints in the region's exact layout
  (masthead block / headline bars / column bars / photo beds per
  §6.11). No fade-in: the unprinted sheet is simply there, as paper is.
- **t = 0–2200ms, looping** — the sheen sweep: one diagonal
  `--ink-mist` gradient (5% → transparent) crosses the region,
  2200ms `--ease-proof`, then rests 0ms and sweeps again — one sweep
  per region, never per block.
- **t = 300ms** — minimum-display lock: even if content arrived at
  t = 40ms, ink-in does not begin before 300ms (a skeleton that
  flashes for one frame is worse than none, §6.11).
- **Content arrival (t = max(arrival, 300ms))** — ink-in: blocks print
  top-down in reading order, each block's real content replacing its
  skeleton bar with the conveyor at quarter travel (7px, 400ms
  `--ease-sheet`), stagger 70ms per block. A 6-block region finishes
  at arrival + 400 + 5×70 = arrival + 750ms.
- **t = 4000ms without content** — the sheen stops mid-state (the
  gradient parks off-region; a stopped press, not an eternal one) and
  the dateline slot prints "LATE WIRE — HOLDING FOR COPY" in
  `--smudge`. The skeleton remains, still, until content or failure.
- **Failure (fetch rejects):** the region prints the correction box
  (Element 16's error language) in place of the skeleton — the
  timeline ends in an admission, not a spinner.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (waiting) | Skeleton + sheen sweeping; `aria-busy="true"` on the region, skeleton itself `aria-hidden` | Identical |
| Hover | None — skeleton blocks are inert placeholders, never links, never thudding | n/a |
| Focus | Nothing inside a skeleton is focusable (no links exist yet); if the region held focus when it re-skeletonised (a rail refresh), focus moves to the region's heading — focus must never be dropped to `<body>` by a loading state | Same |
| Active | None | n/a |
| Scrolled-past | A region the reader has passed still inks in on arrival (silently, off-screen); its ink-in stagger does not run — off-screen blocks print instantly so the page above the fold is never re-laid-out by a rail finishing | Identical |
| Disabled | n/a — under reduced motion the skeleton is present without the sheen (still, dry paper); under no-JS the region shows the printed archive line instead (§6.11) | Identical |

**Breakpoints.** **≥1200px:** skeleton mirrors the full grid — column
bars at the real column count, hairlines between. **768–1199px:**
mirrors the 6-column grid; headline bars shorten to the band's real
measures. **<768px:** single-column bars; photo beds at 16:9; the
sheen still sweeps once per region — a small sheet is dampened the
same way. At every size the skeleton's geometry is generated from the
same layout classes as the content it precedes; a skeleton with its
own bespoke geometry is a second layout to maintain and is banned.

**Edge cases & failure modes.** *Content arrives in fragments (a rail
fetching page by page):* blocks ink in per fragment in reading order;
a later fragment never re-skeletons an inked block. *Content shorter
than the skeleton promised (2 stories against a 6-bar skeleton):* the
surplus bars are removed in the same frame as the ink-in completes —
the sheet is never left with phantom unprinted columns under real
copy. *Content longer:* the region grows by the surplus blocks
printing below with the same stagger; the growth is a layout shift
confined to the region, which is why regions are placed below the
reader's likely position (rails, archives) and never above the lead.
*Slow network:* the 4s sheen-stop and HOLDING line (above) are the
slow-network design, not an afterthought. *No canvas/WebGL:* n/a —
pure CSS. *Low-power:* the sheen is one gradient layer per region,
capped at 2 concurrent regions per viewport (§6.11); on the §16 floor
device the sheen is dropped entirely (dry skeleton) — the layout
information survives, the dampness doesn't ship. *Scroll-up into a
still-loading region:* it is simply there, skeleton and all; no
trigger depends on scroll direction. *SSR content:* skeletons never
appear — a server-rendered region prints immediately (§6.11).

**Accessibility.** `aria-hidden="true"` on all skeleton blocks +
`aria-busy="true"` on the region until inked, then `aria-busy` is
removed and, for regions whose arrival matters (search results), a
polite announcement "214 stories filed" in the paper's units (§13) —
never a per-block announcement. The HOLDING FOR COPY line is real
text, readable, at `--smudge` ≈5.9:1. The correction-box failure is
`role="alert"` only when the region was user-requested (a search, a
filter); background rails fail quietly into their correction box
without interrupting. No focusable elements exist inside a skeleton;
the sheen's motion is covered by the reduced-motion variant (no
sheen). Colour contrast of the bars themselves is structural
(`--newsprint-deep` on `--newsprint`), carrying no information.

**Tokens consumed.** `--newsprint-deep` (bars, beds), `--rule`
(hairlines), `--ink-mist` (sheen at 5%), `--smudge` (HOLDING line),
`--ease-proof` (sheen), `--ease-sheet` (ink-in), `--dur-sheet` (at
400ms ink-in variant). Element-local: `--sheen-period: 2200ms`,
`--skeleton-hold: 4000ms`.

### Element 12 — Fresh-sheet page transition (deepening)

**Choreography timeline** (trigger: an in-site navigation is committed
and the incoming route's critical content is ready or prefetched;
t=0 is the commit):

- **t = 0ms** — the outgoing sheet begins its whisk: translateY
  0→+100%, 380ms `--dur-page`, `--ease-press` (fast, final — a sheet
  leaving the pile does not linger).
- **t = 40ms** — the incoming sheet starts up from below: translateY
  +100%→0, 380ms `--ease-sheet`. Between t = 40ms and t = 380ms both
  sheets share the screen, separated by the 3px ink rule — the press
  bed's edge. The overlap window is 340ms; the visible "gap between
  sheets" is the middle ~200ms of it.
- **t = 420ms** — the incoming sheet has landed (40 + 380). Its
  masthead was pre-stamped (no stamp animation on a navigated-to page —
  the sheet comes off the pile already printed at the head).
- **t = 540ms** — 120ms after landing, the incoming hero's headline
  begins Element 1's strike timeline. Total commit→headline-struck for
  a 3-line hero: ≈ 540 + 450 ≈ 990ms, and the page was readable
  (masthead, deck furniture) from t = 420ms.
- **Back/forward:** the geometry reverses — the returning sheet comes
  down from the pile (translateY −100%→0, `--ease-sheet`), the current
  sheet drops away beneath it (`--ease-press`). Same 380/40ms
  structure; the pile is LIFO (§6.12).
- **Interrupt (a second navigation during the 380ms):** both sheets
  snap — no queue, no completion of the stale transition; the newest
  target's sheet lands within one frame of the new commit plus its own
  transition if armed. A press that cannot change editions mid-cycle
  is broken machinery (§6.12).

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (idle) | No layer; the current sheet is the page | Identical |
| Hover | n/a — the transition is not an element on the page | n/a |
| Focus | During transition, focus stays on the outgoing page's active element until landing; at t = 420ms focus moves to the incoming page's headline (or `main`) and the route change is announced — focus is never left on a translated-away sheet | Same (assistive nav follows the same landing rule) |
| Active | n/a | n/a |
| Scrolled-past | n/a — but scroll *restoration* is a designed case: returning to a page restores its scroll position and Element 5 starts at the true progress (§6.5); the transition does not reset the reader's place in the pile | Identical |
| Disabled | Transition not armed when: plain MPA navigation, `save-data`, effectiveType ≤3g, reduced motion, or the incoming route isn't ready — in every case navigation is native and instant | Identical |

**Breakpoints.** **≥1200px:** full spec, 380ms. **768–1199px:** full
spec, 380ms — sheets are vertical things; the metaphor survives.
**<768px:** duration shortens to 340ms (a smaller sheet whisks
faster); geometry unchanged. At no breakpoint does the transition
become a fade, a slide-from-right, or a scale — direction is meaning
(down = forward into the pile, up = the fresh sheet) and meaning does
not responsive-design away.

**Edge cases & failure modes.** *Incoming route slow despite prefetch:*
the transition does not arm — it never holds a readable page hostage
to an animation (§6.12); if navigation has already committed natively,
the new page simply opens with its masthead and strike. *Prefetch
wrong (user navigates elsewhere):* prefetched sheets are discarded
silently; no cost is visible. *Rapid double navigation:* the
interrupt rule (above). *Browser without View Transitions / router
support:* not armed; native navigation; each page still opens with its
own ceremony (Elements 13, 1). *No canvas/WebGL:* n/a — transforms on
the scroll containers. *Low-power:* on the §16 floor device the
transition disarms itself (two full-screen transforms for 380ms is
the single most expensive gesture in the theme) and navigation is
native — the theme spends its mobile motion budget inside pages, not
between them. *Scroll-up:* n/a (navigation, not scroll). *History
scroll restoration racing the transition:* restoration wins — the
incoming sheet is positioned at the restored offset *before* its
translate begins, so it lands already at the reader's place.

**Accessibility.** The route change is announced to assistive tech at
landing (a polite announcement of the new page's title — the
nameplate's job, in words); focus management per the matrix is
blocking: a transition that strands focus on a removed sheet fails
§10. The moving sheets are never the sole carrier of the navigation
event — the URL, title, and heading change are the real signals.
Under `prefers-reduced-motion` the preferred form is plain instant
navigation with no fade at all (§6.12); the 120ms crossfade exists
only for platforms that force a transition hook. Scroll restoration
and find-in-page are never hijacked beyond the visual layer.

**Tokens consumed.** `--ink` (the 3px bed-edge rule), `--ease-press`,
`--ease-sheet`, `--dur-page` (380ms; 340ms <768px). No colour surface
tokens — the sheets are the pages themselves.

### Element 13 — Masthead navigation & the Late Wire ticker (deepening)

**Choreography timeline** (two clocks: load and scroll):

*Load:*
- **t = 0ms** — the masthead paints in final state except the
  nameplate, which is armed.
- **t ≈ 60ms** (fonts ready or cap) — the nameplate stamps: scale
  1.04→1, blur 1.5px→0, 220ms `--ease-strike`.
- **t = 280ms** — nameplate settled; Element 1's trigger fires (the
  hero waits for the paper to announce itself, §6.13).
- **t = 300ms** — the ticker begins its crawl from a standing start
  (no ease-in — the wire moves at 60px/s from its first frame; a wire
  that accelerates feels like it's winding up).

*Scroll:*
- **Scroll passes 140px:** compression begins — Bands 1 and 3 collapse
  over 260ms `--ease-sheet` to the 52px bar (nameplate at 1.25rem
  left-aligned, section links, ink rule). The ink-line (Element 5) is
  the bar's bottom border throughout — it never leaves the screen
  while the reader reads.
- **Return to top:** expansion begins only above 100px (40px of
  hysteresis), same 260ms — the masthead never flutters at the
  boundary.
- **New wire item (push):** the item is prepended at the prefix block
  with Element 2's stamp-in (180ms) at the moment it joins; the track
  does not jump — the new item enters at the loop's seam, and the
  crawl continues at 60px/s through it.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest (top of page) | Three bands: nameplate row, section rule + nav, Late Wire | Nameplate centred; SECTIONS toggle closed; ticker running at 44px/s |
| Hover | Section links: proofing underline draws (Element 10); ticker pauses while hovered | n/a |
| Focus | Links: pre-drawn underline + ink outline; ticker pauses on focus-within (a keyboard reader can hold the wire still to read it) | Same on focus-visible |
| Active | Links thud; current section carries the *permanent* pre-drawn red underline (the "you are here" mark) | Links thud on tap |
| Scrolled-past | Compressed 52px bar (see timeline); the full masthead never re-appears mid-page | Compressed bar: nameplate-small + SECTIONS toggle + ink rule |
| Disabled | n/a — under reduced motion the ticker is a static 3-item list with a FULL WIRE link and compression swaps instantly; under no-JS the full masthead scrolls away and does not stick (the colophon carries the return link) | Same |

**Breakpoints.** **≥1200px:** full three bands; nameplate to 4.25rem;
ticker 60px/s; compression at 140px. **768–1199px:** nameplate clamps
to ~2.5rem; the weather-and-price slot keeps only the single live fact
(the second fact, if the build had two, is cut — furniture compresses
before type does); ticker at 52px/s. **<768px:** nameplate centred
(§4's one allowed centring), edition furniture moves to a line above
the nameplate, section links collapse behind the SECTIONS toggle —
which opens a full-width printed index (sections as a contents list
with dot leaders to their story counts, on `--newsprint`); ticker
remains at 44px/s because the wire matters more than the furniture
(§6.13). Compressed bar at this size: nameplate-small left, SECTIONS
right, ink rule under.

**Edge cases & failure modes.** *More sections than the rule fits
(9+ sections):* the nav does not shrink its type — sections beyond the
sixth move into the printed index (the SECTIONS list, at all widths);
a front page with nine shouting sections is a directory, not a paper.
*Wire empty (no items in the last edition window):* Band 3 does not
render; a ticker band crawling with nothing — or with filler — is
banned; the masthead is two bands that day. *Wire item very long (a
headline over ~140 characters):* it is edited for the wire (the wire
desk shortens headlines; the ticker never truncates mid-word with an
ellipsis fade — the item is rewritten, per §13's wire style). *Slow
network:* the masthead is server-rendered; the ticker's items are in
the initial HTML (the crawl is a transform on rendered content, never
a fetch-then-start). *Tab hidden:* the crawl pauses (rAF stops; the
track must not have advanced on return — pause is implemented by the
loop's own clock, so hidden time never accumulates). *Low-power:* the
crawl is one transform; on the §16 floor device the ticker still runs
(it is the paper's heartbeat) but compression becomes instant.
*Scroll-up:* expansion only inside the hysteresis band (above).

**Accessibility.** The masthead is a `<header>` with a `<nav
aria-label="Sections">`; the current section link carries
`aria-current="page"` — the red underline is the visual twin of a
programmatic fact, never the only carrier. The ticker: its items are
real links in a list in the DOM; the moving track is a duplicate
presentation — screen readers get the static list (the animated track
is `aria-hidden`, the accessible list is visually the same row when
motion is off, and is present-but-clipped when on; builders must ship
one list, duplicated per the standard marquee pattern, not two
diverging ones). Pause on focus-within and hover is an accessibility
feature, not a courtesy (§6.13). Contrast: nameplate `--ink` ≈16:1;
section links `--ink` ≈16:1, current-section underline `--press-red`
(non-text, duplicates `aria-current`); ticker text `--ink` on
`--newsprint-deep` ≈13:1, LATE WIRE prefix `--press-red` on
`--newsprint-deep` ≈4.3:1 at 11px bold — permitted as a label for a
region whose items are full-contrast, and it steps to `--red-deep`
(≈6.6:1 on the deep ground) in any build where the prefix is the only
label. Touch targets: section links ≥44px tall in the bar (padding,
not type size, provides it); the SECTIONS toggle is 44×44 minimum.

**Tokens consumed.** `--ink`, `--newsprint`, `--newsprint-deep`,
`--press-red`, `--red-deep`, `--smudge` (edition furniture),
`--ease-strike` (nameplate), `--ease-sheet` (compression),
`--ease-wire` (ticker — the theme's only linear motion). Element-local:
`--ticker-speed: 60px/s` (52 / 44 by band), `--masthead-bar: 52px`,
`--compress-at: 140px`.

### Element 14 — Box-score data table (deepening)

**Choreography timeline** (trigger: the table enters at 75% viewport
height):

- **t = 0ms** — row 1 files: conveyor at quarter travel (7px), 500ms
  `--ease-sheet`.
- **t = 40ms × n** — each subsequent row files at a 40ms stagger: a
  12-row table (the cap, §6.14) completes its filing at 500 + 11×40 =
  940ms.
- **Totals row:** files last, on the stagger (it is a row), but its
  counter — if the total is a rolling figure — starts its 1400ms
  `--dur-roll` only when the totals row has landed (t ≈ 940ms for a
  full table), landing on the true total at t ≈ 2340ms. A total that
  rolls before its row exists is a number from nowhere.
- **Sort (user-triggered):** the table re-prints — rows re-feed at
  eighth travel (4px, 300ms) in the new order with a 25ms stagger; no
  FLIP, no crossfade (§6.14). The sorted column's head gains its 2px
  ink underline at the first re-fed row's landing.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed table; totals ink-bold; zebra at 50% `--newsprint-deep` | Identical, inside its horizontal-scroll well |
| Hover | On a sortable head: proofing underline under the column name + the Franklin ▲/▼ mark appears | n/a — sortable heads show their mark persistently on touch (a control that only reveals itself on hover does not exist on touch) |
| Focus | Sort button in the head: pre-drawn underline + ink outline; the table itself is not focusable, its scroll well is (keyboard scrollable, labelled) | Same |
| Active | Sort button thuds; the re-print begins on release | Thud on tap |
| Scrolled-past | Filed and static; counters hold their true totals (they rolled once, on entry) | Identical |
| Disabled | n/a — an empty table is not disabled, it prints "NO RETURNS FILED" (§6.14); a table whose data failed prints the correction line in its body area | Identical |

**Breakpoints.** **≥1200px:** full table, up to 12 rows before the
archive cut. **768–1199px:** columns compress by dropping the
lowest-priority data column into the archive version (the table's
columns carry a priority order in the build spec — the front page
prints the leaders, §6.14); type sizes never shrink. **<768px:** the
box score scrolls horizontally inside its well, first column sticky,
24px `--newsprint` fade mask at the scroll edge; it never reflows
into stacked cards (comparability is the entire point, §6.14). The
well's scroll shadows/mask are the only hint of more table — plus the
caption line "FULL TABLE IN THE ARCHIVE" under the well at this size.

**Edge cases & failure modes.** *More rows than the cap:* 12 visible +
the archive cut line — the cut is editorial (the leaders print), not
a "show more" accordion. *A figure that is not yet known (returns
still coming in):* the cell prints an em dash in `--smudge` — never
0, never a guessed figure (the truth audit, §10 item 4, covers
tables). *A total that disagrees with its rows (source data error):*
the table prints the rows and the source's total with a correction
footnote under the table in the corrections voice (§13) — the paper
does not silently fix figures. *Very wide table (10+ columns):* even
on desktop it goes into the scroll well; a box score squeezed to fit
is a box score lying about its figures' sizes. *Slow network:* tables
are server-rendered content; a client-fetched table (live results)
uses Element 11's skeleton in the table's own ruled geometry. *No
canvas/WebGL:* n/a — a real `<table>`. *Low-power:* row filing is
transform-only and capped at 12 rows; exempt from cuts beyond
dropping the stagger (rows file together, 300ms, on the floor
device). *Scroll-up:* filed is filed; no re-filing.

**Accessibility.** A real `<table>` with `<th scope="col">` and a
`<caption>` that carries the kicker's text ("Box score — circulation
by edition") — the caption is the accessible name, the visible kicker
is its twin. Sortable heads use real `<button>`s with `aria-sort` on
the `<th>`; the ▲/▼ marks are `aria-hidden` decoration on a labelled
button ("Sort by circulation, descending"). Figures are text
(tabular-nums), never images. Contrast: head text `--ink` on
`--newsprint-deep` ≈13:1; body figures `--ink` ≈16:1; row labels
Newsreader `--ink-soft` ≥12:1; the em-dash unknown marker `--smudge`
≈5.9:1. The horizontal-scroll well on mobile is focusable with
`tabindex="0"` and an accessible label ("Box score, scrollable") so
keyboard and switch users can pan it. Touch targets: sort buttons
≥44px (the head row's padding provides it).

**Tokens consumed.** `--ink`, `--ink-soft`, `--newsprint-deep`
(head band + zebra), `--rule` (row hairlines), `--press-red` (the
totals rule, only when the total is the story), `--ease-sheet`,
`--dur-roll` (1400ms). Type: Headline 4 (heads), Data/counter role
(figures), Body small (row labels).

### Element 15 — Story cards (the brief block) (deepening)

**Choreography timeline** (trigger: the card's grid batch enters —
Element 3's observer on the grid, cards staggered within the batch):

- **t = 0ms** — the batch's first card feeds (Element 3 at card scale:
  travel 18px, drift ±1.5px — a cutting is a small sheet, its
  registration error is proportionally smaller), 700ms `--ease-sheet`.
- **t = 70ms × position** — cards in a row feed left→right at 70ms
  offsets, as if laid down by a hand across the pile (§6.15); the next
  row's batch triggers on its own entry, not on the first row's clock.
  Batches cap at 8 cards (§6.15).
- **Hover (pointer-fine):** lift — translateY −3px, 200ms
  `--ease-sheet`, the hard shadow (3px offset, 0 blur, `--ink` 100%)
  appears with the lift (it is the sheet's edge: it must not fade in
  separately or the card looks like it's glowing from behind). The
  headline's underline draws concurrently (220ms, Element 10).
- **Unhover:** lift and shadow release over 200ms; the underline
  retracts per Element 10 (160ms, origin right).
- **Click/tap:** thud (120ms down) — then either navigation (Element
  12, if armed) or the browser's plain departure.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat on the pile: hairline top, kicker + red mini-rule, headline, ≤2-line deck, furniture footer (stamp left, inches right) | Identical |
| Hover | Lifted −3px + hard shadow; headline underlined | n/a — gated behind `(hover: hover)`; a tap never leaves a card lifted |
| Focus | Lift + underline pre-drawn + 2px ink outline offset 3px (the stretched link's focus is shown on the card, not on the headline text alone) | Same on focus-visible |
| Active | Whole-card thud (scale .98 + wash) | Thud on tap — the card's only press feedback |
| Scrolled-past | Fed and flat; feeds never re-run on scroll-up | Identical |
| Disabled | n/a for editorial cards; the *sponsored* variant is a designed extra state: dashed `--smudge` border + "ADVERTISEMENT — NOT FROM THE NEWSROOM" head, no lift (an ad does not get the paper's own lift — it sits *on* the pile, not in it), thud retained if it links | Identical |
| Read (visited, extra state) | Stamp turns `--smudge`; headline ink softens to `--ink-soft` — the cutting looks read (§6.15) | Identical |

**Breakpoints.** **≥1200px:** 3-column briefs grid (per §7's listing
map), photo wells full-bleed to the card's top edge. **768–1199px:**
2 columns; the deck may clamp to 2 lines still (never 3 — a cutting
is cut); photo wells at 3:2. **<768px:** single column, full-width
cuttings; photo wells at 16:9; no lift (no hover); the furniture
footer keeps both items (stamp + inches) — on a 320px card they stack
(stamp line, inches line) rather than either being dropped, because
both are records.

**Edge cases & failure modes.** *Headline longer than the card's
measure:* the headline wraps to its size class's line cap (Headline 4:
3 lines; Headline 3: 2) and is then *edited*, not ellipsised mid-word
— the deck clamps hard (§6.15) but headlines are copy, and copy is
fixed by editors. A build that ships a card with a clipped headline
fails review. *Deck missing (a story with no standfirst):* the card
prints kicker, headline, footer — the space the deck would take
collapses; cards in a row do not stretch to equal height to fake
symmetry (a pile of cuttings is uneven; the grid aligns tops, not
bottoms). *Photo missing:* the card is a text cutting — no empty well,
no placeholder block. *Very many cards (archive rails):* batching
caps animation at 8 per batch; beyond the first two batches, cards
print without feeding as they enter (the pile is deep; the hand does
not lay down the hundredth cutting with ceremony) — they are simply
present, which is never a failure state in this theme. *Slow network:*
cards are server-rendered in listings; client-fetched rails use
Element 11. *Low-power:* the hard shadow is the cheapest shadow that
exists (0 blur); the lift is one transform — cards are exempt from
cuts except the entrance drift (dropped on the floor device, per
Element 3). *Scroll-up:* flat, printed, visited-state intact.

**Accessibility.** One link per card: the headline's anchor stretched
over the card — the card never contains two links to the same story,
and any *second* action (a section link in the kicker) is outside the
stretched area or the card is not one link (choose per build, never
both patterns on one page). The stretched link's accessible name is
the headline; the deck and furniture are readable text in the card,
not part of the link name (a screen reader user browsing links hears
headlines, not paragraphs). Focus outline per the matrix. Contrast:
headline `--ink` ≈16:1 (visited: `--ink-soft` ≥12:1 — a read cutting
stays comfortably readable; visited styling is ink-softening, never
greying into illegibility); deck `--ink` at Body small; furniture
`--smudge` ≈5.9:1; the sponsored head is `--ink-faint` ≈8:1 at 10px
bold — deliberately *above* AA so the disclosure is never the least
readable thing on the card. Touch target: the whole card (≥44px in
both dimensions by construction).

**Tokens consumed.** `--ink`, `--ink-soft`, `--smudge`,
`--newsprint`, `--newsprint-deep` (the pile gaps), `--rule` (card
hairline), `--press-red` (mini-rule), `--ease-sheet`, `--ease-proof`
(underline via Element 10), `--dur-mark`. Element-local:
`--card-lift: -3px`, `--card-shadow: 3px`.

### Element 16 — The clip-coupon form (deepening)

**Choreography timeline** (three timelines: entrance, field, submit):

*Entrance:* the coupon feeds as an ordinary section (Element 3, full
spec) — the scissors never snip (§6.16).

*Field focus:*
- **t = 0ms** — focus enters a field: its bottom rule inks
  (`--newsprint-edge` 1px → `--ink` 2px) over 180ms `--ease-proof`,
  and the label steps `--smudge`→`--ink` with weight 600→700 in the
  same 180ms — the line darkens as a pen presses.
- **Blur with valid content:** the red proof tick (✓, Franklin) stamps
  at the line's right end — Element 2's stamp-in at miniature scale
  (120ms, scale 1.3→1, no rotation — a tick is a mark, not a stamp).
- **Blur with invalid content:** the field's rule turns `--red-deep`
  and holds; the correction box for that field feeds in above it at
  quarter travel (7px, 400ms) — one box per field, printed on blur,
  not on submit (the paper corrects as it reads).

*Submit:*
- **t = 0ms** — the button thuds (120ms down, Element 10) and holds;
  its label swaps to "AT THE PRESS…".
- **Client validation pass:** if any field fails, there is no tear:
  the first failing field's correction box prints (or is scrolled
  to), focus moves to it, and the button releases (260ms). The coupon
  is never torn for a form that didn't go.
- **t = +150ms (valid, submitting)** — the tear begins: the coupon
  block translates down 6px while its dashed border is replaced by
  the torn-edge SVG mask (teeth 2px, irregular), 300ms `--ease-press`.
  The coupon does not slide away or vanish — it is *torn off and
  kept*: it stays on the page, torn, as the reader's copy.
- **t = +450ms** — the receipt prints in the space the form's
  choreography reserved: "RECEIVED AT THE OFFICE — {real time}, No.
  {real reference}" with the office stamp-in (Element 2's 180ms spec)
  at its head. Server failure at this point: no tear has happened
  (the tear waits for the server's acceptance — the timeline above
  is the *success* path; on failure the button releases, a correction
  box prints at the coupon's head: "THE OFFICE COULD NOT TAKE THIS —
  {plain reason}. YOUR WORDS ARE STILL IN THE COUPON." and every
  field keeps its content).

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | Un-clipped coupon: dashed `--smudge` border, scissors mark on the top border, ruled empty fields | Identical |
| Hover | The submit button takes Element 10's underline on its label? No — the submit is a solid ink block; hover steps its ground from `--ink` to `--ink-soft` (a lighter press of the same ink) and the cursor is the pointer. Fields: no hover state (a line on paper does not react to a hovering pen) | n/a |
| Focus | Field: inked rule + darkened label (timeline above). Button: 2px ink outline offset 3px on the ink block (a white-offset ring reads wrong on an ink ground — the outline sits outside on the paper) | Same on focus-visible; tapping a field is focus |
| Active | Button thud (held while submitting) | Thud on tap |
| Scrolled-past | n/a — but a coupon returned to after an abandoned submit keeps its filled fields and any printed corrections; the paper does not clear a half-written coupon because the reader scrolled | Identical |
| Disabled | The submit disables only while a submission is in flight: label "AT THE PRESS…", ink at full strength (not greyed — it is *working*, not unavailable), `disabled` set so it cannot double-post. A form whose edition is closed (past the subscription deadline) prints the coupon struck through with one ink rule and the line "THIS COUPON HAS EXPIRED — WRITE TO THE DESK INSTEAD" with a working link | Identical |

**Breakpoints.** **≥1200px:** coupon at its one-column measure, max
560px, placed at choreography station 7 (§4). **768–1199px:** same
560px cap — a coupon does not widen because the desk is bigger.
**<768px:** full column width; fields stack (they already do); input
text stays ≥16px (iOS auto-zoom ban, §6.16); the scissors mark stays
on the top border at the left — at 320px it sits above the kicker's
first word, never overlapping it (the border's padding grows by 6px
at this band to keep the mark clear of type).

**Edge cases & failure modes.** *Slow network on submit:* the button
holds at "AT THE PRESS…" — there is no timeout theatre before 10s;
at 10s the button releases and the correction box prints "THE WIRE
TO THE OFFICE IS SLOW — YOUR COUPON IS STILL HERE. PRESS AGAIN."
with all content intact. A submission is never silently retried.
*Double submit (double-click, Enter mash):* the `disabled` in-flight
state + a client token make the second press a no-op; the server
deduplicates on the token — the receipt's reference number is the
proof. *No JS:* native submit to the server action; the server
returns a receipt *page* in the same office-stamp styling (§6.16);
validation errors return the coupon page with correction boxes
printed server-side — the no-JS form is a full citizen, not a
fallback apology. *Autofill:* filled fields show their proof ticks
only after a blur or on submit — autofill must not stamp ticks for
values the reader hasn't seen; the ticks appear when the coupon is
submitted or the field is visited. *Very long input (a tip field
with 5,000 words pasted):* textareas grow to a cap (12 rows) then
scroll internally; the coupon's border grows with it — a coupon
that clips a reader's words is a torn form, banned. *Low-power:*
the tear is one transform + a mask swap; exempt from cuts.
*Scroll-up:* n/a.

**Accessibility.** Real `<label>`s (the visible Franklin labels ARE
the labels, programmatically associated — not placeholders-as-labels,
which are banned outright). Errors: each correction box is tied to
its field with `aria-describedby`, the field carries
`aria-invalid="true"` while its rule is red, and on submit-failure
focus moves to the first error and the box is announced via
`role="alert"` (once — the per-field blur boxes are not live
regions). The receipt is a heading + text that receives focus on
success (`tabindex="-1"`), so a screen-reader user is *taken* to
their receipt, not left at a vanished form. Contrast: label
`--smudge` ≈5.9:1 at rest → `--ink` ≈16:1 on focus; input text
Newsreader 17px `--ink` ≈16:1; correction text `--red-deep` on
`--red-wash` ≈5.9:1 (AA at its 13px bold size, and the box also has
the field's red rule + position as redundant signals); the proof
tick `--press-red` is decorative reinforcement of validity that is
also conveyed by the absence of a correction box — never the sole
signal. Touch targets: fields are full-width rows ≥48px tall
(label + line); the submit is full-width, ≥52px.

**Tokens consumed.** `--smudge` (cut line, labels at rest), `--ink`
(inked rules, labels on focus, submit ground), `--ink-soft` (submit
hover), `--newsprint-edge` (field rules at rest), `--press-red`
(proof ticks, required asterisks), `--red-deep` (error rules, error
text), `--red-wash` (correction ground), `--ease-proof`,
`--ease-press`, `--ease-sheet`. Element-local: `--coupon-measure:
560px`, `--tear: 300ms`.

### Element 17 — Colophon footer (deepening)

**Choreography timeline** (trigger: the colophon's closing line
enters the viewport):

- **t = 0ms** — nothing. The colophon deliberately does not feed,
  draw, or lift on entry: the paper is finished, and a footer that
  performs is apologising for the page above it (§6.17).
- **The one beat:** when the closing line itself ("— END OF EDITION
  No. {n} — STOP PRESS —") crosses 90% of viewport height, "STOP
  PRESS" stamps in once — Element 2's timeline exactly (180ms,
  scale 1.35→1, rotate →−1.2° on the words only, set as an inline
  stamp span). It is the last thing the press does on the page, and
  it happens at the moment the reader reaches the end — timed to
  arrival, not to load, so a reader who never scrolls down never
  triggers it.
- **Edition change while the page is open:** the colophon's edition
  number and closing time do NOT update live (an open page is a
  printed sheet of its edition); the change appears on the next
  navigation. The masthead's stamp (Element 2) is the live one; the
  colophon is the record.

**State matrix:**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed on `--newsprint-deep` under the double rule; four columns | Stacked single column: imprint → sections → desk → record |
| Hover | Links take the proofing underline (Element 10) | n/a |
| Focus | Underline pre-drawn + ink outline, per Element 10 | Same on focus-visible |
| Active | Links thud (text links: the ink-darken step only, no scale — small print does not bounce) | Same on tap |
| Scrolled-past | n/a — the colophon is the end; there is no past it | n/a |
| Disabled | n/a — nothing in the colophon can be disabled; a dead route is removed from the index, never greyed (a colophon listing a section that no longer exists is a false record) | n/a |

**Breakpoints.** **≥1200px:** four columns as §6.17. **768–1199px:**
two columns (imprint + sections; desk + record), dot leaders intact.
**<768px:** the stack in the paper's priority order (imprint →
sections → desk → record); the closing line stays centred (its one
allowed place, §4); dot leaders survive — at 320px the leader shrinks
to a minimum of 8 dots before the count right-aligns on the next
line, rather than the count being dropped.

**Edge cases & failure modes.** *Archived edition:* the colophon is
frozen at that edition's values — number, closing time, even the
staff list as it stood (§6.17); a build that renders tonight's
colophon on last month's archive page fails the truth audit.
*Publisher details change (a move, a new printer):* the imprint is
data, not template text — it updates from the publication's record
everywhere at once, including future renders of archived editions'
*imprint* (the imprint is who prints; the edition data is what was
printed — the two are kept separate precisely so this case works).
*Slow network / no JS:* the colophon is static HTML; the STOP PRESS
stamp is its only JS-adjacent flourish and its absence changes
nothing (§6.17). *No canvas/WebGL:* n/a. *Low-power:* zero-cost
element; exempt. *Very long sections index (a paper with 14
sections):* the index column wraps into two ruled sub-columns
rather than shrinking type or truncating with a "more" link — the
record is complete or the section list is redesigned editorially.
*Scroll-up:* the stamp does not re-stamp; printed is printed.

**Accessibility.** The colophon is a `<footer>` (contentinfo) with
labelled nav regions ("Sections", "The desk", "The record") so
assistive users can navigate the record as structure. The closing
line's stamp span is decorative motion on real text — the words are
in the accessibility tree in order. Contrast on `--newsprint-deep`:
imprint body Newsreader 13px in `--ink-soft` ≥11:1; small print in
`--ink-faint` ≈7:1 on the deep ground (recomputed for the deeper
ground — the §2 figure of 8:1 is against `--newsprint`; on
`--newsprint-deep` it holds ≈7:1, still AA); dot leaders are
decorative (`aria-hidden` — the counts are text). The "RETURN TO THE
FRONT PAGE" link is ≥44px tall with its padding. Nothing in the
colophon is the sole location of a legally required route: privacy
and terms also live in the record column of every office page's
shortened colophon (§7).

**Tokens consumed.** `--newsprint-deep` (ground), `--ink`,
`--ink-soft`, `--ink-faint`, `--rule`, `--press-red` (STOP PRESS
stamp), `--ease-strike` (via Element 2's stamp spec). No duration
tokens of its own — stillness is the spec.

---

## 12. Component inventory — every component, in the paper's clothes

Part I specified the elements a front page is made of. A real site
needs more furniture than a front page shows. Every component below
gets its Midnight Press Run treatment; a component that cannot be
given one honestly is refused, and the refusal is part of the spec.

- **Primary button.** A solid ink block: `--ink` ground, `--newsprint`
  text, Franklin 13px 700 uppercase +0.14em, 0 radius, padding 14px
  22px (≥48px tall). Label is a trade verb (§13): "PRINT MY
  SUBSCRIPTION", "FILE YOUR STORY". Hover: ground steps to
  `--ink-soft`. Active: thud. Focus: 2px ink outline offset 3px on
  the paper around the block. Disabled: `--ink-faint` ground, text
  still `--newsprint`, genuinely inert.
- **Secondary button.** The same block un-inked: 1.5px `--ink` border,
  ink text on paper. It is the coupon you didn't clip yet. Never a
  grey button — grey is not a rank in this paper; ink or outline are.
- **Text button / link-button.** A Franklin label with the proofing
  underline as its resting state at 40% (drawn, `--smudge`) and full
  `--press-red` draw on hover. Used for "READ THE FULL WIRE", "MORE
  FROM THE ARCHIVE".
- **Text input.** Element 16's ruled field, everywhere: bottom rule
  only, Newsreader 17px, label above in Franklin 11px. No boxes, no
  filled backgrounds, no floating labels — a floating label is a
  sheet that won't lie flat.
- **Textarea.** The ruled field grown: ruled *lines* every 28px
  (repeating-linear-gradient of `--newsprint-edge`) so writing sits
  on the paper's lines like a letter. For tips and letters to the
  editor.
- **Select.** A ruled field whose closed state shows the value in
  Newsreader with a Franklin "▾" set in type (never an icon font).
  The open list is a printed slip: `--newsprint` panel, 1px
  `--newsprint-edge` border, hard 3px shadow, options as ruled rows,
  the chosen one carrying a red proof tick. Native `<select>` styled
  is preferred wherever the platform allows; a custom listbox must
  meet the native one's keyboard behaviour or not ship.
- **Checkbox.** A small empty box ruled in ink (14px, 1.5px border);
  checked, it receives a red proof tick drawn in (stroke draw, 160ms
  `--ease-proof`) — the editor has marked the choice. The box is the
  target's visible part; the target is the full label row, ≥44px.
- **Radio.** A ruled circle; chosen, it fills with an ink dot that
  stamps in (120ms). A radio group is set as a list of ruled rows —
  "editions" of a choice.
- **Toggle / switch.** Refused as a switch. A binary choice in this
  paper is a checkbox with a proof tick, or it is an *edition
  choice*: two Franklin labels with the current one underlined in
  red ("DAY SHEET / NIGHT DESK" for the theme-mode control — the one
  place a segmented control exists, styled as two masthead labels
  sharing a rule).
- **Badge / tag.** Badges are edition furniture, never pills: a
  Franklin 10px uppercase label with a 1px ink border ("No. 214",
  "LATE WIRE", "CORRECTED"). The CORRECTED badge is the only red-
  bordered one. Tags on stories are the kicker system (§3), not a
  separate chip component — pill chips are banned (§7).
- **Alert.** The correction box (Element 16): `--red-wash` ground,
  `--red-deep` Franklin text, headed "CORRECTION —" or "STOP PRESS —"
  for the informational kind (ink-headed, paper ground, red rule).
  Alerts are *printed in place* in the flow; they never float, never
  overlay, never auto-dismiss — a correction does not un-print
  itself.
- **Toast.** Refused as a floating toast. The theme's equivalent is
  the **wire flash**: a one-line slip that prints at the foot of the
  current section ("FILED — YOUR LETTER IS WITH THE DESK"), in the
  flow, where it stays as part of the page's record. If an action's
  confirmation matters, it gets a receipt (Element 16), not a toast.
- **Modal / dialog.** Restricted to reader-initiated, functional
  dialogs only (confirming a subscription change, an edition-switch
  with consequences) — never timed, never promotional (§9 item 8 is
  absolute: no popup may sell anything in this theme). Treatment: a
  **late slip** — a `--newsprint` sheet pasted over a dimmed page
  (dim = `--ink` at 45%), hard 4px shadow, double rule at its head,
  its headline struck at Headline 4 scale, actions as ink blocks.
  It enters with a half-travel feed (12px, 300ms), focus is trapped
  inside it, Esc closes it, and focus returns to the invoking
  element. Under reduced motion it simply appears.
- **Tabs.** Section fronts within a page are set as an **index row**:
  Franklin labels along a rule, the active one carrying the red
  proofing underline pre-drawn and a 2px ink underline beneath the
  rule — two marks, because a tab is both a place and a choice.
  Panels change by re-printing (eighth-travel re-feed, 300ms, per
  Element 14's sort) — never by crossfade.
- **Accordion.** A **folded page**: each item is a section of the
  sheet with a hairline at its fold; opening unfolds it — the panel
  expands with `--ease-sheet` 350ms while a red mini-rule draws at
  the fold. The control is a real `<button>` with `aria-expanded`;
  the closed state shows the item's headline and its first line —
  a fold hides the continuation, never the existence.
- **Pagination.** Folio furniture (§7): "PAGE 2 OF 6 — CONTINUED IN
  THE ARCHIVE", numbers as Franklin folios, the current page in an
  ink box, prev/next as "← EARLIER SHEETS" / "LATER SHEETS →" with
  the arrows set in type. No infinite scroll anywhere in the theme.
- **Table.** Element 14, the box score — the only table treatment.
- **Chart.** Re-inked or refused: greyscale series + one red series,
  Franklin axis labels, hairline gridlines in `--rule`, set inside a
  clipping frame (§7) if the data is foreign. A chart library's
  default colours, gradients, or rounded bars may never reach the
  page; bars are square, lines are 2px, areas are unfilled or
  `--ink-mist` at 6%.
- **Tooltip.** A **margin gloss**: on hover/focus of a marked term, a
  small note prints in the margin beside it (desktop) or as a slip
  under the paragraph (mobile) — Newsreader italic 13px in
  `--smudge`, with a hairline pointing to the term. Never a dark
  bubble; the gloss is part of the page's apparatus, like a
  footnote that comes to you.
- **Breadcrumb.** A folio trail: "FRONT PAGE / MONSOON / THE LOWER
  CITY" in Franklin 11px with hairline separators — it appears on
  article pages only, above the kicker. On the front page it would
  be furniture about furniture.
- **Avatar / byline portrait.** Portraits print as photographs do:
  a small square halftone well (Element 7's screen at rest, no
  shimmer at this size), never a circle crop — newspapers do not
  print round photographs.
- **Search field.** "SEARCH THE ARCHIVE": a ruled field in the
  masthead's index (mobile) or a dedicated archive page (desktop),
  with results per §7's folio index. The search submit reads
  "SEARCH" — the one place a plain verb survives, because the
  archive's name is already on it.
- **File upload (tip with a clipping).** A dashed cut-line drop area
  inside the tip coupon: "ATTACH A CLIPPING — DROP IT ON THE COUPON,
  OR BROWSE THE DESK DRAWER". Attached files list as ruled rows
  with name, size in Franklin figures, and a red ✗ (set in type) to
  remove. Progress of an upload is the ink-line at miniature scale
  under the row — the theme has one progress language, and it is
  this.
- **Divider.** The theme's rules are its dividers: hairline
  (`--rule`, between furniture), single ink rule (between stories),
  double rule (3px over 1px, between sections), red drawn rule
  (section heads). There is no fifth divider and no divider with a
  centred ornament — the fleuron is banned; a rule is enough.
- **Skeleton / spinner.** Element 11 is the only loading treatment.
  Spinners do not exist in this theme, in any component, ever.

## 13. Content & copywriting voice — the paper's house style

The theme's visuals fail if the words are written like an app's. The
house style is a newspaper's: terse, factual, in the trade's own
vocabulary, and never cute.

**Headline style.** Past tense, active voice, the concrete fact
first, place and time where they matter. Headlines are written to
the measure (§3) — the copy desk shortens them, the browser never
does.

- ✓ "THE RIVER TOOK THE LOWER CITY AT 2 A.M."
- ✓ "COUNCIL VOTES 6–3 TO CLOSE THE NIGHT BUSES"
- ✗ "You Won't Believe What Happened to the Lower City Last Night"
- ✗ "Everything You Need to Know About the Flood" ("everything" is a
  promise no edition can keep)

**Deck style.** One sentence, sentence case, Newsreader — the facts
the headline had no room for, in the order a reader needs them. No
deck repeats the headline's words in a new order.

**Labels & furniture.** Uppercase Franklin, the trade's nouns:
EDITION, WIRE, ARCHIVE, THE DESK, FOLIO, RETURNS, BOX SCORE. A label
that could sit on any SaaS dashboard ("Dashboard", "Settings",
"Notifications") is rewritten into the paper's world or the feature
is reconsidered: "THE DESK" for account, "WIRE FEED" for RSS,
"FILED STORIES" for bookmarks.

**Buttons.** Trade verbs, first person where the reader acts:
"PRINT MY SUBSCRIPTION", "FILE YOUR STORY", "SEARCH THE ARCHIVE",
"WRITE TO THE DESK". Banned: "Submit", "Click here", "Get started",
"Learn more" (learn more *about what*? — the button names its
destination or it is not finished).

**Error voice — the corrections column.** An error is a correction
the paper prints about itself: headed "CORRECTION —", plain words,
the fix stated, no blame and no jokes.

- ✓ "CORRECTION — THE OFFICE COULD NOT TAKE THIS COUPON. THE EMAIL
  LINE IS MISSING ITS @. YOUR OTHER LINES ARE STILL WRITTEN."
- ✓ "CORRECTION — THAT PAGE WAS NOT IN THIS EDITION." (the 404,
  §7)
- ✗ "Oops! Something went wrong 🤷" — the paper does not shrug, and
  it does not emoji. Ever.

**Empty-state voice.** An empty place says what is true, in units:

- ✓ "NO RETURNS FILED" (empty table) · "THE WIRE IS QUIET" (empty
  ticker — which then doesn't render, §11.13) · "NOTHING FILED UNDER
  'MONSOON' YET — THE DESK IS WATCHING THE SKY." (empty search)
- ✗ "No results found." with a cartoon magnifier. There are no
  cartoon anythings in this paper.

**Success voice.** Receipts, not celebrations: "RECEIVED AT THE
OFFICE — 02:14, No. 214." No confetti exists to describe. A success
that needs more than a receipt gets a story card ("YOUR FIRST
EDITION ARRIVES TONIGHT", §7).

**Loading voice.** "HOLDING FOR COPY" (Element 11). "AT THE PRESS…"
(submitting). Never "Loading…" with an ellipsis doing the work of a
personality.

**Numbers & units.** Column inches for reading, folios for pages,
edition numbers for versions, real clock times for stamps. "3 min
read" is banned (§9 item 8) — the paper measures in inches because
its readers can see an inch of type. Figures are Franklin tabular
(§3) in copy as in counters.

**The voice test.** Read any string aloud in a newsroom voice. If it
sounds like a notification from a phone, rewrite it. If it sounds
like something a sub-editor would say at 2 a.m. without smiling, it
is house style.

---

## 14. Three worked examples — with scroll timelines

§8 built the front-page hero end to end on the *load* clock. These
three examples are the v2 complement: the same rigour on the *scroll*
clock — what happens, in order, as the reader's hand moves. Timings
cite Part I/II element specs; nothing here introduces a new number.

### Example A — The hero, on the scroll clock (home, desktop 1440×900)

The monsoon front page of §8, from the moment the reader first
scrolls. Load choreography is §8's; this is what follows it.

| Scroll position | Beat | What the visitor sees & feels |
|---|---|---|
| 0–140px | Masthead full; ink-line at 0; cylinder at 0deg | The whole ceremony is present; the paper has announced itself |
| 140px | Masthead compresses (260ms) to the 52px bar; ink-line stays as its bottom border | The ceremony folds away; the *instrument* stays — reading has begun |
| ~300px (pin stage top at bar) | Lead sticks at top: 96px; photo scrub live at scale ≈1.08 | The front page holds its ground — it is finished, printed |
| 300px–120vh of travel | Briefs 1–5 feed past at 85% entry (700ms each); photo scrubs 1.08→1; cylinder turns through ≈1 turn (page-progress share); ink-line caption steps "12 → 18 → 24 COLUMN INCHES" | Later news keeps arriving beside the fixed lead; the reader feels the desk working |
| Travel ≈ 65vh | Photo passes 1.04; brief 3 feeds | The two rhythms cross — the photo is half-settled exactly as the rail is half-read |
| Travel 120vh | Lead un-sticks; first section front's head crosses 82% | No dead frame: the hand-off beat |
| +150ms after the rule (850ms mark) | The section feeds (Element 3) under its fresh red rule | The run continues onto the next sheet |

*Reduced-motion version:* no pin, no scrub, no compression glide —
lead and briefs stack, the bar swaps instantly at 140px, the
ink-line steps in 10% increments. *Failure version (JS off):* the
§8 static front page; the scroll clock has no beats at all, and
nothing is missing that a reader could name.

### Example B — A mid-page section: "THE SCOREBOARD" section front with its box score

The page: home, the data station of §4's choreography — a section
front carrying a circulation box score (Element 14) above three
story cards (Element 15). The reader arrives from the pinned stage
above.

| Scroll position | Beat | What the visitor sees & feels |
|---|---|---|
| Section head crosses 82% vh | t=0: kicker "THE SCOREBOARD" strikes (180ms) | The editor names the section |
| +100ms | The red rule begins its draw (600ms, `--ease-proof`) | The mark is made across the section's top |
| +700ms | Rule complete; dasharray shed | A drawn line, now just a rule |
| +850ms | The section feeds (Element 3, 900ms): the table block and the cards' first row travel up 26px, drift ±2.5px, register to 0 at +1750ms | The sheet arrives and settles true |
| Table top crosses 75% vh (during the feed, ≈ +1100ms) | Box-score rows begin filing: row 1 at quarter travel (500ms), 40ms stagger; 9 data rows + totals filed by ≈ +1100 + 500 + 9×40 ≈ +1960ms | The figures are filed row by row, like returns coming in |
| Totals row lands (≈ +1960ms) | The circulation total begins its roll: 1400ms `--dur-roll`, tabular figures, landing exactly on the true figure at ≈ +3360ms | The number *arrives* at its truth; it never overshoots |
| Cards' second row crosses 80% | Second batch feeds, 70ms left→right offsets (Element 15) | The pile is laid down across, by a hand |
| Reader hovers the totals row's neighbour card | Lift −3px + hard shadow (200ms); headline underline draws (220ms) | A cutting picked up off the pile |
| Reader scrolls on | Nothing re-runs; the section is print | The run has passed this sheet |

*The numbers a reviewer can check:* rule drawn before feed starts
(150ms gap); table fully filed ≤1s after its trigger; total lands
on the audited figure; red on this screen = the one drawn rule +
card mini-rules only (inside §10's 3% ration). *Short-content
variant:* if the scoreboard has no data story today, the whole
station is absent (§7: stations may be omitted, never reordered or
filled) — the choreography simply has one fewer beat.

### Example C — The conversion section: the subscribe coupon, scroll + interaction clock

The coupon (Element 16) at station 7 of the home page, below the
section fronts. This example runs on two clocks: the scroll that
brings the reader to it, and the hand that fills it.

*Scroll clock:*

| Scroll position | Beat |
|---|---|
| Coupon top crosses 80% vh | The coupon feeds (Element 3, full spec, 900ms) — dashed border, scissors mark and all, arriving like any sheet |
| Coupon crosses 50% vh | Nothing. Deliberately: a form does not perform for an audience; the next beat belongs to the reader |

*Interaction clock (from first focus):*

| t | Beat |
|---|---|
| 0ms | Reader clicks/taps the email field: rule inks to 2px `--ink`, label steps to ink + 700 — 180ms `--ease-proof` |
| Reader types, tabs | Each field inks in turn; the coupon reads as a form being written on, line by line |
| Blur on a valid field | Red proof tick stamps at the line's end (120ms) |
| Blur on the postcode field, left empty-but-required | Its rule turns `--red-deep` and holds; a correction box feeds in above it (400ms, quarter travel): "CORRECTION — THE POSTCODE LINE IS EMPTY. THE OFFICE CANNOT SEND YOUR EDITION WITHOUT IT." |
| Reader fixes it, presses PRINT MY SUBSCRIPTION | Button thuds (120ms) and holds at "AT THE PRESS…" |
| Server accepts (~600ms typical) | The tear: coupon translates 6px, border becomes the torn edge, 300ms `--ease-press` |
| +150ms later | The receipt prints with its office stamp (180ms): "RECEIVED AT THE OFFICE — 02:14, No. 214" + the next-step story card. Focus moves to the receipt |
| (Failure branch) Server rejects | No tear. Button releases (260ms); correction box at the coupon's head; every field keeps its words |

*Reduced-motion version:* focus inking is instant, the tear is a
static border swap at success, the receipt appears unstamped.
*No-JS version:* the same coupon submits natively and the receipt
is a server-returned page in the same dress — the conversion path
never depended on the choreography.

---

## 15. Full-page scroll choreography map — home page, top to footer

Every motion beat on a Midnight Press Run home page, in the order
the reader meets them. If a build's page does something not on this
map, the something is not in the theme.

| # | Scroll zone | Beat | Element(s) | The visitor's felt sense |
|---|---|---|---|---|
| 1 | 0 (load) | Nameplate stamps (220ms); ticker starts; ink-line at true progress | 13, 5 | The paper announces itself |
| 2 | 0 (load, +280ms) | Kicker + edition stamp strike; lead headline strikes line by line (≤450ms); deck wipes | 1, 2 | The news is being printed *now* |
| 3 | 0–first screens | Lead photo develops (dry-down 1100ms); first briefs feed | 7, 6 | Photographs finish; later news arrives |
| 4 | 140px | Masthead compresses to the 52px bar (260ms) | 13 | Ceremony folds; the instrument remains |
| 5 | Continuous | Cylinder turns (3 per page); ink-line fills; caption steps in inches | 4, 5 | The machine keeps pace with the hand |
| 6 | Pin stage (120vh) | Lead pinned; photo scrubs to settled; briefs file past | 6 | The finished front page, the arriving wire |
| 7 | Each section head at 82% | Kicker strikes → red rule draws (600ms) → section feeds (900ms) | 8, 3 | The editor marks; the sheet follows |
| 8 | Data station at 75% | Box-score rows file (40ms stagger); total rolls (1400ms) to its true figure | 14 | Returns coming in, counted honestly |
| 9 | Card batches at 80% | Cards feed left→right (70ms offsets), ≤8 per batch | 15 | Cuttings laid on the pile by a hand |
| 10 | Photo wells at 50% | Each photo develops in its well (scale + dry-down, 1100ms); ≤3 shimmer thereafter | 7 | Photographs finishing as they are met |
| 11 | EXTRA box (when present) | Half-feed on entry; weight pulse while on screen | 9 | The one shout, while it is true |
| 12 | Coupon at 80% | The coupon feeds like a sheet; then stillness — the form waits for the hand | 16 | The paper offers; the reader acts |
| 13 | Colophon entry | Nothing moves — until the closing line crosses 90%: STOP PRESS stamps once (180ms) | 17 | The last act of the press |
| 14 | Any scroll-up | No beat fires in reverse; scrubs (5, 4, 6's photo) track back as gears do; everything printed stays printed | — | A read paper, being re-read |

Two global properties the map guarantees: **no two entrance
choreographies ever run at full size simultaneously** (the queue in
Element 3 and the batch caps in Elements 14/15 enforce it), and
**the page is never more than one beat away from stillness** — at
any scroll position, stopping means the page settles to print within
900ms.

## 16. Whole-page performance budget

Part I gave per-element budgets. This is the page they must add up
to. A build that passes every element and fails this page budget
still fails.

**Asset weight (home page, first load, compressed):**

| Asset | Budget | Notes |
|---|---|---|
| HTML | ≤ 120 KB | The masthead, ticker items and first briefs are in it — the paper is server-printed |
| CSS | ≤ 60 KB (gzip) | One stylesheet; the theme has no utility framework underneath it |
| JS | ≤ 35 KB (gzip) | The shared rAF loop, observers, strike/feed arming, coupon logic — there is no framework runtime in this budget |
| Fonts | ≤ 130 KB total | Libre Franklin variable (subset to Latin + figures) + Newsreader variable with italics; `font-display: swap` with metric overrides (§3) |
| Hero image | ≤ 180 KB | Greyscale-treated, halftone is a CSS layer — the dots are never baked into the file |
| Total first load | ≤ 550 KB | Everything after the hero is lazy by section |

**Runtime budget:**

- **One rAF loop** for the whole page (§5 law 3). Its per-frame cost
  — cylinder transform, ink-line scaleX, photo scrubs, grain
  parallax — must average ≤ 2ms and never exceed 4ms on a mid-range
  Android (Moto G-class) device.
- **No frame over 20ms** attributable to theme code during a
  full-page scroll (§10 item 10); entrance animations are
  transform/filter only, and every animated layer is released at
  `animationend`.
- **Long tasks:** none over 50ms after load; the strike's line-split
  is build-time or server-side work, never a client-side layout
  thrash on first paint.
- **CLS ≤ 0.02** for the page: every space is reserved (stamp box,
  photo aspect ratios, EXTRA's 900-weight twin, skeleton geometries).
  The only permitted shift is a skeleton region inking in *below*
  the reader's position.
- **LCP ≤ 2.0s** on 4G mid-Android: the lead headline is LCP and it
  is server-rendered text — the strike animates a transform on
  already-painted type, so LCP is the paint, not the animation's
  end.
- **INP ≤ 200ms:** the thud answers in the same frame as the press;
  no interaction handler may do layout work synchronously.
- **Ambient CPU:** all loops together (grain shimmer ≤3 wells,
  ticker, EXTRA pulse) under 2% of one core (§5); every loop halts
  off-screen and in hidden tabs.

**Cut order — when the budget is exceeded, cut in this order, and
only this order:**

1. Ink-mist drift in the hero (pure atmosphere).
2. Grain shimmer → static 12% screen (the print look survives).
3. Grain parallax (the screen stays; it stops travelling).
4. Conveyor drift (`--reg` → 0; travel remains — sheets still feed).
5. EXTRA pulse on mid devices (weight stands at 800).
6. Fresh-sheet transition → native navigation (already its own
   rule on slow connections).
7. Cylinder update → every second frame (it turns coarser, §11.4).

**Never cut, at any budget:** the reveal fallbacks and force-settle
timers, the ink-line and its caption, the headline strike's
*existence* (its blur may go, per §11.1), focus visibility, the
coupon's working no-JS path, or any contrast value. A page that is
fast because its safety was removed is not within budget; it is
broken at a higher speed.

## 17. Build-order checklist — implementing the Midnight Press Run

Build in this order. Each step is checkable before the next begins;
the order exists because later steps assume earlier truths (a strike
timed against unloaded fonts, a feed armed before the static page
exists, are the two classic ways this theme is built wrong).

1. **Tokens first.** Implement §2's palette (all derived tokens, the
   night-desk set), §5's easing and duration tokens, and §3's type
   scale as CSS custom properties and utility classes. No component
   work begins until the tokens render a test sheet correctly in
   both modes.
2. **The static paper.** Build every page with zero animation and
   zero JS: masthead, sections, cards, tables, coupon, colophon —
   complete, readable, submittable. This is the product; everything
   after this step is the press being switched on. (§10 items 1–2
   are testable from here.)
3. **Fonts with their safety.** Variable fonts, metric overrides,
   the `document.fonts.ready`/300ms gate — verify no headline can
   strike or shift in a fallback face beyond 2px.
4. **Masthead + ink-line.** Element 13's three bands, then Element
   5's scrub wired to the (new, single) shared rAF loop with its
   lerp. The loop is built here, once; later steps plug into it.
5. **The strike.** Element 1 (with its aria-label discipline) and
   Element 2's stamp, including the server-rendered time and the
   60s clock check.
6. **The feed.** Element 3's observer, seeded `--reg`, queue, and
   the 1.2s force-settle — tested with the observer deliberately
   broken before proceeding.
7. **Section grammar.** Element 8's drawn rules with their
   kicker-first timing, then Element 15's cards and Element 14's
   tables on the feed's stagger system.
8. **The cylinder.** Element 4 into the rail, on the shared loop;
   verify retirement below 1280px and the no-overlap audit.
9. **Photographs.** Element 7's wells: treatment pipeline
   (greyscale, lifted blacks), dry-down, the 3-well shimmer grant,
   print removal.
10. **The pin.** Element 6 last among the scroll pieces — it
    depends on the feed, the scrub loop, and settled transforms
    (Element 3's transform-removal is what makes the sticky stage
    safe). Verify the <600px-height and <900px-width disablements.
11. **The wire & the shout.** Element 13's ticker (accessible-list
    pattern, pause rules, 8-item cap) and Element 9's EXTRA with
    its freshness demotion wired to real data.
12. **Forms.** Element 16 complete: focus inking, per-field
    corrections, the tear + receipt, the no-JS server path, the
    in-flight disable. Then §12's remaining components in the
    order the site's pages need them.
13. **Loading & leaving.** Element 11's skeletons for genuinely
    client-fetched regions; Element 12's transition armed only
    where prefetch is real.
14. **The colophon.** Element 17, with archived-edition freezing
    tested against a fixture of last month's edition.
15. **The gates.** Run §10 in full — blocking eight first, then
    the standard twelve — and §16's budget measurements on a real
    mid-range Android device, not an emulator's promise. Then the
    five-second test (§1) with a viewer who has never seen the
    site.

*End of Part II. A theme file that carries Part I and Part II is
the complete Midnight Press Run: the paper, the press, and the
proof of both.*
