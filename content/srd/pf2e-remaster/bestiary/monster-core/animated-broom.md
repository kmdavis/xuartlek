---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Broom"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/small
statblock: inline
name: "Animated Broom"
level: -1
source: "Monster Core"
aon_id: "creature-2818"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2818"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Animated Broom"
level: "Creature -1"
size: "Small"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +5"
abilityMods: [0, 1, 0, -5, 0, -5]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +3; __Ref__: +6; __Will__: +3 construct armor"
hp: 6
health:
  - name: "HP"
    desc: "6; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 2"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated broom has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated broom is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 13."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bristles +6 (Agile, Magical, Finesse) __Damage__ 1d4 bludgeoning plus dust"
abilities_bot:
  - name: "Dust"
    desc: "A creature hit by an animated broom's bristles must succeed at a DC 15 Fortitude save or spend its next action coughing. Even if hit by multiple dust attacks, the creature has to spend only 1 action coughing to clear the dust out. A creature who doesn't breathe is immune to this effect."
sourcebook: "_Monster Core_, page 18."
```

```encounter-table
name: Animated Broom
creatures:
  - 1: Animated Broom
```
