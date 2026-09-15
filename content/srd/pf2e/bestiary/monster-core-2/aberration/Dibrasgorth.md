---
noteType: pf2eMonster
aliases: "Dibrasgorth"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Dibrasgorth"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4331"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Dibrasgorth"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22; darkvision 120 feet, planar sight 120 feet, [[srd/pf2e/compendium/spells/rank-2/See the Unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +20, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +20, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +20, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +19"
abilityMods: [8, 1, 4, 5, 2, 0]
abilities_top:
  - name: "Planar Sight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) The eyes at the end of their tentacles allow a dibrasgorth to see into planes coterminous with the one it is currently on at the listed range. For instance, if they're in [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]], they can see into the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]] and [[srd/pf2e/compendium/gm/Planes#The Netherworld|the Netherworld]]."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +20; __Will__: +23"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/Conditions#Petrified|petrification]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 15"
abilities_mid:
  - name: "Warped Space"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) 100 feet. The dibrasgorth's presence distorts the fabric of space. Any other creature who uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effect or spell within the aura must attempt a DC 33 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 2."
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d10+16 piercing plus draining bite"
  - name: "Melee"
    desc: "⬻ tentacle +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d8+16 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Breath of Phantasms"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/gm-core/Inhaled|Inhaled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]) The dibrasgorth exhales a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of noxious gas. Each creature in the area takes 7d6 poison damage (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save). On a failure, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 round (or 2 rounds on a critical failure)."
  - name: "Drag Through Dimensions"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The dibrasgorth has a creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] with a tentacle"
  - name: "Effect"
    desc: "The dibrasgorth's tentacle whips through coterminous planes as it smashes the creature it is holding against the ground and other natural features in each plane before returning to this plane. The creature takes 5d8 bludgeoning damage (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). A creature who fails the save is also [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 1 for 1 round and [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 by the rapid planar travel."
  - name: "Draining Bite"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) A dibrasgorth feeds on the spirits of its victims. A creature that is damaged by the dibrasgorth's jaws Strike must attempt a DC 30 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 1 (drained 2 on a critical failure). In addition, the dibrasgorth gains 10 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Temporary Hit Points|temporary Hit Points]] that last for 1 minute if the creature fails or critically fails the save."
  - name: "Transdimensional Tentacles"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The dibrasgorth can worm its tentacles through nearby planes to attack. While in [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]], its tentacle Strikes ignore all [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Cover|cover]] from objects unless those objects exist on both the Universe and either [[srd/pf2e/compendium/gm/Planes#The Netherworld|the Netherworld]] or the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]], or the objects have the [[srd/pf2e/compendium/rules-elements/traits/player-core/Extradimensional|extradimensional]] trait. The Myth Of Black Magga Varisian locals who live near the Storval Deep, an enormous freshwater lake on the Storval Plateau, tell tales of Black Magga, a powerful and unholy dibrasgorth rumored to be older than the gods. They say that terrible storms presage her appearance near the lake's surface, and that those who see her form and live are cursed to be unable to completely describe her, with black blood welling in their mouth if they make the attempt."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Nightmare|Nightmare]], [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Banishment|Banishment]], [[srd/pf2e/compendium/spells/rank-5/Synaptic Pulse|Synaptic Pulse]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/Repulsion|Repulsion]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 104."
```

```encounter-table
name: Dibrasgorth
creatures:
  - 1: Dibrasgorth
```
