---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bodyguard"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bodyguard"
level: 1
source: "NPC Core"
aon_id: "creature-3513"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3513"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bodyguard"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +2"
abilityMods: [4, 2, 3, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Greatclub, Sap, Sling, studded leather"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +7; __Will__: +4"
hp: 25
health:
  - name: "HP"
    desc: "25"
abilities_mid:
  - name: "Bodyguard's Reprisal"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature attacks the subject of bodyguard's defense"
  - name: "Effect"
    desc: "The bodyguard makes a Strike against the triggering creature."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatclub +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d10+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ sap +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d6+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ sling +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Bodyguard's Defense"
    desc: "⬻ The bodyguard grants an adjacent ally a +2 circumstance bonus to AC. This lasts until the start of the bodyguard's next turn or until the ally is no longer adjacent, whichever comes first."
sourcebook: "_NPC Core_, page 82."
```

```encounter-table
name: Bodyguard
creatures:
  - 1: Bodyguard
```
