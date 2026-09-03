---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Burglar"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Burglar"
level: 4
source: "NPC Core"
aon_id: "creature-3429"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3429"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Burglar"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; (11 to find traps)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +7"
abilityMods: [2, 4, 1, 1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Climbing Kit, Composite Shortbow (10 arrows), lesser darkvision elixir, Leather Armor, Shortsword, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +7; __Ref__: +12; __Will__: +10 +1 circumstance to all saves vs. traps"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The burglar isn't [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to creatures of 4th level or lower that are [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]], flanking, or using surprise attack."
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The burglar is targeted with a melee or ranged attack by an attacker it can see"
  - name: "Effect"
    desc: "The burglar gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Mobility"
    desc: "When the burglar Strides half their Speed or less, that movement does not trigger reactions."
  - name: "Sneak Attack"
    desc: "The burglar deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the Burglar."
sourcebook: "_NPC Core_, page 20."
```

```encounter-table
name: Burglar
creatures:
  - 1: Burglar
```
