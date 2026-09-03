---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Water Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/small
statblock: inline
name: "Water Scamp"
level: 1
source: "Monster Core"
aon_id: "creature-2988"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2988"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Water Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Water"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +6, Stealth +6"
abilityMods: [1, 3, 1, -2, 0, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +11; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20 (fast healing 2 (while underwater)); __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ acid 3, fire 3"
speed: "20 feet, fly 25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +8 (Agile, Finesse) __Damage__ 1d6+1 slashing"
abilities_bot:
  - name: "Acid Breath"
    desc: "⬺ (Acid, Arcane) The water scamp breathes acid in a 15-foot cone that deals 2d6 acid damage to each creature within the area (DC 17 basic Reflex save). The water scamp can't use Acid Breath again for 1d4 rounds."
  - name: "Drench"
    desc: "⬻ (Arcane, Water) The water scamp shakes out a seemingly endless supply of water from its fur to put out all fires in a 5-foot emanation. The scamp extinguishes all non-magical fires automatically and attempts to counteract magical fires (+7 counteract modifier)."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9 - __1st__ Create Water - __2nd__ Acid Grip"
sourcebook: "_Monster Core_, page 147."
```

```encounter-table
name: Water Scamp
creatures:
  - 1: Water Scamp
```
