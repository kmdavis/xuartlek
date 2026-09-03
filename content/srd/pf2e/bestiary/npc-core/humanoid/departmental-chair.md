---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Departmental Chair"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Departmental Chair"
level: 7
source: "NPC Core"
aon_id: "creature-3594"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3594"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Departmental Chair"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common; up to 4 additional languages"
skills:
  - name: "Skills"
    desc: "Academia Lore +25, Arcana +22, Diplomacy +15, Occultism +22, Society +17, one additional Lore +22"
abilityMods: [0, 1, 0, 5, 5, 3]
abilities_top:
  - name: "Veteran Researcher"
    desc: "On the rare occasions the departmental chair still deals with their research, they are a 10th-level challenge."
  - name: "Items"
    desc: "spellbook, _+1 staff_, writing kit"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +14; __Will__: +18"
hp: 115
health:
  - name: "HP"
    desc: "115"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +13 (Magical, two-hand d8) __Damage__ 1d4+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Paper Pusher"
    desc: "⬻ (Arcane, Concentrate, Spellshape) The departmental chair has spent so much time dealing with bureaucracy recently that papers and forms have worked their way into the chair's spellcasting. If the departmental chair's next action is to Cast a Spell that deals energy damage, the spell conjures a burst of sharp-edged paper instead. Change the damage type to slashing, and the spell deals an additional 1d6 persistent bleed damage."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ Detect Magic, Ignition, Prestidigitation, Telekinetic Hand - __3rd__ Fireball (×2), Haste, Lightning Bolt - __4th__ Mountain Resilience, Wall of Fire"
sourcebook: "_NPC Core_, page 141."
```

```encounter-table
name: Departmental Chair
creatures:
  - 1: Departmental Chair
```
