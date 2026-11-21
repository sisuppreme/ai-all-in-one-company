# Example 1 — The label that had to fail

## Before

The CI axe suite has been green for three releases. To "test the tests," a developer removes the `<label>` from the email field on a throwaway branch and runs the suite — it still passes, because the scan config only visits the home page and the signup page was never added to the coverage list. The green result was certifying pages nobody scanned.

## After

The seeded-fault control (G-QA-052) is part of the release process: the same label removal now makes `npm run test:a11y` exit non-zero with the axe `label` violation reported, because the signup page and its form states are on the named coverage list. The branch is discarded, and the suite's green result means something again.

Note: demonstrates QA-103 — a suite that cannot fail on a seeded fault is broken, and its passes count for nothing.
