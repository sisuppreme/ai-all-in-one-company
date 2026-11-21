# design-system

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, button component (usage guidance incl. when not to use) — https://design-system.service.gov.uk/components/button/ ; Design Tokens Specification 2025.10, first stable version announcement — https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- **Depends on:** design-tokens
- **Feeds into:** frontend-core, component-library, typography, layout-responsive

## When to use / Do NOT use

- **Use when:** establishing or governing the system itself — its tokens, component inventory, usage rules, and changelog — and when reviewing a page for system-level failures: monotony, drift, invented proof. This skill is the primary home for WCPM's visual-language material: §2 catalog (as reference), §3 diagnosis and CV cures, §4 design brief and distinctiveness, and §6 visual craft.
- **Do NOT use when:** the question is a single token value (design-tokens), a single component's internals (component-library), or a single page's layout (layout-responsive). The system governs; those skills execute.

## Rules

1. **FE-021 — The system is four artifacts.** The token set, the component library, written usage rules, and a changelog. A visual decision that exists only inside one page's code is not part of the system and does not ship as one.
2. **FE-022 — Every decision traces.** Each visual choice on a shipped page traces to a token, a library component, or a documented one-off exception with a written reason. Untraceable styling is drift and is removed or absorbed into the system.
3. **FE-023 — Guidance includes refusal.** Every component's documentation states its purpose, its variants, and at least one "do not use when" case, on the GOV.UK pattern. A component documented only with happy paths will be misused.
4. **FE-024 — Changes are versioned.** A token or component change ships with a changelog entry and a visual-regression pass, never as a silent edit. Consumers of the system learn about change from the changelog, not from a screenshot diff.
5. **FE-025 — Composition varies by role.** Section composition follows content role (hero, proof, dense content, closing): a page where every section shares the same padding, alignment, and loudest element fails system review (DET-VIS-001, DET-VIS-002, DET-VIS-010).
6. **FE-026 — Proof may outrank headings.** Hierarchy serves the message: a metric, a product shot, or a customer quote may be the most prominent element in its section. The heading is not entitled to be loudest by default.
7. **FE-027 — Diagnose before redesigning.** Visual failures are diagnosed against the parameter catalog (WCPM §2, served in this repo by DET-VIS-001…044) and cured with the matching cure rules (CV family) — not by restyling on taste. Clusters are scored as clusters: 3 or more minor tells in one component or section count as one major (WCPM CLU-01…06; enforced by G-DES-02).
8. **FE-028 — The acceptance bar is scored, not felt.** A page passes visual acceptance on the rubric: zero P0 parameters, rubric score ≥ 90, every category ≥ 7, zero F1–F8 auto-fails (WCPM G-DES-01). "Looks fine to me" is not a verdict — human detection of generated design is a near-chance instrument, so the score carries the decision.
9. **FE-029 — Distinctiveness is briefed before building.** Each project opens with a design brief that names its divergence: the visual choices that make this product unlike the template default (WCPM §4, BR- divergence rules and D-MIN minimum thresholds). A brief that could describe any SaaS site is rejected and rewritten.
10. **FE-030 — Imagery belongs to the system.** Photography and illustration follow one documented style and depict the business's real product, place, or people (DET-VIS-023); aspect ratios follow an art-directed grid so subjects survive their crops (DET-VIS-029). Stock or generated imagery depicting nothing real is not a system asset.
11. **FE-031 — The footer is designed.** The footer uses the system's tokens and carries a brand statement, real contact paths, and legal links that resolve — not a generic link grid pasted under the page (DET-VIS-009).

## BAN list

- **BAN-FE-011 — The one-gradient, one-font "system".** Banned: calling a violet-blue gradient, one default font, and copy-pasted cards a design system. Defeats: DET-VIS-017. Bad: every hero, button, and headline on the site carries the same purple-to-blue gradient; the "system" page lists a logo, a gradient, and Inter. Instead: a chosen brand palette with roles, a deliberate type choice, and tokenized scales (design-tokens). Severity: BLOCK.
- **BAN-FE-012 — Invented social proof in the system.** Banned: logo clouds, testimonials, or metrics built from invented marks, people, or numbers as reusable system components. Defeats: DET-VIS-034. Bad: a "trusted-by" component shipping with six plausible-looking wordmarks of companies that are not customers. Instead: the component renders only real, permitted logos — and renders nothing when none exist. Severity: BLOCK.
- **BAN-FE-013 — Imagery that depicts nothing.** Banned: stock or AI imagery with no connection to the business as the system's default visual language. Defeats: DET-VIS-023. Bad: a bakery's site illustrated throughout with fintech dashboard renders and abstract 3D blobs. Instead: photographs of the actual bakery, its products, and its people, in one documented style. Severity: BLOCK.
- **BAN-FE-014 — The uniform section template.** Banned: one section layout — same padding, centered heading, three cards — repeated for every content role on a page. Defeats: DET-VIS-001. Bad: hero, features, story, pricing, and FAQ all rendered as 96px-padded centered blocks differing only in copy. Instead: composition assigned per role (FE-025), with padding and alignment varying deliberately. Severity: WARN.
- **BAN-FE-015 — Generic wave and blob decoration.** Banned: SVG wave dividers, blurred color blobs, and dotted grids pasted between sections as decoration. Defeats: DET-VIS-028. Bad: a purple blob behind the hero, a wave divider before pricing, a dotted grid behind testimonials — none of them brand assets, all of them defaults. Instead: transitions that are structural (color change, overlap, imagery) or a custom brand device used consistently. Severity: WARN.

## Gates

- **G-FE-011 — DET-VIS cluster review.** Verifies: FE-025, FE-026, FE-027, FE-030, FE-031. Check: manual — per milestone, walk DET-VIS-001…044 in ID order against full-page screenshots at 1440px and 390px; mark each hit with a screenshot or measured value; apply the cluster rule (3+ minors in one section = 1 major). Pass: zero blockers, zero majors, clusters resolved. Fail: block the milestone. Recorded in: progress.md.
- **G-FE-012 — Rubric acceptance score.** Verifies: FE-028. Check: manual scoring against the WCPM G-DES-01 bar — count P0 parameter hits, score the rubric, check every category ≥ 7 and zero F1–F8 auto-fails. Pass: 0 P0, score ≥ 90, all categories ≥ 7, zero auto-fails. Fail: block shipment. Recorded in: progress.md.
- **G-FE-013 — System trace audit.** Verifies: FE-021, FE-022, FE-024. Check: automated + manual — sample 10 styled elements per page and resolve each to a token, a library component, or a logged exception; confirm the system changelog has an entry for every token/component change in the release. Pass: 10 of 10 trace, changelog complete. Fail: block until drift is absorbed or removed. Recorded in: progress.md.
- **G-FE-014 — Token and contrast enforcement.** Verifies: FE-022 (via design-tokens). Check: automated — the design-tokens gates run as this skill's enforcement arm: token-literal lint and the semantic-pair contrast script (G-FE-022, G-FE-023). Pass: both green. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The system that is a screenshot.** A Figma frame or a "brand" page exists, but pages are styled ad hoc and nothing traces back to it. Catch it: run the trace audit (G-FE-013); untraceable elements are the system failing, not the page.
- **Drift by a thousand cuts.** Each page is almost consistent — slightly different padding, an off-scale size, a near-miss color. Catch it: drift is a cluster phenomenon; the per-milestone DET-VIS review exists because no single diff looks wrong.
- **Restyle instead of diagnose.** A flagged page gets a new coat of paint with the same structure underneath, and the same parameters hit again next milestone. Catch it: every rework names the parameter and the cure applied (FE-027).
- **Exception inflation.** "Documented one-offs" multiply until the exception is the real system. Catch it: count exceptions per page at review; a third exception of the same kind becomes a token or component, or is removed.

## Examples

- [Example 1 — Uniform sections recomposed by role](examples/example-1.md) — corrects FE-025.
- [Example 2 — A gradient signature replaced by a brand system](examples/example-2.md) — corrects FE-029.
- [Example 3 — An invented logo cloud removed and replaced with real proof](examples/example-3.md) — corrects FE-022 (via BAN-FE-012).

## Recall anchors

- Four artifacts: tokens, components, guidance, changelog.
- If it doesn't trace to the system, it's drift.
- Diagnose against parameters; never restyle on taste.
- The rubric decides — 0 P0, ≥ 90, no category under 7.
- Proof is allowed to be louder than the heading.

## Checklist

- [ ] The system has all four artifacts, current (FE-021).
- [ ] Sampled elements trace to token, component, or logged exception (G-FE-013).
- [ ] Every component documents a "do not use when" case (FE-023).
- [ ] Token/component changes carry changelog entries (FE-024).
- [ ] DET-VIS cluster review walked at 1440px and 390px (G-FE-011).
- [ ] Rubric acceptance bar met: 0 P0, ≥ 90, categories ≥ 7, zero F1–F8 (G-FE-012).
- [ ] Composition varies by section role; proof may outrank headings (FE-025, FE-026).
- [ ] Imagery depicts the real business in one documented style (FE-030).
