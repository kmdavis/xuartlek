---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnome Philomath"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Gnome Philomath"
level: -1
source: "NPC Core"
aon_id: "creature-3635"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3635"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gnome Philomath"
level: "Creature -1"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision"
languages: "Common, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Athletics +3, Crafting +1, History Lore +5, One Additional Lore +5, Society +4, Thievery +3"
abilityMods: [0, 1, 0, 3, 2, 1]
abilities_top:
  - name: "Local Records Specialist"
    desc: "For encounters involving local records and histories, the gnome philomath is a 5th-level challenge."
  - name: "Helpful Hoard"
    desc: "Gnome philomaths can quickly find almost any document in their vast collection. They gain a +8 circumstance bonus to skill checks involving local records and histories."
  - name: "Items"
    desc: "Staff, Writing Set"
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +2; __Ref__: +5; __Will__: +8"
hp: 7
health:
  - name: "HP"
    desc: "7"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +4 (two-hand d8) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Innate Primal Spells"
    desc: "DC 13 - __Cantrips (1st)__ Detect Magic, Light, Prestidigitation __Mind if I Borrow That?__ ⬻ The gnome philomath designates a single item within their sight as an item of interest to their studies. They then gain a +2 circumstance bonus to Disarm or Steal that item. They can only designate one item at a time in this way. If they use Mind if I Borrow That? to designate a new item of interest, they lose the bonus with the previous item."
sourcebook: "_NPC Core_, page 182."
```

```encounter-table
name: Gnome Philomath
creatures:
  - 1: Gnome Philomath
```
