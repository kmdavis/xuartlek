---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Munsahir Gatecrasher"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Munsahir Gatecrasher"
level: 4
source: "Rage of Elements"
aon_id: "creature-2637"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2637"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Munsahir Gatecrasher"
level: "Creature 4"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Common, Pyric"
skills:
  - name: "Skills"
    desc: "Athletics +10, Crafting +12, Plane of Fire Lore +10"
abilityMods: [2, 0, 4, 4, 3, -1]
abilities_top:
  - name: "Items"
    desc: "gatecrasher armor"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +14; __Ref__: +6; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ fire; __Weaknesses__ cold 5"
abilities_mid:
  - name: "Heat of the Forge"
    desc: "(aura, fire) 10 feet. An munsahir's skin radiates heat like a forge's fire. A creature that starts its turn in the area must succeed at a DC 19 Fortitude save or become fatigued while it remains in the area. Creatures immune to environmental heat effects or with any fire resistance are immune."
  - name: "Self-Destruct"
    desc: "When the munsahir is reduced to 0 HP, their armor explodes at the start of their next turn, dealing 5d6 fire damage in a 10-foot radius (DC 19 basic Reflex)."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hammer gauntlet +12 (Free-Hand, Shove) __Damage__ 1d12+6 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ flame jet +12 (Brutal, Fire, range increment 20 feet) __Damage__ 2d6 fire plus 1d6 persistent fire"
abilities_bot:
  - name: "Blazing Rush"
    desc: "⬺ The gatecrasher Strides up to double their Speed in a straight line. They can pass through enemy spaces and make a hammer gauntlet Strike against each creature they move through. Blazing Rush can't be used again for 1d4 rounds."
  - name: "Burning Touch"
    desc: "(Fire, Primal) The munsahir gatecrasher's Strikes deal an extra 1d6 fire damage (included above). When the gatecrasher successfully performs a Grapple or Shove action, they also deal 1d6 fire damage to their target."
sourcebook: "_Rage of Elements_, page 131."
```

```encounter-table
name: Munsahir Gatecrasher
creatures:
  - 1: Munsahir Gatecrasher
```
