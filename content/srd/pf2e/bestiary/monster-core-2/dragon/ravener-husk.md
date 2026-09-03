---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ravener Husk"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ravener Husk"
level: 14
source: "Monster Core 2"
aon_id: "creature-4530"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4530"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ravener Husk"
level: "Creature 14"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Rare"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, soulsense 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +28"
abilityMods: [8, 0, 6, -5, 4, 4]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +28; __Ref__: +22; __Will__: +26"
hp: 325
health:
  - name: "HP"
    desc: "325 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, sleep; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 31 **Boneshatter ⬲"
  - name: "Trigger"
    desc: "The ravener husk takes any amount of bludgeoning damage**"
  - name: "Effect"
    desc: "The ravener's brittle bones shatter, spraying bone shards everywhere. Every creature within a 10-foot emanation of the ravener husk takes 7d6 piercing damage (DC 31 basic Reflex save)."
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +29 (Magical, reach 15 feet) __Damage__ 3d8+16 piercing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ claw +29 (Agile, magical, reach 10 feet) __Damage__ 3d4+16 slashing plus 2d6 void"
abilities_bot:
  - name: "Void Breath"
    desc: "⬺ (Divine, void) The ravener husk breathes a torrent of void energy that deals 16d6 void damage in a 40-foot cone (DC 34 basic Reflex save). They can't use Void Breath again for 1d4 rounds."
  - name: "Ravenous Repast"
    desc: "⬽ (Divine)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The ravener husk makes a jaws Strike against a deceased creature that has been dead no longer than 1 minute, was holy, and was at least level 15 in life. The ravener attempts a DC 5 flat check; if successful, they transform back into a ravener with 1 Hit Point in their soul ward."
sourcebook: "_Monster Core 2_, page 271."
```

```encounter-table
name: Ravener Husk
creatures:
  - 1: Ravener Husk
```
