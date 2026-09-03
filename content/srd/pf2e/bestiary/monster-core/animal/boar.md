---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boar"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Boar"
level: 2
source: "Monster Core"
aon_id: "creature-2854"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2854"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Boar"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [4, 1, 4, -4, 2, -3]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +10; __Ref__: +5; __Will__: +8"
hp: 40
health:
  - name: "HP"
    desc: "40"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusk +10 __Damage__ 2d6+4 piercing"
abilities_bot:
  - name: "Boar Charge"
    desc: "⬺ The boar Strides twice and then makes a tusk Strike. As long as it moved at least 20 feet, it gains a +2 circumstance bonus to its attack roll."
sourcebook: "_Monster Core_, page 43."
```

```encounter-table
name: Boar
creatures:
  - 1: Boar
```
