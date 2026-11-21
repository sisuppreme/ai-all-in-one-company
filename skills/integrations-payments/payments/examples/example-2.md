# Example 2 — Replacing a client-priced checkout with a server-computed, idempotent one

## Before

The browser names the price, and the server believes it:

```text
POST /checkout
{ "plan": "pro", "amount": 100, "currency": "usd" }

  → create charge for 100 minor units ($1.00)
  → no idempotency key
```

The Pro plan costs $49, but the endpoint charges whatever the request
body says. A double-click on Pay also creates two charges, because
nothing ties the retry to the first attempt.

## After

The client names the plan; the server computes the price and keys the call:

```text
POST /checkout
{ "plan": "pro" }

  → order = create order(plan "pro", status "pending")        # order #8412
  → catalog lookup: pro → amount 4900 minor units, currency "usd"
  → provider.createCheckout(
      amount: 4900, currency: "usd",
      idempotencyKey: "order-8412-checkout"
    )
```

A tampered request body cannot change the price — there is no amount
field to tamper with. A double-click or a network retry replays the
same idempotency key, and the provider returns the original checkout
instead of creating a second charge.

Note: corrects IN-001 — amount, currency, and line items are computed server-side from the catalog; a client-supplied amount is a defect.
