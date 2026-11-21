# Example 3 — "Optimisation" that deletes the backups

## Before

A cost-cutting proposal lists three savings: turn off automated database backups, drop the second application replica, and disable the external uptime check. The monthly saving is real and the proposal is approved — until the first disk failure, which is now an unrecoverable data loss that nobody can even detect quickly.

## After

The proposal is rejected and rewritten from the waste sweep instead: an idle staging database two sizes too large is rightsized, orphaned snapshots from a finished migration are deleted, and a forgotten preview environment is terminated. The same monthly saving is reached with backups, redundancy, and monitoring untouched, and the review artifact records which category each saving came from.

Note: corrects DO-330 — optimisation never removes backups, monitoring, or redundancy; presenting it as a saving is banned under BAN-DO-163.
