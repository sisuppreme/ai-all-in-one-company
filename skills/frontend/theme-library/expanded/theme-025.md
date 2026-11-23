# 25. The Obituaries Page — Expanded (v1 + v2)

> Expansion of theme #25 from `themes-001-025.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same four palette
> anchors, the same two typefaces, the same twelve signature elements —
> deepened, never redesigned.

## 1. Concept & world

The most-read page in any newspaper was never the front page. It was
the obituaries page — the one page every reader eventually appears on,
and the one page written as if every word would be kept. This theme
borrows that page's gravity wholesale: lives summarised with economy
and grace, laid out like they matter, because on this page they do.

The world is a printed register of lives. Not a memorial *site* in the
funeral-home sense — no dark velvet, no doves, no candles rendered in
CSS — but a page of record: solemn white paper, ink, hairline column
rules, portraits in oval frames, and silence used as a layout material.
The page is a **procession**. A standing dedication waits at the head.
Then one life at a time: a name, its dates, a portrait that develops
slowly from blank paper the way a photograph develops in a tray, and
the life itself, set in serif at a reading measure. Between lives, a
full viewport of near-empty paper — not a gate, not a loading state,
just room to finish one life before beginning the next. Across each
pause, a floral rule draws itself: a stem, a leaf, one violet flower.
One. The violet is the theme's only colour beyond ink and grey, and it
is rationed like flowers at a graveside — placed, never scattered.

**The theme's one law: the entry order is inviolable.** Within every
entry, without exception, on every page type, at every breakpoint:
**name → dates → portrait → life.** The order is the obituary form
itself; it predates the web by a century and a half, and no layout
fashion, no A/B test, no stakeholder request rearranges it. A build
that shows a portrait before its name has not made a design choice; it
has made an error, and the quality gate (§10) treats it as one.

**Stillness is the design.** This is the quietest theme in the library
and it must stay that way under expansion pressure. Its motion budget
is deliberately the smallest: one 3-second develop per portrait, fades
of 600ms, a dash that lengthens once, a portrait that drifts exactly
2px, a light that settles by 3% and is gone. Everything else is print.
A reviewer who finds this theme "not animated enough" has understood
it correctly and judged it wrongly; the restraint is not an absence of
motion design, it *is* the motion design. Where other themes in this
library perform, this one attends.

**Best-fit sites and audiences.**

- Memorial and tribute platforms: registers of the dead maintained by
  families, regiments, schools, congregations, professional bodies —
  anywhere names are entered once and read for decades.
- Heritage brands with real dead to honour: founders' pages for family
  businesses, centenary histories, "the people who built this" archives
  for firms, orchestras, newspapers, universities.
- Legacy storytelling for the living, used carefully: retirement
  tributes, farewell pages for long-serving colleagues, a founder
  handing over — the form lends its gravity, and §6.10's closing line
  is repurposed for exactly this.
- Institutional remembrance: war-memorial registers, disaster memorials,
  anniversary rolls of honour — contexts where a percentage progress
  bar would be an obscenity and this theme's "lives, n of N" is the
  only acceptable arithmetic.

**When NOT to use it.**

- For anyone whose death is recent news rather than settled record —
  the page's calm is for remembrance, not for breaking grief; a family
  in the first days needs a plainer, warmer tool.
- For celebratory "wall of fame" content. This form buries people;
  borrowing it for employee-of-the-month is a category error the
  audience will feel even if they cannot name it.
- For high-volume directories where lives are skimmed, compared or
  filtered commercially. The procession assumes one life at a time,
  read whole.
- For brands whose voice is playful, loud or ironic. There is no ironic
  register available here; the theme cannot wink.
- Where entries are user-generated at scale without editorial care.
  Every entry on this page reads as *published*; unmoderated text in
  this typography acquires an authority it has not earned.

## 2. Palette

Four anchors, inherited unchanged. The palette is a printed page:
white that is not quite white, ink that is not quite black, a grey for
everything that must recede, and one flower.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--paper` | `#F8F6F1` | The page itself; every background, every pause | ~88% of pixels | Solemn white — warm, matte, unbleached-paper rather than screen-white. Ink on it: 15.9:1. It is never swapped for pure `#FFFFFF` anywhere, including form fields and the footer. |
| `--ink` | `#1D1B18` | Names, life text, dates at full weight, rules at full strength | ~8% of pixels | On paper 15.9:1 — passes every level for every size. The only colour body text may ever be set in. |
| `--grey` | `#6E6A61` | Mourning grey: dates at rest, captions, the foot margin, hairlines at full strength, secondary facts | ~3% of pixels | On paper 5.1:1 — passes AA for text ≥14px and for large text; **never** used below 14px and never for the life itself. Its job is recession with legibility kept. |
| `--violet` | `#5C4A72` | The one flower: the floral rule's single bloom, the hover hairline, text selection, the "In lieu of flowers" line's rule | ≤1% of pixels, hard ration (§9) | On paper 7.4:1 — passes AA at any size, which is irrelevant: violet is rationed by meaning, not by contrast. One flower per floral rule; one rule per entry; nothing else violet except selection and the §6.9 hover hairline. |

**Derived tokens** (computed from the anchors; never new hues):

| Token | Derivation | Use |
|---|---|---|
| `--hairline` | `--grey` at 28% over `--paper` | The column rules and entry hairlines at rest. Decorative only — never the sole carrier of meaning. |
| `--hairline-strong` | `--grey` at 55% over `--paper` | The dedication plaque's border; the form's ruled lines at rest. |
| `--ink-soft` | `--ink` at 72% over `--paper` | The life's secondary paragraphs may not use it — reserved for the register table's (§6.14) dates column and visited-entry names. |
| `--violet-pale` | `--violet` at 14% over `--paper` | The "In lieu of flowers" expansion's background wash (§6.10) and the correction slip (§11). The only tinted surface on the page. |
| `--paper-deep` | `--paper` darkened 3% (`#F1EEE6`) | The skeleton entries' oval fill (§6.12) and the pause's almost-nothing gradient foot. A difference felt, not seen. |
| `--develop-ghost` | `--grey` at 40% over `--paper` | The developing portrait's mid-stage tint (§6.1) — a photograph half-arrived. |

**Dark-mode behaviour.** There is none, and the refusal is the
specification. An obituaries page is a printed page; print does not
invert at night. A build that adds a dark mode has imported the
funeral-home aesthetic this theme exists to refuse — black velvet,
glowing candles, the whole upholstered vocabulary of commercial grief.
`prefers-color-scheme: dark` is answered with the same page, unchanged.
(Reading at night is served by the OS's own brightness and warmth
controls, as it is for paper.) The one concession to darkness anywhere
in the theme: none. State it in the build notes so a future maintainer
does not "fix" it.

**Selection.** Text selection is violet — `--violet` background at 18%
over paper, ink text — the theme's only flourish, inherited from the
original entry. It is the single place a reader's own hand leaves the
flower colour on the page.

## 3. Typography

Two faces, inherited: **Playfair Display** for names, **Source Serif 4**
for everything else. No third face is admitted — no sans for UI chrome,
no script for sentiment. The moment a script font appears, the page
becomes a greeting card; §9 lists it as a failure.

| Role | Face & setting | Size / line-height | Rules |
|---|---|---|---|
| The name | Playfair Display, regular (400), no italic | 44px / 1.08 desktop; 34px tablet; 28px phone | One name per entry, set as a headline is set in the paper: first name and surname, no titles of address in the name line itself ("Dr" and "Mrs" belong to the life's first sentence if anywhere). Never letterspaced, never uppercase, never bold — Playfair at 400 has all the ceremony the name needs. |
| The dates | Source Serif 4, small caps effect via `font-variant-caps`, tabular figures | 15px / 1.4, `--grey` | Format fixed: `1938 — 2026`, en-space, em dash, en-space. The dash is an element (§6.3), not a hyphen; a build that renders `1938-2026` has failed a gate item. A single year with "b." prefix for the living version. |
| The life | Source Serif 4, regular | 18px / 1.78, `--ink` | The reading voice. 55–65ch measure. First paragraph may carry a drop initial? **No** — drop caps are for features pages; a life begins plainly, with its first word. Paragraphs separated by 0.9em space, never indented-and-spaced both. |
| The dedication | Source Serif 4, italic | 19px / 1.65, `--ink` | The only italic on the page, reserved for the standing dedication (§6.13) and for quoted words within a life. Italic is the voice of the page speaking in its own person. |
| Captions & facts | Source Serif 4, regular | 14px / 1.55, `--grey` | Portrait captions ("Eleanor, at the house in Ambleside, 1974"), years of service, family counts. The smallest text on the page; never below 14px. |
| The foot margin | Source Serif 4, letterspaced 0.14em, uppercase | 12px / 1.5, `--grey` | "LIVES, 4 OF 23" and the colophon line. Uppercase exists only here and in form labels — the page's apparatus voice. |
| Form labels | Source Serif 4, letterspaced 0.1em, uppercase | 12px, `--grey` | See §6.16. The form speaks in the apparatus voice until the confirmation, which speaks in the dedication's italic. |

**Type laws.**

1. **The name is the headline.** Nothing on an entry may be set larger
   than its name — not the dedication (19px), not a pull-quote (there
   are none), not the form's heading.
2. **No exclamation marks in type, anywhere.** Not in errors, not in
   confirmations, not in empty states. The gate greps for them (§10).
3. **Figures are tabular and quiet.** Years, counts and ages set in
   Source Serif's tabular figures; they never animate by counting
   (§6.8) and never appear in a size above 18px.
4. **The em dash in the dates is set with en spaces** and is the only
   dash the theme animates (§6.3). Hyphens appear only inside the
   life's ordinary prose, where grammar puts them.

## 4. Layout language

**The procession is the grid.** One centred column of lives on an
unbroken sheet of paper. There is no sidebar, no card grid, no masonry
of the dead. The layout's courage is its refusal to arrange lives side
by side for comparison.

- **The measure.** Life text sets at 62ch maximum (≈620px at 18px).
  The name and dates centre on the measure; the portrait oval centres
  above the life's first line; captions centre beneath the portrait.
  Everything in an entry shares one centre axis — the axis of a
  headstone, and of a newspaper column.
- **The column rules.** Two hairline vertical rules (`--hairline`, 1px)
  run the full height of the procession at the measure's edges,
  unbroken through entries and pauses alike. They are the newspaper
  column made visible, and they are the reference the portraits drift
  against (§6.6). On <768px they retire to the viewport edges at 16px
  inset — present, but no longer touching the text.
- **The pause.** Between entries, exactly one full viewport height
  (100vh, min 560px) of near-empty paper: the column rules, nothing
  else, and the floral rule (§6.5) centred within it. The pause is
  spacing, not a section — it has no heading, no content, no
  interaction. §9 names the failure of filling it.
- **Entry rhythm.** Name at the pause's end +12vh of travel; the entry
  occupies its natural height; the next pause begins 18vh after the
  life's last line and its closing line. The rhythm is processional:
  pause, life, pause, life — a reader learns it by the second entry
  and is never surprised again. Predictability is a kindness here.
- **Density.** The sparsest theme in the library: one entry per
  viewport at most, ~88% paper by pixel. Density increases are refused
  at review; a stakeholder asking to "fit more lives per screen" is
  asking for a different theme (§1).
- **The head and the foot.** The page opens with the masthead register
  line (§6.14's navigation in its quiet form) and the standing
  dedication (§6.13), pinned softly until the first entry arrives. It
  closes with the foot margin (§6.17): the lives count, the floral
  rule drawn complete, and the register's colophon. Nothing else may
  be placed after the last life except the invitation to inscribe
  (§6.16's entry point) and the foot.
- **Whitespace as material.** The paper is not a background the content
  sits on; it is the content's largest component — the silence between
  lives is part of the page's text, set in the layout the way rests
  are set in music. Every spacing value in this section is therefore
  a content decision, and compressing the pauses "for engagement" is
  an editorial change, not a performance optimisation.

## 5. Full motion system

Every motion term from the library's vocabulary, translated into this
theme's language — which mostly means refused, rationed, or slowed
until it behaves like print. Named easings first; they are the only
three the theme owns.

| Token | Curve | Character |
|---|---|---|
| `--ease-develop` | `cubic-bezier(0.55, 0.06, 0.35, 1)` | The developing tray: slow to begin, a long middle where the image gathers, a gentle arrival. Used by §6.1 and §6.12 only. |
| `--ease-settle` | `cubic-bezier(0.25, 0.6, 0.3, 1)` | A page laid down: everything that fades or drifts uses it. The theme's default. |
| `--ease-draw` | `cubic-bezier(0.4, 0, 0.3, 1)` | A pen drawn at even pressure: the floral rule and the dash. |

Durations are long by library standards and fixed: develop **3000ms**,
sequence fades **600ms**, dash **800ms**, figure fades **800ms**,
expansion **500ms**, page transition **700ms**. Nothing in this theme
moves in under 400ms except the hover's contrast settling (400ms) —
haste is the one unaffordable effect.

- **Scroll-triggered reveals** — the entry sequence (§6.2): name, then
  dates, then portrait, then life, each fading 600ms `--ease-settle`
  as the entry crosses the trigger line (element's top at 72% of
  viewport height). Triggered once per entry per page-load; scrolling
  back does not replay a life.
- **Parallax** — almost none, by design (§6.6): portrait ovals drift
  exactly **2px** against their column rules across their scroll pass,
  lerped at `--lerp: 0.06` — the slowest lerp in the library. Nothing
  else parallaxes. Two more pixels is a gate failure (§10), not a
  judgement call.
- **Pinned scenes** — one only: the standing dedication (§6.13) pins
  softly at the head of the procession and releases when the first
  entry's name reaches it. No entry ever pins; a pinned portrait would
  hold a life hostage to the scroll.
- **Masked line reveals** — refused as a device; translated once: the
  portrait reveals inside its oval clip-path as it develops (§6.1) —
  the mask is the frame, and it never moves.
- **Blur-to-sharp reveals** — translated into the develop (§6.1):
  photographic stages (opacity and contrast rising through a ghost
  stage), not a Gaussian blur wipe. Print develops; it does not
  unblur. No element in the theme uses a CSS blur filter at any size.
- **Animated counters** — refused as spectacle; translated into quiet
  figure fades (§6.8): years and counts fade to their figure over
  800ms. A number that *counts up* on an obituaries page is a gate
  failure.
- **Progress indicators** — the floral rule itself (§6.5), drawing
  scrubbed across each pause, plus the discreet "lives, n of N" in
  the foot margin (§6.11). Percentages and bars are forbidden by the
  theme's founding law and grepped at the gate.
- **Marquees** — refused, in writing, permanently. A marquee of names
  would be a desecration of the form; if a design seems to need one,
  the design is wrong.
- **Kinetic typography** — one instance: the lengthening dash (§6.3).
  The dash is the life in one stroke; no other letter or word moves,
  ever. Names never animate letter by letter — a name assembling
  itself is a magic trick performed at a funeral.
- **Ambient loops** — one: the settling light (§6.7), contrast +3%
  over 2s as a portrait centres. There is no second loop. The page's
  ambience is stillness.
- **Micro-interactions** — hover is attention (§6.9: +4% contrast, a
  hairline violet rule); click is the quiet expansion (§6.10). No
  press states scale, bounce or depress; a button on this page is
  pressed the way a register's page is turned — flatly.
- **Page transitions** — a long fade through white, 700ms (§6.12):
  out through paper, in through paper. No slides, no wipes; the
  reader turns a leaf of the register.
- **Image treatments** — portraits only, always in oval frames, always
  grayscale-neutral (the photograph's own tones; **sepia is forbidden**
  — §9), scale-in-frame capped at 1.02 during the develop and never
  again. Photographs are never cropped by the layout after the oval;
  the oval is chosen per portrait at content time (§6.1 edge cases).
- **Scroll smoothing** — the shared rAF loop runs at `--lerp: 0.06`
  and drives exactly two things: the 2px drift and the settling
  light. Everything else is trigger-and-transition. If the loop is
  removed, the page loses a breath and nothing else.
- **Skeleton loading** — developing skeletons (§6.12): oval and grey
  lines that develop in like portraits, because even the page's
  waiting is done in its own processes.


## 6. Signature elements

### 6.1 The developing portrait

- **What & why.** The theme's signature and its thesis performed at
  the pace of chemistry. The portrait develops from blank paper
  inside its oval frame over 3 seconds — opacity and contrast rising
  in developing-tray stages, the way a photograph arrives under red
  light: first nothing, then a ghost, then a person. Nothing else on
  the page moves while it happens. In a library of themes that reveal
  images, this one *develops* them, because the people on this page
  are not content being loaded; they are being remembered, and
  remembering takes the time it takes.
- **Structure.** A `<figure class="portrait">` holding one `<img>` —
  always the real photograph, fully loaded or loading with its real
  `alt` — inside an oval `clip-path: ellipse(50% 50% at 50% 50%)` on
  a frame of aspect 4:5, max-width 300px, centred on the entry axis.
  The develop is a CSS filter/opacity progression on the image itself
  (`opacity`, `contrast`, `brightness`), never an overlay that hides
  it: the photograph is in the DOM and in the accessibility tree from
  the first byte. A hairline oval ring (`--hairline-strong`) sits on
  the frame's edge as print, present in every state.
- **Motion spec.** Triggered by the entry sequence (§6.2) at the
  portrait step. Duration **3000ms**, `--ease-develop`, in three
  stages the easing makes legible: *blank* (0–600ms: opacity 0→0.12,
  contrast 40%, brightness 112% — paper with a rumour on it), *ghost*
  (600–1900ms: opacity →0.62, contrast →78%, tinted through
  `--develop-ghost` — a face findable but not yet met), *arrival*
  (1900–3000ms: opacity →1, contrast →100%, brightness →100%, and the
  frame's scale-in completes 1.02→1.0 across the same span). After
  3000ms all filters are removed by class, leaving the plain
  photograph in its frame — the developed state is the absence of
  effect.
- **Choreography timeline (v2).** Entry sequence reaches the portrait
  step (name settled, dates settled, dash drawn) → t+0: the image
  begins stage one from its pre-state (applied by the sequence, never
  by default CSS) → t+600ms: ghost stage, the sitter's posture
  readable → t+1900ms: the face arrives → t+3000ms: filters clear,
  the caption fades in beneath (600ms, §6.2's order — caption is part
  of the life step, not the portrait's) → the life text begins its
  fade only after t+3000ms. If the visitor scrolls away mid-develop,
  the develop continues off-screen to completion — a photograph does
  not stop developing because the tray was left; on return it is
  simply there.
- **State matrix (v2).** *Rest (pre-trigger):* the frame shows the
  photograph at final state — the pre-state exists only between the
  sequence arming and firing, a window of milliseconds; a portrait
  never *waits* invisible. *Hover:* §6.9 (contrast +4%). *Focus:*
  the image is not focusable; its entry's links are, and focusing
  them does not touch the portrait. *Active:* n/a. *Scrolled-past:*
  developed, static, filters cleared — identical on desktop and
  touch. *Disabled (no JS):* the photograph, plain, in its oval —
  the designed state, fully honourable.
- **Content merge.** The portrait is the entry's own photograph and
  the develop is what photographs do. Remove the effect and the entry
  is a printed obituary with a picture: poorer in ceremony, complete
  in content.
- **Failure fallback.** The founding law, inherited: **the develop is
  an enhancement on a fully-present image with a hard fallback.** If
  the image has not loaded within 2000ms of the portrait step firing,
  the develop is abandoned for that entry — when the image arrives it
  appears at final state in a single 600ms fade. If filters are
  unsupported, the develop degrades to the opacity ramp alone. A
  watchdog at trigger+3400ms forces the final class regardless of
  animation state; `transitionend` is never trusted with a face.
- **Reduced-motion variant.** No develop. The portrait is present at
  final state when its entry is reached, appearing with the life in
  the sequence's single quiet fade — or, under the strictest reading
  (§6.2's variant), simply there. The information lost is zero; the
  ceremony is respectfully omitted.
- **Breakpoints (v2).** ≥1200px: frame 300px wide, as specced.
  768–1199px: 260px; stage timings unchanged (chemistry does not
  hurry for tablets). <768px: 220px; the develop shortens to 2400ms
  (stages compressed proportionally) because a phone is held closer
  and the ghost stage reads sooner; the 2000ms image fallback is
  unchanged.
- **Edge cases & failure modes (v2).** *Missing photograph:* some
  lives have none — the entry omits the figure entirely and the
  sequence runs name → dates → life; an empty oval is never rendered
  (an empty frame reads as a redaction, and this page redacts
  nothing). *Wrong crop:* the oval is set per portrait at content
  time via `object-position`; faces must sit in the oval's upper
  two-thirds — a content rule checked at the gate, because a face
  clipped by the frame is the theme's ugliest possible failure.
  *Very dark or very light photographs:* the ghost stage's contrast
  floor (40%) is relative to the image's own values, so dark prints
  develop darker, never greyer — the stage tints are computed from
  the image, not painted over it. *Scroll-back:* never re-develops;
  a developed portrait stays developed for the page-load's life.
- **Accessibility spec (v2).** The `alt` is the portrait's caption in
  full ("Eleanor Hartley, at the house in Ambleside, 1974") — the
  visible caption repeats it in prose, so the image may be `alt=""`
  where the caption is adjacent and complete; where no caption
  exists, the alt carries the identification. The develop is
  decorative enhancement of an already-announced image; screen
  readers meet the photograph, never the tray. Contrast of the final
  state is the photograph's own; the theme's obligation is the
  caption's legibility (14px `--grey` on paper, 5.1:1 ✓).
- **Performance budget & mobile variant.** One image, no renditions:
  the develop is filters on a single `<img>` (portrait ≤ 120KB,
  served at 2× frame width). Filter animation on one element ≤
  0.4ms/frame in the shared loop's accounting — the cheapest signature
  in the library. Mobile: same single image ≤ 80KB; the shortened
  2400ms develop above.
- **Tokens consumed (v2).** `--paper`, `--develop-ghost`,
  `--hairline-strong`, `--ease-develop`, `--lerp`.

### 6.2 Fixed entry order (the sequence)

- **What & why.** The genre's etiquette, mechanised. Within every
  entry the elements arrive in the inviolable order — **name →
  dates → portrait → life** — each fading in quietly only after the
  previous has settled. The sequence is not a flourish laid over the
  entries; it is how an obituary is *read*, and the animation simply
  refuses to let the eye cheat. A visitor who scrolls fast still
  receives the name before the face. That is the whole point of the
  theme, expressed as a state machine.
- **Structure.** Each entry is an `<article class="entry">` whose four
  steps are children in DOM order — `<h2 class="name">`, `<p
  class="dates">`, `<figure class="portrait">`, `<div class="life">`
  — so the no-JS and screen-reader order *is* the sequence order; the
  enhancement only times what the document already says. A per-entry
  IntersectionObserver arms the sequence when the name's top crosses
  72% of viewport height; a small sequencer then steps a
  `data-step` attribute 0→4, and CSS transitions keyed to the steps
  do the fading. Steps are latched: once an entry has sequenced, its
  steps never reset within the page-load.
- **Motion spec.** Each step fades 600ms `--ease-settle`, starting
  only when the previous step's fade has completed (steps are
  sequential, never overlapped — overlapping fades are chatter).
  Step timings: name 600ms → dates 600ms (its dash, §6.3, draws
  across the dates' own span) → portrait 3000ms (the develop, §6.1)
  → life 600ms, with the life's internal facts (§6.8) fading on
  their own later triggers. Full entry ceremony ≈ 5.4s from trigger
  to a settled life — unhurried, and skippable by simply reading:
  every step's *content* is present in the DOM from the start, and
  the fades are opacity only on elements already laid out.
- **Choreography timeline (v2).** Name crosses 72% line → t+0: name
  fades (0–600ms) → t+600: dates fade (600–1200ms) and the dash
  lengthens within them (§6.3, 800ms from t+600) → t+1200: portrait
  step fires the develop (1200–4200ms) → t+4200: life fades
  (4200–4800ms), caption with it → entry settled; the sequencer
  disarms. If the entry enters the viewport already half-scrolled
  (anchor jump, find-in-page), all steps snap to settled instantly —
  the ceremony is for arrivals, not for landings.
- **State matrix (v2).** *Rest (untriggered, below the fold):*
  content laid out at full opacity in the raw document; pre-states
  are applied by JS only at arm time, so an untriggered entry is
  never invisible in any static rendering. *Hover/focus:* the
  sequence has no interactive states; focus landing inside an
  untriggered entry (keyboard tabbing down the page) forces that
  entry settled instantly — focus must never arrive at invisible
  content. *Active:* n/a. *Scrolled-past:* settled, latched.
  *Disabled (no JS):* the document order, plain — the sequence's
  disabled state is indistinguishable from its content, by design.
  Touch identical to desktop throughout.
- **Content merge.** The sequence *is* the content's own reading
  order; there is nothing to merge because nothing was added. This
  element is the clearest case in the library of motion as etiquette
  rather than effect.
- **Failure fallback.** A per-entry watchdog: 6000ms after arming, if
  any step has not completed (observer fault, transition fault,
  hidden tab throttling), the entry is forced to settled in one
  frame. Globally, if the sequencer script fails to load, no
  pre-states are ever applied and the page is a printed register —
  the fallback is the absence of the enhancement, arranged in
  advance.
- **Reduced-motion variant.** The order is kept and the timing is
  not: all four steps appear together in one 600ms fade (or
  instantly, under `prefers-reduced-motion: reduce` with the build's
  strict flag). Name still precedes portrait *in the document* —
  reduced motion removes the ceremony, never the etiquette.
- **Breakpoints (v2).** Identical choreography at all sizes; only
  §6.1's develop duration changes at <768px, shortening the portrait
  step and therefore the whole entry to ≈4.8s.
- **Edge cases & failure modes (v2).** *Entry without a portrait:*
  the sequence runs three steps; timings compress (life fires at
  t+1200). *Very long life:* the life step fades the whole block as
  one; its internal figure fades (§6.8) arm independently so a long
  entry's later facts still arrive quietly as they are reached.
  *Rapid scroll through many entries:* each arms and sequences
  independently; entries passed entirely without stopping still
  complete their sequences off-screen (latched settled when met
  again) — the page never presents a backlog of un-sequenced lives.
  *Back-scroll:* latched; nothing replays. A life is introduced once.
- **Accessibility spec (v2).** DOM order = reading order = sequence
  order; no `aria-hidden` is ever applied to a pre-state element
  (opacity only), so assistive technology reads a settled page at
  all times regardless of the visual ceremony. Focus-forces-settle
  (above) guarantees keyboard users never tab into a fade. The
  sequence adds no announcements; a life arriving is not an event a
  screen reader should narrate.
- **Performance budget & mobile variant.** One observer per entry,
  transitions on opacity only; sequencer cost negligible (<0.1ms/
  frame amortised). No mobile variant — the ceremony is the same in
  the hand as on the desk.
- **Tokens consumed (v2).** `--ease-settle`, `--ink`, `--grey`.

### 6.3 The lengthening dash

- **What & why.** The entry's single kinetic moment, and the smallest
  piece of kinetic typography in the library: the dash between the
  birth and death years lengthens as the life span is stated. The
  dash *is* the life — everything between the two years, in one
  stroke — and the theme spends its entire kinetic-typography budget
  on it, once per entry. A visitor who notices it has understood the
  page; a visitor who doesn't has lost nothing.
- **Structure.** The dates line is `1938 <span class="dash">—</span>
  2026` where the dash is an inline SVG line (or a scaled em-dash
  glyph in the no-SVG path) inside a span of fixed final width
  (1.6em). The line draws via `stroke-dashoffset` scrubbed by its
  own 800ms transition, `--ease-draw`. The years never move; the
  span's width is reserved from first layout, so the draw causes no
  reflow — the years stand still and the life grows between them,
  which is also the correct metaphysics.
- **Motion spec.** Fires at the dates step of the sequence (§6.2,
  t+600 within the entry): the dash draws left→right, birth→death,
  over **800ms**, completing as the dates' own 600ms fade settles
  around it (the draw outlasts the fade by 200ms deliberately — the
  last thing to settle in the dates line is the life span itself).
  Fires once per entry, latched with the sequence.
- **Choreography timeline (v2).** Dates step begins → t+0: dates at
  opacity 0→1 begin → t+0: dash offset at full (undrawn) → t+200ms:
  draw begins (the years must be legible before the span grows) →
  t+1000ms relative to the step (800ms of draw): dash complete →
  portrait step fires (§6.2's t+1200). Total: the span is whole
  before the face arrives.
- **State matrix (v2).** *Rest:* drawn — the undrawn state exists
  only inside the sequence window. *Hover:* none; the dash is not a
  control. *Focus:* n/a. *Active:* n/a. *Scrolled-past:* drawn.
  *Disabled:* a plain em dash in a dates line — which is to say, the
  correct printed form. Touch identical.
- **Content merge.** The dash is a character in the dates line, not
  an ornament near it. Its animation is the biography's argument made
  visible inside the biography's own first line.
- **Failure fallback.** If SVG is unavailable, the fallback is the
  unanimated glyph — no JS path exists in which the dates render
  without a dash: the dash is in the HTML as a text node from the
  start, and the SVG draw, where used, replaces it only at arm time
  with the glyph retained for assistive technology.
- **Reduced-motion variant.** The dash is simply present. Nothing is
  lost; the dates read as they read in print.
- **Breakpoints (v2).** Unchanged at all sizes; at <768px the dates
  set at 14px and the dash span narrows to 1.4em — proportions kept,
  ceremony kept.
- **Edge cases & failure modes (v2).** *Open-ended dates (the living
  version):* `1938 —` with no death year: the dash draws to 70% and
  stops, unfinished — the one sanctioned incomplete draw in the
  theme, because the life is. *Same-year lives* (infants, `2026 —
  2026`): the dash draws fully but the dates step adds no emphasis;
  the entry's handling is an editorial matter (§12), and the theme
  gives it the same ceremony as any other — no smaller type, no
  shorter pause. *Missing birth year:* the line reads `— 2026`
  ("year of birth not recorded" in the caption register, §12); the
  dash does not draw — there is no span to state.
- **Accessibility spec (v2).** The dates are exposed as text
  ("1938 to 2026" via an `aria-label` on the dates line, since screen
  readers handle the bare dash inconsistently); the animated line is
  `aria-hidden`. The draw is invisible to assistive technology, as it
  should be — the *fact* is the span, and the fact is in the text.
- **Performance budget & mobile variant.** One SVG path transition
  per entry; cost beneath measurement. No mobile variant.
- **Tokens consumed (v2).** `--grey`, `--ease-draw`.

### 6.4 Full-viewport pauses

- **What & why.** Between lives, a full viewport of near-empty paper.
  The pause is the theme's boldest layout decision: an entire screen
  spent on nothing but column rules and silence, so that one life
  can be finished — grieved, admired, closed — before the next
  begins. It is spacing, not a gate: ordinary scrolling passes it at
  any speed, and nothing in it loads, unlocks or triggers. The pause
  is the page trusting the reader with empty time.
- **Structure.** A `<div class="pause" aria-hidden="true">` of height
  100vh (min 560px, and exactly one per inter-entry gap), containing
  only the continuation of the two column rules (drawn by the page's
  background layer, passing through) and the floral rule (§6.5)
  centred vertically within it. The pause carries no text, no links,
  no heading — it is excluded from the accessibility tree and from
  find-in-page results, honestly empty.
- **Motion spec.** None of its own. The pause is where other
  elements' motion is *absent*: the floral rule draws across it
  (§6.5, scrubbed), and that is the only movement the pause ever
  hosts. Scroll behaviour through it is the browser's own — no
  snapping, no scroll-jacking, no velocity modification, ever (§10
  gate item).
- **Choreography timeline (v2).** A life settles → the reader scrolls
  → the life's last line leaves the viewport top → paper, rules, the
  floral rule drawing as the pause crosses the viewport centre →
  the rule completes as the pause's centre passes → paper again →
  the next name crosses the 72% line and its sequence begins (§6.2).
  The pause's "timeline" is the reader's own pace; the theme
  schedules nothing inside it.
- **State matrix (v2).** *Rest:* paper and rules. *Hover/focus/
  active:* no interactive surface exists. *Scrolled-past:* identical
  — a pause read and a pause unread are the same pause. *Disabled:*
  identical; the pause needs no JS to be empty. All sizes, all
  inputs, one state: silence.
- **Content merge.** The pause is not decoration around content; by
  the theme's founding argument (§4) it *is* content — the rest in
  the music. Removing it does not break any entry and destroys the
  page, which is the definition of a structural element.
- **Failure fallback.** The pause cannot fail; it is a height and a
  background. Its failure mode would be absence (a build that
  compresses it), which is an editorial breach caught at review, not
  a runtime fault.
- **Reduced-motion variant.** Identical. The pause is already the
  reduced-motion ideal the original entry names.
- **Breakpoints (v2).** ≥1200px and 768–1199px: 100vh, min 560px.
  <768px: 88vh, min 480px — a phone's viewport is a more intimate
  measure and the full height reads as a fault rather than a rest;
  the reduction is 12%, the smallest the theme permits, and the
  column rules inset to the viewport edges (§4).
- **Edge cases & failure modes (v2).** *Short viewports (landscape
  phones, small laptop windows):* the min-height governs (560/480px)
  so the pause never collapses into a mere gap. *Reader using
  keyboard/page-down:* pauses pass like any content; nothing traps
  focus (the pause contains no focusable element). *Print:* pauses
  collapse to a single page-break with the floral rule printed
  complete (§14) — paper has its own silences.
- **Accessibility spec (v2).** `aria-hidden`, no role, no label —
  assistive technology moves from one life to the next without
  announcing the emptiness, exactly as a reader of the printed page
  turns from one entry to the next. The floral rule inside it is
  decorative to AT (§6.5); the lives count (§6.11) is the progress
  signal, available in the foot margin without entering the pause.
- **Performance budget & mobile variant.** Zero runtime cost. The
  mobile variant is the 88vh height above.
- **Tokens consumed (v2).** `--paper`, `--hairline`.

### 6.5 The self-drawing floral rule

- **What & why.** Between lives, the divider is a floral rule — a
  stem, a leaf, one violet flower — that draws itself in SVG,
  scrubbed as the reader crosses the pause. It is also the theme's
  progress indicator (§5): the reader knows where they are in the
  procession by the drawing of the rules, the way a mourner knows a
  service by its order of service. The rule is drawn *by the act of
  passing* from one life to the next; its completion is the
  permission — never enforced, only offered — to begin the next.
- **Structure.** One inline SVG per pause, width 180px, centred: a
  stem path (a gentle horizontal with a single rise), one leaf path
  branching below the stem's midpoint, and the flower — five petals
  around a centre, drawn as one path — at the stem's right end, the
  only element on the page filled with `--violet`. Total path length
  budgeted at authoring time; `pathLength="100"` normalises the
  scrub math. The stem and leaf stroke in `--grey`; the flower
  strokes and fills in `--violet` at the draw's final beat.
- **Motion spec.** Scrubbed, not timed: `stroke-dashoffset` is a pure
  function of the pause's progress through the viewport (pause centre
  from viewport bottom to viewport centre = draw 0→100%), driven by
  the shared rAF loop at `--lerp: 0.06` — the slowest scrub in the
  library, so the drawing feels like growth, not rendering. Order
  within the draw: stem 0–70%, leaf 55–85% (overlapping, as a leaf
  grows off a living stem), flower 85–100%, its fill fading in over
  the final 10%. Scrolling back un-draws it, symmetrically — the
  rule is a function of position, nothing is latched.
- **Choreography timeline (v2).** Pause enters viewport → stem
  begins at its left → pause centre crosses viewport's lower third →
  leaf branches → pause centre reaches viewport centre → flower
  completes and fills → the next entry's sequence arms (§6.2) as the
  name crosses 72%. A reader who stops mid-pause holds a half-drawn
  rule indefinitely; it waits without impatience.
- **State matrix (v2).** *Rest (pause off-screen below):* undrawn.
  *Rest (pause passed):* drawn complete, and it stays drawn for as
  long as the reader remains below it. *Hover:* none — the rule is
  not a control, and hovering it does nothing, on purpose. *Focus:*
  not focusable. *Active:* n/a. *Scrolled-past:* complete.
  *Disabled (no JS):* the rule renders **fully drawn** — the static
  document shows finished rules between lives, because in print the
  rule is simply there. Touch identical to desktop.
- **Content merge.** The rule is the divider between the two lives it
  separates and the progress of the whole page in one object; it is
  punctuation that reports position. Remove the scrub and the
  printed rule remains — the merge is total.
- **Failure fallback.** If the shared loop stalls or SVG dash
  properties are unsupported, rules render fully drawn (the disabled
  state) — the fallback is print. A rule may never render *partially
  drawn and stuck*: the loop's watchdog (§14) snaps any rule whose
  pause is fully passed to complete.
- **Reduced-motion variant.** Fully drawn, always, in place. The
  progress information survives in §6.11's count; the drawing
  ceremony is omitted.
- **Breakpoints (v2).** ≥1200px: 180px wide, centred in the pause.
  768–1199px: 160px. <768px: 140px, and the scrub range shortens
  with the 88vh pause (§6.4) — the draw completes by the same
  centre-crossing beat.
- **Edge cases & failure modes (v2).** *The last pause:* after the
  final entry there is no next life; the closing rule (§6.17) is a
  separate, always-complete instance in the foot — the scrubbed
  rules exist only *between* lives. *Fast fling through several
  pauses:* the lerp settles each rule to its true offset within
  300ms of scroll rest; no rule is left mid-draw by velocity.
  *Flower ration enforcement:* the SVG is authored with exactly one
  flower path; a build variant with a garland fails §9's ration at
  review, not at runtime.
- **Accessibility spec (v2).** `aria-hidden="true"` on the SVG; the
  rule announces nothing. Progress for assistive technology is the
  lives count (§6.11), exposed as text in the foot margin and
  updated without live-region chatter (polite, on entry settle only,
  and only where the platform's AT conventions expect it — the count
  is primarily visual furniture in the margin, mirrored in the
  register, §6.14).
- **Performance budget & mobile variant.** Three paths per pause,
  one dash update per frame for the pause currently in view only —
  ≤0.15ms/frame. Mobile: the 140px rule above; dash updates
  unchanged.
- **Tokens consumed (v2).** `--grey`, `--violet`, `--ease-draw`,
  `--lerp`.

### 6.6 Two-pixel portrait drift

- **What & why.** The theme's entire parallax budget, spent on one
  gesture: portrait ovals drift exactly 2px against their column
  rules across their scroll pass. Two pixels is not a rounding of a
  larger effect; it is the effect, chosen because at 2px the motion
  is felt rather than seen — the depth cue of a held breath. The
  restraint is the depth. Any build that drifts 6px "so users notice
  it" has vandalised the theme's thesis (§9).
- **Structure.** The portrait figure (§6.1) receives a
  `transform: translateY()` from the shared loop: as the entry
  crosses the viewport, the figure's offset moves from +1px (entry
  low) through 0 (centred) to −1px (entry high) — a total travel of
  2px against the static column rules behind it. Transform only; no
  layout is touched; the caption does not drift (it belongs to the
  page, the portrait to its frame).
- **Motion spec.** Continuous scrub, `--lerp: 0.06` in the shared
  rAF loop. The offset is a pure function of the entry's viewport
  position, clamped to ±1px, with no easing curve of its own — the
  lerp is the easing. It runs only while the entry is within one
  viewport height of the screen; off-screen entries cost nothing.
- **Choreography timeline (v2).** Entry approaches → drift begins at
  +1px as the portrait enters the lower viewport → 0 at centre (where
  §6.7's light settles — the two effects coincide at the moment of
  attention) → −1px as it leaves upward → loop disengages the entry.
  No beats, no triggers: a continuous 2px sigh across the pass.
- **State matrix (v2).** *Rest:* offset is positional, so "rest" is
  wherever the entry sits. *Hover:* §6.9 adds contrast; the drift is
  unaffected. *Focus:* unaffected. *Active:* n/a. *Scrolled-past:*
  the entry rests at −1px until it leaves the loop's range, then the
  transform is removed (offset 0 in the static document — a 1px
  difference no state depends on). *Disabled:* no transform; the
  portrait sits in its frame, correct. Touch identical.
- **Content merge.** The drift is measured *against the portrait's
  own column rules* — the frame moves within the entry's own
  architecture, not against the page background. It is the portrait
  breathing inside its setting, and it carries no content because it
  is a property of the portrait itself.
- **Failure fallback.** If the loop fails, transforms are simply
  never applied; the static layout is the fallback and is pixel-
  identical to the drift's midpoint. There is no broken state
  available to this element.
- **Reduced-motion variant.** Removed entirely — transform never
  applied. The portrait is still. (Stillness, here, is not a
  compromise.)
- **Breakpoints (v2).** All sizes: ±1px. At <768px the column rules
  sit at the viewport edges, so the drift reads against the frame's
  own hairline ring instead — the travel stays 2px; the reference
  changes, the restraint doesn't.
- **Edge cases & failure modes (v2).** *Sub-pixel rendering:* on
  1× displays 1px steps may quantise to a faint shimmer; the lerp's
  slowness (0.06) keeps step frequency below perception, and the
  gate (§10) checks a 1× display explicitly. *Entries without
  portraits:* nothing drifts — text never parallaxes in this theme.
  *Loop contention:* the drift shares the loop with §6.5 and §6.7;
  combined budget §14.
- **Accessibility spec (v2).** Motion-only, content-neutral; nothing
  to label. Vestibular safety is intrinsic (2px, slow) and the
  reduced-motion variant removes it anyway.
- **Performance budget & mobile variant.** One transform write per
  visible portrait per frame — ≤0.05ms. No cheaper variant exists or
  is needed.
- **Tokens consumed (v2).** `--lerp`.

### 6.7 Settling light

- **What & why.** The theme's only ambient loop, and barely one: as
  a portrait passes the centre of the viewport, a light settles on
  it — contrast +3% over 2 seconds, easing back as it leaves — as if
  the room quietened around the person being read. It is the feeling
  of attention, rendered as the smallest measurable change. If a
  reviewer cannot see it, it is working; if a visitor *can* see it
  clearly, it is 1% too strong.
- **Structure.** A contrast adjustment on the portrait image (§6.1's
  `<img>`), driven by the shared loop from the entry's distance to
  viewport centre: a bell curve peaking at centre (contrast 103%),
  falling to 100% at ±60% of viewport height. Implemented as a CSS
  custom property (`--settle`) updated by the loop and consumed by a
  `filter: contrast()` on the image only — never on the frame, the
  caption or the page. No overlay, no gradient, no glow: the light
  is *in* the photograph, the way attention is in the looking.
- **Motion spec.** Continuous, loop-driven, `--lerp: 0.06`. Rise and
  fall each take ≈2s at reading scroll speed because the bell is
  wide; a fast scroll compresses the settle proportionally — the
  light follows attention, and hurried attention is brief. The loop
  applies the filter only while |Δ| from the last frame exceeds
  0.1%, so a centred, stationary portrait costs zero writes.
- **Choreography timeline (v2).** Portrait enters lower viewport →
  contrast 100% → crosses 60% line → begins to gather (101%) →
  centre → 103%, held while the reader dwells (this is the loop's
  resting state — the light *stays* for a reader who stays) →
  scroll resumes → eases back through 101% → 100% at the upper 60%
  line → loop disengages. There is no start or end event; there is a
  geography of regard.
- **State matrix (v2).** *Rest (off-centre):* 100%. *Hover:* §6.9's
  +4% composes with the settle multiplicatively (a centred, hovered
  portrait reaches ≈107% — the one moment the theme permits a face
  to be *looked at properly* in full). *Focus:* focusing an entry's
  link does not summon the light; attention from a keyboard is
  §6.9's rule, not this glow. *Active:* n/a. *Scrolled-past:* 100%,
  filter removed. *Disabled:* 100% forever — the printed photograph.
  Touch identical (touch has no hover composition; the settle alone
  applies).
- **Content merge.** The light falls on the portrait being read and
  nowhere else; it is a property of the act of reading, applied to
  the object read. It decorates nothing — remove the reader and it
  does not run.
- **Failure fallback.** Filter unsupported or loop stalled: contrast
  stays 100%. The element's failure state is indistinguishable from
  its rest state, which is the correct failure design for an effect
  defined by near-imperceptibility.
- **Reduced-motion variant.** Off. The portrait is at 100% at all
  positions. (The reduced-motion page is, as the original entry
  says, this theme's own ideal — the variant and the theme nearly
  coincide.)
- **Breakpoints (v2).** Identical at all sizes; at <768px the bell
  narrows (±50% of viewport height) because a phone's portrait
  occupies more of its viewport and the settle would otherwise peak
  while the entry is still arriving.
- **Edge cases & failure modes (v2).** *Develop in progress (§6.1):*
  the settle does not run during the develop — the filters compose
  on the same property chain and the develop owns it; the settle
  arms only after the develop's final class lands. *Two portraits
  near centre simultaneously:* impossible in the procession's rhythm
  (entries are separated by full-viewport pauses) — the layout is
  the guard. *Photograph already at extreme contrast:* the +3% is
  relative; the gate checks one high-contrast portrait so the settle
  never clips a face into paper or ink.
- **Accessibility spec (v2).** No content, no state, nothing to
  announce. The 3% ceiling keeps the effect below any photosensitive
  threshold by orders of magnitude; it never flashes, pulses or
  repeats — it follows the reader's own hand.
- **Performance budget & mobile variant.** One filter write per
  visible portrait per frame while scrolling; filters on a single
  ≤300px image are the loop's largest cost and still ≤0.3ms/frame.
  Mobile: same, on a smaller image.
- **Tokens consumed (v2).** `--lerp`, `--settle` (element-scoped).

### 6.8 Quiet figure fades

- **What & why.** Years of service, family counts, ages, terms of
  office — the numbers inside a life — simply fade to their figure
  when their line is reached. No counting, no odometer, no spectacle:
  on this page a number is a fact, and facts are stated, not
  performed. This element exists largely as a *refusal with a
  mechanism*: it gives builders the sanctioned way to bring numbers
  in, so that no one improvises a count-up (§9's named failure).
- **Structure.** Figures are `<span class="figure">` inside the
  life's prose (and inside §6.14's register), each observed
  individually; when a figure's line crosses 80% of viewport height
  it fades opacity 0→1 over 800ms `--ease-settle`. The figure is
  real text in the HTML from the start — the fade is an opacity on
  text already laid out, so line breaks never shift.
- **Motion spec.** 800ms fade, once per figure per page-load,
  latched. Figures in the same line fade together (one trigger per
  line, not per digit); figures never stagger — a stagger would be a
  rhythm, and rhythm here would be showmanship.
- **Choreography timeline (v2).** Line crosses 80% → fade 0–800ms →
  figure at rest, indistinguishable from the surrounding prose
  except that it arrived last. Within an entry's life step (§6.2),
  figures in the first viewport of the life ride the life's own fade
  and do not double-trigger.
- **State matrix (v2).** *Rest (below trigger):* present in layout,
  opacity managed by JS only after arming (the raw document shows
  all figures — the pre-state is applied at observer-arm time,
  milliseconds before it can matter). *Hover/focus/active:* none —
  figures are not controls. *Scrolled-past:* faded in, latched.
  *Disabled:* printed numbers. Touch identical.
- **Content merge.** The figure is a word in the sentence that
  carries it ("She served the school for **41 years**"). The fade
  happens to the fact inside its own clause; nothing is extracted
  into a stat block, ever (§9 forbids the stat block outright on
  this page).
- **Failure fallback.** Observer failure → figures simply visible
  (pre-states are JS-applied; no JS, no pre-state, no problem). The
  per-entry watchdog (§6.2) also sweeps figures.
- **Reduced-motion variant.** Figures are present. Full stop.
- **Breakpoints (v2).** Unchanged at all sizes.
- **Edge cases & failure modes (v2).** *A life dense with figures:*
  each line triggers independently; a long service record may fade
  six figures across its length — acceptable, because each arrives
  at its own line's reading moment. *Figures in the register
  (§6.14):* the register is an index, set dense; its figures do NOT
  fade (an index is apparatus, not a life) — the one context where
  this element is switched off, stated here so no builder "fixes"
  it. *Numbers in dates:* governed by §6.3, not this element.
- **Accessibility spec (v2).** Figures are ordinary text to AT at all
  times (opacity is not `aria-hidden`). Tabular figures (§3) keep
  screen magnification users from losing their place to shifting
  widths — the fade never changes layout.
- **Performance budget & mobile variant.** Opacity transitions on
  text spans; beneath measurement. No mobile variant.
- **Tokens consumed (v2).** `--ease-settle`, `--ink`.

### 6.9 Looked-at-properly hover

- **What & why.** The theme's hover, and its whole philosophy of
  interaction in one gesture: hovering a portrait gives it a
  fraction more contrast — +4% over 400ms — as if looked at
  properly, and the entry gains a hairline violet rule. No tilt, no
  lift, no shadow: stillness is respect, and a portrait that leans
  toward the cursor has forgotten where it is. The response to
  attention is attention returned, nothing more.
- **Structure.** On the entry (`<article>`) hover/focus-within: the
  portrait image's contrast transitions to 104% (composing with
  §6.7 per its matrix), and a 1px violet rule (`--violet`, width of
  the measure) fades in beneath the name — implemented as a
  `border-bottom` colour transition on the name's block from
  transparent to `--violet` at 60%, so no element is added or moved.
  On touch, the same state is bound to the entry's first tap on its
  expansion line (§6.10) — touch gets the rule without the contrast
  (a finger is not a gaze).
- **Motion spec.** Contrast 400ms `--ease-settle` in, 500ms out (the
  look lingers a fraction after it leaves — a held glance, then
  released). The violet rule fades 400ms in, 400ms out. Nothing
  scales, translates or rotates; the gate measures transforms on
  hover and fails any nonzero value.
- **Choreography timeline (v2).** Pointer enters entry → t+0:
  contrast begins → t+120ms: the rule begins (the eye finds the name
  after the face) → t+400: both settled → pointer leaves → rule
  fades (400ms), contrast releases over 500ms → entry at rest. A
  pointer crossing quickly (under 120ms dwell) triggers neither —
  a passing glance is not a look, and the theme does not reward
  skimming with response.
- **State matrix (v2).** *Rest:* contrast at §6.7's positional value,
  no rule. *Hover (desktop):* as specced. *Focus:* keyboard focus on
  any control within the entry applies the rule and +2% contrast
  (focus is attention at half strength — the full +4% is reserved
  for the pointer's sustained look) plus the standard visible focus
  outline on the control itself (§6.10/§6.16 specs). *Active:* the
  expansion's press is flat (§6.10); hover states do not change.
  *Scrolled-past:* hover still functions — a life already read may
  be looked at again. *Disabled:* no hover response; the entry is
  print. *Touch:* rule-only, on tap, per Structure.
- **Content merge.** Both responses land on the entry's own materials
  — its portrait's contrast, its name's rule. The violet rule is the
  flower colour spent on *regard*, one of its two sanctioned uses
  (§2's ration counts it: hover rules are transient and exempt from
  the static ration, but a build may not make the rule permanent to
  circumvent it).
- **Failure fallback.** No JS is required — the hover is pure CSS;
  its failure mode is absence. The violet rule's colour transition
  degrades to an instant rule in engines without transitions, which
  is acceptable print behaviour.
- **Reduced-motion variant.** The rule and contrast apply instantly
  (no transition) — state without motion, information identical.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced. <768px:
  hover does not exist; the tap-bound rule applies, and the contrast
  composition is skipped (touch scroll already runs §6.7).
- **Edge cases & failure modes (v2).** *Hover during the develop
  (§6.1):* the develop owns the image's filters; hover's contrast
  queues and applies only after the develop completes — a face being
  developed is not yet being looked at. *Rapid in-out flicker:* the
  120ms dwell threshold plus transition reversal from current value
  (never a restart) keeps the response calm. *Entries without
  portraits:* the rule still applies on hover; the contrast has no
  target and is skipped — the name receives the regard.
- **Accessibility spec (v2).** Hover adds no information — everything
  the rule "says" (this entry is attended) is presentational.
  Focus parity is specified above so keyboard regard is honoured at
  half strength rather than ignored. Contrast change is on a
  photograph, not text; text contrast is untouched at all states.
- **Performance budget & mobile variant.** Two CSS transitions; zero
  loop cost. Mobile variant: the tap-bound rule in Structure.
- **Tokens consumed (v2).** `--violet`, `--ease-settle`.

### 6.10 "In lieu of flowers" expansion

- **What & why.** Every entry ends with the traditional line —
  "In lieu of flowers:" — pointing to the person's cause. Clicking
  it expands the cause quietly: a fade and a few lines, nothing more.
  It is the theme's one accordion, its one conversion-adjacent act on
  the procession itself, and it is deliberately the smallest possible
  version of both: the entry's own final line opening, the way the
  printed form always implied it could. For the living version of
  the theme (§1), the same line carries the tribute's chosen charity,
  fund or instruction — repurposed, never renamed into marketing.
- **Structure.** The closing line is a `<button class="in-lieu">`
  styled as the life's own last line of text (Source Serif 18px,
  ink, with a hairline violet underline at rest — its second
  sanctioned violet use) followed by a region (`<div
  class="cause">`) holding 2–4 lines: the cause's name, one sentence
  of the person's own connection to it, and a plain text link to the
  cause. The region sits on a `--violet-pale` wash — the page's only
  tinted surface — with 20px padding, inside the entry's measure.
  Height animates via grid-rows (0fr→1fr) with opacity; the content
  is in the DOM, `hidden` until first expansion only in the no-JS
  sense described under Fallback.
- **Motion spec.** Expand: 500ms `--ease-settle` — opacity 0→1 and
  height together, no overshoot, no slide of surrounding content
  beyond the region's own growth (the following pause absorbs the
  layout shift because the pause is viewport-relative emptiness —
  the one place in the library where an expansion displaces
  nothing). Collapse: 400ms, the same curve reversed. One entry's
  cause may be open at a time per viewport, but opening another does
  not slam the first — each keeps its own state; restraint includes
  not tidying up after the reader.
- **Choreography timeline (v2).** Click/tap/Enter → t+0: region
  begins (opacity leads height by a hair — content is perceptible
  from t+80ms) → t+500: settled; the cause's link is focusable from
  t+0 (focus is never held hostage to an animation) → the button's
  `aria-expanded` flips at t+0, not at completion. Collapse mirrors.
  If the reader scrolls away mid-expansion, it completes off-screen;
  states are per-entry and patient.
- **State matrix (v2).** *Rest (closed):* the line, its violet
  hairline, nothing else. *Hover:* the underline deepens to full
  `--violet` (400ms) — the §6.9 regard, applied to the line.
  *Focus:* visible focus — the underline thickens to 2px and a 2px
  `--violet` outline offsets 3px; this is one of the page's two
  interactive patterns and its focus must be unmistakable.
  *Active:* flat — no depression, no scale; the line darkens to full
  ink for the press duration. *Open:* the wash, the lines, the link;
  the button now reads as the region's heading and its underline
  retires. *Scrolled-past:* state persists per entry. *Disabled
  (no JS):* the cause is rendered **expanded, always** — print shows
  the whole entry; the collapse is the enhancement. Touch identical,
  with a 44px minimum target on the line (its padding box, not its
  glyphs).
- **Content merge.** The expansion is the entry's own closing line
  fulfilling its printed promise. The cause is not a related-links
  module; it is the last fact of the life, and it opens inside the
  life.
- **Failure fallback.** No-JS = expanded (above). With JS, if the
  height animation faults, the region snaps open — a watchdog on the
  transition forces the final state at 600ms. The link inside works
  in every state including mid-animation.
- **Reduced-motion variant.** Instant open/close, no fade, no height
  animation — the wash and lines are simply there or not. Information
  identical.
- **Breakpoints (v2).** All sizes as specced; at <768px the wash
  bleeds to the column rules (full measure width, padding 16px) —
  the one surface allowed to touch the rules, because a phone's
  measure is narrow enough that the inset wash would cramp the
  cause's sentence.
- **Edge cases & failure modes (v2).** *No cause recorded:* the line
  reads "In lieu of flowers:" followed by the family's stated wish
  in plain text ("the family asks that you simply remember her") —
  if there is no wish either, the line is omitted entirely; an empty
  expansion is never shipped. *Long cause text:* capped at 4 lines
  by editorial rule (§12); the region never scrolls internally — a
  cause that needs more room gets its own page, linked. *Multiple
  rapid toggles:* transitions reverse from current value; the state
  machine is a boolean, not a queue.
- **Accessibility spec (v2).** A real `<button>`, `aria-expanded`,
  `aria-controls` to the region; region is `role="region"` with
  `aria-label` = the cause's name. Focus order: the line → (when
  open) the cause link → the next entry. The wash's contrast: ink on
  `--violet-pale` is 14.8:1 ✓; the link inside is ink with the violet
  underline — never violet text on the pale wash (5.9:1, and reserved
  by ration besides).
- **Performance budget & mobile variant.** One grid-rows + opacity
  transition per toggle; zero loop cost. Mobile: the full-measure
  wash above.
- **Tokens consumed (v2).** `--violet`, `--violet-pale`, `--ink`,
  `--ease-settle`.

### 6.11 Discreet lives progress

- **What & why.** The foot margin carries "lives, n of N", updating
  per entry passed, beside the floral rule. Never a percentage,
  never a bar: the count is in the page's own voice, at the page's
  own margin, in the apparatus type of a register that knows how
  many names it holds. It answers the reader's one legitimate
  positional question — how many lives are in this procession, and
  how far through them am I — in the grammar of a printed index.
- **Structure.** A `<footer class="foot-margin">` line, fixed to the
  viewport's bottom-left margin on ≥1200px (in-flow at the page's
  foot on smaller screens), set in the foot-margin style (§3):
  "LIVES, 4 OF 23", 12px, letterspaced, `--grey`, with a miniature
  complete floral rule (static SVG, 60px) to its left. The count
  updates from the sequencer's latch (§6.2): n = entries whose
  sequence has completed; N = entries in the register. Both numbers
  are counted from the DOM at load — an invented or hard-coded total
  is a gate failure (§10), because a register that miscounts its
  dead has failed at its only arithmetic.
- **Motion spec.** The numeral changes with a 600ms crossfade
  (`--ease-settle`) when an entry settles — the count arrives as
  quietly as the life did. No rolling digits, no ticking: the
  crossfade is a page of the register being turned in the margin.
  Updates are batched to entry-settle events only; scrolling itself
  never moves the number.
- **Choreography timeline (v2).** Entry sequence completes (§6.2's
  t+4800) → the margin crossfades n→n+1 over the following 600ms →
  at rest. If several entries settle during one fast scroll, the
  count crossfades once, directly to the true n — intermediate
  values are never displayed, because the margin reports the
  reader's position, not the scroll's history.
- **State matrix (v2).** *Rest:* the current count, static. *Hover/
  focus/active:* not interactive; hovering it does nothing and it
  takes no focus. *Scrolled-past:* n/a — the margin is the reader's
  companion at every position. *Disabled (no JS):* the margin shows
  "LIVES, 23" — the register's size without the reader's position,
  which is the honest static form (print cannot know where you are).
  Touch identical.
- **Content merge.** The count is part of the page's apparatus — the
  register totalling itself in its own margin. It is not a widget
  overlaid on the content; it sits in the margin the layout reserved
  for it (§4), in the margin's own type.
- **Failure fallback.** If the sequencer fails, the margin falls
  back to the static "LIVES, N" form (the disabled state) — a count
  that cannot update must never display a wrong position.
- **Reduced-motion variant.** The numeral changes instantly, without
  the crossfade.
- **Breakpoints (v2).** ≥1200px: fixed in the bottom-left margin,
  clear of the column (the margin exists because the measure is
  centred — §4). 768–1199px: fixed bottom-right, smaller presence,
  same type. <768px: not fixed — it appears in-flow after every
  fifth entry and at the foot, because a phone has no margin to
  lend and a fixed count would sit on the text. The in-flow
  instances are static snapshots of the count at their position.
- **Edge cases & failure modes (v2).** *Single-entry pages (detail
  view, §7):* the margin reads "LIVES, 1 OF 1" or is omitted by the
  page template — the detail template omits it (§6.14's register is
  the way back). *Register grows while reading (a name added
  mid-session on a live platform):* N is fixed at page load; a
  refresh recounts. The margin never lies retroactively. *n reaching
  N:* the final settle crossfades to "LIVES, 23 OF 23" and the
  closing floral rule (§6.17) is drawn complete — the only
  "completion state" the theme permits itself, and it is a sentence,
  not a celebration.
- **Accessibility spec (v2).** The margin is `aria-hidden` in its
  fixed form (position is visual furniture); the same information is
  available to AT in the register (§6.14), where the index states
  the total and each entry's place. No live regions: a reader's
  progress through the dead is not announced.
- **Performance budget & mobile variant.** One crossfade per entry
  settle; DOM count at load is O(entries). Mobile: the in-flow
  snapshots above.
- **Tokens consumed (v2).** `--grey`, `--ease-settle`.

### 6.12 Developing skeleton + white fade transition

- **What & why.** The theme's two state-changes, both performed in
  its own processes. Loading shows skeleton entries — an oval and
  grey lines — that *develop in* like the portraits, because even
  the page's waiting is done the page's way. Navigation is a long,
  respectful fade through white: the reader turns a leaf of the
  register, and for 700ms there is only paper. Neither state borrows
  a spinner, a shimmer or a progress bar from the generic web; a
  shimmer on this page would be a sequin on a coffin.
- **Structure.** *Skeleton:* entry-shaped placeholders in the real
  procession layout — oval (`--paper-deep` fill, hairline ring),
  name-line bar (Playfair-width grey block at 44px height), dates
  bar, four life-line bars at the measure — occupying the entries'
  true positions so arrival causes no shift. They develop via
  `--ease-develop` filter/opacity stages mirroring §6.1 (grey bars
  gather contrast over 1200ms — skeletons develop faster than
  portraits; they are paper, not people). *Transition:* a full-
  viewport `--paper` layer, opacity 0→1 (350ms) → route change →
  1→0 (350ms), with the destination's first entry already settled
  beneath it (no sequence replays on arrival by transition — the
  ceremony is for the procession, not for navigation).
- **Motion spec.** Skeleton develop: 1200ms `--ease-develop`, stages
  at the same proportions as §6.1. Skeleton display has a minimum of
  600ms (a flash of skeleton is worse than none) and a maximum of
  4000ms, after which the region shows the page's plain apology line
  (§12's error voice) in place of further waiting. Transition:
  700ms total, `--ease-settle`, and it never intercepts the back
  button's *history* — only its rendering; a transition that delays
  history is a trap, and traps are forbidden (§10).
- **Choreography timeline (v2).** *Load:* procession frame paints
  (dedication first — §6.13 is server-rendered and never waits) →
  skeletons develop (0–1200ms) → real entries replace them one by
  one as data lands, each arriving *settled* (a fetched life does
  not re-perform its sequence for having been fetched; its sequence
  runs on scroll-trigger as normal if it lands before being reached,
  or it is simply present if it lands in view — present wins over
  ceremony). *Navigation:* click → fade to paper (350ms) → swap →
  fade in (350ms) → focus moves to the destination's heading.
- **State matrix (v2).** *Skeleton rest:* developing grey entries.
  *Skeleton hover/focus:* skeletons are inert (`aria-hidden`,
  pointer-events none, unfocusable). *Transition active:* the paper
  layer is inert and unfocusable; the destination's focus target is
  set at swap, not before. *Disabled (no JS):* no skeleton (content
  is server-rendered or the page is static), navigation is the
  browser's own — both states vanish, which is correct: they are
  courtesies of the enhanced experience, not necessities.
  *Scrolled-past:* n/a.
- **Content merge.** Both states are the page's own materials —
  developing paper, a turned leaf. The skeleton is shaped like the
  entries it stands for, in their places, at their sizes; the
  transition's white is the page's own paper. Nothing generic is
  admitted.
- **Failure fallback.** Skeleton watchdog at 4000ms → apology line
  (§12) with a plain retry link; the dedication and any loaded
  entries remain usable throughout — a slow register never blanks
  the page. Transition failure (route error) → the fade reverses
  and the origin page stands, with the correction slip (§11) noting
  the failure in the page's voice.
- **Reduced-motion variant.** Skeleton: static grey entries, no
  develop (they still develop *out* — replaced — when content
  lands). Transition: instant swap, no fade; the leaf turns without
  being seen to turn.
- **Breakpoints (v2).** Skeleton geometry follows the entry layout at
  each size. Transition unchanged. At <768px the fade shortens to
  500ms total (a phone's leaf is smaller; the respect is in the
  pause, not the duration).
- **Edge cases & failure modes (v2).** *Partial data (some entries
  loaded, some not):* loaded entries render in place; skeletons
  remain only where their entries will be — the procession never
  reorders to fill gaps early, because order is editorial (§7).
  *Prefetch/back-forward cache:* restored pages show settled
  entries; the transition does not run on history restoration.
  *Very fast connections:* the 600ms skeleton minimum applies only
  when a skeleton was actually painted; sub-100ms loads never show
  one.
- **Accessibility spec (v2).** Skeletons `aria-hidden`; a single
  polite `aria-live` announcement "The register is being prepared"
  fires only if skeletons persist past 1200ms. Transition: focus
  management as specced; the fade is opacity-only and vestibularly
  negligible; reduced-motion removes it.
- **Performance budget & mobile variant.** Skeletons are pure CSS
  shapes (no images) — ≤2KB of markup per entry. The transition
  layer is one fixed div. Mobile: the 500ms fade above.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--grey`,
  `--hairline-strong`, `--ease-develop`, `--ease-settle`.

### 6.13 The standing dedication (page family: hero / head of procession)

- **What & why.** At the head of the procession stands the
  dedication — the page speaking in its own person, in italic,
  before any life is read: who this register is for, and in whose
  memory it is kept. It pins softly while the first entry approaches
  and then releases, the way a dedication page is turned past but
  never removed from the book. It is the theme's hero: not a banner,
  not a headline about the living, but the register's reason for
  existing, set at reading size.
- **Structure.** A `<header class="dedication">` at the procession's
  head: a hairline plaque (border `--hairline-strong`, padding 40px)
  containing the dedication in Source Serif italic 19px — typically
  2–4 lines, authored per register ("For the forty-one men and women
  of this parish who did not come home, and for those who waited for
  them.") — above a small apparatus line (the register's name and
  span, §3's foot-margin style). The pin is `position: sticky` at
  the head of the first pause; it releases (scrolls away naturally)
  when the first entry's name reaches the trigger line. No image,
  no portrait — the dedication precedes all faces.
- **Motion spec.** The pin is sticky, not animated: it holds while
  the first pause scrolls beneath it (the pause at the head is
  shortened to 60vh — the dedication occupies the rest) and releases
  without a transition. On load it fades in once, 800ms
  `--ease-settle`, after the masthead line — the page's first and
  quietest motion. It never re-pins, never follows the reader down
  the procession: a dedication that chased the reader would be a
  banner ad in mourning dress.
- **Choreography timeline (v2).** Load → masthead settles → t+200ms:
  dedication fades (800ms) → reader scrolls → dedication holds
  through the head pause → first name crosses 72% → dedication has
  already released by geometry (sticky range ends at the pause's
  foot) → procession proceeds; the dedication is behind the reader
  for the rest of the page, present in the document, absent from
  the screen — as in a book.
- **State matrix (v2).** *Rest (at head):* pinned, settled. *Hover:*
  none — it contains no controls in its procession form. *Focus:*
  its apparatus line may carry the register's index link (§6.14) on
  some templates; focus there is standard. *Active:* n/a.
  *Scrolled-past:* released, static at the document's head.
  *Disabled:* a static dedication at the head — print's own form.
  Touch identical.
- **Content merge.** The dedication is the register's frontispiece
  text, not a hero module: it states the page's purpose in the
  page's own italic voice, and its pin exists so that purpose is
  still in view at the moment the first life begins.
- **Failure fallback.** Server-rendered and static by default; the
  fade is the only enhancement and its absence is invisible.
- **Reduced-motion variant.** No fade; the dedication is present.
  The pin remains (sticky positioning is layout, not motion, and
  the release is the reader's own scroll).
- **Breakpoints (v2).** ≥1200px: plaque at the measure (620px),
  padding 40px. 768–1199px: padding 32px. <768px: plaque borders
  retire to top and bottom hairlines only (a full plaque crowds a
  phone), italic at 18px, head pause shortens to 40vh — the
  dedication on mobile is a paragraph at the head of a column, which
  is what it always was.
- **Edge cases & failure modes (v2).** *No dedication authored:* the
  element is omitted and the procession begins with its first pause
  at full height — a register may open plainly, but it may not open
  with a *substitute* hero (no stock imagery, no motto generator).
  *Over-long dedication:* editorial cap 4 lines (§12); a dedication
  that needs more is an essay and belongs on the about page (§7),
  linked from the apparatus line. *Detail pages (§7):* the
  dedication does not appear — a single life carries its own head.
- **Accessibility spec (v2).** The dedication is the page's first
  text after the masthead and is a normal paragraph to AT — read
  first, as intended. The pin is positional only; reading order is
  document order. Italic at 19px/1.65 keeps legibility for low-vision
  readers (the theme's only italic block, rationed partly for this
  reason).
- **Performance budget & mobile variant.** Static text and a sticky
  position; zero loop cost. Mobile: the borderless form above.
- **Tokens consumed (v2).** `--ink`, `--hairline-strong`,
  `--ease-settle`.

### 6.14 The register (page family: navigation / index of names)

- **What & why.** Every procession needs its index: the register is
  the alphabetical table of the names on the page — name, dates, and
  the entry's place — serving as both navigation and the theme's
  listing page. It is set as a printed index is set: two quiet
  columns of ruled lines, no photographs, no cards. A reader looking
  for one name should find it the way one finds a name in a book of
  remembrance: by letter, by line, without being shown anyone else's
  face on the way.
- **Structure.** A `<nav class="register">` / index page section: an
  alphabetical grouping (`A`, `B`, … as grey apparatus headings),
  each entry a single ruled row — name (Playfair 20px, a link to the
  entry or its detail page), dates (`--ink-soft`, tabular), and a
  hairline beneath. A quiet filter input at the register's head
  (§11) narrows rows by substring as the reader types — rows hide,
  letters with no remaining names retire, and the count line updates
  ("23 names" → "3 names"). Rows are links entire (the row is the
  target, 44px tall minimum).
- **Motion spec.** Almost none, deliberately: rows are present at
  rest. The filter's narrowing is instant (no fade — an index that
  animates its filtering is showing off at the wrong funeral), with
  one exception: a row arriving from a procession deep-link is
  marked by the §6.9 violet rule for 2s, so a reader sent to the
  index can find their place. Route changes out of the register use
  §6.12's white fade.
- **Choreography timeline (v2).** Register reached → all rows
  present (no sequence — §6.2's ceremony belongs to lives, not to
  the index of them) → typing in the filter → rows narrow per
  keystroke, count line updates at the same beat → row chosen →
  white fade (§6.12) → the entry, sequenced on arrival if the
  destination is the procession (scrolled to its name).
- **State matrix (v2).** *Rest:* all rows, hairlines at rest.
  *Hover (row):* the name gains the §6.9 hairline violet rule and
  the row's hairline deepens to `--hairline-strong` — regard, in
  the index's smaller voice; no contrast change (there is no
  portrait to regard). *Focus (row):* visible outline (2px
  `--violet`, offset 2px) — the register is the page's most
  navigated surface and its focus must be the clearest on the site.
  *Active:* the name darkens to full ink. *Visited:* the name sets
  in `--ink-soft` with a small "read" mark in the margin — a pencil
  tick in the register's margin, the one place the theme permits a
  read-state. *Disabled:* a printed index; the filter is absent and
  all rows stand. Touch: rows are 48px, filter identical.
- **Content merge.** The register *is* the site's navigation and its
  sitemap in one printed object; there is no separate nav chrome to
  merge with. The masthead's quiet line (§4) links here ("The
  Register") and from here to everywhere.
- **Failure fallback.** No-JS: full index, no filter — the printed
  form. Filter script failure leaves all rows visible (hiding is
  JS-applied per keystroke; a failed script hides nothing).
- **Reduced-motion variant.** Identical; there was no motion to
  reduce except the deep-link mark, which applies instantly.
- **Breakpoints (v2).** ≥1200px: two columns of rows (the alphabet
  flows down, then across), measure 480px per column. 768–1199px:
  two columns at 340px. <768px: one column; letter headings sticky
  at the viewport top as their group scrolls (the index's one pin,
  sanctioned because an index is apparatus, not a life).
- **Edge cases & failure modes (v2).** *Very large registers
  (500+ names):* the register paginates by letter-range pages
  ("A–D", "E–K"…) linked in the apparatus voice — never infinite
  scroll (§11's pagination ruling). *Filter with no matches:* the
  empty state in §12's voice ("No life is entered under that name.")
  with the full count restored on clearing. *Duplicate names:* rows
  disambiguate by dates and, where needed, a middle line (place or
  relation) in caption style — the index must never merge two lives
  into one row.
- **Accessibility spec (v2).** A real `<nav>` with a list of links;
  letter headings are headings in the AT outline. The filter is a
  labelled search input ("Find a name in the register") whose result
  count is announced politely (`aria-live="polite"`, debounced
  300ms) — the one live region the theme permits, because a
  narrowing index is otherwise silent about its own state. Row
  targets ≥44px. The visited "read" mark is `aria-hidden` decoration
  over the link's own text.
- **Performance budget & mobile variant.** Rows are text; 500 rows ≤
  60KB of HTML. Filtering is a substring pass over row text, ≤1ms
  per keystroke at that scale. Mobile: the single column above.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--grey`,
  `--hairline`, `--hairline-strong`, `--violet`.

### 6.15 Remembrance cards (page family: cards / the guest book)

- **What & why.** Below a life — on its detail page, or after the
  procession on a platform build — sit the remembrances: short
  messages left by the living, set as cards the way condolence cards
  are laid on a table: one by one, in order of arrival, each signed.
  They are the theme's only user-generated surface, and the card
  form is chosen because a card can be *placed* — moderated, ordered,
  occasionally declined — where a comment thread can only accumulate.
- **Structure.** A `<ul class="remembrances">` of `<li
  class="card">`: hairline-bordered plaque (`--hairline-strong`),
  paper background, padding 24px; inside, the message (Source Serif
  16px/1.65, ink) and beneath it the signature line (caption style,
  grey: name, relation, date — "Margaret E., his sister, March
  2026"). No avatars (the dead have portraits here; the living have
  names), no like counts, no reply nesting — a card answers a life,
  not another card. Maximum measure matches the entry's.
- **Motion spec.** Cards arrive with the quietest version of the
  entry fade: as the remembrance section is reached, cards fade in
  600ms `--ease-settle`, staggered by 120ms in reading order — the
  one sanctioned stagger in the theme, because cards on a table are
  noticed one after another. No entrance from below, no scale: cards
  do not travel. Newly submitted cards (after §6.16's other form, or
  an approval) appear at the list's head of the *unmoderated* queue
  only; on the public list a card appears, settled, on next load —
  this page does not perform publishing.
- **Choreography timeline (v2).** Section top crosses 72% → card 1
  fades (0–600ms) → card 2 at +120ms → … → all settled; a list
  longer than six cards fades only the first six on arrival and
  shows the rest settled below (ceremony is rationed by the same
  law as violet). Scroll-back: latched, like lives.
- **State matrix (v2).** *Rest:* printed card. *Hover:* the card's
  border deepens to full `--grey` at 40% — the §6.9 regard at card
  strength; nothing else. *Focus:* cards are not focusable unless
  they carry a link (a cause link repeated, occasionally); then
  standard focus applies to the link. *Active:* n/a. *Scrolled-past:*
  settled. *Disabled:* printed cards. *Moderation state (platform
  builds):* a declined card is simply absent — the page never shows
  placeholders for removed speech. Touch identical.
- **Content merge.** The cards are the section's entire content —
  messages to a life, placed beneath it. They are not a widget
  appended to the entry; the entry's template ends with them the way
  a condolence book sits at the register's side.
- **Failure fallback.** Static list; the stagger is JS-armed only.
  If the platform's card feed fails, the section shows the §12
  apology line and the life above it is unaffected — a failed guest
  book never takes the life down with it.
- **Reduced-motion variant.** Cards present, no stagger, no fade.
- **Breakpoints (v2).** ≥1200px: cards at the entry measure, one per
  row (never a grid — condolence cards are not tiles). 768–1199px:
  same. <768px: padding 20px, message 16px kept (grief does not
  shrink its type for phones).
- **Edge cases & failure modes (v2).** *Very long messages:*
  editorial cap (§12, ~60 words) enforced by the form, not by
  truncation — a card is never shown cut off with a "read more";
  what cannot be said in sixty words is a letter, and letters are
  sent privately. *Many cards (100+):* paginated in tens with the
  apparatus pagination (§11), newest first by *approval* order.
  *Abuse:* moderation is a product requirement (§1's warning); the
  theme contributes the form's quiet friction — no anonymity, the
  signature line is required and shown.
- **Accessibility spec (v2).** A list, read in order; the signature
  line is part of each card's text. The section heading ("Remembrances")
  is a real heading. No interactive elements to label in the base
  form.
- **Performance budget & mobile variant.** Text cards; ten per page
  ≤ 15KB. No images ever — a build that adds avatars or photos to
  cards has left the theme. Mobile: the padding above.
- **Tokens consumed (v2).** `--ink`, `--grey`, `--hairline-strong`,
  `--ease-settle`.

### 6.16 The inscription form (page family: forms / conversion)

- **What & why.** The theme's conversion, and it is not a sale: the
  inscription form is where a life is *entered* into the register —
  a family submits a name, its dates, the life's text and a portrait
  — or, in its smaller variant, where a remembrance card (§6.15) is
  written. The form is designed as an act of record: ruled lines
  instead of boxes, the apparatus voice for labels, and a
  confirmation that reads like an entry being made in the book —
  because it is one.
- **Structure.** A single column at the entry measure. Fields in the
  register's fixed order — the name; the dates (two year fields with
  the em dash printed between them, §6.3's dash as static print);
  the life (a textarea ruled like a page, min-height for ~10 lines);
  the portrait (a file field styled as a plain instruction line);
  the closing line (the "In lieu of flowers" cause); the inscriber's
  own name and relation (the signature). Inputs are bottom-ruled
  lines only (`--hairline-strong` → `--ink` on focus), transparent
  background, Source Serif 18px. The submit is a hairline-bordered
  plaque-button: "Enter this life in the register" — the verb is
  *enter*, the theme's own (§12). A note above the form, in caption
  style, states the editorial fact plainly: entries are reviewed
  before they appear (§1's moderation law), so no one expects the
  procession to change the moment they submit.
- **Motion spec.** Focus: the field's rule deepens over 200ms and
  its label settles from grey to ink (200ms `--ease-settle`) — the
  register acknowledging where the pen is. Error: the offending
  field's rule turns `--violet` (the flower colour spent on
  correction — its third sanctioned use) and the error line appears
  beneath in the §12 error voice, fading 300ms. Submit: the button
  does not spinner; the form's head gains the line "Entering…" set
  as apparatus text, and on success the whole form is replaced by
  the confirmation (below) through §6.12's white fade at half length
  (350ms) — a leaf turned within the form.
- **Choreography timeline (v2).** Submit pressed → t+0: button
  disabled, "Entering…" appears → server round-trip → success:
  fade to paper (350ms) → confirmation stands: the entered name set
  as an entry's name (Playfair 34px), its dates with the dash drawn
  (800ms, §6.3 — the form's one ceremony), and the italic line:
  "This life has been received. It will appear in the register once
  it has been read." → a plain link, "Return to the register".
  Failure: no fade; the correction slip (§11) appears at the form's
  head and focus moves to the first error.
- **State matrix (v2).** *Rest:* ruled lines, grey labels. *Focus:*
  as specced, plus the standard visible focus (the deepened rule and
  label — the field itself is the indicator; no outline box, which
  would be chrome on a register page; the gate verifies the focus is
  unmistakable by the rule's full-ink weight and label change
  together). *Filled:* the rule stays at 60% ink — a completed line
  on a form is darker than an untouched one. *Error:* violet rule +
  error line, persistent until corrected (errors never time out on
  a form of record). *Submitting:* fields disabled, button flat with
  its label unchanged (the "Entering…" line carries the state).
  *Disabled (no JS):* a plain HTML form posting to the server, which
  re-renders with errors in the same voices — every enhancement is
  progressive over that form.
- **Content merge.** The form is a leaf of the register being filled
  in; its order is the entry order (§6.2's law applied to data:
  name → dates → life → portrait → closing line), so the inscriber
  composes the entry in the genre's own sequence. The confirmation
  is the entry's first appearance — as a receipt, in miniature.
- **Failure fallback.** Server-rendered form as above; client
  validation is a courtesy layer only. A failed submission preserves
  every field's content (a form that loses a family's written life
  to a network error has committed the theme's worst possible fault;
  the gate tests it by killing the connection mid-submit).
- **Reduced-motion variant.** Focus/error states apply instantly;
  the confirmation appears without the fade; the dash in the
  confirmation is printed, not drawn.
- **Breakpoints (v2).** ≥1200px and 768–1199px: the entry measure.
  <768px: full measure minus the column-rule insets; the two year
  fields stay side by side with the printed dash between them (the
  dates are one fact and are never stacked); textarea min-height
  grows to 12 lines (phones are written on slowly).
- **Edge cases & failure modes (v2).** *Portrait upload failure:*
  the entry may be submitted without it (§6.1's missing-photograph
  path) — the error voice offers the choice plainly, never blocking
  the life on its picture. *Dates in the future / death before
  birth:* field-level errors in §12's voice, checked client- and
  server-side; the form never silently corrects a year. *Very long
  life text:* the textarea counts lines quietly in caption style
  ("about 240 words — the register's entries run 150 to 300") as
  guidance, never a hard character wall mid-composition; the
  editorial review is the real limit. *Duplicate entry (same name
  and dates already in the register):* the confirmation step
  surfaces the existing entry and asks — in the page's voice —
  whether this is the same life, before anything is written.
- **Accessibility spec (v2).** Every field has a real `<label>`;
  errors are linked to fields with `aria-describedby` and announced
  by moving focus to the error summary on failed submit (the one
  focus-move the theme performs uninvited, because a family must not
  hunt for what is wrong). Required fields are marked in the label
  text ("(required)" in caption style), never by asterisk alone.
  Touch targets: fields' hit areas ≥48px tall. Contrast: entered
  text is `--ink` on `--paper` (15.9:1 ✓); labels at rest are
  `--grey` 14px-equivalent apparatus — set at 12px letterspaced,
  which fails AA for small text on paper (5.1:1 passes AA normal at
  ≥14px; at 12px it does not) — therefore labels are set in
  `--ink-soft` (9.8:1 ✓) and grey is used only for the optional-field
  annotations. This is a ruling, not a suggestion: the gate checks
  label colour tokens.
- **Performance budget & mobile variant.** The form is HTML and
  rules; the only weight is the portrait the inscriber uploads
  (guided to ≤2MB at the field, compressed server-side to §6.1's
  budget). Mobile: the layout above.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--grey`,
  `--violet`, `--hairline-strong`, `--ease-settle`, `--ease-draw`.

### 6.17 The foot of the register (page family: footer)

- **What & why.** The procession ends the way a register ends: with
  the count, the rule drawn complete, and the colophon of who keeps
  the book. The footer is not a sitemap with a memorial skin; it is
  the last page of the register — the final floral rule (always
  complete, §6.5's closing instance), the lives count stated in full
  ("23 lives are entered in this register."), the dedication's echo
  in one line, and the keeping institution's plain imprint.
- **Structure.** Centred on the measure, after a final full pause:
  the complete floral rule (static SVG, drawn); the count sentence
  (Source Serif 18px, ink); one italic line (the register's
  closing words, authored — often the dedication's last clause);
  then the apparatus block in foot-margin style: register name,
  keeper, place, year span, and three text links at most (The
  Register, Enter a life, About this page) with §6.9-style hairline
  underlines. Nothing else. No newsletter, no social row, no "back
  to top" — the top of this page is not a place readers are hurried
  back to.
- **Motion spec.** The foot fades in as one block, 600ms
  `--ease-settle`, when its rule crosses the 72% line — the
  procession's last ceremony, identical in kind to an entry's
  arrival. The rule does not draw (it is the closing rule; §6.5's
  scrubbed rules live between lives, this one is printed complete,
  because the book is finished).
- **Choreography timeline (v2).** Final entry settles → final pause
  (empty; no rule inside it — the absence tells the reader the
  procession has ended before the foot confirms it) → foot crosses
  72% → block fades (600ms) → §6.11's margin, if fixed, rests at
  "LIVES, N OF N" → the page is at rest, permanently. Nothing on
  this page moves after the foot arrives; the stillness is total
  and is the ending.
- **State matrix (v2).** *Rest:* printed foot. *Hover (links):* the
  hairline underline deepens to violet, 400ms (§6.9's regard in the
  apparatus voice). *Focus:* standard visible outline on links.
  *Active:* flat. *Scrolled-past:* n/a — there is no past. *Disabled:*
  identical. Touch identical.
- **Content merge.** The foot is the register's own last page; its
  count sentence is data (§6.11's N, counted from the DOM), its
  italic line is the dedication's family, its imprint is the
  keeper's legal presence in the book's own form.
- **Failure fallback.** Static block; the fade is JS-armed only. If
  the DOM count is unavailable, the count sentence is omitted rather
  than estimated — the foot never prints a number it cannot stand
  behind.
- **Reduced-motion variant.** Present without the fade.
- **Breakpoints (v2).** All sizes centred on the measure; at <768px
  the apparatus block stacks its lines (it already sets one fact per
  line) and the links go full-width rows of 48px.
- **Edge cases & failure modes (v2).** *Empty register (no lives
  yet):* the foot follows the dedication directly and the count
  sentence reads per §12's empty voice. *Platform builds with legal
  requirements:* privacy/terms links join the apparatus block as
  plain text links — admitted as print, refused as chrome.
- **Accessibility spec (v2).** A real `<footer>`; the count sentence
  is ordinary text (AT readers receive the register's size here,
  complementing §6.11's aria-hidden margin). Links are links, in
  order, with the focus spec above.
- **Performance budget & mobile variant.** Static. Mobile: the
  stacked apparatus above.
- **Tokens consumed (v2).** `--ink`, `--grey`, `--violet`,
  `--ease-settle`.

### 6.18 The unwritten page (page family: 404)

- **What & why.** A name sought and not found, a link that leads
  nowhere: the theme's 404 is a page of the register that has not
  been written — paper, the column rules, and a short statement in
  the page's voice. It refuses the genre's jokes entirely (no "this
  page has died" — the gate greps for it, §9): on a site about the
  dead, a missing page is a small absence and is treated with the
  same plainness as the large ones.
- **Structure.** The procession's frame without an entry: masthead
  line, then centred at the measure — a heading in Playfair 34px,
  "This page has not been written."; two lines of Source Serif
  explaining plainly (the name may not yet be entered; the link may
  be old); and two apparatus links — "The Register" (§6.14) and
  "Enter a life" (§6.16) — the only two useful directions from an
  absence. A single floral rule, printed complete, beneath. The
  pause rhythm is preserved: the 404 occupies one viewport, quietly.
- **Motion spec.** One 600ms fade on arrival (`--ease-settle`), via
  §6.12's transition if navigated to in-app. Nothing else — an error
  page with animation would be a page enjoying itself.
- **Choreography timeline (v2).** Arrival → fade (0–600ms) → rest.
  No sequence (there is no life to sequence), no develop, no rule
  draw.
- **State matrix (v2).** *Rest:* the statement and links. *Hover/
  focus (links):* §6.17's link behaviour. *Active:* flat.
  *Scrolled-past:* the page is one viewport; n/a. *Disabled:*
  identical — the 404 must work with nothing at all, being the page
  shown when things have already gone wrong once.
- **Content merge.** The 404 is a leaf of the same register — same
  paper, rules, type and voice — so a lost reader is still *in* the
  book, one page early.
- **Failure fallback.** The page is its own fallback: static HTML,
  no JS required for any part of it.
- **Reduced-motion variant.** No fade; present.
- **Breakpoints (v2).** All sizes: centred at the measure; at
  <768px the heading sets at 28px.
- **Edge cases & failure modes (v2).** *A sought name that exists
  under another spelling:* where the platform can suggest it, one
  line is added in caption style ("There is an entry for —" with
  the link) — the theme's only search-suggestion, stated plainly,
  never as a playful "did you mean". *Soft 404s are forbidden:* a
  missing entry must return a true 404 status; the register does
  not pretend.
- **Accessibility spec (v2).** The heading is the page's `<h1>`; the
  statement is text; links are the focus order. The page announces
  itself honestly to AT as an error via its heading text — no
  special chrome needed.
- **Performance budget & mobile variant.** The lightest page on the
  site; no images. Mobile: the heading size above.
- **Tokens consumed (v2).** `--ink`, `--grey`, `--violet`,
  `--ease-settle`.

## 7. Page application map

- **Home — the procession.** Masthead line → standing dedication
  (§6.13) → head pause (60vh) → entries (§6.2) separated by pauses
  (§6.4) with their floral rules (§6.5) → the invitation to inscribe
  (one apparatus line linking §6.16, placed after the last entry —
  never between lives) → foot of the register (§6.17). The home page
  *is* the register read straight through; platforms with many lives
  show the current register in full and let the procession be long —
  length is not a defect on a page whose subject is accumulated
  lives. Pagination, if the register is vast, breaks *between*
  processions ("Earlier lives" in the apparatus voice) and never
  mid-entry.
- **Listing — the register (§6.14).** The index of names is the
  listing page. There is no card-grid alternative; a platform that
  needs browsing by decade or place adds those as *apparatus
  groupings within the register* (a decade heading in the same ruled
  rows), never as a different visual species.
- **Detail — a single life.** One entry, given the whole page: the
  sequence (§6.2) runs once at load (name → dates → portrait → life,
  the reader having come *for* this life), the remembrances (§6.15)
  beneath, the "In lieu of flowers" expansion (§6.10) in place, and
  the register as the way back (the foot margin shows no count;
  §6.11's ruling). The dedication does not appear. The detail page
  is where a life is *visited*; its URL is the one families keep.
- **About — the keeping of the register.** The dedication's long
  form: who keeps this book, how a life is entered and read before
  it appears (§6.16's editorial law stated fully), the sources of
  the facts. Set as a single life-column of prose with the same
  typography; the about page is written in the dedication's italic
  only for its opening paragraph — a whole page of italic would
  spend the voice. One portrait is permitted (the register's house,
  its first keeper) and it develops (§6.1) — the theme's processes
  apply to the living subjects of the about page too, which is the
  theme quietly stating that its gravity is a form of respect, not
  a property of death.
- **Contact / conversion — the inscription form (§6.16).** Reached
  as "Enter a life" everywhere. The smaller remembrance variant
  (name, relation, message, signature) lives on detail pages beneath
  §6.15. There is no checkout; where a platform charges for
  inscription or upkeep, payment is a separate, plainly-labelled
  step *outside* the form's leaf — commerce never shares a page with
  the writing of a life (§9).
- **404 — the unwritten page (§6.18).**

## 8. Worked examples

### 8.1 The hero — a parish register opens

*Setting: a parish memorial register, 41 lives, maintained by the
church office. Desktop, ≥1200px.*

The page paints as paper — `#F8F6F1` edge to edge, no header bar, no
chrome. At the top, one apparatus line (12px, letterspaced, grey):
"THE REGISTER OF ST BRIDE'S — 1914 TO THE PRESENT", with "The
Register" and "Enter a life" as its only links, right-aligned in the
same line. Below it, the dedication plaque (§6.13): hairline border,
40px of padding, and in Source Serif italic at 19px: *"For the
forty-one men and women of this parish who did not come home, and
for those who waited for them."* It fades in over 800ms, 200ms after
the masthead — the only motion on load.

The reader scrolls. The dedication holds (sticky) while the 60vh
head pause passes beneath it; the two column rules run down through
the empty paper at the measure's edges. The first name — "Thomas
Wren" — crosses the 72% line; the dedication has already released by
geometry. The sequence runs (§6.2): the name fades in, Playfair at
44px (0–600ms). The dates follow (600–1200ms): "1897 — 1918", and
within them the dash lengthens left to right over 800ms from the
200ms mark (§6.3) — the twenty-one years drawn as one stroke. Then
the portrait step: inside its oval, a photograph develops (§6.1) —
600ms of rumour, a ghost in uniform by 1900ms, and at 3000ms a young
man, filters cleared, caption beneath: "Thomas Wren, before
embarkation, 1916." Only then does the life fade in (600ms): four
sentences, 18px Source Serif at 62ch — apprenticed, enlisted,
killed at Passchendaele, "his name is read aloud in this church
each November." Its one figure — "He was 21." — is simply in the
text (§6.8 does not trigger; the line rode the life's fade). The
entry's last line is the button: "In lieu of flowers:" with its
violet hairline. In the bottom-left margin, the foot line crossfades
to "LIVES, 1 OF 41" (§6.11). Total ceremony: about five seconds, of
which the reader spent most reading. Nothing else on the page has
moved.

### 8.2 Mid-page — crossing from one life to the next

*Setting: the same register, the reader between the seventh and
eighth lives.*

The seventh life — a schoolteacher, 1951–2019 — has been read; its
"In lieu of flowers" was opened earlier and points to the school
library fund (the wash, §6.10, still open above — the theme does not
tidy it away). The reader scrolls on. The life leaves upward; its
portrait, in its last viewport pass, sat at −1px of drift (§6.6) and
its settling light (§6.7) eased back to 100% as it left centre —
neither effect noticed, both felt. Then the pause (§6.4): a full
viewport of paper and the two rules. Centred in it, the floral rule
(§6.5) is drawing as the pause crosses — stem at 70% when the pause's
centre reaches the viewport's lower third, the leaf branching, and
as the pause centres, the single violet flower completes and fills.
The reader has not been told "you are 18% through this page"; they
have watched a flower finish, which is the same information in the
page's own grammar. Past the pause, the eighth name crosses 72% and
its sequence begins — name, dates, dash, develop, life — in the
order the reader has now learned twice and trusts. Predictability,
here, is not boredom; it is liturgy.

### 8.3 Conversion — entering a life

*Setting: the inscription form (§6.16), a daughter entering her
mother's life, phone, <768px.*

The form is a leaf of the register: caption line at the head stating
the editorial fact ("Entries are read before they appear in the
register. This takes a day or two, and is done by a person."), then
the fields in entry order. She types the name — the rule beneath it
deepens, the label settles to ink. The dates: two year fields with
the dash printed between them, never stacked. In the life field,
ruled like a page, she writes 230 words; the quiet caption beneath
counts "about 230 words — the register's entries run 150 to 300"
and says nothing more. She attaches the portrait; the field notes
the photograph's name in caption style. The closing line: the cause
— the hospice, and her mother's years volunteering there. Her own
name and relation last: the signature.

She submits. No spinner: the form's head gains "Entering…" in
apparatus type. One field is wrong — she has typed the death year as
1949, before the birth year 1951 she entered above. The form does
not fade; the date field's rule turns violet, and beneath it, in
the error voice: "The second year is earlier than the first. One of
them wants correcting." Focus has moved to the error summary; she
fixes the year (2019), resubmits. This time: a 350ms fade through
paper, and the confirmation stands — her mother's name in Playfair
at 34px, the dates with the dash *drawing* (800ms, §6.3 — the form's
one ceremony, earned), and in italic: "This life has been received.
It will appear in the register once it has been read." Beneath, one
plain link: "Return to the register." She is not thanked for her
engagement. She is told what will happen, by whom, and roughly when
— which is what the page owes her.

## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to this theme's world; each cure is
the theme's own law restated at the point of temptation.

1. **The percentage progress bar.** A stakeholder asks "how far
   through the memorial am I, as a number?" — and a bar appears.
   *Cure:* §6.11's count and §6.5's rule are the only progress the
   theme permits. A percentage of the dead is an obscenity with a
   UI kit behind it; the gate greps for `%` in progress contexts.
2. **Counting-up numbers.** Years of service tick 0→41 in a stat
   block. *Cure:* §6.8's fades, inside the prose, and no stat blocks
   exist in this theme's inventory to put them in.
3. **The tilt hover.** Portraits lean toward the cursor "for
   delight." *Cure:* §6.9 — contrast and a hairline rule. Stillness
   is respect; the gate measures hover transforms and fails any.
4. **Sepia photographs.** A filter makes every portrait "vintage."
   *Cure:* portraits keep their own tones (§5). Sepia is nostalgia
   applied with a sponge; these are specific people, not an era's
   mood.
5. **The dark mode.** Black background, candle-glow accents — the
   funeral-home theme wearing this theme's name. *Cure:* §2's
   refusal, documented so it is not "fixed" later.
6. **Clip-art mourning.** Doves, angels, lilies in corners, a
   script-font "Forever in our hearts" over the hero. *Cure:* the
   only flower is §6.5's single drawn violet; the only italic is
   the dedication's; sentiment is carried by the writing (§12),
   never by ornament.
7. **Entry order violated.** A template shows the portrait first
   "because images engage." *Cure:* §6.2 is the theme's one law and
   a blocking gate item. Engagement is not a defence available here.
8. **The compressed pause.** Pauses cut to 30vh "to reduce bounce."
   *Cure:* §6.4 — the pause is content. A build that compresses it
   has not optimised the page; it has abridged the silence between
   lives, which is an editorial act requiring an editor's authority.
9. **Violet inflation.** The flower colour spreads — buttons,
   headings, links, a violet "theme." *Cure:* the ration (§2): one
   flower per rule, the hover hairline, selection, error rules,
   focus. Measured at the gate on a full-page screenshot: violet
   ≤1.5% of pixels excluding transient hover/focus states.
10. **The marquee of names.** A scrolling ticker of the dead "so
    every name gets seen." *Cure:* §5's permanent refusal. Names are
    read in the procession or found in the register; they are never
    broadcast.
11. **Euphemism sludge in UI copy.** "Passed away peacefully in our
    hearts forever" as a template line under every name. *Cure:*
    §12's voice — the page says "died", gives the facts, and lets
    the family's own words, where present, carry the feeling.
12. **Commerce on the leaf.** The inscription form gains an upsell,
    a "premium memorial" tier, a candle for £2.99. *Cure:* §7's
    ruling — payment, where a platform truly requires it, is a
    separate plainly-labelled step, never sharing the page where a
    life is written.

## 10. Quality gate

A build may not ship in this theme until every **blocking** item
passes. The reviewer checks evidence (a JS-off load, a full-page
screenshot, a scroll recording), not intentions.

**Blocking — all must pass.**

1. **Entry order audit:** on every page type and breakpoint, every
   entry presents name → dates → portrait → life in DOM order and
   in sequence order. One violation fails the build.
2. **JS-off test:** with JavaScript disabled, every life is fully
   readable in order, portraits at final state, causes expanded,
   the register complete, the form submittable. Nothing invisible,
   nothing missing.
3. **Develop fallback:** with image loading throttled past 2000ms,
   portraits appear at final state on arrival (no blank ovals held);
   with transitions broken, the §6.1 watchdog forces final state by
   trigger+3400ms.
4. **No scroll interference:** a full scroll recording shows no
   snapping, jacking or velocity change through pauses; pauses are
   spacing only.
5. **Progress purity:** no percentage, bar, or count-up anywhere on
   any page (grep + visual audit); the only progress is §6.5's rule
   and §6.11's count, and §6.11's N is DOM-counted.
6. **Violet ration:** full-page screenshots (top, mid, foot) measure
   violet ≤1.5% of pixels in static states; exactly one flower per
   floral rule.
7. **Drift measurement:** portrait drift across a full scroll pass
   measures exactly 2px total travel; hover transforms on entries
   measure 0px.
8. **Contrast audit:** body text ink-on-paper (15.9:1), captions
   ≥14px grey (5.1:1), form labels in `--ink-soft` or darker (never
   12px `--grey`), violet text only where ≥7:1 or non-textual.
9. **Copy audit:** no exclamation mark anywhere in UI strings; no
   banned phrase from §12; every error and empty state in the
   theme's voice; dates everywhere in the `YYYY — YYYY` form with
   the set dash.
10. **Form honesty:** the inscription form preserves all input
    through a killed-connection submit; states the editorial review
    plainly before submission; its confirmation says what happens
    next and by whom.
11. **Reduced-motion parity:** with `prefers-reduced-motion`, the
    page contains identical information in identical order — no
    develop, no drift, no settle, rules printed, sequences
    simultaneous.
12. **Print proof:** `@media print` renders the register as a clean
    document — pauses become page breaks, rules printed complete,
    no fixed margin furniture (§14).

**Standard — at least 9 of 10.**

13. Develop staging reads as three stages (blank/ghost/arrival) in a
    screen recording, not a linear fade.
14. The settling light measures +3% ±0.5% contrast at centre on a
    test portrait, and composes with hover to ≈107%.
15. The dash draws within the dates step's window and completes
    before the portrait step fires.
16. The floral rule's draw order is stem → leaf → flower with the
    fill in the final 10%.
17. Skeleton minimum (600ms) and maximum (4000ms, then the apology
    line) both verified under throttling.
18. The five-second test (§1): a first-time viewer describes the
    page as *a book of remembrance*, not "a memorial website theme."
19. One shared rAF loop drives drift, settle and rule scrub;
    sustained 60fps on a mid-range Android device during a full
    scroll, no frame over 20ms attributable to theme code.
20. The register filter announces its count politely and hides
    nothing when its script is removed.

**Minimum bar, in one line:** a build that passes the blocking
twelve has earned the right to be judged on its quietness; anything
less is a memorial costume, and it goes back to the desk.

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment. Components the theme refuses are listed with their
refusals, so a builder does not import them from a kit.

- **Buttons.** Two only. *The plaque button* (form submit, §6.16):
  hairline border, paper fill, Source Serif 16px, label is a plain
  verb phrase of the register ("Enter this life in the register").
  *The text link-button* (§6.10's line): indistinguishable from the
  life's own text until its underline. No filled primary button
  exists; a page that needs one is asking for emphasis this theme
  does not sell.
- **Inputs.** Ruled-line fields (§6.16): bottom hairline, transparent
  fill, labels above in `--ink-soft` apparatus. Selects, where
  unavoidable (a register grouping), are native selects restyled to
  the ruled line — the theme does not build custom dropdowns over a
  register.
- **Checkboxes / radios.** Where a form truly needs them (consent to
  appear in the register; relation choice), they are small squares
  and circles in hairline ink, checked with a plain ink mark — the
  register's tick, set in type, never a violet fill.
- **Tables.** One: the register (§6.14), which is a table in
  everything but element name — ruled rows, a dates column, no
  zebra striping (striping is for ledgers of money), no sortable
  headers (the alphabet is the sort, and it is not negotiable).
- **Badges.** Refused. A life carries no badges. The nearest kin is
  the "read" pencil mark in the register's margin (§6.14) — a
  reader's trace, not a status the page awards.
- **Alerts.** *The correction slip:* a `--violet-pale` washed block
  with a hairline rule, set in the life's type, used for form errors
  at page level and failed transitions (§6.12). It reads as a slip
  laid on the page, corrects plainly, and stays until dismissed by
  the correction it asked for. No toast variant exists.
- **Pagination.** Apparatus links only: "Earlier lives" / "Later
  lives" at a procession break (§7), letter-range links in the
  register (§6.14), tens in the remembrances (§6.15). Numbered page
  lists are refused — a register is not paginated like search
  results; it is continued, like a book.
- **Modals.** Refused, entirely. Nothing on this page may interrupt
  a life with an overlay. Confirmation is a replaced leaf (§6.16);
  expansion is in place (§6.10). A builder who reaches for a modal
  has a content problem the theme will not solve for them.
- **Toasts.** Refused. State changes speak in place (the form's
  "Entering…" line, the margin's count) or not at all.
- **Tabs.** Refused. The register has one order; a life has one
  text. Groupings are headings, not tabs.
- **Accordions.** One sanctioned instance: §6.10. Nothing else on
  the page folds.
- **Search.** The register filter (§6.14): a ruled-line input at the
  index's head, instant narrowing, polite count announcement. There
  is no global search chrome; a name is found in the register or a
  life is read in the procession.
- **Dividers.** The floral rule (§6.5) between lives; hairlines
  everywhere else. No other divider artwork is admitted.
- **The portrait frame.** §6.1's oval — a component in its own right,
  reused on the about page and nowhere else; it is never used for
  the living in lists, avatars or cards.
- **The dedication plaque.** §6.13 — used once per procession, at
  its head. A template that repeats it mid-page has misunderstood
  what a dedication is.
- **Progress.** §6.5 + §6.11, and nothing else (§10, item 5).

## 12. Content & copywriting voice

The voice is the obituaries desk's: economical, factual, warm only
in its precision. Every word on the page — including its errors —
is written as if it will be kept, because on this page it will be.

**Laws.**

1. **Say "died".** The page's own copy uses the plain word ("She
   died at home, in the village where she was born."). Euphemism is
   permitted only inside a family's own contributed text, where it
   is *their* voice and is never edited into the page's.
2. **The name is the headline; the facts are the tribute.** UI copy
   never adds praise the life itself has not earned in prose. No
   "beloved" is supplied by a template.
3. **No exclamation marks. No questions as headings.** The page
   states; it does not exclaim, and it does not ask the reader how
   they feel.
4. **Dates are always `YYYY — YYYY`** with the set dash (§6.3), in
   every context including the register and the form's confirmation.
5. **The apparatus speaks in short declaratives.** Labels, counts and
   instructions are sentences or sentence fragments of record, never
   marketing fragments.

**By surface.**

- **Headlines (entry names):** the name, nothing else. ✓ "Eleanor
  Hartley" ✗ "Remembering the Wonderful Eleanor Hartley".
- **The dedication:** authored per register, 2–4 lines, first person
  plural of the keeping body, no quotation marks borrowed from
  famous grief. ✓ §8.1's parish line. ✗ "Gone but never forgotten"
  (a template sentiment; if a family writes it in their own text it
  stands — the page never supplies it).
- **Labels:** "The name", "The dates", "The life", "The portrait",
  "In lieu of flowers", "Your name, and how you were related" —
  plain nouns of the register. ✗ "Full legal name*", "Bio",
  "Upload image".
- **Buttons:** "Enter this life in the register", "Return to the
  register", "Read the life" (register deep-links). ✗ "Submit",
  "Get started", "Share your story!".
- **Errors:** plain, specific, correctable, in the second person of
  record. ✓ "The second year is earlier than the first. One of them
  wants correcting." ✓ "The name is needed before the dates can be
  set." ✗ "Oops! Invalid input."
- **Empty states:** ✓ Register, unfiltered: "No life has yet been
  entered in this register." ✓ Register, filtered to nothing: "No
  life is entered under that name." ✓ Remembrances, none yet: "No
  remembrance has been left. The book is open." ✗ "Nothing here
  yet!" anywhere.
- **Confirmation:** states what was received, what happens next, by
  whom, roughly when (§8.3's italic). It never thanks the reader
  for engaging.
- **The closing line:** always "In lieu of flowers:" followed by the
  cause or the family's wish, verbatim from the entry's record. The
  platform never appends its own charity.

**Banned list (grepped at the gate where mechanical):** "gone too
soon" (as supplied copy), "celebrate their life" as a UI heading,
"RIP" in chrome, "angel", "heaven's gain", any exclamation mark, any
percentage in a progress context, "community" as a name for the
readers of the dead.

## 13. Full-page scroll choreography map

The home procession, top to foot, in order. Beats are the reader's,
paced by scroll; timings are the elements' own.

1. **Masthead settles.** The apparatus line is present at paint; no
   motion. The page begins as print.
2. **The dedication fades in** (800ms, §6.13) — the page's first
   movement, and its thesis stated: this will be slow.
3. **The head pause.** The dedication pins; 60vh of paper passes
   beneath it. The reader learns the column rules and the measure.
4. **First release.** The dedication lets go by geometry; the first
   name is approaching the 72% line.
5. **First sequence** (§6.2): name (600ms) → dates with the dash
   drawing (800ms within) → portrait develops (3000ms) → life
   (600ms). The reader's whole education in the page's grammar
   happens here, once.
6. **First count.** The foot margin crossfades to "LIVES, 1 OF N"
   (§6.11). Position has been reported without a number ever being
   performed.
7. **The regard beats.** As the first life is read: its portrait
   drifts its 2px (§6.6), the light settles and holds at centre
   (§6.7), its figures are already in (§6.8). The reader feels the
   page attend.
8. **The first pause.** The life leaves; paper; the floral rule
   draws — stem, leaf, the one violet flower (§6.5). The reader
   crosses.
9. **The procession establishes.** Beats 5–8 repeat per life, with
   variations the content supplies (a life with no portrait runs its
   three-step sequence; an opened "In lieu of flowers" stays open
   above its pause). By the third life the reader no longer notices
   the choreography, which is its completion.
10. **The register's invitation.** After the last entry, one
    apparatus line offers the index and the inscription form —
    placed after, never between (§7).
11. **The final pause.** Empty of even a rule (§6.17's ruling): the
    reader is told the procession has ended by an absence.
12. **The foot arrives** (600ms fade): the complete rule, the count
    sentence, the italic closing line, the imprint. The margin rests
    at "LIVES, N OF N".
13. **Stillness.** Nothing on the page moves again. The map's last
    beat is the absence of a next one.

## 14. Whole-page performance budget

This is the library's lightest theme at runtime and must stay so;
its budget is enforced as a design material, like its pauses.

- **Asset weight.** First load ≤ 380KB total: HTML/CSS/JS ≤ 120KB
  (the theme's entire JS — sequencer, loop, filter — is ≤ 18KB
  gzipped; it has almost nothing to do), fonts ≤ 130KB (Playfair
  Display 400 + Source Serif 4 regular/italic, subsetted, `woff2`),
  first portrait ≤ 120KB. Subsequent portraits lazy-load at ≤ 120KB
  each, one entry ahead of the reader — never the whole register's
  photographs at once.
- **Animation frame budget.** The shared loop drives three things
  (drift, settle, rule scrub) at `--lerp: 0.06`: combined ≤ 0.5ms
  per frame on a mid-range Android; opacity/filter transitions are
  compositor work and off the loop. No frame over 20ms attributable
  to theme code during a full-page scroll (§10, item 19).
- **Long tasks.** None over 50ms after load; the DOM count for §6.11
  is the only O(entries) work and runs once, at load, off the
  critical path.
- **Layout stability.** CLS ≤ 0.02 for the page: portraits reserve
  their oval's aspect box, skeleton geometry matches entry geometry
  (§6.12), the dash's span is width-reserved (§6.3), figures fade in
  place (§6.8). A register whose text jumps has startled a reader,
  which this page may never do.
- **Cut order when the budget is exceeded.** (1) The settling light
  (§6.7) — the most expendable breath. (2) The 2px drift (§6.6).
  (3) Skeleton develop staging (skeletons arrive static). (4) The
  foot-margin crossfade (count changes instantly). **Never cut:**
  the entry order, the develop's fallback watchdog, the pauses, the
  register's completeness, or any content. Motion is this theme's
  garnish; its substance is paper and order, and the budget protects
  them in that sequence.

## 15. Build-order checklist

1. **The static register first.** Semantic HTML for the full
   procession — dedication, entries in DOM order (name → dates →
   portrait → life), pauses, foot — readable and complete with no
   CSS beyond typography and no JS at all. This is the fallback
   state of every element; build it as if it were the product,
   because for some readers it is.
2. **Palette and type.** The four anchors and derived tokens (§2);
   the two faces, subsetted; the type scale and its laws (§3),
   including the dates' set dash as static print.
3. **Layout.** Measure, column rules, pause geometry, dedication
   plaque, foot (§4) — verified at all three breakpoints before any
   motion exists.
4. **The register and 404** (§6.14, §6.18) — the apparatus pages,
   static; the filter added as its progressive layer.
5. **The form as a working server form** (§6.16) — posts, validates
   server-side, preserves input, confirms in voice — before any
   client enhancement. Test the killed-connection case now.
6. **The develop** (§6.1) with its watchdog and 2000ms image rule,
   on the hero entry only; verify the three stages read as stages.
7. **The sequence** (§6.2) and the dash (§6.3) — observers,
   latching, focus-forces-settle, the per-entry watchdog.
8. **The quiet figures** (§6.8) and the expansion (§6.10) — the
   in-place interactions.
9. **The shared loop** — drift (§6.6), settling light (§6.7),
   floral-rule scrub (§6.5), in that order of implementation and
   reverse order of cut (§14). Verify 2px with a measurement, not
   an impression.
10. **The foot margin** (§6.11) with its DOM count, and the foot
    (§6.17).
11. **Hover and focus regard** (§6.9) — CSS only; measure hover
    transforms (must be zero).
12. **Skeleton and transition** (§6.12) — the last enhancements,
    with their minimum/maximum timings tested under throttling.
13. **Remembrances** (§6.15) and the moderation path, if the build
    is a platform.
14. **Reduced-motion pass.** Every variant in §6 verified against
    §10 item 11 — parity of information and order.
15. **Print stylesheet.** Pauses to page breaks, rules complete,
    margin furniture removed (§10, item 12).
16. **The gate.** §10 in full, with evidence: JS-off load,
    screenshots for the violet ration, a scroll recording for drift
    and scroll purity, the copy grep (exclamation marks, banned
    list, date formats). Sign-off recorded with the register's name
    — a build in this theme is signed like a page of the book.
