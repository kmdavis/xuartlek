---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tardigrade Swarm"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Tardigrade Swarm"
level: 12
source: "Howl of the Wild"
aon_id: "creature-3317"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3317"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Tardigrade Swarm"
level: "Creature 12"
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; tremorsense (imprecise) 30 ft"
skills:
  - name: "Skills"
    desc: "Athletics +19, Survival +21"
abilityMods: [2, 4, 6, -5, 3, 1]
abilities_top:
  - name: "Eyespots"
    desc: "A tardigrade swarm can't see anything beyond 30 feet."
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +26; __Ref__: +21; __Will__: +19"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ precision, swarm mind; __Resistances__ all damage 10 (except area and splash)"
abilities_mid:
  - name: "Tun Marbles"
    desc: "As the tardigrade swarm is damaged, the bodies of those that enter a tun state make the ground treacherous. When the tardigrade swarm drops below 70 Hit Points, the space they occupy is considered difficult terrain."
speed: "25 feet, climb 25 feet"
abilities_bot:
  - name: "Stylets"
    desc: "⬻ Each enemy in the swarm's space takes 4d8 piercing damage (DC 32 basic Reflex save). Creatures that fail their save become drained 1 or increase their drained condition by one, to a maximum of drained 4."
sourcebook: "_Howl of the Wild_, page 187."
```

```encounter-table
name: Tardigrade Swarm
creatures:
  - 1: Tardigrade Swarm
```
