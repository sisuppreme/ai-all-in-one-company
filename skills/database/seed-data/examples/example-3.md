# Example 3 — Synthetic, labeled sample users

## Before

```sql
-- Real-looking people, real domains, no label: indistinguishable from customers.
INSERT INTO users (email, full_name) VALUES
  ('sarah.khan@gmail.com', 'Sarah Khan'),
  ('j.miller@outlook.com', 'James Miller');
-- A staging password-reset test emails a real person's inbox.
```

## After

```sql
-- Visibly synthetic (reserved domains, placeholder names) and labeled in the data:
INSERT INTO users (email, full_name, is_seeded) VALUES
  ('sample-user-001@example.test', 'Sample User 001', true),
  ('sample-user-002@example.test', 'Sample User 002', true)
ON CONFLICT (email) DO NOTHING;
```

Corrects DB-064 (sample data is synthetic and visibly synthetic) and DB-065 (sample records are labeled in the data so they can never be mistaken for real users).
