---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Granite Glyptodont"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/large
statblock: inline
name: "Granite Glyptodont"
level: 8
source: "Monster Core 2"
aon_id: "creature-4385"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4385"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Granite Glyptodont"
level: "Creature 8"
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision, tremorsense (imprecise) 90 feet"
skills:
  - name: "Skills"
    desc: "Athletics +18"
abilityMods: [6, 1, 6, 0, 5, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +17"
hp: 145
health:
  - name: "HP"
    desc: "145; __Immunities__ bleed, paralyzed, poison, sleep"
speed: "30 feet, burrow 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ tail +20 (Forceful, reach 10 feet, versatile P) __Damage__ 2d12+9 bludgeoning plus calcification"
abilities_bot:
  - name: "Calcification"
    desc: "(Incapacitation, primal) A blow from a granite glyptodont's tail Strike hardens the flesh of the creature struck. The target must succeed at a DC 26 Fortitude save or become slowed 1 (slowed 2 on a critical failure). Further failed saves against calcification increase the value of the slowed condition. Once a creature's actions are reduced to 0 by calcification, that creature becomes petrified. If the creature isn't petrified, the slowed conditions end once 1 minute passes without the creature failing a save against calcification. Every 24 hours after it was petrified, the creature can attempt a DC 26 Fortitude save to recover. On a success, it becomes flesh again but is slowed 1 for the next 24 hours. On a critical success, the creature recovers and isn't slowed. On a failure, the creature remains petrified but can try again in 24 hours. On a critical failure, the petrification is permanent, and the creature can't attempt any more saves."
  - name: "Earth Glide"
    desc: "A granite glyptodont can Burrow through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
sourcebook: "_Monster Core 2_, page 147."
```

```encounter-table
name: Granite Glyptodont
creatures:
  - 1: Granite Glyptodont
```
