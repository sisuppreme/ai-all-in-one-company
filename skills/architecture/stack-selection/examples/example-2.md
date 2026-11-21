# Example 2 — Repairing version drift between README, ADR, and manifest

## Before

The README stack list says "PostgreSQL 16", ADR-0004 says PostgreSQL 15, and the deployment manifest pins `postgres:14`. A developer hits a behavior difference, checks the README, and debugs against the wrong version for an afternoon.

## After

The manifest is treated as the single source of truth: it is deliberately upgraded to `postgres:16` (the version the team intends to run), the README stack list is corrected to 16, and ADR-0004 gains a dated amendment note pointing at the manifest as authoritative for versions. The version-agreement gate (G-AR-022) is added to CI so the three can never drift again without failing the build.

## Note

Corrects AR-045 (versions named in prose must match the dependency manifest exactly; a mismatch is a defect).
