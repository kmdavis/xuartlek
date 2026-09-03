---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Local Herbalist"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Local Herbalist"
level: 1
source: "NPC Core"
aon_id: "creature-3481"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3481"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Local Herbalist"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +4, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [3, 0, 1, 1, 4, 0]
abilities_top:
  - name: "Herbalism Specialist"
    desc: "For encounters involving collecting herbs or making medicine from them, the local herbalist is a 3rd-level challenge."
  - name: "Natural Medicine"
    desc: "The herbalist can use [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] instead of [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Wounds|Treat Wounds]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Administer First Aid|Administer First Aid]], and gains a +3 circumstance bonus to the check if they're in the wilderness with access to fresh herbal ingredients."
  - name: "Items"
    desc: "cooking pot, medicine bag (functions as a [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|healer's toolkit]]), Staff"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +8; __Ref__: +5; __Will__: +9"
hp: 24
health:
  - name: "HP"
    desc: "24"
abilities_mid:
  - name: "Saving Touch"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Trigger"
    desc: "An ally close enough for the herbalist to reach with a Stride is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The herbalist Strides until adjacent to the allye and [[srd/pf2e/compendium/rules-elements/actions/player-core#Administer First Aid|Administers First Aid]] to that ally."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ fungal spores +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fungus|Fungus]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], range increment 10 feet) __Damage__ 1d4 poison plus 1d4 persistent poison"
abilities_bot:
  - name: "Prompt Poultice"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The local herbalist quickly mixes together a potent healing salve with the most precious ingredients from their medicine bag. They create a temporary [[srd/pf2e/compendium/equipment/alchemical-items/elixir-of-life-true|lesser elixir of life]]. This elixir remains potent for 1 round before becoming sour and useless."
sourcebook: "_NPC Core_, page 60."
```

```encounter-table
name: Local Herbalist
creatures:
  - 1: Local Herbalist
```
