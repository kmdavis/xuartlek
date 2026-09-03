---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Con Rit"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/huge
statblock: inline
name: "Con Rit"
level: 7
source: "Monster Core"
aon_id: "creature-2884"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2884"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Con Rit"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [6, 3, 4, -5, 1, -4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +14; __Will__: +10"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ slashing 5, piercing 5; __Weaknesses__ bludgeoning 5"
speed: "10 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandible +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+8 piercing plus con rit venom"
abilities_bot:
  - name: "Con Rit Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d10 poison (1 round)"
  - name: "Stage 2"
    desc: "2d10 poison and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison, off-guard, and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 round)"
  - name: "Spit Venom"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The con rit spits a propulsive blast of venom that deals 2d10 poison and 2d10 bludgeoning damage in a 30-foot line (DC 25 basic Fortitude save). Creatures who fail their save are also pushed 10 feet. The con rit cannot use Spit Venom again for 1d4 rounds."
  - name: "Undulate"
    desc: "⬻ The con rit Swims. During this movement, it can pass through spaces as narrow as 5 feet without [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeezing]]. Stubborn Reluctance Those who experience the might and tenacity of such a creature often wonder why they are so rarely seen throughout the world. This is due to their reluctance to explore and their stubborn determination to endlessly fight over the same territory. Only in rare instances do larval con rits move to another territory, and it is never by choice. They are either relocated due to a weather phenomenon, a strange change in the currents, or by people."
sourcebook: "_Monster Core_, page 67."
```

```encounter-table
name: Con Rit
creatures:
  - 1: Con Rit
```
