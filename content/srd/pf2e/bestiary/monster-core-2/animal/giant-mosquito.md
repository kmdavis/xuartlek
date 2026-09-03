---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Mosquito"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Mosquito"
level: 6
source: "Monster Core 2"
aon_id: "creature-4482"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4482"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Mosquito"
level: "Creature 6"
size: "Medium"
trait_01: "Animal"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [4, 5, 2, -5, 2, -5]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +17; __Will__: +12"
hp: 80
health:
  - name: "HP"
    desc: "80"
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ proboscis +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d10+7 piercing plus Grab and septic malaria"
abilities_bot:
  - name: "Blood Drain"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant mosquito has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The giant mosquito uses its proboscis to drain blood from the grabbed or restrained creature. This deals 3d6 piercing damage (DC 24 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save), and the giant mosquito gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] equal to the damage dealt that last 1 minute. A creature that takes any damage from having its blood drained by a giant mosquito is [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 until it receives any kind or amount of healing."
  - name: "Septic Malaria"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) The victim can't reduce its sickened condition while it's affected by septic malaria"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Onset"
    desc: "1 day"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 and sickened 1 (1 day)"
  - name: "Stage 3"
    desc: "as stage 2 (1 day)"
  - name: "Stage 4"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] (1 day)"
  - name: "Stage 5"
    desc: "dead"
sourcebook: "_Monster Core 2_, page 228."
```

```encounter-table
name: Giant Mosquito
creatures:
  - 1: Giant Mosquito
```
