---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hunting Spider"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Hunting Spider"
level: 1
source: "Monster Core"
aon_id: "creature-3207"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3207"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hunting Spider"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, web sense"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +5, Stealth +7"
abilityMods: [2, 4, 1, -5, 2, -4]
abilities_top:
  - name: "Web Sense"
    desc: "The spider has imprecise tremorsense to detect the vibrations of creatures touching its web."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +9; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Spring Upon Prey"
    desc: "⬲"
  - name: "Requirements"
    desc: "Initiative has not yet been rolled"
  - name: "Trigger"
    desc: "A creature touches the hunting spider's web while the spider is on it"
  - name: "Effect"
    desc: "The hunting spider automatically notices the creature and Strides, Climbs, or Descends on a Web before it rolls initiative."
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +9 (Finesse) __Damage__ 1d6+2 piercing plus hunting spider venom"
  - name: "Ranged"
    desc: "⬻ web +7 (range increment 30 feet) __Damage__ web trap"
abilities_bot:
  - name: "Descend on a Web"
    desc: "⬻ (Move) The hunting spider moves straight down up to 40 feet, suspended by a web line. It can hang from the web or drop off. The distance it Descends on a Web doesn't count for falling damage. A creature that successfully Strikes the web (AC 20, Hardness 3, 5 HP) severs it, causing the spider to fall."
  - name: "Hunting Spider Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and off-guard (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage, clumsy 1, and off-guard (1 round)"
  - name: "Stage 3"
    desc: "1d6 poison damage, clumsy 2, and off-guard (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the hunting spider's web Strike is immobilized and stuck to the nearest surface until it Escapes (DC 17)."
sourcebook: "_Monster Core_, page 320."
```

```encounter-table
name: Hunting Spider
creatures:
  - 1: Hunting Spider
```
