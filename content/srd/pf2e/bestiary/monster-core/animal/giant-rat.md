---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Rat"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Giant Rat"
level: -1
source: "Monster Core"
aon_id: "creature-3162"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3162"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Rat"
level: "Creature -1"
size: "Small"
trait_01: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +2, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [1, 3, 2, -4, 1, -3]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +7; __Will__: +3"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "30 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 piercing plus putrid plague"
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
sourcebook: "_Monster Core_, page 288."
```

```encounter-table
name: Giant Rat
creatures:
  - 1: Giant Rat
```
