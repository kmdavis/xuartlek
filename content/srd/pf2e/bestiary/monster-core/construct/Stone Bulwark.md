---
noteType: pf2eMonster
aliases: "Stone Bulwark"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Stone Bulwark"
level: 11
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3213"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Stone Bulwark"
level: "Creature 11"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +26"
abilityMods: [7, -1, 4, -5, 0, -5]
abilities_top:
  - name: "Serpentstone Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The bulwark breathes a 60- foot cone of green gas. Each creature in the area must attempt a DC 34 Fortitude save. The bulwark can't use Serpentstone Breath again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature's body hardens, causing it to become [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] for 1 round."
  - name: "Failure"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/Conditions#Petrified|petrified]] for 1 minute. It can attempt a new save at the end of each of its turns."
  - name: "Critical Failure"
    desc: "The creature becomes petrified permanently."
  - name: "Recall Knowledge - Construct"
    desc: "([[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]], [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]]): DC 30"
  - name: "Unspecific Lore"
    desc: ": DC 28"
  - name: "Specific Lore"
    desc: ": DC 25 [[srd/pf2e/bestiary/monster-core/construct/Stone Bulwark|Stone Bulwark]] Uncommon Large Construct Mindless"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +18; __Will__: +19"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Resistances__ physical 10 (except adamantine), spells 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]])"
abilities_mid:
  - name: "Statuary Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]]) 20 feet. Rocks of marble magically arise from the ground in the aura. They protect the bulwark's allies, giving each of them standard cover. These stones can be used for Throw Rock. This aura automatically activates at the start of the stone bulwark's first turn in combat and deactivates at the end of combat."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+13 bludgeoning and binding stone"
  - name: "Ranged"
    desc: "⬻ rock +22 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range increment 120 feet) __Damage__ 2d6+11 bludgeoning and binding stone"
abilities_bot:
  - name: "Binding Stone"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|Earth]]) Any creature hit by the stone bulwark's fist or rock Strike is affected by a DC 30 [[srd/pf2e/compendium/spells/rank-3/Earthbind|_earthbind_]] spell."
  - name: "Inexorable March"
    desc: "⬻ The stone bulwark Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can attempt to bar the way by succeeding at a DC 34 Fortitude save. On a critical success, the resisting creature takes no damage; otherwise it is damaged as if hit by the construct's fist."
  - name: "Throw Rock"
    desc: "⬻ Stone Slabs Depending on the material from which it is made and the care that went into crafting it, a destroyed stone bulwark may be worth as much as an immaculately sculpted marble pillar or as little as a pile of rubble."
sourcebook: "_Monster Core_, page 324."
```

```encounter-table
name: Stone Bulwark
creatures:
  - 1: Stone Bulwark
```
