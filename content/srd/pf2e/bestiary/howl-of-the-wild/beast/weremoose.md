---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Weremoose"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/large
statblock: inline
name: "Weremoose"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3323"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3323"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Weremoose"
level: "Creature 3"
size: "Large"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 60 feet"
languages: "Common; deer empathy"
skills:
  - name: "Skills"
    desc: "Athletics +9, Intimidation +8"
abilityMods: [4, 1, 4, -1, 1, 1]
abilities_top:
  - name: "Deer Empathy"
    desc: "(primal) A weremoose can communicate with deer, including moose."
  - name: "Items"
    desc: "Greataxe, Hatchet (2), Scale Mail"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +11; __Ref__: +8; __Will__: +6"
hp: 60
health:
  - name: "HP"
    desc: "60; __Weaknesses__ silver 5 Cold Adaptation The weremoose treats environmental cold effects as if they were one step less extreme."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +11 (Sweep) __Damage__ 1d12+6 slashing"
  - name: "Melee"
    desc: "⬻ antler +11 __Damage__ 1d8+6 piercing plus curse of the weremoose"
  - name: "Melee"
    desc: "⬻ hatchet +11 (Agile, Sweep) __Damage__ 1d6+6 slashing"
  - name: "Ranged"
    desc: "⬻ hatchet +8 (Agile, thrown 10 feet) __Damage__ 1d6+6 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) Medium human with fist +11 for 1d4+6 bludgeoning, or Large moose with antler and hoof +11 for 1d8+6 bludgeoning."
  - name: "Curse of the Weremoose"
    desc: "(Curse, Primal) Saving Throw DC 17 Fortitude"
  - name: "Moon Frenzy"
    desc: "(Polymorph, Primal) Increases antler damage instead of jaws."
  - name: "Thundering Charge"
    desc: "⬺ The weremoose Strides twice and then makes an antler Strike. A Medium or smaller creature damaged by this attack must succeed at a DC 17 Fortitude save or be stunned 1."
sourcebook: "_Howl of the Wild_, page 196."
```

```encounter-table
name: Weremoose
creatures:
  - 1: Weremoose
```
