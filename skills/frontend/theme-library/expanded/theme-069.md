# 69. The 1962 Space Clipper Brochure — Expanded (v1 + v2)

> A travel brochure for orbital flights as Pan Am would have
> printed it in 1962: optimistic retro-futurism, atomic-age
> typography, stewardess-era service copy, and lithographed
> illustration — the future exactly as the past imagined it.
> The page is not a website wearing a vintage costume. It is a
> printed object that happens to move: a cover that launches,
> a dotted orbit line the reader travels, fares held open like
> a spread on the salesman's counter, and small print honest
> enough to admit the spacecraft has not been invented yet.

**The theme's one law: the brochure prints nothing it cannot
stand behind, and nothing printed is ever hidden.** Every
fare, time, altitude and count on the page traces to one
declared record — the 1962 Schedule (§6.17) — and reconciles
across every printing of it: hero, table, card, form and
colophon. The optimism is the voice; the honesty is the small
print, and the small print is law: the footnote *"Fares
subject to CAB approval and the invention of the spacecraft."*
prints verbatim, at legible size, wherever the fares print.
And no page of the brochure ever waits on an effect — the
brochure ships fully printed, every animation an impression
laid over finished type, each with a named watchdog. A build
that invents a fare, drops the footnote, strands a footnote
behind a reveal, or lets the clipper fly somewhere the
Schedule does not go has broken the law four ways.

---

## 1. Concept & world

The year is fixed: **1962**. Not "the sixties" as a mood —
1962 as a discipline. John Glenn has flown (February 1962);
the brochure writes as if scheduled orbital passenger service
were one CAB ruling away, because in the brochure's world it
is. Pan American World Airways — the original's named carrier
and the era's real "Chosen Instrument" — sells seats on the
Clipper *Morning Star* from Idlewild to an orbital terminal
300 miles up, in a sixteen-page lithographed brochure that
this website performs page by page.

The world has rules, and the rules are the design system:

- **Everything is printed.** Type is letterpress-set, pictures
  are halftone lithographs with honest misregistration, the
  sky itself is dots. Nothing on the page is "rendered"; it is
  *impressed*. Motion is what ink and paper do in this fiction:
  ink squashes as it sets, pages curl as they turn, plates
  settle into their frames, a ticket gets punched.
- **The reader is a passenger before they are a customer.**
  The page's dotted orbit line is the flight route; scrolling
  is travelling it; the margin counts the miles climbed.
  Sections are ports of call. The fare table is not a pricing
  grid — it is the spread the salesman holds open longest.
- **Service is the copy's register.** Stewardess-era courtesy,
  complete sentences, no exclamation marks except on the
  cover. The brochure is confident the way a printed timetable
  is confident: it prints times to the minute and means them,
  while its one honest footnote concedes the whole enterprise
  awaits an invention. That tension — total confidence, total
  candour, in the same spread — is the theme's soul. Lose
  either half and it becomes parody.
- **The future is drawn, not photographed.** All imagery is
  lithograph-style illustration: flat colour plates, halftone
  skies, the clipper drawn in profile with its airline livery.
  A photograph would break the fiction instantly — in 1962
  there was nothing to photograph.

**Best-fit sites and audiences.** Heritage and retro brands
selling a real product through period confidence (a watch, a
hotel, a railway, a distillery); space and aviation museums
and their exhibition microsites; a real space-tourism or
high-altitude experience operator with the nerve to sell the
future in the past's voice; film, theatre and book launches
set in the period; a conference or festival styled as a
world's-fair pavilion. The audience is anyone who reads a
fare table for pleasure — design-literate, nostalgia-fluent,
and allergic to irony at the product's expense.

**When NOT to use it.** Never for a product that needs
clinical trust on first read (medical, legal, financial
advice) — the fiction's charm reads as evasion there. Never
for breaking news or anything time-critical; a brochure is
the slowest medium ever made. Never as a skin over a generic
SaaS landing page: if the content cannot be honestly
re-expressed as cover, voyage, life aboard, fares and
reservations, the theme will fight it on every page. And
never with the irony turned up — the moment the build winks
at the reader ("lol, they thought this was real"), the law
is broken and the theme is dead.

**The physical object being performed.** The brochure is
specified as an object before it is specified as a page:
sixteen pages, 8½ × 11 in, cream stock, three printing
colours plus the gold seal pass, one fold-out (the fare
spread). The site performs that object at reading distance:
sections are its pages in imposition order, the fare spread
is its fold-out — the one sheet that opens wider than the
book, which is why it alone is pinned (§6.5) — and the
colophon (§6.16) is its back page, form number and all.
This is not flavour text: the page budget in §14, the
single-pin rule in §4 and the imposition stagger in §5 all
derive from the object's spec. A build that adds a second
pinned "fold-out" has printed a seventeen-page brochure
and misbound it.

**The one data record.** Everything traces to the **1962
Schedule** (§6.17): two flights, four fares, one ascent
profile, one reservations ledger. It is declared once, in
§6.17, and §10's gate re-adds it.

## 2. Palette

Five anchors from the original entry, unchanged, plus five
derived tokens. Contrast ratios below are computed from the
hex values for this expansion (WCAG relative luminance).

| Token | Hex | Role | Ratio & pairing law |
|---|---|---|---|
| `--cream` | `#F5EDD8` | Brochure paper; the page ground everywhere | The ground itself; all text pairings measured against it |
| `--red` | `#C8402A` | Rocket red: cover headline, clipper livery, the one exclamation | 4.26:1 on cream — display and large type only, never body |
| `--teal` | `#1F6E6A` | Orbit teal: the orbit line, links, table rules, second plate colour | 5.14:1 on cream — body-capable; the working colour of the brochure's interior |
| `--gold` | `#D9A441` | Atomic gold: starbursts, seals, plate frames, the CAB seal | 1.93:1 on cream — **never text on cream**; ornament, rules and fills only |
| `--navy` | `#22304A` | Ink navy: body type, table figures, night plates | 11.32:1 on cream — the brochure's ink; all running text |
| `--cream-deep` | `#EADFC2` | Paper shadow: curl shade, plate mats, skeleton blanks | 9.96:1 under navy text — the shadow side of the paper |
| `--red-deep` | `#A33324` | Second-impression red: fine print, footnote, hover-deepened red | 5.89:1 on cream — the body-capable red; footnotes and punch marks |
| `--teal-deep` | `#174F4C` | Deep orbit: small teal text, table totals, footer ground tint | 7.96:1 on cream — small-text teal |
| `--gold-ink` | `#D9A441` | Gold as lettering — licensed ONLY on navy plates | 5.87:1 on navy — the one legal gold text pairing |
| `--paper-edge` | `#D8C9A3` | Deckle and trim edges, hairline rules on cream | Decorative only; never carries information alone |

**Usage ratios.** Cream ~78% of any viewport (it is paper;
the page is mostly paper). Navy ~12% (ink — type, figures,
line work). Teal ~5% (the route and the apparatus). Red ~3%
— rationed like a cover colour: headline, livery, one seal,
one punch. Gold ~2% (starbursts, frames, the seal's ring).
A viewport where red exceeds gold is a poster, not a
brochure; §10's gate samples it.

**Pairing laws.**
- Body text is navy on cream. Nothing else sets a paragraph.
- Red on navy (2.66:1) is a **forbidden pairing** — the
  clipper's red livery never carries navy type; its name is
  lettered in cream.
- Gold text exists only as `--gold-ink` on navy plates (the
  colophon plate, the CAB seal plate). Gold on cream is
  ornament or it is a defect.
- The footnote and all fine print set in `--red-deep`, never
  in a grey — 1962 brochures did not own a grey; small print
  was printed in the second colour, smaller.
- Misregistration (§6.6) uses red and teal plates offset
  against the navy key plate — the three printing colours
  are red, teal, navy; gold is a fourth, foil-like pass used
  only on seals and frames.

**Dark-mode behaviour.** There is none, and that is a ruling,
not an omission: the object is a printed brochure on cream
stock; a "dark brochure" is a different object. On a navy
plate section (the night-sky plate, the colophon) the
brochure itself prints a dark page — cream type on navy at
11.32:1 — and the theme treats that as a *plate*, not a
mode. `color-scheme: light` is declared; OS dark mode must
not invert the paper.

## 3. Typography

Three families, four voices. No fourth family may be added;
the brochure's type case is closed.

- **Display — Archivo Black.** The atomic-age grotesque of
  the cover: headlines, the fare table's route names, the
  big numerals of the altitude readout's final frame. Set
  tight (−0.01em), uppercase for cover lines, never below
  28px — Archivo Black at small sizes is a smudge, and 1962
  knew it: small emphasis was set in the grotesque's medium
  weight, not the black.
- **Sub-display & labels — Archivo** (the original's
  "geometric Futura-like" voice). Section titles, port
  names, button labels, table headers, the nav. Medium and
  semibold; labels in tracked uppercase (0.14em) at 11–13px
  — the brochure's rubric voice.
- **Body — Libre Caslon.** The elegance the original
  specifies: all running copy, service descriptions, the
  life-aboard prose. 17–19px, line-height 1.55, measure
  34–38em. Caslon's old-style figures are banned from tables
  (see figure law below); in prose they are the period's
  fingerprint and are kept.
- **Data — IBM Plex Mono.** The reservation counter's voice:
  fares in the table's figure column, the altitude readout,
  miles-to-orbit, form echoes, the colophon's form number.
  In-world justification: these are the numbers the counter
  *types* onto the ticket, and the ticket is typewritten.
  Tabular, always; a fare that proportional-spaces is a
  misprint.

**The type scale** (brochure points, translated): cover
headline clamp(44px, 8vw, 96px) Archivo Black; section
titles clamp(30px, 4.5vw, 52px); port names 24px Archivo
semibold; body 17–19px Caslon; fare figures 20px mono;
table body 15px mono/Archivo; captions 13px Caslon italic;
fine print and the footnote 11.5px — **and never smaller**:
the law (§1) makes the footnote's legibility a build gate,
so the brochure's smallest legal size is 11.5px at 1.45
line-height, in `--red-deep` at 5.89:1. A designer who needs
smaller type has written too much small print.

**Type laws.**
1. **Numerals in tables are always mono**, right-aligned,
   with the dollar sign hung in its own column — the period
   table's ruled money column.
2. **Headlines are set, not typed**: they arrive with the
   ink-squash (§6.1) or not at all; a headline in Caslon is
   a chapter in a novel, not a brochure cover.
3. **One exclamation mark per page**, on the cover only, in
   red. Interior pages are too well-bred.
4. **The word ORBIT sets in tracked caps** in Archivo
   wherever it appears as a destination — it is a place
   name on a timetable, and timetables shout their termini.
5. **Italics are Caslon's alone** (captions, the ship's
   name — *Morning Star* is italicised as vessels are);
   Archivo never slants, mono never slants.

**Fallback stacks — the misprint rule.** If Archivo Black
fails to load, headlines fall to Archivo's heaviest
available weight, never to a serif: a Caslon headline is a
chapter heading, and the cover would read as a novel. If
Libre Caslon fails, body falls to Georgia (the one system
serif with Caslon's old-style manners), and mono falls to
ui-monospace with `font-variant-numeric: tabular-nums`
forced — a fare column that loses its tabular figures is
re-set before it is re-shown (§6.5's focus rule lands
figures instantly for the same reason). Font failure is
handled as a printing works handles a broken sort: the
page still prints, in the nearest honest type, and the
watchdog (§5) ensures the ink-squash never performs on a
face that is about to be swapped.

## 4. Layout language

**The page is a brochure**: a single cream sheet, read top
to bottom as a spread sequence, with the dotted orbit line
(§6.2) threading the left margin like a route printed on a
fold-out map. The sheet's measure is 1200px maximum; the
brochure never stretches to fill a cinema screen — wide
screens show more *table* around the brochure (a `--cream-deep`
surround at ≥1600px, the counter the brochure lies on).

**Grid.** 12 columns on desktop, but the brochure thinks in
*plates and columns of type*: illustrations sit in plates
(framed, matted on `--cream-deep`, deckle-edged), text sits
in one or two Caslon columns beside them, and the two
alternate sides down the page in printer's imposition order
— plate left, type right; type left, plate right — the
rhythm of a held-open brochure. Tables break the alternation
deliberately: the fare spread (§6.5) takes the full measure,
because fares are the point.

**Spacing rhythm.** A 8px base unit; sections separated by
96px of paper and a printed rule with a centred starburst
(the brochure's ornament, never an emoji-like divider);
plates carry 20px mats; the orbit line's margin column is
a fixed 72px on desktop, inside which the clipper travels
and the miles accumulate. Whitespace is *paper*: it is the
stock showing, priced into the object — a dense page reads
as a cheap brochure, and §9 names it.

**Density rules.** One plate per section maximum in the
first viewport of that section; one table per page section;
the fare spread is the only pinned element on the page —
a brochure has one spread the salesman holds open, not
five. Fine print clusters at the foot of its own spread,
never exiled to the footer: the footnote lives under the
fare table (§6.5), the baggage note under the reservation
form (§6.14).

**The fold-out rule.** The fare spread's pin (§6.5) is the
site's single fold-out, and the layout treats it as one:
approaching sections narrow slightly toward the standard
measure, the spread itself opens to the full 1200px with
its rail, and following sections resume the measure — the
reader feels the book open wider and close again. No other
section may break the measure for emphasis; a brochure
with five fold-outs is a brochure that was never folded.
On mobile the fold-out is simply a longer page (§6.5's
cut) — a leaflet, honestly.

**Edges.** Plates and the sheet itself carry a deckle-cut
edge — an SVG mask with a 2px irregular bite — on the
outer edge only. Interior edges stay trimmed square; a
brochure is rough outside, precise inside. The page-curl
(§6.4) shades from `--cream-deep`, never from grey or black:
paper shadows are paper-coloured.

## 5. Full motion system

One shared rAF loop drives every scroll-scrubbed value
(lerp 0.11 — a paper glide, heavier than air, lighter than
machinery). Named easings, the press's own: `--ease-press`
(cubic-bezier(0.2, 0.9, 0.25, 1.15) — ink squash, a slight
overshoot as the type bites), `--ease-glide`
(cubic-bezier(0.33, 0.1, 0.2, 1) — paper sliding on a
counter), `--ease-slingshot` (cubic-bezier(0.6, -0.1, 0.2,
1.4) — the clipper's gravity exit, stretch then release),
`--ease-settle` (cubic-bezier(0.25, 0.8, 0.3, 1) — a page
settling flat), `--ease-puff` (cubic-bezier(0.1, 0.6, 0.4,
1) — halftone puffs blooming). Every motion term from the
standard list, translated into print:

- **Scroll-triggered reveals** — pages reach reading
  position and *print in*: content is fully typeset in the
  DOM; the reveal is a 500ms page-curl shade (§6.4) plus a
  2% ink-density rise. Nothing fades from invisible; print
  deepens, it does not appear.
- **Scroll-driven / scrubbed animation** — the orbit line
  draws and the clipper travels it (§6.2), the miles
  accumulate (§6.3), the fare pin's footnote prints
  letter by letter across the pin's travel (§6.5).
- **Parallax** — three print depths only: plates at 0.96×,
  type at 1.0×, halftone sky grain at 1.04× — the depths of
  a lithograph's passes separating almost imperceptibly.
  More than three depths is a diorama, not a brochure.
- **Pinned sections** — exactly one: the fare spread
  (§6.5), pinned 120vh while route details scroll past.
- **Smooth scrolling** — native scroll, lerped read-outs;
  the brochure never hijacks the wheel (a reader turns
  pages at their own speed; the clipper merely keeps up
  via the loop).
- **Progress indicator** — the clipper's position plus
  MILES TO ORBIT in the margin (§6.3). No bar exists;
  a progress *bar* is a machine part.
- **Staggered reveals** — panels stagger in printer's
  imposition order (the order sheets leave a press:
  1, 4, 2, 3 across a spread), 90ms apart.
- **Masked reveals** — the itinerary's route map strokes
  itself as an SVG line (§6.13's table companion plate);
  headline words mask-rise 0.3em as the ink sets.
- **Kinetic typography** — refused as spectacle; the one
  licensed kinetic act is the headline's ink squash
  (§6.1) and the footnote's letter-by-letter print
  (§6.5). Type in this brochure is *set*, and set type
  does not dance.
- **Marquee** — refused. A brochure has no ticker. The
  cover's single permitted ribbon is static print.
- **Counters** — altitude (§6.7), fares (§6.5), miles
  (§6.3), reservations (§6.14) — all count in period
  table style, mono, and all land exactly on Schedule
  figures and *hold* (a counted fare that trembles is a
  fare the airline is unsure of).
- **SVG line-draw** — the orbit line itself, the route
  map, the deckle rules. Drawn lines are printed lines
  being ruled by a straightedge, 600–900ms.
- **Image scale-in-frame** — plates scale 1.05 → 1.0
  inside their misregistered frames (§6.6).
- **Hover / magnetic / tilt micro-interactions** —
  re-ink hover (§6.8) everywhere; plates tilt ≤3° like a
  brochure lifted off the counter (§6.6); magnetic
  buttons are refused — paper is not magnetic, and a
  button that follows the cursor is a salesman who will
  not let go of your sleeve.
- **Custom cursor** — refused by standing rule; the
  system cursor is the reader's own hand on the page.
- **Skeleton loading** — unprinted brochure blanks
  (§6.15): cream sheets with plate-shaped voids that ink
  in as content arrives.
- **Page transitions** — the page-curl wipe (§6.15),
  600ms, shadow from `--cream-deep`.
- **Reduced motion** — the brochure lies open, fully
  printed: no curls, no puffs, no climb; every figure at
  its final value, the clipper parked at the reader's
  section. Specified per element in §6.

**Watchdog law.** Every armed effect carries a named
watchdog (1000–3000ms per element in §6): if the loop,
observer or font race fails, the watchdog prints the
element in its final state. The brochure's promise is
that nothing can remain unprinted.

**Loop mechanics.** The loop keeps one lerped progress
value per *instrument*, not per element: the flight value
(drives §6.2, §6.3 and §6.13's arc — one number, three
printings, incapable of disagreement), the pin value
(§6.5), and per-section turn values (§6.4). Elements
subscribe to an instrument; no element runs its own
scroll math. Ambient cycles (puffs §6.1, stars §6.10,
plate breathing §6.6) run on CSS animations, not the
loop, so a stalled loop never freezes the sky — and a
killed loop leaves the ambience running over a fully
printed page, which the watchdog drill (§10) accepts
as a passing state: the brochure is readable, only its
instruments have stopped.

## 6. Signature elements

### 6.1 The halftone exhaust hero — the cover

- **What & why.** The brochure's cover, performed. A
  lithographed clipper in Pan Am livery sits printed and
  still on the cream cover for one beat — long enough to be
  a picture on paper — then its exhaust plume wakes: layered
  halftone puffs, dot-density circles expanding and fading
  in sequence beneath the tail, while the cover headline
  sets with letterpress ink squash and the altitude readout
  (§6.7) begins its climb in the corner. It belongs because
  the cover is the whole fiction in one spread: a printed
  object that launches. If the hero were a video or a 3D
  model, the brochure would be a lie about its own medium;
  as halftone and ink, the launch is something the *paper*
  does.
- **Structure.** One `<header>` cover plate: an inline SVG
  lithograph (clipper profile, three flat colour passes —
  navy key, red livery, teal shadow — over a halftone dot
  sky built from an SVG `<pattern>` of circles at 6px pitch),
  the exhaust as 5 stacked SVG circle-groups behind the
  tail, each group's dot radius driven by a CSS variable
  from the shared loop; headline in Archivo Black as real
  text over the plate's lower third; the altitude readout
  (§6.7) as a mono counter in the cover's bottom-right
  corner plate; a gold starburst seal ("FIRST FLIGHTS ·
  1965") as a rotated SVG badge, static. Everything is in
  the DOM printed-complete: the SVG ships with the plume at
  its resting mid-bloom, the headline at full ink.
- **Motion spec.** Trigger: load, after the font race
  (watchdog 900ms). Still beat: 600ms of pure print. Puffs:
  1.8s cycle (the original's figure), each puff group
  expanding dot-radius 2px → 9px and fading opacity 0.85 →
  0 over 1400ms `--ease-puff`, groups staggered 300ms, the
  sequence looping with a 400ms rest — a lithograph's idea
  of exhaust: discrete, rhythmic, unhurried. Headline: ink
  squash on load — scale 1.04 → 1.0, blur 1.5px → 0, over
  550ms `--ease-press`, words staggered 70ms in imposition
  order. The clipper itself moves ≤4px (a press tremor,
  not a flight) — the ship does not leave the cover; the
  *plume* says it is flying.
- **States.** Rest (pre-arm): fully printed cover, plume at
  mid-bloom, headline set. Animating: as above. Hover:
  none on the plate itself (covers are not handled); the
  cover's one CTA re-inks (§6.8). Scrolled-past: puffs
  pause off-screen (loop skips off-viewport work); the
  cover remains printed. Returning visitor (session flag):
  the still beat shortens to 200ms — a reader who has seen
  the cover launched is not made to watch it twice.
- **Content merge.** The headline IS the cover's printed
  headline ("ORBIT IS 300 MILES AWAY. WE LEAVE AT 9:30."),
  the readout is the flight's own altitude (§6.7), the seal
  carries the Schedule's service year. The plume blooms
  from the drawn ship's tail — exhaust belongs to this
  rocket, on this cover, or it is clip-art.
- **Failure fallback.** Watchdog at 2400ms from arm: if the
  loop or font race has not completed, the cover is forced
  to its printed state (plume static mid-bloom, headline
  unblurred at scale 1.0, readout at 62). No JS: the cover
  is exactly that printed state. A failed SVG pattern
  degrades to flat cream sky — the ship and headline
  remain.
- **Reduced-motion variant.** The cover as printed: plume
  frozen at mid-bloom, no squash (headline simply set),
  readout at 62 MILES. The brochure's cover in a library —
  looked at, not launched.
- **Performance budget & mobile variant.** SVG pattern dots
  are one `<pattern>` fill, not nodes; puff animation
  updates 5 CSS variables per frame, ≤0.2ms. Cover plate
  ≤120KB total inline. Mobile (<768px): puff groups reduce
  to 3, cycle 2.2s; the seal moves inline beside the
  headline; headline clamp floor 40px.
- **Choreography timeline (v2).** t=0 cover printed →
  t=600 still beat ends → t=600–1150 headline squash, word
  by word → t=700 first puff group blooms → t=1000/1300/
  1600 groups 2–4 follow → t=900 readout begins climb
  (§6.7) → t≈2500 cover at cruising state: puffs cycling,
  headline set, readout holding 62.
- **State matrix (v2).** *Rest:* printed cover. *Hover:*
  none (CTA re-inks only). *Focus:* CTA focus = re-ink +
  2px navy outline. *Active:* CTA punches on click (§6.9).
  *Scrolled-past:* puffs paused, print intact. *Disabled:*
  n/a. *Touch:* identical; no hover states are load-bearing.
- **Breakpoints (v2).** ≥1200px: full cover, plate 7
  columns, sky pattern 6px pitch. 768–1199px: plate full
  measure, pitch 7px. <768px: plate full-bleed to the
  sheet edge, pitch 8px (coarser dots read better small),
  3 puff groups, seal inline.
- **Edge cases & failure modes (v2).** *Slow font load:*
  the squash waits for Archivo Black or the 900ms watchdog
  — squashing a fallback font then swapping would print
  the headline twice, a misprint. *Very tall cover art on
  short screens:* the plate caps at 78vh, sky crops, ship
  never crops. *Reader reloads mid-climb:* session flag
  shortens the beat; the readout restarts (it is a cover
  instrument, not a record).
- **Accessibility spec (v2).** The SVG is `role="img"` with
  `<title>` ("Lithograph of the Clipper Morning Star over a
  halftone sky"); the headline is real text, first in the
  reading order; the readout is `aria-hidden` decoration
  beside a visually-hidden static line ("Altitude at the
  edge of space: 62 miles") so screen readers meet the
  fact, not a ticking counter. Puff motion is far below
  flash thresholds (opacity fades on ≤9px dots).
- **Tokens consumed (v2).** `--cream`, `--red`, `--teal`,
  `--navy`, `--gold`, `--ease-press`, `--ease-puff`,
  `--dur-puff-cycle` (1800ms), `--dur-squash` (550ms).

### 6.2 The orbit-line clipper

- **What & why.** A dotted orbit line threads the whole
  page down the margin column, and a tiny clipper — 22px,
  red livery, cream name — travels it scrubbed to scroll,
  dipping toward each section in a gravity sag and
  slingshotting out with a small speed stretch. It belongs
  because the brochure sells a route, and this makes the
  reader *fly* it: sections are ports of call, and the
  ship that carries you between them is the ship being
  sold. It is the theme's progress indicator, its route
  map and its mascot in one printed line.
- **Structure.** One fixed-position SVG overlay in the
  margin column (72px wide, full height, `pointer-events:
  none`): a dotted path (`stroke-dasharray: 1 7`, round
  caps — a printed dotted route) whose visible length is
  the reader's progress; port ticks at each section's
  boundary with the port's number in mono; the clipper as
  a `<g>` positioned by the loop along the path via
  `getPointAtLength` on a hidden master path whose shape
  includes a sag (a quadratic dip of 14px) at each port.
  The path is rebuilt from the DOM's actual sections at
  load — ports can never disagree with the page.
- **Motion spec.** Trigger: scroll, via the shared loop
  (lerp 0.11). The clipper's position is the lerped
  scroll fraction mapped to path length. Entering a sag:
  the ship slows (path parametrisation does this
  naturally — the dip is longer path per pixel of scroll)
  and pitches 6° toward the port; exiting: `--ease-slingshot`
  stretch, scaleX 1.0 → 1.12 → 1.0 over 300ms, pitch
  releasing. At each port the tick prints (opacity/ink
  rise 200ms) as the ship passes. The dotted line ahead
  of the ship prints at 35% ink; behind it, full ink —
  the route flown is the route printed darker.
- **States.** Rest (top): ship at the cover port, line
  ahead faint. Travelling: as above. At port: pitch 0,
  tick printed, port name shown in the margin (Archivo
  caps 10px, teal-deep). Scrolled-past / at foot: ship
  docked at the colophon port, rotated horizontal — it
  has arrived. Scrolling up: the flight reverses exactly;
  sags are flown backward without stretch (a slingshot
  has no reverse gear; §13 codifies it).
- **Content merge.** The ports ARE the sections (Cover,
  The Clipper, The Voyage, Life Aboard, Fares,
  Reservations, Colophon — the Schedule's own structure),
  the line's total length is the page, and its terminus
  is labelled ORBIT with the Schedule's 300 miles (§6.3).
  Remove the content and the line goes nowhere — literally.
- **Failure fallback.** Watchdog: if the loop has not run
  within 1200ms of load, the line prints fully inked and
  the ship is placed at the top port — a static route map,
  which is what a paper brochure would have anyway. No JS:
  the same static map, drawn by CSS/SVG defaults (ship at
  first port, all ticks printed). The margin never ships
  empty.
- **Reduced-motion variant.** No travel: the line prints
  fully, and the ship sits at the port of the section
  currently in view, stepping between ports as the reader
  scrolls (position changes are instant, announced by the
  printed port name). Position is information; only the
  *flight* is motion.
- **Performance budget & mobile variant.** One
  `getPointAtLength` per frame ≤0.1ms; the overlay is a
  single SVG, compositor-only transforms on the ship
  group. Mobile (<768px): the margin column collapses —
  the line moves to a 28px gutter at the sheet's left
  edge, port names are cut (numbers only), sags flatten
  to 6px. Below 360px the ship is cut entirely and the
  miles readout (§6.3) alone carries progress — §14's
  first cut.
- **Choreography timeline (v2).** Scroll begins → loop
  lerps fraction → ship leaves port, pitch eases in over
  200ms → sag bottom at section boundary: tick prints,
  port name inks in → exit: stretch 300ms → cruise to
  next port. Footer arrival: ship docks, rotates to
  horizontal over 400ms `--ease-settle`.
- **State matrix (v2).** *Rest:* at port, name printed.
  *Hover:* none (overlay is pointer-transparent).
  *Focus:* n/a — the nav (§6.11) carries keyboard
  wayfinding. *Active:* n/a. *Scrolled-past:* ports
  behind are full-ink. *Disabled:* n/a. *Touch:* identical
  scrub; no tap targets on the line.
- **Breakpoints (v2).** ≥1200px: 72px margin, named
  ports, 14px sags. 768–1199px: 56px margin, names on
  arrival only. <768px: 28px gutter, numbered ticks,
  6px sags; <360px ship cut.
- **Edge cases & failure modes (v2).** *A section removed
  in a CMS:* the path rebuilds from the live DOM, so
  ports, ticks and the miles mapping (§6.3) can never
  point at a section that does not exist. *Jump scroll
  (End key, anchor leap):* the ship teleports with the
  lerp catching up in ≤600ms — it flies fast, it does
  not lag a full page behind. *Print:* the line prints
  fully inked with the ship at the first port (a route
  map on paper, §14).
- **Accessibility spec (v2).** The overlay is
  `aria-hidden` — it is a progress *illustration*; the
  same information exists as the real nav (§6.11) and
  the miles readout's visually-hidden text (§6.3). It
  must never be the only wayfinding. No focusable
  elements inside it.
- **Tokens consumed (v2).** `--teal`, `--teal-deep`,
  `--red`, `--cream`, `--ease-slingshot`, `--ease-settle`,
  `--loop-lerp` (0.11), `--orbit-gutter` (72px).

### 6.3 Miles-to-orbit — the margin progress

- **What & why.** Beneath the travelling clipper, the
  margin accumulates **MILES TO ORBIT** in period mono as
  the reader descends the page — 0 at the cover, 300 at
  the colophon, the Schedule's terminal altitude (§6.17).
  It belongs because in this brochure progress is not a
  percentage of a document; it is altitude on the flight
  being sold. Reading the brochure *is* the ascent, and
  the margin is its altimeter.
- **Structure.** A fixed mono readout in the margin
  column, two lines: the label "MILES TO ORBIT" (Archivo
  caps 9px, tracked, teal-deep) and the figure (IBM Plex
  Mono 15px, navy, tabular) — plus, at each port, the
  port's own altitude from the Schedule's ascent profile
  printed as a tick label (The Voyage port reads 62, the
  edge of space). The figure is one text node updated by
  the shared loop from the same lerped fraction that
  drives §6.2 — one cause, two instruments, never a
  disagreement.
- **Motion spec.** The figure counts continuously with
  the lerped fraction: miles = round(300 × fraction),
  updated at most once per frame and only when the
  integer changes. It does not ease, spin or odometer —
  an altimeter needle does not perform. At the foot, it
  lands on exactly 300 and holds; the label gains the
  printed suffix "· ORBIT" in red — the only state
  change, and it is typographic.
- **States.** Rest (top): 0. Climbing: integer counting.
  At ports: the figure passes the port's printed
  altitude exactly as the ship docks (same fraction —
  guaranteed by construction, audited in §10). Arrived:
  300, held, "· ORBIT" printed. Scrolled back up: counts
  down — an altimeter is honest in both directions.
- **Content merge.** The number is the Schedule's
  terminal altitude; the port ticks are the ascent
  profile's own milestones (10, 40, 62 — §6.17). The
  margin is the flight plan, read at reading speed.
- **Failure fallback.** Watchdog: if the loop is dead
  at 1200ms, the readout prints "300" with the suffix —
  the brochure's back cover always knew the total; a
  static "MILES TO ORBIT: 300" is a correct, if quieter,
  instrument. No JS: prints 300 statically.
- **Reduced-motion variant.** The figure steps between
  port altitudes only (0, 10, 40, 62, 300…) as sections
  enter — an altimeter read at stations, not a needle.
  All values remain exact Schedule figures.
- **Performance budget & mobile variant.** One text
  write per integer change; zero layout (fixed-width
  tabular figures, `font-variant-numeric: tabular-nums`).
  Mobile: the readout relocates into the masthead bar
  (§6.11) as a single line "142 MI" — the margin has no
  room, the instrument moves to the counter's edge,
  same node, same loop.
- **Choreography timeline (v2).** Scroll → fraction
  lerps → integer updates → port altitudes crossed
  exactly at their sections → footer: 300 lands, suffix
  prints over 200ms.
- **State matrix (v2).** *Rest:* 0 at cover. *Hover:*
  none. *Focus:* n/a. *Active:* n/a. *Scrolled-past:*
  holds the current altitude. *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: two-line margin
  readout. 768–1199px: one line, figure only + "MI".
  <768px: in the masthead (§6.11), "142 MI" form.
- **Edge cases & failure modes (v2).** *Page shorter
  than expected (sections removed):* the fraction is
  of the actual page, so 300 still lands at the actual
  foot — the altimeter measures this brochure, not an
  ideal one. *Rounding:* round-half-up, stated here so
  two builders' altimeters agree at every scroll
  position.
- **Accessibility spec (v2).** `aria-hidden` on the live
  figure (a ticking number is noise to a screen reader);
  a visually-hidden static text carries the fact:
  "The orbital terminal is 300 miles above the Earth."
  Contrast: navy on cream 11.32:1; the red suffix is
  large-print decoration beside the navy figure, never
  the sole carrier.
- **Tokens consumed (v2).** `--navy`, `--teal-deep`,
  `--red`, `--loop-lerp` (0.11), `--orbit-total` (300).

### 6.4 Page-curl section turns

- **What & why.** Each section, as it reaches reading
  position, turns like a brochure page: a soft paper
  shadow sweeps across its top edge with a slight skew,
  and the section's ink deepens 2% as it settles flat.
  It belongs because the site's founding pretense is that
  the reader holds a physical brochure — chapters are
  pages, and pages are *turned*, not scrolled past. The
  curl is the theme's section reveal, and its restraint
  is the point: a shadow and a settle, never a flap of
  fake paper obscuring the type.
- **Structure.** A `::before` shade layer on each
  `<section>`: a linear-gradient from `--cream-deep`
  (55% at the leading edge → transparent at 18% of
  section height), transformed `skewY(-1.2deg)` at rest
  offset above the section, driven by the loop as the
  section crosses the reading band (viewport 15%–60%).
  Content itself never transforms — only the shade and a
  CSS `filter: saturate()` ink step on the section's
  print layer (1.0 → 1.02, imperceptible except as
  *settling*). Sections ship with the shade parked
  off-section and ink at final value; the pre-state is
  JS-armed only.
- **Motion spec.** Trigger: section entering the reading
  band, scrubbed (not fired): shade position and skew
  read the section's progress through the band — enter
  at 15%: shade full; settle at 60%: shade gone, skew 0,
  ink +2%. Duration is therefore the reader's own scroll
  across ~45vh; at a typical reading glide the visible
  turn takes ~500ms (the original's figure). Reverse
  scroll reverses the shade exactly — a page can be
  turned back.
- **States.** Unturned (below band): shade parked,
  printed complete — a page not yet turned is still a
  printed page, readable if jumped to. Turning: shade
  sweeping. Turned: shade gone, ink settled. Scrolled-
  past: turned state persists (no re-turn on the way
  back down; on the way up the shade returns only in
  the band, symmetrically).
- **Content merge.** The shade falls across the
  section's own top rule and starburst ornament — it
  shades the page furniture first, the type last, and
  never covers body text at more than 12% shade at any
  frame (a hard cap in the gradient stops). The turn is
  something the *page* does, under the reader's hand,
  not a curtain over the words.
- **Failure fallback.** Watchdog per section at 2000ms
  after first intersection: shade parked, ink final.
  No JS: no shade exists; sections print flat — which
  is to say, a brochure lying open, the fallback's own
  dignity.
- **Reduced-motion variant.** No shade, no skew, no ink
  step. Sections are simply present — the open brochure.
- **Performance budget & mobile variant.** One gradient
  layer per visible section, transform/opacity only,
  ≤0.1ms/frame. Mobile: skew halves to −0.6deg and the
  shade's travel halves — a smaller brochure turns
  smaller pages.
- **Choreography timeline (v2).** Section top crosses
  60% viewport → shade at full, skew −1.2° → crosses
  40%: shade at half, ink +1% → crosses 15%: shade
  gone, skew 0, ink +2% — settled. Total travel 45vh.
- **State matrix (v2).** *Rest:* printed, unturned.
  *Hover:* n/a. *Focus:* a section receiving focus
  (skip-link target) is force-settled instantly — a
  keyboard reader never lands on a half-turned page.
  *Active:* n/a. *Scrolled-past:* settled. *Disabled:*
  n/a. *Touch:* identical scrub.
- **Breakpoints (v2).** ≥1200px: full shade + skew.
  768–1199px: shade at 80% depth. <768px: shade at 60%,
  skew −0.6deg.
- **Edge cases & failure modes (v2).** *Anchor jump
  into a section's middle:* the section settles
  instantly (progress computed from position, not
  history). *Very short section (<45vh):* the band
  compresses proportionally; the turn still completes
  within the section's own travel. *Two sections in
  the band at once:* both turn — a spread has two
  pages.
- **Accessibility spec (v2).** Purely decorative layer
  (`aria-hidden`, no focusable content); shade contrast
  never reduces text contrast below the §2 ratios at
  any frame (12% cap, audited). Focus-settle rule above
  is the element's keyboard contract.
- **Tokens consumed (v2).** `--cream-deep`, `--ease-settle`,
  `--curl-skew` (−1.2deg), `--curl-band` (15%–60%).

### 6.5 The pinned fare spread

- **What & why.** The brochure's commercial heart, given
  the salesman's pause: the fare table pins like a
  held-open spread for 120vh while route details scroll
  past in the side column. As the pin begins, the fares
  count up in period table style; last of all — after
  every figure has landed — the footnote prints, letter
  by letter: *"Fares subject to CAB approval and the
  invention of the spacecraft."* It belongs because
  fares are why the brochure exists, and the footnote
  is why the theme is honest. The pin is the one moment
  the page insists on being read slowly.
- **Structure.** A `<section>` with a sticky inner spread
  (`position: sticky`, 120vh of travel): left, the fare
  table itself — a real `<table>`, ruled in teal, money
  column in mono with hung dollar signs, four one-way
  fares and four return fares from the Schedule (§6.17);
  right, a scrolling rail of route details (departure
  times, baggage, the child rule) that translates past
  the pinned table. The footnote is a `<p>` beneath the
  table, in `--red-deep` at 11.5px, fully printed in the
  DOM; its letter-print is a JS-armed mask over finished
  type.
- **Motion spec.** Pin travel 120vh, scrubbed by the
  loop. Fares count over the pin's first 40%: each fare
  counts from 60% of its value to the exact Schedule
  figure over ~700ms `--ease-press`, staggered by row
  in reading order, landing dead and holding (a landed
  fare never moves again — §1's law). The footnote
  prints across the pin's last 30%: letters appear in
  typewriter steps (per-character, ~18ms/char, no
  caret — the counter's machine has no cursor). Route
  rail: translates at 1.0× past the stuck table.
- **States.** Pre-pin: table printed, fares at final
  values (the armed count starts from 60% only when
  the loop arms it — print first). Pinning: counting,
  then footnote printing. Pinned-through: all figures
  landed, footnote complete. Scrolled-past: static
  spread, everything final. Re-entering upward: the
  sequence reverses only in the rail; landed fares do
  NOT un-count — print, once dried, stays.
- **Content merge.** Every figure is the Schedule's
  (§6.17): NY First $4,800, NY Tourist $2,950, SF
  First $5,150, SF Tourist $3,200; returns $8,640 /
  $5,310 / $9,270 / $5,760 — each return exactly
  2 × one-way × 0.9, the printed "10% saving on the
  return Clipper" made arithmetic. The footnote is the
  theme's anti-slop detail, verbatim from the original.
- **Failure fallback.** Watchdog at 2500ms from pin
  start: fares forced to final, footnote fully printed.
  No JS / no sticky support: the spread lays out as a
  normal section, table then footnote, complete. The
  footnote can never be the thing that fails to appear
  — it is the element's reason to exist.
- **Reduced-motion variant.** No pin (the spread flows
  normally), no count (fares printed), no letter-print
  (footnote printed). A reader who asks for stillness
  gets the timetable as timetables are: all at once.
- **Performance budget & mobile variant.** Sticky is
  compositor-cheap; counting writes 8 text nodes over
  700ms; letter-print is a width mask, no reflow of the
  table. Mobile (<768px): **the pin is cut** — a phone
  screen is a single column of a brochure, and a pinned
  spread on it traps the reader; the table flows, the
  rail stacks beneath it, fares print final, footnote
  prints whole. §14's second cut.
- **Choreography timeline (v2).** Pin engages →
  t=0–40% travel: fares count, row by row, landing and
  holding → 40–70%: rail details pass (departures,
  baggage 44 lb, child half fare) → 70–100%: footnote
  prints letter by letter → pin releases with all
  figures final.
- **State matrix (v2).** *Rest:* printed spread.
  *Hover:* rows re-ink (§6.8); a fare row's punch
  target arms. *Focus:* rows are focusable via their
  reservation links (§6.14 anchor); focus lands fares
  instantly if mid-count. *Active:* clicking a fare
  punches it (§6.9) and pre-fills the form (§6.14).
  *Scrolled-past:* final print. *Disabled:* a sold-out
  class (a build-time state) prints "WAIT LIST" in the
  money column — in mono, in red-deep — never a greyed
  row. *Touch:* no pin; tap = punch + pre-fill.
- **Breakpoints (v2).** ≥1200px: pin 120vh, two-column
  spread. 768–1199px: pin 80vh, rail narrows to 260px.
  <768px: no pin; stacked flow.
- **Edge cases & failure modes (v2).** *Reader scrolls
  fast through the pin:* the count is a function of
  pin progress, not time — a fast reader sees fares
  land faster, never wrong; the footnote's print
  compresses to whole words rather than skipping.
  *Footnote longer in a translated build:* the pin's
  last 30% is measured against the footnote's actual
  length; if it cannot fit, the pin extends to 140vh
  before the footnote may truncate — it may never
  truncate. *Sticky unsupported (old WebKit):* graceful
  flow layout, all content present.
- **Accessibility spec (v2).** Real table semantics:
  `<th scope="col">` for class, `<th scope="row">` for
  route; the counting figures carry `aria-label` with
  the final fare so assistive tech never hears a fare
  mid-count; the footnote is plain text in reading
  order, never `aria-hidden`, at 5.89:1. Pin is a
  visual behaviour only — DOM order is table, rail,
  footnote regardless.
- **Tokens consumed (v2).** `--cream`, `--teal`,
  `--teal-deep`, `--red-deep`, `--navy`, `--ease-press`,
  `--pin-travel` (120vh), `--dur-fare-count` (700ms).

### 6.6 Misregistered plates

- **What & why.** The brochure's illustrations are
  lithographs, and lithographs misregister: each plate
  sits in colour passes offset by 2–3px — the red plate
  a breath left, the teal a breath down, against the
  navy key — inside a matted frame with a deckle edge.
  On entry the plate scales 1.05 → 1.0 within its frame
  and the misregistration *breathes* by one pixel, as
  ink settling into paper. It belongs because the
  printing's imperfection is the period's authenticity:
  a perfectly registered "1962" image is a 2026 image
  in costume. The flaw is the proof.
- **Structure.** A `<figure>` with three stacked layers
  of the same SVG illustration (or one SVG with three
  `<use>` passes), each pass a single flat colour
  (red, teal, navy-key on top), offset via transform:
  red (−2px, +1px), teal (+2px, +2px), key (0,0) at
  desktop registration. The frame: `--cream-deep` mat
  20px, gold hairline inner rule, deckle mask on the
  outer edge (§4). Caption beneath in Caslon italic
  with the plate number in mono ("PLATE IV — THE
  CLIPPER AT THE TERMINAL"). Illustrations are drawn
  for the theme (clipper, terminal, stewardess service,
  the Earth from the porthole) — never stock photography,
  never a photograph at all (§1).
- **Motion spec.** Entry (scroll into view, scrubbed
  across the plate's first 30vh of travel): scale 1.05
  → 1.0 `--ease-settle`; simultaneously the red pass
  offset walks (−3px → −2px) and teal (+3px → +2px) —
  the plates *settle into* registration without ever
  reaching it (perfect registration is not available
  in 1962; the settled state keeps its 2px truth).
  Ambient: a ±0.5px breathing of the offsets on a 7s
  sine, felt rather than seen — ink in paper, alive.
  Hover/tilt per below.
- **States.** Rest: settled at 2px misregistration.
  Entering: scaling + settling. Hover: the plate tilts
  like a brochure lifted off the counter — rotateX/Y
  from pointer position, max 3°, lerped at 0.08 (paper
  is heavy; it does not snap) — and re-inks (§6.8).
  Scrolled-past: settled, breathing continues only
  in-viewport. Focus (plates with links): tilt does
  not follow the keyboard; the frame's gold rule
  deepens instead.
- **Content merge.** Each plate illustrates its own
  section's claim and is captioned as evidence: the
  terminal plate stands beside the terminal's
  description with its altitude in the caption; the
  porthole plate's Earth is drawn at the Schedule's
  300 miles — the curvature in the drawing is the
  record's number, pictured. A plate that could move
  to another section unchanged is decoration and is
  cut (§9).
- **Failure fallback.** Watchdog at 1800ms: plate
  forced to settled state (scale 1.0, 2px offsets).
  If SVG fails entirely, the figure falls back to its
  caption + a flat navy key-pass silhouette (the
  illustration's `<img>` fallback carries real `alt`).
  No JS: settled state, static.
- **Reduced-motion variant.** Settled plate, no entry
  scale, no breathing, no tilt. The lithograph in its
  frame, looked at.
- **Performance budget & mobile variant.** Three
  composited layers, transforms only; breathing is one
  variable pair per in-view plate, ≤0.1ms. Mobile:
  offsets halve (1px/1.5px — at small sizes 3px is a
  blur, not a charm), tilt is cut (no pointer), entry
  scale narrows to 1.02 → 1.0.
- **Choreography timeline (v2).** Plate enters →
  scale 1.05, offsets at 3px → across 30vh: scale →
  1.0, offsets → 2px, caption prints last (70ms after
  settle) → rest: breathing ±0.5px, 7s.
- **State matrix (v2).** *Rest:* settled, breathing.
  *Hover:* tilt ≤3°, re-ink. *Focus:* gold rule
  deepens, no tilt. *Active:* n/a (linked plates
  navigate on the link, the plate does not press).
  *Scrolled-past:* settled. *Disabled:* a plate whose
  image fails prints its caption and key silhouette —
  an empty frame is a printing error the brochure
  admits, never a broken-image icon. *Touch:* no tilt;
  entry settle identical.
- **Breakpoints (v2).** ≥1200px: offsets 2–3px, mat
  20px. 768–1199px: offsets 2px, mat 16px. <768px:
  offsets 1–1.5px, mat 12px, tilt off.
- **Edge cases & failure modes (v2).** *Duotone
  source art that fights the passes:* art is authored
  in the three plate colours at build time; a
  full-colour image dropped into a plate is a build
  error the gate catches (§10) — the press prints
  three colours, not four-process. *Plate taller than
  viewport:* settle progress measured on its first
  30vh regardless. *Print:* plates print at settled
  registration — misregistration reproduces faithfully
  on paper, which is where it always lived.
- **Accessibility spec (v2).** Real `alt` written as a
  brochure caption ("The Clipper Morning Star docked
  at the orbital terminal, 300 miles above the
  Earth"); offsets and tilt are decorative and
  `aria-hidden` at the layer level; caption text is
  navy on cream, 11.32:1. Tilt never moves text —
  plates carry no text inside the art except the
  ship's name, lettered in cream on red at display
  size.
- **Tokens consumed (v2).** `--red`, `--teal`,
  `--navy`, `--gold`, `--cream-deep`, `--ease-settle`,
  `--misreg` (2px), `--tilt-max` (3deg).

### 6.7 The altitude climb readout

- **What & why.** On the cover's corner plate, a mono
  readout counts the climb: **ALT 0 → 62 MILES**, in
  step with a small cover orbit arc along which a
  miniature clipper rises. Sixty-two is the Schedule's
  edge-of-space milestone (§6.17) — the altitude at
  which, fifteen minutes into PA-101, the brochure
  says the sky turns black. It belongs because the
  brochure's promise is quantified on its own cover:
  the flight begins, measurably, before the first
  scroll.
- **Structure.** A corner plate on the hero (§6.1):
  label "ALTITUDE" (Archivo caps 9px), the figure in
  IBM Plex Mono 22px tabular with "MILES" in 10px
  beside it, and a 120px SVG arc (quarter orbit, dotted
  teal) with the mini-clipper as a `<g>` the loop
  positions along it. The figure and the ship read one
  progress value — the ship's arc position and the
  number can never disagree, because both are the same
  variable printed two ways.
- **Motion spec.** Trigger: load, beginning at t=900ms
  of the hero choreography (§6.1), after the headline
  has set — the instruments start once the cover is
  printed. Duration 2400ms, ease `--ease-press` on the
  *rate* (fast off the pad, settling at the milestone —
  the count's increments shrink as 62 approaches, like
  a needle damped at its stop). The count passes the
  Schedule's own milestones in order — 10 (t+4 min in
  the fiction's compressed time), 40, 62 — and holds
  at 62. It never counts past 62: the cover promises
  the edge of space; the 300 miles belong to the
  margin instrument (§6.3) and the voyage table
  (§6.13).
- **States.** Rest (pre-arm): printed "62 MILES" —
  the brochure's cover, unanimated, already tells the
  truth. Climbing: counting. Held: 62, with a printed
  tick "EDGE OF SPACE" appearing beneath in red-deep
  9px caps at the hold. Scrolled-past and back: holds
  — a flown climb is not re-flown on the same visit;
  the returning-visitor flag (§6.1) starts it held.
- **Content merge.** Every milestone is the ascent
  profile's (§6.17): 10 mi at 4 minutes, 40 at 10,
  62 at 15. The readout is the voyage table's first
  column, performed on the cover.
- **Failure fallback.** Watchdog at 3000ms from arm:
  figure forced to 62, tick printed, ship parked at
  the arc's top. No JS: printed 62. The readout's
  failure mode is its own resting face.
- **Reduced-motion variant.** Printed 62 with the tick;
  the ship sits at the arc's top. No count.
- **Performance budget & mobile variant.** One text
  node + one transform per frame for 2.4s, then zero —
  the instrument sleeps at its hold. Mobile: the
  corner plate shrinks (figure 18px, arc 84px) and
  moves to the cover's bottom-left, clear of the
  seal's new inline position (§6.1).
- **Choreography timeline (v2).** t=900 count begins
  (fast) → 10 passes at ~t=1400 → 40 at ~t=2300 →
  increments damping → t=3300: 62 lands, tick prints
  150ms later → hold, loop unsubscribes the element.
- **State matrix (v2).** *Rest:* 62 printed. *Hover:*
  none. *Focus:* n/a. *Active:* n/a. *Scrolled-past:*
  held. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 22px figure, 120px
  arc. 768–1199px: 20px, 100px. <768px: 18px, 84px,
  bottom-left placement.
- **Edge cases & failure modes (v2).** *Tab hidden
  mid-climb:* rAF pauses; on return the watchdog's
  deadline (wall-clock) forces the hold — the reader
  never returns to a half-climbed cover. *Reduced
  data / no loop:* printed state, as above.
- **Accessibility spec (v2).** The live figure is
  `aria-hidden`; the cover carries a visually-hidden
  line: "The Clipper reaches the edge of space, 62
  miles up, fifteen minutes after leaving Idlewild."
  — the Schedule's fact, stated once, statically.
- **Tokens consumed (v2).** `--navy`, `--red-deep`,
  `--teal`, `--ease-press`, `--dur-climb` (2400ms),
  `--edge-of-space` (62).

### 6.8 Re-ink hover — the second impression

- **What & why.** Hovering any panel, card, row or
  button deepens its print: saturation and ink density
  rise ~12% over 250ms, as if the press struck the
  element a second time. It belongs because attention
  in a print shop is *pressure* — the visitor's
  interest lands on the element as ink, in the
  element's own colours. It is the theme's universal
  hover language: one behaviour, every surface, always
  the element's own print getting heavier.
- **Structure.** A CSS-only treatment on the `.inkable`
  class: `filter: saturate(1.12) contrast(1.03)` plus
  a 1px deepening of the element's key colour via a
  pre-computed `--ink-deep` custom property per
  component (red elements deepen toward `--red-deep`,
  teal toward `--teal-deep`, navy text toward pure
  ink). Transitions on filter only — no layout, no
  shadow bloom (a shadow is light; ink is weight).
- **Motion spec.** 250ms `--ease-press` in, 350ms out
  (the second impression lands faster than it lifts —
  paper keeps a little of the ink). Focus-visible gets
  the identical treatment plus the standard 2px navy
  outline at 2px offset: focus is a firmer strike of
  the same press.
- **States.** Rest: single impression. Hover: second
  impression. Focus: second impression + outline.
  Active (pressed): a third, brief strike — saturate
  1.18 for 120ms — before the element's own action
  (and, on fares/CTAs, the punch, §6.9). Disabled:
  no re-ink, ever — an element that cannot be used is
  printed once, lightly (85% ink), and says so in its
  label, not just its colour.
- **Content merge.** The deepening uses the element's
  own inks; nothing glows, nothing lifts, no foreign
  colour arrives. On plates (§6.6) the re-ink joins
  the tilt; on table rows it inks the row's figures;
  on the form's fields it inks the field's rule.
- **Failure fallback.** None required — CSS hover
  cannot strand content; with no CSS the brochure is
  single-impression throughout, which is how most
  brochures in the world are printed anyway.
- **Reduced-motion variant.** The deepening still
  applies (it is a colour-value change, not motion)
  but switches instantly, no 250ms ramp.
- **Performance budget & mobile variant.** Filter on
  hover targets only; will-change is never set (the
  press does not idle its rollers). Touch: no hover —
  the first tap on a card strikes the second
  impression as the tap lands; navigation proceeds on
  the same tap for links (the ink is a receipt, not a
  toll).
- **Choreography timeline (v2).** Pointerenter →
  t=250 fully re-inked → hold → leave → t=350 back to
  single impression. Press: +120ms third strike →
  action fires.
- **State matrix (v2).** *Rest:* single impression.
  *Hover:* +12%. *Focus:* +12% + outline. *Active:*
  +18% for 120ms. *Scrolled-past:* n/a. *Disabled:*
  85% ink, no response. *Touch:* tap-strike as above.
- **Breakpoints (v2).** Identical at all widths; the
  treatment is a property of ink, not of layout.
- **Edge cases & failure modes (v2).** *Filter on
  large plates:* the plate's filter applies to its
  frame group, not the full-bleed sky (cost cap,
  §6.6's budget). *Printed (paper) output:* hover
  states do not exist; the stylesheet prints single
  impression.
- **Accessibility spec (v2).** Re-ink never carries
  state alone — hoverables are real links/buttons
  with real labels; the focus outline is the visible
  indicator and meets 11.32:1. Deepened colours stay
  within §2's audited pairings (red-deep 5.89:1 is
  the floor for any text-bearing element).
- **Tokens consumed (v2).** `--red-deep`, `--teal-deep`,
  `--navy`, `--ease-press`, `--dur-reink` (250ms).

### 6.9 Ticket-punch click

- **What & why.** Clicking a fare or a CTA stamps a
  small circular notch into the element's edge — a
  punched hole with a paper shadow inside it — and
  sets "PUNCHED" in tiny mono type beside the fare.
  It belongs because booking, in 1962, was a physical
  act performed on the ticket itself: the conductor's
  punch made the paper yours. The theme's conversion
  ritual is that punch — the transaction performed in
  the period's own ceremony, on the element the
  visitor actually chose.
- **Structure.** The notch is a radial-gradient mask
  circle (14px) bitten into the element's top-right
  edge plus an inner `box-shadow` crescent in
  `--cream-deep` (the hole's paper thickness); the
  "PUNCHED" stamp is a real text span in mono 9px,
  `--red-deep`, rotated −4°, printed beside the fare
  figure. State lives in a `data-punched` attribute;
  on fares it also writes the chosen route/class into
  the reservation form (§6.14) — the punch and the
  paperwork are one act.
- **Motion spec.** The punch lands in 180ms
  `--ease-press`: the element dips 1px (the punch's
  pressure), the notch bites (mask position steps in
  two frames — a punch is a *snap*, not a fade), the
  stamp prints at 120ms with the ink squash at
  miniature scale (1.06 → 1.0). A soft paper *tick* is
  the only sanctioned sound in the theme, and it is
  off by default (sound is never required to complete
  the metaphor).
- **States.** Unpunched: clean edge. Punched: notch +
  stamp, persistent for the session. Re-clicking a
  punched fare un-punches nothing — a punched ticket
  is punched; instead the click scrolls the visitor
  to the form where the choice already waits (§6.14).
  Disabled (wait-list class): the click prints
  "WAIT LIST" beside the fare instead — the punch is
  refused, in print, honestly.
- **Content merge.** The punch lands on the fare the
  visitor chose, at the edge of its own row/card, and
  its consequence is that fare appearing in the form.
  It is not a confetti layer over the page; it is a
  mark on the document, in the document's margin.
- **Failure fallback.** The punch is a class swap; if
  JS is absent, fare links are plain anchors to the
  form with the choice in the query string — the
  paperwork still arrives, unpunched. Nothing about
  the transaction depends on the notch.
- **Reduced-motion variant.** Notch and stamp appear
  instantly, no dip, no squash. The mark matters, not
  its landing.
- **Performance budget & mobile variant.** Mask +
  transform on one element per click; negligible.
  Touch: identical — a tap is a punch, which is why
  the metaphor survives the phone intact.
- **Choreography timeline (v2).** Click → t=0 dip 1px
  → t=60 notch bites → t=120 stamp prints → t=180
  element settles, form pre-filled (§6.14) → the
  visitor's eye is offered the form link in the
  stamped row ("Complete your reservation ↓").
- **State matrix (v2).** *Rest:* clean. *Hover:*
  re-ink (§6.8); the edge shows a faint dotted
  punch-guide circle — where the punch *would* land,
  printed at 30% ink. *Focus:* guide circle full ink
  + outline. *Active:* the punch sequence. *Scrolled-
  past:* punch state persists. *Disabled:* wait-list
  print instead. *Touch:* tap = punch.
- **Breakpoints (v2).** Notch 14px ≥768px, 12px below;
  stamp 9px everywhere (it is fine print, sized like
  it).
- **Edge cases & failure modes (v2).** *Two fares
  punched:* the second punch moves the reservation —
  the first row's stamp prints "VOID" in mono beside
  it (a reissued ticket voids the old stub; the
  brochure shows its working). *Form already
  submitted:* punches disable and print "RESERVED"
  — the ledger (§6.14) has the name.
- **Accessibility spec (v2).** The punch is decoration
  on a real button whose accessible name includes the
  choice ("Reserve New York – Orbit, First Class,
  $4,800"); the stamp text is real text, read as
  "Punched"; `aria-pressed` carries the toggle state
  for the fare selectors. The notch never overlaps
  the fare figure (edge placement is in the build
  spec, audited in §10).
- **Tokens consumed (v2).** `--red-deep`, `--cream-deep`,
  `--navy`, `--ease-press`, `--punch-size` (14px).

### 6.10 The dot-star sky

- **What & why.** The hero's sky is not a gradient —
  it is lithograph dots, and a few of its dot-stars
  breathe (dot density pulsing gently) while one
  shooting dot-star crosses on a long ~20s loop. It
  belongs because in this brochure even the heavens
  are printed: the sky obeys the same halftone physics
  as the exhaust and the plates. It is the theme's
  ambient signature — the quietest element on the
  page, and the one that proves the whole sky is
  paper.
- **Structure.** Part of the hero SVG (§6.1): the sky
  is a `<pattern>` halftone field; above it, ~14
  individual star dots (circles, r 1.5–3px, gold and
  cream) placed on the pattern's own grid — a star is
  a dot that grew, never an alien sparkle shape. Five
  carry the breathing class; one shooting star is a
  3-dot comet (head + two fading trail dots) on a
  diagonal path across the plate's top corner.
- **Motion spec.** Breathing: dot radius oscillates
  ±30% on individual 3.2–4.7s sines (staggered phases;
  a sky does not breathe in unison), opacity steady —
  density, not brightness: the dot *prints heavier*.
  Shooting star: crosses in 900ms `--ease-glide`,
  once per 20s loop, at a randomised offset within
  the top corner's band so repeat viewings differ;
  trail dots lag 90ms apart. Both run only while the
  hero is in the viewport.
- **States.** Rest: static printed sky. Ambient:
  breathing + the 20s crossing. Scrolled-past:
  paused (loop skips). Any state: the sky never
  darkens the headline's contrast zone — stars are
  kept out of the headline's bounding plate by the
  art's own layout, a build rule (§10), not a runtime
  check.
- **Content merge.** The stars are the halftone
  pattern's own dots, enlarged — the sky and the
  exhaust (§6.1) are one printing system at two
  scales. The shooting star crosses toward the
  clipper's nose: even the omens in this sky point
  at the ship.
- **Failure fallback.** Static sky — the pattern is
  declarative SVG; if the loop dies the stars simply
  hold their printed sizes. No watchdog needed for an
  element whose failure state is its printed state.
- **Reduced-motion variant.** No breathing, no
  shooting star. A printed sky, still as paper.
- **Performance budget & mobile variant.** ≤15 nodes
  animated via one CSS-variable radius each; ≤0.05ms/
  frame. Mobile: breathing stars reduce to 3, the
  shooting star's loop lengthens to 30s (a smaller
  sky, a rarer omen).
- **Choreography timeline (v2).** Continuous: breaths
  phase-staggered from load → t≈20s shooting star
  crosses (900ms) → loop. On hero exit: all pause
  mid-phase; on return: resume — the sky does not
  restart its weather for anyone.
- **State matrix (v2).** *Rest:* printed sky.
  *Hover:* none. *Focus:* none. *Active:* none.
  *Scrolled-past:* paused. *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: 14 stars, 5 breathing.
  768–1199px: 10 stars, 4 breathing. <768px: 8 stars,
  3 breathing, 30s crossing loop.
- **Edge cases & failure modes (v2).** *Pattern
  rendering differences:* star dots are explicit
  circles, not pattern-dependent — the named stars
  exist even if a browser renders the field coarsely.
  *Photosensitivity:* radius oscillation on ≤3px
  dots at ≤0.3Hz is orders below flash thresholds;
  audited in §10 regardless.
- **Accessibility spec (v2).** Entirely decorative,
  inside the hero SVG's `role="img"` description
  (§6.1); no information is carried by any star.
- **Tokens consumed (v2).** `--gold`, `--cream`,
  `--ease-glide`, `--star-loop` (20s).

### 6.11 Brochure masthead & port index — navigation

- **What & why.** The brochure's masthead is its cover
  furniture made permanent: a slim top bar carrying
  the wordmark ("PAN AMERICAN — CLIPPER SERVICE TO
  ORBIT", Archivo caps), the port index (the sections
  named as ports of call), and — below 1200px, where
  the margin cannot hold it — the miles readout
  (§6.3). The current port is marked by a small
  printed clipper glyph beside its name. It belongs
  because a brochure's reader orients by its index of
  plates and ports, not by a "menu": navigation here
  is the timetable's own contents page, kept open at
  the top.
- **Structure.** A `<header>` with real `<nav>`: wordmark
  left (link to cover), port links centre/right in
  Archivo caps 12px tracked, the current port's link
  in navy with the clipper glyph (a 14px SVG, red) and
  `aria-current="location"`; the scrollspy reads the
  same section-boundary table as the orbit line (§6.2)
  — one source of "which port am I at" for bar, line
  and altimeter. The bar's ground is cream at 96% with
  a teal hairline under-rule — paper, held up to the
  light.
- **Motion spec.** Bar entrance: prints in with the
  cover (no separate animation — furniture arrives
  with the object). Scrollspy changes: the glyph
  *lifts* from the old port and sets down at the new
  one over 300ms `--ease-glide` (a translate between
  the two links' positions, measured at runtime), the
  old name returns to teal-deep, the new name inks to
  navy over 200ms. On scroll the bar's ground firms
  to solid cream (the counter's edge shadow appears,
  600ms) so print over moving paper stays legible.
  No hide-on-scroll — a contents page does not hide
  from its reader.
- **States.** Rest: current port marked. Hover: links
  re-ink (§6.8). Focus: re-ink + outline. Active
  (current): glyph + navy + `aria-current`. A port
  whose section is unpublished prints in teal-deep at
  60% ink with no link — an index entry for a plate
  not yet printed, admitted in the index itself.
- **Content merge.** The ports are the sections'
  real names from the Schedule's structure (The
  Clipper, The Voyage, Life Aboard, Fares,
  Reservations); the glyph is the same clipper that
  flies the margin line (§6.2) — one ship, two
  duties, never two different ships.
- **Failure fallback.** Watchdog: if scrollspy has
  not fired within 1000ms of load, the first port is
  marked (the reader is at the cover; that is never
  wrong). No JS: no glyph, all links printed and
  working; current-port marking is lost, navigation
  is not.
- **Reduced-motion variant.** The glyph steps between
  ports instantly; name colour changes are instant.
- **Performance budget & mobile variant.** Scrollspy
  via IntersectionObserver, zero per-frame cost.
  Mobile (<768px): the bar holds wordmark (shortened
  to "PAN AM · ORBIT"), the miles readout (§6.3), and
  a "PORTS" button opening a full-width index panel
  printed on `--cream-deep` — the brochure's contents
  page, unfolded — 250ms `--ease-glide`, links at
  ≥44px targets.
- **Choreography timeline (v2).** Load → bar printed
  with cover → first scroll: ground firms → boundary
  crossed: glyph lifts 300ms, names cross-ink 200ms
  → footer: last port marked as the ship docks (§6.2).
- **State matrix (v2).** *Rest:* current marked.
  *Hover:* re-ink. *Focus:* re-ink + outline.
  *Active:* current port as above. *Scrolled-past:*
  n/a (sticky). *Disabled:* unprinted port, dimmed,
  unlinkable. *Touch:* panel form below 768px.
- **Breakpoints (v2).** ≥1200px: full bar, miles in
  margin. 768–1199px: full bar, miles in bar.
  <768px: wordmark + miles + PORTS panel.
- **Edge cases & failure modes (v2).** *Long port
  names in translation:* below 9px-equivalent spacing
  the bar abbreviates to port numbers (PORT III) with
  full names in the panel — the index never wraps to
  two lines. *Glyph travel across a hidden link:*
  positions measured after layout; if a link is
  display:none the glyph steps instead of flying.
- **Accessibility spec (v2).** Landmark header + nav
  with `aria-label="Ports of call"`; skip link first,
  printed navy on `--cream-deep`, visible on focus;
  the glyph is `aria-hidden` — current-ness lives in
  `aria-current`, not in the picture. Link contrast:
  teal-deep 7.96:1 at rest, navy 11.32:1 current.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--teal-deep`, `--navy`, `--red`, `--ease-glide`,
  `--dur-glyph` (300ms).

### 6.12 Port-of-call cards

- **What & why.** The brochure's interior sells the
  journey port by port, and each port gets a card:
  a small plate (misregistered, §6.6), the port's
  name, its altitude or hour from the Schedule, and
  two lines of service copy — "AT 62 MILES the sky
  turns black, and luncheon is served." The cards are
  the itinerary made browsable: the ports of PA-101's
  ascent and the sections of the site, one object
  serving as both timetable and index. It belongs
  because a brochure's reader decides by flipping —
  the cards are the flip, given a grid.
- **Structure.** A `<ul>` of `<li>` cards on cream,
  each an `<article>` with one link (to the port's
  section or detail page): plate area (three-pass
  SVG, §6.6 treatment at card scale), port name in
  Archivo semibold 20px, the Schedule datum in mono
  (altitude, or departure time, or fare-from), copy
  in Caslon 15.5px. The card's whole surface is the
  link; the datum is set in a ruled mono strip at the
  card's foot — the timetable line under the picture
  postcard.
- **Motion spec.** Cards print in on scroll in
  imposition order (§5), 90ms stagger, each with the
  page-curl shade at card scale (§6.4's treatment,
  40vh band compressed to the card's own height).
  Hover: re-ink (§6.8) + the plate's tilt at card
  scale (max 2° — a postcard, not the whole
  brochure). The datum strip never animates: times
  and altitudes are print.
- **States.** Rest: printed card. Hover: re-inked,
  tilted. Focus: re-ink + outline on the card.
  Active: the card's link follows; a card for the
  Fares port carries a punch target (§6.9) in its
  corner when it quotes a fare. Scrolled-past:
  printed. Disabled: a port not yet served (a
  build-time state — "SERVICE FROM 1966") prints
  its plate in key-pass only (uncoloured — the
  plate awaits its colours) with the notice in the
  datum strip.
- **Content merge.** Every card's datum is a
  Schedule line (§6.17): the ascent ports carry the
  profile's altitudes (10 / 40 / 62 / 300), the
  route ports carry departures (09:30 EST), the
  Fares card carries "FROM $2,950" — the Schedule's
  lowest fare, never an invented "from" price.
- **Failure fallback.** Cards are static HTML with
  CSS hover; the print-in is loop-armed over
  finished cards. Watchdog 1500ms per card batch.
  No JS: printed grid, complete.
- **Reduced-motion variant.** No stagger, no tilt;
  cards print as a block with their section.
- **Performance budget & mobile variant.** Grid: 3
  columns ≥1200px, 2 at 768–1199px, 1 below 768px.
  Tilt math is two lerped values on the one hovered
  card. Mobile: tilt off; the plate crops to 16:9;
  datum strip stays full-width (times do not shrink
  below 13px mono).
- **Choreography timeline (v2).** Section enters →
  cards print in imposition order, 90ms apart →
  rest → pointer: re-ink 250ms, tilt lerps in →
  leave: tilt settles 500ms `--ease-settle`.
- **State matrix (v2).** *Rest:* printed. *Hover:*
  re-ink + 2° tilt. *Focus:* re-ink + outline, no
  tilt. *Active:* link follows. *Scrolled-past:*
  printed. *Disabled:* key-pass plate + notice.
  *Touch:* no tilt; tap follows the link.
- **Breakpoints (v2).** ≥1200px: 3-col, tilt 2°.
  768–1199px: 2-col, tilt 2°. <768px: 1-col, no
  tilt, plate 16:9.
- **Edge cases & failure modes (v2).** *A port with
  no plate art:* the card prints a starburst seal in
  the plate area with the port's number — an
  unillustrated plate is a numbered blank, never a
  stock photo (§1: no photographs). *Copy longer
  than two lines:* the card grows; the datum strip
  stays pinned to the card's foot by flex — the
  timetable line never floats mid-card.
- **Accessibility spec (v2).** One link per card with
  a complete accessible name ("The Voyage — 62 miles
  at fifteen minutes — read the ascent"); plate
  `aria-hidden` (its facts are in the name and
  datum). Focus outline on the card itself. Text
  contrasts per §2.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--navy`, `--teal-deep`, `--red-deep`, `--ease-settle`,
  `--dur-reink` (250ms).

### 6.13 The ascent table — the voyage, tabulated

- **What & why.** For the reader who wants the flight
  plain: a true timetable of PA-101's ascent — phase,
  elapsed time, altitude, and what is served or seen
  — printed in mono with ruled lines, a totals row
  carrying the Schedule's 2 h 05 min. It belongs
  because a brochure that cannot be read as a
  timetable is a poster; the table is the theme's
  honesty made structural, the same discipline as
  §6.5's fares but for time. Its one theatre: the
  row for 62 miles — the edge of space — is ruled in
  red, the table's single red rule.
- **Structure.** A semantic `<table>` with caption
  ("PA-101 — New York (Idlewild) to Orbit, daily"),
  scoped headers, four phase rows from the Schedule
  (§6.17): Liftoff–10 mi (4 min), 10–40 mi (6 min),
  40–62 mi (5 min), Coast & rendezvous (1 h 50 min);
  a `<tfoot>` totals row: 2 h 05 min, 300 miles,
  arrival 11:35 EST. Beside the table (desktop), the
  route-map plate: an SVG arc from Idlewild to the
  terminal that strokes itself as the table is read
  (§5's line-draw), its milestone dots at the rows'
  altitudes. On mobile the plate stacks above the
  table, pre-drawn.
- **Motion spec.** The table itself does not perform
  — no reveal beyond its section's curl (§6.4). The
  companion arc draws across the table's reading
  travel (stroke-dashoffset scrubbed by the loop,
  0.11 lerp): as the reader's eye descends the rows,
  the ship's route completes above them. Row hover:
  the row inks to `--cream-deep` over 200ms and the
  arc's corresponding milestone dot fills red —
  table and map are two printings of one record, and
  hover proves it.
- **States.** Rest: printed table, arc drawn to the
  reader's progress. Hover (row): ink + dot. Focus:
  rows are not focusable; the caption's detail link
  (to the full timetable page, §7) re-inks per §6.8.
  Scrolled-past: arc complete. Disabled: a phase
  not yet flown in a build's fiction (none in the
  canonical Schedule) would print "—" in the time
  column with the note in the caption; the canonical
  table has no such row and invents none.
- **Content merge.** The rows ARE §6.17's ascent
  profile; 4 + 6 + 5 + 110 = 125 minutes = the
  totals row's 2 h 05 min, and 09:30 + 2:05 = the
  printed arrival 11:35. The arc's milestones sit at
  10 / 40 / 62 / 300 because the rows say so. §10's
  gate re-adds the column.
- **Failure fallback.** None required — static HTML,
  CSS hover. The arc ships fully drawn in the DOM;
  the scrub only ever *un*-draws ahead of the reader
  from the shipped complete state, so a dead loop
  leaves a complete map. No JS: complete map.
- **Reduced-motion variant.** Arc printed complete;
  row hover is an instant ink change.
- **Performance budget & mobile variant.** One
  dashoffset write per frame while the section is in
  view. Mobile (<768px): the table becomes a stacked
  phase list (definition-list layout, same order,
  same totals row as a ruled final block) — a
  timetable you must side-scroll is a timetable
  lost; no horizontal scroll is ever permitted.
- **Choreography timeline (v2).** Section curl
  (§6.4) → table at rest, arc at reader's fraction →
  rows pass: arc completes → totals row enters: the
  arc's terminal dot prints its starburst.
- **State matrix (v2).** *Rest:* printed. *Hover:*
  row ink + milestone. *Focus:* caption link only.
  *Active:* n/a. *Scrolled-past:* complete.
  *Disabled:* n/a in the canonical record. *Touch:*
  tap on a row inks it for 600ms (no arc scrub
  change).
- **Breakpoints (v2).** ≥1200px: table + arc plate
  side by side. 768–1199px: arc above, table full
  measure. <768px: stacked phase list.
- **Edge cases & failure modes (v2).** *A fifth
  phase added by an editor:* the totals row is
  build-computed from the rows, never authored —
  the table cannot disagree with itself. *Print:*
  the table is the print stylesheet's centrepiece
  (§14): full rules, arc complete, red rule at 62.
- **Accessibility spec (v2).** Full table semantics
  with caption and scoped headers; the totals row
  is a `<tfoot>` with `scope="row"`. The arc is
  `aria-hidden` beside a visually-hidden sentence
  carrying the same facts. Contrasts: navy on cream
  11.32:1; the red rule is a rule, not text.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--teal`, `--red`, `--navy`, `--ease-glide`.

### 6.14 The reservation form & its punched confirmation

- **What & why.** The brochure's conversion, kept in
  period: a reservation coupon — the kind a 1962
  reader would clip and mail — rendered as a working
  form. Name, route, class, party size, and the
  deposit acknowledged ($250 per seat, §6.17). On
  submit, the confirmation is a punched ticket stub:
  "RESERVATION № 1,209 — CLIPPER MORNING STAR,
  PA-101" — the number derived in print before the
  visitor's eyes, because the form's preamble reads
  "Reservations on file: 1,208. Yours will be №
  1,209." It belongs because the brochure's whole
  journey — cover, voyage, fares — exists to arrive
  at this coupon, and the coupon honours the law:
  the number is a kept promise, not a surprise.
- **Structure.** A real `<form>` styled as the
  coupon: dashed clip-line border (the scissors line
  is drawn, with a small scissors glyph — the one
  joke the brochure permits itself, in print since
  1962), fields on cream with navy rules, labels in
  Archivo caps. Route and class are selects whose
  options carry the Schedule's fares in mono; a fare
  punched earlier (§6.9) pre-selects its row. The
  deposit line computes live from party size (n ×
  $250, mono, tabular). Submit is a real button,
  "RESERVE MY SEAT", which punches (§6.9) as it
  submits.
- **Motion spec.** Field focus: the field's rule
  inks teal-deep and thickens 1px → 2px over 200ms.
  Deposit figure: counts 150ms `--ease-press` when
  party size changes — money being typed onto the
  coupon. Submit: the button punches (180ms, §6.9),
  the coupon dims to 85% ink while "the counter
  writes" (a mono line prints "WRITING TO THE
  LEDGER…" — never a spinner; counters write, they
  do not spin). Success (≤ the 4000ms watchdog): the
  coupon region swaps to the ticket stub — notch,
  stamp, № 1,209, the chosen route/class/fare
  reprinted from the Schedule — rising 400ms
  `--ease-settle`. Error: the offending field's
  label gains the red-deep asterisk of the ledger
  and its error line prints beneath in Caslon —
  "The counter needs your name to hold the seat." —
  no shake, no red field flood, ever.
- **States.** Rest: coupon printed, preamble showing
  № 1,209. Focus: rule inks. Submitting: dimmed,
  writing line, fields disabled. Success: the stub.
  Error: marked fields, values preserved, focus to
  the first error. Ledger-closed (endpoint down /
  watchdog fired): the coupon prints the note "The
  counter is closed for the evening; your coupon is
  kept, unmailed, exactly as you wrote it." with
  values intact and a retry control.
- **Content merge.** The form's options ARE the
  Schedule's routes and fares; its deposit is the
  Schedule's $250; its issued number is the ledger's
  count + 1, and on success the Schedule block on
  the page (§6.17's printed form) and the preamble
  update to 1,209 on file — the brochure's own
  record absorbs the visitor's act, in print.
- **Failure fallback.** Watchdog 4000ms on submit:
  restore from dimmed state, print the counter-
  closed note, values intact, idempotent submit
  token prevents a double reservation. No JS:
  native POST to the endpoint; the confirmation is
  a server-rendered stub page with the same number
  logic. Canvas: irrelevant — the coupon is DOM.
- **Reduced-motion variant.** Confirmation prints
  instantly; the deposit figure changes without
  counting; the punch is instant (§6.9's variant).
- **Performance budget & mobile variant.** Form JS
  ≤5KB gz deferred; the deposit count is one text
  node. Mobile: single column, coupon full measure,
  the clip-line becomes a plain dashed rule (the
  scissors glyph is cut — §14's mobile trims the
  joke before the function), submit full-width,
  targets ≥48px.
- **Choreography timeline (v2).** Focus → rule inks
  200ms → party size changes → deposit counts 150ms
  → submit → punch 180ms → dim + writing line →
  response → stub rises 400ms, № 1,209 printed →
  ledger count on page updates to 1,209.
- **State matrix (v2).** *Rest:* coupon + № promise.
  *Hover:* fields re-ink (§6.8). *Focus:* rule inks
  + outline. *Active:* submitting state above.
  *Scrolled-past:* waits; an in-flight submission
  completes. *Disabled:* counter-closed note,
  values held. *Touch:* identical; ≥48px fields.
- **Breakpoints (v2).** ≥1200px: two-column coupon
  (route/class paired), measure 46rem. 768–1199px:
  single column, 40rem. <768px: full measure,
  scissors cut, submit sticky at the coupon's foot.
- **Edge cases & failure modes (v2).** *Party of
  24+ (a full clipper):* the coupon accepts the
  booking and the stub prints "PARTY OF n — THE
  WHOLE CLIPPER" with the deposit n × $250 computed
  the same way; the brochure does not scold a
  charter. *Fare punched, then class changed in the
  form:* the stub prints the form's final choice
  and the earlier punch prints VOID (§6.9) — one
  reservation, one truth. *Duplicate submit:* the
  idempotent token returns the same № 1,209 stub —
  the ledger does not sell one seat twice.
- **Accessibility spec (v2).** Visible labels on
  every field (Archivo caps, navy, 11.32:1); errors
  via `aria-describedby` + an `aria-live="polite"`
  summary in the counter's voice; the stub is an
  `aria-live` region announcing "Reservation number
  1,209" once. Focus management: error → first
  invalid field; success → stub heading. The
  deposit figure is `aria-live="off"` with its
  label ("Deposit due") read on demand — a ticking
  price is never shouted.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--navy`, `--teal-deep`, `--red-deep`, `--gold`,
  `--ease-press`, `--ease-settle`, `--dur-watchdog-form`
  (4000ms).

### 6.15 Unprinted blanks — loader & the page-curl transition

- **What & why.** Loading, in a print shop, is an
  unprinted sheet: regions still arriving show as
  brochure blanks — cream sheets with plate-shaped
  voids and ruled lines where type will sit — and as
  each region's content lands, the blank *inks in*.
  The page transition is the same physics at full
  scale: leaving a page, a page-curl wipe (§6.4's
  shade, grown to a full turn) sweeps the sheet away;
  arriving, the new cover prints in imposition order.
  It belongs because a spinner would be a machine
  part in a paper world; a blank sheet is the
  brochure in its dormant state — the same object,
  not yet impressed.
- **Structure.** Blank regions are DOM elements with
  `data-blank` styling: `--cream-deep` sheet, an
  inset plate void (2px deeper), three ruled lines
  at text measure — shaped like the content they
  precede (a blank plate is wide, a blank coupon is
  coupon-shaped). Inking is a class swap (`.is-inked`)
  that fades the blank's void out as the real
  content, already in the DOM or injected complete,
  prints beneath with the §6.4 ink step. The
  transition reuses §6.4's shade layer at page
  scale: a fixed overlay whose gradient sweeps
  100% → 0 across navigation.
- **Motion spec.** Blank state: the void's ruled
  lines hold a barely-alive ink breath (opacity
  0.85 ± 0.05, 2.6s sine — dormant paper, not a
  pulse). Ink-in on data: 400ms `--ease-press`,
  void fading as print rises. Hard ceiling: any
  region still blank at 1500ms prints its content
  anyway, inked or not — the press does not hold a
  reader hostage to a slow plate. Transition: curl
  sweep 600ms total (300 out, navigation, 300 in),
  watchdogged at 2000ms end to end.
- **States.** Blank (breathing) → inking → printed.
  Error (a region's data fails): the blank prints
  its notice in Caslon — "This plate did not reach
  the brochure — [print it again]" with a real retry
  control; a blank never breathes forever.
  Scrolled-past: below-fold regions ink on arrival
  regardless of visibility. Disabled: JS off → no
  blanks exist; content is server-printed complete.
- **Content merge.** The blank is shaped like its
  content and ruled at its measure; the transition's
  curl is the section turn (§6.4) at cover scale —
  one paper physics for arriving, turning and
  leaving, because it is one brochure.
- **Failure fallback.** Watchdogs: per region
  1500ms (print regardless); on the transition
  2000ms (the destination forces its printed state —
  a reader may never be stranded between pages on a
  blank sheet). No JS: plain navigation, complete
  pages.
- **Reduced-motion variant.** Blanks are static
  sheets that swap to print instantly on data;
  transitions are plain navigations, destination
  printed.
- **Performance budget & mobile variant.** Blanks
  are CSS gradients — zero raster, zero per-frame
  JS. Mobile: the curl sweep shortens to 400ms and
  the blank breath is cut (static sheets) to save
  battery.
- **Choreography timeline (v2).** Region requested
  → blank prints with layout → data lands → ink-in
  400ms → region at rest. Ceiling 1500ms forces
  print. Transition: click → curl out 300ms →
  navigate → cover prints in (imposition order) →
  curl clears 300ms. Watchdog 2000ms.
- **State matrix (v2).** *Rest:* printed content.
  *Hover:* n/a. *Focus:* blanks are unfocusable and
  `aria-hidden` until printed. *Active:* a
  submitting coupon shows the writing line (§6.14),
  not a blank — a form mid-act is never blanked.
  *Scrolled-past:* pre-inked print. *Disabled /
  no-JS:* server print, no blanks. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full treatment.
  768–1199px: full, breath period 3s. <768px:
  static blanks, 400ms transition.
- **Edge cases & failure modes (v2).** *Data faster
  than the blank's first paint:* the region prints
  directly — a blank that never appears is the best
  kind. *Partial failure (2 of 5 cards land):*
  landed cards print; the rest hold blank to their
  own ceiling, then print their notices
  individually — the brochure opens with gaps
  admitted, not with the cover held shut.
  *Double navigation mid-transition:* the watchdog
  belongs to the destination page; the reader still
  lands printed.
- **Accessibility spec (v2).** Blank containers
  carry `aria-busy="true"` and leave the
  accessibility tree until printed; one polite
  announcement ("The brochure is printed") fires
  when the last above-fold region inks — not one
  per region. The transition is never announced.
  Notice contrast: navy on cream 11.32:1.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--navy`, `--ease-press`, `--ease-settle`,
  `--dur-blank-ceiling` (1500ms), `--dur-curl-page`
  (600ms), `--dur-watchdog-transition` (2000ms).

### 6.16 The colophon footer — the printer's mark

- **What & why.** A brochure ends with its colophon,
  and so does the page: a navy plate across the foot
  carrying the printer's statement — form number,
  the Schedule's totals printed for the third and
  final time (300 miles, 2 h 05 min, fares from
  $2,950), the carrier's mark, and the line every
  1962 brochure carried: "PRINTED IN U.S.A." It
  belongs because the colophon is where print
  culture signs its work; the footer's totals are
  the law's closing audit — the same figures, at the
  back of the book, agreeing with the front.
- **Structure.** A `<footer>` on `--navy`: cream
  type (11.32:1), the colophon set in three columns
  (the mark & form № 62-OR-114; the Schedule summary
  in mono; the port index repeated as real links),
  a gold hairline above (the one place gold rules on
  navy), and the clipper docked at the foot of the
  orbit line (§6.2) overlapping the plate's top edge
  — the ship has arrived at the back cover. "PRINTED
  IN U.S.A." sets in tracked Archivo caps; gold
  lettering (`--gold-ink`, 5.87:1 on navy) is
  licensed here for the form number only.
- **Motion spec.** The footer does not animate on
  entry beyond its section curl (§6.4). Its one
  motion is the arrival it hosts: the margin
  clipper docking (§6.2) and the miles readout
  landing on 300 (§6.3) happen at its top edge —
  the footer's stillness is the dock. The gold rule
  draws itself (600ms line-draw) as the footer first
  enters — the printer ruling the colophon's line,
  once.
- **States.** Rest: printed colophon. Hover: links
  re-ink toward cream-full (§6.8's treatment on the
  navy plate: ink = light here, the one inversion,
  specified rather than improvised). Scrolled-past:
  n/a — it is the past. The reservations count in
  the summary column is live: after a booking
  (§6.14) it reads 1,209 on file — the colophon
  reprints itself honestly.
- **Content merge.** Every figure is the Schedule's
  third printing (§6.17): terminal 300 miles, PA-101
  2 h 05 min, fares from the lowest one-way
  ($2,950). The form number ties the page to the
  physical brochure it performs. Nothing appears in
  the colophon that the brochure has not already
  claimed — a colophon introduces nothing.
- **Failure fallback.** Static HTML; the gold rule
  ships drawn, its draw-in armed over it. No JS:
  identical colophon, count at the printed 1,208.
- **Reduced-motion variant.** Rule pre-drawn; no
  other motion exists to remove.
- **Performance budget & mobile variant.** Zero
  per-frame cost. Mobile: columns stack (mark,
  summary, index), the docked clipper sits at the
  plate's top-left, form number stays gold — small
  screens do not demote the printer's mark.
- **Choreography timeline (v2).** Footer enters →
  curl settles (§6.4) → gold rule draws 600ms →
  clipper docks at the top edge (concurrent, §6.2)
  → miles land on 300 (§6.3) → the brochure is
  finished, in every sense.
- **State matrix (v2).** *Rest:* printed. *Hover:*
  links lighten-ink. *Focus:* outline in cream.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three columns.
  768–1199px: two columns (index wraps under).
  <768px: stacked, centred mark.
- **Edge cases & failure modes (v2).** *A build
  with no reservation system:* the count line is
  cut from the summary — the colophon never prints
  a number the site cannot honour (§1). *Print:*
  the colophon prints navy-on-cream inverted back
  to ink economy: the print stylesheet sets it in
  navy type on cream with the gold rule in teal —
  paper brochures did not flood a page with ink for
  the back cover either.
- **Accessibility spec (v2).** Footer landmark;
  cream on navy 11.32:1 body, gold-ink form number
  5.87:1 at 13px mono (large-print class); index
  links carry the ports' full names.
- **Tokens consumed (v2).** `--navy`, `--cream`,
  `--gold`, `--gold-ink`, `--teal`, `--ease-glide`.

### 6.17 The 1962 Schedule — the one source of every figure

- **What & why.** The declared data record from
  which every number, time, fare and behaviour on
  the page is printed: Pan American's Clipper
  Service schedule as the brochure states it —
  flights, the ascent profile, fares, the deposit,
  the reservations ledger. It is an element because
  the theme's law (§1) needs an object: *the
  brochure prints nothing it cannot stand behind*
  is enforceable only if exactly one place holds
  the truth, and every printing — hero readout,
  table, card, form, colophon — is a rendering of
  it, never a re-typing.
- **Structure.** A build-time record, validated
  before render: `form: "62-OR-114"`, `effective:
  "1 October 1962"`, `aircraft: { name: "Clipper
  Morning Star", seats: 24 (8 First, 16 Tourist),
  crew: 5, portholes: 12 }`, `flights: […]`,
  `ascent: […]`, `fares: […]`, `depositPerSeat:
  250`, `baggageLb: 44`, `reservationsOnFile:
  1208`, and derived totals computed by the build,
  never authored (`flightMinutes`, `returnFare`,
  `childFare`). The canonical Schedule:
  **PA-101** New York (Idlewild) → Orbit: depart
  09:30 EST, arrive 11:35 EST, 2 h 05 min.
  **PA-102** Orbit → New York: depart 14:00, arrive
  16:05, 2 h 05 min. **PA-201** San Francisco →
  Orbit: depart 08:15 PST, arrive 10:50 PST,
  2 h 35 min. **Ascent (PA-101):** 0–10 mi in
  4 min · 10–40 mi in 6 min · 40–62 mi in 5 min ·
  coast & rendezvous 1 h 50 min — 4 + 6 + 5 + 110
  = 125 min = 2 h 05 min; 09:30 + 2:05 = 11:35 ✓.
  **Terminal:** 300 miles altitude; orbital speed
  17,500 mph; one circuit 92 minutes (17,500 ×
  92/60 ≈ 26,833 miles of circuit — the geometry
  agrees with itself). **Fares, one-way:** NY First
  $4,800 · NY Tourist $2,950 · SF First $5,150 ·
  SF Tourist $3,200. **Returns** (the printed rule:
  10% saving on the round trip) = 2 × one-way ×
  0.9: $8,640 · $5,310 · $9,270 · $5,760 ✓.
  **Child under 12:** half fare (NY First one-way
  $2,400, return $4,320). **Deposit:** $250 per
  seat, applied to the fare. **The footnote**,
  verbatim, part of the record itself so no
  template can drop it: *"Fares subject to CAB
  approval and the invention of the spacecraft."*
- **Motion spec.** None — the Schedule does not
  move; it is what motion answers to. Its one
  dynamic relation: session state (punched fare,
  issued reservation №) lives in a separate object
  that may *reference* the Schedule but never
  mutate it — except the ledger count, whose single
  licensed mutation is +1 on a confirmed booking,
  reprinted everywhere the count appears (§6.14,
  §6.16). The timetable that happened is not
  editable by the visit being made.
- **States.** The record has no states; its
  printings do (§6.1–§6.16). Its build states are
  pass/fail: schema-valid and arithmetic-verified,
  or the build does not ship (§10).
- **Content merge.** This element IS the content;
  every other element's merge note points here.
- **Failure fallback.** If the record fails
  validation, the build fails — there is no
  fallback brochure with invented fares. At
  runtime the record is static JSON inlined with
  the page; it cannot 404 separately from the page
  it schedules.
- **Reduced-motion variant.** n/a — the record is
  print.
- **Performance budget & mobile variant.** ≤2KB
  JSON, inlined; derived totals computed once at
  build. Identical at every breakpoint — the
  Schedule does not abridge itself for small
  screens; presentation layers (§6.5, §6.13)
  decide what a phone shows first, never what is
  true.
- **Choreography timeline (v2).** n/a — the
  record's only timeline is the flight's own:
  09:30 → 11:35, which §13 maps onto the page.
- **State matrix (v2).** *Canonical:* as printed
  above. *Session:* ledger 1,208 → 1,209 on one
  confirmed booking, then the count is the new
  canonical for that session. *All other fields:*
  immutable in session, full stop.
- **Breakpoints (v2).** Identical at all sizes.
- **Edge cases & failure modes (v2).** *An editor
  changes a fare in one template:* impossible by
  construction — templates render the record; a
  hard-coded fare anywhere is a §10 gate failure
  found by grep. *A route is withdrawn:* the
  record gains a `status: "wait-list"` and §6.5
  prints WAIT LIST from the record — the brochure
  admits it in the table, not in a banner.
- **Accessibility spec (v2).** The record itself is
  data; its accessible printings are §6.5's and
  §6.13's tables, audited there.
- **Tokens consumed (v2).** None — the Schedule is
  upstream of tokens; it consumes nothing and
  authorises everything.

### 6.18 The unprinted page — empty state & 404

- **What & why.** Where the brochure has nothing —
  a search with no ports, a filter with no fares, a
  URL that is not a page — the answer is an
  unprinted page: a cream sheet carrying the
  printer's plain admission, "THIS PAGE WAS NOT
  INCLUDED IN THE BROCHURE", the route home drawn
  as a dotted line back to the cover, and the offer
  of the reservation coupon (a reader lost in a
  brochure is a reader mid-journey). It belongs
  because absence in a print shop is a missing
  leaf, not an error screen — and the 404 is the
  full-page form of the same sheet.
- **Structure.** A region (inline empty state) or
  full page (404) on cream: a deckle-edged sheet
  outline, the admission set in Archivo Black at
  28px, two lines of Caslon in the counter's voice
  ("The brochure you are reading has sixteen
  pages. This is not one of them."), a dotted SVG
  line with the clipper parked at its start,
  pointing home, and real links: the cover, the
  port index, the coupon (§6.14). The orbit line
  (§6.2) does not enter this page — there is no
  port here, and the margin is honestly empty.
- **Motion spec.** Nearly none, by design: the
  dotted line draws itself once (700ms) toward
  the cover link — the way back, ruled in. The
  parked clipper does not fly (it is waiting, not
  travelling). That restraint is the spec: an
  unprinted page has no performance in it.
- **States.** Rest: the admission, printed.
  Hover/focus on the exits: re-ink (§6.8) as
  everywhere. The empty-search variant keeps the
  visitor's query printed in mono at the sheet's
  head ("NO PORTS MATCH 'MOON'") with the nearest
  ports listed as cards (§6.12) below — the
  counter suggesting, not apologising.
- **Content merge.** The admission's page count is
  the brochure's real page/section count from the
  build; the exits are the real index; the 404's
  sheet uses the same deckle and stock as every
  plate. Nothing about being lost exempts the page
  from being the brochure.
- **Failure fallback.** This element IS a fallback;
  it is static HTML that cannot fail into anything
  emptier. No JS required for any part of it.
- **Reduced-motion variant.** The line ships drawn.
- **Performance budget & mobile variant.** One SVG
  line, no loop subscriptions (the shared loop
  idles on this page — the only page where it may).
  Mobile: the sheet narrows, the admission wraps to
  three lines at 24px, exits stack at ≥48px.
- **Choreography timeline (v2).** Page prints →
  line draws 700ms toward the cover link → rest.
  Nothing else, ever.
- **State matrix (v2).** *Rest:* admission printed.
  *Hover:* exits re-ink. *Focus:* exits outline.
  *Active:* exits navigate. *Scrolled-past:* n/a.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: sheet 720px wide,
  admission 28px. 768–1199px: 600px. <768px:
  full-measure sheet, 24px admission, stacked exits.
- **Edge cases & failure modes (v2).** *A search
  with results only in an unpublished port:* the
  sheet says so ("One port matches, and it is not
  yet printed") and offers the index — the
  brochure does not pretend the plate exists.
  *404 for an asset (image) URL:* the server
  returns the plain 404 sheet without the drawn
  line (an asset has no reader to guide).
- **Accessibility spec (v2).** The admission is the
  page's `<h1>`; the 404 returns a real 404 status;
  exits are real links with full names; contrast
  navy on cream 11.32:1 throughout.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--navy`, `--teal`, `--red`, `--ease-glide`.

## 7. Page application map

- **Home (the brochure itself).** The canonical
  sequence: cover (§6.1) → The Clipper (plates,
  §6.6) → The Voyage (ascent table, §6.13) → Life
  Aboard (port cards, §6.12) → Fares (pinned
  spread, §6.5) → Reservations (coupon, §6.14) →
  colophon (§6.16), threaded by the orbit line
  (§6.2) throughout. This is the page every other
  page is an extract of.
- **Listing (all ports / all routes).** The port
  index as a full page: cards (§6.12) in timetable
  order with the ascent table (§6.13) as the
  summary plate at the foot; filters print as
  index tabs in the masthead's language (§6.11) —
  a contents page with better manners.
- **Detail (one port / one route).** A single
  plate chapter: big misregistered plate (§6.6),
  Caslon columns, its Schedule lines as a ruled
  mono strip, and the fare for its route quoted
  from §6.17 with its own punch target (§6.9)
  leading to the coupon. Detail pages never invent
  a local price.
- **About (the carrier).** The brochure's voice at
  its most confident: cover-style headline, the
  colophon's form number promoted to a masthead,
  history set as back-numbers of the brochure —
  each era a plate. The footnote's honesty applies
  to history too: dates are dates.
- **Timetable page.** §6.13 and §6.5 side by side,
  unpinned, at full measure — the page for the
  reader who came for numbers; the brochure does
  not make them wade through plates to reach it.
- **Contact / reservations.** §6.14 full-page: the
  coupon large, the ledger preamble above it, the
  baggage and child rules printed at its foot
  (fine print at home, §4).
- **Checkout equivalent.** There is no cart in
  1962. The coupon IS the checkout: deposit
  acknowledged, stub issued. A build that bolts a
  modern cart onto this theme has left the theme.
- **404 / empty.** §6.18, the unprinted page.

## 8. Worked examples

**Example 1 — the cover, end to end (hero).** The
reader arrives. The sheet is already printed: cream,
the clipper lithograph mid-plume, the headline set —
"ORBIT IS 300 MILES AWAY. WE LEAVE AT 9:30." — the
readout showing 62. At t=600 the JS-armed performance
begins over the finished print: the headline squashes
word by word (550ms, `--ease-press`), the first
halftone puff blooms from the tail (1.8s cycle
established by t=2500), and at t=900 the altitude
readout starts its 2400ms climb from 0 — passing 10,
40, damping into 62 as the tick "EDGE OF SPACE"
prints beneath it. The seal does nothing. The stars
breathe. If any part of the machinery has failed,
the watchdogs (2400ms cover, 3000ms readout) have
already returned the cover to exactly what the
reader saw at t=0: a printed brochure cover, complete.
Scroll timeline: the cover's own parallax separates
its three print depths by ≤4% as it leaves; the
clipper in the margin (§6.2) lifts off its port as
the cover's ship stays home — two ships, one at the
gate, one flying the route, and the brochure never
confuses them because the margin ship is 22px and
red and the cover ship is a lithograph.

**Example 2 — the fare spread, mid-page.** The
reader has flown past The Voyage (margin altimeter
at 62 as the section docks). The fare section
arrives; its curl turns (§6.4). The spread pins.
Across the first 40% of the pin's travel the eight
fares count from 60% and land — $4,800 … $2,950 …
$5,150 … $3,200, then the returns beneath them,
$8,640 first — each landing dead, each exactly
2 × one-way × 0.9 where a return is concerned, the
printed rule "10% SAVING ON THE RETURN CLIPPER"
sitting above the column it describes. In the rail,
departures and the 44 lb baggage rule scroll past.
Across the last 30%, the footnote types itself:
*"Fares subject to CAB approval and the invention
of the spacecraft."* The reader hovers the New York
First row: it re-inks; a dotted punch-guide shows at
its edge. They click: dip, notch, "PUNCHED" — and
the coupon, a page below, now holds New York –
Orbit, First Class, $4,800, deposit $250, waiting
for a name. The pin releases. Nothing on the spread
ever hid; a reader who jumped here by anchor found
it printed, and the count was a courtesy, not a
gate.

**Example 3 — the coupon, conversion.** The reader
reaches Reservations with a punched fare in hand.
The coupon's preamble has kept its promise in
print the whole visit: "Reservations on file:
1,208. Yours will be № 1,209." Route and class are
already selected from the punch; the deposit line
reads $250. The reader adds a second seat — a
child, they note in the party field — and the
deposit counts to $500 (2 × $250) while the fare
summary, computed from the Schedule, prints the
child at half fare: $2,400 beside the adult's
$4,800, subtotal $7,200 one-way, deposit applied.
They submit. The button punches; the counter
writes; within the watchdog the stub rises:
"RESERVATION № 1,209 — CLIPPER MORNING STAR ·
PA-101 · NEW YORK – ORBIT · FIRST CLASS · PARTY
OF 2 · DEPOSIT $500 APPLIED." Behind it, quietly,
the colophon's count and the coupon's own preamble
now read 1,209 on file — the brochure has absorbed
the booking into its record, and the next visitor's
coupon will promise № 1,210. Had the endpoint
failed, the coupon would have kept every word the
visitor wrote and said so, in the counter's voice,
by name.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The wink.** Copy that mocks its own fiction
   ("lol, they really believed this") — the theme
   dies of it instantly. *Cure:* the brochure never
   breaks character; its only irony is the footnote,
   and the footnote is sincere.
2. **Photographs.** A stock photo of a rocket or a
   smiling model in a headset. *Cure:* drawn plates
   only, three passes, misregistered (§6.6); no
   plate art, no plate — a numbered blank (§6.12).
3. **Perfect registration.** Clean, aligned,
   full-colour illustration. *Cure:* the 2px truth
   (§6.6); if it looks rendered, it is wrong.
4. **Sepia-and-scratch "old" filters.** Artificial
   aging — coffee stains, torn corners everywhere,
   distressed type. 1962's brochure was *new*; its
   optimism is mint-condition. *Cure:* cream stock,
   crisp type, one deckle edge. Age is in the voice,
   not in fake damage.
5. **Invented numbers.** A fare, time or altitude
   typed into a template. *Cure:* the Schedule
   (§6.17) renders everything; §10 greps for
   hard-coded figures.
6. **The missing footnote.** Fares without *"subject
   to CAB approval and the invention of the
   spacecraft."* *Cure:* the footnote lives inside
   the record itself (§6.17); a fare table cannot
   be built without it.
7. **Tiny fine print.** The footnote at 9px in grey
   — the law broken with a straight face. *Cure:*
   11.5px minimum, `--red-deep`, 5.89:1 (§3, §6.5).
8. **A progress bar.** Or a spinner, or a toast.
   Machine parts in a paper world. *Cure:* miles
   (§6.3), the writing counter (§6.14), blanks
   (§6.15) — the theme has its own words for these.
9. **Red everywhere.** Red headlines on every
   section, red buttons, red prices. *Cure:* the
   §2 ration — red is the cover colour, ~3% of any
   viewport; interior emphasis is teal and navy.
10. **The clipper as clip-art.** A generic rocket
    emoji-shape pasted into corners. *Cure:* one
    drawn ship, one livery, at every size from the
    22px margin traveller to the cover lithograph —
    the same *Morning Star*, recognisably.
11. **Motion that hides.** Reveals that start from
    invisible, curls that cover text, a pin that
    traps. *Cure:* print-first DOM, the 12% shade
    cap (§6.4), the mobile pin cut (§6.5).
12. **Modern web copy in period dress.** "Unlock
    your journey today!" in Archivo Black is a
    2026 landing page in a costume. *Cure:* §12's
    voice — the counter's courtesy, complete
    sentences, one exclamation per page.
13. **Gold text on cream.** Pretty in a mockup,
    illegible in the world (1.93:1). *Cure:* gold
    is ornament on cream, lettering only on navy
    (§2).
14. **A dark mode.** The brochure inverted by a
    toggle. *Cure:* §2's ruling — navy exists as
    plates inside the brochure, never as a mode.

## 10. Quality gate

Blocking checks — all must pass before this theme
ships in a build:

1. **Figure audit.** Every fare, time, altitude and
   count on the page re-derived from §6.17 by a
   non-builder: ascent sums to 125 min; returns =
   2 × one-way × 0.9; child = half; deposit = n ×
   $250; arrival = departure + duration.
2. **Footnote audit.** The verbatim footnote appears
   with every printing of the fare table, at ≥11.5px,
   in `--red-deep`, and is present in the raw DOM
   (not injected by JS).
3. **Red census.** Red's share sampled on three
   viewports: ≤5% of pixels in interior sections;
   red-on-navy pairings: zero.
4. **Gold census.** Gold text on cream: zero
   instances. Gold lettering only on navy, only the
   licensed spots (§6.16, seals).
5. **Watchdog drill.** Loop killed, fonts blocked,
   JS disabled — three separate passes; in each, the
   full brochure (fares, footnote, tables, coupon)
   is readable within the watchdogs' deadlines.
6. **Reduced-motion pass.** With the preference on:
   no curls, no puffs, no counts, no pin — and every
   figure at its final Schedule value.
7. **Print-first check.** DOM order and content
   complete with scripts stripped: cover headline,
   all fares, ascent table totals, coupon fields,
   colophon totals.
8. **Misregistration check.** Plates measure 2px
   (±0.5) settled offset at desktop, red/teal passes
   present, no four-colour art in any plate.
9. **Pin check.** Exactly one pinned element (the
   fare spread); on <768px, zero pins and the
   footnote still prints whole.
10. **Cursor & cover check.** System cursor only;
    no animated element overlaps body text at any
    frame (shade ≤12% over type, punch notch clear
    of fare figures).
11. **Contrast audit.** All text pairings at §2's
    computed ratios; footnote and fine print
    included by name.
12. **Star-field check.** No star dots inside the
    headline's bounding plate; breathing rates
    ≤0.3Hz.
13. **Ship consistency.** The clipper is one drawing
    at every size — margin traveller, cover
    lithograph, masthead glyph, 404's parked ship —
    traced to the same master art; livery colours
    match §2 exactly; the name *Morning Star* is
    lettered identically (cream on red) wherever it
    appears.
14. **Imposition check.** Panel staggers follow
    printer's imposition order (1, 4, 2, 3 across a
    spread), not DOM order, on the home page's two
    card grids; DOM order itself remains reading
    order for assistive tech — the stagger is a
    visual rhythm laid over a correct document.

Minimum bar: 14/14. A build that fails the footnote
audit fails outright regardless of the rest — it is
the law (§1) with a checkbox.

## 11. Component inventory

Every component a real site in this theme needs,
with its treatment. Components the theme refuses
are named with their in-world replacement.

- **Buttons.** Printed labels in Archivo caps on a
  ruled outline; primary = navy fill, cream type;
  the punch (§6.9) is their click state. No rounded
  pills — a brochure's buttons are rules and type.
- **Links.** Teal-deep, underlined with the rule
  that thickens on hover (re-ink, §6.8).
- **Inputs.** Coupon fields (§6.14): cream ground,
  navy bottom rule that inks teal-deep on focus,
  Caslon entries — the visitor writes in the
  brochure's serif, as with a pen.
- **Selects.** Native selects styled as coupon
  lines; options carry mono fares.
- **Tables.** §6.5 and §6.13 are the pattern: teal
  rules, mono figures, hung dollar signs, totals
  in `<tfoot>`.
- **Cards.** Port-of-call cards (§6.12).
- **Badges / seals.** The gold starburst seal —
  used for exactly three things: the service year
  (cover), the CAB approval mark (fare spread),
  "PRINTED IN U.S.A." companion (colophon). A
  fourth use is a §9 violation in waiting.
- **Alerts.** The ledger note: a ruled mono block
  in the counter's voice (§6.14's counter-closed
  note is the pattern). Never a coloured banner.
- **Modal.** Refused. A brochure has no overlays;
  what a modal would say becomes a plate section
  or the unprinted page (§6.18).
- **Toast.** Refused. Confirmations are documents
  (the stub, §6.14), not weather.
- **Tabs.** Refused as chrome; the port index
  (§6.11) and imposition-order sections do the
  work. Where a build truly needs tabbed data,
  it is set as a timetable with column heads —
  and reviewed against §9.
- **Accordion.** The back-numbers index (about
  page): era plates that unfold like brochure
  pages, §6.4's curl at small scale.
- **Pagination.** "NEXT PORT →" as a printed
  direction at the foot, with the port's name and
  altitude — the reader is travelling, not paging.
- **Breadcrumbs.** The route so far, in the margin
  line's language: ports passed, printed full-ink
  (§6.2). On detail pages, a mono line: COVER /
  THE VOYAGE / 62 MILES.
- **Progress.** Miles-to-orbit (§6.3). Nothing else.
- **Loader.** Unprinted blanks (§6.15).
- **Form errors.** The red-deep asterisk + Caslon
  sentence (§6.14). No red fields, no shake.
- **Empty state.** The unprinted page (§6.18).
- **Footer.** The colophon (§6.16).

## 12. Content & copywriting voice

Two registers, one brochure:

- **The Cover** (display voice): Archivo Black,
  declarative, present tense, the future stated as
  fact. *"ORBIT IS 300 MILES AWAY. WE LEAVE AT
  9:30."* Short lines. One exclamation per page,
  cover only.
- **The Counter** (service voice): Caslon prose and
  mono figures; courteous, complete sentences,
  second person, no contractions in formal lines
  (the counter writes "You will be met at the
  terminal", not "You'll be met"). This is the
  voice of errors, empties and confirmations —
  politeness under all conditions.

**Headline style.** A claim the Schedule can back,
set as a timetable fact: a number, a time, a place.
✓ "LUNCHEON IS SERVED AT 62 MILES." ✗ "Your journey
to the stars begins!!" (two exclamations, no fact,
one cliché — three violations in nine words).

**Label style.** Archivo caps, tracked, nouns of
the trade: PORTS OF CALL, FARES, RESERVATIONS,
BAGGAGE. ✗ "Menu", "Pricing", "Book now".

**Error voice.** The counter, by name and without
blame: ✓ "The counter needs your name to hold the
seat." ✗ "Invalid input." ✓ (ledger closed) "The
counter is closed for the evening; your coupon is
kept, unmailed, exactly as you wrote it."

**Empty-state voice.** The printer's admission
(§6.18): ✓ "This page was not included in the
brochure." ✗ "Oops! Nothing here."

**Fixed strings (verbatim, never paraphrased):**
the footnote (*"Fares subject to CAB approval and
the invention of the spacecraft."*); "MILES TO
ORBIT"; "PRINTED IN U.S.A."; the form promise
("Reservations on file: 1,208. Yours will be №
1,209." — the numbers move with the ledger, the
sentence does not); "EDGE OF SPACE" for the 62-mile
tick; "WAIT LIST" for a withdrawn class.

**Numbers in copy** always come from the Schedule
and always set in mono when they are data; prose
may spell out small numbers in Caslon ("sixteen
pages") — the brochure's own distinction between
reading and reckoning.

## 13. Full-page scroll choreography map

The home page, top to foot — every beat in order:

1. **Cover printed** (t=0): headline set, plume at
   mid-bloom, readout at 62 — the brochure whole.
2. **The launch performance** (t=600–3300): squash,
   puffs, the climb (§6.1, §6.7); stars breathing.
3. **First scroll:** cover depths separate ≤4%;
   the margin clipper leaves the cover port (§6.2);
   miles begin to count (§6.3).
4. **The Clipper section:** curl turns (§6.4); the
   livery plate settles from 3px to 2px
   misregistration (§6.6); altimeter passes 10.
5. **The Voyage:** the ascent table's arc draws
   with the reading (§6.13); the 62-mile row's red
   rule is the page's second red moment; altimeter
   docks at 62 with the port tick.
6. **Life Aboard:** port cards print in imposition
   order, 90ms apart (§6.12); a plate tilts under
   the reader's hand.
7. **Fares:** the spread pins (§6.5) — fares count
   and land, rail passes, footnote types itself;
   perhaps a punch lands (§6.9).
8. **Reservations:** the coupon (§6.14), its
   preamble's promise in print; the deposit counts
   as the party grows; on success, the stub.
9. **Colophon:** the gold rule draws (§6.16); the
   margin ship docks at the plate's edge; miles
   land on **300 · ORBIT**.
10. **Reverse pass:** scrolling up, curls reverse
    in their bands, the ship flies its sags
    backward without stretch, the altimeter counts
    down honestly; landed fares and the printed
    footnote do NOT un-print — ink, once dried,
    stays (§6.5). Jump-scroll to anywhere: every
    element computes its state from position, so
    the brochure is correct at the landing point,
    not after a catch-up.

## 14. Whole-page performance budget

- **Page weight:** ≤900KB total first load; plates
  are inline SVG (≤120KB for the cover, ≤60KB per
  interior plate); fonts: Archivo Black + Archivo
  (2 weights) + Libre Caslon (2) + IBM Plex Mono
  (1), subset, ≤180KB combined. No JavaScript
  framework; the loop and behaviours ≤14KB gz.
- **Frame budget:** ≤1.2ms/frame of JS on a
  mid-range phone CPU — the shared loop touches
  only in-viewport elements; per-element costs are
  stated in §6 and sum under the cap with the hero
  at full performance.
- **Long tasks:** none >50ms; the Schedule's
  derived totals are build-time, never runtime
  arithmetic over the page.
- **Cut order when the budget is exceeded:** (1)
  the margin clipper below 360px (§6.2); (2) the
  mobile fare pin — already cut (§6.5); (3) star
  breathing count; (4) plate breathing (§6.6's
  ±0.5px); (5) parallax depths collapse to one.
  **Never cut:** the footnote, the watchdogs, the
  print-first DOM, the reduced-motion variants —
  the law is not a performance feature.
- **Print stylesheet:** the brochure prints as a
  brochure — cream dropped to white for ink
  economy, plates at settled registration, tables
  complete with the footnote, colophon in navy on
  white (§6.16). A theme about print that cannot
  print is a failed theme; the print pass is in
  §10's drill family.

## 15. Build-order checklist

1. **The Schedule first** (§6.17): record authored,
   arithmetic verified (ascent 125 min, returns
   ×0.9, child halves, arrivals) before any
   template exists.
2. **Tokens & type**: palette (§2) with its pairing
   laws as lint rules; the four voices (§3) with
   the 11.5px floor.
3. **Static brochure**: the complete page, printed,
   JS-free — cover, tables, coupon, colophon —
   passing §10 checks 2 and 7 in this state.
4. **The margin apparatus**: orbit line + miles
   (§6.2, §6.3) reading one boundary table.
5. **Section turns & plates**: curl (§6.4),
   misregistration settle (§6.6), dot-star sky
   (§6.10).
6. **The cover performance**: hero + climb (§6.1,
   §6.7) with watchdogs armed and drilled.
7. **The fare spread**: pin, counts, footnote
   print (§6.5); mobile flow variant.
8. **Interaction layer**: re-ink (§6.8), punch
   (§6.9), cards (§6.12), ascent arc (§6.13).
9. **The coupon**: form, deposit, stub, ledger
   mutation (§6.14); counter-closed path tested
   by killing the endpoint.
10. **Blanks & transitions** (§6.15); **colophon**
    (§6.16); **unprinted page** (§6.18).
11. **Navigation**: masthead + scrollspy (§6.11)
    sharing §6.2's boundary table.
12. **Reduced-motion pass**: every element's
    variant verified against §6, one by one.
13. **The drills**: §10's watchdog, print-first
    and print-stylesheet passes.
14. **Voice pass**: all copy read aloud against
    §12 — one exclamation counted, fixed strings
    checked verbatim.
15. **Gate**: §10 signed by a non-builder; the
    figure audit re-done from the record, not
    from the page.
