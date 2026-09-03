---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ice Troll"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/large
statblock: inline
name: "Ice Troll"
level: 4
source: "Monster Core 2"
aon_id: "creature-4591"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4591"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ice Troll"
level: "Creature 4"
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Troll"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +10, Intimidation +10, Survival +10"
abilityMods: [5, 2, 5, -2, 2, -2]
abilities_top:
  - name: "Easily Misled"
    desc: "The ice troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
  - name: "Items"
    desc: "Hatchet"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +13; __Ref__: +10; __Will__: +8"
hp: 90
health:
  - name: "HP"
    desc: "90 , regeneration 15 (deactivated by fire or sonic); __Immunities__ cold; __Weaknesses__ fire 10, sonic 10"
abilities_mid:
  - name: "Furious Carve"
    desc: "⬲"
  - name: "Trigger"
    desc: "The ice troll takes fire or sonic damage"
  - name: "Effect"
    desc: "The troll makes a hatchet or claw Strike against a random creature within reach. If the ice troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
speed: "30 feet; ice passage"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 (reach 10 feet) __Damage__ 2d8+5 piercing"
  - name: "Melee"
    desc: "⬻ hatchet +13 (Agile, reach 10 feet, sweep) __Damage__ 2d6+5 slashing"
  - name: "Melee"
    desc: "⬻ claw +13 (Agile, reach 10 feet) __Damage__ 2d4+5 slashing"
  - name: "Ranged"
    desc: "⬻ hatchet +10 (Agile, sweep, thrown 10 feet) __Damage__ 2d6+5 slashing"
abilities_bot:
  - name: "Brutal Sweep"
    desc: "⬽"
  - name: "Requirements"
    desc: "The ice troll is wielding a hatchet"
  - name: "Effect"
    desc: "The troll sweeps their hatchet in a large arc, dealing 3d6 slashing damage to all creatures in a 5-foot emanation (DC 18 basic Reflex save)."
  - name: "Ice Passage"
    desc: "An ice troll isn't impeded by difficult terrain caused by snow or ice, nor do they need to attempt Acrobatics checks to keep from falling on slippery ice."
  - name: "Rend"
    desc: "⬻ claw Mixing Variations Cavern trolls and ice trolls spawn their own jotund trolls, two-headed trolls, and warleaders. In these cases, change their immunity, regeneration, and weaknesses to match their origin. You can also update their reaction's trigger and its persistent damage removal to match those weaknesses."
sourcebook: "_Monster Core 2_, page 328."
```

```encounter-table
name: Ice Troll
creatures:
  - 1: Ice Troll
```
