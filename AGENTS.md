# Working in this vault

Constraints and triggers for an agent working on the Xuartlek vault. Rules that
must fire without being asked, and the mistakes that have already been made here
so they are not made twice.

`README.md` explains what the repository is. This file is about how to change it
safely.

## Run the checker before you report anything done

```sh
python3 tools/check-migration.py
```

Nine gates. It is the definition of done for any content change, and it has
caught real leaks. If you add a rule that matters, add a gate for it.

Then build, because the checker does not catch rendering:

```sh
npx quartz build          # ~4 minutes
```

**A green build is not evidence that your change worked.** Read the emitted
HTML. Several bugs here produced valid markdown, a clean build and wrong output.

## The repository is public, and so is the site

Two different exposures, and they are not the same.

| | Contains GM material? |
|---|---|
| The website | **No.** `draft: true` keeps notes out of the build |
| The git repository | **Yes.** `canon/` and `gms/` are committed |

Publishing takes **two** flags, read by different tools: `publish: true` for
quartz-syncer, and the absence of `draft: true` for the site build. Setting only
one does not do what you expect.

> Explicit art was once migrated into `content/setting/`, committed and
> deployed, because an image step globbed a whole directory without reading the
> filenames. `tools/check-migration.py` now has a filename denylist. Do not
> bulk-copy binaries without looking at what you are copying.

**Session transcripts are never migrated.** They contain real-world material
that must not be published. Nothing may even link to them; the checker enforces
both.

## Before declaring anything missing, grep the contents

This mistake has been made **three times in one session**: hybrid studies, base
armour, and ~1,850 compendium entries were each reported missing and each one
was present.

The importer consolidates small categories into a single page of `##` sections.
`Starlit Span` is in `Hybrid Studies.md`. `Leather Armor` is in `Armor.md`.
`Splinter Spear` is a `###` inside `Splintering Spear.md`.

So `find -name "Thing.md"` proves nothing. Use:

```sh
grep -rn "^##* Thing$" content/srd --include=*.md
```

Graded variants (`Atmospheric Staff (Greater)`) also have no page of their own;
they live under the base item.

## Naming

- **Categories kebab-case, names Title Case.** Sources are categories: `bestiary/monster-core/humanoid/Goblin Warrior.md`, never `bestiary/Monster Core/...`.
- **Folder notes are named after their folder.** `The High City/The High City.md` serves at `/the-high-city/`. A folder note must match its folder exactly, so a folder note inside a kebab folder stays kebab.
- Renaming is **URL-neutral**: `Goblin Warrior.md` and `goblin-warrior.md` both slugify to `goblin-warrior`. Renaming does not break links, and existing path-style wikilinks keep resolving.

## Links

- **Escape the alias pipe inside a table**: `[[target\|Label]]`. An unescaped `|` is read as a column separator, splits the cell and shifts every later column. This silently ate the Will column from the party roster for weeks.
- **Setting notes never link into campaign notes.** Campaign into setting is correct and expected. Enforced.
- Relative markdown links are not allowed anywhere in `content/`. Use wikilinks.

## Prose

- **No em dashes. Use `--`.** Enforced by the checker, including in migrated source text.
- Placeholder sections (`[Detailed characteristics to be developed]`) are dropped on migration rather than published as visible blanks.

## Generated content

Several files are **generated and will lose hand edits**:

| File | Generator |
|---|---|
| `campaigns/votgz/shared/players/*.md` | `tools/import-foundry/build_players.py` |
| `campaigns/votgz/shared/Party Composition.md`, `Party Stash.md` | same |
| `content/srd/**` | `tools/import-aon/` |

Fix the generator, not the output. If you hand-edit a generated note, the next
run silently reverts you.

`build_players.py` is guarded by `check_flick.py`, which verifies every derived
statistic against a hand-entered, play-verified sheet. **Run it first.** If it
fails, the derivations are wrong and no output should be trusted.

The `tools/migrate-*.py` scripts are one-offs against sources that no longer
reflect the vault. **Re-running them discards later fixes.**

## Operational

- **Do not call `git mv` thousands of times.** It contends on `.git/index.lock` and leaves a half-renamed tree. Use `mv`, then one `git add -A`; git detects the renames.
- **Convert images to WebP on the way in.** Source art runs 2-5 MB a file; at 1600px q82 it lands around 90% smaller with no visible loss. The repository would otherwise be close to a gigabyte.
- Pass an explicit timeout to long commands. A full build is 4 minutes; the SRD importer is much longer.

## Canon

- **The in-world clock is pinned.** It advances when play advances. `calendar.ts` still carries a real-world epoch from an abandoned realtime format; it is legacy and must not drive the current date.
- The death realm is **Thanatos**, not Golarion's Boneyard. The empire's cosmology is its own: check `setting/concepts/Cosmology.md` before importing Golarion assumptions.
- When source lore contradicts migrated canon, **canon wins and the source gets corrected**, with the correction recorded in the migration script so a re-run agrees.
- Flag contradictions rather than silently resolving them. Several have been found by noticing that two numbers disagreed.
