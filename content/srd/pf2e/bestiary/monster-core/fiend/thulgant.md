---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thulgant"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/qlippoth
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Thulgant"
level: 18
source: "Monster Core"
aon_id: "creature-3157"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3157"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Thulgant"
level: "Creature 18"
size: "Large"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, _truesight_"
languages: "Chthonian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +32, Athletics +35, Occultism +33, Stealth +32"
abilityMods: [9, 6, 6, 5, 6, 9]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +30; __Ref__: +28; __Will__: +32"
hp: 305
health:
  - name: "HP"
    desc: "305 (fast healing 10); __Immunities__ controlled, fear; __Resistances__ mental 15, physical 15 (except cold iron)"
speed: "30 feet, climb 30 feet, fly 50 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ stinger +35 (Magical, reach 10 feet, Unholy) __Damage__ 3d12+17 piercing plus 4d6 mental and thulgant venom"
  - name: "Melee"
    desc: "⬻ tentacle +35 (Agile, Magical, reach 10 feet, Unholy) __Damage__ 3d8+17 bludgeoning plus 3d6 acid and Grab"
abilities_bot:
  - name: "Demon Hunter"
    desc: "⬻ (Occult) The thulgant causes a demon within 30 feet to suffer the effect of its sinful vulnerability."
  - name: "Greater Constrict"
    desc: "⬻ 2d6+17 bludgeoning and 1d6 acid, DC 40"
  - name: "Mind-Rending Sting"
    desc: "⬻"
  - name: "Requirement"
    desc: "The thulgant hits the same enemy with two consecutive sting Strikes in the same round"
  - name: "Effect"
    desc: "The thulgant deals 3d12+17 mental damage to the enemy. If the enemy is affected by thulgant venom, that poison gains the virulent trait."
  - name: "Stunning Display"
    desc: "⬺ (Concentrate, Emotion, Fear, Incapacitation, Mental, Occult, Visual) The thulgant rises up on its twitching limbs and presents its numerous tentacles and stingers in a horrifying display of awfulness. Creatures in a 30-foot emanation must attempt a DC 40 Will save, after which they are temporarily immune to further Stunning Displays for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is stunned 1."
  - name: "Failure"
    desc: "The creature is stunned 4."
  - name: "Critical Failure"
    desc: "The creature is stunned 8."
  - name: "Thulgant Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "Fortitude DC 40"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage and the victim gains one of the following at random: clumsy 1, enfeebled 1, or stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "6d6 poison damage and the victim gains two of the following at random: clumsy 2, enfeebled 2, or stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "9d6 poison damage and the victim gains all three of the following: clumsy 3, enfeebled 3, and stupefied 3 (1 round)."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40 - __Cantrips (9th)__ Daze, Detect Magic - __4th__ Unfettered Movement - __7th__ Interplanar Teleport - __8th__ Dispel Magic, Divine Decree, Phantom Pain (×3), Quandary - __9th__ Petrify (×3), Phantasmal Calamity - __Constant (6th)__ Truesight"
  - name: "Rituals"
    desc: "DC 40 - __8th__ Imprisonment"
sourcebook: "_Monster Core_, page 283."
```

```encounter-table
name: Thulgant
creatures:
  - 1: Thulgant
```
