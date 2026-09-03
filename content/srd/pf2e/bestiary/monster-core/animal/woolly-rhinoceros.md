---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Woolly Rhinoceros"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Woolly Rhinoceros"
level: 6
source: "Monster Core"
aon_id: "creature-3169"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3169"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Woolly Rhinoceros"
level: "Creature 6"
size: "Large"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +13"
abilityMods: [6, 1, 5, -4, 3, -1]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +11; __Will__: +15 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Cold Adaptation"
    desc: "The woolly rhinoceros treats environmental cold effects as if they were one step less severe."
  - name: "Ferocity"
    desc: "⬲"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+6 piercing"
  - name: "Melee"
    desc: "⬻ foot +16 __Damage__ 2d8+6 bludgeoning"
abilities_bot:
  - name: "Rhinoceros Charge"
    desc: "⬺ The rhinoceros Strides twice, then makes a horn Strike. As long as the rhinoceros moved at least 20 feet, the Strike's damage increases to 3d12+6. A Medium or smaller creature struck by this attack must succeed at a DC 24 Reflex save or be automatically [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shoved]]back 5 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] by the force of the blow."
  - name: "Trample"
    desc: "⬽ Medium or smaller, foot, DC 21"
sourcebook: "_Monster Core_, page 293."
```

```encounter-table
name: Woolly Rhinoceros
creatures:
  - 1: Woolly Rhinoceros
```
