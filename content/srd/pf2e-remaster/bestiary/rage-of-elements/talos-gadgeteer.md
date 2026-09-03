---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Talos Gadgeteer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/talos
  - pf2e/creature/trait/medium
statblock: inline
name: "Talos Gadgeteer"
level: 1
source: "Rage of Elements"
aon_id: "creature-2658"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2658"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Talos Gadgeteer"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Talos"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "Common, Talican"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Crafting +6, Society +6, Thievery +6"
abilityMods: [1, 3, 1, 3, 0, 1]
abilities_top:
  - name: "Gadgets"
    desc: "A talos gadgeteer carries the following temporary gadgets, which have no value if sold and last for 24 hours or until the next time the gadgeteer makes their daily preparations: lesser ablative armor plating (1), lesser blast boots (1), lesser explosive mine (3)."
  - name: "Items"
    desc: "artisan's toolkit, formula book, Leather Armor, light hammer (3)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +6; __Will__: +5"
hp: 17
health:
  - name: "HP"
    desc: "17 (plus 5 temporary HP (from ablative armor plating)); __Resistances__ electricity 1"
abilities_mid:
  - name: "Reflective Defense"
    desc: "⬲ (light)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Trigger"
    desc: "A creature within 30 feet targets the talos gadgeteer, and they can see the attacker"
  - name: "Requirements"
    desc: "The talos is in dim or bright light"
  - name: "Effect"
    desc: "The talos gadgeteer reflects light off their metallic skin and into the enemy's eyes; it must succeed at a DC 14 Reflex save or be dazzled until the end of the talos's next turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Finesse, versatile S) __Damage__ 1d6+1 bludgeoning"
  - name: "Melee"
    desc: "⬻ light hammer +6 (Agile) __Damage__ 1d6+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ light hammer +8 (Agile, thrown 20 feet) __Damage__ 1d6+1 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 14 - __Cantrips (1st)__ Detect Metal Traveling Tinkerers While there are no known permanent talos settlements in the Universe, there is a small nomadic community known as the Tinkerers' Caravan. Originally founded in Vudra and inspired by similar clans of janns and sulis, the caravan now travels throughout most of the eastern world, offering all taloses who wish to travel with them a sense of community and belonging that they might not find anywhere else."
sourcebook: "_Rage of Elements_, page 163."
```

```encounter-table
name: Talos Gadgeteer
creatures:
  - 1: Talos Gadgeteer
```
