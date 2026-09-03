---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Equestrian Constable"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Equestrian Constable"
level: 4
source: "NPC Core"
aon_id: "creature-3557"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3557"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Equestrian Constable"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +12, Nature +10, Settlement Lore +8"
abilityMods: [4, 1, 3, 0, 2, 1]
abilities_top:
  - name: "Trained Animal"
    desc: "The equestrian constable rides a trained mount of their level or lower, usually a war horse or, for elite equestrian constables, a veteran war horse. The animal has the standard number of actions, uses its normal stat block, and counts toward the encounter's XP budget normally."
  - name: "Items"
    desc: "Crossbow (20 bolts), Guisarme, Half Plate, poor manacles, Rope, Signal Whistle"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +8; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Opportune Maneuver"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet uses an action with the move trait or leaves a space within the constable's reach during its move action"
  - name: "Effect"
    desc: "The constable attempts to Trip the triggering creature. On a success, the triggering action is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ guisarme +14 (reach 10 feet, Trip) __Damage__ 1d8+8 slashing plus Knockdown"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +11 (range increment 120 feet, reload 1) __Damage__ 1d8+4 piercing"
abilities_bot:
  - name: "Vigilant Vantage"
    desc: "⬻ The equestrian constable Seeks or Points Out a target. They can Interact to draw an item or Command an Animal to approach or attack the target."
sourcebook: "_NPC Core_, page 113."
```

```encounter-table
name: Equestrian Constable
creatures:
  - 1: Equestrian Constable
```
