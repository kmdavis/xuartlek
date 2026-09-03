---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boggard Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/boggard
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Boggard Scout"
level: 1
source: "Monster Core"
other_sources: "Pathfinder Game Night: Dawn of the Frogs (Deluxe Adventure)"
aon_id: "creature-2856"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2856"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Boggard Scout"
level: "Creature 1"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Boggard"
trait_03: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Boggard, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +8, Stealth +7"
abilityMods: [3, 2, 4, -1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Morningstar, Sling (10 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +5; __Will__: +7"
hp: 24
health:
  - name: "HP"
    desc: "24"
speed: "20 feet, swim 25 feet; swamp passage"
attacks:
  - name: "Melee"
    desc: "⬻ morningstar +8 (versatile P) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ tongue +8 (reach 10 feet) __Damage__ tongue grab"
  - name: "Ranged"
    desc: "⬻ sling +7 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Swamp Passage"
    desc: "A boggard scout ignores difficult terrain caused by swamp terrain features."
  - name: "Terrifying Croak"
    desc: "⬻ (Auditory, Emotion, Fear, Mental) The boggard scout unleashes a terrifying croak. Any non-boggard within 30 feet becomes frightened 1 unless they succeed at a DC 17 Will save; those who critically succeed are temporarily immune for 1 minute."
  - name: "Tongue Grab"
    desc: "If the boggard scout hits a creature with their tongue, that creature becomes grabbed by the boggard. Unlike with a normal Grab, the creature isn't immobilized, but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 13 and dealing at least 2 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
sourcebook: "_Monster Core_, page 44."
```

```encounter-table
name: Boggard Scout
creatures:
  - 1: Boggard Scout
```
