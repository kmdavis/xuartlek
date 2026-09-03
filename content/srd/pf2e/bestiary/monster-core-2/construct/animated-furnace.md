---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Furnace"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/huge
statblock: inline
name: "Animated Furnace"
level: 9
source: "Monster Core 2"
aon_id: "creature-4059"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4059"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Animated Furnace"
level: "Creature 9"
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18"
abilityMods: [7, -2, 6, -5, 0, -5]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +11; __Will__: +13 construct armor"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Hardness__ 10"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated furnace has Hardness. This Hardness reduces any damage the swarm takes by an amount equal to the Hardness. Once an animated furnace is reduced to fewer than half its Hit Points or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 26."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ door +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d12+9 bludgeoning plus 1d8 fire and Improved Grab"
abilities_bot:
  - name: "Fan the Flames"
    desc: "⬺ The animated furnace opens its door and fans its flames in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] that deals 5d6 fire damage (DC 28 basic Reflex save)."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 2d8+9 fire, Rupture 15"
sourcebook: "_Monster Core 2_, page 32."
```

```encounter-table
name: Animated Furnace
creatures:
  - 1: Animated Furnace
```
