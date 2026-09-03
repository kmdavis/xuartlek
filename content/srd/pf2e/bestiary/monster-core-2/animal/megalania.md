---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Megalania"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Megalania"
level: 7
source: "Monster Core 2"
aon_id: "creature-4468"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4468"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Megalania"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [7, 2, 4, -4, 2, -2]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +15; __Will__: +13"
hp: 125
health:
  - name: "HP"
    desc: "125"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+9 piercing plus Grab and megalania venom"
abilities_bot:
  - name: "Megalania Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage, clumsy 2, and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage, clumsy 3, and off.guard (1 round)"
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 2d10+7 bludgeoning"
sourcebook: "_Monster Core 2_, page 216."
```

```encounter-table
name: Megalania
creatures:
  - 1: Megalania
```
