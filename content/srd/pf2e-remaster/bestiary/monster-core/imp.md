---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Imp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Imp"
level: 1
source: "Monster Core"
aon_id: "creature-3067"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3067"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Imp"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Chthonian, Common, Daemonic, Diabolic; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Arcana +6, Deception +7, Religion +5"
abilityMods: [-1, 4, 0, 1, 2, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9; __Will__: +7"
hp: 15
health:
  - name: "HP"
    desc: "15; __Resistances__ poison 3; __Weaknesses__ holy 3"
speed: "20 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stinger +9 (Agile, Finesse, Magical, reach 0 feet, Unholy) __Damage__ 1d4–1 piercing plus imp venom"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The imp takes on the appearance of a Medium or smaller animal (page 358). While transformed, the imp loses their normal senses, innate spells, and special actions, but doesn't otherwise change their statistics and can still speak and use telepathy. The imp also gains any special senses of the animal and any Speeds the animal has. This doesn't change the attack and damage modifiers of their Strikes but might change the damage type their Strikes deal (depending on what kinds of attacks the animal has) and prevents them from exposing creatures to imp venom."
  - name: "Fiendish Healing"
    desc: "⬻ (Concentrate, Divine, Healing, Vitality)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The imp regains 1d6 Hit Points."
  - name: "Fiendish Temptation"
    desc: "⬻ (Concentrate, Divine, Fortune, Unholy)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The imp offers a non-fiend within 15 feet a bargain, granting a boon of good luck if the creature accepts voluntarily. The boon lasts for 1 hour once accepted. Once during the hour, the creature can roll an attack roll or saving throw twice and use the higher result. If the creature dies while the boon is in place, the imp decides where the creature's soul travels. This typically makes the soul bound for eternity in the imp's home plane, and the creature unable to be raised or resurrected except by the _wish_ ritual or similar magic."
  - name: "Imp Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage, clumsy 1, and slowed 1 (1 round) Imps of Many Planes Like rats infesting cities, imps litter the fiendish Outer Planes—Abaddon, the Outer Rifts, and most especially Hell. Imps love to learn the tricks of devils, the better to tempt mortals and confine souls. Over centuries spent on the various planes, imps begin to take on the characteristics of the environment they inhabit, often looking flamescorched if they come from Hell, caustic and monstrous if from the Outer Rifts, and red-eyed and fetid if from Abaddon."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Detect Magic - __1st__ Charm - __2nd__ Invisibility (at will; self only) - __4th__ Read Omens"
sourcebook: "_Monster Core_, page 206."
```

```encounter-table
name: Imp
creatures:
  - 1: Imp
```
