---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Smoke Creeper"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/large
statblock: inline
name: "Smoke Creeper"
level: 6
source: "Monster Core 2"
aon_id: "creature-4380"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4380"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Smoke Creeper"
level: "Creature 6"
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, smoke vision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Stealth +15"
abilityMods: [1, 5, 3, -2, 4, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The smoke creeper ignores the concealed condition from smoke."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +17; __Will__: +11"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ bleed, paralyzed, poison, precision, sleep; __Resistances__ fire 5"
abilities_mid:
  - name: "Smoke Form"
    desc: "The smoke creeper can move through the spaces of other creatures but can't end its movement in the same space."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ smoke mandibles +17 (Agile, finesse) __Damage__ 2d8+3 piercing plus 1d6 poison"
abilities_bot:
  - name: "Choking Swoop"
    desc: "⬽ The smoke creeper Flies up to its Speed, moving through the spaces of other creatures and leaving traces of itself behind. Each breathing creature it passes through must attempt a DC 23 Fortitude save. On a failure, the creature inhales part of the elemental and is immobilized for 1 minute by the pain of the smoke rasping in its throat and lungs. A creature can attempt to end this condition by spending an action coughing and succeeding at a DC 23 Fortitude save."
  - name: "Painful Exhalations"
    desc: "⬺"
  - name: "Requirements"
    desc: "At least one creature within 40 feet is immobilized from the smoke creeper's Choking Swoop"
  - name: "Effect"
    desc: "The smoke creeper flaps its wings, violently drawing the lingering smoke free from all creatures immobilized from its Choking Swoop within 40 feet. Each target must attempt a DC 23 Fortitude save. On a failure, the creature is enfeebled 1 for 1 minute and sickened 1 (enfeebled 2 and sickened 2 on a critical failure). Regardless of the result, the creature is no longer immobilized from the smoke creeper's Choking Swoop. Air And Smoke Elementals of smoke, such as the smoke creeper, are often cruel in their attacks on breathing creatures, causing them to choke and cough from their noxious fumes. Some believe that they hold secret allegiances to Ymeri, who holds domain over fire and smoke."
sourcebook: "_Monster Core 2_, page 144."
```

```encounter-table
name: Smoke Creeper
creatures:
  - 1: Smoke Creeper
```
