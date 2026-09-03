---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "String Slime"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/large
statblock: inline
name: "String Slime"
level: 3
source: "Monster Core"
aon_id: "creature-3126"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3126"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "String Slime"
level: "Creature 3"
size: "Large"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; motion sense (precise) 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Athletics +11"
abilityMods: [4, -5, 5, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A string slime can feel nearby motion through vibration and air movement."
ac: 10
armorclass:
  - name: "AC"
    desc: "10; __Fort__: +12; __Ref__: +0; __Will__: +5"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ acid, bleed, critical hits, mental, precision, slashing, unconscious, visual"
abilities_mid:
  - name: "Split"
    desc: "Whenever a string slime would take slashing damage (if it weren't immune) and has at least 10 HP, it splits into two identical slimes with half the original's HP. One string slime is in the same space as the original, and the other appears in an adjacent unoccupied space. If no adjacent space is unoccupied, move smaller creatures and objects out of the way to make a space or the split is canceled at the GM's discretion."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +11 __Damage__ 1d8+4 bludgeoning plus 1d6 acid"
abilities_bot:
  - name: "Tag Team"
    desc: "⬺"
  - name: "Requirements"
    desc: "another string slime is within 30 feet"
  - name: "Effect"
    desc: "The slime arcs protoplasm to the other string slime. Creatures in that line take 3d6 acid damage with a DC 16 basic Reflex save. A creature that fails its save is also knocked prone."
  - name: "Weak Acid"
    desc: "A string slime's acid damages only organic material—not metal, stone, or other inorganic substances."
sourcebook: "_Monster Core_, page 256."
```

```encounter-table
name: String Slime
creatures:
  - 1: String Slime
```
