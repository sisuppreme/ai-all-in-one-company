# Example 3 — A blameless postmortem with tracked actions

## Before

The incident review concludes: "Root cause: Priya deployed a bad config on Friday." Everyone nods, nothing changes, and the same config path takes the site down again six weeks later — this time deployed by someone else.

## After

The postmortem states the root cause as a system property: "A single hand-edited config value can reach production with no validation, no staged rollout, and no automated rollback." Follow-ups are filed in the work tracker with owners and due dates — config schema validation in CI (owner: platform, due in two weeks), staged rollout for config changes (owner: release, due in four weeks) — and reviewed weekly until closed.

Note: Demonstrates DO-289 and DO-290 — the postmortem blames the system, never a person, and its actions are tracked to completion like features.
