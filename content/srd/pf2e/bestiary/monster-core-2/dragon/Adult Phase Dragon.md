---
noteType: pf2eMonster
aliases: "Adult Phase Dragon"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Phase Dragon"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4355"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Phase Dragon"
level: "Creature 13"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 25
perception:
  - name: "Perception"
    desc: "+25; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +25, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +23, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +25, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +23"
abilityMods: [5, 7, 3, 8, 6, 5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +20; __Ref__: +25; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]]"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]"
abilities_mid:
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] any [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effect that targets them (counteract rank 7th, counteract modifier +25). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally. __Shoo!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Trigger"
    desc: "An enemy within 15 feet damages the dragon"
  - name: "Effect"
    desc: "The dragon teleports the creature up to 25 feet away. The destination must be on the ground and in a space with no hazards."
speed: "50 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d12+12 piercing"
  - name: "Melee"
    desc: "⬻ claw +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d10+12 bludgeoning"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The dragon exhales a swirl of energy that pulls creatures apart, dealing 12d6 force damage in a 40-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The dragon can teleport any creature that fails its save, teleporting that creature up to 40 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
  - name: "Phase Jump"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dragon teleports up to 75 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]]."
  - name: "Portal Strike"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The dragon momentarily opens a small portal and makes a claw Strike against a creature within 75 feet. The target is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the Strike."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-4/Planar Tether|Planar Tether]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]]"
sourcebook: "_Monster Core 2_, page 125."
```

```encounter-table
name: Adult Phase Dragon
creatures:
  - 1: Adult Phase Dragon
```
