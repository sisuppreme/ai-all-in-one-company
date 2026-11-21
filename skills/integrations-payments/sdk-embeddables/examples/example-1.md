# Example 1 — Replacing a lookalike card form with the provider's real element

## Before

The checkout "integrates" the payment provider by imitating its element
with house-built inputs and loading a copy of the provider's JS from the
project's own static folder:

```html
<script src="/static/vendor/provider-pay.min.js"></script>  <!-- self-hosted copy -->
<form id="pay-form">
  <input name="card_number" placeholder="Card number">
  <input name="card_expiry" placeholder="MM / YY">
  <input name="card_cvc" placeholder="CVC">
  <button>Pay $49</button>
</form>
```

On submit, the page checks the number is 16 digits, posts the card
fields to the project's own server, and shows "Payment complete." The
self-hosted script is a stale snapshot, raw card data transits project
infrastructure, and any card-shaped input "pays" — no live provider
validates or decides anything.

## After

The provider's JS loads from the provider's origin and renders its own
element; the page handles only IDs and server-confirmed state:

```html
<!-- Provider JS loaded from the provider's own origin, per its docs -->
<div id="payment-element"></div>   <!-- card fields render inside the provider's iframe -->
<button id="pay">Pay $49</button>
```

```text
Browser → card data goes directly to the provider; the page receives
          only the payment intent ID.
Widget  → on the element's callback, shows "Processing…" — never
          "Payment complete."
Server  → confirms the outcome from the verified webhook and only
          then does the page render success.
```

Card data never touches the project's servers, the provider's current
JS validates and declines for real, and success on screen means success
at the provider.

Note: corrects IN-221 — provider JS loads from the provider's origin per its instructions; card data flows browser → provider directly, never through a self-hosted copy or house-built inputs.
