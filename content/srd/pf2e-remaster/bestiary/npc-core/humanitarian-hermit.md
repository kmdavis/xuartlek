---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Humanitarian Hermit"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Humanitarian Hermit"
level: 9
source: "NPC Core"
aon_id: "creature-3486"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3486"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Humanitarian Hermit"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17"
languages: "Common, Fey, Wildsong"
skills:
  - name: "Skills"
    desc: "Athletics +19, Diplomacy +14, Medicine +21, Nature +19, Society +14, Survival +17"
abilityMods: [4, 1, 3, 1, 4, 1]
abilities_top:
  - name: "Items"
    desc: "Hide Armor, expanded healer's toolkit, Primal Symbol, _+1 striking staff of healing_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +16; __Will__: +19"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +20 (Parry, Reach, Trip, two-hand d8) __Damage__ 2d4+10 bludgeoning plus 2d8 vitality"
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
abilities_bot:
  - name: "Cleansing Earth"
    desc: "⬽ (Plant, Primal)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The humanitarian blesses the land and their allies. In a 30-foot emanation, plants grow and become difficult terrain. Additionally, all allies in the emanation gain 20 temporary Hit Points and can ignore the difficult terrain. These effects last for 1 minute."
  - name: "Primal Staff"
    desc: "A staff wielded by the humanitarian hermit gains the parry, reach, and trip traits, and Strikes with it deal an additional 2d8 vitality damage."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the humanitarian hermit's spellcasting action, the hermit attempts a DC 15 flat check. On a success, the action isn't disrupted. Reincarnation Transitions In cases of death from communal enacted injustice, _reincarnate_ can give the perished a renewed chance at life, free from the weight of their past and the trappings of their old society. The humanitarian hermit acts as a caretaker during this transition, helping the individual reach out to old friends for emotional healing and closure. If the hermit believes them to be a good candidate, they may help the reincarnated find a new life within their druidic order."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 27, attack +19 - __Cantrips (5th)__ Electric Arc, Light, Know the Way, Stabilize, Vitality Lash - __1st__ Cleanse Cuisine, Create Water, Vanishing Tracks - __2nd__ Create Food, Environmental Endurance, Peaceful Rest - __3rd__ Earthbind, Haste, Safe Passage - __4th__ Cleanse Affliction (×2), Mountain Resilience - __5th__ Heal (×4), Vital Beacon"
  - name: "Rituals"
    desc: "DC 27 - __3rd__ Reincarnate"
sourcebook: "_NPC Core_, page 63."
```

```encounter-table
name: Humanitarian Hermit
creatures:
  - 1: Humanitarian Hermit
```
