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
    desc: "Perception +35; darkvision, _truesight_"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +39, Deception +34, Intimidation +36, Religion +32, Warfare Lore +36"
abilityMods: [10, 4, 8, 4, 5, 7]
abilities_top:
  - name: "Items"
    desc: "_+2 greater striking halberd_"
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +35; __Ref__: +29; __Will__: +32 +1 status to all saves vs. magic"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ death effects; __Weaknesses__ holy 20"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Scorched Earth"
    desc: "(aura, divine) 60 feet. Any creature that dies within the aura and isn't drawn into the obcisidaemon's cloak of souls via Inherit Soul must attempt a DC 38 Fortitude save. On a failure, the creature's body (but not its gear) is immediately reduced to a fine smear of ashes."
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _halberd_ +36 (Magical, reach 20 feet, versatile S, unholy) __Damage__ 3d10+23 piercing"
  - name: "Melee"
    desc: "⬻ jaws +34 (Magical, reach 15 feet, unholy) __Damage__ 4d6+20 piercing plus Grab"
abilities_bot:
  - name: "Consume Soul"
    desc: "⬺ (Divine) The obcisidaemon consumes a soul from their cloak to gain one of the following effects. A soul consumed in this way can't be resurrected except by a wish ritual or a similarly powerful effect. _Empower Spell_ The obcisidaemon gains a +2 status bonus to their spell DCs and spell attack modifiers until the end of their next turn. _Empower Weapon_ The obcisidaemon's weapon gains the effects of a _greater flaming_, _greater frost_, _greater shock_, or _wounding_ rune until the end of their next turn. _Healing_ (healing, vitality) The daemon regains 8d8+64 Hit Points."
  - name: "Inherit Soul"
    desc: "⬲ (Divine, incapacitation)"
  - name: "Trigger"
    desc: "The obcisidaemon slays a creature"
  - name: "Effect"
    desc: "The obcisidaemon attempts to draw the creature's soul into their cloak of souls. The triggering creature must attempt a DC 38 Fortitude save. On a failure, its soul is consumed and added to the cloak of souls. If the obcisidaemon's cloak can't hold any more souls, the daemon can release one of the souls as a free action; otherwise, the soul isn't absorbed. Soul Hoarding Obcisidaemons carry some souls for months or even years at a time, choosing never to consume them even when doing so might grant them an advantage in combat."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __4th__ Translocate (at will) - __5th__ Translocate - __6th__ Toxic Cloud - __7th__ Paralyze, Spell Riposte - __9th__ Disintegrate, Falling Stars - __10th__ Massacre - __Constant (10th)__ Truesight"
sourcebook: "_Monster Core 2_, page 82."
```

```encounter-table
name: Obcisidaemon
creatures:
  - 1: Obcisidaemon
```
