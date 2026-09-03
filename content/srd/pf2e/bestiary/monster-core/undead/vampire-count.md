---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vampire Count"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/vampire
  - pf2e/creature/trait/medium
statblock: inline
name: "Vampire Count"
level: 6
source: "Monster Core"
aon_id: "creature-3225"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3225"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vampire Count"
level: "Creature 6"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Vampire"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "Common, Necril; plus one regional language"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +13, Deception +14, Diplomacy +14, Intimidation +16, Society +14, Stealth +13"
abilityMods: [5, 3, 2, 2, 4, 4]
abilities_top:
  - name: "Children of the Night"
    desc: "(divine, mental)"
  - name: "Items"
    desc: "Leather Armor, _+1 rapier_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +14; __Will__: +17"
hp: 65
health:
  - name: "HP"
    desc: "65 (coffin restoration, fast healing 7, void healing); __Immunities__ death effects, disease, paralyzed, poison, sleep; __Resistances__ physical 7 (except magical silver)"
abilities_mid:
  - name: "Vampire Vulnerabilities"
    desc: ""
  - name: "Mist Escape"
    desc: "⭓"
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 (deadly d8, disarm +1) __Damage__ 1d6+11 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 (Agile) __Damage__ 1d8+8 slashing plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) Giant bat with fangs +15 for 1d8+9 piercing (page 358)."
  - name: "Create Servitor"
    desc: "(Divine, Downtime)"
  - name: "Dominate"
    desc: "⬺ (Divine, Incapacitation, Mental, Visual) DC 22"
  - name: "Drink Blood"
    desc: "⬻ (Divine) When Drinking Blood, the vampire count regains 10 HP."
  - name: "Turn to Mist"
    desc: "⬻ (Air, Concentrate, Divine, Polymorph)"
sourcebook: "_Monster Core_, page 336."
```

```encounter-table
name: Vampire Count
creatures:
  - 1: Vampire Count
```
