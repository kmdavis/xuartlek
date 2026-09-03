---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fangtooth School"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Fangtooth School"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3276"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3276"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Fangtooth School"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision, scent (imprecise) 120 feet, wavesense (precise) 15 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5"
abilityMods: [-2, 3, 2, -5, 2, -3]
abilities_top:
  - name: "Sunless Sight"
    desc: "While in bright light, the fangtooth fish school is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]]."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +10; __Will__: +9"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 5, piercing 2, slashing 5; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "swim 30 feet"
abilities_bot:
  - name: "Bite and Gnaw"
    desc: "⬻ Each enemy in the school's space takes 2d8 piercing damage (DC 19 basic Reflex save)."
sourcebook: "_Howl of the Wild_, page 149."
```

```encounter-table
name: Fangtooth School
creatures:
  - 1: Fangtooth School
```
