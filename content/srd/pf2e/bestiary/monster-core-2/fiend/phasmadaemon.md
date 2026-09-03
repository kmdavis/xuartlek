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
    desc: "Perception +29; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +31, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +33, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +29"
abilityMods: [8, 8, 6, 3, 4, 6]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +31; __Ref__: +26; __Will__: +31 +1 status to all saves vs. magic"
hp: 340
health:
  - name: "HP"
    desc: "340; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet, DC 35"
  - name: "Unending Terror"
    desc: "Escaping fear near a phasmadaemon is no simple task. Creatures in the phasmadaemon's frightful presence aura don't reduce the value of their [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition automatically at the end of their turns. Instead, they must attempt a Will save at the end of their turn against the DC of the effect that caused the condition. On a success, the creature's frightened condition is reduced by 1."
speed: "25 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d10+19 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d8+19 slashing"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d10+9 bludgeoning, DC 35"
  - name: "Consume Fear"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Requirements"
    desc: "The phasmadaemon has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]; Effect The phasmadaemon feeds on the creature's mortality and innate terror, dealing 6d8 mental damage. The creature must attempt a DC 38 Will save."
  - name: "Critical Success"
    desc: "The creature takes no damage and manages to break free from the phasmadaemon's Grab."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and increases their [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] conditioned by 1, to a maximum of frightened 4."
  - name: "Critical Failure"
    desc: "The creature takes double damage and increases their frightened condition by 2, to a maximum of frightened 4. If the creature is already frightened 4, it must attempt a DC 38 Fortitude saving throw. If it fails, it's reduced to 0 Hit Points and dies. This effect has the [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] traits."
  - name: "Inescapable Form"
    desc: "The phasmadaemon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]] through tight spaces as if it were a Small creature. While Squeezing, it can move at its full Speed. The phasmadaemon can even Squeeze through spaces that typically fit only a Tiny creature but does so at the standard speed for Squeezing."
  - name: "Rend"
    desc: "⬻ claw Fearful Machinations While daemons don't typically require food, phasmadaemons seem intent on feeding on the emotions, and especially the fears, of mortals. Some believe that the life force and emotions of creatures serves as the fuel for a phasmadaemon's magic, while others suspect that phasmadaemons simply enjoy facing mortals eye-to-eye while feeding, delighting in the fear of their prey's final moments."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/nightmare|Nightmare]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]] (×2), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]] (×2) - __7th__ [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]], [[srd/pf2e/compendium/spells/rank-4/vision-of-death|Vision of Death]] - __8th__ [[srd/pf2e/compendium/spells/rank-7/mask-of-terror|Mask of Terror]] - __9th__ [[srd/pf2e/compendium/spells/rank-7/duplicate-foe|Duplicate Foe]], [[srd/pf2e/compendium/spells/rank-9/phantasmagoria|Phantasmagoria]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 81."
```

```encounter-table
name: Phasmadaemon
creatures:
  - 1: Phasmadaemon
```
