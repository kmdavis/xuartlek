---
noteType: pf2eMonster
aliases: "Mage Knight"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mage Knight"
level: 10
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3531"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mage Knight"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +22, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Lore|Warfare Lore]] +20"
abilityMods: [5, 1, 2, 4, 3, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/Armor#Full Plate|full plate]]_, _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/club/Mace|mace]]_, spellbook, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +18; __Ref__: +13 (+16 against damaging effects); __Will__: +21"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _mace_ +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 2d6+11 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+11 bludgeoning"
abilities_bot:
  - name: "Wizard School Spells"
    desc: "DC 28, 2 Focus Points - __5th__ [[srd/pf2e/compendium/spells/focus/Energy Absorption|Energy Absorption]], [[srd/pf2e/compendium/spells/focus/Force Bolt|Force Bolt]]"
  - name: "Bespell Strikes"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Requirements"
    desc: "The mage knight's most recent action was to cast a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Cantrip|cantrip]] spell"
  - name: "Effect"
    desc: "The mage knight siphons spell energy into one weapon they're wielding, or into one of their [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]] attacks. Until the end of the turn, the weapon or unarmed attack deals an extra 2d6 force damage and gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]] trait if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead."
  - name: "Drain Bonded Item"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The mage knight hasn't acted yet on this turn"
  - name: "Effect"
    desc: "The mage knight expends the power stored in their bonded item (typically their shield). This gives them the ability to cast one prepared spell they prepared today and already cast, without spending a slot."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Electric Arc|Electric Arc]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]], [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×2), [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]], [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|Wall of Thorns]] - __4th__ [[srd/pf2e/compendium/spells/rank-3/Fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Weapon Storm|Weapon Storm]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-5/Impaling Spike|Impaling Spike]], [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]]"
sourcebook: "_NPC Core_, page 94."
```

```encounter-table
name: Mage Knight
creatures:
  - 1: Mage Knight
```
