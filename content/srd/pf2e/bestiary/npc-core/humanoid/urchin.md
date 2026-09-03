---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urchin"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Urchin"
level: -1
source: "NPC Core"
aon_id: "creature-3453"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3453"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Urchin"
level: "Creature -1"
size: "Small"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +3, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +3, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +7"
abilityMods: [-1, 3, 0, 1, 1, 2]
abilities_top:
  - name: "Items"
    desc: "shiv"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +7; __Will__: +3"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shiv +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4–1 piercing"
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4–1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4–1 bludgeoning"
abilities_bot:
  - name: "Collaborative Thievery"
    desc: "The urchin gains a +1 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Steal|Steal]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Palm an Object|Palm an Object]] while within 10 feet of an ally who has the pickpocket ability."
  - name: "Pickpocket"
    desc: "For an urchin, the DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Steal|Steal]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Palm an Object|Palm an Object]] isn't increased by 5 for an item that's closely guarded. They can Steal objects that would be extremely noticeable or time-consuming to remove (like worn shoes, armor, or actively wielded objects)."
sourcebook: "_NPC Core_, page 40."
```

```encounter-table
name: Urchin
creatures:
  - 1: Urchin
```
