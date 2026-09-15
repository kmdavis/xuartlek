---
noteType: pf2eMonster
aliases: "Goblin Commando"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Commando"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3025"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goblin Commando"
level: "Creature 1"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "+5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6"
abilityMods: [3, 3, 2, -1, 0, 2]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/polearm/Horsechopper|horsechopper]], Leather Armor, Shortbow (20 arrows)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +8; __Will__: +5"
hp: 18
health:
  - name: "HP"
    desc: "18"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "⬲"
  - name: "Trigger"
    desc: "A goblin ally ends a move action adjacent to the goblin"
  - name: "Effect"
    desc: "The goblin Steps."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horsechopper +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d8+3 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
sourcebook: "_Monster Core_, page 174."
```

```encounter-table
name: Goblin Commando
creatures:
  - 1: Goblin Commando
```
