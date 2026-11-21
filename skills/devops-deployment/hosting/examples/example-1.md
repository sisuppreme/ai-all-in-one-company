# Example 1 — A localhost "launch" replaced by an externally verified deployment

## Before

The deploy finishes and the launch is announced with a screenshot of the app
running at localhost:3000. Nobody opens the public URL. It still serves the
hosting provider's placeholder page, because the production deployment was
never triggered — and the first visitor reports it.

## After

1. The production deployment is triggered from the repo's main branch.
2. From a phone on mobile data (a network other than the deploy network),
   the public URL is loaded: it returns the app over valid HTTPS.
3. The provider's deployment record shows the live commit SHA; it is compared
   with `git rev-parse HEAD` and matches.
4. The URL, the commit SHA, and the check time are written into progress.md.
   Only then is the launch announced.

Note: corrects DO-151 — production is verified from outside, on the current commit, before anything is called launched.
