# Migration spec

Rules for moving legacy content into `content/`. Lives in `docs/` so it is tracked
but never published.

Sources, in the order they were written:

1. `~/Documents/vaults/Myrrhina for DMs` -- Obsidian vault, oldest, 51 md + 46 assets
2. `~/src/github.com/kmdavis/xuartlek-foundry` -- archived, 491 md + 428 ts + 485 images
3. this repo -- the destination

---

## 1. Output rules

**Markdown and images only.** No TypeScript comes across. The `.ts` files were a
loader shim for a TS-first app; this site is markdown-first.

- **288 `deity.ts`** are five-line loaders. Drop all of them.
- **~79 `plane.ts` / `world.ts` / `system.ts` / `calendar.ts`** contain data that
  exists nowhere else: the plane congruence graph, the portal connection graph,
  thumbnail paths, calendar structure, and the 23 Low City district definitions.
  **Mine these into frontmatter, then drop the file.**
- Anything mechanical and parseable goes in **frontmatter**, so Obsidian Bases and
  other tools can read it. Keep keys flat and consistently typed.

## 2. Publishing: there are two gates, and they use different keys

**The repo and the site are both public.** `baseUrl: kmdavis.github.io/xuartlek`.
Current branch is `v5`, which is also what quartz-syncer pushes to.

Content can reach `content/` two ways, and each has its own flag:

| Path in | Gate | Key | Default |
|---|---|---|---|
| **quartz-syncer**, from the Obsidian vault | `publishFrontmatterKey: publish`, `allNotesPublishableByDefault: false` | **`publish: true`** to opt in | nothing syncs |
| **Direct git commit** into `content/` | the `remove-draft` Quartz plugin, which reads `frontmatter.draft` | **`draft: true`** to opt out | everything publishes |

> **`published: false` does nothing under either gate.** The `explicit-publish`
> plugin, which would read `publish`/`published` at build time, is `enabled: false`.

**Set both keys on every migrated note.** `publish: true` on anything that should be
live, `draft: true` on anything that should not. It costs one line and it is correct
whichever way the file travels.

`ignorePatterns` currently excludes `private`, `templates`, `.obsidian`.

### `archive/`

Anything content-like that must live in the repo but never on the site goes in
**`archive/`, mirroring the folder structure of `content/`**.

```
content/campaigns/votgz/sessions/...
archive/campaigns/votgz/sessions/...
```

`archive/` sits outside `content/`, so Quartz never sees it and no flag is needed.
The parallel structure means anything can be promoted by moving it across.

**The repo is public, so `archive/` is not a privacy mechanism.** Session transcripts
do not go in `archive/` either. They are not migrated at all.

**Session transcripts are not migrated at all.** They are raw auto-transcripts of
real conversations containing Shopify-internal material: unposted headcount, named
managers, hiring discussion. They do not enter this repo in any form. Curated
session notes may be migrated; the transcript bodies may not.

**No GM-only content.** Everyone at the table is now a GM. The
`requiredRole: 'gamemaster'` entries in `history.ts` become ordinary content, and
the same for `requiredRole` in the calendar definitions.

## 3. File naming

`lore.md` was a loader convention and it goes away. **416 files are named
`lore.md`.** Each takes a semantic name.

**Default rule:** the file takes the entity's display name and is unique across the
whole of `content/`.

### Folder notes: name the note after its folder

**Decided, and verified against the Quartz source.** An entity with children is a
folder plus a note inside it bearing the same name:

```
atlas/systems/tyros/shubae/shubae.md      -> serves at /atlas/systems/tyros/shubae/
atlas/systems/tyros/shubae/sielmoro.md
```

`slugifyFilePath` in `@quartz-community/utils` does this:

```js
const segments = slug.split("/");
if (segments.length >= 2 && segments[segments.length - 1] === segments[segments.length - 2]) {
  segments[segments.length - 1] = "index";
  slug = segments.join("/");
}
```

So a note named after its parent folder is rewritten to `.../index`, and
`simplifySlug` then trims the `index`. **Clean URLs and unique filenames at the same
time.** Hugo-style `_index.md` is handled too.

An earlier session concluded Quartz could not do this. That was wrong.

**Required config change:** set `folderNoteName` to `{{folder_name}}` in the
folder-notes plugin. It is currently the literal string `index`. The token is
supported. Change it in the Obsidian UI, or close Obsidian first, because a running
Obsidian will overwrite a hand-edited `data.json`.

**Do not use `index.md`.** It gives the same URLs but produces ~100 identically named
files, which breaks Obsidian wikilink resolution even though Quartz would cope.

**Collisions must be resolved, because wikilinks resolve by shortest path.** These
are the ones in the current tree:

| Pattern | Count | Rule |
|---|---|---|
| `{plane}/pantheon/lore.md` | 37 | `{Plane} Pantheon.md` |
| `{world}/calendars/default/lore.md` | 12 | Use the calendar's real `title` from `calendar.ts`, e.g. `Shubese Tidal Calendar.md` |
| Eponymous deities: a plane and its namesake deity | ~9 | Plane keeps the bare name. Deity becomes `{Name} (deity).md`, with `aliases: ["{Name}"]` |
| `planes/material/lore.md` vs `planes/material/material/lore.md` | 1 | Essence group becomes `Material Essence.md`; the plane becomes `Material Plane.md` |

Essence group pages generally: `Mind Essence.md`, `Spirit Essence.md`,
`Matter Essence.md`, `Life Essence.md`, `Material Essence.md`.

**Before any bulk write, re-run the filename collision check:**

```sh
find content -name '*.md' -not -path './srd/*' \
  | awk -F/ '{print tolower($NF)}' | sort | uniq -d
```

Must return nothing, **except** folder notes, which are legitimately named after
their parent folder and are handled by `slugifyFilePath`.

**The SRD must be excluded from that check.** Its 11,389 files already contain
hundreds of duplicate basenames across `bestiary/`, `compendium/` and `books/`:
`deity.md`, `dragon.md`, `shadow.md`, `spirit.md`, `index.md` and many more. Those
collisions predate this migration and are not ours to fix.

**But setting content must not collide with an SRD basename either**, or `[[Shadow]]`
becomes a coin toss. Check any new name against the SRD before using it:

```sh
find content/srd -iname 'YOURNAME.md'
```

Quartz also detects slug collisions at build time (`quartz/util/slugCollisions.ts`)
and warns, resolving them last-write-wins. Treat any such warning as a migration bug
rather than an acceptable outcome.

## 4. Links

**Wikilinks throughout.** `[[Shubae]]`, not `](../../atlas/systems/tyros/shubae/lore.md)`.

- Foundry has **308 relative markdown links** which break the moment the tree is
  reshaped. Convert during the move; there is no cheaper moment.
- The vault has **442 wikilinks** which survive as long as filenames stay unique.
- Use display text where the target name reads badly: `[[Material Plane|the Material]]`.

## 5. Images

Image filenames were a loading convention too, and they get the same treatment as
`lore.md`: **semantic names, unique across the vault.**

497 images. The generic ones:

| Old | Count | What it is | New |
|---|---|---|---|
| `portrait.png` | 287 | deity portrait | `{Entity} portrait.png` |
| `thumbnail.jpg` | 35 | plane thumbnail | `{Entity} thumbnail.jpg` |
| `simple.svg` / `simple.png` | 14 | world map | `{Entity} map.svg` |
| `orbit.gif` | 12 | orbital animation | `{Entity} orbit.gif` |
| `token.png` | 6 | VTT token | `{Entity} token.png` |
| `portrait-nobg.png` | 6 | cutout portrait | `{Entity} portrait nobg.png` |
| `portrait-original.webp` | 2 | source art | `{Entity} portrait original.webp` |
| `settlement.jpg` | 2 | settlement art | `{Entity} settlement.jpg` |

Campaign token images (`token-torvin.png` and friends) are already semantic. Leave
them.

- Keep images colocated with their note.
- Rewrite every `![](./images/portrait.png)` when the note is renamed.
- The `.ts` files carry absolute paths like `/images/atlas/spirit/elysara/thumbnail.jpg`
  with no markdown equivalent. Carry them into frontmatter as `thumbnail:`.
- 287 of the 497 are deity portraits and defer with bucket H.

## 6. Frontmatter

Existing convention in this repo (from the SRD): `cssclasses`, `tags`, `aliases`,
`source`. Keep it, and add the mechanical keys below.

### On every note

```yaml
type: plane | plane-group | system | world | settlement | deity | pantheon |
      calendar | npc | arc | prop | session | rules | ancestry
aliases: []
tags: []
draft: true          # only when it must not publish
```

`title:` only when the display name differs from the filename.

### Per type, mined from the old `.ts`

Keep values flat and consistently typed. Wikilinks as strings inside arrays, so
Bases can read them.

```yaml
# plane
type: plane
essence: spirit          # mind | spirit | matter | material | life
congruent: ["[[Ruinara]]", "[[Exultia]]"]
thumbnail: images/thumbnail.jpg

# system
type: system
worlds: ["[[Shubae]]"]

# world
type: world
system: "[[Tyros]]"
primaryPortal: "[[Xuartlek]]"
secondaryPortals: ["[[Arborisle]]", "[[Tertara]]"]

# settlement
type: settlement
world: "[[Shubae]]"
district: low-city       # or high-city | under-city | estate | none
portals: ["[[Xuartlek]]", "[[Khudealine]]"]

# deity (existing keys already in the lore frontmatter, plus)
type: deity
plane: "[[Ruinara]]"
level: 26
```

### Calendars: Calendarium

`calendar.ts` is the richest machine-readable data in the migration. One file carries
`epoch`, `epochConfiguration`, `yearsOffset`, `msPerSecond: 250`, `hoursPerDay: 26`,
`daysPerWeek`, full month tables and multi-language labels.

**Calendarium is installed and has zero calendars defined.** `eventFrontmatter`,
`parseDates` and `dailyNotes` are all off, `defaultCalendar` is null.

Two things follow:

1. **Calendar definitions do not live in note frontmatter.** They live in
   `.obsidian/plugins/calendarium/data.json` under `calendars: []`. Note frontmatter
   is only for turning notes into *events* on a calendar, which is a separate and
   later decision.
2. **Calendarium cannot represent sub-day time.** Its schema has `weekdays`,
   `months`, `leapDays`, `eras`, `firstWeekDay`, `overflow`. It has no `hoursPerDay`,
   `minutesPerHour` or `secondsPerMinute`. **Shubae's 26-hour day and the 250 ms
   second cannot be carried across.**

So each calendar produces **two** artifacts:

1. **The markdown note is canonical.** Every number, including the sub-day units
   Calendarium cannot hold, in frontmatter so Bases can read it, plus the prose:
   why the numbers are what they are, and the calendar's history. Shubae's 26-hour
   day and 250 ms second live here and nowhere else.
2. **The Calendarium config** gets the day-and-above subset: weekdays, months,
   leap days, eras, `firstWeekDay`, `overflow`. Written into
   `.obsidian/plugins/calendarium/data.json`.

The note is the source of truth. The plugin config is a lossy projection of it and
is regenerable.

**Before generating 13 of them, define one calendar by hand in the Calendarium UI.**
That gives a ground-truth template to generate against, instead of guessing at the
schema. Bucket J is blocked on this and nothing else.

## 7. Corrections that ride along

Fix these in the same pass that moves the file. Doing them afterwards means touching
everything twice.

| Wrong | Right | Where |
|---|---|---|
| Senate, Senators, Ministries, High Council, Parliament | Assize, Delegates, the Authority and its departments, the Assay | vault |
| Nevermelt | Hrimgard | vault |
| 22 Low City districts, 49 total | 23 and 50 | vault |
| Haseira | Hasiera | foundry |
| "fled Tortleheim to escape certain doom" | voluntary exodus, pilgrims | foundry calendar lore |
| "25 years at each world" | 30; the timeline says so for three worlds running | foundry High City lore |
| "Ancient Skyy Tortles" for the estate-bearers | Lesser Skyy Tortles | both |

## 8. Buckets

| # | Bucket | Size | Status |
|---|---|---|---|
| A | Conventions | this document | **approved** |
| B | Vault: government, houses, city | ~10 md | **done** |
| C | Timeline, `history.ts` | 841 lines to markdown | approved |
| D | Atlas spine: planes, systems, worlds | ~89 md + 79 ts to mine | approved |
| E | Low City districts | 23 | **stubs only.** Separate project |
| F | Campaign, active | ~20 md + images | approved |
| G | Session transcripts | 20 files | **never** |
| H | Pantheon | 325 md + 294 portraits | **deferred.** To be partly rewritten |
| I | Vault remainder | ~41 md + 46 assets | mostly skip |
| J | Calendars | ~15 md + 13 ts | approved. Needs one hand-made Calendarium calendar as a template first |

## 9. Definition of done, per bucket

1. Collision check returns nothing.
2. No file named `lore.md` remains in `content/`.
3. No relative markdown links to `.md` remain: `grep -rn '](\.\./' content --include=*.md`
4. No `.ts` under `content/`.
5. Every note has `type:`, `publish:` and where needed `draft:` in frontmatter.
6. No image named `portrait.png`, `thumbnail.jpg`, `simple.svg`, `orbit.gif` or
   `token.png` remains.
6. Every image reference resolves.
7. The corrections table has been applied to everything touched.
