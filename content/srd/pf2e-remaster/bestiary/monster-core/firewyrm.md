---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Firewyrm"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/huge
statblock: inline
name: "Firewyrm"
level: 9
source: "Monster Core"
aon_id: "creature-2983"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2983"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Firewyrm"
level: "Creature 9"
size: "Huge"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, smoke vision"
languages: "Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +20"
abilityMods: [5, 5, 4, -1, 3, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The firewyrm ignores the concealed condition from smoke."
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +18; __Ref__: +20; __Will__: +15"
hp: 165
health:
  - name: "HP"
    desc: "165 (explosion); __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 10, water 10"
abilities_mid:
  - name: "Explosion"
    desc: "(fire) When the firewyrm dies, it explodes, dealing 6d6 fire damage to each creature in a 10-foot emanation (DC 28 basic Reflex save). Intense Heat(aura, fire) 10 feet, 4d6 fire, DC 25 basic Reflex"
speed: "60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +20 (reach 15 feet) __Damage__ 2d8+11 fire plus 2d8 persistent fire"
  - name: "Ranged"
    desc: "⬻ fire mote +20 (range increment 60 feet) __Damage__ 2d8+6 fire"
abilities_bot:
  - name: "Breathe Fire"
    desc: "⬺ (Fire, Primal) The firewyrm breathes a 30-foot cone of fire dealing 7d6 fire and 2d8 persistent fire damage to every creature within the cone (DC 28 basic Reflex save). The firewyrm can't Breathe Fire again for 1d4 rounds."
sourcebook: "_Monster Core_, page 144."
```

```encounter-table
name: Firewyrm
creatures:
  - 1: Firewyrm
```
