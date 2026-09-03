---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghost Commoner"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/ghost
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ghost Commoner"
level: 4
source: "Monster Core"
aon_id: "creature-3007"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3007"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ghost Commoner"
level: "Creature 4"
size: "Medium"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Dwelling Lore +10, Stealth +12"
abilityMods: [-5, 3, 0, 0, 2, 2]
abilities_top:
  - name: "Site Bound"
    desc: ""
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +11; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30 (rejuvenation, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all damage 5 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical)"
abilities_mid:
  - name: "Rejuvenation"
    desc: "(divine) Setting right the injustice that led to the commoner's death allows it to move on to the afterlife."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ghostly hand +13 (Agile, Finesse, Magical) __Damage__ 2d6+2 void"
abilities_bot:
  - name: "Frightful Moan"
    desc: "⬻ (Auditory, Divine, Emotion, Fear, Mental) DC 21 The ghost laments its fate, forcing each living creature within 30 feet to attempt a Will save. On a failure, a creature becomes frightened 2 (or frightened 3 on a critical failure). On a success, a creature is temporarily immune to this ghost's frightful moan for 1 minute"
sourcebook: "_Monster Core_, page 161."
```

```encounter-table
name: Ghost Commoner
creatures:
  - 1: Ghost Commoner
```
