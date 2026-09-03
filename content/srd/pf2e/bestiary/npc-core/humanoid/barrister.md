---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Barrister"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Barrister"
level: -1
source: "NPC Core"
aon_id: "creature-3546"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3546"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Barrister"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9"
abilityMods: [0, 1, 1, 3, 2, 4]
abilities_top:
  - name: "Legal Specialist"
    desc: "In a court case or other legal proceeding, the barrister is a 4thlevel challenge."
  - name: "Sway the Judge and Jury"
    desc: "A barrister gains a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] something of the deciding members within a courtroom. If the barrister successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Perform|Performs]] against a DC of 20 during the 20 minutes prior to the check, they increase the circumstance bonus to +4."
  - name: "Items"
    desc: "court garb (functions as [[srd/pf2e/compendium/equipment/adventuring-gear/clothing-desert|fine clothing]]), law book (functions as [[srd/pf2e/compendium/equipment/adventuring-gear/scholarly-journal-compendium|scholarly journal]]), Writing Set"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +3; __Ref__: +3; __Will__: +12"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Cite Precedent"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]]) The barrister uses existing case law to undermine their opposition. If they succeed at a DC 20 [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] check, they impose a –2 circumstance penalty on the next [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] check an opponent attempts in a legal argument. Any further attempts to Cite Precedent fail until a new topic with different precedents is being argued."
sourcebook: "_NPC Core_, page 108."
```

```encounter-table
name: Barrister
creatures:
  - 1: Barrister
```
