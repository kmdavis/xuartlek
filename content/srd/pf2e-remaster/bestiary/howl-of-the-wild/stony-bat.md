---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stony Bat"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Stony Bat"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3285"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3285"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Stony Bat"
level: "Creature 3"
size: "Small"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; echolocation (precise) 30 ft"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Stealth +11"
abilityMods: [2, 4, 2, -3, 2, 1]
abilities_top:
  - name: "Echolocation"
    desc: "The stony bat can use hearing as a precise sense with the listed range."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +11; __Will__: +7"
hp: 48
health:
  - name: "HP"
    desc: "48; __Immunities__ petrification"
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 (Finesse) __Damage__ 2d8+2 piercing plus stone feast"
abilities_bot:
  - name: "Petrify Vapor"
    desc: "⬺ (Earth, Primal) The stony bat breathes petrifying gas in a 15-foot cone, too thin to harm creatures in the area. However, it petrifies ambient moisture, raining down a cascade of tiny stones onto any creatures in the space directly below the cone. The falling rocks deal 4d6 bludgeoning damage (DC 20 basic Reflex save). The stony bat can't use Petrify Vapor again for 1d4 rounds."
  - name: "Petrify Body Part"
    desc: "⬺ (Earth, Primal) The stony bat breathes a puff of petrifying gas onto an adjacent creature, targeting a specific body part. The target must succeed at a DC 20 Fortitude save or be partially petrified for 1 minute, with an effect varying with the body part targeted."
  - name: "Face"
    desc: "The creature's face stiffens and a film of stone partially blocks its vision. It is dazzled."
  - name: "Hand"
    desc: "One of the creature's hands is petrified. It cannot Release items from that hand or use the hand for fine manipulation. Attack rolls with weapons held in that hand take a –2 status penalty."
  - name: "Leg"
    desc: "A patch of the creature's leg becomes inflexible and heavy. It takes a –10 status penalty to its Speed. If all of the creature's legs become petrified in this way, the creature's Speed is reduced down to 5 feet. At the GM's discretion, a creature with movement that doesn't rely on legs, such as creatures that Fly with wings, don't take a penalty to these other Speeds."
  - name: "Stone Feast"
    desc: "The stony bat specifically targets petrified body parts, which it can consume, unlike flesh. The stony bat's jaws deal an extra 1d6 damage against a creature that has been petrified, either partially or completely, and ignore the Hardness of petrified creatures."
sourcebook: "_Howl of the Wild_, page 154."
```

```encounter-table
name: Stony Bat
creatures:
  - 1: Stony Bat
```
