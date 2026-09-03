---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shambler Troop"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Shambler Troop"
level: 4
source: "Monster Core 2"
aon_id: "creature-4620"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4620"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shambler Troop"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Troop"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
abilityMods: [5, 0, 3, -5, 1, -2]
abilities_top:
  - name: "Slow"
    desc: "A shambler troop is permanently [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 and can't use reactions."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +8; __Will__: +9"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ area damage 5, slashing 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Grave Tide"
    desc: "The shambler troop is less organized than most troops. It can move into other creatures' spaces, and other creatures can move into its spaces. Its spaces are [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] to other creatures."
  - name: "Shambling Onslaught"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The shamblers lash out at any enemies in their squares or within a 5-foot emanation (DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. ⬻ 2d6+5 bludgeoning damage ⬺ 2d6+9 bludgeoning damage"
sourcebook: "_Monster Core 2_, page 358."
```

```encounter-table
name: Shambler Troop
creatures:
  - 1: Shambler Troop
```
