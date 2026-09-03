---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Palace Guard"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Palace Guard"
level: 4
source: "NPC Core"
aon_id: "creature-3419"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3419"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Palace Guard"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; (14 when rolling initiative)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +14, Diplomacy +8, Intimidation +8"
abilityMods: [4, 2, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "chain mail with palace insignia, Halberd, simple manacles"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +10; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60 **Guard's Parry ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "A creature attacks the palace guard's liege, and the liege is within the guard's melee reach"
  - name: "Effect"
    desc: "The liege gains a +2 circumstance bonus to AC against the triggering attack, and the palace guard gains a +2 circumstance bonus to attack and damage rolls until the end of their next turn. **Reactive Strike ⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ halberd +14 (reach 10 feet, versatile S) __Damage__ 1d10+7 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
abilities_bot:
  - name: "Crowd Control"
    desc: "⬻"
  - name: "Requirements"
    desc: "The palace guard's last action was a successful halberd Strike"
  - name: "Effect"
    desc: "The palace guard attempts to Reposition the creature they hit using their halberd's reach. This attempt neither applies nor counts toward the guard's multiple attack penalty"
sourcebook: "_NPC Core_, page 14."
```

```encounter-table
name: Palace Guard
creatures:
  - 1: Palace Guard
```
