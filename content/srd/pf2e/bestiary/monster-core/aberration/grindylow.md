---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grindylow"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/small
statblock: inline
name: "Grindylow"
level: 0
source: "Monster Core"
aon_id: "creature-3038"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3038"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Grindylow"
level: "Creature 0"
size: "Small"
trait_01: "Aberration"
trait_02: "Amphibious"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [1, 3, 2, -1, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Spear"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +7; __Will__: +5"
hp: 14
health:
  - name: "HP"
    desc: "14"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ A grindylow gains 1 extra reaction at the start of each of their turns that they can use only to make a Reactive Strike with a tentacle. They can't use more than one Reactive Strike triggered by the same action or choice."
speed: "10 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 piercing"
  - name: "Melee"
    desc: "⬻ tentacle +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+1 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ spear +5 __Damage__ 1d6+1 piercing"
  - name: "Ranged"
    desc: "⬻ spear +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Clinging Suckers"
    desc: "When a grindylow successfully Grabs a creature larger than themself, they attach to that creature. The [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] creature is not [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], but if it moves, the grindylow moves with it. If the creature is Medium or smaller, it takes a –5-foot status penalty to its Speeds while the grindylow is attached. The grindylow is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] while attached to a creature."
  - name: "Jet"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The grindylow moves up to 60 feet in a straight line through the water without triggering reactions. Giant Grindylows While most grindylows are Small, a minute percentage of these creatures keep growing throughout their lives. Those that become Large or larger gain the [[srd/pf2e/compendium/gm/creature-families/giant|giant]] trait and often become champions of their schools."
sourcebook: "_Monster Core_, page 186."
```

```encounter-table
name: Grindylow
creatures:
  - 1: Grindylow
```
