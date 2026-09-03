---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Torchbearer"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Torchbearer"
level: 0
source: "NPC Core"
aon_id: "creature-3466"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3466"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Torchbearer"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Architecture Lore +2, Athletics +4, Stealth +5, Survival +3"
abilityMods: [2, 3, 1, 0, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Climbing Kit, Dagger, Hand Crossbow (20 bolts), Matchstick (5), Torch (4)"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +9; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ torch +5 __Damage__ 1d6+2 bludgeoning plus 1 fire"
  - name: "Melee"
    desc: "⬻ dagger +6 (Agile, Finesse, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +6 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ hand crossbow +6 (range increment 60 feet, reload 1) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Torch Combatant"
    desc: "A torchbearer is adept at attacking with torches and deals 1 persistent fire damage when they critically hit a creature with a torch."
sourcebook: "_NPC Core_, page 52."
```

```encounter-table
name: Torchbearer
creatures:
  - 1: Torchbearer
```
