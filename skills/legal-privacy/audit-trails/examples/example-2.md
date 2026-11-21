# Example 2 — The entry that got "fixed"

## Before

An auditor asks why an admin exported a customer list. The entry exists but names the wrong admin, so a developer quietly runs `UPDATE audit_trail SET actor = 'admin-EXAMPLE-02'` to make the record match what "must have happened." The hash chain is not checked, nobody notices, and the trail now certifies a version of events nobody witnessed.

## After

The original entry stays exactly as written. A correction entry is appended: it references the original entry's ID, states "actor recorded as admin-EXAMPLE-01 in error; export was performed by admin-EXAMPLE-02, confirmed against the IdP session log REF-EXAMPLE-9," and carries the corrector's own actor and timestamp. The application role has no UPDATE grant on the trail store, and the scheduled integrity job verifies the chain end to end.

*Demonstrates LG-164 and LG-165 — entries are never edited in place; corrections are new entries, and the store is tamper-evident.*
