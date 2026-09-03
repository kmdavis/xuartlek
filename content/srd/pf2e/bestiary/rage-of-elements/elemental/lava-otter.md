---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lava Otter"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/small
statblock: inline
name: "Lava Otter"
level: 1
source: "Rage of Elements"
aon_id: "creature-2633"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2633"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Lava Otter"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Stealth +7"
abilityMods: [1, 4, 1, -4, 3, 1]
abilities_top:
  - name: "Below the Crust"
    desc: "A lava otter can Sneak at its full Speed in lava."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +9; __Will__: +5"
hp: 22
health:
  - name: "HP"
    desc: "22; __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 3"
abilities_mid:
  - name: "Molten Form"
    desc: "(fire) Any creature that hits the lava otter with an unarmed Strike or otherwise touches it takes 1 fire damage. If a gallon or more of water touches the lava otter, or if it's affected by a water effect, its outer layer of lava hardens to a rocky shell, deactivating its molten form and imposing weakness 5 to bludgeoning damage. Molten form reactivates if the otter swims in lava for 1 minute."
speed: "25 feet, swim 40 feet (in lava only)"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 (Finesse) __Damage__ 1d4+1 piercing plus 1d4 fire"
  - name: "Melee"
    desc: "⬻ claw +9 (Agile, Finesse) __Damage__ 1d4+1 slashing"
abilities_bot:
  - name: "Scattering Magma"
    desc: "⬻ (Fire)"
  - name: "Requirements"
    desc: "The otter is in molten form, and its previous action was a successful jaws Strike"
  - name: "Effect"
    desc: "The otter grips with its jaws and rapidly twists, flinging lava. The otter deals 1d4 fire damage to all creatures adjacent to it."
  - name: "Tight-Knit Family"
    desc: "A lava otter can share the same space as another lava otter, but no more than two lava otters can occupy the same space. Familiar Poaching Many greedy fire wizards wish to domesticate lava otters to act as their familiars, a sentiment loathed by most denizens of the Plane of Fire. While the otters' burning pelts serve as a deterrence for would-be poachers, numerous naari (fire geniekin) still take it upon themselves to patrol lava otter habitats to protect them from poaching"
sourcebook: "_Rage of Elements_, page 129."
```

```encounter-table
name: Lava Otter
creatures:
  - 1: Lava Otter
```
