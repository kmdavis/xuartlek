---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Snapdrake"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Snapdrake"
level: 8
source: "Rage of Elements"
aon_id: "creature-2677"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2677"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Snapdrake"
level: "Creature 8"
size: "Large"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Arboreal, Common, Muan; (can't speak any languages)"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Performance +16, Athletics +14"
abilityMods: [4, 6, 3, -2, 3, 4]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +11; __Will__: +19"
hp: 144
health:
  - name: "HP"
    desc: "144; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ axes 10, fire 10"
abilities_mid:
  - name: "Alluring Scent"
    desc: "(aura, olfactory, plant, primal) 30 feet. A creature that enters the emanation must attempt a DC 25 Will save. On a failure, the target is fascinated by the snapdrake and must use at least 1 action on its next turn to Stride closer to the snapdrake. On a success, the target is immune to the snapdrake's alluring scent for 1 hour."
  - name: "Reactive Strike"
    desc: "⬲ Tail scythe only"
speed: "20 feet, fly 50 feet; greater forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +14 __Damage__ 2d12+4 piercing plus Grab and snapdrake pollen"
  - name: "Melee"
    desc: "⬻ tail scythe +16 (deadly d10, Finesse, reach 10 feet) __Damage__ 2d10+6 slashing"
abilities_bot:
  - name: "Greater Forest Passage"
    desc: "The snapdrake ignores difficult terrain and greater difficult terrain from plants and fungi."
  - name: "Snapdrake Pollen"
    desc: "(Plant, Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "8 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage plus dazzled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage plus dazzled 1 and sickened 1 (2 rounds)"
  - name: "Stage 3"
    desc: "2d6 poison damage plus confused and sickened 1 (2 rounds)"
  - name: "Speed Surge"
    desc: "⬻ (Move)"
  - name: "Frequency"
    desc: "3 times per day"
  - name: "Effect"
    desc: "The snapdrake moves up to twice its Speed."
  - name: "Spray Pollen"
    desc: "⬺ (Arcane, Plant, Poison) The snapdrake breathes a blast of pollen in a 40-foot cone. Creatures caught in the blast must succeed at a DC 25 basic Reflex save or be exposed to snapdrake pollen. The snapdrake can't use Spray Pollen again for 1d6 rounds."
sourcebook: "_Rage of Elements_, page 209."
```

```encounter-table
name: Snapdrake
creatures:
  - 1: Snapdrake
```
