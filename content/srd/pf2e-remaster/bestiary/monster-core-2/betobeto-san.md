---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Betobeto-San"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Betobeto-San"
level: 12
source: "Monster Core 2"
aon_id: "creature-4282"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4282"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Betobeto-San"
level: "Creature 12"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Shadow"
trait_03: "Spirit"
trait_04: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; greater darkvision, fearsense (precise) 60 feet"
languages: "Common, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Deception +23, Intimidation +23, Stealth +27"
abilityMods: [4, 7, 5, 4, 4, 5]
abilities_top:
  - name: "Fearsense"
    desc: "(mental, occult) The betobeto-san is aware of all frightened creatures within the listed range."
  - name: "Items"
    desc: "sandals"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +19; __Ref__: +25; __Will__: +22"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ disease, paralyzed, poison, precision; __Resistances__ all damage 10 (except force, _ghost touch_, spirit, or vitality) double resistance vs. non-magical)"
abilities_mid:
  - name: "Ominous Footsteps"
    desc: "(auditory, aura, emotion, fear, illusion, mental, occult) 60 feet. The betobeto-san's footsteps seem to draw ever closer, yet the source remains difficult to pinpoint. Each creature that starts its turn within 60 feet of the betobeto-san must attempt a DC 29 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature becomes frightened 1."
  - name: "Failure"
    desc: "The creature becomes frightened 2."
  - name: "Critical Failure"
    desc: "The creature becomes frightened 4."
  - name: "Shadow Invisibility"
    desc: "The betobeto-san is invisible unless within an area of bright light."
  - name: "Shadow Step"
    desc: "⬲ (occult, shadow, teleportation)"
  - name: "Requirements"
    desc: "The betobeto-san isn't already within an area of bright light"
  - name: "Trigger"
    desc: "A bright light source reveals the betobeto-san"
  - name: "Effect"
    desc: "The betobeto-san Steps briefly into the Netherworld and then back again, appearing up to 30 feet away from where they began."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 (Agile, finesse, magical) __Damage__ 3d12+10 void"
abilities_bot:
  - name: "Stepping Decoy"
    desc: "⬻ (Auditory, illusion, occult) The betobeto-san Steps. They then create two illusory decoys of sound within 15 feet of them that mimic the sounds of their ominous footsteps. These decoys act independently on the betobeto-san's initiative with 2 actions apiece. They can only Sneak or Stride, and they have a Speed of 35 feet. Use the betobeto-san's Stealth DC (typically 37) against attempts to Seek or disbelieve a decoy. Each decoy lasts for 1 minute. Any existing decoys vanish if the betobeto-san uses this ability again. Shadowy Afterimages Betobeto-san are the afterimages of travelers who have passed between the Netherworld and the Universe. While few such journeys create betobeto-san, sages posit that certain emotions or intents from those who travel between these planes can create these apparitions during the transit."
sourcebook: "_Monster Core 2_, page 58."
```

```encounter-table
name: Betobeto-San
creatures:
  - 1: Betobeto-San
```
