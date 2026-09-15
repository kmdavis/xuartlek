---
noteType: pf2eMonster
aliases: "Phoenix"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Phoenix"
level: 15
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3137"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phoenix"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Fire"
trait_03: "Holy"
trait_04: "Rare"
modifier: 27
perception:
  - name: "Perception"
    desc: "+27; darkvision, [[srd/pf2e/compendium/spells/cantrips/Detect Magic|_detect magic_]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +31, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +27, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +25"
abilityMods: [6, 7, 5, 7, 6, 6]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +31; __Will__: +28 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 300
health:
  - name: "HP"
    desc: "300 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Weaknesses__ cold 10, unholy 10"
abilities_mid:
  - name: "Shroud of Flame"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) 20 feet. 4d6 fire, DC 37 basic Reflex save. While this aura is active, any adjacent creature that hits the phoenix with a melee attack or otherwise touches them takes 2d6 fire damage. The phoenix can activate or deactivate the aura with a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]] trait."
  - name: "Self-Resurrection"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) When a phoenix dies, they collapse into a pile of smoldering ashes before returning to life fully healed 1d4 rounds later, as if subject to a 7th-rank [[srd/pf2e/compendium/spells/rituals/Resurrect|_resurrect_]] ritual. Self-resurrection happens only if there are some remains to resurrect; for instance, a phoenix killed by a [[srd/pf2e/compendium/spells/rank-6/Disintegrate|_disintegrate_]] spell can't use this ability. A phoenix whose remains rest within an area devoted to an unholy deity by [[srd/pf2e/compendium/spells/rituals/Consecrate|_consecrate_]] can't self-resurrect until their remains are no longer in that area. A phoenix can self-resurrect only once per year."
speed: "25 feet, fly 70 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 1d12+9 piercing plus 3d8 fire and 2d10 persistent fire"
  - name: "Melee"
    desc: "⬻ talon +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 1d6+6 piercing plus 3d8 fire and 2d10 persistent fire"
  - name: "Ranged"
    desc: "⬻ flame jet +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], range increment 40 feet) __Damage__ 6d6 fire plus 2d10 persistent fire"
abilities_bot:
  - name: "Primal Inante Spells"
    desc: "DC 39 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __6th__ [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]] (x3) - __7th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (x3), [[srd/pf2e/compendium/spells/rank-5/Divine Immolation|Divine Immolation]], [[srd/pf2e/compendium/spells/rank-2/Everlight|Everlight]] (at will), [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (x3), [[srd/pf2e/compendium/spells/rank-4/Wall of Fire|Wall of Fire]] (x3) - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]]"
  - name: "Flaming Strafe"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The phoenix blazes with superheated flame and [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to their Speed. They deal 6d6 fire damage to each creature within 20 feet of each square they move through (DC 37 basic Reflex save). Servants of Sarenrae While phoenixes are not denizens of the Outer Planes, they have long been associated with the goddess [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Sarenrae|Sarenrae]]. Indeed, many phoenixes view the Dawnflower as their patron and subscribe to her mission of redeeming those who have fallen to evil."
sourcebook: "_Monster Core_, page 264."
```

```encounter-table
name: Phoenix
creatures:
  - 1: Phoenix
```
