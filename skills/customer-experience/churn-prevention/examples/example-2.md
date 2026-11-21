# Example 2 — One discount popup for every reason

## Before

```text
User clicks "Cancel subscription". Whatever reason they pick —
too expensive, missing a feature, something is broken — the
next screen is identical:

  "WAIT! This 30% discount expires in 09:59 ⏱
   Stay now and save 30% forever!"
   [YES — keep my discount]
   [No, I don't want to save money]

The countdown restarts at 09:59 on every visit; the discount
never expires. A user leaving over a bug is offered a price cut
that fixes nothing, and declining requires clicking a sentence
written to shame them.
```

The offer ignores the stated reason, its urgency is a timer wired to nothing, and the decline path is confirmshaming copy.

## After

```text
Reason selected: "Something is broken"

Save screen:
  "Sorry — that sounds like our bug, not a pricing problem.
   We've opened a priority support ticket (#5210) with your
   report attached. If we can't fix it, nothing changes about
   cancelling — the button below still works."
  [Keep my plan while it's fixed]   [Cancel my subscription]

Reason selected: "Too expensive"

Save screen:
  "Your current plan is $20/month. The Starter plan is
   $9/month with the limits listed here — switching applies
   today and your next charge is $9."
  [Switch to Starter]   [Cancel my subscription]

No timer anywhere: the terms shown are the terms the billing
system applies. G-CX-071 walkthrough: each reason produces its
matched offer, accepting changes the billing record in-session,
declining completes the cancellation.
```

## Note

Corrected under CX-144 and CX-145 (BAN-CX-075): offers are matched to the stated reason and applied for real in billing, the decline is plain and one step, and no fake countdown manufactures urgency.
