---
noteType: pf2eMonster
aliases: "Gang Leader"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gang Leader"
level: 7
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3618"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gang Leader"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +15, [[srd/pf2e/compendium/rules-elements/skills/Lore|Underworld Lore]] +15"
abilityMods: [4, 4, 2, 2, -1, 4]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/alchemical-items/Glue Bomb|moderate glue bomb]], lesser healing potion, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/Shortsword|shortsword]]_, Sling (10 bullets), studded leather"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +17; __Will__: +12"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The gang leader isn't [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to creatures of 7th level or lower that are [[srd/pf2e/compendium/rules-elements/Conditions#Hidden|hidden]], [[srd/pf2e/compendium/rules-elements/Conditions#Undetected|undetected]], flanking, or using surprise attack."
  - name: "Evasive Reflexes"
    desc: "When the gang leader rolls a success on a Reflex save, they get a critical success instead."
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The gang leader is targeted with an attack by an attacker they can see"
  - name: "Effect"
    desc: "The gang leader gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ _shortsword_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+10 piercing"
  - name: "Ranged"
    desc: "⬻ sling +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+8 bludgeoning"
abilities_bot:
  - name: "Brutal Rally"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Trigger"
    desc: "The gang leader rolls a critical hit against a creature"
  - name: "Effect"
    desc: "All allies that can see the gang leader gain a +1 circumstance bonus to attack rolls until the start of the gang leader's next turn."
  - name: "Gang Up"
    desc: "Any enemy is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] against the gang leader's melee attacks due to flanking as long as the enemy is within melee reach of both the gang leader and one of the gang leader's allies."
  - name: "Quick Draw"
    desc: "⬻ The gang leader Interacts to draw a weapon, then Strikes with that weapon."
  - name: "Sneak Attack"
    desc: "The gang leader deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted are [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the gang leader. Gang Structure A gang leader might run a gang, and several other NPCs in this section and the [[srd/pf2e/compendium/gm/creature-families/Criminal|Criminal]] section make for good gang members. A gang of significant size typically has a pyramid structure so that only a few members report directly to the boss and it's harder to link crimes directly to those in charge if someone gets arrested."
sourcebook: "_NPC Core_, page 160."
```

```encounter-table
name: Gang Leader
creatures:
  - 1: Gang Leader
```
