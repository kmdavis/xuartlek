---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brownie"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/tiny
statblock: inline
name: "Brownie"
level: 1
source: "Monster Core 2"
aon_id: "creature-4287"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4287"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Brownie"
level: "Creature 1"
size: "Tiny"
trait_01: "Fey"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
languages: "Common, Elven, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Crafting +5, Deception +6, Stealth +9"
abilityMods: [-2, 4, 1, 2, 4, 3]
abilities_top:
  - name: "Items"
    desc: "Shortsword"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +9"
hp: 21
health:
  - name: "HP"
    desc: "21; __Weaknesses__ cold iron 3"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +7 (Agile, finesse, versatile S) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Baffling Bluff"
    desc: "⬺ (Emotion, mental, primal) The brownie's antics can confuse and disorient a creature. The brownie targets a single creature within 30 feet; that creature must attempt a DC 17 Will save. The target is temporarily immune to Baffling Bluff for 1 minute."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is fooled momentarily and is off-guard against the next melee Strike the brownie makes against it before the end of the brownie's next turn."
  - name: "Failure"
    desc: "The target is confused for 1 round."
  - name: "Critical Failure"
    desc: "The target is confused for 1 minute. It can attempt a new save at the end of each of its turns to end the confused condition. Brownie Bargains As they're not a monolithic group of fey and often have their own proclivities, it's sometimes hard to predict what might attract a brownie or ensure their aid. One of the more commonplace gifts is a saucer of milk or cream, though brownies seem to enjoy other edible treats. Some farmers have reported success in leaving shiny but inconsequential knickknacks like buttons, painted stones, smoothed glass, thimbles, or silver flatware. The whims of brownies shift, so someone who wants to retain the services of one should vary the gifts they leave for these elusive fey creatures."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (4th)__ Light, Prestidigitation - __1st__ Ventriloquism - __3rd__ Mending - __4th__ Translocate"
sourcebook: "_Monster Core 2_, page 63."
```

```encounter-table
name: Brownie
creatures:
  - 1: Brownie
```
