---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stygira"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Stygira"
level: 7
source: "Monster Core 2"
aon_id: "creature-4569"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4569"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Stygira"
level: "Creature 7"
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; gemsight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], Cyclops, [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Gem Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +17"
abilityMods: [4, 4, 5, 4, 6, 2]
abilities_top:
  - name: "Gemsight"
    desc: "As long as the stygira holds a gemstone, they can see through the gem with darkvision and the effects of [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]. A stygira is blind when they aren't holding a gem in a hand."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/materials/stone-object-low-grade|gemstone]] (worth 25 gp)"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +13; __Will__: +19 +1 status to all saves vs. magic"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]; __Resistances__ physical 10 (except [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]])"
abilities_mid:
  - name: "Light Sickness"
    desc: "A stygira in an area of [[srd/pf2e/books/player-core/chapter-8-playing-the-game/perception-and-detection#Bright Light|bright light]] is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+10 slashing plus stone curse"
abilities_bot:
  - name: "Gem Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The stygira holds aloft a gem and gazes into the mind of a creature within 30 feet, infusing the creature's thoughts with visions of its own dead body slowly petrifying. The creature must succeed at a DC 25 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 1 (frightened 2 on a critical failure)."
  - name: "Stone Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) Wounds dealt by the stygira's claws leave the flesh bleached of color and turn the blood that runs from them dark gray. Each time a creature is damaged by the stygira's claw Strike, it must succeed at a DC 25 Fortitude save or become permanently [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 (slowed 2 on a critical failure) as its flesh stiffens like stone. If a creature is reduced to 0 Hit Points from the stygira's claw Strike and fails the saving throw against stone curse, it's [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]]. A creature that spends 8 hours in direct sunlight can attempt a new saving throw to remove the effects of stone curse, even if it has been petrified. Stygira Gems The gem a stygira carries doesn't need to be particularly valuable, but some stygiras prefer to use more expensive gems as an affectation. More powerful stygiras have developed methods of using particularly expensive gems to enhance their Gem Gaze ability, allowing some to charm those they gaze upon, light their enemies on fire, or even afflict creatures with debilitating poison."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/augury|Augury]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/clairaudience|Clairaudience]], [[srd/pf2e/compendium/spells/rank-3/earthbind|Earthbind]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/clairvoyance|Clairvoyance]], [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]], [[srd/pf2e/compendium/spells/rank-4/shape-stone|Shape Stone]]"
sourcebook: "_Monster Core 2_, page 308."
```

```encounter-table
name: Stygira
creatures:
  - 1: Stygira
```
