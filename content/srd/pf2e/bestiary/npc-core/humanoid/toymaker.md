---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Toymaker"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Toymaker"
level: 3
source: "NPC Core"
aon_id: "creature-3460"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3460"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Toymaker"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +10, Diplomacy +9, Performance +9, Society +8, Toys Lore +12"
abilityMods: [0, 3, 1, 3, 2, 2]
abilities_top:
  - name: "Items"
    desc: "Artisan's Toolkit (toymaking), Hand Crossbow (10 punchout bolts)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +10; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +12 (Nonlethal, range increment 60 feet, reload 1) __Damage__ 1d6+5 bludgeoning plus punchout bolts"
abilities_bot:
  - name: "Punchout Bolts"
    desc: "The toymaker's crossbow bolts are specially constructed with heavy, sap-like heads instead of piercing tips. Strikes with these bolts deal bludgeoning damage instead of piercing and have the nonlethal trait. In addition, a creature hit by one must succeed a DC 20 Fortitude saving throw or be pushed 10 feet back (or 20 feet on a critical failure)."
  - name: "Scatter Blocks"
    desc: "⬻ (Manipulate) The toymaker throws out a handful of toy building blocks of various sizes 20 feet away in a 5-foot burst. The area becomes difficult terrain and hazardous terrain. A creature that moves on the ground through the area takes 1 piercing damage for every square of that area it moves into."
  - name: "Wind-Up Soldier"
    desc: "⬺ (Manipulate) The toymaker releases a wind-up soldier that Strides 15 feet in a straight line. Whenever the soldier moves adjacent to a creature or a creature moves into a space adjacent to the soldier, the creature takes 2d8 slashing damage with a DC 20 basic Reflex save as the soldier wildly slashes its sword. A creature can take damage from the wind-up soldier only once per round. At the start of each of the toymaker's turns, the solder Strides 15 feet further along the same path. The soldier falls apart after it moves three times."
sourcebook: "_NPC Core_, page 45."
```

```encounter-table
name: Toymaker
creatures:
  - 1: Toymaker
```
