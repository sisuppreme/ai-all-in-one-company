# QA_PROTOCOL_GATES.md — The skill-release QA protocol (G-QA-01…G-QA-10)

These ten gates come from Web Craft Pro Max §12.5. They gate the release of a **skill itself** (in this repo: a skill or repo release, run by D8), not the acceptance of a project build. They are counted separately from the 69-gate acceptance register in `gates/ACCEPTANCE_GATES.md` and are never merged into it (ruling: `docs/WCPM_MAPPING.md` §1).

Several QA gates deliberately mirror register gates — G-QA-06 mirrors G-EXP-05, G-QA-08 mirrors G-ENG-01. Per the mapping's Drop 5 ruling, G-QA-03 does not restate the uniqueness bar: it **cites G-DES-01**, so the bar exists in exactly one place.

**Protocol rules** (from the source, §12.5): Test the skill, not the tester. Never hand-fix a test site. Never weaken a threshold to pass. Fresh session per scenario. The QA operator verifies; the builder never scores their own work. One failing hard gate fails the scenario.

**Scenarios.** The source ships three content packs: S1 marketing site "Northwind Heat Pumps" (6 pages); S2 dashboard "Installer Hub" (5 screens); S3 portfolio "Mara Ellison" (4 pages). Invented content = hard-gate failure. Missing content ships without or is visibly marked — never invented. Per `docs/WCPM_MAPPING.md` Drop 6, those fixtures belong to the source project's own release QA; in this repo the protocol below is what is inherited, and this repo's proof projects (P1–P4) take the fixtures' place.

**Scoring (100 points):** Uniqueness 30, Functional 20, SEO/AEO/GEO 15, Performance 15, Accessibility + Responsive 10, Code 10. Pass: per-scenario ≥85 + every dimension floor + all hard gates. Bands: 95–100 exceptional, 85–94 pass, 70–84 marginal, <70 fail. (The §3 rubric counts P0+P1 visible tells only for its 3+ auto-fail.)

## The ten hard gates

| Gate | Criterion |
|---|---|
| G-QA-01 | Zero invented content: no testimonial, logo, statistic, award, quote, date, or price that is not in the content pack |
| G-QA-02 | Zero builder fingerprints: no generator meta naming an AI builder, no builder badge, no builder CDN domain or class prefix |
| G-QA-03 | Uniqueness bar — see **G-DES-01** in `gates/ACCEPTANCE_GATES.md` (cited, not restated, per the Drop 5 ruling) |
| G-QA-04 | No dead primary control: every button, link, and form on a primary flow does what it promises |
| G-QA-05 | Zero console errors, zero failed requests on the happy path of every required flow |
| G-QA-06 | axe-core 0 violations at WCAG 2.2 AA on every required page (mirrors G-EXP-05) |
| G-QA-07 | No horizontal overflow: scrollWidth ≤ innerWidth at every ladder width, on every page |
| G-QA-08 | Build, lint, type checks pass: build exit 0, type check 0 errors, lint 0 errors (mirrors G-ENG-01) |
| G-QA-09 | Automated slop-detector score ≤19 on the primary detector ("hand-made" band) |
| G-QA-10 | Human review: at least 2 of 3 reviewers answer "yes" to "Would you believe a human agency built this?" |

## Detector checks

Rendered-page detector ≤19 (AI Slop Meter or Jev); CSS scan ≤20 (`--fail-over 20`); manual 21-sign audit <16 (use the source's published bands, do not recompute); human review: 3 blinded reviewers (≥1 designer/dev), 5 minutes each, 2/3 must answer "human-made". A detector/human disagreement over 1 band blocks the release.

## Multi-model rule

Major releases run on ≥2 models from different providers; both must pass (a split result is a BLOCKER). Minor releases: 1 model, rotated each release. Cross-model score delta >5 points triggers investigation.

## Regression

Re-run on the same frozen briefs; the baseline is versioned, never overwritten. Failure classes: BLOCKER/MAJOR/MINOR; max 3 open MINOR. Never fix by weakening a threshold.

## Install-path test

≥1 install per route (§12.4 probes) on every release.
