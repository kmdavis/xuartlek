---
noteType: pf2eMonster
aliases: "Jann"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/air
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/water
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Jann"
level: 4
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3002"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jann"
level: "Creature 4"
size: "Medium"
trait_01: "Air"
trait_02: "Earth"
trait_03: "Elemental"
trait_04: "Fire"
trait_05: "Genie"
trait_06: "Metal"
trait_07: "Water"
trait_08: "Wood"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +10, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +8, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +11"
abilityMods: [4, 2, 2, 3, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Scimitar"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +10; __Will__: +13"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ elemental resistance 5"
abilities_mid:
  - name: "Commanding Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 20 feet. A creature that enters the aura must succeed at a DC 19 Will save or be [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]] (frightened 2 on a critical failure) and is then temporarily immune for 1 minute. A [[srd/pf2e/compendium/rules-elements/traits/monster-core/Genie|genie]] (with the exception of another jann) takes a –4 circumstance penalty to its save."
  - name: "Elemental Resistance"
    desc: "The jann's elemental resistance applies to cold, electricity, and fire damage, as well as all damage from elemental sources (including environmental damage from the elemental planes and damage from anything with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Metal|metal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Wood|wood]] trait)."
speed: "25 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d6+7 slashing plus All Made One"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4+7 bludgeoning plus All Made One"
  - name: "Ranged"
    desc: "⬻ composite shortbow +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+5 piercing plus All Made One"
abilities_bot:
  - name: "All Made One"
    desc: "⬻ The jann calls upon all of the elements that make up their being to gain an additional arcane spell they can cast at will and empower their Strikes with the element, dealing an extra 1d4 damage of the listed type. These benefits last until the jann uses this ability again."
  - name: "Air"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Tailwind|_tailwind_]], 1d4 electricity"
  - name: "Earth"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Pummeling Rubble|_pummeling rubble_]], 1d4 bludgeoning"
  - name: "Fire"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Breathe Fire|_breathe fire_]], 1d4 fire"
  - name: "Metal"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Thunderstrike|_thunderstrike_]], 1d4 electricity"
  - name: "Water"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|_hydraulic push_]], 1d4 bludgeoning"
  - name: "Wood"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Summon Plant or Fungus|_summon plant or fungus_]], 1d4 piercing."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The jann transforms into any Small or Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]]. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Wanderer's Wish"
    desc: "⬽"
  - name: "Frequency"
    desc: "three times per year"
  - name: "Effect"
    desc: "The jann instantly grants the benefits of a critical success with the [[srd/pf2e/compendium/spells/rituals/Wish|_wish_]] ritual to a mortal creature. This has no cost. That creature specifies what they wish for, but the interpretation is up to the jann. A jann typically attempts to grant wishes in a way that encourages growth and exploration. A summoned jann can't use this ability. Jann Shuyookhs Jann shuyookhs add the following innate spells: __4th__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|_invisibility_]] (×2), [[srd/pf2e/compendium/spells/rank-4/Read Omens|_read omens_]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×2) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/equipment/runes/Astral|Astral Plane]]; Elemental Planes; or [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 156."
```

```encounter-table
name: Jann
creatures:
  - 1: Jann
```
