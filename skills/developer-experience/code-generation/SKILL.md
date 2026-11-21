# code-generation

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OpenAPI Generator overview and workflow — https://nordicapis.com/introduction-to-openapi-generator/ ; OpenAPI Generator usage in practice — https://apidog.com/blog/openapi-generator-5/ ; OpenAPI Specification v3.1.0 — https://spec.openapis.org/oas/v3.1.0
- **Depends on:** dependency-management, dev-environment
- **Feeds into:** refactoring, versioning

## When to use / Do NOT use

- **Use when:** code is produced mechanically from a machine-readable source — an OpenAPI description (clients, server stubs, types), a database schema (ORM models), or project templates (scaffolding) — and whenever generated output already in the repo changes.
- **Do NOT use when:** the code is written by hand, however repetitive it feels; hand-written code belongs to its owning skill. Do not use generation to produce a finished-looking feature: a generated scaffold is a starting shape, not an implementation.

## Rules

1. **DX-041 — Named source of truth.** Every generated artifact traces to one machine-readable source committed in the repo — an OpenAPI description, a schema, or a template set. The generation command and its source are recorded in the project config; output with no named source is deleted, not adopted.
2. **DX-042 — Never hand-edit output.** A change to generated code is made in the source or the template, then regenerated. A hand edit in a generated file is a defect, even if the edit itself is correct.
3. **DX-043 — Generated header.** Every generated file carries the standard header naming the generator, the generator version, and the source file it was generated from. A file in a generated directory without the header is flagged, not assumed hand-written.
4. **DX-044 — Generator pinned.** The generator and its exact version are declared in the dependency manifest and lockfile like any other dependency. Generating with an unpinned or locally different generator version is not permitted.
5. **DX-045 — Deterministic regeneration.** The same source plus the same generator version produces byte-identical output on any machine. Generators that embed timestamps, absolute paths, or unordered iteration are configured or wrapped until the output is stable.
6. **DX-046 — One output rule, stated.** Generated output is either committed (so a source change shows as an output diff in review) or built fresh in CI and never committed. The project states which rule applies; a mixture of both is drift waiting to happen.
7. **DX-047 — Source reviewed like code.** The spec or schema change goes through the same review as a code change. Generation is never a route for an unreviewed API or data-model change to enter the codebase disguised as a mechanical update.
8. **DX-048 — Generated code passes every gate.** Generated code is linted, type-checked, and tested by the same pipeline as hand-written code. "Generated" is not an exemption from any project gate.
9. **DX-049 — Scaffolds fail loudly.** A generated stub that is not yet implemented throws an explicit not-implemented error or carries a failing test. It never returns canned data that callers or UI can mistake for real behavior.
10. **DX-050 — Template overrides are minimal and documented.** Custom templates are versioned with the project. Where a stock template is overridden, the override is as small as possible and the reason is recorded next to the template.
11. **DX-051 — Regeneration runs in CI.** CI regenerates from the committed source and diffs against the committed output (where output is committed). Any difference fails the build; drift is never merged and fixed later.
12. **DX-052 — Hand-written logic lives outside generated files.** Custom behavior goes in files the generator never overwrites — separate modules, registered hooks, or the generator's documented extension points. If no extension point exists, wrap the generated code; do not fork it by editing it.

## BAN list

- **BAN-DX-021 — The hand-edited generated file.** Banned: editing generated output directly instead of changing the source or template and regenerating. Defeats: DET-CODE-014. Bad: a developer patches a validation rule inside the generated API client; the next regeneration silently reverts it, and the client and server disagree until a user hits the bug. Instead: change the OpenAPI description or the template, regenerate, and commit source and output together. Severity: BLOCK.
- **BAN-DX-022 — The unmarked generated file.** Banned: generated output shipped without the generated-file header naming generator, version, and source. Defeats: DET-CODE-007. Bad: a generated parser lands with no header; review flags it as copy-paste duplication and a god function, and a later editor "cleans it up" by hand. Instead: configure the generator to emit the standard header on every file, and fail the header scan (G-DX-023) on any file missing it. Severity: BLOCK.
- **BAN-DX-023 — The canned-data stub.** Banned: a generated endpoint or function that returns sample data, an empty success, or a hardcoded result while callers and UI treat the feature as working. Defeats: DET-CODE-003. Bad: the generated `listInvoices` stub returns two sample invoices; the billing page ships displaying them as the customer's real records. Instead: leave the stub throwing an explicit not-implemented error until the real implementation replaces it (DX-049). Severity: BLOCK.
- **BAN-DX-024 — The unpinned generator.** Banned: generating from a globally installed, latest, or otherwise unrecorded generator version. Defeats: DET-CODE-028. Bad: two developers regenerate the same spec a week apart and get different output because one's generator updated; the diff is noise and the real change is unreviewable. Instead: pin the generator and its version in the manifest and lockfile (DX-044) and generate only through the project's recorded command. Severity: BLOCK.
- **BAN-DX-025 — The gate-exempt generated directory.** Banned: excluding generated code from lint, type checking, or tests "because it is generated." Defeats: DET-CODE-004. Bad: the generated client calls a method the API library does not have; with type checking disabled for that directory, the hallucinated call reaches production and fails at runtime. Instead: run the full pipeline over generated code like any other code (DX-048); fix failures at the source or template. Severity: BLOCK.

## Gates

- **G-DX-021 — Drift check.** Verifies: DX-042, DX-045, DX-051. Check: automated — in CI, regenerate from the committed source into a temporary directory (`<generate command> --output /tmp/regen`) and run `diff -r /tmp/regen <generated dir>`; also run `git status --porcelain <generated dir>` after a local regeneration. Pass: zero differences. Fail: block the merge; the fix is made in the source or template, never by committing the drift. Recorded in: progress.md.
- **G-DX-022 — Determinism check.** Verifies: DX-044, DX-045. Check: automated — run the recorded generation command twice in clean checkouts and compare `find <generated dir> -type f -exec sha256sum {} +` output between the runs. Pass: identical hash lists. Fail: block; find and remove the nondeterminism (timestamp, path, ordering) before any output is committed. Recorded in: progress.md.
- **G-DX-023 — Header scan.** Verifies: DX-043. Check: automated — `grep -rL "<generated-header marker>" <generated dir>` returns no files, and a grep for manual-edit markers in generated files returns nothing. Pass: every generated file carries the header naming generator, version, and source. Fail: block; regenerate with the header configured. Recorded in: progress.md.
- **G-DX-024 — Full pipeline over generated code.** Verifies: DX-048. Check: automated — run the project's lint, type check, and test suite with no exclusion for generated directories. Pass: all three pass. Fail: block; the correction goes into the source or template and is regenerated, not patched in the output. Recorded in: progress.md.
- **G-DX-025 — Stub honesty check.** Verifies: DX-049. Check: automated plus spot check — grep generated stubs for canned return bodies (literal arrays/objects returned from operations with no implementation), and exercise one unimplemented generated endpoint. Pass: every unimplemented operation throws an explicit not-implemented error; no generated stub returns sample data as if real. Fail: block the feature from being presented as working until implemented. Recorded in: progress.md.

## Anti-patterns

- **The quiet regeneration.** Output is regenerated as a side effect of an unrelated change, producing a huge mechanical diff nobody reviews. Catch it: if a diff touches generated files whose source did not change, stop — that is drift or a generator-version change, and it gets its own commit and explanation.
- **Template fork drift.** A stock template is copied into the project "temporarily" and then edited for months, until upgrading the generator means re-applying a fork nobody understands. Catch it: diff project templates against the stock versions; every difference beyond the documented overrides (DX-050) is removed or documented.
- **Generation as architecture.** New modules are added to the spec mainly because generating them is easy, so the API grows surfaces nobody needs. Catch it: review the source diff first (DX-047) and ask what consumer each new operation serves before looking at the output at all.
- **The almost-generated file.** A file starts as generated output, is copied elsewhere, and is then hand-maintained — two versions of the same logic, one stale. Catch it: search for near-duplicates of generated files outside the generated directory; the copy is deleted or replaced by an import.

## Examples

- [Example 1 — A hand-edited client, fixed at the source](examples/example-1.md) — corrects DX-042.
- [Example 2 — A canned-data stub made honest](examples/example-2.md) — corrects DX-049.
- [Example 3 — Nondeterministic output from an unpinned generator](examples/example-3.md) — corrects DX-044, DX-045.

## Recall anchors

- Edit the source, never the output.
- Same source, same generator, same bytes — on any machine.
- If it is generated, it is marked, pinned, and gated.
- A stub that lies is worse than a stub that throws.
- Drift in CI is a failed build, not a follow-up task.

## Checklist

- [ ] Every generated artifact names its committed source of truth (DX-041).
- [ ] Generator and version are pinned in the manifest and lockfile (DX-044).
- [ ] Drift check passes: regeneration matches committed output exactly (G-DX-021).
- [ ] Determinism check passes: two clean regenerations are byte-identical (G-DX-022).
- [ ] Every generated file carries the standard header (G-DX-023).
- [ ] Lint, type check, and tests pass with no generated-directory exclusions (G-DX-024).
- [ ] No unimplemented stub returns canned data; stubs throw not-implemented (G-DX-025).
- [ ] Template overrides are minimal, versioned, and documented (DX-050).
