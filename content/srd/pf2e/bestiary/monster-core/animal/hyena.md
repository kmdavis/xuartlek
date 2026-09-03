---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hyena"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Hyena"
level: 1
source: "Monster Core"
aon_id: "creature-3065"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3065"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hyena"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [3, 3, 2, -4, 1, -2]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +8; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d8+3 piercing plus Knockdown"
abilities_bot:
  - name: "Drag"
    desc: "⬻ The hyena makes a jaws Strike against a [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] enemy. If it hits, in addition to dealing damage, the hyena Strides up to 10 feet, dragging the enemy along."
  - name: "Pack Attack"
    desc: "The hyena deals an extra 1d4 damage to any creature that's within reach of at least two of the hyena's allies."
sourcebook: "_Monster Core_, page 205."
```

```encounter-table
name: Hyena
creatures:
  - 1: Hyena
```
