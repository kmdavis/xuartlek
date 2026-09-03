---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Shark"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/large
statblock: inline
name: "Goblin Shark"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3307"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3307"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Goblin Shark"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; blood scent, electrolocation 20 feet, scent (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [6, 4, 5, -4, 3, -3]
abilities_top:
  - name: "Blood Scent"
    desc: "The shark can smell blood in the water from up to 1 mile away."
  - name: "Camouflage"
    desc: "The goblin shark's coloration blends in with the water. It doesn't need cover to attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] with a [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] check while underwater."
  - name: "Electrolocation"
    desc: "A goblin shark can sense minute electrical charges in living creatures, which it can use as a precise sense at a range of 20 feet."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +16; __Ref__: +11; __Will__: +10"
hp: 85
health:
  - name: "HP"
    desc: "85"
abilities_mid:
  - name: "Grasping Jaws"
    desc: "Creatures that successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] from the goblin shark's jaws take 1d6 persistent bleed as the shark's hold tears flesh away."
speed: "swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+6 piercing plus Grab"
abilities_bot:
  - name: "Lunging Bite"
    desc: "⬺ The goblin shark dashes forward and extends its jaws bite a creature. It swims up to 10 feet in a straight line and makes a jaws Strike with a reach of 10 feet."
sourcebook: "_Howl of the Wild_, page 179."
```

```encounter-table
name: Goblin Shark
creatures:
  - 1: Goblin Shark
```
