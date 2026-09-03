---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Flash Beetle"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Flash Beetle"
level: -1
source: "Monster Core"
aon_id: "creature-2852"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2852"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Flash Beetle"
level: "Creature -1"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +4"
abilityMods: [1, 3, 2, -5, 1, -2]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +8; __Will__: +4"
hp: 6
health:
  - name: "HP"
    desc: "6"
abilities_mid:
  - name: "Luminescent Aura"
    desc: "(aura, light) 10 feet. The flash beetle's bioluminescent organs fill the area with bright light."
speed: "20 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +8 (Agile, Finesse) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Light Flash"
    desc: "⬻ (Concentrate, Light) The flash beetle creates a brilliant flash of light. All creatures in its luminescent aura must succeed at a DC 17 Fortitude save or be dazzled for 1 minute. The flash beetle's glow then goes out, disabling its aura for 24 hours, during which time it cannot use Light Flash. Light Glands Beetles do not collect treasure, but the two light-producing organs of a flash beetle can be recovered from the creature and used for illumination-based chemical recipes, spell components, and magic item creation."
sourcebook: "_Monster Core_, page 42."
```

```encounter-table
name: Flash Beetle
creatures:
  - 1: Flash Beetle
```
