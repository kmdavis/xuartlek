---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bandit"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bandit"
level: 2
source: "NPC Core"
aon_id: "creature-3425"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3425"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bandit"
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
    desc: "Athletics +6, Deception +5, Forest Lore +4, Intimidation +6, Stealth +8, Survival +6, Thievery +8"
abilityMods: [3, 3, 1, 0, 2, 1]
abilities_top:
  - name: "Bandit's Ambush"
    desc: "When the bandit rolls initiative using Deception or Stealth, they can attempt to Demoralize one creature as a free action."
  - name: "Items"
    desc: "Dagger, Machete, Sling (10 bullets), studded leather"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +9; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ machete +9 (deadly d8, Sweep) __Damage__ 1d6+5 slashing"
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, versatile S) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +9 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+5 piercing"
abilities_bot:
  - name: "Dread Striker"
    desc: "Frightened creatures are off-guard to the bandit."
  - name: "Forest Passage"
    desc: "The bandit ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 18."
```

```encounter-table
name: Bandit
creatures:
  - 1: Bandit
```
