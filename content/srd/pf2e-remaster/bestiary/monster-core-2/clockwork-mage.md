---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Mage"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Clockwork Mage"
level: 9
source: "Monster Core 2"
aon_id: "creature-4296"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4296"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Mage"
level: "Creature 9"
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +17"
abilityMods: [2, 6, 4, -5, 2, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 26, standby"
  - name: "Items"
    desc: "clockwork wand"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +19; __Will__: +17"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Resistances__ physical 5 (except adamantine or orichalcum); __Weaknesses__ electricity 10, orichalcum 10"
abilities_mid:
  - name: "Clockwork Wand"
    desc: "The clockwork mage uses a mechanical wand as a focus to channel magical energy. This wand is built into the clockwork mage's chest, with only the crystal at the end exposed. The mage can Interact to the remove the wand, or someone else can remove it with a DC 31 Thievery check to Disable a Device. The clockwork mage becomes unable to cast any spells except cantrips while the wand is removed. When removed, the clockwork wand is a magic wand containing the last 2nd-rank innate spell the clockwork mage cast (the GM determines the spell randomly if the mage has not cast any eligible spells). The spells are placed within the wand while the mage is created, and the creator can substitute other arcane spells of the appropriate rank."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, finesse) __Damage__ 2d10+6 bludgeoning"
abilities_bot:
  - name: "Energize Clockwork Wand"
    desc: "(Concentrate)"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The clockwork mage regains a spell it has already cast that day. It must spend 1 hour of its operational time, or 2 hours if the spell is 3rd rank or higher."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ Daze, Detect Magic, Frostbite, Shield, Tangle Vine - __1st__ Carryall, Gentle Landing, Grease - __2nd__ Mist, Revealing Light, Web (Player Core 2 255) - __3rd__ Aqueous Orb, Haste, Invisibility - __4th__ Flicker, Fly, Wall of Fire - __5th__ Howling Blizzard, Slither"
sourcebook: "_Monster Core 2_, page 72."
```

```encounter-table
name: Clockwork Mage
creatures:
  - 1: Clockwork Mage
```
