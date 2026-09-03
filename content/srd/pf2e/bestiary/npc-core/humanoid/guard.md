---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Guard"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Guard"
level: 1
source: "NPC Core"
aon_id: "creature-3551"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3551"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Guard"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (8 to find concealed objects)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +3"
abilityMods: [3, 2, 2, 0, 2, -1]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), Dagger, Sap, Scale Mail, Signal Whistle"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +5; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sap +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +6 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing Raise The Alarm! In a settlement with an alarm, brawls, or other major disruptions trigger an alarm 1 round after the watch is alerted. Guards start to arrive after about 5 rounds, usually in patrols of 2 or 3 members, with larger groups of 8–12 near important locations."
sourcebook: "_NPC Core_, page 110."
```

```encounter-table
name: Guard
creatures:
  - 1: Guard
```
