# Example 3 — "Be more careful" replaced by an owned, dated, tracked action

## Before

## Follow-up actions

| Action | Owner | Due | Tracker |
| --- | --- | --- | --- |
| Be more careful with database migrations | Team | — | — |
| Double-check config changes next time | Everyone | — | — |

## After

## Follow-up actions

| Action | Owner | Due date | Tracking ID |
| --- | --- | --- | --- |
| Add a dry-run mode to the migration script and make it mandatory in the deploy pipeline | Platform lead | 2026-12-05 | OPS-118 |
| Add a validator rule rejecting configs missing the `sync_region` field | Backend lead | 2026-11-28 | OPS-119 |
| Update the migration runbook with the dry-run step and link this postmortem | On-call lead | 2026-11-25 | OPS-120 |

Note: corrects PM-087 / BAN-PM-043 — every action is a concrete change with a named owner, an ISO due date, and a tracking ID; no exhortations.
