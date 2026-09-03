---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Morlock Tinkerer"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/morlock
  - pf2e/creature/trait/medium
statblock: inline
name: "Morlock Tinkerer"
level: 2
source: "Monster Core 2"
aon_id: "creature-4478"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4478"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Morlock Tinkerer"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Morlock"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [4, 3, 1, -2, 3, 1]
abilities_top:
  - name: "Light Blindness"
    desc: ""
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/club/club|Club]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +11; __Will__: +9 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +9 __Damage__ 1d6+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+4 piercing"
  - name: "Ranged"
    desc: "⬻ club +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Instinctual Tinker"
    desc: "⬺ The morlock tinkers with an adjacent construct or mechanical hazard. They attempt a [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] check against the construct's or hazard's Fortitude DC. The morlock can't succeed if the target's level is more than double the morlock's."
  - name: "Critical Success"
    desc: "The target regains 4d6 Hit Points and gains a +1 circumstance bonus to attack rolls for 1 minute."
  - name: "Success"
    desc: "The target regains 2d6 Hit Points."
  - name: "Critical Failure"
    desc: "The morlock injures themself, taking 2d6 damage (typically bludgeoning, piercing, or slashing, but potentially a different type at the GM's discretion)."
  - name: "Leap Attack"
    desc: "⬺ The morlock Strides up to twice their Speed, during which they attempt a [[srd/pf2e/compendium/rules-elements/actions/player-core#High Jump|High Jump]] or a [[srd/pf2e/compendium/rules-elements/actions/player-core#Long Jump|Long Jump]]. At any point during their movement, the morlock can make a melee Strike against an enemy in their reach. The morlock then can't use Leap Attack until the end of their next turn."
  - name: "Sneak Attack"
    desc: "A morlock's Strikes deal an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Swarming Stance"
    desc: "A morlock can share the same space as another morlock, but no more than two morlocks can occupy the same space. When morlocks share the same space, they gain a +1 circumstance bonus to attack rolls. Morlock Machinery Morlocks tend toward brutish actions and violent traditions and have little interest in bettering their societies or creating art. However, they have a strange obsession with ancient machinery and magical items, particularly clockwork constructions. Their knack for tinkering helps keep ancient guardians and traps functional, even if their work backfires now and then."
sourcebook: "_Monster Core 2_, page 226."
```

```encounter-table
name: Morlock Tinkerer
creatures:
  - 1: Morlock Tinkerer
```
