---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Gamekeeper"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Gamekeeper"
level: 4
source: "NPC Core"
aon_id: "creature-3663"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3663"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Orc Gamekeeper"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Orcish|Orcish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [3, 4, 0, 0, 3, 1]
abilities_top:
  - name: "Insistent Command"
    desc: "When the gamekeeper rolls a success to [[srd/pf2e/compendium/rules-elements/actions/player-core#Command an Animal|Command an Animal]], they get a critical success instead; if they roll a critical failure, they get a failure instead."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sling/bola|Bola]] (4), [[srd/pf2e/compendium/equipment/snares/hampering-snare|hampering snare]] (2), Net, Whip"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +12; __Will__: +9"
hp: 65
health:
  - name: "HP"
    desc: "65"
abilities_mid:
  - name: "Play Chicken"
    desc: "⬲"
  - name: "Trigger"
    desc: "An adjacent enemy misses the gamekeeper with a melee attack"
  - name: "Effect"
    desc: "The gamekeeper attempts to capture the flailing assailant. They attempt an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] the attacker."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+9 slashing"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ bola +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/ranged-trip|Ranged Trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+9 bludgeoning"
abilities_bot:
  - name: "Animal Tandem"
    desc: "⬺ The orc gamekeeper makes a Strike against a creature adjacent to one of the gamekeeper's animal allies. If it hits, the animal ally deals one die of damage to the target, using the highest damage die among its unarmed attacks."
sourcebook: "_NPC Core_, page 206."
```

```encounter-table
name: Orc Gamekeeper
creatures:
  - 1: Orc Gamekeeper
```
