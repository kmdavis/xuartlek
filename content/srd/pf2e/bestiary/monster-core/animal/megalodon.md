---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Megalodon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Megalodon"
level: 9
source: "Monster Core"
aon_id: "creature-3189"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3189"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Megalodon"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; blood scent, scent (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +21, Stealth +19, Survival +16"
abilityMods: [8, 2, 5, -4, 3, -2]
abilities_top:
  - name: "Blood Scent"
    desc: "The shark can smell blood in the water from up to 1 mile away"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +16; __Will__: +17"
hp: 180
health:
  - name: "HP"
    desc: "180"
speed: "swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 (reach 10 feet) __Damage__ 2d12+10 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +22 (Agile, reach 15 feet) __Damage__ 2d8+10 piercing plus Push 15 feet"
abilities_bot:
  - name: "Breach"
    desc: "⬺ The shark Swims up to its swim Speed, then Leaps vertically out of the water up to 25 feet high, making a Strike against a creature at any point during the jump (this lets it attack a creature within 35 feet of the water's surface, or 40 feet with its tail). After the Strike, the shark splashes back down into the water."
  - name: "Savage"
    desc: "⬻"
  - name: "Requirements"
    desc: "The shark hit with a jaws Strike on its most recent action this turn"
  - name: "Effect"
    desc: "The creature the shark hit takes 2d12 slashing damage."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Huge, 2d8+5 bludgeoning, Rupture 20"
sourcebook: "_Monster Core_, page 307."
```

```encounter-table
name: Megalodon
creatures:
  - 1: Megalodon
```
