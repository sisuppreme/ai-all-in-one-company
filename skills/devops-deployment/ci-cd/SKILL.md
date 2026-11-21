# ci-cd

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.github.com/en/actions/get-started/continuous-integration ; https://dora.dev/capabilities/continuous-delivery/
- **Depends on:** none — standalone: the pipeline is configured from this repo's own build/test commands and branch layout, read directly; no other skill's output is an input. Feeds deployment-strategies, preview-environments, rollback.
- **Feeds into:** deployment-strategies, preview-environments, rollback

## When to use / Do NOT use

- **Use when:** Setting up or auditing the automated pipeline that builds, tests, publishes, and deploys a project — workflow files, branch protection, artifact publishing, deploy jobs, and delivery metrics.
- **Do NOT use when:** Choosing how a release rolls out to users (rolling, blue-green, canary) — that is deployment-strategies. Building the images the pipeline publishes — that is containers.

## Rules

1. **DO-001 — One pipeline definition, in the repo.** The whole pipeline lives in version-controlled workflow files (`.github/workflows/*.yml` or the platform equivalent); no build or deploy step exists only in a console, a wiki, or someone's shell history.
2. **DO-002 — Fixed stage order.** Every run executes in order: checkout → install → lint → build → unit tests → integration tests → end-to-end tests → publish artifact → deploy jobs per environment. A stage may be empty only when the project genuinely has none of that test type, recorded in progress.md.
3. **DO-003 — The pipeline triggers on push and pull request, and its checks are required.** The build/test workflow runs on every push and every pull request, and its status checks are required checks on the protected branch, so a failing run blocks merge.
4. **DO-004 — Prove the pipeline can fail.** Before the gate is trusted, open a throwaway pull request containing a deliberately failing test and confirm the check reports failure and merge is blocked; record the drill result in progress.md. Repeat after any workflow or branch-protection change.
5. **DO-005 — Build once, promote the same artifact.** The artifact deployed to production is bit-identical to the one tested in staging; deploy jobs reference it by digest or immutable version tag, never by rebuilding from source.
6. **DO-006 — Gating jobs run everything, for real.** No skipped tests, no `continue-on-error`, and no commented-out steps on any job whose check is required; a step that cannot run is fixed or the job stops being a gate and the change is recorded.
7. **DO-007 — Install from the lockfile, in CI only.** Dependencies install with the lockfile-frozen command (`npm ci`, `--frozen-lockfile`, or the ecosystem equivalent); nothing installs dependencies at container start or deploy time.
8. **DO-008 — Every deploy leaves a record.** Each deploy writes one record containing the artifact digest, the commit SHA, who or what triggered it, and the timestamp; the live revision of every environment is identifiable from these records alone.
9. **DO-009 — Dependency updates flow as automated pull requests.** Dependabot or Renovate is configured for the project's ecosystems and base images, and CI scans dependencies and images for known vulnerabilities, failing the run on critical findings.
10. **DO-010 — Workflow files are linted in CI.** The pipeline runs a workflow linter (e.g., actionlint) on its own workflow files; a lint error fails the run like any other check.
11. **DO-011 — Secrets come from the CI secret store only.** Workflow files reference secrets by name from the platform secret store; no credential value is written into a workflow file, echoed into logs, or passed to builds triggered by untrusted forks.
12. **DO-012 — Delivery is measured with the DORA four keys.** Deployment frequency, lead time for changes, change fail rate, and failed-deployment recovery time are computed from pipeline and incident records on a regular cadence and reviewed in progress.md — never estimated from memory.

## BAN list

- **BAN-DO-001 — Decorative CI.** Banned: a workflow exists but its checks are not required, so merges proceed on red. Defeats: DET-INF-002. Bad: the test workflow runs only on pushes to `main`, after the merge it was meant to gate. Instead: make the build/test checks required status checks on the protected branch so a failure blocks merge. Severity: BLOCK.
- **BAN-DO-002 — Neutered gating job.** Banned: skipped tests, `continue-on-error`, or commented-out steps on a job whose check is required. Defeats: DET-INF-002. Bad: the test job carries `continue-on-error: true` "until the flaky tests are fixed." Instead: remove the silencer, fix or quarantine the failing test in the open, and let a red job fail the run. Severity: BLOCK.
- **BAN-DO-003 — Hand-carried deploy.** Banned: deploying by copying files over FTP/SFTP, SSHing in to `git pull` and restart, or building on the production server. Defeats: DET-INF-004. Bad: the release step rsyncs the working tree to the server and restarts the process by hand. Instead: the pipeline's deploy job promotes the CI-built immutable artifact and writes a deploy record. Severity: BLOCK.
- **BAN-DO-004 — Floating production artifact.** Banned: production deploys reference a `latest` tag, an ungated branch HEAD, or whatever installs at container start. Defeats: DET-INF-026. Bad: the deploy job runs `docker pull app:latest`, so every restart is an untested upgrade. Instead: deploy the exact digest recorded when the artifact was published and tested. Severity: BLOCK.
- **BAN-DO-005 — Dependency time capsule.** Banned: no automated update tool configured and no vulnerability scan in CI, so the lockfile and base images age untouched from creation day. Defeats: DET-INF-025. Bad: six months after setup there is no Dependabot/Renovate config and no scan step; the base image tag predates two security releases. Instead: enable automated update pull requests and add a CI scan step that fails on critical findings. Severity: WARN.

## Gates

- **G-DO-001 — Broken-test drill (automated).** Verifies: DO-003, DO-004. Check: open a throwaway pull request with a deliberately failing test; query the check-run status via the platform API and confirm the required check concludes `failure` and the branch ruleset reports merge blocked. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per §6.3; it unblocks when a hosted platform with branch rulesets and a check-runs API exists and the drill has been run there. Pass: check is red and merge is refused. Fail: block shipment — the gate is decoration until the drill passes. Recorded in: progress.md.
- **G-DO-002 — Artifact identity check (automated).** Verifies: DO-005, DO-008. Check: script reads the artifact digest from the staging deploy record and the production deploy record for the same release and compares them (`test "$STAGING_DIGEST" = "$PROD_DIGEST"`). Pass: digests are identical. Fail: block shipment and rebuild the promotion path. Recorded in: progress.md.
- **G-DO-003 — Workflow lint (automated).** Verifies: DO-001, DO-010. Check: run `actionlint .github/workflows/*.yml` (or the platform's equivalent linter) as a CI step. Pass: exit code 0. Fail: block merge until the workflow files lint clean. Recorded in: progress.md.
- **G-DO-004 — Gating-job integrity scan (automated).** Verifies: DO-006. Check: `grep -rn "continue-on-error: *true\|skipTests\|test.skip" .github/workflows/` returns no hits inside jobs wired to required checks. Pass: zero hits. Fail: block merge; remove the silencer or un-require the check with the change recorded. Recorded in: progress.md.
- **G-DO-005 — Deploy-record audit (manual).** Verifies: DO-008, DO-012. Check: open the deploy records for the last three production deploys; each must resolve to an artifact digest, a commit SHA, a triggering actor, and a timestamp, and the DORA figures in progress.md must be recomputable from these records plus the incident log. Pass: all three records complete and the metrics recompute. Fail: warn, and fix the record-keeping before the next release. Recorded in: progress.md.

## Anti-patterns

- **Pipeline as documentation.** Beautiful workflow YAML that has not run in weeks because triggers were narrowed to manual dispatch; catch it by checking the date of the last run, not the file.
- **Snowflake staging.** Staging was hand-tweaked (extra env values, a manual hotfix) until a green staging run no longer predicts production; catch it by diffing staging's effective config against what the pipeline would produce.
- **Slow-feedback batching.** The pipeline takes so long that everyone batches huge pull requests to suffer it once; the gate still passes, but review quality and lead time quietly rot. Watch pull request size alongside pipeline duration.
- **Metrics theater.** DORA numbers quoted in a review that nobody can recompute from pipeline and incident records; if the figures have no query or export behind them, they are decoration.

## Examples

- [Example 1 — A gate that actually gates](examples/example-1.md) — violates/corrects DO-003, DO-006.
- [Example 2 — Build once, promote the digest](examples/example-2.md) — violates/corrects DO-005.
- [Example 3 — Lockfile install, CI only](examples/example-3.md) — violates/corrects DO-007.

## Recall anchors

- If a red pipeline can still merge, there is no pipeline.
- Build once; promote the digest, never rebuild for production.
- A gate you have not deliberately broken is a gate you are assuming.
- Every deploy leaves a record: digest, SHA, actor, time.
- DORA numbers come from records, not from vibes.

## Checklist

- [ ] Pipeline definition is committed and triggers on push and pull request (DO-001, DO-002).
- [ ] Build/test checks are required on the protected branch (DO-003).
- [ ] Broken-test drill performed and recorded after the last workflow or protection change (DO-004).
- [ ] Staging and production deploy records show the identical artifact digest (DO-005).
- [ ] No `continue-on-error`, skipped tests, or commented-out steps on gating jobs (DO-006).
- [ ] Dependencies install from the lockfile in CI; nothing installs at container start or deploy time (DO-007).
- [ ] Last three deploys each resolve to digest, commit SHA, actor, and timestamp (DO-008).
- [ ] Automated dependency-update pull requests are flowing and the CI vulnerability scan is green (DO-009).
