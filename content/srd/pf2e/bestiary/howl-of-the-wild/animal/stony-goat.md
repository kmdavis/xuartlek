---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stony Goat"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/small
statblock: inline
name: "Stony Goat"
level: 2
source: "Howl of the Wild"
aon_id: "creature-3313"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3313"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Stony Goat"
level: "Creature 2"
size: "Small"
trait_01: "Animal"
trait_02: "Rare"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; all-around vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [3, 4, 3, -4, 2, 1]
abilities_top:
  - name: "Items"
    desc: "cud worth 28 gp"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +11; __Will__: +5"
hp: 28
health:
  - name: "HP"
    desc: "28"
abilities_mid:
  - name: "Self-Petrify"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph__]])__ Trigger The stony goat gains the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition or takes more than 8 damage in a single hit"
  - name: "Effect"
    desc: "The stony goat turns to stone in self-defense. It gains the [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] condition for 1d4 rounds. If the goat is damaged while it's petrified, it immediately heals by that amount by absorbing minerals from its cud, causing its cud to lose value equal to the amount of Hit Points restored (for instance, losing 5 gp worth of value to restore 5 Hit Points); if the goat's cud is reduced to 0 gp, it has the minerals fully drained from it, and the goat won't form more cud until it has eaten a sufficient quantity of rock and slept."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ head +8 __Damage__ 1d8+3 bludgeoning"
abilities_bot:
  - name: "Overhead Leap"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The stony goat [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] up to 12 feet vertically and 20 feet horizontally; this movement doesn't trigger reactions."
  - name: "Shove and Run"
    desc: "⬻ The stony goat attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]] the nearest creature and then Strides with a +20-foot circumstance bonus to Speed."
  - name: "Stone Bolt"
    desc: "⬲"
  - name: "Trigger"
    desc: "The stony goat loses the [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] condition"
  - name: "Effect"
    desc: "The stony goat's first instinct is to escape. It Strides with a +20 circumstance bonus to its Speed."
sourcebook: "_Howl of the Wild_, page 184."
```

```encounter-table
name: Stony Goat
creatures:
  - 1: Stony Goat
```
