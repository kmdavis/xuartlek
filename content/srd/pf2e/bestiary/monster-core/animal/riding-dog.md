---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Riding Dog"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Riding Dog"
level: 1
source: "Monster Core"
aon_id: "creature-2925"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2925"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Riding Dog"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [2, 2, 2, -4, 2, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +5; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 17"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Pack Attack"
    desc: "The dog's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the dog's allies."
sourcebook: "_Monster Core_, page 102."
```

```encounter-table
name: Riding Dog
creatures:
  - 1: Riding Dog
```
