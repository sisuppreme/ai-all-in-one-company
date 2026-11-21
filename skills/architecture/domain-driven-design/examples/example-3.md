# Example 3 — The oversold seat, fixed at the aggregate

## Before

Booking flow: the API reads `seats_remaining` (1), checks "enough seats,"
then writes the booking in a second statement. Two requests arriving
together both read 1, both pass the check, and the last seat is sold twice.
The invariant "never oversell" exists in a wiki page, not in the code.

## After

Seat inventory for an event is one aggregate. The booking operation is a
single atomic step on that aggregate:

```sql
UPDATE seat_inventory
SET seats_remaining = seats_remaining - 1
WHERE event_id = $1 AND seats_remaining >= 1
RETURNING seats_remaining;
-- zero rows returned = sold out; reject the booking
```

Check and decrement are the same statement, so the invariant holds under
concurrency by construction, and the aggregate is the named enforcer the
invariant trace (G-AR-113) can point to.

Note: corrects AR-224 and AR-231 — aggregates follow invariants, and each invariant is enforced by one aggregate in a single transaction.
