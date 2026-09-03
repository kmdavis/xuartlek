---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Obcisidaemon"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Obcisidaemon"
level: 19
source: "Monster Core 2"
aon_id: "creature-4309"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4309"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Obcisidaemon"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +39, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +34, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +36, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +32, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +36"
abilityMods: [10, 4, 8, 4, 5, 7]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+2 greater striking]] [[srd/pf2e/compendium/equipment/weapons/polearm/halberd|halberd]]_"
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +35; __Ref__: +29; __Will__: +32 +1 status to all saves vs. magic"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 20"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Scorched Earth"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 60 feet. Any creature that dies within the aura and isn't drawn into the obcisidaemon's cloak of souls via Inherit Soul must attempt a DC 38 Fortitude save. On a failure, the creature's body (but not its gear) is immediately reduced to a fine smear of ashes."
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _halberd_ +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d10+23 piercing"
  - name: "Melee"
    desc: "⬻ jaws +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 4d6+20 piercing plus Grab"
abilities_bot:
  - name: "Consume Soul"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The obcisidaemon consumes a soul from their cloak to gain one of the following effects. A soul consumed in this way can't be resurrected except by a wish ritual or a similarly powerful effect. _Empower Spell_ The obcisidaemon gains a +2 status bonus to their spell DCs and spell attack modifiers until the end of their next turn. _Empower Weapon_ The obcisidaemon's weapon gains the effects of a [[srd/pf2e/compendium/equipment/runes/flaming-greater|_greater flaming_]], [[srd/pf2e/compendium/equipment/runes/frost-greater|_greater frost_]], [[srd/pf2e/compendium/equipment/runes/shock-greater|_greater shock_]], or [[srd/pf2e/compendium/equipment/runes/wounding|_wounding_]] rune until the end of their next turn. _Healing_ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) The daemon regains 8d8+64 Hit Points."
  - name: "Inherit Soul"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]])"
  - name: "Trigger"
    desc: "The obcisidaemon slays a creature"
  - name: "Effect"
    desc: "The obcisidaemon attempts to draw the creature's soul into their cloak of souls. The triggering creature must attempt a DC 38 Fortitude save. On a failure, its soul is consumed and added to the cloak of souls. If the obcisidaemon's cloak can't hold any more souls, the daemon can release one of the souls as a free action; otherwise, the soul isn't absorbed. Soul Hoarding Obcisidaemons carry some souls for months or even years at a time, choosing never to consume them even when doing so might grant them an advantage in combat."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]] - __7th__ [[srd/pf2e/compendium/spells/rank-3/paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-7/spell-riposte|Spell Riposte]] - __9th__ [[srd/pf2e/compendium/spells/rank-6/disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-9/falling-stars|Falling Stars]] - __10th__ [[srd/pf2e/compendium/spells/rank-9/massacre|Massacre]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 82."
```

```encounter-table
name: Obcisidaemon
creatures:
  - 1: Obcisidaemon
```
