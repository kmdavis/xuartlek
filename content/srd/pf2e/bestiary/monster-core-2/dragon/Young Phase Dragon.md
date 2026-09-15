---
noteType: pf2eMonster
aliases: "Young Phase Dragon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Phase Dragon"
level: 9
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4354"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Phase Dragon"
level: "Creature 9"
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +20, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +22, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +18, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +17"
abilityMods: [4, 5, 3, 6, 5, 4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +20; __Will__: +19 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]]"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]"
abilities_mid:
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] any [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effect that targets them (counteract rank 5th, counteract modifier +20). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally. __Shoo!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Trigger"
    desc: "An enemy within 15 feet damages the dragon"
  - name: "Effect"
    desc: "The dragon teleports the creature up to 15 feet away. The destination must be on the ground and in a space with no hazards."
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d8+8 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+8 bludgeoning"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The dragon exhales a swirl of energy that pulls creatures apart, dealing 8d6 force damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The dragon can teleport any creature that fails its save, teleporting that creature up to 30 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
  - name: "Phase Jump"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dragon teleports up to 60 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]]"
sourcebook: "_Monster Core 2_, page 124."
```

```encounter-table
name: Young Phase Dragon
creatures:
  - 1: Young Phase Dragon
```
