---
noteType: pf2eMonster
aliases: "Bosun"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bosun"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3600"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bosun"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/Lore|Sailing Lore]] +11"
abilityMods: [2, 4, 1, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Dagger, naval pike (functions as a [[srd/pf2e/compendium/equipment/weapons/spear/Spear|spear]])"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +11; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ naval pike +11 __Damage__ 1d6+5 piercing"
  - name: "Ranged"
    desc: "⬻ naval pike +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d6+5 piercing"
abilities_bot:
  - name: "Bosun's Command"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The bosun orders an ally to attack or to get in position. Until the end of the ally's next turn, they gain the bosun's choice of a +2 status bonus to attack rolls or a +10-foot status bonus to their Speeds."
  - name: "Pike and Strike"
    desc: "⬺ The bosun makes a melee Strike with their naval pike. If this Strike hits, the bosun can either move the target 5 feet within the pike's reach or make a fist Strike against the target without increasing their multiple attack penalty until after the fist Strike. Shipboard Spells A bosun with magical training can exchange Pike and Strike for the following spells."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 18, attack +10; __1st__ [[srd/pf2e/compendium/spells/rank-1/Ant Haul|_ant haul_]], [[srd/pf2e/compendium/spells/rank-1/Gentle Landing|_gentle landing_]], [[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|_hydraulic push_]]; __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Electric Arc|_electric arc_]], [[srd/pf2e/compendium/spells/cantrips/Guidance|_guidance_]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|_know the way_]], [[srd/pf2e/compendium/spells/cantrips/Light|_light_]], [[srd/pf2e/compendium/spells/cantrips/Sigil|_sigil_]]"
sourcebook: "_NPC Core_, page 147."
```

```encounter-table
name: Bosun
creatures:
  - 1: Bosun
```
