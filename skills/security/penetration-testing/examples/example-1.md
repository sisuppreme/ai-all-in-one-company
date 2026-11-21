# Example 1 — Authorization before tooling

## Before

The product owner messages the tester: "Hey, can you test the app this week? Go ahead." The tester treats the chat message as authorization, runs a port scan and an authentication brute-force against the production URL that night, and trips the monitoring alerts. The on-call engineer spends two hours treating it as a real attack because no window, stop conditions, or emergency contact were ever agreed. The scan also touched the payment provider's hosted checkout domain, which was never the owner's to authorize.

## After

Before any tool runs, the owner signs `security/engagement.md`: Authorization (owner name, signature, date), Scope (staging host and the app's own API domain; the payment provider's domains explicitly excluded), Techniques (OWASP WSTG cases; no denial-of-service, no social engineering), Window (Tue–Thu, 09:00–17:00), Data handling (tester-owned accounts only, minimum proof), Stop conditions (any production instability or real-user impact), and Emergency contact (on-call engineer, who is told the window in advance). Testing starts Tuesday at 09:00 against staging, and the alerts that fire are expected and stood down in minutes.

Note: corrects SE-221 — the signed engagement file is step one of the method; a chat message is not authorization.
