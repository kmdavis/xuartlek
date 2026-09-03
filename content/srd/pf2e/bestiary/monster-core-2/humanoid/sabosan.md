---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sabosan"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sabosan"
level: 5
source: "Monster Core 2"
other_sources: "Pathfinder #146: Cult of Cinders"
aon_id: "creature-4532"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4532"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sabosan"
level: "Creature 5"
size: "Medium"
trait_01: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; echolocation 20 feet, low-light vision, scent (imprecise) 30 feet"
languages: "Chthonian, Mwangi"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +12, Stealth +13"
abilityMods: [4, 5, 2, -1, 1, 0]
abilities_top:
  - name: "Echolocation"
    desc: "A sabosan can use their hearing as a precise sense at the listed range."
  - name: "Items"
    desc: "Spear"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +14; __Will__: +10"
hp: 78
health:
  - name: "HP"
    desc: "78"
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ] jaws +15 (Finesse) __Damage__ 2d10+4 piercing plus 1 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +15 (Agile, finesse) __Damage__ 2d8+4 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ spear +14 __Damage__ 1d6+7 piercing"
  - name: "Ranged"
    desc: "⬻ spear +15 (thrown 20 feet) __Damage__ 1d6+7 piercing"
abilities_bot:
  - name: "Drain Blood"
    desc: "⬻"
  - name: "Requirement"
    desc: "The sabosan has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The sabosan drains blood from the creature. The creature must succeed at a DC 22 Fortitude save or become drained 1. The sabosan gains a number of temporary Hit Points equal to the number of Hit Points lost by the creature due to its drained condition."
  - name: "Fell Shriek"
    desc: "⬺ (Auditory) The sabosan emits a deafening cry in a 30-foot cone. Non-sabosan creatures in this area must each succeed at a DC 22 Fortitude save or be deafened for 1 minute. The Sabosan Kingdom Sabosans were not always so confined to the edges of the wilderness. Once, many of their kind occupied the stone metropolis of Jaytirian in the heart of the Mwangi Jungle and defended it against the bestial forces of the dread Gorilla King. However, over the last few hundred years, some unknown force drove the sabosans out, and now they roam the Mwangi Expanse in dwindling numbers, searching for a new home."
sourcebook: "_Monster Core 2_, page 273."
```

```encounter-table
name: Sabosan
creatures:
  - 1: Sabosan
```
