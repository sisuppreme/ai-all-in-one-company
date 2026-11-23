# Theme 14 — Broadside & Ballad (Expanded, v1 + v2 standard)

## 1. Concept & world

A Georgian street wall at dusk, and the bill-poster has just been. One sheet
of wall-worn paper, pasted over the ghosts of older sheets, carrying five
competing notices at five different scales: an enormous wood-type headline
bill for tonight's show, two side bills in Playfair, a lost-dog notice, a
meeting announcement, and — running underneath it all, in quiet Lora — the
ballad itself, the verses that were printed on the back of the sheet and
sung in the street for a penny. The site is not *decorated like* a
broadside. The site *is* the wall: sheets paste up wet, dry in the
lamplight, lift at one corner when a passer-by's attention catches them,
and peel away to the next sheet when the visitor moves on. Yesterday's
show is never fully removed — a half-torn older sheet shows at the edges
of every sheet, and that archaeology is the theme's memory.

The fiction has one law, and it is a blocking gate: **the wall only ever
shows paper that is really there.** Every animated thing is a sheet, a
notice printed on a sheet, the paste on a sheet, or the lamp above the
wall. There is no floating UI chrome, no glass, no gradient mesh, no
generic web furniture wearing a paper texture. If an element could not
have been pasted, printed, torn, or lit on a real wall in 1820, it does
not belong to this theme.

**Mood.** Loud at the top of the sheet, tender at the bottom. The shout
is Fraunces Black at 200px; the whisper is a Lora verse at 19px. The
emotional arc of every page runs shout → bills → ballad: commerce first
(that is what posters are for), story last (that is what ballads are
for).

**Best-fit sites.** Theatre companies (especially touring, folk,
fringe, and repertory), folk and traditional music acts, protest and
arts organisations, community halls, print and zine fairs, historical
societies, pub theatres, storytelling festivals. Any organisation whose
real-world ancestor actually pasted bills on walls.

**Best-fit audiences.** Visitors who respond to print craft and
vernacular typography; audiences for live performance, who read a
poster the way they read a playbill — headline, date, price, then the
small print for love.

**When NOT to use it.** SaaS, fintech, dashboards, anything whose
content is dense tabular data (the wall has no table manners — see §11
for the ledger exception and its limits); luxury minimalism (this theme
is maximal by law — five notices compete, always); sites needing a true
dark-mode product UI (the wall has a lamplight ruling instead, §2);
any brand whose voice cannot tolerate a torn edge. If the client asks
for "clean", this is the wrong wall.

**The one test.** Print the page's hero on paper, paste it to a wall,
photograph it at dusk. If it looks wrong, the build is wrong — no
matter how well the code behaves.

## 2. Palette

Four inks, one wall. The four anchor colours are the sheet's; the wall
tokens exist only outside the sheets and never appear on paper.

| Token | Hex | Role | Ratio on a sheet | Pairing / contrast |
|---|---|---|---|---|
| `--paper` | `#E9DFC8` | The sheet itself; page ground inside every broadside | 62% of sheet area | Ground for `--ink` (12.6:1), `--red` (5.8:1), `--ink-soft` (8.9:1) |
| `--lampblack` | `#1C1A17` | Wood-type headlines, notice text, rules, woodcut ink | 24% | On `--paper` 12.6:1; on `--paper-light` 13.4:1; paper text on a black bill reverses at 12.6:1 |
| `--red` | `#A52A1D` | Poster red: the main bill's shout word, prices, the NEW and LAST NIGHT flags, seal of the printer | 9% | On `--paper` 5.8:1 — passes AA for text ≥14px and all display; never set red body text under 14px |
| `--ochre` | `#C88A2D` | Ochre: secondary bill accents, the paste-brush stroke's dry edge, woodcut second colour, date blocks | 5% | On `--paper` 2.4:1 — **never text on paper**; on `--lampblack` 5.1:1 — display ≥24px only, on black bills |

**Derived tokens** (labelled derived; shades and states of the anchors,
plus the wall):

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--paper-light` | `#F5EEDA` | Paper toward the lamp; hero sheet's lit zone, skeleton paste rectangles before bills land |
| `--paper-deep` | `#D8C9A4` | Paper in shadow and the half-torn older sheet beneath every corner-peek — yesterday's show is always this colour |
| `--ink-soft` | `#45403A` | Lampblack at reading distance: verse text, notice body, captions (8.9:1 on `--paper`) |
| `--red-deep` | `#7C1E13` | Poster red in shadow / hover-pressed state; error ink on forms (8.1:1 on `--paper`) |
| `--ochre-pale` | `#E2B76E` | Ochre lit by the lamp; the wet end of the paste-brush stroke, woodcut highlights |
| `--sheen` | `rgba(255, 251, 238, 0.55)` | Wet paste gloss; exists only as an animated layer, never a static fill |
| `--wall` | `#6E5B47` | Brick at the wall's edge, visible outside sheets; **never on a sheet** |
| `--wall-mortar` | `#99876C` | Mortar lines and the torn-sheet shadow gap; **never on a sheet** |

**Usage law.** Every sheet is paper-first: if a screenshot of a sheet is
more than ~15% red and ochre combined, the bill-poster has shouted over
himself — rebalance to paper and black. Red is rationed to one shout
word, prices, and flags per sheet. Ochre never carries words on paper.

**Dark-mode behaviour — the lamplight ruling.** There is no inverted
wall. Under `prefers-color-scheme: dark`, the wall is the same wall
after dark: `--paper` takes the lamp's amber cast (`#DFD0A6` as lit,
implemented as a warm gradient overlay at 8% over the sheet, never a
token swap, so print contrast is unchanged), `--wall` deepens to
`#4A3D2E`, and the street-lamp light shift (§6.10) becomes the primary
light source instead of an ambient accent. Ink contrast on paper is
preserved by construction — the paper dims, the ink does not lighten.
Products that require a true dark UI are directed away in §1.

## 3. Typography

Three faces, three jobs, no substitutions. **Fraunces** (Black 900, and
600 for numerals) is the wood type — cut big, set tight, never letterspaced
out. **Playfair Display** (700, with italic) is the genteel secondary bill —
the respectable theatre announcing itself in a finer hand. **Lora** (400,
500, italic) is the ballad and the small print — the reading voice of the
sheet.

| Role | Face / weight | Size | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Shout (main bill headline) | Fraunces 900 | clamp(72px, 13.5vw, 216px) | 0.92 | −0.02em | All caps or title case as the bill demands; one shout per sheet; the shout word (§6.6) may take `--red` |
| Bill head (secondary bills) | Playfair Display 700 | clamp(30px, 4.2vw, 54px) | 1.02 | −0.01em | Italic for the ballad-opera title inside a bill; never all caps above 40px |
| Notice head | Fraunces 600 | 20–26px | 1.1 | 0 | The lost-dog and meeting notices; small wood type, still wood type |
| Verse | Lora 400 | 19px (17px <768px) | 1.75 | 0 | Measure 34–42ch, centred on the sheet's lower half; stanza breaks are whitespace, never rules |
| Notice body | Lora 400 | 16.5px | 1.6 | 0 | `--ink-soft`; the small print of each bill |
| Price & figures | Fraunces 600 | 28–44px | 1 | 0 | Wood-type numerals; `font-variant-numeric: tabular-nums` OFF — wood type is not tabular, and counters (§5) roll through real glyph widths |
| Apparatus (dates, "sheet n of N", imprint) | Lora 500, uppercase | 11.5px | 1.4 | 0.18em | The sheet's paperwork: datelines, sheet counts, the printer's imprint |
| Caption (under woodcuts) | Lora italic | 14px | 1.45 | 0 | Names the portrait's character, never describes the image |

**Type laws.**

1. **Five scales compete, always.** A sheet with one headline and tidy
   subheads is a webpage, not a broadside. Every sheet carries the shout,
   two bill heads, and at least two notice-scale texts at visibly
   different sizes (§6.5 posts them; §4 places them).
2. **Wood type is never letterspaced.** Tracking on Fraunces 900 display
   is −0.02em to 0. Air between wood letters reads as a font bug, not
   as posters.
3. **Verses are never justified, never hyphenated, never set in a
   colour below 8.9:1.** The ballad is the sheet's conscience; it gets
   the most comfortable reading conditions on the page.
4. **No webfont swap-in.** If Fraunces fails to load, headlines fall to
   the serif stack and the paste-up (§6.1) waits for `document.fonts.ready`
   up to the 1000ms watchdog — a shout in the wrong face is worse than a
   shout 300ms late.

## 4. Layout language

**The wall.** The page is a brick wall seen straight on. Sheets are
centred on a wall field of `--wall` / `--wall-mortar` that shows only at
the edges: 24–72px of wall at the viewport sides on desktop, 10–16px on
mobile — enough to establish that the paper hangs on something older
than itself. At the sheets' edges, half-torn older sheets (in
`--paper-deep`) protrude 6–20px at two or three corners per sheet,
rotated, their own torn edges drawn — the wall's archaeology is part of
the layout grid, not a background image.

**Sheet geometry.** A sheet is a rectangle of `--paper`, max-width
1180px, min-height 92vh for bill sheets (the shout must own a full
screen), auto height for verse sheets. Sheets stack vertically with a
**negative overlap** of 40–90px: the next sheet's top edge pastes *over*
the previous sheet's bottom edge, exactly as a poster goes over the
last poster's tail. The torn-edge divider (§6.8) lives in that overlap.

**Rotation law.** Sheets and notices sit at fixed, deterministic
rotations — pasted by a human, not scattered by a random function:

| Element | Rotation | Note |
|---|---|---|
| Sheet 1 (hero) | −0.4° | The poster tried hardest on the first sheet |
| Sheet 2 | +0.7° | |
| Sheet 3 | −0.9° | |
| Sheet 4 | +0.5° | |
| Sheet 5+ | alternates −0.6° / +0.8° | |
| Main bill within sheet | 0° (set true) | The shout is always level; only its sheet leans |
| Side bills | −1.6° and +1.3° | Opposing leans, like two posters arguing |
| Small notices | −2.2° to +2.0°, fixed per position | The lost dog always leans left (−2.2°); regulars learn the wall |

Rotations are tokenised (`--lean-sheet`, `--lean-bill-a`, `--lean-bill-b`,
`--lean-notice`) and identical on every load. Random rotation is
slop (§9).

**The wall grid.** Under the apparent chaos, notices sit on a 12-column
grid inside the sheet with 28px gutters: shout spans 12, side bills span
5 and 4 with a 3-column gutter of bare paper between them, notices take
3–4 columns in the sheet's lower third, the verse stream (§6.18) takes a
centred 6-column measure. Bare paper is a layout material: every sheet
keeps ≥18% of its area unprinted — paste needs somewhere to show.

**Pinning geography.** The headline bill pins at the wall top *within
its sheet's zone* (§6.14, §6.18): as the visitor scrolls a verse sheet,
the bill stays at the top of the viewport like the top of the poster
still showing above the verses pasted beneath it. Pinning never crosses
a sheet boundary — when the sheet ends, its bill peels with it (§6.2).

**Spacing rhythm.** Base unit 8px. Sheet padding: 56px top, 48px sides,
72px bottom on desktop (the bottom margin is where the bill-poster's
hand steadied the sheet — it carries the imprint, §6.17). Verse stanza
gap 32px. Notice internal padding 20–28px. Nothing on a sheet is spaced
in multiples of anything but 8 and the stanza's 32.

## 5. Full motion system

All motion on the wall is one of four physical events: **pasting**
(something wet arrives), **drying** (sheen leaves, ink settles),
**peeling** (paper leaves), and **lamplight** (time passes). If a
proposed animation is none of these, it is not this theme's motion.

**Named easings.**

| Token | Curve | Used by |
|---|---|---|
| `--ease-squeegee` | `cubic-bezier(.25,.8,.25,1)` | Band sweeps, brush stroke, torn-edge draw — a hand pulling steadily |
| `--ease-peel` | `cubic-bezier(.55,.06,.35,1)` | Corner lift and peel — slow to start (the paste resists), then gone |
| `--ease-slap` | `cubic-bezier(.3,1.4,.5,1)` | Paste slaps and wood-type drop — overshoot ≤1.04, scale only, never on text blocks |
| `--ease-settle` | `cubic-bezier(.2,.7,.3,1)` | Ink settling, notice arrivals, tilts returning |
| `--ease-drift` | `cubic-bezier(.45,0,.55,1)` | The lamp loop; slow in, slow out, 14s |

**Duration tokens.** `--dur-slap: 110ms` · `--dur-band: 450ms` ·
`--dur-peel: 600ms` · `--dur-drop: 300ms` · `--dur-draw: 500ms` ·
`--dur-tilt: 240ms` · `--dur-strip: 500ms` · `--dur-dry: 2000ms` ·
`--dur-fallback: 1000ms` (the watchdog, law 2).

**The vocabulary, translated.** Every required motion term, in wall
language:

| Motion term | Broadside & Ballad form | Spec |
|---|---|---|
| Scroll-triggered reveals | Notices slap in as their sheet arrives (§6.5); woodcuts settle (§6.9) | IO at 20% sheet visibility; stagger 130ms in bill-poster order |
| Parallax | The wall (brick edges, older torn sheets) drifts at 0.92× behind the sheets at 1.0×; the pinned bill at 1.0× against verses at 1.0× — depth comes from the wall layer only | Single rAF loop, lerp 0.12; wall offset capped ±18px so brick never slides out from behind a sheet edge |
| Pinned scenes | The headline bill pins at the wall top while its sheet's verses scroll beneath (§6.18) | `position: sticky` inside the sheet zone; pin releases at sheet end, bill peels with its sheet |
| Masked line reveals | Squeegee bands: each band of the hero reveals through a horizontal clip-path sweep (§6.1); notice headlines reveal through their own paste band on later sheets | clip-path inset animated top→bottom of band, 450ms `--ease-squeegee` |
| Blur-to-sharp | Wet-ink settle on woodcut portraits only: blur 2px→0 as ink "dries" (§6.9). **Text never blurs** — wood type was carved sharp and stays sharp | 600ms, paired with scale 1.08→1 |
| Animated counters | Admission prices and crowd figures count up in Fraunces 600 wood numerals when a bill's data line enters (§6.15) | 900ms, stepped in 12 frames (wood type lands in sorts, not in a smooth tween); final value always in the DOM |
| Progress indicators | The paste-brush stroke down the left wall edge + "sheet n of N" (§6.7) | Scrubbed to total scroll, lerp 0.12; the counter text updates at sheet boundaries only |
| Marquees | The ballad refrain band: one line of the ballad, lettered as a bill, drifts horizontally across the sheet foot at 28px/s on sheets that carry a refrain (§6.18) | Pauses on hover/focus-within; hidden <768px (the sheet foot is too narrow to sing across) |
| Ambient loops | Street-lamp light shift (±6° gradient drift, 14s) and wall dust in the hero's lamplight (§6.10) | Runs only while the hero sheet is in view; dust ≤14 motes |
| Micro-interactions | Paste-slap click (§6.11); proof-style underline draw on text links (120ms `--ease-settle`) | Feedback is always the paper's own behaviour |
| Hover physics | Corner-peek lift (§6.3) and loose-paper tilt 1–2° (§6.11) | Spring via the shared loop (stiffness 0.18, damping 0.72) — paper overshoots a breath, then rests |
| Page transitions | Wall-strip: the whole wall peels downward in one 500ms strip to the next wall (§6.12) | Top sheet only animates; destination wall is rendered beneath before the strip begins |
| Image treatments | Woodcut portraits scale-in-frame with ink settle (§6.9); all imagery is duotone woodcut-style (lampblack + one colour), never photographic colour | Duotone via CSS filter chain + mix-blend on a paper-tinted layer; originals untouched |

**Global motion laws.**

1. **The sheet beneath is always whole.** Every peel, strip, and peek
   reveals a fully rendered sheet or notice — never a void, never a
   spinner wearing paper.
2. **The 1000ms promise.** A watchdog completes any paste, peel, or
   reveal that has not finished within 1000ms of its trigger (fonts
   late, IO missed, tab inactive). No content may remain hidden,
   clipped, or mid-peel past that line.
3. **Drying is one-way.** Once a sheet is dry (§6.4), it never gets wet
   again this session. Scrolling back up shows dry sheets, instantly,
   exactly as left. Peels do not reverse into re-pastes; the returning
   sheet is simply *there*, the way a wall is there when you walk back.
4. **One loop.** Every scrubbed or spring value (drying, parallax,
   brush stroke, lamp, tilts, peeks) is written by a single
   requestAnimationFrame loop with lerp 0.12. No element owns a timer
   for a scroll-linked value.
5. **The shout never waits.** The hero's shout word is visible in the
   first band's first 450ms or, if anything fails, by the watchdog —
   a poster that cannot be read from across the street has failed its
   only job.

## 6. Signature elements

Eighteen elements: the theme's twelve signatures (§6.1–§6.12) and six
page-family elements (§6.13–§6.18). Every element carries its full build
spec plus the v2 layers — choreography timeline, state matrix, breakpoint
behaviour, edge cases, accessibility spec, and the tokens it consumes.
Timelines are milliseconds from the element's trigger unless stated.

### 6.1 Three-stroke paste-up

**What & why.** The hero sheet arrives the way a bill-poster posts it:
three horizontal bands — top, middle, bottom — each swept down by an
invisible squeegee, the paper wet and shining, then drying over the next
two seconds. It belongs because the page load *is* the posting; a visitor
who watches the hero go up understands the whole theme before reading a
word.

**Structure.** The hero `.sheet` is divided into three `.band` regions
(38% / 34% / 28% of sheet height — the poster's reach, not equal thirds).
Each band's content is normal DOM, present from first paint, clipped by
an animated `clip-path: inset()` on the band wrapper. A `.sheen` layer
(linear-gradient, `--sheen` at 0.55 opacity) sits over each band,
`pointer-events: none`, `aria-hidden`. The shout (§6.6) lives in band 1;
no band may contain a notice that straddles a band boundary (build-time
rule, §15).

**Motion spec.** Trigger: load, gated on `document.fonts.ready` or the
1000ms watchdog, whichever first. Per band: clip-path inset sweeps from
`inset(0 0 100% 0)` to `inset(0 0 0% 0)`, 450ms `--ease-squeegee`;
bands stagger 200ms (band 2 starts as band 1's squeegee is 55% down).
Sheen peaks at each band's reveal and fades to 0 over `--dur-dry`
(2000ms) from that band's start.

**Choreography timeline (v2).**
- t=0 — Fonts ready (or watchdog). Band 1 begins; shout band.
- t=0–450 — Band 1 sweeps down; sheen at full gloss.
- t=200–650 — Band 2 sweeps (stagger 200ms).
- t=400–850 — Band 3 sweeps; the sheet is fully posted at t=850.
- t=850–2000 — Sheen dries band by band; at t=2000 the hero is a dry
  poster and §6.4's scrub takes over the *next* sheets' sheen.
- t=2000 — `.is-posted` set on the sheet; paste-up can never replay.

**State matrix (v2).**

| State | Bands | Sheen | Content | Notes |
|---|---|---|---|---|
| Pre-post (first paint) | Clipped to 0 height | 0 | In DOM, readable by AT/SEO | Lasts <100ms in practice; no-JS skips straight to Posted |
| Posting | Sweeping in sequence | Peaking per band | Revealed band by band | Total 850ms, inside the 1000ms promise |
| Posted / dry (rest) | Fully open | 0 | Fully visible | The permanent state |
| Scrolled-past | Open | 0 | Fully visible | Never re-posts (law 3) |
| Hover/focus-within | Open | 0 | Unchanged | Paste-up ignores pointers entirely |
| Disabled | n/a — the hero sheet is not a control | — | — | — |

**Breakpoint behaviour (v2).** ≥1200px: as specced, three bands.
768–1199px: three bands, stagger 160ms. <768px: **two bands** (55/45) —
a phone screen is one arm's reach, and three sweeps read as a loading
stutter; stagger 140ms, total ≤640ms.

**Edge cases (v2).** Fonts slow: watchdog starts the paste-up at 1000ms
in the fallback serif rather than holding the wall blank (law 5 yields
to law 2 at the line). Tab hidden mid-paste: rAF pauses; on return, the
watchdog completes all bands instantly. Reduced data / save-data: sheen
layer omitted, bands still sweep. Very tall hero (>120vh of content):
bands divide the *sheet*, not the viewport — the third band may start
below the fold and simply be posted when scrolled to.

**Accessibility (v2).** Bands are visual clipping only; the DOM is
complete and in order from first paint, so screen readers never meet a
half-posted sheet. The clip animation is not announced. Focus landing
inside an unposted band forces that band open instantly. Contrast is
final-state contrast at every moment — the sheen is a light overlay
*above* print but below reading contrast thresholds (sheen over text
zones is capped at 0.35 opacity so ink never drops under 7:1 mid-dry).

**Content merge.** The bands are the sheet arriving; remove the sheet's
content and there is nothing to paste. The animation is the page's own
delivery mechanism, not an intro played over it.

**Failure fallback.** JS off, IO/clip-path unsupported, or watchdog
tripped: all bands at `inset(0)`, sheen absent. The hero reads as a
finished, dry poster.

**Reduced motion.** No sweep, no sheen: the sheet is simply posted and
dry at first paint.

**Performance & mobile variant.** Three clip-path animations on
composited wrappers; zero layout work after first paint. Budget: ≤1ms
script (one class add). Mobile variant is the two-band spec above.

**Tokens.** `--dur-band`, `--dur-dry`, `--dur-fallback`,
`--ease-squeegee`, `--sheen`, `--paper`.

### 6.2 Corner-lift peel transitions

**What & why.** Moving from sheet to sheet, the current broadside's
bottom corner lifts — the paste gives, the corner curls — and the whole
sheet peels away downward, revealing the next sheet already pasted
beneath. It belongs because leaving a poster *is* a physical act on a
wall, and because the reveal teaches the theme's archaeology: there is
always another sheet under this one.

**Structure.** Sheets are stacked in normal document flow; the peel is a
transform on the outgoing sheet only. The outgoing `.sheet` gets
`transform-origin: 100% 100%` (bottom-right corner — the corner a hand
would take) and a two-part animation: corner lift (a `::after` curl
shadow + skew on the sheet's corner zone) then the peel proper
(`rotateX` on a `perspective` parent is forbidden — it distorts type;
the peel is `translateY` + `rotate(1.5deg)` + a moving clip, reading as
paper sliding down off its paste). The incoming sheet beneath is fully
rendered at all times (law 1) — it is revealed, never loaded.

**Motion spec.** Trigger: the outgoing sheet's bottom edge crosses 35%
of viewport height on downward scroll, once per sheet per session.
Corner lift: 180ms `--ease-peel` (corner zone skews 0→−4deg, curl
shadow grows). Peel: 600ms `--ease-peel`, sheet translates down 104% of
its height while its top edge clips away progressively, so it reads as
peeling off the wall rather than sliding like a drawer. After the peel,
the outgoing sheet is `visibility: hidden` in place (it keeps its
layout height as the wall's "ghost" only in the verse-stream context,
§6.18; in plain sheet flow the next sheet simply occupies the view —
see Edge cases for the flow ruling).

**Choreography timeline (v2).**
- t=0 — Boundary trigger fires.
- t=0–180 — Corner lift: the bottom-right corner curls, shadow deepens,
  a 24px triangle of the sheet beneath (`--paper-deep` older sheet
  first, then the true next sheet) shows.
- t=180–780 — Peel: the sheet gives way downward, `--ease-peel`
  accelerating; the next sheet's top band is readable from t≈420.
- t=780 — Outgoing sheet hidden; `.is-peeled` set. Total 780ms, inside
  the 1000ms promise.

**State matrix (v2).**

| State | Outgoing sheet | Incoming sheet | Notes |
|---|---|---|---|
| Rest (reading) | Pasted, dry | Pasted beneath, top edge visible in the overlap | Normal wall |
| Corner lifted | Corner curled, shadow grown | 24px triangle visible | Reversible: scroll back above the trigger and the corner settles in 180ms |
| Peeling | Translating/clipping away | Revealed progressively | Pointer events off the outgoing sheet from t=0 |
| Peeled (scrolled-past) | Hidden in place | Fully in view | Never re-pastes on scroll-up (law 3) — scrolling up shows the incoming sheet's own top, and the peeled sheet returns only via a fresh page state |
| Focus-within outgoing sheet | Peel **refused** | — | If focus is inside the outgoing sheet, the peel waits until focus leaves; the wall never pulls paper from under a reader |
| Disabled | n/a | — | — |

**Breakpoint behaviour (v2).** ≥1200px: full peel as specced.
768–1199px: peel 520ms, corner triangle 18px. <768px: peel becomes a
**tear-off**: the sheet translates down in 380ms with the torn-edge
divider (§6.8) as its leading edge — small screens get the ruder,
faster removal a phone's thumb expects; corner lift is cut (no room
for the gesture to read).

**Edge cases (v2).** Fast scroll through two boundaries: peels queue —
the second sheet's peel starts only after the first completes or is
watchdog-completed; if the visitor is already two sheets past, both
peels resolve instantly (catch-up rule). Keyboard/page-down jumps: any
sheet >50% past its boundary is peeled instantly, no animation.
Scrolling back up mid-peel: the peel finishes (paper does not un-fall);
the corner-lift stage alone is reversible. Print stylesheet: all sheets
pasted, none hidden.

**Accessibility (v2).** The peel is decorative sequencing: DOM order is
document order at all times, and the incoming sheet's heading is
reachable by heading navigation before, during, and after the peel.
Focus is never moved by the peel. A `prefers-reduced-motion` visitor
never sees a peel (below). Screen-reader users meet two ordinary
sections; nothing is announced.

**Content merge.** The peel removes the poster you are leaving and
uncovers the one you are entering — the transition *is* the wall's
stack, not a wipe laid over unrelated content.

**Failure fallback.** JS off or watchdog: outgoing sheet stays pasted;
sheets simply follow one another in flow with the torn-edge divider
between them. Nothing hides.

**Reduced motion.** No lift, no peel. Sheets stack in flow; the
torn-edge divider (§6.8) alone marks the boundary.

**Performance & mobile variant.** One transform + clip on one element;
the incoming sheet must already be rendered (it is — law 1), so the
peel costs no paint of new content. Budget: compositor only, 0ms
script beyond class toggles. Mobile variant is the tear-off above.

**Tokens.** `--dur-peel`, `--ease-peel`, `--paper-deep`, `--dur-fallback`.

### 6.3 Hover corner-peek

**What & why.** The theme's signature gesture. Hovering any poster —
the main bill, a side bill, a notice card — lifts its nearest corner
12–18px, and underneath is not a tooltip or a shadow: it is the older,
half-torn sheet, yesterday's show, always the same fragment of the same
forgotten bill. It belongs because it makes the wall's archaeology
touchable, and because the peek rewards curiosity with story, not chrome.

**Structure.** Each `.bill` and `.notice` carries a `.beneath` layer as
its last child: an absolutely positioned fragment of the older sheet
(`--paper-deep`, torn-edge clip-path on its two outer edges, a fixed
fragment of Fraunces headline — "…THEATRE ROY…" and half a date —
identical under every poster on the page; it is one specific yesterday,
not a texture). The bill itself has `transform-origin` set to the
corner *opposite* the lifted one; the lift is a rotate (0→−1.1deg) +
translate along the corner diagonal, driven by the shared loop's spring
(stiffness 0.18, damping 0.72), with a soft contact shadow growing under
the lifted corner.

**Motion spec.** Trigger: pointerenter / focus-within on the bill.
Corner rises over ~240ms with the spring's slight overshoot (the corner
passes its rest lift by ~2px at t≈170 and settles). The `.beneath`
fragment is revealed progressively by the lift geometry — no separate
animation; what you see is what the corner uncovers. On leave, the
corner settles back over 200ms `--ease-settle`.

**Choreography timeline (v2).**
- t=0 — Pointer enters (or focus lands within) the bill.
- t=0–170 — Corner lifts, spring overshooting to ~19px at the diagonal.
- t=170–240 — Settle to 16px lift; the older fragment fully readable in
  the gap: headline fragment, half a date, one torn edge.
- Hold — As long as hover/focus lasts; the fragment does not animate,
  loop, or plead. It is old paper. It waits.
- Leave — t=0–200 settle back to flat; fragment covered again.

**State matrix (v2).**

| State | Corner | Beneath fragment | Notes |
|---|---|---|---|
| Rest | Flat, pasted | Covered | The bill as posted |
| Hover (desktop) | Lifted 16px, spring-settled | Revealed in the corner gap | Pointer anywhere on the bill |
| Focus-within | Lifted 16px | Revealed | Keyboard users get the same peek — non-negotiable |
| Active (press) | Lift reduces to 6px — the hand presses the bill back down | Partially covered | Pairs with §6.11's slap on click |
| Scrolled-past | Flat | Covered | Peeks do not run off-screen |
| Touch | First tap lifts (and does not navigate); second tap activates | Revealed on first tap | See Breakpoints |
| Disabled bill (e.g. sold-out notice) | Lifts 8px only — the paste is old, the corner barely gives | Half-revealed | The one dimmed variant; still peeks |

**Breakpoint behaviour (v2).** ≥1200px: lift 16–18px as specced.
768–1199px: lift 12px. <768px: hover does not exist — the peek is
tap-driven (first tap lifts 12px, second tap follows the link), and
cards in a list get a persistent 6px corner lift on the *first* card
only, as a standing hint that corners lift here.

**Edge cases (v2).** Pointer skims across a grid of notices: a 60ms
intent delay before lifting, so a diagonal mouse path doesn't flutter
six corners; leaving within the delay cancels cleanly. Two bills
overlapping (sheet overlap zone): only the topmost bill peeks. Long
press on touch = peek holds; scroll from a lifted card cancels the
lift at scroll start (the corner must never drag across text). If the
`.beneath` fragment fails to render (CSS clip-path unsupported), the
lift still runs and reveals plain `--paper-deep` — a blank old sheet
is still a correct peek.

**Accessibility (v2).** The `.beneath` fragment is `aria-hidden` (it is
a visual story; its text is a fragment, meaningless to announce), and
the bill's own link/label is fully named without it. Focus-within
triggering gives keyboard parity. The lift never moves the bill's
focusable content by more than the corner geometry — the bill's box
does not resize, so focus outlines stay put. Touch target: the whole
bill, ≥44px in both dimensions by construction (smallest notice is
≥148px wide).

**Content merge.** The peek reveals *content* — the previous show's
bill — that exists only because this wall has a past. Remove the wall's
story and the gesture has nothing to show; it is not a hover effect
applied to a card, it is the card's own underside.

**Failure fallback.** JS off: bills are flat, the `.beneath` layer
sits covered and inert. Nothing is hidden that wasn't a bonus.

**Reduced motion.** The corner lifts instantly to 10px on hover/focus
(no spring, no overshoot) — the information (there is an older sheet)
survives; the paper physics rests.

**Performance & mobile variant.** One transform per bill, driven by the
shared loop; at most one bill lifts at a time. `.beneath` layers are
static, pre-rendered, `content-visibility: auto` off-screen. Mobile
variant is the tap spec above.

**Tokens.** `--paper-deep`, `--dur-tilt`, `--ease-settle`,
`--lean-notice`.

### 6.4 Paste-drying scrub

**What & why.** A freshly pasted sheet shines. As the visitor scrolls
the first 30vh of a sheet's life, its wet sheen fades from gloss 0.5 to
0 — the sheet *ages into the wall* under the visitor's own hand. It
belongs because it gives scrolling a material consequence: you are not
moving a camera, you are giving the paste time to dry.

**Structure.** Each non-hero `.sheet` carries a `.sheen` overlay
(same construction as §6.1: `--sheen` gradient, `pointer-events: none`,
`aria-hidden`) whose opacity is a scrubbed value written by the shared
rAF loop (law 4): opacity = 0.5 × (1 − clamp(scrollProgressInSheet /
0.30)). The hero sheet's sheen is governed by §6.1's timed dry instead;
after its 2s, it joins the same end state (0) and never returns.

**Motion spec.** Trigger: continuous scroll. Range: the sheet's first
30vh of travel through the viewport. The value is lerped (0.12) so a
fast flick doesn't strobe the gloss. At progress ≥0.30 the loop writes
0 once and stops tracking that sheet (`.is-dry`).

**Choreography timeline (v2).** Scrubbed, so the timeline is a map, not
a clock:
- Sheet enters (0% of its first 30vh): gloss 0.5 — visibly wet, lamp
  catching the paste.
- 15vh scrolled: gloss ≈0.25 — drying unevenly is forbidden; the fade
  is uniform because the squeegee was even.
- 30vh scrolled: gloss 0 — dry. The sheet is now wall, not news.
- Any later scroll position, either direction: gloss stays 0 (law 3).

**State matrix (v2).**

| State | Sheen opacity | Notes |
|---|---|---|
| Fresh (sheet arriving) | 0.5 | Only within the first 30vh window |
| Drying (scrolling) | 0.5→0, lerped | Follows the visitor's hand, both directions *within* the window — scrolling up inside the window re-wets visually toward the mapped value, but once `.is-dry` is set the map is closed |
| Dry (rest, ≥30vh) | 0 | Permanent for the session |
| Scrolled-past | 0 | — |
| Hover/focus | Unchanged | Drying ignores pointers |
| Disabled | n/a | — |

**Breakpoint behaviour (v2).** ≥1200px: window 30vh, peak 0.5.
768–1199px: window 26vh, peak 0.45. <768px: window 20vh, peak 0.4 —
mobile scroll is fast; a long wet phase would mean most sheets are
only ever seen glossy, which inverts the fiction.

**Edge cases (v2).** Sheet shorter than 30vh (a verse sheet can be):
the window is min(30vh, 60% of sheet height) so drying always completes
inside its own sheet. Jump scroll (anchor link into sheet 4): all
earlier sheets are `.is-dry` on arrival — you never land on a wet wall
halfway down the page. Print: sheen absent. If the rAF loop is throttled
(background tab), the value snaps to the mapped value on return — no
catch-up animation.

**Accessibility (v2).** The sheen sits above the paper but its peak
opacity over text zones is capped (0.35 over text, 0.5 only over bare
paper and image zones — build-time zoning, §15) so ink contrast never
falls below 7:1 at any scroll position. The effect is invisible to
assistive tech (`aria-hidden`, no live regions).

**Content merge.** The drying happens on the sheet's own surface and
tracks the sheet's own content passing; it is the paste of *this*
poster drying, not a gloss laid over the page.

**Failure fallback.** JS off: no sheen element is ever shown (it is
injected/armed by JS); sheets read dry. A wall of dry posters is the
correct failure.

**Reduced motion.** Sheen never appears; sheets are dry at first paint.

**Performance & mobile variant.** One opacity write per visible wet
sheet per frame, inside the shared loop; sheets leave the loop's watch
list when dry. Mobile variant is the breakpoint spec above.

**Tokens.** `--sheen`, `--dur-dry` (hero only), `--paper`.

### 6.5 Five competing notices stagger

**What & why.** A broadside is five notices fighting for the wall: the
main bill, two side bills, a lost-dog notice, a meeting announcement.
When a sheet arrives, they slap in **in the order a bill-poster works**
— main bill first (it pays), then the side bills, then the small
notices in the gaps — each with a tiny paste-slap. It belongs because
the stagger *is* the sheet's information hierarchy, performed: size and
order tell you what matters before you read anything.

**Structure.** The sheet's five `.bill` / `.notice` children carry
`data-post="1..5"` in bill-poster order (1 = main bill, 2–3 = side
bills, 4–5 = small notices). A single IO on the sheet adds `.is-posting`,
and CSS transitions keyed to `data-post` run the stagger — no per-notice
JS timers. Each notice starts (only when JS is armed, via a `.js` class
on the root) at scale 1.04, translateY −6px, opacity 0 — and the base
(no-JS) state is fully posted (see Fallback).

**Motion spec.** Trigger: sheet 20% visible. Per notice: scale
1.04→1, translateY −6px→0, opacity 0→1, 260ms `--ease-slap`, stagger
130ms by `data-post`. Total ceremony: 260 + 4×130 = 780ms, inside the
1000ms promise. The main bill's shout word gets §6.6's drop on top of
its slap (they are timed to land together: the word drops as its bill
slaps).

**Choreography timeline (v2).**
- t=0 — Sheet 20% visible; `.is-posting`.
- t=0–260 — Main bill slaps in; §6.6's wood-type drop rides it.
- t=130–390 — Side bill A (the −1.6° lean).
- t=260–520 — Side bill B (the +1.3° lean).
- t=390–650 — Lost-dog notice (always `data-post="4"`, always leaning
  −2.2° — regulars learn where the dog lives).
- t=520–780 — Meeting announcement; sheet fully posted, `.is-posted`.

**State matrix (v2).**

| State | Notices | Notes |
|---|---|---|
| Below fold (JS armed) | Held at slap-start (scale 1.04, opacity 0) | Only within the pre-trigger zone; watchdog frees them at 1000ms past first visibility regardless |
| Posting | Slapping in, 130ms stagger | Order is law: never alphabetical, never DOM-random |
| Posted (rest) | Flat, at their fixed leans (§4) | The permanent state |
| Scrolled-past | Posted | Never re-posts (law 3) |
| Hover/focus-within | Posted; the hovered notice may peek (§6.3) / tilt (§6.11) | Posting always completes before peek can engage |
| Disabled notice (e.g. a cancelled meeting) | Posts like the others, then its flag is struck through in `--red-deep` | The wall shows cancellations; it doesn't hide them |

**Breakpoint behaviour (v2).** ≥1200px: stagger 130ms as specced.
768–1199px: stagger 100ms (the wall is narrower, the poster works
faster). <768px: stagger 70ms and the slap scale shrinks to 1.02 —
five notices stack in one column on mobile (§4 grid collapses), and a
full ceremony per sheet would tax a thumb-scroll; total ≤540ms.

**Edge cases (v2).** A sheet with fewer than five notices (a verse
sheet carries two): the stagger runs for what exists; `data-post`
values still encode the poster's order, gaps allowed. A sheet with a
sixth notice (a handbill tucked at the foot): it posts with the fifth
(+0ms offset) — late bills share the last slap. Fast scroll: catch-up
compression — notices already >50% past centre post instantly.
Content longer than its notice box: the notice grows; the slap is a
transform and does not care — but a notice that grows past its grid
span is a build error, caught by the §10 gate, not by this element.

**Accessibility (v2).** DOM order is reading order (main bill, bills,
notices) and matches the visual posting order, so the ceremony and the
screen-reader order tell the same story. The stagger is never announced.
Focus entering an unposted notice posts it instantly. All notice text
meets §2 contrast at rest; mid-slap opacity is a 260ms transition, not
a reading state.

**Content merge.** The notices are the sheet's content and the stagger
is their posting order — remove the notices and there is no animation
left, which is the test.

**Failure fallback.** The pre-slap state exists only under a JS-armed
root class. No JS → every notice is posted and readable from first
paint. IO unsupported → `.is-posted` ships in the class list.

**Reduced motion.** All five appear at once, posted and dry. Order is
kept in the DOM; only the slaps rest.

**Performance & mobile variant.** Five composited transforms per sheet,
CSS-driven from one class; zero per-notice JS. Sheets off-screen hold
no will-change. Mobile variant is the breakpoint spec above.

**Tokens.** `--dur-slap` (family), `--ease-slap`, `--lean-bill-a`,
`--lean-bill-b`, `--lean-notice`.

### 6.6 Wood-type drop

**What & why.** The biggest word on the sheet — the shout — doesn't
fade in like web text. It *drops*: the wood block is pressed onto the
bill from just above, landing with a paste-slap, a hair of overshoot,
and the authority of a word you can read from across the street. It
belongs because wood type is physical: letters were blocks, and blocks
land.

**Structure.** The shout word is a `.shout-word` span inside the main
bill's headline (the rest of the headline is ordinary Fraunces setting
and arrives with its bill's slap, §6.5). The word is wrapped so it can
transform independently: `display: inline-block`, transform-origin at
its baseline centre. Where the shout is two words, only the *larger*
word drops; a two-word drop reads as a title animation, not a press.

**Motion spec.** Trigger: synchronised with its bill's slap in §6.5
(same t=0). translateY −14px→0 and scale 1.03→1, 300ms `--ease-slap`.
The word lands 40ms *after* its bill's slap begins — the block is
pressed once the bill is on the wall. A one-frame `--red` ink flash is
forbidden: the word is printed, not neon.

**Choreography timeline (v2).**
- t=0 — Bill begins its slap (§6.5).
- t=40 — Word starts its drop from −14px, scale 1.03.
- t=40–340 — Drop runs `--ease-slap`; overshoot peaks at t≈300 (scale
  1.005 past rest, translateY +1px) — the block *thuds*.
- t=340 — Word at rest. It will never move again except with its bill
  (peek/tilt move the whole bill, never the word alone).

**State matrix (v2).**

| State | Shout word | Notes |
|---|---|---|
| Pre-drop (JS armed, sheet unposted) | Held −14px, scale 1.03, opacity 1 | Never opacity 0 — a shout that might not appear violates law 5; the watchdog drops it instantly at 1000ms |
| Dropping | Animating | 300ms |
| Rest | Set, level (0° — the shout is always true, §4) | Permanent |
| Scrolled-past | Rest | — |
| Hover/focus | Moves only with its bill (§6.3/§6.11) | No independent hover state — words don't perform |
| Disabled | n/a | — |

**Breakpoint behaviour (v2).** ≥1200px: drop −14px as specced.
768–1199px: −10px. <768px: −8px and scale 1.02 — the shout is smaller
on a phone wall and a full drop would bounce the line height of
everything under it; the drop is transform-only at every size, so
layout never shifts (CLS = 0 by construction).

**Edge cases (v2).** Very long shout word (a German touring company's
name): the word scales down via the clamp in §3 before the drop is
armed; if it still wraps, the drop is **cancelled** for that sheet — a
two-line drop reads broken, and the bill's slap alone carries the
arrival. Fonts late: the drop waits for the bill, and the bill waits
for the watchdog (law 2). RTL languages: the drop is vertical; it is
unchanged, but the word's transform-origin moves to baseline *start*.

**Accessibility (v2).** The word is ordinary text in the heading; the
drop is a transform on a span and is invisible to assistive tech. The
heading's accessible name is the full headline text regardless of which
word is wrapped. Contrast: the shout word in `--red` on `--paper` is
5.8:1 at ≥72px — large-text AA with a wide margin; in `--lampblack`,
12.6:1.

**Content merge.** The dropping word is the headline's most important
word — the show's name, the word the poster exists to shout. The
animation is inseparable from the content it delivers.

**Failure fallback.** No JS: the word sits set in the headline. There
is no state in which the headline lacks its shout.

**Reduced motion.** The word is simply set. No drop, no slap.

**Performance & mobile variant.** One transform on one span per sheet.
Zero script beyond the sheet's posting class. Mobile variant is the
breakpoint spec above.

**Tokens.** `--dur-drop`, `--ease-slap`, `--red`, `--lampblack`.

### 6.7 Paste-brush progress stroke

**What & why.** Down the left edge of the wall runs a single vertical
stroke of paste, laid by the brush that posted everything the visitor
has read. It extends as total page progress grows — progress measured
in paste, on the wall itself — and beside its tip, in apparatus type,
"sheets 2 of 5". It belongs because this theme's progress indicator
must be made of the same stuff as its content, and because a brush
stroke can do what a progress bar cannot: look *wetter* at its growing
tip.

**Structure.** A fixed-position rail at the viewport's left edge,
width 14px, sitting on the wall layer (outside the sheets, over
`--wall`). Inside it, an SVG path (a slightly irregular vertical stroke
with bristle striations — three sub-paths at 60/100/45% opacity) whose
`stroke-dashoffset` is scrubbed by the shared loop. The wet tip is the
path's final 60px, drawn in `--ochre-pale` over the stroke's dry
`--paper-deep` body — the brush is still wet where it last touched.
The "sheet n of N" label is a real DOM element (`.sheet-count`) rotated
−90°, positioned at the tip, updated at sheet boundaries.

**Motion spec.** Trigger: continuous scroll, scrubbed to total document
progress (0→1 maps to rail top→bottom). Lerp 0.12 via the shared loop.
The label text changes only when a new sheet becomes the current sheet
(its top crossing viewport centre) — never mid-sheet, never animated;
the count is paperwork, not theatre.

**Choreography timeline (v2).** Scrubbed map:
- 0% progress: stroke length 0, tip at rail top, label "sheet 1 of N".
- Progress p: stroke drawn to p of the rail; the wet tip rides at the
  drawing edge.
- Each sheet boundary: label swaps (no transition; the new count is
  simply lettered there, the way a poster would chalk it).
- 100%: stroke complete; the tip dries — `--ochre-pale` fades to
  `--paper-deep` over 600ms once progress first reaches 1. The brush
  is done.

**State matrix (v2).**

| State | Stroke | Label | Notes |
|---|---|---|---|
| Top of page | Length 0 | "sheet 1 of N" | The brush hasn't started |
| Mid-page (rest at a scroll position) | Drawn to progress, tip wet | Current sheet count | Holds its length when scroll stops — paste doesn't retreat |
| Scrolling up | **Holds** — the stroke does not un-draw | Count follows the current sheet (may decrease) | Law: paste already laid stays laid; only the label, being information, stays honest |
| Bottom reached | Full length, tip drying→dry | "sheet N of N" | One-way, like §6.4 |
| Focus-within page | Unchanged | Unchanged | The rail is not interactive |
| Disabled | n/a | — | — |

**Breakpoint behaviour (v2).** ≥1200px: rail 14px at the wall's left
edge, label rotated beside the tip. 768–1199px: rail 10px, label
horizontal at the rail's foot (rotation crowds a tablet's edge).
<768px: rail 6px, **label hidden** — a phone wall has no margin for
paperwork; the stroke alone remains, and §6.14's navigation carries the
sheet count in its index instead.

**Edge cases (v2).** Short page (one sheet): the stroke still maps
0→1 across the single sheet's scroll; label reads "sheet 1 of 1" and
is hidden — a one-poster wall doesn't number itself. Anchor jump to
the footer: stroke snaps to the mapped value on the next frame (no
catch-up sweep; paste doesn't perform for teleporting visitors).
Resize: rail height re-measures, stroke length re-maps proportionally.
Print: rail absent.

**Accessibility (v2).** The rail is `aria-hidden` decoration; the sheet
count, being information, is *also* present in §6.14's navigation as
real text ("Sheet 2 of 5" in the bill index), so nothing is lost by
hiding the rail's label from AT. The stroke never overlaps sheet
content (it lives on the wall margin) and its colours are not
information-bearing.

**Content merge.** The stroke is on the wall the posters hang on, laid
by the poster's own brush, lengthening by exactly the wall the visitor
has covered. It is progress *in the theme's material*, not a bar
borrowed from a video player.

**Failure fallback.** JS off: no rail (it is JS-armed); the navigation
index (§6.14) still tells the visitor where they are. Nothing about
the sheets depends on the rail.

**Reduced motion.** The stroke is drawn to the mapped length instantly
per scroll position (it is a scrubbed state, not an animation), tip
always dry; the label still updates at boundaries.

**Performance & mobile variant.** One dashoffset write per frame in
the shared loop; the SVG is ~40 path points. Mobile variant is the
breakpoint spec above.

**Tokens.** `--ochre-pale`, `--paper-deep`, `--wall`, `--dur-draw`.

### 6.8 Torn-edge SVG divider

**What & why.** Between two sheets there is no rule, no gap, no
gradient — there is the tear: the ragged line where the previous sheet
ripped away from the one beneath. As a sheet boundary enters, that torn
edge draws itself in SVG along the overlap, fibre by fibre. It belongs
because on a real wall, sheets are not separated by whitespace; they
are separated by damage, and the damage has a shape.

**Structure.** An inline SVG spanning the sheet's width in the overlap
zone (§4), height 26px, holding one path: the tear line — a jagged,
hand-torn profile generated from a fixed seed per boundary (7 canonical
tear paths ship with the theme; boundary *n* uses path *n mod 7*, so
the wall's tears repeat the way real tearing habits do, never random
per load). The path is stroked in `--paper-deep` with a 1px
`--wall-mortar` shadow path offset 2px beneath — the tear has depth
because paper has thickness. Above the line, the outgoing sheet's torn
fringe (a clip-path on its bottom edge using the same path, inverted);
below it, the incoming sheet's top edge.

**Motion spec.** Trigger: the boundary enters the viewport's lower
third. The path draws via `stroke-dashoffset`, 500ms `--ease-squeegee`
— the tear appears at the speed of a hand pulling. The fringe clip is
present from first paint (the sheet was always torn); only the *line*
draws, so the divider never gates content.

**Choreography timeline (v2).**
- t=0 — Boundary at viewport's lower third.
- t=0–500 — Tear line draws left→right (the direction a right-handed
  tear travels; boundaries alternate direction by parity — even
  boundaries draw right→left, because the poster tore from whichever
  hand was free).
- t=500 — Line complete; it does not redraw, loop, or shimmer. A tear
  is a fact.

**State matrix (v2).**

| State | Tear line | Fringe | Notes |
|---|---|---|---|
| Below fold | Undrawn | Present (clip applied) | Content on both sides fully readable |
| Drawing | Animating | Present | 500ms |
| Drawn (rest) | Complete | Present | Permanent |
| Scrolled-past | Complete | Present | Never un-draws |
| Hover/focus | Unchanged | Unchanged | The divider is not interactive |
| Disabled | n/a | — | — |

**Breakpoint behaviour (v2).** ≥1200px: height 26px, full path detail.
768–1199px: height 20px. <768px: height 14px and the path uses its
coarse variant (fewer, larger teeth — fine fibres vanish at phone
width and read as noise); the draw shortens to 380ms to match §6.2's
mobile tear-off, whose leading edge this line is.

**Edge cases (v2).** Boundary already in view on load (short first
sheet): the line draws on load after the hero's paste-up completes
(t≈900ms), never competing with it. Jump scroll past a boundary: the
line is simply drawn when next seen — no catch-up performance.
SVG unsupported (effectively extinct, but the law is the law): the
fringe clip alone remains, and a 2px `--paper-deep` border on the
outgoing sheet's bottom edge stands in for the line.

**Accessibility (v2).** Purely decorative: `aria-hidden`, role
presentation. Section boundaries are conveyed by headings and
landmarks, never by the tear. The line's contrast against both sheets
is low by design — it carries no information, so it owes no contrast.

**Content merge.** The divider is the physical boundary between two
real sheets — the tear in the actual paper stack the visitor is
reading through. Remove the sheets and the divider has nothing to
divide.

**Failure fallback.** JS off: fringe clips remain (CSS), the line is
present in its drawn state (dashoffset is JS-armed only). The wall
reads as torn paper, statically — correct.

**Reduced motion.** Line present, drawn, at first paint of the
boundary. No draw animation.

**Performance & mobile variant.** One dashoffset animation per
boundary, ≤7 boundaries per page; paths are pre-authored, not
generated at runtime. Mobile variant is the breakpoint spec above.

**Tokens.** `--dur-draw`, `--ease-squeegee`, `--paper-deep`,
`--wall-mortar`.

### 6.9 Woodcut portrait settle

**What & why.** The bills carry portraits — the leading lady, the
fiddler, the villain — printed as woodcuts: bold lampblack shapes, one
flat colour, visible knife work. As a portrait scrolls through the
viewport it *settles*: it scales in its frame from 1.08 to 1 while its
ink darkens and a 2px wet blur dries to sharp — the print finishing
itself in front of you. It belongs because in this theme an image is
not a photograph that loads; it is an impression that dries.

**Structure.** Each `.woodcut` is a figure with a poster frame (a
lampblack keyline border, 3px, with the sheet's paper showing as the
mount). The image itself is duotone by construction: source art is
prepared as lampblack linework over a flat `--red` or `--ochre` field
(build-time duotone, §15 — never a runtime filter over a colour photo,
§9). The settle is a transform on the image inside an
`overflow: hidden` frame, plus a blur filter that exists only during
the settle window.

**Motion spec.** Trigger: portrait's frame 30% visible. Scale
1.08→1.00, 700ms `--ease-settle`; filter blur 2px→0 over the same
700ms; a `--sheen` ink-gloss overlay fades 0.3→0 across 900ms (the ink
is wettest just after the scale lands). The settle happens **once**,
the first time the portrait is properly seen; portraits already in
view on load settle with their sheet's posting (§6.5), offset +200ms.

**Choreography timeline (v2).**
- t=0 — Frame 30% visible.
- t=0–700 — Scale settles 1.08→1; blur dries 2px→0 in step.
- t=200–900 — Ink gloss fades 0.3→0 (starts late: fresh ink shines
  after it lands, not while it moves).
- t=900 — `.is-settled`; the portrait is a dry print forever (law 3).

**State matrix (v2).**

| State | Scale | Blur | Gloss | Notes |
|---|---|---|---|---|
| Unseen (below fold) | 1.08 held | 2px held | 0.3 held | Only under JS-armed root; no-JS state is Settled |
| Settling | Animating | Drying | Fading | 900ms total |
| Settled (rest) | 1.00 | 0 | 0 | Permanent |
| Scrolled-past | Settled | 0 | 0 | Never re-settles |
| Hover | Settled; the *frame's bill* may peek/tilt (§6.3/§6.11) | 0 | 0 | The portrait itself has no hover state — prints don't respond to being looked at |
| Focus-within frame (linked portrait) | Settles instantly if unsettled | 0 | 0 | Focus must never land on a blurred image |
| Disabled | n/a | — | — | — |

**Breakpoint behaviour (v2).** ≥1200px: full settle as specced.
768–1199px: scale from 1.06, blur 1.5px. <768px: scale from 1.04,
**blur cut** (mobile GPUs pay real money for filter animations, and at
phone size 2px of blur is invisible anyway) — the settle is scale +
gloss only, 500ms.

**Edge cases (v2).** Image late (slow network): the frame holds its
paper-toned mount with the portrait's caption already readable; when
the image arrives it is placed **already settled** — a late print does
not perform its drying for an audience that waited; it apologises by
being ready. Image failed: the frame shows the woodcut's fallback —
the character's initial letter as a Fraunces ornament block on the
duotone field (authored at build time for every portrait, §15) — the
bill still reads as designed. Portrait taller than the viewport: the
trigger is the frame's *top* crossing 70% viewport height instead.

**Accessibility (v2).** Every woodcut has real alt text naming the
character and the scene ("Woodcut portrait of Marta Vane as the
Miller's Daughter, holding a lantern") — the duotone treatment never
excuses a decorative-image shrug for content portraits. The blur phase
never applies to an image a user has focused or is reading via AT.
Settled contrast: lampblack linework on its colour field is ≥4.5:1
for the portrait's essential shapes (checked at build, §10).

**Content merge.** The portraits are printed *on the bills* — they are
the cast the poster advertises. The settle is their ink drying on the
very sheet the visitor is reading, inside the poster's own frame.

**Failure fallback.** No JS: portraits sit settled, sharp, full size.
The frame, mount, and caption are plain HTML/CSS.

**Reduced motion.** Portraits are settled and sharp at first paint.
No scale, no blur, no gloss.

**Performance & mobile variant.** Transform + filter on one image per
portrait, ≤4 portraits animating concurrently (the loop staggers
extras by 120ms rather than dropping them). `will-change` only during
the settle. Mobile variant is the breakpoint spec above.

**Tokens.** `--ease-settle`, `--sheen`, `--lampblack`, `--red`,
`--ochre`.

### 6.10 Street-lamp light shift

**What & why.** The wall stands under a street lamp, and the lamp is
alive: over a slow 14-second loop, the light's angle drifts ±6°, so
paste wrinkles throw slightly different shadows, sheet edges catch the
light differently, and dust motes drift through the hero's lamplight.
Nothing moves but the light — which is to say, everything feels
different without anything performing. It belongs because it is the
theme's only purely atmospheric element, and a wall without weather is
a photograph of a wall.

**Structure.** One `.lamp` overlay per sheet: a large radial/linear
gradient layer (`pointer-events: none`, `aria-hidden`, mix-blend-mode:
soft-light at 0.5) whose gradient angle is a CSS custom property
(`--lamp-angle`) written by the shared rAF loop from a 14s sine. Paste
wrinkles are real geometry — 3–5 subtle ridge shadows baked into each
sheet's background via layered gradients at build time (§15); the lamp
layer's moving light is what makes them *read* as wrinkles rather than
stains. Dust exists only in the hero sheet: ≤14 motes, 2–3px
`--paper-light` dots at 0.25–0.5 opacity on a dedicated canvas-free
layer (transform-animated divs — 14 nodes is cheaper than a canvas at
this count), drifting on slow Lissajous paths inside the hero's lamp
cone.

**Motion spec.** Trigger: time, ambient — runs whenever the owning
sheet is in the viewport; pauses entirely off-screen (IO-gated).
Angle: base 118°, drift ±6°, period 14s, `--ease-drift` sine. Dust:
each mote loops its path in 18–30s (per-mote duration from a fixed
table — deterministic, like the rotations), drifting downward overall
at ~4px/s: dust settles, even in lamplight.

**Choreography timeline (v2).** A loop, mapped not clocked:
- Phase 0.0–0.25: light leans left (−6°); left sheet edges brighten,
  right wrinkles deepen.
- Phase 0.25–0.75: light travels through centre (118°) to the right
  lean (+6°); the emphasis crosses the sheet like a cloud crossing a
  street.
- Phase 0.75–1.0: returns. The loop has no seam a visitor can catch —
  the derivative is continuous at the wrap.

**State matrix (v2).**

| State | Lamp layer | Dust (hero only) | Notes |
|---|---|---|---|
| Sheet in view (rest) | Drifting ±6°, 14s | Drifting | The ambient default |
| Sheet off-screen | Paused (property frozen) | Paused | Zero cost for unseen wall |
| Hover/focus anywhere | Unchanged | Unchanged | The lamp does not notice visitors — that is its dignity |
| Scrolled-past | Resumes on return, phase-continuous | Resumes | The loop's clock is global, so all sheets share one lamp phase |
| Dark colour scheme | Lamp becomes primary light (§2 ruling); drift widens to ±8°, layer opacity 0.65 | Visible against the dimmed wall | After dark, the lamp works harder |
| Disabled | n/a | — | — |

**Breakpoint behaviour (v2).** ≥1200px: full spec. 768–1199px: drift
±5°, dust ≤10 motes. <768px: drift ±4°, **dust cut** (on a phone the
hero is one glance; motes read as screen dirt), lamp layer kept — the
wrinkle light is load-bearing for the paper's tactility at every size.

**Edge cases (v2).** Low-power device / `save-data`: the loop drops
to a static angle (118°, the lamp at rest) — a still lamp is a correct
lamp. Tab hidden: loop clock pauses; on return it resumes from the
same phase (no jump). Multiple sheets in view (short sheets on a tall
monitor): all share the single `--lamp-angle` value — one lamp, one
sky; per-sheet angles would be three lamps and a lie.

**Accessibility (v2).** The lamp layer is soft-light at ≤0.5 (0.35
over text zones, same zoning as §6.4's sheen cap): worst-case ink
contrast during the drift stays ≥7:1, verified at both drift extremes
in the §10 gate. The motion is far below any photosensitivity
threshold (one cycle per 14s, luminance delta <4%). Dust is
`aria-hidden`; the layer is never focusable, never announced.

**Content merge.** The light falls on *these* posters — their
wrinkles, their edges, their paste. It is the scene's single light
source, shared by every element on the wall; remove the wall and there
is nothing to light.

**Failure fallback.** JS off: the lamp layer renders at its static
118° base (the layer is CSS; only its drift is JS). The wall is lit,
still, and correct.

**Reduced motion.** Static lamp at 118°, no dust. The wall after the
wind drops.

**Performance & mobile variant.** One custom-property write per frame
(shared loop) driving composited gradients; dust is ≤14 transforms,
hero only. This is the cheapest element in the theme per unit of
atmosphere. Mobile variant is the breakpoint spec above.

**Tokens.** `--ease-drift`, `--paper-light`, `--sheen`.

### 6.11 Loose-paper tilt + paste-slap click

**What & why.** Posters are not glued flat by physics; they are held by
paste and bullied by weather. On hover, a bill tilts 1–2° like loose
paper lifting in a draft; on click, it answers with a paste slap — a
quick press back onto the wall with a wet-sheen flash, the bill
re-stuck by the visitor's own hand. It belongs because it is the
theme's click feedback in the theme's own material: no ripple, no
glow, no colour pulse — paper, pressed.

**Structure.** Every interactive `.bill` / `.notice` / `.card-notice`
(§6.15) is a single transformable element. The tilt is a rotate toward
the pointer's half (pointer in the left half → the bill leans −1.5°;
right half → +1.5°; the lean pivots on the *opposite* bottom corner,
transform-origin at the pasted edge) plus a 1px lift of the free edge's
shadow. The slap is a class-driven keyframe: scale 0.98 at 110ms with
a `.sheen` flash overlay sweeping the bill once (opacity 0→0.4→0,
240ms). Both are driven through the shared loop's spring for the tilt
(stiffness 0.18, damping 0.72 — the same spring as §6.3, so all paper
on the wall has one physics).

**Motion spec.** Tilt: trigger pointerenter/move across halves;
240ms to full lean via the spring; returns to its fixed §4 lean on
leave (200ms `--ease-settle`). Note: the tilt *adds* to the bill's
resting rotation token — a bill at −1.6° rest leans to −3.1°/−0.1°,
never to an absolute angle; the poster's handwriting survives the
weather. Slap: trigger click/activation; scale 1→0.98→1, 110ms
`--ease-slap`; sheen flash 240ms `--ease-squeegee`; then the element's
real action (navigation, §6.16 form focus, etc.) proceeds — the slap
never delays an action by more than its own 110ms.

**Choreography timeline (v2).**
- t=0 — Pointer enters; half detected.
- t=0–240 — Bill leans to ±1.5° over its rest lean, free-edge shadow
  grows; slight overshoot at t≈190 (paper breathes past, settles).
- Hold — Lean holds while hovered; crossing the centre line re-leans
  to the other half over 240ms (no snap).
- Leave — t=0–200: returns to its token lean exactly.
- Click (any time) — t=0–110: slap scale + press; t=0–240: sheen flash
  crosses; the click's action fires at t=0 (the slap is feedback, not
  a gate).

**State matrix (v2).**

| State | Rotation | Scale | Sheen | Notes |
|---|---|---|---|---|
| Rest | Token lean (§4) | 1 | 0 | Pasted |
| Hover (desktop) | Token lean ±1.5° toward pointer half | 1 | 0 | Plus §6.3's corner lift if the element is a bill — tilt and peek compose, they never fight (one spring, summed targets) |
| Focus-visible | Token lean +1° toward centre, held | 1 | 0 | Keyboard's version of the lean: smaller, steadier, plus the focus ring (§6.13's rule ring) |
| Active (press) | Token lean (flattened by the press) | 0.98 | Flashing | The slap |
| Scrolled-past | Token lean | 1 | 0 | No physics off-screen |
| Touch | No tilt (no hover); tap = slap only | 0.98 on tap | Flash on tap | Touch gets the press, not the draft |
| Disabled (e.g. sold-out card) | Token lean, **no tilt** — old paste, heavy paper | 1 | 0 | Click gives no slap; the bill is dead paper and says so by stillness |

**Breakpoint behaviour (v2).** ≥1200px: lean ±1.5°. 768–1199px: ±1.2°.
<768px: tilt disabled entirely (touch has no hover; emulating it on
tap-and-hold caused more confusion than delight in every wall test) —
tap slap remains at full spec.

**Edge cases (v2).** Pointer racing across a row of notices: the 60ms
intent delay from §6.3 applies to tilt too — one spring target per
element, retargeted, never stacked. A bill inside the pinned bill zone
(§6.18): tilt disabled while pinned (the bill is under the visitor's
reading eye; weather is for browsing, not for reading). Slap on a bill
whose action opens §6.16's form sheet: the slap completes on the bill;
the form sheet posts by its own rules — two papers, two physics, no
choreography collision.

**Accessibility (v2).** Tilt is decoration on an otherwise standard
control: the element's role, name, and activation are untouched, and
the focus-visible lean + ring ensure keyboard users get equivalent
"this is live" feedback. The slap never delays activation. Touch
targets are the whole bill (≥44px by construction). The sheen flash
is a 240ms luminance change under 10% — no photosensitivity concern.

**Content merge.** The feedback is the poster's own paper behaviour —
leaning in a draft, pressed by a hand. The same element that carries
the content carries the interaction; there is no overlay, no wrapper
effect.

**Failure fallback.** JS off: bills sit at their token leans (CSS
transforms in the base stylesheet), clicks are plain clicks. The wall
loses its weather and keeps its posters.

**Reduced motion.** No tilt, no slap scale. Click feedback becomes the
sheen flash alone at 0.25 opacity, or nothing if the visitor's setting
is joined by `prefers-reduced-transparency` — in which case focus and
active states rely on the rule ring only.

**Performance & mobile variant.** One spring per hovered element in
the shared loop; only the hovered element is ever in motion. Mobile
variant is the breakpoint spec above.

**Tokens.** `--dur-slap`, `--dur-tilt`, `--ease-slap`,
`--ease-squeegee`, `--ease-settle`, `--sheen`, `--lean-bill-a`,
`--lean-bill-b`, `--lean-notice`.

### 6.12 Paste-rectangle skeleton + wall-strip transition

**What & why.** Two states, one fiction. **Loading:** before a sheet's
bills arrive, the wall shows bare paste rectangles — pale wet oblongs
where posters *will* go, because on a real wall the paste goes up
before the paper. **Leaving:** navigation strips the whole wall in one
fast downward peel — the season is over, the bills come down, the next
wall is already pasted beneath. It belongs because loading and leaving
are the wall's own two acts of change; neither should ever look like a
web app thinking.

**Structure.** Skeleton: each `.sheet` reserves its notices' geometry
with `.paste-mark` rectangles (`--paper-light` fill, a 1px
`--ochre-pale` wet edge at the bottom — paste slumps) at the exact
positions and rotations the bills will occupy (the §4 leans are in the
skeleton too — the paste knows where the paper goes). Bills replace
their marks one-for-one as content lands (each bill's arrival is its
own §6.5 slap, compressed). Strip transition: on route change, the
current wall's top sheet receives the §6.2 peel at `--dur-strip`
(500ms) with the whole wall's sheets following as one stacked peel —
implemented as a single transform on the wall wrapper, the destination
wall rendered beneath before the strip begins (law 1).

**Motion spec.** Skeleton marks are static (wet paste does not
animate; a shimmer is banned, §9) except one behaviour: as each bill
lands, its mark is covered — the replacement is the motion. If content
has not landed in 1200ms, marks remain and a line of apparatus text
appears in the first mark: "THE BILLS ARE LATE — the poster's cart is
coming" (themed, honest, and *in* the fiction; §12's loading voice).
Strip: trigger route change; 500ms `--ease-peel`; the old wall
translates down 102% with progressive top clip; new wall revealed
posted and dry (a fresh wall never performs its paste-up on arrival
via navigation — §6.1 is for first visits only).

**Choreography timeline (v2).**
- Skeleton: t=0 — marks visible with the wall's first paint (no blank
  page, ever). t=content — bills slap over their marks, 90ms stagger
  (compressed §6.5). t=1200 (no content) — the lateness line appears.
- Strip: t=0 — route change committed; destination rendered beneath.
  t=0–500 — old wall strips down. t=500 — destination wall owns the
  viewport; scroll position is the destination's top (or its restored
  position for back navigation).

**State matrix (v2).**

| State | Skeleton marks | Wall | Notes |
|---|---|---|---|
| Loading (first paint) | Shown, static | Wall + marks only | Never a spinner; the paste is the promise |
| Content landing | Covered bill by bill | Bills posting | 90ms compressed stagger |
| Loaded (rest) | Gone (covered) | Posted wall | Marks do not linger under bills |
| Late (>1200ms) | Shown + lateness line | — | Honest, in-fiction, and the §10 gate counts a late wall as a defect to fix, not a state to polish |
| Navigating away | n/a | Stripping | 500ms |
| Back navigation | Skipped — destination restores instantly at its scroll position | Posted | History is a wall you already stood at; it does not re-strip |
| Disabled | n/a | — | — |

**Breakpoint behaviour (v2).** ≥1200px: as specced. 768–1199px: strip
450ms. <768px: strip 380ms (matching §6.2's tear-off family); skeleton
marks keep exact geometry (mobile bills stack in one column, §4, so
marks are full-width oblongs).

**Edge cases (v2).** Navigation interrupted (user hits back mid-strip):
the strip completes to whichever wall the history lands on — the
wrapper transform is idempotent, set from the route, never accumulated.
Slow destination: if the next wall's content isn't ready, its own
skeleton wall shows beneath the strip — the visitor watches a wall
being stripped to a pasted-but-unbilled wall, which is still the
fiction holding. Prefetch failure: strip is cancelled, current wall
stays, the link behaves as a normal navigation. Print: skeleton and
strip absent; walls print as posted sheets.

**Accessibility (v2).** The skeleton region carries `aria-busy="true"`
on the sheet and a visually hidden status ("Loading the bills") that
resolves when the last bill lands — announced once, politely, never
per bill. The strip transition does not move focus; the destination's
heading receives focus by the router's normal rule *after* the strip
completes. Lateness line is real text, readable by AT.

**Content merge.** The skeleton is the wall's paste awaiting the very
bills that will cover it, at their exact places; the strip removes
the very wall the visitor read. Neither state borrows a generic
loader's shape.

**Failure fallback.** JS off: no skeleton (content is server-rendered
into place), no strip (plain navigation). The wall simply *is*.

**Reduced motion.** Skeleton identical (it never moved). Strip becomes
an instant wall swap. Back/forward always instant.

**Performance & mobile variant.** Skeleton is pure CSS geometry —
zero script, zero layout shift (marks reserve the bills' exact boxes,
CLS = 0). The strip is one wrapper transform. Mobile variant is the
breakpoint spec above.

**Tokens.** `--dur-strip`, `--ease-peel`, `--paper-light`,
`--ochre-pale`, `--dur-fallback`.

### 6.13 Bill-index navigation

**What & why.** A wall has no navbar; it has the bill-poster's index —
a narrow strip pasted at the wall's top listing every sheet on the wall
by its shout's first words, the way a poster would chalk his rounds.
The current sheet's line is struck in `--red`. It belongs because
navigation on this wall must be *another piece of paper*, smaller and
plainer than the bills it indexes, or the fiction tears at the very
first element a visitor touches.

**Structure.** A `.bill-index` strip, fixed to the wall top (above the
sheets' layer, on the wall itself), full wall width, height 52px:
left, the house name in Fraunces 600 18px ("THE GOOSE & FIRKIN" for
the §8 example client); centre/right, the sheet index as a horizontal
list of apparatus-type links (Lora 500 uppercase, 11.5px, 0.18em) —
each link is a sheet's short title ("TONIGHT", "THE COMPANY", "SONGS",
"TICKETS", "THE HOUSE"). The current sheet's link carries a `--red`
rule drawn beneath it (2px, the proofreader's stroke borrowed by the
poster). On scroll past the hero, the strip gains a `--paper-deep`
backing (it was transparent over the wall) so it reads as a pasted
label, never as glass.

**Motion spec.** The strip is pasted from first paint (it never
animates in — the index was here before you were). The red rule moves
between links as the current sheet changes: it *draws* from the old
link to the new (a 260ms width/position transition, `--ease-squeegee`,
like a brush stroke re-laid). Backing fade: 200ms when the hero's top
leaves the viewport. Links get §6.11's slap on click (they are paper)
and §6.3's peek is **refused** here — the index is too small to peek
and too useful to play with.

**Choreography timeline (v2).**
- t=0 (load) — Strip present, first link ruled in red (drawn 260ms
  after the hero's band 1 completes — the index signs the wall once
  the first poster is up).
- Sheet change — t=0–260: rule draws across to the new current link;
  the old rule is not erased first — the stroke travels.
- Scroll past hero — backing fades in over 200ms; strip is now a label
  on the wall, permanently for this page.

**State matrix (v2).**

| State | Strip | Current rule | Notes |
|---|---|---|---|
| Top of page | Transparent backing, over wall | Under sheet 1's link | — |
| Scrolled (rest) | `--paper-deep` backing | Under current sheet's link | — |
| Hover (link) | — | — | Link underlines with a 120ms rule draw; link leans +0.8° (§6.11 family, reduced) |
| Focus-visible | — | — | 2px `--lampblack` outline offset 3px — the "rule ring" used across the theme; never colour alone |
| Active | — | — | §6.11 slap, 110ms |
| Current link | `aria-current="true"` | `--red` rule beneath | The red is *also* carried by weight (600) so colour is not the only signal |
| Disabled | n/a — index links are never disabled | — | A sheet that doesn't exist isn't indexed |

**Breakpoint behaviour (v2).** ≥1200px: full strip, all sheet links
visible. 768–1199px: house name shortens to its initials block
("G&F" as a small wood block), links keep. <768px: the index becomes
**two rows**: house line, then a horizontally scrollable link row
(scroll-snap, no visible scrollbar, the current link scrolled into
view on sheet change); strip height 84px. The sheet count ("sheet n
of N") appears at the row's end — this is where §6.7's hidden mobile
label lives on.

**Edge cases (v2).** Many sheets (a festival wall with 9 sheets):
the desktop strip truncates the index to the first 6 links plus a
"MORE BILLS" link that opens §6.15's listing sheet — the index never
wraps to two lines on desktop; a wrapped nav is a poster falling off
the wall. Long house name: the name block truncates with an ellipsis
in Fraunces — never shrinks below 16px (wood type doesn't do small).
Route change: the strip persists across the §6.12 strip transition
(it belongs to the wall, not the sheet) — only its rule re-draws.

**Accessibility (v2).** A real `<nav>` with an aria-label ("Sheets on
this wall"); links are links, in DOM order = sheet order; current
sheet conveyed by `aria-current` + weight + rule (three signals).
Focus order: house name (home link) first, then index links. Touch
targets ≥44px tall (the strip's full height is the target). The
mobile scrollable row is keyboard-scrollable and its links remain in
tab order.

**Content merge.** The index lists the actual sheets below it, by
their own first words; it is the wall's table of contents pasted on
the wall. It contains nothing that isn't down the page.

**Failure fallback.** No JS: strip renders with its backing on, the
first link ruled; links are anchor links to sheet IDs and work
natively. Current-sheet tracking is an enhancement.

**Reduced motion.** The rule swaps instantly between links; backing
appears without fade; link lean removed.

**Performance & mobile variant.** One fixed strip; the rule is one
transform/width transition; current-sheet tracking rides the sheets'
existing IO (§6.5) — no separate observer. Mobile variant is the
breakpoint spec above.

**Tokens.** `--red`, `--paper-deep`, `--lampblack`, `--ease-squeegee`,
`--dur-slap`.

### 6.14 Headline bill hero composition

**What & why.** The hero is not a section with a headline in it; it is
**one bill** — the main bill of the first sheet — composed the way a
bill-poster's best work is composed: the shout at the top in wood type,
the Playfair bill beneath it (the respectable announcement), the
woodcut portrait at the side, the price and date struck in red at the
foot, and the first stanza of the ballad beginning below the fold of
the sheet like a promise. This element is the composition spec that
§6.1 pastes up and §6.6 drops into.

**Structure.** Inside sheet 1 (§4 geometry): a `.main-bill` occupying
the sheet's top 62%: shout line(s) (Fraunces 900, §3), a `--lampblack`
rule (4px) with a torn right end, the Playfair bill head + two lines of
notice body, and a two-column foot — left, the woodcut portrait
(§6.9, ~34% width); right, the data block: date in apparatus type,
admission prices as wood-numeral figures (§6.15's counters live here
first), and the primary action: a **ticket slip** button styled as a
small pasted notice (`--red` border, paper fill — §11's bill-button).
Below the main bill, the sheet's remaining notices (§6.5) and the
verse stream's opening stanza (§6.18). The bill pins (§6.18) only on
verse sheets; on the hero sheet it does not pin — the first sheet is
read whole.

**Motion spec.** The hero's motion is the sum of its parts, sequenced
by §6.1: bands sweep (450ms ×3, stagger 200ms), the shout word drops
(§6.6, riding band 1), notices slap ( §6.5 — on the hero sheet the
"five notices" *are* the main bill's components plus the two small
notices: the composition posts as one poster, so its slap order is:
main bill, portrait, data block, small notice A, small notice B),
portrait settles ( §6.9, +200ms), counters count ( §6.15, when the data
block is posted). Total hero ceremony ≤2000ms including the sheen dry;
everything readable by t=850 (bands) and fully dry by t=2000.

**Choreography timeline (v2).**
- t=0 — §6.1 band 1 (shout band) sweeps; §6.6 drop rides at +40ms.
- t=200 — Band 2 (bill head, portrait frame) sweeps; portrait begins
  its settle at +200 more.
- t=400 — Band 3 (data block, notices) sweeps; counters start when the
  data block lands (≈t=650).
- t=850 — Sheet fully posted; hero readable end to end.
- t=850–2000 — Sheen dries (§6.1); lamp (§6.10) is already drifting —
  it started at first paint and never waited for the ceremony.

**State matrix (v2).**

| State | Composition | Notes |
|---|---|---|
| First paint | Bands clipped, content in DOM | <100ms in practice |
| Posting | Per §6.1/§6.5/§6.6/§6.9 timelines | Sequenced, never simultaneous — a poster has two hands |
| Posted (rest) | Dry bill, lamp drifting | The state 99% of the visit lives in |
| Scrolled-past | Posted; §6.2 peel may take the sheet at its boundary | The hero peels like any sheet — no celebrity exemption |
| Hover/focus-within | Components respond individually (§6.3/§6.11) | The composition itself has no hover state |
| Disabled | n/a | The ticket slip has its own states (§6.16/§11) |

**Breakpoint behaviour (v2).** ≥1200px: as specced; portrait column
34%. 768–1199px: portrait column 40%, shout clamp steps down per §3.
<768px: the composition **stacks in bill order** — shout, rule, bill
head, portrait (full sheet width, 16:9 crop of the woodcut's upper
field — the face, never the feet), data block, action. Bands reduce
to §6.1's two. The data block's two columns become one; prices stay
wood-numeral and large — a phone poster still shouts its price.

**Edge cases (v2).** No portrait available (a poetry night, no cast):
the portrait column is replaced by a second small notice (a review
quote pasted as a bill) — the composition's grid holds; an empty
frame is banned (§9). Very long shout (three lines): the bill head
moves below the fold of the sheet and the hero sheet grows — the
shout is never shrunk below the §3 clamp floor to fit a viewport;
posters are allowed to be tall. Sold-out show: the data block's price
line is struck through in `--red-deep` and a "HOUSE FULL" notice
slaps over the bill's corner at rest (pre-posted, not animated in
late) — bad news is typeset, §6.5's disabled rule.

**Accessibility (v2).** The hero's heading hierarchy: the shout is the
page's `<h1>` (the full bill title, with the dropped word a plain
span inside it); the bill head is a `<p>` styled large, *not* a
heading — one poster, one headline, no heading inflation. The ticket
slip is a real link/button with a full name ("Book tickets for The
Miller's Daughter"). Focus order: index (§6.13) → ticket slip → the
sheet's notices in reading order. All contrast per §2 at rest and
mid-ceremony (§6.1's sheen cap).

**Content merge.** The composition *is* the page's primary content —
show, portrait, price, date, action — arranged as the poster that
advertises it. There is no hero "design" separate from the bill.

**Failure fallback.** No JS: the full bill sits posted and dry; every
component readable; the ticket slip works.

**Reduced motion.** The bill is simply there. Counters show final
figures; the portrait is settled; the sheen never appears.

**Performance & mobile variant.** The hero's cost is its parts' costs
(§§6.1, 6.5, 6.6, 6.9) plus one woodcut image (≤120KB, §14). No
additional loops. Mobile variant is the breakpoint spec above.

**Tokens.** `--red`, `--lampblack`, `--paper`, `--dur-band`,
`--dur-dry`.

### 6.15 Notice cards

**What & why.** Beyond the hero, the wall's listings — other shows,
other nights, the company's repertoire — are **notice cards**: small
bills, each a complete poster in miniature (shout-scale head at notice
size, woodcut thumb, date, price, one line of notice body), pasted in
a grid on their sheet. They belong because a theatre's season is a
wall of bills, and because this is where the theme's counters live:
admission prices and crowd figures count up in wood-type numerals when
a card's data line arrives.

**Structure.** A `.card-notice` is an `<article>` on the §4 grid
(4 columns desktop, its own fixed lean from the §4 table by position).
Inside: woodcut thumb (top, 3:2, §6.9 settle on arrival), notice head
(Fraunces 600, 22px), one line of Lora body (≤90 chars — cards do not
carry paragraphs), a data row: date (apparatus) left, price (Fraunces
600, 28px) right, and a text link "Read the bill" with the 120ms rule
draw. The whole card is §6.3-peekable and §6.11-tiltable; the link is
the card's only control (the card itself is not a link — the peek and
the tilt need a surface that isn't a button).

**Motion spec.** Cards post with their sheet (§6.5 stagger, in grid
reading order). Counters: when a card's data row first enters, its
price/crowd figure counts from 0 (or from the figure's first digit's
sort — see below) to its value in 900ms, **stepped in 12 frames**
(75ms steps, no easing curve — wood type lands sort by sort), set in
Fraunces 600 with real glyph widths (no tabular forcing, §3). A crowd
figure ("1,900 songsheets") counts its thousands in chunks of 25 per
step near the end — counters decelerate by chunk size, not by easing.
Each card counts once.

**Choreography timeline (v2).**
- t=0 — Card's sheet posts (§6.5 slot by grid order).
- t=data row visible — Counter starts; steps at 75ms intervals.
- t=+900 — Counter lands on the true figure; `.is-counted`; the figure
  is thereafter plain text.
- Hover/focus — §6.3 peek (12–16px) and §6.11 tilt compose over the
  posted card; the counter, if still running, finishes instantly
  (a reader leaning in wants the number, not the show).

**State matrix (v2).**

| State | Card | Counter | Notes |
|---|---|---|---|
| Unposted (below fold, JS armed) | Held at §6.5 slap-start | Not started; final value in DOM for AT/no-JS | — |
| Posted (rest) | Flat at its lean | Final figure | The durable state |
| Counting | Posted | Stepping | ≤900ms, once |
| Hover/focus-within | Corner lifted (§6.3), tilted (§6.11) | Final figure (finishes instantly on focus) | — |
| Active (link press) | §6.11 slap on the card body | Final | The link navigates at t=0 |
| Sold out (disabled) | Posts normally; price struck in `--red-deep`, "HOUSE FULL" apparatus line under the data row | Does not count — a full house doesn't advertise its crowd | Peek reduces to 8px (§6.3) |
| Scrolled-past | Posted | Final | — |

**Breakpoint behaviour (v2).** ≥1200px: 3 cards per row (4-column
spans with gutter paper). 768–1199px: 2 per row. <768px: 1 per row,
thumb crops to 16:9 top field, counter steps reduce to 8 (faster
landing on a fast-scrolling wall), peek is tap-driven per §6.3.

**Edge cases (v2).** A season of one show: the listing sheet carries
the single card at shout-adjacent scale (span 8) plus the §6.18 verse
stream — a one-card grid is a layout error the §10 gate rejects.
Missing price (free event): the data row shows "FREE" lettered as a
wood-type word — it *drops* (§6.6 mechanics, notice scale) instead of
counting; free is a shout, not a number. Long titles wrap to two lines
max, then the card grows — cards in a row are *not* equalised by
truncation (posters are the size they are); the row's baseline grid
absorbs it via the §4 overlap.

**Accessibility (v2).** The counter is `aria-hidden` while stepping,
with the final figure present in an adjacent visually-hidden span
from first paint — AT users get the number, not the theatre. The
card's link name includes the show title ("Read the bill for The
Miller's Daughter"). Sold-out state is text ("House full"), never
colour alone. Card images carry §6.9's alt discipline.

**Content merge.** Each card is a real bill for a real show, with its
real price counted in the poster's own numerals. The grid is the
season pasted up; remove the shows and the element is gone.

**Failure fallback.** No JS: cards sit posted, counters show final
figures (they are the DOM values; the count is a JS-armed overlay of
the stepping). Nothing is gated on the animation.

**Reduced motion.** Cards post with their sheet's reduced state;
counters show final figures immediately.

**Performance & mobile variant.** Cards share their sheet's IO and the
shared loop; counters are 12 timeouts *or* loop steps (implemented as
loop steps — law 4 — one counter at a time per viewport). Mobile
variant is the breakpoint spec above.

**Tokens.** `--red-deep`, `--lampblack`, `--ease-slap`, `--lean-notice`.

### 6.16 Box-office booking form

**What & why.** Conversion on this wall is a **booking notice**: a
form pasted up like every other bill — "BOOKING — write plainly, the
box office reads everything" — whose fields are ruled lines on paper,
whose errors are proof-marks in red in the margin, and whose success
is a stamped ticket stub. It belongs because a theatre form that looks
like a SaaS checkout would tear the fiction exactly where money
changes hands, and because the broadside's own conversion artefact
(the penny ballad's "to be had of the printer") is a form by another
name.

**Structure.** The form lives on its own sheet (the Tickets sheet) as
a single-column notice, max-width 560px, centred on the sheet, at the
−0.6° lean. Fields (name, email, performance date — a styled
`<select>` of real dates, seats — a stepper of two bill-buttons,
seating tier — two radio "bills" side by side): each field is a label
in apparatus type above a 1px `--ink-soft` ruled line; the input is
transparent, borderless, Lora 18px, sitting *on* the line like ink.
Required fields carry a small `--red` ❦ (a printer's fleuron, not an
asterisk in UI grey). The submit is the theme's bill-button: a pasted
mini-notice, `--red` 2px border, Fraunces 600 label "PASTE MY NAME
DOWN" (the §12 voice — booking is putting your name on the list).
Beneath it, the honest small print in Lora italic: what happens next,
in the box office's own words.

**Motion spec.** Focus: the field's ruled line inks from `--ink-soft`
to `--lampblack` and thickens to 2px (180ms `--ease-settle`); the
label takes a 1px impression shift down (the pencil pressing). Error:
on submit-with-errors, the first invalid field's line turns
`--red-deep`, a hand-drawn-style SVG proof mark (circle + caret) draws
in the sheet's right margin beside the field (300ms `--ease-squeegee`)
with a three-to-five-word note in `--red-deep` Lora italic ("the date
has passed", "a name is wanted") — drawn, because a proof mark is
struck, not faded. Submit (valid): the button slaps (§6.11), the whole
form notice takes a full impression — scale 0.995, ink deepens 6% —
and holds 500ms while the request sends (the notice is *being pasted
to the box-office wall*). Success: the form is replaced by the ticket
stub (§11) — a perforated-edge notice (dashed tear line, §6.8's
geometry at small scale) with the booking facts set as a bill:
show, date, seats, and a Fraunces reference number.

**Choreography timeline (v2).**
- Focus — t=0–180: line inks, label impresses.
- Error submit — t=0: button slap refused (scale 0.99, no sheen — a
  slap that doesn't stick); t=80–380: first proof mark draws; focus
  moves to the first invalid field at t=380 (after the mark exists —
  the reader is shown *then* taken).
- Valid submit — t=0: slap; t=0–500: impression hold (inputs
  disabled, button label changes to apparatus "PASTING…" with the
  ellipsis as three printed dots, not animated); t=response: stub
  replaces the form with a §6.5-style slap (260ms).
- Failure response — impression releases, a notice-strip (§11 alert)
  posts above the form: the box office's apology in its own voice
  (§12), form values intact. Entered data is never lost to a failed
  paste.

**State matrix (v2).**

| State | Field line | Label | Notes |
|---|---|---|---|
| Rest | `--ink-soft` 1px | Flat | The unfilled notice |
| Focus | `--lampblack` 2px, inking 180ms | Impressed 1px | One field at a time |
| Filled | Stays at 60% ink weight (line darker than untouched) | Flat | A filled line reads filled |
| Error | `--red-deep` 2px + margin proof mark + note | Flat | Persistent until corrected — errors never time out on paper |
| Submitting (form-level) | All lines at full ink | — | Whole notice impressed, inputs disabled |
| Success | Replaced by ticket stub | — | The stub is the confirmation and the receipt |
| Disabled field (a sold-out date in the select) | Line dashed | — | The date is lettered with a strike in the option list — visible, unbookable, honest |

**Breakpoint behaviour (v2).** ≥1200px: form 560px, proof marks in
the right margin (the sheet gives it 180px). 768–1199px: form 520px,
margin 120px, proof notes shorten to ≤3 words. <768px: the sheet has
no right margin — proof marks move *beneath* their field (mark + note
on one line), form goes full sheet width minus 32px, inputs stay
18px (also prevents iOS zoom), the tier radio bills stack vertically.

**Edge cases (v2).** Double submit: the impression hold disables the
button; a second click is physically refused by the state, not by a
debounce prayer. Browser autofill: filled-state line weight applies
on the `:-autofill` repaint — the notice must not look empty when it
isn't. Server validation returning an error for a field the client
passed: the same proof-mark treatment, note verbatim from the box
office's message (mapped through §12's voice table, never raw stack
language). JS off: the form is a plain HTML form posting to the box
office endpoint; errors return as a server-rendered notice with the
same proof notes as text — the theatre survives, the transaction
survives.

**Accessibility (v2).** Real `<label>`s, programmatically associated;
error notes tied by `aria-describedby`; the form carries
`aria-invalid` on failed fields and the error summary (a small notice
at the form's head listing the marks, in reading order) is focused on
failed submit before the field focus move — no, the order is:
summary announced via `role="alert"` *and* focus to first field
(§ timeline) — the summary is reachable by heading order for those
who want it. Focus ring is the theme's rule ring (§6.13). All error
meaning is carried by text + mark, never colour alone. Contrast:
`--red-deep` notes on `--paper` are 8.1:1.

**Content merge.** The form is a document of the business — the same
notice the box office would paste at the stage door. Its fields, its
proof marks, and its stub are the transaction's paper trail, styled
as the paper itself.

**Failure fallback.** Plain HTML form, server round-trip, same voices.
Every enhancement is CSS/JS over that form.

**Reduced motion.** Focus/error states apply instantly; submit skips
the impression hold and shows a static "PASTING…" apparatus line;
the stub arrives without its slap.

**Performance & mobile variant.** No loops; transitions on focus,
error, submit only. The proof-mark SVGs are three pre-authored paths.
Mobile variant is the breakpoint spec above.

**Tokens.** `--ink-soft`, `--lampblack`, `--red-deep`, `--red`,
`--ease-settle`, `--ease-squeegee`, `--dur-slap`.

### 6.17 Printer's imprint footer

**What & why.** Every broadside ever printed ends the same way: the
printer's name at the foot — *Printed by J. Catnach, 2 Monmouth
Court* — because the sheet must say who made it. The footer is that
imprint, grown to hold a modern site's legal line: set as a real
colophon-notice at the last sheet's foot, with the wall's oldest
fragment beneath it. It belongs because a footer that looks like a
SaaS sitemap would be the fiction's final tear, and because the
imprint is where this theme tells the truth about itself.

**Structure.** Centred apparatus column (Lora 500 uppercase 11.5px,
0.18em) on the final sheet, above a torn edge (§6.8 geometry, drawn
at rest): line 1, the fleuron ornament (a Fraunces ❦ at 20px,
pre-drawn); line 2, the making line — "SET IN FRAUNCES & LORA ·
PRINTED ON WALL-WORN PAPER · PASTED BY HAND" (the §12 voice);
line 3, the edition line — "SHEET n OF N · THIS WALL" plus the
visit's date lettered as a bill dateline; line 4, the house's legal
line and 2–4 text links (Imprint, Terms, Find the hall) with the
120ms rule draw. Below the sheet, on the wall itself, the oldest
fragment: a `--paper-deep` torn strip carrying half a headline from a
show nobody remembers — the wall's bedrock, present on every page.

**Motion spec.** The imprint posts with its sheet (§6.5, last slot —
the printer signs after the bills). The fleuron does not animate.
The links' rule draws are §6.11-family micro-interactions. Nothing
else moves; the foot of the wall is the quietest place on it — the
lamp (§6.10) still drifts over it, because the lamp drifts over
everything.

**Choreography timeline (v2).**
- Sheet posts — imprint arrives in the final stagger slot (+130ms
  after the sheet's last notice).
- Thereafter — rest. The imprint's timeline is deliberately the
  shortest in the theme: a signature, not a performance.

**State matrix (v2).**

| State | Imprint | Notes |
|---|---|---|
| Unposted (below fold) | With its sheet | — |
| Posted (rest) | Printed, static | The permanent state |
| Hover (links) | Rule draws beneath the link | §6.11 family |
| Focus-visible | Rule ring (§6.13) | — |
| Scrolled-past | Posted | The visitor has left the wall; the imprint remains |
| Disabled | n/a | Links are never disabled |

**Breakpoint behaviour (v2).** ≥1200px: as specced. 768–1199px:
unchanged (it was always a narrow column). <768px: the making line
wraps to two lines (never shrinks — apparatus type has a floor of
11px), the oldest fragment shortens to its headline's first three
words.

**Edge cases (v2).** A one-sheet page (a single-notice site): the
imprint sits on that sheet; the "sheet n of N" reads "THE ONLY
SHEET" — the voice rule (§12) prefers the honest joke to a false
count. Missing legal line (a pre-launch wall): line 4 carries the
house name and year only; an imprint may be brief but never absent —
the §10 gate blocks a wall with no imprint.

**Accessibility (v2).** A real `<footer>` (contentinfo) with the
links as links; the fleuron and fragment are `aria-hidden`. The
edition line duplicates §6.7's count as real text — by design, the
foot of the wall is where AT users get the paperwork the rail
decorates. Contrast: apparatus on `--paper` in `--ink-soft` is
8.9:1.

**Content merge.** The imprint is content — type credits, making
credits, edition, legal — the facts a broadside is legally and
proudly required to carry. The fragment beneath is the wall's own
oldest layer, the same yesterday §6.3 peeks at.

**Failure fallback.** Static centred text block on the last sheet.
Every link a plain link.

**Reduced motion.** Identical — the imprint never had motion to
reduce, beyond its sheet's posting (which rests under reduced
motion per §6.5).

**Performance & mobile variant.** Zero loops, zero observers of its
own. Mobile variant is the breakpoint spec above.

**Tokens.** `--ink-soft`, `--paper-deep`, `--dur-slap`.

### 6.18 The verse stream

**What & why.** The ballad itself. On verse sheets, the sheet's
headline bill **pins at the wall top** while the ballad's stanzas
scroll beneath it — the poster still showing above the verses pasted
under it, the way a broadside's top half stayed readable while its
tail was sung through and torn. Between stanzas, woodcut ornaments;
at the sheet's foot, the refrain line drifts across as a marquee
bill. It belongs because it is the theme's reason to exist: the
shout brings the crowd, but the song is what they came for, and the
song deserves the theme's most careful reading machinery.

**Structure.** A verse sheet has two zones: `.bill-pin` (the sheet's
headline bill, `position: sticky; top: 52px` — below the §6.13
index — within the sheet zone only) and `.verses` (the stanza flow,
centred 6-column measure per §4, Lora 19px/1.75). Each `.stanza` is a
`<section>` with a stanza number in apparatus type in the left
margin ("III."). Refrain stanzas carry `data-refrain` and are set in
Playfair italic — the tune coming back. The sheet foot carries the
`.refrain-band`: a single-line bill (the refrain's first line,
Fraunces 600, 28px) translating horizontally across the sheet width.
Stanza reveals: each stanza's first line is masked by a paste band
(§5) that sweeps as the stanza enters; the remaining lines are never
masked — verses are read, not unveiled line by line (§9).

**Motion spec.** Pin: sticky, no JS, no animation — the bill simply
stays, and releases at the sheet's end where §6.2 peels the whole
sheet. Stanza band sweep: 450ms `--ease-squeegee` per stanza, trigger
stanza top at 75% viewport height. Refrain band: translateX from 0 to
−(band width − sheet width) and back is **forbidden** (ping-pong is a
fairground); the band drifts one direction at 28px/s, wraps with a
torn-edge seam, loops seamlessly; it pauses on hover and on
focus-within, and it never runs while its sheet is off-screen.

**Choreography timeline (v2).**
- Sheet entry — bill posts (§6.5); stanza 1's band sweeps as it
  enters.
- Scroll — bill pins at the index line; stanzas pass beneath; each
  stanza's band sweeps 450ms as its top crosses 75% viewport height;
  the pin's shadow on the verses deepens 0→1 over the first 120px of
  pinned travel (the bill is *above* the paper beneath — light says
  so).
- Refrain stanza arrival — its Playfair italic is already set; no
  extra motion. The tune returning needs no announcement.
- Sheet foot — refrain band drifts at 28px/s while in view.
- Sheet end — pin releases; §6.2 takes the sheet.

**State matrix (v2).**

| State | Pinned bill | Stanzas | Refrain band | Notes |
|---|---|---|---|---|
| Sheet entering | Posting (§6.5) | Band-sweeping on entry | Still | Pin engages only after the bill is posted |
| Reading (pinned) | Stuck at wall top, shadow deepening then held | Scrolling beneath | Drifting if foot in view | The core state |
| Pin released (sheet end) | Scrolls away with its sheet | Last stanzas pass | Drifting | Release is a scroll position, not an animation |
| Scrolled-past | Gone with sheet | Read | Gone | — |
| Hover/focus-within band | — | — | **Paused** | A reader chasing a moving line is a design failure |
| Focus inside a stanza | Pinned as-is | The focused stanza's band completes instantly | Paused if foot in view | Focus never lands behind a mask |
| Disabled | n/a | — | — | — |

**Breakpoint behaviour (v2).** ≥1200px: full spec; pin top 52px.
768–1199px: pin top 52px; verses measure widens to 7 columns (the
tablet wall is read closer). <768px: **the pin is cut** — a pinned
bill eats a phone's reading height and the verses matter more; the
bill posts at the sheet top and scrolls away naturally, and a
one-line apparatus reminder ("THE MILLER'S DAUGHTER — continued")
appears at each stanza break in its place. Refrain band hidden
(§5's rule). Stanza numbers move inline before the first line
(the margin is gone).

**Edge cases (v2).** A very long ballad (30+ stanzas): the pin zone
is capped — after 12 stanzas the bill releases early and a fresh
small bill (the show's name + "the ballad continues") pins in its
place for the remainder; one bill holding a whole epic becomes a
fixture, not a poster. Browser without sticky support: the bill
simply scrolls — the verses lose nothing. Print: verses print in
full, bill at the head, band absent — the ballad on paper, as it
began. Stanza content shorter than expected (a two-line chorus): the
band sweep still runs — brevity is not a reason to skip the poster's
hand.

**Accessibility (v2).** Stanzas are real sections with numbered
apparatus labels that are *not* headings (the sheet's heading is its
bill); a "Ballad text only" skip link at the sheet top jumps past
the pinned bill for AT and keyboard users. The refrain band's text
exists once in the DOM in reading order (the marquee duplicates are
`aria-hidden`); the band is never the only carrier of its line — the
refrain's stanza carries it in the flow. Verse contrast is the
theme's best (§3 law 3). The pin never covers focused content: the
sticky zone's height is reserved in the scroll-margin of every
stanza (`scroll-margin-top` = pin height + index height).

**Content merge.** The stream *is* the ballad — the product a folk
audience buys. The pinned bill is the song's own poster; the band is
the song's own refrain, lettered as a bill. Nothing here decorates
anything else.

**Failure fallback.** No JS: no band sweeps (stanzas fully visible),
pin still works (pure CSS sticky), refrain band renders static and
centred. The song reads.

**Reduced motion.** No band sweeps, no marquee drift (band static,
centred, possibly wrapped to two lines), pin retained (it is a
layout state, not a motion) — but the pin's shadow transition is
instant.

**Performance & mobile variant.** Sticky is compositor-cheap; band
sweeps ride the sheets' IO; the marquee is one transform in the
shared loop, gated to in-view. Verses are text — the cheapest
content on the wall. Mobile variant is the breakpoint spec above.

**Tokens.** `--ease-squeegee`, `--dur-band`, `--lampblack`,
`--paper`.

## 7. Page application map

| Page type | The wall's treatment |
|---|---|
| **Home** | The full wall: hero sheet (§6.14), a listing sheet of notice cards (§6.15), a verse sheet carrying the current show's ballad (§6.18), the tickets sheet (§6.16), imprint (§6.17). Five sheets is the canonical home wall; a sixth sheet must justify itself to the poster. |
| **Listing** (season / repertoire) | One long wall of card sheets grouped by month, each month a sheet with its own small bill ("MARCH — THREE NIGHTS ONLY"). Cards post per §6.15; the month bills pin briefly (one viewport) as their group passes — a lesser pin than §6.18's, released without ceremony. |
| **Detail** (one show) | The show gets a whole wall to itself: its bill as hero (no competing main bill — the side bills become the *other* shows, smaller), its ballad or synopsis as the verse stream, its woodcuts large, its booking form on the final sheet. The detail wall is where §6.18's long-form pin earns its keep. |
| **About** (the company) | The wall as archive: older sheets, deliberately — the company's past productions as half-dried bills with more `--paper-deep` showing, the founding story set as a ballad (verse stream with the company's own myth in stanzas). The about wall is the one place extra torn edges are encouraged. |
| **Contact / booking** | The tickets sheet promoted to a page: §6.16's form as the hero sheet's main bill, the hall's finding-information (address, "the door is under the lamp") as small notices, the form's stub as the page's success state. No verse stream — a person booking a ticket is not here to sing. |
| **Article / news** (a review, an announcement) | The article is a single sheet: headline as a bill head (not a shout — news is Playfair's job), body in Lora at verse measure, pull-quotes pasted as small notices in the margins. Reviews from the papers are pasted as *their* bills, quoted with their paper's name in apparatus type. |
| **404** | A sheet with one notice: "THIS BILL WAS NEVER PASTED" — the lost-dog slot's layout, the dog replaced by the missing page's description if known, and the index (§6.13) offered as the way back to the wall. The joke is allowed exactly once per wall, here. |

## 8. Worked examples (v2: hero, mid-page, conversion — end-to-end)

The example client throughout: **The Goose & Firkin Theatre**, a
touring folk company, presenting the ballad opera **"The Miller's
Daughter"**. Prices: stalls £14, gallery £8, under-16s £5. The
ballad's refrain: *"Oh, the mill wheel turns, and the river runs
clear."*

### Example A — The hero: sheet 1, "THE MILLER'S DAUGHTER"

**Content.** Shout: "THE MILLER'S DAUGHTER" (Fraunces 900, two lines,
"DAUGHTER" the dropped word in `--red`). Bill head (Playfair): "A
Ballad Opera in Two Acts — sung as it was sung in the streets".
Portrait: woodcut of Marta Vane as the Daughter, lantern in hand
(duotone lampblack on `--ochre`). Data block: "FRIDAY & SATURDAY ·
8 O'CLOCK" (apparatus), prices as counters (£14 / £8 / £5), ticket
slip: "Book tickets for The Miller's Daughter". Small notices: a
lost-dog-format notice repurposed — "FOUND: one fiddle, left at the
Candlemas ball — claim at the stage door" (the company's real lost
property, because the wall's jokes must be true), and a meeting
announcement: "THE FRIENDS OF THE FIRKIN meet Thursday, all welcome".

**Scroll/load timeline.**
- t=0 — Wall paints: brick edges, hero sheet clipped in bands, index
  strip (§6.13) present, lamp (§6.10) drifting from first paint.
- t=0–450 — Band 1 sweeps: the shout arrives; at +40ms "DAUGHTER"
  drops (§6.6), landing at t≈380.
- t=200–650 — Band 2: bill head, portrait frame; portrait settles
  from t≈600 (§6.9).
- t=400–850 — Band 3: data block, prices begin counting at t≈650
  (12 steps, landing by t≈1550), ticket slip, both small notices in
  their §6.5 slots.
- t=850 — Hero fully posted and readable; index rule draws under
  "TONIGHT".
- t=2000 — Sheen dry. The visitor has been reading since t=450; the
  ceremony never once gated the words.

### Example B — Mid-page: the season listing sheet

**Content.** Sheet 3, small bill at its head: "THE SEASON — SIX
NIGHTS, SIX SONGS". Six notice cards (§6.15): The Miller's Daughter
(sold out), The Candlemas Ball, A Night of Sea Songs, The Plough &
the Stars (a new writing night), Children's Matinee: The Goose Girl,
and the Friends' Singaround (free — its data row letters "FREE" and
drops it, notice-scale, §6.15).

**Scroll timeline.**
- Sheet top crosses 20% visibility — cards post in grid order, 130ms
  stagger (70ms on mobile), each thumb settling as it lands.
- Each card's counter runs as its data row enters: prices count; the
  Singaround's FREE drops instead; the Miller's Daughter card posts
  with its price already struck and "HOUSE FULL" beneath — it does
  not count, and its corner will only peek 8px (§6.3) when hovered,
  as if its paste were old.
- The sheet's sheen dries across its first 30vh (§6.4) while the
  visitor is still reading the second row — by the time they reach
  the Singaround, the top of the sheet is wall, not news.
- Boundary out: torn edge (§6.8) draws at the lower third; the sheet
  peels (§6.2) as its bottom crosses 35% viewport height — unless
  focus is inside it, in which case the wall waits, politely, for
  the reader to leave.

### Example C — Conversion: the tickets sheet

**Content.** Sheet 5. Main bill (notice scale — conversion sheets
don't shout): "BOOKING — write plainly". The form (§6.16): name,
email, date (select: Fri 12 Dec — stalls only; Sat 13 Dec; Sat 20 Dec
— HOUSE FULL, shown struck and unbookable), seats stepper, tier
radios (Stalls £14 / Gallery £8 as two small bills). Small print:
"Names are pasted to the box-office list each morning at nine. No
names are sold, lent, or sung about." Submit: "PASTE MY NAME DOWN".

**Interaction timeline.**
- Visitor focuses Name — line inks over 180ms, label impresses.
- Submits with the date unchosen and email malformed — button refuses
  its slap; at t=80 the first proof mark draws in the margin beside
  Date: "a night must be chosen"; the email's note waits its turn
  (one mark leads; the summary notice at the form head lists both).
  Focus lands on the date select at t=380.
- Visitor corrects both, resubmits — slap lands, the notice impresses
  for 500ms ("PASTING…"), then the stub slaps in: "THE MILLER'S
  DAUGHTER · SAT 13 DEC · GALLERY ×2 · £16 · No. 0417" with its
  perforated edge — and beneath it, in Lora italic, the box office's
  last word: "Come early. The lamp is lit at seven, and the singing
  starts when the room is full."

## 9. Anti-slop — how THIS theme goes cheap, and the cure

1. **Distressed-texture wallpaper.** A stock "grunge paper" photo
   behind clean web content. *Cure:* the paper is flat tokens and
   baked wrinkle geometry (§6.10); texture that doesn't respond to
   the lamp is a photograph, and photographs are banned from the wall.
2. **Random rotations.** Notices scattered by `Math.random()` leans,
   different every load. *Cure:* the §4 rotation table — fixed,
   tokenised, learnable. A wall you can't learn is a wall you can't
   trust.
3. **Every headline shouts.** Six Fraunces Black headlines per sheet
   at full clamp. *Cure:* one shout per sheet (§3 law 1); the scale
   ladder is the hierarchy. If everything is enormous, nothing is a
   poster — it's a ransom note.
4. **Peek that reveals a tooltip.** The corner lifts and shows a
   shadow, a glow, or "Learn more". *Cure:* §6.3's fragment is a
   specific older bill, identical everywhere, with half a date. The
   peek is archaeology or it is nothing.
5. **Colour photographs in poster frames.** A glossy cast photo inside
   a woodcut frame. *Cure:* build-time duotone (§6.9, §15) — if the
   source art can't survive as linework and one flat colour, it isn't
   a woodcut and doesn't go on a bill.
6. **The marquee as a SaaS logo strip.** The refrain band reused for
   sponsor logos or testimonials. *Cure:* the band carries the
   ballad's own refrain line, only (§6.18). Sponsors get a notice
   like everyone else.
7. **Verses as decoration.** Ballad text used as filler texture,
   truncated mid-stanza, set in low contrast for "mood". *Cure:*
   §3 law 3 — full stanzas, best contrast on the page, real songs
   with real words. A ballad you can't read is wallpaper with
   pretensions.
8. **Skeleton shimmer.** The paste marks (§6.12) given a CSS shimmer
   sweep. *Cure:* wet paste is still. The marks are geometry and
   patience; the bills' arrival is the only motion.
9. **Peel everywhere.** Peeling hovers, peeling buttons, peeling
   cards. *Cure:* the peel is for sheet boundaries (§6.2) and route
   changes (§6.12) only. A gesture used on everything signifies
   nothing; the corner-peek (§6.3) is the small gesture, the peel is
   the large one, and the wall rations both.
10. **Clean sans creep.** A "helpful" UI sans sneaking into buttons,
    form fields, or the index. *Cure:* three faces, three jobs (§3).
    If a string exists on the wall, it is set in Fraunces, Playfair,
    or Lora — including error messages, including the 404.

## 10. Quality gate

No wall ships unless every item passes. Blocking items are marked ◆.

- ◆ **One shout per sheet**, at the §3 clamp; the scale ladder (§3
  law 1) visibly present on every sheet — five scales, minimum.
- ◆ **Peel safety:** with JS disabled, and again with the watchdog
  forced, every sheet is fully readable in flow; no content exists
  only mid-peel (§6.2, law 1–2).
- ◆ **The beneath fragment** (§6.3) is the same fragment under every
  poster, in `--paper-deep`, with its torn edges — verified visually
  on three different bills.
- ◆ **Counters land on true figures** (§6.15): DOM values match the
  box office's real prices/counts; AT receives final values without
  the stepping.
- **Rotation audit:** every sheet and notice matches the §4 table
  exactly; no runtime randomness in any transform.
- **Contrast sweep:** ink on paper 12.6:1, red text ≥14px only,
  ochre never text on paper; sheen-capped text zones ≥7:1 at peak
  gloss (§6.4) and at both lamp extremes (§6.10).
- **Drying is one-way:** scroll down 30vh, scroll up, re-scroll —
  no sheet re-wets, no notice re-posts, no counter re-counts.
- **Pin discipline:** §6.18's bill pins only inside its sheet zone;
  on mobile the pin is absent and the stanza-break reminders are
  present.
- **Duotone audit:** every image on a bill is lampblack + one colour;
  no photographic colour anywhere on the wall.
- **Form honesty:** §6.16 with JS off completes a booking end-to-end
  against the real endpoint; error notes match §12's voice table.
- **Imprint present** (§6.17) on every page type, including 404.
- **Performance:** §14 budgets met on the reference device; the
  shared loop writes ≤6 properties per frame with all systems live.
- **Reduced motion:** full pass with `prefers-reduced-motion` — the
  wall is posted, dry, lit, and complete; the ballad reads; the form
  books.

## 11. Component inventory (v2)

Every component a real site in this theme needs, with its wall
treatment. If a component is not listed, it is built by analogy to its
nearest listed neighbour — never by importing a foreign UI kit.

| Component | Broadside & Ballad treatment |
|---|---|
| **Primary button** | The bill-button: a small pasted notice — `--paper` fill, 2px `--red` border, Fraunces 600 uppercase label, at a −0.6° lean; §6.11 slap on press; never rounded (paper has corners), never shadowed with grey (its shadow is a paste offset in `--paper-deep`) |
| **Secondary button** | The plain notice: 1px `--lampblack` border, Lora 500 label, no lean; hover draws the rule (§6.13 family) |
| **Text link** | Lora, underlined by a rule that draws in 120ms on hover; visited links take `--red-deep` — a link you have read is a bill you have seen |
| **Text input** | §6.16's ruled line: label above, ink line below, text sits on the line |
| **Select** | A ruled line with a Fraunces ❦ marker; the open list is a small sheet (paper, lampblack border) whose options are lines of a bill; sold-out options struck in `--red-deep` |
| **Stepper** (seats) | Two small bill-buttons, "−" and "+" as wood-type sorts, flanking the figure in Fraunces 600; the figure slaps (§6.11) on change |
| **Radio group** | Side-by-side mini-bills (the tiers); the chosen bill is the one *pasted flatter* — its lean goes to 0° and its border inks to `--red`; unchosen bills keep their lean |
| **Checkbox** | A square of bare paper with a lampblack border; checked = a proof-tick drawn in `--red-deep` (300ms draw) — consent on this wall is a mark made by hand |
| **Table** (the ledger exception) | Performance ledgers (dates × availability) are set as a *playbill table*: Fraunces 600 header row, Lora rows, rules in `--ink-soft`, sold-out rows struck. No zebra striping — paper is one colour; rules do the work. This is the only table the wall permits, and §1's warning stands: data-dense products should not choose this theme |
| **Badge / flag** | A small torn strip ("LAST NIGHT", "NEW", "HOUSE FULL") pasted across a bill's corner at −12°, `--red` fill, `--paper` Fraunces 600 text; torn edges on both short sides |
| **Alert** | A notice-strip pasted above the relevant sheet zone: paper fill, 3px `--lampblack` left rule (or `--red-deep` for the box office's apologies), Lora voice per §12; dismiss = a small "tear off" text button that plays §6.8's tear at strip scale (300ms) |
| **Pagination** | "MORE BILLS BELOW" — a pasted strip at the listing sheet's foot that posts the next group of cards (§6.15) in place; numbered pagination exists only in the §6.13 index's sheet list, because walls don't have page numbers, they have more wall |
| **Modal** | A bill pasted *over* the wall on a full `--wall` scrim (the wall darkens, never blurs — blur is banned from the wall): the modal is a sheet at 0° (modal paper is held true by two hands), with its own small imprint; it peels (§6.2 mechanics, 400ms) on dismiss. Focus trapped inside; ESC = tear off |
| **Toast** | **Refused.** A toast is a notification from an operating system. The wall's equivalent is the alert notice-strip, which stays until torn off — news on a wall does not evaporate in 4 seconds |
| **Tabs** | A row of small bills along a sheet's top edge (the nights of the week); the active tab is pasted flat (0°) and ruled in `--red` beneath; panels are the sheet's own zones, posted per §6.5 when first shown |
| **Accordion** | "Folded bills": each item is a notice whose lower half is folded up (clip) until opened, when it unfolds downward (400ms `--ease-squeegee`) — the fold line is a `--paper-deep` crease that remains visible when open, because folded paper remembers |
| **Search** | A single ruled-line input (§6.16 pattern) labelled "FIND A BILL"; results post as notice cards on a fresh sheet below; the empty result is the 404 notice at search scale (§12's voice) |
| **Tooltip** | **Refused as a pattern.** Anything worth saying on the wall is printed on the wall. Where a control needs a name, it gets a visible apparatus label, not a hover secret. (The corner-peek, §6.3, is not a tooltip: it reveals paper, not help text.) |
| **Breadcrumb** | The §6.13 index *is* the breadcrumb: sheet short-titles in order, current ruled in red. Deeper hierarchies (a show inside a season) add the season's small bill above the sheet, linked — paper all the way up |
| **Avatar / person chip** | A person on this wall is a woodcut (§6.9) or a name in a bill. There are no circular photo chips; a circle crop is the one shape a bill-poster's knife never made |
| **Divider** | The torn edge (§6.8) between sheets; within a sheet, a 4px lampblack rule with a torn right end (the §6.14 rule) or bare paper — whitespace is the third divider |
| **Skeleton** | §6.12's paste marks, exact geometry, no shimmer |
| **Progress** | §6.7's brush stroke for the page; inside a form, progress is the stub's perforated edge filling with `--red` ticks per completed field group — paperwork progress, stated in fields, not percentages |

## 12. Content & copywriting voice (v2)

The wall speaks in two registers, and they never swap clothes.

**The Bill (loud register)** — Fraunces and Playfair, for headlines,
flags, buttons. Short. Declarative. Present tense. The bill does not
hedge, apologise, or say "please".

**The Hand (quiet register)** — Lora, for verses, body, errors, and
small print. Complete sentences. Kind. The hand explains what the bill
shouted.

| Slot | Voice rule | ✓ Do | ✗ Don't |
|---|---|---|---|
| Headline / shout | The show's name or the night's fact, ≤5 words at shout scale | "THE MILLER'S DAUGHTER" | "An Unforgettable Evening of Folk Magic Awaits" |
| Bill head | Playfair, the respectable facts: what, when, where | "A Ballad Opera in Two Acts" | "You won't BELIEVE this show" |
| Button | The bill's verb, first person welcome | "PASTE MY NAME DOWN" / "BOOK THE TICKETS" | "Submit" / "Proceed to checkout" |
| Label | Apparatus, uppercase, the paperwork of the wall | "SHEET 2 OF 5" / "ADMISSION" | "Step 2 of 5" / "Pricing tier" |
| Error | The hand, in the margin, naming the fix in ≤5 words beside the field; the summary in full sentences | "a night must be chosen" / "The date has passed — choose another night." | "Invalid input" / "Oops! Something went wrong" |
| Empty state | The lost-notice layout, the hand's honesty | "No bills for that night — the wall is bare. Try Friday." | "No results found." with a magnifying-glass icon |
| Success | The stub states facts; the hand adds one warm line | "No. 0417 — Gallery ×2" + "Come early. The lamp is lit at seven." | "Success! Your booking has been successfully completed." |
| Loading | The poster's lateness, in-fiction (§6.12) | "THE BILLS ARE LATE — the poster's cart is coming" | A spinner, or "Loading…" in a sans |
| Verse | Real ballad text, full stanzas, attributed where traditional | "Oh, the mill wheel turns, and the river runs clear." | Lorem-ipsum "verse" texture, or truncated stanzas |

**Banned words on the wall:** "leverage", "synergy", "solutions",
"seamless", "oops", "invalid", "submit", "content" (as a noun for the
work), and any exclamation mark in the quiet register — the hand does
not shout; the bill does not need punctuation's help.

**Numbers** are always real and always wood-type where they are
figures of the house (prices, counts, dates). A number the box office
cannot stand behind does not go on the wall — the Real Content rule
wears a poster's apron here.

## 13. Full-page scroll choreography map (v2)

The canonical home wall (§7), top to bottom. Every beat names what the
visitor sees and what it is *for*; a beat with no purpose is cut, not
kept.

| # | Beat | What happens | What the visitor feels / learns |
|---|---|---|---|
| 0 | First paint | Wall, index strip, hero bands clipped, lamp already drifting | A wall exists; something is being posted |
| 1 | 0–850ms | §6.1 paste-up; "DAUGHTER" drops (§6.6); portrait settles (§6.9) | The show arrives by hand, not by server |
| 2 | 850–2000ms | Prices count (§6.15); sheen dries (§6.1); index rule draws | The bill is real: dates, prices, a way to book |
| 3 | Hero reading | Lamp drifts (§6.10); small notices wait with their peeks (§6.3) | The wall has a past (first peek discovery) |
| 4 | Sheet 1 boundary | Torn edge draws (§6.8); sheet 1 peels (§6.2) | Leaving a poster is physical; there is more wall |
| 5 | Sheet 2 (season) posts | Cards stagger in (§6.5/§6.15), thumbs settle, counters land per row | The season is a wall of bills, each with its price |
| 6 | Sheet 2 drying | Sheen scrubs off across 30vh (§6.4) while row 3 posts | Time passes on paper; the top of the sheet is already history |
| 7 | Sheet 3 (ballad) entry | Bill posts; pin engages (§6.18) | The shout stays; the song begins |
| 8 | The long read | Stanzas band-sweep one by one beneath the pinned bill; refrain band drifts at the sheet foot | The theme's heart: commerce holding the frame, art filling it |
| 9 | Sheet 3 end | Pin releases; peel takes the sheet | Even the song ends; the wall continues |
| 10 | Sheet 4 (company) | Archive bills post with heavier `--paper-deep` show-through | The company's past is literally underneath its present |
| 11 | Sheet 5 (tickets) | Booking notice posts; form rests, lines bare | The ask, made of the same paper as the art |
| 12 | Booking | §6.16's timeline: ink, proof marks, impression, stub | Conversion feels like being written onto the list by hand |
| 13 | The foot | Imprint (§6.17) under the lamp's drift; the oldest fragment below the sheet | The wall tells the truth about who made it; the day ends |

**Reverse pass.** Scrolling up retraces the map with everything dry,
posted, counted, and peeled state preserved (law 3) — the wall on the
way back is the wall as the visitor left it, which is how they know
it is *the same wall*.

## 14. Whole-page performance budget (v2)

Reference device: a mid-range Android (the wall's audience books from
phones outside venues) on 4G, plus a desktop check.

| Budget line | Limit | Notes |
|---|---|---|
| Initial HTML + CSS + JS | ≤ 210KB total (JS ≤ 45KB gz) | The wall is mostly paper and type; weight has no excuse |
| Fonts | ≤ 3 families, ≤ 6 files, ≤ 150KB | Fraunces (2 weights), Playfair (1 + italic), Lora (2 + italic), subset to Latin + the ❦ fleuron's slot |
| Images | ≤ 120KB per woodcut, ≤ 5 woodcuts above the fold of their sheet | Duotone art compresses well; a woodcut over budget is redrawn smaller, never re-encoded blurrier |
| First paint | LCP ≤ 2.2s (the shout, set in fallback serif if fonts lag — law 5) | The shout is the LCP element by design |
| Frame budget | Shared loop ≤ 2ms script per frame with lamp + drying + one spring live | All scrubbed values are transform/opacity/custom-property writes |
| Long tasks | None > 50ms after load; the paste-up is CSS-driven | Counters and staggers ride the loop/IO, never bespoke timers (law 4) |
| Layout stability | CLS ≤ 0.02 | Skeleton marks reserve exact geometry (§6.12); rotations and drops are transform-only |
| Interaction | INP ≤ 200ms; the slap never gates an action (§6.11) | — |

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead): 1) hero dust motes (§6.10); 2) lamp drift amplitude
(±6°→±3°, then static); 3) parallax wall drift; 4) refrain marquee
(band renders static); 5) portrait blur phase (scale-only settle);
6) corner-peek overshoot (lift without spring). **Never cut:** the
watchdog and fallbacks (law 2), the no-JS readability of any sheet,
reduced-motion variants, the form's plain-HTML path, contrast caps
on sheen/lamp. A wall that is fast but can hide its words has failed
at the only job that matters.

## 15. Build-order checklist (v2)

Build in this order; each step assumes only verified earlier steps.

1. **Tokens first.** Colours (§2, incl. derived + wall), type scale
   (§3), leans (§4), easings and durations (§5) as CSS custom
   properties. Nothing visual before the tokens exist.
2. **The static wall.** Sheets, bills, verses, imprint — fully
   readable with no JS and no motion. Pass the §10 no-JS items now;
   they are never cheaper to fix later.
3. **Duotone art pipeline.** Woodcut preparation (linework + one flat
   colour), per-portrait fallback initial blocks (§6.9), image
   budgets enforced in the asset step.
4. **The wall layer.** Brick edges, older-sheet protrusions, torn
   fringe clips (§6.8 geometry) — the archaeology before the weather.
5. **Index + imprint.** §6.13 and §6.17 — the wall's paperwork, so
   navigation exists before any sheet performs.
6. **Posting system.** §6.5's stagger + §6.1's bands on the hero,
   with the watchdog (law 2) wired before the first animation is
   tuned. Band-boundary rule enforced: no notice straddles a band.
7. **The shout.** §6.6's drop, synchronised to §6.5; verify law 5
   (shout readable ≤450ms or by watchdog).
8. **Counters.** §6.15's stepped figures with final values in the DOM
   and the AT span in place.
9. **Peel + strip.** §6.2 and §6.12, including the focus-refusal and
   catch-up rules; test fast scroll and keyboard jumps now, not at
   the end.
10. **Peek, tilt, slap.** §6.3 and §6.11 on the shared spring; the
    `.beneath` fragment audited identical under every bill.
11. **Scrubbed systems.** §6.4 drying and §6.7 brush stroke into the
    shared loop; zoning caps for sheen-over-text verified.
12. **The verse stream.** §6.18 pin + stanza bands + refrain band;
    mobile pin-removal and stanza reminders verified at <768px.
13. **The lamp.** §6.10 last of the motion systems (it is atmosphere;
    it must never be load-bearing in a test written earlier), with
    its contrast sweep at both drift extremes.
14. **The form.** §6.16 over its plain-HTML path: states, proof
    marks, stub, server-error mapping through §12's table.
15. **Reduced-motion + print passes.** Every element's reduced
    variant checked against its spec; print stylesheet (all sheets
    posted, no rails, no pins) verified.
16. **The gate.** Full §10 pass on the reference device (§14),
    including the scroll-down/up/down drying audit. Only then may
    the wall be called a wall.
