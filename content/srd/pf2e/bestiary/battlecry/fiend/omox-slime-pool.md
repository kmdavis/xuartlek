---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Omox Slime Pool"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Omox Slime Pool"
level: 17
source: "Battlecry!"
aon_id: "creature-3930"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3930"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Omox Slime Pool"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Ooze"
trait_04: "Troop"
trait_05: "Unholy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision"
languages: "Chthonian, Draconic, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +33, Religion +28, Stealth +36"
abilityMods: [9, 6, 9, 2, 4, 4]
abilities_top:
  - name: "Clean Vulnerability"
    desc: "Omoxes embody filth, and they find the concept of cleanliness abhorrent. An omox slime pool subjected to an effect that cleans them takes 4d6 mental damage. They also take this damage the first time each round a creature damaged by an omox slime pool spends actions cleaning off the resultant filth."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +29; __Will__: +26 +1 status to all saves vs. magic"
hp: 315
health:
  - name: "HP"
    desc: "315 (4 segments); __Immunities__ acid, critical hits, disease, poison, precision; __Weaknesses__ area damage 15, cold iron 15, holy 15, splash damage 15"
abilities_mid:
  - name: "Absorb Weapon"
    desc: "⬲ (concentrate)"
  - name: "Trigger"
    desc: "A creature hits the omox slime pool with a melee weapon"
  - name: "Effect"
    desc: "The omoxes attempt to Disarm the creature. On a critical success, the weapon becomes subsumed within the body of an omox rather than falling to the ground. Retrieving the weapon requires a successful DC 45 Athletics check to Disarm."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet, climb 20 feet, swim 80 feet; troop movement"
abilities_bot:
  - name: "Slime Barrage"
    desc: "⬺ The omoxes hurl balls of heavy slime in a 10- foot burst within 30 feet. All creatures in the area take 4d6 bludgeoning damage and 2d6 acid damage (DC 35 basic Reflex save). A creature that fails the save is mired in the slime, taking a –10-foot circumstance penalty to its Speeds for 1 minute or until it Escapes (DC 38); on a critical failure, the creature is also clumsy 1 for the same duration. When the slime pool is reduced to 2 segments, the area decreases to a 5-foot burst."
  - name: "Smothering Grasp"
    desc: "⬻"
  - name: "Requirements"
    desc: "The omox slime pool has a creature grabbed or restrained"
  - name: "Effect"
    desc: "Omox slime flows onto the creature, completely covering it. The creature must then succeed at a DC 38 Fortitude save or it becomes blinded and must hold its breath or begin suffocating. These effects last as long as the omoxes have the creature grabbed or restrained."
  - name: "Waves of Sludge"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The omoxes attack all enemies in a 5-foot emanation with slimy tendrils (DC 35 basic Reflex save). A creature that critically fails this saving throw is also grabbed by the slime pool. The damage depends on the number of actions. ⬻ 1d6+3 bludgeoning damage plus 1d6 acid damage ⬺ 3d6+12 bludgeoning damage plus 2d6 acid damage ⬽ 4d6+14 bludgeoning damage plus 3d6 acid damage"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __5th__ Control Water, Create Water (at will), Translocate (at will) - __8th__ Toxic Cloud"
  - name: "Rituals"
    desc: "DC 38 - __1st__ Demonic Pact"
sourcebook: "_Battlecry!_, page 186."
```

```encounter-table
name: Omox Slime Pool
creatures:
  - 1: Omox Slime Pool
```
