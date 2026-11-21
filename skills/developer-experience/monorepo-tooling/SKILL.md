# monorepo-tooling

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Turborepo concepts and pipeline practice — https://www.devtoolsguide.com/turborepo-monorepo-guide/ ; mise dev tools (task/tool layer at repo root) — https://mise.jdx.dev/dev-tools/
- **Depends on:** dev-environment, dependency-management
- **Feeds into:** versioning, ci-cd

## When to use / Do NOT use

- **Use when:** a project has two or more deployables (web app plus API, worker, or second app) or a package genuinely shared by more than one of them, and the operator wants shared code and atomic cross-package changes in one repository.
- **Do NOT use when:** the project is a single app with no shared package — a plain single-package repo (or separate repos per deployable) is the honest default. Do not scaffold a monorepo for a landing page, and do not use this skill to split one app into packages that only exist to look architectural.

## Rules

1. **DX-021 — Stated trigger, recorded.** A monorepo is created only when the trigger holds: 2+ deployables, or one package consumed by 2+ deployables. The reason is recorded in the project's stack file or an ADR before scaffolding. No trigger, no monorepo.
2. **DX-022 — One lockfile, at the root.** Exactly one lockfile exists, at the repository root, committed. CI installs from it frozen; a package-level lockfile or an install that modifies the root lockfile is a defect.
3. **DX-023 — Declared internal dependencies only.** Every internal package a package uses is declared in that package's manifest. The task graph (build/lint/test order) is derived from those declarations by the task runner — never from a hand-maintained build-order list or script sequence.
4. **DX-024 — Entry points, not reach-across.** A package imports another package only through its declared package name and public entry point (or declared export subpaths). Relative imports that cross a package boundary are forbidden.
5. **DX-025 — Acyclic, tool-enforced boundaries.** The package dependency graph has no cycles, and boundary rules (allowed dependency directions, entry-point-only imports) are enforced by lint or graph tooling in CI — not by convention or review memory.
6. **DX-026 — Every task declares outputs.** Each build/test task in the pipeline config declares its outputs. A task that cannot declare outputs is marked uncacheable in the config with the reason written next to it.
7. **DX-027 — Cache keys cover all inputs.** Cache keys include the lockfile hash and every environment variable the task reads. A cache hit after any input changed is a correctness bug to be fixed in the key, never a speedup to be celebrated.
8. **DX-028 — Shared configs live in config packages.** TypeScript, lint, and test-preset configs live in internal config packages and are extended or referenced by each package. Config files are never copy-pasted per package.
9. **DX-029 — Root scripts are the only entry points.** `build`, `lint`, `test`, and `dev` run from the root and fan out through the task graph. Documentation names only root scripts; per-package scripts are implementation detail.
10. **DX-030 — One versioning model, chosen up front.** The repo states its model before the first release: independent per-package versioning (Changesets-style) or one fixed version for the whole repo. The two are never mixed by accident; internal dependency ranges follow the chosen model.
11. **DX-031 — Affected-only CI for changes.** Pull-request CI builds and tests only the changed packages and their dependents (affected/filter run). A change to a shared package automatically pulls every dependent into the run. The full pipeline runs on merge to the main branch.
12. **DX-032 — Deliberate internal ranges.** Internal dependencies use the workspace protocol (or the ecosystem equivalent) so local packages link locally. No internal or external dependency is declared with `*` or `latest`.

## BAN list

- **BAN-DX-011 — Reach-across imports.** Banned: importing another package's source by relative path (`../../api/src/db/client`) instead of its declared entry point. Defeats: DET-CODE-014. Bad: `apps/web` imports `../../packages/api/src/internal/session.ts`, so the API package cannot move a file without breaking the web build. Instead: declare `@repo/api` in the web package's manifest and import the exported entry point. Severity: BLOCK.
- **BAN-DX-012 — Copy-pasted shared configs.** Banned: duplicating `tsconfig`, ESLint, or test-preset files into every package and editing the copies separately. Defeats: DET-CODE-032. Bad: five packages carry five near-identical `tsconfig.base.json` copies; one gets `strict: true`, the others silently do not. Instead: one internal config package (e.g. `@repo/tsconfig`) that every package extends. Severity: BLOCK.
- **BAN-DX-013 — Undeclared internal dependency.** Banned: importing an internal package that is not declared in the importing package's manifest, relying on hoisting to make it resolve. Defeats: DET-CODE-028. Bad: `packages/ui` imports `@repo/utils` with no manifest entry; the build passes by hoisting luck and breaks under a stricter linker, and the task graph omits the edge so `ui` is not rebuilt when `utils` changes. Instead: declare every internal import in the manifest so the graph edge exists. Severity: BLOCK.
- **BAN-DX-014 — Wildcard and latest ranges.** Banned: `*` or `latest` as a version range for any dependency, internal or external. Defeats: DET-CODE-028. Bad: `"@repo/utils": "*"` and `"react": "latest"` in two manifests, so two installs a week apart produce different trees under the same lockfile discipline. Instead: workspace protocol for internal packages and the project's deliberate range policy for external ones, resolved by the single root lockfile. Severity: BLOCK.
- **BAN-DX-015 — Monorepo without a trigger.** Banned: scaffolding workspaces, a task runner, and shared packages for a single deployable with no shared package. Defeats: DET-CODE-015. Bad: a marketing landing page ships as a four-package monorepo with a task graph, a remote cache, and one app. Instead: a plain single-package repo; adopt this skill when a second deployable or a genuinely shared package appears. Severity: BLOCK.

## Gates

- **G-DX-011 — Double-run cache verification.** Verifies: DX-026, DX-027. Check: automated — from a clean checkout, run the full root pipeline twice (`turbo run build test` or the Nx equivalent); hash all declared outputs after each run and `diff` the two hash lists. Pass: the second run reports cache hits for every unchanged package and the outputs are byte-identical. Fail: block shipment; fix the task's declared outputs or cache inputs. Recorded in: progress.md.
- **G-DX-012 — Affected-only rebuild test.** Verifies: DX-023, DX-031. Check: automated — in a scratch clone, touch one file in a leaf package and run the CI affected command (e.g. `turbo run build --filter=...HEAD^` or `nx affected`); then touch one file in a shared package and repeat. Pass: the first run builds only the leaf and its dependents, and the second run includes every dependent of the shared package. Fail: block shipment; the graph is missing a declared edge. Recorded in: progress.md.
- **G-DX-013 — Boundary and cycle check.** Verifies: DX-024, DX-025. Check: automated — run the boundary lint/graph check in CI (e.g. the task runner's graph validation plus `grep -rn "from '\.\./" packages/*/src apps/*/src` excluding same-package relative imports), and a cycle detector over the package graph. Pass: zero cross-boundary relative imports and zero cycles. Fail: block the merge. Recorded in: progress.md.
- **G-DX-014 — Single-lockfile frozen install.** Verifies: DX-022, DX-032. Check: automated — `find . -name "*lock*" -not -path "*/node_modules/*"` (ecosystem equivalent) returns exactly one lockfile at the root; then a frozen install (`pnpm install --frozen-lockfile` or equivalent) succeeds and `git status` shows the lockfile unmodified. Pass: one lockfile, frozen install clean. Fail: block the merge. Recorded in: progress.md.

## Anti-patterns

- **The dumping-ground shared package.** A `utils` or `shared` package that every package depends on and into which unrelated helpers are thrown, so any leaf change rebuilds the world. Catch it: list the shared package's dependents and its export count; unrelated domains in one package means split it by domain.
- **Cache-hit triumphalism.** Reporting a high cache-hit rate as a performance win while never verifying that hit outputs match a clean build. Catch it: if G-DX-011's byte-identical check has not run since the pipeline config last changed, the hit rate proves nothing.
- **External version drift inside the repo.** Two packages resolving different major versions of the same external library, so the "shared" platform behaves differently per package. Catch it: run the package manager's dedupe/why report; duplicate majors of one library need a recorded reason or a single aligned range.
- **Root script swamp.** Dozens of root scripts that duplicate package scripts with slight variations (`build:web:fast`, `build:web:ci`) until nobody knows the real entry point. Catch it: if a root script does not fan out through the task graph, delete it or move it into the owning package.

## Examples

- [Example 1 — Reach-across import replaced by a declared dependency](examples/example-1.md) — corrects DX-023, DX-024.
- [Example 2 — Copy-pasted configs replaced by one config package](examples/example-2.md) — corrects DX-028.
- [Example 3 — Hand-ordered build script replaced by a task graph with honest caching](examples/example-3.md) — corrects DX-023, DX-026, DX-027.

## Recall anchors

- No trigger, no monorepo.
- One repo, one lockfile, one version policy.
- If it is imported, it is declared; the graph comes from the manifests.
- Entry points only — never reach across a boundary.
- A cache hit on changed inputs is a bug, not a speedup.

## Checklist

- [ ] The monorepo trigger is recorded and still holds (DX-021).
- [ ] Exactly one lockfile, at the root, and the frozen install leaves it untouched (G-DX-014).
- [ ] Every internal import is declared in the importing package's manifest (DX-023).
- [ ] Zero cross-boundary relative imports and zero package cycles (G-DX-013).
- [ ] Every task declares outputs, or is marked uncacheable with a reason (DX-026).
- [ ] Double-run check passed: cache hits with byte-identical outputs (G-DX-011).
- [ ] Affected-only run rebuilds a shared package's dependents (G-DX-012).
- [ ] Shared configs come from config packages; no copy-pasted config files (DX-028).
- [ ] The versioning model is stated and internal ranges follow it (DX-030, DX-032).
