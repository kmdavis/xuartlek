---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tooth Fairy Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Tooth Fairy Swarm"
level: 3
source: "Monster Core"
aon_id: "creature-3217"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3217"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tooth Fairy Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Fey"
trait_02: "Swarm"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Stealth +10, Thievery +12"
abilityMods: [-2, 3, 0, -1, 2, 2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +10; __Will__: +7"
hp: 28
health:
  - name: "HP"
    desc: "28; __Immunities__ grabbed, precision, prone, restrained, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, cold iron 5, splash damage 5"
abilities_mid:
  - name: "Plaque Burst"
    desc: "When killed, a tooth fairy bursts into sticky, foul-smelling white dust. Each creature in a 15-foot emanation must succeed at a DC 20 Fortitude save or become sickened 1 (sickened 2 on a critical failure)."
speed: "10 feet, fly 40 feet"
abilities_bot:
  - name: "Pinch"
    desc: "⬻ Tooth fairies pinch their victims' fingers, noses, ears, or similar protruding body parts. Each enemy in the swarm's space takes 2d6 bludgeoning damage (DC 20 basic Reflex save). Creatures that critically fail this save are sickened 1 from the pain."
  - name: "Pry"
    desc: "⬽ The tooth fairies try to pry out one of their target's teeth. One enemy in the swarm's space takes 4d6 bludgeoning damage with a DC 20 basic Reflex save. On a failed save, the target takes 2 persistent bleed damage and loses a tooth. If the creature loses a tooth, it takes a –1 status penalty to Charisma-based skill checks and must succeed at a DC 5 flat check to Cast a Spell unless that spell has the subtle trait. These effects last for 1 day, or until the stolen tooth is returned and the target regains at least 1 Hit Point."
sourcebook: "_Monster Core_, page 327."
```

```encounter-table
name: Tooth Fairy Swarm
creatures:
  - 1: Tooth Fairy Swarm
```
