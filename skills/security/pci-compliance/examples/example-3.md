# Example 3 — Marketing claim: "PCI certified" vs attestation-matched copy

## Before

The pricing page carries a badge copied from the payment provider's site:

```text
🔒 PCI DSS Certified — your payments are 100% legally compliant.
We use a PCI-compliant provider, so our checkout is fully PCI compliant.
```

No attestation has been filed by the merchant, the provider's compliance does not transfer, and PCI DSS is a contractual standard — not a law the business can be "legally compliant" with by association.

## After

The badge is removed until the SAQ A attestation is filed and confirmed by the acquirer; the replacement copy says only what the attestation supports:

```text
Card payments are processed by our payment provider over an encrypted
connection. We never see or store your full card number.
```

If a compliance statement is needed later, it quotes the filed attestation's scope ("merchant has completed SAQ A for e-commerce transactions") and nothing beyond it.

Note: corrects SE-248 and SE-245 — claims match the filed attestation exactly, and PCI DSS is described as a contractual obligation, not a legal certification.
