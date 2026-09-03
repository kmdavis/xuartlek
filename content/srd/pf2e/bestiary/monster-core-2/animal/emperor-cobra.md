---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Emperor Cobra"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Emperor Cobra"
level: 5
source: "Monster Core 2"
aon_id: "creature-4556"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4556"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Emperor Cobra"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +13, Survival +11"
abilityMods: [6, 4, 4, -4, 2, -2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +11; __Will__: +9"
hp: 80
health:
  - name: "HP"
    desc: "80"
speed: "25 feet, climb 25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +15 (reach 10 feet) __Damage__ 2d8+8 piercing plus emperor cobra venom"
abilities_bot:
  - name: "Emperor Cobra Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d8 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d8 poison damage and drained 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage and drained 2 (1 round)"
  - name: "Flare Hood"
    desc: "⬻ (Emotion, fear, mental, visual) The emperor cobra flares its hood. Each non–emperor cobra creature within a 20-foot emanation must attempt a DC 22 Will save. The creature is then temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is frightened 3."
sourcebook: "_Monster Core 2_, page 295."
```

```encounter-table
name: Emperor Cobra
creatures:
  - 1: Emperor Cobra
```
