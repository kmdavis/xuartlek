---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Okenevem"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Okenevem"
level: 15
source: "Monster Core 2"
aon_id: "creature-4081"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4081"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Okenevem"
level: "Creature 15"
size: "Large"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision"
languages: "Diabolic, Draconic, Empyrean, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Diplomacy +28, Heaven Lore +33, Medicine +28, Nature +28, Religion +31, Society +27"
abilityMods: [4, 6, 5, 6, 8, 7]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +25; __Ref__: +26; __Will__: +31 +1 status to all saves vs. magic"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ fear; __Weaknesses__ unholy 10"
abilities_mid:
  - name: "Divine Defenders"
    desc: "(aura, divine, holy, spirit) 60 feet. Okenevem hold an exalted place among archons for their holy station. This draws lesser archons to defend them. When an enemy in the aura takes a hostile action against the okenevem, a cloud of minor archons swarms around it, causing it to take 2d6 persistent slashing damage and 2d6 persistent spirit damage. This persistent damage ends automatically if the enemy spends a round without taking a hostile action against the okenevem."
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ humbling touch +29 (Divine, Finesse, Holy, Mental, Nonlethal, Spirit) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
  - name: "Ranged"
    desc: "⬻ humbling word +27 (Auditory, Divine, Holy, Mental, Nonlethal, range increment 60 feet, Spirit) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
abilities_bot:
  - name: "Spells"
    desc: "DC 36, attack +28 - __Cantrips (8th)__ Divine Lance, Light, Message - __4th__ Translocate (at will) - __7th__ Spiritual Guardian (×3) - __8th__ Calm - __Constant (5th)__ Truespeech"
  - name: "Humble Bow"
    desc: "(Divine, Holy, Mental) A creature hit by one of the okenevem's Strikes is compelled to bow down in reverence. It must succeed at a DC 36 Will save or fall prone. If the creature Stands before the end of its next turn, it takes 3d8 mental damage. If the creature succeeds, it's temporarily immune for 1 minute."
  - name: "Sublime Vision"
    desc: "⬺ (Divine)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The okenevem casts the _overwhelming presence_ spell, except instead of aggrandizing themself, the okenevem summons a vision of Heaven within 100 feet, and the target must humble themself in self-reflection rather than pay tribute."
sourcebook: "_Monster Core 2_, page 38."
```

```encounter-table
name: Okenevem
creatures:
  - 1: Okenevem
```
