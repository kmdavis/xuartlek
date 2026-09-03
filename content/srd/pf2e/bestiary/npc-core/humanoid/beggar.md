---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Beggar"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Beggar"
level: -1
source: "NPC Core"
aon_id: "creature-3452"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3452"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Beggar"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +3, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +2"
abilityMods: [1, 3, 2, 0, 1, 1]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +4; __Ref__: +7; __Will__: +3"
hp: 10
health:
  - name: "HP"
    desc: "10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4+1 bludgeoning"
abilities_bot:
  - name: "Beat a Retreat"
    desc: "⬺ The beggar Strides three times and gains a +2 circumstance bonus to AC during those actions."
sourcebook: "_NPC Core_, page 40."
```

```encounter-table
name: Beggar
creatures:
  - 1: Beggar
```
