---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kholo Bonekeeper"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Kholo Bonekeeper"
level: 3
source: "Monster Core"
aon_id: "creature-3070"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3070"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kholo Bonekeeper"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
languages: "Chthonian, Common, Kholo"
skills:
  - name: "Skills"
    desc: "Intimidation +7, Medicine +7, Religion +10, Stealth +7, Survival +8"
abilityMods: [2, 2, 0, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Falchion, Hide Armor, wooden religious symbol"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +8; __Ref__: +6; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ falchion +10 (Forceful, Sweep) __Damage__ 1d10+3 slashing"
  - name: "Melee"
    desc: "⬻ jaws +10 (Agile) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Pack Attack"
    desc: "A kholo bonekeeper deals 1d4 extra damage to any creature that's within reach of at least two of the kholo bonekeeper's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ Daze, Detect Magic, Light, Read Aura, Sigil - __1st__ Command, Fear, Runic Weapon - __2nd__ Darkness, Harm (×4), Spiritual Armament"
sourcebook: "_Monster Core_, page 209."
```

```encounter-table
name: Kholo Bonekeeper
creatures:
  - 1: Kholo Bonekeeper
```
