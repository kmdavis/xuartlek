#!/usr/bin/env python3
"""Bucket D: migrate the atlas spine from xuartlek-foundry into content/setting/places/.

Sources
  lore.md            prose, wrapped in XML-ish tags the old app parsed out
  plane/world/system.ts   structured data (group, typed connections, settlements)

Rules
  - <dm-secrets> never reaches a published note; it goes to one GM note with draft: true.
  - Sections whose whole body is a "[... to be developed]" placeholder are dropped.
  - Folder notes are named after their parent folder, so Quartz collapses them to /folder/.
  - Em dashes become "--".
"""
import re
import json
import pathlib
import shutil
import subprocess
import sys

SRC = pathlib.Path(
    "/Users/kevandavis/src/github.com/kmdavis/xuartlek-foundry/bazaar/app/data/atlas"
)
DEST = pathlib.Path(
    "/Users/kevandavis/src/github.com/kmdavis/xuartlek/content/setting/places"
)

ESSENCE_TITLE = {
    "life-essence": "Life Essence",
    "matter-essence": "Matter Essence",
    "mind-essence": "Mind Essence",
    "spirit-essence": "Spirit Essence",
    "material": "Mortal Essence",
}
ESSENCE_REALM = {
    "life-essence": ("Inner Realms", 5),
    "matter-essence": ("Elemental Realms", 6),
    "mind-essence": ("Far Realms", 8),
    "spirit-essence": ("Outer Realms", 16),
    "material": ("Material", 1),
}
# founding years for the 23 Low City districts, from the bucket C timeline
DISTRICT_YEAR = {}
DISTRICT_RIM = {}


def load_timeline():
    ev = json.load(open("/tmp/events.json"))
    rim = {}
    for e in ev:
        m = re.match(r"(\w+)(?: founded and)? Portal completed \((.+)\)$", e["label"])
        if m:
            rim[m.group(1)] = m.group(2)
    for e in ev:
        m = re.match(r"(\w+) founded(?: and Portal completed \(.+\))?$", e["label"])
        if m:
            DISTRICT_YEAR[m.group(1)] = e["xyear"]
            if m.group(1) in rim:
                DISTRICT_RIM[m.group(1)] = rim[m.group(1)]


def title_from_lore(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def ts_field(src, name):
    m = re.search(rf"^\s*{name}:\s*'([^']*)'", src, re.M)
    return m.group(1) if m else None


def ts_connections(src):
    block = re.search(r"connections:\s*\[(.*?)\]", src, re.S)
    if not block:
        return []
    return [
        {"to": m.group(1), "type": m.group(2)}
        for m in re.finditer(r"\{\s*to:\s*'([^']+)',\s*type:\s*'([^']+)'\s*\}", block.group(1))
    ]


def ts_settlements(src):
    """Pull the settlements array out of a world.ts, one dict per district."""
    i = src.find("settlements: [")
    if i < 0:
        return []
    depth, j = 0, src.index("[", i)
    start = j
    while j < len(src):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                break
        j += 1
    body = src[start : j + 1]
    out = []
    for m in re.finditer(r"\{\s*id:\s*'([^']+)',\s*name:\s*'([^']+)',", body):
        k, d = m.start(), 0
        while k < len(body):
            if body[k] == "{":
                d += 1
            elif body[k] == "}":
                d -= 1
                if d == 0:
                    break
            k += 1
        obj = body[m.start() : k + 1]
        desc = re.search(r"description:\s*`([^`]*)`", obj)
        out.append(
            {
                "id": m.group(1),
                "name": m.group(2),
                "description": (desc.group(1).strip().replace("\u2014", "--") if desc else ""),
                "group": ts_field(obj, "group"),
                "connections": ts_connections(obj),
                "thumbnail": ts_field(obj, "thumbnail"),
            }
        )
    return out


PLACEHOLDER = re.compile(r"^\s*\[[A-Z][^\]]*(?:to be|yet to be) (?:developed|written)\]\s*$", re.M)


def clean_lore(text):
    """Strip the XML-ish tags, drop placeholder-only sections, split off DM secrets."""
    text = text.replace("\u2014", "--")

    # Pull DM secrets out by TAG, not by heading: four atlas files carry a
    # bare <dm-secrets> block with no "## DM Secrets" heading above it, and a
    # heading-based match silently leaves those in the player-facing note.
    secrets = ""
    parts = []
    for m in re.finditer(r"<dm-secrets>(.*?)</dm-secrets>", text, re.S):
        parts.append(m.group(1))
    if parts:
        secrets = "\n\n".join(parts)
        text = re.sub(r"<dm-secrets>.*?</dm-secrets>", "", text, flags=re.S)
        # drop the now-empty heading that introduced it, if there was one
        text = re.sub(r"^##+\s*DM Secrets\s*$\n*", "", text, flags=re.M | re.I)
    if re.search(r"</?dm-secrets>", text):
        raise AssertionError("unbalanced dm-secrets tag survived the strip")

    def strip_tags(s):
        return re.sub(r"^</?[a-z][a-z-]*>\s*$", "", s, flags=re.M)

    text, secrets = strip_tags(text), strip_tags(secrets)

    # drop any "## Heading" whose body is only a placeholder
    parts = re.split(r"^(##\s+.+)$", text, flags=re.M)
    rebuilt = [parts[0]]
    for head, body in zip(parts[1::2], parts[2::2]):
        stripped = PLACEHOLDER.sub("", body).strip()
        if stripped:
            rebuilt.append(head + body)
    text = "".join(rebuilt)

    # a public line that says "see dm-secrets" advertises the existence of a
    # secret to players; drop the pointer, the GM note carries the content
    text = re.sub(r"\s*\(see dm-secrets\)", "", text, flags=re.I)

    text = re.sub(r"^#\s+.+\n+", "", text, count=1)   # frontmatter title becomes the H1
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text, re.sub(r"\n{3,}", "\n\n", secrets).strip()


def rewrite_links(text, srcdir, image_names, dirmap):
    """Resolve relative links against the source tree, not against link text.

    The old app used paths like ../lore.md and ./pantheon/lore.md. Turning those
    into [[link text]] produces junk targets such as [[<- Back to Atlas]], so
    every path is resolved on disk and mapped to the note it became.
    Embeds whose file does not exist are dropped: 22 of them dangle in the source.
    """
    from urllib.parse import unquote

    def image(m):
        alt, ref = m.group(1), unquote(m.group(2))
        f = (srcdir / ref).resolve()
        if not f.exists():
            return ""                       # dangling in the source, drop it
        name = image_names.get(pathlib.Path(ref).name)
        return f"![[{name}]]" if name else ""

    text = re.sub(r"!\[([^\]]*)\]\((\.[^)]+)\)", image, text)

    def link(m):
        label, ref = m.group(1).strip(), m.group(2)
        label = re.sub(r"^[<\u2190\u2192-]+\s*", "", label)  # strip "<- Back to ..." arrows
        target = (srcdir / ref).resolve()
        if target.name == "Cosmology.md":
            return f"[[Cosmology|{label}]]"
        if target.parent.name == "pantheon":
            parent = target.parent.parent.name
            if parent in ("data", "atlas"):
                return "[[Pantheon Overview]]"
            return f'[[{parent.replace("-", " ").title()} Pantheon]]'
        try:
            rel = str(target.parent.relative_to(SRC))
        except ValueError:
            return label
        stem = dirmap.get(rel)
        if not stem:
            return label
        return f"[[{stem}]]" if label.lower() == stem.lower() else f"[[{stem}|{label}]]"

    text = re.sub(r"\[([^\]]+)\]\((\.[^)]*\.md)\)", link, text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def fm(d):
    out = ["---"]
    for k, v in d.items():
        if v is None or v == [] or v == "":
            continue
        if isinstance(v, list):
            if all(isinstance(x, str) for x in v):
                out.append(f"{k}: [{', '.join(json.dumps(x) for x in v)}]")
            else:
                out.append(f"{k}:")
                for x in v:
                    out.append(
                        "  - " + ", ".join(f"{kk}: {vv}" for kk, vv in x.items())
                    )
        elif isinstance(v, str) and (":" in v or v.startswith(("[", "{"))):
            out.append(f"{k}: {json.dumps(v)}")
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    return "\n".join(out)


if __name__ == "__main__":
    load_timeline()
    print(f"timeline: {len(DISTRICT_YEAR)} district founding years, {len(DISTRICT_RIM)} rims")


# ---------------------------------------------------------------- naming
# filename = the bare proper noun; title = whatever the lore's own H1 says.
# Explicit, because there are only about ten irregular cases and a regex
# clever enough to catch them all would be a liability.
NAME = {
    ".": "places",
    "planes": "realms",
    "planes/life-essence": "Life Essence",
    "planes/matter-essence": "Matter Essence",
    "planes/mind-essence": "Mind Essence",
    "planes/spirit-essence": "Spirit Essence",
    "planes/material": "Mortal Essence",
    "planes/material/material": "Material Plane",
    "systems": "systems",
    "systems/chelon": "Chelon",
    "systems/tessara": "Tessara",
    "systems/umbra": "Umbra",
    "systems/vortalis": "Vortalis",
    "systems/xuar": "Xuar",
    "systems/tyros/shubae/thelonese": "Thelonésë",
}
SKIP = ("pantheon", "calendars", "settlements", "images")


def target_for(rel):
    """Map an atlas directory to its destination path under content/setting/places/."""
    parts = [] if rel == "." else rel.split("/")
    name = NAME.get(rel)
    if name is None:
        name = parts[-1].replace("-", " ").title()

    if rel == ".":
        return DEST / "places.md", name
    if parts[0] == "planes":
        if len(parts) == 1:
            return DEST / "realms" / "Planes.md", name
        ess = NAME[f"planes/{parts[1]}"]
        if len(parts) == 2:
            return DEST / "realms" / ess / f"{ess}.md", name
        return DEST / "realms" / ess / f"{name}.md", name
    if parts[0] == "systems":
        if len(parts) == 1:
            return DEST / "systems" / "Systems.md", name
        sysn = NAME.get(f"systems/{parts[1]}", parts[1].title())
        if len(parts) == 2:
            return DEST / "systems" / sysn / f"{sysn}.md", name
        worldn = NAME.get("/".join(parts[:3]), parts[2].replace("-", " ").title())
        if len(parts) == 3:
            return DEST / "systems" / sysn / worldn / f"{worldn}.md", name
        return DEST / "systems" / sysn / worldn / f"{name}.md", name
    raise ValueError(rel)


def spine_dirs():
    out = []
    for f in sorted(SRC.rglob("lore.md")):
        rel = str(f.parent.relative_to(SRC))
        if any(s in rel.split("/") for s in SKIP):
            continue
        if rel.endswith("the-high-city"):
            continue  # already migrated by hand
        out.append(rel)
    return out


TYPE_FOR = {"planes": "plane", "systems": "system"}


def node_kind(rel):
    parts = [] if rel == "." else rel.split("/")
    if rel == ".":
        return "atlas"
    if parts[0] == "planes":
        return "essence" if len(parts) == 2 else ("realms-root" if len(parts) == 1 else "plane")
    if len(parts) == 1:
        return "systems-root"
    if len(parts) == 2:
        return "system"
    if len(parts) == 3:
        return "world"
    return "settlement"


def emit():
    load_timeline()
    written, secrets_blocks, images = [], [], {}
    dirmap = {rel: target_for(rel)[0].stem for rel in spine_dirs()}

    for rel in spine_dirs():
        srcdir = SRC / rel
        path, title = target_for(rel)
        kind = node_kind(rel)
        lore = (srcdir / "lore.md").read_text()
        body, secret = clean_lore(lore)

        # collect this node's images, renamed to something unique and descriptive
        imap = {}
        for img in sorted((srcdir / "images").glob("*")) if (srcdir / "images").is_dir() else []:
            if img.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
                continue
            new = f"{path.stem} {img.stem}.webp".replace("  ", " ")
            imap[img.name] = new
            images[img] = path.parent / new
        body = rewrite_links(body, srcdir, imap, dirmap)

        parts = rel.split("/") if rel != "." else []
        meta = {"title": title, "type": kind, "publish": "true"}

        if kind == "plane":
            ts = (srcdir / "plane.ts").read_text() if (srcdir / "plane.ts").exists() else ""
            ess = parts[1]
            realm, count = ESSENCE_REALM[ess]
            theme = re.search(r"\*\*Theme\*\*:\s*(.+)", body)
            # every plane's Overview holds exactly Plane, Essence Group and Theme,
            # all of which are frontmatter, so the section earns nothing on the page
            body = re.sub(r"^##\s+Overview\s*$.*?(?=^##\s|\Z)", "", body, flags=re.M | re.S)
            meta |= {
                "essence": ESSENCE_TITLE[ess],
                "realm_group": realm,
                "theme": theme.group(1).strip() if theme else None,
                "connections": [f'{c["to"]} ({c["type"]})' for c in ts_connections(ts)],
            }
        elif kind == "essence":
            realm, count = ESSENCE_REALM[parts[1]]
            meta |= {"realm_group": realm, "plane_count": count}
        elif kind == "system":
            meta |= {"worlds": [NAME.get("/".join(parts[:3]), d.name.replace("-", " ").title())
                                for d in sorted(srcdir.iterdir())
                                if d.is_dir() and (d / "world.ts").exists()]}
        elif kind == "world":
            ts = (srcdir / "world.ts").read_text() if (srcdir / "world.ts").exists() else ""
            meta |= {
                "system": NAME.get(f"systems/{parts[1]}", parts[1].title()),
                "connections": [f'{c["to"]} ({c["type"]})' for c in ts_connections(ts)],
            }
        elif kind == "settlement":
            meta |= {"world": NAME.get("/".join(parts[:3]), parts[2].title())}

        meta["tags"] = ["setting/xuartlek", "atlas"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(fm(meta) + "\n\n" + body + "\n")
        written.append(path)
        if secret:
            secrets_blocks.append((title, path.stem, secret))

    # ---- the 23 Low City districts, which live only inside world.ts ----
    for wts in sorted(SRC.rglob("world.ts")):
        rel = str(wts.parent.relative_to(SRC))
        parts = rel.split("/")
        sysn = NAME.get(f"systems/{parts[1]}", parts[1].title())
        worldn = NAME.get(rel, parts[2].replace("-", " ").title())
        for s in ts_settlements(wts.read_text()):
            meta = {
                "title": s["name"], "type": "settlement", "publish": "true",
                "world": worldn, "system": sysn,
                "district_of": "The High City" if s["group"] == "low-city-districts" else None,
                "founded": DISTRICT_YEAR.get(s["name"]),
                "rim_harbour": DISTRICT_RIM.get(s["name"]),
                "connections": [f'{c["to"]} ({c["type"]})' for c in s["connections"]],
                "tags": ["setting/xuartlek", "atlas"],
            }
            yr = DISTRICT_YEAR.get(s["name"])
            rim = DISTRICT_RIM.get(s["name"])
            lines = [s["description"] or f'{s["name"]} is a settlement on {worldn}.', ""]
            if yr and rim:
                lines += [
                    f'Founded in **{yr}**, its primary portal opens onto **{rim}**, one of the '
                    f'four rim harbours of [[The High City]]. See [[timeline|the imperial timeline]] '
                    f'for the founding sequence.', ""]
            lines += [f"Part of [[{worldn}]], in the [[{sysn}]] system."]
            p = DEST / "systems" / sysn / worldn / f'{s["name"]}.md'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(fm(meta) + "\n\n" + "\n".join(lines) + "\n")
            written.append(p)

    # ---- one GM note for every <dm-secrets> block ----
    g = ["""---
title: GM Atlas Secrets
type: atlas
publish: false
draft: true
aliases: ["Atlas Secrets"]
tags: ["setting/xuartlek", "gm-only"]
---

# GM Atlas Secrets

> [!danger] Do not show players
> `draft: true` keeps this off the built site and `publish: false` keeps
> quartz-syncer from pushing it. The repository is public, so this guards
> against players browsing the site, not against players browsing GitHub.

Every `<dm-secrets>` block from the atlas, one section per place. The
player-facing notes link nowhere near this file.
"""]
    for title, stem, secret in sorted(secrets_blocks):
        g.append(f"\n## {title}\n\nPlayer-facing note: [[{stem}]]\n\n{secret}\n")
    gp = DEST / "GM Atlas Secrets.md"
    gp.write_text("\n".join(g))
    written.append(gp)

    return written, images, secrets_blocks
