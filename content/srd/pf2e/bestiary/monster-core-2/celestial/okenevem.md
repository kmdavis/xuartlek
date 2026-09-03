---
obsidianUIMode: preview
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
aon_id: "creature-4081"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4081"
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
    desc: "Perception +29; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +28, [[srd/pf2e/compendium/rules-elements/skills/lore|Heaven Lore]] +33, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +28, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +28, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +31, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +27"
abilityMods: [4, 6, 5, 6, 8, 7]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +25; __Ref__: +26; __Will__: +31 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 10"
abilities_mid:
  - name: "Divine Defenders"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]) 60 feet. Okenevem hold an exalted place among archons for their holy station. This draws lesser archons to defend them. When an enemy in the aura takes a hostile action against the okenevem, a cloud of minor archons swarms around it, causing it to take 2d6 persistent slashing damage and 2d6 persistent spirit damage. This persistent damage ends automatically if the enemy spends a round without taking a hostile action against the okenevem."
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ humbling touch +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|Spirit]]) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
  - name: "Ranged"
    desc: "⬻ humbling word +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], range increment 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|Spirit]]) __Damage__ 4d8 mental plus 4d6 spirit and humble bow"
abilities_bot:
  - name: "Spells"
    desc: "DC 36, attack +28 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-5/spiritual-guardian|Spiritual Guardian]] (×3) - __8th__ [[srd/pf2e/compendium/spells/rank-2/calm|Calm]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Humble Bow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A creature hit by one of the okenevem's Strikes is compelled to bow down in reverence. It must succeed at a DC 36 Will save or fall [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. If the creature Stands before the end of its next turn, it takes 3d8 mental damage. If the creature succeeds, it's temporarily immune for 1 minute."
  - name: "Sublime Vision"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The okenevem casts the [[srd/pf2e/compendium/spells/rank-9/overwhelming-presence|_overwhelming presence_]] spell, except instead of aggrandizing themself, the okenevem summons a vision of Heaven within 100 feet, and the target must humble themself in self-reflection rather than pay tribute."
sourcebook: "_Monster Core 2_, page 38."
```

```encounter-table
name: Okenevem
creatures:
  - 1: Okenevem
```
