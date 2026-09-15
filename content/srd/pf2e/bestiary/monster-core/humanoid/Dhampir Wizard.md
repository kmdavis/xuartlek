---
noteType: pf2eMonster
aliases: "Dhampir Wizard"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/dhampir
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dhampir Wizard"
level: 2
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2913"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dhampir Wizard"
level: "Creature 2"
size: "Medium"
trait_01: "Dhampir"
trait_02: "Human"
trait_03: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "+4; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +8, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, Vampire Lore +8"
abilityMods: [2, 3, 0, 4, 0, 1]
abilities_top:
  - name: "Items"
    desc: "Dagger, spellbook containing their prepared spells, Staff"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +7; __Will__: +6 +2 circumstance to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
hp: 22
health:
  - name: "HP"
    desc: "22 (void healing)"
abilities_mid:
  - name: "Blood of the Night"
    desc: "The dhampir's penalty and Hit Point reduction from the [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] condition are reduced as though the condition value were 1 lower."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ staff +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-handed d8]]) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+2 piercing"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +8 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]] (×2) Dhampir Dwellings Most dhampirs make their homes in urban areas, though some more reclusive individuals claim ruins or dungeons as their domains. Those few who maintain a connection with a vampire parent may be found living under that parent's roof and even inheriting an estate after the vampire meets an untimely end."
sourcebook: "_Monster Core_, page 95."
```

```encounter-table
name: Dhampir Wizard
creatures:
  - 1: Dhampir Wizard
```
