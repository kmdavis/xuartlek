---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gylou"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Gylou"
level: 14
source: "Monster Core"
aon_id: "creature-2910"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2910"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gylou"
level: "Creature 14"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; greater darkvision, _truesight_"
languages: "Common, Diabolic, Draconic, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +28, Athletics +28, Arcana +25, Deception +30, Diplomacy +28, Religion +26, Stealth +28"
abilityMods: [4, 8, 4, 5, 6, 8]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +22; __Ref__: +25; __Will__: +28 +1 status to all saves vs. magic"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ fire; __Resistances__ physical 10 (except silver), poison 10; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Reflexive Grab"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature leaves a square within the gylou's reach using a move action or attempts a melee Strike against the gylou"
  - name: "Effect"
    desc: "The gylou lashes out with a tentacle, attempting to Grapple the triggering creature. If the triggering Strike was with a melee weapon, the attacking creature can Release the weapon to cause the gylou to automatically fail the Athletics check."
speed: "35 feet, climb 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +30 (Finesse, Magical, reach 10 feet, Unholy) __Damage__ 3d12+12 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ claw +30 (Agile, Finesse, Magical, Unholy) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The gylou adopts the appearance of any Small or Medium humanoid. This doesn't change their Speed or the attack and damage modifiers of their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Encage in Tentacles"
    desc: "⬻ (Attack)"
  - name: "Requirements"
    desc: "The gylou has a Medium or smaller creature grabbed or restrained"
  - name: "Effect"
    desc: "The gylou transfers the grabbed creature into their lower body's net of encaging tentacles, freeing their limbs and tentacles to make Strikes. This has the same effects as Swallow Whole (Medium, 2d12+12 bludgeoning, Rupture 30; page 360), except the encaged creature is not at risk of suffocation, and the gylou can bring the encaged creature with them when they cast _translocate_. A gylou can have only one creature encaged at a time."
  - name: "Indispensable Savvy"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The gylou attempts a skill check but hasn't rolled yet"
  - name: "Effect"
    desc: "The gylou demonstrates a preternatural ability for the task at hand. They use their Deception modifier for the triggering check and for all skill checks using the same skill thereafter until the next time the gylou uses this ability or until 24 hours have passed, whichever happens first."
spellcasting:
  - name: "Rituals"
    desc: "DC 36 - __1st__ Diabolic Pact"
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28 - __4th__ Charm (×3), Translocate (at will), Enthrall (at will) - __5th__ Illusory Object (at will), Slither, Translocate - __7th__ Dispel Magic, Dominate - __Constant (7th)__ Truesight"
sourcebook: "_Monster Core_, page 91."
```

```encounter-table
name: Gylou
creatures:
  - 1: Gylou
```
