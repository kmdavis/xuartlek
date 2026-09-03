---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ankhrav"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Ankhrav"
level: 3
source: "Monster Core"
aon_id: "creature-2822"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2822"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ankhrav"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [4, 1, 3, -4, 0, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +8; __Will__: +7"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet, burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]]) __Damage__ 1d8+4 piercing plus 1d6 acid"
  - name: "Ranged"
    desc: "⬻ acid spit +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], range 30 feet) __Damage__ 3d6 acid"
abilities_bot:
  - name: "Armor-Rending Bite"
    desc: "⬺ The ankhrav makes a mandibles Strike; if the Strike hits, the target's armor takes the damage and the acid damage bypasses the armor's Hardness."
  - name: "Spray Acid"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The ankhrav spews acid in a 30-foot cone, dealing 3d6 acid damage and 1d6 persistent acid damage (DC 20 basic Reflex save). Ankhrav Burrows As if the appearance of a hungry ankhrav in a stretch of farmland isn't bad enough, it almost always indicates the proximity of an ankhrav hive nearby. A disturbing number of ankhravs can infest a lair. However, adventurers brave enough to crawl through the tangled burrows are often rewarded with large amounts of treasure, as ankhravs have a habit of dragging their victims back to the deepest corners of their den to feast, usually discarding the remains with most of the gear intact."
sourcebook: "_Monster Core_, page 20."
```

```encounter-table
name: Ankhrav
creatures:
  - 1: Ankhrav
```
