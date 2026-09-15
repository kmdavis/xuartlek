---
noteType: pf2eMonster
aliases: "Poppet Mage"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/small
statblock: inline
name: "Poppet Mage"
level: 2
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4515"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Poppet Mage"
level: "Creature 2"
size: "Small"
trait_01: "Construct"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; two languages their creator speaks"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +8, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +8"
abilityMods: [1, 1, 0, 4, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Hand Crossbow (10 bolts), spellbook containing their prepared spells, Staff"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +5; __Will__: +11"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 3"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand 1d8]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Magic Hat"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Frequency"
    desc: "one per day"
  - name: "Requirements"
    desc: "The poppet mage has a free hand"
  - name: "Effect"
    desc: "The poppet mage pulls off their hat, and with a jaunty display, pulls one of the following items from their hat: a [[srd/pf2e/compendium/equipment/alchemical-items/Glue Bomb|lesser glue bomb]], a [[srd/pf2e/compendium/equipment/alchemical-items/Smoke Ball|lesser smoke ball]], or a [[srd/pf2e/compendium/equipment/consumables/Healing Potion|_minor healing potion_]]. This consumable lasts for 1 hour before becoming inert."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Dizzying Colors|Dizzying Colors]], [[srd/pf2e/compendium/spells/rank-1/Mending|Mending]], [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]]"
sourcebook: "_Monster Core 2_, page 256."
```

```encounter-table
name: Poppet Mage
creatures:
  - 1: Poppet Mage
```
