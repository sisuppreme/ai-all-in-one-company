# Example 2 — A contact form whose success toast fired with no request

## Before

Dynamic pass, network test on the contact form. The tester fills the form
and clicks Send. The page shows a green toast: "Message sent — we'll reply
within one business day."

The network capture for the whole interaction:

```
(no requests issued on submit)
```

The submit handler is a stub: it prevents the default form action, shows
the toast, and discards the input. No endpoint is called, no record is
created, and the promised reply can never happen. Filed as a blocker
against DET-FAKE-015 (BAN-QA-142).

## After

The form is wired to the real endpoint by the builder skill. The retest
shows:

```
POST /api/contact            201 Created
GET  /admin/messages         → the submitted message, listed verbatim
```

The success toast now renders only after the 201 response. A second probe
submits with the endpoint forced to return 500: the form shows an error
state and preserves the typed text instead of claiming success. The
persistence test confirms the message survives a reload and a fresh login.

Note: corrects QA-285 — a success UI state with no corresponding server write in the network capture is a blocker finding by definition, never a style note.
