# Example 3 — A loosened threshold returned to the budget

## Before

The release run fails: checkout p(95) measures 1,400 ms against a budgeted
threshold of 800 ms, and k6 exits non-zero. Inside the same pull request
that carries the load script, the threshold line is edited:

```diff
-    'http_req_duration{journey:checkout}': ['p(95)<800'],
+    'http_req_duration{journey:checkout}': ['p(95)<2000'],
```

The pipeline goes green and the release ships — on a budget nobody
approved, changed in the one place nobody reviews budgets.

## After

The threshold edit is reverted; the script again carries the budgeted
800 ms, the run fails honestly, and the release is blocked. Two artifacts
come out of the failure:

1. A defect for the checkout regression, with the run's percentile table
   and a query profile attached (QA-131).
2. A separate, reviewed proposal against the performance budget document
   itself, arguing — with the trend data from the release archive — for
   whether 800 ms is still the right number. D12 owns that decision; if
   the budget changes, the script copies the new value in a later change
   that cites the budget revision.

The gate is green only when the system meets the budget, or the budget
is changed in the open — never when the test quietly moves the line.

Note: corrects QA-125 — thresholds come from the budget / SLO documents, and loosening one is a reviewed change to those documents, never an edit inside the test PR.
