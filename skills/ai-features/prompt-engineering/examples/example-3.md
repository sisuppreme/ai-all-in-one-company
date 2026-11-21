# Example 3 — A vibes paragraph rebuilt to anatomy with a contract

## Before

```text
You are a super helpful, friendly assistant for our store. Answer customer
questions nicely and amazingly. Be warm and delightful!
```

Replies vary in length and structure from call to call, sometimes invent a
delivery timeframe, and the returns flow cannot parse anything from them.
There is no stated format to fix, so every complaint becomes a fresh round of
wording tweaks.

## After

`prompts/support-answers.md`, version 2.0.0:

```text
Header: feature support-answers; inputs: question (string), order (object,
may be absent); output: support-answer schema (fields: answer, action,
reference).

Task: Answer the customer's question about their order using only the order
data provided.

Steps:
1. Identify what the question asks: delivery status, return, or other.
2. Answer from the order data. State dates exactly as given.
3. If the order data does not contain the answer, say so and name what the
   customer can do next. Never estimate a delivery date.

Output: JSON matching the support-answer schema. The answer field is at most
60 words, plain language, no greeting or sign-off.

Failure behavior: if no order data is provided and the question needs it,
return the abstention response asking the customer for their order number.
```

The returns flow now consumes a stable schema, delivery dates are quoted or
the feature abstains, and wording changes are evaluated against the golden
set before release.

Note: corrects AI-023 and AI-025 — every prompt carries the fixed anatomy, and the output format is stated explicitly, never implied.
