---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Yarnspinner"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Yarnspinner"
level: 7
source: "NPC Core"
aon_id: "creature-3647"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3647"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Halfling Yarnspinner"
level: "Creature 7"
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; keen eyes"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Halfling|Halfling]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|History Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +19, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +15, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +15"
abilityMods: [-1, 4, 0, 4, 3, 5]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action to find [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Tale Specialist"
    desc: "For encounters involving storytelling, local history, or lore, the yarnspinner is a 10th-level challenge."
  - name: "Items"
    desc: "book of fables, Chain Shirt, _+1 [[srd/pf2e/compendium/equipment/weapons/sling/halfling-sling-staff|halfling sling staff]]_ (20 bullets), _+1 [[srd/pf2e/compendium/equipment/weapons/sword/shortsword|shortsword]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +15; __Will__: +18"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Guidance Through Tales"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "An ally the yarnspinner can see fails a skill check"
  - name: "Effect"
    desc: "The yarnspinner offers a brief reminder about a legendary hero, granting their ally a +2 circumstance bonus to the triggering skill check, potentially turning the failure into a success."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _shortsword_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+3 piercing plus resonant weapons"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _halfling sling staff_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 30 feet, reload 1) __Damage__ 1d10+3 bludgeoning plus resonant weapons"
abilities_bot:
  - name: "Mesmerizing Tale"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The yarnspinner weaves a long-winded but captivating narrative that enchants those nearby. Any creature that's in a 20-foot emanation or starts its turn in the aura must attempt a DC 24 Will save. The Mesmerizing Tale lasts until the end of the yarnspinner's next turn, but can be Sustained. The first time the yarnspinner Sustains the aura on subsequent rounds, the aura expands by 10 feet, to a maximum of 60 feet."
  - name: "Critical Success"
    desc: "The creature is unaffected, and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the yarnspinner until the start of its next turn, and must spend all its actions to move closer to the yarnspinner and listen to the tale."
  - name: "Resonant Weapons"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) If the yarnspinner's Mesmerizing Tale aura is active or they have cast a spell within the last round, their Strikes with magic weapons deal an additional 2d10 sonic damage."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]], [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]], [[srd/pf2e/compendium/spells/rank-1/mindlink|Mindlink]], [[srd/pf2e/compendium/spells/rank-1/ventriloquism|Ventriloquism]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/laughing-fit|Laughing Fit]], [[srd/pf2e/compendium/spells/rank-2/revealing-light|Revealing Light]], [[srd/pf2e/compendium/spells/rank-1/soothe|Soothe]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/heroism|Heroism]], [[srd/pf2e/compendium/spells/rank-3/ring-of-truth|Ring of Truth]], [[srd/pf2e/compendium/spells/rank-1/soothe|Soothe]] (4 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-4/confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-4/honeyed-words|Honeyed Words]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (3 slots)"
sourcebook: "_NPC Core_, page 192."
```

```encounter-table
name: Halfling Yarnspinner
creatures:
  - 1: Halfling Yarnspinner
```
