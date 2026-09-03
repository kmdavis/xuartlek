---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Coppermouth"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Coppermouth"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3283"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3283"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Giant Coppermouth"
level: "Creature 7"
size: "Medium"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, greater electrolocation 20 feet, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +14, Stealth +17, Survival +15"
abilityMods: [3, 6, 4, -4, 4, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "The giant coppermouth can hold its breath for 1 hour."
  - name: "Greater Electrolocation"
    desc: "A giant coppermouth can sense minute electrical charges in living creatures, which it can use as a precise sense at a range of 20 feet. This distance increases to 100 feet against any creature that has used an electricity effect within the last minute."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +18; __Will__: +12"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ electricity"
speed: "30 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +18 (Electricity, Finesse) __Damage__ 2d8+6 piercing plus 1d4 electricity and coppermouth venom"
abilities_bot:
  - name: "Coppermouth Venom"
    desc: "(Electricity, Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and 1d6 electricity (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison and 1d6 electricity and clumsy 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison and 2d6 electricity and clumsy 2"
  - name: "Quickening Jolt"
    desc: "⬺ (Electricity) The coppermouth manipulates its own nervous system by increasing its reaction time, Striding and making two Strikes against different targets during the movement. Both attacks count toward its multiple attack penalty, but the penalty doesn't increase until after it has made both attacks."
  - name: "Venomous Spit"
    desc: "⬺ (Electricity, Poison) The coppermouth unleashes a stream of electrified venom in a 30-foot line. The venom deals 8d6 electricity damage (DC 22 basic Reflex save) and creatures that take damage from the venom are immediately exposed to coppermouth venom. The copper mouth can't use Venomous Spit again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 152."
```

```encounter-table
name: Giant Coppermouth
creatures:
  - 1: Giant Coppermouth
```
