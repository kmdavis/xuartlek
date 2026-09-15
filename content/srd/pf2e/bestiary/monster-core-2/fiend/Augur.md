---
noteType: pf2eMonster
aliases: "Augur"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/tiny
statblock: inline
name: "Augur"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4606"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Augur"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; greater darkvision, painsight"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +4, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Lore|Torture Lore]] +7"
abilityMods: [-1, 3, 1, 2, 1, -1]
abilities_top:
  - name: "Painsight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A velstrac automatically knows whether a creature it sees has any of the [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]], and [[srd/pf2e/compendium/rules-elements/Conditions#Wounded|wounded]] conditions as well as the value of those conditions."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 15
health:
  - name: "HP"
    desc: "15 , regeneration 2 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] or [[srd/pf2e/compendium/equipment/materials/Silver|silver]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]]; __Weaknesses__ holy 5, silver 5"
abilities_mid:
  - name: "Feel the Blades"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. When a creature ends its turn in the aura, it feels the sharp barbs of the augur's blades on its skin. The creature must succeed at a DC 17 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] 1 (frightened 2 on a critical failure)."
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ blade +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d4–1 slashing plus 1d4 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) The augur stares at a creature they can see within 30 feet. The target must immediately attempt a Will save against feel the blades. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the augur's next turn."
  - name: "Whirling Slice"
    desc: "⬺ The augur [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]], whirling as they move. The augur deals the damage of their blade Strike to each creature whose space they enter (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). Each creature is affected only once, even if the augur moves through its space multiple times."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (×3) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Augury|Augury]] (×2) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]] (once per week)"
sourcebook: "_Monster Core 2_, page 344."
```

```encounter-table
name: Augur
creatures:
  - 1: Augur
```
