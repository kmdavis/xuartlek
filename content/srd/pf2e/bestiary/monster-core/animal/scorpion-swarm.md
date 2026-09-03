---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Scorpion Swarm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Scorpion Swarm"
level: 4
source: "Monster Core"
aon_id: "creature-3176"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3176"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Scorpion Swarm"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [0, 5, 2, -5, 0, -4]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +13; __Will__: +8"
hp: 55
health:
  - name: "HP"
    desc: "55; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grapple]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ bludgeoning 3, piercing 7, slashing 7; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "25 feet"
abilities_bot:
  - name: "Scorpion Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Swarming Stings"
    desc: "⬻ Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 basic Reflex save) and is exposed to scorpion venom."
sourcebook: "_Monster Core_, page 298."
```

```encounter-table
name: Scorpion Swarm
creatures:
  - 1: Scorpion Swarm
```
