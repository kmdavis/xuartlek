---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spider Swarm"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Spider Swarm"
level: 0
source: "Monster Core"
aon_id: "creature-3206"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3206"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Spider Swarm"
level: "Creature 0"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision, web sense"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +2, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [-2, 3, 0, -5, 0, -4]
abilities_top:
  - name: "Web Sense"
    desc: "The spider swarm has imprecise tremorsense to detect the vibrations of creatures touching its web."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +4; __Ref__: +7; __Will__: +2"
hp: 12
health:
  - name: "HP"
    desc: "12; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "20 feet, climb 20 feet"
abilities_bot:
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the spider swarm's space takes 1d4 piercing damage with a DC 14 basic Reflex save. A creature that fails its save is exposed to spider swarm venom."
  - name: "Spider Swarm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 14 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
sourcebook: "_Monster Core_, page 320."
```

```encounter-table
name: Spider Swarm
creatures:
  - 1: Spider Swarm
```
