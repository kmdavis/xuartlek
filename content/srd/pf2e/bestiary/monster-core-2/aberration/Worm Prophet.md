---
noteType: pf2eMonster
aliases: "Worm Prophet"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Worm Prophet"
level: 12
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4572"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Worm Prophet"
level: "Creature 12"
size: "Medium"
trait_01: "Aberration"
trait_02: "Swarm"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 23
perception:
  - name: "Perception"
    desc: "+23; darkvision, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +20, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +22, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +24, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +22, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +25, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +22"
abilityMods: [5, 2, 4, 3, 7, 6]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Religious Symbol|silver religious symbol]] (10), _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/hammer/Warhammer|warhammer]]_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +20; __Ref__: +20; __Will__: +25"
hp: 160
health:
  - name: "HP"
    desc: "160; __Immunities__ precision, swarm mind, [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ physical 10, poison 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] 10; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage 10"
abilities_mid:
  - name: "Discorporate"
    desc: "When the worm prophet is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the worm prophet can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the worm prophet permanently. The invertebrates have a collective pool of HP, typically equal to 40 HP, and the same AC, saves, immunities, resistances, and weaknesses as the worm prophet. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the worm prophet."
speed: "25 feet, burrow 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _warhammer_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 2d8+11 bludgeoning plus clinging remnants"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]]) __Damage__ 1d4+1 bludgeoning plus clinging remnants"
abilities_bot:
  - name: "A Thousand Mouths in Prayer"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]]) The worm prophet's constituent creatures whisper countless paeans to their gods. The worm prophet attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] (counteract modifier +24, counteract rank 6) an effect on a creature within 30 feet that's imposing one of the following conditions: [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]], [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]], [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]], [[srd/pf2e/compendium/rules-elements/Conditions#Deafened|deafened]], [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]], [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]], [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent damage]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]], or [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]]. Once the worm prophet successfully counteracts an effect in this way, it can't do so again for 1d4 rounds."
  - name: "Clinging Remnants"
    desc: "A worm prophet's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 3d4 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent piercing damage]]."
  - name: "Draw Bugs"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|Healing]]) The worm prophet draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 15 HP. At the GM's discretion, the skittering slayer doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Squirming Embrace"
    desc: "⬻ The worm prophet [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]]. If they end their movement sharing a space with a creature, they deal 4d6 piercing damage to the creature, with a DC 32 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save. The worm prophet can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] instead of Striding."
  - name: "Swarm Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The worm prophet collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession. In this form, the worm prophet can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]]. They can use the same action to coalesce from their swarm shape back into their normal form."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Divine Wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Talking Corpse|Talking Corpse]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/Crisis of Faith|Crisis of Faith]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-5/Spiritual Guardian|Spiritual Guardian]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Blessed Boundary|Blessed Boundary]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]]"
sourcebook: "_Monster Core 2_, page 312."
```

```encounter-table
name: Worm Prophet
creatures:
  - 1: Worm Prophet
```
