# Example 1 — The delete that only hid

## Before

```sql
-- "Delete my account" handler
UPDATE users SET visible = false, deleted_at = now() WHERE id = $1;
-- UI then shows: "Your account has been deleted."
```

The profile disappears from the app, but the row, the user's posts in the search index, and their events in the analytics store are all still there and still queryable from the admin panel.

## After

```text
Erasure job for subject #4821 (request DSAR-2026-0117):
1. DELETE FROM users, posts, messages WHERE subject = 4821        (primary store)
2. Remove subject 4821 documents from search index                (verified: 0 hits)
3. Purge subject 4821 events from analytics store                 (verified: 0 rows)
4. Send deletion instruction to processors: email provider, file storage
   → confirmations filed with request DSAR-2026-0117
5. Add subject 4821 to backup-suppression list (deleted on rotation,
   per retention schedule in project file)
6. Residue query across DB, index, analytics, admin views: 0 records
```

## Note

Corrected under LG-050: erasure executes across every store and is proven by a zero-result residue query (G-LG-021); a visibility flag is a hide, not an erasure (BAN-LG-021, DET-FAKE-011).
