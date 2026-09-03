---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Carved Beast"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Carved Beast"
level: 6
source: "Rage of Elements"
aon_id: "creature-2675"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2675"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Carved Beast"
level: "Creature 6"
size: "Medium"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
skills:
  - name: "Skills"
    desc: "Nature +15, Stealth +16, Athletics +15"
abilityMods: [2, 4, 3, 0, 1, 2]
abilities_top:
  - name: "Top-Heavy"
    desc: "While the carved beast is not Dug In (see below), its unwieldy design leaves it vulnerable to falling over. The DC of any attempt to knock the carved beast prone is reduced by 5, and the beast takes a –5 status penalty to any check or save it attempts to resist being knocked prone. Additionally, whenever the beast fails to Trip opponents with its roots Strike, it critically fails instead. If successfully Shoved by an opponent, the beast must succeed at a DC 20 Reflex save or fall prone."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +13 (+15 while Dug In); __Ref__: +9; __Will__: +17"
hp: 92
health:
  - name: "HP"
    desc: "92; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ axes 5, fire 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ statue +15 (Shove) __Damage__ 2d8+5 (3d8+5 while Dug In) bludgeoning plus Knockdown"
  - name: "Melee"
    desc: "⬻ roots +17 (Finesse, Trip) __Damage__ 2d8+5 bludgeoning"
abilities_bot:
  - name: "Dig In"
    desc: "⬻ The carved beast digs its roots into the ground for better protection and purchase. While Dug In, the carved beast can't Stride nor use its roots Strike; however, this also negates the effects of top-heavy, grants the beast a +2 status bonus to its AC and Fortitude saves, and increases the damage of its statue Strike by 1d8. The carved beast can spend an action on its turn to end the effect; alternatively, the effect ends when the carved beast is moved by force, such as via a successful Shove attack. Carved Treasures If an adventurer is careful while defeating a carved beast, the statue may be recovered intact from its defeated body and sold as a lesser art object. With a level-appropriate skill check, a character trained in Crafting can potentially increase the statue's quality to moderate or repurpose it into something else entirely, such as whittling a small bird shape into a decorative whistle."
sourcebook: "_Rage of Elements_, page 208."
```

```encounter-table
name: Carved Beast
creatures:
  - 1: Carved Beast
```
