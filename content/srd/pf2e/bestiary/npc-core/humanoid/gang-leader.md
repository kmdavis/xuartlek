---
obsidianUIMode: preview
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
aon_id: "creature-3618"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3618"
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
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +15"
abilityMods: [4, 4, 2, 2, -1, 4]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/alchemical-items/glue-bomb-major|moderate glue bomb]], lesser healing potion, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/shortsword|shortsword]]_, Sling (10 bullets), studded leather"
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
    desc: "The gang leader isn't [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to creatures of 7th level or lower that are [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]], flanking, or using surprise attack."
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
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ _shortsword_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+10 piercing"
  - name: "Ranged"
    desc: "⬻ sling +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+8 bludgeoning"
abilities_bot:
  - name: "Brutal Rally"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Trigger"
    desc: "The gang leader rolls a critical hit against a creature"
  - name: "Effect"
    desc: "All allies that can see the gang leader gain a +1 circumstance bonus to attack rolls until the start of the gang leader's next turn."
  - name: "Gang Up"
    desc: "Any enemy is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the gang leader's melee attacks due to flanking as long as the enemy is within melee reach of both the gang leader and one of the gang leader's allies."
  - name: "Quick Draw"
    desc: "⬻ The gang leader Interacts to draw a weapon, then Strikes with that weapon."
  - name: "Sneak Attack"
    desc: "The gang leader deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the gang leader. Gang Structure A gang leader might run a gang, and several other NPCs in this section and the [[srd/pf2e/compendium/gm/creature-families/criminal|Criminal]] section make for good gang members. A gang of significant size typically has a pyramid structure so that only a few members report directly to the boss and it's harder to link crimes directly to those in charge if someone gets arrested."
sourcebook: "_NPC Core_, page 160."
```

```encounter-table
name: Gang Leader
creatures:
  - 1: Gang Leader
```
