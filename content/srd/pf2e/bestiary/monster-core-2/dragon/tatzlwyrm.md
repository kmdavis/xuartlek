---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tatzlwyrm"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/medium
statblock: inline
name: "Tatzlwyrm"
level: 2
source: "Monster Core 2"
aon_id: "creature-4576"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4576"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tatzlwyrm"
level: "Creature 2"
size: "Medium"
trait_01: "Dragon"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +4, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [4, 1, 3, -3, 2, 0]
abilities_top:
  - name: "Natural Camouflage"
    desc: "A tatzlwyrm's green, gray, and brown scales provide it natural camouflage. In areas of dense undergrowth, a tatzlwyrm can move at its full Speed when [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaking]], and it gains a +4 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]]."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +5; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d8+6 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 1d6+6 slashing"
abilities_bot:
  - name: "Poison Gasp"
    desc: "⬻ The tatzlwyrm belches a puff of poisonous vapor into the face of an adjacent creature, which must attempt a DC 15 Fortitude save; the creature takes a –2 circumstance penalty to this save if it's [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. The tatzlwyrm can't use Poison Gasp again for 2 rounds."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
  - name: "Failure"
    desc: "The target takes 2d6 poison damage and is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 for 1 round."
  - name: "Critical Failure"
    desc: "The target takes 4d6 poison damage and is enfeebled 1 for 1 minute. Other Tatzlwyrms People in some regions claim to have seen creatures that appear just like tatzlwyrms in most respects—a long body, two arms, and a head—except that they have traits not of reptilian origin. Travelers on a savanna should beware a furry, [[srd/pf2e/bestiary/monster-core/animal/lion|lion]]-headed tatzlwyrm protecting their cubs, while those in the mountains might be attacked by a feathered (but wingless) variant with the head of an [[srd/pf2e/bestiary/monster-core/animal/eagle|eagle]]."
sourcebook: "_Monster Core 2_, page 316."
```

```encounter-table
name: Tatzlwyrm
creatures:
  - 1: Tatzlwyrm
```
