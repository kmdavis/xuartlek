---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Strix Aerialist"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/strix
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Strix Aerialist"
level: 9
source: "Monster Core 2"
aon_id: "creature-4568"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4568"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Strix Aerialist"
level: "Creature 9"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Strix"
trait_03: "Uncommon"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Strix"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +20, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +20, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +18"
abilityMods: [3, 5, 2, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]]_ (2), _[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+1]] [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +18; __Ref__: +21; __Will__: +15"
hp: 120
health:
  - name: "HP"
    desc: "120"
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+7 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+7 piercing"
abilities_bot:
  - name: "Aerial Feint"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The aerialist chooses a creature within 20 feet and attempts an [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] check against the target's [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] DC. On a success, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the aerialist's Strikes for 1 round."
  - name: "Dive Bomb"
    desc: "⬺ The strix aerialist [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to double its fly Speed in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]], descending at least 10 feet, and then makes a melee Strike."
  - name: "Sneak Attack"
    desc: "The strix aerialist's Strikes deal an additional 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core 2_, page 307."
```

```encounter-table
name: Strix Aerialist
creatures:
  - 1: Strix Aerialist
```
