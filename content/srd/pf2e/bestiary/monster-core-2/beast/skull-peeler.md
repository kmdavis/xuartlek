---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skull Peeler"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/small
statblock: inline
name: "Skull Peeler"
level: 6
source: "Monster Core 2"
aon_id: "creature-4551"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4551"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Skull Peeler"
level: "Creature 6"
size: "Small"
trait_01: "Beast"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16"
abilityMods: [5, 4, 3, -3, 3, 1]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +16; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75"
abilities_mid:
  - name: "Snatch Skull"
    desc: "⬲"
  - name: "Trigger"
    desc: "The skull peeler is using Perfect Camouflage, and a creature moves into a space within 15 feet of it"
  - name: "Effect"
    desc: "The skull peeler [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] toward the triggering creature and Strikes with its tongue. If this Strike is successful, the skull peeler automatically Grabs (page 361) the target with its tongue."
speed: "20 feet, climb 15 feet, fly 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tongue +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d4+8 slashing plus 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]]"
  - name: "Melee"
    desc: "⬻ claw +17 __Damage__ 2d10+8 slashing"
abilities_bot:
  - name: "Anticoagulant"
    desc: "The skull peeler's razor-sharp tongue is coated in an anticoagulant substance that makes wounds it inflicts particularly hard to close. The DC of the flat check to end the [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] from a skull peeler's tongue Strike is 16, or 11 with appropriate assistance."
  - name: "Perfect Camouflage"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]])"
  - name: "Requirements"
    desc: "The skull peeler is in a treetop or standing on a tree limb"
  - name: "Effect"
    desc: "Until the next time it acts, the skull peeler hangs perfectly still, blending into the treetop surroundings. It has an automatic result of 36 on [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] checks and DCs to Hide from any creature more than 10 feet away from it. A Grim Nature While explorers and adventurers who encounter skull peelers in the wild often assume the small beasts resulted from some ill-advised magical experiment by a foolish [[srd/pf2e/compendium/character/classes/wizard|wizard]], they're actually a naturally occurring species. Though their unusual assembly of characteristics might carry some minor [[srd/pf2e/compendium/gm/planes#First World|First World]] influence, skull peelers evolved from other tree-dwelling mammals over thousands of years. In their current form, they're successful predators in their environment, mostly feeding on long-necked dinosaurs—prey that other, much larger carnivores still struggle to bring down!"
sourcebook: "_Monster Core 2_, page 292."
```

```encounter-table
name: Skull Peeler
creatures:
  - 1: Skull Peeler
```
