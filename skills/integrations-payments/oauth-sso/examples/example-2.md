# Example 2 — Auto-linked by email

Corrects IN-166, IN-167 — Identity is keyed on (`iss`, `sub`); linking is explicit, never an email match.

## Before

```js
async function onProviderSignIn(profile) {
  // Same email = same person, right?
  let user = await users.findByEmail(profile.email);
  if (!user) user = await users.create({ email: profile.email });
  return startSession(user); // an existing admin account is silently inherited
}
```

An attacker who controls any provider account carrying the admin's email address is merged straight into the admin's account — permissions granted by a cosmetic match (DET-FAKE-021).

## After

```js
async function onProviderSignIn(claims) {
  const identity = await identities.findByIssSub(claims.iss, claims.sub);
  if (identity) return startSession(identity.user);

  // New identity: create a fresh, unprivileged account keyed on (iss, sub)
  const user = await users.createUnprivileged();
  await identities.create({ userId: user.id, iss: claims.iss, sub: claims.sub, email: claims.email });
  return startSession(user);
}

// Linking to an existing account happens only here:
// the user is already signed in and explicitly confirms the link.
async function linkIdentity(currentUser, claims) {
  await identities.create({ userId: currentUser.id, iss: claims.iss, sub: claims.sub, email: claims.email });
}
```

Same email at two providers yields two identities; they become one account only when the signed-in owner confirms the link.
