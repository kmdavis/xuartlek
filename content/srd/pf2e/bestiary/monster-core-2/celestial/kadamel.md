---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kadamel"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Kadamel"
level: 17
source: "Monster Core 2"
aon_id: "creature-4082"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4082"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kadamel"
level: "Creature 17"
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; darkvision, _truesight_"
languages: "Diabolic, Draconic, Empyrean, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +32, Diplomacy +30, Intimidation +32, Religion +34"
abilityMods: [9, 5, 7, 4, 9, 7]
abilities_top:
  - name: "Stone Shield"
    desc: "The kadamel can create a stone shield for defense, which grants a +2 circumstance bonus to AC and has Hardness 15, HP 120, and BT 60."
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +29; __Ref__: +26; __Will__: +32 +1 status to all saves vs. magic"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ fear; __Weaknesses__ unholy 15"
abilities_mid:
  - name: "Patience of Stone"
    desc: "(aura, divine) 10 feet. Any enemy that ends its turn in the aura must succeed at a DC 36 Fortitude save or be slowed 1 for 1 minute. If the creature succeeds, it's temporarily immune for 24 hours."
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 20 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone axe +32 (Holy, Magical, Sweep) __Damage__ 3d10+15 slashing plus 2d12 electricity"
  - name: "Ranged"
    desc: "⬻ stone axe +32 (Brutal, Holy, Magical, thrown 20 feet) __Damage__ 3d10+15 slashing plus 2d12 electricity"
abilities_bot:
  - name: "Spells"
    desc: "DC 38, attack +30 - __Cantrips (9th)__ Light - __4th__ Translocate (at will) - __7th__ Blessed Boundary, Interplanar Teleport, Planar Tether - __8th__ Planar Seal - __Constant (8th)__ Truesight, Truespeech, Veil of Privacy"
  - name: "Calcifying Cloud"
    desc: "⬻ (Divine, Incapacitation)"
  - name: "Requirements"
    desc: "The kadamel hit with a stone axe Strike during its most recent action"
  - name: "Effect"
    desc: "The kadamel's axe explodes into calcifying powder. The creature the axe hit and each non-archon creature in a 5-foot emanation must succeed at a DC 38 Fortitude save or become slowed 1 for 1 minute. If the creature was already slowed by one of the kadamel's abilities, a failed save causes it to be petrified permanently."
  - name: "Guardian Glyph"
    desc: "⬻ (Concentrate)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The kadamel alters the inscriptions on their body to store an 8th-rank spell, choosing from _divine decree_, _divine immolation_, _divine wrath_, or _planar seal_. While storing the spell, the kadamel chooses an area they're guarding, typically a room containing a planar portal. When an intruder enters the area, the spell is cast automatically and expended. If the spell is targeted, it targets the triggering creature, and if it has an area, the area is centered on the triggering creature. Noticing the glyph requires a successful DC 38 Perception check. The glyph has an unlimited duration and ends if the kadamel uses this ability again or Dismisses the glyph."
  - name: "Re-Arm"
    desc: "⭓ (Divine) The kadamel forms a new stone axe or stone shield in a free hand."
  - name: "Statue"
    desc: "⬻ (Concentrate) Until the next time they act, the kadamel appears to be a statue. They have an automatic result of 50 on Deception checks and DCs to pass as a statue. While remaining motionless in this way, the kadamel has fast healing 20."
sourcebook: "_Monster Core 2_, page 39."
```

```encounter-table
name: Kadamel
creatures:
  - 1: Kadamel
```
