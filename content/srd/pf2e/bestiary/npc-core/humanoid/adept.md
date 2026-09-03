---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adept"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Adept"
level: -1
source: "NPC Core"
aon_id: "creature-3532"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3532"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Adept"
level: "Creature -1"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Scribing Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +5"
abilityMods: [0, 2, 0, 3, 2, 1]
abilities_top:
  - name: "Items"
    desc: "journal, robes, scroll case, Writing Set"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +4; __Will__: +6"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ journal +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6 bludgeoning"
abilities_bot:
  - name: "Occult Spells Known"
    desc: "DC 15 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]]"
  - name: "Focused Thinker"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The adept concentrates to muster knowledge and wisdom. While focusing, they gain a +2 status bonus to checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]], but take a –2 penalty to Perception. They can Dismiss this focused state."
sourcebook: "_NPC Core_, page 96."
```

```encounter-table
name: Adept
creatures:
  - 1: Adept
```
