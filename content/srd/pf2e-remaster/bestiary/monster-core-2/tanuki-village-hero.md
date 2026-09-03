---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tanuki Village Hero"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tanuki
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Tanuki Village Hero"
level: 1
source: "Monster Core 2"
aon_id: "creature-4575"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4575"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tanuki Village Hero"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tanuki"
trait_03: "Uncommon"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
languages: "Common, Tanuki"
skills:
  - name: "Skills"
    desc: "Athletics +5, Diplomacy +6, Legal Lore +3, Stealth +6"
abilityMods: [2, 3, 2, 0, -1, 3]
abilities_top:
  - name: "Items"
    desc: "Dart (10), Kama, studded leather"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +8; __Will__: +2"
hp: 21
health:
  - name: "HP"
    desc: "21"
abilities_mid:
  - name: "Tactical Retreat"
    desc: "⬲ (emotion, fear, mental)"
  - name: "Trigger"
    desc: "The tanuki takes damage"
  - name: "Effect"
    desc: "The tanuki runs to a better tactical position. The tanuki gains the fleeing condition until the beginning of their next turn and Strides."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kama +7 (Agile, trip) __Damage__ 1d6+2 slashing"
  - name: "Ranged"
    desc: "⬻ dart +8 (Agile, range increment 20 feet, thrown) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, polymorph, primal) The tanuki takes on the form of a mundane raccoon dog. This makes them Tiny and gives them a +2 status bonus to their Stealth modifier, but they can't make Strikes."
  - name: "Tricky Throw"
    desc: "⬺ (Polymorph) The tanuki winds up and puts their everything into a throw. They make a dart Strike at one enemy within 40 feet. If the Strike is unsuccessful, the tanuki falls prone. If the Strike is successful, they really did put everything into the throw, having transformed into the dart the moment they threw it. The tanuki disappears from the space they threw from, appears in a space adjacent to the enemy and makes a kama Strike against said enemy, who's off-guard to the attack."
sourcebook: "_Monster Core 2_, page 315."
```

```encounter-table
name: Tanuki Village Hero
creatures:
  - 1: Tanuki Village Hero
```
