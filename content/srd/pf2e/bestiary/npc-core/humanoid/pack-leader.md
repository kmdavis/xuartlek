---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pack Leader"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Pack Leader"
level: 4
source: "NPC Core"
aon_id: "creature-3581"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3581"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Pack Leader"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common, Wildsong"
skills:
  - name: "Skills"
    desc: "Athletics +6, Diplomacy +9, Nature +12, Stealth +9, Survival +10"
abilityMods: [0, 3, 1, 0, 4, 3]
abilities_top:
  - name: "Animal Empathy"
    desc: "The pack leader can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Items"
    desc: "Leather Armor, Sickle, Sling (10 bullets)"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +9; __Ref__: +9; __Will__: +12"
hp: 55
health:
  - name: "HP"
    desc: "55 __Stay Strong!__ ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "An allied animal within 30 feet attempts a saving throw"
  - name: "Effect"
    desc: "The pack leader shouts a word of encouragement, granting the allied animal a +1 circumstance bonus to the save."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sickle +11 (Agile, Finesse, Trip) __Damage__ 1d4+4 slashing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +11 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Timely Trick"
    desc: "⬻ (Auditory, Concentrate, Mental) The pack leader commands an animal ally within 30 feet to perform a specific action; the target can spend its reaction to immediately Step, Stride, or Strike. Pack Leader Companions In addition to the trained bat companion (and, optionally, with one of the support benefits), these _Monster Core_ animals make good companions for the pack leader."
  - name: "Level 3"
    desc: "dire wolf, giant mantis, giant scorpion, giant wasp, gorilla, grizzly bear, hyaenodon, lion, pachycephalosaurus"
  - name: "Level 4"
    desc: "daeodon, giant stag beetle, great white shark, griffon, hadrosaurid, rhinoceros, tiger."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ Gouging Claw, Guidance, Ignition, Stabilize, Tangle Vine - __1st__ Gentle Landing, Heal, Pet Cache - __2nd__ Animal Messenger, Enlarge, Summon Animal"
  - name: "Druid Order Focus Spells"
    desc: "DC 20, 1 Focus Point - __2nd__ Heal Animal"
sourcebook: "_NPC Core_, page 132."
```

```encounter-table
name: Pack Leader
creatures:
  - 1: Pack Leader
```
