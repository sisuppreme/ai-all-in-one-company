# Example 3 — Dead tokens kept forever replaced by provider-feedback pruning

## Before

```js
// Provider errors are ignored entirely. Tokens for uninstalled apps
// stay in the table forever, and every send to them "succeeds"
// from the code's point of view.
async function sendPush(userId, message) {
  const tokens = await db.deviceTokens.listForUser(userId);
  for (const t of tokens) {
    try {
      await messaging.send({ token: t.token, notification: message });
    } catch {
      // ignore — maybe it worked
    }
  }
}
```

## After

```js
// Every send records the provider's response against the delivery;
// an invalid-token response prunes the token immediately.
async function sendPush(delivery, tokenRow, message) {
  try {
    const response = await messaging.send({ token: tokenRow.token, notification: message });
    await db.deliveries.complete(delivery.id, { providerResponse: response });
  } catch (err) {
    await db.deliveries.fail(delivery.id, { providerError: err.code });
    if (err.code === "messaging/registration-token-not-registered") {
      await db.deviceTokens.delete(tokenRow.id); // prune on provider feedback
    }
    throw err; // the queue decides whether the failure is retryable
  }
}
```

Note: the slop version swallowed provider errors and kept dead tokens forever; the corrected version records every outcome and prunes tokens the provider reports as invalid — BE-266, BE-267.
