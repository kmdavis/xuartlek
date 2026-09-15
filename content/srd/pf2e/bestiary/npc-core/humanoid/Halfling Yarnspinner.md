---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3647"
socialImage: og-image.png
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
    desc: "+14; keen eyes"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Halfling|Halfling]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +16, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|History Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +19, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +15, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +15"
abilityMods: [-1, 4, 0, 4, 3, 5]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action to find [[srd/pf2e/compendium/rules-elements/Conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/Conditions#Undetected|undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Tale Specialist"
    desc: "For encounters involving storytelling, local history, or lore, the yarnspinner is a 10th-level challenge."
  - name: "Items"
    desc: "book of fables, Chain Shirt, _+1 [[srd/pf2e/compendium/equipment/weapons/sling/Halfling Sling Staff|halfling sling staff]]_ (20 bullets), _+1 [[srd/pf2e/compendium/equipment/weapons/sword/Shortsword|shortsword]]_"
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
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "An ally the yarnspinner can see fails a skill check"
  - name: "Effect"
    desc: "The yarnspinner offers a brief reminder about a legendary hero, granting their ally a +2 circumstance bonus to the triggering skill check, potentially turning the failure into a success."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _shortsword_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+3 piercing plus resonant weapons"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _halfling sling staff_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 30 feet, reload 1) __Damage__ 1d10+3 bludgeoning plus resonant weapons"
abilities_bot:
  - name: "Mesmerizing Tale"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The yarnspinner weaves a long-winded but captivating narrative that enchants those nearby. Any creature that's in a 20-foot emanation or starts its turn in the aura must attempt a DC 24 Will save. The Mesmerizing Tale lasts until the end of the yarnspinner's next turn, but can be Sustained. The first time the yarnspinner Sustains the aura on subsequent rounds, the aura expands by 10 feet, to a maximum of 60 feet."
  - name: "Critical Success"
    desc: "The creature is unaffected, and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] with the yarnspinner until the start of its next turn, and must spend all its actions to move closer to the yarnspinner and listen to the tale."
  - name: "Resonant Weapons"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]]) If the yarnspinner's Mesmerizing Tale aura is active or they have cast a spell within the last round, their Strikes with magic weapons deal an additional 2d10 sonic damage."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]], [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]], [[srd/pf2e/compendium/spells/rank-1/Mindlink|Mindlink]], [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Laughing Fit|Laughing Fit]], [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/Heroism|Heroism]], [[srd/pf2e/compendium/spells/rank-3/Ring of Truth|Ring of Truth]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (4 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-4/Honeyed Words|Honeyed Words]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (3 slots)"
sourcebook: "_NPC Core_, page 192."
```

```encounter-table
name: Halfling Yarnspinner
creatures:
  - 1: Halfling Yarnspinner
```
