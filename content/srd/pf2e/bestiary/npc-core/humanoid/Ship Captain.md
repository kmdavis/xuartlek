---
noteType: pf2eMonster
aliases: "Ship Captain"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Ship Captain"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3604"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Ship Captain"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Lore|Sailing Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +10"
abilityMods: [4, 2, 0, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, Hand Crossbow (10 bolts), Leather Armor, Main-gauche, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/Rapier|rapier]]_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +12; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Bravery"
    desc: "When the ship captain rolls a success on a Will save against a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]] effect, they get a critical success instead. In addition, anytime they gain the [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] condition, reduce its value by 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ main-gauche +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +14 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Dual Disarm"
    desc: "⬺ The captain makes two Strikes, one with their rapier and one with their main-gauche (in either order). If both Strikes hit, the ship captain can attempt to Disarm the target. Their multiple attack penalty increases only after all the attacks are made. __No Quarter!__ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The captain orders their shipmates to fight without mercy. All allied creatures of equal or lower level within 20 feet of the ship captain gain a +1 status bonus to attack rolls and damage rolls until the end of the ship captain's next turn. Shipboard Spells The ship captain can gain the following spells in place of Dual Disarm."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +16; __2nd__ [[srd/pf2e/compendium/spells/rank-2/Summon Elemental|_summon elemental_]], [[srd/pf2e/compendium/spells/rank-2/Water Breathing|_water breathing_]], [[srd/pf2e/compendium/spells/rank-2/Water Walk|_water walk_]]; __1st__ [[srd/pf2e/compendium/spells/rank-1/Gentle Landing|_gentle landing_]], [[srd/pf2e/compendium/spells/rank-1/Gust of Wind|_gust of wind_]] (×2); __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Electric Arc|_electric arc_]], [[srd/pf2e/compendium/spells/cantrips/Guidance|_guidance_]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|_know the way_]], [[srd/pf2e/compendium/spells/cantrips/Light|_light_]], [[srd/pf2e/compendium/spells/cantrips/Sigil|_sigil_]]"
sourcebook: "_NPC Core_, page 149."
```

```encounter-table
name: Ship Captain
creatures:
  - 1: Ship Captain
```
