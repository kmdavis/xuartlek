---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rekhep"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Rekhep"
level: 10
source: "Monster Core"
aon_id: "creature-2835"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2835"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Rekhep"
level: "Creature 10"
size: "Large"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +19, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +19, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [5, 1, 7, 2, 3, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/lance|lance]]_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +23; __Ref__: +15; __Will__: +19 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 10"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 15 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _holy lance_ +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/jousting|jousting d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+11 piercing plus 1d4 spirit (or 2d4 spirit vs. an [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] target)"
abilities_bot:
  - name: "Archon's Pursuit"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The rekhep saw another creature teleport within the last round and has at least one [[srd/pf2e/compendium/spells/rank-4/translocate|_translocate_]] spell remaining"
  - name: "Effect"
    desc: "The rekhep casts one of their _translocate_ spells, which is heightened to 5th rank and causes the rekhep to arrive in an unoccupied space it chooses within 30 feet of the creature it's pursuing. If the creature is too far away, the rekhep arrives as close as possible."
  - name: "Courageous Switch"
    desc: "When a rekhep uses their [[srd/pf2e/compendium/spells/rank-4/translocate|_translocate_]] innate spell, they can choose to move into the space of a willing ally they can see within range. If they do, the ally switches places with the archon, appearing in the space the archon just vacated, as if it too had cast _translocate_."
  - name: "Holy Armament"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]]) Any weapon gains the [[srd/pf2e/compendium/equipment/runes/holy|_holy_]] rune while the rekhep wields it."
  - name: "Living Shield"
    desc: "⬻ The rekhep grants an adjacent ally a +2 circumstance bonus to AC until they're no longer adjacent or until the start of the archon's next turn, whichever comes first. When the rekhep uses Archon's Protection against an attack against the shielded ally, the rekhep gains the resistance and takes the damage rather than the ally."
  - name: "Terrifying Smite"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The rekhep makes a Strike against an enemy that has one of the rekhep's allies within its reach. On a hit, the target takes an additional 2d8 mental damage and is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]. The extra damage and frightened value are doubled on a critical hit."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 27 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] (×3) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/share-life|Share Life]] (×3) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 28."
```

```encounter-table
name: Rekhep
creatures:
  - 1: Rekhep
```
