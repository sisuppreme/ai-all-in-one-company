# Example 2 — The billing flow nobody could see

## Before

```text
Behavior record (excerpt)
Flow: Members' area — update billing details
Status: RECORDED FROM SOURCE
Spec: Card form validates number format inline; saving shows a
      prorated charge preview, then confirms by email.
```

The operator held no members' account and never saw this flow. The spec was assembled from a competitor's billing page and the client's verbal description, then filed as observed behavior — invented functionality presented as evidence.

## After

```text
Behavior record (excerpt)
Flow: Members' area — update billing details
Status: UNOBSERVED
Reason: flow sits behind a member login; the client has not
        provisioned a test account (requested 2026-11-21).
Handoff: passes to page-reconstruction labeled `unobserved`;
        no parity claim may be made for this flow.
```

## Note

Violates CL-085 (interactions the operator cannot legitimately observe are recorded as `unobserved` with the reason, never invented); corrected by replacing the fabricated spec with an honest unobserved record and a labeled handoff.
