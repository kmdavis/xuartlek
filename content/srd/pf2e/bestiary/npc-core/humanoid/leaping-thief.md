---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leaping Thief"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/catfolk
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Leaping Thief"
level: 3
source: "NPC Core"
aon_id: "creature-3623"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3623"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Leaping Thief"
level: "Creature 3"
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "Amurrun, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +9"
abilityMods: [0, 4, 2, 1, 0, 3]
abilities_top:
  - name: "Items"
    desc: "Claw Blade, Leather Armor, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +7; __Ref__: +11; __Will__: +7"
hp: 38
health:
  - name: "HP"
    desc: "38"
speed: "25 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw blade +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d4+6 slashing"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 slashing"
abilities_bot:
  - name: "Coiled Leap"
    desc: "⬺ The leaping thief [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] up to 10 feet vertically or 30 feet horizontally."
  - name: "Sneak Attack"
    desc: "The leaping thief deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Stealthy Pad"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The leaping thief Steps, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hides]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaks]], ignoring difficult terrain for this movement."
  - name: "Unexpected Angle"
    desc: "When the leaping thief successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumbles Through]] a foe's space or [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] to a position higher than a foe, the foe is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the next attack the leaping thief makes before the end of their turn."
sourcebook: "_NPC Core_, page 172."
```

```encounter-table
name: Leaping Thief
creatures:
  - 1: Leaping Thief
```
