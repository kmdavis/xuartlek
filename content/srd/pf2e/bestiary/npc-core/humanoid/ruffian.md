---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ruffian"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Ruffian"
level: 2
source: "NPC Core"
aon_id: "creature-3427"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3427"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Ruffian"
level: "Creature 2"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [3, 2, 3, -1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Club, Sling (10 bullets), Studded Leather Armor"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +8; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +9 __Damage__ 1d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ club +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+5 bludgeoning"
abilities_bot:
  - name: "Brutal Beating"
    desc: "The ruffian's brutality shakes foes' confidence. When the ruffian deals damage on a critical hit, the target is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]], and the ruffian can push the target up to 10 feet."
  - name: "Combat Grab"
    desc: "⬻"
  - name: "Trigger"
    desc: "The ruffian has one hand free"
  - name: "Effect"
    desc: "The ruffian makes a melee Strike while keeping one hand free. If this Strike hits, the ruffian Grabs the target using their free hand. The creature remains [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] until the end of the ruffian's next turn or until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]], whichever comes first."
  - name: "Sneak Attack"
    desc: "The ruffian deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 19."
```

```encounter-table
name: Ruffian
creatures:
  - 1: Ruffian
```
