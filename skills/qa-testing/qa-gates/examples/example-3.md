# Example 3 — Re-run until green, replaced by quarantine

## Before

The checkout e2e gate fails roughly one run in four, always at the payment step, and the team's habit is to press re-run until it passes. A PR merges on the fourth attempt under a green "Passed" indicator. Two weeks later a real payment regression ships: it failed the same way the flake did, was re-run three times, and passed once when the fixture happened to take the unaffected path — the retry habit had trained everyone to ignore exactly this failure.

## After

The flaky test enters quarantine as a recorded state: named owner, expiry two weeks out, and a quarantine count that appears in the release report (G-QA-114). While quarantined, the payment step is covered by an integration-layer test that cannot flake the same way, so coverage is reduced honestly rather than cosmetically. The owner traces the flake to a race with the provider sandbox, fixes it before the expiry date, and the test returns to the required-checks list with its seeded-fault history intact.

Note: demonstrates QA-228 — quarantine is a counted, expiring state with an owner, never a re-run habit.
