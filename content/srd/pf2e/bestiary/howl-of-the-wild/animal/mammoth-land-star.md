---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mammoth Land Star"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/huge
statblock: inline
name: "Mammoth Land Star"
level: 8
source: "Howl of the Wild"
aon_id: "creature-3298"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3298"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Mammoth Land Star"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
trait_02: "Mindless"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; scent (precise) 100 feet, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +16, Stealth +15, Survival +18"
abilityMods: [6, 3, 6, -5, 4, -2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +13; __Will__: +15"
hp: 100
health:
  - name: "HP"
    desc: "25 (limb), regrowth; __Immunities__ mental"
abilities_mid:
  - name: "Limb Regrowth"
    desc: "A healthy mammoth land star typically has five limbs. A creature can sever a limb by targeting it and dealing damage equal to the limb's Hit Points. The mammoth land star can regrow a missing limb over the course of 24 hours."
  - name: "Regrowth"
    desc: "Whenever a limb is severed, it must attempt a DC 5 flat check. On a success, the limb will slowly begin to grow into a new mammoth land star over the course of a week, unless it is doused in acid or fire."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ feet +20 (Agile, reach 10 feet) __Damage__ 1d4+6 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ limb spines +20 (reach 10 feet) __Damage__ 2d8+6 piercing plus spiny venom"
abilities_bot:
  - name: "Detach"
    desc: "⬺ (Move)"
  - name: "Requirements"
    desc: "The mammoth land star falls below half its total Hit Points"
  - name: "Effect"
    desc: "The mammoth land star severs one of its own limbs as a distraction, then Strides three times. This movement doesn't trigger reactions."
  - name: "Digest"
    desc: "⬻"
  - name: "Requirements"
    desc: "The mammoth land star has a target grabbed"
  - name: "Effect"
    desc: "The mammoth land star extrudes its stomach onto its prey and digests it alive. The target takes 2d12+6 acid damage and is drained 1."
  - name: "Glide"
    desc: "⬺ (Move) The land star blows air through its feet to hover 1 foot in the air and Strides twice with a +5-foot circumstance bonus to Speed, ignoring uneven ground and difficult terrain below it."
  - name: "Pry"
    desc: "⬻"
  - name: "Requirements"
    desc: "The mammoth land star has a target grabbed that is wearing armor"
  - name: "Effect"
    desc: "The mammoth land star makes a feet Strike against a creature it has grabbed. If that Strike hits and the creature is wearing armor with Hardness 12 or lower, the armor is broken. This Strike doesn't further damage armor that's already broken."
  - name: "Spiny Venom"
    desc: "(Incapacitation, Poison)"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and slowed 1"
  - name: "Stage 2"
    desc: "2d6 poison and slowed 2"
  - name: "Stage 3"
    desc: "2d8 poison and paralyzed"
sourcebook: "_Howl of the Wild_, page 169."
```

```encounter-table
name: Mammoth Land Star
creatures:
  - 1: Mammoth Land Star
```
