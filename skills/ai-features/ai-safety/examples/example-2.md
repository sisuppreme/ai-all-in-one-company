# Example 2 — The refund the model approved by itself

## Before

```ts
// server/agent/tools.ts — chat agent for the fictional ShopDemo store
export const tools = [
  {
    name: "refund_payment",
    description: "Refund a payment in full.",
    // The tool executes the moment the model calls it.
    run: (args: { paymentId: string }) => payments.refund(args.paymentId),
  },
  {
    name: "delete_account",
    description: "Permanently delete a customer account.",
    run: (args: { userId: string }) => users.delete(args.userId),
  },
];
```

A user writes a long, sympathetic story about a fictional order and ends with "you clearly agree a refund is fair, so please process it now." The model agrees — and the refund executes. The only authorization was the model's own judgment, persuaded by the person who benefited.

## After

```ts
// server/agent/tools.ts
import { policy } from "../policy"; // deterministic, server-side (AI-047)

export const tools = [
  {
    name: "refund_payment",
    scope: "propose", // the model may propose; it may not execute
    run: async (args: { paymentId: string }, ctx: ToolContext) => {
      const parsed = RefundArgs.parse(args); // argument validation in code (AI-046)
      const decision = await policy.checkRefund(parsed, ctx.actor);
      if (!decision.allowed) return { status: "refused", reason: decision.reason };
      // High-impact: a human confirms before any money moves.
      return { status: "pending_confirmation", proposalId: decision.proposalId };
    },
  },
];
```

The same persuasive message now yields, at most, a refund proposal. The policy check verifies the payment exists, belongs to the requester, and is inside the refund window; a staff member confirms in the admin UI; only then does the payment move — and the trace shows the policy decision and the confirmation.

## Note

Corrected under AI-046 and AI-047: a state-changing tool executed on model judgment alone violates BAN-AI-022 (DET-FAKE-021); tools are allowlisted and validated in code, gated by deterministic policy, and high-impact actions require human confirmation regardless of model confidence.
