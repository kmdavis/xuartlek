---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Guide"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Guide"
level: 4
source: "NPC Core"
aon_id: "creature-3472"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3472"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Guide"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +8, [[srd/pf2e/compendium/rules-elements/skills/lore|Scouting Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [4, 1, 2, 1, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (40 arrows), Greataxe, Scale Mail"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +8; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Guide's Warning"
    desc: "⬲"
  - name: "Trigger"
    desc: "The guide is about to roll a Perception or [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] check to determine their initiative"
  - name: "Effect"
    desc: "The guide visually or audibly warns allies, granting them a +1 circumstance bonus to their initiative rolls. This bonus increases to +2 if the guide was [[srd/pf2e/compendium/rules-elements/actions/player-core#Scout|Scouting]]. Depending on how the guide warns allies, this action has the [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]] trait."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+8 slashing"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 1d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Guiding Words"
    desc: "⬻ The guide points out a weakness of a creature within 30 feet. Until the start of the guide's next turn, the guide and all allies that can hear the guiding words gain a +1 circumstance bonus to attack rolls against that creature, and the guide's Strikes deal an extra 1d4 precision damage to that creature."
sourcebook: "_NPC Core_, page 55."
```

```encounter-table
name: Guide
creatures:
  - 1: Guide
```
