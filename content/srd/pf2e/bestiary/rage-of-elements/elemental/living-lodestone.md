---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Lodestone"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/small
statblock: inline
name: "Living Lodestone"
level: 6
source: "Rage of Elements"
aon_id: "creature-2649"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2649"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Living Lodestone"
level: "Creature 6"
size: "Small"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [5, 3, 4, 0, 4, 4]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +13; __Will__: +16"
hp: 95
health:
  - name: "HP"
    desc: "95; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 5"
abilities_mid:
  - name: "Magnetic Field"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/metal|metal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 60 feet. A living lodestone constantly emits a powerful magnetic field that is either positively or negatively aligned. Each creature within the aura that is wielding a metallic weapon, wearing metallic armor, or made partially or entirely out of metal is subject to an effect determined by the lodestone's current polarity."
  - name: "Negative"
    desc: "An affected creature is pushed 5 feet away from the lodestone at the start of each of its turns, and it treats each square in the aura as difficult terrain when moving closer to the lodestone. Unattended metal objects in the aura of 2 Bulk or less are pushed just outside the aura."
  - name: "Positive"
    desc: "An affected creature is pulled 5 feet toward the lodestone at the start of each of its turns, and it treats each square in the aura as difficult terrain when moving farther from the lodestone. Unattended metal objects in the aura of 2 Bulk or less are pulled adjacent to the lodestone."
  - name: "Electromagnetic Disruption"
    desc: "When living lodestone takes electricity damage, they automatically reverses polarity."
speed: "20 feet; hover"
attacks:
  - name: "Melee"
    desc: "⬻ jolt +15 __Damage__ 2d6+8 electricity"
  - name: "Ranged"
    desc: "⬻ hurled metal object +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], range increment 60 feet) __Damage__ 2d10+7 bludgeoning, piercing, or slashing (depending on object)"
abilities_bot:
  - name: "Hover"
    desc: "A living lodestone floats above the ground high enough to ignore all difficult terrain and greater difficult terrain on the ground."
  - name: "Magnetic Disarm"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The living lodestone attempts to Disarm a metal weapon from a creature within its magnetic field. On a critical success, the weapon is either pushed to just outside the aura if the polarity is negative or is pulled to the lodestone and sticks to it if the polarity is positive. An item stuck to the lodestone can be wrenched free with an Interact action."
  - name: "Reverse Polarity"
    desc: "⬺ The living lodestone switches the polarity of its magnetic field from positive to negative, or vice versa. Each creature affected by the lodestone's aura falls prone unless it succeeds at a DC 21 Reflex save. The lodestone can't Reverse Polarity again for 1d4 rounds. Lodestone Loot The cyclone of metallic objects constantly orbiting a living lodestone often contains items of value, ranging from simple coinage and bits of precious metal to long-lost weapons, jewelry, and sometimes even enchanted metal trinkets. The lodestone itself has no concept of the value of such things, and is just as likely to fling one of these valuable items at a foe as it is any other object."
sourcebook: "_Rage of Elements_, page 155."
```

```encounter-table
name: Living Lodestone
creatures:
  - 1: Living Lodestone
```
