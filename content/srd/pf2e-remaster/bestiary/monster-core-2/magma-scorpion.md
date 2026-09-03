---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Magma Scorpion"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/large
statblock: inline
name: "Magma Scorpion"
level: 8
source: "Monster Core 2"
aon_id: "creature-4389"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4389"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Magma Scorpion"
level: "Creature 8"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, smoke vision"
skills:
  - name: "Skills"
    desc: "Athletics +16"
abilityMods: [6, 3, 5, -4, 4, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The magma scorpion ignores the concealed condition from smoke."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +14; __Will__: +16"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 10"
speed: "40 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +20 (Agile, reach 10 feet) __Damage__ 2d6+9 bludgeoning plus 1d6 persistent fire and Grab"
  - name: "Melee"
    desc: "⬻ tail sting +20 (reach 10 feet) __Damage__ 1d10+9 piercing plus 1d6 persistent fire and magma scorpion venom"
  - name: "Ranged"
    desc: "⬻ magma spit +17 (Fire, range increment 40 feet) __Damage__ 1d6+9 fire plus 1d6 persistent fire"
abilities_bot:
  - name: "Magma Scorpion Venom"
    desc: "(Fire, injury, poison)"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 fire damage (1 round) and enfeebled 1"
  - name: "Stage 2"
    desc: "3d6 fire damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core 2_, page 149."
```

```encounter-table
name: Magma Scorpion
creatures:
  - 1: Magma Scorpion
```
