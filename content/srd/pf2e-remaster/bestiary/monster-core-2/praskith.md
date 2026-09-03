---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Praskith"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/huge
statblock: inline
name: "Praskith"
level: 7
source: "Monster Core 2"
aon_id: "creature-4516"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4516"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Praskith"
level: "Creature 7"
size: "Huge"
trait_01: "Fungus"
trait_02: "Plant"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision"
languages: "Fey; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +15, Stealth +14"
abilityMods: [7, 2, 5, -2, 3, 0]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +12; __Will__: +13"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ acid; __Resistances__ piercing 5, slashing 5; __Weaknesses__ fire 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ Vine only."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mouth +18 (reach 10 feet) __Damage__ 2d10+11 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ vine +18 (Agile, reach 15 feet) __Damage__ 2d6+11 bludgeoning plus Grab"
abilities_bot:
  - name: "Praskith Venom"
    desc: "(Incapacitation, Poison)"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "clumsy 2 (1 round); Stage 2 clumsy 2 and slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "paralyzed (1 round)"
  - name: "Rampant Growth"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature the praskith has Swallowed Whole has taken damage since the end of the praskith's last turn, and the praskith hasn't used any other actions this turn"
  - name: "Effect"
    desc: "The praskith regains 3d8 Hit Points and recovers from the fatigued and slowed conditions. It reduces any enfeebled value it has by 2."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Large, 2d10+7 acid plus praskith venom, Rupture 14 Praskith Lacquer Objects coated with praskith lacquer gain resistance 5 to acid. Making and applying praskith lacquer requires a 5th-level formula, the Alchemical Crafting skill feat, and the fluid from the stomach of a praskith. A successful DC 20 Crafting check and 4 days of work are enough to protect 1 Bulk of items with no other cost in materials, but the fluid is used up even on a failed check."
sourcebook: "_Monster Core 2_, page 257."
```

```encounter-table
name: Praskith
creatures:
  - 1: Praskith
```
