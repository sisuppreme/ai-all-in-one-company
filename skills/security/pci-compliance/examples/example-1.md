# Example 1 — Checkout form: own form vs provider hosted fields

## Before

The checkout page renders its own card inputs and posts them to the product's server, which forwards them to the payment provider and writes the payload to the request log:

```html
<form action="/api/charge" method="post">
  <input name="card_number" autocomplete="cc-number">
  <input name="card_cvc" autocomplete="cc-csc">
  <button>Pay</button>
</form>
```

The merchant then files SAQ A because "we only store tokens." The PAN crossed the product's page, server, and logs, so the real scope is SAQ D territory and the log store holds live card numbers.

## After

Card entry happens in provider-served hosted fields; the product's server only ever receives a token:

```html
<!-- Card inputs are iframes served from the provider's origin;
     no card value ever enters this page's DOM or the product's API. -->
<div id="provider-card-element"></div>
<script>
  // On submit, the provider's JS exchanges the card for a token client-side.
  // The product posts only { token, amount, currency } to /api/charge.
</script>
```

The integration class is documented as "provider hosted fields — typically SAQ A" and confirmed with the acquirer before launch.

Note: corrects SE-241 and SE-243 — card data never touches the product, and the SAQ mapping follows the actual integration.
