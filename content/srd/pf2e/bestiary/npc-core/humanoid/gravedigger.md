---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gravedigger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gravedigger"
level: 1
source: "NPC Core"
aon_id: "creature-3495"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3495"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gravedigger"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Graveyard Lore]] +7, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +4"
abilityMods: [4, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "bull's-eye lantern (2 oils), gravedigger's garb (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), [[srd/pf2e/compendium/equipment/adventuring-gear/religious-symbol-silver|religious symbol]] of Pharasma, shovel"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +4; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] 2"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shovel +9 __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
abilities_bot:
  - name: "Light in the Dark"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|Vitality]])"
  - name: "Requirements"
    desc: "The gravedigger is holding a [[srd/pf2e/compendium/equipment/adventuring-gear/lantern-hooded|bull's-eye lantern]] in one hand and their [[srd/pf2e/compendium/equipment/adventuring-gear/religious-symbol-silver|religious symbol]] in the other, and the lantern contains [[srd/pf2e/compendium/equipment/adventuring-gear/oil|oil]]"
  - name: "Effect"
    desc: "The gravedigger recites a brief chant to ignite their lantern with vital energy. Each [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]] creature in a 15-foot line takes 3d6 vitality damage with a DC 14 basic Fortitude save. This action uses all remaining oil in the bull's-eye lantern."
sourcebook: "_NPC Core_, page 69."
```

```encounter-table
name: Gravedigger
creatures:
  - 1: Gravedigger
```
