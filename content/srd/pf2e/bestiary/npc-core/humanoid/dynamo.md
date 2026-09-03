---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dynamo"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Dynamo"
level: 8
source: "NPC Core"
aon_id: "creature-3464"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3464"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dynamo"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +18, Crafting +17, Engineering Lore +17, Medicine +16, Thievery +17"
abilityMods: [6, 3, 2, 3, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Artisan's Toolkit (blacksmithing), _+1 dragon mouth pistol_ (10 rounds), Repair Toolkit, steel plating (functions as half plate)"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +17; __Will__: +14"
hp: 145
health:
  - name: "HP"
    desc: "145"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ modular prosthesis +20 __Damage__ 2d8+12 and see Modular Prostheses"
  - name: "Ranged"
    desc: "⬻ dragon mouth pistol +18 (Concussive, range increment 20 feet, reload 1, scatter 5 feet) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Extend Arms"
    desc: "⬻ The dynamo extends their collapsible steel arms, giving them both a reach of 20 feet with all melee attacks. However, the dynamo becomes enfeebled 1 and can't use the Interact action. The dynamo can Dismiss this ability."
  - name: "Extend Legs"
    desc: "⬻ The dynamo rises into the air on 10-foot-tall telescoping steel legs. While their legs are extended, the dynamo gains a +10-foot status bonus to land Speed and ignores any cover granted by barriers less than 10 feet tall. However, the dynamo becomes clumsy 1 and can't use the Climb, Leap, Swim, or Tumble Through actions. The dynamo can Dismiss this ability."
  - name: "Modular Prostheses"
    desc: "⬻ The dynamo configures one or both of their mechanical prosthetic hands into a specific configuration. Each configuration deals a specific damage type and has its own weapon traits: fist (bludgeoning; free-hand), gaff hook (piercing; grapple), impact driver (bludgeoning; shove), or spinning blade (slashing; trip). The dynamo can alternatively transform a hand into a steel shield with Hardness 8, HP 72, and BT 36. A broken prosthesis can't be reconfigured until repaired."
sourcebook: "_NPC Core_, page 48."
```

```encounter-table
name: Dynamo
creatures:
  - 1: Dynamo
```
