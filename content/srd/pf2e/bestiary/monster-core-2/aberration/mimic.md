---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mimic"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Mimic"
level: 4
source: "Monster Core 2"
aon_id: "creature-4475"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4475"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mimic"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +12, Deception +8, Dwelling Lore +10"
abilityMods: [4, 1, 3, 0, 1, 0]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +9; __Will__: +9"
hp: 75
health:
  - name: "HP"
    desc: "75"
abilities_mid:
  - name: "Object Lesson"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature touches or physically interacts with the mimic while the mimic is transformed using Mimic Object"
  - name: "Effect"
    desc: "The mimic makes a jaws Strike against the triggering creature. If initiative hasn't yet been rolled, the mimic then rolls initiative. Object Lesson can't be used again until the mimic escapes and takes on a new disguise."
speed: "10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 2d8+4 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ pseudopod +14 (Agile, reach 10 feet) __Damage__ 1d8+4 bludgeoning"
abilities_bot:
  - name: "Mimic Object"
    desc: "⬻ (Concentrate, polymorph) The mimic assumes the shape of any Medium object. This doesn't change the mimic's texture or overall size but can alter their coloration and visual appearance. They have an automatic result of 28 on Deception checks and DCs to pass as the object that they're mimicking."
  - name: "Mobile Morph"
    desc: "⬻ The mimic transforms part of their body into climbing claws, wings, or paddles. Until the end of their turn, they gain a climb, fly, or swim Speed of 40 feet. This speed is halved if the mimic has a creature swallowed. If they're in the air at the end of their turn, they fall as normal."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Medium, 2d8 acid, Rupture 13 Creative Mimics The older the mimic, the more creative its guise, but within practical limits. For example, a mimic can appear as a neatly organized bookshelf with a single book out of place, a dried-up cistern with something glittering at its center, or an inconspicuous wooden door with a conveniently placed peephole."
sourcebook: "_Monster Core 2_, page 223."
```

```encounter-table
name: Mimic
creatures:
  - 1: Mimic
```
