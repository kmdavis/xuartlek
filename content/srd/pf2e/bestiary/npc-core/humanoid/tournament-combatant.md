---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tournament Combatant"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tournament Combatant"
level: 5
source: "NPC Core"
aon_id: "creature-3501"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3501"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tournament Combatant"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +11"
abilityMods: [3, 5, 1, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Nunchaku, Shuriken (5)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +15; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d8+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ nunchaku +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ shuriken +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+5 piercing"
abilities_bot:
  - name: "Flying Attack"
    desc: "⬺ The tournament combatant makes a [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leap]], [[srd/pf2e/compendium/rules-elements/actions/player-core#High Jump|High Jump]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Long Jump|Long Jump]]. At any point during the jump, if they're adjacent to an enemy, they can Strike that enemy with a fist or nunchaku Strike, even in midair. The combatant falls to the ground after the Strike. If the distance they fall is no more than the height of their jump, they land upright and take no damage."
  - name: "Somersault Attack"
    desc: "⬻ The tournament combatant attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumble Through]] a target's space. If they succeed on their [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] check, the tournament combatant can make a fist or nunchaku Strike against that target while moving through its space."
  - name: "Powerful Fists"
    desc: "The martial artist's fist Strikes don't take penalties when making lethal attacks."
  - name: "Work The Crowd"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Requirements"
    desc: "The combatant is within 50 feet of at least three spectators"
  - name: "Effect"
    desc: "With a flashy flurry of moves, the tournament combatant elicits cheers. The tournament combatant is [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] for 1 minute. They can use the extra action only to Strike or Stride."
sourcebook: "_NPC Core_, page 72."
```

```encounter-table
name: Tournament Combatant
creatures:
  - 1: Tournament Combatant
```
