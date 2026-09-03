---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Warrior"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Warrior"
level: -1
source: "Monster Core"
aon_id: "creature-3072"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3072"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kobold Warrior"
level: "Creature -1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
languages: "Common, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Crafting +2, Stealth +5"
abilityMods: [1, 3, -1, 0, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Sling (20 bullets), Spear"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +7; __Will__: +3"
hp: 7
health:
  - name: "HP"
    desc: "7"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spear +3 __Damage__ 1d6+1 piercing"
  - name: "Ranged"
    desc: "⬻ sling +5 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spear +5 (thrown 20 feet) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Scamper"
    desc: "⬻"
  - name: "Requirements"
    desc: "The kobold warrior is adjacent to at least one enemy"
  - name: "Effect"
    desc: "The kobold warrior Strides up to their Speed plus 5 feet and gains a +2 circumstance bonus to AC against reactions triggered by this movement. They must end this movement in a space that's not adjacent to any enemy."
  - name: "Sneak Attack"
    desc: "The kobold warrior deals an extra 1d4 precision damage to off-guard creatures."
sourcebook: "_Monster Core_, page 210."
```

```encounter-table
name: Kobold Warrior
creatures:
  - 1: Kobold Warrior
```
