---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Teacher"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Teacher"
level: -1
source: "NPC Core"
aon_id: "creature-3589"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3589"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Teacher"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 3 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Academia Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|one additional Lore]] +14"
abilityMods: [0, 0, -1, 4, 2, 3]
abilities_top:
  - name: "Academic Specialist"
    desc: "For academic encounters, a teacher is a 4th-level challenge."
  - name: "Font of Knowledge"
    desc: "The teacher can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] on any general subject with a +10 modifier."
  - name: "Inspirational Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 50 feet. Any of the teacher's students in the aura gain a +1 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]]."
  - name: "Items"
    desc: "cane (functions as [[srd/pf2e/compendium/equipment/weapons/club/staff|staff]]), textbook, Writing Set"
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +1; __Ref__: +2; __Will__: +6"
hp: 5
health:
  - name: "HP"
    desc: "5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ cane +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
sourcebook: "_NPC Core_, page 139."
```

```encounter-table
name: Teacher
creatures:
  - 1: Teacher
```
