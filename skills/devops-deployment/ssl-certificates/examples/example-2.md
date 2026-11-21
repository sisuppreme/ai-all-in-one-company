# Example 2 — HTTP left serving beside HTTPS

## Before

HTTPS works, but the plain-HTTP site was never turned off:

```text
$ curl -sI http://example.com/login
HTTP/1.1 200 OK
```

The login page and the API both answer over HTTP, so credentials can be submitted unencrypted, and no `Strict-Transport-Security` header is sent. The deploy notes say "HTTPS is on," and nobody probed the HTTP routes.

## After

Every HTTP route redirects to its HTTPS equivalent, and HSTS is added only after the redirect is verified on all routes:

```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

```text
$ curl -sI http://example.com/login
HTTP/1.1 301 Moved Permanently
Location: https://example.com/login

$ curl -sI https://example.com/login
HTTP/2 200
strict-transport-security: max-age=63072000
```

Note: corrects DO-222, DO-223 — every HTTP route redirects to HTTPS; HSTS enabled after HTTPS is proven stable.
