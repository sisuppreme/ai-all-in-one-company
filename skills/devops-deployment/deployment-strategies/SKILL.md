# deployment-strategies

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GitHub Docs, "Managing environments for deployment" — https://docs.github.com/en/enterprise-server@3.11/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment ; DORA, "Continuous delivery" — https://dora.dev/capabilities/continuous-delivery/ ; Kubernetes Docs, "Deployment" (rollout and rollback) — https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- **Depends on:** ci-cd
- **Feeds into:** rollback, hosting, reliability

## When to use / Do NOT use

- **Use when:** choosing or changing how a release reaches production — the promotion path, the traffic-shift pattern, the abort conditions — or when a project's deploy is still manual, per-environment, or impossible to reverse.
- **Do NOT use when:** the pipeline itself does not exist yet (ci-cd builds it first), or the question is recovery after a bad deploy has already shipped (rollback owns the response; this skill owns making it possible).

## Rules

1. **DO-041 — Strategy chosen per change, and recorded.** Every release names its strategy — rolling (the default), blue-green, or canary — with the risk reason, in the deploy record. "We always deploy the same way" without a per-change risk check is not a strategy.
2. **DO-042 — No manual deploy steps.** No FTP/SFTP file copies, no SSH `git pull` + restart, no builds on the production server. Deploys run from CI off the built artifact, end to end.
3. **DO-043 — Build once, promote unchanged.** One immutable artifact (image digest or version tag) is promoted preview → staging → production. What was tested in staging is bit-identical to what ships.
4. **DO-044 — Every deploy leaves a record.** Artifact digest, commit SHA, strategy used, who/what triggered it, and when. The live production revision is identifiable from the record at any moment.
5. **DO-045 — Production sits behind environment protection.** The production deploy job runs only from the protected branch and only after the environment's protection rules pass (required reviewers, deployment-branch restrictions, wait timer where configured). For a single operator, the reviewer gate becomes a deliberate pause plus the release checklist — the gate is never silently deleted.
6. **DO-046 — Abort condition named before promotion.** Every blue-green or canary release names, in advance, the metric and threshold that sends traffic back (for example: error rate above baseline +1 percentage point for 5 minutes). A strategy without a written abort condition does not start.
7. **DO-047 — Database changes expand and contract.** Schema changes ship so old and new code both run against the new shape during the promotion window: add first, migrate reads/writes, remove the old shape in a later release.
8. **DO-048 — Config comes from the environment, never the artifact.** All deploy-varying values (URLs, credentials, toggles) arrive via environment variables or a config service per target. The artifact itself is identical in every environment.
9. **DO-049 — Deploy and release are separate events.** Risky user-visible changes deploy dark behind a feature flag; the flag flip is the release. Rollback of a flagged change is the flag flip first — seconds, no redeploy.
10. **DO-050 — Smoke-test the idle side before switching.** In blue-green, the idle environment passes its health check and a key-route smoke test before the router moves any traffic to it.
11. **DO-051 — Previous version stays returnable.** The old environment/artifact remains deployable until the new version clears its observation window. Tearing down the return path in the same action that ships is a failed deploy design.
12. **DO-052 — Canary promotion is metrics-gated, not clock-gated.** Each canary step compares error rate and latency against the pre-release baseline; traffic increases only while both stay within the DO-046 thresholds, and any breach aborts automatically or by the named operator action.

## BAN list

- **BAN-DO-021 — The hand-carried deploy.** Banned: shipping production changes by FTP/SFTP upload, SSH `git pull` + restart, or editing files on the live server. Defeats: DET-INF-004. Bad: the release note says "uploaded the new build folder and restarted the service" — nobody can say which commit is live. Instead: deploy from CI off the versioned artifact and record the digest and SHA (DO-042, DO-044). Severity: BLOCK.
- **BAN-DO-022 — The per-environment rebuild.** Banned: rebuilding the artifact for each environment, or deploying a floating target (`latest` tag, branch HEAD) instead of the tested artifact. Defeats: DET-INF-026. Bad: staging passed on Monday's build; production was rebuilt Wednesday "from the same code" with a newer transitive dependency. Instead: promote the one digest that passed staging, unchanged (DO-043). Severity: BLOCK.
- **BAN-DO-023 — Config baked into the artifact.** Banned: environment-specific URLs, hosts, or toggles compiled or copied into the artifact or a hand-edited per-server config file. Defeats: DET-INF-007. Bad: the production image contains `API_URL=https://api.example.com` as a source constant, so staging needs a different image. Instead: inject the value per target from environment variables or a config service (DO-048). Severity: BLOCK.
- **BAN-DO-024 — The abort-free rollout.** Banned: a canary or blue-green release with no pre-named metric, threshold, and return action. Defeats: DET-INF-017. Bad: "we'll watch the dashboard for a bit and roll back if it looks bad" — at 3 a.m. nobody knows what "bad" is or which button returns traffic. Instead: write the abort metric, threshold, and switch-back action into the release plan before promotion starts (DO-046). Severity: BLOCK.
- **BAN-DO-025 — The same-release contract.** Banned: dropping or renaming a database column/table in the same release that stops using the old shape. Defeats: DET-INF-018. Bad: the release removes `users.full_name` while the still-running old version reads it during the rollout, erroring every request it serves. Instead: expand in this release, contract in a later one after the old code is gone (DO-047). Severity: BLOCK.

## Gates

- **G-DO-021 — Deploy-history audit.** Verifies: DO-043, DO-044. Check: automated — script the deploy log/platform API for the last three production deploys; each must resolve to a commit SHA and an artifact digest, and the production digest must equal the digest that passed staging for that release. Pass: 3 of 3 resolve and match. Fail: block the next release until records exist. Recorded in: progress.md.
- **G-DO-022 — Manual-step scan.** Verifies: DO-042. Check: automated — grep CI workflows, deploy scripts, and the runbook for `ftp `, `scp `, `rsync` to a production host, and `ssh` followed by `git pull` or a build command; deploy tooling that runs from CI off an artifact is exempt and must be annotated as such. Pass: zero unannotated hits. Fail: block shipment; the manual step is automated or the release does not go. Recorded in: progress.md.
- **G-DO-023 — Switch and switch-back drill.** Verifies: DO-046, DO-050, DO-051. Check: manual, timed, in staging — run the blue-green/canary switch, exercise the written abort threshold, and switch back; the previous version must be serving again within the project's rollback target time. Pass: switch-back completes in target with the abort condition demonstrably triggered. Fail: the strategy is downgraded to rolling until the drill passes. Recorded in: progress.md.
- **G-DO-024 — Production environment protection.** Verifies: DO-045. Check: automated where the platform API allows, else console inspection with a screenshot filed — the production environment has branch restrictions and its approval/pause rule enabled, and a test deploy from a non-protected branch is refused. Pass: refusal observed and rules present. Fail: block production deploys until protection is configured. Recorded in: progress.md.

## Anti-patterns

- **The ceremonial canary.** One percent of traffic for five minutes, then full promotion because the clock ran out — no baseline comparison was ever made. Catch it: the canary record shows elapsed time but no error-rate or latency numbers against baseline.
- **Staging theater.** Staging runs a different artifact shape or hand-set config, so a green staging drill proves nothing about production. Catch it: diff the staging and production deploy specs; differences beyond env values are the tell.
- **The flag graveyard.** Feature flags are flipped on and never removed; six months later nobody can say which flags are live or safe to touch. Catch it: list flags older than one release cycle with no owner — each gets an owner and a removal date or is deleted.
- **Deploy by hero.** One person holds the deploy sequence in their head; releases wait for them and incidents wait longer. Catch it: a second operator (or the same operator, cold, from the runbook alone) must be able to run the deploy — if the runbook cannot carry it, the process is the hero.

## Examples

- [Example 1 — Hand-carried deploy replaced by artifact promotion](examples/example-1.md) — corrects DO-042, DO-043.
- [Example 2 — Abort-free canary given metrics gates](examples/example-2.md) — corrects DO-046, DO-052.
- [Example 3 — Same-release column drop split into expand-and-contract](examples/example-3.md) — corrects DO-047.

## Recall anchors

- Build once; promote the same artifact everywhere.
- No hands on production: CI deploys, records prove it.
- No abort condition written down, no rollout.
- Expand now, contract later — old and new code coexist.
- The flag flip is the release; the flip back is the rollback.

## Checklist

- [ ] Strategy named for this change, with its risk reason, in the deploy record (DO-041).
- [ ] Deploy runs entirely from CI off the staging-passed digest — no manual steps (G-DO-022, DO-043).
- [ ] Deploy record holds digest, commit SHA, strategy, trigger, timestamp (DO-044).
- [ ] Production environment protection verified; non-protected-branch deploy refused (G-DO-024).
- [ ] Abort metric, threshold, and return action written before promotion (DO-046).
- [ ] Database changes are expand-only in this release; contract deferred (DO-047).
- [ ] Previous version still deployable until the observation window closes (DO-051).
- [ ] Last switch-back drill passed within the rollback target time (G-DO-023).
