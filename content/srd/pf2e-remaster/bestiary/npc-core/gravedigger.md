---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gravedigger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gravedigger"
level: 1
source: "NPC Core"
aon_id: "creature-3495"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3495"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gravedigger"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +7, Graveyard Lore +7, Religion +5, Stealth +4"
abilityMods: [4, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "bull's-eye lantern (2 oils), gravedigger's garb (functions as leather armor), religious symbol of Pharasma, shovel"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +4; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ void 2"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shovel +9 __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
abilities_bot:
  - name: "Light in the Dark"
    desc: "⬺ (Concentrate, Divine, Manipulate, Vitality)"
  - name: "Requirements"
    desc: "The gravedigger is holding a bull's-eye lantern in one hand and their religious symbol in the other, and the lantern contains oil"
  - name: "Effect"
    desc: "The gravedigger recites a brief chant to ignite their lantern with vital energy. Each undead creature in a 15-foot line takes 3d6 vitality damage with a DC 14 basic Fortitude save. This action uses all remaining oil in the bull's-eye lantern."
sourcebook: "_NPC Core_, page 69."
```

```encounter-table
name: Gravedigger
creatures:
  - 1: Gravedigger
```
