---
noteType: pf2eMonster
aliases: "Kholo Hunter"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Kholo Hunter"
level: 2
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3069"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kholo Hunter"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Kholo|Kholo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +5"
abilityMods: [4, 3, 2, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "battle axe, Leather Armor, Shortbow (20 arrows)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +7; __Will__: +7"
hp: 29
health:
  - name: "HP"
    desc: "29"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ battle axe +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d8+4 slashing"
  - name: "Melee"
    desc: "⬻ jaws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d8+2 piercing"
  - name: "Ranged"
    desc: "⬻ shortbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Pack Attack"
    desc: "A kholo hunter deals 1d4 extra damage to any creature that's within reach of at least two of the kholo hunter's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
sourcebook: "_Monster Core_, page 208."
```

```encounter-table
name: Kholo Hunter
creatures:
  - 1: Kholo Hunter
```
