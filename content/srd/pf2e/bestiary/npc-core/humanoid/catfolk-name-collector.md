---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Catfolk Name Collector"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/catfolk
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Catfolk Name Collector"
level: 6
source: "NPC Core"
aon_id: "creature-3624"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3624"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Catfolk Name Collector"
level: "Creature 6"
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision, spiritsense (imprecise) 30 feet"
languages: "Amurrun, Common"
skills:
  - name: "Skills"
    desc: "Catfolk Lore +15, Occultism +12, Performance +14, Society +12"
abilityMods: [0, 4, 1, 2, 1, 4]
abilities_top:
  - name: "Spiritsense"
    desc: "The name collector senses spirits, embodied or not (including living creatures, most non-mindless undead, and haunts)."
  - name: "Items"
    desc: "Leather Armor, _+1 sickle_, _scroll of command_, _scroll of protection_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +14; __Will__: +13"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Name the Worthy"
    desc: "⬲ (auditory, linguistic, mental)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "Another creature critically succeeds at a check"
  - name: "Effect"
    desc: "The name collector honors the achievement with a new name. The creature gets a +1 status bonus on the same check until their next daily preparations. They become temporarily immune for 1 month."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _sickle_ +15 (Agile, Finesse, Magical, Trip) __Damage__ 1d4+9 slashing"
  - name: "Melee"
    desc: "⬻ claw +14 (Agile, Finesse, Unarmed) __Damage__ 1d4+9 slashing"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ Daze, Detect Magic, Read Aura - __1st__ Bless, Spirit Link, Sure Strike - __2nd__ Laughing Fit, See the Unseen, Soothe - __3rd__ Heroism, Illusory Creature"
sourcebook: "_NPC Core_, page 172."
```

```encounter-table
name: Catfolk Name Collector
creatures:
  - 1: Catfolk Name Collector
```
