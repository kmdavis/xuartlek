---
obsidianUIMode: preview
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
aon_id: "creature-3454"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3454"
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
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +3, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +7"
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
    desc: "⬻ shiv +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The prisoner deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the prisoner."
  - name: "You're Next"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Trigger"
    desc: "The prisoner reduces a creature to 0 Hit Points"
  - name: "Effect"
    desc: "The prisoner attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] a creature that saw their victory, with a +2 circumstance bonus to the [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check."
sourcebook: "_NPC Core_, page 40."
```

```encounter-table
name: Prisoner
creatures:
  - 1: Prisoner
```
