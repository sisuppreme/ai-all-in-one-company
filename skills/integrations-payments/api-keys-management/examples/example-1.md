# Example 1 — Moving a secret key out of the client bundle

## Before

The browser calls the payment provider directly with the account's secret key:

```js
// shipped to every visitor's browser in the app bundle
const provider = new ProviderClient("sk_live_EXAMPLE");
const charge = await provider.charges.create({ amount: 4900, currency: "usd" });
```

Anyone who opens the page source or the network tab owns a full-access
credential: they can issue refunds, read customer records, and create
charges against the account until someone notices.

## After

The secret key never leaves the server; the client holds only the
publishable key and a per-session intent the server minted:

```js
// browser: publishable key only — public by design, domain-restricted
const provider = new ProviderClient("pk_live_EXAMPLE");
const elements = provider.elements({ clientSecret: intentFromServer });
```

```text
POST /checkout            (server-side, secret key from the secret store)
  → create the payment intent with the server-computed amount
  → return only the intent's client secret to the browser
```

The bundle scan in CI (G-IN-101) now finds no secret material, and a
leaked copy of the frontend contains nothing worth stealing.

Note: corrects IN-202 — secret keys are used server-side only; the client receives publishable keys or short-lived scoped tokens minted per session.
