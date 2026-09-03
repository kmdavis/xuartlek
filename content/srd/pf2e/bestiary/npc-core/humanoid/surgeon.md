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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +16"
abilityMods: [1, 3, 1, 2, 4, 0]
abilities_top:
  - name: "Medical Specialist"
    desc: "In medical matters, a surgeon is a 6th-level challenge. Doctor's Hand When the surgeon rolls a critical failure on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Disease|Treat Disease]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Poison|Treat Poison]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Wounds|Treat Wounds]], they get a failure instead."
  - name: "Items"
    desc: "bonesaw (functions as a [[srd/pf2e/compendium/equipment/weapons/sword/temple-sword|temple sword]]), [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|Healer's Toolkit]], scalpel (3. functions as a [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]])"
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
    desc: "⬻ bonesaw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d8+1 slashing"
  - name: "Melee"
    desc: "⬻ scalpel +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ scalpel +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Medical Malpractice"
    desc: "⬻ The surgeon attempts a [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check against the Fortitude DC of one living creature they can see within 60 feet. On a success, the surgeon's melee Strikes deal an extra 1d6 precision damage against that creature (2d6 on a critical success) until 1 minute passes or the surgeon critically hits that creature, whichever comes first. Using this action again ends any previous one. A surgeon can target an individual creature no more than once per day with this ability."
sourcebook: "_NPC Core_, page 61."
```

```encounter-table
name: Surgeon
creatures:
  - 1: Surgeon
```
