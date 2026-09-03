---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Mantis"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Mantis"
level: 3
source: "Monster Core"
aon_id: "creature-3094"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3094"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Mantis"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [5, 3, 3, -5, 2, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +12; __Will__: +7"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet, climb 25 feet, fly 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ leg +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+5 piercing plus Capturing Grab"
  - name: "Melee"
    desc: "⬻ mandibles + 12 __Damage__ 1d12+5 piercing"
abilities_bot:
  - name: "Capturing Grab"
    desc: "⬻ This ability functions as Grab, plus on a success, the mantis can choose to pull the creature adjacent to it, then makes a mandibles Strike against the creature. This extra benefit doesn't apply when the mantis maintains the Grab."
  - name: "Lunging Strike"
    desc: "⬺ The giant mantis lunges forward, making a leg Strike with an extended reach of 20 feet. If it hits, the mantis can use Capturing Grab after the Strike even if the creature is out of reach."
  - name: "Sudden Strike"
    desc: "On the first round of combat, creatures that haven't acted are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the giant mantis."
sourcebook: "_Monster Core_, page 229."
```

```encounter-table
name: Giant Mantis
creatures:
  - 1: Giant Mantis
```
