---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wood Wisp"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/tiny
statblock: inline
name: "Wood Wisp"
level: 0
source: "Rage of Elements"
aon_id: "creature-2668"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2668"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Wood Wisp"
level: "Creature 0"
size: "Tiny"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, Plane of Wood Lore +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [3, 1, 2, 0, 3, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +2; __Will__: +8"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 2, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 2"
abilities_mid:
  - name: "Resonance"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/wood|wood]]) 30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. A creature in the area gains a +1 status bonus to attack and damage rolls for effects with the [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/wood|wood]] trait; a creature with the [[srd/pf2e/compendium/rules-elements/traits/player-core/elemental|elemental]] trait and either plant trait or wood trait gains this bonus to all attack and damage rolls. For wood wisps, this bonus also applies to nonmagical wooden weapons, such as staves and clubs."
  - name: "Accord Essence"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]])"
  - name: "Trigger"
    desc: "An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack"
  - name: "Effect"
    desc: "The wisp detonates itself in a small elemental explosion of leaves and pollen. This gives temporary Hit Points equal to half the wisp's current HP to all allies within 30 feet that have benefited from the wisp's resonance aura in the past hour. These temporary Hit Points last 1 hour. A wisp that uses this reaction is permanently destroyed and can be restored only by a _wish_ ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
speed: "fly 20 feet, climb 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ thorny vine +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d4 bludgeoning plus 1 piercing"
abilities_bot:
  - name: "In Concert"
    desc: "When a wood wisp rolls a critical failure on a check to Aid, they get a failure instead, and when they roll a success, they get a critical success instead."
sourcebook: "_Rage of Elements_, page 204."
```

```encounter-table
name: Wood Wisp
creatures:
  - 1: Wood Wisp
```
