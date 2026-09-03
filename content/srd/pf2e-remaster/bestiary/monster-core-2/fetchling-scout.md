---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fetchling Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fetchling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/medium
statblock: inline
name: "Fetchling Scout"
level: 1
source: "Monster Core 2"
aon_id: "creature-4400"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4400"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fetchling Scout"
level: "Creature 1"
size: "Medium"
trait_01: "Fetchling"
trait_02: "Humanoid"
trait_03: "Shadow"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Common, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +4, Deception +5, Diplomacy +5, Society +3, Stealth +7, Thievery +7"
abilityMods: [1, 4, 2, 0, 0, 2]
abilities_top:
  - name: "Items"
    desc: "Chain Shirt, Dagger"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Shadow Blending"
    desc: "When the fetchling scout is concealed as a result of dim light, the flat check to target them has a DC of 7, not 5."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, finesse, versatile S) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, finesse, thrown 10 feet, versatile S) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Shadow Stride"
    desc: "⬻ (Illusion, occult, shadow)"
  - name: "Requirements"
    desc: "The fetchling is in dim light"
  - name: "Effect"
    desc: "The fetchling Strides. They have a +10-foot status bonus to their Speed during this Stride. The DC from shadow blending increases to 11 during this Stride, and the fetchling remains concealed by dim light until the end of the movement, even if they leave dim light during the Stride."
  - name: "Sneak Attack"
    desc: "The fetchling scout's Strikes deal an additional 1d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 15 - __1st__ Illusory Disguise"
sourcebook: "_Monster Core 2_, page 156."
```

```encounter-table
name: Fetchling Scout
creatures:
  - 1: Fetchling Scout
```
