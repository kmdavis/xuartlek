---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crystal Strider"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Crystal Strider"
level: 10
source: "Rage of Elements"
aon_id: "creature-2625"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2625"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Crystal Strider"
level: "Creature 10"
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +20"
abilityMods: [7, 3, 5, 0, 4, 1]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +20"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 10"
abilities_mid:
  - name: "Crystal Refraction"
    desc: "⭓"
  - name: "Trigger"
    desc: "The crystal strider is targeted by a [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]] effect"
  - name: "Effect"
    desc: "The strider redirects the triggering effect to a different creature of its choice within 30 feet or absorbs the effect harmlessly, reducing the number of rounds left to recharge Release Light by 1."
speed: "45 feet, climb 45 feet; precise steps"
attacks:
  - name: "Melee"
    desc: "⬻ leg +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d10+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crystal dart +21 (range increment 30 feet) __Damage__ 2d10+13 piercing"
abilities_bot:
  - name: "Precise Steps"
    desc: "The crystal strider's many narrow legs allow it to ignore difficult terrain."
  - name: "Release Light"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The strider emits the light that continually refracts within them to cast _chromatic ray_ as an innate primal spell heightened to 5th rank, with a +21 spell attack roll. The crystal strider can't Release Light again for 1d4 rounds."
  - name: "Trample"
    desc: "⬽ Large or smaller, leg, DC 29"
sourcebook: "_Rage of Elements_, page 104."
```

```encounter-table
name: Crystal Strider
creatures:
  - 1: Crystal Strider
```
