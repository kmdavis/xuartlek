---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Trained Raven"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Trained Raven"
level: -1
source: "Monster Core 2"
aon_id: "creature-4527"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4527"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Trained Raven"
level: "Creature -1"
size: "Tiny"
trait_01: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Deception +5, Thievery +5"
abilityMods: [-3, 3, 0, -4, 3, 0]
abilities_top:
  - name: "Cunning"
    desc: "A raven can use simple items as tools, such as poking a stick at an opening to tease out a piece of food. They're also quite adept at stealing objects. A raven can't use Thievery to Palm an Object, Disable a Device, or Pick a Lock, but it can use Thievery to Steal light objects that it can carry in its beak or talons or to accomplish other relatively simple tasks."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +7; __Will__: +5"
hp: 7
health:
  - name: "HP"
    desc: "7"
speed: "10 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +7 (Finesse) __Damage__ 1d4—1 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "A raven's melee Strikes deal an additional 1d4 precision damage to off-guard creatures. Raven Traders Given enough time to develop the relationship and establish what you want, it's possible to engage a raven in a sort of trade. Placing a small, shiny object where the raven can take it might entice it to grab the prize and fly off, returning 3d6 minutes later with something from its own stash. Convincing a raven to trade requires a successful DC 20 Nature check to Command an Animal and, of course, a raven who has the inclination to trade with you in the first place."
sourcebook: "_Monster Core 2_, page 267."
```

```encounter-table
name: Trained Raven
creatures:
  - 1: Trained Raven
```
