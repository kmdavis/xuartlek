---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ambush Copse"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Ambush Copse"
level: 13
source: "Monster Core 2"
aon_id: "creature-4026"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4026"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ambush Copse"
level: "Creature 13"
size: "Huge"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; tremorsense 30 feet"
languages: "Common, Fey, Muan; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +27, Intimidation +20, Stealth +23"
abilityMods: [8, 4, 6, 0, 4, 0]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +22; __Will__: +22"
hp: 300
health:
  - name: "HP"
    desc: "300; __Resistances__ bludgeoning 10, piercing 10; __Weaknesses__ axes 10, fire 15"
abilities_mid:
  - name: "Berserk"
    desc: "An ambush copse that sees fire or axes has a chance of going berserk. At the start of its turn, if it is aware of an axe or a fire the size of a lit torch or larger, the ambush copse must succeed at a DC 5 flat check or go berserk. A berserk ambush copse can't use concentrate actions and wildly attacks the nearest living creature, or the nearest object if no creatures are nearby."
  - name: "Blinding Branches"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 20 feet of the ambush copse leaves a square during a move action it's using"
  - name: "Requirements"
    desc: "The triggering creature is in forest terrain"
  - name: "Effect"
    desc: "The ambush copse's elemental energy animates nearby tree branches to swat at the creature's face. The triggering creature must succeed at a DC 30 Reflex save or become blinded for 1 round."
  - name: "Felling Ambush"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature moves within 10 feet of the ambush copse"
  - name: "Requirements"
    desc: "The ambush copse is disguised as trees or logs"
  - name: "Effect"
    desc: "The ambush copse makes a log Strike against the triggering creature. If the attack hits, the creature must attempt a DC 30 Reflex save or be knocked prone."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ log +27 (Backswing, Forceful, reach 20 feet, Sweep) __Damage__ 3d12+14 bludgeoning plus pounding smash"
  - name: "Ranged"
    desc: "⬻ caber +25 (thrown 40 feet) __Damage__ 3d12+6 bludgeoning"
abilities_bot:
  - name: "Feign Copse"
    desc: "⬻ (Concentrate) Until the next time it acts, the ambush copse appears to be a harmless patch of trees or logs. It has an automatic result of 43 (45 in forests) on Deception checks and DCs to pass as trees or logs."
  - name: "Pounding Smash"
    desc: "Regardless of whether the Strike hits or misses, the ambush copse's melee Strikes create a 5-foot-square of difficult terrain in the target's space."
  - name: "Pulverizing Barrage"
    desc: "⬽ The ambush copse makes three log Strikes, each at a –2 penalty, all targeting the same creature. The ambush copse's multiple attack penalty doesn't increase until after it has made all three attacks. The ambush copse gains the clumsy 2 condition until the beginning of its next turn."
  - name: "Sunder Objects"
    desc: "When an ambush copse damages an item or structure, it deals an additional 15 damage to that item or structure. Ravages Of Revenge An endless wait for revenge invariably leaves an ambush copse riddled with mushrooms and termites. Apply the weak adjustment to such an ambush copse and give it weakness 10 to bludgeoning damage. During a period of dormancy, parts of the ambush corpse might break off, gain their own sentience, and make their way into a nearby camp or village. Use the stats for a twigjack to represent these stray pieces, whose arrival might presage the full awakening of an ambush copse."
sourcebook: "_Monster Core 2_, page 24."
```

```encounter-table
name: Ambush Copse
creatures:
  - 1: Ambush Copse
```
