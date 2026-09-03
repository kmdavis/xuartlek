---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phoenix"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Phoenix"
level: 15
source: "Monster Core"
aon_id: "creature-3137"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3137"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phoenix"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Fire"
trait_03: "Holy"
trait_04: "Rare"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, _detect magic_, _see the unseen_"
languages: "Common, Empyrean, Pyric, Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +27, Diplomacy +31, Intimidation +27, Nature +25"
abilityMods: [6, 7, 5, 7, 6, 6]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +31; __Will__: +28 +1 status to all saves vs. magic"
hp: 300
health:
  - name: "HP"
    desc: "300 , regeneration 20 (deactivated by cold or unholy); __Immunities__ fire; __Weaknesses__ cold 10, unholy 10"
abilities_mid:
  - name: "Shroud of Flame"
    desc: "(aura, fire, primal) 20 feet. 4d6 fire, DC 37 basic Reflex save. While this aura is active, any adjacent creature that hits the phoenix with a melee attack or otherwise touches them takes 2d6 fire damage. The phoenix can activate or deactivate the aura with a single action, which has the concentrate trait."
  - name: "Self-Resurrection"
    desc: "(healing, primal) When a phoenix dies, they collapse into a pile of smoldering ashes before returning to life fully healed 1d4 rounds later, as if subject to a 7th-rank _resurrect_ ritual. Self-resurrection happens only if there are some remains to resurrect; for instance, a phoenix killed by a _disintegrate_ spell can't use this ability. A phoenix whose remains rest within an area devoted to an unholy deity by _consecrate_ can't self-resurrect until their remains are no longer in that area. A phoenix can self-resurrect only once per year."
speed: "25 feet, fly 70 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +30 (Finesse, Fire, Magical, reach 20 feet) __Damage__ 1d12+9 piercing plus 3d8 fire and 2d10 persistent fire"
  - name: "Melee"
    desc: "⬻ talon +30 (Agile, Finesse, Fire, Magical, reach 20 feet) __Damage__ 1d6+6 piercing plus 3d8 fire and 2d10 persistent fire"
  - name: "Ranged"
    desc: "⬻ flame jet +30 (Fire, range increment 40 feet) __Damage__ 6d6 fire plus 2d10 persistent fire"
abilities_bot:
  - name: "Primal Inante Spells"
    desc: "DC 39 - __Cantrips (8th)__ Light - __6th__ Cleanse Affliction (x3) - __7th__ Dispel Magic (at will) - __8th__ Cleanse Affliction, Dispel Magic (x3), Divine Immolation, Everlight (at will), Heal (x3), Wall of Fire (x3) - __Constant (6th)__ See the Unseen - __Constant (8th)__ Detect Magic"
  - name: "Flaming Strafe"
    desc: "⬻ (Fire, Primal) The phoenix blazes with superheated flame and Flies up to their Speed. They deal 6d6 fire damage to each creature within 20 feet of each square they move through (DC 37 basic Reflex save). Servants of Sarenrae While phoenixes are not denizens of the Outer Planes, they have long been associated with the goddess Sarenrae. Indeed, many phoenixes view the Dawnflower as their patron and subscribe to her mission of redeeming those who have fallen to evil."
sourcebook: "_Monster Core_, page 264."
```

```encounter-table
name: Phoenix
creatures:
  - 1: Phoenix
```
