---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zuhra Shuyookh"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Zuhra Shuyookh"
level: 13
source: "Rage of Elements"
aon_id: "creature-2656"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2656"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Zuhra Shuyookh"
level: "Creature 13"
size: "Large"
trait_01: "Elemental"
trait_02: "Genie"
trait_03: "Metal"
trait_04: "Rare"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision"
languages: "Common, Talican; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +27, Athletics +24, Crafting +26, Deception +26, Intimidation +24, Performance +28, Society +22"
abilityMods: [5, 6, 8, 5, 4, 7]
abilities_top:
  - name: "Items"
    desc: "_+2 striking spiked chain_"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +29; __Ref__: +23; __Will__: +21"
hp: 212
health:
  - name: "HP"
    desc: "212; __Resistances__ electricity 10"
abilities_mid:
  - name: "Conductive Redirection"
    desc: "⬲ (arcane, concentrate, electricity)"
  - name: "Trigger"
    desc: "The zuhra is hit by an attack, spell, or effect that deals electricity damage"
  - name: "Effect"
    desc: "The zuhra conducts the electricity through their body, taking damage as normal, and redirecting a bolt at one target within 30 feet that they can see. The zuhra makes a ranged attack roll with a +27 modifier against the target's AC. On a hit or critical hit, the target takes electricity damage equal to the full damage of the triggering effect."
  - name: "Magnetic Field"
    desc: "(arcane, aura, metal) 10 feet. All squares in the aura are difficult terrain for creatures wearing metal armor or made of metal. Strikes with metallic weapons made by or against creatures in this aura take a –2 status penalty to the attack roll. Zuhras ignore these effects."
speed: "30 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spiked chain_ +27 (Disarm, Finesse, Magical, reach 15 feet, Trip) __Damage__ 2d8+11 slashing plus 1d12 electricity"
  - name: "Melee"
    desc: "⬻ hand blade +25 (Agile, Finesse, Magical, reach 15 feet) __Damage__ 2d4+11 slashing plus 4d4 persistent bleed"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Arcane, Concentrate, Polymorph) The zuhra transforms into a Small or Medium metal elemental or animal. This doesn't affect the zuhra's statistics, but it could change the damage type of their Strikes."
  - name: "Magnetic Reposition"
    desc: "⬻ (Arcane)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The shuyookh targets any number of creatures affected by their magnetic field, and moves each target 10 feet in a direction the zuhra chooses. Each target can resist being moved if it succeeds at a DC 32 Fortitude save."
  - name: "Magnetic Storm"
    desc: "⬽ (Arcane)"
  - name: "Requirements"
    desc: "The shuyookh's magnetic field is active"
  - name: "Effect"
    desc: "The shuyookh electromagnetically flings razor-sharp metal scraps. Each creature in a 30-foot emanation takes 8d6 slashing damage and 3d12 electricity damage, with a DC 32 basic Fortitude save. The shuyookh's magnetic field is deactivated for 1d4 rounds."
  - name: "Mercurial Wish"
    desc: "(Downtime)"
  - name: "Frequency"
    desc: "three times per year"
  - name: "Effect"
    desc: "The shuyookh conducts a _wish_ ritual for the benefit of a mortal, requiring no cost or secondary casters. The shuyookh's result is a success if they succeed at a DC 5 flat check or a failure if not. The shuyookh attempts to fulfill the wish in a way that creates an unstable or impermanent benefit."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 32, attack +24 - __Cantrips (7th)__ Detect Magic - __5th__ Invisibility (×2), Magnetic Acceleration (at will), Magnetic Attraction (at will) - __6th__ Mercurial Stride, Wall of Metal - __7th__ Clad in Metal (can choose uncommon and rare metals), Enthrall, Interplanar Teleport (at will; to Astral Plane, Elemental Planes, or the Universe only), Weapon Storm - __Constant (5th)__ Truespeech"
sourcebook: "_Rage of Elements_, page 161."
```

```encounter-table
name: Zuhra Shuyookh
creatures:
  - 1: Zuhra Shuyookh
```
