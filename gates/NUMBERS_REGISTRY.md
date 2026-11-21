# NUMBERS_REGISTRY.md — Numbers registry (single source of truth)

Extracted faithfully from Web Craft Pro Max Appendix F.2. Every duration, threshold, budget, size, and ratio in the inherited system is stated in exactly one place: this registry. Skills and gates cite entries by N-ID; they do not copy the values into their own tables (see `docs/WCPM_MAPPING.md` Drop 2 — duplicated threshold tables are how the source's own 68-vs-69 gate-count slip happened).

Every other section references the registry entry by ID; where a section shows the number inline, it shows the number AND the registry ID. Never round a registry value when restating it. A number that differs by context is TWO entries with different IDs.

## Performance & motion (N01–N19)

| ID | Quantity | Canonical value | Context / measurement method | Used in |
|---|---|---|---|---|
| N01 | LCP (field) | ≤2.5 s | p75, mobile and desktop separately, rolling 28 days | §9.2 |
| N02 | LCP (lab) | ≤2.0 s | Lighthouse, median of 3 runs, throttled slow 4G, 4× CPU | §9.2, §12.3 |
| N03 | CLS (field) | ≤0.1 | p75, mobile and desktop separately, rolling 28 days | §9.2 |
| N04 | CLS (lab) | ≤0.05 | Lighthouse, median of 3 runs, throttled slow 4G, 4× CPU | §9.2, §12.3 |
| N05 | Lighthouse Performance score | ≥90 | Mobile, median of 3 runs, throttled slow 4G, 4× CPU | §12.3 |
| N06 | Lighthouse Accessibility score | 100 | Mobile and desktop | §12.3 |
| N07 | INP | ≤200 ms (Google good); ≤150 ms (house target) | p75, field only. Lab cannot measure INP — use TBT (N08) as proxy | §9.2, §7.8 |
| N08 | TBT (lab) | ≤200 ms | Lighthouse, median of 3 runs | §9.2, §12.3 |
| N09 | Frame rate (motion) | ≥55 fps sustained, zero frames >33 ms | Under 4× CPU (every page) and 6× CPU (heaviest page) | §7.8 |
| N10 | Hover-in duration | 200 ms | `--dur-base` | §7.2 |
| N11 | Hover-out duration (button) | 150 ms | `--dur-fast` | §7.2 |
| N12 | Entrance/transition/cascade ceiling | 600 ms | Absolute ceiling; named exemptions only (mask-wipe 800 ms, 3D intro ≤1.5 s, count-up magnitude-scaled) | §7.3 |
| N13 | Hover-out duration (card/reveal) | 250 ms | `--dur-medium` | §7.2 |
| N14 | Single UI animation ceiling | 800 ms | UI animations only; no 400 ms ceiling exists | §7.3 |
| N15 | Micro-interaction ceiling | 200 ms | Complete interaction | §7.4 |
| N16 | Feedback latency | ≤100 ms | Visible state change after pointer/key event | §7.1 |
| N17 | Scroll-triggered movement | ≤100 px, no rotation | Triggered only; driven motion excluded | §7.5 |
| N18 | Parallax travel | ≤ min(±40 px, ±6% element height, 8% vh) | Per section; max 2 sections per page | §7.5 |
| N19 | Pin cap | 250 vh | Pinned sections | §7.3 |

LCP sub-budget (lab, sums to N02's ≤2.0 s): TTFB ≤800 ms (stretch target ≤600 ms) / server delay ≤200 ms / resource load ≤800 ms / render ≤200 ms.

## Assets, sizes & text (N20–N40)

| ID | Quantity | Canonical value | Context / measurement method | Used in |
|---|---|---|---|---|
| N20 | Hero/LCP image weight | ≤150 KB | Compressed, modern format; target 80–120 KB | §9.3 |
| N21 | Single image weight | ≤200 KB | Compressed, modern format | §9.3 |
| N22 | Above-the-fold images, combined | ≤300 KB | All images in the initial viewport | §9.3 |
| N23 | Absolute image ceiling | 500 KB | No image on a public page exceeds this | §9.3 |
| N24 | Autoplay loop video | ≤1 MB (≤10 s) | Hard cap | §9.3 |
| N25 | JavaScript per route (landing) | ≤170 KB | Compressed transfer size | §9.2 |
| N26 | JavaScript per route (app) | ≤350 KB | Compressed transfer size | §9.2 |
| N27 | Font first load | ≤100 KB target / 150 KB ceiling | Per page load in its locale | §9.3 |
| N28 | Font deferred total | ≤250 KB | Strictly post-interaction subsets only (R-9.3-11) | §9.3 |
| N29 | 3D weight before first interaction | ≤500 KB | Total session-streaming ceiling 5 MB / 2 MB, post-interaction only | §9.2 |
| N30 | Touch target size | ≥44 × 44 px (minimum); 48 × 48 px (preferred) | CSS px, every interactive control; capability-keyed (§11.2) | §11.2 |
| N31 | Touch target separation | ≥8 px | Between adjacent targets; 12–16 px near destructive actions | §11.2 |
| N32 | Body text minimum | ≥16 px | Never below 16 px for body text | §11.1 |
| N33 | Text contrast (body) | ≥4.5:1 | WCAG AA, normal text | §11.3 |
| N34 | Text contrast (large / UI) | ≥3:1 | Large text (≥24 px, or ≥18.66 px bold) and UI components | §11.3 |
| N35 | Absolute text minimum | ≥12 px | Never below 12 px for any text | §11.1 |
| N36 | Measure (line length) | 66 ch target; 45–75 ch range; 75 ch hard max | House ceiling; WCAG 1.4.8 allows 80 | §11.1 |
| N37 | Title length | 50–60 chars, never over 70 | Per page | §10.2 |
| N38 | Meta description length | 120–155 chars, ceiling 160 | Per page; core answer in first 120 chars | §10.2 |
| N39 | Word count (this file) | ≤40,000 words | Hard cap; measured at assembly | Header |
| N40 | Token estimate | 1 word ≈ 1.33 tokens | Authoring conversion; both units recorded | Header |

## Registry maintenance

The glossary/registry dispute rule — glossary wins for terms, registry wins for numbers, newest dated decision wins for conflicts. The consistency pass runs before every release and on any edit touching 2+ sections.

*Extraction note: the source's F.2 also carries one stray non-registry line (catalog tell counts) that is not a numbers entry; it is not reproduced here — the count reconciliation lives in `docs/WCPM_MAPPING.md` and `docs/WEB_CRAFT_PAPER.md`.*
