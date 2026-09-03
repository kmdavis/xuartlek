---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Weretiger"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/medium
statblock: inline
name: "Weretiger"
level: 4
source: "Monster Core"
aon_id: "creature-3238"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3238"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Weretiger"
level: "Creature 4"
size: "Medium"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; tiger empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [4, 3, 3, 0, 3, -1]
abilities_top:
  - name: "Tiger Empathy"
    desc: "The weretiger can communicate with felines."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +13; __Will__: +9"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ silver 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 2d6+7 piercing plus curse of the weretiger and Grab"
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d4+7 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Human with fist +14 for 1d4+7 bludgeoning, or tiger with Speed 30 feet and Wrestle (Wrestle ⬻ The tiger makes a claw Strike against a creature it is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbing]]. If the attack hits, that creature is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]])."
  - name: "Curse of the Weretiger"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Moon Frenzy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Pounce"
    desc: "⬻ The weretiger Strides and makes a Strike at the end of that movement. If the weretiger began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], they remain hidden until after this ability's Strike."
  - name: "Rend"
    desc: "⬻ claw"
sourcebook: "_Monster Core_, page 347."
```

```encounter-table
name: Weretiger
creatures:
  - 1: Weretiger
```
