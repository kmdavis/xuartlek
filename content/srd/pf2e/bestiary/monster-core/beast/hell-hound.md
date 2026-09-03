---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hell Hound"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Hell Hound"
level: 3
source: "Monster Core"
aon_id: "creature-3047"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3047"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hell Hound"
level: "Creature 3"
size: "Medium"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Fire"
trait_04: "Unholy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, scent (imprecise) 60 feet"
languages: "Diabolic; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +9, Stealth +8, Survival +9"
abilityMods: [4, 3, 2, -2, 2, -2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +10; __Will__: +7"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ fire; __Weaknesses__ cold 5"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 (Magical, Unholy) __Damage__ 1d8+4 piercing plus 1d6 fire"
abilities_bot:
  - name: "Hellfire Breath"
    desc: "⬻ (Divine, Fire, Unholy) The hell hound breathes flames that deal 4d6 fire damage to all creatures in a 15-foot cone (DC 19 basic Reflex save). The hell hound can't use Hellfire Breath again for 1d4 rounds. If the hell hound would take fire damage or be targeted by a fire effect, their Hellfire Breath recharges."
  - name: "Pack Attack"
    desc: "The hell hound's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the hell hounds' allies."
sourcebook: "_Monster Core_, page 194."
```

```encounter-table
name: Hell Hound
creatures:
  - 1: Hell Hound
```
