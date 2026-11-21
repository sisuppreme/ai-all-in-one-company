# load-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Grafana k6, "Thresholds" — https://grafana.com/docs/k6/next/using-k6/thresholds/ ; PROJECT_ANATOMY.md, Load and performance testing element
- **Depends on:** test-strategy, test-data
- **Feeds into:** qa-gates, performance-budgets

## When to use / Do NOT use

- **Use when:** a release candidate must prove it holds the project's performance budgets under realistic load, a capacity question needs a measured answer, or a performance regression is suspected between releases.
- **Do NOT use when:** the question is whether a feature works at all (that is e2e-testing), whether one screen feels fast in a browser audit (performance-budgets owns the budget; a Lighthouse run is not a load test), or the target is a third party's production service — never load-test what you do not own.

## Rules

1. **QA-121 — Percentiles, never averages.** Results are reported and gated on p(95), p(99), and error rate. A mean latency is never a result; a mean that hides a collapsing p99 is a failed report.
2. **QA-122 — Journey mix, not one endpoint.** The script models the real journeys — login, browse, search, checkout — in production-like proportions. A single-endpoint run is labeled a smoke run in its header and its report.
3. **QA-123 — The header declares the run.** Every script header states, before the run executes: scenario mix, data volume, target environment, and the document each threshold came from. A run whose header is filled in afterward is void.
4. **QA-124 — Production-shaped data.** Release runs execute against production-shaped data volumes. A run against an empty or fixture-sized database is a smoke run and cannot satisfy a release gate.
5. **QA-125 — Thresholds live in the budget.** Threshold values are copied from the project's performance budget / SLO documents (owned by D12). Changing a value is a reviewed change to those documents, never an edit inside the test PR.
6. **QA-126 — Thresholds before the run.** Thresholds are written into the script before execution and are part of the reviewed script. Thresholds added or adjusted after seeing results void the run.
7. **QA-127 — Staged load profile.** Every release scenario declares ramp-up, steady hold, and spike stages. Instant full load is a smoke profile, not a release scenario.
8. **QA-128 — Third parties stubbed or sandboxed.** Payment, email, and other external providers are stubbed or run in sandbox mode. A load run never sends its traffic to a real provider's production endpoints.
9. **QA-129 — The exit code is the gate.** The k6 exit code is wired into the pipeline: non-zero blocks the release. A manual override is recorded as an override, never as a pass.
10. **QA-130 — Results archived per release.** The run summary, the environment record, and the declared data volume are archived with the release, so regressions read as trends across releases instead of being rediscovered.
11. **QA-131 — Bottlenecks become defects.** Every threshold breach or bottleneck is filed as a defect with the run's evidence — percentile table and a profile — attached. "It got slow at 400 users" without a profile is not a finding.
12. **QA-132 — The environment is named.** Release runs execute against staging or a production-like environment whose configuration is recorded with the results. A run against a developer machine is a smoke run.

## BAN list

- **BAN-QA-061 — The toy-dataset proof.** Banned: presenting a run against an empty or fixture-sized database as release-grade load evidence. Defeats: DET-FAKE-017. Bad: the release notes claim "checkout holds p(95) under 800 ms at 500 users" from a run seeded with 12 products and 3 user accounts. Instead: seed production-shaped volumes, declare the volume in the script header, and label any small-data run a smoke run that cannot satisfy the release gate. Severity: BLOCK.
- **BAN-QA-062 — The canned target.** Banned: hammering one static or cached page and reporting the numbers as application load results. Defeats: DET-FAKE-008. Bad: the script requests only the homepage — served from cache — and the report announces "10,000 requests/second sustained" for the whole system. Instead: drive the journey mix against the real application and data tier, and report per-journey percentiles. Severity: BLOCK.
- **BAN-QA-063 — The doctored green gate.** Banned: loosening a threshold, trimming the load profile, or reclassifying a failed run so the pipeline shows a pass the system never earned. Defeats: DET-NONE — no DET parameter names this signal; governed by QA-125. Bad: p(95) is raised from 800 ms to 2,000 ms inside the test PR after a failing run, and the release ships on the new green check. Instead: the run fails, a defect is filed with the evidence, and any threshold change goes through review of the budget document itself. Severity: BLOCK.
- **BAN-QA-064 — The frozen result.** Banned: carrying performance figures from a previous release, a template, or a target document into a report as this release's measured results. Defeats: DET-FAKE-004. Bad: three consecutive release reports show the identical p(95) of 212 ms because the summary block is copied forward each time. Instead: every reported figure comes from the archived summary of the run it claims to describe, and the archive is linked from the report. Severity: BLOCK.

## Gates

- **G-QA-061 — Release load gate.** Verifies: QA-121, QA-125, QA-129. Check: automated — in CI on the release candidate, run `k6 run scripts/load/release.js`; the script carries thresholds on `http_req_duration` p(95) and p(99) and on the `http_req_failed` rate. Pass: k6 exits 0. Fail: non-zero exit blocks the release; no manual pass is recorded. Recorded in: progress.md.
- **G-QA-062 — Seeded-fault threshold check.** Verifies: QA-126, QA-129. Check: automated — in a throwaway run, tighten one threshold below current measured performance (for example p(95) at 1 ms) and re-run the release script. Pass: k6 exits non-zero and the pipeline blocks. Fail: the gate machinery is broken; repair it before any release run counts. Recorded in: progress.md.
- **G-QA-063 — Data-volume audit.** Verifies: QA-123, QA-124. Check: automated — a pre-run script prints the seeded row counts of the test environment and diffs them against the volumes declared in the script header and the production-shaped minimum recorded in TESTING.md. Pass: declared and seeded volumes match and meet the minimum. Fail: the run is reclassified as a smoke run and cannot satisfy G-QA-061. Recorded in: progress.md.
- **G-QA-064 — Archive completeness.** Verifies: QA-130, QA-131. Check: automated — after the release run, assert the release archive contains the k6 summary output, the environment record, and a defect link for every threshold breach. Pass: all artifacts present. Fail: the release record is incomplete and is completed before sign-off. Recorded in: progress.md.

## Anti-patterns

- **The victory-lap rerun.** The scenario is re-run until a green result appears, and only the passing run is archived. Catch it: compare the CI run history against the archived summaries — missing failed runs are the tell.
- **The all-cache measurement.** Every request in the "application" scenario is served from cache, so the data tier is never touched and the numbers flatter it. Catch it: check the cache-hit ratio and per-journey breakdown in the run evidence; a release run shows real origin and database traffic.
- **The unprofiled verdict.** "The database is the bottleneck" asserted from latency curves alone, with no query profile or trace behind it. Catch it: ask for the profile attached to the defect (QA-131); a verdict without one is sent back.
- **The spike that never lands.** The profile declares a spike stage, but CI timeouts quietly cut the run during ramp-up, so the spike is never executed. Catch it: compare the stage durations in the run summary against the stages declared in the script.

## Examples

- [Example 1 — Averages replaced by percentile thresholds](examples/example-1.md) — corrects QA-121.
- [Example 2 — A toy-database run relabeled and reseeded](examples/example-2.md) — corrects QA-124.
- [Example 3 — A loosened threshold returned to the budget](examples/example-3.md) — corrects QA-125.

## Recall anchors

- Percentiles and error rate — a mean is never a result.
- Toy data makes a smoke run, never release evidence.
- Thresholds come from the budget, before the run, or the run is void.
- The k6 exit code is the gate; an override is not a pass.
- Every breach becomes a defect with a profile attached.

## Checklist

- [ ] Script header declares scenario mix, data volume, environment, and threshold sources (QA-123).
- [ ] Data-volume audit passed: seeded volumes are production-shaped (G-QA-063).
- [ ] Thresholds match the current budget documents exactly (QA-125).
- [ ] Seeded-fault check observed k6 exiting non-zero (G-QA-062).
- [ ] Release run exited 0 on the release candidate, or the release is blocked (G-QA-061).
- [ ] Third parties were stubbed or sandboxed for the run (QA-128).
- [ ] Summary, environment record, and breach defects are archived with the release (G-QA-064).
- [ ] Report shows p(95), p(99), and error rate per journey — no averages (QA-121).
