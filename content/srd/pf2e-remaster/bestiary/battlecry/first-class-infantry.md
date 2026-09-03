---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "First-Class Infantry"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "First-Class Infantry"
level: 13
source: "Battlecry!"
aon_id: "creature-3915"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3915"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "First-Class Infantry"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +27, Warfare Lore +24"
abilityMods: [8, 4, 5, 0, 2, 0]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +23; __Will__: +20"
hp: 240
health:
  - name: "HP"
    desc: "240 (4 segments); __Weaknesses__ area damage 12, splash damage 12"
abilities_mid:
  - name: "No Retreat"
    desc: "These soldiers have been extensively trained to hold their ground no matter the situation. If any effect would force the first-class infantry to move, reduce the distance by 10 feet. Any time they would be affected by the fleeing condition, the first-class infantry is instead slowed 2 for the same duration."
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Bolt Salvo"
    desc: "⬽ The first-class infantry draws, loads, and shoots a salvo from their crossbows. The salvo is a 10-foot burst within 120 feet that deals 4d8 piercing damage (DC 30 basic Reflex save). When the first-class infantry is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Clash of Steel"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The first-class infantry attacks each enemy in a 5-foot emanation, with a DC 29 basic Reflex save. The damage depends on the number of actions. ⬻ 2d6+1 slashing damage ⬺ 4d6+10 slashing damage ⬽ 4d6+18 slashing damage"
  - name: "Drilled in Formations"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The first-class infantry uses Change Formation. An first-class infantry unit typically knows the marching column and wedge formations."
  - name: "First-class Charge"
    desc: "⬺ The first-class infantry rushes forward with a hunger for battle. They Stride up to twice their Speed. At the end of their movement, each enemy within a 5-foot emanation takes 2d6+5 slashing damage, with a DC 30 basic Reflex save."
sourcebook: "_Battlecry!_, page 180."
```

```encounter-table
name: First-Class Infantry
creatures:
  - 1: First-Class Infantry
```
