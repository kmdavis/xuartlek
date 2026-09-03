---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hexworm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Hexworm"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3289"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3289"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Hexworm"
level: "Creature 4"
size: "Tiny"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; arcanosense (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [2, 4, 3, -5, 1, 0]
abilities_top:
  - name: "Arcanosense"
    desc: "A hexworm can sense sources of magic at the listed range as though it has a 4th-rank [[srd/pf2e/compendium/spells/cantrips/detect-magic|_detect magic_]] constant innate spell."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +14; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45; __Resistances__ arcanovore"
abilities_mid:
  - name: "Arcanovore"
    desc: "A hexworm has resistance 5 against all damage caused by spells."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +8 __Damage__ 2d6+2 piercing plus Arcane Consumption"
abilities_bot:
  - name: "Arcane Consumption"
    desc: "⬻ The hexworm attempts to consume the magic of an adjacent magical effect or unattended magic item. It attempts a counteract check against the target with a +11 modifier. On a success, the magical effect ends. A magic item instead becomes a mundane item for 1 round. The hexworm gains 2d8 Hit Points."
  - name: "Arcanotaxis"
    desc: "⭓"
  - name: "Requirements"
    desc: "The hexworm has detected a source of magic with its arcanosense"
  - name: "Trigger"
    desc: "The hexworm's turn begins"
  - name: "Effect"
    desc: "The hexworm Strides up to its Speed toward the nearest source of magic it can detect."
sourcebook: "_Howl of the Wild_, page 159."
```

```encounter-table
name: Hexworm
creatures:
  - 1: Hexworm
```
