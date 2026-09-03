---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skittering Slayer"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Skittering Slayer"
level: 8
source: "Monster Core 2"
aon_id: "creature-4571"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4571"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Skittering Slayer"
level: "Creature 8"
size: "Medium"
trait_01: "Aberration"
trait_02: "Swarm"
trait_03: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16"
abilityMods: [5, 4, 6, 0, 3, 3]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/armor#Chain Mail|Chain Mail]], _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/flail/flail|flail]]_, [[srd/pf2e/compendium/equipment/weapons/hammer/light-hammer|Light Hammer]] (3)"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +16; __Will__: +13"
hp: 130
health:
  - name: "HP"
    desc: "130; __Immunities__ precision, swarm mind; __Resistances__ physical 5, poison 5; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Agitated by Light"
    desc: "When exposed to bright light, the skittering slayer must attempt a DC 25 Will save. On a failure, they become [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 1 (frightened 2 on a critical failure). The skittering slayer then becomes immune to being agitated by light for 10 minutes."
  - name: "Discorporate"
    desc: "When the skittering slayer is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the skittering slayer can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the skittering slayer permanently. The invertebrates have a collective pool of HP, typically equal to 32 HP, and the same AC, saves, immunities, resistances, and weaknesses as the skittering slayer. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the skittering slayer."
  - name: "Scatter"
    desc: "⬲"
  - name: "Trigger"
    desc: "The skittering slayer is targeted by a splash attack or would attempt a Reflex save against an area effect"
  - name: "Effect"
    desc: "The skittering slayer scatters in place, gaining a +2 circumstance bonus to AC and Reflex saves against the triggering effect."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _flail_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]]) __Damage__ 2d6+11 bludgeoning plus clinging remnants"
  - name: "Melee"
    desc: "⬻ light hammer +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d6+11 bludgeoning plus clinging remnants"
  - name: "Melee"
    desc: "⬻ fist +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 1d4+11 bludgeoning plus clinging remnants"
  - name: "Ranged"
    desc: "⬻ light hammer +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+11 bludgeoning plus clinging remnants"
abilities_bot:
  - name: "Clinging Remnants"
    desc: "A skittering slayer's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 2d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent piercing damage]]."
  - name: "Draw Bugs"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]]) The skittering slayer draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 10 HP. At the GM's discretion, the skittering slayer doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Swarm Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The skittering slayer collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession. In this form, the skittering slayer can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]]. They can use the same action to coalesce from their swarm shape back into their normal form."
sourcebook: "_Monster Core 2_, page 311."
```

```encounter-table
name: Skittering Slayer
creatures:
  - 1: Skittering Slayer
```
