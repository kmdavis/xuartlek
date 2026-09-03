---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Moose"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Moose"
level: 3
source: "Monster Core 2"
aon_id: "creature-4477"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4477"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Moose"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8"
abilityMods: [5, 3, 4, -4, 0, 1]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +10; __Will__: +5"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Cold Adaptation"
    desc: "The moose treats environmental cold effects as if they were one step less severe."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ antler +12 __Damage__ 1d10+7 piercing"
  - name: "Melee"
    desc: "⬻ hoof +12 __Damage__ 1d8+7 bludgeoning"
abilities_bot:
  - name: "Kick Back"
    desc: "⬻ The moose bucks and kicks back with both hind hooves, making a hoof Strike with a –2 circumstance penalty to the attack roll. If it hits, it deals an extra 1d8 bludgeoning damage. This counts as two attacks when calculating the moose's multiple attack penalty."
  - name: "Thundering Charge"
    desc: "⬺ The moose Strides twice and then makes an antler Strike. A Medium or smaller creature damaged by this attack must succeed at a DC 18 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 1."
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 20 Moose Tracks Moose thrive in cooler climates and have many adaptations to survive in the cold, including thick skin and dense, heat-retaining fur. They often make their own trails in the snow to find the best food. Adventurers sometimes stumble upon these trails and assume they lead to shelter, only to find themselves happening upon a fiercely territorial moose."
sourcebook: "_Monster Core 2_, page 225."
```

```encounter-table
name: Moose
creatures:
  - 1: Moose
```
