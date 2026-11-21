# Example 3 — The alert muted since March

## Before

```yaml
# silence: DiskAlmostFull on db-01
# created: March 3 — "flapping, mute until we get to it"
# expires: never
```

The disk fills during a November launch. Nothing pages: the alert still exists on paper, so the team believed the disk was covered.

## After

```yaml
# silence: DiskAlmostFull on db-01
# reason: "Flaps during nightly backup window 02:00-02:20; threshold fix in task OPS-412"
# expires: March 17 (14 days)
# Review outcome (AN-130 cadence): alert re-thresholded and demoted —
#   page  -> disk predicted full within 4h at current growth rate
#   ticket -> disk above 85% outside the backup window
# The raw "disk > 90%" rule is deleted; the G-AN-064 inventory audit
# lists any silence past expiry as a defect until this state is reached.
```

Note: corrects AN-129 — the indefinite mute becomes a time-boxed, reasoned silence with a linked fix, and the review replaces the noisy rule with symptom-based tiers instead of restoring it unchanged.
