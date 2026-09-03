---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fire Giant"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Fire Giant"
level: 10
source: "Monster Core"
aon_id: "creature-3014"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3014"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Fire Giant"
level: "Creature 10"
size: "Large"
trait_01: "Fire"
trait_02: "Giant"
trait_03: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +18"
abilityMods: [7, 0, 5, 2, 2, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/greatsword|greatsword]]_, _+1 [[srd/pf2e/compendium/equipment/armor#Half Plate|half plate]]_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +23; __Ref__: +16; __Will__: +18"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatsword_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d12+13 slashing"
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ flame +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], range 120 feet) __Damage__ 4d6 fire plus 2d6 persistent fire"
abilities_bot:
  - name: "Flaming Stroke"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The fire giant imbues their blade with flames and makes a greatsword Strike with a –2 circumstance penalty against each creature in a 15-foot line. They make one attack roll only and compare the result to each creature's AC. This Strike deals an additional 1d6 fire damage and counts as one attack for the fire giant's multiple attack penalty."
sourcebook: "_Monster Core_, page 166."
```

```encounter-table
name: Fire Giant
creatures:
  - 1: Fire Giant
```
