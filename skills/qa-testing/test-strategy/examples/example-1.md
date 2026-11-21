# Example 1 — Mapping acceptance criteria to layers

## Before

TESTING.md says: "We test thoroughly at all levels." The acceptance criteria require that a declined card shows an error and charges nothing, but no layer owns payment failure: the e2e suite covers only the happy-path checkout, and the gap surfaces only when a user reports a false "Payment successful."

## After

TESTING.md carries a mapping table: "Payments — approval path: e2e-testing (provider test mode); decline path: e2e-testing (documented decline card must decline visibly); persistence of the order record: integration-testing (read-back through a second endpoint)." Every acceptance class names its layer before the release audit runs.

Note: demonstrates QA-203 — every acceptance class maps to a layer that can catch its failure.
