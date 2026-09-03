---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Armor"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/medium
statblock: inline
name: "Animated Armor"
level: 2
source: "Monster Core"
aon_id: "creature-2819"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2819"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Animated Armor"
level: "Creature 2"
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9"
abilityMods: [3, -3, 4, -5, 0, -5]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +3; __Will__: +4 construct armor"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Hardness__ 9"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, animated armor has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated armor is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 13."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ glaive +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+4 slashing"
  - name: "Melee"
    desc: "⬻ gauntlet +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d6+4 bludgeoning"
sourcebook: "_Monster Core_, page 18."
```

```encounter-table
name: Animated Armor
creatures:
  - 1: Animated Armor
```
