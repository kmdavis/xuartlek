---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Despairing Pall"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Despairing Pall"
level: 1
source: "Rage of Elements"
aon_id: "creature-2617"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2617"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Despairing Pall"
level: "Creature 1"
size: "Small"
trait_01: "Air"
trait_02: "Elemental"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Intimidation +6, Stealth +8"
abilityMods: [0, 4, 1, 0, 0, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ bleed, electricity, paralyzed, poison, sleep"
abilities_mid:
  - name: "Duskflow"
    desc: "⬲ (darkness)"
  - name: "Trigger"
    desc: "The despairing pall is damaged by a melee Strike"
  - name: "Effect"
    desc: "Darkness billows out from the despairing pall, covering its attacker in inky shadow. The despairing pall immediately Steps up to 15 feet in any direction. If the despairing pall took the triggering damage due to a reaction it provoked by moving, it can then finish the movement. For one round, the triggering attacker is cloaked in darkness and perceives light as one step lower (bright light becomes dim light, for example), affecting its ability to sense creatures and objects accordingly."
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hot air +7 (Air) __Damage__ pushed 5 feet"
  - name: "Ranged"
    desc: "⬻ lightning bolt +7 (Electricity, range increment 50 feet) __Damage__ 1d6 electricity"
abilities_bot:
  - name: "Downcast"
    desc: "⬺ (Air, Emotion, Mental) The despairing pall Flies up to its Speed, then rains gloom and despair in a 15-foot line straight down. Creatures in the area must succeed at a DC 16 Will save or take a –1 status penalty to attack rolls until the end of the despairing pall's next turn."
sourcebook: "_Rage of Elements_, page 82."
```

```encounter-table
name: Despairing Pall
creatures:
  - 1: Despairing Pall
```
