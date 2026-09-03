---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Centaur Herbalist"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/centaur
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Centaur Herbalist"
level: 3
source: "Monster Core"
aon_id: "creature-2874"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2874"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Centaur Herbalist"
level: "Creature 3"
size: "Large"
trait_01: "Beast"
trait_02: "Centaur"
trait_03: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common, Elven, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +11, Diplomacy +6, Medicine +7, Nature +7, Survival +7"
abilityMods: [3, 2, 1, 0, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Healer's Toolkit, herbal sachet, Sling (10 bullets)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +10"
hp: 36
health:
  - name: "HP"
    desc: "36"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hoof +9 (Agile) __Damage__ 1d10+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +8 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Load Sachet"
    desc: "⬻"
  - name: "Requirements"
    desc: "The centaur herbalist has at least one herbal sachet"
  - name: "Effect"
    desc: "The centaur herbalist Interacts to load an herbal sachet in her sling. The next ranged Strike she makes with her sling deals an additional 1d6 poison damage."
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 18 Centaur Craftwork Many centaurs appreciate fine weapons and armor. Some craft their own, maintaining designs traditional to their communities, while others use quality armaments they take from their enemies; however, due to their forms, centaurs who want to use armor heavier than breastplates need to have it tailor-made"
sourcebook: "_Monster Core_, page 58."
```

```encounter-table
name: Centaur Herbalist
creatures:
  - 1: Centaur Herbalist
```
