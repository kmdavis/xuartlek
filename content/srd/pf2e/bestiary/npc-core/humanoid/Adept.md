---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3532"
socialImage: og-image.png
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
    desc: "+4"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +5, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +5, [[srd/pf2e/compendium/rules-elements/skills/Lore|Scribing Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +5"
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
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ journal +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d6 bludgeoning"
abilities_bot:
  - name: "Occult Spells Known"
    desc: "DC 15 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]]"
  - name: "Focused Thinker"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The adept concentrates to muster knowledge and wisdom. While focusing, they gain a +2 status bonus to checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]], but take a –2 penalty to Perception. They can Dismiss this focused state."
sourcebook: "_NPC Core_, page 96."
```

```encounter-table
name: Adept
creatures:
  - 1: Adept
```
