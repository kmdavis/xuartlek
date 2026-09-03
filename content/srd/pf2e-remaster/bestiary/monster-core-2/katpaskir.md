---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Katpaskir"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Katpaskir"
level: 18
source: "Monster Core 2"
aon_id: "creature-4322"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4322"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Katpaskir"
level: "Creature 18"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 31
perception:
  - name: "Perception"
    desc: "Perception +31; darkvision, _see the unseen_, warp sense"
languages: "Aklo, Chthonian, Common, Draconic, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +31, Arcana +35, Deception +31, Occultism +33, Religion +32, Stealth +31, Thievery +31"
abilityMods: [6, 5, 9, 7, 6, 5]
abilities_top:
  - name: "Warp Sense"
    desc: "The katpaskir senses changes in the planar fabric within 1 mile, including any teleportation effects, sensing the direction and distance to the disturbance. If it senses such a disturbance within 500 feet, the katpaskir can cast _scouting eye_ to observe the area without needing line of sight to the location."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +35; __Ref__: +29; __Will__: +30 +1 status to all saves vs. magic"
hp: 415
health:
  - name: "HP"
    desc: "415; __Immunities__ poison; __Weaknesses__ cold iron 15, holy 15"
abilities_mid:
  - name: "Distortion Field"
    desc: "(aura) 30 feet. Reality bends and warps all senses without displacing the katpaskir's actual location. Creatures of the katpaskir's choice who start their turn in the aura must succeed at a DC 37 Will save or treat the area as greater difficult terrain and uneven ground (DC 20). A creature that succeeds still treats the area as difficult terrain. For chosen creatures, the distance through the aura is doubled for determining range penalty."
  - name: "Breach Planar Wards"
    desc: "⭓"
  - name: "Trigger"
    desc: "An effect attempts to prevent the katpaskir from using a teleportation effect or from casting _summon fiend_"
  - name: "Effect"
    desc: "The katpaskir attempts to counteract the triggering effect (counteract modifier of +29). The katpaskir automatically fails against an artifact's effect."
  - name: "Mirrored Summons"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 30 feet that the katpaskir is aware of casts _summon celestial_ or otherwise summons a holy creature"
  - name: "Effect"
    desc: "The katpaskir casts _summon fiend_, regaining the daily ability to do so if needed. This effect is automatically sustained as long as the triggering summoning is sustained, for up to 1 minute."
speed: "35 feet, burrow 15 feet, fly 35 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ claw +34 (Magical, unholy) __Damage__ 3d12+14 slashing plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ talon +34 (Agile, magical, unholy) __Damage__ 3d8+14 slashing plus 1d6 spirit"
abilities_bot:
  - name: "Dimensional Ambush"
    desc: "⬺ (Divine, teleportation) The katpaskir casts _translocate_, then makes a melee Strike that deals three extra dice of damage. This Strike counts as two attacks when calculating the katpaskir's multiple attack penalty. Rift Makers Katpaskirs sense weaknesses in planar fabric. These demons worm their way into spaces between dimensions and break down the barriers. They leave holes aimed at causing chaos and dissolution. In this way, katpaskirs gnaw at reality, hoping to one day unravel it."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32 - __4th__ Planar Tether (at will) - __5th__ Scouting Eye (at will), Translocate (at will) - __7th__ Interplanar Teleport, Teleport - __8th__ Banishment (×3), Disintegrate, Flicker - __9th__ Summon Fiend (demons only) - __Constant (9th)__ See the Unseen, Unfettered Movement"
  - name: "Rituals"
    desc: "DC 40 - __1st__ Demonic Pact"
sourcebook: "_Monster Core 2_, page 94."
```

```encounter-table
name: Katpaskir
creatures:
  - 1: Katpaskir
```
