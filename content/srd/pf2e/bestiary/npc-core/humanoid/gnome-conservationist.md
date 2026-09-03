---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnome Conservationist"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Gnome Conservationist"
level: 6
source: "NPC Core"
aon_id: "creature-3639"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3639"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gnome Conservationist"
level: "Creature 6"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision"
languages: "Common, Gnomish"
skills:
  - name: "Skills"
    desc: "Athletics +13, Crafting +11, Nature +15, Survival +15"
abilityMods: [2, 1, 1, 2, 4, 2]
abilities_top:
  - name: "Animal Elocutionist"
    desc: "The conservationist can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Items"
    desc: "seeds (functions as sling bullets), _+1 sling_, trowel (functions as a sickle)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +11; __Will__: +14"
hp: 100
health:
  - name: "HP"
    desc: "100"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trowel +14 (Agile, Finesse, Trip) __Damage__ 1d4+8 slashing"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _sling_ +16 (Magical, Propulsive, range increment 60 feet, reload 1) __Damage__ 1d6+7 bludgeoning"
abilities_bot:
  - name: "Wild Leadership"
    desc: "⬻ (Auditory, Concentrate, Primal) With a primal incantation, the gnome conservationist inspires a willing animal. The animal becomes quickened for 1 round. It can use this additional action only to Climb, Burrow, Fly, Stride, or Strike."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +17 - __Cantrips (3rd)__ Detect Magic, Gouging Claw, Know the Way, Light, Tangle Vine - __1st__ Charm, Gentle Landing, Runic Body, Spider Sting - __2nd__ Animal Messenger, Darkvision, Entangling Flora, Oaken Resilience - __3rd__ Grease, Mad Monkeys, Safe Passage"
sourcebook: "_NPC Core_, page 184."
```

```encounter-table
name: Gnome Conservationist
creatures:
  - 1: Gnome Conservationist
```
