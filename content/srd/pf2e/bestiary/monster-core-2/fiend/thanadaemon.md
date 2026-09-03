---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thanadaemon"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Thanadaemon"
level: 13
source: "Monster Core 2"
aon_id: "creature-4306"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4306"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Thanadaemon"
level: "Creature 13"
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +22, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/lore|Styx Lore]] +24"
abilityMods: [6, 6, 4, 3, 5, 7]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/club/bo-staff|bo staff]]_, _soul gem_"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +21; __Ref__: +23; __Will__: +26 +1 status to all saves vs. magic"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Terrifying Gaze"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a creature ends its turn in the aura, it must attempt a DC 30 Will save. If the creature fails, it becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2. The creature is then temporarily immune to terrifying gaze (but not Focus Gaze) for 24 hours."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/parry|parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d8+16 bludgeoning plus 1d6 void and draining strike"
  - name: "Melee"
    desc: "⬻ claw +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d6+17 slashing plus draining strike"
abilities_bot:
  - name: "Draining Strike"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) When a thanadaemon damages a living creature with a melee Strike, the creature must succeed at a DC 33 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1. Further damage dealt by the thanadaemon increases the drained condition value by 1 on a failed save, to a maximum of drained 4."
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The thanadaemon glares at a single creature they can see within 30 feet. The target must immediately attempt a DC 33 Will save against the thanadaemon's terrifying gaze. If the target was already [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]], a failed save causes it to become [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] for 1d4 rounds; this second effect has the [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] trait. After attempting its save, the creature is temporarily immune to this ability until the start of the thanadaemon's next turn."
  - name: "Soul Crush"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The thanadaemon has a soul gem"
  - name: "Effect"
    desc: "The thanadaemon crushes the soul gem in one hand and gains fast healing 15 for 1 minute. Styx Passage Fees Gliding with eerie ease along the murky River Styx, thanadaemons are only too happy to offer mortals passage aboard their dilapidated skiffs—for a price. Gold is typically an acceptable payment for a thanadaemon's services, though these fiends are well-known for altering the details of arrangements after the fact and may just as likely demand a favor or some esoteric good, such as a _soul gem_, instead of coin."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-3/slow|Slow]], [[srd/pf2e/compendium/spells/rank-6/vampiric-exsanguination|Vampiric Exsanguination]] (×2) - __7th__ [[srd/pf2e/compendium/spells/rank-7/execute|Execute]], [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (at will; self plus skiff and passengers only; Astral; Ethereal; and unholy planes only), [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 34 - __2nd__ [[srd/pf2e/compendium/spells/rituals/create-undead|Create Undead]]"
sourcebook: "_Monster Core 2_, page 80."
```

```encounter-table
name: Thanadaemon
creatures:
  - 1: Thanadaemon
```
