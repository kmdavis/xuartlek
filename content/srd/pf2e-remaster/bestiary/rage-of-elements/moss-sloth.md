---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Moss Sloth"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/small
statblock: inline
name: "Moss Sloth"
level: 2
source: "Rage of Elements"
aon_id: "creature-2671"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2671"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Moss Sloth"
level: "Creature 2"
size: "Small"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
skills:
  - name: "Skills"
    desc: "Nature +7, Survival +8"
abilityMods: [3, 0, 4, -4, 2, 1]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +3; __Will__: +11"
hp: 40
health:
  - name: "HP"
    desc: "40 , regeneration 5 (deactivated by fire); __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ bludgeoning 5; __Weaknesses__ fire 4, slashing 3"
abilities_mid:
  - name: "Insect Swarm"
    desc: "The first time each day that the moss sloth takes damage from a bludgeoning melee attack, a patch of moss collapses inward, releasing insects that swarm the attacking creature and deal 2d4 piercing damage (DC 15 basic Reflex save)."
speed: "10 feet, climb 15 feet; hold fast"
attacks:
  - name: "Melee"
    desc: "⬻ wooden claw +9 __Damage__ 1d8+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ fruit +6 (range increment 15 feet) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Hold Fast"
    desc: "A moss sloth can climb on ceilings and other inverted surfaces, though it treats such surfaces as difficult terrain."
sourcebook: "_Rage of Elements_, page 206."
```

```encounter-table
name: Moss Sloth
creatures:
  - 1: Moss Sloth
```
