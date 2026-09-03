---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mist Bear"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Mist Bear"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3273"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3273"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Mist Bear"
level: "Creature 7"
size: "Large"
trait_01: "Beast"
trait_02: "Ethereal"
trait_03: "Uncommon"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +17, Survival +15"
abilityMods: [6, 2, 5, -3, 4, 2]
abilities_top:
  - name: "Mist Form"
    desc: "(concentrate, exploration, occult, polymorph) Over the course of a minute, a mist bear can transmute its form into a cloud of ethereal vapor. In this state it has resistance 10 to physical damage, is immune to precision damage, and can't use any actions with the attack or manipulate trait. It has a fly Speed of 10 feet and can slip through tiny cracks. The mist bear can return to solid form as a single action."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +13; __Will__: +15"
hp: 140
health:
  - name: "HP"
    desc: "140"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 (Agile) __Damage__ 2d8+8 slashing plus Grab"
abilities_bot:
  - name: "Clouded Charge"
    desc: "⬺ (Concentrate, Occult, Visual) The mist bear Strides twice. During this movement, wisps of ethereal smoke trail from its body, making it concealed. The mist bear then Strikes. The target is off-guard to this attack if the bear moved at least 20 feet."
  - name: "Misty Mauling"
    desc: "⬻ (Concentrate, Occult, Polymorph)"
  - name: "Requirements"
    desc: "The mist bear has a creature grabbed"
  - name: "Effect"
    desc: "The mist bear digs its claws into the grabbed creature as it dissipates into mist. The grabbed creature takes 3d8 slashing damage (DC 25 basic Fortitude save). The mist bear gains the benefits of its Mist Form, Fliesup to 10 feet, and then returns to its solid form."
sourcebook: "_Howl of the Wild_, page 147."
```

```encounter-table
name: Mist Bear
creatures:
  - 1: Mist Bear
```
