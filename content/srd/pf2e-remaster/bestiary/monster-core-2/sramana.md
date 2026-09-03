---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sramana"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Sramana"
level: 15
source: "Monster Core 2"
aon_id: "creature-4030"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4030"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sramana"
level: "Creature 15"
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, heed the fettered (imprecise) 120 feet"
languages: "Diabolic, Draconic, Empyrean, Requian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +29, Diplomacy +26, Legal Lore +27, Medicine +27, Religion +29"
abilityMods: [8, 4, 6, 4, 8, 5]
abilities_top:
  - name: "Heed the Fettered"
    desc: "The sramana can detect penitent creatures who wish to atone for their misdeeds, creatures with the soulbound trait, and soul gems as an imprecise sense with a range of 120 feet."
  - name: "Soul-Rescuing Vow"
    desc: "A sramana can use _interplanar teleport_ to teleport near a truly penitent creature, soulbound creature, or soul gem of which they're aware. If they do, they don't need a planar key and arrive 1d20 miles away from the subject. They can also teleport to Nirvana or The Boneyard without a planar key."
  - name: "Items"
    desc: "_+1 striking handwraps of mighty blows_, expanded healer's toolkit, _+2 striking khakkara_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +26; __Ref__: +24; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ confused, fear; __Resistances__ mental 15; __Weaknesses__ unholy 15"
abilities_mid:
  - name: "Aura of Renunciation"
    desc: "(aura, divine, mental) 100 feet. Truly penitent creatures in the sramana's aura are affected by a DC 35 _sanctuary_ spell. If any creature within the aura takes a hostile action, _sanctuary_ ends for only that creature, not for the other creatures in the aura. In addition, soul gems in the aura can't be ingested, consumed, or otherwise used. A creature who attempts to do so becomes sickened 1 unless it succeeds at a DC 37 Fortitude save."
speed: "40 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _khakkara_ +31 (Holy, Shove, two-hand d10, versatile P) __Damage__ 2d6+14 bludgeoning plus 2d6 spirit"
  - name: "Melee"
    desc: "⬻ _fist_ +30 (Agile, Holy, Nonlethal, Unarmed) __Damage__ 2d4+14 bludgeoning plus 2d6 spirit"
abilities_bot:
  - name: "Shelter the Suffering"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The sramana tosses the shawl of their robes into the air, where it expands to protect the suffering. Each truly penitent creature in a 100-foot emanation is affected by an _invisibility_ spell, and the area is affected by the _field of life_ spell, though it affects only penitent creatures and soulbound creatures. These effects last for 1 round but can be sustained for up to 1 hour. Soul Saviors Over the course of helping souls renounce suffering, many sramanas develop alliances with psychopomps, whose goal of returning the lost and trapped to the River of Souls they gladly share. These bonds run so deep that it isn't unusual to find sramana volunteering as legal advocates in the Boneyard's courts."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29 - __Cantrips (8th)__ Daze, Divine Lance, Light, Message, Vitality Lash - __7th__ Calm, Cleanse Affliction, Dispel Magic, Divine Decree, Heal, Interplanar Teleport (at will; see soul-rescuing vow), Planar Seal, Sending - __8th__ Clear Mind, Divine Inspiration, Moment of Renewal, Pinpoint - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 37 - __1st__ Angelic Messenger - __4th__ Atone"
sourcebook: "_Monster Core 2_, page 28."
```

```encounter-table
name: Sramana
creatures:
  - 1: Sramana
```
