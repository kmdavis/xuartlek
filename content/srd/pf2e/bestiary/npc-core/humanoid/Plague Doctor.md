---
noteType: pf2eMonster
aliases: "Plague Doctor"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Plague Doctor"
level: 5
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3484"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Plague Doctor"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +13, [[srd/pf2e/compendium/rules-elements/skills/Lore|Plague Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +13"
abilityMods: [0, 1, 4, 2, 4, 2]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), [[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit|Healer's Toolkit]], _[[srd/pf2e/compendium/equipment/consumables/Healing Potion|minor potion of healing]]_ (4), Staff, studded leather"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +8; __Will__: +13 +2 circumstance to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 23, 1 Focus Point - __3rd__ [[srd/pf2e/compendium/spells/focus/Healer's Blessing|Healer's Blessing]]"
  - name: "Healing Hands"
    desc: "When the plague doctor casts [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]], they roll d10s instead of d8s."
  - name: "Improved Communal Healing"
    desc: "When the plague doctor casts [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]] targeting a single creature, the plague doctor also restores Hit Points equal to the spell's level to themself or any other creature within range of the spell."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Detect Poison|Detect Poison]], [[srd/pf2e/compendium/spells/rank-1/Cleanse Cuisine|Cleanse Cuisine]] (×2) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Clear Mind|Clear Mind]] (×2), [[srd/pf2e/compendium/spells/rank-2/Peaceful Rest|Peaceful Rest]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]] (×2), [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×3)"
sourcebook: "_NPC Core_, page 62."
```

```encounter-table
name: Plague Doctor
creatures:
  - 1: Plague Doctor
```
