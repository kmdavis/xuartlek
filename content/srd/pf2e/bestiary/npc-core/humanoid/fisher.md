---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fisher"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Fisher"
level: 0
source: "NPC Core"
aon_id: "creature-3493"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3493"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Fisher"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; (8 to spot fish)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +7, Fishing Lore +8, Nature +4, Sailing Lore +6, Survival +4"
abilityMods: [3, 2, 1, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "assorted knives, fishing rod, Net, Rope (50 feet), Spear, tackle box"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +6; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spear +7 __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ fishing line +6 (range increment 20 feet) __Damage__ 1 piercing plus 1 persistent bleed and fishhooked"
  - name: "Ranged"
    desc: "⬻ spear +6 (thrown 20 feet) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Fishhooked"
    desc: "While it has persistent bleed damage from the fisher's fishing line Strike, a creature has a fishhook embedded in it. The creature can't move farther away from the fisher (though it can move laterally). The fisher can reel the creature in as a single action with the attack and manipulate trait, attempting an Athletics check against the creature's Fortitude DC. On a success, the creature takes 2d4 slashing damage and is pulled 10 feet closer to the fisher (double the damage and distance on a critical success)."
sourcebook: "_NPC Core_, page 68."
```

```encounter-table
name: Fisher
creatures:
  - 1: Fisher
```
