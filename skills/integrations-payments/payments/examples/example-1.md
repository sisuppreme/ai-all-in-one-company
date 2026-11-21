# Example 1 — Replacing the success-page grant with a webhook grant

## Before

The checkout success handler grants access directly:

```text
GET /checkout/success?session=cs_123
  → order.status = "paid"
  → user.plan = "pro"
  → render "Welcome to Pro"
```

Anyone who visits or guesses the success URL is upgraded without paying.
A customer who pays and closes the tab before the redirect lands never
gets access, because the redirect was the only place the grant existed.
No provider payment ID is stored, so support cannot verify the purchase.

## After

The redirect only displays state; the verified webhook grants:

```text
GET /checkout/success?session=cs_123
  → read order by session ID
  → render "Payment processing — access appears here once confirmed"

POST /webhooks/payment-provider   (signature verified, event deduplicated)
  → event: payment_succeeded, payment ID pi_456, amount 4900, currency usd
  → reconcile against order: account, amount, currency, state all match
  → order.status = "paid", order.provider_payment_id = "pi_456"
  → user.plan = "pro"
```

The customer who closed the tab is granted by the same webhook. The
visitor who guesses the URL sees a processing page and nothing else.

Note: corrects IN-005 — entitlement comes from the verified webhook or a server-side re-read of the payment object, never from the success redirect.
