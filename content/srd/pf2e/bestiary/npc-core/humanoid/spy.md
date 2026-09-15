---
noteType: pf2eMonster
aliases: "Spy"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Spy"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3421"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Spy"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|Local Court Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +14, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +16, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +14"
abilityMods: [0, 4, 0, 2, 2, 4]
abilities_top:
  - name: "Noble's Ally"
    desc: "The spy has positioned themself to seem a trusted ally, gaining a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] or to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] among the nobles of that court."
  - name: "Items"
    desc: "Dagger (4), Disguise Kit, [[srd/pf2e/compendium/equipment/adventuring-gear/Clothing|fine clothes]], Leather Armor, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/Rapier|rapier]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/Thieves' Toolkit|Thieves' Toolkit]]"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +16; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d6+7 piercing"
  - name: "Melee"
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+7 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+7 piercing"
abilities_bot:
  - name: "Hidden Blade"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The spy draws a weapon and then Strikes with it. The target of the Strike is off-guard against the attack."
  - name: "Sneak Attack"
    desc: "The spy deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 15."
```

```encounter-table
name: Spy
creatures:
  - 1: Spy
```
