---
noteType: pf2eMonster
aliases: "Wood Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/small
statblock: inline
name: "Wood Scamp"
level: 1
source: "Rage of Elements"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2670"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Wood Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 3
perception:
  - name: "Perception"
    desc: "+3; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7"
abilityMods: [3, 1, 0, -2, 0, 1]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +6; __Ref__: +4; __Will__: +10"
hp: 24
health:
  - name: "HP"
    desc: "24; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 3, slashing 3"
speed: "20 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +8 __Damage__ 1d6 piercing plus thorn puncture"
abilities_bot:
  - name: "Breathe Pollen"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]]) The wood scamp breathes choking pollen in a 15- foot cone that deals 2d6 poison damage to each creature within the area (DC 17 basic Reflex save; creatures who don't need to breathe are immune). The wood scamp can't Breathe Pollen again for 1d4 rounds."
  - name: "Thorn Puncture"
    desc: "The wood scamp breaks off one of its thorn-like claws in the target's skin, dealing 1 persistent bleed damage until the thorn is removed, which requires an Interact action. This damage is cumulative with each thorn caught in a creature's skin."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 15 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Verdant Sprout|Verdant Sprout]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Oaken Resilience|Oaken Resilience]] (self only)"
sourcebook: "_Rage of Elements_, page 205."
```

```encounter-table
name: Wood Scamp
creatures:
  - 1: Wood Scamp
```
