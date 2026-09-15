# Xuartlek

The setting bible and campaign vault for **Voyage of the Grim Zephyr**, a
rotating-GM Pathfinder 2e (Remaster) campaign.

An Obsidian vault that also builds to a website:
**<https://kmdavis.github.io/xuartlek/>**

You do not need Obsidian to read it. You do need it to get folder notes,
Calendarium and the statblock renderer behaving like the published site.

## What is in here

| Path | What | Notes |
|---|---|---|
| `content/setting/` | The setting: 36 planes, 15 systems, 15 worlds, districts, calendars, timeline, government | 124 notes |
| `content/campaigns/votgz/` | The campaign | 57 notes |
| `content/srd/` | Pathfinder 2e Remaster reference, imported from Archives of Nethys | 11,399 notes |
| `tools/` | Importers and the migration checker | |
| `plugins/` | Two local Quartz plugins | |

### The campaign splits three ways

This matters, because the repository is public.

```
campaigns/votgz/
  shared/     player-facing. Party sheets, props, the roster.   published
  canon/      what no GM may contradict. Patron, premise.       draft: true
  gms/<name>/ each GM's own prep. Nothing starts shared.        draft: true
```

`draft: true` keeps a note out of the built site, so **the website carries no GM
material**. The repository does. Clone it only if you are running a game.

New material starts in `gms/<your name>/` and gets promoted to `shared/` or
`canon/` deliberately. Each GM has `people/`, `places/` and so on beneath their
own folder.

## Building

```sh
npm ci
npx quartz plugin install
npx quartz build          # ~4 minutes, writes public/
npx quartz build --serve  # local preview
```

Pushing to `v5` deploys through `.github/workflows/deploy.yaml`, which takes
about 7 minutes.

### Before you commit

```sh
python3 tools/check-migration.py
```

Ten checks: filename collisions, collisions with the SRD, stray `lore.md` or
`.ts`, relative links, missing `type:`/`publish:`, unresolved wikilinks, em
dashes, setting notes linking into campaign notes, material that must never be
published, and references to session transcripts.

## Conventions

- **Categories are kebab-case, names are Title Case.** `bestiary/monster-core/humanoid/Goblin Warrior.md`. Sources count as categories, so `monster-core` stays kebab.
- **Folder notes are named after their folder**, so `The High City/The High City.md` serves at `/the-high-city/`. Set `folderNoteName` to `{{folder_name}}` in the Obsidian folder-notes plugin.
- **Publishing takes two flags.** `publish: true` for quartz-syncer, and the absence of `draft: true` for the site build. They are read by different tools.
- **Setting notes never link into campaign notes.** The reverse is fine and expected. The checker enforces this.
- **No em dashes.** Use `--`. Also enforced.
- **Aliased wikilinks inside a table must escape the pipe**: `[[target\|Label]]`. An unescaped one is read as a column separator and silently eats the rest of the row.

## Tools

| Tool | Does |
|---|---|
| `tools/check-migration.py` | The pre-commit gate described above |
| `tools/import-aon/` | Builds `content/srd/` from the Archives of Nethys Elasticsearch API |
| `tools/import-foundry/` | Turns Foundry actor exports into player notes, party roster and stash |
| `tools/migrate-atlas.py` | One-off: the atlas spine out of the old app |
| `tools/migrate-calendars.py` | One-off: the 13 calendars |
| `tools/migrate-campaign.py` | One-off: the campaign into the multi-GM layout |

`tools/import-foundry/check_flick.py` verifies every derived statistic against a
hand-entered, play-verified sheet. It runs as a guard before `build_players.py`
writes anything; if it fails, the derivations are wrong and nothing should be
trusted.

**Re-running the one-off migrations will discard later hand fixes.** They
regenerate from the old sources, which no longer reflect the vault.

## Plugins

Both are local, registered in `quartz.config.yaml` as `./plugins/...`.

- **`quartz-spoiler`** renders ```spoiler fences as collapsed callouts, matching the Obsidian spoiler plugin, and `||inline spoilers||` as click-to-reveal spans. Hides text from a glance, not from view-source.
- **`quartz-statblocks`** renders the 1,333 ```statblock fences written for Obsidian's fantasy-statblocks, using the Basic Pathfinder 2e Layout.

## Timekeeping

The in-world date is **pinned**, not wired to the system clock. It advances when
play advances. See `content/setting/timeline/`.

## Credit

Built on [Quartz](https://quartz.jzhao.xyz/) by Jacky Zhao. Pathfinder content
is Paizo's, under the ORC licence, imported from
[Archives of Nethys](https://2e.aonprd.com/).
