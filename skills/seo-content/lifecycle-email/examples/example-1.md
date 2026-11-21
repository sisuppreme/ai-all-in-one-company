# Example 1 — Win-back journey with suppression and a tested fallback

## Before

A win-back journey is defined by signup date alone and sent to everyone inactive for 30 days:

```
Audience: signed up 30+ days ago
Subject: We miss you, {{first_name}}!
Body: Hi {{first_name}}, it's been a while — come back and see what's new.
```

It lands on a user who purchased yesterday (their signup is 45 days old), and because their profile has no first name, the greeting renders literally as "Hi {{first_name}}".

## After

The journey is defined by events, with suppression and a fallback greeting:

```
Stage: win-back
Entry event: no session AND no purchase for 30 days
Suppression: purchased in last 30 days OR active in last 7 days → excluded
Subject: Your saved projects are still here
Body: Hi {{first_name | fallback: "there"}}, your drafts from last month
      are saved — pick up where you left off.
Seed-send: passed, fallback path exercised with an empty-name profile
```

Note: corrects CO-148 (event-based suppression excludes recent purchasers) and CO-146 (merge field carries a tested fallback, so no token ever renders raw).
