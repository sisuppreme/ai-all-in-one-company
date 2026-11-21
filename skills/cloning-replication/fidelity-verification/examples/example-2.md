# Example 2 — Regenerated baseline vs. reason-recorded change

## Before

The home page comparison fails at 91% after the rebuild's header is restyled. To unblock the release, the verifier re-screenshots the baseline from the rebuild itself; the suite now passes at 100% and the failure leaves no trace anywhere.

## After

The 91% result is logged as a defect. Review shows the header restyle was an approved design change, so the deviation log records the change, its approval, and the approver. The source baseline itself stays frozen — the accepted deviation record carries the difference, so the comparison continues to report the known, approved gap rather than being regenerated to green. Baselines are regenerated only when the frozen source capture set itself is re-frozen, and the baseline-change audit (G-CL-062) matches any new baseline file to its reason record.

Note: corrects CL-129 / BAN-CL-062 — baselines change only with a recorded reason tied to an approved change; silent regeneration is a falsified result.
