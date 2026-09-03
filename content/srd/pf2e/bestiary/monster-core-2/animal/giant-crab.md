---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Crab"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Crab"
level: 2
source: "Monster Core 2"
aon_id: "creature-4302"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4302"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Crab"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [4, 3, 1, -4, 2, -3]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +9; __Will__: +7"
hp: 25
health:
  - name: "HP"
    desc: "25; __Resistances__ physical 3 (except bludgeoning)"
abilities_mid:
  - name: "Vulnerable to Prone"
    desc: "If a creature critically succeeds at a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] the giant crab, the crab is flipped over onto its back in addition to the usual effects. Until it Stands, a giant crab that's flipped onto its back has a particularly hard time defending itself; instead of taking the normal –2 circumstance penalty to AC for being [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], it takes a –4 circumstance penalty to AC."
  - name: "Scuttle"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature that the giant crab can see targets the crab with an attack while the giant crab isn't prone"
  - name: "Effect"
    desc: "The giant crab scuttles to the side and gains a +2 circumstance bonus to AC against the triggering attack. After the attack resolves, the crab can [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]] up to its speed in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] as part of the reaction."
speed: "25 feet, swim 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 __Damage__ 1d10+4 slashing plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d6+3 bludgeoning, DC 18"
sourcebook: "_Monster Core 2_, page 77."
```

```encounter-table
name: Giant Crab
creatures:
  - 1: Giant Crab
```
