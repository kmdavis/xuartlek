---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mime"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mime"
level: 3
source: "NPC Core"
aon_id: "creature-3573"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3573"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mime"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Common; sign language"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +8, Deception +10, Performance +10, Stealth +10"
abilityMods: [1, 3, 0, 1, 2, 4]
abilities_top:
  - name: "Mimicry Specialist"
    desc: "For encounters involving mimicry or pantomime, the mime is a 6th-level challenge."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +9; __Will__: +12"
hp: 45
health:
  - name: "HP"
    desc: "45; __Resistances__ sonic 5"
abilities_mid:
  - name: "Skill Mimicry"
    desc: "The mime receives a +1 circumstance bonus to skill checks to perform actions they have witnessed another creature successfully perform in the last minute, or +2 if they witness a creature critically succeed instead."
  - name: "Versatile Performance"
    desc: "The mime can use Performance instead of Diplomacy to Make an Impression, instead of Intimidation to Demoralize, and instead of Deception to Impersonate."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
abilities_bot:
  - name: "Mimic Assault"
    desc: "⬺ (Attack, Mental, Visual)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "A creature damaged the mime with a weapon Strike since their previous turn"
  - name: "Effect"
    desc: "The mime makes a Performance check against the Perception DC of the creature who damaged them, gesturing as if making an attack with the same weapon. On a success, the mime deals two dice of damage to the creature, using the same type and die size as the required weapon Strike."
  - name: "Pantomime"
    desc: "⬺ (Illusion, Mental, Visual) The mime uses exaggerated movements to emulate one of the following effects, which lasts until the end of their next turn. Any creature who sees this ability can attempt to disbelieve this ability as it is used with a DC 14 Will save. Creatures that disbelieve are temporarily immune to pantomime for 1 minute. _Barrier_: The mime creates an invisible 10-foot-by-10-foot stretch of wall adjacent to them and within their reach. The wall has AC 10, 5 hardness, and 10 HP. If the mime Sustains this effect, they can add an additional wall in the same manner. _Rope_: The mime tugs an invisible rope, trying to knock over or pull at a creature within 15 feet. If the creature fails to disbelieve the pantomime, the mime can choose to either knock the creature prone or to move it 5 feet towards them. _Wind_: The mime creates a 30-foot line of imaginary wind. Creatures who don't disbelieve the pantomime treat this area as difficult terrain, and if they enter or begin their turn in the area, they fall prone."
sourcebook: "_NPC Core_, page 126."
```

```encounter-table
name: Mime
creatures:
  - 1: Mime
```
