---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Root Leshy Groundskeeper"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Root Leshy Groundskeeper"
level: -1
source: "NPC Core"
aon_id: "creature-3656"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3656"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Root Leshy Groundskeeper"
level: "Creature -1"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision"
languages: "Common, Fey; _speak with plants_ (root vegetables only)"
skills:
  - name: "Skills"
    desc: "Athletics +5, Labor Lore +2, Nature +5, Stealth +4, Survival +5"
abilityMods: [3, 0, 3, -1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "shovel (functions as pick)"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +8; __Ref__: +2; __Will__: +5"
hp: 9
health:
  - name: "HP"
    desc: "9"
abilities_mid:
  - name: "Verdant Burst"
    desc: "(healing, primal, vitality) When the root leshy groundskeeper dies, a burst of primal energy explodes from their body, restoring 1d4 Hit Points to each plant creature in a 30-foot emanation. This area immediately fills with roots and vines, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shovel +5 (fatal d10) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The root leshy groundskeeper transforms into a Small root vegetable. This ability otherwise uses the effects of _one with plants_."
  - name: "Root in Place"
    desc: "⬻ (Manipulate, Primal) The root leshy groundskeeper roots themself into the ground, reducing their Speed to 0 and granting them a +1 circumstance bonus to AC and 2 temporary Hit Points until the start of their next turn."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13 - __Constant (3rd)__ Speak with Plants (root vegetables only)"
sourcebook: "_NPC Core_, page 200."
```

```encounter-table
name: Root Leshy Groundskeeper
creatures:
  - 1: Root Leshy Groundskeeper
```
