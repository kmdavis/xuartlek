---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mammoth"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Mammoth"
level: 10
source: "Monster Core"
aon_id: "creature-2994"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2994"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mammoth"
level: "Creature 10"
size: "Huge"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +22, Survival +19"
abilityMods: [8, 1, 5, -4, 1, -2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +15; __Will__: +18 +2 status to all saves vs. cold"
hp: 190
health:
  - name: "HP"
    desc: "190"
abilities_mid:
  - name: "Cold Adaptation"
    desc: "The mammoth reduces the effects it suffers from cold environments by one step."
speed: "45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusk +22 (reach 15 feet) __Damage__ 3d8+12 piercing"
  - name: "Melee"
    desc: "⬻ trunk +22 (reach 15 feet) __Damage__ grabbing trunk"
  - name: "Melee"
    desc: "⬻ foot +22 (reach 10 feet) __Damage__ 2d10+12 bludgeoning"
abilities_bot:
  - name: "Dual Tusks"
    desc: "⬻ The mammoth makes two tusk Strikes, each against a different creature. This counts as one attack for the mammoth's multiple attack penalty, and the penalty doesn't increase until after both attacks."
  - name: "Grabbing Trunk"
    desc: "A Medium or smaller creature hit by the mammoth's trunk is grabbed. If the mammoth moves, it can bring the grabbed creature along with it."
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 28"
sourcebook: "_Monster Core_, page 150."
```

```encounter-table
name: Mammoth
creatures:
  - 1: Mammoth
```
