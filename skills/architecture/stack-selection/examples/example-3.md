# Example 3 — Replacing a settled component with a superseding ADR

## Before

The project's queue library, chosen in ADR-0006, stops being maintained. A developer swaps in a different library by editing the dependency manifest and the worker code. No record explains why; six months later a reviewer finds ADR-0006 still marked "accepted" describing a library the project no longer uses.

## After

ADR-0011 is written: context (ADR-0006's library is unmaintained, with the last-release evidence), considered options (the two maintained candidates, scored on the original criteria), decision outcome (the replacement), and consequences. ADR-0011's status is "accepted"; ADR-0006's status is updated to "superseded by ADR-0011" in the same commit as the manifest change.

## Note

Corrects AR-050 (replacing a settled component requires a new ADR that supersedes the old one; silent swaps are forbidden).
