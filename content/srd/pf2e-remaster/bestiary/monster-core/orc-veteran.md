---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Veteran"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Veteran"
level: 1
source: "Monster Core"
aon_id: "creature-3130"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3130"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Orc Veteran"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Athletics +7, Intimidation +4, Survival +4"
abilityMods: [4, 2, 3, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Javelin (4), Orc Necksplitter, Shortsword (2)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +7; __Will__: +4"
hp: 23
health:
  - name: "HP"
    desc: "23"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ orc necksplitter +7 (Forceful, Sweep) __Damage__ 1d8+4 slashing"
  - name: "Melee"
    desc: "⬻ shortsword +7 (Agile, versatile P) __Damage__ 1d6+4 slashing"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Nonlethal) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +5 (thrown 30 feet) __Damage__ 1d6+4 piercing"
sourcebook: "_Monster Core_, page 258."
```

```encounter-table
name: Orc Veteran
creatures:
  - 1: Orc Veteran
```
