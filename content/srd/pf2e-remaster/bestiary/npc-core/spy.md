---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spy"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Spy"
level: 6
source: "NPC Core"
aon_id: "creature-3421"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3421"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Spy"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Deception +16, Diplomacy +14, Intimidation +14, Local Court Lore +16, Society +14, Stealth +16, Thievery +14"
abilityMods: [0, 4, 0, 2, 2, 4]
abilities_top:
  - name: "Noble's Ally"
    desc: "The spy has positioned themself to seem a trusted ally, gaining a +2 circumstance bonus to Gather Information or to Make an Impression among the nobles of that court."
  - name: "Items"
    desc: "Dagger (4), Disguise Kit, fine clothes, Leather Armor, _+1 rapier_, Thieves' Toolkit"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +16; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 (deadly d8, Disarm, Finesse, Magical) __Damage__ 1d6+7 piercing"
  - name: "Melee"
    desc: "⬻ dagger +16 (Agile, Finesse, versatile S) __Damage__ 1d4+7 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +16 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+7 piercing"
abilities_bot:
  - name: "Hidden Blade"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The spy draws a weapon and then Strikes with it. The target of the Strike is off-guard against the attack."
  - name: "Sneak Attack"
    desc: "The spy deals an extra 2d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 15."
```

```encounter-table
name: Spy
creatures:
  - 1: Spy
```
