# Example 3 — Replacing a homegrown card form with provider elements

## Before

The checkout page ships its own card inputs:

```html
<form id="pay-form">
  <input name="card_number" placeholder="Card number">
  <input name="card_expiry" placeholder="MM / YY">
  <input name="card_cvc" placeholder="CVC">
  <button>Pay $49</button>
</form>
```

On submit, the page checks that the number is 16 digits, posts the card
fields to the project's own server, and marks the order paid. Raw card
data transits and rests on project infrastructure, an expired card
"pays" exactly like a real one, and no provider is ever contacted — the
checkout confirms an order while charging nothing.

## After

The provider's JS element collects the card; the project's server only
ever sees IDs:

```html
<!-- Provider JS loaded from the provider's own origin -->
<div id="payment-element"></div>   <!-- card fields render inside the provider's iframe -->
<button id="pay">Pay $49</button>
```

```text
Browser → card data goes directly to the provider; the page receives
          only the payment intent ID.
Server  → creates the PaymentIntent (server-computed amount,
          order-derived idempotency key) and reads the outcome from
          the verified webhook.
Logs    → contain order IDs and provider payment IDs, never card data.
```

Card data never touches the project's servers (SAQ A posture), and the
provider's response — approval or decline — decides the order state.

Note: corrects IN-004 — card data never transits or rests on project infrastructure; hosted checkout or provider elements only.
