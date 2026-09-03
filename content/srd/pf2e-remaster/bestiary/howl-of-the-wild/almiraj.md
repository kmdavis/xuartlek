---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Almiraj"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Almiraj"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3253"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3253"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Almiraj"
level: "Creature 4"
size: "Small"
trait_01: "Animal"
trait_02: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; tremorsense (imprecise) 40 feet"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +10, Survival +8"
abilityMods: [5, 3, 4, -4, 0, 3]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +11; __Will__: +8"
hp: 63
health:
  - name: "HP"
    desc: "63"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 5 feet, DC 22. Creatures that critically fail are also fleeing for 1 round."
  - name: "Reactive Strike"
    desc: "⬲ Horn only. Fleeing creatures take an additional 1d6 persistent bleed damage. On a critical hit, the target is knocked prone."
speed: "35 feet, burrow 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +13 __Damage__ 2d8+7 slashing"
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d6+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +13 (Agile) __Damage__ 2d4+7 slashing"
abilities_bot:
  - name: "Final Shake"
    desc: "⬻"
  - name: "Requirements"
    desc: "The almiraj has a creature grabbed"
  - name: "Effect"
    desc: "The almiraj clamps its jaws down on the creature and shakes it vigorously, attempting to finish it off. The creature takes 2d6 bludgeoning damage and must succeed at a DC 20 Fortitude save or become enfeebled 1. Small or smaller creatures take a –2 circumstance penalty to their save."
  - name: "Goring Charge"
    desc: "⬺ The almiraj lowers its head and moves with ferocity toward its selected prey. The almiraj Strides twice. If it ends its movement within melee reach of at least one enemy, it makes a horn Strike against that enemy. This Strike deals an additional 1d6 persistent bleed damage."
  - name: "Into the Earth"
    desc: "⬻"
  - name: "Requirements"
    desc: "The almiraj has a Medium or smaller creature grabbed"
  - name: "Effect"
    desc: "The almiraj attempts to flee with its meal, burrowing into the ground. The grabbed creature must succeed at a DC 20 Reflex save or be dragged beneath the ground as the almiraj Burrows up to its Speed. If the target succeeds at its save, it Escapes and the almiraj continues burrowing as normal; if it fails, the grabbed creature must hold its breath or begin suffocating under the dirt."
sourcebook: "_Howl of the Wild_, page 124."
```

```encounter-table
name: Almiraj
creatures:
  - 1: Almiraj
```
