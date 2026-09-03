---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elemental Inferno"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/huge
statblock: inline
name: "Elemental Inferno"
level: 11
source: "Monster Core"
aon_id: "creature-2984"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2984"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elemental Inferno"
level: "Creature 11"
size: "Huge"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, smoke vision"
languages: "Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +21"
abilityMods: [6, 6, 5, 0, 3, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The elemental inferno ignores the concealed condition from smoke."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +23; __Will__: +19"
hp: 210
health:
  - name: "HP"
    desc: "210 (explosion); __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 15, water 10"
abilities_mid:
  - name: "Explosion"
    desc: "(fire) When the elemental inferno dies, it explodes, dealing 7d6 fire damage to each creature in a 10-foot emanation (DC 30 basic Reflex save)."
  - name: "Intense Heat"
    desc: "(aura, fire) 10 feet, 7d6 fire, DC 28 basic Reflex"
speed: "70 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +24 (reach 15 feet) __Damage__ 2d10+12 fire plus 3d8 persistent fire"
  - name: "Ranged"
    desc: "⬻ fire mote +24 (range increment 60 feet) __Damage__ 2d10+6 fire"
abilities_bot:
  - name: "Blue Flames"
    desc: "When the elemental inferno scores a critical hit, its body surges with blue flames, increasing the damage of its intense heat and Inferno Leap by 3d6 until the start of its next turn."
  - name: "Inferno Leap"
    desc: "⬺ (Fire) The elemental inferno jumps horizontally and vertically with a maximum height and distance each equal to its Speed. Its intense heat is suppressed until the end of the jump. Instead, at any point during the jump, flames explode from the elemental in a 30-foot emanation, dealing 12d6 fire damage to each creature within the area (DC 30 basic Reflex save). The elemental inferno can't Inferno Leap again for 1d4 rounds."
sourcebook: "_Monster Core_, page 145."
```

```encounter-table
name: Elemental Inferno
creatures:
  - 1: Elemental Inferno
```
