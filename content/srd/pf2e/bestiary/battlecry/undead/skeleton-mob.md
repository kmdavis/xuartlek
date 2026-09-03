---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeleton Mob"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Skeleton Mob"
level: 6
source: "Battlecry!"
aon_id: "creature-3938"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3938"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Skeleton Mob"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Troop"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +13"
abilityMods: [4, 2, 1, -5, 1, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +14; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments, void healing (page 217)); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 7, electricity 7, fire 7, piercing 7, slashing 7; __Weaknesses__ area damage 7, splash damage 7"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, troop movement"
abilities_bot:
  - name: "Ossuary Storm"
    desc: "⬺ The skeleton mob hurls skulls and fragments of bone in a 10-foot burst within 30 feet. This attack deals 3d6 piercing damage (DC 21 basic Reflex save). When the skeleton mob is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Rattling Bones"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The skeletons engage using their claws and broken bones to attack each enemy in a 5-foot emanation, with a DC 21 basic Reflex save. The damage depends on the number of actions. ⬻ 1d4+1 piercing or slashing damage ⬺ 2d4+7 piercing or slashing damage ⬽ 3d4+10 piercing or slashing damageto 2 segments, this area decreases to a 5-foot burst."
sourcebook: "_Battlecry!_, page 191."
```

```encounter-table
name: Skeleton Mob
creatures:
  - 1: Skeleton Mob
```
