---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zombie Dragon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/huge
statblock: inline
name: "Zombie Dragon"
level: 9
source: "Monster Core 2"
aon_id: "creature-4622"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4622"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Zombie Dragon"
level: "Creature 9"
size: "Huge"
trait_01: "Dragon"
trait_02: "Mindless"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Athletics +19"
abilityMods: [6, 3, 4, -5, 3, -2]
abilities_top:
  - name: "Slow"
    desc: "A zombie dragon is permanently slowed 1 and can't use reactions."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +18; __Will__: +16"
hp: 210
health:
  - name: "HP"
    desc: "210 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Weaknesses__ slashing 10, vitality 10"
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ upper jaw +21 (reach 15 feet) __Damage__ 2d10+12 piercing"
  - name: "Melee"
    desc: "⬻ claw +21 (Agile, reach 10 feet) __Damage__ 2d8+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +19 (reach 20 feet) __Damage__ 2d6+12 bludgeoning"
abilities_bot:
  - name: "Viscera Breath"
    desc: "⬺ (Poison) The zombie dragon breathes a wave of fetid viscera that deals 5d6 bludgeoning damage and 5d6 poison damage (DC 28 basic Reflex save). A creature that critically fails is also sickened 2. The zombie dragon can't use Viscera Breath again for 1d4 rounds. Hoarding Instincts Though zombies have no use for wealth—indeed, most don't understand the concept in the first place—zombie dragons retain a hint of their innate tendency to hoard. A fresher corpse might guard the hoard it gathered in life (or what remains of it), while a zombie dragon further from life might instead hoard bones, rocks, corpses, or other unusual objects. The monetary value of these hoards varies widely."
sourcebook: "_Monster Core 2_, page 359."
```

```encounter-table
name: Zombie Dragon
creatures:
  - 1: Zombie Dragon
```
