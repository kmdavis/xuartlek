---
obsidianUIMode: preview
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
aon_id: "creature-4354"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4354"
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
    desc: "Perception +20; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +20, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +22, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +18, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +17"
abilityMods: [4, 5, 3, 6, 5, 4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +20; __Will__: +19 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to [[srd/pf2e/books/player-core/chapter-7-spells/counteracting|counteract]] any [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]] effect that targets them (counteract rank 5th, counteract modifier +20). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally. __Shoo!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "An enemy within 15 feet damages the dragon"
  - name: "Effect"
    desc: "The dragon teleports the creature up to 15 feet away. The destination must be on the ground and in a space with no hazards."
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d8+8 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+8 bludgeoning"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]]) The dragon exhales a swirl of energy that pulls creatures apart, dealing 8d6 force damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The dragon can teleport any creature that fails its save, teleporting that creature up to 30 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
  - name: "Phase Jump"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dragon teleports up to 60 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
sourcebook: "_Monster Core 2_, page 124."
```

```encounter-table
name: Young Phase Dragon
creatures:
  - 1: Young Phase Dragon
```
