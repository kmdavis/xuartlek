---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mountaineer"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mountaineer"
level: 5
source: "NPC Core"
aon_id: "creature-3473"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3473"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mountaineer"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Common, Petran, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +13, Mountain Lore +15, Nature +12, Survival +12"
abilityMods: [4, 3, 2, 0, 3, 0]
abilities_top:
  - name: "Experienced Steps"
    desc: "A mountaineer isn't impeded by difficult terrain caused by snow or ice. They gain a +2 circumstance bonus to Acrobatics checks to Balance on slippery ice."
  - name: "Professional Climber"
    desc: "While climbing, the mountaineer can have up to five allies Following the Expert and grants a +3 circumstance bonus to Athletics checks to Climb."
  - name: "Items"
    desc: "Chalk (10), extreme climbing kit, Compass, Hatchet (2), Hide Armor, Pick, Spyglass, Survey Map"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +12; __Will__: +9"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Lost My Footing"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The mountaineer critically fails a check to Balance or Climb"
  - name: "Effect"
    desc: "Training kicks in, and the mountaineer catches themself, improving the check from a critical failure to a failure."
  - name: "Tuck and Roll"
    desc: "During an avalanche, the mountaineer gains a +2 circumstance bonus to their Reflex save against bludgeoning damage and natural disasters."
speed: "25 feet; arctic passage"
attacks:
  - name: "Melee"
    desc: "⬻ pick +14 (fatal d10) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ hatchet +14 (Agile, Sweep) __Damage__ 1d6+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hatchet +13 (Agile, thrown 10 feet) __Damage__ 1d6+10 slashing"
abilities_bot:
  - name: "Arctic Passage"
    desc: "The mountaineer ignores difficult terrain caused by ice or snow."
  - name: "Team Awareness"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is undetected by one or more of the mountaineer's allies but is observed by the mountaineer"
  - name: "Effect"
    desc: "The mountaineer Points Out an enemy and makes a Strike against them."
  - name: "Chasm Crossing"
    desc: "⬺ The mountaineer Strides twice and Leaps up to 20 feet horizontally."
  - name: "Quick Draw"
    desc: "⬻ The mountaineer Interacts to draw their hatchet or pick, then Strikes with the weapon."
sourcebook: "_NPC Core_, page 55."
```

```encounter-table
name: Mountaineer
creatures:
  - 1: Mountaineer
```
