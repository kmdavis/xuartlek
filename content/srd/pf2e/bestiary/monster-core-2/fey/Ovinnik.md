---
noteType: pf2eMonster
aliases: "Ovinnik"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/tiny
statblock: inline
name: "Ovinnik"
level: 4
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4443"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ovinnik"
level: "Creature 4"
size: "Tiny"
trait_01: "Fey"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; tremorsense (imprecise) within their entire bound granary or storeroom"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Lore|Household Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13"
abilityMods: [0, 5, 0, 2, 5, 3]
abilities_top:
  - name: "Items"
    desc: "pitchfork"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +13; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 5; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 5"
abilities_mid:
  - name: "Shy"
    desc: "A ovinnik is naturally [[srd/pf2e/compendium/rules-elements/Conditions#Invisible|invisible]] while within sight of their bound home. The ovinnik can become visible, or even selectively visible— allowing some people to see them."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d6+3 slashing"
abilities_bot:
  - name: "Raise Grain Cloud"
    desc: "⬺ While in their bound storeroom or granary, the ovinnik slams a paw against the ground, stirring up a cloud of grain dust in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]]. Within this cloud, they gain a +4 status bonus to any fire damage they deal. The ovinnik doubles their fire [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Immunity, Weakness, and Resistance#Resistance|resistance]] against this increased damage. The grain cloud dissipates after the first such effect or after 1 minute if no such effects occur. Ovinnik's Foretelling Ovinniks, on certain days, might deign to tell the future. Peasants approach the window or doorway of the fey's domain and present their bare palms. If the ovinnik touches them with a furred paw, then their family lives will be good. A smooth hand, however, signals brewing strife."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Cleanse Cuisine|Cleanse Cuisine]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Augury|Augury]], [[srd/pf2e/compendium/spells/rank-1/Breathe Fire|Breathe Fire]], [[srd/pf2e/compendium/spells/rank-2/Floating Flame|Floating Flame]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]]"
sourcebook: "_Monster Core 2_, page 195."
```

```encounter-table
name: Ovinnik
creatures:
  - 1: Ovinnik
```
