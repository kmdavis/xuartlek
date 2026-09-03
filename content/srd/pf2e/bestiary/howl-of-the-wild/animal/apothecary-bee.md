---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Apothecary Bee"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Apothecary Bee"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3254"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3254"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Apothecary Bee"
level: "Creature 7"
size: "Tiny"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, potionsight (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Stealth +17, Thievery +15"
abilityMods: [1, 6, 3, -4, 2, 2]
abilities_top:
  - name: "Internal Cauldron"
    desc: "With an appropriate diet, an apothecary bee will create a potion of 6th level or lower every two weeks. Most often, this is a _moderate healing potion_. Each apothecary bee can store only one completed potion at a time. Unused potions can generally be harvested from an apothecary bee with a successful DC 23 Nature or Survival check."
  - name: "Potionsight"
    desc: "Apothecary bees' complex eyes let them see the auras of magical potions and instinctively identify potions of their level or lower. These auras are visible through mundane containers, though their eyes have no special ability to perceive or identify non-magical solutions, such as alchemical elixirs."
  - name: "Items"
    desc: "_moderate healing potion_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +14; __Ref__: +19; __Will__: +13"
hp: 115
health:
  - name: "HP"
    desc: "115; __Weaknesses__ smoke susceptibility"
abilities_mid:
  - name: "Smoke Susceptibility"
    desc: "An apothecary bee is slowed 1 if it starts its turn in heavy smoke."
speed: "10 feet, climb 10 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stinger +19 (Magical, Poison) __Damage__ 1d4+4 piercing plus 3d6 poison"
abilities_bot:
  - name: "Drain Potion"
    desc: "⬺ (Manipulate)"
  - name: "Requirements"
    desc: "The apothecary bee has no stored potions"
  - name: "Effect"
    desc: "The apothecary bee slurps up a potion within its reach, storing it internally. A creature can attempt a DC 25 Reflex save to protect a potion in its possession."
  - name: "Ingest Potion"
    desc: "⬻ The apothecary bee consumes the potion it has stored in its body. If the potion has the healing trait, the apothecary bee heals for the maximum amount."
  - name: "Inject Potion"
    desc: "⬻ (Manipulate) The apothecary bee injects its stored potion into a willing creature within its reach. This deals 1 piercing damage and grants the recipient the normal effects of drinking the potion."
sourcebook: "_Howl of the Wild_, page 125."
```

```encounter-table
name: Apothecary Bee
creatures:
  - 1: Apothecary Bee
```
