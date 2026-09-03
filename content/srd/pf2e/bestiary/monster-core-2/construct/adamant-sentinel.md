---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adamant Sentinel"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Adamant Sentinel"
level: 18
source: "Monster Core 2"
aon_id: "creature-4010"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4010"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adamant Sentinel"
level: "Creature 18"
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Rare"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +38"
abilityMods: [9, -1, 9, -5, 0, -5]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +33; __Ref__: +27; __Will__: +29"
hp: 255
health:
  - name: "HP"
    desc: "255 (repair mode); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/damage-rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 20 (except [[srd/pf2e/compendium/equipment/runes/vorpal|_vorpal_]] [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]]), spells 20"
abilities_mid:
  - name: "Repair Mode"
    desc: "When the adamant sentinel is at 0 HP, it isn't destroyed. Instead, it enters repair mode, during which it's [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1, can't take reactions, and can take only the Self-Repair action. Once it has more than 30 HP, it can use any type of action and can use reactions, though it remains slowed 1 and can't take any reactions until the start of its next turn. If a critical hit with a vorpal adamantine weapon reduces the sentinel to 0 HP, or if such a weapon hits it while it's already at 0 HP, the sentinel is destroyed."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 3d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+17 bludgeoning plus destructive strike"
abilities_bot:
  - name: "Destructive Strike"
    desc: "On a critical hit, the adamant sentinel's fist Strike breaks the target's armor, if any, in addition to dealing damage to the target. If the target has a shield raised, the sentinel breaks the shield instead."
  - name: "Inexorable March"
    desc: "⬻ The adamant sentinel Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can try to bar the way by attempting a DC 45 Fortitude save."
  - name: "Critical Success"
    desc: "The sentinel halts its movement and cannot enter the creature’s square."
  - name: "Success"
    desc: "As critical success, but the resisting creature takes 3d10+17 bludgeoning damage."
  - name: "Failure"
    desc: "The resisting creature takes 3d10+17 bludgeoning damage, and its armor, if any, is [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]]. If the resisting creature has a shield raised, the sentinel breaks the shield instead."
  - name: "Self-Repair"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The sentinel repairs itself, regaining 30 Hit Points."
  - name: "Vent"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) The sentinel vents a 30-foot cone of superheated steam from its internal forge. This deals 15d6 fire damage to all creatures in the cone (DC 40 basic Reflex). The sentinel can't use Vent again for 1d6 rounds. Adamantine Hunks The incredible amount of adamantine necessary to create a single adamant sentinel is worth more than many nations’ treasuries. The powerful heart of an adamant sentinel can be turned into a legendary forge for blacksmithing."
sourcebook: "_Monster Core 2_, page 8."
```

```encounter-table
name: Adamant Sentinel
creatures:
  - 1: Adamant Sentinel
```
