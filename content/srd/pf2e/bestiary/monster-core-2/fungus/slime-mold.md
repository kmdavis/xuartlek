---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Slime Mold"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/large
statblock: inline
name: "Slime Mold"
level: 2
source: "Monster Core 2"
aon_id: "creature-4497"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4497"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Slime Mold"
level: "Creature 2"
size: "Large"
trait_01: "Fungus"
trait_02: "Mindless"
trait_03: "Ooze"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; motion sense 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [3, 0, 5, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A slime mold can sense nearby creatures through vibration and air or water movement."
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +11; __Ref__: +3; __Will__: +4"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Critical Hits|critical hits]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
speed: "10 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +8 __Damage__ 1d8+3 bludgeoning plus slime rot"
abilities_bot:
  - name: "Slime Rot"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Onset"
    desc: "1d4 days"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 and [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (1 day)"
  - name: "Stage 2"
    desc: "as stage 1 (1 day)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1, enfeebled 2, and sickened 2 (1 day)"
  - name: "Stage 4"
    desc: "as stage 3 (1 day)"
  - name: "Stage 5"
    desc: "drained 2 plus [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] (no [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] check to wake up) (1 day)"
  - name: "Stage 6"
    desc: "dead, and the body erupts to release a new slime mold Slime Mold Fungi The particularly foul environments in which slime molds dwell are conducive to the growth of extremely potent and dangerous mushrooms and other fungi. A dead slime mold can be a source of enough materials to produce a few doses of [[srd/pf2e/compendium/equipment/alchemical-items/deathcap-powder-equipment-3331|deathcap powder]] or other types of poison. Some creatures, such as deros or those with inherent immunity to [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], cultivate slime molds to harvest these materials."
sourcebook: "_Monster Core 2_, page 241."
```

```encounter-table
name: Slime Mold
creatures:
  - 1: Slime Mold
```
