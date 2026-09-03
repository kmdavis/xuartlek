---
obsidianUIMode: preview
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
aon_id: "creature-3451"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3451"
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
    desc: "Perception +27; lifesense 60 feet"
languages: "Common, Necril; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +26, Deception +27, Intimidation +29, Religion +31, Undead Lore +33"
abilityMods: [5, 4, 6, 2, 4, 6]
abilities_top:
  - name: "Mark of Fate"
    desc: "(curse, divine) A creature that slays the deific vessel must succeed at a DC 35 Will save or be visibly marked as anathema to Urgathoa. It gains weakness 10 to unholy and takes a –2 circumstance penalty to Charisma-based skill checks against followers of Urgathoa. Creatures attempting to Gather Information about or Track the marked creature gain a +2 circumstance bonus to their checks. The mark can't be hidden and can be removed only by participating in an _atone_ ritual led by a worshipper of Urgathoa who is 12th level or higher."
  - name: "Items"
    desc: "_+2 resilient explorer's clothing_, Scythe"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +28; __Ref__: +24; __Will__: +26"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ death effects, disease, paralyzed, unconscious; __Resistances__ void 15; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Void Tendrils"
    desc: "(aura, divine, void) 30 feet. When a creature in the aura would be healed by a vitality effect, the healing is reduced by 15 and the deific vessel regains 15 Hit Points."
  - name: "Limited Lifespan"
    desc: "(divine) The deific vessel takes 25 damage at the end of its turn if it Cast a Spell, used Borrow Time, or made a Strike that turn. This damage ignores resistance."
  - name: "Shattered Vessel"
    desc: "(divine, unholy) When the deific vessel dies, the divine power barely contained within their form explodes outward, dealing 6d8 spirit damage to each creature in a 30-foot emanation with a DC 33 basic Reflex save."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _decaying frost scythe_ +28 (deadly d10, Death, Magical, Trip, Unholy) __Damage__ 3d10+11 slashing plus 1d6 cold and 1d4 void"
  - name: "Melee"
    desc: "⬻ _decaying frost fist_ +28 (Agile, Death, Magical, Unarmed, Unholy) __Damage__ 3d4+11 bludgeoning plus 1d6 cold and 1d4 void"
  - name: "Ranged"
    desc: "⬻ grave pulse +27 (Cold, Death, ranged 120 feet, Unholy, Void) __Damage__ 3d6 cold plus 2d8 void"
abilities_bot:
  - name: "Borrow Time"
    desc: "⬻ (Divine, Void) The vessel chooses two different creatures in their void tendrils aura. Each one must be either undead or the vessel themself. One target loses 25 HP and the other regains that many HP. If a target is unwilling, it can negate the transfer with a successful DC 39 Fortitude save."
  - name: "Grave Chill"
    desc: "(Divine) The vessel's unarmed attacks and scythe gain the _+2 decaying frost greater striking_ runes when used by the vessel, and their Strikes gain the death trait. Consequences Of Magnitude Directly interceding in the mortal plane opens deities up to direct consequences from other divine entities and the very forces of fate itself. The moment a deific vessel comes into existence, a clock begins ticking down, ready to change the fate of all involved in the creation of this powerful entity. The gods and their heralds, from their unassailable positions, face far fewer consequences than the relatively unprotected vessels themselves."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 39, attack +31 - __Cantrips (8th)__ Detect Magic, Divine Lance, Message - __4th__ Harm (at will) - __6th__ Truesight, Vampiric Exsanguination, Zealous Conviction - __7th__ Divine Decree, Eclipse Burst, Execute - __8th__ Dominate, Harm (×4), Mask of Terror - __Constant (5th)__ Truespeech"
sourcebook: "_NPC Core_, page 37."
```

```encounter-table
name: Deific Vessel of Urgathoa
creatures:
  - 1: Deific Vessel of Urgathoa
```
