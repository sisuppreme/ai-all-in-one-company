# Example 3 — The judge nobody calibrated

## Before

```text
evals/summarizer/config.yaml
judge:
  model: <whatever the provider's default alias resolves to this week>
  prompt: "Score the summary's quality from 0 to 100."
  temperature: unset

Dashboard, release review: "Summary quality: 94.2% (judge-scored). Ship it."
```

The judge model is unpinned, its prompt has no rubric, and its scores have never been compared with a single human judgment. The decimal precision on the dashboard is decoration: nobody knows whether 94.2 means good, or whether the judge would score a summary that drops the document's main conclusion at 90.

## After

```text
evals/summarizer/config.yaml
judge:
  model: <pinned model ID, named in config>
  temperature: 0
  prompt_file: evals/summarizer/judge-rubric.md   # criteria: coverage of source claims,
                                                  # no unsupported claims, abstains on empty input
calibration:
  sample: evals/summarizer/calibration.jsonl     # 120 items with human labels
  agreement_floor: 0.80                          # recorded before first gated run

Calibration run (G-AI-072), stored with the eval report:
judge vs. human agreement 0.86 ≥ floor 0.80 — judge scores may gate.
Deterministic graders decide schema validity and forbidden strings first (AI-144);
the judge scores only the rubric criteria no cheaper grader can decide.
```

The judge is a measured instrument: pinned model and temperature, a written rubric, and a recorded agreement rate against human labels that is re-measured whenever the judge changes. Its scores can now be published — with their provenance.

## Note

Violates AI-145 (BAN-AI-074): an uncalibrated judge's output is a number without a measurement behind it. Corrected by pinning the judge, giving it a rubric, and gating its authority on recorded agreement with human labels (G-AI-072).
