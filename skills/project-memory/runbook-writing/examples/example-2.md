# Example 2 — Person-only escalation replaced by role escalation and verification

## Before

Runbook: "Checkout errors" — final section:

> If the restart doesn't fix it, call Dave, he knows the payment service.
> Once the service is restarted, close the ticket.

Dave has left the company, "the restart" is the only remedy offered, and the
ticket closes on the restart itself — whether checkout works again is never
checked.

## After

> ## Escalation
>
> If verification (below) still fails 15 minutes after the procedure is
> complete, page the **payments on-call** role via the paging tool
> (service: `checkout-api`, escalation policy: `payments-primary`). State
> the alert name, the step reached, and the verification output. If the
> payments on-call does not acknowledge within 15 minutes, the paging tool
> escalates to the engineering manager role automatically.
>
> ## Verification
>
> 1. Run the checkout smoke check:
>    `./scripts/smoke-checkout.sh`
>    Expected: exit code 0 and the final line `checkout flow OK`.
> 2. Confirm the alert `CheckoutErrorRateHigh` shows as resolved in the
>    alert dashboard.
>
> Only close the incident when both checks pass. If either fails, escalate
> as above — do not repeat the restart more than once.

Escalation routes to a role through a tool that survives staff changes,
with a stated time threshold, and the incident closes on proof that the
user-visible flow works again.

Note: corrects PM-068 — the escalation path names a role, a channel, and a time threshold, never only a person.
