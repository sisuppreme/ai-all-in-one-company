# Theme 086 — The Drift Buoy Network (50x Expansion)

*Four hundred drifting buoys reporting from every ocean. The site is a live chart of wanderers: each buoy has a small biography, and the network's story is told by things that drift, report, and eventually fall silent. Nothing on this page is a map illustration — it is a working chart, kept by an office that writes everything down and rounds nothing.*

---

## 1. Concept & world

A drift buoy is a small orange machine the size of a beach ball, dropped from a ship's stern into open ocean with a drogue — an underwater sail — hanging fifteen metres below it. It has no engine, no steering, and no destination. It goes where the water goes, and every few hours it wakes, fixes its position, measures the sea's skin temperature, and radios home: *I am here. The water is this warm. My battery is this full.* Then it sleeps, and drifts. A network of hundreds of them is how humanity actually knows the surface currents — not by modelling the ocean, but by asking things that are lost in it, politely, for years. The Drift Buoy Network builds a website inside that fact. The page is a chart table in a chart office: bathymetry contours and a graticule under everything, report cards stamped as they arrive, and one chosen buoy — the page's protagonist — whose whole told life the visitor reads by scrolling. Its wandering drift line draws down the margin as the story advances. Its weekly reports arrive stamped, and the stamps grow fainter as its battery dies. Its battery figure, pinned beside the reader the whole way down, counts *down* as the reader's progress counts up. And at the bottom of the page the story does the thing the whole theme exists to do: the buoy stops answering. The final section is half a report, a timestamp, white space, and one line — BUOY 22914 — SILENT SINCE MARCH. DRIFTING STILL. No animation performs there. The line simply stops.

The mood is patient, exact, and quietly elegiac — a hydrographic office that loves its instruments. This is not a "live data dashboard" skin with a map hero and glassmorphism stat cards, and it is not a screensaver of a rotating earth. Everything on the chart is either a reading, a record, or an artefact of the office that keeps the record: stamps, cards, ledgers, tallies. The theme's emotional engine is accounting. A reader who finishes the page has watched a machine spend its entire battery telling the truth about where it was, and the page honours that by never once inventing a number the buoy did not send.

**The theme's one law: the chart records only what was transmitted.** Every position, temperature, battery figure, distance, and count on the page traces to the one declared voyage ledger (§6.17) — the chosen buoy's deployment record and its forty weekly transmissions plus one fragment — or to the fleet record printed beside it (412 buoys in the network, 401 reporting, 11 silent). The drift line draws only between transmitted positions; it never extrapolates past the last one, and its projected continuation is refused outright (§6.2). The battery never resets, never estimates, and never counts from a number the buoy did not send. A figure the network did not receive is printed as a gap — an em dash, a half-finished coordinate — never filled in by a helpful designer. If a reading cannot be loaded, the page prints the last received value and labels it LAST KNOWN. The chart would rather show a hole than a guess.

**Best-fit sites and audiences.** Ocean and climate data programmes (drifter fleets, Argo-style float networks, tide and current services); satellite-IoT and maritime telemetry companies whose product is exactly this — small machines reporting from far away; environmental monitoring networks (air, water, glacier, wildfire sensors) that need their remoteness to feel like a virtue rather than a limitation; research-vessel and expedition sites; ocean-conservation campaigns that fund hardware; open-data portals that publish instrument records and want the records to read like literature. The audience is literate and patient: scientists, sailors, funders, students, and the kind of citizen who adopts a buoy the way other people adopt a highway. They will check the arithmetic. The theme is built to survive being checked.

**When NOT to use it.** Not for anything that must feel fast or urgent — the network's quickest honest event is a 700ms signal delay, and the theme's whole posture is that the ocean answers slowly. Not for a product with no instruments, no telemetry, and no records: if the client cannot name the things that report and what they report, there is nothing for the chart to keep, and the theme collapses into a map skin (see §9). Not for dense e-commerce or anything with a checkout that must convert in seconds; the conversion surface here (§6.13) is a follow-a-buoy signup, deliberately unhurried. Not where legal or marketing will demand rounded, inflated numbers — "over 400 buoys!" — because the law forbids the rounding and the theme's credibility is the count. Not for a story with no ending: the theme's signature is that its protagonist falls silent, and a client unwilling to let anything on their homepage *end* should choose another theme.

**The world, concretely.** The chart office has: the chart itself (graticule, contours, buoy dots), the roll-call (buoys reporting in), the margin rail where the chosen buoy's drift line draws and its ID card pins, the weekly report cards and their stamps, the fleet table (every buoy, one row each), biography cards for individual buoys, the follow-a-buoy form whose confirmation is itself a stamped report card, the voyage ledger (§6.17) from which every figure is drawn, and the last transmission — the one section where the office stops performing and simply leaves the record open. Every element in §6 is one of these things. Nothing enters from outside the world: no toast, no spinner, no generic stat card; §11 gives each ordinary component its chart-office treatment or refuses it.

---

## 2. Palette

Five anchors, taken unchanged from the theme's original entry. The ground of the page is ocean chart — the pale green-grey of a printed nautical chart, paper that has been at sea. Deep water is the chart's printed depth colour and the theme's structural voice: headlines' rules, the ID card, the footer — a green so dark it is nearly a second ink. Buoy orange is the hardware: the one colour that is a physical object (every buoy in the fleet is painted it), spent on dots, rings, the chosen buoy's marker, and nothing else. Signal green is the network answering — received-transmission marks, the reporting state, live tallies. Log ink is the office's handwriting colour become print: all body text and every stamp.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--chart` | `#DCE8E4` | Page ground; chart paper; the sea as printed | ~52% of surface | Ground for `--ink` text: **11.3:1** — the page's default text pairing |
| `--deep` | `#1F4E4A` | Structure: ID card, rules, footer, table heads, the night chart's ink | ~16% | On `--chart`: **7.4:1** — text permitted at all sizes; `--chart` on `--deep` also 7.4:1 (the ID card's pairing) |
| `--buoy` | `#E86A17` | The hardware only: buoy dots, ripple rings, the chosen marker, the stamp's buoy glyph | ≤4% | On `--chart`: **2.6:1** — graphics only, never text; on `--deep`: 2.9:1, same ruling |
| `--signal` | `#3E7A4E` | Received marks: report ticks, live tallies' glyphs, the reporting pulse | ~5% | On `--chart`: **4.1:1** — glyphs and large data only; running text uses `--signal-deep` (below) |
| `--ink` | `#2B2B28` | All body text; stamps; coordinates; the log's voice in print | ~20% | On `--chart` 11.3:1 (AAA); on `--chart-lit` 13.0:1 |
| `--chart-lit` | `#F2F6F3` | Raised paper: report cards, biography cards, the form leaf | derived | With `--ink`: 13.0:1; with `--deep`: 8.6:1 |
| `--chart-deep` | `#C4D6CF` | Recessed chart: table striping, skeleton soundings, the margin rail's ground | derived | With `--ink`: 9.4:1 |
| `--abyss` | `#14332F` | Night-watch ground (dark scheme); the deepest bathymetry band | scheme only | With `--chart` text: **10.8:1** |
| `--signal-deep` | `#2E5C3B` | Signal green made legible: status words, received-line text | derived | On `--chart`: **6.2:1** — text permitted |
| `--orange-deep` | `#A34708` | Buoy orange made legible: warning words, the LOW BATTERY line | derived | On `--chart`: **4.8:1** — text permitted (AA) |
| `--contour` | `#9FBCB2` | Bathymetry contour lines and graticule hairlines on `--chart` | derived | Graphic only — contours are geography, never information carriers |
| `--contour-night` | `#3D6B62` | Contours and graticule on the night chart | derived | Graphic only |

**Contrast method.** Ratios above are computed from the hex values by the WCAG relative-luminance formula for this expansion, not estimated. Two forbidden pairings are load-bearing and are checked in the quality gate (§10): `--buoy` as text anywhere (2.6:1 on the ground — the orange is a painted object, and painted objects are not lettering), and `--signal` on `--deep` (1.8:1 — a received-mark must never be set on the ID card's ground; the card's received ticks are `--chart` and its live dot is `--buoy`). A builder who sets a paragraph in signal green, or a caption in buoy orange, has broken the theme even if the page "looks nautical."

**Dark behaviour — the night watch, not an inversion.** Under `prefers-color-scheme: dark`, the office goes on night watch: the page ground becomes `--abyss`, the graticule and contours switch to `--contour-night`, and body text becomes `--chart` on the abyss (10.8:1). The report cards and biography cards stay `--chart-lit` paper — they are paper, pinned to the night chart, and paper does not change colour because the room darkened. Buoy orange keeps its hex exactly (a buoy is orange at 2 a.m. too) and gains contrast on the dark ground (4.2:1 — still graphics-only). The pinned ID card inverts its own pairing honestly: it becomes a `--chart` card with `--deep` structure and `--ink` text, because the card is a printed artefact, not a screen. There is no fully-dark content surface in either scheme: in this theme, everything readable is printed on paper, day or night.

**Colour discipline.** Orange is rationed like hardware: it appears where a buoy physically is (a dot, a marker, a ring it emitted, the glyph in a stamp) and nowhere else — never as a link colour, a button fill, or a headline accent. Signal green means exactly one thing — *a transmission was received* — and is spent only on received marks and the tallies that count them; a green "success" flourish on a form would spend the meaning, so the form's confirmation is stamped in ink (§6.13). Deep water is structure, not atmosphere: it frames and heads things; a full-bleed deep-water section background is forbidden except the footer, which is the office's desk at the bottom of the chart.

---

## 3. Typography

Three families, exactly as the original entry specifies — Archivo for display, Newsreader for body, JetBrains Mono for the machine's voice (buoy IDs, timestamps, battery, coordinates). No fourth family is added; the stamp's lettering is Archivo at inscription settings, and the office's handwriting does not exist — this office types its log.

- **Archivo** — display. A grotesque with a chart-title's confidence; used for headlines, the chart title, report-card heads, and the fleet table's group heads. Its tabular lining figures are *not* used for data — data is mono's job (Type law 1).
- **Newsreader** — body. An old-style serif with optical sizing that reads like a well-kept logbook; body text, buoy biographies, report-card prose. Its italic is the biography voice (§12) — the human note inside the machine's record.
- **JetBrains Mono** — the machine voice. Every buoy ID, timestamp, coordinate, battery figure, drift distance, and tally, with tabular numerals always engaged. When mono speaks, a buoy or the office's instruments are speaking.

**The type scale** (root 16px):

| Role | Size / line-height | Family & settings | Used for |
|---|---|---|---|
| Display 1 | 58px / 1.04, −0.015em | Archivo 640 | The chart title (hero headline), once per page |
| Display 2 | 40px / 1.1 | Archivo 600 | Section heads: the fleet, the silence |
| Display 3 | 28px / 1.16 | Archivo 580 | Report-card heads, biography names |
| Heading | 20px / 1.35 | Archivo 600 | Sub-heads, table group heads |
| Body | 17px / 1.65 | Newsreader 400 | All reading text; measure capped at 64ch |
| Body small | 15px / 1.6 | Newsreader 400 | Card bodies, secondary text |
| Biography | 16px / 1.62, italic | Newsreader italic 400 | Buoy biographies — the human note (§12) |
| Caption | 13px / 1.5 | Newsreader 400 | Chart notes, figure notes |
| Inscription | 12px / 1.45, +0.13em, uppercase | Archivo 600 | Stamps' fixed lines, card eyebrows, table heads — the office's rubber-stamp register |
| Data | 14.5px / 1.5, tabular | JetBrains Mono 500 | Coordinates, timestamps, battery, distances, tallies |
| Data large | 22px / 1.3, tabular | JetBrains Mono 500 | The pinned card's battery figure, hero tallies |

**Type laws.**
1. **If a machine sent it, mono sets it.** An ID, a coordinate, a timestamp, a battery percentage, a drift distance, a count of buoys — JetBrains Mono, tabular, with its unit or label attached (`BATTERY 65%`, `DRIFT 2,690 KM`). A number set in Archivo or Newsreader is a number a human made up, and the page has none of those.
2. **Coordinates print as the buoy sent them** — degrees and minutes with the prime and hemisphere letter: `29°58′N 070°44′W`. Never decimal degrees on the chart (an API response is not the chart), never rounded to whole degrees, and a coordinate the buoy failed to finish prints unfinished: `41°0—′N` (§6.9).
3. **Numbers are never rounded for drama.** The network is 412 buoys, not "400+". The drift is 5,603 km, not "over 5,600". The battery is 4%, not "nearly empty" — the *copy* may say the buoy is dying; the *figure* says 4%. (§12 fixes where each voice may speak.)
4. **Headlines name water, weather, and work** — currents, storms, reports, silence — in Archivo, sentence case, at most eight words. The chart does not shout: Display 1 appears once, and no headline anywhere uses an exclamation mark.
5. **The stamp is a type setting, not an image.** Stamp text is live Archivo inscription text inside a bordered, slightly rotated frame — selectable, translatable, and set at the opacity the battery dictates (§6.3). A stamp rendered as a PNG is a forgery of the office's paperwork.

---

## 4. Layout language

**The chart table.** The page is one continuous chart, max width 1480px, laid over a bathymetry field (§6.8): contour lines and a graticule (hairlines every 80px in `--contour` at low alpha, heavier every 400px with minute ticks at the page edges — the chart's frame) under all content. On desktop (≥1200px) the composition is two columns: a **margin rail** of 300px at the left, and the **chart column** holding the sections. The rail is the theme's signature furniture: the chosen buoy's ID card pins at its head (§6.4), and its drift line draws down the rail's centre (§6.2) for the whole length of the story, passing each report section as the line reaches it. The rail is not a sidebar with widgets; it is the chart's margin, where navigators have always written the voyage. On tablet the rail narrows to 220px and the card pins above the line; on mobile the rail dissolves — the card becomes a sticky strip at the top of the viewport and the drift line moves *behind* the report cards as a left-edge track (24px gutter), still scrubbed, still stopping where it stops.

**Grid and rhythm.** 12 columns at ≥1200px (gutters 32px), 8 at 768–1199px, 4 below 768px. Vertical rhythm is the *report rhythm*: each weekly report card is separated from the next by 120px of open chart on desktop (88px tablet, 64px mobile) — open water between transmissions, because a week of drifting is mostly nothing happening, and the layout says so. Whitespace here is ocean: it is the medium the story travels through, and it is never "filled" with decoration, related links, or promotional ballast. The graticule is sacred: content may cross it, sit on it, be ruled by it — nothing may delete it locally to make a section "cleaner."

**Density rules.** One report card per viewport-height, roughly — a card's prose is capped near 300 words (§12) so the stamp, not the scroll, marks the week's passing. The fleet table (§6.12) prints 25 rows per page of itself; the full 412 are never dumped into the DOM as one scroll. Biography cards (§6.11) come in rows of three at most. The hero chart (§6.1) holds at most 14 buoy dots in its reporting-in sequence — the roll-call is a sample of stations, and the caption says the count is fleet-wide (§6.18), so the chart never pretends 14 dots are the network.

**Section choreography (summary; full map in §13).** Hero: the fleet reports in; the chosen buoy's card rises last, without a ripple, marked LAST KNOWN. Then the story column: eight printed weekly reports (W01–W40 of the ledger) with the drift line drawing and the battery falling beside them; the storm leg at W19 widens the line's wander; the Stream leg at W25 straightens and speeds it. Then the fleet itself (biography cards, the table), the follow-a-buoy form, and finally the last transmission — after which the drift line has stopped, the battery reads NO SIGNAL, and the footer prints the office's totals on deep water. The page's geography descends: surface chart, deepening contours, silence.

---

## 5. Full motion system

All motion in the network is one of five physical behaviours, each with a named easing. There is no generic "fade-up" anywhere in the theme: things report, drift, ripple, stamp, or flip — the five things buoys and chart offices actually do.

**Named easings.**
- `--ease-current` — `cubic-bezier(0.45, 0.05, 0.35, 1)`: a current-borne glide — slow to start, never stopping sharply. The drift line's hand, the pinned card's week changes, hover drifts.
- `--ease-ripple` — `cubic-bezier(0.2, 0.6, 0.3, 1)`: a ring leaving a centre — fast birth, long decelerating expansion, fading as it widens.
- `--ease-flip` — `cubic-bezier(0.3, 1.3, 0.4, 1)`: an ID card flipping up from the chart's bottom edge and slapping flat, with a small overshoot settle.
- `--ease-stamp` — `cubic-bezier(0.85, 0, 0.6, 0.3)` with an impact beat: the stamp falls fast, lands, and breathes once (scale 1.04 → 1.0 in 90ms) — paperwork being struck, not UI appearing.
- `--ease-drift` — `cubic-bezier(0.4, 0, 0.2, 1)`: small office movements — link underlines, card lifts, the rail marker's travel.

**The one loop.** Every scroll-scrubbed or continuous value — drift-line draw progress, battery figure, bathymetry tone, stamp arming, ripple phases, tally values during a settle — is driven by a single `requestAnimationFrame` loop that lerps each registered value toward its target at **0.09** per frame (the heaviest lerp in the library's chart themes: a current does not hurry). No scroll handler writes a style. The loop sleeps when the tab is hidden, and when every registered value is within 0.001 of target and no ambient behaviour is armed; ambient ripples (§6.7) keep it awake only while the hero chart or fleet chart is within one viewport of the reader.

**Motion terms, in the network's language.**
- *Scroll-triggered reveals:* report cards do not reveal — they **arrive**. A card's content is printed in full from first paint; what scroll triggers is its *stamp* (§6.3), landing when the card's head crosses 70% of the viewport height — the office acknowledging receipt of a week the reader has just read.
- *Scroll-driven / scrub animation:* the drift line's draw (§6.2), the battery's descent (§6.4), and the bathymetry's deepening (§6.8) are all pure functions of one story-progress value `p` ∈ [0, 1] measured across the story column — scrubbed, reversible, exact in both directions.
- *Parallax:* three depths only — graticule at 0.94×, contours at 1.0×, buoy dots on the hero chart at 1.05× (the buoys ride *on* the water, slightly proud of the paper). The report cards never parallax; paperwork lies flat.
- *Pinned sections:* the ID card pins at the margin head for the story's whole length (§6.4); the fleet table's header pins inside its frame (§6.12). Nothing else pins — a chart office has two hands, not twelve.
- *Smooth scrolling:* native, with the loop's 0.09 lerp supplying the felt drift; `scroll-behavior: smooth` for in-page jumps (fleet index → a buoy's card), which the scrub treats as teleports (§6.2's jump rule).
- *Progress indicator:* the drift line itself, with the battery as its cost — progress you can watch being spent (§6.2, §6.4). There is no progress bar anywhere in the theme.
- *Staggered + masked reveals:* the hero's roll-call is the stagger (stations calling in sequence, §6.1); headlines settle line by line through a chart-rule mask — a `--deep` hairline under each line that the line rises past (400ms, `--ease-current`, 90ms stagger). Report prose never masks; it is printed.
- *Kinetic typography:* refused, with one exception — mono digits in the tallies and the battery (§6.18, §6.4) count, because instruments count. Headlines do not move; a chart title is not a ticker.
- *Marquee:* **refused.** Nothing on a chart scrolls sideways forever. The fleet is a table (§6.12), not a ticker.
- *Counters:* §6.18 — tallies travel from the previous true value to the new true value and hold; the battery counts *down* (§6.4), the only counter in the library that is allowed to fall, because falling is its truth.
- *SVG line-draw:* the drift line (§6.2); the sounding skeleton's contours (§6.14); the footer's miniature route (§6.15).
- *Image scale-in-frame:* deployment photographs on biography cards scale 1.05 → 1.0 inside their chart frames (§6.11) — a photograph being laid flat on the chart, not a zoom.
- *Hover / micro-interactions:* the ripple-answer (§6.5) — hover is a hail on the network's own protocol; links deepen to `--orange-deep` with an underline drawn left-to-right in 240ms; buttons press like a stamp key (§11). Magnetic pull and tilt are **refused** — charts lie flat and buoys do not lean toward visitors.
- *Custom cursor:* **refused** — normal system cursor only, per standing rule. The visitor's hand is on the chart, not replaced by a gadget.
- *Skeleton loading:* the sounding (§6.14) — the chart prints as unsounded water: contour ghosts and card outlines with their labels already set.
- *Page transitions:* the chart veil (§6.14): a contour wipe crosses, the new page's chart is already printed beneath it.
- *Reduced motion:* §6 passim — the full track charted, every report printed and stamped at rest, the battery stated as its range, no ripples, no roll-call; the network at rest is a complete chart.

**Ambient loops — exactly one licensed.** The ambient report ripples (§6.7). They pause off-screen and die under reduced motion, and no second loop may be added: a chart with two things moving on their own is a toy; with one, it is a network at work.

---

## 6. Signature elements

The nine original signature elements (§6.1–§6.9) are deepened, never redesigned. §6.10–§6.18 are the page-family elements the original layout implies — the chart's navigation, biography cards, the fleet table, the follow-a-buoy form, the sounding and veil, the footer, the uncharted page, the voyage ledger itself, and the honest counters. All eighteen draw every figure from the one ledger (§6.17). Where a number appears in an element's spec — a battery percentage, a distance, a delay — it is the number that element ships with.

### 6.1 Reporting-in hero (the roll-call)

**What & why.** On load, the chart is still, and then the network calls in. Fourteen buoy dots across the hero chart report in sequence: each emits a ripple ring and its ID card flips up briefly along the chart's bottom edge, like stations answering a roll-call, then settles back. Thirteen of them are live reports — the fleet tally (§6.18) climbs 388 → 401 as they call, because the roll-call was already running before the visitor arrived and these are its last stations. The fourteenth card rises last and stays raised: BUOY 22914, the chosen buoy. It sends no ripple. Its card is raised by the page, not by the buoy, and it is marked LAST KNOWN — the hero's whole thesis in one beat: a network of the living, and one the office keeps on the chart by hand. It merges with content because the hero *is* the network doing its job; remove the roll-call and the chart is a picture of a map.

**Structure.** An inline SVG chart (viewBox 1200×640) over the bathymetry field: graticule, contour paths, 14 buoy dots positioned from the fleet record's hero sample, each dot a `<g>` with a circle and a ripple `<circle>` animated by the shared loop (radius and opacity as registered values, not CSS animations, so the watchdog can settle them). The ID cards are a DOM strip along the chart's bottom edge — real text, one card per hero buoy, flipped with a CSS transform driven by a loop-registered value. Beneath everything, the chart ships as a static printed SVG (the no-JS layer) with all 14 dots and 22914's card already raised in the DOM strip.

**Motion spec.** Sequence begins at first paint + 400ms. Each station: ripple expands 0 → 46px radius over 900ms (`--ease-ripple`), opacity 0.55 → 0; the dot brightens to full `--buoy` at the ripple's birth; its card flips up (rotateX −88° → 0°, 380ms, `--ease-flip`), holds 700ms, settles back to a 12° rest tilt (200ms, `--ease-drift`). Station interval: 260ms, staggered by the record's order, not by screen position — the roll-call follows the fleet list, and two adjacent dots may answer far apart in time. Total sequence ≈ 4.9s. The tally climbs in step (§6.18). 22914's card rises at sequence end + 500ms, slowly (900ms, `--ease-current`), no ripple, no brightening — its dot stays at rest tone, because the office, not the buoy, is moving.

**Choreography timeline.** 0ms static chart complete, all cards printed in the strip · +400ms station 1 ripples · +660ms station 2 · … · +3520ms station 13 ripples; tally reaches 401 · +4220ms last live card settles · +4720ms a held stillness (500ms of nothing — the office listening) · +5220ms 22914's card begins its slow rise · +6120ms card raised, LAST KNOWN line visible; ambient ripples (§6.7) arm.

**State matrix.** *Rest (pre-trigger):* static chart, all dots printed, 22914's card raised — the page is complete in this state. *Calling:* as above; the chart is not focusable and pointer events pass through the ripple layer. *Settled:* ambient ripples arm; hover hands over to §6.5. *Scrolled-past:* the sequence never replays; returning to the top shows the settled chart. *Disabled (no JS):* the static layer is the hero. *Touch:* identical — the roll-call is time-triggered, never pointer-triggered, on every device. *Repeat visit:* a `sessionStorage` flag replays only the short form (tally already at 401, cards printed, 22914's card raised; no sequence) — the office does not re-perform the morning roll-call for a visitor who was just here.

**Content-merge.** The fourteen dots are fourteen real buoys from the fleet record, with real IDs on their cards; the tally they feed is the fleet's true reporting count (§6.17); the raised card is the protagonist of the story column below. The hero is not an illustration of the network — it is a window onto its first five seconds.

**Breakpoints.** ≥1200px: chart 1200×640, 14 dots, card strip along the bottom edge. 768–1199px: chart 100% × 480px, 10 dots (the record's first 10 hero stations; the tally still climbs the same 13 — the caption's count is fleet-wide, and the strip shows a "+3 MORE CALLED IN" card so the arithmetic stays honest), card strip wraps to two rows. <768px: chart 100% × 340px, 6 dots, station interval 200ms, cards become a horizontally scrollable strip pinned under the chart; 22914's card is the strip's fixed last card, always visible.

**Edge cases & failure modes.** Slow device: if the first 30 frames average >24ms, ripple count per station drops to one ring and the interval compresses to 180ms — the roll-call still completes in ≈4s. Tab hidden mid-sequence: the loop sleeps; on return, if elapsed >5000ms the sequence snaps to settled (watchdog state) rather than resuming a stale roll-call. A hero buoy whose record is missing (data failure): its dot does not render and its card prints `BUOY ——— — NO RECORD` — the fleet tally is unaffected because the tally reads the fleet record, not the dots. Content longer than expected: the card strip caps at 14 cards by construction; the fleet's other 398 buoys live in §6.12, never in the hero.

**Fallback & watchdog.** The static chart and the raised 22914 card are in the DOM from first paint; the animated layer only adds ripples and flips on top. **Watchdog: 5000ms** from sequence start — if the sequence has not completed (loop stalled, rAF throttled), all cards snap to their settled states, the tally snaps to 401, and ambient ripples arm. With JS disabled, the static hero is simply the hero.

**Reduced motion.** No roll-call: the static chart, the tally printed at 401, 22914's card raised with its LAST KNOWN line. The hero is a photograph of the network at work.

**Accessibility.** The SVG chart is `aria-hidden="true"`; its meaning is carried by real text beside it: the chart title (an `<h1>`), and a printed summary line — "401 OF 412 BUOYS REPORTED IN THE LAST 24 HOURS. 11 ARE SILENT." — in the data register. The card strip is a list with real list semantics; 22914's card carries its LAST KNOWN status as text, not colour. Focus order never enters the chart.

**Performance & mobile variant.** Ripple/dot updates are the only per-frame cost: ≤0.5ms/frame at 14 stations on a mid-tier laptop; ripple circles are compositor-friendly SVG attributes updated via the loop, zero allocation. Mobile: 6 dots, ≤0.3ms/frame. The static chart SVG is ≤9KB gzipped.

**Tokens.** `--chart`, `--deep`, `--buoy`, `--signal`, `--ink`, `--ease-ripple`, `--ease-flip`, `--ease-current`, `--hero-chart-h: 640px`, `--rollcall-interval: 260ms`, `--ripple-max-r: 46px`.

### 6.2 The wandering drift line (margin progress)

**What & why.** The chosen buoy's track draws down the margin rail, scrubbed to scroll — not a straight rule but a meandering path whose wander amplitude is the weather: it swings wide through the storm legs (W19 at ×2.2 amplitude, W31 at ×1.8), runs fast and nearly straight through the Stream leg (W25, ×1.4, drawn with longer strides), slackens in the final leg (×0.6), and stops — mid-margin, mid-ocean — at the last transmitted position. It is the page's progress indicator, and it merges with content absolutely: the line *is* the voyage, drawn between the eight transmitted positions of the ledger (§6.17), passing each weekly report section at the moment the reader reaches it. A reader always knows where they are in the story by where the line has got to — and what it cost to get there is printed in the battery beside it (§6.4).

**Structure.** An SVG path in the rail (desktop: 300px wide, full story height; the path's viewBox is 300 × story-height in px, preserved by `preserveAspectRatio="none"` on the vertical axis only via a viewBox matched to the rendered height at build time — the path is generated from the ledger's eight positions mapped onto the story column's section offsets, so the line passes each report card's head exactly at that card's scroll threshold). The path is drawn with `stroke-dasharray`/`stroke-dashoffset` as a loop-registered value driven by story progress `p`. Waypoint dots at each transmitted position (small `--deep` circles, the W40 terminus in `--buoy`), each with its week label in the inscription register. The full path ships pre-rendered in the DOM at full draw (the fallback layer); JS re-arms it to zero-draw only after the loop's first frame confirms it can animate.

**Motion spec.** Draw progress = `p`, the story-progress value: 0 when the story column's first report reaches 60% viewport height, 1 when the last full report (W40) reaches it. The visible line tip lerps toward `p` at 0.09 — scrolling feels like being towed: the line lags a breath behind the reader, then catches up, never snapping. Wander: the path between waypoints is a Catmull-Rom spline whose lateral control offsets are scaled by the leg's amplitude factor from the ledger (fair 1.0, storm 2.2/1.8, Stream 1.4, final 0.6) — the geometry is fixed at build; only the draw moves. Each waypoint dot fills (`--deep` → `--buoy` ring) in 240ms (`--ease-drift`) as the tip passes it. The terminus: at `p` = 1 the tip stops at W40 and a 6px `--buoy` dot rests there. Nothing draws beyond it — there is no dashed projection, no fade-out tail.

**Choreography timeline.** Relative to story progress: p 0.00: tip at W01, first waypoint fills · p 0.14: W06 · p 0.31: W12 · p 0.47: W19 — the wide storm swings now visible above the tip · p 0.60: W25 — the line visibly straightens · p 0.74: W31 · p 0.88: W36 — swings narrowing · p 1.00: W40; tip stops; terminus dot rests; the line will not move again on this page, whatever the reader does next.

**State matrix.** *Rest:* full line drawn, all waypoints filled — the completed track, which is also the reduced-motion and no-JS state. *Drawing:* tip lerping behind `p`; waypoints fill as passed. *Scrolled-past (down):* line complete to the terminus. *Scrolled back up:* the draw reverses exactly — the line un-draws toward the earlier `p` (the reader is re-reading earlier weeks; the chart follows the reading, not a ratchet). *Jump scroll (anchor, find-in-page, restoration):* if `p` teleports by >0.25, the tip snaps to the new `p` on the next frame — no long tow across the whole story. *Disabled:* the pre-rendered full line. *Touch:* identical; the line is scroll-driven, never gesture-driven.

**Content-merge.** The line's waypoints are the ledger's transmitted positions; its legs pass the very report cards that transmitted them; its amplitude is the weather those reports record. Remove the reports and the line is a squiggle; remove the line and the reports lose their geography. They are one element wearing two forms, specified as two because they fail differently.

**Breakpoints.** ≥1200px: rail line, 300px viewBox, waypoint labels beside each dot. 768–1199px: rail narrows to 220px; labels move below their dots. <768px: the line becomes a 24px left-edge track behind the report cards (dots only, no labels — the cards themselves carry the week numbers); amplitude scaled ×0.5 so the wander stays inside the gutter.

**Edge cases & failure modes.** Content longer than the design expects (a report card with extra prose): waypoint offsets are measured from the rendered DOM at build-and-resize time, not hard-coded — the line re-maps on resize (debounced 200ms) so a waypoint never drifts away from its card. Very fast scrolling: the lerp caps the tip's speed at 2400px/s of path; the line arrives late but whole, never torn. Browser without SVG dash support (effectively none, but the rule stands): the line ships fully drawn and the scrub is skipped. The story column missing (a page type without the story, §7): the rail and line are absent entirely — the line belongs to 22914's story pages only, never reused as generic decoration on other pages.

**Fallback & watchdog.** The full path is in the DOM pre-drawn; JS arms the scrub only after the first loop frame. If the loop dies mid-page, the line freezes at its current draw — still truthful (it shows positions up to a real waypoint region) — and a **watchdog at 3000ms** of loop silence snaps the draw to the current `p` value computed from scroll position, so the chart never lags a dead loop by more than one check. With JS disabled, the completed track is the margin.

**Reduced motion.** The full track is drawn, all waypoints filled, the terminus resting. Progress is read from the printed week labels — the chart complete, the voyage visible at a glance.

**Accessibility.** The SVG is `aria-hidden="true"`. Its information is fully duplicated in text: each report card prints its own position in the data register, and the pinned card (§6.4) announces the current week and position as the reader passes it. No information exists only in the line.

**Performance & mobile variant.** One path's dash-offset per frame: negligible (≤0.05ms). The path geometry is build-time; no per-frame path computation. Mobile: same mechanism in the 24px track, amplitude halved.

**Tokens.** `--deep`, `--buoy`, `--ink`, `--ease-drift`, `--rail-w: 300px`, `--drift-lerp: 0.09`, `--wander-fair: 1.0`, `--wander-storm: 2.2`, `--wander-final: 0.6`.

### 6.3 Weekly report cards & their fading stamps

**What & why.** The story column is built of weekly report cards — one per printed transmission of the ledger (W01, W06, W12, W19, W25, W31, W36, W40 on the home page; all forty on the buoy's detail page). Each card is the week's paperwork: an inscription-register head (`WEEK 19 — TRANSMISSION RECEIVED`), the data block the buoy sent (position, sea temperature, battery, drift to date — all mono, all from the ledger), and the office's prose note in Newsreader. As each card arrives in the reader's view, the office stamps it: a rotated, bordered stamp lands on the card's corner with the date and position — and the stamp's ink is the battery made visible. Stamp opacity is a function of the week's transmitted battery: `opacity = clamp(battery + 13, 35, 100)` percent — 100% at W01 (battery 87%), fading week by week to W36's 40%, and at W40 the formula gives 17%, below legibility, so the office re-inks the final stamp by hand to the 35% floor and *says so on the card* ("STAMP RE-INKED BY HAND — BATTERY 4%"). The fading is not a style. It is the buoy weakening, in its own paperwork, with the one human intervention admitted in print.

**Structure.** A `<article>` per week on `--chart-lit`, 1px `--deep` rule frame, the data block as a definition list in the data register, the prose in Newsreader. The stamp is a DOM element (live Archivo inscription text in a double-ruled border, rotated −6°, positioned at the card's top-right, overlapping the frame) whose opacity is set from the ledger value — printed in the DOM at its final opacity from first paint; JS only arms the *landing* animation. The stamp's text: `RECEIVED` / the date / the position — three lines, exactly what the office would strike.

**Motion spec.** The stamp lands when the card's head crosses 70% of viewport height: it falls from 14px above its rest position and 1.6× scale to rest in 160ms (`--ease-stamp`), with the 90ms impact breath (scale 1.04 → 1.0), then stillness — a stamp lands once and never moves again. Landing is one-shot per card per page-load; scrolling back up does not re-stamp (paperwork is not un-struck), though the card's data and prose are, as always, already fully printed before the stamp ever falls. Stagger: if two cards cross the threshold in the same frame (fast scroll), their stamps land 120ms apart in document order.

**Choreography timeline.** Per card, relative to threshold crossing: 0ms threshold crossed · 0–160ms stamp falls · 160–250ms impact breath · 250ms still; the card is paperwork now. The W40 card's stamp lands identically — its difference is printed (the re-ink note), not performed.

**State matrix.** *Rest (pre-arrival):* card fully printed, stamp present at final opacity but un-landed (resting 14px high, at full scale — visible, honest, simply not yet struck). *Landing:* as above. *Stamped:* final state, permanent for the page-load. *Scrolled-past:* unchanged. *Disabled:* stamps rest at their printed positions and opacities — the full set of cards reads as a filed log. *Touch:* identical (scroll-triggered). *Focus:* a card is not focusable; its data is plain text in reading order.

**Content-merge.** The card is the content — the week's transmission and the office's note on it — and the stamp is the office's handling of that content, with the battery's decline written into the handling. The stamp tells the reader nothing the data block doesn't; it makes the reader *feel* what the data block says, which is the theme's whole method.

**Breakpoints.** ≥1200px: card spans the chart column (max 880px), stamp 150×96px at the top-right, data block in two columns. 768–1199px: stamp 132×84px, data block one column. <768px: card full-width, stamp 112×72px rotated −4°, overlapping the top border rather than the corner (so it never covers the data block on a narrow screen); prose measure full-width.

**Edge cases & failure modes.** A week whose transmission is partial in the ledger (only the fragment, §6.9, which is *not* a card — it gets its own element precisely because it must not be normalised into a card). A card whose data fails to load: the card prints with its data block reading `POSITION — NOT RECEIVED · SST — · BATTERY —` and no stamp ever lands (the office does not stamp what it did not receive); the prose prints the office's note about the gap. Long prose (over the §12 cap): the card grows; the drift line re-maps (§6.2) — the stamp is positioned to the card's frame, not to fixed coordinates, so it cannot land on the wrong card. Battery value missing for a week: opacity defaults to the 35% floor and the card prints `STAMP INK — UNRECORDED` — the office admits the gap rather than interpolating a fade.

**Fallback & watchdog.** Stamps ship printed at final opacity and position-adjacent; the landing is an enhancement armed by JS. **Watchdog: 1600ms** after a card's threshold crossing — if the stamp has not landed (loop stalled), it snaps to rest. With JS disabled, every card is a filed, stamped report: the story reads complete.

**Reduced motion.** No landing: stamps rest printed at their positions and opacities from first paint. The fade across the eight cards — the element's meaning — is fully preserved, because it lives in the opacities, not the animation.

**Accessibility.** The stamp is real text, read in document order after the card head: "Received, 23 September 2024, 29 degrees 58 minutes north, 070 degrees 44 minutes west." Its rotation is visual only. Stamp text contrast: `--ink` at the card's opacity against `--chart-lit` — at the 35% floor the *stamp* is a graphic artefact (its content is duplicated in the data block at full contrast), and the spec states this openly rather than pretending a 35% stamp is body text. Touch targets: cards are not interactive; no target needed.

**Performance & mobile variant.** One transform/opacity update per landing; zero per-frame cost. Mobile: same, smaller stamp. The eight home-page cards' total DOM is capped by the §4 density rule.

**Tokens.** `--chart-lit`, `--deep`, `--ink`, `--ease-stamp`, `--stamp-rot: -6deg`, `--stamp-ink-floor: 0.35`, `--stamp-fall: 160ms`.

---

### 6.4 The pinned ID card & the battery countdown

**What & why.** At the head of the margin rail, one card pins for the whole story: the chosen buoy's ID card — `BUOY 22914`, its deployment line, and three living figures that read the story as the reader does: the week currently being read, the position that week transmitted, and the battery that week had left. The battery is the theme's countdown: it begins at 87% beside W01 and falls — 81, 74, 65, 56, 44, 27 — to 4% beside W40, scrubbed to the same story progress `p` as the drift line, piecewise-linear through the ledger's eight transmitted values, displayed as the whole percent the buoy sent. It never resets, never estimates between transmissions (it holds each transmitted value until the next report's threshold, then travels to it — a step function with a short glide, because the office knows the battery only when the buoy speaks). After the last report, in the silence section, the battery line changes to `—` and then to the card's final state: `NO SIGNAL`. The reader's progress is the buoy's remaining life, printed in mono at the margin's head — reading costs the buoy something, and the card keeps the account.

**Structure.** A `<aside>` card on `--deep` (chart text upon it, 7.4:1), sticky at the rail head (`position: sticky; top: 24px`). Contents: the buoy glyph (an SVG hull-and-drogue mark in `--buoy`), `BUOY 22914` in Data large, the deployment line in inscription register (`DEPLOYED 13 MAY 2024 · 18°12′N 042°30′W · DROGUE 15 M`), a rule, then the three living figures as a definition list in the data register: `WEEK`, `POSITION`, `BATTERY`. The figures are loop-registered values updated from `p` and the ledger's report thresholds — the same code path as the drift line's waypoints, so card and line can never disagree about which week the reader is in. The card ships printed at its W01 state (the story's start); JS advances it.

**Motion spec.** Figure changes are step-and-glide: when `p` crosses a report threshold, the week and position lines cross-fade (120ms, `--ease-drift`, old value down 2px, new value in) and the battery figure counts from the previous transmitted value to the new one over 900ms (`--ease-current`, integer steps only — a battery does not do decimals) — at reading speed the count lands just after the reader arrives at the new report, like a reading being taken. Between thresholds, nothing on the card moves; the card is an instrument at rest, not a widget. The final change (into the silence section) is slower and unadorned: battery fades to `—` over 1200ms, holds for one viewport, then `NO SIGNAL` prints. No other state change on the card ever takes 1200ms; the office lingers only there.

**Choreography timeline.** Relative to each threshold crossing: 0ms threshold crossed · 0–120ms week/position cross-fade · 100–1000ms battery counts to the new transmitted value · 1000ms card at rest in the new week. At the silence threshold: 0–1200ms battery fades to `—` · the drift line's terminus (§6.2) is already at rest above this section · after one further viewport of scroll, `NO SIGNAL` replaces the dash.

**State matrix.** *Rest:* card shows the current week's transmitted figures, still. *Counting:* battery mid-count between two transmitted values — the only animated state. *Scrolled-past (the fleet and form sections):* the card un-pins at the story column's end (sticky range ends) and scrolls away with the page — its work is done; it does not follow the reader into the fleet's present tense. *Scrolled back up:* figures return to the earlier week's values by the same step-and-glide (the reader is re-reading; the card re-reads with them — the battery rising on the way up is honest, because the card is labelled with the week it is reading). *Disabled:* card printed at W01 state with the full range stated beneath: `BATTERY ACROSS THE STORY: 87% → 4%`. *Touch:* identical. *Focus:* the card is not interactive; its figures are plain text, updated outside any live region (a screen reader must not be read a battery countdown).

**Content-merge.** The card is the story's dashboard and its conscience: it holds the deployment facts, the current reading position, and the cost. Every figure on it is a ledger figure; the card introduces no number of its own. It merges because it is *about* the adjacent content at the level of mechanism — it reads the same record the reports print.

**Breakpoints.** ≥1200px: card 300px wide in the rail, Data large battery (22px). 768–1199px: card 220px, battery 19px, deployment line wraps to two lines. <768px: the rail dissolves; the card becomes a sticky top strip (full width, 56px tall): `BUOY 22914 · WEEK 19 · BATTERY 65%` on one mono line, deployment line cut (it lives in the hero and the ledger). The strip's sticky range is the story column, exactly as on desktop.

**Edge cases & failure modes.** A reader who jump-scrolls to the silence: the card snaps to the final state (battery `—`, then NO SIGNAL on the next frame check) — it does not count down through seven values in a panic. A reader on a very tall viewport who can see two report thresholds at once: the card reads the *lower* threshold's week (the furthest the reader has certainly reached) — a deterministic rule, stated here so two builders build the same card. Ledger data missing: the card prints its deployment lines and `BATTERY — UNRECORDED`; it never invents a percentage. The sticky card on a short story (detail pages print all 40 reports): the same mechanism, thresholds from the 40-report record.

**Fallback & watchdog.** The card ships complete and correct at the story's first state; every later state is an enhancement. Because its figures are pure functions of scroll position computed in the shared loop, a **watchdog at 3000ms** of loop silence recomputes the card's state directly from scroll position and the ledger, so the card can never be left showing the wrong week by a dead loop. With JS disabled, the printed range line carries the story's battery arc in one sentence.

**Reduced motion.** The card updates by cut at thresholds (no count, no fade); the silence state's changes are also cuts. The printed range line is added beneath the battery for reduced-motion readers, so the arc is stated, not just stepped through.

**Accessibility.** Figures are text; updates are *not* in a live region. The card's week/position/battery are duplicated in each report card's own data block (§6.3), so nothing depends on the pinned card being visible. Contrast: `--chart` on `--deep` 7.4:1 at all states; the battery's low values are *not* colour-coded (no red battery — the number is the news; a `LOW` inscription appears beside values under 30%, in `--chart`, because the office writes words, not warnings in colour).

**Performance & mobile variant.** Text updates only at thresholds; the 900ms count is one registered value in the loop (≤0.05ms/frame). Mobile strip: same mechanism, one line.

**Tokens.** `--deep`, `--chart`, `--buoy`, `--ink`, `--ease-current`, `--ease-drift`, `--card-top: 24px`, `--battery-count: 900ms`, `--battery-low: 30%`.

### 6.5 Ripple-answer hover (the hail)

**What & why.** Hovering any buoy dot — on the hero chart, on a biography card's miniature chart, in the fleet table's chart column — sends a ripple ring back from it and brightens its ID: the buoy answers. Hover in this theme is not a style change; it is a hail on the network's own protocol, and the answer is the network's own signal — a ring on the water and the station naming itself. It merges with content because the thing hovered *is* the content (a specific buoy, with a specific ID), and the answer identifies it. A buoy that has fallen silent does not answer: hovering a silent buoy's dot sends no ripple — its ID brightens faintly, and its status line prints `NO ANSWER — SILENT SINCE MARCH` (or its own date). The protocol distinguishes the living from the lost, and the hover is where the reader learns to feel the difference.

**Structure.** Each buoy dot is an SVG `<g>` (or a button wrapping one, where the dot is also the §6.6 click target) with: the dot (4px `--buoy` at 70% rest tone for reporting buoys; `--deep` at 50% for silent ones), a ripple `<circle>` (loop-registered radius/opacity, shared ripple pool — at most 6 ripple nodes exist page-wide, reused), and the ID label in the data register, printed beside the dot on charts large enough, or in the chart's caption strip on small ones. The answer's text (ID + status) also prints into a visually-hidden live-adjacent node for focus parity (see Accessibility).

**Motion spec.** On hover (or focus) of a reporting buoy: the dot brightens to full `--buoy` in 120ms (`--ease-drift`); a ripple is born at 200ms — radius 0 → 34px over 800ms (`--ease-ripple`), opacity 0.5 → 0; the ID label's opacity goes 0.55 → 1 in 200ms. One ripple per hail; re-hovering during a ripple restarts it only after it completes (a buoy answers a hail fully before answering another). On leave: dot and label return over 300ms. For a silent buoy: no ripple at any point; the dot holds its tone; the ID brightens to 0.8 and the status line fades in over 300ms. The asymmetry is the spec, not a bug: 800ms of ring for the living, stillness for the lost.

**Choreography timeline.** For a reporting buoy: 0ms pointer enters · 0–120ms dot brightens · 200ms ripple born · 200–1000ms ripple expands and fades · label at full by 200ms · pointer leaves → 300ms settle back. (Silent buoy). 0ms pointer enters · 0–300ms ID and status line fade in · nothing else, for as long as the pointer stays.

**State matrix.** *Rest:* dot at rest tone, ID at 0.55. *Hailed (hover/focus):* as above. *Active (pressed, touch):* the hail fires on touchstart's release — touch has no hover, so a tap on a dot *is* the hail, and if the dot is also a §6.6 target the report request follows the completed ripple (tap = hail, then answer-with-data). *Scrolled-past:* dots outside the viewport do not answer (their ripples are not armed). *Disabled:* dots and IDs printed statically; the status of every buoy is available in §6.12's table regardless. *Focus:* keyboard focus produces the identical answer as hover — focus is a hail too.

**Content-merge.** The hail identifies a real buoy and reports its real status; the silent buoys' non-answer is the theme's thesis at fingertip scale. Nothing decorative ripples: decorative water does not exist on this chart (§6.7's ambient ripples are also reports, on their own schedule).

**Breakpoints.** ≥1200px: full spec; ID labels beside dots on the hero chart. 768–1199px: ripple radius 28px; labels on the hero chart only. <768px: ripple radius 24px; IDs print in the caption strip (the tapped/hovered buoy's ID and status appear in a fixed line under the chart, since beside-dot labels would collide at small sizes).

**Edge cases & failure modes.** Pointer sweeping across many dots (a hail storm): ripples are pooled (6 nodes); a dot whose hail can't get a ripple node still brightens and labels — identification never waits for water. A buoy whose status is unknown (record gap): it answers like a reporting buoy but its status line reads `STATUS — UNRECORDED`; the office does not guess it silent. Reduced-motion pointers (coarse + reduced motion): the answer is the ID and status only, instantly. The hero sequence (§6.1) running: hails are disabled until the roll-call settles — the office does not talk over the roll-call.

**Fallback & watchdog.** The hail is pure enhancement: dots, IDs, and statuses are all printed without it (statuses in §6.12; IDs on the cards). Ripples are loop-driven; if the loop is stalled the **watchdog (3000ms, shared with §6.4)** leaves dots at rest tone — a buoy that cannot ripple still brightens via the CSS `:hover` rule that ships as the no-loop fallback (brightening is CSS, rippling is loop; the degradation is graceful by construction).

**Reduced motion.** No ripple. The dot brightens and the ID/status print instantly on hover/focus. The silent buoys' behaviour is unchanged — it was already stillness.

**Accessibility.** Every dot that answers is reachable by keyboard where it is interactive (focus = hail, identical timing). The answer's content (ID + status) is text, exposed to assistive tech via the dot's accessible name: `Buoy 30772, reporting. Buoy 22914, silent since March.` Contrast: IDs at rest are 0.55 opacity *as a graphic affordance*; the same IDs print at full contrast in the card strip and table, so no information rides on the dimmed label.

**Performance & mobile variant.** Ripple pool of 6 SVG circles page-wide; per-frame cost ≤0.1ms while any ripple lives. Mobile: tap-hail with the caption-strip ID; pool of 3.

**Tokens.** `--buoy`, `--deep`, `--ink`, `--signal-deep`, `--ease-ripple`, `--ease-drift`, `--ripple-answer-r: 34px`, `--dot-r: 4px`, `--ripple-pool: 6`.

### 6.6 Click-to-request a report (the answer, with its delay)

**What & why.** Clicking a buoy dot requests its current report — and the network takes a moment. After a realistic beat (~700ms, the ledger's nominal signal delay), the buoy's report card flips up beside the chart: current position, sea temperature, battery, last transmission time. The wait is not a loading spinner wearing a costume; it is the world's physics — a signal goes up to a satellite and an answer comes down from a machine that wakes on its own schedule — and the theme makes the visitor feel 700ms of it, with the buoy's dot pulsing once while the request is out. For a silent buoy, the request is still honoured: after the same delay, its card flips up with its *last* transmission, stamped LAST KNOWN, and the line `NO ANSWER SINCE 03 MAR 2025` (its first missed report). The office answers every hail with everything it has; what it has, for the silent, is a record that ends.

**Structure.** The report card is a DOM element (`--chart-lit`, framed like §6.3's cards in miniature) associated with the chart, one instance reused for all buoys (its contents are filled from the fleet record). The request state lives on the dot: a pulsing ring (loop-registered, 2 pulses over the delay window) and the dot's `aria-busy`. The delay is a timer, not an animation: 700ms nominal from the record's `signalDelayMs`, with the card's flip (380ms, `--ease-flip`) starting at the delay's end. The card carries a close control (a real button, `DISMISS` in inscription register) and traps nothing — it is a card on the chart table, not a modal.

**Motion spec.** Click: dot pulses (ring radius 0 → 18px, 350ms `--ease-ripple`, twice, second pulse at +350ms). At +700ms: the card flips up from the chart's bottom edge nearest the dot (rotateX −80° → 0°, 380ms, `--ease-flip`), its data lines stagger in at 40ms intervals (position, SST, battery, last transmission — the order a transmission arrives). Card holds until dismissed, another buoy is clicked (the card re-flips with the new buoy's data after a fresh delay — the office re-asks, it does not swap instantly), or the chart scrolls a full viewport away (card settles back, 200ms). Maximum wait is bounded by the watchdog below; the delay never stretches for effect.

**Choreography timeline.** 0ms click; dot's first pulse · +350ms second pulse · +700ms card begins its flip · +1080ms card flat; data lines complete · card holds. (Silent buoy: identical timing; the card's stamp line reads LAST KNOWN and its final data line is the no-answer line.)

**State matrix.** *Rest:* no card; dots at rest. *Requesting:* dot pulsing, `aria-busy="true"`; a second click on the same dot is ignored (one hail out at a time); a click on a different dot cancels and re-issues. *Answered:* card up, data printed. *Answered (silent):* card up with LAST KNOWN stamp and the no-answer line. *Failed (record unreachable):* after the watchdog, the card flips up with the buoy's last cached record labelled `LAST KNOWN — RECORD UNREACHABLE`, or, if no record exists at all, `BUOY ——— — NO RECORD`. The request never ends in a spinner or a blank. *Scrolled-past:* card dismissed by the settle rule above. *Disabled (no JS):* no request mechanism; every buoy's current report is §6.12's table row and §6.11's cards — the click is a shortcut, never the only road. *Touch:* tap = click, identical.

**Content-merge.** The card's data is the buoy's real current record from the fleet record — the same figures its table row prints. The delay merges because it is the system's true latency class, disclosed in the card's footer line: `SIGNAL DELAY ≈ 0.7 S — THE BUOY ANSWERS WHEN IT WAKES.` A fake instant answer would be the one lie this element could tell, and it is specified against.

**Breakpoints.** ≥1200px: card 340px, flips up at the chart's bottom edge, aligned toward the clicked dot's horizontal position (clamped to the chart). 768–1199px: card 300px, centred on the chart's bottom edge. <768px: the card becomes a sheet fixed to the viewport bottom (full width, max-height 60vh, scrollable data), flipping up as a rise (translateY) — the flip's rotateX is cut on small screens because a 3D flip on a 340px sheet reads as a glitch, not paperwork.

**Edge cases & failure modes.** Rapid clicking across buoys: last click wins; in-flight pulses are cancelled cleanly (pool nodes released). A buoy that reports *during* the delay (its ambient interval fires): the card shows the fresher record and its timestamp line updates — the office uses the newest paper on the desk. Content longer than the card (a buoy with a long note): the card's note area scrolls internally; the data block never scrolls away. The same buoy clicked from two different charts on one page (hero + fleet): the shared card instance serves both; focus returns to the invoking dot on dismiss.

**Fallback & watchdog.** **Watchdog: 3000ms** — if no record has resolved by then (data layer hung), the card flips up with the failure states above. The mechanism degrades to §6.12's table without JS. No state of this element can leave a visitor watching a pulse forever: the pulse is capped at the watchdog, after which a card — some card, with honest text — always arrives.

**Reduced motion.** No pulses, no flip: after the same 700ms (the delay is content, not motion), the card appears by cut with its data printed. The wait remains, because the wait is the point; the theatre around it does not.

**Accessibility.** Dots that request are real `<button>`s (44px touch target via a transparent hit area around the 4px dot — the dot is small because buoys are small; the target is not). The card is a `role="status"` region? No — it is a labelled complementary region (`aria-label="Report for Buoy 30772"`), appearing without moving focus (focus stays on the dot; the card's arrival is announced via a polite live region with the one-line summary: "Buoy 30772 reports: battery 61 percent, last transmission 2 hours ago."). Esc dismisses and returns focus. All data is text at full contrast.

**Performance & mobile variant.** One card instance, one timer, pooled pulses: ≤0.1ms/frame while pulsing. Mobile: the bottom-sheet variant, same timer and watchdog.

**Tokens.** `--chart-lit`, `--deep`, `--buoy`, `--ink`, `--ease-flip`, `--ease-ripple`, `--signal-delay: 700ms`, `--report-watchdog: 3000ms`, `--report-card-w: 340px`.

---

### 6.7 Ambient report ripples (the network at work)

**What & why.** Distant buoys across the chart pulse slow ripples on their own intervals — 8 to 20 seconds each, unsynchronised, taken from the fleet record's per-buoy reporting intervals — whether or not anyone is watching. This is the theme's one licensed ambient loop, and it exists to make a single claim continuously: the chart is a working network, not a map illustration. Things report while you read about other things. The ripples are sparse by law: at most three may be alive on screen at once, their births are staggered by the record's intervals (never quantised to a shared beat — synchronised ripples read as a screensaver's pulse, and the gate checks for it), and a buoy whose interval elapses while its chart is off-screen simply reports unwitnessed, like the real ones.

**Structure.** The ripple pool from §6.5 (6 SVG circles page-wide; ambient use caps at 3 concurrent) driven by the shared loop. Each chart on the page (hero, fleet miniature) registers its visible buoys' next-report times from the fleet record (`nextReportAt` per buoy, advanced by its interval after each firing). A firing buoy: dot brightens for the ripple's life, one ring expands (0 → 40px, 1400ms — slower and wider than a hail's answer; an unwitnessed report is a bigger, lonelier ring), and if the buoy is in §6.12's table and the table is on screen, its row's received tick (§6.12) flashes once. The schedule is data, not decoration: intervals ship in the record.

**Motion spec.** Per firing: ring 1400ms (`--ease-ripple`), opacity 0.4 → 0; dot brightens 0.7 → 1.0 over 200ms, returns over 600ms after the ring dies. Concurrency cap 3; if a fourth buoy's time arrives while 3 rings live, its report is *skipped, not queued* (the ocean does not queue). The loop checks schedules once per second, not per frame. After 60 seconds of continuous visibility, the hero chart's ambient rate halves (intervals ×2) — a watched network settles; the office is not performing.

**Choreography timeline.** Continuous and deliberately unpatterned: each buoy's first firing at (page load + its record offset), then every interval. No global timeline exists to print, and that is the spec: any two screenshots a minute apart should show different, unsynchronised rings.

**State matrix.** *Rest:* between firings, the chart is still — stillness is the loop's most common state. *Firing:* as above. *Off-screen:* schedules advance, rings don't render; a buoy that "reported" while unwatched shows its received tick updated when next seen (its record advanced honestly). *Hidden tab:* loop sleeps; on return, schedules fast-forward to now (no catch-up storm of rings). *Disabled:* no ambient motion; the chart is printed. *Reduced motion:* the loop never arms (see below).

**Content-merge.** Each ripple is a specific buoy's specific scheduled report from the fleet record; the same event updates its table tick. The ambience is the data layer breathing — remove the record and there is nothing to animate, which is exactly the test the anti-filler law demands.

**Breakpoints.** ≥1200px: full spec on hero and fleet charts. 768–1199px: cap 2 concurrent. <768px: cap 1 concurrent, ring radius 30px, and ambient ripples arm only on the hero chart (small screens get a quieter sea).

**Edge cases & failure modes.** A record with many buoys sharing an interval (a fleet deployed together): the loop jitters each buoy's first firing by a deterministic per-buoy offset (buoy ID mod 7 seconds) so a deployment cohort doesn't pulse as one — the jitter is derived from the ID, so two builders' pages breathe identically. Battery-critical buoys (the record's `lowPower` flag): their intervals double in the ambient schedule, as the real buoys' do — the chart slows for the dying, and §6.12's row says why. Loop stall: rings freeze mid-expansion; the shared watchdog (3000ms) clears all ambient rings to rest rather than leaving frozen circles on the chart.

**Fallback & watchdog.** Pure enhancement: with no JS, no rings, and the chart loses nothing it needs. The shared **watchdog (3000ms)** clears stalled rings. If the fleet record fails to load, no ambient schedule exists and none is invented — the chart is still, and §6.12's failure state explains the silence in the office's voice.

**Reduced motion.** Never arms. The network's aliveness is carried instead by the printed tallies and timestamps (§6.18), which are text.

**Accessibility.** `aria-hidden` throughout; no live region announces ambient reports (a screen reader must not be serenaded with buoy traffic). The information a ripple carries — this buoy reported at this time — is text in §6.12's last-transmission column.

**Performance & mobile variant.** ≤3 rings, one 1s schedule tick: ≤0.1ms/frame worst case. The loop sleeps entirely when no chart is within one viewport. Mobile: 1 ring, hero only.

**Tokens.** `--buoy`, `--signal`, `--ease-ripple`, `--ambient-max: 3`, `--ambient-ring-r: 40px`, `--ambient-ring-dur: 1400ms`.

### 6.8 Bathymetry that deepens (the chart's geography)

**What & why.** Under everything, the chart's contour lines deepen in tone as the drift descends the page into deeper water. The story begins over the continental shelf and ends over the abyssal plain, and the paper itself knows: contour bands cross the page at the story's thresholds, each band's lines drawn closer and darker (`--contour` stepping toward `--deep` at 8% increments per band), with depth soundings printed in the margin in mono — `200 M`, `1,000 M`, `4,000 M` — as the water under the buoy deepens. It merges with content because it *is* the content's setting-as-data: the buoy's reports (§6.3) print the deepening in their notes ("the shelf falls away beneath her this week"), and the chart under the reader's eyes agrees. Geography that responds to the journey is the difference between a chart and a wallpaper.

**Structure.** A full-page SVG background (one per page, `position: fixed` within the chart column's stacking context, `aria-hidden`) holding: the graticule (vector lines), and 6 contour bands, each a set of closed contour paths generated from a simple depth model (depth as a function of story progress — a shelf profile: 180m at W01 descending to 4,850m at W40, with the shelf break at W19's storm leg and a seamount rise at W31 that the W31 report mentions). Band tones are precomputed colour steps between `--contour` and `--deep`; the *transition* between bands is scrubbed: a soft mask edge (120px gradient) travels with story progress `p`, so the deepening is continuous, not stepped — the water deepens gradually under the reader, the way it deepens under the buoy. Sounding figures are DOM text in the rail at each band boundary, printed at all times.

**Motion spec.** The mask edge is a loop-registered value tied to `p` (the same story progress as §6.2/§6.4 — one cause, three readings: line, battery, depth). No independent animation: at rest (fixed `p`) the bathymetry is perfectly still. Band crossings have no flourish; a reader who notices the paper darkening slightly by W31 has received exactly the intended dose.

**Choreography timeline.** Continuous with `p`: p 0.0 shelf tones (band 1, 180m sounding printed) · p 0.31 shelf break begins (W12) · p 0.47 the break completes under the storm leg (1,000m) · p 0.74 seamount rise lightens one band briefly (W31, 2,600m — the only place the deepening reverses, because the record says the bottom rose) · p 1.0 abyssal tones (4,850m) · the silence section sits over the deepest band, and the footer (§6.15) ends it on `--deep`.

**State matrix.** *Rest:* tones match the current `p` exactly. *Scrolling:* mask lerps at 0.09 with everything else. *Scrolled back up:* the water shallows again, exactly — the function is symmetric, there is no ratchet. *Jump scroll:* snaps with `p` (the §6.2 jump rule). *Disabled:* the full depth profile prints statically, band by band down the page (each section simply sits on its band — arguably the more legible version). *Touch:* identical.

**Content-merge.** The depth profile is declared in the ledger (§6.17) alongside the positions — depth at each report is a record field (`depthBelowM`), printed in the W-cards' notes where the office remarks on it. The background is the record drawn as geography; a builder may not deepen the water for mood in a section whose record says shelf.

**Breakpoints.** ≥1200px: full contour set (6 bands, ~40 paths). 768–1199px: 4 bands, contour count halved (every second line). <768px: 3 bands, contours at 60% tone strength — on a small screen the deepening must whisper; the soundings still print.

**Edge cases & failure modes.** No SVG support / SVG fails: the ground is flat `--chart` and the soundings still print — the geography is lost, the data is not. Extremely long pages (the 40-report detail page): the profile stretches — depth is a function of the *story*, so the same 6 bands map across 40 reports; band boundaries follow report thresholds, not pixel heights. Print stylesheet: bathymetry prints at band tones (charts are printed artefacts; the print gate (§10) checks the profile survives).

**Fallback & watchdog.** The bathymetry is a background: its total failure mode is a flat chart ground, which is the theme's resting state anyway. No watchdog is needed for a value that is a pure function of scroll position; the shared loop's watchdog (§6.4) recomputes `p` and with it the mask. JS disabled: static bands, fully printed.

**Reduced motion.** Identical to the disabled state: static bands per section. (The scrub is the only motion this element has, and it is cut with all scrubbing.)

**Accessibility.** Purely decorative-geographic; `aria-hidden`. Every fact it carries (depth at each report) is printed in text in the report cards and the ledger. Contrast: contours are graphics; no text is ever set directly on a contour line at less than its band's audited pairing (§10 checks body text against the deepest band it can sit on: `--ink` on band-6 ground ≥ 9:1 by construction of the tone steps).

**Performance & mobile variant.** One masked SVG, compositor-handled; per-frame cost ≈ 0 (a mask position). The SVG ships ≤14KB gzipped at desktop density, ≤7KB mobile.

**Tokens.** `--chart`, `--contour`, `--contour-night`, `--deep`, `--ink`, `--depth-bands: 6`, `--depth-mask-feather: 120px`.

### 6.9 The last transmission (the silence)

**What & why.** The final story section is half a report. It arrives as a fragment on the chart: a timestamp, a coordinate that stops mid-figure — `41°0—′N 043°—′W` — a temperature that stops mid-decimal — `SST 8.—` — and then nothing: white space where the rest of the transmission would be, the drift line already stopped in the margin above it, and one line in the inscription register: `BUOY 22914 — SILENT SINCE MARCH. DRIFTING STILL.` No animation performs here. No ripple answers, no stamp lands, no counter counts. This is the only element in the library specified primarily by what it refuses to do, and it is the theme's reason to exist: the one page in the set designed to make a reader feel something about hardware. It merges with content because it *is* the content's ending — the ledger's forty-first entry is a fragment (§6.17), and this section prints it exactly as received, incompleteness and all.

**Structure.** A section on the open chart (no card — the office does not file a fragment as a report; it lies on the chart where it fell). Contents, in order: the fragment's head in inscription register (`WEEK 41 — TRANSMISSION BEGUN 24 FEB 2025, 07:40 UTC — INCOMPLETE`), the fragment's data in mono exactly as received with em dashes where the signal cut, a whitespace block of 40vh (the rest of the transmission, absent), the silence line in inscription register at Display-3 weight, and beneath it one quiet prose paragraph in Newsreader — the office's note: what a drifting buoy with a dead battery most likely is now (still drifting, drogue down, hull fading), and the standing invitation to §6.13 (follow another buoy; the network goes on). The pinned card (§6.4) has reached NO SIGNAL by this section; the drift line (§6.2) ended one section earlier. The stillness is composed of three other elements' endings arriving together.

**Motion spec.** None, and the none is specified: no entrance animation (the fragment is printed, present from first paint), no scroll-triggered event in the section, no ambient ripple may fire on any chart within this section's viewport (the ambient scheduler (§6.7) excludes the fragment's chart region — a ripple here would be obscene, and the gate tests for it), no hover answer on the fragment's coordinate (§6.5's silent protocol applies, at its stillest). The only motion permitted in the section is the reader's own scroll and the shared loop settling to sleep as its last registered values reach their targets — the page itself winds down.

**Choreography timeline.** Deliberately empty. Arrival: everything already printed. Dwell: nothing happens, for as long as the reader stays. Departure (scrolling to the footer): nothing happens. The timeline's emptiness is the choreography, and §13's map prints this beat as a held rest.

**State matrix.** *Rest:* the fragment printed, the silence line printed — this is every state. *Hover/focus:* the silent protocol (§6.5) — the coordinate's status line only. *Scrolled-past:* unchanged; the footer follows. *Disabled / reduced motion / touch:* identical, by design — this element is the one place all modes converge, because its medium is print and absence.

**Content-merge.** Total: the section is the ledger's final entry, the drift line's terminus, the battery's zero, and the theme's thesis, occupying one screen. It cannot be removed without the page becoming a brochure; it cannot be decorated without becoming a lie.

**Breakpoints.** ≥1200px: whitespace block 40vh. 768–1199px: 32vh. <768px: 26vh — the pause must survive small screens, but a phone's reader should not have to scroll an ocean of nothing to reach the footer; 26vh of nothing on a phone is still a held breath.

**Edge cases & failure modes.** The one failure mode is a builder adding something: a "back to top" buoy that bobs, a fade-in on the silence line, a related-content carousel ("other silent buoys"). All are specified against, and §9 names them. A data failure here is impossible by construction — the fragment is static content, shipped in the HTML, not fetched. If the ledger fails to load, this section still prints: the ending does not depend on the data layer.

**Fallback & watchdog.** The element *is* the fallback state of the whole theme: print, absence, one line. No watchdog applies; there is nothing to stall.

**Reduced motion.** Identical. This element is the reduced-motion experience of the entire theme, arrived at early: it proves the theme's deepest beat needs no motion at all.

**Accessibility.** The fragment's unfinished figures are marked up so assistive tech reads them as incomplete data, not typos: the coordinate carries an `aria-label` — "41 degrees, incomplete minutes, north; 043 degrees, incomplete, west — transmission cut off." The silence line is a real heading (`<h2>`), so the story's structure survives non-visual reading: deployment, forty reports, a fragment, a silence. The whitespace is visual only; the note paragraph follows the line directly in reading order.

**Performance & mobile variant.** Zero cost — the cheapest element in the theme, and the most expensive one to get right. Mobile: the 26vh rule above.

**Tokens.** `--chart`, `--ink`, `--deep`, `--silence-gap: 40vh`.

---

### 6.10 Graticule masthead & fleet navigation (the chart's frame)

**What & why.** A nautical chart is framed by its graticule and titled in its margin; the site's navigation lives in that frame. The masthead is a chart title block: the network's name in Archivo, the chart's number and edition in inscription register (`CHART DBN-01 · NORTH ATLANTIC & ALL OCEANS · EDITION 2026`), and the navigation as a list of *waters and offices* — THE FLEET, THE STORY OF 22914, FOLLOW A BUOY, THE LEDGER — each entry printed like a chart index entry with its coordinates of the page (section marks in mono). The current section is marked the way a navigator marks a position: a small `--buoy` cross and the section's name underlined by a drawn rule. Navigation here is not a menu bar wearing a costume; it is the chart's own furniture, and it merges because a chart without a title block and index is not a chart.

**Structure.** A `<header>` on `--chart` over the graticule, bottom-ruled in `--deep`. Title block left; `<nav>` as a horizontal index on desktop, each item a link with a mono section mark (`§ FLEET`). The position marker is a loop-registered element: as the reader's scroll crosses section thresholds, the cross travels to the current item and its rule draws (240ms, `--ease-drift`). The header is *not* sticky — charts don't follow you; instead, a miniature position line (§6.4's mobile strip is its cousin) — no: the spec is plain: the masthead prints at the top and stays there, and orientation inside the page is the rail's job (§6.2, §6.4). On mobile the index collapses behind a `CHART INDEX` button that opens the index as a full chart-overlay panel.

**Motion spec.** Page load: the title block's rule draws left-to-right once (600ms, `--ease-current`) — the chart being ruled before use. Position marker: travels between items over 240ms as thresholds cross; the rule under the active item draws in the same beat. Hover on an item: its mono mark brightens to `--orange-deep` and the item's underline draws (240ms). No other motion: the frame of a chart is the stillest thing on it.

**Choreography timeline.** 0ms header printed (it is never hidden) · rule draw 0–600ms on first load only · thereafter, marker moves only at section thresholds, 240ms each.

**State matrix.** *Rest:* marker on the current section (or the first, at load). *Hover/focus:* underline draw + mark brightening, identical for focus. *Active (the reader's section):* cross + full rule, in `--buoy` and `--ink` respectively — the cross is orange because a position mark is a physical mark on the chart (one of orange's licensed uses, §2). *Mobile closed/open:* the index panel opens by cut-and-rule-draw (300ms); Esc closes; focus returns to the button. *Disabled:* a plain header and list of links — which is all it ever was.

**Content-merge.** The index entries are the page's real sections with their real marks; the edition line is the site's real chart edition (a versioned document, like a chart — corrections are issued as new editions, and §6.15's footer prints the correction line). Navigation that admits it is an edition of a chart is navigation that can be corrected like one.

**Breakpoints.** ≥1200px: full title block + horizontal index. 768–1199px: title block compresses (edition line drops to one line, index wraps under the title). <768px: `CHART INDEX` button + overlay panel; the title reduces to the network name and chart number.

**Edge cases & failure modes.** A page with sections the index doesn't list (utility pages, §7): the marker rests on the nearest listed ancestor or prints no cross — never a wrong position. Very long section names: the index wraps; the cross aligns to the item's first line. The overlay panel on mobile with JS disabled: the index prints as a plain list at the page top (the button is JS-only furniture; the links are not).

**Fallback & watchdog.** All content is static DOM; the marker is the only enhancement, driven by the shared loop with the §6.4 watchdog (3000ms) recomputing the current section from scroll position if the loop dies. Nothing here can strand: worst case, no cross — the index still reads perfectly.

**Reduced motion.** The rule draw and marker travel become cuts. The cross still marks the section (it is information, not motion).

**Accessibility.** A real `<nav>` with a list; the current item carries `aria-current="true"` (updated with the marker). The cross is decorative (`aria-hidden`). Mobile panel: focus trapped while open, labelled `Chart index`, Esc closes. Contrast: index text `--ink` on `--chart` 11.3:1; the mono marks at rest are `--deep` 7.4:1 — full contrast, no dimmed nav text anywhere.

**Performance & mobile variant.** One travelling marker; negligible. Mobile panel is DOM, no library.

**Tokens.** `--chart`, `--deep`, `--ink`, `--buoy`, `--orange-deep`, `--ease-current`, `--ease-drift`, `--rule-draw: 600ms`.

### 6.11 Buoy biography cards (the fleet, person by person)

**What & why.** Each buoy has a small biography, and the listing surfaces are built of biography cards: a buoy's deployment photograph (the moment it left the stern, orange against grey water), its ID and deployment line, its current status in the data register, and two or three sentences in Newsreader italic — the human note: where it has been, what it has survived, what the office calls it. ("22907 rides the same current as her sister did, and reports like her: briefly, and only when it matters.") The cards merge data and affection without mixing their typefaces — mono for what the buoy sent, italic for what the office thinks — and they are the fleet made browsable as *persons*, which is how the network's funders and followers actually relate to it. The chosen buoy's card is always first on the home fleet section, marked with its LAST KNOWN stamp (at its true ledger opacity), because the story the reader just finished is standing in this list among the living.

**Structure.** A `<article>` card on `--chart-lit`: photograph in a chart frame (1px `--deep` rule, caption strip beneath with the photo's own data — vessel, date, position of deployment, all mono), ID in Data large, status block (state, last transmission, battery — mono), biography in Newsreader italic (capped at 3 sentences / ~55 words, §12), and a `READ ITS RECORD` link to the buoy's detail page. Silent buoys' cards carry their stamp (`LAST KNOWN` + silence date, at ledger opacity) and no battery figure — the field prints `BATTERY — NO SIGNAL`. Cards are generated from the fleet record; the photograph is a real deployment photo or, where none exists, the card prints a chart excerpt of the deployment position instead — never a stock ocean photograph (a stock wave is this theme's clip-art, §9).

**Motion spec.** Cards arrive like reports: as a card crosses 70% viewport height, its photograph settles into its frame (scale 1.05 → 1.0, 700ms, `--ease-current`) and the card's top rule draws (300ms). Nothing else moves — biographies are read, not performed. Hover: the card lifts 2px (`--ease-drift`, 200ms) and its photograph's caption strip brightens; if the card carries a miniature chart, §6.5's hail applies to its dot. A silent buoy's card does not lift on hover — it brightens only. (The office handles the lost more gently; the difference is 2px and entirely deliberate.)

**Choreography timeline.** Per card: 0ms threshold · 0–700ms photograph settles · 0–300ms rule draws · then rest. Stagger across a row: cards settle in document order at 90ms offsets as the row crosses.

**State matrix.** *Rest:* fully printed card. *Arriving:* settle + rule draw. *Hover/focus:* lift (reporting) or brighten (silent); the record link's underline draws. *Scrolled-past:* settled state persists. *Disabled:* printed cards, photographs at rest scale. *Touch:* no hover states; the settle still fires on scroll. *Data-missing buoy:* card prints with `RECORD INCOMPLETE` in the status block and a chart excerpt instead of a photograph — the fleet list shows its gaps.

**Content-merge.** A card is the buoy — its record, its photograph, its office note — in one filing unit. The status figures are the fleet record's; the biography is the office's; the two never share a typeface, so the reader always knows which voice is speaking (§12).

**Breakpoints.** ≥1200px: rows of 3, card ~400px, photograph 3:2. 768–1199px: rows of 2. <768px: single column; photograph 16:9; biography cap unchanged (the note is the card's soul at every size).

**Edge cases & failure modes.** A buoy with no biography written yet: the card prints its record and the line `NOTE — NOT YET WRITTEN` in italic; the office admits an unwritten note rather than generating one. Photograph fails to load: the chart excerpt fallback renders (it is in the DOM as the img's background layer) and the caption gains `PHOTOGRAPH — NOT RECEIVED`. A fleet of 412: the home section prints 6 cards (the chosen + 5 featured from the record) with the index line `SIX OF 412 — THE FULL FLEET IS §6.12'S TABLE`; the listing page paginates cards 24 at a time. Counts are printed, never implied.

**Fallback & watchdog.** Cards ship fully printed with photographs at rest scale; the settle is JS-armed. **Watchdog: 1600ms** (shared pattern with §6.3) — a card whose settle hasn't completed snaps to rest. No-JS: complete cards.

**Reduced motion.** No settle, no lift: cards print, photographs rest, rules are drawn. The silent/reporting hover distinction collapses to brightening for all — the one place reduced motion simplifies a meaning, noted honestly here; the stamps still distinguish the lost.

**Accessibility.** The card's link wraps only the `READ ITS RECORD` text (not the whole card — a card is a document, not a button). Photographs carry real alt text naming the buoy and the moment ("Buoy 22914 leaving the stern of RV Meridian, 13 May 2024"). Status figures are text. Stamp text is duplicated in the status block at full contrast (as §6.3).

**Performance & mobile variant.** Photographs ≤90KB each, lazy-loaded below the fold, aspect ratios reserved (CLS 0). Settle cost negligible. Mobile: same cards, one column.

**Tokens.** `--chart-lit`, `--deep`, `--ink`, `--buoy`, `--ease-current`, `--ease-drift`, `--card-settle: 700ms`, `--bio-max-words: 55`.

### 6.12 The fleet table (every buoy, one row)

**What & why.** The network's full roll, printed as a table: 412 rows, one per buoy — ID, basin, deployed date, last transmission, battery, status. This is the office's master document and the theme's data backbone: §6.1's tally, §6.11's cards, and §6.6's reports all read the same record this table prints in full. It merges because it is not a UI component styled as paperwork — it *is* the paperwork, and every other element is a view onto it. Its signature behaviours are two: the received tick (a row's status glyph flashes `--signal` once when that buoy's ambient report fires, §6.7 — the table is alive at the speed of the network) and the honest pagination (25 rows per page, `PAGE 2 OF 17 — ROWS 26–50 OF 412`, because 412 rows at 25 is 17 pages and the table says so).

**Structure.** A `<table>` on `--chart-lit` with a `--deep` header row (chart text), inscription-register heads, data-register cells. Columns: BUOY (mono ID), BASIN, DEPLOYED, LAST TRANSMISSION (relative + absolute on focus/hover), BATTERY (figure or `—`), STATUS (`REPORTING` in `--signal-deep` text / `SILENT SINCE <date>` in ink). Filters above the table in the §11 select treatment: basin, status, battery band — native selects, server-round-trippable. The header row pins inside the table's frame on scroll (`position: sticky` within a max-height region on desktop; on the full-page variant the page scrolls and the header pins to the viewport top under the masthead rule). Rows for silent buoys carry no battery figure and their status cell prints the silence date; 22914's row is reachable by the index link `FIND 22914` that the story's end provides.

**Motion spec.** Almost none, deliberately: filter changes re-print the table by cut with a 200ms rule redraw; pagination likewise. The received tick: when §6.7 fires for a buoy whose row is rendered, its status glyph (a 6px `--signal` square) pulses opacity 0.25 → 1 → 0.25 over 1400ms in step with the ripple — the table and the chart agree about the event because they are the same event. Sorting (by ID, deployed, last transmission, battery) is offered on the three numeric columns; a sort re-prints by cut. No row animations, no expand-in-place: rows are records.

**Choreography timeline.** On load: table printed (server-rendered first page), header pinned. On a buoy's report: glyph pulse synced to §6.7's ring (0–1400ms). On filter/sort/page: cut + 200ms rule redraw.

**State matrix.** *Rest:* printed rows. *Reporting event:* one glyph pulses. *Filtered:* the count line reprints (`FILTERED — 38 OF 412 · BASIN: SOUTH PACIFIC`) — a filtered table always confesses its filter. *Empty filter result:* the §12 empty state — `NO BUOYS MATCH — THE NETWORK HAS NONE IN THESE WATERS WITH THAT STATUS.` plus a clear-filter link. *Disabled:* the table is server-rendered and paginated by links; filters are a GET form. *Touch:* same table, columns prioritised (see Breakpoints).

**Content-merge.** Total: the table is the fleet record's public face. Its figures are the record's figures; §10's audit reconciles the table's counts (412 rows, 401 reporting, 11 silent) against the tally and the footer automatically.

**Breakpoints.** ≥1200px: all 6 columns. 768–1199px: BASIN merges into the BUOY cell (two-line cell); 5 columns. <768px: the table becomes a list of row-cards (ID + status + battery + last transmission; deployed and basin in the card's second line) — a 412-row table does not shrink to a phone, it re-files itself; pagination and filters unchanged.

**Edge cases & failure modes.** Record fails to load: the table prints its server-rendered first page (which ships in the HTML) and a notice bed (§11): `THE FLEET RECORD IS NOT ANSWERING — SHOWING THE LAST PRINTED ROLL.` with the print date. A buoy whose battery telemetry is missing: `—`, never 0% (0% is a claim; a dash is a gap). Duplicate IDs in a bad record: the table prints both and flags the second `DUPLICATE — UNDER REVIEW` — the office shows its problems. Sorting stability: secondary sort is always buoy ID ascending, so two builders' tables order identically.

**Fallback & watchdog.** Server-rendered and complete without JS; filters and pagination work as plain links/forms. The tick pulse is the only JS behaviour, loop-driven under the shared watchdog. There is no loading state for the table beyond §6.14's sounding on first navigation.

**Reduced motion.** The glyph pulse becomes a steady 1400ms highlight at fixed opacity (a state, not an animation), or under `prefers-reduced-motion: reduce` plus the still-toggle (§11), no highlight at all — the row's last-transmission text still updates.

**Accessibility.** A real `<table>` with `<th scope>` and a caption (`The fleet roll — 412 buoys`). Sort buttons are real buttons with `aria-sort` on the active column. The glyph is `aria-hidden`; status is text. Filter selects have visible labels. Row contrast: ink on `--chart-lit` 13.0:1; striping `--chart-deep` rows at 9.4:1.

**Performance & mobile variant.** 25 rows per render, never 412 in the DOM. Pulse cost negligible. Mobile list variant: same data, card layout, same pagination counts.

**Tokens.** `--chart-lit`, `--chart-deep`, `--deep`, `--chart`, `--ink`, `--signal`, `--signal-deep`, `--rows-per-page: 25`.

---

### 6.13 Follow a buoy (the conversion form)

**What & why.** The network's one conversion: a visitor chooses a buoy (or "the fleet — one email a week, the week's reports") and an email address, and thereafter receives that buoy's reports as they arrive. The form's genius, and its merge, is its confirmation: not a toast, not a tick — a *stamped report card*, printed on the page in §6.3's own furniture, stamped `FOLLOWER Nº 1,209` (the number derived from the printed follower count, 1,208, + 1) with the chosen buoy's ID and the line `FIRST REPORT — WHEN SHE NEXT TRANSMITS.` Following a buoy is joining the roll-call's audience; the confirmation files the visitor into the office's paperwork. For a silent buoy the form still works — followers of 22914 receive her full record once, and the confirmation says so: `SHE IS SILENT. YOU WILL RECEIVE HER RECORD — ALL FORTY WEEKS AND THE FRAGMENT.` The office does not upsell the living over the lost.

**Structure.** A form on a `--chart-lit` leaf: a buoy select (native `<select>` styled per §11, listing buoys grouped by basin with status in the option text — `22914 — NORTH ATLANTIC — SILENT SINCE MARCH`), an email input, and the submit button as a stamp key (§11). The confirmation replaces the form leaf in place: a report-card composition — inscription head `FOLLOWER ENROLLED`, the follower number stamped (Archivo inscription, rotated −6°, ink at full opacity — this stamp is fresh, its battery is the visitor's), the buoy's ID and next-report line in mono, and the office's closing sentence (§12's fixed string). The no-JS path posts to the server and returns the same confirmation as a rendered page.

**Motion spec.** Buoy select change: if the chosen buoy has a chart on the page, its dot answers with §6.5's hail (reporting) or its status prints (silent) — choosing is hailing. Submit: the stamp key presses (1px, 120ms); the state word changes to `TRANSMITTING…` for the request's true duration (a form post, typically 400–900ms — never a fixed fake duration); on success the leaf settles (200ms, `--ease-drift`) into the confirmation card and the stamp lands (160ms, `--ease-stamp`, with its impact breath) at +250ms. On error: no stamp; the error prints above the field in `--orange-deep` text (§12's error voice), every field preserved.

**Choreography timeline.** 0ms submit; key press · state word `TRANSMITTING…` for the true request duration · +0ms on response: leaf settles 200ms · +250ms stamp falls · +410ms impact breath ends; confirmation complete and readable. The follower number in the stamp was true at the moment of enrolment and is not re-rendered afterwards.

**State matrix.** *Rest:* form printed, follower count stated in the leaf's head (`1,208 PEOPLE FOLLOW BUOYS OF THIS NETWORK`). *Choosing:* hail/status response per buoy. *Transmitting:* button disabled, state word honest. *Enrolled:* confirmation card, permanent for the session; a `FOLLOW ANOTHER` link restores a fresh form (the count in its head now reads 1,209 — the record moved, and the page moves with it). *Error (validation):* field-level, §12 voice, fields preserved. *Error (buoy filled / programme full — not applicable here; the network takes all followers):* n/a, and the spec says so rather than inventing scarcity. *Disabled:* the form is a plain HTML form; confirmation is server-rendered. *Touch:* identical; the select is native.

**Content-merge.** The confirmation is a document of the same office that stamped the weekly reports — same furniture, same type, same honesty rules (the number is derived from a printed count; §10 audits the derivation). Conversion here is enrolment in the record, and it feels like it.

**Breakpoints.** ≥1200px: leaf 560px in the chart column; confirmation card matches §6.3's card width. 768–1199px: leaf full column width. <768px: leaf full-width; the stamp on the confirmation is 112×72px (as §6.3's mobile stamp) and lands at the card's top border, never over the follower number's text.

**Edge cases & failure modes.** Duplicate enrolment (same email + buoy): the confirmation prints `ALREADY ON THE ROLL — FOLLOWER Nº 843` with the original number — the office finds the existing filing rather than issuing a second. A buoy retired between page load and submit: the error voice explains and offers its record page. Request timeout: the **watchdog (3000ms)** ends the transmitting state with `THE OFFICE DIDN'T ANSWER — YOUR DETAILS ARE STILL HERE. TRY AGAIN.` and the form intact. The follower count itself failing to load: the head prints `THE ROLL IS BEING KEPT` and the confirmation stamp omits the number rather than inventing one — a stamp without a number is odd, and the oddity is the honesty.

**Fallback & watchdog.** Plain form + server confirmation without JS. Watchdog 3000ms on the request, as above. The stamp's landing has §6.3's 1600ms snap if the loop stalls.

**Reduced motion.** No press, no settle, no stamp fall: the confirmation prints with its stamp at rest. The transmitting state word still shows (it is information).

**Accessibility.** Labels are visible and above their fields. The select's options carry status as text (a screen reader choosing a buoy hears `silent since March` before committing). Errors are linked to fields with `aria-describedby` and summarised in a focusable head. The confirmation is a heading + text; focus moves to its head on arrival (the one place this theme moves focus — a document has arrived, and the reader is told). Contrast: all text per §2; the stamp's text is duplicated in the card body at full contrast.

**Performance & mobile variant.** One form, one request; negligible. Mobile: same leaf, native select, stamp at mobile size.

**Tokens.** `--chart-lit`, `--deep`, `--ink`, `--buoy`, `--orange-deep`, `--ease-stamp`, `--ease-drift`, `--stamp-rot: -6deg`, `--request-watchdog: 3000ms`.

### 6.14 The sounding (loader & page transition)

**What & why.** Before a chart is sounded, its depths are unknown; the office prints the chart's furniture first and sounds the water after. Loading in this theme is a *sounding*: the incoming page prints immediately as unsounded water — the graticule, the section labels, the card outlines with their heads already set — while contour ghosts (pale, dashed) mark where the bathymetry will lie, and a sounding line in the margin counts the fathoms as content arrives: `SOUNDING — 40 FM… 120 FM…` When the content lands, the contours ink in and the cards fill. Page transitions use the same furniture as a *chart veil*: a contour wipe crosses the viewport (the old chart is covered by a sheet of unsounded water sliding over it), the new page is already printed beneath, and the veil lifts. Waiting, in this office, is hydrography — and like §6.13's delay, it is honest: the sounding counts only while real loading is happening, and it is capped.

**Structure.** Skeleton state: the real page layout with real labels (heads, captions, table heads are text, never grey bars — a sounding chart has its labels before its depths), contour ghosts as dashed SVG paths in `--contour`, card bodies as empty `--chart-deep` frames with their inscription heads printed. The sounding counter is a mono line in the rail position. The veil: a fixed full-viewport layer in `--chart` with a contour band at its leading edge, translated by the loop during navigation transitions (client-side route changes only; full page loads use the sounding alone).

**Motion spec.** Sounding: contour ghosts pulse *not at all* (no shimmer — shimmer is a screensaver habit); the sounding counter increments as fetch milestones resolve (shell → record → images), each increment a cut, not a count-up; when content arrives, contours ink in over 500ms (`--ease-current`, opacity + stroke tone) and card bodies fill by cut. Veil: on route change, the veil crosses in 450ms (`--ease-current`), holds only until the new page's shell is ready (max 900ms), and lifts in 450ms. Total transition budget ≤1.8s worst case; typical 900ms.

**Choreography timeline.** Navigation: 0ms veil begins crossing · 450ms chart covered; new shell printing beneath · ≤900ms new page ready · veil lifts 450ms · sounding continues on the new page only if its record is still loading. First load: shell + labels at first paint · sounding line counts milestones · contours ink at record arrival · done — the state exits by completion, never by timer theatre.

**State matrix.** *Sounding:* labels printed, ghosts dashed, counter live. *Sounded:* full page; the sounding line is replaced by the chart's edition line (§6.10). *Veil crossing / lifting:* as above. *Stalled load:* at the watchdog, the sounding line prints `SOUNDING FAILED — SHOWING THE LAST CHART` and the cached/last-known content renders (every element in this theme has a last-known state; the loader's job is to reach one). *Disabled:* no skeleton — the server-rendered page simply arrives (skeletons are a client-side courtesy, never a gate on content).

**Content-merge.** The skeleton is the page's own chart with its soundings missing — labels, structure, and geography present; only the depths (data) pending. It teaches the page's shape while it waits, and its counter is the load's true progress in the office's units.

**Breakpoints.** ≥1200px: full sounding with rail counter. 768–1199px: counter moves to the masthead's edition line position. <768px: sounding counter under the chart title; veil crossing shortens to 300ms each way (small screens, shorter patience, same honesty).

**Edge cases & failure modes.** Instant load (cache): the sounding may never appear — the shell-to-content path skips it if the record resolves before first paint + 150ms (no skeleton flash for a fast answer; the office doesn't perform soundings it doesn't need). Partial load (record yes, images no): cards fill, photographs arrive per §6.11's fallback rules. Repeated rapid navigation: the veil never stacks; a new navigation during a crossing cuts the veil to the newest page.

**Fallback & watchdog.** **Watchdog: 2400ms** — if the record hasn't resolved, the sounding ends into the last-known state with its printed admission. The veil's own watchdog: 1800ms from crossing start, it lifts regardless — a veil that never lifts is a blank page wearing a costume.

**Reduced motion.** No veil crossing (route changes are cuts) and no contour ink-in (contours print at final tone when content arrives). The sounding counter still counts — it is data, in mono, by cuts.

**Accessibility.** The sounding state carries `aria-busy="true"` on the main region and the counter is *not* a live region (milestone text is available to read, not announced repeatedly). Labels present in the skeleton mean the page's heading structure is complete during loading — a screen reader meets the chart's shape immediately. The veil is `aria-hidden` and never blocks focus (focus moves to the new page's heading only after the veil lifts).

**Performance & mobile variant.** The skeleton is the page's own DOM — no extra payload beyond the ghost contours (≤4KB). Veil is one transformed layer. Mobile: shortened veil, same sounding.

**Tokens.** `--chart`, `--chart-deep`, `--contour`, `--deep`, `--ink`, `--ease-current`, `--sounding-watchdog: 2400ms`, `--veil-cross: 450ms`.

### 6.15 The chart-office footer (the desk at the bottom of the chart)

**What & why.** The footer is printed on `--deep` — the office's desk at the bottom of the chart, the one licensed full-bleed deep surface (§2). It carries the network's totals in their third printing (hero, table, footer — three printings that must agree, §10 audits them): `412 BUOYS IN THE NETWORK · 401 REPORTED IN THE LAST 24 HOURS · 11 SILENT`, the chosen buoy's closed line (`22914 — 5,603 KM — SILENT SINCE MARCH`), a miniature of the drift route drawing itself once along the footer's top rule (the voyage, at desk scale), the chart's correction line (`CHART DBN-01 · EDITION 2026 · CORRECTED TO 14 NOV 2026 — CORRECTIONS ARE PRINTED, NEVER SILENT`), and the office's ordinary furniture: contact, data licence, the API's plain link. The footer merges because it is where the office signs its work — totals, corrections, and the route, in the chart's own hand.

**Structure.** A `<footer>` on `--deep`, chart-coloured text (7.4:1). Top rule with the route miniature: an SVG path (the ledger's eight positions, simplified to the footer's 1200×36 viewBox) drawn by §6.2's dash mechanism, one-shot on first arrival. Totals as a data-register line; the correction line in inscription register; link columns in Newsreader with mono marks. The footer's buoy glyph in `--buoy` — orange's last licensed appearance on the page.

**Motion spec.** The route miniature draws once when the footer first enters the viewport (1200ms, `--ease-current`, dash-driven by the loop) — the voyage retraced at the desk, slowly, the way you'd run a finger along it. Links: underline draws 240ms on hover/focus. Nothing else moves; a desk does not perform. The totals do not count up in the footer — by the bottom of the page, the numbers are facts, not events (counting is §6.18's hero job).

**Choreography timeline.** Footer enters: 0–1200ms route draws · then rest, permanently. Repeat visits: route printed drawn (sessionStorage, as §6.1's short form).

**State matrix.** *Rest:* fully printed footer. *Drawing:* the one route draw. *Scrolled-past:* drawn state persists. *Disabled:* route printed drawn; totals printed — the footer is complete as print. *Touch:* identical.

**Content-merge.** The footer's numbers are the record's numbers in their third printing; its correction line is the site's real versioning practice; its route is the story the reader just read, at signature scale. A footer that repeated the hero's *marketing* would break the merge; this one repeats the hero's *arithmetic*.

**Breakpoints.** ≥1200px: totals on one line, three link columns. 768–1199px: totals wrap to two lines, two columns. <768px: totals stacked (one figure per line — at phone width the tally reads like a list, which suits it), one column, route miniature full width at 24px tall.

**Edge cases & failure modes.** Totals that disagree with the hero (a record updated mid-session): the footer prints the *newer* record and the correction line gains `· CORRECTED DURING THIS VISIT` — the office shows its working rather than letting two printings contradict in silence. Long correction histories: the line prints the latest correction only, with a link to the full corrections page (§7).

**Fallback & watchdog.** Static print; the route draw is the only enhancement, under the shared 3000ms watchdog (snap to drawn). No-JS: complete footer.

**Reduced motion.** Route printed drawn. Links' underlines by cut.

**Accessibility.** Real footer landmarks and link lists. The route SVG is `aria-hidden` (its data is the story, already read). Totals are text at 7.4:1. The correction line is text, not a badge.

**Performance & mobile variant.** One small SVG (≤2KB), one draw. Mobile: stacked totals, same content.

**Tokens.** `--deep`, `--chart`, `--buoy`, `--ink`, `--ease-current`, `--footer-route-h: 36px`.

### 6.16 The uncharted page (404)

**What & why.** Waters no buoy reports from. The 404 is a chart of an empty ocean: graticule, contours, no dots, no ripples — and in the middle of the empty chart, the office's line in inscription register: `NO BUOY REPORTS FROM THESE WATERS.` Beneath it, in Newsreader, one honest sentence (the address was wrong, or the buoy was retired, or the page drifted) and the chart's useful exits: the fleet, the story, the follow-a-buoy form — the three harbours of the site. Its choreography is specified as *none*: no buoy answers here because there is no buoy here, and an ambient ripple on the 404 would be the theme's saddest lie — the office does not fake a signal in empty water.

**Structure.** A page on the chart ground with the masthead (§6.10) and footer (§6.15) in place; the centre is an SVG chart region (empty — graticule and contours only, its emptiness is the content) with the inscription line set across it in Archivo, and the exit links as a chart index list with mono marks. The chart region ships with a printed sounding in its corner: `DEPTH BELOW — UNCHARTED` in mono — the one joke the office permits itself, and it is a data joke, told in the data register.

**Motion spec.** None. The page loads complete. (The masthead's rule draw is also suppressed here — even the frame is quiet on an uncharted page.)

**Choreography timeline.** Empty, deliberately — §13's map does not include this page; uncharted water is not on any route.

**State matrix.** *Rest:* the printed empty chart — every state is this state. *Hover/focus:* exit links underline as usual (§6.10's link treatment). *Disabled / reduced / touch:* identical.

**Content-merge.** The 404 is the theme's world holding at its emptiest: a real chart of a place with nothing in it, filed by the same office. Its exits are the site's real harbours, indexed like chart entries.

**Breakpoints.** ≥1200px: chart region 60vh. 768–1199px: 48vh. <768px: 40vh, exits stack. The emptiness scales down but never disappears — a 404 with no empty water in it has missed its own point.

**Edge cases & failure modes.** A retired buoy's URL (a *known* absence): the page adds one line — `BUOY 18— WAS RETIRED IN 2023. HER RECORD IS IN THE LEDGER.` with the link — because the office distinguishes *never existed* from *no longer reporting*, and the distinction is the theme in miniature. A 500 variant: same chart, the line reads `THE OFFICE CANNOT REACH THE RECORD — THE CHART IS SAFE.` and the exits are the cached pages.

**Fallback & watchdog.** Static; returns a real 404 status. No watchdog — nothing is loading.

**Reduced motion.** Identical (there was never motion).

**Accessibility.** A real `<h1>` ("No buoy reports from these waters"), exits as a labelled nav list. The empty chart is `aria-hidden`; its sounding line is text. The page is fully usable with the chart region ignored entirely.

**Performance & mobile variant.** The lightest page on the site: no record fetch, no loop. Mobile: as above.

**Tokens.** `--chart`, `--contour`, `--deep`, `--ink`.

---

### 6.17 The voyage ledger (the one data record)

**What & why.** Every figure on every page of this theme traces to one declared record: the voyage ledger of BUOY 22914, plus the fleet record it sits inside. The ledger is an element — the most important one — because the theme's law (§1) is enforceable only if there is exactly one place the truth lives. It holds: the deployment (13 May 2024, from RV *Meridian*, 18°12′N 042°30′W, drogue at 15 m); the forty weekly transmissions (the home page prints eight of them — W01, W06, W12, W19, W25, W31, W36, W40 — the detail page prints all forty); the fragment of W41; the derived fields the office computes honestly from transmissions (drift distance to date, stamp ink, depth below); and the silence (first missed report 03 Mar 2025). The fleet record holds the network's figures (412 tracked, 401 reporting, 11 silent), each buoy's interval and next-report time (§6.7), the signal delay (700ms, §6.6), and the follower roll (1,208, §6.13). A builder who hard-codes any of these numbers anywhere else has failed the build — §10's audit greps for the literals outside this record and its generated printings.

**Structure.** A single data object (JSON or equivalent), versioned with the chart edition, from which every printing is generated:

```
buoy: {
  id: "22914", deployed: "2024-05-13", vessel: "RV Meridian",
  deployPos: "18°12′N 042°30′W", drogueM: 15,
  reports: [   // the eight printed on the home page; the record holds all 40
    { week: 1,  date: "2024-05-20", pos: "18°41′N 044°58′W", sst: 26.4, battery: 87, driftKm: 212,  depthBelowM: 180,  wander: 1.0, stampInk: 100 },
    { week: 6,  date: "2024-06-24", pos: "21°03′N 052°17′W", sst: 27.1, battery: 81, driftKm: 891,  depthBelowM: 640,  wander: 1.0, stampInk: 94 },
    { week: 12, date: "2024-08-05", pos: "24°36′N 061°02′W", sst: 28.3, battery: 74, driftKm: 1764, depthBelowM: 980,  wander: 1.2, stampInk: 87 },
    { week: 19, date: "2024-09-23", pos: "29°58′N 070°44′W", sst: 27.6, battery: 65, driftKm: 2690, depthBelowM: 1450, wander: 2.2, stampInk: 78 },
    { week: 25, date: "2024-11-04", pos: "35°22′N 068°19′W", sst: 24.9, battery: 56, driftKm: 3588, depthBelowM: 2900, wander: 1.4, stampInk: 69 },
    { week: 31, date: "2024-12-16", pos: "38°47′N 058°36′W", sst: 18.2, battery: 44, driftKm: 4402, depthBelowM: 2600, wander: 1.8, stampInk: 57 },
    { week: 36, date: "2025-01-20", pos: "40°15′N 049°08′W", sst: 11.6, battery: 27, driftKm: 5117, depthBelowM: 4300, wander: 1.0, stampInk: 40 },
    { week: 40, date: "2025-02-17", pos: "41°02′N 043°51′W", sst: 8.9,  battery: 4,  driftKm: 5603, depthBelowM: 4850, wander: 0.6, stampInk: 35, stampNote: "RE-INKED BY HAND — FORMULA GIVES 17" }
  ],
  fragment: { week: 41, begun: "2025-02-24 07:40 UTC", pos: "41°0—′N 043°—′W", sst: "8.—", battery: null },
  firstMissedReport: "2025-03-03", silentSince: "MARCH 2025"
}
fleet: { tracked: 412, reporting24h: 401, silent: 11, heroRollCallStart: 388, heroStations: 14,
         signalDelayMs: 700, followers: 1208 }
```

The derived fields obey printed rules, stated here so any builder derives identically: leg distances are the differences of consecutive `driftKm` (212, 679, 873, 926, 898, 814, 715, 486 — summing to 5,603); `stampInk = clamp(battery + 13, 35, 100)`, with the W40 intervention recorded in `stampNote` rather than hidden; the battery's between-report behaviour is §6.4's step-and-glide; `wander` scales §6.2's spline offsets per leg.

**Motion spec.** The ledger itself does not move. Its printings move (§6.1–§6.18), each reading from the record at the moment of printing. When the record updates mid-session (a buoy reports), printings update by their own elements' rules — the table's tick (§6.12), the tallies (§6.18) — never by a global re-render.

**Choreography timeline.** None of its own; it is the score the other elements' timelines are written from. Its one temporal rule: a printing always shows the record as of its print moment, and §6.15's footer states the record's edition time so a stale printing can be recognised as one.

**State matrix.** *Loaded:* the full record; all printings live. *Partially loaded (fleet yes, voyage no):* fleet surfaces print; the story column prints its server-rendered HTML (which ships the eight reports as static content) and the live mechanisms (scrub, stamps' landings) arm only when the record arrives — the story is never held hostage by its own data layer. *Failed:* every surface falls to its last-known state with its printed admission (§6.12, §6.14); the silence section (§6.9) is unaffected — it is static content. *Stale (record older than its edition claims):* the footer correction line prints the record's true timestamp; the office does not freshen a date.

**Content-merge.** The ledger is the content, declared. Every other element in §6 is a printing of it, a mechanism over it, or — in §6.9's case — the faithful display of its final, broken entry.

**Breakpoints.** The record is size-independent; its printings carry the breakpoint rules. The one layout fact the record dictates at small sizes: positions and timestamps never wrap mid-figure (mono lines are `white-space: nowrap` with the card allowed to grow) — a coordinate broken across lines is a coordinate misread.

**Edge cases & failure modes.** A report with a missing field: the field is `null` in the record and prints as `—` everywhere (never interpolated — the office does not average a battery). Two reports with the same week: the record keeps both, the second flagged `DUPLICATE — UNDER REVIEW` in its printing (§6.12's rule, applied here at the source). A battery that rises between reports (a warm week recovering a cold-sagged cell — it happens): the record prints the rise; §6.4's glide travels *up* to it and the W-card's note explains the sag recovery — the law is traceability, not monotonicity, and the one place the fiction of a smooth decline would be easier is exactly where the record refuses it. (In 22914's printed eight, no rise occurs; the rule exists for the other forty and for other buoys' ledgers.)

**Fallback & watchdog.** The record's fallback is the server-rendered printing of itself (the story, table's first page, and tallies ship as HTML). **Watchdog: 2400ms** (shared with §6.14) — surfaces waiting on the record resolve to last-known at that bound, with admissions printed.

**Reduced motion.** No effect on the record; its printings carry their own variants.

**Accessibility.** The record is data; its printings carry the accessibility specs. The one rule that belongs here: every figure in the record must have a text printing somewhere at full contrast — there is no canvas-only or colour-only fact in the ledger.

**Performance & mobile variant.** The voyage record is ≤8KB JSON; the fleet record's full 412 rows are paginated server-side (§6.12) and never shipped whole to a phone. The hero sample (14 buoys) ships inline.

**Tokens.** `--record-edition` (the chart edition string), `--signal-delay: 700ms`.

### 6.18 Counters that tell the truth (the tallies)

**What & why.** The network's tallies — buoys tracked, buoys reporting, buoys silent — appear three times on the home page (hero, fleet section head, footer) and they obey the office's arithmetic: a tally counts only events, it travels only between true values, and it never starts from zero for drama. The hero tally is the worked example: when the visitor arrives, the day's roll-call is already running and 388 buoys have reported; the hero sequence (§6.1) adds the last 13 stations one by one — each increment synced to a real ripple on the chart — and the tally settles at 401, where it holds, captioned `OF 412 IN THE NETWORK · 11 SILENT`. The three numbers always reconcile: 401 + 11 = 412, in every printing, on every page, and §10's audit checks the reconciliation mechanically. A tally in this theme is a small ledger, not a firework.

**Structure.** Mono figures (Data register; Data large in the hero) generated from the fleet record, each with its caption line in inscription register. The hero tally is a loop-registered value driven by §6.1's sequence events (increment per station, not per frame — the count changes when a buoy reports, which is the only reason a count may change). Other printings are static text from the record. A tally's accessible text always states the full fact ("401 of 412 buoys reported in the last 24 hours; 11 are silent"), whatever the visual figure shows mid-count.

**Motion spec.** Hero: 13 increments across §6.1's ≈4.9s sequence, each a single integer step landing with the station's ripple (the figure changes *because* the ripple fired — cause and effect in the right order), with a 120ms `--ease-resonate`-free settle — no overshoot: a count that overshoots 401 to 403 and comes back would be a count that lied twice. Between increments, stillness. Fleet-section and footer printings: no motion at all. A mid-session record update (a buoy reports while the visitor reads the fleet page): the reporting tally steps +1 at the moment of the §6.7/§6.12 event, and if the buoy was silent, the silent tally steps −1 in the same beat — the reconciliation is maintained live, or the tallies freeze rather than disagree (see Edge cases).

**Choreography timeline.** Hero: increments at §6.1's station times (+400ms … +3520ms), settling at 401 with the last ripple. Elsewhere: none. The battery (§6.4) is *not* one of these tallies — it is a gauge reading one buoy's transmissions, and its separate spec is deliberate: tallies count the fleet's events; the battery spends one life.

**State matrix.** *Rest:* tallies at the record's true values. *Counting (hero only):* between stations, the figure holds the last true intermediate value (388 + stations so far — every intermediate is itself a true count of reports received, never an interpolation). *Updated mid-session:* step changes per the rule above. *Scrolled-past:* settled values persist; the hero tally does not recount on return. *Disabled:* printed true values. *Touch:* identical.

**Content-merge.** The tallies are the fleet record's headline figures, printed beside the things they count (the chart, the table, the desk). Their captions name what is counted and over what window (`IN THE LAST 24 HOURS`) — a tally without its window is a number without a unit, and Type law 1 forbids it company.

**Breakpoints.** ≥1200px: hero tally Data large (22px) beside the chart title. 768–1199px: 19px, under the title. <768px: the hero tally moves into the caption strip under the chart (§6.5's strip) at 16px; the increments still sync to the (reduced) roll-call, and the caption carries the full reconciliation in text.

**Edge cases & failure modes.** A record update that would break reconciliation (reporting + silent ≠ tracked — a data bug): the tallies freeze at their last reconciled values and the fleet section prints `TALLY UNDER REVIEW — THE ROLL IS BEING RECOUNTED` — the office would rather show a held number with an admission than a live number that doesn't add up. A visitor arriving after all stations have called (record's roll-call complete): the hero tally prints 401 statically; §6.1's sequence still performs the last stations for the chart's sake, but the tally does not pretend to recount — it holds, and the caption's window line carries the fact. Negative or null fields: printed as `—` with the §6.17 gap rule.

**Fallback & watchdog.** Tallies ship printed at their true values; the hero's counting is armed by JS over the printed 401 (the DOM's first state is the *final* true value, and the count-down-to-388-and-up is the armed performance — if JS never arms, the visitor simply sees the truth without the roll-call's arithmetic, which is the correct degradation order). Loop stall mid-count: the shared **watchdog (3000ms)** snaps the tally to 401.

**Reduced motion.** No counting: tallies print at their true values. Mid-session updates arrive by cut.

**Accessibility.** Tallies are text; the counting is not announced (no live region — a screen reader reads the final true sentence, which is in the DOM from the start as the tally's accessible text). Tabular figures throughout, so a changing tally never shifts layout (CLS 0).

**Performance & mobile variant.** Integer steps at event times; zero per-frame cost. Mobile: caption-strip placement, same rules.

**Tokens.** `--ink`, `--deep`, `--signal-deep`, `--ease-drift`, `--tally-hero-size: 22px`.

---

## 7. Page application map

**Home (the chart of the network).** The reference build §8 walks through: masthead (§6.10), reporting-in hero (§6.1) with the tallies (§6.18), the story column — pinned ID card and drift line (§6.4, §6.2) beside the eight printed weekly reports (§6.3) over deepening bathymetry (§6.8) — then the last transmission (§6.9), a fleet section of six biography cards (§6.11), the follow-a-buoy form (§6.13), and the chart-office footer (§6.15). The fleet table (§6.12) appears on the home page only as its first page behind the fleet section's `THE FULL ROLL` link — 412 rows are a destination, not a homepage section.

**Listing page (the fleet).** Biography cards (§6.11) paginated 24 at a time with the count printed (`PAGE 1 OF 18 — 24 OF 412`), filters in the §11 select treatment (basin, status, battery band), and the fleet table (§6.12) as the alternate view (a printed toggle: `CARDS / ROLL` — the same record, two filings). No drift line, no pinned card: those belong to 22914's story, and reusing them as listing furniture would spend their meaning (§9). The hero of a listing page is a quiet chart with ambient ripples (§6.7) and the tallies.

**Detail page (one buoy).** The buoy's own story page, built exactly like the home story column but from that buoy's ledger: its pinned ID card, its drift line (if it has transmitted positions enough to draw one — a buoy with one transmission has a dot, not a line, and the page prints the dot), all its report cards (22914's page prints all forty + the fragment + §6.9 verbatim), its deployment photograph large, and the follow form (§6.13) pre-set to it. A reporting buoy's page ends not with silence but with its next scheduled report: `NEXT REPORT — WHEN SHE WAKES, ≈ 6 HOURS` — the living get a future tense; the page grammar knows the difference.

**About (the office / the programme).** Text on the chart: how buoys are built, deployed, and lost; the office's methods (how a position is fixed, why a battery figure can be trusted, what "silent" means and what it doesn't — a silent buoy is *unheard*, not known sunk, and the About page is where the office says so in full sentences). Specimen furniture: a buoy's anatomy diagram in the chart's line style, deployment photographs (§6.11's frames). No story column; the drift line appears once, as a labelled diagram of how a track is drawn — a diagram, marked as one, because the office distinguishes exhibits from evidence.

**Contact / data requests (the office door).** The §11 form system on a chart-lit leaf: name, office (affiliation), the data wanted, in plain fields. Researchers requesting the raw record get the ledger's own formats (the record is downloadable as printed data — CSV/JSON — with its edition line). No chart theatre on this page beyond the masthead and ground: correspondence is paperwork.

**Checkout / donations (fund a buoy).** **Routed out of the chart's theatre**, as other document-themes route payment out: a plain chart-lit surface (§11 buttons/inputs at their calmest), no ripples, no stamps performing, no drift line. The confirmation, however, returns to the office: it prints as a stamped filing — `DEPLOYMENT FUNDED — BUOY Nº PENDING ASSIGNMENT` — because a confirmation is a document, and documents are where this theme is strongest. The funded buoy's eventual ID is emailed when assigned; the confirmation never invents one on the spot.

**The uncharted page (404/500).** §6.16, verbatim.

---

## 8. Worked examples

### 8.1 The hero — "A live chart of wanderers" (the roll-call)

**The scene.** An ocean-data nonprofit's home page. The visitor arrives at a chart: pale chart ground, graticule, contours of the North Atlantic shelf, fourteen orange dots scattered like a fleet at anchor in print. The chart title in Archivo: "A live chart of wanderers." Beneath it, the tally line in mono: a figure and its caption.

**Scroll timeline.** 0ms: first paint — the static chart is complete: all fourteen dots printed, the tally reading `401` with its caption `OF 412 IN THE NETWORK · 11 SILENT`, and along the chart's bottom edge a strip of ID cards, the last one — BUOY 22914 — already raised, marked LAST KNOWN. The page is whole before anything moves. +400ms: the armed performance begins — the tally steps *back* to 388 (the roll-call's state when the visitor arrived; the caption gains `ROLL-CALL IN PROGRESS`), and the stations call in: a ripple blooms at a dot off Bermuda, its card flips up along the bottom edge — `BUOY 30772` — holds, settles. Another, in the South Atlantic. Another. The tally climbs in step: 389, 390… The visitor watches a network wake up in the order its own list dictates. +3520ms: the thirteenth ripple; the tally reaches 401 and the caption drops its progress line. +4220ms: the last live card settles. Then — the beat the whole hero exists for — 500ms of nothing. +5220ms: 22914's card, already raised in the static print, is *confirmed* by a slow brightening of its LAST KNOWN line — no ripple, no flip; the office's hand resting on the card a moment. +6120ms: ambient ripples arm somewhere distant on the chart, and the hero is at rest: a working chart, one card kept by hand.

**Build notes.** Everything here is §6.1 + §6.18 + §6.7 composed; the only hero-specific decisions are the headline and the fourteen-station sample, both in the record. If JS never arms, this hero is pixel-for-pixel the static composition — chart, tally at truth, card raised — which is why the static layer is specified first in §6.1 and the performance second.

### 8.2 Mid-page — Week 19, the storm leg

**The scene.** Deep in the story column. The reader has passed W01's fair departure, W06, W12's quickening. The drift line in the margin has been wandering politely. The pinned card reads `WEEK 12 · BATTERY 74%`. Now the W19 section approaches — and the chart changes character: the contour bands beneath the section have stepped darker (the shelf is falling away, §6.8), and the drift line above the reader's position has swung *wide* — great lateral loops in the margin, the spline at its storm amplitude (×2.2).

**Scroll timeline.** The W12 card's stamp is already struck (87% ink — still strong). As the reader scrolls into the storm leg, the line's tip tows through the wide swings, lagging at the 0.09 lerp so the loops draw like something being dragged through weather. The pinned card crosses W19's threshold: week and position cross-fade (120ms) — `WEEK 19 · 29°58′N 070°44′W` — and the battery counts down 74 → 65 over 900ms, integer steps, landing just as the reader reaches the card. The W19 report card itself: its data block prints the week's facts (SST 27.6°C, drift to date 2,690 km), and its prose is the office's storm note — a hurricane passing east of the buoy, the drogue holding, the buoy riding out three days of swell and reporting on schedule, because reporting on schedule is what she does. As the card's head crosses 70% viewport, its stamp falls — at 78% ink. The reader who has been watching the stamps can *see* the difference from W01's full-strength strike without being told. Below, the W25 section waits, where the line will straighten into the Stream and the prose will turn almost cheerful — the fastest water of her life.

**Build notes.** The beat is §6.2 (amplitude from the ledger's `wander` field) + §6.4 (threshold figures) + §6.3 (stamp at the formula's 78%) + §6.8 (band 3 tones) arriving together from one scroll value — the section is the theme's argument that four mechanisms reading one record feel like one world, while four mechanisms with four data sources feel like a template.

### 8.3 Conversion — "Follow her" (the form, at the story's end)

**The scene.** The reader has finished the story: the fragment, the whitespace, the silence line. The footer is still below. Here, between the silence and the desk, sits the follow-a-buoy leaf (§6.13) — placed after the ending deliberately, because the reader who has just watched a buoy spend its battery is the reader who understands what following one means. The leaf's head reads `1,208 PEOPLE FOLLOW BUOYS OF THIS NETWORK`. The select is pre-set — not to a living buoy, but to `22914 — NORTH ATLANTIC — SILENT SINCE MARCH`, because that is whose page this is.

**Scroll/submit timeline.** The reader opens the select, considers the living — hovers 30772 and somewhere on the page's chart the dot answers with a ripple (§6.5 via §6.13) — then keeps 22914. They type their email and press the stamp key. `TRANSMITTING…` for the request's true 600ms. The leaf settles; at +250ms a stamp falls on the confirmation card: `FOLLOWER Nº 1,209`. The card's body, in mono and Newsreader: `BUOY 22914 — SHE IS SILENT. YOU WILL RECEIVE HER RECORD — ALL FORTY WEEKS AND THE FRAGMENT — AND WORD IF SHE IS EVER HEARD AGAIN.` Then the office's closing sentence (§12's fixed string): "The network goes on. So does she — drifting still." The reader has not been sold anything. They have been filed, kindly, into the paperwork of a network that keeps its dead on the roll — and the confirmation's number, 1,209, is the printed 1,208 plus one, auditable by anyone who scrolls up and checks.

**Build notes.** The no-JS path posts and returns this same confirmation server-rendered. The duplicate path (this email already follows 22914) prints `ALREADY ON THE ROLL — FOLLOWER Nº 843` with the original number. The error path preserves every field. §10's gate exercises all three.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A stock map with pins.** A Google-Maps-style basemap, a generic world map SVG, location pins teardropping onto continents — the clip-art of "global network." *Cure:* the chart is drawn in the theme's own line (graticule, contours, chart ground) and the "pins" are buoy dots with IDs; §10's review rejects any basemap asset.
2. **A rotating globe hero.** The 3D earth, the arcs between glowing cities — satellite-marketing wallpaper. *Cure:* the hero is a flat working chart and a roll-call (§6.1). The theme's claim is a ledger, not a planet.
3. **Invented live data.** A "live" counter ticking up by random increments, positions jittering to feel alive, a fake real-time feed. *Cure:* the law (§1) and §6.17 — every figure traces to the record; ambient events fire on the record's schedule (§6.7); §10's one-record audit greps for stray numerals.
4. **Rounded network numbers.** "400+ buoys!" "Over 5,000 km!" — marketing rounding that a scientist reader catches instantly. *Cure:* Type law 3 — 412, 5,603, 4%. The exactness is the brand voice.
5. **The drift line as decoration.** A wavy line reused as a section divider, a footer squiggle, a logo flourish. *Cure:* the line exists only as §6.2, drawn from transmitted positions, on story pages. §6.15's miniature is the one licensed echo, and it is the same data at desk scale.
6. **A cheerful silence.** The last transmission played for uplift — swelling fade-in, "her journey continues in our hearts," a bobbing buoy illustration. *Cure:* §6.9's refusals — no motion, no ripple, whitespace and one line. Sentimentality here is a lie about what happened.
7. **Stamps as clip-art.** A grunge-texture stamp PNG, rotated randomly per card, identical ink on every card. *Cure:* Type law 5 + §6.3 — live text, formula opacity, the re-ink admission on the last card.
8. **Glassmorphism stat cards.** Frosted panels floating over a wave photograph with big rounded numbers. *Cure:* the theme's figures live in the pinned ID card, the report data blocks, and the tallies — paper on a chart, mono type, rules not shadows.
9. **A wave photograph hero.** A beautiful stock breaker as the homepage's face. *Cure:* the chart is the face (§6.1); photographs exist only as deployment records with captions of fact (§6.11).
10. **Counters from zero.** The network tally spinning 0 → 401 on load. *Cure:* §6.18 — the count begins at the true 388 because the roll-call predates the visitor; a from-zero count claims the network started when the page loaded.
11. **Instant answers.** Click a buoy, get its report in the same frame, with a spinner for decoration. *Cure:* §6.6's honest 700ms and its printed reason. Latency is the world's physics; faking instantaneity is faking the ocean.
12. **Orange everywhere.** Buoy orange as the link colour, the button fill, the headline accent — until it means "brand" instead of "hardware." *Cure:* §2's rationing — orange is where a buoy physically is, plus the position cross and the stamp glyph; §10's orange census counts it per viewport.

## 10. Quality gate

The build may not ship unless **every** blocking check passes. A non-builder signs the gate.

1. **One-record audit.** Grep the build for the ledger's literals (`22914`, `5,603`, `412`, `401`, `87%` outside generated printings) and for any numeral in a data register that does not trace to §6.17 or the fleet record: zero strays. Every printing — stamps, card, table, tallies, footer — is generated from the record.
2. **Reconciliation audit.** Mechanically verify, on every page type: reporting + silent = tracked (401 + 11 = 412); the eight printed legs sum to 5,603 km; the hero tally's start + stations = its settle (388 + 13 = 401); the form's confirmation number = printed followers + 1.
3. **Stamp-formula audit.** For each printed report, computed stamp opacity = `clamp(battery + 13, 35, 100)`; the W40 card carries its re-ink note verbatim; no stamp is an image (DOM text check).
4. **Silence test.** In §6.9's section: no animation runs, no ambient ripple fires within its viewport, no hover answer beyond the silent protocol, at any scroll speed, for a full 60s dwell. Any motion in the silence fails the build.
5. **No-JS pass.** With JavaScript disabled: hero complete with tally at truth and 22914's card raised; story fully printed with stamps at rest; battery range line present; table's first page and form functional; the silence intact.
6. **Reduced-motion pass.** With `prefers-reduced-motion`: full track drawn, stamps printed un-landed, no roll-call, no ripples, tallies at truth, form confirmation by cut — all content identical.
7. **Watchdog drill.** With the shared loop artificially stalled: stamps snap at 1600ms, hero settles at 5000ms, report requests resolve at 3000ms, sounding ends at 2400ms, tallies snap to truth — and no printing is ever left showing a value the record contradicts.
8. **Contrast audit.** Body ink-on-chart ≥11:1 measured; no `--buoy` or `--signal` running text anywhere ( DOM scan for colour usage on text nodes); stamp text duplicated in data blocks; footer text 7.4:1.
9. **Orange census.** Per viewport at any scroll position: orange appears only as buoy dots/rings, the chosen marker, position cross, stamp glyphs, and the footer's buoy glyph. A orange button or link anywhere fails.
10. **Delay honesty test.** §6.6's request: measured delay within 600–900ms; the card's delay line printed; a silent buoy's request returns its last transmission with the no-answer line — never a fresher invention.
11. **Performance budget (§14) verified** on a mid-tier Android over throttled 4G: LCP ≤2.5s, per-frame loop ≤0.6ms with ambient armed, no long task >50ms during the roll-call.
12. **404 honesty.** The uncharted page returns a real 404, contains zero buoy dots and zero ripples, and its exits resolve.

---

## 11. Component inventory

Every ordinary component, with its chart-office treatment — or its refusal and replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | The **stamp key**: a `--deep` key with a `--chart` inscription-register label and a 1px pressed travel (120ms settle); used once per view (the form's "Follow this buoy", a funding action) — it strikes, it does not glow |
| Secondary button | Chart key: `--chart-lit` face, `--deep` 1px edge, ink label; hover warms the edge; the edge is a rule, not a radius — corners are square throughout the theme (charts and cards are cut paper) |
| Text link | Ink, underline draws left-to-right 240ms; visited links deepen to `--deep` (a read chart is a used chart); data links (IDs, coordinates) are mono and underline in `--orange-deep` |
| Inputs (text/email) | Chart-leaf fields on `--chart-lit`, 1px `--deep` rule beneath, label above in Archivo 600; focus: the rule thickens to 2px and the label gains the position cross `+` in `--buoy` — the field you are in is the position you are at |
| Select | Native `<select>` in a chart field with a `--deep` chevron — the buoy picker (§6.13), the table filters (§6.12); options carry status as text; never a custom listbox |
| Radios / checkboxes | **Position squares**: small `--deep`-ruled squares that take a position cross (drawn, 160ms) when checked; radios are the same squares in a circle rule — the mark is always the navigator's cross, never a filled dot blob |
| Tabs | **Chart index tabs** (fleet view CARDS / ROLL, §7): inscription-register labels on a `--deep` rule, the active tab's rule thickens and gains the cross; content swaps by cut |
| Accordion | **Log folds**: a section that opens downward like a logbook leaf — content prints behind a settling rule (400ms, `--ease-current`); one open at a time; headings are real buttons (the forty reports on a detail page file this way) |
| Table | §6.12's fleet table is the pattern for all tables: chart-lit leaf, deep header, mono data columns, printed pagination |
| Cards | §6.3 report cards and §6.11 biography cards are the two card species; there is no third, generic card |
| Badge / tag | **Refused as pills.** A status is a data-register line (`REPORTING`, `SILENT SINCE MARCH`) printed in ink or `--signal-deep` — never a coloured chip |
| Alert / banner | A **notice bed**: a `--chart-deep` strip with a `--deep` left rule and the message in body text; errors use `--orange-deep` text (never an orange fill, never red — the office has no red) |
| Toast | **Refused.** Outcomes are documents (the stamped confirmation, §6.13) or notice beds that persist until dismissed; nothing in an office vanishes after four seconds |
| Modal | The **chart drawer**: a `--chart-lit` panel sliding from the chart's bottom edge over a `--deep`-at-88% scrim (the chart darkens like a drawer closing over the table); one maximum; Esc and scrim-click close; focus trapped and returned. Used for the full-record view of a buoy from the table — rarely, and never for marketing |
| Tooltip | A small chart label, data register, above its element after 400ms hover/focus — tooltips carry data (a buoy's last transmission time), never instructions |
| Pagination | Printed pagination: `PAGE 2 OF 17 — ROWS 26–50 OF 412` as text links (§6.12) — counts always stated |
| Progress bar | **Refused as a bar.** Progress is the drift line + battery (§6.2, §6.4); inside the form's transmitting state, the state word is the progress |
| Spinner | **Refused.** Waiting is a sounding (§6.14) or a signal delay (§6.6), both with printed reasons |
| Skeleton | §6.14's sounding — labels printed, depths ghosted |
| Breadcrumbs | The **position line**: `CHART / FLEET / BUOY 22914` in inscription register at a page's head, links underlining as usual — where you are, stated like a fix |
| Search | A chart field in the fleet section: search by buoy ID or basin; results are biography cards + table rows (the fleet's two shapes); a search for a silent buoy returns its card with its stamp — search does not hide the lost |
| Toggle ("Still the chart") | A labelled chart switch: kills ambient ripples (§6.7) for the session; state persists; `aria-pressed`. Named for what it does — the chart goes still, the data remains |
| Empty state | §12 voice: `NO BUOYS MATCH — THE NETWORK HAS NONE IN THESE WATERS WITH THAT STATUS.` (§6.12) — a true sentence and a way back |
| 404 | §6.16, the uncharted page |
| Footer | §6.15, the chart-office desk |

## 12. Copywriting voice

Two registers, one office.

**The Office register** (headlines, report-card prose, empty states, the footer's lines): the voice of the chart office that keeps this network — exact, unhurried, fond of its instruments, allergic to drama it cannot footnote. Sentence case, declaratives, numbers always with units and never rounded (Type law 3). Headlines name water, weather, and work: "A live chart of wanderers." / "The week the shelf fell away." / "She reported on schedule, in a hurricane." *Not:* "Meet the incredible journey of Buoy 22914!!" (exclamation marks are banned from the chart entirely — the ocean does not shout), not "Our revolutionary IoT platform leverages…" (the office keeps buoys; it does not leverage), not "Sadly, all good things…" (the office does not perform sadness; it prints the fragment).

**The Machine register** (data blocks, stamps, tallies, table cells, error facts): JetBrains Mono and the inscription settings — the buoy's voice and the stamp's. `WEEK 19 — TRANSMISSION RECEIVED` · `BATTERY 65%` · `DRIFT TO DATE 2,690 KM` · `SILENT SINCE MARCH`. Errors are written Office for the sentence, Machine for the fact: "The office didn't answer — your details are still here. — REQUEST TIMED OUT AT 3.0 S · Try again."

**Fixed strings (verbatim, do not paraphrase).**
- The silence line: "BUOY 22914 — SILENT SINCE MARCH. DRIFTING STILL."
- The confirmation's closing line (living buoy): "First report — when she next transmits." (silent buoy): "She is silent. You will receive her record — all forty weeks and the fragment."
- The story's closing sentence (§8.3): "The network goes on. So does she — drifting still."
- The network error: "The office didn't answer — your details are still here. Try again."
- The 404 line: "No buoy reports from these waters."
- The still-toggle: "Still the chart."

**Error voice.** Specific, preserving, and blameless: name the field and the fact ("The email needs an @ — we could not read it as an address."), never clear the form, never apologise in the abstract. **Empty-state voice.** A true sentence about the water plus the next true thing: no filter matches → the counts of what does exist; a basin with no buoys → "The network has no buoys in the South Atlantic gyre this season — the nearest reporting water is the North Atlantic, 38 buoys." **Label style.** Buttons are verbs from the world: "Follow this buoy", "Read its record", "Sound the chart" — never "Submit", "Click here", "Learn more" (say what will be learned: "Read how a position is fixed"). **Biography voice** (§6.11): Newsreader italic, the office's affection kept on a short line — one observed fact and at most one fond clause; a biography that reaches for poetry twice is cut to once.

## 13. Scroll choreography map

The whole home page, top to footer, in order. (Story pages run beats 2–7 per buoy; listing pages run 1, 8, and 10 only.)

1. **Arrival.** Static hero complete (chart, tally at 401, 22914's card raised). Masthead rule draws (600ms). The roll-call arms (+400ms).
2. **The roll-call.** Thirteen stations ripple and flip in record order; the tally climbs 388 → 401 in step; 500ms of stillness; 22914's LAST KNOWN line confirms. Ambient ripples arm.
3. **The story opens (W01).** Story progress `p` starts; the drift line's tip rests at the deployment's first fix; the pinned card reads WEEK 1 · BATTERY 87%; bathymetry at shelf tones (180m sounding in the rail).
4. **Fair legs (W06, W12).** Stamps land at 94%, 87% ink; the battery steps and glides 87 → 81 → 74; the line wanders politely; contours begin their fall.
5. **The storm leg (W19).** The line swings wide (×2.2) as it tows past; the shelf break completes beneath (1,000m sounding); the stamp lands at 78%; the card counts to 65%.
6. **The Stream and the winter (W25, W31).** The line straightens and lengthens its stride (W25, fastest water), then swings again, narrower (W31, ×1.8), over the seamount's brief shallowing; stamps at 69%, 57%; battery 56%, 44% — the LOW inscription joins the card below 30% at the next step.
7. **The weakening (W36, W40).** Wander slackens (×0.6 on the final leg); the stamp lands at 40%, then the last stamp — re-inked by hand to 35%, its note printed; the battery counts to 4% and the line's tip stops at the terminus dot. It will not move again.
8. **The silence.** The fragment, printed. 40vh of nothing. The silence line. The office's note. In the rail, the pinned card fades its battery to `—`, then NO SIGNAL; the card un-pins as the section ends — its watch is over.
9. **The fleet.** Six biography cards settle as reached; the tallies print at truth (no counting — facts now); ambient ripples continue on the fleet chart, sparse, unsynchronised.
10. **The follow leaf.** Choosing a buoy hails it; submitting transmits honestly and the confirmation is stamped — follower № 1,209 for the reader who came down the story.
11. **The desk.** The footer: totals in their third printing, the route miniature drawing itself once along the rule, the correction line. Stillness.

**Reverse pass.** Every beat runs backwards faithfully where it is a reading (drift line un-draws, battery re-reads earlier weeks, bathymetry shallows) and never backwards where it is an event (stamps, once struck, stay struck; the roll-call does not un-call). **Jump scroll.** Teleporting across the story snaps `p`-driven values to the landing point (the §6.2 rule); stamps for cards jumped *over* land in document order at 120ms intervals on arrival — the office files the paperwork for the weeks the reader skipped, because the record is complete even when the reading wasn't.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 700KB | Fonts ≤ 130KB (Archivo + Newsreader + JetBrains Mono subsets, `font-display: swap`); hero chart SVG ≤ 9KB; bathymetry ≤ 14KB; deployment photos ≤ 90KB each, ≤ 2 above the fold |
| Shared loop | One rAF; ≤ 0.6ms/frame with ambient armed | Registered values only; zero allocation in the loop; sleeps when settled and no chart is near |
| Ripple system | Pool of 6 nodes page-wide; ambient ≤ 3 concurrent | SVG attribute updates only |
| Drift/battery/bathymetry | Pure functions of one scroll value | Recomputed on scroll-frame, not per element |
| LCP | ≤ 2.5s on throttled 4G, mid-tier Android | The hero is DOM + static SVG at first paint — no canvas, no fetch gates LCP |
| CLS | 0.00 target | Card strip reserves its height; tally figures are tabular; images reserve aspect ratios; stamp positions are absolute within reserved card frames |

**Cut order when the budget is exceeded** (in this order, never silently): 1) ambient ripple rate (intervals ×2), 2) bathymetry contour density (every second line), 3) hero stations shown 14 → 10 (tally arithmetic unchanged — the caption is fleet-wide), 4) biography photograph settle (photographs print at rest), 5) the veil (§6.14) to cuts, 6) footer route draw to printed. **Never cut:** the record's printings, the stamps and their formula, the battery's truth, the silence's whitespace, any reduced-motion variant, any watchdog. A chart that must choose between its ripples and its record keeps its record.

## 15. Build-order checklist

1. **The record first.** Author §6.17's ledger and fleet record; generate all printings from it; write the reconciliation audit (§10.2) before any figure ships.
2. **Print the chart.** Static HTML/CSS: masthead, hero (static chart, tally at truth, card raised), story column with all reports and stamps at rest, the silence, fleet cards, table's first page, form (server path), footer. Verify the no-JS pass (§10.5) — the printed chart is the foundation, not a fallback afterthought.
3. **Typography & palette tokens** exactly as §2–§3; run the contrast audit (§10.8) and the orange census (§10.9).
4. **The shared loop** with the 0.09 lerp; register story progress `p` and wire §6.2 (line), §6.4 (card), §6.8 (bathymetry) to it — one cause, three readings, tested together.
5. **Stamps** (§6.3): arming, landing, the 1600ms snap; verify the formula and the W40 note.
6. **The roll-call** (§6.1) with its 5000ms watchdog and the tally's increments (§6.18); then ambient ripples (§6.7) with the concurrency cap and the silence exclusion.
7. **Hail and request** (§6.5, §6.6): the ripple pool, the silent protocol, the 700ms delay and 3000ms watchdog.
8. **Fleet surfaces** (§6.11, §6.12): cards, table, filters, printed pagination, the received tick.
9. **The form** (§6.13) end-to-end: hail-on-select, honest transmitting state, the stamped confirmation with its derived number, duplicate and error paths; test the no-JS POST.
10. **Sounding & veil** (§6.14) with both watchdogs; the uncharted page (§6.16) with its real 404.
11. **The silence drill**: §10.4's 60-second dwell test with the ambient scheduler forced active — nothing may fire.
12. **Reduced-motion variants** for every element; run §10.6.
13. **Mobile transformations**: rail dissolution, sticky strip card, table-to-list, caption-strip IDs.
14. **Performance pass** against §14 on real mid-tier hardware; apply the cut order if needed.
15. **The gate.** §10 signed by a non-builder — one-record, reconciliation, stamp formula, silence, watchdogs, orange census — before the theme may be used in a build.

---

*End of Theme 086 — The Drift Buoy Network (50x expansion). Identity preserved from the original entry: same concept, same five palette anchors, same three type families, all nine original signature elements deepened, and the theme's anti-slop heart kept intact — the final section is the buoy's last transmission, half a report and one line, because a network that writes everything down must also write down the silence.*
