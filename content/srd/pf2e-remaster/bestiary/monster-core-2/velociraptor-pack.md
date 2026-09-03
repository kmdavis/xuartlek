---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Velociraptor Pack"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Velociraptor Pack"
level: 5
source: "Monster Core 2"
aon_id: "creature-4334"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4334"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Velociraptor Pack"
level: "Creature 5"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: "Troop"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +11, Intimidation +12, Stealth +12"
abilityMods: [2, 5, 3, 0, 2, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +14; __Will__: +8"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet; troop movement"
abilities_bot:
  - name: "Bites and Talons"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The pack makes a melee attack against each enemy in a 5-foot emanation (DC 19 basic reflex save). The damage depends on the number of actions. ⬻ 1d6 piercing or slashing damage and 1d4 precision damage ⬺ 2d6 piercing or slashing damage and 2d4 precision damage ⬽ 3d6 piercing or slashing damage and 2d4 precision damage"
  - name: "Puff Up"
    desc: "The velociraptors ruffle their plumage to appear larger. They ignore the –4 penalty to Demoralize for not knowing the same language as their target."
  - name: "Raptor Leap"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The pack Strides, ignoring difficult terrain (but not greater difficult terrain). At the end of this movement, each enemy in a 5-foot emanation takes 1d8 piercing or slashing damage (DC 19 basic Reflex save)."
sourcebook: "_Monster Core 2_, page 106."
```

```encounter-table
name: Velociraptor Pack
creatures:
  - 1: Velociraptor Pack
```
