---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Carnotaurus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Carnotaurus"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3263"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3263"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Carnotaurus"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +18, Survival +14"
abilityMods: [7, 2, 4, -4, 2, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +15; __Will__: +13"
hp: 145
health:
  - name: "HP"
    desc: "145"
abilities_mid:
  - name: "Headbutt"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature ends a move action within reach of the carnotaurus's horn Strike"
  - name: "Effect"
    desc: "The carnotaurus makes a horn Strike against the triggering creature."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 (reach 15 feet) __Damage__ 2d10+9 piercing plus vicious mauling"
  - name: "Melee"
    desc: "⬻ horn +18 (reach 15 feet) __Damage__ 1d12+9 piercing"
abilities_bot:
  - name: "Powerful Charge"
    desc: "⬺ The carnotaurus lowers its horns and surges toward a foe. It Strides twice, then makes a horn Strike. If it moved at least 20 feet from its starting position, the Strike's damage is increased to 2d12+9 and knocks the target prone if successful."
  - name: "Vicious Mauling"
    desc: "The carnotaurus's jaws Strike deals an additional 1d8 persistent bleed damage to prone targets."
sourcebook: "_Howl of the Wild_, page 137."
```

```encounter-table
name: Carnotaurus
creatures:
  - 1: Carnotaurus
```
