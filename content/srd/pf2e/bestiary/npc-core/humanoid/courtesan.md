---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Courtesan"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Courtesan"
level: 2
source: "NPC Core"
aon_id: "creature-3417"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3417"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Courtesan"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (13 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; plus two additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Art Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +10"
abilityMods: [-1, 3, 0, 2, 3, 4]
abilities_top:
  - name: "Group Impression"
    desc: "When the courtesan [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Makes an Impression]], they can compare their [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] check result to the Will DCs of up to four targets instead of one."
  - name: "Social Specialist"
    desc: "When entertaining or socializing, the courtesan is a 5th-level challenge."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/clothing-desert|fine clothing]], [[srd/pf2e/compendium/equipment/adventuring-gear/musical-instrument-virtuoso-heavy|flute]], jewelry, [[srd/pf2e/compendium/equipment/assistive-items/cane|sword cane]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +7; __Will__: +11"
hp: 25
health:
  - name: "HP"
    desc: "25"
abilities_mid:
  - name: "Beguiling Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 10 feet. Creatures in the area that can observe the courtesan take a –2 status penalty on their Will DC against the courtesan's attempts to make a [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] of them."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sword cane +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Cutting Remarks"
    desc: "⬻ The courtesan levies insults or backhanded compliments, attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] a creature using their [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] modifier instead of [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]]."
  - name: "Words of Encouragement"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The courtesan praises the performance of one ally who can hear them. The targeted ally ignores any circumstance and status penalties they have until the start of the courtesan's next turn. The target then becomes temporarily immune to this ability for 10 minutes. Elegant Establishments Courtesans thrive both in business and status by catering to the elite upper class through creating private, exclusive spaces such as theaters, art galleries, tea houses, and boutiques. This allows both the courtesans and the upper class to strengthen alliances and accumulate secrets."
sourcebook: "_NPC Core_, page 13."
```

```encounter-table
name: Courtesan
creatures:
  - 1: Courtesan
```
