---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ankhrav Hive Mother"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ankhrav Hive Mother"
level: 8
source: "Monster Core"
aon_id: "creature-2823"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2823"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ankhrav Hive Mother"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
trait_02: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, tremorsense (imprecise) 90 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [6, 1, 4, -4, 2, -2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +18; __Ref__: +15; __Will__: +14"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]]) __Damage__ 2d8+6 piercing plus 2d6 acid"
  - name: "Ranged"
    desc: "⬻ acid spit +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], range 30 feet) __Damage__ 5d6 acid"
abilities_bot:
  - name: "Armor-Rending Bite"
    desc: "⬺ The hive mother makes a mandibles Strike; if the Strike hits, the target's armor takes the damage and the acid damage bypasses the armor's Hardness."
  - name: "Frenzy Pheromone"
    desc: "⬺ The hive mother unleashes a pheromone that causes all other ankhravs within a 100-foot emanation to become [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] until the start of the hive mother's next turn, and they can use the extra action only for [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]], Stride, or Strike actions. The hive mother can't unleash the pheromone again for 1d4 rounds."
  - name: "Spray Acid"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]]) The hive mother spews acid in a 60- foot cone, dealing 8d6 acid damage and 1d6 persistent acid damage (DC 26 basic Reflex save). It can't Spray Acid again for 1d4 rounds."
sourcebook: "_Monster Core_, page 20."
```

```encounter-table
name: Ankhrav Hive Mother
creatures:
  - 1: Ankhrav Hive Mother
```
