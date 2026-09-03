---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Demonbane Warrior"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Demonbane Warrior"
level: 5
source: "NPC Core"
aon_id: "creature-3632"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3632"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Demonbane Warrior"
level: "Creature 5"
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision"
languages: "Chthonian, Common, Elven"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Demon Lore +12, Religion +11, Stealth +10, Survival +11"
abilityMods: [3, 4, 2, 1, 2, 0]
abilities_top:
  - name: "Sin Sense"
    desc: "A demonbane warrior automatically learns all weaknesses of a demon they've identified by Recalling Knowledge."
  - name: "Items"
    desc: "Chain Shirt, Composite Shortbow (20 arrows), cold iron elven branched spear"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +13; __Will__: +11"
hp: 76
health:
  - name: "HP"
    desc: "76"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ cold iron elven branched spear +15 (deadly d8, Finesse, Reach) __Damage__ 1d6+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +15 (deadly d10, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+7 piercing"
abilities_bot:
  - name: "Demonbane"
    desc: "A demonbane warrior gains a +1 circumstance bonus to damage rolls against demons. If their actions force a demon to take damage from its sin vulnerability, increase the damage from the vulnerability by 2."
  - name: "Imbue Righteousness"
    desc: "⬻ (Divine, Holy) The warrior imbues a weapon they wield with holy energy. Until the start of their next turn, their Strikes with that weapon gain the holy trait and deal an additional 1d6 spirit damage to unholy creatures."
sourcebook: "_NPC Core_, page 179."
```

```encounter-table
name: Demonbane Warrior
creatures:
  - 1: Demonbane Warrior
```
