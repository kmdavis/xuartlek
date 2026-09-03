---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Asp Of Grief"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/small
statblock: inline
name: "Asp Of Grief"
level: 10
source: "Rage of Elements"
aon_id: "creature-2640"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2640"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Asp Of Grief"
level: "Creature 10"
size: "Small"
trait_01: "Beast"
trait_02: "Elemental"
trait_03: "Metal"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; low-light vision, magnetic vision"
languages: "Common, Empyrean, Talican"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Arcana +21, Psychology Lore +19, Nature +19, Survival +21"
abilityMods: [4, 7, 3, 7, 5, 3]
abilities_top:
  - name: "Magnetic Vision"
    desc: "An asp of grief can see magnetic fields, allowing it to detect large sources of magnetic metal (Bulk 1 or greater) as a precise sense."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +15; __Ref__: +21; __Will__: +21 +1 status vs. emotion"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ physical 10 (except adamantine)"
abilities_mid:
  - name: "Curtain of Calm"
    desc: "(arcane, aura, emotion, mental) 20 feet. The asp of grief consumes the emotions of the creatures around it. An enemy that begins its turn in the aura must attempt a DC 29 Will save. If it fails, the asp consumes its grief. The creature feels a lack of feelings and motivation, reducing its frightened value by 1 and becoming stupefied 1 (or stupefied 2 on a critical failure) for 1d4 rounds. Regardless of the result of the saving throw, the creature is temporarily immune to curtain of calm for 1 minute. The asp becomes charged with grief (see iron grief) for 1 minute whenever a creature fails this saving throw."
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 (Agile, Finesse) __Damage__ 2d12+10 piercing"
abilities_bot:
  - name: "Iron Grief"
    desc: "If the asp casts _magnetic acceleration_ while charged with grief, it can either heighten the spell to 5th rank or target up to three creatures instead of one, rolling separately against each. After casting the spell, the asp is no longer charged with grief."
  - name: "Magnetic Traveler"
    desc: "An asp can ride magnetic fields to travel long distances. In a location with strong magnetic fields (including the Plane of Metal and Golarion), its travel Speed is doubled if it's flying. Calling the Asps In the Plane of Metal, funeral rites often include placing the deceased upon tall towers surrounded by dishes of water. Chunks of sodium, a silvery-white alkali metal, dance across the surface of the water and catch fire, sending plumes of hydrogen gas into the air. As the asps of grief skate upon the magnetic fields, they can sense this announcement of death and sorrow and follow the trail back to the mourners."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ Detect Magic, Read Aura - __3rd__ Magnetic Acceleration (at will; see iron grief) - __5th__ Magnetic Attraction, Magnetic Repulsion"
sourcebook: "_Rage of Elements_, page 150."
```

```encounter-table
name: Asp Of Grief
creatures:
  - 1: Asp Of Grief
```
