---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Landslide"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Living Landslide"
level: 5
source: "Monster Core"
aon_id: "creature-2978"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2978"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Living Landslide"
level: "Creature 5"
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [5, -1, 4, -2, 1, -1]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the living landslide is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] and can't use reactions."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +8; __Will__: +10"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]] **Crumble ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "The living landslide takes damage from a hostile source while atop rock or earth**"
  - name: "Effect"
    desc: "The living landslide crumbles into the ground, [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrowing]]down 10 feet. This Burrowing does not trigger reactions. The living landslide can't Crumble again for 1d4 rounds."
speed: "25 feet, burrow 25 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+8 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "The elemental can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through any earthen matter, including rock. When it does so, the elemental moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Sliding Earth"
    desc: "⬺ The living landslide Strides up to twice its normal Speed in a straight line, then attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] a creature in its reach. If a creature falls prone from this Trip, it takes 1d4 bludgeoning damage for every 10 feet the living landslide moved."
sourcebook: "_Monster Core_, page 142."
```

```encounter-table
name: Living Landslide
creatures:
  - 1: Living Landslide
```
