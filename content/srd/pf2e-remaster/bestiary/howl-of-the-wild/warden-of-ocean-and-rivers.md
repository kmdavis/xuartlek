---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warden of Ocean and Rivers"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/water
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Warden of Ocean and Rivers"
level: 22
source: "Howl of the Wild"
aon_id: "creature-3327"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3327"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Warden of Ocean and Rivers"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Beast"
trait_03: "Unique"
trait_04: "Water"
modifier: 39
perception:
  - name: "Perception"
    desc: "Perception +39; darkvision, scent (imprecise) 200 feet"
languages: "voice of nature"
skills:
  - name: "Skills"
    desc: "Acrobatics +37, Athletics +40, Intimidation +36, Nature +39, Stealth +42, Survival +42"
abilityMods: [10, 9, 12, 6, 8, 6]
abilities_top:
  - name: "Voice of Nature"
    desc: ""
  - name: "Warden's Crown"
    desc: ""
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +39; __Ref__: +36; __Will__: +33 +1 to all saves vs. primal"
hp: 540
health:
  - name: "HP"
    desc: "540; __Immunities__ controlled, emotion, mental, poison, precision; __Resistances__ bludgeoning 20, cold 20; __Weaknesses__ electricity 15"
abilities_mid:
  - name: "Bioluminescent Maelstrom"
    desc: "(aura, primal, visual, water) 30 feet. The warden's wrath conjures a dazzling storm around them that makes the area difficult terrain. Creatures that enter the storm must attempt a DC 45 Will save. A creature that succeeds at this save is temporarily immune to the luring visuals for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is dazzled for 1 round, and for the first action on its next turn, the creature must use a single action to move as close to the warden as possible."
  - name: "Critical Failure"
    desc: "The creature is dazzled for as long as it remains in the aura. Whenever the creature begins its turn within the aura, the creature must use the first action of its turn to move as close to the warden as possible. It can attempt a new save at the end of its turn, ending this effect on a success."
speed: "swim 100 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horned crown +41 (Magical, reach 10 feet) __Damage__ 2d8+15 cold plus 2d8+15 poison"
  - name: "Melee"
    desc: "⬻ tentacle +43 (Agile, reach 30 feet, Magical) __Damage__ 4d10+16 bludgeoning plus Grasp of the Deep"
abilities_bot:
  - name: "All Are One"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Effect"
    desc: "The warden attracts organisms that extend their influence. The area of bioluminescent maelstrom and the reach of their tentacle Strike increase by 10 feet for 1 minute, to a maximum of an additional 30 feet."
  - name: "Arctic Embrace"
    desc: "⬺ (Cold) All creatures in the warden's bioluminescent maelstrom take 10d6 cold damage (DC 45 basic Fortitude save). On a failure, the creature is also slowed 1 for 1 round."
  - name: "Grasp of the Deep"
    desc: "Creatures struck by one of the warden's tentacles gain cold weakness 10 and take a –2 status penalty to Fortitude saves for 1 round."
  - name: "I Am The Tide"
    desc: "⬺ (Primal, Water) The warden creates three lines of rushing water, each 10 feet wide and 120 feet long. Creatures in the area take 18d8 bludgeoning damage (DC 45 basic Fortitude save). The warden can either push or pull, and all creatures that fail this save move up to 40 feet in the direction chosen. The warden can't use I Am The Tide again for 1d4 rounds."
  - name: "What Lurks Beneath"
    desc: "⬽ The warden attacks with their tentacles six times."
sourcebook: "_Howl of the Wild_, page 207."
```

```encounter-table
name: Warden of Ocean and Rivers
creatures:
  - 1: Warden of Ocean and Rivers
```
