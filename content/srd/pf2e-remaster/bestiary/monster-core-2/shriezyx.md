---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shriezyx"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Shriezyx"
level: 4
source: "Monster Core 2"
aon_id: "creature-4544"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4544"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shriezyx"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +12"
abilityMods: [3, 5, 4, -4, 2, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +12; __Will__: +8 +1 status to all saves vs. mental"
hp: 70
health:
  - name: "HP"
    desc: "70; __Resistances__ poison 6; __Weaknesses__ fire 6"
abilities_mid:
  - name: "Pyrophobia"
    desc: "If the shriezyx takes fire damage or starts its turn within 30 feet of a fire at least the size of a torch, it becomes frightened 1."
speed: "35 feet; climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +13 (Finesse) __Damage__ 2d6+5 piercing damage plus numbing toxin"
  - name: "Melee"
    desc: "⬻ claw +13 (Agile, finesse) __Damage__ 2d4+5 slashing damage"
abilities_bot:
  - name: "Clicking Scurry"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The shriezyx Strides or Climbs, and then makes a claw Strike"
  - name: "Flesh Web"
    desc: "⬺ The shriezyx's shoots a fleshy web at a target within 30 feet. The target must succeed at a DC 20 Reflex save or become immobilized and exposed to numbing toxin. Due to the grotesque nature of the webbing, the target becomes sickened 1 and can't reduce its sickened condition until it Escapes (DC 20)."
  - name: "Numbing Toxin"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "1d8 poison damage, clumsy 2, and slowed 1 (1 round) Infestation Problems Shriezyx are resilient, and even if trapped in collapses, they can survive for an extraordinary length of time with little to eat. When a public works project in Magnimar revealed a cavern in the Irespan, swarms of shriezyx were let loose in the city. Since then, it's common practice to use specialized tools to listen for the telltale sounds of a shriezyx's clicking claws before demolishing any old, hollowed structures or bunkers."
sourcebook: "_Monster Core 2_, page 286."
```

```encounter-table
name: Shriezyx
creatures:
  - 1: Shriezyx
```
