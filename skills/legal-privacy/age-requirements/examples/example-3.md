# Example 3 — The under-age account support found

## Before

A parent emails support: "My daughter is 11 and has an account with your app — please remove it." The account is two years old and active. Support replies:

```text
Thanks for letting us know! Unfortunately we can't verify users' ages
after signup, so we're unable to take action on the account.
```

The terms of service bar under-13s; the account stays live, keeps collecting data, and the exchange is not logged anywhere. The product now has actual knowledge of an under-age user and a written record of deciding to do nothing.

## After

The report enters the actual-knowledge path defined for the product:

```text
1. Ticket flagged "age report" → account suspended the same day
   (login and posting disabled; data preserved pending step 2).
2. The parent is offered the two regime outcomes in writing:
   verifiable parental consent through the accepted method, or deletion.
3. No consent within the configured window → deletion executes across
   the database, search index, analytics, and processors.
4. A residue query for the account returns nothing in any store or
   admin view; the ticket, the suspension, and the deletion are
   recorded in the audit trail with timestamps.
```

## Note

Corrected under LG-148 and LG-150: actual knowledge of an under-age user triggers the same flow as a fresh under-threshold signup — consent or removal, executed and verified — and time already spent on the platform grandfathers nothing.
