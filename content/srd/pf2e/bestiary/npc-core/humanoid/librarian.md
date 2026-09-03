---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Librarian"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Librarian"
level: -1
source: "NPC Core"
aon_id: "creature-3587"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3587"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Librarian"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]]; up to 4 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Academia Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Library Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +8, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +8"
abilityMods: [0, 1, 0, 3, 2, 1]
abilities_top:
  - name: "Research Specialist"
    desc: "A librarian is a 3rd-level challenge for encounters involving research."
  - name: "Methodical Research"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]]) When [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Searching]] through stacks of books, a librarian can find the answer to almost any question. This allows the librarian to use [[srd/pf2e/compendium/rules-elements/skills/lore|Library Lore]] in place of other lore skills, given enough time. The GM determines the DC of the check and the amount of time it takes (typically, a librarian can attempt three or four checks during 1 day of downtime)."
  - name: "Items"
    desc: "books, Dagger, Writing Set"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +2; __Ref__: +3; __Will__: +7"
hp: 6
health:
  - name: "HP"
    desc: "6"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ book +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ book +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4 bludgeoning"
sourcebook: "_NPC Core_, page 138."
```

```encounter-table
name: Librarian
creatures:
  - 1: Librarian
```
