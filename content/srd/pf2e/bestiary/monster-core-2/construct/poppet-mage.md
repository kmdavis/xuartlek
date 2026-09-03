---
obsidianUIMode: preview
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
aon_id: "creature-4515"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4515"
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
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; two languages their creator speaks"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +8, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +8"
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
    desc: "30; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 3"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand 1d8]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Magic Hat"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Frequency"
    desc: "one per day"
  - name: "Requirements"
    desc: "The poppet mage has a free hand"
  - name: "Effect"
    desc: "The poppet mage pulls off their hat, and with a jaunty display, pulls one of the following items from their hat: a [[srd/pf2e/compendium/equipment/alchemical-items/glue-bomb-major|lesser glue bomb]], a [[srd/pf2e/compendium/equipment/alchemical-items/smoke-ball-greater|lesser smoke ball]], or a [[srd/pf2e/compendium/equipment/consumables/healing-potion-major|_minor healing potion_]]. This consumable lasts for 1 hour before becoming inert."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/dizzying-colors|Dizzying Colors]], [[srd/pf2e/compendium/spells/rank-1/mending|Mending]], [[srd/pf2e/compendium/spells/rank-1/sleep|Sleep]]"
sourcebook: "_Monster Core 2_, page 256."
```

```encounter-table
name: Poppet Mage
creatures:
  - 1: Poppet Mage
```
