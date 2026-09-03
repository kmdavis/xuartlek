---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Frost Giant"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Frost Giant"
level: 9
source: "Monster Core"
aon_id: "creature-3013"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3013"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Frost Giant"
level: "Creature 9"
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision"
languages: "Common, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +23, Crafting +18, Intimidation +18, Nature +17, Stealth +17"
abilityMods: [6, 0, 5, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Breastplate, _+1 striking greataxe_"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +23; __Ref__: +16; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ cold; __Weaknesses__ fire 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet; ice stride"
attacks:
  - name: "Melee"
    desc: "⬻ _greataxe_ +21 (Magical, reach 10 feet, Sweep) __Damage__ 2d12+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +21 (Agile, reach 10 feet) __Damage__ 2d8+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ icicle +19 (Cold, Primal, range 120 feet) __Damage__ 2d8 piercing plus 3d6 cold"
abilities_bot:
  - name: "Chill Breath"
    desc: "⬻ (Cold, Primal) The frost giant breathes out a 15-foot cone of freezing moisture that quickly condenses into ice, dealing 4d6 cold damage. Each creature in the cone must attempt a DC 28 basic Reflex save. A creature that fails its save is also immobilized and takes 2d6 cold damage at the end of each of its turns until it gets free (Escape DC 28). The giant can't use Chill Breath again for 1d4 rounds."
  - name: "Ice Stride"
    desc: "A frost giant isn't impeded by difficult terrain caused by snow or ice, nor do they need to attempt Acrobatics checks to keep from falling on slippery ice."
  - name: "Wide Swing"
    desc: "⬻ The frost giant makes a single greataxe Strike and compares the attack roll result to the ACs of up to two foes within their reach. This counts as two attacks for the frost giant's multiple attack penalty."
sourcebook: "_Monster Core_, page 165."
```

```encounter-table
name: Frost Giant
creatures:
  - 1: Frost Giant
```
