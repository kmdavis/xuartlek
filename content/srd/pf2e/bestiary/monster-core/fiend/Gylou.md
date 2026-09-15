---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2910"
socialImage: og-image.png
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
    desc: "+28; greater darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +25, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +30, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +26, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +28"
abilityMods: [4, 8, 4, 5, 6, 8]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +22; __Ref__: +25; __Will__: +28 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Resistances__ physical 10 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 10"
abilities_mid:
  - name: "Reflexive Grab"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature leaves a square within the gylou's reach using a [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] action or attempts a melee Strike against the gylou"
  - name: "Effect"
    desc: "The gylou lashes out with a tentacle, attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] the triggering creature. If the triggering Strike was with a melee weapon, the attacking creature can Release the weapon to cause the gylou to automatically fail the [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] check."
speed: "35 feet, climb 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d12+12 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The gylou adopts the appearance of any Small or Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't change their Speed or the attack and damage modifiers of their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Encage in Tentacles"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]])"
  - name: "Requirements"
    desc: "The gylou has a Medium or smaller creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The gylou transfers the grabbed creature into their lower body's net of encaging tentacles, freeing their limbs and tentacles to make Strikes. This has the same effects as Swallow Whole (Medium, 2d12+12 bludgeoning, Rupture 30; page 360), except the encaged creature is not at risk of suffocation, and the gylou can bring the encaged creature with them when they cast [[srd/pf2e/compendium/spells/rank-4/Translocate|_translocate_]]. A gylou can have only one creature encaged at a time."
  - name: "Indispensable Savvy"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The gylou attempts a skill check but hasn't rolled yet"
  - name: "Effect"
    desc: "The gylou demonstrates a preternatural ability for the task at hand. They use their [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] modifier for the triggering check and for all skill checks using the same skill thereafter until the next time the gylou uses this ability or until 24 hours have passed, whichever happens first."
spellcasting:
  - name: "Rituals"
    desc: "DC 36 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28 - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-3/Enthrall|Enthrall]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-5/Slither|Slither]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __7th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core_, page 91."
```

```encounter-table
name: Gylou
creatures:
  - 1: Gylou
```
