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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; deer empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8"
abilityMods: [4, 1, 4, -1, 1, 1]
abilities_top:
  - name: "Deer Empathy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) A weremoose can communicate with deer, including moose."
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
    desc: "⬻ greataxe +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+6 slashing"
  - name: "Melee"
    desc: "⬻ antler +11 __Damage__ 1d8+6 piercing plus curse of the weremoose"
  - name: "Melee"
    desc: "⬻ hatchet +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+6 slashing"
  - name: "Ranged"
    desc: "⬻ hatchet +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+6 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Medium human with fist +11 for 1d4+6 bludgeoning, or Large moose with antler and hoof +11 for 1d8+6 bludgeoning."
  - name: "Curse of the Weremoose"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Saving Throw DC 17 Fortitude"
  - name: "Moon Frenzy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Increases antler damage instead of jaws."
  - name: "Thundering Charge"
    desc: "⬺ The weremoose Strides twice and then makes an antler Strike. A Medium or smaller creature damaged by this attack must succeed at a DC 17 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]."
sourcebook: "_Howl of the Wild_, page 196."
```

```encounter-table
name: Weremoose
creatures:
  - 1: Weremoose
```
