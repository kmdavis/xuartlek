---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lyrakien"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Lyrakien"
level: 1
source: "Monster Core"
aon_id: "creature-2840"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2840"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lyrakien"
level: "Creature 1"
size: "Tiny"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Diabolic, Draconic, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Diplomacy +6, Performance +8, Religion +6, Stealth +7"
abilityMods: [-2, 4, 1, 1, 3, 3]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +7; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25; __Weaknesses__ cold iron 3, unholy 3"
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Finesse, Holy, Magical, reach 0 feet) __Damage__ 1d4–2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ starlight ray +7 (Holy, Light, range 30 feet) __Damage__ 2d4 spirit"
abilities_bot:
  - name: "Starlight Blast"
    desc: "⬺ (Holy, Light) The lyrakien unleashes a blast of holy starlight in a 5-foot emanation. Enemies in the area take 2d6 spirit damage with a DC 17 basic Reflex save. The lyrakien can't use Starlight Blast or their starlight ray ranged attack for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Daze, Detect Magic, Light - __1st__ Heal, Illusory Object - __4th__ Read Omens - __Constant (4th)__ Unfettered Movement"
sourcebook: "_Monster Core_, page 32."
```

```encounter-table
name: Lyrakien
creatures:
  - 1: Lyrakien
```
