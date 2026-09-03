---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Centipede"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Centipede"
level: -1
source: "Monster Core"
aon_id: "creature-2875"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2875"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Centipede"
level: "Creature -1"
size: "Medium"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +2, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [-1, 3, 1, -5, 1, -4]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +6; __Will__: +2"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4–1 piercing plus giant centipede venom"
abilities_bot:
  - name: "Giant Centipede Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 14 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 3"
    desc: "1d4 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], and [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] (1 round)"
sourcebook: "_Monster Core_, page 59."
```

```encounter-table
name: Giant Centipede
creatures:
  - 1: Giant Centipede
```
