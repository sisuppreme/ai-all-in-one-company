# Example 2 — Memory timeline replaced by a log-sourced timeline

## Before

## Timeline

- ~14:00 — Errors started appearing.
- 14:05 — The team noticed the errors and began investigating.
- 14:20 — Rollback started.
- 14:40 — Service recovered.

(Written the following morning from the responders' recollection.)

## After

## Timeline

- 13:47 — Error-rate alert fired for the checkout service (alert log #A-2214).
- 13:52 — On-call acknowledged the alert (pager log).
- 14:09 — Deploy of release 1.8.2 identified as the last change before the error window (deploy log).
- 14:31 — Rollback to release 1.8.1 initiated (deploy log).
- 14:38 — Error rate returned below threshold (monitoring, incident window closed 14:38).

Note: corrects PM-084 / BAN-PM-042 — every entry carries a timestamp from a named record; the detection gap (13:47–13:52) is visible instead of smoothed over.
