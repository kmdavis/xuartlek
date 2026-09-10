#!/usr/bin/env python3
"""Bucket J: migrate the 13 calendars.

Only the Xuartlek Imperial Calendar is modelled in Calendarium. The other twelve
are lore: worlds run on different day lengths and keeping them all in sync in a
plugin is not worth the effort. A converter can be ported from xuartlek-foundry
later if it is ever needed at the table.

World calendars sit beside their world note. The imperial calendar sits with the
timeline, because it belongs to the travelling city rather than to any world.

Three corrections are applied, each contradicting canon in
setting/compendium/deities/material/Xuartlek.md:
  1. "fled Tortleheim" / "escape certain doom" -> the exodus was voluntary
  2. "Xuartlek ... perfect 364-day orbital year" -> Xuartlek does not orbit
  3. Shubese "Year Length: 370 days" -> its own month list sums to 372
  4. Tortlian "365 days" -> 364 base plus one leap day every third year, which
     is also where the imperial 364 comes from; the empire inherited the year
     and dropped only the leap day
"""
import re
import pathlib

SRC = pathlib.Path(
    "/Users/kevandavis/src/github.com/kmdavis/xuartlek-foundry/bazaar/app/data/atlas"
)
ROOT = pathlib.Path("/Users/kevandavis/src/github.com/kmdavis/xuartlek/content/setting")
PLACES = ROOT / "places" / "systems"

SYSTEM = {
    "belcanto": ("Belcanto", "Tertara"), "calderon": ("Calderon", "Langsevain"),
    "chelon": ("Chelon", "Tortleheim"), "eirion": ("Eirion", "Hrimgard"),
    "lumiere": ("Lumiere", "Emerraine"), "shamsara": ("Shamsara", "Khashayar"),
    "shenzhou": ("Shenzhou", "Qigang"), "strathis": ("Strathis", "Strafmack"),
    "sylvoria": ("Sylvoria", "Arborisle"), "tessara": ("Tessara", "Myrrhina"),
    "tyros": ("Tyros", "Shubae"),
}

CORRECTIONS = [
    # 1. the exodus was a pilgrimage, not an escape
    ("When the Skyy Tortles fled Tortleheim, they followed the demi-god Xuartlek "
     "to escape certain doom.",
     "When the Skyy Tortles left Tortleheim they followed the demi-god Xuartlek by "
     "choice. This was not a flight from catastrophe but a voluntary exodus, pilgrims "
     "following a partially ascended leader into the unknown."),
    ("When the Skyy Tortles fled Tortleheim during the great exodus and eventually "
     "founded the Xuartlek Empire, they brought this calendar with them. However, "
     "upon settling in Xuartlek--which happened to have a perfect 364-day orbital "
     "year--they modified the calendar by removing the leap days entirely.",
     "When the Skyy Tortles left Tortleheim on the voluntary exodus that founded the "
     "Xuartlek Empire, they brought this calendar with them. They then removed the "
     "leap days entirely. Xuartlek is not a world and does not orbit anything, so "
     "there was no longer an orbit to correct for; the imperial year was set at 364 "
     "days because that is exactly 52 weeks."),
    # 3. the Shubese summary contradicts its own month list
    ("- **Year Length**: 370 days (14 months)",
     "- **Year Length**: 372 days (14 months alternating 26 and 27 days)"),
    # 4. Tortlian is 364 + a leap day every third year; its own next line already
    #    says "13 months of 28 days each (364 days)"
    ("- **Year Length**: 365 days (Tortleheim's actual orbital period)",
     "- **Year Length**: 364 days (13 months x 28), plus one leap day every third\n"
     "  year, tracking Tortleheim's orbital period of about 364.33 days"),
    ("This calendar derives from the ancient Tortlian calendar (365 days with leap "
     "days every 3 years).",
     "This calendar derives from the ancient [[Tortlian Calendar]], which runs 364 "
     "days with one leap day every third year. The imperial calendar keeps the "
     "364-day year unchanged and drops the leap day, which is its only modification."),
]

# Intercalary days were written as *[Name: description]*. The brackets are
# decorative, but a single-bracket span reads as a link to anyone scanning the
# page, so strip them and keep the italics.
BRACKETED_LINE = re.compile(r"^\*\[([^\]]*)\]\*$", re.M)

PLACEHOLDER = re.compile(
    r"^\s*\[[A-Z][^\]]*(?:to be|yet to be) (?:developed|written)\]\s*$", re.M
)


def clean(text):
    text = text.replace("\u2014", "--")
    text = re.sub(r"^</?[a-z][a-z-]*>\s*$", "", text, flags=re.M)
    parts = re.split(r"^(##\s+.+)$", text, flags=re.M)
    out = [parts[0]]
    for head, body in zip(parts[1::2], parts[2::2]):
        if PLACEHOLDER.sub("", body).strip():
            out.append(head + body)
    text = "".join(out)
    text = BRACKETED_LINE.sub(r"*\\1*", text)
    text = re.sub(r"^#\s+.+\n+", "", text, count=1)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def overview(text, key):
    m = re.search(rf"^\-\s+\*\*{key}\*\*:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def ts_facts(ts):
    if not ts:
        return {}
    lens = [int(x) for x in re.findall(r"daysPerMonth:\s*(\d+)", ts)]
    wk = re.search(r"daysPerWeek:\s*\{\s*type:\s*'\w+',\s*value:\s*(\d+)", ts)
    epoch = re.search(r"base:\s*'([^']+)',\s*target:\s*'([^']+)'", ts)
    return {
        "months": len(lens) or None,
        "days_per_year": sum(lens) or None,
        "days_per_week": int(wk.group(1)) if wk else None,
        "has_leap_days": "true" if re.search(r"leapDays:\s*\[\s*\{", ts) else None,
        "epoch_base": epoch.group(1) if epoch else None,
        "epoch_target": epoch.group(2) if epoch else None,
    }


def main():
    written = []
    for lore in sorted(SRC.rglob("calendars/*/lore.md")):
        text = lore.read_text()
        title = re.search(r"^#\s+(.+)$", text, re.M).group(1).strip()
        ts_path = lore.parent / "calendar.ts"
        facts = ts_facts(ts_path.read_text() if ts_path.exists() else "")

        # corrections must land before the overview is read, or the frontmatter
        # keeps the value the correction exists to remove
        for bad, good in CORRECTIONS:
            text = text.replace(bad, good)
        body = clean(text)
        # the old relative links pointed at the world's lore.md
        body = re.sub(r"\[([^\]]+)\]\(\.\./\.\./lore\.md\)", r"[[\1]]", body)
        body = re.sub(r"\[([^\]]+)\]\(\.[^)]*\.md\)", r"[[\1]]", body)

        parts = lore.relative_to(SRC).parts
        imperial = "the-high-city" in parts
        if imperial:
            system = world = None
            dest = ROOT / "timeline" / f"{title}.md"
        else:
            system, world = SYSTEM[parts[1]]
            dest = PLACES / system / world / f"{title}.md"

        meta = {
            "title": title, "type": "calendar", "publish": "true",
            "world": world, "system": system,
            "year_length": overview(text, "Year Length"),
            "day_length": overview(text, "Day Length"),
            "in_calendarium": "true" if imperial else "false",
            **{k: v for k, v in facts.items() if v},
        }
        fm = ["---"]
        for k, v in meta.items():
            if v:
                fm.append(f'{k}: "{v}"' if isinstance(v, str) and (":" in v or "," in v) else f"{k}: {v}")
        fm += ['tags: ["setting/xuartlek", "calendar"]', "---"]

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n".join(fm) + "\n\n" + body + "\n")
        written.append(dest)
    return written


if __name__ == "__main__":
    w = main()
    print(f"wrote {len(w)} calendar notes")
    for p in w:
        print("  ", p.relative_to(ROOT.parent))
