---
obsidianUIMode: preview
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
aon_id: "creature-3421"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3421"
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
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Local Court Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +14"
abilityMods: [0, 4, 0, 2, 2, 4]
abilities_top:
  - name: "Noble's Ally"
    desc: "The spy has positioned themself to seem a trusted ally, gaining a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] or to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] among the nobles of that court."
  - name: "Items"
    desc: "Dagger (4), Disguise Kit, [[srd/pf2e/compendium/equipment/adventuring-gear/clothing-desert|fine clothes]], Leather Armor, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/rapier|rapier]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
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
    desc: "⬻ _rapier_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d6+7 piercing"
  - name: "Melee"
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+7 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+7 piercing"
abilities_bot:
  - name: "Hidden Blade"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The spy draws a weapon and then Strikes with it. The target of the Strike is off-guard against the attack."
  - name: "Sneak Attack"
    desc: "The spy deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 15."
```

```encounter-table
name: Spy
creatures:
  - 1: Spy
```
