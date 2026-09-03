---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Miner"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Miner"
level: 0
source: "NPC Core"
aon_id: "creature-3494"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3494"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Miner"
level: "Creature 0"
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
    desc: "Acrobatics +3, Athletics +6, Mining Lore +4, Survival +4"
abilityMods: [2, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Hammer, Lantern, miner's harness (functions as leather armor), Pick, Piton (5), Rope (100 feet)"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +5; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pick +6 (fatal d10) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Piton Pin"
    desc: "⬻ (Attack)"
  - name: "Requirements"
    desc: "The miner has their hammer in hand"
  - name: "Effect"
    desc: "The miner Interacts to draw a piton, then hammers it into a creature to pin them in place, attempting an Athletics check against the target's Reflex DC. On a hit, the target is immobilized until it removes the piton with a successful DC 10 Athletics check made as an Interact action."
sourcebook: "_NPC Core_, page 68."
```

```encounter-table
name: Miner
creatures:
  - 1: Miner
```
