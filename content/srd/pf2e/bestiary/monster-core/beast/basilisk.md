---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Basilisk"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/medium
statblock: inline
name: "Basilisk"
level: 5
source: "Monster Core"
aon_id: "creature-2847"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2847"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Basilisk"
level: "Creature 5"
size: "Medium"
trait_01: "Beast"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +8"
abilityMods: [4, -1, 5, -3, 2, 1]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +14; __Ref__: +8; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ petrified"
abilities_mid:
  - name: "Petrifying Glance"
    desc: "⬲ (arcane, aura, visual)"
  - name: "Trigger"
    desc: "A creature within 30 feet that the basilisk can see starts its turn"
  - name: "Effect"
    desc: "The target must attempt a DC 20 Fortitude save. If it fails, it's slowed 1 for 1 minute as its body slowly stiffens."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 __Damage__ 2d8+4 piercing"
abilities_bot:
  - name: "Petrifying Gaze"
    desc: "⬺ (Arcane, Concentrate, Incapacitation, Visual) The basilisk stares at a creature it can see within 30 feet. That creature must attempt a DC 22 Fortitude save. If it fails and has not already been slowed by Petrifying Glance or this ability, it becomes slowed 1. If the creature was already slowed by this ability or Petrifying Glance, a failed save causes the creature to be petrified permanently. A creature petrified in this manner that is coated (not just splashed) with fresh basilisk blood no more than 1 hour old is instantly restored to flesh. A single basilisk contains enough blood to coat 1d4 Medium creatures in this manner. Basilisk Lairs Basilisks can be found in almost any terrestrial environment, including caves, forests, hills, mountains, plains, and swamps. Their hides often bear complexions that allow them to more easily blend with their environments. As a result, forest-dwelling basilisks may have scales of a verdant emerald color to match surrounding vegetation, while a basilisk that lives in the desert may be a sandy brown or shale color."
sourcebook: "_Monster Core_, page 39."
```

```encounter-table
name: Basilisk
creatures:
  - 1: Basilisk
```
