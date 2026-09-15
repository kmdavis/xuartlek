---
noteType: pf2eMonster
aliases: "Flaming Skull"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Flaming Skull"
level: 2
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4280"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Flaming Skull"
level: "Creature 2"
size: "Tiny"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 9
perception:
  - name: "Perception"
    desc: "+9; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +7"
abilityMods: [1, 4, 1, -5, 3, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +10; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]] 3"
abilities_mid:
  - name: "Fiery Explosion"
    desc: "When destroyed, a flaming skull explodes in a blast of fire and bone that deals 1d6 piercing damage plus 1d6 fire damage to each adjacent creature (DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save)."
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ forehead +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d6+3 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ spitfire +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], range increment 20 feet) __Damage__ 1d12+2 fire"
abilities_bot:
  - name: "Flaming Shroud"
    desc: "A flaming skull is shrouded in hideous flames. It deals 1d6 fire damage to any unattended item it touches and on a forehead Strike. When a flaming skull gets a critical hit with a Strike that deals fire damage, the target catches fire, taking 1d4 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent fire damage]]."
sourcebook: "_Monster Core 2_, page 56."
```

```encounter-table
name: Flaming Skull
creatures:
  - 1: Flaming Skull
```
