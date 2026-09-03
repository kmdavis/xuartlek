---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eseneth"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Eseneth"
level: 17
source: "Monster Core 2"
aon_id: "creature-4525"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4525"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Eseneth"
level: "Creature 17"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, lifesense 120 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +33, Boneyard Lore +29, Medicine +31, Sewing Lore +35, Stealth +33"
abilityMods: [8, 8, 5, 6, 4, 2]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +28; __Ref__: +32; __Will__: +27"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ death effects, disease; __Resistances__ poison 15, void 15"
abilities_mid:
  - name: "Sudden Stitch"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the eseneth's reach successfully Strikes the eseneth"
  - name: "Effect"
    desc: "The eseneth attempts an Athletics check to Grapple the triggering creature."
speed: "25 feet, fly 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ spirit needle +33 (Magical) __Damage__ 3d10+14 piercing plus shepherd's touch and Improved Grab"
  - name: "Ranged"
    desc: "⬻ spirit needle +33 (Magical, thrown 30 feet) __Damage__ 3d10+14 piercing plus shepherd's touch"
abilities_bot:
  - name: "Mend Soul"
    desc: "⬻ (Manipulate)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The eseneth restores 25 HP to itself or an incorporeal creature it has grabbed."
  - name: "Seize Soul"
    desc: "⬻ (Attack, Incapacitation)"
  - name: "Requirements"
    desc: "The eseneth has a corporeal creature grabbed or restrained"
  - name: "Effect"
    desc: "The eseneth tries to yank the soul out of the required creature. The eseneth attempts an Athletics check against the target's Fortitude DC."
  - name: "Critical Success"
    desc: "The eseneth grabs the target's soul. The body is released and is paralyzed for 2 rounds. When the body ceases being paralyzed, its soul returns instantly, and the target wakes. The soul—grabbed by the eseneth—is incorporeal, is invisible, has a fly Speed equal to the creature's Speed, and otherwise has all the same statistics. It can't attack, cast spells, or attempt any skill checks that require a physical body other than checks to Escape (DC 38), and it must always maintain line of effect to its body."
  - name: "Success"
    desc: "As critical success, but the paralysis ends after 1 round."
  - name: "Failure"
    desc: "The target remains grabbed or restrained, but its soul remains in its body."
  - name: "Critical Failure"
    desc: "The target is no longer grabbed or restrained."
  - name: "Shepherd's Touch"
    desc: "A psychopomp's Strikes affect incorporeal creatures with the effects of a _ghost touch_ property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to undead."
  - name: "Shred Soul"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The eseneth has an incorporeal creature grabbed or restrained"
  - name: "Effect"
    desc: "The eseneth deals 3d10+14 force damage to the required creature."
  - name: "Spirit Grasp"
    desc: "An eseneth can Grapple incorporeal creatures despite being corporeal. The eseneth uses Athletics to Grapple incorporeal creatures as normal but can't use Athletics for other actions against incorporeal creatures, like Shove or Trip. Spirit Needles An eseneth's spirit needles are composed of the psychopomp's essence. The needles form and dissipate at the eseneth's will and exist only as long as the eseneth does."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __2nd__ Invisibility (at will; self only) - __4th__ Translocate (at will) - __8th__ Spirit Blast (×3) - __Constant (4th)__ Unfettered Movement"
sourcebook: "_Monster Core 2_, page 265."
```

```encounter-table
name: Eseneth
creatures:
  - 1: Eseneth
```
