# Example 2 — Headers moved from the page layer to one central middleware

Demonstrates SE-162 and SE-169: the policy is set once, centrally, and error and API responses carry it too.

## Before

Headers are added by the HTML rendering helper, so only successful page renders carry them:

```python
def render_page(template, context):
    response = render(template, context)
    response.headers["Content-Security-Policy"] = CSP
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response
```

`curl -sI https://example.com/api/projects` and the 500 error page return no security headers at all — the JSON API and every error path sit outside the policy.

## After

One middleware wraps every response the app produces — pages, API routes, redirects, and the error handler — and sets the full sheet in one place:

```python
SECURITY_HEADERS = {
    "Content-Security-Policy": CSP,
    "Strict-Transport-Security": "max-age=31536000",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}

@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)  # includes error-handler responses
    for name, value in SECURITY_HEADERS.items():
        response.headers.setdefault(name, value)
    return response
```

Gate G-SE-081 diffs a page route, an API route, and a forced-error route against the header sheet at release.
