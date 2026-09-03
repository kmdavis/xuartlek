---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ofalth"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Ofalth"
level: 10
source: "Monster Core"
aon_id: "creature-3117"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3117"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ofalth"
level: "Creature 10"
size: "Large"
trait_01: "Aberration"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
abilityMods: [7, 3, 6, -2, 2, -2]
abilities_top:
  - name: "Refuse Pile"
    desc: "When they're not in danger, an ofalth can spend 1 minute settling into a 10-foot pile that looks like a heap of garbage. Until the next time it takes an action, the ofalth gains a +2 circumstance bonus to AC. A creature that enters the area of the garbage heap or interacts with it must attempt a save against the ofalth's stench."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +22; __Ref__: +17; __Will__: +18"
hp: 170
health:
  - name: "HP"
    desc: "170 (filth wallow); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]"
abilities_mid:
  - name: "Filth Wallow"
    desc: "An ofalth gains fast healing 2 when in an area with a high concentration of debris or excrement, such as a refuse heap or sewer."
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 28"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+13 bludgeoning plus wretched weeps"
  - name: "Ranged"
    desc: "⬻ offal +19 (range increment 30 feet) __Damage__ 2d10+9 bludgeoning plus wretched weeps"
abilities_bot:
  - name: "Wretched Weeps"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "2d4 persistent bleed every hour and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 day)"
  - name: "Stage 3"
    desc: "2d6 persistent bleed every hour and enfeebled 2 (1 day)"
sourcebook: "_Monster Core_, page 249."
```

```encounter-table
name: Ofalth
creatures:
  - 1: Ofalth
```
