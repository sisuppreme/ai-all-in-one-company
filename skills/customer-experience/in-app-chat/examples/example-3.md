# Example 3 — Client-supplied identity replaced with a signed token

## Before

The widget is installed with the snippet from the vendor's quick-start:

```html
<script>
  window.messengerSettings = { app_id: "APP_ID", user_id: currentUserId };
</script>
```

`currentUserId` is rendered into the page by client-side code. Anyone who
edits the value in a browser console and reloads boots the widget as that
user — and sees their past conversations, including billing threads.

## After

Identity is verified by the server, following the vendor's documented
installation model:

1. When a signed-in user loads a page, the server generates a signed
   identity token (a JWT signed with the app secret) for that account and
   passes only the token to the widget snippet.
2. The widget boots with the token; the tool verifies the signature before
   attaching the conversation to the account.
3. G-CX-012 runs at launch and on every identity change: a tampered token
   and a raw client-supplied user ID are both rejected, and no
   conversation is created or exposed.

A value typed in a console can no longer become someone else's inbox.

Note: corrects CX-021 — identity is server-verified with a signed token; a client-supplied user ID alone is never trusted.
