# Example 3 — The failed card that silently ended the account

## Before

```text
Day 1:  Renewal charge fails — card was replaced by the bank
        last month. No retry is configured.
Day 1:  One email: "Your payment failed." No link, no next step.
Day 3:  Subscription cancelled automatically for non-payment.
Day 9:  User signs in, finds the account gone, data in the
        30-day purge queue. They had never decided to leave.

Churn report for the month: "Churn: 4.1%" — voluntary and
involuntary mixed, so nobody sees a fixable billing problem.
```

A routine card replacement became a lost customer because no retry, card update, or guided fix ran before the account was cancelled — and the blended metric hid it.

## After

```text
Day 1:  Renewal charge fails. Smart retries scheduled across
        the following days; an account-updater check asks the
        card network for the replacement card number.
Day 1:  Dunning email: "Your payment didn't go through. Update
        your card here: [link] — your plan stays active while
        we retry, until July 20."
Day 4:  Network supplies the updated card. Retry succeeds.
        User gets: "Payment recovered — nothing changed."
        (Most sequences end here, invisibly.)

If every retry had failed:
Day 18: Final notice: "We couldn't complete your payment.
        Your plan ends July 20; export your data before then."
Day 20: Cancellation for non-payment takes effect.

Churn log: involuntary · cause=card-replaced · recovered at retry.
Monthly report shows voluntary and involuntary churn separately.
```

## Note

Corrected under CX-149 and CX-150: retries, automatic card updates, and dunning emails with a working payment-update link all run before any cancellation for non-payment, the end date is announced in advance, and involuntary churn is logged apart from voluntary (CX-141).
