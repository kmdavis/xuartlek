---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tomb Jelly"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/large
statblock: inline
name: "Tomb Jelly"
level: 5
source: "Monster Core"
aon_id: "creature-3127"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3127"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tomb Jelly"
level: "Creature 5"
size: "Large"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; motion sense (precise) 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Athletics +13"
abilityMods: [6, -5, 6, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A tomb jelly can feel nearby motion through vibration and air movement."
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +15; __Ref__: +4; __Will__: +7"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ acid, bleed, critical hits, mental, precision, slashing, unconscious, visual, void"
speed: "15 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +15 __Damage__ 1d8+6 bludgeoning plus 1d6 acid and tomb curse"
abilities_bot:
  - name: "Bound in Death"
    desc: "⬻ (Healing, Void) The tomb jelly splatters some of its substance on a willing undead creature within its reach. The target regains 5 HP and its melee Strikes get the benefits of tomb curse until the end of its next turn."
  - name: "Flesh-dissolving Acid"
    desc: "A tomb jelly's acid damages only flesh."
  - name: "Tomb Curse"
    desc: "(Curse, Divine, Void) A creature hit by a tomb jelly's pseudopod takes 1d6 persistent void damage. If the creature dies while it has this persistent damage, its corpse is affected by _peaceful rest_, except the tomb jelly can still dissolve its flesh."
sourcebook: "_Monster Core_, page 257."
```

```encounter-table
name: Tomb Jelly
creatures:
  - 1: Tomb Jelly
```
