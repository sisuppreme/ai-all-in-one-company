# X-Visual Detection Parameters — Visual Tells of AI-Generated Websites

Purpose: give any reviewer a repeatable, evidence-based checklist for spotting websites that were AI-generated or template-assembled rather than designed by a human professional. Each parameter names a concrete signal, the AI-typical pattern, the professional contrast, an exact check, known false positives, and a severity. Parameters are signals, not verdicts: single tells prove nothing; clusters do.

How to run the check: screenshot the page at a desktop width (1440px) and a mobile width (390px), full-page, with animations settled. Walk the parameters in ID order and mark each hit with a screenshot or a measured value. Apply the cluster rule: 3 or more minor tells inside one component or section count as one major. Record blockers individually; never average them away.

## Calibration

The Web Craft Pro Max research paper makes two quantitative claims. Both were re-checked against traceable sources on 2026-11-21. Verdicts:

**Claim 1 — "Humans detect AI-generated websites at ~55.5% accuracy." Verdict: PARTIALLY SUPPORTED; the exact figure is untraceable.**
No peer-reviewed study reporting 55.5% for AI-generated *websites* could be found. The nearest website-specific evidence is a commercial Sortlist survey in which 500 business owners judged five sites (three AI-built, two agency-built) and roughly half failed to separate them — a vendor survey, not a peer-reviewed study (https://www.sortlist.com/datahub/reports/ai-web-design-opinion/?repeat=w3tc). Peer-reviewed work on AI media generally lands near chance: Cooke et al., "As Good as a Coin Toss" (Communications of the ACM), measured 51.2% overall accuracy across 1,276 participants, with images worst at 49.4% (https://cacm.acm.org/research/as-good-as-a-coin-toss-human-detection-of-ai-generated-content/). A preregistered three-country study (n=3,002) found image detection below 50% and no modality above 60% (https://arxiv.org/html/2312.05976v1). The claim's ballpark — humans are barely better than chance, low-to-mid 50s — is consistent with this evidence; the precise "55.5%" and its restriction to websites are not. Do not cite 55.5% as a measured fact.

**Claim 2 — "AI-detector vendor accuracy claims run 15–30 points above independent benchmarks." Verdict: CONFIRMED in substance, with named examples.**
Independent comparisons document exactly this gap for text detectors: Copyleaks advertises 99.12% accuracy while a Scribbr 12-tool benchmark measured 66%; GPTZero claims 99% while the same benchmark measured 52% overall (https://fast.io/resources/ai-detector-accuracy-comparison-2026/). A second comparison puts the claimed-vs-measured gap at 15–23 points and cites the peer-reviewed RAID benchmark (ACL 2024) as the reference standard (https://www.edenai.co/post/are-ai-content-detectors-accurate-2026-benchmarks-false-positives). Peer-reviewed support for vendor overstatement: Liang et al. (Patterns, 2023) found seven GPT detectors falsely flagged an average of 61.3% of non-native English essays as AI-generated, far from vendors' near-zero false-positive claims (https://scriptgrain.com/reference/ai-detector-accuracy). Caveat: these benchmarks measure *text* detectors; the 15–30-point range is confirmed there and plausible, but not independently established, for website/visual detectors.

Calibration consequence for this squad: human gut feeling is a near-chance instrument (Claim 1 evidence), so X-Visual never reports "looks AI" — it reports measured parameter hits. And no detector tool's score is ever quoted without an independent benchmark beside it (Claim 2 evidence).

## Layout and spacing

### DET-VIS-001 — Uniform section padding
- **Signal:** Vertical padding of consecutive page sections, measured in computed styles.
- **AI-typical:** Every section uses the same padding (commonly 80px or 96px top and bottom) regardless of content weight or hierarchy.
- **Professional:** Padding varies deliberately: hero, dense content, and closing sections breathe differently to pace the page.
- **Check:** In devtools, record `padding-top/bottom` for each top-level section. Identical values across 4+ consecutive sections are a candidate only — before flagging, compare those sections' internal composition (layout structure, media treatment, content arrangement). Flag only when the internal structure is also uniform across the sections. A single padding value held as the page's deliberate spacing rhythm over sections whose internal composition varies does not flag — the tell is unvarying default padding over default-structured sections, not a chosen rhythm.
- **False positives:** Strict design systems standardize section spacing, and a canonical system may hold one padding rhythm (e.g. 128px) across hero and dense sections alike, varying only the footer. Distinguish: uniformity of padding alone never flags; flag only padding uniformity plus uniformity of internal section structure.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** layout-responsive, design-tokens

### DET-VIS-002 — Centered-everything composition
- **Signal:** Alignment of headings, body text, and CTAs across all sections.
- **AI-typical:** Every block is center-aligned with a max-width container near 768px; no left-aligned or asymmetric composition anywhere on the page.
- **Professional:** Alignment follows reading patterns and content type; editorial and product sections mix left, split, and offset layouts.
- **Check:** Screenshot review: count sections whose primary text block is center-aligned; flag if all sections on the page are centered.
- **False positives:** Single-column landing pages for one offer are legitimately centered. Distinguish: check other pages of the site; a designed site varies by page type.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** layout-responsive, design-system

### DET-VIS-003 — Perfectly even card grids
- **Signal:** Feature/pricing/testimonial cards: dimensions, internal padding, and text length per card — combined with card copy that is generic enough to swap between cards (or products) unchanged.
- **AI-typical:** 3 or 6 identical cards, same height, same icon size, same two-line description length, no card standing out.
- **Professional:** Content of unequal importance gets unequal weight; one item is featured, spans wider, or carries richer media.
- **Check:** Measure card bounding boxes and character counts; if all cards match within a few pixels and ~10 characters, read the copy before flagging — flag only when the text is also generic/interchangeable (DET-CON-006 territory). Uniform length with specific, non-interchangeable copy is disciplined editing, not a tell.
- **False positives:** Comparison tables, pricing tiers, and professionally edited feature/testimonial grids are intentionally uniform — disciplined copy editing produces near-identical description lengths as a craft outcome. Distinguish: uniformity of form alone never flags; flag only uniformity of form plus generic, interchangeable content.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, design-system

### DET-VIS-004 — No spacing rhythm breaks
- **Signal:** The set of distinct spacing values used across the page.
- **AI-typical:** Spacing snaps to a small set of round values (16/24/32/48) applied mechanically, with no larger dramatic gaps or tight groupings.
- **Professional:** A spacing scale exists, but designers break it intentionally for emphasis — a tight label-to-heading gap, a wide pause before a CTA.
- **Check:** Extract all margin/padding values from computed styles; flag if the distribution shows only scale steps with zero off-scale values in content areas.
- **False positives:** Token-driven design systems enforce scale discipline. Distinguish: professional systems still show intentional one-off values in hero and editorial areas.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-tokens, layout-responsive

### DET-VIS-005 — Container width sameness
- **Signal:** Max-width of content containers across sections and pages.
- **AI-typical:** One container width (often 1200px or 1280px) everywhere, including full-bleed-intended sections that end up boxed.
- **Professional:** Width is a design variable: narrow for reading, wide for galleries, full-bleed for imagery.
- **Check:** Measure container widths per section; flag if a long page uses exactly one width for every section.
- **False positives:** Utility-first frameworks default to one container. Distinguish: designed sites override the default where content demands it.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** layout-responsive, frontend-core

### DET-VIS-006 — Hero formula composition
- **Signal:** Hero structure: eyebrow label, two-line headline, one-line subtext, two buttons, image or gradient below/right.
- **AI-typical:** The exact five-piece formula, in that order, with a primary plus ghost button pair and a badge pill above the headline.
- **Professional:** Hero composition follows the offer: product shot first, editorial statement, video, or search-led — chosen per brand.
- **Check:** Annotate the hero screenshot piece by piece; flag a full formula match including the pill badge and dual-button pair.
- **False positives:** The formula converts well and agencies reuse it. Distinguish: it is a tell only in cluster with other parameters, never alone.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-system, component-library

### DET-VIS-007 — Missing edge cases in layout
- **Signal:** Long words, long names, and dense content inside fixed components (nav, cards, tables).
- **AI-typical:** Layout only works with the short placeholder content it shipped with; a long nav label or title overflows, wraps awkwardly, or clips.
- **Professional:** Components are stress-tested with real, messy content lengths during design and QA.
- **Check:** Inspect components holding the longest real strings on the page; screenshot any overflow, clipping, or broken wrap.
- **False positives:** A single long German compound word can break any design. Distinguish: flag when ordinary-length real content (a normal product name) already breaks the layout.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, layout-responsive

### DET-VIS-008 — Symmetrical feature alternation
- **Signal:** Feature sections alternating image-left/image-right down the page.
- **AI-typical:** A strict zigzag of identical two-column blocks, each with the same image ratio, heading size, and paragraph length.
- **Professional:** Alternation is one device among several; designed pages vary block structure to match each feature's content.
- **Check:** Count consecutive alternating two-column sections; flag 3+ in a row with matching structure and media ratios.
- **False positives:** Product pages for genuinely parallel features. Distinguish: real features differ in media (a chart, a screenshot, a video); AI zigzags reuse one image style throughout.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** layout-responsive, design-system

### DET-VIS-009 — Footer as afterthought grid
- **Signal:** Footer structure versus the rest of the site's design system.
- **AI-typical:** A generic 4-column link grid plus social icons, using spacing, type sizes, and colors that match no other section.
- **Professional:** The footer is designed: brand statement, real contact paths, legal links that resolve, consistent tokens.
- **Check:** Compare footer computed styles to the page's token values; click every footer link and flag dead or `#` targets (also a blocker under UX parameters).
- **False positives:** Large corporate sites have standardized mega-footers. Distinguish: standardized is not inconsistent — tokens still match the site system.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-system, component-library

### DET-VIS-010 — No visual hierarchy inversion
- **Signal:** The single most prominent element per section versus what the section is about.
- **AI-typical:** Every section's loudest element is its heading; supporting evidence (numbers, images, quotes) is uniformly quieter.
- **Professional:** Designers often make the proof the hero: an oversized metric, a product screenshot, a customer quote set larger than the heading.
- **Check:** Per section, identify the largest/highest-contrast element; flag if it is the heading in every section.
- **False positives:** Documentation and text-led pages are heading-dominant by nature. Distinguish: apply to marketing and product pages, not docs.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-system, typography

## Typography

### DET-VIS-011 — Default font pairing
- **Signal:** Computed `font-family` for headings and body.
- **AI-typical:** Inter, Poppins, or Roboto for everything, at default weights, with no brand-specific type choice anywhere on the site.
- **Professional:** Type is selected for the brand (often a distinctive display face) and loaded deliberately with a considered fallback stack.
- **Check:** Read computed font families; flag the Inter/Poppins/Roboto-only pattern when the brand claims a distinct identity.
- **False positives:** Many real design systems (including government ones) standardize on neutral sans faces. Distinguish: those systems pair the neutral face with distinctive scale, weight, and layout choices elsewhere.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** typography, design-tokens

### DET-VIS-012 — Flat type scale
- **Signal:** The set of font sizes used across the page.
- **AI-typical:** Sizes cluster at framework defaults (16/20/24/30/36) with a weak ratio; headings barely separate from body text.
- **Professional:** A deliberate scale with clear steps; display sizes are dramatically larger than body, captions distinctly smaller.
- **Check:** List distinct computed font sizes; flag if the largest heading is under 2.5× body size on a marketing page.
- **False positives:** Dense app UIs use compact scales by design. Distinguish: apply the ratio test to marketing/editorial pages, not dashboards.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** typography, design-tokens

### DET-VIS-013 — Uniform line length and leading
- **Signal:** Line length (characters per line) and line-height across text blocks.
- **AI-typical:** Body text runs to the container edge (100+ characters per line) or is uniformly ~65ch everywhere, with one line-height (1.5 or 1.6) for all sizes.
- **Professional:** Line length is tuned per context; display type gets tight leading, body text gets air, captions get their own treatment.
- **Check:** Measure characters per line in the widest text block and line-height ratios at three sizes; flag edge-to-edge body text on desktop.
- **False positives:** Data tables and code blocks legitimately run wide. Distinguish: test prose blocks only.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** typography, layout-responsive

### DET-VIS-014 — No typographic detail
- **Signal:** Presence of letterspacing on labels, hanging punctuation, real quotation marks, en/em dashes, and numerals style.
- **AI-typical:** All-caps labels without tracking, straight quotes throughout, hyphens used as dashes, no tabular numbers in tables.
- **Professional:** Micro-typography is finished: tracked-out labels, proper quotes and dashes, tabular figures where columns must align.
- **Check:** Inspect label styles for letter-spacing; scan visible copy for straight quotes and hyphen-as-dash in prose; check numeric columns for proportional figures.
- **False positives:** Plain-text CMS fields can strip smart punctuation. Distinguish: flag when the pattern is site-wide, including hand-set headings.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** typography

### DET-VIS-015 — Heading case and weight monotony
- **Signal:** Heading capitalization pattern and weight distribution.
- **AI-typical:** Every heading is Title Case (or every heading sentence case) at one weight, usually 600 or 700, across all levels.
- **Professional:** Case and weight vary by level and purpose; light-weight large headings and bold small labels coexist.
- **Check:** Sample H1–H3 computed weights and transform/casing in source copy. A single weight and single case pattern across all levels is a candidate only — flag only when the presentation is the framework default: a default or generic font at a default weight (600 or 700) with default casing. A single weight that is itself a distinctive choice (e.g. 300 light display, or 800 extra-bold) set in a custom typeface does not flag — it is a type system, not the absence of one.
- **False positives:** A single heading weight can be the brand system itself (light-weight large display type in a custom face, or uniform extra-bold), with variation carried by size, color, and spacing instead of weight. Distinguish: monotony means the default presentation — default font, default weight, default casing; a distinctive single weight in a custom typeface is a system, not an absence of one.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** typography, design-tokens

### DET-VIS-016 — Emoji as iconography in headings
- **Signal:** Emoji characters inside headings, feature titles, and list items.
- **AI-typical:** 🚀 ⚡ 🔒 style emoji prefixed to feature headings in lieu of an icon system.
- **Professional:** A drawn icon set with consistent stroke and metaphor; emoji appear, if at all, in informal copy only.
- **Check:** Scan heading and list text for emoji codepoints; flag any in feature or product headings.
- **False positives:** Playful consumer brands and social copy use emoji deliberately. Distinguish: deliberate brand voice uses them in copy, not as the structural icon for every feature.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, typography

## Color and gradients

### DET-VIS-017 — Purple-blue gradient signature
- **Signal:** Gradient fills on hero backgrounds, headings, buttons, and cards.
- **AI-typical:** A violet-to-blue (or violet-to-pink) linear gradient, often clipped into headline text, as the site's main color event.
- **Professional:** Brand color is usually a chosen solid with a supporting palette; gradients, when used, are brand-specific and sparing.
- **Check:** Inspect computed `background-image` values on hero, H1, and primary buttons; flag the violet-blue gradient in 2+ of those places.
- **False positives:** Fintech and dev-tool brands genuinely brand in purple gradients. Distinguish: branded gradients come with a full custom palette and distinctive type/imagery; the tell is gradient plus defaults everywhere else.
- **Severity:** major
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-tokens, design-system

### DET-VIS-018 — Gradient text on headline
- **Signal:** `background-clip: text` or equivalent on the H1 or key words within it.
- **AI-typical:** One or two headline words rendered in a rainbow or violet gradient while the rest is solid.
- **Professional:** Headline emphasis is achieved with weight, size, italic, or a solid accent color; gradient text is a rare, art-directed choice.
- **Check:** Inspect H1 computed styles for background-clip:text; flag combined with DET-VIS-017.
- **False positives:** Award-style campaign sites use gradient type as a concept. Distinguish: concept sites pair it with custom art direction throughout, not template sections below.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** typography, design-tokens

### DET-VIS-019 — Dark background with neon glow
- **Signal:** Page background luminance plus glow shadows on cards/buttons.
- **AI-typical:** Near-black background, glowing colored box-shadows, glassmorphism cards with translucent white borders — the default "AI product" look.
- **Professional:** Dark themes are built with layered surface colors, restrained elevation, and contrast-checked text, not glow effects.
- **Check:** Read body background and card box-shadow values; flag colored glow shadows on 3+ components.
- **False positives:** Gaming and music brands use neon legitimately. Distinguish: legitimate neon is a brand system with custom assets; the tell is glow plus generic layout and type.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-system, design-tokens

### DET-VIS-020 — Single accent color monoculture
- **Signal:** The full set of distinct hues used across interactive elements.
- **AI-typical:** One accent hue (commonly indigo or teal) does everything: links, buttons, icons, highlights, charts, badges.
- **Professional:** A palette with roles: primary, secondary, semantic (success/warning/error), and neutral ramp, each visibly distinct.
- **Check:** Sample computed colors of buttons, links, badges, and alerts; flag if a single hue covers all roles including semantic states.
- **False positives:** Strong single-color brands exist (e.g., all-red identities). Distinguish: even monochrome brands differentiate semantic colors for errors and success.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-tokens, design-system

### DET-VIS-021 — Default shadow stack
- **Signal:** Box-shadow values across cards, buttons, and modals.
- **AI-typical:** One soft shadow (a large blur, low opacity black) repeated identically on every elevated element, or framework default shadow utilities at one size.
- **Professional:** An elevation scale: subtle for cards, deeper for menus and modals, matched to light direction.
- **Check:** Collect distinct box-shadow values; flag if all elevated components share one identical shadow.
- **False positives:** Flat design systems intentionally use borders instead of shadows. Distinguish: no shadows at all is a system; one shadow everywhere is a default.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-tokens, component-library

### DET-VIS-022 — Unchecked contrast in colored sections
- **Signal:** Text contrast on tinted/gradient section backgrounds.
- **AI-typical:** White or light-gray text on mid-tone gradients and pastel panels falls below WCAG AA (4.5:1 for body text) because colors were picked aesthetically, not checked.
- **Professional:** Palettes are contrast-tested per surface; text on tinted panels uses a darkened foreground token.
- **Check:** Measure contrast of body text on every non-white section with a contrast tool and record every measurement, including sub-threshold ones. Flag as a finding only body text that is persistently under 4.5:1 in its resting state. Where low contrast is one phase of a designed de-emphasis pattern — an emphasis rotation or interactive state in which the highlighted element passes and the site's ordinary body text on tinted sections passes — record the measurement as an observation, not a finding; the measurement is always kept, only the verdict changes.
- **False positives:** Large display text legitimately uses the 3:1 large-text threshold, and designed de-emphasis states (one element highlighted while siblings recede) legitimately sit below threshold in their receded phase. Distinguish: apply 4.5:1 to body-size text in its resting state; a de-emphasis phase is recorded as an observation, while persistently sub-threshold resting text still flags.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-tokens, ui-states

## Imagery and icons

### DET-VIS-023 — Generic stock or AI imagery mismatch
- **Signal:** Hero and section images versus the actual product or business.
- **AI-typical:** Smiling-team stock photos, abstract 3D blobs, or AI-rendered scenes that depict no real product, place, or person connected to the business.
- **Professional:** Imagery shows the actual product UI, premises, team, or commissioned art in a consistent style.
- **Check:** For each image, ask what real thing it depicts; flag sections where the answer is "nothing specific" across the whole page.
- **False positives:** Early-stage startups legitimately use stock before a shoot. Distinguish: legitimate use still matches the business domain; the tell is imagery unrelated to the offer (a bakery with fintech dashboard art).
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-system, frontend-core
- **See also:** DET-CON-019 (stock or generated portraits captioned as the real team are CON-019's fabrication verdict; VIS-023 covers imagery that depicts nothing real about the business)
- **See also:** DET-FAKE-014 (seed people shipped as real users are FAKE-014's scope; VIS-023 covers the imagery mismatch on the page)

### DET-VIS-024 — AI image artifacts
- **Signal:** Hands, text, logos, and reflections inside photographic imagery.
- **AI-typical:** Malformed hands, gibberish text on in-image signage/screens, warped logos, inconsistent reflections or lighting direction.
- **Professional:** Photography is real or professionally retouched; in-image text is legible and correct.
- **Check:** Zoom each photographic image to 100% and inspect hands, text, and logos; flag any gibberish text or anatomical errors.
- **False positives:** Busy real photos contain odd details at pixel level. Distinguish: artifacts are structural (extra fingers, melted lettering), not merely busy.
- **Severity:** blocker
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** frontend-core, design-system

### DET-VIS-025 — Mixed icon styles
- **Signal:** Stroke width, corner style, and fill style across all icons on a page.
- **AI-typical:** Icons drawn from two or more sets (e.g., outline icons beside filled duotone icons) with visibly different stroke weights.
- **Professional:** One icon library or custom set, one stroke weight, one metaphor style, sized on a grid.
- **Check:** Screenshot all icons in one view; measure stroke widths; flag 2+ distinct styles or stroke weights.
- **False positives:** Brand logos in a "featured in" row are foreign by nature. Distinguish: exclude third-party logos; judge the site's own UI icons.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, design-system

### DET-VIS-026 — Icon-in-colored-circle formula
- **Signal:** Feature icon presentation.
- **AI-typical:** Every feature icon sits in an identical soft-tinted circle or rounded square in the accent color, in every grid on the site.
- **Professional:** Icon treatment varies by context or uses a distinctive brand device; the tinted-chip look is one option, not the universal default.
- **Check:** Inspect feature grids across 2+ pages; flag the identical tinted-chip treatment everywhere.
- **False positives:** Icon chips are a genuine pattern in mature systems (e.g., settings UIs). Distinguish: in systems, chips accompany varied layouts; the tell is chips plus identical cards plus identical copy length (see DET-VIS-003).
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** component-library, design-system

### DET-VIS-027 — Identical avatar circles
- **Signal:** Testimonial and team avatars.
- **AI-typical:** Perfectly circular gradient or initial avatars, or AI/stock faces with uniform lighting and no environmental context; names and roles in identical format.
- **Professional:** Real headshots with natural variation, or a deliberate no-photo treatment (name, role, company) when photos are unavailable.
- **Check:** Inspect avatar images for gradient/initial placeholders and AI-face artifacts (see DET-VIS-024); flag placeholders presented as real people.
- **False positives:** Privacy-conscious products hide photos deliberately. Distinguish: deliberate treatments say so or omit the photo slot; placeholders dressed as photography are the tell — and fake people are a blocker under Fake parameters.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, ui-states
- **See also:** DET-CON-010 (fabricated testimonial text is CON-010's blocker verdict; VIS-027 covers the avatar treatment as the visual tell)
- **See also:** DET-CON-013 (fake review patterns are CON-013's verdict; VIS-027 covers the uniform avatar presentation)
- **See also:** DET-CON-019 (stock photos captioned as named team members are CON-019's verdict; VIS-027 covers the placeholder/AI avatar tell)
- **See also:** DET-FAKE-014 (seed accounts shipped as real users are FAKE-014's scope; VIS-027 covers avatars presented as real people)

### DET-VIS-028 — Decorative blob and wave dividers
- **Signal:** Section transitions and background decorations.
- **AI-typical:** SVG wave dividers, blurred color blobs, and dotted grids pasted between sections as generic decoration.
- **Professional:** Transitions are structural (color change, overlap, imagery) or use brand-specific graphic devices.
- **Check:** Screenshot section boundaries; flag wave/blob decorations on 2+ boundaries.
- **False positives:** Playful consumer brands use waves as identity. Distinguish: identity use is consistent, custom-drawn, and paired with matching illustration; generic waves sit atop default layouts.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-system, layout-responsive

### DET-VIS-029 — Image aspect ratio chaos or monotony
- **Signal:** Aspect ratios of content images across a page.
- **AI-typical:** Either every image is the same 16:9/4:3 crop regardless of subject, or ratios vary randomly with awkward object-fit cropping cutting off subjects.
- **Professional:** Ratios follow an art-directed grid; crops are chosen per image so subjects survive.
- **Check:** List natural vs. rendered ratios and inspect crops; flag cut-off heads/products or one ratio forced on unlike subjects.
- **False positives:** User-generated content grids normalize ratios by necessity. Distinguish: UGC normalization still uses focal-point-aware cropping; check whether subjects are decapitated.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** layout-responsive, component-library

### DET-VIS-030 — Screenshot-in-browser-frame mockups
- **Signal:** Product screenshots presented in fake browser chrome or floating device frames.
- **AI-typical:** A generic browser-frame mockup containing a blurred, fake, or unrelated dashboard image that is not the actual product.
- **Professional:** Real product screenshots at readable resolution, updated with the product, framed plainly or not at all.
- **Check:** Zoom the mockup image; flag if the enclosed UI is illegible, generic, or inconsistent with the product's actual UI (compare with DET-VIS-023).
- **False positives:** Pre-launch waitlist pages show concept mockups. Distinguish: concepts are labeled as such; presenting a fake UI as the shipping product is the tell.
- **Severity:** major
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** frontend-core, component-library

## Components and states

### DET-VIS-031 — Identical button treatment everywhere
- **Signal:** Button variants across the page: sizes, radii, and states.
- **AI-typical:** One pill or one rounded-rectangle button style at one size for every action, primary and secondary differing only by fill.
- **Professional:** A button hierarchy with size and emphasis variants matched to context (nav, hero, card, form), all with visible focus states.
- **Check:** Collect button computed styles site-wide; flag a single size/radius pair for all contexts and missing `:focus-visible` styling.
- **False positives:** Minimal brands restrict variants deliberately. Distinguish: deliberate minimalism still differentiates primary from destructive and text actions.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, design-tokens

### DET-VIS-032 — Missing or fake UI states
- **Signal:** Hover, focus, disabled, loading, and empty states of interactive components.
- **AI-typical:** Buttons and links with no hover change, inputs with no focus ring, and lists with no designed empty state (a blank gap instead).
- **Professional:** Every component ships its full state set; empty and loading states are designed, not absent.
- **Check:** Tab through the page (focus visibility), hover primary controls, and view a list with zero items if reachable; flag each missing state.
- **False positives:** Print-style campaign pages have few interactive elements. Distinguish: judge only the interactive elements that exist; one missing focus state on a real control counts.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** ui-states, component-library
- **See also:** DET-UX-008 (loading state: VIS-032 owns whether a designed loading treatment exists; UX-008 owns whether feedback actually appears during real waits)
- **See also:** DET-UX-009 (empty state: VIS-032 owns the designed empty treatment; UX-009 owns the user-facing blank-container behavior)
- **See also:** DET-UX-010 (error state: VIS-032 owns the designed error treatment; UX-010 owns the failed-load behavior and recovery)
- **See also:** DET-CODE-026 (the code-level cause — components with no state handling; CODE-026 covers the absence in code, VIS-032 the rendered result)

### DET-VIS-033 — Badge and pill saturation
- **Signal:** Count of pill-shaped badges ("New", "Popular", category tags) per viewport.
- **AI-typical:** Pills above every heading, on every card, and beside every price — decorative labeling with no informational role.
- **Professional:** Badges are scarce and meaningful: a status, a genuine novelty, a category the user can act on.
- **Check:** Count visible pills in the first three viewports; flag 6+ or a pill above every section heading.
- **False positives:** E-commerce grids legitimately tag many products. Distinguish: product tags filter or inform; decorative heading pills do neither.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** component-library, design-system

### DET-VIS-034 — Logo cloud of invented or mismatched marks
- **Signal:** "Trusted by" logo rows: recognizability and rendering of the logos.
- **AI-typical:** Grayscale logo rows containing distorted, misspelled, or unrecognizable brand marks, or generic wordmarks in default fonts.
- **Professional:** Real customer logos, correctly drawn, with permission, in consistent optical sizing.
- **Check:** Read every logo aloud; flag any misspelled, warped, or unidentifiable mark (fabricated social proof is also a blocker under Fake parameters).
- **False positives:** Obscure but real startups look unfamiliar. Distinguish: unfamiliar is fine; misspelled or malformed renderings of known brands are not.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, frontend-core
- **See also:** DET-CON-012 (invented marks are fabrication — a blocker under CON-012; VIS-034's major rating covers mismatched or poorly rendered real marks only)

### DET-VIS-035 — Stat band with round numbers
- **Signal:** Metric bands ("10,000+ customers", "99.9% uptime", "4.9/5 rating") and their visual treatment.
- **AI-typical:** Three or four oversized round numbers in a row, identically styled, with no source, date, or methodology.
- **Professional:** Metrics are specific, dated, and sourced, or omitted; visual treatment varies with the story.
- **Check:** Record the stats shown and record the band as a candidate only — the visual pass does not flag it. The flag is raised only after the source check runs: a uniform band of round numbers with no source for its figures anywhere on the page escalates to Content/Fake (DET-CON-011). A linked source for the band's figures anywhere on the page (annual letter, status page, methodology note) clears the candidate before it is raised.
- **False positives:** Mature companies publish real headline metrics in standard stat bands. Distinguish: the visual tell alone never flags — the visual pass records, the source check decides; real metrics survive a source check, unsourced-plus-round is the cluster signal.
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** component-library, design-system
- **See also:** DET-CON-011 (VIS-035 is the visual tell only — a hit here must escalate to a CON-011 check; fabricated or unsourced statistics are a blocker under CON-011)

### DET-VIS-036 — Pricing table template fingerprint
- **Signal:** Pricing section structure: three tiers, middle highlighted, identical feature lists with check icons.
- **AI-typical:** The default SaaS pricing table, middle tier scaled up with a "Most Popular" pill, feature rows differing by one or two lines.
- **Professional:** Pricing presentation follows the actual model (usage, seats, one-time) and differentiates tiers by real packaging decisions.
- **Check:** Compare tier structures; flag the three-tier/middle-highlight/checklist pattern when the product's model is not seat-based SaaS.
- **False positives:** Actual SaaS products converge on this pattern because buyers expect it. Distinguish: never flag alone; count only inside a cluster.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** component-library, design-system

## Responsive behavior and motion

### DET-VIS-037 — Breakpoint collapse, not adaptation
- **Signal:** Layout at 390px versus 1440px.
- **AI-typical:** Multi-column sections simply stack in DOM order with identical spacing; type sizes barely shrink; tap targets stay desktop-sized or shrink below 24px.
- **Professional:** Mobile layouts are recomposed: order changes for priority, type scale adjusts, targets stay comfortably tappable.
- **Check:** Compare desktop and mobile screenshots section by section; flag pure stacking with unchanged spacing/type across 3+ sections.
- **False positives:** Simple brochure sites legitimately stack. Distinguish: designed stacking still adjusts type scale and spacing rhythm for the narrow viewport.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** layout-responsive, frontend-core
- **See also:** DET-VIS-038 (VIS-038 is outright page-level overflow; VIS-037 is stacking without recomposition — no overflow required)
- **See also:** DET-UX-023 (UX-023 owns the primary-task verdict at mobile widths; VIS-037 covers the un-adapted layout pattern behind it)

### DET-VIS-038 — Horizontal overflow on mobile
- **Signal:** Horizontal scrollbar or clipped content at small widths.
- **AI-typical:** A wide table, oversized heading word, or fixed-width element forces sideways scrolling at 360–390px.
- **Professional:** Every component is tested at small widths; wide content gets a deliberate treatment (scroll region, reformat, wrap).
- **Check:** At 360px, scroll horizontally; flag any page-level overflow and identify the offending element in devtools.
- **False positives:** Intentional in-component scroll regions (code blocks, data tables) are legitimate. Distinguish: page-level overflow is the defect; contained scroll regions are design.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** layout-responsive, frontend-core
- **See also:** DET-UX-023 (UX-023 owns the verdict on whether the primary task survives at mobile widths; VIS-038 covers page-level horizontal overflow as the visual defect)
- **See also:** DET-VIS-037 (adjacent: VIS-037 covers breakpoint collapse — stacking without recomposition — where VIS-038 is raw overflow)

### DET-VIS-039 — Fixed hero height clipping
- **Signal:** Hero content fit across viewport heights and widths.
- **AI-typical:** A `100vh` or fixed-pixel hero clips its own content on short or narrow screens; text overlaps the image or the CTA falls below an unreachable fold.
- **Professional:** Heroes size to content with min-height, and remain intact from small phones to short laptop windows.
- **Check:** Resize to 360×640 and 1280×600; screenshot the hero at both; flag any clipped or overlapping hero content.
- **False positives:** Full-screen media heroes intentionally crop background imagery. Distinguish: cropping a background is fine; clipping foreground text or CTAs is not.
- **Severity:** major
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** layout-responsive, component-library

### DET-VIS-040 — Uniform fade-up scroll animation
- **Signal:** Scroll-triggered animation pattern across sections.
- **AI-typical:** Every section fades in and translates up by the same distance over the same duration as it enters the viewport — one library default applied globally.
- **Professional:** Motion is selective and meaningful: most content is simply present; animation explains a change or draws the eye once.
- **Check:** Scroll the page slowly and record which elements animate; flag if 80%+ of sections share the identical fade-up.
- **False positives:** Some brands adopt a single house motion style. Distinguish: house styles vary easing/duration by element type and respect reduced-motion (see DET-VIS-041).
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** motion, scroll-experiences

### DET-VIS-041 — Reduced motion ignored
- **Signal:** Animation behavior with `prefers-reduced-motion: reduce` emulated.
- **AI-typical:** Parallax, auto-playing motion, and scroll animations continue unchanged; the media query is absent from the CSS.
- **Professional:** Reduced-motion users get a calm page: parallax and non-essential animation disabled or replaced with fades.
- **Check:** Emulate reduced motion in devtools and reload; census what still animates and grep CSS for the media query. Flag continuing animation of content-bearing or layout elements — parallax, auto-playing media, scroll-jacking, moving text or panels. Continuing ambient background motion that carries no information and does not move content (a decorative dot grid, texture drift, or similar backdrop animation behind static content) is recorded as an observation, not a flag.
- **False positives:** A site with no animation at all trivially passes, and a site may honor the preference for all content motion while an ambient background texture keeps animating. Distinguish: only flag sites whose content-bearing or layout animation continues under reduced motion; ambient background decoration is an observation, not a hit.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** motion, scroll-experiences

### DET-VIS-042 — Hover-dependent mobile dead ends
- **Signal:** Content or actions revealed only on hover (cards, menus, image overlays).
- **AI-typical:** Key links and details appear only in hover states, so touch users never see them; menus require hover to open.
- **Professional:** Hover enhances; it never gates. Every hover reveal has a tap/click and focus equivalent.
- **Check:** On the mobile screenshot pass, tap each hover-reveal component; flag any content unreachable by touch or keyboard.
- **False positives:** Tooltips on desktop data tools are hover-first by convention. Distinguish: tooltips supplement visible data; gated navigation or CTAs are dead ends.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** ui-states, layout-responsive

### DET-VIS-043 — Inconsistent radius language
- **Signal:** Border-radius values across buttons, cards, inputs, images, and modals.
- **AI-typical:** A scatter of radii (8px cards, 12px buttons, 24px images, full-pill inputs) with no system — pieces pasted from different templates.
- **Professional:** A radius scale with roles (small for inputs, medium for cards, pill only for chips/tags) applied consistently.
- **Check:** Collect computed border-radius values per component type; flag 4+ unrelated values with no role pattern.
- **False positives:** Expressive brands mix sharp and round deliberately by component family. Distinguish: deliberate mixes are consistent within each family; the tell is variance within the same component type.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** design-tokens, component-library

### DET-VIS-044 — Above-the-fold density mismatch
- **Signal:** Information density of the first viewport versus the rest of the page.
- **AI-typical:** A polished, dense hero followed by visibly emptier, thinner sections — effort concentrated where a demo screenshot would look.
- **Professional:** Quality is even down the page; later sections carry the same craft as the hero.
- **Check:** Compare full-page screenshot regions; flag a marked density/craft drop after the second section.
- **False positives:** Long-form sales pages intentionally front-load. Distinguish: front-loading varies emphasis, not basic finish (spacing, states, image quality stay consistent).
- **Severity:** minor
- **Source:** Derived: WCPM inheritance (Phase 2 verification pending)
- **Fix:** design-system, frontend-core
