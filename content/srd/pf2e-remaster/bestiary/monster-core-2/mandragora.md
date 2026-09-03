---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mandragora"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Mandragora"
level: 4
source: "Monster Core 2"
aon_id: "creature-4471"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4471"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mandragora"
level: "Creature 4"
size: "Small"
trait_01: "Plant"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; blood scent, low-light vision"
languages: "Chthonian, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +10, Stealth +12"
abilityMods: [2, 5, 3, -1, 2, 0]
abilities_top:
  - name: "Blood Scent"
    desc: "A mandragora can smell creatures with blood as an imprecise sense at a range of 30 feet, and it can smell demons, fey, and sorcerers with blood as a precise sense at a range of 30 feet."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +13; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ bludgeoning 5, electricity 5; __Weaknesses__ fire 5"
abilities_mid:
  - name: "Vulnerability to Supernatural Darkness"
    desc: "Whenever a mandragora begins its turn in an area of magical darkness, it's slowed 1 on that turn."
speed: "30 feet, burrow 10 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 (Finesse) __Damage__ 2d8+4 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ thorny vine +14 (Agile, finesse, reach 10 feet) __Damage__ 2d4+4 slashing plus mandragora venom"
abilities_bot:
  - name: "Blood Drain"
    desc: "⬻"
  - name: "Requirements"
    desc: "The mandragora has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The mandragora drains blood from the creature it has grabbed or restrained, dealing 2d6 piercing damage (DC 21 basic Fortitude save). If the creature is a demon, fey, or sorcerer, the mandragora gains temporary Hit Points equal to the damage dealt for 1 minute. A creature that takes any damage from having its blood drained by a mandragora is drained 1 until it receives any kind or amount of healing."
  - name: "Mandragora Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage, confused, and stupefied 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage, confused, and stupefied 1 (1 round)"
  - name: "Piercing Shriek"
    desc: "⬻ (Auditory, mental, primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The mandragora emits an unsettling shriek. Each non-mandragora creature within 30 feet must attempt a DC 23 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is sickened 1."
  - name: "Failure"
    desc: "The creature is sickened 2."
  - name: "Critical Failure"
    desc: "The creature is sickened 2 and slowed 1. As long as the creature remains sickened, this slowed condition value can't be reduced below 1. Madragora Sucklings Sometimes a mandragora offers its services to a spellcaster in exchange for sustenance. Tales tell of sorcerers or other magical creatures that keep mandragora “familiars” whose loyalty is sustained by feeding the little beasts with their own blood. These tales generally have gruesome endings wherein the mandragora is overcome with bloodlust and, unable to control itself, devours its master."
sourcebook: "_Monster Core 2_, page 219."
```

```encounter-table
name: Mandragora
creatures:
  - 1: Mandragora
```
