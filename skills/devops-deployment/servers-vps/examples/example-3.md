# Example 3 — A public admin panel moved behind a network restriction

## Before

The application's admin panel is reachable at `https://<domain>/admin` from
anywhere on the internet. Its only protection is its own login form: no rate
limit, no allowlist, no second factor. A scanner finds the path within a day
of launch, and password guesses run against it continuously and invisibly —
the admin logs are on the same box and nobody reviews them.

## After

The panel stops being a public surface:

1. The reverse proxy restricts `/admin` to the office VPN's exit addresses
   (IP allowlist); every other source gets 403 before the request reaches
   the application.
2. The application's own authentication stays in place on top of the
   restriction — the allowlist is a wall, not a login.
3. The gate probe confirms it: from a non-allowlisted address,
   `curl -s -o /dev/null -w "%{http_code}" https://<domain>/admin`
   returns 403, while the public site answers normally (G-DO-062).

The login form still exists. The internet can no longer reach it.

Note: corrects DO-123 — admin surfaces sit behind authentication plus a network restriction, never on the public interface alone.
