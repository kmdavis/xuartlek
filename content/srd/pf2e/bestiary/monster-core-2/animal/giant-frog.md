---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Frog"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Frog"
level: 1
source: "Monster Core 2"
other_sources: "Pathfinder Game Night: Dawn of the Frogs (Deluxe Adventure)"
aon_id: "creature-4404"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4404"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Frog"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [3, 2, 3, -4, 2, -1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +7; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d6+3 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tongue +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ tongue grab"
abilities_bot:
  - name: "Sticky Feet"
    desc: "Giant frogs are not [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] when [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balancing]] on a narrow surface, and they gain a +4 circumstance bonus to Reflex saves to avoid [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Falling|falling]]."
  - name: "Tongue Grab"
    desc: "A creature hit by the giant frog's tongue becomes [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the giant frog. The creature isn't [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], but it can't move beyond the reach of the frog's tongue. A creature can sever the tongue with a Strike against AC 13 that deals at least 2 slashing damage. This deals no damage to the frog but prevents it from using its tongue Strike until it regrows its tongue, which takes a week."
sourcebook: "_Monster Core 2_, page 158."
```

```encounter-table
name: Giant Frog
creatures:
  - 1: Giant Frog
```
