---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stegosaurus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Stegosaurus"
level: 7
source: "Monster Core"
aon_id: "creature-2920"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2920"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Stegosaurus"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20"
abilityMods: [7, 2, 4, -4, 2, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +13"
hp: 125
health:
  - name: "HP"
    desc: "125"
abilities_mid:
  - name: "Dorsal Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The stegosaurus is targeted with a melee attack"
  - name: "Effect"
    desc: "The stegosaurus leans its dorsal plates into the attack, gaining a +2 circumstance bonus to its AC against the triggering attack. If the attack misses, the stegosaurus Steps after the attack."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+9 piercing"
  - name: "Melee"
    desc: "⬻ foot +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+9 bludgeoning"
abilities_bot:
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 25"
sourcebook: "_Monster Core_, page 99."
```

```encounter-table
name: Stegosaurus
creatures:
  - 1: Stegosaurus
```
