---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeletal Titan"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Skeletal Titan"
level: 13
source: "Monster Core 2"
aon_id: "creature-4550"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4550"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Skeletal Titan"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +28"
abilityMods: [9, 3, 4, -5, 2, -1]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +24; __Will__: +21"
hp: 210
health:
  - name: "HP"
    desc: "210 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 10, electricity 10, fire 10, piercing 15, slashing 15"
speed: "40 feet, fly 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mountain sword +26 (reach 20 feet) __Damage__ 3d12+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, reach 15 feet) __Damage__ 3d8+13 slashing"
  - name: "Melee"
    desc: "⬻ foot +26 (reach 15 feet) __Damage__ 3d8+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ bone +24 (Brutal, range increment 60 feet) __Damage__ 2d10+13 plus bone debris"
abilities_bot:
  - name: "Bone Debris"
    desc: "The bones a skeletal titan throws are large enough to clutter the battlefield. When the skeletal titan hits a creature with a bone attack, the projectile becomes difficult terrain in the square the creature occupies (or, if the creature occupies more than one square, one square it occupies of the titan's choice). If the titan misses with a bone attack, instead a random square adjacent to the creature becomes difficult terrain."
  - name: "Mountain Slam"
    desc: "⬽ The skeletal titan slams its mountain sword into the ground. The shock wave reverberates, dealing 3d12+13 bludgeoning damage to all creatures in a 20-foot line (DC 33 basic Reflex save). A creature that fails its save is also knocked prone."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 33"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31 - __Constant (7th)__ Fly"
sourcebook: "_Monster Core 2_, page 291."
```

```encounter-table
name: Skeletal Titan
creatures:
  - 1: Skeletal Titan
```
