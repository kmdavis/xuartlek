---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arboreal Copse"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Arboreal Copse"
level: 9
source: "Battlecry!"
aon_id: "creature-3901"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3901"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Arboreal Copse"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Plant"
trait_02: "Troop"
trait_03: "Uncommon"
trait_04: "Wood"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
languages: "Arboreal, Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +20, Stealth +16"
abilityMods: [5, 1, 5, 2, 5, 1]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +16; __Will__: +18"
hp: 150
health:
  - name: "HP"
    desc: "150 (4 segments); __Resistances__ bludgeoning 8, piercing 8; __Weaknesses__ area damage 10, axes 8, fire 12, splash damage 10"
abilities_mid:
  - name: "Reactive Attack"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy within 5 feet of the arboreal copse uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The arboreals swing their stone swords. The triggering enemy takes 2d8+9 bludgeoning damage (DC 25 basic Reflex save). If the creature critically fails their saving throw and the trigger was a manipulate action, the troop disrupts that action."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Raise Shields"
    desc: "⬻ The arboreal wardens of the copse raise their shields in tandem, gaining a +2 circumstance bonus to AC and Reflex saves."
  - name: "Shoving Shield Wall"
    desc: "⬺ The arboreal copse Strides. All enemies whose square the copse begins in or passes through during their movement take 5d6 bludgeoning damage (DC 25 basic Fortitude). On a failed saving throw, the arboreal copse carries the creature along on their shields, moving them in the same distance and direction for the rest of their Stride."
  - name: "Sword Bash"
    desc: "The arboreal copse uses their blunt stone longswords to pummel its foes. Each enemy in a 10- foot emanation must attempt a DC 25 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+1 bludgeoning damage ⬺ 2d8+9 bludgeoning damage ⬽ 3d8+10 bludgeoning damage"
sourcebook: "_Battlecry!_, page 173."
```

```encounter-table
name: Arboreal Copse
creatures:
  - 1: Arboreal Copse
```
