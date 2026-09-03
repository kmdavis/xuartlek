---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dancer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dancer"
level: 1
source: "NPC Core"
aon_id: "creature-3569"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3569"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dancer"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Theater Lore]] +5"
abilityMods: [1, 3, 1, 0, 0, 4]
abilities_top:
  - name: "Dance Specialist"
    desc: "For encounters involving contests of dancing, the dancer is a 5thlevel challenge."
  - name: "Items"
    desc: "Dagger (3), jewelry and clothes (worth 10 gp)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +8; __Will__: +3"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ foot +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Fascinating Dance"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dancer Strides up to their Speed. Once during this movement, when the dancer is adjacent to a creature, the dancer can attempt to mesmerize that creature, who attempts a DC 17 Will save. On a failure, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the dancer until the end of its next turn."
sourcebook: "_NPC Core_, page 124."
```

```encounter-table
name: Dancer
creatures:
  - 1: Dancer
```
