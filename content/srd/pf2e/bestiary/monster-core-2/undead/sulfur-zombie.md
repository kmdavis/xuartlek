---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sulfur Zombie"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/medium
statblock: inline
name: "Sulfur Zombie"
level: 6
source: "Monster Core 2"
aon_id: "creature-4621"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4621"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sulfur Zombie"
level: "Creature 6"
size: "Medium"
trait_01: "Fire"
trait_02: "Mindless"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [5, 2, 4, -5, 2, -2]
abilities_top:
  - name: "Slow"
    desc: "A sulfur zombie is permanently [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 and can't use reactions"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +16; __Ref__: +12; __Will__: +10"
hp: 125
health:
  - name: "HP"
    desc: "125 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ slashing 7, [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] 7"
abilities_mid:
  - name: "Death Throes"
    desc: "When a sulfur zombie dies, its body explodes in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] of fire and debris that deals 2d10 bludgeoning damage and 2d10 fire damage to each creature in the area (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +17 __Damage__ 2d6+5 bludgeoning plus 1d6 p[[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|ersistent fire]] and blinding sulfur"
abilities_bot:
  - name: "Blinding Sulfur"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]]) A sulfur zombie burns with putrid inner fire. A creature hit by a sulfur zombie's fist Strike must attempt a DC 22 Fortitude save. On a failure, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round, or for 1 minute on a critical failure."
sourcebook: "_Monster Core 2_, page 358."
```

```encounter-table
name: Sulfur Zombie
creatures:
  - 1: Sulfur Zombie
```
