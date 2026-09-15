---
noteType: pf2eMonster
aliases: "Ardande Gardener"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/ardande
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Ardande Gardener"
level: 1
source: "Rage of Elements"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2686"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Ardande Gardener"
level: "Creature 1"
size: "Medium"
trait_01: "Ardande"
trait_02: "Human"
trait_03: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6"
abilityMods: [0, 3, 1, 1, 4, 0]
abilities_top:
  - name: "Plant Empathy"
    desc: "The ardande gardener can use [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] to Make an Impression and make very simple requests of plants."
  - name: "Items"
    desc: "gardening tools, [[srd/pf2e/compendium/equipment/consumables/Glowing Lantern Fruit|_glowing lantern fruit_]], Shortbow (20 arrows), Sickle"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +6; __Will__: +9"
hp: 17
health:
  - name: "HP"
    desc: "17"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sickle +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d4 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Decompose"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Void energy seeps out of the ardande gardener, decaying everything within a 5-foot emanation and causing plants and foliage to age and decompose. Natural difficult terrain is destroyed, and creatures in the area with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Wood|wood]] trait take 1d6 void damage (DC 16 basic Fortitude). First World Ardande Some ardandes are born in the [[srd/pf2e/compendium/gm/Planes#First World|First World]], the children of dryads who take mortal lovers. These ardandes have little contact with other mortals and think of themselves as elemental fey rather than planar scions, a reasonable perspective when life in the First World means severance from the River of Souls."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 17, attack +9 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Take Root|Take Root]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]], [[srd/pf2e/compendium/spells/cantrips/Timber|Timber]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/Tailwind|Tailwind]], [[srd/pf2e/compendium/spells/rank-1/Wall of Shrubs|Wall of Shrubs]]"
sourcebook: "_Rage of Elements_, page 217."
```

```encounter-table
name: Ardande Gardener
creatures:
  - 1: Ardande Gardener
```
