# Example 2 — The failing questions that disappeared

## Before

```text
Eval run, Monday:  overall 81% (floor 85%) — release blocked.
Failed items: #041 refund-after-30-days, #087 duplicate-charge, #112 partial-refund

Git history, Tuesday (single commit, message: "dataset cleanup"):
- #041 deleted
- #087 deleted
- #112 rubric changed from "must cite the refund policy clause" to "mentions refunds"

Eval run, Tuesday: overall 88% — release approved.
```

Nothing about the prompt, model, or retrieval stack changed. The pass rate rose because the test got easier: two failing items were removed and one rubric was loosened, with no correctness reason recorded anywhere.

## After

```text
Eval run, Monday:  overall 81% (floor 85%) — release blocked.
Failed items: #041 refund-after-30-days, #087 duplicate-charge, #112 partial-refund

Change record for the fix:
- Prompt v2.3: added the refund-policy clause to retrieved context and a sequential
  instruction to cite it (prompt-engineering change, reviewed diff).
- Dataset change, reviewed separately: #112's reference corrected — it named a
  superseded policy clause; reason recorded in the diff. #041 and #087 unchanged.

Eval run, Wednesday (dataset v1.5, prompt v2.3): overall 89%, billing category
84% → 93%, no category regressed. Delta recorded in the change record (G-AI-074).
```

The stack improved and the score followed. The one dataset edit is a reviewed, versioned diff whose reason — a wrong reference answer — is stated openly, so the before/after numbers remain comparable and honest.

## Note

Violates AI-146 (BAN-AI-072): editing the golden set to rescue a failing run makes the metric a fixture that no longer measures the system. Corrected by fixing the prompt and retrieval instead, and keeping dataset changes reviewed, versioned, and reasoned.
