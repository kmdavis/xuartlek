---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Line Infantry"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Line Infantry"
level: 6
source: "NPC Core"
aon_id: "creature-3526"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3526"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Line Infantry"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +15, Warfare Lore +12"
abilityMods: [5, 2, 3, 0, 1, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +14; __Will__: +13"
hp: 96
health:
  - name: "HP"
    desc: "96 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "No Retreat"
    desc: "These soldiers have been extensively trained to hold their ground no matter the situation. If any effect would force the line infantry to move, reduce the distance by 5 feet. Any time they would be affected by the fleeing condition, the line infantry is instead slowed 2 for the same duration."
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Bolt Salvo"
    desc: "⬽ The line infantry draws, loads, and shoots a salvo from their crossbows. The salvo is a 10-foot burst within 120 feet that deals 2d8 piercing damage (DC 21 basic Reflex save). When the line infantry is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Clash of Steel"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The line infantry lays into each enemy in a 5-foot emanation, with a DC 21 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+2 slashing damage ⬺ 2d6+7 slashing damage ⬽ 3d6+10 slashing damage"
  - name: "Drilled in Formations"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The line infantry uses Change Formation (see below in Military). A line infantry unit typically knows the marching column and wedge formations."
sourcebook: "_NPC Core_, page 90."
```

```encounter-table
name: Line Infantry
creatures:
  - 1: Line Infantry
```
