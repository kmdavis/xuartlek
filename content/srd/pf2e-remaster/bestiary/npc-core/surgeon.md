---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Surgeon"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Surgeon"
level: 2
source: "NPC Core"
aon_id: "creature-3482"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3482"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Surgeon"
level: "Creature 2"
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
    desc: "Crafting +10, Diplomacy +8, Medicine +16"
abilityMods: [1, 3, 1, 2, 4, 0]
abilities_top:
  - name: "Medical Specialist"
    desc: "In medical matters, a surgeon is a 6th-level challenge. Doctor's Hand When the surgeon rolls a critical failure on a check to Treat Disease, Treat Poison, or Treat Wounds, they get a failure instead."
  - name: "Items"
    desc: "bonesaw (functions as a temple sword), Healer's Toolkit, scalpel (3. functions as a dagger)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +7; __Will__: +10"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bonesaw +9 (Trip) __Damage__ 1d8+1 slashing"
  - name: "Melee"
    desc: "⬻ scalpel +11 (Agile, Finesse, versatile S) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ scalpel +11 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Medical Malpractice"
    desc: "⬻ The surgeon attempts a Medicine check against the Fortitude DC of one living creature they can see within 60 feet. On a success, the surgeon's melee Strikes deal an extra 1d6 precision damage against that creature (2d6 on a critical success) until 1 minute passes or the surgeon critically hits that creature, whichever comes first. Using this action again ends any previous one. A surgeon can target an individual creature no more than once per day with this ability."
sourcebook: "_NPC Core_, page 61."
```

```encounter-table
name: Surgeon
creatures:
  - 1: Surgeon
```
