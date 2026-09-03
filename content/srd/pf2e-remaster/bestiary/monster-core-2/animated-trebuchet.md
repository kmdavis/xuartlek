---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Trebuchet"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Animated Trebuchet"
level: 13
source: "Monster Core 2"
aon_id: "creature-4060"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4060"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Animated Trebuchet"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +24"
abilityMods: [9, 2, 8, -5, 0, -5]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +29; __Ref__: +19; __Will__: +17 construct armor"
hp: 200
health:
  - name: "HP"
    desc: "200; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 14"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated trebuchet has Hardness. This Hardness reduces any damage the construct takes by an amount equal to the Hardness. Once an animated trebuchet is reduced to fewer than half its Hit Points or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 32."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ arm +27 (Magical, reach 15 feet) __Damage__ 3d12+11 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ rock +27 (Brutal, Magical, range increment 120 feet) __Damage__ 3d10+11 bludgeoning"
abilities_bot:
  - name: "Launch"
    desc: "⬻"
  - name: "Requirements"
    desc: "The animated trebuchet has a creature grabbed in its arm"
  - name: "Effect"
    desc: "The animated trebuchet attempts an Athletics check against the grabbed creature's Fortitude DC. On a success, it fires the creature up to 40 feet in height and up to 120 feet away. The creature takes 4d12 bludgeoning damage plus the appropriate falling damage. If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage (DC 33 basic Reflex save). On a successful Launch, the animated trebuchet must Interact to reposition its arm into the proper position before it can Launch again."
  - name: "Trample"
    desc: "⬽ (Attack) Large or smaller, arm, DC 33"
sourcebook: "_Monster Core 2_, page 33."
```

```encounter-table
name: Animated Trebuchet
creatures:
  - 1: Animated Trebuchet
```
