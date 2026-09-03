---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Despot"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Despot"
level: 5
source: "NPC Core"
aon_id: "creature-3614"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3614"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Despot"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Common, Diabolic"
skills:
  - name: "Skills"
    desc: "Athletics +11, Deception +13, Diplomacy +11, Intimidation +13, Performance +13, Religion +11, Society +13, Warfare Lore +13"
abilityMods: [2, 2, 0, 4, 2, 4]
abilities_top:
  - name: "Persistent Lies"
    desc: "Any creature deceived by the despot's Deception skill believes the deception more readily on the next day. Any later Perception checks attempted against the despot's Deception DC take a –2 circumstance penalty, as do other creatures' attempts to convince the creature otherwise, such as through Diplomacy or further Deception."
  - name: "Items"
    desc: "lesser darkvision elixir, lesser healing potion (2), Spiked Gauntlet"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +9; __Will__: +13"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spiked gauntlet +11 (Agile, Free-Hand) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Sorcerer Bloodline Spells"
    desc: "DC 23, 1 Focus Point - __3rd__ Diabolic Edict"
  - name: "Sorcerous Potency"
    desc: "When the despot Casts a Spell from a spell slot that deals damage, they gain a status bonus to the spell's initial damage equal to the spell's rank."
  - name: "Tongue of Flame"
    desc: "When the despot casts _charm_, _diabolic edict_, _enthrall_, or _floating flame_, either a target takes 1 fire damage per spell rank, or the despot gains a +2 status bonus to Deception checks for 1 round."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 23, attack +14 - __Cantrips (3rd)__ Daze, Ignition, Message, Shield, Void Warp - __1st__ Bane, Command, Fear, Sanctuary (4 slots) - __2nd__ Blood Vendetta, Calm, Floating Flame, See the Unseen (4 slots) - __3rd__ Chilling Darkness, Enthrall, Harm (3 slots)"
sourcebook: "_NPC Core_, page 157."
```

```encounter-table
name: Despot
creatures:
  - 1: Despot
```
