---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Witchwyrd"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Witchwyrd"
level: 6
source: "Monster Core 2"
other_sources: "Pathfinder #149: Against the Scarlet Triad"
aon_id: "creature-4617"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4617"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Witchwyrd"
level: "Creature 6"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Uncommon"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]; one or more planar languages, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Desert Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15"
abilityMods: [3, 3, 1, 4, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1]] [[srd/pf2e/compendium/equipment/weapons/polearm/ranseur|ranseur]]_"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +13; __Ref__: +13; __Will__: +15"
hp: 110
health:
  - name: "HP"
    desc: "110; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]] 5"
abilities_mid:
  - name: "Absorb Force"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Trigger"
    desc: "A [[srd/pf2e/compendium/spells/rank-1/force-barrage|_force barrage_]] or Force Dart (see below) is fired at the witchwyrd, and the witchwyrd is aware of it and has a free hand"
  - name: "Effect"
    desc: "The witchwyrd “catches” one force projectile, absorbing it, preventing the damage, and causing that hand to glow while it holds this energy. A hand that's holding energy can't be used for any other purpose except to use Force Dart. The energy lasts for 1 minute or until it's released."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ranseur +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]]) __Damage__ 1d6+6 bludgeoning plus Grab"
abilities_bot:
  - name: "Force Dart"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/orc|force]]) The witchwyrd fires one dart of force per action spent (dealing 1d4+1 force damage each). They can't spend more actions on this ability than they have free hands. If they use a hand that has Absorbed Force, that hand hurls two darts instead of one, expending the held energy. Alien Allies High-ranking or wealthy witchwyrds rarely travel the planes alone, employing bodyguards to accompany them and leading entourages composed of various strange beings they’ve met during their travels."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/carryall|Carryall]] (at will), [[srd/pf2e/compendium/spells/rank-1/phantasmal-minion|Phantasmal Minion]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/resist-energy|Resist Energy]] (×2), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 355."
```

```encounter-table
name: Witchwyrd
creatures:
  - 1: Witchwyrd
```
