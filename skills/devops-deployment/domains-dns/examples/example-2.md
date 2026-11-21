# Example 2 — Migration done on hope and "propagation"

Demonstrates DO-204, DO-205, and DO-210: lower TTL first, verify with `dig`, never report "propagating".

## Before

The site moves to a new host at noon. The A record (TTL 86400) is edited at
noon and the status update reads "done — DNS is propagating, check back in
24–48 hours." Visitors keep hitting the old server for a day, some sessions
land on each host, and nobody can say which value any resolver holds because
nothing was ever checked with `dig`.

## After

1. The day before the move, the A record's TTL is lowered to 300 seconds and
   the change is confirmed with `dig +short example.com A` showing the old
   address at the new TTL.
2. After 86400 seconds of cached answers have expired, the A record is
   changed to the new host's address from the record sheet.
3. Verification runs immediately against the authoritative nameservers:
   `dig +short example.com A` returns the new address.
4. The status update quotes that `dig` output, and the TTL is raised back
   to 3600.

The migration is reported done because the check proves it, not because time
passed.
