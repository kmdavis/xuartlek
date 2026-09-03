---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goliath Spider"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Goliath Spider"
level: 11
source: "Monster Core"
aon_id: "creature-3209"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3209"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goliath Spider"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Animal"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, web sense"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22"
abilityMods: [8, 5, 7, -5, 3, -4]
abilities_top:
  - name: "Web Sense"
    desc: "The spider has imprecise tremorsense to detect the vibrations of creatures touching its web."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +25; __Ref__: +21; __Will__: +17"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Spring Upon Prey"
    desc: "⬲"
  - name: "Requirements"
    desc: "Initiative has not yet been rolled"
  - name: "Trigger"
    desc: "A creature touches the goliath spider's web while the spider is on it"
  - name: "Effect"
    desc: "The goliath spider automatically notices the creature and Strides, Climbs, or Descends on a Web before it rolls initiative."
speed: "45 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+12 piercing plus goliath spider venom"
  - name: "Ranged"
    desc: "⬻ web +22 (range increment 60 feet) __Damage__ web tether"
abilities_bot:
  - name: "Descend on a Web"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The goliath spider moves straight down up to 120 feet, suspended by a web line. It can hang from the web or drop off. The distance it Descends on a Web doesn't count for falling damage. A creature that successfully Strikes the web (AC 20, Hardness 5, 20 HP) severs it, causing the spider to fall."
  - name: "Goliath Spider Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 30 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage and __slowed 1__ (1 round)"
  - name: "Stage 2"
    desc: "3d8 poison damage and slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "3d10 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] for 2d4 hours"
  - name: "Web Tether"
    desc: "A creature hit by the spider's web Strike is [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] and tethered to the spider, preventing it from being moved farther away from the spider. The spider can have one creature tethered at a time. The DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Force Open]] the web is 30. The tether can be severed with a Strike (AC 20, Hardness 5, HP 20), but this doesn't free the restrained creature."
sourcebook: "_Monster Core_, page 321."
```

```encounter-table
name: Goliath Spider
creatures:
  - 1: Goliath Spider
```
