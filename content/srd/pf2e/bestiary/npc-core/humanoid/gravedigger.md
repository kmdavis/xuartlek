---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3495"
socialImage: og-image.png
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
    desc: "+6"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Lore|Graveyard Lore]] +7, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +5, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +4"
abilityMods: [4, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "bull's-eye lantern (2 oils), gravedigger's garb (functions as [[srd/pf2e/compendium/equipment/Armor#Leather Armor|leather armor]]), [[srd/pf2e/compendium/equipment/adventuring-gear/Religious Symbol|religious symbol]] of [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Pharasma|Pharasma]], shovel"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +4; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 2"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shovel +9 __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
abilities_bot:
  - name: "Light in the Dark"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|Vitality]])"
  - name: "Requirements"
    desc: "The gravedigger is holding a [[srd/pf2e/compendium/equipment/adventuring-gear/Lantern|bull's-eye lantern]] in one hand and their [[srd/pf2e/compendium/equipment/adventuring-gear/Religious Symbol|religious symbol]] in the other, and the lantern contains [[srd/pf2e/compendium/equipment/adventuring-gear/Oil|oil]]"
  - name: "Effect"
    desc: "The gravedigger recites a brief chant to ignite their lantern with vital energy. Each [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] creature in a 15-foot line takes 3d6 vitality damage with a DC 14 basic Fortitude save. This action uses all remaining oil in the bull's-eye lantern."
sourcebook: "_NPC Core_, page 69."
```

```encounter-table
name: Gravedigger
creatures:
  - 1: Gravedigger
```
