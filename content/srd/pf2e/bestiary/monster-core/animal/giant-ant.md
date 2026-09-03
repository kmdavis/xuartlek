---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Ant"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Ant"
level: 2
source: "Monster Core"
aon_id: "creature-2824"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2824"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Ant"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [4, 1, 4, -5, 1, -4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +7; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "40 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +9 __Damage__ 1d8+4 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+4 piercing plus giant ant venom"
abilities_bot:
  - name: "Giant Ant Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d8 poison and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d10 poison and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "1d12 poison and enfeebled 3 (1 round)"
  - name: "Haul Away"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant ant has a Large or smaller creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The giant ant Strides up to its full Speed, carrying the grabbed creature with it. It is [[srd/pf2e/compendium/rules-elements/conditions#Encumbered|encumbered]] if the grabbed creature is Medium or larger. Giant Ant Hives Giant ants form vast underground colonies, excavating deep burrows or infesting existing caverns. Ants are omnivorous and cultivate fungus farms, but they are happy to eat whatever presents itself. Humanoids and their domesticated animals are easy fuel for the insectile machinery of their hives. Worker ants lack the sting of their warrior cousins, while elite drones fly on gossamer wings (fly Speed of 30 feet) to seek new food sources for their queen."
sourcebook: "_Monster Core_, page 21."
```

```encounter-table
name: Giant Ant
creatures:
  - 1: Giant Ant
```
