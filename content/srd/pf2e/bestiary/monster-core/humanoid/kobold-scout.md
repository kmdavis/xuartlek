---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Scout"
level: 1
source: "Monster Core"
aon_id: "creature-3073"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3073"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kobold Scout"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Crafting +3, Nature +6, Stealth +7, Survival +6"
abilityMods: [0, 4, 1, 0, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Leather Armor, Shortsword"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +6 +1 circumstance to all defenses vs. traps"
hp: 16
health:
  - name: "HP"
    desc: "16"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +9 (Agile, Finesse, versatile S) __Damage__ 1d6 piercing"
  - name: "Ranged"
    desc: "⬻ crossbow +9 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing"
abilities_bot:
  - name: "Construct Trap"
    desc: "⬽ (Manipulate) The kobold scout creates a rudimentary trap on any square adjacent to it. This must be on a surface, such as a floor, wall, or ceiling. The trap activates the next time a creature moves adjacent to it. The creature takes 1d6 piercing damage and 1 persistent bleed damage with a DC 16 basic Reflex save. The trap is destroyed when activated or after 1 hour, whichever comes first. The scout typically carries enough raw materials to make one trap."
  - name: "Scamper"
    desc: "⬻"
  - name: "Requirements"
    desc: "The kobold scout is adjacent to at least one enemy"
  - name: "Effect"
    desc: "The kobold scout Strides up to their Speed plus 5 feet and gains a +2 circumstance bonus to AC against reactions triggered by this movement. They must end this movement in a space that's not adjacent to any enemy."
  - name: "Sneak Attack"
    desc: "The kobold scout deals an extra 1d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core_, page 210."
```

```encounter-table
name: Kobold Scout
creatures:
  - 1: Kobold Scout
```
