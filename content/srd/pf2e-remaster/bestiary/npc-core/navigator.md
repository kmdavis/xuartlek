---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Navigator"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Navigator"
level: 2
source: "NPC Core"
aon_id: "creature-3598"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3598"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Navigator"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Nature +11, Sailing Lore +14, Society +8, Survival +9"
abilityMods: [0, 2, 1, 4, 3, 0]
abilities_top:
  - name: "Chart a Course"
    desc: "(concentrate) By spending 10 minutes of work and succeeding at a DC 22 Sailing Lore check, the navigator plots an optimal course. The severity of environmental conditions during the journey is reduced by one step for 24 hours (two steps on a critical success). This changes moderate damage to minor damage, winds that create greater difficult terrain cause only difficult terrain, and so on."
  - name: "Sailing Specialist"
    desc: "For encounters involving navigation or sailing, the navigator is a 4th-level challenge."
  - name: "Items"
    desc: "Dagger, scroll case with ship's charts, Writing Set"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +8; __Will__: +9"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4+4 piercing plus navigator's edge"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing plus navigator's edge"
abilities_bot:
  - name: "Navigator's Edge"
    desc: "The navigator's Strikes deal an additional 1d6 damage when on a ship."
sourcebook: "_NPC Core_, page 146."
```

```encounter-table
name: Navigator
creatures:
  - 1: Navigator
```
