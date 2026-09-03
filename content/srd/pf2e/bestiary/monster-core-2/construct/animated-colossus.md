---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Colossus"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Animated Colossus"
level: 15
source: "Monster Core 2"
aon_id: "creature-4061"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4061"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Animated Colossus"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +27"
abilityMods: [9, 2, 8, -5, 0, -5]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +31; __Ref__: +21; __Will__: +19 construct armor"
hp: 245
health:
  - name: "HP"
    desc: "245; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 15"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated colossus has Hardness. This Hardness reduces any damage the construct takes by an amount equal to the Hardness. Once an animated colossus is reduced to fewer than half its Hit Points or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 35."
  - name: "Enormous"
    desc: "An animated colossus takes up a space of 6 squares by 6 squares (30 feet by 30 feet) and is 100 feet tall."
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +32 (Magical, reach 30 feet) __Damage__ 3d12+17 bludgeoning plus Improved Grab"
  - name: "Melee"
    desc: "⬻ foot +32 (Agile, Magical, reach 20 feet) __Damage__ 3d8+17 bludgeoning"
abilities_bot:
  - name: "Colossus's Grasp"
    desc: "The colossus can Grab a creature using only one hand. It can move normally with a creature grabbed or restrained in its fist, carrying the creature along. If it has two creatures grabbed in this way, it can't use its fist Strike."
  - name: "Constrict"
    desc: "⬻ 3d12+11 bludgeoning, DC 36"
  - name: "Trample"
    desc: "⬽ (Attack) Huge or smaller, foot, DC 36"
sourcebook: "_Monster Core 2_, page 33."
```

```encounter-table
name: Animated Colossus
creatures:
  - 1: Animated Colossus
```
