---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Warrior"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Warrior"
level: -1
source: "Monster Core"
aon_id: "creature-3024"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3024"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goblin Warrior"
level: "Creature -1"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 2
perception:
  - name: "Perception"
    desc: "Perception +2; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +2, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +1, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [0, 3, 1, 0, -1, 1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sword/dogslicer|Dogslicer]], Leather Armor, Shortbow (10 arrows)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +3"
hp: 6
health:
  - name: "HP"
    desc: "6"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "⬲"
  - name: "Trigger"
    desc: "A goblin ally ends a move action adjacent to the warrior"
  - name: "Effect"
    desc: "The goblin warrior Steps."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dogslicer +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
sourcebook: "_Monster Core_, page 174."
```

```encounter-table
name: Goblin Warrior
creatures:
  - 1: Goblin Warrior
```
