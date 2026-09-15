---
noteType: pf2eMonster
aliases: "Lich"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Lich"
level: 12
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3082"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lich"
level: "Creature 12"
size: "Medium"
trait_01: "Rare"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +17, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +20"
abilityMods: [0, 4, 0, 6, 4, 3]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/consumables/Invisibility Potion|_invisibility potion_]], [[srd/pf2e/compendium/spells/rank-6/Teleport|_scroll of teleport_]], [[srd/pf2e/compendium/equipment/staves/Staff of Fire|_greater staff of fire_]]"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]"
hp: 190
health:
  - name: "HP"
    desc: "190 (void healing, rejuvenation); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, physical 10 (except magical bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 60 feet, DC 29"
  - name: "Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Drain Soul Cage"
    desc: "⭓ 6th rank"
  - name: "Siphon Life"
    desc: "DC 34"
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/False Vitality|False Vitality]], [[srd/pf2e/compendium/spells/rank-2/Resist Energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/Fire Shield|Fire Shield]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]] (×2), [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-5/Wall of Ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]]"
sourcebook: "_Monster Core_, page 219."
```

```encounter-table
name: Lich
creatures:
  - 1: Lich
```
