---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Owb"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Owb"
level: 6
source: "Monster Core 2"
aon_id: "creature-4503"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4503"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Owb"
level: "Creature 6"
size: "Medium"
trait_01: "Shadow"
trait_02: "Uncommon"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; greater darkvision"
languages: "Caligni; (can't speak any languages), telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Deception +13, Diplomacy +11, Occultism +12, Religion +11, Stealth +15"
abilityMods: [4, 5, 4, 0, 3, 3]
abilities_top:
  - name: "Light Blindness"
    desc: ""
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +15; __Will__: +13"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ cold"
speed: "5 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, magical) __Damage__ 1d8+7 slashing plus 1d8 cold"
  - name: "Ranged"
    desc: "⬻ burning cold +17 (Magical, range 120 feet) __Damage__ 2d8 cold plus 1d8 persistent cold"
abilities_bot:
  - name: "Curse of Darkness"
    desc: "⬻ (Curse, darkness, occult) The owb inflicts a curse on one creature taking persistent cold damage from their burning cold Strike, stealing the victim's vibrancy. The creature must attempt a DC 23 Fortitude save. On a failure, the creature gains light blindness, and its coloration turns to washed out shades of gray, along with all equipment it carries, wields, or wears. These effects have an unlimited duration. Regardless of the result of its save, the creature is temporarily immune for 1 minute. If the owb uses this ability on a caligni, the curse can't be removed short of a _wish_ ritual or similar powerful magic. Shadows Among Shadows Little is known about owbs' lives on the Netherworld. They keep to themselves so much that most other shadowy denizens either remain unaware of their presence or disbelieve they even exist. Some rumors suggest that these creatures lack any real power on the Netherworld and thus spend most of their time manipulating their strange caligni “children” in the Universe."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +15 - __Cantrips (3rd)__ Daze, Read Aura, Shield, Void Warp - __3rd__ Mind Reading (at will) - __4th__ Darkness (at will), Invisibility - __5th__ Shadow Blast, Umbral Journey - __7th__ Interplanar Teleport (self only;to or from the Netherworld only)"
sourcebook: "_Monster Core 2_, page 246."
```

```encounter-table
name: Owb
creatures:
  - 1: Owb
```
