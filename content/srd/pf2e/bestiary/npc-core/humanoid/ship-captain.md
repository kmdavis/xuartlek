---
obsidianUIMode: preview
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
aon_id: "creature-3604"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3604"
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
    desc: "Perception +12"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [4, 2, 0, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, Hand Crossbow (10 bolts), Leather Armor, Main-gauche, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/rapier|rapier]]_"
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
    desc: "When the ship captain rolls a success on a Will save against a [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] effect, they get a critical success instead. In addition, anytime they gain the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition, reduce its value by 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ main-gauche +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +14 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Dual Disarm"
    desc: "⬺ The captain makes two Strikes, one with their rapier and one with their main-gauche (in either order). If both Strikes hit, the ship captain can attempt to Disarm the target. Their multiple attack penalty increases only after all the attacks are made. __No Quarter!__ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The captain orders their shipmates to fight without mercy. All allied creatures of equal or lower level within 20 feet of the ship captain gain a +1 status bonus to attack rolls and damage rolls until the end of the ship captain's next turn. Shipboard Spells The ship captain can gain the following spells in place of Dual Disarm."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +16; __2nd__ [[srd/pf2e/compendium/spells/rank-2/summon-elemental|_summon elemental_]], [[srd/pf2e/compendium/spells/rank-2/water-breathing|_water breathing_]], [[srd/pf2e/compendium/spells/rank-2/water-walk|_water walk_]]; __1st__ [[srd/pf2e/compendium/spells/rank-1/gentle-landing|_gentle landing_]], [[srd/pf2e/compendium/spells/rank-1/gust-of-wind|_gust of wind_]] (×2); __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/electric-arc|_electric arc_]], [[srd/pf2e/compendium/spells/cantrips/guidance|_guidance_]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|_know the way_]], [[srd/pf2e/compendium/spells/cantrips/light|_light_]], [[srd/pf2e/compendium/spells/cantrips/sigil|_sigil_]]"
sourcebook: "_NPC Core_, page 149."
```

```encounter-table
name: Ship Captain
creatures:
  - 1: Ship Captain
```
