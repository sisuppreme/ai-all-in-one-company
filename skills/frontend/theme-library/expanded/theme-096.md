# 96. From the Wings — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A theatre site experienced from backstage: ropes,
sandbags, spike tape and a stage manager's cue sheet. The audience
never sees this side of the building; members do, and this site is
written for members. Palette anchors: wing-space black `#14100D` ·
canvas & rope hemp `#D9C7A7` · cue-light red `#A62B25` ·
stage-manager green `#2F5D50` · worn gilt `#8A6D3B`. Type: Playfair
Display (show titles — front-of-house glamour) + Space Mono (cue
sheets, calls, and all working text). The page opens behind a closed
curtain, runs in numbered cues called from a pinned prompt corner,
changes its scenes in honest 200ms blackouts, and ends — as every
working night ends — at the stage door.

## 1. Concept & world

From the Wings is the website of a theatre turned inside out. Every
theatre has two buildings sharing one address: the one the audience
sees — gilt, velvet, the Playfair title glowing over the door — and
the one behind the curtain, which is black-painted brick, hemp rope,
sandbags, glow tape on a boards floor, and a stage manager in the
prompt corner calling the show off a marked-up book. The front of
house sells the illusion. The wings are where the illusion is
*worked*: hauled, spiked, cued and caught, night after night, by
people whose names are in the programme in 8pt and whose mistakes
would be visible from the stalls. This theme builds the site out of
the second building. The visitor is not seated in the auditorium;
they are standing in the wings with a headset on, close enough to
the tabs to smell the dust, watching the show get *made* — and the
page's argument is that this side is the more honest glamour, the
one members, students, backstage crews and theatre obsessives
actually want to live in.

The page therefore runs the way a show runs. It opens behind a
closed curtain that parts sideways on ropes (§6.1) — theatres'
tabs do not rise like a lift door, they travel, and so does this
page. Nothing on the page "reveals": each section is *called*,
by number, from the prompt corner (§6.2), the way a stage manager
calls "Standby Q13… Q13, GO" into the cans. Between major scenes
the light honestly goes out for 200ms (§6.3) and the new set is
standing there when it returns — a blackout is not a loading
spinner wearing a costume, it is the theatre's real machinery for
changing worlds in the dark, and the page uses it at its real
duration. Scenery is flown the way scenery is flown: scroll hauls
the backdrop up its rope marks while the sandbags descend in
counterweight (§6.4). The floor knows where things belong because
the floor is marked — spike tape (§6.5) shows exactly where each
section's key element stands. Progress through the page is not a
scrollbar skin; it is the cue list itself, checked off in green
pencil in the margin (§6.6), with the running time tallying beside
it in mono. And buried in the middle of the working paperwork is
the theme's heart, a cue that changes nothing and means
everything: *Q47 — House lights. Breathe.* (§6.10). When the page
reaches it, the machinery pauses, the light warms a fraction, and
the site remembers the crew it is running for.

**The theme's one law: the page runs on a real prompt book, and
the book does not lie.** Two clauses, both audited by the gate.
(1) *Every cue traces to the book.* There is exactly one declared
cue sheet (§6.17): an ordered record of every Q-number on the
page, what it calls, and its running time. The prompt corner's
list (§6.11), the called cues (§6.2), the green-pencil check-offs
(§6.6) and the running-order table (§6.13) are four printings of
that one record — a cue number that appears in the corner but not
in the book, a check-off for a section that does not exist, a
running time in the table that disagrees with the tally (§6.14):
each is a gate failure. (2) *A blackout always lifts.* The 200ms
blackout (§6.3) and the curtain (§6.1) are overlays on a page that
ships complete and lit underneath; both are dismissed by timers
that do not depend on the animation completing, on scroll
arriving, or on any asset loading. A missed cue in a real theatre
leaves the scene simply there, fully lit, and the show goes on —
a build in which a failed animation can leave a section dark or
hidden has broken the first rule of stage management and fails
the gate outright.

**Best-fit sites and audiences.** Producing theatres and receiving
houses launching a season to members and subscribers; dance
companies, whose backstage culture (rosin, spike marks, quick
changes) is the same world in a different accent; drama schools
and conservatoires recruiting students who want the working life,
not the poster; live venues and fringe spaces whose whole brand
is the unvarnished room; theatre podcasts, stage-management
training programmes, and backstage-tour or open-day campaigns.
The audience it suits is the insider and the aspiring insider:
members who renew because the building feels like theirs,
students reading the cue sheet the way other students read a
syllabus, crew and creatives for whom a correct sandbag is a sign
of respect. Conversion in this world is membership, season
tickets, enrolment and backstage-tour bookings — commitments made
by people who intend to come back to the building, and the page
is built to feel like being let into it.

**When NOT to use it.** Not for a venue whose brand is pure
front-of-house luxury with no interest in the working building —
the theme will keep dragging the visitor into the wings, and if
the client finds rope and glow tape embarrassing, they want the
gilt theme, not this one. Not for ticketing *checkout* itself:
the stage-door form (§6.15) takes memberships, enrolments and
enquiries, but a high-pressure seat-map purchase flow needs
auditorium clarity, not blackout scene changes, and §7 routes
payment to a plainer surface. Not for content with no show in it
— a static brochure of hire rates and room dimensions has no cues
to call, and forcing Q-numbers onto a price list is exactly the
slop §9 refuses. Not for children's theatre aimed at under-tens:
the register is the working night — black paint, standby calls,
adult patience — and it will read as gloom to a seven-year-old.
And not for any build that cannot maintain the prompt book: the
law requires one true cue sheet, kept in step with the page, and
a team that will let the numbers drift should not wear a theme
whose entire credibility is that its paperwork is right.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme, and
the gate greps built CSS for undeclared hex values. The world is
a black-painted wing lit by working light: hemp and paper tones
carry the reading, the two cue colours are *signals* — they mean
standby and go — and are rationed accordingly, and gilt is the
one front-of-house material allowed backstage, always worn,
never polished.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--wing` | `#14100D` | Wing-space black — the page ground; black-painted brick and boards | ~58% of viewport area | Carries `--hemp` text at **11.42:1**, `--paper` at **15.25:1**. The default reading ground; every other colour is something standing in its dark. |
| `--hemp` | `#D9C7A7` | Canvas & rope hemp — body text, rope lines, canvas flats, tape-adjacent labels | ~22% | On `--wing` **11.42:1** (body text, all sizes). On `--sm-green` **4.52:1** and on `--cue-red` **4.23:1** — labels on called-cue chips pass at large/mono-bold only; body text never sits on a cue colour. |
| `--paper` | `#EFE6D2` | Prompt-book paper — the cue sheet's page, form fields, the running-order table's ground | ~8% | On `--wing` **15.25:1**; on `--sm-green` **6.04:1**, on `--cue-red` **5.65:1** — the only tone allowed as text on a cue-colour ground. |
| `--cue-red` | `#A62B25` | Cue-light red — STANDBY only: the armed cue light, standby states, error ink | ~3% | On `--wing` **2.70:1** — a signal glow, never text. Its one job is to be *seen*, at lamp size, from across the stage. Any red used decoratively is a gate failure: red means a cue is armed. |
| `--cue-red-lit` | `#D96A5F` | The red lamp lit — standby hover/focus text on black, the blinking lamp's bright phase | <1% | On `--wing` **5.57:1** — the only red permitted as text, and only for the standby word itself. |
| `--sm-green` | `#2F5D50` | Stage-manager green — GO states, the pencil of the check-offs, called-cue grounds | ~5% | On `--wing` **2.53:1** — a ground and a pencil, never body text on black. Carries `--paper` at **6.04:1** and `--hemp` at **4.52:1**. |
| `--go-lit` | `#7FB69E` | The green lamp lit / pencil on black — check-off ticks and "GO" set in type on the dark | ~2% | On `--wing` **8.19:1** — the text-weight green; the deep `--sm-green` is for surfaces and strokes. |
| `--gilt` | `#8A6D3B` | Worn gilt — front-of-house traces backstage: title rules, the proscenium edge, prices | ~2% | On `--wing` **3.90:1** — large display and rules only, never body text; gilt is a material, not an ink. Brightens under the followspot (§5) but never past this hex at rest. |
| `--hemp-dim` | `#A8946F` | Hemp in shadow — captions, cue-list entries not yet called, table rules on black | ~2% | On `--wing` **6.43:1** — captions and secondary mono only, minimum 12px. |

**Dark-mode behaviour.** The theme is born dark and does not
invert. A `prefers-color-scheme: light` visitor still gets the
wings — a theatre does not paint its wings white because the
matinee is at two — but the *prompt book* surfaces (`--paper`
fields, the running-order table) are already light, and under
Q47 (§6.10) the whole page warms: `--wing` lifts to `#1B1510`
and `--hemp` gains one step of amber for exactly that section's
length, the house-lights state. Forced-colors mode: cue lamps
become outlined discs with the words STANDBY / GO printed beside
them (colour is never the only signal anywhere in the theme —
every lamp is paired with its word, §6.2), spike tape becomes
`Highlight`, and the curtain is a plain border.


## 3. Typography

Two families, inherited exactly, and the split between them is
the building's split. **Playfair Display** is front of house: it
is allowed backstage only where the show itself is named — show
titles, the season name, the hero headline, prices of honour.
**Space Mono** is the working building: cue sheets, calls, body
text, tables, forms, buttons — everything that is *done* rather
than *admired* is set in the mono, because backstage information
is typed, pencilled and taped, never typeset. A page that sets its
body in Playfair has wandered into the auditorium and lost the
theme.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Show title (hero) | Playfair Display 700 | clamp(44px, 7.2vw, 96px) / 1.02 | −0.01em | Title case as billed; never all-caps (Playfair caps read as a hotel). Called letter by letter on entry (§5). |
| Section title | Playfair Display 600 | clamp(30px, 4vw, 52px) / 1.08 | −0.005em | Always preceded by its cue line in mono — the cue calls, then the title stands in the light. |
| Cue line | Space Mono 700 | 13px / 1.4 | +0.14em, uppercase | Format is law: `Q13 · STANDBY` / `Q13 · GO`. The Q-number is never styled apart from its word. |
| Body | Space Mono 400 | 16.5px / 1.65 | 0 | Max measure 62ch. Mono body is the theme's wager: it reads as typed paperwork, and it must be given generous line-height or it tires. Never below 15px. |
| Caption / call note | Space Mono 400 | 12.5px / 1.5 | +0.04em | `--hemp-dim`; the stage manager's pencil notes, set as asides in brackets in copy (§12). |
| Data / running order | Space Mono 400–700 | 13–15px, tabular | 0 | Running times right-aligned, always `mm:ss` from the book (§6.17); cue counts are integers and never rounded, suffixed or "~". |
| Prices | Playfair Display 600 | 20–28px | 0 | The one number front of house is allowed to glamour; always paired with its mono terms line beneath. |

**Type laws.** (1) *Numerals are data.* A running time, a cue
count, a date in the running order is set in Space Mono tabular
figures and traces to the book or the season record — Playfair
numerals appear only in prices and the show year on the title.
(2) *The cue word is never decorative.* STANDBY and GO are set
only when a cue is genuinely armed or called (§6.2, §6.9);
a button labelled GO that merely links somewhere is slop (§9).
(3) *Pencil is a colour, not a font.* Annotations, check-offs
and corrections are `--go-lit` or `--hemp-dim` Space Mono —
there is no handwriting font backstage; the stage manager types
and pencils in the same hand. (4) Letterspacing is for cue lines
and labels only; body text is never tracked out — typed sheets
are not.

## 4. Layout language

The page is a stage plan drawn in section: a black floor, a
working margin, and marks that say where things stand.

- **The prompt-corner margin.** At ≥1200px the layout carries a
  fixed left margin, 264px wide, which is the prompt corner
  (§6.11): cue list, cue lamp, running-time tally, house tabs.
  Content lives in the remaining measure as if on the stage
  floor to its right. The margin is not a sidebar with widgets;
  it is a *position* — the corner the show is called from — and
  nothing may be placed in it that the stage manager would not
  have on the desk: the book, the lamp, the clock, the tabs.
- **The floor grid.** Content sections sit on a 12-column grid
  with a 96px vertical rhythm — one "board" — and each section
  is a *scene*: it occupies the full stage width available to
  it, enters as one placed unit (§6.8), and its key element
  stands on spike marks (§6.5) that are part of the section's
  own layout, not an overlay. Scenes are separated by black —
  real black, `--wing` unbroken for at least one board — the
  way scenes are separated by the dark they change in.
- **Density.** Working density: mono body at 16.5/1.65, tables
  at 13–15px with 10px cell padding, cue lines rationed to one
  per scene. The page never crowds: a backstage that is tidy
  enough to run in the dark is the aesthetic. Whitespace here is
  *wing space* — the kept-clear area stage left where the next
  scene is preset — and it is defended in §9 against filling.
- **The proscenium trace.** A single worn-gilt hairline
  (`--gilt`, 1px, 55% opacity) runs the content edge where the
  prompt margin meets the floor at ≥1200px: the one line where
  the two buildings touch. It is the only gilt geometry allowed
  outside titles and prices.
- **Section choreography.** Each scene follows the call order:
  cue line first (top-left of the scene, where the SM's eye
  lands), title under the followspot, body in the lit pool,
  key element on its marks, paperwork (table, tally, note) at
  the scene's foot. No scene may lead with an image: backstage,
  things are *called*, then they appear.

## 5. Full motion system

Every motion term, in this theme's own language. One shared rAF
loop drives all scroll-scrubbed values with lerp **0.12** (the
wagon loop — heavy things glide and settle, they do not snap to
scroll); discrete calls (cue flashes, blackouts, lamp blinks) run
on their own timers and never write styles from scroll handlers.

**Named easings.** `--ease-pulley` — rope-and-pulley:
`cubic-bezier(.68,0,.22,1)`, a fast haul that eases as the load
comes onto the rope, for the curtain and flown scenery.
`--ease-wagon` — wagon-brake: `cubic-bezier(.19,.86,.24,1)`, a
long heavy glide with a firm stop, for set pieces and the
backdrop scrub settle. `--ease-call` — the called snap:
`cubic-bezier(.2,.9,.25,1)`, 120–240ms, for cue flashes, lamp
blinks, spike pops. `--ease-drift` — dust in a beam:
`cubic-bezier(.45,.05,.55,.95)` at 6–11s, for ambient loops.
`--ease-breath` — house lights: `ease-in-out` at 1400ms, used
exactly once per page (§6.10).

- **Scroll-triggered reveals — called cues.** A section is not
  revealed; it is called (§6.2): at 62% viewport height the
  prompt corner arms the cue (red), 400ms later calls GO
  (green), and the section's entrance runs. No section animates
  before its cue; no cue fires without its section.
- **Scroll-driven / scrubbed — the backdrop haul.** The flown
  backdrop (§6.4) is bound to scroll progress through its scene
  with the wagon lerp: rope, cloth and sandbags in counterweight,
  position = f(scroll) exactly, reversible while scrubbing (a
  flown cloth *can* be lowered again — unlike a called cue,
  which once checked off stays checked, §6.6).
- **Parallax.** Three depths, all in the hero and backdrop
  scenes only: curtain folds at 0.92×, rope runs at 1.0×, the
  lit stage beyond at 1.06× — a shallow backstage box, never a
  landscape. Parallax is banned from paperwork scenes (tables,
  forms): paperwork does not drift.
- **Pinned scenes.** The prompt corner pins for the whole page
  (≥1200px). The big scene change pins the backdrop scene for
  180vh while the haul completes. Nothing else pins: a theatre
  has one prompt corner and one fly floor, not five.
- **Masked & staggered reveals.** Show titles are called letter
  by letter (§5 entrance): each letter snaps in on a cue-light
  blink, 45ms stagger, `--ease-call`. Spike marks pop in
  staggered 60ms apart (§6.5). Set pieces take their marks one
  at a time in blocking order (§6.8), never as a simultaneous
  fade — simultaneous fades are cinema, not stagecraft.
- **Blur-to-sharp.** Banned. Backstage light does not focus
  like a lens; things are lit or they are in the dark. The
  theme's reveal states are *dark → lit* (opacity + a 6%
  brightness lift under the followspot), never blurred.
- **Counters.** Running time and cue count tally in the prompt
  book (§6.14) in spinning-free mono: digits change at 90ms
  steps, quantised, landing exactly on the book's figures.
- **Progress indicator.** The cue list itself (§6.6): green
  pencil check-offs down the margin, current cue lit. There is
  no progress bar anywhere on the page.
- **Marquee.** Refused. Nothing backstage scrolls sideways on a
  loop; the one horizontal traveller in the building is the
  curtain, and it travels once, on a cue.
- **Kinetic typography.** The letter-by-letter title call
  (above) and the cue line's type-on: Q-numbers type at 28ms
  per character when the corner first arms them. No other type
  moves.
- **SVG line-draw.** The blocking diagram's chalk line (§6.7)
  draws at 900ms/m of path, `--ease-wagon`, crosses and arrows
  in blocking order.
- **Image scale-in-frame.** Photographs (production stills,
  the house at night) stand in taped frames and are *lit*, not
  scaled: a followspot pool (§6.8 hover) blooms over the frame
  at 500ms `--ease-drift`; the image itself never zooms — a
  photograph backstage is a thing on a wall, not a screen.
- **Hover / magnetic / tilt.** Hover blooms a followspot pool
  on set pieces and cards (§6.12); magnetic pull is refused
  (ropes pull scenery, not pointers); tilt is refused (flats
  stand plumb or they fall). Buttons answer with the lamp:
  hover arms (red glow 120ms), click calls (green blink).
- **Custom cursor.** Normal system cursor only. Standing rule.
- **Skeleton loading.** The uncalled scene (§6.16): paperwork
  printed at 40% ink behind a "NOT YET CALLED" tape strip,
  written in full when its cue is called.
- **Page transitions.** The blackout (§6.3) at scene changes
  in-page; the tabs-closed curtain (§6.16) between pages.
- **Ambient loops.** Exactly two: dust drifting in the hero's
  followspot beam (11s, §6.1 scene) and the standby lamp's slow
  pulse while a cue is armed (2.4s, §6.2). Both pause offscreen
  and under reduced motion. A third loop is a gate failure.
- **Reduced motion.** Curtain opens instantly, blackouts are
  removed (scenes simply stand), no drift, no pulse, scrubbed
  haul jumps to its scroll-true position without lerp. The
  page rests fully lit, fully called, fully readable.


## 6. Signature elements

### 6.1 The sideways parting curtain

- **What & why.** The page opens behind a closed curtain — full
  viewport, deep folds, hemp-dark rather than red-velvet (the
  working tabs, not the house tabs) — and on first scroll it does
  not rise: it *parts sideways*, hauling on ropes with
  rope-and-pulley easing, fabric bunching at both edges with fold
  shading deepening as it gathers, until the lit stage beyond
  stands revealed with the headline centre. It belongs because
  entry is stagecraft: this theatre opens the way theatres
  actually open, and the visitor's first scroll is the first cue
  of the show — the page teaches its own grammar in its first
  gesture.
- **Structure.** The hero scene ships complete in the DOM
  beneath the curtain: headline, cue line, hero copy, all lit
  and readable. The curtain is two absolutely positioned panels
  (left/right) over the hero only, each a layered CSS/SVG fold
  field (repeating-linear-gradient fold shading over `--wing`
  deepened to `#0B0908`, one SVG turbulence pass for cloth
  grain), `pointer-events:none`, `aria-hidden`. Rope runs are
  two 2px `--hemp-dim` lines at the panels' top corners that
  visibly travel as the panels part. JS arms the parting by
  adding `.tabs-open` on first scroll intent; without JS the
  panels are never rendered (they are inserted by the arming
  script, not shipped in HTML).
- **Motion spec.** Trigger: first scroll intent (wheel, touch
  drag, or keyboard scroll) after load, once per session
  (`sessionStorage` flag `fw-tabs`). Panels travel from
  centre-closed to bunched at edges over 1400ms `--ease-pulley`:
  fast haul in the first 55% (the pull), easing settle as folds
  gather. Fold shading deepens via a gradient-position shift
  bound to the same progress. Rope lines extend at 1.0× panel
  travel. At completion the panels rest bunched at 11% width
  each side, framing the hero for the rest of the visit — they
  are never removed; a parted curtain stays parted, at the
  edges, like tabs do.
- **States.** Closed (first paint before arming — hero already
  readable beneath if the overlay is absent) → parting (1400ms)
  → parted (rest). Hover/focus: none; the curtain is not a
  control. Returning visitor within session: opens parted.
  Scrolled-past: unchanged — scrolling back to the top never
  re-closes the tabs; shows do not un-open.
- **Content merge.** The curtain is the page's own front door:
  what it reveals is the show title itself, centre-stage, and
  the bunched folds remain as the hero's frame — the building's
  architecture, not a splash screen over it.
- **Failure fallback.** Watchdog at 1800ms from arming: if the
  parting has not completed (rAF starved, tab backgrounded),
  panels jump to parted and the flag is set. No-JS: no curtain
  exists; the hero simply stands lit. The law (§1) holds: the
  overlay is inserted only by the script that can also remove
  it, over content that never depended on it.
- **Reduced-motion variant.** No travel: if armed at all, the
  panels are placed already parted at first paint — the visitor
  arrives to an open stage. No fold animation, no rope travel.
- **Performance budget & mobile variant.** Fold field is CSS
  gradients + one inline SVG ≤ 6KB; transform-only animation,
  two panels, zero ongoing cost after t=1400ms. Mobile
  (<768px): panels part over 1100ms to 7% bunched width, fold
  count reduced from 9 to 5 per panel, grain pass dropped.
- **Choreography timeline (v2).** t=0 first paint (hero lit
  beneath, curtain closed if armed) → first scroll intent →
  t=0–770ms haul phase (panels to 62% open, ropes extending) →
  t=770–1400ms settle (folds bunch, shading deepens) → t=1400ms
  rest, hero fully framed → §6.2 arms Q1 at t=1450ms → dust
  loop (§5) fades in over the following 2000ms → watchdog
  deadline t=1800ms passes unused.
- **State matrix (v2).** *Rest:* parted, framing the hero.
  *Hover:* none. *Focus:* focus landing inside the hero before
  first scroll parts the curtain instantly to its end state (a
  keyboard visitor is never asked to scroll through a door).
  *Active:* n/a. *Scrolled-past:* stays parted. *Disabled /
  no-JS:* no curtain; hero lit. *Touch:* first drag parts it;
  a tap does not (taps are for controls, and this is not one).
- **Breakpoints (v2).** ≥1200px: bunched panels 11% each side,
  9 folds per panel, hero framed within the prompt-corner
  layout. 768–1199px: 9% panels, 7 folds. <768px: 7% panels,
  5 folds, parting 1100ms, the prompt corner already stacked
  above (§6.11) so the hero takes full width.
- **Edge cases & failure modes (v2).** *Slow network:* the
  curtain is CSS/SVG only — it never waits for an image; if
  fonts lag, the parting still runs (the title reflows once,
  in the dark, before the reveal completes). *Tab hidden
  during parting:* rAF pauses; on visibility the watchdog
  settles the panels parted — no half-open curtain greets a
  returning visitor. *Very tall hero content:* panels are
  hero-height, not page-height; the curtain never covers
  content below the fold. *Scroll-jacking refusal:* the
  parting is bound to the visitor's own scroll position via
  the shared loop, never to a hijacked timer — if they do not
  scroll, the tabs stay closed and the hero's first screen
  still shows its title strip above the curtain's hem line.
- **Accessibility spec (v2).** The curtain is decorative over
  complete content: `aria-hidden`, absent from the tab order,
  and the hero headline is in the accessibility tree from
  first paint. A visually hidden "skip the opening" is
  unnecessary because focus parts it instantly (above).
  `prefers-reduced-motion` removes the travel entirely.
- **Tokens consumed (v2).** `--wing`, `--hemp-dim`, `--gilt`
  (hem line), `--ease-pulley`, `--dur-tabs` (1400ms),
  `--tabs-bunch` (11%).

### 6.2 Called cues

- **What & why.** Every section of the page is a cue. As the
  visitor scrolls a section toward its mark, the prompt corner
  (§6.11) arms its cue: the cue line flashes in Space Mono, the
  cue lamp blinks red — *standby* — then, 400ms later, green —
  *GO* — and only then does the section take its place with its
  entrance. Sections do not reveal; they are *called*, in
  order, off the book (§6.17). It belongs because it is the
  theme's central verb: the page runs on a prompt book, and the
  visitor feels the show being run — someone competent is on
  the cans, and nothing appears by accident.
- **Structure.** Each scene carries a cue line element
  (`<p class="cue-line">Q13 · <span class="cue-word">STANDBY
  </span></p>`) printed in the DOM with its number from the
  book, and a lamp: a 10px disc beside the cue line in the
  prompt corner's list and a matching lamp in the corner
  header. The word is text, always — colour is never the only
  signal. An IntersectionObserver at 62% viewport height arms
  the cue; the GO call is a timer, not a scroll threshold, so a
  fast scroller's cues queue and call in order at 400ms
  intervals rather than firing in a pile.
- **Motion spec.** Arming: lamp fades to `--cue-red-lit` over
  160ms `--ease-call`, word flips to STANDBY, a single 90ms
  blink. Standby hold: 400ms (the SM's beat — long enough to
  read, short enough to feel called). GO: lamp crosses to
  `--go-lit` with a 120ms double-blink (blink-blink, the real
  cue-light language for "execute"), word flips to GO, and the
  section's entrance begins in the same frame. The cue line in
  the section itself strikes through in green pencil (§6.6)
  once its entrance completes.
- **States.** Uncalled (cue line printed dim, `--hemp-dim`,
  word reads the section's name, not STANDBY) → standby (red,
  400ms) → GO (green, entrance running) → called (rest: word
  removed, cue line at full `--hemp`, tick in the margin list).
  Hover: cue lines are not controls (the clickable version is
  §6.9). Focus: a cue line is never focusable. Scrolled-past:
  stays called — cues are one-way, like check-offs.
- **Content merge.** The cue line is the section's own header
  furniture — it sits above the section title, naming the
  section the way the book names it. Remove the mechanism and
  the page loses its section headers, not a decoration.
- **Failure fallback.** Watchdog per cue: if the observer never
  fires (JS partial failure), a scroll-position sweep on the
  shared loop arms any cue whose section is above 62% — and if
  JS is absent entirely, every section stands called: cue lines
  print with their numbers, no word, sections fully visible.
  A cue can fail to *perform*; it can never hide its section.
- **Reduced-motion variant.** No blinks, no 400ms hold: the cue
  word flips STANDBY → GO in one step as the section arrives,
  and the section stands without entrance motion. The
  paperwork (numbers, words, ticks) is identical.
- **Performance budget & mobile variant.** Observer + timers
  only; lamp is a background-color transition on a 10px disc.
  Budget: ≤ 2KB of JS shared with §6.6/§6.11. Mobile: the lamp
  and cue line render in the stacked corner (§6.11) above the
  section instead of the fixed margin; timing identical.
- **Choreography timeline (v2).** Section top crosses 62%
  viewport → t=0 arm (red fade 160ms, blink at t=160ms) →
  t=0–400ms standby hold → t=400ms GO double-blink (120ms) →
  t=400ms section entrance starts (§6.8 or the scene's own) →
  entrance completes → green-pencil tick drawn in margin
  (240ms, §6.6) → cue count tally increments (§6.14).
- **State matrix (v2).** *Rest (called):* full hemp cue line,
  tick present. *Hover:* n/a. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* called state persists; scrolling up never
  un-calls. *Disabled:* a cue whose section was removed from
  the page is struck from the book (§6.17) and never arms —
  the corner never calls a cue for a scene that is not there.
  *Touch:* identical; no touch-specific states.
- **Breakpoints (v2).** ≥1200px: lamp + line in fixed prompt
  corner and mirrored cue line atop each section. 768–1199px:
  corner becomes a slim top bar (§6.11); cue lines remain atop
  sections. <768px: cue line atop section only; the corner bar
  shows current cue + lamp.
- **Edge cases & failure modes (v2).** *Jump scroll* (anchor
  link, find-in-page): all cues above the landing point call
  instantly in order without the 400ms holds — the SM catches
  up the book in one pencil pass. *Back-button return mid-page:*
  cues above restore as called from the book state, not
  re-performed. *Section taller than viewport:* arms on its
  cue line crossing 62%, not its top. *Duplicate numbers:* a
  build-time check (§10) fails the build if two sections claim
  one Q-number — the book is the single source (§6.17).
- **Accessibility spec (v2).** Cue state changes are **not**
  announced live — a screen-reader visitor hears the section
  headings in order, not a running commentary of lamps. The
  cue word is real text beside the lamp at every state
  (contrast: `--cue-red-lit` 5.57:1 and `--go-lit` 8.19:1 on
  `--wing`, both pass for the 13px bold mono). Lamp discs are
  `aria-hidden`; the word carries the meaning.
- **Tokens consumed (v2).** `--cue-red`, `--cue-red-lit`,
  `--sm-green`, `--go-lit`, `--hemp`, `--hemp-dim`,
  `--ease-call`, `--dur-arm` (160ms), `--dur-standby` (400ms),
  `--dur-go-blink` (120ms).


### 6.3 The 200ms blackout scene change

- **What & why.** Between major scenes — season to company,
  company to visit, visit to the form — the page dips to black
  for exactly 200ms and the new scene is already standing when
  the light returns. No fade, no cross-dissolve, no wipe: a
  blackout is the theatre's honest machine for changing the
  world in the dark, at the duration a real blackout takes to
  fall and lift. It belongs because transitions in this theme
  are stage machinery, not film grammar — and because 200ms is
  short enough that the visitor feels a *blink of the house*,
  not a loading state.
- **Structure.** A single fixed overlay, `#0A0806` (blacker
  than `--wing` — a blackout is darker than the wings), opacity
  0 at rest, `pointer-events:none`, inserted by the arming
  script over a page whose scenes all ship in place. The
  blackout fires when a scene boundary crosses 50% viewport
  during scroll: opacity snaps to 1 in ≤30ms (a blackout
  *falls* — it does not fade), holds while the incoming scene's
  entrance states are set beneath it, and lifts at exactly
  200ms total.
- **Motion spec.** Total event: 200ms, no easing curve on the
  fall or the lift (steps, not slopes — light switches, it does
  not glide). Fall ≤30ms, hold ≈140ms, lift ≤30ms. Maximum one
  blackout per 1200ms of scrolling; boundaries crossed inside
  the lockout simply stand lit when reached. The blackout
  never fires on upward scroll (scene changes happen on the
  way in, not on the way back) and never twice for one
  boundary.
- **States.** Rest (opacity 0) → blackout (200ms) → rest.
  Hover/focus/active: none — it is not a control and never
  intercepts input (pointer-events none throughout, so a click
  mid-blackout lands on the scene beneath). Scrolled-past:
  boundaries behind the visitor never re-fire.
- **Content merge.** The blackout *is* the seam between the
  page's acts — it exists only where the content genuinely
  changes scene (a new company, a new room of the building),
  and §7's map fixes which boundaries earn one. A page that
  blackouts between two paragraphs has misunderstood it (§9).
- **Failure fallback.** The lift is a timer set at the moment
  of the fall, independent of rAF, scroll, or asset state: at
  200ms the overlay is at opacity 0 whatever else has failed.
  A second hard watchdog at 600ms removes the overlay node
  from the DOM entirely if its opacity is somehow still >0.
  No-JS: no overlay exists. The law (§1): a blackout always
  lifts.
- **Reduced-motion variant.** No blackout, ever. Scenes stand
  in place; the boundary is marked only by the black board of
  wing space the layout already keeps between scenes (§4).
- **Performance budget & mobile variant.** One fixed div, one
  opacity transition: negligible. Identical on mobile — a
  blackout costs the same in a hand as in a house.
- **Choreography timeline (v2).** Boundary crosses 50% →
  t=0–30ms fall → t=30–170ms hold (incoming scene's §6.8 marks
  set beneath) → t=170–200ms lift → incoming scene's cue
  (§6.2) arms at t=200ms → watchdog checkpoint t=600ms passes
  with overlay at 0.
- **State matrix (v2).** *Rest:* overlay transparent.
  *Hover/focus:* unaffected; focus is never moved or trapped
  by a blackout — the focused element beneath keeps focus
  throughout. *Active:* n/a. *Scrolled-past:* spent.
  *Disabled:* reduced-motion and no-JS both disable it
  entirely. *Touch:* identical; touch scrolling across a
  boundary fires the same 200ms event.
- **Breakpoints (v2).** Identical at all widths — the one
  element with no breakpoint behaviour, deliberately: a
  blackout does not care how wide the stage is.
- **Edge cases & failure modes (v2).** *Fast scroll through
  three boundaries:* lockout (1200ms) collapses them to the
  first blackout; the rest stand lit. *Scroll stops exactly on
  a boundary:* the blackout fires once when the boundary is
  crossed, not repeatedly while it hovers at 50% (hysteresis:
  re-arm only after 15vh of travel away). *Tab hidden
  mid-blackout:* timers still run; the visitor returns to a
  lit page. *Print:* overlay never prints (print stylesheet
  removes it).
- **Accessibility spec (v2).** The overlay is `aria-hidden`,
  carries no content, and moves no focus. Photosensitivity:
  200ms at ≤30ms edges is a single dark blink, below flash
  thresholds (no luminance oscillation — one fall, one lift);
  reduced-motion removes it for any visitor who asks.
- **Tokens consumed (v2).** `--blackout` (`#0A0806`),
  `--dur-blackout` (200ms), `--blackout-lockout` (1200ms).

### 6.4 The flown backdrop haul

- **What & why.** Mid-page, the season's backdrop — a painted
  cloth, full stage width — is *flown*: as the visitor scrolls
  through its pinned scene, the cloth hauls up its rope marks,
  the rope runs travel through their cleats, and the sandbags
  on the counterweight cradle descend exactly as far as the
  cloth rises. Cause and counterweight, both visible: the
  scenery moves by its real mechanism. It belongs because
  flying is the wings' most beautiful labour, and because a
  scrubbed image that merely slides is a screensaver — this
  one is rigging, with the physics drawn in.
- **Structure.** A pinned scene (`position:sticky` stage,
  180vh scroll length at ≥1200px) containing: the cloth (a
  full-bleed production image or painted SVG backdrop, hung
  from a batten bar), three rope lines (2px `--hemp-dim`)
  running from batten to a cleat rail at stage right, rope
  marks (numbered tape ticks on the rail: OUT, ¼, ½, ¾, DEAD —
  the flyman's marks), and a sandbag stack (SVG bags, hemp with
  gilt stencilled weights) on a cradle at stage left. Cloth
  position, rope offset and bag height are all transforms of
  one scrub value `q` from the shared rAF loop (lerp 0.12).
- **Motion spec.** Scrub: as scroll crosses the 180vh scene,
  `q` runs 0→1; the cloth translates up by 62% of its height
  (`--ease-wagon` settle applied to the lerp, not the mapping —
  the mapping is linear and honest, the *feel* is the wagon).
  Bags descend the same pixel distance the cloth's batten
  rises — counterweight arithmetic is exact, not approximate:
  `bagY = −clothY`. Rope marks pass the cleat line in order;
  at DEAD (q=1) the cloth is fully flown and the scene
  unpins. Scrolling back lowers the cloth and raises the bags
  — flying is reversible, unlike cues.
- **States.** Rest (cloth at OUT, bags high) → hauling
  (scrubbing) → flown (DEAD, rest). Hover: the cleat rail
  highlights the nearest mark (hemp brightens 160ms).
  Focus: the scene is not focusable as a unit; its caption
  link is a normal link. Scrolled-past: cloth stays at DEAD
  until scrolled back into the scene. Disabled: no-pin
  fallback (below).
- **Content merge.** The cloth *is* content: it carries the
  season's painted backdrop with the headline production's
  title worked into the painting, and its caption — set as a
  flyman's note — names the production, the painter and the
  cloth's own cue (it flies on Q31 in the real show, and the
  page says so). Remove the haul and the season loses its
  centrepiece image, not a widget.
- **Failure fallback.** If `position:sticky` or rAF fails, the
  scene renders unpinned with the cloth at ½ (half-flown, the
  most legible state) and bags matched — a still photograph of
  the rig, fully captioned. No-JS: same still. The image
  itself is a normal `<img>`/SVG in flow: it can never be
  hidden by the mechanism that moves it.
- **Reduced-motion variant.** No pin, no scrub: the cloth
  stands at ½ with its caption, bags matched beside it — the
  rig at rest, honestly photographed.
- **Performance budget & mobile variant.** Transforms only on
  three layers; cloth image ≤ 180KB (AVIF/WebP) or inline SVG
  ≤ 40KB. Mobile (<768px): scene length 120vh, cloth travel
  45%, bags move to a single bag (the stack is a desktop
  pleasure), rope lines reduce to two.
- **Choreography timeline (v2).** Scene top reaches viewport
  top → pin engages → scroll 0–180vh maps q 0→1 (lerped) →
  marks pass cleat at q=0.25/0.5/0.75 (¼, ½, ¾ — each tick
  brightens 120ms as it passes) → q=1: DEAD, a single soft
  canvas-bag settle (translateY 3px, 240ms `--ease-wagon` —
  the load coming onto the cleat) → unpin → §6.2 calls the
  next scene's cue.
- **State matrix (v2).** *Rest:* at OUT or DEAD per scroll.
  *Hover:* cleat marks brighten. *Focus:* caption link normal.
  *Active:* n/a. *Scrolled-past:* holds DEAD. *Disabled:*
  still at ½. *Touch:* scrub bound to touch scroll identically;
  no separate gesture — the page never traps touch to fly the
  cloth.
- **Breakpoints (v2).** ≥1200px: 180vh scene, 62% travel,
  3 ropes, full bag stack (5 bags). 768–1199px: 150vh, 55%
  travel, 3 ropes, 3 bags. <768px: 120vh, 45%, 2 ropes,
  1 bag, marks list shortened (OUT, ½, DEAD).
- **Edge cases & failure modes (v2).** *Image fails to load:*
  the painted SVG fallback stands in the same frame (the
  frame and caption are independent of the image). *Content
  longer than expected* (a second cloth requested): refused —
  one flown cloth per page; a second becomes a §6.12 card.
  *Scroll-up mid-haul:* bags rise, cloth lowers, exact reverse
  — the arithmetic is symmetric by construction. *Low-power
  device:* lerp drops to 0.2 (stiffer, cheaper) and the bag
  settle is cut; the scrub itself never is.
- **Accessibility spec (v2).** The haul is decorative motion
  over a captioned image: the image carries full alt text
  (what the backdrop depicts), the caption is real text, and
  the rope marks are `aria-hidden` (their information — how
  far the cloth has flown — is not information a non-visual
  visitor needs, and the alt says "shown flown halfway" only
  in the still state). Reduced motion gets the still.
- **Tokens consumed (v2).** `--hemp`, `--hemp-dim`, `--gilt`
  (bag stencils), `--ease-wagon`, `--lerp-wagon` (0.12),
  `--haul-travel` (62%).


### 6.5 Spike-tape marks

- **What & why.** On the floor of every scene, glow-tape marks
  show where things stand: a cross of two tape strips at the
  exact point each section's key element takes, an arrow of
  tape pointing to it from the wing side, and — for elements
  that travel in (§6.8) — their number in tape numerals beside
  the mark. Backstage, spike marks are how a show survives its
  crew changing nightly: the floor remembers. On the page they
  are wayfinding with the metaphor load-bearing — the mark is
  *at* the element, pointing *at* the element, and appears when
  the element is called. It belongs because it is the theme's
  anti-slop signature (§9): tape that points at nothing is the
  exact failure this theme exists to refuse.
- **Structure.** Inline SVG per scene, absolutely positioned
  over the scene's floor area, `aria-hidden`, `pointer-events:
  none`: tape strips are rounded rectangles (7px wide, lengths
  34–52px) in `--go-lit` at 82% opacity with a 1px darker edge
  — glow tape in working light is pale green-white, and the
  theme spends its `--go-lit` here as a material, not a signal.
  Each mark is grouped: cross + arrow + optional numeral, with
  a `data-stands-for` naming the element it marks (audited,
  §10: every mark's target must exist in the same scene).
- **Motion spec.** Marks pop in after their scene's cue GO
  (§6.2): staggered 60ms apart in blocking order, each a 180ms
  `--ease-call` scale from 0.6 with a 2px settle — tape pressed
  down by a thumb, not faded in. A mark for an element that has
  not yet taken its position (§6.8) pops at 55% opacity and
  firms to full when the element lands on it.
- **States.** Uncalled (absent — the floor is bare until the
  scene is preset) → popping (180ms × stagger) → standing
  (rest). Hover: none (marks are floor, not controls).
  Scrolled-past: marks persist — tape stays down for the whole
  run; scrolling back up, the floor is still marked.
  Disabled/no-JS: marks are printed standing from the start
  (they are in the shipped SVG, dimmed only by the arming
  script).
- **Content merge.** Total: a mark with no element on it is a
  build error, and an element of §6.8 without a mark is
  equally one. The marks are how the visitor learns where to
  look in a black scene — the eye goes to the tape, the tape
  is under the thing.
- **Failure fallback.** Marks ship visible in the SVG; the
  pop-in is armed by JS hiding them first. Any failure leaves
  standing tape and standing content. If SVG is unavailable,
  marks degrade to a CSS cross (two rotated divs) with the
  arrow dropped — position survives, direction is a luxury.
- **Reduced-motion variant.** Marks stand from first paint of
  their scene; no pop, no stagger. The floor is simply already
  marked, as it is when the crew arrives.
- **Performance budget & mobile variant.** ≤ 1.5KB SVG per
  scene, transform/opacity only. Mobile: arrows shorten by
  30%, numerals drop (numbers are in the cue line instead),
  crosses unchanged — a mark must survive a small floor.
- **Choreography timeline (v2).** Scene cue GO (t=0) → first
  mark pops t=80ms → subsequent marks +60ms each → travelling
  elements' marks at 55% until landed (§6.8) → all marks full
  by the time the scene's entrance completes → marks rest for
  the page's duration.
- **State matrix (v2).** *Rest:* standing, full opacity.
  *Hover:* none. *Focus:* none — marks are never focusable.
  *Active:* n/a. *Scrolled-past:* standing. *Disabled:*
  standing (shipped state). *Touch:* identical; marks are not
  touch targets and never enlarge to become any.
- **Breakpoints (v2).** ≥1200px: full marks with numerals.
  768–1199px: numerals kept, arrows −15%. <768px: no numerals,
  arrows −30%, cross size unchanged (a spike mark is a spike
  mark at any stage size).
- **Edge cases & failure modes (v2).** *Responsive reflow*
  moves an element off its mark: marks are positioned relative
  to the element's own box (anchored to the element, offset to
  its floor corner), not to page coordinates — the tape moves
  with the furniture it marks, as real tape on a set piece
  does. *Overlapping marks* in a dense scene: stagger marks by
  10px along the floor edge; never stack crosses. *Long
  scenes:* marks rationed to the key element + at most two
  secondary — a floor covered in tape marks nothing.
- **Accessibility spec (v2).** Fully decorative and
  `aria-hidden`: the information a mark carries ("the key
  element is here") is carried for non-visual visitors by
  document order — the key element follows its heading
  directly. Contrast is a material property, not text; no
  requirement, but the 82% `--go-lit` on `--wing` measures
  ≈6.4:1 for anyone reading the numerals at ≥1200px.
- **Tokens consumed (v2).** `--go-lit`, `--wing`,
  `--ease-call`, `--dur-spike` (180ms), `--spike-stagger`
  (60ms).

### 6.6 Green-pencil cue progress

- **What & why.** The margin cue list is the page's progress
  indicator, and it progresses the way a stage manager's book
  does: as each cue is called (§6.2), its entry in the prompt
  corner's list is checked off in green pencil — a hand-drawn
  tick stroke in `--go-lit` — and the entry firms from dim to
  full hemp. There is no progress bar anywhere on the page
  because the building already owns a better instrument: a
  list that fills with ticks *is* the show advancing, and the
  visitor can read *which* cues remain, not just how many.
- **Structure.** The cue list is real HTML in the prompt corner
  (§6.11): an `<ol>` printed from the book (§6.17), each entry
  `Q13 — Fly the cloth` with a tick slot (14px SVG path,
  stroke `--go-lit`, stroke-width 2.5, round caps — a pencil
  tick, slightly irregular path by design). Entries ship
  unticked and dim (`--hemp-dim`); the tick path's
  stroke-dashoffset is armed by JS only.
- **Motion spec.** On a cue's entrance completing: the tick
  draws over 240ms `--ease-call` (dashoffset → 0, the pencil
  moving left-to-right, down-up — the actual stroke order of a
  tick), and the entry's colour steps to `--hemp` over the
  same 240ms. The currently-armed cue's entry pulses its lamp
  (§6.2) but is not yet ticked — a tick means *done*, in
  pencil, forever: ticks never un-draw on scroll-up.
- **States.** Upcoming (dim, unticked) → armed (lamp lit,
  §6.2) → called (tick drawn, full hemp) → rest. The final
  entry — the last cue of the book — when ticked, the list's
  foot prints `THAT'S THE SHOW.` in caption mono (§12 voice).
  Hover on an entry: if its scene is on the page, the entry
  underlines in pencil (a 1px `--go-lit` line draws 160ms) —
  entries are links to their scenes (§6.11). Focus: same
  underline + visible outline. Scrolled-past: ticks persist.
- **Content merge.** The list is the book's table of contents
  and the page's progress in one object: every entry is a real
  section, in order, with its real name. It cannot drift from
  the page because it is generated from the same record
  (§6.17) — progress here is not a percentage of scroll, it is
  a count of *work done*, which is why it never lies about a
  long scene: a 180vh haul is one cue, ticked once.
- **Failure fallback.** No-JS: entries print unticked and full
  hemp (the book before the show — still a complete contents
  list). If the tick SVG fails, the tick degrades to a printed
  `✓` in `--go-lit` mono — the pencil becomes a pen, the record
  survives.
- **Reduced-motion variant.** Ticks appear fully drawn in one
  step when their cue calls; no draw-on. Entries still firm in
  colour (a state change, not a motion).
- **Performance budget & mobile variant.** One 14px SVG path
  per entry, dash animation on a single property: negligible.
  Mobile: the list lives in the collapsed corner (§6.11) as
  `Q13 / Q52 · CALLED` summary + expandable full list; ticks
  identical.
- **Choreography timeline (v2).** Cue GO (t=0, §6.2) → scene
  entrance runs → entrance completes → t=+0 tick draws 240ms
  → entry firms → §6.14 tally increments its cue count in the
  same beat → next cue may arm (queue, §6.2).
- **State matrix (v2).** *Rest:* per state above. *Hover:*
  pencil underline (link entries). *Focus:* underline +
  2px `--go-lit` outline offset 2px. *Active:* entry pressed
  — jumps scroll to its scene with the §6.16 blackout.
  *Scrolled-past:* ticked, permanent. *Disabled:* an entry
  whose scene is absent is struck from the list at build
  (§6.17 audit), never rendered disabled. *Touch:* entries are
  ≥36px tall targets in the expanded list.
- **Breakpoints (v2).** ≥1200px: full list in the fixed
  corner, ticks + names. 768–1199px: list in the top bar's
  disclosure, ticks + names. <768px: summary line + disclosure;
  inside, full list at 15px mono.
- **Edge cases & failure modes (v2).** *Very long books*
  (30+ cues): the corner list scrolls internally with the
  current cue kept in view (scroll-into-view on arm, instant
  under reduced motion); the page's own scroll is never
  hijacked for it. *Jump scroll:* all passed cues tick in one
  240ms pencil pass, in order — the SM catching up the book.
  *A cue re-called via §6.9:* its tick does not redraw (it was
  never un-ticked); the replay is the section's, not the
  record's.
- **Accessibility spec (v2).** The list is a nav landmark
  (`aria-label="Cue list"`); the current cue carries
  `aria-current="true"`; tick SVGs are `aria-hidden` and each
  called entry's link text gains a visually hidden "(called)"
  suffix so state is available non-visually. Colour is never
  the only signal: tick + full-strength text accompany the
  green.
- **Tokens consumed (v2).** `--go-lit`, `--hemp`,
  `--hemp-dim`, `--sm-green`, `--ease-call`, `--dur-tick`
  (240ms).


### 6.7 The blocking diagram chalk line

- **What & why.** Across the floor of the company scene, an SVG
  chalk line draws the blocking diagram: the stage rectangle in
  chalk-white hemp, crosses where each dancer or actor stands,
  curved arrows for the crosses' travel, numbered positions in
  chalk numerals. Blocking is the choreography written down
  before it is danced — the diagram is drawn *on the floor it
  describes*, at the moment the scene that uses it arrives.
  It belongs because it is the one place the theme lets a
  drawing be a drawing: chalk on boards, explaining real
  positions, in the scene about the people who stand in them.
- **Structure.** One inline SVG (viewBox 800×460) laid as the
  scene's floor panel, beneath the company copy and beside the
  cast list it diagrams: stage outline, 6–9 crosses (two-stroke
  paths), 3–4 travel arrows (curved paths with chalk arrowheads),
  position numerals in Space Mono rendered as SVG text. All
  strokes `--hemp` at 78% with a 0.6px rough edge (an SVG
  feTurbulence displacement at 1.2 scale — chalk is not a
  vector). Paths ship fully drawn; dash offsets are armed by
  JS only.
- **Motion spec.** Trigger: the scene's cue GO. Draw order is
  blocking order: stage outline first (1100ms), then crosses in
  position order (each 260ms, 90ms stagger), then arrows
  (480ms each, overlapping the last cross by 120ms), numerals
  fade-stamp last (120ms each). Stroke speed ≈ 900ms per metre
  of path at desktop scale, `--ease-wagon` throughout — chalk
  moves at hand speed, steadily, with the hand's slight ease at
  corners.
- **States.** Undrawn (armed only) → drawing (≈3.4s total) →
  drawn (rest, permanent). Hover on a cross: the corresponding
  cast-list entry highlights (`--go-lit` left rule, 160ms) and
  vice versa — diagram and list are one dataset (§6.17's
  company record). Scrolled-past: stays drawn; chalk is not
  wiped between visits within the session.
- **Content merge.** The diagram's crosses are the cast list's
  people, in their actual opening positions for the headline
  production; its caption is the SM's note ("Opening positions —
  Act I, from the book"). It teaches the visitor to read a
  stage the way the company does. A diagram of nothing, or of
  positions no scene uses, is §9 slop.
- **Failure fallback.** Paths ship drawn; any JS failure leaves
  a complete chalk diagram. No-SVG fallback: the cast list
  stands alone with positions in text ("Amara — centre, mark
  3") — the information has a text home independent of the
  drawing.
- **Reduced-motion variant.** Diagram stands fully drawn at
  scene entry; hover cross-highlighting remains (it is a state
  change at 160ms, kept under the motion threshold — and is
  removed too if the visitor's setting is paired with reduced
  transparency requests).
- **Performance budget & mobile variant.** One SVG ≤ 9KB,
  dash animations on ≤ 14 paths, no ongoing cost. Mobile: the
  diagram stacks above the cast list at full width; arrows
  reduce to 2 (the principal crosses), numerals kept — a
  phone floor is smaller, the blocking is not falsified, only
  the minor travels are left undrawn and their positions remain
  in the text list.
- **Choreography timeline (v2).** Cue GO t=0 → outline draws
  t=100–1200ms → crosses t=1200–2600ms (260ms each, 90ms
  stagger) → arrows t=2480–3900ms → numerals stamp
  t=3900–4300ms → diagram rests; cast-list hover links arm.
- **State matrix (v2).** *Rest:* drawn. *Hover:* cross ↔ list
  entry highlight pair. *Focus:* cast-list entries are links;
  focusing one highlights its cross identically to hover.
  *Active:* n/a. *Scrolled-past:* drawn. *Disabled:* no-JS =
  drawn (shipped state). *Touch:* tap on a cast entry
  highlights its cross for 1200ms (no hover on touch, so the
  pairing is tap-driven).
- **Breakpoints (v2).** ≥1200px: diagram right of the copy,
  800×460. 768–1199px: diagram below the intro copy, full
  measure width. <768px: stacked first, simplified arrows (2),
  numerals 11px minimum.
- **Edge cases & failure modes (v2).** *Cast changes* (a
  production recast): diagram and list regenerate from the
  company record — a hand-edited SVG that disagrees with the
  list is a gate failure (§10 cross-check). *Long cast*
  (12+ positions): crosses cap at 9 drawn; the rest are listed
  as "ensemble — upstage line" in text, the way real blocking
  books notate a chorus. *Displacement filter unsupported:*
  strokes render clean — chalk becomes pencil, acceptable.
- **Accessibility spec (v2).** The SVG is `role="img"` with a
  full text alternative: "Blocking diagram: opening positions
  for Act I — " followed by the position list, identical to
  the cast list's text. The diagram adds no information the
  text lacks; it adds *sight* of it, which is its honest job.
- **Tokens consumed (v2).** `--hemp`, `--go-lit`, `--wing`,
  `--ease-wagon`, `--dur-chalk` (900ms/m).

### 6.8 Set pieces taking their marks

- **What & why.** A scene's furniture — its card, its table,
  its image frame, its price block — does not fade in. Each
  piece *takes its mark*: it travels the last part of the way
  in, sliding or scaling the final distance onto its spike
  marks (§6.5) and settling with a wagon-brake ease, in
  blocking order, one at a time. Content arrives like scenery:
  carried in, placed, and *stopped* — the settle matters, a
  piece that glides to a halt without weight reads as a
  screensaver, and a piece that snaps reads as a pop-up. It
  belongs because placing is the wings' core skill, and because
  the visitor should feel the scene being *set* by hands that
  know the floor.
- **Structure.** Each set piece is a normal content element
  with a `data-mark` naming its spike cross. Its shipped state
  is *on* its mark, fully visible. JS arming translates it off
  its mark by its travel vector — pieces from the wings slide
  from their wing side (left pieces −48px, right +48px),
  flown pieces drop from +36px above, floor pieces scale from
  0.96 at their base — and the entrance returns it to zero.
  Travel vectors are per-piece attributes set from the scene's
  blocking (§6.7's logic), never randomised.
- **Motion spec.** Trigger: the scene's cue GO (§6.2). Pieces
  move in blocking order, 140ms stagger, each 620ms
  `--ease-wagon` (long glide, firm stop), with a final 60ms
  1px settle (the wagon brake biting). A piece's spike mark
  firms from 55% to full (§6.5) in the frame it lands. Total
  scene entrance ≤ 620 + 140×(n−1) ms, capped: pieces beyond
  the fifth travel together as one preset unit (a dressed
  flat, not five chairs).
- **States.** Off-mark (armed only) → travelling (620ms) →
  on-mark (rest). Hover (on interactive pieces — cards,
  buttons): the followspot pool blooms (§5, 500ms
  `--ease-drift`, a radial `--gilt` at 14% pool centred on the
  piece) — light, not lift; pieces never translate on hover,
  furniture does not lean toward visitors. Focus: outline in
  `--go-lit`. Scrolled-past: on-mark, permanent within the
  session.
- **Content merge.** The pieces *are* the content — this is
  the entrance grammar for everything the page shows, from the
  season cards (§6.12) to the running-order table (§6.13) to
  the form (§6.15). There is no separate decorative layer to
  merge with; the merge is total, which is the point.
- **Failure fallback.** Pieces ship on their marks. Watchdog
  per scene at entrance-start + 2000ms: any piece still
  translated is snapped to zero. No-JS: every scene stands set
  from first paint. A stuck animation leaves a *set stage*,
  never a scattered one.
- **Reduced-motion variant.** Pieces stand on their marks; the
  scene's arrival is marked only by its cue (§6.2). No travel,
  no settle, no spot bloom (focus outline remains).
- **Performance budget & mobile variant.** Transforms only,
  ≤ 6 concurrent travellers, all on the shared rAF loop.
  Mobile: travel distances halve (24px / 18px), stagger 100ms,
  scale pieces become slides (scale on small screens reads as
  zoom, and the theme bans zoom grammar, §5).
- **Choreography timeline (v2).** Cue GO t=0 → piece 1 travels
  t=0–620ms → piece 2 t=140–760ms → … → last piece lands →
  its mark firms → scene declared set → §6.6 tick draws.
- **State matrix (v2).** *Rest:* on-mark. *Hover:* spot pool
  (interactive pieces only). *Focus:* `--go-lit` outline 2px,
  offset 3px. *Active:* buttons/cards press 1px down (the
  piece's own weight) 90ms. *Scrolled-past:* on-mark.
  *Disabled:* a disabled control sits on its mark at 55% ink
  with its tape numeral struck — preset but not in this show.
  *Touch:* no hover pool; first tap on a card shows the pool
  for 600ms, second tap follows the link (the standard
  two-tap honesty for hover-bearing cards).
- **Breakpoints (v2).** ≥1200px: full travel vectors.
  768–1199px: vectors × 0.75. <768px: vectors × 0.5, scale
  pieces converted to slides, stagger 100ms.
- **Edge cases & failure modes (v2).** *Content added late*
  (a card injected by a filter, §6.12): it takes its mark with
  a single 420ms travel, no stagger queue — late furniture is
  carried in quietly, not re-set as a whole scene. *Very tall
  pieces* (the running-order table): travel is 24px maximum
  regardless of height — a table does not glide across the
  floor, it is *already there* and is uncovered. *Scroll-up
  re-entry:* pieces never re-travel; once set, a scene is set.
- **Accessibility spec (v2).** Entrance motion never delays
  content availability: pieces are in the accessibility tree,
  in order, from first paint (transforms do not remove them).
  Focus is never moved by an entrance. Touch targets on pieces
  are their natural sizes, ≥ 44px for controls.
- **Tokens consumed (v2).** `--gilt` (spot pool), `--go-lit`,
  `--ease-wagon`, `--ease-drift`, `--dur-set` (620ms),
  `--set-stagger` (140ms), `--lerp-wagon` (0.12).


### 6.9 Standby… GO — the reader's cue button

- **What & why.** In the prompt corner, beside each called
  cue, sits the one piece of power the page lends the reader:
  a cue button. Press it and the cue light blinks, the button's
  word flips from "standby…" to "GO", and that section's
  entrance (§6.8) executes again — the scene is re-set in front
  of you. It belongs because every other element keeps the
  visitor in the audience side of the wings; this one puts
  their finger on the cue button, for one section at a time,
  and teaches the standby/GO discipline by hand: you cannot GO
  without first standing by.
- **Structure.** A real `<button>` per called cue in the
  corner's list (§6.11), 44px tall, mono: left, the cue number;
  centre, its word (`standby…` at rest after first call, or the
  section name before); right, a 10px lamp (§6.2's lamp,
  shared). The button exists only for cues already called once
  by scroll — you cannot pre-call a scene you have not reached;
  the book is run in order even by its guests.
- **Motion spec.** Press: lamp arms red (120ms `--ease-call`),
  word flips to "standby…", hold 650ms (longer than the
  scroll call's 400ms — a hand on the button should feel the
  weight of the pause), then GO: lamp double-blinks green
  (120ms), word flips to "GO", and the target section — scrolled
  into view first if offscreen (a 700ms `--ease-wagon` scroll
  glide, or instant under reduced motion) — re-runs its §6.8
  entrance. After the entrance, the word settles back to the
  section name; the lamp rests green for 2000ms, then dims to
  hemp.
- **States.** Uncalled (button absent) → called (rest, section
  name) → standby (red, 650ms) → GO (green, entrance running)
  → called. Hover: lamp glows `--cue-red-lit` at 40% — the
  button *wants* to be armed. Focus: 2px `--go-lit` outline.
  Active: pressed 1px. Disabled: while its own entrance is
  running, the button is disabled (you cannot double-GO a
  scene mid-set) and reads "WORKING…".
- **Content merge.** The button operates the page's real
  sections — it is the cue list's verb. Its merge test: if a
  section's entrance cannot be re-run, its button must not
  exist; §6.4's flown cloth, notably, has no cue button (you
  re-fly it by scrolling, its own honest mechanism).
- **Failure fallback.** If the entrance re-run fails (element
  detached, rAF dead), the section snaps to its set state —
  the GO still "works" from the reader's side. The scroll
  glide failing leaves the button functional in place: press,
  blink, and the section resets where it stands.
- **Reduced-motion variant.** No standby hold theatrics beyond
  the word change (the 650ms hold remains — it is timing, not
  motion, and the discipline is the content), no scroll glide
  (instant jump), entrance replaced by the section standing set.
- **Performance budget & mobile variant.** Timers + the shared
  loop; ≤ 1KB. Mobile: buttons live in the expanded cue list
  (§6.11), full-width rows, 48px tall.
- **Choreography timeline (v2).** Press t=0 → lamp red t=120ms
  → "standby…" holds t=120–770ms → GO blink t=770–890ms →
  scroll glide (if needed) t=890–1590ms → entrance re-run
  (§6.8 timeline) → lamp rests green 2000ms → dims.
- **State matrix (v2).** *Rest:* section name, lamp hemp.
  *Hover:* red glow 40%. *Focus:* green outline. *Active:*
  1px press; the standby sequence. *Scrolled-past:* n/a (the
  button lives in the corner). *Disabled:* during its own
  re-run, "WORKING…". *Touch:* identical; the button is a
  ≥44px target and touch gets the full standby hold — the
  pause is the point on every device.
- **Breakpoints (v2).** ≥1200px: in the fixed corner list.
  768–1199px: in the top-bar disclosure list. <768px: same,
  full-width 48px rows.
- **Edge cases & failure modes (v2).** *Mash-pressing:*
  presses during standby queue nothing — the button is
  inert until the sequence completes (a cue button is not a
  drum). *Pressing for a section removed by a filter*
  (§6.12): the button for a hidden scene disables with the
  word "NOT IN THIS BILL" — the SM does not call scenes that
  are not in tonight's show. *Session return:* buttons exist
  for all cues called in previous visits this session (the
  book remembers, §6.6).
- **Accessibility spec (v2).** A button with an accessible name
  that includes its action and target: "Re-run cue Q13, Fly
  the cloth". State changes are announced politely via a
  visually hidden live region ("Q13 — GO") because here the
  *visitor* caused the call — the one place announcements
  belong (§6.2's scroll calls stay silent). The lamp is
  decorative; the word carries state.
- **Tokens consumed (v2).** `--cue-red-lit`, `--go-lit`,
  `--hemp`, `--ease-call`, `--ease-wagon`,
  `--dur-standby-hand` (650ms), `--dur-go-blink` (120ms).

### 6.10 Q47 — House lights. Breathe.

- **What & why.** One cue in the book is not a scene change.
  Between the visit information and the form, the cue list
  reads: *Q47 — House lights. Breathe.* When the visitor
  reaches it, nothing is set, flown or sold: the page warms
  its light by a fraction — the black lifts toward brown, the
  hemp gains amber — the machinery pauses for one beat, and a
  single line of copy stands in the warmed light: an invitation
  to do nothing for a moment, in a building that runs on
  split seconds. It is the theme's heart, hidden in its
  paperwork, and it belongs because backstage care is real:
  stage managers call rest cues, house lights are how a theatre
  says *you are safe, the show is held*, and a page that only
  ever sells and calls would have missed the reason people
  love the building.
- **Structure.** A scene of deliberate emptiness: one board of
  warmed wing space, the cue line, and one centred Playfair
  line (the house's own words — e.g. the season's title with
  "— house lights" in mono beneath). The warmth is a scoped
  token shift: within the scene, `--wing` → `#1B1510` and a
  radial `--gilt` glow at 9% pools from the top, as if the
  house tabs had opened a crack. The scene ships in its warmed
  state; JS arms the *transition into* warmth only.
- **Motion spec.** Trigger: Q47's cue (§6.2 calls it like any
  other — standby, GO). On GO: the warmth cross-fades over
  1400ms `--ease-breath` (the system's slowest ease, used
  nowhere else), holds for the scene's full height, and cools
  back over 1400ms as the next scene's cue arms. No element
  travels, draws or counts during Q47 — the pause is structural:
  it is the one scene with no §6.8 entrance.
- **States.** Uncalled (scene printed warm but unlit — flat
  `--wing`) → warming (1400ms) → house lights (rest, warm) →
  cooling (1400ms on exit). Hover/focus: none — there is
  nothing in the scene to operate, by design. Scrolled-past:
  cooled; the tick in the list (§6.6) is drawn like any other.
- **Content merge.** Q47 is in the book (§6.17) with a running
  time like every cue, appears in the running order (§6.13)
  as "HOUSE LIGHTS — BREATHE (0:45)", and its tick counts
  toward the show like any cue. It is not an Easter egg pasted
  between sections; it is paperwork that happens to be kind.
- **Failure fallback.** If the colour transition never runs,
  the scene stands at flat `--wing` with its line readable —
  a plainer pause, still a pause. No-JS: identical. Nothing in
  Q47 can hide content because there is almost no content to
  hide, and what there is ships lit.
- **Reduced-motion variant.** The warmth is present statically
  for the scene's extent (no cross-fade); everything else is
  unchanged — the pause survives intact, because the pause was
  never the motion.
- **Performance budget & mobile variant.** Two colour
  transitions on one scene: negligible. Mobile: identical;
  the scene is one board tall at every width.
- **Choreography timeline (v2).** Q47 arms (red, 400ms
  standby, §6.2) → GO → warmth fades in t=0–1400ms → the
  Playfair line stands (it never animated) → visitor crosses
  the scene at their own pace — the cue's running time in the
  book is 0:45, a suggestion, not a gate → next cue arms →
  warmth cools t=0–1400ms → Q47's tick draws.
- **State matrix (v2).** *Rest:* warm, still. *Hover:* none.
  *Focus:* the scene contains no focusable element except the
  global nav — a deliberate emptiness; keyboard visitors pass
  through one tab stop fewer. *Active:* n/a. *Scrolled-past:*
  cooled, ticked. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: scene spans the floor width,
  glow pool centred on the line. 768–1199px: same, pool 80%.
  <768px: the line wraps to two lines, glow softens to 6% —
  warmth, not glare, on a small screen at night.
- **Edge cases & failure modes (v2).** *A build that moves
  Q47* (a client wants it earlier): permitted — it is a cue,
  cues are numbered by the book — but it must remain a cue
  with nothing to sell; placing the form inside Q47's warmth
  is a §9 failure (the pause is not a conversion device).
  *Multiple Q47s:* refused — one rest cue per show; a second
  "breathe" is a poster, not paperwork. *Dark-mode tools*
  forcing colours: the warmth may flatten; the line and the
  pause remain.
- **Accessibility spec (v2).** Contrast inside the warmth:
  `--hemp` on `#1B1510` measures ≈10.6:1, Playfair line in
  `--paper` ≈14:1 — the warmed scene is as legible as the
  dark one. The scene's heading is its cue line; screen
  readers meet a short, quiet section, which is the correct
  experience. Nothing flashes, pulses or demands attention.
- **Tokens consumed (v2).** `--wing-warm` (`#1B1510`),
  `--gilt`, `--paper`, `--hemp`, `--ease-breath`,
  `--dur-house` (1400ms).


### 6.11 The prompt corner — navigation

- **What & why.** The site's navigation is the prompt corner:
  the desk position, stage left, from which the show is
  called. It holds the cue list (§6.6), the cue lamp (§6.2),
  the running-time tally (§6.14), and the house tabs — the
  site's main sections lettered on tabs of card like the
  dividers in a prompt book: SEASON · COMPANY · VISIT · JOIN.
  It belongs because a theatre site navigated from a top bar
  has put its visitors in the wrong building; here you navigate
  from the corner the show is run from, and the navigation
  *is* the progress, the lamp and the clock, in one desk.
- **Structure.** At ≥1200px: a fixed left column, 264px, full
  height, `--wing` with the gilt hairline at its right edge
  (§4). Contents top-to-bottom: the house name (Playfair, the
  one front-of-house sign allowed on the desk), the lamp +
  current cue readout, the cue list (`<nav aria-label="Cue
  list">` wrapping §6.6's `<ol>`), the tally (§6.14), and the
  house tabs as a vertical tab strip at the foot. All content
  is shipped HTML; the corner is never injected.
- **Motion spec.** The corner itself does not move. Within it:
  the lamp (§6.2 timings), tick draws (§6.6), tally steps
  (§6.14). Tab switches between pages run the §6.16 transition.
  The corner's internal list scrolls (when the book is long)
  with the current cue kept in view — an instant jump-cut
  scroll, never a glide: paperwork does not glide.
- **States.** Rest (current page's tab marked with a gilt
  edge and a pencil tick). Hover on tabs: hemp brightens
  120ms. Focus: `--go-lit` outline. Active tab: `aria-current=
  "page"`, its tab card stands 6px proud of the strip (a
  physical tab, pulled). Scrolled-past: n/a — the corner is
  the constant.
- **Content merge.** The corner holds nothing decorative: name,
  lamp, book, clock, tabs. Remove it and the site loses its
  navigation, its progress and its cue system at once — the
  definition of merged.
- **Failure fallback.** The corner is plain HTML/CSS: no-JS
  leaves a fully working nav (tabs are links, the list is a
  contents). If fixed positioning fails, it renders as a
  static header block above the content — less theatrical,
  fully usable.
- **Reduced-motion variant.** Identical (the corner has no
  motion of its own); lamp pulses and tick draws follow their
  own reduced variants.
- **Performance budget & mobile variant.** Static layout,
  negligible cost. 768–1199px: the corner becomes a top bar —
  house name, lamp + current cue, tally, and a "THE BOOK"
  disclosure holding the cue list and tabs. <768px: same bar,
  tally compresses to cue count only.
- **Choreography timeline (v2).** Page load: corner stands
  complete → Q1 arms per §6.2 → on each call, lamp + list +
  tally update in the §6.2/§6.6 beats → on tab press, §6.16
  transition runs and the new page's corner stands with its
  own book.
- **State matrix (v2).** *Rest:* as above. *Hover:* tabs
  brighten. *Focus:* visible outline, list entries per §6.6.
  *Active:* tab pressed → transition. *Scrolled-past:* n/a.
  *Disabled:* a tab for a page not in this bill (e.g. JOIN
  during a dark week) renders struck-through in pencil with
  the note "DARK" — theatres go dark; the book says so.
  *Touch:* tabs ≥44px tall in bar form.
- **Breakpoints (v2).** ≥1200px: fixed 264px corner.
  768–1199px: top bar 64px + disclosure. <768px: top bar 56px,
  house name shortens to its initials in gilt if the full name
  exceeds the bar (never wraps to two lines).
- **Edge cases & failure modes (v2).** *Long house names:*
  Playfair name caps at 24px in the corner and wraps to two
  lines maximum, pushing the lamp down — the lamp is never
  squeezed out. *Long books:* internal scroll (§6.6).
  *Print:* the corner prints as a header with the full cue
  list unticked — a paper book, correctly.
- **Accessibility spec (v2).** Landmarks: `banner` (house
  name), `nav` (cue list), `nav` (house tabs, labelled).
  Skip link lands on the first scene's heading, past the
  corner. Focus order: skip → tabs → cue list → content.
  All corner text ≥ 12.5px mono with the contrasts of §2.
- **Tokens consumed (v2).** `--wing`, `--gilt`, `--hemp`,
  `--hemp-dim`, `--go-lit`, `--corner-w` (264px).

### 6.12 The call board — season & show cards

- **What & why.** In the wings, the call board is where the
  company's paper lives: tonight's call sheet, notices, the
  season pinned up. The page's listing surface — productions,
  tour dates, workshops — is a call board: each item a card of
  `--paper` pinned to the black, headed by its call time (its
  date) in mono, titled in Playfair, with its spike numeral
  (§6.5) taped at the corner. It belongs because listings in
  this world are not a shop grid; they are the notices the
  company itself reads, and a visitor browsing the season is
  reading over the stage manager's shoulder.
- **Structure.** Cards on a 2–3 column board (grid, 20px gaps)
  within the scene. Card: paper ground, top strip with call
  date + running time (mono, from the season record), Playfair
  title, one-line mono description, a production still in a
  taped frame (two tape strips, top corners, §6.5's material),
  and a foot row: venue + its cue-button-style link "STANDBY —
  details" (a link, styled as paperwork, never a fake GO,
  §3 law 2). Cards ship complete; §6.8 gives them their marks.
- **Motion spec.** Cards take their marks per §6.8 (slide from
  their wing side, 620ms `--ease-wagon`, 140ms stagger, cap 5
  then preset unit). Hover: followspot pool blooms over the
  card's image (500ms `--ease-drift`) and the card's tape
  numeral firms. Filtering (by month / by company) re-sets the
  board: departing cards are *struck* — a pencil line draws
  through them (200ms) and they fold to 0 height (300ms
  `--ease-wagon`) — while arriving cards take their marks at
  the §6.8 late-arrival 420ms.
- **States.** Rest (pinned, lit). Hover: spot pool + numeral
  firm. Focus: `--go-lit` outline on the card's link.
  Active: n/a. Scrolled-past: set. Disabled: a sold-out or
  dark production's card is pencil-struck with "DARK — NO
  PERFORMANCE" taped across its foot — it stays on the board
  (the company still did the show) but its link is removed.
  Touch: two-tap honesty per §6.8.
- **Content merge.** The board is the season: dates, running
  times and venues are the record's own data, and the card for
  the headline production is the same object whose backdrop
  flies in §6.4 and whose blocking is chalked in §6.7 — one
  production, three paperwork views, all agreeing (§10).
- **Failure fallback.** Cards ship set and readable; filters
  are progressive enhancement over a complete board (no-JS:
  all cards, no filter — the full season pinned up, as it
  would be). Images failing leave taped empty frames with alt
  text standing in the frame (§9 forbids broken-image icons;
  the frame + caption carry on).
- **Reduced-motion variant.** Cards stand; filtering swaps
  instantly (struck cards simply absent, with the filter's
  count line updated); no pools.
- **Performance budget & mobile variant.** Images ≤ 90KB each,
  lazy below the fold; grid reflow is layout, not animation.
  Mobile: single column, cards full measure, tape numerals
  dropped (per §6.5), spot pool off (no hover), tap targets
  ≥48px.
- **Choreography timeline (v2).** Scene cue GO → cards take
  marks (staggered, §6.8) → board rests → filter press →
  strikes draw 200ms → folds 300ms → arrivals take marks
  420ms → count line updates ("6 CALLS PINNED") last, in mono.
- **State matrix (v2).** *Rest:* pinned. *Hover:* pool +
  numeral. *Focus:* outline. *Active:* link press 1px.
  *Scrolled-past:* set. *Disabled:* struck DARK state above.
  *Touch:* two-tap per §6.8; filters are ≥44px chips.
- **Breakpoints (v2).** ≥1200px: 3 columns. 768–1199px: 2
  columns. <768px: 1 column, card padding 16px, title 24px.
- **Edge cases & failure modes (v2).** *Empty filter result:*
  the board shows the empty state in voice (§12): a single
  paper slip — "NOTHING PINNED FOR THOSE DATES. THE BOARD IS
  EMPTY, NOT BROKEN." — with a clear-filter link. *Long
  titles:* Playfair clamps at 2 lines with the full title in
  the link's accessible name. *Many cards (20+):* the board
  paginates by bill (§11) rather than infinite scroll — a
  call board has edges.
- **Accessibility spec (v2).** Cards are list items in a
  `<ul>`; each card's link has a full accessible name (title +
  date + venue). Paper ground carries `--wing` text at 11.42:1
  (hemp-on-wing inverted: text is `--wing` on `--paper`,
  ≈13.9:1). Filter changes announce the count politely.
- **Tokens consumed (v2).** `--paper`, `--wing`, `--gilt`,
  `--go-lit`, `--hemp-dim`, `--ease-wagon`, `--ease-drift`,
  `--dur-set` (620ms).


### 6.13 The running order — cue table

- **What & why.** One scene prints the whole show as a table:
  the running order. Columns: CUE · CALL · SCENE · RUNNING
  TIME — every cue in the book, in order, with the stage
  manager's notes in a final pencil column. It is the page's
  data table and its proof of law (§1): the corner's list, the
  called cues and this table are one record in three
  printings, and a visitor who doubts the page's paperwork can
  check it here, in full, in mono. It belongs because a theme
  whose credibility is its book must somewhere *show the whole
  book* — and because running orders are genuinely useful:
  members plan their night by them.
- **Structure.** A real `<table>` on a `--paper` ground (the
  book's page, §2) with `--wing` text, ruled with 1px
  `--hemp-dim` lines, sticky header row. Rows for cues already
  called carry the green-pencil tick in the CUE cell (§6.6's
  tick, same SVG). The notes column is `--sm-green` pencil
  text on paper (6.04:1 for `--paper` on green is the inverse;
  here green ink on paper measures ≈5.9:1 — pencil that can be
  read). Q47's row is present, worded exactly as in the book.
- **Motion spec.** The table takes its mark as one preset unit
  (§6.8, 24px travel maximum — paperwork is uncovered, not
  hauled). Rows do not animate individually. When a cue calls
  (§6.2) while the table is on screen, its row's tick draws
  (240ms, §6.6) and the row flashes once with a 6% gilt wash
  (300ms) — the SM's pencil tapping the line. Nothing else in
  the table ever moves.
- **States.** Rest (printed, ticks per progress). Hover on a
  row: the row's left edge gains a hemp rule (120ms) — rows
  are not links, hover is a reading aid only. Focus: the table
  is not focusable; its one interactive child (a "print the
  running order" button, §11) is a normal button.
  Scrolled-past: ticks persist. Disabled: n/a.
- **Content merge.** The table is generated from §6.17's
  record at build time — hand-editing a row is a gate failure
  (§10 diff-checks table vs book vs corner list). Its merge is
  the law itself, printed.
- **Failure fallback.** A table needs no fallback: it ships
  printed. No-JS: ticks for cues called *this session* are
  absent (the book before the show) — the table is complete
  regardless; progress is the enhancement.
- **Reduced-motion variant.** Ticks appear drawn; the gilt row
  flash becomes a static 600ms wash (state, not motion) or is
  dropped at the builder's discretion — the tick remains.
- **Performance budget & mobile variant.** Static table,
  ≤ 60 rows by law (a longer book paginates by act, §11).
  Mobile: the NOTES column drops (notes live in the scenes
  themselves), CUE/CALL/RUNNING TIME remain, 13px mono,
  horizontal scroll is *refused* — the table reflows, it does
  not slide off the stage.
- **Choreography timeline (v2).** Scene cue GO → table
  uncovers (24px, 420ms) → stands → live ticks/flashes as
  later cues call (only if the visitor lingers) → print button
  arms.
- **State matrix (v2).** *Rest:* printed. *Hover:* row rule.
  *Focus:* print button only. *Active:* n/a. *Scrolled-past:*
  printed, ticks current. *Disabled:* n/a. *Touch:* rows are
  reading matter, not targets; the print button is 44px.
- **Breakpoints (v2).** ≥1200px: 5 columns incl. NOTES.
  768–1199px: 4 columns (notes merged into SCENE as a second
  line). <768px: 3 columns as above, header sticky retained.
- **Edge cases & failure modes (v2).** *A cue with no running
  time* (Q47's pause is timed 0:45 in the book — every cue has
  a time, even the rest): a row may never print "—"; if the
  book lacks a time, the build fails (§10). *Very long scene
  names:* wrap to two lines; the table grows, it does not
  truncate the book. *Print:* this table is the print
  stylesheet's centrepiece — full book, unticked, on paper.
- **Accessibility spec (v2).** Proper `<th scope>` headers,
  caption: "Running order — every cue in the book, in order."
  Ticks are `aria-hidden`; called rows carry a visually
  hidden "(called)" in the CUE cell. Contrast on paper:
  `--wing` text ≈13.9:1, pencil notes ≈5.9:1.
- **Tokens consumed (v2).** `--paper`, `--wing`, `--sm-green`,
  `--hemp-dim`, `--gilt`, `--go-lit`, `--dur-tick` (240ms).

### 6.14 The half-hour call — running-time tally

- **What & why.** On the prompt desk, two numbers keep the
  show honest: how long it has been running, and how many cues
  have been called. On the page they tally in the corner (§6.11)
  as the visitor descends: RUNNING TIME — the sum of the book
  times of the scenes passed, in `mm:ss` — and CUES CALLED —
  *n* of *N*, an integer count of §6.6's ticks. They belong
  because they are the theme's counters, and they obey the
  law: both are computed from the book (§6.17), never from
  scroll percentage, never estimated. A tally that says 12:30
  is claiming twelve and a half minutes of show have passed in
  front of this visitor — the book must back it.
- **Structure.** Two mono readouts in the corner, labelled in
  caption caps: `RUNNING TIME 12:30` / `CUES 9 / 52`. Values
  are text nodes updated by the cue system (§6.2) on each
  call — there is no independent clock: the tally advances
  when a cue calls, by that cue's book time, and at no other
  moment. Between cues the numbers are still, as a stopped
  show clock is still.
- **Motion spec.** On a cue call: the cue count increments in
  one step; the running time counts in 90ms quantised steps
  from the old sum to the new (a 3:00 cue adds its time over
  ≈600ms of stepping digits — the SM writing the time up).
  Digits never spin, blur or roll; mono digits step, like a
  flip clock's duller, honester cousin.
- **States.** Rest (current sums). Hover/focus: none — the
  tally is a readout, not a control. Scrolled-past: sums are
  monotonic — scrolling up never subtracts (the show does not
  un-run). Session return: sums restore from the book state.
  Disabled: n/a.
- **Content merge.** The tally is the corner's clock, and its
  figures are the same figures the running order (§6.13)
  prints per cue and totals — three printings, one arithmetic.
  The final cue's call sets RUNNING TIME to the book's total,
  and the corner prints beneath it: `FULL TIME — AS CALLED.`
- **Failure fallback.** No-JS: the tally prints the book's
  totals as static text ("RUNNING TIME OF THE FULL SHOW
  94:00 · 52 CUES") — the same numbers, framed as the show's
  facts rather than the visitor's progress.
- **Reduced-motion variant.** Steps become single-step updates
  (old sum → new sum in one change). The numbers are the
  content; the stepping is not.
- **Performance budget & mobile variant.** Two text updates
  per cue: negligible. Mobile bar: running time drops, cue
  count remains (`CUES 9 / 52`) — the count is the progress;
  the clock is a desk luxury.
- **Choreography timeline (v2).** Cue entrance completes →
  tick draws (§6.6, 240ms) → in the same beat, count +1 and
  time steps begin (≈600ms) → tally rests at the new sums
  before the next cue can arm.
- **State matrix (v2).** *Rest:* sums stand. *Hover:* none.
  *Focus:* none (not focusable; available to AT as text in
  the corner landmark). *Active:* n/a. *Scrolled-past:*
  monotonic. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: both readouts in the corner.
  768–1199px: both, in the top bar, 12.5px. <768px: count
  only.
- **Edge cases & failure modes (v2).** *A cue re-called via
  §6.9:* adds nothing — re-running a scene does not re-run
  the show's clock (the tally counts first calls only, and
  §6.17's record marks them). *Book edited* (a scene added):
  totals recompute from the record; a hard-coded total
  anywhere is a gate failure. *Visitor reads without
  scrolling:* tally stands at 0:00 / 0 — honest: no show has
  been called yet.
- **Accessibility spec (v2).** Readouts are plain text in the
  corner, *not* a live region (a clock announcing itself
  every cue would be unbearable); a visually hidden summary
  in the cue list's nav ("9 of 52 cues called") carries the
  same state for AT at section boundaries.
- **Tokens consumed (v2).** `--hemp`, `--hemp-dim`,
  `--go-lit`, `--dur-step` (90ms).


### 6.15 The stage-door form — membership & joining

- **What & why.** Every theatre night ends at the stage door,
  and every visit to this site ends at its form: membership,
  enrolment, backstage-tour booking — the conversion, taken at
  the stage door, on a form that is a call sheet. Fields are
  calls: NAME · COMPANY (optional — theatres ask who you are
  with) · EMAIL · WHAT ARE YOU STANDING BY FOR (a select of
  real intents: Membership / Season ticket / Backstage tour /
  Classes) · and the submit is the one button on the page
  allowed the full ceremony: it reads "STANDBY", and on press
  it stands by, then goes. It belongs because conversion in
  this world is joining the building, and the form should feel
  like being put on the call sheet — your name, in the book,
  in pencil that becomes ink.
- **Structure.** A real `<form>` on a `--paper` ground (a call
  sheet pinned at the stage door, one tape strip at its head,
  §6.5's material), `--wing` text, mono fields with hemp rules,
  labels above fields in caption caps. The form is the scene's
  key element and stands on spike marks (§6.5). Validation is
  inline, per field, in the SM's voice (§12): errors in
  `--cue-red` ink on the paper (5.65:1 for `--paper` on red is
  the inverse — red ink on paper measures ≈4.6:1, used at
  13px bold mono only, always paired with the field's name).
- **Motion spec.** The form takes its mark per §6.8 (24px —
  paperwork). Field focus: the field's rule thickens to 2px
  `--sm-green` over 140ms (the pencil underlining where you
  are). Submit press: the button arms — word to "standby…",
  lamp red, 650ms hold (§6.9's hand discipline) — then GO:
  lamp green double-blink, the form is sent; on success the
  sheet is *signed off*: a green-pencil tick draws across the
  form's head (300ms) and the confirmation prints beneath in
  the book's format: "Q-LAST — [NAME] IS ON THE CALL SHEET."
  with a real reference from the response.
- **States.** Rest (sheet blank, button "STANDBY — JOIN").
  Focus: green rule. Filled-valid: field's tick in pencil at
  its right edge. Error: red ink message + field rule red;
  the error is written, never shaken (forms backstage are not
  shaken; they are corrected). Submitting: button disabled,
  "WORKING THE DOOR…". Success: signed-off state above; the
  form remains visible, struck through lightly in pencil —
  a completed call sheet is filed, not vanished.
- **Content merge.** The form's intents are the site's real
  conversions, its reference number enters the same world as
  the book (it is printed, kept, and quoted in the confirmation
  email's subject in the same format). The standby/GO ceremony
  is not decoration on a submit: it *is* §6.9's discipline,
  applied where a real commitment is made.
- **Failure fallback.** The form is a working HTML form: no-JS
  submits natively to its endpoint with server validation in
  the same voice. If the async path fails (network), the sheet
  stays filled — input is never eaten — and the note prints:
  "THE DOOR DIDN'T ANSWER. YOUR SHEET IS STILL FILLED IN —
  TRY AGAIN, OR WRITE TO [email]." A failed cue leaves the
  scene lit (§1).
- **Reduced-motion variant.** The standby hold shortens to
  250ms (the discipline is timing, kept in miniature), no tick
  draw (tick appears), no travel. Everything else identical.
- **Performance budget & mobile variant.** Native form +
  ≤ 3KB enhancement JS. Mobile: single column, fields 16px
  (no iOS zoom), button full width 52px, the tape strip and
  paper ground retained — the sheet is the sheet at any size.
- **Choreography timeline (v2).** Scene cue GO → sheet takes
  mark (420ms) → visitor completes fields (ticks per field) →
  press → standby 650ms → GO blink 120ms → send → success:
  head tick draws 300ms → confirmation prints → §6.6 ticks the
  scene's own cue if it was the page's last.
- **State matrix (v2).** *Rest:* blank sheet. *Hover:* button
  lamp glows red 40% (§6.9). *Focus:* green rules per field;
  visible focus on every control. *Active:* the standby
  sequence. *Scrolled-past:* n/a. *Disabled:* submit disabled
  only while sending. *Touch:* identical, targets ≥48px.
- **Breakpoints (v2).** ≥1200px: sheet 560px wide, two-column
  for NAME/COMPANY. 768–1199px: 520px, single column.
  <768px: full measure, single column, select native.
- **Edge cases & failure modes (v2).** *Long names / company
  names:* fields grow; the sheet never truncates the visitor's
  own name in the confirmation (it prints in full, wrapping).
  *Duplicate submission:* the signed-off state disables
  re-send; a second intent starts a fresh sheet via a printed
  link. *Honeypot/autofill:* standard, invisible, and never
  punished with a fake error — the door is polite.
- **Accessibility spec (v2).** Labels are real `<label>`s;
  errors are `aria-describedby`-linked and announced once on
  submit via a polite live region summarising count + first
  error ("Two calls need correcting — the first is EMAIL").
  Focus moves to the first error field on failed submit. All
  paper contrasts per §2/§6.13. The standby hold never blocks
  a screen-reader user: the button's state is text throughout.
- **Tokens consumed (v2).** `--paper`, `--wing`, `--sm-green`,
  `--cue-red`, `--cue-red-lit`, `--go-lit`, `--hemp-dim`,
  `--ease-call`, `--dur-standby-hand` (650ms).

### 6.16 Tabs closed — loader & page transition

- **What & why.** Between pages of the site, the tabs close
  and open: the incoming page arrives the way the next show
  does, behind a curtain that parts (§6.1's mechanism, at
  transition weight), and while a page is genuinely loading,
  the closed tabs carry a single printed line — "TABS CLOSED —
  [PAGE] IS BEING SET" — with the cue lamp on standby. It
  belongs because the site has already taught the visitor its
  door; using a spinner at the one moment the door is needed
  would break the world's contract. The skeleton state belongs
  here too: a scene not yet called prints its paperwork at 40%
  ink behind a tape strip reading "NOT YET CALLED" (§5).
- **Structure.** Transition: a full-viewport curtain (two
  panels, §6.1's build, heavier fold count) inserted on
  navigation click, closing over 500ms, page swap at full
  close, parting over 900ms on the new page. Loader: if the
  new page's first paint exceeds 900ms, the closed tabs show
  the printed line + lamp; there is no percentage — a set is
  ready when it is ready, and the book does not guess.
  Skeleton scenes are DOM sections with a `.not-called` class
  (40% ink, tape strip) removed by their cue (§6.2).
- **Motion spec.** Close 500ms `--ease-pulley` (heavier,
  slower than the hero's parting — full tabs, full weight),
  hold only as long as the swap needs (0ms target), part
  900ms `--ease-pulley`. Total perceived transition ≈ 1.4s
  worst case, and it is *skippable*: a second click or any key
  during the close jumps to the parted state on the new page.
- **States.** Idle (no overlay) → closing → closed (line +
  lamp if >900ms) → parting → idle. Hover/focus: the overlay
  is inert; focus is managed (below). Scrolled-past: n/a.
  Disabled: reduced-motion and no-JS both remove it (plain
  navigation).
- **Content merge.** The transition is the site's actual
  navigation (§6.11's tabs) — every internal page change uses
  it, no page invents its own. The skeleton's "NOT YET CALLED"
  strip names the real reason the scene is dim: its cue has
  not been called — loading states in this world are honest
  about being *unreached*, not "loading".
- **Failure fallback.** Hard watchdog: the closed state can
  never exceed 3000ms — at 3000ms the panels part on whatever
  page is present, complete or not. If the swap fails
  (navigation error), the tabs re-part on the *current* page
  and the corner prints the note: "THAT CALL DIDN'T GO
  THROUGH — YOU'RE STILL ON [PAGE]." No-JS: ordinary links,
  ordinary loads.
- **Reduced-motion variant.** No curtain: page changes are
  instant, and the skeleton state is not used (scenes print at
  full ink). The "NOT YET CALLED" concept survives only as
  the cue system itself.
- **Performance budget & mobile variant.** Panels are §6.1's
  assets reused (no second curtain to download). Mobile:
  close 420ms / part 760ms, folds reduced per §6.1.
- **Choreography timeline (v2).** Tab press t=0 → close
  t=0–500ms → swap at t≈500ms → (if load >900ms: line + lamp
  at t=900ms) → part t=+0–900ms from ready → new page's Q1
  arms → watchdog deadline (close + 3000ms) passes unused.
- **State matrix (v2).** *Rest:* no overlay. *Hover:* n/a.
  *Focus:* on parting, focus moves to the new page's first
  heading (a real focus management duty — the curtain never
  leaves focus on a removed page). *Active:* skip input
  during close. *Scrolled-past:* n/a. *Disabled:*
  reduced-motion / no-JS. *Touch:* swipe-back and system
  gestures are never intercepted; the transition decorates
  navigation, it does not own it.
- **Breakpoints (v2).** ≥1200px: full fold count. 768–1199px:
  −2 folds. <768px: timings above, lamp + line centred.
- **Edge cases & failure modes (v2).** *Back button:* the
  browser's own history wins — a bfcache restore shows the
  page parted, never mid-transition. *Slow page:* the 3000ms
  watchdog (above). *Anchor links within a page:* no curtain —
  the §6.3 blackout grammar covers in-page scene changes; the
  tabs are for *shows* (pages), not scenes.
- **Accessibility spec (v2).** The overlay is `aria-hidden`;
  a polite live region announces the new page's title once
  parted. Focus management per the matrix. Reduced-motion
  removes the whole ceremony without removing any content or
  any link.
- **Tokens consumed (v2).** `--wing`, `--hemp`, `--cue-red-lit`,
  `--ease-pulley`, `--dur-tabs-close` (500ms),
  `--dur-tabs-part` (900ms), `--tabs-watchdog` (3000ms).


### 6.17 The prompt book — the cue sheet record

- **What & why.** Behind every printing of the show stands one
  record: the prompt book. In build terms it is a single
  declared data object — every cue's number, name, scene,
  running time and note — from which the corner's list (§6.6),
  the running order (§6.13), the tally's arithmetic (§6.14)
  and every section's cue line (§6.2) are generated. It is an
  element of the theme, not an implementation detail, because
  the theme's law (§1) is a claim about this object: *the book
  does not lie* — and the visitor can audit the claim because
  the book is printed, whole, in §6.13. A theme about paperwork
  must have paperwork that reconciles.
- **Structure.** One source (a JSON/JS module or a templating
  data file, per stack) with entries:
  `{ q: 13, call: "FLY THE CLOTH", scene: "season-backdrop",
  time: 190, note: "Bags to the dead mark; check the cleat." }`
  (`time` in seconds; printed as `mm:ss`). Build generates:
  cue lines, corner list, running-order rows, tally totals,
  §6.9's buttons. Hand-written cue numbers in templates are a
  build error — the linter greps for `Q\d+` outside generated
  output and the book file itself.
- **Motion spec.** None of its own — the book is paper. Its
  motion is the sum of its printings' (§6.2, §6.6, §6.13,
  §6.14), all of which read their numbers from it.
- **States.** The book has one state per performance: tonight's
  bill. A matinee variant (a school show cut from the bill) is
  a *different book*, selected whole — entries are never hidden
  per-visitor at runtime, because a book with secretly missing
  cues is a lie with good typography.
- **Content merge.** Total: the book is the page's contents
  list, its clock and its contract. The company record (cast,
  positions for §6.7; productions for §6.12) sits beside it in
  the same source directory, under the same rule: one record,
  many printings.
- **Failure fallback.** If generation fails, the build fails —
  the book never falls back to hand-typed numbers (that is
  precisely the failure the law exists to prevent). At runtime
  the printings are static HTML; the record's absence cannot
  blank a page that has already been printed from it.
- **Reduced-motion variant.** n/a — paper does not move.
- **Performance budget & mobile variant.** The record itself
  ships to the client only as its printings (HTML) plus the
  small runtime state (called/not) — the full JSON is a build
  input, ≤ 8KB for a 52-cue book, not a page weight.
- **Choreography timeline (v2).** Build time: record → linter
  (numbers unique, sequential, timed) → generation of the four
  printings → §10 diff-check (printings agree) → ship.
  Runtime: the book's only event is a cue's state flipping to
  called, recorded against its entry.
- **State matrix (v2).** *Rest:* tonight's book. *Hover /
  focus / active:* n/a. *Scrolled-past:* entries flip to
  called (§6.6). *Disabled:* an entry for a cut scene is
  removed from the book and the book renumbers — Q-numbers
  are always sequential in the printed book; a gap would be a
  lie about a cue that never existed. *Touch:* n/a.
- **Breakpoints (v2).** The record is breakpoint-blind; its
  printings carry their own (§6.6, §6.13).
- **Edge cases & failure modes (v2).** *Two scenes claiming
  one number:* linter fails the build. *A scene with no cue*
  (an orphan section): linter fails — every scene is called
  or it is not in the show. *Running time zero:* permitted
  only for Q47-class pauses, which are timed honestly (0:45)
  — a 0:00 entry is a linter warning. *The book grows past
  60 cues:* the page splits by act (§11 pagination) rather
  than letting the corner list become a scroll of its own.
- **Accessibility spec (v2).** The record's printings carry
  the accessibility duties (§6.6, §6.13); the record itself
  must include, per cue, the plain-language call name used in
  §6.9's accessible button names — a cue whose name is
  backstage shorthand ("LX 12-ish") gets a book name a visitor
  can parse ("LIGHTS — THE STAGE WARMS").
- **Tokens consumed (v2).** None directly; its printings
  consume §6.2/§6.6/§6.13/§6.14's tokens.

### 6.18 The dark stage — 404 & empty states

- **What & why.** A page that does not exist is a dark stage:
  the house is real, the show is not on. The 404 stands in
  wing black with the tabs parted on nothing — an empty lit
  floor, one spike cross (§6.5) with nothing standing on it,
  and the stage manager's note in mono: "NO CUE CALLS THIS.
  THE PAGE YOU WANT ISN'T IN TONIGHT'S BILL." Beneath: the
  bill that *is* on — links to the season, the company, the
  visit page — set as a short cue list. It belongs because a
  theme's honesty is tested where it has nothing to sell: the
  dark stage does not pretend the missing page is a feature,
  does not apologise in front-of-house language, and puts the
  visitor back to work with the real bill in one glance.
- **Structure.** A normal page (corner §6.11 present, its book
  the *site's* bill, not a show's) with one scene: cue line
  "Q0 — DARK STAGE" (Q0 is reserved across the theme for the
  uncalled), the note, the empty mark (one cross, standing at
  55% — a mark waiting), and the bill links as §6.6-style list
  entries with pencil underlines. Empty states elsewhere
  (an empty filter board, §6.12; a search with no calls) reuse
  the same furniture at scene scale: one paper slip, the note
  in voice (§12), the way back.
- **Motion spec.** Almost none, deliberately: the scene stands
  set on arrival (no §6.8 travel — there is nothing to carry
  in). The one permitted motion: the empty spike cross firms
  from 55% to full over 600ms `--ease-drift` when the bill
  links take focus or hover — the mark brightens as if someone
  backstage has noticed you standing in the dark. The lamp in
  the corner stays dark: no cue is armed on a dark stage, and
  a blinking lamp here would be a lie.
- **States.** Rest (dark, note printed, links standing).
  Hover/focus on links: pencil underline (§6.6) + the mark
  firms. Scrolled-past: n/a (the page is one scene).
  Disabled: n/a.
- **Content merge.** The 404's bill links are the site's real
  navigation, and its Q0 convention is book-keeping: §6.17's
  linter reserves Q0 and forbids any real cue from taking it.
  The empty state is the theme's paperwork for absence.
- **Failure fallback.** The 404 must be the most robust page
  on the site: static HTML, no JS required for any of it, the
  corner's tabs as plain links. If the theme's CSS fails, the
  note and links still read in browser default styles — a dark
  stage with the lights out entirely still has a stage door.
- **Reduced-motion variant.** Identical, minus the mark's
  firming transition (it changes in one step).
- **Performance budget & mobile variant.** ≤ 30KB total page
  weight budget — the page a visitor meets when something
  already went wrong must not add its own weight to the
  evening. Mobile: identical structure, bill links full-width
  48px rows.
- **Choreography timeline (v2).** Arrival (via §6.16, parted
  tabs) → scene stands → note reads → links stand → (focus /
  hover) mark firms 600ms → departure via any bill link
  (§6.16 again). No cue arms; no tally moves (the site bill's
  tally is not shown on the dark stage — nothing is running).
- **State matrix (v2).** *Rest:* dark and still. *Hover:*
  underline + mark firms. *Focus:* outline + mark firms.
  *Active:* link press. *Scrolled-past:* n/a. *Disabled:*
  n/a. *Touch:* links are 48px rows; the mark firms on first
  tap's focus.
- **Breakpoints (v2).** ≥1200px: corner + centred scene.
  768–1199px: top bar + scene. <768px: scene full measure,
  the note at 16.5px — the SM's note is never shrunk to
  caption size; it is the page.
- **Edge cases & failure modes (v2).** *A deleted production's
  URL:* lands here, and the note gains one line if the
  referrer is internal: "IT WAS IN THE BILL — IT HAS BEEN
  STRUCK." with the season link (a struck show is still
  paperwork). *Search empties:* the scene-scale variant
  (above) with the query quoted in mono — the book records
  what was asked for, even when the answer is nothing.
- **Accessibility spec (v2).** The page's `<h1>` is the note
  itself (screen readers meet the meaning first). Status is a
  real 404. Links carry full names. Contrast per §2; the dim
  mark is decorative and `aria-hidden`.
- **Tokens consumed (v2).** `--wing`, `--hemp`, `--hemp-dim`,
  `--go-lit`, `--ease-drift`.

## 7. Page application map

- **Home (tonight's bill).** The full grammar: curtain (§6.1),
  called scenes in book order — the headline production (hero
  on its marks, §6.8), the flown backdrop (§6.4), the call
  board (§6.12), the company with its chalk blocking (§6.7),
  the running order (§6.13), Q47 (§6.10), visit paperwork, and
  the stage-door form (§6.15) as the last cue. Blackouts (§6.3)
  at two boundaries only: company → visit, visit → form.
- **Season / listing.** The call board (§6.12) is the page;
  its hero is a single board header (call date of the season's
  opening), no curtain — returning inside the building, the
  tabs are already open. Filters strike and pin per §6.12.
- **Production detail.** One show, whole book treatment: its
  own short cue list (the production's scenes — story, cast,
  dates, access), its backdrop as a still at ½ (§6.4's fallback
  state, by design), cast list paired with a small blocking
  diagram (§6.7 grammar at half scale), dates as a running
  order of performances (§6.13 grammar), and booking routed
  out to the plain checkout (see below).
- **Company / about.** The chalk scene (§6.7) leads; staff are
  listed as the book lists them — by job, in the order the
  show needs them: stage management first, then company, then
  front of house. (Backstage order is the theme's quiet joke
  and its thesis.)
- **Visit.** Pure paperwork, proudly: opening times as a
  running order, access information as SM's notes, the stage
  door address in mono with the one gilt line — the price of
  a backstage tour — set per §3's price rule.
- **Join / membership / enrol.** The stage-door form (§6.15)
  is the page; the scenes before it are the call board of
  membership tiers (cards §6.12, prices in Playfair per §3).
- **Checkout (tickets).** *Not this theme.* The site links out
  to a plain, fast, auditorium-clear checkout (the theme's own
  §1 ruling). The handoff is honest: a printed note at the
  link — "BOOKING LEAVES THE WINGS — THE BOX OFFICE IS PLAIN
  ON PURPOSE." A build that skins the seat map in wing black
  and cue lamps has failed §9.
- **404 / dark.** §6.18, verbatim.


## 8. Worked examples

### 8.1 The hero — "The Wintering" opens

The house is a producing theatre; the headline production is
*The Wintering*. The visitor arrives. First paint: wing black,
and — because the arming script ran — the closed tabs (§6.1),
hemp-dark folds, the gilt hem line at their foot. Beneath them,
already lit, the hero: cue line `Q1 · THE HOUSE OPENS`, the
title *The Wintering* in Playfair at 96px, beneath it the mono
standfirst: "A new play in the big house. Fourteen weeks. The
company is called for seven." — and at the hero's foot, its
paperwork strip: opening date, running time (2:05 incl.
interval, from the book), and the season's one gilt price.

First scroll: the tabs haul sideways over 1400ms
`--ease-pulley`, bunching to 11% at each edge, ropes travelling.
As they part, the title is called letter by letter — each
letter snapping in on a lamp blink, 45ms stagger — although the
title was never hidden: the call is a *performance over a
printed title*, letters re-striking in place (opacity was never
below 1; the blink is a gilt flash behind each letter, 90ms).
Dust begins its 11s drift in the followspot pool that blooms
over the title. Q1's tick draws in the corner; the tally reads
RUNNING TIME 03:00 · CUES 1 / 52 — Q1's book time, honestly
added. Scroll timeline: tabs (1400ms) → title call (letters,
≈800ms across) → dust in (2000ms fade) → hero rests, framed by
its own bunched curtain, for the rest of the visit.

### 8.2 Mid-page — the flown backdrop scene

Forty percent down the home page, the season's painted cloth.
The scene pins (180vh). Its cue was called as it approached:
Q31 in the corner list — standby, 400ms, GO — and the tick is
waiting for the haul, not the arrival: this scene's cue
completes at DEAD, not at pin. The cloth hangs at OUT: the
painted winter headland, the production's title worked into
the painting's sky, rope marks on the cleat rail at stage
right — OUT ¼ ½ ¾ DEAD — and five sandbags high on their
cradle at stage left, weights stencilled in gilt: 25, 25, 20,
20, 15.

The visitor scrolls. The shared loop (lerp 0.12) hauls: cloth
rising 62% of its height across the scene, bags descending
the exact pixel count the batten rises, rope lines travelling
through the cleat. The ½ mark passes and brightens; the
painting's lower half — painted as the view *from* the flown
position, the headland's continuation — comes into frame,
which is why the cloth was painted long. At DEAD: a 3px bag
settle, 240ms, the load coming onto the cleat; Q31's tick
draws; the tally adds 3:10. The caption, in the flyman's
voice: "Flown on Q31 in the show, by hand, in view of the
house. It takes eleven seconds and two people. Here it takes
your scroll." Scroll timeline: pin → haul (scroll-bound,
≈180vh) → DEAD settle (240ms) → tick → unpin → blackout
(200ms) into the company scene.

### 8.3 Conversion — the stage-door form

The last scene of the home page, after Q47's warmth has cooled.
Its cue: `Q52 · THE STAGE DOOR`. The sheet (§6.15) stands on
its spike marks — paper on black, one tape strip at its head —
headed "JOIN THE COMPANY OF THIS BUILDING" in Playfair (the
one glamour the door is allowed), with the mono sub-line:
"Membership is a standing call: first refusal on seats, the
wings open on tour nights, your name in the book."

A visitor — call her Samira — fills NAME and EMAIL, chooses
MEMBERSHIP from the select. Each valid field takes its pencil
tick. She presses STANDBY — JOIN. The button arms: "standby…",
lamp red, the 650ms hold — long enough for her to feel she is
committing to something with a door and a book, not a
newsletter. GO: green double-blink, the sheet sends. One
second later the head tick draws across the sheet in green
pencil, and the confirmation prints in the book's format:
"Q-LAST — SAMIRA IS ON THE CALL SHEET. REF W-2214. THE FIRST
CALL IS THE SEASON LAUNCH, 12 SEPT." Her sheet stays visible,
lightly struck — filed. The corner's final tick draws; beneath
the tally: "FULL TIME — AS CALLED." Scroll timeline: cue →
sheet set (420ms) → fields (visitor's pace) → standby (650ms)
→ GO → tick (300ms) → the show, and the visit, complete.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Tape that points at nothing.** Spike marks scattered as
   decoration, arrows aimed at margins, crosses under empty
   space. The theme's signature (§6.5) is a *claim* — something
   stands here — and decoration-tape is that claim lying.
   Cure: the §10 audit — every mark names its element, in its
   scene, or the build fails.
2. **Red used as a colour.** Cue-red as a heading colour, a
   sale badge, a hover state. Red backstage means *standby —
   something is about to move*. Cure: red exists only as
   §6.2/§6.9/§6.15's lamp and error ink; the gate greps for
   `--cue-red` outside those components.
3. **GO on a link.** A "GO" button that merely navigates.
   GO is a executed cue (§3, law 2). Cure: links are worded as
   paperwork ("STANDBY — DETAILS" is a link's most theatrical
   allowed form, and it navigates on click without pretending
   a cue fired).
4. **The fade-up reveal.** Sections fading and rising 20px in
   unison — cinema grammar wearing a headset. Cure: entrances
   are calls + placements (§6.2, §6.8), staggered in blocking
   order, or the scene stands still.
5. **A blackout that loads.** The 200ms dip stretched to hide
   late content, or fired between every pair of sections.
   Cure: §6.3's lockout and §7's boundary list; content ships
   in place, the blackout is a blink, not a curtain for
   lateness.
6. **Invented paperwork.** Cue numbers typed decoratively
   ("Q99!" on a poster block), running times rounded for
   rhythm, a tally that counts scroll percent. Cure: §6.17 —
   one book, generated printings, linter-enforced.
7. **Velvet and chandeliers.** Slipping front-of-house clip
   art — red curtains, gold tassels, comedy/tragedy masks —
   into the wings. The tabs here are hemp-dark working tabs;
   the masks are banned outright. Cure: the palette is closed
   (§2) and the material list is rope, canvas, tape, chalk,
   paper, one worn gilt.
8. **A progress bar.** Any bar, ring or percentage wearing
   this theme. Progress is a list with ticks (§6.6) or it is
   not this theme. Cure: gate grep for progressbar roles
   outside §6.13's print button.
9. **Q47 with a form in it.** Monetising the rest cue —
   warming the light to soften a sales pitch. Cure: §6.10's
   edge rule; Q47 contains a line of type and nothing to
   operate.
10. **Backstage stock-photo cosplay.** Gritty filtered photos
    of strangers' theatres, brick-wall textures, Edison bulbs.
    The wings are built from the *actual* building: its cloth,
    its marks, its book — photographed plainly or drawn as
    paperwork. Cure: imagery is the house's own (§6.4, §6.12)
    or it is an honest diagram (§6.7).

## 10. Quality gate

Blocking — all must pass before this theme ships in a build:

1. **Book reconciliation.** Corner list, running order, cue
   lines and tally totals diff-checked against §6.17's record:
   same numbers, same names, same times, sequential with no
   gaps and no duplicates. Q0 reserved and unused by real cues.
2. **Mark audit.** Every §6.5 mark's `data-stands-for` resolves
   to an element in the same scene; every §6.8 key element has
   a mark. Zero orphan tape.
3. **Blackout drill.** With rAF disabled mid-test, every
   §6.3 blackout still lifts by its 600ms hard watchdog; total
   event ≤ 200ms in normal runs; lockout verified at three
   boundaries in fast scroll.
4. **Curtain drill.** JS disabled: no curtain, hero lit.
   JS on, tab hidden during parting: watchdog settles panels.
   Focus into hero pre-scroll: instant part.
5. **Red census.** `--cue-red` / `--cue-red-lit` appear only
   in §6.2, §6.9, §6.15 components and the corner lamp.
   `--go-lit` as *signal* only in cue contexts (its §6.5 tape
   material use is the one licensed exception, listed here).
6. **No-hidden-content sweep.** With all arming scripts
   blocked, the full page — every scene, table, form — reads
   complete in order. Screenshots at load+0ms show lit content
   under every overlay state.
7. **Reduced-motion pass.** Full page with
   `prefers-reduced-motion`: no travel, no blackouts, no
   pulses, no scrub-lerp; all cues, ticks, tallies and the
   Q47 warmth present as states.
8. **Counterweight check.** §6.4: bag displacement equals
   cloth displacement at q = 0.25 / 0.5 / 0.75 / 1 (measured,
   not eyeballed); DEAD state reached exactly at scene end.
9. **Tally arithmetic.** After a scripted full scroll, RUNNING
   TIME equals the book's total and CUES reads N / N; a §6.9
   re-call changes neither.
10. **Contrast & focus.** All text pairings meet §2's measured
    ratios; every interactive element shows a visible focus
    state; the form's error flow (§6.15) completes keyboard-
    only, with focus landing on the first error.
11. **Loop census.** Exactly two ambient loops running (dust,
    armed-lamp pulse), both paused offscreen; frame budget per
    §14 verified on a mid-tier phone.


## 11. Component inventory

Every component a real site in this theme needs, with its
treatment. Components the theme refuses are listed with their
in-theme replacement — a refusal is a design decision, and it
is recorded here so a builder does not improvise one.

| Component | Treatment in From the Wings |
|---|---|
| Primary button | The cue button (§6.9 grammar): mono, lamp at right, arms red then GO green; reserved for actions that *execute* something on the page or send the form (§6.15). |
| Secondary button | A paperwork button: 1px hemp rule, mono caps, hover firms the rule to `--go-lit` pencil; no lamp — it does not call a cue, it files a request (print, download the book, add to calendar). |
| Text link | Mono, pencil underline (§6.6 draw, 160ms); visited links are struck once lightly in pencil — the book remembers where you have been. |
| Text input | §6.15's call-sheet field: paper ground, hemp rule, green rule on focus, pencil tick when valid, red ink error beneath. |
| Select | Native select in the sheet's styling — backstage uses the tool that works in gloves; options are real intents, never "Please select…" (the label above does that job). |
| Checkbox / radio | A pencil box: 16px square, 1.5px hemp border; checked = green-pencil tick drawn (240ms; appears under reduced motion). Radios are spike crosses in a circle of tape. |
| Toggle / switch | Refused. Backstage things are called or they are not; a two-state commitment is a checkbox in the book. |
| Tabs | The house tabs (§6.11): card dividers in a strip, the active pulled 6px proud with a gilt edge. In-page tab sets (access info) reuse the card stock at scene scale. |
| Accordion | The preset list: rows headed by cue lines; opening a row is a called cue (standby flash optional at builder's restraint — default: none; the row simply stands open with a pencil tick). |
| Table | The running order (§6.13): paper ground, ruled, sticky header, ticks in the cue cell. All data tables inherit it. |
| Badge / tag | A tape label: `--go-lit` at 18% ground, mono caps, stuck at a 1.5° angle (tape is never straight — the one licensed rotation in the theme, echoing §6.5's material). |
| Alert / notice | A called note: paper slip pinned at the scene's head with a lamp-less cue line ("NOTE — FROM THE BOOK:"); errors use §6.15's red ink. Nothing slides in from a corner of the world. |
| Toast | Refused as a pattern. Confirmations are printed where the action happened (§6.15's sign-off) — a stage manager does not shout from offstage; the book is annotated. |
| Modal / dialog | The DSM's call: a full blackout (§6.3 grammar at 400ms, longer because a dialog is a held show) to a single paper sheet centred — used only for genuine interruptions (age gates, access requirements). Focus trapped properly, Esc = "STAND DOWN" button, worded so. |
| Pagination | By act: "ACT I · ACT II · ACT III" links with pencil ticks on the act you are in; numbered pages are running-order rows (§6.13). Infinite scroll is refused (a call board has edges, §6.12). |
| Breadcrumbs | The cue trail: `THE BOOK › SEASON › THE WINTERING` in caption mono with pencil separators — the path is paperwork, so it is printed like it. |
| Progress bar | Refused (§9.8). Progress = §6.6's list + §6.14's tally. A determinate upload in the form uses a rope line that hauls across its cleats (the one licensed bar, drawn as rigging, with its % in mono — numbers beat metaphors). |
| Spinner | Refused. Waiting is tabs-closed (§6.16) or a printed "NOT YET CALLED". |
| Search | The book index: a mono input in the corner; results print as a cue list (each result a call — title, where it stands, its Q if it has one). No results = §6.18's scene-scale note. |
| Card | The call-board card (§6.12): paper, taped still, spike numeral, call-date strip. |
| Hero | §6.1 + §8.1: the parted tabs framing the called title. |
| Footer | §6.11's corner resolves at the page foot into the stage door: address in mono, the book's last line "THAT'S THE SHOW." (§6.6), stage-door email, and the gilt hairline closing the proscenium trace. No social icons row — the door has a bell, not a feed: one email, one phone, printed. |
| Form | §6.15 entire. |
| 404 / empty | §6.18 entire. |
| Tooltip | A pencil note: `--paper` slip, mono 12px, appears above its anchor after 500ms hover/focus, worded as an SM's aside (§12). Never on touch (tap targets carry their meaning in their labels). |
| Skip link | "SKIP TO THE FIRST CUE" — lands on the first scene heading, past the corner (§6.11). |

## 12. Content & copywriting voice

Two registers share the building. **Front of house** (Playfair)
speaks rarely and only names beauty: show titles, the season
name, the one line in Q47. Everything else is **the book**
(Space Mono): the stage manager's voice — precise, numbered,
unhurried, kind in the specific way of people who keep others
safe in the dark. The book never exclaims. The book never says
"amazing". The book says what happens, when, and who it is for.

- **Headlines (the book's scene titles, where Playfair is not
  used):** mono, sentence case, factual with one dry turn
  allowed: "The cloth is flown by hand." / "Where to stand
  when you visit." Never a pun on "stage" or "drama" — the
  building does not pun about itself.
- **Cue lines:** law format (§3): `Q13 · STANDBY`, calls in
  imperative caps from the book's record ("FLY THE CLOTH",
  "HOUSE LIGHTS — BREATHE"). A cue call is a verb phrase, never
  a noun: not "THE BACKDROP" but "FLY THE CLOTH".
- **Labels:** caption caps, mono: `RUNNING TIME`, `CUES
  CALLED`, `FROM THE BOOK`. Labels name the paperwork, not the
  marketing ("THE BOOK" not "DISCOVER MORE").
- **Buttons:** actions in the book's verbs: "STANDBY — JOIN",
  "PRINT THE RUNNING ORDER", "PUT ME ON THE CALL SHEET".
  Never "Submit", never "Click here", never "GO" alone (§9.3).
- **Error messages:** the SM correcting a call, without blame
  and with the fix: ✓ "EMAIL — THAT ADDRESS DOESN'T TAKE A
  CALL. CHECK THE SPELLING AND STAND BY AGAIN." ✗ "Invalid
  input!!" ✗ "Oops — something went wrong." The book does not
  say oops; the book says what happened.
- **Empty states:** ✓ "NOTHING PINNED FOR THOSE DATES. THE
  BOARD IS EMPTY, NOT BROKEN." (§6.12). The voice states the
  fact and the reassurance in one breath, then offers the way
  back.
- **Confirmation:** in the book's format, with its reference:
  "Q-LAST — SAMIRA IS ON THE CALL SHEET. REF W-2214." (§8.3).
- **Fixed strings (verbatim, never paraphrased):** the Q47
  line — `Q47 — House lights. Breathe.`; the cue list's
  closing line — `THAT'S THE SHOW.`; the dark stage note —
  `NO CUE CALLS THIS.`; the form's failure note — `THE DOOR
  DIDN'T ANSWER.` A build that rewrites these has changed the
  show, not the copy.

## 13. Full-page scroll choreography map

The home page, top to footer, in order. Every beat names its
cue, what the visitor sees, and what it should feel like: being
walked into a working building by someone who knows it.

1. **Arrival — the closed tabs (§6.1).** Black, folds, a gilt
   hem. *Feel:* the moment before the house opens; you are
   early, and the building knows it.
2. **First scroll — the parting (1400ms).** The tabs haul
   sideways; the title is called letter by letter; dust in the
   followspot. *Feel:* the show beginning, from the wrong —
   right — side.
3. **Q1 called & ticked.** Corner lamp settles; tally 03:00 ·
   1/52. *Feel:* someone is running this. You can relax into
   being run.
4. **The season board (§6.12).** Cards take their marks in
   blocking order; the eye learns the tape. *Feel:* the call
   board at the half-hour — everything pinned, everything
   findable.
5. **Blackout (200ms) → the backdrop scene (§6.4).** A blink
   of dark; then the cloth, the ropes, the bags. Scroll hauls
   it to DEAD. *Feel:* labour, made visible and beautiful;
   your scroll has weight in it.
6. **The company (§6.7).** Chalk draws the blocking across the
   floor; crosses pair with names. *Feel:* the show as a
   drawing before it is a dance — intelligence, backstage
   style.
7. **The running order (§6.13).** The whole book, printed.
   The visitor checks the paperwork and finds it reconciles.
   *Feel:* trust, earned in mono.
8. **Blackout (200ms) → visit paperwork.** Times, access, the
   stage-door address. Plain, ruled, complete. *Feel:* the
   building being practical on your behalf.
9. **Q47 — House lights. Breathe. (§6.10).** Warmth, one line,
   nothing to do. *Feel:* the held breath of the whole page —
   the beat the visitor will describe to someone else.
10. **The stage-door form (§6.15).** The sheet, the fields,
    the standby, the GO, the sign-off in green pencil.
    *Feel:* joining something with a door and a book, not
    subscribing to something with a funnel.
11. **The footer — the stage door.** "THAT'S THE SHOW." The
    tally at full time. *Feel:* leaving by the stage door at
    night, called by your name, into the street.

Reverse pass: scrolling up, nothing un-calls, un-ticks or
reheats — the cloth alone lowers (§6.4), because rigging is
reversible and paperwork is not. Jump scroll: cues catch up in
one pencil pass (§6.6), blackouts are skipped (the visitor has
teleported; the SM does not blackout a teleport).

## 14. Whole-page performance budget

- **Total page weight (home):** ≤ 780KB compressed, of which
  images ≤ 380KB (the cloth §6.4 ≤ 180KB; board stills ≤ 90KB
  each, lazy below the fold), fonts ≤ 120KB (Playfair Display
  600/700 + Space Mono 400/700, subset to Latin + the Q47
  line's characters), CSS ≤ 60KB, JS ≤ 55KB.
- **Frame budget:** the shared rAF loop (lerp 0.12) must hold
  60fps on a mid-tier Android (Pixel 6a class) during the
  §6.4 haul with all three layers live: transforms and opacity
  only, no layout or paint in the loop; per-frame main-thread
  budget ≤ 6ms, long tasks (>50ms) zero during scroll.
- **Animation census:** concurrent animated properties page-
  wide ≤ 14 at any moment (the haul is the peak: cloth, ropes
  ×3, bags, marks); ambient loops exactly 2 (§10.11).
- **Load:** LCP = the hero title (text, not the curtain) ≤
  2.0s on 4G; the curtain never blocks LCP measurement or
  paint of the hero beneath it. CLS = 0.00 target: every
  overlay is out-of-flow, every scene's height is reserved by
  its content (content ships in place — the theme's law is
  also its layout stability).
- **Cut order when over budget:** (1) dust loop's particle
  count halves, then the loop is cut; (2) board stills drop
  to one per row; (3) §6.4's bag stack reduces (5 → 3 → 1);
  (4) chalk displacement filter dropped (clean strokes);
  (5) curtain folds reduce (9 → 5). **Never cut:** the cue
  system, the book's printings, the blackout watchdogs, the
  form's error flow, Q47. The paperwork is the theme; the
  weather is negotiable.

## 15. Build-order checklist

1. **The book first (§6.17).** Write the cue record; pass the
   linter (sequential, timed, named). No page exists before
   its book.
2. **Static lit page.** All scenes, content complete, cue
   lines printed, tables and form working, no JS. Verify the
   §10.6 no-hidden-content sweep on this build — it is the
   fallback every later layer must preserve.
3. **Palette & type tokens (§2, §3).** Closed token list in
   CSS custom properties; grep for undeclared hex.
4. **Layout (§4):** prompt corner (fixed, then bar forms),
   floor grid, proscenium hairline, scene rhythm.
5. **The corner's printings:** cue list (§6.6 unticked state),
   tally (§6.14 static totals), house tabs (§6.11) — all
   generated from the book.
6. **Cue system (§6.2):** observer, standby/GO timers, queue,
   jump-scroll catch-up. Then §6.6 ticks and §6.14 live tally.
7. **Entrances (§6.8 + §6.5):** arming, travel vectors from
   blocking, marks and their audit attributes.
8. **Scene machinery:** blackout (§6.3) with both watchdogs;
   curtain (§6.1) with its watchdog and focus-part rule;
   haul (§6.4) with counterweight arithmetic tested at four
   q values.
9. **Q47 (§6.10)** — deliberately late: the warmth is a scoped
   token shift, added once the page's black is final.
10. **Interactive layer:** §6.9 cue buttons, §6.12 filters,
    §6.15 form ceremony + error flow, §6.16 transitions.
11. **Diagrams:** §6.7 chalk (paths ship drawn; arm the draw).
12. **Dark stage (§6.18)** and scene-scale empty states.
13. **Reduced-motion pass** across every element (each §6
    variant), then the full §10 gate, signed by a non-builder.
14. **Performance pass** against §14 on a mid-tier device;
    apply the cut order if needed — paperwork last.

