---
obsidianUIMode: preview
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
aon_id: "creature-3418"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3418"
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
    desc: "Perception +11"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Games Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +10"
abilityMods: [2, 3, 1, 1, 2, 4]
abilities_top:
  - name: "Lip Reader"
    desc: "After years of sticking their nose where it doesn't belong, the noble has learned to read lips from afar. If they're trying to read lips in an encounter or attempting a difficult feat of lip reading, they are [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], and might need to succeed at a [[srd/pf2e/compendium/rules-elements/skills/society|Society]] check with a DC determined by the GM."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/clothing-desert|fashionable fine clothes]], [[srd/pf2e/compendium/equipment/adventuring-gear/loaded-dice|Loaded Dice]], Rapier, silver flask, signet ring"
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
    desc: "⬻ rapier +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Noble's Ruse"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The noble [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|FeintS]]. On a success, the noble Strikes the target."
  - name: "Sneak Attack"
    desc: "The noble deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 13."
```

```encounter-table
name: Noble
creatures:
  - 1: Noble
```
