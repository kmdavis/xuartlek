---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wolf Pack"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Wolf Pack"
level: 6
source: "Battlecry!"
aon_id: "creature-3943"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3943"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Wolf Pack"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Troop"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +15, Stealth +13, Survival +15"
abilityMods: [2, 4, 3, -4, 4, -2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +17; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "35 feet; troop movement"
abilities_bot:
  - name: "Harry Prey"
    desc: "⬺ The wolf pack focuses all their efforts on biting a single adjacent foe, who takes 4d6+8 piercing damage (DC 21 basic Reflex save). If the creature fails this saving throw, the wolf pack can immediately attempt an Athletics check to Trip the creature."
  - name: "Pack Hunt"
    desc: "The wolves work together to fell their opponents. Each enemy within a 5-foot emanation attempts a DC 21 basic Reflex save. A creature who is prone is clumsy 2 for this attack. The damage depends on the number of actions. ⬻ 1d6+1 piercing damage ⬺ 2d6+7 piercing damage ⬽ 2d6+11 piercing damage"
sourcebook: "_Battlecry!_, page 194."
```

```encounter-table
name: Wolf Pack
creatures:
  - 1: Wolf Pack
```
