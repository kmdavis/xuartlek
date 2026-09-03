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
    desc: "Perception +26; darkvision, _truesight_"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +22, Deception +26, Intimidation +26, Religion +22, Styx Lore +24"
abilityMods: [6, 6, 4, 3, 5, 7]
abilities_top:
  - name: "Items"
    desc: "_+1 striking bo staff_, _soul gem_"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +21; __Ref__: +23; __Will__: +26 +1 status to all saves vs. magic"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ death effects; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Terrifying Gaze"
    desc: "(aura, divine, emotion, fear, mental, visual) 30 feet. When a creature ends its turn in the aura, it must attempt a DC 30 Will save. If the creature fails, it becomes frightened 2. The creature is then temporarily immune to terrifying gaze (but not Focus Gaze) for 24 hours."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +28 (Magical, parry, reach 10 feet, trip, unholy) __Damage__ 2d8+16 bludgeoning plus 1d6 void and draining strike"
  - name: "Melee"
    desc: "⬻ claw +27 (Agile, finesse, magical, unholy) __Damage__ 3d6+17 slashing plus draining strike"
abilities_bot:
  - name: "Draining Strike"
    desc: "(Divine) When a thanadaemon damages a living creature with a melee Strike, the creature must succeed at a DC 33 Fortitude save or become drained 1. Further damage dealt by the thanadaemon increases the drained condition value by 1 on a failed save, to a maximum of drained 4."
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, visual) The thanadaemon glares at a single creature they can see within 30 feet. The target must immediately attempt a DC 33 Will save against the thanadaemon's terrifying gaze. If the target was already frightened, a failed save causes it to become fleeing for 1d4 rounds; this second effect has the incapacitation trait. After attempting its save, the creature is temporarily immune to this ability until the start of the thanadaemon's next turn."
  - name: "Soul Crush"
    desc: "⬺ (Manipulate)"
  - name: "Requirements"
    desc: "The thanadaemon has a soul gem"
  - name: "Effect"
    desc: "The thanadaemon crushes the soul gem in one hand and gains fast healing 15 for 1 minute. Styx Passage Fees Gliding with eerie ease along the murky River Styx, thanadaemons are only too happy to offer mortals passage aboard their dilapidated skiffs—for a price. Gold is typically an acceptable payment for a thanadaemon's services, though these fiends are well-known for altering the details of arrangements after the fact and may just as likely demand a favor or some esoteric good, such as a _soul gem_, instead of coin."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __4th__ Translocate (at will) - __5th__ Translocate - __6th__ Slow, Vampiric Exsanguination (×2) - __7th__ Execute, Interplanar Teleport (at will; self plus skiff and passengers only; Astral; Ethereal; and unholy planes only), Teleport - __Constant (7th)__ Truesight"
  - name: "Rituals"
    desc: "DC 34 - __2nd__ Create Undead"
sourcebook: "_Monster Core 2_, page 80."
```

```encounter-table
name: Thanadaemon
creatures:
  - 1: Thanadaemon
```
