# Example 2 — Admin order view: full PAN vs brand + last four

## Before

The staff order page renders the customer's full card number and expiry "so support can help with refunds," and a support agent pastes the number into a ticket note:

```text
Order #1042 — Card: 4242 4242 4242 4242, exp 12/28
Ticket note: "Customer confirmed card 4242 4242 4242 4242 is correct."
```

The full PAN now lives in the admin database view and the support ticket system — two more systems dragged into PCI scope.

## After

The order view stores and shows only what the provider returns for display, and refunds run on the provider transaction ID:

```text
Order #1042 — Card: Visa •••• 4242 — Provider txn: pi_3N8example
[Refund] → POST /refunds { transaction_id: "pi_3N8example", amount }
```

Support identifies the payment by order number and last four digits; the full number exists only at the provider.

Note: corrects SE-247 and SE-242 — admin tools sit inside the payment trust boundary and never display or store a full card number.
