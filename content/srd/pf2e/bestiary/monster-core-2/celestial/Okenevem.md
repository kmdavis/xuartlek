---
noteType: pf2eMonster
aliases: "Okenevem"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Okenevem"
level: 15
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4081"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Okenevem"
level: "Creature 15"
size: "Large"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 29
perception:
  - name: "Perception"
    desc: "+29; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +28, [[srd/pf2e/compendium/rules-elements/skills/Lore|Heaven Lore]] +33, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +28, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +31, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +27"
abilityMods: [4, 6, 5, 6, 8, 7]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +25; __Ref__: +26; __Will__: +31 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 10"
abilities_mid:
  - name: "Divine Defenders"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]]) 60 feet. Okenevem hold an exalted place among archons for their holy station. This draws lesser archons to defend them. When an enemy in the aura takes a hostile action against the okenevem, a cloud of minor archons swarms around it, causing it to take 2d6 persistent slashing damage and 2d6 persistent spirit damage. This persistent damage ends automatically if the enemy spends a round without taking a hostile action against the okenevem."
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ humbling touch +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
  - name: "Ranged"
    desc: "⬻ humbling word +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], range increment 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
abilities_bot:
  - name: "Spells"
    desc: "DC 36, attack +28 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-5/Spiritual Guardian|Spiritual Guardian]] (×3) - __8th__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Humble Bow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) A creature hit by one of the okenevem's Strikes is compelled to bow down in reverence. It must succeed at a DC 36 Will save or fall [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. If the creature Stands before the end of its next turn, it takes 3d8 mental damage. If the creature succeeds, it's temporarily immune for 1 minute."
  - name: "Sublime Vision"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The okenevem casts the [[srd/pf2e/compendium/spells/rank-9/Overwhelming Presence|_overwhelming presence_]] spell, except instead of aggrandizing themself, the okenevem summons a vision of Heaven within 100 feet, and the target must humble themself in self-reflection rather than pay tribute."
sourcebook: "_Monster Core 2_, page 38."
```

```encounter-table
name: Okenevem
creatures:
  - 1: Okenevem
```
