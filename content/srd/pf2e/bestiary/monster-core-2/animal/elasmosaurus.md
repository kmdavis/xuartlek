---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elasmosaurus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Elasmosaurus"
level: 7
source: "Monster Core 2"
aon_id: "creature-4377"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4377"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Elasmosaurus"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +17"
abilityMods: [6, 4, 6, -4, 5, -1]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +13; __Will__: +16"
hp: 125
health:
  - name: "HP"
    desc: "125"
abilities_mid:
  - name: "Long Neck"
    desc: "An elasmosaurus's long neck allows it to interact with the surface while its body remains submerged underwater. While submerged no deeper than 15 feet underwater, an elasmosaurus can still stick its head up to breathe. An elasmosaurus gains cover against attacks made against creatures that are above the water's surface while it is underwater, even if its head is above the surface."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only."
speed: "5 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 (reach 15 feet) __Damage__ 2d12+10 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ paddle +16 __Damage__ 2d6+10 bludgeoning"
abilities_bot:
  - name: "Drag Below"
    desc: "⬻ (Attack) The elasmosaurus attempts an Athletics check against a grabbed foe's Fortitude DC. If the elasmosaurus succeeds, the foe is forcibly moved 5 feet toward the elasmosaurus's body. If the elasmosaurus critically succeeds, the foe is moved 10 feet toward the elasmosaurus's body."
  - name: "Thrashing Retreat"
    desc: "⬺ A swimming elasmosaurus thrashes the area around it as it attempts to flee. It makes two paddle Strikes, each of which must be against separate targets, and each of which takes the normal multiple attack penalty. It then Swims up to its swim Speed. This Swim does not trigger reactions based on movement. Other Aquatic Reptiles The elasmosaurus is but one of many types of aquatic reptiles found in primeval oceans or lost worlds. Some, like the ichthyosaurus, are almost fishlike in appearance. Others, such as the mosasaurus, are truly massive beasts capable of killing and eating whales."
sourcebook: "_Monster Core 2_, page 143."
```

```encounter-table
name: Elasmosaurus
creatures:
  - 1: Elasmosaurus
```
