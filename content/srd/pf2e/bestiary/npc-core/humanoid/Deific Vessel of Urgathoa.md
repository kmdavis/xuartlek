---
noteType: pf2eMonster
aliases: "Deific Vessel of Urgathoa"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Deific Vessel of Urgathoa"
level: 15
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3451"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Deific Vessel of Urgathoa"
level: "Creature 15"
size: "Medium"
trait_01: "Divine"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "+27; lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +26, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +29, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +31, [[srd/pf2e/compendium/rules-elements/skills/Lore|Undead Lore]] +33"
abilityMods: [5, 4, 6, 2, 4, 6]
abilities_top:
  - name: "Mark of Fate"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A creature that slays the deific vessel must succeed at a DC 35 Will save or be visibly marked as anathema to [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Urgathoa|Urgathoa]]. It gains weakness 10 to [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] and takes a –2 circumstance penalty to Charisma-based skill checks against followers of Urgathoa. Creatures attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] about or [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] the marked creature gain a +2 circumstance bonus to their checks. The mark can't be hidden and can be removed only by participating in an [[srd/pf2e/compendium/spells/rituals/Atone|_atone_]] ritual led by a worshipper of Urgathoa who is 12th level or higher."
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/Resilient|resilient]] [[srd/pf2e/compendium/equipment/Armor#Explorer's Clothing|explorer's clothing]]_, Scythe"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +28; __Ref__: +24; __Will__: +26"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Void Tendrils"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) 30 feet. When a creature in the aura would be healed by a vitality effect, the healing is reduced by 15 and the deific vessel regains 15 Hit Points."
  - name: "Limited Lifespan"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) The deific vessel takes 25 damage at the end of its turn if it Cast a Spell, used Borrow Time, or made a Strike that turn. This damage ignores resistance."
  - name: "Shattered Vessel"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) When the deific vessel dies, the divine power barely contained within their form explodes outward, dealing 6d8 spirit damage to each creature in a 30-foot emanation with a DC 33 basic Reflex save."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _decaying frost scythe_ +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d10+11 slashing plus 1d6 cold and 1d4 void"
  - name: "Melee"
    desc: "⬻ _decaying frost fist_ +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d4+11 bludgeoning plus 1d6 cold and 1d4 void"
  - name: "Ranged"
    desc: "⬻ grave pulse +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], ranged 120 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) __Damage__ 3d6 cold plus 2d8 void"
abilities_bot:
  - name: "Borrow Time"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) The vessel chooses two different creatures in their void tendrils aura. Each one must be either [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] or the vessel themself. One target loses 25 HP and the other regains that many HP. If a target is unwilling, it can negate the transfer with a successful DC 39 Fortitude save."
  - name: "Grave Chill"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) The vessel's unarmed attacks and scythe gain the _+2 [[srd/pf2e/compendium/equipment/runes/Decaying|decaying]] [[srd/pf2e/compendium/equipment/runes/Frost|frost]] [[srd/pf2e/compendium/equipment/runes/Striking|greater striking]]_ runes when used by the vessel, and their Strikes gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] trait. Consequences Of Magnitude Directly interceding in the mortal plane opens deities up to direct consequences from other divine entities and the very forces of fate itself. The moment a deific vessel comes into existence, a clock begins ticking down, ready to change the fate of all involved in the creation of this powerful entity. The gods and their heralds, from their unassailable positions, face far fewer consequences than the relatively unprotected vessels themselves."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 39, attack +31 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]], [[srd/pf2e/compendium/spells/rank-6/Zealous Conviction|Zealous Conviction]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-7/Eclipse Burst|Eclipse Burst]], [[srd/pf2e/compendium/spells/rank-7/Execute|Execute]] - __8th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (×4), [[srd/pf2e/compendium/spells/rank-7/Mask of Terror|Mask of Terror]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_NPC Core_, page 37."
```

```encounter-table
name: Deific Vessel of Urgathoa
creatures:
  - 1: Deific Vessel of Urgathoa
```
