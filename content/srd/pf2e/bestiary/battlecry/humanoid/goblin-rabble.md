---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Rabble"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Goblin Rabble"
level: 4
source: "Battlecry!"
aon_id: "creature-3920"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3920"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Goblin Rabble"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +10, Stealth +12, Thievery +12"
abilityMods: [1, 5, 2, 0, 1, 1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +14; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60 (4 segments); __Weaknesses__ area damage 4, splash damage 4"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; troop movement"
abilities_bot:
  - name: "Dogpile"
    desc: "The goblin rabble engage in as coordinated an attack as they can with their dogslicers, attacking each enemy in a 5-foot emanation (DC 18 basic Reflex save). The damage depends on the number of actions. A creature who critically fails their save is also knocked prone. ⬻ 1d6 slashing damage ⬺ 2d6+4 slashing damage ⬽ 2d6+7 slashing damage"
  - name: "Hobble Pursuit"
    desc: "⬺ The goblin rabble hamstring and hobble as many enemies as possible. Each enemy in a 5-foot emanation must attempt a DC 18 Reflex save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes a –5-foot circumstance penalty to their Speeds."
  - name: "Failure"
    desc: "The creature takes a –10-foot circumstance penalty to their Speeds and is slowed 1."
  - name: "Critical Failure"
    desc: "The creature takes a –15-foot circumstance penalty to their Speeds and is slowed 1."
  - name: "Rush and Steal"
    desc: "⬺ Quickly moving in with grasping hands, the goblin rabble take what they can. The goblin rabble Strides up to twice their Speed. During this movement, the goblins Interact to pick up an unattended object no larger than 2 Bulk or attempt to Steal an item from a creature they are adjacent to; the goblins can pick up or Steal as many objects as they have remaining segments in any combination."
sourcebook: "_Battlecry!_, page 182."
```

```encounter-table
name: Goblin Rabble
creatures:
  - 1: Goblin Rabble
```
