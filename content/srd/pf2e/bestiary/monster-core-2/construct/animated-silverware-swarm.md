---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Silverware Swarm"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Animated Silverware Swarm"
level: 1
source: "Monster Core 2"
aon_id: "creature-4058"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4058"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Animated Silverware Swarm"
level: "Creature 1"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Swarm"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8"
abilityMods: [1, 3, 4, -5, 0, -5]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +8; __Will__: +3 construct armor"
hp: 14
health:
  - name: "HP"
    desc: "14; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Weaknesses__ area damage 3, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 3; __Hardness__ 3"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated silverware swarm has Hardness. This Hardness reduces any damage the swarm takes by an amount equal to the Hardness. Once an animated silverware swarm is reduced to fewer than half its Hit Points or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 12."
speed: "20 feet"
abilities_bot:
  - name: "Slice and Dice"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) Each enemy in the animated silverware swarm's space takes 1d6 piercing or slashing damage (DC 17 basic Reflex save)."
  - name: "Stick a Fork in It"
    desc: "⬻ The animated silverware swarm attempts to pin a single creature. The target must attempt a DC 17 Reflex save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "Silverware pins portions of the target's clothing and gear. The target takes a –10-foot circumstance penalty to its Speeds as long as it remains in the swarm's space."
  - name: "Failure"
    desc: "As success, and the target also can't Step until it leaves the swarm's space."
  - name: "Critical Failure"
    desc: "The target is thoroughly pinned by the silverware, becoming [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 17) or uses 2 Interact actions to remove all the silverware pinning it down."
sourcebook: "_Monster Core 2_, page 32."
```

```encounter-table
name: Animated Silverware Swarm
creatures:
  - 1: Animated Silverware Swarm
```
