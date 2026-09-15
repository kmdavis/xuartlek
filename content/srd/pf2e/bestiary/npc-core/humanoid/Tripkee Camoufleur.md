---
noteType: pf2eMonster
aliases: "Tripkee Camoufleur"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Camoufleur"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3674"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tripkee Camoufleur"
level: "Creature 2"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Tripkee|Tripkee]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +7, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +7"
abilityMods: [1, 4, 1, 1, 3, 0]
abilities_top:
  - name: "Camouflage Specialist"
    desc: "For encounters involving avoiding detection or hiding an object or creature, the camoufleur is a 5th-level challenge."
  - name: "Natural Disguise"
    desc: "The camoufleur can use their [[srd/pf2e/compendium/equipment/adventuring-gear/Disguise Kit|disguise kit]] to disguise a creature or object as natural flora. A creature gains a +2 item bonus to [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] checks while in a natural environment until its next daily preparations or until its disguise is ruined, whichever comes first. An object in a natural environment can be found only by actively searching (using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Search]] activity while exploring or the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action in an encounter) and uses the camoufleur's Stealth DC."
  - name: "Items"
    desc: "darts (5), Disguise Kit, Hand Adze, Leather Armor"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +11; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet, climb 20 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ hand adze +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d4+3 slashing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+3 piercing"
  - name: "Ranged"
    desc: "⬻ hand adze +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d4+3 slashing"
abilities_bot:
  - name: "Forest Passage"
    desc: "The tripkee ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 214."
```

```encounter-table
name: Tripkee Camoufleur
creatures:
  - 1: Tripkee Camoufleur
```
