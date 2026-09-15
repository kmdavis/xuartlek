---
noteType: pf2eMonster
aliases: "Noble"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Noble"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3418"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Noble"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +10, [[srd/pf2e/compendium/rules-elements/skills/Lore|Games Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +10"
abilityMods: [2, 3, 1, 1, 2, 4]
abilities_top:
  - name: "Lip Reader"
    desc: "After years of sticking their nose where it doesn't belong, the noble has learned to read lips from afar. If they're trying to read lips in an encounter or attempting a difficult feat of lip reading, they are [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] and [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]], and might need to succeed at a [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] check with a DC determined by the GM."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Clothing|fashionable fine clothes]], [[srd/pf2e/compendium/equipment/adventuring-gear/Loaded Dice|Loaded Dice]], Rapier, silver flask, signet ring"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +10; __Will__: +11"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Noble's Ruse"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The noble [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|FeintS]]. On a success, the noble Strikes the target."
  - name: "Sneak Attack"
    desc: "The noble deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 13."
```

```encounter-table
name: Noble
creatures:
  - 1: Noble
```
