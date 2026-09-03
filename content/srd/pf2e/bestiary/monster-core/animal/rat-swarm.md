---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rat Swarm"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Rat Swarm"
level: 1
source: "Monster Core"
aon_id: "creature-3163"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3163"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Rat Swarm"
level: "Creature 1"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [-2, 3, 1, -4, 1, -3]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +7; __Will__: +4"
hp: 14
health:
  - name: "HP"
    desc: "14; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ physical 6 (except bludgeoning); __Weaknesses__ area damage 3, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 3"
speed: "30 feet, climb 10 feet"
abilities_bot:
  - name: "Putrid Plague"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) The [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] and [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] conditions from putrid plague can't end or be reduced until the disease is cured"
  - name: "Saving Throw"
    desc: "DC 14 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1d4 hours)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (1 day)"
  - name: "Stage 3"
    desc: "sickened 1 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 day)"
  - name: "Stage 4"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] (1 day)"
  - name: "Stage 5"
    desc: "dead"
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 1d6 piercing damage and must attempt a DC 17 basic Reflex save. A creature that fails its save is exposed to putrid plague. Rats and Disease Rats have a reputation of being vicious, aggressive animals that attack food stores in great numbers and spread disease. While rats are immune to the most severe effects of their own putrid plague, the disease makes them unpredictable and aggressive. Some populations of rats carry even more deadly diseases, such as bubonic plague."
sourcebook: "_Monster Core_, page 288."
```

```encounter-table
name: Rat Swarm
creatures:
  - 1: Rat Swarm
```
