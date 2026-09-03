---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Mage"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Clockwork Mage"
level: 9
source: "Monster Core 2"
aon_id: "creature-4296"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4296"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Mage"
level: "Creature 9"
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17"
abilityMods: [2, 6, 4, -5, 2, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 26, standby"
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/lock-superior|clockwork wand]]"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +19; __Will__: +17"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Nonlethal|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 5 (except [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]] or [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10, [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]] 10"
abilities_mid:
  - name: "Clockwork Wand"
    desc: "The clockwork mage uses a mechanical wand as a focus to channel magical energy. This wand is built into the clockwork mage's chest, with only the crystal at the end exposed. The mage can [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interact]] to the remove the wand, or someone else can remove it with a DC 31 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disable a Device|Disable a Device]]. The clockwork mage becomes unable to cast any spells except cantrips while the wand is removed. When removed, the clockwork wand is a magic wand containing the last 2nd-rank innate spell the clockwork mage cast (the GM determines the spell randomly if the mage has not cast any eligible spells). The spells are placed within the wand while the mage is created, and the creator can substitute other arcane spells of the appropriate rank."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d10+6 bludgeoning"
abilities_bot:
  - name: "Energize Clockwork Wand"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The clockwork mage regains a spell it has already cast that day. It must spend 1 hour of its operational time, or 2 hours if the spell is 3rd rank or higher."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/tangle-vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/carryall|Carryall]], [[srd/pf2e/compendium/spells/rank-1/gentle-landing|Gentle Landing]], [[srd/pf2e/compendium/spells/rank-1/grease|Grease]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/revealing-light|Revealing Light]], [[srd/pf2e/compendium/spells/rank-2/web|Web]] (Player Core 2 255) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/aqueous-orb|Aqueous Orb]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-4/fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/wall-of-fire|Wall of Fire]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|Howling Blizzard]], [[srd/pf2e/compendium/spells/rank-5/slither|Slither]]"
sourcebook: "_Monster Core 2_, page 72."
```

```encounter-table
name: Clockwork Mage
creatures:
  - 1: Clockwork Mage
```
