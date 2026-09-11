#!/usr/bin/env python3
"""Migration checks for content/. Run from the repo root.

Implements the "definition of done" in docs/migration.md. The SRD is excluded
from collision checks: its 11,389 files already contain hundreds of duplicate
basenames that predate this migration.
"""
import re
import sys
import pathlib
import collections

ROOT = pathlib.Path("content")
SKIP = {"srd"}
ASSET_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp3"}


def ours(p):
    return not (set(p.parts) & SKIP)


def frontmatter_aliases(text):
    if not text.startswith("---"):
        return set()
    fm = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    out = set()
    m = re.search(r"^aliases:\s*\[(.*?)\]", fm, re.M)
    if m:
        out |= {a.strip().strip("\"'").lower() for a in m.group(1).split(",")}
    m = re.search(r"^aliases:\s*\n((?:\s*-\s*.+\n)+)", fm, re.M)
    if m:
        out |= {
            line.split("-", 1)[1].strip().strip("\"'").lower()
            for line in m.group(1).splitlines()
            if "-" in line
        }
    return {a for a in out if a}


def main():
    md = [p for p in ROOT.rglob("*.md")]
    assets = [p for p in ROOT.rglob("*") if p.suffix.lower() in ASSET_EXT]
    mine = [p for p in md if ours(p)]
    fail = 0

    # 1. filename collisions, excluding folder notes and the SRD
    seen = collections.defaultdict(list)
    for p in mine:
        if p.stem.lower() == p.parent.name.lower():
            continue  # folder note, handled by slugifyFilePath
        seen[p.stem.lower()].append(str(p))
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    if dupes:
        fail = 1
        print("FAIL filename collisions:")
        for k, v in dupes.items():
            print(f"  {k}: {v}")
    else:
        print("ok   no filename collisions")

    # 2. collisions against the SRD
    srd = {p.stem.lower() for p in md if not ours(p)}
    clash = sorted({p.stem.lower() for p in mine if p != ROOT / "index.md"} & srd)
    if clash:
        fail = 1
        print(f"FAIL {len(clash)} names collide with the SRD: {clash[:10]}")
    else:
        print("ok   no collisions with the SRD")

    # 3. no lore.md, no .ts under content/
    strays = [str(p) for p in mine if p.name == "lore.md"]
    strays += [str(p) for p in ROOT.rglob("*.ts") if ours(p)]
    if strays:
        fail = 1
        print(f"FAIL stray files: {strays[:10]}")
    else:
        print("ok   no lore.md and no .ts")

    # 4. no relative markdown links. The pattern deliberately does not require a
    # leading "./": bucket F shipped links like [00](sessions/00-.../notes.md),
    # which the old anchored pattern missed entirely.
    rel = []
    for p in mine:
        for m in re.finditer(r"\]\((?!https?:|#|mailto:)([^)]+\.md[^)]*)\)", p.read_text()):
            rel.append(f"{p}: {m.group(1)}")
    if rel:
        fail = 1
        print(f"FAIL {len(rel)} relative md links: {rel[:5]}")
    else:
        print("ok   no relative markdown links")

    # 5. every note has type: and publish:
    missing = [
        str(p)
        for p in mine
        if not re.search(r"^type:", p.read_text(), re.M)
        or not re.search(r"^publish:", p.read_text(), re.M)
    ]
    if missing:
        print(f"WARN {len(missing)} notes lack type:/publish: {missing[:8]}")
    else:
        print("ok   every note has type: and publish:")

    # 6. wikilinks resolve
    known = {p.stem.lower() for p in md} | {p.stem.lower() for p in assets}
    known |= {p.name.lower() for p in assets}
    for p in md:
        known |= frontmatter_aliases(p.read_text())
    broken = collections.defaultdict(set)
    total = 0
    for p in mine:
        for m in re.finditer(r"\[\[([^\]|#]+)", p.read_text()):
            t = m.group(1).strip()
            if not t:
                continue
            total += 1
            if t.split("/")[-1].lower() not in known:
                broken[str(p)].add(t)
    if broken:
        print(f"WARN unresolved wikilinks ({total} checked):")
        for f, ts in broken.items():
            print(f"  {f}: {sorted(ts)}")
    else:
        print(f"ok   all {total} wikilinks resolve")

    # 7. no em dashes
    dashes = [str(p) for p in mine if "\u2014" in p.read_text()]
    if dashes:
        fail = 1
        print(f"FAIL em dashes in: {dashes}")
    else:
        print("ok   no em dashes")

    # 8. no setting -> campaign links
    leaks = []
    campaign_names = {
        p.stem.lower() for p in mine if "campaigns" in p.parts
    }
    for p in mine:
        if "setting" not in p.parts:
            continue
        for m in re.finditer(r"\[\[([^\]|#]+)", p.read_text()):
            if m.group(1).strip().lower() in campaign_names:
                leaks.append(f"{p} -> {m.group(1)}")
    if leaks:
        fail = 1
        print(f"FAIL setting links to campaign: {leaks}")
    else:
        print("ok   no setting -> campaign links")

    # 9. material that must never be published, by filename
    BLOCKED = ("explicit", "nsfw", "nude", "-bedroom", "-backroom")
    leaked = [str(p) for p in ROOT.rglob("*")
              if p.is_file() and any(b in p.name.lower() for b in BLOCKED)]
    if leaked:
        fail = 1
        print(f"FAIL blocked material in content/: {leaked}")
    else:
        print("ok   no blocked material in content/")

    # 10. nothing may reference the session transcripts, which are never migrated
    sess = [f"{p}" for p in mine if re.search(r"sessions?/\d|/sessions/", p.read_text())]
    if sess:
        fail = 1
        print(f"FAIL references to session transcripts: {sess}")
    else:
        print("ok   no references to session transcripts")

    print("\nFAILED" if fail else "\nPASS")
    return fail


if __name__ == "__main__":
    sys.exit(main())
