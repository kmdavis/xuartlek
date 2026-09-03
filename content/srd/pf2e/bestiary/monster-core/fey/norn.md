---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Norn"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Norn"
level: 20
source: "Monster Core"
aon_id: "creature-3108"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3108"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Norn"
level: "Creature 20"
size: "Large"
trait_01: "Fey"
trait_02: "Rare"
modifier: 41
perception:
  - name: "Perception"
    desc: "Perception +41; [[srd/pf2e/compendium/spells/cantrips/detect-magic|_detect magic_]], greater darkvision, lifesense 120 feet, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +36, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +35, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +37, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +28, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +38, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +34, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +31, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +34"
abilityMods: [7, 6, 6, 6, 10, 7]
abilities_top:
  - name: "Sense Fate"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]]) A norn automatically rolls a 20 when she rolls initiative."
  - name: "Triumvirate"
    desc: "This functions as the coven ability, except only norns can join a triumvirate, and it functions only as long as exactly three norns are part of the triumvirate. A triumvirate grants the following spells: [[srd/pf2e/compendium/spells/rank-10/cataclysm|_cataclysm_]], [[srd/pf2e/compendium/spells/rank-9/foresight|_foresight_]], [[srd/pf2e/compendium/spells/rank-10/manifestation|_manifestation_]] (once per day), [[srd/pf2e/compendium/spells/rank-8/pinpoint|_pinpoint_]], and [[srd/pf2e/compendium/spells/rank-10/revival|_revival_]]."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/knife/shears|Shears]] (see favored weapon)"
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +34; __Ref__: +30; __Will__: +38 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 375
health:
  - name: "HP"
    desc: "375 , regeneration 20 (deactivated by [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Weaknesses__ cold iron 20"
speed: "35 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shears +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 4d4+15 slashing plus 6d6 void and sever fate"
  - name: "Melee"
    desc: "⬻ hand of fate +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 4d10+15 void plus sever fate"
abilities_bot:
  - name: "Fated"
    desc: "When a creature is subject to a [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] effect from a norn and a [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effect from any source other than a norn (or vice versa), the norn's effect automatically counteracts the other effect and then takes place normally, rather than the two effects canceling each other out. If both the fortune and misfortune effect are from a norn, then the two cancel each other out as normal. At the GM's discretion, powerful entities related to fate or luck, like Desna, Magdh, or Pharasma, can't have their effects negated by this ability."
  - name: "Sever Fate"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) When a norn deals void damage with a Strike, she regains 10 Hit Points. The target must succeed at a DC 39 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (drained 2 on a critical failure). Further void damage dealt by the norn increases the drained condition value by 1 on a failed save (or by 2 on a critical failure), to a maximum of drained 4."
  - name: "Shift Fate"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Trigger"
    desc: "A creature within 120 feet attempts a saving throw"
  - name: "Effect"
    desc: "The creature rolls the saving throw twice, and then the norn decides which result applies. If the norn chooses the lower roll, this is a [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effect; if she chooses the higher roll, it's a [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] effect; if they're the same, she decides which trait to apply."
  - name: "Snip Thread"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The norn produces a golden thread linked to the fate of a creature within 100 feet of her, then snips it short with her shears. The target takes 100 void damage (DC 42 basic Fortitude save). If the target is reduced to 0 Hit Points from this damage, the thread is completely severed and the creature dies immediately. A creature slain by Snip Thread can't be restored to life except by a [[srd/pf2e/compendium/spells/rituals/wish|_wish_]] ritual or similarly powerful magic; or by divine intervention. Regardless of the outcome of their saving throw, a creature targeted by Snip Thread then becomes temporarily immune for 24 hours. The norn can't use Snip Thread again for 1d4 rounds."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 42 - __7th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]] (at will), [[srd/pf2e/compendium/spells/rank-6/spellwrack|Spellwrack]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-8/migration|Migration]], [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]] - __9th__ [[srd/pf2e/compendium/spells/rank-7/execute|Execute]], [[srd/pf2e/compendium/spells/rank-9/phantasmagoria|Phantasmagoria]], [[srd/pf2e/compendium/spells/rank-7/retrocognition|Retrocognition]] - __10th__ [[srd/pf2e/compendium/spells/rank-10/freeze-time|Freeze Time]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/rank-8/hidden-mind|Hidden Mind]], [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 42 - __3rd__ Geas - __7th__ [[srd/pf2e/compendium/spells/rituals/collective-memories|Collective Memories]]"
sourcebook: "_Monster Core_, page 240."
```

```encounter-table
name: Norn
creatures:
  - 1: Norn
```
