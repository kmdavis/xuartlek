---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dream Spider"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Dream Spider"
level: 0
source: "Monster Core 2"
aon_id: "creature-4561"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4561"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Dream Spider"
level: "Creature 0"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, web sense"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +2, Stealth +7"
abilityMods: [0, 3, 1, -5, 0, -4]
abilities_top:
  - name: "Web Sense"
    desc: "The dream spider has imprecise tremorsense to detect the vibrations of creatures touching its web."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15"
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +7 (Finesse) __Damage__ 1d6 piercing plus dream spider venom"
  - name: "Ranged"
    desc: "⬻ web +7 (range increment 10 feet) __Damage__ web trap plus dream spider venom"
abilities_bot:
  - name: "Dream Spider Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage plus stupefied 1 (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the dream spider's web attack is immobilized and stuck to the nearest surface until it Escapes (DC 16). Venom Addicts Talented alchemists process dream spider venom into an addictive drug. Those who become addicted can be driven in desperation to seek out dream spiders and allow the creatures to bite their flesh to get their fix—an arrangement that backfires horribly as the spiders feed."
sourcebook: "_Monster Core 2_, page 302."
```

```encounter-table
name: Dream Spider
creatures:
  - 1: Dream Spider
```
