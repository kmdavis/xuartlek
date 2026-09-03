---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "False Priest"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "False Priest"
level: 4
source: "NPC Core"
aon_id: "creature-3537"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3537"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "False Priest"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +8, Deception +12, Performance +12, Religion +8, Society +6"
abilityMods: [0, 4, 3, 0, 2, 4]
abilities_top:
  - name: "Items"
    desc: "alchemical tools (used as “blessed items” to fool marks), Backpack, cloak, collection of fake relics, Hand Crossbow (20 bolts), Rapier, wooden religious symbol, Studded Leather Armor"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +12; __Will__: +10"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +12 (deadly d8, Disarm, Finesse) __Damage__ 1d6+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +12 (range increment 60 feet, reload 1) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Deceiver's Surprise"
    desc: "On the first round of combat, if the false priest rolls Deception or Performance for initiative, creatures that haven't acted yet are off-guard to them."
  - name: "Fickle Prophecy"
    desc: "⬻ (Emotion, Mental) The false priest convinces another creature of their omnipotence by attempting a Deception check compared to the creature's Will DC. If successful, the target gains 1d8+4 temporary Hit Points that last for 1 hour or until the false priest removes them by rebuking the target, whichever occurs first."
  - name: "The Jig Is Up"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Trigger"
    desc: "The false priest critically fails a Deception or Performance check"
  - name: "Effect"
    desc: "The false priest Strides."
  - name: "Sneak Attack"
    desc: "The false priest deals an additional 1d6 precision damage to off-guard creatures. This increases to 2d6 against creatures off-guard due to the false priest's Feint or deceiver's surprise."
sourcebook: "_NPC Core_, page 98."
```

```encounter-table
name: False Priest
creatures:
  - 1: False Priest
```
