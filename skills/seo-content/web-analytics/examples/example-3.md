# Example 3 — Three names for one signup

## Before

Over two releases, three developers instrument the same signup action three
ways: `sign_up` from the plan, plus `signup` and `SignUp` added on the fly.
GA4 now shows three conversion rows, each holding roughly a third of the
real total. The monthly review picks the largest row as "the signup number",
understates conversions by two-thirds, and nearly kills a landing page that
was actually performing.

## After

The change is proposed into the shared tracking plan instead of shipped
directly: `sign_up` is confirmed as the single canonical name (D12 owns the
taxonomy), the two variants are removed, and the G-CO-121 plan diff confirms
no live event is missing from the plan. A debug session validates the fix
before release — one signup, one event, one row. The review re-reads the
corrected total and the landing page keeps its place, now on evidence.

Note: corrects CO-250 — event changes go through the shared tracking plan under one canonical name; variant spellings fragment reports and fail BAN-CO-124 (DET-CON-017).
