---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mountain Guardian"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mountain Guardian"
level: 6
source: "NPC Core"
aon_id: "creature-3582"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3582"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mountain Guardian"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; tremorsense 10 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [4, 1, 4, 0, 1, 2]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +11 (+13 vs. damaging effects); __Will__: +11"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]] 6, [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 6"
abilities_mid:
  - name: "Kinetic Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 10 feet. Pieces of rock and earth float in the aura. The aura must be active for the guardian to use [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|impulse]] actions, and deactivates if the guardian uses an [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/overflow|overflow]] impulse, is [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|knocked out]], or Dismisses it. The guardian can Channel Elements to reactivate it."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ elemental blast +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|Impulse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d8+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ elemental blast +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|Impulse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], range increment 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d8 bludgeoning"
abilities_bot:
  - name: "Base Kinesis"
    desc: "⬺ The mountain guardian generates, moves, or suppresses up to 1 Bulk of naturally occurring earthen matter within 15 feet. Generating creates earthen matter, moving moves existing matter up to 20 feet into any direction, and suppressing destroys a piece of that element (which can't be a durable crafted good, only natural forms of the element)."
  - name: "Channel Elements"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mountain guardian reactivates their kinetic aura and can make an elemental blast Strike."
  - name: "Empowered Blast"
    desc: "⬺ The mountain guardian makes a melee or ranged elemental blast Strike with a +4 status bonus to damage."
  - name: "Tremor"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|Impulse]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/overflow|Overflow]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mountain guardian stomps on natural earth or stone, causing a localized tremor. All creatures in a 10-foot burst within 30 feet take 3d10 bludgeoning damage with a DC 24 basic Fortitude save. A creature hat critically fails is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. Earth and stone in the area is difficult terrain until the start of the mountain guardian's next turn."
  - name: "Weight of Stone"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|Impulse]], [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/overflow|Overflow]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mountain guardian calls down boulders in a cylinder 20 feet in diameter and 80 feet high within 120 feet. Each creature in the area takes 4d8 bludgeoning damage with a DC 24 basic Reflex save. A creature that fails is also pushed downward 40 feet (80 feet on a critical failure) without taking falling damage and can't leave the ground for 1 round. Kineticist Rules The mountain guardian is based on the [[srd/pf2e/compendium/character/classes/kineticist|kineticist]] class from _Pathfinder Rage of Elements_, though simplified for use and an NPC. Their actions with the [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/impulse|impulse]] trait can be used only if their kinetic aura is active and they have a hand free. When they use an action with the [[srd/pf2e/compendium/rules-elements/traits/rage-of-elements/overflow|overflow]] trait (Tremor or Weight of Stone), their kinetic aura deactivates until they Channel Elements."
sourcebook: "_NPC Core_, page 133."
```

```encounter-table
name: Mountain Guardian
creatures:
  - 1: Mountain Guardian
```
