# ai-evaluation

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.openai.com/api/docs/guides/evaluation-getting-started ; https://www.n4n.ai/blog/golden-datasets-for-llm-evals-how-to-build-one
- **Depends on:** llm-integration, prompt-engineering
- **Feeds into:** prompt-engineering, rag-retrieval, search-relevance, recommendations, ai-observability

## When to use / Do NOT use

- **Use when:** an AI feature is being built or changed — new prompt, model, retrieval, or configuration — and its quality must be measured before release, or when a quality figure about an AI feature is about to be stated anywhere.
- **Do NOT use when:** the task is screening inputs/outputs for safety (use ai-safety), tuning search ranking against a judgment set (use search-relevance, which applies this skill's discipline to NDCG), or watching live traffic (use ai-observability). This skill owns the offline golden-set measurement that gates changes.

## Rules

1. **AI-141 — No golden dataset, no ship.** Every AI feature owns a golden dataset — fixed inputs, each with a reference answer or an explicit grading rubric and a category — stored as a single versioned artifact in the repo. A feature without one does not release, and an eval run once at launch and never again counts as no eval.
2. **AI-142 — Items come from real usage.** Dataset items are seeded from production logs, support failures, and observed failure modes, not invented happy paths. Each item records its source (log, ticket, incident, or authored edge case) so its realism is auditable.
3. **AI-143 — Failure and adversarial categories are mandatory.** The dataset includes, as named categories: malformed and empty inputs, unanswerable questions where abstention is the correct behavior, refusal cases, and adversarial inputs (injection attempts, contradictory instructions). A dataset of only well-formed, answerable questions is incomplete by definition.
4. **AI-144 — Graders run cheapest-first.** Grading stacks deterministic checks first (exact match, schema validity, forbidden strings, required citations), then similarity measures, then a model judge only for criteria no cheaper grader can decide. Every item names which grader decides it.
5. **AI-145 — The judge is pinned and calibrated.** A model judge's model ID and temperature are pinned in the eval config. Before its scores may gate anything, its agreement with human labels is measured on a labeled calibration sample and recorded; it is re-measured at every judge model or judge-prompt change. Below the recorded agreement floor, judge scores are advisory only.
6. **AI-146 — The dataset is reviewed like code.** Dataset changes land as reviewed, versioned diffs with a stated reason. Correcting a wrong reference answer or an ambiguous rubric is legitimate; changing an item because the current stack fails it is not, and the diff must say which of the two it is.
7. **AI-147 — Eval data and tuning data are disjoint.** No golden item, and no near-duplicate of one, appears in prompts, few-shot examples, or fine-tuning data. The eval measures generalization, never memorization of the test itself.
8. **AI-148 — Every change runs the eval.** Any change to a prompt, model ID, retrieval configuration, or grading-relevant parameter triggers a full eval run in CI before merge or release. There is no "trivial change" exemption; wording changes are exactly what evals exist to catch.
9. **AI-149 — Floors and tolerances are set in advance.** Each feature's eval config records, before any run: the minimum overall pass rate for release and the maximum allowed regression per category. A threshold may not be lowered in the same change whose run fails it.
10. **AI-150 — Results are recorded per version.** Every run stores a report naming the prompt version, model ID, retrieval config, and dataset version, with the overall pass rate, the per-category breakdown, and the list of failed items — not just an aggregate number. Reports are kept with the change that produced them.
11. **AI-151 — Production failures feed the dataset.** Failed production cases surfaced by ai-observability (user corrections, escalations, thumbs-down traces) are triaged on a fixed cycle: each is added to the golden dataset as a new item, or rejected with a recorded reason. The dataset version bumps when items are added.
12. **AI-152 — A quality figure carries its provenance.** Any pass rate or quality claim stated in a UI, report, or release note names the dataset version, the stack version, and the run date. A figure that cannot be traced to a stored report (AI-150) is not published.

## BAN list

- **BAN-AI-071 — Fixture eval scored as production quality.** Banned: running the eval against a stubbed model, fixture responses, or a demo pipeline, then reporting the score as the real feature's quality. Defeats: DET-FAKE-009. Bad: the eval harness points at recorded model replies so CI stays green in seconds, and the release notes cite its 100% pass rate. Instead: the runner executes the real wrapper, prompt, model, and retrieval stack end to end (AI-148); stubs belong only in llm-integration's fault-injection tests. Severity: BLOCK.
- **BAN-AI-072 — The test edited to pass.** Banned: deleting, rewording, or re-rubric-ing golden items after a run fails them, so the next run passes without the stack improving. Defeats: DET-FAKE-004. Bad: three failing refund questions are quietly removed from the dataset the night before release, and the dashboard shows the pass rate climbing. Instead: item changes go through reviewed diffs with a correctness reason (AI-146); a genuinely wrong reference is fixed openly and the fix is visible in the version history. Severity: BLOCK.
- **BAN-AI-073 — Happy-path showcase set presented as the eval.** Banned: a small set of easy, well-formed demo questions standing in for the golden dataset, with its score reported as measured quality. Defeats: DET-FAKE-017. Bad: twenty polished questions the demo always nails are labeled "evaluation: 95% accurate," while malformed inputs, unanswerable questions, and injection attempts are never tested. Instead: build the dataset from real usage with the mandatory failure and adversarial categories (AI-142, AI-143). Severity: BLOCK.
- **BAN-AI-074 — Uncalibrated judge presented as measurement.** Banned: a model judge's scores displayed or gated on as precise quality metrics with no human-labeled calibration behind them. Defeats: DET-FAKE-018. Bad: a dashboard shows "Answer quality: 94.2%" from a judge that has never been compared against a single human label, and releases are approved on its movement. Instead: pin the judge, measure its agreement with human labels on a calibration sample, and publish scores only with that agreement recorded (AI-145, AI-152). Severity: BLOCK.
- **BAN-AI-075 — Grading the memorized test.** Banned: tuning prompts, few-shot examples, or fine-tuning data on golden items or near-duplicates, then citing the same set's score as held-out performance. Defeats: DET-FAKE-008. Bad: the twelve hardest eval questions are pasted into the prompt as worked examples; the eval passes 100% and the first unseen user question fails. Instead: keep eval and tuning data disjoint and scan for overlap before a run counts (AI-147, G-AI-073). Severity: BLOCK.

## Gates

- **G-AI-071 — CI eval gate.** Verifies: AI-141, AI-148, AI-149, AI-150. Check (automated): on any change to prompt files, model configuration, or retrieval configuration, CI runs the feature's eval runner against the committed dataset (e.g. `python evals/run_evals.py --feature <feature> --dataset evals/<feature>/golden.jsonl --config evals/<feature>/config.yaml`, adjusted to the project's runner) and writes the report into the change record. Pass: overall pass rate at or above the floor recorded in the eval config, and no category regresses beyond its recorded tolerance. Fail: block merge and release. Recorded in: progress.md.
- **G-AI-072 — Judge calibration check.** Verifies: AI-145. Check (automated): run the pinned judge over the feature's human-labeled calibration sample and compute its agreement with the human labels; store the result with the judge model ID and temperature. Pass: agreement at or above the floor recorded in the eval config. Fail: judge scores are advisory only and may not gate a release until re-calibration passes. Recorded in: progress.md.
- **G-AI-073 — Dataset integrity and contamination scan.** Verifies: AI-141, AI-143, AI-147. Check (automated): a script over the dataset file asserts every item has a category, a source, and a reference answer or rubric; asserts the mandatory failure and adversarial categories are non-empty; and asserts no item's normalized text matches or near-duplicates any prompt few-shot example or tuning file in the repo. Pass: zero violations. Fail: block the eval run from counting toward G-AI-071. Recorded in: progress.md.
- **G-AI-074 — Change-record eval audit.** Verifies: AI-148, AI-150, AI-152. Check (manual): pick the most recent prompt, model, or retrieval change for the feature and open its change record. Pass: the record links a stored eval report naming prompt version, model ID, dataset version, overall and per-category results, and the delta against the previous version. Fail: the change is treated as unmeasured and re-run before the next release. Recorded in: progress.md.
- **G-AI-075 — Production-failure intake review.** Verifies: AI-151. Check (manual): at the feature's review cycle, list the failed production cases flagged by ai-observability since the last review. Pass: every case is either present as a new golden item (dataset version bumped) or carries a recorded rejection reason. Fail: intake is completed before the next release is approved. Recorded in: progress.md.

## Anti-patterns

- **Vibes-based comparison.** Two versions are compared by eyeballing a handful of outputs and declaring the new one "better." Catch it by asking for the run report: if no dataset version and pass rates exist, the comparison never happened, however convincing the samples look.
- **Aggregate-only reporting.** A single overall pass rate is quoted while one category — usually abstention or adversarial — has silently collapsed to zero. Catch it by refusing any report without the per-category breakdown AI-150 requires.
- **Stale golden set.** The dataset has not changed in months while the product, corpus, and user behavior moved on; the eval now certifies last year's feature. Catch it by checking the dataset's version history against the production-failure intake (G-AI-075): no new items means intake is not happening.
- **Rubric-free judge prompts.** The judge is told to "score quality from 1–10" with no rubric, examples, or pinned settings, so its scores drift with phrasing and cannot be compared across runs. Catch it by reading the judge prompt in the eval config: no rubric and no pinned model means the numbers are decoration.

## Examples

- [Example 1 — The 95% showcase set](examples/example-1.md) — violates/corrects AI-142, AI-143 (BAN-AI-073).
- [Example 2 — The failing questions that disappeared](examples/example-2.md) — violates/corrects AI-146 (BAN-AI-072).
- [Example 3 — The judge nobody calibrated](examples/example-3.md) — violates/corrects AI-145 (BAN-AI-074).

## Recall anchors

- No golden dataset, no ship — and launch-day-only counts as none.
- Items come from real failures, not invented happy paths.
- Cheapest grader first; the judge is pinned and calibrated.
- Never edit the test to pass; never tune on the test.
- "It felt better" is not a release criterion — the recorded delta is.

## Checklist

- [ ] The feature has a versioned golden dataset in the repo, seeded from real usage, with source recorded per item (AI-141, AI-142).
- [ ] Failure, adversarial, refusal, and unanswerable/abstention categories exist and are non-empty (AI-143, G-AI-073).
- [ ] Each item names its grader, stacked cheapest-first: deterministic, similarity, then judge (AI-144).
- [ ] The judge model and temperature are pinned, and its agreement with human labels is measured and recorded (AI-145, G-AI-072).
- [ ] Dataset changes are reviewed, versioned diffs with correctness reasons — none made to rescue a failing run (AI-146).
- [ ] No golden item or near-duplicate appears in prompts, few-shot examples, or tuning data; contamination scan is clean (AI-147, G-AI-073).
- [ ] The eval ran in CI for this change; overall pass rate meets the pre-recorded floor and no category regressed beyond tolerance (AI-148, AI-149, G-AI-071).
- [ ] The report is stored with prompt/model/dataset versions, per-category results, and failed items, and any published figure cites that provenance (AI-150, AI-152).
