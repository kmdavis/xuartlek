---
noteType: pf2eMonster
aliases: "Prisoner"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Prisoner"
level: 1
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3454"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Prisoner"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +3, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +7"
abilityMods: [3, 4, 1, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "shiv"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +6"
hp: 17
health:
  - name: "HP"
    desc: "17"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shiv +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The prisoner deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the prisoner."
  - name: "You're Next"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Trigger"
    desc: "The prisoner reduces a creature to 0 Hit Points"
  - name: "Effect"
    desc: "The prisoner attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] a creature that saw their victory, with a +2 circumstance bonus to the [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] check."
sourcebook: "_NPC Core_, page 40."
```

```encounter-table
name: Prisoner
creatures:
  - 1: Prisoner
```
