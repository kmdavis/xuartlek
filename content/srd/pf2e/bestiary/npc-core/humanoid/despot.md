---
noteType: pf2eMonster
aliases: "Despot"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Despot"
level: 5
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3614"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Despot"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +13, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +11, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +13, [[srd/pf2e/compendium/rules-elements/skills/Lore|Warfare Lore]] +13"
abilityMods: [2, 2, 0, 4, 2, 4]
abilities_top:
  - name: "Persistent Lies"
    desc: "Any creature deceived by the despot's [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] skill believes the deception more readily on the next day. Any later Perception checks attempted against the despot's Deception DC take a –2 circumstance penalty, as do other creatures' attempts to convince the creature otherwise, such as through [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] or further Deception."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/alchemical-items/Darkvision Elixir|lesser darkvision elixir]], [[srd/pf2e/compendium/equipment/consumables/Healing Potion|lesser healing potion]] (2), Spiked Gauntlet"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +9; __Will__: +13"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spiked gauntlet +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Free-Hand|Free-Hand]]) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Sorcerer Bloodline Spells"
    desc: "DC 23, 1 Focus Point - __3rd__ [[srd/pf2e/compendium/spells/focus/Diabolic Edict|Diabolic Edict]]"
  - name: "Sorcerous Potency"
    desc: "When the despot Casts a Spell from a spell slot that deals damage, they gain a status bonus to the spell's initial damage equal to the spell's rank."
  - name: "Tongue of Flame"
    desc: "When the despot casts [[srd/pf2e/compendium/spells/rank-1/Charm|_charm_]], [[srd/pf2e/compendium/spells/focus/Diabolic Edict|_diabolic edict_]], [[srd/pf2e/compendium/spells/rank-3/Enthrall|_enthrall_]], or [[srd/pf2e/compendium/spells/rank-2/Floating Flame|_floating flame_]], either a target takes 1 fire damage per spell rank, or the despot gains a +2 status bonus to [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks for 1 round."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 23, attack +14 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bane|Bane]], [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blood Vendetta|Blood Vendetta]], [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-2/Floating Flame|Floating Flame]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Chilling Darkness|Chilling Darkness]], [[srd/pf2e/compendium/spells/rank-3/Enthrall|Enthrall]], [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (3 slots)"
sourcebook: "_NPC Core_, page 157."
```

```encounter-table
name: Despot
creatures:
  - 1: Despot
```
