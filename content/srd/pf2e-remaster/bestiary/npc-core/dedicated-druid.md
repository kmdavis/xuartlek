---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dedicated Druid"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dedicated Druid"
level: 7
source: "NPC Core"
aon_id: "creature-3583"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3583"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dedicated Druid"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; lifesense (imprecise) 30 feet"
languages: "Common, Wildsong"
skills:
  - name: "Skills"
    desc: "Diplomacy +14, Intimidation +12, Nature +17, Religion +15, Stealth +13, Survival +17"
abilityMods: [4, 2, 1, 1, 4, 1]
abilities_top:
  - name: "Plant Empathy"
    desc: "The dedicated druid can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
  - name: "Items"
    desc: "Hide Armor, _scroll of revealing light_ (2), _+1 spear_, Wooden Shield (Hardness 3, HP 12, BT 6)"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +13; __Will__: +15"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +16 (Magical) __Damage__ 1d6+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _spear_ +14 (Magical, thrown 20 feet) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Nature's Patient Healing"
    desc: "⬽ (Primal)"
  - name: "Requirement"
    desc: "The dedicated druid is in a natural environment"
  - name: "Effect"
    desc: "The dedicated druid camouflages themself to blend in with the surrounding area, sprouting leaves or covering themself with scree. They gain concealment until the end of their next turn, they can Hide with a +4 circumstance bonus, and they recover 4d8 Hit Points. If the druid moves or otherwise leaves their space, these benefits end."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ Electric Arc, Ignition, Know the Way, Tangle Vine, Vitality Lash - __1st__ Air Bubble, Gentle Landing, Gust of Wind - __2nd__ Entangling Flora, Mist, One with Plants - __3rd__ Earthbind, Fireball, Wall of Thorns - __4th__ Fly, Lightning Bolt __Druid Order Spells 1 Focus Point,__ DC 25 - __4th__ Cornucopia"
sourcebook: "_NPC Core_, page 134."
```

```encounter-table
name: Dedicated Druid
creatures:
  - 1: Dedicated Druid
```
