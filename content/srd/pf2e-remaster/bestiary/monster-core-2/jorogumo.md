---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jorogumo"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Jorogumo"
level: 13
source: "Monster Core 2"
other_sources: "Pathfinder #160: Assault on Hunting Lodge Seven"
aon_id: "creature-4450"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4450"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Jorogumo"
level: "Creature 13"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Uncommon"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision"
languages: "Aklo, Common; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +23, Crafting +22, Deception +28, Diplomacy +26, Performance +24, Stealth +23, Survival +24"
abilityMods: [6, 4, 5, 3, 5, 7]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +23; __Will__: +26"
hp: 270
health:
  - name: "HP"
    desc: "270; __Resistances__ poison 15; __Weaknesses__ peachwood 10"
abilities_mid:
  - name: "Darting Legs"
    desc: "⬲"
  - name: "Requirements"
    desc: "The jorogumo has their spider legs extended or has Changed Shape"
  - name: "Trigger"
    desc: "The jorogumo is targeted with an attack"
  - name: "Effect"
    desc: "The jorogumo raises a leg, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 __Damage__ 3d12+14 piercing plus jorogumo venom"
  - name: "Melee"
    desc: "⬻ claw +27 (Agile) __Damage__ 3d8+14 slashing"
  - name: "Ranged"
    desc: "⬻ web +23 (range increment 60 feet) __Damage__ web trap"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, occult, polymorph) The jorogumo takes on the appearance of any Small or Medium spider. This doesn't change their Speed or Strikes."
  - name: "Jorogumo Venom"
    desc: "(Incapacitation, poison)"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude"
  - name: "Maximum Duration"
    desc: "4 hours"
  - name: "Stage 1"
    desc: "3d6 poison damage and stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 4"
    desc: "paralyzed for 1d4 hours"
  - name: "Spider Legs"
    desc: "⬻ (Concentrate, occult, polymorph)"
  - name: "Requirement"
    desc: "The jorogumo is in humanoid form"
  - name: "Effect"
    desc: "Eight large spider legs sprout from the jorogumo's back, granting a 40-foot climb Speed and allowing them to use the Darting Legs reaction."
  - name: "Web Trap"
    desc: "A creature hit by the jorogumo's web attack is immobilized and stuck to the nearest surface, preventing the creature from moving. The DC to Escape or Force Open the web trap is 32. Peachwood Vulnerability Peachwood, often cultivated by Pharasmin priests, is used to ward away the undead. However, jorogumo also despise this auburn-tinged wood, despite being quite clearly a living creature. This has led many to speculate on the origins of these arachnid ambushers, but their secretive nature has made further research difficult. Learn more about peachwood in Lost Omens Tian Xia Character Guide."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 34 - __1st__ Charm (at will) - __2nd__ Speak with Animals (spiders only) - __3rd__ Mind Reading (at will) - __4th__ Outcast's Curse (×3), Suggestion (×3) - __7th__ Summon Animal (spiders only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 201."
```

```encounter-table
name: Jorogumo
creatures:
  - 1: Jorogumo
```
