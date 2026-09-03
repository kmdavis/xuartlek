---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Abysium Horror"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/huge
statblock: inline
name: "Abysium Horror"
level: 10
source: "Rage of Elements"
aon_id: "creature-2652"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2652"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Abysium Horror"
level: "Creature 10"
size: "Huge"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +19"
abilityMods: [7, 3, 5, 3, 3, 3]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +17"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10"
abilities_mid:
  - name: "Green Glow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], radiation) 20 feet. An abysium horror constantly emanates a powerful energy toxic to life. This radiation sheds dim light in the area. Any creature beginning its turn in the aura must attempt a DC 27 Fortitude save, becoming sickened 1 on a failure or sickened 2 on a critical failure. Once out of the aura, an affected creature's sickened condition automatically decreases by 1 at the beginning of each of its turns."
  - name: "Heavy"
    desc: "As long as it is immobile, the elemental can't be forcibly moved or knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. If it takes a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action, it loses this immunity until the start of its next turn."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+10 slashing plus 2d4 poison"
  - name: "Ranged"
    desc: "⬻ radioactive shrapnel +23 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet) __Damage__ 2d8+7 piercing plus 2d4 poison"
abilities_bot:
  - name: "Trample"
    desc: "⬽ Large or smaller, claw, DC 27"
sourcebook: "_Rage of Elements_, page 158."
```

```encounter-table
name: Abysium Horror
creatures:
  - 1: Abysium Horror
```
