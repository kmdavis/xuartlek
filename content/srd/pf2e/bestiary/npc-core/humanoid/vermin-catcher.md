---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vermin Catcher"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Vermin Catcher"
level: 2
source: "NPC Core"
aon_id: "creature-3499"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3499"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Vermin Catcher"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +9, Nature +6, Stealth +8, Survival +6, Vermin Lore +9"
abilityMods: [3, 2, 4, 1, 0, -2]
abilities_top:
  - name: "Items"
    desc: "Arsenic, Club, Leather Armor, rat traps (4)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +8; __Will__: +6"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +9 __Damage__ 1d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ club +8 (thrown 10 feet) __Damage__ 1d6+5 bludgeoning"
abilities_bot:
  - name: "Giant Rat Trap"
    desc: "⬽ The vermin catcher places a rat trap in an adjacent space. Any Small or Medium creature that moves into the space with the trap triggers it and must attempt a DC 18 basic Reflex save. On a failure, the creature takes 1d4 persistent bleed damage (2d4 on a critical failure) and is immobilized and off-guard for 1 round."
  - name: "Sneak Attack"
    desc: "The vermin catcher deals 1d6 extra precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 71."
```

```encounter-table
name: Vermin Catcher
creatures:
  - 1: Vermin Catcher
```
