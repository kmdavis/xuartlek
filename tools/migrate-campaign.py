#!/usr/bin/env python3
"""Bucket F: migrate the active campaign into the multi-GM structure.

Layout, agreed with Kevan:

  campaigns/votgz/
    shared/     player-visible: PCs, party sheets, props     publish: true
    canon/      what no GM may contradict: Connie, the Book  draft: true
    gms/kevan/  everything else starts here, promoted later  draft: true
      people/ places/ arcs/ rules/ props/ creatures/

Images: keep one portrait per NPC and the battle maps. Drop the "-nobg" and
"-token" variants, which are Foundry VTT assets with no use in a wiki.
"""
import re
import shutil
import pathlib
from urllib.parse import unquote

SRC = pathlib.Path(
    "/Users/kevandavis/src/github.com/kmdavis/xuartlek-foundry/bazaar/app/data/campaigns/votgz"
)
DEST = pathlib.Path("/Users/kevandavis/src/github.com/kmdavis/xuartlek/content/campaigns/votgz")
KEVAN = DEST / "gms" / "kevan"

PLACE = {"thelonese": "Thelonésë", "sielmoro": "Sielmoro",
         "camp-six": "Camp Six", "thorne-fleet": "Thorne Fleet"}

# files that are not NPCs, keyed by source path -> (subfolder, title)
EXPLICIT = {
    "README.md": ("", "Campaign README"),
    "arcs/README.md": ("arcs", "Arcs"),
    "arcs/commodore-thorne.md": ("arcs", "Commodore Thorne"),
    "arcs/homeward-bound.md": ("arcs", "Homeward Bound"),
    "locations/README.md": ("places", "Locations"),
    "locations/camp-six/README.md": ("places", "Camp Six"),
    "locations/thelonese/README.md": ("places", "Thelonésë"),
    "locations/thelonese/jobs.md": ("places", "Thelonésë Jobs"),
    "locations/thelonese/threads/bounty.md": ("threads", "The Bounty"),
    "locations/thelonese/threads/extortion.md": ("threads", "The Extortion"),
    "locations/camp-six/creatures/dusk-stalker.md": ("creatures", "Dusk Stalker"),
    "props/letter-of-marque.md": ("props", "Letter of Marque"),
    "props/love-letter.md": ("props", "Love Letter"),
    "rules/README.md": ("rules", "House Rules"),
    "rules/naval-architecture.md": ("rules", "Naval Architecture"),
    "rules/trade-goods.md": ("rules", "Trade Goods"),
}


def title_of(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def camel(name):
    """captain-stormeye -> CaptainStormeye, to match the image filenames."""
    return "".join(w.capitalize() for w in name.split("-"))


ATLAS = SRC.parent.parent / "atlas" / "systems" / "tyros" / "shubae"

# The repository and the built site are both public. Some source art is explicit
# and some is suggestive; none of it is migrated, and the guard is a filename
# denylist rather than a judgement call at review time.
BLOCKED = ("explicit", "-bedroom", "-backroom", "nsfw", "nude")


def is_blocked(p):
    return any(b in p.name.lower() for b in BLOCKED)


def find_portrait(src_md):
    """One portrait per NPC. Skip Token/-nobg variants and anything blocked."""
    stem = camel(src_md.stem)
    dirs = [src_md.parent / "images", src_md.parent.parent / "images", src_md.parent,
            ATLAS / "thelonese" / "images", ATLAS / "sielmoro" / "images"]
    for d in dirs:
        if not d.is_dir():
            continue
        for ext in (".png", ".jpg"):
            for cand in (d / f"{stem}{ext}", d / f"{src_md.stem.replace('-', ' ').title()}{ext}"):
                if cand.exists() and not is_blocked(cand):
                    return cand
    # camp-six NPCs only ever got a VTT token; better than a blank page
    for d in dirs:
        if not d.is_dir():
            continue
        tok = d / f"token-{src_md.stem}.png"
        if tok.exists() and not is_blocked(tok):
            return tok
    return None


def clean(text, title, src=None, titles=None):
    text = text.replace("\u2014", "--")
    text = re.sub(r"^#\s+.+\n+", "", text, count=1)     # frontmatter carries the title
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)\s*\n?", "", text)  # re-added from the resolved portrait
    # Cross-links become wikilinks. The pattern must not require a leading "./":
    # the campaign README links its session index as [00](sessions/00-.../notes.md).
    def link(m):
        label, ref = m.group(1), m.group(2)
        # bucket G is never migrated, so a link to a transcript would dangle
        # forever and advertise material we deliberately excluded
        if "sessions/" in ref:
            return label
        target = (src.parent / unquote(ref.split("#")[0])).resolve() if src else None
        if titles and target in titles:
            resolved = titles[target]
            return f"[[{resolved}]]" if resolved == label else f"[[{resolved}|{label}]]"
        return label
    text = re.sub(r"\[([^\]]+)\]\((?!https?:|#|mailto:)([^)]+\.md[^)]*)\)", link, text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# Titles whose filename cannot be derived safely. "Xuartlek: Voyage of the Grim
# Zephyr" would otherwise truncate to "Xuartlek" and collide with the deity note.
FILENAME_OVERRIDE = {"Xuartlek: Voyage of the Grim Zephyr": "Voyage of the Grim Zephyr"}


def filename_for(title, kind):
    if title in FILENAME_OVERRIDE:
        return FILENAME_OVERRIDE[title]
    """Titles make poor filenames: colons break URLs, and the campaign place
    notes collide with the settlement notes migrated in bucket D."""
    name = re.sub(r"^(Thread|Arc|Campaign|Location)\s*:\s*", "", title)
    name = name.split(":")[0].strip() if ":" in name else name
    if kind == "place":
        name += " GM Notes"
    return name.replace("/", "-")


def aliases_for(src_md, title):
    """Notes link each other by short name (Scar, Commodore Thorne), but the H1
    is the full form. The source slug is exactly the short name."""
    short = src_md.stem.replace("-", " ").title()
    out = {short}
    bare = re.sub(r'\s*\(.*?\)|"', "", title).strip()
    if bare and bare != title:
        out.add(bare)
    return sorted(a for a in out if a and a != title)


def fm(d):
    out = ["---"]
    for k, v in d.items():
        if v in (None, "", []):
            continue
        if isinstance(v, list):
            out.append(f"{k}: [{', '.join(chr(34)+x+chr(34) for x in v)}]")
        else:
            out.append(f'{k}: "{v}"' if isinstance(v, str) and (":" in v) else f"{k}: {v}")
    out.append("---")
    return "\n".join(out)


def main():
    written, images = [], []

    # pass one: every source file's final title, so links can resolve to it
    titles = {}
    for src in sorted(SRC.rglob("*.md")):
        rel = str(src.relative_to(SRC))
        if rel.startswith(("sessions/", "characters/")):
            continue
        text = src.read_text()
        parts = rel.split("/")
        if rel in EXPLICIT:
            sub, tt = EXPLICIT[rel]
            tt = title_of(text, tt) if sub != "places" else tt
            titles[src.resolve()] = filename_for(tt, "place" if sub == "places" else "x")
        elif len(parts) > 2 and parts[2] == "npcs":
            titles[src.resolve()] = filename_for(
                title_of(text, src.stem.replace("-", " ").title()), "npc")

    for src in sorted(SRC.rglob("*.md")):
        rel = str(src.relative_to(SRC))
        if rel.startswith(("sessions/", "characters/")):
            continue
        text = src.read_text()
        parts = rel.split("/")

        if rel in EXPLICIT:
            sub, title = EXPLICIT[rel]
            title = title_of(text, title) if sub not in ("places",) else title
            kind = {"arcs": "arc", "places": "place", "threads": "thread",
                    "creatures": "creature", "props": "prop", "rules": "rules",
                    "": "campaign"}[sub]
        elif len(parts) > 2 and parts[2] == "npcs":
            sub, kind = "people", "npc"
            title = title_of(text, src.stem.replace("-", " ").title())
        else:
            continue

        meta = {"title": title, "type": kind, "publish": "false", "draft": "true",
                "gm": "kevan", "aliases": aliases_for(src, title)}
        if len(parts) > 1 and parts[0] == "locations" and parts[1] in PLACE:
            meta["location"] = PLACE[parts[1]]
        meta["tags"] = ["campaign/votgz", "gm/kevan"]

        body = clean(text, title, src, titles)
        portrait = find_portrait(src) if kind == "npc" else None
        if portrait:
            newname = f"{filename_for(title, kind)}.webp"
            images.append((portrait, KEVAN / sub / newname))
            body = f"![[{newname}]]\n\n{body}"

        fname = filename_for(title, kind)
        out = KEVAN / sub / f"{fname}.md" if sub else KEVAN / f"{fname}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fm(meta) + "\n\n" + body + "\n")
        written.append(out)

    # battle maps are worth keeping; tokens are not
    for m in sorted(SRC.rglob("*.png")):
        if "sessions" in m.parts or "characters" in m.parts:
            continue
        n = m.name
        if n.startswith("token-") or "-nobg" in n or "-token" in n or "-2x" in n:
            continue
        if is_blocked(m):
            continue
        if any(k in n for k in ("JungleChase", "CampSix", "jungle-ford", "party-of-6")):
            images.append((m, KEVAN / "places" / f"{m.stem}.webp"))
    return written, images


if __name__ == "__main__":
    w, i = main()
    print(f"notes: {len(w)}   images: {len(i)}")
    import collections
    for k, v in sorted(collections.Counter(p.parent.name for p in w).items()):
        print(f"  {k or 'root'}: {v}")
