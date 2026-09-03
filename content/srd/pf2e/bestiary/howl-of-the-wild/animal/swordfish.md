---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Swordfish"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/large
statblock: inline
name: "Swordfish"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3277"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3277"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Swordfish"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +12"
abilityMods: [5, 3, 1, -4, 2, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +12; __Will__: +7"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Warm Brain"
    desc: "⬲"
  - name: "Requirement"
    desc: "The swordfish is in cold water"
  - name: "Trigger"
    desc: "The swordfish rolls initiative"
  - name: "Effect"
    desc: "The swordfish Seeks or Swims."
speed: "swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bill +12 (Sweep) __Damage__ 1d10+5 slashing"
abilities_bot:
  - name: "Fast Sweep"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Effect"
    desc: "The swordfish makes two bill Strikes against two adjacent targets, with a +1 circumstance bonus to its attack rolls."
sourcebook: "_Howl of the Wild_, page 149."
```

```encounter-table
name: Swordfish
creatures:
  - 1: Swordfish
```
