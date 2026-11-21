# Example 2 — Three "click here"s, three destinations

## Before

A features page closes three sections like this:

- "To see what it costs, click here." → `/pricing`
- "For setup instructions, click here." → `/docs/setup`
- "To read the customer story, click here." → `/customers/acme`

Read out of context — in a link list, a screen reader's links menu, or a crawler's anchor index — all three anchors are identical and say nothing about where they go.

## After

- "See [pricing plans and per-seat costs](/pricing)."
- "Follow the [setup guide for your first workspace](/docs/setup)."
- "Read [how Acme cut onboarding time](/customers/acme)."

Each anchor now names its destination's topic and works as a micro-description wherever it is extracted.

Note: violates CO-204 (anchor text describes the destination); corrected by rewriting each anchor as the destination's topic.
