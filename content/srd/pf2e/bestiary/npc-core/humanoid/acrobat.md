---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Acrobat"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Acrobat"
level: 2
source: "NPC Core"
aon_id: "creature-3570"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3570"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Acrobat"
level: "Creature 2"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/lore|Circus Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [2, 4, 2, 1, 0, 1]
abilities_top:
  - name: "Acrobatic Specialist"
    desc: "For encounters involving contests of acrobatics and similar activities, the acrobat is a 5th-level challenge."
  - name: "Steady Balance"
    desc: "When the acrobat rolls a success on an [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] check, they get a critical success instead. They aren't off-guard when attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balance]] and can attempt an Acrobatics check instead of a Reflex save to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grab an Edge|Grab an Edge]]."
  - name: "Items"
    desc: "Climbing Kit, Dagger (5), Rope (50 feet)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +11; __Will__: +4"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Cat Fall"
    desc: "The acrobat treats all falls as 25 feet shorter."
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The acrobat is targeted with a melee or ranged attack by an attacker they can see"
  - name: "Effect"
    desc: "The acrobat gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ foot +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The acrobat deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Swinging Strike"
    desc: "⬺ The acrobat swings on a rope or trapeze, moving up to double their Speed. At any point during the swing, they can make a melee Strike."
sourcebook: "_NPC Core_, page 124."
```

```encounter-table
name: Acrobat
creatures:
  - 1: Acrobat
```
