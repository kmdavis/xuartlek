---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rhinoceros"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Rhinoceros"
level: 4
source: "Monster Core"
aon_id: "creature-3168"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3168"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Rhinoceros"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [6, 0, 4, -4, 3, -1]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +14; __Ref__: +8; __Will__: +11"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +14 __Damage__ 2d8+6 piercing"
  - name: "Melee"
    desc: "⬻ foot +12 __Damage__ 2d6+6 bludgeoning"
abilities_bot:
  - name: "Rhinoceros Charge"
    desc: "⬺ The rhinoceros Strides twice, then makes a horn Strike. As long as the rhinoceros moved at least 20 feet, the Strike's damage increases to 3d8+6. A Medium or smaller creature struck by this attack must succeed at a DC 21 Reflex save or be automatically [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shoved]] back 5 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] by the force of the blow."
  - name: "Trample"
    desc: "⬺ Medium or smaller, foot, DC 18"
sourcebook: "_Monster Core_, page 293."
```

```encounter-table
name: Rhinoceros
creatures:
  - 1: Rhinoceros
```
