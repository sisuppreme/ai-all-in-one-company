# experimentation-platform

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md, "Growth experimentation" ; Optimizely, experimentation strategy documentation — https://docs.optimizely.com/experimentation-strategy/docs/take-action-based-on-the-results-of-an-experiment
- **Depends on:** event-tracking (exposure and outcome events ride the shared tracking plan), product-analytics
- **Feeds into:** growth-experiments (D9 — consumes the result payloads this platform emits), dashboards

## When to use / Do NOT use

- **Use when:** building or changing the experimentation infrastructure itself: the assignment function, exposure logging, experiment configuration, sample-ratio-mismatch (SRM) health checks, and the analysis job that produces a result.
- **Do NOT use when:** the question is program discipline — which experiments to run, hypothesis quality, cadence, or the experiment register. Those belong to growth-experiments (D9). This skill owns the machinery (assignment, exposure, health checks); D9 owns the program and keeps the register. A result this platform emits is an input to D9's record, never a substitute for it.

## Rules

1. **AN-041 — Assignment is a deterministic hash.** A unit's variant is computed as a hash of experiment ID + unit ID (usually user ID), bucketed against the configured split. The same inputs always yield the same variant — across sessions, devices, and deploys — and the computation is reproducible in a test.
2. **AN-042 — Assignment is server-verifiable and identical everywhere.** One assignment implementation serves every surface; there is no second client-side bucketing that can disagree with it. Any surface that cannot call the shared function does not run the experiment.
3. **AN-043 — Exposure is logged at assignment time.** The moment a unit is assigned and the variant is actually served, an exposure event (experiment ID, variant, unit ID, timestamp) is written as a durable event into the same analytics stream as the outcome events — not into request logs, not into a side table nobody reconciles.
4. **AN-044 — Exposure is never reconstructed.** Exposure counts come only from AN-043 events. Rebuilding exposure after the fact from pageviews, sessions, or variant-render logs is forbidden: a pageview proves a page rendered, not that a unit was assigned and served a variant.
5. **AN-045 — Pre-registration lives in the experiment config.** Before launch, the versioned experiment config records: hypothesis, exactly one primary metric, guardrail metrics, minimum runtime and sample size, the traffic split, the bot/internal-traffic filtering rules, and the decision rule. The platform refuses to activate an experiment whose config lacks any field.
6. **AN-046 — SRM is a stop condition, enforced by the analysis job.** The analysis job computes a chi-squared check of observed exposure counts against the configured split before producing any result. While the check fails at the significance threshold recorded in the config, the job renders no verdict — it reports the mismatch and the experiment is treated as broken (bucketing, logging, or filtering) until the cause is found.
7. **AN-047 — No peeking-based decisions.** Results unlock at the pre-registered horizon, or the config names a sequential / always-valid method in advance. The platform exposes no "current winner" readout that invites an early stop; a run stopped early for a peeked lead is emitted as invalid, not as a result.
8. **AN-048 — Minimum runtime is one full business cycle.** The pre-registered minimum runtime is at least one complete business cycle for the surface under test (weekday/weekend pattern included), regardless of how quickly the sample size is reached.
9. **AN-049 — One surface, one active experiment — or explicit layers.** Experiments touching the same surface are mutually exclusive by assignment layer: a unit enters at most one of them, enforced by the assignment function, never by hoping the audiences do not overlap.
10. **AN-050 — A leaked or flipped assignment invalidates the run.** If any unit's variant can change mid-run — a salt change, a split edit, a second bucketing path, a config push that rehashes — the affected data is discarded and the run is emitted as invalid with the cause recorded. Contaminated data is never "interpreted with caution."
11. **AN-051 — Filtering rules are pre-registered and symmetric.** Bot, internal-user, and QA exclusions are declared in the config before launch (AN-045) and applied by the pipeline identically to every variant. Post-hoc exclusions invented after seeing results are forbidden; a needed new filter ends the run and starts a new experiment.
12. **AN-052 — Conclusion emits a complete result payload.** When a run ends — horizon reached, stopped, or invalidated — the platform emits one payload: experiment ID, pre-registration reference, primary-metric result with confidence interval, guardrail outcomes, final SRM status, runtime, and the ship/kill/invalid outcome. D9's growth-experiments files this payload in the register, including for losers and inconclusive runs; an experiment that ends without a payload is a platform defect.

## BAN list

- **BAN-AN-021 — Random or per-request assignment.** Banned: bucketing with a random draw, a timestamp, or any input that can give the same unit different variants on different requests. Defeats: DET-CON-015. Bad: the client calls `Math.random() < 0.5 ? 'A' : 'B'` on each page load; a user sees the new checkout on Monday and the old one on Tuesday, and support screenshots contradict each other. Instead: assign by deterministic hash of experiment ID + unit ID per AN-041. Severity: BLOCK.
- **BAN-AN-022 — A verdict rendered while SRM fails.** Banned: an analysis job or dashboard that displays a winner, an effect size, or a ship recommendation for an experiment whose SRM check is failing — the health check exists on paper but never actually gates the output. Defeats: DET-INF-002. Bad: the results page shows "B +4.2%, significant" above a red SRM warning the team has learned to ignore. Instead: the job refuses to render a verdict while SRM fails, per AN-046; only the mismatch and its investigation are reported. Severity: BLOCK.
- **BAN-AN-023 — The peeked "winner."** Banned: stopping an experiment before its pre-registered horizon because a variant is "winning," then reporting the lead as the experiment's result. Defeats: DET-CON-011. Bad: at day two, variant B leads on a secondary metric; the test is stopped, and the launch note claims a measured conversion lift that no valid analysis produced. Instead: run to the horizon or the pre-declared sequential method (AN-047); an early stop is emitted as invalid under AN-050/AN-052, never as a lift. Severity: BLOCK.
- **BAN-AN-024 — Exposure kept only in ephemeral logs.** Banned: recording assignment or exposure only in server console output, request logs, or any store that rotates, restarts away, or is never reconciled against assignment counts. Defeats: DET-INF-013. Bad: the variant each user saw is knowable only from application stdout, which the platform rotated after 24 hours; by analysis day, exposure is unrecoverable and is quietly estimated. Instead: emit a durable exposure event at assignment time per AN-043, reconciled by G-AN-023. Severity: BLOCK.
- **BAN-AN-025 — Mid-run split or salt edits.** Banned: changing the traffic split, the variant set, the targeting, or the hash salt of a running experiment while continuing to pool its data. Defeats: DET-CON-011. Bad: traffic is raised from 10% to 50% and the salt rotated in week two to "balance the arms"; the pooled report presents one experiment where two different assignments ran. Instead: stop the run, emit its payload (AN-052), and start a new experiment ID with the new configuration. Severity: BLOCK.

## Gates

- **G-AN-021 — Assignment determinism test.** Verifies: AN-041, AN-042. Check: automated — hash a fixed set of 10,000 recorded unit IDs twice, in two separate processes simulating different sessions, and diff the variant maps; also assert the observed split matches the configured split within the tolerance stated in the test. Pass: the two maps are identical for 100% of units. Fail: block the experiment launch; the assignment function is fixed and the test re-run. Recorded in: progress.md.
- **G-AN-022 — SRM gate in the analysis job.** Verifies: AN-046. Check: automated — run the analysis job against the live exposure counts; it computes the chi-squared statistic of observed vs. expected counts per variant and compares it with the config's threshold. Pass: the job renders a verdict only when the check passes, and a forced test with skewed fixture counts renders no verdict. Fail: block any result publication; investigate bucketing, logging, or filtering before reading anything. Recorded in: progress.md.
- **G-AN-023 — Exposure-completeness reconciliation.** Verifies: AN-043, AN-044. Check: automated — reconcile exposure-event counts against assignment counts per variant over the run window. Pass: the gap is within the tolerance recorded in the experiment config, and every counted exposure traces to an AN-043 event (zero reconstructed exposures). Fail: results are computed on partial data — publication is blocked until the gap is explained or the run is emitted as invalid. Recorded in: progress.md.
- **G-AN-024 — Pre-registration completeness check.** Verifies: AN-045, AN-048, AN-051. Check: automated — schema-validate the experiment config at activation: hypothesis, one primary metric, guardrails, minimum runtime ≥ one business cycle, minimum sample, split, filtering rules, and decision rule all present. Pass: activation succeeds only with every field present. Fail: activation is refused; the missing field is added to the config, never supplied verbally. Recorded in: progress.md.
- **G-AN-025 — Conclusion payload audit.** Verifies: AN-050, AN-052. Check: list every experiment whose run ended in the period; for each, confirm exactly one result payload exists containing the primary-metric result with confidence interval, final SRM status, and a ship/kill/invalid outcome. Pass: 100% of ended experiments have a complete payload, losers and invalid runs included. Fail: the missing payload is emitted before the next experiment launches on that surface. Recorded in: progress.md.

## Anti-patterns

- **Render-then-assign flicker.** Assignment is deterministic but evaluated in the browser after first paint, so users watch the control render, then swap to the variant. Catch it: if a variant change is visible as a flash, assignment is happening too late — it belongs in the server response or the first evaluation, and the exposure event must mark what was actually served (AN-043).
- **The significance thermometer.** A dashboard shows a live p-value or "percent to significance" that the team watches daily, so the fixed-horizon rule exists in the config and nowhere else. Catch it: if anyone can quote today's leader, AN-047 is already being violated in spirit — hide interim effect readouts; health (SRM, exposure counts) is the only live view.
- **Salt-shuffling to "fix" imbalance.** When arms look uneven, someone rotates the hash salt or nudges the split to even them out, quietly restarting assignment for everyone. Catch it: any mid-run config touch is BAN-AN-025; imbalance is an SRM investigation (AN-046), not a tuning knob.
- **Guardrail theater.** Guardrail metrics are named in the config but the results view shows only the primary metric, so a conversion win that doubled error rates ships unread. Catch it: if the payload (AN-052) can be read without its guardrail section, the view is wrong, not the data.

## Examples

- [Example 1 — Coin-flip bucketing becomes a deterministic hash](examples/example-1.md) — violates/corrects AN-041.
- [Example 2 — The verdict that shipped over a failing SRM check](examples/example-2.md) — violates/corrects AN-046.
- [Example 3 — Exposure rebuilt from pageviews becomes exposure at assignment](examples/example-3.md) — violates/corrects AN-043.

## Recall anchors

- Hash of experiment + unit decides the variant — never chance, never the clock.
- Exposure is an event written when the variant is served, or it did not happen.
- SRM failing means the experiment is broken; no verdict renders until it passes.
- Peeked, flipped, or re-salted data is discarded, not interpreted.
- D12 builds the machinery; D9 runs the program and keeps the register.

## Checklist

- [ ] Assignment is a deterministic hash of experiment ID + unit ID, one implementation for all surfaces (AN-041, AN-042).
- [ ] Determinism test passes: 10,000 unit IDs, two runs, identical variant maps (G-AN-021).
- [ ] Exposure events fire at assignment time into the shared analytics stream (AN-043).
- [ ] Experiment config is pre-registered and complete; activation refuses missing fields (AN-045, G-AN-024).
- [ ] Minimum runtime covers at least one full business cycle (AN-048).
- [ ] Analysis job renders no verdict while the SRM check fails (AN-046, G-AN-022).
- [ ] Exposure counts reconcile with assignment counts within the config's tolerance (G-AN-023).
- [ ] Every ended experiment — win, loss, inconclusive, invalid — has exactly one complete result payload for D9's register (AN-052, G-AN-025).
