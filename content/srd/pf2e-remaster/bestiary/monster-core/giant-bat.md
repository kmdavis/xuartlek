---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Bat"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Bat"
level: 2
source: "Monster Core"
aon_id: "creature-2849"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2849"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Bat"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; echolocation (precise) 40 feet, low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +8, Stealth +8"
abilityMods: [4, 2, 3, -4, 3, -2]
abilities_top:
  - name: "Echolocation"
    desc: "A bat can use its hearing as a precise sense at the listed range."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +8; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Wing Thrash"
    desc: "⬲"
  - name: "Trigger"
    desc: "An adjacent enemy damages the giant bat"
  - name: "Effect"
    desc: "The bat makes one or two wing Strikes—one against the triggering creature and one against another adjacent creature."
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +9 __Damage__ 1d10+4 piercing"
  - name: "Melee"
    desc: "⬻ wing +9 (Agile) __Damage__ 1d6+4 slashing"
sourcebook: "_Monster Core_, page 40."
```

```encounter-table
name: Giant Bat
creatures:
  - 1: Giant Bat
```
