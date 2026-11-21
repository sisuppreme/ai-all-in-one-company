# Example 3 — A written exclusion with an accepted risk

## Before

The project has no chaos testing and no load testing, and TESTING.md never mentions either. At the first traffic spike the team discovers — live — that nobody ever decided whether that proof was needed, skipped, or forgotten.

## After

TESTING.md's Accepted Risks section reads: "Chaos testing: not run for this release. Reason: single-instance deployment has no redundancy to fail over to, so the experiment cannot pass until the scaling work lands. Accepted by: project lead, 2026-11-21. Revisit: when a second instance is deployed." The gap is a recorded decision with an owner and a revisit trigger.

Note: demonstrates QA-204 — exclusions are written, with a reason and a named acceptor.
