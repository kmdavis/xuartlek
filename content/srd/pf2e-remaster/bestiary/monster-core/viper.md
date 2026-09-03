---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Viper"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Viper"
level: -1
source: "Monster Core"
aon_id: "creature-3200"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3200"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Viper"
level: "Creature -1"
size: "Tiny"
trait_01: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +1, Stealth +5, Survival +3"
abilityMods: [-3, 4, 0, -4, 1, -2]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +7; __Will__: +5"
hp: 8
health:
  - name: "HP"
    desc: "8"
abilities_mid:
  - name: "Slink"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature ends its movement adjacent to the viper or within the viper's space"
  - name: "Effect"
    desc: "The viper Strides, Climbs, or Swims up to 10 feet (or up to the relevant Speed, if that Speed is less than 10 feet). It must end its movement in a location that isn't within 5 feet of a foe. This movement doesn't trigger reactions."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +6 (Agile, Finesse, reach 0 feet) __Damage__ 1d8–3 piercing plus viper venom"
abilities_bot:
  - name: "Viper Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d8 poison damage (1 round)"
sourcebook: "_Monster Core_, page 316."
```

```encounter-table
name: Viper
creatures:
  - 1: Viper
```
