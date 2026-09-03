---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elf Ranger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Elf Ranger"
level: 1
source: "Monster Core"
aon_id: "creature-2995"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2995"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elf Ranger"
level: "Creature 1"
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [1, 4, 1, 3, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Dagger, Shortbow (20 arrows)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 17
health:
  - name: "HP"
    desc: "17"
speed: "30 feet; unimpeded journey"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ shortbow +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], range increment 60 feet) __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Double Shot"
    desc: "⬻ The elf ranger makes two shortbow Strikes targeting two different creatures within the shortbow's first range increment. Both Strikes uses the elf's current multiple attack penalty, but each strike takes a –2 penalty."
  - name: "Elf Step"
    desc: "⬻ The elf Steps twice."
  - name: "Unimpeded Journey"
    desc: "The elf ranger ignores difficult terrain."
sourcebook: "_Monster Core_, page 151."
```

```encounter-table
name: Elf Ranger
creatures:
  - 1: Elf Ranger
```
