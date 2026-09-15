---
noteType: pf2eMonster
aliases: "Executioner"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Executioner"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3561"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Executioner"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +10"
abilityMods: [5, 2, 3, -1, 2, 2]
abilities_top:
  - name: "Items"
    desc: "chainmail, _+1 [[srd/pf2e/compendium/equipment/weapons/axe/Greataxe|greataxe]]_, hood"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +12; __Will__: +14"
hp: 105
health:
  - name: "HP"
    desc: "105"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greataxe_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d12+9 slashing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
abilities_bot:
  - name: "Behead"
    desc: "⬽"
  - name: "Requirements"
    desc: "The executioner is adjacent to a [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]] creature or a creature specifically prepared for a killing blow"
  - name: "Effect"
    desc: "The executioner Strikes the creature with their greataxe. On a hit, in addition to taking damage, the target must attempt a DC 23 Fortitude save or be reduced to 0 HP and become dying 1. If the creature was already dying (including if it was reduced to 0 HP by the Strike's damage), the creature's dying value increases by 1, in addition to any increase from the Strike. On a critical failure, the creature dies instantly. If the executioner's Strike was a critical hit, the target uses the outcome one degree of success worse than the result of their saving throw."
  - name: "Intimidating Strike"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The executioner makes a melee Strike. If it hits and deals damage, the target is [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]], or frightened 2 on a critical hit."
  - name: "Mark for Death"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The executioner marks a single creature they can see for death. The first time each round the executioner Strikes that creature, the Strike deals an extra 1d12 precision damage. The creature remains marked for death until the executioner is knocked out, marks a different creature for death, or the encounter ends."
sourcebook: "_NPC Core_, page 116."
```

```encounter-table
name: Executioner
creatures:
  - 1: Executioner
```
