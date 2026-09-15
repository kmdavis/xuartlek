---
noteType: pf2eMonster
aliases: "Druid Circle"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Druid Circle"
level: 12
source: "Battlecry!"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3913"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Druid Circle"
level: "Creature 12"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Wildsong|Wildsong]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +25, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +25, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +25"
abilityMods: [1, 4, 1, 2, 7, 4]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +19; __Ref__: +22; __Will__: +25"
hp: 210
health:
  - name: "HP"
    desc: "210 (4 segments); __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Call Down the Storm"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|Electricity]]) The druids summon wind and lightning against all creatures in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Burst|burst]] within 80 feet. This storm deals 3d10 electricity damage (DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). A creature who fails the save is also pushed 5 feet away from the druid circle. When the druid circle is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Sickle and Staff"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The druids strike out in a coordinated melee attack against all enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] with a DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save. The damage dealt depends on the number of actions. ⬻ 2d6 bludgeoning or slashing damage ⬺ 4d6+9 bludgeoning or slashing damage ⬽ 5d6+13 bludgeoning or slashing damage"
  - name: "Troop Spellcasting"
    desc: "When the druid circle [[srd/pf2e/compendium/rules-elements/actions/player-core#Cast a Spell|Casts a Spell]], its constituent members combine their efforts into casting a more powerful version of the spell than any one member could achieve alone. When Casting a Spell that has an area of a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Burst|burst]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]], or [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Line|line]] and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 32, attack +26 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Caustic Blast|Caustic Blast]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Hydraulic Torrent|Hydraulic Torrent]], [[srd/pf2e/compendium/spells/rank-3/Lightning Bolt|Lightning Bolt]], [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|Speak with Plants]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]], [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]], [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]], [[srd/pf2e/compendium/spells/rank-6/Tangling Creepers|Tangling Creepers]]"
sourcebook: "_Battlecry!_, page 179."
```

```encounter-table
name: Druid Circle
creatures:
  - 1: Druid Circle
```
