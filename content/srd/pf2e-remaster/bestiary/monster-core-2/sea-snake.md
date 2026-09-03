---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sea Snake"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Sea Snake"
level: 0
source: "Monster Core 2"
aon_id: "creature-4553"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4553"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sea Snake"
level: "Creature 0"
size: "Small"
trait_01: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +2, Stealth +5, Survival +5"
abilityMods: [0, 3, 1, -4, 1, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "The sea snake can hold its breath for about an hour."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +3"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Lash Out"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the sea snake's reach uses a move action"
  - name: "Effect"
    desc: "The sea snake makes a fangs Strike against the attacker."
speed: "15 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +7 (Agile, finesse) __Damage__ 1d8 piercing plus sea snake venom"
abilities_bot:
  - name: "Sea Snake Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and enfeebled 1 (1 round)"
sourcebook: "_Monster Core 2_, page 294."
```

```encounter-table
name: Sea Snake
creatures:
  - 1: Sea Snake
```
