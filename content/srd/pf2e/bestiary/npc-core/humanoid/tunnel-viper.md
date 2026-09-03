---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tunnel Viper"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/ratfolk
  - pf2e/creature/trait/small
statblock: inline
name: "Tunnel Viper"
level: 1
source: "NPC Core"
aon_id: "creature-3667"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3667"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tunnel Viper"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/languages#Ysoki|Ysoki]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +6"
abilityMods: [3, 3, 0, 1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/crossbow/arbalest|Arbalest]] (20 bolts), Caltrops (3), Ranseur, Scale Mail"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet; swarming, tunnel travel"
attacks:
  - name: "Melee"
    desc: "⬻ ranseur +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+3 piercing"
  - name: "Melee"
    desc: "⬻ jaws +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+3 piercing"
  - name: "Ranged"
    desc: "⬻ arbalest +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], range increment 110 feet, reload 1) __Damage__ 1d10 piercing"
abilities_bot:
  - name: "Running Reload"
    desc: "⬻ The tunnel viper Strides, Steps, or [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaks]], then Interacts to reload."
  - name: "Swarming"
    desc: "A tunnel viper can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
  - name: "Tunnel Fighter"
    desc: "The tunnel viper deals an additional 1d6 precision damage to creatures that are [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]] or in difficult terrain due to narrow spaces."
  - name: "Tunnel Travel"
    desc: "Narrow spaces aren't difficult terrain for the tunnel viper, and the viper can [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]] at 5 feet per round (or 10 feet on a critical success)."
sourcebook: "_NPC Core_, page 210."
```

```encounter-table
name: Tunnel Viper
creatures:
  - 1: Tunnel Viper
```
