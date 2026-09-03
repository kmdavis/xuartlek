---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Esipil"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Esipil"
level: 1
source: "Monster Core 2"
aon_id: "creature-4533"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4533"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Esipil"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +6, Intimidation +7, Stealth +7"
abilityMods: [0, 4, 2, 1, 2, 2]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the _binding circle_ ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +5"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ fear; __Weaknesses__ holy 2"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 (Finesse, magical, unholy, versatile P) __Damage__ 1d8 slashing plus 1d4 spirit and Grab"
  - name: "Melee"
    desc: "⬻ claw +9 (Agile, finesse, magical, unholy) __Damage__ 1d6 slashing plus 1d4 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, divine, polymorph) The esipil transforms into a Tiny cat, dog, or other unassuming domestic animal. This doesn't affect the esipil's statistics, but it could change the damage type of its Strikes."
  - name: "Skip Between"
    desc: "⬻ (Divine, teleportation) The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 15 - __Cantrips (1st)__ Telekinetic Hand - __1st__ Fear (at will) - __2nd__ Blur - __3rd__ Fear"
sourcebook: "_Monster Core 2_, page 274."
```

```encounter-table
name: Esipil
creatures:
  - 1: Esipil
```
