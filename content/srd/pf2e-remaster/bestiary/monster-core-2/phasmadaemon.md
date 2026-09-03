---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phasmadaemon"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Phasmadaemon"
level: 17
source: "Monster Core 2"
aon_id: "creature-4308"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4308"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Phasmadaemon"
level: "Creature 17"
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, _truesight_"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +31, Athletics +30, Deception +31, Intimidation +33, Religion +29"
abilityMods: [8, 8, 6, 3, 4, 6]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +31; __Ref__: +26; __Will__: +31 +1 status to all saves vs. magic"
hp: 340
health:
  - name: "HP"
    desc: "340; __Immunities__ death effects, fear; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 35"
  - name: "Unending Terror"
    desc: "Escaping fear near a phasmadaemon is no simple task. Creatures in the phasmadaemon's frightful presence aura don't reduce the value of their frightened condition automatically at the end of their turns. Instead, they must attempt a Will save at the end of their turn against the DC of the effect that caused the condition. On a success, the creature's frightened condition is reduced by 1."
speed: "25 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 (Magical, reach 10 feet, unholy) __Damage__ 3d10+19 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +33 (Agile, magical, reach 10 feet, unholy) __Damage__ 3d8+19 slashing"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d10+9 bludgeoning, DC 35"
  - name: "Consume Fear"
    desc: "⬻ (Emotion, fear, mental)"
  - name: "Requirements"
    desc: "The phasmadaemon has a creature grabbed or restrained; Effect The phasmadaemon feeds on the creature's mortality and innate terror, dealing 6d8 mental damage. The creature must attempt a DC 38 Will save."
  - name: "Critical Success"
    desc: "The creature takes no damage and manages to break free from the phasmadaemon's Grab."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and increases their frightened conditioned by 1, to a maximum of frightened 4."
  - name: "Critical Failure"
    desc: "The creature takes double damage and increases their frightened condition by 2, to a maximum of frightened 4. If the creature is already frightened 4, it must attempt a DC 38 Fortitude saving throw. If it fails, it's reduced to 0 Hit Points and dies. This effect has the death and incapacitation traits."
  - name: "Inescapable Form"
    desc: "The phasmadaemon can Squeeze through tight spaces as if it were a Small creature. While Squeezing, it can move at its full Speed. The phasmadaemon can even Squeeze through spaces that typically fit only a Tiny creature but does so at the standard speed for Squeezing."
  - name: "Rend"
    desc: "⬻ claw Fearful Machinations While daemons don't typically require food, phasmadaemons seem intent on feeding on the emotions, and especially the fears, of mortals. Some believe that the life force and emotions of creatures serves as the fuel for a phasmadaemon's magic, while others suspect that phasmadaemons simply enjoy facing mortals eye-to-eye while feeding, delighting in the fear of their prey's final moments."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __4th__ Translocate (at will), Nightmare (at will) - __5th__ Shadow Blast (×2), Translocate - __6th__ Shadow Blast (×2) - __7th__ Shadow Blast, Vision of Death - __8th__ Mask of Terror - __9th__ Duplicate Foe, Phantasmagoria - __Constant (9th)__ Truesight"
sourcebook: "_Monster Core 2_, page 81."
```

```encounter-table
name: Phasmadaemon
creatures:
  - 1: Phasmadaemon
```
