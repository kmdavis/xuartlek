---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hexmoth"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Hexmoth"
level: 8
source: "Howl of the Wild"
aon_id: "creature-3290"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3290"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Hexmoth"
level: "Creature 8"
size: "Small"
trait_01: "Animal"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; arcanosense (precise) 120 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Arcana +18, Stealth +14"
abilityMods: [3, 6, 3, -4, 1, 2]
abilities_top:
  - name: "Arcanosense"
    desc: "A hexmoth can sense sources of magic at the listed range as though it has a 4th-rank _detect magic_ constant innate spell."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +16; __Will__: +11"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ advanced arcanovore"
abilities_mid:
  - name: "Advanced Arcanovore"
    desc: "A hexmoth has resistance 10 against all damage caused by spells. It's immune to one type of energy it consumed most as a hexworm, typically acid, cold, electricity, fire, or sonic."
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ proboscis +13 __Damage__ 2d10+9 piercing plus Arcane Consumption"
  - name: "Ranged"
    desc: "⬻ hexbolt +13 (range 30 feet) __Damage__ 2d8+6 of the energy damage the hexmoth is immune to"
abilities_bot:
  - name: "Arcane Consumption"
    desc: "⬻ The hexmoth attempts to consume the magic of an adjacent magical effect or unattended magic item. It attempts a counteract check against the target with a +17 modifier. On a success, the magical effect ends. A magic item instead becomes a mundane item for 1 round. The hexmoth gains 2d8 Hit Points."
  - name: "Arcanotaxis"
    desc: "⭓"
  - name: "Requirements"
    desc: "The hexmoth has detected a source of magic with its arcanosense"
  - name: "Trigger"
    desc: "The hexmoth's turn begins"
  - name: "Effect"
    desc: "The hexmoth Strides or Flies up to its Speed toward the nearest source of magic it can detect."
  - name: "Hexdust Wind"
    desc: "⬺ With a few fierce wingbeats, the hexmoth expels magical scale dust in a 30-foot cone. This deals 10d6 damage of the type to which the hexmoth is immune (DC 23 basic Fortitude save). It can't use Hexdust Wind again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 159."
```

```encounter-table
name: Hexmoth
creatures:
  - 1: Hexmoth
```
