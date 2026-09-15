---
noteType: pf2eMonster
aliases: "Tripkee Rain-Caller"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Rain-Caller"
level: 4
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4590"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tripkee Rain-Caller"
level: "Creature 4"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Tripkee|Tripkee]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Lore|Jungle Lore]] +10, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +12, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [1, 3, 2, 1, 5, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/dart/Dart|Dart]] (4), [[srd/pf2e/compendium/equipment/weapons/club/Staff|Staff]]"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +11; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet, climb 20 feet; jungle passage"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Prepared Primal Spells"
    desc: "DC 21, attack +14 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Electric Arc|Electric Arc]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Gust of Wind|Gust of Wind]], [[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|Hydraulic Push]], [[srd/pf2e/compendium/spells/rank-1/Thunderstrike|Thunderstrike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/Summon Elemental|Summon Elemental]] (water only), [[srd/pf2e/compendium/spells/rank-2/Water Walk|Water Walk]]"
  - name: "Druid Focus Spell"
    desc: "DC 21, 1 Focus Point - __2nd__ [[srd/pf2e/compendium/spells/focus/Tempest Surge|Tempest Surge]]"
  - name: "Jungle Passage"
    desc: "Tripkees [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Ignore Difficult Terrain|ignore difficult terrain]] in forests and jungles."
sourcebook: "_Monster Core 2_, page 327."
```

```encounter-table
name: Tripkee Rain-Caller
creatures:
  - 1: Tripkee Rain-Caller
```
