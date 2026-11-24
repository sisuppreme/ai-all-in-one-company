# design-tokens

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Design Tokens Format Module 2025.10 (DTCG) — https://www.designtokens.org/tr/2025.10/ ; Style Dictionary, DTCG support — https://styledictionary.com/info/dtcg/
- **Depends on:** none — standalone: tokens are defined from the project's own visual decisions (user-supplied palette and type choices) in the token source files; this is the source layer, so nothing upstream feeds it. Its tokens feed design-system, component-library, typography, frontend-core, and motion.
- **Feeds into:** design-system, component-library, typography, frontend-core, motion

## When to use / Do NOT use

- **Use when:** defining, changing, or auditing the token source files — the single place a visual value may be defined — and when a page shows value-level tells: gradient signatures, shadow monoculture, radius scatter, unchecked contrast. WCPM's colour/gradient bans (C- working IDs), the COL family, and the SPC family are prevented here, at the token layer.
- **Do NOT use when:** the question is how a value is used (component-library, layout-responsive) or whether a composition works (design-system). Tokens define values; they do not design pages.

## Rules

1. **FE-041 — One format, one source.** Tokens are authored once in DTCG-format JSON — every token an object with `$value`, `$type`, and aliases by dot-path — and transformed by Style Dictionary (or Terrazzo) into CSS custom properties and other platform outputs. Hand-edited output files are defects.
2. **FE-042 — Three tiers.** Primitive (raw values) → semantic (roles: `color-action-primary`, `surface-raised`) → component. Theming happens at the semantic tier by overriding the same names; a theme never duplicates the primitive file.
3. **FE-043 — Semantic only in components.** Components reference semantic tokens exclusively. A primitive value, hex code, pixel, or millisecond literal in component styles is a defect found by lint, not by opinion.
4. **FE-044 — Every token is documented.** Each token carries a `$description` naming its role. Retired tokens are marked `$deprecated` with a pointer to their replacement — never silently deleted, so existing code fails loudly instead of drifting.
5. **FE-045 — Scales with named roles.** Elevation, radius, spacing, and duration are scales whose steps have roles (radius: input / card / pill; elevation: flat / card / menu / modal). Values are applied by role — the direct counter to the single-shadow default (DET-VIS-021) and radius scatter (DET-VIS-043).
6. **FE-046 — Pairs pass contrast before they are named.** A semantic foreground/background pair is only admitted to the token set after its WCAG ratio is computed: ≥ 4.5:1 for body text, ≥ 3:1 for large text and non-text indicators — including pairs that sit on tinted or gradient surfaces (DET-VIS-022).
7. **FE-047 — The palette has roles, not a hue.** The color system defines primary, secondary, semantic (success / warning / error), and a neutral ramp as distinct tokens. One accent hue covering every role, semantic states included, fails review (DET-VIS-020).
8. **FE-048 — Gradients are tokens with a reason, or absent.** A gradient exists only as a named token whose description states its brand basis and where it may be used. The violet-blue linear gradient is never a default primary, background, or text treatment (DET-VIS-017, DET-VIS-018).
9. **FE-049 — Dark surfaces are layered, not glowing.** Dark themes are built from layered surface tokens with restrained elevation; colored glow shadows are not an elevation device (DET-VIS-019).
10. **FE-050 — Token changes are reviewed as diffs.** Any change to the token source ships with a diff review and the design-system changelog entry (FE-024); a changed value with no diff review is treated as an accidental edit.

**Architecture must never leak into the UI.** Tokens are build-time values, never content. Token names, token values, and the token hierarchy must never be rendered as labels, shown in interface text, or exposed through UI copy, tooltips, or error messages. A colour, a spacing value, or a duration is a decision the user feels; it is never a word the user reads.

## BAN list

- **BAN-FE-021 — Raw values in component styles.** Banned: hex codes, pixel values, or millisecond literals written directly in component or page styles. Defeats: DET-VIS-020. Bad: `.btn-primary { background: #6d5df6; padding: 13px 22px; }` — a one-off violet and an off-scale padding that exist nowhere in the token set and will never theme, never be audited, and never match the next page. Instead: `background: var(--color-action-primary); padding: var(--space-control-y) var(--space-control-x)`. Severity: BLOCK.
- **BAN-FE-022 — The violet-blue gradient as default.** Banned: a purple-to-blue (or purple-to-pink) linear gradient as the site's primary color event — hero background, buttons, or clipped into headline text. Defeats: DET-VIS-017. Bad: hero background, primary button, and H1 all carrying `linear-gradient(90deg,#8b5cf6,#3b82f6)`. Instead: a chosen solid brand color with a supporting palette; a gradient only as a named token with a stated brand basis (FE-048). Severity: BLOCK.
- **BAN-FE-023 — Text on an unchecked surface.** Banned: naming a text/surface token pair that has never had its contrast ratio computed. Defeats: DET-VIS-022. Bad: white button text on a mid-tone amber panel chosen by eye, measuring 2.9:1 — unreadable for body-size text and never checked. Instead: darken the foreground token or deepen the surface until the pair computes ≥ 4.5:1, then admit the pair (FE-046). Severity: BLOCK.
- **BAN-FE-024 — One shadow for everything.** Banned: a single box-shadow value applied to cards, menus, modals, and buttons alike. Defeats: DET-VIS-021. Bad: `box-shadow: 0 8px 30px rgba(0,0,0,.12)` on every elevated element regardless of height or light direction. Instead: the elevation scale — subtle for cards, deeper for menus and modals, matched to one light direction (FE-045). Severity: WARN.
- **BAN-FE-025 — Radius scatter.** Banned: unrelated border-radius values assigned per component with no role pattern. Defeats: DET-VIS-043. Bad: 8px cards, 12px buttons, 24px images, full-pill inputs on one page — pieces pasted from different templates. Instead: the radius scale applied by role (input / card / pill) everywhere (FE-045). Severity: WARN.

## Gates

- **G-FE-021 — Token build in CI.** Verifies: FE-041, FE-042, FE-044. Check: automated — Style Dictionary build runs in CI; a broken alias, a missing `$type`, or a hand-edited output file fails the build. Pass: build green and outputs regenerate byte-identical from source. Fail: block shipment. Recorded in: progress.md.
- **G-FE-022 — Literal lint.** Verifies: FE-043. Check: automated — a stylelint custom rule (or grep script) fails on hex, px, or ms literals in component and page style files, excluding the token source and generated outputs. Pass: zero hits. Fail: block until values move into tokens. Recorded in: progress.md.
- **G-FE-023 — Contrast script.** Verifies: FE-046, FE-047. Check: automated — a script computes the WCAG ratio for every semantic text-on-surface token pair, including tinted and gradient surfaces. Pass: every pair ≥ 4.5:1 (≥ 3:1 for pairs designated large-text or non-text). Fail: block; the pair is not admitted or is fixed. Recorded in: progress.md.
- **G-FE-024 — Token diff review.** Verifies: FE-044, FE-050. Check: manual — review the token diff for the release: new tokens have descriptions, retired tokens are `$deprecated` with replacements, no scale gained a step without a role. Pass: diff approved and changelog entry present. Fail: warn and hold the token change. Recorded in: progress.md.

## Anti-patterns

- **Token sprawl.** Forty near-identical grays and six "primary" blues accumulate because adding a token is easier than choosing one. Catch it: count tokens per role at review; duplicates collapse into one semantic name.
- **The bypass variable.** A component defines a local CSS variable with a raw value to "just fix this one screen" — a primitive smuggled past the lint. Catch it: the literal lint covers local variable definitions too (G-FE-022).
- **Theme by duplication.** Dark mode ships as a second, diverging token file instead of semantic-tier overrides. Catch it: both themes must resolve the same semantic names (FE-042); a name existing in only one theme fails the build review.
- **Deprecated forever.** Tokens marked `$deprecated` years ago are still referenced by live components. Catch it: the build report lists references to deprecated tokens; the count must trend to zero.

## Examples

- [Example 1 — Hard-coded values become semantic tokens](examples/example-1.md) — corrects FE-043.
- [Example 2 — An unchecked amber pair becomes a passing token pair](examples/example-2.md) — corrects FE-046.
- [Example 3 — One default shadow becomes an elevation scale](examples/example-3.md) — corrects FE-045.

## Recall anchors

- Values live in tokens; components name roles, never numbers.
- Three tiers; themes override semantic names, not files.
- A pair passes contrast before it is named.
- Scales have roles — radius, elevation, spacing, duration.
- Retire with `$deprecated` and a pointer, never by deletion.

## Checklist

- [ ] Token source is DTCG JSON; outputs regenerate cleanly (G-FE-021).
- [ ] No raw hex/px/ms literals in component or page styles (G-FE-022).
- [ ] Every token carries a `$description` (FE-044).
- [ ] Every semantic text/surface pair computes ≥ 4.5:1 or ≥ 3:1 large (G-FE-023).
- [ ] Palette defines primary, secondary, semantic, and neutral roles (FE-047).
- [ ] Elevation and radius applied by role from their scales (FE-045).
- [ ] Any gradient is a named token with a stated brand basis (FE-048).
- [ ] Token diff reviewed; deprecations point at replacements (G-FE-024).
