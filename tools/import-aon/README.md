# PF2e Remaster SRD importers

Generates `content/srd/pf2e/` from Archives of Nethys. Source of truth is AoN,
not the PDFs.

## Regenerating

Run in this order. The link map has to exist first: a note cannot link to a page
whose path is only decided while writing that page, so every destination is
computed up front.

```bash
cd tools/import-aon
rm -rf ../../content/srd/pf2e/{books,bestiary,compendium}   # NOT tables/
uv run --no-config --index-url https://pypi.org/simple --script build_linkmap.py
uv run --no-config --index-url https://pypi.org/simple --script import_aon.py
uv run --no-config --index-url https://pypi.org/simple --script import_bestiary.py --all
uv run --no-config --index-url https://pypi.org/simple --script import_compendium.py --all
```

Takes about 90 seconds and needs no network: generation reads `.snapshot/*.json`,
never the live endpoint.

**Delete only those three directories.** `content/srd/pf2e/tables/` is
hand-curated and no importer writes it. That is exactly why it lives beside
`books/` rather than inside `compendium/` -- anything inside an importer-owned
directory is destroyed on every run.

`uv` needs `--no-config --index-url https://pypi.org/simple`. The Shopify extra
index in `~/.config/uv/uv.toml` returns 400 for `beautifulsoup4` and `requests`.

## Scripts

| script | what it does |
|---|---|
| `books.py` | The 16 books in scope, with citation codes. Read the docstring before adding one. |
| `build_linkmap.py` | Computes every destination up front. **Run first.** |
| `import_aon.py` | Rulebook chapters, by scraping `Rules.aspx`. |
| `import_bestiary.py` | Creatures, as Fantasy Statblocks YAML. |
| `import_compendium.py` | Everything else: feats, spells, equipment, deities, traits. |
| `build_tables.py` | One-off. Rebuilds `content/srd/pf2e/tables/` from the legacy archive. |
| `linkmap.py` | Shared resolver turning AoN references into wikilinks. |
| `audit_creatures.py`, `analyze_layout.py` | Read-only checks. |

## Refreshing the snapshot

`.snapshot/` and `.cache/` are gitignored and about 100 MB. To pull new AoN data,
pass `--refresh` to `import_compendium.py`, or merge one book without refetching
everything:

```python
from import_compendium import fetch, SKIP_CATEGORIES
fetch("deity", ["divine mysteries"])
```

## Things that will bite you

- **AoN keeps legacy records alongside Remaster ones.** Nine creatures are
  indexed twice with different stats (Calikang AC 35 vs 31). Resolution prefers
  the record listing a Remaster book first in `source`; ids are useless, because
  Boggard Scout's Remaster record has the *lower* id.
- **Ids are unique only per category.** `equipment-2306` and `weapon-2306` are
  different things.
- **Three kinds of record are not content** and are dropped by `synthetic()`:
  `item-bonus` rows, item activations (AoN flags these `exclude_from_search`,
  and names them after their trait list, hence pages titled
  "(air, concentrate)"), and item variants, each of which carries a copy of the
  entire parent entry.
- **AoN serves CRLF.** The repo is `core.safecrlf=true` with `* text=auto eol=lf`,
  so all three importers normalise at input and at write.
- **Consolidated page sharding is by entry count, not bytes.** It has to be
  predictable before any body is rendered, or the link map cannot point at the
  right shard.
- **Obsidian resolves wikilinks by suffix**, so `[[srd/pf2e/...]]` works from a
  vault rooted at the repo, while staying exact for Quartz's `content/` root.
- **`public/` must stay in `.obsidian/app.json` `userIgnoreFilters`.** It holds
  ~40k Quartz build artifacts and indexing them makes Obsidian hang on
  "Loading cache...".
