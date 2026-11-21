# in-app-chat

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Intercom, Messenger installation (server-signed identity) — https://developers.intercom.com/installing-intercom/web/installation ; Intercom, "Set your default office hours" — https://www.intercom.com/help/en/articles/732390-set-your-default-office-hours ; Intercom, "Share your expected response time" — https://www.intercom.com/help/en/articles/732436-share-your-expected-response-time
- **Depends on:** support-ticketing, help-center
- **Feeds into:** support-ticketing, feedback-loops

## When to use / Do NOT use

- **Use when:** a chat or messenger widget is installed, configured, or audited on any page — before it goes live, and on every change to hours, automation, or identity handling.
- **Do NOT use when:** the channel is email or a web form with no conversational widget (support-ticketing covers those), or the surface is a marketing chatbot demo that never claims to reach support — label that a demo and keep it off support pages.

## Rules

1. **CX-021 — Server-verified identity.** For logged-in users the widget boots with a server-signed identity token; a client-supplied user ID alone is never trusted, and a forged or tampered token is rejected.
2. **CX-022 — Every conversation lands somewhere real.** Each conversation is created in the operator's staffed inbox or ticket queue with requester identity attached. A widget whose messages create no record does not ship.
3. **CX-023 — Hours configured before launch.** Office hours and expected reply time are set in the tool from the operator's real availability before the widget goes live. The vendor's 24/7 default is never shipped unexamined.
4. **CX-024 — Honest offline state.** Outside configured hours the widget states when the team returns, shows the expected reply time, and captures the message as a ticket with a reference the user can quote.
5. **CX-025 — No automation without an exit.** Every automated flow ends in exactly one of: human handoff, ticket creation, or a help-center article. A flow that can loop or dead-end is removed until it has an exit.
6. **CX-026 — Automation identifies itself.** Bot and automated messages are labeled as automated. No bot uses a human name, photo, or first-person persona that implies a person is typing.
7. **CX-027 — Copy matches staffing.** The widget and site say "message us" unless a human is staffed live in those hours; "live chat" and reply-time claims appear only where the configuration and staffing back them.
8. **CX-028 — Named owner, stated cadence.** The inbox has a named owner and a written review cadence before launch. An unmonitored inbox is a launch blocker, not a backlog item.
9. **CX-029 — History persists.** A user's conversations stay attached to their account and visible to them across sessions and devices; signing out and back in never empties the thread.
10. **CX-030 — Delivered means acknowledged.** A message shows as sent only after the server acknowledges it; a failed send shows an error and a retry or ticket path, never a silent success.
11. **CX-031 — Immediate acknowledgment.** On first message the user gets an automatic acknowledgment confirming capture and stating the expected reply time from the configuration — not a time invented in copy.
12. **CX-032 — Escalation keeps context.** Converting a conversation to a ticket or handing it to a human carries the full transcript and identity with it; the user never re-types what they already wrote.

## BAN list

- **BAN-CX-011 — The looping tutorial bot.** Banned: a canned bot script that cycles generic replies, never reaches a human, and collects messages nobody monitors. Defeats: DET-FAKE-009. Bad: the widget answers every question with "Have you tried our help center?" in a loop, and the inbox behind it has no owner. Instead: automation handles acknowledgment and article suggestions only, and every flow exits to a human, a ticket, or an article (CX-025). Severity: BLOCK.
- **BAN-CX-012 — The unstaffed "live chat".** Banned: labeling the widget "live chat" or showing an "online / replies in minutes" presence when no human is staffed in those hours. Defeats: DET-FAKE-018. Bad: the site promises live replies at 2 a.m. from a one-person team that configured nothing. Instead: configure real hours, say "message us," and let the tool display the true expected reply time (CX-023, CX-027). Severity: BLOCK.
- **BAN-CX-013 — Messages into the void.** Banned: a widget that accepts and displays messages that persist nowhere and notify nobody. Defeats: DET-FAKE-015. Bad: the demo widget renders the user's message in the thread, fires no request, and the "conversation" is gone on reload. Instead: wire the widget to the inbox or ticket queue and show "sent" only on server acknowledgment (CX-022, CX-030). Severity: BLOCK.
- **BAN-CX-014 — The bot in human clothing.** Banned: automation presented as a named human agent — human name, headshot, "typing…" performance — with no disclosure that it is automated. Defeats: DET-FAKE-009. Bad: "Hi, I'm Sarah from support!" is a decision tree, and Sarah does not exist. Instead: label the automation as a bot or assistant and offer the human path from the first message (CX-026). Severity: BLOCK.
- **BAN-CX-015 — Client-trusted identity.** Banned: attaching conversations to an account using a user ID supplied by the browser with no server verification. Defeats: DET-FAKE-021. Bad: changing a `user_id` value in the widget snippet opens another customer's conversation history. Instead: boot the widget with a server-signed token and reject forged tokens (CX-021). Severity: BLOCK.

## Gates

- **G-CX-011 — Two-state delivery test.** Verifies: CX-022, CX-029, CX-030. Check: automated — using the messenger's test mode, send a unique-marker message from the widget logged in and logged out; assert both conversations appear in the team inbox with the correct identity, reply from the inbox, and assert the reply renders in the widget and the thread survives sign-out and sign-in; include one attachment sent from the widget and one attachment sent from the inbox, and assert each attachment is visible and openable on the receiving side. Pass: both directions delivered in both states, attachments delivered each way, history intact. Fail: block launch. Recorded in: progress.md.
- **G-CX-012 — Forged-identity test.** Verifies: CX-021. Check: automated — boot the widget with a tampered identity token and with a raw client-supplied user ID for a second test account; assert both are rejected and no conversation is created or exposed. Pass: zero conversations created under a forged identity. Fail: block launch. Recorded in: progress.md.
- **G-CX-013 — Offline-path test.** Verifies: CX-023, CX-024, CX-027. Check: automated — set the tool clock outside configured office hours, open the widget, and send a message; assert the widget states the team's return time, shows no "live" or "online" wording, and a ticket with a quotable reference exists in the queue. Pass: all three conditions true. Fail: block launch. Recorded in: progress.md.
- **G-CX-014 — Config-vs-copy audit.** Verifies: CX-023, CX-027, CX-031. Check: scripted diff — extract every availability and reply-time claim from the widget and site support copy and compare against the tool's configured office-hours and expected-reply-time values; assert the configuration is non-default. Pass: zero mismatches and hours are operator-set. Fail: block the release until copy or configuration is corrected. Recorded in: progress.md.
- **G-CX-015 — Automation exit walkthrough.** Verifies: CX-025, CX-026, CX-032. Check: scripted walkthrough — run every automated flow to completion and assert each terminates in a human handoff, a ticket, or an article within a bounded number of steps, that automated messages carry the automation label, and that escalation carries the full transcript into the ticket. Pass: every flow exits, labeled, with context intact. Fail: block launch of the failing flow. Recorded in: progress.md.

## Anti-patterns

- **The greeter ambush.** A proactive chat popup fires on every page load, covers content on mobile, and reappears after dismissal. Catch it: it triggers at most once per session, only on pages where users get stuck, and a dismissal is permanent for that session.
- **Reply-time drift.** The configured expected reply time was set at launch and never revisited, while actual staffing shrank. Catch it: compare the configured expectation against the measured median first-response time on the owner's review cadence; drift means reconfigure or restaff.
- **The context shredder.** The user explains the problem in chat, gets escalated, and the human's first reply asks them to describe the problem. Catch it: read the transcript before replying; if the reply asks for anything already in the thread, the handoff failed even if the tooling worked.
- **The attachment dead end.** The widget offers file upload, the user sends a screenshot, and the agent view shows nothing attached. Catch it: include one attachment in the G-CX-011 delivery test, in both directions.

## Examples

- [Example 1 — The looping bot given an exit](examples/example-1.md) — corrects CX-025.
- [Example 2 — The 24/7 default replaced with real hours](examples/example-2.md) — corrects CX-023, CX-024.
- [Example 3 — Client-supplied identity replaced with a signed token](examples/example-3.md) — corrects CX-021.

## Recall anchors

- If no human or ticket waits behind it, it is not chat — it is decoration.
- Hours are configuration, not copy; the 24/7 default never ships.
- Every bot flow ends: human, ticket, or article.
- The bot says it is a bot.
- Delivered means the server said so.

## Checklist

- [ ] Widget boots with server-signed identity; forged-token test passes (G-CX-012).
- [ ] Office hours and expected reply time are configured from real availability, non-default (CX-023).
- [ ] Two-state delivery test passes, including one attachment each way (G-CX-011).
- [ ] Offline path shows return time, no "live" wording, and creates a ticket (G-CX-013).
- [ ] Every automated flow exits to a human, a ticket, or an article, labeled as automation (G-CX-015).
- [ ] Copy-vs-config audit is clean: no availability claim the configuration does not back (G-CX-014).
- [ ] Named inbox owner and review cadence are written down (CX-028).
- [ ] Conversation history persists across sign-out and sign-in (CX-029).
