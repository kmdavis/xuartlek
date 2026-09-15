---
noteType: pf2eMonster
aliases: "Unsanctioned Sheriff"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Unsanctioned Sheriff"
level: 5
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3509"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Unsanctioned Sheriff"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; (15 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +13"
abilityMods: [4, 2, 2, 0, 2, 2]
abilities_top:
  - name: "Items"
    desc: "badge, Dueling Pistol (2, 20 rounds), Sap, Scale Mail"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +11; __Will__: +13"
hp: 75
health:
  - name: "HP"
    desc: "75"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sap +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d6+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dueling pistol +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/Concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fatal|fatal d10]], range increment 60 feet, reload 1) __Damage__ 1d6+5 piercing"
abilities_bot:
  - name: "Lay Down the Law"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Requirements"
    desc: "The sheriff's last action this turn was a successful Strike against a creature within 30 feet"
  - name: "Effect"
    desc: "The sheriff yells a command at the creature they hit. The target must succeed at a DC 22 Will save or spend the first action on its next turn doing as commanded (or all its actions on its next turn on a critical failure). The sheriff can command a creature to approach the sheriff, release what its holding, or drop prone. Regardless of the result of its save, the creature is temporarily immune for 10 minutes."
sourcebook: "_NPC Core_, page 78."
```

```encounter-table
name: Unsanctioned Sheriff
creatures:
  - 1: Unsanctioned Sheriff
```
