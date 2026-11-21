# Example 2 — The flag that did not exist

Demonstrates: PM-022 — verify before you write; every documented behavior is checked against the actual system, and unverifiable behavior is not documented.

## Before

Written from the feature ticket, which proposed a dry-run mode that was descoped before release:

> ## Previewing a backup
>
> To see what a backup would include without writing anything, run it in dry-run mode:
>
> ```
> backup --dry-run
> ```
>
> The command prints every file it would snapshot and the total size, then exits without creating a snapshot. Use `--dry-run --verbose` to also print excluded files.

The shipped CLI has no `--dry-run` flag. Readers who follow the page get `error: unknown flag --dry-run`, and some script against output that never existed.

## After

The writer ran the CLI's help and the command itself, found no dry-run mode, and documented the verified way to inspect a backup's scope:

> ## Checking what a backup includes
>
> The include and exclude rules in `backup.toml` decide what a snapshot contains. To review the effective rules as the tool reads them, run:
>
> ```
> backup rules --effective
> ```
>
> This prints each include and exclude pattern from `backup.toml` in the order the tool applies them, marking patterns that match nothing in the current data directory. It does not create a snapshot.
>
> There is no preview mode that lists the exact files a snapshot would contain; the open request is tracked in issue #214.

Every claim on the corrected page was executed against the current build before the page shipped, and the missing capability is an honest, tracked gap instead of an invented instruction.
