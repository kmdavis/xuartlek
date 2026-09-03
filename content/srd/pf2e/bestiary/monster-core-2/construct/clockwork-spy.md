---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Spy"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/tiny
statblock: inline
name: "Clockwork Spy"
level: -1
source: "Monster Core 2"
aon_id: "creature-4294"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4294"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Spy"
level: "Creature -1"
size: "Tiny"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +5"
abilityMods: [-1, 3, 0, -5, 2, 0]
abilities_top:
  - name: "Record Audio"
    desc: "⬻ The clockwork spy records all sounds within 25 feet onto a small gemstone worth 1 gp embedded in its body. The clockwork spy can record up to 1 hour of sound on a single gemstone. Once it begins recording, it can't cease recording early, nor can it record onto a gemstone that already contains a recording. Some clockwork spies contain multiple gemstones to allow for a series of recordings. Since clockwork spies are not intelligent, they must be given simple commands regarding when to start recording sounds. A clockwork spy can differentiate between different kinds of creatures but not between specific individuals. The spy can start or stop playback of recorded sound by spending a single action. Removing a gemstone from or installing a gemstone into a clockwork spy requires a successful DC 14 Thievery check to Disable a Device; on a failure, the gemstone is undamaged, but any recorded sounds are erased and the gemstone still can't be used to make another recording."
  - name: "Wind-Up"
    desc: "24 hours, DC 14, standby"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +7; __Will__: +4"
hp: 7
health:
  - name: "HP"
    desc: "7; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Weaknesses__ electricity 2, orichalcum 2"
abilities_mid:
  - name: "Self-Destruct"
    desc: "⬲ A clockwork spy must use this reaction unless specifically programmed otherwise by its creator"
  - name: "Trigger"
    desc: "The clockwork spy is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The spy thrashes around and emits a tinny scream followed by a steady ticking sound. At the beginning of what would have been its next turn, the clockwork spy explodes, dealing 1d10 piercing damage in a 5-foot emanation (DC 16 basic Reflex save). Its gemstone is destroyed, along with any information contained inside it. An adjacent creature can cancel the self-destruct sequence by succeeding at a DC 16 Thievery check to Disable a Device."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spherical body +7 (Finesse) __Damage__ 1d6–1 bludgeoning"
sourcebook: "_Monster Core 2_, page 70."
```

```encounter-table
name: Clockwork Spy
creatures:
  - 1: Clockwork Spy
```
