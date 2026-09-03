---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Frog"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Frog"
level: 1
source: "Monster Core 2"
other_sources: "Pathfinder Game Night: Dawn of the Frogs (Deluxe Adventure)"
aon_id: "creature-4404"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4404"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Frog"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +6, Stealth +7"
abilityMods: [3, 2, 3, -4, 2, -1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +7; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d6+3 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tongue +8 (reach 15 feet) __Damage__ tongue grab"
abilities_bot:
  - name: "Sticky Feet"
    desc: "Giant frogs are not off-guard when Balancing on a narrow surface, and they gain a +4 circumstance bonus to Reflex saves to avoid falling."
  - name: "Tongue Grab"
    desc: "A creature hit by the giant frog's tongue becomes grabbed by the giant frog. The creature isn't immobilized, but it can't move beyond the reach of the frog's tongue. A creature can sever the tongue with a Strike against AC 13 that deals at least 2 slashing damage. This deals no damage to the frog but prevents it from using its tongue Strike until it regrows its tongue, which takes a week."
sourcebook: "_Monster Core 2_, page 158."
```

```encounter-table
name: Giant Frog
creatures:
  - 1: Giant Frog
```
