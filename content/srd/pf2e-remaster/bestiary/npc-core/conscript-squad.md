---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Conscript Squad"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Conscript Squad"
level: 3
source: "NPC Core"
aon_id: "creature-3523"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3523"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Conscript Squad"
level: "Creature 3"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +9"
abilityMods: [4, 2, 2, 0, -1, 0]
abilities_top:
  - name: "Untrained Rabble"
    desc: "At the start of each of its turns, the conscript squad must succeed at a DC 10 Will save or be confused that turn."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +9; __Will__: +6 –2 circumstance to all saves vs. fear"
hp: 54
health:
  - name: "HP"
    desc: "54 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Indiscriminate Assault"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The conscript squad lashes out at each other creature in a 5-foot emanation, friend and foe, with a DC 17 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8 piercing damage ⬺ 1d8+4 piercing damage ⬽ 2d8+4 piercing damage"
sourcebook: "_NPC Core_, page 89."
```

```encounter-table
name: Conscript Squad
creatures:
  - 1: Conscript Squad
```
