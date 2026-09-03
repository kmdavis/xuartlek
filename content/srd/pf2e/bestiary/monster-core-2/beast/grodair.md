---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grodair"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Grodair"
level: 5
source: "Monster Core 2"
aon_id: "creature-4428"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4428"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Grodair"
level: "Creature 5"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: "Fey"
trait_04: "Water"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [4, 2, 4, 1, 2, 2]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +15; __Ref__: +9; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Death Flood"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) When a grodair dies, their body explodes in a blast of pressurized water that deals 4d6 bludgeoning damage to creatures within a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 22 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature that fails its save is pushed 5 feet away from the grodair's corpse (10 feet on a critical failure)."
speed: "25 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 __Damage__ 2d8+7 piercing"
  - name: "Melee"
    desc: "⬻ tentacle +15 __Damage__ 1d10+7 bludgeoning plus Knockdown"
  - name: "Ranged"
    desc: "⬻ water jet +13 (range increment 60 feet) __Damage__ 3d6 bludgeoning plus Push 10 feet"
abilities_bot:
  - name: "Muddy Field"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) The grodair transforms all soil, sand, or similar sediment in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] into mud for 1 round. This mud is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] for creatures other than grodairs."
  - name: "Organ of Endless Water"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) The grodair causes water to pour through its scales from a magical sac in its body, either at a rate of 1 gallon per round or in a 5-foot-long stream at a rate of 5 gallons per round. It can stop the flow of water as a single action. Grodair Treasure Amid the vile, rubbery entrails of an exploded grodair is a cluster of tubular organs the size of a melon which contains their extradimensional water storage. Harvesting the organ cluster takes 5 minutes and a successful DC 22 [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] check. For the next 2d6 hours, the cluster can then be used to produce water in the same manner as a grodair's Organ of Endless Water ability. However, on a critical failure to harvest the organ cluster, it bursts and deals 2d6 bludgeoning damage to the harvester."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22 - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]]"
sourcebook: "_Monster Core 2_, page 181."
```

```encounter-table
name: Grodair
creatures:
  - 1: Grodair
```
