---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2652"
socialImage: og-image.png
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
    desc: "+17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +19"
abilityMods: [7, 3, 5, 3, 3, 3]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +17"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 10"
abilities_mid:
  - name: "Green Glow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], radiation) 20 feet. An abysium horror constantly emanates a powerful energy toxic to life. This radiation sheds dim light in the area. Any creature beginning its turn in the aura must attempt a DC 27 Fortitude save, becoming sickened 1 on a failure or sickened 2 on a critical failure. Once out of the aura, an affected creature's sickened condition automatically decreases by 1 at the beginning of each of its turns."
  - name: "Heavy"
    desc: "As long as it is immobile, the elemental can't be forcibly moved or knocked [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. If it takes a [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] action, it loses this immunity until the start of its next turn."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d8+10 slashing plus 2d4 poison"
  - name: "Ranged"
    desc: "⬻ radioactive shrapnel +23 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 60 feet) __Damage__ 2d8+7 piercing plus 2d4 poison"
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
