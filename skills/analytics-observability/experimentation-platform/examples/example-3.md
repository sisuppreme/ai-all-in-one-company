# Example 3 — Exposure rebuilt from pageviews becomes exposure at assignment

## Before

Nobody instrumented exposure for the onboarding experiment. At analysis time, the analyst reconstructs it: every user who viewed the onboarding page while the experiment was live is counted as "exposed," and split into arms by re-running the bucketing code over the user list. The reconstruction counts users who were assigned but never reached the page, misses users whose variant was served by a cached page, and cannot be reconciled against anything — yet the report presents the counts as measured exposure.

## After

Exposure is an event emitted by the assignment path itself, at the moment the variant is served, into the same analytics stream as the outcomes:

```json
{
  "event": "Experiment Exposed",
  "properties": {
    "experiment_id": "onboarding-2026-11",
    "variant": "guided",
    "unit_id": "u_88412",
    "timestamp": "2026-11-21T09:14:03Z"
  }
}
```

Analysis reads exposure only from these events, and G-AN-023 reconciles their counts against assignment counts per variant; any gap beyond the config's tolerance blocks publication instead of being silently absorbed.

Note: corrects AN-043 (exposure is logged at assignment time as a durable event; see also AN-044, exposure is never reconstructed).
