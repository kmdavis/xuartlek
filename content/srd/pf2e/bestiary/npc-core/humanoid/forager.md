---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Forager"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Forager"
level: 1
source: "NPC Core"
aon_id: "creature-3467"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3467"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Forager"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (11 to notice flora and fauna)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Local Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +3, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [1, 3, 1, 0, 4, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]], if the forager rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and four additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Natural Specialist"
    desc: "For encounters involving [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] or [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]], the forager is a 3rd-level challenge."
  - name: "Items"
    desc: "Dagger, pouches, wicker baskets"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +8; __Will__: +8"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ fruit or vegetable +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d4+1 bludgeoning"
abilities_bot:
  - name: "Local Poison"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The forager coats their dagger in a diluted, locally sourced poison. Until the end of their turn, Strikes with their dagger deal an additional 2 persistent poison damage."
sourcebook: "_NPC Core_, page 52."
```

```encounter-table
name: Forager
creatures:
  - 1: Forager
```
