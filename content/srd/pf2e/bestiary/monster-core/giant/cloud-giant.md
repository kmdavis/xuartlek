---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cloud Giant"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/air
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/huge
statblock: inline
name: "Cloud Giant"
level: 11
source: "Monster Core"
aon_id: "creature-3015"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3015"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cloud Giant"
level: "Creature 11"
size: "Huge"
trait_01: "Air"
trait_02: "Giant"
trait_03: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; cloudsight, low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +26, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +21, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +21"
abilityMods: [7, 0, 5, 1, 3, 1]
abilities_top:
  - name: "Cloudsight"
    desc: "Cloud giants ignore [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]]from weather conditions, including clouds and rain."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/polearm/ranseur|ranseur]]_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +25; __Ref__: +18; __Will__: +21"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _ranseur_ +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d10+13 piercing"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+13 bludgeoning"
abilities_bot:
  - name: "Crushing Cloud"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The cloud giant solidifies some clouds, including fog or mist, around a creature that's already in a cloud up to 120 feet away. The target takes 3d8 bludgeoning damage (DC 30 basic Fortitude save). If it fails its save, it treats clouds as difficult terrain for 1 round."
  - name: "Wind Strike"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The cloud giant Strikes a creature with their ranseur, surrounded in a roar of rushing air. On a hit, the target takes an additional 4d8 bludgeoning damage and is [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]] for 1 minute. Whether or not the Strike hits, each non-cloud giant within a 20-foot emanation, including the target of the Strike, is buffeted by roaring winds and must attempt a DC 30 Fortitude saving throw."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes 2d8 sonic damage."
  - name: "Failure"
    desc: "The creature takes 4d8 sonic damage and is deafened until the end of its next turn."
  - name: "Critical Failure"
    desc: "As failure, but double damage and also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 30 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/mist|Mist]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/levitate|Levitate]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/vapor-form|Vapor Form]]"
sourcebook: "_Monster Core_, page 167."
```

```encounter-table
name: Cloud Giant
creatures:
  - 1: Cloud Giant
```
