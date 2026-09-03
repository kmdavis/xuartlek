---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grimple"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/tiny
statblock: inline
name: "Grimple"
level: -1
source: "Monster Core 2"
aon_id: "creature-4422"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4422"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Grimple"
level: "Creature -1"
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "Sakvroth"
skills:
  - name: "Skills"
    desc: "Crafting +5, Deception +2, Nature +4, Stealth +5, Thievery +5"
abilityMods: [1, 3, 3, 1, 2, -2]
abilities_top:
  - name: "Items"
    desc: "satchel with 5 rocks"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +7; __Will__: +4"
hp: 9
health:
  - name: "HP"
    desc: "9; __Weaknesses__ cold iron 2"
abilities_mid:
  - name: "Gremlin Lice"
    desc: "Whenever a living creature touches or is touched by a grimple (including via a successful unarmed melee Strike), it must succeed at a DC 13 Reflex save or become infested by gremlin lice. While infested, the targeted creature is distracted by the itching sensation and is stupefied 1, though it can use an Interact action to scratch at the itching lice to suppress the stupefied condition from the lice for 1d4 rounds. The infestation ends after 24 hours or until the creature is submerged in water or exposed to a severe cold environment, whichever comes first."
speed: "10 feet, climb 20 feet, fly 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +7 (Agile, finesse) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ rock +7 (Agile, range increment 20 feet) __Damage__ 1d4+1 bludgeoning"
abilities_bot:
  - name: "Putrid Vomit"
    desc: "⬻ The grimple spews a 30-foot line of vomit. Each creature in the line must succeed at a DC 16 Fortitude save or become sickened 1 (sickened 2 on a critical failure). The grimple can't use Putrid Vomit again for 1d4 rounds. Grimple Allies Grimples sometimes team up with other gremlins to cause trouble. Stronger gremlins, such as jinkins, use cranky grimples to lure victims into dangerous traps. Left to their own devices, grimples bully mitflits or train giant rats (Monster Core 288) and spider swarms to do their bidding."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Prestidigitation, Telekinetic Hand - __1st__ Grease"
sourcebook: "_Monster Core 2_, page 176."
```

```encounter-table
name: Grimple
creatures:
  - 1: Grimple
```
