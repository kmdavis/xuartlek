---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Magma Worm"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Magma Worm"
level: 18
source: "Monster Core"
aon_id: "creature-2873"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2873"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Magma Worm"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Fire"
trait_03: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, tremorsense (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +38"
abilityMods: [10, -1, 9, -3, -1, -1]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +36; __Ref__: +25; __Will__: +27"
hp: 410
health:
  - name: "HP"
    desc: "410; __Immunities__ fire; __Weaknesses__ cold 15"
abilities_mid:
  - name: "Fire Healing"
    desc: "As long as a magma worm is in contact with a fire or body of magma at least as large as itself, it gains fast healing 20. When struck by a magical fire effect from anything other than itself, a magma worm regains Hit Points equal to half the fire damage the effect would otherwise deal."
  - name: "Inexorable"
    desc: "The cave worm recovers from the paralyzed, slowed, and stunned conditions at the end of its turn. It's also immune to penalties to its Speeds and the immobilized condition, and it ignores difficult terrain and greater difficult terrain."
  - name: "Slough Skin"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The cave worm would be affected by a condition or adverse effect (such as _cursed metamorphosis_)"
  - name: "Effect"
    desc: "The cave worm negates the triggering condition or effect by sloughing an outer layer of its skin. Effects from artifacts, deities, or a similarly powerful source can't be avoided in this way."
speed: "40 feet, burrow 40 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +36 (deadly 3d10, Fire, reach 20 feet) __Damage__ 3d10+18 piercing plus 2d6 fire and Improved Grab"
  - name: "Melee"
    desc: "⬻ stinger +36 (Agile, Fire, Poison, reach 20 feet) __Damage__ 2d12+18 piercing plus 2d6 fire and magma worm venom"
  - name: "Melee"
    desc: "⬻ body +34 (Fire, reach 15 feet) __Damage__ 2d10+16 bludgeoning plus 2d6 fire"
abilities_bot:
  - name: "Fast Swallow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The worm Grabs a creature"
  - name: "Effect"
    desc: "The worm uses Swallow Whole."
  - name: "Fire Breath"
    desc: "⬺ (Fire, Primal) The magma worm breathes a blast of flame in a 60-foot cone that deals 18d6 fire damage to all creatures in the area (DC 41 basic Reflex save). It can't use Fire Breath again for 1d4 rounds."
  - name: "Magma Worm Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 41 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and drained 1 (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage and drained 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage and drained 2 (1 round)"
  - name: "Rock Tunneler"
    desc: "A cave worm can burrow through solid stone at a Speed of 20 feet. It can leave a tunnel if it desires, and it usually does."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Huge, 3d10+10 bludgeoning plus 2d6 fire, Rupture 36"
  - name: "Thrash"
    desc: "⬺ The worm attempts one Strike against each creature in its reach. It can Strike up to once with its jaws, up to once with its stinger, and any number of times with its body. Each attack counts toward the worm's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all the attacks."
sourcebook: "_Monster Core_, page 57."
```

```encounter-table
name: Magma Worm
creatures:
  - 1: Magma Worm
```
