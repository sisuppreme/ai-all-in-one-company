# Example 1 — A hard-coded prompt fork, merged into one canonical file

## Before

The invoice-explainer prompt exists in three places:

- A string literal in the billing service: "Explain this invoice in plain
  language. Mention the refund window of 14 days."
- A copy in the support console dashboard, edited last month by hand:
  "…Mention the refund window of 30 days."
- A third variant in the mobile app's fallback code, with no refund mention
  at all.

Customers asking the same question get different answers depending on which
surface they used. Nobody knows which copy is current, and the last wording
fix was applied to only one of the three.

## After

1. One canonical file, `prompts/invoice-explainer.md`, version 1.3.0, with a
   contract header (owner feature: billing-explainer; inputs: `invoice`
   object; output: the plain-language explanation schema).
2. The refund window is read from the project's fact sheet — 14 days — and
   stated once, in that file.
3. The billing service, the support console, and the mobile fallback all load
   the canonical file through the integration layer; the dashboard copy and
   the app string are deleted.
4. The canonical-copy scan (G-AI-012) now runs in CI so a fourth copy fails
   the build instead of drifting quietly.

Note: corrects AI-021 and AI-022 — prompts are versioned files, and each prompt has exactly one canonical copy.
