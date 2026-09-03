---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cavern Troll"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/large
statblock: inline
name: "Cavern Troll"
level: 6
source: "Monster Core 2"
aon_id: "creature-4592"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4592"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Cavern Troll"
level: "Creature 6"
size: "Large"
trait_01: "Earth"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Troll"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Jotun, Sakvroth"
skills:
  - name: "Skills"
    desc: "Athletics +16, Intimidation +14"
abilityMods: [6, 2, 6, -2, 2, -2]
abilities_top:
  - name: "Easily Misled"
    desc: "The cavern troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +16; __Ref__: +13; __Will__: +9"
hp: 135
health:
  - name: "HP"
    desc: "135 , regeneration 20 (deactivated by acid or sonic); __Immunities__ bleed; __Weaknesses__ acid 10, sonic 10"
abilities_mid:
  - name: "Sunlight Petrification"
    desc: "If exposed to direct sunlight, a cavern troll immediately becomes slowed 1 and can't use reactions. The slowed value increases by 1 each time the cavern troll ends its turn in sunlight. If the cavern troll's actions are reduced to 0 in this way, they become petrified until they spends at least 1 minute in darkness. Spells like _sunburst_ that create magical sunlight can't petrify a cavern troll, but the troll is slowed 1 for 1d4 rounds after being exposed to such an effect."
  - name: "Furious Throw"
    desc: "⬲"
  - name: "Trigger"
    desc: "The cavern troll takes acid or sonic damage"
  - name: "Effect"
    desc: "The troll uses Throw Rock targeting a random enemy within their first range increment. If the cavern troll has persistent acid damage, they attempt a DC 15 flat check to remove it."
speed: "25 feet, burrow 20 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 (reach 10 feet) __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, reach 10 feet) __Damage__ 2d6+8 slashing"
  - name: "Ranged"
    desc: "⬻ rock +16 (Brutal, range increment 120 feet) __Damage__ 1d12+8 bludgeoning"
abilities_bot:
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Rock Tunneler"
    desc: "A cavern troll can burrow through solid stone at a Speed of 10 feet. They can leave a tunnel if they desire."
  - name: "Throw Rock"
    desc: "⬻ Mixing Variations Cavern trolls and ice trolls spawn their own jotund trolls, two-headed trolls, and warleaders. In these cases, change their immunity, regeneration, and weaknesses to match their origin. You can also update their reaction's trigger and its persistent damage removal to match those weaknesses."
sourcebook: "_Monster Core 2_, page 328."
```

```encounter-table
name: Cavern Troll
creatures:
  - 1: Cavern Troll
```
