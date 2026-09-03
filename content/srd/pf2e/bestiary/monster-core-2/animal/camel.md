---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Camel"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Camel"
level: 1
source: "Monster Core 2"
aon_id: "creature-4291"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4291"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Camel"
level: "Creature 1"
size: "Large"
trait_01: "Animal"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [4, 3, 4, -4, 1, -1]
abilities_top:
  - name: "Desert-Adapted"
    desc: "A camel is well-adapted to heat and deserts. If allowed to drink and eat its fill (roughly 40 gallons), it can [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]] for 2 weeks without needing to attempt [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks, and it treats environmental [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Temperature|heat effects]] as if they were one step less severe."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +9; __Ref__: +8; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+4 piercing"
  - name: "Ranged"
    desc: "⬻ spit +6 __Damage__ camel spit"
abilities_bot:
  - name: "Camel Spit"
    desc: "To drive away enemies, the camel spits the partially digested contents of its stomach at a creature within 10 feet. On a hit, the target is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round and must succeed at a DC 17 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1. The camel can't use its camel spit Strike again for 1d4 rounds."
  - name: "Sand Stride"
    desc: "⬺ The camel [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] twice. It has a +5-foot circumstance bonus to its Speed during these Strides, ignoring difficult terrain caused by rubble, sand, and uneven ground made of earth and stone. Camel Cousins Rumors in the high desert tell of an ancient species related to both camels and llamas that still lives in sheltered mountain valleys and along hidden rivers: the camelops. Larger and stronger than domesticated camels, camelops remain wild creatures. No living examples exist in captivity, though fables of their luxurious coats and indomitable endurance lead some riders to seek them out regardless."
sourcebook: "_Monster Core 2_, page 67."
```

```encounter-table
name: Camel
creatures:
  - 1: Camel
```
