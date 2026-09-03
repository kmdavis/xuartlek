---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Triceratops"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Triceratops"
level: 8
source: "Monster Core"
aon_id: "creature-2921"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2921"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Triceratops"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21"
abilityMods: [7, 0, 4, -4, 2, -1]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +12; __Will__: +14"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Frill Defense"
    desc: "⬲"
  - name: "Trigger"
    desc: "The rider is targeted with an attack"
  - name: "Requirements"
    desc: "A creature must be mounted on the triceratops"
  - name: "Effect"
    desc: "The triceratops intercepts the attack with its bony frill. The rider gains a +2 circumstance bonus to its AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horns +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+9 piercing plus Knockdown"
  - name: "Melee"
    desc: "⬻ foot +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+9 bludgeoning"
abilities_bot:
  - name: "Lumbering Charge"
    desc: "⬻ The triceratops Strides up to 10 feet and then makes a Strike."
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 26"
  - name: "Vicious Gore"
    desc: "A triceratops deals 2d6 extra persistent bleed damage to [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] targets it hits with its horns."
sourcebook: "_Monster Core_, page 99."
```

```encounter-table
name: Triceratops
creatures:
  - 1: Triceratops
```
