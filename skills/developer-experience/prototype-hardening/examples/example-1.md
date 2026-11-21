# Example 1 — Any-password login replaced with real server-side auth

Scenario: "TaskBoard" (a hypothetical demo MVP) is being promoted from a
sales demo to a pilot with real teams. The hardening ledger built under
DX-161 — by exercising the running prototype, not by reading its comments —
classifies the auth flow as SIMULATED: signing in with a wrong password,
with an empty password, and with a stranger's email all "work," and nothing
about the login survives in any server-side store (DX-162).

## Before

```js
// src/auth/LoginForm.jsx — the entire "authentication"
function onSubmit(email, password) {
  if (password.length > 0) {
    localStorage.setItem('tb_logged_in', 'true');
    localStorage.setItem('tb_user', email);
    navigate('/board');
  }
}

// src/auth/RequireAuth.jsx — the entire "authorization"
const isAdmin = localStorage.getItem('tb_user') === 'admin@taskboard.demo';
```

```text
# What the ledger exercise showed (DX-161, DX-162)
- Wrong password ............ accepted
- Empty password ............ rejected only by the length check above
- Reload / new browser ...... "session" is whatever localStorage says
- Server restart ............ no effect; there is no server-side session
- Privileged page .......... reachable by editing tb_user in dev tools
```

This is exactly BAN-DX-081: authentication decided in the browser, any
non-empty password accepted, and a stored "logged in" flag treated as a
session. Hiding the admin link in the UI is not authorization either —
DX-164 requires the check server-side on every privileged request.

## After

```js
// server/auth.js — credentials verified server-side (DX-164)
import { compare } from 'bcryptjs'; // password_hash stored per user (cost 12)

export async function login(req, res) {
  const { email, password } = req.body ?? {};
  // Boundary validation first (DX-166): types, lengths, allowed shape.
  if (typeof email !== 'string' || email.length > 254 ||
      typeof password !== 'string' || password.length < 1 ||
      password.length > 128) {
    return res.status(400).json({ error: 'Invalid sign-in request.' });
  }
  // Parameterized query — no string-built SQL (BAN-DX-085).
  const user = await db.oneOrNone(
    'SELECT id, password_hash, role FROM users WHERE email = $1',
    [email.toLowerCase()],
  );
  // Same generic failure for unknown email and wrong password (DX-167).
  if (!user || !(await compare(password, user.password_hash))) {
    return res.status(401).json({ error: 'Email or password is incorrect.' });
  }
  const session = await sessions.create(user.id); // server-side, revocable;
  // a fresh identifier is issued at login and any pre-login session is
  // discarded, so a fixated identifier cannot survive authentication (DX-164)
  res.cookie('tb_session', session.id, { httpOnly: true, secure: true,
                                          sameSite: 'lax' });
  return res.json({ ok: true });
}

// server/auth.js — authorization on every privileged request (DX-164)
export async function requireAdmin(req, res, next) {
  const session = await sessions.get(req.cookies.tb_session);
  if (!session) return res.status(401).json({ error: 'Sign in required.' });
  const user = await db.oneOrNone('SELECT role FROM users WHERE id = $1',
                                   [session.userId]);
  if (user?.role !== 'admin') {
    return res.status(403).json({ error: 'Not permitted.' });
  }
  return next();
}
```

Password reset is completed, not stubbed (DX-164): the reset handler sets a
new `password_hash` and deletes every existing session for that user, so the
old credential and old sessions stop working in the same operation. The old
client-side path is deleted in the same change — `tb_logged_in` / `tb_user`
are no longer read anywhere — rather than layered under the real one.

```js
// tests/auth.test.js — tests that can fail (DX-170; BAN-DX-088 avoided)
test('correct password is accepted and the session survives a reload', async () => {
  const res = await loginAs('pilot@example.com', 'correct-horse-42');
  expect(res.status).toBe(200);
  const board = await getWithSession('/api/board', res.sessionCookie);
  expect(board.status).toBe(200);
});

test('wrong password is rejected server-side', async () => {
  const res = await loginAs('pilot@example.com', 'wrong-password');
  expect(res.status).toBe(401);
  expect(res.sessionCookie).toBeUndefined();
});

test('low-privilege session replaying an admin request is rejected', async () => {
  const member = await loginAs('member@example.com', 'member-pass-7');
  const replay = await getWithSession('/api/admin/users', member.sessionCookie);
  expect(replay.status).toBe(403);
});

test('password reset invalidates the old credential and old sessions', async () => {
  const before = await loginAs('pilot@example.com', 'correct-horse-42');
  await requestAndCompleteReset('pilot@example.com', 'new-passphrase-9');
  expect((await loginAs('pilot@example.com', 'correct-horse-42')).status).toBe(401);
  expect((await getWithSession('/api/board', before.sessionCookie)).status).toBe(401);
});
```

Verification is gate G-DX-082 run against the production-configured build:
wrong password rejected, protected page refused with no session, the
admin replay refused, and the reset probe confirming the old credential is
dead. Only then is the auth area closed HARDENED under DX-174.

## Note

Corrected under DX-164 (real, server-side, complete auth and per-request
authorization), DX-166 (server-side boundary validation, parameterized
queries), and DX-170 (named critical-path tests). Removes the violation in
BAN-DX-081 (client-only / any-password authentication) and the
string-built-query pattern in BAN-DX-085. Verified by G-DX-082.
