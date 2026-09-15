---
noteType: pf2eMonster
aliases: "Dero Magister"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/dero
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Dero Magister"
level: 5
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2904"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dero Magister"
level: "Creature 5"
size: "Small"
trait_01: "Dero"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +12, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +10, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +12, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11"
abilityMods: [1, 4, 2, 3, -1, 5]
abilities_top:
  - name: "Items"
    desc: "cytillesh toolkit (see sidebar), Staff"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +10; __Ref__: +13; __Will__: +10"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]]"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A dero magister takes 10 damage for every hour they're exposed to sunlight."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand 1d8]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Cytillesh Stare"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The magister focuses their gaze on a creature they can see within 30 feet. The target is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] for 1 round and must succeed at a DC 24 Will saving throw or be [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 round."
  - name: "Dero Medicine"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The dero is wearing a cytillesh toolkit and has a hand free"
  - name: "Effect"
    desc: "The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8+10 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Nightmare|Nightmare]], [[srd/pf2e/compendium/spells/rank-4/Rewrite Memory|Rewrite Memory]]"
  - name: "Occult Spontaneous Spells"
    desc: "DC 24 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Forbidding Ward|Forbidding Ward]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]], [[srd/pf2e/compendium/spells/rank-1/Phantom Pain|Phantom Pain]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Laughing Fit|Laughing Fit]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]], [[srd/pf2e/compendium/spells/rank-2/Stupefy|Stupefy]], [[srd/pf2e/compendium/spells/rank-2/Telekinetic Maneuver|Telekinetic Maneuver]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-3/Levitate|Levitate]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] (3 slots)"
sourcebook: "_Monster Core_, page 85."
```

```encounter-table
name: Dero Magister
creatures:
  - 1: Dero Magister
```
