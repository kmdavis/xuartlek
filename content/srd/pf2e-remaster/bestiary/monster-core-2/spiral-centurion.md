---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spiral Centurion"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/medium
statblock: inline
name: "Spiral Centurion"
level: 11
source: "Monster Core 2"
aon_id: "creature-4563"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4563"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Spiral Centurion"
level: "Creature 11"
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +23"
abilityMods: [6, 6, 5, -5, 2, -5]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +22; __Ref__: +25; __Will__: +16"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 10"
abilities_mid:
  - name: "Top-Heavy"
    desc: "A spiral centurion's top-like design makes it susceptible to effects that would cause it to fall prone. The DC of any attempt to knock the spiral centurion prone is reduced by 5. If the spiral centurion attempts a check or saving throw to resist being knocked prone, it takes a –5 status penalty. A spiral centurion that has been knocked prone can't use any actions other than to attempt to Stand, but it must succeed at a DC 30 Acrobatics check to do so."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ blade +23 (Agile, sweep) __Damage__ 2d12+12 slashing"
abilities_bot:
  - name: "Hurl Blade"
    desc: "⬺ The spiral centurion hurls one of its blades with an angled spin to ensure a swooping flight path. The blade deals 6d6 slashing damage to each creature in a 40-foot line (DC 30 basic Reflex save). At the start of the spiral centurion's next turn, the blade swoops around and returns along the same flight path, again dealing 6d6 slashing damage (DC 30 basic Reflex save) to each creature along the same line."
  - name: "Rev Up"
    desc: "⬻"
  - name: "Requirements"
    desc: "The spiral centurion hasn't acted yet this turn"
  - name: "Effect"
    desc: "The spiral centurion Strides up to its Speed. It then gains a +2 circumstance bonus to attack and damage rolls until the end of its turn."
  - name: "Trample"
    desc: "⬽ Medium or smaller, blade, DC 30"
  - name: "Whirling Death"
    desc: "⬽ The spiral centurion spins furiously in place, its blades extended to slice through nearby creatures. It makes up to five melee blade Strikes. No single creature can be targeted by more than one blade Strike during one use of this ability. These attacks count toward the spiral centurion's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks are made. Spiral Centurion Glitches A spiral centurion might have one of the following glitches."
  - name: "Dulled Blades"
    desc: "Its blade Strike deals only 2d10+5 bludgeoning damage."
  - name: "Misaligned Gears"
    desc: "It loses Rev Up, and if it Strides more than once per round, it takes 1d10 damage."
  - name: "Stuck in a Rut"
    desc: "It uses the same actions each round, regardless of the circumstances."
sourcebook: "_Monster Core 2_, page 303."
```

```encounter-table
name: Spiral Centurion
creatures:
  - 1: Spiral Centurion
```
