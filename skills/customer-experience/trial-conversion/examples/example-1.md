# Example 1 — Terms and reminder

## Before

The pricing page says "Try Pro free for 14 days." The signup form asks for a card immediately, with a footnote: "Billing applies per our terms." Nothing states when the first charge lands or how much it is. On day 15 the user is charged $15 with no email or in-app notice beforehand — the first they hear of it is the card statement.

## After

The signup screen states: "Free for 14 days. Your card is charged $15 on 4 December 2026, then $15/month. Cancel any time before then and you pay nothing." Three days before the trial ends, the billing platform's trial-will-end event triggers an email and an in-app notice repeating the charge date and amount, with a one-click cancel link.

Violates/corrects CX-101 and CX-105 — terms are stated before signup, and a reminder naming the date and amount always precedes the first charge.
