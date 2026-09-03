---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Diver"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Diver"
level: 3
source: "NPC Core"
aon_id: "creature-3601"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3601"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Diver"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Ocean Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +9"
abilityMods: [3, 3, 2, 0, 2, 0]
abilities_top:
  - name: "Underwater Fighter"
    desc: "The diver isn't [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] underwater and doesn't take penalties for using a bludgeoning or slashing melee weapon in water."
  - name: "Items"
    desc: "Trident"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +12; __Will__: +6"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Underwater Awareness"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy Strikes the diver while they're underwater"
  - name: "Effect"
    desc: "The diver senses the movement of their enemy in the water and jerks back in time. They gain a +2 circumstance bonus to their AC against the triggering attack."
speed: "25 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trident +12 __Damage__ 1d8+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ trident +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "Dive"
    desc: "⬻ The diver moves up to twice their swim Speed downward."
sourcebook: "_NPC Core_, page 148."
```

```encounter-table
name: Diver
creatures:
  - 1: Diver
```
