---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Army"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Animated Army"
level: 8
source: "Battlecry!"
aon_id: "creature-3899"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3899"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Animated Army"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Troop"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18"
abilityMods: [6, 0, 6, -5, 0, -5]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +14; __Will__: +13 construct armor"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], nonlethal attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Weaknesses__ area damage 8, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 8; __Hardness__ 10"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, the animated statues of the animated army have Hardness. This Hardness reduces any damage the animated army takes by an amount equal to the Hardness. Once an animated army is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 23."
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Battering Fists"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The animated army makes a melee attack against each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 23 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage dealt depends on the number of actions. ⬻ 1d8+2 bludgeoning damage ⬺ 2d8+8 bludgeoning damage ⬽ 3d8+10 bludgeoning damage"
sourcebook: "_Battlecry!_, page 173."
```

```encounter-table
name: Animated Army
creatures:
  - 1: Animated Army
```
