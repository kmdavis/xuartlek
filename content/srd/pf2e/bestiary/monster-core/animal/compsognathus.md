---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Compsognathus"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/tiny
statblock: inline
name: "Compsognathus"
level: -1
source: "Monster Core"
aon_id: "creature-2914"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2914"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Compsognathus"
level: "Creature -1"
size: "Tiny"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [0, 3, 2, -4, 2, -2]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +4; __Ref__: +7; __Will__: +4"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "30 feet, swim 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d6 piercing plus compsognathus venom"
abilities_bot:
  - name: "Compsognathus Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d8 poison damage and enfeebled 1 (1 round)"
sourcebook: "_Monster Core_, page 96."
```

```encounter-table
name: Compsognathus
creatures:
  - 1: Compsognathus
```
