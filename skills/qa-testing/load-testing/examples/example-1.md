# Example 1 — Averages replaced by percentile thresholds

## Before

The load script declares no thresholds, and the release report summarizes
the run in one line:

> "Load test: 500 users, average response time 180 ms. Fast. ✅"

The average is real but useless: during the same run the checkout journey's
p(99) latency was over 9 seconds and 4% of checkouts failed. The mean hid
both, because fast homepage requests outnumbered slow checkouts fifty to
one. The release shipped on the strength of the average.

## After

Thresholds are written into the script before the run, copied from the
performance budget:

```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<800', 'p(99)<2000'],
    http_req_failed: ['rate<0.01'],
    'http_req_duration{journey:checkout}': ['p(95)<1000'],
  },
};
```

The report now carries the percentile table per journey — p(95), p(99),
and error rate for login, browse, search, and checkout — and k6's exit
code decides the gate. The 4% checkout failure rate fails the run, a
defect is filed with the table attached, and the release waits for the
fix instead of shipping on a reassuring mean.

Note: corrects QA-121 — results are reported and gated on percentiles and error rate, never on averages.
