# Example 2 — Advisory Lighthouse step to required gate

## Before

From the CI workflow:

```yaml
- name: Performance check
  run: lhci autorun
  continue-on-error: true
```

The step runs, the assertion fails on an LCP breach, and the pull request merges anyway because the job is advisory. The budget exists on paper and gates nothing.

## After

```yaml
- name: Performance budget gate
  run: lhci autorun
```

The step has no `continue-on-error`, the workflow is a required status check in branch protection, and the Lighthouse CI configuration collects three runs per template and asserts the median:

```json
{
  "ci": {
    "collect": { "numberOfRuns": 3 },
    "assert": {
      "assertions": {
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }]
      }
    }
  }
}
```

A failed assertion now exits non-zero and blocks the merge; the breach exits only by fixing it or by a written waiver.

Note: corrects AN-204 — CI enforcement is a required, build-failing gate, with the median-of-runs rule of AN-205.
