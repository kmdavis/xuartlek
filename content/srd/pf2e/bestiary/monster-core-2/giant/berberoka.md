---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Berberoka"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/huge
statblock: inline
name: "Berberoka"
level: 15
source: "Monster Core 2"
aon_id: "creature-4281"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4281"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Berberoka"
level: "Creature 15"
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +26"
abilityMods: [8, 4, 6, -1, 3, 4]
abilities_top:
  - name: "Deep Breath"
    desc: "A berberoka can hold their breath for 2 hours."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +29; __Ref__: +23; __Will__: +24"
hp: 310
health:
  - name: "HP"
    desc: "310; __Weaknesses__ fear of crabs"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Fear of Crabs"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) If a berberoka sees a crab or crab-like creature, they must attempt a DC 33 Will save. They then become immune to the sight of that creature for 10 minutes."
  - name: "Critical Success"
    desc: "The berberoka is unaffected."
  - name: "Success"
    desc: "The berberoka becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2."
  - name: "Failure"
    desc: "The berberoka gains the [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] condition for 1 round and is frightened 4."
speed: "30 feet, swim 30 feet; 15 feet while waterlogged"
attacks:
  - name: "Melee"
    desc: "⬻ fist +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+16 bludgeoning plus Grab"
abilities_bot:
  - name: "Greater Constrict"
    desc: "⬻ 2d12+12 bludgeoning, DC 33"
  - name: "Consume Lake"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The berberoka drinks a prolific amount from an adjacent water source. If the water source is equal to or greater in volume than themself, the berberoka consumes up to 1,500 gallons of water per minute and becomes waterlogged. They can release water at the same rate. While waterlogged, the berberoka can use Spray Water, their size grows to Gargantuan, and their Speed is reduced to 15 feet."
  - name: "Spray Water"
    desc: "⬺"
  - name: "Requirements"
    desc: "The berberoka is waterlogged"
  - name: "Effect"
    desc: "The berberoka sprays a blast of water in a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] and is no longer waterlogged. All creatures in the line take 12d8 bludgeoning damage (DC 35 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). On a failed save, a creature is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] and pushed back 5 feet (10 feet on a critically failed save). Kabourophobia Berberokas share an unusually intense fear of crabs, so many folktales suggest that fishers bring a crab with them should they suspect a berberoka is lurking nearby. If no crab is available, clicking one's tongue or snapping one's fingers might suffice."
sourcebook: "_Monster Core 2_, page 57."
```

```encounter-table
name: Berberoka
creatures:
  - 1: Berberoka
```
