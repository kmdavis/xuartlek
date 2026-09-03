---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Feathered Bear"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/large
statblock: inline
name: "Feathered Bear"
level: 10
source: "Monster Core 2"
aon_id: "creature-4565"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4565"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Feathered Bear"
level: "Creature 10"
size: "Large"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [7, 2, 5, 0, 2, 3]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +16; __Will__: +18"
hp: 160
health:
  - name: "HP"
    desc: "160; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision; __Resistances__ all damage 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]], [[srd/pf2e/compendium/equipment/runes/ghost-touch|_ghost touch_]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]; double resistance vs. non-magical)"
abilities_mid:
  - name: "Guardian's Aegis"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 30 feet. All allies within 30 feet of the feathered bear gain a +1 status bonus to saves against magical effects. The bonus increases to +2 if the effect originated from a [[srd/pf2e/compendium/rules-elements/traits/player-core/fiend|fiend]]."
  - name: "Avenging Claws"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet damages the feathered bear's ally with a melee attack"
  - name: "Effect"
    desc: "The feathered bear immediately [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Steps]] toward the triggering attacker and makes a claws Strike."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d10+9 force"
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d6+9 force plus Grab"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The spirit guide forms a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 20, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. This bond strengthens the spirit guide's connection to the [[srd/pf2e/compendium/gm/planes#The Universe|Universe]]. While bonded, the spirit guide loses the [[srd/pf2e/compendium/rules-elements/traits/gm-core/incorporeal|incorporeal]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] traits, loses their immunities and resistances, and changes their Strikes to deal the appropriate physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "⬺"
  - name: "Requirements"
    desc: "The spirit guide is currently Bonded with a Mortal"
  - name: "Effect"
    desc: "The spirit guide makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
  - name: "Mauler"
    desc: "The feathered bear gains a +4 circumstance bonus to damage rolls against creatures they've [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/environmental-endurance|Environmental Endurance]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-1/jump|Jump]], [[srd/pf2e/compendium/spells/rank-2/oaken-resilience|Oaken Resilience]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 305."
```

```encounter-table
name: Feathered Bear
creatures:
  - 1: Feathered Bear
```
