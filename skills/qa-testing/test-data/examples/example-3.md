# Example 3 — Labeled synthetic fixture people

## Before

```json
{ "name": "Sarah Mitchell", "email": "sarah.mitchell@gmail.com", "phone": "+1-555-014-2288", "plan": "pro" }
```

The fixture file reads like a real customer export: plausible names paired with real email domains and dialable-looking numbers, no marker distinguishing these records from real users. One address belongs to an actual person, and when the fixtures leak into a demo the "customers" look genuine.

## After

```json
{ "name": "Seed User 014", "email": "seed-user-014@example.com", "phone": "+1-555-0100", "plan": "pro", "is_seed": true }
```

Every fixture person is visibly and mechanically synthetic: invented label-style names, reserved `example.com` addresses, numbers from the reserved fictional range, and an `is_seed` marker that the placeholder-scan sweep (G-QA-123) audits. The data still exercises the same code paths — it just can never be mistaken for a real customer.

Note: corrects QA-246 (synthetic data labeled end to end) and QA-249 (no real personal details in fixtures).
