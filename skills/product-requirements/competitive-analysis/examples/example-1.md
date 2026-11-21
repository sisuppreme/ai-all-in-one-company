# Example 1 — The landing-page feature matrix

## Before

```markdown
| Capability | Us | RivalBoard | TaskPilot |
|---|---|---|---|
| AI reports | ✗ | ✓ | ✓ |
| Time tracking | ✓ | ✓ | ✗ |
| Guest access | ✓ | ✗ | ✓ |

Source: competitor homepages, checked "recently."
```

RivalBoard's "AI reports ✓" came from a screenshot on its landing page. Nobody opened a RivalBoard account; the trial tier has no report generator at all — the screenshot shows a mockup of a roadmap feature.

## After

```markdown
| Capability | Us | RivalBoard | TaskPilot |
|---|---|---|---|
| AI reports | ✗ (not built) | Claimed, unverified — landing page shows a report mockup; trial account (2026-11-10) has no report feature | ✓ — generated a summary report from a 12-task board, trial account, 2026-11-10 |
| Time tracking | ✓ — timer on task card, verified in our build 2.4 | ✓ — started/stopped timer on a test task, trial account, 2026-11-10 | ✗ — no timer found in trial account, 2026-11-11 |
| Guest access | ✓ | ✗ — invite flow requires a paid seat, trial checkout, 2026-11-10 | ✓ — guest joined via link, trial account, 2026-11-11 |

Evidence: trial notes + screenshots in research/competitive-2026-11/ (one file per cell).
Refresh date: 2027-02-10.
```

## Note

Corrected under PR-162 and PR-164: capabilities are verified by running the same tasks hands-on, and anything known only from a marketing page is recorded as "claimed, unverified" — never as a matrix fact.
