---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Guildmaster"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Guildmaster"
level: 8
source: "NPC Core"
aon_id: "creature-3414"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3414"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Guildmaster"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Architecture Lore +25, Athletics +13, Bureaucracy Lore +19, Crafting +25, Diplomacy +24, Intimidation +22, Society +21"
abilityMods: [3, 1, 2, 4, 2, 3]
abilities_top:
  - name: "Craft Specialist"
    desc: "For encounters involving matters of crafting or architecture, the guildmaster is a 12th-level challenge."
  - name: "Items"
    desc: "Artisan's Tools, construction schematics, guildmaster's uniform (functions as hide armor), _+1 striking light hammer_, tax ledgers"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +14; __Will__: +17"
hp: 135
health:
  - name: "HP"
    desc: "135"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _light hammer_ +16 (Agile, Magical) __Damage__ 2d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _light hammer_ +14 (Agile, Magical, thrown 20 feet) __Damage__ 2d6+5 bludgeoning"
abilities_bot:
  - name: "Call to Action"
    desc: "⬻ (Auditory, Concentrate, Emotion, Mental) The guildmaster gives a speech to inspire themself and all guild-member allies within 60 feet, granting a +1 status bonus to attack and damage rolls until the start of the guildmaster's next turn."
  - name: "Sworn Duty"
    desc: "While within the guild or presiding over guild business, the guildmaster gains a +2 circumstance bonus to weapon attack rolls and deals an additional 2d6 damage on a successful weapon attack."
sourcebook: "_NPC Core_, page 9."
```

```encounter-table
name: Guildmaster
creatures:
  - 1: Guildmaster
```
