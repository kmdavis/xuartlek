---
title: Xuartlek Imperial Calendar
type: calendar
publish: true
in_calendarium: true
calendarium_status: needs re-adding
current_date: 500-01-01
clock: pinned
months: 13
days_per_year: 364
days_per_week: 7
epoch_base: "gregorian:2024-10-01T00:00:00Z"
epoch_target: "xuartlek:500-03-01T00:00:00Z"
tags: ["setting/xuartlek", "calendar"]
---

The universal standard timekeeping system across the Xuartlek Empire, featuring 13 months of 28 days each for a perfect 364-day year with no leap days.

## Overview

The Xuartlek Imperial Calendar is the official timekeeping system of the empire. Unlike calendars tied to specific worlds, it operates independently of any orbital period - a necessity for an empire whose capital travels between worlds.

## Calendar Structure

- **13 months** of 28 days each = 364 days exactly
- **7-day weeks** (4 weeks per month, 52 weeks per year)
- **No leap days** - the calendar is independent of any world's orbit

## Historical Context - The Exodus

This calendar derives from the ancient [[Tortlian Calendar]], which runs 364 days with one leap day every third year. The imperial calendar keeps the 364-day year unchanged and drops the leap day, which is its only modification. When the Skyy Tortles left Tortleheim they followed the demi-god Xuartlek by choice. This was not a flight from catastrophe but a voluntary exodus, pilgrims following a partially ascended leader into the unknown.

They removed the leap days because they were no longer tied to any fixed world's orbit:
1. They were no longer orbiting Chelon (Tortleheim's star)
2. They were now living on the shell of a traveling demi-god
3. They could never return to their ancestral homeworld

The 364-day calendar (52 weeks exactly) was chosen for its mathematical perfection. The leap-day removal symbolizes the Skyy Tortles' acceptance of their nomadic destiny.

## Languages

The calendar is bilingual:
- **Common**: Trade language names reflecting natural phenomena
- **Tortlian**: Ancient names from the Skyy Tortles honoring their lost heritage

## Days of the Week

The 7-day week aligns with magical theory of planar convergence:

| Common | Tortlian | Meaning |
|--------|----------|---------|
| Beasday | Kragdor | Material plane, beasts and nature |
| Elemenday | Zorgath | Elemental planes, raw forces |
| Fienday | Vroknak | Lower planes, devils and demons |
| Celesday | Thrakul | Upper planes, angels and archons |
| Feyday | Drogmar | Feywild, fey and magic |
| Restday | Xulkath | Shadowfell, rest and contemplation |
| Faithday | Grakthur | Divine planes, worship and devotion |

## Months

| # | Common | Tortlian | Season | Description |
|---|--------|----------|--------|-------------|
| 1 | Lowsun | Grokthul | Winter | Deep winter, shortest days |
| 2 | Deepsnow | Kraznak | Winter | Peak winter cold |
| 3 | Icefall | Throkmar | Winter | Late winter, ice storms |
| 4 | Frostwane | Zorgath | Spring | Winter's end, thaw begins |
| 5 | Firstseed | Vroknak | Spring | Early spring, planting |
| 6 | Flowertide | Drakthul | Spring | Mid spring, blossoms |
| 7 | Brightdays | Xulkath | Spring | Late spring, long days |
| 8 | Highsun | Grakthur | Summer | Summer solstice, longest days |
| 9 | Heatswrath | Zarthok | Summer | Peak summer heat |
| 10 | Stormwall | Kragdor | Summer | Late summer, storm season |
| 11 | Firewane | Vorthrax | Autumn | Early autumn, heat fades |
| 12 | Redfall | Drogmar | Autumn | Mid autumn, leaves turn |
| 13 | Lateharvest | Thrakul | Autumn | Late autumn, final harvest |

## The current date is pinned

**The campaign date is 500-01-01, 1 Lowsun 500.** It advances when play advances
and at no other time.

The calendar was originally built for a realtime west-marches game, where the
clock ran whether or not anyone was at the table. `calendar.ts` still carries the
epoch that did it:

```
base:   gregorian:2024-10-01T00:00:00Z
target: xuartlek:500-03-01T00:00:00Z
```

That game did not last, so **the epoch is legacy and must not drive the current
date**. Left running against real time it reads 502-01-16 as of August 2026,
which is two years of drift nobody played.

When the converter is ported, it needs to read the current timestamp from a
static file rather than the system clock. The utility lives at
`scripts/calendar.mts` in `xuartlek-foundry`, though the substance of it is in
an unpublished package.

### Converting anyway

The arithmetic is trivial when you need it: 364 days a year, thirteen months of
twenty-eight, no leap correction. One real day is one imperial day, so the offset
from any known pair is plain addition.

## Calendarium

This is the only calendar modelled in Calendarium. The other twelve are lore
only: the worlds run on different day lengths and keeping them all in sync in a
plugin buys nothing at the table. `xuartlek-foundry` has a converter that could
be ported if a session ever needs one.

The plugin should be configured to match this note. Checked against
`.obsidian/plugins/calendarium/data.json`, the required values are:

| Setting | Value |
|---|---|
| Months | 13, each 28 days |
| Weekdays | 7 |
| Leap days | none |
| Year length | 364 |
| Current date | 500-01-01, pinned |

Month names in plugin order are the thirteen listed under Months, starting at
Lowsun. Weekday names are Beasday, Elemenday, Fienday, Celesday, Feyday,
Restday, Faithday.

## Cultural Significance

- The 13-month, 364-day structure is considered mathematically perfect
- Empire law requires all official dates use this calendar
- Local worlds maintain their own calendars but convert to Xuartlek Imperial for trade
- Tortlian names honor the Skyy Tortles who founded the empire millennia ago
