# Example 3 — The receipt with sample totals

Note: the Before violates IN-130 (and is banned by BAN-IN-064); the After corrects IN-130.

## Before

The receipt email template is built with the designer's sample content left in the body: "Pro plan — $49.00, charged to Visa •••• 4242." The send job passes only the customer's name, so every buyer receives the same $49.00 receipt — including the one who paid $19.00 on a different card — and finance cannot reconcile the emails against real charges.

## After

The receipt job loads the provider-confirmed payment record for the order and renders the plan name, amount, currency, and card brand/last digits from that record. The template contains no figures of its own. A test purchase at a second price point produces a receipt matching that charge exactly, and the message row links to the payment it describes.
