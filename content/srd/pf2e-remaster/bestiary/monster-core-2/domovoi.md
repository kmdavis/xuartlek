---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Domovoi"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/tiny
statblock: inline
name: "Domovoi"
level: 2
source: "Monster Core 2"
aon_id: "creature-4441"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4441"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Domovoi"
level: "Creature 2"
size: "Tiny"
trait_01: "Fey"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; tremorsense (imprecise) within their entire bound home"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Crafting +9, Household Lore +10, Stealth +7"
abilityMods: [1, 3, 1, 3, 5, 1]
abilities_top:
  - name: "Master of the Home"
    desc: "A home with a friendly domovoi is blessed, as the domovoi cooks, cleans, fetches water, and does a hundred other small tasks. A home so blessed never encounters random accidents such as fires, and any checks to Craft, Earn Income, Repair, or Subsist in the home receive a +2 circumstance bonus. If the domovoi is unfriendly, such checks take a –2 circumstance penalty instead, as the domovoi hides things, makes noise when people try to sleep, tangles weaving, and otherwise makes life a misery. A domovoi must spend a week in a place before these benefits occur."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9; __Will__: +11"
hp: 35
health:
  - name: "HP"
    desc: "35; __Weaknesses__ cold iron 4"
abilities_mid:
  - name: "Shy"
    desc: "A domovoi is naturally invisible while within sight of their bound home. The domovoi can become visible, or even selectively visible— allowing some people to see them."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ broom +7 __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ enraged home +9 (Primal, range increment 30 feet) __Damage__ 1d8+4 bludgeoning, piercing, or slashing (depending on object)"
abilities_bot:
  - name: "Home Guardian"
    desc: "By commanding their home to attack, the domovoi can Disarm, Grapple, Reposition, Shove, or Trip with their enraged home Strike. The domovoi uses their Household Lore instead of Athletics skill for these checks."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18 - __Cantrips (1st)__ Prestidigitation, Telekinetic Hand, Telekinetic Projectile - __1st__ Mending (at will)"
sourcebook: "_Monster Core 2_, page 194."
```

```encounter-table
name: Domovoi
creatures:
  - 1: Domovoi
```
