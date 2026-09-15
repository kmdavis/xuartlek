---
noteType: pf2eMonster
aliases: "Traveling Priest of Desna"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Traveling Priest of Desna"
level: 9
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3448"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Traveling Priest of Desna"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "+19"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +17, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +21, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +19"
abilityMods: [2, 4, 1, 1, 4, 2]
abilities_top:
  - name: "Path of the Faithful"
    desc: "The pilgrim can evangelize their religious teachings to use their [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] modifier instead of [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]]."
  - name: "Traveler's Lesson"
    desc: "Creatures that engage in conversation with the traveling priest gain a +2 circumstance bonus to all [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] checks and [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] checks for 4 hours related to any topics discussed with the traveling priest."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/worn-items/Shining Symbol|_shining symbol_]], _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/knife/Starknife|starknife]]_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +19"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Messenger's Amnesty"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A traveling priest with a message to deliver is continually protected by a DC 25 [[srd/pf2e/compendium/spells/rank-1/Sanctuary|_sanctuary_]] spell. If the traveling priest breaks the _sanctuary_, the effect returns if the traveling priest ceases hostility for 10 minutes."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _starknife_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ _starknife_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+8 piercing"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 27, 2 Focus Points - __5th__ [[srd/pf2e/compendium/spells/focus/Agile Feet|Agile Feet]], [[srd/pf2e/compendium/spells/focus/Traveler's Transit|Traveler's Transit]]"
  - name: "Blessing of Travel"
    desc: "If the traveling priest takes an action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] trait, their Strikes deal an extra 2d8 spirit damage until the end of their turn."
  - name: "Zealous Rush"
    desc: "⬲"
  - name: "Trigger"
    desc: "The traveling priest casts a spell that takes 1 or more actions and affects only them"
  - name: "Effect"
    desc: "The traveling priest Strides up to 10 feet, or up to their full Speed if the triggering spell took 2 actions or more to cast."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 27, attack +19 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/Create Water|Create Water]], [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Create Food|Create Food]], [[srd/pf2e/compendium/spells/rank-2/Environmental Endurance|Environmental Endurance]], [[srd/pf2e/compendium/spells/rank-2/Silence|Silence]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Dream Message|Dream Message]], [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]], [[srd/pf2e/compendium/spells/rank-3/Safe Passage|Safe Passage]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]], [[srd/pf2e/compendium/spells/rank-2/Spiritual Armament|Spiritual Armament]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×5), [[srd/pf2e/compendium/spells/rank-5/Sending|Sending]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]]"
sourcebook: "_NPC Core_, page 34."
```

```encounter-table
name: Traveling Priest of Desna
creatures:
  - 1: Traveling Priest of Desna
```
