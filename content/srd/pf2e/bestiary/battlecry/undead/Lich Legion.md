---
noteType: pf2eMonster
aliases: "Lich Legion"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Lich Legion"
level: 18
source: "Battlecry!"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3926"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Lich Legion"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Rare"
trait_02: "Troop"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "+30; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +38, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +35, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +35, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +31, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +29"
abilityMods: [1, 5, 0, 9, 6, 4]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +27; __Ref__: +30; __Will__: +33 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]"
hp: 330
health:
  - name: "HP"
    desc: "330 (4 segments, mass rejuvenation, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 15, physical 15 (except magical bludgeoning); __Weaknesses__ area damage 15, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage 15"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 60 feet, DC 37"
  - name: "Mass Rejuvenation"
    desc: "This functions similarly to a [[srd/pf2e/compendium/gm/creature-families/Lich|lich's]] rejuvenation ability, though with all the liches of a legion returning as a troop thanks to a collective soul cage, which is a level 18 item that has Hardness 15 and 54 Hit Points."
  - name: "Troop Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the legion's sight casts a spell the legion has prepared"
  - name: "Effect"
    desc: "The lich legion expends a prepared spell to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counter]] the triggering creature's casting of that same spell. The lich legion loses the spell slot as if they had cast the triggering spell. The lich legion then attempts to counteract the triggering spell with a +2 status bonus to the counteract check."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Siphoning Grip"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The lich legion touches all enemies within a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] to drain their life (DC 37 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. For each action the lich legion uses, the legion gains 10 temporary Hit Points that last 1 minute. ⬻ 2d8 void damage ⬺ 4d8+11 void damage ⬽ 6d8+13 void damage"
  - name: "Steady Troop Spellcasting"
    desc: "When the lich legion Casts a Spell, their constituent members combine their efforts into casting a more powerful version of the spell than any one member could achieve alone. When Casting a Spell that has an area of a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Burst|burst]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]], or [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Line|line]] and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line. If a reaction would disrupt the lich legion's spellcasting action, the lich legion attempts a DC 12 flat [[srd/pf2e/books/player-core/chapter-1-introduction/Playing the Game#Check|check]]. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 40, attack +35 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/False Vitality|False Vitality]], [[srd/pf2e/compendium/spells/rank-2/Resist Energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/Fire Shield|Fire Shield]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]] (×2), [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-5/Wall of Ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]] (×2), [[srd/pf2e/compendium/spells/rank-6/Never Mind|Never Mind]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Eclipse Burst|Eclipse Burst]] (×2), [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]], [[srd/pf2e/compendium/spells/rank-7/Warp Mind|Warp Mind]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/Arctic Rift|Arctic Rift]] (×2), [[srd/pf2e/compendium/spells/rank-8/Desiccate|Desiccate]], [[srd/pf2e/compendium/spells/rank-8/Earthquake|Earthquake]] - __9th__ [[srd/pf2e/compendium/spells/rank-9/Falling Stars|Falling Stars]], [[srd/pf2e/compendium/spells/rank-9/Massacre|Massacre]], [[srd/pf2e/compendium/spells/rank-9/Phantasmagoria|Phantasmagoria]]"
sourcebook: "_Battlecry!_, page 185."
```

```encounter-table
name: Lich Legion
creatures:
  - 1: Lich Legion
```
