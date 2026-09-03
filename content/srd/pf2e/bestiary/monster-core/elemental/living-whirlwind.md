---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Whirlwind"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Living Whirlwind"
level: 5
source: "Monster Core"
aon_id: "creature-2974"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2974"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Living Whirlwind"
level: "Creature 5"
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Stealth +14"
abilityMods: [3, 5, 2, -2, 1, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +9; __Ref__: +16; __Will__: +10"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "High Winds"
    desc: "(air, aura) 20 feet. Air within the emanation is difficult terrain for Flying creatures that don't have the air trait."
  - name: "Disperse"
    desc: "⬲ (air)"
  - name: "Trigger"
    desc: "The living whirlwind takes damage from a hostile action"
  - name: "Effect"
    desc: "The living whirlwind disperses. Until the end of the current turn, it can't be attacked or targeted, doesn't take up space, and its high winds aura is suppressed. At the end of the turn, the living whirlwind reforms in any unoccupied space within 25 feet of where it dispersed, and its high winds are restored."
speed: "fly 50 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ gust +14 (Finesse, reach 10 feet) __Damage__ 2d6+7 bludgeoning"
abilities_bot:
  - name: "Forceful Winds"
    desc: "⬺ (Air) The living whirlwind creates a 60-foot line of violent wind. Creatures in the area must succeed at a DC 25 Fortitude save or be pushed back 10 feet and knocked prone."
  - name: "Swiftness"
    desc: "The living whirlwind's movement doesn't trigger reactions."
sourcebook: "_Monster Core_, page 140."
```

```encounter-table
name: Living Whirlwind
creatures:
  - 1: Living Whirlwind
```
