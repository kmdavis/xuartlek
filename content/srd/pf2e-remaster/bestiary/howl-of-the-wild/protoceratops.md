---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Protoceratops"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/medium
statblock: inline
name: "Protoceratops"
level: 2
source: "Howl of the Wild"
aon_id: "creature-3261"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3261"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Protoceratops"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +8"
abilityMods: [4, 2, 3, -4, 2, 1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +8; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Frill Block"
    desc: "⬲"
  - name: "Requirements"
    desc: "The protoceratops is in its Defensive Posture"
  - name: "Trigger"
    desc: "An adjacent ally would take damage from a physical attack"
  - name: "Effect"
    desc: "The protoceratops partially blocks the blow with its frill, reducing the damage by 5."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ head +10 __Damage__ 1d8+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ tail +10 (Agile) __Damage__ 1d6+4 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Defensive Posture"
    desc: "⬻ The protoceratops tucks in its head and presents its sturdy frill, granting a +1 circumstance bonus to AC adjacent allies. The protoceratops remains in its Defensive Posture until the start of its next turn, but only grants the bonus while allies remain adjacent."
sourcebook: "_Howl of the Wild_, page 136."
```

```encounter-table
name: Protoceratops
creatures:
  - 1: Protoceratops
```
