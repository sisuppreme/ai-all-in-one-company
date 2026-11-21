# Example 1 — The looping bot given an exit

## Before

The widget opens with a decision tree copied from a tutorial:

- User: "My export is empty."
- Bot: "Have you tried our help center? [Yes] [No]"
- User clicks No.
- Bot: "Here are popular topics: Billing · Account · Getting started."
- User: "None of these. I need a person."
- Bot: "Have you tried our help center? [Yes] [No]"

There is no human handoff, no ticket is created, and nobody owns the inbox
behind the widget. The conversation is a loop with a chat bubble on it.

## After

Automation is cut back to what it can honestly do:

1. First message gets an immediate automated acknowledgment, labeled as
   automated, stating the configured expected reply time.
2. The bot may suggest one help-center article matched to the message.
3. Every bot message carries a visible "Talk to the team" action; choosing
   it — or sending a second message the bot cannot match — converts the
   conversation to a ticket with the full transcript attached.
4. The inbox has a named owner who reviews it on a stated daily cadence.

The user who needs a person reaches one in one click, and the user who
does not still gets the article.

Note: corrects CX-025 — every automated flow ends in a human handoff, a ticket, or a help-center article.
