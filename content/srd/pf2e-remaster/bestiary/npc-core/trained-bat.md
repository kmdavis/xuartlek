---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Trained Bat"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Trained Bat"
level: 4
source: "NPC Core"
aon_id: "creature-3676"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3676"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Trained Bat"
level: "Creature 4"
size: "Medium"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; echolocation (precise) 20 feet, low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +9, Intimidation +6, Stealth +12, Survival +8"
abilityMods: [3, 4, 3, -4, 2, 0]
abilities_top:
  - name: "Items"
    desc: "light barding"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +12; __Will__: +10"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 (Finesse) __Damage__ 2d6+6 piercing"
  - name: "Melee"
    desc: "⬻ wing +14 (Agile, Finesse) __Damage__ 2d4+6 slashing"
abilities_bot:
  - name: "Wing Thrash"
    desc: "⬺ The trained bat thrashes wildly with its wings, making wing Strikes against up to three adjacent foes. Each attack counts toward the bat's multiple attack penalty, but the penalty increases only after all the attacks have been made."
sourcebook: "_NPC Core_, page 218."
```

```encounter-table
name: Trained Bat
creatures:
  - 1: Trained Bat
```
