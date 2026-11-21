# Example 1 — One page, two jobs

Demonstrates: PM-021 — one page, one Diátaxis mode; a page serving two reader needs is split before it ships.

## Before

A single page titled "Backups" tries to teach and to specify at once:

> ## Backups
>
> Welcome! In this guide you will learn how backups work and become a backup pro. Backups are important because data loss can happen at any time.
>
> ### Reference: flags
>
> | Flag | Type | Default |
> |---|---|---|
> | `--full` | bool | false |
> | `--retain` | int | 7 |
> | `--dest` | path | `./backups` |
>
> ### Your first backup
>
> 1. Open a terminal.
> 2. Run `backup --full`.
>
> ### Why we chose snapshot-based backups
>
> When the team designed the backup system in 2024, we considered three approaches…

The page mixes a tutorial (learn by doing), a reference table (look up a fact), and an explanation (design rationale). The learner wades through a flag table; the reader looking up a default value wades through a lesson.

## After

The same material split into three pages, each declaring its mode in front matter:

**`tutorials/first-backup.md`** — `mode: tutorial`

> ## Your first backup
>
> In this tutorial you will run a full backup and restore one file from it.
>
> 1. Run `backup --full`. You should see `Snapshot written to ./backups`.
> 2. Delete the file `notes.txt` from your test folder.
> 3. Run `restore notes.txt`. The file reappears — your backup works.
>
> For every flag and default, see the [backup command reference](../reference/backup-command.md).

**`reference/backup-command.md`** — `mode: reference`

> ## `backup` command
>
> | Flag | Type | Default | Meaning |
> |---|---|---|---|
> | `--full` | bool | false | Snapshot all data, not only changes since the last snapshot |
> | `--retain` | int | 7 | Snapshots kept before the oldest is deleted |
> | `--dest` | path | `./backups` | Directory snapshots are written to |

**`explanation/snapshot-design.md`** — `mode: explanation`

> ## Why backups are snapshot-based
>
> The backup system stores snapshots rather than file copies because…

Each reader now lands on a page written only for their need, and each page can be reviewed and re-dated on its own trigger.
