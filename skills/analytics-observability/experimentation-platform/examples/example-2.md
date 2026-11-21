# Example 2 — The verdict that shipped over a failing SRM check

## Before

The checkout experiment is configured for a 50/50 split, but after one week the exposure counts are 61,204 control and 48,910 treatment. The results page renders anyway:

> **Variant B: +4.2% conversion (p = 0.01). Recommendation: ship.**

The team ships B. Two weeks later someone notices the treatment arm was under-filled because a CDN rule served the control to a slice of mobile traffic — the "+4.2%" was measuring which users the CDN dropped, not the checkout change. The launch note quoting the lift is still in the release record.

## After

The analysis job runs the SRM check before it computes anything else:

```
$ analyze-experiment checkout-2026-11
SRM check: observed 61204 / 48910 vs expected 50/50 — chi-squared p < 0.001
FAIL (threshold in config: 0.001). No verdict rendered.
Investigate: bucketing, exposure logging, or traffic filtering.
```

No effect size, no winner, no ship recommendation exists to quote. The investigation finds the CDN rule, the run is emitted as invalid with that cause in its payload (AN-052), and a corrected experiment starts under a new ID once the rule is fixed.

Note: corrects AN-046 (SRM is a stop condition enforced by the analysis job; see also BAN-AN-022).
