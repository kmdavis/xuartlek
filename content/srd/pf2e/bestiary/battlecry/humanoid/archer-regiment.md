---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Archer Regiment"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Archer Regiment"
level: 12
source: "Battlecry!"
aon_id: "creature-3902"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3902"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Archer Regiment"
level: "Creature 12"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +22"
abilityMods: [4, 7, 3, 1, 5, 1]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +19; __Ref__: +25; __Will__: +22"
hp: 210
health:
  - name: "HP"
    desc: "210 (4 segments); __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Dagger Defense"
    desc: "The archer regiment draws daggers to attack close-range enemies. Each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must attempt a DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. The archer regiment gains a +1 circumstance bonus to AC until the beginning of their next turn. ⬻ 2d4+2 piercing damage ⬺ 4d4+12 piercing damage ⬽ 4d4+15 piercing damage"
  - name: "Drilled in Formations"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The archer regiment uses [[srd/pf2e/compendium/gm/creature-families/military|Change Formation]]. An archer regiment unit typically knows the loose and marching column formations."
  - name: "Rain of Arrows"
    desc: "⬺ The archer regiment fires their longbows in a coordinated volley. This volley is either a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 200 feet that deals 4d8 piercing damage or a 10- foot burst within 100 feet that deals 6d8 piercing damage. Either effect has a DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. When the archer regiment is reduced to 2 segments, both areas are reduced by 5 feet."
sourcebook: "_Battlecry!_, page 174."
```

```encounter-table
name: Archer Regiment
creatures:
  - 1: Archer Regiment
```
