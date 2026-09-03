---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tor Linnorm"
tags:
  - pf2e/creature/level/21
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tor Linnorm"
level: 21
source: "Monster Core"
aon_id: "creature-3086"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3086"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tor Linnorm"
level: "Creature 21"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Uncommon"
modifier: 37
perception:
  - name: "Perception"
    desc: "Perception +37; darkvision, scent (imprecise) 60 feet, _truesight_"
languages: "Aklo, Draconic, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +35, Athletics +40, Stealth +37"
abilityMods: [11, 8, 9, -1, 8, 9]
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +38; __Ref__: +35; __Will__: +33 +1 status to all saves vs. magic"
hp: 440
health:
  - name: "HP"
    desc: "440 , regeneration 20 (deactivated by cold iron); __Immunities__ curse, fire, paralyzed, sleep; __Weaknesses__ cold iron 15"
abilities_mid:
  - name: "Curse of Boiling Blood"
    desc: "(curse, fire, primal) When a creature slays the linnorm, it must succeed at a DC 48 Will save or gain weakness to fire 20 and slowed 1 from the agonizing pain it now endures at all times, with an unlimited duration. As long as a character continues to suffer this curse, its slowed condition can never be reduced below slowed 1."
  - name: "Lava Affinity"
    desc: "The linnorm can breathe and swim freely while submerged in lava and magma."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "35 feet, climb 35 feet, fly 100 feet, swim 60 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +40 (reach 30 feet, Magical) __Damage__ 4d12+19 piercing plus tor linnorm venom"
  - name: "Melee"
    desc: "⬻ claw +40 (reach 30 feet, Agile, Magical) __Damage__ 4d8+19 slashing"
  - name: "Melee"
    desc: "⬻ tail +40 (reach 30 feet, Agile, Magical) __Damage__ 4d6+19 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d6+21 bludgeoning, DC 46"
  - name: "Pyroclastic Breath"
    desc: "⬺ (Fire, Primal) The tor linnorm expels a 60-foot cone of flame and ash dealing 20d6 fire damage to creatures within the area (DC 46 basic Reflex save). The linnorm can't use Pyroclastic Breath again for 1d4 rounds. At the start of the tor linnorm's next turn, the area of the Pyroclastic Breath is covered in thick, scorching smoke that burns both the lungs and eyes, dealing an additional 10d6 fire damage to all creatures in the area (DC 46 basic Reflex save). A creature that spends an entire round in the smoke with open eyes must succeed at a DC 44 Fortitude save or be blinded for 1 minute. The smoke dissipates after 1 minute; in strong winds, the smoke dissipates in 5 rounds, and in more powerful winds, it may clear even more quickly."
  - name: "Slashing Claws"
    desc: "⬻ The tor linnorm makes four Strikes with their claws, each against a different target. These attacks count toward the tor linnorm's multiple attack penalty, but the multiple attack penalty doesn't increase until after the tor linnorm makes all their attacks."
  - name: "Tor Linnorm Venom"
    desc: "(Fire, Poison)"
  - name: "Saving Throw"
    desc: "DC 44 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "8d6 fire damage and drained 1 (1 round)"
  - name: "Stage 2"
    desc: "12d6 fire damage and drained 2 (1 round)"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 44 - __8th__ Truesight - __Constant (9th)__ Unfettered Movement"
sourcebook: "_Monster Core_, page 222."
```

```encounter-table
name: Tor Linnorm
creatures:
  - 1: Tor Linnorm
```
