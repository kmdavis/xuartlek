---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ship Captain"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Ship Captain"
level: 6
source: "NPC Core"
aon_id: "creature-3604"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3604"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Ship Captain"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +12, Diplomacy +11, Intimidation +13, Sailing Lore +17, Survival +10"
abilityMods: [4, 2, 0, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, Hand Crossbow (10 bolts), Leather Armor, Main-gauche, _+1 rapier_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +12; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Bravery"
    desc: "When the ship captain rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, anytime they gain the frightened condition, reduce its value by 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 (deadly d8, Disarm, Magical) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ main-gauche +16 (Agile, Disarm, Parry, versatile S) __Damage__ 1d4+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +14 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Dual Disarm"
    desc: "⬺ The captain makes two Strikes, one with their rapier and one with their main-gauche (in either order). If both Strikes hit, the ship captain can attempt to Disarm the target. Their multiple attack penalty increases only after all the attacks are made. __No Quarter!__ ⬻ (Auditory, Concentrate, Emotion, Linguistic, Mental) The captain orders their shipmates to fight without mercy. All allied creatures of equal or lower level within 20 feet of the ship captain gain a +1 status bonus to attack rolls and damage rolls until the end of the ship captain's next turn. Shipboard Spells The ship captain can gain the following spells in place of Dual Disarm."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +16; __2nd__ _summon elemental_, _water breathing_, _water walk_; __1st__ _gentle landing_, _gust of wind_ (×2); __Cantrips (2nd)__ _electric arc_, _guidance_, _know the way_, _light_, _sigil_"
sourcebook: "_NPC Core_, page 149."
```

```encounter-table
name: Ship Captain
creatures:
  - 1: Ship Captain
```
